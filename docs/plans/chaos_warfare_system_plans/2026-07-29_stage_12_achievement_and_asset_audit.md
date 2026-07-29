# Stage 12 achievement and asset audit

Date: 2026-07-29

Status: eleven supported achievements active; four unsupported achievements skipped; full fifteen-identity art archive retained

## Scope decision

The accepted prompt proposed fifteen Chaos Warfare achievements. Four could not be implemented with exact current-version receipts or an accepted eligibility definition:

- `chaos_warfare_air_still_breathable` lacks an accepted CBRN regional-power definition.
- `chaos_warfare_no_wind_is_friendly` depends on unavailable exact ground-operation weather, forecast-reversal, and friendly-exposure receipts.
- `chaos_warfare_antidote_arrived` depends on the unavailable exact nerve-suppression state transaction.
- `chaos_warfare_unbroken_supply_corridor` depends on unavailable assigned-Army supply-ratio and major-offensive-objective receipts.

The user authorized unsupported content to be skipped. These four entries, completion predicates, localisation entries, and sprite registrations were removed from active runtime surfaces. No major-only narrowing, state-control proxy, duration estimator, neutral receipt, or other fallback replaces them.

## Active package

The active registry contains eleven supported achievements:

1. `chaos_warfare_masks_before_guns`
2. `chaos_warfare_prepared_army`
3. `chaos_warfare_poisoned_victory`
4. `chaos_warfare_clean_hands_dirty_work`
5. `chaos_warfare_evidence_survives`
6. `chaos_warfare_quarantine_without_collapse`
7. `chaos_warfare_arsenal_dismantled`
8. `chaos_warfare_terminal_contagion`
9. `chaos_warfare_mask_for_every_door`
10. `chaos_warfare_weapon_turns_home`
11. `chaos_warfare_first_user_pays`

Every active entry has a dedicated completion predicate, final localisation, and completed, grey, and not-eligible icon registration.

The one-time startup transaction records campaign eligibility and starting civil-defence identity. `A Mask for Every Door` consumes the starting civil-defence receipt, preventing profile switching from manufacturing eligibility.

`Quarantine Without Collapse` reads exact current and needed trucks and trains through `get_supply_vehicles_temp`, requires 80 percent of each needed class at catastrophic-outbreak recovery, and writes a dedicated supply-ready receipt only at that transaction.

`Arsenal Dismantled` rejects post-start regime change and capitulation. `Terminal Contagion` requires the 90-day interval, ongoing war, active-sanctions history, and serious Chemical contamination or catastrophic Biological history. `A Poisoned Victory` requires current high Condemnation rather than a historical peak alone.

## Asset disposition

The production package contains fifteen source masters and forty-five completed/grey/not-eligible variants. All forty-five DDS files remain preserved as validated art output, but only the thirty-three variants for the eleven supported achievements are registered by `interface/chaosx_achievements.gfx`.

The four skipped triplets are archive material only. Their existence does not imply an active achievement or a fallback contract.

The artifact report records exact 64-by-64 one-level uncompressed BGRA DDS output and pixel identity between processed PNGs and final DDS files. No placeholder icon, resized cross-type substitute, or overwritten military-raid icon is used.

## Remaining validation boundary

The eleven active achievements require final package reachability and anti-exploit review in the completion audit. Live unlock observation remains user-owned.
