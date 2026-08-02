# Event 006 decision and mission matrix current audit

Date: 2026-08-02

## Scope and disposition

This audit compares the accepted `docs/specs/006_independence_wave_specs/matrices/006_decision_mission_map.csv` against the current Event 006 decision categories, all 31 `common/decisions/006*.txt` files, the decision, FORM-03, crisis, and scenario helper surfaces, Event 006 English localisation, and their `ai_will_do` blocks.

Static disposition: **PASS for the accepted row map.**

All 80 accepted rows have one current, unique implementation identifier: DM-01 through DM-62 in `common/decisions/006_independence_wave_decisions.txt`, and FORM03-D01 through FORM03-D18 in `common/decisions/006_independence_wave_form03_decisions.txt`.

No gameplay, localisation, GUI, focus, scripted-effect, scripted-trigger, category, or accepted-spec source was changed.

## Issue list, sorted by severity

### P2: SCN-008 scenario evidence remains incomplete

The current scenario contract is eight player-facing modes by four intensities, for 32 source/MCP acceptance cells. The static source establishes the contracts, including the three independently selectable Universal Belligerence rules, but this audit did not execute the 32 cells or the documented collision-heavy allocator cases.

The doubled automatic ladder and host-crisis contracts are also source-wired but not observed through mission completion, queue retry, finalization, repeated launch, or save/load behavior.

### P3: Package and live-engine evidence remain outside this matrix audit

The row map does not grant package admission or replace package, asset, focus-layout, allocator, or live-engine acceptance evidence. Current package decision files were included in the static inventory, but their country-specific readiness remains owned by the corresponding package audits.

### No source-missing accepted row or narrow source defect found

The accepted matrix has zero source-missing rows. No passive political-power store, missing `ai_will_do`, missing custom-cost localisation triplet, missing mission timeout/cancellation contract, stale target cleanup omission, or direct matrix contradiction was found that supports a narrow source patch.

## Audit method and current static counts

| Check | Current result |
| --- | --- |
| Accepted matrix rows | 80 |
| Unique source implementations mapped | 80 |
| Source-missing rows | None |
| Rows with own name, description, availability gate, `available`, AI block, and completion or cleanup contract | 80 of 80 |
| Matrix custom-cost keys | 27, all base, `_blocked`, and `_tooltip` keys resolve |
| All Event 006 decision custom-cost keys | 133, all base, `_blocked`, and `_tooltip` keys resolve |
| Event 006 decision files statically inventoried | 31 |
| Direct-child timed missions in that inventory | 59 |
| Timed missions missing `available`, `timeout_effect`, or `cancel_trigger` | None |
| Selectable timed missions | 19 |
| Selectable timed missions without `ai_will_do` | None |
| Literal zero-cost decision controls | Only the three read-only SCN-008 rejection-ledger navigation controls |

The current code comment convention marks DM-01 through DM-60 directly. DM-61 and DM-62 use explanatory comments instead, so the static map resolves them by their implementation identifiers rather than treating them as missing.

## Row-level matrix audit

Legend: `N/D` means source `name` and `desc` localisation keys exist. `C3` means the custom cost, blocked cost, and cost tooltip all resolve. `T`, `R`, and `C` mean timeout, remove, and cancel paths respectively. `1x` is a one-time flag or bounded lifecycle guard. Cost codes use the material helpers in `common/scripted_effects/006_independence_wave_decision_effects.txt`: administration spends factory capacity, command power, and manpower; diplomatic spends command power plus convoys or trains; security spends command power or manpower, Army XP, infantry equipment, and support equipment; strategic adds stability and war-support sacrifice to the diplomatic standard package.

### Founding, government, recognition, and security

