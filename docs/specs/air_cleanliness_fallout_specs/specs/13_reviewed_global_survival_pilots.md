# Reviewed Global Survival Pilots

This file promotes the reviewed Names for the Missing contract into the source-spec suite. It records the implementation boundary for candidate 269 without claiming that the dormant Fallout scheduler is active.

## Names for the Missing

| Surface | Contract |
| --- | --- |
| Candidate | 269 |
| Transaction | 710013 |
| Route | 7113 |
| Event namespace | `chaosx.fallout` |
| Target | No target type and target value zero |
| Human envelope | Opening, one delayed result, and one delayed callback |
| Human opening cost | 3 visible budget units reserved for the full envelope |
| Human delayed rows | One visible budget unit for the result and callback |
| Hidden AI delayed rows | Zero visible budget units for the result and callback |
| Result delay | 21 days |
| Callback delay | 180 days |
| Event Log | History 9118 with fifteen payloads |
| Asset | `GFX_report_event_fallout_names_missing` |

Eligibility requires a current country registry row, current Fallout survival rows, at least 25,000 recorded civilian deaths, Recognition below 65, a clear durable memory, and one affordable branch. The player country is not replaced by this chain. No state target, successor assignment, or ordinary super-event path is created.

## Deterministic grading

The candidate converts the country Deaths ledger into a bounded scheduler severity with the explicit formula:

`severity = clamp(recorded civilian deaths * 0.001, 0, 100)`

Names uses `survival_resource` as its pressure source, so mechanic pressure is exactly zero. Recognition supplies the state value. Result grading freezes Deaths, Recognition, Cohesion, and exposure before the delayed row is reserved. Branch thresholds select success, partial, or failure without random or MTTH selection.

## Effects and cleanup

The four branches spend distinct Food, Scrap, Power, or Recognition resources and alter Food, Scrap, Power, Recognition, Cohesion, Stability, War Support, and intelligence exposure. Result failure requests 0.4 percent of each owned state's remaining population through the Deaths contract. Callback failure requests 0.2 percent through a separate helper. No direct population effect is used.

Result and callback history are idempotent. Cleanup releases delayed receipts, clears temporary registry values, retains durable memory and exposure, and records scheduling failure when a follow-up cannot be reserved.

## Implementation and proof boundary

Gameplay files, Event Log mappings, localisation, the dedicated report picture, and the asset crosswalk are wired. The candidate remains dormant. Live ordinary receipt production, delayed dispatch, host authority, save recovery, multiplayer input blocking, and runtime Event Log delivery remain unobserved. The exact native all-valid-province thermonuclear sweep is separately blocked and is not implied by this pilot.

The global family matrix still lists memorial, archive, and family-reunion follow-ups as future consumers. Those consumers are queued until a later reviewed tranche and are not counted as implemented by candidate 269.
