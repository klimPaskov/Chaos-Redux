# Event 014 country-package final bounded audit

Date: 2026-08-25.

Scope: CBA-CBH, CBL, the existing ZZZ Wendigo crossover, Event 014 country/history/unit/character/idea/activation surfaces, and the country-linked focus, event, technology, and dynamic-state dependencies.

Outcome: no isolated gameplay defect was safe to patch in this pass. The only gameplay files currently dirty before this handoff are `common/scripted_effects/014_cannibalism_effects.txt` and `common/scripted_triggers/014_cannibalism_triggers.txt`, which contain concurrent package work; they were inspected and left untouched. No gameplay commit was created.

## Coverage checklist

- Tags: `common/country_tags/014_cannibalism_countries.txt:8-16` registers exactly the eight reusable warlord slots `CBA` through `CBH` and the separate ordinary host `CBL`.
- Histories and country definitions: all eight `CB*` warlord histories and `CBL - Cannibal Unified Host.txt` are dormant neutral shells; runtime setup supplies territory, leader, ideas, technologies, templates, forces, and focus trees.
- Warlord origins: `common/scripted_effects/014_cannibalism_effects.txt:4510-5382` limits origin selection to Island Host, Siege Commune, and March Host, derives a capital candidate, transfers at most two valid connected controlled neighbours, and applies origin-specific ideas and specialist units. No live `prison_host` or `Prison Host` identifier remains in the inspected package sources.
- Reuse and cleanup: slot allocation and release are guarded by `common/scripted_triggers/014_cannibalism_triggers.txt:3599-3609` and `common/scripted_effects/014_cannibalism_effects.txt:5396-5479`; cleanup clears incarnation state and all nine activation technologies at `common/scripted_effects/014_cannibalism_effects.txt:5608-5620`.
- Leaders and identity: generated warlords are created by `common/scripted_effects/014_cannibalism_effects.txt:4727-4758` with dynamic region/name/portrait localisation; CBL uses `CBL_hannibal`, while Wendigo uses `ZZZ_hannibal_wendigo` from `common/characters/014_cannibalism_characters.txt:10-24`. The source pass found no opposite-gender generated pairing or Wendigo trait leakage into ordinary warlords.
- Politics, ideas, AI, and recruitment: the dormant histories, origin ideas, existing Event 014 decisions, AI strategy file, and population/Larder-gated recruitment paths are wired to runtime setup. No Event 014 advisor, high-command, theorist, or political-advisor surface exists; adding one would be a broad identity-design change and was not invented here.
- Focus loading: warlords load `cannibalism_warlord_focus_tree` at `common/scripted_effects/014_cannibalism_effects.txt:5230`, CBL loads `cannibalism_unified_focus_tree` in the reveal path, and the Wendigo overlay loads `cannibalism_wendigo_focus_tree` at `common/scripted_effects/014_cannibalism_effects.txt:19159-19171`.
- Units and technologies: nine inactive custom line subunits, nine matching hidden activation technologies, locked templates, route grants, and reset calls are present. Bone Riders is a custom cavalry subunit, while Scavenged Elephant Column uses separate vanilla `elephantry` access.
- Player control and Wendigo preservation: player-safe host selection and transfer guards are present in the CBL creation path; `cannibalism_prepare_wendigo_merge_identity` preserves the original ZZZ country in place, applies `ZZZ_CANNIBALISM_HANNIBAL`, prepares the pack contract before the overlay, recreates the Wendigo leader, and preserves the existing territory/equipment/units/ideas state through the guarded merge path at `common/scripted_effects/014_cannibalism_effects.txt:18661-18715` and `19224-19243`.
- Wendigo anchor state: pre-lock command gating, anchor designation, countdown, anchor break/stabilisation, and locked-state checks are present in `common/scripted_triggers/014_cannibalism_triggers.txt:4988-5180` and the matching decision/effect sections. The source supports the required attackable pre-lock/countdown form and post-lock terminal form.

## Nine activation consumers

`common/technologies/014_cannibalism_irregular_activation_technologies.txt:12-82` declares one `allow = { always = no }`, `ai_will_do = { factor = 0 }` hidden technology per subunit, and each technology enables only its matching unit.

`common/scripted_effects/014_cannibalism_activation_effects.txt:10-115` resets all nine levels and exposes the package, origin, unified, inherited, and Wendigo grant helpers. Warlord setup calls the package grant at `common/scripted_effects/014_cannibalism_effects.txt:5180-5218`; focus and decision contracts call the Feast Cohort, Bone Guard/Bone Riders, origin specialist, and Network Cadre helpers at `common/scripted_effects/014_cannibalism_effects.txt:17401-17567` and `17716-17750`; unified and Wendigo transitions call the inherited, legion, origin-specialist, and bone-guard helpers at `common/scripted_effects/014_cannibalism_effects.txt:12172-12183`, `15910-15943`, and `18616`.

