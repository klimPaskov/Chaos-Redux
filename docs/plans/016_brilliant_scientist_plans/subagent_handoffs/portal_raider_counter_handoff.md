# Portal Raider counter art handoff

Owner requested: `chaosx_icon_artist`. Parent retains GFX/runtime wiring and live validation.

Status: exact references inspected and art brief ready; bespoke outputs not yet produced.

## Consumers and output tokens

The parent-specified custom-unit counter consumers are:

- large division strip token/file stem: `unit_portal_raider_icon`
- small on-map strip token/file stem: `onmap_unit_portal_raider_icon`

Proposed output paths, derived from installed vanilla:

- `gfx/interface/counters/divisions_large/unit_portal_raider_icon.dds`
- `gfx/interface/counters/divisions_small/onmap_unit_portal_raider_icon.dds`

No custom GFX sprite definition or active consumer was inspected because parent-owned runtime wiring is not yet present. Do not invent the final sprite identifier. The parent must register and bind it against the actual portal-raider subunit consumer.

## Installed-vanilla evidence

Definition: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/subuniticons.gfx`.

- line-family precedent `GFX_unit_infantry_icon_medium`: `gfx/interface/counters/divisions_large/unit_infantry_icon.dds`, `noOfFrames = 2`
- line-family precedent `GFX_unit_infantry_icon_medium_white`: `gfx/interface/counters/divisions_small/onmap_unit_infantry_icon.dds`, `noOfFrames = 2`

Exact DDS files:

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/counters/divisions_large/unit_infantry_icon.dds`: 152x42 BGRA, two 76x42 frames, SHA-256 `B33A8E3B69CC789EB0E31BA99F4E5BA4E5B0A8B51EC1A7A7F709C3516F720C23`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/counters/divisions_small/onmap_unit_infantry_icon.dds`: 60x12 BGRA, two 30x12 frames, SHA-256 `58AB78662C2A64A519B8D5D144582E7B2785915BD0A0A822696D87A9DE6F766C`

Decoded copies are preserved at:

- `docs/assets/shared_portal_raider_system/models_3d/portal_raider/evidence/counter/vanilla_unit_infantry_icon.png`
- `docs/assets/shared_portal_raider_system/models_3d/portal_raider/evidence/counter/vanilla_onmap_unit_infantry_icon.png`

Skill-local reference families inspected:

- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/counters_large/`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/counters_large/contact_sheet.png`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/map_counters/`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/map_counters/contact_sheet.png`

## Frame and palette contract

- Large canvas: 152x42, two frames ordered exactly like the installed infantry strip; frame size 76x42.
- Small canvas: 60x12, two frames ordered exactly like the installed on-map infantry strip; frame size 30x12.
- Preserve transparent background/alpha, border weight, contrast, and state behavior from the reference strips.
- Large infantry frame-one opaque silhouette occupies approximately x=21..54, y=9..36 within its 76x42 frame.
- Small infantry frame-one opaque silhouette occupies approximately x=8..21, y=0..11 within its 30x12 frame.
- Sampled vanilla-green anchors from the large strip: RGB `(73,106,73)` and `(74,107,74)` for the dominant midtone, with highlights around `(100,128,100)` and `(116,141,116)`. Match this family and its value range; arbitrary green is forbidden.
- Preserve the reference frame-two black/gray/white state treatment and exact frame order rather than recoloring both frames green.

## Original-art direction

Create an identity-neutral portal-infantry symbol that remains legible at both frame sizes. The large frame should combine a goggled protected head/torso silhouette with one unmistakable compact portal coil and a short ray-rifle profile. The small map frame should reduce this to the goggled head plus a single coil/rifle cue without fine cable detail. No country, ideology, event, organization, provider, text, watermark, or named-character markings.

Required package from `chaosx_icon_artist`:

- original source PNGs
- processed frame-aware PNG strips at the exact canvases above
- final DDS files
- per-frame preview and large/small comparison contact sheet against the installed infantry family
- sampled palette evidence
- manifest entries with source/output hashes
- `gfx_handoff.md` naming the proposed sprites and exact parent-owned registration paths

A renamed/reused vanilla counter, generic placeholder, or unreferenced green imitation is not acceptable final art.
