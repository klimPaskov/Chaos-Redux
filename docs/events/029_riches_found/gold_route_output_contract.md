# Gold Disease movement output storage

The five state-scoped callers of `riches_found_roll_gold_route` allocate `riches_found_gold_route_spreads` before invoking the roll.
The roll still resets that caller-owned temporary result to zero, then sets it to one only for its spread outcome.
The caller can therefore consume the returned result in the same effect chain without relying on a temporary first created inside a nested helper.
The variable remains temporary and introduces no persistent boolean, currency, actor, timer, scan or duplicated mine contribution.

| Caller | Existing movement route |
| --- | --- |
| `riches_found_move_gold_through_workforce` | Departing workers to another controlled registered mine or the capital |
| `riches_found_move_gold_through_rotation` | Rotated guards or soldiers into the controller's army |
| `riches_found_move_gold_through_smuggling` | Stolen material to one eligible neighboring controller |
| `riches_found_move_gold_through_sponsor` | Departing concession staff to the existing sponsor |
| `riches_found_spread_gold_to_controller` | Shared capital delivery for shipment and pay-transport routes |

The shared capital caller serves two distinct actions, preserving all six specified routes.
Recipient selection, report payloads, restrictions, duration, pressure changes and cleanup are unchanged.
Gold Disease remains a fictional compulsive crisis, with no biological outbreak or Event018 underground integration.

## Source and comparison evidence

Offline `Data structures - Hearts of Iron 4 Wiki.md:435-443`, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`, documents caller allocation across scripted-helper boundaries.
Installed effects documentation `set_temp_variable`, lines 7820-7841, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, provides the assignment syntax.
The scripted-effect comment preserves the original random-list line position, so both before and after candidates have stable `:30.entry.1` and `:30.entry.2` identities.
Before source SHA-256 is `d80093b036568a3da7606859d15f655942e119548505e309ea0c7dfb8f9f96c8`; corrected source SHA-256 is `0e31f8fdcdd3a1542ef2103625bf6d10ad13fa1f07446ee10d3476934f36a0da`.

The probability auditor inspected the two-entry pool, evaluated typed `RF_GOLD_02_AUTHORITARIAN_WARTIME`, attempted the restriction sweep and compared the exact same named scenario and two candidates against the frozen source.
The retained direct request and tool result are `docs/plans/029_riches_found_plans/evidence/2026_10_07_gold_caller_compare.json`.
Its replay returns `PROBABILITY_ANALYZED`, analysis `probability-5cfe4c1ba7e22775e3dcf880`, complete coverage for these two entries, zero comparison changes and zero unresolved candidates.
Source revision is `8125f5ec0eb9549a399d9851a6f046073c4cf0006b0cd8fab9b5ea86814f4798`.
Scenario hash is `07d0e062e0464b5a8f79568203d5766306cbbb1e5efd262fa317439a8f7f8b2c`.
The parent read the full returned analysis artifact, SHA-256 `20d961743b9e4ca6ec8d62de5a37e94743f15e41ebc107e0260b3d3ec86bf427`, and opened its comparison PNG.
The analysis shows unchanged conditional proportions 2/5 spread and 3/5 contained when this unrestricted random list executes, with the restriction modifier inactive in this fixture.
Those are not event-firing or decision-click probabilities.

## Validation limits and remaining work

The comparison does not execute helper call frames or prove downstream receiver probabilities.
The restricted-factor sweep failed to activate its declared restriction and therefore establishes no sensitivity or rank-reversal result.
The one foreign-score caller storage correction remains a separate source tranche with an unsupported deterministic max-score adapter, not a passed probability comparison.
The broader thirty-nine-scenario contract, incident and target pools, complete event comparison and live-game evidence remain required.
No fallback or simplified movement route was introduced by this correction, and this document does not claim Event029 completion.
