# IW-017 Corsica portrait GFX handoff

This handoff is review-only. Preserve the existing sprites and paths; do not
convert or overwrite a runtime DDS until an independent visual audit passes the
corresponding exact PNG hash.

| Role | Review PNG | Stable sprite | Authoritative runtime texture path | Target | Status |
|---|---|---|---|---|---|
| Civic leader / Adolphe Landry | `processed_png/COR_adolphe_landry.png` | `GFX_portrait_COR_independence_wave_adolphe_landry` | `gfx/leaders/006_independence_wave/portrait_COR_independence_wave_adolphe_landry.dds` | 156x210 | `needs_independent_visual_audit` |
| Security commander / Jean Chiappe | `processed_png/COR_jean_chiappe.png` | `GFX_portrait_COR_independence_wave_jean_chiappe` | `gfx/leaders/006_independence_wave/portrait_COR_independence_wave_jean_chiappe.dds` | 156x210 | `needs_independent_visual_audit` |

Even if both portraits pass, IW-017 requires a fresh post-wiring country-package
audit before compile-time content attestation. Candidate approval must not
create advisor/dossier or `_small` derivatives.
