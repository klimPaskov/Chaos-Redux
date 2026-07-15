# Event 014 idea icon repair handoff — 2026-07-15

## Outcome

Completed the eight missing Event 014 national-spirit picture assets as eight independent built-in `$imagegen` compositions. Each asset has a preserved full-resolution source, full-resolution transparent master, native `68x68` PNG, uncompressed BGRA runtime DDS, exact prompt, hash record, and visual-review evidence.

The root agent visually accepted the contact sheet and wired all eight sprites into `interface/014_cannibalism.gfx:152-159`. This subagent did not edit the `.gfx` file or any gameplay, localisation, spec, spreadsheet, or catalog surface.

## Asset identifiers and runtime files

| Picture / idea id | Runtime DDS | Sprite |
|---|---|---|
| `cannibalism_wendigo_conjoined_hunger` | `gfx/interface/ideas/014_cannibalism/idea_cannibalism_wendigo_conjoined_hunger.dds` | `GFX_idea_cannibalism_wendigo_conjoined_hunger` |
| `cannibalism_wendigo_winter_feeding_network` | `gfx/interface/ideas/014_cannibalism/idea_cannibalism_wendigo_winter_feeding_network.dds` | `GFX_idea_cannibalism_wendigo_winter_feeding_network` |
| `cannibalism_wendigo_locked_terminal_form` | `gfx/interface/ideas/014_cannibalism/idea_cannibalism_wendigo_locked_terminal_form.dds` | `GFX_idea_cannibalism_wendigo_locked_terminal_form` |
| `cannibalism_liberated_feeding_states` | `gfx/interface/ideas/014_cannibalism/idea_cannibalism_liberated_feeding_states.dds` | `GFX_idea_cannibalism_liberated_feeding_states` |
| `cannibalism_identification_and_burial_emergency` | `gfx/interface/ideas/014_cannibalism/idea_cannibalism_identification_and_burial_emergency.dds` | `GFX_idea_cannibalism_identification_and_burial_emergency` |
| `cannibalism_broken_military_trust` | `gfx/interface/ideas/014_cannibalism/idea_cannibalism_broken_military_trust.dds` | `GFX_idea_cannibalism_broken_military_trust` |
| `cannibalism_rebuilt_supply_discipline` | `gfx/interface/ideas/014_cannibalism/idea_cannibalism_rebuilt_supply_discipline.dds` | `GFX_idea_cannibalism_rebuilt_supply_discipline` |
| `cannibalism_permanent_vigilance` | `gfx/interface/ideas/014_cannibalism/idea_cannibalism_permanent_vigilance.dds` | `GFX_idea_cannibalism_permanent_vigilance` |

## Package files

Primary package: `docs/assets/014_cannibalism/idea_icon_repair/`

- `manifest.md` — complete asset ledger, paths, source mode, subjects, wiring state, and validation summary
- `gfx_handoff.md` — confirmed sprite names, runtime paths, and root-owned definitions
- `hashes.sha256` — SHA-256 for all 33 binary deliverables: source, transparent master, processed PNG, DDS, and contact sheet
- `prompts/idea_icon_prompts.md` — exact prompt from each of the eight built-in image-generation calls
- `source_png/` — eight original `1254x1254` RGB chroma-key source PNGs
- `key_removed_png/` — eight preserved `1254x1254` RGBA transparent masters
- `processed_png/` — eight final `68x68` RGBA previews
- `contact_sheets/event014_idea_icon_repair_contact_sheet.png` — native and `2x` nearest-neighbour checkerboard review
- `notes/process_idea_icons.py` — deterministic crop/fit/shadow/contact-sheet processor; it does not draw or substitute source art
- `notes/visual_audit.md` — per-asset native-readability and constraint audit

## Visual direction delivered

- `conjoined_hunger`: paired invented winter-horror skull profiles around a cracked ration cup
- `winter_feeding_network`: three-node frozen military supply hub
- `locked_terminal_form`: black-ice heart under a closed riveted exoskeleton clasp
- `liberated_feeding_states`: liberation bell, relief grain, field kitchen pot, and restrained sunrise
- `identification_and_burial_emergency`: casualty register, blank identity tags, plain field marker, and burial cloth
- `broken_military_trust`: split command star, separating anonymous gloves, and snapped baton
- `rebuilt_supply_discipline`: sealed supply crate, inspection seal, inventory strap, and rail wheel
- `permanent_vigilance`: field binoculars, protected archive folder, and compact alert lamp

All eight silhouettes remain distinct at native size. None is a resized focus icon, recolor, crop variant, placeholder, or locally drawn primitive substitute.

## Constraint audit

- No real-person likeness appears.
- No living Indigenous clothing, art, ritual, or sacred motif appears.
- The three winter-horror briefs explicitly excluded antlers, deer skulls, dreamcatchers, feathers, beadwork, medicine wheels, totems, ceremonial masks, and sacred geometry.
- No icon uses cages, prison bars, cell doors, shackles, barbed wire, guard towers, or prison-host presentation.
- No generated readable text, flag, state insignia, watermark, opaque square background, focus frame, or fake checkerboard remains.
- The burial marker is deliberately unmarked and non-religious; identity tags are blank.

## Processing and validation evidence

1. Generated each source in a separate built-in `$imagegen` call on a flat chroma-key canvas.
2. Removed the key with the installed imagegen helper using border sampling, soft matte, despill, and one-pixel edge contraction.
3. Cropped only transparent source margin; fit each painted subject within a shared 62-pixel safe area on a `68x68` canvas; retained the painted dark contour and added a restrained one-pixel UI shadow.
4. Audited native and enlarged output on the contact sheet. Root agent visually accepted the sheet.
5. Converted every preview with `.tools/convert_to_dds.py`.
6. Validated every DDS against the complete legacy-header contract: `DDS ` magic, header size `124`, pixel-format block at byte 76, flags `RGB | ALPHAPIXELS`, fourCC `0`, bit count `32`, BGRA masks, `DDSCAPS_TEXTURE`, declared `68x68`, and exact file length `18,624` bytes.
7. Confirmed each DDS alpha spans `0..255` and each decoded runtime pixel matches its processed PNG after BGRA channel ordering.
8. Confirmed zero visible chroma-green pixels in all eight processed previews and unique SHA-256 hashes across every corresponding source, preview, and runtime file.
9. Root reported final closure after wiring: 9 GFX files, 812 references, 598 unique texture paths, and 0 missing paths.

## References and skills used

- `chaos-redux-event-assets`
- official `imagegen`
- required offline core wiki pages plus `Idea modding`, `Interface modding`, and `Graphical asset modding`
- vanilla `common/ideas`, `interface/ideas.gfx`, and uncompressed BGRA national-spirit DDS precedents
- repository Event 014 idea folder, existing `interface/014_cannibalism.gfx` pattern, and the skill's idea reference images

No skills were created or modified.

## Ownership boundary

Files created by this subagent are limited to the eight runtime DDS files, `docs/assets/014_cannibalism/idea_icon_repair/`, and this handoff. Root-agent changes to `interface/014_cannibalism.gfx` are acknowledged as completed but are not part of this subagent's edit ownership.

## Simplifications, omissions, and blockers

None. The requested `68x68` target was used exactly, even though vanilla national-spirit precedents commonly use `60x68` and other Event 014 assets use `64x64`; the root agent accepted and wired the requested dimensions. No fallback generation route was used.
