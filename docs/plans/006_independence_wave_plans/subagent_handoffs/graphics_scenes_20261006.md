# Event 006 scene-art style repair handoff

- Disposition: implemented.
- Acceptance basis: the parent prompt authorized repairs to the five named existing Event006 scene sprites; the parent explicitly accepted the iw043/iw058 existing-picture style repairs despite their attached state-puzzle scripted GUI, with both picture registrations and GUI attachments preserved.
- Implementation evidence: five regenerated sources, five processed previews, five 32-bit BGRA DDS files, contact sheets, exact prompt lineage, and runtime hashes are recorded in `docs/assets/006_independence_wave/takeover_20261006_scenes/manifest.md`.
- Parent review: the parent reviewed the native comparison and 4x edge/mask sheets and approved runtime installation on 2026-10-06; the parent accepted IW058's lower-light interior without another exposure change.

## Changed runtime assets

- `gfx/event_pictures/006_independence_wave/report_event_006_country_opening.dds` now uses sepia period-photo source art processed through the standard tilted report-card helper to a 210x176 transparent card; its alpha mask is pixel-identical to the existing Event006 report-card mask with 7.93% transparent pixels.
- `gfx/interface/decisions/visual_consistency_repair/pictures/decision_cat_picture_independence_wave_iw043_middle_volga_congress.dds` is now an opaque 114x101 sepia river-and-congress-venue photograph with a thin paper edge and vignette.
- `gfx/interface/decisions/visual_consistency_repair/pictures/decision_cat_picture_independence_wave_iw058_council_of_communities.dds` is now an opaque 114x101 sepia, people-free council chamber photograph with a thin paper edge and vignette.
- `gfx/interface/decisions/visual_consistency_repair/pictures/decision_cat_picture_independence_wave_iw093_asante_compact.dds` is now an opaque 114x101 sepia, people-free courtyard photograph with a thin paper edge and vignette; the selected ImageGen edit removed unexplained crossed foreground rods.
- `gfx/interface/decisions/visual_consistency_repair/pictures/decision_cat_picture_independence_wave_iw098_sokoto_compact.dds` is now an opaque 114x101 sepia Sahelian civic-arch photograph with a thin paper edge and vignette.

## Wiring and review boundary

- Registration names and target `.gfx` files remain `GFX_report_event_006_country_opening` in `interface/006_independence_wave_small_assets.gfx` and the four category sprites in `interface/visual_consistency_repair.gfx`.
- Category `picture` consumers in `common/decisions/categories/006_independence_wave_categories.txt` remain unchanged, including both `scripted_gui = independence_wave_formable_state_puzzle_scripted_gui` attachments for iw043 and iw058.
- All five DDS files round-trip pixel-for-pixel to their processed PNGs, have their verified native canvases, and use the repository's 32-bit BGRA DDS converter.
- The report alpha plane exactly matches existing Event006 assets001-003 and form03; category backgrounds remain fully opaque and no background-removal fallback was used.
- No `.gfx`, `.gui`, gameplay, localisation, or other parent-owned source was edited, and no live-game rendering was performed.
- No simplifications or omissions were made within the authorized five-asset scope.
- The `chaos-redux-event-assets` skill and the official `imagegen` skill were used; no skill was created or changed.
