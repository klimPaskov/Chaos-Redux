# Event 021 Random Civil War decision and mission audit — 2026-09-20

## Disposition

This is a read-only audit handoff for the current checkout. The decision and mission system remains incomplete and runtime-unverified; this report does not claim completion or final acceptance.

No gameplay files were modified. The only intended new file from this audit is this handoff.

Status labels used below are source-proven, runtime-unverified, stale, incomplete, and blocked. Source-proven means the current checked-out files demonstrate the behavior or defect. Runtime-unverified means the source contract exists but live activation, expiry, state scopes, visual wrapping, or gameplay consequences have not been observed. Stale means an earlier handoff describes a source contract that the current checkout no longer supports or does not fully prove. Incomplete means a required contract is only partly implemented or only partly evidenced. Blocked means the required MCP or live evidence could not certify the claim.

## Scope and references

The audit read AGENTS.md; .agents/skills/chaos-redux-decisions-missions/SKILL.md; .agents/skills/chaos-redux-events/SKILL.md; .agents/skills/chaos-redux-scripted-gui/SKILL.md; .agents/skills/chaos-redux-subagents/SKILL.md; the Event 021 decision and mission prompt; the Event 021 specification parts for decisions, Evolution I, Evolution II, Evolution III, and AI/balance; the Event 021 probability scenario matrix; acceptance evidence; the action-family crosswalk; the current Event 021 overview and prior decision, mission, probability, exposure, and cleanup handoffs.

The required offline Paradox wiki pages were consulted for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, AI modding, interface modding, and scripted GUI modding. Vanilla documentation consulted included effects_documentation.md, triggers_documentation.md, modifiers_documentation.md, script_concept_documentation.md, loc_formatter_documentation.md, common/decisions/_documentation.md, and common/scripted_guis/_documentation.md. Vanilla selectable-mission precedents were checked in AFG.txt, AST.txt, and CHI_warlord_decisions.txt.

The principal current source files are common/decisions/021_random_civil_war_decisions.txt, common/decisions/categories/021_random_civil_war_categories.txt, common/scripted_effects/021_random_civil_war_decision_effects.txt, common/scripted_effects/021_random_civil_war_effects.txt, common/scripted_effects/021_random_civil_war_parent_effects.txt, common/scripted_triggers/021_random_civil_war_parent_triggers.txt, common/script_constants/021_random_civil_war_constants.txt, common/scripted_localisation/021_random_civil_war_localisation.txt, localisation/english/021_random_civil_war_l_english.yml, and interface/021_random_civil_war.gfx.

## Highest-severity findings

### P1 — Priority Front uses a different carrier from every player-facing consumer

Classification: source-proven defect; runtime-unverified only as to the exact visible symptom in the live consumer.

common/scripted_effects/021_random_civil_war_effects.txt:1026-1031, event021_set_priority_front, saves event_target:random_civil_war_anchor_state as the global event target random_civil_war_priority_front_state and sets random_civil_war_priority_front_active. It does not set normal variables random_civil_war_priority_front_state or random_civil_war_priority_front_state_id.

common/scripted_triggers/021_random_civil_war_parent_triggers.txt:890-900, event021_priority_front_depot_target_valid, requires the normal variable random_civil_war_priority_front_state. common/scripted_effects/021_random_civil_war_decision_effects.txt:131-141, event021_decision_seize_depot, also reads that normal variable. common/scripted_localisation/021_random_civil_war_localisation.txt:132-153, event021_GetCrisisTargetName and event021_GetPriorityFrontName, require both normal variables and the positive state id.

A repository search found no current assignment to random_civil_war_priority_front_state or random_civil_war_priority_front_state_id. The current writer and consumers therefore cannot agree on the selected state. In the source contract this makes the depot target trigger false, makes Seize an Opposition Depot unavailable, and makes the category Focus and Set the Priority Front text fall back to N/A even though the global event target exists. This directly fails the accepted requirement to expose the current selected or priority front in a multi-front crisis.

Recommended fix: choose one carrier contract and use it everywhere. Either mirror the state scope and id into normal variables at event021_set_priority_front and clear those mirrors in event021_clear_priority_front and lifecycle cleanup, or change the depot trigger, decision effect, scripted localisation, and log consumers to use has_event_target and event_target:random_civil_war_priority_front_state. Do not retain a mixed global-target and normal-variable contract.

### P1 — Sponsor commitment state is not closed by regional exposure cleanup

Classification: source-proven cleanup gap; runtime-unverified as to whether a later unrelated exposure or evolution review consumes the stale records first.

common/scripted_effects/021_random_civil_war_effects.txt:1190-1220, event021_cleanup_regional_exposure, clears exposure presentation, route flags, relief, armed support, role profiles, action state, mediation state, and the source scope. It does not clear random_civil_war_sponsor_commitment_active, random_civil_war_sponsor_commitment_received, random_civil_war_sponsor_id, random_civil_war_sponsor_recipient_id, random_civil_war_sponsor_front_id, random_civil_war_sponsor_support_amount, random_civil_war_sponsor_commitment_start_date, or random_civil_war_sponsor_commitment_until.

