# IW-042 Galicia-Lodomeria registered-tag compatibility handoff (2026-08-14)

## Status

The bounded IW-042 GAL compatibility tranche is complete as a dormant package-local trigger/effect adapter and is intentionally not promoted into Event 006 central admission or runtime dispatch.

No central adapter, content attestation, scenario preflight, release list, Join route, asset, localisation, workbook, country history, vanilla CZE focus, or unrelated file was edited.

The parent agent owns review and commit; this subagent did not stage or commit.

## Changed files and identifiers

- `common/scripted_triggers/006_independence_wave_iw042_gal_compatibility_triggers.txt`
  - `is_independence_wave_iw_042_gal_compatibility_context`
  - `has_independence_wave_iw_042_gal_anchor_surface`
  - `has_independence_wave_iw_042_gal_compact_surface`
  - `has_independence_wave_iw_042_gal_vanilla_surface`
  - `has_independence_wave_iw_042_gal_cze_core_witness`
  - `has_independence_wave_iw_042_gal_compatibility_contract`
- `common/scripted_effects/006_independence_wave_iw042_gal_compatibility_effects.txt`
  - `independence_wave_iw_042_gal_compatibility_clear_institution_selection`
  - `independence_wave_cleanup_iw_042_gal_compatibility`
- Selector flag reserved for a future source-backed institutional owner: `independence_wave_iw_042_gal_institution_selected`.

The adapter requires `original_tag = GAL`, `is_independence_wave_active_country = yes`, `independence_wave_active_origin`, `liberation_origin.independence_wave`, exact `independence_wave_package_id.iw_042`, and the selector flag.

The strict contract additionally requires ownership, control, GAL cores, and capital state 91, the same ownership/control/GAL-core surface on state 89, and the installed `generic_focus` tree.

The cleanup effect only clears the selector under that strict contract and never mutates origin, package identity, state ownership, cores, capital, history, leader, or assets.

## Source and vanilla identity findings

The IW-042 research row is `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:43`, which binds Galicia-Lodomeria to registered tag `GAL`, high-chaos-only scope, exact anchors `91|89`, and reservation group `RG-91-89`.

The current package loader is `common/scripted_effects/006_independence_wave_packages_region_04_effects.txt:107-151`; it reserves state 91 and attempts compact state 89 without any GAL compatibility adapter call.

The current package availability gate is `common/scripted_triggers/006_independence_wave_packages_region_04_triggers.txt:76-82`; it checks GAL tag availability, state-91 anchor availability, and the exact IW-042/reservation-group arrays without touching this dormant contract.

Vanilla registers `GAL = "countries/Galicia and Lodomeria.txt"` at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/country_tags/00_countries.txt:371`.

Vanilla `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/GAL - Galicia and Lodomeria.txt` retains capital state 88, three research slots, neutrality politics, and no `recruit_character`, `add_country_leader`, or `set_country_leader` entry.

Vanilla has no GAL-specific character definition in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/characters`; no GAL portrait or leader wiring is therefore safe to add in this tranche.

Vanilla state 91 is `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/91-Tarnopol.txt` and state 89 is `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/89-Krakow.txt`; both are currently POL-owned and neither has a vanilla GAL core.

Vanilla CZE focus `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/national_focus/czechoslovakia_mu.txt:1650,1690,3125-3127` keeps the idempotent `add_core_of = GAL` and `release_puppet_on_controlled = GAL` behavior on state 88; the adapter exposes this only as the read-only `has_independence_wave_iw_042_gal_cze_core_witness` and never rewrites it.

Vanilla Poland focus `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/national_focus/poland.txt:7756-7790` is a separate Habsburg Galicia route that restores the diet and adds the Galicia-Lodomeria ruler trait; it is not part of IW-042 and was not changed.

Vanilla localisation identifies `GAL` as Galicia and Lodomeria and `GAL_neutrality` as Kingdom of Galicia and Lodomeria; no localisation change is required for this dormant adapter.

## Coverage checklist

| Surface | Result | Finding and exact scope |
| --- | --- | --- |
| Country tag and identity | PASS for bounded adapter | Registered `GAL` is guarded by exact `original_tag`, exact IW-042 package id, and active Event 006 origin. |
| History and registered-tag preservation | PASS for bounded adapter | GAL history is read-only evidence with capital 88; no history writer or tag replacement was added. |
| Map and state setup | PASS for bounded adapter / runtime unproven | Exact Event 006 anchors are 91 and 89; strict contract requires both owned, controlled, and GAL-cored with capital 91. Current vanilla owner/core state remains POL/POL+UKR and is intentionally untouched. |
| CZE-origin core/release interaction | PASS for preservation | Vanilla CZE state-88 GAL core/release effects remain the only CZE-origin writer; the adapter only observes a core witness. |
| Leader, character, portrait, flag, advisor, party | HOLD | Vanilla GAL has no GAL leader/character and no asset route. Any future named institutional identity needs source review and `chaosx_portrait_creator`; no fictional portrait or localisation was invented. |
| Focus tree | PASS for bounded adapter / baseline diagnostics | GAL has the installed generic focus tree witness. CZE and POL linked vanilla trees were inspected/rendered read-only; their unrelated baseline missing-icon/reference diagnostics remain outside this tranche. |
| Decisions, missions, ideas, and assets | HOLD / no surface | No IW-042 package decision, mission, idea, icon, flag, or portrait exists in scope and none was created. |
| Military, technology, industry, supply, and production | HOLD / deferred package | No starting setup or force package is admitted by this dormant adapter; no technology viewer is installed, so no Technology Tree Viewer evidence exists. |
| AI and playability | HOLD / central surface unchanged | No IW-042 AI strategy or package AI was added. The central Region-04 random list remains unchanged and was only inspected read-only. |
| Cleanup and replay safety | PASS for bounded adapter | Cleanup is idempotent and fail-closed; it clears only the package-local selector under the exact contract. |

