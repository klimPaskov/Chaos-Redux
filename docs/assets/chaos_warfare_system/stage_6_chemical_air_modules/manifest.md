# Stage 6 chemical-air module asset manifest

Package scope: nine independently generated aircraft equipment-designer module icons for the exact Chemical Air payload racks.

Counts: 9 source PNGs, 9 processed PNGs, 9 archive DDS files, 9 runtime DDS files, 1 checkerboard contact sheet, 1 prompt record, and 1 GFX handoff.

All source masters were produced through the built-in image-generation workflow in independent generations. Each uses a flat `#ff00ff` processing field and a materially different period dispersal-rack composition. No internet or archival image was used. No icon is a recolor, crop, resize, or cross-type substitute for another asset, and none uses the generic vanilla bomb-lock icon.

## Format contract

- Source masters: `1448x1086` PNG.
- Processed previews: exact `56x42` RGBA PNG with real transparency, matching the inspected vanilla aircraft equipment-module icon surface.
- Runtime and archive DDS: exact `56x42`, 9,536-byte, one-level uncompressed 32-bit BGRA.
- DDS header: 124-byte legacy header; flags `0x0000100F`; pitch `224`; pixel-format flags `0x00000041` (`RGB | ALPHAPIXELS`); masks `R 0x00FF0000`, `G 0x0000FF00`, `B 0x000000FF`, `A 0xFF000000`; `DDSCAPS_TEXTURE`; zero mip levels.
- Runtime directory: `gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air/`.
- Registered GFX file: `interface/chaosx_equipment.gfx`.

## Asset mapping

| Exact module ID | Source PNG | Processed PNG | Archive DDS | Runtime DDS | Sprite ID | Visual identity | Status |
|---|---|---|---|---|---|---|---|
| `chem_air_bomb_chlorine` | `source_png/chem_air_bomb_chlorine.png` | `processed_png/chem_air_bomb_chlorine.png` | `dds_archive/chem_air_bomb_chlorine.dds` | `gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air/chem_air_bomb_chlorine.dds` | `GFX_EMI_chem_air_bomb_chlorine` | Twin cylinders, brass valves, pale green choking plume | complete |
| `chem_air_bomb_phosgene` | `source_png/chem_air_bomb_phosgene.png` | `processed_png/chem_air_bomb_phosgene.png` | `dds_archive/chem_air_bomb_phosgene.dds` | `gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air/chem_air_bomb_phosgene.dds` | `GFX_EMI_chem_air_bomb_phosgene` | Heavy cylinders, protective hood, yellow-green vent | complete |
| `chem_air_bomb_mustard` | `source_png/chem_air_bomb_mustard.png` | `processed_png/chem_air_bomb_mustard.png` | `dds_archive/chem_air_bomb_mustard.dds` | `gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air/chem_air_bomb_mustard.dds` | `GFX_EMI_chem_air_bomb_mustard` | Amber liquid canisters and sealed transfer hose | complete |
| `chem_air_bomb_lewisite` | `source_png/chem_air_bomb_lewisite.png` | `processed_png/chem_air_bomb_lewisite.png` | `dds_archive/chem_air_bomb_lewisite.dds` | `gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air/chem_air_bomb_lewisite.dds` | `GFX_EMI_chem_air_bomb_lewisite` | Angular rack, corroded fittings, amber outlet mist | complete |
| `chem_air_bomb_tabun` | `source_png/chem_air_bomb_tabun.png` | `processed_png/chem_air_bomb_tabun.png` | `dds_archive/chem_air_bomb_tabun.dds` | `gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air/chem_air_bomb_tabun.dds` | `GFX_EMI_chem_air_bomb_tabun` | Sealed lacquered canisters and covered manifold | complete |
| `chem_air_bomb_sarin` | `source_png/chem_air_bomb_sarin.png` | `processed_png/chem_air_bomb_sarin.png` | `dds_archive/chem_air_bomb_sarin.dds` | `gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air/chem_air_bomb_sarin.dds` | `GFX_EMI_chem_air_bomb_sarin` | Streamlined capsules and fine diffuser fan | complete |
| `chem_air_bomb_soman` | `source_png/chem_air_bomb_soman.png` | `processed_png/chem_air_bomb_soman.png` | `dds_archive/chem_air_bomb_soman.dds` | `gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air/chem_air_bomb_soman.dds` | `GFX_EMI_chem_air_bomb_soman` | Three rugged canisters around a central valve block | complete |
| `chem_air_bomb_malodor` | `source_png/chem_air_bomb_malodor.png` | `processed_png/chem_air_bomb_malodor.png` | `dds_archive/chem_air_bomb_malodor.dds` | `gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air/chem_air_bomb_malodor.dds` | `GFX_EMI_chem_air_bomb_malodor` | Squat canisters and oversized perforated diffuser | complete |
| `chem_air_bomb_behavioral` | `source_png/chem_air_bomb_behavioral.png` | `processed_png/chem_air_bomb_behavioral.png` | `dds_archive/chem_air_bomb_behavioral.dds` | `gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air/chem_air_bomb_behavioral.dds` | `GFX_EMI_chem_air_bomb_behavioral` | Small canisters and central vaned diffuser cage | complete |

