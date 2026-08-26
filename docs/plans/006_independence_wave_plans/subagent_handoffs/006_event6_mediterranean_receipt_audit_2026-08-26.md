# Event 006 Mediterranean founding-mission setup-receipt audit

Date: 2026-08-26

## Scope and verdict

This bounded audit covers the Corsica, Sardinia, and Sicily founding missions in common/decisions/006_independence_wave_mediterranean_decisions.txt, their package setup effects, and the three Form-05 preparation projects in the same file.

Before the patch, all three founding missions required their package setup receipt in activation, but their cancel_trigger blocks did not cancel when that receipt disappeared during a setup retry or failed preparation.

The narrow source repair is complete for all three missions: each cancellation OR now includes NOT = { has_country_flag = <matching_setup_receipt> }.

No cost, AI-weight, admission, route, balance, localisation, Form-05, or unrelated mission logic changed.

The whole Event 006 implementation remains HOLD / PARTIAL under the current source-of-truth map.

## Issue list, sorted by severity

1. High, resolved: independence_wave_cor_hold_island_supply_together, independence_wave_arx_hold_island_authority_together, and independence_wave_asx_hold_port_authority_together could remain active after their setup receipt was cleared because the matching receipt-loss cancellation branch was absent.
2. No remaining confirmed source omission in the three founding mission blocks: activation, setup clear/restore, cancellation, timeout, success, and failure paths now agree.
3. Evidence blocker: the specialized chaosx_ai_probability_auditor route is not exposed in the current runtime tool list, so its mandated subagent route could not be invoked; direct hoi4_probability_inspect evidence is recorded below and is not treated as equivalent.

## Changed source and identifiers

- common/decisions/006_independence_wave_mediterranean_decisions.txt:27 — independence_wave_cor_hold_island_supply_together.cancel_trigger now tests absence of independence_wave_iw_017_setup_complete.
- common/decisions/006_independence_wave_mediterranean_decisions.txt:170 — independence_wave_arx_hold_island_authority_together.cancel_trigger now tests absence of independence_wave_iw_018_setup_complete.
- common/decisions/006_independence_wave_mediterranean_decisions.txt:309 — independence_wave_asx_hold_port_authority_together.cancel_trigger now tests absence of independence_wave_iw_019_setup_complete.
- docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_mediterranean_receipt_audit_2026-08-26.md — this handoff.

The gameplay diff is exactly three one-line trigger additions.

## Decision-category lifecycle notes

| Package/category | Founding mission contract | Setup receipt lifecycle | Cancellation and terminal behavior |
| --- | --- | --- | --- |
| IW-017 COR / independence_wave_cor_corsica_category | Activation requires is_independence_wave_cor_package, independence_wave_iw_017_setup_complete, and neither resolved nor failed crisis flag. | independence_wave_setup_iw_017_corsica clears the receipt at :733 before setup work and restores it only inside has_prepared_independence_wave_iw_017_package_setup = yes at :774-775. | :27 cancels on package loss, receipt loss, stable maritime access, or capital loss; stable access resolves, while receipt loss and other non-stable cancellation take the existing failure helper. Timeout at :32 fails the package. |
| IW-018 ARX / independence_wave_arx_sardinia_category | Activation requires is_independence_wave_arx_package, independence_wave_iw_018_setup_complete, and neither resolved nor failed crisis flag. | independence_wave_setup_iw_018_sardinia clears the receipt at :784 before setup work and restores it only inside has_prepared_independence_wave_iw_018_package_setup = yes at :824-825. | :170 cancels on package loss, receipt loss, stable civic cohesion, or capital loss; stable cohesion resolves, while receipt loss and other non-stable cancellation take the existing failure helper. Timeout at :172 fails the package. |
| IW-019 ASX / independence_wave_asx_sicily_category | Activation requires is_independence_wave_asx_package, independence_wave_iw_019_setup_complete, and neither resolved nor failed crisis flag. | independence_wave_setup_iw_019_sicily clears the receipt at :834 before setup work and restores it only inside has_prepared_independence_wave_iw_019_package_setup = yes at :874-875. | :309 cancels on package loss, receipt loss, stable port authority, or capital loss; stable authority resolves, while receipt loss and other non-stable cancellation take the existing failure helper. Timeout at :311 fails the package. |

The package-specific prepared predicates remain in common/scripted_triggers/006_independence_wave_mediterranean_package_triggers.txt:202, :261, and :320; each complete predicate continues to require the common setup receipt and its package-specific receipt at :379, :391, and :403.

The Form-05 preparation decisions at :144-159, :283-298, and :452-467 are ordinary timed projects with days_remove, not founding missions with days_mission_timeout. Their existing cancellation checks for prospective carrier and connected core partner remain unchanged because this audit's receipt contract applies to the package founding mission blocks.

## Cognitive-load notes

- Each package exposes one automatic founding mission with available = { always = no }; the repair does not add a player action, category, tab, or visible value.
- The existing project queues remain serialized by the package-specific active-project predicates; no simultaneous-mission or action-density behavior changed.
- Existing package values such as maritime access, civic cohesion, and port authority retain their existing scripted descriptions and stable thresholds; the receipt guard only governs lifecycle validity.
- The three Form-05 project entries retain their existing concise names, descriptions, requirements, and strategic-cost presentation; no new explanatory prose was introduced.
- The setup receipt now has an unambiguous significance: it means the current package generation passed preparation, and losing it cancels the founding mission.

## Mission-quality notes

