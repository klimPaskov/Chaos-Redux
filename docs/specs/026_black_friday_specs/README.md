# Event 26: Black Friday specification package

Current workflow owners: [event integration](../../../.claude/skills/chaos-redux-events/SKILL.md), [subagent routing](../../../.claude/skills/chaos-redux-subagents/SKILL.md), and [asset production](../../../.claude/skills/chaos-redux-event-assets/SKILL.md).
The source parts preserve the proposed expanded design.
Explicit user requirements retain their cited basis, while broader claims labelled accepted require an attributable user decision or parent acceptance before implementation.
Package location and manual closure reports do not establish that acceptance.

This folder is the source specification package for Event 26, **Black Friday**. Its repository location is `docs/specs/026_black_friday_specs/`.

The package maps replacement of the desert-industry concept from the supplied pre-implementation snapshot, as recorded in Part 9. Event ID `26` remains a Minor Fire-Once event. Its player-facing identity, implementation contract, event-log wiring, assets, catalog entry, and localisation must all change together.

## Design result

Black Friday becomes a global one-day sale that can enter the random-event pool at Gathering Storm, which begins at 200 chaos. Once selected, the event is reserved and waits for an eligible in-game Friday. It fires on that Friday, snapshots either a 50 percent or 75 percent discount, applies the sale to every registered purchase cost, and expires on the next daily tick.

The central implementation goal is a reusable cost quotation and payment framework. Dynamic cost surfaces use the shared framework directly. Static but script-reachable surfaces receive complete event-aware variants or conditional adapters. Engine-inaccessible surfaces must be documented with exact evidence. A short sample of discounted actions does not satisfy the specification.

## Package map

1. `026_black_friday_spec_part_1_event_identity_and_player_experience.md` defines the event premise, player loop, balance role, and visible behavior.
2. `026_black_friday_spec_part_2_friday_reservation_and_lifecycle.md` defines selection, reservation, timing, cancellation, save persistence, and event-system pacing.
3. `026_black_friday_spec_part_3_reusable_cost_modifier_architecture.md` defines the shared payment ratio, quotation, rounding, composition, payment, and refund contracts.
4. `026_black_friday_spec_part_4_cost_surface_coverage.md` defines the coverage boundary, cost families, adapter classes, and audit requirements.
5. `026_black_friday_spec_part_5_ai_multiplayer_balance_and_exploit_controls.md` defines AI behavior, multiplayer synchronization, balance limits, and abuse prevention.
6. `026_black_friday_spec_part_6_event_logs_evolution_and_presentation.md` defines the event chain, Event Details, evolution logging, active status, and writing direction.
7. `026_black_friday_spec_part_7_assets_and_achievement.md` defines the required visual assets and the event achievement.
8. `026_black_friday_spec_part_8_acceptance_scenarios.md` defines implementation and live-test scenarios.
9. `026_black_friday_spec_part_9_implementation_crosswalk.md` maps the specification to current repository surfaces and completion evidence.
10. `026_black_friday_cost_surface_registry_template.md` provides the required coverage ledger structure.
11. `026_black_friday_asset_prompt.md`, `026_black_friday_achievement_prompt.md`, `026_black_friday_coding_prompt.md`, and `026_black_friday_goal_prompt.md` are historical build contracts for the installed implementation.
12. `026_black_friday_catalog_update_brief.md` defines the authoritative workbook change.
13. `026_black_friday_improvement_loop_closure.md` records the anti-bloat review and closure decision.
14. `026_black_friday_source_reading_record.md` records the complete provided-source review.
15. `026_black_friday_subagent_review_record.md` records the role-based subagent review.
16. `PACKAGE_MANIFEST.md` records final file sizes, hashes, and package integrity notes.

## Authority and implementation state

The specification files in this folder are source design.
Particular accepted amendments retain their recorded user decision, including the 2026-09-25 native-raid achievement rule.
The remaining expanded design requires the acceptance basis described above. Working audits and implementation handoffs should go under `docs/plans/026_black_friday_plans/`.

This package contains design and implementation requirements.
Event 26 is implemented at source level (`events/026_black_friday.txt`, overview in `docs/events/026_black_friday.md`), but the workstream is incomplete: the D36 stale-contribution defect, partial owner adoption, queued catalog wording and engine acceptance remain open in [the takeover status](../../plans/026_black_friday_plans/takeover_status_2026-10-06.md).
The downstream prompts are historical build contracts.

## Completion rule

Implementation is incomplete while any discovered Vanilla or Chaos Redux purchase surface lacks a recorded coverage disposition, any displayed price differs from the paid price, the Friday reservation can duplicate or stall event pacing, the one-day expiry leaves stale discounts, or the old desert-industry identity remains anywhere in active files or player-facing documentation.

## Open questions

1. Native sale as an ordinary cost modifier (proposed, spec audit 2026-10-10).
   Part 1 asks every surface to charge exactly 50 or 75 percent of its current payable cost.
   Native purchase surfaces (laws, advisors, military staff) compose their price inside the engine, so Event 26 stores a compensating contribution at activation, and D36 shows that contribution goes stale when ordinary factors change during the day, which can even reach a zero price.
   Proposal: for native surfaces only, apply the sale as one temporary additive cost-factor modifier (`-0.50`, or `-0.75` at Chaos Tier) and describe it as "half price" or "a quarter of the price" before other modifiers, accepting that stacked native factors make the final price approximate.
   The displayed native price still equals the paid price, the stored-contribution machinery and the D36 blocker disappear, and script-reachable Chaos Redux costs keep the exact quotation framework.
   This changes the exact-ratio rule for native surfaces, so it needs user acceptance.
2. No other design change is proposed.
   The 8 October review retained reservation, one-day activation, live cost composition, paid-amount refunds and action validity, and rejected a sale store, extra currency or purchase cap; this audit agrees.

## Changelog

- 2026-10-10 spec audit, pass 1:
  - Replaced the stale "not implemented" statement with the current source-level state and a pointer to the takeover status.
  - Marked the coding, goal, asset and achievement prompts as historical build contracts.
  - Repointed workflow-owner links from the ignored `.agents/skills/` mirror to `.claude/skills/` and refreshed the manifest hashes for the changed files.
- 2026-10-10 spec audit, pass 2:
  - Added the native-surface modifier proposal that would remove the D36 blocker.
