# Event 007 Fury Decision and Mission Audit Handoff

Date: 2026-10-05.

Disposition: narrow decision, mission, route, and affordability fixes implemented; full engine and probability validation remains blocked.

Acceptance basis: the parent delegated the existing decision surface for small fixes and explicitly accepted the depot four-cost reserve release, focus/category links, one-neighbor actor threshold, legal rival targeting, preterminal reserve sharing, war-only paid depot use, removal of the redundant paid neighbor survey, and removal of the no-op paid recognition-denial decision whose only remaining effect was an unread pressure variable.

## Files changed in this subtask

- `common/decisions/007_fury_decisions.txt`.
- `common/decisions/categories/007_fury_categories.txt`.
- `common/scripted_triggers/007_fury_triggers.txt`.
- `docs/plans/007_fury_plans/decision_audit_2026-10-05.md`.

The shared effect/constant and localisation changes were made by the assigned helper and text owners; they are not attributed to this subtask. Their handoffs are `docs/plans/007_fury_plans/helper_audit_2026-10-05.md` and `docs/plans/007_fury_plans/localisation_audit_2026-10-05.md`.

## Changed identifiers and behavior

`fury_war_office_category` now requires both the Fury actor flag and `fury_war_office_unlocked`, matching the focus `fury_war_office_without_a_door`.

`fury_select_new_target` is visible only while the actor is at peace, has no current target, is below the existing overextension gate, is not at extreme occupation pressure, and has a legal ordinary neighbor. Availability rechecks that no current target exists before charging.

`fury_open_forward_depots` is visible only to an active Fury actor during war, after `fury_depot_cadres_unlocked`, and while a finite reserve remains. Availability gives separate reserve and owned-and-controlled deployment-state reasons. Its cost row uses resource-only affordability; availability and payment also require the actor, focus unlock, reserve, and deployment state. Completion clears a payment receipt, charges once, and spawns only after a successful receipt.

The depot trigger helpers are `fury_has_reinforcement_reserve`, `fury_has_depot_spawn_state`, `fury_can_use_reinforcement_depot`, `fury_can_pay_reinforcement_depot_resources`, and `fury_can_pay_reinforcement_depot_cost`. Its four ordinary spendable costs are 15 command power, 610 infantry equipment, 40 support equipment, and 6,300 manpower; Black Friday adjusts the command-power/rifle quote while the support/manpower deployment fees remain fixed.

Before, the paid depot action used the dynamic 1–8 full-column spawn formula for a 450-rifle quote without consuming the finite reserve or charging the actual support/manpower fill. After, it releases exactly one full column from the reserve, pays the four authored costs once, and does not grant extra stockpile/manpower through the paid spawn helper.

`fury_register_occupation_settlement` hides after `fury_occupation_registers_unlocked`, when the focused register action replaces it.

`fury_garrison_the_names_mission` cannot activate during `fury_occupation_crisis_active` and cancels if the crisis begins, leaving `fury_restore_the_registers_mission` to handle the overlapping defense objective. Crisis cancellation routes through failure, other cancellation clears the active marker, and the timeout success effect independently checks that no crisis is active.

`fury_form_war_table` and `fury_mark_rival_column` check both route flags in visibility and availability, so a selected route cannot be farmed again after its 45-day cooldown; both route choices also hide once `fury_world_end_active` begins. The War Table decision requires a valid living Fury partner who is neither on the rival route nor at war with the caller, repeats that candidate check before payment, and marks only those eligible partners as project pact members. It does not create a native faction. The same `fury_is_valid_war_table_partner` trigger is used by the focus response; no extra focus-completion gate blocks the early Evolution II decision route.

The redundant `fury_survey_beyond_the_border` decision was removed. It paid command power to repeat the ordinary neighbor scan and incremented the unused `fury_reach` variable. The text owner removed its visible strings and unreferenced wrappers; the six cost-adapter target keys required by shared 026 selectors remain for compatibility.

`fury_share_terminal_reserves` now uses `fury_can_share_reserves` and `fury_can_pay_terminal_reserve_share_cost` for both the preterminal pact route and the existing World End route. `fury_is_valid_reserve_share_target` requires an active, noncapitulated Fury recipient, excludes the donor and countries at war with it, requires the accepted pact/cooperation route before World End, rejects rival-route recipients, and preserves the terminal actor path. The effect owner locks one recipient, rechecks that same recipient before debit and transfer, and does not reroll after payment.

