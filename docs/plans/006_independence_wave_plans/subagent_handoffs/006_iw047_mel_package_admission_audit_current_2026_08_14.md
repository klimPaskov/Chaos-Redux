# IW-047 Mari El package admission audit — current 2026-08-14

## Scope and verdict

This is a read-only admission audit of the IW-047/MEL source after the package-local effects, decisions, focus hooks, AI source, and localisation landed.

## Superseding implementation receipt (2026-08-14)

The earlier state-256/formable and route-flag findings below are superseded by the parent implementation tranche. FORM-12 and FORM-13 now use state 833, the installed Mari El anchor, throughout both consumer specs, generated exact-geometry manifests, source/processed PNGs, DDS outputs, GUI entries, GFX entries, scripted localisation, and qualification helpers. State 256 remains Chuvashia and is no longer used as a MEL proxy. The four generated alternate-history route flag identities (`CIVICX`, `FORESTX`, `SOCIALISTX`, `EMERGENCYX`) have 12/12 TGA and 12/12 DDS evidence; the neutral 1936 flag remains unattested.

**Verdict: BLOCKED. Keep central content attestation, normal preflight, scenario preflight, and deterministic Join fail-closed. Do not widen a central list from this audit.**

The package-local gameplay surface is now materially present, but it is not centrally dispatched or attested, the generic allocator still requires the legacy content-ready gate, and the portrait identity gate remains blocked.

No gameplay, asset, central registry, attestation, preflight, Join, or formable files were edited by this audit.

## Country-package coverage checklist

