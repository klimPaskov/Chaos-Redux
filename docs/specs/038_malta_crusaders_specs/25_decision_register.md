# Detailed decision and mission register

## Register use

This register defines the required action families and owns the row-level detail.
The principles and phase structure are in `07_decisions_missions_and_failure.md`.
Final IDs and numbers belong to implementation.
Every row needs route-aware visibility, clear costs, AI behavior, cleanup, and localisation.
"Standing" means Command Standing from `04_crusade_council_mechanic.md`.

## Crusade Council decisions

| Working ID | Action | Phase | Main requirement | Cost families | Main outcome | Failure or risk |
| --- | --- | --- | --- | --- | --- | --- |
| `council_review_status` | Review the Crusade Council | all | Event 38 actor | none | opens the window | none |
| `council_convene_joint_command` | Convene Joint Command | opening onward | Cohesion 50 or more, two seated orders | command power, army XP, planning time | Cohesion and mixed command bonus | incident and a Standing step for 90 days |
| `council_accept_demand` | Accept Order Demand | demand | open demand | demand-specific, max four | fulfils the request | none |
| `council_compromise_demand` | Compromise on Order Demand | demand | open demand, not used by this order for this demand | half the request | half the Cohesion gain | grievance unchanged |
| `council_refuse_demand` | Refuse Order Demand | demand | open demand | none | keeps resources or territory | Cohesion loss, grievance up by 1 |
| `council_arbitrate_jerusalem` | Arbitrate Jerusalem | Holy Land held | Jerusalem held 120 days | concessions | chooses the custody model | major rival grievance |
| `council_reform_government` | Reform the Crusade Council | route settlement | route focus, Functional or better, no open incident | political commitment | transforms government and ideas | locks incompatible routes |
| `council_name_dominant_order` | Name the Dominant Order | political | route focus, order path proof, Functional or better | Cohesion | dominant-order package | rivals weaken |
| `council_confirm_confederation` | Confirm the Confederation | political | Cohesion 75 or more, four seated orders | civilian burden | confederation government | slower command |
| `council_restore_civilian_courts` | Restore Civilian Courts | civilian route | Malta secure | political power, temporary command penalty | local stability and Legitimacy | order resistance |
| `council_request_papal_arbitration` | Request Papal Arbitration | diplomacy | valid Pope | diplomatic obligation | resolves one incident or dispute | Papal influence rises |
| `council_publish_accounts` | Publish the Order Accounts | reform | Templar treasury active | corruption exposure | Legitimacy and trust | scandal if records are bad |
| `council_seize_treasury` | Seize an Order Treasury | harsh route | Functional or better, order not dominant | command power, stability | equipment or funds | Cohesion collapse risk |

Incident responses (concede, arbitrate, suppress) are event options, not decisions.

## Logistics decisions

| Working ID | Action | Main requirement | Cost families | Duration | Main outcome | Risk |
| --- | --- | --- | --- | --- | --- | --- |
| `logistics_escort_sea_road` | Escort the Sea Road | valid Malta to bridge route | fuel, convoys, naval commitment | 120 to 180 days | protected supply | convoy losses |
| `logistics_repair_holy_land_rail` | Repair the Holy Land Rail | control of named corridor | trains, support equipment, civilian burden | 120 to 180 days | rail, depot, and supply improvement | sabotage or delay |
| `logistics_fortify_selected_port` | Fortify a Port | selected eligible coastal state, Malta included | civilian burden, equipment, time | 140 to 220 days | port repair and coastal defence | local resistance |
| `logistics_emergency_air_bridge` | Establish Emergency Air Bridge | blocked land or sea supply | transport aircraft, fuel, air commitment | 60 to 100 days | temporary supply | aircraft losses |

## Formation and equipment decisions

| Working ID | Action | Requirement | Cost families | Outcome | Limits |
| --- | --- | --- | --- | --- | --- |
| `raise_armored_knight_banner` | Raise Armored Knight Banner | provider, armour equipment, cap | manpower, knight armour, infantry equipment, army XP | trained formation mission | dynamic cap |
| `raise_mounted_knight_column` | Raise Mounted Knight Column | provider, remount capacity from equipment and focus | manpower, infantry equipment, support equipment, army XP | mobile formation | production cap |
| `raise_ranged_company` | Raise Ranged Company | bow equipment, crossbow technology selects the variant | manpower, ranged equipment, training time | Archer or Crossbow formation | regional recruitment |
| `raise_siege_host` | Raise Siege Host | siege equipment and technology | manpower, siege equipment, support equipment, trains | siege formation | one per workshop tier |
| `raise_blessed_guard` | Raise Blessed Guard | Evolution III, Legitimacy 65 or more, sponsor, cap | manpower, elite equipment, army XP | elite formation | strict cap |
| `train_crusader_engineers` | Train Crusader Engineers | support technology | support equipment, army XP, manpower | support company capacity | training duration |
| `convert_captured_equipment` | Convert Captured Equipment | captured stock of a selected family | captured equipment, factory burden | crusader equipment at a conversion loss | no value-gain loop |
| `request_foreign_equipment` | Request Foreign Equipment | sponsor | diplomatic obligation, convoys | bounded package | cooldown and refusal memory |

