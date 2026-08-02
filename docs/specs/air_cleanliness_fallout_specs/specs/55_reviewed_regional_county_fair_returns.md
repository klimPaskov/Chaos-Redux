# Spec 55: The County Fair Returns

Status: accepted implementation tranche for the dormant Fallout scheduler.

This ordinary North American regional chain is a seven-block institution story about recovered rural districts turning food, repair work, local security, and public memory into a seasonal gathering.

The chain is not a super-event, decision category, mission, focus route, bilateral partner, country creation, recurring on-action, scripted GUI, achievement, formable, or map rewrite.

## Ownership

The chain uses the dedicated `chaosx.fallout` namespace and the remapped ownership row below.

| Surface | Assigned value |
| --- | --- |
| Candidate and opening token | `572` |
| Hidden AI opening | `573` |
| Human result | `574` |
| Hidden AI result | `575` |
| Human callback | `576` |
| Hidden AI callback | `577` |
| Cleanup | `578` |
| Transaction key | `710054` |
| Route | `7154` |
| Event Log history | `9159` |
| Catalogue identity | `FALLOUT-572` |
| Report asset | `fallout_county_fair_returns` |

The previous County Fair proposal used the River Ration League ownership row. That proposal was rescanned and remapped before implementation.

## Admission and host selection

The row remains dormant until the Fallout scheduler activation gates are deliberately opened by a later reviewed tranche.

The country must have a current Fallout identity, durable resource row, current generation, North American region, a campaign day from 1095 through 5999, and no completed, pending, committed, or closed County Fair memory.

Food must be at least 24, Cohesion at least 30, Recognition at least 12, and at least one branch must be affordable.

At least three eligible native owned and controlled rural states are required for admission.

Each state must have a current-generation Fallout row, a produced Air Winter snapshot, surviving population, Food reserve at least 18, Supply Access at least 20, adaptation at least 15, reclamation at least 15, exposure below 65, and disease below 55.

The state selector counts eligible states and chooses the lowest native state id as the single host.

Only the host state is frozen and reserved. The transaction never invents partner state ids or expands into a multi-state write.

The host state must have no unresolved hazard, evacuation, village relocation, Ashline, frost, orchard, or other exclusive transaction receipt, and it must not have County Fair host memory.

## Four authored branches

The opening offers Civic Exhibition, Seasonal Exchange, Militia Muster, and Memorial Gathering.

Each option exposes its branch cost, the 35-day result delay, the host-state recheck, and the local risk.

Civic Exhibition spends Food 6, Scrap 4, and Recognition 2, then grades Cohesion, Recognition, civic trust, repair readiness, exposure, and disease.

Seasonal Exchange spends Food 8, Fuel 4, Scrap 2, and Recognition 1, then grades Food reserve, Supply Access, trade trust, route reliability, exposure, and disease.

Militia Muster spends Fuel 6, Equipment 3, and Recognition 1, then grades state supply, arms discipline, militia alignment, civic trust, exposure, and disease.

Memorial Gathering spends Food 5, Medicine 5, and Recognition 2, then grades Cohesion, family trust, public health, cause memory, exposure, and disease.

Unaffordable branches are unavailable to a human and receive zero hidden-AI weight.

Human and hidden AI lanes call the same branch cost, snapshot, grading, delayed result, callback, and cleanup effects.

## Frozen inputs, result, and callback

The opening freezes Food, Fuel, Scrap, Medicine, Recognition, Cohesion, War Support, Army Experience, Command Power, the host owner and controller, current generation, state Food, Supply Access, adaptation, reclamation, exposure, disease, and the branch ledgers used by the selected route.

The result is scheduled exactly 35 days after a valid branch choice.

The result deterministically resolves to success, partial success, or failure through named threshold constants and no random list or MTTH grading.

Success, partial success, and failure apply branch-aware resource, Cohesion, state supply, reclamation, exposure, disease, ledger, stability, War Support, dynamic modifier, building, and local Deaths effects.

Any civilian loss uses `apply_exact_state_civilian_population_loss`, the Fallout aftermath cause, and the minimum remaining population contract.

The callback is scheduled exactly 365 days after result settlement.

The callback reauthenticates country, generation, host state, owner, controller, branch, result, and callback token before applying a durable annual institution, partial tradition, or interrupted memory.

The callback has deterministic success, partial, and failure outcomes with branch-aware ledgers and local consequences.

## Event Log and asset contract

The opening records a branch choice, the result records branch and outcome, and the callback records its outcome.

Each history entry uses history `9159`, the country as primary actor, and the authenticated host state as secondary actor.

The dedicated report card is `GFX_report_event_fallout_county_fair_returns` and resolves to `gfx/event_pictures/fallout/report_event_fallout_county_fair_returns.dds`.

The asset has a source image, processed PNG, prompt, hashes, manifest, and handoff. Earlier package variants remain non-selected evidence and are not runtime consumers.

## Engine-sensitive proof boundary

The candidate producer is a dormant registry row and does not set `fallout_event_scheduler_activation_approved` or `fallout_event_scheduler_active`.

The normal-map and Air Winter route is proven through native state variables and current generation receipts, while live event dispatch, probability parity, and delayed queue execution remain user-owned runtime checks because this task does not launch HOI4.

The implementation must fail closed when the issued receipt, generation, owner, controller, state target, branch, or cleanup ticket no longer matches the registry.

## Future depth

Later tranches may add character memories, successor-specific focus hooks, diplomacy, or a reviewed annual institution event, but this tranche ends at the first callback and owns no recurring scheduler.
