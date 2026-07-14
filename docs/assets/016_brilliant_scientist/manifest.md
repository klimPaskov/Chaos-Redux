# Event 016 Brilliant Scientist asset and presentation manifest

Date: 2026-07-14

## Status

This is a planning and reconciliation manifest. The Doctor Warren Kruger stage-0 source package, shared scientist or leader portrait, and advisor portrait are produced and registered in `interface/016_brilliant_scientist.gfx`. Their final character assignment remains part of the incomplete gameplay lifecycle. Stage I through IV static and animated sprite contracts are pre-registered, but all referenced later assets remain unproduced. All other Event 016 visual assets remain unproduced and unwired.

Super-event text and audio research are complete for all six packages. Six final Event 016-owned OGG files are ready under `music/016_brilliant_scientist/` at visible IDs 90 through 95. Commit `0e8c6f8e` performed the role-preserving rename to those IDs. Shared music definitions, sound wrappers, settings-aware playback, event triggers, GUI, and localisation remain parent-owned and unwired.

## Fixed inventory

| Family | Required count | Current final count | Wiring status |
| --- | ---: | ---: | --- |
| Super-event images | 6 | 0 | Unwired |
| Achievement completed icons | 17 | 0 | Unwired |
| Achievement grey icons | 17 | 0 | Unwired |
| Achievement not-eligible icons | 17 | 0 | Unwired |
| Severe Kruger portrait animation families | 5 | 0 | Sprite contracts registered, assets and state wiring missing |
| Severe Kruger static fallbacks | 5 | 0 | Sprite contracts registered, assets and state wiring missing |
| Kruger stage-0 scientist or leader portrait | 1 | 1 | Registered, character assignment pending |
| Kruger stage-0 advisor portrait | 1 | 1 | Registered, character assignment pending |
| Kruger stages I through III portrait states | Specification-defined | 0 | Sprite contracts registered, assets and state wiring missing |
| Kruger State base and route flag triplets | Specification-defined | 0 | Unwired |
| Directorate UI art | Specification-defined | 0 | Unwired |
| Report and news images | Specification-defined | 0 | Unwired |
| Focus, idea, decision, category, project, technology, unit, and equipment icons | Specification-defined | 0 | Unwired |

## Doctor Warren Kruger stage-0 source package

### Source and provenance

- Approved source mode: user-directed repository-tracked source asset.
- Authoritative source location: `gfx/leaders/scientists/generic_scientists/portrait_generic_biowarfare_europe_male_01.dds`.
- Immutable Event 016 source copy: `docs/assets/016_brilliant_scientist/source_dds/originals/portrait_generic_biowarfare_europe_male_01.dds`.
- Repository provenance: introduced by Klim Pashkov in commit `6aa363c64195eb9dbb4faed174e8493287666715` on 2025-08-08, commit subject `Biowarfare facilities scientists and historical starting locations`.
- Original and immutable-copy SHA-256: `5D0CF3F973B6099DB895C96A6FED9544F30873076985DDF885032793C5183075`.
- Source encoding: legacy uncompressed 32-bit BGRA DDS, `156x210`, eight mip levels, fully opaque alpha.
- Decoded reference: `docs/assets/016_brilliant_scientist/source_png/portraits/portrait_generic_biowarfare_europe_male_01_decoded.png`, RGBA PNG, `156x210`, SHA-256 `13BE2B86DB91C89A2C3588DC7B2A22D64563DB9B8632AB82DCC334272114318D`.
- License status: no standalone license or public-domain statement is stored with the tracked source. It is approved for this project by the user and is not claimed as public domain. External redistribution rights remain unresolved.
- Vanilla comparison: the source is neither byte-identical nor decoded-pixel-identical to vanilla `gfx/leaders/scientists/generic_scientists/portrait_generic_europe_male_01.dds`.

### Final static outputs

| Asset | Use | Processed PNG | Final DDS | Dimensions and encoding | Proposed sprite | Target GFX | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Doctor Warren Kruger stage-0 scientist or leader portrait | Special-project scientist `large` portrait and later leader portrait | `docs/assets/016_brilliant_scientist/processed_png/portraits/leader_doctor_warren_kruger_stage_0.png` | `gfx/leaders/KRG/leader_doctor_warren_kruger_stage_0.dds` | `156x210`, exact BGRA DDS copy with eight mip levels | `GFX_portrait_KRG_doctor_warren_kruger_stage_0` | `interface/016_brilliant_scientist.gfx` | `complete_registered` |
| Doctor Warren Kruger stage-0 advisor portrait | Advisor or theorist `small` portrait | `docs/assets/016_brilliant_scientist/processed_png/portraits/idea_doctor_warren_kruger_stage_0.png` | `gfx/interface/ideas/016_brilliant_scientist/idea_doctor_warren_kruger_stage_0.dds` | `65x67`, legacy one-level uncompressed BGRA DDS | `GFX_idea_doctor_warren_kruger_stage_0` | `interface/016_brilliant_scientist.gfx` | `complete_registered` |

