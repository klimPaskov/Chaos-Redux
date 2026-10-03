# Event 025 Physical Destruction Policy Audit

Date: 2026-10-03

Workspace: C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux

Disposition: unresolved for player-facing cost localization and required AI probability evidence. The bounded source review is complete. No gameplay source was edited.

## Scope and acceptance basis

This review covers the accepted Event 025 specs 005_decisions_missions_and_costs.md, 006_outcomes_rewards_and_aftermath.md, and 014_acceptance_criteria.md, plus the parent source intent in the audit request.

The accepted source intent is sender-owned physical retirement with custody proof, inclusive costs of 50 support equipment and 0.02 stability, a 60 point Dependence reduction, preserved learned technology and reward history, cancellation of only a running Contain Systems project, and no costs, cooldown, policy flags, or Chaos callback when retirement is rejected.

The parent retains ownership of source edits, GUI geometry, broader Event 025 review, balance targets, transfer policy, and the shared worktree commit.

## Findings by severity

1. Evidence blocker for the decision AI score. chaosx_nr25_dependence_destroy has ai_will_do base = 8 at common\decisions\025_alien_technology_in_antarctica_evolution_decisions.txt:226. No source weight changed. The live decision_inspect schema requires declared scenarios. My first request without scenarios returned MCP -32602 with “Decision inspection requires declared scenarios at scenarios.” The parent’s corrected destroy_exact_resources scenario request is still pending and has not returned analysis. probability_inspect is callable by schema, but both my scoped request and narrower source-plus-adapter retry remained pending for over two minutes and were stopped without a result. No probability evaluation, sweep, comparison, or rendering result exists.

   The prior handoff at docs\plans\025_alien_technology_in_antarctica_plans\subagent_handoffs\025_reward_probability_baseline_20261003.md remains blocked. It audits the Event 016 external reward API custom pool, so it does not establish scenario evidence for this decision’s base 8 score. Do not describe the score as a click probability or treat source inspection as equivalent.

2. Blocked custom-cost localization is not wired to the native blocked key. The decision uses custom_cost_text = chaosx_nr25_dependence_destroy_cost at common\decisions\025_alien_technology_in_antarctica_evolution_decisions.txt:224. Its base key at localisation\english\025_alien_technology_in_antarctica_l_english.yml:330 invokes GetChaosxNr25DestroyMaterialCost, while the four ready or blocked variants are named chaosx_nr25_destroy_material_cost_* in localisation\english\025_alien_technology_in_antarctica_custody_l_english.yml:4-7. No chaosx_nr25_dependence_destroy_cost_blocked key exists. The offline Decision modding page says a false custom_cost_trigger selects the custom cost key with the _blocked suffix. Vanilla AUS.txt:990-995 pairs custom_cost_text with decisions_l_english.yml:85-87, which defines the base, _blocked, and _tooltip keys. The intended red per-resource states therefore are not reached through the native blocked-cost lookup.

   Recommended owner fix: define chaosx_nr25_dependence_destroy_cost_blocked as [This.GetChaosxNr25DestroyMaterialCost] beside the base key in localisation\english\025_alien_technology_in_antarctica_l_english.yml. Consider a concise _tooltip key if the native cost hover should repeat the two payments.

3. Destruction adds 10 Exposure Risk without naming that consequence in the effect tooltip. The executor adds constant:chaosx_nr25_cost.exposure_destroy at common\scripted_effects\025_alien_technology_in_antarctica_custody_policy_effects.txt:21, and the constant is 10 at common\script_constants\025_alien_technology_in_antarctica_constants.txt:456. The player-facing chaosx_nr25_dependence_destroy_effect at localisation\english\025_alien_technology_in_antarctica_l_english.yml:298 explains destruction, retained technology, lower Dependence, ended material incidents, and Contain cancellation, but not the Exposure Risk increase.

   This matters especially in the new active-race route. The board selects Dependence only after settlement or a recorded fragment/Event 036 outcome at common\scripted_triggers\025_alien_technology_in_antarctica_triggers.txt:754-760. A pre-winner fragment holder therefore remains on the Exposure Risk value while this action can run. The named accepted specs do not state the +10 effect. Keep the balance value untouched in this review, and ask the parent to either accept and describe this consequence or resolve its design status.

