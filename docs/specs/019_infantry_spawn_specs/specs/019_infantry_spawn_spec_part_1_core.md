# Event 019 Infantry Spawn spec part 1, core event design

This file is a source design document, not final localisation. Any title, branch, route, decision, focus, achievement, and asset labels in this pack are working labels. Implementation must write final player-facing text from the direction given here.

## Event identity

| Field | Design value |
| --- | --- |
| Event ID | 19 |
| Event name | Infantry Spawn |
| Type | Minor Repeatable |
| Current catalog state | To Be Reworked |
| Core fantasy | Every state suddenly receives formations that should not have appeared, and governments must decide whether to absorb, discipline, exploit, or fear them |
| Player role | Turn an unexpected army into useful force without letting supply, command, absurd templates, and strange officers break the state |
| Repeat role | Each firing should feel like another wave of irregular mobilisation, not a clean equipment grant |

The event should start as a strange but useful mobilisation shock. At low chaos, countries receive weak basic formations across much of their territory. At higher chaos, the gift becomes a management problem. The units become stronger, stranger, and less obedient. By the final evolution the event can produce supernatural unit families from other Chaos Redux systems, but those families must use a separate lesser identity and must not hijack the parent event chains that created those unit types elsewhere.

## Playable promise

The player should feel three pressures at once.

First, the country gains bodies on the map. The sudden divisions can fill quiet fronts, guard ports, and help minors survive.

Second, the new forces are messy. They can strain supply, consume equipment, add command confusion, and dilute training.

Third, the later versions of the event ask whether the country should keep asking for more. More units can solve an immediate military problem, but reckless use makes the next formation less sane, the generals more demanding, and the eventual revolt more likely.

This is not a free army event. It is a mobilisation weather system that sometimes helps and sometimes leaves a state trapped inside an army it cannot understand.

## Baseline firing flow

When the baseline event fires, every eligible country is evaluated. Most controlled states in each country can receive one division. Large countries have lower per-state density, but their total number of divisions still grows with territory. There must be no hard cap that makes large countries stop benefiting. The tradeoff is that a sprawling empire gets a thinner and worse distributed wave than a compact country.

Each country receives a hidden short-term record of the wave. The record should remember approximate number of spawned divisions, whether the country was at war, whether equipment fill was low or high, and whether the country already carried prior Infantry Spawn strain. That memory should drive follow-up events, decision availability, AI behavior, and later repeat tuning.

The event should avoid selecting invalid states, empty wastelands, demilitarized abnormal states, states controlled by nonhuman special countries where ordinary mustering would make no sense, and states that are temporary event staging areas owned by other Chaos Redux systems. When a special chaos country is meant to receive units from this event, the country package must define an explicit exception.

## Repeatable memory and campaign identity

The repeatable design should track country-level memory rather than treating every firing as clean.

| Memory value | Meaning | Gameplay use |
| --- | --- | --- |
| muster_fatigue | How much the country has been burdened by repeated waves | Raises supply strain and lowers quality if unmanaged |
| roster_backlog | How many units remain unintegrated | Unlocks organisation decisions and affects revolt risk |
| depot_disorder | How much equipment and supply sorting has failed | Raises under-equipped spawn chance and reduces reinforcement quality |
| command_confusion | How badly command channels are overloaded | Creates temporary army penalties and general demand events |
| formation_absurdity | How weird the newest formations are | Drives Evolution III random battalion outcomes |
| chaos_leakage | How much nonstandard mustering has entered ordinary recruitment | Drives Evolution IV chaos unit weights and splinter risk |
| officer_appetite | How much special generals think the army owes them authority | Drives demand chains, concessions, and revolts |

These values should decay or be reduced through decisions. They should rise from careless on-demand spawns, accepting dangerous generals, failing missions, spawning chaos units, and keeping too many unusable divisions in the field.

## Baseline stages and evolutions

Baseline stages are the ordinary repeat cycle. Evolutions are global mutation tracks that change the event across future firings and active country decision categories. Ordinary repeat waves should not be logged as evolutions.

| Layer | Working label | What changes |
| --- | --- | --- |
| Baseline | Sudden Muster | Weak formations appear across most controlled states |
| Evolution I | Organized Muster | Better equipment fill, more coherent templates, stronger support, reduced random trash |
| Evolution II | Arsenal Muster | Multiple divisions can appear in a state, mechanized and armored packages enter, weird but usable specialist units appear, decision category opens |
| Evolution III | Possessed Muster | Default clean spawns stop, the crisis becomes managed through decisions, divisions are built from random battalion and support company rolls, possessed generals can demand authority and revolt |
| Evolution IV | Chaos Muster | Registered Chaos Redux unit families can appear, trainable or spawn-only rules apply, reckless use can create weaker zombie, ghost, golem, or future chaos splinter countries |

