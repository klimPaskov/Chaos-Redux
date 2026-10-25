# Deterministic tooling, validation and `.tools` organisation plan

Disposition: `accepted and queued`.
Acceptance basis: on 25 October 2026 the user accepted the whole plan and all 13 recommendations in section 12 as written, in the planning chat ("Accept all 13 recommendations as written. Record them in the plan as my decisions and mark the plan accepted and queued.").
Queued because: this session was limited to planning; implementation starts with section 10 step 1 in a later task.
Scope: Chaos Redux first, then the generic Agentic HOI4 Modding package (`C:/Users/klimp/Documents/Projects/agentic-hoi4-modding`), as requested on 25 October 2026.
No script, asset, game content, skill, CI configuration, `CLAUDE.md` or `AGENTS.md` was changed while preparing this plan.
Every number below was measured on 25 October 2026 at commit `d3398692d5` with the working tree as found; the measurement commands are listed in the appendix.

## 1. Summary of current problems

### P1. The repository-wide audits report, but never decide

`audit_localisation_static.py`, `audit_asset_wiring_static.py` and `audit_script_references_static.py` exit `0` whatever they find, have no path filter, and mix exact defects with long candidate lists.
A full run takes 33 s, 27 s and 78 s respectively, so agents either skip them or rerun all three and reason over the output.
The output buries a handful of exact categories under very large candidate lists:

| Audit | Exact categories (all currently 0) | Candidate or advisory lists |
|---|---|---|
| localisation | `parse_errors`, `duplicates`, `missing_bom`, `no_header`, `encoding_artifacts`, `missing_event_content`, `missing_event_roots`, `missing_prefixed`, `exposed_flags`, `exposed_variables`, required implicit keys | 21,589 unbound keys, 1,874 advisory implicit keys, 1,162 expanded scripted triggers |
| asset wiring | `missing_files`, `missing_vanilla_files`, `unresolved_refs`, `implicit_missing` | 3,797 unreferenced registrations (3,545 of them suppressed as implicit) |
| script references | none are exact | 6,300 dead and 2,007 dynamic definition candidates (5,790 of the dead are scripted triggers), 330 flags checked but never set, 9,369 set but never checked, 92 exact and 326 parametric clone groups |

Because every exact category is at zero today, they can become blocking checks with no clean-up first.
The candidate lists are useful worklists for `chaos-redux-codebase-cleanup` and must stay non-blocking.

### P2. Several explicit repository rules are enforced only by reading

`CLAUDE.md` rules such as "never use `<=` or `>=`", "no `:0` localisation keys" and "no unary `-` on variable tokens" have no mechanical check, so every agent re-reads files to satisfy them.
A scan on 25 October found zero violations of each, so a blocking check would cost nothing to adopt and would stop regressions.
`report_colour_audit.py`, which the `chaos-redux-events` skill requires after every report or news text edit, finds one colour-bearing parchment key in `events/038_malta_crusaders.txt` today and still exits `0`.
`reindent_script_files.py --check` would rewrite 9,344 lines in 16 files, and `check_structural_indentation.py --check` reports drift in 188 files; both exit `0`.

### P3. GFX size standards conflict, and the tool's profiles cite a source that no longer exists

`.tools/gfx/gfx.py size --profile` encodes slot sizes from "the explicit October GFX repair plan".
The parent report (`docs/plans/gfx_fix_2026-10/shared_tools_report.md`) names the accepted source as `C:/Users/klimp/Videos/chaos_redux_trailer/records/gfx_review/gfx_fix_plan.md`, which is no longer present.
The same sizes appear differently in `.claude/skills/chaos-redux-event-assets/SKILL.md` ("Standard HOI4 asset sizes"), and both differ from vanilla in places:

| Family | Skill table | `gfx.py` profile | Installed vanilla (dominant / total) | Chaos Redux today |
|---|---|---|---|---|
| Focus | 94x86 | 94x86, 2 px margin | 100x88 (2,680 / 2,951) | 94x86 (3,342), 100x88 (714) |
| Decision icon | 32x32 | 34x34, 2 px | 33x32 (179 / 518) | 32x32 (1,722), 33x32 (242) |
| Decision category small icon | not listed | 52x40, 3 px | 52x40 (94) | 52x40 (120) |
| Decision category picture | not listed | not profiled | 114x101 (130) | 114x101 (148) |
| Idea | 64x64 | 64x64, 2 px | 65x67 (1,639), 60x68 (1,121), 64x64 (530) | 64x64 (702), 60x68 (169) |
| Report event picture | 210x176 | 210x176 | 210x176 (532) | 210x176 (751) |
| News event picture | 397x153 | 397x153 | 397x153 (233) | 397x153 (211) |
| Flags | 82x52, 41x26, 10x7 | not profiled | 2,202 / 2,203 per folder | 82x52 (1,289) plus 4 misfiled, see P4 |
| Achievement | 64x64 | not profiled | 64x64 (882 / 882) | 64x64 (2,145) |
| Division counter large / small | not listed | 76x42 / 30x12 per frame, 2 frames | 152x42 (111 / 115) / 60x12 (83 / 83) | 152x42 (103) |
| Technology medium | 132x52 | not profiled | 146x54 (269), 131x52 (55) | not surveyed |

Flags, achievements, counters, the decision category sizes and report/news pictures agree across every source.
Focus, decision and idea sizes do not, so a blocking size check for those families would encode a guess (see decisions D1–D3).
The literal alpha rule "subject mean alpha below 200 is a finding" also fires on vanilla's own antialiased infantry counters (162.3 and 164.2), which the tool's report already acknowledges.

### P4. Mechanical asset rules are written as manual steps

The flag rules in `references/event-images-and-flags.md` ask agents to run `file` and compare three folders by eye.
Nothing checks that `.gfx` frame counts divide the texture width.
A quick read-only scan for this plan found three concrete candidates that no current tool reports:

- `interface/countrystateview.gfx` declares `noOfFrames = 35` for `gfx/interface/buildings/building_icon_strip.dds`, whose width is 1,656 px (47.31 px per frame). Vanilla's strip is 1,426 px with 31 frames (exactly 46 px), and 1,656 = 36 × 46, so the mod strip probably contains 36 frames. This needs owner review before any change.
- `DHR_democratic.tga` and `DHR_neutrality.tga` are top-origin TGAs in all three flag folders, which the flag rule forbids. Vanilla itself ships 5 top-origin flags out of 2,203, so the rule's engine basis should be confirmed before the check blocks.
- `gfx/flags/route_black_apostolate_{medium,small}.tga` and `route_herald_of_zol_{medium,small}.tga` sit in the normal flag folder at medium and small sizes. They are untracked and referenced nowhere, so they are probably another session's unfinished output; the flag-ladder check would catch this before commit.

Some runtime DDS files use the `DX10` header (for example `gfx/interface/chaosx_settings_bg.dds`) and Pillow cannot decode four idea textures.
These are established, working UI assets, so a format check must parse headers itself and must not treat `DX10` or Pillow decode failure as a defect.

### P5. Tests are scattered and there is no single way to run them

`.tools/` holds 134 tracked files outside `3d_pipeline/`, including 62 top-level `test_*.py` files mixed with the tools themselves, plus `.tools/validation/` (4 Python validators, 24 JS tests) and `.tools/tests/` (2 JS tests).
There is no test discovery command and no documented way to run them; the trace in section 2 found that every test currently passes, but four event validators and audits fail, and 43 Python tests fail under standard discovery because of how they import each other.
`docs/` also tracks 485 scripts, including `docs/testing/*_source_tests.js` and eleven snapshot copies of `blender_worker.py` in 3D recovery drafts.
Those are historical evidence rather than maintained tools, but nothing marks them as such.

### P6. No Python or JavaScript quality tooling exists

There is no `pyproject.toml`, ruff, mypy, pyright, eslint or pre-commit configuration, no CI workflow, and no lint step anywhere.
The maintained Python under `.tools/` and skills is 196 files and about 65,000 lines; 26% of functions carry annotations, 59 functions exceed 100 lines and 242 exceed a McCabe-style complexity of 15.
The worst cases are concentrated: `audit_event6_allocator.py:main` (870 lines), `3d_pipeline/adapter/blender_worker.py:import_animation_action` (603 lines, complexity 131).
The default `python` is 3.9.12, while the 3D adapter declares `requires-python >=3.10` and the generic package's CI uses 3.13; `py -3.13` and `uv` are installed.

### P7. Guidance budgets are already at the limit

`CLAUDE.md` is 59,956 bytes against its 60,000-byte guidance ceiling, so any new section requires an equal relocation.
`sync_read_limits.py --check` exits `1` today: `.claude/skills/chaos-redux-event-assets/SKILL.md` is 58,224 bytes against the 58,000-byte root-skill ceiling.
`CLAUDE.md` and `AGENTS.md` are maintained by hand and differ in 6 lines, some intentionally (runtime-specific image routes and playtest wording); the generic package generates its `AGENTS_template.md` from `CLAUDE_template.md` with `sync_instructions.py` and a replacement table.

