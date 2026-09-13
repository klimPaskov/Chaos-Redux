# Camp startup parser repair

Status: implemented source repair, pending parent startup retest.
Authority: parent delegated existing camp helper parse repairs under the user's explicit unlimited startup debug-playtest authorization.
No commit was made.

## Root causes and repair

Cycle 01 reports invalid GROUP, PROGRAM, CATEGORY, BONUS, CAUSE, KIND and ORIGIN effects and cascading unexpected braces at ordinary scripted-effect argument blocks.
Ordinary HOI4 scripted effects use `helper = yes`, while these helpers relied on unsupported dollar-parameter substitution.
The installed vanilla scripted-effect source search found no matching dollar-parameter precedent, and the offline Effects page documents plain scripted-effect calls separately from `meta_effect` interpolation.
Six predicates also used the nonexistent `political_power` trigger instead of installed `has_political_power`.
The repair preserves the exact comparator and threshold in all six.

## Files changed

- `common/scripted_effects/camp_administration_country_census_effects.txt`
- `common/scripted_effects/camp_administration_country_effects.txt`
- `common/scripted_effects/camp_administration_effects.txt`
- `common/scripted_effects/camp_administration_integration_effects.txt`
- `common/scripted_effects/camp_administration_occupation_effects.txt`
- `common/scripted_effects/camp_repression_rework_effects.txt`
- `common/scripted_triggers/camp_administration_country_triggers.txt`
- `common/scripted_triggers/camp_administration_ui_triggers.txt`
- Paired `camp_administration_effects.md`, `camp_administration_country_effects.md`, `camp_administration_integration_effects.md` and `camp_administration_occupation_effects.md` contracts.

Pre-edit byte copies are under `baseline/camp/common/` in this run folder.
The manifest `camp_parameter_contract.json` records exact helper identifiers, argument mappings, input call sites and script before/after hashes.
`repair_camp_parameters.py` is a one-time mechanical migration artifact and refuses to overwrite existing backups.
`validate_camp_parameters.py` is the independent expanded-body comparison and can be rerun without changing gameplay.

## Helper map and contracts

| Family | Scope and inputs | Outputs, side effects and callers |
| --- | --- | --- |
| `camp_admin_initialize_cause_records_<cause>` | Current country or state, explicit custody/labor/violence/institutional suffix | Same guarded month/cumulative variable initialization, called by `camp_admin_initialize_records` |
| `camp_admin_record_cause_<cause>` | Current country or state, actual measured receipt remains the existing input | Same cause-ledger increments, called by existing cause dispatcher |
| `camp_admin_country_apportion_census_<group>` | Country, unchanged ceiling/stock/lifetime temps and active site registry | Same denominator, current stock, finite remaining allowance and state admission dispatch |
| `camp_admin_country_admit_census_host_<group>` | State with responsible country in PREV, unchanged shared census inputs | Same physical headroom, finite membership, admission proof and accepted receipt increments |
| `camp_admin_country_award_program_<program>` | Country, same institutional state and award contract | Exact per-program completion flag, category, bonus name/value, anti-stacking predicate, engineer release and slot cleanup |
| `camp_admin_country_start_program` | Country, required `camp_admin_start_program_input` temp | Copies exact program constant to persistent program state before original host selection, nine immediate callers |
| `camp_admin_integration_record_site_history` | State, required `camp_admin_history_kind_input` temp | Copies kind only after immutable attribution proof and writes existing history, six immediate lifecycle/evidence callers |
| `camp_occ_seed_origin` | Origin country, required `camp_occ_origin_ceiling_input_k` temp | Copies exact origin constant inside original once-only guard, then unchanged source denominator and residual accounting, 21 immediate callers |

Census suffixes are `ger_camps`, `ger_labor`, `sov_camps`, `jap_industry`, `jap_pingfang` and `jap_railway`.
Award suffixes are the nine original program tokens listed individually in the contract manifest.
Every explicit variant is a full literal expansion of the corresponding original body, including the nested apportion-to-admit call.
The common/events caller inventory found no external decision, GUI, on-action or event call requiring a patch.
All ordinary calls use `= yes` after migration.

