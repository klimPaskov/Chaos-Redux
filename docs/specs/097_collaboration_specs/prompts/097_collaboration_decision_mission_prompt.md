# Event 097 Collaboration: Decision and Response Prompt

Implement the two Event 097 decision categories and the Collaborators Unmasked event choice defined in `docs/specs/097_collaboration_specs/specs/097_collaboration_spec_part_4_decisions_and_responses.md`. Follow `chaos-redux-decisions-missions` for every surface. Event-owned decisions belong in `common/decisions/097_collaboration_decisions.txt` and their categories in `common/decisions/categories/097_collaboration_categories.txt`, unless an inspected engine constraint requires otherwise.

The design audit in `docs/plans/097_collaboration_plans/subagent_handoffs/097_decision_mission_audit.md` shaped this part. Read it for the reasoning behind the rules below.

## Surfaces

| Surface | Working label | Content |
| --- | --- | --- |
| Host category | Divided Loyalties | A1 Loyalty Commissions, A2 Arrest the Prepared Officials, A3 Evacuate the Ministries, A4 Commissars in the Ministries, A5 Charter a Government in Exile |
| Installer category | Prepared Governments | B1 Seat the Prepared Government (targeted), B2 Arm the Installed Administration (targeted) |
| Event choice | Collaborators Unmasked | Purge or Amnesty |

## Requirements

1. Phase every action exactly as Part 4 states, and confirm the rows-by-situation table: Divided Loyalties never shows more than four actions, and Prepared Governments never more than six rows.
2. Keep every cost to at most four distinct spendable types, with the correct texticon for each displayed cost, at most three values in the inline cost row, and a full cost tooltip. Use the `<base>`, `<base>_blocked`, and `<base>_tooltip` key pattern for custom costs. Check affordability inclusively just below, at, and just above each quote. Do not copy strict comparisons from older precedents.
3. A3 shows only the transport it will take, and its factory output penalty appears as the decision's timed modifier. A5 shows convoys or trucks the same way. Timed penalties of A3 and A4 always run their full duration.
4. Put every cost anchor, scaling bound, duration, cooldown, threshold, ladder row, floor, and cap in one Event 097 script-constant group. Use file-scoped constants only where a field rejects constant and variable tokens.
5. Political power quotes vary, so `ai_hint_pp_cost` must be a static value mirrored from the highest quote an action can reach, or omitted where a lower quote must stay reachable for AI. Record the choice for each action.
6. Use one shared affordability predicate for each custom cost in both `available` and `custom_cost_trigger`, and debit the custom payment once in `complete_effect`.
7. Name blocked requirements precisely, such as the stability floor for A1 and A4, the missing seated state for A2, and the current and required compliance for B1.
8. Targets come from lists the event maintains in its own hooks: enemies holding seated states for each host, capitulated or exiled B1 targets, and each installer's living registry rows. Use root prechecks for the installer. Category visibility reads markers set by those hooks. Nothing searches every country every day.
9. B1's compliance requirement uses the ladder in Part 4, written so a pure trigger can check it, with collaboration on its native 0 to 1 scale. Split B1 into visibility and availability as Part 4 states.
10. A2 and the Purge option subtract fixed points and stop at zero, following the reduction rules in Part 4. Verify the engine behavior first. Report a blocker if no accepted route works.
11. B1 and the capitulation offer must call one shared installation helper that owns the registry, the Installed Administration spirit, auxiliaries, Chaos, and the competing-orders check. Auxiliary prices come from the template constants.
12. The Divided Loyalties category uses a static category picture, after inspecting the canonical picture reference family and its contact sheet. The Prepared Governments category uses its icon and text only.
13. The category text shows the networks reading, the effective Fifth Column band with the strongest network and the held-down note when relevant, and the names of running measures. No remaining days, pipes, divider rows, or raw variable names.
14. Implement the raw and effective band split exactly as the table in Part 4 assigns it.
15. Implement the Fallout rules, the evolution-disabled rules, the war-scoped guards from Part 3, and every exploit guard in Part 4.
16. Implement AI weights from the orderings in Part 4, Part 6, and `matrices/097_collaboration_ai_probability_scenarios.md`, using MTTH-backed entries. Run `chaosx_ai_probability_auditor` before and after setting weights, with an immutable pre-edit copy for comparison.
17. Spawn `chaosx_decision_mission_auditor` with a self-contained prompt after implementation and resolve its findings.

## Engine checks for this part

Verify these facts and record them in `docs/events/097_collaboration/` before relying on them: whether negative collaboration changes stop at zero, the scale of the collaboration and compliance reads, whether the compliance trigger accepts a variable, how spawned divisions are equipped, whether decision re-enable timers count from completion or removal, and whether cost text can show per-target quotes for targeted decisions.

## Balance evidence

Record the scenario results requested in Part 6, Balance review requirements, for every action. A statement that the system is balanced without recorded scenarios is not acceptable.
