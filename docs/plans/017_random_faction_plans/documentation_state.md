# Event 017 Random faction documentation state

Date: 2026-07-02
Scope: Event 017 `Random faction` documentation reconciliation after implementation work.

This ledger records documentation state only. It does not claim gameplay completion. Final completion remains blocked on the parent and/or `chaosx_event_completion_auditor`.

## Cleanup Scope

Read and reconciled:

- `AGENTS.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `docs/specs/017_random_faction_specs/`
- `docs/events/017_random_faction.md`
- `docs/systems/event_clusters.md`
- `docs/assets/017_random_faction/manifest.md`
- `docs/assets/017_random_faction/gfx_handoff.md`
- `docs/plans/017_random_faction_plans/subagent_handoffs/`
- Targeted implementation evidence from `events/017_join_faction.txt`, `common/scripted_effects/017_random_faction_effects.txt`, `common/scripted_triggers/017_random_faction_triggers.txt`, `common/decisions/017_random_faction_decisions.txt`, `common/achievements/chaos_redux_achievements.txt`, `interface/017_random_faction.gfx`, `interface/chaosx_achievements.gfx`, and `localisation/english/017_join_faction_l_english.yml`.

No gameplay, localisation, asset binary, GFX, GUI, spreadsheet, achievement, event, decision, scripted effect, scripted trigger, or workbook file was edited by this documentation pass.

## Source-of-Truth Map

| Surface | Current disposition | Notes |
| --- | --- | --- |
| `docs/specs/017_random_faction_specs/specs/017_random_faction_spec_part_1_core.md` | Accepted source spec | Defines dynamic minor/faction selection, player one-to-four forced choices, baseline pressure, log, and cluster role. |
| `docs/specs/017_random_faction_specs/specs/017_random_faction_spec_part_2_bloc_pressure_and_decisions.md` | Accepted source spec | Defines Bloc Pressure category, selected-minor, pressured-neutral, and faction-leader decision families. |
| `docs/specs/017_random_faction_specs/specs/017_random_faction_spec_part_3_evolutions_ai_balance.md` | Accepted source spec | Defines Evolutions I-III, AI and balance intent, caps, and edge cases. |
| `docs/specs/017_random_faction_specs/specs/017_random_faction_spec_part_4_implementation_assets_acceptance.md` | Accepted source spec plus acceptance checklist | Helper and asset names are working names; current implementation uses some renamed helpers documented below. Acceptance still belongs to the parent/completion auditor. |
| `docs/specs/017_random_faction_specs/matrices/*.md` | Supporting accepted design material | AI, decision, scripted-system, and catalog matrices remain useful as design references. Some working ids were renamed during implementation. |
| `docs/specs/017_random_faction_specs/research/017_random_faction_research_notes.md` | Historical inspiration only | Not final localisation and not implementation evidence. |
| `docs/specs/017_random_faction_specs/prompts/*.md` | Pre-implementation prompt package | Keep as historical routing instructions. Do not treat as current state proof. Completion-auditor and any missing spreadsheet handoff remain relevant. |
| `docs/events/017_random_faction.md` | Current implementation-facing event documentation | Describes the runtime architecture, decisions, evolutions, event log, achievements, cleanup, and asset wiring visible in current files. |
| `docs/systems/event_clusters.md` | Current cluster documentation | Records Event 17 as a Diplomatic Panic optional low-danger member with 65% participation and dynamic faction eligibility. |
| `docs/assets/017_random_faction/manifest.md` | Current asset manifest | Updated by this pass to state the asset subagent stalled and main completed runtime DDS processing locally from generated source art. |
| `docs/assets/017_random_faction/gfx_handoff.md` | Current GFX handoff | Runtime sprite paths and validation summary for Event 17 DDS outputs. |
| `docs/plans/017_random_faction_plans/subagent_handoffs/2026-07-02_bloc_pressure_decision_audit_patch.md` | Implemented patch handoff | Decision/mission audit patch is evidence for decision surface changes. Its static-category-header note is superseded by later localisation/docs evidence, and later parent changes resolved per-leader corridor target mapping. |
| `docs/plans/017_random_faction_plans/subagent_handoffs/2026-07-02_random_faction_localisation_audit_handoff.md` | Implemented localisation audit handoff | Localisation patch was applied and key coverage checked. Its spreadsheet stale note is superseded by the follow-up spreadsheet handoff. |
| `docs/plans/017_random_faction_plans/subagent_handoffs/2026-07-02_random_faction_spreadsheet_update_handoff.md` | Implemented spreadsheet handoff | Records the Event 17 workbook row update after the localisation audit. |
| `docs/spreadsheets/chaos_redux_events_catalog.xlsx` | Updated by second spreadsheet worker | Workbook row for Event ID 17 mirrors final Event Details and Evolution III wording. |

## Implementation Evidence Checked

This pass used targeted text evidence only. It did not perform a completion audit.

| Claim checked | Evidence |
| --- | --- |
| Event namespace and visible Event 17 chain exist | `events/017_join_faction.txt` contains `add_namespace = chaosx.nr17` and events `chaosx.nr17.1`, `.10`, `.20`, `.30`, `.40`, `.50`, `.60`, `.70`, `.80`, `.81`, `.82`, `.84`, and `.86`. |
| Shared runtime helpers exist | `common/scripted_effects/017_random_faction_effects.txt` contains `random_faction_prepare_runtime_context`, `random_faction_collect_faction_options`, `random_faction_join_selected_faction`, `random_faction_reopen_dead_faction_file`, `random_faction_run_evo1_regional_bloc_race`, `random_faction_run_evo2_pressure`, `random_faction_run_evo3_cascade`, `random_faction_record_current_evolution`, and cleanup helpers. |
| Current trigger names exist | `common/scripted_triggers/017_random_faction_triggers.txt` contains `is_random_faction_eligible_country`, `is_random_faction_allowed_faction_leader`, `random_faction_is_valid_faction_leader_for_root_target`, `can_random_faction_join_faction`, `random_faction_region_can_cascade`, mission objective triggers, and cost triggers. |
| Bloc Pressure decisions exist | `common/decisions/017_random_faction_decisions.txt` contains the documented selected-minor, pressured-neutral, and faction-leader decisions plus missions and AI weights. |
| Achievement ids and sprites exist | `common/achievements/chaos_redux_achievements.txt` and `interface/chaosx_achievements.gfx` contain all six Event 17 achievement ids/sprites. |
| Event 17 sprite registry exists | `interface/017_random_faction.gfx` contains Event 17 report, decision, idea, animated, and fallback sprite names. |
| Event name/detail/evolution localisation exists | `chaosx_event_names_l_english.yml` maps `chaosx.event_name.17` to `Random faction`; `017_join_faction_l_english.yml` contains Event 17 event-detail and evolution-detail keys. |

## Plan and Handoff Disposition

| Item | Disposition | Reason / follow-up |
| --- | --- | --- |
| Four-part Event 17 source spec | Accepted source design | Keep in `docs/specs/017_random_faction_specs/specs/`. Do not rewrite into post-hoc implementation docs. |
| AI matrix | Accepted supporting design | Current implementation should still be audited by completion auditor for AI behavior; this curator only verified named surfaces exist. |
| Decision map | Implemented with patch evidence | Decision audit handoff records mission/cost patches. Later parent changes resolved per-leader corridor target mapping through `random_faction_corridor_targets` and added dynamic decision-category status localisation. Selected-target browsing is not required because the source spec makes it conditional on an existing repository pattern; current targeted decisions use validated target arrays. Costs are concrete, centralised constants with conditional risk costs in effects. |
| Scripted-system architecture matrix | Implemented with renamed helper ids | Current helper names differ from several working labels, but current docs/events records implementation names. Completion auditor should decide whether behavior satisfies the spec. |
| Catalog handoff matrix | Superseded by final localisation plus spreadsheet-worker handoff | Keep as historical direction. The follow-up spreadsheet handoff records the workbook row update after localisation audit. |
| Asset prompt | Superseded for production path | Asset subagent stalled and was shut down. Main completed runtime DDS locally from generated source art and wrote manifest/GFX handoff. |
| Achievement prompt | Implemented according to visible ids; completion not claimed | Achievement ids and sprite triplets exist. Unlock behavior requires completion audit. |
| Coding/goal prompts | Historical implementation instructions | Keep as pre-implementation prompts. Do not re-run all tasks from them unless parent reopens a specific gap. |
| Subagent routing prompt | Implemented route with documented local asset completion | Decision audit, localisation audit, spreadsheet update, and documentation cleanup handoffs exist. Asset production was completed locally after subagent stall and is documented in the asset manifest/GFX handoff. Completion auditor remains queued before final completion claim. |
| `2026-07-02_bloc_pressure_decision_audit_patch.md` | Implemented patch handoff | Static category header finding is superseded by later dynamic status localisation evidence. Corridor target mapping was resolved by leader-local `random_faction_corridor_targets`. Broader target browsing and cost scaling remain optional/future tuning, not Event 17 completion blockers. |
| `2026-07-02_random_faction_localisation_audit_handoff.md` | Implemented localisation audit handoff | Spreadsheet stale finding is superseded by the follow-up spreadsheet handoff. The faction-leader reaction now names the aligned minor through `random_faction_target_country`. |
| `2026-07-02_random_faction_spreadsheet_update_handoff.md` | Implemented spreadsheet handoff | Documents the Event 17 workbook row update after final localisation. |

## Contradictions and Resolutions

| Status | File(s) | Evidence | Resolution |
| --- | --- | --- | --- |
| Resolved by this pass | `docs/assets/017_random_faction/manifest.md` | Manifest attributed generated source and processing to the Event 17 asset subagent, but parent reports the asset subagent stalled and main completed runtime DDS processing locally. | Manifest now records the subagent stall/shutdown and local main-pass DDS processing. |
| Resolved/superseded | `2026-07-02_bloc_pressure_decision_audit_patch.md` vs `docs/events/017_random_faction.md` / `017_join_faction_l_english.yml` | Decision audit says category header remained static. Later docs/localisation show `[GetRandomFactionBlocPressureStatus]` and faction-aware status lines. | Treat the decision-audit note as superseded by the later localisation patch and current event doc. |
| Resolved | `2026-07-02_random_faction_localisation_audit_handoff.md` vs spreadsheet update | Localisation audit says spreadsheet row 17 still had old wording. The follow-up spreadsheet handoff records the updated Details and Evo III cells. | Treat the spreadsheet stale note as superseded. |
| Working-name mismatch, not a blocker | Spec/matrix vs implementation | Specs use working labels such as `is_random_faction_valid_faction_leader`, `random_faction_schedule_followup`, and `random_faction_clear_pressure`; implementation uses `is_random_faction_allowed_faction_leader`, `random_faction_is_valid_faction_leader_for_root_target`, evolution-specific helpers, and `random_faction_clear_current_country_pressure`. | Current implementation doc records actual names. Completion auditor should evaluate behavior, not literal working names, unless parent requires exact ids. |

## Duplicate or Superseded Documents

| Document | Disposition |
| --- | --- |
| `docs/specs/017_random_faction_specs/prompts/017_random_faction_asset_prompt.md` | Superseded as production route; still useful as original asset scope. |
| `docs/specs/017_random_faction_specs/prompts/017_random_faction_coding_prompt.md` | Historical implementation prompt; current state is in event docs, handoffs, manifest, and this ledger. |
| `docs/specs/017_random_faction_specs/prompts/017_random_faction_goal_prompt.md` | Historical goal prompt; do not use as completion proof. |
| `docs/specs/017_random_faction_specs/prompts/subagents/*.md` | Historical routing prompts. `chaosx_event_completion_auditor_prompt.md` remains useful for the next completion-audit pass. |
| `docs/specs/017_random_faction_specs/matrices/017_random_faction_catalog_handoff.md` | Superseded by final localisation and parent-reported spreadsheet worker update for current catalog wording. |
| `docs/specs/017_random_faction_specs/source_review/full_read_manifest.md` | Historical planning package context only; it accurately says no checkout/subagent runtime existed during planning and should not be treated as current implementation state. |

## Stale Prompt or Instruction List

- Asset prompt still says an asset subagent should produce final DDS, contact sheets, manifest, and GFX handoff. Current state: subagent stalled; main completed DDS locally.
- Coding/goal prompts say to use several subagents "at minimum." Current route has decision, localisation, spreadsheet, documentation, and completion-auditor routing, plus local main asset completion after the asset subagent stalled.
- Localisation audit handoff's spreadsheet-stale note is superseded by the follow-up spreadsheet update handoff.

## Remaining Parent Decisions

- Run or route `chaosx_event_completion_auditor` before any completion claim.
- Review any completion-auditor findings that identify a required behavior gap.

## Validation

- Opened the required offline wiki core pages through the local `paradox_wiki/` snapshot before patching docs.
- Read the Event 17 source spec package, current event doc, cluster doc, asset manifest/GFX handoff, and the two Event 17 handoffs present under `docs/plans/017_random_faction_plans/subagent_handoffs/`.
- Ran targeted `rg` checks for old names and stale references including `Choose faction`, `Axis`, `Comintern`, `random_faction_schedule_followup`, `random_faction_select_ai_option`, `random_faction_region_can_cascade`, and `GFX_report_event_random_faction_regional_cascade`.
- Ran targeted `rg` checks confirming key current implementation identifiers in the named event, effect, trigger, decision, achievement, GFX, and localisation files.
- Ran `git status --short`; the Event 17 workbook is modified in the broader worktree, but this documentation pass did not inspect or edit the workbook.

## Skipped Validation

- Did not inspect binary DDS or generated image files.
- Did not open or edit `docs/spreadsheets/chaos_redux_events_catalog.xlsx`; spreadsheet work belongs to `chaosx_spreadsheet_doc_worker`, and the parent specifically scoped this pass away from spreadsheet edits.
- Did not run a gameplay completion audit or HOI4 launch.

## Remaining Documentation Risks

- Spreadsheet parity is documented in `2026-07-02_random_faction_spreadsheet_update_handoff.md`; the older localisation-audit stale note should be treated as superseded.
- Pre-implementation prompt files remain in the source spec package. This ledger marks their disposition, but they are not modified because they are useful historical routing artifacts.
- Current docs describe implementation surfaces as evidence, not as final approval. Completion status remains intentionally unclaimed.
