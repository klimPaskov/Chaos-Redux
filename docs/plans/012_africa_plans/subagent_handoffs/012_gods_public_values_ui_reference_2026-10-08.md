# Event 012 Gods public-values UI implementation handoff

Disposition: `implemented` source with bounded preview limitations; final visual coverage remains incomplete for the specific states below, with the parent 20/15 boundary recheck appended at the end.
The parent explicitly reviewed both integrated v4 native ImageGen references, accepted their composition/mapping, and sent `PROCEED` before implementation.
The parent later accepted only the saved participant 48/38 crop, not overall latest-source, hover, full-parent, or multiscale completion.
This current handoff supersedes its phase-one queued status and is the single implementation record.

## Ownership, parent, and entry point

Event 012, repository slug `africa`, is Africa Is One; `chaosx.nr12.602` introduces the Gods subsystem in `events/012_africa_gods_of_africa.txt:42-55`.
Both ordinary categories in `common/decisions/categories/012_africa_gods_categories.txt` attach `scripted_gui = gods_of_africa_public_values`.
The approved block has `context_type = decision_category`, `window_name = gods_of_africa_public_values_window`, and player-country scope.
Vanilla `countrydecisionview.gui:65-72` supplies the 502-unit category slot within a 550-unit decision window; the category inlay follows its description and precedes the ordinary decision list.
The display is 502 by 172 logical units and creates no separate opening action, tab, fullscreen window, metric, cost, AI, or gameplay effect.

Only five new engine text files, the two category presentation attachments/picture assignments, the two ordinary English headers, and event-owned asset/document paths were changed.
Parent-owned industry localisation and cost strings in `012_africa_gods_l_english.yml` were preserved.
No Git operation, game launch, workbook edit, message to another thread, shared UI edit, or data-owner effect/trigger edit occurred.

## Accepted references and exact artwork

- Participant reference: `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/docs/assets/012_africa/gods_public_values_ui/participant_with_picture_reference_v4.png`, SHA-256 `eb72e986119f9160e8dbdd8725b7e75db1e99176dff52a3664e8bf507d141cd4`.
- Host reference: `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/docs/assets/012_africa/gods_public_values_ui/host_with_picture_reference_v4.png`, SHA-256 `687195983eda773ac89b45651a1ecda8cee4576a9fafd38ea456634979179535`.
- Exact 114x101 decoded picture preview: `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/docs/assets/012_africa/gods_public_values_ui/category_picture_native_preview.png`, SHA-256 `00ba993dae9878710a18dd6442be4287511dbba19028c3ac683b9ce2579897b8`.

The accepted v4 references are native ImageGen composition studies; no generated scene or painted meter pixels are runtime artwork.
Runtime consumes exactly one `GFX_decision_cat_picture_012_africa_gods` icon, registered in `interface/012_africa_event_pictures.gfx:20`, from `gfx/interface/decisions/012_africa/decision_cat_picture_012_africa_gods.dds`.
The 114x101 picture stays at native aspect and size at x0/y35; text and meters occupy a separate right region.
The initial picture-only native capture (`event012_gods_public_values_picture_probe`, source revision `7dd1dbf2b0b95402c1074e2d1b861d58dd8156db684d82fdff0e6a29c10913d6`) was reviewed before removing either category picture assignment.
The post-removal picture capture (`event012_gods_public_values_picture_single`, revision `6ec3a147f4caae29641c391fccb8384cfba7399769f60ec7ff2fb046776dd3ac`) retained the same full-image SHA `9517f61bdc40863520140ac32310b7626d10efd5b7b93546355bb7c08cec82b7`.
This proves the selected widget retained its picture; source review proves both old category assignments were removed, while the exact-window selector does not render the entire category consumer.

## Native element mapping

