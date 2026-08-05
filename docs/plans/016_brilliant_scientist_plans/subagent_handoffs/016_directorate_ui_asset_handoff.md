# Event 016 Directorate UI asset handoff

Status: superseded in part on 2026-08-05. The state-card, meter, control, portrait-frame, and animation evidence below remains authoritative, but the original 700-pixel shell and refresh-control contract does not. `016_directorate_background_refresh_handoff.md` owns the replacement `500x620` full panel and `500x58` compact header, while the revised GUI removes the refresh control and fits vanilla's 502-pixel decision grid.

## Runtime files and exact dimensions

Every path below exists as a 32-bit uncompressed BGRA DDS under `gfx/interface/016_brilliant_scientist/directorate/`. The authoritative machine manifest is `docs/assets/016_brilliant_scientist/directorate_ui/manifest.json`.

### Directorate shell and profiles

| Runtime path | Size |
| --- | --- |
| `decision_category_directorate.dds` | 52x40 |
| `directorate_background.dds` | 700x500 |
| `directorate_compact_header.dds` | 700x58 |
| `profile_frame_human.dds` | 168x218 |
| `profile_frame_secured.dds` | 168x218 |
| `profile_frame_sovereign.dds` | 168x218 |

### Meters

All sixteen meter paths are 112x34: `meter_mandate_low.dds`, `meter_mandate_moderate.dds`, `meter_mandate_high.dds`, `meter_mandate_extreme.dds`, `meter_dependence_low.dds`, `meter_dependence_moderate.dds`, `meter_dependence_high.dds`, `meter_dependence_extreme.dds`, `meter_exposure_low.dds`, `meter_exposure_moderate.dds`, `meter_exposure_high.dds`, `meter_exposure_extreme.dds`, `meter_capacity_low.dds`, `meter_capacity_moderate.dds`, `meter_capacity_high.dds`, and `meter_capacity_extreme.dds`.

### Control status, project, facility, contact, sovereignty, and singularity states

All five `control_status_{unassessed,secure,contested,compromised,lost}.dds` paths are 240x34.

All six `project_card_{locked,theory,prototype,deployment,weaponized,damaged}.dds` paths are 204x222.

All five `facility_card_{normal,hardened,infiltrated,damaged,lost}.dds` paths are 226x222.

All five `foreign_contact_{neutral,offer,threat,operation,resolved}.dds` paths are 226x222.

All four `sovereignty_panel_{hidden,demand,countdown,confrontation}.dds` paths are 472x222.

All six `singularity_indicator_{rumored,theory,prototype,construction,delivery,armed}.dds` paths are 104x96.

### Four-frame controls

The existing `effectFile = "gfx/FX/buttonstate.lua"` entries consume horizontal four-frame sheets in normal, hover, pressed, disabled order.

| Runtime path | Full sheet | Per frame |
| --- | ---: | ---: |
| `directorate_tab_button.dds` | 368x30 | 92x30 |
| `directorate_close_control.dds` | 144x36 | 36x36 |
| `directorate_open_control.dds` | 144x36 | 36x36 |
| `directorate_refresh_control.dds` | 496x34 | 124x34 |
| `directorate_animation_control.dds` | 496x34 | 124x34 |

### Animated loops and static fallbacks

Each animated registration retains a separately registered static fallback. The static paths are `control_warning_static.dds` (224x32), `active_project_marker_static.dds` (196x214), and `singularity_armed_static.dds` (116x108).

The three animated sheet paths are `control_warning_sheet.dds` (1792x32, 8 frames at 5 fps), `active_project_marker_sheet.dds` (1568x214, 8 frames at 5 fps), and `singularity_armed_sheet.dds` (1160x108, 10 frames at 4 fps). Their frame widths are 224, 196, and 116 respectively. The existing `.gfx` registrations also retain the contract pause values: 0.35 seconds, 0.25 seconds, and 0.45 seconds.

## Source and processing package

