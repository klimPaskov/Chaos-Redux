# Event 001 GUI Release Repair Handoff

Status: the accepted dashboard source repair is applied, but this handoff remains visually blocked because post-change `hoi4.gui_inspect` and `hoi4.gui_render` calls closed their transport before producing evidence.

## Ownership and acceptance

The repaired surface belongs to Event 001, `001_communism_spread`, and is limited to the existing Communist Insurgency dashboard and state-map level marker.

`common/decisions/categories/001_communism_spread_categories.txt` attaches `communism_spread_dashboard_scripted_gui` to `chaosx_communism_fight_category`; `common/scripted_guis/001_communism_spread_scripted_guis.txt` binds its `decision_category` context to `communism_spread_dashboard_container` and binds the state marker GUI's `state_mapicon` context to `communism_control_state_mapicon_container`.

The mapicon GUI is shown only for a state with `communist_controlled_state`, an active `communism_spread` global flag, a non-communist host with `communism_spread_idea`, and a host that is not classified as a special Chaos country.

The parent accepted the narrow G5/G6 repair: retain the authoritative threat score and qualitative stage, show the three current level counts, replace the aggregate total and daily-drift row with a short map-selection prompt, and center the level groups inside the existing 470 by 174 dashboard.

This decision is specific to this implementation repair; it does not resolve broader pending Event 001 spec or release acceptance.

## Files and identifiers

The owned GUI layout is `interface/chaosx_decisions.gui`, with containers `communism_spread_dashboard_container` and `communism_control_state_mapicon_container`.

The source binding is `common/scripted_guis/001_communism_spread_scripted_guis.txt`, identifiers `communism_spread_dashboard_scripted_gui` and `communism_control_state_mapicon_scripted_gui`; it was inspected and left unchanged.

The dashboard uses `GFX_revolutionary_threat_meter_000` through `GFX_revolutionary_threat_meter_100` and the existing `GFX_communism_control_level_1_texticon`, `GFX_communism_control_level_2_texticon`, and `GFX_communism_control_level_3_texticon` sprites.

The mapicon reuses the same three tier sprites and remains informational; its tooltip directs players to the Communist Insurgency decisions.

The only localization key changed is `communism_dashboard_counts` in `localisation/english/chaosx_decisions_l_english.yml`; `communism_dashboard_status` remains unchanged and displays `[?communism_revolutionary_threat|.0]` with `[GetCommunismThreatStatus]`.

The decision entry point is the `chaosx_communism_fight_category` decision category; no decision, effect, cost, AI, gameplay, or localization behavior beyond the one prompt key was changed.

## Before-edit references and findings

The intended correction reference was created before source edits at `gui_release_20261005_evidence/dashboard_reference.png` (SHA-256 `e46db8c66c4f9350ca57b2159ab0e083373325e77ba5a2f64271f67cb3cc0a86`) and `dashboard_reference.svg` (SHA-256 `1b6c9484f265c9ac0661abc4a18fb62b4f3d63a24a06792b98c778f209e5411e`); it maps the pre-edit production render to the desired response row and centered tier group without redesigning the meter or status row.

The source-grounded map-marker reference was also created before any mapicon edit at `gui_release_20261005_evidence/mapicon_reference.png` (SHA-256 `1fa9cef7bba3cb3897b4b738109bf64522427c8c18caefdbd4b7da46a3528c76`) and `mapicon_reference_overlay.svg` (SHA-256 `92a51da7eeacf21a4c5fa742f8f43c4e6b7b73a1cc9e1ffe88f924cfb37f393f`); California state 378 is an installed-game USA-owned state, and the 37 by 39 painted level-1 mark fits within the 42 by 42 logical container.

The source-derived dashboard baseline fixture is `evt001_gui_dashboard_regular_host_baseline`, USA, 1936.1.10, normal, 1920 by 1080 at UI scale 1, with generated scenarios disabled, threat 34, one state at each control level, and source-aligned getter outputs `Growing Unrest` and `GFX_revolutionary_threat_meter_030`.

The pre-edit production artifacts are `gui_release_20261005_evidence/resolved_pre_dashboard_full.png` (SHA-256 `445d9d623bb7fedc3006b61a75580a1668c0b5e96e22adb12deededdf5bbe847`), `resolved_pre_dashboard_cropped.png` (SHA-256 `46cc29f35c8b67fc90dc26dff0a21340de8880e65cc5dbb05ebae2ab994b81d0`), and `resolved_pre_dashboard_annotated.png` (SHA-256 `0c7c340f12f1fe5139c6a004be82b9fbc8c8d04468180485f01f923572e37925`).

