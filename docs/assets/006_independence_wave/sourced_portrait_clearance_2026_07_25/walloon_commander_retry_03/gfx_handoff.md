# GFX handoff: IW-006 Walloon commander source retry 03

This is a parent-wiring handoff only. No `.gfx`, event, character, localisation, gameplay, ImageGen, or DDS file was edited or generated in this bounded source-clearance tranche.

## Candidate

- Subject: Louis Hubert baron Ruquoy (period source spelling: Louis Rucquoy).
- Role: grounded real-person army commander and senior military-security council figure.
- Walloon connection: born at Frasnes-lez-Buissenal in Hainaut.
- 1936 fit: alive throughout 1936; retired Belgian lieutenant-general and former Chief of the General Staff.
- Suggested future sprite name: `GFX_portrait_AFX_walloon_louis_ruquoy`.
- Suggested consumer: the parent-owned IW-006 Walloon Defence Council commander slot, only after independent portrait review and parent approval.

## Source-locked crop

- Immutable master: `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_25/walloon_commander_retry_03/source_masters/ruquoy_rol_1923_group.jpg`.
- Master provenance: Agence Rol / Bibliotheque nationale de France, Gallica, item `btv1b531010537`; public domain as marked by the Commons Gallica record (PD France, PD-1996, PD US expired).
- Selected exact crop: `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_25/walloon_commander_retry_03/source_crops/ruquoy_rol_1923_head_shoulders.png`.
- Crop rectangle: `(3300, 1000, 5050, 2900)` half-open decoded pixels from the unchanged 8419 x 6051 grayscale master.
- Crop proof: `source_crops/ruquoy_rol_1923_head_shoulders.json` with `decoded_pixels_equal: true`.
- The crop is source evidence, not a final HOI4 texture. Commander runtime textures must remain full `156 x 210` portraits; do not wire this 1750 x 1900 PNG directly.

The source is a four-person group photograph. The full caption identifies the center subject as general Rucquoy; the archive title and default page caption foreground general Henri Maglinse, so retain this caption-order identity basis as a provenance note. The crop itself shows Ruquoy's cap, moustache, ears, eyes, collar, upper coat, and both shoulders at high resolution.

## Rights and attribution

The selected BnF Gallica source is marked public domain by the Commons record. Preserve this attribution in any future runtime or distributed source notice:

`Agence Rol / Bibliotheque nationale de France, Gallica, item btv1b531010537.`

The LPDF 118 crop and *Le Miroir* 215 crop remain secondary likeness and uniform corroboration. LPDF is a CC BY-SA 3.0 Garitan scan; *Le Miroir* carries a disputed-copyright-information warning and must not replace the selected source without a fresh rights review.

## Parent-owned next gate

The parent must have an independent reviewer compare the unchanged master, selected crop, any future raw ImageGen result, future deterministic `156 x 210` commander candidate, and canonical commander references at native and at least 4x nearest-neighbour scale. Identity, style, and provenance are separate gates. The source package remains `needs_user_review`; this handoff does not authorize ImageGen, DDS conversion, or `.gfx` registration.
