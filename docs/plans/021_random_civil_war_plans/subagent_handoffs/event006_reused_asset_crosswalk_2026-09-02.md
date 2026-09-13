# Event006 reused asset crosswalk for Event021

Status: incomplete bounded partial, written read-only on 2026-09-02. This handoff maps the exact Event021 admission array and the Event006 visual paths recovered before the requested stop; it does not claim package completion, visual acceptance, rights clearance, or engine/render validation.

## Exact Event021 admission

Event021 currently admits exactly 32 Event006 package IDs through `common/scripted_effects/006_independence_wave_event021_adapter_registry_effects.txt:16-47`: `iw_001/SCO`, `iw_002/WLS`, `iw_004/BRI`, `iw_006/AFX`, `iw_007/AGX`, `iw_008/RHI`, `iw_009/BAY`, `iw_010/AJX`, `iw_012/ICE`, `iw_014/CAT`, `iw_017/COR`, `iw_018/ARX`, `iw_019/ASX`, `iw_023/TRA`, `iw_024/AXX`, `iw_026/MAC`, `iw_027/BAX`, `iw_028/BBX`, `iw_029/BOS`, `iw_030/MNT`, `iw_031/KOS`, `iw_033/KAR`, `iw_038/RUT`, `iw_040/KUB`, `iw_041/CRI`, `iw_044/TAT`, `iw_045/BSK`, `iw_070/ARM`, `iw_071/GEO`, `iw_072/AZR`, `iw_173/HAW`, and `iw_184/HBX`.

The central runtime adapter trigger contains 40 IDs, with eight adapter-only IDs outside the Event021 array: `iw_043`, `iw_058`, `iw_177`, `iw_179`, `iw_093`, `iw_098`, `iw_013`, and `iw_015`.

The machine-readable package table, anchor states, setup sources, family assignments, and every recovered asset-path mapping are in [event006_reused_asset_crosswalk_2026-09-02.json](C:/Users/klimp/OneDrive/Documents/Paradox%20Interactive/Hearts%20of%20Iron%20IV/mod/chaos_redux/docs/plans/021_random_civil_war_plans/subagent_handoffs/event006_reused_asset_crosswalk_2026-09-02.json).

## Lifecycle result

Event006 recognition does not replace the adapter flags with an active-origin receipt in the inspected Event021 path. `event021_record_event6_origin` records `random_civil_war_event6_origin_recorded`, origin kind, date, and generation in `common/scripted_effects/021_random_civil_war_effects.txt:906-917`, while `event021_apply_event6_origin_adapter` writes only `random_civil_war_event6_adapter_complete` and `random_civil_war_origin_adapter_complete` in the following adapter block.

The parent source update adds `is_independence_wave_event021_package_country` at `common/scripted_triggers/006_independence_wave_triggers.txt:16-27`. It requires the two adapter-complete flags, `independence_wave_event021_adapter_setup_proven`, `random_civil_war_event6_origin_recorded`, `independence_wave_package_id`, and a non-active, non-ended origin. `is_independence_wave_package_content_active` now reuses that exact branch at `common/scripted_triggers/006_independence_wave_triggers.txt:29-44`.

Core cleanup at `common/scripted_effects/021_random_civil_war_effects.txt:1633-1640` now preserves `random_civil_war_event6_adapter_complete`, `random_civil_war_origin_adapter_complete`, and `random_civil_war_event6_identity_ready` only when `is_independence_wave_event021_package_country` is true, and clears those three receipts when the predicate is false. This removes the prior stale claim that core cleanup unconditionally clears the completion/origin-adapter receipts.

The resulting content gate is conditional rather than uniformly false: a living complete package can keep `is_independence_wave_package_content_active` true through the new exact branch, while an incomplete or ended package loses that branch. The strict `independence_wave_active_origin` contract is unchanged, so this source update does not itself establish an Event006 active-origin receipt.

The independent player-surface gate at `common/scripted_triggers/006_independence_wave_triggers.txt:42-51` rejects all four lifecycle flags, including `independence_wave_event021_adapter_setup_proven`. The new receipt branch fixes ordinary post-cleanup content loss for a living complete package, but it does not fix this player-surface gate, so required local formable/progression categories and explicitly global league/network/evolution surfaces remain blocked by the same helper until routing changes.

## Consumer gate split

