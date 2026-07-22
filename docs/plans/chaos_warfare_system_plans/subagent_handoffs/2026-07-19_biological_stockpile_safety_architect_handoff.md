# Biological stockpile safety helper tranche

Date: 2026-07-19
Owner: `chaosx_scripted_system_architect`
Status: reusable private helper tranche complete; caller wiring remains intentionally queued.

This handoff covers only the four files in the exclusive write scope. It does not claim that the biological accident/capture/doomsday system is fully wired.

## Changed files

- `common/script_constants/biological_stockpile_safety_constants.txt`
- `common/scripted_triggers/biological_stockpile_safety_triggers.txt`
- `common/scripted_effects/biological_stockpile_safety_effects.txt`
- `docs/plans/chaos_warfare_system_plans/subagent_handoffs/2026-07-19_biological_stockpile_safety_architect_handoff.md`

No existing file was edited. No decision, raid, operation, event, on-action, localisation, project, lifecycle helper, shared registry, or dirty concurrent file was changed. No files were staged, committed, reverted, or deleted.

## Helper map and caller contracts

All helpers are country-scoped unless noted. They are private to the biological stockpile-safety subsystem and do not substitute for a native raid or operation.

| Helper | Inputs | Outputs | Side effects and caller contract |
| --- | --- | --- | --- |
| `bio_stockpile_safety_capture_agent_stockpiles` | Country scope; no inferred state | `bio_stockpile_safety_anthrax_stockpile`, `...plague_stockpile`, `...tularemia_stockpile`, `...smallpox_stockpile`, raw total, danger-weighted total, supplied proof | Reads the live `num_equipment@` values for the four payload models. Call in country scope; do not use as a world pulse. |
| `bio_stockpile_safety_prepare_agent_weights` | Country scope | Four `bio_stockpile_safety_*_weight` variables and supplied proof | Weights are the unmodified actual four stockpile counts. `bio_stockpile_safety_agent_weights_are_selectable` additionally requires a positive total before `random_list` use. |
| `bio_stockpile_safety_arsenal_pointer_is_valid` | Country variable `bio_stockpile_safety_arsenal_state`, `bio_stockpile_safety_arsenal_pointer_source`, and persistent flag `bio_stockpile_safety_arsenal_designated` | Boolean validity | Dereferences only the one supplied state. It requires the state to exist, be owned and controlled by the caller, be an eligible ordinary-pathogen state, and contain an actual `biowarfare_facility`. The source must be `selected_state` or `verified_special_project_facility`. |
| `bio_stockpile_safety_capture_exact_arsenal_condition` | Country scope with a valid exact pointer | Exact facility level, damaged level, non-damaged level, infrastructure level, war-damage indicator, recent-bombing indicator, supplied proof | Enters only `var:bio_stockpile_safety_arsenal_state`; uses state dynamic building values and `days_since_last_strategic_bombing`. Sets transient state flag `bio_stockpile_safety_condition_snapshot_active`. |
| `bio_stockpile_safety_capture_handling_state` | Valid exact pointer; optional caller-owned exact-state flags `bio_stockpile_safety_explicit_sabotage_active` and `bio_stockpile_safety_recent_handling_active` | Exact-context status, sabotage value, recent-handling value | Current native sabotage is accepted only when `bio_sabotage_operation_in_progress` and `bio_sabotage_active_state` match the exact arsenal. A recent native sabotage record is accepted only when its exact `bio_last_sabotage_state` matches and its `bio_last_sabotage_start_date` is within the constant window. |
| `bio_stockpile_safety_refresh_risk_band` | Valid exact pointer, actual stockpile snapshot, `cbrn_biological_security`, exact facility/war/handling snapshots | Visible 0–100 risk score, effective safety, tech tier, component values, and `controlled`/`strained`/`dangerous`/`critical` band | Combines actual stockpile, existing Biosecurity, the three existing safety technologies, exact facility condition, exact-state war damage/recent bombing, explicit sabotage, and recent handling. It never alters lifecycle evidence, attribution, deaths, contamination history, medical saturation, Condemnation, use history, or stockpile. |
| `bio_stockpile_safety_prepare_incident_severity_inputs` | `bio_stockpile_safety_incident_kind = ordinary_accident`, valid refreshed context | Five positive selection weights: contained, lab contamination, local outbreak, major domestic outbreak, international exposure | Produces only `random_list` inputs. It does not choose a lifecycle route or dispatch an incident. |
| `bio_stockpile_safety_select_incident_severity` | Same as severity-input helper | `bio_stockpile_safety_selected_incident_severity` | Uses the prepared weights and selects only the private severity enum. The caller must map that result to the existing lifecycle route/source/result contract. |
| `bio_stockpile_safety_prepare_stock_loss_amount` | Valid exact pointer, selected existing lifecycle agent enum, positive `bio_stockpile_safety_requested_loss`, actual snapshot | Selected live stockpile, positive bounded loss, negative removal amount, supplied proof | Rounds the request, enforces minimum one, caps at the selected agent's actual equipment, and prepares but does not debit equipment. Native raid/operation/lifecycle accounting remains authoritative. |
| `bio_stockpile_safety_highest_safety_ordinary_accident_immunity` | Ordinary-accident incident kind, valid exact/condition/handling context, `fail_safe_containment_facilities` | Boolean; `yes` means an ordinary accident may be rejected | This trigger is deliberately false for sabotage, bombing, capture release, and doomsday input kinds. It also fails closed for exact explicit sabotage or recent bombing. Callers must classify the incident before invoking it. |
| `bio_stockpile_safety_cleanup_runtime_context` | Country scope; pointer retained until cleanup | None | Clears all private runtime country variables, the transient exact-state snapshot flag, and the two private runtime input flags. It intentionally retains the persistent exact arsenal pointer/source/designation so a caller can reuse a verified designation. |

