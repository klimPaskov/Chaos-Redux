# Event 014 Cannibalism Asset Authority

Date: 2026-07-15

This directory is the current source-of-truth asset package for Event 014. Runtime files remain authoritative for the game. This manifest records the generated or licensed sources, processing evidence, previews, validation, and GFX handoff that reproduce them.

## Current visual direction

- Flags are flat front-on flag designs, not painted scenes or photographed cloth.
- The eight reusable warlord slots support exactly three origins: Island Host, Siege Commune, and March Host.
- Warlord portraits are distinct feral HOI4-style command busts with open battlefield, smoke, naval, urban, or neutral command backdrops.
- Hannibal Lecter's ordinary portrait is reveal-gated. The live static sprite binds directly to `gfx/leaders/014_cannibalism/hannibal.dds`. That exact image is frame `000`, followed by 11 separately image-generated fork, lick, bite, chew, and reset states.
- Wendigo Hannibal binds directly to `gfx/leaders/014_cannibalism/hannibal_wendigo.dds`. That exact image is frame `000`, followed by 15 separately image-generated jaw, tongue, crush, chew, swallow, and reset states with no borrowed sacred or living Indigenous motif.
- Super-event art is action-led: attacks, pursuit, civilian flight, counterattack, and rescue rather than static tableaux.

Superseded flag, portrait, and retired transform-only animation packages are not part of this authority and are not present here. The current package contains no fourth origin asset set.

## Authoritative packages

| Package | Current scope | Evidence |
| --- | --- | --- |
| `flags_refresh/` | 65 independently generated designs and 195 runtime TGAs at 82x52, 41x26, and 10x7 | Exact prompts, source PNGs, processed PNGs, hashes, contact sheets, manifest |
| `leader_portraits_refresh/` | 56 distinct warlord portraits, ordinary Hannibal 12-frame animation, and Wendigo Hannibal 16-frame animation | Source images, processed PNG/DDS, static fallbacks, sheets, GIF previews, manifests, validation |
| `idea_icon_repair/` | Eight independently generated national-spirit icons that close the final idea-picture gap | Prompts, sources, processed PNG/DDS, contact sheet, hashes, GFX handoff |
| `gui_animation_portraits/` | 26 static GUI PNG/DDS pairs and 12 non-portrait animations built from 114 distinct source frames | Static fallbacks, source frames, sheets, GIF previews, manifest, inventory, GFX handoff |
| `warlord_focus_icons_imagegen/` | 68 current warlord focus icons | Prompt ledger, source/alpha/processed/package DDS, contact sheets, validation, handoff |
| `unified_focus_assets/` | 108 unified-country focus icons | Generated sources, processed files, validation and handoff |
| `wendigo_focus_icons_imagegen/` | 28 Wendigo focus icons | Generated sources, processed files, validation and handoff |
| `registered_static_icons_imagegen/` | 30 current containment and route idea/decision/category assets | Generated sources, processed files, current validation and contact sheets |
| `remaining_registered_icons_imagegen/` | Remaining registered Event 014 idea, decision, and category assets | Generated sources, processed files, manifests and validation |
| `static_icons_imagegen/unified_decisions/` | 38 distinct live unified-decision icons | Source/processed files plus row-range manifests `manifest_rows_01_09.md`, `subsets/rows_10_24/manifest.md`, and `manifest_rows_25_39.md`. Matching row-range handoffs live under `docs/plans/014_cannibalism_plans/subagent_handoffs/` |
| `static_icons_imagegen/` | Other static icon families | Generated sources, subset manifests, processing and validation |
| `warlord_command_assets_imagegen/` | 32 current command surfaces plus two report-event pictures | Generated sources, prompt ledger, processed files, validation, contact sheets |
| `report_news_imagegen/` | Report and news picture families | Generated sources, processed files and handoff |
| `achievements_imagegen/` | 18 achievement triplets | Generated sources, locked/unlocked variants, validation and handoff |
| `static_event_art_imagegen/` | Four action-heavy super-event images and the remaining static event-art families | Exact source records, processed DDS, visual audit, manifests |
| `source_audio/` | Eight 44,100 Hz runtime files: four WAV for four unique licensed super-event recordings | Source files, research/evidence records and runtime handoff |

## Runtime closure

- Focus icons: 204 DDS files (68 warlord, 108 unified, 28 Wendigo).
- Decision/category textures: 135 DDS files.
- Registered idea/modifier textures: 62 DDS files.
- Report/news textures: 29 DDS files.
- Achievement textures: 54 DDS files for 18 achievements.
- Super-event images: 4 DDS files.
- Country flags: 195 unique TGA files from 65 separate built-in ImageGen masters across three sizes.
- Portrait textures: 56 warlord DDS portraits, two ordinary Hannibal DDS textures, and two Wendigo Hannibal DDS textures.
- Animation runtime: exactly 14 semantic packages with 142 source and 142 processed frames. Every package has real planned states, a sheet DDS, static fallback, GIF preview, contact sheet, manifest, and GFX handoff. The two portrait sheets run at 12 FPS with `gfx/FX/buttonstate_blendframes.lua`.
- Event 014 GFX closure: exactly one dedicated registry plus the two required shared registries, with 812 path references, 598 unique runtime paths, 598 unique hashes, and 0 missing paths.
- Unit/equipment visual scope: no custom subunit or equipment identifiers were added. Existing battalion and equipment surfaces remain in use, so no bespoke unit counter or equipment art is required. This is a verified scope disposition, not a fallback.

The per-package manifests carry exact dimensions, formats, prompts, source hashes, runtime hashes, and processing notes. `gfx_handoff.md` identifies the current registration files and cross-package ownership.

## Current exclusions

- No retired origin-specific focus, decision, idea, flag, portrait, or prompt remains in the current source packages or runtime registration.
- Generic prisoner protection, prisoner accounting, confinement-site seizure, transfer-record containment, and humanitarian recovery art remains where the live mechanics still use it.
- Protected unrelated Wendigo assets are not overwritten by this package.
- No actor likeness, prison portrait setting, living Indigenous-tradition claim, or borrowed sacred motif is used.
