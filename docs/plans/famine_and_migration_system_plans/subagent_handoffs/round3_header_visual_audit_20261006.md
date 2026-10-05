# Famine and Migration Report Header Visual Audit, 2026-10-06

Disposition: `blocked` for current-source visual acceptance. This was a read-only audit of the existing famine and migration decision-category report headers; no GUI, scripted GUI, art, localisation, or other source was changed. The parent owns these shared utility/category headers, so this work did not use `chaosx_event_ui_worker`.

## Scope and evidence boundary

The requested windows were `famine_report_header_window` from `interface/famine_report_header.gui` and `migration_report_header_window` from `interface/migration_report_header.gui`, attached to their respective decision-category scripted GUIs. The requested output was one 1920×1080 render at UI scale 1 covering famine generic, island blockade, and relief-arrival scenes, plus migration wartime evacuation, closed border, nuclear evacuation, and return scenes.

The live schemas were read from the exposed `mcp__hoi4_agent_tools__hoi4_gui_inspect` and `mcp__hoi4_agent_tools__hoi4_gui_render` declarations. Both schemas expose scenario inputs as `unknown`, `relatedScenarios`, and `generatedScenarios`; render also exposes `resolutions`. The connected tool inventory exposed no separate health/version/capability route, so service health and client task negotiation could not be independently verified. The attempted `hoi4_reference_context(surface="gui")` call did not return within 52 seconds.

The first famine inspect request was immediately rejected with `MCP error -32602` because the scenario object included unsupported `actor`. I removed that field and retried with only `id` and an explicit `flags` map; the input then passed adapter validation, but the request returned no result within the 52-second caller bound. Migration inspect and both render requests used the same supported fixture shape and also returned no result within 52 seconds. These are bounded observation timeouts, not MCP tool status results; no job handle, diagnostics, response artifact, or continuation URI was returned. I made no further GUI-route calls after all four required attempts.

The four accepted fixture requests used `generatedScenarios: { enabled: false }`, `resolutions: [{width:1920,height:1080,uiScale:1}]` for renders, exact `windowName`, and one scenario per distinct state in `relatedScenarios`. Scenario IDs and explicit visibility facts were:

| Window | Scenario ID | Scene flag true | All other scene flags | Dormant flag |
| --- | --- | --- | --- | --- |
| Famine | `famine_generic` | `famine_report_generic` | `famine_report_island_blockade=false`, `famine_report_relief_arrival=false` | `famine_decision_dormant=false` |
| Famine | `famine_blockade` | `famine_report_island_blockade` | `famine_report_generic=false`, `famine_report_relief_arrival=false` | `famine_decision_dormant=false` |
| Famine | `famine_relief` | `famine_report_relief_arrival` | `famine_report_generic=false`, `famine_report_island_blockade=false` | `famine_decision_dormant=false` |
| Migration | `migration_wartime` | `migration_report_wartime_evacuation` | `migration_report_closed_border=false`, `migration_report_nuclear_evacuation=false`, `migration_report_return=false` | `migration_decision_dormant=false` |
| Migration | `migration_closed_border` | `migration_report_closed_border` | `migration_report_wartime_evacuation=false`, `migration_report_nuclear_evacuation=false`, `migration_report_return=false` | `migration_decision_dormant=false` |
| Migration | `migration_nuclear` | `migration_report_nuclear_evacuation` | `migration_report_wartime_evacuation=false`, `migration_report_closed_border=false`, `migration_report_return=false` | `migration_decision_dormant=false` |
| Migration | `migration_return` | `migration_report_return` | `migration_report_wartime_evacuation=false`, `migration_report_closed_border=false`, `migration_report_nuclear_evacuation=false` | `migration_decision_dormant=false` |

No successful current-source inspect or render result exists for these IDs. No current-source full image, crop, annotated PNG, `validation.json`, fidelity report, visibility/enablement result, click-region artifact, or source-revision/scenario hash was returned. I therefore have no image-based defect findings and do not treat earlier stored SVG references as this audit's proof.

## Source-only observations

Both GUI files define a 470×190 non-moveable clipped container at `(0,0)` with `GFX_tiled_window` background. Each scene image is placed at `(7,7)` without an explicit logical size in the GUI declaration; each title starts at `(230,14)` with `maxWidth=220` and `maxHeight=32`; each summary starts at `(230,52)` with `maxWidth=220` and `maxHeight=120`. This leaves a 23-pixel nominal right margin for the title/summary boxes and 38 pixels between the image's origin and the text origin; actual painted bounds, overlap, line wrapping, clipping, contrast, and crop quality are unverified without the requested render artifacts.

The famine window declares three image/title/summary triplets; migration declares four. Their linked GFX definitions resolve each image name to a famine or migration report DDS path. The scripted GUI roots use `context_type = decision_category`, their exact named window, human-only visibility, a false dormant-flag gate, and the relevant selected-scene predicate. The category files attach each header to its matching category. The scene trigger definitions test the corresponding country flags, and the English localisation files contain the title and summary key for every requested scene. These establish wiring and source presence only; they do not prove what appears in the rendered GUI.

