# Event 006 ASSET-040–043 frame-animation audit, 2026-09-13

Disposition: needs_user_review for source-transparency provenance and live animation/fallback behavior; no asset repair selected.

## Scope and outcome

This bounded audit covered only ASSET-040 recognition seal, ASSET-041 dependency warning, ASSET-042 league charter activation, and ASSET-043 formable eligibility seal.

No gameplay, localisation, GUI layout, `.gfx`, `.gui`, scripted-GUI, or runtime asset file was changed.

The four packages pass the mechanical image and DDS checks, and every requested state is represented by a distinct authored source frame rather than a transform-only derivative.

The only worktree change from this subtask is this handoff; no staging or commit was performed.

## Exact package files reviewed

For each family, the audit opened the brief, frame plan, source prompts, all `source_frames/*_source.png`, all `notes/_chroma_removed/*.png`, all `processed_frames/*.png`, the family sheet PNG, static PNG, contact sheet, and GIF preview.

| Asset | Source states and exact review files | Sheet and fallback |
| --- | --- | --- |
| ASSET-040 | `docs/assets/006_independence_wave/animations/independence_wave_recognition_seal/source_frames/{hidden,weak,rising,strong,entrenched}_source.png`; matching `notes/_chroma_removed/`, `processed_frames/`, `previews/independence_wave_recognition_seal_{contact.png,preview.gif}` | `sheets/independence_wave_recognition_seal_sheet.png`; `independence_wave_recognition_seal_static.png` |
| ASSET-041 | `docs/assets/006_independence_wave/animations/independence_wave_dependency_warning/source_frames/{calm,watch,danger}_source.png`; matching `notes/_chroma_removed/`, `processed_frames/`, `previews/independence_wave_dependency_warning_{contact.png,preview.gif}` | `sheets/independence_wave_dependency_warning_sheet.png`; `independence_wave_dependency_warning_static.png` |
| ASSET-042 | `docs/assets/006_independence_wave/animations/independence_wave_league_charter_activation/source_frames/{rest,drafting,vote,activated}_source.png`; matching `notes/_chroma_removed/`, `processed_frames/`, `previews/independence_wave_league_charter_activation_{contact.png,preview.gif}` | `sheets/independence_wave_league_charter_activation_sheet.png`; `independence_wave_league_charter_activation_static.png` |
| ASSET-043 | `docs/assets/006_independence_wave/animations/independence_wave_formable_eligibility_seal/source_frames/{hidden,discovered,eligible,proclaimed}_source.png`; matching `notes/_chroma_removed/`, `processed_frames/`, `previews/independence_wave_formable_eligibility_seal_{contact.png,preview.gif}` | `sheets/independence_wave_formable_eligibility_seal_sheet.png`; `independence_wave_formable_eligibility_seal_static.png` |

The package metadata reviewed was `docs/assets/006_independence_wave/animations/manifest.md`, `gfx_handoff.md`, and `animation_build_report.json`.

The runtime DDS files reviewed were `gfx/interface/006_independence_wave/animations/independence_wave_{recognition_seal,dependency_warning,league_charter_activation,formable_eligibility_seal}_{sheet,static}.dds`.

The read-only wiring context reviewed was `interface/006_independence_wave.gfx` and `interface/006_independence_wave.gui`.

## Frame and visual review

The state order, subject identity, and visual progression match the four frame plans: recognition `hidden → weak → rising → strong → entrenched`; dependency `calm → watch → danger`; league `rest → drafting → vote → activated`; and formable `hidden → discovered → eligible → proclaimed`.

All sixteen processed frames were reviewed in native 64x64 and enlarged contact/montage views, and all four decoded DDS sheets and four decoded static DDS fallbacks were opened enlarged.

The visual states are distinct and readable, with no fake checkerboard, clipped subject, missing frame, transform-only motion, or obvious matte halo at native size.

All source masters are 1254x1254 opaque RGB images on the documented flat green chroma-key background.

All chroma-removed intermediates are 1254x1254 RGBA, all processed frames are 64x64 RGBA, and all processed frame corners are transparent.

Alpha bounds stay inside the canvas and remain centered: recognition bounds span x=3–61 and y=3–61 with weighted centers x=30.99–31.55 and y=31.47–31.54; dependency bounds span x=9–54 (danger x=11–53) and y=3–61 with centers x=30.98–31.50 and y=30.51–30.82; league bounds span x=3–61 and y=3–61 (activated ymax=60) with centers x=31.07–31.53 and y=31.08–32.99; formable bounds span x=3–61 and y=3–61 with centers x=30.98–31.57 and y=31.46–32.24.

The league drafting y-center offset is attributable to the intentionally tall rolled parchment and does not produce visible frame drift.

The GIF previews decode as 64x64 indexed images with frame counts 5/3/4/4, 200 ms per frame, and loop=0.

Indexed GIF previews show palette-fringe pixels when composited onto a dark inspection background at 4x; this is a review-preview quantization artifact and is not present as an opaque background in the PNG/DDS runtime assets.

## Sheet, static, and DDS evidence

