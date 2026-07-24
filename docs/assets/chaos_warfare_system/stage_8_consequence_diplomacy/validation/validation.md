# Stage 8 CBRN Consequence Diplomacy Icon Validation

All three source masters are retained as independently generated 1254x1254 PNGs with opaque chroma-key backgrounds.

All three chroma-key-removed intermediates are 1254x1254 RGBA PNGs with transparent corners and zero recorded pure-green residual pixels under the recorded residual test.

All three processed previews are exact 32x32 RGBA PNGs with transparent corners and alpha ranges of 0 to 255.

The processed alpha coverage values are `0.7227` for `decision_cbrn_demand_inspections`, `0.7129` for `decision_cbrn_share_forensic_evidence`, and `0.7080` for `decision_cbrn_sponsor_decontamination_mission`.

Each final DDS is 4224 bytes, consisting of a 128-byte legacy DDS header and one 32x32x4 payload.

Each final DDS declares `DDS ` magic, header size `124`, header flags `4111`, `DDS_PIXELFORMAT` size `32`, pixel-format flags `65`, fourCC `0`, 32-bit pixels, BGRA masks `0x00FF0000 / 0x0000FF00 / 0x000000FF / 0xFF000000`, and `DDSCAPS_TEXTURE` `0x1000`.

The decoded BGRA payload of every final DDS matches its processed PNG RGBA pixels byte-for-byte after channel conversion.

All three final DDS files exist under `gfx/interface/decisions/cbrn_diplomacy/` at the exact requested 32x32 runtime size.

The native-size and 8x nearest-neighbour processed preview review is in `contact_sheets/stage_8_consequence_diplomacy_decision_icons.png`.

The decoded final-DDS review is in `contact_sheets/stage_8_consequence_diplomacy_final_dds_contact_sheet.png`.

Machine-readable dimensions, alpha metrics, header fields, round-trip results, and SHA-256 hashes are in `asset_hashes_and_qa.json`.

No placeholder, local primitive drawing, resized unrelated icon, or cross-type substitute was used.
