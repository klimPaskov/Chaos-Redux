# Event 016 Directorate UI asset contract

## Status

This contract resolves the dimension and packing questions recorded in `directorate_ui_blocker.md`.

It is binding for the Event 016 Directorate art tranche unless the parent review finds a concrete clipping or click-region defect.

The live consumer is `interface/016_brilliant_scientist_directorate.gui`, the sprite registry is `interface/016_brilliant_scientist_directorate.gfx`, and the scripted consumer is `common/scripted_guis/016_brilliant_scientist_directorate_scripted_gui.txt`.

## Reference evidence

- The Directorate container and full panel are `700x500`.
- The compact panel is `700x58`.
- The registered Kruger leader portrait is `156x210` and sits inside the profile frame with a six-pixel top and side inset.
- The five tabs begin at x positions `202`, `299`, `396`, `493`, and `590`, leaving a `97`-pixel pitch.
- The project, facility, foreign, and sovereignty panels are `480x230`.
- The existing Event 15 Commonwealth Ledger uses a final `700x500` DDS for its `700x500` GUI and a separate full-width header plate.
- HOI4 decision-category icons use the standard `52x40` surface.

The attempted `hoi4.gui_inspect` render found the window after correcting its name to `kruger_directorate_container`, but the repository-wide scan exceeded the tool byte limit before it could render the window.

## Static texture dimensions

| Family | Files | Final dimensions |
| --- | --- | ---: |
| Decision category | `decision_category_directorate.dds` | `52x40` |
| Full background | `directorate_background.dds` | `700x500` |
| Compact header | `directorate_compact_header.dds` | `700x58` |
| Profile frames | `profile_frame_human.dds`, `profile_frame_secured.dds`, `profile_frame_sovereign.dds` | `168x218` |
| Meter states | all `meter_mandate_*`, `meter_dependence_*`, `meter_exposure_*`, and `meter_capacity_*` files | `112x34` |
| Government Control states | all `control_status_*` files | `240x34` |
| Project cards | all `project_card_*` files | `204x222` |
| Facility cards | all `facility_card_*` files | `226x222` |
| Foreign-contact cards | all `foreign_contact_*` files | `226x222` |
| Sovereignty panels | all `sovereignty_panel_*` files | `472x222` |
| Singularity indicators | all `singularity_indicator_*` files | `104x96` |

Every family must share exact geometry across its state variants.

State changes must alter symbols, damage, seals, mechanical details, or scene content where applicable; recolouring one unchanged master is not sufficient.

## Four-state button sheets

All button sheets pack frames horizontally in this order:

1. normal;
2. hover;
3. pressed;
4. disabled.

| File | Per-frame dimensions | Final sheet dimensions |
| --- | ---: | ---: |
| `directorate_tab_button.dds` | `92x30` | `368x30` |
| `directorate_close_control.dds` | `36x36` | `144x36` |
| `directorate_open_control.dds` | `36x36` | `144x36` |
| `directorate_refresh_control.dds` | `124x34` | `496x34` |
| `directorate_animation_control.dds` | `124x34` | `496x34` |

The normal state must remain readable beneath the GUI-provided button text.

The disabled state must remain visually distinct without relying only on alpha reduction.

## Frame-animation contracts

All animation sheets pack independent frames horizontally.

The static fallback uses the same dimensions as one animation frame.

| Package | Frames | Per-frame dimensions | Final sheet dimensions | Static fallback |
| --- | ---: | ---: | ---: | --- |
| Government Control warning | 8 | `224x32` | `1792x32` | `control_warning_static.dds` |
| Active-project marker | 8 | `196x214` | `1568x214` | `active_project_marker_static.dds` |
| Armed Singularity | 10 | `116x108` | `1160x108` | `singularity_armed_static.dds` |

The Government Control warning occupies the area beginning at GUI position `448,120`.

The active-project marker is a full-card overlay inside the `204x222` project card, leaving a four-pixel inset.

The armed-Singularity animation is an overlay around the `104x96` static indicator, leaving a six-pixel inset relationship.

Each animation must follow `chaos-redux-frame-animation`: separately authored source frames, static fallback, processed frames, final sheet, contact sheet, preview GIF, timing record, and GFX or GUI handoff.

Transform-only, filter-only, or single-still animation is forbidden.

## Art direction

Use a restrained 1930s–40s scientific-directorate dossier language: blue-black enamel, oxidized brass, paper-blue instrumentation, engraved laboratory geometry, and low-contrast drafting grids.

The profile frames should progress from human institutional legitimacy through hardened security to scientific sovereignty.

Mandate, Dependence, Exposure, and Capacity must remain visually distinguishable even without their labels.

Government Control states should progress from blank assessment to secured seal, contested paperwork, compromised breach, and institutional loss.

Project, facility, contact, sovereignty, and Singularity states should communicate a changed material condition rather than a generic colour tier.

Do not place generated text, numerals, flags, signatures, or labels inside the art.

## Production and acceptance

The producer must create all 64 registered texture paths, source and processed PNGs, final DDS files, prompt or provenance records, source and decoded-DDS contact sheets, animation previews, and a row-level validation table.

Parent review must verify exact dimensions, alpha treatment, button slicing, animation frame count, static fallbacks, visual distinction, and consumption by every registered sprite.

No generic, vanilla, borrowed, or placeholder texture is authorized.