That dashboard render used source revision `7bf6c91a1ee932192af6a64b620afa9a28752d048bea9c7d7da95cc30141dfa9` and showed the 30-percent meter frame with the current status and all three counts; the original row showed both total controlled states and daily drift.

The pre-edit dashboard inspection artifact was `gui-inspect.207406a02041ac51.json`, SHA-256 `554097b6283054fa580883c1157c2eb8ac8f05df0191bc4a4fe22a3043ff65f5`, source revision `207406a02041ac51bbae6b025e10b5c99f80a7bd0a33f59baecc42afbe8fe0ac`; it reported 4-to-10-pixel spacing gaps and an unresolved getter before the source-backed `values` fixture was used.

The resolved pre-edit dashboard layout artifact `communism_spread_dashboard_container-layout.json` had SHA-256 `7d40c76a08d9b3bb9ee4e697a5e95513d1587985b76cda15d7b9b94902ef8a37`; it measured the count row at x=8, y=104 and the level logical group from x=32 through x=342, with the group center left of the 470-pixel container center.

The pre-edit mapicon render used California state 378, explicit owner/controller USA, and level-1 state-flag facts; its full SVG artifact `pre_mapicon_full.svg` has SHA-256 `e2ff9acf9122999ea3f98e43b87446f9454f5ccfe1a4f84e545bb6ced2eac83a`, and the rasterized preview `pre_mapicon_full.png` has SHA-256 `454e38afb9acba8a97bb3c41f2080d1ab9275c5c046d8136d003449e5c3ea311`.

The exact single-level mapicon inspection artifact `gui-inspect.b6699488e3b1a63e.json` has SHA-256 `aa1617385f19eb75df35d996b26dc2d5850a242edee7d1ae8c2fe907754414f6`; it resolved the three level triggers and found no visible overlap, but its whole-window visibility predicate remained unresolved because the generic custom `is_special_chaos_country` classifier is not modeled by the fixture evaluator.

The pre-edit mapicon production render itself still reported three unresolved visibility findings and a truncated response, so only the full SVG was retained and reviewed; no other hidden or unsupported states are claimed as covered.

## Implemented correction

The dashboard response row moved from x=8, y=104 to x=8, y=102 to leave a consistent 8-pixel gap after the status row.

The level 1, 2, and 3 icon positions are now x=80, 186, and 292 at y=132; their count text boxes are now x=114, 220, and 326 at y=142.

The three-pair logical group is 310 pixels wide and centered in the 470-pixel container, with 80-pixel side margins; each count remains directly beside its corresponding tier icon.

The row now reads `Select a marked state to intervene.` and retains the existing `communism_controlled_states_tt`, where the daily communist support detail remains available.

The intended hierarchy is the existing threat meter, the authoritative status and threat score, a concise map-selection prompt, then the three color-coded level counts.

The accepted visible-value budget is four mechanic values: one threat score/meter and one count for each of the three control levels; the qualitative threat stage is a label, not an additional numeric value.

The panel has no clickable button or cost controls; selecting a marked state is the response affordance and the existing decision category supplies intervention choices.

The meter, status, aggregate-row tooltip, tier sprites, tier count tooltips, and mapicon tooltip identifiers are unchanged; MCP's current renderer omits `pdx_tooltip` content, so the localized tooltip prose was source-reviewed but its in-render presentation was not verified.

The dashboard's state coverage before the service failure was normal only; hover, selected, disabled, warning, completed, empty, and crowded states are not applicable to these non-actionable text and icon children, while tooltip display remains an MCP renderer limitation.

The pre-edit fixture covered one count in each tier, not zero-count or maximum-count layouts; the requested zero/some/maximum count matrix is unresolved pending a working post-edit render route.

The mapicon fixture covered a source-backed level-1 mark with explicit mutually exclusive L1/L2/L3 flag facts; level-2 and level-3 marker visuals were not rendered and remain unresolved.

Early and late threat status labels are source-defined by `GetCommunismThreatStatus` and the Event 001 scripted triggers, but no post-edit MCP samples for these statuses could be produced; the source thresholds are Growing Unrest above 19 and below 40, Dangerous above 39 and below 65, Revolutionary Crisis above 64 and below 85, Collapse Imminent above 84, and Rebel War Imminent above 99.

