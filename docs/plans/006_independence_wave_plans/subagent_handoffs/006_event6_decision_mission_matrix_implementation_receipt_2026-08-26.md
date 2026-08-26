# Event 006 80-row decision and mission implementation receipt

Date: 2026-08-26  
Scope: accepted Event 006 decision/mission matrix only, inside the currently admitted boundary.  
Disposition: source-complete crosswalk; one source-proven localisation repair applied. No decision, mission, event, AI, GUI, admission, or broad-balance design was changed.

## Sources and method

- Accepted source of truth: docs/specs/006_independence_wave_specs/matrices/006_decision_mission_map.csv, 80 rows.
- Mechanics contract: docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_3_mechanics_and_decisions.md.
- Current definitions: common/decisions/006_independence_wave_decisions.txt (DM-01 through DM-62) and common/decisions/006_independence_wave_form03_decisions.txt (FORM03-D01 through FORM03-D18).
- Current player text: localisation/english/006_independence_wave_decisions_l_english.yml and localisation/english/006_independence_wave_form03_l_english.yml.

The receipt script checked all 80 matrix IDs against current definitions. It found 80 current definitions, 80 visibility-or-activation gates, 80 available gates, 80 AI blocks, 80 terminal effects, and 80 lifecycle markers. It found 18 current timed-mission blocks, each with available, timeout_effect, and cancel_trigger. It resolved title and description text for all 80 rows, and base, blocked, and tooltip text for all 79 custom-cost rows. FORM03-D11 is the expected prepaid selectable objective and has no custom cost.

Legend used in the receipt:

- V/A/E means the current definition contains its visibility or activation gate, availability gate, and terminal effect.
- M means the action is a matrix mission/mission-chain contract. Its active current mission blocks use available, timeout_effect, and cancel_trigger.
- D means a one-shot, repeat-limited, cooldown, replacement, or removal path is present in the current definition; the accepted cleanup outcome is summarized after the slash.
- C3 means the cost has current base, blocked, and tooltip localisation keys. It is not a statement that every row consumes three resources.
- Owner abbreviations: R released-country; H former-host/bilateral; L league member; F formable; X radical; LCX FORM-03 carrier; S sovereign BEL/HOL/LUX member.

## One-to-one receipt: shared founding, recognition, and security rows