Every sheet cell is pixel-equal to its matching processed frame in manifest order, and every static PNG/DDS is pixel-equal to the family’s first processed frame.

The sheets are exactly 320x64, 192x64, 256x64, and 256x64 for ASSET-040 through ASSET-043 respectively.

The static DDS files are each 64x64 and 16,512 bytes; the sheet DDS files are 320x64 and 82,048 bytes, 192x64 and 49,280 bytes, and 256x64 and 65,664 bytes for the applicable families.

Manual DDS decoding confirmed valid legacy uncompressed BGRA headers with 32-bit pixels, alpha mask `0xFF000000`, and exact expected file lengths.

Decoded runtime DDS sheets are pixel-equal to all corresponding processed PNG cells, including alpha, and decoded runtime static DDS files are pixel-equal to their first processed PNG.

`animation_build_report.json` integrity is current: 56 listed files, zero missing, zero bad hashes, report SHA-256 `26d2079766e05ac95fa342c0edc6b190820bd9e48015d6319fc63064037203c4`.

No exact key-green pixels remain in processed frames.

A heuristic finds a few green-dominant low-alpha edge samples around the league activated cyan/gold halo and a few green-dominant pixels in the formable proclaimed painted shield/ribbons, but native-size and enlarged black/white background review found no actionable green matte or edge spill.

## Reference and engine evidence

The matching canonical reference root was used exclusively for visual-reference inspection: `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/interface/README.md`, `interface/vanilla/_review_contact_sheet.png`, `interface/chaos_redux/chaos_meter/chaos_meter_deaths_window.png`, and `interface/vanilla/design_and_organization/unitleader_trait_tree_window.png`.

The offline `Graphical asset modding`, `Interface modding`, and `Scripted GUI modding` wiki pages and installed scripted-GUI documentation were reviewed, along with vanilla `frameAnimatedSpriteType` precedents in `interface/alerts.gfx`, `countryconstructionsview.gfx`, `nationalfocusview.gfx`, `landcombat.gfx`, and `unitview.gfx`.

The vanilla pattern confirms horizontal sheet plus `noOfFrames`, FPS, looping, `play_on_show`, `pause_on_loop`, and optional transparency behavior; the package follows that pattern without adding a guessed fallback field.

## MCP GUI evidence and blockers

Read-only `hoi4_gui_inspect` succeeded for `independence_wave_status_window` with scenario id `normal`, 1920x1080, uiScale 1, and generated scenarios disabled.

The inspect workspace was `mod_chaos_redux_ea3b2d67c2c0`, source revision `cddd27b9b2c3db9d16752e6b1678cbebf51f780dd9cd5fb3c6eee0eb4c2283fb`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/71f3b640dea2c637ce05f0d930ed7c104a0b0fa23ec2418fac4e28ed96d48901/423987679749c31e9623b9d90c072f25fa556214aeed20ce875c3f57b8a115c2/gui-inspect.cddd27b9b2c3db9d.json`.

The inspect graph parsed without blocking diagnostics, but the offline inspector reports `GUI_ANIMATION_STATIC_FALLBACK_MISSING` for all four `*_animated` sprites even though separate `*_static` sprite definitions exist in `interface/006_independence_wave.gfx`.

The same inspect reports `GUI_SPRITE_RENDER_PARTIAL` because `gfx/FX/buttonstate_blendframes.lua` is retained in the source graph but not executed by the offline renderer.

Read-only `hoi4_gui_render` also returned `GUI_RENDERED` for the normal scenario at 1920x1080 with 27 artifacts, but its `offlineRepresentation` is true and therefore it does not prove live blendframe playback, dynamic visibility, or static-fallback resolution in the game engine.

Live game playback and user-visible toggle validation remain parent/user-owned and were not performed.

## Source-alpha provenance blocker

The current source masters are opaque chroma-key RGB rather than native-transparent ImageGen outputs.

The source notes document an installed `remove_chroma_key.py` fallback with soft matte/despill, but no such helper exists in the current repository file inventory, so the exact fallback settings and initial native-transparency failure cannot be independently reproduced from this checkout.

The untouched opaque source masters, transparent processed frames, and runtime DDS outputs were preserved; no re-generation or unverified edge repair was attempted because no missing visual state or concrete runtime pixel defect was found.

Parent review is required to decide whether the existing documented chroma-key lineage is accepted or whether the four families must be re-authored through the approved native-transparent ImageGen route.

## Per-asset disposition

ASSET-040, ASSET-041, ASSET-042, and ASSET-043 are mechanically complete and visually reviewable, with source, processed frames, sheet PNG/DDS, static PNG/DDS, GIF preview, contact sheet, manifest/build report, and GFX handoff present.

All four remain `needs_user_review` for the source-alpha provenance blocker and the unresolved live engine diagnostics above.

No concrete frame boundary, alpha, normalization, conversion, path, sheet-size, or frame-order repair was justified.

No ImageGen call was needed because all required real visual states exist and no frame is missing.

Skills used for this bounded review: `chaos-redux-event-assets`, `chaos-redux-frame-animation`, `chaos-redux-subagents`, and `chaos-redux-scripted-gui`.

No skill was modified.
