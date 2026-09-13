# Event 016 foreign operations active audit and narrow patch

Date: 2026-09-05.

Status: implemented for the two confirmed local P2 presentation defects described below; the working tree remains unstaged and uncommitted.

This handoff is the durable result of the bounded foreign-operations audit requested by the parent agent.

## Ownership and evidence boundary

The owned gameplay surfaces were `common/decisions/016_brilliant_scientist_foreign_decisions.txt`, `common/decisions/016_brilliant_scientist_directorate_foreign.txt`, `common/decisions/categories/016_brilliant_scientist_foreign_categories.txt`, `common/scripted_effects/016_brilliant_scientist_foreign_effects.txt`, `common/scripted_triggers/016_brilliant_scientist_foreign_triggers.txt`, `common/script_constants/016_brilliant_scientist_foreign_constants.txt`, `common/mtth/016_brilliant_scientist_foreign_mtth.txt`, `common/opinion_modifiers/016_brilliant_scientist_foreign_opinion_modifiers.txt`, and `common/scripted_localisation/016_brilliant_scientist_foreign_scripted_localisation.txt`.

The matching localization and documentation surfaces were reviewed, including `localisation/english/016_brilliant_scientist_foreign_l_english.yml`, `localisation/english/016_brilliant_scientist_directorate_l_english.yml`, `docs/events/016_brilliant_scientist/systems/foreign_operations.md`, and `docs/events/016_brilliant_scientist/systems/directorate.md`.

`events/016_brilliant_scientist_foreign_events.txt`, the terminal/on-action callers, the accepted completion contract, prior receipt handoffs, the offline Paradox wiki pages, and the required vanilla documentation were read as read-only references.

No containment, evolution/event source, focus tree, GUI definition, model, biological/Portal/Alien core, or shared catalog file was edited.

The current source files already contain concurrent lifecycle changes for typed receipts, pending responses, history alignment, host reconciliation, and terminal cleanup, so this audit did not rewrite or duplicate those changes.

## Implemented narrow fixes

### Joint-laboratory requirement presentation

Changed `brilliant_scientist_directorate_open_joint_laboratory` in `common/decisions/016_brilliant_scientist_directorate_foreign.txt` so its complex `available` block is wrapped by `custom_trigger_tooltip = { tooltip = brilliant_scientist_joint_laboratory_requirements_tt ... }`.

The hidden trigger preserves the original partner, viable-site, support-equipment, motorized-equipment, and fuel checks exactly, while the player-facing row now receives one readable requirement explanation instead of a raw nested requirement dump.

Added `brilliant_scientist_joint_laboratory_requirements_tt` to `localisation/english/016_brilliant_scientist_directorate_l_english.yml`.

The tooltip uses the existing `brilliant_scientist_directorate_cost.joint_laboratory_support_gate`, `.joint_laboratory_truck_gate`, and `.joint_laboratory_fuel_gate` constants and the existing `£support_equipment_text_icon`, `£GFX_motorized_equipment_text_icon`, and `£GFX_fuel_texticon` texticons.

This is a presentation-only change to the requirement surface and does not alter the four spendable cost types, effect, timer, route, or AI behavior.

### Foreign-operation cost and requirement text

Updated `brilliant_scientist_foreign_protection_requirements_tt`, `brilliant_scientist_foreign_counter_program_requirements_tt`, `brilliant_scientist_foreign_offer_protection_effect_tt`, and `brilliant_scientist_foreign_counter_program_effect_tt` in `localisation/english/016_brilliant_scientist_foreign_l_english.yml`.

Protection support-equipment quantity now comes from `constant:brilliant_scientist_foreign_consequence.protection_host_support_equipment` and uses `£support_equipment_text_icon`.

Counter-program support-equipment quantity now comes from `constant:brilliant_scientist_foreign_cost.counter_program_support_equipment` and uses `£support_equipment_text_icon`.

The counter-program duration and Political Power payment now use `constant:brilliant_scientist_foreign_duration.counter_program_days` and `constant:brilliant_scientist_foreign_cost.counter_program_pp`, with `£pol_power` and `£support_equipment_text_icon` coverage.

No decision cost, effect, requirement trigger, AI weight, route lock, or receipt behavior changed in this localization-only correction.

The foreign localization file also has a concurrent wording change to `brilliant_scientist_foreign_theft_effect_tt` visible in the worktree diff; that wording change was not authored by this audit and is intentionally preserved.

## Severity-ranked findings

### P0 and P1

No confirmed P0 or P1 defect remains in the owned foreign-operation paths.

The current receipt implementation binds delayed callbacks and event options to the fixed expected operation, original actor, original host id, and regular event-target context.

