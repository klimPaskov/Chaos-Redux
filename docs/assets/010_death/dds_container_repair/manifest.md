# Event 010 Death DDS Container Repair

Event: 010 Death (010_death).
Repair scope: preserve the existing runtime filenames and paths while changing six full-canvas RGB24 DDS containers to the repository-standard uncompressed BGRA32 DDS layout.
Source mode for every asset: inherited DDS; original master provenance unresolved.
The original source master was not available in the bounded package. No ImageGen source or prompt proof is claimed.
Status: complete for the requested DDS container repair.

The untouched input DDS files were archived before conversion under source_originals/. source_archive_hashes.md records each original runtime path, exact archive path, byte length, and SHA-256. The original DDS files were uncompressed RGB24 with no stored alpha channel; decoding yielded uniformly opaque alpha (255). Each temporary PNG input was decoded from the archived DDS, converted with the repository-standard converter, and removed with its temporary directory after validation.

The news and super-event reference families were inspected in the canonical skill reference root. Their contact sheets are 1200×498; individual canvases are 397×153 for news and 457×328 for super-events. All six assets retain their original canvas and use the opaque full-canvas treatment.

| Asset ID | In-game use | Runtime path | Size | Original SHA-256 | Output SHA-256 | Decoded RGBA pixel SHA-256 (source = output) | Result |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| news_event_death_mainland_reveal | News event image | gfx/event_pictures/010_death/news_event_death_mainland_reveal.dds | 397×153 | 3f702692d08ac0723bf3957941e87167d52ad09317e9306ef99ea972659f7882 | 71ba59017a387d40806eebd5b5ebdd8430ec8f29c26a8f5b603f2fd00ab2513e | 5968cef3358cd05b8dc64c4455f6d4bc059cc70a7ace635c49d55377339ec94d | Exact decoded-pixel match; alpha 255 throughout |
| news_event_death_defeated | News event image | gfx/event_pictures/010_death/news_event_death_defeated.dds | 397×153 | af8d3975cffb6457a0c6fa3a51a03bd9796d032c4a1142dc73d8a218458b8424 | 8402aebefe5b52d1c2abee5236711671762cee3a7d759c350cc656aa2a9ba3de | b6f7e342edd739952ab9fba55d62afc7c1302eb9baf6b8f7e37c75e30339c7c9 | Exact decoded-pixel match; alpha 255 throughout |
| super_event_death_world_end | Super-event image | gfx/super_events/010_death/super_event_death_world_end.dds | 457×328 | be7dd85ab3951f82af896cb24e89cfafe9d564401fbae394aff90aabfc57d481 | e031d67d14d27744eaadea96ab7959e2f5075c88eda39620cf46d1f684a0ea14 | cb9c7d33397b38d0cf00d17e4585b1a00c6efcc646073450b123b6fde32b06bc | Exact decoded-pixel match; alpha 255 throughout |
| super_event_death_defeat_aftermath | Super-event image | gfx/super_events/010_death/super_event_death_defeat_aftermath.dds | 457×328 | ac163525e88e8be025bd3cae59687ceb8abfe0b3f7387c6e9a81df9eb1fc6201 | 91cf3d61088f0930e9dd278b9a4aef7874dcebd8a965b1057d198c2e0d613351 | 049f457235967b2eb57b9f1efdb600b4ca79c1a5a56abcacf573ae4f3d65123c | Exact decoded-pixel match; alpha 255 throughout |
| super_event_death_world_consumed | Super-event image | gfx/super_events/010_death/super_event_death_world_consumed.dds | 457×328 | 84af862910e6b8344dcff1e4b568bb8db2efa6ca58c688e6e480c1e22b01a424 | 2a753dab03d323372c28cc070af8b8ad7b8058b49ba77d5546fdc0450ccd65b4 | f46135f22d661af6700f8f096678caed57b76738e3aa59597cae73d1e7c454f8 | Exact decoded-pixel match; alpha 255 throughout |
| super_event_death_black_oath | Super-event image | gfx/super_events/010_death/super_event_death_black_oath.dds | 457×328 | 20e4c7290fe7abf96e2c39441be5150f4e1d9fb1aa13a7a56a2afcf445fdd675 | bd2550dbb2bd4496062e728830006a9f26c0cb3544e20a34d5dc89c2a6fe1264 | 78275eb9603c09f176c9447375673638e646faeec5da490205625882386b333b | Exact decoded-pixel match; alpha 255 throughout |

