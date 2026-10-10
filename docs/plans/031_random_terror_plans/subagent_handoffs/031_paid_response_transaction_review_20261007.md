# Event 31 paid response transaction preflight review

Status: Source-level review is complete for the two paid decision callbacks. The live decision-scenario inspection did not return, so callback and threshold scenarios remain unresolved as MCP evidence.

Scope is limited to `random_terror_security_surge`, `random_terror_targeted_raid`, their two scripted preflight triggers, their cost display and the existing Hostage Deadline interaction. This is not a whole Event 31 completion audit.

## Authority and preserved design

The accepted design references are `docs/specs/031_random_terror_specs/031_random_terror_decision_mission_matrix.md` and `docs/specs/031_random_terror_specs/031_random_terror_decision_mission_prompt.md`, read alongside the parent task instruction. They preserve Event31/rootMinorRepeatChaos1/fiveNames/GlobalJihad#016/#018/FalseRev1000+gates, noInternalFracture, IV-fictional-only opposition, and no changes to identity, recruitment, or target weights.

The task explicitly records that Hostage Deadline partial resolution and emergency Security Surge/Targeted Raid access already exist. This review retains those behaviors and introduces no route, outcome, cost, AI, UI, country, unit, asset, counter, or sound change.

## Severity-ranked findings

1. **P2 - Transaction scenario evidence unresolved.** The exposed `hoi4.decision_inspect` schema was used to submit `mode = inspect` scenarios for `random_terror_security_surge` and `random_terror_targeted_raid`, including exact-cost, below-cost, above-cost, emergency-slot, foreign-owned/root-controlled, changed-controller, wrong-country-receipt, stale-target, actor, action-recent, duplicate-target, and world-end cases. The two calls produced no result, diagnostics, validation object, or artifact after approximately 97 seconds, so the local wait was terminated. This is a delayed or unobserved result, not an explicit MCP error. Source review is not equivalent to those missing scenario results.

2. **P2 - Native rejected-click cooldown remains unverified.** Both decisions set `days_re_enable = constant:random_terror_tuning.decision_action_cooldown_days`, currently 14 days. A false click-time preflight performs no scripted debit or dispatch. Whether the engine still starts its native re-enable timer after that selected decision returns without effects is not established by the documentation or returned MCP evidence. Do not promise a native cooldown refund or cancellation.

3. **P3 - Targeted Raid requirement tooltip omits the accepted emergency route.** `random_terror_targeted_raid_requirements_tt` at `localisation/english/031_terrorist_attack_l_english.yml:360` says the selected state must contain an active or entrenched organization. The emergency branch in `random_terror_can_execute_targeted_raid` also accepts ROOT's own active hostage or uprising mission subject through the receiver-keyed receipt, without the normal active/entrenched-stage test. If the parent includes tooltip cleanup in the reviewed scope, this string should describe both valid routes. No localisation edit was authorized or made here.

No transaction-guard defect was found by source inspection. The required MCP scenario coverage and the existing tooltip issue remain the review limits above.

## Callback and helper audit

`random_terror_can_execute_security_surge` and `random_terror_can_execute_targeted_raid` in `common/scripted_triggers/031_random_terror_triggers.txt:173` and `:198` run in country scope with ROOT as payer and FROM as the exact selected state. Both call `random_terror_can_government_response`, the matching inclusive affordability helper, reject `world_end` and terminal phase, require FROM to remain controlled by ROOT, and require FROM to remain one of ROOT's response targets.

`random_terror_can_government_response` rejects a missing country, an actual nonhuman country, an Event31 actor, and `random_terror_action_recent`. It requires the payer to be affected or to have an active crisis state. The response-target helper admits ROOT's priority state, ROOT's own emergency subject, and the existing response-mission subjects.

The emergency receipt is country-scoped: a hostage subject flag suffixed for ROOT must be paired with ROOT's active Hostage Deadline flag, and an uprising subject suffixed for ROOT must be paired with ROOT's active uprising flag. A state flagged only for another country's mission does not satisfy ROOT's receipt check. The selected state also has to remain controlled by ROOT. Ownership by another country alone does not reject a state that ROOT currently controls.

