# 012 Africa spec part 17, focus node blueprint atlas

This file expands the route packs into working focus node blueprints. Every label is an internal working label, not final localisation. The implementation agent may split, merge, rename, or move nodes if the route logic, mutual exclusions, idea lifecycle, decision unlocks, AI behavior, and asset motifs remain intact.

## Blueprint rules

- Keep every public country name direct and readable.
- Do not turn the tree into a vertical reward ladder.
- A focus node counts only when it changes decisions, missions, ideas, units, diplomacy, regions, routes, assets, or AI behavior.
- Ordinary routes stay grounded. Deep Green and nonhuman content stays high-chaos only.
- No focus grants free full continent cores.
- Final focus names and descriptions remain localisation work, not planning text.

## Shared opening node pack

| Working label | Role | Prerequisite logic | Main unlocks | Idea lifecycle | AI use |
| --- | --- | --- | --- | --- | --- |
| `opening_identity_seed` | Establish the selected African capital country as the continental claimant while leaving neighbours as targets for invitation, defense, pressure, or rivalry. | Start package | Cosmetic tag, continental claims, first League value display, basic war preparation decisions. | Initial unifier idea starts mixed, with ambition and administrative strain. | Never locks future politics. AI always takes this opener. |
| `opening_capital_summons` | Call the first continental assembly around the capital region. | After identity seed | Unlocks Charter invitation selectors and the first regional survey mission. | Adds assembly legitimacy to the mixed starting idea. | AI takes quickly unless at capital siege. |
| `opening_map_the_claim` | Create the public continental claim layer without giving free continent cores. | After capital summons | Reveals region groups, claims, and integration project previews. | No core grants. Claim pressure raises foreign alert. | AI takes after stabilising first war front. |
| `opening_defense_clause` | Make defense of African countries the first practical use of the claim. | After capital summons | Unlocks intervene against coloniser decisions and emergency aid missions. | Turns ambition into protector identity if used successfully. | AI takes if nearby African country is at war. |
| `opening_logistics_belt` | Prepare rail, port, convoy, and truck needs for a continent-scale project. | After map claim | Unlocks regional logistics works and supply hub missions. | Upgrades administrative strain if missions succeed. | AI prioritises when supply or industry is weak. |
| `opening_league_register` | Create the membership ledger for Charter League confidence and autonomy. | After defense clause | Shows member confidence, influence, and autonomy pressure. | Adds League institution stage one. | AI always takes before integration pressure. |
| `opening_regional_envoys` | Send route-neutral envoys to every named integration region. | After league register | Unlocks regional target pools and first refusal logic. | No direct integration. Improves confidence floor. | AI prioritises regions adjacent to capital. |
| `opening_arm_the_capital` | Create a defensive reserve so the unifier is not crushed before the tree opens. | After logistics belt | Spawns scaled capital guard units and depot defense missions. | Creates reserve idea that later routes upgrade or remove. | AI takes if under threat. |
| `opening_first_restorations` | Reveal restored polity subject options as partners, not annexation fodder. | After regional envoys | Unlocks first restoration candidate decisions by region. | Adds cultural legitimacy but can raise autonomy pressure. | AI uses only stable nearby candidates. |
| `opening_route_congress` | Force the major political route choice to appear after basic survival work. | After several opening nodes | Unlocks six normal route families and high-chaos route preview gates. | The mixed starting idea waits for route upgrade. | AI uses route weights from route packs. |
| `opening_continental_nameplate` | Update visible identity after the country has chosen its public continental method. | After route congress | Applies ideology or route compatible direct country name and flag path. | No office-like map names. | AI follows selected route. |
| `opening_early_test` | Run a first limited regional integration project so the player learns the loop. | After route congress and regional envoys | Starts one staged coring or association mission in the home region. | Failure can create rival appeal early. | AI selects the safest home region target. |

## Federal Charter node pack