`fury_can_be_selected` now uses `constant:fury_actor_selection.minimum_valid_neighbors`, set to one by the parent. `fury_can_target_rival_actor` permits rivalry only when the actor has no legal ordinary neighbor or is an explicit `fury_triggerable_scenario_actor` under `fury_triggerable_scenario_hostile`. `fury_is_valid_rival_actor_target` now applies faction, war, and declaration checks to the acting country through `PREV`, rather than the outer launcher's `ROOT`.

`anti_fury_response_visible` rejects `fury_all_actors_defeated`, closing stale Anti-Fury actions after the last Fury actor is removed. Actor setup clears that flag when a new actor is created, so the category can reopen without a per-frame country scan.

The paid `anti_fury_recognition_denial` decision was removed because its effect only changed the unread `global.anti_fury_response_pressure` value. Its visible title, description, and action tooltips were removed from localisation. The six legacy shared Black Friday cost-adapter target strings and their ordinary affordability fallback trigger remain for compatibility; no active decision uses them. The effect owner removed the recognition payment/effect helpers, and all remaining writes to the unread pressure variable were removed while retained aid, defense, and denial consequences were preserved.

`can_pay_fury_march_core_cost` now checks command power, manpower, rifles, and stability. The parent-owned effect and constants remove the fifth support-equipment cost while retaining the stability payment and its affordability threshold.

## Severity-ordered findings

1. **Engine and probability evidence is unresolved.** `hoi4.reference_context` and my `hoi4.decision_inspect` call returned `MCP tool hoi4_agent_tools/hoi4.reference_context is not available to the model` and `MCP tool hoi4_agent_tools/hoi4.decision_inspect is not available to the model`. A later `reference_search` invocation failed because `tools.mcp__hoi4_agent_tools__hoi4_reference_search` was not callable. The cost-display auditor later got a partial decision inventory, but its focused sale-source scenario timed out; neither output supplies a rendered cost row or complete eligibility scenario. The probability auditor saved the task-start decision source at `docs/plans/007_fury_plans/source_baseline_2026-10-05/common/decisions/007_fury_decisions.txt` with SHA-256 `F1D1C7019E8AC1F0566FD5DA22946D47908CBBCD95EA7C16DF6323C058DEC40D`. The named scenario candidates included `FURY_DECISION_POST_CONQUEST_GATES`, `FURY_DECISION_PACT_ROUTE`, `FURY_DECISION_HOSTILE_ROUTE`, and `FURY_RIVAL_TARGET_SCOPE`, but their state records were empty because inspection never returned its accepted scenario schema. The corrected inspect calls and subsequent same-scenario comparisons timed out without returning evaluations, sweeps, comparison artifacts, source revisions, or scenario hashes. Later changes narrowed War Table partner eligibility and removed a no-op Anti-Fury choice, but no updated comparison returned. No AI score or balance conclusion is claimed.

2. **The remaining `fury_reach` counter has no source reader.** Repository search found it is initialized, incremented by focuses, and cleared but is not read by any trigger, effect, event, or decision. The decision-side writes to the unread `fury_pact_cohesion` and `fury_compliance_drive` counters were removed; their actual pact/compliance ideas and partner flags remain. The decision spec assigns reach and pact cohesion concrete gameplay roles, so giving reach a threshold and visible player response still requires a parent design pass.

3. **The source action-count cap depends on the route.** The focus-driven and event-driven Evolution II paths source-cap at six simultaneous primary buttons: peace target selection or wartime depot reinforcement, one register action, rail survey, one core route, and the two route-choice decisions. The two route actions and target/depot alternatives cannot appear together in the terminal phase: `fury_world_end_active` hides both route choices, while terminal reserve sharing and front assignment appear, preserving a six-button cap. Basic registration is replaced after the register focus, and admin/march coring use mutually exclusive focuses. Automatic mission status rows are excluded from the six-button cap as directed by the parent. The focused event-driven candidate scenario remains uninspected because the decision route did not return a validated state fixture.

4. **Anti-Fury missions still fall short of their mapped map actions.** Border Watch and Supply Denial share the same owner, category, failure trigger, cancel trigger, and capital-control condition; neither checks supplied border divisions or rail access. Emergency Aid transfers equipment to its target before a 60-day mission that checks only the sender's capital, not a convoy or rail route. The category can show up to three simultaneous Anti-Fury missions, at the allowed cap, but their map requirements remain a design gap.

5. **Reserve sharing can repeat.** Each use spends command power, manpower, rifles, and support equipment and has a 45-day cooldown, while success adds pact cohesion and relieves overextension for both sender and recipient. The parent-approved design has no per-pact use cap; numeric balance remains unresolved with the probability route.

