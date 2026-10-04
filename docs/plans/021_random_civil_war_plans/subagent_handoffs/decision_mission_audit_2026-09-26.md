# Event 021 decision and mission implementation audit, 2026-09-26

Disposition: unresolved. This is a bounded, read-only source audit for parent review. No gameplay, decision, scripted-localisation, or localisation source was changed. This handoff does not claim overall Event 021 completion or AI balance acceptance.

## Scope and source coverage

Read the requested decision, action-effect, parent-trigger, constants, scripted-localisation, and English localisation files. Also read the category metadata and the exact directly called authority, pressure, priority-front, exposure, settlement-review, and crisis-gate helpers needed to assess the listed decisions and missions. The picture sprite registration and its processed PNG preview were inspected because the accepted contract requires a static category picture.

Worktree note: `git status` currently marks all six requested implementation/localisation files modified. This audit did not write those files and preserved their contents. No initial status snapshot was taken before inspection, so this handoff does not attribute those modifications to a specific owner or task.

Relevant handoffs read: `localisation_audit_2026-09-26.md`, `decision_mission_audit_2026-09-25.md`, and `decision_mission_parent_refresh_2026-09-19.md`. The current source confirms the 2026-09-25 parent disposition that the alleged seven-action exposure/prevention overlap is excluded by `event021_country_can_prevent_fracture`, and that `event021_end_sponsor_commitment` belongs to the settlement signatory's sponsor-repayment obligation. The localization handoff's four-value inline settlement-cost finding remains current.

The 18 action IDs are `event021_secure_arsenals`, `event021_defend_capital`, `event021_review_loyalty`, `event021_seize_depot`, `event021_open_relief_corridor`, `event021_offer_emergency_settlement`, `event021_reconstruct_administration`, `event021_integrate_formations`, `event021_set_priority_front`, `event021_monitor_border`, `event021_support_government`, `event021_support_opposition`, `event021_offer_mediation`, `event021_end_sponsor_commitment`, `event021_complete_disarmament`, `event021_complete_coalition_governance`, `event021_protect_communications`, and `event021_review_regional_administration`.

The three mission IDs are `event021_hold_the_capital_mission`, `event021_secure_rail_spine_mission`, and `event021_hold_settlement_terms_mission`.

## Findings by severity

### P1: the rail mission can restart immediately after each failure

`event021_secure_rail_spine_mission` has `fire_only_once = no`. Its activation blocks a secured or repaired rail, but it does not block `event021_rail_spine_lost`. `event021_mission_secure_rail_timeout` sets that lost flag, clears the active marker, and applies the centralized `mission_failure_authority_loss = -8` and `mission_failure_pressure_gain = 8`. If reconstruction and the other activation conditions remain true, the same mission can become eligible again immediately, with no cooldown; each selected 30-day attempt that expires without success can reapply the failure effect. The lost flag is otherwise only cleaned up by the decision-state cleanup path.

Recommended follow-up: make a failed rail objective terminal for the current crisis, or define an explicit capped or delayed retry using centralized tuning and matching localisation. Do not infer a retry balance target from this audit.

### P1: the timed hold objectives are checked as an end-date snapshot, and the capital success resolver omits a stated gate

`event021_hold_the_capital_mission` says to keep the capital under supplied control for 150 days, and `event021_secure_rail_spine_mission` says to hold its named state for 30 days. The only in-scope calls to their success helpers are inside the timeout resolvers. Those resolvers inspect current control, infrastructure, supply, and rail eligibility at timeout; there is no in-scope daily receipt or other call that proves uninterrupted control during the stated period. Losing and retaking a target before timeout can therefore satisfy the final snapshot even though the displayed text says it must remain held.

The capital mission's `available` block additionally requires `event021_capital_defense_active` or `event021_capital_held`, but `event021_mission_hold_capital_resolve` does not test either flag before dispatching `event021_mission_hold_capital_complete`. A timeout can therefore record success when the physical capital checks pass even if the defense receipt is absent at resolution.

Recommended follow-up: either track the hold condition through the full timer and resolve from that receipt, or describe and implement a deadline snapshot. Keep the capital defense/held receipt identical between the availability and success predicates. Validate selection, timeout, and cancellation ordering in the live consumer.