The longest English summary in the famine set is the blockade text (94 characters); the longest migration summary is the wartime text (145 characters). With 220×120 text boxes, long-text wrapping is a particular current-source visual check still required. This is a fit risk to inspect, not a confirmed overflow or clipping defect.

## Current source identities

SHA-256 values below were read from the shared workspace during this audit. Header hashes match the values captured before the four MCP attempts.

| Source | SHA-256 |
| --- | --- |
| `interface/famine_report_header.gui` | `CC5D8CB8EE389DEC3EACF3E47A25EEFFCFCA3F6619E75E253CB718A520FAFA8C` |
| `interface/migration_report_header.gui` | `51D5908A2F5E13C5E7E732D115D8834F4DF5106ED1E98E954F5619CE23B022C6` |
| `interface/famine_report_pictures.gfx` | `7CEFBDE5D364519D1DAB2CB6D7AB144EA41EEBC5CE1623C667700C0343DD9F56` |
| `interface/migration_report_pictures.gfx` | `60DCA06F11963A1EDFBD4FFD6C8501B54AE6FB00CDB47C9AF8D0EA0C98EBD19D` |
| `common/scripted_guis/famine_report_header_scripted_gui.txt` | `A5B5938674185188D684DC7A63D277126F94E8AAD79568ECFE62265DCBB37741` |
| `common/scripted_guis/migration_report_header_scripted_gui.txt` | `53AAB49EED8C254978713D4F3412FFD817BAC941414B8F8C7CE5FB3DDFC3C9D2` |
| `common/scripted_triggers/famine_report_triggers.txt` | `F263E5BD9D2DF413ED87CC35D01FB9EF59499D3300F3BA07D10B495E40D9D3F0` |
| `common/scripted_triggers/migration_report_triggers.txt` | `93F7C813CCA1219FF46CD6605B8ADAFFF8DC22C9CA816C0D86C400823B3427C6` |
| `common/decisions/categories/famine_decision_category.txt` | `57F18CAD843ED6B82ADF796486F3CF962F682F7AD4EE9B00E0971AF5AABCE270` |
| `common/decisions/categories/migration_decision_category.txt` | `7F26B478CDA0D46B04E2C77E639843D9604A4E0D82C22F7137AE6089A90F7271` |
| `localisation/english/famine_l_english.yml` | `0AE8EF64D98339D0A550B50E73756764A313377CCE1822A449A57415E78CDC65` |
| `localisation/english/migration_l_english.yml` | `2C232EC324FF100399D5BA274CE4A180B7E09D68CDBD26E5553DDB051D656EF1` |

## References and prior evidence

The local offline wiki files read were `paradox_wiki/Interface modding - Hearts of Iron 4 Wiki.md` (SHA-256 `B74AFC86BE4E5DBB3B0FC600820D73A8340F7DC1821FC5EF02C9EE1F028C0B1C`, relevant container and image/textbox sections around lines 27–33, 77–79, 180, and 198) and `paradox_wiki/Scripted GUI modding - Hearts of Iron 4 Wiki.md` (SHA-256 `B07D850EA78C4E1E3FC113574059AD2F3EA37DF320B9259128D66814023C1F30`, snapshot captured 2026-09-19, window assignment and element visibility sections around lines 31–42). The installed documentation read was `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/scripted_guis/_documentation.md` (SHA-256 `43CE647FC5FDE27488855B060B5463C790E5E356149FCEB010D36B960B40F838`, decision-category context and window assignment at lines 15 and 23, triggers section following line 43). The direct local references were used because the connected `hoi4_reference_context` route timed out; no MCP reference citation or revision was returned.

`docs/plans/famine_and_migration_system_plans/completion_report.md` lines 324–328 records earlier successful split-header inspect/render calls and SVG URIs for famine and migration at two resolutions and normal/long-text/missing-localisation states. That report also says the workspace graph exceeded its 2,000-diagnostic ceiling. Those stored records do not provide the current call's branch-specific PNGs, `validation.json`, or returned source/scenario identities, so they remain historical evidence and cannot close this current visual gate. `post_split_decision_closure.md` lines 137–143 likewise records an older famine SVG and its global-diagnostic limitation.

## Required follow-up

Rerun current-source `gui_inspect` and `gui_render` for the seven named scenarios if the connected route becomes responsive. Keep the same resolution and complete true/false flag maps. Preserve every returned full/crop/annotated PNG and `validation.json`, record `sourceRevision`, source hash, scenario ID/hash and the visibility/enablement evidence, then review each image for bounds, icon/text alignment, text wrapping/clipping, background, asset appearance, and state selection. Until those artifacts are returned and reviewed, the report header visual audit remains blocked; source-only observations above are not visual acceptance.
