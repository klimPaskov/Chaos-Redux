# Handoff: report_event_fallout_mine_generator

The approved static report-event asset is registered for the dormant Mine Generator tranche.

- Final runtime DDS: `gfx/event_pictures/fallout_world_end/report_event_fallout_mine_generator.dds`.
- Package DDS copy: `report_event_fallout_mine_generator.dds`.
- Sprite name: `GFX_report_event_fallout_mine_generator`.
- Target size: `210x176`.
- Registered target `.gfx`: `interface/fallout_world_end.gfx`.
- Texture path: `gfx/event_pictures/fallout_world_end/report_event_fallout_mine_generator.dds`.
- Source mode: Built-in ImageGen generated fictional alternate-history documentary scene.
- Processed treatment: `.agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py` with transparent corners and edge space, deterministic tilt, soft shadow, monochrome, restrained sepia, grain, and paper border.
- Parent follow-up: User-owned runtime presentation review for events `642`, `644`, and `646`.
- Blockers: None in the static package or wiring.

Suggested sprite definition:

```text
spriteType = {
	name = "GFX_report_event_fallout_mine_generator"
	texturefile = "gfx/event_pictures/fallout_world_end/report_event_fallout_mine_generator.dds"
}
```
