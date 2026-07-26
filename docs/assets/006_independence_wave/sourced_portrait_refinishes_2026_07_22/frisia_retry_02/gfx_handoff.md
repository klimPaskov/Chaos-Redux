# IW-007 Frisia portrait refinishes — GFX handoff

This is a historical evidence handoff. At the time of this package the parent
deferred DDS/runtime conversion until independent likeness review. The
2026-07-26 trial-02 package supersedes this handoff for current runtime bytes;
see `../../sourced_portrait_refinishes_2026_07_26/frisia_douwe_kalma_trial_02/`
and `../../sourced_portrait_refinishes_2026_07_26/frisia_pieter_reenalda_trial_02/`.

| Role | Candidate to audit | Stable sprite | Intended runtime texture path | Target | Target `.gfx` | Status |
|---|---|---|---|---|---|---|
| AGX civic leader / Douwe Kalma | `processed_png/AGX_friesland_coastal_council.png` | `GFX_portrait_AGX_friesland_coastal_council` | `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_council.dds` | 156x210 | Historical candidate; current promoted DDS is documented in the 2026-07-26 trial manifest | `superseded_review_evidence` |
| AGX coastal commander / Pieter Reenalda | `processed_png/AGX_friesland_coastal_commander.png` (candidate 02) | `GFX_portrait_AGX_friesland_coastal_commander` | `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_commander.dds` | 156x210 | Historical candidate; current promoted DDS is documented in the 2026-07-26 trial manifest | `superseded_review_evidence` |

Candidate 01 for Reenalda is retained at
`processed_png/AGX_friesland_coastal_commander_candidate_01.png` solely for
comparison and is blocked for identity drift. Do not wire it.

The independent audit passed both selected candidates in this historical
package. Current promotion was performed from the newer exact-crop/ImageGen
trial-02 candidates after a fresh producer-separate audit; the stable sprite
definitions remain unchanged. The bounded post-wire portrait/package audit is
`docs/plans/006_independence_wave_plans/subagent_handoffs/006_agx_postwire_portrait_package_audit_2026_07_26.md`.