## Category lifecycle and cognitive load

The War Office category opens from its focus flag and closes when Fury cleanup removes the actor flag. The Anti-Fury category closes after `fury_all_actors_defeated` and reopens when actor creation clears it. Both categories use `visible_when_empty = no`.

The decision rows do not present a raw dynamic-number dump or a custom GUI. Current descriptions explain the action, requirement, and cost, but the remaining `fury_reach` value has no visible threshold/consequence because source logic does not consume it.

For focus-driven normal play, route and war-state gates produce at most six primary decision buttons. Depot reinforcement and target preparation are separated by war state; basic registration is replaced after the register focus; admin and march core routes are mutually exclusive; and the Pact focus closes the two route-choice buttons before reserve sharing appears. World End adds reserve sharing and terminal-front assignment while retaining a six-button source-level cap. The crisis exposes one Fury defense mission at a time after the Garrison/Restore phase gate. Anti-Fury can expose four primary actions and at most three mission rows; the mission rows remain separate from the primary-action budget.

## Mission quality

| Mission | Owner and category | Region and requirement | Duration | Success and failure | Duplicate risk |
| --- | --- | --- | ---: | --- | --- |
| `fury_garrison_the_names_mission` | Fury actor; War Office | Hold the capital and every registered noncore state. Losing either triggers failure; actor loss or no remaining settlement cancels. | 70 days | Timeout reduces occupation pressure/overextension and improves compliance only outside an occupation crisis; crisis cancellation fails and other cancellation clears the active marker. | Suppressed and cancelled when the crisis-specific Restore mission activates. |
| `fury_restore_the_registers_mission` | Fury actor; War Office | Same capital and registered states during occupation crisis. | 45 days | Timeout lowers occupation pressure/overextension and clears recent integration failures; loss triggers failure. | Replaces Garrison during crisis. |
| `anti_fury_border_watch_mission` | Non-Fury country; Anti-Fury Response | Hold the capital and avoid war with a neighboring Fury. No supplied-division or rail objective is checked. | 90 days | Timeout improves defense; capital loss or neighbor war adds Fury momentum. | Same capital/war failure condition as Supply Denial. |
| `anti_fury_aid_route_mission` | Non-Fury aid sender; Anti-Fury Response | Hold the sender's capital while the stored, live, noncapitulated, non-player-linked target remains valid. No route-access objective is checked. | 60 days | Timeout resolves aid successfully; capital loss triggers failure; invalid target/system cancels and clears target/source variables. | Can overlap the two neighboring-country missions. |
| `anti_fury_supply_denial_mission` | Non-Fury country; Anti-Fury Response | Hold the capital and avoid war with a neighboring Fury. No rail/depot sabotage objective is checked. | 70 days | Timeout raises containment and Fury pressure; failure relieves Fury overextension. | Same capital/war failure condition as Border Watch. |

## Cost and requirement audit

All existing spendable actions are within the four-type hard limit. The March support cost was removed by the parent-owned effect and constants patch; stability remains the fourth cost.

| Decision ID | Spendable cost types | Count |
| --- | --- | ---: |
| `fury_select_new_target` | command power | 1 |
| `fury_open_forward_depots` | command power, infantry equipment, support equipment, manpower | 4 |
| `fury_register_occupation_settlement` | command power, infantry equipment, support equipment | 3 |
| `fury_count_captured_registers` | command power, infantry equipment, support equipment | 3 |
| `fury_rail_registry_survey` | command power, trains, support equipment | 3 |
| `fury_core_state_by_administration` | command power, manpower, infantry equipment, support equipment | 4 |
| `fury_core_state_by_march` | command power, manpower, infantry equipment, stability | 4 |
| `fury_form_war_table` | command power, infantry equipment | 2 |
| `fury_mark_rival_column` | command power | 1 |
| `fury_share_terminal_reserves` | command power, manpower, infantry equipment, support equipment | 4 |
| `fury_assign_terminal_fronts` | command power, army experience | 2 |
| `anti_fury_border_watch` | command power, infantry equipment | 2 |
| `anti_fury_send_emergency_aid` | command power, infantry equipment, support equipment, trains | 4 |
| `anti_fury_firebreak_staff_talks` | command power, army experience | 2 |
| `anti_fury_start_supply_denial` | command power, infantry equipment | 2 |