| Mission | Owner and category | Region and requirement | Duration | Success | Failure and duplicate risk |
| --- | --- | --- | --- | --- | --- |
| independence_wave_cor_hold_island_supply_together | COR package / Corsica category | Mediterranean island package; package identity, IW-017 setup receipt, unresolved and unfailed founding crisis, stable maritime access or capital control during the mission. | constant:independence_wave_mediterranean_duration.founding_mission_days at :26. | Existing cancellation effect resolves when stable maritime access is present. | Receipt loss, package loss, or capital loss reaches the existing failure path; timeout at :32 fails. Resolved/failed flags and package cleanup prevent duplicate founding missions. |
| independence_wave_arx_hold_island_authority_together | ARX package / Sardinia category | Mediterranean island package; package identity, IW-018 setup receipt, unresolved and unfailed founding crisis, stable civic cohesion or capital control during the mission. | Shared founding-mission constant at :169. | Existing cancellation effect resolves when stable civic cohesion is present. | Receipt loss, package loss, or capital loss reaches the existing failure path; timeout at :172 fails. Resolved/failed flags and package cleanup prevent duplicate founding missions. |
| independence_wave_asx_hold_port_authority_together | ASX package / Sicily category | Mediterranean island package; package identity, IW-019 setup receipt, unresolved and unfailed founding crisis, stable port authority or capital control during the mission. | Shared founding-mission constant at :308. | Existing cancellation effect resolves when stable port authority is present. | Receipt loss, package loss, or capital loss reaches the existing failure path; timeout at :311 fails. Resolved/failed flags and package cleanup prevent duplicate founding missions. |

## Cost and requirement clarity

The three founding missions have zero spendable cost types because they are automatic missions with available = { always = no } and no custom_cost_text or payment effect.

The three Form-05 preparation projects each retain one strategic cost localisation key, independence_wave_cost_strategic, and were not changed.

The unchanged strategic cost uses texticons for stability, command power, civilian factories, and the dynamic convoy/train branch: localisation/english/006_independence_wave_decisions_l_english.yml:31-33,52 and common/scripted_localisation/006_independence_wave_scripted_localisation_registry.txt:225-234.

No decision or gameplay-changing GUI action in this patch introduces more than four spendable cost types, and no literal resource label was added.

## AI validity and route-lock notes

All three founding missions retain ai_will_do = { base = constant:independence_wave_decision_ai.urgent }; no weight or target-selection logic changed.

The package identity and stable-value scripted triggers remain the existing route locks, with no new country target or border assumption.

Read-only MCP probability inspection was run against the current decision source with adapter mission_ai_will_do.

Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/901707a09388da5253d10923d8134ce6c8d6d89e6ac2cb844508dd7fe6b62ab3/72f134710c7d6e9787c1152871edf5001b045715194a49fc42a0d6980a9b636b/probability-inspect-86b793ff0f40.json.

The MCP receipt reports source revision 7378fff1bc4a086c1027c2fe8810e0117aaf860950140fed3177d9a69a16946c, source hash 86b793ff0f4049a4c68b4e00052a147b26f27b6d2ea7932ecfa5189093318c81, 29 candidates, zero scenario-free available candidates, 53 required inputs, zero unresolved parser inputs, and poolComplete = false.

Because this patch does not modify any AI weight, no probability compare, sweep, or balance target change was performed.

## Localisation and tooltip gaps

No localisation keys changed or were added.

Existing founding mission descriptions, stable-value requirements, failure custom tooltips, and timeout effects remain wired to their prior identifiers.

No GUI surface is introduced or changed, so hoi4.gui_inspect and hoi4.gui_render are not applicable to this bounded source patch.

## Cleanup and exploit-risk notes

When a setup retry clears a package receipt, the corresponding active founding mission now cancels through its existing cancel_effect; package identity loss, stable success, capital loss, and timeout retain their prior branches.

The repair closes a stale-mission lifecycle gap and does not create a new cost refund, free-unit loop, equipment loop, war-goal loop, formable loop, or cooldown path.

Package cleanup already removes these missions at common/scripted_effects/006_independence_wave_mediterranean_package_effects.txt:906, :968, and :1018, with matching receipt cleanup at :919, :981, and :1033.

## Validation

Focused PowerShell source assertions passed for all three missions: activation receipt, package guard, exactly one matching cancellation receipt guard, setup clear-before-work, prepared-success-only restore, and clear-before-restore ordering.

The following Event 006 static validators passed on the current checkout:

- python -B .tools/audit_event6_allocator.py — 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, 40 adapters, 32 attestations, and 29 compatible reservation groups.
- python -B .tools/audit_event6_country_api.py — 242 broad rows, 191 unique carriers, zero missing, zero duplicates, and IW-031 crosswalk pass.
- python -B .tools/audit_event6_flags.py --strict — 102 registered tags and 102 complete flag families.
- python -B .tools/audit_event6_form16.py — ARM/GEO/AZR FORM-16 contract pass.
- python -B .tools/audit_event6_scenario_matrix.py — all 32 SCN-008 cells and eight edge-case receipts.

## Skipped meaningful validation and remaining risks

No live Hearts of Iron IV run, save/load test, or runtime mission cancellation test was performed or claimed.

The specialized chaosx_ai_probability_auditor could not be called because it is absent from the available tool list; direct MCP probability inspection is recorded only as partial read-only evidence.

No probability compare was needed because the patch leaves AI weights unchanged, and the inspect artifact explicitly reports an incomplete candidate pool and no normalized selection probability.

No GUI inspection or render was run because this source surface contains no scripted GUI.

No broad plan handoff was written because the confirmed issue was a local three-line guard repair.

Remaining risk is limited to engine/runtime behavior and the existing Event 006 HOLD / PARTIAL evidence boundary; live mission cancellation and save/load persistence remain unproven here.