common/scripted_effects/021_random_civil_war_decision_effects.txt:264-281 and common/scripted_effects/021_random_civil_war_evidence_effects.txt:447-458 create those active, received, identity, amount, and duration records. event021_decision_end_sponsor_commitment at decision_effects.txt:386-397 clears only the active flag, records repayment, and clears sponsor evidence; it does not clear the identity and amount variables. random_civil_war_sponsor_commitment_active is also an input to the Evolution II MTTH modifiers in common/mtth/021_random_civil_war_mtth.txt:44-80, so a stale flag can affect later timing or an unrelated future role.

The parent crisis cleanup removes missions, action state, exposure flags, and global targets, but it does not visit and normalize the neighboring sponsor and recipient records. This conflicts with the Evolution II cleanup requirement that sponsor records resolve when the source war ends. It is not a demonstrated free-equipment loop, but it is a real stale-state and balance risk.

Recommended fix: add a bounded sponsor-record cleanup path invoked on source-war termination and neighbor exposure expiry, with separate handling for durable settlement/treaty proof before clearing repayment history. Clear or migrate the active and received flags, sponsor identity, recipient, front, support amount, start date, and expiry date on both owning scopes. Preserve only the historical receipt fields that the settlement and event-log contracts explicitly require.

### P2 — Reconstruction action and rail mission can award two infrastructure increases on one stored rail state

Classification: source-proven balance risk; runtime-unverified as to frequency and whether the intended design treats the two increments as separate stages.

common/scripted_effects/021_random_civil_war_decision_effects.txt:191-216, event021_decision_reconstruct_administration, immediately adds one infrastructure level to random_civil_war_rail_mission_state when the state is owned and controlled. common/scripted_effects/021_random_civil_war_decision_effects.txt:476-499, event021_mission_secure_rail_complete, can add another infrastructure level to the same stored state and also grants train recovery, authority, and pressure relief.

The rail mission is only 30 days in common/script_constants/021_random_civil_war_constants.txt:563-572. Its available and timeout checks accept a state with a supply node or infrastructure above the gate, not an explicit unrepaired receipt. A reconstruction action followed by a short hold can therefore produce two infrastructure increments when the state remains valid. The source does not prove that this is always an exploit, but the reward stack is stronger than a single named rail objective and is shorter than the other 150/180-day objectives.

Recommended fix: either make the action repair a general administration step while the mission protects a distinct unrepaired junction, or require an explicit damaged-rail receipt before the mission and remove the duplicate infrastructure reward. If two stages are intended, document and balance the combined result through the same named scenarios and a measured mission sequence.

### P2 — Full role-specific AI and balance remain uncertified

Classification: incomplete and blocked for runtime probability; source role factors are present.

The current decision file has profile and route factors, but many candidates retain base weight 1 outside a narrow profile or phase condition. This is deliberate source structure, not proof that all roles rank distinctly. The current MCP decision evaluation had 48 unresolved inputs and no normalized probabilities. The current mission evaluation had 5 unresolved inputs and no complete runtime mission pool. No independent auditor certificate was available at handoff time.

The source also hard-zeros invalid or nonviable support targets, mediator military support, near-defeat or resource-starved support, and invalid priority-front depot use. Those are good fail-closed gates, but the named role scenarios have not been evaluated with a complete typed state fixture.

## Category presentation and phase exposure

### Static category and dynamic status

Classification: source-proven; visual runtime proof blocked/non-certifying.

common/decisions/categories/021_random_civil_war_categories.txt:9-21 defines one normal category, event021_civil_war_crisis_category, with visible_when_empty = no, one static picture GFX_decision_category_picture_021_civil_war, one icon GFX_decision_category_021_civil_war_crisis, and priority 82. interface/021_random_civil_war.gfx:10-18 registers the picture and icon, and the referenced static picture DDS exists.

The category localisation at localisation/english/021_random_civil_war_l_english.yml:9-10 is concise in structure: State Authority value and band, threshold guidance, phase, Focus, and one strongest-pressure summary. The scripted localisation exposes only State Authority as the main visible numeric value and maps the phase and summary without exposing a raw pressure ledger.

The category satisfies the no-custom-scripted-GUI design in the specification. The mandatory GUI read-only calls were still attempted. The corrected synthetic call to hoi4.gui_inspect returned GUI_INSPECTED with zero inspected elements, fidelityCounts modelled = 0, approximated = 1, missing = 1, and a diagnostic set containing GUI_WINDOW_MISSING among global graph diagnostics. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2417d4f2233d5cf0ae50fac80113ecff95ece97001f8de623dc7a6470376178f/167246f4d29be43a468366280008e7ea5748336b17897c9248f5c426f9a3f792/gui-inspect.e4038371fbed6095.json.

