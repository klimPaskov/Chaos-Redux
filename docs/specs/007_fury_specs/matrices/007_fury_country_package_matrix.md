# 007 Fury dynamic country package matrix

Fury transforms an existing AI minor. It does not require a new hardcoded country tag for the baseline.

## Package overview

| Surface | Design |
| --- | --- |
| Tag | existing country tag selected dynamically |
| Player status | player cannot be selected |
| Country name | base country name can remain at first |
| Cosmetic identity | optional route names through ideas and event text, not required for every country |
| Flag | base country flag remains by default |
| Faction emblem | shared Fury faction emblem if cooperation or world-end branch forms |
| Leader | current leader remains unless War Directorate route replaces them |
| Optional leader replacement | `The War Directorate`, fictional institutional leader |
| Focus tree | shared Fury tree loaded for Fury actor |
| Decisions | Fury War Office category |
| Ideas | National Fury and route upgrades |
| Units | dynamic starting units and finite reserve-spawned reinforcements |
| Cores | gained through decisions after compliance and control |
| AI | aggressive expansion AI with target safety rules |
| Event log actor | selected Fury country |

## Dynamic identity rules

Fury is meant to work on many countries. Avoid country-specific hardcoding in the first implementation.

Visible identity should come from:

- `National Fury` spirit.
- Fury focus tree.
- Fury decision category.
- news event naming the country.
- event log actor.
- optional Fury faction name.
- optional institutional leader if route chooses it.

Do not create a unique flag for every possible Fury country. The event is dynamic. A generic faction emblem and shared idea icons are better than a large impossible flag set.

## Optional leader package

If the War Directorate route replaces the leader, use a fictional institutional leader.

| Field | Direction |
| --- | --- |
| Leader name | The War Directorate |
| Leader type | institutional or council |
| Portrait | generated council or war office portrait |
| Gender handling | institutional, no personal name pool |
| Traits | war-office planning, expansion AI, diplomacy penalty |
| Unlock | War Directorate focus route |
| Cleanup | if Fury defeated, leader can remain only if aftermath says the state survives as a militarized government |

The implementation may keep the original leader for simplicity if the route does not reach War Directorate. This is not a fallback. It is the baseline design.

## Starting ideas

| Idea | Applies | Role |
| --- | --- | --- |
| National Fury | all Fury actors | main package |
| Improvised Command | weak candidates | compensates tiny army, creates planning weakness |
| Fury Overextension | after conquest | administrative strain |
| Compliance Drive | after occupation branch | captured land absorption |
| Hardened Fury | Evolution I | stronger capped reserve quality and war planning |
| Fury Pact Command | pact branch | cooperation with other Fury actors |
| Rival Fury Doctrine | hostile branch | war against other Fury actors |
| World Fury | terminal branch | world-end package |

## Starting army matrix

| Situation | Divisions | Quality | Equipment | Notes |
| --- | --- | --- | --- | --- |
| Baseline ordinary | 5 to 8 | irregular infantry | rifles and limited support | enough to beat weak neighbor |
| Weak candidate | 3 to 5 | irregular infantry | lower stockpile | target selection must choose weaker target |
| Hardened opening | 8 to 12 | regularized columns | rifles, support, small artillery chance | Evolution I |
| Two Fires opening | 8 to 12 each | regularized columns | better stockpile | Evolution II or Medium scenario |
| All Borders opening | 12 or more each | storm columns | stronger stockpile | Evolution III or High and Maximum scenario |
| World-end seed | scaled by continent and intensity | evolved columns | strong but not infinite | joins main Fury faction |

## Template families

| Template | Use | Source |
| --- | --- | --- |
| Fury Column | baseline attack | starting package and finite reserve growth |
| Capital Guard | capital defense | starting package |
| Border Runner | low-supply fronts | terrain or supply branch |
| Depot Cadre | garrison and occupation | occupation branch |
| Storm Column | evolved assault | Evolution I and III |
| Pact Cadre | shared aid | cooperation branch |
| Rival Absorption Column | Fury-on-Fury winner | hostile branch reward |

Templates should be small and dynamically improved by focus progress. Avoid giant perfect units early.

## Reinforcement pathways

Fury reinforcement is finite. Every actor has a hidden reserve pool. Weekly spawns draw from that pool and stop completely at zero. Fury can still recruit normally through the base game.

Allowed reinforcement sources:

- initial army package.
- starting hidden reserve pool.
- capped focus reserve refills.
- capped decision reserve refills.
- capped conquest or depot rewards.
- capped scenario setup reserve size.
- capped evolution reserve modifiers.

No reinforcement pathway may create an uncapped weekly division loop.

Fury gains units through:

- finite weekly reserve pulse.
- opening package.
- focus rewards.
- depot decisions.
- occupation decisions.
- pact aid.
- rival absorption.
- terminal world-end seed support.

Fury should not gain units only through political power decisions.

## Country package by candidate type

| Candidate type | Package adjustment |
| --- | --- |
| One-state minor with weak industry | more opening units relative to size, lower equipment quality |
| Two or three-state minor | fewer compensating units, better logistics |
| Minor already at war | stronger capital guard, target selection avoids impossible extra war |
| Minor in faction | usually excluded, unless scenario or high evolution allows safe handling |
| Minor with custom tree | can be selected, but doc marks tree replacement as intentional Fury takeover |
| New release from another event | valid only after cooldown and if not protected by parent event logic |
| Special chaos country | excluded unless future spec explicitly allows it |

## Country-local decisions

Dynamic Fury does not need country-specific decisions. Decisions use dynamic target, state group, and continent logic.

Country-local flavor can appear later through scripted localisation:

- country name in news.
- continent name in no-neighbor branch.
- target name in first-conquest news.
- capital state in mission text.
- border region in Border Watch mission.

## Faction package

If pact or world-end branch creates a faction:

| Surface | Direction |
| --- | --- |
| Faction name | Fury Pact or The World in Fury |
| Faction leader | strongest or first major Fury actor |
| Members | active Fury actors in pact mode or world-end seed |
| Emblem | generated faction emblem, no readable text |
| Mechanics | Fury Pact Cohesion, shared aid, partition |
| AI | coordinate target choice and support weaker members |
| Cleanup | dissolve if fewer than two Fury actors remain unless world-end says otherwise |

## Compatibility notes

- Fury should not replace systems for non-human or special chaos countries.
- Player countries cannot become Fury through ordinary selection or scenario setup, but they can become Fury targets when they pass the same normal target gates as any other neighbor.
- Fury should not steal player-occupied states during settlement.
- Fury should not load its tree on a player country through normal selection.
- If another event creates a small AI country, that country can later become Fury after cooldown if safe.
