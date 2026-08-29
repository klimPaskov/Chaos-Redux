# Undefined Helper Repair Handoff

Date: 2026-08-26

Owner: `/root/undefined_helper_repair_0826`

Status: implementation edits are complete for the bounded undefined-helper repair. No Git commit was created. The shared worktree contains concurrent untracked famine and migration files, so these edits must be reviewed in place rather than cherry-picked or reset.

## Scope and ownership boundaries

This pass repaired stale effect and trigger calls for the famine and migration split. Famine remains the owner of food reserves and famine relief. Migration remains the owner of displacement pressure, active-state/country registries, and movement request intake. Humanitarian validation and corridor helpers remain neutral shared APIs. `common/scripted_effects/migration_decision_owner_effects.txt` was not touched because it remains parent-owned.

The organized-evacuation block in `common/decisions/famine_decisions.txt` was deliberately left unchanged by this pass because the parent requested that exact concurrently edited block remain untouched. A concurrent owner edit subsequently changed its call to the canonical `humanitarian_corridor_execute_evacuation`; that change was observed during final review and was not authored by this pass.

## Canonical mapping applied

| Stale token | Canonical owner/helper | Call-site treatment |
| --- | --- | --- |
| `famine_state_is_valid` | `humanitarian_state_is_valid` in `common/scripted_triggers/humanitarian_validation_triggers.txt` | Replaced in famine relief/opposition consumers. |
| `famine_country_is_valid` | `humanitarian_country_is_valid` in `common/scripted_triggers/humanitarian_validation_triggers.txt` | Replaced in famine opposition consumers. |
| `migration_state_is_valid` | `humanitarian_state_is_valid` | Replaced in migration spontaneous/forced movement and destination-selection consumers. |
| `migration_country_is_valid` | `humanitarian_country_is_valid` | Replaced in migration cohort-history, presentation, destination-selection, and capacity consumers. |
| `migration_register_active_displacement_country` | `migration_register_active_country` in `common/scripted_effects/migration_core_effects.txt` | Replaced in reception-capacity registration/dirty callbacks. |
| `migration_register_active_displacement_state` | `migration_register_active_state` in `common/scripted_effects/migration_core_effects.txt` | Replaced in the spontaneous movement request adapter. |
| `migration_unregister_active_displacement_state` | `migration_unregister_active_state` in `common/scripted_effects/migration_core_effects.txt` | Replaced in spontaneous movement cleanup branches. |
| `migration_apply_movement_request` | `migration_apply_flight_request` in `common/scripted_effects/migration_core_effects.txt` | The spontaneous movement adapter now maps its proof, amount, source, and actor-proof envelope into the canonical pressure request fields, calls the flight endpoint, and preserves the result in its existing adapter result variable. |
| `famine_refresh_food_reserve_capacity` | `famine_refresh_reserve_capacity` in `common/scripted_effects/famine_core_effects.txt` | Replaced in famine relief effects and documentation. |
| `famine_update_food_reserve` | `famine_update_reserve` in `common/scripted_effects/famine_core_effects.txt` | Replaced in famine relief effects. |
| `famine_transfer_food_reserves` | `famine_transfer_reserves` in `common/scripted_effects/famine_core_effects.txt` | Replaced in famine relief effects and documentation. The existing narrow alias `famine_requisition_reserves` remains the requisition call used by the decision. |
| `famine_select_safe_food_reserve_donor` | `famine_relief_select_donor` in `common/scripted_effects/famine_relief_effects.txt` | The safer-state decision now seeds the canonical land route and reserve-requisition request amount, invokes the selector, and consumes `event_target:famine_relief_selected_donor_state` only when `famine_relief_selection_result` is valid. |
| `humanitarian_prepare_corridor_contract` | `humanitarian_corridor_prepare_contract` in `common/scripted_effects/humanitarian_corridor_effects.txt` | Replaced in the migration corridor negotiation decision. |
| `humanitarian_submit_corridor_offer` | `humanitarian_corridor_submit_offer` in `common/scripted_effects/humanitarian_corridor_effects.txt` | Replaced in the migration corridor negotiation decision. |
| `humanitarian_execute_corridor_evacuation` | `humanitarian_corridor_execute_evacuation` in `common/scripted_effects/humanitarian_corridor_effects.txt` | Replaced in both migration evacuation decisions. The separate famine organized-evacuation call is now also canonical in the shared worktree through a concurrent owner edit; this pass did not edit that block. |

