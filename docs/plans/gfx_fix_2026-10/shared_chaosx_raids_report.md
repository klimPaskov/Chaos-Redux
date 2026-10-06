# Shared raid icon repairs

Status: the six approved, original raid icon assets are promoted and the three scientist raid sprite leaves are wired to their unique textures. The asset tranche covers all seven `shared_chaosx_raids` findings in the 2026-10 review.

## Findings and dispositions

| Severity | Sprite | Review finding | Disposition |
| --- | --- | --- | --- |
| 2 | `GFX_raid_type_icon_chemical_sarin_rocket_strike` | Reused the same image as Sarin vial raids, so the rocket variant was indistinguishable. | Completed with one compact finned rocket integrated behind a green Sarin vial. |
| 2 | `GFX_raid_type_icon_chemical_soman_rocket_strike` | Byte-identical to the Soman vial icons. | Completed with one compact finned rocket integrated behind an amber Soman vial. |
| 3 | `GFX_raid_type_icon_chemical_soman_strike` | Differed from Sarin by only two pixels and read as the same green-glow vial. | Completed with amber liquid inside dark glass and no external aura. |
| 2 | `GFX_raid_category_small_brilliant_scientist_raids` | Used the biological raid biohazard medallion. | Completed with an original microscope-and-atom scientist medallion; parent GFX leaf points to the new shared texture. |
| 2 | `GFX_raid_unit_icon_brilliant_scientist_raids` | Reused the biological raid medallion. | Completed with the same purpose-built scientist medallion; parent GFX leaf points to the new shared texture. |
| 2 | `GFX_raid_type_icon_brilliant_scientist_portal_facility_raid` | Used the biological facility preserve icon. | Completed with a distinct laboratory gate and portal; parent GFX leaf points to a new unique texture. |
| 3 | `GFX_raid_type_icon_zombie_cure_strike` | Read nearly the same as the weaponized-zombie green vial. | Completed with a frosted medicine vial and pale-blue cross. |

## Sources and final files

All six subjects were generated with the official ImageGen skill with genuine transparency requested in the initial call. The native requests are preserved verbatim in the prompt files; the manifest includes their prompt text and SHA-256, each source and processed hash, exact canvases, visible bounds, alpha measurements, runtime paths, and bindings.

| Subject | Native source and SHA-256 | Processed PNG and SHA-256 | Final runtime DDS and SHA-256 |
| --- | --- | --- | --- |
| Sarin rocket | [source](../../assets/gfx_fix_2026-10/shared_chaosx_raids/source_pngs/raid_sarin_rocket.png), `443458bbefab96c7a8aee29a701e70c06e351a714f0e791c96cf64a2abb0fc47`; [prompt](../../assets/gfx_fix_2026-10/shared_chaosx_raids/prompts/raid_sarin_rocket.md) | [processed](../../assets/gfx_fix_2026-10/shared_chaosx_raids/processed_pngs/raid_sarin_rocket.png), `bb99bd0b98866c1b643302b2175b019747884ba7c36d654d68f7f39c399e1b99` | `gfx/interface/military_raids/map_icons/raid_type_icon_chemical_sarin_rocket_strike.dds`, `43538b3f54708937f76b6bb405e11853c32f120a7b9d01709e1bbaac0557438b` |
| Soman rocket | [source](../../assets/gfx_fix_2026-10/shared_chaosx_raids/source_pngs/raid_soman_rocket.png), `83c232f121bb6baa1d77239e37d6d08ed83eaab35ee3dd7e21087b78ad3d7f87`; [successful prompt](../../assets/gfx_fix_2026-10/shared_chaosx_raids/prompts/raid_soman_rocket.md) | [processed](../../assets/gfx_fix_2026-10/shared_chaosx_raids/processed_pngs/raid_soman_rocket.png), `7828a3581bae623bc2f563fd8ccb3de3ecf124fc7a88bac4fab9ab569aa97007` | `gfx/interface/military_raids/map_icons/raid_type_icon_chemical_soman_rocket_strike.dds`, `439e4b319dc76abde15897aa9889fcdf1a932e5885fb0e9f0c710557d9447c6e` |
| Soman vial | [source](../../assets/gfx_fix_2026-10/shared_chaosx_raids/source_pngs/raid_soman_strike.png), `a1f199a8c30886005e78664152d4711a7c80e8d184eaddbff6da982e1fbc3b52`; [prompt](../../assets/gfx_fix_2026-10/shared_chaosx_raids/prompts/raid_soman_strike.md) | [processed](../../assets/gfx_fix_2026-10/shared_chaosx_raids/processed_pngs/raid_soman_strike.png), `68fa7545b46a34942f50b07bc8688df5a5a6ed2caf1fe45183da44cca4de974a` | `gfx/interface/military_raids/map_icons/raid_type_icon_chemical_soman_strike.dds`, `ba2cdf646092dfad903fa9c88de0cda795ca6bdb26565e2adafd6cfafd4b81aa` |
| Scientist medallion | [source](../../assets/gfx_fix_2026-10/shared_chaosx_raids/source_pngs/raid_brilliant_scientist_medallion.png), `551fcbeabc20c447d99828715b9db840f1da90b49fe2cc5940eaad5214a73893`; [prompt](../../assets/gfx_fix_2026-10/shared_chaosx_raids/prompts/raid_brilliant_scientist_medallion.md) | [processed](../../assets/gfx_fix_2026-10/shared_chaosx_raids/processed_pngs/raid_brilliant_scientist_medallion.png), `c14b9d16967fa92aacf3940e403139f25292fba82a614c833e6c2922708e6268` | `gfx/interface/military_raids/map_icons/raid_unit_icon_brilliant_scientist_raids.dds`, `3b51e10f892f90fc2013b11158a8cc5e2f54b522d8fa867f65e74a7d9b6c3113` |
| Portal facility | [source](../../assets/gfx_fix_2026-10/shared_chaosx_raids/source_pngs/raid_portal_facility.png), `577af58abd2be8d0d6ca90d4517f0d4ec825ca4af483faee8a3d5c35c15ab7af`; [prompt](../../assets/gfx_fix_2026-10/shared_chaosx_raids/prompts/raid_portal_facility.md) | [processed](../../assets/gfx_fix_2026-10/shared_chaosx_raids/processed_pngs/raid_portal_facility.png), `9168ce63299812fe2fb516403fd624e411182642ea653743932dcf255e5f5283` | `gfx/interface/military_raids/map_icons/raid_type_icon_brilliant_scientist_portal_facility_raid.dds`, `da24224a5dc51f7722ac2728d6056a68fb61de1ff519eb4c55eecb2861293f79` |
| Zombie cure | [source](../../assets/gfx_fix_2026-10/shared_chaosx_raids/source_pngs/raid_zombie_cure.png), `57457549613b576a8cd39dd8f05dcfae9d590c0886dad3e7b2657e2ea4fbae3b`; [prompt](../../assets/gfx_fix_2026-10/shared_chaosx_raids/prompts/raid_zombie_cure.md) | [processed](../../assets/gfx_fix_2026-10/shared_chaosx_raids/processed_pngs/raid_zombie_cure.png), `f02dc4efb8748ea199129c4e93304fcb2190659b773826cc4497e2f9419f136a` | `gfx/interface/military_raids/map_icons/raid_type_icon_zombie_cure_strike.dds`, `005d90b6c8d967dac976d7fcb11cba2d86ced9795a7a3e43f5fb516846316199` |