4. The blocked-requirement sentence does not name the new active-race condition. chaosx_nr25_destroy_material_requirements currently says to “finish the previous expedition action” in localisation\english\025_alien_technology_in_antarctica_custody_l_english.yml:2. In the active race, availability instead requires an already running Contain Systems phase mission. When the button is blocked because that exact mission is absent, the generic sentence does not identify the needed mission. A scoped dynamic tooltip should distinguish the active-race Contain requirement from the aftermath cooldown requirement.

5. Two rejection paths lack direct destruction-policy regression cases. The new test test_fragment_holder_can_destroy_during_active_race_containment proves the positive Contain exception at .tools\test_event025_destruction_policy.py:140-155, but there is no paired case with an unrelated phase_mission_kind. The shared physical-custody consistency trigger rejects an owned fragment role outside 1-6, but the bad_role case at .tools\test_event025_custody.py:246-265 exercises transfer, not destruction. Add source tests for an unrelated active phase and a corrupted sender-owned role, asserting zero debit, flags, cooldown, and callbacks. The current source predicates appear to reject both states, so these are confidence gaps rather than confirmed runtime defects.

## Decision category lifecycle

The relevant ordinary category is chaosx_nr25_evolution_category in common\decisions\categories\025_alien_technology_in_antarctica_categories.txt:24-38. It stays visible to a participant while an Event 025 evolution is active. No scripted GUI layout is part of this bounded surface.

At most five Evolution V policy actions are visible together: Contain, Destroy, Transfer, Conceal, and Integrate. Destroy is visible only while the country holds physical material. After successful retirement it disappears because the ledger no longer proves custody. The other policy rows can remain visible while the participant’s settlement state is valid, and Integrate is visibly blocked by the active-material tooltip. The category remains open for the non-terminal aftermath. This surface stays within the six-action budget.

## Cognitive load and player-facing values

The destruction row has two inline spendable values and no resource-name prose. The support-equipment and stability texticons are wired at interface\chaosx_texticons.gfx:90 and the installed vanilla interface\texticons.gfx:105 respectively.

The requirement and effect sentences are short and do not expose raw triggers. The effect text clearly states that learned technology remains and that the material is retired. Its missing Exposure Risk consequence is the one unexplained value change identified above.

The parent explicitly excluded GUI geometry and reported no GUI source change. No GUI render or visual-fit claim is made here. The source cost strings contain two short entries, but their native blocked-key route is incomplete.

## Mission quality

| Mission | Owner | Category | Region | Requirement | Duration | Success | Failure | Duplicate risk |
| --- | --- | --- | --- | --- | ---: | --- | --- | --- |
| chaosx_nr25_contain_alien_systems_mission | Participant country holding a valid Evolution V material route | chaosx_nr25_evolution_category | Country-level with no map target. It can run during a qualifying active race or in aftermath. | Mission active flag, participant flag, and phase kind contain_alien_systems | 240 days | Completion without a Dependence accident and below the accident threshold is full success. Completion without an accident but above the threshold is partial success. | An accident or timeout marks failure, increases Dependence and Exposure Risk, and clears the contained state. | One phase mission can run at a time. The mission is repeatable after resolution and cooldown. No simultaneous duplicate path was found. |

The active-race destruction exception requires the running phase kind to be contain_alien_systems. The policy effect removes only chaosx_nr25_contain_alien_systems_mission and clears its active phase marker and kind. It does not invoke the broad phase-mission cleanup helper.

chaosx_nr25_contain_systems_attempted is set when the mission starts and cleared if Destroy cancels a running Contain mission. A repository source search found no other reader. It does not act as a once-only receipt or repeat guard. Sequential mission repeats remain possible, which is consistent with a recoverable containment route unless the parent intends one attempt only.

## Cost and requirement audit

| Spendable type | Display | Affordability | Debit | Count |
| --- | --- | --- | --- | ---: |
| Support equipment | 50 with support_equipment_text_icon | num_equipment@support_equipment >= 50 | Remove exactly 50 after the ledger receipt | 1 |
| Stability | 2% with stability_texticon | has_stability >= 0.02 | add_stability = -0.02 after the ledger receipt | 1 |

The action has two spendable cost types, below the four-type limit. The cost is not a political-power exchange. The retirement itself is the action outcome, not an extra resource payment. Dependence reduction is a benefit. Exposure Risk increase is an outcome and is not counted as a spendable cost.

