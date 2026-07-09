# 012 Africa spec part 16, achievements and asset handoff expansion

This file expands achievement conditions and asset prompts into exact handoff items. Achievement titles and descriptions remain direction-only. Super-event title, quote, button, cultural remark, and audio remain research-gated.

## Achievement tracking model

Achievements should use flags and variables that can be checked from final state or from durable route history. Do not unlock achievements automatically when the event fires.

Common tracking values:
- `africa_unifier_tag_saved`
- `africa_route_federal_completed`
- `africa_route_revolutionary_completed`
- `africa_route_crown_completed`
- `africa_route_command_completed`
- `africa_route_sacred_soil_completed`
- `africa_route_black_star_completed`
- `africa_route_deep_green_completed`
- `africa_member_wars_against_african_countries`
- `africa_regions_core_integrated_count`
- `africa_federal_members_count`
- `africa_restored_polities_count`
- `africa_rival_bloc_reconciled`
- `africa_rsa_continental_victory`
- `africa_allies_peace_after_rsa`
- `africa_diaspora_lanes_established`
- `africa_diaspora_convoy_tragedies`
- `africa_settlement_regions_stable`
- `africa_scramble_reaction_survived`
- `africa_outside_power_wars_won`
- `africa_high_chaos_actor_recognized_count`
- `africa_world_is_one_terminal_complete`

Final variable and flag names can change during implementation, but the tracking logic should preserve these meanings.

## Achievement suite

| Working id | Working label direction, not final text | Eligible country | Unlock conditions | Disqualifiers | Visibility | Icon direction |
| --- | --- | --- | --- | --- | --- | --- |
| africa_012_federal_without_conquest | Peaceful federation mastery | Africa unifier | Complete Federal Charter, integrate or federate all African regions, zero offensive wars against independent African-capital countries | Any coercive annexation, African member war count above 0 | Hidden or rare | Linked hands over continent-colored cloth, no map-table scene |
| africa_012_charter_never_broke | League confidence mastery | Africa unifier | Keep League cohesion above high threshold from first member to Africa is one | Member exit, rival bloc war, failed protection of member capital | Visible hard | Charter seal and raised banners |
| africa_012_rsa_breakaway_victory | RSA civil-war branch mastery | Azania or continental RSA side | Win RSA civil war, trigger Allied peace, continue into Africa package | Loyalist side wins, Allied peace not resolved | Visible | Broken chain over southern landscape |
| africa_012_liberation_without_annexation | Defensive anti-colonial route | Africa unifier | Defend at least five African countries against colonizers and keep them as members or federal partners | Annexing those defended countries within a short window | Visible | Shield over port and rail workers |
| africa_012_ten_restored_polities | Restoration breadth | Africa unifier | Restore at least ten major or secondary polities and keep them alive in the League | Fewer than ten survive, restored-polity revolt active | Visible | Ten small carved emblems around central banner |
| africa_012_crown_of_many_houses | Crown route mastery | Africa unifier on Crown route | Complete crowned federation or empire route with at least six restored polity partners | Revolutionary Congress capstone, all restored polities annexed by force | Hidden | Royal umbrella and regional emblems |
| africa_012_congress_against_empires | Revolutionary route mastery | Africa unifier on Revolutionary route | Expel all colonial control from Africa through League wars, aid, or revolutions | Joining a colonial faction or accepting colonial protectorate | Visible | Printing press, rail depot, and liberation banner |
| africa_012_command_continent | Military route mastery | Africa unifier on Command route | Survive Scramble reaction war and complete all command logistics projects | League cohesion falls below collapse threshold | Visible hard | Field radio, rail hub, and marching boots |
| africa_012_sacred_soil_steward | Sacred Soil route mastery | Africa unifier on Sacred Soil route | Complete all heritage and water missions in several regions before Africa is one | Desecration or extraction backlash above threshold | Visible | Baobab, well, and stone ruin motif |
| africa_012_black_star_safe_harbor | Diaspora safety mastery | Africa unifier on Black Star Return | Establish at least five lane families, zero convoy tragedies, and high local reception in several regions | Convoy tragedy count above 0, housing crisis unresolved | Hidden hard | Ocean liner approaching lit port |
| africa_012_returnee_guardians | Diaspora military use | Africa unifier | Use returnee guard units to defend a League member capital or port during war | Unit type never created or member capital falls | Hidden | Port guards and star motif |
| africa_012_no_member_left_behind | Protection mastery | Africa unifier | No member loses capital to colonizer after joining League, and Africa is one fires | Any protected member capitulates to colonizer | Hidden hard | Shield around several small flags |
| africa_012_rival_reconciled | Diplomacy recovery | Africa unifier | Rival bloc forms, then reconciles peacefully and re-enters League before Africa is one | Rival bloc destroyed by annexation, direct conquest route | Hidden | Two broken banners tied together |
| africa_012_every_region_integrated | Regional integration mastery | Africa unifier | Complete staged integration for every named region, with no active resistance outcome | Any region remains Stage 3 or lower at Africa is one | Visible hard | Regional seals around central city |
| africa_012_scramble_breaker | Outside reaction victory | Africa unifier | Scramble response triggers and Africa survives sanctions, ultimatum, or coalition war | Africa loses Africa is one status or collapses | Visible | Ship silhouettes facing coastal banners |
| africa_012_recognition_conference | Diplomatic Scramble outcome | Africa unifier | End Scramble reaction through recognition conference without major outside war | Major outside war starts before recognition | Hidden | Conference table can appear, but central focus should be delegates and flags |
| africa_012_red_sea_oracle_bound | High-chaos maritime anomaly | Africa unifier | Recognize or contain Red Sea Oracle without losing a major diaspora lane | Oracle hostile at end, port crisis unresolved | Secret | Storm and port lantern |
| africa_012_forest_pact_kept | Nonhuman covenant safety | Africa unifier on Deep Green or Sacred Soil | Recognize a forest nonhuman actor, keep habitat promises, and avoid forest blowback until Africa is one | Broken habitat promise, hostile nonhuman actor at end | Secret | Gorilla or forest silhouette with protected valley |
| africa_012_stone_hosts_contained | Supernatural heritage mastery | Africa unifier | Awaken or contain a living-stone actor and complete integration without heritage revolt | Host becomes hostile or destroys integration region | Secret | Stone figure and old walls |
| africa_012_fever_without_name_contained | Fictional disease containment | Any Africa package country | Contain fictional outbreak pressure without weaponizing it | Abstract weaponization used, outbreak unresolved | Secret | Medical mask and sealed icon, no real pathogen imagery |
| africa_012_deep_green_dominion | High-chaos route completion | Africa unifier on Deep Green | Complete Deep Green Covenant and keep at least half the League or equivalent members stable | League collapses fully before capstone | Secret hard | Forest canopy, animal eyes, and storm light |
| africa_012_africa_is_one | Continental milestone | Africa unifier | Trigger Africa is one through any valid route | Event owner loses status before milestone | Visible | Continental celebration, not a flat map |
| africa_012_all_routes_in_one_campaign_family | Replay spread meta | Player profile or campaign flag if supported | Complete several route families across separate valid runs if achievement system supports persistence | Not applicable if persistence unsupported | Hidden meta | Seven route emblems |
| africa_012_the_world_is_one | Terminal world-end | Africa or final continent-scale power | Complete The World is One terminal path with all required continent unifiers present | World-end branch not completed | Secret terminal | Planet-scale emblem, final super-event asset direction research-gated |

