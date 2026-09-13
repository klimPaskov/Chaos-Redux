# Detailed decision and mission register

## Register use

This register defines the required action families. Final IDs and numbers belong to implementation. Every row needs route-aware visibility, clear costs, AI behavior, cleanup, and localisation.

## Crusade Council decisions

| Working ID | Action | Phase | Main requirement | Cost families | Main outcome | Failure or risk |
| --- | --- | --- | --- | --- | --- | --- |
| `council_review_status` | Review the Crusade Council | all | Event 38 actor | none | opens GUI and status | none |
| `council_convene_joint_command` | Convene Joint Command | opening onward | two active orders | command power, army XP, planning time | Cohesion and mixed command | public dispute |
| `council_accept_demand` | Accept Order Demand | demand | active demand | demand-specific, max four | fulfils charter | rival grievance |
| `council_negotiate_demand` | Negotiate Order Demand | demand | active demand, no prior deferral | political or command cost, concession | reduced cost or compromise | partial grievance |
| `council_refuse_demand` | Refuse Order Demand | demand | active demand | Authority or Cohesion consequence | keeps resources or territory | incident pressure |
| `council_defer_demand` | Defer Order Demand | demand | no prior deferral | Authority and deadline pressure | short extension | stronger refusal consequence |
| `council_reassign_headquarters` | Reassign Headquarters | governance | valid selected state | trains, support equipment, civilian burden | moves order HQ | temporary disruption |
| `council_arbitrate_jerusalem` | Arbitrate Jerusalem | Holy Land held | stable Jerusalem control | Authority, legitimacy, concessions | chooses custody model | major rival grievance |
| `council_reform_government` | Reform the Crusade Council | route settlement | route focus and thresholds | political commitment | transforms government and ideas | locks incompatible route |
| `council_name_dominant_order` | Name the Dominant Order | political | route focus and order proof | Cohesion, Authority | dominant-order package | rivals weaken |
| `council_confirm_confederation` | Confirm the Confederation | political | high Cohesion and several orders | civilian burden, authority compromise | confederation government | slower command |
| `council_restore_civilian_courts` | Restore Civilian Courts | civilian route | Malta secure | political power, temporary command penalty | local stability and legitimacy | order resistance |
| `council_request_papal_arbitration` | Request Papal Arbitration | diplomacy | valid Pope | diplomatic obligation | resolves one dispute | Papal influence rises |
| `council_publish_accounts` | Publish the Order Accounts | reform | treasury system active | corruption exposure | legitimacy and trust | scandal if records are bad |
| `council_seize_treasury` | Seize an Order Treasury | harsh route | high Authority | command power, stability | equipment or funds | Cohesion collapse risk |

## Logistics decisions

| Working ID | Action | Main requirement | Cost families | Duration | Main outcome | Risk |
| --- | --- | --- | --- | --- | --- | --- |
| `logistics_escort_sea_road` | Escort the Sea Road | valid Malta to bridge route | fuel, convoys, naval commitment | 120 to 180 days | protected supply | convoy losses |
| `logistics_repair_holy_land_rail` | Repair the Holy Land Rail | control named corridor | trains, support equipment, civilian burden | 120 to 180 days | rail and supply improvement | sabotage or delay |
| `logistics_fortify_selected_port` | Fortify Selected Port | selected eligible coastal state | civilian burden, equipment, time | 140 to 220 days | port and coastal defence | local resistance |
| `logistics_build_depot` | Build a Crusader Depot | valid supply region | trains, support equipment, civilian burden | 120 to 180 days | supply node or depot | attack can interrupt |
| `logistics_emergency_air_bridge` | Establish Emergency Air Bridge | blocked land or sea supply | transport aircraft, fuel, air commitment | 60 to 100 days | temporary supply | aircraft losses |
| `logistics_requisition_transport` | Requisition Local Transport | controlled populated region | Authority consequence, local cooperation | 60 to 90 days | short supply boost | migration and resistance |
| `logistics_contract_foreign_convoys` | Contract Foreign Convoys | valid sponsor | political obligation, civilian burden | 120 days | convoy grant or lease | sponsor influence |
| `logistics_clear_mines` | Clear the Approaches | hostile mines or naval danger | navy XP, fuel, escort commitment | 90 to 140 days | safer port access | ship damage |
| `logistics_repair_grand_harbour` | Repair the Grand Harbour | Malta damaged | civilian burden, steel or equipment | 120 to 200 days | dockyard and repair recovery | delayed naval support |
| `logistics_disperse_workshops` | Disperse Order Workshops | bombing threat | civilian burden, support equipment | 100 to 160 days | production resilience | lower short-term output |

