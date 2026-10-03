# Event 032 operation preparation and launch decision audit

Date: 2026-10-03.

Disposition: read-only audit handoff. No gameplay source was changed. The only file created by this audit is this handoff.

Scope: the human target selector, the precision, strategic, saturation, and counterforce preparation decisions, their four timed missions, the prepared-operation launch decision, and the source helpers those actions call. This is not a full Event 032 balance or campaign audit.

The current source preserves the parent’s evolution-gate work. The current operation-effects file SHA-256 is 1FDAF60021D4824C0C4FB8F3170E9F92366DC2EF8B6AE3F4771F2AFDEBE42187, matching the parent-provided current hash. The parent reports that this final file contains 45 flag renames and new helpers; this audit did not change them. The mission file remains byte-identical to the immutable evolution-gates snapshot at A9D8A1F4C83D3B5450CDA48540B8B69C38177C79AE0ADACDFA61815CCD07F158. The current decision file differs from its before snapshot only at the saturation and special-warhead guard call sites in the read-only diff; no AI-weight hunk was changed there. The current operation-trigger file contains the parent’s added operation-track and payload-custody guards. No EVO edit was reverted or modified.

## Source verdict

The four preparation decisions use the real vanilla keyword state_target = any_owned_state. The installed decision guide calls its state-selection field state_trigger in common/decisions/_documentation.md:38-45, but installed vanilla source uses state_target in AFG.txt:1069-1080 and BRA.txt:619-627, and the offline Decision modding page uses state_target at lines 576-586. Do not normalize the Event 032 keyword to state_trigger. The native targeted-decision rule is clear: FROM is the target scope, and for a state-targeted decision that scope is the exact State, not its owner or controller country.

The Event 032 target predicate missiles_target_is_valid is a country predicate. Its body at common/scripted_triggers/032_missiles_triggers.txt:254-262 uses country war, subject, and controlled-state checks. The four state-targeted decisions pass their state-valued FROM to that predicate at common/decisions/032_missiles_decisions.txt:409, 416, 449, 453, 486, 490, 523, and 527. The four complete_effect blocks do not consume the decision’s FROM state. Their shared preflight instead chooses a target state from the stored enemy country and a launch site from the owner’s site pool at common/scripted_effects/032_missiles_operations_effects.txt:2216-2246. This is a scope mismatch plus unused state targeting. If the predicate happened to match through an engine coercion, it would still create duplicate state entries for the same action. The exact runtime row result remains unobserved.

An accepted ordinary preflight creates the active operation receipt before its matching mission is activated. missiles_country_can_prepare_operation includes NOT = { missiles_operation_active = yes } at common/scripted_triggers/032_missiles_triggers.txt:282-286, while every preparation mission cancels on NOT missiles_country_can_prepare_operation at common/decisions/032_missiles_missions.txt:167-172, 199-204, 225-230, and 251-256. Therefore, after a successful preflight, the mission’s own cancellation predicate becomes true because the operation is active. Its cancel_effect calls abort and cleanup.

If preflight rejects before creating an active receipt, the decision still activates its mission. The mission then has no ready transition and can remain until cancellation or timeout. In either branch, the ordinary path cannot proceed through its intended timed preparation.

The sole setter of missiles_operation_ready is missiles_complete_preparation at common/scripted_effects/032_missiles_operations_effects.txt:2296-2300. A scoped search found it called only by event chaosx.nr32.83 at events/032_missile_crisis.txt:403-416. That event is queued only from the rogue and retaliation paths at common/scripted_effects/032_missiles_operations_effects.txt:1192 and 4410, and it commits the operation immediately after the setter. None of the four ordinary preparation decisions queues that event or calls the setter. The ordinary preparation missions therefore never reach their available flag through their own path.

The native mission semantics support an automatic preparation completion once the readiness condition becomes true. The offline Decision modding page says that available completes a mission automatically unless selectable_mission = yes is set, and says activate_mission bypasses activation. Event 032 does not set selectable_mission, which matches a no-second-click preparation objective. The current mission complete_effect blocks only show a tooltip, while the ready setter remains outside the ordinary mission path.

The user’s proposed coalesced hidden receiver is recorded below as an unresolved implementation option, not as an accepted fallback. No receiver or other source was added by this audit.

## Issues sorted by severity