| Matrix row | Current decision or mission source | Owner / type | Cost evidence | Gate -> terminal direction | Cleanup and localisation evidence |
|---|---|---|---|---|---|
| DM-01 | independence_wave_secure_provisional_capital (006_independence_wave_decisions.txt:23) | R / timed mission | provisional-capital C3 | capital control, supply, assigned divisions -> security and capacity | V/A/E; M; ends on success, capital loss, annexation, or relocation; title/desc/C3 |
| DM-02 | independence_wave_establish_revenue_service (:84) | R / timed mission | administration-standard C3 | economic anchor and stability -> recurring revenue/capacity | V/A/E; M; completion or government-collapse cleanup; title/desc/C3 |
| DM-03 | independence_wave_register_population (:132) | R / timed mission | administration-light C3 | anchor control and local peace -> legitimacy/capacity/manpower | V/A/E; M; one founding-state use; title/desc/C3 |
| DM-04 | independence_wave_hold_first_assembly (:200) | R / goal mission | administration-standard C3 | secure capital and legitimacy -> constitutional route | V/A/E; M; route-lock or annexation cancel; title/desc/C3 |
| DM-05 | independence_wave_confirm_traditional_authority (:257) | R / goal mission | administration-light C3 | traditional-support gate -> traditional route/legitimacy | V/A/E; M; incompatible-route cancel; title/desc/C3 |
| DM-06 | independence_wave_recruit_local_civil_servants (:316) | R / clickable | administration-light C3 | educated population and capital -> capacity / low patron influence | V/A/E; D / replaced by mature-ministry action; title/desc/C3 |
| DM-07 | independence_wave_recall_exile_administrators (:345) | R / clickable | diplomatic-light C3 | exile network or foreign access -> capacity/recognition | V/A/E; D / one use per exile network; title/desc/C3 |
| DM-08 | independence_wave_retain_former_host_officials (:379) | R / clickable | administration-light C3 | officials exist and purge route closed -> fast capacity | V/A/E; D / official pool clears; title/desc/C3 |
| DM-09 | independence_wave_create_provincial_compacts (:426) | R / targeted | administration-standard C3 | diverse/distant province -> control and lower instability | V/A/E; D / one per region, obsolete after integration; title/desc/C3 |
| DM-10 | independence_wave_establish_treasury_and_currency (:478) | R / mission chain | administration-major C3 | revenue service and economic anchor -> currency/capacity tools | V/A/E; M; one time then mature treasury; title/desc/C3 |
| DM-11 | independence_wave_send_diplomatic_mission (:594) | R / targeted | diplomatic-light C3 | target, route, foreign-service capacity -> recognition/liaison | V/A/E; D / target cooldown and death cleanup; title/desc/C3 |
| DM-12 | independence_wave_request_former_host_recognition (:659) | R / major targeted | diplomatic-standard C3 | living former host and unsettled relation -> negotiated separation | V/A/E; D / settlement or host-death closure; title/desc/C3 |
| DM-13 | independence_wave_seek_regional_guarantee (:727) | R / targeted | diplomatic-standard C3 | interested regional power and relations -> guarantee/recognition | V/A/E; D / target cooldown; title/desc/C3 |
| DM-14 | independence_wave_accept_arms_limit_recognition (:785) | R / clickable | diplomatic-light C3 | foreign offer -> recognition and lower host threat | V/A/E; D / treaty expiry/break removes limits; title/desc/C3 |
| DM-15 | independence_wave_build_permanent_foreign_service (:830) | R / mission chain | administration-standard C3 | capacity and recognition -> lower mission cost/wider access | V/A/E; M; one time; title/desc/C3 |
| DM-16 | independence_wave_coordinate_recognition_campaign (:872) | L / shared mission | diplomatic-standard-factory C3 | supporting members and target -> recognition/cohesion | V/A/E; M; target recognition or death ends it; title/desc/C3 |
| DM-17 | independence_wave_integrate_militias (:1014) | R / mission chain | security-standard C3 | militia pool and command capacity -> templates/security | V/A/E; M; militia-pool exhaustion closes; title/desc/C3 |
| DM-18 | independence_wave_secure_depot (:1055) | R / map objective | security-light C3 | named depot control and supplied divisions -> supply/security | V/A/E; D / one depot use; title/desc/C3 |
| DM-19 | independence_wave_recall_defecting_officers (:1103) | R / clickable | security-light C3 | officer pool -> commanders/organization | V/A/E; D / one-time pool; title/desc/C3 |
| DM-20 | independence_wave_form_border_guards (:1131) | R / mission chain | security-standard C3 | controlled border and manpower -> readiness | V/A/E; M; limited by border sectors; title/desc/C3 |
| DM-21 | independence_wave_open_volunteer_corridor (:1171) | R / targeted | corridor C3 | route or league access -> volunteers/security | V/A/E; D / invalid route closes; title/desc/C3 |
| DM-22 | independence_wave_raise_emergency_units (:1228) | R / limited | security-major C3 | severe threat and force budget -> temporary survival units | V/A/E; D / bounded pool and demobilisation cleanup; title/desc/C3 |
| DM-23 | independence_wave_professionalize_army (:1281) | R / mission family | security-major C3 | integrated militia/training/equipment -> durable force | V/A/E; M; tier-limited use; title/desc/C3 |

## One-to-one receipt: settlement, patron, and league rows

