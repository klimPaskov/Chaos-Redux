# Event 006 non-portrait asset documentation path reconciliation

Date: 2026-08-30.

## Scope and authority

This bounded pass checked only the named Event 006 non-portrait asset manifests and GFX handoffs for stale current-owner claims.

The current source of truth for the affected small event, report, news, and super-event sprites is `interface/006_independence_wave_small_assets.gfx`.

The former `interface/006_independence_wave_event_pictures.gfx`, `interface/006_independence_wave_mediterranean_assets.gfx`, and `interface/006_independence_wave_form05.gfx` files are absent from the runtime tree.

No gameplay, localisation, portrait, flag, GFX registry, runtime asset, specification, workbook, or unrelated-event file was changed.

## Source-of-truth map and file disposition

| Scoped document | Current-owner evidence | Disposition |
| --- | --- | --- |
| `docs/assets/006_independence_wave/generated_event_scenes_manifest.md` | The manifest names `interface/006_independence_wave_small_assets.gfx` at line 48. | Left unchanged because it is current. |
| `docs/assets/006_independence_wave/generated_event_scenes_gfx_handoff.md` | The handoff names `interface/006_independence_wave_small_assets.gfx` at line 5. | Left unchanged because it is current. |
| `docs/assets/006_independence_wave/low_countries_form03_progression/report_scene/submanifest.md` | The coverage and ownership rows name `interface/006_independence_wave_small_assets.gfx` at lines 18 and 37. | Left unchanged because it is current. |
| `docs/assets/006_independence_wave/low_countries_form03_progression/report_scene/metadata/report_event_006_form03_charter_convention_metadata.json` | The JSON registration object names `interface/006_independence_wave_small_assets.gfx` at lines 97-99. | Left unchanged because it is current and parses as JSON. |
| `docs/assets/006_independence_wave/low_countries_form03_progression/report_scene/gfx_runtime_handoff.md` | The runtime handoff names `interface/006_independence_wave_small_assets.gfx` at line 7. | Left unchanged because it is current. |
| `docs/assets/006_independence_wave/mediterranean_gameplay_assets_2026_07_16/manifest.md` | The manifest names `interface/006_independence_wave_small_assets.gfx` at line 10. | Left unchanged because it is current. |
| `docs/assets/006_independence_wave/mediterranean_gameplay_assets_2026_07_16/gfx_handoff.md` | The handoff names the consolidated small-assets registry at line 3. | Left unchanged because it is current. |
| `docs/assets/006_independence_wave/form05_mediterranean_assets_2026_07_16/manifest.md` | The manifest names the consolidated small-assets registry in the current-registration sentence at line 113. | Left unchanged because it is current. |
| `docs/assets/006_independence_wave/iw043_iw058_generated_visuals_2026_07_18/manifests/asset_manifest.json` | The JSON entries name `interface/006_independence_wave_small_assets.gfx` at lines 1126 and 1176. | Left unchanged because it is current and parses as JSON. |
| `docs/assets/006_independence_wave/iw043_iw058_generated_visuals_2026_07_18/gfx_handoff.md` | The handoff names `interface/006_independence_wave_small_assets.gfx` at line 24. | Left unchanged because it is current. |
| `docs/assets/006_independence_wave/manifest.md` ASSET-048 prose | The ASSET-048 record names `interface/006_independence_wave_small_assets.gfx` at line 168. | Left unchanged because it is current. |

The only file created by this pass is this dated handoff.

The package documents under `docs/assets/` are ignored by the repository policy, so they were not force-added to Git when no stale current-owner claim remained to patch.

## Preserved historical references

Six legacy-path mentions remain in scoped documents, and each is explicitly labelled as former, historical, dated provenance, or a source marker rather than a current owner.

The preserved locations are `generated_event_scenes_manifest.md:50`, `generated_event_scenes_gfx_handoff.md:7`, `low_countries_form03_progression/report_scene/gfx_runtime_handoff.md:18`, `mediterranean_gameplay_assets_2026_07_16/gfx_handoff.md:5`, `form05_mediterranean_assets_2026_07_16/manifest.md:113`, and `iw043_iw058_generated_visuals_2026_07_18/gfx_handoff.md:26`.

Dated historical handoffs such as `006_event6_asset_gap_research_2026-08-22.md`, `006_event6_small_presentation_registry_merge_2026-08-25.md`, `006_event6_small_file_merge_continuation_2026-08-26.md`, `006_event6_support_and_small_asset_registry_merge_2026-08-24.md`, `006_form03_report_asset_handoff_2026-07-15.md`, and `006_event6_completion_audit_v96_2026_08_02.md` retain their original parser-path observations as historical evidence.

## Plan and handoff dispositions

| Record | Disposition |
| --- | --- |
| `006_event6_assets_audit_current_2026-08-29.md` | Retained as a dated audit; its stale-document observations are temporal evidence and are superseded by the current scoped files. |
| `006_event6_asset_source_repairs_2026-08-29.md` | Retained as the preceding reconciliation handoff confirming the consolidated registry. |
| `006_source_of_truth_map.md` | Retained as the current Event 006 source map. |
| This handoff | Added to record the final path-only reconciliation and validation boundary. |

No plan disposition changed during this pass.

## Contradictions, duplicates, and stale instructions

The only apparent contradiction is between the dated 2026-08-29 audit's stale-document findings and the current package documents, which now identify the consolidated registry; this is resolved as a time-separated audit observation, not an active contradiction.

No duplicate current-owner manifest or handoff was found in the scoped paths.

No stale prompt or instruction file was included in the named scope.

## Markdown hard-wrap audit

No path-reconciliation sentence required joining in the checked current-owner sections.

Unrelated existing hard wraps remain in `docs/assets/006_independence_wave/manifest.md` around lines 6-8 and in `docs/assets/006_independence_wave/form05_mediterranean_assets_2026_07_16/manifest.md` around lines 15-18; they were left unchanged because this pass is limited to removed-parser current-owner claims.

## Validation and limitations

The exact old-path scan over the scoped documents returned only the six explicitly historical references listed above.

The exact current-path scan found the consolidated registry in every applicable manifest, metadata object, and GFX handoff.

The current registry exists, all three removed parser files are absent, and both named JSON manifests parse successfully.

The read-only `hoi4.event_inspect` route was not completed in this final documentation-only pass: an initial selector form was rejected because it lacked the required `selector.eventId`, and the follow-up multi-event request was interrupted while finalizing this bounded handoff.

Because that MCP event inspection did not complete, this handoff makes no MCP-backed gameplay or event-chain claim; the path reconciliation is limited to direct documentation text and filesystem evidence.

## Remaining blockers and parent decisions

No path correction remains for the named documents.

The parent should retain legacy registry names only where they are explicitly historical and should decide separately whether ignored package manifests need a repository-policy change before they can become tracked durable documentation.

Unrelated prior asset blockers, including audio-rights review, naming-collision review, NWE alias coverage, incomplete ASSET-046 coverage, flag coverage, and animation presentation alignment, remain outside this path-only cleanup.

No gameplay or asset completion claim is made.