| Row | Implementation and category | Availability | Cost | Duration / timeout | AI | Localisation | Cleanup and static disposition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DM-01 | `independence_wave_secure_provisional_capital` in Founding | Active origin, auto garrison/capital objective | Garrison commitment, no click cost | 75-day mission | urgent | N/D | T+C+1x, PASS |
| DM-02 | `independence_wave_establish_revenue_service` in Founding | Active origin, secured capital, no competing founding mission | administration standard + 2 civilian factories | 150-day selectable mission | high | N/D+C3 | T+C+1x, PASS |
| DM-03 | `independence_wave_register_population` in Founding | Active origin, revenue service and controlled anchor | administration light + 1 civilian factory | 150-day selectable mission | standard | N/D+C3 | T+C+1x, PASS |
| DM-04 | `independence_wave_hold_first_assembly` in Founding | Provisional constitutional route, capital and legitimacy gate | administration standard + 2 civilian factories | 180-day goal mission | standard | N/D+C3 | T+C+1x, PASS |
| DM-05 | `independence_wave_confirm_traditional_authority` in Founding | Suitable active origin and traditional-authority gate | administration light + 1 civilian factory | 180-day goal mission | standard | N/D+C3 | T+C+1x, PASS |
| DM-06 | `independence_wave_recruit_local_civil_servants` in Government | Active origin, capital and local-administration gate | administration light + 1 civilian factory | 75-day decision | high | N/D+C3 | R+C+1x, PASS |
| DM-07 | `independence_wave_recall_exile_administrators` in Government | Provisional origin with valid exile/foreign-access path | diplomatic light | 75-day decision | standard | N/D+C3 | R+C+1x, PASS |
| DM-08 | `independence_wave_retain_former_host_officials` in Government | Active origin, host-official pool and no purge route | administration light | 45-day decision | standard | N/D+C3 | R+C+1x, PASS |
| DM-09 | `independence_wave_create_provincial_compacts` in Government | Provisional origin and valid controlled provincial target | administration standard + 2 civilian factories | 120-day targeted decision | standard | N/D+C3 | R+C, target validity, PASS |
| DM-10 | `independence_wave_establish_treasury_and_currency` in Government | Revenue service, economic anchor, and founding-slot gate | administration standard + 3 civilian factories | 240-day selectable mission | high | N/D+C3 | T+C+1x, PASS |
| DM-11 | `independence_wave_send_diplomatic_mission` in Recognition | Provisional origin, valid target, service and route checks | diplomatic light | 75-day targeted decision, 180-day cooldown | standard | N/D+C3 | R+C+target cooldown, PASS |
| DM-12 | `independence_wave_request_former_host_recognition` in Recognition | Provisional origin with living unsettled former host | diplomatic standard | 120-day targeted decision | standard | N/D+C3 | R+C+1x, host validity, PASS |
| DM-13 | `independence_wave_seek_regional_guarantee` in Recognition | Provisional origin and valid regional guarantor | diplomatic standard | 120-day targeted decision, 365-day cooldown | standard | N/D+C3 | R+C+target cooldown, PASS |
| DM-14 | `independence_wave_accept_arms_limit_recognition` in Recognition | Active offer and no active arms-limit treaty | diplomatic light | Immediate; 720-day treaty flag | low | N/D+C3 | 1x, treaty expiry, PASS |
| DM-15 | `independence_wave_build_permanent_foreign_service` in Recognition | Recognized origin with capacity and recognition gate | administration standard + 2 civilian factories | 300-day selectable mission | high | N/D+C3 | T+C+1x, PASS |
| DM-16 | `independence_wave_coordinate_recognition_campaign` in Recognition | Recognized network/league actor and valid recognition target | diplomatic standard + 1 civilian factory | 180-day targeted decision, 180-day cooldown | high | N/D+C3 | R+C+target validity, PASS |
| DM-17 | `independence_wave_integrate_militias` in Security | Active origin, militia pool and command gate | security standard | 180-day selectable mission | high | N/D+C3 | T+C+1x, PASS |
| DM-18 | `independence_wave_secure_depot` in Security | Active origin and valid controlled depot target | security light | 120-day map decision | high | N/D+C3 | R+C+1x, target validity, PASS |
| DM-19 | `independence_wave_recall_defecting_officers` in Security | Active origin and officer-pool gate | security light | 45-day decision | standard | N/D+C3 | R+C+1x, PASS |
| DM-20 | `independence_wave_form_border_guards` in Security | Active frontier origin and manpower/border gate | security standard | 180-day selectable mission | high | N/D+C3 | T+C+1x, PASS |
| DM-21 | `independence_wave_open_volunteer_corridor` in Security | Active or provisional origin with valid route target | corridor helper | 120-day targeted decision, 365-day cooldown | low | N/D+C3 | R+C+route and target cleanup, PASS |
| DM-22 | `independence_wave_raise_emergency_units` in Security | Severe host threat or Armed Birth flag, force receipt, anchor | security major | Immediate; 180-day raised flag | urgent | N/D+C3 | 1x; fixed-id demobilization from professionalization and origin cleanup, PASS |
| DM-23 | `independence_wave_professionalize_army` in Security | Recognized origin, integrated militia/training/force gates | security major | 360-day selectable mission | high | N/D+C3 | T+C+1x; demobilizes DM-22 reserve, PASS |