| Matrix row | Current decision or mission source | Owner / type | Cost evidence | Gate -> terminal direction | Cleanup and localisation evidence |
|---|---|---|---|---|---|
| DM-24 | independence_wave_offer_ceasefire_line (006_independence_wave_decisions.txt:1330) | H / bilateral | diplomatic-light C3 | conflict or mobilised frontier -> temporary peace/talks | V/A/E; D / expiry or treaty conversion; title/desc/C3 |
| DM-25 | independence_wave_divide_state_property (:1389) | H / negotiation mission | administration-standard C3 | ceasefire or talks -> settled assets/relations | V/A/E; M; one time; title/desc/C3 |
| DM-26 | independence_wave_negotiate_citizenship_and_return (:1438) | H / negotiation mission | administration-standard C3 | movement/property dispute -> lower border tension | V/A/E; M; one per bilateral relation; title/desc/C3 |
| DM-27 | independence_wave_accept_limited_claims (:1487) | R / major | diplomatic-light C3 | host recognition offer -> treaty/recognition | V/A/E; D / renounced claims lock until treaty break; title/desc/C3 |
| DM-28 | independence_wave_demand_recognition_by_force (:1530) | R / ultimatum mission | strategic C3 | security, route, target host -> recognition or war opening | V/A/E; M; one active ultimatum; title/desc/C3 |
| DM-29 | independence_wave_offer_association_or_reunion (:1594) | H / bilateral | strategic C3 | compatible route/public support -> association or reunion | V/A/E; D / origin-active content cleans if sovereignty ends; title/desc/C3 |
| DM-30 | independence_wave_prepare_reclamation_defense (:1647) | R / emergency mission | security-major C3 | host preparation detected -> readiness/coalition | V/A/E; M; threat expiry or war start ends it; title/desc/C3 |
| DM-31 | independence_wave_accept_arms_mission (:1703) | R / targeted | diplomatic-standard C3 | active sponsor/route -> equipment/training | V/A/E; D / cooldown/channel cap; title/desc/C3 |
| DM-32 | independence_wave_accept_industrial_credits (:1767) | R / targeted | administration-standard C3 | sponsor and project capacity -> industry/infrastructure | V/A/E; D / one active project per sponsor; title/desc/C3 |
| DM-33 | independence_wave_invite_security_advisers (:1841) | R / targeted | diplomatic-light C3 | sponsor/security need -> counterintelligence/stability | V/A/E; D / expiry or permanent conversion; title/desc/C3 |
| DM-34 | independence_wave_grant_base_or_transit_rights (:1883) | R / major targeted | strategic C3 | sponsor request/viable location -> guarantee/aid | V/A/E; D / treaty break or buyout ends it; title/desc/C3 |
| DM-35 | independence_wave_balance_patrons (:1945) | R / mission chain | patron-balance C3 | two active patrons -> autonomy | V/A/E; M; repeatable with escalating difficulty; title/desc/C3 |
| DM-36 | independence_wave_buy_out_concession (:2006) | R / clickable | strategic-major C3 | active concession/economy -> lower patron influence | V/A/E; D / one concession at a time; title/desc/C3 |
| DM-37 | independence_wave_expose_foreign_interference (:2047) | R / risky | diplomatic-light C3 | evidence/domestic support -> lower influence/coup network | V/A/E; D / target cooldown; title/desc/C3 |
| DM-38 | independence_wave_choose_client_future (:2100) | R / route | strategic C3 | dominant patron/route commitment -> aid/patron tree | V/A/E; D / autonomy routes close and league eligibility updates; title/desc/C3 |
| DM-39 | independence_wave_recognize_new_independence_wave_country (:2145) | R / targeted | diplomatic-light C3 | target active Event 006 origin -> recognition/network standing | V/A/E; D / target-death cleanup; title/desc/C3 |
| DM-40 | independence_wave_send_civil_service_cadres (:2195) | R / targeted | administration-standard C3 | surplus capacity/member -> target capacity/standing | V/A/E; D / target death or war cutoff; title/desc/C3 |
| DM-41 | independence_wave_contribute_emergency_reserve (:2249) | L / repeat-limited | safe-reserve C3 | league and resource surplus -> reserve/cohesion | V/A/E; D / contribution/withdrawal ledger; title/desc/C3 |
| DM-42 | independence_wave_request_collective_recognition (:2275) | L / shared mission | diplomatic-standard-factory C3 | low-recognition member/supporters -> recognition/confidence | V/A/E; M; success, target death, or route change ends it; title/desc/C3 |
| DM-43 | independence_wave_request_border_arbitration (:2355) | L / bilateral mission | diplomatic-standard C3 | active member dispute -> settlement/cohesion | V/A/E; M; one case per pair; title/desc/C3 |
| DM-44 | independence_wave_rescue_threatened_member (:2477) | L / shared crisis | rescue-aid C3 | capital/existence threat -> member survival/cohesion | V/A/E; M; threat resolution ends it; title/desc/C3 |
| DM-45 | independence_wave_convene_founding_congress (:2652) | L / mission chain | strategic C3 | members/standing/common cause -> charter vote | V/A/E; M; one global active congress; title/desc/C3 |
| DM-46 | independence_wave_adopt_charter_pillar (:2706) | L / vote | diplomatic-standard C3 | active congress -> selected pillar/identity | V/A/E; D / one outcome per pillar; title/desc/C3 |
| DM-47 | independence_wave_challenge_league_leadership (:2801) | L / vote mission | strategic C3 | standing, contribution, alternative agenda -> leadership/reform | V/A/E; M; cooldown/emergency lockout; title/desc/C3 |
| DM-60 | independence_wave_call_charter_expulsion_vote (:2866) | L / targeted timed | strategic C3 | anti-puppetry ground/charter -> expulsion case resolution | V/A/E; M; active case clears after resolution; title/desc/C3 |
| DM-61 | independence_wave_sponsor_member_coup (:2945) | L / immediate targeted | security-standard C3 | security-standard manpower -> civil-war sponsorship evidence | V/A/E; D / one immediate eligible action/cooldown; title/desc/C3 |
| DM-62 | independence_wave_request_charter_war_mandate (:3002) | L / targeted timed | diplomatic-standard-factory C3 | mutual-defence pillar/charter -> 365-day mandate | V/A/E; M; unconsumed mandate then matching declaration consumes it; title/desc/C3 |