| Working label | Role | Prerequisite logic | Main unlocks | Idea lifecycle | AI use |
| --- | --- | --- | --- | --- | --- |
| `federal_member_charters` | Make member consent the route engine. | Route opener | Unlocks member charter negotiations and confidence rewards. | League institution gains consent stage. | High if democratic or stable unifier. |
| `federal_conference_circuit` | Create rotating conferences by region. | After member charters | Regional conferences lower autonomy demand when supply and aid are real. | Builds federation legitimacy. | AI prefers during peace. |
| `federal_common_rail` | Tie federal legitimacy to logistics improvements. | After conference circuit | Rail and supply missions give confidence and later core discounts. | Logistics belt idea upgrades. | AI chooses poor infrastructure regions first. |
| `federal_member_reserves` | Build voluntary shared defense. | After member charters | Member reserve decisions provide units without annexing members. | Reserve idea becomes federal defense network. | AI chooses if League has enemies. |
| `federal_court_of_arbitration` | Resolve member disputes without immediate war. | After conference circuit | Arbitration missions can prevent rival bloc formation. | Cohesion rises on success. | AI uses when confidence is low. |
| `federal_customs_pool` | Create common economic gains without full state absorption. | After common rail | Resource and factory programs require member consent. | Adds economic federation stage. | AI uses if stability is high. |
| `federal_autonomy_guarantee` | Promise that members can stay inside the League without automatic annexation. | After arbitration | Lowers refusal risk and blocks coercive route buttons. | Locks out hard conquest options while active. | AI almost always accepts as democratic. |
| `federal_capital_rotation` | Give symbolic weight to multiple regions. | After customs pool | Rotating capital ceremonial missions raise confidence outside home region. | Adds regional trust. | AI uses when distant members resist. |
| `federal_constituent_status` | Create a middle tier between ally and annexed state. | After autonomy guarantee | Unlocks constituent member route and staged core missions. | Member idea gains federal rights. | AI takes when confidence is high. |
| `federal_referendum_ladder` | Cores require visible local support and time. | After constituent status | Plebiscite missions convert selected states if support, supply, and peace hold. | No instant continent cores. | AI uses cautiously. |
| `federal_continental_parliament` | Turn the League into a continental state only after repeated consent successes. | Late federal capstone | High legitimacy, peaceful integration discounts, rival reconciliation options. | Starting strain idea removed. | AI only with strong cohesion. |
| `federal_final_union_settlement` | Resolve remaining subjects, rivals, and associated states. | After continental parliament | Creates post-unification settlement projects and achievement hooks. | Federal final idea appears. | AI avoids during major war. |

## Revolutionary Congress node pack

| Working label | Role | Prerequisite logic | Main unlocks | Idea lifecycle | AI use |
| --- | --- | --- | --- | --- | --- |
| `revolutionary_liberation_committees` | Create local committees for anti-colonial war and member politics. | Route opener | Unlocks committee support in colonised or occupied states. | Starting idea turns into revolutionary legitimacy. | High if communist or in anti-colonial wars. |
| `revolutionary_print_networks` | Use radio, newspapers, and clandestine schools as influence tools. | After committees | Influence missions raise support but increase foreign crackdown risk. | Adds propaganda pressure. | AI uses against colonial targets. |
| `revolutionary_arms_corridors` | Commit equipment and convoys to liberation fronts. | After committees | Aid corridors consume rifles, trucks, convoys, or trains. | Arms influence component rises. | AI uses if stockpiles are healthy. |
| `revolutionary_general_strike` | Turn urban and port labour into a timed objective. | After print networks | Strike mission can weaken colonial owner in target region. | Raises revolutionary heat. | AI uses only if target owner is already strained. |
| `revolutionary_red_front` | Offer a militant League member path. | After arms corridors | Members can become revolutionary associates with lower autonomy but higher faction risk. | Member confidence splits by ideology. | AI prefers ideological allies. |
| `revolutionary_land_and_mines` | Make resource expansion political rather than pure extraction. | After general strike | Resource decisions trade output for local support and foreign sanctions. | Economic idea becomes mass production network. | AI chooses when industry is weak. |
| `revolutionary_purge_patrons` | Limit foreign sponsor capture of the movement. | After red front | Reduces sponsor influence and blocks foreign puppet outcomes. | Dependency risk falls. | AI uses if sponsor pressure is high. |
| `revolutionary_armed_congress` | Let the Congress command unified military action. | After red front and arms corridors | Shared war declarations and volunteer columns unlock. | League cohesion rises during anti-colonial wars. | AI uses if enemy controls many African states. |
| `revolutionary_rival_cells` | Represent internal radical competition. | After armed congress | High revolutionary heat can trigger factional struggle missions. | Failure creates rival left bloc. | AI avoids if stability is low. |
| `revolutionary_continental_communes` | Create integration through communes and congress seats. | After land and mines | Staged cores need local support and committee stability. | Revolutionary legitimacy upgrades. | AI uses in high support regions. |
| `revolutionary_export_the_congress` | Prepare support for other continent unifiers after near-unification. | Late route capstone | Unlocks continent sponsor missions without final world-end text. | Post-unification route opens. | AI uses only in high chaos. |
| `revolutionary_settle_the_cells` | Resolve radical factionalism before final unification. | After rival cells | Success prevents civil split. Failure unlocks emergency congress missions. | Final idea depends on outcome. | AI prioritises before big wars. |