### P8. Batch HOI4 script validation exists only inside an agent session

`hoi4_script_validate` (HOI4 Agent Tools 4.1.0) checks syntax, command kinds, declared scopes, player text, event popups and known mistakes for one file, and it worked on `events/chemical_warfare_events.txt` during this audit.
The installed package exposes only `stdio.js`, `http.js` and `setup.js`, so there is no command-line route for a deterministic, repository-wide or changed-files run.

### P9. Shared helpers are duplicated across the two repositories

Five event-asset tools and `save_inspect.py` exist in both repositories as near-identical copies that differ by a few path and label strings, and the 3D pipeline has diverged in both directions (see section 8).

### P10. Tooling policy is split across four places

The rules live in `CLAUDE.md` rules 23–24, the tooling paragraph in section 5, the retention rules in `.tools/README.md`, and the `chaos-redux-codebase-cleanup` skill.
They agree, but none tells an agent to look for an existing check before reasoning through a mechanical question, and no single index says which check answers which question.

## 2. Inventory of existing tools

The trace searched every file name and module stem across `CLAUDE.md`, `AGENTS.md`, skills, agents, `docs/`, `.tools/`, MCP and runtime configuration, `.gitattributes` and imports.
Each tool was then run read-only, with writes outside the system temporary directory blocked.
Reference classes: **A** active instructions (`CLAUDE.md`, skills, agents, `docs/systems`, `.tools` READMEs, MCP configs); **S** source-adjacent contract docs (`common/**/*.md`, `docs/events`, `docs/specs`); **H** historical plans and handoffs only; **N** no reference; **Imp** imported by another tool.
"Pass" means the documented command exited `0`; for report-only tools that says nothing about findings (see P1).

### 2.1 Repository-wide audits and hygiene

| Tool | Purpose | Refs | Result | Action | Reason |
|---|---|---|---|---|---|
| `audit_localisation_static.py` | Localisation integrity and implicit keys | A | exit 0, exact categories all 0 | **Improve** | Add levels, `--paths`, `--fail-on`; move to `audits/`; parser to `lib/` |
| `audit_asset_wiring_static.py` | Sprite, texture and mesh wiring | A | exit 0, exact categories all 0 | **Improve** | Same; becomes the registration reader for the new GFX checks |
| `audit_script_references_static.py` | Dead definitions, flags, clones | A | exit 0, review lists only | **Improve** | Same flags; its output stays `review` apart from B5 |
| `report_colour_audit.py` | `§` codes in parchment text | A (events skill) | exit 0 with 1 finding | **Improve** | Non-zero exit and `--paths`; add to README, which omits it |
| `reindent_script_files.py` | Leading spaces to tabs | A | exit 0 while reporting 16 files | **Merge** | Merge with the next row into one `indentation` tool whose `--check` exits `1` |
| `check_structural_indentation.py` | Brace-depth indentation drift | N | exit 0 while reporting 188 files | **Merge** | Overlaps the row above; both carry their own brace walker and BOM constant |
| `check_planning_identifiers.py` | Planning reservations against runtime and workbook | S (`docs/specs/shared_identifier_registry.md`) | pass | **Keep**, document | Protects a shared registry; missing from README |

### 2.2 Generators and synchronisers

| Tool | Purpose | Refs | Result | Action | Reason |
|---|---|---|---|---|---|
| `export_event_catalog_csv.py` | Workbook to CSV exports | A (CLAUDE, AGENTS, xlsx skill) | not run (writes tracked CSVs) | **Improve** | Add `--check` (A4) |
| `generate_formable_state_puzzle_runtime.mjs` | Formable runtime from manifests | A | not run (writes tracked files) | **Improve** | Add `--check` (A4); move to `formables/` |
| `build_event016_transit_state_catalog.py` | Event 016 state catalog | S, Imp by its test | `--check` pass | **Keep**, move | Already has `--check`; belongs with Event 016 tests |
| `package_chatgpt_project_sources.py`, `.bat` | ChatGPT source bundle | A | not run | **Keep**, move | Recurring packaging entry point |
| `sync/sync_agents.py` | Runtime agent mirrors | A | `--verify` pass | **Keep** | Required generator |
| `sync/sync_read_limits.py` | Read budgets | A | `--check` **fails** (event-assets skill 224 bytes over) | **Keep** | Correct failure; fix the skill. Note it rewrites three config files when run without `--check` |
| `wiki/sync_wiki_snapshot.py` | Wiki refresh | A | not run (network) | **Keep** | Only supported refresh route |
| `wiki/verify_wiki_snapshot.py` | Wiki acceptance | A | **fails**: 18 `escape_artifact` findings in 4 pages | **Keep** | Correct failure; repair the snapshot in a separate task |

### 2.3 Asset and live tooling

| Tool | Purpose | Refs | Result | Action | Reason |
|---|---|---|---|---|---|
| `gfx/gfx.py`, `test_gfx.py` | Alpha, size, counter, DDS, defringe, sheets | A (own README), H (2,600+ handoffs) | tests pass | **Improve** | Add `sprites`, `flags`, binary checks and `profiles.json` |
| `live_testing/clausewitz_linux.py` and test | WSL MCP bridge | A | not run | **Keep** | Required runtime adapter; its `/home/klim/...` WSL paths stay as adapter configuration (D13) |
| `3d_pipeline/**` | Meshy, Blender, PDX and texture pipeline | A | not run | **Keep**; document test command | 29 `unittest` tests have no documented run command; it carries three more Clausewitz readers |
| skill `chaos-redux-event-assets/tools/convert_to_dds.py` | Canonical BGRA DDS writer | A (19 refs), Imp | not run | **Keep** | Single canonical writer |
| skill `tools/create_advisor_icon.py` | Advisor card compositor | A | not run | **Improve** | Has its own `write_bgra_dds` at line 802; delegate to the canonical writer |
| skill `tools/extract_portrait_source_crop.py`, `process_achievement_icons.py`, `process_report_event_image.py` | Asset processors | A | not run | **Keep**; report processor gains provenance (B7) | Approved recipes |
| skill `assets/gfx_references/scripted_guis/build_contact_sheets.py` | Reference contact sheets | A (two READMEs) | not run | **Move and improve** | Overwrites the tracked `contact_sheet.png` by default; move to the skill's `tools/` and require `--out` |
| skill `chaos-redux-save-inspection/scripts/save_inspect.py` | Save inspector | A | not run | **Keep** | Skill-owned; identical to the generic copy apart from line endings |

### 2.4 Event-scoped validators and regression tests

All 62 top-level `test_*.py` files, `gfx/test_gfx.py`, the 24 `validation/*.js` tests and the 2 `tests/*.js` tests pass.
They are maintained regression tests under the README's retention rule, so the default action for every passing test is **keep and move** into `tests/events/<id>/` or `tests/systems/<system>/`.

| Group | Refs | Result | Action |
|---|---|---|---|
| `audit_event6_*.py` (6) | A (README) + H | pass | **Keep**, move to `events/006/`; replace three copies of the same brace extractor with `lib/` |
| `test_event021_*` (13), `test_event025_*` (9), `test_event035_*` (10), `test_event32_*` (15), `test_event016/018/020/042` | S or H; several **N** | pass | **Keep and move**; group by event |
| `test_cbrn_*`, `test_famine_*`, `test_humanitarian_*` (4), `test_national_policy_*` (5), `test_camp_panel_publishers` | A, S or **N** | pass | **Keep and move** to `tests/systems/` |
| `validation/test_012_gods_*.js` (10), `validation/test_033_*.js` (14), `tests/event016_*.test.js` (2) | S, H or **N** | pass | **Keep and move**; copy the shared parser they `require()` from `docs/plans/033_acid_rain_plans/validation/` into `tests/lib/` |
| `validation/validate_028_near_miss.py`, `validate_028_presentation.py` | H | pass | **Keep and move** |
| `validation/validate_028_availability.py` | H | **fails**: `chaosx.nr28.8` now has an `immediate` block | **Improve** (D12): the event change is deliberate; allow exactly the `asteroid_incoming_refresh_board_ready` call |
| `validation/validate_033_acid_rain.py` | H + `docs/events` | **fails**: workbook description differs from localisation since the deliberate localisation restore of 12 October (`a7e7466d3f`) | **Keep** (D12): the finding is real; correct the workbook row to match the localisation |
| `audit_mengele_conventional_incident_contract.mjs` | S + H | **fails**: `TypeError` at line 286 | **Retire** (D12) to `.tmp/archive/` |
| `audit_mengele_project_adapter_contract.mjs` | S + H | **fails**: unsupported trigger `request_is_deployment` | **Retire** (D12) to `.tmp/archive/` |

Seven passing tests have no reference anywhere: `test_event021_parent_candidate_lifetime`, `test_event021_sponsor_cleanup`, `test_humanitarian_panel_publishers`, `test_camp_panel_publishers`, `test_national_policy_costs`, `test_national_policy_panel_numbers` and `test_012_gods_refresh_hooks.js`.
An unreferenced passing test is not dead; it gains a README index row and stays.