Generated masters, generated storyboard sheets, button-state source variants, and prompt records are under `docs/assets/016_brilliant_scientist/directorate_ui/source_masters/` and `docs/assets/016_brilliant_scientist/directorate_ui/prompts/`. Target-size static PNGs are under `processed_png/`; packed PNG sheets are under `sheets/`; individual animation frames are under `source_frames/` and `processed_frames/`; static fallback PNGs are under `static_fallbacks/`; GIF previews are under `previews/`; and DDS-decoded PNGs are under `decoded_dds/`.

The image-generation provenance record is `prompts/provenance.json`, and the prompt summary is `prompts/directorate_ui_prompts.md`. The source masters are generated art and do not borrow vanilla pixels. The canonical vanilla decision-category contact sheet was inspected only as style and footprint reference.

The warning, active-project, and singularity animations use independent generated storyboard states sliced into preserved source frames. No still-image offset, scaling, blur, glow pulse, rotation, warp, recolour, or shape-overlay trick is used as the final animation.

## Existing consumers

The parent agent should keep the existing consumers unchanged: `interface/016_brilliant_scientist_directorate.gfx` registers all 64 textures and `interface/016_brilliant_scientist_directorate.gui` consumes the shell, profile, meter, control, project, facility, contact, sovereignty, singularity, and animation sprites. The current GUI contract assumes a 700x500 main panel, a 700x58 compact header, 156x210 portrait aperture inside the 168x218 profile frame, five tab slots at the existing pitch, and 480x230 panel surfaces. This handoff does not alter those files.

## Validation evidence

`validation/row_validation.tsv` was generated by parsing every `texturefile` in `interface/016_brilliant_scientist_directorate.gfx`, opening each DDS header, checking the exact contract dimensions and 32-bit uncompressed payload length, measuring alpha bounds, and decoding the BGRA payload to PNG. It reports 64 GFX rows, 64 runtime DDS files, and 64 rows with status `OK`.

The decoded contact sheet is `contact_sheets/directorate_decoded_runtime_contact.png`. Processed static and per-animation contact sheets are in `contact_sheets/`, and the three GIF previews are in `previews/`. The runtime directory contains exactly 64 DDS files after removing five unreferenced button-sheet conversion duplicates; the five canonical button DDS paths remain intact.

## Parent visual review checklist

- Confirm the shell and profile frames leave the GUI's text and portrait apertures clear.
- Confirm all 16 meters, five control statuses, six projects, five facilities, five contacts, four sovereignty panels, and six singularity indicators read as distinct semantic states at native size.
- Confirm button sheets slice cleanly into four states in the existing `buttonstate.lua` order.
- Confirm animation sheets read as eight/eight/ten real state frames and that static fallbacks are acceptable when animation is unavailable.
- Confirm the generated art's blue-black enamel, oxidized brass, paper-blue instrumentation, and low-contrast drafting-grid direction matches the rest of Event 016.
- Confirm no text, numerals, flags, signatures, labels, watermarks, logos, or modern electronics appear in the source or runtime art.

## Simplifications, omissions, and blockers

None. All 64 requested runtime paths have source PNG provenance, exact processed PNGs, final DDS files, decoded-runtime evidence, manifest entries, and this handoff. No fallback was substituted for a requested asset; the three static fallback files are the explicitly required companions to the animated registrations.

## Parent review disposition

Accepted on 2026-07-24 after visual inspection of the decoded-runtime contact sheet, the full static processed contact sheet, and all three source and processed animation contact sheets. The shell, meters, state cards, controls, and terminal indicators remain legible at their registered footprints; the four-state button sheets separate cleanly; and the warning, active-project, and armed-Singularity loops contain genuinely distinct illustrated frames rather than transform-only motion. The 64-of-64 decoded DDS validation and exact consumer-path match are accepted as the static asset evidence for this tranche. Live in-game rendering remains part of final acceptance and is not claimed here.
