# Event 006 COG overlay cost localisation repair

Date: 2026-08-03

Status: **Implemented and source-checked.**

The four shared COG overlay decision cost strings now read their displayed amounts from `constant:independence_wave_iw_cog_overlay_cost` instead of repeating literal tuning values. The mechanically identical sibling overlay family now reads `constant:independence_wave_iw_region_overlay_cost` in `localisation/english/006_independence_wave_iw156_iw196_iw197_iw204_overlays_l_english.yml`. The base, blocked, and tooltip variants for cabinet, depot, force, and charter costs remain in the same key families and preserve the existing icon order and player-facing wording.

After the independent re-audit identified noncanonical bare equipment icon tokens, the parent normalized both families to the installed canonical sprites: `£GFX_train_texticon`, `£support_equipment_text_icon`, and `£infantry_equipment_text_icon`. No new art was created; this is a reference-name correction only.

## Source surfaces

- `localisation/english/006_independence_wave_iw101_iw102_iw105_cog_overlays_l_english.yml` now uses the centralized command-power, manpower, trains, support-equipment, army-experience, and infantry-equipment fields.
- `localisation/english/006_independence_wave_iw156_iw196_iw197_iw204_overlays_l_english.yml` applies the same constant-driven display contract to the four reusable regional overlay carriers.
- `common/script_constants/006_independence_wave_iw101_iw102_iw105_cog_overlays_constants.txt` remains the sole tuning source.
- `common/decisions/006_independence_wave_iw101_iw102_iw105_cog_overlays_decisions.txt` keeps the existing affordability triggers, payment effects, and custom-cost key references.

## Validation

- The localisation file retains its UTF-8 BOM.
- All twelve cost keys remain present with no accidental `cog_cog` key or duplicate replacement key.
- The constant field names in the twelve strings match the four cost families consumed by the decision triggers and payment effects.
- The sibling regional overlay strings resolve the same cost-family fields from `independence_wave_iw_region_overlay_cost` and retain all twelve consumer keys.
- Both families use only icon tokens with definitions present in the installed vanilla interface references; no bare `£train_equipment`, `£support_equipment`, or `£infantry_equipment` token remains on these cost surfaces.
- No decision, trigger, effect, AI, asset, or gameplay route was otherwise changed.

This is a tuning-drift repair only. It does not promote COG overlay identities, change their origin boundary, add advisor icons, or claim live/UI/save-load evidence. The obsolete pasted flag log is not used as evidence.