The nine unit definitions are at `common/units/014_cannibalism_irregular_infantry.txt:309`, `359`, `408`, `458`, `507`, `562`, `618`, `668`, and `728`. All share `category_cannibal_irregular_infantry`; Bone Riders has `cavalry = yes`, `type = { infantry }`, and `group = mobile` at lines 507-525. The separate locked `Scavenged Elephant Column` template uses vanilla `elephantry` at the concurrent template section around `common/scripted_effects/014_cannibalism_effects.txt:4846-4854` and receives base access from warlord/CBL/Wendigo setup.

## Engine evidence

The HOI4 MCP workspace was `mod_chaos_redux_ea3b2d67c2c0`.

Technology inspection and rendering completed for all nine IDs at revision `4803a687203ff008314fdbad6b6420b47efaa67b6e066e46f4f3a41831bf052c` and graph hash `088e79afc1261a70da527db50bceb2b44b48ef8f7b00b70632a1d807d41943a7`. Each route returned `TECH_INSPECTED_PARTIAL` and `TECH_RENDERED_PARTIAL`, with the expected `MCP_INLINE_FILES_TRUNCATED` diagnostic and deferred helper projections. Useful inspect artifacts are:

- `cannibalism_scavenger_warband_tech`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d645c16f1657ffbfda89337727eb1ac7379554dbac6595f42acac51364ae8eb3/72d22c1452a564a53a1709464f8848536bbf44f23e0e6a6d565ad1a31907bfe5/technology-unlocks-4803a687203f.json`
- `cannibalism_feast_guard_tech`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f55958e8658f4fb99f07ee09a74c694e49120a729c947ef6a03637f43ac389ab/b1d048a295dd0759083b4f6111a25738d85f91ea208541b34b2e1230d747d36f/technology-unlocks-4803a687203f.json`
- `cannibalism_feast_cohort_tech`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/19024ae22332483482e01b31006bf744e7b7bb6c4cda426b5962309c5a9affdc/66cf6823029c6466ffbc85cb83f02d1a0af066020a9292e8a39cbd86e22221ee/technology-unlocks-4803a687203f.json`
- `cannibalism_bone_guard_tech`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2a5d1399842161d4fdfec8960c44d8e34307b6e2d17a3026f54379f01f315547/fdbcaf4bc7ed4388471382d828eaa0cf14311926dd07c7e4f4467f97ec3b75a6/technology-unlocks-4803a687203f.json`
- `cannibalism_bone_riders_tech`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1a56fc9c911c5f55c5398fb524ce5e7cfe1cf969b455c9a2f7a1eb68a6c39708/9f5fbdfe7513f2912c5c6166449fb4503df5373f0eeb9192bf7240cfbb8a7153/technology-unlocks-4803a687203f.json`
- `cannibalism_island_reavers_tech`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d7dffb206114daab1e7f22b98e2b0df1e6915316b56ea90b4fb925393d0b0d5f/70383bd62efbd5af6e8a37858922bb56d24ba7b872bee4672664d65321ca8d6d/technology-unlocks-4803a687203f.json`
- `cannibalism_siege_eaters_tech`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f06b81f8a5c14094f6ed1597aefc59112cf52e81cfce8287fc0dac5a31b61f12/6e1f46c38dd031a49e1d9d8fdf230428cae0430c09ea7727322096c9884a04ad/technology-unlocks-4803a687203f.json`
- `cannibalism_march_predation_column_tech`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/92d20a8b3edf8dbd14a3fc652c4af867610b1b121d3b88e9d8cda8af31791292/dc64157c9946eade728709b2578e3ab77c0bf63a148d86805012e089641008f7/technology-unlocks-4803a687203f.json`
- `cannibalism_network_cadre_tech`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/419448a716fddcb42767d5e2a7e6e83f0795d16a552a2db57121ef49b8da04db/d4e67ab69c413f9275dea32a0ac77e6c6e4b2aef62b8a6db51165b63c04b5928/technology-unlocks-4803a687203f.json`

Focus inspection/rendering completed for `cannibalism_unified_focus_tree`, `cannibalism_warlord_focus_tree`, and `cannibalism_wendigo_focus_tree` from `common/national_focus/014_cannibalism_focus.txt`. All three returned `FOCUS_INSPECTED` and `FOCUS_RENDERED` with validation passed. The only diagnostic was the shared missing localisation reference `continuous_restrict_freedom_desc`; localisation was outside this bounded ownership.

Useful focus render artifacts: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5ce6d574f816c17b124b2d83d7272c7a51687166639c86e13bae887f71038724/b3c0d6cbc959c7080221683b2a8a6c0ef10e7f38753cb30befad52e7e3adfc4d/cannibalism_unified_focus_tree.focus.html`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2dde8ec8fff3200e335b7ed32f35337522f0596cf2e83db8e8bc5c8445514654/251c4d145e12881deb0dfbe877c2a0853c084c9c9d61906c415eee463f799029/cannibalism_warlord_focus_tree.focus.html`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c6688349369a7653ad8477bd50eb2148dcf408ac4ebe50da9b712227660477a1/5528fce60eb2cbaa51eafd49a2c5498699aecdc6ad1e46a296c18ddeab33bcd3/cannibalism_wendigo_focus_tree.focus.html`.

