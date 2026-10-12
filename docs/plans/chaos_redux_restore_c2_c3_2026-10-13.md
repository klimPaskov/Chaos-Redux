# C2 and C3 restore/fix evidence

The owner explicitly assigned C2 and C3 on 13 October 2026, authorized autonomous work without questions, and prohibited pushing, launching HOI4, replacing existing art, and writing outside the repo except the trailer ledger.
These are the current task notes; temporary source snapshots and checks live in `.tmp/restore_c2_c3/`.

## C2: slight crisis pressure for every scheduled event

History evidence: `20462d8898a2b6e264b3a9b6a4946c3f5c5c54bc` introduced the reusable pressure helpers, chance additions 6/12/18/25 and cooldown reductions 5/10/16/24, with the setting enabled by default.
`c180c6ed4db06f9126e6ce8bbe0e5cc429e76fdd` removed the earlier player toggle while retaining the default-On initialization.
`baaeb00fc5cba75b4d98b3694fc3c50db8f876fd` introduced the current setting tooltip restricting its description to communist spread, escalation and sabotage.
Its parent has no `chaosx_system_settings_l_english.yml`; there is no earlier generic tooltip to restore.
The changes here implement the owner's explicit C2 request rather than inventing purported historical wording.

The setting defaults Off in initialization and both reset paths.
The existing player-country flag and checkbox remain the control.
Every scheduled event uses the same country-owned timer; the pressure helper multiplies the next interval after ordinary Chaos scaling, before rounding and the existing minimum-day clamp.
The factors for tiers 0–5 are 0.98, 0.974, 0.968, 0.962, 0.956 and 0.95.
This gives 2–5% shorter intervals without changing event eligibility, target selection or event weights.
Manual event triggers remain immediate.
Existing communist crisis calls retain their structure and receive only 1/2/3/4 additional chance points and 1/1/2/2 fewer cooldown days.
AI countries and human countries with the setting Off receive zero pressure.

Changed sources: `common/script_constants/crisis_pressure_constants.txt`, `common/scripted_effects/chaosx_crisis_pressure_effects.txt`, the one timer call in `chaosx_logic_effects.txt`, the default lines in `chaosx_settings_effects.txt` and `chaosx_system_settings_effects.txt`, the checkbox comment in `chaosx_scripted_localisation_system_settings.txt`, and `localisation/english/chaosx_system_settings_l_english.yml`.
The public helper contract is recorded in `common/scripted_effects/chaosx_dynamic_effects.md`; the two existing settings documents describe the current default and consumers.
Only owned hunks are committed from the already modified shared files.

Source-calculated cases: an otherwise 100-day interval becomes 98, 97, 97, 96, 96 or 95 days across tiers 0–5 after rounding; a timer at the minimum stays at the minimum.
For a standard communist crisis with one controlled state out of three, 10% support, 80% stability and war support, peace, and a regular intervention target, the spread draw is 41.333% with pressure versus 39.333% Off and 51.333% under the earlier +12 bonus.
The corresponding spread cooldown is about 67 days versus 68 Off and 58 under the earlier 10-day reduction.
The standard escalation cooldown is 119 versus 120 Off, and sabotage cooldown about 137 versus 138 Off, before unrelated modifiers.
Cooldown floors can erase a reduction; they cannot amplify it.
These are conditional calculations from source, not observed engine results.

## C3: cosmetic cracks and removal of the cascade

History evidence: `3098ed9d2bc3d6b0eab5008c5bcd9e6d2b086422` introduced the Fracture Cascade report, Global Fracture news and SCN-018 launcher.
Its parent `2e44610483208a74831ea9242c2faaa9389cf6ca` has ordinary Event 021 and no cascade-specific event blocks or manual scenario.
The cascade-specific blocks are restored to that earlier absence selectively, preserving genuinely new ordinary civil-war mechanics and unrelated scenarios.
`480b47bff` introduced cosmetic UI wear and purple world-end styling; `e2dc84c0c` introduced the current very dim surface-damage art and direct tier visibility; `18d2ff192` adjusted the topbar positions.
The existing live-tier binding already follows the earlier/current state, so no invented restoration of it is needed.

The cosmetic setting remains independent of civil-war gameplay.
Calm World has no tier cracks; Gathering Storm starts slight wear; progressively larger visible networks and stronger red treatment appear through World Collapse.
The world-end flag selects stronger and wider red networks independently of the tier, including tier 0, with one additional divider decal and no purple glow.
The unsupported minimap `parent_window_name` attachment is corrected to the documented `parent_window_window` field.
All decoration stays click-through.

Eight new DDS files are derived from the four existing original crack sheets: `chaos_ui_wear_<shape>_red_tiers.dds` and `chaos_ui_wear_<shape>_red_world_end.dds`, where shape is `corner_tl`, `strip_h`, `strip_v` or `strip_short`.
They have new sprite names in `interface/chaos_ui_wear.gfx`; no original DDS or existing sprite texture path is changed.
New red tier sheets retain the original cumulative crack networks and frame canvases.
Strips are compressed with premultiplied alpha into narrow unused border bands, and corner art is masked to its border arms.
World-end alpha widens by one pixel within those same bands.
Original SHA-256 values: corner `f709b1cc36179c20c1d2724dd28d2f8fd341f00e4537ccd638efe270d1134f10`, horizontal `de9e09680b935f28e566b8cd1023db7a235d4f70cd3f5d69f34c438bb3c094aa`, vertical `d87d60b0a6772b5148a87749da92ecc637e98eeb535275b9fa2006f7f0356c05`, short `71cebd663303c816788678493af662b84de8df710a56db952eb653643c14863c`.