| Reference region | Native elements and logical bounds | Data and interaction |
| --- | --- | --- |
| Left picture | `gods_of_africa_public_values_picture`, x0/y35, 114x101 | Exact existing picture sprite once; decorative. |
| Strength region | `gods_of_africa_public_strength_row`, x120/y0, 382x84 | Existing `GFX_012_africa_gods_strength` icon 64x64 at row x0/y4. |
| Wrath region | `gods_of_africa_public_wrath_row`, x120/y86, 382x84 | Existing `GFX_012_africa_gods_wrath` icon 64x64; guarded actor cache plus pure visibility helper. |
| Name/value | `*_name` x72/y1, 120x22; `*_value` x190/y1, 100x22 | `hoi_18mbs`; cached floor integer /100; value has native `pdx_tooltip`. |
| Band/trend | `*_band` x72/y23, 200x20; `*_trend` x276/y23, 96x20 | `hoi_16mbs`; existing band getters plus Rising/Falling/Steady word. |
| Fill | `*_meter`, x72/y44, displayed 181x15.8375 | `GFX_012_africa_gods_public_values_meter`, native `frame` binding, 101 static states. |
| Next tick | `*_threshold_20/40/60/80` or `*_threshold_15/30/50/70/85`, y42 | `GFX_progress_marker`; one next raw boundary visible, none above highest band. |
| Next label | `*_next_threshold`, x72/y62, 300x20 | Next band and threshold; `No higher band` at Strength80+ or Wrath85+, while fill continues to100. |
| Host lower region | `gods_of_africa_public_host_context`, x120/y86, 382x84 | Mutually exclusive with Wrath; doctrine x72/y5 and reach x72/y32, 300-wide; reach also has Strength tooltip. |

The `*` prefixes in this table are `gods_of_africa_public_strength` and `gods_of_africa_public_wrath`.
Strength marker x coordinates are 102/138/175/211; Wrath marker x coordinates are 93/120/157/193/220, centering the 12-pixel marker on the 181-unit rail boundaries.
The existing band getters are `GetGodsOfAfricaStrengthBand` and `GetGodsOfAfricaWrathBand`.
New getters are `GetGodsOfAfricaPublicStrengthTrend`, `GetGodsOfAfricaPublicWrathTrend`, `GetGodsOfAfricaPublicStrengthNextThreshold`, `GetGodsOfAfricaPublicWrathNextThreshold`, `GetGodsOfAfricaPublicStrengthReachLine`, `GetGodsOfAfricaPublicStrengthCause`, `GetGodsOfAfricaPublicWrathCause`, and `GetGodsOfAfricaPublicWrathFloor`.

## Binding, static meter asset, and source corrections

The parent-reviewed API is from source observer `f60193166208a306426959d24a44ee402bf4fc56` (parent-supplied identity; no Git verification).
The UI reads `global.gods_of_africa_strength_display/fill/frame` and actor `gods_of_africa_wrath_display/fill/frame`; original raw metrics remain the band and threshold truth.
Strength rising/falling flags are read on `event_target:africa_host`; Wrath rising/falling flags are read on the actor; no flag means Steady.
The pure `gods_of_africa_public_wrath_is_visible` excludes the current host and requires the actor's raw Wrath variable.
Rows also require all delivered caches; absence hides the consumer rather than displaying an invented zero.
Host doctrine/reach require the current host identity and valid Strength data.
No capture-only engine binding was installed; all fixtures are external MCP requests and JSON records.

The installed decision-category documentation does not establish a dynamic `progress` property, so the final source uses the explicitly approved SOV-style dynamic `frame` route.
An earlier direct-progress prototype rendered correctly offline but was not accepted as engine syntax proof and was replaced.
`build_native_meter_frames.py` compiles a static 101-frame DDS from the exact installed `subject_progress_bar_long.dds` and `subject_progress_bar_long_bg.dds`, matching the selected stock rail family; this is numeric state selection, not animation.
Stored frames are 160x14, atlas16160x14, keeping its width below16384; native icon `scale = 1.13125` restores 181x15.8375 display bounds without moving labels or markers.
Frame1 is empty,49 is48%,39 is38%,81 is80%,86 is85%,101 isfull; the approved cache quantizes sub-point values downward, under one percentage point.
The texture lives under the authorized asset path `gfx/interface/012_africa/gods_public_values_meter_101.dds`; the parent promoted unchanged texture bytes from the source workspace into the shipped graphics path.
Source texture hashes: fill `829cd572703bd25cdd873c1187a5abc611d15ff7589c748243dfc7fc4a730c01`, rail `559d4b2102894c76a575e417e92e1e2dac5a6bdc2a52bd81129456e346f3ecc7`.
No new external artwork, portrait, illustration, third-party asset license, or animated asset was introduced; the compiled rail uses installed Paradox artwork and the existing mod icons/picture retain their original provenance.

