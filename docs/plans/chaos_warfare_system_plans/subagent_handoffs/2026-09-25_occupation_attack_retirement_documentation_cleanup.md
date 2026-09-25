# Occupied-state CBRN attack retirement: documentation cleanup handoff

## Scope and acceptance basis

The parent assigned documentation-only reconciliation for the 2026-09-25 user-approved removal of all decision-based CBRN attacks, retaining exactly two native CBRN raid categories and historical aftermath without inventing an owned-state replacement. This handoff covers only `docs/systems/cbrn_warfare/cbrn_occupation_and_nerve_suppression.md`, `common/scripted_effects/cbrn_scripted_effects.md`, and `common/scripted_triggers/cbrn_scripted_triggers.md`. The source snapshot is evidence of implementation, not a second acceptance basis or a live-game result.

## Source-of-truth map

| Claim | Acceptance or current evidence | Limit |
| --- | --- | --- |
| Retire Sarin and Soman occupied-state decision attacks without replacement. | Explicit user-approved plan relayed in the parent assignment; the final searched `common/decisions/cbrn_occupation_decisions.txt`, `common/scripted_effects/cbrn_occupation_effects.txt`, and `common/scripted_triggers/cbrn_occupation_triggers.txt` have no Sarin or Soman attack decision, direct execution helper, or preparation and target gate. | Parent still owns final cross-repo and raid-category review. |
| Keep occupation law compatibility and defensive occupation. | The coercive authorization decision remains hidden, the coercive law and AI law gate remain, and Protected Occupation Administration is still offered in the decision and occupation-law files. | Hidden legacy gate presence does not imply attack availability. |
| Keep external protective aid. | `cbrn_deploy_protective_aid` reserves exact-state real masks at selection, debits Political Power after a positive reservation, tracks the paid project, and refunds unused masks on cancellation or invalid completion. | No live decision-row or gameplay test is claimed. |
| Keep historical aftermath and disclosure. | The four record-response decisions and exact UID, trauma, backlash, discovery, and control-change helpers remain in the occupation source files. | The retained accepted-operation writers have no caller in the bounded text-source search; they do not establish a current attack. |
| Keep camp method separate. | `common/scripted_effects/cbrn_camp_effects.txt` still bridges the restricted-site camp transaction. | Camp gameplay and native raid completion are outside this documentation pass. |

## Document dispositions

| Document | Disposition | Basis and action |
| --- | --- | --- |
| `docs/systems/cbrn_warfare/cbrn_occupation_and_nerve_suppression.md` | Implemented documentation alignment. | Replaced the stale attack walkthrough with a concise current source map, law and aid behavior, historical record readers, camp distinction, and evidence limits; source files above support each present-behavior claim. |
| `common/scripted_effects/cbrn_scripted_effects.md` | Implemented documentation alignment. | Removed the deleted direct attack helper contract; described retained law, external-aid receipt, exact UID, and aftermath effects from current source. |
| `common/scripted_triggers/cbrn_scripted_triggers.md` | Implemented documentation alignment. | Removed deleted condition-hook, preparation, execution, AI target, and cooldown gate descriptions; kept source-level coercive-law AI compatibility and aid/record predicates. |
| `docs/plans/chaos_warfare_system_plans/2026-09-25_cbrn_occupation_probability_baseline_fixture.json` | Unresolved. | It records an unbound, partial baseline for the former two decision candidates with 96 unresolved inputs and no normalized choice; parent reports post-edit comparison pending. It is evidence, not approval of a weighted outcome. |
| Older stage 9 and July/August occupation audit handoffs | Unresolved as whole historical reports; their active Sarin/Soman decision claims are superseded by the current system doc. | They contain other audit content outside this assignment, so no whole-file superseded notice or merge was applied. The parent should decide whether to annotate them after reviewing their other claims. |

No other plan or addendum was named for disposition in this bounded task. No accepted design was promoted into a spec.

## Contradictions and stale references

Resolved inside the three owned docs: the system doc previously described two 21-day Sarin/Soman attack preparations, their real operation payment and AI target selection, and a pending native condition hook as if they remained current; the source has retired them. The scripted-effect reference previously described the deleted execution helper, and the scripted-trigger reference named deleted condition, preparation, execution, target, and AI gates. These sections now state the current source boundary.