The same inclusive cost predicate is reached by available through the legacy alias chaosx_nr25_dependence_destroy_cost_available at common\scripted_triggers\025_alien_technology_in_antarctica_triggers.txt:1069-1071, by custom_cost_trigger, by the dynamic cost text, and by the executor’s current preflight. The alias forwards to chaosx_nr25_destroy_material_cost_available. The cost text uses the correct icon for each spendable value, but the native _blocked localization key is missing as described above.

The non-consumed requirements are Evolution V enabled, a participant, an independent non-capitulated country, physical custody with consistent slot receipts, scientific capacity at least 1, and an eligible aftermath or exact active-race Contain context. The active-race branch also requires cooldown at or below 0, a live unresolved race, and a non-terminal actor. The source does not hide a fifth payment in the effect tooltip or nested helper.

## Physical proof, AI validity, and route locks

chaosx_alien_recovery_ledger_destroy_physical_custody rechecks the sender’s independent-country eligibility, actual core or fragment ownership, and physical-custody consistency at common\scripted_effects\025_alien_technology_in_antarctica_ledger_effects.txt:1035-1076. The core must still resolve to the sender and not have a destroyed receipt. A fragment must have an owner target matching the sender, an assigned receipt, and no destroyed receipt. The consistency predicate checks sender-owned slot roles against the valid 1-6 range in common\scripted_triggers\025_alien_technology_in_antarctica_triggers.txt:260-381.

The destroy helper retires only the current sender’s core and owned fragments. It leaves another country’s fragment slots untouched. Retirement clears the relevant owner projections, marks the core or slots destroyed, rebuilds the fragment projections, and returns custody_applied = 1 only after mutation. Repeated retirement has no physical receipt and cannot charge again. The initialized-core receipt prevents the core from being recreated.

The new active-race path is exact to a live Contain phase marker and kind. The same country-validity, physical custody, consistency, scientific-capacity, and cost checks remain outside that branch. It does not satisfy the ordinary base-action gate by turning off phase-mission exclusivity.

The public chaosx_nr25_execute_evolution_action rechecks retired-material eligibility for Integrate before calling the private unchecked body at common\scripted_effects\025_alien_technology_in_antarctica_runtime_effects.txt:2268-2284. Repository search found no other production callsite for the unchecked body. Dependence pulse growth and accident branches both use chaosx_nr25_active_material_incidents_allowed at runtime_effects.txt:969-979 and 1020-1034. Reacquiring a different valid physical slot makes that gate true again.

The decision and AI use the same native visible, available, custom-cost, and complete-effect route. The action has no country target. Its existing base weight remains 8 at evolution_decisions.txt:226. No AI weight or balance target was changed. The AI score remains unevaluated pending the probability route.

## Cleanup, outcomes, and exploit risk

chaosx_nr25_execute_destroy_material initializes its result to zero, requires the complete current preflight, initializes all nested ledger outputs, calls physical retirement, and debits only after custody_applied equals 1. Only after that receipt does it change Dependence, policy flags, cooldown, and the destruction result at custody_policy_effects.txt:5-41.

The unchecked executor skips its generic last-action and cooldown write for Destroy. Its final Chaos, evolution-gate, board, and achievement callback block runs for Destroy only when destruction_applied equals 1 at runtime_effects.txt:2482-2536. The destruction tests exercise exact resources, repeated calls, rejections, and ledger rejection at .tools\test_event025_destruction_policy.py:95-179. The test harness uses callback spies and does not emulate HOI4 stockpiles, scheduling, GUI, or save/reload.

The ledger preserves the historical Event 025 owner and learned technology. The source does not revoke technology or rewrite the reward record. The destruction policy lowers Dependence by 60 and clamps at zero. The action is non-terminal.

## Recommended owner follow-up

1. Add the native blocked-cost alias at localisation\english\025_alien_technology_in_antarctica_l_english.yml using the existing scripted getter.
2. Resolve whether Exposure Risk +10 is accepted for both aftermath and the active-race exception. If retained, explain the visible change in chaosx_nr25_dependence_destroy_effect. Do not change the value as part of this audit.
3. Replace or branch the generic blocked-requirement sentence so the active-race Contain requirement is explicit.
4. Add the two negative source cases for unrelated phase kind and corrupted sender-owned role. If the pulse behavior itself needs coverage, execute the pulse branch after retirement and after assigning a different physical fragment, rather than checking only the helper predicate.
5. Keep the AI score and owner API unchanged until a scenario-specific probability audit and comparison are returned.

## Validation and evidence limits

