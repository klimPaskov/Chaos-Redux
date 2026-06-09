# The World in Fury Triggerable Scenario Specification

## Core promise

`The World in Fury` is a custom triggerable scenario that starts the Fury system at a larger scale. Instead of waiting for one random AI minor to become Fury through the normal repeatable event pool, the scenario turns several valid AI minor countries into Fury countries at the start of the scenario action.

The scenario should feel like the world has several local wars ignite at once. It should not replace the normal Fury event. It should use the same Fury country package, target rules, weekly reinforcement logic, focus tree, decisions, ideas, integration tools, and cleanup rules where possible.

The player must never become a Fury country. This is true at every intensity level and for every Fury type. If the scenario needs more candidates, it must select fewer Fury countries instead of filling the count with a player or player-owned country.

## Design boundaries

This scenario is larger than a normal Fury ignition, but it should still be understandable. It does not need a new country type, a new world-end system, or a separate Fury tree. It is a setup wrapper around the Event 007 Fury mechanics.

The scenario should add these things only:

- scenario setup logic
- intensity-based Fury country count
- intensity-based starting unit strength
- Fury type selection
- scenario-specific opening report
- scenario-specific safeguards and cleanup
- documentation and UI text for the triggerable scenario

## Hard rules

1. The player must never become Fury.
2. Player-controlled countries must never be used to fill the Fury count.
3. Player subjects should be excluded unless the implementation has a clear safe reason not to.
4. The scenario must select dynamic countries from the current campaign, not a hardcoded list.
5. Selected countries must be AI-controlled minors.
6. Selected countries should be non-island candidates with valid land expansion options.
7. Selected countries should have few states, with one-state minors strongly preferred.
8. The scenario must not overwrite special chaos countries or scripted crisis countries that should not receive ordinary Fury logic.
9. If there are not enough valid candidates for the selected intensity, the scenario uses every valid candidate it can find and records the reduced count.
10. The scenario must not spawn invalid wars to satisfy intensity.
11. The normal repeatable Fury event can still exist after the scenario.

## Scenario setup settings

### Intensity slider

All triggerable scenarios have an intensity slider. For this scenario, intensity controls two things:

- how many AI minors become Fury countries
- how strong their starting units and first reinforcement waves are

Intensity should not only add flat divisions. It should also affect the quality of those divisions, the first-war preparation delay, and the opening reserve package.

Recommended intensity table:

| Intensity | Fury country target | Starting force direction | First reinforcement direction | War tempo direction |
| --- | --- | --- | --- | --- |
| Low | 2 Fury countries | small militia-heavy package | weak weekly pulse | slower first wars |
| Standard | 4 Fury countries | mixed militia and regular package | normal weekly pulse | normal first-war delay |
| High | 7 Fury countries | stronger regular package | stronger weekly pulse | shorter first-war delay |
| Maximum | at least 10 Fury countries when 10 valid candidates exist | strong opening package | strong weekly pulse plus early reserve | fast opening wars |

Maximum intensity must mean at least 10 AI minors become Fury if the valid pool contains at least 10 candidates. If the valid pool has fewer than 10 candidates, the scenario must not select the player or invalid countries to reach the number. It should use all valid candidates and report that the valid candidate pool limited the setup.

### Fury type selector

The Fury type selector controls how selected Fury countries relate to each other at scenario start.

Recommended setting values:

| Setting value | Meaning |
| --- | --- |
| Fury Pact | Selected Fury countries begin as a coordinated bloc. They do not target each other and should use cooperation mechanics from the beginning. |
| Every Border Is Prey | Selected Fury countries begin without a pact. They are hostile to normal countries and can become hostile to other Fury countries when borders meet. |

The selector should be visible in the scenario UI beside the intensity setting. It should have short explanatory text so the player understands the difference before triggering the scenario.

## Candidate selection

The scenario should use the Event 007 Fury candidate rules as its baseline.

Required candidate rules:

