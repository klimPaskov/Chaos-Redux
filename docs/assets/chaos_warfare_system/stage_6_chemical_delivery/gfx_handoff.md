# Stage 6 chemical-delivery GFX handoff

Parent wiring only. No `.gfx` or `.gui` file was edited in this asset package.

The parent-registered declarations were verified in `interface/cbrn_chemical_delivery.gfx`; the sprite names and runtime texture paths below are exact. Equipment cards use the established runtime-equivalent technology directory and `131x52` framing. The idea icon uses the parent-registered idea directory and the standard `64x64` transparent idea-icon framing.

## Ready-to-use sprite and texture mapping

| Asset ID | Sprite name | Target size | Runtime DDS path | Suggested/registered GFX file | Related gameplay ID |
|---|---|---:|---|---|---|
| `archetype_chemical_agent_payload` | `GFX_archetype_chemical_agent_payload_medium` | 131x52 | `gfx/interface/technologies/stage_6_chemical_delivery/equipment/archetype_chemical_agent_payload.dds` | `interface/cbrn_chemical_delivery.gfx` | `archetype_chemical_agent_payload` |
| `chlorine_agent_lot_1` | `GFX_chlorine_agent_lot_1_medium` | 131x52 | `gfx/interface/technologies/stage_6_chemical_delivery/equipment/chlorine_agent_lot_1.dds` | `interface/cbrn_chemical_delivery.gfx` | `chlorine_agent_lot_1` |
| `phosgene_agent_lot_1` | `GFX_phosgene_agent_lot_1_medium` | 131x52 | `gfx/interface/technologies/stage_6_chemical_delivery/equipment/phosgene_agent_lot_1.dds` | `interface/cbrn_chemical_delivery.gfx` | `phosgene_agent_lot_1` |
| `mustard_agent_lot_1` | `GFX_mustard_agent_lot_1_medium` | 131x52 | `gfx/interface/technologies/stage_6_chemical_delivery/equipment/mustard_agent_lot_1.dds` | `interface/cbrn_chemical_delivery.gfx` | `mustard_agent_lot_1` |
| `lewisite_agent_lot_1` | `GFX_lewisite_agent_lot_1_medium` | 131x52 | `gfx/interface/technologies/stage_6_chemical_delivery/equipment/lewisite_agent_lot_1.dds` | `interface/cbrn_chemical_delivery.gfx` | `lewisite_agent_lot_1` |
| `tabun_agent_lot_1` | `GFX_tabun_agent_lot_1_medium` | 131x52 | `gfx/interface/technologies/stage_6_chemical_delivery/equipment/tabun_agent_lot_1.dds` | `interface/cbrn_chemical_delivery.gfx` | `tabun_agent_lot_1` |
| `sarin_agent_lot_1` | `GFX_sarin_agent_lot_1_medium` | 131x52 | `gfx/interface/technologies/stage_6_chemical_delivery/equipment/sarin_agent_lot_1.dds` | `interface/cbrn_chemical_delivery.gfx` | `sarin_agent_lot_1` |
| `soman_agent_lot_1` | `GFX_soman_agent_lot_1_medium` | 131x52 | `gfx/interface/technologies/stage_6_chemical_delivery/equipment/soman_agent_lot_1.dds` | `interface/cbrn_chemical_delivery.gfx` | `soman_agent_lot_1` |
| `malodor_agent_lot_1` | `GFX_malodor_agent_lot_1_medium` | 131x52 | `gfx/interface/technologies/stage_6_chemical_delivery/equipment/malodor_agent_lot_1.dds` | `interface/cbrn_chemical_delivery.gfx` | `malodor_agent_lot_1` |
| `behavioral_agent_lot_1` | `GFX_behavioral_agent_lot_1_medium` | 131x52 | `gfx/interface/technologies/stage_6_chemical_delivery/equipment/behavioral_agent_lot_1.dds` | `interface/cbrn_chemical_delivery.gfx` | `behavioral_agent_lot_1` |
| `archetype_chemical_artillery_ammunition` | `GFX_archetype_chemical_artillery_ammunition_medium` | 131x52 | `gfx/interface/technologies/stage_6_chemical_delivery/equipment/archetype_chemical_artillery_ammunition.dds` | `interface/cbrn_chemical_delivery.gfx` | `archetype_chemical_artillery_ammunition` |
| `chemical_shell_lot_1` | `GFX_chemical_shell_lot_1_medium` | 131x52 | `gfx/interface/technologies/stage_6_chemical_delivery/equipment/chemical_shell_lot_1.dds` | `interface/cbrn_chemical_delivery.gfx` | `chemical_shell_lot_1` |
| `archetype_chemical_air_payload` | `GFX_archetype_chemical_air_payload_medium` | 131x52 | `gfx/interface/technologies/stage_6_chemical_delivery/equipment/archetype_chemical_air_payload.dds` | `interface/cbrn_chemical_delivery.gfx` | `archetype_chemical_air_payload` |
| `choking_chemical_air_payload_lot_1` | `GFX_choking_chemical_air_payload_lot_1_medium` | 131x52 | `gfx/interface/technologies/stage_6_chemical_delivery/equipment/choking_chemical_air_payload_lot_1.dds` | `interface/cbrn_chemical_delivery.gfx` | `choking_chemical_air_payload_lot_1` |
| `blister_chemical_air_payload_lot_1` | `GFX_blister_chemical_air_payload_lot_1_medium` | 131x52 | `gfx/interface/technologies/stage_6_chemical_delivery/equipment/blister_chemical_air_payload_lot_1.dds` | `interface/cbrn_chemical_delivery.gfx` | `blister_chemical_air_payload_lot_1` |
| `nerve_chemical_air_payload_lot_1` | `GFX_nerve_chemical_air_payload_lot_1_medium` | 131x52 | `gfx/interface/technologies/stage_6_chemical_delivery/equipment/nerve_chemical_air_payload_lot_1.dds` | `interface/cbrn_chemical_delivery.gfx` | `nerve_chemical_air_payload_lot_1` |
| `incapacitating_chemical_air_payload_lot_1` | `GFX_incapacitating_chemical_air_payload_lot_1_medium` | 131x52 | `gfx/interface/technologies/stage_6_chemical_delivery/equipment/incapacitating_chemical_air_payload_lot_1.dds` | `interface/cbrn_chemical_delivery.gfx` | `incapacitating_chemical_air_payload_lot_1` |
| `cbrn_first_chemical_shock` | `GFX_idea_cbrn_first_chemical_shock` | 64x64 | `gfx/interface/ideas/stage_6_chemical_delivery/cbrn_first_chemical_shock.dds` | `interface/cbrn_chemical_delivery.gfx` | `cbrn_first_chemical_shock` |