Output format for every asset: legacy one-level, uncompressed BGRA32 DDS; DDS_HEADER size 124; DDS_PIXELFORMAT size 32, flags 65, fourCC 0, bit count 32; masks 0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000; DDSCAPS_TEXTURE present; no mipmaps; exact length 128 + width × height × 4. Output alpha extrema were 255–255. The bytewise decoded RGBA comparison and matching pixel SHA-256 establish preservation of every decoded pixel.

Tools: Python 3.9.12, Pillow 11.1.0 for DDS decoding and pixel comparison, and .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py for DDS writing.
No recolouring, cropping, resizing, lossy compression, regeneration, or drawing was performed.

## Processed PNG previews

Each full-resolution PNG below was decoded from its repaired runtime DDS and verified for exact RGBA pixel equality and alpha 255 throughout. The repaired DDS files were SHA-256 checked before and after preview creation and were not modified.

| Asset ID | Processed PNG path | Dimensions | PNG SHA-256 | Source DDS SHA-256 | Pixel and alpha check |
| --- | --- | ---: | --- | --- | --- |
| news_event_death_mainland_reveal | docs/assets/010_death/dds_container_repair/processed_png/news_event_death_mainland_reveal.png | 397x153 | ea319915b175845bb11e1c4b8435e60b6ad5d560736d1cf48992abdccff12afd | 71ba59017a387d40806eebd5b5ebdd8430ec8f29c26a8f5b603f2fd00ab2513e | exact pixels; alpha 255?255 |
| news_event_death_defeated | docs/assets/010_death/dds_container_repair/processed_png/news_event_death_defeated.png | 397x153 | e8e1005d859bb3f0332d4e87a06fa1f7cc07e1772a63015bfa21fd8e196dcd6b | 8402aebefe5b52d1c2abee5236711671762cee3a7d759c350cc656aa2a9ba3de | exact pixels; alpha 255?255 |
| super_event_death_world_end | docs/assets/010_death/dds_container_repair/processed_png/super_event_death_world_end.png | 457x328 | 8a9722d6822f7a5c82e481f0e7776a1eb19f03a87630d40dcfa8f8c89cd1ed13 | e031d67d14d27744eaadea96ab7959e2f5075c88eda39620cf46d1f684a0ea14 | exact pixels; alpha 255?255 |
| super_event_death_defeat_aftermath | docs/assets/010_death/dds_container_repair/processed_png/super_event_death_defeat_aftermath.png | 457x328 | 6a848945893bf5d3478d1f4504c2c4023cc35cfcb344071762f1e6c722e96973 | 91cf3d61088f0930e9dd278b9a4aef7874dcebd8a965b1057d198c2e0d613351 | exact pixels; alpha 255?255 |
| super_event_death_world_consumed | docs/assets/010_death/dds_container_repair/processed_png/super_event_death_world_consumed.png | 457x328 | 7b68aeb71352c5d444fb586c31ba676d9cfdbe8f0ed01430c83e2348be7276c7 | 2a753dab03d323372c28cc070af8b8ad7b8058b49ba77d5546fdc0450ccd65b4 | exact pixels; alpha 255?255 |
| super_event_death_black_oath | docs/assets/010_death/dds_container_repair/processed_png/super_event_death_black_oath.png | 457x328 | f6777188be452b02311fcb9e9739dee933d11a888e79643e890c7b9041de25a9 | bd2550dbb2bd4496062e728830006a9f26c0cb3544e20a34d5dc89c2a6fe1264 | exact pixels; alpha 255?255 |

Contact sheet: docs/assets/010_death/dds_container_repair/contact_sheet.png (974?1142); SHA-256 e026a3a0d03076c9e84da30a5ea5c9639e1ff923c766674a0366fa4cbc4dcf25. Each tile uses the original native-size pixels; the longest side is 1142 px.