The matching hoi4.gui_render call returned GUI_RENDERED with only a tiny synthetic event021_civil_war_crisis_category-full.svg artifact and no rendered category elements. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5ef75a6a7ef175373b04e952f07db1c5485b233c549b09cce1f12071075d1eb7/679d80295c006c62e8e3a2d37565a7757a3d8fe8940425b5c825e1947a65e4eb/event021_civil_war_crisis_category-full.svg. This is not a production visual pass; the ordinary decision category is not a scripted-GUI window and has no inspectable scripted hierarchy. Text wrapping, clipping, actual decision-card spacing, and in-game click regions remain runtime-unverified.

### Visible action and mission counts

The following counts are source-proven from the visible and phase triggers. They describe the maximum before resource availability removes a card.

| Phase or role | Visible primary actions | Active missions | Assessment |
| --- | ---: | ---: | --- |
| Opening government | Four opening actions plus Offer Emergency Terms when the government can offer settlement, for a maximum of five | Hold the Capital | Meets the normal three-to-five action ceiling and one-mission target. |
| Opening opposition | Secure Arsenals, Defend the Capital, Review Command Loyalty, and Seize an Opposition Depot only when its target is valid; the carrier defect currently removes the depot path | Hold the Capital | Intended count is four; current source behavior can fall to three and leaves the priority target unresolved. |
| Multi-front government or claimant | Review Loyalty, Integrate Formations, Set the Priority Front, and possibly Offer Emergency Terms | Hold the Capital | Four actions and one mission before resource or settlement gates. |
| Regional exposure | Relief Corridor, Monitor Border, Support Government, Support Opposition, and Offer Mediation, with target validity and one neighbor-action lock | No Event 021 mission | Maximum five actions. The Evolution II specification allows a compact action surface and up to two neighbor missions, so zero is not a strict source violation, but a literal one-mission-per-phase acceptance reading is not met. |
| Settlement plus reconstruction | Reconstruct Administration, End Sponsor Commitment when active, one obligation action, Protect Communications, and Review Regional Administration, for a maximum of five | Secure the Rail Spine plus Hold Settlement Terms can overlap | Within the action ceiling and within the one-to-three mission ceiling, but the rail reward stack requires balance review. |
| Evolution III prevention | Review Command Loyalty and Protect Communications | No mission | Two actions. This is an accepted stable/prevention exception in spec part 6, which calls for one or two targeted preventive actions, rather than a normal active-war phase. |

Phase precedence is reconstruction, settlement, regional exposure, multi-front, active war, and prevention in common/scripted_localisation/021_random_civil_war_localisation.txt:59-82. After settlement, both random_civil_war_settlement_phase and random_civil_war_reconstruction_phase are set at common/scripted_effects/021_random_civil_war_parent_effects.txt:5301-5308; reconstruction wins the displayed phase label while settlement obligation actions and the settlement mission remain available. This is intentional overlap but should be checked live for confusing phase wording.

## Decision category lifecycle notes

Opening and multi-front crisis countries enter the shared category through event021_country_can_manage_crisis, while exposed neighbors enter through event021_country_can_manage_exposure and prevention countries enter through event021_country_can_prevent_fracture. Settlement and reconstruction use their own phase gates and the category remains hidden when no applicable action is visible.

Actions become one-use through per-action flags, missions become one-use through active/success/failed or objective-met receipts, and parent cleanup removes all three mission entries. The category can therefore shrink after an action, expand when the crisis changes phase, and disappear after settlement/reconstruction cleanup. The source contract is coherent, but the live ordering of activation, removal, source-war expiry, and re-entry is unverified.

The settlement-to-reconstruction transition intentionally leaves both phase flags present until parent cleanup. The display prioritizes Reconstruction, while settlement obligations and Hold Settlement Terms remain actionable. This is a lifecycle overlap rather than a second category, but it makes the exact player-facing phase wording and action ordering a runtime check.

## Cognitive-load notes

The category has one main visible numeric value, State Authority, with four readable bands and next-threshold guidance. Pressure is not exposed as a second raw number; the category instead exposes one strongest-pressure summary. This is source-proven and meets the specification's anti-ledger intent.

Normal active phases stay at three to five source-visible primary actions before resource gating. Exposure has at most five actions and a shared one-action lock. Settlement plus reconstruction has at most five actions and at most two missions. Prevention has two actions by accepted Evolution III design. No phase in the source intentionally exposes a wall of raw counters or more than six primary actions.

Visible values are not all equally meaningful in the current checkout. State Authority has a band, threshold, consequence, and response. The phase and strongest-pressure summary have clear meaning. The selected/priority front is supposed to carry that same significance but currently falls back to N/A because of the carrier mismatch. Mission durations and costs are visible in localisation, while cost tooltip prose does not repeat the numeric amounts.

