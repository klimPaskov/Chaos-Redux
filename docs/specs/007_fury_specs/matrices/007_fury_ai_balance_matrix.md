# 007 Fury AI and balance matrix

## Balance goals

Fury must be strong enough for a tiny AI country to matter. It must also have brakes.

The balance target is:

- early local shock.
- repeated regional wars if unchecked.
- major-Fury threshold only when it wins several wars.
- world-end branch only after major success and high chaos.
- no player access to Fury growth.
- no ordinary player-target declarations.
- real ways for AI and player-adjacent countries to contain Fury.

## Target scoring factors

Target score should combine several factors.

| Factor | Raises target priority | Lowers target priority |
| --- | --- | --- |
| Target divisions | few divisions | many divisions |
| Target industry | low factories | strong factories |
| Target manpower | low fielded manpower | large army reserve |
| Target war state | already stretched | at peace and ready |
| Target faction | alone | backed by major faction |
| Player link | none | player, player subject, player faction |
| Terrain | open and connected | mountains, jungle, supply gaps |
| Supply | good Fury approach | poor Fury approach |
| Fury momentum | high momentum allows harder target | low momentum restricts target |
| Fury overextension | low strain | high strain blocks target |
| Evolution | high evolution expands target set | baseline keeps target small |

## AI route matrix

| AI situation | Preferred behavior |
| --- | --- |
| First war active | finish the target, prioritize capital and supply |
| Winning war | keep pressure, avoid unrelated wars |
| Losing war | use emergency units, guard capital, reduce target ambitions |
| First conquest complete | settlement, compliance, next target |
| Overextension high | occupation branch, pause new targets, core first ring |
| No target exists | next target decision or no-neighbor path |
| Another Fury exists, pact type | cooperation branch and shared aid |
| Another Fury exists, hostile type | rivalry after ordinary targets are gone |
| Fury became major | push expansion and world-threat state, but manage overextension |
| World-end active | seed continents, coordinate main faction, accept global escalation |

## AI focus weights

| Branch | High weight when | Low weight when |
| --- | --- | --- |
| Opening trunk | always early | trunk complete |
| Army | low divisions, at war, Evolution I or III | manpower and equipment empty |
| Expansion | target valid, momentum high | overextension high or no target |
| Occupation | conquered land, resistance, overextension | no conquered land |
| Cooperation | pact type and another Fury exists | hostile type or no Fury partner |
| Rivalry | hostile type, rival Fury nearby | pact type with high cohesion |
| No-neighbor | no valid AI neighbors | target exists |
| World-end | terminal eligible | chaos threshold not met or world-end disabled |

## Weekly unit scaling

Weekly units should be dynamic.

Suggested inputs:

- base weekly unit value by evolution.
- country size and industry.
- active war count.
- manpower and equipment reserve.
- current focus bonuses.
- scenario intensity.
- overextension penalty.
- supply penalty.
- pact aid bonus.
- terminal branch bonus.

Growth should be visible but controlled.

Examples of scaling direction:

| State | Weekly result |
| --- | --- |
| Baseline, one war, low overextension | one small Fury Column most weeks |
| Hardened Fury | one stronger column and occasional extra support |
| Evolution III multi-front | two or more units, mixed quality |
| High overextension | weaker units or skipped high-quality spawns |
| Equipment shortage | understrength units or no storm units |
| Pact aid active | a limited extra unit or equipment package |
| Terminal branch | strong weekly growth with high overextension pressure |

## Overextension brakes

Overextension prevents Fury from becoming a pure snowball.

Overextension rises from:

- each conquered non-core state.
- multiple active wars.
- high casualties.
- low supply.
- harsh coring.
- Fury-on-Fury rivalry.
- terminal spread.

Overextension effects:

- slower target selection.
- weaker weekly units.
- higher resistance.
- lower stability.
- AI shifts to occupation branch.
- chance of stall report.
- blocks world-end setup if the main Fury cannot administer its continent.

