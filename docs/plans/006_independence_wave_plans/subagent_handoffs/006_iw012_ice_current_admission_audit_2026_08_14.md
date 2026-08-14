# IW-012 ICE current bounded admission audit — 2026-08-14

## Disposition

IW-012 is source-backed **static PASS / runtime HOLD**. The package-local country, map-anchor, vanilla-tree carrier, politics, force, ideas, decisions, localisation, asset-reuse, cleanup, and current central-admission references are present. No gameplay file was changed in this audit. No central admission, attestation, preflight, deterministic Join, workbook, commit, or staging operation was performed.

The package remains fail-closed for an admission/completion claim until the parent obtains live allocator, former-host survival, force materialisation, save/load cleanup, route/formable, AI timing, and synchronized transaction evidence.

## Package and identity coverage

| Surface | Current evidence | Status |
| --- | --- | --- |
| Identity | `ICE`, `IW-012`, `RG-100`, Northern and Western Europe, standard depth, port/island archetype in `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv`, `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv`, and `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv` | PASS |
| Tag and history | Reuses installed vanilla `ICE`; no duplicate country, dormant history, state, OOB, or flag was added | PASS |
| Anchor and host | Package trigger requires event target state `100`, owned and controlled by `ROOT`, capital state `100`, a living former host, and the former host's protected state | STATIC PASS; live transaction HOLD |
| Vanilla carrier | `common/national_focus/iceland.txt` keeps `iceland_tree`, its vanilla country gate, and vanilla focus declarations; Event 006 contributes only twelve explicit `shared_focus` imports at lines 28–42 | SOURCE PASS; imported-node visibility HOLD |
| Command roster | Existing `ICE_sveinn_bjornsson` and `ICE_bjorn_sveinsson_bjornsson`; the latter is required as corps commander | PASS |
| Assets | The package manifest records reuse of vanilla ICE flag and male leader/commander portraits; no generated portrait, advisor icon, or fallback asset is used | PASS for source reuse |

The authoritative package-local source files are `common/scripted_triggers/006_independence_wave_ice_package_triggers.txt`, `common/scripted_effects/006_independence_wave_ice_package_effects.txt`, `common/decisions/006_independence_wave_ice_decisions.txt`, `common/decisions/categories/006_independence_wave_ice_categories.txt`, `common/ideas/006_independence_wave_ice_ideas.txt`, `common/ai_strategy/006_independence_wave_ice.txt`, `common/script_constants/006_independence_wave_ice_constants.txt`, `common/national_focus/iceland.txt`, and `localisation/english/006_independence_wave_ice_l_english.yml`.

## Map, state, host, and starting setup

Vanilla `history/states/100-Iceland.txt` confirms owner/core `ICE`, victory point province `12674`, provinces `4861 12674 12689 13266 13267 13268 13271`, infrastructure 1, dockyard 1, naval base 1, and industrial complex 1. Vanilla `history/countries/ICE - Iceland.txt` confirms capital `100`, `ICE_1936` OOB, existing ICE politics/economy/technology setup, and existing dated character roster. Vanilla `history/units/ICE_1936.txt` contains the six-infantry-plus-recon `Ríkislögreglan` template and infantry/support production; IW-012 adds its p12 coastal-maritime force mapping and navy inheritance through the shared force adapter rather than replacing this OOB.

Fresh read-only MCP map inspection selected state `100` and province `12674`. State/region membership, networks, adjacencies, supply nodes, and railways passed for the selected map records. The inspection also reported workspace-wide pre-existing position/port diagnostics (`MAP_BUILDING_POSITION_INVALID` and `MAP_PORT_ADJACENT_SEA_INVALID`) and failed the global position/locator check; these are not IW-012 source changes and were not patched. The parent-provided fresh map receipts are `2bbb0ec…` and map-render `055065…`; the full current map artifact is also recorded by the parent context.

## Politics, leaders, ideas, decisions, localisation, and cleanup