### P2: the settlement action exceeds the separate three-value inline cost limit

`event021_offer_emergency_settlement_cost_text` and `event021_offer_emergency_settlement_cost_text_blocked` display political power, command power, infantry equipment, and manpower in one row. The action has four distinct spendable types, which is within the hard four-type action budget, but violates the separate maximum of three inline values. All four values are still explicitly paid and displayed, and the fourth must remain explicit in a concise full-cost tooltip if the row is reduced to three values.

### P2: rail mission activation does not require a rail target variable

The activation block's negated repaired-state check is true when `random_civil_war_rail_mission_state` is absent because the inner `AND` then fails. Activation does not otherwise require the variable. The mission can thus start in reconstruction without a target, while `available` and the timeout resolver require the target variable. Such a mission cannot succeed and can feed the repeat-failure loop above.

Recommended follow-up: require the target at activation and apply the same validity predicate used by `event021_secure_rail_requirement_tt` and the timeout resolver. Preserve intentional failure when a valid target is lost after activation.

### P2: the priority-front action does not gate payment on the target pointer consumed by its effect

`event021_set_priority_front.available` requires a nonempty `random_civil_war_opening_core_states` array and command power, but does not require or validate `event_target:random_civil_war_anchor_state`. `event021_decision_set_priority_front` charges the 10 command power, sets `event021_priority_front_action_used`, and applies authority/pressure outcomes before calling `event021_set_priority_front`. That setter only stores the priority state and activates the target when `has_event_target = random_civil_war_anchor_state` is true. A missing pointer can therefore consume the action and cost without setting the intended target. `event021_clear_priority_front` is called by the parent terminal cleanup, and the depot predicate separately checks the mirrored state variable's ownership, control, opening-core membership, and supply node or arms factory.

Recommended follow-up: share an explicit current-anchor validity gate between availability and the setter, including the actual state membership/ownership conditions, so the cost row, payment, and target mutation agree.

### P2: ordinary decision rendering and exact simultaneous UI state remain unverified

The current source phase guards prevent the previously reported seven-action state. Before `event021_neighbor_action_used` is set, exposure can present five candidates: relief, border monitoring, government support, opposition support, and mediation. `event021_country_can_prevent_fracture` excludes that uncommitted exposure state. After the shared neighbor-action flag is set, monitoring, both support actions, and mediation hide, while prevention actions may appear. This is a source-level gate analysis, not proof of the rendered or currently affordable row count.

The category description and the four-value settlement row were not rendered. The corrected `hoi4.gui_inspect` request for `windowName = countrydecisionview` and `{id, state: normal, flags: {}}` timed out after 180 seconds with `timed out awaiting tools/call`. The matching `hoi4.gui_render` request at 1920×1080, UI scale 1, with normal/disabled/active/long-text/missing-localisation states also timed out after 180 seconds and returned no artifact. A prior 2026-09-25 attempt in the named decision audit inspected zero category elements and produced a 661-byte SVG with no render data and failed validation. Therefore text wrapping, clipping, cost-row fit, exact simultaneous visibility, background rendering, and click-region behavior remain unverified. No visual defect is waived as a renderer difference.

### P3: support cost and received equipment amounts are not explained as the same quantity

`event021_support_government` and `event021_support_opposition` each debit 150 infantry equipment, while their target-side helpers transfer 100. The remaining 50 is consumed at the sponsor and has no distinct player-facing explanation in the assigned action text or cost tooltip. The displayed 150 matches the sponsor debit, so this is not a debit/display mismatch or a free-equipment loop, but the output amount and the cost's use are unclear.

Recommended follow-up: explain the 50-unit logistics/administrative difference in the action tooltip if intentional, or align transfer and payment if it is not. Do not change the amount as a balance target in this audit.

### P3: neighbor-support descriptions do not name their current target

