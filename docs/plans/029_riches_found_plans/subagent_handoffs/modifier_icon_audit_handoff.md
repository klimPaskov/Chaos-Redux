# Event 029 Riches Found Modifier Icon Audit Handoff

Status: `complete_parent_wiring_pending_live_review`.

This package contains one separately authored modifier-family icon for the country-scope `riches_found_controller_aggregate` dynamic modifier. The parent completed GFX registration, the dynamic-modifier `icon` field change, and runtime placement; live in-game validation remains user-owned.

## Selected asset

| Item | Path or value |
|---|---|
| Asset id | `029_riches_found_controller_aggregate_modifier` |
| Asset type | Generic/dynamic modifier icon |
| Source mode | Official built-in ImageGen |
| Background mode | `native_transparent` |
| Target canvas | 30x20 |
| Proposed sprite | `GFX_modifier_riches_found_controller_aggregate` |
| Proposed runtime texture | `gfx/interface/modifiers/029_riches_found/riches_found_controller_aggregate_modifier.dds` |
| Target GFX file | `interface/029_riches_found.gfx` (parent-owned; wired) |
| Gameplay consumer | `common/dynamic_modifiers/029_riches_found_state_modifiers.txt:101-109` |
| Current consumer icon | `GFX_modifier_riches_found_controller_aggregate` |
| Parent action | Completed sprite registration, runtime copy, and consumer icon replacement; retain live rendering review as user-owned |

The motif is a restrained mine-shaft arch joined to a brass registry tablet with grouped mineral markers. It contains no readable text, flags, portraits, animation, audio, units, 3D, fantasy chest, crystal, demon, or biological imagery.

## Retained files and hashes

| Surface | Path | Dimensions | SHA-256 | Alpha/bounds |
|---|---|---:|---|---|
| Native ImageGen source | `docs/assets/029_riches_found/source_png/modifier/riches_found_controller_aggregate_modifier_source.png` | 1536x1024 | `d23fb76b448fb3f77e4703575bfd34c67a1096fcf6b77a057f8063d4320a9762` | alpha 0-254; alpha bbox `(47,0)-(1490,944)`; threshold-32 visible bbox `(50,132)-(1488,827)`; all four corners zero-alpha |
| Processed PNG | `docs/assets/029_riches_found/processed_png/modifier/riches_found_controller_aggregate_modifier.png` | 30x20 | `3929862590a50f8ade059a4160fc65d1dc153f59ff266095517fc47ae88933d8` | alpha 0-255; alpha bbox `(1,1)-(29,19)`; threshold-32 visible bbox `(1,3)-(29,17)`; all four corners zero-alpha |
| Final DDS evidence | `docs/assets/029_riches_found/final_dds/modifier/riches_found_controller_aggregate_modifier.dds` | 30x20 | `c9566ea0abae93961c46955c96f99ca5a4234fe55dd6d2a4804104d5979ae96c` | decoded alpha 0-255; decoded bbox `(1,1)-(29,19)` |
| Decoded DDS PNG | `docs/assets/029_riches_found/notes/decoded_dds/modifier/riches_found_controller_aggregate_modifier.png` | 30x20 | `3929862590a50f8ade059a4160fc65d1dc153f59ff266095517fc47ae88933d8` | alpha 0-255; all four corners zero-alpha |

The DDS is 2528 bytes, exactly `128 + 30*20*4`. The retained validation record confirms `DDS_HEADER` size 124, `DDS_PIXELFORMAT` size 32, flags 65, zero fourCC, 32-bit pixels, BGRA masks `0x00FF0000/0x0000FF00/0x000000FF/0xFF000000`, and `DDSCAPS_TEXTURE` `0x00001000`. The decoded DDS is pixel-identical to the processed PNG.

## Prompt and ImageGen provenance

The exact prompt is retained at `docs/assets/029_riches_found/prompts/modifier/riches_found_controller_aggregate_modifier_prompt.md`.

