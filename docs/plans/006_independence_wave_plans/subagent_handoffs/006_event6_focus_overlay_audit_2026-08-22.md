# Event 006 focus and overlay audit

Date: 2026-08-22.

Scope: current `independence_wave_focus_tree` framework, its imported IW-043/IW-058, IW-093/IW-098, Pacific, Catalonia, Corsica, and registered-carrier overlay surfaces, plus the reviewed ICE carrier tree. No gameplay source was changed in this audit. The generic focus file already had unrelated uncommitted edits, so those edits were preserved.

## Evidence and validation

Required offline wiki pages and the vanilla focus, trigger, effect, modifier, localisation, scope, on-action, event, decision, idea, AI, and national-focus documentation were read before source review.

The source audit found 318 unique Event 006 focus definitions: 184 direct `focus = {}` nodes and 134 `shared_focus = {}` definitions across `common/national_focus/006_independence_wave_focus.txt`, `006_independence_wave_iw043_iw058_focus.txt`, `006_independence_wave_iw093_iw098_focus.txt`, and `006_independence_wave_pacific_focus.txt`. The main tree has 27 explicit shared-focus import roots.

Every one of the 318 definitions has an icon, coordinates, search filters, `available`, `ai_will_do`, and `completion_reward`. Every title key, `_desc` key, and `custom_effect_tooltip` key resolved against the Event 006 English localisation files. The 121 unique icon references used by these definitions all have a normal sprite and `_shine` sprite in the Event 006 GFX files.

All focus prerequisite and mutual-exclusion references in the four Event 006 focus sources resolve to one of the 318 definitions. The direct 184-node tree has no duplicate coordinates. Relative coordinates in shared package modules intentionally repeat and are resolved through `relative_position_id`.

`hoi4.focus_inspect` on the generic tree returned `FOCUS_INSPECTED`, focus count 184, layout hash `014c594a446087d67b6623767e34af4b83a026e7446235e5a3bd3cbc4eceef2a`, one long connector, and seven Event 006 layout/design diagnostics. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2c823cbdb823425b8cba8975d6d874e17b7c63347705a79a318394e4ea24aebd/2a391953ddd07ecc70e2a7d7214556448ef980161cdfe17b0f7b46cf0a966c20/focus-inspect.e96a318054c8867f.json`.

`hoi4.focus_render` on the generic tree returned deterministic HTML, SVG, JSON, source-map, and plan artifacts. SVG artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fe758b11228c203e9dbbbe784074e0da37e5049de9ed492a8e1e2f55403ae66c/71b6ff14ad894ed30e344782b8638ac57e6a392f023c2d9bb30315c2218e1a5c/independence_wave_focus_tree.focus.svg`.

`hoi4.focus_inspect` and `hoi4.focus_render` were also run on `iceland_tree`. The ICE tree returned focus count 89 and two connector crossings in the existing carrier layout. Its blocking icon diagnostics are existing vanilla ICE references, not Event 006 overlay sprites. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a2aafe4ced70cca098fac98fb1565bb584b7e2162b6dfd40810a3dd0fc08b60a/c16c08da972b3dc83e4e094e573b7e124580189d0c373869fcaa3d170a91f397/focus-inspect.52a5e21598ac1839.json`. Render SVG artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/20a60cdd70336f2142585d7089f046f4edf3847458f9a03756547c373587168e/a5f2b96c72cd87a12d8613b3a5af05407d29052c161c0706dcabe6ffd1edaa0f/iceland_tree.focus.svg`.

No `hoi4.focus_lint` or `hoi4.focus_validate` tool is exposed in this runtime. Focus diagnostics from `hoi4.focus_inspect` were therefore used as the available lint-equivalent evidence; a separate focus lint pass remains blocked by tool availability.

## Route coverage

