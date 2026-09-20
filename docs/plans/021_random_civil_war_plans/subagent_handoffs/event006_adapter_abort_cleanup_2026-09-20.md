# Event 021 Event 006 adapter abort cleanup

Date: 2026-09-20.

Disposition: **implemented for the bounded source tranche; runtime certification remains queued under `Needs Testing`.**

## Scope

The Event 021 adapter can prepare a complete dormant Event 006 package before the actor's war is proven. A failed primary or additional-front attempt previously cleared Event 021 flags and annexed a newly released carrier, but did not explicitly run Event 006's documented generation-local reset on the actor. That left a source-level risk that package ideas, decisions, force mappings, or other partial generation state could survive an abort, especially when the selected carrier was an existing dormant country.

## Implementation

`event021_parent_prepare_event6_adapter_actor` now sets the Event 021-owned `random_civil_war_event6_adapter_setup_attempted` marker while the shared package-only preparation window is open and snapshots a pre-existing Event 021 generation value when present.

`event021_parent_cleanup_failed_event6_adapter_actor`, called by `event021_parent_abort_event6_opening` and `event021_parent_abort_event6_secondary_front`, runs `independence_wave_reset_current_generation` in the selected actor scope while the marker is present, restores the prior Event 021 generation value when one was saved, and clears Event 021 package, opening, route, and crisis transaction variables before clearing adapter flags or annexing a newly released carrier. This is the existing Event 006 reset contract: it dispatches package cleanup, clears generation-local force, decision, focus, active/network/league, origin-idea, and package state, and preserves historical ledgers. No Event 006 firing state, generation sequence, evolution, or league admission is opened by this repair.

`event021_parent_clear_event6_package_transaction` clears the attempt marker and generation snapshot on the selected actor after a successful opening or ordinary rollback. The marker is not a package readiness flag and does not make a carrier selectable.

## Validation

The touched parent effect file has balanced script delimiters and no unsupported `<=` or `>=` operators. The focused read-only `hoi4.event_inspect` lint for `chaosx.nr21.1` returned `EVENT_INSPECTED_PARTIAL`, zero blocking diagnostics, and zero skipped sources at revision `a8fde3e58546f004e81d855d73d29674ae3c5be8f894a1caf9586621929a6657`; artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6010d8e4738e1b479fa8f213c797894ee81d0725da52e6412013f650d83bab5b/56607bcee413125a78e01bbd132146fe99d3e5993da9f01e5c01e830447322f6/event-lint-a8fde3e58546.json`.

The MCP result remains partial because the large workspace defers helper-expanded lifecycle validation. No live game, save/reload, or Event 006 package runtime test was run. The 32-package runtime/asset matrix remains open.

## Remaining risk

The cleanup contract is source-repaired but not live-proven for both a newly released carrier and every pre-existing dormant carrier. The ordinary-successor external-war continuity gap remains separately blocked because installed documentation does not expose a same-war identity or prove post-annex preservation through `add_to_war`.
