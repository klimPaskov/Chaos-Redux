# Event 31 Random Terror decision and mission matrix

## Matrix purpose

This matrix maps the accepted national response and territorial-actor actions into implementation-ready design rows.

Working IDs can be adjusted to match repository naming style.

The action identity, phase, purpose, cost family, outcome family, AI intent, and cleanup obligation should remain intact.

No action may show more than four spendable cost types.

## Government decisions

| Working decision ID | Phase | Visible target | Main requirements | Spendable cost families | Public result | Main risk or failure | AI priority | Cleanup |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `random_terror_establish_response_cell` | Immediate | country | active crisis, no response cell | command capacity, support equipment, temporary administration burden | unlocks coordinated response, improves intelligence quality, reveals active-state summary | delayed setup can miss the first operation window | high with several states or prior failure | remove after final recovery, preserve earned institutional upgrade when applicable |
| `random_terror_protect_transport` | Immediate and Active | one rail, port, hub, or corridor state | valid critical transport target | trains, fuel, support equipment, tied divisions | starts transport-protection mission and lowers disruption chance | other targets become less protected, committed forces strain fronts | highest for capital supply, fronts, hubs, ports | release units and temporary burden when mission ends or target invalidates |
| `random_terror_support_victims` | Immediate and Recovery | one affected state | civilian losses or service disruption | civilian factories, support equipment, trains or convoys, emergency manpower | restores services, raises legitimacy, reduces panic and copycat pressure | no direct cell removal, cost can weaken war economy | high after major civilian losses or low legitimacy | end state commitment after recovery, retain completed recovery flag |
| `random_terror_intelligence_sweep` | Immediate and Active | one active state or organization | response cell or accepted reduced-quality route | intelligence capacity, support equipment, command or manpower burden | raises breakthrough chance and raid precision | false lead, exposed informant, dormant relocation | high with legitimacy and available capacity | clear temporary intelligence window and invalid target |
| `random_terror_security_surge` | Immediate and Emergency | one active state | valid state, available forces | command power, fuel, support equipment, tied units | blocks immediate attack and raises local control | civilian harm, legitimacy loss, survivors relocate | high for capital or short deadline | release surge and unit requirement automatically |
| `random_terror_targeted_raid` | Active | one exact active state | intelligence threshold or explicit high-risk choice | command power, army experience, support equipment, tied divisions | can remove a cell, free hostages, capture records, lower activity | costly, partial, failed, or abusive outcome | high after breakthrough, low with no intelligence | consume paid costs, clear raid target and window, handle survivors once |
| `random_terror_disrupt_support` | Active and Transnational | current supply profile | identified sponsor, corridor, criminal patron, or captured-revenue source | convoys, intelligence exposure, civilian burden, support equipment | lowers External Supply or exposes sponsor | wrong profile wastes resources, retaliation or route shift | high only when profile matches evidence | clear obsolete source actions after profile changes |
| `random_terror_request_allied_intelligence` | Active and Transnational | eligible partner | valid relations, access, partner can respond | initiating administrative burden, accepted partner cost after consent | joint intelligence, corridor discovery, improved operations | refusal, compromised sources, diplomatic exposure | high for coalition AI with shared threat | no partner spending before acceptance, clear request on invalidation |
| `random_terror_offer_defection_channel` | Active and Territorial | organization or enclave | credible protection, no blocked atrocity leader | administrative capacity, security manpower, legitimacy commitment | raises defections, can split organization, reveals support | hardliner backlash, victim opposition, false surrender | high against divided or weakened actor | protect accepted defectors, close channel after actor collapse |
| `random_terror_movement_restrictions` | Active | one state or corridor | active spread risk | stability, transport output, support equipment, tied manpower | lowers short-term movement and spread | legitimacy loss, economic disruption, route shifts elsewhere | emergency use only, lower weight when already extended | hard expiry, rising repeat cost, no permanent stacking |
| `random_terror_protect_community_sites` | Active and Jihadist | threatened institutions in one state | intimidation, targeted site, or Evolution IV opposition | local security, emergency services, support equipment | prevents retaliation, raises legitimacy, strengthens community rejection | other targets remain exposed | high when recruitment depends on intimidation | remove when threat ends, preserve protected-site outcome |
| `random_terror_expose_sponsor` | Active and Transnational | foreign sponsor | sufficient evidence | intelligence exposure, diplomatic cost, possible stability burden | public case, Condemnation, sanctions or coalition support | weak case harms credibility, sponsor retaliates | high with strong proof and allies | evidence consumed or archived, target cleared if sponsor gone |
| `random_terror_quiet_sponsor_leverage` | Active and Transnational | foreign sponsor | sufficient evidence and secret channel | intelligence exposure, political or diplomatic capacity | withdrawal, false information, prisoner exchange, or route closure | cover-up exposure, sponsor manipulates government | preferred by isolationist or intelligence-led AI | closes on exposure or sponsor change |
| `random_terror_military_reinforcement` | Territorial | threatened states | armed insurgency or state-loss risk | divisions, fuel, equipment, command capacity | improves local control and blocks easy seizure | weakens other fronts, supply strain | highest for capital and only viable core | benefits require units present, release on end |
| `random_terror_capital_security` | Emergency | capital and command network | capital infiltration or takeover risk | elite units, support equipment, fuel, command capacity | protects government continuity and mission | other states become more vulnerable | highest emergency priority | remove after mission, preserve continuity outcome |
| `random_terror_isolate_enclave` | Territorial | extremist enclave | border access and sufficient force | divisions, fuel, trains or convoys, diplomatic burden | lowers External Supply and opens surrender pressure | civilian suffering, Condemnation, relief failure | high when assault is too costly | end blockade on peace, annexation, target loss, or route change |
| `random_terror_relief_corridor` | Territorial and Recovery | contested state | civilian movement and valid access | divisions, convoys or trains, support equipment, civilian burden | lowers civilian deaths and recruitment, protects displacement | corridor attack or supply diversion | high after severe Deaths or low legitimacy | close after civilians safe or access invalid |
| `random_terror_prepare_retake` | Territorial | lost state | valid parent claim, supply, units, route | army experience, fuel, equipment, tied divisions | starts state objective and preparation bonuses | stalled offensive entrenches actor | high when relative force and supply are credible | clear if state restored, parent collapses, or peace reached |
| `random_terror_negotiate_surrender` | Territorial | weakened actor | actor isolated, no blocked route, credible terms | administrative burden, security manpower, legitimacy risk | disarmament, enclave settlement, prisoner and reintegration chain | actor rebuilds, hardliners split, public backlash | high for exhausted fragile governments against weak actor | one settlement per actor, clear rejected offers and terms |
| `random_terror_request_intervention` | Territorial and Final | eligible foreign power | access, threat, partner capacity | diplomatic influence, convoys, concessions, dependency risk | aid, volunteers, intelligence, blockade, air support, or intervention | patron demands, proxy control, escalation | high for weak parent, low for strong domestic AI | clear offers after conflict, preserve accepted obligations |
| `random_terror_restore_services` | Recovery | recaptured or cleared state | no armed control, damaged services | civilian factories, trains, support equipment, manpower | repairs buildings, raises legitimacy, clears recovery stage | neglect preserves dormant activity | high when final closure is near | complete once per damage package, close invalid state target |
| `random_terror_public_accounting` | Recovery | country or major incident | public casualties or exposed abuse | administrative capacity, stability risk | raises legitimacy, exposes responsibility, improves recurrence resistance | reveals state misconduct and Condemnation | high for democratic or legitimacy-led AI, situational elsewhere | one per incident package, preserve public record |
| `random_terror_security_reform` | Recovery | country | crisis cleared, response lessons available | civilian or military factory burden, XP, administrative capacity | creates limited lasting capacity and longer cooldown | short-term cost, authoritarian route can distort reform | high after repeated crises | replace temporary response cell with one bounded institutional result |