| Severity | Surface and identifiers | Evidence and finding |
| --- | --- | --- |
| P1 | Ordinary preparation lifecycle: missiles_prepare_precision_strike, missiles_prepare_strategic_barrage, missiles_prepare_saturation_barrage, missiles_prepare_counterforce_strike, and their matching missions | Successful preflight sets an active receipt, which makes the current cancel predicate true. Rejected preflight still activates a mission. Neither branch has a working ordinary readiness transition. |
| P1 | Four state-targeted preparation decisions | state_target selects actor-owned States and passes each as FROM. The decision checks the country-only missiles_target_is_valid predicate and ignores FROM in its effect. This can suppress all rows or multiply identical rows; source inspection cannot prove which visible result the engine produces. |
| P1 | Four preparation cost transactions | Each decision subtracts command power, fuel, and support equipment before calling its preparation helper and does not test missiles_operation_preflight_result before charging or activating the mission. A rejected preflight can charge the player and apply the decision cooldown without creating a valid operation. |
| P2 | Four preparation mission timers | Native timeouts are 14, 21, 30, and 18 days, while the scripted dynamic deadlines can extend to 29, 37, 45, and 39 days respectively. The static timeout can therefore abort an operation before its computed due date. |
| P2 | missiles_launch_prepared_operation | Its available trigger checks for any controlled launchable site, while missiles_operation_can_be_committed checks the exact receipt, track gates, selected target and state, assigned site, payload custody, reserve receipt and amount, ready state, incident state, and cooldown. The launch button can appear available for an unrelated site while the assigned operation is no longer committable. |
| P2 | missiles_prepare_counterforce_strike | The effect sets operation type counterforce but strike profile strategic at common/scripted_effects/032_missiles_operations_effects.txt:2290-2294. The profile selector maps strategic to broad_strategic at lines 1717-1724. That profile accepts ordinary factories, rail, supply, rocket sites, and capitals, so the operation does not require a proven missile or CBRN facility as specified. |
| P2 | Target-state ranking for all four profiles | missiles_select_best_operation_target_state stores the best-scoring state in missiles_operation_target_state at common/scripted_effects/032_missiles_operations_effects.txt:1812-1818. missiles_select_operation_target_state then overwrites it by randomly selecting any profile-valid state at lines 1847-1863. The final target can ignore the best-state score and the expected ordering in the Event 032 matrix. |
| P2 | Human target selection and category lifecycle | The only Event 032 decision category is missiles_program_management_category. missiles_select_target_country is inside it and targets every valid entry in global.enabled_countries_list. The part 5 spec calls for a separate target-management category and a clear-target action; neither exists in the scoped category/source. A target list can therefore exceed six visible choices in the same category, and the selected target has no player-facing clear action in this decision file. |
| P2 | Cost and category status display | Each preparation displays three cost values, but the preflight also reserves a dynamic operational-reserve amount. The row and its cost tooltip omit that amount. The live category description displays nine status/value fields at once, more than the four-value hard ceiling in the decision/GUI interaction budget, and gives only a generic sentence about reserve, target, site, and command requirements. |
| P2 | Counterforce selector and target eligibility | The human country selector’s target_trigger uses missiles_target_is_valid, but its effect missiles_select_target requires missiles_ordinary_target_is_valid. A faction partner that passes the first predicate can receive a visible selector row whose effect does nothing. The target-country and final-operation checks also use the less restrictive predicate after a target has already been selected. |
| Blocked | Decision and mission score analysis | The required probability auditor attempted decision_ai_will_do inspection for the five preparation/launch decisions twice with the named workspace and timed out both times after 600 seconds. No score scenarios, evaluation, sweep, rendering, or comparison result was returned. Source weights below are not balance evidence. |

## Minimal patch plan for the parent

No gameplay patch was applied. These are exact source hunks for the parent to review and implement.

1. In common/decisions/032_missiles_decisions.txt:400-549, retain the four decision IDs, current cost amounts, cooldowns, and parent-authored saturation/special-warhead gates. Remove the four unused any-owned-state targets and their FROM country-predicate checks if the operation helper continues to choose the target state and launch site automatically. Keep the four actions as one root-country action each. If a state target is retained by design, make the chosen state the actual preflight input and validate it with state-scope predicates.

2. In the same four complete_effect blocks, run and check the operation preflight before debiting the three ordinary costs or activating a mission. Debit and activate only when the preflight receipt is accepted. Preserve the existing amounts and make rejection leave no fee debit, mission, cooldown side effect where the engine permits, or active receipt.

