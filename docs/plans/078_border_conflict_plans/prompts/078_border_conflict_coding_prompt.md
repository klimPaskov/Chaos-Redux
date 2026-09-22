# Implement Event 078 Border Conflict

Implement the complete Event 078 rework from `docs/specs/078_border_conflict_specs/`.
Begin with `078_border_conflict_spec_part_1_core.md`, then read every supporting specification in that folder.
Read `docs/plans/078_border_conflict_plans/README.md`, the engine evidence, reading limits, implementation handoff, validation matrices, and prepared specialist briefs.
The package contains planned behavior and explicit unproven engine gates.
Do not treat a planning document or source snippet as successful runtime validation.

Follow the current `AGENTS.md`, mechanics, planning, events, decisions and missions, assets, dynamic effects and triggers, MTTH, debugging, improvement-loop, and subagent skills.
Fully read the relevant current implementation and installed vanilla references required by those skills.
The supplied archive was read by the planning author, but its external dependencies and complete current framework implementation were not all reviewed.
Resolve those gaps before relying on a copied pattern.

## Prove the engine first

Use a bounded native fixture to establish simultaneous border battles for one country against several neighbors, independent simultaneous battles between one pair, and exact conflict-specific result identity.
Also prove participation during an unrelated normal war.
Record installed game version, DLC, endpoints, native callbacks, results, and save/load behavior.
If the engine cannot meet the contract, return the exact evidence and blocker.
Do not substitute a normal war, an abstract military roll, or serialized country-by-country combat.
Do not invent a country concurrency cap.

## Implement the full lifecycle

Each accepted firing examines the current worldwide land-neighbor map.
Deduplicate unordered country pairs.
Exclude a direct normal war between the two participants and native-invalid endpoints, but never apply a blanket peacetime or no-existing-border-war rule to a country.
Give each pair its baseline opportunity before evolved extra roots.
Sample distinct target states uniformly, then choose a valid staging endpoint.
Respect incompatible reservations across waves and other border-war systems.

A battle has one declared disputed state.
Use native combat with automatic state transfer disabled, then award only that target after a validated attacking victory.
A defensive win retains it.
Draws, cancellations, stale callbacks, foreign ownership changes, and a new direct normal war grant no Event 078 state.
Both sides' callbacks must converge on one idempotent result.
Do not keep the old global opponent variable or ordinary-war option reachable.

Implement all three Chaos thresholds, separate evolution toggles, immediate evolved openings, and the paced active-evolution route.
Multiple Frontiers uses the specified cumulative root allowance.
Border Momentum seeds after an eligible capture and continues through genuinely newly opened adjacency against the original opponent.
Borders in Motion amplifies only enabled mechanics.
A seeded chain has no repeated seed roll, arbitrary depth cap, third-country branch, or delayed retry queue.
Do not generate free troops, reset their organization, or refill consumed roots.

Implement repeat overlap, wave closure, interruption, owner/controller changes, tag reuse, and safe legacy-save handling as specified.
Preserve the shared timer, weights, one-firing cluster accounting, evolution history, event log, and narrative-only Event Details.
Inspect actual current framework names before editing them.

## Consequences, presentation, and objectives

Implement every event-owned Chaos source and the containment reduction with exact occurrence tests, cross-wave rolling guards, and wave budgets.
Prove generic shared sources are not double counted.
Implement all three achievements from attributable Event 078 results and continuous holds.
Keep hold tracking separate from live-wave evolution eligibility.

Build the native informational category and state-targeted presentation without paid combat decisions or an unrelated scripted GUI.
Write final localization from the direction briefs.
Produce every report, news, category, and achievement asset through the canonical pipeline and inspect its actual native consumer.
Use the separate asset, achievement, and decision-mission prompts.
No final images or localization were produced by the planning author.

## Specialist execution and completion

Use real `collaboration.spawn_agent` calls with `fork_turns="none"` and self-contained bounded prompts when those tools are available.
Use the prepared specialist briefs and enforce their allowed file scopes.
Do not represent the role definitions as already executed.
Run `chaosx_ai_probability_auditor` for target pools, root seeds, repeat selection, and active MTTH, beginning with `hoi4.probability_inspect`.
Evaluate named scenarios, sweep boundaries and toggles, simulate only declared uncertainty, and compare after relevant changes.
A source-only inspection cannot replace the required probability evidence.

Near completion, spawn `chaosx_improvement_loop_planner` and resolve its addendum or closure handoff.
Run the relevant independent decision, localization, completion, and documentation checks.
Keep iterating until the implemented files satisfy the complete specification.
Missing tools and failed native gates remain explicit blockers, not passed tests.

Update the authoritative catalog workbook through the spreadsheet worker after final implemented behavior and wording are ready.
Preserve Minor Repeatable, Chaos level 1, Wars/Medium, and the three evolution thresholds.
Regenerate exports through the repository tool and never hand-edit CSV snapshots.
Do not change To Be Reworked to completed before actual acceptance.

Return a concrete completion report covering files changed, preserved compatibility boundaries, source and native evidence, probability outputs, asset previews, multiplayer and save/load results, specialist findings, resolved improvements, and all remaining blockers.
Do not claim completion until the delivered implementation satisfies the full source specification.
