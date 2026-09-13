# Later scripted effects startup repair handoff

Status: source repair complete and frozen for parent startup validation; probability comparison remains parent-owned.
The final release section below supersedes the earlier pending-work list.
Ownership: 027/031/033/035 scripted effects and 027/029 triggers; 032 missile files were transferred to a separate worker before edits.
No commit created.
Pre-edit bytes are preserved under `baseline/scripts/<relative path>`.
`script_later_changes.diff` compares these backups against the seven edited files, including untracked files that ordinary Git diff omits.

## Completed source repairs

| File | Repair |
|---|---|
| `common/scripted_effects/031_random_terror_effects.txt` | Four infrastructure, arms-factory, and naval-base damage operations use existing `damage_state_building_dynamic`, with the same building tokens and original minor/major constants. No weight tokens changed. |
| `common/scripted_effects/033_acid_rain_achievement_effects.txt` | Removed eight unsupported manual clears of local event targets after exact identifier read/write review. |
| `common/scripted_effects/033_acid_rain_effects.txt` | Added missing `var =` in the global dissipation-date comparison. |
| `common/scripted_effects/033_acid_rain_preparedness_effects.txt` | Migrated selected transaction state pointer to a regular country scope variable with real explicit invalidation; corrected `acid_rain_urgent_cost.evacuate_*` consumers to existing `evacuation_*` constants per root instruction. |
| `common/scripted_effects/035_great_depression_effects.txt` | Wrapped civilian commitment, project elapsed time, and recovery-watch cursor comparisons in `check_variable`; removed invalid ROOT qualification from temporary prune cursor array indices; removed two terminal local target clears; implemented missing phase pacing helper. |
| `common/scripted_effects/035_great_depression_decision_effects.txt` | Removed terminal unsupported clear of a local source-country event target, overwritten before every consumer. |
| `common/scripted_triggers/029_riches_found_triggers.txt` | Replaced unsupported divisions_in_state.size constant token with documented file-local literal-zero macro. |

## Helper map and cleanup proof

`great_depression_set_pulse_interval`: country scope; input `great_depression_phase`; output regular country variable `great_depression_pulse_interval`; no gameplay effect except setting the existing due-check interval.
The sole call site is `great_depression_weekly_pulse` immediately before elapsed-day comparison.
It reads existing `great_depression_pacing` intervals: panic 4, depression 7, stabilization 12, recovery 8, paralysis 4 days.
The existing `great_depression_event.pulse_days` value of 7 initializes the output before recognized phase overrides.
No tuning constants were added or changed.
The source header documents purpose, scope, input, output, and initialization.

`acid_rain_resolve_action_target_state`: country scope; reads frozen global state registry and saved country `acid_rain_action_target_state`; outputs country scope variable `acid_rain_selected_action_state` only upon an exact valid match.
It clears that variable before lookup, so a failed lookup cannot reuse a previous transaction's state.
All consumers in the same preparedness file now use `has_variable` and `var:` rather than event-target existence and scope syntax.
The write occurs in selected state scope through `ROOT`, matching existing transaction root assumptions.
The release helper clears the scope variable after unlocking the matching state.
All identifier references were searched across common, events, and localisation; there are no external consumers of this particular pointer.
The original persistent state-id source, validity gates, payment requirements, action flags, timing, and effect calls remain intact.

The eight acid-rain achievement event-target names are `acid_rain_033_achievement_registration_state`, `acid_rain_033_achievement_transfer_state`, `acid_rain_033_achievement_exposure_state`, `acid_rain_033_achievement_recovery_snapshot_state`, `acid_rain_033_achievement_severe_target_state`, `acid_rain_033_achievement_severe_pulse_state`, `acid_rain_033_achievement_protection_state`, and `acid_rain_033_achievement_evacuation_state`.
Each target's consumers are confined to its owning helper and follow its same-branch save; each repeated helper invocation saves its target again before consumption.
The severe-pulse/protection targets have no target consumer beyond their save/unsupported-clear pair.
Nested helpers use different target identifiers; none consumes the parent's identifier after the removed terminal clear.
No caller, delayed continuation, localisation consumer, or has_event_target predicate reads these exact target identifiers outside the helper.
The two depression freeze targets likewise have only same-iteration save and immediately following array insertion consumers.
`great_depression_supported_source_country` is saved unconditionally at the start of its source-country aid transaction, then consumed within that transaction's recipient array checks; no other exact identifier consumers exist.
Local event targets expire with their chain; no global event targets were introduced and no null helper was added.

## Validation and references

Required references consulted: AGENTS.md, events/subagents/debug-playtest/decisions-missions skills, core offline wiki pages, Doctrine and Technology modding pages, vanilla effect/trigger/script-constant documentation, and existing dynamic-effect source/documentation.
Vanilla `common/scripted_triggers/00_scripted_triggers.txt:63` uses `divisions_in_state = { state = PREV size > 0 }`.
Vanilla documentation and offline Data structures explicitly state local event targets expire with their chain and cannot be manually cleared.
The existing building-damage helper documents literal injection through meta_effect; all four migrated calls retain their exact type/amount pairing.
Meaningful source checks confirmed all four damage call sites, complete selected-state pointer consumer migration, unchanged incident weight declarations, and existing evacuation constant names.
These checks are not runtime evidence.