## Crown of the Continent node pack

| Working label | Role | Prerequisite logic | Main unlocks | Idea lifecycle | AI use |
| --- | --- | --- | --- | --- | --- |
| `crown_restore_court_language` | Build a monarchist or dynastic route around a direct country identity. | Route opener | Unlocks court legitimacy and regnal flavor pools. | Starting idea becomes disputed court. | High for monarchist or neutrality leaning AI. |
| `crown_regnal_pool_gate` | Use only the two required source-language name strings until further source review. | After court language | Adds leader flavor hooks without file-name use. | No new obscene names invented. | AI neutral. |
| `crown_old_thrones_embassy` | Contact restored polities as partner courts. | After route opener | Restored kingdoms can join as subjects or court allies. | Court legitimacy rises through acceptance. | AI targets historically compatible regions. |
| `crown_sacred_capitals` | Create coronation missions tied to Aksum, Kongo, Asante, Kush, and other anchors. | After embassy | Capital and shrine missions raise legitimacy without immediate annexation. | Court idea gains ritual authority. | AI chooses controlled or allied capitals. |
| `crown_palace_guard` | Build route-specific elite and ceremonial defense units. | After route opener | Spawns limited palace guard, later upgradeable. | Reserve idea becomes guard household. | AI uses when manpower is adequate. |
| `crown_dynastic_compacts` | Use marriage, regency, treaty, and tribute as association routes. | After embassy | Members can become associated kingdoms with high autonomy. | Lower coercion risk but slower integration. | AI uses for strong members. |
| `crown_tribute_roads` | Make old trade routes the economic branch. | After dynastic compacts | Caravan, port, and mine projects build resources and rail. | Court economy stage rises. | AI picks regional trade corridors. |
| `crown_challenge_the_usurper` | Allow rival royal claimants to appear if legitimacy is low. | After sacred capitals | Mission chain can create monarchist rival bloc. | Failure worsens disputed court. | AI avoids if weak. |
| `crown_continental_coronation` | Crown route proclamation after broad recognition. | Late route capstone | Cosmetic identity, final route idea, and post-unification court settlement. | Direct country name remains readable. | AI uses only after broad control. |
| `crown_protect_the_old_names` | Keep restored polities visible instead of absorbing every subject. | After coronation | Associated states can remain on map for bonuses. | Adds heritage trust component. | AI uses if not expansionist. |
| `crown_imperial_integration` | Offer a harder path to absorb associated kingdoms. | After coronation | Requires support, legitimacy, and low resistance. | Risks court backlash. | AI rare. |
| `crown_world_court_route` | Prepare late interaction with other continent monarchic or dynastic unifiers. | Late high-chaos gate | Diplomatic route opens, no final super-event text. | Post-unification ambition only. | AI only with high legitimacy and high chaos. |

