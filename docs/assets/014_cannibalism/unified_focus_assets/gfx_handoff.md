# Event 014 Unified Focus GFX Handoff

Target registry: `interface/014_cannibalism.gfx`.

For every unified focus ID `<id>`:

- static sprite: `GFX_goal_<id>`;
- shine sprite: `GFX_goal_<id>_shine` using `gfx/FX/buttonstate.lua`;
- texture: `gfx/interface/goals/014_cannibalism/goal_<id>.dds`;
- dimensions/format: 94x86, uncompressed 32-bit BGRA, one image level, true alpha.

`validation/unified_focus_gfx_handoff.tsv` expands this contract into all 108 exact focus IDs and paths. `validation/unified_focus_asset_validation.tsv` proves each runtime texture is present, unique, correctly formatted, and hash-identical to its package DDS.