The regular Security Surge path retains the initial phase, no response cell, no slot-1 mission, active-crisis-stage, and no existing surge-target conditions. Its emergency subject path retains the previously accepted occupied-slot exception. The regular Targeted Raid path retains the initial phase, active response cell, intelligence breakthrough or legitimacy threshold, and active/entrenched target conditions. Its emergency subject path retains the previously accepted own-hostage/uprising access. The raid duplicate-target rejection is outside its branch OR, so it applies to both normal and emergency execution.

In `common/decisions/031_random_terror_decisions.txt`, each `available` custom tooltip calls its corresponding full `can_execute` predicate. Each `complete_effect` uses the same predicate as the outer limit before any debit. The cost row's `custom_cost_trigger` continues to call the matching affordability-only helper, which keeps the resource display independent from non-cost requirements.

Security Surge debits command power, fuel, and support equipment once inside the accepted emergency or regular branch. Targeted Raid debits command power, army experience, and support equipment once inside its guarded effect, then sets its target receipt, dispatches the existing raid helper, and invokes the existing outcome resolver. A rejected preflight has no scripted debit, saved action target, outcome roll, mission dispatch, or custody receipt.

The affordability helpers reject only when a resource is strictly below its quoted constant, so exact equality satisfies the source predicate. The MCP boundary scenarios did not return, so this conclusion is source-level evidence only.

## Costs, requirements, localization, and tooltips

| Decision | Spendable cost types | Current amounts | Display texticons | Cost-key coverage |
| --- | ---: | --- | --- | --- |
| `random_terror_security_surge` | 3 | 10 command power, 35 fuel, 100 support equipment | `£command_power`, `£GFX_fuel_texticon`, `£support_equipment_text_icon` | Base, blocked, and tooltip keys at `localisation/english/031_terrorist_attack_l_english.yml:352-354` |
| `random_terror_targeted_raid` | 3 | 15 command power, 5 army experience, 140 support equipment | `£command_power`, `£army_experience`, `£support_equipment_text_icon` | Base, blocked, and tooltip keys at `localisation/english/031_terrorist_attack_l_english.yml:361-363` |

Each action is below the four-type spendable-cost limit and the three-value inline cost limit. Every spendable amount has its matching texticon. The cost strings do not spell out resource names, add prose between icons, or hide a fourth or fifth payment in the effect tooltip. The displayed amounts and negative debit constants match `common/script_constants/031_random_terror_constants.txt:582-592`.

The Security Surge effect tooltip distinguishes the normal containment mission from the emergency hostage/uprising effect tooltip. The Targeted Raid effect tooltip explains the operation and its risks. The targeted-raid availability requirement string has the emergency-path omission recorded above. No long raw trigger is exposed by the new preflight calls.

## Category lifecycle, cognitive load, missions, AI, and cleanup

The patch adds no category, decision, mission, player-facing value, or scripted GUI. The reviewed pair contributes two visible actions, below the category six-action ceiling, but this count does not audit the full Event31 category. The actions remain targeted to one controlled state at a time in the native decision/map surface. A custom scripted GUI is not part of this scope, so no GUI layout inspection, render, comparison, or UI-worker task applies.

No active mission is added by this guard patch. The emergency path intentionally remains usable while ROOT's own Hostage Deadline occupies slot 1. The existing Hostage Deadline is receiver-owned, targets the selected hostage state, and uses the existing 45-day duration recorded in the frozen baseline. Full recovery resolves through success. Timeout selects the existing partial resolver when the receiver-keyed partial-freed flag is present and otherwise selects failure. Cancellation and terminal paths call the existing cleanup helper. This review did not re-audit other Event31 missions.

No new mechanic value is displayed. The costs are the only additional player-facing resource values within the two actions, and their meaning and payment are explicit in the icon-first custom cost rows. The action descriptions explain the visible purpose. The category-wide value list, mission count, and text density were not re-audited.

