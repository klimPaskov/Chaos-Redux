# Event 014 Americas Warlord Portrait Validation

Validation date: 2026-07-12

## Accepted visual set

The parent reviewed and accepted the complete 16-source board after four North/South replacement rounds. The final board confirms one adult male-presenting bald fictional human-origin subject per image, strong facial asymmetry, bloodshot or unequal eyes, damaged teeth, visible dried blood, invented rough clothing, scavenged 1930s-1940s gear, and an active origin-specific behavior. No selected image repeats the Europe CBA skull-licking pose or Europe CBB ration-biscuit action.

The 16 selected action silhouettes are:

- North America: rope haul, broken boat hook, wire-wrapped trench hammer, casing/pliers/plate, field megaphone, starter crank, snapped baton, dented spoon.
- South America: dock gaff, weighted bell clapper, bolt cutters, masonry chisel/plate, torn rein, T-handle spark-plug spanner, broken key/lock plate, sleeve strip and snapped cuff hinge.

No selected portrait includes living ceremonial, tribal, Indigenous, Pacific, African, or religious regalia; sacred motifs; readable text; a national symbol; actor or real-person likeness; antlers; or supernatural transformation.

## Exact format and decode proof

All 16 processed PNGs are exactly `156x210 RGBA`; alpha extrema are `(255, 255)`. All 16 DDS files have:

- total size `131168` bytes;
- DDS magic and 124-byte header;
- dimensions `156x210`;
- row pitch `624`;
- pixel-format flags `0x41` (RGB plus alpha);
- 32 bits per pixel;
- masks `00FF0000`, `0000FF00`, `000000FF`, `FF000000`;
- caps `DDSCAPS_TEXTURE`;
- no mip chain field, meaning one stored base image level.

Every DDS was decoded independently through FFmpeg. For each of the 16 pairs, the decoded 156x210 RGBA byte stream is exactly equal to the matching processed PNG byte stream. Raw RGBA SHA-256 values were unique for all 16 pairs.

| Asset | Raw RGBA SHA-256 | DDS header | Pixel-identical decode |
| --- | --- | --- | --- |
| CBA North America | `03A909B0B54D4096E7584CF8F9A9C1D09A3000E1C86A406569BC1493E09871A3` | valid | yes |
| CBB North America | `1A66FE30D42FC6993530341EBA886BF9479934668D318B1EC5F1A1FDF042C53F` | valid | yes |
| CBC North America | `C92B68BA5AB7ED582C69E349E0A69F6772E80EF4D10526E546A798A47BF3A03C` | valid | yes |
| CBD North America | `580DC37ABD9E8C1CFE56824B6A8D7BE85E247191EF81C922BB5D4A8E52F8B07F` | valid | yes |
| CBE North America | `811814E05F65C0B935A8BC3114BF841415060AA081887507AAEE29BA9174E5BF` | valid | yes |
| CBF North America | `1BAABE012FECB784EBB050A7B0A2002B581E98BCA01B59B1D652443BD35D845F` | valid | yes |
| CBG North America | `C85E447D1A612C2873100B9339795AE52B4C802C5CFC514150287C739E31E518` | valid | yes |
| CBH North America | `78D55ADD9C6DFF424D637525C444DE10AB3E6E0D4DA1F7673A76D666B87BA5D0` | valid | yes |
| CBA South America | `E9AFE557F7C2431E0A36EBFAEE6364F25CE7E406AF778BDFD80D55327DAC1E78` | valid | yes |
| CBB South America | `3D3A29E69C23EE6DA7F9B9571716D81EF68C87BFAE60D32B95CA2498630E3D9A` | valid | yes |
| CBC South America | `8EA64FA836A68FFEDB66E12DF9DC71F44691D06EA8587D4D6F2E11202DD5F1FA` | valid | yes |
| CBD South America | `47B80D4CF702FEB04DDB9B2E468694F9705F418C20483086437AF26326F63DE2` | valid | yes |
| CBE South America | `7203DFCCD1A6739F6757E3C43D5165A10B9EDDE7271C5E39057C24B0C5075276` | valid | yes |
| CBF South America | `137AC3772B9BC96042CF6BCF561935872D505C53D5DD7D83476BB79FA81618E9` | valid | yes |
| CBG South America | `3369AB852A21B469735000D79FB568C3A6E92C0B6F671E97668E3773A9587353` | valid | yes |
| CBH South America | `74CA63D0E72EF601C42A7CBF99ABC3B6E93CE47A9A0B76F465882547B94CF5F4` | valid | yes |

## Uniqueness evidence

Source, processed-PNG, and DDS file hashes are each unique across the 16 accepted assets. Full-image 64-bit dHash distances range from 21 to 43 bits. The closest pairs remain visibly separated by face geometry, posture, action, prop, clothing construction, lighting, and background; no selected source is a crop, recolor, or edit of another source.

## Contact sheets

- Source: `../contact_sheets/warlord_americas_source_contact_2026-07-12.png`
- Processed: `../contact_sheets/warlord_americas_processed_contact_2026-07-12.png`
- DDS decoded: `../contact_sheets/warlord_americas_dds_decoded_contact_2026-07-12.png`

