# GFX handoff: Spec 66 The Second Dust Bowl

- Final DDS path: `gfx/event_pictures/fallout_world_end/report_event_fallout_second_dust_bowl.dds`
- Proposed sprite name: `GFX_report_event_fallout_second_dust_bowl`
- Suggested target file: `interface/fallout_world_end.gfx`
- Target texture size: `210x176`
- Intended use: static report-event picture for Spec 66, The Second Dust Bowl.
- Suggested sprite definition:

```text
spriteType = {
	name = "GFX_report_event_fallout_second_dust_bowl"
	texturefile = "gfx/event_pictures/fallout_world_end/report_event_fallout_second_dust_bowl.dds"
}
```

- Parent agent should register the sprite in the existing `spriteTypes` block and connect the Spec 66 event/report consumer. Keep the texture path and sprite name stable.
- No localisation key is required by the asset itself. Event title, description, and report wiring remain parent-owned.
- Asset is static; no frame sequence, timing, loop, or audio handoff applies.
- Runtime wiring uncertainty: the exact event id/consumer token is parent-owned and was not changed here.
