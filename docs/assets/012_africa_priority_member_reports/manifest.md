# Event 012 Africa priority-member report art manifest

This package supplies the four generated alternate-history report pictures required by Event 012 Africa priority-member outcomes.

The source mode for every asset is the official built-in `$imagegen` workflow because these are fictional or alternate-history narrative scenes rather than verifiable photographs.

The canonical reference family inspected before generation was `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/report/`, including its `contact_sheet.png`, `README.md`, and `CATALOG.md` entries for the 1936–1945 report-art family.

The source paintings are retained at their generated dimensions, then center-fitted to the exact requested 350x240 RGB PNG canvas with Pillow `ImageOps.fit` and converted to uncompressed 32-bit BGRA DDS using `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`.

All four runtime files are complete and ready for the parent agent's existing `interface/012_africa_priority_member_assets.gfx` definitions.

## Asset entries

### `report_event_012_africa_priority_member_political_settlement`

- Related event: `012_africa`; asset slug: `priority_member_reports`.
- Asset type: generated report event picture.
- Intended use: single-polity political settlement with a decorated sovereign and civic signatories.
- Source mode: `$imagegen` built-in generation, historical-scene treatment.
- Prompt record: `prompts/report_event_012_africa_priority_member_political_settlement.txt`.
- Generation fit: unique fictional civic chamber and invented polity identity were required, so generation fit better than sourcing a real event photograph.
- Source PNG: `source_png/report_event_012_africa_priority_member_political_settlement.png` (1515x1038).
- Processed PNG: `processed_png/report_event_012_africa_priority_member_political_settlement.png` (350x240, RGB).
- Final DDS: `gfx/event_pictures/012_africa/priority_members/report_event_012_africa_priority_member_political_settlement.dds` (350x240, 336128 bytes).
- Proposed sprite name: `report_event_012_africa_priority_member_political_settlement`.
- Target `.gfx`: parent-owned `interface/012_africa_priority_member_assets.gfx`.
- Related localisation/event consumer: Event 012 Africa priority-member political-settlement report outcome; parent owns the exact event/localisation wiring.
- Visual notes: solemn civic chamber, decorated sovereign at left, three signatories at a carved desk, restrained invented banners, no readable text, no combat.
- SHA-256 source: `bb8296a2022dfb5e9aa031de70300bb3c31928048d6a6f0c71b9a71f4df8b828`.
- SHA-256 processed: `4b1c2ceccb77c944e70cb2a2b9dc6559a97df3a3ef472233dab7eade485e2995`.
- SHA-256 DDS: `3f5484bb9f3e83074ecc7c0b17cf87ef1a6c74c2dc31a63cbfd00059121629a2`.
- Status: `complete`.

### `report_event_012_africa_priority_member_league_bargain`

- Related event: `012_africa`; asset slug: `priority_member_reports`.
- Asset type: generated report event picture.
- Intended use: negotiated Charter bargain with visible clauses, maps, seals, and no council portrait.
- Source mode: `$imagegen` built-in generation, historical-scene treatment.
- Prompt record: `prompts/report_event_012_africa_priority_member_league_bargain.txt`.
- Generation fit: the scene needed an invented Charter exchange and abstract clauses without readable language, so generation fit better than sourcing a real document photograph.
- Source PNG: `source_png/report_event_012_africa_priority_member_league_bargain.png` (1514x1039).
- Processed PNG: `processed_png/report_event_012_africa_priority_member_league_bargain.png` (350x240, RGB).
- Final DDS: `gfx/event_pictures/012_africa/priority_members/report_event_012_africa_priority_member_league_bargain.dds` (350x240, 336128 bytes).
- Proposed sprite name: `report_event_012_africa_priority_member_league_bargain`.
- Target `.gfx`: parent-owned `interface/012_africa_priority_member_assets.gfx`.
- Related localisation/event consumer: Event 012 Africa priority-member Charter-bargain report outcome; parent owns the exact event/localisation wiring.
- Visual notes: hands exchange a sealed Charter packet over a map table, abstract clause lines and seals only, no visible council and no readable text.
- SHA-256 source: `ff8badffe118011c0b52c667c35b2764d0f5609332264bfd6f0bb0be20e30b9f`.
- SHA-256 processed: `f3c811986ffe83163c8c0bd0cf8838acfc9922af6815b49bc5ed8bc46cc89c4f`.
- SHA-256 DDS: `6f0e796877f572809e5ba767b3f6667eb23e2f68937f27515fdd5219c703d9ad`.
- Status: `complete`.