### Former-host relations, patrons, network, and league

| Row | Implementation and category | Availability | Cost | Duration / timeout | AI | Localisation | Cleanup and static disposition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DM-24 | `independence_wave_offer_ceasefire_line` in Host Relations | Active host conflict or frontier escalation | diplomatic light | 75-day bilateral decision | high | N/D+C3 | R+C+host validity, PASS |
| DM-25 | `independence_wave_divide_state_property` in Host Relations | Active origin with ceasefire or recognized host talks | administration standard + 2 civilian factories | 180-day negotiation | high | N/D+C3 | R+C+1x, PASS |
| DM-26 | `independence_wave_negotiate_citizenship_and_return` in Host Relations | Active origin with living host and population dispute | administration standard + 2 civilian factories | 240-day negotiation | high | N/D+C3 | R+C+1x, PASS |
| DM-27 | `independence_wave_accept_limited_claims` in Host Relations | Provisional origin with current host offer | diplomatic light | Immediate | low | N/D+C3 | 1x; removes matching claims, PASS |
| DM-28 | `independence_wave_demand_recognition_by_force` in Host Relations | Recognized military route with valid former host | strategic | 120-day ultimatum | low | N/D+C3 | R+C+single active target, PASS |
| DM-29 | `independence_wave_offer_association_or_reunion` in Host Relations | Compatible bilateral route and public-support gate | strategic | 240-day bilateral decision | very low | N/D+C3 | R+C+sovereignty cleanup, PASS |
| DM-30 | `independence_wave_prepare_reclamation_defense` in Host Relations | Active origin with detected host preparation | security major | 75-day emergency mission | urgent | N/D+C3 | T+C+1x, host-threat expiry/war gate, PASS |
| DM-31 | `independence_wave_accept_arms_mission` in Patrons | Provisional origin, active sponsor, route access | diplomatic standard | 75-day targeted decision, 365-day cooldown | standard | N/D+C3 | R+C+channel cap, PASS |
| DM-32 | `independence_wave_accept_industrial_credits` in Patrons | Provisional origin, valid sponsor and project capacity | administration standard + 2 civilian factories | 240-day targeted decision | standard | N/D+C3 | R+C+1x sponsor project, PASS |
| DM-33 | `independence_wave_invite_security_advisers` in Patrons | Provisional origin, sponsor and security problem | diplomatic light | 120-day targeted decision, 365-day cooldown | standard | N/D+C3 | R+C+target validity, PASS |
| DM-34 | `independence_wave_grant_base_or_transit_rights` in Patrons | Recognized origin, sponsor request and viable location | strategic | 180-day treaty decision | low | N/D+C3 | R+C+1x, treaty invalidation, PASS |
| DM-35 | `independence_wave_balance_patrons` in Patrons | Recognized origin with at least two active patrons | patron-balance helper | 240-day selectable mission, 365-day cooldown | high | N/D+C3 | T+C+escalating route state, PASS |
| DM-36 | `independence_wave_buy_out_concession` in Patrons | Regional power with active concession and economy gate | strategic + 3 civilian factories | 240-day decision | high | N/D+C3 | R+C+1x, PASS |
| DM-37 | `independence_wave_expose_foreign_interference` in Patrons | Recognized origin with evidence and domestic support | diplomatic light | 45-day decision, 365-day cooldown | low | N/D+C3 | R+C+target cooldown, PASS |
| DM-38 | `independence_wave_choose_client_future` in Patrons | Provisional/recognized origin with dominant patron and route | strategic | Immediate permanent route choice | low | N/D+C3 | 1x; locks incompatible routes, PASS |
| DM-39 | `independence_wave_recognize_new_independence_wave_country` in Network | Active Event 006 origin and valid target | diplomatic light | Immediate, 180-day cooldown | standard | N/D+C3 | target death and cooldown safety, PASS |
| DM-40 | `independence_wave_send_civil_service_cadres` in Network | Recognized origin with capacity surplus and valid member | administration standard + 2 civilian factories | 120-day targeted decision, 365-day cooldown | standard | N/D+C3 | R+C+target/war validity, PASS |
| DM-41 | `independence_wave_contribute_emergency_reserve` in Network | Recognized league member with safe surplus | safe-reserve helper | Immediate, 180-day cooldown | standard | N/D+C3 | contribution ledger and bounded cooldown, PASS |
| DM-42 | `independence_wave_request_collective_recognition` in Network | League actor and valid low-recognition member | diplomatic standard + 1 civilian factory | 180-day shared decision, 365-day cooldown | high | N/D+C3 | R+C+target death/route cleanup, PASS |
| DM-43 | `independence_wave_request_border_arbitration` in Network | Compliant charter member, arbitration charter, exact live dispute pair | diplomatic standard | 120-day targeted decision, 365-day cooldown | high | N/D+C3 | R+C; clears pending case, claims, stored target, PASS |
| DM-44 | `independence_wave_rescue_threatened_member` in Network | Compliant league member and threatened member capital | rescue-aid helper | 75-day shared crisis, 365-day cooldown | urgent | N/D+C3 | R+C; material reserve/refund and abandonment record, PASS |
| DM-45 | `independence_wave_convene_founding_congress` in League | Recognized eligible origin, member/standing/common-cause gate | strategic + 2 civilian factories | 300-day selectable mission | high | N/D+C3 | T+C+1x global congress guard, PASS |
| DM-46 | `independence_wave_adopt_charter_pillar` in League | Active congress and eligible member | diplomatic standard | Immediate vote, 90-day cooldown | high | N/D+C3 | pillar result and route lock, PASS |
| DM-47 | `independence_wave_challenge_league_leadership` in League | Regional power, plausible support, no emergency lockout | strategic | 120-day selectable mission | low | N/D+C3 | T+C+1x/cooldown lifecycle, PASS |
| DM-60 | `independence_wave_call_charter_expulsion_vote` in League | Charter authority, anti-puppetry, valid factual expulsion target | strategic + 2 civilian factories | 120-day decision, 365-day cooldown | very low | N/D+C3 | R+C; clears active case and target, PASS |
| DM-61 | `independence_wave_sponsor_member_coup` in League | Compliant member, anti-puppetry charter, live non-war target | security standard | Immediate, 365-day cooldown | very low, radical modifier | N/D+C3 | Records factual coup case without persistent target pointer, PASS |
| DM-62 | `independence_wave_request_charter_war_mandate` in League | Compliant defensive-congress member with valid external target | diplomatic standard + 1 civilian factory | 45-day decision, 180-day cooldown, then 365-day authorization | low | N/D+C3 | R+C; one target authorization and matching-war consumption, PASS |

