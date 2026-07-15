# Event 014 Scripted GUI Dimension Ledger

> **Fulfilled frozen contract.** The measured dimensions below remain the wiring contract. Final static surfaces, twelve non-portrait frame packages, both real-frame portrait packages, hashes, and GFX handoff data are recorded in `docs/assets/014_cannibalism/gui_animation_portraits/manifest.md` and its validation ledgers.

Date frozen: 2026-07-11

This ledger is the implementation-owned size contract for the five Event 014 mechanic windows in `interface/014_cannibalism_frontline_hunger.gui`. It removes the former GUI-dimension blocker from the asset plan. Every final is fictional generated art and uses uncompressed 32-bit BGRA DDS.

## Window surfaces

| Surface | Runtime file | Exact size |
| --- | --- | ---: |
| Early containment background | `gfx/interface/014_cannibalism/early_category_background.dds` | 470x304 |
| Network background | `gfx/interface/014_cannibalism/network_window_background.dds` | 860x620 |
| Warlord command background | `gfx/interface/014_cannibalism/warlord_command_background.dds` | 470x340 |
| Revealed command background | `gfx/interface/014_cannibalism/revealed_command_background.dds` | 470x380 |
| Wendigo command background | `gfx/interface/014_cannibalism/wendigo_command_background.dds` | 470x400 |

## Static components

| Family | Runtime files | Exact size |
| --- | --- | ---: |
| Early meters | `field_hunger_meter.dds`, `command_integrity_meter.dds`, `cult_cohesion_meter.dds` | 278x48 each |
| Early state card | `primary_state_card.dds` | 278x72 |
| Network entries | `network_country_card.dds`, `network_state_card.dds` | 374x64 each |
| Network selected target | `network_target_frame.dds` | 374x64 |
| Warlord meters | `larder_meter.dds`, `frenzy_meter.dds`, `network_alignment_meter.dds` | 278x48 each |
| Warlord state card | `controlled_state_card.dds` | 278x72 |
| Revealed meters | `global_larder_meter.dds`, `global_network_meter.dds` | 278x48 each |
| Revealed cards | `warlord_loyalty_card.dds`, `continental_target_card.dds` | 278x72 each |
| Portrait frames | `revealed_portrait_frame.dds`, `transformed_portrait_frame.dds` | 166x220 each |
| Wendigo anchor card | `anchor_card.dds` | 278x72 |
| Wendigo meters | `countdown_frame.dds`, `wendigo_unit_capacity.dds`, `winter_hunger_meter.dds` | 278x48 each |

All static component paths above are rooted at `gfx/interface/014_cannibalism/`.

## Exact animation packages

| Animation | Frames | Frame size | Sheet size | Static and sheet runtime stems |
| --- | ---: | ---: | ---: | --- |
| Early warning seal | 8 | 64x64 | 512x64 | `cannibalism_early_warning_seal` |
| Cult Cohesion emblem | 8 | 64x64 | 512x64 | `cannibalism_cult_cohesion_emblem` |
| Network threads | 12 | 824x120 | 9888x120 | `cannibalism_network_threads` |
| Island alert | 8 | 64x64 | 512x64 | `cannibalism_island_alert` |
| Selected target overlay | 6 | 374x64 | 2244x64 | `cannibalism_selected_target_overlay` |
| Critical Larder glow | 8 | 64x64 | 512x64 | `cannibalism_critical_larder_glow` |
| Frenzy border | 8 | 142x54 | 1136x54 | `cannibalism_frenzy_border` |
| Warlord route emblem | 8 | 94x86 | 752x86 | `cannibalism_warlord_route_emblem` |
| Unification seal | 12 | 94x86 | 1128x86 | `cannibalism_unification_seal` |
| Ordinary terminal frame | 12 | 438x40 | 5256x40 | `cannibalism_ordinary_terminal_frame` |
| Wendigo anchor pulse | 12 | 64x64 | 768x64 | `cannibalism_wendigo_anchor_pulse` |
| Wendigo terminal frame | 12 | 438x40 | 5256x40 | `cannibalism_wendigo_terminal_frame` |

All non-portrait animation files are rooted at `gfx/interface/animated/014_cannibalism/`. Each package requires separate generated source frames, processed frames, a PNG sheet, the listed BGRA DDS sheet, a finished static fallback, a preview GIF, a contact sheet, a manifest row, and a GFX handoff row.

## Portrait animation packages

| Portrait | Frames | Frame size | Sheet size | Static runtime | Sheet runtime |
| --- | ---: | ---: | ---: | --- | --- |
| Ordinary revealed Hannibal | 12 | 156x210 | 1872x210 | `gfx/leaders/014_cannibalism/hannibal.dds` | `gfx/leaders/014_cannibalism/leader_CBL_hannibal_sheet.dds` |
| Wendigo Hannibal | 16 | 156x210 | 2496x210 | `gfx/leaders/014_cannibalism/hannibal_wendigo.dds` | `gfx/leaders/014_cannibalism/leader_ZZZ_hannibal_wendigo_sheet.dds` |

The ordinary portrait is reveal-gated. The transformed portrait is additionally gated by the Wendigo route. Neither portrait may resolve through an early or network GUI surface.

## Category art added by the final category registry

The nine missing category families use one 32x32 decision-category icon and one 114x101 category panel each:

- International Response
- Reconstruction
- Unified Command
- Unified Larder
- Unified War Machine
- Unified Global Campaign
- Unified World End
- Wendigo Command
- Wendigo Counterwar

The existing Containment, Network Alerts, and Warlord Command families retain their own distinct files. No category reuses another category's art.

## Interaction ownership

- Gameplay clicks remain in decisions and missions.
- GUI buttons only open, close, filter, sort, refresh, select a read-only scope, or toggle finished animations.
- The network ledger reads `global.cannibalism_actor_countries` and `global.cannibalism_node_states` into country-scoped view arrays.
- GUI state is cleared by the Event 014 country reset and global cleanup path.
- AI does not use the human GUI. It uses the same decisions, triggers, costs, and scripted effects directly.
