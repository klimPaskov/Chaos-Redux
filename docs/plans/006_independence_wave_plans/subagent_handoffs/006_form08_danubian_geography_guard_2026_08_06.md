# Event 006 FORM-08 Danubian geography guard - 2026-08-06

## Verdict

Applied one narrow fail-closed source fix to keep the FORM-08 helper aligned with the accepted Danubian geography. The helper no longer treats IW-026 Macedonia (MAC, state 106) as a FORM-08 member, integration target, or capital fallback. The registry minimums remain three members, three consents, and three unique anchors, so this change cannot create a formation path from an unaccepted substitute. FORM-08 remains intentionally incomplete until the accepted Vojvodina overlay and Slavonia package/map gates are independently resolved.

## Authority and evidence

The accepted family row in `docs/specs/006_independence_wave_specs/matrices/006_formable_family_registry.csv` names Transylvania, Banat, Vojvodina, Slavonia, and compatible members for FORM-08. The candidate registry binds IW-023 Transylvania to TRA states 84|76, IW-024 Banat to AXX state 82, IW-025 Vojvodina to a non-selectable HUN-origin overlay at state 45, and IW-032 Slavonia to BFX with no unique current-map binding. IW-026 Macedonia is a separate MAC package on reservation group RG-106 and is not listed as a FORM-08 geography member.

The installed-map binding ledger records IW-024's optional state 764 extension as colliding with IW-025's optional West Banat extension. The reservation group `RG-DANUBE-BORDERLAND` permits at most one automatic package per coarse state and requires a current-map substate, negotiated formable, later secession, or scenario variant for additional identities. The region-03 trigger explicitly keeps IW-025 as `always = no` because it is an overlay and omits IW-032 because no unique Slavonia anchor exists.