The existing parent declarations are equivalent to:

```text
spriteType = { name = "GFX_idea_cbrn_first_chemical_shock" texturefile = "gfx/interface/ideas/stage_6_chemical_delivery/cbrn_first_chemical_shock.dds" }
```

The 17 equipment declarations follow the same one-line `spriteType` form with the exact sprite and texture pairs listed above. No new sprite name or DDS path is proposed.

## Changed files in this bounded package

Each row below names every source, processed, archive DDS, and runtime DDS file created for the asset. The archive DDS is retained for provenance; the runtime DDS is the parent-registered game path.

| Asset ID | Source PNG | Processed PNG | Archive DDS | Runtime DDS |
|---|---|---|---|---|
| `archetype_chemical_agent_payload` | `source_png/equipment/archetype_chemical_agent_payload_source.png` | `processed_png/equipment/archetype_chemical_agent_payload.png` | `dds/equipment/archetype_chemical_agent_payload.dds` | `gfx/interface/technologies/stage_6_chemical_delivery/equipment/archetype_chemical_agent_payload.dds` |
| `chlorine_agent_lot_1` | `source_png/equipment/chlorine_agent_lot_1_source.png` | `processed_png/equipment/chlorine_agent_lot_1.png` | `dds/equipment/chlorine_agent_lot_1.dds` | `gfx/interface/technologies/stage_6_chemical_delivery/equipment/chlorine_agent_lot_1.dds` |
| `phosgene_agent_lot_1` | `source_png/equipment/phosgene_agent_lot_1_source.png` | `processed_png/equipment/phosgene_agent_lot_1.png` | `dds/equipment/phosgene_agent_lot_1.dds` | `gfx/interface/technologies/stage_6_chemical_delivery/equipment/phosgene_agent_lot_1.dds` |
| `mustard_agent_lot_1` | `source_png/equipment/mustard_agent_lot_1_source.png` | `processed_png/equipment/mustard_agent_lot_1.png` | `dds/equipment/mustard_agent_lot_1.dds` | `gfx/interface/technologies/stage_6_chemical_delivery/equipment/mustard_agent_lot_1.dds` |
| `lewisite_agent_lot_1` | `source_png/equipment/lewisite_agent_lot_1_source.png` | `processed_png/equipment/lewisite_agent_lot_1.png` | `dds/equipment/lewisite_agent_lot_1.dds` | `gfx/interface/technologies/stage_6_chemical_delivery/equipment/lewisite_agent_lot_1.dds` |
| `tabun_agent_lot_1` | `source_png/equipment/tabun_agent_lot_1_source.png` | `processed_png/equipment/tabun_agent_lot_1.png` | `dds/equipment/tabun_agent_lot_1.dds` | `gfx/interface/technologies/stage_6_chemical_delivery/equipment/tabun_agent_lot_1.dds` |
| `sarin_agent_lot_1` | `source_png/equipment/sarin_agent_lot_1_source.png` | `processed_png/equipment/sarin_agent_lot_1.png` | `dds/equipment/sarin_agent_lot_1.dds` | `gfx/interface/technologies/stage_6_chemical_delivery/equipment/sarin_agent_lot_1.dds` |
| `soman_agent_lot_1` | `source_png/equipment/soman_agent_lot_1_source.png` | `processed_png/equipment/soman_agent_lot_1.png` | `dds/equipment/soman_agent_lot_1.dds` | `gfx/interface/technologies/stage_6_chemical_delivery/equipment/soman_agent_lot_1.dds` |
| `malodor_agent_lot_1` | `source_png/equipment/malodor_agent_lot_1_source.png` | `processed_png/equipment/malodor_agent_lot_1.png` | `dds/equipment/malodor_agent_lot_1.dds` | `gfx/interface/technologies/stage_6_chemical_delivery/equipment/malodor_agent_lot_1.dds` |
| `behavioral_agent_lot_1` | `source_png/equipment/behavioral_agent_lot_1_source.png` | `processed_png/equipment/behavioral_agent_lot_1.png` | `dds/equipment/behavioral_agent_lot_1.dds` | `gfx/interface/technologies/stage_6_chemical_delivery/equipment/behavioral_agent_lot_1.dds` |
| `archetype_chemical_artillery_ammunition` | `source_png/equipment/archetype_chemical_artillery_ammunition_source.png` | `processed_png/equipment/archetype_chemical_artillery_ammunition.png` | `dds/equipment/archetype_chemical_artillery_ammunition.dds` | `gfx/interface/technologies/stage_6_chemical_delivery/equipment/archetype_chemical_artillery_ammunition.dds` |
| `chemical_shell_lot_1` | `source_png/equipment/chemical_shell_lot_1_source.png` | `processed_png/equipment/chemical_shell_lot_1.png` | `dds/equipment/chemical_shell_lot_1.dds` | `gfx/interface/technologies/stage_6_chemical_delivery/equipment/chemical_shell_lot_1.dds` |
| `archetype_chemical_air_payload` | `source_png/equipment/archetype_chemical_air_payload_source.png` | `processed_png/equipment/archetype_chemical_air_payload.png` | `dds/equipment/archetype_chemical_air_payload.dds` | `gfx/interface/technologies/stage_6_chemical_delivery/equipment/archetype_chemical_air_payload.dds` |
| `choking_chemical_air_payload_lot_1` | `source_png/equipment/choking_chemical_air_payload_lot_1_source.png` | `processed_png/equipment/choking_chemical_air_payload_lot_1.png` | `dds/equipment/choking_chemical_air_payload_lot_1.dds` | `gfx/interface/technologies/stage_6_chemical_delivery/equipment/choking_chemical_air_payload_lot_1.dds` |
| `blister_chemical_air_payload_lot_1` | `source_png/equipment/blister_chemical_air_payload_lot_1_source.png` | `processed_png/equipment/blister_chemical_air_payload_lot_1.png` | `dds/equipment/blister_chemical_air_payload_lot_1.dds` | `gfx/interface/technologies/stage_6_chemical_delivery/equipment/blister_chemical_air_payload_lot_1.dds` |
| `nerve_chemical_air_payload_lot_1` | `source_png/equipment/nerve_chemical_air_payload_lot_1_source.png` | `processed_png/equipment/nerve_chemical_air_payload_lot_1.png` | `dds/equipment/nerve_chemical_air_payload_lot_1.dds` | `gfx/interface/technologies/stage_6_chemical_delivery/equipment/nerve_chemical_air_payload_lot_1.dds` |
| `incapacitating_chemical_air_payload_lot_1` | `source_png/equipment/incapacitating_chemical_air_payload_lot_1_source.png` | `processed_png/equipment/incapacitating_chemical_air_payload_lot_1.png` | `dds/equipment/incapacitating_chemical_air_payload_lot_1.dds` | `gfx/interface/technologies/stage_6_chemical_delivery/equipment/incapacitating_chemical_air_payload_lot_1.dds` |
| `cbrn_first_chemical_shock` | `source_png/ideas/idea_cbrn_first_chemical_shock_source.png` | `processed_png/ideas/idea_cbrn_first_chemical_shock.png` | `dds/ideas/cbrn_first_chemical_shock.dds` | `gfx/interface/ideas/stage_6_chemical_delivery/cbrn_first_chemical_shock.dds` |