The existing lifecycle enums are reused exactly: `bio_lifecycle_agent.*`, `bio_lifecycle_math.*`, `bio_lifecycle_proof.*`, and the existing lifecycle route/source/result enums. No lifecycle pipeline was copied.

## Constants and tuning table

`bio_stockpile_safety_constants.txt` centralizes all new tuning:

- `bio_stockpile_safety_band`: `none`, `controlled`, `strained`, `dangerous`, `critical`.
- `bio_stockpile_safety_pointer_source`: `selected_state`, `verified_special_project_facility`.
- `bio_stockpile_safety_incident_kind`: `ordinary_accident`, `sabotage`, `bombing`, `capture_release`, `doomsday_release`.
- `bio_stockpile_safety_incident_severity`: `contained`, `lab_contamination`, `local_outbreak`, `major_domestic_outbreak`, `international_exposure`.
- `bio_stockpile_safety_agent_risk`: Anthrax `1.00`, Plague `1.25`, Tularemia `0.75`, Smallpox `1.50`; these affect the visible risk total only.
- `bio_stockpile_safety_risk`: score bounds, band cutoffs, stockpile scale, facility damage/inoperability penalties, war damage, bombing, sabotage, recent handling, and the 30-day recent-state windows.
- `bio_stockpile_safety_loss.minimum`: `1`.
- `bio_stockpile_safety_incident_weight`: one five-outcome weight table for each risk band.

Existing shared values are referenced instead of duplicated:

- lifecycle agent IDs and math/proof values from `biological_lifecycle_constants.txt`;
- existing lifecycle safety-tech contributions from `bio_lifecycle_response.*`;
- the existing exact-state war-damage infrastructure threshold from `bio_lifecycle_environment.war_damage_infrastructure_threshold`.

Doctrine is intentionally absent. The helper does not reduce evidence, attribution, deaths/history, contamination/history, medical saturation/history, accident records, use records, public-harm floors, or stockpile debit.

## Exact pointer, event-target, and cleanup plan

The persistent arsenal designation is a normal country variable containing one exact state scope:

- `bio_stockpile_safety_arsenal_state`
- `bio_stockpile_safety_arsenal_pointer_source`
- `bio_stockpile_safety_arsenal_designated` (country flag)

The caller owns the act of writing these values. For a player-selected arsenal, it must write the exact selected state. For a special-project facility, it must write the exact `facility_state` while that special-project context exposes it and mark the source as `verified_special_project_facility`. The helper never scans for another state and never reconstructs a facility location from a completed project.

No new event target is created by this tranche. This is deliberate: regular event targets are chain-scoped, while a persistent national designation requires an explicitly cleaned normal country variable. Existing lifecycle/raid/operation event targets are not touched.

Runtime cleanup clears the country snapshot, risk, handling, incident, selection, and loss variables. It clears `bio_stockpile_safety_condition_snapshot_active`, `bio_stockpile_safety_explicit_sabotage_active`, and `bio_stockpile_safety_recent_handling_active` on the exact designated state. It does not clear the persistent designation or any existing lifecycle, raid, operation, sabotage, capture, history, or zombie flag.

