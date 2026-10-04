# Event 31 mission receiver isolation review

## Disposition and scope

Read-only bounded review of the final owner-isolation source set identified by the user; this handoff is the only file created by this review.

The accepted design basis for this review is docs\specs\031_random_terror_specs\031_random_terror_decision_mission_matrix.md and docs\specs\031_random_terror_specs\031_random_terror_decision_mission_prompt.md.

The before-behavior summary below comes from the named prior owner-contract handoff; this review did not reread or compare the frozen 2026-10-03 source snapshot.

The review followed AGENTS.md, .agents\skills\chaos-redux-subagents\SKILL.md, .agents\skills\chaos-redux-decisions-missions\SKILL.md, 031_mission_owner_and_progress_contract_20261003.md, 031_mission_owner_probability_baseline_20261003.md, and the named 031_mission_reference_refresh_20261004.md.

No gameplay, localisation, GUI, asset, workbook, Git, game-launch, or log operation was performed.

This is not a full Event 31 mission-completion or balance claim; success progression, exact cost/resource design, and numeric AI comparison remain open.

## Final source snapshot reviewed

Workspace: C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux

| Current source path | SHA-256 |
| --- | --- |
| common\decisions\031_random_terror_missions.txt | C775B7556270CFFAE07B33C1B8435D50B5990B1C8EA1383654E70C8458A71BD2 |
| common\decisions\031_random_terror_decisions.txt | 810E8EEC735E2AEDB35571609E1EA070443129C18E3B34ABC1F1F4A13C379236 |
| common\scripted_effects\031_random_terror_effects.txt | 7BCE6DFA2B13CB3707D88B868F8393B73892CB914952C608565F0D499318F460 |
| localisation\english\031_terrorist_attack_l_english.yml | 94203E52F8701E92114EDEE5CD641E2C6D0EFFBAD664F340495FFBF1F20394F1 |

The current mission source is 819 lines and contains exactly 24 calls to random_terror_close_country_recovery.

These hashes were re-read from the live repository immediately before writing this handoff and match the final hashes supplied by the user.

## Severity-ranked findings

### High — Five success-receipt loops and hostage completion remain unresolved

The owner-key patch does not complete mission progress, consistent with the parent’s stated queue.

random_terror_contain_attack_wave requires random_terror_containment_success_@ROOT, whose only current setter is its success resolver; both setup callers clear the keyed marker and no post-start producer was found.

random_terror_protect_transport_network requires random_terror_transport_protection_success_@ROOT; the starter helper writes it before activation, the caller clears it, and the remaining setter is the success resolver.

random_terror_break_cross_border_corridor requires random_terror_support_disruption_success_@ROOT; the caller runs random_terror_decision_disrupt_support, which sets only a country flag, while random_terror_resolve_support_disruption has no call site and the mission success resolver is the other setter.

random_terror_prevent_capital_seizure requires random_terror_capital_security_success_@ROOT; its starter helper writes the marker, its caller clears it before activate_mission, and the remaining setter is the success resolver.

random_terror_restore_civil_authority requires random_terror_civil_authority_restored_@ROOT; the starter helper writes that marker, the caller clears it before activation, and the remaining setter is the success resolver.

random_terror_hostage_deadline has only success and failure timeout branches, with no partial outcome.

The hostage progress producer is random_terror_decision_security_surge, but that decision’s availability and payment guard require slot 1 to be empty while the hostage mission occupies slot 1; its success action is therefore blocked during the mission.

Do not treat the owner-key changes, callback closures, or this review as fixing those mission outcomes.

### Medium — Target transfer does not rebind or immediately invalidate the old receiver’s mission

All eight mission cancellation triggers test the receiver-keyed subject receipt, family state, shared slot, and route or crisis conditions, but do not generally test whether the target’s owner or controller has changed.

A transfer therefore leaves the original receiver’s keyed receipt and mission in place until another cancellation condition or timeout resolves it; the receipt is not reassigned to the new controller.

This is not cross-receiver consumption or cleanup: keyed ownership stays with the original mission receiver.

The parent should disposition target-transfer behavior per mission while preserving foreign-owned or foreign-controlled accepted targets and the external claimed/core retake design; do not add a blanket owner-equals-ROOT rule.

### Medium — One unkeyed state fact has a live achievement consumer

random_terror_decision_restore_services sets the generic state flag random_terror_civil_authority_restored at 031_random_terror_effects.txt:2279, before the timed restoration mission succeeds; the mission resolver also sets this generic fact at line 3871.

031_random_terror_achievement_effects.txt:653 reads the generic fact when evaluating the No Collective Punishment achievement condition.

The mission’s receiver-specific completion marker is separate and is cleared before activation, so this generic state fact is not a receiver receipt.

