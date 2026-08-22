# Zombie counter artwork GFX handoff

Status: all seven requested counter packages are produced, visually reviewed, and promoted to their runtime destinations.

This handoff contains evidence/package DDS files and records the completed runtime promotion. Live HOI4 playback remains user-owned.

## Requested units

| Unit | Large package | Small package | Distinctive silhouette cue |
| --- | --- | --- | --- |
| `infected_zombies` | `infected_zombies/counters/large/unit_infected_zombies_icon.dds` | `infected_zombies/counters/small/onmap_unit_infected_zombies_icon.dds` | hunched infected figure, reaching arm, ragged hair |
| `rabid_zombies` | `rabid_zombies/counters/large/unit_rabid_zombies_icon.dds` | `rabid_zombies/counters/small/onmap_unit_rabid_zombies_icon.dds` | low rabid sprint, raised claws, thrust jaw |
| `parasitic_zombies` | `parasitic_zombies/counters/large/unit_parasitic_zombies_icon.dds` | `parasitic_zombies/counters/small/onmap_unit_parasitic_zombies_icon.dds` | asymmetrical host body and shoulder tendrils |
| `mutant_zombies` | `mutant_zombies/counters/large/unit_mutant_zombies_icon.dds` | `mutant_zombies/counters/small/onmap_unit_mutant_zombies_icon.dds` | oversized forearms and broad loping body |
| `undead_zombies` | `undead_zombies/counters/large/unit_undead_zombies_icon.dds` | `undead_zombies/counters/small/onmap_unit_undead_zombies_icon.dds` | broad skeletal infantry silhouette and coat flare |
| `necrotic_zombies` | `necrotic_zombies/counters/large/unit_necrotic_zombies_icon.dds` | `necrotic_zombies/counters/small/onmap_unit_necrotic_zombies_icon.dds` | collapsed corpse posture, sagging torso, hanging jaw |
| `demonic_zombies` | `demonic_zombies/counters/large/unit_demonic_zombies_icon.dds` | `demonic_zombies/counters/small/onmap_unit_demonic_zombies_icon.dds` | swept horns, wing-like shoulders, long limbs |

Every sheet has exactly two frames in vanilla order: frame 0 normal on the left, frame 1 pale sparse alternate on the right.

## Exact runtime destinations and existing consumers

| Surface | Existing sprite consumer | Expected runtime DDS destination | Package canvas |
| --- | --- | --- | ---: |
| Large division counter | `GFX_unit_<unit>_icon_medium` | `gfx/interface/counters/divisions_large/unit_<unit>_icon.dds` | 152×42, 2×76×42 frames |
| Small on-map counter | `GFX_unit_<unit>_icon_medium_white` | `gfx/interface/counters/divisions_small/onmap_unit_<unit>_icon.dds` | 60×12, 2×30×12 frames |

The sprite names and runtime destinations above were inspected from the existing mod sprite definitions and the installed vanilla `interface/subuniticons.gfx` precedent. The parent owns any runtime copy/wiring decision.

## Reference and palette evidence

Installed vanilla definitions and DDS were inspected read-only:

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/subuniticons.gfx`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/counters/divisions_large/unit_infantry_icon.dds`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/counters/divisions_small/onmap_unit_infantry_icon.dds`

The canonical contact sheets were inspected first from `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/counters_large/contact_sheet.png` and `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/map_counters/contact_sheet.png`, followed by the matching individual infantry references. The decoded installed references and comparison sheets are in `counter_evidence/installed_vanilla/`.

The final opaque pixels use exact sampled colors from the corresponding installed vanilla infantry frame. The normal large palette includes the sampled vanilla green `#496a49` (`RGB 73,106,73`); alternate pixels use the installed pale schematic palette. Small normal pixels use the installed small on-map infantry palette. No arbitrary green, copied vanilla silhouette, generic identical copy, or static placeholder was used.

Matching zombie model inputs and weaponized portrait references are captured in `counter_evidence/matching_refs/`. Existing mod generic counter files are captured in `counter_evidence/current_mod/` and were not reused.

## Validation and manifests

- `counter_evidence/vanilla_inspection.md` records the installed definitions, canvas/frame structure, alpha behavior, palette range, and current-mod inspection.
- `counter_evidence/generation_prompts.md` records the source-generation prompts and the undead source replacement.
- `counter_evidence/processed_large_contact_sheet.png` and `processed_small_contact_sheet.png` show all seven final sheets.
- `counter_evidence/validation_summary.json` records the 14 DDS checks.
- Each unit's `counters/validation.json` records dimensions, frame bounds, palette-subset checks, and DDS round-trip equality.
- Each unit's `counters/manifest.md` and `counters/sha256sums_artifacts.txt` record the package paths and per-file SHA-256 values.
- `counter_evidence/shared_evidence_sha256sums.txt` hashes the shared inspection and handoff evidence.
- `counter_evidence/counter_package_file_inventory.txt` enumerates the generated package files and handoffs.

The final 14 DDS files all validate at their exact target dimensions, round-trip pixel-identically against the processed PNG sheets, and contain only colors from the matching installed vanilla state palette for opaque processed pixels.

## Files intentionally not touched

The base `zombies` model and sound definitions were preserved. The armored undead, necrotic, and demonic unit bindings now reuse their specialized parent entities through `common/units/zombies.txt`; the seven bespoke counter DDS files were promoted to the registered runtime paths.
