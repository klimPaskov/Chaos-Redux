# Event 020 documentation reconciliation handoff

Date: 2026-08-06

## Scope and outcome

This documentation-only pass reconciles the accepted Event 020 source package, current runtime overview, focus and GUI audit, shared rat model handoff, plans, prompts, and reviews after the 2026-08-05 model promotion. It does not claim gameplay, sound, counter, GUI, spreadsheet, or live in-game completion.

The current source map is [`../documentation_state.md`](../documentation_state.md), and the parent resume packet is [`../resume_packet.md`](../resume_packet.md).

## Files changed

- `docs/specs/020_black_plague_specs/README.md`
- `docs/specs/020_black_plague_specs/manifest.md`
- `docs/specs/020_black_plague_specs/matrices/asset_inventory.md`
- `docs/specs/020_black_plague_specs/review/source_of_truth_and_plan_disposition.md`
- `docs/specs/020_black_plague_specs/review/limitations_and_blockers.md`
- `docs/specs/020_black_plague_specs/review/completion_audit.md`
- `docs/specs/020_black_plague_specs/review/package_validation.md`
- `docs/specs/020_black_plague_specs/prompts/black_plague_coding_prompt.md`
- `docs/specs/020_black_plague_specs/prompts/black_plague_goal_prompt.md`
- `docs/specs/020_black_plague_specs/prompts/black_plague_decision_mission_prompt.md`
- `docs/events/020_black_plague/overview.md`
- `docs/events/020_black_plague/rat_route_depth.md`
- `docs/events/020_black_plague/rat_king_depth.md`
- `docs/events/020_black_plague/rat_route_modules.md`
- `docs/plans/020_black_plague_plans/2026-07-29_event20_core_readiness_report.md`
- `docs/plans/020_black_plague_plans/2026-08-01_event20_consequence_and_aftermath_addendum.md`
- `docs/plans/020_black_plague_plans/2026-08-01_event20_content_tranche_handoff.md`
- `docs/plans/020_black_plague_plans/2026-08-02_event20_aftermath_recovery_handoff.md`
- `docs/plans/020_black_plague_plans/2026-08-02_event20_scenario_content_handoff.md`
- `docs/plans/020_black_plague_plans/2026-08-05_focus_gui_mcp_layout_audit.md`
- `docs/plans/020_black_plague_plans/documentation_state.md`
- `docs/plans/020_black_plague_plans/resume_packet.md`

No gameplay, event script, focus source, decision, localisation, GUI, GFX, model, sound, image, DDS, asset, spreadsheet, or export-only CSV file was edited.

## Promotion, supersession, and disposition

- The 2026-08-05 shared rat ground-unit model handoff is the current model authority for one `black_plague_rat_mesh`/`black_plague_rat_entity` package serving six RTA/RTX subunits and five locked templates.
- The shared model brief is promoted into the current runtime evidence set, while per-subtype and separate Rat King model proposals remain rejected.
- The current active specs, event docs, reviews, prompts, and plans now use 52 RTA focuses and 71 RTX focuses.
- The 2026-08-02 documentation reconciliation handoff is superseded for its 51/71 count and blanket no-model claims; its two-tag and historical audit evidence remains archive-only.
- The 2026-08-01 content tranche, consequence/aftermath addendum, 2026-07-29 readiness report, 2026-08-02 recovery/scenario handoffs, and 2026-08-05 layout audit now carry scoped current overrides instead of denying the separately promoted model package.
- Older subagent handoffs and prompts that retain no-model, 51-focus, or retired-count language remain historical records; the parent must use `documentation_state.md` and this handoff as current instructions.
- The event catalog workbook and derived CSVs remain unchanged and parent/spreadsheet-worker owned.

## Contradictions resolved

- The old RTA 51 count and 51/70 floor wording were replaced by source/MCP-confirmed 52 RTA and 71 RTX counts in active documentation.
- The old blanket “no bespoke model” boundary was replaced by the accepted one-shared-model boundary, with per-subtype and separate Rat King models still rejected.
- Static worker/runtime model evidence is now separated from parent-owned sound definitions, counter review, and live in-game validation.
- The 2026-08-05 focus/GUI layout audit is explicitly scoped so its “not produced in this pass” wording cannot negate the separate shared model handoff.

## Contradictions still open

- The event-scoped `docs/assets/020_black_plague` source/provenance records were restored from the repository after this documentation pass; the separate worker evidence directory `docs/assets/020_black_plague/models_3d/rat_ground_unit_shared/` remains absent, so provider-output retention is still unverified.
- Four sound candidates remain `needs_user_review`, with no accepted impact/contact source, parent sound-definition wiring, or live playback proof.
- Bespoke counter art is installed according to the handoff but remains review-gated, and no live counter visual validation is claimed.
- `hoi4.event_inspect` timed out twice after 180 seconds, so no event-level MCP artifact is available for `chaosx.nr20.1` in this pass.
- Focus MCP reported 14 generic vanilla continuous-focus palette diagnostics per tree and Event 020 layout-detour warnings; no Event 020-owned blocking reference or geometry failure was reported.
- GUI MCP returned a seven-element bounded header artifact but also inline-source truncation, missing/unsupported scripted-context diagnostics, and global overlap findings outside the bounded header; the full board remains unverified.

## Markdown hard-wrap audit

- New and directly patched prose in this pass keeps each sentence on one physical line and preserves deliberate Markdown headings, lists, tables, and code spans.
- Historical core-readiness and older handoff bodies contain inherited mid-sentence wraps; they remain archive evidence and were not flattened in this pass because flattening them would rewrite audit provenance.
- No hard-wrap correction was applied to gameplay, localisation, GUI, GFX, asset, model, sound, or spreadsheet files.

## Validation performed

- Targeted `rg` checks confirmed that active Event 020 specs, reviews, prompts, event docs, route docs, and current plans no longer contain the old 51-focus or blanket no-model phrases.
- The source files and handoff paths were checked against the current Event 020 tree and the documented runtime model paths.
- The focus MCP national inspections and bounded GUI MCP inspection were preserved as evidence with their artifact URIs in `documentation_state.md` and `resume_packet.md`.
- The event MCP route was attempted twice and the exact timeout was recorded rather than treating source-only inspection as equivalent.
- The workbook, binary assets, and live game were intentionally skipped because they are outside documentation-curator ownership and live validation is parent/user-owned.

## Parent decisions required

- Decide whether the absent temporary model evidence directory is intentionally archived or needs provenance recovery from the retained model handoff; do not invent provider outputs.
- Accept, reject, or block the sourced sound roles and then wire parent-owned sound definitions without unlicensed or synthetic fallback.
- Visually review the bespoke counters and record the result in the durable model handoff.
- Run live HOI4 validation for model consumers, counters, event chain, SCN-012, missions, GUI, audio, and balance.
- Route any catalog wording changes through the authoritative workbook and exporter after implementation facts settle.

## Completion boundary

The documentation set is reconciled for current model/runtime/audit facts, with a source-of-truth map and resume packet delivered. Gameplay completion, asset completion, sound completion, GUI completion, spreadsheet completion, and live validation are not claimed.
