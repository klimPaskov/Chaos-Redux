# Event 012 elephant equipment/technology icon handoff — 2026-08-05

Status: `needs_user_review` pending parent contact-sheet review and parent-owned `.gfx`/subunit wiring.

## Deliverable

Created one original HOI4-style medium equipment/technology icon for the separate `chaosx_elephant` subunit.

The icon uses the approved oversized shared elephant model render as the sole subject reference and depicts the same elephant with readable dark iron brow, shoulder, flank, and harness armour.

No second model, generic fallback, copied vanilla icon, unrelated unit art, gameplay file, localisation file, or `.gfx` file was created or edited.

## Files

- Source PNG: `docs/assets/012_africa/models_3d/elephant_shared_base/evidence/equipment/source/chaosx_elephant_equipment_imagegen_source.png`.
- Exact source prompt: `docs/assets/012_africa/models_3d/elephant_shared_base/evidence/equipment/source/chaosx_elephant_equipment_imagegen_prompt.txt`.
- Chroma-key cutout: `docs/assets/012_africa/models_3d/elephant_shared_base/evidence/equipment/processed/chaosx_elephant_equipment_cutout.png`.
- Processed runtime PNG: `docs/assets/012_africa/models_3d/elephant_shared_base/evidence/equipment/processed/chaosx_elephant_equipment.png`.
- Native-size review contact sheet: `docs/assets/012_africa/models_3d/elephant_shared_base/evidence/equipment/contact/chaosx_elephant_equipment_contact_sheet.png`.
- DDS round-trip PNG: `docs/assets/012_africa/models_3d/elephant_shared_base/evidence/equipment/roundtrip/chaosx_elephant_equipment_roundtrip.png`.
- DDS validation JSON: `docs/assets/012_africa/models_3d/elephant_shared_base/evidence/equipment/validation/dds_validation.json`.
- Manifest and QA record: `docs/assets/012_africa/models_3d/elephant_shared_base/evidence/equipment/manifest.md`.
- Final runtime DDS: `gfx/interface/technologies/012_africa/chaosx_elephant_equipment.dds`.

## Proposed wiring

- Proposed stable sprite: `GFX_chaosx_elephant_equipment_medium`.
- Proposed texture path: `gfx/interface/technologies/012_africa/chaosx_elephant_equipment.dds`.
- Suggested existing `.gfx` owner: `interface/chaosx_equipment.gfx`; use the parent-selected technology `.gfx` instead if the technology consumer is registered there.
- Parent-owned consumer: the separate `chaosx_elephant` equipment/technology and subunit definitions.
- This handoff does not authorize editing the shared elephant counters or model entity package.

## Exact reference evidence

The canonical contact sheet was inspected first at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/equipment/technology_art/contact_sheet.png`.

The selected installed-vanilla precedent is `support_equipment_1.png` at 133x55 RGBA with transparent background, registered as `GFX_tech_support_medium` in the installed `interface/Technologies.gfx` and backed by `gfx/interface/technologies/support_equipment_1.dds` at 133x55.

The final 131x52 canvas follows the existing Chaos Redux medium equipment precedent, including `gfx/interface/technologies/coal_golem_equipment.dds`.

Reference pixels were not copied, traced, recoloured, or resized into the final icon.

## QA

- Final DDS is a legacy one-level uncompressed BGRA file with dimensions 131x52 and exact file length 27376 bytes.
- DDS header has magic `DDS `, header size `124`, `DDS_PIXELFORMAT` size `32`, flags `65`, fourCC `0`, bit count `32`, BGRA masks `0x00FF0000`, `0x0000FF00`, `0x000000FF`, `0xFF000000`, and texture caps `0x1000`.
- Processed PNG alpha range is `0..255` with visible bbox `(42,2)-(89,50)` and transparent corners.
- Chroma-key edge audit found 9,033 semi-transparent pixels and zero greenish fringe pixels after despill.
- FFmpeg DDS decode is 131x52 with alpha range `0..255`; decoded pixels are exactly equal to the processed PNG (`ImageChops.difference(...).getbbox() == None`).
- Contact sheet includes source, chroma-key alpha cutout, smooth enlarged native preview, decoded DDS preview, and vanilla reference over checkerboards.

## Checksums

- Approved render `elephant_shared_base_final_three_quarter.png`: `ABD972121E92AAED40571F2301361487215842058192ACD494210E1BCDBC3508`.
- ImageGen source PNG: `33C81C3FDC8B5A9CF953F2DDFCF5BD06F5DCF4B76F14FB55E6BEE15169267619`.
- Prompt: `820FD2372C94E280C5B889858EB827C20310E900724959247E9CF5B9DDBF8F9C`.
- Chroma-key cutout PNG: `764766D6CCC3F2B53A0EDD082F5297D0E92C87AE71A9F2FEE406B4BBEA6A31AE`.
- Processed runtime PNG: `298CD784929F9D80EF6098CEC0A17C4471FE356F7A5AD4D6CAFE7B307A78B900`.
- Final runtime DDS: `400E69C295801DA059A15C6E28F2F3E2241D6EB7475EB3D758A561FA879ACDB4`.
- DDS round-trip PNG: `EDBDAEC354B6442F6104E962F6B24FA7994FF13DEE6E339176A19960C4BF581E`.
- Contact sheet: `F64DC5115125B93104988F6F76078D72E0009066AA5D14C337CCC8976B9AAF85`.
- DDS validation JSON: `48A8B1A8C03BDBDF69D0FD9F887860B3BF9947D62C58CC168F73B982BAF1C118`.

## Parent action

Review `chaosx_elephant_equipment_contact_sheet.png`, register `GFX_chaosx_elephant_equipment_medium` in the appropriate existing `.gfx`, and bind the DDS to the parent-owned `chaosx_elephant` equipment/technology consumer.

Do not claim in-game completion until `.gfx` and gameplay wiring are added and the parent confirms the reviewed sprite in the target consumer.