No compatibility alias was added for the stale names. All runtime identifiers introduced or retained by this pass stay within the `famine_*`, `migration_*`, or neutral humanitarian/civilian-transfer namespaces. No `famine_migration_*` or `fm_*` runtime token was introduced.

## Donor decision adaptation

`common/decisions/famine_decisions.txt` now initializes the destination as before, assigns `famine_relief_route_mode = constant:famine_relief_route_mode.land`, derives `famine_relief_requested_amount` from the destination daily need multiplied by `constant:famine_mission_contract.reserve_requisition_days`, rounds it, and calls `famine_relief_select_donor`. The transfer branch requires both a valid `famine_relief_selection_result` and `has_event_target = famine_relief_selected_donor_state`, then runs the existing reserve requisition and outcome handling against that canonical target.

The canonical selector is a weighted sparse-pool helper. It refreshes recipient reserve capacity, validates the relief recipient and actor, checks the seeded route/request inputs, iterates `global.famine_relief_registered_donor_states`, and persists the selected donor state/country plus the selection result. No fabricated donor, generic country fallback, or migration pool was added.

There is a semantic review risk that must remain visible to the parent: the canonical relief selector's relation gate requires a donor owner different from the requesting `ROOT`, while the existing safer-state decision availability and target gates describe a same-country controlled neighboring reserve donor. The parent explicitly directed this canonical selector mapping, so this pass did not alter the decision's targeting design or invent a same-country fallback. If the intended requisition semantics are same-country transfer, the parent must decide whether to realign the decision target predicates or provide an explicitly owned famine selector; the current repair is a compile/call-contract repair, not a redesign of that donor policy.

## Helper contract notes

| Helper family | Scope and inputs | Outputs and side effects |
| --- | --- | --- |
| `humanitarian_state_is_valid` / `humanitarian_country_is_valid` | State or country scope; no arguments. | Read-only boolean validation; no variables, flags, registries, or targets written. |
| `migration_register_active_state` / `migration_register_active_country` and unregister counterparts | Exact state or country scope; registry state is already initialized by the caller. | Idempotently updates migration active registries and lifecycle flags through the migration core owner. |
| `migration_apply_flight_request` | State scope with temporary `migration_pressure_request_proven`, amount, source, and actor-proof inputs. | Applies the canonical migration flight pressure transaction, registers active state/country, and returns temporary `migration_pressure_request_result`. The spontaneous adapter copies that result to its legacy adapter result variable for its existing caller contract. |
| `famine_refresh_reserve_capacity` / `famine_update_reserve` / `famine_transfer_reserves` | Famine state scope; transfer additionally receives the existing temporary request/proof envelope and destination target. | Famine-owned reserve capacity/update/transfer ledgers and measured transfer result; no migration registry or population mutation is introduced by this repair. |
| `famine_relief_select_donor` | Recipient state scope; `ROOT` is the relief actor, and the owner supplies route mode plus requested amount. | Two-pass weighted sparse-pool selection, regular `famine_relief_selected_donor_state` and country targets on success, persisted donor state/country/actor/result variables, and no reserve movement. |
| `humanitarian_corridor_prepare_contract` / `humanitarian_corridor_submit_offer` / `humanitarian_corridor_execute_evacuation` | Existing corridor state/actor scopes and request variables. | Existing neutral corridor contract, offer, and evacuation transaction outputs; no helper alias or additional corridor target was added. |

## Constants, tuning, and persistence plan

