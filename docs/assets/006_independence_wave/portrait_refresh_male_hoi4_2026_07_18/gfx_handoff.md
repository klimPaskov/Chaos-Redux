# Event 006 portrait refresh gfx handoff

The runtime DDS files are already placed under `gfx/leaders/006_independence_wave/` at the existing stable filenames. Do not add new sprite names or edit `.gfx` in this handoff.

This handoff is superseded and retained only as provenance for the earlier full-size generated assets. Event 006 defines no commander miniature, advisor-card, dossier, or `_small` portrait. Current registrations must use full `156x210` source-cleared portraits only.

## Runtime texture mapping

For each source-cleared full portrait stem `<stem>`:

```text
GFX_portrait_<tag>_<role> -> gfx/leaders/006_independence_wave/portrait_<stem>.dds
```

Country-leader and commander DDS files are exact `156x210`. No Event 006 `_small` derivatives exist.

No `.gfx` or gameplay files were edited by the asset producer. The main agent should retain the current sprite identifiers and only verify that their existing texture paths resolve to the runtime files listed in the manifest.

## Stable sprite names and DDS paths

| Existing sprite name | Runtime texture |
|---|---|
| `portrait_ACX_cornish_port_and_mines_committee` | `gfx/leaders/006_independence_wave/portrait_ACX_cornish_port_and_mines_committee.dds` |
| `portrait_ACX_cornish_coastal_commander` | `gfx/leaders/006_independence_wave/portrait_ACX_cornish_coastal_commander.dds` |
| `portrait_AEX_flemish_civil_industrial_board` | `gfx/leaders/006_independence_wave/portrait_AEX_flemish_civil_industrial_board.dds` |
| `portrait_AEX_flemish_industrial_security_commander` | `gfx/leaders/006_independence_wave/portrait_AEX_flemish_industrial_security_commander.dds` |
| `portrait_AFX_walloon_provisional_assembly` | `gfx/leaders/006_independence_wave/portrait_AFX_walloon_provisional_assembly.dds` |
| `portrait_AFX_walloon_reserve_commander` | `gfx/leaders/006_independence_wave/portrait_AFX_walloon_reserve_commander.dds` |
| `portrait_AGX_friesland_coastal_council` | `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_council.dds` |
| `portrait_AGX_friesland_coastal_commander` | `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_commander.dds` |
| `portrait_AJX_saar_municipal_neutral_commission` | `gfx/leaders/006_independence_wave/portrait_AJX_saar_municipal_neutral_commission.dds` |
| `portrait_AJX_saar_industrial_security_commissioner` | `gfx/leaders/006_independence_wave/portrait_AJX_saar_industrial_security_commissioner.dds` |
| `portrait_BAY_independence_wave_state_council` | `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_state_council.dds` |
| `portrait_BAY_independence_wave_mountain_commandant` | `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_mountain_commandant.dds` |
| `portrait_BRI_independence_wave_civic_commission` | `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_civic_commission.dds` |
| `portrait_BRI_independence_wave_coastal_commandant` | `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_coastal_commandant.dds` |
| `portrait_RHI_independence_wave_provisional_directorate` | `gfx/leaders/006_independence_wave/portrait_RHI_independence_wave_provisional_directorate.dds` |
| `portrait_RHI_independence_wave_river_commandant` | `gfx/leaders/006_independence_wave/portrait_RHI_independence_wave_river_commandant.dds` |
| `portrait_SCO_independence_wave_civic_convention` | `gfx/leaders/006_independence_wave/portrait_SCO_independence_wave_civic_convention.dds` |
| `portrait_SCO_independence_wave_territorial_commandant` | `gfx/leaders/006_independence_wave/portrait_SCO_independence_wave_territorial_commandant.dds` |
| `portrait_WLS_independence_wave_national_council` | `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_national_council.dds` |
| `portrait_WLS_independence_wave_mountain_commandant` | `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_mountain_commandant.dds` |
