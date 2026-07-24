# Event 016 KRG hazardous mission-pressure implementation plan

Status: accepted by the parent on 2026-07-24 and implemented locally by the KRG decision/mission subagent; not staged or committed.

## Scope

This bounded tranche deepens exactly four existing hazardous missions without creating a new category, currency, GUI, focus, event chain, asset, or shared-system dependency.

- `brilliant_scientist_krg_clone_drift_review_mission`
- `brilliant_scientist_krg_rogue_node_containment_mission`
- `brilliant_scientist_krg_maintenance_audit_mission`
- `brilliant_scientist_krg_transit_breach_closure_mission`

Ministry consolidation and ministry replacement remain passive administrative commitments by parent disposition.

## Implementation contract

Each mission receives one objective decision visible only while that exact mission is active and its objective receipt is absent.

Each objective uses an existing material-cost helper plus its matching 1/2/4/6 factory-capacity trigger and a timed factory burden.

Each objective writes one cycle-local receipt and a permanent history receipt only when its own timed work completes.

Mission timeout grants the existing full result only when the objective receipt and its operational evidence are still valid.

Missing objective work or lost operational evidence grants no full receipt, preserves the sunk start/objective costs, writes a distinct permanent failure history receipt, applies a meaningful contained consequence, and sets a bounded retry cooldown.

Cancellation under the ordinary KRG/world-end lifecycle clears transient mission/objective flags without creating a success or failure reward.

## Mission objectives

| Hazardous mission | Objective decision | Operational proof at timeout | Full result | Partial/failure consequence |
| --- | --- | --- | --- | --- |
| Clone drift review | Quarantine and sequence the active clone lineage | Clone route remains operational and the controlled growth site remains held | Existing repaired-registry receipt and stability gain | Drift remains unresolved, stability loss, failure history, and cooldown before another review |
| Rogue-node containment | Isolate the operational machine power node | Machine route remains operational and the controlled power node remains held | Existing rogue-node-contained receipt and stability gain | Network remains exposed, stability loss, failure history, and cooldown before another containment attempt |
| Maintenance audit | Service the controlled primary facility | The saved primary facility still exists, belongs to KRG, is controlled, and is not destroyed | Existing maintenance receipt and force-package rebuild | Deferred maintenance receipt, stability loss, failure history, and cooldown before another audit |
| Transit-breach closure | Seal the operational controlled transit terminal | Portal route remains operational and the controlled terminal remains held | Existing transit-breach-closed receipt and stability gain | Breach remains open, stability loss, failure history, and cooldown before another closure |

## AI and anti-farming contract

AI may start each objective only while its matching mission is active and the same material/factory proof is true.

Objective decisions are one-per-mission-cycle through their objective-completed receipt, and the objective receipt is cleared when a new mission cycle begins.

Full success receipts remain one-time as before.

Failure history is permanent while the retry cooldown is timed and does not erase the history receipt.

## Files and validation

Permitted implementation surfaces are the three existing decision files, Event 016 KRG constants/triggers/effects when required, English KRG decision localisation, the KRG decision-system documentation, this plan, and the existing KRG audit handoff.

Validation must prove objective visibility, active-mission gating, matching capacity/material gates, AI blocks, one-cycle receipt clearing, full-success versus partial/failure branches, retry cooldowns, ordinary cancellation cleanup, localisation coverage, and unchanged ministry missions.

The implementation satisfies this contract and must not be treated as a second general Event 016 improvement-loop addendum.
