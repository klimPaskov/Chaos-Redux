# The Grid Vote GFX handoff

Register this exact sprite in `interface/fallout_world_end.gfx`:

```text
spriteType = {
	name = "GFX_report_event_fallout_grid_vote"
	texturefile = "gfx/event_pictures/grid_vote/report_event_fallout_grid_vote.dds"
}
```

The event opening, delayed result, callback, and cleanup presentation use `GFX_report_event_fallout_grid_vote`. The path is dedicated to candidate `824` and is not shared with another Fallout chain.