### 2.5 Structural defects in the test estate

- **Import path.** Python tests import siblings by bare module name and only work as `python .tools/<file>.py`; `unittest discover` from the root fails 43 of them with `ModuleNotFoundError`. Moving them requires a package layout (`tests/__init__.py` plus relative imports) or one `conftest`-free path setup in the runner.
- **Dependencies on historical folders.** Thirteen JS tests `require()` a parser under `docs/plans/033_acid_rain_plans/`, and two 012 tests read evidence under `docs/plans/012…/subagent_handoffs`. Cleaning plan folders would break maintained tests.
- **Pinned commits.** Nine tests call `git show <sha>`, so they fail in a shallow clone.
- **Writes on import.** `test_humanitarian_panels.py` writes to `.tmp/national_policy_panels/` at module level, and three tests write there without creating the folder, so a fresh clone fails until another test has created it.
- **Absolute paths.** The Steam install path is hardcoded in the two main audits and `3d_pipeline/review/provider_intake.py`, and two 012 JS tests need the installed game.
- **Duplicated parsers.** About 20 independent Python Clausewitz readers exist (three in the main audits, three in the Event 006 audits, family parsers in the 021, 032, 035, 025, 020 and 028 tests, six private copies in tests whose siblings share one, and four in the save inspector and 3D pipeline), plus nine JS tokenizers, six localisation readers, three copies of the BOM constant and seven DDS readers.

### 2.6 Documentation gaps

`.tools/README.md` requires every tool to be documented, but omits `check_planning_identifiers`, `check_structural_indentation`, `report_colour_audit`, `build_event016_transit_state_catalog`, both Mengele audits, every `test_*.py`, and the `tests/`, `validation/`, `gfx/` and `live_testing/` folders.
No active document says how to run the maintained tests; the cleanup skill says only "run any touched `.tools/test_*`".

## 3. Where deterministic automation belongs

A check belongs in maintained tooling only when all four conditions hold:

1. It enforces a named rule: a `CLAUDE.md` or skill rule, an engine convention with a vanilla or documentation citation, or a source-to-output relationship produced by a maintained generator.
2. Its inputs are files in the repository or the installed game, read without network access or a running game.
3. Its expected result can be stated independently of the tool, so a valid and an invalid example can be written down.
4. The question recurs across events or systems, rather than belonging to one task.

Scripts never author substantive content.
Focus trees, events, decisions, ideas, descriptions, lore, localisation prose and art direction stay with the agent or person doing the task, and no proposed tool generates them.
Existing generators that assemble registries from hand-authored manifests (`generate_formable_state_puzzle_runtime.mjs`, `export_event_catalog_csv.py`, `sync_agents.py`) are mechanical transformations of reviewed sources and stay in scope.

Each check reports one of three enforcement levels:

- `error`: an exact, reliable rule with a zero false-positive design. It sets a non-zero exit code.
- `warning`: a heuristic or a rule with an unsettled source. It is printed but does not fail, until calibration or a user decision promotes it.
- `review`: a candidate list for a person or agent to judge (dead code, clones, visual quality). It is written to the JSON report only, with a one-line count in the console.

## 4. Prioritised checks

Each row names the rule it enforces, where it runs and its limits.
"Quick" means it runs on the changed paths during routine work; "full" means it runs over the whole repository at a review boundary.

### Tier A: reliable now, adopt first

| # | Check | Rule enforced | Implementation | Level | Limits |
|---|---|---|---|---|---|
| A1 | Localisation integrity | Encoding (CLAUDE.md §2.1), duplicate keys, parse errors, `l_english:` header, event title/description keys, required implicit keys | Existing `audit_localisation_static.py`; add `--paths`, `--fail-on error` and per-category levels | error | Runtime-assembled keys are matched by prefix only; text quality is never checked |
| A2 | Asset reference integrity | Every referenced texture, mesh and `GFX_` name resolves; implicit engine lookups resolve | Existing `audit_asset_wiring_static.py`; same flags | error | Calibrated implicit rules only; unreferenced sprites remain `review` |
| A3 | Forbidden script syntax | CLAUDE.md §1.2 (`<=`, `>=`), §1.11 (unary `-` on a variable token), §2.5 (`:0` keys), §2.3 (`§`/`£` written into scripted localisation) | New `script_rules` check inside one shared content-lint module (see section 5); comment- and string-aware | error | Lexical only; it cannot judge scope or semantics |
| A4 | Generated-output freshness | The CSV exports, agent mirrors and formable runtime equal what their generators would write now | Add `--check` to `export_event_catalog_csv.py` and `generate_formable_state_puzzle_runtime.mjs` (render to a temporary directory and compare bytes); `sync_agents.py --verify` already exists | error | Proves consistency with the current source, not that the source is right |
| A5 | Guidance size | `read_limits.json` ceilings (CLAUDE.md §9.8) | Existing `sync_read_limits.py --check` (already exits 1) | error | Byte estimate, not a tokenizer |
| A6 | Frame strips | A multi-frame sprite's texture width is divisible by `noOfFrames` | New `sprites` subcommand in `.tools/gfx/gfx.py`, reading registrations through the asset audit's parser | error | Divisibility proves geometry, not that frames are in the right order |
| A7 | Flag ladder | Normal, medium and small TGAs exist together at 82x52, 41x26 and 10x7 (skill flag rules, vanilla 2,202 / 2,203) | New `flags` subcommand in `gfx.py` | error for size and missing sizes; top-origin TGA is a warning (D4) | Orientation of the artwork itself still needs the contact sheet |
| A8 | Achievement triplets | Base, `_grey` and `_not_eligible` exist, 64x64 (vanilla 882 / 882, `process_achievement_icons.py`) | Reuse the processor's existing validator in check mode | error | Says nothing about the art |
| A9 | Runtime binaries are real files | No Git LFS pointer stub or truncated DDS/TGA in runtime asset folders | New check in `gfx.py`; header parsing with `DX10` allowed | error | Does not judge pixels |
| A10 | Parchment text colour | `chaos-redux-events` rule: report and news text on parchment carries no `§` codes, including scripted localisation output | Existing `report_colour_audit.py`; add `--paths` and a non-zero exit | error after the one current finding (Event 038) is fixed by its owner | Follows `[This.GetX]` chains it can resolve statically |
| A11 | Maintained tests pass | Each maintained regression test protects a current contract (`.tools/README.md` retention rule) | `python -m unittest discover` over the consolidated test tree; `node --test` for JS | error | Only as good as each test's assertions |
| A12 | Changed-file script validation | Installed `effects_documentation.md` and `triggers_documentation.md` command kinds and scopes, as checked by `hoi4_script_validate` | `check.py quick` calls the MCP tool for changed script files through the shared stdio client (D6) | error for reported findings; unresolved commands and unchecked argument blocks are listed as unresolved | Only the tool's `checksPerformed`; parameter semantics and engine behaviour stay unverified; skipped with a notice when the MCP server is unavailable |

### Tier B: useful, but start as warnings

| # | Check | Rule or reference | Level and promotion condition |
|---|---|---|---|
| B1 | Family canvas sizes for focus, decision and idea icons | D1–D3 | Focus: sizes other than 94x86 or 100x88 are `error`, and a new or changed 100x88 file is a `warning`. Decision: sizes other than 32x32, 33x32 or 34x34 are `warning`. Idea: sizes other than 64x64, 60x68 or 65x67 are `warning` |
| B2 | Transparent unused canvas | Skill rule: icons, counters, emblems, overlays and transparent animation frames have transparent unused canvas | `warning`: corners and outer one-pixel ring must be alpha 0 for files whose sprite is in a declared transparent family. Promote after a calibration run on the matching vanilla families shows no false positives |
| B3 | Empty or ghosted subject | `gfx.py alpha` (empty subject is already a hard failure), D5 | Empty subject: `error`. Mean alpha below 200: permanently `warning`, because vanilla counters fall below it |
| B4 | Chroma fringe | `gfx.py` magenta and green edge definitions | `warning`; legitimate green or purple art exists |
| B5 | Flags checked but never set | `audit_script_references_static.py` | `warning` on the changed files' flags only; full list stays `review` |
| B6 | Indentation | CLAUDE.md §1.1 | `warning` on changed files only; no repository-wide reformat (it would touch 188 files) |
| B7 | Report-image processing recipe | `process_report_event_image.py` is the approved recipe | `warning` until processed files carry provenance (see B7 note below) |
| B8 | Python quality | Section 6 | Ruff defect rules as `error` on changed files, complexity as `warning` with a ratchet |

B7 note: whether a report image "was processed correctly" can only be verified when the output records its source hash, tool version and arguments.
The proposal is that `process_report_event_image.py` writes that record into the existing asset manifest, and the check re-runs the recipe on the recorded source and compares the result.
Without a recorded source, the check can only confirm dimensions and transparent edge space, and must say so; it must never infer correct processing from similarity scores or metadata.

