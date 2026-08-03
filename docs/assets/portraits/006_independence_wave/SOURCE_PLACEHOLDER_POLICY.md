# Independence Wave historical portrait source placeholders

Historical or otherwise grounded leader portraits currently use a provenance-preserving source placeholder. The required sequence is:

1. Preserve the attributed original source image unchanged.
2. Make an explicit head-and-shoulders crop and retain the crop evidence.
3. Fit the crop deterministically to `156x210` without repainting, recolouring, retouching, or applying an HOI4-style filter.
4. Convert that processed image to the runtime DDS and record the result as `source_placeholder`.

The unchanged originals are archived in this single durable folder and are not runtime inputs:

- `portrait_ARX_gioacchino_solinas_source.png`
- `portrait_ARX_independence_wave_emilio_lussu_source.jpg`
- `portrait_ARX_luigi_mella_santelia_source.gif`
- `portrait_ARX_vittorio_verne_source.jpg`
- `portrait_BAY_rupprecht_of_bavaria_source.jpg`
- `portrait_FIJ_ratu_sir_lala_sukuna_source.jpg`
- `portrait_FIJ_vishnu_deo_source.jpg`
- `portrait_RHI_josef_friedrich_matthes_source.jpg`
- `portrait_ASX_luigi_rizzo_source.jpg`
- `portrait_ASX_luigi_sturzo_source.jpeg`
- `portrait_ASX_pietro_lanza_di_scalea_source.jpg`
- `portrait_ASX_vincenzo_di_benedetto_source.gif`
- `portrait_COR_adolphe_landry_source.jpg`
- `portrait_COR_jean_chiappe_source.jpg`
- `portrait_WLS_j_h_thomas_source.jpg`
- `portrait_WLS_george_cornwallis_west_source.jpg`
- `portrait_DOX_prempeh_ii_source.jpg`
- `portrait_SOK_muhammad_dikko_source.jpg`

The archive is intentionally separate from the event workspace and contains one folder only. Runtime `.dds` files remain under `gfx/leaders/006_independence_wave/`. A later HOI4-style repaint is an optional replacement pass and requires an explicit user request; it must retain the unchanged original and the source-placeholder candidate.

The current processed placeholder tranche is recorded under `docs/assets/006_independence_wave/source_placeholder_2026_08_03/` with one crop, metadata record, and `156x210` PNG per promoted source. The corresponding runtime DDS files are wired under `gfx/leaders/006_independence_wave/`; no runtime reference points into the durable archive.

Fictional or genuinely high-chaos portraits follow the generated HOI4-style portrait workflow and keep their source/prompt package beside the other durable portrait records. This policy does not authorize new advisor icons for Independence Wave.
