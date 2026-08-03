# Event 006 grounded source-placeholder manifest

This tranche preserves the original archival source for each grounded historical portrait, records the exact crop metadata, and maps the deterministic `156x210` processed PNG to its runtime DDS. No ImageGen, ComfyUI, repainting, recolouring, or HOI4-style filter was applied. `source_placeholder` is the current manifest state; it does not clear rights, identity, package, or Event 006 admission gates.

The immutable source masters are kept in the single flat archive `docs/assets/portraits/006_independence_wave/`. Crop equality and command metadata live beside the processed candidates in this directory. Runtime DDS files are one-level 156x210 BGRA textures and decode pixel-identically to the processed candidate listed in each row.

| Candidate stem | Durable source master | Crop dimensions | Processed PNG SHA-256 prefix | Runtime DDS | DDS SHA-256 prefix | Status |
| --- | --- | ---: | --- | --- | --- | --- |
| `portrait_ARX_independence_wave_emilio_lussu` | `docs/assets/portraits/006_independence_wave/portrait_ARX_independence_wave_emilio_lussu_source.jpg` | `180x242` | `8569e4f83870edd3` | `portrait_ARX_independence_wave_emilio_lussu.dds` | `106e63fb13d03e6e` | `source_placeholder` |
| `portrait_ARX_luigi_mella_santelia` | `docs/assets/portraits/006_independence_wave/portrait_ARX_luigi_mella_santelia_source.gif` | `143x193` | `9e5dc6d9ac0c6a06` | `portrait_ARX_luigi_mella_santelia.dds` | `746c60bedb76abdb` | `source_placeholder` |
| `portrait_ARX_vittorio_verne` | `docs/assets/portraits/006_independence_wave/portrait_ARX_vittorio_verne_source.jpg` | `186x250` | `00c3dd377d492e82` | `portrait_ARX_vittorio_verne.dds` | `5002742c35a37951` | `source_placeholder` |
| `portrait_ASX_luigi_rizzo` | `docs/assets/portraits/006_independence_wave/portrait_ASX_luigi_rizzo_source.jpg` | `263x354` | `3b486995cda6ce7a` | `portrait_ASX_independence_wave_luigi_rizzo.dds` | `6a5fd9d89e465498` | `source_placeholder` |
| `portrait_ASX_luigi_sturzo` | `docs/assets/portraits/006_independence_wave/portrait_ASX_luigi_sturzo_source.jpeg` | `650x875` | `412218c729f80258` | `portrait_ASX_independence_wave_luigi_sturzo.dds` | `17556fee575b624c` | `source_placeholder` |
| `portrait_ASX_pietro_lanza_di_scalea` | `docs/assets/portraits/006_independence_wave/portrait_ASX_pietro_lanza_di_scalea_source.jpg` | `340x458` | `c625be45fb9dee9b` | `portrait_ASX_independence_wave_pietro_lanza_di_scalea.dds` | `2c36c843b1f3d929` | `source_placeholder` |
| `portrait_ASX_vincenzo_di_benedetto` | `docs/assets/portraits/006_independence_wave/portrait_ASX_vincenzo_di_benedetto_source.gif` | `297x401` | `d97d6d86105d3629` | `portrait_ASX_independence_wave_vincenzo_di_benedetto.dds` | `1b9a19b65673924e` | `source_placeholder` |
| `portrait_BAY_rupprecht_of_bavaria` | `docs/assets/portraits/006_independence_wave/portrait_BAY_rupprecht_of_bavaria_source.jpg` | `1300x1750` | `7d06249c1c0f6828` | `portrait_BAY_rupprecht_of_bavaria.dds` | `00f82253f674cd2a` | `source_placeholder` |
| `portrait_COR_adolphe_landry` | `docs/assets/portraits/006_independence_wave/portrait_COR_adolphe_landry_source.jpg` | `440x592` | `3621bc887e0d8200` | `portrait_COR_independence_wave_adolphe_landry.dds` | `19cc485579d3676c` | `source_placeholder` |
| `portrait_COR_jean_chiappe` | `docs/assets/portraits/006_independence_wave/portrait_COR_jean_chiappe_source.jpg` | `300x404` | `9b8896622e985614` | `portrait_COR_independence_wave_jean_chiappe.dds` | `d6c8543e99721d60` | `source_placeholder` |
| `portrait_DOX_prempeh_ii` | `docs/assets/portraits/006_independence_wave/portrait_DOX_prempeh_ii_source.jpg` | `275x370` | `e4cd9a0f55504f76` | `portrait_DOX_prempeh_ii.dds` | `601e10a85fc67396` | `source_placeholder` |
| `portrait_RHI_josef_friedrich_matthes` | `docs/assets/portraits/006_independence_wave/portrait_RHI_josef_friedrich_matthes_source.jpg` | `386x520` | `51206053ea9e2283` | `portrait_RHI_josef_friedrich_matthes.dds` | `103ceb73f2df2f7a` | `source_placeholder` |
| `portrait_SOK_muhammad_dikko` | `docs/assets/portraits/006_independence_wave/portrait_SOK_muhammad_dikko_source.jpg` | `506x745` | `4b20fe233a58733b` | `portrait_SOK_muhammad_dikko.dds` | `0e74d236149cb689` | `source_placeholder` |
| `portrait_WLS_george_cornwallis_west` | `docs/assets/portraits/006_independence_wave/portrait_WLS_george_cornwallis_west_source.jpg` | `1000x1280` | `971e93bfae40a4a1` | `portrait_WLS_independence_wave_mountain_commandant.dds` | `873bfc5fd3e95fd5` | `source_placeholder` |
| `portrait_WLS_j_h_thomas` | `docs/assets/portraits/006_independence_wave/portrait_WLS_j_h_thomas_source.jpg` | `3000x4000` | `051521fa37d9f681` | `portrait_WLS_independence_wave_national_council.dds` | `7dbd7ceaad173efb` | `source_placeholder` |

The ASX, COR, and WLS runtime names intentionally retain their existing role or institutional sprite names; the candidate stem remains the durable subject name so the source identity is not hidden behind an institutional consumer. The independent row-level crop/provenance audit is recorded separately in `docs/plans/006_independence_wave_plans/subagent_handoffs/006_grounded_portrait_placeholder_audit_2026_08_03.md`.

Full source, crop, processed-PNG, and runtime-DDS hashes are in `SHA256_FULL.txt`.