- AI-controlled
- minor country
- not the player
- not a player-controlled tag in multiplayer
- not a player subject or player faction member if this would indirectly gift the player a Fury ally
- owns few states
- one-state countries receive the highest weight
- has at least one valid AI land neighbor
- not already Fury
- not a special chaos country excluded from ordinary Fury logic
- not protected by another event's active scripted state
- not in a blocked scripted peace or forced transition
- not a country whose existing package would be broken by runtime Fury focus loading

Preferred selection behavior:

- spread Fury countries across regions when possible
- avoid selecting ten countries in the same small area unless the valid pool forces it
- avoid selecting neighbors that would instantly fight each other in Pact mode
- allow closer selection in hostile mode because Fury-on-Fury conflict is part of that variant
- avoid selecting countries already stuck in severe wars unless high intensity allows riskier starts

The selection should be weighted, not fixed. A one-state AI minor with several weaker AI land neighbors should be a strong candidate. A minor inside a major faction, a subject web, or a player-adjacent dead end should be weak or invalid.

## Candidate spread model

`The World in Fury` should feel global when the campaign map allows it. The selection should try to spread Fury countries across continents or large regions.

Suggested spread rules:

1. Build a full valid candidate pool.
2. Split candidates into broad regions or continents using existing map region logic where possible.
3. Select at least one candidate per region while the intensity target and candidate pool allow it.
4. After every eligible region has one Fury country or no candidates left, fill remaining slots by weighted score.
5. In Pact mode, avoid selecting direct neighbors unless the scenario is at maximum intensity or the valid pool is too small.
6. In hostile mode, allow neighboring Fury selections because early Fury rival wars are allowed.

The region spread model should remain a preference. It should not force invalid tags or create hardcoded country lists.

## Fury type behavior

### Fury Pact

`Fury Pact` starts the selected Fury countries as a coordinated bloc.

Gameplay role:

- stronger united threat
- less Fury-on-Fury waste
- cooperation mechanics available immediately
- shared military confidence from the start
- clearer world threat identity

Setup effects:

- create or reuse the Fury Pact faction if the implementation has a safe faction helper
- add selected Fury countries to the pact
- prevent selected Fury countries from targeting each other while pact mode is active
- enable Fury coordination value from the beginning
- unlock cooperation decisions and the cooperation focus route without falsely logging Evolution II as having occurred
- give a small pact cohesion value or equivalent if the implementation supports it

War behavior:

- each Fury country picks non-Fury AI land neighbors first
- target deconfliction should prevent two pact members from repeatedly selecting the same small target when another valid target exists
- pact members can receive shared reserve help, but not enough to become free unit farms
- pact members should not be able to call every pact member into every tiny border war by default unless high intensity or later focus progress unlocks wider war calls

Failure and cleanup:

- if a pact member capitulates, remove that member from active Fury coordination
- if too many pact members die, pact cohesion drops or the pact becomes only a loose label
- if only one pact member remains, cooperation decisions hide or convert into solo consolidation decisions

### Every Border Is Prey

`Every Border Is Prey` starts the selected Fury countries without a shared pact.

Gameplay role:

- more chaotic map
- more local wars
- Fury countries can collide with each other
- weaker single global threat than Pact mode, but harder to predict

Setup effects:

- no common Fury Pact faction at scenario start
- each Fury country receives hostile posture against nearby non-Fury AI countries
- Fury countries do not receive cooperation decisions at the start
- cooperation focus routes are hidden or unavailable unless a later event explicitly creates a pact
- direct opinion penalties between Fury countries are allowed if useful for target logic

War behavior:

- first-wave scripted wars should still prefer non-Fury AI minors
- after the first wave or after borders touch, Fury countries can target other Fury countries if they are valid neighbors
- high intensity can shorten the delay before Fury-on-Fury wars become valid
- no Fury country should receive free coordination bonuses from another Fury country in this mode

Failure and cleanup:

- defeated Fury countries clean up individually
- another Fury country that conquers a Fury country may receive a special momentum reward, but it should also inherit occupation strain
- hostile mode should not create a hidden pact through focus or decision rewards unless a later route explicitly changes the scenario state

## Starting force model

The scenario should use the normal Fury unit package system with intensity multipliers.

Starting force should be dynamic and based on:

- intensity slider
- candidate state count
- candidate manpower
- candidate industry
- candidate existing army size
- local supply
- chaos value if available
- Fury type
- whether the country starts near several valid targets

Recommended force direction:

| Intensity | Immediate divisions | Quality direction | Reserve timing |
| --- | --- | --- | --- |
| Low | small package, roughly 3 to 5 divisions for a one-state country | militia-heavy | no early reserve unless first war stalls |
| Standard | moderate package, roughly 5 to 8 divisions | mixed militia and regulars | small reserve after first declaration |
| High | strong package, roughly 8 to 12 divisions | more regulars and support elements | reserve wave within the first two weeks |
| Maximum | strong package, roughly 10 to 16 divisions where supply allows | best Fury templates available before evolutions | early reserve wave plus stronger weekly pulse |

The exact implementation values should live in script constants or the project tuning file. The spec values are balance targets, not hardcoded script instructions.

Unit templates should still fit the Fury country scale. A one-state minor should not spawn a modern great-power army. At maximum intensity, the threat comes from many Fury countries and stronger tempo, not from one tiny country receiving impossible elite armies.

Recommended template families:

- Border Militias
- March Battalions
- Depot Guards
- Shock Detachments
- Command Reserve Columns

Maximum intensity can use better versions of these templates, but it should not bypass equipment, manpower, supply, or occupation strain limits.

## Opening war timing

The scenario should avoid one giant same-day declaration wave.

Recommended timing:

- selected Fury countries receive their package immediately
- first-wave target selection happens quickly, but not all on the same exact day
- declarations are staggered across a short setup window
- intensity shortens the window
- hostile mode can create more overlap than Pact mode
- maximum intensity can be aggressive, but still should not create avoidable script spikes

Suggested direction:

| Intensity | First declaration window |
| --- | --- |
| Low | several days after setup |
| Standard | short delay |
| High | very short staggered delay |
| Maximum | fastest staggered delay that remains safe |

The event text should describe sudden border mobilizations before full declarations begin.

## Interaction with normal Fury evolutions

The triggerable scenario should not falsely record ordinary setup choices as evolutions.

Important distinction:

- intensity is a scenario setting
- Fury type is a scenario setting
- Event 007 evolutions are mutation tracks inside the Fury event identity

Pact mode may unlock cooperation mechanics from the beginning, but that should not automatically count as Evolution II unless the implementation deliberately treats the scenario as starting at that evolution. The safer design is to use scenario flags such as `fury_scenario_pact_mode` and `fury_scenario_hostile_mode`, then let normal evolution logging remain separate.

Maximum intensity can make Evolution I or II more likely later, but the scenario setup itself should remain a triggerable scenario state.

## Focus tree interaction

Every selected Fury country should receive the same runtime Fury tree or additive Fury branch used by the normal event.

Scenario-specific focus handling:

- Pact mode unlocks or reveals cooperation branches from the start
- Hostile mode hides cooperation branches and may reveal rivalry or all-border pressure focuses
- maximum intensity can reveal stronger opening military focuses earlier
- scenario starts should use a scenario origin flag so the focus tree can show correct localisation
- existing meaningful focus trees should not be blindly overwritten unless the Fury implementation already uses a safe runtime tree loading pattern

Possible scenario-origin focus names:

- The World Has Already Broken
- Ten Sparks at Once
- Pact Orders Circulated
- Every Border Is Prey
- No Safe Minor State

These are focus direction names, not mandatory exact focus ids.

## Decision and mission interaction

The scenario should use the normal Fury decision category with scenario-aware header text.