The localisation owner reports inline rows capped at three iconized values and full tooltips containing the fourth amount. Active decision cost wrappers now compose per-resource getters so each component colors independently according to its own affordability, including the depot's support/manpower costs, core support/stability, emergency-aid trains, and reserve-share support. The verified texticons are vanilla `£command_power`, `£army_experience`, `£manpower_texticon`, `£infantry_equipment_text_icon`, `£GFX_train_texticon`, and `£stability_texticon`, plus the mod-defined `£support_equipment_text_icon` in `interface/chaosx_texticons.gfx`.

The depot payment trigger separates resource affordability from state/reserve availability, so those non-cost requirements do not gate whether payment is affordable. `fury_cost_display_quote_component` and its per-component getters provide the active wrapper values; the retired Survey and Recognition cost targets remain for compatibility with shared 026 selectors. The separate `fury_core_cost_text*` literal values likewise have no live decision consumer and remain only as a legacy shared-adapter target. The cost-display audit reports 129 below/exact/above boundary cases and 132 per-resource shortage patterns passed against its source model. Native GUI coloring and sale-source engine rendering remain unverified because the decision scenario route timed out.

The shared terminal-reserve and terminal-front command-power quote/gate constants are 29.99 and 24.99, while their normal-mode debits are 30 and 25. The 0.01 margin appears intentional for strict greater-than affordability checks, and costs display rounded to whole numbers, but resource precision and exact engine payment behavior were not testable through the unavailable decision route.

The reserve-share terminal/pact helper uses a fixed payload of 1,000 manpower, 600 rifles, and 40 support equipment. The effect owner reports that active Black Friday discounts may debit less than this transfer payload; the physical-conservation difference is unresolved and must not be presented as validated.

## AI validity, route locks, cleanup, and exploit notes

No `ai_will_do` score was edited. Availability changes affect the actor-selection pool, rival targets, depot action, route choices, crisis missions, and reserve-share target pool, so the probability auditor must compare the saved pre-edit source under the same named scenarios. That compare did not return.

The rival target check now runs against the actor in `PREV`, requires no legal ordinary neighbor unless the explicit hostile-scenario actor exception applies, and retains current faction/war/declaration checks. The share target rejects a dead, capitulated, donor, at-war, or hostile-rival recipient before payment.

The paid depot action cannot farm units beyond its bounded reserve: it consumes exactly one reserve and performs no extra stockpile/manpower grant. The focus route supplies separate one-time unit waves and later finite reserve refills; no world-loop spawning or new decision family was added.

War-table and rival-route actions cannot repeat once their route flags are set and both are hidden after the terminal world end begins. The removed Survey action could previously spend command power, increment the unread `fury_reach` value, and repeat a scan on cooldown; the regular target loop remains the only ordinary neighbor scan.

`fury_assign_terminal_fronts` can repeat every 60 days and applies momentum, preparation, cohesion, and overextension relief to all terminal actors for the caller's command power and army experience. `fury_share_terminal_reserves` can repeat every 45 days for paid aid and pact effects. Both are source-bounded by resource costs and cooldowns, but numeric balance/exploit tolerance remains a parent probability/balance follow-up.

## Localisation, event visibility, and report/news checks

The localisation handoff is `docs/plans/007_fury_plans/localisation_audit_2026-10-05.md`; the per-component implementation and source-model evidence are in `docs/plans/007_fury_plans/cost_display_audit_2026-10-05.md`. The text audit records the depot, route, mission, cost, focus-partner, and flag wording; its final focused source scan reports no missing Event 007 localisation bindings or raw Fury/Anti-Fury flags. It preserves the legacy cost-adapter keys for the removed Survey and Recognition buttons as requested.

The only decision-triggered event in the audited target flow is the hidden `chaosx.nr7.10` neighbor rescan. No report/news helper or coloured report/news output was added by these decision changes. The localisation owner reports `report_colour_audit.py --event 007` returned zero coloured report/news keys.

## References, validation, and skipped evidence

Required reads: `AGENTS.md`; `.agents/skills/chaos-redux-decisions-missions/SKILL.md`; `.agents/skills/chaos-redux-events/SKILL.md`; `.agents/skills/chaos-redux-subagents/SKILL.md`; `.agents/skills/chaos-redux-focus-trees/SKILL.md`; `docs/specs/007_fury_specs/specs/007_fury_decisions_missions_spec.md`; `docs/specs/007_fury_specs/prompts/007_fury_decision_mission_prompt.md`; `docs/specs/007_fury_specs/specs/007_fury_focus_tree_spec.md`; and `docs/plans/007_fury_plans/subagent_handoffs/2026-06-10_fury_decision_mission_audit_handoff.md`.

