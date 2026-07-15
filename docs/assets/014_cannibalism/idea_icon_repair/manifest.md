# Event 014 national-spirit idea icon repair manifest

## Package summary

- Event: `014_cannibalism`
- Asset type: eight dedicated idea / national-spirit icons
- Source mode: built-in `$imagegen`, one independent call per icon
- Source rationale: all eight concepts are fictional or symbolic; none depicts a real person or requires archival source material
- Source master: `1254x1254` RGB PNG on a removable chroma-key canvas
- Preserved transparent master: `1254x1254` RGBA PNG
- Processed preview: `68x68` RGBA PNG with transparent unused canvas
- Runtime format: one-level legacy DDS, uncompressed 32-bit BGRA, `68x68`, 18,624 bytes
- Runtime folder: `gfx/interface/ideas/014_cannibalism/`
- Sprite registry: `interface/014_cannibalism.gfx`
- Exact prompts: [prompts/idea_icon_prompts.md](prompts/idea_icon_prompts.md)
- Review sheet: [contact_sheets/event014_idea_icon_repair_contact_sheet.png](contact_sheets/event014_idea_icon_repair_contact_sheet.png)
- Hash ledger: [hashes.sha256](hashes.sha256)
- Processing provenance: [notes/process_idea_icons.py](notes/process_idea_icons.py)

The generated icon family intentionally excludes real-person likenesses, prison-host imagery, and borrowed living Indigenous clothing, art, ritual, or sacred motifs. The three fictional winter-horror stages also exclude antlers, deer skulls, dreamcatchers, feathers, beadwork, medicine wheels, totems, ceremonial masks, and sacred geometry.

## Asset ledger

| Picture / related idea | Visual subject | Source PNG | Transparent master | Processed PNG | Final DDS | Sprite | Target `.gfx` | Status |
|---|---|---|---|---|---|---|---|---|
| `cannibalism_wendigo_conjoined_hunger` | Two invented winter-horror skull profiles fused around a cracked field ration cup | `source_png/cannibalism_wendigo_conjoined_hunger_source.png` | `key_removed_png/cannibalism_wendigo_conjoined_hunger_transparent.png` | `processed_png/idea_cannibalism_wendigo_conjoined_hunger.png` | `gfx/interface/ideas/014_cannibalism/idea_cannibalism_wendigo_conjoined_hunger.dds` | `GFX_idea_cannibalism_wendigo_conjoined_hunger` | `interface/014_cannibalism.gfx` | `wired` |
| `cannibalism_wendigo_winter_feeding_network` | Three-node frost-rimmed military supply hub linked by broad ice conduits | `source_png/cannibalism_wendigo_winter_feeding_network_source.png` | `key_removed_png/cannibalism_wendigo_winter_feeding_network_transparent.png` | `processed_png/idea_cannibalism_wendigo_winter_feeding_network.png` | `gfx/interface/ideas/014_cannibalism/idea_cannibalism_wendigo_winter_feeding_network.dds` | `GFX_idea_cannibalism_wendigo_winter_feeding_network` | `interface/014_cannibalism.gfx` | `wired` |
| `cannibalism_wendigo_locked_terminal_form` | Black-ice heart enclosed by a closed riveted exoskeleton clasp | `source_png/cannibalism_wendigo_locked_terminal_form_source.png` | `key_removed_png/cannibalism_wendigo_locked_terminal_form_transparent.png` | `processed_png/idea_cannibalism_wendigo_locked_terminal_form.png` | `gfx/interface/ideas/014_cannibalism/idea_cannibalism_wendigo_locked_terminal_form.dds` | `GFX_idea_cannibalism_wendigo_locked_terminal_form` | `interface/014_cannibalism.gfx` | `wired` |
| `cannibalism_liberated_feeding_states` | Weathered liberation bell, relief grain sacks, field kitchen pot, and low sunrise | `source_png/cannibalism_liberated_feeding_states_source.png` | `key_removed_png/cannibalism_liberated_feeding_states_transparent.png` | `processed_png/idea_cannibalism_liberated_feeding_states.png` | `gfx/interface/ideas/014_cannibalism/idea_cannibalism_liberated_feeding_states.dds` | `GFX_idea_cannibalism_liberated_feeding_states` | `interface/014_cannibalism.gfx` | `wired` |
| `cannibalism_identification_and_burial_emergency` | Open casualty register, blank identity tags, unmarked field grave stone, and folded burial cloth | `source_png/cannibalism_identification_and_burial_emergency_source.png` | `key_removed_png/cannibalism_identification_and_burial_emergency_transparent.png` | `processed_png/idea_cannibalism_identification_and_burial_emergency.png` | `gfx/interface/ideas/014_cannibalism/idea_cannibalism_identification_and_burial_emergency.dds` | `GFX_idea_cannibalism_identification_and_burial_emergency` | `interface/014_cannibalism.gfx` | `wired` |
| `cannibalism_broken_military_trust` | Anonymous military gloves separating a split brass command star over a snapped baton | `source_png/cannibalism_broken_military_trust_source.png` | `key_removed_png/cannibalism_broken_military_trust_transparent.png` | `processed_png/idea_cannibalism_broken_military_trust.png` | `gfx/interface/ideas/014_cannibalism/idea_cannibalism_broken_military_trust.dds` | `GFX_idea_cannibalism_broken_military_trust` | `interface/014_cannibalism.gfx` | `wired` |
| `cannibalism_rebuilt_supply_discipline` | Sealed field-supply crate, brass inspection seal, canvas strap, and rail wheel | `source_png/cannibalism_rebuilt_supply_discipline_source.png` | `key_removed_png/cannibalism_rebuilt_supply_discipline_transparent.png` | `processed_png/idea_cannibalism_rebuilt_supply_discipline.png` | `gfx/interface/ideas/014_cannibalism/idea_cannibalism_rebuilt_supply_discipline.dds` | `GFX_idea_cannibalism_rebuilt_supply_discipline` | `interface/014_cannibalism.gfx` | `wired` |
| `cannibalism_permanent_vigilance` | Period field binoculars, protected archive folder, and compact alert lamp | `source_png/cannibalism_permanent_vigilance_source.png` | `key_removed_png/cannibalism_permanent_vigilance_transparent.png` | `processed_png/idea_cannibalism_permanent_vigilance.png` | `gfx/interface/ideas/014_cannibalism/idea_cannibalism_permanent_vigilance.dds` | `GFX_idea_cannibalism_permanent_vigilance` | `interface/014_cannibalism.gfx` | `wired` |

