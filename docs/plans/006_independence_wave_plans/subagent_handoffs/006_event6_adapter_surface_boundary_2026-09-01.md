# Event 006 adapter surface boundary handoff

Date: 2026-09-01

## Scope

The Event 006 category registry now blocks every non-origin-gated category while an Event 021 country is using the origin-neutral Event 006 package adapter.

## Finding

`is_independence_wave_package_content_active` is intentionally adapter-aware so Event 021 can consume package leaders, forces, and setup content without creating an Event 006 origin. Several formable, phase, and overlay category predicates do not themselves require `is_independence_wave_active_country`, so a transient adapter receipt could otherwise publish a player-facing category.

## Change

Added `is_independence_wave_event6_player_surface_allowed` to `common/scripted_triggers/006_independence_wave_triggers.txt`. It fails while any Event 021 adapter preparation or completion receipt is present: `random_civil_war_event6_adapter_preparing`, `random_civil_war_event6_adapter_complete`, `random_civil_war_origin_adapter_complete`, or `independence_wave_event021_adapter_setup_proven`.

Applied the guard to all 36 Event 006 category blocks that do not already require the strict active-origin predicate, including recognition/patron/formation categories, formable family surfaces, overlay categories, the rival-bloc and scenario ledgers, and FORM-16 integration. Existing package-specific categories remain directly origin-gated.

## Preservation

The adapter still uses `is_independence_wave_package_content_active` for package setup and content validation. Normal Event 006 countries and post-formation member surfaces are unchanged because the new guard only rejects the four transient adapter receipts.

No decision costs, missions, queue/pressure content, allocator admission, package attestation, release logic, or Event 021 effect flow changed.

## Evidence

The category parser found 88 Event 006 category blocks with no block lacking either the strict active-origin gate, the adapter-surface guard, the overlay runtime gate, or the explicit SCN-008 publication gate.

Focused validators passed: allocator, country API, strict flags, FORM-16, SCN-008 scenario matrix, and GUI semantic matrix.

The required Event MCP route remains partial and no live game or save/load proof is claimed.

## Remaining risk

Source checks cannot prove behavior after an interrupted Event 021 effect chain leaves stale receipt flags. Existing Event 021 abort and absorbed-adapter cleanup remain the cleanup owners; the guard intentionally fails closed until those receipts are cleared.
