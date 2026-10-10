# Event 029 implementation continuation prompt

Continue Chaos Redux Event 029, Riches Found, from its current source to the design in `docs/specs/029_riches_found_specs/`.

The event is substantially implemented; do not rebuild it from scratch, and do not replace any accepted route with a smaller prototype, a political-power shop, a scripted GUI, a new country tag, a custom unit, or an Event 018 fallback.

## Read first

1. `CLAUDE.md` (coding style, reference workflow, MCP retry limits, completion and commit rules).
2. `.claude/skills/chaos-redux-events/SKILL.md`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-mtth`, and `chaos-redux-subagents` under `.claude/skills/`.
3. [The Event 029 overview](../../events/029_riches_found/overview.md), the source map of what exists.
4. [The latest continuation checkpoint](../../plans/029_riches_found_plans/subagent_handoffs/parent_continuation_2026_10_08.md) and [the agent decisions record](../../plans/029_riches_found_plans/agent_decisions_2026-10-04.md).
5. The spec parts, which own the design; the README's Open questions list what still needs the user's answer.

Other sessions may have uncommitted edits in Event 029 files; read the working tree, keep their hunks, and commit only your own change through `chaos-redux-shared-git-commit`.

## Where each rule lives

| Topic | Owner |
| --- | --- |
| Recipient, state selection, Event 018 separation, transfer, values, header, aggregate and caps | [Part 1](029_riches_found_spec_part_1_core_loop.md) |
| Milestones and overlays, projects, revenue routes, concessions, security, closure, collapse, conquest | [Part 2](029_riches_found_spec_part_2_baseline_progression.md) |
| Decision layers, cost rules, decision and mission families, foreign targets, occupation, cleanup, exploits | [Part 3](029_riches_found_spec_part_3_decisions_missions_foreign_interference.md) |
| Evolutions, containment, late outcomes, Gold Disease routes, the account | [Part 4](029_riches_found_spec_part_4_evolutions.md) |
| AI intent, balance, exploit prevention, shared systems, multiplayer, persistence | [Part 5](029_riches_found_spec_part_5_ai_balance_interactions.md) |
| Assets, writing direction, achievements | [Part 6](029_riches_found_spec_part_6_assets_localisation_achievements.md) |
| Probability scenarios and audit sequence | [AI scenarios](029_riches_found_ai_probability_scenarios.md) |
| Test scenarios | [Acceptance criteria](029_riches_found_acceptance_criteria.md) |
| Catalog wording | [Catalog alignment](029_riches_found_catalog_alignment.md) |

## Remaining work

Accepted design that is not yet in source:

1. Header and tooltip trim: the Part 1 header (Development as a band, one conditional line), the shorter aggregate tooltip, and the two-value opening option tooltips in Part 6; reconcile with the uncommitted header edit already in the working tree.
2. Cost scaling by geography, damage, and repetition (Part 3 cost rules), including the specialist-labour, workforce-replacement and evacuation transport helpers, which are parked unloaded in `docs/plans/029_riches_found_plans/deferred_transport_cost/` with their contract until a decision consumes them (no decision calls them, and an unused helper module must not ship in `common/`).
3. Event 028 crater handling during the ordinary refresh (Part 1).
4. Live consumers for the three evolution icons (Part 6).
5. Individual review or repair of the 37 unreviewed decision icons (Part 6).
6. Unlock and disqualifier acceptance for the seven achievements (Part 6 and the acceptance criteria).
7. Probability evidence for the surfaces still open in the AI scenarios file, using script calculations where the tool cannot classify decisions.
8. Closure review of the sealing receipts and the native civilian-factory ordering gap ([seal receipt contract](../../events/029_riches_found/seal_receipt_contract.md)).
9. The distant naval-power partner route (Part 2, Foreign interest).
10. The open checkpoint items: surviving-claim and aftermath category lifecycle, continuous supplied-force proof for Hold the Mine and the pay train, anti-farming and achievement campaign tracking, the wartime and occupation policy scenarios, and the housing and diversification effects check.
11. Cleanup: remove the never-set claims-policy constants (Part 2).

Proposals that need acceptance before any source change: the famine food-need adapter, the migration evacuation hand-off, the Event 013 earthquake hand-off, and the hidden-value merges.

## Checks

Use the acceptance criteria for scenarios, the AI scenarios file for weighted surfaces, and the auditors named in `CLAUDE.md` before a completion claim.

Keep `docs/events/029_riches_found/overview.md` and the package README's implementation status in step with every change, and update the workbook only through `chaosx_spreadsheet_doc_worker` and the exporter when player-facing wording changes.

Report every blocker, simplification, and unresolved item as `CLAUDE.md` section 5 requires; the user owns live-game testing.
