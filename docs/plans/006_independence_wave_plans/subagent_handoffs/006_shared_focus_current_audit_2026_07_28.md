# Event 006 current shared focus and overlay audit - 2026-07-28

> **Superseded for current geometry routing (2026-08-03):** This dated audit preserves its pre-reflow 14-diagnostic HOLD / PARTIAL result and additive-carrier limitations. Use `006_focus_geometry_reflow_parent_2026_08_02.md` for current geometry and `006_event6_current_completion_evidence_v102_2026_08_02.md` for whole-event disposition.

## Status and scope

This is a read-only re-audit of the current Event 006 focus tree, shared-focus imports, package overlays, and additive-overlay assignment contract. No gameplay, localisation, icon, scripted-effect, or focus source file was patched, and no commit was created. The result remains HOLD / PARTIAL for focus completion because the central tree is not validator-clean and additive carrier visibility is not proven.

The bounded source surfaces were `common/national_focus/006_independence_wave_focus.txt`, `common/national_focus/006_independence_wave_iw043_iw058_focus.txt`, `common/national_focus/006_independence_wave_iw093_iw098_focus.txt`, `common/national_focus/006_independence_wave_pacific_focus.txt`, the Event 006 focus icon `.gfx` files, Event 006 focus localisation, `common/scripted_effects/006_independence_wave_focus_effects.txt`, and `common/scripted_triggers/006_independence_wave_focus_triggers.txt`. The IW-005 Flanders carrier was checked through its implementation and independent audit handoffs because that package intentionally does not edit a focus tree.

The accepted architecture requires an existing meaningful country tree to remain active while receiving an additive Independence Wave overlay (`docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_4_focus_tree_architecture.md:26-30`). It also requires existing countries to receive additive branches or decision integration instead of destructive replacement (`...part_4_focus_tree_architecture.md:837-844`) and formed countries to use a reviewed post-formation overlay insertion (`docs/plans/006_independence_wave_plans/subagent_handoffs/006_focus_framework_handoff.md:237`). The offline national-focus wiki and vanilla national-focus documentation were consulted for `shared_focus`, `relative_position_id`, `allow_branch`, prerequisite semantics, and tree loading.

## Current source metrics

| Source | Regular `focus` blocks | `shared_focus` blocks | Total IDs | Result |
| --- | ---: | ---: | ---: | --- |
| `006_independence_wave_focus.txt` | 184 | 13 | 197 | Main tree plus generic overlay and COR extension |
| `006_independence_wave_iw043_iw058_focus.txt` | 0 | 48 | 48 | IW-043 Volga/Ural and IW-058 Mesopotamian shared routes |
| `006_independence_wave_iw093_iw098_focus.txt` | 0 | 43 | 43 | IW-093 Asante and IW-098 Sokoto shared routes |
| `006_independence_wave_pacific_focus.txt` | 0 | 20 | 20 | HBX, HAW, and FIJ Pacific shared routes |
| **Total** | **184** | **124** | **308** | **308 unique IDs; no duplicate focus IDs** |

The main tree has 16 top-level `shared_focus` imports at `common/national_focus/006_independence_wave_focus.txt:40-60`. They import the COR, Pacific, generic overlay, FIJ, IW-043, IW-058, IW-093, and IW-098 roots, including the three explicitly disconnected IW-043 spurs and the IW-058 civilian-command spur. Shared-only files do not define a `focus_tree` and therefore return `FOCUS_TREE_NOT_FOUND` when inspected as standalone trees; the main-tree inspect resolves their imported definitions.

All 308 parsed blocks have an icon, `completion_reward`, `ai_will_do`, title localisation, and `_desc` localisation. The source parser found 121 unique icon IDs, 308/308 title keys, 308/308 description keys, 308/308 reward blocks, 308/308 AI blocks, and no duplicate IDs.

## Route coverage

