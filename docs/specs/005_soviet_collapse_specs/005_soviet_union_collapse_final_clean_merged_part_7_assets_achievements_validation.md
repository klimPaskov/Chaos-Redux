# Soviet Union Collapse Final Clean Merged Specification, Part 7
# Assets, Achievements, Super-Events, Validation, and Final Reporting

## Asset policy

Reuse existing assets only when they are valid, correctly placed, correctly sized, wired, documented, and suitable for the route identity.

Create or source new assets when existing assets are missing, broken, generic, duplicated, wrongly oriented, wrong size, unwired, undocumented, or unsuitable.

Historical flags and real leader portraits must be sourced. Fictional leaders, symbolic councils, high-chaos authorities, factory portraits, cult portraits, and invented icons may be generated.

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

`docs/assets/005_soviet_union_collapse/manifest.md`

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

The implementation must run or document these scenarios:

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

The final completion report must include:

1. Source files read
2. Files changed
3. Implementation ledger path
4. Country package coverage
5. Republic and internal republic coverage
6. High-chaos splinter coverage
7. Focus tree rewrite summary
8. Route coverage table for every major focus tree
9. Unique focus icon coverage
10. Remove-idea tooltip cleanup
11. Mission cleanup summary
12. Mission clarity fixes
13. Threat and balance summary
14. Exploit check summary
15. MTTH release summary
16. Influence system summary
17. League and faction implementation summary
18. Union Unmade release and war logic
19. Puppet release aftermath
20. Super-event cleanup
21. News and report events
22. Asset coverage
23. Achievement implementation
24. AI behavior
25. Validation scenario results
26. Simplifications and deviations
27. Blockers
28. Remaining work

If any section is missing, the goal is incomplete.

## Final acceptance

The implementation is complete only when:

- every required source spec is represented in the clean implementation
- every required country has a package row
- every high-chaos splinter has a package row
- every focus tree has required branch families
- every focus has a unique icon assignment
- focus names, descriptions, rewards, and icons match
- repeated remove-idea tooltip spam is gone
- missions are clear and non-duplicate
- threat balance passes calm strong USSR scenarios
- Union Unmade releases all required republics and subjects
- all released republics get dynamic units
- local leagues obey member requirements
- factions have goals and rules
- super-event scope is corrected
- assets are wired and documented
- achievements exist
- AI behavior is updated
- docs and ledgers prove the work

If any of these are missing, the agent must say the goal is not complete.
