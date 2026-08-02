# Event 020 RTA hierarchy focus icon manifest

Status: `complete`.

This package contains six distinct generated symbolic focus icons for the RTA rat hierarchy branch. The final assets use the existing Event 020 focus-icon convention: transparent, one-level uncompressed BGRA DDS at `94x86`. The matching canonical national-focus contact sheet and individual references were inspected before generation. Parent-owned `.gfx`, focus, and localisation wiring is promoted and verified in `interface/020_black_plague_rat_identity.gfx`, `common/national_focus/020_black_plague_rat_focus.txt`, and `localisation/english/020_black_plague_rat_l_english.yml`.

## Requirement-to-runtime crosswalk

| Focus id | Asset type / use | Sprite | Source PNG | Processed PNG | Final DDS | Target / `.gfx` | State |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `black_plague_rat_four_mouths` | Focus icon / RTA hierarchy route | `GFX_goal_black_plague_rat_four_mouths` | `source_png/focus_black_plague_rat_four_mouths_imagegen_source.png` | `processed_png/goal_black_plague_rat_four_mouths.png` | `gfx/interface/goals/020_black_plague/goal_black_plague_rat_four_mouths.dds` | `94x86` / `interface/020_black_plague_rat_identity.gfx` | Complete |
| `black_plague_rat_choose_a_voice` | Focus icon / RTA hierarchy route | `GFX_goal_black_plague_rat_choose_a_voice` | `source_png/focus_black_plague_rat_choose_a_voice_imagegen_source.png` | `processed_png/goal_black_plague_rat_choose_a_voice.png` | `gfx/interface/goals/020_black_plague/goal_black_plague_rat_choose_a_voice.dds` | `94x86` / `interface/020_black_plague_rat_identity.gfx` | Complete |
| `black_plague_rat_read_the_marks` | Focus icon / RTA hierarchy route | `GFX_goal_black_plague_rat_read_the_marks` | `source_png/focus_black_plague_rat_read_the_marks_imagegen_source.png` | `processed_png/goal_black_plague_rat_read_the_marks.png` | `gfx/interface/goals/020_black_plague/goal_black_plague_rat_read_the_marks.dds` | `94x86` / `interface/020_black_plague_rat_identity.gfx` | Complete |
| `black_plague_rat_many_nests_one_signal` | Focus icon / RTA hierarchy route | `GFX_goal_black_plague_rat_many_nests_one_signal` | `source_png/focus_black_plague_rat_many_nests_one_signal_imagegen_source.png` | `processed_png/goal_black_plague_rat_many_nests_one_signal.png` | `gfx/interface/goals/020_black_plague/goal_black_plague_rat_many_nests_one_signal.dds` | `94x86` / `interface/020_black_plague_rat_identity.gfx` | Complete |
| `black_plague_rat_fang_above_the_warren` | Focus icon / RTA hierarchy route | `GFX_goal_black_plague_rat_fang_above_the_warren` | `source_png/focus_black_plague_rat_fang_above_the_warren_imagegen_source.png` | `processed_png/goal_black_plague_rat_fang_above_the_warren.png` | `gfx/interface/goals/020_black_plague/goal_black_plague_rat_fang_above_the_warren.dds` | `94x86` / `interface/020_black_plague_rat_identity.gfx` | Complete |
| `black_plague_rat_stolen_route_memory` | Focus icon / RTA hierarchy route | `GFX_goal_black_plague_rat_stolen_route_memory` | `source_png/focus_black_plague_rat_stolen_route_memory_imagegen_source.png` | `processed_png/goal_black_plague_rat_stolen_route_memory.png` | `gfx/interface/goals/020_black_plague/goal_black_plague_rat_stolen_route_memory.dds` | `94x86` / `interface/020_black_plague_rat_identity.gfx` | Complete |

## Source mode and visual directions

- Source mode: official built-in ImageGen, generated from scratch on a flat `#00ff00` chroma-key background, then locally alpha-extracted with `remove_chroma_key.py`.
- Prompt record: `prompts/rat_hierarchy_focus_icons_2026-08-01.md` contains the six exact generation briefs.
- All six source masters are retained under `source_png/`; alpha extraction evidence is retained under `alpha_intermediate/`.
- `four_mouths`: four snarling rat muzzles around a central iron knot, representing rival voices.
- `choose_a_voice`: one commanding rat with a signal horn and amber eye, representing a chosen voice.
- `read_the_marks`: a rat claw over carved tunnel marks, representing emergent route-reading.
- `many_nests_one_signal`: three nests linked to one brass beacon, representing distributed broods sharing a pulse.
- `fang_above_the_warren`: one crown-mounted fang suspended above a warren, representing dominant authority.
- `stolen_route_memory`: a rat wrapped around a torn route ribbon and key, representing a remembered stolen path.
- No text, flags, watermarks, UI frame, modern objects, or explicit gore are present in the generated direction.

## Dimensions and hashes