## Formation and equipment decisions

| Working ID | Action | Requirement | Cost families | Outcome | Limits |
| --- | --- | --- | --- | --- | --- |
| `raise_armored_knight_banner` | Raise Armored Knight Banner | provider, armour equipment, cap | manpower, knight armour, infantry equipment, army XP | trained formation mission | dynamic cap |
| `raise_mounted_knight_column` | Raise Mounted Knight Column | provider, remount capacity | manpower, infantry equipment, support equipment, army XP | mobile formation | remount cap |
| `raise_archer_levy` | Raise Archer Levy | bow equipment | manpower, war bows, training time | ranged formation | regional recruitment |
| `raise_crossbow_company` | Raise Crossbow Company | crossbow technology | manpower, crossbow equipment, support equipment | stronger ranged formation | production cap |
| `raise_siege_host` | Raise Siege Host | workshop and technology | manpower, siege equipment, support equipment, trains | siege formation | one per workshop tier |
| `raise_blessed_guard` | Raise Blessed Guard | Evolution III, legitimacy, cap | manpower, elite equipment, army XP, legitimacy consequence | elite formation | strict cap |
| `convert_captured_rifles` | Convert Captured Rifles | captured stock | captured equipment, factory burden | Event 38 equipment | conversion loss |
| `convert_captured_artillery` | Adapt Captured Artillery | captured artillery, siege route | artillery, support equipment, factory burden | siege equipment | no value gain loop |
| `establish_siege_workshop` | Establish Siege Workshop | valid industrial state | civilian burden, steel or equipment, support equipment | production capacity | bounded per region |
| `create_remount_service` | Create Remount Service | rural or sponsor capacity | manpower, equipment, civilian burden | mounted sustainment | famine vulnerability |
| `request_foreign_equipment` | Request Foreign Equipment | sponsor | diplomatic obligation, convoys | bounded package | cooldown and refusal memory |
| `train_crusader_engineers` | Train Crusader Engineers | support tech | support equipment, army XP, manpower | support company capacity | training duration |

## Campaign target decisions

| Working ID | Action | Requirement | Cost families | Outcome |
| --- | --- | --- | --- | --- |
| `campaign_select_target` | Select Regional Objective | valid target pool | none | human selected target |
| `campaign_hide_target` | Close Regional Objective | active selection | none | clears human selection |
| `campaign_survey_coast` | Survey the Coast | coastal target | fuel, navy or air XP, intelligence | target data and preparation |
| `campaign_contact_local_allies` | Contact Local Allies | valid local actor | political power, equipment, exposure risk | support or negotiation |
| `campaign_prepare_landing_fleet` | Prepare Landing Fleet | port and convoys | convoys, fuel, dockyard burden, time | invasion window |
| `campaign_stock_forward_depots` | Stock Forward Depots | selected theater | trains, support equipment, fuel | supply readiness |
| `campaign_issue_ultimatum` | Issue Crusader Ultimatum | Authority and force proof | legitimacy or political risk | acceptance, bargain, or war preparation |
| `campaign_launch_regional_crusade` | Launch Regional Crusade | completed preparation | command power, equipment reserve | limited war or intervention |
| `campaign_request_papal_blessing` | Request Papal Blessing | Papal relation | diplomatic obligation | legitimacy and volunteers | Papal conditions |
| `campaign_call_order_chapters` | Call Foreign Chapters | Evolution I | convoys, equipment, sponsor obligation | officers and volunteers | cooldown |

