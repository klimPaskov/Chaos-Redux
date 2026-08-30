# Event 006 focus gap probe — no-change handoff (2026-08-30)

## Disposition

This bounded audit found no safe source-backed route, prerequisite, mutual-exclusion, icon, localisation, reward, or focus-AI patch inside the Event 006 focus surface.

No gameplay focus files were changed, no focus IDs were changed, and no geometry rewrite was attempted.

The shared tree and imported overlays remain unchanged because the required route coverage and source wiring are present, while the remaining gaps are package-admission evidence, carrier diagnostics outside the overlay, or probability-auditor availability issues.

## Scope and authority

The audit covered `common/national_focus/006_independence_wave_focus.txt`, `common/national_focus/006_independence_wave_iw043_iw058_focus.txt`, `common/national_focus/006_independence_wave_iw093_iw098_focus.txt`, and the carrier trees that import the shared overlay, `common/national_focus/iceland.txt` and `common/national_focus/austro_hungarian_releasable_shared.txt`.

The design authority was `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_4_focus_tree_architecture.md`, `docs/specs/006_independence_wave_specs/diagrams/006_focus_tree_lane_map.md`, `docs/specs/006_independence_wave_specs/matrices/006_ai_strategy_matrix.csv`, `006_regional_overlay_matrix.csv`, and `006_idea_lifecycle_matrix.csv`.

The latest relevant handoffs reviewed were `006_event6_focus_audit_current_2026-08-29.md`, `006_event6_focus_surface_scan_2026-08-26.md`, `006_event6_focus_overlay_gap_audit_2026-08-26.md`, `006_event6_focus_kosovo_registry_merge_2026-08-26.md`, `006_event6_focus_geometry_closure_current_2026-08-25.md`, `006_event6_focus_economy_lane_repair_2026-08-24.md`, and `006_event6_focus_military_cohort_reflow_2026-08-24.md` under `docs/plans/006_independence_wave_plans/subagent_handoffs/`.

Required offline references were consulted in `paradox_wiki/`: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, and National focus modding.

