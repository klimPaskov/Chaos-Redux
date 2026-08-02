# Fallout 761 sprite handoff

The main event file uses `GFX_report_event_fallout_mutant_envoy_at_gate` for events `chaosx.fallout.761`, `chaosx.fallout.763`, and `chaosx.fallout.765`.

```text
spriteType = {
    name = "GFX_report_event_fallout_mutant_envoy_at_gate"
    texturefile = "gfx/event_pictures/fallout/report_event_fallout_mutant_envoy_at_gate.dds"
}
```

The sprite is registered in `interface/fallout_world_end.gfx`. The DDS is 210 x 176 pixels and uses the legacy one-level uncompressed BGRA layout. The event does not reference the source or processed PNG at runtime.
