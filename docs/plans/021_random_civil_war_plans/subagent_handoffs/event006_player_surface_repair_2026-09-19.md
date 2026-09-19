# Event 021 Event 006 player-surface gate repair — 2026-09-19

Disposition: implemented for test entry; runtime package reachability and final acceptance remain open.

The completion audit found a source contradiction in the Event 006 public gates. The Event 021 acceptance ledger and improvement disposition described complete human Event 021-origin packages as eligible for the reused Event 006 focus, category, and decision surfaces, but `common/scripted_triggers/006_independence_wave_triggers.txt` still required `is_independence_wave_active_country` for both public predicates.

The current source now resolves that contradiction in the direction required by the accepted Event 021 package contract:

- `is_independence_wave_event6_local_content_active` admits either a real active Event 006 origin or `is_independence_wave_event021_package_country`.
- `is_independence_wave_event6_player_surface_allowed` admits the same two complete paths.
- The Event 021 path is fail-closed because `is_independence_wave_event021_package_country` requires a normal human country, complete adapter and origin receipts, a package id, no active Event 006 origin, and no ended Event 006 origin.
- The transient `random_civil_war_event6_adapter_preparing` path remains excluded from the player surface.
- No Event 006 fired marker, evolution, league, network, or normal-origin state is set by this predicate change.

The change is limited to `common/scripted_triggers/006_independence_wave_triggers.txt`; it reuses the existing Event 006 category, decision, and focus consumers and introduces no duplicate package, character, tag, asset, or lifecycle state.

Validation is source-level only in this handoff. A fresh `hoi4.event_inspect` lint after the repair returned `EVENT_INSPECTED_PARTIAL` at revision `d210fa95a760b0a1e5ef406659ecb3ca39ac7887f2f983a0767bec4c0b14fad4`, with zero blocking diagnostics and zero skipped sources; the linked artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4ff5b16f56878cfd2a431bc06a8c5c3bd6e95cad1f37882e7754b8ee3d6d88a7/01a5d9cbc262cf5523120c1e50e4e29f18d1446ba61cd57351264b1c32b467cd/event-lint-d210fa95a760.json`. The result remains partial because the installed MCP defers workspace-wide helper and lifecycle projection. The admitted 32-package Event 021-origin runtime matrix, focus-loading reachability, save/reload behavior, asset provenance, and player-owned live validation remain testing gates. IW-095 and every incomplete or actual nonhuman package remain excluded by the existing Event 021 adapter predicate.

This repairs the B01 source mismatch identified by the 2026-09-19 completion audit; it does not close the inherited Event 006 package, portrait, probability, or runtime evidence gates.
