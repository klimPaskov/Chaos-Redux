# Event 006 absent-target release validation repair — 2026-08-27

## Status

Completed a narrow source repair for the standalone Independence Wave transaction when a selected registered country tag has not yet been instantiated. No live game, save/load, or in-engine country-release result is claimed.

## Finding

The release planner intentionally stores selected Event 006 countries in the active aligned plan arrays before any country exists, but the shared frozen-plan validator required every selected country and every selected state owner to carry a durable country flag and metadata variables. An uninstantiated tag cannot retain those country-scoped markers, so validation rejected an otherwise valid frozen plan before the release loop could create the countries and transfer their states.

The pasted `capital_scope` diagnostics identify pre-consolidation Banat, Thrace, and Epirus trigger files that are no longer present in the current source tree. The generic Event 006 provisional-phase trigger also dereferenced `capital_scope`, which is invalid for an empty dormant shell before its capital state is transferred.

## Source changes

- Updated `liberation_release_validate_set_invariants` in `common/scripted_effects/chaosx_liberation_release_effects.txt` so an Event 006 state row may satisfy the reservation receipt through active plan-array membership, while other plan owners still require their durable reservation marker and metadata.
- Updated `liberation_release_validate_country_rows` in `common/scripted_effects/chaosx_liberation_release_effects.txt` with the same owner-gated Event 006 array receipt, preserving strict marker and metadata validation for Event 005 and for non-array-backed rows.
- Replaced the generic `capital_scope` gate in `can_independence_wave_enter_provisional_phase` with `has_independence_wave_current_capital_controlled_by_root`, which checks an owned capital state and fails closed for a dormant shell without constructing an invalid capital target.

## Invariants

The array receipt is accepted only when the active plan owner is `constant:liberation_plan_owner.independence_wave`, and the state invariant still requires the target to be present in `global.liberation_plan_countries`. Existing dormant shells and living countries continue through the durable reservation and living-tag checks. The hidden `chaosx.nr6.1` event remains the standalone transaction entry point, and the public report remains gated on a committed non-empty plan.

## Evidence

Focused checks passed after the patch: `python -B .tools/audit_event6_allocator.py`, `python -B .tools/audit_event6_country_api.py`, `python -B .tools/audit_event6_flags.py --strict`, `python -B .tools/audit_event6_form16.py`, and `python -B .tools/audit_event6_scenario_matrix.py`.

The touched Clausewitz files have balanced blocks and no diff whitespace errors. Fresh read-only `hoi4_event_inspect` and `hoi4_event_render` calls for `chaosx.nr6.1` returned partial results with zero blocking diagnostics; the server deferred large helper and lifecycle projections and emitted only the workspace inline-file truncation notice.

## Remaining risk

The user must verify `event chaosx.nr6.1` in a live session to confirm country instantiation and state transfer. Whole Event 006 remains HOLD/PARTIAL because package attestation, deferred MCP helper/lifecycle projections, weighted AI/probability audit, GUI evidence, and live runtime validation are outside this narrow repair. No fallback package, pre-event crisis surface, or new decision category was added.
