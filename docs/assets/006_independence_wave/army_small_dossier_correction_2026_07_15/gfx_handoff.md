# Event 006 army-small dossier GFX handoff

## Runtime contract

All stable texture paths and sprite names remain unchanged. The correction only
replaces the bytes behind the existing `_small` texture paths with independent
`65x67` dossier cards.

| Tag | Sprite | Installed DDS | Registration state |
|---|---|---|---|
| ACX | `GFX_portrait_ACX_cornish_coastal_commander_small` | `gfx/leaders/006_independence_wave/portrait_ACX_cornish_coastal_commander_small.dds` | retained pool handoff; not registered by this correction |
| AEX | `GFX_portrait_AEX_flemish_industrial_security_commander_small` | `gfx/leaders/006_independence_wave/portrait_AEX_flemish_industrial_security_commander_small.dds` | retained pool handoff; not registered by this correction |
| AFX | `GFX_portrait_AFX_walloon_reserve_commander_small` | `gfx/leaders/006_independence_wave/portrait_AFX_walloon_reserve_commander_small.dds` | `interface/006_independence_wave_region_01_portraits.gfx` |
| AGX | `GFX_portrait_AGX_friesland_coastal_commander_small` | `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_commander_small.dds` | `interface/006_independence_wave_region_01_portraits.gfx` |
| AJX | `GFX_portrait_AJX_karl_becker_small` | `gfx/leaders/006_independence_wave/portrait_AJX_saar_industrial_security_commissioner_small.dds` | `interface/006_independence_wave_region_01_portraits.gfx` |
| BAY | `GFX_portrait_BAY_independence_wave_mountain_commandant_small` | `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_mountain_commandant_small.dds` | `interface/006_independence_wave_region_01_portraits.gfx` |
| BRI | `GFX_portrait_BRI_independence_wave_coastal_commandant_small` | `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_coastal_commandant_small.dds` | `interface/006_independence_wave_brittany_portraits.gfx` |
| RHI | `GFX_portrait_RHI_independence_wave_river_commandant_small` | `gfx/leaders/006_independence_wave/portrait_RHI_independence_wave_river_commandant_small.dds` | `interface/006_independence_wave_region_01_portraits.gfx` |
| SCO | `GFX_portrait_SCO_independence_wave_territorial_commandant_small` | `gfx/leaders/006_independence_wave/portrait_SCO_independence_wave_territorial_commandant_small.dds` | `interface/006_independence_wave_region_01_portraits.gfx` |
| WLS | `GFX_portrait_WLS_independence_wave_mountain_commandant_small` | `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_mountain_commandant_small.dds` | `interface/006_independence_wave_region_01_portraits.gfx` |

## Engine format

Every installed texture is a one-level, uncompressed, legacy `65x67` BGRA DDS
with alpha and exact length `17,548` bytes. `validation_report.json` proves that
each installed file matches the retained `final_dds/` copy byte for byte and
decodes pixel-identically to its approved processed PNG.

No `.gfx` edit is required. Consumers continue to use the same `small` portrait
fields and sprite names. These commander dossier sprites must not be reused as
political-advisor, high-command, focus, decision, or idea icons.
