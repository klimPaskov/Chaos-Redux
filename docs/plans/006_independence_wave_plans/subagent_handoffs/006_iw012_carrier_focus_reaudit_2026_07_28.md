# Event 006 IW-012 carrier focus re-audit — 2026-07-28

## Status and scope

This is a read-only re-audit of the IW-012 Iceland carrier after the carrier import was added. No gameplay, focus, AI, localisation, icon, or source file was patched by this audit. The source carrier and route gates are structurally present, while live shared-focus visibility, the central tree geometry, and dynamic former-host AI targeting remain unresolved validation items.

The review covered `common/national_focus/iceland.txt`, `common/national_focus/006_independence_wave_focus.txt`, `common/scripted_triggers/006_independence_wave_ice_package_triggers.txt`, `common/ai_strategy/006_independence_wave_ice.txt`, `interface/006_independence_wave.gfx`, and `localisation/english/006_independence_wave_focus_l_english.yml`, together with the Event 006 focus architecture and IW-012 package specifications, offline Paradox wiki pages, vanilla focus documentation, and vanilla/shared-focus precedents.

## Route coverage

| Required route or lane | Current evidence | Coverage |
| --- | --- | --- |
| Existing meaningful carrier preservation | `common/national_focus/iceland.txt:1-3436` retains the vanilla `iceland_tree` body; after removing the 12 Event 006 imports and six carrier comments, the normalized source matches the vanilla file byte-for-byte. | PASS at source level; runtime shared-focus admission is not proven. |
| Event 006 survival/state overlay | `independence_wave_overlay_take_stock_of_independence`, `...secure_state_services`, and `...integrate_release_forces` are defined in `common/national_focus/006_independence_wave_focus.txt:3151-3184` and imported by ICE at `iceland.txt:28,32-33`. | Present. |
| Government/internal power overlay | `...open_foreign_desk`, `...address_former_host`, `...join_network`, `...open_regional_ambition`, and `...mature_independence` are defined at `006_independence_wave_focus.txt:3185-3275` and imported by ICE at `iceland.txt:34-38`. | Present with the generic government fan and route-aware availability. |
| IW-012 government routes | `independence_wave_ice_choose_constitutional_route`, `...restore_traditional_authority`, `...establish_emergency_command`, and `...accept_patron_mandate` are defined at `006_independence_wave_focus.txt:3286-3361` and imported at `iceland.txt:39-42`. Each has the shared overlay prerequisite, package-aware branch trigger, route-specific lock trigger, and pairwise mutual exclusions. | Present. |
| Economy and administration | The generic service/foreign/host overlay is joined by ICE shipping-registers, municipal-charter, port-authority, and coastwatch decisions in `common/decisions/006_independence_wave_ice_decisions.txt`; the serialized-project guard excludes the persistent survival deadline. | Present as additive package mechanics; there is no separate full ICE economy focus lane by design. |
| Army and security | `...integrate_release_forces` is imported, the emergency route is gated by coastwatch expansion/readiness, and the ICE package provides the coastwatch and armed-neutrality decision surfaces. | Present. |
| Former-host and borders | `...address_former_host` is imported and the ICE route/decision surfaces consume `has_event_target = independence_wave_setup_former_host` and `var:independence_wave_former_host` checks in `common/scripted_triggers/006_independence_wave_ice_package_triggers.txt:16-30,110-124`. | Present in focus and trigger source; dynamic AI target remains wrong-risk. |
| Network, league, and FORM-02 | `...join_network` and `...open_regional_ambition` are imported; the patron route requires compact delegation/support and the registered North Atlantic Compact family. | Present without a separate ICE high-chaos branch. |
| High-chaos/popular/radical branches | The IW-012 route triggers intentionally expose only the four package routes; `has_prepared_independence_wave_iw_012_package_setup` explicitly excludes popular and radical route availability. | Intentional package simplification, not an omitted required IW-012 route. |

## Missing or simplified content

