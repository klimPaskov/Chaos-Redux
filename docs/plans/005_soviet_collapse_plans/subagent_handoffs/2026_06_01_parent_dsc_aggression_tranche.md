# Event005 Parent Handoff - Dead Soldiers Congress Aggression Tranche

## Scope

Parent patch for the Dead Soldiers Congress high-chaos successor.

## Files Changed

- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`

## Gameplay Changes

- `soviet_collapse_setup_dsc_successor` now immediately:
  - claims the Dead Soldiers front-road states,
  - cores any of those claimed states it already controls,
  - spawns custom splinter assault columns,
  - launches neighbor war goals immediately at chaos tier 5, chaos triggerable scenario launch, or forced-all-chaos release.
- `DSC_stalingrad_roll_call` now reinforces the controlled-front-road coring loop early instead of waiting for late expansion focuses only.
- `DSC_grave_ordnance_claims` now also cores controlled front-road states and spawns assault columns when high-chaos expansion claims are granted.

## Why This Is Aligned

The Dead Soldiers Congress is meant to play as an extreme high-chaos military death-state. This patch moves some aggression from late decisions/finale only into setup and early route progression, so the country starts acting dangerous when it appears on the map.

## Validation

- Brace balance clean for touched files.
- No unsupported `<=` or `>=` in touched files.
- `git diff --check` clean for touched files.
- `git diff --name-only -- gfx/flags interface/flags` produced no output.

## Remaining Risks

- This is not a full focus-tree rework. It deepens one named chaos country and should be followed by equivalent tranches for the remaining chaos-country identities and ordinary republic trees.
- The full release/scenario coverage still needs a separate verified matrix against every possible SOV-core tag and every special chaos tag.
