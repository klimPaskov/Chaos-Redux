# Fallout 775 sprite handoff

The main event file uses `GFX_report_event_fallout_ghost_convoy` for events `chaosx.fallout.775`, `chaosx.fallout.777`, and `chaosx.fallout.779`.

```text
spriteType = {
	name = "GFX_report_event_fallout_ghost_convoy"
	texturefile = "gfx/event_pictures/fallout/report_event_fallout_ghost_convoy.dds"
}
```

The sprite is registered in `interface/fallout_world_end.gfx`. The DDS is 210 x 176 pixels and uses the legacy one-level uncompressed BGRA layout. Hidden AI lanes and cleanup do not display the image. The event does not reference the source or processed PNG at runtime.