## Constants, targets and cleanup

No constant, tuning value, AI weight, selection order, balance target, event target, cohort field or array operation was added or changed.
Numeric inputs have no defaults and are written immediately before every call.
Their only consumer is the owning helper's initial copy, with the existing kind and origin guards retained.
No absence or sentinel consumer exists for these new temporary names, and no scoped aliases or delayed calls are introduced.
There were no `clear_temp_variable` or `clear_event_target` occurrences in owned camp script files, so no cleanup substitution or deletion was performed.

## Validation and limits

`camp_parameter_validation.json` proves exact body equality for all 29 explicit variants against the backed-up original with its intended literal substitutions and nested call conversion.
It also checks all 36 numeric caller contracts.
This caught a draft migration defect that substituted the numeric PROGRAM input into award identity tokens, which was corrected before handoff.
The final award bodies preserve every original per-program flag and bonus identity.
Admission, finite stock/lifetime ceilings, cause attribution, cohort bookkeeping and physical-death calls remain inside those exact expanded bodies.
This is source contract evidence and does not prove engine execution or scenario balance.

Read-only MCP `hoi4.event_inspect` scan returned `EVENT_INSPECTED_PARTIAL` for the foundation surface.
Its evidence artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2699fdada6126c7e5c0afe81409de532da9a6532935c2357ffaaf504fbf80022/8b9ac03b3208d08414c1730d39688adcae8ab6104a545e937267840c116b77f4/event-scan-4bccb6ec7fe1.json`.
The scan deferred workspace-wide helper projections and lifecycle passes and did not validate them.
The post-change request `mode=state_flow`, `selector={kind:file,sourcePath:common/scripted_effects/camp_administration_integration_effects.txt}`, `expandHelpers=true`, `maxDepth=2`, `maxNodes=30`, `maxEdges=40` returned `INTERNAL_ERROR`, message `Unexpected internal error`, and no artifacts.
That route failure is an explicit evidence blocker, not equivalent source validation.
Parent owns subsequent startup launches, fresh log acceptance and linked GUI inspection for the four existing affordability predicates.

## Simplifications, omissions and blockers

No gameplay simplification, missing-input default, blank helper, balance change or content suppression was introduced.
Source repair is complete within the assigned parser surface.
Fresh engine startup acceptance and the failed MCP state-flow evidence remain pending.
No game process or desktop was controlled by this worker.

Skills used: chaos-redux-events, chaos-redux-subagents, chaos-redux-debug-playtest and chaos-redux-state-ledgers.
No skill was created or changed.

## Post-stop baseline addendum

The parent supplied `logs/cycle_01/error_after_stop.log` after the source handoff.
Its old country-effects line 110 refers to the original unresolved `$CATEGORY$` token.
The repaired variants use `industry`, `support_tech` and `engineers_tech`, verified in installed `common/technology_tags/00_technology.txt` at lines 22, 76 and 78.
The existing `has_tech_bonus = { category = <category> }` form matches installed trigger documentation and `common/technologies/NSB_armor.txt` line 663.
No additional category or bonus change was made.

Two further cleanup parser errors were repaired in `common/scripted_effects/camp_repression_colonial_country_effects.txt`, helpers `camp_rework_colonial_expand_current_state` and `camp_rework_colonial_apply_minor_project_to_current_state`.
Both scalar removal statements are now `remove_dynamic_modifier = { modifier = genocide_forced_labor_exploitation_state }`, matching installed effects documentation and existing camp-rework removal calls.
The exact modifier exists in `common/dynamic_modifiers/genocide_crisis_dynamic_modifiers.txt`.
The containing state scope, absence of an optional modifier scope, cleanup order and following effect bodies are unchanged.
The pre-edit file is backed up under `baseline/camp/`, and `camp_modifier_removal_validation.json` proves byte equivalence apart from the two required field wrappers.
Total touched gameplay files is nine.
Fresh startup acceptance remains parent-owned and pending.
