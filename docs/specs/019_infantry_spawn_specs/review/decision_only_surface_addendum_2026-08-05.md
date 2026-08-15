# Event 019 Decision-Only Surface Addendum

This addendum records the accepted player-facing surface change requested on 2026-08-05: Event 019 no longer uses a custom scripted GUI. The ordinary-country formation management category and the separate claimant category are the complete player interaction surfaces.

The shared Event 019 selection caches and scripted effects remain because they are gameplay state, not a window. They keep lot, generation, family, claimant, cost, AI, and cleanup transactions aligned. Their historical `infantry_spawn_muster_gui_*` variable names remain save-compatible and are not exposed as a runtime interface.

The former GUI opener is replaced by `infantry_spawn_review_formation_ledger`. Evolution IV countries with more than one eligible registry family can use `infantry_spawn_cycle_anomalous_family_decision`, and countries with more than one live claimant file can use `infantry_spawn_cycle_claimant_file`. These decisions only rebuild or move the shared selection cursor; every substantive action remains an ordinary decision with its own requirement, cost, effect tooltip, and AI gate.

The decision category retains the existing lifecycle gate. It disappears after the country has no unresolved or unaccounted Event 19 work, no live recorded formations, no active claimant or anomalous family transaction, and no pending management operation. The claimant category remains conditional on the claimant system and live claimant rows. Existing pulse and cleanup effects continue to clear selection caches when the crisis becomes irrelevant.

The Muster Board family cache invokes each aligned provider's `event19_get_management_cost_display` callback after management eligibility is evaluated. The callback writes only a presentation profile (`0-18` for provider-specific cost text or `99` for a ledger-backed zero-debit adapter); it does not debit resources or replace the provider payment/refund contract. Any profile `99` row must tell the player that its obligation is tracked by the Event 19 ledger rather than directly removed from the displayed stockpile.

The runtime files `common/scripted_guis/019_infantry_spawn_muster_board_scripted_gui.txt` and `interface/019_infantry_spawn_muster_board.gui` and their seven runtime-only DDS consumers were removed. The generated background, frame sheets, static fallbacks, and their production manifests remain archival provenance under `docs/assets/019_infantry_spawn/`; they are not runtime fallbacks or active Event 019 controls.

No gameplay route was removed by this surface change. Generation, diminishing coverage, weighted lots, equipment accounting, Muster Control, Army Congestion, integration, demobilization, claimant takeover/revolt, dynamic Chaos-family registry dispatch, train-versus-spawn rules, containment, saturation, derivative revolt creation, AI, achievements, scenario bypasses, Event Log integration, and defeat cleanup continue to use the same effects and decision contracts.
