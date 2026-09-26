# IW-040/KUB bounded decision and mission audit

**Status:** Read-only audit of the current working tree on 2026-09-26. No gameplay or localisation source was edited, no tests were added or run, and HOI4 was not launched.

## Scope and acceptance basis

Compared the IW-040/KUB founding cycle and paid-focus integration with Part 3’s founding-mission and decision-family design, Part 5’s Level 2 package requirement/status, the accepted IW-040 section in Part 4, the KUB improvement addendum, and the KUB package reference.

The current working tree has pending changes against HEAD in the scoped decision, trigger, effect, and focus files. Findings below describe that working-tree version; the scoped diff adds mission-phase gates, paid receipts, and companion handling while leaving the established payment helpers, project durations, route callbacks, cancel triggers, and failure effects intact. Other pending workspace changes were outside this audit and were not reviewed or touched.

## Findings, sorted by severity

1. **High — mandatory AI/probability evidence is incomplete.** The required read-only `chaosx_ai_probability_auditor` route returned inspections but no named scenario evaluation, sweep, or rendered analysis before this audit was wrapped. The decision adapter `decision_ai_will_do` returned `PROBABILITY_SOURCE_DISCOVERED` with zero candidates and suggested `mission_ai_will_do`; that adapter found 23 candidates, `poolComplete=false`, 19 required input types, and `selectionRule=score_only`. No scenario IDs, rankings, weight traces, `hoi4.probability_evaluate`, `hoi4.probability_sweep`, or `hoi4.probability_render` results were returned. Do not treat the source review as balance evidence or these scores as click probabilities.

   Decision inspection revision: `76d3ce2f0069a66871046125b595f130cb5eaf14a10d2eccf0689cbf1389445d`; source hash: `f678c9a236daab7488f7af1634e2bc18a927bc549bcd2e8269b79c923e1f8254`; [mission-weight inspection artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6c85b7bf7597ac11f44a8b68a85d78b14ddeaf74ca6c88d4ad8739fe9231074b/babeef82f8fba573207b74107e9314dd10a5041ace2c3a6eacc1354f3eee1cf7/probability-inspect-f678c9a236da.json). The first decision-adapter discovery was revision `8d6599deaa9bf85f56be27ac67bff09596107e3f1386b949944d30026fb6f07c`, with the same source hash; [artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5b83035ef9f69ea187e3c4ffa46a6e6b79bac44ccdab6381aef002d4e4ec0b25/0b4075c3e89f7ee825bb07e1ea238755b5233eba84e6643a7cd64dc4c56411aa/probability-inspect-f678c9a236da.json). The five-focus source inspection found 184 candidates, `poolComplete=false`, 17 required inputs, and no candidate examples; revision `7d912b23eb5439a30153ba3f36985c2589a70fe99efb9f51c90159ed65321f3f`, source hash `4c4d2a35e6897758371f2332c04835794838e71e60ae5f558492c485f633d283`; [artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/abb532015a55e51c352502fc10fc57fb6986bb1abd5e899feeaa2eb2ffc10f7e/c7616df422aa38440bc6987f3e3ea6733a87667f6b0a1e006d9708b18c4bc48f/probability-inspect-4c4d2a35e689.json). The MCP probability tools were exposed; the unresolved item is the missing scenario analysis result, not a confirmed service outage.

2. **Medium — three cost strings show four inline values.** `independence_wave_cost_security_standard` (Integrate the Border Guards), `independence_wave_cost_security_major` (Mounted Emergency Command), and `independence_wave_kub_cost_strategic` (Codify Durable Sovereignty) each display four cost entries inline, exceeding the decisions skill’s three-value inline presentation limit. Each action remains within the hard four-cost-type ceiling, and every displayed value has a matching icon. The actual decision-row wrapping was not rendered, so no visual fit claim is made. A future text-only correction should keep the complete payment explicit in the cost tooltip and preserve the current payment mechanics.

3. **Low — source provenance comment is stale.** The KUB category block in `common/decisions/006_independence_wave_frontier_decisions.txt` is bracketed by a comment naming `common/decisions/006_independence_wave_kuban_decisions.txt`, but no such separate file exists in the current tree. The live definitions are in the frontier file. This does not change behavior, but can misdirect later source review.

## Mission and category lifecycle

| Mission | Owner / category | Region | Requirement and duration | Success / failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- |
| `independence_wave_kub_hold_mounted_compact_together` | KUB / `independence_wave_kub_mounted_compact_category` | State 234, Krasnodar; setup also requires it as capital | Auto-activated for IW-040 setup and unresolved state; 600 days. Success requires Civic Concord and Mounted Readiness each at the stable threshold, one selected government, ownership and control of state 234, and capital control. | Its success branch in `cancel_effect` sets `independence_wave_kub_compact_crisis_resolved`. Timeout marks failure and applies the existing project-failure effects. Loss of package/setup, state 234, or capital control cancels into the failure path. | One mission ID; no parallel KUB founding mission was found. |