## Settlement decisions

| Working ID | Action | Requirement | Main effect | Tradeoff |
| --- | --- | --- | --- | --- |
| `settle_direct_commandery` | Establish Direct Commandery | stable control | direct output and military access | resistance and administration |
| `settle_order_grant` | Grant Territory to an Order | valid order and region | order HQ and specialist recruitment | autonomy and rival grievance |
| `settle_principality` | Charter a Principality | Evolution II, valid country package | subject creation | lower direct output, succession risk |
| `settle_local_restoration` | Restore Local Christian Government | valid identity and support | local government and legitimacy | reduced direct control |
| `settle_papal_administration` | Establish Papal Administration | valid Pope | Papal subject and legitimacy | church disputes and political rigidity |
| `settle_return_under_treaty` | Return Territory under Treaty | valid former owner | peace and diplomatic relief | Authority and territorial loss |
| `settle_integrate_commandery` | Integrate Commandery | compliance, route, time | staged core or full administration | high cost and resistance risk |
| `settle_revise_charter` | Revise Principality Charter | active principality | changes obligations | loyalty consequence |
| `settle_dissolve_failed_subject` | Dissolve Failed Principality | invalid or collapsed subject | transfers territory and cleanup | legitimacy and local unrest |

## Relic decisions

| Working ID | Action | Requirement | Cost families | Outcome | Risk |
| --- | --- | --- | --- | --- | --- |
| `relic_sponsor_expedition` | Sponsor Relic Expedition | Evolution III, valid location | convoys, civilian burden, equipment, intelligence | delayed outcome | fraud or foreign competition |
| `relic_examine_claim` | Examine the Claim | relic in custody | political or scientific capacity | higher confidence or exposure | scandal |
| `relic_display_jerusalem` | Display in Jerusalem | control and custody | security, legitimacy commitment | pilgrimage and legitimacy | theft risk |
| `relic_transfer_order` | Transfer to an Order | active order | none or concession | order benefit | rival grievance |
| `relic_transfer_pope` | Transfer to the Pope | valid Pope | custody loss | Papal support | reduced Malta control |
| `relic_hide_disputed_object` | Remove from Public View | disputed relic | Authority or legitimacy cost | contains scandal | leak risk |
| `relic_recover_stolen` | Recover Stolen Relic | valid thief and route | intelligence, equipment, exposure | custody restored | diplomatic crisis |
| `relic_protect_pilgrimage` | Protect the Pilgrimage | route active | units, convoys, equipment | timed legitimacy mission | civilian harm if failed |

## Principality decisions

| Working ID | Action | Requirement | Cost families | Outcome |
| --- | --- | --- | --- | --- |
| `principality_review_obligations` | Review Obligations | active selected principality | none | details and target selection |
| `principality_request_levy` | Request Levy | valid charter | Authority, local manpower or equipment | contribution mission |
| `principality_send_relief` | Send Relief | threatened subject | equipment, convoys, fuel | loyalty and defence |
| `principality_arbitrate_succession` | Arbitrate Succession | succession crisis | political power, legitimacy, concession | selects candidate |
| `principality_reduce_tribute` | Reduce Tribute | burdened subject | direct income loss | loyalty and stability |
| `principality_enforce_charter` | Enforce Charter | refusal | command power, equipment, Authority | compliance or crisis |
| `principality_offer_autonomy` | Offer Greater Autonomy | low loyalty | direct control loss | stabilizes subject |
| `principality_begin_integration` | Begin Integration | full proof | civilian burden, Authority, time | staged integration mission |
| `principality_federate_members` | Form Principality Federation | route and member proof | political and Authority commitment | joint structure |

## Eleventh Crusade decisions