| Required route or surface | Current implementation | Status and evidence |
| --- | --- | --- |
| Survival and state construction | Twelve direct nodes from `independence_wave_prepare_capital_administration` through `independence_wave_complete_founding_settlement`, with optional internal power-struggle mapping and three settlement choices | Implemented in `common/national_focus/006_independence_wave_focus.txt:95-363`. The capstone uses `can_complete_independence_wave_survival_capstone` and exposes the permanent route families. |
| Government settlements | Constitutional, popular council, traditional restoration, emergency military, patron-client, radical sovereignty, plus IW-010 municipal neutral commission | Implemented in `common/national_focus/006_independence_wave_focus.txt:947-1429`. First commitments are mutually exclusive and package adapters gate route availability. |
| Economy and administration | Emergency revenue, food/fuel, regional transport, customs, package economic program, independent treasury | Implemented in `common/national_focus/006_independence_wave_focus.txt:364-489`. |
| Military and security | Militia integration, depots, officers, border guard, archetype program, five route-choice pairs, professional-defense capstone | Implemented in `common/national_focus/006_independence_wave_focus.txt:490-796`. The choice set matches the accepted military route list. Current graph isolation risk is recorded below. |
| Diplomacy and recognition | Foreign office, first missions, neighbor recognition, neutrality, patron balancing, treaty state, permanent foreign service | Implemented in `common/national_focus/006_independence_wave_focus.txt:797-946`. |
| Former-host settlement | Negotiated separation, guarded frontier, voluntary association, reclamation conflict, and host-collapse successor ledger | Implemented in `common/national_focus/006_independence_wave_focus.txt:1429-1623`. The four living-host choices are mutually exclusive. |
| Regional ambition and integration | Ambition survey, local committees, congress, postwar integration authority, signature extension, formable preparation and integration commission | Implemented in `common/national_focus/006_independence_wave_focus.txt:1624-2086`. Decisions and formable systems remain the owners of paid formation actions. |
| Network and league | New-state recognition, civil-servant exchange, aid corridor, arbitration, charter, founding members, congress, and four proposal branches | Implemented in `common/national_focus/006_independence_wave_focus.txt:1700-1890`. |
| High-chaos and revisionist route | Further ruptures, coordinated reclamation, open sovereignty, border charter rewrite | Implemented and hidden behind route or world-collapse gates in `common/national_focus/006_independence_wave_focus.txt:2087-2151`. |
| Package and regional modules | IW-001, IW-002, IW-004, IW-006, IW-007, IW-008, IW-009, IW-010, IW-014, IW-017, IW-018, IW-019 direct signature modules, plus the imported IW-043/IW-058, IW-093/IW-098, Pacific, CAT, and COR roots | Implemented as gated shared or direct modules. Main import roots are `common/national_focus/006_independence_wave_focus.txt:53-91`; the four imported module files contain 134 shared definitions. |
| IW-012 ICE carrier overlay | Eight shared overlay focuses plus four mutually exclusive ICE route consumers, all explicitly imported by `common/national_focus/iceland.txt:28-44` | Implemented as an additive carrier overlay. The carrier remains `iceland_tree`; assignment is fail-closed through `can_attach_independence_wave_additive_focus_carrier`. |

## Missing or simplified content

- No accepted route family was missing from the current shared framework. The architecture remains one generic tree with gated package modules rather than bespoke country trees, matching `docs/events/006_independence_wave/systems/generic_focus_tree.md` and Part 4 of the accepted focus specification.
- The generic tree explicitly imports the 27 package roots but intentionally does not import the seven overlay descendants or four ICE route consumers. Those 11 definitions are imported explicitly by the carrier tree in `common/national_focus/iceland.txt:34-44`; treating them as missing from the generic full framework would be incorrect.
- The current implementation exposes only the overlay carriers accepted by the runtime trigger: ICE, the IW-023 lifecycle on `austro_hungarian_releasable_focus`, and BOS on that same tree in `common/scripted_triggers/006_independence_wave_focus_triggers.txt:70-87`. The broader Part 5 overlay ledger contains additional overlay obligations, so each future carrier still requires its own import, preservation, package, and runtime evidence before admission.
- The direct Event 006 tree has no duplicate coordinates, no unresolved focus references, and no missing Event 006 focus sprites or localisation keys. No simplification was introduced by this audit.

## Layout and route risks requiring parent review

The following diagnostics came from the current MCP-rendered generic tree and were not patched because the current source has unrelated uncommitted edits and the parent requested no unproven coordinate changes.

| Severity | Focuses | Evidence and risk |
| --- | --- | --- |
| High review | `independence_wave_standardize_with_league`, `independence_wave_preserve_independent_command` | MCP reports both as `FOCUS_ISOLATED`. `standardize_with_league` has no explicit prerequisite at `006_independence_wave_focus.txt:758`; the current working-tree diff also removes the `adopt_military_archetype_program` prerequisite from `preserve_independent_command` at `:777`. Their `available` triggers still require the archetype, so gameplay is gated, but the visible graph loses the military branch connection. Restore or add explicit archetype prerequisites only after confirming the parent’s intended prerequisite correction. |
| Medium | `independence_wave_secure_food_and_fuel` -> `independence_wave_build_regional_transport_authority` | `FOCUS_LAYOUT_LINEAR_DETOUR` at `006_independence_wave_focus.txt:411-428`; same x coordinate skips a row. Moving the transport focus to y4 would be mechanically direct, but the coordinate change was intentionally left for parent review. |
| Medium | `independence_wave_activate_package_economic_program` -> `independence_wave_create_independent_treasury` | `FOCUS_LAYOUT_LINEAR_DETOUR` at `:468-487`; the treasury capstone shifts four columns left. This may be intentional centering, so no automatic move was applied. |
| Medium | `independence_wave_form_border_guard` -> `independence_wave_adopt_military_archetype_program` | `FOCUS_LAYOUT_LINEAR_DETOUR` at `:580-597`; the route skips y6 and shifts two columns. Review alongside the military choice layout. |
| Medium | `independence_wave_define_former_host_policy` -> `independence_wave_inherit_successor_ledger` | `FOCUS_LAYOUT_LONG_CONNECTOR` at `:1590-1608`; the collapse branch spans nine columns to keep the four living-host branches readable. It is a deliberate branch-separation tradeoff, not an automatic safe move. |
| Medium | `independence_wave_build_postwar_integration_authority` -> `independence_wave_focus_discover_regional_identity` | `FOCUS_LAYOUT_LINEAR_DETOUR` at `:1894-1906`; the formable handoff shifts two columns. Review with the regional/formable lane. |

