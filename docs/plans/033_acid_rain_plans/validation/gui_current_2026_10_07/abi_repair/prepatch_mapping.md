# Event033 A4–A6 repair mapping recorded before patch

Recorded 2026-10-07 before any authorized ABI source edit.
Parent acceptance is the explicit bounded A4–A6 instruction, accepted Part 6 / D24 anchors and the prior scoped reference `docs/assets/033_acid_rain/gui_repair_reference/acid_rain_world_window_scoped_reference_2026-10-03.png`.
This annotation preserves the existing design and maps correctness repairs to existing controls, without producing a replacement design or image.

Immutable baseline GUI effects SHA-256: `24b1c3767bdc82094e37c602f297ea71e92637f7b758aff9ceec3615cf1ef64c`.
Immutable baseline scripted localisation SHA-256: `0c9bbd39cfce6cf8c28417424efc18522e8bea97170f571661cf107e10402894`.
Raw copies are retained in `sources_before/`, verified after byte-for-byte copy.
GUI source remains `91faf794f739ca28dbdf637de5a2e48df1c31ff02180759a3fa959e6082c7629`, including the other owner's Main_14 font changes.

| Existing reference/native region | Existing producer and consumer | Intended source-computed correction |
| --- | --- | --- |
| Map front markers in the left map | `acid_rain_gui_project_front_1/2/3` → `acid_rain_gui_set_region_anchor` → existing front marker x/y variables | Caller declares x/y before the anchor call so authored coordinates survive the child frame. No coordinate/layout change. |
| Global storm markers in the same map | Three `acid_rain_gui_refresh_read_only` marker calls → nested region anchor helper → existing superstorm marker/shown/region fields | Each refresh call declares shown, region, x, y. Nested anchor sees inherited x/y and 48-pixel shared-region offsets are retained. |
| Seven region rows and their existing hover text | `GetAcidRainRegion1Tooltip` through `GetAcidRainRegion7Tooltip` → region loader → `acid_rain_gui_region_tt` and weather/name selectors | Each getter declares its ten consumed outputs. Preserve its region input and use the existing projected array facts. |
| National Preparedness label and hover breakdown | `GetAcidRainPreparednessTooltip` → Preparedness loader → existing breakdown key | Declare fourteen tier/point/max outputs. Keep actual tiers, authored gains/weights and existing total. |

Authored anchor pairs by region ID: 1 = 201/83, 2 = 350/126, 3 = 368/61, 4 = 220/115, 5 = 385/175, 6 = 148/74, 7 = 125/138.
Three listed same-region Europe storms therefore intend x = 201, 249, 297 and y = 83 with visible marker flags, while aftercare keeps marker flags hidden.
Inputs and iterator indices are not output storage and must not be reset.
All declarations use `constant:acid_rain_runtime.zero` and are temporary only.
Public output requirements will be documented on the existing helper/getter comments because trigger-source helper comments are outside granted write scope.

The mandatory baseline is the retained actual MCP inspect/render evidence under the parent validation folder, supplemented by source-frame-computed before fixtures for this repair.
Before/after rendering must preserve resolution, uiScale 1, language, states, scenario facts and asset/font bytes, apart from actual source-computed repaired outputs.
MCP declared projection rendering does not execute the production helpers.
Separate-frame tests must execute their real bodies and expose that distinction.
Existing map, background, coverage, checkbox, row-alignment and value-budget findings remain parent/GUI-owner work, not authorized fixes here.

The parent additionally authorizes isolation for all existing GUI effect loops, including the native documented `for_loop_effect` default break field.
There are six for loops and no foreach or while loops in this exact file.
The three region-fact loops and three front severe-count loops will each receive distinct private break temporaries, initialized to `constant:acid_rain_runtime.zero` immediately before the loop and explicitly bound through its existing native break field.
Bounds, iterator names, nested traversal, native caps and publication remain unchanged.
The source replay must honor both the legacy default `break` temporary and each explicit private break field, testing inherited break 1, private break 1 and repeated invocation.