| Required lane or overlay | Current implementation evidence | Coverage and unresolved risk |
| --- | --- | --- |
| Survival and state construction | `independence_wave_prepare_capital_administration` through `independence_wave_complete_founding_settlement` at `006_independence_wave_focus.txt:66-219` | Present with a real early trunk and a founding capstone. |
| Internal power and government settlements | `independence_wave_map_internal_power_centers` at `:225`; constitutional `:823-899`; popular-council `:903-954`; traditional `:958-1022`; emergency-military `:1026-1077`; patron-client `:1081-1146`; radical sovereignty `:1150-1211`; AJX neutral commission `:1219-1270` | Present. Six main government families plus the package-gated AJX municipal-neutral route have route availability and route locks. |
| Economy and administration | Emergency revenue, food/fuel, transport authority, customs, package economic program, and treasury at `:285-381` | Present and connected to the durable-sovereignty capstone. |
| Army, security, and professional defence | Militia integration and depots at `:405-465`; professional-defence merge and five paired choices at `:507-665` | Present. The capstone uses separate prerequisite blocks for five one-of-each choice pairs, and each pair has mutual exclusion. |
| Diplomacy, recognition, and patrons | Foreign office, missions, recognition, neutrality, patrons, treaty-backed state, and permanent foreign service at `:676-815` | Present. Parent runtime checks still need to prove patron reachability and focus-order selection. |
| Former host, borders, and regional ambition | Former-host policy and negotiated, guarded, association, reclamation, and collapse branches at `:1279-1444`; ambition lane at `:1461-1515` | Present. Five former-host families converge into regional ambition. |
| Network, league, formables, and high chaos | Recognition/network/league at `:1534-1699`; formable preparation and FORM-03 at `:1718-1875`; high-chaos chain at `:1916-1956`; durable capstone at `:3130-3143` | Present in the full tree. Family-level reachability and formable completion are not scenario-proven. |
| Main package overlays | Package-gated SCO (5), WLS (5), AJX (10), BRI (5), AFX (8), AGX (8), RHI (8), BAY (8), ARX (6), and ASX (8) blocks at `:1976-3111` | Present in source with package gates, rewards, icons, localisation, and AI blocks. Live package admission remains outside this audit. |
| IW-017 Corsica shared extension | Five COR shared blocks at `:3280-3348`; root imported at `:40` | Present for full-framework COR packages. |
| Pacific HBX, HAW, and FIJ shared extensions | Twenty blocks in `006_independence_wave_pacific_focus.txt`; HBX, HAW, and three FIJ roots imported at `006_independence_wave_focus.txt:41-46` | Present in source. HAW/FSM/FIJ admission and carrier visibility remain runtime risks. |
| IW-043 and IW-058 shared extensions | Forty-eight blocks in `006_independence_wave_iw043_iw058_focus.txt`; roots imported at `006_independence_wave_focus.txt:47-57` | Present in source, including disconnected economy and civilian-command spurs. Main-tree import resolution is evidenced; standalone shared-file rendering is not applicable. |
| IW-093 and IW-098 signature extensions | Forty-three blocks in `006_independence_wave_iw093_iw098_focus.txt`; capstone roots imported at `006_independence_wave_focus.txt:59-60` | Present in source. Identity, formable, and runtime admission remain parent-owned blockers. |
| Generic additive overlay | Eight `independence_wave_overlay_*` shared blocks at `006_independence_wave_focus.txt:3150-3270`; root imported only by the Event 006 full tree at `:43` | **Source definitions present, existing-tree carrier visibility unresolved.** No existing meaningful country tree in `common/national_focus` imports the root. |
| IW-005 Flanders living-BEL overlay | Decisions, ideas, triggers, effects, and `on_daily_BEL` package only. `006_iw005_flanders_overlay_implementation_2026_07_16.md:13-15,46` explicitly says Belgium's focus tree is unchanged. | **Partial against the generic focus architecture.** The package is intentionally decisions-only and preserves Belgium's meaningful vanilla tree, but no additive shared-focus branch is wired. Parent must either accept/document this exception or design a safe carrier insertion. |

