# Event 014 focus-tree final re-audit

Date: 2026-07-15

Mode: completion audit with two narrow in-scope repairs

Status: completion-ready within the Event 014 focus-tree scope

## Verdict

The Event 014 focus package satisfies the accepted 68/108/28 focus contract, all three trees are exclusion-aware reachable, all focus and idea art is registered and unique, the three-origin contract has no retired fourth-origin residue, pre-reveal text does not expose Hannibal, and both terminal routes require Chaos strictly greater than 1000.

| Priority | Open findings |
| --- | ---: |
| P0 | 0 |
| P1 | 0 |
| P2 | 0 |
| P3 | 0 |

No fallback, placeholder, simplification, omission, or blocker remains in this audit scope.

## Narrow repairs applied during this re-audit

1. Neutralized the last live fourth-origin-shaped internal flag name without changing the current general expansion focus:
   - old: `cannibalism_warlord_prison_depot_raids_open`
   - current: `cannibalism_warlord_detention_depot_raids_open`
   - reset: `cannibalism_warlord_focus_reset_contract`
   - producer: `cannibalism_warlord_focus_seize_prisons_and_depots`
   - consumer: `cannibalism_prepare_warlord_origin_operation_contract`
   - exact old-name references remaining: 0
2. Restored the accepted Wendigo route totals and five-point normalization:
   - `constant:cannibalism_wendigo_focus.stability_reward = 0.05`
   - `constant:cannibalism_wendigo_focus.war_support_reward = 0.05`
   - Stability applications: 3, for exactly +0.15
   - War Support applications: 5, for exactly +0.25
   - obsolete small/medium Stability or War Support ladder keys and references: 0

## Tree structure and reachability proof

The parser used comment-aware, quote-aware brace matching, resolved relative coordinates to absolute positions, and enumerated prerequisite alternatives while rejecting mutually exclusive combinations.

| Tree | Focuses | Roots | Prerequisite blocks | Prerequisite refs | Mutual refs | Feasible focuses | Max minimal path variants |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Warlord | 68 | 1 | 73 | 79 | 18 | 68 | 27 |
| Unified | 108 | 1 | 117 | 132 | 24 | 108 | 36 |
| Wendigo | 28 | 1 | 32 | 32 | 0 | 28 | 1 |
| Total | 204 | 3 | 222 | 243 | 42 | 204 | - |

The following counts are all zero:

- duplicate focus IDs, including cross-tree duplicates
- dangling or self prerequisites
- dangling, self, or asymmetric mutual exclusions
- unreachable focuses after mutual-exclusion constraints
- duplicate absolute positions
- unresolved relative positions or coordinate cycles
- prerequisite parents at or below their children
- missing `ai_will_do` blocks or AI bases
- missing completion rewards
- bypassed focuses

Cost distribution is 45 short and 23 normal for Warlord; 74 short, 25 normal, and 9 terminal for Unified; and 7 short, 18 normal, and 3 terminal for Wendigo.

## Route, AI, and reward proof

All 204 focuses call one exact completion helper. The three helper sets contain 68/68, 108/108, and 28/28 unique normalized bodies. The helpers set 309 distinct focus-contract flags, and every one has at least one downstream `has_country_flag` consumer across the 90 Event 014 runtime files.

AI bases are nonzero on every focus:

| Tree | Maximum | Urgent | High | Standard |
| --- | ---: | ---: | ---: | ---: |
| Warlord | 9 | 20 | 30 | 9 |
| Unified | 37 | 32 | 29 | 10 |
| Wendigo | 3 | 11 | 13 | 1 |

All mutually exclusive route roots retain nonzero standard bases. The three origin roots use `constant:cannibalism_ai.invalid_factor` outside their matching origin. The reusable warlord AI file contains one common profile plus distinct Island Host, Siege Commune, and March Host profiles.

The previously called-out reward paths are substantive and distinct:

- `Battlefield Harvest` sets `cannibalism_warlord_battlefield_harvest_upgraded`, while `Organize Battlefield Recovery` opens the base harvest. The paid-origin-operation consumer adds the upgrade recovery, and the capitulation consumer uses `cannibalism_warlord_harvested_countries` so each defeated country pays once. The base receipt is 75 Larder, 350 infantry equipment, and 35 support equipment; the upgrade adds 25 Larder, 125 infantry equipment, and 15 support equipment.
- `March: Raid the Depots` sets `cannibalism_warlord_depot_raids_open` and adds medium Larder recovery plus captured trucks to paid March operations. General `Raid the Neighboring States` sets the separate `cannibalism_warlord_neighboring_state_raids_open` and adds small duration, Larder, and infantry recovery on every origin, including March.
- `Raise the First Anchors` adds anchor strength, defenses, and authority.
- `Feed the Anchor Guardians` adds anchor strength, paid Pack capacity, and command power.
- `Link the Transformation Anchors` adds anchor strength, infrastructure, and political power.

The visible tooltips describe these current state transitions.

## Origin and secrecy proof

`cannibalism_origin` contains exactly:

- `none = 0`
- `island_host = 1`
- `siege_commune = 2`
- `march_host = 3`

Origin selection, flags, ideas, specialist spawning, tree overlays, and AI profiles use only those three playable origins. The Warlord tree contains one four-focus overlay for each origin. The reusable CBA-CBH slots remain origin-agnostic until the selection effect applies a package.

An exact runtime and current-source-inventory scan found:

- retired Prison Host identifiers: 0
- retired Prison Host basenames: 0
- `lockhouse`, `lock_house`, or `lock-house` identifiers/basenames: 0

The scan intentionally targeted retired identifiers such as `prison_host`, `origin_prison`, `warlord_prison_`, `goal_cannibalism_warlord_prison_`, and `idea_cannibalism_prison_host`. Current general prisoner, detention, and depot content is not a fourth origin.

The current `goal_cannibalism_warlord_train_the_origin_specialists` icon visibly combines three motifs only: island anchor/rope, siege shovel/masonry, and march wheel/road gear. It contains no fourth-origin motif, text, or portrait. Processed PNG and live DDS RGBA pixels are identical, with SHA-256 `c90cfa7b3c94dc71033b65a5c6a82f13c054bc2dccb4ac477ed5556d4da32c3b`.

All 612 focus-facing localisation keys (title, description, and tooltip for 204 focuses) exist exactly once and are nonempty. The localisation file has its UTF-8 BOM. The 204 pre-reveal Warlord values contain zero instances of `Hannibal`, `Lecter`, or `Wendigo`. The Unified tree requires `cannibalism_reveal_complete`; the Wendigo tree requires that flag plus the transformed original-ZZZ country and character. The unification and Wendigo effects set the reveal flag before loading their post-reveal tree state.

## Focus and idea asset proof

Focus asset closure:

- 204 focus icon references, all unique
- 204 base sprite definitions and 204 shine definitions
- 204 existing texture paths
- 204 unique DDS SHA-256 hashes
- 204 files in `gfx/interface/goals/014_cannibalism`, with 0 unused
- all 204 are valid 94x86 legacy BGRA DDS files
- 0 missing, duplicate, or mismatched registrations

Current source packages:

| Package | Source PNG | Alpha PNG | Processed PNG | Package DDS | Live pixel matches |
| --- | ---: | ---: | ---: | ---: | ---: |
| Warlord focus icons | 68 | 68 | 68 | 68 | 68 |
| Unified focus icons | 108 | 108 | 108 | 108 | 108 |
| Wendigo focus icons | 28 | 28 | 28 | not duplicated | 28 |
| Registered static icons | 30 | 29 | 30 | 30 | covered by GFX closure |

The registered static package has 29 alpha intermediates because its opaque category panel intentionally does not use one.

Idea asset closure:

- 37 live Event 014 idea picture declarations, all unique
- 37/37 exact `GFX_idea_<picture>` definitions
- 62 runtime idea DDS files, all registered
- 62 unique DDS SHA-256 hashes
- 54 files at 64x64 and 8 repaired files at 68x68, all valid legacy BGRA DDS
- 0 missing, duplicate, or unregistered idea textures

The eight visually reviewed repaired ideas are:

- `cannibalism_wendigo_conjoined_hunger`
- `cannibalism_wendigo_winter_feeding_network`
- `cannibalism_wendigo_locked_terminal_form`
- `cannibalism_liberated_feeding_states`
- `cannibalism_identification_and_burial_emergency`
- `cannibalism_broken_military_trust`
- `cannibalism_rebuilt_supply_discipline`
- `cannibalism_permanent_vigilance`

The contact sheet shows eight distinct, readable national-spirit icons without placeholders, focus-art reuse, or retired fourth-origin motifs.

Full Event 014 GFX closure covers the seven `interface/014_cannibalism*.gfx` files plus Event 014-owned references in `chaosx_pictures.gfx` and `chaosx_super_events.gfx`:

- 9 GFX files
- 812 texture references
- 598 unique texture paths
- 598 unique texture hashes
- 31 shared-file references
- 0 missing files

## Terminal gates, counterplay, and intentional terminal power

The terminal threshold used by both routes is `constant:cannibalism_evolution_threshold.world_end_chaos = 1000`. Every active Event 014 terminal check uses either `compare = greater_than` or the short `>` form, so Chaos must be strictly greater than 1000.

The ordinary terminal additionally requires the unified country, terminal route readiness, every operational package, the ordinary scenario, network reach at least 92, more than 35 controlled states, at least 25,000 thousand consumed population, at least 750 Larder, no prior world end, and no disabled world end. The final focus also requires the paid terminal-mobilization preparation flag.

The Wendigo countdown additionally requires the transformed country, winter network, completed countdown route, at least 3 live anchors, network reach at least 85, more than 20 controlled states, at least 10,000 thousand consumed population, at least 5 winter victories, at least 80 authority, at least 800 Larder, and no broken or locked transformation. Terminal lock further requires the active countdown, completed terminal route, enabled Wendigo scenario, and progress at 100.

Counterwar decisions remain available before lock and allow defenders to identify, assault, disrupt, and break recruitment sites and anchors. The full terminal hunt sequence costs 1,000 Larder, 125 command power, 1,500 infantry equipment, 300 support equipment, and 1,500 fuel. A four-action defender break sequence costs 40,000 manpower, 120 command power, 2,000 infantry equipment, and 400 support equipment. Hunt success adds 5 progress and failure removes 10.

No focus or hunt action directly sets `world_end`. `cannibalism_complete_wendigo_terminal_lock` is reached through the transformation pulse and runs only when `cannibalism_wendigo_can_lock_terminal_form` passes. The locked idea's extreme post-lock modifiers are intentional: +300 percent attack, defense, breakthrough, and recovery; +200 percent organization; +100 percent speed and reinforce rate; and -99 percent supply consumption, alongside the terminal leader package. The accepted design explicitly makes the completed lock effectively undefeatable after the counterplay window closes.

## Files changed by this audit

- `common/scripted_effects/014_cannibalism_warlord_focus_effects.txt`
- `common/scripted_effects/014_cannibalism_warlord_decision_effects.txt`
- `common/script_constants/014_cannibalism_wendigo_focus_constants.txt`
- `common/scripted_effects/014_cannibalism_wendigo_focus_effects.txt`
- `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_focus_tree_reaudit_2026-07-15.md`

No commit was created.

## Authorities and skills used

The audit followed the offline Paradox wiki snapshot, vanilla HOI4 documentation and focus/AI precedents, the accepted Event 014 specifications and addenda, and the repository skills `chaos-redux-focus-trees`, `chaos-redux-events`, `chaos-redux-subagents`, `chaos-redux-decisions-missions`, and `chaos-redux-event-assets`.
