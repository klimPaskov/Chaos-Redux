# Event 010 Death DDS Handoff

Status: complete for container repair; all six runtime paths and filenames are unchanged.
Source mode: inherited DDS; original master provenance unresolved.
No ImageGen proof is available or claimed. No GFX files were edited.

| Asset ID | Final DDS path | Existing sprite name | Existing target .gfx / consumer | Use |
| --- | --- | --- | --- | --- |
| news_event_death_mainland_reveal | gfx/event_pictures/010_death/news_event_death_mainland_reveal.dds | `GFX_news_event_death_mainland_reveal` | `interface/chaosx_pictures.gfx:68`, rechecked by the parent | News event art, 397×153, opaque full canvas |
| news_event_death_defeated | gfx/event_pictures/010_death/news_event_death_defeated.dds | `GFX_news_event_death_defeated` | `interface/chaosx_pictures.gfx:72`, rechecked by the parent | News event art, 397×153, opaque full canvas |
| super_event_death_world_end | gfx/super_events/010_death/super_event_death_world_end.dds | `GFX_super_event_death_world_end` | `interface/chaosx_super_events.gfx:72`, rechecked by the parent | Super-event image, 457×328, opaque full canvas |
| super_event_death_defeat_aftermath | gfx/super_events/010_death/super_event_death_defeat_aftermath.dds | `GFX_super_event_death_defeat` | `interface/chaosx_super_events.gfx:76`, rechecked by the parent | Super-event image, 457×328, opaque full canvas |
| super_event_death_world_consumed | gfx/super_events/010_death/super_event_death_world_consumed.dds | `GFX_super_event_death_world_consumed` | `interface/chaosx_super_events.gfx:80`, rechecked by the parent | Super-event image, 457×328, opaque full canvas |
| super_event_death_black_oath | gfx/super_events/010_death/super_event_death_black_oath.dds | `GFX_super_event_death_black_oath` | `interface/chaosx_super_events.gfx:84`, rechecked by the parent | Super-event image, 457×328, opaque full canvas |

The repaired DDS files are ready at the same paths consumed before this task. The parent should leave the established registrations and consumer identifiers unchanged. Full archive hashes, output hashes, exact DDS format, dimensions, per-asset decoded-pixel hashes, and alpha evidence are in manifest.md; original source bytes are under source_originals/.

## Processed PNG previews

Contact sheet: docs/assets/010_death/dds_container_repair/contact_sheet.png (974x1142), SHA-256 e026a3a0d03076c9e84da30a5ea5c9639e1ff923c766674a0366fa4cbc4dcf25; longest side 1142 px.

| Asset ID | Full-resolution PNG preview | Dimensions | PNG SHA-256 |
| --- | --- | ---: | --- |
| news_event_death_mainland_reveal | docs/assets/010_death/dds_container_repair/processed_png/news_event_death_mainland_reveal.png | 397x153 | ea319915b175845bb11e1c4b8435e60b6ad5d560736d1cf48992abdccff12afd |
| news_event_death_defeated | docs/assets/010_death/dds_container_repair/processed_png/news_event_death_defeated.png | 397x153 | e8e1005d859bb3f0332d4e87a06fa1f7cc07e1772a63015bfa21fd8e196dcd6b |
| super_event_death_world_end | docs/assets/010_death/dds_container_repair/processed_png/super_event_death_world_end.png | 457x328 | 8a9722d6822f7a5c82e481f0e7776a1eb19f03a87630d40dcfa8f8c89cd1ed13 |
| super_event_death_defeat_aftermath | docs/assets/010_death/dds_container_repair/processed_png/super_event_death_defeat_aftermath.png | 457x328 | 6a848945893bf5d3478d1f4504c2c4023cc35cfcb344071762f1e6c722e96973 |
| super_event_death_world_consumed | docs/assets/010_death/dds_container_repair/processed_png/super_event_death_world_consumed.png | 457x328 | 7b68aeb71352c5d444fb586c31ba676d9cfdbe8f0ed01430c83e2348be7276c7 |
| super_event_death_black_oath | docs/assets/010_death/dds_container_repair/processed_png/super_event_death_black_oath.png | 457x328 | f6777188be452b02311fcb9e9739dee933d11a888e79643e890c7b9041de25a9 |

Every preview decodes to the same RGBA pixels as its final DDS and has alpha 255 throughout. Runtime DDS paths, bytes, registrations, and consumers were left unchanged.

The parent reviewed the six images through `contact_sheet_review_1100.png` (938x1100) and verified the six existing texture registrations above.