Still open outside edit ownership: `docs/plans/chaos_warfare_system_plans/2026-07-29_near_completion_improvement_loop_closure.md` says the Sarin/Soman actions merely remain unavailable through an old hook; `docs/plans/chaos_warfare_system_plans/stage_9_decision_mission_audit_handoff.md` inventories both timed attack decisions; and several July/August audit handoffs repeat those historical claims. The 2026-09-25 remaining cost-row audit also assesses the retired decisions as if still payable. These files are historical evidence, but a future reader needs a dated superseded notice or a current index pointer. The parent owns that wider cleanup decision.

No duplicate current system document was merged or deleted. No prompt file was named or inspected, so stale prompt instructions remain unassessed rather than presumed absent.

## Markdown and validation

No accidental mid-sentence or mid-clause hard wraps were found in the three owned Markdown files with a prose-line scan excluding headings, lists, tables, block quotes, and code fences. The rewrite retained deliberate Markdown structure and placed each new prose sentence on one physical line.

Targeted source searches found no remaining Sarin or Soman attack decisions, direct execution helper, or retired preparation and valid-target gates in the three parent-owned implementation files. A call-site search across text scripts found `cbrn_occupation_apply_accepted_operation_state` and `cbrn_occupation_record_country_history` only at their definitions. A targeted grep of the three owned docs found no operative instruction to use the deleted helpers. `git diff --check` found no content error in the three documentation edits.

The installed offline Paradox wiki core pages, installed vanilla decision, effect, trigger, raid documentation, and one vanilla land raid precedent were read before repository reconciliation. The `chaos-redux-subagents`, `chaos-redux-decisions-missions`, and `chaos-redux-native-raids` skills were applied. No repository skill was created or changed.

The HOI4 MCP event service responded to narrow `hoi4.event_inspect` traces for `cbrn_occupation.1` and `.2` and `hoi4.event_render` neighborhood views at source revision `f38750d657aae964fc445b75e7bd6dc5ca78a5f72ff6779d08ba080a8eaded7e`. The result codes were `EVENT_INSPECTED_PARTIAL` and `EVENT_RENDERED_PARTIAL`: the service deferred workspace-wide helper projections and lifecycle passes, so these artifacts do not prove reachability or complete event coverage. Stable trace artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5e4650fb4f73704acd898b2ebb2f97c5fdb472f8cfc67ae9de2cbf6338b00f35/10cf60c88ac43d7df145f681f51f62e026197373555a95de7c955253698a7e06/event-trace-f38750d657aa.json` for `.1` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5c1ec5824ffbece5e82a5df7e82bf358518215b807463b95945ede49f343dafd/3c5e9231c9cc1edb95eeb1f6f1514ac4acab812cf5eaaa7d6450e8d0d4ccaca8/event-trace-f38750d657aa.json` for `.2`. Render JSON artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e9cc3de735bb604baecd20dab7595ec3f09a11785ecc6aeba3864a69c8faa12f/f574fefffc041fc333ebea09bc3f91bbdef3b83454a49653447199596876d9db/event-neighborhood-f38750d657aa.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0d742525d4573ae7c52323c05e28fe43c69cdf3fba91bd089a9f6befb1ca0ef3/7a47f71038a1e56094af39d6143d192cb06aa8a1d89f4100e7211bb222eda02e/event-neighborhood-f38750d657aa.json`, respectively. No event comparison was run because this documentation pass changed no event source and had no comparable pre-edit event artifact.

The HOI4 MCP probability tool names are exposed in this agent context, but exposure alone does not prove their current service health. This curator did not run a new probability scenario: the specialist baseline fixture is partial, and the parent's post-edit auditor comparison remains pending. No technology, GUI, focus, or map behavior is asserted by these docs. No live-game validation was run or claimed.

## Files changed and parent review

- `docs/systems/cbrn_warfare/cbrn_occupation_and_nerve_suppression.md`
- `common/scripted_effects/cbrn_scripted_effects.md`
- `common/scripted_triggers/cbrn_scripted_triggers.md`
- This handoff.

The parent should verify that the final gameplay, localisation, and sprite edits have settled before relying on the source map, review the two native raid categories and their MCP evidence, obtain the post-edit probability auditor handoff, and decide how to mark older historical audits. The documentation pass made no gameplay, localisation, asset, spreadsheet, or spec edit and makes no overall completion claim. No commit was created; the parent owns review and commit.
