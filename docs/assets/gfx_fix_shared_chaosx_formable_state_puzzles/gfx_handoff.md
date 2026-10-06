# Shared formable state-puzzle GFX handoff

Target texture registry: `interface/chaosx_formable_state_puzzles.gfx`.

All existing sprite names and texture paths remain in place; the 272 changed runtime DDS files were replaced at those current texture paths, and the exact sprite-name-to-path mapping and final hashes are in `processed_v3/promotion_v3.json`.

The 260 palette outputs retain their registered dimensions except the ring-overlap states North Sea 932 and Scandinavia 910, whose unresolved and qualifying textures are now `15x15`.

The 12 ring-only textures are GOE Hindustan 320 (`15x15`), 321 (`15x16`), and 985 (`15x16`); Maghreb 783 (`15x15`); Greater Italy 116 (`15x16`); and Latin Africa 796 (`16x16`), each with unresolved and qualifying variants.

The parent applied the eight iconType position edits to preserve each original core's map anchor by moving the leaf up and left by its core padding; all eight current GUI coordinates match this table:

| GUI file | IconType leaf | Old position | New position | Core padding | New texture size |
| --- | --- | --- | --- | --- | --- |
| `interface/chaosx_formable_state_puzzle_form_north_sea_empire.gui` | `form_north_sea_empire_state_932_piece` | `(126, 140)` | `(121, 135)` | `(5, 5)` | `15x15` |
| `interface/chaosx_formable_state_puzzle_form_scandinavia.gui` | `form_scandinavia_state_910_piece` | `(239, 164)` | `(234, 159)` | `(5, 5)` | `15x15` |
| `interface/chaosx_formable_state_puzzle_goe_form_hindustan.gui` | `goe_form_hindustan_state_320_piece` | `(220, 149)` | `(215, 144)` | `(5, 5)` | `15x15` |
| `interface/chaosx_formable_state_puzzle_goe_form_hindustan.gui` | `goe_form_hindustan_state_321_piece` | `(190, 130)` | `(185, 125)` | `(5, 5)` | `15x16` |
| `interface/chaosx_formable_state_puzzle_goe_form_hindustan.gui` | `goe_form_hindustan_state_985_piece` | `(267, 60)` | `(262, 56)` | `(5, 4)` | `15x16` |
| `interface/chaosx_formable_state_puzzle_unite_maghreb.gui` | `unite_maghreb_state_783_piece` | `(122, 66)` | `(117, 61)` | `(5, 5)` | `15x15` |
| `interface/chaosx_formable_state_puzzle_proclaim_greater_italy.gui` | `proclaim_greater_italy_state_116_piece` | `(185, 157)` | `(181, 152)` | `(4, 5)` | `15x16` |
| `interface/chaosx_formable_state_puzzle_unite_latin_africa.gui` | `unite_latin_africa_state_796_piece` | `(181, 105)` | `(176, 101)` | `(5, 4)` | `16x16` |

There is one static iconType leaf per state in each listed GUI; no second qualifying-specific leaf was found in these blocks. The parent applied the positions listed above and verified each current local coordinate. The parent's before/after MCP inspect/render attempts for all six windows returned `Transport closed`, so local mosaic approval and source-coordinate checks are the available review evidence.

The nine canonical `docs/formables/state_puzzles/*/manifest.json` records now contain current DDS hashes, per-variant processed-PNG hashes for all 382 declared paths, padded bitmap bboxes or `canvas_position` aliases for the eight ring states, and verified `manifest_sha256` digests. The five legacy schemas retain their `assets[].png_sha256` fields, and the Maghreb, Greater Italy, and Latin Africa states now have matching per-variant `png_sha256` maps. Details are in `canonical_manifest_validation_v2.json`, `canonical_manifest_reconcile_final_v1.json`, and the two focused patch files.

The existing FORM11/FORM18 sprites remain at the paths and hashes recorded by committed Event006 package `1cb4d061f`; FORM03 state 36 remains unchanged. All 382 path-backed processed previews now exist. The 116 previews restored from runtime DDS bytes are documented as derived previews rather than original source layers. The GOE Hindustan manifest has no processed-PNG path, so no canonical path was invented for its six candidate PNGs.

This asset worker updated the nine canonical puzzle manifests and their 382 declared processed-PNG paths under the parent's expanded grant; the parent separately edited the six GUI files. No `.gfx`, gameplay, localisation, or event files were edited, and the game was not run.
