# Event 006 FORM-08 current Danubian gate audit - 2026-08-03

## Verdict

The shared FORM-08 scripted path is source-consistent with authority v105 and the accepted adapter handoff, with a deliberate runtime admission hold for unresearched AXX and MAC package adapters. No gameplay helper, trigger, constant, or threshold patch is warranted in this audit. AXX and MAC remain fail-closed.

## Authority and scope

This audit used `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw023_form08_danubian_adapter_2026_08_03.md`, `docs/plans/006_independence_wave_plans/subagent_handoffs/006_form08_ledger_gate_repair_2026_08_03.md`, `docs/plans/006_independence_wave_plans/006_event6_current_completion_evidence_v105_2026_08_03.md`, and `docs/systems/006_independence_wave_form08_danubian_confederation.md` as the current design evidence.

The reviewed surface covers carrier readiness, member and anchor ledgers, consent snapshots, HUN_EMPIRE identity clearance, generic congress ordering, identity and integration adapters, post-formation ledgers, project decisions, rollback, cleanup, and TRA/AXX/MAC admission boundaries.

## Existing helper map

* `is_independence_wave_form08_eligible_member` is a country-scope trigger that accepts only active sovereign Event 006 countries with selected family 8, a matching anchor variable, an owned and controlled capital anchor, and the researched TRA 84, AXX 82, or MAC 106 row. It excludes autonomous/full formable, founding-proposal, and Soviet-origin replacements. The registry ledger builder and member-candidate trigger consume it.
* `has_independence_wave_form08_identity_clearance` is a country-scope trigger with global and world identity checks. It rejects the FORM-08 global lock, the vanilla Austria-Hungary formation flag, and any living `HUN_EMPIRE` cosmetic carrier. The identity adapter consumes it without side effects.
* `has_independence_wave_form08_corridor_ready`, `has_independence_wave_form08_strict_mutation_preconditions`, and `has_independence_wave_form08_runtime_commit_proof` are layered country-scope gates. The corridor gate is an intermediate two-anchor check; runtime proof restores the registry minimum of three members, three anchors, and three consents before mutation.
* `independence_wave_formable_build_member_and_anchor_ledgers` and `independence_wave_formable_recount_member_and_anchor_ledgers` are the shared action-time ledger effects. They write parallel member, generation, anchor, consent, and integration arrays and recount member, anchor, consent, observer, opposed, and controlled-anchor totals.
* `independence_wave_form08_register_readiness` is the family-registration adapter. It currently attests FORM-08 only from the researched Transylvania package with state 84 ownership and capital control. There is no AXX or MAC package registration call, so those packages cannot silently become carriers.
* `independence_wave_formable_identity_adapter_8` is the mutation identity effect. After mutation prevalidation, identity clearance, and runtime proof, it sets `HUN_EMPIRE`, the global identity lock, the carrier flag, and the identity-committed receipt.
* `independence_wave_formable_integration_adapter_8` consumes only frozen consenting rows. Full-integration authorization transfers TRA 84 and optional 76, AXX 82, or MAC 106. Other consenting rows receive autonomous membership and retain their Event 006 origin. It counts two additional members beyond the carrier before committing integration and selects capital in deterministic 84, 82, 106 order.
* `independence_wave_form08_start_postformation_progression`, `independence_wave_form08_change_charter_values`, and `independence_wave_form08_refresh_charter_idea` own the four post-formation ledgers, clamped 0-100 values, and provisional/coordinated/integrated charter promotion.
* `independence_wave_form08_rollback_identity` and `independence_wave_form08_cleanup_runtime` own identity rollback, autonomous-member idea cleanup, project removal, ledger clearing, and global lock release. The generic decision-layer cleanup calls them before the shared active-origin teardown.

## Admission and cleanup ordering

The generic order is complete discovery, ledger build and recount, congress vote, congress-ready receipt, commit prevalidation, FORM-08 runtime proof, identity adapter, integration adapter, active/committed receipts, post-formation initialization, and proposal closure.

The member arrays preserve the generic active-country iteration order and carry the frozen generation, family, sequence, anchor, and consent rows. No TRA-first reorder is introduced. TRA is the only currently researched carrier because its package calls family-8 readiness registration; AXX and MAC remain prospective member rows only if a future researched package supplies family selection and anchor state.

Rollback clears `HUN_EMPIRE`, its global lock, and the carrier receipt when integration has not committed. Runtime cleanup removes FORM-08 decisions and autonomous ideas, drops the cosmetic identity, clears the global lock, clears post-formation flags and four ledger variables, and then the generic cleanup clears arrays, profile variables, consent snapshots, and transaction flags. `independence_wave_end_active_origin` reaches this path through `independence_wave_cleanup_decision_layer`, including annex and dissolution cleanup.

## Constants and tuning table

* `independence_wave_formable_registry.danubian_confederation` remains the authoritative registry row with minimum members 3, minimum consents 3, and minimum anchors 3.
* `independence_wave_formable_tuning.minimum_member_anchors = 2` is retained only for the intermediate corridor gate. It is not a commit threshold because `has_independence_wave_form08_runtime_commit_proof` explicitly checks the family registry minimums.
* `independence_wave_form08_value` centralizes the four ledger range, starting values, gains, losses, and coordinated/integrated thresholds of 50 and 75.
* `independence_wave_form08_duration` centralizes the 120-day congress, 180-day arbitration, and 150-day transport decision windows.

No new constant or threshold is proposed. Lowering any FORM-08 admission threshold would violate the authority contract.

## Migration plan

No duplicated FORM-08 admission or cleanup logic was found that can be safely extracted without changing the shared registry contract. Existing call sites already dispatch family identity and integration through the generic meta-effect helpers. No migration is required.

## Risks, unsupported evidence, and holds

* The region-03 loader can reserve IW-024 AXX state 82 and IW-026 MAC state 106, but reservation is not a FORM-08 readiness attestation. Their package adapters, source evidence, and runtime setup are not yet researched. They must remain fail-closed.
* The accepted family registry names Transylvania, Banat, Vojvodina, Slavonia, and compatible members, while the audited adapter admits only TRA, AXX, and MAC anchors. Vojvodina remains the HUN-origin overlay and the Slavonia/map crosswalk remains unresearched. No geography broadening is authorized.
* The header shorthand `TRA 84/76` describes the optional full-integration transfer. The carrier and member eligibility gate still requires TRA anchor 84; state 76 is not an independent carrier anchor.
* Static evidence confirms HUN identity collision guards and cleanup calls. Independent living-carrier coexistence and save/load behavior remain untested because live-game validation is outside this subagent scope.

## Validation

The following task-relevant static audits passed in the current workspace: `python -B .tools/audit_event6_flags.py --strict` reported 102 complete flag families; `python -B .tools/audit_event6_allocator.py` passed the 6/8/10/14/20 allocator ladder and reservation ordering; `python -B .tools/audit_event6_scenario_matrix.py` passed all 32 SCN-008 cells and 8 edge cases; `python -B .tools/audit_event6_gui_matrix.py` passed the Event 006 statehood-ledger semantic matrix; and `python -B .tools/audit_chaosx_country_tags.py --surface-scan` reported zero external country-definition or identity-surface collisions.

No Hearts of Iron IV process, live save, save/load cycle, or whole-event AI simulation was run. No fallback, threshold reduction, package promotion, or unrelated file change was made.