Event inspection/rendering covered `chaosx.nr14.70` and `chaosx.nr14.72`. Trace/state-flow and state renders were emitted as `EVENT_INSPECTED_PARTIAL` and `EVENT_RENDERED_PARTIAL`; the direct evidence is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5ea9c4105b702717335df2d338b9bd4cc2bca74b32b8573dcd16dee9aca9060a/cd1cf28d0b3a53ff0c5d557a44c0a9b6ddadaa56a2bfa0ceb3b053304d1ff20b/event-trace-59143acd4a23.json` for `.70` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fd71bb880c738737b31566c2aac4a0c1784c41a3e65d8b49927f1a93e183dbfb/28f01cba3c91a584b71f331a1f4818b886b0539e11511ac1f2346a58982ee95b/event-state_flow-59143acd4a23.json` for `.72`.

The required read-only map pass completed with `MAP_INSPECTED` and `MAP_RENDERED` on revision `bc32e10cc517987efadbf7615bf577766492b0fdf689dd1d5395cad9cf0e6fc9`. Useful artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/98c2485664c2ec8da54530afa9b8f74355369b3108f650dd1330628ef1eb6054/0114bcc404eea31ee494d7940da27e3bdf5be457070b92718ea577a41bd2871d/map-inspect.bc32e10cc517987e.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/003a562675caf0b276cccec361be139b350a7a4630927297ab56c16da7e3792e/3811d42606bff5f2482635a2e3a7e973e4ed0741089d092d677965fa70c40ef0/map-state.json`. No map rewrite was attempted.

## Findings, risks, and blockers

- No country-package P1 defect was proven in the bounded source pass, so no narrow gameplay patch was applied.
- The generated Oceania name pool remains Anglo-settler leaning in `localisation/english/014_cannibalism_l_english.yml:477-504`; this is a broad identity/design concern and not a safe country-file patch.
- The focus route reports the shared `continuous_restrict_freedom_desc` localisation warning. Localisation is outside this ownership and no localisation edit was made.
- The map report exposes global pre-existing diagnostics for invalid building positions and floating-harbor sea adjacency in states 12, 77, 85, 116, 118, 126, 145, 163, and 178. These are not dynamic Event 014 state IDs and no map write was attempted.
- The installed tool inventory has no callable `chaosx_ai_probability_auditor`. Because the named probability-auditor route is mandatory, no generic probability tool or source-only AI review was substituted for the required scenario baseline/compare pass. AI quantitative confidence is therefore blocked; source references remain `common/ai_strategy/014_cannibalism_warlords.txt` and the AI-bearing scripted decision/focus helpers.
- The installed package exposes no dedicated Technology Tree Viewer. The available `hoi4.tech_inspect` and `hoi4.tech_render` routes produced partial direct evidence, but helper projections were deferred and validation reported false. Full Technology Tree Viewer validation remains unresolved.
- Event MCP inspection covered the full workspace and returned partial reports with 8,301 unresolved nodes, 24,105 diagnostics, and 14 blocking diagnostics across the overall event corpus. No skipped source was reported, but those global diagnostics cannot be attributed to Event 014 without a narrower working viewer route.

## Files changed by this handoff

- Added `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_country_final_bounded_audit_2026-08-25.md` only.
- No country, history, unit, technology, scripted effect, scripted trigger, character, idea, AI, focus, event, map, GUI, asset, audio, or localisation file was changed by this subagent.
- No commit was created because the bounded pass found no isolated patch and two owned gameplay files were concurrently dirty before this handoff.