| Surface | Current evidence | Status |
| --- | --- | --- |
| Identity and origin | `common/scripted_triggers/006_independence_wave_mari_package_triggers.txt:10-19` requires `original_tag = MEL`, package `iw_047`, `liberation_origin.independence_wave`, and excludes Soviet Collapse flags and origin. | Present and correctly guarded locally. |
| Host and release safety | The same trigger file at `61-93` and `150-164` requires state 833 ownership/control, capital 833, a distinct living former host or a valid protected-state proof, and the setup event targets. | Present locally; central execution is absent. |
| Vanilla roster | Vanilla `history/countries/MEL - Mari El.txt:1,101`, `common/characters/MEL.txt:2-14`, and `history/states/833 - Mari El.txt:2-23` provide capital 833, `MEL_zinovy_zhadinov`, and the MEL core. The package checkpoint at `common/scripted_effects/006_independence_wave_mari_package_effects.txt:353-360` only accepts that existing character. | Vanilla identity is preserved; portrait identity/rights remains blocked. |
| Map and anchor | The current registry, region-05 allocator, and package source agree on MEL/state 833 and `river_or_corridor` at `common/scripted_effects/006_independence_wave_packages_region_05_effects.txt:52-61`; allocator eligibility remains gated by `common/scripted_triggers/006_independence_wave_packages_region_05_triggers.txt:40-46`. | Runtime anchor and FORM-12/13 consumers are aligned at 833; package-binding baseline 256 is retained only as historical rebind traceability. |
| Map MCP | Current `hoi4.map_inspect` inspected states 833, 256, 249, 397, 399, and 651 in artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1a5eebb00b1d9eb511d8d7715ba363b170f7da51f0697f78fcbfccd7db1e73c8/8330c690ea0bbff60840d8838912c515192bfe25f24678d61ba6184069506c8c/map-inspect.227c6ae0638c6f11.json`. State membership, networks, and selected IDs were valid, but global building-position and floating-port diagnostics made the map validation fail. The read-only state render passed in artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e055b7b04365920a70aa5119fb6979a3b584c1d81b1da3350217b13f7464b750/9a3b35b2e5d9356e3e2da0d919b2a5e200dd8465232f77e3107e265ff08b9b60/map-state.png`. | No direct state-833 map defect was shown; workspace-wide map diagnostics remain unresolved. |
| Force and starting military | `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv:48` maps IW-047 to `river_jungle`, tradition 47, and five paths including `league_cadres`; constants confirm profile 8, tradition 47, and mask 551 at `common/script_constants/006_independence_wave_force_package_constants.txt:124,338,552`. The current setup at `common/scripted_effects/006_independence_wave_mari_package_effects.txt:416-423` and prepared trigger at `common/scripted_triggers/006_independence_wave_mari_package_triggers.txt:193-203` both require integrate militias, regional guards, secure depots, league cadres, and professional officers while excluding terrain units. | **Locally reconciled; not runtime-proven.** The p47 mask is now source-aligned, but central dispatch and attestation remain absent, so this does not admit IW-047. |
| Ideas and lifecycle | `common/ideas/006_independence_wave_mari_ideas.txt:11-77` defines seven ideas. Package lifecycle and route replacement are in `common/scripted_effects/006_independence_wave_mari_package_effects.txt:12-47,181-274`. | Present locally; not runtime-proven without central dispatch. |
| Decisions and mission | `common/decisions/006_independence_wave_mari_decisions.txt:15-577` defines the founding mission plus ten serialized projects, and `common/decisions/categories/006_independence_wave_mari_categories.txt:9-15` exposes the package category behind the exact setup flag. | Present locally with localisation; no central runtime path. |
| Focus hooks | The shared tree now contains five MEL guards at `common/national_focus/006_independence_wave_focus.txt:119,165,192,1424,1695`, calling the package helpers in `common/scripted_effects/006_independence_wave_mari_package_effects.txt:279-351`. | Present and correctly package-guarded. |
| Focus MCP | Current `hoi4.focus_inspect` artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1620929ffe9f2fb6f3c7f86f0ef7db2f61e580c7d832c20b02f4120e10ef0f59/6b07099d4bb2dd44f996c0bfebb904c2e996af7e8b7b2519c709e5314e68665a/focus-inspect.653a3a130d61c0732e89233cc5b3964d7b1fce657e032eaadb754538565d05bb.json`; it resolved 184 focuses and 196 connectors, with no MEL helper unresolved, but the full workspace retained 14 generic missing-icon blockers. Current read-only render passed artifact generation but retained the same 14 diagnostics in `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6c95b6d7fe0b98c27b9c2f47455dbf4ccc4a13568ac2c53c537dc1c0dd7098c1/ffd9dec82efe3419af6f3e7be98f52a7a8afd65c590ac9af6a47cce927f00b54/independence_wave_focus_tree.focus.html`. | MEL focus wiring is usable; the shared tree is not globally clean. |
| AI | `common/ai_strategy/006_independence_wave_mari.txt:21-70` contains forest-survival, host-restraint, settled-compact, and emergency-guard layers, enabled by package setup and lifecycle flags. | Static source present. |
| AI MCP | Current `hoi4.probability_inspect` artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/07a95ff58593bc2bf819f2675445a17ef01def856c114e4b2f68190b64f3fbb7/bff6cf6865c8dd9a34f3b61be2b5006d39cf1325aea27c70e0a9e558f7622c80/probability-inspect-1ebebf8cc5f5.json`. The adapter reported `no_weighted_surfaces`, zero candidates, and no available adapters. | No quantitative AI ranking, activation, or balance claim is permitted. |
| Cleanup | `common/scripted_effects/006_independence_wave_mari_package_effects.txt:447-495` removes the mission, all ten decisions, all seven ideas, route cosmetic state, package flags, ledger variables, route flags, and provisional party/popularity changes. | Package-local cleanup is comprehensive; the central cleanup dispatcher does not call it. |
| Route cosmetics and flags | Palette-only route tags are defined at `common/countries/cosmetic.txt:1832-1853`, and current consumers/localisation use `MEL_INDEPENDENCE_WAVE_CIVICX`, `MEL_INDEPENDENCE_WAVE_FORESTX`, `MEL_INDEPENDENCE_WAVE_SOCIALISTX`, and `MEL_INDEPENDENCE_WAVE_EMERGENCYX`. | **Present locally, admission-independent:** the generated route package contains 12/12 validated TGA ladders and 12/12 DDS evidence outputs. The neutral 1936 flag remains unattested, and no central admission follows from route cosmetics. |
| Portrait and character assets | No MEL character override, portrait `.gfx`, runtime DDS, or character-scoped source-placeholder consumer exists. The portrait handoff remains HOLD because the exact vanilla Zinovy identity has no rights-clear attributed image, and the period Mari officeholder alternatives are different people or post-1936. | **Blocked identity and rights gate.** Do not substitute a generic or opposite person. |
| Localisation | `localisation/english/006_independence_wave_mari_l_english.yml:1-110` covers parties, four current cosmetics, seven ideas, category, founding mission, ten projects, tooltips, and helper-facing names. | Present and current; no runtime category renderer is available in the installed MCP. |
| Formable linkage | The current FORM-12/13 consumer specs, manifests, generated state pieces, GFX, scripted GUI, scripted localisation, and qualification helpers use state 833 for MEL, alongside carrier/member states 249, 651, 399, and 397. The separate `form_idel_uralic_republic` manifest still carries both 833 and 256 under its own independent formable contract. | **Rebound and source-aligned locally.** Central MEL admission and formable-dependent attestation remain fail-closed until the complete package gate is accepted. |

The source hardening recorded in `006_form12_form13_mel_state256_fail_closed_hardening_2026_08_14.md` is historical evidence for the intermediate fail-closed state. It has been superseded by the exact state-833 consumer rebind described above.

## Current FORM-12/13 rebind evidence (2026-08-14)

The consumer specs were rebuilt from the canonical state registry with required and candidate state IDs `249, 397, 399, 651, 833`. Both generated manifests are complete, and the runtime generator refreshed the state-puzzle GFX, scripted GUI, scripted localisation, localisation, and DDS ladders. A scoped source scan found no FORM-12 or FORM-13 runtime reference to `state_256`; the separate Idel-Uralic formable's state-256 member remains independent and unchanged.