## One-to-one receipt: border, formable, and high-chaos rows

| Matrix row | Current decision or mission source | Owner / type | Cost evidence | Gate -> terminal direction | Cleanup and localisation evidence |
|---|---|---|---|---|---|
| DM-48 | independence_wave_survey_claimed_districts (006_independence_wave_decisions.txt:3086) | R / regional mission | administration-standard C3 | package ambition -> requirements/local support | V/A/E; M; one use per ambition region; title/desc/C3 |
| DM-49 | independence_wave_sponsor_plebiscite (:3147) | R / targeted mission | strategic-major C3 | support, observers, valid claim -> transfer or claim | V/A/E; M; one state/region use; title/desc/C3 |
| DM-50 | independence_wave_negotiate_transfer (:3225) | R / bilateral mission | strategic-major C3 | relations/compensation -> peaceful transfer | V/A/E; M; target cooldown; title/desc/C3 |
| DM-51 | independence_wave_prepare_border_ultimatum (:3283) | R / timed crisis | border-ultimatum-major C3 | security/route commitment -> transfer, war, or settlement | V/A/E; M; one active ultimatum; title/desc/C3 |
| DM-52 | independence_wave_integrate_settled_district (:3383) | R or F / mission | integration-major C3 | control, connection, local support -> core/durable integration | V/A/E; M; one per state and origin; title/desc/C3 |
| DM-53 | independence_wave_discover_regional_identity (:3434) | R / focus-unlocked | administration-standard C3 | package family and route -> formation requirements | V/A/E; D / one family discovery; title/desc/C3 |
| DM-54 | independence_wave_convene_formation_congress (:3468) | L / mission chain | strategic C3 | territory, consent, legitimacy, recognition -> formation vote | V/A/E; M; one family congress; title/desc/C3 |
| DM-55 | independence_wave_proclaim_military_union (:3511) | F / major | formable-commit C3 | territory/military route -> formable and claims | V/A/E; D / cleans old decisions; title/desc/C3 |
| DM-56 | independence_wave_integrate_member_region (:3544) | F / mission family | integration-major C3 | controlled member region/admin path -> cores/institutions | V/A/E; M; one use per region; title/desc/C3 |
| DM-57 | independence_wave_sponsor_another_breakaway (:3598) | X / targeted | breakaway-sponsorship C3 | Evolution 5/intelligence/future candidate -> opening strength | V/A/E; D / one sponsorship at a time; title/desc/C3 |
| DM-58 | independence_wave_coordinate_reclamation_fronts (:3652) | X / shared mission | reclamation-front C3 | compatible member claims -> synchronised operations | V/A/E; M; one operation at a time; title/desc/C3 |
| DM-59 | independence_wave_transform_league_charter (:3783) | L / vote chain | strategic C3 | high chaos/common cause/radical support -> armed/revisionist league | V/A/E; M; irreversible charter transformation; title/desc/C3 |

