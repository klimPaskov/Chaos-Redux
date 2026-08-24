# Event 014 focus final audit v4

Date: 2026-08-24

## Scope and authority

This read-only audit covers the live consolidated Event 014 focus source at `common/national_focus/014_cannibalism_focus.txt`, its focus-local rewards, AI weights, localisation, icon registry, terminal triggers, and the existing Warlord, Unified, and Wendigo integration hooks. The current authority was checked against `docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_5_focus_tree_architecture.md`, `part_7_hannibal_reveal_and_unification.md`, `part_8_wendigo_and_world_end.md`, `part_9_ai_balance_and_integrations.md`, `part_12_acceptance_criteria.md`, `matrices/focus_route_matrix.md`, `matrices/ai_strategy_matrix.md`, and the supersession notes in `docs/plans/014_cannibalism_plans/014_removed_origin_cleanup_2026-07-15.md`.

The offline Paradox references consulted were `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md`, `Data structures - Hearts of Iron 4 Wiki.md`, `Triggers - Hearts of Iron 4 Wiki.md`, `Effects - Hearts of Iron 4 Wiki.md`, `Modifiers - Hearts of Iron 4 Wiki.md`, `Localisation - Hearts of Iron 4 Wiki.md`, `Scopes - Hearts of Iron 4 Wiki.md`, `On actions - Hearts of Iron 4 Wiki.md`, `Event modding - Hearts of Iron 4 Wiki.md`, `Decision modding - Hearts of Iron 4 Wiki.md`, `Idea modding - Hearts of Iron 4 Wiki.md`, and `AI modding - Hearts of Iron 4 Wiki.md`. Vanilla precedent and documentation were checked in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/national_focus/australia.txt`, `.../common/national_focus/abdacom_shared_branch.txt`, and the installed `documentation/effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, and `script_concept_documentation.md`.

No gameplay source was changed by this v4 audit. The existing concurrent four-line Wendigo coordinate edit and concurrent Event 014 localisation/unit work were preserved.

## Route coverage

| Surface | Spec target | Live source | Route coverage and gate result |
| --- | ---: | ---: | --- |
| Unified Hannibal / CBL | 108 | 108 focus blocks under `cannibalism_unified_focus_tree` (`common/national_focus/014_cannibalism_focus.txt:24`) | Opening convergence (8), three mutually exclusive Warlord disposition routes (15), three mutually exclusive Supreme hierarchy routes (15), Continental Larder with four methods (23), army (14), navy (8), air (7), intelligence/cells (8), expansion (4), counterwar (4), and ordinary terminal (2). The tree root requires CBL, `cannibalism_unified_country`, `cannibalism_reveal_complete`, and excludes `cannibalism_wendigo_hannibal_country` (`:28-36`). |
| Reusable Warlord | 68 | 68 focus blocks under `cannibalism_warlord_focus_tree` (`:1527`) | Survival trunk (`:1546`), hierarchy, shared Larder plus rapid/managed/mobile methods, military doctrine, three four-focus origin overlays, regional predation/infiltration, and Evolution II network alignment/manipulation/defiance (`:2728`). The country gate requires the active reusable Warlord slot, open Warlord decisions, and no release-pending flag (`:1530-1538`). |
| Original-ZZZ Wendigo overlay | 28 | 28 focus blocks under `cannibalism_wendigo_focus_tree` (`:2953`) | Five merge-trunk, five winter-hunger, five paid recruitment, five cannibal-legacy, five transformation-countdown, and three alternate-terminal focuses (`:2974`, `:3095`, `:3200`, `:3299`, `:3410`, `:3528`). The root and first focus preserve `original_tag = ZZZ`, the transformed-country flag, reveal completion, overlay availability, Hannibal-Wendigo character, and no existing world end (`:2957-2999`). |
| Total | 204 | 204 | Exact target count. No route family is missing or replaced by a generic fallback. |

Prerequisite source checks found no dangling focus reference. The OR/AND-sensitive terminal gate is explicit: the three completed preparation focuses are inside one `custom_trigger_tooltip` block at `:1476-1481`, while the `cannibalism_can_complete_ordinary_world_end` trigger supplies the separate operational package requirements. Warlord origin roots use both `allow_branch` and `available` on the matching Island, Siege, and March flags (`:2326-2327`, `:2409-2410`, `:2492-2493`). The Wendigo countdown uses one visible parent edge plus a five-focus custom AND gate at `:3505-3512`. The 19 mutual-exclusion declarations contain 42 symmetric references; no asymmetric mutex was found.

