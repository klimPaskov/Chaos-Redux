# 012 Africa spec part 30, high-chaos and nonhuman closure

This file closes the high-chaos route planning. It preserves absurd gameplay while keeping strict boundaries against human caricature, real-world disease misuse, and uncontrolled AI use.

## Boundary principle

High chaos can be supernatural, animal, impossible, and frightening. Baseline Africa remains grounded and researched. Nonhuman and supernatural actors appear only after explicit gates. They must be written as nonhuman, supernatural, fictional, or environmental powers. They must not represent human African ethnic groups in animal costume.

## Actor classes

| Actor class | Examples | Allowed role | Forbidden framing |
| --- | --- | --- | --- |
| Nonhuman animal nation | Virunga Gorillas, Congo Chimpanzees | high-chaos nonhuman country with animal leader, animal units, forest defense | never a proxy for a human ethnicity |
| Supernatural forest actor | Deep Green Covenant, forest oracle state | impossible weather, disaster bargains, forest pressure | no tribal caricature or primitive stereotype |
| Living monument actor | Living Statues of Kush, Stone Host of Great Zimbabwe | ancient stone units, heritage gate, slow powerful defense | no living human caricature |
| Prophet disaster state | Rain Prophet State, Flood Council, Drought Oracle | abstract disaster pressure and warning missions | no real-world faith mockery |
| Fictional disease actor | Fever Without Name, River Breath, Ash Rot | fictional disease mechanics and containment | no real pathogen branding, no direct real-world bioweapon instructions |
| Coastal or river power | Red Sea Oracle, Congo River Mouth, Nile Flood Court | supernatural naval and river pressure | no ethnic animalization |

## High-chaos gates

| Gate | Requirement direction | Unlocks |
| --- | --- | --- |
| `green_door_open` | Sacred Soil route, high chaos, player choice or rare AI gate | Deep Green route |
| `nonhuman_country_revealed` | Deep Green or special route focus plus region trigger | animal or supernatural tag package |
| `disaster_pressure_active` | high-chaos focus or failed nature demand | abstract disaster pressure |
| `fictional_disease_pressure_active` | high-chaos disease route, safety gate, and world chaos threshold | fictional outbreak mechanics |
| `living_statue_host_active` | heritage route, high chaos, state group control | stone host units |
| `oracle_state_active` | coastal, river, or forest route, high chaos | prophecy missions and disaster prediction |
| `ai_high_chaos_permission` | explicit rare AI profile and chaos threshold | limited AI access |

## Disaster pressure loop

Disaster pressure should be a value that escalates through route choices, failed demands, wars, and high-chaos retaliation.

| Action | Pressure direction | Target effect direction | Blowback |
| --- | --- | --- | --- |
| Issue nature demand | small pressure rise | target chooses concession, refusal, or war | League fear rises |
| Refusal by outside power | medium pressure rise | chance of abstract disaster mission against target | unifier diplomacy worsens |
| High-chaos war action | medium to high pressure rise | recurring state penalties, supply damage, infrastructure harm | local support drops if overused |
| Oracle prediction fulfilled | lowers backlash if player warned members | member confidence may rise | rival blocs accuse manipulation |
| Uncontrolled disaster | pressure over safe threshold | affects enemies and friendly regions | route failure or containment missions |
| Disaster bargain | temporary benefit | powerful combat or attrition effects | later debt, stability hit, or disease risk |

Do not state in player text that a specific Chaos Redux natural disasters event will fire. Use in-world consequence direction and mechanic tooltips.

## Fictional disease mechanics

The high-chaos disease route should be fictional and abstract. It may integrate with Chaos Redux biological warfare, deaths, and contamination systems, but it must not provide real-world biological weapon instructions.

### Disease layers

| Layer | Meaning | Gameplay direction |
| --- | --- | --- |
| `river_breath` | fictional riverborne pressure | supply, movement, local manpower, medical missions |
| `green_fever` | fictional forest fever pressure | attrition, recovery, resistance, hospital projects |
| `ash_rot` | fictional post-disaster sickness | industry and state recovery penalty |
| `stone_lung` | supernatural dust from living-statue route | combat recovery and construction penalty near heritage zones |
| `salt_mist` | coastal or Red Sea oracle pressure | naval base, port, and convoy disruption |

