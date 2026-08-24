# Chaos Redux repository tools

This directory contains maintained repository tooling that supports more than one implementation surface, protects a shared contract, or is required by the Codex, Qoder, Cursor, spreadsheet, map, asset, or 3D workflows.

It is not a storage area for generated output, temporary experiments, editor state, Python bytecode, event-local evidence, or copied dependencies that can be resolved from a lock file.

## Retention rules

A tool belongs here when at least one of these conditions is true:

- it generates or validates a shared source-of-truth artifact used by several systems or events;
- it enforces a repository-wide contract that ordinary source inspection cannot safely replace;
- it is a required runtime adapter, wrapper, synchronizer, exporter, or packaging entry point;
- it is a specialized validator for an active shared registry whose consumers span multiple event packages.

A file should be removed or moved out of this directory when it is a one-time migration, a superseded generator, event-local evidence with no continuing validation role, a cached interpreter artifact, a temporary report, or an unreferenced preset.

Before retiring a tool, search its filename, module name, output signatures, and generated-file headers across `AGENTS.md`, `.agents/skills/`, `.codex/`, docs, configuration, runtime source, and Git history. Preserve uncertain or recently active tooling until its owner and replacement are clear.

## Supported tools

### Catalog and project packaging

- `export_event_catalog_csv.py` exports the `Events`, `Clusters`, and `Scenarios` sheets from the authoritative `docs/spreadsheets/chaos_redux_events_catalog.xlsx` workbook. Never edit the exported CSV files directly.
- `package_chatgpt_project_sources.py` builds the curated ChatGPT project-source bundle. `package_chatgpt_project_sources.bat` is the Windows launcher and opens the finished package by default.

Run the catalog exporter after every successful workbook edit:

```powershell
python .tools/export_event_catalog_csv.py
```

Preview or build the ChatGPT source package:

```powershell
python .tools/package_chatgpt_project_sources.py --dry-run
.tools/package_chatgpt_project_sources.bat
```

The default package output is outside the repository under the current user's Downloads folder. The repository-local `.chatgpt_project_sources/` path remains ignored for explicit local overrides.

### Agent-definition synchronization

- `sync/sync_qoder_agents.py` generates Qoder agent definitions from canonical `.codex/agents/*.toml` files.
- `sync/sync_cursor_agents.py` generates Cursor agent definitions and the Cursor agent map from the same canonical TOML files.

Run both after changing a Codex subagent definition:

```powershell
python .tools/sync/sync_qoder_agents.py
python .tools/sync/sync_cursor_agents.py
```

Do not hand-edit generated Qoder or Cursor agent files.

### Universal formable-state tooling

- `generate_formable_state_puzzle_runtime.mjs` discovers complete manifests and emits the shared runtime surfaces.

This is the sole supported formable-state tool in `.tools`. It rebuilds the shared GFX, GUI, scripted-GUI, scripted-localisation, and localisation outputs from complete manifests under `docs/formables/state_puzzles/`.

The former geometry, registry, and consumer compilers are retained under `archive/` as reviewed-build provenance. They are not normal maintenance commands and must be restored and reviewed deliberately before a map revision or new consumer is compiled.

### Event 006 static validators

The maintained Event 006 validators protect the current source contracts without launching Hearts of Iron IV or claiming live execution:

- `audit_event6_allocator.py` checks the anchor-first allocator, package publishers, admission/attestation boundary, reservation groups, exact automatic ladder, SCN-008 ranking, joint ordering, dormant-anchor safety, and retired pre-event surface.
- `audit_event6_country_api.py` checks the broad country API against Event 006, Soviet Collapse, and Africa carrier projections.
- `audit_event6_flags.py` checks normal, medium, and small flag families for every registered Event 006 tag. Pass `--strict` to fail on an incomplete family.
- `audit_event6_scenario_matrix.py` checks all 32 SCN-008 cells and eight edge-case receipts against the scenario source witnesses.
- `audit_event6_form16.py` checks the admitted ARM/GEO/AZR FORM-16 contract, exact anchors, consent/refusal, mutation, rollback, and cleanup gates.
- `audit_event6_gui_matrix.py` checks the Statehood Ledger semantic source matrix and its static/animated sibling registrations. It does not claim a runtime GUI render.

Run the bounded source checks from the mod root with `python -B`:

```powershell
python -B .tools/audit_event6_allocator.py
python -B .tools/audit_event6_country_api.py
python -B .tools/audit_event6_flags.py --strict
python -B .tools/audit_event6_scenario_matrix.py
python -B .tools/audit_event6_form16.py
python -B .tools/audit_event6_gui_matrix.py
```

The validators read the consolidated Event 006 constant and support-event registries directly. They are source/static checks only; MCP event, focus, map, probability, GUI-render, and live terminal evidence remain separate acceptance boundaries.

### 3D model pipeline

The `3d_pipeline/` package contains the shared Meshy, Blender, `io_pdx_mesh`, material, verification, and wrapper infrastructure. Its detailed contract and commands are in `3d_pipeline/README.md`.

Keep source, dependency locks, wrappers, reusable tests, and current generated environment evidence. Do not commit virtual environments, Python bytecode, transient process logs, provider secrets, or event-owned model outputs. Event-owned jobs and durable evidence belong under the matching `docs/assets/<owner>/models_3d/` workspace.

## Generated and local-only data

Python bytecode directories, `*.pyc` files, and transient `*.log` files are ignored within `.tools`. Run repository Python tools with `python -B` when practical.

The 3D adapter's `.venv/` is local runtime state and is already ignored by the repository root `.gitignore`. It may remain on a working machine while active, but it is never source and must not be committed. Recreate it from the tracked adapter metadata and lock files when necessary.

Generated reports should be tracked only when another maintained tool or durable handoff consumes them and their provenance is current. Place event-local audit receipts and implementation handoffs in the matching `docs/plans/<event>_plans/` hierarchy, not in `.tools`.

## Archive

Retired, event-specific, and one-off generation scripts are preserved under `archive/` for provenance and possible future recovery. They are not supported repository tools, are not part of normal validation, and must not be cited as current completion proof without a fresh review against current source.

## Adding or removing a tool

When adding a tool:

1. Confirm that an existing tool or skill-local utility does not already provide the capability.
2. Give it a narrow command-line contract, safe defaults, and a read-only check or dry-run mode when practical.
3. Document its authoritative inputs, generated outputs, dependencies, and destructive behavior here or in a dedicated package README.
4. Reference it from the owning system documentation or skill.
5. Keep generated artifacts and caches out of Git.

When removing a tool:

1. Verify direct references, imports, dynamically constructed commands, generated-file headers, docs, skills, agents, configuration, and historical handoffs.
2. Identify the authoritative replacement or explain why no continuing tool is required.
3. Update active instructions and generated-output provenance in the same change.
4. Leave uncertain future hooks in place and document the unresolved owner instead of deleting them.
