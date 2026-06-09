# Event006 Completion Audit - Current Corrections

Date: 2026-06-05 17:00:31 UTC  
Agent: chaosx_event_completion_auditor  
Scope: read-only audit. This markdown report is the only file changed.

## Sources Consulted

- Repository instructions from `AGENTS.md`.
- Skills: `.agents/skills/chaos-redux-events/SKILL.md` and `.agents/skills/chaos-redux-subagents/SKILL.md`.
- Required Event006 specs/plans:
  - `docs/specs/006_independence_wave_specs/006_independence_wave_spec.md`
  - `docs/specs/006_independence_wave_specs/006_independence_wave_focus_trees.md`
  - `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md`
  - `docs/specs/006_independence_wave_specs/006_independence_wave_decisions_ai.md`
  - `docs/specs/006_independence_wave_specs/006_independence_wave_assets_prompt.md`
  - `docs/specs/006_independence_wave_specs/006_independence_wave_super_event_prompt.md`
  - `docs/specs/006_independence_wave_specs/006_independence_wave_achievements_prompt.md`
  - `docs/specs/006_independence_wave_specs/006_independence_wave_coding_prompt.md`
  - `docs/specs/006_independence_wave_specs/006_independence_wave_catalog_update.md`
  - `docs/specs/006_independence_wave_specs/006_independence_wave_research_notes.md`
  - `docs/plans/006_independence_wave_plans/source_of_truth_map.md`
  - `docs/plans/006_independence_wave_plans/006_independence_wave_improvement_loop_gate.md`
  - `docs/plans/006_independence_wave_plans/006_independence_wave_improvement_addendum_post_focus_formation_tranche.md`
  - `docs/events/006_independence_wave.md`
- Required offline Paradox wiki pages from `paradox_wiki/`, including data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, AI modding, national focuses, country creation, unit modding, and division modding.
- Vanilla documentation under `~/projects/Hearts of Iron IV/documentation/` and relevant common-system documentation files.
- Current implementation surfaces under `events/`, `common/`, `localisation/`, `interface/`, `history/`, `gfx/flags/`, `docs/assets/`, and `docs/spreadsheets/`.

Spreadsheet note: `openpyxl` was not available in the local Python environment, so the workbook audit was limited to inspecting `xl/sharedStrings.xml` through `unzip`.

## Executive Finding

Event006 should not be claimed fully complete yet. The core runtime implementation substantially matches the current user corrections: KUB/ALT are excluded from active candidate scope, the released-country focus tree is shared/generic, released countries receive startup army support, the news event can list all releases, evolution logs are limited to chaos-tier milestones, and inspected Event006 files do not depend on Event005 state.

The remaining blockers are mostly completion-claim and consistency blockers rather than obvious immediate runtime blockers: stale catalog/spreadsheet text still describes superseded KUB/ALT and a 125-focus tree, stale KUB/ALT package remnants remain in Event006 AI/idea files, and Event005-side separation has not been exhaustively proven from every Event005 loader/decision path.

## Current Corrections Check