Paths in the Source, Processed, and Archive columns are relative to this package directory. Generation wording and shared exclusions are preserved in `prompts/chem_air_bomb_prompts.md`. The review sheet is `contact_sheets/stage_6_chemical_air_modules_checkerboard.png` (`630x480`).

## Hash ledger

| Asset ID | Source SHA-256 | Processed SHA-256 | Archive/runtime DDS SHA-256 |
|---|---|---|---|
| `chem_air_bomb_chlorine` | `c057d8d60940b819e046075ea2f62c3ff9cb985315cf364592ee19935bac8af7` | `03a6e923dd7575cf74ab4aa68a9dfa7175eb557ad799c9e360683c8418baa438` | `780c4c16c00a665165568de6dd53465dd4a9a7de70841f49a3c5e4fb3b92e732` |
| `chem_air_bomb_phosgene` | `d9c1a973bb4da04295bdca1df4147e36f5351370043322e5e5156e1f4321cb86` | `5a91cbfe3a571bd83c7cfad41df8c83ff84b0be1ca38bb0650361d9229516a29` | `926bd51b84194d632b044ae1e37403fb231885d9b63ea1ce0d62fd6277768d99` |
| `chem_air_bomb_mustard` | `d29bea8440f5b7c9d6dec23eff1ed1ab044b538ef95eb01bd7f77ece93e18871` | `d1ec41c496960222269684f42cba13b13da6eb0bc4cc626aa817ccd3ac560097` | `5cd4740daaacb84ded29022fc6e49c6bdead8382602b59af76eb64bfa4a8d311` |
| `chem_air_bomb_lewisite` | `0bf73c8bddcf6f159b30905edbb8c8dd07400b2992c4230d9fa4e3d8d8e42ae9` | `5527bd8c13efe9910dd9455c571f2639de633c7ad014fa5720ec2604b978646e` | `c3d704ebd0bee6b7ebda5af4ade810cb6240e83fd81a1d7534c247ba73942d8a` |
| `chem_air_bomb_tabun` | `e00abce32c663021c5017248ba54db1e6f68be6927cbc3a591466049e23d5da6` | `12568cb308ed00b10994804a604ed60d39aa4ff60643759e8a950e23b4a08ae4` | `dd80e7d85134488a7f9827590ccacde49e3db47f6971affd5355a6d7c92b108b` |
| `chem_air_bomb_sarin` | `cfd278a0f8e4bd06e2c6a6516154493329ee9313f83801866833dae59b8f650f` | `3ae524bdf9cd9053f50bd28eb906f6cef01bb5e4749dccd90cf7b57438cdd094` | `55f3a6ea26eaa10239f944c093610353fee5169e80bdd5ee10cbb8a18797a735` |
| `chem_air_bomb_soman` | `c53c888a98ab1b96f7d772d59abf238b49e3f2f42582727be54c00874a8af9ce` | `bfef0dc70fe8a595a3f92b030b2c904e22c7477264f587ca9dec7af80dbce437` | `269976b1de6e1d5bc77678ad4155075b339fe1ec1e7dfc8cad1f5761a4ce376a` |
| `chem_air_bomb_malodor` | `bf3fec981fdadfc617ebbd4010168b50acc4524d2f973d7e00bcb0d2d595ba67` | `45d7263212e6e7439e8c3be72a2029b1109348ab934938fd1b03830b16fcb566` | `46edf94f7c8475f78eb21b75c777840eab50e0b20bb3bef3c888c6e3528547d7` |
| `chem_air_bomb_behavioral` | `0395a65e1507c56ef16eb652b8c0ae5cc97361e7c64733f492ed0c3d503b44b0` | `fc586265816cae6ca74ad1104c2818ee4db41af3d48478e7547f0fce66a4227c` | `f85fef077634a2df9c991c539ba0ebf87effd91f793518c6122c1f47d7653640` |

## Validation evidence

- All nine source, processed, archive, and runtime sets exist.
- Source, processed, and runtime hashes are unique across all nine IDs.
- Every archive/runtime pair is byte-identical.
- Every processed image has both transparent and visible pixels; final processed images contain no opaque chroma-magenta pixels.
- The Lewisite processed image and both DDS copies were regenerated after a one-pixel chroma residue was detected; the final hashes above describe the corrected files.
- Every runtime DDS passed the same magic, dimensions, BGRA masks, pitch, caps, mip-count, and byte-size checks.
- The checkerboard sheet was visually reviewed at original resolution and shows nine distinct readable silhouettes.
- `interface/chaosx_equipment.gfx` contains exactly one matching `GFX_EMI_` declaration per ID and zero generic bomb-lock references in this module family.

## Remaining risk

No asset in this package is blocked. Live game colour management and final aircraft-designer scaling remain part of the wider Stage 14 scenario review. This manifest does not claim the chemical-delivery system or the full Chaos Warfare package complete.
