# Chaos Redux repository tools

This directory contains maintained repository tooling that supports more than one implementation surface, protects a shared contract, or is required by the Codex, Qoder, Cursor, spreadsheet, map, asset, or 3D workflows.

It is not a storage area for generated output, temporary experiments, editor state, Python bytecode, event-local evidence, or copied dependencies that can be resolved from a lock file.

## Retention rules

A tool belongs here when at least one of these conditions is true:

- it generates or validates a shared source-of-truth artifact used by several systems or events;
- it enforces a repository-wide contract that ordinary source inspection cannot safely replace;
- it is a required runtime adapter, wrapper, synchronizer, exporter, or packaging entry point;
- it is a specialized validator for an active shared registry whose consumers span multiple event packages.
- it is a maintained regression test for current behavior, with meaningful failure assertions and an identifiable owner or caller.

A file belongs in ignored `.tmp/<task>/` instead when it is a one-time migration or repair, a superseded generator, a fixed-unit runner, event-local evidence with no continuing validation role, a temporary report, or an unreferenced preset.
Do not create `.tools/tmp/` or a permanent `.tools/archive/` for that work.
A maintained regression test can cover one event when it protects a current, nontrivial contract; its name or date alone does not make it disposable.

Before retiring a tool, search its filename, module name, output signatures, and generated-file headers across `AGENTS.md`, `CLAUDE.md`, `.claude/`, docs, configuration, runtime source, and Git history. An old audit mention alone does not make a helper maintained; check whether a current command, import, test, or workflow still needs it. Preserve a genuinely active dependency until its callers have been updated.

## Supported tools

### Catalog and project packaging

- `export_event_catalog_csv.py` exports the `Events`, `Clusters`, and `Scenarios` sheets from the authoritative `docs/spreadsheets/chaos_redux_events_catalog.xlsx` workbook. Never edit the exported CSV files directly.
- `package_chatgpt_project_sources.py` builds the curated ChatGPT project-source bundle and places `all-project-sources.zip` beside the loose files in the output folder. `package_chatgpt_project_sources.bat` is the Windows launcher and opens the finished package by default.

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

- `sync/sync_agents.py` generates the Codex, Qoder, Cursor, and opencode subagent definitions, their agent maps, the Claude Code agent map, and the `.agents/skills/` links from the canonical Claude Code definitions in `.claude/agents/` and `.claude/skills/`.
- `sync/agent_profiles.json` holds the model routing table, the tier-to-model mapping per runtime, authority classes, and Codex nickname candidates.
- `sync/sync_read_limits.py` applies the shared read and output budgets from `sync/read_limits.json`.

Run the generator after changing a subagent definition or adding a skill, and verify the model routing by reading the outputs back:

```powershell
python .tools/sync/sync_agents.py
python .tools/sync/sync_agents.py --verify
```

Do not hand-edit generated Codex, Qoder, Cursor, or opencode agent files.
`CLAUDE.md` is edited directly, and `AGENTS.md` carries the same rules for the other runtimes.

### Universal formable-state tooling

- `generate_formable_state_puzzle_runtime.mjs` discovers complete manifests and emits the shared runtime surfaces.

This is the sole supported formable-state tool in `.tools`. It rebuilds the shared GFX, GUI, scripted-GUI, scripted-localisation, and localisation outputs from complete manifests under `docs/formables/state_puzzles/`.

The former geometry, registry, and consumer compilers are retained locally under `.tmp/archive/`, with their tracked originals recoverable from Git history. They are not normal maintenance commands and must be reviewed against current inputs before a map revision or new consumer is compiled.

### Offline Paradox wiki snapshot

- `wiki/sync_wiki_snapshot.py` regenerates `paradox_wiki/` from the live Hearts of Iron IV wiki. It is the only supported way to refresh that reference; hand-editing a page is lost on the next refresh.
- `wiki/verify_wiki_snapshot.py` is the read-only acceptance check for the result.

`AGENTS.md` names `paradox_wiki/` as the required modding reference, so the two commands run as a pair whenever the wiki moves:

```powershell
python -B .tools/wiki/sync_wiki_snapshot.py
python -B .tools/wiki/verify_wiki_snapshot.py
```

The sync never launches Hearts of Iron IV and never claims engine evidence. Its contract, options, page set, and downstream mirror step are in `wiki/README.md`. Commit the refreshed snapshot and any wiki-file references it changes together.

### Repository-wide static audits

These audits answer source-only questions across the whole mod. They never launch Hearts of Iron IV and never claim live, engine, or render evidence. Each one is read-only; only `reindent_script_files.py` writes, and only with `--apply`.

