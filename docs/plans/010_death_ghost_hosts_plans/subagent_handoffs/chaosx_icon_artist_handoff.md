# Death ghost counter artist handoff

Status: `runtime_wired_needs_user_visual_review`.

The bespoke vanilla-green counter package was rebuilt as an isolated asset handoff under `docs/assets/010_death/models_3d/ghost_hosts/counter_handoff/` from the two surviving source atlases named by the parent prompt. No new source image family was generated, and no file outside the bounded counter handoff or this parent handoff was edited.

## Completed assets

| Surface | Sprite token | Native canvas | Frame layout | Processed PNG SHA-256 | Final DDS | Final DDS SHA-256 |
| --- | --- | ---: | --- | --- | --- | --- |
| Large land counter | `GFX_unit_death_ghost_icon_medium` | `152x42` | two adjacent `76x42` frames | `4EB58FCCFFF21F26A47B19BE59BACF7316498DA5108D848AEC194DD30651681` | `counter_handoff/dds/gfx/interface/counters/divisions_large/unit_death_ghost_icon.dds` | `4D239545067E785A8F631E1DFF14E08C55AF530D5ECBED651234F6D4B5B554BA` |
| On-map counter | `GFX_unit_death_ghost_icon_medium_white` | `60x12` | two adjacent `30x12` frames | `FD36F0DAA68D8539A32E3000B142CEFE149DBC22E05A04648A6BABC473B195E8` | `counter_handoff/dds/gfx/interface/counters/divisions_small/onmap_unit_death_ghost_icon.dds` | `2B0751C499C752FB984A72F59C1DCCAF5AC34BE674509379D018CA74898EA4C9` |
| Small texticon | `GFX_unit_death_ghost_icon_small` | `60x12` | two adjacent `30x12` frames | `BC30D121D1925956FE4455F77CCB673C4A168985CC8DFA0F9DB2757B60E0BBBA` | `counter_handoff/dds/gfx/texticons/unit_death_ghost_icon_small.dds` | `D80AD956975949DBC3C3AF6863760CE91D29FBADF97B37342951052B07B0FE58` |

Frame 0 is the normal state and frame 1 is the alternate state for every token. The large counter uses a muted vanilla-green normal silhouette and a separate pale schematic alternate glyph. The `_medium_white` on-map counter uses white/grey treatment for both frames, matching the inspected land map family. The small texticon uses a vanilla-green normal silhouette and pale schematic alternate glyph.

## Exact source evidence

| Source atlas | Dimensions | SHA-256 |
| --- | ---: | --- |
| `counter_handoff/source/ghost_counter_atlas_land_map.png` | `1690x931` | `BFA495295B5DAC597DDEFBF4A2C6BE2D59A295D90CC7250C7286713772CEFC2E` |
| `counter_handoff/source/ghost_counter_atlas_small.png` | `1568x1003` | `2DE949CBECA10B57A96208F806862A05DB2103F0B33C047890BFD07D2127DD61` |

The source atlas bytes remain unchanged. The official ImageGen transparent-background workflow was used only for the required local chroma-key-to-alpha processing with the installed helper; no alternate source prompt or duplicate generation was introduced.

## Vanilla inspection and validation

The exact installed definitions and DDS files were inspected before processing:

- `interface/subuniticons.gfx#GFX_unit_infantry_icon_medium` -> `gfx/interface/counters/divisions_large/unit_infantry_icon.dds`, `152x42`, `noOfFrames = 2`.
- `interface/subuniticons.gfx#GFX_unit_infantry_icon_medium_white` -> `gfx/interface/counters/divisions_small/onmap_unit_infantry_icon.dds`, `60x12`, `noOfFrames = 2`.
- `interface/texticons.gfx#GFX_unit_infantry_icon_small` -> `gfx/texticons/unit_infantry_icon_small.dds`, `60x12`, `noOfFrames = 2`, `legacy_lazy_load = no`.

The canonical contact sheets under the skill-local `vanilla_reference/units/land/counters_large/` and `map_counters/` folders were inspected before individual references. Palette, alpha bounds, frame order, and visual scale evidence is recorded in `counter_handoff/validation/installed_definition_audit.json` and `counter_handoff/validation/reference_stats.json`.

`counter_handoff/validation/dds_roundtrip.json` records `pixel_equal = true`, `different_channels = 0`, and `max_channel_difference = 0` for all three outputs. Each output is a native-size, one-level, uncompressed BGRA DDS with valid header masks, texture caps, exact file length, and transparent pixels.

`counter_handoff/contact_sheet.png` shows both exact source atlases, processed native canvases, enlarged smooth previews, decoded DDS previews, frame boundaries, and inspected vanilla evidence over checkerboard transparency.

## Parent-owned handoff

The parent copied the DDS files from `counter_handoff/dds/` into the runtime `gfx/` paths, added the three sprite definitions in `interface/chaosx_subuniticons.gfx` and `interface/chaosx_texticons.gfx`, and linked all three Death ghost consumers through `sprite = death_ghost`. Live HOI4 visual acceptance remains user-owned. A ready-to-copy snippet and the exact target files remain in `counter_handoff/gfx_handoff.md`.

## Changed files

- Updated `docs/plans/010_death_ghost_hosts_plans/subagent_handoffs/chaosx_icon_artist_handoff.md` with this final handoff.
- Added `counter_handoff/manifest.md`, `counter_handoff/gfx_handoff.md`, and `counter_handoff/source/imagegen_provenance.md`.
- Added the selected chroma-key alpha atlases under `counter_handoff/processed/source_alpha_contract/`, target processed strips under `counter_handoff/processed/`, per-frame PNGs under `counter_handoff/processed/frames/`, and checkerboard/native/smooth previews under `counter_handoff/previews/`.
- Added `counter_handoff/contact_sheet.png`, the three final DDS files under `counter_handoff/dds/`, and validation evidence under `counter_handoff/validation/`.
- Reused `counter_handoff/source/ghost_counter_atlas_land_map.png`, `counter_handoff/source/ghost_counter_atlas_small.png`, and `counter_handoff/source/source_manifest.json` without changing their source bytes or source manifest content.

Parent runtime wiring changed `common/units/010_death_ghost_hosts.txt`, `interface/chaosx_subuniticons.gfx`, and `interface/chaosx_texticons.gfx`; the three runtime counter DDS files were copied byte-for-byte from this handoff. The package remains `runtime_wired_needs_user_visual_review` until live HOI4 visual acceptance is complete.
