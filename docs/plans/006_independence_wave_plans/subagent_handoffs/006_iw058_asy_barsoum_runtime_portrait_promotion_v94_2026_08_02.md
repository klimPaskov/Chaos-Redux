# IW-058 ASY Barsoum runtime portrait promotion v94

Date: 2026-08-02

## Scope and decision

This parent-owned follow-up promotes only the audited Ignatius Aphrem I Barsoum concordat-council portrait to the existing ASY civilian-large consumer. It does not admit IW-058, alter its package readiness, change formables, or replace any other ASY leader. The v93 independent audit passes identity/likeness, HOI4 leader style/framing, provenance, and the explicit PD-1923/1921 rights/date basis with a low-resolution group-photo caveat. Parent release acceptance is recorded here as a source-admission decision and is not a legal opinion.

## Source-to-runtime chain

| Stage | Path | Evidence |
| --- | --- | --- |
| Immutable source | `docs/assets/006_independence_wave/asy_portrait_source_retry_v92_2026_08_01/source_masters/ASY_ignatius_afram_barsoum_paris_1921.png` | 1728x1314 RGBA; SHA-256 `ed5473dab88a27d4dd5736ab5b6136a95e1e9fef1622eff7005dd0e17ed7d9d9` |
| Exact crop | `docs/assets/006_independence_wave/asy_portrait_source_retry_v92_2026_08_01/source_crops/ASY_concordat_council_ignatius_afram_barsoum_paris_head_shoulders.png` | `(650,85,970,470)`, 320x385 RGBA; decoded pixels equal; SHA-256 `c91d7e97dc8fa06ed9dc3f7fa70b01b09be71ef53a60e07c29737728999d1555` |
| Raw HOI4 repaint | `docs/assets/006_independence_wave/asy_portrait_source_retry_v92_2026_08_01/repaints_raw/ASY_concordat_council_ignatius_afram_barsoum_hoi4_repaint_v1.png` | 1144x1375 RGB; SHA-256 `8b0251b0638340ef85fe4610efd2cafa70b561e6297490dcd07cac8d2707ef35` |
| Deterministic candidate | `docs/assets/006_independence_wave/asy_portrait_source_retry_v92_2026_08_01/repaints_processed/ASY_concordat_council_ignatius_afram_barsoum_156x210_candidate_v1.png` | 156x210 RGB; SHA-256 `220e81c29b35963668bcc2de3d8340aec3047a74da6655fabcda07f26d59d595` |
| Runtime DDS | `gfx/leaders/006_independence_wave/portrait_ASY_independence_wave_concordat_council.dds` | DirectXTex BGRA DDS, 156x210, 131168 bytes; SHA-256 `5c034700247de09480eedd294ca192045c18dd8b9582fe236dda776e7d67ad06` |

The conversion used `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` with explicit `--width 156 --height 210`. The existing sprite registration remains `GFX_portrait_ASY_independence_wave_concordat_council` in `interface/006_independence_wave_iw043_iw058_portraits.gfx`; no `.gfx` edit was necessary. The superseded runtime DDS hash was `8cfd82ac...`, and the new file is the only current consumer at this stable path.

## Boundaries and validation

- The wider ASY package remains outside the fourteen exact content attestations.
- No advisor, high-command, commander-small, operative, dossier, `_small`, or other portrait family was created or wired.
- No character, localisation, focus, decision, formable, flag, or gameplay file changed.
- DDS header inspection confirms the `DDS ` signature, width `156`, height `210`, and one-level texture output (`mips` field `0` as emitted by texconv for a single level).
- The v93 independent audit remains the visual/provenance authority: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw058_asy_barsoum_pd1923_portrait_visual_audit_v93_2026_08_02.md`.