Scenario-specific decision behavior:

- intensity should increase starting reinforcement options
- Pact mode enables shared reserve and target deconfliction decisions
- Hostile mode enables rival border pressure decisions when Fury countries border each other
- integration and coring decisions remain staged
- no decision should let a player become Fury or claim Fury rewards
- no decision should become a free unit loop because several Fury countries exist at once

Useful scenario decision families:

| Decision family | Mode | Role |
| --- | --- | --- |
| Coordinate First Campaigns | Pact | stagger or deconflict first targets |
| Shared March Reserves | Pact | limited partner support with equipment cost |
| Mark Rival Fury Border | Hostile | prepare for Fury-on-Fury conflict after borders meet |
| Consume the Weak Frontier | Any | faster first-war preparation at higher intensity |
| Stabilize the First Conquests | Any | reduce occupation strain after early victories |

## Event log and scenario report

The scenario should receive a clear event log entry separate from ordinary Fury random fires.

Recommended report event:

- title direction: `The World in Fury`
- role: scenario opening report
- timing: after selected countries receive Fury packages, before or during the first declaration window
- content direction: multiple small governments have entered rapid military mobilization, foreign observers disagree on whether this is coordination or collapse, border commands report unusual troop movements

The report should show:

- number of Fury countries selected
- selected Fury type
- intensity label
- reduced-count warning if not enough valid AI minors existed

It should not show raw implementation values. It should explain the visible campaign state.

## Player handling

The player is excluded from becoming Fury in all cases.

The scenario should also avoid using player countries as filler targets during setup. If a Fury country borders only the player and no valid AI target, that Fury candidate should usually be rejected from initial selection.

After the scenario begins, later player involvement depends on the normal Fury event rules and broader campaign state. The scenario should not create a day-one player dogpile through setup logic. If a later world-end or high-chaos branch allows Fury to threaten the player directly, that should be handled by the main Fury spec and clearly documented there.

## Multiplayer handling

In multiplayer, every human-controlled country must be excluded from Fury selection.

Candidate selection should also avoid selecting direct subjects of human players or countries whose transformation would instantly gift a human player a powerful ally.

Scenario UI text should not imply that only one player is protected. The wording should say player-controlled countries are excluded.

## AI behavior

### Fury AI

Fury AI should:

- choose first targets quickly
- prefer weaker AI land neighbors
- avoid impossible naval expansion
- use reinforcement decisions according to intensity
- use integration decisions when occupation strain grows
- use pact coordination in Pact mode
- ignore cooperation routes in hostile mode
- not repeatedly target the same country from several pact members when other valid targets exist

### Non-Fury AI

Nearby AI countries should:

- increase defensive awareness when bordering Fury
- consider guarantees or containment if they are regional powers
- avoid suicidal attacks unless already threatened
- react more strongly at high and maximum intensity
- treat Pact mode as a larger strategic threat
- treat hostile mode as a chaotic local threat that may burn itself out

### Major AI countries

Major powers should not instantly solve the scenario by guaranteeing every minor on day one. Their reaction should scale with:

- intensity
- number of first victories
- proximity
- faction interests
- ideology
- existing wars
- world tension
- chaos value

Pact mode should produce stronger containment interest than hostile mode because it creates a coordinated threat.

## Balance and exploit controls

The scenario must prevent these problems:

| Risk | Required control |
| --- | --- |
| Player becomes Fury | hard exclusion from candidate pool |
| Player gets Fury ally through subject or faction | exclude player subjects and close player faction members |
| Max intensity uses invalid tags | use fewer Fury countries and report reduced count |
| Same-day performance spike | stagger first declarations and reserve waves |
| Tiny minors become impossible superpowers | scale units by supply, manpower, industry, and intensity |
| Pact mode creates global free-war blob instantly | do not auto-call every pact member into every tiny war by default |
| Hostile mode secretly cooperates | keep cooperation branches hidden unless later route changes it |
| Coring becomes free | keep staged compliance and coring costs from main Fury system |
| Multiple Fury countries farm units | tie weekly units to active Fury state, war state, supply, manpower, and equipment strain |
| Scenario setup logs as normal repeatable event fire | record scenario setup separately from ordinary random Fury fire |