### Tier C: keep with people, MCP tools or the game

- Artistic fit, likeness, composition, readability of a NATO glyph, and HOI4 style: native-size visual review against the catalogued vanilla references.
- Focus layout, branch logic and missing focus references: use `hoi4_focus_inspect` and `hoi4_focus_render`, not a new script.
- Event chains and weighted logic: `hoi4_event_inspect`, `hoi4_probability_inspect`.
- Argument semantics, unresolved helpers and anything outside `hoi4_script_validate`'s `checksPerformed` (A12 covers the rest for changed files).
- Runtime behaviour, error.log cleanliness and visual layout in game: user-owned live testing, or `chaos-redux-debug-playtest` when the user invokes it.

## 5. Shared design for the checks

### One entry point

Add `.tools/check.py` as the single documented command for routine and boundary checks:

```powershell
python -B .tools/check.py quick              # changed and untracked paths from git, Tier A plus warnings
python -B .tools/check.py quick --paths events/foo.txt gfx/interface/goals/x.dds
python -B .tools/check.py full               # whole repository, Tier A, warnings and review counts
python -B .tools/check.py full --json .tmp/checks/full.json
```

It is a thin dispatcher, not a framework: it maps paths to the existing audits and the few new checks, runs them in-process where they are Python, and normalises their output.
It is justified because there is no CI in this repository, there are seven agent runtimes, and today each agent has to remember five separate commands with different exit semantics.
Its maintenance cost is one small file plus a table of path patterns.

### Output contract

- Console: one line per finding, sorted by path, line and rule id: `path:line: error RULE-ID message`. A summary line per check with counts. Review lists print only their counts.
- `--json PATH` writes the complete structured report; `--verbose` prints warnings' context lines.
- Exit codes: `0` no errors, `1` errors found, `2` usage or input failure (missing file, unreadable game directory).
- Read-only by default. Any fixer (`reindent_script_files.py --apply`, `gfx.py defringe`) stays a separate, explicit command and is never invoked by `check.py`.

### Shared library

Create `.tools/lib/` with one canonical implementation of each parser that the checks share; section 2.5 lists about 20 Python Clausewitz readers, six localisation readers and seven DDS readers today:

- a Clausewitz block reader (comment- and string-aware, keeps line numbers),
- a localisation YAML reader (BOM, header, key, version, value),
- the sprite-registration reader used by the asset audit,
- the report and exit-code helpers above.

Existing audits migrate to it one at a time with their current outputs compared before and after.
Event tests that already share a family parser keep working through it; tests are migrated only when they are touched for another reason, because rewriting 60 passing tests carries risk without a defect to fix.
The DDS writer stays canonical in `.claude/skills/chaos-redux-event-assets/tools/convert_to_dds.py`, which `gfx.py` already imports; the BC-compressed model-texture DDS code in `3d_pipeline/textures/` is a different format family and stays where it is.

### Data-driven size profiles

Move the `gfx.py` slot table into `.tools/gfx/profiles.json`, one row per family with its canvas, frames, margin, enforcement level and a `source` field naming the user decision, vanilla citation or catalogue entry.
The skill's "Standard HOI4 asset sizes" list then points to that file instead of repeating numbers, which also recovers bytes for P7.
No row is added without a cited source. The focus, decision and idea rows cite D1–D3 and list their accepted alternative sizes; families with no settled source carry `"level": "warning"`.

### Game directory

Every tool that reads the installed game takes it from `HOI4_GAME_DIR`, defaulting to the current Steam path (D13), through one helper in `.tools/lib/`.
A missing game directory is exit code `2` with the variable name in the message, never a silent skip.

### Examples kept as fixtures

Each new rule gets one valid and one invalid fixture under `.tools/tests/fixtures/<check>/`, for example a 1,656-px strip with 35 frames (invalid) and 36 frames (valid), a 41x26 flag in the normal folder (invalid), and a scripted localisation entry containing `§` (invalid).
These fixtures double as the documentation of what the rule means.
No broader test framework is proposed.

## 6. Code quality for the tooling itself

Tooling is pinned in `.tools/requirements-dev.txt` and run through `uvx` or `py -3.13 -m`, so nothing is installed globally and the 3.9 default interpreter stays untouched.

Proposed ruff configuration (in a new root-level `ruff.toml`, scoped to `.tools/**` and `.claude/skills/**/tools|scripts/**`):

- Enabled as errors: `F` (unused imports and variables, undefined names), `E9` (syntax errors), `B` (bugbear: mutable defaults, loop-variable capture, `assert False`), `PLE` (pylint errors), `S110` and `BLE001` (silently swallowed exceptions; two `except Exception: pass` blocks and one bare `except` exist today), `RUF100` (unused `noqa`).
- Enabled as warnings via the ratchet: `C901` with `max-complexity = 15` and `PLR0915` (too many statements). Existing functions above the limit are recorded in a baseline file and may not grow; new or rewritten functions must meet the limit. 15 is ruff's default and matches the measured distribution (242 functions exceed it, almost all in the 3D adapter and the Event 006 auditors).
- Not enabled: formatting, import sorting, quote style and line length. They would touch most of the 65,000 lines for no defect reduction.
- `vendor/` and `.venv/` are excluded.

Type checking: `mypy --strict` (or pyright strict) for `.tools/lib/`, `.tools/gfx/`, `.tools/sync/`, `check.py` and the skill tools, which are small and already 98% annotated in the skills.
The 3D adapter and older audits stay unchecked until they are touched; a module joins the strict list when its owner annotates it.
JavaScript: `node --check` on maintained `.js` and `.mjs` files; no ESLint, because the 28 JS files are self-contained tests and one generator.

Exceptions must be written as a file-level or line-level suppression with a reason, never by widening the global ignore list.

## 7. Proposed `.tools` structure and migration

```text
.tools/
  README.md                tool index: one row per maintained tool (purpose, command, when to run, owner skill)
  check.py                 single read-only entry point (new)
  requirements-dev.txt     pinned ruff, mypy (new)
  lib/                     canonical shared parsers, report helpers, game-directory helper, stdio MCP client (new)
  audits/                  audit_localisation_static, audit_asset_wiring_static, audit_script_references_static,
                           check_structural_indentation, reindent_script_files, check_planning_identifiers*
  gfx/                     gfx.py, profiles.json, README, tests (existing, extended)
  catalog/                 export_event_catalog_csv, package_chatgpt_project_sources (.py, .bat)*
  formables/               generate_formable_state_puzzle_runtime.mjs*
  events/                  event-scoped static validators that are still maintained (Event 006, 028, 033)*
  tests/                   all maintained regression tests: tests/events/<id>/, tests/systems/<system>/, tests/fixtures/
  sync/  wiki/  live_testing/  3d_pipeline/   unchanged
```

Rows marked `*` follow the keep actions in section 2; the two Mengele audits are retired (D12) and do not move.
Skill-specific helpers stay beside their skill (`.claude/skills/<skill>/tools/` or `scripts/`), and `.agents/skills/` remains a symlink mirror, so no runtime receives a copy.
`build_contact_sheets.py` is maintained (two active READMEs call it), so it moves from `assets/gfx_references/scripted_guis/` into the same skill's `tools/`.

Migration steps, one commit per step:

1. Record a baseline: run every maintained test and audit, store the JSON outputs in `.tmp/tooling_migration/before/`.
2. Move files with `git mv` so history follows them.
3. Update every active reference in the same commit: `CLAUDE.md`, `AGENTS.md`, skills, agent definitions, `.tools/README.md`, `docs/systems/`, `docs/testing/` instructions and any import or `subprocess` path. Historical handoffs under `docs/plans/` keep their old paths, as the README's provenance rule requires.
4. Re-run and compare against the baseline; outputs must be identical apart from path strings.
5. Run `python .tools/sync/sync_agents.py` and `--verify` after any skill or agent text changes.
6. No compatibility shims are left at old paths. Other sessions that run an old command get a clear "file not found" and the README index gives the new path.

`docs/` scripts are not moved, untracked or deleted (D8). New task scripts go to `.tmp/<task>/`; a script that later proves recurring is promoted through the README procedure.

## 8. Generic Agentic HOI4 Modding package (after Chaos Redux)

The generic package already has CI (`validate-hoi4-mod-setup-manifests.yml`), generated `AGENTS_template.md`, `check_guidance_size.py`, and unit tests for two skill tools, but it has no linter, type checker, content validator or GFX check.
Once the Chaos Redux work is accepted and implemented, port only the parts that are not Chaos Redux-specific:

1. Policy: add the same tooling section to `CLAUDE_template.md` in generic wording (no `chaos-redux-*` names; `check_release_package.py` rejects them) and regenerate `AGENTS_template.md` with `sync_instructions.py`.
2. Checks: port A1–A3, A6–A9, A12, the output contract and the `HOI4_GAME_DIR` helper as `.tools/check.py` plus `.tools/lib/`, with size profiles reduced to the rows that have vanilla citations (flags, achievements, counters, report and news pictures, category pictures). The Chaos Redux focus, decision and idea decisions (D1–D3) are not exported.
3. GFX: port `gfx.py` without the Chaos Redux slot table; the generic `hoi4-feature-assets` size table gains the vanilla citations that `vanilla_reference/CATALOG.md` already uses for category pictures.
4. Code quality: add the same ruff and strict-typing configuration and run it in the existing CI workflow after the unit tests.
5. Shared tools: Chaos Redux is the upstream (D9) for `convert_to_dds.py`, `create_advisor_icon.py`, `extract_portrait_source_crop.py`, `process_achievement_icons.py`, `process_report_event_image.py` and `save_inspect.py`. After their differing strings become settings, copy them byte-identically and add a compare check to the generic package's CI.
6. Skills and agents: update `hoi4-feature-assets`, `hoi4-subagents` and the `hoi4-skill-maintainer` agent with the generic equivalents of the skill changes in section 9, then run the package's `sync_agents.py`, `sync_skills.py` and `sync_instructions.py` with `--check`.

## 9. Proposed instruction changes

### 9.1 New `CLAUDE.md` section

Insert as section 4a, directly after "4. HOI4 Modding Rules Summary", replacing rules 23 and 24 and the "Do not replace real implementation work with tooling work" paragraph of section 5, whose requirements it carries over:

```markdown
## 4a. Deterministic Tools and Checks

Mechanical questions get mechanical answers. Before reasoning through a question that a file can answer (does this key, sprite, texture or flag exist, is this size or frame count right, is this output stale), run the existing check.

1. Look first. `.tools/README.md` indexes every maintained tool and the question it answers, and skills name the checks for their workflows. Run `python -B .tools/check.py quick` on the files you changed before review, and `python -B .tools/check.py full` at the end of a large task. Read a check's documented limits before relying on its result.
2. Add or improve a tool only for a recurring task with an explicit rule, known inputs and an independently checkable result. Extend the owning tool before creating a new one, and give each new rule one valid and one invalid fixture.
3. Document every maintained tool in `.tools/README.md` or its package README: purpose, command, inputs, outputs, dependencies, the rule or reference it enforces, and its limits. Checks are read-only by default; fixers are separate and explicit.
4. Place shared tools under `.tools/` with one canonical implementation in `.tools/lib/`, and helpers used by one skill in that skill's `tools/` or `scripts/` folder. Never copy a tool between `.tools/`, `.claude/`, `.agents/` or another runtime folder.
5. When a reusable workflow gains or changes a tool, update the skill that owns the workflow in the same change.
6. Keep one-off repairs, migrations, job-specific scripts and temporary checks in ignored `.tmp/<task>/`. `.tools/3d_pipeline/` is shared infrastructure, not storage for unit-specific runners. Retain maintained regression tests that protect a current contract, even for one event; a filename or date does not make a test disposable. Promote a helper only for demonstrated recurring use or a required shared entry point; command-line arguments alone do not make a one-off tool reusable.
7. Before adding a skill, document, report, wrapper or helper, check its existing owner and extend that source. Keep one current task report and control bloat by removing duplication, not by deleting specific requirements.
8. Tools never replace design, gameplay reasoning, writing, art direction or review. Do not generate focus trees, events, decisions, ideas, localisation prose or lore with scripts, and do not count generated volume as progress.
9. A passing check proves only the properties it checks. A size or alpha check does not establish visual quality, and a reference check does not establish gameplay behaviour; report it that way.
10. Never weaken a check, add a suppression, lower a threshold, edit a baseline or change a requirement to make validation pass. Fix the finding, or report it with its reason and get the rule owner's decision.
```

Byte budget: the section is about 2,810 bytes; removing rules 23–24 (1,178 bytes) and the section 5 paragraph (401 bytes) frees 1,579, leaving about 1,230 bytes to recover.
Proposed relocation: move the complete "Meta effect example" subsection (1,953 bytes) verbatim into `common/scripted_effects/chaosx_dynamic_effects.md`, which already documents dynamic and meta-effect helpers, and replace it with one line under rule 12: "A worked `meta_effect` example is in `common/scripted_effects/chaosx_dynamic_effects.md#meta-effect-example`."
Net result: about 59,350 bytes, under the 60,000 ceiling. This relocation is decision D7.

The "Small scripts may be used for mechanical audits…" sentence of section 5 is preserved in rule 8 and the section's first paragraph; the bulk-generation paragraph that follows it stays in section 5 unchanged.

### 9.2 `AGENTS.md`

Adopt the generic package's `sync_instructions.py` as `.tools/sync/sync_instructions.py`, with a replacement table for the 6 intentional runtime differences (D10).
`AGENTS.md` is then generated from `CLAUDE.md`, so it receives section 4a and the D7 relocation automatically, and `--check` catches drift.
Rule 24's "avoid duplicate instruction copies outside the established generators" and the README's "`CLAUDE.md` is edited directly, and `AGENTS.md` carries the same rules" line are updated to name the new generator.

### 9.3 Skills

| Skill | Change |
|---|---|
| `chaos-redux-event-assets` | Replace the size list with a pointer to `.tools/gfx/profiles.json` and its decisions (also brings the file under its 58,000-byte ceiling); replace the manual `file` flag procedure with `gfx.py flags`; add `gfx.py sprites` to the pre-wiring checklist; state which properties the checks cannot establish |
| `chaos-redux-codebase-cleanup` | Use `check.py full --json` for the worklist; keep the existing "candidate list is a worklist, not a deletion list" rule |
| `chaos-redux-events`, `chaos-redux-focus-trees`, `chaos-redux-decisions-missions` | One line each in the validation step: run `check.py quick` on the changed paths, then the MCP inspect tool the skill already names |
| `chaos-redux-subagents` | Audit roles run `check.py quick` on their scope before reporting, and report its findings by rule id |
| `chaos-redux-scripted-gui` | Point to `gfx.py sprites` for frame and texture checks |

No skill gains a duplicated copy of the policy; each points to section 4a.

## 10. Implementation sequence

1. **Owner fixes found by this audit.** Correct the Event 033 workbook row to match its localisation and re-export the CSVs (D12); relax the Event 028 `immediate` assertion (D12); hand the building icon strip frame count, the DHR flag origins (D4) and the Event 038 parchment colour code to their owners.
2. **Make existing checks decide.** Add `--paths`, `--fail-on` and severity levels to the three audits; add `check.py` with A1, A2, A5, A10 and A11 wiring; record the test baseline. Fix the `chaos-redux-event-assets` size overrun by relocating a complete section (A5 fails today).
3. **Cheap exact rules.** A3 forbidden syntax, A4 generator `--check` modes, A6 frame strips, A7 flag ladder, A8 achievements, A9 runtime binaries, A12 changed-file script validation, and the `HOI4_GAME_DIR` helper (D13), each with fixtures.
4. **Policy.** Add `sync_instructions.py` (D10), then land section 4a and the D7 relocation in `CLAUDE.md`, regenerate `AGENTS.md`, update the skill pointers, and add `check.py full` to the push routine (D11). Refer only to commands that now exist.
5. **Tests and quality.** Consolidate tests under `.tools/tests/` with a package layout so standard discovery works; move the shared 033 parser out of `docs/plans/`; make tests create their own `.tmp/` folders and write nothing on import; retire the two Mengele audits (D12); then add ruff and strict typing with the complexity baseline.
6. **Folder reorganisation and shared library.** Move the remaining tools, migrate audits onto `.tools/lib/` one at a time with before/after output comparison.
7. **GFX profiles and heuristics.** `profiles.json` with the D1–D3 rows, B1–B4 at the levels in section 4, B7 provenance recording, calibration runs against vanilla.
8. **Generic package port** as in section 8.

Steps 1–4 deliver most of the value; steps 5–7 can pause at any boundary without leaving anything half-moved.

## 11. Acceptance criteria

