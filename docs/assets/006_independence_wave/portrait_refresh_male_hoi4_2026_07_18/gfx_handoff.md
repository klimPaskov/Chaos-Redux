# Event 006 portrait refresh gfx handoff

The runtime DDS files are already placed under `gfx/leaders/006_independence_wave/` at the existing stable filenames. Do not add new sprite names or edit `.gfx` in this handoff.

Suggested existing registration surface: `interface/006_independence_wave_region_01_portraits.gfx` for ACX/AEX/AFX/AGX/AJX/BAY/RHI/SCO/WLS and `interface/006_independence_wave_brittany_portraits.gfx` for BRI, preserving the current sprite names and army `large`/`small` slots. The leader-only institutional portraits use their existing large sprite names in the same registration surfaces.

## Runtime texture mapping

For each commander large stem `<stem>`:

```text
GFX_portrait_<tag>_<role>_large -> gfx/leaders/006_independence_wave/portrait_<stem>.dds
GFX_portrait_<tag>_<role>_small -> gfx/leaders/006_independence_wave/portrait_<stem>_small.dds
```

Commander large DDS files are exact `156x210`; their matching small DDS files are exact `65x67` derivatives. The ten small derivatives are only for the ten commander stems in `manifest.md`.

Institutional/country-leader large DDS files use the existing large sprite definitions only; no small derivatives were produced for those ten stems.

No `.gfx` or gameplay files were edited by the asset producer. The main agent should retain the current sprite identifiers and only verify that their existing texture paths resolve to the runtime files listed in the manifest.

## Stable sprite names and DDS paths

| Existing sprite name | Runtime texture |
|---|---|
| `portrait_ACX_cornish_port_and_mines_committee` | `gfx/leaders/006_independence_wave/portrait_ACX_cornish_port_and_mines_committee.dds` |
| `portrait_ACX_cornish_coastal_commander` | `gfx/leaders/006_independence_wave/portrait_ACX_cornish_coastal_commander.dds` |
| `portrait_ACX_cornish_coastal_commander_small` | `gfx/leaders/006_independence_wave/portrait_ACX_cornish_coastal_commander_small.dds` |
| `portrait_AEX_flemish_civil_industrial_board` | `gfx/leaders/006_independence_wave/portrait_AEX_flemish_civil_industrial_board.dds` |
| `portrait_AEX_flemish_industrial_security_commander` | `gfx/leaders/006_independence_wave/portrait_AEX_flemish_industrial_security_commander.dds` |
| `portrait_AEX_flemish_industrial_security_commander_small` | `gfx/leaders/006_independence_wave/portrait_AEX_flemish_industrial_security_commander_small.dds` |
| `portrait_AFX_walloon_provisional_assembly` | `gfx/leaders/006_independence_wave/portrait_AFX_walloon_provisional_assembly.dds` |
| `portrait_AFX_walloon_reserve_commander` | `gfx/leaders/006_independence_wave/portrait_AFX_walloon_reserve_commander.dds` |
| `portrait_AFX_walloon_reserve_commander_small` | `gfx/leaders/006_independence_wave/portrait_AFX_walloon_reserve_commander_small.dds` |
| `portrait_AGX_friesland_coastal_council` | `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_council.dds` |
| `portrait_AGX_friesland_coastal_commander` | `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_commander.dds` |
| `portrait_AGX_friesland_coastal_commander_small` | `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_commander_small.dds` |
| `portrait_AJX_saar_municipal_neutral_commission` | `gfx/leaders/006_independence_wave/portrait_AJX_saar_municipal_neutral_commission.dds` |
| `portrait_AJX_saar_industrial_security_commissioner` | `gfx/leaders/006_independence_wave/portrait_AJX_saar_industrial_security_commissioner.dds` |
| `portrait_AJX_saar_industrial_security_commissioner_small` | `gfx/leaders/006_independence_wave/portrait_AJX_saar_industrial_security_commissioner_small.dds` |
| `portrait_BAY_independence_wave_state_council` | `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_state_council.dds` |
| `portrait_BAY_independence_wave_mountain_commandant` | `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_mountain_commandant.dds` |
| `portrait_BAY_independence_wave_mountain_commandant_small` | `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_mountain_commandant_small.dds` |
| `portrait_BRI_independence_wave_civic_commission` | `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_civic_commission.dds` |
| `portrait_BRI_independence_wave_coastal_commandant` | `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_coastal_commandant.dds` |
| `portrait_BRI_independence_wave_coastal_commandant_small` | `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_coastal_commandant_small.dds` |
| `portrait_RHI_independence_wave_provisional_directorate` | `gfx/leaders/006_independence_wave/portrait_RHI_independence_wave_provisional_directorate.dds` |
| `portrait_RHI_independence_wave_river_commandant` | `gfx/leaders/006_independence_wave/portrait_RHI_independence_wave_river_commandant.dds` |
| `portrait_RHI_independence_wave_river_commandant_small` | `gfx/leaders/006_independence_wave/portrait_RHI_independence_wave_river_commandant_small.dds` |
| `portrait_SCO_independence_wave_civic_convention` | `gfx/leaders/006_independence_wave/portrait_SCO_independence_wave_civic_convention.dds` |
| `portrait_SCO_independence_wave_territorial_commandant` | `gfx/leaders/006_independence_wave/portrait_SCO_independence_wave_territorial_commandant.dds` |
| `portrait_SCO_independence_wave_territorial_commandant_small` | `gfx/leaders/006_independence_wave/portrait_SCO_independence_wave_territorial_commandant_small.dds` |
| `portrait_WLS_independence_wave_national_council` | `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_national_council.dds` |
| `portrait_WLS_independence_wave_mountain_commandant` | `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_mountain_commandant.dds` |
| `portrait_WLS_independence_wave_mountain_commandant_small` | `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_mountain_commandant_small.dds` |