Overextension falls from:

- coring.
- compliance.
- occupation branch focuses.
- garrison missions.
- rail and registry decisions.
- winning a war quickly with low casualties.

## Momentum limits

Momentum rises from:

- first conquest.
- defeated capitals.
- repeat victories.
- major threshold.
- pact cooperation.
- rival Fury defeat.

Momentum falls from:

- losing battles.
- stalled war timers.
- high casualties.
- failed target preparation.
- overextension.
- capital threatened.
- target survives border watch.

Momentum should not be permanent. It should decay slowly when Fury is at peace and has valid targets but does not attack.

## Player exploit checks

| Exploit risk | Prevention |
| --- | --- |
| Player becomes Fury | random and scenario setup exclude player |
| Player farms Fury units by tag switching | achievements disqualify player-as-Fury, ordinary player path not supported |
| Player uses Fury as free ally | Fury faction membership excludes player by default |
| Fury attacks player-linked weak puppet early | target rules exclude player subjects and player faction |
| Player lets Fury conquer then steals settlement | settlement avoids player-controlled or player-occupied states |
| Fury grants instant cores | coring requires decisions, compliance, control, and resources |
| Weekly units become infinite | overextension, equipment, manpower, and cleanup limits |
| Ten-Fury scenario selects majors to hit count | fallback broadens minor criteria but does not select majors unless explicitly redesigned later |
| AI declares impossible wars | target score checks faction, strength, player link, and supply |
| World-end branch fires too early | requires major or no-neighbor success, high chaos, and focus or branch state |

## AI containment behavior

AI neighbors should react if Fury becomes threatening.

| Actor group | Response |
| --- | --- |
| Direct neighbor | border watch, defense weighting, aid requests |
| Regional power | emergency aid to target, guarantees if not player-linked |
| Major power | staff talks after major-Fury threshold, aid if Fury near interests |
| Fury target | capital defense and emergency mobilization |
| Fury pact member | aid weaker partner if pact cohesion is high |
| Hostile Fury actor | opportunistic rivalry after ordinary targets exhausted |

AI should not take anti-Fury decisions when Fury is weak and far away.

## Difficulty and chaos scaling

Chaos should affect intensity and probability, not act as a simple wall.

| Chaos state | Fury behavior |
| --- | --- |
| Low | rare, one Fury, weak opening |
| Medium | ordinary Fury, first conquest more possible |
| High | Evolution I and II more likely |
| Very high | multiple Fury actors and stronger weekly units |
| Terminal threshold | world-end branch can become eligible after Fury success |

## Failure state balance

Fury should be beatable.

| Failure state | Balance purpose |
| --- | --- |
| Early capitulation | stops bad candidate from wasting cycles |
| Overextension stall | gives neighbors and player time to respond |
| Pact dispute | prevents multiple Fury actors from always snowballing together |
| Rival Fury war | hostile type can self-balance |
| Supply failure | tiny countries cannot ignore geography forever |
| Resistance crisis | conquest without integration slows expansion |
| Major response | once Fury becomes major, more countries notice |

## Validation scenarios for implementation

| Scenario | Expected result |
| --- | --- |
| Luxembourg-like one-state AI | can attack a weaker neighbor if one exists, player excluded |
| Uruguay-like mainland minor | can use land-neighbor logic, not treated as island |
| Pure island minor | excluded if no land neighbor exists |
| Player one-state minor | not selected |
| Player subject neighbor | not targeted in ordinary loop |
| Fury wins first war | news fires and settlement runs |
| Fury loses first war | cleanup runs and no weekly units remain |
| Evolution I active | stronger units and hardened branch unlock |
| Evolution II active | second Fury can spawn and pact or rivalry branch unlocks |
| Evolution III active | three Fury actors and all-neighbor declarations are available |
| Maximum scenario | ten Fury actors are created when enough safe candidates exist |
| World-end branch | other continents get Fury actors that join main Fury faction |
