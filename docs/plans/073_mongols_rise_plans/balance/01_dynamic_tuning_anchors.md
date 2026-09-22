# Dynamic tuning anchors

## Status

These values are parent-authored test starting points. They have not been measured in Hearts of Iron IV. They are separated from the source specification so balancing can change them without rewriting the campaign's identity. Formula inputs are design quantities until mapped to verified game data.

All percentages in this file are percentage-point modifiers unless a multiplier is explicitly stated. Round authored rewards and costs to multiples of five. Engine indices, battalion counts, dates, and the two seven-day opening focuses are explicit structural exceptions.

## Opening entitlement

| Tier | Base cumulative cavalry divisions | Intended immediately fielded share | Separate replacement manpower anchor | Army Experience anchor |
|---|---:|---:|---:|---:|
| Baseline | 30 | 65% | 50,000 | 100 |
| Evolution I | 60 | 65% | 100,000 | 150 |
| Evolution II | 100 | 70% | 200,000 | 200 |
| Evolution III | 150 | 75% | 300,000 | 250 |

The division count responds to local opposition and campaign date through a bounded factor from 0.75 to 1.25, rounded to five divisions. Opposition uses nearby relevant forces and protecting alliances, not every division in the world. The date component responds to contemporary military scale and equipment. Do not apply full independent multipliers for every factor and accidentally multiply the total several times.

The immediate share is a staging anchor, not permission to omit the remainder. Deploy as much as safe reception permits immediately. Aim to release the rest rapidly through prepared sites. If no site is viable, keep a visible unspent entitlement and make reception a concrete problem. No unverified promise of unlimited local supply is allowed.

Use a standard initial division skeleton of eight mounted line battalions as a test anchor, with support appropriate to unlocked technology. Raider formations can be smaller and support-heavy formations larger. Final battalion counts come from equipment, frontage, speed, and supply tests. These are game formations, not literal historical ten-thousand-man tumens.

## Exact equipment accounting

For each template family, calculate personnel and equipment required by one fully equipped division from the current game definition. Multiply by the granted family count. That is the opening formation allocation.

Add a separate spare-equipment reserve equal to an initial 25%, 35%, 45%, or 55% of formation equipment at successive tiers, adjusted within a bounded range for date and initial enemy strength. Include infantry equipment, support equipment, and the actual artillery or support requirements. Add trains and trucks only to the extent required by a verified logistical plan.

Do not list an invented rifle total when the current custom unit and support requirements are not yet implemented. Fill the equipment ledger during the first military feasibility stage and test the actual stockpile after all formations spawn.

## Active upgrade example

At the unscaled anchors, an empire entering at Baseline receives a total entitlement of 30. Evolution I adds 30, Evolution II adds 40, and Evolution III adds 50. If only 12 of the initial 30 divisions survive, Evolution I still adds 30, not 48.

Freeze the division-entitlement scale factor when the restoration is accepted and use that same factor for every cumulative tier in that occurrence. A later upgrade adds the difference between those scaled cumulative totals. Current unlocked equipment can determine compatible equipment quality for newly awarded formations, but it does not recalculate or regrant old formations. Test this fixed occurrence basis at every tier boundary.

## Military modifier budget

| Contribution | Baseline | Evolution I | Evolution II | Evolution III |
|---|---:|---:|---:|---:|
| Cavalry attack anchor | +15% | +25% | +35% | +45% |
| Cavalry breakthrough anchor | +25% | +40% | +55% | +75% |
| Cavalry speed anchor | +15% | +20% | +25% | +30% |
| Cavalry static defense | -25% | -25% | -25% | -25% |
| Entrenchment factor | -50% | -50% | -50% | -50% |
| Urban attack limitation | -25% | -25% | -25% | -25% |
| Fort attack limitation | -25% | -25% | -25% | -25% |

These are desired category-scoped effects, not verified modifier keys. The local implementation must find supported scopes and measure final combined stats. A country-wide fallback that also buffs tanks violates the intent unless separately accepted.

High Momentum can add a bounded offensive contribution, initially up to another 15% attack and 20% breakthrough. Low Momentum removes that temporary contribution. Commander, support, route, and political bonuses share a reviewed total budget. Permanent defense and entrenchment weaknesses may not be erased by later focus stacking.

Terrain and supply benefits need a single reviewed source. Do not apply both a custom unit bonus and an identically described country bonus unknowingly. Cold is a weather condition, not an invented generic terrain type. The exact implementation must match the engine's supported condition.

## Momentum

Start at an initial anchor of 50 with a thirty-day preparation grace. Qualifying first-time local victories add around 5, substantial campaign settlements around 10 to 15, and severe defeats remove around 10 to 20. Scale by the achievement's importance relative to the campaign's starting situation, then cap the result.

During an active stalled war, use a weekly decay anchor of 5 after a reviewed period without qualifying progress. Equipment shortage, severed supply, and repeated failed offensives can increase the loss within a bounded range. Do not claim direct detection of individual failed attacks unless such telemetry exists.

In peace, settle gradually toward a readiness floor around 35. Completed consolidation can support a floor around 50 for a limited period when the country actually repairs reserves and routes. Peacetime decay cannot by itself trigger fragmentation.

## Authority

Start at an anchor of 50, adjusted for the accepted political settlement and starting sovereignty. Honored major obligations or a recognized succession can add 5 to 15. Broken major promises, a lost imperial center, or a severe unresolved claim can remove 10 to 20.

A warning range begins around 35. Serious defiance becomes possible around 20 when a concrete unresolved trigger exists. These are response thresholds, not automatic release commands. Route choice, the number and strength of khanates, and whether the center kept its promises determine the actual risk.

## Costs, time, and tribute

Campaign preparation begins around 50 political power and 20 command power, scaled by distance, target strength, existing preparation, and Evolution. Command power remains at or below 60. Costly support choices may use infantry or support equipment instead of another political-power purchase.

Local mission windows start around 100 days, regional windows around 150, and major construction or continental commitments around 240. Short sovereignty responses start around 15 days with adjustments for the actual crisis. Main factors are distance, terrain, war conditions, required holding period, and available access. A seven-day focus is not automatically a seven-day war.

Tribute review begins from a sixty-day interval. Equipment installments are capped by the agreement and a small feasible share of the donor's usable reserve. War and supply disruption can trigger deferral. Repeated renegotiation has a bounded cooldown that becomes longer after abuse and shorter after a genuine territorial or diplomatic change.

## Calibration priorities

Test the full army at the actual reception sites, not just its paper count. Compare a successful opening, an offensive into defended cities, an armored counterattack, a severed supply route, a long stalemate, and a post-defeat recovery at all four tiers. Tune strength and staging before increasing global bonuses to compensate for a bad spawn location.