| Correction | Audit status | Evidence |
| --- | --- | --- |
| KUB/ALT must not be expanded as Event006 package scope unless reopened. | Mostly satisfied, with stale remnants. | `can_independence_wave_use_candidate_tag` excludes `tag = KUB` and `tag = ALT`. Current specs/source map mark KUB/ALT superseded. However, Event006 AI/idea remnants still reference old KUB/ALT package surfaces. |
| Focus trees for released countries must stay generic/shared. | Satisfied in current implementation. | `common/national_focus/006_independence_wave_focus.txt` has one shared `independence_wave_liberation_provisional_tree`, gated by `is_independence_wave_release = yes`. No republic-specific stacked focus tree was found. |
| Released countries need starting units, ability to build an army, and generic ways to expand beyond one state. | Satisfied at core level. | `independence_wave_setup_released_country` adds manpower, infantry equipment, support equipment, a 4-infantry provisional template, two startup units, one arms factory, and loads the shared focus tree. Expansion is represented through generic focus/decision structures such as border commission and provisional governance. |
| Independence Wave news should display all countries released. | Satisfied for the implemented release-count ceiling. | The event stores current-wave countries in `global.independence_wave_country_1` through `global.independence_wave_country_16`; scripted localisation `GetIndependenceWaveReleasedCountryList` supports lists from 1 to 16; news localisation prints the count and the full generated list. |
| Evolution logs should be only a few actual chaos-tier stages, not per-wave progression. | Satisfied. | `independence_wave_record_tier_evolution` records four milestone stages only: gathering storm, rising cascade, old names, and impossible statehood. No active call was found that records every individual release as an evolution stage. |
| Event006 must be independent from Event005 systems. | Mostly satisfied from the Event006 side; needs Event005-side audit. | Event006 setup uses `chaosx_release_origin_independence_wave`, `chaosx_release_origin = 6`, and `is_independence_wave_release`. Inspected Event006 script/focus/AI files do not read `soviet_collapse` or Event005 route state. Full proof requires an Event005-side audit of loaders, decisions, and on-action hooks. |

## Critical Missing or Blocking Items

1. Stale catalog/spreadsheet row blocks a full completion claim.
   - `docs/spreadsheets/chaos_redux_events_catalog.xlsx` still contains strings describing a "shared 125-focus Liberation Provisional tree" and current Evo IV proofs including Kuban/KUB and Altai/ALT.
   - This contradicts the current implementation and user corrections. The implementation currently has 50 shared focuses, and KUB/ALT are explicitly out of Event006 active package scope.
   - This is not a runtime script blocker, but it is a completion blocker because Event006 documentation/catalog surfaces are required to stay aligned.

2. Stale KUB/ALT package implementation surfaces remain.
   - `common/ai_strategy/006_independence_wave.txt` still has old-name package AI conditions for `independence_wave_package_kuban`, `independence_wave_package_altai`, `independence_wave_kuban_black_sea_records_opened`, and `independence_wave_altai_oyrot_records_opened`.
   - `common/ideas/006_independence_wave_ideas.txt` still defines `independence_wave_kuban_cossack_rada_spirit` and `independence_wave_altai_kurultai_spirit`.
   - Because KUB/ALT candidate tags are blocked, these appear unreachable in normal Event006 flow. They still contradict the cleanup intent unless deliberately retained as parser-stable inactive remnants and documented as such.

3. Event005 separation is not fully proven from the Event005 side.
   - Event006 origin setup and focus loading are independent in inspected Event006 files.
   - The remaining risk is whether any Event005 decision, focus loader, setup effect, AI strategy, or on-action path can still touch countries with `chaosx_release_origin_independence_wave`.
   - A dedicated Event005-origin exclusion audit should happen before final completion.

4. Dynamic truce duration should be parser-verified.
   - Event006 uses `set_truce = { ... days = independence_wave_release_truce_days }` after assigning a script constant to a temp variable.
   - The repository instructions warn that some duration fields reject constants or dynamic values. I did not find direct proof in this audit that `set_truce days` accepts a variable token.
   - This needs a parser/load validation or replacement with a known-supported form.

5. The docs still acknowledge incomplete follow-up surfaces.
   - `docs/events/006_independence_wave.md` lists queued future items including remaining package data, package-specific decisions, and catalog/spreadsheet/event-detail alignment.
   - That is appropriate as an honest status note, but it means the full long-term Event006 spec should not be represented as finished unless those items are explicitly reclassified as future scope.

## Spec Contradictions and Stale Source-Of-Truth Issues

