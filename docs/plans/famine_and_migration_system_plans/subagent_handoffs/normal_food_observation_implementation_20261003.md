# Normal food observation implementation

Date: 2026-10-03.
Status: implemented in source, with numeric probability comparison and native execution evidence unresolved.
Acceptance basis: parent acceptance of a famine-owned on-demand assessment using the established neutral loss-pressure model baseline, without granting physical stock, services or route guarantees.
The parent explicitly authorized immutable source preservation and helper/refactor work before baseline, then released publication, retirement and consumer integration after the probability auditor completed its source-backed baseline and narrower inspection attempts.
Those two baseline inspections returned actual 600-second timeouts without artifacts, so release does not constitute numeric probability certification.
The parent also accepted a non-reveal pending enqueue after the auditor identified query activation as an interaction risk.

## Current changed files and ownership

- `common/scripted_effects/famine_core_effects.txt`: shared component, existing-stock relief, score/requested-stage and non-advancing blockade calculations, evaluator assessment recording, non-reveal enqueue through the existing sparse registry/processor, and control/retirement proof cleanup.
- `common/scripted_effects/famine_core_effects.md`: new paired calculation-helper contracts and usage.
- `common/scripted_effects/famine_adapter_effects.txt`: observer, assessment provenance, fail-closed publication gate and invalidation.
- `common/scripted_effects/famine_adapter_effects.md`: observer inputs, outputs, defaults, side effects and usage.
- `common/scripted_triggers/famine_core_triggers.txt`: pending stable-stage retirement guard using only the current score and existing supply-strain threshold.
- `common/scripted_effects/migration_adapter_effects.txt`: the food-consumer helper and its attached comment only.
- `common/scripted_effects/migration_adapter_effects.md`: its food-consumer table row only.
- Immutable before sources under `validation_baselines/normal_food_observation_20261003/`.
- This handoff.

The observer is wired through the existing migration food consumer after baseline release.
Existing origin/adjacent and capacity-candidate prepasses already invoke that consumer, so `migration_destination_selection_effects.txt` requires no separate edit and remains byte-identical to baseline.
No numeric weight, destination target predicate, CXT grant, category, event ID, GUI, asset, route or population effect changed.
Concurrent Event 012 reception helpers remain untouched.
The migration-adapter baseline comparison shows the owned food-consumer hunk plus the parent's separate removal of two custody actor-ID equality checks.
Those parent-owned removals were preserved because the Camp proof token is an approved action identifier rather than actor ID.

## Public and internal helper contracts

| Helper | Scope and inputs | Outputs/defaults | Side effects |
| --- | --- | --- | --- |
| `famine_observe_migration_food_context` | Exact valid civilian state with positive native population. Present pressure/input/profile fields must lie within their existing bounds. A present stage must be an actual existing stage enum. Declared surface/profile contexts require complete owner inputs. A known positive stage requires its durable model, stock, exposure and clock fields. | Temporary `famine_food_observation_result`, default zero. Missing ordinary model values use existing neutral initializer defaults only after validation. Current score/components and assessment flags are famine-owned. | Collects current supported context and shared calculations. Preserves existing inputs, pressure, stock, committed stage, exposure and timers. Newly material stable-stage assessment enqueues only this exact state without active/category flags and invalidates destination proof. Does not create stock, services, routes, mortality, flight or player presentation. |
| `famine_record_food_assessment` | State after shared current component/score calculation. | `famine_food_assessment_current` boolean flag. `famine_food_observation_pending_material` records stable committed stage plus score at/above the existing supply-strain threshold. | Provenance only. Does not commit stages or advance time. |
| `famine_rebuild_food_components` | Initialized state input/profile/pressure fields and current collector outputs, plus optional proven reception-demand amount. | Eight existing bounded normal component fields. | Rebuilds components without simulation-clock or stock mutation. |
| `famine_apply_existing_reserve_relief` | Existing stock, daily need and transient reserve relief. | Existing component relief plus temporary `famine_food_reserve_score_relief_output`. Non-positive daily need contributes no stock-days relief. | Reads stock only. Ordinary simulation updates stock before this call. Observation never does. |
| `famine_calculate_food_score` | Current eight components and unchanged constants. | Normal `famine_food_security_score`, temporary raw score and requested stage. | Calculation only. Committed stage and hysteresis remain separate. |
| `famine_apply_current_blockade_components` | Current full blockade proof and existing exposure. | Current bounded transport/need contribution. | Does not advance or reset blockade exposure. |
| `famine_apply_blockade_components` | Registered simulation state. | Existing one-day exposure advance or reset, same attribution and pressure calculation. | Retains the simulation clock while delegating its arithmetic to the non-advancing helper. |
| `famine_register_state_in_runtime` | Exact valid state. | Existing sparse array membership/count and registry result. | Common insertion only, with no state/category activation. |
| `famine_enqueue_food_observation_assessment` | Exact valid state with material assessment. | `famine_food_observation_pending_job` when simulation is not active, plus existing registry membership. | No query-caused active/phase/report/incident flags. Existing processor consumes the job and activates ordinary evaluation at its normal boundary. |