Additional package documentation and review files:

- `manifest.md`
- `prompts/stage_6_prompts.md`
- `contact_sheets/equipment_contact_sheet_checker.png`
- `contact_sheets/idea_cbrn_first_chemical_shock_checker.png`
- `gfx_handoff.md`

## Source provenance and visual review

All source PNGs are generated masters from the built-in imagegen run stored temporarily under `C:/Users/klimp/.codex/generated_images/019f5f49-4f90-7fe0-a28e-04445a687699/`; package-local source files are the preserved handoff artifacts. Equipment concepts were generated independently by payload type and agent lot. The idea icon was generated independently from the equipment concepts after inspecting the Chaos Redux idea references. The processed contact sheets show transparent corners over checkerboard backgrounds and retain separate silhouettes at final-size review scale.

## Validation evidence

- 17 equipment source PNGs, 17 equipment processed PNGs, 17 equipment archive DDS files, and 17 equipment runtime DDS files exist.
- 1 idea source PNG, 1 idea processed PNG, 1 idea archive DDS, and 1 idea runtime DDS exist.
- Processed equipment PNGs are exact `131x52` RGBA images with transparent corners and real alpha; the idea preview is exact `64x64` RGBA with transparent corners and real alpha.
- Final DDS validation covers the legacy `DDS ` magic, 124-byte header, 32-bit `RGB | ALPHAPIXELS` pixel format, BGRA masks, texture caps, zero mip count, exact byte length, declared dimensions, and alpha min/max.
- Every runtime DDS path is present in the existing parent declarations in `interface/cbrn_chemical_delivery.gfx`.
- No source concept is a resized or recolored copy of another requested asset; the idea icon is a separate asset type and separate imagegen output.

## Unresolved risk

No asset is blocked. The only remaining non-blocking review risk is normal in-game UI scaling and colour-management variation; the package contact sheets provide the checkerboard transparency and final-size readability evidence for parent review.