Its intended meaning is unresolved from this bounded owner review: it may record the immediate service-restoration action, or it may be prematurely representing successful civil-authority restoration to the achievement check.

random_terror_clear_state_commitments still clears base, unkeyed state flags, but the scanned active mission conditions, setup writers, and mission callbacks use receiver-suffixed receipts; no other active unkeyed mission-subject or progress consumer was found.

### No receiver-isolation defect found in the reviewed owner/callback paths

Direct country decision starts key their state subject and progress receipts with @ROOT; hostage and coordinated-uprising setup enter the target controller before writing the state receipt with @PREV, and subsequent mission callbacks use that receiver as ROOT.

The uprising start registers the controller’s slot, family flag, target variable, subject receipt, and cleared progress receipt before applying uprising pressure or transferring control.

The shared random_terror_government_response_category contains all eight non-selectable missions, each with a distinct country family-active flag and its assigned shared slot.

Each mission activation requires its own family-active flag, its shared slot, and its exact receiver-keyed state subject; each cancel, completion, and timeout callback is guarded by that mission’s family-active flag.

Every callback clears only the current receiver’s suffixed subject/progress receipts, its own slot and family flag, and its own target variable before calling random_terror_close_country_recovery.

The 24 calls comprise the cancel, complete, and timeout callback for each of eight missions; repeated callbacks become no-ops after the first callback clears that family-active flag, so a later family using the same slot is not cleared by the old family callback.

The mission owner/target variables are random_terror_mission_target_containment, random_terror_mission_target_transport, random_terror_mission_target_corridor, random_terror_mission_target_capital, random_terror_mission_target_retake, random_terror_mission_target_restore, random_terror_mission_target_hostage, and random_terror_mission_target_uprising; each setup path writes its country-scoped target and each mission callback plus country cleanup clears that receiver’s variable.

random_terror_clear_country_commitments uses @PREV inside its every_state loop to key cleanup to the current receiver even when an outer ROOT differs; random_terror_clear_state_commitments clears only unkeyed base state flags and does not clear the other receiver’s suffixed receipts.

random_terror_clear_actor_runtime and random_terror_cleanup_actor run owner-local country cleanup before their owned-state generic cleanup, so generic actor cleanup does not erase another receiver’s keyed mission receipts.

random_terror_resolve_defeat deliberately iterates every country through owner-local receipt cleanup and then every state through generic state cleanup; this is the explicit all-country teardown path.

No is_owned_by = ROOT requirement was found in these mission targets; current control requirements remain only where already used, including transport, capital, restoration, and retake progress.

## Starter transaction order and before/after behavior

Before the starter fix, the owner contract handoff reported that random_terror_decision_restore_services could call random_terror_close_country_recovery after writing its target receipt but before registering its mission family and slot, allowing the close helper to clear the newly written metadata when recovery conditions were otherwise complete.

In the current source, the restore-services paid start checks that slot 3 is free before debiting its costs, writes the exact selected-state subject, reserves slot 3, registers random_terror_mission_active_restore, stores the target variable, and only then calls random_terror_decision_restore_services.

The helper still calls random_terror_close_country_recovery, but that close effect now refuses to clear country commitments while any of slots 1, 2, or 3 is active; after the helper returns, the caller clears the transient owner-keyed success receipt and activates random_terror_restore_civil_authority.

That ordering prevents the reported self-erasure; moving the helper or adding another lifecycle hook is not required for this specific source path.

The seven paid mission starts guard the relevant existing slot inside the cost-bearing complete_effect before their first manual debit: response-cell containment and security-surge containment guard slot 1; transport guards slot 1; corridor and capital guard slot 2; retake and restoration guard slot 3.

The accepted foreign-target behavior remains intact: transport, capital, and restoration use current control where specified, while retake may target an externally claimed/core state controlled by an actor.

## Receiver and lifecycle contract matrix

| Mission | Receiver at activation | Target binding and slot | Owner-local source review |
| --- | --- | --- | --- |
| random_terror_contain_attack_wave | Government decision ROOT; two direct setup callers | Exact selected state suffixed for ROOT; slot 1 | Family guard and receipt-scoped callbacks present |
| random_terror_protect_transport_network | Government decision ROOT | Exact controlled target, foreign ownership remains possible; slot 1 | ROOT receipt; callbacks retain the control predicate only where the objective uses it |
| random_terror_break_cross_border_corridor | Government decision ROOT | Exact selected controlled state; slot 2 | ROOT receipt; no foreign controller becomes the mission receiver |
| random_terror_prevent_capital_seizure | Government decision ROOT | Exact currently controlled capital, foreign ownership remains possible; slot 2 | ROOT receipt and capital target variable |
| random_terror_retake_lost_state | Government decision ROOT | Exact external claimed/core target; slot 3 | ROOT receipt; no owner-equals-ROOT restriction |
| random_terror_restore_civil_authority | Government decision ROOT | Exact controlled recovery state; slot 3 | ROOT receipt; starter slot reservation precedes helper and activation |
| random_terror_hostage_deadline | Target state CONTROLLER at incident time | Saved incident state; slot 1; setup suffix is @PREV from the nested state scope | Controller country owns slot, family flag, and pointer; callbacks resolve under that owner’s ROOT |
| random_terror_stop_coordinated_uprising | Target state CONTROLLER before pressure/state transfer | Saved uprising state; slot 2; defender is bound before transfer; setup suffix is @PREV | Actor, state owner, controller, and receiver remain distinct; callback ROOT is the bound receiver |