## Source transformation evidence

`gui_release_20261005_evidence/source_before.json` preserves the exact pre-edit dashboard and mapicon containers, the source file hashes, and the original two dashboard localization lines; its SHA-256 is `e702b2a4b62812daeefbdc6883c01ac191f16d63546a314ba62e444e780d1a65`.

`gui_release_20261005_evidence/source_after.json` preserves exact old and new dashboard blocks, the transformation list, unchanged mapicon proof, and post-edit hashes; its SHA-256 is `69d84776fac09cadae2eb16054a3c1e987b8be484309007d32ac637532f3f8e5`.

The dashboard container block hash changed from `b1ab9c5e4914a12f2f23280ea1878e7210df3290c16310fd3497d4f1a40d92e4` to `0cb75ac7e1198bb1bf3d67592cdfb851da5d8af80d9f3e75fb31d1402cc0cc1d`; the mapicon container hash is unchanged.

The full GUI file hash changed from `92c3c5855c0c8f8abaea31c81557f6a81f57f6c6440f4ac5329b1b97a538d828` to `0947cba3d6dd9213472dbbb1ec9ccf0dd41710e13c85efeb3c5bddf4be821c57`; the file also contains separate contemporaneous edits in the Holy Realm UI from another worker, which were preserved and are outside this repair.

The localization file hash changed from `7616669c05cc2a989c6c222cba95aca7c5bfed1eea92de468592b4a9f681d92b` to `7f8845b2d78ced9cd0a46582dee9aa2ac93ca430c7b504a7a3e46fce9dac1c1c`; other concurrent localization edits remain outside this repair and were preserved.

## Post-edit MCP gap

After the source edit, `hoi4.gui_inspect` was called on `communism_spread_dashboard_container` using the matched `evt001_gui_dashboard_regular_host_baseline` fixture, USA on 1936.1.10, the same 34-percent threat and tier counts, and generated scenarios disabled; it ran for about nine minutes and returned `tool call error: tool call failed for hoi4_agent_tools/hoi4.gui_inspect — Caused by: Transport closed`.

A bounded retry of that same post-edit selector with the parent-confirmed country record and root fact shape returned the same `Transport closed` error immediately; the earlier same-fixture retry also returned `Transport closed`.

The matched post-edit `hoi4.gui_render` call for `communism_spread_dashboard_container`, at 1920 by 1080 and UI scale 1 with the same scenario, also returned `tool call error: tool call failed for hoi4_agent_tools/hoi4.gui_render — Caused by: Transport closed` immediately.

The exact selectors and failures are also retained in `gui_release_20261005_evidence/mcp_failures.json`; they are recorded rather than treating source inspection, prior screenshots, or an inferred geometry calculation as post-change production evidence, so post-edit comparison, hierarchy, click-region, state, and resolution evidence remain blocked.

No post-edit mapicon inspect or render was run after the shared GUI MCP transport closed; its source block was unchanged, and no visual completion claim is made for it.

## References and limits

The offline scripted-GUI wiki section `Scripted GUI modding`, revision `b07d850ea78c4e1e3fc113574059ad2f3ea37df320b9259128d66814023c1f30`, lines 144–164 documents `decision_category`, `state_mapicon`, and `PREV` scope use; the offline Interface modding section, revision `b74afc86be4e5dbb3b0fc600820d73a8340f7dc1821fc5ef02c9ee1f028c0b1c`, lines 81–109 documents native container sizing and clipping.

Installed scripted-GUI documentation `common/scripted_guis/_documentation.md`, revision `43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838`, lines 1–80 documents `state_mapicon` context; vanilla precedent inspected was `interface/sov_paranoia_system_scripted_gui.gui` with `common/scripted_guis/SOV_paranoia_system_scripted_gui.txt`.

No custom background, frame, icon, button, or DDS asset was added or required; the existing meter art and AAT-derived texticon sprites remain the installed assets.

No gameplay effects, costs, AI behavior, values, route structure, or mechanics were changed; no simplification beyond the parent-accepted removal of the total and drift figures from the overview row was made.

The user still owns live in-game validation; no game was launched, and this handoff does not claim in-game completion.

The broader Event 001 integration, gameplay, balance, category actions, event-log/details wiring, localization audit outside the two granted keys, and final commit remain with the parent.