- **Audits decide:** each of the three audits exits `1` on a seeded exact defect in a fixture and `0` on the current tree; `--paths` limits reporting (cross-reference audits still scan the whole repository, because a reference can only be resolved against every definition); the full JSON output is unchanged apart from added level fields.
- **`check.py`:** `quick` on a typical single-event change completes in under 30 seconds; output is sorted and stable across two runs; exit codes follow section 5; it never writes outside `--json` and `.tmp/`.
- **Exact rules (A3, A6–A10):** each has a valid and an invalid fixture that pass and fail respectively; the current tree has no false positives, or every remaining finding has been confirmed as a real defect by its owner.
- **Generator freshness (A4):** `--check` fails after a one-cell workbook edit without export and passes after export; no tracked file is written in check mode.
- **GFX profiles:** every row in `profiles.json` has a `source`; no blocking row lacks a user decision or vanilla citation; the skill no longer repeats the numbers.
- **Tests:** one documented command run from the mod root discovers and runs every maintained Python and JS test and all pass, including the corrected `validate_028_availability.py` and `validate_033_acid_rain.py`; the Mengele audits are in `.tmp/archive/` with no active reference left; no maintained test imports from `docs/plans/`, writes on import, or fails on a fresh clone because a `.tmp/` folder is missing.
- **Code quality:** ruff defect rules report zero findings on `.tools/lib`, `.tools/gfx`, `.tools/sync`, `check.py` and skill tools; strict typing passes on the same set; the complexity baseline exists and the ratchet rejects growth.
- **Organisation:** `.tools/` top level contains only README, `check.py`, requirements and subfolders; every maintained tool has one README row; no tracked file is byte-identical to a maintained tool elsewhere in the repository outside historical `docs/plans/`.
- **Instructions:** `sync_read_limits.py --check` exits `0`; `sync_agents.py --verify` and `sync_instructions.py --check` pass; `CLAUDE.md` and the generated `AGENTS.md` carry section 4a and no conflicting older wording; no skill repeats the policy.
- **Script validation (A12):** `check.py quick` reports a seeded unknown effect in a fixture file and lists unresolved helpers separately; with the MCP server stopped it prints a skip notice and exits by the other checks' results.
- **Game directory (D13):** with `HOI4_GAME_DIR` pointing at an empty folder, every tool that needs the game exits `2` naming the variable.
- **Generic package:** its CI runs the ported checks and ruff; `check_release_package.py` still passes; templates regenerate cleanly.

## 12. Decisions

All thirteen decisions are user decisions of 25 October 2026, accepted as recommended in the planning chat.
Each entry gives the question, the decision, and the evidence it rests on.

- **D1 Focus icon canvas.** Question: enforce 94x86, accept both 94x86 and 100x88, or move to 100x88? Decision: 94x86 and 100x88 are both valid; any other size is an `error`. New art uses 94x86, and a new or changed file at 100x88 gets a `warning`. Evidence: 3,342 Chaos Redux focus icons are 94x86 and 714 are 100x88, both render, and vanilla uses 100x88 (2,680 of 2,951).
- **D2 Decision icon canvas.** Question: which target, and do existing files stay? Decision: new art uses 32x32; existing 33x32 and 34x34 files are valid; any other size is a `warning`. The `gfx.py` `decision` profile changes from 34x34 to 32x32 and keeps 33x32 and 34x34 as accepted alternatives. Evidence: the skill table and 1,722 files use 32x32; vanilla mostly uses 33x32; the 34x34 target came from one repair task.
- **D3 Idea icon canvas.** Question: is 64x64 a deliberate convention? Decision: yes, new art uses 64x64; the vanilla 60x68 and 65x67 sizes are also valid, so reused vanilla-style art is not flagged; any other size is a `warning`.
- **D4 Flag TGA origin.** Question: should a top-origin flag block? Decision: `warning`, not `error`. Flag size and missing ladder sizes stay `error`. `DHR_democratic.tga` and `DHR_neutrality.tga` go to their owner for review. Evidence: vanilla ships 5 top-origin flags out of 2,203.
- **D5 Alpha threshold.** Question: keep "mean alpha below 200"? Decision: keep it as a `warning` only. An empty subject is an `error`, and the transparent-canvas check (B2) covers opaque backgrounds. Evidence: vanilla infantry counters average 162.3 and 164.2.
- **D6 Batch script validation.** Question: CLI in HOI4 Agent Tools, a stdio client here, or per-file only? Decision: `check.py` calls `hoi4_script_validate` for changed script files through the existing stdio MCP client `.tools/3d_pipeline/lib/mcp_stdio.py` (moved to or re-exported from `.tools/lib/` with its 15 importers updated). A command-line mode is requested from HOI4 Agent Tools separately, and `check.py` switches to it once it exists. Findings follow the tool's own `checksPerformed`; unresolved commands are reported as unresolved, not passed.
- **D7 `CLAUDE.md` budget.** Decision: move the complete "Meta effect example" subsection verbatim into `common/scripted_effects/chaosx_dynamic_effects.md` and leave a one-line pointer under rule 12, as in section 9.1. The same relocation applies to `AGENTS.md`.
- **D8 Historical scripts in `docs/`.** Decision: leave the 485 tracked scripts as provenance and add no new ones; new task scripts go to `.tmp/<task>/`. Maintained tests stop loading files from `docs/plans/` (section 10 step 5) before any plan folder is cleaned.
- **D9 Upstream for shared asset tools.** Decision: Chaos Redux is the upstream for `convert_to_dds.py`, `create_advisor_icon.py`, `extract_portrait_source_crop.py`, `process_achievement_icons.py`, `process_report_event_image.py` and `save_inspect.py`. The few differing strings become settings so both copies are byte-identical, and the generic package gains a compare check that fails when its copy drifts.
- **D10 Generated `AGENTS.md`.** Decision: generate `AGENTS.md` from `CLAUDE.md` with the generic package's `sync_instructions.py` and a replacement table for the 6 intentionally different lines; its `--check` mode fails on drift. `CLAUDE.md` stays the only hand-edited instruction file.
- **D11 CI.** Decision: no GitHub Actions workflow and no pre-push hook. `check.py full` becomes a step in the existing manual push routine. Evidence: the full audits need the installed game, and a slow hook would block agents pushing from the shared checkout.
- **D12 Failing event validators.** Decisions, per validator:
  - `validate_033_acid_rain.py` found a real defect. The workbook row says the rain exposes "the inhabited states in its path"; the in-game `acid_rain.event_details.description` says "the inhabited states registered at formation". The workbook row is corrected to match the localisation through `chaos-redux-xlsx`, the CSVs are re-exported, and the validator is kept.
  - `validate_028_availability.py` is outdated. `chaosx.nr28.8` gained an `immediate` block that only calls `asteroid_incoming_refresh_board_ready`, from the deliberate target-board change of 4 October. The assertion is relaxed to allow exactly that refresh call; the rest of the validator is kept.
  - `audit_mengele_conventional_incident_contract.mjs` and `audit_mengele_project_adapter_contract.mjs` are retired to `.tmp/archive/` (recoverable from Git history). Each embeds its own script interpreter that breaks whenever source uses a trigger it does not model, here `request_is_deployment`. Active references in `common/**/*.md` are updated in the same commit.
- **D13 Machine-specific paths.** Decision: tools read the game directory from the `HOI4_GAME_DIR` environment variable, defaulting to `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV`. This covers the two main audits, `3d_pipeline/review/provider_intake.py` and the two Event 012 JS tests, and the generic package port reuses it. `live_testing/clausewitz_linux.py` keeps its WSL paths, which belong to its runtime adapter configuration.

## 13. Implementation record

This section is the single current report for the implementation; each step updates it in place.

### Step 1: owner fixes (25 October 2026)

- **Event 028 validator.** `validate_028_availability.py` failed on two outdated assumptions, both from deliberate event changes. `chaosx.nr28.8` now has an `immediate` block that only calls `asteroid_incoming_refresh_board_ready` (commit `f9cb13c4f8`, 4 October); the assertion now allows exactly that block and still rejects `fire_only_once` and any other setup. The 12 October report pagination (`01a1e2be19`, `docs/systems/event_system/report_event_choice_pages.md`) left four direct options on each board, so the option comparison now reads the complete five-option pool from each board's AI-only companion event (`chaosx.nr28.94699` and `chaosx.nr28.94799`). All 19 source-model cases pass, as do the sibling `validate_028_near_miss.py` and `validate_028_presentation.py`.
- **Event 033 catalog row.** The workbook was the stale side: the localisation was deliberately restored on 12 October (`a7e7466d3f`) and the workbook kept the earlier wording. `chaosx_spreadsheet_doc_worker` replaced two inline-string cells through the narrow OOXML route, `Events` row ID 33 column C (now "…the inhabited states registered at formation… crossed every eligible state.") and `Clusters` row ID 5 (Natural Disasters) column C, which the same validator also compares with localisation. Only `xl/worksheets/sheet1.xml` and `sheet2.xml` changed (workbook SHA-256 `d9ad04ce…` to `3e0b8dbf…`); the export changed exactly one cell in each of the events and clusters CSVs and none in the scenarios CSV.
- **Event 033 validator.** With the workbook aligned, `validate_033_acid_rain.py` reached a second outdated block: it asserted the Acid Rain mixed-Major cluster pacing override, which the 13 October historical restore (`1927a7901c`) removed deliberately. That block now asserts the restored contract instead: the effective pacing type comes from `get_event_cluster_type` with no Acid Rain override, the major and minor pacing updates run once each, Acid Rain is registered once as a Major event and never as repeatable, and `acid_rain_cluster_reserved` is still set (it is checked in `033_acid_rain_triggers.txt`). The validator and all 14 `test_033_*.js` tests pass.

### Step 2: make existing checks decide (25 October 2026)

Status: `implemented`. Validation is source and command evidence only; no game run was involved.