Required vanilla references were consulted in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/`, including `triggers_documentation.md`, `effects_documentation.md`, `console_commands_documentation.md`, and `script_concept_documentation.md`.

The National focus wiki confirms that one prerequisite block containing several focuses is OR, separate prerequisite blocks are AND, mutual exclusions must be symmetric, `available` is an AND gate, and focus icons require normal and `_shine` sprite definitions.

## Route coverage

| Spec lane or surface | Current source evidence | Audit result |
| --- | --- | --- |
| Survival and state construction | `common/national_focus/006_independence_wave_focus.txt:103-366` | Opening, capital, provisional authority, inventory, oath, ministries, treasury, legal, communications, provinces, leadership, legitimacy, capacity, capital, and founding-settlement gates are present. |
| Economy and administration | `common/national_focus/006_independence_wave_focus.txt:370-489` | Economy/admin lane and its trunk handoffs are present. |
| Army and security | `common/national_focus/006_independence_wave_focus.txt:496-794` | Domestic arsenals versus foreign arms, border defence versus reclamation, and league standardisation versus independent command are symmetric route choices. |
| Diplomacy, recognition, and patrons | `common/national_focus/006_independence_wave_focus.txt:805-946` | Recognition, provisional diplomacy, patron access, and external settlement hooks are present. |
| Government and internal power | `common/national_focus/006_independence_wave_focus.txt:957-1430` | Constitutional, popular, traditional, emergency, patron, and radical routes have route gates and mutual exclusions. |
| Former host and borders | `common/national_focus/006_independence_wave_focus.txt:1439-1625` | Former-host settlement choices and border/expansion handoffs are present. |
| Regional ambition | `common/national_focus/006_independence_wave_focus.txt:1629-1705` | Regional ambition is gated and continues into the network/league surfaces. |
| Network, league, and formables | `common/national_focus/006_independence_wave_focus.txt:1710-2092` | Network/league branches and formable preparation are present, including the capstone prerequisites. |
| Hidden radical/high-chaos route | `common/national_focus/006_independence_wave_focus.txt:2097-2155` | Hidden revisionist/high-chaos lane is present and remains separate from ordinary route choices. |
| Shared package modules | `common/national_focus/006_independence_wave_iw043_iw058_focus.txt:18-786` and `common/national_focus/006_independence_wave_iw093_iw098_focus.txt:23-738` | All 91 module definitions are reachable from the 14 imported module roots; no module definition is omitted. |
| Shared overlay | `common/national_focus/006_independence_wave_focus.txt:3399-3710` | Overlay take-stock root, secure services, release forces, foreign desk, former-host, network, regional ambition, mature independence, and four ICE route consumers are present. |
| ICE carrier | `common/national_focus/iceland.txt:28,34-44` | Carrier imports the overlay plus all four ICE route consumers; carrier inspect/render evidence is available. |
| Austro-Hungarian carrier | `common/national_focus/austro_hungarian_releasable_shared.txt:31-38` | Carrier imports the eight shared overlay nodes; no ICE-specific route consumer is incorrectly imported. |

The static graph audit found `BLOCKS_TOTAL=318`, `DIRECT=184`, `SHARED=134`, `UNIQUE=318`, `DUPLICATE_IDS=0`, and `MISSING_REQUIRED_FIELDS=0`; every focus/shared block has `icon`, `search_filters`, `completion_reward`, and `ai_will_do`.

The root has 27 imports and the two module files define 91 imported module focuses; all 91 module definitions are reachable from the root import set, with `OMITTED=0`.

The root inline shared graph has 134 shared definitions, of which 123 are reachable from root imports; the 11 omitted from the root-only graph are the expected carrier-only overlay and ICE descendants, and are reachable through the ICE carrier imports.

## Prerequisite and mutual-exclusion audit

The source parser found `DEFS=318`, `MUTEX_OWNERS=55`, `ASYMMETRIC=0`, and `MISSING_PREREQS_WITHIN_SURFACE=0`; 129 relative-position references resolve.

The military route pairs are symmetric: `independence_wave_fund_domestic_arsenals` versus `independence_wave_accept_foreign_arms`, `independence_wave_adopt_border_defense` versus `independence_wave_adopt_reclamation_doctrine`, and `independence_wave_standardize_with_league` versus `independence_wave_preserve_independent_command`.

`independence_wave_adopt_reclamation_doctrine` has an explicit visible prerequisite on `independence_wave_adopt_military_archetype_program` and a package/host route gate; no OR-versus-AND correction is justified from the current source.

The government route choices in `common/national_focus/006_independence_wave_focus.txt:957-1430` also have symmetric exclusion sets.

## Icons, localisation, and rewards

| Surface | Evidence | Result |
| --- | --- | --- |
| Focus icons | `interface/006_independence_wave.gfx`, `interface/006_independence_wave_iw093_iw098_focus.gfx`, and `interface/006_independence_wave_small_assets.gfx` | `UNIQUE_ICONS=121`; normal definitions missing `0`; `_shine` definitions missing `0`; all 271 Event6 texture references resolve. |
| Focus localisation | `localisation/english/006_independence_wave*_l_english.yml` (37 files) | `DEFS=318`, `LOC_KEYS=8270`, `MISSING_TITLE=0`, `MISSING_DESC=0`, `MISSING_TT=0`, `BAD_BOM=0`. Every focus title, `_desc`, and `custom_effect_tooltip` reference resolves. |
| Scripted reward helpers | Event6 focus sources and `common/scripted_effects/006_independence_wave*.txt` | Fresh focus-call candidates: `12`; missing helper definitions: `0`. The prior broader reward-helper audit also recorded 331 references with zero missing definitions. |

No focus-name/reward mismatch or repeated missing reward hook was found, so no localisation, icon, or reward patch was made.

## AI behavior

All 318 direct/shared focus definitions contain `ai_will_do`.

Generic focus constants are in `common/script_constants/006_independence_wave_constants_registry.txt:1740+`, including the standard, high, urgent, preferred, prerequisite-boost, avoidance, and war-avoid factors.

The current generic strategy source is `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt:711-833`, containing `independence_wave_generic_survival_profile`, `independence_wave_generic_recovery_profile`, and `independence_wave_generic_consolidation_profile`; the older handoff reference to `common/ai_strategy/006_independence_wave_generic.txt` is stale and should not be used as the current source path.

Package module focus weights use route-aware package constants and modifiers in `common/script_constants/006_independence_wave_constants_registry.txt` and the two package module files.

The mandatory `chaosx_ai_probability_auditor` route is unavailable in this runtime: `ALL_TOOLS` exposes no callable tool with that identifier, and only the raw `hoi4_probability_inspect`, `hoi4_probability_evaluate`, `hoi4_probability_sweep`, and `hoi4_probability_compare` routes are exposed. Therefore this handoff makes no AI weight claim beyond source presence and makes no AI patch; a same-scenario baseline/compare must be run by the parent through the required auditor before any balance change.

## Mandatory MCP focus evidence

### Shared root

`hoi4.focus_inspect` on `common/national_focus/006_independence_wave_focus.txt`, tree `independence_wave_focus_tree`, returned `FOCUS_INSPECTED`, revision `dd5d3a2eb0ba3fa88f0cbd14f6a184c6861d72881f62074076556ead5dde2233`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9d4e6c1206b128e21aa2f6362df6424b96c7f7eb43ecfa14879fc11212f88d9d/d7eb4cf18c892af682020d86a9d7d85c54e6381745eb0f9fbea404dbd2b7be82/focus-inspect.dd5d3a2eb0ba3fa88f0cbd14f6a184c6861d72881f62074076556ead5dde2233.json`.

