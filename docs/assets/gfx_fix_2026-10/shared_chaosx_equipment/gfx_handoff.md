# Shared equipment asset handoff

Status: Seven wide cylinders and seven tank shells (14 DDS textures) are promoted in the shared worktree and the parent has wired all 28 corresponding GFX leaves. The parent has not yet supplied the commit hash. The separate 27-variant chemical-air row has parent-approved native and processed art but still needs canonical DDS conversion, round-trip QA, and guarded replacement.

## Cylinder and shell paths

| Agent | Asset | Runtime DDS | SHA-256 | Sprite leaf or aliases |
| --- | --- | --- | --- | --- |
| Chlorine | Cylinder, 131x52 | `gfx/interface/technologies/equipment_wide/chemical_chlorine_payload_cylinder.dds` | `6c271520fad7190f139fab0a4729ca27f2c9d33b59c9118d7c67c8574b0ea7b8` | `GFX_chemical_chlorine_payload_cylinder`, `GFX_chemical_chlorine_payload_cylinder_medium`, `GFX_chemical_chlorine_payload_cylinder_1_medium` |
| Phosgene | Cylinder, 131x52 | `gfx/interface/technologies/equipment_wide/chemical_phosgene_payload_cylinder.dds` | `9a343a42393b5faf5b59c80f6a1d5fb08f145c097ff7667b6d6e274b8e147521` | `GFX_chemical_phosgene_payload_cylinder`, `GFX_chemical_phosgene_payload_cylinder_medium`, `GFX_chemical_phosgene_payload_cylinder_1_medium` |
| Mustard | Cylinder, 131x52 | `gfx/interface/technologies/equipment_wide/chemical_mustard_payload_cylinder.dds` | `57e5072af7949476db0b3dd404bd9fa91ccaf47abcb73d695f5c1d6c4f448b94` | `GFX_chemical_mustard_payload_cylinder`, `GFX_chemical_mustard_payload_cylinder_medium`, `GFX_chemical_mustard_payload_cylinder_1_medium` |
| Lewisite | Cylinder, 131x52 | `gfx/interface/technologies/equipment_wide/chemical_lewisite_payload_cylinder.dds` | `d102e2ea8aa789d91941f4dbaa35b8afa4691b74a4abc07657bd60500fae380c` | `GFX_chemical_lewisite_payload_cylinder`, `GFX_chemical_lewisite_payload_cylinder_medium`, `GFX_chemical_lewisite_payload_cylinder_1_medium` |
| Tabun | Cylinder, 131x52 | `gfx/interface/technologies/equipment_wide/chemical_tabun_payload_cylinder.dds` | `a39aef4d88503ed09fd8b7bdb83c51dcabcb1495a433904bb050f8f679397cfc` | `GFX_chemical_tabun_payload_cylinder`, `GFX_chemical_tabun_payload_cylinder_medium`, `GFX_chemical_tabun_payload_cylinder_1_medium` |
| Sarin | Cylinder, 131x52 | `gfx/interface/technologies/equipment_wide/chemical_sarin_payload_cylinder.dds` | `a26d85f0a769950f849adeae0844e5071b96a43497c54e50787b518b5a992145` | `GFX_chemical_sarin_payload_cylinder`, `GFX_chemical_sarin_payload_cylinder_medium`, `GFX_chemical_sarin_payload_cylinder_1_medium` |
| Soman | Cylinder, 131x52 | `gfx/interface/technologies/equipment_wide/chemical_soman_payload_cylinder.dds` | `0e690764722b58438ddebc2e633567d9e0477a2398f37d1307b14a9a6565da17` | `GFX_chemical_soman_payload_cylinder`, `GFX_chemical_soman_payload_cylinder_medium`, `GFX_chemical_soman_payload_cylinder_1_medium` |
| Chlorine | Tank shell, 70x43 | `gfx/interface/equipmentdesigner/tanks/modules/chemical_tank_shells/tank_module_chemical_shell_chlorine.dds` | `4010d340ec65ff2d6367e98ecb7ad6914ba3758dc298d46b1dc3e4e1c6dba1c0` | `GFX_EMI_chemical_tank_shell_chlorine` |
| Phosgene | Tank shell, 70x43 | `gfx/interface/equipmentdesigner/tanks/modules/chemical_tank_shells/tank_module_chemical_shell_phosgene.dds` | `d11300bd48bab88b2e8b42b9cb0d977a9f92e1e4c951a54f69a53676c74374ec` | `GFX_EMI_chemical_tank_shell_phosgene` |
| Mustard | Tank shell, 70x43 | `gfx/interface/equipmentdesigner/tanks/modules/chemical_tank_shells/tank_module_chemical_shell_mustard.dds` | `4f0dd58a55f0ed53277c33f0f00c9d301add610a7d897a3cc9de5a5982520e9d` | `GFX_EMI_chemical_tank_shell_mustard` |
| Lewisite | Tank shell, 70x43 | `gfx/interface/equipmentdesigner/tanks/modules/chemical_tank_shells/tank_module_chemical_shell_lewisite.dds` | `41e0ef1fd28d0b235c6fdb1bcb10ac88787ab25cefe93ccb7f05ff3166494101` | `GFX_EMI_chemical_tank_shell_lewisite` |
| Tabun | Tank shell, 70x43 | `gfx/interface/equipmentdesigner/tanks/modules/chemical_tank_shells/tank_module_chemical_shell_tabun.dds` | `ca27dd6436f01423a3bec9148d2d3fa38ee9a51b0358fa14d6d747c493873f6f` | `GFX_EMI_chemical_tank_shell_tabun` |
| Sarin | Tank shell, 70x43 | `gfx/interface/equipmentdesigner/tanks/modules/chemical_tank_shells/tank_module_chemical_shell_sarin.dds` | `8b647b3f174bbb6fd35120459b94939bb8bca926619fbb35bfb93fa34995e469` | `GFX_EMI_chemical_tank_shell_sarin` |
| Soman | Tank shell, 70x43 | `gfx/interface/equipmentdesigner/tanks/modules/chemical_tank_shells/tank_module_chemical_shell_soman.dds` | `cadb86288c244c88914da082872285d7452603bfca91663a01555b289661d48a` | `GFX_EMI_chemical_tank_shell_soman` |

