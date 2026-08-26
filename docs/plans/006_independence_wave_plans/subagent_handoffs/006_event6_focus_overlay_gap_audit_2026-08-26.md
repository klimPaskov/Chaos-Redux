# Event 006 focus overlay gap audit — 2026-08-26

Date: 2026-08-26.

## Scope and disposition

This bounded audit covers the accepted Part 4 focus architecture, focus lane map, regional overlay matrix, the shared `independence_wave_focus_tree`, the IW-043/IW-058 and IW-093/IW-098 shared-focus modules, the merged Pacific/CAT/COR blocks, and the admitted ICE and austro-Hungarian carrier overlay imports.

The offline Paradox national-focus, data-structure, trigger, effect, modifier, localisation, scope, on-action, event, decision, idea, and AI pages were read alongside the required vanilla documentation and vanilla focus examples before source review.

No gameplay source is changed by this audit. No accepted route, prerequisite, mutual-exclusion, reward, icon, localisation, or AI defect was proven safe to repair without changing the established 184-focus geometry or expanding package admission. The only file added is this dated handoff.

## MCP and static evidence

The current root `independence_wave_focus_tree` was inspected with `hoi4.focus_inspect` and rendered with `hoi4.focus_render` from `common/national_focus/006_independence_wave_focus.txt` in workspace `mod_chaos_redux_ea3b2d67c2c0`.

The inspector returned 184 focuses and 195 connectors with zero crossings, zero node intersections, zero long connectors, zero too-close pairs, maximum horizontal span 8, and no duplicate-coordinate diagnostic. The root inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e8a268efcbebdafa4f0843ba166594a187c2e82c8ff35960de321feb6a672915/e72cea16463e5b29f4f838516bcb0618bb94a95d9ee7a0572c1ecea43a8f17a3/focus-inspect.3f8540dcbbcb78d1.json`.

The root render returned `FOCUS_RENDERED`, validation passed, and layout hash `a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7`. A reviewed SVG artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fe758b11228c203e9dbbbe784074e0da37e5049de9ed492a8e1e2f55403ae66c/71b6ff14ad894ed30e344782b8638ac57e6a392f023c2d9bb30315c2218e1a5c/independence_wave_focus_tree.focus.svg`.

Direct inspection and rendering of `006_independence_wave_iw043_iw058_focus.txt` and `006_independence_wave_iw093_iw098_focus.txt` returned `FOCUS_TREE_NOT_FOUND` with the message `The source file contains no focus tree`. These files intentionally contain only `shared_focus` definitions and are imported by the root tree or carrier trees, so this is an MCP surface limitation rather than evidence of an absent route.

Static source review across the three current Event 006 focus sources found 318 unique definitions: 184 direct focuses and 134 shared focuses. All 318 have `available`, `completion_reward`, `ai_will_do`, `icon`, coordinates, and `search_filters`; all prerequisite, mutual-exclusion, and relative-position references resolve; and no mutual-exclusion pair is asymmetric.

The Event 006 focus icon audit found 121 unique icon IDs with 121 normal sprites and 121 matching `_shine` sprites. The reward-token audit found no Event 006 focus reward helper token without a matching custom effect definition. Title, description, and custom tooltip key checks resolved for all 318 definitions.

No distinct `hoi4.focus_lint` or `hoi4.focus_validate` route is exposed in this runtime. `hoi4.focus_rewrite` was not used because no safe focus patch was identified. Live HOI4 execution and save validation were not run by design.

## Route coverage

| Required route or surface | Current implementation | Status and exact source references |
| --- | --- | --- |
| Survival and state construction | Capital administration through founding settlement, with settlement choices and survival capstone | Covered in `common/national_focus/006_independence_wave_focus.txt:95-363`. |
| Government settlements | Constitutional republic, popular councils, traditional restoration, emergency military, patron-client, radical sovereignty, plus neutral commission | Covered in `common/national_focus/006_independence_wave_focus.txt:947-1429`. |
| Economy and administration | Revenue, food/fuel, transport authority, package economic program, and independent treasury | Covered in `common/national_focus/006_independence_wave_focus.txt:364-489`. |
| Army and security | Militia, depots, officers, border guard, military archetype, route choices, and professional defense | Covered in `common/national_focus/006_independence_wave_focus.txt:490-796`. The standardization and independent-command choices have restored archetype prerequisites at `:762-791`. |
| Diplomacy and recognition | Foreign office, missions, recognition, neutrality, patron balancing, treaty state, and permanent foreign service | Covered in `common/national_focus/006_independence_wave_focus.txt:797-946`. |
| Former-host and border settlement | Separation, guarded frontier, association, reclamation conflict, and successor ledger | Covered in `common/national_focus/006_independence_wave_focus.txt:1429-1623`, with the four living-host choices mutually exclusive. |
| Regional ambition and formables | Identity survey, committees, congress, integration authority, signature extensions, and formable preparation | Covered in `common/national_focus/006_independence_wave_focus.txt:1624-2086`; paid formation remains owned by decision/formable systems. |
| Network and league | Recognition, exchange, aid corridor, arbitration, charter, members, congress, and proposal branches | Covered in `common/national_focus/006_independence_wave_focus.txt:1700-1890`. |
| High-chaos and revisionist route | Further ruptures, coordinated reclamation, open sovereignty, and charter rewrite | Covered behind route or world-collapse gates in `common/national_focus/006_independence_wave_focus.txt:2087-2151` and the high-chaos terminals near `:3370-3387`. |
| IW-043 and IW-058 overlays | 48 shared definitions with explicit main-tree roots and route-terminal rewards | Imported by `common/national_focus/006_independence_wave_focus.txt:60-67`; definitions are in `common/national_focus/006_independence_wave_iw043_iw058_focus.txt:18-786`. Direct module MCP inspection/render is blocked because the file has no tree wrapper. |
| IW-093 and IW-098 overlays | 43 shared definitions with explicit main-tree roots and route-terminal rewards | Imported by `common/national_focus/006_independence_wave_focus.txt:72-87`; definitions are in `common/national_focus/006_independence_wave_iw093_iw098_focus.txt:23-738`. Direct module MCP inspection/render is blocked for the same reason. |
| Pacific, Catalonia, and Corsica package modules | Pacific blocks merged into the main source, with CAT and COR signature roots | Covered in `common/national_focus/006_independence_wave_focus.txt:3718-4247`, including the Pacific source marker and package-gated roots. |
| Additive carrier overlay | Overlay root, secure/integrate/foreign/host/network/ambition/maturity descendants, and ICE route consumers | ICE imports the overlay and route consumers in `common/national_focus/iceland.txt:28-44`; the runtime carrier whitelist is fail-closed in `common/scripted_triggers/006_independence_wave_focus_triggers.txt:70-87`. The austro-Hungarian carrier imports the overlay descendants in `common/national_focus/austro_hungarian_releasable_shared.txt:31-38`. |

