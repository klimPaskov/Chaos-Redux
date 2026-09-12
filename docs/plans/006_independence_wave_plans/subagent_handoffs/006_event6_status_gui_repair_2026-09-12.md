# Event 006 Statehood Ledger: bounded repair evidence

Disposition: **blocked**.
Date: 2026-09-12.
Event: `006_independence_wave`.
The inspection and baseline render succeeded, but the requested visual repair is incomplete.
No runtime source, localisation, gameplay, asset, or shared interface was changed.
The parent explicitly instructed the worker to leave source untouched and finalize this evidence handoff after review identified unresolved fixture coverage and a content-priority decision outside a layout-only repair.

## Ownership and accepted scope

The event-owned window is `independence_wave_status_window` in `interface/006_independence_wave.gui`.
Its controller is `independence_wave_status_scripted_gui` in `common/scripted_guis/006_independence_wave_scripted_gui.txt`, with `context_type = decision_category`.
The founding category `independence_wave_founding_category` attaches that controller through `scripted_gui = independence_wave_status_scripted_gui` in `common/decisions/categories/006_independence_wave_categories.txt`.
Its visibility depends on `is_independence_wave_event6_local_content_active`.
This establishes a dedicated Event 006 mechanic surface, not ownership of the shared event log, event details, settings, or super-event interfaces.

The parent accepted preservation of the existing 700 × 500 composition for a bounded repair, with no new art, gameplay change, fallback, or redesign.
The accepted review targets are 1920 × 1080 and 1366 × 768 at explicit UI scale, with the Government, Recognition, Security, League, and Ambitions tabs and their supported states.
Older 1280 × 720 documentation is historical, not a substitute for the current target resolutions.
The parent withheld permission to change the concurrently modified scripted-GUI file; its working-tree modification was reported by the parent as EOL-only with no semantic diff.
It remained untouched.

Acceptance references inspected:

- `docs/specs/006_independence_wave_specs/matrices/006_asset_family_registry.csv`: ASSET-039 identifies the main mechanic panel; ASSET-040 through ASSET-043 identify recognition, dependency, league, and formable animation families.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_current_completion_audit_after_mac_commit_2026_08_06.md`: Statehood Ledger completion-proof gap.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_decision_mission_current_audit_2026-08-22.md`: founding-category attachment and decision/UI integration evidence limits.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_visual_asset_audit_2026-09-03.md`: existing panel and icon families, static/animated siblings, and the distinction between asset checks and dynamic-window proof.

These documents support the assigned review but their existence alone does not constitute redesign approval.
The current scripted-GUI skill makes `gui_rewrite` optional; historical claims that rewriting itself is a mandatory gate are not applied here.

## Guidance and precedents consulted

Read `AGENTS.md` and the scripted-GUI skill's integrated [Scripted GUI visual and usability review](../../../../.agents/skills/chaos-redux-scripted-gui/SKILL.md#scripted-gui-visual-and-usability-review), plus the decisions/missions, events, event-assets, and frame-animation skills.
Consulted the required core offline wiki pages and read the relevant Interface modding and Scripted GUI modding snapshot guidance.
Vanilla references consulted were `common/scripted_guis/_documentation.md`, the localisation concepts in `documentation/script_concept_documentation.md`, and the exact attached-display precedent `interface/sov_paranoia_system_scripted_gui.gui` with `common/scripted_guis/SOV_paranoia_system_scripted_gui.txt`.
The precedent separates panel art, text, meter values, and tooltip/control elements; the existing Event 006 composition retains native elements rather than flattened interactive artwork.
No skills were created or changed.

## Source snapshot and identifiers

MCP workspace: `mod_chaos_redux_ea3b2d67c2c0`.
Inspect/render source revision: `002afb7d0452a97585e8ba4ea265a1a714f6c0905ed9f5f2b80c91fe1362076b`.

| Source | SHA-256 |
| --- | --- |
| `interface/006_independence_wave.gui` | `f0f012733724b03dc535f4975025af60027caf1c23591dcaf125bbed44469c94` |
| `interface/006_independence_wave.gfx` | `ed545b4bbf5dcdc08524956d72595b1f74f6322fc0b693cb68f9727e6e4b2119` |
| `common/scripted_guis/006_independence_wave_scripted_gui.txt` | `ba8f9e9dccfa5b9dbed9b369d9bcc0c427afbd1646e63bc4d6582f6ceab4709c` |
| `localisation/english/006_independence_wave_gui_l_english.yml` (inspection dependency) | `d00f2e09dbe92d6a108ab7d93d3603b4c7bd5ea23c9cb4c2c7db0dd9af8a46e3` |

The selected-window inspection resolved 48 elements, 16 sprites, two fonts, 39 localisation keys, and one scripted GUI.
The fonts are `hoi_24header` and `hoi_16mbs`.
Relevant native identifiers include `independence_wave_status_panel_background`, `independence_wave_status_legitimacy`, `independence_wave_status_recognition`, `independence_wave_status_capacity`, `independence_wave_status_security`, `independence_wave_status_instability`, and `independence_wave_status_instability_warning`.
The background uses `GFX_independence_wave_status_panel`; the controls reuse `GFX_chaosx_button_123x34_vanilla`.
The founding row icons use `GFX_idea_independence_wave_founding_identity`, `GFX_idea_independence_wave_unrecognized_state`, `GFX_idea_independence_wave_improvised_government`, `GFX_idea_independence_wave_fragmented_command`, and `GFX_idea_independence_wave_post_release_instability`.
The four dynamic frame properties read `ROOT.independence_wave_gui_recognition_frame`, `ROOT.independence_wave_gui_dependency_frame`, `ROOT.independence_wave_gui_league_frame`, and `ROOT.independence_wave_gui_formable_frame`.
The inspection artifact below retains the complete exact element, sprite, localisation, animation, and source-link inventory without duplicating it into a potentially stale secondary registry.

## Baseline route and fixture

The exact selector was `windowName: independence_wave_status_window` for `hoi4.gui_inspect` and `hoi4.gui_render`.
The successful explicit scenario was:

```json
{"id":"event006_status_repair_baseline","resolution":{"width":1920,"height":1080},"uiScale":1}
```

Both calls used `generatedScenarios: {"enabled":false}`; rendering requested `states:["normal"]`.
The normalized scenario has empty `flags`, `values`, `variables`, `visibility`, `scriptedGui`, `localisation`, `elementStates`, and `selectedFrames` maps, English localisation, normal state, and animation time zero.
It is therefore an empty baseline fixture, not a coherent Government or other gameplay-state fixture.

An initial schema attempt incorrectly placed `uiScale` inside `resolution` and was rejected with `-32602`, unrecognized `uiScale` at `scenario.resolution`.
Moving it to the scenario root succeeded.
A later explicit-state probe supplied a Government flag and `scriptedGui: {"independence_wave_status_scripted_gui":{"visible":true}}`; inspection rejected it with `-32602`, invalid input at `scenario.scriptedGui.independence_wave_status_scripted_gui`.
This is an unresolved valid-fixture schema/input dependency, not proof that the route cannot support explicit visibility mocks.
No valid complete replacement fixture was established before the parent's no-edit instruction.

Inspection completed with no skipped elements.
The fidelity counts were 556 modelled, five approximated, 15 ignored, zero missing, four unsupported, and 12 unresolved.
The validation flag was true, but it does not establish visual acceptance.
There were 64 overlap warnings, including expected background containment and unresolved sibling/panel cases requiring actual visual review.
The renderer reported four static-fallback-missing animation warnings despite existing static sibling definitions, and four unsupported `gfx/FX/buttonstate_blendframes.lua` execution cases.
No fallback mapping, rename, substitute asset, or animation rewrite was invented.

## Artifacts

All references below belong to the same source revision and baseline fixture.

- [Inspection JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/540a34c94852d79e8ed27fe44a3f29dea658df2230b8216a2e3b34b233dff2a0/a6ab97621a8fd8553454c3383c4c171727af641bc5c22a7d5e14b0d57f0dd831/gui-inspect.002afb7d0452a975.json)
- [Full-window PNG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b69c93a2569d4392d07bd27e1e37652f29cc4edbbecb1d183e58f5d02b41c284/72604e23c1b95e76d97e59f78a75b721d66153847bf8c7df44081d45e80aa01a/independence_wave_status_window-full.png)
- [Cropped PNG, visually inspected](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/85019c3dc77eaec0799fe1b0d0806d2f2942cddebc8fa67357627747fa5a77e4/68ac62d34bb57adb8694860362c145d1a1bc002db964a01b8a1306595fa6d3d1/independence_wave_status_window-cropped.png)
- [Annotated PNG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e76635fc0cc2e020c037ac630c8dbf8fdfa346affc8f6dbcdac575dc7f003273/6fa320686f6b5f2e3292bd415f5abe62a7712926990827932b03f71b1d572f8c/independence_wave_status_window-annotated.png)
- [Click-region PNG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f6eb93da154f832d2b6df86dfb764b56b893af485e1ce1e537e5135601b85f24/ff886b54de42c1c1c8d620a1050e2c4e3eea3b5cdc2cd5aa92a11fffaf3baf64/independence_wave_status_window-click-regions.png)
- [Hierarchy SVG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d6ab51bd1a02d1bcc37371410041db872f48ec537d4ffcbc31799ba71b7e9c69/0c51344f50cda08b9cf81508c15a25dd056e7ce8fd71f07414e3e33bfc78ea42/independence_wave_status_window-hierarchy.svg)
- [Layout JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7b2606749d6351bfa46e11eb729778c2c1d863988a0287ac9b9e74747e8fb712/1368054271ce4566e99da330fe24bbd4fb52b5a32f5d763da0e13e7774376d65/independence_wave_status_window-layout.json)
- [Normalized scenario JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0a38aace1c2c5a5b98a6361d519332414bdf7245c949596e3519ec29fa535ad6/1268f3cd4e8ddb24a2cf98f04e41b393803d35207ecc4666022ac576700602fc/independence_wave_status_window-scenario.json)
- [Fidelity JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/85d50111a5225411f583b688d9e33a1bb67053e92d3e9bf4e1405e0cd6c1636d/9db462db8edba9a9a7f40e996391257f60825ca6bac0b0c68a50b04cdab88105/independence_wave_status_window-fidelity.json)
- [Resolution/scale JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/00a6778f14e4002d617fc6cc1fa0d5472f1ebeaaca8c9081ebcaf78890383260/77c49a76c3a951a4b1a9c583a7f76c7a0fce6cc81dc93786ca0267eb0880dd88/independence_wave_status_window-resolution-scale.json)
- [State matrix JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f75154ec46d0073b647f78f1d870ffea41d5add0b538d832ca2e02cee057978a/84f964bdf4a9f1e8e788e29afe024ae28b0d1662daf4ec3369fd257e1ea5996b/independence_wave_status_window-state-matrix.json)
- [Automatic self-comparison JSON, not repair proof](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c9adc158e6281fc052f521427df898f2b3c8e9cd0fd90224c46f9d285479354c/73f991dc90cd76c3b866c73f0b8b81217af18d7dbffd37326d98667501df7b1b/independence_wave_status_window-comparison.json)

The render returned 27 artifacts, one state, one scenario, five variants, and four resolution entries.
Those automatic variants were not individually visually accepted and do not prove the required 1366 × 768 case.
Its zero changed-pixel self-comparison is not a matched pre-change/post-change comparison.
Large MCP resources were retrieved through the server's documented offset/length resource template because the initial whole-resource response was truncated.
The cropped 716 × 516 image was actually viewed; it includes the native 700 × 500 window and margin.
The other listed visual views were generated but are not claimed as individually reviewed or passing.

## Reference mapping and observed defects

The selected reference is the existing-composition cropped baseline above, used only to locate defects and preserve hierarchy.
It is not an approved corrected reference.
A corrected reference and content-priority mapping remain blocked; no implementation preceded their approval.

| Existing region | Native mapping and bounds | Review result |
| --- | --- | --- |
| Panel | Background at 0,0; 700 × 500 root; clipping enabled | Painted industrial-frame background covers the window in the reviewed crop. |
| Heading | Title at 26,16; subtitle at 28,48 | Title reads normally; subtitle wraps over two lines. No full long-text acceptance claimed. |
| Founding status | Five native icon/text rows, icons x24, text x74, y92/142/192/242/292; text 300 × 36 | Five always-visible mechanic metrics exceed the four-value ceiling before right-column summaries are counted. |
| Host/patron/network | Text at x366, y84–322 | Dynamic values and names remain unresolved in the empty fixture. |
| Phase/mission | Text at x366, y334–450 | Mission logical bounds extend to y450, while tab panels begin y444; final-text overlap requires a coherent fixture. |
| Navigation | Five native tabs at left, y380/412/444; animation/refresh controls at top right | Controls retained; painted/logical centering and click-region acceptance remain incomplete. |
| Tab content | Five native panels all x280,y444, 386 × 42 | Baseline shows severe overprint. Source uses this shared rectangle for mutually exclusive content. |
| State icons | Recognition/dependency near top right; league/formable near bottom right | Static/animated siblings exist; fixture and animation diagnostics remain unresolved. |

The cropped production render visibly overprints the five bottom-right tab panels.
The normal source click paths each set their own tab flag and clear the other four; Government defaults visible when none of the other four flags is set, while the other panels require their respective flag.
This source evidence does not support moving all five panels apart as a safe fix, and the empty fixture does not establish that ordinary click navigation violates exclusivity.
The bad production render remains a completion blocker; it is not dismissed as a renderer discrepancy.

The instability warning at x306,y292 has approximately 48 × 48 logical bounds after scaling.
It intersects the instability text rectangle x74–374, y292–328 and visibly touches the placeholder band text in the crop.
This proves a collision risk in the current geometry, but no final dynamic-text/warning fixture or accepted correction was established before the parent required no edits.
The warning was not moved speculatively.

The renderer reported 11 unresolved dynamic text elements: the five founding metrics/bands, host status, host relationship, patron influence/status/name, network standing/league phase, founding phase, and mission state.
Window visibility was the remaining unresolved input and required an explicit scenario mock.
Literal placeholder widths cannot establish normal, crowded, or long-localisation text acceptance.

## Budgets and action integrity

There are ten simultaneously displayed numeric mechanic values in the source: legitimacy, recognition, administrative capacity, security, instability, host claim intensity, host hostility, host obligations, strongest patron influence, and network standing.
The five founding metrics alone exceed the skill's hard ceiling of four simultaneously visible mechanic values.
The additional host/patron/network summaries make this a parent-owned design/content-priority blocker, not an issue that can be solved safely by a small spacing adjustment.
No metrics were hidden, merged, redefined, or moved into a new navigation design without acceptance.

The five tab controls are navigation, and the animation toggle changes presentation.
Refresh invokes `independence_wave_refresh_country_state`; it is not assumed to be a cosmetic action merely because it appears in a status GUI.
The GUI itself displays no spendable cost string, so there is no demonstrated missing cost texticon in this bounded surface.
The decision owner retains proof of refresh requirements, outcomes, costs, AI equivalents, and cleanup.
No cost, effect, AI, probability, or balance changes were made.
The source has `ai_enabled = { always = no }`; the MCP graph's `aiEnabled: true` projection is a source/projection discrepancy, not an authorization to alter gameplay behavior.
The number of navigation controls is not reported as seven simultaneous gameplay primary actions.

## State and visual acceptance matrix

| Gate | Evidence/status |
| --- | --- |
| Event ownership and bounded selector | Established from exact source and category entry. |
| Pre-change inspection | Succeeded at the recorded revision. |
| Normal 1920 × 1080, UI scale 1 | Rendered; cropped visual reviewed; visible defects remain. |
| Coherent Government/Recognition/Security/League/Ambitions fixtures | Not established; source exclusivity reviewed only. |
| Hover/selected/locked/active/disabled/completed | Not visually accepted; only normal state requested. |
| Warning | Collision visible in baseline; no coherent severe-instability fixture accepted. |
| Empty/crowded/long-text/missing-localisation | Empty substitution baseline exists; it is not proof for the other states. |
| 1366 × 768 and matching UI scale | Required explicit visual acceptance not completed. |
| Static/animated state siblings | Source present; diagnostic/fidelity warnings unresolved. |
| Label centering, symmetry, clipping, spacing, painted bounds | Partial crop review only; no overall pass. |
| Hierarchy and click regions | Artifacts generated; full state-matched review not completed. |
| Visible-value/text-density budget | Failed: ten numeric values, including five founding metrics, against four-value ceiling. |
| Corrected reference and native mapping acceptance | Blocked pending content priority and complete fixture. |
| Post-change inspect/render/comparison | Not performed because no source changes were authorized or applied. |
| Live consumer validation | No game launch or live evidence; no in-game completion claim. |

## Handoff and remaining work

The only worker-created file is this handoff.
Runtime behavior before and after this assignment is unchanged.
No new missing art was established by this bounded review, and no art production, static fallback, gameplay fallback, or simplification was implemented.
Existing ASSET-039 through ASSET-043 remain the asset basis; their presence is not a dynamic-GUI completion claim.

The parent must settle content priority within the four-value budget and provide/accept the resulting narrowly scoped reference before another layout implementation pass.
A subsequent pass must establish a valid explicit fixture for window visibility, tab exclusivity, dynamic text, frame values, and warning state, then review the required states and both target resolutions.
Only then can the bounded collision repair and any accepted presentation changes be compared across matching source revisions, fixtures, hierarchy, and click regions.
The unresolved production overprint, dynamic text, value budget, warning collision, animation diagnostics, and missing matched post-change proof must remain visible in the completion report.
All shared and unrelated interfaces, gameplay, localisation, and assets remain outside this worker's edits.
No commit was attempted: the repair is blocked, and the parent requested no staging/commit while coordinating the repository index lock.
