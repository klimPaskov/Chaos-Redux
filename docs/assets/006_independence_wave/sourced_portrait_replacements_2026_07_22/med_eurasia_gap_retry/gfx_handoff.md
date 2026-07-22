# Event 006 sourced portrait retry — deferred GFX handoff

This file records proposed runtime names only. No PNG, DDS, `.gfx`, crop, or
resize was produced in the source-only retry. The parent must independently
review each source-ready master and run the approved portrait processing and
DDS pipeline before wiring.

## Source-ready candidates

| Consumer role | Proposed sprite name | Proposed runtime DDS path | Source master | Status |
|---|---|---|---|---|
| `ASX_salvatore_licata` | `GFX_portrait_ASX_independence_wave_salvatore_licata` | `gfx/leaders/006_independence_wave/portrait_ASX_independence_wave_salvatore_licata.dds` | [`source_masters/sicily/asx_luigi_rizzo_rear_admiral_1935.jpg`](source_masters/sicily/asx_luigi_rizzo_rear_admiral_1935.jpg) | `source_ready`; deferred processing |
| `CHU_independence_wave_federal_presidium` | `GFX_portrait_CHU_independence_wave_federal_presidium` | `gfx/leaders/006_independence_wave/portrait_CHU_independence_wave_federal_presidium.dds` | [`source_masters/volga/chu_galimzhan_ibrahimov.jpg`](source_masters/volga/chu_galimzhan_ibrahimov.jpg) | `source_ready`; deferred processing |
| `ASY_independence_wave_civic_national_assembly` | `GFX_portrait_ASY_independence_wave_civic_national_assembly` | `gfx/leaders/006_independence_wave/portrait_ASY_independence_wave_civic_national_assembly.dds` | [`source_masters/assyria/asy_naum_faiq_1920s.jpg`](source_masters/assyria/asy_naum_faiq_1920s.jpg) | `source_ready`; deferred processing |
| `ASY_independence_wave_levies_guardianship` | `GFX_portrait_ASY_independence_wave_levies_guardianship` | `gfx/leaders/006_independence_wave/portrait_ASY_independence_wave_levies_guardianship.dds` | [`source_masters/assyria/asy_agha_petros_1920.jpg`](source_masters/assyria/asy_agha_petros_1920.jpg) | `source_ready`; deferred processing |

## Do not wire

The Sardinian Gavino Piras and Vittorio Pala gaps remain blocked (late-era or
role-mismatched candidates). CHU Bolgar remains blocked on the 187x250 Shamil
Usmanov master; CHU River Security remains needs-review on the Bashkir Zeki
Velidi Togan master and blocked on the group Musa Murtazin photograph. ASY
Concordat remains blocked on the pre-1936 Mar Benyamin Shimun image and on the
watermarked/rights-unclear Malik Ismail II lead. No fallback or generated face
is authorized by this handoff.

## Deferred steps

1. A separate reviewer confirms identity, role fit, and the source/rights notes
   in `manifest.md`.
2. The approved processing workflow creates the exact runtime PNG and DDS
   outputs; this handoff does not create them.
3. Only after those files exist may the main implementation agent add or
   update `.gfx` registrations and gameplay references.