A confirmed exact-boundary defect used strict shortened `check_variable >` lower bounds and hid the next tick at20/40/60 and15/30/50/70.
Seven lower-bound predicates now use explicit `compare = greater_than_or_equals`; `threshold_review.json` evaluates the actual source blocks against existing constants immediately below, at, and above all nine thresholds.
This correction followed the last MCP source snapshot and is source-verified, not visually recaptured.
The new English file's key indentation was corrected without changing the parent-owned English file outside the two ordinary headers.

## Actual captures reviewed and acceptance scope

Current saved render request, result identities, source revision, diagnostics, and artifact URIs are in `mcp_final_render_manifest.json`.
The last successful render is `event012_gods_public_values_frame_48_38_final`, revision `fadc0bc0e30e7867220daae540ecf9eda5f77a40f1fbc616d77ba5b1b75a0d6f`.
The native GUI hash for this composition and current source is `aae60f5ff015f1a58f39590133f51e424402f37f965066819e6299ec91474442`; the final scripted-GUI hash differs from the captured strict-boundary version and is listed below.
The parent accepted `mcp_frame_final_cropped.png` only for its 502-width participant layout: icons,48/38 values, bands, trends, and Next60/50 fit and read cleanly.
That artifact's exact SHA is `5fb3ad49bacf7748c7a6011b06671f46f3fa9c773f488ddc78a4a277202ddbbf`; full-image SHA is `692080d12e6b4d2c3d456ba45f7cf42c94f5f7499eeb9b657af1833e1c6cef69`.

Reviewed saved artifacts in `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/docs/assets/012_africa/gods_public_values_ui/`:

| Artifact/state | Actual review and limits |
| --- | --- |
| `mcp_frame_final_full.png`, `mcp_frame_final_cropped.png` | Full exact-window canvas and native crop reviewed;48/38 fills are distinct and correct to native pixel precision; picture once. Parent accepts crop only. |
| `mcp_frame_final_scenario-matrix.png/.svg/.json` | Eight named1920x1080 fixtures; underlying native PNGs extracted unchanged from the returned SVG, with hashes in `mcp_embedded_scenario_images.json`. |
| `mcp_embedded_minimum_final_detail.png` | Genuine valid0/0 caches: empty rails, Calm/limited bands, next20/15 ticks and labels. |
| `mcp_embedded_highest_band_final_detail.png` |80/85 partial rails; both `No higher band`; Wrath Rising visible. |
| `mcp_embedded_maximum_final_detail.png` |100/100 full rails; both `No higher band`; Wrath Falling visible;100 text fits. |
| `mcp_embedded_treaty_floor_hover_final_detail.png` |48/70 with broken-agreement/unresolved flags: qualitative cause and activefloor fit in two native tooltip lines. This coherent fixture replaces the old38-with70-floor styling fixture. |
| `mcp_frame_final_resolution-scale.png/.svg/.json`, `mcp_resolution_1280x720_1_detail.png`, `mcp_resolution_2560x1440_1.25_detail.png` | Emitted primary participant matrix is1920x1080@1,1280x720@1,2560x1440@1.25; extracted native PNG details reviewed with aligned art/text/rail and no visible clipping. Related boundary/hover/host cases are1920 only, not a24-case resolution cross-product. |
| Host/absent-cache matrix fixtures | Final matrix shows Strength/doctrine/reach without Wrath, and art-only without fake numbers. Visibility is an explicit capture assumption; actual host scope remains source evidence. |

