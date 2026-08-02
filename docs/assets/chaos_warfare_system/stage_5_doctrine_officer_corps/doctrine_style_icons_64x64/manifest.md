# Chaos Warfare doctrine-style icon regeneration manifest

Package: `chaos_warfare_system` / doctrine-style icon regeneration.

Target surface: verified 64x64 doctrine adoption/subdoctrine icons.

Source mode: built-in `$imagegen`; each icon has an independent generated source master, alpha master, processed transparent PNG, final DDS, and visual inspection contact sheet.

The grand doctrine icon at `gfx/interface/doctrines/icons/doctrine_chaos_warfare.dds` was not regenerated or overwritten. Existing stage-5 generated files under `gfx/interface/doctrines/icons/stage_5_chaos_warfare/` were preserved.

| Asset type / related gameplay id | Source PNG -> alpha master -> processed PNG | Final DDS | Sprite / `.gfx` | Target / status / uncertainty |
|---|---|---|---|---|
| Doctrine style / `subdoctrine_extermination_columns` | `source_png/doctrine_hazard_assault_formations_source.png` -> `alpha_master/doctrine_hazard_assault_formations_alpha.png` -> `processed_png/doctrine_hazard_assault_formations.png` | `gfx/interface/doctrines/icons/chaos_warfare_doctrine_style/doctrine_hazard_assault_formations.dds` | `GFX_doctrine_extermination_columns_medium` / `interface/cbrn_doctrine.gfx` | 64x64, 1 frame, wired in `interface/cbrn_doctrine.gfx`; original grand-doctrine sprite preserved. |
| Doctrine style / `subdoctrine_chemical_suppression` | `source_png/doctrine_toxic_armored_warfare_source.png` -> `alpha_master/doctrine_toxic_armored_warfare_alpha.png` -> `processed_png/doctrine_toxic_armored_warfare.png` | `gfx/interface/doctrines/icons/chaos_warfare_doctrine_style/doctrine_toxic_armored_warfare.dds` | `GFX_doctrine_chemical_suppression_medium` / `interface/cbrn_doctrine.gfx` | 64x64, 1 frame, wired in `interface/cbrn_doctrine.gfx`; original grand-doctrine sprite preserved. |
| Doctrine style / `subdoctrine_contaminant_firebases` | `source_png/doctrine_contaminant_fire_support_source.png` -> `alpha_master/doctrine_contaminant_fire_support_alpha.png` -> `processed_png/doctrine_contaminant_fire_support.png` | `gfx/interface/doctrines/icons/chaos_warfare_doctrine_style/doctrine_contaminant_fire_support.dds` | `GFX_doctrine_contaminant_firebases_medium` / `interface/cbrn_doctrine.gfx` | 64x64, 1 frame, wired in `interface/cbrn_doctrine.gfx`; original grand-doctrine sprite preserved. |
| Doctrine style / `subdoctrine_integrated_chemical_operations` | `source_png/doctrine_integrated_cbrn_command_source.png` -> `alpha_master/doctrine_integrated_cbrn_command_alpha.png` -> `processed_png/doctrine_integrated_cbrn_command.png` | `gfx/interface/doctrines/icons/chaos_warfare_doctrine_style/doctrine_integrated_cbrn_command.dds` | `GFX_doctrine_integrated_chemical_operations_medium` / `interface/cbrn_doctrine.gfx` | 64x64, 1 frame, wired in `interface/cbrn_doctrine.gfx`; original grand-doctrine sprite preserved. |

Contact sheet: `contact_sheets/doctrine_style_contact_sheet_checker.png`.

Prompts: `prompts.md`.

Header validation: all four DDS files are 64x64, 16,512 bytes, one-level uncompressed BGRA 32-bit, `DDS_PIXELFORMAT` flags 65, fourCC 0, masks `00FF0000/0000FF00/000000FF/FF000000`, texture caps `0x1000`, and alpha range 0..255.
