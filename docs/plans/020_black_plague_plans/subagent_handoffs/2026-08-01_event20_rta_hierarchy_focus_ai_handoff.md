# Event 020 RTA hierarchy focus AI handoff

Date: 2026-08-01

## Scope

This bounded gameplay tranche adds route-aware AI weights to the reusable `RTA` hierarchy branch. It does not add a country tag, a disease category, a human manpower or equipment path, or any model asset.

## Runtime changes

- `common/script_constants/020_black_plague_rat_constants.txt` adds centralized fixed-point factors for hierarchy sprawl, concentration, overseas pressure, Hunger-crisis urgency, and hierarchy follow-up preference.
- `common/national_focus/020_black_plague_rat_focus_tree.txt` adds `ai_will_do` blocks to `black_plague_rat_four_mouths`, `black_plague_rat_choose_a_voice`, and `black_plague_rat_read_the_marks`.
- The three follow-up focuses `black_plague_rat_many_nests_one_signal`, `black_plague_rat_fang_above_the_warren`, and `black_plague_rat_stolen_route_memory` now reinforce the selected route with the same live conditions.

Distributed Instinct is preferred when the carrier spans multiple controlled states or uses a Field or Urban archetype. Dominant Beast is preferred for a concentrated carrier, a War archetype, or an active Hunger crisis. Emergent Cunning is preferred for a Dock archetype after the verified Evolution II overseas gate. These weights change AI selection only; the existing completion rewards and runtime route consumers remain authoritative.

## Validation

- Both touched Clausewitz files have balanced braces and quotes.
- No unsupported `<=` or `>=` operators were introduced.
- Existing scripted triggers and constants resolve by exact identifier: `black_plague_rat_hunger_is_crisis`, `black_plague_evolution_ii_active`, `black_plague_rat_hierarchy_route`, and `black_plague_value.one`.
- The offline focus inspector could not complete a whole-workspace scan because it returned `SCAN_BYTE_LIMIT`; no source was mutated by that tool. Static source checks remain clean, and the existing prior RTA tree audit covers prerequisite and mutual-exclusion structure.

## Remaining risks

No live game process was launched. Focus AI ranking and the timing of the first post-emergence hierarchy choice still require consumer validation. Broader narrative-depth and presentation work remains tracked in the Event 020 overview and content tranche handoff.