| Working ID | Action | Phase | Cost families | Outcome |
| --- | --- | --- | --- | --- |
| `eleventh_evacuate_exposed_orders` | Evacuate Exposed Orders | survivors | convoys, fuel, command | saves cadres |
| `eleventh_consolidate_equipment` | Consolidate Equipment | survivors | temporary organization loss | preserves stock |
| `eleventh_fortify_malta` | Fortify Malta | survivors | civilian burden, support equipment | island survival |
| `eleventh_seek_refuge` | Seek Temporary Refuge | survivors | diplomatic concession | foreign base or refusal |
| `eleventh_call_volunteers` | Call for Volunteers | rebuild | convoys, obligation | manpower and officers |
| `eleventh_rebuild_transports` | Rebuild Transports | rebuild | dockyard burden, fuel, civilian capacity | invasion capacity |
| `eleventh_reopen_workshops` | Reopen Workshops | rebuild | civilian burden, equipment | production recovery |
| `eleventh_select_landing` | Select New Landing | rebuild | none | target pool |
| `eleventh_secure_local_allies` | Secure Local Allies | invasion | equipment, political power, exposure | local support |
| `eleventh_stage_fleet` | Stage the Fleet | invasion | convoys, fuel, naval commitment | invasion readiness |
| `eleventh_launch` | Launch the Eleventh Crusade | invasion ready | command power, reserve equipment | war or landing |
| `eleventh_accept_fortress_malta` | Accept a Fortress Malta Settlement | final failure | Authority and ambition | stable compact ending |
| `eleventh_restore_jerusalem` | Restore the Holy Land Command | successful return | administration and equipment | returns normal campaign |

## Holy World preparation decisions

| Working ID | Action | Requirement | Cost families | Outcome |
| --- | --- | --- | --- | --- |
| `holy_world_select_continent` | Select Continental Proof | valid Pope, 800 Chaos | none | selected contract |
| `holy_world_bind_subject` | Bind Papal Subject | valid aligned country | autonomy concession, diplomacy | approved subject state |
| `holy_world_invite_government` | Invite Believer Government | valid target | equipment, guarantee, political obligation | alignment or refusal |
| `holy_world_found_foreign_order` | Found Foreign Order Chapter | valid target and Evolution I | equipment, convoys, legitimacy | local movement and units |
| `holy_world_build_continental_office` | Build Continental Campaign Office | selected continent | civilian burden, equipment, time | proof and logistics |
| `holy_world_reorganize_principality` | Reorganize as Papal Subject | valid principality | charter change | terminal preparation |
| `holy_world_prepare_terminal_reserves` | Prepare Terminal Reserves | ready route | equipment, manpower, factories | post-activation stock |
| `holy_world_dissolve_preparation` | Dissolve Holy World Preparation | not terminal | Authority and legitimacy loss | closes route and possible Chaos reduction |

## Holy World terminal decisions

| Working ID | Action | Requirement | Cost families | Outcome |
| --- | --- | --- | --- | --- |
| `holy_world_call_believer_contribution` | Call Believer Contribution | active terminal and valid ally | subject or alliance obligation | bounded equipment or unit aid |
| `holy_world_build_front_supply` | Build Front Supply | selected active front | civilian burden, trains, equipment | hubs and rail |
| `holy_world_raise_papal_formation` | Raise Papal Formation | provider and cap | manpower, equipment, XP | terminal unit |
| `holy_world_demand_submission` | Demand Submission | valid nonbeliever | legitimacy and threat | submit, bargain, resist |
| `holy_world_open_regional_campaign` | Open Regional Campaign | valid region | command, logistics, reserves | queues wars |
| `holy_world_settle_conquest` | Settle Conquered Country | capitulated target | Authority and administration | annex, subject, restoration |
| `holy_world_defend_rome` | Defend Rome | Rome threatened | units, equipment, command | emergency defence |
| `holy_world_defend_jerusalem` | Defend Jerusalem | Jerusalem threatened | units, equipment, command | emergency defence |

