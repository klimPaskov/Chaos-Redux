# Soviet Union Collapse Final Clean Merged Specification, Part 7
# Assets, Achievements, Super-Events, Validation, and Final Reporting

## Asset policy

Historical June 5 urgent-playability scope excluded asset and flag edits.
The [source-of-truth map](../../plans/005_soviet_collapse_plans/source_of_truth_map.md) records later bounded asset handoffs and supersedes that blanket no-flag status.
Current production scope must come from the active parent brief, while the asset requirements below remain design and validation requirements.

Reuse existing assets only when they are valid, correctly placed, correctly sized, wired, documented, and suitable for the route identity.

Create or source new assets when existing assets are missing, broken, generic, duplicated, wrongly oriented, wrong size, unwired, undocumented, or unsuitable.

Historical flags and real leader portraits require attributed sources.
Use [chaos-redux-event-assets](../../../.claude/skills/chaos-redux-event-assets/SKILL.md) for current source classification, historical-flag reconstruction, native transparency, portrait production, conversion, and manifests.
Every character portrait belongs to `chaosx_portrait_creator`.
A council, factory, cult, or high-chaos label does not by itself make a grounded person or institution fictional.

## Required asset coverage

Every visible element requires asset coverage:

- focus icons
- idea and national spirit icons
- decision icons
- decision category icons
- flags
- route flags
- ideology flags where relevant
- leader portraits
- council portraits
- factory portraits
- faction emblems
- local league emblems
- Free Republics' League emblem
- achievement icons
- news images
- report images
- super-event images
- custom UI panels and progress assets

Every focus must have a unique icon assignment. Missing focus icons are not a minor issue.

Fix upside-down flags. Check normal, medium, small, ideology variant, route, puppet, cosmetic, custom chaos, factory state, and ancient restoration flags.

Update:

`docs/assets/005_soviet_collapse/manifest.md`

This is the package's asset manifest path, matching the existing `docs/assets/005_soviet_collapse/` directory that already holds the audio sources; the older `005_soviet_union_collapse` spelling is an alias and must not create a second asset folder.
The manifest is absent in the current checkout, so asset provenance is `unresolved` and no asset coverage claim can be made from the older dated handoffs alone.

The manifest must list source mode, source path, processed PNG, final DDS, target size, sprite name, use, status, and blocker if any.

## Focus icon requirements

Focus icons must match focus content.

Examples:

- construction focuses use construction, city, engineer, factory, rail, or infrastructure motifs
- air defense focuses use anti-air, radar, airfield, or sky defense motifs
- leader route focuses use leader, council, flag, seal, or political symbol motifs
- expansion focuses use maps, borders, flags, treaties, soldiers, or regional symbols
- League focuses use compacts, conferences, linked hands, maps, rails, medical trains, or arsenals
- high-chaos focuses use distinct motifs matching the high-chaos route

Do not use generic factory or equipment icons across unrelated focuses.

## Super-event package

Keep super-events limited to major moments.

Union Unmade is required. It should represent broad irreversible Soviet authority failure and the war of successor republics.

Allowed rare high-chaos super-events:

- Black Banner Returns
- The Dead Are Citizens
- The World as One Factory
- Every Port a Council
- other rare major transformations when implemented as campaign-defining branches

Every super-event requires:

- title
- description
- button remark
- verified quote
- image
- audio file
- audio id
- audio license or source documentation
- event effect wiring
- settings-aware playback
- documentation

Do not invent quotes. Do not use undocumented audio.

## News and report events

Use news events for:

- local league formation
- internal republic release
- Komi or Karelia sovereignty
- Volga republic formation
- Far Eastern Republic revival
- Siberian Regional Authority emergence
- republics joining local leagues
- local leagues declaring war
- major foreign recognition events

Use report events for:

- MTTH release warnings
- one-member liaison offices
- failed missions
- sponsor influence changes
- puppet release aftermath
- dynamic starting unit explanations
- mission outcome reports
- balance-relevant crisis shifts

## Achievements

Achievements are required.

They must be creative and difficult. Do not create achievements that unlock simply because the event fired.

The achievement set must cover:

- Soviet containment
- negotiated union survival
- depot control
- harsh restoration
- Free Republics' League
- Ukraine League or expansion routes
- Ukraine Black Banner and Bread State routes
- Belarus switchyard and forest routes
- Kazakhstan and Alash routes
- Central Asian League or cascade
- Caucasus League or mountain settlement
- Moldova and Dniester routes
- Kronstadt, Green Army, Basmachi, Pale Railway, Dead State, Factory State, Tunguska, Northern Revenant Fleet, and ancient restoration routes
- foreign sponsor balancing
- avoiding puppet dependency
- extreme high-chaos outcomes
- full republic release and anti-Soviet war outcomes

Each achievement needs:

- id
- title
- player-facing description direction
- eligible country or route
- unlock conditions
- failure or disqualifying conditions
- visible, hidden, rare, or secret status
- difficulty tier
- icon direction
- related route, decision, focus, evolution, tag, faction, or super-event
- tracking notes

Achievement icons require 64x64 completed icon direction.

## Validation scenarios

These scenarios are documented from source review and the available offline checks; the agent does not launch the game, and live confirmation belongs to the user.
An unavailable tool limits the affected scenario's claim and does not block the surrounding work.

Cover these scenarios:

1. Calm World, strong USSR, event fired manually.
2. Calm World, strong USSR, first month.
3. Calm World, strong USSR, six months of successful Soviet missions.
4. Calm World, six months of failed Soviet missions.
5. USSR at war with Germany.
6. USSR at war with Japan.
7. High chaos opening.
8. Totalen Chaos opening.
9. one Caucasus republic free.
10. two Caucasus republics free.
11. one Central Asian republic free.
12. two Central Asian republics free.
13. Union Unmade.
14. Soviet puppet republics at Union Unmade.
15. MTTH internal republic release.
16. high-chaos splinter release.
17. Northern Revenant Fleet eligibility path.
18. factory-state eligibility path.
19. Ukraine focus routes.
20. Belarus focus routes.
21. Kazakhstan focus routes.
22. fallback tree route.
23. local league war entry.
24. Free Republics' League expansion.
25. repeated remove-idea tooltip review.
26. focus icon coverage review.
27. decision category clutter review.
28. balance exploit check.

For every scenario, document observed result, expected result, status, and blocker if any.

## Required completion report

The repository's completion and simplification rules define the general report shape, and the single implementation audit named in Part 1 carries it.
Beyond those rules, this event's report must cover the coverage items that are specific to it:

1. Country package coverage, including every republic, internal republic and high-chaos splinter
2. A route coverage table for every major focus tree, with unique focus icon coverage
3. Remove-idea tooltip cleanup and mission clarity and duplication cleanup
4. Threat balance and exploit results, including the calm strong-USSR scenarios
5. MTTH release behaviour, influence, leagues and factions
6. Union Unmade release and war logic, puppet aftermath and super-event scope
7. Asset coverage against the manifest, achievements and AI behaviour
8. Validation scenario results with their evidence limits

## Final acceptance

The Part 1 completion gate is the single acceptance list; this part adds no second one.
It is satisfied only when every required country and splinter has a package row, every focus tree has its required branch families with matching names, descriptions, rewards and unique icons, remove-idea tooltip spam is gone, missions are clear and non-duplicate, threat balance holds in the calm strong-USSR scenarios, Union Unmade releases every required republic and subject with dynamic units, local leagues obey their member requirements, factions have goals and rules, super-event scope is correct, assets are wired and documented, achievements exist, AI behaviour is updated, and the implementation audit and manifest prove the work.

If any of these are missing, the agent must say the goal is not complete.
