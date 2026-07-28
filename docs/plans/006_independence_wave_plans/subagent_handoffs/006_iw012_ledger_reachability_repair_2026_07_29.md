# IW-012 ledger reachability repair — 2026-07-29

## Finding

The accepted IW-012 contract requires six costed projects to establish a founding posture and keeps Coastwatch Readiness at 55 as the Armed Neutrality gate. The previous implementation started Coastwatch at 20, added only 15 before Armed Neutrality, and therefore could never reach the 55 gate or the 60 harbour-stability threshold.

## Repair

The registers, municipal charter, North Atlantic Compact, and former-host charter now each add the centrally tuned `independence_wave_ice_value.minor_gain` (5) to Coastwatch Readiness. Coastwatch expansion and Armed Neutrality retain their existing `major_gain` (15) contributions. Costs, project durations, serialization, route ownership, and threshold values remain unchanged.

## Reachability proof

The executable project order must settle the former-host charter before the Compact. The Compact requires 45 Compact Support and Network Standing at the observed band of 15; setup starts Network Standing at 10, so a separate costed network action or reviewed focus reward must raise it before the Compact project. The six-project duration total excludes that network action and therefore does not by itself prove the 210-day harbour margin.

| Stage | Coastwatch | Shipping Security | Route consequence |
| --- | ---: | ---: | --- |
| Starting ledger | 20 | 20 | No route commitment |
| Registers | 25 | 30 | Shipping administration exists |
| Municipal charter | 30 | 35 | Constitutional route can qualify through Civic Cohesion |
| Coastwatch expansion | 45 | 45 | Coastwatch institution exists |
| Former-host charter | 50 | 50 | Compact Support reaches the 45-point negotiation gate after the charter; Network Standing still needs the observed-band action |
| North Atlantic Compact | 55 | 55 | Compact and Network Standing gates are reachable only after the former-host charter and the separate network action |
| Armed Neutrality | 70 | 65 | Emergency route and the 60/60 harbour-stability gate are reachable |

The other three ledgers remain within the same 0–100 clamp and preserve their existing route signals. The six projects still total 1,230 project-days before the 1,440-day harbour deadline, but the separate network action and its costed duration must be identified and validated before the accepted 210-day margin can be claimed.

## Files

- `common/decisions/006_independence_wave_ice_decisions.txt`
- `docs/events/006_independence_wave_iw012_ice_package.md`
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`

## Validation boundary

Static source calculations confirm the intended route and harbour thresholds are reachable. Live project timing, AI ordering, focus visibility, harbour mission resolution, save/load, and runtime package admission remain separate Event 006 completion gates.
