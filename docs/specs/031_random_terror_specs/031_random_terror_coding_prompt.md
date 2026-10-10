# Event 31 Random Terror implementation continuation prompt

## Goal

Finish Event 31 Random Terror against the accepted design in `docs/specs/031_random_terror_specs/`.
Event 31 already has a substantial runtime implementation that is enabled by default.
This prompt lists only the remaining work and points to the part that owns each requirement.
The parts, not this prompt, are the design source.

Do not replace mapped content with a smaller prototype, fallback, placeholder, or partial chain.
Do not claim completion while any item below is open.

## Read first

- `CLAUDE.md` at the repository root, including the HOI4 MCP retry limits and completion reporting rules.
- [The package README](README.md) for acceptance basis, status and open questions.
- [The event documentation](../../events/031_random_terror/overview.md) for the implemented identifiers.
- [The current completion audit](../../plans/031_random_terror_plans/subagent_handoffs/031_current_completion_audit_20261007.md) for findings C01 to C14 and their source line references.
- [The agent decisions](../../plans/031_random_terror_plans/agent_decisions_20261004.md) D1 to D13 and R1 to R47, which are accepted design.
- The skills `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-focus-trees` and `chaos-redux-subagents`, and the others named by the task.

Other sessions may be editing Event 31 files.
Read the current working tree before editing and keep unrelated edits intact.

## Stable identity

Keep every identity in the README's Stable accepted terms.
Do not register Internal Fracture.

## Remaining work

Work in this order, since later items depend on earlier ones.

1. Terminal access and commit (Part 8, C01 and C03): keep the government response category usable after `world_end`, and recheck the full gate at the delayed commit.
2. Terminal player choice and unification (Part 8 Player control and Actor unification, C02): let a human dominant actor choose before promotion, make contesting start a real war or rival claimant, and stop automatic subordination of non-jihadist actors.
3. Strategic victory and unity meaning (Part 8 Major strategic victory, Part 4 status, C04).
4. Leadership contest comparison (Part 5 status, C05).
5. Chaos impact map (Part 10 Chaos impact map): remove the per-incident Chaos call from the incident tail and add the milestone rows with their guards, reversal rows and rolling cap.
6. Deaths reasons (Part 10 Deaths system, C11): add the three Event 31 reasons and route each loss to the right one.
7. Valid incident pools (Part 2 Incident selection by stage, C13): filter families before the draw.
8. Famine, migration and camp bridges (Part 10 Famine, migration and camps, Part 3 Coercive response): use the owner seams named in `docs/systems/famine_system.md` and `docs/systems/migration_system.md` and read camp facts only.
9. Supply Collapse rename (Part 5 Captured Economy) with matching idea, localisation and icon wiring.
10. Hostage approach choice (Part 3 The Hostage Deadline).
11. Terminal presentation budget, campaign beats and aftermath (Part 8).
12. Global Jihad geography and Random Pattern mixture (Part 7, C06).
13. Actor forces, capitals, mergers and takeover (Part 5, country matrix, C07 and C08).
14. Scaled costs and maintained commitments (Part 3 Cost design, C09).
15. Evolution I organization identity and support profile (Part 4 status).
16. Forge the Seal staged cores (Part 6 status).
17. Achievement receipts (Part 12 status, C12).
18. Asset follow-ups (Part 11 status): static entity portrait before the revelation, inventory hash refresh, flag-cycle disposition.
19. Catalog: the workbook owner applies [catalog_changes_pending.md](../../plans/031_random_terror_plans/catalog_changes_pending.md), then runs `python .tools/export_event_catalog_csv.py`.

Do not resolve the README open questions on your own.
They wait for a user or parent decision.

## Checks and audits

Use the AI scenario matrix for every changed weight, including `P11_chaos_feedback`, through `chaosx_ai_probability_auditor` with before and after evidence.
Use the decision, country, focus, localisation and completion auditors from [the routing table](031_random_terror_subagent_routing_prompts.md) before any completion claim.
Follow the MCP retry limits in `CLAUDE.md` and record route failures once in the existing plans folder.
Agents do not launch Hearts of Iron IV; live validation belongs to the user.

## Documentation

Update `docs/events/031_random_terror/overview.md` with each change, record new design decisions in the agent decisions file, and update the part's Implementation status section when an item closes.
Keep one current completion report in the plans folder rather than adding new ones.

## Completion report

Report changed files, closed findings, remaining findings, validation limits, and every simplification under `Simplifications, omissions, and blockers`, as `CLAUDE.md` section 5 requires.