The 600-day value comes from `constant:independence_wave_kuban_duration.founding_crisis` (600). The stable threshold is the shared KUB pressure constant (60 in the accepted package reference and category text). `has_stable_independence_wave_kub_compact` checks both ledgers at that threshold. The mission remains non-selectable and does not auto-complete through `available`; its completion condition is deliberately handled by the cancellation success branch.

During the active unresolved mission, the four government choices are the only visible primary decision actions. Their shared gate requires the exact KUB package, completed IW-040 setup, the active founding mission, and neither resolved nor failed state. Their availability additionally requires the matching route, capital control, affordability, no selected government, and no other government-choice decision active. The serialization helper uses `has_decision` on all four choice IDs. Installed vanilla trigger documentation defines `has_decision` as checking a country’s “active selected decision,” matching the running timer state needed here.

The other six projects use `is_independence_wave_kub_project_ready`, which requires the resolved flag and excludes failure. Thus they remain hidden before success. After success the category exposes no more than six ordinary projects, at the hard action cap. One project at a time is enforced by `has_independence_wave_kub_active_package_project`. Mission and project counts do not create a wall of simultaneous actions.

## Government and project behavior

The four government choices preserve their current costs, durations, route gates, success callbacks, cancel triggers, and failure calls:

| Decision | Existing cost types | Duration | Success route callback |
| --- | --- | ---: | --- |
| `independence_wave_kub_ratify_constitutional_autonomy` | Command power, manpower, civilian-factory use | 75 days | `independence_wave_install_kub_constitutional_government` plus administrative progress |
| `independence_wave_kub_adopt_agrarian_compact` | Command power, convoy **or** train | 180 days | `independence_wave_install_kub_agrarian_government` plus diplomatic progress |
| `independence_wave_kub_convene_socialist_councils` | Command power, manpower, civilian-factory use | 75 days | `independence_wave_install_kub_socialist_government` plus administrative progress |
| `independence_wave_kub_establish_mounted_emergency_command` | Manpower, army XP, infantry equipment, support equipment | 120 days | `independence_wave_install_kub_emergency_government` plus security progress |

Current shared cost constants are 10 command power/2,500 manpower for light administration; 20 command power plus 10 convoys or 10 trains for standard diplomacy; and 10,000 manpower/35 army XP/1,000 infantry equipment/200 support equipment for major security. One civilian factory is tied up by the relevant administration modifier; it is not an additional stockpile debit. No route exceeds four spendable or committed types.

The six post-resolution projects are: Secure the Mounted Depots (3 types, 75 days), Integrate the Border Guards (4 types, 120 days), Register the Community Compacts (3 types, 120 days), Settle the Former Host Ledgers (command power plus convoy/train alternative, 180 days), Codify Durable Sovereignty (4 types, 300 days), and Open the Black Sea Steppe Network Corridor (command power plus convoy/train alternative, 180 days). Requirements such as capital control, route membership, founding settlement, and stable ledgers are separate from consumed costs.

The scoped diff confirms that only visibility/availability gates and the two paid-project success wrappers were changed. The four government choices retain their original payment calls, timer constants, route helpers, cancellation conditions, and `independence_wave_kub_apply_project_failure` call. The six ordinary project gates still require successful mission resolution.

## Paid-focus receipt and reward audit

- `independence_wave_kub_integrate_border_guards` and `independence_wave_kub_register_community_compacts` pay in `complete_effect`; their project-paid flags are absent there. Each successful `remove_effect` calls the original idempotent callback first, then sets only its matching receipt, then awards its companion if the corresponding branch focus is complete.
- The decision visibility checks now use `independence_wave_kub_border_guards_project_paid` and `independence_wave_kub_community_compacts_project_paid`, not `independence_wave_kub_guards_integrated` or `independence_wave_kub_communities_guaranteed`. A prior generic-focus callback therefore does not hide an unpaid project.
- Focus-first order applies the branch reward; its companion helper does nothing until the paid receipt exists. On later project success, the receipt is set after the old callback and the helper awards the companion once. Project-first order sets the receipt and later awards the companion from the branch focus. Each helper checks its receipt and a one-time companion marker.
- No receipt is published on preview, project start, cancellation, or founding-mission timeout. The two markers clear on KUB setup and cleanup. Existing generic callback flags guard their original effects; the project-failure helper is idempotent. Full-framework focus assignment resets the companion markers alongside focus-history reset. No free or repeatable companion reward path was found.
- The docket focus requires its matching completed branch and paid receipt. It cannot be unlocked by the generic callback flag alone.

## Cognitive load, costs, localisation, and AI

The category description labels both values, shows each against the 0–100 maximum, and states that both must reach the stable threshold. The mission description names the 600-day window, government selection, both values, and state 234 control/ownership. Focus and project tooltips describe the ledger effects and the conditional stability transition. The player-facing values have clear significance and an actionable threshold; no unexplained number dump was found.

Cost text uses the appropriate icons for command power, manpower, civilian-factory use, army XP, infantry equipment, support equipment, stability, convoys, and trains. Diplomatic transport localisation selects convoy or train text dynamically. No literal resource-name fallback or hidden fifth cost was found. The factory-use tooltip repeats the icon string and does not explicitly say that the factory is committed for the timer’s duration; this is a minor clarity point, not a cost/payment mismatch.