## Achievement implementation notes

- Do not reveal secret route details in ordinary focus or decision text.
- Use achievement UI and docs for full requirements.
- If persistent profile tracking is not supported, replace the replay spread achievement with a hard single-campaign variant.
- Hidden and secret achievements need icon assets at the same quality as visible ones.
- Achievement icons need completed, grey, and not-eligible variants if the system requires them.
- Achievement ids should be stable and root-level final DDS names should match the registered achievement ids.

## Asset handoff index

All paths are proposed. The asset agent or implementation agent may adjust only if repo patterns require it.

### Focus icon families

| Asset id | Type | Target size | Source mode | Proposed final DDS path | Proposed sprite | Related content | Visual direction |
| --- | --- | --- | --- | --- | --- | --- | --- |
| goal_012_africa_continental_proclamation | Focus icon | 94x86 | Generated | gfx/interface/goals/012_africa/goal_012_africa_continental_proclamation.dds | GFX_goal_012_africa_continental_proclamation | Opening pack | Crowd, flag, sunrise, no map-table |
| goal_012_africa_charter_convention | Focus icon | 94x86 | Generated | gfx/interface/goals/012_africa/goal_012_africa_charter_convention.dds | GFX_goal_012_africa_charter_convention | Federal Charter | Hands and charter seal |
| goal_012_africa_revolutionary_cells | Focus icon | 94x86 | Generated | gfx/interface/goals/012_africa/goal_012_africa_revolutionary_cells.dds | GFX_goal_012_africa_revolutionary_cells | Revolutionary Congress | Print shop and rail depot |
| goal_012_africa_crown_regalia | Focus icon | 94x86 | Generated with source-informed motifs | gfx/interface/goals/012_africa/goal_012_africa_crown_regalia.dds | GFX_goal_012_africa_crown_regalia | Crown route | Royal umbrella, gold weights, court drum |
| goal_012_africa_continental_command | Focus icon | 94x86 | Generated | gfx/interface/goals/012_africa/goal_012_africa_continental_command.dds | GFX_goal_012_africa_continental_command | Command route | Field radio and soldiers |
| goal_012_africa_sacred_soil | Focus icon | 94x86 | Generated | gfx/interface/goals/012_africa/goal_012_africa_sacred_soil.dds | GFX_goal_012_africa_sacred_soil | Sacred Soil | Baobab, well, heritage stones |
| goal_012_africa_black_star_lanes | Focus icon | 94x86 | Generated | gfx/interface/goals/012_africa/goal_012_africa_black_star_lanes.dds | GFX_goal_012_africa_black_star_lanes | Black Star Return | Ocean liner and port crane |
| goal_012_africa_deep_green_covenant | Focus icon | 94x86 | Generated | gfx/interface/goals/012_africa/goal_012_africa_deep_green_covenant.dds | GFX_goal_012_africa_deep_green_covenant | Deep Green | Forest canopy, storm light, nonhuman signs |
| goal_012_africa_restored_polities | Focus icon | 94x86 | Generated with sourced motif review | gfx/interface/goals/012_africa/goal_012_africa_restored_polities.dds | GFX_goal_012_africa_restored_polities | Restoration branch | Several regional symbols, no unreadable text |
| goal_012_africa_scramble_response | Focus icon | 94x86 | Generated | gfx/interface/goals/012_africa/goal_012_africa_scramble_response.dds | GFX_goal_012_africa_scramble_response | Post-unification branch | Ships, coastline, mobilized defenders |