No required full-tree lane was missing from the current source. The two material route-visibility gaps are the generic additive carrier and the post-formation carrier, not absent focus IDs in the Event 006 full tree.

## Prerequisite and mutual-exclusion audit

The main government routes use separate `prerequisite` blocks where both child branches are required before a settlement capstone, while each route-opening focus has a single prerequisite from the founding settlement. The professional-defence merge at `common/national_focus/006_independence_wave_focus.txt:509-513` uses five separate blocks, each containing two alternatives, which matches the intended AND-of-five-OR-pairs semantics. The paired choices at `:532-661` have reciprocal mutual exclusions. No obvious OR-versus-AND semantic error was found in the bounded static pass.

Package `allow_branch` and `available` gates are present on the package overlays, and the focus-trigger helpers in `common/scripted_triggers/006_independence_wave_focus_triggers.txt` keep full-framework and additive flags mutually exclusive. Static semantics do not prove that a target tree actually owns the shared root, however.

## Missing or simplified content

1. **High priority: generic additive carrier insertion is not wired.** The only declaration of `shared_focus = independence_wave_overlay_take_stock_of_independence` is `common/national_focus/006_independence_wave_focus.txt:43`. A repository-wide search finds no target meaningful country tree importing that root and no `add_shared_focus` effect or equivalent dynamic insertion helper. The additive assignment contract at `common/scripted_effects/006_independence_wave_focus_effects.txt:26-56` deliberately sets flags and calls `mark_focus_tree_layout_dirty`, but only the full-framework branch calls `load_focus_tree` at `:40-46`. Under the offline wiki's shared-focus semantics, a flag alone does not attach the shared-focus chain to a different owning tree. This is a source/runtime integration gap, not a safe local focus patch.

2. **High priority: post-formation overlay is accepted by the assignment contract but has no producer or reviewed owning-tree insertion.** `post_formation_overlay` is defined in `common/script_constants/006_independence_wave_focus_constants.txt:16-18` and sets `independence_wave_post_formation_focus_overlay` in `common/scripted_effects/006_independence_wave_focus_effects.txt:51-55`. A repository-wide search finds no call site that sets `independence_wave_focus_assignment_input` to `post_formation_overlay`, and no post-formation focus tree imports the generic overlay root. The current maturity focus is additive-mode gated at `common/national_focus/006_independence_wave_focus.txt:3259-3270`, but that does not establish a post-formation producer or carrier.

3. **Central geometry remains validator-blocked.** The current inspect reports 14 blocking diagnostics with no movable focus IDs. The four coupled clusters are the opening oath/economy crossing at `006_independence_wave_focus.txt:284-301`, the founding-settlement fan crossing the food/fuel lane at `:323-340`, the same fan crossing the depot lane at `:446-465`, and the professional-defence merge at `:506-529`. Nonblocking warnings include 17-, 14-, and 12-column connectors and two through-node intersections from the founding fan. A coordinated reflow is required; an isolated shift is unsafe.

4. **Family-level runtime reachability is unproven.** Structural IDs and main-tree imports are present, but no scenario matrix or probability sweep proves every patron, league, formable, high-chaos, package, and post-formation path. This remains a parent validation gap rather than a source omission.

No fallback route, placeholder focus, generic country replacement, or route family was introduced by this audit.

## MCP inspect, render, and raster evidence

`hoi4.focus_inspect` on `common/national_focus/006_independence_wave_focus.txt` with tree `independence_wave_focus_tree` returned `FOCUS_INSPECTED` with `validation.passed = false` and 14 blocking focus diagnostics. Current revision is `0b97975e36fd4711f3c5838b236d8e1af24ec15781d388e787f1f246c372f7fa`, layout hash is `a7bd7fe6afd3db003f656ef344cedcc280edb3c30cb5e0c5f12cab316890acb1`, and inspect artifact is [focus-inspect.0b97975e36fd4711.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/da337c21248cb368d5baa861bd464a4d9f425ece5ef7fd829ca5ed5718e805e3/076856257ab67149f43272006fe8286601ab587ab899f0d6da64314fddb953af/focus-inspect.0b97975e36fd4711.json).

