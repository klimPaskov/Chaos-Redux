# Corridor Evacuation and Requisition Owner Patch

> **Superseded historical identifier banner (2026-08-25):** Any `fm_*` or `famine_migration_*` identifier quoted in this historical handoff is source-snapshot terminology only and is superseded; current authorities use separate `famine_*`, `migration_*`, or narrow neutral `civilian_transfer_*`/`humanitarian_*` names; see [source_of_truth_map.md](../source_of_truth_map.md).

Status: bounded owner patch complete in the shared worktree. No commit was created.

## Ownership and changed files

The only gameplay file changed by this owner pass is [common/decisions/famine_migration_decisions.txt](../../../../common/decisions/famine_migration_decisions.txt).

This handoff is the only new documentation file: `docs/plans/famine_and_migration_system_plans/subagent_handoffs/corridor_evacuation_and_requisition_owner_patch.md`.

The decision file already contained concurrent famine and migration edits when this pass began. Those edits were preserved; this patch is limited to the three evacuation consumers, the requisition consumer, and the named corridor mission/response surface.

## Changed decision identifiers

The corridor evacuation branch was added to `fm_famine_evacuation`, `fm_evacuate_vulnerable`, and `fm_evacuate_workers`.

The flat pressure mutations were removed from `fm_requisition_safer_state`.

The empty `complete_effect` was removed from `fm_negotiate_corridor`.

`fm_mission_hold_humanitarian_corridor`, `fm_accept_corridor_offer`, and `fm_reject_corridor_offer` received no additional gameplay or AI-weight tuning.

## Corridor branch behavior

Each evacuation consumer first checks the selected origin for `famine_migration_corridor_accepted`.

An accepted origin calls `famine_migration_execute_corridor_evacuation` only when `famine_migration_corridor_operation_is_valid` proves an evacuation operation and the corridor has not already recorded `famine_migration_corridor_evacuation_proven`.

The corridor branch consumes the helper's `famine_migration_corridor_transaction_result`, `famine_migration_corridor_evacuation_actual_debit`, `famine_migration_corridor_evacuation_route_deaths`, and `famine_migration_corridor_evacuation_survivor_credit` outputs for decision-local pressure, route-death stability, report, and arrival-evidence follow-up.

`fm_evacuate_vulnerable` and `fm_evacuate_workers` also clear their consumed `famine_migration_evacuation_prepared` flag after a valid corridor transaction.

The corridor branch does not call the general destination selector, `famine_migration_record_displaced_cohort`, `famine_migration_bind_cohort_destination`, `famine_migration_apply_reception_delta`, or any duplicate trapped-population or mission-slot mutation. Those responsibilities remain in `famine_migration_execute_corridor_evacuation` and its corridor helpers.

An accepted but stale or invalid corridor enters the accepted branch and does nothing; it cannot fall through to a weighted destination. The weighted `famine_migration_select_general_safe_evacuation_destination` branch is available only when the origin has no accepted corridor. The ordinary exact transfer, cohort, destination, reception, and generic evacuation-mission path remains unchanged for that no-corridor branch.

## Requisition and relief behavior

`fm_requisition_safer_state` still initializes the selected destination and donor, requests one exact reserve transfer, and relies on `famine_migration_requisition_food_reserves` for the sole reserve debit/credit transaction.

The old destination `famine_migration_food_pressure` subtraction, donor pressure addition, relief-fraction temporaries, and unused donor denominator were removed.

After a valid transfer with destination credit above the existing minimum grant, the destination calls `famine_migration_mark_relief_access`, preserves the existing route/relief mission success-or-arm logic, registers the destination food state, and the requester records the existing report, stability outcome, strained-state flag, and predatory-requisition achievement evidence.

No supply, reserve, or direct pressure value is fabricated by the decision follow-up.

## Mission and response review

`fm_mission_hold_humanitarian_corridor` still uses the exact corridor mission validity and finalize/expire helpers. Its success and timeout outcomes remain owner decision effects, while the corridor helper retains transaction and cleanup ownership.

`fm_accept_corridor_offer` and `fm_reject_corridor_offer` continue to call the public corridor response aliases with the shared offer-validity trigger. Their AI bases and modifiers were deliberately not tuned.

`fm_negotiate_corridor` still prepares and submits the exact corridor offer and charges its declared costs only after a valid offer submission in its existing `remove_effect`; changing that timing was outside this bounded tranche and remains a parent review point against the vanilla custom-cost convention.

## Validation and evidence

Required source review was completed before editing: `AGENTS.md`, all eight famine/migration specification parts and supporting matrices/prompts, the decisions/missions and state-ledgers skills, the subagent skill, relevant offline Paradox wiki pages, and the required vanilla documentation and decision precedents.

The parent confirmed focused Clausewitz brace balance after the patch. Source searches confirm three corridor helper call sites and retain the general selector only in each no-accepted-corridor branch.

A fresh read-only `hoi4.gui_inspect` of `famine_migration_report_header_window` with the `default` scenario completed before the final shorthand correction and produced artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8cc3cc0111f7aced92f116d4fc57c75c0132810fe90920cf2342b58eb77f14d4/f2f8f81b9a8444611b2ae1b828c38154b9bce90677d7f60921bfb680cf510dad/gui-inspect.7ad991d52af50b53.json`.

That inspect identified three unsupported long-form `check_variable` comparisons in the newly added survivor-credit guards; the guards were corrected to the repository's accepted shorthand immediately afterward. The post-correction inspect retry was interrupted at the parent agent's stop request, so no post-correction GUI inspect artifact is claimed.

The required read-only `hoi4.gui_render` request for the same window, `default` scenario, normal/active/warning/long-text/missing-localisation states, and 1920x1080 plus 1280x720 resolutions timed out after 180 seconds with no artifact. The inspect artifact also contains known workspace-wide graph truncation, overlap, and unrelated collision diagnostics; it is not a clean visual-quality certification.

A fresh source-only `hoi4.probability_inspect` request for `common/decisions/famine_migration_decisions.txt` timed out after 180 seconds. The callable tool registry exposed no `chaosx_ai_probability_auditor` route, so no auditor baseline/evaluate/sweep/compare claim is made. Existing decision, mission, corridor acceptance, and destination-selection AI factors were not changed and remain for the later named-scenario probability audit.

No live Hearts of Iron IV launch or gameplay validation was performed, as required by repository policy.

## Remaining blockers and risks

1. High: the mandatory `chaosx_ai_probability_auditor` route is unavailable in this runtime, and the direct source probability inspection timed out. AI validity and balance for the unchanged weights remain unresolved until the parent runs the named scenarios through the auditor and same-scenario compare.
2. High: the post-correction GUI inspect and the requested GUI render lack fresh usable post-patch artifacts because of interruption/timeout. No GUI layout or visual-fidelity claim is made.
3. Medium: counterpart-country response visibility and save/reload resolution of `var:<database_id>` corridor pointers still require runtime validation in the existing helper contract; this pass did not change those helpers.
4. Medium: the corridor attack-disqualification owner callback remains outside this decision file and is not supplied by this patch.
5. Low: negotiation cost timing remains deferred to successful offer submission in `remove_effect`; the parent should decide whether the ordinary decision should instead debit its custom costs at selection time under the vanilla convention.

No other files, constants, helper contracts, localisation, hooks, mapmodes, assets, or AI weights were changed by this owner patch.