## Lineage and QA

The full 14-asset manifest records every exact prompt, native source path/hash, processed preview path/hash, reference path/hash, target DDS path/hash, palette evidence, promotion receipt, and GFX leaf mapping: [equipment_shared_14_cylinders_tank_shells_manifest.json](evidence/equipment_shared_14_cylinders_tank_shells_manifest.json). The parent wiring snapshot confirms 21 cylinder aliases and seven tank-shell leaves in `interface/chaosx_equipment.gfx`: [equipment_shared_14_gfx_wiring_snapshot.json](evidence/equipment_shared_14_gfx_wiring_snapshot.json).

All 14 runtime DDS files pass the alpha/dimension audit and match their selected processed PNG pixels exactly after decode: [equipment_shared_14_runtime_alpha.json](evidence/equipment_shared_14_runtime_alpha.json). The tank-shell canonical conversion report and absence-guard promotion receipt are [here](evidence/tank_shell_candidate_dds_conversion.json) and [here](evidence/tank_shell_promotion_receipt.json). The cylinder canonical conversion receipts and protected research overlap checks remain in [the wide-cylinder manifest](evidence/equipment_wide_cylinders_manifest.json).

The exact installed vanilla tank-module references are recorded with hashes in [vanilla_tank_module_reference_paths.json](evidence/vanilla_tank_module_reference_paths.json), and the exact protected research palette anchors are in [chemical_cylinder_research_palette_map.json](evidence/chemical_cylinder_research_palette_map.json). The parent-approved shell visual review is [native](evidence/tank_shell_palette_reconciled_native.png) and [4x](evidence/tank_shell_palette_reconciled_4x.png).

## Separate chemical-air tranche

All 27 native sources and 56x42 previews are parent-approved, but their existing DDS targets remain untouched pending the separate conversion and hash-guarded promotion pass. Their complete prompt/source/baseline record is [chem_air_variants_27_progress_manifest.json](evidence/chem_air_variants_27_progress_manifest.json); review sheets for batches 1–7 sit alongside it. The protected technology 64x64 research textures, equipment costs, module stats, combat behavior, localization, and gameplay remain unchanged.
