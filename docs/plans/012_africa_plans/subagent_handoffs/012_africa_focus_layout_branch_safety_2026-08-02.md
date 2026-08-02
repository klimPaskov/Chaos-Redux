# Event 012 Africa focus layout branch-safety audit

Date: 2026-08-02

Status: bounded audit complete. One narrow layout-refresh patch was applied. The authored overlay coordinates were not moved.

## Scope and sources

The audit covers `common/national_focus/012_africa_continental_focus_tree.txt`, its regional and constitutional branch predicates, the continental focus loader and layout-refresh helpers, and the related focus architecture handoffs.

The offline focus documentation was checked in `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md`. Its `allow_branch` example uses a focus branch whose visibility is changed at runtime and explicitly refreshes the tree with `mark_focus_tree_layout_dirty` or a same-tree `load_focus_tree` with `keep_completed = yes`. Installed vanilla effect documentation describes `mark_focus_tree_layout_dirty` as forcing a refresh of the scoped country's tree layout at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md:4811-4820`.

Vanilla precedent exists in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/national_focus/congo.txt:6160-6300`: six mutually exclusive country-flag branches use the same `(x = 0, y = 2)` position relative to one parent. This is the same branch-local coordinate pattern used by the Africa overlays.

## MCP evidence

`hoi4.focus_inspect` returned `FOCUS_INSPECTED` for `africa_continental_focus_tree` with `focusCount = 276`, `resolvedTitleCount = 276`, and no changed files. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/21ed3979886edefc2814d162ee3c3cc77107d9a61234680d43895c32cc2b498f/168e415d2f051aa25d60e23f38540e9bba0a8e380c38fdd73a17ff25b9d8f845/focus-inspect.ad3f1cdf80579eb4.json`.

The inspector reports `validation.passed = false` with `570 blocking focus diagnostics`. The authored layout metrics are 348 connectors, 448 connector crossings, 1,028 node intersections, 37 long connectors, 235 same-row pairs, and 55 same-row spacing conflicts. The inspector reports `branchCount = 0`, so it is evaluating the static source graph without evaluating the country-scoped `allow_branch` predicates.

Representative diagnostics are:

| Diagnostic | Coordinates | Focus IDs | Source area |
| --- | --- | --- | --- |
| `FOCUS_DUPLICATE_COORDINATE`, `FOCUS_LAYOUT_COORDINATE_CONFLICT`, `FOCUS_LAYOUT_VISIBLE_OVERLAP` | `(12, 2)` | `africa_maghreb_sahara_face_divided_sovereignty`, `africa_congo_basin_transfer_authority_from_concessions`, plus the Great Lakes and Madagascar overlay peers | `012_africa_continental_focus_tree.txt:321-767` |
| Same diagnostic family | `(8, 3)` | `africa_maghreb_sahara_join_coast_and_caravan`, `africa_congo_basin_open_the_river_rail_spine`, plus the Great Lakes and Madagascar overlay peers | `012_africa_continental_focus_tree.txt:338-784` |
| Same diagnostic family | `(16, 3)` | `africa_maghreb_sahara_prepare_the_first_guarantee`, `africa_congo_basin_protect_the_first_basin_partner`, plus the Great Lakes and Madagascar overlay peers | `012_africa_continental_focus_tree.txt:355-801` |

A source-coordinate census finds six repeated overlay bands, each containing all nine overlay variants: `(12,2)`, `(8,3)`, `(16,3)`, `(8,4)`, `(16,4)`, and `(12,5)`. The remaining duplicate groups come from the intentionally templated constitutional branches and relative-position layouts. These are static graph collisions, not duplicate focus IDs.

## Branch exclusivity and refresh proof

The nine overlay focuses use `allow_branch = { africa_focus_uses_*_overlay = yes }` in `common/national_focus/012_africa_continental_focus_tree.txt:323-1265`.

The nine predicates in `common/scripted_triggers/012_africa_triggers.txt:642-687` each require `africa_is_current_host = yes` and equality against one `africa_overlay` constant. The constants are `none = 0` and nine distinct values `1` through `9` in `common/script_constants/012_africa_constants.txt:240-256`. The host classifier assigns one mapped value in `common/scripted_effects/012_africa_effects.txt:319-373`. For a valid mapped host, at most one overlay predicate can be true. An unmapped `none = 0` host shows no overlay rather than two overlays.

The six grounded route openers are also mutually exclusive in the focus source. For example, `africa_federal_representation_before_merger` excludes the other five grounded openers at `012_africa_continental_focus_tree.txt:1382-1406`, and the other roots use the same reciprocal pattern. Hidden Covenant reveal and commitment are gated by `africa_focus_can_reveal_covenant` / `africa_focus_shows_covenant_route`; its reveal and commitment effects refresh the tree at `common/scripted_effects/012_africa_focus_route_effects.txt:233-259`.

