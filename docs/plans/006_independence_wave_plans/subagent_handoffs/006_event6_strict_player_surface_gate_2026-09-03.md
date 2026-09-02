# Event 006 strict player-surface gate — 2026-09-03

## Scope

This bounded repair closes the remaining Event 006 pre-event visibility path in the shared `is_independence_wave_event6_player_surface_allowed` trigger. The separate Event 021 package-content predicate remains available for internal adapter setup and effect consumers, but it cannot publish Event 006 categories or decisions.

## Source change

`common/scripted_triggers/006_independence_wave_triggers.txt` now requires `is_independence_wave_active_country = yes` before the shared player-surface helper can succeed. The existing adapter-receipt exclusions remain in place for preparation, completion, origin-neutral completion, and proven setup receipts.

This keeps the accepted boundary absolute: before the public `chaosx.nr6.1` firing path creates an active Event 006 origin, no Event 006 category, mission, cost, queue, pressure, or other player-facing indication can be exposed through the shared helper. The adapter-aware `is_independence_wave_package_content_active` trigger is intentionally unchanged for non-player-facing setup and effect work.

## Validation and limits

The strict allocator audit reports the retired pre-event crisis surface with no category, mission, cost, or queue. The Event 006 decision/category source audit reports all 88 categories gated either directly by the active-origin predicate or through this helper. The Event MCP route remains a partial workspace projection; no live-game or save/load claim is made here.

No package admission, automatic count, cost debit, portrait, flag, asset, Event 021 gameplay, or runtime release behavior changed in this tranche.
