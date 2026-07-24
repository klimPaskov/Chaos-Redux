# Japan Biological Campaign Icon Handoff

Status: `handed_off`; parent `.gfx` wiring remains pending by design.

## Runtime asset

- Asset type: decision-category icon.
- Native target: `52x40`.
- Final DDS: `gfx/interface/decisions/biowarfare/japan_china/decision_category_japan_biological_campaign.dds`.
- Sprite identifier: `GFX_decision_category_japan_biological_campaign`.
- Parent-owned `.gfx` file: `interface/biological_warfare.gfx`.
- Gameplay/localisation/spec files: not edited in this handoff.

Suggested copy-ready definition for the parent-owned `.gfx` file:

```text
spriteType = {
	name = GFX_decision_category_japan_biological_campaign
	texturefile = "gfx/interface/decisions/biowarfare/japan_china/decision_category_japan_biological_campaign.dds"
}
```

The parent agent should preserve the exact sprite name, texture path, and 52x40 target when wiring the definition.

## Source evidence

- Generated source master: `docs/assets/chaos_warfare_cbrn/japan_biological_campaign/source_png/japan_biological_campaign_icon_source_master.png`.
- Alpha source: `docs/assets/chaos_warfare_cbrn/japan_biological_campaign/source_png/japan_biological_campaign_icon_source_alpha.png`.
- Generation prompt: `docs/assets/chaos_warfare_cbrn/japan_biological_campaign/prompts/japan_biological_campaign_icon_prompt.md`.
- Processed preview: `docs/assets/chaos_warfare_cbrn/japan_biological_campaign/processed_png/decision_category_japan_biological_campaign_52x40.png`.
- Review contact sheet: `docs/assets/chaos_warfare_cbrn/japan_biological_campaign/contact_sheets/decision_category_japan_biological_campaign_contact_sheet.png`.
- Manifest: `docs/assets/chaos_warfare_cbrn/japan_biological_campaign/manifest.md`.
- Processing and validation notes: `docs/assets/chaos_warfare_cbrn/japan_biological_campaign/notes/transparent_processing_verification.md`.

The source package was already present and visually usable, so it was preserved rather than regenerated. The prompt records `$imagegen` built-in generation and the intended chroma-key alpha workflow; the original master, extracted alpha source, processed preview, contact sheet, and final DDS remain distinct files.

## Review result

The alpha source and processed preview have real transparency, transparent corners, no opaque chroma-green residue, no white matte, no fake checkerboard, and no square background. The icon remains readable as a biological field-medical flask crossed by a dispatch scroll with a subdued red disc at the native decision-category scale.

The canonical reference family was reviewed from the single allowed root at `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/decision_categories/`. Its contact sheet was inspected first, followed by individual decision-category references. Those references were review-only and were not copied or used as final art.

DDS validation passed for exact 52x40 dimensions, 8448-byte legacy uncompressed BGRA layout, required pixel-format masks, texture caps, and alpha range `0..255`.

## Parent action

Wire the sprite definition in `interface/biological_warfare.gfx` and connect the existing parent gameplay reference to `GFX_decision_category_japan_biological_campaign`. No fallback, placeholder, cross-type substitute, or military-raids asset was used.