## Migration plan

No call sites were changed because the user-locked write scope excludes all callers. The parent implementation should wire the helpers in this order:

1. Add an exact designation/safety-management caller that writes the one state pointer from a player selection or an active special-project `facility_state` proof. Do not replace this with `random_controlled_state`, an alternate-state search, or a completed-project estimator.
2. At an event-driven biological accident boundary, call the stockpile snapshot, exact condition snapshot, handling snapshot, and risk refresh in country scope. Reject only when the caller has explicitly set the incident kind to `ordinary_accident` and `bio_stockpile_safety_highest_safety_ordinary_accident_immunity` is true.
3. For ordinary accidents, call the severity helper and map its result to the existing lifecycle route/source/result records. Continue through `bio_lifecycle_dispatch_seed`; do not add a second lifecycle pipeline.
4. For sabotage, bombing, capture release, and doomsday release, set the corresponding incident kind and use their existing exact-native records. Never pass those kinds through the ordinary-accident immunity branch.
5. Use `bio_stockpile_safety_prepare_stock_loss_amount` only where a caller has an exact stock-loss contract. Apply the prepared amount through the existing native/lifecycle accounting path; this helper intentionally does not remove equipment itself.
6. Call cleanup after the one incident/selection transaction resolves, before rebinding the persistent arsenal pointer. Do not add a global daily, weekly, or monthly all-country pulse.

The legacy four MTTH accident blocks in `events/biowarfare_events.txt` remain untouched and are not silently considered migrated. Their later replacement must preserve accident records and exact stock debit while moving only the reusable snapshot/risk/selection logic to these helpers.

## Validation performed

- Read the required repository guidance, the offline Data Structures/Triggers/Effects/Modifiers/Localisation/Scopes/On actions/Event/Decision/Idea/AI pages, relevant equipment/state/technology pages, and the installed HOI4 documentation for script constants, dynamic variables, effects, triggers, scopes, event targets, stockpile arithmetic, `random_list`, and special-project facility state.
- Confirmed the four payload IDs against the current special-project/biological source surface and repo-wide references: `anthrax_bomb_1`, `plague_bomb_1`, `tularemia_bomb_1`, `smallpox_bomb_1`.
- Confirmed the referenced technologies exist: `pathogen_handling_protocols`, `sealed_containment_laboratories`, `fail_safe_containment_facilities`.
- Confirmed the referenced lifecycle constants and `bio_lifecycle_state_is_eligible_ordinary_pathogen_target` helper exist in the current lifecycle files.
- Confirmed the existing exact sabotage records and state variables used by the handling helper: `bio_sabotage_operation_in_progress`, `bio_sabotage_active_state`, `bio_last_sabotage_start_date`, and `bio_last_sabotage_state`.
- Checked the current-version vanilla dynamic-equipment precedent in `common/decisions/NOR.txt` and the installed dynamic-variable documentation for `num_equipment@<equipment_id>`; checked the current-version `random_list` variable-weight precedent in `events/001_communism_spread.txt`.
- Checked the new files for unsupported `<=`/`>=` operators and unary-negative variable tokens; the negative loss output is created by multiplying with the existing `constant:bio_lifecycle_math.negation`.
- Read-only HOI4 MCP inspection was attempted for `events/biowarfare_events.txt` with artifact `event-scan-ae47532d7e1f.json` (`sha256 e261ce...`). The server returned `EVENT_INSPECTED_PARTIAL` with an oversized unresolved inventory, so it was used only as a read-only evidence reference and not treated as complete source linkage.

## Gaps, limitations, and follow-up

- There are no gameplay call sites in this tranche by design. Risk display, accident event routing, exact arsenal UI/decision wiring, and final lifecycle mapping remain parent work.
- The installed special-project documentation states that `facility_state` is available in the special-project facility context and that a facility may be absent when a project is completed by script. The normal `is_special_project_completed` trigger does not provide the completed facility state. Therefore no helper was added to discover that state after completion; doing so would be an unsupported fallback.
- The new 0–100 score cutoffs and incident weights are centralized initial tuning, not a completed balance pass. They need scenario review when the parent wires event-driven accident boundaries.
- No live game execution or runtime parser was available in this tranche. Static identifier and contract validation was performed; parent wiring should run the normal task-specific load/lint validation after adding callers.
- Weaponized zombies remain outside every new enum, trigger, effect, and cleanup path.