`event021_support_government_desc` and `event021_support_opposition_desc` say “the nearby civil war” and identify the side, but do not name the live government/claimant. `event021_monitor_border_desc` likewise does not identify the relevant country or route. The target predicates are substantially safer than the text: they require a live scope, valid side/host/actor relationships, non-capitulation, controlled states, and factories or a country leader. Add names only through the validated current target scope and preserve the existing neutral fallback.

## Decision category lifecycle and cognitive load

There is one ordinary category, `event021_civil_war_crisis_category`, with `visible_when_empty = no`, one icon, one static picture, and a category visibility OR over crisis, exposure, settlement, and prevention predicates. The category has no `scripted_gui`, meter, custom control, or animated element. The one static picture is therefore eligible under the simple-category picture rule.

The category description key `event021_civil_war_crisis_category_desc` exposes one numeric State Authority value via `event021_GetAuthorityValue`, its band via `event021_GetAuthorityBand`, a threshold/response sentence via `event021_GetAuthorityGuidance`, and a current focus via `event021_GetCrisisTargetName`. Constants define a 0–100 range and bands at 69, 39, and 14. Each band names its next threshold or collapse state and a broad response. The category does not expose a raw pressure dump. Semantically the value has meaning and player response, but its visual wrap and relationship to the picture are unverified because both current ordinary-window MCP calls timed out.

There are 18 decisions in total, phase and role filtered. The source-level exposure maximum is five before a shared one-use flag is set. The prior seven-action finding is superseded by the explicit exposure/prevention exclusion in `event021_country_can_prevent_fracture`; the exact rendered simultaneous availability remains unproven. There are exactly three mission definitions and no explicit category-level active-mission cap. The 2026-09-25 source handoff records two missions overlapping during settlement-to-reconstruction transition. Whether the capital mission can persist into that boundary depends on parent lifecycle cleanup outside this bounded surface, so do not report an exact active count as visually/runtime verified.

The category text is concise in value structure, not a telemetry table. Decision descriptions are generally concrete, while dynamic country/state identity is missing from several neighbor actions. The settlement-terms mission dynamically names one of five obligation types through `event021_GetSettlementObligationName`, but its requirement key `event021_settlement_terms_requirement_tt` only says the obligation must remain active through its period. Its underlying success helper branches on recognition, disarmament, rail security, sponsor repayment, or coalition governance. The action-to-obligation relationship is not visible in that requirement sentence.

## Cost and requirement clarity

All 18 decisions use centralized gate and spend constants, custom-cost rows, matching affordability clauses in `available` and `custom_cost_trigger`, and one manual debit path. Every gate amount checked equals its negative spend amount. No fifth cost is hidden in an effect or tooltip. The four-type settlement action is the maximum. The affordability clauses are duplicated inline rather than called through one named shared predicate, so the present values match but future edits can drift.

| Decision ID | Cost text key | Distinct spendable types and displayed values |
| --- | --- | --- |
| `event021_secure_arsenals` | `event021_secure_arsenals_cost_text` | 3: command power 10, infantry equipment 100, trains 1 |
| `event021_defend_capital` | `event021_defend_capital_cost_text` | 3: command power 15, infantry equipment 150, manpower 1,000 |
| `event021_review_loyalty` | `event021_review_loyalty_cost_text` | 3: command power 10, army XP 10, political power 25 |
| `event021_seize_depot` | `event021_seize_depot_cost_text` | 3: command power 10, infantry equipment 100, motorized equipment 10 |
| `event021_open_relief_corridor` | `event021_open_relief_corridor_cost_text` | 3: political power 15, motorized equipment 10, convoys 5 |
| `event021_offer_emergency_settlement` | `event021_offer_emergency_settlement_cost_text` | 4: political power 25, command power 15, infantry equipment 150, manpower 1,000. Inline limit violation. |
| `event021_reconstruct_administration` | `event021_reconstruct_administration_cost_text` | 3: political power 20, trains 1, manpower 500 |
| `event021_integrate_formations` | `event021_integrate_formations_cost_text` | 3: army XP 10, infantry equipment 150, manpower 1,000 |
| `event021_set_priority_front` | `event021_set_priority_front_cost_text` | 1: command power 10 |
| `event021_monitor_border` | `event021_monitor_border_cost_text` | 3: command power 10, motorized equipment 10, convoys 5 |
| `event021_support_government` | `event021_support_government_cost_text` | 3: political power 20, infantry equipment 150, convoys 5 |
| `event021_support_opposition` | `event021_support_opposition_cost_text` | 3: political power 20, infantry equipment 150, convoys 5 |
| `event021_offer_mediation` | `event021_offer_mediation_cost_text` | 3: political power 20, command power 10, convoys 5 |
| `event021_end_sponsor_commitment` | `event021_end_sponsor_commitment_cost_text` | 2: political power 15, command power 10 |
| `event021_complete_disarmament` | `event021_complete_disarmament_cost_text` | 3: army XP 10, infantry equipment 100, manpower 500 |
| `event021_complete_coalition_governance` | `event021_complete_coalition_governance_cost_text` | 2: political power 20, command power 10. Reuses mediation cost constants. |
| `event021_protect_communications` | `event021_protect_communications_cost_text` | 2: command power 10, trains 1 |
| `event021_review_regional_administration` | `event021_review_regional_administration_cost_text` | 2: political power 15, manpower 500 |