Country-local Event006 categories use `is_independence_wave_active_country` and include the BRI, CAT, BBX, ICE, KOS, COR, ARX, ASX, MNT, HBX, HAW, AXX, BAX, KUB, TAT, BOS, MAC, RHI, BAY, RUT, AJX, SCO, WLS, Transcaucasus, TRA, AFX, and AGX package categories defined in `common/decisions/categories/006_independence_wave_categories.txt`.

The player-surface helper currently blocks two classes that must remain distinct in review. Required country-local content includes recognition, patron, borders, formable, formable transaction, regional formables, FORM-16 integration, and the FORM-01/02/03/04/05/08/09/39/48 invitation/compact progression categories. Explicitly protected global surfaces identified in this bounded pass are `independence_wave_rival_bloc_category` and `independence_wave_scenario_ledger_category`; other network/evolution names remain unresolved rather than being inferred as global.

The full focus framework is `independence_wave_focus_tree` in `common/national_focus/006_independence_wave_focus.txt:38-46`; its use trigger requires `is_independence_wave_package_content_active` in `common/scripted_triggers/006_independence_wave_focus_triggers.txt:32-38`. A living complete package can satisfy that use-trigger prerequisite through the new branch, but the tree country modifier still requires strict active-origin state. Formable state-puzzle triggers also require package content activity, while FORM-16 integration additionally uses the unchanged player-surface gate.

For classification, recognition, patron, border, formable, and regional progression categories are required country-local surfaces in this audit. Only the explicitly identified `independence_wave_rival_bloc_category` and `independence_wave_scenario_ledger_category` are classified as protected global surfaces in this bounded correction; other network/evolution category names remain unresolved rather than being inferred.

## Concrete reused asset paths

The current wired portrait crosswalk contains 46 GFX sprite-registration rows and 46 unique runtime DDS paths. This is not a count of unique live characters or proof that all rows are selected by every package; actual character reachability was not enumerated in this partial. The rows are the current Event006 GFX registrations for BRI, AXX, BAX, BBX, BOS, MNT, KOS, RUT, BSK, MAC, COR, ARX, ASX, AFX, AGX, RHI, BAY, AJX, SCO, WLS, HBX, and HAW under `interface/006_independence_wave_portraits_registry.gfx`, `interface/006_independence_wave.gfx`, and `interface/006_independence_wave_small_assets.gfx`.

Every one of those rows is review-pending. The prior portrait handoff `docs/plans/006_independence_wave_plans/subagent_handoffs/006_portrait_wiring_reconciliation_2026-08-30.md` reports its selected/runtime portraits as grounded `source_placeholder` rather than styled final; this audit did not promote that evidence to a final or rights pass.

The exact current portrait runtime paths are machine-readable in the JSON under `asset_crosswalk.portraits`, including the current ARX mappings to Emilio Lussu, Luigi Mella Santelia, and Vittorio Verne, and the current RHI/BAY shared mappings to Josef Friedrich Matthes and Rupprecht of Bavaria.

The ten admitted packages without a current mod Event006 portrait row are `iw_012/ICE`, `iw_014/CAT`, `iw_023/TRA`, `iw_033/KAR`, `iw_040/KUB`, `iw_041/CRI`, `iw_044/TAT`, `iw_070/ARM`, `iw_071/GEO`, and `iw_072/AZR`. Known source-only or vanilla consumer evidence is listed in the JSON, including ICE Sveinn Bjornsson, CAT Lluís Companys, KAR Ukki Vainamoinen and Jalmari Takkinen, and GEO Giorgi Kvinitadze, Noe Zhordania, and George Bagration Mukhrani.

The prior unresolved portrait/source-clearance inputs are YAK Anatoly Pepelyayev, BYA Ardan Markizov, BYA Mikhei Erbanov, ALT Grigory Gurkin, ALT Samuil Yufit, FER Alexander Krasnoshchyokov, FER Pyotr Nikiforov, KUR Seyid Riza, ACX Cornish Port and Mines Committee, ARX Gioacchino Solinas, FIJ Ratu Sir Lala Sukuna, FIJ Vishnu Deo, and GLC Alexandre Bóveda. Of those, only ARX is in the Event021 package set, and Gioacchino Solinas is evidence-only with no current live ARX runtime consumer.

