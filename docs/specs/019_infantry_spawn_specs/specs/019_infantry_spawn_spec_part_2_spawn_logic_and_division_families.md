# Event 019 Infantry Spawn spec part 2, spawn logic and division families

This file defines the unit-generation design. It is not final code and does not define final localisation.

## State and country eligibility

Every valid country should be considered when the event fires unless the country is explicitly excluded by shared Chaos Redux classification.

A valid ordinary country can receive the event if it has at least one controlled state that can host a land division. Puppets, faction members, countries at war, countries at peace, and small minors all remain eligible. A country should not be excluded because it is weak. Weak countries are often the ones that feel this event most strongly.

State eligibility should prefer controlled land states that can plausibly host units. The implementation should use scripted state groups or filters so the selection can be audited.

| State class | Baseline handling | Later evolution handling |
| --- | --- | --- |
| Core and controlled homeland | High priority | High priority, safer template quality |
| Non-core occupied state | Medium priority | More irregulars and higher command confusion |
| Capital state | Always eligible unless unsafe | Can receive extra staff or guard units at high intensity |
| Island state | Eligible | More naval garrison, militia, bicycle, cavalry, or marines if templates exist |
| Wasteland or dead-zone state | Excluded by default | Eligible only for special chaos splinter profiles that explicitly use it |
| Active outbreak or nonhuman control zone | Excluded for ordinary spawns | Eligible only through chaos unit registry rules |
| Demilitarized or scripted staging state | Excluded unless the owning event marks it safe |

The spawned division should appear in the state it belongs to. If the state cannot safely receive a unit, the country should redirect the unit to the nearest eligible capital, supply hub, port, or owned neighboring state when a helper can find one. If not, skip the state without replacing it with a stockpile reward.

## Diminishing state density without a hard cap

The baseline should usually attempt one spawn per eligible state, but large countries must have lower per-state probability. The design goal is simple.

A compact country with three states should get close to one unit in each state. A country with fifty states should still get far more units than the compact country, but many states should receive nothing and the units should be harder to organize.

Recommended density bands for tuning:

| Controlled eligible states | Expected baseline density | Design note |
| --- | --- | --- |
| 1 to 5 | Very high | Nearly every state gets a unit |
| 6 to 15 | High | Most states get a unit |
| 16 to 35 | Medium | A large country gets many units, but visible gaps appear |
| 36 to 80 | Low medium | The total is large, but the per-state burden becomes uneven |
| 81 plus | Low | The empire gains a huge number in absolute terms, but many states are untouched |

Density should also react to war state, stability, industry, supply, and prior muster_fatigue. High stability and good rail networks make distribution cleaner. Low stability, poor supply, recent occupation, and high fatigue make the wave patchier and stranger.

## Baseline template families

Baseline units should be weak or basic. They should help but should not create elite armies.

| Family | Intended role | Composition direction | Equipment fill | Spawn weight factors |
| --- | --- | --- | --- | --- |
| Local rifle company | Emergency garrison | Small infantry template with few battalions | Low to medium | Common everywhere |
| Territorial militia | Static defense | Infantry with poor organization and no support | Low | More common in occupied or low-stability states |
| Rural cavalry screen | Mobile patrol | Cavalry with low support | Low to medium | More common in low industry, wide territory, steppe, desert, and rural countries |
| Field gun detachment | Weak line support | Infantry with a small artillery element | Low | More common for countries with industry or stockpiles |
| Support cadre | Slightly more useful | Infantry with one support company from an eligible low-tech pool | Medium | More common in capitals and at-war countries |
| Port guard | Coastal defense | Small infantry, maybe support artillery or engineers when allowed | Low to medium | More common in coastal and island states |
| Police column | Occupation control | Cavalry or infantry with suppression flavor | Low | More common in non-core controlled states |

These divisions should not grant large equipment stockpiles. The event should prefer creating under-equipped or partially equipped divisions rather than adding equipment directly. If the engine requires equipment fill, use low fill and short-term country strain to represent hidden equipment pressure.

## Evolution I template families

Evolution I makes the sudden army more organized. It should not become fully professional yet.

| Family | Upgrade from baseline | New purpose |
| --- | --- | --- |
| Mustered infantry regiment | Larger infantry formation with a clearer command structure | Basic line holding |
| Reserve cavalry regiment | Cavalry with better organization | Rapid reaction and gap filling |
| Support company regiment | Infantry with engineers, recon, logistics, maintenance, or medical support when valid | Stronger country utility |
| Artillery-backed infantry | Infantry with line or support artillery | Soft attack boost with supply cost |
| Depot guard battalion group | Defensive infantry with support | Protects supply hubs and capitals |
| Veteran odds | A small chance of better training if country is at war and has army experience | Makes wartime countries feel different |

Evolution I should reduce template trash. It should increase organization, equipment fill, and starting experience modestly. It should also open a country event direction about rushed registers, converted depots, and units with serial numbers that fit together too neatly.

## Evolution II template families

Evolution II begins creating serious armies and strange units. Some states can receive more than one division.

