# GFX handoff: The County Fair Returns

- Final DDS: `gfx/event_pictures/fallout_world_end/report_event_fallout_county_fair_returns.dds`.
- Proposed sprite name: `GFX_report_event_fallout_county_fair_returns`.
- Target `.gfx`: add the sprite to the existing event-picture sprite definition file selected by the main agent.
- Target dimensions: `210x176`.
- Intended consumer: the Fallout event chain’s “The County Fair Returns” report event.
- Ready-to-copy sprite definition shape:

```text
spriteType = {
	name = "GFX_report_event_fallout_county_fair_returns"
	texturefile = "gfx/event_pictures/fallout_world_end/report_event_fallout_county_fair_returns.dds"
}
```

- Wiring note: keep the sprite name and DDS path exactly as above when adding the `.gfx` entry and event-picture reference.
- Processing note: the final texture is already the standard tilted report card with sepia treatment, soft shadow, and transparent corners; do not apply another card frame or resize in `.gfx`.
- Asset status: `handed_off`.
