# GFX handoff: Dormant Fallout Mine Generator report art

## Ready asset

- Final DDS: `gfx/event_pictures/fallout_world_end/report_event_fallout_mine_generator.dds`.
- Sprite name: `GFX_report_event_fallout_mine_generator`.
- Target size: `210x176`.
- Registered `.gfx`: `interface/fallout_world_end.gfx` contains the sprite entry in the Fallout report-event registry.
- Texture path in the sprite definition should point to `gfx/event_pictures/fallout_world_end/report_event_fallout_mine_generator.dds`.
- Suggested snippet:

```text
spriteType = {
	name = "GFX_report_event_fallout_mine_generator"
	texturefile = "gfx/event_pictures/fallout_world_end/report_event_fallout_mine_generator.dds"
}
```

## Use notes

The source scene is fictional alternate-history documentary material generated with ImageGen and locally processed through the repository report-event card pipeline.

The approved card has transparent corners and edge space, a restrained tilt, soft shadow, black-and-white treatment with subdued sepia, and no readable text or branding.

Parent-owned follow-up is live presentation review and the dormant Fallout Mine Generator event reference.

No blockers are known for the asset itself.
