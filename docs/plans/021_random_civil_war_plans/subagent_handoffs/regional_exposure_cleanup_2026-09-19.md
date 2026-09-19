# Event 021 regional exposure cleanup repair — 2026-09-19

## Disposition

Implemented in the current Event 021 test-entry source. Final acceptance remains open because the live exposure-expiry and settlement sequence is not available to the agent.

## Source change

`event021_parent_review_exposure_lifecycle` is now called from `event021_global_review_current_country`, after the bounded current-country review. It checks the existing `event021_country_can_manage_exposure` source-validity contract and calls cleanup only for a country carrying an active or presentation exposure marker whose source is no longer live and usable.

`event021_cleanup_regional_exposure` now removes the exposure presentation marker, the stale-source receipt, route-ready flags, review and presentation receipts, containment/mediator/sponsor role profiles, separate relief and armed-support state, neighbor-action state, mediation/relief/border-monitoring state, and saved source/channel variables. The existing exposure registry removal and centralized cooldown remain unchanged.

## Files changed

- `common/scripted_effects/021_random_civil_war_effects.txt`
- `common/scripted_effects/021_random_civil_war_parent_effects.txt`
- `common/scripted_effects/021_random_civil_war_effects.md`
- `common/scripted_effects/021_random_civil_war_parent_effects.md`
- `docs/events/021_random_civil_war/acceptance_evidence.md`
- `docs/plans/021_random_civil_war_plans/source_of_truth_map.md`

## Evidence

The touched effect files have balanced braces and no unsupported comparison operators. The refreshed focused `hoi4.event_inspect` lint for `chaosx.nr21.1` returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics and zero skipped sources at revision `dec87bc5349e92d00e2affee2cb645e0aa4f9f91aad80ed2cf5a584674fef0f7`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d9efd5e0461b81f9c34400c27fd66cf4f225f5a8335ac8c8e6d247b3159a71cf/854b4999ea10d00d16bdc6acb6128054189b07786641c8cd20f0bb4dd7dbb6f3/event-lint-dec87bc5349e.json`.

## Remaining risk

The repair is not a substitute for live verification that a source war ending, settlement, annexation, or evolution disablement reaches this bounded review before a neighbor action is offered again. The large-workspace MCP state-flow projection remains deferred, and user-owned live testing is still required.