Decision AI weights are present in source, including the mission’s urgent base weight, fixed category weights, and war/host-threat modifiers on some decisions. The focus addendum’s route-aware AI intent and deadline feasibility remain unresolved, and the five KUB focus nodes do not provide a probability-validated route preference. Do not infer campaign choice probabilities from `ai_will_do` scores. No numeric weight changes were made or recommended by this audit.

No KUB-specific scripted GUI is attached to the ordinary decision category in the inspected source; the accepted package reference specifies no dedicated GUI. The scripted-GUI MCP route was therefore not used. Native decision-row wrapping and the four-entry cost render remain unverified.

## Cleanup and exploit risks

KUB cleanup removes the mission and all ten KUB project decisions, clears the two payment receipts and the generic callback flags, clears both ledgers and route/lifecycle flags, and restores package-owned politics/identity state. The project-failure effect applies its penalty once. Focus companion markers are reset by the full-framework focus assignment that reloads focus history; KUB setup clears the paid receipts before that assignment. No repeatable or unpaid reward path was found in the inspected callers.

## Files and references inspected

- Repository instructions and skills: `AGENTS.md`; `.agents/skills/chaos-redux-decisions-missions/SKILL.md`; `.agents/skills/chaos-redux-subagents/SKILL.md`; `.agents/skills/chaos-redux-scripted-gui/SKILL.md`.
- Offline wiki: Decision modding, Event modding, Effects, Triggers, Scopes, Localisation, Data structures, Modifiers, On actions, Idea modding, and AI modding.
- Installed vanilla documentation: `documentation/triggers_documentation.md` (`has_decision`, `has_active_mission`, `controls_state`, `owns_state`) and `documentation/effects_documentation.md` (`activate_mission`, `remove_mission`, country flag effects).
- Accepted design: Part 3, Part 4 accepted IW-040 section, Part 5, `006_event6_reg04_kuban_focus_group_improvement_addendum_2026-09-26.md`, and `docs/events/006_independence_wave/kuban_package.md`.
- Gameplay/localisation source: `common/decisions/006_independence_wave_frontier_decisions.txt`; `common/scripted_triggers/006_independence_wave_kuban_package_triggers.txt`; `common/scripted_effects/006_independence_wave_kuban_package_effects.txt`; `common/scripted_effects/006_independence_wave_decision_effects.txt`; `common/scripted_triggers/006_independence_wave_decision_triggers.txt`; `common/script_constants/006_independence_wave_constants_registry.txt`; `common/national_focus/006_independence_wave_focus.txt`; `common/scripted_effects/006_independence_wave_focus_effects.txt`; `common/scripted_localisation/006_independence_wave_scripted_localisation_registry.txt`; `localisation/english/006_independence_wave_frontier_l_english.yml`; `localisation/english/006_independence_wave_decisions_l_english.yml`.
- `common/scripted_effects/006_independence_wave_kuban_package_decision_effects.txt` was checked and is absent; the relevant KUB helpers are in `006_independence_wave_kuban_package_effects.txt`.

## Validation limits and follow-up

Static review compared the current KUB working-tree diff, helper call order, constants, and localisation against the accepted sources. No tests or live-game checks were run per instruction. The required probability workflow did not reach scenario evaluation/sweep/render, so AI validity, deadline feasibility, and quantitative balance remain unresolved. The probability inspector also returned an incomplete candidate pool and unresolved external inputs. No decision-row visual render was captured. Complete the named-scenario probability pass before drawing balance conclusions or changing any numeric weight.

**Skills used:** `chaos-redux-decisions-missions`, `chaos-redux-subagents`, and `chaos-redux-scripted-gui`. No skill was created or updated.

## Parent integration (2026-09-26)

The parent compacted the flagged inline cost rows to at most three values while keeping the full payment explicit in the corresponding cost tooltip. The shared security-standard and security-major strings still show all four costs in their full tooltips; their inline rows now show Army XP and the two equipment types. The KUB strategic row now displays stability, command power, and its convoy/train alternative inline, with the civilian-factory commitment and project duration in the full tooltip. The shared security keys serve KUR and KUB decisions, so the display correction applies to each current caller. Affordability triggers, amounts, payments, and durations are unchanged.

No native decision-row render was produced; actual row wrapping remains unverified. The required typed probability scenario evaluation and deadline/balance evidence also remain unresolved.

## Parent integration (2026-09-26)

The three inline cost labels flagged in this audit now show at most three values: the shared security-standard and security-major rows show Army XP, infantry equipment, and support equipment inline; their full tooltips list all four resources including manpower. The KUB strategic row shows stability, command power, and the convoy/train alternative inline; its full tooltip names the civilian factory commitment and project duration. The security cost keys are shared by KUR and KUB decisions, so this compact display applies to all callers. Payment helpers, affordability triggers, and cost amounts were not changed. The native decision-row render remains unverified, so actual fit is not claimed.