## Hidden Teutonic decisions

| Working ID | Action | Actor | Main outcome |
| --- | --- | --- | --- |
| `teutonic_open_negotiations` | Open Three-State Negotiations | Malta | hidden talks |
| `teutonic_demand_concession` | Demand Alliance Concession | each member | bargain state |
| `teutonic_accept_pact` | Accept the Pact | each member | assent |
| `teutonic_reject_pact` | Reject the Pact | each member | route closes or delays |
| `teutonic_form_faction` | Proclaim the Teutonic Order | Malta or agreed leader | faction and super-event |
| `teutonic_select_campaign` | Select Final Crusade Region | faction leader | regional campaign |
| `teutonic_recruit_multinational_knights` | Recruit Multinational Knights | valid members | capped formations |

## Atlantis decisions

| Working ID | Action | Requirement | Main outcome |
| --- | --- | --- | --- |
| `atlantis_accept_transformation` | Accept Atlantis | eligible Germany | betrayal and transformation |
| `atlantis_reject_transformation` | Reject Atlantis | human Germany | route block or delay |
| `atlantis_open_roman_campaign` | Open Roman Program Campaign | active Atlantis | regional targets |
| `atlantis_open_atlantic_campaign` | Open Atlantic Program Campaign | route progress | overseas targets |
| `atlantis_build_supreme_tank` | Build Supreme Armour Formation | technology and industry | expensive replacement formation |
| `atlantis_integrate_program_state` | Integrate Claimed State | controlled state and policy | actual core after proof |
| `atlantis_expand_repression` | Expand Repression Network | harsh route and shared site eligibility | camp system action |
| `atlantis_destroy_records` | Destroy Records | active evidence | cover-up and discovery risk |
| `atlantis_relocate_industry` | Relocate Industry to Atlantus | control and capacity | industry shift and civilian burden |

## Mission register

| Working ID | Objective | Duration band | Success | Failure |
| --- | --- | --- | --- | --- |
| `mission_hold_four_anchors` | hold Malta, Jerusalem, bridge, and supply port | 120 to 180 days | Authority and route unlock | opening crisis worsens |
| `mission_keep_sea_road_open` | maintain convoy and port access | 120 to 180 days | supply status | convoy and Authority loss |
| `mission_guard_jordan_corridor` | supplied divisions and control | 120 to 180 days | rail security | siege and local resistance |
| `mission_protect_grand_harbour` | garrison and naval defence | 120 days | fortress benefit | damage and supply crisis |
| `mission_joint_order_offensive` | two order families participate in a named front | 90 to 150 days | Cohesion and victory bonus | blame incident |
| `mission_complete_port_project` | hold target during construction | project duration | port completed | partial loss and delay |
| `mission_principality_obligation` | subject fulfils selected charter duty | 120 to 240 days | loyalty and contribution | succession or autonomy pressure |
| `mission_protect_pilgrims` | secure route and avoid major civilian harm | 120 days | Legitimacy | scandal and resistance |
| `mission_evacuation` | move designated formations and civilians | 60 to 100 days | survivors preserved | trapped population and equipment loss |
| `mission_rebuild_eleventh_force` | reach dynamic equipment and formation proof | 180 to 365 days | invasion route | permanent route weakening |
| `mission_hold_new_foothold` | hold new landing area | 120 to 180 days | comeback success | second failure settlement |
| `mission_full_continent` | exact curated continent control | stabilization period | Holy World Ready | proof pauses or resets |
| `mission_defend_rome_terminal` | prevent fall of Rome | 90 days | terminal cohesion | emergency succession |
| `mission_defend_jerusalem_terminal` | prevent fall of Jerusalem | 90 days | legitimacy and recruitment | terminal legitimacy loss |

## Register acceptance

Implementation can merge rows only when the merged action preserves every route, target, cost, AI, result, and cleanup role. Any removed or materially changed row must be reported in route coverage and the completion report.
