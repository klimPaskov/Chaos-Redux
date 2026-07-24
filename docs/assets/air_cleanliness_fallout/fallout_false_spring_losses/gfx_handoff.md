# Fallout False Spring Losses GFX handoff

Register this dedicated sprite in `interface/fallout_world_end.gfx`:

```text
GFX_report_event_fallout_false_spring_losses
gfx/event_pictures/fallout_world_end/report_event_fallout_false_spring_losses.dds
```

The event picture is used by the opening, delayed result, and second-sowing callback events in `events/fallout_world_end_events.txt` with ids 478, 480, and 482. The hidden AI and cleanup events do not display it.

The source, processed review image, runtime DDS, and manifest remain under `docs/assets/air_cleanliness_fallout/fallout_false_spring_losses/` so later audits can compare the staged copy to the reviewed source.