MCP also reported 12 missing icons in vanilla `game:common/continuous_focus/generic.txt` and many existing vanilla ICE icon references. Those diagnostics are outside the Event 006 focus files and were not patched. The Event 006 icon audit found no missing normal or shine sprites.

## Icon coverage table

| Surface | Coverage | Finding |
| --- | ---: | --- |
| Event 006 focus definitions | 318/318 | Every direct and shared definition has an icon reference. |
| Event 006 icon definitions | 121/121 unique icons | Every referenced normal sprite is present in `interface/006_independence_wave*.gfx`. |
| Event 006 shine sprites | 121/121 | Every normal icon has a matching `_shine` sprite. |
| Event 006 focus localisation | 318/318 title and 318/318 descriptions | All keys resolve in the Event 006 English localisation surfaces. |

The most reused family icons are `GFX_goal_independence_wave_former_host_settlement` (22 focuses), `..._army_integration` (19), `..._infrastructure_authority` (18), `..._founding_administration` (17), `..._league_congress` (14), `..._regional_formable` and `..._high_chaos_sovereignty` (13 each), and `..._recognition_diplomacy` (11). These are defined and route-consistent, but the repeated family art reduces per-focus visual distinction and is a future art/UX improvement rather than a missing-asset defect.

## Localisation and reward mismatch list

No proven title, description, tooltip-key, or icon mismatch was found. The source audit resolved all 318 title keys, all 318 `_desc` keys, and all 318 `custom_effect_tooltip` keys. Sampled military, economy, host, league, formable, and overlay descriptions describe the visible route effect without exposing hidden implementation state.

The only open review item is semantic rather than a key failure: the two graph-isolated military command choices have valid visible route text and `available` gates, but their explicit prerequisite display does not currently match the rest of the military choice set after the uncommitted edit described above.

## AI behavior gaps

All 318 Event 006 focus definitions have `ai_will_do`. The generic focus source uses route-aware constants and modifiers, and the baseline profiles in `common/ai_strategy/006_independence_wave_generic.txt:35-104` cover survival, recovery, consolidation, and related state values. ICE route focuses use ledger, war, host-threat, compact, and instability conditions in `common/national_focus/006_independence_wave_focus.txt:3565-3710`.

The mandatory `chaosx_ai_probability_auditor` route was unavailable in this runtime. No callable subagent or collaboration route with that identifier was exposed, so no probability baseline or same-scenario compare is claimed here. The parent must route the weighted focus audit through that auditor before changing any AI target or claiming balance completion. This is the exact unresolved AI blocker.

## High-priority fixes first

1. Parent review should decide whether to restore or add explicit `independence_wave_adopt_military_archetype_program` prerequisites for `independence_wave_standardize_with_league` and `independence_wave_preserve_independent_command`, then rerun `hoi4.focus_inspect` and `hoi4.focus_render`.
2. Route the current focus AI constants, government-route weights, high-chaos gates, and ICE route weights through `chaosx_ai_probability_auditor` with named scenarios and a compare pass before any AI edit.
3. Review the five layout warnings listed above in one focused layout pass. Do not move the former-host or capstone nodes without checking branch readability in the rendered tree.
4. Keep the 12 vanilla continuous-focus icon diagnostics and existing ICE vanilla icon diagnostics out of the Event 006 fix set unless a separate task authorizes vanilla asset repairs.

## Changed files

Only this handoff was added:

- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_focus_overlay_audit_2026-08-22.md`

No focus, overlay, localisation, icon, decision, scripted-trigger, or AI source file was modified. Existing uncommitted edits in `common/national_focus/006_independence_wave_focus.txt` were preserved.

## Remaining limits

- Focus lint is unavailable as a distinct MCP route.
- MCP inline source inventories were truncated for large trees; the linked artifacts retain the complete inspector evidence, while the 318-definition source counts came from the four Event 006 files directly.
- The ICE MCP inspector reports existing vanilla icon errors and does not inline all imported shared-focus definitions, so the carrier import proof was checked directly in `common/national_focus/iceland.txt` and the Event 006 source modules.
- Live HOI4 execution and in-game validation were not run, in accordance with repository instructions.

Plan handoff path: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_focus_overlay_audit_2026-08-22.md`.
