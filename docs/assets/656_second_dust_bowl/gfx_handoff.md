# GFX handoff: Spec 66 The Second Dust Bowl

- Final DDS path: `gfx/event_pictures/fallout_world_end/report_event_fallout_second_dust_bowl.dds`
- Runtime sprite name: `GFX_report_event_fallout_second_dust_bowl`
- Runtime registration: present in `interface/fallout_world_end.gfx`
- Target texture size: `210x176`
- Intended use: static report-event picture for Spec 66, The Second Dust Bowl.
- Runtime sprite definition:

```text
spriteType = {
	name = "GFX_report_event_fallout_second_dust_bowl"
	texturefile = "gfx/event_pictures/fallout_world_end/report_event_fallout_second_dust_bowl.dds"
}
```

- The sprite is registered in the existing `spriteTypes` block and consumed by events `chaosx.fallout.656`, `chaosx.fallout.658`, and `chaosx.fallout.660`. Keep the texture path and sprite name stable.
- No localisation key is required by the asset itself. Event title and description localisation is in `localisation/english/fallout_world_end_second_dust_bowl_l_english.yml`.
- Asset is static. No frame sequence, timing, loop, or audio handoff applies.
- Live presentation and report-card rendering remain unverified because HOI4 was not launched.