The read-only `hoi4.map_inspect` pass inspected states 45, 76, 82, 84, 106, 109, and 764 in workspace `mod_chaos_redux_ea3b2d67c2c0`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/92bf99313df470c966388078decb9c476f05ef376703db0d2b6fe61acddb41e1/83302ed18f5e30cec1bfbd481ddc82ba59a37364f8d481701010726af7119a91/map-inspect.8d2d804287013e4a.json`. The map-files, bitmap geometry, state-region membership, and network/adjacency checks passed for the inspected state set; global map-position and port diagnostics failed elsewhere in the installed map and are not treated as FORM-08 runtime proof.

## Files changed

* `common/scripted_triggers/006_independence_wave_form08_triggers.txt`
* `common/scripted_effects/006_independence_wave_form08_effects.txt`
* `docs/plans/006_independence_wave_plans/subagent_handoffs/006_form08_danubian_geography_guard_2026_08_06.md`

## Helper changes

* `is_independence_wave_form08_eligible_member` now accepts only the existing TRA state-84 and AXX state-82 anchor branches. Its sovereignty, Event 006 active-origin, family-selection, anchor ownership/control, and capital checks are unchanged.
* The deleted MAC state-106 branch also disappears from every caller that consumes the eligibility trigger, including the shared member and member-candidate ledger paths. No new Vojvodina or Slavonia branch was added.
* `independence_wave_formable_integration_adapter_8` no longer transfers MAC state 106 or selects it as the post-formation capital. It still transfers only the explicit TRA 84/76 and AXX 82 rows when a frozen consenting member has full-integration authorization.

## Helper map and call-site contract

* `is_independence_wave_form08_eligible_member` is a country-scope, no-argument read-only trigger. It consumes the active-origin flag, selected-family variable, anchor variable, original tag, anchor ownership/control, and capital scope, and returns a boolean admission result to `is_independence_wave_form08_member`, `has_independence_wave_form08_exact_carrier_anchor`, and `has_independence_wave_form08_member_candidate`. The generic formable ledger builder and recount effects consume those wrappers; the trigger has no side effects.
* `independence_wave_form08_register_readiness` remains a country-scope, no-argument adapter. It reads the TRA/state-84 territory and capital proof and emits the family, territory, identity, flag, integration, and readiness receipt flags. The generic family-registration dispatcher calls it before identity mutation; this patch does not widen that call site.
* `independence_wave_formable_integration_adapter_8` remains a country-scope, no-argument effect. It consumes mutation proof, identity commitment, aligned frozen member/consent arrays, and full-integration authorization, then transfers only the TRA/AXX states listed above or installs the existing autonomous-member idea. It emits the existing integration and post-formation flags and is dispatched by the shared formable integration adapter.

No event target is created, renamed, or persisted by this guard. Existing parallel ledger arrays, generation variables, identity flags, and autonomous-member ideas retain their current cleanup order through `independence_wave_form08_cleanup_runtime` and the generic Event 006 teardown.

## Migration plan

No cross-file helper migration is required. The eligibility branch removal automatically propagates through the existing member, carrier, candidate, registry-ledger, identity-proof, and integration call sites. The parent should update stale FORM-08 prose that still names MAC after reviewing the package and compatible-member gates; adding a new geography branch before those gates are attested would be an unsafe migration.

## Readiness, identity, and cleanup

The generic ledger builder and recount effects remain unchanged and continue to iterate only active Event 006 origins with aligned parallel arrays. The FORM-08 readiness adapter remains TRA/state-84-specific, and the HUN_EMPIRE identity clearance, mutation proof, rollback, and cleanup helpers were not weakened or bypassed. Runtime commit proof still reads the registry constants `minimum_members = 3`, `minimum_consents = 3`, and `minimum_anchors = 3`; the intermediate two-anchor corridor threshold was not changed.

Vojvodina remains a HUN-origin route overlay and is not promoted to a standalone country or ledger member by this patch. Slavonia remains unbound because the installed map has broad Croatia state 109 rather than a unique Slavonia state. No package, tag, state reservation, identity, threshold, or compatibility-member policy was invented.

## Constants and dynamic helper documentation

No script constant or generic dynamic scripted effect was added or changed. `common/scripted_effects/chaosx_dynamic_effects.md` was intentionally left untouched because this was a direct FORM-08 admission correction and that file already contains unrelated in-progress documentation changes from the parent worktree.

## Validation

The following task-relevant static audits passed after the patch: `python -B .tools/audit_event6_flags.py --strict` reported 102 complete flag families; `python -B .tools/audit_event6_allocator.py` passed allocator and reservation ordering; `python -B .tools/audit_event6_scenario_matrix.py` passed all 32 SCN-008 cells and 8 edge cases; `python -B .tools/audit_event6_gui_matrix.py` passed the Event 006 statehood-ledger semantic matrix; and `python -B .tools/audit_chaosx_country_tags.py --surface-scan` reported zero external country-definition or identity-surface collisions. A source scan confirms that the two FORM-08 helper files contain no remaining `MAC` or `Macedonia` branch.

No Hearts of Iron IV process, live save, save/load cycle, probability simulation, or runtime event execution was run. The map-inspect artifact is read-only evidence and its unrelated global position/port failures remain a limitation.

## Remaining gates and parent follow-up

* IW-024 Banat still requires its package-level readiness and runtime evidence before it can carry or commit FORM-08; the source binding alone is not an admission receipt.
* IW-025 Vojvodina requires an explicit compatible-member/overlay policy if it is ever allowed to contribute to FORM-08, while remaining non-selectable as a new country.
* IW-032 Slavonia requires a unique current-map substate or a formally approved negotiated/secession route, plus package research, before it can enter the ledger.
* The accepted compatible-member policy, HUN_EMPIRE concurrent-identity behavior, and save/load behavior remain parent-owned review gates.
* Several older FORM-08 reports and system pages still describe MAC as a current helper anchor. The parent should reconcile those source-of-truth documents with this guard before claiming the family is complete; this handoff does not promote any package or claim completion.

No fallback, threshold reduction, geography broadening, or unrelated gameplay edit was made.