The inspect metrics are 184 regular focuses, 223 connectors, 49 crossings, 18 node intersections, 27 long connectors, bounds `x=1..101` and `y=0..19`, maximum horizontal span 80, maximum vertical span 6, total horizontal span 1172, total vertical span 278, and maximum Manhattan span 81. The MCP inline inventory was truncated to 64 of 68 paths, but no missing asset or unresolved imported-focus diagnostic was returned.

`hoi4.focus_render` reproduced the same hash and blockers. The latest render artifacts are [HTML](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a918524bc2b5fce688cba59571dee2f90c18785768d6cae2283983f01d67459a/a0dd3452261c832ba2c2133ad39f23e6f3d44ec5c40eff1463e173719b535fa9/independence_wave_focus_tree.focus.html), [SVG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d93f70c7b435ad871d99c8010b7590a3bd2ff577705882971df5ce9e2fa8c239/96dcb5d3e353b9f157d8fe5b1b0cfae4c4701ab7495dcb54849e473ba5117ada/independence_wave_focus_tree.focus.svg), [JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/20b450c4fde493c76a1f5e6f93acc68fb5e1dbc7b70f163deed4f2f4124df60e/50796198674a8918c462d4607e38d2ac5102e5467159135af6f3264bcf665822/independence_wave_focus_tree.focus.json), and [source map](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/62e25f36effa7c02058c9b4e0aa630a4e97a19c62e745fd88fb8e64bfa344a18/3da1fd25c87663aa5df11d10eaef0a10c556de60fbb337310333634d27d7eb79/independence_wave_focus_tree.focus.source-map.json).

`hoi4.focus_raster` completed and produced a [PNG preview](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/71bf187420173187d89f871a8bc5bb0073edd823580987d68030bf735eadcd55/ae3923b8112c1a674682f23516aac0966d53f073c5b5bd92710df0377ab4ce9f/independence_wave_focus_tree.focus.png), [SVG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/175e31c39225031f2e8124f57d308ed20f99d915a4a3d6ad26ab66d337e70a4f/20e65a3b13426609378602c32d613f50316e8dfd30faa40b84b733db4e20a6db/independence_wave_focus_tree.focus.svg), and [HTML](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/63058e71343abc6de419f17bfb3f990af827c33675edb1da2dc43aa4ecae46f4/b798a960af115a18462ecfd19962a5b90a6a4f84f5de60a0d6d69845a500164c/independence_wave_focus_tree.focus.html). The raster SVG URI is retained as returned by MCP; the HTML and PNG are the review artifacts.

## Icon coverage

| Surface | Result | Evidence |
| --- | --- | --- |
| Focus/shared-focus blocks | 308/308 blocks specify an icon | Balanced source parser over all four Event 006 focus files |
| Unique icon IDs | 121 | No missing base sprite reference |
| Base and shine sprites | 121/121 base and 121/121 `_shine` definitions resolve | Event 006 and package `.gfx` files under `interface/` |
| Repeated icon families | Reuse is concentrated in lane-family icons, not undefined references | Highest counts are former-host settlement 21, army integration 19, infrastructure authority 18, founding administration 17, league congress 14, regional formable 13, high-chaos sovereignty 12, and recognition diplomacy 11 |
| Missing/bad icon finding | None in this pass | No undefined reference or missing shine pair was found |

## Localisation and reward mismatch list

The wider English localisation tree contains title and `_desc` keys for all 308 focus/shared-focus IDs. The 34 Event 006 localisation files checked all begin with UTF-8 BOM. No duplicate title or description key was found for the parsed IDs.

