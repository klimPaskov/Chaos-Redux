# GFX handoff: Fallout Triage Wall report image

## Final asset

- Final DDS: `gfx/event_pictures/fallout_triage_wall/fallout_triage_wall_report.dds`
- Dimensions: `210x176`
- Proposed sprite name: `GFX_report_event_fallout_triage_wall`
- Suggested target `.gfx`: the existing event-picture sprite registry used by the mod
- Related event family: The Triage Wall
- Related event id: `chaosx.fallout.175` through `chaosx.fallout.187`
- Localisation key: `chaosx.fallout.175.t`, result family `chaosx.fallout.177` through `chaosx.fallout.185`

## Ready-to-copy sprite definition

```text
spriteType = {
	name = GFX_report_event_fallout_triage_wall
	texturefile = "gfx/event_pictures/fallout_triage_wall/fallout_triage_wall_report.dds"
}
```

The sprite is registered in `interface/fallout_world_end.gfx`.

## Source and preview evidence

- Source PNG: `docs/assets/fallout_triage_wall/source_png/fallout_triage_wall_report_source.png`
- Processed preview: `docs/assets/fallout_triage_wall/processed_png/fallout_triage_wall_report.png`
- Generation prompt: `docs/assets/fallout_triage_wall/prompts/fallout_triage_wall_report_prompt.txt`
- Manifest: `docs/assets/fallout_triage_wall/manifest.md`

## Use notes

The image is an original generated Fallout medical triage scene. It uses a salvaged allocation wall rather than a patient queue, battlefield, zombie attack, or generic wasteland panorama. The final report card has transparent corners and sepia monochrome treatment. No existing Fallout or zombie ids, assets, or paths were reused.

## Uncertainty and review

- The event id, localisation family, and exact `.gfx` target are now recorded above.
- Asset status is `wired`. Independent visual review remains a release gate.