## Continental Command node pack

| Working label | Role | Prerequisite logic | Main unlocks | Idea lifecycle | AI use |
| --- | --- | --- | --- | --- | --- |
| `command_emergency_staff` | Create a military government route without making the country name bureaucratic. | Route opener | Unlocks command obedience, mobilization, and emergency reserve missions. | Starting idea becomes command strain. | High if at war or low stability. |
| `command_joint_operations` | Build a unified League military staff. | After emergency staff | Member reserves and joint planning become stronger but autonomy demand rises. | Command obedience rises. | AI uses in war. |
| `command_border_belts` | Secure ports, railways, and borders before offensives. | After joint operations | Timed missions require divisions in key regions. | Failure lowers obedience and confidence. | AI prioritises threatened borders. |
| `command_depot_levies` | Use captured depots as unit and equipment sources. | After border belts | Spawns scaled levy units only when depot states are controlled. | Reserve idea becomes depot command. | AI uses with equipment shortage. |
| `command_military_governors` | Create route-specific occupation and integration methods. | After joint operations | Military governor decisions speed integration but raise resistance. | Legitimacy falls if abused. | AI avoids overuse unless high threat. |
| `command_continental_training` | Standardise templates and officers. | After depot levies | Unlocks training decisions and commander recruitment. | Command strain mitigated. | AI takes often. |
| `command_member_obedience` | Pressure League members into military alignment. | After military governors | Members can accept command status or rebel. | Confidence and autonomy values matter. | AI uses on weak members. |
| `command_forced_march_wars` | Enable hard unification wars only after diplomatic route has failed. | After member obedience and border belts | War goals on refusing blocs with resistance risks. | Foreign alert rises. | AI uses if very strong. |
| `command_civilian_restoration_question` | Choose whether command returns power or remains permanent. | Mid route fork | Unlocks soft military republic or permanent command branch. | Idea lifecycle splits. | AI choice depends on stability. |
| `command_continental_high_command` | Capstone for permanent command. | Late route capstone | Strong army payoff, weak diplomatic trust, and harsher integration. | Final command idea. | AI rare outside high war pressure. |
| `command_guarded_federation` | Capstone for return-to-civil route. | Late route capstone | Better confidence, weaker war bonuses, more federal compatibility. | Command idea softened. | AI chooses if peace returns. |
| `command_world_campaign_staff` | Prepare continent-scale warfare against other unifiers. | Post-unification gate | Opens continent war planning without terminal trigger text. | World-end remains rare. | AI only at world collapse. |

## Sacred Soil node pack

