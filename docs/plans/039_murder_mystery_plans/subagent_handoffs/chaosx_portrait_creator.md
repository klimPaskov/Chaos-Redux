# Chaos Redux portrait creator handoff — Event 039 Murder Mystery

Status: portrait production and portrait-specific runtime sprite wiring complete; parent character attachment and live consumer review pending.

## Changed files

- `interface/039_murder_mystery_portraits.gfx` adds five portrait-specific `spriteType` entries and points only to the new Event 039 leader DDS folder.
- `gfx/leaders/039_murder_mystery/leader_039_emergency_constitutional_successor.dds`
- `gfx/leaders/039_murder_mystery/leader_039_first_knife.dds`
- `gfx/leaders/039_murder_mystery/leader_039_hidden_hand.dds`
- `gfx/leaders/039_murder_mystery/leader_039_cells_without_masters.dds`
- `gfx/leaders/039_murder_mystery/leader_039_necessary_mask.dds`
- `docs/assets/039_murder_mystery/portraits/manifest.md` records source mode, reference gate, rights status, identifiers, hashes, dimensions, conversion, review, replacement boundary, and authorization boundary.
- `docs/assets/039_murder_mystery/portraits/portrait_wiring.md` records the parent-owned character-token to `civilian.large` sprite map.
- `docs/assets/039_murder_mystery/portraits/prompts/` contains five retained native ImageGen prompts.
- `docs/assets/039_murder_mystery/portraits/source_png/` contains five untouched copied native ImageGen source PNGs.
- `docs/assets/039_murder_mystery/portraits/processed_png/` contains five processed `156x210` PNG candidates.
- `docs/assets/039_murder_mystery/portraits/review/portrait_contact_sheet.png`, `native_4x_nearest_contact_sheet.png`, and `dds_roundtrip_contact_sheet.png` retain visual review evidence.

No gameplay event, focus, country, localisation, spreadsheet, sound, general GFX, or existing character-definition file was edited. No existing character portrait reference existed for Event 039 at production time, so the parent attachment map is supplied instead of changing `common/characters/`.

## Portrait identifiers

| Role | Fictional identity | Character token for parent attachment | Sprite key | Runtime DDS |
| --- | --- | --- | --- | --- |
| Emergency constitutional successor | Mara Vey | `murder_mystery_emergency_constitutional_successor` | `GFX_portrait_039_emergency_constitutional_successor` | `gfx/leaders/039_murder_mystery/leader_039_emergency_constitutional_successor.dds` |
| First Assassin State leader / First Knife | Ivo Saran | `murder_mystery_first_knife` | `GFX_portrait_039_first_knife` | `gfx/leaders/039_murder_mystery/leader_039_first_knife.dds` |
| The Hidden Hand | Oren Vale | `murder_mystery_hidden_hand_route_leader` | `GFX_portrait_039_hidden_hand` | `gfx/leaders/039_murder_mystery/leader_039_hidden_hand.dds` |
| Cells Without Masters | Lida Ors | `murder_mystery_cells_without_masters_route_leader` | `GFX_portrait_039_cells_without_masters` | `gfx/leaders/039_murder_mystery/leader_039_cells_without_masters.dds` |
| The Necessary Mask | Sava Pell | `murder_mystery_necessary_mask_route_leader` | `GFX_portrait_039_necessary_mask` | `gfx/leaders/039_murder_mystery/leader_039_necessary_mask.dds` |

All five use the `civilian.large` slot and full `156x210` opaque leader textures. The three route portraits are distinct rather than aliases or resized substitutes.

## Generation and source evidence

Source mode for every portrait is `fictional_high_chaos` with native built-in ImageGen. The five prompt files and source PNGs are co-located under `docs/assets/039_murder_mystery/portraits/`. Native ImageGen output files came from `C:/Users/klimp/.codex/generated_images/01a04f14-ad5b-7750-9523-3cbe24871a9b/` and remain there in addition to the copied repository evidence.