The evaluator and observer predeclare new shared temporary output fields before calling the relevant scripted effect.
That preserves their lifetime across the parent chain.
Both callers also predeclare the eight current collector outputs, and the collector predeclares its five occupation-resolver outputs before that child call.
These zero/none declarations are overwritten by the unchanged collector/resolver and add no formula term or resource effect.
Callers of the observer must similarly predeclare `famine_food_observation_result` before checking its return.

## Immutable pre-edit sources

Copies were created before any owner source edit and verified byte-equal with their original source SHA-256.
No baseline was overwritten.

| Source and copy filename | SHA-256 |
| --- | --- |
| `famine_core_effects.txt` | 9E57983FF15737321F4F31B2471F3BEA4B438432EF8F521E4DA0C87906F42B1F |
| `famine_core_triggers.txt` | 9ABA0F437AEA85B1F371E9257FF20C22291AD3E88EEF575805719403E53EE6E9 |
| `famine_adapter_effects.txt` | 05E5855A19BE1B4999BD52F61E8D2208C288005E0A2B7F0F26B5D698E9C460F1 |
| `migration_adapter_effects.txt` | 679856D9FDDECF00A780DBB8BEA2954927607EDFD5F60FE278752F8AF9A65AF4 |
| `migration_destination_selection_effects.txt` | F20084BF1FE1B12A885710B0A3E081E251F3AEFD3505ACA4C65925421CAEB9FF |
| `migration_destination_selection_triggers.txt` | 3C4AAC5707EC80279477005E22980723CC5846ABA200228395A16C117B06141D |
| `migration_core_triggers.txt` | 00031F2DBCC7549E0D1FD2EBD40613809EB97332D9CD4B8EC68F8266BC7864FE |
| `migration_decisions.txt` | 279487DC7F2FCEF921F7294FD207BA8C1C33F871C652280EBB31D2D1FD2A3E8B |
| `migration_capacity_effects.txt` | 62CE76598B5EE2FCD7517613370C52A8899B23347DF289872C44B31DB1AE607B |

Source locations retain their corresponding `common/scripted_effects`, `common/scripted_triggers` or `common/decisions` directory.
Copy filenames live directly under the baseline directory.
The migration-adapter copy deliberately preserves the full mixed-file state, including other owners' current work, for comparison provenance.
It is evidence, not authorization to alter those other blocks.

## Source evidence completed

The extracted component, existing-reserve relief and score bodies match the immutable source bodies exactly.
No numeric weight, threshold, duration or formula term changed.
The pre-integration evaluator expands to the same 1,443 baseline script tokens after inlining shared calculations and removing caller output declarations.
Final evaluator changes beyond that refactor are assessment recording and the accepted pending-job/retirement lifecycle.

Seven source-parsed shared-score cases preserve:

| Case | Positive component level | Relief | Score | Requested stage |
| --- | --- | --- | --- | --- |
| zero | 0 | 0 | 0 | stable |
| below strain | 24.9 | 0 | 24.9 | stable |
| strain boundary | 25 | 0 | 25 | supply strain |
| acute boundary | 50 | 0 | 50 | acute shortage |
| famine boundary | 75 | 0 | 75 | famine |
| catastrophic boundary | 100 | 0 | 100 | catastrophic famine |
| relief floor | 0 | 100 | 0 | stable |

