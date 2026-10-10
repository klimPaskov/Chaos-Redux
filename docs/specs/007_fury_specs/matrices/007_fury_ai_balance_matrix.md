# 007 Fury AI and balance matrix

## Balance goals

Fury must be strong enough for a tiny AI country to matter.
It must also have brakes.

The balance target is:

- early local shock.
- repeated regional wars if unchecked.
- major-Fury threshold only when it wins several wars.
- world-end branch only after major success and high chaos.
- no player access to Fury growth.
- no uncapped free-division loop.
- real ways for AI and player-adjacent countries to contain Fury.

## Target scoring factors

`fury_score_current_target_candidate` combines these factors, tuned in the `fury_target_score` constant block; the best score above `minimum_score` becomes the target.

| Factor | Raises target priority | Lowers target priority |
| --- | --- | --- |
| Target size | one or two states | more states |
| Target strength | few divisions, low manpower, weak industry, weaker than Fury | many divisions, large manpower, deep equipment stock, stronger than Fury |
| Target war state | already at war elsewhere | at peace |
| Target faction or status | alone | in a faction, or a major |
| Terrain and supply | open ground, adequate supply nodes | rough terrain, weak supply |
| Actor state | momentum above zero, target preparation, Evolution I or III | overextension above the high gate |
| Rivalry | a legal target also pursued by a non-allied rival, or a rival actor when rivalry targeting is open | the previous target (churn penalty) |

Player-controlled countries are scored like any other neighbour; the player link is not a score factor.
Momentum, preparation, and evolution add the same amount to every candidate, so they only widen the minimum-score gate rather than change which neighbour wins; a proposal in the README makes preparation a spent, per-war resource.

## AI route matrix

| AI situation | Preferred behavior |
| --- | --- |
| First war active | finish the target, prioritize capital and supply |
| Winning war | keep pressure, avoid unrelated wars |
| Losing war | use capped emergency reserve tools, guard capital, reduce target ambitions |
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
| Rivalry | hostile type, rival Fury nearby | cooperation route already chosen |
| No-neighbor | no valid neighbors | target exists |
| World-end | terminal eligible | chaos threshold not met or world-end disabled |

## Finite reinforcement reserve scaling

Weekly loop units must draw from a hidden finite reinforcement reserve pool.
When that pool reaches zero, free weekly spawning stops completely and the Fury actor must rely on normal recruitment, focus rewards, decision rewards, or later capped reserve setup.
Scripted weekly reserve grants are capped at 100 total divisions per Fury actor.

Suggested inputs:

- base reserve pool size by evolution; the weekly draw itself is fixed at one column.
- country size and industry.
- active war count.
- manpower and equipment reserve.
- current focus bonuses.
- scenario intensity.
- overextension penalty.
- supply penalty.
- pact aid bonus.
- terminal branch bonus.

Growth should be visible but controlled by script constants for pool sizes, draw amounts, evolution multipliers, scenario multipliers, direct reward sizing, decision cooldowns, and maximum reserve clamps.
The current implementation draws one reserve division every weekly tick while the hidden reserve remains.
Focuses and depot decisions keep their direct reinforcement-wave behavior and do not refill the weekly reserve pool.

Examples of scaling direction:

| State | Weekly result |
| --- | --- |
| Baseline, one war, low overextension | one small Fury Column every weekly tick while reserve remains |
| Hardened Fury | stronger reserve-spawned columns and a larger capped pool |
| Evolution II multi-actor opening | smaller per-actor pools because two Fury actors exist |
| Evolution III multi-front | stronger openings and capped multi-front reserve draw |
| High overextension | smaller one-time direct waves; the weekly draw is unchanged |
| Equipment shortage | columns spawn with the scaled stockpile the actor can field |
| Pact sharing active | the actual paid manpower, rifle, and support vector moves to a partner |
| Terminal branch | strong capped reserve pool with high overextension pressure |

Exploit protection:

- No event, evolution, scenario, or terminal branch may add uncapped weekly reserve.
- Focus and decision direct unit rewards must stay one-time or cooldown-gated; they must not create an uncapped weekly loop.
- Weekly spawning must check reserve remaining before creating units.
- Weekly reserve setup must use script constants and respect the 100-division reserve cap.
- Cleanup must clear reserve variables when Fury actor state ends.