## UI and localisation direction

Scenario title:

`The World in Fury`

Scenario description direction:

Several minor states enter sudden military mobilization at once. Border commands move before diplomats can explain what is happening. Some governments appear to coordinate. Others prepare to devour anything near them.

Intensity label:

`Fury Intensity`

Intensity tooltip direction:

Controls how many AI minor countries become Fury countries and how strong their starting forces are. Player-controlled countries are never selected.

Fury type label:

`Fury Type`

Pact option name:

`Fury Pact`

Pact option tooltip direction:

Fury countries begin as a coordinated bloc. They avoid fighting each other and can use cooperation mechanics from the beginning.

Hostile option name:

`Every Border Is Prey`

Hostile option tooltip direction:

Fury countries begin without a pact. They can clash with normal countries and, once borders meet, with each other.

Reduced candidate warning direction:

The selected intensity requested more Fury countries than the valid AI minor pool could safely provide. The scenario used every valid non-player candidate instead.

## Documentation needs

Update or create scenario documentation that explains:

- scenario name
- how it relates to Event 007 Fury
- intensity slider behavior
- Fury type behavior
- player exclusion rules
- candidate selection rules
- maximum intensity target of at least 10 Fury countries when valid candidates exist
- reduced-candidate behavior
- startup report
- AI behavior
- known balance safeguards

The main Fury event documentation should mention that `The World in Fury` exists as a triggerable setup scenario, but the detailed scenario behavior should live in this spec or a scenario documentation page.

## Implementation acceptance criteria

The implementation is acceptable only when:

1. `The World in Fury` appears as a custom triggerable scenario.
2. The scenario has an intensity slider.
3. The intensity slider controls both Fury country count and starting unit strength.
4. Maximum intensity creates at least 10 Fury countries when at least 10 valid AI minor candidates exist.
5. The player is never selected as Fury.
6. Human-controlled countries in multiplayer are never selected as Fury.
7. The scenario has a Fury type selector.
8. `Fury Pact` mode creates coordinated Fury behavior from the start.
9. `Every Border Is Prey` mode starts Fury countries without a pact and allows Fury rivalry when valid.
10. Candidate selection is dynamic and weighted, not hardcoded.
11. Invalid or protected countries are excluded.
12. If the valid pool is too small, the scenario selects fewer countries and reports the reduced count.
13. Starting units scale by intensity and country context.
14. First declarations are staggered enough to avoid unnecessary script spikes.
15. Scenario setup does not falsely log ordinary Fury evolutions.
16. Fury focus tree and decisions react to scenario mode.
17. The scenario has clear UI localisation and tooltips.
18. Scenario report or event log entry records intensity, Fury type, and selected count.
19. Balance controls prevent free unit farming, free coring, player empowerment, and invalid target spam.
20. Documentation is updated with final behavior and any simplifications.

## Coding prompt addition

Add this to the Event 007 Fury implementation prompt:

Implement the custom triggerable scenario `The World in Fury` from `docs/specs/007_fury_specs/007_fury_triggerable_scenario_spec.md`. It must use the shared Fury mechanics instead of duplicating the event. Add an intensity slider that controls Fury country count and starting force strength. At maximum intensity, create at least 10 Fury countries when at least 10 valid AI minor candidates exist. Never select player-controlled countries. Add a Fury type selector with `Fury Pact` and `Every Border Is Prey`. Pact mode starts coordinated Fury countries with cooperation mechanics. Hostile mode starts Fury countries without a pact and allows Fury rivalry when valid. Stagger first wars, scale units dynamically, report reduced candidate counts, update UI localisation, docs, event log or scenario report text, and completion validation.
