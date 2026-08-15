# Event 006 pre-event crisis specification supersession

Date: 2026-08-15.

## Decision

The later user decision supersedes the original Part 2 and Part 3 pre-wave crisis design. Before the public Event 006 report fires, the player-facing state is intentionally empty: no pressure category, mission, cost, queue, history row, or other indication of an early wave request may appear.

Pressure, stability, resistance, occupation, or host conditions do not imply that the Independence Wave has begun. The normal Event 006 decision and mission map becomes available only after the public event has created an active Event 006 origin, subject to the existing package and origin gates.

## Source reconciliation

The current implementation already deleted `common/decisions/006_independence_wave_crisis_decisions.txt` and `common/decisions/categories/006_independence_wave_crisis_categories.txt`, removed the crisis cost and player-facing strings, and hard-disabled `can_independence_wave_open_crisis` in `common/scripted_triggers/006_independence_wave_crisis_triggers.txt`.

This follow-up reconciles the user decision into the accepted source package by replacing the active crisis sections in Part 2 and Part 3, the coding prompt, the acceptance checklist, and the manual improvement-loop review. The catalog handoff now carries an explicit superseding note; older crisis paragraphs and dated handoffs remain historical traceability only.

## Files updated

- `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_2_event_flow_and_evolutions.md`
- `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_3_mechanics_and_decisions.md`
- `docs/specs/006_independence_wave_specs/prompts/independence_wave_coding_prompt.md`
- `docs/specs/006_independence_wave_specs/quality/spec_acceptance_checklist.md`
- `docs/specs/006_independence_wave_specs/quality/manual_improvement_loop_review.md`
- `docs/specs/006_independence_wave_specs/quality/catalog_alignment_handoff.md`

## Boundaries

The post-event synchronized allocator, host-survival covenant, Event 005 collision order, active-origin decision categories, Join system, and ordinary Event 006 public report are unchanged. Legacy crisis effects, constants, hidden callback, and scripted localisation remain only for parser and historical compatibility; they are not a player-facing mechanic and must not receive new callers.

## Validation target

The source package should contain no current active specification or prompt that instructs a future implementation to restore the pre-event crisis surface. Historical plans and handoffs may still mention the superseded design when their dates and status make that traceability explicit.