The root has 184 materialized focuses and 195 connectors, bounds `x=1..121`, `y=0..19`, zero crossings, zero node intersections, zero long connectors, maximum horizontal span 8, zero too-close rows, and `diagnosticCount=0`; validation passed.

`hoi4.focus_render` on the same root returned `FOCUS_RENDERED`, validation passed, and the same layout hash `a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7`.

Render artifacts were `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bff2883b89731542e086b5be9acd0ac8e4c89ec0b730dff304c43f708639826e/400dce0578cee5b00e1d78a2b71e8b2375fd406caec8c9bbf073012e01a25e69/independence_wave_focus_tree.focus.html`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/790ac83c6f2cdb9816133b30e7a650f0e74f3823cf45efd0753fa9182ec87279/c024172984265bdd2e1e63ce390617f4f4cf8029ca655434f9299def11fa916b/independence_wave_focus_tree.focus.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b8910c875484794c1482583777e1baa1fc8f516fc48297fd582388bbb454198f/e8f22d17f392b7324607765fa946fdc3680d77fc7db602f2ccc70527bf0d9723/independence_wave_focus_tree.focus.json`.

The root render dimensions are 21424x2440, above the 16384 raster ceiling, so raster capture was skipped; the production SVG/HTML/JSON render remains available.

### Shared-focus-only modules

Direct `hoi4.focus_inspect` and `hoi4.focus_render` calls for both `006_independence_wave_iw043_iw058_focus.txt` and `006_independence_wave_iw093_iw098_focus.txt` returned `FOCUS_TREE_NOT_FOUND` with the exact blocker that the selected source contains no national focus tree.

This is an MCP surface limitation of `shared_focus`-only source modules, not evidence of missing route content; the imported carrier/root trees are the valid inspection surfaces.

### ICE carrier

`hoi4.focus_inspect` on `common/national_focus/iceland.txt`, tree `iceland_tree`, returned revision `781d731941d79e3441b7390c118c20b67694299811bde892162afadd61300654`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1dd868d78dee117f2a648f4fce8932de127db83fdd8b7f7e9cf86f9c742317a2/9a0543fad1800fab387ac537b48cba68184c940344b6fe35ffad912d70276fa5/focus-inspect.781d731941d79e34.json`.

The carrier has 89 focuses and 104 connectors, layout hash `519ea6ed46008ccdaca74b3938aa42abcd45a1b88feb080bf224a21ed17b3e8c`, bounds `x=2..37`, `y=0..9`, two connector crossings, zero node intersections, zero long connectors, and 57 diagnostics.

The seven blocking diagnostics are pre-existing carrier ideas at `iceland.txt:802-803`, `:1460-1461`, `:2099-2100`, and `:2274`; twelve focus-filter warnings are on older ICE focuses. None targets an Event6 overlay focus, so they are outside this bounded patch scope.

The ICE `hoi4.focus_render` returned `FOCUS_RENDERED` but validation false for the same seven missing carrier ideas; this is recorded as carrier evidence, not as Event6 overlay failure.

### Austro-Hungarian carrier

