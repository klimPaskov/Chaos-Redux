# Achievement Matrix

All titles are working labels, not final localisation. Achievement IDs are planning keys that must be checked against the live achievement registry.

| Working ID | Working label | Eligible actor | Unlock conditions | Disqualifiers | Visibility | Difficulty | Tracking needs | Icon direction |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `chaosx_020_first_cordon` | The First Cordon | origin owner | origin reaches Cured, no other state ever reaches Infected, deaths below strict origin-population share | weapon project started, second infection, rat emergence | visible | hard | origin state, max infected-state count, attributed deaths, cure state | closed black gate around a small plague mark |
| `chaosx_020_forty_days` | Forty Days | country bordering infected foreign state | targeted border cordon held 40 days, country at war during part, no infection through corridor, front supply maintained | corridor reopened early, target infection crosses | visible | hard | selected corridor, timer, war state, supply threshold, route attribution | old border post, hourglass, dark mist |
| `chaosx_020_open_roads_closed_graves` | Open Roads, Closed Graves | first infected country | domestic eradication without full border closure or total civilian travel suspension, losses below threshold | prohibited restrictions used, domestic Rat Nation | hidden | very hard | action-use flags, death share, domestic disease count | open road passing a sealed plague pit |
| `chaosx_020_physician_against_night` | Physician Against the Night | infected human country | countermeasure 100 before Evolution I, every domestic state Cured, findings published | weaponization begun | visible | very hard | evolution timestamp, progress, domestic cleanup, publication | plague doctor lamp over dark city |
| `chaosx_020_common_remedy` | The Common Remedy | any human country | medical or knowledge aid to 10 countries, meaningful contribution to global eradication, no biological deployment | any bioweapon deployment | visible | hard | unique aid recipients, contribution score, eradication actor, deployment history | many hands passing a medical case |
| `chaosx_020_black_glass_cabinet` | The Cabinet of Black Glass | biowarfare country | complete Safety-First weapon project, hold stockpile 365 days, no domestic accident, never deploy, finish full domestic cure | accident, deployment, stockpile loss before timer | hidden | very hard | project branch, stockpile timer, accident and deployment flags, cure progress | sealed black vial inside locked cabinet, no readable label |
| `chaosx_020_physicians_folly` | The Physician's Folly | country that deploys Black Plague | traced domestic return outbreak from own program, contain and cure it, same government survives | annexed, government replaced, outbreak not attributed | hidden | very hard | deployment provenance, return route, government continuity, cleanup | cracked plague mask reflected in dark glass |
| `chaosx_020_burn_warrens` | Burn the Warrens | any human country | lead destruction of the `RTA` carrier before Rat King, clear every liberated burrow node, complete global eradication | Rat King appears | visible | extreme | rat kill contribution, Rat King flag, burrow cleanup global, eradication | engineer torch over collapsed burrow entrance |
| `chaosx_020_no_census_required` | No Census Required | base Rat Nation | field at least 100 rat divisions through pulses, control 30 plague states, no ordinary manpower or equipment use | becomes Rat King before threshold if conditions not preserved | visible to rat actor | hard | pulse-created division count, state count, manpower and equipment audit | vast rat silhouettes over an empty ledger |
| `chaosx_020_one_crown_many_tails` | One Crown, Many Tails | Rat King after the `RTA` transfer | absorb five internal brood basins or their surviving state markers, complete the Evolution IV transfer, and become Rat King | another candidate crowned | visible to rat actor | extreme | absorbed brood-state count, candidate score, transfer identity | five entwined tails below a dark crown |
| `chaosx_020_rat_that_read` | The Rat That Read | Rat King | Council route complete, Sentience maximum, capture defined research capitals, preserve minimum controlled human population | Empty the Cities route, population falls below floor | hidden | extreme | government route, Sentience, target capitals, preserved population | rat paw over open book and radio dial, no text |
| `chaosx_020_crown_one_continent` | Crown of One Continent | Rat King | continent control verified on the pre-terminal route, Evolution V not yet recorded, terminal takeover not yet triggered | loses control before award check, Evolution V or world_end already active | visible to rat actor | extreme | continent target, control percentage, capital list, pre-terminal route state | continent silhouette beneath a tail crown |
| `chaosx_020_pale_sovereign` | The Pale Sovereign | Rat King | complete world-end path and trigger Rat King terminal scenario | another world_end active | hidden | terminal | scenario flag and actor identity | pale throne above a ruined globe, no text |
| `chaosx_020_doctor_wu_last_call` | Doctor Wu's Last House Call | human country with Event 163 link | use Doctor Wu protocol after Evolution II, cure states on at least 2 continents, no Rat King appears | Rat King flag, fewer than 2 continents | hidden | rare extreme | Event 163 bridge, continent cure set, Evolution II, Rat King state | medical bag and lantern beside two dark coastlines |

## Achievement implementation requirements

- use one root-level achievement registry according to project convention
- assign a stable unique achievement ID only after conflict checking
- write title and description localisation from the achievement directions, not from working labels automatically
- implement disqualifiers explicitly
- preserve historical tracking across tag changes where intended
- a permanent Black Plague triggerable-scenario flag disqualifies the ordinary Event 20 achievements unless an achievement is explicitly designed for scenario play
- prevent puppet, observer, console-like, or unrelated scenario shortcuts when existing achievement rules require it
- create completed, grey, and not-eligible 64 by 64 DDS assets
- list each achievement in event docs and asset manifest
- avoid unlocking achievements merely because Event 20 fired