## Missing or simplified content

No missing focus route, simplified branch, copied terminal, or generic replacement was found against the current three-tree specification. The retired Prison Host/Lockhouse origin is absent from the live runtime surfaces: a case-insensitive search of `common`, `events`, `history`, `interface`, and `localisation` returned zero `Prison Host`, `prison_host`, `origin_prison`, `warlord_prison_`, `lockhouse`, or `lock_house` identifiers. Legitimate prison ledgers, prisoner trains, prison hulks, and prison/port cells remain ordinary logistics or intelligence focuses rather than a fourth origin.

The focus helpers are not cosmetic-only rewards. The unified Bone Guard focus at `:957` calls `cannibalism_unified_focus_bone_guard_command`, which opens paid guard recruitment, capacity, Bone Riders, and Elephantry at `common/scripted_effects/014_cannibalism_effects.txt:15937-15942`. The Warlord Bone Guard focus at `:2225` calls the helper that opens paid guard recruitment, Bone Riders, and Elephantry (`common/scripted_effects/014_cannibalism_effects.txt:17551-17555`). The Wendigo Pack focus at `:3233` opens paid Pack and receipt-backed muster contracts (`common/scripted_effects/014_cannibalism_effects.txt:19416-19422`). No focus directly grants free population, manpower, equipment, or units.

## Icon coverage

| Surface | Focus icon IDs | Base DDS registrations | Dimensions | Duplicate/missing result |
| --- | ---: | ---: | --- | --- |
| Unified CBL | 108 | 108 | 94x86 | 0 missing, 0 bad dimensions, 0 duplicate SHA-256 hashes |
| Warlord | 68 | 68 | 94x86 | 0 missing, 0 bad dimensions, 0 duplicate SHA-256 hashes |
| Wendigo | 28 | 28 | 94x86 | 0 missing, 0 bad dimensions, 0 duplicate SHA-256 hashes |
| Total | 204 | 204 | 94x86 | `interface/014_cannibalism.gfx` has 408 matching base/shine sprite registrations; all 204 base mappings resolve |

The source uses one unique `icon = GFX_goal_*` per focus. The exact registrations include `GFX_goal_CBL_reveal_the_command` at `interface/014_cannibalism.gfx:236`, `GFX_goal_ZZZ_wendigo_bind_the_two_hungers` at `:475`, and `GFX_goal_cannibalism_warlord_survive_the_first_encirclement` at `:983`.

## Localisation and reward mismatch list

No focus-localisation mismatch was found. The Event 014 localisation file has a UTF-8 BOM, zero duplicate keys, and all 204 implicit title keys, 204 description keys, and 204 custom tooltip keys resolve to nonempty strings. The 204 `custom_effect_tooltip` values are unique, and the first hidden focus helper in each reward is unique. The source and localisation currently agree for the paid Bone Guard, Bone Riders, Scavenged Elephant Column, Wendigo Pack, ordinary-terminal, and Wendigo-terminal contracts. The Warlord title/description/tooltip values contain zero pre-reveal `Hannibal`, `Lecter`, `Wendigo`, `Carthage`, `Barca`, or ancient-general identity terms.

Terminal wording is consistent with the effect boundary. `CBL_final_global_mobilization_tt` and `CBL_dismantle_the_ordinary_world_tt` describe the paid preparation and final levy, while the latter does not claim that the focus alone sets `world_end`. `ZZZ_wendigo_the_world_beneath_winter_tt` explicitly says that the focus confirms the countdown and does not set the world-end state (`localisation/english/014_cannibalism_l_english.yml:1317-1320`, `:1378-1379`).

## AI behavior gaps

All 204 focus blocks have one `ai_will_do` block and one AI base. All Unified and Warlord focuses have at least one modifier. The Unified pool uses terminal, resource-secure, resource-poor, Warlord-origin, network-response, and invalid-route factors; the Warlord pool uses origin, terminal, resource, and invalid-route factors. Wendigo has six route-aware modifier families (`ai_war_factor`, `ai_branch_factor`, `ai_countdown_factor`, `ai_low_authority_factor`, `ai_terminal_factor`, and `ai_low_network_factor`) across 26 of 28 focuses. The two base-only Wendigo focuses, `ZZZ_wendigo_bind_the_two_hungers` and `ZZZ_wendigo_mark_the_irreversible_road`, are fixed merge/countdown trunk steps rather than selectable route branches. Origin production strategy is self-removing and route-gated in `common/ai_strategy/014_cannibalism_warlords.txt:25-76`; Unified and Wendigo target behavior is owned by `common/scorers/country/014_cannibalism_target_scorers.txt:14-60` and the targeted-decision MTTH consumers.

