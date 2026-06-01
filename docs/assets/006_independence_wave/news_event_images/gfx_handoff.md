# Event 006 News Event Image GFX Handoff

Suggested target `.gfx` file:
- `interface/006_independence_wave_news_event_images.gfx`

Final DDS folder:
- `gfx/event_pictures/`

Sprite names and texture paths:
- `GFX_news_event_independence_wave_partition_week` -> `gfx/event_pictures/news_event_independence_wave_partition_week.dds`
- `GFX_news_event_independence_wave_league` -> `gfx/event_pictures/news_event_independence_wave_league.dds`

Ready-to-copy sprite snippets:

```txt
spriteType = {
	name = "GFX_news_event_independence_wave_partition_week"
	texturefile = "gfx/event_pictures/news_event_independence_wave_partition_week.dds"
}

spriteType = {
	name = "GFX_news_event_independence_wave_league"
	texturefile = "gfx/event_pictures/news_event_independence_wave_league.dds"
}
```

Related usage:
- Event 006 Independence Wave news-image tranche only

Validation notes:
- Both processed PNG previews exist at `397x153`.
- Both final DDS files exist at `397x153`.
- `file` reports both final DDS files as `32-bit color, ARGB8888`.
- No country flag files were created or modified in this tranche.

Uncertainty:
- `partition_week` uses a sourced 1945 geopolitical map rather than a photographed newsroom or telegraph office scene.
- `league` uses a sourced 1930 League of Nations chamber image because it matched the institutional brief more exactly than later, lower-readability conference alternatives.
