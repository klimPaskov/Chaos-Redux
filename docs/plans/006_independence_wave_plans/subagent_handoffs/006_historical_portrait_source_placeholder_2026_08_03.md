# Event 006 historical portrait source-placeholder handoff

This handoff applies the latest portrait decision to the promoted grounded identities in the current runtime tranche. Historical portraits use the unchanged sourced image, an explicit head-and-shoulders crop, deterministic `156x210` resizing, and DDS conversion. No ImageGen, ComfyUI, repainting, recolouring, retouching, or HOI4-style filter was applied.

## Durable source archive

The unchanged source masters are kept in the single folder `docs/assets/portraits/006_independence_wave/`. The archive is not a runtime path. Crop equality metadata and processed candidates are under `docs/assets/006_independence_wave/source_placeholder_2026_08_03/`.

## Runtime conversions

Every processed candidate is RGB `156x210`; each DDS is a one-level BGRA `156x210` file produced by `convert_to_dds.py`.

| Source-placeholder candidate | Runtime DDS | Candidate SHA-256 prefix | DDS SHA-256 prefix |
| --- | --- | --- | --- |
| `portrait_ARX_independence_wave_emilio_lussu.png` | `gfx/leaders/006_independence_wave/portrait_ARX_independence_wave_emilio_lussu.dds` | `8569e4f83870edd3` | `106e63fb13d03e6e` |
| `portrait_ARX_luigi_mella_santelia.png` | `gfx/leaders/006_independence_wave/portrait_ARX_luigi_mella_santelia.dds` | `9e5dc6d9ac0c6a06` | `746c60bedb76abdb` |
| `portrait_ARX_vittorio_verne.png` | `gfx/leaders/006_independence_wave/portrait_ARX_vittorio_verne.dds` | `00c3dd377d492e82` | `5002742c35a37951` |
| `portrait_ASX_luigi_rizzo.png` | `gfx/leaders/006_independence_wave/portrait_ASX_independence_wave_luigi_rizzo.dds` | `3b486995cda6ce7a` | `6a5fd9d89e465498` |
| `portrait_ASX_luigi_sturzo.png` | `gfx/leaders/006_independence_wave/portrait_ASX_independence_wave_luigi_sturzo.dds` | `412218c729f80258` | `17556fee575b624c` |
| `portrait_ASX_pietro_lanza_di_scalea.png` | `gfx/leaders/006_independence_wave/portrait_ASX_independence_wave_pietro_lanza_di_scalea.dds` | `c625be45fb9dee9b` | `2c36c843b1f3d929` |
| `portrait_ASX_vincenzo_di_benedetto.png` | `gfx/leaders/006_independence_wave/portrait_ASX_independence_wave_vincenzo_di_benedetto.dds` | `d97d6d86105d3629` | `1b9a19b65673924e` |
| `portrait_BAY_rupprecht_of_bavaria.png` | `gfx/leaders/006_independence_wave/portrait_BAY_rupprecht_of_bavaria.dds` | `7d06249c1c0f6828` | `00f82253f674cd2a` |
| `portrait_COR_adolphe_landry.png` | `gfx/leaders/006_independence_wave/portrait_COR_independence_wave_adolphe_landry.dds` | `3621bc887e0d8200` | `19cc485579d3676c` |
| `portrait_COR_jean_chiappe.png` | `gfx/leaders/006_independence_wave/portrait_COR_independence_wave_jean_chiappe.dds` | `9b8896622e985614` | `d6c8543e99721d60` |
| `portrait_DOX_prempeh_ii.png` | `gfx/leaders/006_independence_wave/portrait_DOX_prempeh_ii.dds` | `e4cd9a0f55504f76` | `601e10a85fc67396` |
| `portrait_RHI_josef_friedrich_matthes.png` | `gfx/leaders/006_independence_wave/portrait_RHI_josef_friedrich_matthes.dds` | `51206053ea9e2283` | `103ceb73f2df2f7a` |
| `portrait_SOK_muhammad_dikko.png` | `gfx/leaders/006_independence_wave/portrait_SOK_muhammad_dikko.dds` | `4b20fe233a58733b` | `0e74d236149cb689` |
| `portrait_WLS_j_h_thomas.png` | `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_national_council.dds` | `051521fa37d9f681` | `7dbd7ceaad173efb` |
| `portrait_WLS_george_cornwallis_west.png` | `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_mountain_commandant.dds` | `971e93bfae40a4a1` | `873bfc5fd3e95fd5` |

All crop metadata is in the matching `metadata/<basename>_source_crop.json` file. The two WLS DDS files use the existing role-specific runtime names; the placeholder candidate names follow the durable source subject names so provenance is not hidden behind an institutional sprite id.

## Scope and holds

This is a source-placeholder conversion tranche, not a package-admission claim. It does not authorize new advisor icons or revive blocked identities. Fictional/high-chaos institutional portraits remain on the generated HOI4-style workflow. Historical rows without an accepted source master remain held rather than receiving a generic or generated face.

The old source-locked HOI4 repaint outputs remain in their evidence workspaces for traceability. They are not used as the current runtime input for the rows listed above.