### Borders, formables, and high chaos

| Row | Implementation and category | Availability | Cost | Duration / timeout | AI | Localisation | Cleanup and static disposition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DM-48 | `independence_wave_survey_claimed_districts` in Borders | Regional power, package ambition and valid claimed region | administration standard + 2 civilian factories | 120-day regional decision | high | N/D+C3 | R+C+1x region, PASS |
| DM-49 | `independence_wave_sponsor_plebiscite` in Borders | Regional power, valid claim, local support and observer target | strategic + 3 civilian factories | 240-day targeted mission | high | N/D+C3 | R+C+target cooldown, PASS |
| DM-50 | `independence_wave_negotiate_transfer` in Borders | Regional power, valid host and compensation route | strategic + 3 civilian factories | 180-day bilateral mission | high | N/D+C3 | R+C+target cooldown, PASS |
| DM-51 | `independence_wave_prepare_border_ultimatum` in Borders | Regional military route and security commitment | border-ultimatum helper + 3 civilian factories | 120-day crisis | low | N/D+C3 | R+C+1x operation guard, PASS |
| DM-52 | `independence_wave_integrate_settled_district` in Borders | Regional power/formable with controlled settled state | integration helper + 3 civilian factories | 360-day regional decision | high | N/D+C3 | R+C+1x state/origin, PASS |
| DM-53 | `independence_wave_discover_regional_identity` in Formables | Recognized origin, package family and focus unlock | administration standard + 2 civilian factories | 120-day decision | high | N/D+C3 | R+C+1x family, PASS |
| DM-54 | `independence_wave_convene_formation_congress` in Formables | Regional power, consent/territory/legitimacy proof | strategic + 3 civilian factories | Formable congress window mission | high | N/D+C3 | T+C+1x transaction guard, PASS |
| DM-55 | `independence_wave_proclaim_military_union` in Formables | Regional military route, controlled territory and formation proof | selected-formable-commit helper | Immediate, long integration follow-through | high | N/D+C3 | 1x; old decision cleanup through formation helper, PASS |
| DM-56 | `independence_wave_integrate_member_region` in Formables | Formable, controlled member region and administration path | integration helper + 3 civilian factories | Formable integration duration | high | N/D+C3 | R+C+1x region/origin, PASS |
| DM-57 | `independence_wave_sponsor_another_breakaway` in High Chaos | Regional radical origin, Evolution 5 and valid candidate | breakaway-sponsorship helper + 2 civilian factories | 180-day targeted decision, 365-day cooldown | low | N/D+C3 | R+C+one candidate, PASS |
| DM-58 | `independence_wave_coordinate_reclamation_fronts` in High Chaos | Radical league, focus/member/reserve gates and injective front preflight | reclamation-front helper | 180-day selectable mission | high | N/D+C3 | T+C+1x; staged rollback before payment, PASS |
| DM-59 | `independence_wave_transform_league_charter` in High Chaos | Radical league leader, high-chaos support and common-cause gate | strategic | 180-day selectable mission | high | N/D+C3 | T+C+1x irreversible charter, PASS |