The offline Decision modding wiki was read at lines 83–110, 278–329, 357–372, and 465–478; SHA-256 `7713B9BCEE5F3818D63AAFBD45D18E812A9173A7C59AB238384B57DB60DB6162`.

The offline AI modding wiki was read at lines 26–55; SHA-256 `917CD261F7DA51FE4D8687C5D7663E768A09C5C101AC130CE646BC64637AA818`.

The offline Scopes wiki was read at lines 260–263 and its PREV examples were checked against `fury_is_valid_target`; SHA-256 `18EF5249E4991F5427ECA9EC4A2F66DD47F51E26A491C730ADC622F1F5DB1B49`.

Installed `triggers_documentation.md` was read for `any_owned_state` (1612–1620), `custom_override_tooltip` (2431–2450), `has_manpower` (4121–4127), `has_stability` (4800–4806), `is_controlled_by` (5381–5387), and `is_owned_by` (6088–6094); SHA-256 `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29`.

Vanilla `common/decisions/AFG.txt` lines 144–168 was read as a mission precedent; SHA-256 `DABC91C3F7FB1810D64D91D07147E827068D42540326CE10554A0752EE48D7A7`.

Meaningful source-contract validation was delegated to the effect owner. Its fixture covers ordinary and sale payment, all four depot shortages, reserve exhaustion, inactive actor, invalid state, BF payer rejection, one reserve debit, exact transfer recipient locking, and no payment on invalid targets. It reports an external BF quote stub and no engine proof.

The required HOI4 routes did not provide evidence: `hoi4.reference_context` and `hoi4.decision_inspect` returned “not available to the model”; `reference_search` was not callable; `source_lookup` and `script_validate` were not callable; and no revision-bound `reference_read` input was available. The probability worker preserved a baseline but did not obtain `probability_inspect`, scenario results, or `probability_compare`. Source-only review is not an equivalent substitute.

No live game was launched. No dedicated scripted GUI was introduced. The decision inspector returned only a partial inventory for the cost worker and no rendered cost-row scenario; native spacing, tooltip, and color presentation therefore remain unverified. No game-runtime or decision-scenario results are claimed. Current owned-source SHA-256 values are `common/decisions/007_fury_decisions.txt` `833713FFD36728CEB232DF50C0CA421AFFDD67505CED240266ABF95355066DCB`, `common/decisions/categories/007_fury_categories.txt` `6A3BDCC0C83C303FB2AF400B0F328D61EAC63679984844CCF9F2B24AAB53BD6D`, and `common/scripted_triggers/007_fury_triggers.txt` `B2FCD29AB46427D1E641787B18D3F7D445279E0468825C6447F602EAC079946F`.

## Parent follow-up

- Review the probability worker's final blocker and rerun `probability_inspect`, named scenario evaluations/sweeps, and same-scenario comparison when the service responds.
- Confirm whether the 29.99/24.99 terminal command-power quote gates versus 30/25 normal debits are acceptable with the game’s exact resource precision; no engine decision inspection returned.
- Resolve whether active Black Friday discounts may debit less than the fixed reserve-share transfer payload.
- Add the private `fury_cost_display_quote_component` caller contract to the shared scripted-effects documentation before another subsystem adopts this cost-display helper.
- Review the cost-display handoff's seven superseded numeric getter candidates before deleting any shared references.
- Remove now-unused `fury_anti_response` pressure constants from `007_fury_constants.txt` after eliminating all readers and writers.
- Give the remaining `fury_reach` value a visible threshold/consequence or retire its remaining focus writes in a broader accepted design pass.
- Review the Anti-Fury mission objectives against the named border, rail, depot, and aid-route requirements in the decision spec.

This handoff is the requested plan record at `docs/plans/007_fury_plans/decision_audit_2026-10-05.md`.

## Final parent dispositions, 2026-10-06

The above follow-up list is historical checkpoint evidence.
The parent implemented exact 30/25 CP quotation inputs, debit-derived reserve shipments with deferred settlement and refund, the private display-helper contract, removal of the seven obsolete numeric getters, and retirement of unread pressure/Reach counters and constants.
Those items are superseded by current source and the accepted release-spec addendum.
The named Anti-Fury mission logistics discrepancy and unverified native cost-row rendering remain unresolved.
Final probability outcomes are in the refreshed probability handoff, including partial recovered inspection and missing scenario state.
