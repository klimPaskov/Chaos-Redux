# IW-007 Frisia portrait refinishes — GFX handoff

This is an evidence handoff only. The parent explicitly deferred DDS/runtime
conversion until independent likeness review. No `.gfx`, gameplay,
localisation, or runtime file was edited here.

| Role | Candidate to audit | Stable sprite | Intended runtime texture path | Target | Target `.gfx` | Status |
|---|---|---|---|---|---|---|
| AGX civic leader / Douwe Kalma | `processed_png/AGX_friesland_coastal_council.png` | `GFX_portrait_AGX_friesland_coastal_council` | `gfx/leaders/AGX_friesland_coastal_council.dds` | 156x210 | existing AGX portrait `.gfx` definition; preserve current file and sprite name | `needs_independent_visual_audit` |
| AGX coastal commander / Pieter Reenalda | `processed_png/AGX_friesland_coastal_commander.png` (candidate 02) | `GFX_portrait_AGX_friesland_coastal_commander` | `gfx/leaders/AGX_friesland_coastal_commander.dds` | 156x210 | existing AGX portrait `.gfx` definition; preserve current file and sprite name | `needs_independent_visual_audit` |

Candidate 01 for Reenalda is retained at
`processed_png/AGX_friesland_coastal_commander_candidate_01.png` solely for
comparison and is blocked for identity drift. Do not wire it.

After an independent audit approves a candidate, the parent may convert its
`156x210` processed PNG through the repository-standard converter and promote
the DDS to the intended runtime path. Until then, there is no copy-ready DDS
snippet and no approval claim.