- **Shared contract.** `.tools/lib/report.py` defines the finding record (check, rule, level, path, line, message), the three levels, `--paths`/`--paths-from`/`--fail-on`, stable ordering and exit codes. `audit_localisation_static.py`, `audit_asset_wiring_static.py`, `audit_script_references_static.py` and `report_colour_audit.py` map every category onto it, document their rule levels in their docstrings, add `findings` and `levels` to their JSON, and exit `1` on an error unless `--fail-on none` is given. A before/after comparison of the three audits' JSON on the current tree showed every existing field unchanged; all three and the colour audit exit `0`.
- **`check.py`.** `.tools/check.py quick|full` runs localisation (A1), asset wiring (A2), parchment colour (A10), guidance size (A5) and the 101 maintained tests (A11) in parallel, plus the script-reference audit in `full`. A 038-only `quick` run took 19 s; `full` took 75 s and exits `0`. The full baseline is in `.tmp/tooling_migration/before/` (local, ignored).
- **Guidance size.** `chaos-redux-event-assets/SKILL.md` was 58,224 bytes against its 58,000-byte ceiling. The complete "Temporary event asset workspaces" section moved verbatim to `references/manifest-and-lineage.md`, leaving a pointer in the root in the same style as the family sections; the root is now 57,920 bytes and `sync_read_limits.py --check` passes.
- **Fixture evidence.** `.tools/tests/test_check_contract.py` (12 cases) seeds synthetic findings and proves that a missing BOM, an ordinal-suffix key and a missing GFX file exit `1`, that review candidates and reference-audit warnings exit `0`, and that the path filter, ordering and quick-mode check selection behave as documented. It runs as part of A11.

Differences from the plan text, all within the accepted design:

- `--paths` limits reporting, not scanning, for the cross-reference audits; the acceptance criterion now says so.
- A10 reports at `warning` level until the Event 038 hand-off below is fixed; promoting it is a one-word change in `report_colour_audit.py`.
- `quick` runs the tests only when `.tools/` changed, and leaves the 78 s script-reference audit to `full`; B5 (flag warnings on changed files) can add it to `quick` later.
- `--paths-from FILE` was added because the shared working tree's path list exceeded the Windows command-line limit.
- The shared package is named `lib`, as planned. `.tools/3d_pipeline/lib/` uses the same name for its own scripts, so D6 must merge `mcp_stdio.py` and `paths.py` into `.tools/lib/` rather than add a second `lib` to one `sys.path`.

### Step 3: cheap exact rules (25 October 2026)

Status: `implemented`. Validation is source, command and fixture evidence; no game run was involved.

- **D13 game directory.** `.tools/lib/game.py` reads `HOI4_GAME_DIR` (default: the Steam path). The localisation and asset-wiring audits and `audit_event6_allocator.py` (which previously read `HOI4_ROOT`) use it, and the two main audits exit 2 naming the variable when the folder is not a game installation; `gfx/test_gfx.py`, `3d_pipeline/review/provider_intake.py` and the two Event 012 JS tests read the same variable directly. The 3D audio tests and `3d_pipeline/config/*.json` keep their configured paths as adapter configuration.
- **A3 forbidden syntax.** `audit_script_rules.py` reports `<=`/`>=`, unary minus on a variable token, and `§`/`£` in scripted localisation; ordinal keys stay with the localisation audit. The current tree has no findings. Fixtures: `tests/fixtures/script_rules/` (valid, invalid, invalid scripted localisation), tested by `tests/test_script_rules.py`.
- **A4 generator freshness.** `export_event_catalog_csv.py --check` and `generate_formable_state_puzzle_runtime.mjs --check` render without writing and print `Would update <path>`; with `build_event016_transit_state_catalog.py --check` and `sync_agents.py --verify` they form the `generators` check. `tests/test_generator_checks.py` proves the exporter check passes on the current exports and fails after a one-cell change or a missing export. The formable generator cannot run against the committed manifests (hand-off below), so the check reports that as an error.
- **A6–A9 GFX.** `gfx/gfx.py` gained `sprites`, `flags`, `achievements`, `binaries` and `audit`. Binary fixtures outside `gfx/` are ignored by `.gitignore`, so `tests/test_gfx_conformance.py` builds minimal DDS and TGA files in a temporary folder.
- **A12 script validation.** `validate_scripts_mcp.py` validates changed script files in one HOI4 Agent Tools session through `lib/mcp_session.py`; `tests/test_validate_scripts_mcp.py` checks the level mapping against recorded real responses. A 038-only quick run, including server start-up and indexing, took 19.5 s.
- **`check.py`.** New checks `script-rules`, `gfx`, `generators` and quick-only `script-validate`, which reports itself as skipped when the server cannot start. `full` took 46 s and exits 1 on five genuine errors: the formable generator failure and four misfiled untracked route flags (both below). All 105 maintained tests pass.

Differences from the plan text, each forced by measured evidence:

- **A6 is a warning, not an error.** Vanilla ships 79 of 1,798 multi-frame sprites whose width does not divide by `noOfFrames`, so the engine tolerates it. The building strip (36 icons sliced as 35 frames) remains a hand-off.
- **A7 missing ladder sizes are warnings.** Vanilla ships incomplete ladders (89 normal flags have no small file, and 112 small flags have no normal one); wrong sizes stay errors and origin is a warning (D4).
- **A8 checks size only.** Triplet presence for defined achievements was already an error in the asset-wiring audit's implicit achievement-art rule; a separate triplet rule misread 33 tracked `__shard6_c0N` candidate files as achievement bases.
- **D6 uses a new session client.** `3d_pipeline/lib/mcp_stdio.py` is hash-pinned in `3d_pipeline/config/dependencies.lock.json`, starts one server per call (about 19 s of indexing each), and closes stdin before a Node server answers. Changing it requires an adapter release, so `.tools/lib/mcp_session.py` (about 100 lines) runs one session for many calls; the D6 merge of the two clients belongs with that release.
- **Known-mistake matches are warnings.** On `chaosx_event_cluster_effects.txt`, `KNOWN_MISTAKE_TEMP_VARIABLE_SCOPE_PREFIX` reported eight false positives on script constants such as `constant:tensions_rising_event_log.event_id`.

### Step 4: policy (25 October 2026)

Status: `implemented`.

- **Generated `AGENTS.md` (D10).** `.tools/sync/sync_instructions.py`, adopted from the generic package with an added check for replacement pairs whose source line no longer exists, regenerates `AGENTS.md` from `CLAUDE.md`. `instruction_projection.json` holds the six intentional runtime lines as whole-line pairs; before any `CLAUDE.md` edit the projection reproduced the existing `AGENTS.md` byte for byte. `check.py` runs `--check` as part of `generators`, and a deliberately appended line was reported as `GEN-STALE` and then restored. `.tools/sync/README.md`, `.tools/README.md` and `.codex/README.md` now describe `CLAUDE.md` as the only hand-edited instruction file.
- **Section 4a and D7.** `CLAUDE.md` gained section 4a in place of rules 23–24 and the section 5 tooling paragraph. Compared with the draft in section 9.1, rule 3 also names callers, rule 7 keeps rule 24's generator, scaffolding and bloat clauses, and rule 8 keeps the section 5 sentence about scripts and report generators, so every removed requirement survives. The complete "Meta effect example" moved verbatim to `common/scripted_effects/chaosx_dynamic_effects.md#meta_effect_example` (with a table-of-contents entry and CRLF endings preserved), and rule 12 links to it. `CLAUDE.md` is 59,920 bytes and `AGENTS.md` 59,741 bytes, both under the 60,000-byte ceiling.
- **Skills.** One pointer each, without repeating the policy: `chaos-redux-events` (final checklist), `chaos-redux-focus-trees` (section 16), `chaos-redux-decisions-missions` (section 20), `chaos-redux-subagents` (audit roles report `check.py quick` findings by rule id), `chaos-redux-scripted-gui` (handoff), `chaos-redux-codebase-cleanup` (`check.py full --json` as the worklist), and `chaos-redux-event-assets`: the flag checklist in `references/event-images-and-flags.md` uses `gfx.py flags` instead of `file`, the frame-strip rule in `references/icon-and-ui-families.md` names `gfx.py sprites`, and the root flag summary names `gfx.py flags`. The root skill is 57,937 bytes against its 58,000-byte ceiling, so its wiring section gained no further text; the size list keeps its numbers until step 7 introduces `profiles.json`.
- **Push routine (D11).** `CONTRIBUTING.md` asks for `python -B .tools/check.py full` before a pull request or push, with its dependencies and `HOI4_GAME_DIR`. The agent memory for the filtered push route lists it as the first step.

Observation for the owner of the relocated example: its `defined_text` sample writes `localisation_key`, while scripted localisation uses `localization_key`; it was moved verbatim, as D7 requires, and not corrected.

### Step 5: tests and quality (25 October 2026)

Status: `implemented`.