### Idea and national spirit icons

| Asset id | Type | Target size | Source mode | Proposed final DDS path | Proposed sprite | Visual direction |
| --- | --- | --- | --- | --- | --- | --- |
| idea_012_africa_unfinished_mandate | Idea icon | 64x64 | Generated | gfx/interface/ideas/012_africa/idea_012_africa_unfinished_mandate.dds | GFX_idea_012_africa_unfinished_mandate | Torn banner being stitched |
| idea_012_africa_charter_services | Idea icon | 64x64 | Generated | gfx/interface/ideas/012_africa/idea_012_africa_charter_services.dds | GFX_idea_012_africa_charter_services | Service seal, rail, clinic |
| idea_012_africa_liberation_congress | Idea icon | 64x64 | Generated | gfx/interface/ideas/012_africa/idea_012_africa_liberation_congress.dds | GFX_idea_012_africa_liberation_congress | Press and clenched banner |
| idea_012_africa_continental_regalia | Idea icon | 64x64 | Generated with source review | gfx/interface/ideas/012_africa/idea_012_africa_continental_regalia.dds | GFX_idea_012_africa_continental_regalia | Regalia chest |
| idea_012_africa_command_state | Idea icon | 64x64 | Generated | gfx/interface/ideas/012_africa/idea_012_africa_command_state.dds | GFX_idea_012_africa_command_state | Field radio and rail star |
| idea_012_africa_land_councils | Idea icon | 64x64 | Generated | gfx/interface/ideas/012_africa/idea_012_africa_land_councils.dds | GFX_idea_012_africa_land_councils | Well and meeting circle |
| idea_012_africa_returnee_network | Idea icon | 64x64 | Generated | gfx/interface/ideas/012_africa/idea_012_africa_returnee_network.dds | GFX_idea_012_africa_returnee_network | Port and star |
| idea_012_africa_deep_green_pressure | Idea icon | 64x64 | Generated | gfx/interface/ideas/012_africa/idea_012_africa_deep_green_pressure.dds | GFX_idea_012_africa_deep_green_pressure | Forest seal with dark outline |

### Decision and category icons

