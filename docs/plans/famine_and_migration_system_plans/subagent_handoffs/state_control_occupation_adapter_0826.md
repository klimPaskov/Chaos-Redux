# State-Control Occupation-Pressure Adapter Audit

Date: 2026-08-26.

Status: blocked; no gameplay source patch was made.

## Decision

The existing `on_state_control_changed` callback is not a causally sufficient producer for either `famine_request_occupation_pressure` or `migration_request_occupation_pressure`.

The callback exposes the exact changed state, the new controller, and the old controller, and `occupation_law` is readable in the state scope, but it does not expose whether the transfer was hostile, peaceful, or an allied liberation, nor does it provide an exact affected-people amount or an accepted occupation transaction receipt.

Submitting pressure from this callback would therefore require an ungrounded population fraction, guessed occupation-law timing, or ambiguous actor proof, all of which are prohibited by the current famine and migration contracts.

The existing behavior remains the correct fail-closed behavior: the hook invalidates corridor identity and dispatches famine and migration cleanup/reassessment only.

## Inspected artifacts

| Artifact | Evidence used |
| --- | --- |
| `common/on_actions/humanitarian_runtime_on_actions.txt:46-55` | The hook saves `FROM` as `migration_previous_controller`, then calls `humanitarian_corridor_handle_state_control_change` and `humanitarian_handle_state_control_change` from `FROM.FROM`. Its comment records `FROM.FROM` as the state, `ROOT` as the new controller, and `FROM` as the old controller, and explicitly says the transfer is not an attack receipt. |
| `common/scripted_effects/humanitarian_runtime_effects.txt:74-76` | The shared handler only calls `famine_handle_state_control_change` and `migration_handle_state_control_change`. |
| `common/scripted_effects/famine_core_effects.txt:446-475` | `famine_apply_pressure_request` requires the validated request envelope and converts an exact people amount into normalized food pressure using live state population. |
| `common/scripted_effects/famine_core_effects.txt:506` | `famine_request_occupation_pressure` only sets the occupation source and delegates to the existing famine owner. |
| `common/scripted_effects/famine_core_effects.txt:835-989` | `famine_resolve_occupation_profile` maps current occupation-law identifiers to profile and extra component magnitudes. It is a read-only normalized context resolver, not a people-denominated receipt. |
| `common/scripted_effects/famine_core_effects.txt:2816-2830` | The famine control-change handler unregisters relief, cleans mission subjects, marks reassessment, re-registers an already active state, refreshes modifiers, or cleans invalid registration. It does not submit pressure. |
| `common/scripted_effects/migration_core_effects.txt:734-777` | `migration_apply_flight_request` requires the validated request envelope and adds the exact people amount to migration flight pressure and state flight population. |
| `common/scripted_effects/migration_core_effects.txt:789` | `migration_request_occupation_pressure` only sets the occupation source and delegates to the existing migration owner. |
| `common/scripted_effects/migration_core_effects.txt:2146-2165` | The migration control-change handler performs mission cleanup, pending reassessment, active-state registration, reception-capacity dirtying, modifier refresh, presentation refresh, or invalid-state cleanup. It does not submit pressure. |
| `common/scripted_triggers/famine_core_triggers.txt:50-59` | Famine pressure validation requires a valid state, positive request proof, positive amount, source, and actor proof. |
| `common/scripted_triggers/migration_core_triggers.txt:17-26` | Migration pressure validation requires the same positive proof, amount, source, and actor envelope. |
| `common/script_constants/famine_core_constants.txt` | `famine_surface_context` values such as occupation extraction, vulnerability, and governance pressure are normalized component points, not affected civilian totals. `famine_food_shock.population_share_for_maximum = 0.20` is an existing conversion bound, not an occupation receipt. |
| `common/script_constants/humanitarian_runtime_constants.txt` | `humanitarian_population.people_per_k = 1000` and the minimum request constants define units and validation floors, not a transfer fraction. |
| `common/occupation_laws/chaosx_occupation_laws.txt:77-93` | The custom occupation laws set policy and state modifiers but do not provide a people-affected amount or control-transfer cause. |
| `common/scripted_effects/cbrn_occupation_effects.txt:77-97` | The current mod writes occupation laws through explicit policy effects, but those effects do not write a famine or migration people receipt. |
| `common/scripted_effects/famine_adapter_effects.md` | Generic occupation-law changes remain API-only until an owner supplies an exact state-local food receipt. |
| `common/scripted_effects/migration_adapter_effects.md` | No movement or flight request is fabricated at a state-control change; migration requires exact state, people, actor, and causal proof. |
| `docs/plans/famine_and_migration_system_plans/source_of_truth_map.md` | Occupation APIs are definition-only because generic law changes do not carry the required amount, actor, cause, generation, revision, and request identity. |
| `docs/plans/famine_and_migration_system_plans/completion_report.md` | The current completion audit records generic occupation-law changes as an exact source-data blocker and confirms both occupation wrappers remain definition-only. |
| `docs/specs/famine_and_migration_system_specs/famine_and_migration_system_spec_part_4_deaths_occupation_atrocity.md` | Occupation pressure is allowed only on scoped hooks with exact causal context; state control change does not itself become an attack receipt. |
| `docs/specs/famine_and_migration_system_specs/famine_and_migration_system_spec_part_7_cross_system_connections.md` | Occupation-law changes and liberation are separate causal surfaces; liberation lowers pressure only after explicit checks. |
| `docs/specs/famine_and_migration_system_specs/famine_and_migration_system_integration_matrix.csv` | The occupation-law integration row assigns policy ownership to occupation and requires audited law identifiers with scoped control/law hooks. |
| `docs/specs/famine_and_migration_system_specs/famine_and_migration_system_coding_prompt.md` | The adapter contract requires actual conditions, exact state-local amounts, and separate famine/migration ownership. |

