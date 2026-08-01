# Fallout 782 sprite handoff

The main event file uses `GFX_report_event_fallout_harbor_without_city` for events `chaosx.fallout.782`, `chaosx.fallout.784`, and `chaosx.fallout.786`.

```text
spriteType = {
	name = "GFX_report_event_fallout_harbor_without_city"
	texturefile = "gfx/event_pictures/harbor_without_city/report_event_fallout_harbor_without_city.dds"
}
```

The sprite is registered in `interface/fallout_world_end.gfx`. The DDS is 210 x 176 pixels and uses the legacy one-level uncompressed BGRA layout. Hidden AI lanes and cleanup do not display the image. The event does not reference the source or processed PNG at runtime.
