# Spec 62: The Canal Schedule

Status: accepted implementation tranche for the dormant Fallout scheduler.

The Canal Schedule is a South Asian regional water-governance chain for one agricultural state whose surviving communities must agree how to release a finite clean-water reserve through the first recovery season.

The chain is Fallout-owned and uses `chaosx.fallout` only. It is not a super-event, decision category, mission, focus route, bilateral partner, country creation, recurring on-action, scripted GUI, achievement, formable, or map rewrite.

## Ownership

| Surface | Assigned value |
| --- | --- |
| Candidate and human opening | `628` |
| Hidden AI opening | `629` |
| Human result | `630` |
| Hidden AI result | `631` |
| Human seasonal callback | `632` |
| Hidden AI seasonal callback | `633` |
| Cleanup | `634` |
| Transaction key | `710061` |
| Route | `7161` |
| Event Log history | `9167` |
| Catalogue identity | `FALLOUT-628` |
| Report asset | `fallout_canal_schedule` |

The row remains dormant while both Fallout scheduler activation flags are unset.

## Admission and target selection

The country must have a current Fallout identity, durable country resources, a current generation, the South Asia regional row, a campaign day from `730` through `5999`, sufficient Food, Clean Water, Cohesion, and Recognition, and at least one affordable branch.

The target is the lowest eligible native owned and controlled South Asian rural or pastoral state with a produced Air Winter snapshot, surviving population, Food reserve, Supply Access, Adaptation, Reclamation, infrastructure, Exposure, and Disease Pressure inside the reviewed thresholds.

HOI4 exposes no generic canal topology building. The chain therefore records a transaction-scoped canal schedule memory from regional agricultural and water evidence. A specific historic canal name requires an additional country-memory receipt and is not asserted by this tranche.

Only the selected state is frozen and reserved. The chain does not invent a partner state or perform a multi-state write.

## Four authored branches

The human opening offers Joint Schedule, Upstream Priority, Gate Guard, and Local Water Councils.

Joint Schedule spends Clean Water, Food, and Recognition to raise allocation trust and country Cohesion while improving Supply Access and Reclamation.

Upstream Priority spends Power, Fuel, and Recognition to protect immediate field delivery while increasing downstream grievance and reducing the shared schedule ledger.

Gate Guard spends Fuel, Command Power, and support equipment to secure the release point while increasing military control and costing Cohesion.

Local Water Councils spend Food, Medicine, and Recognition to strengthen local authority and reduce Disease Pressure while lowering central compliance.

Unaffordable branches are hidden from human choice and receive no hidden AI selection. Human tooltips disclose each branch cost, local risk, and 42-day result timing.

## Frozen inputs and deterministic result

The opening freezes the country resource row, Cohesion, War Support, Recognition, generation, owner, controller, target state identity, state Food, Supply Access, Adaptation, Reclamation, Exposure, Disease Pressure, population, and infrastructure values consumed by the grade.

The branch cost is paid once after the exact ordinary receipt, current target, and branch affordability checks pass. It is refunded when the delayed-result transaction is rejected before commitment.

The result is scheduled exactly 42 days after a valid choice. The grade uses frozen values and the selected ledger, with branch thresholds of 60 and 40 for Joint Schedule, 63 and 43 for Upstream Priority, 64 and 44 for Gate Guard, and 58 and 38 for Local Water Councils.

Success, partial success, and failure update country Food, Clean Water, Power, Fuel, Medicine, Recognition, Cohesion, Stability, War Support, and the target state's Supply Access, Food reserve, Reclamation, Exposure, Disease Pressure, and infrastructure where failure requires native damage.

Failure routes bounded civilian loss through `apply_exact_state_civilian_population_loss` with the Fallout aftermath cause and the minimum remaining population contract.

Durable ledgers track allocation trust, upstream priority, downstream grievance, gate maintenance, local-council authority, military control, and illicit-water pressure. All ledgers are clamped and scoped to the owning country.

## Seasonal callback and cleanup

The callback is scheduled exactly 240 days after result settlement. It represents the next seasonal release review and cannot recalculate the already-settled result.

The callback uses the frozen baseline and current target-state Supply Access, Food, Reclamation, Exposure, and Disease Pressure. It applies a second bounded survival pass and a bounded Deaths request on callback failure.

Continuity and Food Compact governments prefer Joint Schedule. Warlord Command favors Gate Guard during war. Technates and Machine Protocol governments favor Joint Schedule or Upstream Priority according to Power and gate maintenance. Nomad Convoys and Religious Refuges favor Local Water Councils. Quarantine governments favor Joint Schedule or Local Water Councils when Medicine is available and Disease Pressure is high. Ties use the fixed branch order.

Result, callback, and cleanup reauthenticate the country generation, candidate identity, transaction, route, target state, branch, event token, and delayed ticket.

If ownership, control, or generation becomes stale, the exact transaction is cancelled, history `9167` records the cancellation, payment is refunded only when commitment did not occur, and the state reservation and transient variables are cleared without touching a replacement transaction.

Successful completion preserves durable Canal Schedule ledgers and the state memory while cleanup releases the result and callback rows exactly once.

## Event Log and asset contract

The opening, result, callback, and cancellation write explicit choice and outcome payloads to Event Log history `9167` with the country as primary actor and the authenticated target state as secondary actor.

Dedicated scripted localisation resolves branch, result, callback, and cancellation payloads. The report card uses `GFX_report_event_fallout_canal_schedule` and `gfx/event_pictures/fallout/report_event_fallout_canal_schedule.dds` at `210x176`.

## Engine-sensitive proof boundary

Static checks must prove unique event ids, balanced script blocks, constant references, branch affordability revalidation, callback outcome locking, cancellation Event Log routing, localisation coverage, Event Log routing, and the `210x176` DDS contract.

The candidate producer remains dormant and does not set `fallout_event_scheduler_activation_approved` or `fallout_event_scheduler_active`.

Live scheduler dispatch, delayed queue delivery, invalid-target runtime behavior, Event Log rendering, save recovery, multiplayer delivery, and host authority remain unobserved because HOI4 is not launched by this task.

## Future depth

Later tranches may consume Canal Schedule memory in Bengal Delta successor diplomacy, migration, food compacts, and South Asian focus overlays. This tranche owns no recurring scheduler or global daily sweep.