The category text is compact in source, but ordinary-category line wrapping and card spacing were not certifiable through the synthetic GUI route. The player-facing visual density therefore remains runtime-unverified.

## Action cost and requirement audit

Every action uses centralized gate and spend constants in common/script_constants/021_random_civil_war_constants.txt:398-499. The source gates, custom-cost triggers, negative resource spends, and visible icon-first cost strings agree by action. Requirements such as role, phase, target viability, controlled state, and settlement obligation are not counted as spendable cost types.

| Action | Exact source gate and role condition | Spendable cost and count | Cost result |
| --- | --- | --- | --- |
| event021_secure_arsenals | Opening; unused arsenal action | 10 £command_power + 100 £infantry_equipment_text_icon + 1 £GFX_train_texticon | 3 types; source-proven. |
| event021_defend_capital | Opening; unused capital action | 15 £command_power + 150 £infantry_equipment_text_icon + 1000 £manpower_texticon | 3 types; source-proven. |
| event021_review_loyalty | Opening, multi-front, or prevention; unused loyalty action | 10 £command_power + 10 £army_experience + 25 £pol_power | 3 types; source-proven. |
| event021_seize_depot | Opening opposition only; valid owned/controlled opening-core priority state with supply node or military factory; unused depot action | 10 £command_power + 100 £infantry_equipment_text_icon + 10 £GFX_motorized_equipment_text_icon | 3 types; gate is currently broken by the carrier mismatch. |
| event021_open_relief_corridor | Regional exposure; unused relief action and no recent relief flag | 15 £pol_power + 10 £GFX_motorized_equipment_text_icon + 5 £convoy_texticon | 3 types; source-proven. |
| event021_offer_emergency_settlement | Settlement phase or active government offer path; no resolved talks or used settlement action | 25 £pol_power + 15 £command_power + 150 £infantry_equipment_text_icon + 1000 £manpower_texticon | 4 types, exactly at the ceiling; source-proven. |
| event021_reconstruct_administration | Reconstruction; unused reconstruction action | 20 £pol_power + 1 £GFX_train_texticon + 500 £manpower_texticon | 3 types; source-proven. |
| event021_integrate_formations | Multi-front; unused integration action | 10 £army_experience + 150 £infantry_equipment_text_icon + 1000 £manpower_texticon | 3 types; source-proven. |
| event021_set_priority_front | Multi-front; unused priority action and at least one opening-core state | 10 £command_power | 1 type; target carrier is incomplete. |
| event021_monitor_border | Regional exposure; neighbor action unused | 10 £command_power + 10 £GFX_motorized_equipment_text_icon + 5 £convoy_texticon | 3 types; source-proven. |
| event021_support_government | Exposure; government target valid and viable; neighbor action unused | 20 £pol_power + 150 £infantry_equipment_text_icon + 5 £convoy_texticon | 3 types; also transfers 100 infantry to the target, which is an effect and not a fourth spend. |
| event021_support_opposition | Exposure; opposition target valid and viable; neighbor action unused | 20 £pol_power + 150 £infantry_equipment_text_icon + 5 £convoy_texticon | 3 types; also transfers 100 infantry to the target, which is an effect and not a fourth spend. |
| event021_offer_mediation | Regional exposure; neighbor action unused | 20 £pol_power + 10 £command_power + 5 £convoy_texticon | 3 types; source-proven. |
| event021_end_sponsor_commitment | Settlement phase; sponsor commitment active and disengagement unused | 15 £pol_power + 10 £command_power | 2 types; stale commitment records remain after this action. |
| event021_complete_disarmament | Settlement phase; disarmament obligation; unused disarmament action | 10 £army_experience + 100 £infantry_equipment_text_icon + 500 £manpower_texticon | 3 types; source-proven. |
| event021_complete_coalition_governance | Settlement phase; coalition obligation; unused coalition action | 20 £pol_power + 10 £command_power | 2 types; source-proven, but it reuses mediation constants. |
| event021_protect_communications | Prevention, reconstruction, or settlement; unused communications action | 10 £command_power + 1 £GFX_train_texticon | 2 types; source-proven. |
| event021_review_regional_administration | Reconstruction or settlement; unused administration action | 15 £pol_power + 500 £manpower_texticon | 2 types; source-proven. |

No action exceeds four spendable resource types. No fifth spend is hidden in a tooltip, confirmation effect, scripted helper, or secondary panel in the reviewed paths. The support transfers are not free-unit grants because each support action consumes 150 infantry equipment while transferring 100, plus political power and convoys. Action-use flags, the neighbor-action lock, and settlement/reconstruction phase gates also prevent straightforward repeat-click loops.

All reviewed cost strings are icon-first and use the expected texticons, including £pol_power, £command_power, £infantry_equipment_text_icon, £GFX_train_texticon, £GFX_motorized_equipment_text_icon, £convoy_texticon, £army_experience, and £manpower_texticon. No literal resource-name replacement was found.