The host-response phase uses `brilliant_scientist_foreign_host_response_pending` separately from `brilliant_scientist_foreign_operation_resolution_recorded`, which correctly permits detected covert responses after resolution and prevents duplicate response mutation.

Actor reports require a matching recorded receipt with no pending host response, and stale or mismatched responses fail closed without settling a newer operation.

### P2 resolved by this audit

The joint-laboratory decision exposed a long nested partner/site/material requirement block without a concise custom tooltip and had four visible resource gates that needed icon-first meaning.

The protection and counter-program foreign tooltips exposed fixed resource wording or omitted the exact dynamic amount and duration, making the spendable requirement less clear than the source constants.

Both defects were local and were fixed without changing the mechanic contract.

### P2 remaining or conditional

Destroyed or annexed participant cleanup remains an engine-ordering limitation rather than a confirmed ordinary-path defect.

The owned foreign effect provides `brilliant_scientist_foreign_cleanup_country_operations`, participant-owned hooks call it from the documented terminal paths, and `brilliant_scientist_foreign_reconcile_incoming_operations` rebuilds only the affected host registry.

The available source and offline documentation do not prove that a native popup whose recipient country has been destroyed can still execute its timeout or retain a usable country scope, so terminal cleanup is not claimed as fully engine-certified.

The foreign category defines eleven operation actions and can expose several of them against one current host at once, but the standard decisions-panel layout is not a dedicated owned GUI surface and no callable GUI inspect/render route was exposed in this runtime.

This is a cognitive-load follow-up risk, not a reason to invent a new category or phase in this bounded patch.

Public challenge has its own public consequence set and records detection, while the generic covert detection surcharge is not applied by `brilliant_scientist_foreign_resolve_public_challenge`.

The source documentation distinguishes public consequences from covert surcharge behavior, so this remains a contract question rather than a confirmed defect and was not changed.

## Decision category lifecycle

`brilliant_scientist_foreign_operations_category` is visible only for an initialized Evolution II foreign actor with an active contest and a current target array.

Each actor receives one current-host target, each targeted decision uses `fire_only_once = yes`, and all route-specific decisions recheck actor readiness and current-host validity.

The eleven foreign actions are observation, formal invitation, assistant recruitment, archive theft, project sabotage, encouraged defection, extraction, protection offer, assassination attempt, counter-program, and public challenge.

Eight actions are timed and use `days_remove`, `cancel_trigger`, `cancel_effect`, and `remove_effect`; invitation, protection, and public challenge open immediate host response events.

The shared start effect owns receipt acquisition, operation type, original host id, project family/stage selection, incoming-slot acquisition, immediate dispatch, and the counter-program support-equipment debit.

The actor live-operation limit is one and the host incoming-operation limit is two.

Cancellation records one cancellation row where the receipt is still unresolved, releases the matching host slot, preserves the one-shot target history, and does not refund preparation.

Covert resolution records the result before opening detected host response events, while immediate diplomacy records only after the host response.

Terminal country cleanup settles the country-owned outgoing receipt and matching incoming actors before context removal; it does not use a world-wide periodic scan.

The directorate foreign category has six liaison actions and no mission definitions.

## Cognitive-load notes

The foreign category has eleven decision definitions, but each actor carries one current host target rather than a wall of duplicated country rows.

Depending on prerequisites, several actions can be visible together, so the source-level category still has a possible greater-than-six primary-action density that should be reviewed if the standard decisions panel proves cluttered in live use.

The directorate foreign category has six liaison actions and no simultaneous mission list.

The foreign category description identifies interest, diplomacy, intelligence access, ideology, relations, project maturity, host security, and prior operations as the causal state behind availability and outcomes.

The operation tooltips identify timing, route consequence, detection, selected family, and host response where applicable.

The joint-laboratory tooltip now explains partner validity, viable site, three material reserves, and the subsequent matching consumption in one readable sentence.

The visible support-equipment, motorized-equipment, fuel, and Political Power amounts changed by this audit are icon-first and constant-backed.

There are no foreign-operation missions to audit for owner, category, region, duration, success, failure, or duplicate risk.

## Mission quality notes

No mission is defined in the owned foreign-operation or directorate-foreign decision surfaces.

Mission lifecycle fields are therefore not applicable to this audit.

## Cost and requirement clarity

Foreign timed and immediate decisions use native Political Power cost plus, for the counter-program only, one support-equipment debit inside the successful start boundary.

The foreign counter-program therefore has two spendable cost types and no hidden fifth cost.

The directorate joint-laboratory decision uses Political Power, support equipment, motorized equipment, and fuel, which is exactly four spendable types and remains within the accepted limit.

The joint-laboratory requirement tooltip uses the same strict `>` gates as the source trigger and the same centralized constants as the decision effect.

