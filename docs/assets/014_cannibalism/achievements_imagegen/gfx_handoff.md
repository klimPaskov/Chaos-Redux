# Event 014 Achievement GFX Handoff

Target registry: `interface/014_cannibalism_achievements.gfx`.

For each current `<achievement_id>`:

- completed sprite: `GFX_achievement_<achievement_id>`;
- grey sprite: `GFX_achievement_<achievement_id>_grey`;
- not-eligible sprite: `GFX_achievement_<achievement_id>_not_eligible`;
- runtime triplet: `gfx/achievements/<achievement_id>{,_grey,_not_eligible}.dds`;
- exact format: 64x64, fully opaque, uncompressed one-image-level BGRA DDS.

`validation/achievement_gfx_handoff.tsv` expands the contract to all 18 exact IDs. `validation/achievement_icon_validation.tsv` proves all 54 registered paths are present, package/runtime DDS hashes match, completed masters are unique, grey variants are monochrome, and not-eligible variants contain the red project overlay.