Earlier completed images retain their original scope and were not replayed: host full/crop/resolution capture at revision `5908f3a9d5efeec5830d902fae8b79c21c5058afff5c0f0762d7ea5769797406`, and Strength default-cause tooltip full/crop at revision `ac8ece8019daa6aaa6e97881d3cc8ff83ddb359d776ae8df3459e8bc4df28b30`.
Host hashes were full `c6603602ed87d89fa06f43e6cde7d559304ff72b4697e5971c2de9f3e706ef1c`, crop `2968a9979f7c6f0935bc45d5d7536e4b339f55a5897a0148588faed24af1b319`, resolution matrix `5d46189d8279a594e93844149793e32e2223358f12fe1e3903f3151719fa64c0`.
Strength tooltip crop hash was `ff0ddab03d25526a9dea291dbd96a621c80d652f3eb77e5d828a461a5a9e83cc`, showing three visual lines of concise contributors and reach.
The earlier participant stock-rail render at revision `55ea40529cfce2b42f8cd154a3cf1ef98a10f0d4d4fc8e8ebe620542002db3ab` compared with the picture-only GUI baseline using matched48/38 inputs;31164 pixels changed, ratio0.015028935185185185.
That comparison adds real widgets to the existing picture; it is not a historical full-category or live-game comparison.
`mcp_participant_48_38_subject.png` and earlier probe/candidate images remain retained iteration evidence, not final source proof.

## Specific check limitations and dispositions

- Last normal preview source graph linked without blocking diagnostics; primary fidelity had no missing/unresolved/unsupported entries. The passing result does not prove game execution or the final inclusive tick patch.
- Final exact20/15 and treaty70 captures still contain the missing next tick from the pre-correction predicates. Source correction and actual-block boundary checks are complete; no final recapture was made after the shared initial-plus-narrowed retry budget.
- Host and no-cache captures explicitly override row visibility. Their hidden-child trigger operands remain unresolved in MCP when Wrath or all metric variables are absent; native source guards hide those rows. These fixtures do not prove country/event-target resolution in a campaign.
- Wrath hover fidelity explicitly approximates caller placement/padding and stretched ToolTip frame composition; delayed timing and `click_to_front` are unsupported. Text, line count, contrast, and bounds were reviewed; automatic native placement, frame composition, and timing were not established.
- Strength event-target Rising/Falling and capital-loss/surrender cause branches, the other Wrath floor/cause combinations, longest no-floor tooltip, host final-frame multiscale/hover, and exact boundaries at other tiers have source review but no final native preview. Existing Strength default tooltip and host geometry reviews remain valid for their original revisions.
- The exact-window selector renders the widget on a canvas, not its complete expanded decision category with description/list and sibling consumers; overall parent integration placement is source/vanilla evidence.
- Old Wrath-hover fidelity and crop retrievals returned `Artifact provenance manifest is unavailable`; the issue received one alternate artifact/chunk retrieval and stopped. New native PNGs embedded in the current successful SVG were retained; no service repair or replacement client was created.
- Prior stock progress-sprite source-index errors are superseded by the final registered static sprite. Six overlap/alignment findings are the intended tick-on-rail relationships. Hidden0x0 clipping/size findings describe hidden fixture children. Fixed-category normalized-viewport drift is reported; actual three-resolution native crops remain aligned within the fixed502-unit category geometry.

There are no dropped required metrics, fills, bands, trends, threshold cues, hover widgets, or existing picture art, and no gameplay simplification.
The explicitly approved static-frame route is the native binding adaptation; under-one-point quantization and stored-texture resampling are disclosed above.
Final visual completion is not claimed for the uncaptured correction/states; no unavailable check is promoted to an implementation blocker or an infinite retry request.
No new extension is proposed in this bounded repair; any later presentation expansion stays parent-owned.

## Final source hashes and files

Paths below are relative to `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux`; `final_source_hashes.json` also records untouched data/picture dependencies.

