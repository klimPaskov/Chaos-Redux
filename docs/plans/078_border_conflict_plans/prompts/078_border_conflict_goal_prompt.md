/goal
Implement Event 078 Border Conflict completely from docs/specs/078_border_conflict_specs/, starting with 078_border_conflict_spec_part_1_core.md and every supporting spec.
Use docs/plans/078_border_conflict_plans/prompts/078_border_conflict_coding_prompt.md and the adjacent asset, achievement, and decision_mission prompts.
Read the plans README, research limits, engine evidence, implementation handoff, acceptance matrix, probability scenarios, and specialist briefs.
Follow current AGENTS.md, mechanics, events, planning, decisions, assets, dynamic effects and triggers, MTTH, debugging, improvement-loop, and subagent skills.
Fully inspect required current repository and installed vanilla sources before relying on their behavior.

First prove native simultaneous border battles for one country against several neighbors and multiple independent fronts between one pair, with exact conflict-specific callback identity and unrelated-war participation.
Document version, DLC, endpoints, callbacks, persistence, and results.
An unsupported engine requirement is a blocker.
Never substitute normal wars, abstract outcomes, serialized country queues, or hidden country caps.

Every firing checks the current worldwide land-neighbor map, deduplicates pairs, and gives baseline opportunities before evolved extras.
Exclude direct normal war between the pair and genuinely invalid endpoints, never a participant's unrelated war or disjoint border battle.
Respect reservations across waves and systems.
Choose a distinct target state uniformly before choosing its staging state.
Use native combat with automatic transfer disabled.
Attacking victory awards only the declared target once, defending victory retains it, and cancellation awards nothing.
Reject stale callbacks, foreign ownership changes, reused identities, and duplicate receipts.
Remove the old ordinary-war option and global opponent pointer safely.

Implement all three thresholds, separate toggles, evolved openings, paced active mutations, cumulative root quotas, and repeat overlap.
Momentum seeds only after an eligible capture, advances through newly opened adjacency against the original opponent, and continues after wins until a defined stop.
No root refill, repeated seed roll, third-country jump, delayed retry queue, free units, or organization reset.
Preserve one-firing timer, weight, and Wars cluster accounting plus correct evolution history and narrative-only Event Details.

Implement every mapped Chaos source, cross-wave rolling guard, wave budget, and containment reduction.
Prove shared generic consequences are not double counted.
Implement all three achievements from genuine result evidence and continuous holds without keeping closed waves active.
Build the native information category, complete localization from the briefs, and produce all report, news, category, and achievement assets through canonical references and processors.
Validate each actual consumer, exact identity, dimensions, alpha, and achievement states.

Execute real bounded specialist handoffs with fork_turns="none" when collaboration is available.
Spawn chaosx_ai_probability_auditor, begin with hoi4.probability_inspect, evaluate named scenarios, sweep thresholds and toggles, and compare changes using verified adapters.
Near completion spawn chaosx_improvement_loop_planner and resolve its addendum or closure before final acceptance.
Run completion, decision, localization, and documentation reviews.
Missing tools are blockers, not passed reviews.
Update only the authoritative workbook, regenerate exports, and retain To Be Reworked until acceptance.
Keep iterating until the implemented files satisfy the full spec.
Return concrete source, native, probability, asset, multiplayer, save/load, specialist, and catalog evidence with every remaining blocker.
Do not claim completion until the delivered implementation meets the complete specification.