| Family | Composition direction | When it appears |
| --- | --- | --- |
| Serious infantry | Larger infantry, artillery, and support companies | Common for at-war countries and majors |
| Motorized column | Motorized infantry with support | Countries with fuel, trucks, industry, or high war state |
| Mechanized cadre | Mechanized units even if technology is absent | Rare, weighted by industry, war state, and high chaos |
| Tank detachment | Light, medium, or mixed armor | Rare, stronger for at-war countries and industrial countries |
| Armored car patrol | Armored cars, cavalry mix, or scout units | Weird but useful, common in large countries and occupation zones |
| Helicopter-only oddity | Very rare, intentionally absurd if the unit exists in the mod | Higher with chaos, high absurdity, and reckless decisions |
| Specialist shock group | Marines, mountaineers, paratroopers, or other special forces when available | Terrain, port, mountain, and high war state weights |
| Logistics repair column | Low combat, support-heavy | Appears where supply strain is already high |

Technology locks are loosened for this event. The event can spawn units using equipment that the country has not researched, but it should not unlock production lines unless a decision or later branch does so deliberately. The player receives the unit as a mystery, not a new industrial capability.

## Evolution III random division construction

Evolution III should no longer use ordinary default spawns. When a country chooses to raise new formations, each division is assembled from random battalion and support company rolls. The result can be lucky, usable, silly, or dangerous.

The random pool should include all base vanilla land battalion types available to the mod, plus modded base unit types when the implementation marks them as safe for this event. The pool should include infantry, cavalry, motorized, mechanized, armor, armored cars, camels, bicycles, marines, mountaineers, paratroopers, amphibious tanks, flame tanks, anti-air, anti-tank, artillery, rocket artillery, and any base support company class that is valid for a division template.

The count of battalions should be random inside a weighted envelope.

| Result class | Battalions | Support companies | Typical cause |
| --- | --- | --- | --- |
| Broken fragment | 1 to 2 | 0 | High absurdity, low command coherence, low equipment |
| Usable oddity | 3 to 6 | 0 to 2 | Normal Evolution III crisis handling |
| Serious accidental force | 7 to 12 | 1 to 4 | High army experience, at war, strong depots, lucky roll |
| Absurd machine | 13 plus | 3 plus | High chaos, high officer appetite, reckless on-demand spawns |
| Dangerous anomaly | Variable | Variable | Evolution IV registry adds chaos unit families |

Support companies should be random but bounded by compatibility. If an impossible support combination would break templates, the implementation should reroll or use a safe fallback within the random pool, not replace the entire division with a normal infantry unit.

## War state and peace state differences

Countries at war may receive stronger spawned units than countries at peace. This must be visible through unit quality and follow-up penalties.

At-war countries:

- higher chance of useful infantry, artillery, motorized, and armor
- higher equipment fill when industry and stockpiles support it
- higher command_confusion because the army is already busy
- higher supply_strain near fronts and capitals
- higher chance of officer demand events
- lower chance of harmless flavor-only follow-up

Countries at peace:

- lower strength and lower equipment fill
- more police, militia, cavalry, and training units
- more decisions to absorb or disband before crisis appears
- lower immediate revolt risk
- higher chance of public panic or political scandal if units are bizarre

Neutral countries with very low army size should be able to gain useful garrison strength, but the event must not turn them into global powers without cost.

## Temporary national effects

Spawns should create short-term national strain. The strain is the price for receiving formations.

| Effect family | Cause | Gameplay direction |
| --- | --- | --- |
| Supply strain | Many units, motorized units, armor, low rail capacity | Temporary supply consumption, slower organization, or logistics penalty |
| Command confusion | Many units, low army XP, high officer appetite | Division organization, planning, reinforce, command power, or doctrine friction |
| Training dilution | Weak country, low manpower, many broken templates | Lower division experience gain or starting training |
| Depot disorder | Under-equipped units and repeated events | Reinforcement strain and decision costs |
| Public alarm | Strange templates, peace state, high chaos | Stability or war support pressure with follow-up decisions |

The strongest temporary penalties should be avoidable or reducible. Players who spend army XP, equipment, support equipment, trains, fuel, and time should be able to organize the wave. Players who take every on-demand unit should carry lasting fatigue and revolt risk.

## Abuse prevention

The event must avoid becoming an equipment farm.

Design safeguards:

- spawned units should usually be under-equipped
- very strong units should be rare and tied to strain
- disbanding event-spawned units should not return a windfall that exceeds the burden created by the event
- decisions can convert bad units into training cadres, manpower recovery, or limited equipment recovery with cost and cooldown
- countries with high prior exploitation should get higher formation_absurdity and lower equipment fill
- on-demand spawn decisions should scale costs and risks with prior uses
- AI should not spam on-demand formations when supply, manpower, or equipment debt is dangerous

## Unit naming direction

Final unit names should vary by country culture where implementation has safe name pools. The spec does not provide final names. Direction should include local reserve, militia, depot, field regiment, emergency column, border guard, port guard, and later absurd or possessed naming pools. The weirdest names should appear only at Evolution III and IV.