### FORM-03 Low Countries post-charter progression

| Row | Implementation and category | Availability | Cost | Duration / timeout | AI | Localisation | Cleanup and static disposition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FORM03-D01 | `independence_wave_form03_convene_language_convention` in FORM-03 | Post-charter LCX, convention focus, no active language action | administration standard + 1 civilian factory | 180-day decision | urgent | N/D+C3 | R+C; cancellation reduces accommodation, PASS |
| FORM03-D02 | `independence_wave_form03_open_multilingual_service_examinations` in FORM-03 | Parallel-services or working-register model, unlocked action | administration standard + 1 civilian factory | 150-day decision | high | N/D+C3 | R+C; carrier-state invalidation, PASS |
| FORM03-D03 | `independence_wave_form03_publish_member_language_codes` in FORM-03 | Selected model, convention complete, service focus | administration light | 120-day decision | high | N/D+C3 | R+C; carrier-state invalidation, PASS |
| FORM03-D04 | `independence_wave_form03_establish_federal_language_appeals` in FORM-03 | Territorial-administration model and appeals unlock | administration standard + 1 civilian factory | 180-day decision | high | N/D+C3 | R+C; carrier-state invalidation, PASS |
| FORM03-D05 | `independence_wave_form03_extend_protected_local_services` in FORM-03 | Working-register model and local-service unlock | protected-services helper + 1 civilian factory | 180-day decision | high | N/D+C3 | R+C; carrier-state invalidation, PASS |
| FORM03-D06 | `independence_wave_form03_reconnect_sambre_meuse_corridor` in FORM-03 | Post-charter LCX, state 34 owned and controlled, no active works | 3 civilian factories, 20 command power, 20 trains | 180-day decision | high, war-averse | N/D+C3 | R+C; state-loss integration penalty and AFX hook, PASS |
| FORM03-D07 | `independence_wave_form03_coordinate_frisian_waterway_standards` in FORM-03 | Post-charter LCX, state 36 owned and controlled, no active works | 3 civilian factories, 20 command power, 10 trains, 5 convoys | 180-day decision | high, war-averse | N/D+C3 | R+C; state-loss integration penalty and AGX hooks, PASS |
| FORM03-D08 | `independence_wave_form03_standardize_rail_and_customs_manifests` in FORM-03 | Corridor-standards focus and no competing industrial action | diplomatic standard + 1 civilian factory | 180-day decision | high | N/D+C3 | R+C; carrier-state invalidation, PASS |
| FORM03-D09 | `independence_wave_form03_request_development_compact_technical_mission` in FORM-03 | Development Compact member, reserve at least 80, no current commitment | administration light + 1 civilian factory + 20 reserve | 180-day decision | high | N/D+C3 | R+C; once-only reserve refund, PASS |
| FORM03-D10 | `independence_wave_form03_invite_sovereign_corridor_partners` in FORM-03 | LCX corridor standards and exact unresolved BEL/HOL/LUX associate | diplomatic standard + 1 civilian factory | 180-day decision | high | N/D+C3 | R+C; exact late-member dispatch, PASS |
| FORM03-D11 | `independence_wave_form03_ratify_confederal_charter` in FORM-03 | Activated by convergence focus, real language scope and both values at least 70 | Completed convergence work, no click cost | 360-day selectable mission | urgent | N/D | T+C; exact full, compromise, or rupture resolver, PASS |
| FORM03-D12 | `independence_wave_form03_resubmit_confederal_charter` in FORM-03 | Repairable compromise and full ratification gate | diplomatic standard | 180-day decision | urgent | N/D+C3 | R+C; bounded failure-cycle state, PASS |
| FORM03-D13 | `independence_wave_form03_reopen_charter_talks` in FORM-03 | Rupture outcome and no competing industrial action | strategic + 3 civilian factories | 360-day decision | high | N/D+C3 | R+C; rupture persists on cancellation, PASS |
| FORM03-D14 | `independence_wave_form03_repair_language_settlement` in FORM-03 | Compromise and accommodation below ratification threshold | administration standard + 1 civilian factory | 180-day decision | high | N/D+C3 | R+C+1x failure cycle, PASS |
| FORM03-D15 | `independence_wave_form03_repair_industrial_compact` in FORM-03 | Compromise and integration below ratification threshold | 3 civilian factories, 20 command power, 20 trains | 240-day decision | high | N/D+C3 | R+C+1x failure cycle, PASS |
| FORM03-D16 | `independence_wave_form03_implement_member_language_guarantees` in FORM-03 | Sovereign BEL/HOL/LUX associate with pending accession | administration light + 1 civilian factory | 180-day decision | high, democratic modifier | N/D+C3 | R+C; member lifecycle guard, PASS |
| FORM03-D17 | `independence_wave_form03_fund_associate_corridor_share` in FORM-03 | Sovereign associate, pending corridor invite and exact owned/controlled legal state | diplomatic light + 1 civilian factory | 180-day targeted decision | high, war-averse | N/D+C3 | R+C; target/member invalidation, PASS |
| FORM03-D18 | `independence_wave_form03_withdraw_from_autonomous_membership` in FORM-03 | Living sovereign associate with no active member action | diplomatic standard | 120-day decision | very low | N/D+C3 | R+C+1x tombstone, no territory/subject shortcut, PASS |