### `report_event_012_africa_priority_member_overlap_settlement`

- Related event: `012_africa`; asset slug: `priority_member_reports`.
- Asset type: generated report event picture.
- Intended use: border-overlap settlement reached by consent.
- Source mode: `$imagegen` built-in generation, historical-scene treatment.
- Prompt record: `prompts/report_event_012_africa_priority_member_overlap_settlement.txt`.
- Generation fit: the fictional consent ritual around a shared boundary marker and invented member flags had no required archival source, so generation fit better than sourcing.
- Source PNG: `source_png/report_event_012_africa_priority_member_overlap_settlement.png` (1515x1038).
- Processed PNG: `processed_png/report_event_012_africa_priority_member_overlap_settlement.png` (350x240, RGB).
- Final DDS: `gfx/event_pictures/012_africa/priority_members/report_event_012_africa_priority_member_overlap_settlement.dds` (350x240, 336128 bytes).
- Proposed sprite name: `report_event_012_africa_priority_member_overlap_settlement`.
- Target `.gfx`: parent-owned `interface/012_africa_priority_member_assets.gfx`.
- Related localisation/event consumer: Event 012 Africa priority-member overlap-settlement report outcome; parent owns the exact event/localisation wiring.
- Visual notes: equal delegations meet at a painted stone with a survey tripod and shared notebook, open-hand consent, peaceful landscape, no conquest or charge.
- SHA-256 source: `6990aa64d42648a5849a27ec53495f4d96858749e0c7025976aff9fbe0d5da68`.
- SHA-256 processed: `30da204c90ccb3d4d473308edd70945a19d201eb8e8d72718c68428a34baaa9f`.
- SHA-256 DDS: `e224254fb39fc8d11907fec44b67d8298d278a17fad0d20d8207f5e2e1f1e68d`.
- Status: `complete`.

### `report_event_012_africa_priority_member_departure`

- Related event: `012_africa`; asset slug: `priority_member_reports`.
- Asset type: generated report event picture.
- Intended use: orderly member departure with flags and a guarded frontier, explicitly not conquest.
- Source mode: `$imagegen` built-in generation, historical-scene treatment.
- Prompt record: `prompts/report_event_012_africa_priority_member_departure.txt`.
- Generation fit: the fictional departure convoy and agreed frontier scene required a bespoke narrative composition, so generation fit better than sourcing a real photograph.
- Source PNG: `source_png/report_event_012_africa_priority_member_departure.png` (1514x1039).
- Processed PNG: `processed_png/report_event_012_africa_priority_member_departure.png` (350x240, RGB).
- Final DDS: `gfx/event_pictures/012_africa/priority_members/report_event_012_africa_priority_member_departure.dds` (350x240, 336128 bytes).
- Proposed sprite name: `report_event_012_africa_priority_member_departure`.
- Target `.gfx`: parent-owned `interface/012_africa_priority_member_assets.gfx`.
- Related localisation/event consumer: Event 012 Africa priority-member departure report outcome; parent owns the exact event/localisation wiring.
- Visual notes: calm customs gate, departing train and lorry convoy, separate flags, unhurried guards, final salutes, no combat, panic, prisoners, or conquest.
- SHA-256 source: `b4ecf67938404df53a8594f78aa4875bf17d039a46b744d2983ecdeeac957112`.
- SHA-256 processed: `be36134742372b1763ad3624320bf300c7b9286e14dde5068a7683944ecfcddb`.
- SHA-256 DDS: `d224e16a04965e9eb9a26d31c0342db33e9e67fddd3e40304a67ee3f0f89ce19`.
- Status: `complete`.

## Package review evidence

- Final processed contact sheet: `contact_sheets/report_event_012_africa_priority_member_contact_sheet.png`.
- DDS decode evidence: `validation/decoded_png/` and `validation/dds_validation.json`.
- All four decoded DDS images are 350x240 RGBA with alpha extrema 255/255, exact one-level 32-bit BGRA payload length, and the expected legacy DDS header masks and texture caps.
- No flags, portraits, icons, UI panels, GFX files, gameplay files, localisation files, specs, or workbook files were edited in this package.