The existing `ai_will_do` blocks remain outside the two preflight edits. No weight target or decision priority was changed. The parent-assigned `chaosx_ai_probability_auditor` owns the separate probability comparison, and this handoff does not claim probability evidence or reinterpret willingness scores as click probabilities.

After a successful action, the existing decision effects set the shared 14-day `random_terror_action_recent` lock. `random_terror_can_government_response` blocks another response while that lock is active. Targeted Raid also sets its state target flag before dispatch, and the outcome resolver clears that temporary flag. Hostage and uprising outcomes continue to set their current receiver-keyed success or partial receipts. No new cleanup or repeat-reward path is introduced.

## Before and after behavior

Before the parent patch, the frozen decision callback could debit and dispatch after selection without rerunning the full payer, selected-state, controller, phase, world-end, response-target, and affordability contract. The frozen trigger source contained the shared base and affordability helpers but not these two complete click-time preflights.

After the parent patch, availability and the cost-bearing callback use the same read-only full preflight for each action. A stale callback that fails the preflight has no scripted payment or dispatch. A valid callback retains the previous emergency exception, normal requirements, costs, action effects, AI recipe, outcome logic, and cooldown definitions.

The current source hashes are `common/decisions/031_random_terror_decisions.txt` SHA-256 `47E92D500BC5E0D4A8EBEB7D9292437638C89F718F6004010C35A676C3E4FA2E` and `common/scripted_triggers/031_random_terror_triggers.txt` SHA-256 `179DD12823D4580A14A1D753F6BF7C7ED6154D2392F1D69FFE156174025B54A7`. They match the identities supplied by the parent.

The matching frozen pre-change decision and trigger snapshots are `docs/plans/031_random_terror_plans/evidence/hostage_response_before_20261007/common/decisions/031_random_terror_decisions.txt` SHA-256 `5e75e834953bd21d56c231637211ee25199cc660d81d13c3c29d55a516ef29c0` and `docs/plans/031_random_terror_plans/evidence/hostage_response_before_20261007/common/scripted_triggers/031_random_terror_triggers.txt` SHA-256 `ae57d52a62c3097e5252be8c368a2cca40177332f03d6e46588fe41df04bdd25`. The frozen scenario fixture `docs/plans/031_random_terror_plans/evidence/031_hostage_response_probability_scenarios_20261007.json` has SHA-256 `4e7c90bb68b3c7e54686cc7a82d9e3bb81c71a50245486fa8c1964ac938ee6de`.

## Evidence, validation limits, and handoff

The installed decision documentation was read at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/_documentation.md:16-46`, revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`. It describes `available` as frame-refreshed and the targeted root/target triggers as daily checks.

The offline wiki Decision modding cost section was read at `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md:308-336`, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`. It states custom costs are display-only, must be debited in `complete_effect`, and use the base, blocked, and tooltip localization keys.

The offline wiki state-target section was read at `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md:578-595`, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`. It describes `FROM` as the selected state target. The installed vanilla precedent was read locally at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/AFG.txt:458-512`, SHA-256 `DABC91C3F7FB1810D64D91D07147E827068D42540326CE10554A0752EE48D7A7`.

The parent-provided `hoi4.script_validate` result is `SCRIPT_CHECK_PARTIAL` for seven scripted helpers. Native command kinds and scopes were checked, while helper parameters remain unchecked. No `ROOT` binding was invented for that validator.

`hoi4.source_lookup` calls for the current definitions and AFG precedent were submitted but produced no result before the local wait was terminated. Direct local source inspection and the vanilla file/hash above supplied the cited source evidence. This does not claim an MCP source-lookup result.

No source contract test was added or run. The routed validator did not return executable production-helper coverage, and no flat mock was used as native proof. No game was launched or controlled. No logs were requested or searched. No Git command or gameplay-source edit was made.

The only file changed by this reviewer is this handoff. No decision, mission, scripted-trigger, scripted-GUI, or localization identifier was changed. The parent remains responsible for reviewing the unresolved decision-inspector result and the P3 requirement-tooltip note before making the overall commit or completion claim.