## MCP evidence

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.

Map inspection for states 91/89 succeeded with no missing geometry or state/region/network membership errors for the selected states; the selected-state inspection artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4161998b9908a3efb2e59d1f3dde8613eb255c70128a39dd929500410e1a352d/2107d6da03547383446d8f2025695915f9a2933b55e183a35e1bce9218312dd4/map-inspect.24bebf72ae84437c.json`.

The bounded owner-layer map render with coastlines, victory points, resources, buildings, supply nodes, and railways passed validation; its JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c0d0bc8e50fc6856b219c9805f27b7990a35c7f16410772e7be3071b48d53e48/603dcc3251e66b139f4bacfcf11b06bafd0dbc8b6d27256ba97a5d04feba256b/map-owner.json` and its rendered PNG is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9a9b699614e18b16f89981f73bc332c1890dd0f192ef7d835376c3733745c209/6fed5589e5231e6a0237169c5eef3e32da1e894202d2c18705a34e916bf261b9/map-owner.png`.

CZE `mu_czech_focus` inspection artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4e314ed6be593659e583d187e320dbe967e761db8576deed6d211046208fed68/b2c7788e787ad21b445b44144bb7f62e2ae09cf219ee3b9f01032a1320b73261/focus-inspect.5bb17398adee2259.json`.

CZE `mu_czech_focus` rendered JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9b551dde63d82889366f9707dfec75887b95fd349fcd433b0458e07eff39b812/15d327f38c6f9a129d4c39fc5d1f599afa595c8a146abca6813db27da7abf866/mu_czech_focus.focus.json`.

POL `polish_focus` inspection artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4709a037fdfdbacd9a3abb492c09e06296452e33ecaa18458f24eb8fc29aae4f/92ad488712405e8e8dd0d142cc9559cf0db66f1eb2e34f75b31651e18ff351a1/focus-inspect.5bb17398adee2259.json`.

POL `polish_focus` rendered JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9fdc7d901d4e9bfa9ac600d3c66c1d931fd693f7824d440a17418beec0e3ac0b/a01e6b1a26e20475af50b1608d6031a6a5a11361ed05a194d0fadaa2bdfd94e1/polish_focus.focus.json`.

The focus artifacts report the installed vanilla baseline's existing missing icon/gameplay references and were not treated as IW-042 defects.

Event 006 `hoi4.event_inspect` returned `EVENT_INSPECTED_PARTIAL` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3cb368c1050f023b3da7fedb01b92680a9d51a04c164708ac8cb3d525c1ac3ac/b9f04288fc3461eea99254a96c5102a8101e1b34cf9ea08b4d08c27e335d4208/event-scan-741883f50501.json`.

The corresponding Event 006 overview render returned `EVENT_RENDERED_PARTIAL` with manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/64ce61a29fa5d5c9cbe152fc329db203cf47b5185c99d9907fafac92837c4735/1fb837173598f60ce30f9d80e33eb3979729baf971c2d2ec8056f5caaa2d8ad5/event-overview-741883f50501-manifest.json` and PNG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7fa0175af9c12eb9eec117b596be4f77755cc0e435036e3025619b83817fa8d2/ab5684316d4de6da43106a0f0988a872aaf5f1563725fec48634ca5988b7ad04/event-overview-741883f50501.png`.

The Event Chain Viewer did not include the mod `events/006_independence_wave.txt` in its `filesScanned` inventory despite file/source/event selectors and instead scanned the vanilla event inventory; this is the exact unresolved MCP limitation for mod Event 006 source evidence.

The Region-04 weighted source was inspected read-only with `random_list`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b51fac93d010fe3d487ab60c307b4ab417f48fafbe8dde9ae5db7d50ff08b05e/abb47daadebdb416eb2270a864d86a3805bc3b66f00a8e7d4bf71dd085e5a131/probability-inspect-e8f1792fa6b1.json` reports eight candidates and no unresolved inputs. This tranche changed no weighted source, so no before/after probability comparison applies; the parent-owned probability audit remains authoritative for central allocation balance.

## Validation and remaining risks

Meaningful validation covered offline wiki and vanilla documentation syntax for `original_tag`, `is_independence_wave_active_country`, `owns_state`, `controls_state`, `capital_scope`, `is_core_of`, `has_focus_tree`, conditional effects, and cleanup; source review covered the exact GAL history, states 91/89, CZE/POL focus references, and registered-tag searches; and MCP read-only map, focus, event, and weighted-surface inspections were run as listed above.

No live Hearts of Iron IV launch, save/load, or in-game execution was run because agents must not launch the game; no Technology Tree Viewer is installed; and the Event Chain Viewer mod-source inventory limitation remains unresolved.

Remaining setup and identity risks are that the strict contract cannot pass until a future package owner creates the state-91/state-89 GAL cores and sets a source-backed institutional selector, and no GAL leader, portrait, flag, advisor, party, decision, force, or AI route exists yet.

No plan handoff beyond this durable adapter handoff was needed.
