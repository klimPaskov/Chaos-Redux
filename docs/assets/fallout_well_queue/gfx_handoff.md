# GFX handoff: Fallout “The Well Queue”

Asset production is complete and ready for main-agent wiring.

- Final DDS: `gfx/event_pictures/fallout_world_end/report_event_fallout_well_queue.dds`
- Native/target size: `210x176` report event image
- Proposed sprite name: `GFX_report_event_fallout_well_queue`
- Suggested target: the existing Chaos Redux event-picture `.gfx` registry. The main agent selects the established file, and this package requires no new `.gfx` file.
- Related event surface: Fallout global-survival family, “The Well Queue” report event
- Source mode: `$imagegen`, fictional alternate-history documentary scene
- Processed treatment: canonical tilted sepia report card with transparent corners and soft shadow

Ready-to-copy sprite definition (adapt formatting to the existing registry):

```hoi4
spriteType = {
    name = "GFX_report_event_fallout_well_queue"
    texturefile = "gfx/event_pictures/fallout_world_end/report_event_fallout_well_queue.dds"
}
```

No `.gfx`, event, localisation, GUI, or gameplay files were edited in this package. The parent/main agent must add the sprite definition and bind it to the exact event id. No blocker or fallback asset exists.
