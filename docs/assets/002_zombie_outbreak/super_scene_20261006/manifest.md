# Event002 zombie outbreak super-event art

Status: complete. Parent approved the exact-size and 4x review images on 2026-10-06, and the validated candidate now replaces the runtime texture at its stable path.

The final consumer is GFX_super_event_zombies in interface/chaosx_super_events.gfx, currently linked to gfx/super_events/002_zombie_outbreak/super_event_zombies.dds. The parent confirmed that the scene consumer is an opaque 457x328 canvas. No GFX file was edited.

I inspected the canonical event_art/super_event contact sheet and the super_event_world_in_fury.png reference, a 457x328 Chaos Redux source whose cataloged source is gfx/super_events/007_fury/super_event_world_in_fury.dds. It provides a precedent for a dense period crowd scene with a clear threat focal point across the opaque super-event canvas.

Source mode is generated fictional period documentary scene. ImageGen fits because this is an alternate-history 1936 outbreak and the scene does not require a verifiable historical photograph. The source depicts no identifiable person, actor, named figure, landmark, logo, or legible text. The art remains a fictional generated illustration; it is not described as real documentary evidence.

The original runtime DDS was copied byte-for-byte to notes/previous_unverified_master.dds before producing the new scene. Its SHA-256 is 11afee1fa72763cae98d42a696c7e4bbba84222f274192b30cb10c3633a8b7eb. The archived frame is a Night of the Living Dead group still. Its provenance and legal status remain unverified; this archive records the prior runtime asset only and does not assert legal clearance.

## Candidate artwork

The native ImageGen source is source_png/super_event_zombies_source.png. The exact prompt and tool settings are in prompts/super_event_zombies_imagegen.md. The source artifact ID and original default output location are in notes/asset_metadata_and_dds_validation.json.

The processed preview is processed_png/super_event_zombies.png at 457x328. The 2x and 4x review images are contact_sheets/super_event_zombies_2x.png and contact_sheets/super_event_zombies_4x.png. Because the source and consumer aspect ratios differ by less than 0.1 percent, processing resizes the complete opaque source to 457x328 without cropping scene content.

The repository-standard converter produced a candidate DDS at notes/super_event_zombies_candidate.dds. It has a valid legacy uncompressed BGRA header, one mip level, an opaque alpha channel, and exact decoded pixel equality with the processed PNG. Per-file hashes and structural details are in notes/asset_metadata_and_dds_validation.json.

The final runtime texture is gfx/super_events/002_zombie_outbreak/super_event_zombies.dds with SHA-256 748799a096c58a639d2eef1717142caaa2a9703807250c8ed74958f2ec83121c. Its bytes match the reviewed candidate DDS exactly. The old unverified file remains archived separately.