## Engine and vanilla evidence

The offline `On actions - Hearts of Iron 4 Wiki.md` records `on_state_control_changed` as `ROOT` new controller, `FROM` old controller, and `FROM.FROM` state ID.

The vanilla `common/on_actions/00_on_actions.txt:5075-5076` carries the same scope comments.

The offline triggers documentation defines `occupation_law` for state and country scope and states that state scope checks the occupier's current law for the occupied state.

The vanilla effects documentation defines `set_occupation_law` for state and country scope, but does not document a control-change reason, hostile-transfer flag, or affected-civilian amount emitted by `on_state_control_changed`.

The required vanilla `documentation/on_actions_documentation.md` file is absent from the installed documentation directory; the on-action scope contract was therefore cross-checked against the offline wiki and vanilla `00_on_actions.txt` precedent.

This proves that current `occupation_law` can be read as a state-local policy fact when the callback runs, but it does not prove how the state was transferred, when a prior law changed, or how many civilians were affected by that transfer.

## Causal blocker

### Hostile-control proof is unavailable

`ROOT` is the current controller and `FROM` is the previous controller, but those roles do not prove that `ROOT` performed a hostile occupation action.

The same callback can follow a peaceful state transfer or an allied liberation, and no documented callback field distinguishes those outcomes from a hostile capture.

A same-controller guard could reject an equal-tag case if the engine ever delivered one, but it would not solve peaceful transfer or allied liberation and is not an action receipt.

The saved `event_target:migration_previous_controller` is the old-controller pointer used by migration reception-capacity dirtying and cannot be repurposed as responsible hostile actor proof.

### Exact affected-people amount is unavailable

Both public pressure owners require a positive people amount in their temporary request envelope.

The state population is the whole current state population and is not an occupation transaction total, an affected cohort, or a civilian loss receipt.

The existing `famine_surface_context` occupation values are normalized 0-100 component magnitudes used by famine context collection; passing one as a people amount would make the famine owner interpret a pressure point as people and would be especially wrong for migration, whose owner adds the amount to flight-population ledgers.

Multiplying `state_population_k` by any occupation-law fraction would fabricate the prohibited population fraction.

No current occupation-law effect writes a state-local affected-people amount, generation, revision, request identity, or accepted pressure receipt that this callback can consume.

### Timing and request identity are unavailable

The callback can read the current occupation law, but the inspected documentation does not define a historical previous law or a guaranteed ordering between a law assignment and a later controller change.

The callback supplies no replay-safe generation, revision, request identity, or owner transaction envelope.

Setting only the source to `occupation_policy` and using `ROOT` as actor would make the request pass only after inventing the missing amount and causal proof.

## Helper map

No new helper was created because no valid call site exists.