Every block has a nonempty `completion_reward` and every reward contains a `custom_effect_tooltip`. Three IDs use a deliberate `focus_` prefix normalization in their tooltip key: `independence_wave_focus_build_permanent_foreign_service` uses `independence_wave_build_permanent_foreign_service_tt`, `independence_wave_focus_discover_regional_identity` uses `independence_wave_discover_regional_identity_tt`, and `independence_wave_focus_coordinate_reclamation_fronts` uses `independence_wave_coordinate_reclamation_fronts_tt`. All three tooltip keys resolve in `localisation/english/006_independence_wave_focus_l_english.yml`; they are not reward mismatches.

No direct focus-name-to-reward contradiction was identified in the bounded static pass. A full prose review of every focus description and every effect payload was not repeated, so this is not a claim that all narrative wording is perfect. No obvious hover-spam or noisy duplicate tooltip pattern was found.

## AI behavior gaps

All 184 regular focuses and 124 shared focuses declare `ai_will_do`. In the main tree, 80 of 184 regular focuses have inline AI modifiers and 104 use only their base constant. Across all 308 blocks, 129 contain inline `factor` or `modifier` logic and 179 use base-only AI weights.

The source contains route-aware gates for government, military, patron, former-host, league, high-chaos, and package focuses. The generic additive overlay itself uses common high/urgent constants at `006_independence_wave_focus.txt:3160-3270`, and no package-specific focus-order strategy block was found for the additive carrier. No `hoi4.probability_inspect` scenario sweep was run for valid/invalid patrons, league membership, formables, high-chaos, meaningful-tree overlays, or post-formation overlays. Fiji's package handoff separately records no FIJ-specific focus-order strategy. These are evidence gaps, not missing AI blocks.

## High-priority fixes first

1. Resolve the additive and post-formation carrier design before claiming overlay completion. For each meaningful existing tree, explicitly register the shared root in the owning tree or document and implement an engine-supported insertion path that preserves the tree. For formed countries, add a reviewed post-formation producer and carrier. Do not call `load_focus_tree` for meaningful trees without an accepted preservation design.
2. Reflow the four MCP-blocking geometry clusters as one coordinated change. Re-run inspect and render after each coherent tranche and retain before/after metrics; preserve all focus IDs, prerequisite semantics, mutual exclusions, rewards, icons, localisation, and AI weights.
3. Run parent-owned scenario and probability validation for full framework, meaningful-tree overlay, formable, league, patron, former-host, high-chaos, and post-formation cases. Include package-carrier admission and save/load cleanup checks where relevant.
4. Re-audit IW-005 as an explicit architecture exception or add a safe shared-focus registration path. Its current decisions-only implementation is internally coherent but does not demonstrate the generic additive focus lane promised by Part 4.

## Validation performed and skipped

Validation performed was the required offline wiki and vanilla documentation review, balanced parsing of all four focus source files, duplicate-ID and field coverage checks, localisation key/BOM checks, icon base/shine resolution checks, `hoi4.focus_inspect`, `hoi4.focus_render`, and `hoi4.focus_raster`. The main-tree inspect and render both reproduced the same 14 blocking diagnostics and layout hash. Standalone inspect attempts for the shared-only files returned `FOCUS_TREE_NOT_FOUND` as expected because those files contain definitions but no `focus_tree` block.

`hoi4.focus_rewrite` was intentionally skipped because the remaining geometry defects are coupled and no safe movable IDs were returned. No game executable was launched, no save was loaded, no live country admission was attempted, and no probability simulation was run. Those checks belong to the parent-owned completion surface.

## Changed files, identifiers, and remaining risks

Changed files: none. Changed focus IDs: none. Localisation keys changed: none. Icon IDs changed: none. No plan-mode improvement addendum was written because the full tree is not shallow or missing a route family; the remaining work is a carrier-design decision, coordinated geometry reflow, and runtime validation. This handoff is the plan/audit path: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_shared_focus_current_audit_2026_07_28.md`.

Remaining risks are unresolved additive carrier visibility, dead/unproven post-formation assignment, 14 blocking geometry diagnostics, unproven family-level route reachability, package-specific AI selection evidence, and live package admission. No simplification or fallback was introduced by this audit.
