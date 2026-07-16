# Event 006 generated event-scene GFX handoff

## Registered sprites

Runtime file: `interface/006_independence_wave_event_pictures.gfx`. The deterministic handoff names are now registered unchanged.

```txt
spriteTypes = {
	spriteType = { name = "GFX_report_event_006_asset_001_wave_summary" texturefile = "gfx/event_pictures/006_independence_wave/report_event_006_asset_001_wave_summary.dds" }
	spriteType = { name = "GFX_report_event_006_asset_002_host_crisis" texturefile = "gfx/event_pictures/006_independence_wave/report_event_006_asset_002_host_crisis.dds" }
	spriteType = { name = "GFX_report_event_006_asset_003_first_recognition" texturefile = "gfx/event_pictures/006_independence_wave/report_event_006_asset_003_first_recognition.dds" }
	spriteType = { name = "GFX_news_event_006_asset_004_league_congress" texturefile = "gfx/event_pictures/006_independence_wave/news_event_006_asset_004_league_congress.dds" }
	spriteType = { name = "GFX_super_event_006_asset_005_league_formation" texturefile = "gfx/super_events/006_independence_wave/super_event_006_asset_005_league_formation.dds" }
	spriteType = { name = "GFX_super_event_006_asset_006_revisionist_milestone" texturefile = "gfx/super_events/006_independence_wave/super_event_006_asset_006_revisionist_milestone.dds" }
}
```

## Intended uses

- ASSET-001: automatic independence-wave summary report.
- ASSET-002: consolidated host-crisis report.
- ASSET-003: first-recognition milestone report.
- ASSET-004: first league-congress proclamation news event.
- ASSET-005: super-event titled `The League of New States`; its DDS and sprite registration are retained, but slot 23 has no runtime dispatch while audio 6001 remains blocked.
- ASSET-006: super-event titled `Every Border a Casus Belli`; it is wired to runtime slot 24 and audio 6002.

`chaosx.nr6.2` uses `GFX_report_event_006_asset_001_wave_summary`. ASSET-006 is consumed by the implemented dangerous-milestone incident. The host, recognition, league-news, and ASSET-005 sprites remain registered without this handoff claiming that their later incidents are wired.
