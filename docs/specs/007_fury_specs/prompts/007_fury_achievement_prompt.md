# Achievement implementation prompt for Event 007 Fury

Use the Fury achievement spec at `docs/specs/007_fury_specs/specs/007_fury_achievements_spec.md`.

Implement achievements only after core Fury state flags, scenario flags, and defeat tracking exist.

## Required achievements

Implement or prepare these achievements.

1. `achievement_fury_fuse_cut`, Fuse Cut Short.
2. `achievement_fury_no_minor_major`, No Minor Shall Be Major.
3. `achievement_fury_firebreak`, The Firebreak Holds.
4. `achievement_fury_pact_breaker`, Break the March Pact.
5. `achievement_fury_ten_fires`, Ten Fires, No Dawn.
6. `achievement_fury_last_neighbor`, The Last Neighbor Stands.
7. `achievement_fury_world_without_fury`, A World Without Fury.
8. `achievement_fury_rivals_burn`, Let the Fires Fight.
9. `achievement_fury_major_without_faction`, Alone Against the Major.
10. `achievement_fury_no_cores`, Paper Borders Hold.

## Tracking requirements

Add tracking for:

- player was never Fury.
- Fury actor created.
- first Fury conquest.
- Fury major threshold.
- Fury world-end start and defeat.
- scenario intensity.
- scenario type.
- Fury actor count at scenario setup.
- Fury coring completed.
- Fury Pact formed.
- two Fury actors fought.
- player faction status for factionless achievement.
- player capital held where needed.
- player contribution or valid aid contribution.

## Asset requirements

Use the asset prompt for 64x64 achievement icons. Completed icons are required first. Grey and not-eligible variants can follow existing Chaos Redux achievement patterns.

## Design rule

Do not make achievements unlock simply because the event fired. Every achievement must require player action, difficult containment, scenario challenge completion, or a rare route outcome.

## Disqualifiers

Most Fury achievements should fail if:

- the player becomes a Fury country through console, tag switch, or unexpected setup.
- the achievement requires ordinary random Fury but the player used Maximum scenario.
- the player joins the Fury faction.
- the achievement route requires factionless play and the player joins a faction.

## Documentation

Update achievement docs and event docs with each achievement's route and tracking flags.