## Missing or simplified content

No accepted route family is missing from the current shared framework. One generic tree with gated package and carrier modules is intentional and matches Part 4 rather than a simplification introduced by this audit.

The broader package-admission ledger remains `HOLD / PARTIAL`, with 32 content-attested selectable packages, 40 runtime adapters, and 161 unattested selectable rows in the current resume packet. Those rows require package evidence, carrier preservation, and admission review; they are not a safe generic focus-file patch.

The overlay module sources cannot receive direct MCP tree evidence because they are shared-focus-only files. Root-tree and carrier import wiring was checked in source, but no module-level layout claim is made.

## Icon coverage

| Surface | Coverage | Finding |
| --- | ---: | --- |
| Event 006 focus definitions | 318/318 | Every direct and shared definition has an icon reference. |
| Event 006 normal sprites | 121/121 unique IDs | No missing Event 006 normal sprite was found in the Event 006 GFX files. |
| Event 006 shine sprites | 121/121 | Every normal icon has a matching `_shine` sprite. |
| Event 006 title/description/tooltip localisation | 318/318 | All source keys resolve in the Event 006 English localisation surfaces. |

Family art is intentionally reused across routes, including former-host settlement, army integration, infrastructure authority, founding administration, league congress, regional formable, high-chaos, and recognition families. This is an art-distinction improvement opportunity, not a missing icon wiring defect, and no asset patch is justified inside this bounded audit.

## Localisation and reward mismatch list

No missing or mismatched Event 006 focus localisation key was found. All 318 title keys, `_desc` keys, and `custom_effect_tooltip` keys resolve.

No reward helper reference is source-missing: every Event 006 focus reward token matched an existing custom effect definition. Sampled survival, government, economy, military, diplomacy, former-host, league, formable, and overlay rewards describe their route effects and are not merely flat generic rewards.

No localisation, reward, focus, or icon file was changed.

## AI behavior gaps

All 318 Event 006 focus definitions have an `ai_will_do` block. Route-aware focus constants and modifiers are present in the generic tree, and baseline strategy profiles cover survival, recovery, consolidation, and state values in `common/ai_strategy/006_independence_wave_generic.txt:35-104`.

The required `chaosx_ai_probability_auditor` route was not callable in this runtime. No probability baseline or same-scenario compare is claimed, and no AI weight was edited. A parent-owned probability audit is required before changing route weights, high-chaos gates, or country-specific focus selection behavior.

## High-priority fixes and next owner

1. No gameplay focus patch is justified by this evidence. Preserve the closed 184-focus and 195-connector geometry.
2. Route all future focus AI or probability-bearing changes through `chaosx_ai_probability_auditor` with named scenarios and a compare pass.
3. Treat broader package admission as a package-evidence task, not a generic focus-tree task; preserve the fail-closed carrier whitelist until each accepted overlay has its own imports, runtime gate, route lock, localisation, and preservation evidence.
4. If a parent review later requests module layout evidence, inspect a wrapper tree or carrier tree that actually imports the shared-focus module; direct module calls will continue to return `FOCUS_TREE_NOT_FOUND`.

## Changed files and behavior

Changed files: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_focus_overlay_gap_audit_2026-08-26.md` only.

Changed focus IDs: none.

Route behavior before and after: unchanged; no focus source, prerequisite, mutual exclusion, reward, AI, localisation, icon, or carrier import was modified.

No improvement plan was written because the audit found no shallow accepted route or new route family that could be safely addressed inside this bounded task. The next owner is the parent agent for package-admission evidence and the required probability-auditor route.

## Remaining route risks

- Broader package admission remains incomplete and evidence-gated in the Event 006 resume packet.
- Country-specific focus AI and probability behavior has not received the mandatory auditor baseline/compare because that route was unavailable here.
- Shared-focus-only modules lack direct module-level MCP inspection/render evidence, although root and carrier imports are source-confirmed.
- Reused family art can reduce visual distinction despite complete icon wiring.
- The root render retains only the unrelated vanilla `continuous_restrict_freedom_desc` localisation diagnostic; it is outside Event 006 focus scope.

No gameplay simplification, fallback, or unapproved route expansion was introduced by this audit.