| Changed engine/asset file | SHA-256 |
| --- | --- |
| `interface/012_africa_gods_public_values.gui` | `aae60f5ff015f1a58f39590133f51e424402f37f965066819e6299ec91474442` |
| `interface/012_africa_gods_public_values.gfx` | `e392e9af38cf823126587ee3a84d3ca272825f8c6e0aa35d46d2a46675462024` |
| `common/scripted_guis/012_africa_gods_public_values_scripted_gui.txt` | `f2ca1bf0a2165804855d18143588b8f124964974c1241d9b54291fc4bba9cccf` |
| `common/scripted_localisation/012_africa_gods_public_values_scripted_localisation.txt` | `3b68835ff86d823c969df7a08ad6e6dec5945388d11fc88c6d596b6466dd4192` |
| `localisation/english/012_africa_gods_public_values_l_english.yml` | `5bfc17fdb9d3333a7752765deaf79f59a179407f587d463c54f6fd64b0699999` |
| `common/decisions/categories/012_africa_gods_categories.txt` | `146055668936f6c519f0818fab858c0ddff2de369f501abdfc6d9f39c5d5fe0e` |
| `localisation/english/012_africa_gods_l_english.yml` | `27ec52a8cb192856dd9fa6b2341e70bed229bdb5c9c17eed3356e7be4665ba2a` |
| `gfx/interface/012_africa/gods_public_values_meter_101.dds` | `6d3a43efced0dddb4afe9b4209b7f29b192ddfefa1270aa3cbf4684891282de0` |

The category change is limited to its presentation comment, two attachments, and two removed picture assignments.
The main English changes are exactly `gods_of_africa_participant_category_desc_ordinary` and `gods_of_africa_host_category_desc_ordinary`, describing native actions without repeating the displayed metrics.
Whole-file hashes identify shared source at delivery and do not imply ownership of unrelated parent hunks.

## Reference and native precedent citations

`hoi4.reference_context(surface = gui)` and targeted `hoi4.reference_search` and `hoi4.reference_read` calls used the connected `hoi4_agent_tools` service in workspace `mod_chaos_redux_ea3b2d67c2c0`.

