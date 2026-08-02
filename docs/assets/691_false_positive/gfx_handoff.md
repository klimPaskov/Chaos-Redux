# False Positive GFX handoff

The runtime sprite is registered in `interface/fallout_world_end.gfx` as `GFX_report_event_fallout_false_positive`.

The sprite points to `gfx/event_pictures/fallout/report_event_fallout_false_positive.dds`.

Events `chaosx.fallout.691`, `chaosx.fallout.693`, and `chaosx.fallout.695` use `picture = GFX_report_event_fallout_false_positive` for the human opening, delayed result, and appeal callback. Hidden AI events share the chain logic without adding another asset path.

The asset is dedicated to False Positive and does not reuse the First Red Line source, processed PNG, DDS, sprite, or path.
