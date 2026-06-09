# Event005 parent release intensity tranche

Date: 2026-06-04

Scope:
- `common/script_constants/005_soviet_collapse_constants.txt`

No-touch confirmation:
- No `gfx/flags`, `interface/flags`, flag sprite, or flag definition files were edited.

## Changes

Raised central release tuning values so the existing dynamic release system reaches niche republics and nested releasables more aggressively.

Changed release constants:
- `follow_on_gathering_storm_releases`: 24
- `follow_on_gathering_storm_internal_releases`: 16
- `follow_on_chaos_tier_4_releases`: 96
- `follow_on_chaos_tier_5_releases`: 160
- `follow_on_chaos_tier_4_internal_releases`: 56
- `follow_on_chaos_tier_5_internal_releases`: 96
- `follow_on_release_cap`: 180
- `terminal_ordinary_release_passes`: 180
- `terminal_all_possible_release_passes`: 320

Reasoning:
- The existing release system already uses dynamic possible-country scans, terminal all-core release passes, Soviet subject liberation, chaos successor spawning, terminal leagues, and anti-Soviet/breakaway war starts.
- The weak point was release throughput: gathering storm and high-chaos cascades did not have enough headroom to reliably show many niche internal republics before the terminal path.
- Terminal/scenario exhaustive passes now have more headroom for nested releasables that only become valid after earlier releases transfer states.

## Validation

Checks run:
- Diff whitespace check on touched Event005 focus, localisation, constant, and handoff files.
- Unsupported comparison operator scan on touched Event005 gameplay files and handoff docs.
- Brace-balance check on touched Event005 focus, localisation, and constants files.
- Focus layout audit from the paired focus tranche still reports zero same-row mutual-exclusion spans through intervening nodes and zero duplicate same-tree focus coordinates.

## Remaining gaps

This is a tuning and throughput tranche, not a complete proof that every possible Soviet-core country appears in every live game path.

Remaining broad work:
- Runtime validation or a deeper scripted audit of every possible country with a Soviet-core state.
- Confirming all pressure successor spawn helpers can fire in the intended chaos tiers.
- Confirming scenario normal mode excludes only special chaos successors while still releasing all ordinary possible Soviet-core countries.
- Confirming chaos scenario mode spawns every special successor and starts the intended hostile wars.