## Decision-category lifecycle notes

- The core categories are phase-gated rather than permanent stores: Founding, Government, Security, Recognition, Host Relations, Patrons, Network, League, Borders, Formables, and High Chaos each have category visibility gates in `common/decisions/categories/006_independence_wave_categories.txt`.
- `independence_wave_form03_low_countries_category` stays visible when empty only for its bounded carrier, sovereign-associate, invitation, or eligible-BEL situations. Its per-action gates prevent the post-charter panel from becoming a generic regional mission list.
- The crisis category appears only for real pressure, an active crisis mission, or a currently eligible request. The SCN-008 ledger category is temporary and player-owned, visible only while a frozen blocked-row display flag and at least one row exist.
- DM-60 through DM-62 remain inside the League category but carry their own compliant-charter, factual-ground, target, and crisis-lock gates. This prevents the League category from using its broad visibility as permission to open an invalid enforcement action.

## Mission quality, costs, requirements, AI, and route locks

- The accepted map uses concrete actions rather than political-power exchanges. Core cost helpers spend civilian project capacity, manpower, command power, Army XP, infantry equipment, support equipment, trains, convoys, fuel, stability, war support, and the relevant ledger value. The only `cost = 0` controls are the SCN-008 rejection-ledger Previous, Next, and Close controls, which change no gameplay value and have AI base zero.
- The 59-current-mission inventory has distinct timeout and cancellation behavior. Matrix missions use target, host, route, phase, state-control, capital, active-slot, or lifecycle flags to avoid passive success and duplicate active missions.
- Current AI values are centralized in `common/script_constants/006_independence_wave_decision_constants.txt` with values of 2, 5, 10, 25, and 100 for very low through urgent. The row table records each base, while source modifiers further suppress invalid routes, active war projects, unsafe reserve actions, non-radical coups, and inappropriate targets.
- Targeted host, network, league, border, patron, and associate actions use `target_root_trigger`, `target_trigger`, or stored-target revalidation. DM-43, DM-44, DM-60, and DM-62 clear active target state after resolution or cancellation. DM-58 proves distinct participants before accepting its shared operation.

