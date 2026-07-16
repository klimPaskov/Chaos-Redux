# Event 006 male HOI4 portrait tranche: BAY, BRI, RHI, SCO, WLS

Date: 2026-07-16

Status: approved, processed, installed, decoded, and validated.

## Scope

This tranche replaces ten non-approved large portraits and five commander army-small portraits while preserving every existing filename and sprite/effect reference. Every subject is male. The five civic institutions are represented by one fictional male delegate each.

The `_small` files are 65x67 army commander thumbnails/dossiers. They are not political-advisor assets. The canonical `advisor` processor mode is used only because it is the repository's dossier-card renderer; no Event 006 advisor asset was created or edited.

## Installed runtime DDS

| Role | Runtime DDS | SHA-256 |
|---|---|---|
| BAY state council | `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_state_council.dds` | `3ec70cefb21f1d376ecdcf02a4abb68823e6a2aada11b73be7d859f36001d40e` |
| BAY mountain commandant | `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_mountain_commandant.dds` | `c854606389bca79a911ece1aeb79da7c050f560310be763ba2c4c833946de143` |
| BAY mountain commandant army-small | `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_mountain_commandant_small.dds` | `390834ae7f0742a9721f1cfc139bb12eca443061a76f76fca79fd5687a3f7e6a` |
| BRI civic commission | `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_civic_commission.dds` | `f749ffc030798177716f4edd94439e951290ecbded228c4869e621353919b0b6` |
| BRI coastal commandant | `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_coastal_commandant.dds` | `6f928104a5b32d01a2d482fdadc7d03cdfe1f07a35fab6c49899330a668a781c` |
| BRI coastal commandant army-small | `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_coastal_commandant_small.dds` | `ec8b56c40fab15f7037b138fba6389725780c33935b46ec278d8d40d001d1068` |
| RHI provisional directorate | `gfx/leaders/006_independence_wave/portrait_RHI_independence_wave_provisional_directorate.dds` | `23504a0e3cd99773bf920a6d66654d5ea81899330387f088610edaf17a01d801` |
| RHI river commandant | `gfx/leaders/006_independence_wave/portrait_RHI_independence_wave_river_commandant.dds` | `cbfcd9db87d592e57e56898716e2187e9a86c4ffa4c4272f80d017cc7b8797f5` |
| RHI river commandant army-small | `gfx/leaders/006_independence_wave/portrait_RHI_independence_wave_river_commandant_small.dds` | `f395b3ddaa96dde868c0e59d70484c38185026232358d49a096207ad1ba6fba1` |
| SCO civic convention | `gfx/leaders/006_independence_wave/portrait_SCO_independence_wave_civic_convention.dds` | `e9dd04b1d6a70efe5d86649e78cb2aa7990162df008e1b2db1690d24a97b3148` |
| SCO territorial commandant | `gfx/leaders/006_independence_wave/portrait_SCO_independence_wave_territorial_commandant.dds` | `21d4b24f7cf23141f3567bdbf9c0774be1db3a14e1f8c0f876092dedc24fd007` |
| SCO territorial commandant army-small | `gfx/leaders/006_independence_wave/portrait_SCO_independence_wave_territorial_commandant_small.dds` | `cdc2dfe49ce9e1ad0b322810a61a82c842d708a6532a9fd2febac15d5f53e129` |
| WLS national council | `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_national_council.dds` | `2408cf71b36beb0b93e9f7cd0e91c9975d3f93ba83958cc3fe19b661d9ae24e4` |
| WLS mountain commandant | `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_mountain_commandant.dds` | `0b6355779b071ac9bf7a2638b19fbfdbcf7829ac05e7697b24c0d192c7f940f9` |
| WLS mountain commandant army-small | `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_mountain_commandant_small.dds` | `c64f1309de2ea5dcb36a404fcceada2ee2d1ca608b262c8202b1439a2f10c30a` |

## Generation and processing provenance

- The frozen prompt files in `../prompts/` were used verbatim with OpenAI built-in ImageGen. There is one selected generated master for each runtime stem.
- The first RHI river-commandant output attempt was rejected during output moderation and returned no image. The unchanged frozen prompt was retried once; no weaker prompt, substitute source, or fallback was used.
- Large portraits use processor version `4.3`, leader render `2.0`, processor SHA-256 `c300a0acc6ca91beb98d5ae62fcb6c98ad61c39bb7c271491c761295ca11b411`.
- Army-small portraits were rerun consistently from a complete private OS-temp copy of the committed v4.3 bundle. It pinned processor `c300a0ac...`, schema-4 manifest `be1ff82d...`, frame source/overlay `77857264...` / `950596dd...`, and paper source/overlay `5d5f5c76...` / `e5db0602...`. The temporary production directory was removed after processing, then the exact seventeen required Git blobs from commit `6729ad0cd74e0ed294a0b603a0eb677a0533099c` were retained permanently under `../_tooling/v4_3_frozen_inputs/`. All five small metadata records resolve there. The unrelated working v4.4 skill files were not edited or reverted.

## Review and validation evidence

- Large comparison: `contact_sheets/large_processed_contact_sheet.png`.
- Army-small native strip: `contact_sheets/army_small_native_1x.png`.
- Army-small enlarged nearest-neighbour comparison: `contact_sheets/army_small_enlarged_nearest_4x.png`.
- Individual large and army-small review sheets are under `review_sheets/`; every army-small sheet includes the six frozen canonical dossier references.
- Retained DDS files are under `final_dds/`; decoded copies are under `dds_decoded_png/`.
- `validation/validation_report.json` records prompt, raw, processed, metadata, review, DDS, runtime, decoded, processor, overlay, face-placement, alpha, and guard hashes.
- `../hashes/frozen_v4_3_inputs_sha256.sha256` records the permanent processor/input bundle; `../validation/frozen_v4_3_input_resolution.md` records the path repair and independent recheck boundary.
- Every runtime DDS is byte-identical to its retained DDS. Every decoded DDS is pixel-identical to its processed PNG. Large files are 156x210 RGBA8 DDS; army-small files are 65x67 RGBA8 DDS with alpha extrema 0/255 and four transparent corners.

The root agent approved all ten large portraits at target size. The primary Event 006 portrait worker approved all five army-small portraits at native and enlarged size.

## Protected and shared-file guards

- BAY Rupprecht remained byte-identical: `7f0af64fdf4fecd49df454d1198935bb3ce6a8f74afc1ac82f8223704eaaad2b` before and after.
- RHI Josef Friedrich Matthes remained byte-identical: `aa61cc3a12fb6670b690c7685feb9383383ce58599c9e6d6e7c14f20fab3bce2` before and after.
- During production, `docs/assets/006_independence_wave/manifest.md` remained `4a371c23389f84a026d2924e8baae988e0c849d0545341c18934f2bff259983b` and the then-current shared NWE officer-small contact sheet remained `66ee64d97247d5cd2172af5fe0ac2edc1e6c015a34fba25baa118c235019304d`. These were non-mutation guards, not current package dependencies; the accepted documentation promotion and rejected-evidence cleanup supersede both historical snapshots.
- Existing `.gfx` and scripted-effect wiring was inspected and left unchanged.

## Simplifications, omissions, and fallbacks

None.