| Helper | Scope and contract | Status and call site |
| --- | --- | --- |
| `humanitarian_handle_state_control_change` | STATE scope; dispatches neutral corridor invalidation plus separate famine and migration lifecycle handlers; no pressure output; cleanup/reassessment side effects only. | Existing call from `common/on_actions/humanitarian_runtime_on_actions.txt:54`; retained unchanged. |
| `famine_request_occupation_pressure` | STATE scope; consumes the famine request envelope with positive people amount, proof, source, and actor proof; returns the famine request result and mutates only famine pressure/registration. | Existing public wrapper at `famine_core_effects.txt:506`; not called from the control hook. |
| `migration_request_occupation_pressure` | STATE scope; consumes the migration request envelope with positive people amount, proof, source, and actor proof; returns the migration request result and mutates only migration flight pressure/registration. | Existing public wrapper at `migration_core_effects.txt:789`; not called from the control hook. |
| `famine_try_submit_occupation_control_pressure` | Potential future STATE helper; would require an owner-written exact food receipt, hostile-action proof, current-controller actor proof, and replay identity before calling `famine_request_occupation_pressure`. | Deferred and intentionally not defined because the required receipt does not exist. |
| `migration_try_submit_occupation_control_pressure` | Potential future STATE helper; would require an owner-written exact flight-pressure people receipt, hostile-action proof, current-controller actor proof, and replay identity before calling `migration_request_occupation_pressure`. | Deferred and intentionally not defined because the required receipt does not exist. |

The famine and migration helper names remain separate; no combined namespace or shared pressure ledger is proposed.

## Constants and tuning plan

No constants were added or changed.

The existing occupation profile component constants remain the source-backed normalized policy magnitudes for context collection.

The existing `famine_food_shock.population_share_for_maximum` remains a famine pressure normalization bound and must not be reused as a generic occupation-control population fraction.

If a future owner supplies an exact affected-people receipt, the adapter should pass that amount directly through the existing owner request envelope and should not derive it from total state population.

No guessed law timing constant, hostility threshold, liberation discount, or transfer fraction is justified by the available source.

## Event-target and cleanup plan

No new event target was added.

The existing regular `migration_previous_controller` target remains available only for the current migration reception-capacity dirtying path after control change.

It must not be treated as hostile actor proof, a famine source, a migration source, or a durable global pointer.

No global target, pressure receipt target, population ledger, cohort target, or cleanup path is needed while the adapter is blocked.

If a future exact owner receipt is persisted across a short effect chain, it should use a regular event target and be consumed once; a global target would require explicit clear logic and is not justified here.

## Migration plan

No source migration was performed.

The existing hook and owner handlers remain the baseline.

When an occupation owner eventually provides a complete receipt, the parent should add two separate owner-local calls from the narrow state callback or from the exact law-change owner, with all of the following fail-closed checks before submission: exact state scope, valid current controller, different old and new controllers, explicit hostile-action proof, non-liberation or non-peaceful-transfer proof, positive exact people amount, actor proof tied to the responsible current controller, and replay identity.

Famine should call only `famine_request_occupation_pressure`; migration should call only `migration_request_occupation_pressure`.

Neither call may invoke population mutation, deaths, physical movement, cohort creation, reception mutation, or a recurring scan.

## Validation and unsupported analysis

The source census confirmed one humanitarian control-change hook, one neutral shared dispatcher, one famine occupation wrapper, one migration occupation wrapper, and no occupation-pressure call site elsewhere in `common`.

The `set_occupation_law` census found only the current CBRN occupation policy writers in `common/scripted_effects/cbrn_occupation_effects.txt`; those writers do not emit a famine or migration people receipt.

The handler inspection confirmed the current control-change paths perform cleanup/reassessment only and contain no pressure, death, population, movement, or cohort mutation.

The profile inspection confirmed that occupation values are normalized context components and that the resolver does not provide affected civilian totals.

No on-action, event, focus, GUI, or map surface is linked to this adapter beyond the generic on-action callback, so no event/focus/GUI/map MCP route was applicable.

No weighted or probability-bearing helper was added, so no probability inspection or probability auditor pass was applicable.

No whole-world recurring scan was added or modified.

No live Hearts of Iron IV run was performed, in accordance with repository policy that live consumer validation belongs to the user.

Unsupported by the inspected engine/documentation contract: hostile-versus-peaceful control-change reason, allied-liberation reason, same-controller guarantee, exact affected-people total, previous occupation-law snapshot, law-change ordering, and replay-safe transaction identity.

## Parent-owned follow-up

The parent should keep this handoff as the exact blocker record and leave the existing occupation request APIs definition-only until an occupation, battle, liberation, or policy owner can write a state-local receipt with exact people, responsible actor, causal operation, generation, revision, and request identity.

The parent should not resolve this blocker by deriving a fraction of `state_population_k`, treating profile points as people, treating `migration_previous_controller` as attacker proof, or assuming that every state-control callback is hostile occupation.

No simplification or fallback was used; no requested gameplay behavior was silently approximated.