The main localisation clarity gap is that the *_cost_text_tooltip strings describe the role of the payment without repeating its numeric amount. The visible *_cost_text strings do show exact numbers and icons, so this is a medium/low tooltip clarity issue rather than a missing-cost issue. Visual wrapping remains runtime-unverified.

## Mission quality and lifecycle

All three missions follow the vanilla selectable-mission shape: selectable_mission = yes, a centralized days_mission_timeout, complete_effect that records an active receipt, timeout_effect that resolves the objective, and a cancel_trigger. This is source-proven and matches the vanilla AFG, AST, and CHI selectable-mission precedents. Activation, expiry cadence, cancellation, and scope behavior remain runtime-unverified.

| Mission | Owner and category | Region, map requirement, and duration | Success | Failure or cancellation | Duplicate risk |
| --- | --- | --- | --- | --- | --- |
| event021_hold_the_capital_mission | Active crisis country; opening or multi-front | Capital controlled by ROOT, infrastructure above zero, supply node above zero, and capital defense active or capital held; 150 days | Clears active receipt, sets success, adds authority and same-tag government leverage if the timeout check still passes | Timeout sets failed, removes active receipt, loses authority, raises pressure, and adds claimant leverage; cancels when crisis is no longer manageable or settlement is resolved | Success/failed flags block reactivation; parent cleanup removes the mission. |
| event021_secure_rail_spine_mission | Reconstruction phase; active crisis country | Stored rail mission state is owned and controlled by ROOT, in opening cores, with a supply node or infrastructure above the gate; 30 days | Clears active receipt, sets rail secured, may add infrastructure, recovers trains, adds authority, and reduces pressure | Timeout clears active receipt, sets rail lost, loses authority, raises pressure; cancels when reconstruction is no longer manageable | Rail secured flag blocks reactivation; parent cleanup removes the mission. |
| event021_hold_settlement_terms_mission | Settlement phase with an active obligation | Obligation hold-until date exists, obligation is active, and it is not already failed; 180 days | Checks the exact obligation objective and no committed recurrence, marks objective met, and reviews the parent obligation | Timeout marks obligation failed and reviews it; cancels when settlement management or obligation activity ends | Objective-met and active-receipt flags prevent duplicate selection; parent cleanup removes the mission. |

The settlement objective maps recognition, disarmament, rail security, sponsor repayment, and coalition governance to their exact completion flags in common/scripted_triggers/021_random_civil_war_parent_triggers.txt:717-740. There is no second payment click after mission selection or objective completion.

The short 30-day rail duration is visibly distinct from 150 and 180 days, but it may be too forgiving for an infrastructure reward that can be paired with the instant repair action. The current source has no explicit partial-success branch. That is acceptable where the binary objective is intended, but the accepted mission prompt calls for partial success when useful, so the absence should be reviewed against the intended rail design rather than assumed complete.

## AI validity, role specificity, and route locks

Source role factors are present in common/decisions/021_random_civil_war_decisions.txt:46-176, 211-215, 257-262, 296-336, 373-376, 409-412, 454-473, 515-533, 568-580, 612-615, 649-687, 721-761, and 802-880.

The source gives the following meaningful role or state preferences:

- Government actors prefer Secure the Arsenals and Defend the Capital.
- Command claimants and government actors prefer Review Command Loyalty.
- Opposition actors prefer Seize an Opposition Depot, subject to the broken priority carrier.
- Humanitarian pressure and exposure prefer Open a Relief Corridor.
- Negotiators and failing authority prefer Offer Emergency Terms, while hardliners receive the concession discouragement factor.
- Successor sides prefer reconstruction; multi-front and command claimants prefer integration; multi-front sides prefer priority-front selection.
- Containment profiles prefer border monitoring.
- Opportunistic sponsors and aligned targets prefer the corresponding government or opposition support; mediator profiles hard-zero military support.
- Mediator profiles prefer mediation; opportunistic sponsors receive concession discouragement.
- Negotiators prefer sponsor disengagement and coalition governance; government actors prefer disarmament.
- Capital or supply risk prefers communications protection; failing authority prefers regional administration.
- Missions use government, opposition, Event 006, same-tag, reconstruction, settlement, and phase factors.

The target validity triggers require live scopes, normal-human or side identity, non-capitulation, controlled-state count, and either factories or a leader. The support decisions also require target viability and hard-zero AI weights for invalid targets, near defeat, and insufficient political power, infantry equipment, or convoys. These are source-proven route locks. The current priority-front mismatch defeats the depot route despite its intended hard-zero guard.

The base AI constants are base action 1, base mission 1, priority factor 1.5, and discouragement factor 0.75. Because many actions have no additional role factor outside their narrow condition, the source does not by itself prove distinct ordering in all named personas. That claim is blocked by incomplete scenario fixtures and the unresolved MCP evaluations.

## Neighbor relief versus armed support