Selected built-in ImageGen execution: `exec-45efa1eb-2ce9-454d-bef8-e2a274c314a0`.

The initial selected source requested genuine transparent output. Native alpha validation found zero-alpha corners and no need for background removal. The source was processed with the retained local Pillow tool `docs/assets/029_riches_found/notes/process_modifier_icon.py` using alpha-bounds crop, Lanczos downsampling to a maximum 28x18 subject, and centered compositing on a 30x20 transparent canvas.

The earlier built-in ImageGen execution `exec-ea3ae955-bd76-4f36-85ca-cec2b58169b9` is retained under `docs/assets/029_riches_found/notes/superseded_sources/riches_found_controller_aggregate_modifier_scene_candidate.png` for audit history only. It was rejected because its mine-cart and oversized seal composition was too scene-like and too detailed for the 30x20 modifier surface.

## Consumer and reference evidence

The exact installed vanilla dynamic-modifier schema is `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/dynamic_modifiers/0_dynamic_modifiers.txt:1-27`. It documents an optional explicit `icon` GFX token shown in GUIs and states that dynamic modifiers can be added to countries, states, unit leaders, or special projects.

The installed vanilla country-scope aggregate precedent is `BUL_foreign_industry_dynamic_modifier` at `0_dynamic_modifiers.txt:248-259`. It combines political power, construction, factory output, efficiency, and consumer-goods effects under a dedicated icon token, so a country-scope aggregate does not require an idea-family sprite.

The installed vanilla dynamic-modifier UI evidence is `interface/countrystateview.gui:391-398` for the dynamic-modifier grid and `interface/countrystateview.gui:747-764` for the runtime-supplied icon entry. The country-army modifier GFX precedent is `interface/countryarmyview.gfx:167-180` and `212-225`.

The canonical reference root was `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference`. The matching family was `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/modifiers/`; its `contact_sheet.png` was inspected before the five individual references. `CATALOG.md:326-330` records `army_speed_factor.png`, `max_planning.png`, `modifier_attrition.png`, `modifier_org_loss_when_moving.png`, and `modifier_supply_consumption_factor.png` as Vanilla HOI4 modifier icons with native 30x20 canvases and transparent unused canvas.

The canonical references show compact centered silhouettes, dark outlines/shadows, selective warm orange/yellow or muted green/steel accents, and no painted square background. The selected asset uses its own ImageGen artwork with the same 30x20 transparent-family treatment and a restrained charcoal/steel, slate-green, brass/ochre palette; no canonical art was copied or resized.

The full consumer/reference note is `docs/assets/029_riches_found/notes/modifier_consumer_reference.md`.

## Review evidence

The native-size four-panel review is `docs/assets/029_riches_found/contact_sheets/modifier_contact_sheet.png`. It compares the native-alpha ImageGen source, processed 30x20 preview over checkerboard, smooth enlargement over dark solid, and decoded DDS round-trip over light solid.

The contrast review is `docs/assets/029_riches_found/notes/review/riches_found_controller_aggregate_modifier_contrast_review.png`.

The machine audit is `docs/assets/029_riches_found/notes/validation/modifier_validation.json`, with a short summary at `docs/assets/029_riches_found/notes/validation/modifier_validation.md`. It confirms dimensions, alpha, bounds, strict DDS header, exact length, hashes, and pixel equality.

## Parent wiring handoff

The parent may use this ready-to-copy sprite definition shape in the existing `interface/029_riches_found.gfx` file:

```text
spriteType = {
	name = "GFX_modifier_riches_found_controller_aggregate"
	texturefile = "gfx/interface/modifiers/029_riches_found/riches_found_controller_aggregate_modifier.dds"
}
```

The parent changed only the icon token in the existing dynamic-modifier definition from `GFX_idea_riches_found_windfall_receipts` to `GFX_modifier_riches_found_controller_aggregate`, added the sprite definition, and synchronized the runtime DDS. Live in-game rendering remains user-owned.
