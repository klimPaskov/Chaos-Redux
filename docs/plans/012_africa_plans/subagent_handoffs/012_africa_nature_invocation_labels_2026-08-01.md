# Event 012 Africa — Nature Invocation Labels Handoff

## Scope

This bounded content tranche gives the existing priority-member nature decisions package-specific visible invocation names. It does not create tags, countries, target stores, effects, or natural-disaster families.

## Changed files

- `common/scripted_localisation/012_africa_scripted_localisation.txt`
- `localisation/english/012_african_union_l_english.yml`
- `docs/events/012_africa/natural_disaster_weapons.md`

## Runtime contract

- The two existing decisions still use `africa_natural_disaster_enemy_targets` and the shared reserve, cooldown, revalidation, Event 013 bridge, and cleanup kernels.
- The action descriptions now resolve through `GetAfricaPriorityMemberNatureInvocationName`, selecting one label from the existing 16 package predicates.
- If a package is not mapped, the scripted localisation falls back to `Unrecorded Nature Invocation`; no technical identifier or tag is generated from the display text.

## Validation

- Static key audit must confirm 17 new localisation keys (16 package labels plus fallback) and one new defined-text block.
- The package predicate list must remain exactly the 16 approved priority packages.
- Localisation remains UTF-8 with BOM.

## Remaining gates

The action ledger remains 90 implemented and 12 explicitly gated. End-to-end priority-package receipts, W5 package receipts, live scenario proof, and the requested model/audio/native-review surfaces remain blocked and are not weakened by this label-only tranche.
