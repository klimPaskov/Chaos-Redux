# Event 014 CBC/AIX Classic HOI4 Portrait Repaint Handoff

Date: 2026-07-15
Asset owner: `chaosx_generated_event_art` worker
Scope: exactly the 14 static fictional CBC and AIX warlord portrait stems assigned by the parent
Status: complete and visually approved; no commit created

## Outcome

The 14 CBC/AIX warlord portraits were regenerated from independent built-in ImageGen calls and replaced at their existing source, processed, metadata, review-sheet, and DDS paths. The new set is deliberately painted rather than photographic: opaque oil/gouache handling, simplified facial planes, firm painted edges, low skin microdetail, muted 1930s-1940s values, quiet brushed backgrounds, and period clothing.

No interface, localisation, gameplay, Hannibal, shared manifest, aggregate prompt matrix, or aggregate validation document was edited. Existing sprite names and texture paths remain unchanged in `interface/014_cannibalism.gfx`.

## Skills and required references used

- `imagegen`
- `chaos-redux-event-assets`
- Offline wiki core pages required by `AGENTS.md`, plus `paradox_wiki/Portrait modding - Hearts of Iron 4 Wiki.md`
- Vanilla official portrait-related effect documentation and `interface/_leader_portraits.gfx`
- Canonical asset-library rules and portrait catalog

Every generation call used these same three images as **style-only** references:

1. `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/den_thorvald_stauning.png`
2. `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/ire_eamon_de_valera.png`
3. `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/fin_carl_mannerheim.png`

They were used only for finish, restrained bust framing, softly brushed background treatment, and controlled value range. Prompts explicitly prohibited copying or blending the depicted identities, facial features, clothing, insignia, or poses.

## Shared prompt/style contract

Every selected prompt required:

- one wholly original fictional adult male warlord, never a real-person or actor likeness;
- a completely bald smooth scalp with no head hair;
- distinct regional plausibility, anatomy, build, expression, clothing, prop, and face-adjacent action;
- a vertical head-and-shoulders or restrained-bust composition with the full bald head, hands, and prop retained inside the 156x210 crop;
- unmistakable classic HOI4 country-leader painting: hand-painted opaque oil/gouache, simplified illustrative facial planes, firm painted edges, deliberate brush shapes, restrained texture, and low photographic microdetail;
- a muted olive/umber/charcoal/gray 1930s-1940s palette and quiet softly brushed background;
- period-appropriate wool, cotton, leather, waxed cotton, wood, steel, tin, resin, or bone materials;
- a visibly deranged or uncanny expression without gore, fresh injury, or active violence.

Every prompt explicitly avoided:

- photorealism, photographic pores, camera/lens language, depth-of-field blur, cinematic grading, dramatic rim lights, glossy 3D, and smooth modern digital concept art;
- modern tactical vests, nylon, plastic, headsets, radios, modern weapons, modern fasteners, or other modern objects;
- prisons, cells, bars, cages, confinement, restraints, or prisoner clothing;
- text, logos, flags, frames, borders, watermarks, copied insignia, copied real-person identity, and living Indigenous sacred motifs.

## Selected generation provenance and prompt deltas

Built-in ImageGen output root:

`C:/Users/klimp/.codex/generated_images/019f6710-0cb6-7610-b296-3673035a3164/`