| Asset id | Type | Target size | Source mode | Proposed final DDS path | Proposed sprite | Related system |
| --- | --- | --- | --- | --- | --- | --- |
| decision_category_012_africa_charter_league | Decision category icon | Pattern size to verify | Generated | gfx/interface/decisions/012_africa/decision_category_012_africa_charter_league.dds | GFX_decision_category_012_africa_charter_league | Charter League |
| decision_category_012_africa_regional_integration | Decision category icon | Pattern size to verify | Generated | gfx/interface/decisions/012_africa/decision_category_012_africa_regional_integration.dds | GFX_decision_category_012_africa_regional_integration | Integration |
| decision_category_012_africa_diaspora_lanes | Decision category icon | Pattern size to verify | Generated | gfx/interface/decisions/012_africa/decision_category_012_africa_diaspora_lanes.dds | GFX_decision_category_012_africa_diaspora_lanes | Black Star Return |
| decision_012_africa_invite_member | Decision icon | 32x32 | Generated | gfx/interface/decisions/012_africa/decision_012_africa_invite_member.dds | GFX_decision_012_africa_invite_member | League invitation |
| decision_012_africa_defend_member | Decision icon | 32x32 | Generated | gfx/interface/decisions/012_africa/decision_012_africa_defend_member.dds | GFX_decision_012_africa_defend_member | Member defense |
| decision_012_africa_federal_vote | Decision icon | 32x32 | Generated | gfx/interface/decisions/012_africa/decision_012_africa_federal_vote.dds | GFX_decision_012_africa_federal_vote | Federal accession |
| decision_012_africa_restore_polity | Decision icon | 32x32 | Generated with source review | gfx/interface/decisions/012_africa/decision_012_africa_restore_polity.dds | GFX_decision_012_africa_restore_polity | Restored polities |
| decision_012_africa_open_lane | Decision icon | 32x32 | Generated | gfx/interface/decisions/012_africa/decision_012_africa_open_lane.dds | GFX_decision_012_africa_open_lane | Diaspora shipping |
| decision_012_africa_escort_convoy | Decision icon | 32x32 | Generated | gfx/interface/decisions/012_africa/decision_012_africa_escort_convoy.dds | GFX_decision_012_africa_escort_convoy | Diaspora shipping |
| decision_012_africa_housing_works | Decision icon | 32x32 | Generated | gfx/interface/decisions/012_africa/decision_012_africa_housing_works.dds | GFX_decision_012_africa_housing_works | Settlement |
| decision_012_africa_scramble_sanctions | Decision icon | 32x32 | Generated | gfx/interface/decisions/012_africa/decision_012_africa_scramble_sanctions.dds | GFX_decision_012_africa_scramble_sanctions | Outside reaction |
| decision_012_africa_high_chaos_contain | Decision icon | 32x32 | Generated | gfx/interface/decisions/012_africa/decision_012_africa_high_chaos_contain.dds | GFX_decision_012_africa_high_chaos_contain | High-chaos containment |

### Country flags and portraits

| Package | Asset need | Source mode | Notes |
| --- | --- | --- | --- |
| Africa unifier cosmetic identity | Base cosmetic flag and ideology variants | Generated alternate-history, unless route uses sourced symbol | Keep original country flag untouched unless cosmetic tag changes |
| Azania | Civil-war side flag, leader or council portrait | Generated, with historical symbol research if using real motifs | Direct map name |
| South Africa loyalist emergency | Optional emergency flag or portrait | Existing assets plus generated emergency variant if needed | Do not overwrite base flag |
| Aksum | Flag variants and leader portrait if restored | Source historical motifs, generate fictional leaders | Real historical portraits only if specific real leader is used |
| Kush | Flag variants and symbolic portrait or council | Source-informed symbols, generated fictional art | Heritage source notes required |
| Makuria | Flag variants | Source review or generated historically grounded motif | Avoid fabricated final claims |
| Kanem-Bornu | Flag variants and leader portrait | Source review for symbols, generated fictional leader if needed | Sultanate route needs direct name |
| Songhai | Flag variants and council portrait | Source review and generated variants | Manuscript motifs should avoid readable fake text |
| Oyo | Flag variants and leader portrait | Source review, generated variants | Cavalry and court motifs |
| Benin or Edo | Flag variants | Source review due court symbols | Avoid crude appropriation of specific art without source |
| Asante | Flag variants | Source review for royal symbols | Golden Stool direction requires care |
| Kongo | Flag variants and leader portrait | Source review for symbols | Generated fictional variants allowed |
| Luba and Lunda | Flag variants | Source review or generated historically grounded variants | Record uncertainty |
| Great Zimbabwe and Mutapa | Flag variants | Source review and generated variants | Great Zimbabwe art can use UNESCO-inspired stone direction |
| Kilwa | Flag variants | Source review for sultanate and Swahili coastal motifs | UNESCO Kilwa source direction |
| Buganda, Merina, Sokoto, Futa Jallon, Zulu | Flag variants and portraits as needed | Source historical flags if attested, otherwise documented generated variants | No office-like country names |
| High-chaos actors | Emblems, portraits, route flags | Generated | Must look nonhuman, supernatural, or abstract |

### Report and super-event image directions

