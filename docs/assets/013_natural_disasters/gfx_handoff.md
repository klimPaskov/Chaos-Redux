# GFX Handoff: Event 013 Natural Disasters Event Art

Event image target `.gfx` file:
- `interface/013_natural_disasters.gfx`

Super-event target `.gfx` file:
- `interface/chaosx_super_events.gfx`

## Report event sprites

```txt
spriteType = { name = "GFX_report_event_natural_disaster_baseline" texturefile = "gfx/event_pictures/013_natural_disasters/report_event_natural_disaster_baseline.dds" }
spriteType = { name = "GFX_report_event_natural_disaster_warning" texturefile = "gfx/event_pictures/013_natural_disasters/report_event_natural_disaster_warning.dds" }
spriteType = { name = "GFX_report_event_natural_disaster_impact" texturefile = "gfx/event_pictures/013_natural_disasters/report_event_natural_disaster_impact.dds" }
spriteType = { name = "GFX_report_event_natural_disaster_recovery" texturefile = "gfx/event_pictures/013_natural_disasters/report_event_natural_disaster_recovery.dds" }
spriteType = { name = "GFX_report_event_natural_disaster_earthquake" texturefile = "gfx/event_pictures/013_natural_disasters/report_event_natural_disaster_earthquake.dds" }
spriteType = { name = "GFX_report_event_natural_disaster_flood" texturefile = "gfx/event_pictures/013_natural_disasters/report_event_natural_disaster_flood.dds" }
spriteType = { name = "GFX_report_event_natural_disaster_storm" texturefile = "gfx/event_pictures/013_natural_disasters/report_event_natural_disaster_storm.dds" }
spriteType = { name = "GFX_report_event_natural_disaster_drought" texturefile = "gfx/event_pictures/013_natural_disasters/report_event_natural_disaster_drought.dds" }
spriteType = { name = "GFX_report_event_natural_disaster_wildfire" texturefile = "gfx/event_pictures/013_natural_disasters/report_event_natural_disaster_wildfire.dds" }
spriteType = { name = "GFX_report_event_natural_disaster_landslide" texturefile = "gfx/event_pictures/013_natural_disasters/report_event_natural_disaster_landslide.dds" }
spriteType = { name = "GFX_report_event_natural_disaster_volcano" texturefile = "gfx/event_pictures/013_natural_disasters/report_event_natural_disaster_volcano.dds" }
spriteType = { name = "GFX_report_event_natural_disaster_tsunami" texturefile = "gfx/event_pictures/013_natural_disasters/report_event_natural_disaster_tsunami.dds" }
spriteType = { name = "GFX_report_event_natural_disaster_meteor" texturefile = "gfx/event_pictures/013_natural_disasters/report_event_natural_disaster_meteor.dds" }
```

## News event sprites

```txt
spriteType = { name = "GFX_news_event_regional_disaster_system" texturefile = "gfx/event_pictures/013_natural_disasters/news_event_regional_disaster_system.dds" }
spriteType = { name = "GFX_news_event_disaster_chains" texturefile = "gfx/event_pictures/013_natural_disasters/news_event_disaster_chains.dds" }
spriteType = { name = "GFX_news_event_abnormal_disaster_age" texturefile = "gfx/event_pictures/013_natural_disasters/news_event_abnormal_disaster_age.dds" }
```

## Super-event sprite

```txt
spriteType = { name = "GFX_super_event_natural_disasters_abnormal_disaster_age" texturefile = "gfx/super_events/super_event_natural_disasters_abnormal_disaster_age.dds" }
```

## State-modifier idea sprites

```txt
spriteType = { name = "GFX_idea_recent_earthquake_damage" texturefile = "gfx/interface/ideas/natural_disasters/idea_recent_earthquake_damage.dds" }
spriteType = { name = "GFX_idea_flooded_transport_belt" texturefile = "gfx/interface/ideas/natural_disasters/idea_flooded_transport_belt.dds" }
spriteType = { name = "GFX_idea_crop_failure_pressure" texturefile = "gfx/interface/ideas/natural_disasters/idea_crop_failure_pressure.dds" }
spriteType = { name = "GFX_idea_storm_wreckage" texturefile = "gfx/interface/ideas/natural_disasters/idea_storm_wreckage.dds" }
spriteType = { name = "GFX_idea_burned_districts" texturefile = "gfx/interface/ideas/natural_disasters/idea_burned_districts.dds" }
spriteType = { name = "GFX_idea_unstable_mountain_passes" texturefile = "gfx/interface/ideas/natural_disasters/idea_unstable_mountain_passes.dds" }
spriteType = { name = "GFX_idea_volcanic_ashfall" texturefile = "gfx/interface/ideas/natural_disasters/idea_volcanic_ashfall.dds" }
spriteType = { name = "GFX_idea_tsunami_scoured_coast" texturefile = "gfx/interface/ideas/natural_disasters/idea_tsunami_scoured_coast.dds" }
spriteType = { name = "GFX_idea_meteor_scars" texturefile = "gfx/interface/ideas/natural_disasters/idea_meteor_scars.dds" }
spriteType = { name = "GFX_idea_disaster_recovery_pressure" texturefile = "gfx/interface/ideas/natural_disasters/idea_disaster_recovery_pressure.dds" }
```

Use notes:
- Report images are already processed into the repo report-card style at `210x176`.
- News images are black-and-white and sized `397x153`.
- The super-event title, quote, button text, and audio are tracked in the super-event research docs and wired through the shared super-event files.
- DDS files were built with `convert -define dds:compression=none` after the repo DDS helper failed on this checkout.
