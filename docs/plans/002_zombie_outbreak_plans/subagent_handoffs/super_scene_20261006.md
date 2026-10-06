# Event002 super-event scene handoff

Disposition: implemented. Parent approved the exact-size and 4x previews on 2026-10-06. The original generated scene, processed 457x328 PNG, 2x/4x reviews, and validated DDS are retained in the source workspace, and the validated DDS now replaces the prior unverified runtime still.

## Review files

- Processed review image: docs/assets/002_zombie_outbreak/super_scene_20261006/processed_png/super_event_zombies.png
- 2x review: docs/assets/002_zombie_outbreak/super_scene_20261006/contact_sheets/super_event_zombies_2x.png
- 4x review: docs/assets/002_zombie_outbreak/super_scene_20261006/contact_sheets/super_event_zombies_4x.png
- Exact native prompt: docs/assets/002_zombie_outbreak/super_scene_20261006/prompts/super_event_zombies_imagegen.md
- Candidate DDS: docs/assets/002_zombie_outbreak/super_scene_20261006/notes/super_event_zombies_candidate.dds

## Runtime ownership and replacement gate

Only runtime asset path in scope: gfx/super_events/002_zombie_outbreak/super_event_zombies.dds.

Current sprite consumer: GFX_super_event_zombies in interface/chaosx_super_events.gfx. The existing sprite name and GFX path are unchanged. No GFX, event, localisation, GUI, gameplay, spreadsheet, portrait, sound, or other asset file was edited.

The prior unverified group still is archived byte-exact at docs/assets/002_zombie_outbreak/super_scene_20261006/notes/previous_unverified_master.dds with SHA-256 11afee1fa72763cae98d42a696c7e4bbba84222f274192b30cb10c3633a8b7eb. No legal clearance is asserted for that prior still. The installed runtime DDS has SHA-256 748799a096c58a639d2eef1717142caaa2a9703807250c8ed74958f2ec83121c, matching the reviewed candidate exactly.

The approved candidate was copied to the sole runtime path above and its hash equality was verified. Do not edit interface/chaosx_super_events.gfx.

## Candidate validation and limits

The installed DDS is 457x328, uncompressed 32-bit BGRA, 599712 bytes, has no mipmaps and an opaque alpha channel, and decodes pixel-exactly to the processed PNG. The original and final hashes and DDS header evidence are in notes/asset_metadata_and_dds_validation.json.

The generated scene is explicitly fictional period art, not archival photography. Its prompt and source-mode rationale are retained with the source PNG. It contains no identifiable real person or portrait, no text or logos, no modern props, and no gore. The parent owns the final shared-window render review; no game was launched for this task.

The exact task-owned runtime, source, review, archive, metadata, and handoff path list is docs/assets/002_zombie_outbreak/super_scene_20261006/notes/owned_files_manifest.txt.
