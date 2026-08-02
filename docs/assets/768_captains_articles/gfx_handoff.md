# Fallout 768 sprite handoff

The main event file uses `GFX_report_event_fallout_captains_articles` for events `chaosx.fallout.768`, `chaosx.fallout.770`, and `chaosx.fallout.772`.

```text
spriteType = {
	name = "GFX_report_event_fallout_captains_articles"
	texturefile = "gfx/event_pictures/fallout/report_event_fallout_captains_articles.dds"
}
```

The sprite is registered in `interface/fallout_world_end.gfx`. The DDS is 210 x 176 pixels and uses the legacy one-level uncompressed BGRA layout. Hidden AI lanes and cleanup do not display the image. The event does not reference the source or processed PNG at runtime.
