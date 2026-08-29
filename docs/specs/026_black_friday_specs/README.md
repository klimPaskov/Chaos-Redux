# Event 26: Black Friday specification package

This folder is the source specification package for Event 26, **Black Friday**. It is intended to be placed at `docs/specs/026_black_friday_specs/` in the Chaos Redux repository.

The package replaces the existing Event 26 concept and script that move industry into desert states. Event ID `26` remains a Minor Fire-Once event. Its player-facing identity, implementation contract, event-log wiring, assets, catalog entry, and localisation must all change together.

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
11. `026_black_friday_asset_prompt.md`, `026_black_friday_achievement_prompt.md`, `026_black_friday_coding_prompt.md`, and `026_black_friday_goal_prompt.md` provide bounded downstream prompts.
12. `026_black_friday_catalog_update_brief.md` defines the authoritative workbook change.
13. `026_black_friday_improvement_loop_closure.md` records the anti-bloat review and closure decision.
14. `026_black_friday_source_reading_record.md` records the complete provided-source review.
15. `026_black_friday_subagent_review_record.md` records the role-based subagent review.
16. `PACKAGE_MANIFEST.md` records final file sizes, hashes, and package integrity notes.

## Authority and implementation state

The specification files in this folder are the accepted design source when implementation begins. Working audits and implementation handoffs should go under `docs/plans/026_black_friday_plans/`.

This package contains design and implementation requirements. It does not claim that Event 26 has been implemented, tested in game, or entered into the authoritative catalog workbook.

## Completion rule

Implementation is incomplete while any discovered Vanilla or Chaos Redux purchase surface lacks a recorded coverage disposition, any displayed price differs from the paid price, the Friday reservation can duplicate or stall event pacing, the one-day expiry leaves stale discounts, or the old desert-industry identity remains anywhere in active files or player-facing documentation.