Each listed key has matching `_blocked` and `_tooltip` entries. The in-game texticon names are verified against installed vanilla or the registered Chaos Redux texticon: `£command_power`, `£pol_power`, `£army_experience`, `£infantry_equipment_text_icon`, `£GFX_train_texticon`, `£GFX_motorized_equipment_text_icon`, `£manpower_texticon`, and `£convoy_texticon`. No inline row spells out a resource name. The gate and payment amounts are centralized in `event021_action_cost`. AI PP hints are file constants mirroring the fixed political-power costs, as required by `ai_hint_pp_cost`.

The one-shot action flags and 30/45-day re-enable constants prevent routine repeat use inside a crisis. Most effects move State Authority, pressure, a route receipt, a timed idea, or a map/logistics state. Those output values are in `event021_action_tuning` and related constants. They are source-centralized; this audit does not certify their numerical balance. Mission timers are likewise centralized at 150, 30, and 180 days, but are fixed values rather than condition-scaled durations. Whether the accepted dynamicity contract requires state-dependent duration scaling remains unresolved.

## Mission quality

| Mission ID | Owner and category | Region/target | Requirement and duration | Success | Failure | Cancellation and duplicate risk |
| --- | --- | --- | --- | --- | --- | --- |
| `event021_hold_the_capital_mission` | Current crisis country; `event021_civil_war_crisis_category` | Current capital state | Opening or fronts phase; capital controlled, infrastructure and supply node present, and capital-defense-active or capital-held receipt. 150 days. | Resolver currently checks control/infrastructure/supply at expiry, then adds 5 Authority and 8 government leverage. It omits the defense/held receipt from its final check. | Adds -8 Authority and +8 pressure, marks failed, and adds 8 claimant leverage. | Cancels when crisis-management ends or settlement resolves. Success/failure flags prevent reactivation. No duplicate award loop found. |
| `event021_secure_rail_spine_mission` | Reconstruction country; same category | `random_civil_war_rail_mission_state`, constrained to opening-core territory | State owned/controlled, still in opening-core array, and has supply node or infrastructure above gate 2. 30 days. Activation does not require the target variable. | If current state checks pass at expiry, may add one infrastructure level, one train, 5 Authority, and pressure relief, then marks rail secured. | Adds -8 Authority and +8 pressure, marks rail lost, and clears active marker. | Cancels if reconstruction ends or a repair receipt appears. Failure does not block activation, so the mission can repeat every 30 days. Existing country/state receipts prevent repeated success infrastructure. |
| `event021_hold_settlement_terms_mission` | Settlement-obligation owner; same category | Current settlement obligation, dynamically named by `event021_GetSettlementObligationName` | Obligation active, hold-until variable exists, objective not already met/failed. 180 days. | Validates the obligation-specific receipt and no committed recurrence, records fulfilment, and runs parent review. | Marks the obligation failed; parent review records breach and clears the active obligation. | Cancels when settlement management or the active obligation ends. Parent review prevents repeat fulfilment. Requirement tooltip names only the active period, while the mission description names the obligation type. |

