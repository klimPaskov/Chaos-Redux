# Event 011 Secret Alliance achievements

All six Event 011 achievements are available to any human tag. Their authoritative definitions are in `common/achievements/chaos_redux_achievements.txt`. This document records the gameplay predicates, snapshots, disqualifiers, scenario rules, localisation, and icon wiring.

## Shared tracking contract

The event snapshots normal, scenario, and forced/debug origin separately. A normal origin is recorded only for the automatic Event 011 opening. Coalition Unmasked records scenario intensity and clears normal origin. A launch performed through debug or force-trigger state records `achievement_secret_alliance_forced_origin`. Forced origin disqualifies all six achievements.

Every normal or scenario initialization first clears the target's Event 011 run snapshots, qualification flags, resolution flags, and starting-capital state. Achievement evidence therefore belongs to one pact only and cannot carry into a later manual or automatic run.

`chaosx.nr11.900` is the hidden AI-target test entry. It is triggered only from a valid AI country scope, temporarily enables the AI target initializer, and sets `secret_alliance_ai_test_origin`. Event initialization converts that origin into `achievement_secret_alliance_forced_origin`. The entry is absent from player-facing content and cannot qualify any Event 011 achievement.

At public reveal the fixed target snapshots valid active membership, active majors, Evidence, independent evidence-class count, whether every active member was confirmed, whether a founder or major sponsor had been turned, whether that controlled channel survived, and the number of members that must later leave for Divide the Table. Starting-capital control is checked at settlement. Innocent public naming, normal war against an innocent lead, and annexation of an unconfirmed suspect are recorded as durable disqualifiers where applicable.

## The Empty Chair

- Eligibility: normal automatic Event 011 origin, human target, and target has not capitulated.
- Required: correctly confirm a true founder and collapse the concealed pact before any public reveal.
- Disqualifiers: publicly name or normally attack an innocent suspect, annex an unconfirmed suspect, maximum scenario origin, or forced/debug origin.
- Snapshot: `achievement_secret_alliance_true_founder_confirmed` is set when confidence confirmation identifies a true founder. `achievement_secret_alliance_empty_chair_ready` is set only by the hidden-collapse effect after all disqualifiers are checked.

## Every Thread

- Eligibility: normal automatic Event 011 origin, human target, and target has not capitulated.
- Required at reveal: Evidence is exactly the complete-network band, all six independent evidence classes are present, and every valid active reveal member is correctly confirmed.
- Disqualifiers: an innocent country was publicly named or the run has forced/debug origin.
- Snapshot: Evidence, independent-class count, and all-members-confirmed are copied to the fixed target before the public faction is created.

## Their Man in the Room

- Visibility: hidden achievement.
- Eligibility: normal automatic Event 011 origin, human target, and target has not capitulated.
- Required: turn a founder or major sponsor, preserve its controlled channel through reveal, and have an accepted planted false plan convert into a public-war consequence when the pact is revealed.
- Disqualifiers: maximum scenario origin or forced/debug origin.
- Snapshot: founder-or-major status and channel survival are recorded before the public faction transaction. `achievement_secret_alliance_their_man_in_the_room_ready` is set during reveal conversion only when the accepted false plan and both preserved-channel snapshots are present; it does not wait for a later target-victory branch.

## Divide the Table

- Eligibility: human target that has not capitulated. Normal or scenario origin is allowed.
- Required: remove at least half of the valid reveal membership from the target war through Event 011 defection, call refusal, fracture, or separate terms. The threshold is the reveal count divided by two and rounded once at reveal.
- Disqualifiers: coalition victory or forced/debug origin.
- Counting rule: capitulation alone does not increment `secret_alliance_event_fracture_exit_count`.

## Surrounded, Not Buried

- Eligibility: Coalition Unmasked at Maximum intensity. The achieved composition reaches the requested roster or exactly exhausts every safe valid candidate, even when that safe pool contains fewer than eight countries. Requested major sponsorship is achieved. The human target has not capitulated.
- Required: survive the configured opening-pulse threshold, keep control of the snapshotted starting capital, remain independent, and reach target victory through dissolution or settlement.
- Disqualifiers: human-consent bypass, forced/debug origin, or any active world-end state.
- Snapshot: requested members, requested majors, safe valid pool, achieved members, and achieved majors are stored before reveal. `achievement_secret_alliance_maximum_composition_qualified` is set only from those immutable values. The target capital is saved before reveal. Opening survival is recorded by the public-war pulse. A qualifying dissolution or negotiated/continued settlement records `achievement_secret_alliance_resolution_qualified`; only then is final readiness set.

## Two Giants, One Grave

- Visibility: hidden achievement.
- Eligibility: normal Event 011 origin or Coalition Unmasked at High/Maximum intensity, human target, and target has not capitulated.
- Required: the reveal snapshot contains at least two active major members, the target keeps its starting capital, the target wins, and Coalition Resolve falls below the collapse band.
- Disqualifiers: Low/Medium scenario origin or forced/debug origin.

## Localisation and icons

Names, descriptions, and exact player-facing eligibility text are in `localisation/english/chaosx_achievements_l_english.yml`. Each achievement has three final 64x64 DDS files: normal, grey, and not eligible.

| Achievement | Sprite root | Final files |
| --- | --- | --- |
| The Empty Chair | `GFX_achievement_011_secret_alliance_the_empty_chair` | `gfx/achievements/011_secret_alliance_the_empty_chair{,_grey,_not_eligible}.dds` |
| Every Thread | `GFX_achievement_011_secret_alliance_every_thread` | `gfx/achievements/011_secret_alliance_every_thread{,_grey,_not_eligible}.dds` |
| Their Man in the Room | `GFX_achievement_011_secret_alliance_their_man_in_the_room` | `gfx/achievements/011_secret_alliance_their_man_in_the_room{,_grey,_not_eligible}.dds` |
| Divide the Table | `GFX_achievement_011_secret_alliance_divide_the_table` | `gfx/achievements/011_secret_alliance_divide_the_table{,_grey,_not_eligible}.dds` |
| Surrounded, Not Buried | `GFX_achievement_011_secret_alliance_surrounded_not_buried` | `gfx/achievements/011_secret_alliance_surrounded_not_buried{,_grey,_not_eligible}.dds` |
| Two Giants, One Grave | `GFX_achievement_011_secret_alliance_two_giants_one_grave` | `gfx/achievements/011_secret_alliance_two_giants_one_grave{,_grey,_not_eligible}.dds` |

All triplets are registered in `interface/chaosx_achievements.gfx`. Their generated sources, processed PNGs, recovered standard not-eligible overlay, and validation evidence are recorded in `docs/assets/011_secret_alliance/manifest_icons_ui_animation.md`.