No script constants or probability weights were added or retuned. The requisition adapter uses existing `famine_relief_route_mode.land`, `famine_mission_contract.reserve_requisition_days`, `famine_relief_result.valid`, and the existing reserve-transfer minimum-grant constants. The weighted donor formula remains centralized in the existing famine relief constants and candidate-weight helper.

The only new persistence use in the requisition caller is the canonical selector's existing regular event target `famine_relief_selected_donor_state`; it is consumed inside the same effect chain. The selector's recipient-local donor state/country/result variables remain the existing famine relief contract fields. No global target, recurring scan, migration registry, or cleanup hook was added. The existing transfer destination target remains chain-local, and existing corridor target cleanup remains corridor-owner logic.

The migration adapter deliberately maps only the exact flight lane selected by its caller. It does not infer food movement, civilian transfer, or a generic migration request, and it leaves the existing caller-owned source reset in place after the canonical endpoint returns.

## Changed files

The following files received narrow call-site or documentation edits in this pass. Their final content includes concurrent work already present in the shared worktree; hashes below are integrity references for review, not patch identifiers.

### Script and decision files

- `common/decisions/famine_decisions.txt`
- `common/decisions/migration_decisions.txt`
- `common/scripted_effects/famine_relief_effects.txt`
- `common/scripted_effects/migration_capacity_effects.txt`
- `common/scripted_effects/migration_cohort_history_effects.txt`
- `common/scripted_effects/migration_destination_selection_effects.txt`
- `common/scripted_effects/migration_presentation_effects.txt`
- `common/scripted_effects/migration_spontaneous_movement_effects.txt`
- `common/scripted_triggers/famine_opposition_triggers.txt`
- `common/scripted_triggers/famine_relief_triggers.txt`
- `common/scripted_triggers/migration_destination_selection_triggers.txt`
- `common/scripted_triggers/migration_forced_movement_triggers.txt`
- `common/scripted_triggers/migration_spontaneous_movement_triggers.txt`

### Documentation files

- `common/scripted_effects/famine_opposition_effects.md`
- `common/scripted_effects/famine_relief_effects.md`
- `docs/plans/famine_and_migration_system_plans/source_of_truth_map.md`

The handoff itself is `docs/plans/famine_and_migration_system_plans/subagent_handoffs/undefined_helper_repair_0826.md`.

## Validation and evidence

The stale-token source census over `.txt`, `.yml`, `.gui`, `.gfx`, and `.asset` runtime files found zero stale effect/trigger calls. The only remaining token hit is the legacy definition `famine_select_safe_food_reserve_donor` at `common/scripted_effects/famine_decision_owner_effects.txt:14`; it has no live callers and was not modified because it is concurrent owner content. All other reported stale tokens have zero source hits.

The canonical definition census found the expected owners: humanitarian validation triggers, migration core active registration and flight request effects, famine core reserve effects, famine relief donor selection, and the three humanitarian corridor effects.

A targeted Clausewitz brace scan over the 13 touched script/decision files returned `BRACE_CHECK_OK`. The repaired source scan found no forbidden `famine_migration_*` or `fm_*` runtime tokens.