The protection tooltip communicates the host support-equipment transfer as a consequence, not as an actor payment.

The counter-program tooltip communicates duration and both consumed resources with `£pol_power` and `£support_equipment_text_icon`.

No literal numeric resource name remains in the four patched cost or requirement strings.

Other event prose still uses ordinary words such as “support equipment” when describing a detachment or a lost stockpile rather than a spendable decision row; those descriptions were not rewritten because they are not cost fields.

## AI validity and route-lock notes

The eleven foreign AI entries in `common/mtth/016_brilliant_scientist_foreign_mtth.txt` are target-aware and factor foreign interest, intelligence, exposure, project state, diplomacy, ideology or hostility, grievance/dependence/capacity, and prior-operation state according to route.

The source review found no AI target that bypasses current-host validity, permanent per-operation history, incoming capacity, actor live-operation capacity, or route-specific access checks.

Assassination requires a hostile route, intelligence service, strategic project threat, and no shared faction; theft and sabotage select distinct eligible family targets; defection and extraction revalidate transfer readiness at resolution.

No AI weight was changed by this audit, so no balance target or normalized probability is invented here.

## Localisation and tooltip gaps

The two patched localization files remain UTF-8 with BOM.

The foreign localization has complete operation names, descriptions, requirement keys, effect keys, project-family selectors, and response/report text for the audited routes.

The directorate localization now includes the joint-laboratory requirement key used by the decision wrapper.

The standard decisions-panel visual presentation remains uninspected because no dedicated owned GUI surface or callable `hoi4.gui_inspect`/`hoi4.gui_render` route was available in this runtime.

No GUI rewrite was requested or performed.

## Cleanup and exploit-risk notes

The current foreign effects clear transient pending, result, transfer, and assassination flags before a new start and clear the live host scope only after final settlement.

`brilliant_scientist_foreign_record_resolution` is guarded by the matching receipt and a not-recorded check, appends aligned actor and host history exactly once, and pads legacy metadata with an invalid sentinel rather than inventing dates or stages.

`brilliant_scientist_foreign_finish_owned_operation` removes only the matching actor from the original host registry, then reconciles the actual unique incoming actors and assassination marker.

The host reconciliation does not clear another actor's live receipt, does not release a second slot from duplicate array entries, and does not erase a different live assassination marker.

The transfer helper revalidates recipient and host state, converts a race into a partial result, and clears transfer-success flags on a non-commit path.

Assassination continuity converts a nominal success into injury for clone, machine, temporal, or extraterrestrial continuity instead of committing an invalid death.

No free-equipment loop, repeated project reward, same-type replay, duplicate host response, war-goal spam, or cooldown bypass was found in the owned paths.

The remaining risk is native engine behavior when a saved event target or country scope is destroyed before the callback can reach the participant-owned cleanup path.

## Mandatory MCP evidence

The representative event trace for `chaosx.nr16.100` was inspected with the read-only event workflow before the MCP surface disappeared.

The result was `EVENT_INSPECTED_PARTIAL`, status `ok`, zero blocking diagnostics, revision `942046ff1db8d3f54fb81ad636fb3755123696d69d77eb5a19bda1bc71156ee1`, and graph hash `288aed3bc4b8b594c98bfd311ecdbbf6bcad98e289f8b54de196a7fbf99c1713`.

The exact trace artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/51a0d2fb0b4ff2eff3df607aa52d176234a76f29b3105070e9c8e4f852392e50/69743821548d10a9bebc604ca86d16080a49e109a5e703d26bd2050af8feabaa/event-trace-942046ff1db8.json`.

The matching read-only event-options render returned `EVENT_RENDERED_PARTIAL` with the same revision and graph hash because helper and lifecycle analysis was deferred for the large workspace.

Its exact manifest is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/40f4d55b7601ff18b2acf3f6ee1226d01bac9d46f4a619d79eb100a703358988/bff3639595fe3e45c38425b5cb073333f12ad5fee7f4ac7495404c3ac93c6eb4/event-options-942046ff1db8-manifest.json`.

The render JSON, SVG, and PNG artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a943c009b7adb8818c808adc9f84eb41de64484e7f62071e6094eb42b33bce54/44f80f7a82e7cbe30d2b4e962611549b52731b44912b97ce2c5cad5da7f3cce5/event-options-942046ff1db8.json`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/60d29e78bf8aca75b29575195780f3aab9b527aafad39d78fbb3801eaf7c6769/41610c62d2c0aa320d1193151e21e8e4ef9e972dda10a0e4e4d12c46303904d9/event-options-942046ff1db8.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e87ec26a5837dc6930b2e1a1b1af0bee4beea0e729d7392dae471734c25a188a/d4d907836913a08bac414029b065f83a7b9aa669b4e7d5851a53924cb4c21ef0/event-options-942046ff1db8.png`.

