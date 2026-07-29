# Decision custom-cost localisation follow-up

## Status

Deferred for parent review because the migration requires coordinated localisation and payment-path verification beyond the bounded cleanup patch.

## Scope

The audit found 161 Event 001 to Event 020 custom-cost keys without one or both of the engine-resolved `<key>_blocked` and `<key>_tooltip` variants.

The affected decision files are `001_communism_spread_decisions.txt` with 4 keys, `005_soviet_collapse_decisions.txt` with 11 keys, `010_death_decisions.txt` with 5 keys, `014_cannibalism_decisions.txt` with 90 keys, and `016_brilliant_scientist_directorate_project_board.txt` with 51 keys.

## Required migration

Do not bulk-copy the normal cost string into every missing variant.

Each family needs a source review to confirm which inputs are actually spent by its completion effect, whether a regular political-power cost is also present, and whether factory use or duration belongs in the hover text.

Implement by event family, beginning with the low-count Event 001 and Event 010 groups.

For each key, add a red `<key>_blocked` form and a concise `<key>_tooltip` form whose values, icons, duration, and factory commitment match the corresponding trigger and payment effect.

Use existing script constants or scripted-localisation values rather than hardcoded duplicate amounts.

After each family, verify every `custom_cost_text` call resolves all three forms and that the payment effect cannot spend a resource absent from its custom trigger.

## Evidence

The cost scan was limited to `common/decisions/001_*` through `020_*` and their English localisation keys.
