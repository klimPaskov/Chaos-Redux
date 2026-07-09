# 012 Africa spec part 27, regional state-group closure atlas

This file expands the state-group handoff without inventing exact HOI4 state ids. Exact ids require live vanilla and repo state files. This atlas gives the implementation agent the canonical mapping method, target groups, and integration requirements.

## State-id gate status

Exact HOI4 state ids remain blocked in this sandbox because the live game files and Chaos Redux repository are not available. The final package should not guess them from memory. The implementation agent must resolve them by reading vanilla `history/states/`, Chaos Redux state overrides, and any modded map files.

## State resolver worksheet

The implementation agent should build a resolver table with these columns before scripting region triggers.

| Column | Purpose |
| --- | --- |
| state id | exact HOI4 state id |
| state name | vanilla or modded state name |
| 1936 owner | starting owner |
| 1936 controller | starting controller |
| original cores | cores at game start |
| colonial owner group | British, French, Belgian, Portuguese, Italian, Spanish, South African, independent, or other |
| region bucket | one canonical region from this file |
| restored polity candidates | country packages that can plausibly use the state |
| capital or VP note | major city, capital, or victory point |
| port | yes or no |
| rail | none, weak, medium, strong |
| supply hub | yes or no |
| resources | major resource notes |
| terrain pressure | desert, jungle, mountain, savanna, urban, coast, island |
| integration difficulty | low, medium, high, extreme |
| special gate | island, Sahara, Nile, Congo forest, RSA branch, high-chaos, Black Star lane |
| source note | vanilla, Chaos Redux override, or manual review |

## Canonical region buckets

| Bucket | Geographic intent | Key mechanics | Typical difficulty |
| --- | --- | --- | --- |
| `maghreb_mediterranean` | Morocco, Algeria, Tunisia, Libya coast, Mediterranean approaches | ports, forts, foreign reaction, Mediterranean diplomacy | high because outside powers care |
| `egypt_nile_delta` | Egypt and lower Nile when map scope permits | Nile access, Suez pressure, world reaction | extreme if Suez or major power control is involved |
| `sahara_fezzan_tibesti` | Sahara interior, Fezzan, Tibesti, desert corridors | water, airstrips, desert logistics | high due to supply |
| `western_sahel` | Senegal river, Mali, Niger west, Burkina Faso corridors | caravan defense, Futa, Mossi, Songhai | medium to high |
| `lake_chad_bornu` | Lake Chad, Bornu, Chad basin | Sao, Kanem-Bornu, lake defense | medium |
| `gulf_of_guinea_west` | Ghana, Togo, Benin coast, Ivory Coast, Guinea coast | Asante, Dahomey, Futa Jallon, port lanes | medium to high |
| `yoruba_edo_delta` | Southwestern Nigeria, Edo, Niger delta borderlands | Oyo, Ife, Ijebu, Owo, Benin or Edo | medium |
| `central_forest_congo` | Congo basin and central forest | Kongo, Kuba, Luba, Lunda, Loango, Deep Green | high due to forest and disease gates |
| `katanga_luapula_copper` | Katanga, Luapula, copper belt | Luba, Kazembe, Lunda, resource projects | high economic value |
| `nile_horn_highlands` | Sudan, Ethiopia, Eritrea, Red Sea highlands | Kush, Nubia, Makuria, Alodia, Aksum | high |
| `somali_red_sea_coast` | Somalia, Gulf of Aden, Red Sea ports | Adal, Harar, Ajuran, Warsangali, Mogadishu | medium to high |
| `swahili_coast` | Kenya and Tanzania coast, Mozambique coast where linked | Kilwa, Mombasa, Zanzibar, Pate, Lamu, Sofala | high port value |
| `great_lakes` | Uganda, Rwanda, Burundi, Lake Victoria region | Buganda and lake diplomacy | medium |
| `zambezi_plateau` | Zimbabwe, Zambia, Malawi, Mozambique interior | Great Zimbabwe, Mutapa, Rozwi, Barotse | medium to high |
| `southern_africa_core` | South Africa, Botswana, Lesotho, Eswatini, Namibia | RSA branch, Zulu, Xhosa, Basotho, Griqua | extreme during RSA civil war |
| `madagascar_island` | Madagascar | Merina and Madagascar route variants | high island logistics |
| `indian_ocean_islands` | Comoros, Mauritius, Seychelles, island relays | convoy, diaspora, island federation | high naval dependency |
| `atlantic_island_relays` | Cape Verde, Canary, Atlantic relays where map allows | Black Star lanes, foreign access | high foreign reaction |

## Region integration project template

Each region should use a staged project.