The parent reports 51 task tests pass. I did not rerun tests because this assignment was a read-only review. I reviewed test_event025_destruction_policy.py, test_event025_custody.py, and test_event025_active_hazards.py and their explicit limits.

No HOI4 process was launched. No GUI geometry, transfer policy, whole-event behavior, or full AI campaign audit is claimed.

hoi4.reference_context returned MCP -32603 while scanning C:\Users\klimp\AppData\Local\hoi4-agent-tools\state\request-capacity\43f52410ceeba65a\1. The parent reports reference_context limit 2 and limit 1 both timed out at 600 seconds, while reference_search for num_equipment succeeded and reference_read retries at 3 lines and 1 line timed out at 600 seconds. The corresponding offline wiki and installed documentation sections were read directly. These local references are not MCP revisions.

The live decision_inspect schema was retrieved. A request without scenarios was rejected with MCP -32602 because declared scenarios are required. The parent’s corrected destroy_exact_resources scenario request remains pending. probability_inspect’s live schema was retrieved, but scoped and minimal calls remained pending without results and were stopped. No probability artifact, scenario hash, source revision, sweep, or comparison is available.

Reference evidence read directly:

| Source | Section | Local SHA-256 |
| --- | --- | --- |
| paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md | Custom cost fallback, lines 305-320 | 7713B9BCEE5F3818D63AAFBD45D18E812A9173A7C59AB238384B57DB60DB6162 |
| paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md | num_equipment stockpile semantics, line 1615 | 62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4 |
| C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\dynamic_variables_documentation.md | num_equipment and has_stability, lines 435-441 and 557-564 | 538525747F0C285062C9CE8DB14B4E07C3CF6BAC1013115FA4F57291CB4EBDDA |
| C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md | Stockpile removal and add_stability, lines 1252-1265 and 2173-2180 | 2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF |
| C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md | has_equipment and check_variable, lines 3835-3842 and 2110-2127 | 7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29 |

Current source byte identities:

| Source | SHA-256 |
| --- | --- |
| common\scripted_triggers\025_alien_technology_in_antarctica_custody_policy_triggers.txt | 7439DF874F0A6E3973DC4924383D8D1159D0C4AE2685BDF857748DC7595C490D |
| common\scripted_effects\025_alien_technology_in_antarctica_custody_policy_effects.txt | 59530725673BAF8688343A82210CCB96B8703CB5BC2B2562DD829303ADC3EFF3 |
| common\decisions\025_alien_technology_in_antarctica_evolution_decisions.txt | FEE503F8C6B2FB4C4376C1F95AD9222602B3DF3F59F4D965BD429454C08FA574 |
| common\scripted_effects\025_alien_technology_in_antarctica_ledger_effects.txt | 91F55888298A54E2B711EFE1CA1AD4C2F122951D6121089E1DD637886C4692DE |
| common\scripted_effects\025_alien_technology_in_antarctica_runtime_effects.txt | DE2CB1DBF84A7C62C4875218C03A459F0346B7A077B06AAD49DCE156DD6C4162 |
| localisation\english\025_alien_technology_in_antarctica_custody_l_english.yml | E05DF823161C102E5BA1A47760EB15D65BF8C439B1A745AAD9FCCE5EA2E148C9 |
| .tools\test_event025_destruction_policy.py | F5578549C61881351BF839919C55B5C8CB83582662B82CD8F1348ACE5DAE7B09 |

## Handoff files and behavior

Changed file: docs\plans\025_alien_technology_in_antarctica_plans\subagent_handoffs\025_destruction_policy_audit_20261003.md only.

Changed decision, mission, scripted GUI, and localization IDs: none. Source and player-facing behavior before and after this audit are identical.

No source patch, balance change, GUI change, test run, commit, or plan handoff was made. The parent should review the findings and own any follow-up patch and commit.

## Parent follow-up status, 2026-10-03

This appendix preserves the preceding sections as the initial read-time record. The statuses below describe the later parent-owned source changes that I reviewed afterward. The initial disposition and findings are not silently rewritten.