`independence_wave_initialize_ice_politics` seeds the documented ICE popularity profile and promotes the existing vanilla roster. The four route focus consumers select constitutional, traditional, emergency-military, or patron-client politics through `independence_wave_ice_apply_government_route_politics`; no duplicate leader or opposite-gender portrait/name pool is introduced.

The five package ideas are `ice_exposed_north_atlantic_charter`, `ice_north_atlantic_service_compact`, `ice_municipal_shipping_council`, `ice_coastwatch_emergency_command`, and `ice_north_atlantic_patron_mandate`. The package category exposes the timed `independence_wave_ice_hold_the_harbour` mission and six serialized projects: `independence_wave_ice_reconcile_shipping_registers`, `independence_wave_ice_charter_municipal_council`, `independence_wave_ice_expand_coastwatch`, `independence_wave_ice_negotiate_north_atlantic_compact`, `independence_wave_ice_settle_former_host_charter`, and `independence_wave_ice_declare_armed_neutrality`.

The direct IW-012 localisation surface is covered in `localisation/english/006_independence_wave_ice_l_english.yml`, including the category, mission, six projects, five ideas, ledger values, former-host values, Network Standing, and League values. The existing localisation re-audit found no missing direct package keys. Cleanup in `independence_wave_cleanup_iw_012_ice` removes only the package mission, six projects, five ideas, package flags, ledgers, and dynamic former-host AI receipt; it does not remove vanilla ICE history, tree, characters, flag, or cosmetic identity.

## Focus and MCP focus/event receipts

Current `hoi4.focus_inspect` returned `FOCUS_INSPECTED` for `iceland_tree` from `common/national_focus/iceland.txt`, resolving 89 vanilla focus blocks and preserving the vanilla source declarations. Current `hoi4.focus_render` returned `FOCUS_RENDERED` with HTML/SVG/JSON/source-map artifacts. The current receipts are:

- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cc80251942267cad6cd3d4f9a12632506e38cb9478d28e59ab3ccda423706fda/9724e44152c14ec8b88266abfb8ef230e537179f38c01608fb237e2a344e5b0f/focus-inspect.303d822953113564.json`
- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/95154e8f5da333009f0aa0d9e03302abf8c4bdfc454577e0951349844ec34773/a6463ed24ab595974abb85ca3939428e288ee5d541075f918941203d268f0dd0/iceland_tree.focus.html`
- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0f3cd46371e4b568f6b5ffc0dc7c65bedd5339177663eeceda01ca48aec9176f/843daeee66bbd2e903968581823f00991cf71d4fe7f2e74677683982a61d3456/iceland_tree.focus.svg`
- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/187e31ae0a9236c85802d12e354182b9a74c89c268ad0b6b84f9c0cf9b857db7/da7bfcb49c8ea02ef1fecb5aaf0591ca582ecb1e89c1fbe7ab674916f30db652/iceland_tree.focus.json`

The focus inspection reported 193 blocking diagnostics and the render reported 110 blocking diagnostics, including missing generic/vanilla sprite references and the unexpanded shared-focus carrier. These diagnostics are workspace-wide and the imported Event 006 shared nodes were not resolved in the ICE-only render, so additive overlay visibility and route-hook runtime rendering remain HOLD. The parent also supplied fresh focus receipt prefixes `464595…` and `0f3cd…` for the current context. No focus rewrite was attempted.

The Event 006 namespace scan/render used the read-only Event Chain Viewer with `chaosx.nr006`. Both returned partial workspace analyses with no blocking diagnostics in the selected bounded view, but deferred workspace-wide helper/lifecycle projections. Receipts:

- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/61a948a1423b0d0d9aa14729c13ffd28c02fa9a890d8f72e0008f0e5dcc29556/832c15c6a4cf98cff1914f52b53d26c21eea359e3e695d853c59919523bfdf6b/event-scan-741883f50501.json`
- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f0d5e208f8e0c92f1bde6f72d14c6018dda83bfcac73a6f04c8e8ed5ac6830f0/6f9ac6f057c7e5ad0f2b49acffec74eb74e1fb371cac86d90f3fae713993bbe9/event-overview-741883f50501-manifest.json`