All three use `selectable_mission = yes`, an active marker in `complete_effect`, explicit cancel cleanup, and distinct timeout success/failure resolution. The source uses the timeout boundary to resolve the objectives. No live native decision-list render established how selection, timer, and the `available` predicate appear to the player.

## AI validity and route-lock notes

Every decision and mission has an `ai_will_do` block. Base action and mission scores, major priority, and discouragement factors are centralized in `event021_ai`; conditional role/phase modifiers use current crisis, exposure, settlement, or reconstruction flags. This is a score/willingness source review only.

Government and opposition support use live target-valid/viable triggers. Those checks reject missing/dead scopes, wrong sides, capitulated or nonviable receivers, and absent host/opposition actor pointers. The depot action requires an owned/controlled priority-front state in the opening-core array with a supply node or arms factory, and its AI weight is zero for invalid targets. The priority-front action itself lacks an equivalent anchor-pointer validity check. The rail mission AI weight is phase/role-based, while its activation can lack a rail-state target.

The category actions do not automatically enroll a country in an Event 006 league. The in-scope Event 006 reference is a role/phase score modifier for Event 006-front missions. The separate 2026-09-25 Event 006 adapter handoff reports source-level reuse of the existing complete-package loader, but its engine-level package/rollback and weighted-scenario validation remains unresolved. This bounded decision audit does not certify the wider package adapter.

The current decision file SHA-256 is `8937CAC0802745EAD68D6F1EC1B2BFA97DCCAA451EFFCC925D45A715DEDD3123`. A new read-only run was delegated to `chaosx_ai_probability_auditor` agent `01a0dc84-e37e-71c1-9ba6-4b06c80ae26b` for the 18 action and three mission weights. It was still running when this handoff was written and returned no new scenario results or artifacts. The prior 2026-09-25 probability evaluation had empty state/scopes and unresolved eligibility; it is historical partial score evidence, not current-source balance evidence. Do not call the weights balanced or probability-certified.

## Localisation and tooltip gaps

The category display keys are `event021_civil_war_crisis_category_desc`, `event021_GetAuthorityValue`, `event021_GetAuthorityBand`, `event021_GetAuthorityGuidance`, and `event021_GetCrisisTargetName`. The three mission requirement keys are `event021_hold_capital_requirement_tt`, `event021_secure_rail_requirement_tt`, and `event021_settlement_terms_requirement_tt`.

`event021_hold_capital_requirement_tt` says the capital must “keep its defenses in place,” while the trigger names either `event021_capital_defense_active` or `event021_capital_held`. The general phrase does not distinguish the action/receipt that satisfies that gate. The support descriptions lack dynamic names for the government/claimant. Cost tooltip prose repeats cost labels, but every cost amount is present in its dedicated row.

The 2026-09-26 localisation handoff reports no missing or duplicate keys in its assigned files and records context-specific target fallbacks. Those findings cover key wiring, not current production wrapping or scripted-scope interpolation. No localisation or texticon source was changed.

## Cleanup and exploit risk

`event021_cleanup_decision_state` clears one-shot action markers, mission active/success/failure markers, the mirrored priority state variables, rail receipts, sponsor-repayment receipts, settlement variables, and event-owned action state. The parent terminal cleanup separately calls `event021_clear_priority_front`, which clears `random_civil_war_priority_front_state` as a global target. Sponsor/recipient pointers are paired and checked against IDs before disengagement. The prior parent audit marked these cleanup repairs implemented at source level, with runtime ordering still untested.

The bounded failure exploit is the repeatable rail mission timeout. Decision action cooldowns and one-use flags otherwise prevent a routine same-crisis payment loop. No free-unit or repeated equipment-award loop was found in these action effects. Government/opposition support does debit 150 infantry equipment and transfers 100 to the receiver, so the remaining 50-unit consumption needs an explanation but is not a free award.

## Picture and asset eligibility