## Overextension brakes

Overextension prevents Fury from becoming a pure snowball.

Current sources of strain (overextension and the derived occupation pressure):

- each registered conquered non-core state and each non-core controlled state.
- being at war, weekly.
- resistance above the failure threshold in a controlled state.
- harsh coring, rivalry, evolution, and terminal focus costs.
- a successful anti-Fury Supply Denial.

Current effects:

- the `Fury Overextension` idea at high pressure.
- smaller direct reinforcement waves.
- a target-score penalty and, above the selection gate, no `Select the Next Target` decision.
- at extreme pressure, no valid targets outside Evolution III or the world-end branch, and the occupation crisis mission.
- AI shifts to occupation decisions and coring.

Current relief:

- peace, weekly.
- registration, rail registry, and garrison capacity.
- coring and occupation focuses.
- garrison and crisis mission success.
- terminal fronts coordination.

High casualties, low supply, a stall report, and a world-end administration block were planned but are not implemented.

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

Momentum should not be permanent.
It should decay slowly when Fury is at peace and has valid targets but does not attack.

Current implementation: momentum gains a fixed amount every week regardless of results and falls only through anti-Fury mission outcomes, so the falls listed above are design intent rather than current behavior.
The README records a proposal that ties weekly momentum to territorial progress.

## Player exploit checks

| Exploit risk | Prevention |
| --- | --- |
| Player becomes Fury | random and scenario setup exclude player |
| Player farms Fury units by tag switching | achievements disqualify player-as-Fury, ordinary player path not supported |
| Player uses Fury as free ally | Fury faction membership excludes player by default |
| Fury attacks a protected player-linked puppet early | target rules exclude every subject, the actor's own faction members, and countries already at war with the Fury actor |
| Player lets Fury conquer then steals settlement | settlement avoids player-controlled or player-occupied states |
| Fury grants instant cores | coring requires decisions, compliance, control, and resources |
| Weekly units become infinite | hidden reserve pool is finite; weekly spawns consume it; weekly reserve setup is capped by the 100-division per-actor reserve limit and cleanup clears reserve state |
| Maximum-spread scenario selects majors to hit count | fallback broadens minor criteria but does not select majors unless explicitly redesigned later |
| AI declares impossible wars | target score checks faction, strength, subject status, current wars, and supply |
| World-end branch fires too early | requires major or no-neighbor success, high chaos, and focus or branch state |

## AI containment behavior

AI neighbors should react if Fury becomes threatening.

| Actor group | Response |
| --- | --- |
| Direct neighbor | border watch, defense weighting, aid requests |
| Regional power | emergency aid to target and guarantees when the diplomatic state allows it |
| Major power | staff talks after major-Fury threshold, aid if Fury near interests |
| Fury target | capital defense and emergency mobilization |
| Fury pact member | share reserves with a weaker partner once sharing is open |
| Hostile Fury actor | opportunistic rivalry after ordinary targets exhausted |

AI should not take anti-Fury decisions when Fury is weak and far away.

## Difficulty and chaos scaling

Chaos should affect intensity and probability, not act as a simple wall.

| Chaos state | Fury behavior |
| --- | --- |
| Low | rare, one Fury, weak opening |
| Medium | ordinary Fury, first conquest more possible |
| High | Evolution I and II more likely |
| Very high | multiple Fury actors and stronger capped reserve-spawned units |
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
| Player-controlled neighbor | can be targeted only when normal target gates allow it |
| Fury wins first war | news fires and settlement runs |
| Fury loses first war | cleanup runs and no reserve-spawned units remain |
| Evolution I active | stronger reserve-spawned units and hardened branch unlock |
| Evolution II active | second Fury can spawn and pact or rivalry branch unlocks |
| Evolution III active | three Fury actors and all-neighbor declarations are available |
| Maximum scenario | up to sixteen dispersed Fury actors are created when enough safe candidates exist |
| World-end branch | other continents get Fury actors that join main Fury faction |