- **One test folder.** The 62 top-level `test_*.py` files and the 28 files of `.tools/validation/` moved with `git mv` into `.tools/tests/`, with the Event 012 fixture folder under `tests/fixtures/`. The folder is flat rather than split into `events/<id>/` and `systems/<system>/`, because the tests import each other by module name across families (the national policy and humanitarian tests load the Event 035 parser, the Event 032 tests load the CBRN reservation model); a flat folder keeps every import working when a file runs as a script and under `python -m unittest discover -s .tools/tests -p "test_*.py"`, which ran 613 cases successfully. Moved files had their repository-root depth, sibling `sys.path` entries and own-path literals updated. Two literals stay on the old path on purpose: the Event 033 evolution-controls archive key and the Event 035 handoff code, which is redirected in memory exactly as that test already patches it.
- **No imports from `docs/plans/`.** Fifteen JS tests loaded helpers from plan folders. `tests/lib/clausewitz_source_model.js` holds the five Event 033 parser helpers copied unchanged, and `tests/lib/universal_cost_source_model.js` holds the Event 026 universal-cost model with only its root depth changed; the originals stay in their plan folders as records. Tests that read evidence data from plan folders still do so.
- **No writes on import.** The humanitarian panel and national policy law and cost tests write their evidence only under `__main__` and create `.tmp/national_policy_panels/` themselves; `test_humanitarian_cost_display.py` creates it too. A run with that folder removed passed and an import wrote nothing. `test_cbrn_payload_reservations.py` loads its source model in `setUpClass`, so discovery runs its 43 cases.
- **Mengele audits retired (D12).** Both `.mjs` audits were removed with `git rm` and copied to `.tmp/archive/mengele_audits_2026-10-25/`; the three Mengele effect docs now label their recorded scenario counts as the last results of retired tools and point to `check.py`.
- **References.** Twenty-six active documents (`common/**/*.md`, `docs/events/`, `docs/specs/`, `docs/systems/`) and the codebase-cleanup skill now cite `.tools/tests/`; `.gitattributes` keeps its `-text -filter` pins on the moved Event 033 tests; historical plans, assets and testing evidence keep their old paths.
- **Ruff and mypy.** `ruff.toml` enables only defect rules plus the complexity ratchet; `quality.py` runs ruff and `mypy --strict` through `uvx` (`requirements-dev.txt` pins ruff 0.8.4 and mypy 1.14.1) and joins `check.py` as `quality`. The strict set (`lib/`, `check.py`, `quality.py`, `audit_script_rules.py`, `validate_scripts_mcp.py`, `gfx/gfx.py`, `sync/`, and the event-assets and save-inspection skill helpers) passes `mypy --strict` and has no ruff defect: about 290 type errors were fixed by annotation and minimal narrowing (no `type: ignore`, no relaxed flags; `gfx.py audit` output was byte-identical before and after, and all helper `--help` runs, GFX tests and sync checks still pass). Five broad `except Exception` clauses in `gfx.py` and `check.py` were narrowed or given a reasoned `noqa`. Everything else is held by `quality_baseline.json`: 365 entries across 121 files (221 functions over the complexity limit and 144 older defect findings, most in the hash-pinned 3D adapter and the event tests). `tests/test_quality_ratchet.py` proves that an extra defect, a grown function and a strict-file defect fail while recorded findings pass. `check.py full` takes 68 s and still exits 1 only on the formable generator failure and the four misfiled untracked route flags.
- **Differences from the plan text.** The test folder is flat (above). The 3D pipeline's own 42 tests stay in `3d_pipeline/tests/` and are not run by `check.py`, because they need the adapter environment. Tests that `git show` pinned commits still fail in a shallow clone. Of the baselined defects, `F821 Undefined name adapter` in `3d_pipeline/tests/blender_humanoid_component_review_integration.py:225` may be a real bug in a Blender-only integration probe and is listed below.

### Owner hand-offs

These findings came from the audit; per the plan they are reported to their owners rather than fixed inside the tooling change.

| Finding | Evidence | Proposed fix | Owner surface |
|---|---|---|---|
| Building icon strip frame count | `interface/countrystateview.gfx` sprite `GFX_buildings_strip` declares `noOfFrames = 35` for `gfx/interface/buildings/building_icon_strip.dds` (1,656x46). A contact sheet on a 46-px grid shows 36 icons, each in its own 46-px cell, so the engine slices 47.31-px frames and every icon after the first drifts. The 35 was set on 2 August (`34a22131be`, "Fix custom building interface coverage"); the texture was last changed in January | Set `noOfFrames = 36`, then check every `frame =` index that points into this strip | Building interface (`interface/countrystateview.gfx`) |
| DHR flag origin | `gfx/flags/DHR_democratic.tga` and `DHR_neutrality.tga`, and their `medium/` and `small/` copies, are top-origin TGAs; the flag rule in `chaos-redux-event-assets/references/event-images-and-flags.md` forbids that, while vanilla ships 5 of 2,203 flags that way (D4) | If the flags display upside down, rewrite the six TGAs bottom-origin with the same pixels | DHR country package |
| Event 038 parchment colour code | `chaosx.nr38.42.d` (the `desc` of the event at `events/038_malta_crusaders.txt:812`, localisation line 136) wraps `[FROM.GetMaltaPrStatus]` in `§Y…§!`, which the `chaos-redux-events` parchment rule forbids; `report_colour_audit.py` reports it | Remove the `§Y`/`§!` codes and keep the plain status text | Event 038 localisation |
| Leftovers of the removed Acid Rain pacing override | After `1927a7901c`, nothing sets `acid_rain_cluster_pacing_type_@var:…`, yet `chaosx_event_cluster_effects.txt` still clears it at lines 2962 and 4376, and `event_cluster_get_effective_pacing_type` still sets the unused temporary `event_cluster_acid_rain_pacing_row_index` (line 2913) | Remove the three dead lines with `chaos-redux-codebase-cleanup` | Event cluster system |
| Formable state-puzzle generator cannot reproduce its outputs | `node .tools/generate_formable_state_puzzle_runtime.mjs --check` stops with "Duplicate normalized decision category manifest" because the committed FORM-17, 32, 36 and 37 manifests (group `independence_wave_formables`, unchanged since `10b26112c4`, 7 October) share `independence_wave_ready_formable_routes_category`. The committed `common/scripted_guis/chaosx_formable_state_puzzles.txt` mentions `independence_wave_form37` six times and FORM-17, 32 and 36 not at all, so the generated files and the manifests disagree | Decide whether grouped members may share a category (then exempt same-group members from the duplicate guard) or the manifests are wrong, regenerate, and review the four puzzles' runtime surfaces | Event 006 formable package |
| Misfiled untracked route flags | `gfx/flags/route_black_apostolate_{medium,small}.tga` and `route_herald_of_zol_{medium,small}.tga` sit in the normal-size flag folder; 18 untracked `*_planned` flags exist only in `medium/` and `small/` | Move the medium and small files into their folders before committing, and add normal-size files for the planned flags | The sessions producing those flags |
| Candidate files in the runtime achievement folder | 33 tracked `gfx/achievements/chaosx_081_*__shard6_c0N.dds` files were added on 11 October as icon alternatives (`121ff730ce`); no script, interface or localisation file names them, so the game never loads them | Choose the final icons, then move the unused alternatives to the Event 081 asset workspace or the LFS archive the event-assets skill describes | Event 081 assets |
| Undefined name in a Blender integration probe | Ruff `F821`: `adapter` is undefined at `.tools/3d_pipeline/tests/blender_humanoid_component_review_integration.py:225`, so that path raises `NameError` when reached; the file is outside the adapter hash lock but runs only inside Blender | Define or import `adapter` there, then rerun the probe in Blender and run `quality.py --write-baseline` to drop the entry | 3D model pipeline |
| HOI4 Agent Tools known-mistake false positive | `KNOWN_MISTAKE_TEMP_VARIABLE_SCOPE_PREFIX` treats `constant:<category>.event_id` as a scoped temporary variable (eight reports in `chaosx_event_cluster_effects.txt`, lines 1466–1657) | Report it in the HOI4 Agent Tools repository with these lines as a reproduction | HOI4 Agent Tools |

## Appendix: how the measurements were taken

All commands ran read-only from the mod root on 25 October 2026; their outputs are in the session scratchpad, not the repository.

- `python -B .tools/audit_localisation_static.py --json <tmp>`, likewise for the asset and script-reference audits.
- `python -B .tools/reindent_script_files.py --check`, `python -B .tools/check_structural_indentation.py --check`, `python -B .tools/sync/sync_read_limits.py --check`, `python -B .tools/sync/sync_agents.py --verify`.
- Pillow size surveys over `gfx/interface/{goals,decisions,ideas}`, `gfx/event_pictures`, `gfx/flags*`, `gfx/achievements` and the counter folders, in both the mod and the installed game.
- A comment- and string-aware scan for `<=`, `>=`, `= -<token>` and `key:N "` patterns.
- A `.gfx` scan comparing texture width with `noOfFrames` for every multi-frame sprite with a local texture (572 sprites, 431 local and checkable).
- An AST scan of `.tools/` and skill Python for annotations, function length, complexity and swallowed exceptions.
- `hoi4_script_validate` on `events/chemical_warfare_events.txt` (valid, six checks performed).