Classification: source-proven separation; exposure expiry and cross-scope cleanup remain runtime-unverified.

event021_decision_open_relief_corridor sets civilian-relief active and available flags, adds stability, reduces pressure, and applies the administrative idea. It never sets random_civil_war_neighbor_armed_support.

event021_decision_support_government and event021_decision_support_opposition set random_civil_war_neighbor_armed_support, record the specific recipient and sponsor commitment, and transfer 100 infantry equipment units to the selected side. They do not set civilian relief. Both support actions require their own valid and viable target.

event021_decision_offer_mediation clears armed-support and civilian-relief-available state, and the shared event021_neighbor_action_used flag prevents a second neighbor action in the same exposure window. event021_cleanup_regional_exposure clears relief and armed support independently. This correctly avoids treating displaced civilians as an enemy, but the live source-war expiry path still needs user validation.

## Localisation and tooltip review

Action names and descriptions are concise, actor-aware, and generally state the real public act. Target requirement tooltips cover the depot, government-support, opposition-support, capital, rail, and settlement conditions. Mission descriptions name the location or obligation and state the success/failure consequence.

The category text is concise in structure but not fully correct because the Focus path reads the missing normal priority variables. The fallback N/A is safe but hides a required state.

The cost rows are compact and icon-first. The cost tooltip prose omits numeric amounts even though the visible cost rows include them. This should be treated as a player-comprehension gap, especially for the four-type settlement action.

The GUI inspect/render calls did not produce a real ordinary decision-category hierarchy, so no claim is made about text overflow, card spacing, clipping, asset scaling, or click-region alignment. The production render evidence required for a scripted GUI is not applicable because the accepted design explicitly forbids a custom scripted GUI, but the ordinary category still needs user-owned visual validation.

## Cleanup and exploit-risk notes

Positive source cleanup includes removal of all three missions, Event 021 ideas, phase/action flags, relief and armed-support flags, mediation timing, front integration state, global registries, priority-front global target, and global host/anchor targets. Parent cleanup is at common/scripted_effects/021_random_civil_war_parent_effects.txt:6958-7066. Crisis cleanup and global registry cleanup are at common/scripted_effects/021_random_civil_war_effects.txt:1894-1990.

The remaining sponsor commitment fields described in the P1 finding are the main cleanup gap. Timed recent flags event021_relief_corridor_recent, event021_border_monitoring_recent, and event021_mediation_recent are not explicitly cleared by the broad cleanup effect; they may be intentional cooldown receipts, but their interaction with exposure re-entry is runtime-unverified.

The missions are protected against ordinary duplicate selection by active, success, failed, secured, objective-met, and obligation flags. Parent cleanup uses remove_mission, so removed missions do not run their complete or timeout effect. No direct free-unit loop was found. Government and opposition support cost more infantry equipment than they transfer. Depot use is one-use per crisis and requires a valid controlled opening-front state when its target carrier works.

The main balance risks are the rail double-repair stack, sponsor stale-state acceleration, and the limited distinctiveness of base-1 AI weights. The coalition action reuses mediation_political_power_gate and mediation_command_power_gate at decisions.txt:655-682; this is currently numerically consistent but creates tuning coupling and can silently change two unrelated actions together.

## MCP evidence and exact blockers

All fresh probability calls used workspace mod_chaos_redux_ea3b2d67c2c0 and were read-only.