The runtime large DDS is byte-identical to the approved tracked source and has SHA-256 `5D0CF3F973B6099DB895C96A6FED9544F30873076985DDF885032793C5183075`. The advisor DDS has SHA-256 `487F5D52167543FAFB998A103C1576321AC1DE67FFFDCF804F3B3AAF55122503`. Vanilla scientist characters use one `portraits = { army = { large = ... small = ... } }` family. The `156x210` large portrait therefore serves the scientist and later leader surfaces without a redundant second scientist DDS. The advisor derivative uses the verified vanilla `65x67` small-character surface rather than a guessed `64x64` icon.

GFX and character wiring details are in `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_base_portrait_source_handoff.md`. Commit `43125d91a` registered the two stage-0 sprites. The later Stage I through IV names currently registered in `interface/016_brilliant_scientist.gfx` are filename contracts only. No referenced later portrait DDS or animated sheet exists yet.

## Six super-event packages

| Visible ID | Role | Text status | Image status | Audio status | Live wiring |
| ---: | --- | --- | --- | --- | --- |
| 90 | International recognition | Selected and sourced | Missing | Final OGG ready | Missing |
| 91 | Kruger State formation | Selected and sourced | Missing | Final OGG ready | Missing |
| 92 | Global Kruger threat | Selected and sourced | Missing | Final OGG ready | Missing |
| 93 | Laboratory World | Selected and sourced | Missing | Final OGG ready | Missing |
| 94 | Strategic Singularity | Selected and sourced | Missing | Final OGG ready | Missing |
| 95 | Qualifying defeat aftermath | Selected and sourced | Missing | Final OGG ready | Missing |

Text evidence: `docs/super_events/016_brilliant_scientist_super_event_research.md`.

Audio evidence and exact final paths: `docs/super_events/016_brilliant_scientist_super_event_audio_research.md` and `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_super_event_audio_research_handoff.md`.

International recognition and defeat are conditional at runtime. They remain required production packages.

Live reservation supersession, 2026-07-14: Event 015 occupies visible super-event slots 85 through 89, so Event 016 uses slots 90 through 95. Event 016 world-end scenario IDs remain 11 and 12.

## Severe portrait packages

| Package | Frames | Static fallback | Manifest | Contact sheet | Preview | GFX handoff |
| --- | --- | --- | --- | --- | --- | --- |
| Clone Kruger | Missing | Missing | Missing | Missing | Missing | Missing |
| Machine-linked Kruger | Missing | Missing | Missing | Missing | Missing | Missing |
| Temporal Continuum Kruger | Missing | Missing | Missing | Missing | Missing | Missing |
| Xenobiological or alien Kruger | Missing | Missing | Missing | Missing | Missing | Missing |
| Synthesis Kruger | Missing | Missing | Missing | Missing | Missing | Missing |

The xenobiological-or-alien package follows the campaign conclusion actually proven. Transformation alone must not make the asset imply extraterrestrial provenance.

## Achievement icon triplets

Seventeen working slugs require completed, grey, and not-eligible variants:

`borrowed_century`, `every_door`, `public_method`, `the_one_who_left`, `clean_break`, `approve_everything`, `the_former_host`, `combined_arms_redefined`, `clever_girl`, `the_machine_continues`, `population_one`, `yesterday_sent_help`, `not_from_here`, `no_second_sun`, `the_last_calculation`, `the_world_is_the_laboratory`, and `ordinary_people_won`.

`public_method` and `clean_break` remain separate.

## Planned roots and registration

- Event and report art: `gfx/event_pictures/016_brilliant_scientist/`.
- UI art: `gfx/interface/016_brilliant_scientist/`.
- Ideas: `gfx/interface/ideas/016_brilliant_scientist/`.
- Focuses: `gfx/interface/goals/016_brilliant_scientist/`.
- Technologies: `gfx/interface/technologies/016_brilliant_scientist/`.
- Leaders: `gfx/leaders/KRG/`.
- Super-events: `gfx/super_events/016_brilliant_scientist/`.
- Achievements: `gfx/achievements/`.
- Flags: `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`.
- Event-owned sprites: `interface/016_brilliant_scientist.gfx`.
- Shared super-event sprites: `interface/chaosx_super_events.gfx` after live ID reservation.

## Required production handoffs

Every final visual asset needs source or generation evidence, processed PNG, final DDS or flag output, exact dimensions, stable filename, target sprite, target code reference, and manifest row.

Every final animation additionally needs separately created source frames, processed frames, a horizontal sheet, static fallback, preview GIF, contact sheet, timing, anchor, trigger, and GFX or GUI handoff. Transform-only motion is not acceptable.

Every final audio package needs source URL, author or performer, work and recording identity, rights evidence, access date, duration, source file, converted OGG, proposed live identifier, sound wrapper, volume behavior, settings-aware playback, and documentation. No generic or shared fallback track is authorized.

## Blockers

- Visible super-event IDs 90 to 95 and world-end scenario IDs 11 and 12 are reserved. Their live shared-registry entries are not implemented.
- Later image and animation production has not started. Stage 0 is the completed exception.
- Final OGGs are ready, but parent-owned shared music and optional sound-channel wiring remain absent.
- Stage-0 GFX registration is complete, and later portrait contracts are pre-registered. Character assignment, later portrait files, GUI state wiring, achievement wiring, shared music and sound wiring, localisation, and gameplay wiring remain absent.
- External redistribution rights for the copied stage-0 base remain unresolved. Internal Event 016 use is explicitly user-authorized.
