# Event 006 IW-043 / IW-058 portrait source handoff

This handoff records one parent-owned promotion and five deferred source-only rows. No `.gfx` file was edited or renamed. The existing CHU federal-presidium sprite was retained, and its v2 candidate was converted to the final DDS only after the independent visual/provenance audit PASS. The remaining rows stay blocked or source-only until their own gates pass.

## Proposed consumer mapping

| Route | Proposed subject | Existing character token | Proposed sprite name | Intended runtime DDS path | Status |
| --- | --- | --- | --- | --- | --- |
| CHU federal presidium | Galimzhan Ibrahimov | `CHU_independence_wave_federal_presidium` | `GFX_portrait_CHU_independence_wave_federal_presidium` | `gfx/leaders/006_independence_wave/portrait_CHU_independence_wave_federal_presidium.dds` | `runtime_promoted`; v2 raw master, candidate, prompt, provenance, independent visual audit, and DDS hash retained; existing `.gfx` sprite and character consumer unchanged |
| CHU Bolgar civic presidium | Shamil Usmanov | `CHU_independence_wave_bolgar_civic_presidium` | `GFX_portrait_CHU_independence_wave_bolgar_civic_presidium` | `gfx/leaders/006_independence_wave/portrait_CHU_independence_wave_bolgar_civic_presidium.dds` | `blocked`; 187x250 source fails quality gate |
| CHU river security directorate | Ahmet Zeki Velidi Togan | `CHU_independence_wave_river_security_directorate` | `GFX_portrait_CHU_independence_wave_river_security_directorate` | `gfx/leaders/006_independence_wave/portrait_CHU_independence_wave_river_security_directorate.dds` | `needs_user_review`; source institution/date/role review open |
| ASY concordat council | Mar Benyamin Shimun XXI lead only as rejected evidence | `ASY_independence_wave_concordat_council` | `GFX_portrait_ASY_independence_wave_concordat_council` | `gfx/leaders/006_independence_wave/portrait_ASY_independence_wave_concordat_council.dds` | `blocked`; subject died in 1918 and living Mar Eshai sources are unlicensed |
| ASY civic national assembly | Naum Faiq | `ASY_independence_wave_civic_national_assembly` | `GFX_portrait_ASY_independence_wave_civic_national_assembly` | `gfx/leaders/006_independence_wave/portrait_ASY_independence_wave_civic_national_assembly.dds` | `source_ready` pending explicit legacy-continuity approval |
| ASY Levies guardianship | Agha Petros | `ASY_independence_wave_levies_guardianship` | `GFX_portrait_ASY_independence_wave_levies_guardianship` | `gfx/leaders/006_independence_wave/portrait_ASY_independence_wave_levies_guardianship.dds` | `source_ready` pending explicit legacy-continuity approval |

The already accepted rows remain unchanged: Mirsaid Sultan-Galiev maps to `GFX_portrait_CHU_independence_wave_middle_volga_congress`, and Gallo Shabo maps to `GFX_portrait_ASY_independence_wave_provisional_national_council`. This handoff does not duplicate or rewire either accepted row.

## Deferred processing contract

For each `source_ready` row, use the source master and exact crop listed in `manifest.md` and `crop_metadata/`. The crop is the identity reference, not a runtime texture. Use the canonical leader style references at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/` only for painterly treatment, framing, and subdued palette.

The later producer must retain the raw source, crop-equality JSON, source-locked identity-preserving repaint master at original output size, deterministic `156x210` processed PNG, review sheet, independent likeness/style/provenance audit, and final DDS in distinct paths. Run `convert_to_dds.py` only after the independent audit passes every gate. No plain resize, filter, illustration, or generated substitute is acceptable. For the promoted Galimzhan row, the final DDS is `gfx/leaders/006_independence_wave/portrait_CHU_independence_wave_federal_presidium.dds` with SHA-256 `977e0f8d359930f75e01e380a36893ef6a8f25a5b1ce5bbd8cc3c2f3abf6b5f5`.

## Explicit blockers

- Do not wire the Shamil Usmanov source or crop; the source is too small for a dependable HOI4 leader portrait and no higher-resolution redistributable source was found.
- Do not wire the Mar Benyamin Shimun source or crop; the Library of Congress subject died in 1918 and therefore cannot represent a living 1936 concordat office without a separately approved legacy design amendment.
- Do not wire Mar Eshai Shimun XXIII Foundation imagery; the archive states copyright protection and gives no reusable license.
- Do not wire Malik Ismail II Tyareh imagery; the located family image is watermarked and rights-unclear.
- Do not wire a generated or generic replacement for any blocked or needs-review row.
