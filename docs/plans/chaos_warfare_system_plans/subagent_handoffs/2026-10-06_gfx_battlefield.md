# Chemical ground-raid map glyphs

Disposition: implemented, parent accepted within the explicit graphics-repair task.
Four 32x32 gold/beige glyphs depict a gas cylinder, a Livens tube battery, a chemical shell and an armored delivery vehicle.
They replace oversized 64x64 painted scenes in the native raid map consumer.
The parent reviewed their native and four-times previews and approved the distinct silhouettes, clean alpha and complete framing.
Final DDS pixels match the approved processed PNGs.
The source prompts, original generated subjects and review evidence remain under `docs/assets/chaos_warfare_system/2026-10-06_gfx_primary/` while the graphics package is active.
Contact sheet: `contact_sheets/cbrn_battlefield_map_glyphs_native_4x.png`.
Conversion evidence: `notes/battlefield_runtime_alpha.json`.
Existing live sprite names and raid references are retained.
The unconsumed Cycle Agent sprite and its dedicated texture are removed after an active-registry reference check.
The GFX header describes the actual map consumer.

The orchestrator should prepare one raid from each ground family and check that the four map markers fit their native 32px slots without a square backdrop, oversized scene or crop.
