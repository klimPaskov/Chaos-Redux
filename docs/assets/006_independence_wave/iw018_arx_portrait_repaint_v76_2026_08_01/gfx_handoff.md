# IW-018 ARX Emilio Lussu portrait handoff

| Consumer | Character key | Intended sprite | Intended DDS | Current state |
| --- | --- | --- | --- | --- |
| ARX provisional assembly | `ARX_emilio_lussu` | `GFX_portrait_ARX_independence_wave_emilio_lussu` | `gfx/leaders/006_independence_wave/portrait_ARX_independence_wave_emilio_lussu.dds` | Promoted; source-locked HOI4 repaint and byte-matched runtime DDS |
| ARX crown consultative council | `ARX_sardinian_crown_consultative_council` → visible `ARX_luigi_mella_santelia` | `GFX_portrait_ARX_independence_wave_luigi_mella_santelia` | `gfx/leaders/006_independence_wave/portrait_ARX_luigi_mella_santelia.dds` | Promoted researched Mella replacement for the former Pala placeholder |
| ARX Sardinian-linked guard command | `ARX_gavino_piras` → visible `ARX_vittorio_verne` | `GFX_portrait_ARX_independence_wave_vittorio_verne` | `gfx/leaders/006_independence_wave/portrait_ARX_vittorio_verne.dds` | Promoted sourced Verne replacement; role wording is Sardinia-linked, not Sardinian-born |
| ARX Sardinian-born guard command | Evidence-only `ARX_gioacchino_solinas` | `GFX_portrait_ARX_independence_wave_gioacchino_solinas` | no runtime DDS | Evidence only; PD-Italy-only 1943 source remains rights-gated |

The stable Lussu, Mella, and Verne consumers are wired in `common/characters/006_independence_wave_mediterranean_characters.txt`, `interface/006_independence_wave_mediterranean_portraits.gfx`, and localisation. The internal ARX_gavino_piras key remains stable for scripts while its visible name is Verne; exact Pala/Piras identities are not relabelled. This handoff does not add advisor icons. The parent-owned package audit and exact IW-018 attestation are now the admission authority.
