# Event 012 shared elephant 3D-model handoff — 2026-08-05

Package root: `docs/assets/012_africa/models_3d/elephant_shared_base/`.

## Produced package

- Mesh: `exports/elephant_shared_base.mesh`, SHA-256 `6C3B53731646C3F57F56D26AFE5E4F7215C3E034469AD04179A3F0A70F4D5988`, 44,908 triangles.
- Actions: `elephant_idle`, `elephant_move`, `elephant_deploy`, `elephant_supply_load`, `elephant_attack`, and `elephant_impact` under `exports/anim/`; all six have JSON and Blender reimport proofs under `validation/` and `blender/checkpoints/`.
- Scale: vanilla rider target `5.8814594268` effective runtime height at entity scale `0.8`; exported elephant source height `33.5147094727`.
- Rig: custom 17-bone nonhumanoid elephant skeleton. The fused provider shell required explicit recorded semantic spatial segmentation.
- Textures: packed PDX runtime maps `exports/elephant_shared_base_diff.dds`, `exports/elephant_shared_base_spec.dds`, and `exports/elephant_shared_base_n.dds`; provider/processed evidence remains under `textures/`.
- Counter companion: `gfx/interface/counters/divisions_large/unit_elephant_shared_base_icon.dds` (SHA-256 `5D455DC3268BE89451D967E187FD5AAA8D6966C9A82FF8AE933208DF2201A21E`) and `gfx/interface/counters/divisions_small/onmap_unit_elephant_shared_base_icon.dds` (SHA-256 `6E2AC8B322F4FE1D6D126E1B02727BE721B83FD4EEC5788D6B9D0AB083188BDD`), both two-frame land-counter assets.
- Provider lineage: Meshy task `019fd212-8909-765a-a4f0-70294b8ff7f3`; estimated 20 credits, actual 30; no further paid calls.
- Locked environment: Meshy MCP `0.4.0`, adapter `1.2.0`, Blender `5.1.2` build `ec6e62d40fa9`, io_pdx_mesh `0.91.0` with archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`.

## Complete sourced sound package

All six required sound roles are covered by preserved CC0/public-domain originals and mechanically derived WAV candidates. No audio was generated or synthesized.

- `movement` and `impact`: public-domain `Dull Thud` by gregoryweir, original SHA-256 `5B91906D41BD57F1F6551E446D30FBFF06EC59A39D22725140293EF4AEC6CDB3`.
- `creature_idle`, `attack`, and `death_or_disappearance`: CC0 `Elephant voice - trumpeting`, original SHA-256 `E5F3120E5EACA87CC080BBF57BD185C96D52FD0F63CC1DFE33228C8BFA29F3BC`.
- `special_supply_load`: public-domain `Squeaky door` by leonmire, original SHA-256 `B60B97C3F73C9754FC36B58CEA4862D50FF800F12632C9B55BC6F8132E93D9C5`; derived candidate `evidence/audio/derived/elephant_supply_load_creak.wav`, SHA-256 `00F6473ED59DF603434B3B80521373CFC8D5F09EA2EA42D8D56A5992640CC35A`, synchronized to frame 20.
- Full source pages, direct-download URLs, authors, licenses, usage terms, transformations, hashes, and synchronization points: `evidence/audio/source_urls.json`, `evidence/audio/audio_manifest.json`, and `evidence/audio/sound_design_handoff.md`.
- The first public-domain casket candidate remains documented as a rejected HTTP 429 download; it is not used.

## Dormant handoff status

- Parent-owned runtime copies and registrations now exist under `gfx/models/units/chaosx_elephants/`, `gfx/entities/chaosx_elephants.gfx`, `gfx/entities/chaosx_elephants.asset`, and `sound/chaosx_elephants_sound.asset`; no unit-template or country-tag changes were made. Per the current Event 012 direction, the package remains intentionally dormant and has no live unit consumer.
- The bespoke large and on-map counter DDS files are copied under `gfx/interface/counters/divisions_large/` and `gfx/interface/counters/divisions_small/`, with their `noOfFrames = 2` sprite registrations in `interface/chaosx_subuniticons.gfx`.
- The exported semantic partition reports 4,998 boundary edges, although it reports no degenerate or non-manifold faces. Keep this as a topology review item.
- The single shared export has the cargo/howdah silhouette by approved design; logistics and shock use one shared body, action set, texture set, and counter package.
- Parent owns any future runtime hash synchronization, `.asset`/entity/animation/material/sound/soundeffect/unit-template wiring, and live in-game validation if the dormant package is later approved for use.
- No gameplay, GFX, entity, sound-definition, localisation, or spreadsheet file was edited. This package does not claim in-game completion.