1. The MCP national-focus inspector and renderer do not expand `shared_focus` imports into the carrier graph, so the ICE artifacts report 89 regular vanilla nodes rather than the 12 imported Event 006 nodes. This is a tooling limitation, not evidence that the source imports are absent.
2. The ICE inspect/render artifacts report vanilla missing-sprite diagnostics and truncated diagnostic collections; these are baseline inventory/parser findings on the preserved vanilla tree, not missing Event 006 route icons.
3. Live HOI4 load/save proof that all 12 imports appear in `iceland_tree` is still missing. The source import list is explicit and the vanilla body is preserved, but this audit did not launch the game.
4. The shared central tree still has 14 blocking geometry diagnostics, so a broad coupled reflow is required before the framework can claim layout completion. The four affected clusters are the opening economy/state fan, founding-settlement fan, depot/recall fan, and professional-defense merge; no local endpoint movement is safe.
5. Dynamic former-host AI targeting is simplified to static `DEN` in the ICE AI profile. The package trigger proves that the former host is dynamic, so this is a material route behavior gap when the host is not Denmark.

## Icon coverage

| Imported focus IDs | Icon IDs | Result |
| --- | --- | --- |
| `independence_wave_overlay_take_stock_of_independence`, `...secure_state_services`, `...mature_independence` | `GFX_goal_independence_wave_founding_administration` | Regular and `_shine` sprites exist in `interface/006_independence_wave.gfx`. |
| `...integrate_release_forces` | `GFX_goal_independence_wave_army_integration` | Regular and `_shine` sprites exist. |
| `...open_foreign_desk` | `GFX_goal_independence_wave_recognition_diplomacy` | Regular and `_shine` sprites exist. |
| `...address_former_host` | `GFX_goal_independence_wave_former_host_settlement` | Regular and `_shine` sprites exist. |
| `...join_network` | `GFX_goal_independence_wave_league_congress` | Regular and `_shine` sprites exist. |
| `...open_regional_ambition` | `GFX_goal_independence_wave_regional_formable` | Regular and `_shine` sprites exist. |
| `independence_wave_ice_choose_constitutional_route` | `GFX_goal_independence_wave_constitutional_state` | Regular and `_shine` sprites exist. |
| `independence_wave_ice_restore_traditional_authority` | `GFX_goal_independence_wave_traditional_restoration` | Regular and `_shine` sprites exist. |
| `independence_wave_ice_establish_emergency_command` | `GFX_goal_independence_wave_military_emergency` | Regular and `_shine` sprites exist. |
| `independence_wave_ice_accept_patron_mandate` | `GFX_goal_independence_wave_patron_client` | Regular and `_shine` sprites exist. |

All 12 imported shared-focus blocks have an intended icon and a matching shine sprite. No icon patch is justified by this audit.

## Localisation and reward mismatch list

- All 12 imported shared-focus IDs have title, `_desc`, and tooltip keys in `localisation/english/006_independence_wave_focus_l_english.yml:396-431`.
- All 12 imported blocks have a `completion_reward` and `ai_will_do` block in `006_independence_wave_focus.txt:3151-3361`.
- Focus names and rewards align: the seven generic titles invoke founding, services, forces, foreign desk, former-host settlement, network, ambition, and maturity effects, while the four ICE titles lock the corresponding constitutional, traditional, emergency, and patron route helpers.
- No localisation/reward mismatch was found and no localisation patch was made.

## AI behavior gaps

Every imported shared-focus block has `ai_will_do`; the route gates are package-aware and the four ICE route nodes use distinct route lock triggers. However, the ICE AI profile hardcodes the former host as Denmark at `common/ai_strategy/006_independence_wave_ice.txt:36,47-48,59-60`:

```text
ai_strategy = { type = befriend id = DEN ... }
ai_strategy = { type = prepare_for_war id = DEN ... }
```

The former host is instead persisted dynamically through `event_target:independence_wave_setup_former_host` and `var:independence_wave_former_host` in `common/scripted_triggers/006_independence_wave_ice_package_triggers.txt:22-30,118-124`. No route-probability sweep or live AI activation proof was run, so route selection remains HOLD.

## High-priority bounded fix recommendation

