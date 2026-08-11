# Event 012 Africa final decision, mission, and mechanics certification - 2026-08-10

## Certification status

This is a strictly read-only audit of the current shared worktree. No gameplay, decision, mission, scripted GUI, localisation, event, focus, or documentation source outside this handoff was patched, staged, or committed by this audit.

The Event 012 decision and mission surface is source-complete for 96 of 102 matrix action rows. Six high-chaos rows remain explicitly `blocked_with_gate` in the acceptance ledger (rows 71-76); their selectors, profiles, guards, outcome hooks, and localisation are present, but their declared fictional-disease authorization/native receipt or strange-formation package/manifest gates are intentionally closed. The feature is therefore not a clean 102-of-102 gameplay certification.

The audit treats the user waiver of live/in-game validation as authoritative. Missing live screenshots or campaign observations are not counted as source omissions. Runtime-scope uncertainty, MCP fidelity/truncation, and incomplete probability normalization are recorded below rather than converted into false completion claims.

## Evidence and acceptance inputs

I read `AGENTS.md`, `.agents/skills/hoi4-decisions-missions/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, and `.agents/skills/hoi4-focus-trees/SKILL.md`. I consulted the required offline Paradox wiki pages (data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, AI modding, interface modding, and scripted GUI modding) and the relevant vanilla documentation and precedents under `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\`.

The complete Event 012 specification set was read: `docs/specs/012_africa_specs/specs/012_africa_spec_part_1_core_progression.md` through `012_africa_spec_part_9_priority_member_country_packages.md`, all five diagrams under `docs/specs/012_africa_specs/diagrams/`, and all six prompts under `docs/specs/012_africa_specs/prompts/`, including `africa_decision_mission_prompt.md`. The row-level sources were `docs/specs/012_africa_specs/matrices/012_africa_decision_mission_matrix.csv`, its notes file, and `docs/plans/012_africa_plans/012_africa_acceptance_ledger.csv`.

Latest implementation evidence consulted includes `012_africa_decision_final_audit_2026-08-09.md`, `012_africa_decisions_full_final_2026-08-09.md`, `012_africa_decisions_full_fix_followup_2026-08-09.md`, `012_africa_actions_71_76_final_2026-08-09.md`, `012_africa_promoted_tiera_final_2026-08-09.md`, `012_africa_highchaos_operations_2026-08-10.md`, `012_africa_elephant_operations_final_2026-08-10.md`, `012_africa_nile_gold_operations_2026-08-10.md`, `012_africa_rsa_final_2026-08-09.md`, `012_africa_charter_gui_final_layout_2026-08-09.md`, `012_africa_focus_final_audit_2026-08-10.md`, `012_africa_ai_probability_final_audit_2026-08-10.md`, and `012_africa_final_spreadsheet_update_2026-08-10.md`.

Current source touchpoints audited were `common/decisions/012_africa_decisions.txt`, `common/decisions/categories/012_africa_categories.txt`, `common/decisions/012_africa_elephant_operations_decisions.txt`, `common/decisions/012_africa_rsa_decisions.txt`, `common/decisions/012_africa_promoted_tiera_decisions.txt`, `common/scripted_effects/012_africa_action_effects.txt`, `common/scripted_effects/012_africa_effects.txt`, `common/scripted_effects/012_africa_diaspora_effects.txt`, `common/scripted_effects/012_africa_elephant_operation_effects.txt`, `common/scripted_effects/012_africa_promoted_tiera_effects.txt`, `common/scripted_effects/012_africa_rsa_effects.txt`, the matching scripted triggers/constants, `events/012_african_union.txt`, `events/012_africa_diaspora_protocol.txt`, `events/012_africa_rsa.txt`, and the W1-W5/world-order scripted effects and triggers.

## Exact matrix-row coverage

The matrix contains 102 rows. Static reconciliation against current selectors, action constants, shared action profiles, full/partial/failure disposition branches, AI profile dispatch, and player-facing localisation found no missing row. The ledger disposition is 96 `implemented` and six `blocked_with_gate`.

| Matrix rows | Family | Exact decision keys | Ledger status |
| --- | --- | --- | --- |
| 1-10 | Protection | `guarantee_sovereignty`, `open_aid_corridor`, `dispatch_charter_mission`, `deploy_volunteers`, `intervene_against_coloniser`, `evacuate_leaders_archives`, `recognise_provisional_government`, `secure_border_sanctuary`, `break_blockade`, `emergency_relief_column` | 10 implemented |
| 11-20 | Accession | `offer_defence_charter`, `offer_development_charter`, `offer_federal_charter`, `offer_crown_charter`, `offer_peoples_charter`, `offer_security_charter`, `offer_sacred_ecological_compact`, `renegotiate_accession_clauses`, `hold_accession_referendum`, `admit_member_in_emergency` | 10 implemented |
| 21-30 | Regional congress | `convene_regional_congress`, `settle_overlapping_claims`, `create_regional_charter`, `form_regional_federation`, `restore_historical_polity`, `approve_direct_integration_schedule`, `guarantee_regional_representation`, `fund_congress_security`, `invite_diaspora_delegates`, `enforce_congress_settlement` | 10 implemented |
| 31-40 | Integration | `build_administrative_bridge`, `connect_member_capitals`, `standardise_customs`, `integrate_security_services`, `harmonise_officer_corps`, `negotiate_autonomy_statute`, `launch_local_settlement_programme`, `grant_core_recognition`, `impose_emergency_administration`, `federalise_restored_polities` | 10 implemented |
| 41-50 | Economy | `survey_continental_resources`, `build_regional_rail_spine`, `expand_river_transport`, `modernise_continental_port`, `create_local_processing_chain`, `continental_procurement_contract`, `food_security_reserve`, `resource_sovereignty_review`, `charter_development_fund`, `continental_industrial_plan` | 10 implemented |
| 51-58 | Diaspora | `open_voluntary_return_registry`, `charter_passage_programme`, `build_returnee_housing`, `invite_afro_american_technical_mission`, `veterans_and_volunteers_programme`, `diaspora_investment_bonds`, `citizenship_and_representation_convention`, `diaspora_emergency_evacuation` | 8 implemented |
| 59-66 | Rival blocs | `monitor_rival_bloc`, `offer_rival_arbitration`, `support_rival_member_defection`, `counter_foreign_patronage`, `prepare_member_exit_terms`, `suspend_disloyal_member`, `emergency_leadership_vote`, `contain_regional_secession_war` | 8 implemented |
| 67-70 | High chaos | `consult_oracle_network`, `bargain_with_the_green`, `petition_the_rain`, `defy_the_drought` | 4 implemented |
| 71-76 | High chaos | `contain_emergent_disease`, `research_disease_countermeasure`, `weaponise_fictional_pathogen`, `awaken_stone_cohort`, `train_gorilla_heavy_infantry`, `organise_pan_sappers` | 6 blocked_with_gate |
| 77-84 | Scramble response | `seek_international_recognition`, `prepare_anti_sanctions_network`, `answer_foreign_ultimatum`, `mobilise_continental_defence`, `disrupt_expedition_planning`, `offer_base_withdrawal_treaty`, `call_global_anti_colonial_conference`, `break_intervention_coalition` | 8 implemented |
| 85-92 | World order | `sponsor_continent_unifier`, `mediate_continent_union`, `prepare_continental_war`, `force_continent_submission`, `form_dynamic_two_continent_union`, `declare_the_world_is_one`, `administer_world_regions`, `contain_terminal_high_chaos` | 8 implemented |
| 93-99 | Constitutional route crises | `convene_federal_deadlock_conference`, `conduct_first_continental_election`, `arbitrate_continental_succession`, `balance_food_and_industrial_plan`, `review_victorious_commander_loyalty`, `ratify_confederal_emergency_action`, `review_covenant_obligation` | 7 implemented |
| 100 | Post-unification governance | `hold_postwar_constitutional_review` | 1 implemented |
| 101 | Host opening | `recover_failed_host_proof` | 1 implemented |
| 102 | Regional congress and restorations | `promote_priority_member_package` | 1 implemented |

Rows 71-73 are source-present disease branches with Evolution III, `africa_fictional_pathogen_review_authorized`, episode/research/payload, target-validity, and weapon cooldown checks. Rows 74-76 are source-present strange-force branches with Evolution III, `africa_strange_formation_package_ready`, active-action and formation caps, owned/controlled state proof, per-family asset/audio manifests, spawned-once, and cooldown checks. The acceptance ledger intentionally keeps all six rows blocked until their approved package/API/authorization is available; no weather, real-pathogen, model, tag, unit, or free-unit fallback is authorized.

For every row, the matrix requirements, dynamic cost inputs, duration band/default, objective, success, partial success, failure, and cleanup text are carried into the shared quote and immutable action record. `africa_action_objective_is_complete` and the four duration missions consume that recorded objective; `africa_resolve_action`, `africa_cancel_action`, and `africa_timeout_current_action` then dispatch the row-specific full/partial/failure semantics and result localisation. This is the row-level objective contract used by the acceptance ledger, rather than a generic completion timer.

## Severity-sorted findings and concrete follow-up

### High - completion gate: six high-chaos rows remain blocked

`contain_emergent_disease`, `research_disease_countermeasure`, `weaponise_fictional_pathogen`, `awaken_stone_cohort`, `train_gorilla_heavy_infantry`, and `organise_pan_sappers` cannot be counted as available actions while the declared review/package flags remain unset. The current fail-closed behavior is correct and prevents unsafe or exploitative substitutes, but the 102-row acceptance target is incomplete until the parent accepts the fictional disease API/authorization and the separately approved formation/template/entity/model/audio package.

### Medium - shared mission timeout scope remains runtime-unproven

The four shared missions use `days_mission_timeout = FROM.africa_active_action_duration_days` at `common/decisions/012_africa_decisions.txt:488-566`. Source lint and the D1 quote/record contract accept the scoped duration, and the user waived live testing, but the exact mission-engine `FROM` scope at timeout is not proven by the available offline/MCP evidence. A frozen-source runtime check remains parent-owned; this is an unresolved runtime semantic, not a missing source branch.

### Medium - mandatory GUI MCP evidence is complete but fidelity output is globally noisy

Read-only `hoi4.gui_inspect` for `africa_charter_window` returned `GUI_INSPECTED`, `complete=true`, 107 inspected elements, and the current artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/746e648b388c561c661c300aee2ea00ccce7a6d6c61e7eb0ef534b06a377278a/89fbf25495c91b36101e3e96b71821a45b1726998340796cbff37c8b206da527/gui-inspect.9e4448585eefd88d.json`. The result reports modelled 983, approximated 17, ignored 133, missing 6, unsupported 64, and unresolved 13, with global index-collision, overlap, and diagnostic truncation warnings. These diagnostics are global/offline-tool fidelity counts rather than evidence of a missing Event 012 button; the prior source audit found 35 buttons, all click effects/triggers, 56/56 text/buttonText localisation keys, and all button rectangles inside the 1000x680 window.