- `audit_localisation_static.py` checks every English localisation file for parse errors, BOM and header damage, duplicate keys, keys that no script binds, and events whose title or description key is missing. It reads each event's actual `title =` / `desc =` binding, so it does not assume the `<id>.t` convention, and it exempts `hidden = yes` events. It also lists flags checked in a displayed decision, mission, or focus requirement, directly or through the scripted triggers those requirements call, that have no localisation key and would show their raw identifier in the tooltip. The event-key check has a positive control: deleting a known key must make it appear.
- `audit_asset_wiring_static.py` checks sprite registration against use. It reports `GFX_` names referenced but registered nowhere here or in vanilla, sprite registrations with no reference outside their own definition file, and texture or mesh references with no backing file. Asset references are resolved by filename, because Clausewitz searches the model folders recursively.
- `reindent_script_files.py` enforces the repository's tab-indentation rule ("Indent script blocks with tabs"). It converts only the leading whitespace run of a line, preserves line endings and the UTF-8 BOM, and leaves already-tabbed lines alone. Run it with `--check` before `--apply`.

```powershell
python .tools/audit_localisation_static.py --json .tmp/loc_audit.json
python .tools/audit_asset_wiring_static.py --json .tmp/asset_audit.json
python .tools/reindent_script_files.py --check
```

Interpretation limits, which matter when reading the output:

- A localisation key reported as unbound is not dead when scripted localisation or a `meta_effect` assembles its name at runtime, or when the engine resolves it by naming convention (an idea `picture`, a decision `icon`, an advisor portrait).
- A sprite reported as unreferenced is likewise a candidate, not proof.
- A missing localisation key and a missing asset file are exact findings and can be acted on directly.

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

The validators read the consolidated Event 006 constant, regional publisher, regional trigger, and support-event registries directly. They are source/static checks only; MCP event, focus, map, probability, GUI-render, and live terminal evidence remain separate acceptance boundaries.

### 3D model pipeline

The `3d_pipeline/` package contains the shared Meshy, Blender, `io_pdx_mesh`, material, verification, and wrapper infrastructure. Its detailed contract and commands are in `3d_pipeline/README.md`.

Keep source, dependency locks, wrappers, reusable tests, and current generated environment evidence. Do not commit virtual environments, Python bytecode, transient process logs, provider secrets, or event-owned model outputs. Event-owned jobs and durable evidence belong under the matching `docs/assets/<owner>/models_3d/` workspace.

## Generated and local-only data

Python bytecode directories, `*.pyc` files, and transient `*.log` files are ignored within `.tools`. Run repository Python tools with `python -B` when practical.

The 3D adapter's `.venv/` is local runtime state and is already ignored by the repository root `.gitignore`. It may remain on a working machine while active, but it is never source and must not be committed. Recreate it from the tracked adapter metadata and lock files when necessary.

Generated reports should be tracked only when another maintained tool or durable handoff consumes them and their provenance is current. Place event-local audit receipts and implementation handoffs in the matching `docs/plans/<event>_plans/` hierarchy, not in `.tools`.

## Temporary and retired tools

Retired generators are kept locally in `.tmp/archive/`; the former `.tools/tmp/` scratch files are in `.tmp/tools_scratch/`.
Fixed-model pilots, unit-specific inspection scripts, and dated audio-repair helpers are in `.tmp/3d_pipeline/`.
These local files are ignored, are not required for a fresh checkout, and are not normal maintenance commands. Tracked originals remain available in Git history.
Retain historical reports and generated-file headers as records of what ran at the time; update active commands and imports instead of rewriting old results.

## Adding or removing a tool

When adding a tool:

1. Confirm that an existing tool or skill-local utility does not already provide the capability.
2. Give it a narrow command-line contract, safe defaults, and a read-only check or dry-run mode when practical.
3. Document its authoritative inputs, generated outputs, dependencies, and destructive behavior here or in a dedicated package README.
4. Reference it from the owning system documentation or skill.
5. Keep generated artifacts and caches out of Git; put one-off helpers in `.tmp/<task>/` rather than promoting them by default.
6. Reuse an existing tool before adding a wrapper or generator. A new permanent tool needs demonstrated recurring use or a required shared entry point; accepting arguments alone is not enough.

When removing a tool:

1. Verify direct references, imports, dynamically constructed commands, generated-file headers, docs, skills, agents, configuration, and historical handoffs.
2. Identify the authoritative replacement or explain why no continuing tool is required.
3. Update active instructions, imports, and dependency records in the same change; preserve historical provenance unchanged.
4. Preserve moved bytes in `.tmp/` and keep required runtime dependencies, locks, and maintained regression tests in place. Do not retain an unused hook solely for hypothetical future use.