The required weighted analysis began with `hoi4_probability_inspect` for `common/scripted_effects/famine_relief_effects.txt` and candidate pool `famine_relief_donor_candidate_weight`. The read-only result was successful source discovery with `poolComplete=false`, zero discoverable candidates, zero available candidates, and one unresolved input. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9d6a18ec6295ca412592e1da5dab5065fb5632656ea8ad4829500b97f0bb3266/2baa1575e1fb5f5af5e8e2f27009bdf7bf36194c14e192cf6698c00433a103e1/probability-inspect-5a25ba4a424f.json`.

No probability constants or weight formulas changed in this pass, so no probability comparison was run. The required `chaosx_ai_probability_auditor` evidence route was not callable in this session; the available tool registry exposed the read-only HOI4 probability tools but no auditor subagent/tool route. Parent-owned same-scenario probability evidence remains an open gate if the selector or its targeting is changed.

The offline Paradox wiki core pages and relevant vanilla documentation were read before editing, including data structures, triggers, effects, scopes, decisions, and script constants. No game process was launched.

## Unresolved blockers and follow-up

1. The canonical famine relief donor selector is foreign-relief oriented, while the safer-state decision's existing availability predicates describe same-country neighboring reserves. Parent review must resolve that policy alignment without adding a fallback or crossing famine/migration ownership.
2. The legacy `famine_select_safe_food_reserve_donor` definition remains in the concurrently authored `famine_decision_owner_effects.txt` with no callers. Parent should decide whether to remove or retain that dead owner helper after reviewing the canonical relief mapping; this pass did not overwrite it.
3. The probability artifact reports an incomplete custom-pool manifest with one unresolved input and no candidates. This is an analysis limitation, not a source fallback.
4. No in-game runtime validation was performed; live consumer validation remains parent/user-owned.

## SHA-256 integrity references

Hashes are generated after the final implementation and documentation edits. They describe the complete files currently visible in the shared worktree and therefore include any concurrent content in those files.

| File | SHA-256 |
| --- | --- |
| `common/decisions/famine_decisions.txt` | `125d6cda1f68ac1926c121852166b28f2c2b40fd76c4d58dd82816c4496cb076` |
| `common/decisions/migration_decisions.txt` | `bd748779a4eb8a0037215a58be3f92597973f22be9e668a35efdc3cef9a3a6a6` |
| `common/scripted_effects/famine_relief_effects.txt` | `edb8313ee76953a2c20694e8c79c8469d1c2de0fc404f49bcff3ba9a8619858b` |
| `common/scripted_effects/migration_capacity_effects.txt` | `a501e128857916e0c2153bad23fa3a66fb09cfee15ef03f2000eb1cf072b0798` |
| `common/scripted_effects/migration_cohort_history_effects.txt` | `e236e828b21fbf4d4211883e03b4c2d37246b09e0e787dc22e343b060b7c0439` |
| `common/scripted_effects/migration_destination_selection_effects.txt` | `739fb5ba55aa4cba58ad963303c823225c77e0d76283a8cae2d09f7ddc56feb4` |
| `common/scripted_effects/migration_presentation_effects.txt` | `7dbda21cac8663fc61ea938fff753c9425137d6709840ba9a50b19a9e0dd69ec` |
| `common/scripted_effects/migration_spontaneous_movement_effects.txt` | `3d26111149dea53fc669a696b385626059ba3a2ad427e9c5e836039d24f828fb` |
| `common/scripted_triggers/famine_opposition_triggers.txt` | `10981fb0d6b76ade06e40f83f11bda8e4310ff82f3f8fbeb105c563c96aab84a` |
| `common/scripted_triggers/famine_relief_triggers.txt` | `928570d6eacd7a10f76402df434e01db262aefee03a5a15ec2393cbc2962a77f` |
| `common/scripted_triggers/migration_destination_selection_triggers.txt` | `3ac1ee6c8450c86c2031bfe73e269bdda98158392ed37a4302711aed7d6df033` |
| `common/scripted_triggers/migration_forced_movement_triggers.txt` | `300f531f1718057f9acd3eb0e2bc4c3dcc858291d7a4f7d6efe43de132109f3c` |
| `common/scripted_triggers/migration_spontaneous_movement_triggers.txt` | `c6dcc6debf54a4bdd8968c271181770e34b78e6909d2421857fe158f3d4d9430` |
| `common/scripted_effects/famine_opposition_effects.md` | `fb861aa307029975a74acb493e2c292a4c82b45d32dd4448be2120cc837535b9` |
| `common/scripted_effects/famine_relief_effects.md` | `79ad7087c7b71e7667feee0eeaa6c4e7d01cc322aa8c387d93a0b6c907b4e855` |
| `docs/plans/famine_and_migration_system_plans/source_of_truth_map.md` | `57e5d90f0e9d0a55948e7749ceed77b112f821f1830598af0ad5cdbb94bc0fcf` |