The matching installed-vanilla reference family was inspected at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/`, including its contact sheet and `156x210` opaque leader examples. The installed vanilla `ICE_sveinn_bjornsson` character/GFX/DDS precedent was also checked.

Rights status is synthetic native ImageGen output with no Internet source, third-party photograph, attribution, or public-domain claim. No real person or real religion, ethnicity, historical society, anarchist tradition, or extremist group is used as identity coding. The visual motif is limited to empty chairs, severed command knots, and restrained hand-mask props; no crescents, Alamut, hashish, ninja imagery, generic full-face masks, modern tactical gear, gore, weapons, generated text, or watermarks were accepted.

## Hashes and dimensions

| Basename | Source dimensions / SHA-256 | Processed dimensions / SHA-256 | DDS dimensions / bytes / SHA-256 |
| --- | --- | --- | --- |
| `leader_039_emergency_constitutional_successor` | `1082x1454 / 95cd9f79d9d0cf98ec77add452534ae6b6745671881049fe609b060270ecaa11` | `156x210 / dc267aa8cf69f3bdb5c0c8626a25ae6fd82e24089a0a20524da429c3d1c903a9` | `156x210 / 131168 / e8f9cc871767cd66504acd0ee7f0e8cb867b0c793997ac71dc89663886ab3f3a` |
| `leader_039_first_knife` | `1081x1455 / a9f9025f520f69dd48c6aa94954fc61eae6367578a28dd20f2d08577501e2d2e` | `156x210 / 9b475fc3d5e499ab0969510c997dedce232199105a27cff16dfc8fd1ec3fe823` | `156x210 / 131168 / da592e7440ac1ce9ec06b552edb82a7093c0e92888cda725c3ec731a20009930` |
| `leader_039_hidden_hand` | `1083x1453 / 0943fb70cfcc5a02ed6390b99eb808bcf29aafd0466dcf77a4b055c08145b81b` | `156x210 / 90095a40f3c8b3c918d5c1b62deac08e4c9163f50313180952a5a1f87a8ac0ab` | `156x210 / 131168 / 4c0b52cfc9f23eca6b1a972496a6ebd4b368a10d510168dcb328c9fbbe99ca0b` |
| `leader_039_cells_without_masters` | `1082x1454 / ce79cf0bfe62e4aad60619bc3f20623aca6fe1b268bdd3207c679efbf2dbe18d` | `156x210 / 268d17df0d5af2d16b34df12b4f1ea0fe2180221a1b06c28ae02b171d5e21730` | `156x210 / 131168 / 78bf986a99cd1beaab9190e506e9db96aa8d5fe89df9d3f3c87ceea40495aa45` |
| `leader_039_necessary_mask` | `1082x1454 / 1dd8566e970c5afee6ecd3e1fe00f6c9689fecfa8a321ca540c39bc4f5684b44` | `156x210 / a137e1388e27e6092e717253f46425af647956c3edc15c770f59018aa6c7b26e` | `156x210 / 131168 / e887e806f746d6b73630ff28de9e92929e85fa9d6fb22f71aa7d520da6c7a64f` |

The required DDS converter was run once per processed PNG with `--width 156 --height 210`. Every DDS passed the legacy one-level uncompressed BGRA header contract, exact file length `131168`, declared `156x210` dimensions, alpha range `255–255`, and decoded pixel round-trip equality against its processed PNG.

## Review result and replacement state

The portrait contact sheet, native/4x-nearest framing sheet, and DDS round-trip sheet were reviewed at native size and enlarged size. All five candidates PASS framing, face readability, role distinction, background treatment, forbidden-motif exclusion, and no-text/no-watermark checks. Parent visual/runtime review is still pending because the shared repository has no Event 039 character consumer yet.

No asset is `replacement_pending`. These are final fictional ImageGen portraits; the user does not need to run RunPod or supply a replacement. If any parent review rejects a candidate, request a targeted native ImageGen regeneration and retain the rejected source as evidence rather than repainting or substituting a grounded face.

## Risks and blockers

- The parent must attach the five stable sprite keys to the final Event 039 character tokens in the country package; no `common/characters/` file was changed here.
- The accepted spec leaves the eventual dynamic Assassin State carrier tag unresolved; the portrait folder is tag-neutral and does not require a tag change.
- No live HOI4 launch or engine screenshot was performed by this worker, and no RunPod route was used.
- Commanders, advisor cards, operative portraits, and intelligence-organizer portraits were intentionally not created because they were outside the user-authorized minimum set and had no live 039 consumer at production time.
