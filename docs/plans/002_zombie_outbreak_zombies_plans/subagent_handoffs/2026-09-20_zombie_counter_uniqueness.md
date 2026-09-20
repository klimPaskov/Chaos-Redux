# Zombie counter uniqueness handoff

Status: `implemented` for bounded asset production and `needs_user_review` for parent visual and live consumer review.

## Ownership and scope

This handoff repairs the five duplicate zombie-family large and map counter pairs named by the parent task.

The original affected hashes were large `6409846e58734fa198ff1d1d6b37863c65fb058fafe16e6f47e66cd0fd1ac291` and small `8eafd2bf7b2fb65ea48e0be01e5d5741b4f5db2bcad0302c409da7130e5d3623`.

The existing base zombie counter remains accepted and was not changed.

Texticon aliases, chemical tank aliases, Livens aliases, gameplay, GFX, GUI, model, entity, and sound files remain outside this bounded ownership.

## Changed runtime files

The following ten runtime files were replaced with unique strict BGRA DDS outputs.

| Runtime path | Dimensions | SHA-256 |
| --- | ---: | --- |
| `gfx/interface/counters/divisions_large/unit_wendigo_zombies_icon.dds` | `152x42` | `207a131b7e91285ceb2baf8580390666c2eed18e17e47be7e10b812060656f82` |
| `gfx/interface/counters/divisions_small/onmap_unit_wendigo_zombies_icon.dds` | `60x12` | `c93b567cd639d058d85bc3d6e9dc08372f4cd49dfd733094e15bd90a67538e2e` |
| `gfx/interface/counters/divisions_large/unit_armored_undead_zombies_icon.dds` | `152x42` | `87eb099646c9cd688da9282338d0f9699da5775aa5fdcd4f221898e2e31efe46` |
| `gfx/interface/counters/divisions_small/onmap_unit_armored_undead_zombies_icon.dds` | `60x12` | `ce8de32af63d4c2fa1852161b39a2782d8176677f81613af8cab9e8765340c99` |
| `gfx/interface/counters/divisions_large/unit_armored_necrotic_zombies_icon.dds` | `152x42` | `c7a46d4b9d4f0c20a85dd8010a4000a172a2572cf6463bd4954bff486324ef95` |
| `gfx/interface/counters/divisions_small/onmap_unit_armored_necrotic_zombies_icon.dds` | `60x12` | `d409196fa33bab49bef02c34761c53d4ae7b9e32adb3dbd7f84e3e8b670240df7` |
| `gfx/interface/counters/divisions_large/unit_armored_demonic_zombies_icon.dds` | `152x42` | `df9c485843a6ff4e078d3323d51169fac024982f2af983d64aadee860d5a80c0` |
| `gfx/interface/counters/divisions_small/onmap_unit_armored_demonic_zombies_icon.dds` | `60x12` | `0a9b389ffd5e965cc634ad98a678d32ab5536aea104c66ff152d3297e3c44cc4` |
| `gfx/interface/counters/divisions_large/unit_armored_wendigo_zombies_icon.dds` | `152x42` | `7807948ab934ef1ade75e8c01a4049b8f99297b5722aeff08c52aec618631422` |
| `gfx/interface/counters/divisions_small/onmap_unit_armored_wendigo_zombies_icon.dds` | `60x12` | `6e583c72ed86ef19c9b1a800d26ca3576325665ee0c0fc2a66b439815f3a0ff7` |

No `interface/chaosx_subuniticons.gfx` edit was needed because the existing sprite names and paths already target these files.

## Production evidence

Native ImageGen source PNGs are in `docs/assets/002_zombie_outbreak/models_3d/zombie_counter_uniqueness/source_png/`.

The source prompt record is `docs/assets/002_zombie_outbreak/models_3d/zombie_counter_uniqueness/prompts/zombie_counter_uniqueness_prompts.md`.

Processed per-frame PNGs and exact two-frame strips are in `docs/assets/002_zombie_outbreak/models_3d/zombie_counter_uniqueness/processed_png/`.

The manifest and asset handoff are `docs/assets/002_zombie_outbreak/models_3d/zombie_counter_uniqueness/manifest.md` and `docs/assets/002_zombie_outbreak/models_3d/zombie_counter_uniqueness/gfx_handoff.md`.

The large and small comparison sheets are `docs/assets/002_zombie_outbreak/models_3d/zombie_counter_uniqueness/contact_sheets/zombie_counter_uniqueness_large.png` and `docs/assets/002_zombie_outbreak/models_3d/zombie_counter_uniqueness/contact_sheets/zombie_counter_uniqueness_small.png`.

## Validation evidence

The final DDS files were made with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`.

The strict DDS validator confirmed 32-bit uncompressed BGRA headers, exact `152x42` and `60x12` dimensions, alpha min/max preservation, and exact pixel equality after decoding each DDS back to RGBA against its processed PNG.

All ten affected DDS files have unique hashes within their size family.

The full runtime zombie counter audit found twelve unique large files and thirteen unique small files with no duplicate groups remaining.

The machine-readable evidence is in `docs/assets/002_zombie_outbreak/models_3d/zombie_counter_uniqueness/validation/dds_validation.json`, `processing_metrics.json`, and `file_hashes.json`.

## Remaining review and risks

Parent review should confirm the contact sheets against the intended unit identities and inspect the unchanged existing GFX definitions.

The normal large frames use the sampled vanilla green palette anchored at `#496a49`, while alternate large and map frames use the sampled pale and neutral vanilla family palettes.

The armored undead and armored necrotic small sources were regenerated after the first processing pass because the first silhouettes were too narrow for the `30x12` map frame.

The generated art is original and transparent, but the user still owns final live in-game readability review.