All processed PNGs and runtime DDS files are `94x86`. DDS validation: 128-byte header, `DDS_HEADER` size `124`, `DDS_PIXELFORMAT` size `32`, flags `65`, zero fourCC, 32-bit BGRA masks `0x00FF0000/0x0000FF00/0x000000FF/0xFF000000`, `DDSCAPS_TEXTURE` `0x1000`, exact length `32464` bytes, and alpha range `0..255` with transparent corners.

| Asset | Dimensions | SHA-256 |
| --- | ---: | --- |
| `source_png/focus_black_plague_rat_four_mouths_imagegen_source.png` | 1312x1199 | `daca4c63187c912b932d894a137458187da287353ff2cffb619ad00fbe8292ea` |
| `processed_png/goal_black_plague_rat_four_mouths.png` | 94x86 | `bf6f19d6d218e4513f021d398bfe8771b21365c83cd59b7d60d191add0be86b8` |
| `gfx/interface/goals/020_black_plague/goal_black_plague_rat_four_mouths.dds` | 94x86 | `583adc075c51b36ffb75d4b875c4fa33d7c15e9952f801f17d02eba7f5aae439` |
| `source_png/focus_black_plague_rat_choose_a_voice_imagegen_source.png` | 1168x1346 | `43cb04ea057dbb461724c7ef6f88993295df74082d870168403fd9ca814bbd23` |
| `processed_png/goal_black_plague_rat_choose_a_voice.png` | 94x86 | `e8c0fc153b95a0feb69453a9f9107082e016ca047d66a8f834fbadc274fc0e22` |
| `gfx/interface/goals/020_black_plague/goal_black_plague_rat_choose_a_voice.dds` | 94x86 | `bfb8c504bd4621ce8a4745ea1e116c13c223a82b5a7e7d8f68c2e2664517a12f` |
| `source_png/focus_black_plague_rat_read_the_marks_imagegen_source.png` | 1312x1199 | `82331143d34dba420321353302b14dee6804f5b49232f9bc9a38f2dbda4897b6` |
| `processed_png/goal_black_plague_rat_read_the_marks.png` | 94x86 | `3441a8edf3756e2e09c13f038769e6e038296f038ac5034397cc60381abefb91` |
| `gfx/interface/goals/020_black_plague/goal_black_plague_rat_read_the_marks.dds` | 94x86 | `2eb8da5ecd2d5b15d6a38dffd0273f35db0fdc04bc5a8d541f47a6ac42eabaf2` |
| `source_png/focus_black_plague_rat_many_nests_one_signal_imagegen_source.png` | 1312x1199 | `785b4a4cac564cc374dc110f4f942f6a39c79eead1fd3ba452e3dfc1458c0dea` |
| `processed_png/goal_black_plague_rat_many_nests_one_signal.png` | 94x86 | `4f34d1fa37a486c5c39464c8652ed2946599f19c35237fce8f749dff13ac2e51` |
| `gfx/interface/goals/020_black_plague/goal_black_plague_rat_many_nests_one_signal.dds` | 94x86 | `c3226f927a1a88e7881fb9d3b0f32a36f03975370ea1d05d8e48ede7f2f0e2dd` |
| `source_png/focus_black_plague_rat_fang_above_the_warren_imagegen_source.png` | 1168x1347 | `acc2b664ba15d26f9342833505ed01e8312249126181edfae5d9eab3484c165f` |
| `processed_png/goal_black_plague_rat_fang_above_the_warren.png` | 94x86 | `24b7edbbaf6721d13714e256ff0516068261a9162494cbdf424aaa9ae4a4c30e` |
| `gfx/interface/goals/020_black_plague/goal_black_plague_rat_fang_above_the_warren.dds` | 94x86 | `caf5491972edcdae16b9ebd91dbe8b01a9093e710beec742e31aa7fa37a23283` |
| `source_png/focus_black_plague_rat_stolen_route_memory_imagegen_source.png` | 1312x1199 | `994f39b159e09ff7f4473e2436971c5ea8bc57b49f02bcc1c87f24147bdf36dd` |
| `processed_png/goal_black_plague_rat_stolen_route_memory.png` | 94x86 | `27dfc87069dc1d0cbf09631ab24d5a3c0c80680e5c8e65cc0a32da11b8b2c58c` |
| `gfx/interface/goals/020_black_plague/goal_black_plague_rat_stolen_route_memory.dds` | 94x86 | `cd9fe5057c16342cc70280565bce22d327cb70e221fa60232b30c1e5da9a5e40` |
| `contact_sheets/event020_rat_hierarchy_contact_sheet.png` | 780x440 | `7fdbee9530cb3e4da747b9b5cf530df84cb15110a904c5c12d6369dc8a8d2827` |

## Parent-owned wiring boundary

The parent agent's wiring handoff is complete: all six base sprites use the exact names and DDS paths in `gfx_handoff.md`, and every focus consumer has matching localisation. Existing Event 020 focus icons also expose `_shine` sprites through `gfx/FX/buttonstate.lua`; no additional shine entry was required by the live focus-tree convention. No `.gfx`, focus, localisation, or gameplay file was edited in this package.