All eight use random_terror_government_response_category, selectable_mission = no, fire_only_once = no, is_good = no, and a scripted timeout constant.

The matrix’s region, duration tuning values, exact objective balance, cost/resource counts, equipment or unit adequacy, and duplicate balance are not fully audited here; the current review is limited to ownership and transaction behavior.

## Receipt keys, family locks, and player-facing tooltips

The eight subject receipts are random_terror_containment_mission_subject, random_terror_transport_mission_subject, random_terror_corridor_mission_subject, random_terror_capital_mission_subject, random_terror_retake_mission_subject, random_terror_restore_civil_authority_subject, random_terror_hostage_mission_subject, and random_terror_uprising_subject.

Direct country starts and callbacks use @ROOT; only the nested hostage and uprising setup writes use @PREV to capture the actual receiving controller.

The eleven receiver-keyed progress/commitment fields are random_terror_containment_success, random_terror_transport_protection_success, random_terror_transport_protection_committed, random_terror_support_disruption_success, random_terror_support_disruption_committed, random_terror_capital_security_success, random_terror_retake_commitment_active, random_terror_civil_authority_restored, random_terror_hostages_recovered, random_terror_hostage_crisis_resolved, and random_terror_uprising_stopped.

The eight corresponding country family locks are random_terror_mission_active_containment, random_terror_mission_active_transport, random_terror_mission_active_corridor, random_terror_mission_active_capital, random_terror_mission_active_retake, random_terror_mission_active_restore, random_terror_mission_active_hostage, and random_terror_mission_active_uprising.

The reviewed hostage correction is present: the negative hostage-family-active check is in the country-level cancel_trigger OR; the available state-level OR contains only the two receiver-keyed hostage progress receipts.

Each objective uses a matching *_objective_tt through custom_trigger_tooltip, and the English file aliases that key to a target-name description; each mission has success and failure text, while hostage has no partial tooltip because no partial branch exists.

The offline Triggers reference says custom_trigger_tooltip hides its nested trigger conditions and substitutes its localisation; the installed documentation confirms the trigger is supported in any scope, so these private state/country flag names are not exposed by the reviewed objective gate.

## MCP and source evidence

hoi4.decision_inspect without declared scenarios returned the exact input error that inspect mode requires scenarios.

Two narrow retries for hostage and restoration with one declared minimal source-audit scenario returned DECISION_ANALYZED_PARTIAL, status = ok, sourceRevision = 48b26d10e7b925af6775a92d52d2e810ec972b1916c7e6dfab228c62d9b2e686, 7,949 indexed decisions, 1,972 categories, 218 unresolved definitions, and an incomplete decision-coverage validation.

The partial hostage artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fb232426a15e443a5a507b7bfb072c16ceba6312501d647730ae4161c47e1e95/16fb222b555554a1b30d9dcf161f3cd511280dccacc6cd6c1b50f6455a128077/decision-db93ba1e6a17cda0b032eda2.json; the partial restoration artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0a0c85cb01bf215105f8f1a926207b1d4e9923bd987e58f7795cdf21c2b4a648/4055e968e2b1d30d77903d8da4316626b7321c2e7914108a86504a4ffebf5062/decision-f5fe90c1eba5ef456acedb9d.json.

Those artifacts are broad partial inventories with unbound scenario state; they do not prove A/B runtime isolation, callback execution, or state-transfer behavior.

hoi4.source_lookup successfully returned random_terror_close_country_recovery from mod:common/scripted_effects/031_random_terror_effects.txt:4352-4381 and the owner cleanup definitions; source lookup revisions changed between calls, so the four current file hashes above are the source identity for this review.

The successful detailed references read were installed effects_documentation.md:661-670 for activate_mission at revision 2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af; offline Scopes - Hearts of Iron 4 Wiki.md:811-872 and :245-266 at revision 18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49; offline Data structures - Hearts of Iron 4 Wiki.md:102-126 at revision 62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4; offline Decision modding - Hearts of Iron 4 Wiki.md:465-479 at revision 7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162; offline Triggers - Hearts of Iron 4 Wiki.md:329-403 at revision abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06; and installed triggers_documentation.md:2482-2489 at revision 7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29.