| Working label | Role | Prerequisite logic | Main unlocks | Idea lifecycle | AI use |
| --- | --- | --- | --- | --- | --- |
| `soil_local_custodians` | Make land, shrine, forest, and water protection a political route. | Route opener | Unlocks custodian missions and local reception value. | Starting idea becomes custodianship. | High for non-aligned or defensive AI. |
| `soil_ancestral_claims` | Tie claims to region memory and protection, not instant conquest. | After custodians | Claims and protectorate options by region. | Local support rises when defensive. | AI uses in home and adjacent regions. |
| `soil_forest_oaths` | Introduce nature covenant imagery without nonhuman actors yet. | After custodians | Disaster pressure remains dormant unless high-chaos gate opens. | Custodianship idea grows. | AI safe route. |
| `soil_river_and_rain` | Build water, flood, drought, and agriculture missions. | After forest oaths | Infrastructure and food missions protect regions from failure states. | Industry branch gains rural support. | AI uses in low supply regions. |
| `soil_guardians_of_sites` | Protect Aksum, Meroe, Great Zimbabwe, Kilwa, Timbuktu, and other anchor sites. | After ancestral claims | Site guard missions raise legitimacy and unlock restoration candidates. | Heritage protection value rises. | AI chooses controlled sites. |
| `soil_refuse_extraction` | Reject pure resource strip-mining. | After river and rain | Resource decisions require local support and longer timers. | Raises trust, lowers speed. | AI uses if stable. |
| `soil_hidden_oracles` | Create the route gate for oracle states at high chaos. | After forest oaths and high chaos | Reveals nonhuman or supernatural options only if boundaries are met. | No human caricature framing. | AI almost never. |
| `soil_custodian_league` | Offer a high autonomy League model. | After guardians | Members can become protected custodians instead of annexed subjects. | Confidence rises, integration slows. | AI uses with strong members. |
| `soil_living_land_warning` | Introduce abstract disaster pressure as a mechanic gate. | High-chaos route gate | Disasters are abstract game effects tied to demands and war. | Pressure value becomes visible. | AI restricted. |
| `soil_deep_green_choice` | Split ordinary sacred soil from Deep Green Covenant. | Late fork | Normal route remains human and grounded. High-chaos route opens only by gate. | Idea lifecycle splits. | AI only chooses normal unless special rule. |
| `soil_continental_stewardship` | Normal route capstone for a grounded custodian federation. | Late route capstone | Integration through protection, agriculture, and heritage projects. | Final custodian idea. | AI safe. |
| `soil_green_door` | Formal gate into high-chaos forest and disaster systems. | High-chaos transition | Unlocks Deep Green route if chaos, route, and player choice align. | Blocks if high-chaos disabled. | AI blocked by default. |

## Black Star Return node pack

| Working label | Role | Prerequisite logic | Main unlocks | Idea lifecycle | AI use |
| --- | --- | --- | --- | --- | --- |
| `black_star_harbour_call` | Open diaspora contact through ports and associations. | Route opener | Unlocks returnee lane display and first port missions. | Starting idea gains diaspora promise. | High for naval or trade-oriented AI. |
| `black_star_line_memory` | Use Garveyite and wider Pan-African shipping history as research-gated inspiration. | After harbour call | Shipping lanes require convoys, escorts, and port access. | No final slogan text. | AI uses if convoys are available. |
| `black_star_liberia_gateway` | Model Liberia and Atlantic return corridors with historical sensitivity. | After harbour call | Gateway missions balance returnee settlement and local reception. | Local support matters. | AI uses only if region stable. |
| `black_star_caribbean_societies` | Add Caribbean association and volunteer channels. | After line memory | Volunteer, labour, and cultural missions affect industry and diplomacy. | Diaspora network value rises. | AI uses with free convoys. |
| `black_star_afro_american_invitation` | Invite Afro-American returnees through staged missions. | After gateway | Settlement missions need housing, port capacity, and local consent. | Can create cultural diplomacy benefits. | AI uses cautiously. |
| `black_star_returnee_settlements` | Create settlement projects as real map and industry work. | After invitation | Builds factories, infrastructure, and local industry if conditions are met. | Failure raises reception strain. | AI picks high capacity states. |
| `black_star_skilled_cadres` | Turn returnees into technical, medical, and officer paths. | After settlements | Advisor, officer, and industry decisions unlock. | Network idea upgrades. | AI uses if education route available. |
| `black_star_lane_escorts` | Protect shipping lanes from foreign disruption. | After line memory and settlements | Escort missions consume convoys, fuel, ships, or naval access. | Failure disrupts lane. | AI uses if at war or raided. |
| `black_star_cultural_diplomacy` | Use diaspora networks to improve recognition without final text. | After skilled cadres | Diplomatic missions lower sanctions and raise confidence. | Recognition component rises. | AI uses in peace. |
| `black_star_returnee_guard` | Create limited units from trained returnee cadres. | After lane escorts | Spawns small specialist guard if missions succeeded. | No free army loop. | AI one-time only. |
| `black_star_homecoming_settlement` | Capstone for successful return route. | Late route capstone | Final diaspora idea, achievement hooks, cultural diplomacy payoff. | Failure states still possible if reception low. | AI only if lanes stable. |
| `black_star_broken_piers` | Failure branch for disrupted lanes and settlement backlash. | Failure gate | Emergency missions repair confidence and port capacity. | Diaspora promise becomes strained if ignored. | AI prioritises if visible. |