MCP event inspection and neighborhood rendering completed with PARTIAL status for roots 29, 31, 33, and 35 at revision `4bccb6ec7fe1a73728780d86d162cce29175781f0177cb5975beec17f22caa3d`.
The service deferred workspace-wide helper projections and lifecycle passes, so it does not prove cleanup correctness.
Compare using that revision failed with `EVENT_REVISION_NOT_CACHED`; artifact-backed comparison failed with `Transport closed`.
Artifact URIs and partial-validation statements are recorded in `script_later_mcp_evidence.json`.
Doctrine inspection (`tech_inspect`, trace, new_fleet_in_being) timed out awaiting tools/call after 180 seconds.
No source-only claim substitutes for that missing engine evidence.

## Pending work and blockers

- 027 AI-path owner-readiness helper typos, bare AI result comparisons, and invalid cruiser/convoy naval-unit predicates await parent probability baseline before repair.
- 031 random-list macro key parse failures await parent probability baseline; no weights have been altered.
- 035 imported-resource amount constant tokens, invalid faction-member scope in exposure calculation, incident initializer effects mistakenly inside a trigger limit, and incident random-selector target cleanup await probability baseline.
- Root owns missing script constants and synchronized tokens.
- Root owns fresh startup validation; this subagent has not launched the game.
- No gameplay simplification was introduced; the overall assigned loader-error repair remains incomplete while the above work is pending.

027 follow-up reference: vanilla triggers_documentation.md:4453 uses `has_navy_size = { size > 10 type = convoy }`; the convoy predicate must use `type`, while cruiser coverage requires both installed `light_cruiser` and `heavy_cruiser` subunits.
The global motorized/engineers/encryption_1/radar database errors do not identify source paths and no exact has_tech use of those identifiers exists in the assigned 027 files.

## Final released repairs and freeze

The parent released exact syntax-equivalent repairs based on probability baseline `probability-e11c0526b49e287ed803f328` for 031 and recorded adapter limits for 027/035.
No balance redesign was authorized or performed.

- 027: repaired the missing `ai_` qualifier on navy/air owner-readiness calls, wrapped four bare result-variable comparisons in `check_variable`, expanded invalid generic cruiser predicates to the existing light/heavy cruiser subunits, and used the documented `type = convoy` predicate.
- 031: all five affected random lists receive dedicated temporary weight variables seeded immediately before every draw from existing incident constants and the parent-added runtime constant category.
The list keys use those unscoped temporary variable names, as documented for native random_list.
The 40 exact tokens are in `script_later_weight_tokens.txt`; none is an absence sentinel, every consuming pool initializes every key immediately beforehand, and no calls intervene between initialization and the draw.
The legacy @ declarations remain as reference values; they no longer occupy random-list key positions.
- 035: imported-resource predicates use a file-local literal-4 macro matching the existing threshold because this field rejected constant tokens.
The invalid faction-member scope becomes `any_other_country` with `is_in_faction_with = PREV` and the original active-crisis flag.
Incident history/clock/pressure initializer effects execute inside the active-crisis branch before the unchanged due-time test and pool selection.
- 035 incident pointer cleanup: the three state/partner/center pointers are regular country scope variables with real clear_variable operations at the same reset/cleanup boundaries.
Each selected state/country writes its pointer back through PREV; nested partner identity comparisons explicitly read PREV's pointer.
Same-country consumers use has_variable and var: scope lookup.
All exact consumers were confined to the incident effect file and two center-status helper lines in the main 035 effects file.
Random candidate filters, tickets, order, valid-result numeric contracts, fallback order, and outcome effects are preserved.

The final diff and hash inventory cover ten changed source files.
`script_later_final_validation.json` contains baseline byte paths, before/after SHA256 values, named 031 scenarios, and exact before/after ticket arrays.
Static comparison resolved every legacy macro and every new constant binding and verified identical ordered weights in all five affected pools: totals 158, 100, 100, 100, and 100.
The incident pool's first and last weights remain 16 and 2.
This is source equivalence evidence; mandatory MCP probability comparison remains with the root auditor.

Parent compare contract: scenarios `RT_INCIDENT_POOL_READY` and `RT_INCIDENT_POOL_READY_REPEAT`, scenarioHash `d4cd3ab1315015265274df348df57260d5ad89b90f95ade6362e9bd58c82fd1b`, baseline candidate positions `common/scripted_effects/031_random_terror_effects.txt:406.entry.1` through `.24`.
Source insertions moved the pool, so after-candidate mapping must use the same ordered 24 options at the current line rather than stale line numbers.
Baseline JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5b20483a2257fd2fb738e541f2f96f40fe78056593e7cd3c8c2d492b68166734/b78220db590cd8c12ab746aaeeadc8eece94b57956beef5043f98c97cbb071c6/probability-e11c0526b49e287ed803f328.json

Freeze chronology: 027 and 035 semantic repairs were written at 10:06:53 local; 031 temporary-weight repair was written at 10:07:58, before cycle 02 launched at 10:08:04.
An indentation-only rewrite of `035_great_depression_incident_effects.txt` completed at 10:08:44 before the freeze message was received.
That write did not change its 10:06:53 semantics, but it overlapped the parent's load and must be retained as a validation limitation.
No source mutation followed receipt of the freeze instruction.
No assigned source edits remain pending; fresh startup results and MCP comparisons remain parent-owned.
No gameplay simplification was made.