| Stage | Meaning | Typical requirements | Result direction |
| --- | --- | --- | --- |
| Survey | identify local institutions and infrastructure | control or League access, no active battle, scout mission | reveals local project decisions |
| Stabilize | prevent immediate revolt or rival recruitment | local support, supplied divisions, basic aid, port or rail security | lowers resistance pressure |
| Build | invest in rail, ports, factories, hospitals, schools, or depots | civilian factories, trains, convoys, support equipment, time | raises integration capacity |
| Negotiate | settle autonomy, restored polity status, or member rights | confidence, autonomy charter, route-specific concessions | opens federation or puppet path |
| Integrate | convert claims to staged cores or federated status | mission success, stability, compliance, no rival bloc control | grants cores slowly or creates durable member |
| Review | post-integration cleanup and unrest check | no active revolt, resistance under threshold, route fit | closes project or opens failure event |

## Region-specific requirements

| Region | Required proof before coring | Extra risk | Best route |
| --- | --- | --- | --- |
| Maghreb Mediterranean | port security, foreign reaction cooled, regional government | great-power ultimatums | Federal, Command, Revolutionary |
| Egypt Nile Delta | Suez and Nile settlement, international crisis cooldown | global war escalation | Federal or Command only after major threshold |
| Sahara Fezzan Tibesti | water and supply route project | attrition and low infrastructure | Sacred, Federal, Command |
| Western Sahel | caravan and rail route restored | cross-border rival claims | Federal, Crown, Revolutionary |
| Lake Chad Bornu | lake defense and border settlement | Kanem-Bornu autonomy demand | Crown, Federal |
| Gulf of Guinea West | port and trade settlement | Black Star lane backlash and coastal foreign pressure | Federal, Black Star, Revolutionary |
| Yoruba Edo Delta | city autonomy and trade route pact | Oyo and Benin rivalry | Federal, Crown |
| Central Forest Congo | disease safety, river control, local support | high-chaos spillover and resistance | Sacred, Federal, Deep Green only if gated |
| Katanga Luapula Copper | resource charter and labor settlement | exploitation accusations | Federal, Revolutionary, Command |
| Nile Horn Highlands | highland legitimacy and Red Sea route | Aksum or Kush symbolic refusal | Crown, Federal, Sacred |
| Somali Red Sea Coast | port security and clan autonomy | rival coastal blocs | Federal, Sacred, Command |
| Swahili Coast | port autonomy, convoy safety, customs settlement | Indian Ocean blockade | Black Star, Federal |
| Great Lakes | lake route and local monarchy or republic settlement | regional border tension | Federal, Crown |
| Zambezi Plateau | rail, plateau defense, heritage settlement | Great Zimbabwe, Mutapa, and Rozwi rivalry | Crown, Federal, Sacred |
| Southern Africa Core | RSA civil war aftermath, racial regime legacy, border settlement | Allied peace and loyalist resistance | Federal or Command after civil war |
| Madagascar Island | convoy safety and island institutions | naval blockade | Federal, Black Star |
| Indian Ocean Islands | port access and convoy guarantee | tiny states can be swallowed too easily | Federal, Black Star |
| Atlantic Relays | foreign access or conquest settlement | outside-power reaction | Black Star, Federal |

## Federal member route

Federal integration should let some members remain visible. This can be subject status, autonomy status, or a special member flag. The player should choose between direct absorption and durable federation when the design supports it.

Federal member benefits:

- lower resistance
- higher League cohesion
- better regional project speed
- restored-polity achievements
- more stable post-unification order

Federal member costs:

- slower centralization
- fewer instant cores
- member confidence upkeep
- possible vetoes or regional demands

## Puppet route

Puppet route should apply to dependent members, defeated rivals, or protected states. Puppet route is not the same as voluntary federation.

Puppet requirements:

- high unifier influence or war victory
- target dependency or defeated status
- local resistance below crisis threshold
- no strong foreign guarantee
- route allows subject management

Puppet risks:

- rival appeal rises in nearby members
- foreign powers can support puppet independence
- puppet can become a weak link in continent wars
- coercive puppet conversion can block federal achievements

## Coercive annexation route

Coercive annexation is allowed for Command, some Revolutionary outcomes, and high-chaos routes. It should be powerful and risky.

Required consequences:

- immediate claims or occupation tools, not free full cores
- resistance pressure
- League cohesion penalty
- outside-power reaction if used on many members
- rival bloc chance
- delayed coring missions
- achievement disqualifier for consensual routes

## Region cleanup

When a region is fully integrated, cleanup should:

- hide survey and early stabilization decisions
- keep unrest and review decisions only while risks remain
- remove obsolete member target flags
- convert remaining subject or member states based on the chosen route
- preserve achievement flags for voluntary, puppet, coercive, and high-chaos paths
- record regional completion for Scramble and world-end thresholds

## State-id implementation blocker

This final package gives enough geographic structure to implement safely once live state files are available. It does not provide exact state ids. Guessing exact state ids from memory would be a false completion claim.