Offline `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md:225-228`, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`, says a category scripted GUI appears below its description and uses the `decision_category` context.

Offline `paradox_wiki/Scripted GUI modding - Hearts of Iron 4 Wiki.md:40-67,157,395-441`, revision `b07d850ea78c4e1e3fc113574059ad2f3ea37df320b9259128d66814023c1f30`, covers independent window assignment, `decision_category` context, dynamic frame properties, and tooltip-compatible native elements.

Offline `paradox_wiki/Interface modding - Hearts of Iron 4 Wiki.md:31-34,73-80,152-177,371-386`, revision `b74afc86be4e5dbb3b0fc600820d73a8340f7dc1821fc5ef02c9ee1f028c0b1c`, covers containers, element types, and parent-relative positions.

Offline `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md:143-173`, revision `f8e3d4ad382f4e5f8e170492a484d090bad62e3711cabfb5d3bf84e58ab32dd9`, documents `progressbartype`, its two textures, colors, size, direction, and step precision.

Installed `common/scripted_guis/_documentation.md:1-146`, revision `43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838`, documents `decision_category` attachment, scope, `window_name`, visibility, properties, frames, and triggers. Installed `common/focus_inlay_windows/documentation.md:34-41`, revision `88811b9f1fa564c8e1e3fc756591808cd2c96d52fb4809b0dc475f30f23a8a2d5`, demonstrates a `progress` variable for focus inlay progress bars; it does not establish the same property for a decision-category scripted GUI.

The reference search route reported `script_doc` unavailable while `wiki` and `game_doc` sources were available. The relevant offline wiki and installed documentation sections above were retrieved successfully. An initial `reference_context` question exceeded the 160-character schema limit, then a shorter GUI query succeeded.

Targeted `hoi4.source_lookup` returned the SOV scripted-GUI definition at `game:common/scripted_guis/SOV_paranoia_system_scripted_gui.txt:3-84`, revision `965a108d5b17898fd5f43d8b46ff2f95fbac9a4d592940dca393670ddc951222`, and its window at `game:interface/sov_paranoia_system_scripted_gui.gui:20-188`, revision `4660389eb7ec7fade35e8d3c96c6c2f5803e6ec13909da3d9619b6cee51792ec`.

Targeted source lookups for the participant and host category definitions returned the event-owned metadata blocks in `common/decisions/categories/012_africa_gods_categories.txt:10-28` and `:30-48`. The vanilla progress sprite lookup found four linked usages of `GFX_decision_item_progress_good` in the ordinary decision view and an operation overview; its exact GFX definition was read from `interface/countrydecisionview.gfx`.

Additional local reference: offline `Data structures - Hearts of Iron 4 Wiki.md:566`, SHA `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`, explicitly documents strict shortened comparisons.
The stock rail definition is installed `interface/countrypoliticsview.gfx:61-69`, SHA `83d3e5b5b88c373921c732d627fc6adce61f46e8ea1c3c866ef32a99bcc3932f`.
Installed `countryoccupationview.gui:555-564` demonstrates native icon scale/frame consumers, SHA `3080603eaa4f0a3e4789aab322e00b6d57331812b1c237950ef039ca229d2c9f`.
SOV is the decision-category dynamic-frame/context precedent, not a copied circular meter, portrait, or action surface.

The already-recorded absence baseline remains inspect revision `f55eabb8e30c71974320efc8824000d7d6a3a26ceb72e073abd527d0d40d88dd` with0 elements/missing1, and empty render revision `1409e1fcaac6081815a9c3eec678c5513697c4e67cb92833d7d809eaabff277e`, SVG SHA `8e95cdb63290ab8081fd64704cfd34e50d88c23b4f702ca7f29fdcf795c4dade`.
No missing-window retry was repeated.

Skills used: `chaos-redux-scripted-gui`, `chaos-redux-event-assets`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-subagents`, and `imagegen`.
The current bounded scripted-GUI policy was reread on resume; no skill was changed.

Parent integration on 2026-10-09 promotes the unchanged DDS into `gfx/interface/012_africa/` and updates only its sprite texture path.
Its SHA-256 remains `6d3a43efced0dddb4afe9b4209b7f29b192ddfefa1270aa3cbf4684891282de0`.
The archive copy remains provenance, and the final source hash manifest records the updated registry.

Parent boundary review on 2026-10-09 rendered current source after the inclusive-trigger correction and runtime texture promotion.
The exact 20 Strength / 15 Wrath fixture at 1920x1080 and UI scale 1 shows Regional / Watchful, correctly sized 20% / 15% fills, and visible next ticks and labels at 40 / 30.
The parent reviewed `docs/assets/012_africa/gods_public_values_ui/mcp_parent_inclusive_20_15_cropped.png`, SHA-256 `890b9afe709b72dc840874509d801287e35288eb72d257b666ff2c3c74214f71`.
The five byte ranges assembled to 76,444 bytes and matched the emitted artifact hash.
The request, result, diagnostics and source revision `a3a473e7df61cf7d67bd9cc5480ebcec9e9bc34f9c52de2644f50b961dbe64a3` are in `parent_boundary_render_receipt.json` in the same asset workspace.
This closes the missing visual recheck for those two exact boundaries and preserves the remaining full-category, other host/hover and native-game limits.
Hidden threshold elements have zero rendered size, while the visible next markers intentionally overlap their meter rail.
The reviewed crop has no clipped label, missing art or visible geometry defect.

Parent text wiring reads the shared constants in all nine next-threshold labels and both public scale endpoints.
The accepted default text is unchanged, and later threshold tuning cannot leave a different number in these labels.

The parent retains the accepted references, selected final images, requests, source hashes and threshold review in the versioned `012_gods_public_values_ui_2026-10-09_evidence/` archive beside this handoff.
The ignored source workspace remains available while the broader goal is active, and runtime reads only the shipped graphics texture.