The parent also supplied fresh event-render receipt prefix `6467…`. IW-012's package gameplay is primarily decisions and scripted package effects rather than a dedicated ICE event chain, so this receipt does not prove live package setup or cleanup.

## AI and probability receipts

`common/ai_strategy/006_independence_wave_ice.txt` contains four package-gated profiles: coastal survival, shipping registers, former-host charter, and compact. The source contains no hard-coded `DEN` target; former-host diplomacy is dynamically targeted by `independence_wave_ice_apply_host_ai` and reversed by its cleanup helper. Existing package decision and focus AI hooks remain source-backed in the current handoffs.

The mandatory read-only probability pass was attempted through the installed `ai_strategy_factor` and `national_focus_ai_will_do` adapters. `hoi4.probability_inspect` on `common/ai_strategy/006_independence_wave_ice.txt` returned `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason = no_weighted_surfaces`, zero candidates, and zero unresolved inputs: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6e5590eb3d7b53a23f335ee170b320d5ee7876029fc5ea93b0ac99affdfd9140/e27338f53033c798b564985257b7783616d537fd8e115b085d4a9394efda5fdd/probability-inspect-74a34e545404.json`. The focus adapter discovered 184 shared-tree candidates but could not match the four imported ICE route IDs because they live in shared-focus source, not the carrier file: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/96fcd94ea550eaf0c5591187fcde2331082345f8159f9ad58dcbe34087b2d9ae/01514a7e5d969eb0441e4d2a231172d97c80a04065d86a1550aba1aee1641a67/probability-inspect-9374a056d1e6.json`. Decision and AI-strategy source discovery also returned the exact MCP `INTERNAL_ERROR` blocker; no probability compare was fabricated and no weighted source was changed.

## Central authority and Join status

The current central authority is 40 runtime adapters, 32 content attestations, 29 compatible reservation groups, and 161 unattested selectable rows (`40/32/29/161`), with the active `3/4/5/7/10` ladder. Current source checks, read-only only, show IW-012 in the adapter dispatch (`common/scripted_effects/006_independence_wave_package_dispatch_effects.txt:20,52,98`), attestation OR-list (`common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:159-172`), normal/scenario preflight (`:208-250` and `:411-449`), exact tag gate (`common/scripted_triggers/006_independence_wave_package_triggers.txt:479-486` and `common/scripted_triggers/006_independence_wave_package_triggers.txt:1019-1042`), and package load/reservation (`common/scripted_effects/006_independence_wave_packages_region_01_effects.txt:159-162,324-328`).

Deterministic Join remains parent-owned shared authority in `events/006_independence_wave_join.txt` (`chaosx.nr6.36` through `.40`) and `docs/events/006_independence_wave/join_wave.md`. IW-012 appears in the documented 32-package first-success order, but this package audit did not claim live Join execution, synchronized release, or save/load evidence. No central file was edited.

The installed environment did not provide a package-scoped Technology Tree Viewer receipt for this audit; vanilla technology/OOB source review is recorded above, and runtime technology-tree validation remains unresolved as required by the admission contract.

## Remaining blockers and handoff

1. Obtain parent-owned live allocator dry-run/review/apply/post-validation evidence for state `100`, `RG-100`, exact dormant `ICE`, living former-host survival, Event 005 collision, rollback, and save/load.
2. Obtain live force materialisation and navy-inheritance evidence for p12 coastal-maritime setup, plus route/formable and AI timing evidence.
3. Resolve or explicitly waive the current shared-focus MCP expansion/diagnostic limitation before claiming the carrier is visibly accepted in the engine.
4. Keep the global map-position/port diagnostics and missing focus-sprite diagnostics separate from IW-012; this audit did not patch unrelated map or vanilla assets.
5. Re-run a typed probability audit through `chaosx_ai_probability_auditor` for decision AI, imported focus AI, and dynamic host strategy once the MCP adapters accept those package-specific candidate pools.

No safe package-local source gap was proven. No plan handoff was required beyond this current audit. Nothing needs committing; the only new file is this durable handoff.
