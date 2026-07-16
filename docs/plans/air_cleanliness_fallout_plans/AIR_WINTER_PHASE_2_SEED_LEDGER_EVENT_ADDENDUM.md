# Air Winter Phase 2 Seed Ledger Event Addendum

## Status

This addendum is the reviewed contract for the Phase 2 seed-ledger incident. `chaosx.fallout.10` carries the opening policy choice and `chaosx.fallout.18` carries the delayed result. The contract leaves the Phase 2 route selector, monthly winter formulas, Fallout survival grading, and the Fallout living-world scheduler unchanged.

## Event shape

`chaosx.fallout.10` keeps its three opening choices:

1. open guarded seed vaults for measured planting
2. slaughter the herds for an emergency ration
3. preserve breeding stock through the winter ration

Each valid choice records one state branch, binds the current owner through the established pending-chain transaction, refreshes the country event cooldown, and schedules `chaosx.fallout.18` after 45 days. The refreshed 46-day cooldown remains one day longer than the result delay even when the opening popup was left unresolved. Guarded seed storage also diverts 10 percent of local factory availability for 46 days.

## Delayed outcomes

| Opening route | Delayed test | Outcome |
| --- | --- | --- |
| Guarded seed vaults | Reclamation above 25 and Exposure below 60 | A temporary factory diversion supports the trial. Successful plots add Food Reserve, Adaptation, and Reclamation. Failure removes Food Reserve and adds Disease Pressure and Building Damage Pressure. |
| Slaughter the herds | Fixed consequence | The emergency ration is followed by lower Food Reserve and Reclamation with higher Disease Pressure. |
| Preserve breeding stock | Food Reserve above 30 and Shelter Capacity above 25 | Surviving herds add Food Reserve, Adaptation, and Reclamation. Failure removes Food Reserve and Reclamation and adds Disease Pressure. |

The result has five mutually exclusive options. A player cannot choose a branch or success state that does not match the stored row.

## AI contract

The seed-vault AI test translates the result gate back through the opening route's two-point Reclamation gain. Its pre-choice Reclamation boundary is above 23. Exposure is unchanged, so its pre-choice ceiling remains below 60.

The breeding-stock AI test translates the result gate back through the opening route's four-point Food Reserve cost. Its pre-choice Food Reserve boundary is above 34. Shelter Capacity is unchanged, so its pre-choice boundary remains above 25.

The seed-vault choice also responds to low food. The breeding choice retains an additional preference at very high food reserves. Implausible routes receive the shared weak AI factor. The seed-vault manpower cost is checked when the option is shown and again when the click resolves.

## Ownership and cleanup

The three branch flags are part of `air_winter_event_has_pending_chain`. The generic pending owner remains the country that made the opening choice. Monthly reconciliation cancels a partial row or a row whose state changed owner. State reset and Fallout snapshot cleanup clear every pending branch and the temporary seed-vault industry modifier. The Fallout snapshot still freezes the live Air Winter values before cancellation.

A later owner can reopen the Phase 2 route. Before writing a new choice, the opening clears older seed-ledger branch and outcome memory from that state. Completed results clear the active branch, retain one outcome memory, refresh the state ledger, and let the shared reconciler remove the generic pending receipt.

## Assets and text

Both events use `GFX_report_event_air_winter_phase_2`. The temporary industry modifier uses `GFX_air_winter_phase_2`. These are dedicated Air Winter and Fallout assets. No zombie file, path, sprite, sound, or event identifier is used. The asset manifest covers the Phase 2 image route through event 18.

The result text names the selected state and uses the current government's Air Winter authority or official term. Tooltips disclose the delay, thresholds, and exact ledger changes.

## Review gates

- unique event id 18
- one opening branch per valid click
- five mutually exclusive delayed results
- exact pre-choice AI threshold derivation
- click-time affordability and target validation
- owner-bound cancellation and reset coverage
- 46-day factory diversion removed on result or cancellation
- matching final localisation with UTF-8 BOM
- dedicated asset manifest coverage
- no coupling to Fallout survival grading

The baseline's later post-Fallout food-recovery consequence remains outside this tranche because its numerical consumer is approval-gated. The active user contract also forbids political-power stores, so the opening uses manpower and the temporary local factory diversion instead.