| Stem | Selected built-in output | Installed source SHA-256 | Decisive prompt delta |
| --- | --- | --- | --- |
| `leader_CBC_warlord` | `exec-0738576b-56d5-4f3b-aa89-1ec79699ca7e.png` | `8ca54fcc05b3098578e93d28352068c1a266d7ba14d17b7b3c38f8488bdbc079` | Lean European, long triangular face, late-1930s charcoal railway coat; screaming into a clean dry skull held like a telephone in a bell-tower square. |
| `leader_CBC_warlord_africa` | `exec-35a0ca12-b483-442a-af2b-dd25e0d167a6.png` | `2e7138e94e5969146e945c992b6b6481cdc41c40e334f989d66c25b132c15321` | Tall long-faced African, brown railway coat; biting an oversized faceted wooden molar at a savanna rail junction. |
| `leader_CBC_warlord_asia` | `exec-c8ede85b-ef20-44d9-b412-e5fc91861474.png` | `1a652b2deea63b4b72aaa010a640195fe6207d07b087fecab598529d6ae24dd7` | Heavyset South Asian, indigo dock foreman's coat; licking an empty scratched aluminum ration spoon before old river cranes. |
| `leader_CBC_warlord_middle_east` | `exec-6c5948a5-944f-4405-8761-ad36b56f8f9e.png` | `be5106c895a3f1fb6af015577e7dd261f98ac1b759e6feb4283180aff62cebc6` | Lean Middle Eastern, camel wool coat and scarf; pressing and rubbing a tarnished coin across his lips before refinery haze. |
| `leader_CBC_warlord_north_america` | `exec-0c985150-22f2-4bf7-b097-8eae4ca75e82.png` | `de7bdf3c80e6f51db6fa0575da5733af0671d3905f2ca5a2089950a1cbecf132` | Lean African-descended North American, wool forestry coat and checked shirt; balancing a carved tooth token upright on his tongue before burned pines. |
| `leader_CBC_warlord_south_america` | `exec-5548b13d-a34e-4433-9f08-bc25010e3cfb.png` | `9179a5660a0f4c3187efa4a3bb39e6862e6677aa40cdb86111655e1365ea7371` | Narrow long-necked South American, oxblood dock coat; stitching a crooked grin onto a canvas ration puppet held to his cheek. |
| `leader_CBC_warlord_oceania` | `exec-a7157325-6bc2-4d66-b457-0b1dcaa8b8c5.png` | `d5e8bf3c1196330b3dfb5419ac8832b5a50aa540e7c4db9149dc7674f0e3bb58` | Gaunt broad-shouldered Pacific Islander, gray waxed-cotton harbor coat; playing a plain drilled bone whistle at a storm-damaged wharf. |
| `leader_AIX_warlord` | `exec-cc0c299a-e326-450b-84c9-30380b3c5e0b.png` | `253f418540659ec7d0089768d835afe8492a52edfa287afb14fc04cda3270ad5` | Stocky Mediterranean European, charcoal engineer's wool coat and old leather apron; tipping carved tooth tokens into a chipped cup below his mouth. |
| `leader_AIX_warlord_africa` | `exec-311a8289-ab45-44c6-ba2c-c8941b0243b6.png` | `c9416788687be05553dea96e3f417c38419b13151f8f0776c0e1de9f4b399296` | Angular African mechanic in faded olive; threading drilled tooth tokens on plain wire with old steel pliers. |
| `leader_AIX_warlord_asia` | `exec-efe46c92-0d82-4fd3-aae8-44d43d4a5300.png` | `1b084421f2f87819a18fff665c32b59379a99584f2b21a3cf49aaea18a89fce8` | Angular Southeast Asian in a late-1930s leather aviation work jacket; filing an artificial crooked jaw trinket beside his mouth. |
| `leader_AIX_warlord_middle_east` | `exec-f735b3ba-abb0-475a-a287-fa0a6cbb98b2.png` | `5fc51509c0fa5e4662eae13b00c60e9cb7263709bd6b4095447889329df99704` | Stocky Middle Eastern mechanic in a stiff high-collared charcoal wool coat; arranging four carved molars along the collar edge. |
| `leader_AIX_warlord_north_america` | `exec-a28571e7-2ff0-4f06-a2e2-b50f3c5d416e.png` | `35998c034aa8b6972aee83d6a49c755179b6c9ab62645f9a2aa0069288dec7dc` | Long-faced Mexican-American railroad marshal in period wool; puckered lips visibly kissing a skull's front incisors at a desert depot. |
| `leader_AIX_warlord_south_america` | `exec-8b80f74d-976a-4fa6-bb4e-ac4fd701574a.png` | `ce0502d62af10b6a2c4c25ea0b9c3a62e0f868d9c61a7148ab01e9a5ec56dcfd` | Long-necked South American in an Andean highland setting and burgundy wool coat; pouring carved tooth tokens from a battered tin cup into his open mouth. |
| `leader_AIX_warlord_oceania` | `exec-975df947-e1d6-4301-b98e-3da0be9ec73b.png` | `3a7932b70a0145e925d0046ae8cb77b03cdbfeef85a05ca7167b170ea15d1815` | Broad Australian coastal warlord in navy waxed cotton; biting a bent counting wire while tooth-shaped counters remain threaded on it. |

### Retry accounting

- Total built-in ImageGen calls: 16.
- Required distinct portraits: 14; every required portrait had its own separate call.
- `leader_AIX_warlord_north_america`: first output `exec-511684c0-46b1-49a8-a3ca-e702799437cc.png` was rejected because the kiss landed near the skull's nasal bridge. The selected retry moves the lips onto the front incisors.
- `leader_AIX_warlord_oceania`: a stricter broken-wire alternative, `exec-71e59848-4c05-430c-9585-790565c53a6a.png`, was rejected because its counters stopped reading as tooth forms. The selected source kept the clearer tooth counters and unmistakable wire-bite action at 156x210.
- CLI generation, alternate models, local procedural portrait art, source substitution, and fallback assets were not used.

## Processing record

Every selected master was processed through `the retired portrait-processing utility leader` with `--source-kind fictional`, the canonical leader reference directory, explicit source-pixel crop coordinates, per-portrait JSON metadata, and per-portrait comparison sheet.

