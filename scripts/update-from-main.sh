#!/usr/bin/env bash

set -euo pipefail

echo "==> Updating from main (safe mode)"

REMOTE="origin"
MAIN_BRANCH="main"

error() {
  echo "Error: $*" >&2
  exit 1
}

command -v git >/dev/null 2>&1 || error "git not found in PATH"
git rev-parse --is-inside-work-tree >/dev/null 2>&1 || error "Not a git repository"

REPO_ROOT=$(git rev-parse --show-toplevel)
cd "$REPO_ROOT"

git remote get-url "$REMOTE" >/dev/null 2>&1 || error "Remote '$REMOTE' is not configured"
git fetch --prune "$REMOTE"
git ls-remote --exit-code "$REMOTE" "$MAIN_BRANCH" >/dev/null 2>&1 || error "Remote branch '$REMOTE/$MAIN_BRANCH' not found"

CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
echo "Current branch: $CURRENT_BRANCH"

BACKUP_BRANCH="backup/${CURRENT_BRANCH}-$(date +%Y%m%d-%H%M%S)"
git branch "$BACKUP_BRANCH" || true
echo "Created safety backup branch: $BACKUP_BRANCH"

STASH_CREATED=false
STASH_REF=""
STASH_MSG="update-from-main-on-${CURRENT_BRANCH}-$(date +%Y-%m-%d-%H%M%S)"

if [ -z "$(git status --porcelain=v1)" ]; then
  echo "No local changes to stash."
else
  echo "Stashing local changes..."
  git stash push -u -m "$STASH_MSG"
  STASH_CREATED=true
  STASH_REF="stash@{0}"
  echo "Stashed local changes as: $STASH_MSG (Ref: $STASH_REF)"
fi

if ! git show-ref --verify --quiet "refs/heads/$MAIN_BRANCH"; then
  git branch "$MAIN_BRANCH" "$REMOTE/$MAIN_BRANCH"
fi

git checkout "$MAIN_BRANCH"

set +e
git pull --ff-only "$REMOTE" "$MAIN_BRANCH"
PULL_EXIT=$?
set -e

if [ $PULL_EXIT -ne 0 ]; then
  echo "---"
  echo "Your 'main' branch has conflicts with remote."
  echo "Your work is safe in backup branch: $BACKUP_BRANCH"
  if [ "$STASH_CREATED" = true ]; then
      git stash apply "$STASH_REF" || true
  fi
  exit 1
fi

if [ "$CURRENT_BRANCH" != "$MAIN_BRANCH" ]; then
  git checkout "$CURRENT_BRANCH"
  echo "Merging latest '$MAIN_BRANCH' into '$CURRENT_BRANCH'..."

  set +e
  git merge --no-ff --no-edit "$MAIN_BRANCH"
  MERGE_EXIT=$?
  set -e
  if [ $MERGE_EXIT -ne 0 ]; then
    echo "---"
    echo "Merge conflicts detected."
    echo "Your work is safe in backup branch: $BACKUP_BRANCH"
    exit 1
  fi
  echo "Merge successful."
fi

if [ "$STASH_CREATED" = true ]; then
  echo "Re-applying stashed changes..."
  set +e
  git stash apply "$STASH_REF"
  APPLY_EXIT=$?
  set -e

  if [ $APPLY_EXIT -ne 0 ]; then
    echo "---"
    echo "Stash conflicts detected."
    echo "Your work is safe. Stash ref: $STASH_REF"
    exit 1
  fi
  echo "Reapplied stashed changes successfully."
fi

printf "\n"
echo "Current branch: $(git rev-parse --abbrev-ref HEAD)"
printf "\n"
echo "Recent history:"
git log --oneline --graph --decorate -n 10
printf "\n"
echo "Status:"
git status -sb

printf "\n==> Done\n"

exit 0
