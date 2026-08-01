# Event 012 Africa route identity art v2 handoff

Status: all seven requested identity packages are complete and ready for parent wiring. No fallback or copied/recoloured route was used. No `.gfx`, gameplay, localisation, country, GUI, focus, decision, or workbook file was edited.

## Runtime files

### Flat flag ladders

Each listed tag has all three exact HOI4 ladder files. Normal is 82x52, medium is 41x26, small is 10x7. Every TGA is 32-bit RGBA, type-2 uncompressed, descriptor byte 8 (bottom-left origin; no top-origin bit).

- `AFRICA_CHARTER_FEDERATION`: `gfx/flags/AFRICA_CHARTER_FEDERATION.tga`, `gfx/flags/medium/AFRICA_CHARTER_FEDERATION.tga`, `gfx/flags/small/AFRICA_CHARTER_FEDERATION.tga`
- `AFRICA_CONTINENTAL_REPUBLIC`: `gfx/flags/AFRICA_CONTINENTAL_REPUBLIC.tga`, `gfx/flags/medium/AFRICA_CONTINENTAL_REPUBLIC.tga`, `gfx/flags/small/AFRICA_CONTINENTAL_REPUBLIC.tga`
- `AFRICA_UNITED_KINGDOMS`: `gfx/flags/AFRICA_UNITED_KINGDOMS.tga`, `gfx/flags/medium/AFRICA_UNITED_KINGDOMS.tga`, `gfx/flags/small/AFRICA_UNITED_KINGDOMS.tga`
- `AFRICA_PEOPLES_UNION`: `gfx/flags/AFRICA_PEOPLES_UNION.tga`, `gfx/flags/medium/AFRICA_PEOPLES_UNION.tga`, `gfx/flags/small/AFRICA_PEOPLES_UNION.tga`
- `AFRICA_CONTINENTAL_COMMAND`: `gfx/flags/AFRICA_CONTINENTAL_COMMAND.tga`, `gfx/flags/medium/AFRICA_CONTINENTAL_COMMAND.tga`, `gfx/flags/small/AFRICA_CONTINENTAL_COMMAND.tga`
- `AFRICA_CONFEDERATION`: `gfx/flags/AFRICA_CONFEDERATION.tga`, `gfx/flags/medium/AFRICA_CONFEDERATION.tga`, `gfx/flags/small/AFRICA_CONFEDERATION.tga`
- `AFRICA_COVENANT_UNION`: `gfx/flags/AFRICA_COVENANT_UNION.tga`, `gfx/flags/medium/AFRICA_COVENANT_UNION.tga`, `gfx/flags/small/AFRICA_COVENANT_UNION.tga`

The matching processed RGB PNG previews are under `docs/assets/012_africa_route_identity_art_v2/processed_png/flags/{normal,medium,small}/`.

### Standalone emblem textures

Each emblem is a distinct 64x64 transparent RGBA PNG preview converted to a one-level uncompressed BGRA DDS. Use these exact sprite IDs and texture paths:

| Sprite ID | Final DDS | Visual fit |
| --- | --- | --- |
| `GFX_012_africa_charter_federalism_emblem` | `gfx/interface/012_africa/emblems/012_africa_charter_federalism_emblem.dds` | copper protective arch, linked civic pillars, green leaf |
| `GFX_012_africa_continental_republic_emblem` | `gfx/interface/012_africa/emblems/012_africa_continental_republic_emblem.dds` | open civic book, rising sun, linked stars |
| `GFX_012_africa_council_of_crowns_emblem` | `gfx/interface/012_africa/emblems/012_africa_council_of_crowns_emblem.dds` | three linked sovereign crowns and sun |
| `GFX_012_africa_peoples_union_emblem` | `gfx/interface/012_africa/emblems/012_africa_peoples_union_emblem.dds` | gear, three rising leaves, linked rings |
| `GFX_012_africa_military_continentalism_emblem` | `gfx/interface/012_africa/emblems/012_africa_military_continentalism_emblem.dds` | compass, command baton, shield |
| `GFX_012_africa_continental_confederation_emblem` | `gfx/interface/012_africa/emblems/012_africa_continental_confederation_emblem.dds` | six interlocking rings and river diamond |
| `GFX_012_africa_high_chaos_covenant_emblem` | `gfx/interface/012_africa/emblems/012_africa_high_chaos_covenant_emblem.dds` | impossible living tree, crescent river, cyan ring |

Processed emblem PNGs are under `docs/assets/012_africa_route_identity_art_v2/processed_png/emblems/`. The generated RGB masters are under `source_png/`; alpha-cleaned chroma-key evidence is under `notes/alpha_emblems/`.

## Parent wiring

Add the seven standalone `spriteType` definitions to the parent-owned Africa interface GFX surface, suggested target `interface/012_africa.gfx`, with the exact sprite IDs and texture paths above. Then point the existing `GFX_idea_africa_unity_federal_union`, `GFX_idea_africa_unity_continental_republic`, `GFX_idea_africa_unity_council_of_crowns`, `GFX_idea_africa_unity_peoples_union`, `GFX_idea_africa_unity_continental_command`, `GFX_idea_africa_unity_continental_confederation`, and `GFX_idea_africa_unity_ancestral_covenant` consumers in `interface/012_africa.gfx` at the appropriate standalone emblem textures or sprites as the parent design requires. Keep the new sprite IDs stable.

## QA evidence

- `docs/assets/012_africa_route_identity_art_v2/contact_sheets/flags_source_and_ladders.png` shows every full source master beside normal, medium, and small exports; `flags_tga_decoded.png` shows the decoded runtime TGAs and orientation.
- `docs/assets/012_africa_route_identity_art_v2/contact_sheets/emblems_source_and_processed.png` shows every alpha-cleaned emblem beside its enlarged 64x64 processed preview.
- `docs/assets/012_africa_route_identity_art_v2/notes/hashes_dimensions.txt` records SHA-256, decoded dimensions, image modes, and byte sizes for all source, processed, TGA, and DDS files.
- DDS validation: all seven files are 16,512 bytes with declared 64x64 dimensions, 128-byte legacy headers, BGRA masks `0x00FF0000/0x0000FF00/0x000000FF/0xFF000000`, `DDSCAPS_TEXTURE`, and alpha range 0–255.
- TGA validation: every ladder file decodes to the required dimensions and RGBA mode, with descriptor byte 8. The Windows environment does not include the Unix `file` utility; direct header inspection and Pillow decode were used instead.

## Limitations

- ImageGen-generated flags and emblems are fictional alternate-history/supernatural designs, not historical heraldry or sourced institutions.
- At 10x7, fine heraldic details necessarily merge; each small export retains its route-specific field layout and central silhouette.
- The active `docs/assets/012_africa_route_identity_art_v2/` workspace remains intentionally retained for parent review and should only be removed after durable provenance and wiring facts are accepted.
- Final sprite registration and the rewire of the seven existing idea consumers remain parent-owned; no runtime `.gfx` claim is made here.
