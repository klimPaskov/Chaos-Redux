# IW-018 ARX v75 research-only GFX handoff

No `.gfx` file was edited and no final DDS exists in this package.

The parent-owned consumers remain:

| Consumer | Existing sprite | Research disposition | Runtime action |
|---|---|---|---|
| `ARX_sardinian_provisional_assembly` | `GFX_portrait_ARX_independence_wave_emilio_lussu` | Emilio Lussu source master is `source_ready_for_parent_review`. | Keep sprite stable; do not wire the existing DDS until the new source-locked repaint and independent audit pass. |
| `ARX_sardinian_crown_consultative_council` | `GFX_portrait_ARX_independence_wave_vittorio_pala` | Exact `Vittorio Pala` identity is `blocked_name_only`. Mella is a candidate only if the parent explicitly changes identity/name; Eugenio and Adalberto are rights-blocked alternatives. | Keep current sprite unwired. Do not relabel a candidate as Vittorio Pala. |
| `ARX_gavino_piras` | `GFX_portrait_ARX_independence_wave_gavino_piras` | Exact `Gavino Piras` identity is `blocked_name_only`. Solinas is the strongest Sardinian-born candidate but remains rights/style review; Vernè is rights-strong but not Sardinian-born; Valle is owner-blocked; Pizzorno is quality-blocked. | Keep current sprite unwired. Do not relabel a candidate as Gavino Piras. |

If the parent accepts a candidate identity change, the parent must update the character/localisation design and then create a new final sprite only after the grounded portrait gate passes. The final runtime texture should remain under the existing event-owned leader folder and use the stable sprite name supplied by the parent.

Suggested downstream source paths:

- `docs/assets/006_independence_wave/iw018_arx_portrait_source_research_v75_2026_08_01/source_masters/emilio_lussu_senate_pre1958.jpg`
- `docs/assets/006_independence_wave/iw018_arx_portrait_source_research_v75_2026_08_01/source_masters/luigi_mella_santelia_senate.gif`
- `docs/assets/006_independence_wave/iw018_arx_portrait_source_research_v75_2026_08_01/source_masters/gioacchino_solinas_1943_original.png`

These are evidence masters only, not runtime paths. No processed PNG, DDS, crop JSON, or sprite snippet is being handed off as complete.
