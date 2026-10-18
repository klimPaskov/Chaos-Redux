# Event033 GUI return ABI repair, 2026-10-07

Disposition: implemented source repair with source-model verification, while the required visual gate remains incomplete.
This handoff resumes the 2026-10-07 tranche on 2026-10-08 and does not approve the full GUI or Event033.

## Authority and current identifiers

The parent explicitly authorized A4–A6 from \`helper_output_contract_audit_2026_10_07.md\`, then extended presentation-only authority to isolation of every existing GUI effect loop kind.
Write authority covers only \`common/scripted_effects/033_acid_rain_gui_effects.txt\`, \`common/scripted_localisation/033_acid_rain_scripted_localisation.txt\`, this handoff and this worker's validation/tests.
The event-owned source still defines \`acid_rain_world_window\` and \`acid_rain_category_inlay\`, bound by \`acid_rain_world_scripted_gui\` and \`acid_rain_decisions_scripted_gui\`.
The resume prompt's logical name \`chaosx_acid_rain_window\` has no definition in those owned GUI/binding files and was not renamed or substituted.
Part 6 explicitly assigns this dedicated map and compact category inlay to Event033, opened from Acid Rain Response and Event033 Event Details.
Shared EventLog, Event Details, Settings, SuperEvent and registries were neither edited nor audited.

Layout, GUI, GFX, assets, runtime, root effects, triggers, selectors, weights, costs, AI and workbooks remain unchanged by this tranche.
No commit, game launch, desktop control, log search, new role or asset production was performed.
The parent retains runtime warning/severe ABI, operation-family, lifecycle and evolution work.

## Exact source identity and immutable snapshots

All paths below are relative to \`C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux\`.

| Source | Before SHA-256 | Applied/current SHA-256 |
| --- | --- | --- |
| \`common/scripted_effects/033_acid_rain_gui_effects.txt\` | \`24b1c3767bdc82094e37c602f297ea71e92637f7b758aff9ceec3615cf1ef64c\` | \`d8da2914c924b5ee200449b811de88d971af99be9e48e4d632cedd46b70a623a\` |
| \`common/scripted_localisation/033_acid_rain_scripted_localisation.txt\` | \`0c9bbd39cfce6cf8c28417424efc18522e8bea97170f571661cf107e10402894\` | \`326cf6d0b4906c0546b3cd1a719656b664e611a61f7adf5245384a43ed955223\` |

Raw copies live under \`validation/gui_current_2026_10_07/abi_repair/sources_before/\` and \`sources_after/\`.
Their physical bytes were SHA-256 verified and were not replaced during resumption.
The intermediate comment-only after hash \`324d43becb12787a5342d70efaab43c401f9e0a825f7eef77ba7839ecd7059d9\` belongs to \`after_replay.json\`, not the final helper source.
\`final_source_replay.json\` and \`resume_source_replay_2026_10_08.json\` bind the final helper hash.

Preserved GUI SHA-256 is \`91faf794f739ca28dbdf637de5a2e48df1c31ff02180759a3fa959e6082c7629\`.
It includes the other owner's 38 Arial12-to-Main_14 edits, left intact.
Preserved GFX SHA-256 is \`a24cba2e9b7c4b567a96c0d1731ac97ee136e48cf41db0f8e03fef8bff29b7f6\`.
Preserved scripted GUI SHA-256 is \`6f04ffdc4596f6ce54ece1c0f87de7edd7aa2b8021bb915f9712836cc1893903\`.
The current replay's read-only dependencies are triggers \`ec7bec54a95a62e321a5344d5ab05cd23d57698b45f38db262e56528ecbf0681\`, constants \`58deff691f6e43f7de79cf60a5757dfdcb9e003b77d7104bd064ec7a5a83137c\` and English localisation \`5f8169ac30b4cf546d5b91b03f347ba868890a65788df9d4724b12db1bd51963\`.
Those dependencies are not claimed to be a frozen whole-workspace historical snapshot.

## Applied caller contracts

| Surface | Exact repaired caller or API | Applied storage |
| --- | --- | --- |
| A4 | \`acid_rain_gui_project_front_1/2/3\`, anchor calls at current lines 613, 645, 677 | Declare \`acid_rain_gui_anchor_x/y\` before each anchor helper, preserving the region input. |
| A5 | \`acid_rain_gui_refresh_read_only\`, marker calls at 346, 367, 388 | Declare \`acid_rain_gui_marker_shown\`, \`acid_rain_gui_anchor_region\`, \`acid_rain_gui_anchor_x/y\` before each marker call. The complete envelope reaches the nested anchor helper. |
| A6 region | \`GetAcidRainRegion1Tooltip\` through \`GetAcidRainRegion7Tooltip\`, loader calls at 505, 526, 547, 568, 589, 610, 631 | Declare all ten consumed \`acid_rain_gui_tt_*\` outputs inside each consuming \`text.trigger\`, preserving \`acid_rain_gui_tt_region\`. |
| A6 Preparedness | \`GetAcidRainPreparednessTooltip\`, loader call at 679 | Declare all fourteen tier, points, maximum and total-maximum outputs before the loader. |

The ten region outputs are eligible, touched, untouched, status, front, active, visit, quota, severe and days.
The fourteen Preparedness outputs are shelter/water/medical/transport tier, points and max, plus max_tier and preparedness_max.
All declarations use \`constant:acid_rain_runtime.zero\` and temporary storage.
No new persistent gameplay fields or controls were added.
Existing public marker and anchor helper comments document the required caller envelope and initial values, and getter comments document the loader envelopes within the authorized localisation file.

## Loop isolation

The exact file contains six \`for_loop_effect\` loops and zero \`while_loop_effect\`, \`for_each_loop\` or \`for_each_scope_loop\` loops.
Every present loop has an immediately preceding zero reset and explicit private break binding.

| Existing loop | Private temporary |
| --- | --- |
| Region fact rows | \`acid_rain_gui_region_facts_regions_break\` |
| Region fact front traversal | \`acid_rain_gui_region_facts_fronts_break\` |
| Nested regional severe cells | \`acid_rain_gui_region_facts_severe_break\` |
| Front 1 severe cells | \`acid_rain_gui_front_1_severe_break\` |
| Front 2 severe cells | \`acid_rain_gui_front_2_severe_break\` |
| Front 3 severe cells | \`acid_rain_gui_front_3_severe_break\` |

Bounds, comparison semantics, indices and existing publication remain unchanged.
No foreach loop or undocumented foreach ceiling was invented.
The source contains no intentional private-break early stop to modify.
The documented native for-loop cap remains intact.

## Acceptance and before-patch mapping

The parent accepted existing Part 6 / D24 region anchors and the prior scoped reference.
\`validation/gui_current_2026_10_07/abi_repair/prepatch_mapping.md\` was written before the patch and maps the repair to the existing map markers, region-row hover consumers and Preparedness hover consumer.
The accepted image is \`docs/assets/033_acid_rain/gui_repair_reference/acid_rain_world_window_scoped_reference_2026-10-03.png\`, SHA-256 \`2ca8693424c479bd0a40ee1ff34d8d75727a82ba22d6398117e5add221594bda\`.
No redesign or replacement art was produced.

Authored region anchors remain 201/83, 350/126, 368/61, 220/115, 385/175, 148/74 and 125/138.
Three listed Europe storms retain the existing 48-pixel shift, producing x 201, 249, 297 and y 83.
Aftercare preserves hidden marker flags under the existing global-layer gate.

## Separate-frame source tests

Run \`node docs/plans/033_acid_rain_plans/validation/gui_current_2026_10_07/abi_repair/source_frame_tests.js\` from the repository root.
The resumed test passes 149 assertions, recorded in \`resume_source_replay_2026_10_08.json\`.
The before replay has 119 assertions including explicit defect reproduction, recorded in \`before_replay_v2.json\`.
These are assertion counts, not 149 native game runs.

The runner parses actual source bodies, clones temporary frames at scripted-helper calls and copies back only caller-preexisting storage.
Global and COUNTRY regular saved maps remain separate from temporary storage.
It executes complete front projectors and marker/anchor helpers, the actual reset-and-three-marker-call refresh tail, region/Preparedness loaders and localisation selectors.
A source AST comparison preserves non-envelope helper and selector structure.
A separate inventory checks all four loop kinds, six unique bindings and each immediate zero reset.

The before cold model loses x/y at all three front consumers, loses all four outer marker outputs even with an inner-only repair, and retains none of the ten/fourteen getter outputs.
The applied model retains all seven authored anchors, nested markers, all region weather selectors, nonzero tooltip facts, tier clamping and component points.
With inherited break 1, the baseline performs zero modeled loop visits.
The repair performs 202 visits in each repeated full traversal fixture, publishes severe counts 10/11/11 and all seven eligibility rows, and preserves the caller's break value 1.
Seeding each private break with 1 gives the same complete repeated traversal.

The date converter is explicitly a fixture-relative stub.
These tests do not execute HOI4, native fixed-point/date behavior, campaigns, callbacks, payments, hover timing, save/load or the actual native getter engine.
\`cold_projection_fixtures_2026_10_08.json\` adds distinct source-body projection cases with inherited/private break 1, actual front reset/admission, region publication, marker tail and source-resolved getter strings.
Remaining ledger/country values are declared synthetic inputs, not gameplay observations.
No engine-generated \`[!action]\` text was fabricated.

## MCP evidence and current gate

All calls use explicit workspace \`mod_chaos_redux_ea3b2d67c2c0\`, native 1920x1080 / 1600x900 / 1366x768 at uiScale 1 and \`generatedScenarios: { enabled: false }\`.
Primary scenario resolution is explicit, independent of the resolution gallery.
The earlier gallery-only “1600/1366” requests produced primary 1920 images and are retained as such, not counted as lower-resolution primary proof.
The old 65.6-million aggregate budget rejection was not evaded by shrinking a preview or changing native UI scale.

Inspect/render requests and exact returned artifact URIs, SHA-256, byte counts, diagnostics and source revisions live in the owning validation folders.
Successful PNG/JSON/hierarchy copies were verified against their returned artifact identities.
Full SVG URIs remain in each tool result and are not claimed to be downloaded where only the URI was retained.
Automatically emitted zero-delta self-comparison artifacts do not count as historical source comparisons.
No helper-source overlay through the GUI-only sourceBaseline field was invented.

| One-front native image | Before source revision | After source revision | Historical qualification |
| --- | --- | --- | --- |
| 1920x1080 | \`b8c2ebc7303fa29b51eef6f237fbba4f2f26c3734c9e1d67dad8683530a5d205\` | \`3ad1449d98f520a81a524f5edc2b80cdb63d0e1880ffc52c562b4480eaf20ff2\` | Before graph contains original scripted localisation hash, after graph contains patched hash. |
| 1600x900 | \`2569b65df6e3cc2c4019f02e403dc418830fdeff433fa5f1d742dff87135bb3f\` | \`3ad1449d98f520a81a524f5edc2b80cdb63d0e1880ffc52c562b4480eaf20ff2\` | Before graph contains original scripted localisation hash, after graph contains patched hash. |
| 1366x768 | \`3ad1449d98f520a81a524f5edc2b80cdb63d0e1880ffc52c562b4480eaf20ff2\` | same revision | Before-output reconstruction on patched presentation source, not historical before-source proof. |

These files are under \`abi_repair/before/regional_one_<resolution>/\` and \`after/regional_one_<resolution>/\`.
Actual after full images at all three resolutions, the 1920 crop and the 1366 click-region image were inspected.
The before marker overlaps the map title at output x/y 0/0, while the repaired source-computed output places it at the Europe anchor.
All five navigation controls remain in bounds, with distinct modeled hit regions.
This is declared source-output projection through MCP, not observed gameplay producer execution.
The one-front render reports unresolved 0 / missing 0, but approximated 2 and unsupported 2 for the animated effectFile path.
Those limitations are retained without excusing visible defects.

\`before_inspect_result.json\` and \`after_inspect_result.json\` preserve the actual inspect responses.
The latter returned GUI_INSPECTED for 160 selected elements, skipped source 0, unresolved 0, shared revision \`3ad1449d98f520a81a524f5edc2b80cdb63d0e1880ffc52c562b4480eaf20ff2\`.
Its linked artifact is \`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2d268a12cb8ffa8a0f23126bc8a20c73167b3781256d12b8f75fe2a4abb87a3f/64842413a39b7748106ed7d6d2557567d0d9711ac55c3e5cea04e62a5d1d0dda/gui-inspect.3ad1449d98f520a8.json\`, declared 1849204 bytes.
An artifact URI alone does not establish that all its bytes were archived.

### Observer loss and outstanding proof

The old observer cells 94, 108 and 111 returned “exec cell not found” on resumption.
No durable backend job IDs were supplied for these synchronous calls.
Backend failure is not inferred from observer loss.
\`recovered_manifest_inventory_2026_10_08.json\` retains exact recovered own scenarios and verified cache bytes.
Late before-output cases captured patched localisation, including regional_two_1600x900, and cannot be promoted into historical pre-patch evidence.

The current connected server reports 3.10.0, stdio, PID 37212, started 2026-10-08T07:03:42.943Z.
This differs from the prior PID 43056 and does not establish completion of its old requests.
The current source/config/schema identity is retained in \`resume_2026_10_08_status.json\`.
No backend source or configuration was changed.

The new paired tooltip requests compare real before-source-computed and after-source-computed text through current presentation source at all three native resolutions.
They are a documented output-scenario comparison, not historical source-version or native getter execution proof.
The first 1920 region-tooltip request returned a client observation timeout after 600 seconds.
It is retained in \`paired_tooltips_2026_10_08/region_tooltip_1920x1080_paired_outputs/tool-result.json\`, with backend outcome unresolved.
It was not retried.
New cold-source phase requests are distinct inherited-break projection checks, not duplicates of lost marker-only requests.

Still required before a visual completion claim: actual current-source two/three-front, global, aftercare/static image and hit-region review across the native matrix, completed tooltip views, exact qualifying before/after lineage, resolved visible owner defects and final parent review.
The literal \`chaosx_acid_rain_window\` naming mismatch also remains explicit.
The first whole-file script_validate request was rejected because file checks infer kind/scope, and the corrected old request's outcome was not observed.
No script_validate pass is claimed from that missing response.

## Retained visible findings outside this repair authority

| Finding | Concrete evidence and owner work |
| --- | --- |
| Weather-state/asset distinction | Dense worldwide weather remains in one-front and quiet aftercare composition. Aftercare had all weather/marker flags hidden and zero shader approximation yet still showed storm art. Parent/GUI-asset owner must correct the owned composition. |
| Global/empty card background coverage | A 272x86 texture paints only 86 pixels in the logical 272x267 global/empty card, leaving the storm rows or no-front text outside the designed panel. |
| Completion marks | Complete regions render the hollow first checkbox frame rather than a completed check. Owner must verify the native checked frame, not merely trust a completed variable. |
| Coverage bar accuracy | 35 percent is shown with 212/536 pixels of fill, about 39.55 percent. The 55/75 examples likewise overshoot. |
| Inlay alignment | Status text baseline 67 and World map label baseline 77 differ by about 10 pixels in the same row. Main_14 is preserved. |
| Tooltip hover boundaries | National warning/exposed/severe tooltip rectangles overlap by one pixel at two boundaries. Native pointer arbitration was not executed. |
| Value and wording review | Header Air/current-added-remaining/deaths plus coverage and Preparedness exceed the normal mechanic-value budget. “Next dissipation” describes a check window as though it were a fixed end. Parent must reconcile accepted ledger presentation and truthful labels. |

These remain findings, not renderer discrepancy excuses.
Manual Motion Off partners were actually rendered in the prior scoped review, while automatic fallback-association warnings and animated shader limits remain in the MCP diagnostics.
The tiny clipped-height diagnostic difference was approximately 4e-14 pixels with no observed cut edge, and the diagnostic remains retained.
The scoped GUI skill companion \`references/visual-review.md\` was absent, so the full inline skill checklist was used and that reference gap remains documented.
The parent separately owns full v3 cloud-frame visual/loop approval.
The brief's uiScale 1 matrix does not establish Part 6's additional 125 percent scale acceptance.

## Primary references and limitations

\`primary_references.json\` retains live revision-bound reads for installed effects set_temp_variable 7820–7827, triggers set_temp_variable 7482–7488, effects for_loop_effect 4312–4330, offline Data structures Variable types 435–443 and for_loop_effect 1220.
Effects revision is \`2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af\`.
Triggers revision is \`7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29\`.
Offline Data structures revision is \`62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4\`.
The incorrect first wiki-section ID was rejected with REFERENCE_POSITION_OUTSIDE_SECTION, then corrected through targeted search/read.
No complete reference coverage is inferred from a context heading bundle.

Prior GUI evidence also read installed \`common/scripted_guis/_documentation.md:1–146\`, offline Interface buttonType 227–256 and Scripted GUI window/parent sections 40–143, plus graphical frame-animation sections.
Vanilla \`interface/sov_paranoia_system_scripted_gui.gui:20–64\` and \`common/scripted_guis/SOV_paranoia_system_scripted_gui.txt:1–84\` were directly read and source_lookup bound to exact definitions.
Their revisions are \`4965a0c3e86ed8b68dc578d77058037f27c3f7ef9ff744a5e93bf8fe1109bc43\` and \`fa24329d87cc2b9c273a54da873a53294f634f4c0bdb1be81fd5e0b8eadafef6\`.
The loop-isolation reference was read completely, together with installed foreach/for/while break documentation.
No native helper cleanup, date arithmetic, hover timing or game outcome was claimed from these references or source tests.

## Completion status and simplifications

Source repair is implemented and reproducibly source-model verified.
Mandatory visual proof remains partial, and no full GUI/Event033 approval or completion is claimed.
No implementation simplification or fallback was introduced.
Missing visual evidence, observer outcomes, historical tooltip/source lineage, native behavior and owner patch/review gaps are explicitly unresolved rather than replaced by source-only claims.
Skills used are chaos-redux-events, chaos-redux-scripted-gui and chaos-redux-subagents for this resumed tranche, with the earlier event-assets/frame-animation/decisions skill review retained in the scoped audit.
No skill was created or edited.