## One-to-one receipt: FORM-03 rows

| Matrix row | Current decision or mission source | Owner / type | Cost evidence | Gate -> terminal direction | Cleanup and localisation evidence |
|---|---|---|---|---|---|
| FORM03-D01 | independence_wave_form03_convene_language_convention (006_independence_wave_form03_decisions.txt:207) | LCX / timed | administration-standard-factory C3 | active LCX and convention focus -> language model | V/A/E; M; one per LCX lifecycle; title/desc/C3 |
| FORM03-D02 | independence_wave_form03_open_multilingual_service_examinations (:240) | LCX / timed | administration-standard-factory C3 | parallel-services/register model -> accommodation/capacity | V/A/E; M; legal carrier loss cancels; title/desc/C3 |
| FORM03-D03 | independence_wave_form03_publish_member_language_codes (:282) | LCX / timed | administration-light C3 | selected language model/service focus -> accommodation/legitimacy | V/A/E; M; legal carrier loss cancels; title/desc/C3 |
| FORM03-D04 | independence_wave_form03_establish_federal_language_appeals (:324) | LCX / timed | administration-standard-factory C3 | territorial administration model -> accommodation/stability | V/A/E; M; legal carrier loss cancels; title/desc/C3 |
| FORM03-D05 | independence_wave_form03_extend_protected_local_services (:356) | LCX / timed | protected-services C3 | working-register model -> accommodation | V/A/E; M; legal carrier loss cancels; title/desc/C3 |
| FORM03-D06 | independence_wave_form03_reconnect_sambre_meuse_corridor (:393) | LCX / timed | sambre-meuse-project C3 | owns/controls state 34 -> integration/state works | V/A/E; M; state loss cancels with integration loss; title/desc/C3 |
| FORM03-D07 | independence_wave_form03_coordinate_frisian_waterway_standards (:435) | LCX / timed | frisian-waterway-project C3 | owns/controls state 36 -> integration/waterline hooks | V/A/E; M; state loss cancels with integration loss; title/desc/C3 |
| FORM03-D08 | independence_wave_form03_standardize_rail_and_customs_manifests (:477) | LCX / timed | manifests C3 | corridor-standards focus -> integration | V/A/E; M; legal carrier loss cancels; title/desc/C3 |
| FORM03-D09 | independence_wave_form03_request_development_compact_technical_mission (:506) | LCX / timed | compact-technical-mission C3 | compact membership and reserve >=80 -> integration/capacity | V/A/E; M; cancel refunds 10 reserve once; title/desc/C3 |
| FORM03-D10 | independence_wave_form03_invite_sovereign_corridor_partners (:549) | LCX / timed | corridor-invitations C3 | unresolved eligible sovereign members -> BEL/HOL/LUX invitations | V/A/E; M; legal carrier loss cancels; title/desc/C3 |
| FORM03-D11 | independence_wave_form03_ratify_confederal_charter (:586) | LCX / selectable objective | pre-paid convergence objective | values >=70, resolved status, real language scope -> full compact | V/A/E; M; one activation then compromise/rupture timeout; title/desc |
| FORM03-D12 | independence_wave_form03_resubmit_confederal_charter (:614) | LCX / timed | diplomatic-standard C3 | repairable compromise/full gate -> full compact | V/A/E; M; bounded failure-cycle repeat; title/desc/C3 |
| FORM03-D13 | independence_wave_form03_reopen_charter_talks (:640) | LCX / timed | reopen-charter-talks C3 | rupture outcome -> values >=50 and repair opening | V/A/E; M; one reopening per rupture; title/desc/C3 |
| FORM03-D14 | independence_wave_form03_repair_language_settlement (:669) | LCX / timed | administration-standard-factory C3 | accommodation below 70 -> accommodation repair | V/A/E; M; once per failure cycle; title/desc/C3 |
| FORM03-D15 | independence_wave_form03_repair_industrial_compact (:699) | LCX / timed | repair-industrial C3 | integration below 70 -> integration repair | V/A/E; M; once per failure cycle; title/desc/C3 |
| FORM03-D16 | independence_wave_form03_implement_member_language_guarantees (:729) | S / timed | member-language C3 | pending full accession -> constitutional ratification | V/A/E; M; one member/lifecycle; title/desc/C3 |
| FORM03-D17 | independence_wave_form03_fund_associate_corridor_share (:757) | S / targeted timed | member-corridor C3 | exact owned/controlled legal member state -> integration/standing | V/A/E; M; target/membership loss cancels; title/desc/C3 |
| FORM03-D18 | independence_wave_form03_withdraw_from_autonomous_membership (:794) | S / timed | diplomatic-standard C3 | living member/no action -> sovereign withdrawal/tombstone | V/A/E; M; one member/lifecycle, no territory/subject change; title/desc/C3 |