## Government missions

| Working mission ID | Typical duration | Objective | Success | Partial success | Failure | Main live requirements |
| --- | --- | --- | --- | --- | --- | --- |
| `random_terror_contain_attack_wave` | `90` to `120` days | prevent new active state and lower pressure or clear original hotspot | pressure falls, spread blocked, legitimacy can rise | no spread, original cell remains | valid new hotspot or stage advance | protection, active target, no invalid duplicate |
| `random_terror_protect_transport_network` | about `120` days | keep named transport assets operational with required protection | no major disruption, supply preserved, activity falls | route stays open with bounded damage | route disruption, captured supply, pressure rises | units or resource commitment maintained |
| `random_terror_break_cross_border_corridor` | about `150` days | coordinate participating countries and control named connection | corridor removed, reach or supply falls | corridor weakens and shifts | spread or retaliation | all participants accepted, valid route and targets |
| `random_terror_prevent_capital_seizure` | `60` to `90` days | maintain capital control and command continuity | seizure blocked, compromised actors exposed | capital held, nearby loss | coup, paralysis, civil war, or capital loss | capital valid, emergency protection maintained |
| `random_terror_retake_lost_state` | about `180` days | regain and hold extremist territory | control restored and recovery opens | military control without civil restoration | actor entrenches and gains authority | real war or state objective, forces and supply |
| `random_terror_restore_civil_authority` | `120` to `180` days | repair services, prevent revenge, rebuild administration | activity clears, legitimacy rises, cooldown extends | state remains contested | dormant or entrenched return | recaptured state, relief and administration actions |
| `random_terror_hostage_deadline` | `30` to `75` days | resolve a named hostage crisis | hostages recovered or released with bounded casualties | some freed, leaders escape | mass casualties, propaganda victory, pressure rise | one active crisis, chosen response remains valid |
| `random_terror_stop_coordinated_uprising` | `60` to `120` days | prevent Final Jihad cells from seizing states during offensive | uprising collapses and world revolt weakens | one state held, cells survive | civil war or transfer | Evolution V, real pressure and active cells |