The concrete currently wired ARX orphan runtime files are `gfx/leaders/006_independence_wave/portrait_ARX_independence_wave_gavino_piras.dds` and `gfx/leaders/006_independence_wave/portrait_ARX_independence_wave_vittorio_pala.dds`.

Known shared focus paths are `gfx/interface/goals/006_independence_wave/goal_independence_wave_{founding_administration,constitutional_state,popular_councils,traditional_restoration,military_emergency,patron_client,recognition_diplomacy,army_integration, infrastructure_authority,former_host_settlement,league_congress,regional_formable,high_chaos_sovereignty}.dds` plus the AJX path `gfx/interface/goals/006_independence_wave/goal_independence_wave_ajx_neutral_commission.dds`.

Specialized focus paths recovered are the AFX set under `gfx/interface/goals/006_independence_wave/afx/`, the HBX set under `gfx/interface/goals/006_independence_wave/goal_independence_wave_hbx_*.dds`, the HAW set under `gfx/interface/goals/006_independence_wave/goal_independence_wave_haw_*.dds`, the Mediterranean set under `gfx/interface/goals/006_independence_wave/mediterranean/`, the RHI/BAY set under `gfx/interface/goals/006_independence_wave/rhineland_bavaria/`, and the FORM-03 set under `gfx/interface/goals/006_independence_wave/form03/`. The JSON gives the exact filenames and package scopes for each recovered set.

Known shared idea paths are the eight files under `gfx/interface/ideas/006_independence_wave/` for improvised government, unrecognized state, fragmented command, unsettled borders, patron pressure, league membership, founding identity, and post-release instability.

Known specialized idea paths are the four RHI files, four BAY files, and six FORM-03 files recorded in the JSON. The complete Mediterranean and Transcaucasus specialized idea lists remain explicitly unresolved in this partial.

Known shared decision paths are the twelve files under `gfx/interface/decisions/006_independence_wave/` for recognition, government, army integration, depot/border, former-host, patron, network, league, border arbitration, formable proclamation, and integration missions. The JSON also lists the exact recovered FORM-03, Mediterranean, and FORM-05 decision paths and marks the RHI/BAY custom decision set as incomplete.

Known formable emblem paths are only FORM-05 at `gfx/interface/006_independence_wave/emblems/independence_wave_formable_form_05.dds` and FORM-48 at `gfx/interface/006_independence_wave/emblems/independence_wave_formable_form_48.dds`. Other family emblem paths were not established from the collected GFX evidence.

No Event006 country/cosmetic flag runtime path is promoted here. The identity/carrier tag map is exact in the JSON, but flag/cosmetic-tag asset extraction remains unresolved and no flag is visually passed.

## Proved package repair and remaining limits

`iw_023/TRA` was admitted by the 32-entry Event021 array, but its setup source assigned `independence_wave_focus_assignment = additive_overlay` while the Event021 package-setup proof requires `full_framework`. The setup adapter now requests `full_framework`, and its package proof now requires the matching full-framework and generic-tree flags. This repairs the source-level admission/readiness mismatch; it does not prove the package's complete runtime, asset, or in-game consumer acceptance.

The new complete-package branch does not change any global decision/category routing. The country-local package categories and local sections of the aggregate Event006 decision file now use `is_independence_wave_event6_local_content_active`; required local formable/progression categories and explicitly global network, league, evolution, and adapter-only categories continue to use their strict origin-aware predicates. All remain separate from the new content receipt.

## Limitations and handoff state

This is intentionally not a whole Event006 audit. The TRA setup/validation contract was edited as the bounded repair described above; no artwork was generated or repaired by this crosswalk, no visual asset was passed here, and no commit was made.

HOI4 MCP read-only event, focus, map, technology, probability, and GUI calls were attempted earlier but timed out before returning artifacts; no engine/render evidence or tool-availability conclusion is claimed.

Other Event021 lifecycle cleanup paths still need a separate audit, including the lifecycle cleanup block around `common/scripted_effects/021_random_civil_war_lifecycle_effects.txt:910-927` and the absorbed-adapter path at `:984-1003`.

The parent can begin individual reused-visual review from the JSON exact path lists, then resolve the ten admitted package portrait gaps, the current 46-row source-placeholder/final-rights status, the missing flag paths, and the post-cleanup receipt/player-surface gates.
