# IW-007 Frisia portrait refinishes — GFX handoff

This is an evidence handoff only. The parent explicitly deferred DDS/runtime
conversion until independent likeness review. No `.gfx`, gameplay,
localisation, or runtime file was edited here.

| Role | Candidate to audit | Stable sprite | Intended runtime texture path | Target | Target `.gfx` | Status |
|---|---|---|---|---|---|---|
| AGX civic leader / Douwe Kalma | `processed_png/AGX_friesland_coastal_council.png` | `GFX_portrait_AGX_friesland_coastal_council` | `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_council.dds` | 156x210 | `interface/006_independence_wave_region_01_portraits.gfx`; existing sprite preserved | `approved_wired_pending_country_package_reaudit` |
| AGX coastal commander / Pieter Reenalda | `processed_png/AGX_friesland_coastal_commander.png` (candidate 02) | `GFX_portrait_AGX_friesland_coastal_commander` | `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_commander.dds` | 156x210 | `interface/006_independence_wave_region_01_portraits.gfx`; existing sprite preserved | `approved_wired_pending_country_package_reaudit` |

Candidate 01 for Reenalda is retained at
`processed_png/AGX_friesland_coastal_commander_candidate_01.png` solely for
comparison and is blocked for identity drift. Do not wire it.

The independent audit passes both selected candidates. The parent converted
the exact processed PNGs with the repository-standard converter, retained the
existing sprite definitions, and copied byte-identical DDS files to the paths
above. Package-level runtime admission remains fail-closed until a fresh IW-007
country-package audit passes.
