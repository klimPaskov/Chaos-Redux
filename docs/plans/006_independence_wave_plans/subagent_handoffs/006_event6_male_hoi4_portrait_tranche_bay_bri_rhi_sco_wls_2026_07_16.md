# Event 006 male HOI4 portrait tranche handoff: BAY, BRI, RHI, SCO, WLS

Date: 2026-07-16

Owner: `/root/asset_reference_audit`

Status: tranche complete and ready for the primary Event 006 portrait merge

## Delivered scope

Produced, processed, installed, decoded, and validated ten male large portraits:

- BAY state council and mountain commandant
- BRI civic commission and coastal commandant
- RHI provisional directorate and river commandant
- SCO civic convention and territorial commandant
- WLS national council and mountain commandant

Produced the five matching commander `_small` 65x67 army thumbnails/dossiers. These are army portraits, not political-advisor assets. No Event 006 advisor asset, sprite, portrait block, gameplay definition, or localisation was created or edited.

## Files and evidence

- Frozen prompts: `docs/assets/006_independence_wave/portrait_regeneration_male_hoi4_2026_07_16/prompts/`
- Ten selected raw ImageGen masters: `docs/assets/006_independence_wave/portrait_regeneration_male_hoi4_2026_07_16/raw_outputs/`
- Ten processed 156x210 PNGs: `docs/assets/006_independence_wave/portrait_regeneration_male_hoi4_2026_07_16/processed_png/`
- Five processed 65x67 army-small PNGs: `docs/assets/006_independence_wave/portrait_regeneration_male_hoi4_2026_07_16/small_processed_png/`
- Tranche-only manifest, contact sheets, individual review sheets, processor metadata, retained DDS files, decoded DDS PNGs, hashes, and validation: `docs/assets/006_independence_wave/portrait_regeneration_male_hoi4_2026_07_16/tranche_bay_bri_rhi_sco_wls/`
- Machine-readable validation: `docs/assets/006_independence_wave/portrait_regeneration_male_hoi4_2026_07_16/tranche_bay_bri_rhi_sco_wls/validation/validation_report.json`

The installed runtime files are the ten matching large `.dds` files and five commander `_small.dds` files under `gfx/leaders/006_independence_wave/`. Existing filenames, `.gfx` sprite names, and scripted-effect portrait references were preserved without edits.

## Runtime hashes

| File stem | Large SHA-256 | Army-small SHA-256 |
|---|---|---|
| `portrait_BAY_independence_wave_state_council` | `3ec70cefb21f1d376ecdcf02a4abb68823e6a2aada11b73be7d859f36001d40e` | — |
| `portrait_BAY_independence_wave_mountain_commandant` | `c854606389bca79a911ece1aeb79da7c050f560310be763ba2c4c833946de143` | `390834ae7f0742a9721f1cfc139bb12eca443061a76f76fca79fd5687a3f7e6a` |
| `portrait_BRI_independence_wave_civic_commission` | `f749ffc030798177716f4edd94439e951290ecbded228c4869e621353919b0b6` | — |
| `portrait_BRI_independence_wave_coastal_commandant` | `6f928104a5b32d01a2d482fdadc7d03cdfe1f07a35fab6c49899330a668a781c` | `ec8b56c40fab15f7037b138fba6389725780c33935b46ec278d8d40d001d1068` |
| `portrait_RHI_independence_wave_provisional_directorate` | `23504a0e3cd99773bf920a6d66654d5ea81899330387f088610edaf17a01d801` | — |
| `portrait_RHI_independence_wave_river_commandant` | `cbfcd9db87d592e57e56898716e2187e9a86c4ffa4c4272f80d017cc7b8797f5` | `f395b3ddaa96dde868c0e59d70484c38185026232358d49a096207ad1ba6fba1` |
| `portrait_SCO_independence_wave_civic_convention` | `e9dd04b1d6a70efe5d86649e78cb2aa7990162df008e1b2db1690d24a97b3148` | — |
| `portrait_SCO_independence_wave_territorial_commandant` | `21d4b24f7cf23141f3567bdbf9c0774be1db3a14e1f8c0f876092dedc24fd007` | `cdc2dfe49ce9e1ad0b322810a61a82c842d708a6532a9fd2febac15d5f53e129` |
| `portrait_WLS_independence_wave_national_council` | `2408cf71b36beb0b93e9f7cd0e91c9975d3f93ba83958cc3fe19b661d9ae24e4` | — |
| `portrait_WLS_independence_wave_mountain_commandant` | `0b6355779b071ac9bf7a2638b19fbfdbcf7829ac05e7697b24c0d192c7f940f9` | `c64f1309de2ea5dcb36a404fcceada2ee2d1ca608b262c8202b1439a2f10c30a` |

