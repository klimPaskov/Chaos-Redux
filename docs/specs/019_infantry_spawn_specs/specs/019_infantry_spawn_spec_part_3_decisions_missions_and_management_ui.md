# Event 019 Infantry Spawn spec part 3, decisions, missions, and management UI

This file defines the decision and UI design. It uses working labels only.

## Decision category lifecycle

The event begins without a permanent category at baseline. A short-lived category can appear for a country that receives a large wave, but the permanent management layer begins at Evolution II.

| Phase | Category behavior |
| --- | --- |
| Baseline | Optional short cleanup decisions appear only for countries with large waves or high strain |
| Evolution I | Cleanup decisions are more useful, especially normalization and depot sorting |
| Evolution II | Main category appears, letting countries organize the wave and request random units on demand |
| Evolution III | Category becomes a crisis. Clean default spawns stop, and decisions become the main way to create units |
| Evolution IV | Category adds chaos unit authorization, quarantine, exorcism, binding, and splinter containment |

The category should never show every possible decision at once. It should use phases, active caps, country state, selected targets, and crisis flags. The player should see the current management problem, not a debug list of all possible spawns.

## Core visible values

The category should display values with short dynamic summaries. Each value needs consistent colour identity in final localisation.

| Value | Meaning | Rises from | Falls from | Unlocks or blocks |
| --- | --- | --- | --- | --- |
| Command coherence | Whether the army can absorb new formations | too many units, low army XP, refusing structured decisions | drills, staff integration, army XP spending | better templates, fewer revolts, stronger AI confidence |
| Supply strain | Logistics stress caused by sudden forces | many divisions, armor, motorized, low rail and trains | depot sorting, trains, trucks, logistics decisions | supply penalties, mission difficulty, unit quality |
| Roster backlog | How many formations need processing | each wave and on-demand spawn | inspection, integration, disbanding | category visibility and follow-up events |
| Formation absurdity | How random and incoherent new divisions become | reckless requests, chaos tier, failed management | inspection, template filtering, disbanding | Evolution III unit weirdness |
| Officer appetite | How much special generals demand authority | accepting demands, victories by spawned units, high chaos | refusing, purging, rotation, concessions with cost | possessed general events and revolt chance |
| Chaos leakage | How much nonstandard unit logic entered the army | chaos unit use, ghost or golem spawns, zombie training | quarantine, exorcism, containment missions | Evolution IV chaos units and splinter risk |

These values should not be hidden. The player should understand why the next spawned unit might be terrible or dangerous.

## Decision family map

| Family | Phase | Player action | Costs and requirements | Result direction | AI behavior |
| --- | --- | --- | --- | --- | --- |
| Inspect the wave | Baseline plus | Spend time and small army resources to reveal quality | army XP, command power, active backlog | lowers hidden uncertainty and unlocks better sorting | AI uses when backlog is high and at peace |
| Sort depots | Baseline plus | Use logistics to reduce supply strain | trains, trucks, support equipment, fuel, civilian burden | lowers supply strain, improves equipment fill | AI uses when supply strain is high and industry exists |
| Standardize formations | Evolution I plus | Convert weak units toward a sane template | army XP, infantry equipment, support equipment | lowers absurdity and upgrades some units | AI uses if not desperate and equipment exists |
| Absorb local officers | Evolution I plus | Bring officers into the regular chain | command power, army XP, stability risk | lowers command confusion but may raise officer appetite | AI uses cautiously in war |
| Disband the worst | Evolution I plus | Remove useless fragments without farming equipment | stability risk, manpower loss, command cost | lowers backlog and absurdity, limited recovery | AI uses for broken fragments when supply is bad |
| Request a random unit | Evolution II plus | Spawn a fully random unit on demand | escalating army XP, equipment, manpower, supply strain, cooldown | can produce anything from one battalion to a strong unit | AI uses only under war pressure or severe weakness |
| Emergency front muster | Evolution II plus | Target a front or border region for units | war state, divisions at front, equipment, command power | more useful units, higher strain | AI uses if losing fronts |
| Capital defense muster | Evolution II plus | Target capital and adjacent area | control capital, manpower, infantry equipment | defensive units with lower weirdness | AI uses if capital threatened |
| Depot lottery | Evolution II plus | Trade logistics order for chance of heavy units | trains, trucks, fuel, support equipment | tanks, motorized, armored cars, or nonsense | AI rare unless industrial and at war |
| Ban further musters | Evolution II plus | Shut down on-demand spawning for a time | political cost, stability, army resentment | lowers future risk, blocks some decisions | AI uses if supply and command are collapsing |
| Empower a general | Evolution III plus | Grant a possessed or strange general more control | command power, army XP, political risk | immediate units or buffs, higher appetite | AI rare, higher for desperate countries |
| Rotate the general staff | Evolution III plus | Reduce one general's grip | command power, stability, officer resistance | lowers appetite, may trigger demand event | AI uses if appetite near revolt |
| Hunt illegal regiments | Evolution III plus | Find units forming outside command | manpower, equipment, stability, military police style costs | reduces revolt pool, may cause clashes | AI uses if not in immediate collapse |
| Quarantine chaos units | Evolution IV | Restrict supernatural units and training | command power, supply, stability, support equipment | lowers chaos leakage, may weaken chaos units | AI uses often if at peace or stable |
| Authorize base zombie training | Evolution IV | Unlock base zombie training only | chaos leakage threshold, harsh political and medical costs | allows base zombie units, raises splinter risk | AI almost never except desperation or high chaos |
| Bind golem cadres | Evolution IV | Use spawned golems under control | equipment, support equipment, construction burden | strong defensive units, high supply and autonomy risk | AI rare, defensive states prefer it |
| Exorcise ghost companies | Evolution IV | Remove or weaken ghost divisions | stability, army XP, support equipment, religious or security flavor | lowers ghost splinter risk, may lose units | AI uses when leakage is high |
| Contain a splinter | Evolution IV | Respond to emerging breakaway | units in area, equipment, command power, stability | delays or weakens revolt | AI uses when threat is nearby |

