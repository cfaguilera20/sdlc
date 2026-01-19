.PHONY: help \
	run-init run-init-noid \
	validate-run validate-json \
	split-bundle split-bundle-new-run \
	materialize \
	features-init features-import-backlog features-next features-next-claim features-set-status features-list \
	cursor-sync

help:
	@echo ""
	@echo "SDLC (Cursor-first) helper commands"
	@echo ""
	@echo "Run folder:"
	@echo "  make run-init TICKET=PROJ-123 TITLE='short title'          # creates runs/<...>/"
	@echo "  make run-init-noid TITLE='short title'                     # creates runs/NOID_<...>/"
	@echo ""
	@echo "Validation:"
	@echo "  make validate-run RUN=runs/PROJ-123_slug_YYYYMMDD_HHMMSS    # validates known artifacts in a run folder"
	@echo "  make validate-json SCHEMA=schemas/spec.schema.json FILE=... # validates a single JSON file"
	@echo ""
	@echo "one_message bundle:"
	@echo "  make split-bundle BUNDLE=runs/.../bundle.json RUN=runs/...  # writes ticket_context.json/spec.json/etc"
	@echo "  make split-bundle-new-run BUNDLE=... TICKET=... TITLE=...   # creates run folder + writes artifacts"
	@echo ""
	@echo "Domain scaffolding:"
	@echo "  make materialize FILE=runs/.../01x_domain_scaffold.json     # apply materialize.files[]"
	@echo ""
	@echo "features.json (multi-session):"
	@echo "  make features-init PROJECT_ID=PROJ TITLE='Epic title' OUT=features.json"
	@echo "  make features-import-backlog BACKLOG=runs/.../backlog.json FEATURES=features.json RUN_DIR=runs/..."
	@echo "  make features-next FEATURES=features.json"
	@echo "  make features-next-claim FEATURES=features.json"
	@echo "  make features-set-status FEATURES=features.json ID=PROJ-1 STATUS=done"
	@echo "  make features-list FEATURES=features.json"
	@echo ""
	@echo "Sync prompts/rules for onboarding:"
	@echo "  make cursor-sync DEST=\$$HOME/.cursor/sdlc FORCE=1"
	@echo ""
	@echo "Note: Some commands require 'pip install jsonschema' for schema validation."
	@echo ""

run-init:
	@test -n "$(TICKET)" || (echo "Missing TICKET=..."; exit 2)
	@test -n "$(TITLE)" || (echo "Missing TITLE=..."; exit 2)
	@python3 scripts/new_run.py --ticket "$(TICKET)" --title "$(TITLE)"

run-init-noid:
	@test -n "$(TITLE)" || (echo "Missing TITLE=..."; exit 2)
	@python3 scripts/new_run.py --ticket "NOID" --title "$(TITLE)"

validate-run:
	@test -n "$(RUN)" || (echo "Missing RUN=... (runs/<...>)"; exit 2)
	@python3 scripts/validate_run.py "$(RUN)"

validate-json:
	@test -n "$(SCHEMA)" || (echo "Missing SCHEMA=schemas/<name>.schema.json"; exit 2)
	@test -n "$(FILE)" || (echo "Missing FILE=path/to.json"; exit 2)
	@python3 scripts/validate_json_schema.py "$(SCHEMA)" "$(FILE)"

split-bundle:
	@test -n "$(BUNDLE)" || (echo "Missing BUNDLE=path/to/bundle.json"; exit 2)
	@test -n "$(RUN)" || (echo "Missing RUN=runs/<...>"; exit 2)
	@python3 scripts/split_one_message_bundle.py "$(BUNDLE)" "$(RUN)"

split-bundle-new-run:
	@test -n "$(BUNDLE)" || (echo "Missing BUNDLE=path/to/bundle.json"; exit 2)
	@test -n "$(TICKET)" || (echo "Missing TICKET=..."; exit 2)
	@test -n "$(TITLE)" || (echo "Missing TITLE=..."; exit 2)
	@python3 scripts/split_one_message_bundle.py "$(BUNDLE)" --ticket "$(TICKET)" --title "$(TITLE)"

materialize:
	@test -n "$(FILE)" || (echo "Missing FILE=path/to/01x_output.json"; exit 2)
	@python3 scripts/apply_materialize.py "$(FILE)"

features-init:
	@test -n "$(PROJECT_ID)" || (echo "Missing PROJECT_ID=..."; exit 2)
	@test -n "$(TITLE)" || (echo "Missing TITLE=..."; exit 2)
	@test -n "$(OUT)" || (echo "Missing OUT=features.json"; exit 2)
	@python3 scripts/features.py init --project-id "$(PROJECT_ID)" --title "$(TITLE)" --out "$(OUT)"

features-import-backlog:
	@test -n "$(BACKLOG)" || (echo "Missing BACKLOG=runs/.../backlog.json"; exit 2)
	@test -n "$(FEATURES)" || (echo "Missing FEATURES=features.json"; exit 2)
	@test -n "$(RUN_DIR)" || (echo "Missing RUN_DIR=runs/<...>"; exit 2)
	@python3 scripts/features.py import-backlog "$(BACKLOG)" --features "$(FEATURES)" --run-dir "$(RUN_DIR)"

features-next:
	@test -n "$(FEATURES)" || (echo "Missing FEATURES=features.json"; exit 2)
	@python3 scripts/features.py next --features "$(FEATURES)"

features-next-claim:
	@test -n "$(FEATURES)" || (echo "Missing FEATURES=features.json"; exit 2)
	@python3 scripts/features.py next --features "$(FEATURES)" --claim

features-set-status:
	@test -n "$(FEATURES)" || (echo "Missing FEATURES=features.json"; exit 2)
	@test -n "$(ID)" || (echo "Missing ID=<feature-id>"; exit 2)
	@test -n "$(STATUS)" || (echo "Missing STATUS=pending|in_progress|done|blocked|cancelled"; exit 2)
	@python3 scripts/features.py set-status --features "$(FEATURES)" --id "$(ID)" --status "$(STATUS)"

features-list:
	@test -n "$(FEATURES)" || (echo "Missing FEATURES=features.json"; exit 2)
	@python3 scripts/features.py list --features "$(FEATURES)"

cursor-sync:
	@if [ -z "$(DEST)" ]; then echo "Missing DEST=... (e.g. \$$HOME/.cursor/sdlc)"; exit 2; fi
	@if [ "$(FORCE)" = "1" ]; then ./scripts/sync_cursor_assets.sh --dest "$(DEST)" --force; else ./scripts/sync_cursor_assets.sh --dest "$(DEST)"; fi