The rocket and cure sources have real alpha with transparent canvas pixels; all processed previews are 32x32 with preserved alpha. There was no background-removal fallback. The initial Soman rocket request was blocked by ImageGen moderation; the blocked request is retained in `prompts/raid_soman_rocket_initial_blocked.md`, and the selected image came from the preserved successful retry rather than a reconstructed prompt.

## Reference and validation evidence

Before generation, the canonical `icons/military_raids/contact_sheet.png` was inspected, followed by its airfield, dam-bombing, port, land-infiltration, naval-commando, and nuclear raid references. The canonical family directory is `.agents/skills/chaos-redux-event-assets/assets/gfx_references/icons/military_raids/`; exact reference-file hashes are recorded in the group manifest.

Installed vanilla comparison assets were read from `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/military_raids/map_icons/`. Their definitions were read in `interface/military_raids/military_raids.gfx`, including the unit sprites around lines 83-96 and raid-type sprites around lines 281-323. The exact installed definition paths, DDS hashes, dimensions, and visible bounds are preserved in `manifest.json` and `evidence/installed_vanilla_reference_alpha.json`.

The parent reviewed and approved all six sources in the native-size and 4x comparison sheets: [before/after, native](../../assets/gfx_fix_2026-10/shared_chaosx_raids/evidence/raids_before_after_native.png) and [before/after, 4x](../../assets/gfx_fix_2026-10/shared_chaosx_raids/evidence/raids_before_after_4x.png). Parent review confirmed that Sarin and Soman rocket glyphs remain distinct, the Soman vial and cure have different silhouettes, and the portal and scientist symbols read at 32px.

Every final DDS passed the strict BGRA header check and decoded pixel-equal to its 32x32 processed PNG. A fresh canonical BGRA reconversion independently matched the candidate bytes and hashes; these results are in `evidence/strict_dds_validation.json` and `evidence/canonical_reconversion_report.json`. Existing live files were promoted only after matching their frozen baseline SHA-256; previously absent unique paths were required to be absent. The old bytes are preserved under `evidence/runtime_before_promotion/`, and the promotion receipt records before/after hashes.

The review workspace already contained candidate DDS files before the packaging converter was attempted, so those files were not overwritten. Their strict decode, pixel equality, and exact match to the independent canonical reconversion were verified. A subsequent converter attempt refused the existing candidate paths as designed; the refusal is preserved in `evidence/dds_conversion_refused_existing.json` and is not a failed asset conversion.

## Runtime handoff and limits

Parent updated and confirmed these leaves in `interface/chaosx_raids.gfx`: `GFX_raid_category_small_brilliant_scientist_raids` and `GFX_raid_unit_icon_brilliant_scientist_raids` both use `gfx/interface/military_raids/map_icons/raid_unit_icon_brilliant_scientist_raids.dds`, while `GFX_raid_type_icon_brilliant_scientist_portal_facility_raid` uses `gfx/interface/military_raids/map_icons/raid_type_icon_brilliant_scientist_portal_facility_raid.dds`. Sarin rocket, Soman rocket, Soman vial, and zombie cure retain their existing leaves and filenames; their texture bytes were replaced at those exact paths.

No raid definitions, costs, outcomes or localization files were changed by the asset worker.
The parent changed only the three texture leaves described above.
The user retains live-game visual validation; no game was launched here.
The HOI4 MCP transport is closed, so this report makes no engine-render claim.