## Campaign target decisions

| Working ID | Action | Requirement | Cost families | Outcome |
| --- | --- | --- | --- | --- |
| `campaign_select_target` | Select Regional Objective | valid target pool, Functional or better | none | human selected target, closable |
| `campaign_issue_ultimatum` | Issue Crusader Ultimatum | credible force, selected target | Legitimacy risk | acceptance, bargain, or refusal |
| `campaign_launch_regional_crusade` | Launch Regional Crusade | selected target, supplied forces, crossing capacity if overseas | command power, equipment reserve, convoys and fuel if overseas | limited war or intervention |
| `campaign_request_papal_blessing` | Request Papal Blessing | Papal relation | diplomatic obligation | Legitimacy and volunteers, Papal conditions |
| `campaign_call_order_chapters` | Call Foreign Chapters | Evolution I | convoys, equipment, sponsor obligation | officers and volunteers, cooldown |

## Settlement decisions

| Working ID | Action | Requirement | Main effect | Tradeoff |
| --- | --- | --- | --- | --- |
| `settle_direct_commandery` | Establish Direct Commandery | stable control | direct output and military access | resistance and administration |
| `settle_order_grant` | Grant Territory to an Order | valid seated order and region | order headquarters and specialist recruitment | autonomy and rival grievance |
| `settle_principality` | Charter a Principality | Evolution II, Recognized standing, valid country package | subject creation | lower direct output, succession risk |
| `settle_local_restoration` | Restore Local Christian Government | valid identity and support | local government and Legitimacy | reduced direct control |
| `settle_papal_administration` | Establish Papal Administration | valid Pope | Papal subject and Legitimacy | church disputes and political rigidity |
| `settle_return_under_treaty` | Return Territory under Treaty | valid former owner | peace, lower Condemnation, small Chaos reduction | territorial loss and a Standing step for 90 days |
| `settle_integrate_commandery` | Integrate Commandery | compliance, route, Recognized standing, time | staged core or full administration | high cost and resistance risk |
| `settle_revise_charter` | Revise Principality Charter | active principality | changes obligations, tribute, or autonomy | loyalty consequence |
| `settle_dissolve_failed_subject` | Dissolve Failed Principality | invalid or collapsed subject | transfers territory and cleans up | Legitimacy and local unrest |

## Relic decisions

| Working ID | Action | Requirement | Cost families | Outcome | Risk |
| --- | --- | --- | --- | --- | --- |
| `relic_sponsor_expedition` | Sponsor Relic Expedition | Evolution III, valid location, fewer than three claims | convoys, civilian burden, equipment | delayed discovery of a claim | fraud or foreign competition |
| `relic_examine_claim` | Examine the Claim | claim in custody | political or scientific capacity | fixes the claim as accepted, disputed, or exposed | scandal |
| `relic_display_jerusalem` | Display in Jerusalem | Jerusalem held, custody | security commitment | pilgrimage and Legitimacy | theft risk |
| `relic_transfer_custody` | Transfer Custody | an order, Jerusalem, or the Pope | custody loss | order benefit or Papal support | rival grievance or reduced Malta control |

## Principality decisions

| Working ID | Action | Requirement | Cost families | Outcome |
| --- | --- | --- | --- | --- |
| `principality_request_levy` | Request Levy | valid charter | local manpower or equipment, goodwill | contribution mission |
| `principality_send_relief` | Send Relief | threatened subject | equipment, convoys, fuel | loyalty and defence |
| `principality_arbitrate_succession` | Arbitrate Succession | succession crisis | political power, Legitimacy, concession | selects the candidate |
| `principality_enforce_charter` | Enforce Charter | refusal | command power, equipment | compliance or crisis |
| `principality_begin_integration` | Begin Integration | full proof, Recognized standing | civilian burden, time | staged integration mission |
| `principality_federate_members` | Form Principality Federation | route and member proof | political commitment | joint structure |

Tribute and autonomy changes are made through `settle_revise_charter`.

## Eleventh Crusade decisions