## Timed missions

Timed missions should create real objectives rather than passive checks.

| Mission working label | Trigger | Objective direction | Duration band | Success | Failure |
| --- | --- | --- | --- | --- | --- |
| Guard the depots | supply_strain high | Place supplied divisions near key rail or depot states | medium | lowers supply strain and depot disorder | raises depot disorder and weakens future equipment fill |
| Register the regiments | roster_backlog high | Keep army XP or command coherence above target while no new on-demand spawns happen | medium | lowers backlog and absurdity | raises officer appetite and command confusion |
| Hold the capital rails | capital threatened or low supply | Keep capital connected and controlled | medium to hard | safer capital defense units | harsh supply strain and panic |
| Break the rogue drill field | Evolution III illegal regiments found | Control named state and keep loyal divisions there | medium | removes part of revolt pool | creates local uprising or general demand |
| Seal the strange barracks | Evolution IV chaos leakage high | Place units in selected state and pay support equipment | medium | lowers chaos leakage | can spawn chaos units or splinter seed |

Mission target locations should be named through scripted localisation. Do not expose raw state lists.

## Follow-up flavor events with real effects

Flavor events should not be cosmetic. They should alter values, launch missions, or change decision costs.

| Event family | Direction | Mechanical consequence |
| --- | --- | --- |
| Rushed conscription | Crowds and local authorities are pulled into sudden unit registration | manpower shifts, stability pressure, training dilution |
| Poor coordination | Units receive conflicting orders and crowd rail lines | supply strain, command confusion, mission spawn |
| Depot discovery | Equipment appears in places the army cannot explain | chance to improve equipment fill or raise absurdity |
| Counterfeit ranks | Officers appear with real insignia and false paper trails | officer appetite, demand chain seed |
| Town square drill | Civilians drill as if ordered by someone else | local support risk, militia spawn, panic |
| Frontline miracle | Desperate country receives useful units where needed | strong units with future officer appetite |
| Barracks rumor | Soldiers describe a general who has not reported for duty | possessed general chain seed |
| Hospital alarm | Strange units need food, medical storage, or containment | stability, support equipment, chaos leakage |

The event family should vary by ideology, war state, country size, and evolution. Final text should stay in-world and avoid explaining hidden variables.

## Custom UI and animated presentation

The decision category should start as a normal category, but Evolution III and IV justify an attached scripted GUI or compact custom panel if implementation capacity allows.

Suggested UI working label: Muster Ledger.

The UI should show:

- current values with concise labels
- three current action lanes, Order, Demand, and Containment
- one selected target area when a mission or revolt seed exists
- a recent formation card showing the last spawned unit's quality class
- warning state when officer appetite or chaos leakage approaches revolt
- a lock state when the country bans further musters

Animation planning pass:

| Asset | State logic | Target surface | Animation direction | Static fallback |
| --- | --- | --- | --- | --- |
| Muster category seal | active category, higher glow with strain | decision category header or GUI | slow stamped-paper flicker, not a filter-only pulse | static stamped seal |
| Command coherence meter | safe, strained, collapsing | scripted GUI | frame variants for stable, rattled, and cracked meter frame | static meter frame |
| Officer demand warning | appetite near revolt | scripted GUI warning card | eye-like glint or twitching insignia from real source frames | static warning icon |
| Chaos leakage warning | Evolution IV leakage high | scripted GUI warning card | drifting particles or dim supernatural seepage from separate frames | static warning icon |
| Random unit button glow | decision available and not on cooldown | scripted GUI button | subtle activation state from planned frames | static available button |

Animations are optional for the first implementation only if the implementation report records why static presentation is clearer. If animated assets are created, they must follow the frame-animation skill with real source frames, sheet DDS, static fallback, GIF preview for review, and GFX handoff.

## Cost and balance style

The decision system should avoid political power as the main cost. Political power may appear when the action is a public decree or political concession. Most actions should use army XP, command power, infantry equipment, support equipment, artillery, trucks, trains, fuel, manpower, stability, war support, supply strain, local state control, and time.

Costs must be dynamic. A tiny country should not pay the same support equipment and trains as a major. A country at war should pay more command and supply pressure. A country with high roster_backlog should pay more to standardize and less to disband.

Command power costs should remain conservative. Expensive command power decisions should add other costs rather than exceeding safe command power ranges.

## Category cleanup

The category should hide when a country has no backlog, no strain, no active missions, no general demand, no chaos leakage, and no active cooldowns. Temporary flags, target states, selected general references, mission targets, and active target decisions must be cleaned when the country is annexed, tag-switched, loses every valid state, or when the event is disabled.

If a splinter country forms, the parent should keep a containment category until the splinter is gone, pacified, or no longer directly connected to the parent's spawned units.