## Generation and processing notes

- Every row has its own asset-type-specific national-spirit brief and its own built-in image-generation call. None is a resized focus icon, placeholder, recolor, or crop variant of another asset.
- Chroma removal used the installed `$imagegen` helper with border auto-keying, soft matte, despill, and a one-pixel edge contraction. The preserved transparent masters retain the full generated resolution.
- Native processing crops transparent margin only, fits the painted emblem into a shared 62-pixel safe area, adds a restrained one-pixel UI shadow, and preserves the original painted contour.
- The contact sheet shows every selected icon at native `68x68` and at `2x` nearest-neighbour scale over a checker background.
- Root-agent wiring was confirmed on 2026-07-15 at `interface/014_cannibalism.gfx:152-159`. The asset worker did not edit that file.

## Validation summary

- All eight processed PNGs have real alpha, transparent corners, full alpha range `0..255`, centered visible subjects, and zero visible chroma-green pixels.
- All eight DDS files declare `68x68`, use the required legacy 128-byte DDS header, BGRA masks, alpha flags, `DDSCAPS_TEXTURE`, one level, and exact length `128 + 68 * 68 * 4 = 18,624` bytes.
- Runtime DDS pixels match their processed PNGs exactly after BGRA channel ordering.
- Every source, transparent master, processed PNG, and runtime DDS has a unique SHA-256 hash.
- Visual review found eight distinct native-size silhouettes and no prison/cage imagery, real-person likeness, or borrowed living Indigenous sacred motif.

## Simplifications, omissions, and blockers

None. All eight requested assets, provenance files, processed previews, runtime DDS files, review evidence, and sprite handoff information are present. Wiring was completed by the root agent in the existing Event 014 `.gfx` registry.
