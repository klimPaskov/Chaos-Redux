# Event 006 dormant reservation-art flag package

Status: complete for the 17 requested dormant API reservation tags. Every asset is marked `reservation_art`; none claims historical statehood, and none is wired to a playable package, country history, localisation, event, or `.gfx` definition.

Source mode: official ImageGen, one source result per visually distinct flag. The matching canonical reference family was inspected at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/flags/` (normal, medium, small, and contact sheet). The references informed HOI4 flag legibility and ladder sizing only; these reservation markers are fictional symbolic designs rather than historical reconstructions.

## Output contract

- Normal preview: `processed_png/normal/<TAG>.png` at `82x52`.
- Medium preview: `processed_png/medium/<TAG>.png` at `41x26`.
- Small preview: `processed_png/small/<TAG>.png` at `10x7`.
- Runtime normal TGA: `gfx/flags/<TAG>.tga`.
- Runtime medium TGA: `gfx/flags/medium/<TAG>.tga`.
- Runtime small TGA: `gfx/flags/small/<TAG>.tga`.
- Package copies of all runtime TGAs: `final_tga/<TAG>_{normal|medium|small}_<width>x<height>.tga`.
- Source masters: `source_png/<TAG>_imagegen_source.png`.
- Prompts: `prompts/<TAG>.txt`.
- Complete source/master/ladder review sheet: `contact_sheets/reservation_flag_ladders_contact_sheet.png`.
- Header and round-trip checks: `metadata/flag_validation.json`.
- SHA-256 inventory: `metadata/hashes.sha256`.

The source masters are 1619x971 ImageGen outputs. Processing center-crops only the generated flat flag to the HOI4 82:52 ratio and resizes it; no new geometry, tracing, palette substitution, or programmatic emblem was introduced. TGAs are uncompressed 32-bit BGRA with 8-bit alpha and bottom-left origin (`descriptor=0x08`), with opaque alpha. `build_flags.py` is retained as reproducible processing evidence.

## Reservation rows

| Tag | Reservation marker | Design direction | State |
| --- | --- | --- | --- |
| DJX | Tuareg/Kel placeholder reservation | Indigo, sand, teal; abstract desert star and caravan ring | dormant `reservation_art` |
| DMX | Toubou/Teda-Daza reservation | Charcoal, rust, turquoise; dune arcs and well ring | dormant `reservation_art` |
| DNX | Atlas/Kabyle-adjacent reservation | Cobalt, terracotta, ivory; mountain chevron and rosette | dormant `reservation_art` |
| ENX | Maasai territorial reservation | Maroon, black, ochre, cream; civic shield and bead ring | dormant `reservation_art` |
| EXX | Nama reservation | Navy, copper, sage, sand; desert-flower compass | dormant `reservation_art` |
| EYX | Ovambo reservation | Emerald, white, ochre; braided-river civic emblem | dormant `reservation_art` |
| FPX | Naga reservation | Crimson, forest, ivory; woven chevron and ridge | dormant `reservation_art` |
| GDX | Karen reservation | Vermilion, navy, cream, jade; mountain-river glyph | dormant `reservation_art` |
| GGX | Chin/Zo reservation | Plum, slate, gold, ivory; stacked ridge and rosette | dormant `reservation_art` |
| GHX | Arakan/Rakhine reservation | Sea teal, saffron, white, deep blue; coastal wave crown | dormant `reservation_art` |
| GLX | Hmong reservation | Midnight blue, moss, copper, ivory; spiral seed-pod shield | dormant `reservation_art` |
| HHX | Pueblo member reservation | Clay, turquoise, cream, charcoal; stepped window and sun disc | dormant `reservation_art` |
| HMX | Garifuna reservation | Ocean blue, coral, cream, green; interlocking tide arcs | dormant `reservation_art` |
| HQX | Specific Quechua member reservation | Rust, maize, teal, ivory; stepped mountain lozenge | dormant `reservation_art` |
| HTX | Gran Chaco member reservation | Dry green, ochre, charcoal, cream; thorn-tree civic emblem | dormant `reservation_art` |
| HWX | Amazonian river peoples reservation | Rainforest green, river blue, amber, cream; braided tributaries | dormant `reservation_art` |
| HXX | Historic maroon community reservation | Umber, red, gold, forest; broken-chain mountain ring | dormant `reservation_art` |

## Non-wiring boundary

No `.gfx` files, country files, gameplay scripts, localisation, or spreadsheet files were changed. These are loader-gap assets only. If a later accepted design promotes one reservation to a playable package, the main agent must perform the separate cosmetic-tag/country wiring and update the permanent Event 006 specification; this package intentionally does not imply that promotion.