## Deep Green Covenant node pack

| Working label | Role | Prerequisite logic | Main unlocks | Idea lifecycle | AI use |
| --- | --- | --- | --- | --- | --- |
| `green_threshold` | Confirm this path is high-chaos only and never baseline. | Requires high chaos and Sacred Soil transition | Reveals high-chaos mechanics only after explicit gate. | Normal human politics no longer define the route. | AI blocked unless manually allowed. |
| `green_speaking_forest` | Introduce supernatural forest actor as nonhuman or supernatural force. | After threshold | Unlocks abstract demand missions and disaster pressure. | No ethnic caricature framing. | AI blocked. |
| `green_oracle_circles` | Let oracle states predict or bargain with disasters. | After speaking forest | Prediction missions lower blowback if obeyed. | Oracle pressure rises. | AI only with special high-chaos permission. |
| `green_great_ape_embassies` | Open nonhuman animal actor diplomacy only as clearly nonhuman content. | After threshold | Gorilla and chimpanzee actor packages can appear. | No human polity mimicry. | AI rare scripted. |
| `green_living_stone` | Unlock living-statue host conditions. | After oracle circles | Stone or statue units appear only through rare gated missions. | Severe supply and stability costs. | AI almost never. |
| `green_wrath_of_weather` | Use disaster pressure against enemies as abstract monthly pulses. | After speaking forest | War enemies can suffer state disaster effects from scripted pressure. | Blowback can strike owner. | AI blocked unless route owner is special. |
| `green_fever_without_name` | Open fictional disease mechanics with no real pathogen details. | After high-chaos disease gate | Fictional fever pressure spreads by in-game variables, not real biology. | Condemnation and blowback risks rise. | AI blocked by default. |
| `green_bargain_with_cities` | Offer cities relief in exchange for compliance. | After wrath of weather | Target states can accept protection, resist, or trigger disaster pressure. | Resistance outcomes matter. | AI restricted. |
| `green_nonhuman_commanders` | Create leader and commander assets for nonhuman or supernatural actors. | After ape embassies or living stone | Generated portraits and unit names required. | No real human leader mapping. | AI no generic path. |
| `green_continent_of_roots` | High-chaos continental integration through nature pressure. | Late route capstone | Absurd power and major blowback, no free instant cores. | Final high-chaos idea. | AI only in scenario or rare gate. |
| `green_world_weather_pact` | Post-unification interaction with other continent unifiers. | Post-unification high-chaos | Can threaten or bargain through abstract disasters. | World-end still gated. | AI only at world collapse. |
| `green_ashes_in_the_rain` | Failure branch when blowback exceeds control. | Failure gate | Disaster relief missions and route collapse risk. | Can break the high-chaos state. | AI tries emergency relief. |

## Mutual exclusion and interaction notes

- Federal Charter, Revolutionary Congress, Crown of the Continent, Continental Command, Sacred Soil, and Black Star Return are normal route families. They should be mutually exclusive only at the public governing method layer, while industry, logistics, military, and regional integration support branches remain broadly available.
- Deep Green Covenant is not a normal political route. It is a high-chaos conversion from Sacred Soil or a rare scenario gate. It should never be chosen by ordinary AI without an explicit high-chaos permission flag.
- Black Star Return can cooperate with Federal Charter, Revolutionary Congress, Crown of the Continent, and Sacred Soil through side nodes if the implementation prefers a secondary route design. If it is implemented as a full political route, its returnee settlement and shipping-lane systems must remain unique.
- Continental Command can borrow federal or revolutionary support nodes only after it chooses whether command is temporary or permanent.
- Crown of the Continent must preserve the two required source-language leader-name strings only as flavor data. No raw obscene strings should appear in technical identifiers.