## Applied local repair

Changed file:

- localisation/english/006_independence_wave_form03_l_english.yml

The repair is intentionally localisation-only and covers the FORM-03 rows whose actual payment helpers choose one transport alternative rather than charging both:

| Matrix row | Cost keys changed | Before | After |
|---|---|---|---|
| FORM03-D08 | independence_wave_form03_manifests_cost and _blocked | Displayed convoy and train icons beside one convoy amount | Uses This.GetIndependenceWaveDiplomaticStandardTransportCostText / BlockedText, matching can_pay_independence_wave_diplomatic_standard_cost and independence_wave_decision_pay_diplomatic_standard |
| FORM03-D10 | independence_wave_form03_corridor_invitations_cost and _blocked | Same false dual transport display | Same standard dynamic transport helper |
| FORM03-D13 | independence_wave_form03_reopen_charter_talks_cost and _blocked | Same false dual transport display | Same standard dynamic transport helper, matching the strategic helper's standard payment delegation |
| FORM03-D17 | independence_wave_form03_member_corridor_cost and _blocked | Same false dual transport display | Uses This.GetIndependenceWaveDiplomaticLightTransportCostText / BlockedText, matching can_pay_independence_wave_diplomatic_light_cost and independence_wave_decision_pay_diplomatic_light |

Before the patch, the UI implied that the player must provide both a convoy and a train. The payment trigger/effect instead accepts and consumes convoys if sufficient, otherwise trains. The new dynamic strings show convoy, train, or either according to the actual eligible payment route.

The affected visible cost strings remain within the four-spendable-type limit:

- FORM03-D08 and FORM03-D10: command power, one dynamic transport type, civilian factory.
- FORM03-D13: stability, command power, one dynamic transport type, civilian factory.
- FORM03-D17: command power, one dynamic transport type, civilian factory.