1. Keep non-targeted ICE build and equipment priorities in `common/ai_strategy/006_independence_wave_ice.txt`, but move target-specific `befriend` and `prepare_for_war` strategy injection into the ICE setup/refresh scripted effect using `add_ai_strategy` with the saved former-host event target. Remove the static `id = DEN` relationship entries and clear/reapply the dynamic strategies when the host target changes or the package cleans up. Existing Chaos Redux dynamic-target patterns at `common/scripted_effects/011_secret_alliance_effects.txt:5819-5825` and `common/scripted_effects/condemnation_sanctions_effects.txt:1221-1249` provide the implementation precedent. This recommendation is source-level only and was not applied here; the parent should validate the exact strategy cleanup syntax before changing it.
2. Treat the central-tree geometry as a coordinated reflow task, not a local focus rewrite. Preserve all existing prerequisites, mutual exclusions, rewards, icons, localisation, and AI weights while resolving the four coupled clusters.
3. Run a live ICE carrier load/save check and a scenario-level AI route sweep after the source fix; MCP inspect/render alone cannot prove imported shared-focus runtime behavior.

## MCP artifacts and validation

The central-tree `hoi4.focus_inspect` artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cfc9197de8cc67e3e4c3fcb8273c734819b77db826ffdc479b87b5718f3bfc37/89d6b8418c021e3d10842cc5f576a1aae3ece1aa193cb33032b4a36c208523bf/focus-inspect.f42cf9c8592f7781.json`.

The central-tree render artifacts are the HTML `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9994d741adf1344f28598b911e5dde71bfc2a4920798fde8d4cc50850d6a8d6b/f3bdc6ab171fc007033af02467c475ddc55e66f4aca9de3da7b36d244308c131/independence_wave_focus_tree.focus.html` and JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c94cc48f9870bdab577e413a696e2c11bf186dd9e29cfef100389622b1c191ad/a7de8e6edbfb4890cb39027c1c8cced074d0b3d2dcf6b8ea616bce71812897a0/independence_wave_focus_tree.focus.json`.

The ICE `hoi4.focus_inspect` artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/daf944b5f680c2274a3b50320cdbb2a5560acb385624e3291c0dfdec71baed57/2bf5cef11251ecb7335549b2ec665143ea9510883a76b5c869665f715ee42fc1/focus-inspect.f42cf9c8592f7781.json`.

The ICE render artifacts are HTML `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1650c21aaefe757b802d68fd8976177e419d3602b66d0c5b2c8c5d0dd69415c3/8232d7452a49494d3cb0d664315c57f021ca4a96d3b52cd1e1f19a1a821c3e48/iceland_tree.focus.html`, SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0f3cd46371e4b568f6b5ffc0dc7c65bedd5339177663eeceda01ca48aec9176f/a853c8310c40f3415769fc75940c4da1c8bb26a43c303cc2ef1c5e6104d069c8/iceland_tree.focus.svg`, and JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/892106fb901f1d111d9cb11ca1db89eeeeae35a23f78f0a0776a179c85ca0825/b3f171c206de53acfe84a0b7960a42683acda34f5d5d2dfb1af847751a86f261/iceland_tree.focus.json`.

Validation was limited to the required wiki and vanilla-documentation review, static source comparison of the vanilla ICE body, focus/source ID and route-trigger inspection, icon/localisation key coverage checks, and `hoi4.focus_inspect` plus `hoi4.focus_render` on the central and ICE trees. `hoi4.focus_rewrite` was not used, no gameplay was launched, and no live save/load or AI probability sweep was run because this was a read-only carrier audit and the geometry blockers are coupled.

## Remaining route risks

- The source carrier imports all 12 Event 006 shared blocks, but runtime expansion of `shared_focus` imports is not confirmed by the available MCP artifacts.
- The central framework remains visually/validator blocked by 14 coupled geometry diagnostics.
- Static `DEN` relationship targets can send ICE AI toward the wrong former host in non-Danish IW-012 setups.
- AI activation and route probabilities remain source-only until the parent runs live validation.
