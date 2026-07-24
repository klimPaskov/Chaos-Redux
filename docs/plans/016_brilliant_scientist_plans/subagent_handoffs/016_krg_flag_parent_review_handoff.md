# Event 016 KRG flag parent review

## Review identity

- Date: 2026-07-24
- Mode: parent visual, technical, and consumer review
- Scope: base Kruger State flag and six route-specific cosmetic-tag flag families
- Skill applied: `chaos-redux-event-assets`

## Accepted flag identities

| Flag family | Runtime identity | Gameplay consumer |
| --- | --- | --- |
| `KRG` | Kruger provisional laboratory state | Base country tag |
| `KRG_SCIENTIFIC_REPUBLIC` | Scientific Republic | `KRG_SCIENTIFIC_REPUBLIC` cosmetic tag |
| `KRG_REPLICATED_STATE` | Replicated State | `KRG_REPLICATED_STATE` cosmetic tag |
| `KRG_MACHINE_STATE` | Machine State | `KRG_MACHINE_STATE` cosmetic tag |
| `KRG_TEMPORAL_CONTINUUM` | Temporal Continuum | `KRG_TEMPORAL_CONTINUUM` cosmetic tag |
| `KRG_XENOBIOLOGICAL_ASCENDANCY` | Xenobiological Ascendancy | `KRG_XENOBIOLOGICAL_ASCENDANCY` cosmetic tag |
| `KRG_PROJECT_SYNTHESIS` | Project Synthesis | `KRG_PROJECT_SYNTHESIS` cosmetic tag |

The base laboratory state uses a four-point apparatus seal.

The Scientific Republic uses a civic scientific triangle.

The Replicated State uses a divided replicated-cell emblem.

The Machine State uses a gear and machine-aperture emblem.

The Temporal Continuum uses a clock and directional continuity mark.

The Xenobiological Ascendancy uses a three-part organic growth emblem.

Project Synthesis combines mechanical, biological, and temporal symbols in a deliberately mixed banner.

The shared horizontal laboratory-state grammar keeps the package related without reusing one emblem.

## Runtime ladder

Each of the seven identities has:

- an `82x52` normal flag under `gfx/flags/`;
- a `41x26` medium flag under `gfx/flags/medium/`;
- a `10x7` small flag under `gfx/flags/small/`.

This produces 21 final TGA files.

The package record is `docs/assets/016_brilliant_scientist/package_records/krg_flag_package.json`.

The review contact sheet is `docs/assets/016_brilliant_scientist/contact_sheets/krg_flag_source_vs_runtime_contact_sheet.png`.

## Visual review

The source, solid-palette master, and decoded runtime ladder were reviewed together.

All seven identities remain distinct at normal size.

The medium ladder preserves the route symbol and principal palette.

The small ladder preserves the route palette and major vertical or horizontal division even where the ten-pixel width cannot carry the full seal.

No source contains generated text or a copied real-world emblem.

## Technical evidence

Package validation found:

- seven independent source records;
- all seven source PNGs and processed masters present;
- all 21 processed size PNGs, packaged TGAs, and runtime TGAs present;
- every runtime width and height equal to the recorded native ladder;
- every runtime SHA-256 equal to the package record;
- every runtime TGA equal to its packaged TGA;
- decoded runtime pixels equal to the corresponding processed PNG according to the package record.

## Consumer review

`common/countries/016_brilliant_scientist_cosmetics.txt` declares all six route cosmetic tags.

`common/scripted_effects/016_brilliant_scientist_country_effects.txt` applies each route tag through a separate route-resolution effect.

`localisation/english/016_brilliant_scientist_country_l_english.yml` supplies each route name, definite form, adjective, and governing-ideology alias.

No fallback flag or unrelated borrowed identity is used.