## Territorial-actor decisions

| Working decision ID | Actor stage | Target | Main costs or requirements | Result | Failure or tradeoff | Cleanup |
| --- | --- | --- | --- | --- | --- | --- |
| `random_terror_raise_local_militia` | Local and above | controlled populated state | manpower, infantry equipment, control threshold | capped militia formation | lowers control or equipment reserve | unit cap, cooldown, remove when no valid state |
| `random_terror_integrate_defectors` | Local and above | defecting formation or state | actual defector flag, equipment, command capacity | transfers or rebuilds one compatible formation | loyalty risk and internal rivalry | consume defector record once |
| `random_terror_repair_captured_depot` | Regional and above | damaged depot or industrial state | civilian capacity, support equipment, control | restores bounded production and supply | vulnerable to parent raid | remove when state lost |
| `random_terror_open_external_corridor` | Transnational and above | valid border, port, or route | authority, sponsor or neighboring access, convoys or trucks | raises External Supply and creates route | exposure and foreign retaliation | clear on route loss or sponsor death |
| `random_terror_seek_sponsor` | All durable actors | foreign country | route compatibility, relations, sponsor interest | aid agreement and patronage | dependency and demands | clear when sponsor changes or turns hostile |
| `random_terror_support_foreign_cell` | Transnational and above | high-value active foreign country | Network Authority, equipment or support, reach | strengthens existing cell or creates Traces under valid rules | exposure, resource loss, retaliation | no duplicate cell, clear invalid target |
| `random_terror_relocate_network` | Shadow Council | threatened cell or leadership | authority and safe destination | preserves cell or leader | loses local assets and control | one relocation per threat window |
| `random_terror_convert_militia` | War Directorate | existing militia formation | equipment, XP, control, supply | upgrades template or formation | drains stockpile | no unit duplication |
| `random_terror_ideological_mobilization` | Secretariat | controlled state | legitimacy or control tradeoff, equipment, manpower | recruitment and obedience | resistance and purge risk | duration and stage cap |
| `random_terror_absorb_actor` | Regional and above | compatible Event 31 actor | authority, route, consent or AI acceptance | merger, subject, or command | rivalry war or split | transactional, no duplicate assets |
| `random_terror_contest_network_leader` | Transnational and above | faction leader | authority, support, current unity | leadership contest | civil war, expulsion, authority loss | clear contest state after result |
| `random_terror_prepare_state_offensive` | War Directorate or expansion route | adjacent strategic state | army XP, fuel, equipment, forces | operation and war objective | stalled offensive and control loss | remove on state result |
| `random_terror_build_civil_administration` | Civil Administration | controlled state | civilian factories, manpower, control | raises control and repairs economy | slower war output | one stage per state |
| `random_terror_force_extraction` | Coerced Economy | controlled state | control and coercive route | immediate equipment or output | deaths, resistance, Condemnation | escalating cost and state cooldown |
| `random_terror_recruit_foreign_fighters` | Evolution II or IV | network route | reach, corridor, authority, equipment | manpower and experienced recruits | rival influence and route exposure | bounded intake, cooldown, no free loop |
| `random_terror_join_jihadist_international` | Evolution IV | Jihadist International | compatible route, unity, authority | faction membership and shared content | subordination and new enemies | leave or split only through valid route |
| `random_terror_call_coordinated_uprising` | Evolution V | high-pressure foreign country | authority, reach, unity, real local cell | pressure-scaled uprising | exposure, cell loss, unity cost | one uprising per target window |
| `random_terror_accelerate_revelation` | Evolution V | dominant command | `1000+` Chaos, readiness near threshold, public branch enabled | shortens terminal delay | internal split, readiness loss, leader death | cannot bypass hard gates, one attempt |

## Visible-action budgets

| Category phase | Normal visible primary decisions | Hard maximum | Active missions |
| --- | --- | --- | --- |
| Immediate shock | `3` to `5` | `6` | `1` to `2` |
| Active network | `3` to `5` | `6` | `1` to `3` |
| Territorial challenge | `3` to `5` | `6` | `1` to `3` |
| Recovery | `2` to `4` | `5` | `0` to `2` |
| Territorial actor | `3` to `5` | `6` | `1` to `3` |
| Final state | `3` to `5` | `6` | `1` to `3` |

## Matrix acceptance

The implementation should compare every visible decision and mission with this matrix.

A missing row, merged row, altered cost family, removed failure state, new action, or changed phase needs an explicit disposition in the completion report.