3. In common/decisions/032_missiles_missions.txt:160-268, replace the cancellation use of missiles_country_can_prepare_operation with lifecycle checks appropriate to an already-active operation: program management remains valid, the current operation receipt remains active, the selected enemy and exact target state remain valid, the assigned launch site remains valid, and missiles_operation_tracks_are_enabled remains true. Mirror the active-receipt check in cancellation cleanup as required by the setup-receipt lifecycle rule.

4. Keep the four timed missions. Their successful transition should occur only after the current operation receipt is active, its current ready date is due, the shared track guards pass, and the selected target, target state, assigned site, reserve receipt, and payload custody still satisfy their operation checks. A native available trigger can auto-complete a nonselectable mission when the ready condition becomes true, then call missiles_complete_preparation from the mission’s complete_effect. The separate launch decision remains the player/AI commit action.

5. Do not invent an activate_mission duration object. Installed effects_documentation.md:661-669 documents only activate_mission = <mission>. Installed documentation lists add_days_mission_timeout with an integer example at lines 1051-1063. Offline Effects modding documents int or variable days at lines 1917-1925, while a vanilla source precedent proves a signed literal adjustment at common/national_focus/argentina.txt:486-489. No vanilla dynamic-variable activation override was found. Because the native timers can be shorter than the dynamic due dates, the parent must verify the exact timer-update syntax before relying on it.

6. If dynamic mission timeout adjustment is not verified, the parent’s proposed bounded hidden receiver remains an unresolved option pending acceptance and syntax validation. It should coalesce one pending wakeup per country, wake only the country root, and recheck the current active receipt, current due date, track gates, target, target state, and assigned site before calling the readiness setter. A stale wakeup should do nothing and coalesce/reschedule one current wakeup only when the receipt remains active. The receiver must not debit costs, create incidents, or commit an ordinary launch. Event chaosx.nr32.83 cannot be reused unchanged because it commits immediately.

7. In common/decisions/032_missiles_decisions.txt:583-604, make launch availability use the existing missiles_operation_can_be_committed predicate so the player and AI see the same exact commit gate that missiles_commit_operation enforces. Preserve the current shared evolution and custody guards.

8. In common/scripted_effects/032_missiles_operations_effects.txt:1706-1734 and 2290-2294, route the counterforce operation to the counterforce target profile and require the specified enemy launch or CBRN facility and intelligence evidence before payment. In lines 1847-1863, preserve the best-scoring target state rather than overwriting it with a random profile-valid state.

9. Keep the category ordinary and avoid a new GUI. Align target selection with the accepted part 5 target-management flow, add its clear-target step if that design remains accepted, and reduce the category description to four or fewer simultaneous mechanic values with concise threshold, consequence, and response explanations.

## Category lifecycle and cognitive-load notes

The sole registered category is missiles_program_management_category at common/decisions/categories/032_missiles_categories.txt:5-13. It is visible when missiles_country_can_manage_program passes and remains visible when empty. Decision entries phase themselves through missiles_program_phase_* flags and management/operation triggers.

With a human target selected, the operation phase has five unique actions at most: four preparation choices and optional special-payload integration. Each preparation definition is state-targeted over any_owned_state, so the potential row count is four times the number of matching owned states until the scope mismatch is resolved. With no target selected, one selector decision is generated for every valid country in global.enabled_countries_list inside the same category; this is the phase most likely to exceed six visible choices. In the prepared phase the intended primary actions are launch and abort.

The source has one active-operation flag and the preparation-root predicate prevents starting another while it is active, so the intended active-mission count is one. The current cancel predicate immediately collapses that lifecycle.

The live category description at localisation/english/032_missiles_decisions_l_english.yml:4 simultaneously displays Operational Reserve, Launch Readiness, Command Control, Technology, Sites, Guidance, Target, Retaliation, and Crisis. The first three numeric values are named and iconed, but their thresholds and immediate consequences are not stated there. Technology, site count, guidance, target, retaliation, and crisis are concise statuses without an adjacent cause/response explanation. This is a dense nine-value header against the four-value surface ceiling; no custom GUI or world scan is recommended by this audit.

## Mission quality audit