| Call | Result | Evidence and limitation |
| --- | --- | --- |
| hoi4.probability_inspect, decision_ai_will_do, source common/decisions/021_random_civil_war_decisions.txt | PROBABILITY_SOURCE_INSPECTED | 18 candidates, poolComplete = false, availableCandidates = 0, requiredInputs = 12, unresolved = 0, sourceRevision 748d962d21d92e5ab4ec91f9f8a93ef538f82e23bf5d69d6b05ab9ae105fe64b, sourceHash d942638f25e433a83c1a662b45196ec500df4507d393db0bc387caacebe55c60. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0b7768c80a6805e9541ae84f4e5c1024dbefd5438d285f46d2a975e8ade667c0/b84418724d50ccb4a098567bb61b1901244c4ba0241780645bb63deef2c9263b/probability-inspect-d942638f25e4.json. No complete runtime country/phase/resource pool was supplied. |
| hoi4.probability_inspect, mission_ai_will_do, the same source | PROBABILITY_SOURCE_INSPECTED | 3 candidates, poolComplete = false, availableCandidates = 0, requiredInputs = 2, unresolved = 0, sourceRevision 748d962d21d92e5ab4ec91f9f8a93ef538f82e23bf5d69d6b05ab9ae105fe64b, sourceHash d942638f25e433a83c1a662b45196ec500df4507d393db0bc387caacebe55c60. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/07c5c72ee7aa29e97e71dd8dfa4c1f645a5512669858ff2a4b3eb089d9249cad/5973819c090e13db7e9210efaa3578796c681e51cc1200b51cfa210615e68fbf/probability-inspect-d942638f25e4.json. No complete runtime mission state was supplied. |
| hoi4.probability_evaluate, decision_ai_will_do, one empty fixture with all 18 candidates | PROBABILITY_ANALYZED_PARTIAL | Analysis probability-a7e4a78f5600fdf58f8cdeed, scenarioHash 69d40c188c2a440d81294de4f8e339ba1336b79ae8c506617541c9534713c5a5, 48 unresolved items, 16 diagnostics, no normalized probabilities. JSON artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e79de4a26ad88c0e2f9659795f491877f6b526fcb7e19a1dd0861a99135cb74c/c31f77c51560c766e1b6a435ea3bf274b4a297d42274ea7cd68ae43b937857c5/probability-a7e4a78f5600fdf58f8cdeed.json. The service explicitly surfaced unsatisfied priority factors and unresolved hidden/phase/target inputs. |
| hoi4.probability_evaluate, mission_ai_will_do, one empty fixture with all 3 missions | PROBABILITY_ANALYZED_PARTIAL | Analysis probability-877a956035b2b4c2b848c42e, scenarioHash 56c4c70fffa6f638652608cc0b066bff97f57d1cae33fa9b6330c8b314be2f4b, 5 unresolved items, 4 diagnostics. The empty fixture reported Hold the Capital never eligible, which is expected for an empty capital/resource state and is not a live ranking. JSON artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1d7250997043a6108414aba21b7724c4468431d4c4c1f0f7898116e933ef74ea/ca2bd53a2fcdb7fe7e3e007e512b0207a30cc62359717e98750bd0ff95ebbc71/probability-877a956035b2b4c2b848c42e.json. |
| hoi4.probability_sweep, decision_ai_will_do, empty fixture paths | INTERNAL_ERROR | No artifact and no analysis id. The route returned Unexpected internal error. |
| hoi4.probability_sweep, mission_ai_will_do, empty fixture paths | PROBABILITY_SWEEP_RANGE_REQUIRED | No artifact. Exact blocker: Every sweep path requires a scenario range, numeric alternatives, or numeric state value; path has_variable in scenario E021-DECISION-MISSION-EMPTY-FIXTURE-2026-09-20. |
| hoi4.event_inspect, lint, selector event chaosx.nr21.1 | EVENT_INSPECTED_PARTIAL | Revision a8fde3e58546f004e81d855d73d29674ae3c5be8f8941a1caf9586621929a6657, graphHash c83030c9d67b704f9c6437d31b7e4f5000463e6431ae40865f5b74e4cb15af21, zero blocking diagnostics, but validation deferred large-workspace helper/lifecycle projections. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6298fbd55bb7c912feda5080027697e0e116241230c49045ae8d72dd70be66fa/b47b52074d3e11bf7b88781f1ab71b6614016da8be955359ba90015a9d2de485/event-lint-a8fde3e58546.json. |
| hoi4.gui_inspect, synthetic ordinary-category name | GUI_INSPECTED | Zero elements inspected and GUI_WINDOW_MISSING among truncated global diagnostics. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2417d4f2233d5cf0ae50fac80113ecff95ece97001f8de623dc7a6470376178f/167246f4d29be43a468366280008e7ea5748336b17897c9248f5c426f9a3f792/gui-inspect.e4038371fbed6095.json. This is not a production ordinary-category layout certificate. |
| hoi4.gui_render, synthetic ordinary-category name at 1920x1080 | GUI_RENDERED | Returned a synthetic SVG with no category elements. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5ef75a6a7ef175373b04e952f07db1c5485b233c549b09cce1f12071075d1eb7/679d80295c006c62e8e3a2d37565a7757a3d8fe8940425b5c825e1947a65e4eb/event021_civil_war_crisis_category-full.svg. No visual pass is claimed. |

An initial GUI call was rejected with MCP error -32602 because the supplied scenario contained unsupported schemaVersion and a state object instead of a supported named state. The corrected call used scenario id E021-GUI-CATEGORY-EMPTY-2026-09-20 and state normal. The window-name route remained synthetic because the source is an ordinary decision category.

The independent chaosx_ai_probability_auditor was spawned with fork_context = false, read-only scope, and the current decision/mission files. Two bounded waits returned no final status or certificate at the time of writing. Independent probability confirmation is therefore pending and blocked, not inferred from the parent receipts.

## Prior handoff reconciliation

decision_mission_parent_refresh_2026-09-19.md remains useful for the vanilla selectable-mission contract and the source-level 18-action/3-mission inventory, but it explicitly left independent probability and live mission cadence open. It does not detect the current priority-front carrier mismatch.

decision_mission_presentation_repair_2026-09-19.md is stale/incomplete where it says Priority Front records the action flag and treats the presentation repair as sufficient. The current source records the global target but not the normal variables consumed by the depot trigger and localisation. Its recorded historical MCP receipts are not current-revision certification.

