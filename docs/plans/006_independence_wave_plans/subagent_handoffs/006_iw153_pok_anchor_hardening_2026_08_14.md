# IW-153 POK dormant anchor hardening — 2026-08-14

## Scope

This bounded source repair strengthens the dormant IW-153 POK compatibility contract without admitting the package or changing any central dispatcher, attestation, preflight, scenario, or Join list.

## Source change

`common/scripted_triggers/006_independence_wave_iw153_pok_compatibility_triggers.txt` now requires the Event 006 country to both own and control state 334 in `has_independence_wave_iw_153_pok_compatibility_contract`, alongside the existing capital-scope, core, releasable, character, origin, and package-identity witnesses.

This matches the anchor witness pattern used by the adjacent dormant compatibility adapters and prevents a capital-only predicate from being treated as a current-map preservation proof.

## Boundary

IW-153 remains dormant and fail-closed. No POK state transfer, core mutation, leader recruitment, flag or portrait installation, central adapter/attestation widening, preflight change, scenario admission, or Join change was made.

## Validation

The edited trigger block is balanced and `git diff --check` reports no whitespace errors. The existing POK preservation audit remains the source of truth for identity, vanilla-origin, map, and admission blockers.

## Fresh MCP and authority receipt

The required bounded `hoi4.map_inspect` rerun for states 334 and 1022 returned `MAP_INSPECTED` at revision `0248b8dd4ff1d992312f3d0e49c628dc738b14e529d465b8515959803888fb01`.

The selected-state checks passed for map files and definitions, bitmap geometry, state and region membership, and networks and adjacencies.

Aggregate locator validation remains false because the workspace contains unrelated `MAP_BUILDING_POSITION_INVALID` and `MAP_PORT_ADJACENT_SEA_INVALID` diagnostics in `map/buildings.txt`.

The linked inspection artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1e9b85939a1af50893c3e98ec5954f5ddbb666e517c758d094b4ea12f1f82a25/35baef5e7a42de55f0ff5f54851c630d43045bf02184419dfe98605bed5f6ba7/map-inspect.0248b8dd4ff1d992.json`.

The paired owner-layer `hoi4.map_render` returned `MAP_RENDERED` with validation passed.

The render artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/af3d3fda685bb991339113baa527a49fc94a78351081bbf2f6e73f9465b2b2ef/60db99bd59bb732e6f6a50f82a055fc920789b7be3a26fe39ac9c622fb24b4a9/map-owner.png`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9730eda315d13bc333999519b092f78cff3b6df2192a136c87e203c147728b90/fa56eef8513a7f8f9decb2fd1d06cfb32df02db70faafa45c882da4acad84437/map-owner.json`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b1edaa7f920a7522830ba8e5c2af16c3d57612cc78e38ff8f05ffacba104b2ef/3fcfd2b81769548bf643b60728fdd03d4590ba3e76c34b29e1b452c83ecf300e/map-owner.html`.

The allocator, SCN-008 scenario matrix, flag-family, and country-API audits still pass with 149 publishers, 40 runtime adapters, 32 attestations, 29 compatible groups, 161 unattested rows, and the `3/4/5/7/10` ladder.

These receipts strengthen the dormant anchor witness only.

IW-153 remains unbound and fail-closed because named-community identity, leader and portrait provenance, flag evidence, complete package mechanics, and central admission evidence are still absent.