| Mission | Owner, category, and region | Requirement and duration | Success and failure | Duplicate risk |
| --- | --- | --- | --- | --- |
| missiles_precision_strike_preparation_mission | Issuing country; missiles_program_management_category; selected enemy target country and the automatically selected target state/site | available is only missiles_operation_ready; static timeout 14 days; dynamic preparation is 10-29 days | Success is tooltip-only; cancel and timeout abort/cleanup and refund the reserved operational reserve | One unique mission, but its current cancel gate is self-triggered after successful preflight |
| missiles_strategic_barrage_preparation_mission | Issuing country; same category; selected enemy target country and selected state/site | available is only missiles_operation_ready; static timeout 21 days; dynamic preparation is 13-37 days | Success is tooltip-only; cancel and timeout abort/cleanup | One unique mission; static timer can expire before the dynamic deadline |
| missiles_saturation_barrage_preparation_mission | Issuing country; same category; selected enemy target country and selected state/site | available is only missiles_operation_ready; static timeout 30 days; dynamic preparation is 23-45 days | Success is tooltip-only; cancel and timeout abort/cleanup | One unique mission and saturation-gated; static timer can expire before the dynamic deadline |
| missiles_counterforce_strike_preparation_mission | Issuing country; same category; selected enemy target country and selected state/site | available is only missiles_operation_ready; static timeout 18 days; dynamic preparation is 15-39 days | Success is tooltip-only; cancel and timeout abort/cleanup | One unique mission; static timer can expire before the dynamic deadline and current target profile is broad strategic |

The four missions do not run concurrently by design. Their timeout and cancellation text is shared and generic, so it does not tell the player whether the target, site, command, reserve, payload, route, or deadline invalidated the operation.

## Cost, requirement, AI, and localization audit

Each preparation has four distinct spendable types at most: its dynamic operational-reserve reservation, command power, fuel, and support equipment. This stays within the four-type hard limit.

The displayed command power, fuel, and support-equipment costs use the matching texticons in localisation/english/032_missiles_decisions_l_english.yml:224-235. The custom operational-reserve icon exists as GFX_032_missiles_operational_reserve_texticon in interface/032_missiles.gfx:18, and the current reserve total uses it in the category description. No preparation cost row or corresponding cost tooltip shows the dynamic amount reserved by missiles_operation_missile_cost. The operation amount is therefore a hidden fourth spendable cost even though its icon is registered. No literal resource-name fallback appears in the three displayed cost rows.

The three displayed costs are manually debited before preflight acceptance is known. On an abort, missiles_abort_operation refunds the active reserve receipt at common/scripted_effects/032_missiles_operations_effects.txt:4509-4517; it does not restore the command power, fuel, or support equipment debited by the ordinary decision. The actual affordability trigger covers those three costs, while reserve affordability is checked later in preflight.

The five in-scope decision weights are missiles_prepare_precision_strike, missiles_prepare_strategic_barrage, missiles_prepare_saturation_barrage, missiles_prepare_counterforce_strike, and missiles_launch_prepared_operation. Their source AI modifiers are war/capability gates, but no probability result was produced. The four mission weights are similarly only source scores. Do not interpret any of them as click probabilities or as a balance verdict.

The human selector’s target_trigger uses missiles_target_is_valid, whereas missiles_select_target in the completion effect uses missiles_ordinary_target_is_valid. The AI’s fallback selector uses the ordinary predicate. The preflight and commit validation of an already-selected target still use the base predicate, so target validity can diverge after selection. Preserve the current missiles_operation_tracks_are_enabled calls and other parent-owned EVO guards when correcting mission completion.

Preparation descriptions are short. The counterforce decision description and mission text promise a proven facility, but the current broad-strategic profile does not require one. The precision mission description names its selected site, target state, reserve, and command chain; the other three mission descriptions give less specific requirements. The shared timeout/cancel text does not state which preflight or lifecycle condition failed.

## Cleanup, exploit, and validation notes

The current abort helper refunds only an active uncommitted reserve receipt, and cleanup clears the reserved site array and operation state. The cost-loss path is failed preparation after a decision fee has already been debited. The cooldowns and resource requirements do not form a free launch, unit, equipment, or repeated-success loop in the inspected path.

No source patch, game launch, desktop control, world scan, or GUI inspection/render was performed. The user scoped this task to no GUI and no game launch.

MCP evidence is incomplete under load. The decision reference_context request timed out after 600 seconds. The decision_inspect request for missiles_prepare_precision_strike returned input validation because scenarios were required and omitted. Two bounded source_lookup requests, for activate_mission and missiles_prepare_precision_strike, each timed out after 600 seconds. The live source_lookup schema is symbol/line based and has no view or keyPath fields. No script_validate route was exposed.

The required chaosx_ai_probability_auditor called probability_inspect twice for decision_ai_will_do using workspace mod_chaos_redux_ea3b2d67c2c0 and the five decision IDs. Both calls timed out after 600 seconds. No evaluate, sweep, simulation, render, or compare artifact was returned. AI probability and scenario ranking remain unresolved; the source review is not a substitute.