`hoi4.focus_inspect` on `common/national_focus/austro_hungarian_releasable_shared.txt`, tree `austro_hungarian_releasable_focus`, returned artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fb410f772d2c1d6b9fa0697dc9199c20754875a33570ba02f76e02117f9f1787/d302f59d38ad90a0b7668afbfbe974e1c79a4eed3dd2198367ec6e665db07e83/focus-inspect.781d731941d79e34.json`.

The carrier has 56 focuses and 62 connectors, layout hash `8e1c44e617e03adc234cb622e850552e6b313e775be0cd3452761fa1f52f98bf`, bounds `x=0..22`, `y=0..7`, one crossing, one node intersection, no long connectors, and 13 diagnostics; validation passed.

The warnings are on old AHR generic branches, including repeated generic rewards, linear detours, and a naval connector crossing, and do not target the Event6 overlay. No geometry change is justified.

The AHR `hoi4.focus_render` returned `FOCUS_RENDERED`, validation passed, with HTML `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/01165b619eed74d6ff25a9fc56570dd8767924a878096cfb52ef389982ec3110/968793061b45671367b1e3b4df4ba58babdc81607b510b45336f9eaedfa38506/austro_hungarian_releasable_focus.focus.html`, SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c8f9e28d3344978df4ba1ba2f9032cbb7823bb6c4293448760449d0f5d877431/60503b35c7c22b93d22f4f95dd5fb181c8230f08fe8fb20fde609afc047bed8b/austro_hungarian_releasable_focus.focus.svg`, and JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/293b668962ec684e792eaa4872edc02bffdfe8248f522073137415fe31c7115d/3e8a95d6a6fa216af39bcc55106c6e047b3a4318dfb3a3cb30f7b033a673e1cd/austro_hungarian_releasable_focus.focus.json`.

## Missing or simplified content

No accepted Part 4 route, lane, overlay node, package module, route lock, prerequisite, mutual exclusion, icon, localisation key, or reward helper is missing from the audited source surface.

The package-admission audit remains partial by design: prior evidence records 32 content-attested selectable packages, 40 runtime adapters, 29 compatible reservation groups, and 161 unattested rows; adapter-only rows remain fail-closed, including IW-013 NAV, IW-015 GLC, IW-043 CHU, IW-058 ASY, IW-093 DOX, IW-098 SOK, IW-177 FIJ, and IW-179 FSM, while IW-095 DAH has no central focus callback. This is package-evidence work and not a safe focus-file patch.

No improvement plan was written because the accepted Event6 routes are not shallow or disconnected in the audited surface, and the remaining issues require package-admission or AI-auditor decisions rather than a bounded focus edit.

## High-priority follow-up

1. Keep the root Event6 geometry unchanged while its MCP layout remains clean with zero diagnostics.

2. Have the parent run the required `chaosx_ai_probability_auditor` baseline and same-scenario compare before changing any focus or strategy weight; the auditor is unavailable in this runtime.

3. Preserve fail-closed package admission until the unattested rows and IW-095 callback have explicit package-source evidence.

4. Use the ICE or Austro-Hungarian carrier trees as the MCP wrapper for shared-focus-only overlay validation; direct module inspection cannot materialize a `shared_focus`-only source.

5. Keep pre-existing ICE missing-idea diagnostics and old AHR generic warnings separate from Event6 overlay ownership.

## Change and validation record

Changed file: this dated no-change handoff only, `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_focus_gap_probe_2026-08-30.md`.

Changed focus IDs: none.

Route behavior before and after: unchanged.

Localisation keys and icon IDs changed: none.

Meaningful validation completed: required offline wiki and vanilla documentation review; static focus graph, import reachability, prerequisite/mutex, icon, localisation, reward-helper, and AI-source audits; fresh root `hoi4.focus_inspect` and `hoi4.focus_render`; direct shared-module inspect/render blocker checks; ICE carrier inspect/render; and Austro-Hungarian carrier inspect/render.

Meaningful validation skipped: `hoi4.focus_rewrite` because no safe patch was identified; dedicated probability-auditor baseline/compare because no callable `chaosx_ai_probability_auditor` exists; raster render because the root output is 21424 pixels wide and exceeds the 16384 raster ceiling; and live HOI4 execution because repository policy assigns in-game validation to the user.

No gameplay simplification, fallback, unapproved expansion, or geometry change was made.

Plan handoff path: none; this is a no-change audit handoff.