## Decision-category lifecycle and cognitive-load notes

- The source map phases founding, provisional state, recognized state, regional power, league, formable, and FORM-03 drafting/works/accession actions. The receipt found every row gated by visibility-or-activation and availability logic; no accepted row is an unconditional flat political-power exchange.
- The founding Statehood Ledger and formable-state-puzzle categories are the two decision-owned GUI surfaces touched by this matrix. This patch changes cost text only; it does not alter category layout, button count, active mission count, or scripted-GUI source.
- Source review cannot prove a runtime upper bound on simultaneously visible actions or missions because that requires the current scenario/UI projection. The relevant gates are present, but the mandatory current GUI paths did not return. Do not treat this receipt as visual acceptance.
- All patched costs are icon-first. No literal spendable-resource words were introduced. The prior false paired transport icon was the only source-proven cost-clarity defect found in this pass.

## AI, route-lock, cleanup, and exploit notes

- Every one of the 80 current definitions contains an AI block. The requested probability route was started through the probability specialist, but fresh evaluation is unavailable: parent stopped the nested audit after prior findings, and the MCP service is timing out. No AI value, weight, target, or balance behavior was patched.
- The receipt confirms gates and lifecycle markers, not runtime target reachability. Exact target death, annexation, route, state-control, treaty, timer, and cooldown contracts remain represented in the accepted map cleanup column and current source definitions.
- No new free-unit, equipment, core, war-goal, reserve, or cooldown loop was added. FORM03-D09 retains its source refund-once contract; FORM03-D11 remains the one prepaid mission exception.

## MCP evidence and remaining blockers

- Direct decision and mission inspection is not exposed by the installed HOI4 MCP inventory. Source structural review is therefore not equivalent to an engine decision projection.
- Current read-only MCP attempt: hoi4.gui_inspect, window independence_wave_status_window, scenario { id: independence_wave_status_default }, timed out awaiting tools/call after 180 seconds.
- Current read-only MCP attempt: hoi4.gui_render, same window/scenario, normal at 1280x720, timed out awaiting tools/call after 180 seconds.
- Current read-only MCP attempt: hoi4.gui_inspect, window chaosx_independence_wave_formable_state_puzzle_window, scenario { id: E6_FORMABLE_STATE_PUZZLE_GUI_SETTLED_2026_08_09 }, timed out awaiting tools/call after 180 seconds.
- No fourth long render attempt was made after parent directed finalisation. Existing historical GUI artifacts are not claimed as new current visual acceptance.

## Validation

- Matrix-to-source crosswalk: 80 accepted rows, 80 unique current decision/mission definitions, no missing matrix ID or extra mapped ID.
- Structural lifecycle check: 80/80 visibility-or-activation, availability, AI, terminal-effect, and lifecycle markers; 18 timed mission blocks with available, timeout_effect, and cancel_trigger.
- Localisation check: 80/80 current title/description keys; 32 current custom-cost key triplets across shared and FORM-03 localisation; FORM03-D11 correctly excluded as pre-paid.
- Focused post-patch inspection confirmed the eight changed FORM-03 base/blocked strings use the appropriate standard or light dynamic transport localisation helper and no longer contain the false paired convoy/train icon sequence.
- python -B .tools/audit_event6_allocator.py completed successfully: 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 packages, 40 adapters, 32 attestations, 29 reservation groups, and the documented 3/4/5/7/10 ladder.

Skipped meaningful validation: live game validation is user-owned and was not run; current GUI MCP inspect/render and probability evaluation were blocked as recorded above.

## Files and handoff status

- Changed: localisation/english/006_independence_wave_form03_l_english.yml.
- Added: this receipt.
- No other file was changed by this pass. Nothing was staged or committed.

Skills used: chaos-redux-decisions-missions and chaos-redux-events. No skill was created or changed.
