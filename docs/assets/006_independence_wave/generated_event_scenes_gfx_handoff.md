# Event 006 generated event-scene GFX handoff

## Registration target

Suggested file: `interface/006_independence_wave.gfx`. These are proposed deterministic names because no final sprite identifiers were registered when production began.

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
- ASSET-005: super-event titled `The League of New States`; the final super-event slot remains owned by the main implementation.
- ASSET-006: super-event titled `Every Border a Casus Belli`; the final super-event slot remains owned by the main implementation.

No `.gfx`, `.gui`, event, localisation, scripted-localisation, spreadsheet, or spec file was edited by the asset tranche. The main agent must bind the proposed sprite names to the final event pictures and super-event slots and update this handoff if implementation chooses different stable identifiers.
