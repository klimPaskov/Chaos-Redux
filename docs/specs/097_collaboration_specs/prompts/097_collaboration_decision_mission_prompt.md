# Event 097 Collaboration: Decision and Response Prompt

Implement the two Event 097 decision categories and the Collaborators Unmasked event choice defined in `docs/specs/097_collaboration_specs/specs/097_collaboration_spec_part_4_decisions_and_responses.md`. Follow `chaos-redux-decisions-missions` for every surface. Event-owned decisions belong in `common/decisions/097_collaboration_decisions.txt` and their categories in `common/decisions/categories/097_collaboration_categories.txt`, unless an inspected engine constraint requires otherwise.

## Surfaces

| Surface | Working label | Content |
| --- | --- | --- |
| Host category | Divided Loyalties | A1 Loyalty Commissions, A2 Arrest the Prepared Officials, A3 Evacuate the Ministries, A4 Commissars in the Ministries, A5 Charter a Government in Exile |
| Installer category | Prepared Governments | B1 Seat the Prepared Government (targeted), B2 Arm the Installed Administration (targeted) |
| Event choice | Collaborators Unmasked | Purge or Amnesty |

## Requirements

1. Phase every action exactly as Part 4 states. The host category never shows more than four actions at once.
2. Keep every cost to at most four distinct spendable types, with the correct texticon for each displayed cost, at most three values in the inline cost row, and a full cost tooltip.
3. Put every cost anchor, scaling factor, duration, cooldown, threshold, and cap in one Event 097 script-constant group. Use file-scoped constants only where a duration field rejects constant and variable tokens.
4. Use one shared affordability predicate for each custom cost in both `available` and `custom_cost_trigger`, and debit the custom payment once in `complete_effect`.
5. Name blocked requirements precisely, such as the stability minimum for A1 or the missing seated state for A2.
6. A2 and the Purge option reduce native collaboration relatively and stop at zero. Verify that the engine supports this. If it does not, report a blocker. Never use an absolute set for a reduction.
7. B1 and the capitulation offer must call one shared installation helper that owns the registry, the Installed Administration spirit, auxiliaries, Chaos, and the competing-orders check.
8. The Divided Loyalties category uses a static category picture, after inspecting the canonical picture reference family and its contact sheet. The Prepared Governments category uses its icon and text only.
9. The category header shows the qualitative readings and, only when relevant, the Fifth Column band, the strongest network country, and the active protective measure. No pipes, divider rows, or raw variable names.
10. Implement AI weights from the orderings in Part 4 and `matrices/097_collaboration_ai_probability_scenarios.md`. Run `chaosx_ai_probability_auditor` before and after setting weights, with an immutable pre-edit copy for comparison.
11. Implement every cleanup rule and exploit guard from Part 4.
12. Spawn `chaosx_decision_mission_auditor` with a self-contained prompt after implementation and resolve its findings.

## Balance evidence

Record the scenario results requested in Part 6, Balance review requirements, for every action. A statement that the system is balanced without recorded scenarios is not acceptable.