| Stem | Source size | Explicit crop `(left, top, right, bottom)` | Visual review at source and 156x210 |
| --- | ---: | --- | --- |
| `leader_CBC_warlord` | 1081x1455 | `(0, 0, 1081, 1455)` | Pass: skull-to-ear telephone pose and scream into the open jaw remain clear. |
| `leader_CBC_warlord_africa` | 1080x1456 | `(0, 1, 1080, 1455)` | Pass: carved wood facets, bite contact, eyes, and both hands remain clear. |
| `leader_CBC_warlord_asia` | 1082x1453 | `(1, 0, 1081, 1453)` | Pass: empty spoon, extended tongue, and split gaze remain clear. |
| `leader_CBC_warlord_middle_east` | 1080x1456 | `(0, 1, 1080, 1455)` | Pass: round tarnished coin remains visible in direct lip contact. |
| `leader_CBC_warlord_north_america` | 1080x1456 | `(0, 1, 1080, 1455)` | Pass: single tooth token remains centered and upright on the tongue. |
| `leader_CBC_warlord_south_america` | 1080x1456 | `(0, 1, 1080, 1455)` | Pass: puppet-to-cheek pose, stitched grin, needle, and thread remain readable. |
| `leader_CBC_warlord_oceania` | 1082x1454 | `(1, 0, 1081, 1454)` | Pass: drilled bone whistle, both hands, and blowing pose remain clear. |
| `leader_AIX_warlord` | 1076x1461 | `(0, 6, 1076, 1455)` | Pass: falling tooth-token stream and receiving cup remain clear. |
| `leader_AIX_warlord_africa` | 1082x1454 | `(1, 0, 1081, 1454)` | Pass: pliers, wire, drilled tokens, and obsessive threading pose remain clear. |
| `leader_AIX_warlord_asia` | 1080x1456 | `(0, 1, 1080, 1455)` | Pass: hand file, crooked jaw trinket, and dry filings remain clear. |
| `leader_AIX_warlord_middle_east` | 1080x1456 | `(0, 1, 1080, 1455)` | Pass: four separate molars and both arranging hands remain clear on the wool collar. |
| `leader_AIX_warlord_north_america` | 1083x1453 | `(2, 0, 1082, 1453)` | Pass after retry: lips visibly touch the skull's front incisor row. |
| `leader_AIX_warlord_south_america` | 1080x1456 | `(0, 1, 1080, 1455)` | Pass: cup, falling tooth tokens, open mouth, and destination remain readable. |
| `leader_AIX_warlord_oceania` | 1054x1492 | `(0, 32, 1054, 1451)` | Pass: bent counting wire, tooth-shaped counters, clenched bite point, and both fists remain clear. |

All 14 metadata records were changed from the processor's candidate state to `visually_approved` after source-scale, native-size processed, and whole-sheet review.

## Final file list

Working root:

`docs/assets/014_cannibalism/leader_portraits_refresh/cba_cbd/`

For every stem listed below, all five exact same-stem files were overwritten:

- `source_png/<stem>_source.png`
- `processed_png/<stem>.png`
- `metadata/<stem>.json`
- `review_sheets/<stem>_review.png`
- `gfx/leaders/014_cannibalism/<stem>.dds`

Final stems:

1. `leader_CBC_warlord`
2. `leader_CBC_warlord_africa`
3. `leader_CBC_warlord_asia`
4. `leader_CBC_warlord_middle_east`
5. `leader_CBC_warlord_north_america`
6. `leader_CBC_warlord_south_america`
7. `leader_CBC_warlord_oceania`
8. `leader_AIX_warlord`
9. `leader_AIX_warlord_africa`
10. `leader_AIX_warlord_asia`
11. `leader_AIX_warlord_middle_east`
12. `leader_AIX_warlord_north_america`
13. `leader_AIX_warlord_south_america`
14. `leader_AIX_warlord_oceania`

Whole-set review sheet:

`docs/assets/014_cannibalism/leader_portraits_refresh/cba_cbd/contact_sheets/cbc_cbd_hoi4_repaint_contact_sheet.png`

## DDS and wiring review

- Every processed PNG and final DDS is exactly 156x210.
- Every DDS is a one-level legacy 32-bit BGRA texture with `DDS ` magic, 124-byte header, 32-byte pixel-format block, RGB+alpha flags, zero FourCC, 32-bit channel masks, `DDSCAPS_TEXTURE`, and exact file length 131168 bytes.
- These leader portraits are intentionally opaque; every DDS alpha range is 255-255.
- Existing `GFX_portrait_CBC_warlord*` and `GFX_portrait_AIX_warlord*` definitions in `interface/014_cannibalism.gfx` still point to the unchanged `gfx/leaders/014_cannibalism/<stem>.dds` paths.
- No sprite or interface edit was required or made.

## Blockers, fallbacks, and simplifications

None. All 14 assigned portraits, their source/processed/metadata/review/DDS artifacts, the requested contact sheet, and the exact actions are present. No fallback, placeholder, modern-gear substitute, omitted region, copied real identity, or unwired filename was used.