| Working ID | Action | Phase | Cost families | Outcome |
| --- | --- | --- | --- | --- |
| `eleventh_evacuate_exposed_orders` | Evacuate Exposed Orders | survivors | convoys, fuel, command | saves cadres |
| `eleventh_fortify_malta` | Fortify Malta | survivors | civilian burden, support equipment | island survival and consolidated stock |
| `eleventh_seek_refuge` | Seek Temporary Refuge | survivors | diplomatic concession | foreign base or refusal |
| `eleventh_call_volunteers` | Call for Volunteers | rebuild | convoys, obligation | manpower and officers |
| `eleventh_rebuild_transports` | Rebuild Transports and Workshops | rebuild | dockyard burden, fuel, civilian capacity | invasion capacity and production recovery |
| `eleventh_select_landing` | Select New Landing | rebuild | none | target pool |
| `eleventh_launch` | Launch the Eleventh Crusade | invasion ready | command power, reserve equipment, fleet staging | landing and hold mission |
| `eleventh_accept_fortress_malta` | Accept a Fortress Malta Settlement | final failure | ambition | stable compact ending |
| `eleventh_restore_jerusalem` | Restore the Holy Land Command | successful return | administration and equipment | returns the normal campaign |

## Holy World preparation decisions

| Working ID | Action | Requirement | Cost families | Outcome |
| --- | --- | --- | --- | --- |
| `holy_world_select_continent` | Select Continental Proof | valid Pope, 800 Chaos | none | selected contract |
| `holy_world_bind_subject` | Bind Papal Subject | valid aligned country | autonomy concession, diplomacy | approved subject state |
| `holy_world_invite_government` | Invite Believer Government | valid target | equipment, guarantee, political obligation | alignment or refusal, local order chapter on acceptance |
| `holy_world_build_continental_office` | Build Continental Campaign Office | selected continent | civilian burden, equipment, time | proof and logistics |
| `holy_world_reorganize_principality` | Reorganize as Papal Subject | valid principality | charter change | terminal preparation |
| `holy_world_dissolve_preparation` | Dissolve Holy World Preparation | not terminal | Legitimacy loss | closes the route and may reduce Chaos |

Pre-activation stockpiling of terminal reserves is not offered, because it would let the player bank terminal strength before the proof is earned.

## Holy World terminal decisions

| Working ID | Action | Requirement | Cost families | Outcome |
| --- | --- | --- | --- | --- |
| `holy_world_call_believer_contribution` | Call Believer Contribution | active terminal, valid ally | subject or alliance obligation | bounded equipment or unit aid |
| `holy_world_build_front_supply` | Build Front Supply | selected active front | civilian burden, trains, equipment | hubs and rail |
| `holy_world_raise_papal_formation` | Raise Papal Formation | provider and cap | manpower, equipment, XP | terminal unit |
| `holy_world_demand_submission` | Demand Submission | valid nonbeliever | Legitimacy and threat | submit, bargain, or resist |
| `holy_world_open_regional_campaign` | Open Regional Campaign | valid region | command, logistics, reserves | queues wars |
| `holy_world_settle_conquest` | Settle Conquered Country | capitulated target | administration | annex, subject, or restoration |

Defending Rome and Jerusalem are the terminal missions below.

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
| `mission_hold_four_anchors` | hold Malta, Jerusalem, the bridge, and the supply port | 120 to 180 days | Recognized standing and route unlock | opening crisis worsens |
| `mission_keep_sea_road_open` | maintain convoy and port access | 120 to 180 days | supply status | convoy losses and a Standing step |
| `mission_guard_jordan_corridor` | supplied divisions and control | 120 to 180 days | rail security | siege and local resistance |
| `mission_protect_grand_harbour` | garrison and naval defence | 120 days | fortress benefit | damage and supply crisis |
| `mission_joint_order_offensive` | two order families on a named front | 90 to 150 days | Cohesion and victory bonus | blame incident |
| `mission_complete_port_project` | hold the target during construction | project duration | port completed | partial loss and delay |
| `mission_principality_obligation` | subject fulfils a charter duty | 120 to 240 days | loyalty and contribution | succession or autonomy pressure |
| `mission_protect_pilgrims` | secure the route and avoid major civilian harm | 120 days | Legitimacy | scandal and resistance |
| `mission_evacuation` | move designated formations and civilians | 60 to 100 days | survivors preserved | trapped population and equipment loss |
| `mission_rebuild_eleventh_force` | reach a dynamic equipment and formation proof | 180 to 365 days | invasion route | permanent route weakening |
| `mission_hold_new_foothold` | hold the new landing area | 120 to 180 days | comeback success | second failure settlement |
| `mission_full_continent` | exact curated continent control | stabilization period | Holy World Ready | proof pauses or resets |
| `mission_defend_rome_terminal` | prevent the fall of Rome | 90 days | terminal cohesion | emergency succession |
| `mission_defend_jerusalem_terminal` | prevent the fall of Jerusalem | 90 days | Legitimacy and recruitment | terminal Legitimacy loss |

## Register acceptance

Implementation can merge rows only when the merged action preserves every route, target, cost, AI, result, and cleanup role.
Any removed or materially changed row must be reported in route coverage and the completion report.
