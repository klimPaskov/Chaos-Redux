# County Fair Returns report-event art handoff

Status: handed off for parent wiring.

## Runtime asset

- Final DDS: `gfx/event_pictures/fallout_world_end/report_event_fallout_county_fair_returns.dds`
- Dimensions: `210x176`
- DDS format: one-level, uncompressed 32-bit BGRA with transparent card corners; validated header, dimensions, exact byte length, and alpha range.
- Proposed sprite name: `GFX_report_event_fallout_county_fair_returns`
- Intended consumer: the ordinary Fallout report popup for The County Fair Returns, a cold but hopeful North American rural recovery fair.
- Source mode: generated fictional alternate-history report art via the built-in imagegen workflow.
- Source PNG: `docs/assets/air_cleanliness_fallout/fallout_county_fair_returns/source_png/report_event_fallout_county_fair_returns_source.png`
- Processed preview: `docs/assets/air_cleanliness_fallout/fallout_county_fair_returns/processed_png/report_event_fallout_county_fair_returns.png`
- Prompt: `docs/assets/air_cleanliness_fallout/fallout_county_fair_returns/prompts/report_event_fallout_county_fair_returns_imagegen.txt`
- Hashes: `docs/assets/air_cleanliness_fallout/fallout_county_fair_returns/hashes.sha256`
- Retained alternate evidence: `docs/assets/air_cleanliness_fallout/fallout_county_fair_returns/source_png/fallout_county_fair_returns_source.png` and `processed_png/fallout_county_fair_returns_processed.png` with the existing contact sheet; these are not the selected runtime candidate.

## Visual fit

The source is an original people-free documentary-style rural fairground: repaired timber barn, salvaged sheet-metal livestock pens, seed jars, preserved food, hand tools, frost-browned fields, guarded gate, and blank notice/remembrance boards. The processed card applies the canonical Fallout report treatment (sepia, grain, subtle tilt, paper edge, soft shadow, transparent corners). It contains no real people, real flags, readable text, logos, zombies, corpses, radioactive monsters, modern props, amusement rides, military parade, or super-event drama.

## Parent-owned `.gfx` wiring

Add the sprite to the existing report-event `.gfx` registry used by the Fallout report pictures. A ready-to-copy texture reference is:

```text
spriteType = {
	name = "GFX_report_event_fallout_county_fair_returns"
	texturefile = "gfx/event_pictures/fallout_world_end/report_event_fallout_county_fair_returns.dds"
}
```

The exact target `.gfx` filename is intentionally left to the parent’s existing report-event registry lookup; this asset-only subagent did not create or edit a new GFX file. Keep the sprite name and DDS path stable when the provisional event-id collision rescan is completed.

## Scope and risks

- No gameplay, event, localisation, spreadsheet, or `.gfx` files were edited here.
- The addendum’s `565`/`FALLOUT-565` identity is provisional and explicitly unreserved; remap the entire chain if the parent collision rescan finds a conflict.
- This is a single static asset, so no animation frame plan or contact sheet is required.