The probability compare step is inapplicable to this audit because no AI weight was changed. A later owner weight patch requires the same named scenarios and a before/after compare against the immutable snapshots.

## Evidence index

Current and immutable source hashes:

| File | Current SHA-256 | Immutable before SHA-256 |
| --- | --- | --- |
| common/decisions/032_missiles_decisions.txt | 2DAC7EC6050754848B64F0737F1CB4E51D557BBE59F60F0253FD199AA3224DB2 | FAF772392B482EE0309EF317259FF6DD2520D3EFA8A08F7415275841ACA2E99F |
| common/decisions/032_missiles_missions.txt | A9D8A1F4C83D3B5450CDA48540B8B69C38177C79AE0ADACDFA61815CCD07F158 | A9D8A1F4C83D3B5450CDA48540B8B69C38177C79AE0ADACDFA61815CCD07F158 |
| common/scripted_triggers/032_missiles_operations_triggers.txt | 3D08B39F0B6F45F59C5DD666AB30B7C9604C84E240B39D0B9814EE2E4F1D0E4B | F39334F373E66876333999C1460C67BF29CB5D630C255F4D080512111A0F6098 |
| common/scripted_effects/032_missiles_operations_effects.txt | 1FDAF60021D4824C0C4FB8F3170E9F92366DC2EF8B6AE3F4771F2AFDEBE42187 | A6B34365268CECB810ED035249D50A944E2FC7013608576CFA3413BA7D2B27AF |

Reference revisions:

| Source | Lines used | SHA-256 |
| --- | --- | --- |
| Installed common/decisions/_documentation.md | 13-20 and 31-45 | 5E7E686B5582F32C38D898D805E17171E88F3BFEEE4A030DEB1884F9726DE019 |
| Installed documentation/effects_documentation.md | 661-669 and 1051-1063 | 2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF |
| Vanilla common/decisions/AFG.txt | 1069-1080 | DABC91C3F7FB1810D64D91D07147E827068D42540326CE10554A0752EE48D7A7 |
| Vanilla common/national_focus/argentina.txt | 486-489 | E7B06A02BFE938AE96C455FB13923C23A160178E74A1733CF92A7C1A38ED2A7E |
| Offline Decision modding wiki | 465-478 and 576-594 | 7713B9BCEE5F3818D63AAFBD45D18E812A9173A7C59AB238384B57DB60DB6162 |
| Offline Scopes wiki | 54-63, 256-268, and 388 | 18EF5249E4991F5427ECA9EC4A2F66DD47F51E26A491C730ADC622F1F5DB1B49 |
| Offline Effects wiki | 1908-1926 | 997DDB09BFD63EFB41A425149C46BD812D5F8953217A403386B2F6C85196AA0C |
| Offline Triggers wiki | 646-650, 963-966, and 1077-1081 | ABC51AD18A2C46E46D47BAA795C5A840EBAF7C4AE3E777426C64A9F4C0C0CE06 |

Specification references are docs/specs/032_missiles_specs/032_missiles_spec_part_5_decisions_missions_and_scenario.md:49-56, 95-127, 427-452, 454-592, and 787-820; docs/specs/032_missiles_specs/032_missiles_spec_part_6_ai_and_probability.md:252-285, 333-380, and 552-586; and docs/specs/032_missiles_specs/032_missiles_probability_scenario_matrix.md:20-52.

## Handoff summary

Files changed: this report only.

Decision, mission, and localization IDs changed: none.

Before/after behavior: no gameplay behavior changed. The current source is blocked on ordinary mission cancellation/readiness and scope errors. The recommended transaction keeps the four preparation missions, current cost amounts and evolution guards, and the separate launch action; it moves the ready transition to a due-date/receipt-validated path and prevents failed preflight from charging resources.

Meaningful validation run: source-scoped searches, read-only comparison to the immutable before snapshots, direct reads of the offline wiki and installed documentation, and vanilla state-target and mission-timeout precedents.

Skipped meaningful validation: decision_inspect did not receive its required scenario set; source_lookup/reference_context timed out after 600 seconds; the probability auditor timed out after 600 seconds twice. No runtime game validation was authorized. GUI work was explicitly out of scope.

Plan handoff path: none. The coalesced hidden receiver remains a proposal pending native timing-syntax verification and parent acceptance.

Skills applied: chaos-redux-decisions-missions, chaos-redux-events, and chaos-redux-subagents. The scripted-GUI skill was read during initial surface triage; the parent subsequently excluded GUI work, so no GUI implementation or render was attempted.