regional_exposure_cleanup_2026-09-19.md is incomplete for sponsor cleanup. It correctly describes clearing exposure, role, relief, armed-support, and action state, but current source does not clear the sponsor commitment flag and identity/amount/date records listed above.

docs/events/021_random_civil_war/acceptance_evidence.md still labels Event 021 Needs Testing and says runtime, helper-expanded lifecycle, probability, performance, and user-owned live evidence remain open. That status is consistent with this audit.

## Concrete recommended follow-up

1. Repair the priority-front carrier contract and rerun the decision, localisation, depot-target, event-log, and cleanup checks against the same named source revision.

2. Add and document sponsor/recipient cleanup at exposure expiry and source-war termination, preserving only durable treaty and historical-log receipts. Verify that the Evolution II MTTH and future exposure actions no longer see a stale sponsor commitment.

3. Decide whether reconstruction action plus rail mission is a two-stage reward. If it is not, remove the duplicate infrastructure path or add an unrepaired-state gate. If it is, tune the 30-day duration and combined rewards through an explicit mission sequence audit.

4. Run complete, typed MCP probability fixtures for opening government, opening opposition, multi-front command claimant, containment neighbor, mediator neighbor, opportunistic sponsor, negotiator settlement, successor reconstruction, and prevention. Use the same named scenarios for evaluation, sweep, and compare; do not convert the current empty-fixture raw scores into probabilities.

5. Review cost tooltip wording so the payment explanation includes exact icon-and-number pairs or clearly points the player to the numeric cost row. Keep every spendable value icon-first.

6. Separate coalition-governance tuning constants from mediation constants if those actions are expected to balance independently.

7. User-owned live validation remains required for phase counts, category text, card spacing, mission selection and timeout, mission cancellation, source-war expiry, neighbor target death, settlement plus reconstruction overlap, save/reload, and final cleanup. No game process was launched by this audit.

## Validation boundary

## Parent reconciliation — current checkout after bounded repairs

The findings above describe the pre-repair source and are stale for the three named defects. The current checkout now mirrors `random_civil_war_priority_front_state` and `random_civil_war_priority_front_state_id` when `event021_set_priority_front` publishes the global carrier, and `event021_clear_priority_front` plus decision cleanup clear the mirrors. `event021_cleanup_regional_exposure` now clears paired sponsor and receiving-side commitment receipts on expiry or source-war invalidation. Reconstruction writes `event021_reconstruction_rail_repaired` on the stored rail state, the action refuses a repaired state, and `event021_secure_rail_spine_mission` refuses and cancels against that receipt.

The current source-only MCP refresh found the decision surface with 18 candidates and 12 required runtime inputs and the mission surface with three candidates and three required runtime inputs. Both pools remain incomplete without a typed runtime fixture. The current mission artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a3d52c55981d467228836a0eae1e25e3f74c66fed6602a4bb332618d2bf7ac58/8786f2b9c625d6c49d93a4b9d1a662a64cbb661887f47000ce80fac34d19b790/probability-inspect-f6f499612056.json`, and the current decision source artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/32d11fa2d620586d87ac6422d7b63ade8b3910b9a1caf8743b009abbb1f55d83/efa5d9b2b6013f9d0e42f1f834cbfcd4a2a707f09d5b3e094007bd7c5c62abc9/probability-inspect-f6f499612056.json`; a direct decision-adapter refresh also returned `INTERNAL_ERROR`. A parent before/after compare attempt returned `PROBABILITY_SURFACE_EMPTY` and is not treated as a balance certificate.

The current root `hoi4.event_inspect` lint for `chaosx.nr21.1` returned zero blocking diagnostics and zero skipped sources in artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6010d8e4738e1b479fa8f213c797894ee81d0725da52e6412013f650d83bab5/56607bcee413125a78e01bbd132146fe99d3e5993da9f01e5c01e830447322f6/event-lint-a8fde3e58546.json`, but validation remains partial because helper-expanded lifecycle analysis was deferred. The parent therefore classifies the repaired decision/mission source as source-repaired and structurally linted, but runtime-unverified and probability-blocked; Event 021 remains `Needs Testing`, not complete.

## Parent follow-up after the postrepair audit

The current source now closes the remaining bounded findings identified by the postrepair completion review: mission-first and reconstruction-first rail ordering share both state receipts, and redirected sponsor cleanup reaches the actual host or claimant recipient through a stored scope pointer. The manual scenario's locked enumeration also bypasses successor grace while retaining the shared individual-crisis load cap. These edits are source-level only; live mission order, exposure expiry, typed probability comparison, and helper-expanded lifecycle evidence remain open.

The fresh source and MCP evidence supports a detailed audit, not a completion claim. No gameplay patch, GUI rewrite, localisation edit, balance change, or fallback implementation was made. No plan handoff was created because this report is the requested audit handoff and the identified fixes remain bounded follow-up work.