All seven positive components use the indicated same level in this threshold matrix.
The interpreter uses the actual current source and parsed source constants.
This is source arithmetic evidence, not observed engine fixed-point behavior.

Eleven parsed observer validation-prefix cases accept normal missing defaults, complete known crisis fields and retired retained neutral inputs.
They reject fractional stage, negative pressure, production above 100, negative stock, negative exposure, a known crisis missing durable fields, a declared profile missing its fields and a declared surface missing its fields.
The known-crisis fixture carries stage 3, exposure 20, stock 12345 and explicit start/next-mortality dates, which validation leaves unchanged.

The independent completion audit identified a missing-stage gap when current crisis flags or modifiers existed without the numeric stage.
The observer now treats active positive stage flags and current severity modifiers as known-current-crisis markers, requires their valid matching numeric stage and complete durable model, and rejects before initialization can repair that state.
It preserves quiet retired historical flags as historical evidence rather than automatically declaring a current crisis.
Nine additional parsed final-source validation cases cover this correction without changing any normal variable during validation:

| Case | Result |
| --- | --- |
| Active famine flag, missing numeric stage | Reject. |
| Active catastrophic flag, missing numeric stage | Reject. |
| Current famine modifier, missing numeric stage | Reject. |
| Current catastrophic modifier, missing numeric stage | Reject. |
| Quiet retired famine/catastrophic historical flags, no active/current modifier | Allow fresh observation. |
| Current catastrophic modifier with numeric supply-strain stage | Reject inconsistent state. |
| Active famine flag with numeric stable stage | Reject inconsistent state. |
| Complete active famine stage/model with matching flags and modifier | Accept assessment, retaining unsafe committed stage. |
| Active pending stable state without positive severity markers | Allow ordinary pending assessment. |

Direct observer call review excludes reserve update/refresh, pressure decay, stage transition, mortality, survivor-flight and retirement entry points.
The shared current blockade helper contains no exposure mutation.
Only its ordinary simulation wrapper advances or resets exposure.
The observer's initializer writes missing defaults, including zero stock, and preserves existing fields.

## Completed integration and source cases

After the parent probability baseline release, the following source integration was applied:

1. Required real current assessment in `famine_publish_migration_food_safety`, with pending-material stable-stage assessment rejected.
2. Recorded assessment after ordinary stage/mortality logic and before publication, clearing pending-material when a stage is recognized or current score recovers.
3. Cleared current, pending-material and pending-job flags during cleanup, and invalidated assessment on control change and through the public invalidator.
4. Guarded stable-stage retirement against a current score at/above the existing supply-strain threshold, preserving the ordinary candidate timer.
5. Wired only `migration_consume_famine_food_safety` to observe before publishing, with caller-side temporary declarations and accepted-result gating.
6. Preserved existing adjacent prepasses, which already call that consumer on origin and neighboring states.
No separate weighted-loop rewrite or target predicate relaxation is required.
7. Added a non-reveal exact-state enqueue to the existing sparse state registry/processor.
Mandatory same-scenario probability comparison remains parent/auditor-owned and must retain actual results or its route blocker.

Seven source-parsed retirement cases prove missing-score stable, below-threshold stable and recovered score-zero states may retire when other obligations are clear.
Stable-stage scores at 25 or 75 cannot retire before ordinary stage timing.
Recognized supply strain and positive reception demand remain non-retirable.
The pending enqueue/common insertion source writes no simulation-active, country category/phase, report or incident field.
The existing registered-state processor consumes `famine_food_observation_pending_job` before ordinary activation/evaluation.

