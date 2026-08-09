# Event 012 Africa super-event image manifest

Status: complete for the four requested generated image packages, pending parent review and runtime consumer validation.

Date: 2026-08-09.

Source mode: `generated_alternate_history` through the built-in `$imagegen` workflow. Generation fits because all four accepted roles are fictional or alternate-history political thresholds and need unique emotional compositions rather than a real photographed person, battle, place, or archival artifact.

Canonical reference inspected: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/super_event/` including `contact_sheet.png`, `super_event_006_league_formation.png`, `super_event_angel_directorate.png`, `super_event_angelic_world_order.png`, `super_event_divine_sovereignty.png`, and `super_event_world_in_fury.png`.

Processing: each generated RGB source was cover-fitted to the exact `457x328` consumer canvas with Lanczos resampling, then received a restrained contrast and sharpness lift for small UI readability and was saved as RGBA PNG. Each processed PNG was converted with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` to an uncompressed 32-bit BGRA DDS and decoded back for the round-trip contact sheet.

| Role | Source PNG | Processed PNG | Final DDS | Sprite name | Target `.gfx` | Runtime path | Source hash | Processed hash | DDS hash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Africa Is One | `docs/assets/012_africa/super_events/images_final/sources/source_super_event_012_africa_africa_is_one.png` | `docs/assets/012_africa/super_events/images_final/processed/processed_super_event_012_africa_africa_is_one.png` | `gfx/super_events/012_africa/super_event_012_africa_africa_is_one.dds` | `GFX_super_event_012_africa_africa_is_one` | `interface/012_africa_event_pictures.gfx` | slot 101, existing sprite and path preserved | `3e1ed9586bcb8b91ad829fcb982b1242088170f3dce60389a9886b357defd944` | `85996b22965540941bc617ef4758444b1267d1f038ba466e758d0b572ecac958` | `f45e4fa9910d6f492819700ea45efd98cf6b4f8ca8fd3827b75dcff086a07867` |
| Scramble Response | `docs/assets/012_africa/super_events/images_final/sources/source_super_event_012_africa_scramble_response.png` | `docs/assets/012_africa/super_events/images_final/processed/processed_super_event_012_africa_scramble_response.png` | `gfx/super_events/012_africa/super_event_012_africa_scramble_response.dds` | `GFX_super_event_012_africa_scramble_response` | `interface/012_africa_event_pictures.gfx` | slot 102, existing sprite and path preserved | `3697f8c4de08bb22248ec103265e4258ad13f4a01c0b4a4b171088fe973a4562` | `8566fe5465b3dd86560ae4f4986ff694e26426d167d0bbf3b19119a95f1c3442` | `778cf740a08c97e36066d2f79e686f659b685c0aaa0705a0831e8be7ede03bd4` |
| Continental Wars | `docs/assets/012_africa/super_events/images_final/sources/source_super_event_012_africa_continental_wars.png` | `docs/assets/012_africa/super_events/images_final/processed/processed_super_event_012_africa_continental_wars.png` | `gfx/super_events/012_africa/super_event_012_africa_continental_wars.dds` | `GFX_super_event_012_africa_continental_wars` | `interface/012_africa_event_pictures.gfx` | slot 103, existing sprite and path preserved | `a023b2b1a501d6f86c73c01dfe3dfbaec16b851df1e951898b2d2a1e3f657328` | `490fa5ca9367a3b8a5d97327865b30cc78d1952fffb540f68a040074fedc10d9` | `26407f06589a53da27a2c9685a57f30c5fc32cd34e4a8edc08e5f43bbe536612` |
| The World | `docs/assets/012_africa/super_events/images_final/sources/source_super_event_012_africa_the_world.png` | `docs/assets/012_africa/super_events/images_final/processed/processed_super_event_012_africa_the_world.png` | `gfx/super_events/012_africa/super_event_012_africa_the_world.dds` | `GFX_super_event_012_africa_the_world` | `interface/012_africa_event_pictures.gfx` | slot 104, existing sprite and path preserved | `f127691fdf1d2a7ec6310fe8cc51d12d436158560ae289e3d53954bd750f194f` | `ba149f7f2e336a1f1537a97b87378cc008ad4bd5294eca10c9be778fa66a6a9` | `ea58405ade57f2cbd9a25cd7265a4092373975e48b3100a3884594398c244061` |

Distinctness review: Africa Is One is an institutional congress with rail and harbor continuity. Scramble Response is a fortified port command scene with distant outside fleets. Continental Wars is a broken railway crossing with rival continental armies, armored trains, and aircraft. The World is a postwar global council with an empty final seat, diverse delegates, and lowered standards.

Review package: `docs/assets/012_africa/super_events/images_final/contact/super_event_012_africa_images_contact_sheet.png`.

Runtime status: the four existing dormant DDS files were replaced in place with the new generated art. No `.gfx`, gameplay, localisation, GUI, event, sound, focus, country, or spreadsheet files were edited by this package.

Open item: parent should review the contact sheet and run its normal runtime consumer checks before promoting the temporary `docs/assets/012_africa/` workspace to permanent documentation or cleanup.