Read-only `hoi4.gui_render` returned `GUI_RENDERED` with the current full render artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c545f294678e367c1b44c2fa3f9914a1eeffd283462bc2d388a839302163e663/2636a7d5d2c4f2bb5303dfb672c0f2972283b8615988a836205555004d6ba551/africa_charter_window-full.svg`. The MCP response was `MCP_RESPONSE_TRUNCATED`, validation was false with no blocker list, and no rewrite was attempted. The detailed post-layout inspect/render/click-region and 1920px state matrix remain in `012_africa_charter_gui_final_layout_2026-08-09.md`.

### Medium - weighted analysis is bounded, not normalized

The current main decision source inspection (`common/decisions/012_africa_decisions.txt`, `decision_ai_will_do`) is artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/28a0f741d1675cfebd0b783f5117cae299b37dbf81d6fc557a7f4d5a7358dbd/7f8244e6bc41a3ef18e4fa9398449837201d6013582fa64f58197e41e21d54b5/probability-inspect-3c6be98a0c68.json` with 210 candidates, 23 required inputs, unresolved inspect 0, and `poolComplete=false`. The action-effect random-list inspect is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/80ff48db822129219902c2b74a8d885f5be6282a66d7c0a903ee649aa43edab7/9c18e6269c0e29f762178cee705dc8d8015f99f8440101130d00e964aa2fb977/probability-inspect-0dc62e23ca53.json` with 14 candidates, one unresolved construct, and `poolComplete=false`. The mission adapter returned no mission candidates and redirected to the decision/controller adapter; no exact AI click probability or long-horizon balance claim is justified.

The promoted Tier A, priority-member, RSA, and elephant source inspections are retained in `012_africa_ai_probability_final_audit_2026-08-10.md`. The current direct artifacts are Tier A `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8ebf00dc311c93200b7001622a7e8d3a363f6247c3c271014d4964d573fd6307/75b3352ba35b0d337a19d8fb7ccb41c1fa53a7e0d999520a673fa15e5384d088/probability-inspect-3bed4d1e2482.json`, priority member `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fb7ede3ce6a59911bbb3f796f99d199e84b446a0ba6abff97428b566bbeba869/a35a723730e7ad1568e24b98001a0ba9def2a7201894d61d0f3a71c516859671/probability-inspect-cf9d9c016d05.json`, RSA `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/591302bc1da32db709044ad003198c58ba64091602bafd5783bead5f8fa227dd/f0b037e26dfccbf2cf75098f76eecb2352bb921aa59fe1eb004728a1322859/probability-inspect-39f39e6b16a8.json`, and elephant `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c3eac16fecccbb982c509182938c166514cb0ad61d5e94f3c5e1428804755696/762a8362f5e61fa0cbb6c76a44e049cdab6f07339498142694366b01d4e07a76/probability-inspect-12381b652998.json`. These artifacts are source evidence only; elephant artifacts in particular predate the late tightening and require a same-scenario rerun after source freeze.

### Low - list-only late families are intentional

The charter GUI exposes eight recurring action families. Constitutional crisis, post-unification, host-opening, regional-restoration, Scramble, world-order, W4 union, and W5 terminal operations remain ordinary decision-category surfaces or package/event-owned surfaces rather than extra GUI tabs. This is the documented clutter-control design, not an omitted button family.

## Decision category lifecycle notes

`africa_charter_council_category` at `common/decisions/categories/012_africa_categories.txt:9-14` is visible only to the current host and owns `scripted_gui = africa_charter_window`. The eight recurring host pages (`protection`, `accession`, `regional_congress`, `integration`, `economy`, `diaspora`, `rival_bloc`, and `high_chaos`) are visible only when the selected family matches; high chaos additionally requires `africa_evolution_iii_logged`.

The non-recurring categories are phase and package gated: `africa_host_transfer_actions_category` is successor/congress controlled; `africa_priority_member_natural_disaster_actions_category` is the bounded non-host exception; `africa_scramble_actions_category` requires Africa Is One plus an active Scramble response; `africa_world_order_actions_category` requires world-order/scramble-aftermath/world-end state; `africa_world_polity_actions_category` is package-only; constitutional crisis requires a committed constitution; post-unification requires Africa Is One; host opening requires the failed first-proof flag; and regional restorations requires the League congress unlock.

Selector decisions deliberately use `cost = 0` as the quote/selection layer. The actual host or selected-country execution decisions at `common/decisions/012_africa_decisions.txt:451-483` apply `custom_cost_trigger = africa_selected_action_dynamic_cost`, `custom_cost_text = africa_selected_action_dynamic_cost`, and `africa_begin_quoted_action_against_target`. This is not a free-action loop: the shared begin effect re-quotes the exact target, validates phase/capacity/specific requirements, charges the concrete quote, records the target and generation, and either resolves an instant action or activates one of the four shared timed missions.

The GUI writes overlay, member, state, and family selectors only. It does not execute action effects, scan the world, or bypass the ordinary decision cost/target path. No other Event 012 decision category attaches a scripted GUI; elephant, RSA, promoted Tier A, W4, and W5 surfaces are ordinary decisions/missions or package event surfaces.

## Mission quality notes

| Mission | Owner/category/region | Requirements and duration | Success, failure, and cleanup | Duplicate risk |
| --- | --- | --- | --- | --- |
| `mission_africa_action_short`, `mission_africa_action_medium`, `mission_africa_action_long`, `mission_africa_action_epic` | Current Event 012 host; selected recurring/late family; target arrays `africa_active_action_*_targets` plus exact target/state snapshots. | Active action record, current host, matching duration band, current generation, and row objective; timeout reads the recorded action duration. | Objective complete calls `africa_resolve_action`; generation/contract invalidation calls `africa_cancel_action`; timeout calls `africa_timeout_current_action`; result event `chaosx.nr12.220` and idempotent cleanup clear missions, targets, reservations, capacity, disease/disaster/diaspora state, and cooldowns. | Active-action cap, exact target cooldown, generation marker, and `africa_action_record_active` prevent duplicate records; timeout scope remains runtime-unproven. |
| `africa_elephant_logistics_mission` | Current host; `africa_elephant_operations_category`; selected controlled state and exact one-division elephant roster. | Sealed formation/material contract, supply-node state, marked roster, and completion-day variable; duration `var:africa_elephant_logistics_timeout_days` (180-day contract in the final handoff). | Intact contract at completion calls `africa_elephant_complete_logistics_contract`; timeout/cancel calls `africa_elephant_fail_logistics_contract`; material, state, division, and generation witnesses are cleared. | One roster template/division cap, operation-active flags, sealed material ledger, and generation marker prevent free duplication or repeated stockpile farming. |
| `africa_elephant_protection_mission` | Current host; elephant category; protected partner and saved protection state. | Protected relationship target, defensive-war and settlement witness, exact roster, current generation; duration `var:africa_elephant_protection_timeout_days`. | Settlement witness calls `africa_elephant_complete_protection_expedition`; invalidation/timeout calls `africa_elephant_fail_protection_expedition`; saved target and active flags are cleared. | One active expedition, exact roster, target contract, and settled receipt prevent duplicate protection awards. |
| `africa_rsa_first_proof_mission` | RSA allied/continental coalition owner; RSA decision surface; civil-war corridor/coalition state. | Prepared by `africa_rsa_prepare_first_proof`; `activation = always = no`; secure civilian corridor and active civil war; duration `var:africa_rsa_first_proof_days`. | `africa_rsa_complete_civil_war_first_proof` writes the proof and consumes the first-proof ledger; cancel/timeout calls `africa_rsa_fail_civil_war_first_proof`, closes active proof, and exposes the recovery route. | Success/failure flags, compound first-proof ledger, and coalition-active guards prevent repeat proof farming. |
| Scramble phase windows (`africa_scramble_recognition_window`, `africa_scramble_coalition_window`, `africa_scramble_intervention_window`, `africa_scramble_aftermath_window`) | Current host; Scramble response category; active phase and participant/coalition arrays. | Phase-specific gates and constants for recognition, coalition, intervention, and aftermath windows. | Timeout advances the phase, launches unresolved expedition, ratifies/ closes settlement, or records prolonged negotiations; phase transition removes obsolete window. | Phase flags and settlement receipts prevent reopening an already resolved window. |
| World sponsorship obligations (`africa_world_sponsorship_*_obligation`) | Current host; world-order/package surfaces; target array `africa_world_sponsorship_targets`. | Mode-specific obligation due, host, target, package phase; duration `constant:africa_world_sponsorship_mode.obligation_days`. | Due obligation opens the matching diplomatic/material/military/ideological response; world end or no-longer-due target cancels; timeout defaults the mode. | Target obligation flags, mode, due state, and package status prevent repeated fulfilment without a new offer. |

Promoted Tier A actor operations are bounded decisions rather than new shared GUI missions. They require the current active package, cooperative human-member relationship, explicit integration consent/representation, a 90-day target lock, and a 180-day high-chaos operation cooldown; Stoneborn actor/member-war pairing and host great-power victory receipts add their own capitulation/core-control proofs. Forest actor operations call the Event 013 forest actor API and retain the same cleanup/cooldown discipline.

## Cost and requirement clarity

`africa_compute_action_quote` at `common/scripted_effects/012_africa_action_effects.txt:2543` derives concrete political power, command power, manpower, equipment, trains, convoys, fuel, civilian capacity, intelligence, stability, and war-support costs from the row base, target size, factory/state count, selected-state count, integration burden, colonial pressure, active-action load, target confidence, overlay/route/access modifiers, and war/no-access surcharges. The quote is clamped and rounded through constants, copied into the immutable action record, and displayed by `africa_selected_action_dynamic_cost` and the row contract/objective tooltips.

The diaspora actions use capacity lanes and the target-owner consent protocol. Passage/return/housing/volunteer/investment/representation routes cannot debit or move people until the target accepts; emergency evacuation additionally requires a fresh emergency-active consent. Action 54 is a technical mission and does not silently become a relocation action.

Natural-disaster member actions use the target-array decision shell with `africa_natural_disaster_member_cost_is_available` and `africa_priority_member_natural_disaster_dynamic_cost`. The member pays the caller reserve, the host owns the ordinary generation-safe action record, and failed launch refunds the reserve while a valid Event 013 attempt consumes it and enters cooldown.

Elephant operations use command power plus a sealed elephant-equipment, truck, train, and fuel material commitment. Terrain is selected from an authored state registry and an actual existing elephant division is rebound to the one-division operation roster; no generic country-wide terrain proxy or free division loop is used.

RSA routes use explicit PP/CP/material/stability gates (including trains and support equipment for relief), optional ESX branch state selection, and separate recognition/truce/cleanup handling. Promoted Tier A and world-order actions use package, consent, target-lock, war, capitulation, receipt, route, and terminal-state gates rather than flat political-power-only exchanges.

## AI validity and route locks

`common/scripted_effects/012_africa_ai_profile_effects.txt` dispatches all 102 matrix action concepts through the shared controller, with 87 early actions and 16 late actions plus the explicit sentinel. The AI uses the same action-specific target checks, dynamic quote requirements, phase/capacity checks, and cleanup outcomes as the human execution path; selector decisions with `ai_will_do = { base = 0 }` are GUI/quote selectors, not missing AI behavior.

The current AI profile and action effects contain no recurring `every_country` or `random_country` scan. The remaining `every_country` uses are one-shot prefire contact/host-pool helpers in `common/scripted_effects/012_africa_effects.txt`; natural-disaster targets iterate maintained relationship/package/Scramble/sponsorship/war-partner arrays and cap the roster at the selected-target constant (16). AI disaster choice uses the same bounded roster and `random_scope_in_array` path.

Rows 52, 53, 55, 56, 57, and 58 require diaspora owner response, capacity, target validity, and standing/emergency consent. Rows 69-70 require eligible natural-disaster actors, war, valid targets, caller cost, and cooldown. Rows 71-73 require disease authorization, episode/research/payload, valid targets, and weapon cooldown. Rows 74-76 require Evolution III, formation package readiness, active/formation caps, owned/controlled state, four family manifests, spawned-once, and cooldown guards. Rival, constitutional, host-opening, priority-member, RSA, W4, and W5 paths similarly reject dead targets, stale generations, closed routes, annexed targets, and incompatible package state.

The probability route remains `score-only`/bounded: the main decision pool is incomplete, the action random-list has one unresolved construct, the mission adapter has no independent mission candidates, and late elephant artifacts predate the final tightening. No balance conclusion is promoted to an exact click probability; the dedicated AI probability handoff records the required same-scenario rerun/compare after source freeze.

## Localisation and tooltip gaps

No missing action name, description, full-result, partial-result, failure-result, dynamic-cost, duration/objective-contract, requirement, or cleanup key was found for the 102 matrix rows in the final localisation audit. Player-facing text describes current target/route/cost/consent/phase state rather than implementation history. The Charter GUI source audit resolves all 56 text/buttonText keys, and the ordinary elephant, RSA, Tier A, W4, and W5 surfaces have their requirement/effect/cost/result keys in their owner handoffs.

The six blocked rows are intentionally visible only behind their authorization/package gates; their tooltips explain the gate rather than exposing an executable but unsupported fallback. The absence of a late-family tab in the Charter GUI is documented list-only behavior, not a localisation omission.

## Cleanup and exploit-risk notes

`africa_cleanup_action` is idempotent and generation-aware. It removes the exact shared mission, clears action actor/target/state arrays, active flags, reservations, capacity reservations, diaspora request/withdrawal state, disease receipts/seeds, natural-disaster reserve/cooldown state, and sets target cooldown. `africa_resolve_action` fires `chaosx.nr12.220`; the current `africa_cancel_action` also fires the result event after the cancellation follow-up, preventing silent cancellation. Annexed/stale targets use generation-safe cleanup.

The diaspora owner protocol clears pending request targets after resume/refusal/withdrawal, withdraws consent and emergency state before cancelling, and never transfers ownership, population, or territory. Natural-disaster launch/refund/cooldown paths clear caller and host reserves. Disease outcome branches call receipt-aware full/partial/failure/cleanup helpers. Strange-force spawn paths require explicit manifests, cap formation count, set spawned-once/cooldown witnesses, and do not grant free units while the package flag is closed.

Elephant operations retain an exact division scope, one-division roster, state terrain registry, generation marker, sealed material ledger, completion/settlement witness, and failure receipt. Tier A operations retain package identity, consent, target lock, active operation cooldown, actor/member pairing, and terminal victory receipts. W4/W5 package and union/war paths retain candidate/actor/receipt flags, ballots/clauses, successor/exile/breakup records, and terminal cleanup guards.

Residual exploit/runtime risks are the unproven mission timeout `FROM` scope, incomplete MCP normalization for dynamic pools, and the intentionally closed six-row package gates. No static free-action, equipment-farming, world-scan, war-goal-spam, core-spam, or cooldown-bypass loop was found in the current source.

## Named mechanics and cross-system links

### Diaspora consent protocol

`common/scripted_effects/012_africa_diaspora_effects.txt:70-168`, `common/scripted_triggers/012_africa_diaspora_triggers.txt`, and `events/012_africa_diaspora_protocol.txt` implement immutable request snapshots, target accept/counterterms/refusal, payment and validation only after acceptance, emergency consent, withdrawal review, and cleanup. The shared action begin path re-runs the exact quote and requirements after the owner callback.

### Natural-disaster API

`common/scripted_effects/013_natural_disasters_effects.txt` exposes a fail-closed public contract for caller type/event ID/family/group/target/sequence/news/report/aftermath/chain/log/scales. Event 012 prepares bounded strength/scales and caller reserve, then invokes the API only from the two weather actions; no unsupported direct Event 013 call or world scan is used.

### Elephant operations

`common/decisions/012_africa_elephant_operations_decisions.txt`, `common/scripted_effects/012_africa_elephant_operation_effects.txt`, and `common/scripted_triggers/012_africa_elephant_operation_triggers.txt` provide three decisions and two missions: terrain registration, logistics contract, and protection expedition. The operation uses an exact existing elephant division, authored terrain bands, material commitments, supply-node checks, protected-member targets, and generation-safe receipts.

### High chaos and promoted Tier A

The regular high-chaos page exposes rows 67-76 behind Evolution III and action-specific gates. Promoted Tier A operations in `common/decisions/012_africa_promoted_tiera_decisions.txt` and matching effects/triggers cover nonhuman rampage, forest actor rampage, Stoneborn rights violation, Stoneborn human-member war, host great-power war, and nonhuman great-power victory receipt. Cooperative human-member consent/representation, package identity, target lock, cooldown, capitulation/core-control, and Event 013 forest actor integration are all source-bound.

### RSA

`common/decisions/012_africa_rsa_decisions.txt`, `common/scripted_effects/012_africa_rsa_effects.txt`, `common/scripted_triggers/012_africa_rsa_triggers.txt`, and `events/012_africa_rsa.txt` cover Allied first-contact suppression, optional dynamic ESX state selection, civilian corridor/first proof, recognition, relief, truce, autonomy/faction restoration, and separate cleanup. The first-proof mission and failure/recovery ledger are present; no EQX consumption or unvalidated static branch was found in the final handoff.

### Charter, union, W4, W5, and world order

The Charter category/GUI routes ordinary action families through overlay/member/state/family selectors and then the shared quote/mission controller. `form_dynamic_two_continent_union` is backed by the W4 union protocol in `common/scripted_effects/012_africa_world_union_war_effects.txt` and `common/scripted_triggers/012_africa_world_union_war_triggers.txt`, which require eligible partner/faction compatibility, constituent quorum, ballots, constitution, defence/resource/withdrawal clauses, and explicit activation/strain/dissolution cleanup.

Scramble rows 77-84 are phase-windowed by recognition, coalition, intervention, and aftermath missions. World-order rows 85-92 are gated by Africa Is One, world-order phase, continental-war state, settled external package receipts, and terminal world guards. W5 package and terminal paths use candidate/actor identity, seven per-package receipts, successor/exile/breakup/terminal disposition flags, and terminal cleanup; no unbounded generic continent or world target was found.

### Focus and event links

`common/scripted_effects/012_africa_focus_route_effects.txt` opens and closes route action contracts for constitutional crisis and post-unification actions, maps overlays to concrete corridor actions, and retries AI routes through the shared action quote path. Event 012 result/cancellation/launch-rejection events are `chaosx.nr12.220`, `chaosx.nr12.221`, and `chaosx.nr12.210`; diaspora owner events are `chaosx.nr12.310` through `.313`. The current event/focus handoffs confirm these callbacks remain wired to the shared action and cleanup kernels.

## GUI evidence and ownership conclusion

The only Event 012 decision-owned scripted GUI attachment found by source search is `africa_charter_window` at `common/decisions/categories/012_africa_categories.txt:13`, implemented by `common/scripted_guis/012_africa_charter_scripted_gui.txt` and `interface/012_africa_charter.gui`. The mandatory read-only inspect and render were performed against workspace `mod_chaos_redux_ea3b2d67c2c0`, scenario `default`, resolution 1920x1080. No `hoi4.gui_rewrite` call was made, and no elephant/RSA/Tier A GUI handoff is missing because those surfaces are ordinary decision categories without scripted GUI attachment.

## Validation, omissions, and handoff

Meaningful read-only validation completed: full 102-row matrix/ledger reconciliation; selector/constant/profile/full/partial/failure coverage; AI ID and bounded-array census; localisation key audit; category and scripted-GUI attachment search; source inspection of dynamic quote, execution, mission, consent, natural-disaster, elephant, Tier A, RSA, union, W4/W5, and cleanup kernels; mandatory GUI inspect/render; and current MCP probability inspections. No gameplay files were changed and no commit/stage was created.

Skipped validation: live campaign execution, in-game screenshots, save-state probes, and engine-timeout confirmation were skipped because the user explicitly owns live/in-game testing and waived it as a completion requirement. Probability compare was not claimed because this audit did not patch gameplay and the available adapter lacks an immutable before snapshot for late owner changes; the dedicated probability handoff records the exact rerun/compare follow-up.

Simplifications and blockers: six matrix rows are intentionally blocked by approved gates; mission timeout scope is runtime-unproven; GUI MCP output has global diagnostics and response truncation; dynamic decision/mission/random pools are not fully normalizable; and elephant probability artifacts predate final tightening. No other source omission, missing localisation, missing AI equivalence, missing event/focus link, or unsafe fallback was found.

Recommended parent follow-up is to keep this handoff as the final decisions/missions certification, preserve the six gated rows as partial until their package/API approvals land, freeze source, rerun the named probability scenarios (including elephant and Tier A) with a valid immutable before snapshot, and perform the user-owned live mission-timeout/consent/cleanup checks.