- The source-of-truth map and current event documentation correctly say KUB/ALT are superseded, but some older implementation surfaces still contain KUB/ALT AI and idea definitions.
- The spreadsheet/catalog workbook is stale against the current source-of-truth docs because it still describes KUB/ALT as current proofs and a 125-focus tree.
- `006_independence_wave_catalog_update.md` still reads as a proposed catalog/achievement update surface rather than a verified current-state manifest. It should be reconciled after the implementation facts are finalized.
- Research notes contain older package flavor guidance, including notes that are no longer authoritative for the current generic/shared-release lane. The source map correctly says research notes do not override current user corrections, but stale research language can still mislead future implementers.
- Event-log/localisation helper text for release dossiers and package detail exists beyond the active tier evolution calls. This is not necessarily wrong if it supports event details, but docs should clearly distinguish active chaos-tier evolution rows from auxiliary detail/dossier text.

## Stale Docs, Manifests, and Data Surfaces

- `docs/spreadsheets/chaos_redux_events_catalog.xlsx` is the highest-priority stale data surface.
- `docs/events/006_independence_wave.md` is mostly aligned with current corrections but still openly lists future implementation and alignment tasks.
- `docs/plans/006_independence_wave_plans/source_of_truth_map.md` is useful and current, but it still notes that unused helpers may remain for parser stability. Any retained inactive helper should be named explicitly or removed to avoid ambiguity.
- Asset manifests were present for Event006 report/news image work, but this audit did not perform a binary DDS dimension/format validation pass.
- No spreadsheet edits were made, per the read-only audit instruction.

## Validation Performed

- Checked brace balance across current Event006 focus, effect, trigger, event, and decision files. The audited set balanced to zero.
- Counted current shared focus tree structure: 50 `focus = {` blocks, 50 `ai_will_do` blocks, 50 `completion_reward` blocks, and 50 focus icons in `common/national_focus/006_independence_wave_focus.txt`.
- Verified `is_independence_wave_release` origin gating and Event006 setup path in scripted triggers/effects.
- Verified news release-list support through global current-wave country variables and scripted localisation from 1 through 16 releases.
- Verified evolution logging calls are tier-milestone based, not per-release progression based.
- Verified current candidate trigger exclusions for KUB and ALT.
- Inspected XLSX shared strings for stale Event006 catalog text.

## Validation Gaps

- No in-game load, error-log, or parser validation was performed by this read-only subagent.
- Spreadsheet validation was limited because `openpyxl` was unavailable.
- Event005-side separation was sampled but not exhaustively audited.
- DDS/image dimensions and `.gfx` sprite renderability were not fully validated.
- Package-specific balance and AI behavior were not line-by-line validated beyond the current corrections.
- No live scenario validation was possible for release count, host survival, border commission behavior, or post-release army buildup.

## Next Implementation Priorities

1. Reconcile the catalog/spreadsheet to the current Event006 state: 50-focus shared tree, no active KUB/ALT package scope, all released countries shown in news, four chaos-tier evolution milestones, and independent Event006 origin.
2. Remove, neutralize, or explicitly document the stale KUB/ALT Event006 AI/idea remnants. If they are retained only for parser stability, name them as inactive retained surfaces in the source map.
3. Run a dedicated Event005 separation audit and patch any Event005 focus loaders, decisions, on-actions, AI strategies, or setup effects that can still affect Event006-origin countries.
4. Parser-verify `set_truce days = independence_wave_release_truce_days`; if unsupported, replace it with a known-supported constant or variable pattern.
5. Decide which queued items in `docs/events/006_independence_wave.md` are completion blockers versus explicitly future scope, then update specs/source map/catalog accordingly.
6. Complete a final assets and UI validation pass for Event006 news/report images, sprite definitions, and manifest alignment.
7. Re-run a full localisation/key audit after stale KUB/ALT and catalog surfaces are cleaned.

## Completion Judgment

Event006 is close to satisfying the current user corrections at the gameplay-script level, but it is not ready for a full completion claim. The main blockers are stale external documentation/catalog data, stale inactive KUB/ALT implementation remnants, incomplete Event005-side separation proof, and one dynamic-duration parser validation gap.

No gameplay, localisation, asset, or spreadsheet files were modified by this audit.