The accepted reference is `.tmp/restore_c2_c3/gui_reference/intended_topbar_world_end_1920.png`, a source composite of the installed vanilla topbar texture and the derived art, selected by the parent under the owner's border-only instruction before native edits.
Native mappings and positions are recorded in `docs/systems/chaos_ui_wear.md`.
The parent inspected the native contact sheets and reference image.
All eight new DDS files passed strict header and exact decoded-pixel roundtrip checks; original hashes are unchanged and alpha outside the reserved border masks is zero.
World-end variants have more visible pixels than their tier-5 counterparts.
The setting, all five tiers, Calm and world end are mutually exclusive by live flags; disabled wear hides every variant.

## Reference and check limits

The connected reference-context and reference-read routes initially returned installed `common/scripted_guis/_documentation.md` lines 1–80, revision `43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838`; offline Interface modding `iconType` lines 178–195, revision `b74afc86be4e5dbb3b0fc600820d73a8340f7dc1821fc5ef02c9ee1f028c0b1c`; and installed effects `add_to_temp_variable` lines 2327–2333, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
Source lookup for the vanilla paranoia precedent and the later wiki properties read returned no result and were stopped; pertinent installed/wiki files and actual vanilla topbar, panel and minimap consumers were read locally instead.
The historical UI-wear renderer already exhausted two attempts with `JOB_WORKER_EXIT`; it was not retried.
The current narrow GUI inspection and file-scoped pressure script validation returned no result and were stopped; those checks are unavailable, not passed.
The pressure auditor's probability route was unavailable after the allowed narrow retry; balance evidence is calculated from source.
No MCP render, live-game test or engine execution is claimed.

Skills used: chaos-redux-scripted-gui, chaos-redux-event-assets, chaos-redux-ai-strategies, chaos-redux-subagents, chaos-redux-shared-git-commit, chaos-redux-events, chaos-redux-decisions-missions and chaos-redux-xlsx. No skill was created or changed.
No design simplifications are authorized or used; unavailable preview tools limit visual verification only.
Final commits and completion dispositions are appended to C2 and C3 in the owner's plan after review.

## Final removal and preservation evidence

The removed cascade surfaces are report `.6`, news `.212`, manual callbacks `.15`/`.19`, Critical new-war callback `.18`, SCN-018 registry/type/launch UI, broad random-country registration, Critical new-war dispatch, and the stale public Evolution III log entry.
Six unused Global Fracture localisation keys and the stale `Events!F22` description are absent.
Ordinary Event 021 lifecycle callbacks and stage/capacity state remain because registered civil wars use them for settlement and reconstruction; none is connected to the cosmetic setting.
The isolated before/after comparison preserves all 24 surviving event definitions and 144 helper bodies byte-for-byte outside the deliberately changed scheduler and announcement wrapper.
The authoritative workbook changes only its Events worksheet, Scenarios worksheet and scenario table; the other 22 ZIP payloads are exact.
All 15 other scenarios and Evolutions I/II are preserved, all three exports match the workbook, and the Clusters export is unchanged.
Workbook final SHA-256: `f3d1e0d4143890e26b3f0d3f77ea0f305ead83946a5778b53b978a518d1ed2c8`.

The parent caught faint post-compression tier-5 strips during native-size review and corrected their alpha gains before publication.
The final tier-1 through tier-5 alpha-threshold footprint increases strictly for every shape; tiers 4/5 widen within the reserved masks, and world end widens further and exceeds tier-5 visibility.
The final source/asset check resolves all 121 decorative icons to registered DDS frames and live visibility predicates, with zero painted alpha outside the reserved masks.
Right-anchored date decoration remains within the tested source bounds at 1920x1080, 1366x768 and 2560x1440, scale 1.
No existing sprite is repointed and no original crack texture is changed.

Commits: C2 `d9ad38c307309ca4422eb99d2456c9e4f318e2c3`; C3 cosmetic package `4b054623c79d08f07e953c03ffe45de089903c87`; C3 cascade removal `1938e23f0c5ebab07ef45228520d1b2f5b9d97ad`.
The owner plan records those hashes only on C2 and C3.
The final note commit also shortens the edited Reset All tooltip's weight to `1k`.

Nothing required was omitted or replaced by a weaker mechanic.
There is no earlier generic crisis-pressure tooltip to recover from history, so that wording and the slight timer factors implement the explicit current instruction.
No push or HOI4 launch occurred.

Additional direct local references:

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md`, lines 216-248, SHA-256 `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/script_constants/documentation.md`, lines 1-35, SHA-256 `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c`.
- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, lines 211-242, SHA-256 `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
- `paradox_wiki/Scripted GUI modding - Hearts of Iron 4 Wiki.md`, lines 391-441, SHA-256 `b07d850ea78c4e1e3fc113574059ad2f3ea37df320b9259128d66814023c1f30`.