Quantitative route dominance, starvation, and rank-reversal certification remains unresolved. The callable tool inventory does not expose `chaosx_ai_probability_auditor` or a collaboration/spawn route, so the mandatory custom-auditor pass could not be routed and no balance claim is made. Direct MCP evidence is retained only as bounded source evidence:

- `hoi4.probability_inspect` with `national_focus_ai_will_do` succeeded for `common/national_focus/014_cannibalism_focus.txt`, discovering 204 candidates, zero unresolved source inputs, and `poolComplete = false`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a394e82e545c8973ae8bb32cdc5e7c000acfafcecf3b3cc6c6ca732fe6097cb0/497e7fce60b1636a43dc359c1c86e216343c55f00eb48a66b6a2206e8680173d/probability-inspect-2413e679ae5f.json`.
- A direct empty-state evaluation over three representative focus IDs returned `PROBABILITY_ANALYZED_PARTIAL` with 11 unresolved rows because the supplied pool/state was intentionally incomplete. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c944043385b6540a54d46274ee0fb050242734a44ba443462482686b55f6519f/f1646520f37b0823732aa41cba64ed8ca2e97e6f72bdc74f29cf92842d1de1c9/probability-6f24deec462586b4280e642b.json`.
- A direct sweep attempt was rejected with `PROBABILITY_SWEEP_RANGE_REQUIRED` because the supplied scenario did not declare numeric alternatives for `state.has_war`. No sweep or before/after compare is presented as completed evidence.

## Terminal gates, identity, and control preservation

The ordinary terminal focuses explicitly require `global.chaos_meter_value > constant:cannibalism_evolution_threshold.world_end_chaos` at `common/national_focus/014_cannibalism_focus.txt:1482-1483` and `:1498-1499`. The canonical trigger repeats strict greater-than at `common/scripted_triggers/014_cannibalism_triggers.txt:3434-3455`; the constant is exactly `world_end_chaos = 1000` at `common/script_constants/014_cannibalism_constants.txt:947`. The ordinary helper repeats the same check before opening the terminal preparation or calling the existing world-end effect (`common/scripted_effects/014_cannibalism_effects.txt:16176-16198`).

Every Wendigo terminal focus calls `cannibalism_wendigo_can_start_countdown` through its `available` block (`common/national_focus/014_cannibalism_focus.txt:3539-3540`, `:3565-3566`, `:3588-3589`). That trigger requires the transformed country, winter network, completed countdown route, no broken or locked transformation, no existing/disabled world end, and strict Chaos greater-than-1000 at `common/scripted_triggers/014_cannibalism_triggers.txt:5364-5408`. The terminal lock trigger composes the same gate with scenario enablement, active countdown, terminal route completion, and progress maximum at `:5410-5419`.

The Wendigo focus root requires `original_tag = ZZZ`, and the focus helper source contains no `change_tag`, release, dynamic-country, annexation, or replacement-country operation. The existing ZZZ identity, control, units, templates, technology, ideas, and paid history therefore remain outside the focus reward surface. The terminal focus only sets the terminal route/open flags and refreshes live anchors (`common/scripted_effects/014_cannibalism_effects.txt:19578-19584`); the existing transformation pulse owns the final lock at `:19062-19072`.

## Layout and MCP evidence

