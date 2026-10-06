# Shared ChaosX super-event GFX handoff

`GFX_super_event_azl` keeps its existing sprite and texture path; only the text-free scene replaces the current poster.

Add or repoint the terminal sprite in `interface/chaosx_super_events.gfx` to the unique terminal texture below. Keep the main-stage `GFX_super_event_final_silence` on its current texture.

```text
name = GFX_super_event_final_silence_terminal
texturefile = gfx/super_events/003_holy_realm/super_event_the_final_silence_terminal.dds
```

The terminal stage is active at `super_event_visible=9`; the main image remains the stage at `super_event_visible=8`.