### Safe use constraints

- Use fictional names only.
- Do not describe viable transmission methods.
- Do not describe cultivation, delivery, dosage, or real pathogen handling.
- Use abstract stockpiles, pressure values, and scripted effects.
- Treat weaponization as a route consequence, not a how-to process.
- Add condemnation, deaths, air cleanliness, and blowback where the existing systems support them.
- Allow containment and medical counterplay.
- Make AI use extremely restricted.

## Nonhuman country package requirements

Every nonhuman actor needs a different package from restored human polities.

| Required field | Direction |
| --- | --- |
| public name | direct and clearly nonhuman or supernatural |
| leader | fictional animal, oracle, stone host, or symbolic body |
| portrait | generated, never real human |
| flag | fictional generated flag |
| politics | fixed-purpose high-chaos politics with internal method choices |
| units | special units with extreme strengths and supply tradeoffs |
| diplomacy | limited normal diplomacy, special demands, high fear |
| focus tree | method, hierarchy, survival, expansion, disaster, endgame |
| AI | player-only or rare high-chaos AI |
| cleanup | if defeated or contained, remove disaster pressure and special recruitment |
| classification | register as special chaos country and actual nonhuman country when implemented |

## High-chaos unit directions

| Unit | Actor | Role | Strength | Downside |
| --- | --- | --- | --- | --- |
| elephant formations | grounded or high-chaos military route | shock and breakthrough in limited terrain | strong attacks and morale effect | supply, terrain, equipment, and attrition risk |
| gorilla forest guard | gorilla nation | forest defense and ambush | strong jungle and forest defense | weak in plains and mechanized warfare |
| chimpanzee raider | chimpanzee nation | disruption and raids | high reconnaissance and sabotage | poor conventional durability |
| living statue cohort | stone host | slow heavy assault | high armor-like defense and fort attack | very slow and hard to reinforce |
| oracle guard | oracle state | defensive aura and prediction support | better defense during disaster pressure | weak industry and manpower |
| river host | river supernatural route | river crossing and port pressure | river and marsh advantages | low performance inland |
| fever wardens | disease route | containment or weaponized pressure | reduces friendly disease impact or spreads abstract pressure | condemnation and blowback |

## AI restrictions

| Route | Normal AI | High-chaos AI | Player |
| --- | --- | --- | --- |
| Deep Green reveal | no | rare with explicit permission | yes |
| Nonhuman country spawn | no unless scenario or high-chaos event | rare | yes |
| Disaster demands | no | limited and targeted | yes |
| Fictional disease weaponization | no | almost never | yes with heavy costs |
| Living statue host | no | rare if route owns required heritage state | yes |
| World-end high-chaos support | no | only world collapse | yes |

## Blowback and containment

High-chaos power must create consequences.

| Blowback | Source | Response |
| --- | --- | --- |
| League fear | repeated disaster or disease pressure | reassurance missions, autonomy guarantees |
| Local panic | high-chaos units near member states | containment patrols and local support |
| Foreign containment | outside powers see impossible weather or disease | Scramble reaction escalates |
| Route corruption | Sacred Soil route overuses Deep Green tools | split route, lose grounded bonuses |
| Disease escape | fictional disease pressure exceeds safety | medical missions, quarantine abstractions |
| Nonhuman diplomacy collapse | animal or supernatural actors treated as normal puppets | special subject route or containment war |
| Heritage backlash | living statues used outside heritage regions | local legitimacy loss |

## Localisation direction

Text should show consequences, fear, impossible weather, strange animal behavior, sealed roads, warped supply lines, or missing patrols. It should not call human communities animals. It should not mock real rituals, languages, or religions. It should not describe real disease manufacture.

## High-chaos acceptance

The route is complete only if it includes gates, nonhuman classifications, generated assets, special units, AI restrictions, disaster pressure, disease safety, blowback, containment, cleanup, and route-specific achievements.