| Initial finding | Follow-up status |
| --- | --- |
| Missing native blocked-cost key and cost hover key | Resolved in current localisation. The base, _blocked, and _tooltip keys now exist at localisation\english\025_alien_technology_in_antarctica_l_english.yml:330-332. |
| Exposure Risk increase was absent from the effect tooltip | Resolved by parent acceptance of the existing +10 as the physical-dismantling consequence within the Exposure Risk system. The value is unchanged and the tooltip now says dismantling raises Exposure Risk. No budget or AI weight changed. |
| Active-race availability and blocked-requirement wording | The initial statement that every active-race destruction required a running Contain mission was incorrect and is corrected below. The current dynamic requirement localization distinguishes normal availability, a running Contain mission, and an unrelated active project. |
| Missing negative source cases | Resolved in the current source tests for unrelated phase projects in both race and aftermath contexts, corrupted sender-fragment roles, and pulse execution after retirement and after new material is acquired. The parent reports all 54 source cases passing. I did not rerun them. |
| AI probability evidence | Still unresolved. No AI weight or balance target changed. No probability artifact or scenario result has been returned. |

### Correction to initial Finding 4

The normal active-race path does not require starting Contain. The first branch in chaosx_nr25_destroy_material_context_valid calls chaosx_nr25_evolution_technology_changes_users_action_available. Its normal base_action_available path requires no active phase mission, so a participant with verified physical material may destroy it during the active race without starting a Contain mission.

The separate active-race AND branch is an exception for an already running Contain Systems mission. In the current trigger, a final phase guard rejects any active phase mission whose kind is not Contain Systems. This also rejects unrelated projects in aftermath. The updated GetChaosxNr25DestroyMaterialRequirements helper chooses distinct normal, Contain, or unrelated-project text.

I withdraw the initial claim that the active-race normal path required a running Contain mission. The initial source already allowed the no-mission normal path through base_action_available. The later parent change adds the explicit cross-context unrelated-project rejection and dynamic blocked-reason text.

### Current source and test follow-up

The native blocked-cost lookup now reaches the same dynamic getter as the ready state. The _tooltip key now supplies cost-hover text. The effect tooltip names the retained technology, Dependence reduction, Exposure Risk increase, end of material incidents, and cancellation of a running Contain project.

The new unrelated-phase test checks both active-race and aftermath contexts. The corrupted-role test assigns an invalid role to a sender-owned fragment and checks that retirement causes no debit or policy mutation. The pulse test executes the hazard branches after retirement and again after a different physical fragment is assigned. These are source-harness results as reported by the parent, not HOI4 engine or live-game evidence.

Current source byte identities for the parent follow-up:

| Source | SHA-256 |
| --- | --- |
| common\scripted_triggers\025_alien_technology_in_antarctica_custody_policy_triggers.txt | 0F1B11191C95994E3B1CD96A2187FBC8E5253A727FB315B9D65D937360CBABF7 |
| common\scripted_localisation\025_alien_technology_in_antarctica_custody_scripted_localisation.txt | 319BC2C93FE735DAAE41EFDEE0EFC87F21ED1783C3E85EB8610B79A2E234DD56 |
| localisation\english\025_alien_technology_in_antarctica_l_english.yml | C4F073FD172D42E52272173A729B78E506D5E4AB887BF9382BD8B2AA40180CB4 |
| localisation\english\025_alien_technology_in_antarctica_custody_l_english.yml | 46A036420E4AB658E8726BE7CFCBBBD42832DD448FA65055FCA0F93FF559D715 |
| .tools\test_event025_destruction_policy.py | AA5A19DB8D1172718543883A84F6D10D0286AAE39E03F61893E16726CF18CBE9 |
| .tools\test_event025_active_hazards.py | BA99A92DC25CB781BFD88265363F0B80A8FDAB6EBB51454BAD6C9554FFBC0354 |

### Current MCP status reported by the parent

The corrected decision_inspect request with the declared destroy_exact_resources scenario returned an UNKNOWN-lstat job error beginning with job 1344. A narrow mode=inventory request for the same decision remains pending. Neither is a completed inspect result.

The parent reports reference_context retries at limits 2 and 1, plus narrow reference_read retries of 3 lines and 1 line, each timing out at 600 seconds. reference_search for num_equipment succeeded. The local offline references remain the syntax evidence recorded above, not MCP revisions.

The probability evidence remains unresolved from the earlier 025_reward_probability_baseline_20261003 handoff. That handoff covers the Event 016 external reward pool, not the unchanged Event 025 decision base 8 score. Do not use it as scenario equivalence.

Current disposition: the cost-localization, exposure-tooltip, active-race clarification, and source-test findings are resolved in the parent follow-up. The AI probability evidence remains unresolved. This reviewer changed only this handoff file and did not stage or commit it.