The decision context bundle was limited to two sources and reported five omitted source groups; targeted searches and detailed reads covered the flag suffix, mission activation, PREV scope, and tooltip rules cited above.

The named parent reference-refresh handoff records a separate failed write route to docs\plans\031_random_terror_plans\031_random_terror_mcp_evidence.md; this review did not retry or alter that canonical ledger.

## Validation limits and parent follow-up

Meaningful read-only validation performed: reviewed the current mission definitions and all 24 callback contexts, traced the seven paid starter guards and restoration helper ordering, inspected owner-local and global cleanup source, scanned active uses of the unkeyed receipt-name bases, checked the exact four SHA-256 hashes, and obtained partial decision-inspect plus successful targeted reference/source lookups.

Not performed: native gameplay scenarios, save/load testing, tests, cost-count/texticon audit, unit/resource adequacy review, mission balance evaluation, probability comparison, or GUI inspection/rendering.

Numeric AI comparison remains with the parent and chaosx_ai_probability_auditor; the earlier mission-owner baseline reports all 208 candidate-scenario instances unresolved and requires the same named scenario set for any after comparison.

Before commit, the parent should disposition the five self-blocked success receipts, hostage slot deadlock/partial result, transfer-specific cancellation policy, and the generic civil-authority flag’s achievement meaning; exact costs, resource/unit amounts, and numeric AI comparison remain open.

## Changed files, ids, and skills

Only this new handoff was created: docs\plans\031_random_terror_plans\subagent_handoffs\031_mission_receiver_isolation_review_20261004.md.

No gameplay ids, localisation keys, weights, helper definitions, or source files were changed by this reviewer.

The reviewed mission ids are random_terror_contain_attack_wave, random_terror_protect_transport_network, random_terror_break_cross_border_corridor, random_terror_prevent_capital_seizure, random_terror_retake_lost_state, random_terror_restore_civil_authority, random_terror_hostage_deadline, and random_terror_stop_coordinated_uprising.

The skills used were chaos-redux-subagents and chaos-redux-decisions-missions; no skill file was created or updated.

## Post-review disposition addendum — generic civil-authority fact

Disposition: the prior Medium finding about the unkeyed random_terror_civil_authority_restored achievement fact is repaired within the accepted Event 31 achievement basis.

The accepted basis is docs\specs\031_random_terror_specs\031_random_terror_achievement_prompt.md:187-194, whose final condition says every recaptured state completes Restore Civil Authority.

The current helper random_terror_decision_restore_services at common\scripted_effects\031_random_terror_effects.txt:2271-2284 no longer sets the generic random_terror_civil_authority_restored state flag; it retains only the receiver-keyed transient random_terror_civil_authority_restored_@ROOT receipt at line 2279, which the decision caller clears at common\decisions\031_random_terror_decisions.txt:1714 immediately before activate_mission at line 1715.

The generic physical-state fact is set only in the full-success resolver at common\scripted_effects\031_random_terror_effects.txt:3870, alongside the receiver-keyed success receipt at line 3871 and the accepted achievement-recording call at line 3872.

A scan of current common script source found exactly one unkeyed setter for random_terror_civil_authority_restored, at the full-success resolver line cited above; the achievement criterion consumer remains at common\scripted_effects\031_random_terror_achievement_effects.txt:653.

The current effects SHA-256 is 41DF95B5C1F72D5F464E2A650921B32C3787EA1F250FAFAE56D00877D498CB35; the other three reviewed source hashes remain missions C775B7556270CFFAE07B33C1B8435D50B5990B1C8EA1383654E70C8458A71BD2, decisions 810E8EEC735E2AEDB35571609E1EA070443129C18E3B34ABC1F1F4A13C379236, and English 94203E52F8701E92114EDEE5CD641E2C6D0EFFBAD664F340495FFBF1F20394F1.

The accepted prompt file SHA-256 is D39ED37C0B9BEA17357382B796E17F0C1A04A16631BEF3B95FF9CF6B353E4540.

This addendum supersedes only the Medium unkeyed-fact disposition above; the original review text and its source snapshot table are retained unchanged.

A byte-prefix check matches the pre-addendum handoff SHA-256 0538E99FE058D459CD1FF5E5C5B032007B24CEFE4A02B4D5C35C9A9581246157 after trimming only the separator newline; the original review body remains byte-for-byte intact.

The five success-producer loops and hostage slot deadlock/partial outcome remain open; this fact correction does not resolve them.

No gameplay edit was made by this reviewer; only this handoff was appended.