| Exact case | Source behavior and limits |
| --- | --- |
| Normal untracked healthy state | Validate positive native population and normal civilian scope, initialize only missing neutral model defaults, collect current supported context and compute score. Safe stable assessment may publish. Stock remains zero absent a real prior amount. No simulation registration or category flag is created. |
| Healthy internal adjacent state | Existing origin/neighbor prepass invokes the observer through the consumer. Food receipt can become valid, but unchanged owner capacity, infrastructure, native hazard, exact history, controller and route requirements remain necessary. This is not a route or service grant. |
| Healthy foreign adjacent state | Same food observation, with unchanged foreign owner, control, admission policy, capacity, hazard, route and history gates. Dormant host first-service activation remains unresolved. No free foreign housing/medical baseline was added. |
| Newly material stage-zero state | Score at/above existing supply-strain threshold keeps receipt invalid, marks pending material and queues one exact pending job. Query leaves active/category/report/incident flags unset. Ordinary processing consumes the job, establishes simulation at its boundary and preserves candidate timing until stage recognition or safe recovery. |
| Known crisis | Complete stored inputs, stock, committed stage, exposure and timers are preserved. A valid assessment of stage 3 remains unsafe for destination gates rather than being reset stable. |
| Malformed or incomplete state | Out-of-range/fractional stage, negative pressure/stock/exposure, oversized component or incomplete declared context rejects before neutral defaults can manufacture a healthy receipt. Current/projection proof is invalidated. |
| Repeated same-date query | Component reconstruction starts from owner input/profile/collector facts rather than accumulating past components. Registry insertion is idempotent. No reserve update, pressure decay, exposure increment, candidate/recovery advancement, mortality or flight pulse is called. |
| Queries stop after first material observation | Pending job remains in the existing registry. Ordinary simulation, rather than further queries, progresses candidate timing. If current score becomes safe and remaining obligations clear, cleanup removes registration and all pending/current assessment flags. |
| Control change/retirement | Current proof is invalidated on control change. Retirement clears assessment/job/material flags and projected facts. Later bounded observation must establish fresh facts. |
| Missing services or aggregate CXT request only | Food observation grants neither shelter/medical receipts nor aggregate capacity. Existing capacity validation still fails without actual registered service evidence. |

Ordinary `migration_open_reception` triggers remain read-only.
Candidate assessment before that trigger requires a parent-selected bounded preparation/request lifecycle.
Dormant foreign-host first-service activation remains separately unresolved and cannot be claimed closed by food observation.

## Tools and validation limits

The required reference-context and source-lookup calls in the architecture audit returned actual 600-second timeouts.
Exact local spans, hashes, current source reachability and installed/offline reference reading are recorded in `normal_destination_bootstrap_audit_20261003.md`.

Live `mechanic_test` validation confirms flat numeric entries under `scenario.state` are accepted.
The rejected form was a nested `state.variables` object.
Equals assertions require `id`, `path = { key = ... }` and `expected`, and reject `key`/`value` directly on the assertion.
This corrects the overly broad earlier phrase about a typed scope-record map.
A schema-valid `food_observation_shared_score_zero_20261003` fixture was submitted after those validation findings and returned `timed out awaiting tools/call after 600s` from `hoi4.mechanic_test`.
No effect execution, artifact or native outcome is inferred from that timeout.

## Final owned source identities

| File | SHA-256 |
| --- | --- |
| `famine_core_effects.txt` | 095974659833AC0C8A6D6BC0B40BCE34A545754976C83B78CFE1007D97A1025D |
| `famine_core_triggers.txt` | 3BE7168A1E1E2CB54E76A1AE6969870113AF5E53FF7DEDC0F2CE0F011EDB44A9 |
| `famine_adapter_effects.txt` | 09BF27C2F784BBDCBD1883DFA7192B796EF8E18CAD3D622820C131B18145FEA0 |
| `migration_adapter_effects.txt` | 37AAD37C1B3AA4A31CC24DD6CC0C789B9C0648FF7070ACB473C62E890C4D7C7A |
| `migration_destination_selection_effects.txt`, unchanged | F20084BF1FE1B12A885710B0A3E081E251F3AEFD3505ACA4C65925421CAEB9FF |

The source correction is implemented and documented.
Same-scenario probability comparison, native helper/selector execution and dynamic map consumer evidence remain unresolved.
The separate foreign-host service/request design remains a genuine parent-owned design gap.
No simulation, tuning, route or resource simplification was introduced.

No `script_validate` route was exposed.
No game was launched and no logs were read.
No world scan, event target, new meter or free service was added.
Skills used are the event, decision/mission, state-ledger and subagent skills already recorded in the architecture audit.
No skill was modified and no commit was made.