The canonical continental loader marks the layout dirty after initial activation at `common/scripted_effects/012_africa_effects.txt:1418-1451`. Route commitment and Covenant reveal also refresh the layout. RSA successor transfer calls the canonical loader and an explicit refresh after transfer at `common/scripted_effects/012_africa_rsa_effects.txt:1016-1023`.

## Narrow patch

Compact promotion changes `africa_host_depth` from `compact` to `promoted`, which makes the four full host-signature focuses visible through `africa_focus_shows_full_host_signature`. The decision previously called `africa_promote_compact_host_package` without refreshing the focus layout, so the newly eligible branch could remain stale until another refresh.

Changed file: `common/scripted_effects/012_africa_effects.txt`.

Changed identifier: `africa_promote_compact_host_package` now calls `africa_refresh_continental_focus_tree_layout = yes` inside its successful promotion branch at lines 1382-1394.

Before: promotion changed host depth and package flags but did not invalidate the focus layout.

After: successful promotion changes the host depth and immediately forces the active continental tree to reevaluate branch visibility. The helper is guarded by `africa_is_current_host` and `has_focus_tree = africa_continental_focus_tree`, so it is a safe no-op outside the loaded host tree.

## Route and layout coverage

| Surface | Source coverage | Assessment |
| --- | ---: | --- |
| Shared opening | 16 focuses | Present and ordered through first proof, congress, and constitutional principle. |
| Regional overlays | 9 x 6 = 54 focuses | Present; branch predicates are mutually exclusive for mapped hosts and intentionally share six coordinate bands. |
| Charter federalism | 21 focuses | Present with route root, choices, crisis, recovery, and capstone. |
| Continental republic | 21 focuses | Present with civic, election, executive, and regional acceptance branches. |
| Council of crowns | 21 focuses | Present with succession, restoration consent, and Charter settlement. |
| People’s union | 21 focuses | Present with planning, food continuity, administration, and host-privilege outcomes. |
| Military continentalism | 21 focuses | Present with command architecture, commander crisis, handover, and civilian mandate. |
| Confederation | 21 focuses | Present with voting, free-rider, lawful refusal, withdrawal, and capstone. |
| Hidden Covenant | 18 focuses | Present and reveal-gated; grounded-origin history is retained by design. |
| Shared support | 36 focuses | Present and dispatched through route-sensitive reward helpers. |
| Host/formation/post-formation | 26 focuses | Present, including full/compact signatures and Charter League settlement. |
| Matrix payoff anchors | 78/78 | All stable anchor IDs resolve; acceptance ledger marks rows 1-77 implemented and row 78 queued for external-package readiness. |

## Icon, localisation, reward, and AI checks

| Surface | Result |
| --- | --- |
| Continental icons | 13 unique family refs; base and shine registrations and DDS files resolve through `interface/012_africa.gfx`. |
| Focus localisation | All 276 continental focus IDs have title and `_desc` keys in `localisation/english/012_africa_focus_l_english.yml`; no focus-title gap was found. |
| Rewards | Every continental focus has a completion reward. Route focuses set `africa_focus_route_context` and `africa_focus_route_step`; support focuses set `africa_focus_support_step` before dispatching the shared helpers. No focus-name/reward mismatch was found against the 78-row anchor map. |
| AI | All route-body focus blocks carry `ai_will_do`; the shared route-pressure modifier is present in the current route body. Overlay and host-playbook AI remains primarily focus-local and requires runtime scenario validation. |

## Recommended parent action and limits

Do not move the nine overlay coordinate bands in the current scope. Vanilla Congo demonstrates the same branch-local coordinate pattern, and the Africa predicates are single-valued equality checks. Moving them would be an unbounded layout redesign and would alter authored relative connectors. Treat the MCP collisions as static-renderer false positives for the mutually exclusive branches, but retain them as an explicit runtime acceptance risk until branch-aware renders or campaign evidence show one visible overlay at a time.

Parent validation should render or inspect one mapped host per overlay, one host per grounded constitutional route, Covenant before and after reveal, compact promotion, and RSA successor transfer. Confirm that the corresponding `mark_focus_tree_layout_dirty` calls update visible branch counts and that no two branch peers are simultaneously visible.

No other focus, icon, localisation, prerequisite, mutual-exclusion, or reward patch was made. No gameplay fallback, route redesign, tag, model, or asset substitution was introduced.

## Validation and skipped checks

Meaningful checks completed: current `hoi4.focus_inspect`; source verification of all nine overlay predicates and constants; static review of grounded-route mutual exclusions; source review of loader, route-commit, Covenant-reveal, RSA-transfer, and compact-promotion refresh paths; and comparison with the vanilla Congo branch-local coordinate precedent.

Skipped: branch-aware MCP rendering and live HOI4 execution. The current focus inspector has no branch-aware scenario selector (`branchCount = 0`), and live consumer validation is parent/user-owned.
