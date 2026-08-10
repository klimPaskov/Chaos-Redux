# Event 005 Successor Relations

Status: Implemented. The Black International, Free Soviet Congress, and Iron Production Bloc use the existing Event 005 regional-faction lifecycle and do not require a parallel diplomacy system.

## Player flow

An eligible Soviet-collapse successor sees one or more bloc-founding decisions after regional foundation pressure is active. Founding spends the shared regional-faction political-power and command-power costs, marks the founder and member identity, creates the named faction, recruits eligible governments that are not subjects, faction members, or at war with the founder, applies the established pressure against Moscow, and opens the faction's charter event.

The Black International accepts Black Banner and anarchist successors, including the Ukrainian Black Banner route. The Free Soviet Congress accepts communist governments, council routes, socialist route-depth milestones, and the Kronstadt naval council state while excluding Black International identities. The Iron Production Bloc accepts factory, rail, Ural worker, mining, depot-depth, and unconventional-warfare production authorities. UWR and KMB are therefore first-class Iron Production Bloc candidates rather than isolated follow-up packages.

After formation, all three blocs use the shared invitation, coordination, common-goal, goal-resolution, tension-mediation, unit-deployment, defensive-war, security-zone mandate, and member-withdrawal decisions. Missing aligned members are valid security-zone targets through the same mandate trigger used by the geographic leagues. Faction leaders cannot use the withdrawal action, preventing a leaderless or repeatedly abandoned bloc. Non-leader withdrawals clear the appropriate identity-member flag before leaving.

## Event and script wiring

The founding effects fire `chaosx.nr5.33` for the Black International, `chaosx.nr5.34` for the Free Soviet Congress, and `chaosx.nr5.37` for the Iron Production Bloc. Each charter event offers the established binding staff, local autonomy, and patron-channel choices, with the same cohesion, tension, stability, recognition, depot, and Soviet-pressure consequences as the other regional factions.

The Black Banner endgame calls the shared `soviet_collapse_found_or_join_black_international` effect. The first qualifying endgame creates and announces the faction; a later Black Banner successor joins the existing faction and receives the same member registration instead of attempting to create a duplicate faction.

The principal implementation files are:

- `common/decisions/005_soviet_collapse_decisions.txt`
- `common/decisions/categories/005_soviet_collapse_categories.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/scripted_triggers/005_soviet_collapse_triggers.txt`
- `events/005_soviet_collapse.txt`
- `localisation/english/005_soviet_collapse_l_english.yml`

## Assets

All required final assets already existed and are retained under stable identifiers. The three decision icons are `GFX_decision_soviet_collapse_black_international`, `GFX_decision_soviet_collapse_free_soviet_congress`, and `GFX_decision_soviet_collapse_iron_production_bloc`, defined in `interface/005_soviet_collapse.gfx` and backed by DDS files under `gfx/interface/decisions/005_soviet_collapse/`. The full and miniature faction logo families are defined in the same GFX file and backed by DDS files under `gfx/interface/factions/faction_logos/005_soviet_collapse/`. No placeholder, duplicate, or fallback icon is used.

## Balance and AI

Founding uses the shared `soviet_collapse_regional_faction` script constants and the established medium AI baseline. Black Banner endgame pressure, socialist route depth, and depot route depth provide urgent AI modifiers for their matching blocs. Recruitment and all later faction actions retain the existing dynamic costs, cooldowns, shared goals, and Moscow-pressure effects, so the new founders participate in the same balance surface as the Baltic, Caucasus, and Central Asian leagues.

## Future plans

No future implementation is required for the accepted Successor Relations scope. Optional later narrative work could add bloc-specific follow-up flavor after repeated common-goal successes, but it must consume the completed shared lifecycle and must not introduce a second faction-management framework. This suggestion is not an accepted or queued Event 005 blocker.