Fresh `hoi4.focus_inspect` completed successfully for the consolidated source with workspace `mod_chaos_redux_ea3b2d67c2c0`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/452c5afa8a44fe0fbe1f3eb20125ee04d40915c3cb1accde077f154158bc7853/9ce4ce3489501dcb5ec05e05f987de5744d52050d919ccee9d937d7e1a742054/focus-inspect.7560f8cdc543cec6.json`.

The inspect metrics report 108/68/28 focuses, zero connector crossings, zero node intersections, zero long connectors, no dangling references, and passed blocking validation for all three trees. The current renderer produced deterministic artifacts for each tree:

- Unified: HTML `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0d7f8dedc1d0fdf3264341acf249f184bb5066426b427c0d0b227091d0efbfd7/113896fda101dfd4fe31ab69267581139e67dceefdac6588f14cb8c191b67777/cannibalism_unified_focus_tree.focus.html`, SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bd09b694bcd253a1ae6bfaadec4279fe13f017fc308fa07b10ee95bab4e615b4/8c805e5cd98828b51e0c5aea8f43035ec388b6e2d43db5a45064c5ce1e35b495/cannibalism_unified_focus_tree.focus.svg`, JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3a0ccebc9b8389d4002967bdb88c37b7c2f4470f8cf8d17ae88449c252a1d649/f32fd27b97898350476d364e59873ddd978fb5ad66967d25568f993a1b2d1a1d/cannibalism_unified_focus_tree.focus.json`.
- Warlord: HTML `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/309685252c4c928a5a7a82e3b5dea2e1ad54a8c594db21dab4a5c8d775e7ca07/1c22e71919decdbd4b8b4ca345721c84188dbec03bfdf7a54504f746c45d6828/cannibalism_warlord_focus_tree.focus.html`, SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5791167975f262b44ac05dacf7889e5132b14aa0f2ea9fadd1cd9da71db377fe/c68877fcf9f1abe150e463b0c073343712b42338d07d5fea3402f4e4fa58ceca/cannibalism_warlord_focus_tree.focus.svg`, JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3ae9f1b3109455c826dbac89c62538ef92f6d6d00e91545e60c187b06d780fd8/2294ecbfc3c139beb6be5c9dad1aa5893b72bba7ccfb341e9c0e217a1fe913d0/cannibalism_warlord_focus_tree.focus.json`.
- Wendigo: HTML `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9288b9bab68f6f2de2f996c6c392e7172c58ef85287c1af410c423be3f3704d5/29f28b3465188f4a6d2f1cf4f36d74c7a674762f5e0c651aa581c7c742d05787/cannibalism_wendigo_focus_tree.focus.html`, SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/232389eb0676368c65dd7d366ccaac11558a757021802f9dd4c4c0119274643d/3b50b95fb62f759ae8fb5f886c20baabc67966bf92f6df1d094b4741b4bd7671/cannibalism_wendigo_focus_tree.focus.svg`, JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e39ebd7cbae0b23f86f1d2106d04d6f209634b9e05334862ec6a9b391b505773/55a4267292f83f240c8f1bb31e927e91cd694ffa8a4890eefff514cf2ad4139d/cannibalism_wendigo_focus_tree.focus.json`.

The current inspect reports 18 non-blocking Unified presentation warnings, consisting of linear-detour warnings and one zigzag-chain warning. It still reports zero crossings, intersections, and long connectors. The 2026-08-05 layout handoff records that compact automatic rewrite introduced intersections/longer connectors and was rejected. Because no owned geometry defect was blocking or locally isolated in this pass, no `focus_rewrite` was run and no coordinates were changed by v4.

## Changed files and focus IDs

- Gameplay files changed by v4: none.
- Focus IDs changed by v4: none.
- Handoff created: `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_focus_final_audit_v4.md`.
- Concurrent changes preserved: four existing Wendigo `y` coordinate edits in `common/national_focus/014_cannibalism_focus.txt` and unrelated/current Event 014 localisation and irregular-unit text changes.

## Validation run and skipped validation

Meaningful validation completed: MCP focus inspect, three MCP focus renders, source block/count/reference checks, mutual-exclusion symmetry check, focus localisation key/BOM/duplicate check, icon mapping/file/dimension/hash check, terminal trigger/effect trace, no-Prison-Host runtime scan, and direct probability inspect/evaluate attempts.

Skipped or blocked: no `hoi4.focus_lint`/`hoi4_focus_lint` tool is registered in the callable MCP inventory, so focus inspect blocking validation is the available lint-equivalent evidence. No focus rewrite or post-change compare was run because v4 did not patch focus source; no focus compare tool is registered. The custom `chaosx_ai_probability_auditor` route and collaboration/spawn route are unavailable, so direct probability artifacts remain partial/unresolved and are not treated as auditor-equivalent balance proof. Hearts of Iron IV was not launched, so this handoff makes no in-game claim.

## Remaining route risks and simplifications

No simplification, fallback, placeholder, or route omission was introduced by v4. Remaining risks are limited to the unresolved quantitative AI certification, the non-blocking Unified detour warnings, unavailable focus-lint/compare routes, and parent-owned concurrent edits that were not modified here. No improvement-loop plan was written because no broad focus redesign or depth gap was found.
