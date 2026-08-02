# Vanilla doctrine reference inspection

This package records the direct vanilla inspection required for the regenerated Chaos Warfare doctrine-style icons. It is review evidence only and contains no runtime copies or final substitutes.

## Canonical sources inspected

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/doctrines/icons/doctrine_mass_assault.dds`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/doctrines/icons/doctrine_grand_battleplan.dds`
- `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/gfx/interface/doctrines/icons/doctrine_chaos_warfare.dds` (user original; style anchor only)
- Existing Chaos Redux doctrine-style review sheet: `../contact_sheets/doctrine_contact_sheet_checker.png` (stage-5 generated art, not a vanilla reference)

The canonical reference library has no `icons/doctrines` family or doctrine contact sheet. Direct vanilla DDS inspection was therefore used for the doctrine surface, while the canonical `units/land/counters_large/contact_sheet.png` was inspected for the separate counter family.

## Header and dimension facts

| Source | Canvas | DDS header facts | Alpha | Notes |
|---|---:|---|---|---|
| `doctrine_mass_assault.dds` | 64x64 | 128-byte legacy header; `DDS_HEADER=124`; `DDS_PIXELFORMAT=32`; flags `65`; fourCC `0`; 32-bit BGRA masks; one top-level image; texture caps | 0..255 | Vanilla doctrine icon surface is 64x64 with transparent unused canvas. |
| `doctrine_grand_battleplan.dds` | 64x64 | Same legacy uncompressed BGRA contract as Mass Assault | 0..255 | Strong central silhouette, black contour, ivory body, orange accent, minimal internal detail. |
| user original `doctrine_chaos_warfare.dds` | 64x64 | 64x64 BGRA source with the user's existing mipmapped header; preserved byte-for-byte | 0..255 | Style anchor only; it was not regenerated, overwritten, recolored, or used as final source art for the new family. |

## Palette and shape observations

Vanilla doctrine icons use one dominant centered military symbol, a thick dark contour, restrained internal detail, and a transparent canvas that survives the 64x64 UI surface. The inspected Chaos Redux anchor adds a black/ivory/orange high-contrast identity; the new four icons use that palette as direction while remaining original generated art.

The new family was generated as four separate doctrine assets rather than resized or relabeled copies of the grand icon. The concepts are a masked assault formation, sealed toxic tank, chemical projector/shell, and integrated CBRN command case.

## Preview policy

No vanilla source DDS or decoded vanilla PNG was copied into this documentation folder. The asset skill forbids adding new reference images outside the canonical `assets/vanilla_reference` root. A temporary three-source review sheet was used during inspection and is not part of the runtime or final asset package.