## Evolution entry paths

Each evolution needs both active-event and pre-fire behavior.

| Evolution | Active-event evolution | Pre-fire evolved opening |
| --- | --- | --- |
| I | Existing countries with roster_backlog gain the Organized Muster decision package and a one-time chance to normalize old templates | Future firings start with stronger baseline templates and higher equipment fill |
| II | Countries with active category unlock on-demand random units, supply triage, and formal absorption decisions | Future firings can spawn more than one unit in some states and can include armor, mechanized, armored cars, helicopters, and specialist packages |
| III | Countries stop receiving ordinary clean default waves and instead receive mustering crisis pressure, possessed-general incidents, and random-battalion decisions | First firing at this evolution opens directly with a crisis category, a command confusion spirit, several randomized formations, and at least one general demand seed for large or wartime countries |
| IV | Existing crisis categories add chaos unit management, chaos quarantine, special unit authorization, and splinter containment actions | First firing can include low-weight chaos units and can immediately seed chaos_leakage if the country is at war, unstable, high chaos, or already mismanaged |

Evolution logging should use actor context when a milestone belongs to a country, such as the first possessed general demand or first chaos splinter. If the evolution is global and no country owns it, it should log without a leaked actor.

## Event cluster placement

Infantry Spawn does not fit the current Wars, Liberations, Diplomatic Panic, or Peace clusters cleanly. It should remain unclustered for the first rework pass, but the spec recommends a future cluster working label named Sudden Mobilisations if several military disruption events are grouped later.

Possible future cluster members could include Infantry Spawn, weapons appearing in stockpiles, sudden officer coups, emergency conscription shocks, and old reserve networks returning. That cluster should not be created only for this event unless another event is ready to join it.

## Connections to existing Chaos Redux systems

| Existing system or event | Connection |
| --- | --- |
| Zombie Outbreak | Evolution IV can authorize training of the base zombie unit only. It must not unlock advanced zombie variants or trigger Zombie Outbreak parent mechanics |
| Death | Evolution IV can spawn ghost divisions and a weaker ghost splinter. It must not create the Death country, use the Black Ledger, or instantly erase state population |
| Fury | Fury actors should receive special AI handling. They may use spawned units aggressively, but Infantry Spawn should not create Fury actors or advance Fury evolutions |
| War Declarations | New units can make countries more willing to fight, but the event should not directly trigger unrelated wars except through the triggerable scenario or revolts |
| Soviet Union Collapse and liberation crises | Spawned units in unstable countries can increase breakaway confidence, but they should not replace those events' release logic |
| Chaos Warfare | If chaos or chemical sub-units exist as valid land units, they must enter only through the Evolution IV registry and only when marked eligible |
| Chaos Meter | Higher chaos raises intensity, absurdity, and chaos unit weights. The event itself should add modest chaos on large uncontrolled revolts rather than on every ordinary spawn |
| Deaths system | Ghost, zombie, and chaos splinters can add deaths through slow local harm. Ordinary spawned infantry should not create deaths by appearing |
| World threat framework | A large active chaos splinter can become a lesser world-threat source distinct from parent zombie or Death sources |

## Boundary rule for terminal escalation

The event can create severe wars, mutinies, and nonhuman breakaways, but it should not set terminal campaign flags or replace parent world-end branches. The triggerable scenario is a crisis launch, not a final campaign state. Parent events keep their own world-end logic.

## Player-facing text direction

Final event details should describe the public premise. They should not list unit counts, modifiers, formulas, or hidden variables. The writing direction should focus on soldiers appearing in villages, rail yards, docks, barracks courtyards, and fields, with officers trying to identify formations that no register admits to creating.

Options should not be bland. Low chaos responses can use dry military understatement or confused bureaucracy. Higher chaos responses should feel increasingly worried, arrogant, or self-damning depending on ideology and war state. Do not invent final option lines in the spec.

## Documentation and catalog direction

The event doc should explain the baseline wave, the evolution split, the decision category, the random-battalion crisis, possessed generals, chaos units, breakaway countries, triggerable scenario, AI handling, and dynamic balance safeguards.

The spreadsheet Details field should mirror the Event Details premise, not the script effects. Evolution columns should describe actual evolution tracks, not ordinary repeat stages.