The terminal selector `chaosx.nr16.190` was also rendered read-only with terminal-focused selection and returned `EVENT_RENDERED_PARTIAL` with no source mutation; the result was limited by the same deferred helper/lifecycle analysis.

The mandatory probability inspection used adapter `decision_ai_will_do`, source identifier `brilliant_scientist_foreign_operations_category`, the exact eleven operation decision IDs, and the named lifecycle fixture.

The current inspect result was `PROBABILITY_SOURCE_INSPECTED` with source revision `9ce7cd4523a4add943f826677c6be8372eb84245c25ce825fdfd29c70d92967a`, source hash `538c761ce7ccf1c00b68e1c2ffd6a716548b8afb04b4b5211c816e054cae7682`, `poolComplete=false`, one discovered candidate, zero available candidates, five required inputs, and ten unresolved candidates.

The exact current probability-inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eeac7ed8d6212de328023148cd52b6e4e1e1916a27afaaea1fe7645b8388e919/92fda4c66b69e9d8b4b8a7cf8a1767d8906f4decee93512c5bca77d7fe9e5486/probability-inspect-538c761ce7cc.json`.

The same named fixture was used for a required probability evaluation attempt after the repository instruction refresh, but the exact blocker was `MCP tool \`hoi4_agent_tools/hoi4.probability_evaluate\` is not available to the model`.

No normalized probability, ranking, or post-patch balance claim is made from the incomplete inspect.

The fixture is `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/E016_FOREIGN_RECEIPT_LIFECYCLE_2026_09_02.scenarios.json` with scenario hash `5d6c32359c2215900683ace57139969c8dd47bd79e67167105cdf483d109c346` and scenarios `E016_FOREIGN_FRIENDLY`, `E016_FOREIGN_NEUTRAL`, `E016_FOREIGN_HOSTILE`, `E016_FOREIGN_INTELLIGENCE_DOMINANT`, `E016_FOREIGN_IDEOLOGY_OPPOSED`, `E016_FOREIGN_REPEATED_TARGET`, `E016_FOREIGN_VALID_LIVE_RESPONSE`, `E016_FOREIGN_EXPIRED_RESPONSE`, `E016_FOREIGN_MISMATCHED_TYPE`, and `E016_FOREIGN_MISMATCHED_HOST`.

The retained prior handoff `016_final_foreign_receipt_probability_2026-09-02.md` records earlier partial inspections and comparisons for the same decision and response pools, including `comparisonChanges=0` on the supported pools, incomplete candidate discovery, unresolved helper/event-target inputs, and no normalized probability.

No `chaosx_ai_probability_auditor` route was callable in this runtime, no decision-specific inspect route was exposed beyond the probability adapter, and the probability service disappeared before the required evaluate/compare rerun.

No GUI MCP evidence is claimed for the standard decisions panel because the current runtime exposed neither a dedicated owned GUI surface nor callable GUI inspect/render endpoints.

## Local validation

The two edited localization files begin with the required UTF-8 BOM bytes `EF BB BF`.

Targeted search confirmed the new joint-laboratory tooltip key is referenced by the decision and defined in directorate localization.

Targeted search confirmed the patched protection and counter-program requirement/effect strings use the expected texticons and constant paths.

`git diff --check` was clean for the edited decision and localization files; Git emitted only its existing LF-to-CRLF normalization warnings.

No game was launched and no logs were requested because live gameplay validation belongs to the user.

## Remaining issues, simplifications, and recommended follow-up

No mechanic was simplified, no route was removed, and no fallback was introduced.

The standard decisions-panel action-density question remains unverified and should be checked by the parent or user in the live game if the eleven-operation category presents more than six simultaneous primary rows.

The destroyed-country native-popup ordering and saved-scope behavior remain engine-level acceptance questions; any future fix must preserve typed result history and settle matching transfer, extraction, and assassination receipts before removing stale host-array entries.

The public-challenge detection-surcharge wording remains a contract decision for the owner; do not add the covert surcharge without accepting that it is intended for the public route.

If the HOI4 MCP service returns, rerun probability inspect and evaluate with the exact fixture and candidate pool, then use the same named scenarios for any AI-weight patch comparison.

## Changed-file and commit disposition

Gameplay/localization changes from this audit are limited to `common/decisions/016_brilliant_scientist_directorate_foreign.txt`, `localisation/english/016_brilliant_scientist_foreign_l_english.yml`, and `localisation/english/016_brilliant_scientist_directorate_l_english.yml`.

The durable handoff is this file at `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_final_foreign_operations_active_audit_2026-09-05.md`.

No source or documentation file was staged or committed by this audit.