Category metadata is `common/decisions/categories/021_random_civil_war_categories.txt`; it points to static sprite `GFX_decision_category_picture_021_civil_war` and icon `GFX_decision_category_021_civil_war_crisis`. `interface/021_random_civil_war.gfx` maps the picture to `gfx/interface/decisions/021_random_civil_war/decision_category_picture_021_civil_war.dds`. The DDS exists and is referenced by a static `spriteType`, with no animation frames. The processed PNG preview shows a war-damaged rail town and fits the civil-war/preparedness category theme. The canonical 13-image vanilla picture contact sheet was inspected; its reference images are 114×101. The DDS itself was not decoded by the local image viewer, and the production render timed out, so in-game image appearance remains unverified.

There is no `scripted_gui`, meter, custom control, or other animation in the category metadata. The category is eligible for one static picture under the simple-category picture rule. The picture contains no fake button, value, or control.

## Meaningful validation and MCP results

- Source gate review covered all 18 decision visibility/availability/cost/payment/AI blocks, all three mission activation/availability/cancellation/timeout blocks, the directly invoked mission resolvers, action constants, State Authority guidance, target predicates, priority-target cleanup, and settlement obligation review.
- Cost audit paired every resource gate with its payment debit and the `_cost_text`, `_blocked`, and `_tooltip` keys. The installed vanilla texticon definitions confirm each displayed icon; no literal resource-name fallback or hidden fifth cost was found.
- `hoi4.gui_inspect`: first schema probe rejected the supplied game-state fixture (`actor` unrecognized, `scenario.state` must be a visual-state enum, `scenario.flags` must be a record). Corrected call for `countrydecisionview` with `state = normal` and empty flags timed out after 180 seconds. No artifact was returned.
- `hoi4.gui_render`: corrected call for `countrydecisionview`, the same scenario, 1920×1080 at UI scale 1, and normal/disabled/active/long-text/missing-localisation states timed out after 180 seconds. No artifact was returned.
- Historical GUI artifacts from `decision_mission_audit_2026-09-25.md` are nonusable: inspection modeled zero category elements and failed validation (`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b14c3ca2666ec8d95c72b508d3e2c96d42c3d692e084974073acd3ad81dd5225/9298e5f6a34f21afe50c242ee7794c1d54804b6d5efd92414e765c11e50f7417/gui-inspect.a6cd265ac259ee8d.json`); the matching SVG was 661 bytes with no render data and failed validation (`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5ef75a6a7ef175373b04e952f07db1c5485b233c549b09cce1f12071075d1eb7/4203e314c8ec357b66793b75ef01ce56c19a09bbdfee2338f82ebe15d46fcf97/event021_civil_war_crisis_category-full.svg`). These historical artifacts do not validate the current source.
- The separate probability auditor had no result by handoff time. Its pending status and the prior incomplete empty-scope probability artifacts leave all numeric AI willingness comparisons unresolved.
- No game executable, test harness, source parser, workbook, event chain, or unrelated Event 021 package surface was run or changed. Live gameplay and ordinary decision-screen acceptance remain outside this audit.

## Recommended parent follow-up

1. Resolve the two mission semantics findings and the rail retry loop in `common/decisions/021_random_civil_war_decisions.txt` and `common/scripted_effects/021_random_civil_war_decision_effects.txt`, with any changed duration/threshold centralized in `common/script_constants/021_random_civil_war_constants.txt` and matching mission text in `localisation/english/021_random_civil_war_l_english.yml`.
2. Repair the priority-front target gate at `event021_set_priority_front` and its decision `event021_set_priority_front` so selection, affordability, and payment agree on a live anchor.
3. Resolve the four-value settlement inline row without removing any of its four gameplay costs.
4. Explain the support-action cost/transfer difference and name the current support targets in player-facing descriptions if those scopes remain valid at display time.
5. Obtain usable ordinary-category rendering and explicit source scenarios for simultaneous visible/available actions and missions. The current MCP timeout is the exact blocker; source review is not a visual substitute.
6. Receive and review the still-running `chaosx_ai_probability_auditor` handoff before any numerical AI conclusion. Preserve its exact scenarios, MCP artifacts, and unresolved inputs.

No source fallback, gameplay simplification, balance target, or design change was applied. No commit was made because this is an audit handoff only.