The required map inspection of states `833, 256, 249, 397, 399, 651` returned `MAP_INSPECTED` at revision `a08888ecbb9231a96578e1d3e7cf482281921d2bbdddefecd9c2f950dd49aa01`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/77d29b65e30b4ae5a8a11e39648eb68c149ee20f69fa972090d581f26d8fea9c/68f4908098d0aaddcca36c44d2e1f143e1bf44f9fcdfdf56fc052da872a41712/map-inspect.a08888ecbb9231a9.json`. State membership, networks, and selected IDs passed; the aggregate validation remains false only because unrelated workspace building-position and floating-port diagnostics are truncated. The paired state render returned `MAP_RENDERED` with PNG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0550658fb9a890f6226150e4b0ff98fd5cfcbdbe6a75da2372173d4cf4d8dacc/6128ba19a336cb046ae1e47ed47ea84913cd82577a480ee894f223e1c601409a/map-state.png` and passed its render validation.

The grouped formable GUI inspection used scenario `E6_FORMABLE_STATE_PUZZLE_GUI_REBOUND_2026_08_14` and returned `GUI_INSPECTED` at revision `bfed1fd8eadbbfc5b20d7769acdbffa26b2d29b5a6706c5609c0c658196f1095`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f7f7bc0e77369342e0fe7b9ac0a59aacaae8ea1ca3cd731ee369b539b1afb452/4d6831fbf207a65d52ea53beaf248f3977ab39a6e1306cd457a7cd9ef05c07bc/gui-inspect.bfed1fd8eadbbfc5.json`. It inspected 93 elements and retained aggregate workspace graph/overlap diagnostics, so it is reachability evidence rather than family-isolated acceptance. The paired render returned `GUI_RENDERED` with SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9654598f01c40a19da62a51464f8e7698112a52589404fd484b76aaf61e8203f/e61d7d6ed187a985019eaf508d0bd3f6834dfd2f3514aa81f11fc2fc0862fa9c/chaosx_independence_wave_formable_state_puzzle_w-full.svg`; its validation remained false because the shared graph diagnostics are aggregate and truncated.

## Central admission boundary

`common/scripted_effects/006_independence_wave_package_dispatch_effects.txt:13-41,45-72,92-119` has no MEL setup, final-validation, or cleanup wrapper.

`common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-62` has no `iw_047` adapter branch, and its content attestation OR at `159-202` has no MEL entry.

Normal preflight at `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:207-214` therefore rejects IW-047 because the adapter and attestation proofs are absent, and the scenario preflight at `411+` has no exact IW-047 branch.

`common/scripted_effects/006_independence_wave_join_effects.txt:213-247` fixed deterministic probe order contains no IW-047, and `common/scripted_triggers/006_independence_wave_join_triggers.txt` has no exact IW-047/MEL branch.

The scenario rank array entry in `common/scripted_effects/006_independence_wave_scenario_effects.txt:284` is only ranking metadata and is not executable admission.

The generic allocator still calls `is_independence_wave_candidate_tag_available`, which requires the legacy `independence_wave_package_content_ready` flag at `common/scripted_triggers/006_independence_wave_package_triggers.txt:43-49`; no setter for that flag was found in the current package/source scan, and no package-local source is allowed to invent it as a shortcut.

## Required parent actions before any central widening

1. Preserve the completed state-833 registry, runtime, and FORM-12/13 consumer rebind; keep package-binding baseline 256 only as historical traceability and do not reintroduce state 256 as a MEL proxy.
2. Preserve the completed four-route generated flag package while keeping the neutral 1936 flag unattested.
3. Resolve the `MEL_zinovy_zhadinov` identity and portrait rights gate without generic fallback or silent person substitution, or approve a distinct institutional consumer with its own character contract.
4. Re-run package-specific static and MCP evidence after those fixes, then add central setup/final/cleanup dispatch, adapter, attestation, normal/scenario preflight, and deterministic Join entries only after every gate is independently evidenced.

## Simplifications and limitations

No gameplay or central files were changed by this audit, no map write was attempted, and no live HOI4 launch or save validation was performed.

The Event 006 MCP inspection of `chaosx.nr6.350` returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics but deferred workspace-wide helper and lifecycle projections in artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0f45d027565568c1eed29cefcb9a688e617613629b43f6ae95ae11e66fb8cd9b/5814cd1334aed180a28defe92b053846e882dc94bd12c3f711f4dd3cad41c778/event-state_flow-d21fdfa2723e.json`; the corresponding render was `EVENT_RENDERED_PARTIAL` with PNG artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/383c232e5e703f2969d6d179db6f42256a3e69e4f7d56454501355e14f2ae4a4/f7db25697d3c95a5dab03b0b45a0e2c4c40557ff3ced407b8d2c07a4812729a7/event-state-d21fdfa2723e.png`, and is evidence only for the shared event framework, not MEL admission.

The installed MCP exposes no decision-category renderer and no Technology Tree Viewer, so no engine-level category or technology claim is made.

Older IW-047 handoffs that say MEL effects, decisions, localisation, or focus hooks were absent are superseded by the current package-local source; the central admission verdict remains fail-closed.
