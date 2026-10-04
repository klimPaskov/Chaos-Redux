# Legacy genocide crisis decision disposition handoff

Status: the German decision's paid post-administration exact-cohort route is accepted under the user's explicit 2026-09-26 choice and present in current source; engine scenario and AI probability validation remain pending.

Acceptance basis: `accepted_implementation.md` records the user's explicit 2026-09-06 request for the complete Camps, Forced Labor and Repression plan. Its accepted contract makes administration mandate, priority, spending ceiling, finite cohorts and country institution slots responsible for routine output; meaningful famine, evidence, review, closure and aftermath outcomes remain explicit.

Additional acceptance basis: `accepted_implementation.md:37-38` records the user's explicit 2026-09-26 choice to keep a separate paid German prisoner-transfer decision after administration begins, drawing from a verified living occupation cohort through the exact occupation-to-custody transaction. The dated automatic Łódź route remains separate.

## Exact identifier dispositions

| Decision ID | Disposition after `camp_admin_initialized` | Source evidence and reason |
| --- | --- | --- |
| `germany_intensify_extermination_policy` | Retired | `genocide_germany_intensify_extermination_policy` applies the legacy timed death multiplier and crisis counters. The action is already cut over in visible and available. |
| `germany_transfer_prisoners_to_experiment_site` | Retained as one paid post-administration exact-cohort national order; current source evidence, engine proof pending | The decision now requires `camp_admin_initialized` and uses `camp_occ_manual_transfer_country_ready` and `camp_occ_manual_transfer_can_pay`. The bounded `camp_occ_refresh_manual_transfer_source` helper selects the oldest preflight-valid registered occupation row and displays its source state, avoiding a map-target fanout. Its completion calls `camp_rework_germany_apply_exact_cohort_transfer`; the helper quotes 5% of that living row, caps the request by state-88 capacity and population-share headroom, and calls `camp_occ_transfer_to_custody_exact`. The caller charges 35 political power, 5 army experience, 180 support equipment and 18 trains only after a valid positive custody receipt. The former pre-initialization route and manpower fifth cost were retired. |
| `genocide_intensify_deportations` | Retired | AI-only repeatable site-pressure and multiplier action; visible and available already require pre-initialization. |
| `genocide_redirect_trains_and_supplies` | Retired | AI-only timed transport-priority and site-pressure action; visible and available already require pre-initialization. |
| `japan_transfer_prisoners_to_experimental_facilities` | Retired | The legacy selected-state effect can instantly build a new concentration camp before registering an experiment site. The accepted Japan program uses the bounded Pingfang institutional slot and supported-site rules. Visible and available were already cut over; a matching `target_root_trigger` guard is now present. |
| `sov_deport_suspected_opposition_groups` | Retired | The effect registers a new Gulag repression site and its finite monthly policy. Its visible, target-root and available checks already require pre-initialization. |
| `sov_confiscate_food_from_disloyal_regions` | Retained as the explicit famine crisis route | The effect sets famine-pressure flags, increases `sov_famine_state_pressure`, registers the famine site and feeds Soviet famine events. It contains no instantaneous population debit and no `camp_admin_initialized` guard was added. |
| `sov_raise_forced_labor_quotas` | Retired | The selected-state effect raises the legacy forced-labor pressure and adds site exploitation pressure. The administration country helper states that annual/monthly quota administration moved into the paid finite-cohort pulse. Visible and available already require pre-initialization; a matching `target_root_trigger` guard is now present. |

The six retired IDs remain listed under `merge_or_replace_operational` in `source_inventory.json`. The famine and German transfer IDs are listed under `retained_meaningful_routes`; `unresolved_routes` is empty for this reviewed set. The German entry's acceptance basis, current source evidence and validation limit are recorded separately. The decision's previous pre-initialization path is retired; the dated automatic Łódź path remains a separate movement.

## Changed files and behavior

The 2026-09-25 disposition pass added `NOT = { has_country_flag = camp_admin_initialized }` to the `target_root_trigger` blocks for the then-unresolved Germany transfer, replaced Japan transfer and replaced Soviet forced-labor-quota decisions. The 2026-09-26 German repurpose removed its pre-initialization cutover, requires `camp_admin_initialized`, and routes the selected state through the exact occupation-to-custody helper; Japan and Soviet quota retirement remains as recorded. The earlier broad patch's accidental guards on `japan_conduct_anti_partisan_reprisals` and the Soviet famine decision were removed before that pass's validation.

`docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/source_inventory.json` classifies Soviet food confiscation as a retained famine crisis route and records the source-level rationale for all eight IDs. Its German entry now records the later user decision and source repurpose, while preserving the other seven per-ID dispositions.

This documentation reconciliation changes no gameplay, AI weights, effect files, GUI files or localisation files. The German source repurpose changed its decision, triggers, effects, constants and localisation in the shared implementation; that change is source evidence for this handoff, not an edit made here. The transfer helper records a living movement rather than an immediate death or research reward.

## Validation and limits

The offline Decision modding, Effects, Triggers, Data structures and Scopes wiki snapshots were consulted along with vanilla `effects_documentation.md`, `triggers_documentation.md` and targeted vanilla state-targeted decision precedents. The decision wiki documents that `target_root_trigger` is evaluated for the decision's country before per-target checks. The German root gate now calls `camp_occ_manual_transfer_country_ready`, which requires initialized administration and the controlled destination; the former root cutover is historical behavior.

The 2026-09-25 source checks confirmed cutover guards for all six replaced IDs and the then-unresolved German transfer, matching root guards for the three targeted gaps, an unguarded retained famine effect and no accidental cutover on the Japan anti-partisan route. The 2026-09-26 source check confirms that the German decision's visible, root and available gates now require the post-administration path; the other dispositions have not been reopened by this documentation pass. `source_inventory.json` parsed successfully as JSON.

The German transfer is now one national decision under the user's compact-presentation choice. A bounded country helper selects the first preflight-valid registered occupation row in insertion order, and scripted localisation names the current source; the decision has no state-target fanout. Its visible and available gates require the initialized route and its selected-source and destination checks. The AI uses the same decision definition with `ai_will_do = { base = constant:genocide_ai_weight.germany_direct_holocaust }`; the old site-creation cap no longer blocks a movement that creates no site. The available-cost checks and completion debit cover political power, army experience, support equipment and trains. The custom cost and blocked/hover strings in `localisation/english/chaosx_decisions_l_english.yml` use those same script constants and texticons.
After a positive receipt the exact wrapper retains the old route's crisis activation, decision count, escalation and hidden-attempt pressure so report and exposure gates still see the order. Camp evidence, tribunal pressure and history also advance; cloning/research progress does not, because institutional work has its own continuing payment and award gate.

No non-weighted HOI4 decision-inspection route is exposed in the tool set examined for this documentation pass. Tool exposure alone does not establish service health. No matching decision engine scenario, exact-cohort conservation proof or scenario-specific `hoi4.probability_inspect`/`hoi4.probability_compare` handoff was supplied to this pass. Parent-side source and MCP review remains required; the user owns live-game validation.

The German source now calls the occupation-to-custody transaction with a proven living occupation row; the previous whole-population request and pre-initialization route are historical source behavior. Source review still cannot prove exact-once population and row conservation, rollback, displayed costs or AI selection in the engine. Future Mengele work should continue to follow the accepted rule that experiment-specific technical procedures are not introduced.

## Documentation reconciliation handoff

| Source or working document | Disposition and basis |
| --- | --- |
| `accepted_implementation.md` | Accepted design: the 2026-09-06 full-plan request and explicit 2026-09-26 German transfer choice are recorded there; the dated Łódź route stays separate. |
| `source_inventory.json` | Current-state ledger: the German route is retained with source evidence and a validation limit; the other seven reviewed crisis decisions keep their prior dispositions. |
| This handoff | Historical 2026-09-25 review supplemented by the 2026-09-26 German repurpose; old pre-initialization and unresolved German conclusions are superseded by the current decision, trigger and effect source cited above. |

There is no unresolved acceptance decision for the German paid route. Its transaction, costs, target gates and AI selection remain pending engine and specialist probability evidence; no MCP artifact or source revision was available to this documentation pass. The source inventory's broader accepted and queued plans, GUI and event MCP gaps, and other handoffs were left unchanged.

The scoped files contain no duplicate German disposition after this edit and no stale prompt instruction was found in either file. The replaced German status sentences are the superseded documentation; no document was deleted or merged. No accidental mid-sentence Markdown hard wraps were found in this handoff, and its table rows, headings and paragraph boundaries were preserved. Parent review should verify the exact transaction and source conservation, obtain the scenario-specific AI probability handoff, and retain user live-game validation as the final consumer check.