| Asset id | Type | Target size | Source mode | Proposed final DDS path | Sprite | Direction |
| --- | --- | --- | --- | --- | --- | --- |
| report_event_012_africa_first_proclamation | Report image | 210x176 | Generated documentary style | gfx/event_pictures/012_africa/report_event_012_africa_first_proclamation.dds | GFX_report_event_012_africa_first_proclamation | Crowd and banners at first proclamation |
| report_event_012_africa_rsa_civil_war | Report image | 210x176 | Generated documentary style | gfx/event_pictures/012_africa/report_event_012_africa_rsa_civil_war.dds | GFX_report_event_012_africa_rsa_civil_war | Rail guards, port defense, civil split |
| report_event_012_africa_member_defense | Report image | 210x176 | Generated documentary style | gfx/event_pictures/012_africa/report_event_012_africa_member_defense.dds | GFX_report_event_012_africa_member_defense | League troops defending member capital |
| report_event_012_africa_return_arrival | Report image | 210x176 | Generated documentary style | gfx/event_pictures/012_africa/report_event_012_africa_return_arrival.dds | GFX_report_event_012_africa_return_arrival | Ship arrivals and port families |
| report_event_012_africa_restored_polity | Report image | 210x176 | Generated or sourced depending on polity | gfx/event_pictures/012_africa/report_event_012_africa_restored_polity.dds | GFX_report_event_012_africa_restored_polity | Restoration ceremony with source-informed symbols |
| report_event_012_africa_deep_green_sign | Report image | 210x176 | Generated | gfx/event_pictures/012_africa/report_event_012_africa_deep_green_sign.dds | GFX_report_event_012_africa_deep_green_sign | Forest anomaly, nonhuman traces |
| super_event_012_africa_is_one_image | Super-event image | 457x328 | Generated unless research demands source | gfx/super_events/012_africa/super_event_012_africa_is_one_image.dds | GFX_super_event_012_africa_is_one_image | Continental public moment, title research required |
| super_event_012_africa_scramble_response_image | Super-event image | 457x328 | Generated or sourced montage direction | gfx/super_events/012_africa/super_event_012_africa_scramble_response_image.dds | GFX_super_event_012_africa_scramble_response_image | Outside panic and African mobilization, title research required |
| super_event_012_africa_world_is_one_image | Super-event image | 457x328 | Generated symbolic world-end | gfx/super_events/012_africa/super_event_012_africa_world_is_one_image.dds | GFX_super_event_012_africa_world_is_one_image | Terminal world unity conflict, title research required |

### Animated assets

| Asset id | Target | Frame plan direction | Static fallback | Animated sprite | Use |
| --- | --- | --- | --- | --- | --- |
| africa_charter_league_seal | Decision category or scripted GUI | 8 frames, soft seal activation, no transform-only loop | GFX_africa_charter_league_seal | GFX_africa_charter_league_seal_animated | Shows League category active and stable |
| africa_regional_integration_meter | Scripted GUI meter | 8 to 12 frames for warning state if pressure is high | GFX_africa_regional_integration_meter | GFX_africa_regional_integration_meter_animated | Shows integration danger state |
| africa_black_star_port_seal | Diaspora lane UI | 8 frames, port lantern and ship movement through real source frames | GFX_africa_black_star_port_seal | GFX_africa_black_star_port_seal_animated | Shows lane open or convoy active |
| africa_deep_green_covenant_seal | High-chaos route UI | 10 frames, forest light and animal silhouettes from planned source frames | GFX_africa_deep_green_covenant_seal | GFX_africa_deep_green_covenant_seal_animated | Shows covenant pressure |
| africa_living_statue_portrait_overlay | Leader or event portrait overlay | 10 frames, stone light and dust drawn per source frame | GFX_africa_living_statue_portrait_overlay | GFX_africa_living_statue_portrait_overlay_animated | Shows supernatural actor reveal |

All animated assets must follow the frame-animation workflow. A GIF is preview only. Final game asset is a frame-sheet DDS with static fallback.

## Prompt update needs

The asset prompt should be expanded with:
- every asset table above
- source mode for each flag and portrait
- reference folder to inspect for every asset type
- target sizes
- exact proposed paths and sprite names
- animation brief for each animated asset
- source documentation requirements
- no generated real leader portraits
- no historical flag invention without source review

The achievement prompt should be expanded with:
- the achievement suite table above
- tracking flags and variables
- disqualifier logic
- icon ids and paths
- hidden and secret achievement handling
- route coverage requirements

The coding prompt should be expanded with:
- target-state mechanics
- regional integration stages
- route group packs
- cleanup requirements
- AI route weights
- no instant annexation
- no free continent cores
- full reporting for skipped routes or assets
