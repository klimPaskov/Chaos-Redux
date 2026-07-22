# IW-010 Saar Schmelcher portrait GFX handoff

This handoff is review-only. No DDS or runtime edit is authorized until the
independent visual audit passes.

| Role | Review PNG | Stable sprite | Authoritative runtime texture path | Target | Status |
|---|---|---|---|---|---|
| AJX industrial-security commander / Willy Schmelcher | `processed_png/AJX_saar_industrial_security_commissioner.png` | `GFX_portrait_AJX_karl_becker` | `gfx/leaders/006_independence_wave/portrait_AJX_saar_industrial_security_commissioner.dds` | 156x210 | `needs_independent_visual_audit` |

If the portrait passes, preserve the sprite and texture filename, convert only
the approved native PNG with the repository-standard DDS converter, and change
the player-facing character identity from fictional Karl Becker to Willy
Schmelcher in the matching localisation/biography surfaces. IW-010 remains
fail-closed until its civic portrait and full package re-audit also pass.