## Localisation and tooltip findings

Every accepted implementation id has title and description localisation. The 27 custom-cost keys reached by the matrix and all 133 current Event 006 decision custom-cost keys have base, blocked, and tooltip localisation.

DM-01 and FORM03-D11 are the two expected no-custom-cost rows. DM-01 is a real garrison mission, and FORM03-D11 is a selectable convergence objective whose work is already paid and completed before ratification. Neither is a free reward click.

No raw matrix prerequisite was found exposed as a missing player-facing cost key. The targeted and complex rows retain custom tooltips or named helper-backed conditions.

## Cleanup and exploit-risk findings

No matrix-row exploit loop was found at source.

- DM-22 creates only the predeclared understrength reserve under its fixed id and exact anchor proof. Professionalization and origin cleanup call the matching demobilizer.
- DM-41 writes ledgered reserve contributions under a material-surplus gate and cooldown.
- DM-43 and DM-60 through DM-62 use active-case/target clearing, valid-target checks, cooldowns, and factual grounds. DM-62 issues only one 365-day target-specific authorization, consumed by the matching declaration.
- DM-52, DM-54 through DM-56, and the FORM-03 projects use state, formation, transaction, and lifecycle guards rather than repeatable core or integration rewards.
- FORM03-D06 and FORM03-D07 apply a cancellation integration penalty when their owned-and-controlled project state is lost. FORM03-D09 refunds its committed reserve once only. FORM03-D18 preserves sovereign withdrawal and its tombstone without a territory or subject-state shortcut.

## Doubled scenario and host-crisis contract audit