## ImageGen and visual review

- Every selected master was produced with the exact frozen prompt and built-in ImageGen. There is one selected master per stem.
- The first RHI river-commandant output attempt was rejected during output moderation and produced no image. The identical prompt was retried once; there was no prompt rewrite, substitute source, or fallback.
- Root reviewed the ten-target large contact sheet and approved all ten as male, distinct, period-correct, target-size readable, and convincingly vanilla-HOI4 painterly.
- `/root/mediterranean_packages` reviewed the five native/enlarged army-small outputs and approved identity, readability, and consistent canonical frame/paper treatment.

## Processor pin and shared-tool race resolution

The large outputs were processed with committed processor v4.3 (`c300a0acc6ca91beb98d5ae62fcb6c98ad61c39bb7c271491c761295ca11b411`), leader render v2.0.

An unrelated uncommitted v4.4 processor/paper change appeared in the shared skill directory during the small-portrait tranche. Per root direction, all five army-small portraits were rerun from one complete private OS-temp bundle copied from committed HEAD:

- processor/render: `4.3` / `4.3`
- processor: `c300a0acc6ca91beb98d5ae62fcb6c98ad61c39bb7c271491c761295ca11b411`
- schema-4 overlay manifest: `be1ff82d3f460ca1e0572ff3cb23853fdd87d2a0a8444f20cdad6565cacd2d2f`
- frame source/overlay: `77857264f8f6e36c75c675969f73e5ba5ee936f38599c6d843e2e07c527c0740` / `950596dd88da0b58861af9e58cacdaa80b2e6308af9168dd98ad390ae42aea79`
- paper source/overlay: `5d5f5c76e0a290c848cc71e8ff8f102a87e47227d32c9902350bc7f1eb00d491` / `e5db0602b4b5d82ba148552bfa2a6c7b6e00c6a91137de2b3baec404535210a0`

All five metadata records report those committed values. The private temp directory was removed after the run. The exact seventeen required v4.3 Git blobs are retained permanently under `docs/assets/006_independence_wave/portrait_regeneration_male_hoi4_2026_07_16/_tooling/v4_3_frozen_inputs/`, and all five metadata records now resolve there. The working v4.4 tool, manifest, and paper files were left untouched.

## Validation and guards

- All ten large retained/runtime DDS pairs are byte-identical and are 156x210 uncompressed RGBA8 DDS.
- All five army-small retained/runtime DDS pairs are byte-identical and are 65x67 uncompressed RGBA8 DDS.
- Every decoded DDS is pixel-identical to its processed PNG.
- Every army-small output has alpha extrema 0/255 and four fully transparent corners. The individual review sheets compare each output with all six frozen canonical advisor/army-small dossier references.
- BAY Rupprecht stayed byte-identical at `7f0af64fdf4fecd49df454d1198935bb3ce6a8f74afc1ac82f8223704eaaad2b`.
- RHI Josef Friedrich Matthes stayed byte-identical at `aa61cc3a12fb6670b690c7685feb9383383ce58599c9e6d6e7c14f20fab3bce2`.
- The shared Event 006 asset manifest and shared NWE small contact sheet retained their pre-tranche hashes. They were not edited.

## Remaining risks and blockers

None within this tranche. The unrelated working v4.4 skill changes remain owned outside this handoff and were deliberately neither reverted nor incorporated.

## Simplifications, omissions, and fallbacks

None.

## Skills used

- `imagegen`
- `chaos-redux-event-assets`
- `chaos-redux-subagents`