The current static contract is present and internally aligned across `common/script_constants/006_independence_wave_crisis_constants.txt`, `common/decisions/006_independence_wave_crisis_decisions.txt`, `common/scripted_triggers/006_independence_wave_crisis_triggers.txt`, `common/scripted_effects/006_independence_wave_crisis_effects.txt`, `docs/events/006_independence_wave/systems/triggerable_scenario.md`, and the current source-of-truth map.

- The automatic ladder is `6/8/10/14/20`, and the World Collapse target is 20. The 14 and 20 bands remain fail-closed below admitted package and reservation capacity.
- `independence_wave_open_host_crisis` is a 120-day selectable mission. It requires either sub-35 percent stability or a qualifying 50-resistance occupation state, pays the security-standard material package plus command power and stability, records its cause, and queues `chaosx.nr6.3` only while pressure and the shared release barrier still hold.
- Cancellation and unavailable queue resolution apply the documented failure consequence, clear runtime flags, and begin the 365-day cooldown. Requester-loss recovery clears the queued state before the country scope disappears.
- SCN-008 attempts the current 138 bound package rows, records 55 unbound rows and 13 route-only overlays as non-release surfaces, and applies type behavior only after the frozen release transaction commits.
- Universal Former Hosts sets the temporary distinct-target policy and uses the `independence_wave_scenario_belligerence_targets` array. Failed declarations roll target marks back, and the universal cleanup clears flags, array entries, and policy. Wars of Separation deliberately keeps that policy disabled, retaining one viable host war per release even when releases share a former host.

### Current SCN-008 matrix gaps

No source defect is identified, but the following evidence remains open:

1. The declared eight-mode by four-intensity matrix, or 32 cells, has not been executed with source/MCP scenario evidence.
2. The scenario cases for zero-ready candidates, mixed living/unready/anchor-collision failures, protected-host survival, Event 005 collisions, each of the three Universal Belligerence rules, repeated launches, and ledger-array alignment remain unobserved.
3. The host-crisis mission still needs execution evidence for success queueing, blocked resolution, cancellation, requester loss, bounded retry, final committed receipt, and repeated use after cooldown.
4. No live HOI4 process, save/load, AI selection, or player-owned GUI/event-log observation was run by this audit.

## Recommended fixes and follow-up

No narrow source patch is recommended.

The parent should retain the current row sources and pursue the outstanding evidence through `docs/events/006_independence_wave/systems/triggerable_scenario.md` and the owning SCN-008/allocator audit surface. Do not weaken package admission, host protection, former-host target reservation, crisis payment, or the 14/20 fail-closed capacity gate to make an unobserved cell appear successful.

## Changed files and validation

Changed file:

- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_decision_mission_matrix_current_audit_2026_08_02.md`

Changed decision, mission, scripted-GUI, localisation, focus, and helper identifiers: none.

Meaningful validation:

- Current row extractor confirmed 80 accepted rows, 80 unique source identifiers, no source-missing row, and no missing row-level name, description, availability, `available`, AI, or cleanup field.
- Current matrix and full Event 006 custom-cost localisation triplet inventories passed.
- Current direct-child mission inventory confirmed the 59/19 mission and selectable-mission contracts.
- Direct source tracing covered category lifecycle, the core payment helpers, DM-22 demobilization, DM-43 and DM-60 through DM-62 target cleanup, FORM-03 state and member cancellation, the doubled ladder, host crisis, and SCN-008 former-host target reservation.

Skipped meaningful validation:

- No 32-cell SCN-008 source/MCP scenario matrix was executed.
- No live game, save/load, runtime AI, or player-owned GUI/Event Log observation was run.
- No probability evaluation was run because a complete campaign candidate pool and external state set were not declared.

Simplifications, omissions, and blockers: no gameplay fallback or simplification was introduced. The audit is complete as a current static row-level decision and mission audit, while the SCN-008 and host-crisis execution evidence listed above remains open.

Skills used: `hoi4-decisions-missions`, `chaos-redux-events`, and `chaos-redux-subagents`.
