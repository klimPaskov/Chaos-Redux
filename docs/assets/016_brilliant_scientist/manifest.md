# Event 016 Brilliant Scientist asset and presentation manifest

Date: 2026-07-14

## Status

This is a planning and reconciliation manifest. The Doctor Warren Kruger stage-0 source package, shared scientist or leader portrait, and advisor portrait are produced, registered, and assigned to the fixed character in `common/characters/016_brilliant_scientist_characters.txt`. The opening appointment report card and the six-image report and super-event tranche below are produced and converted. Stage I through IV static and animated sprite contracts are pre-registered, while the other later visual families remain unproduced and unwired.

Super-event text and audio research are complete for all six packages. Six final Event 016-owned OGG files are ready under `music/016_brilliant_scientist/` at visible IDs 90 through 95. Commit `0e8c6f8e` performed the role-preserving rename to those IDs. Shared music definitions, sound wrappers, settings-aware playback, event triggers, GUI, and localisation remain parent-owned and unwired.

## Fixed inventory

| Family | Required count | Current final count | Wiring status |
| --- | ---: | ---: | --- |
| Super-event images | 6 | 6 | Runtime DDS present; parent-owned wiring pending |
| Achievement completed icons | 17 | 0 | Unwired |
| Achievement grey icons | 17 | 0 | Unwired |
| Achievement not-eligible icons | 17 | 0 | Unwired |
| Severe Kruger portrait animation families | 5 | 0 | Sprite contracts registered, assets and state wiring missing |
| Severe Kruger static fallbacks | 5 | 0 | Sprite contracts registered, assets and state wiring missing |
| Kruger stage-0 scientist or leader portrait | 1 | 1 | Registered and assigned to the fixed character |
| Kruger stage-0 advisor portrait | 1 | 1 | Registered and assigned to the fixed character |
| Kruger stages I through III portrait states | Specification-defined | 0 | Sprite contracts registered, assets and state wiring missing |
| Kruger State base and route flag triplets | Specification-defined | 0 | Unwired |
| Directorate UI art | Specification-defined | 0 | Unwired |
| Report and news images | Specification-defined | 7 reports / 0 news | Opening appointment plus six report-event tranche DDS present; parent-owned event references pending |
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

## Opening appointment report event

| Field | Evidence |
| --- | --- |
| Asset | Doctor Warren Kruger appointment dossier |
| Related event | `chaosx.nr16.2` first-host appointment and `chaosx.nr16.3` referred-recipient appointment |
| Event slug | `016_brilliant_scientist` |
| Asset type | Static report event picture |
| Intended use | Replace the raw Stage-0 portrait presentation in the two visible opening appointment events with a period dossier or report-card image |
| Source mode | User-directed repository-tracked Stage-0 identity derivative; no image generation and no internet source |
| Source PNG | `docs/assets/016_brilliant_scientist/source_png/report_events/report_event_016_brilliant_scientist_appointment_source.png` |
| Processed PNG | `docs/assets/016_brilliant_scientist/processed_png/report_events/report_event_016_brilliant_scientist_appointment.png` |
| Final DDS | `gfx/event_pictures/016_brilliant_scientist/report_event_016_brilliant_scientist_appointment.dds` |
| Review contact sheet | `docs/assets/016_brilliant_scientist/contact_sheets/report_event_016_brilliant_scientist_appointment_contact_sheet.png` |
| Target size | `210x176` |
| Proposed sprite | `GFX_report_event_016_brilliant_scientist_appointment` |
| Target GFX | `interface/016_brilliant_scientist.gfx` |
| Localisation | Not applicable; the image is shared by the existing `chaosx.nr16.2` and `chaosx.nr16.3` text surfaces |
| Status | `wired` |

### Source and identity provenance

- The source PNG is `206x164` RGBA and fully opaque, with SHA-256 `33C8ADD65AFB63DD6CD7E995E1C1DF05A2AD264B9D4F2802C8AB77DF8FF29D4D`.
- Pixels `x=25..180`, `y=0..163` are exactly identical to pixels `x=0..155`, `y=0..163` of `docs/assets/016_brilliant_scientist/source_png/portraits/portrait_generic_biowarfare_europe_male_01_decoded.png`. The remaining source pixels are symmetric 25-pixel blue-grey side margins. No face, clothing, anatomy, or stage detail was generated, repainted, or substituted.
- The source inherits the Stage-0 licensing note. It is approved for internal Event 016 use, is not claimed as public domain, and has unresolved external redistribution rights.
- Stage I and later source art was not opened, processed, or reused for this asset.

### Processing and output record

- `.agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py` applied the standard report treatment with a `192x153` card, 2-pixel paper border, 3-degree tilt, soft shadow, monochrome sepia tone, deterministic grain seed `1616`, and a transparent `210x176` RGBA canvas.
- The processed PNG has SHA-256 `716CEC05CDD2F66E4FA96D61261857AD9676AAAED115E28D1411C3E3CFFAF03E`. Its four corner alpha values are zero, its alpha range is `0..255`, its non-zero alpha bounding box is `(5, 6, 209, 174)`, and every outer edge remains fully transparent, so neither the card nor shadow is hard-clipped.
- `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` produced a one-level legacy uncompressed BGRA DDS with SHA-256 `5DFD9CC830A650271D7C66A3501E51F027ED160935151FB0153C8C1FDBB65B5B`. The file is exactly `147968` bytes, matching the 128-byte header plus `210 * 176 * 4` bytes of pixel data.
- The DDS declares a 124-byte legacy header, `210x176`, pitch `840`, `DDS_PIXELFORMAT` size `32`, flags `65`, 32-bit BGRA masks `0x00FF0000`, `0x0000FF00`, `0x000000FF`, and `0xFF000000`, and `DDSCAPS_TEXTURE` at byte 108. Pillow decodes it successfully, and the decoded RGBA pixels are exactly identical to the processed PNG.
- The contact sheet has SHA-256 `B3FB28D7A90738845EA074BB09099EAE6DEC056D8B6D60F67F1C98D2A3FFB9D7` and shows the approved source, processed RGBA card over a checker background, and decoded DDS together for review.

Sprite registration and event-reference instructions are in `docs/assets/016_brilliant_scientist/gfx_handoff.md`. The bounded production handoff is `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_opening_report_asset_handoff.md`.

## Six super-event packages

| Visible ID | Role | Text status | Image status | Audio status | Live wiring |
| ---: | --- | --- | --- | --- | --- |
| 90 | International recognition | Selected and sourced | Complete DDS present | Final OGG ready | Parent-owned live wiring pending |
| 91 | Kruger State formation | Selected and sourced | Complete DDS present | Final OGG ready | Parent-owned live wiring pending |
| 92 | Global Kruger threat | Selected and sourced | Complete DDS present | Final OGG ready | Parent-owned live wiring pending |
| 93 | Laboratory World | Selected and sourced | Complete DDS present | Final OGG ready | Parent-owned live wiring pending |
| 94 | Strategic Singularity | Selected and sourced | Complete DDS present | Final OGG ready | Parent-owned live wiring pending |
| 95 | Qualifying defeat aftermath | Selected and sourced | Complete DDS present | Final OGG ready | Parent-owned live wiring pending |

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
- The opening appointment report and the six-image report and super-event tranche are produced. News images, Stage I through IV portrait art, and animation packages remain unproduced.
- Final OGGs are ready, but parent-owned shared music and optional sound-channel wiring remain absent.
- Stage-0 GFX registration and character assignment are complete, and later portrait contracts are pre-registered. Later portrait files, GUI state wiring, achievement wiring, shared music and sound wiring, localisation, and gameplay wiring remain absent.
- External redistribution rights for the copied stage-0 base remain unresolved. Internal Event 016 use is explicitly user-authorized.

## 2026-07-24 report and super-event image tranche

All rows in this tranche use source mode `$imagegen` for fictional alternate-history period documentary art. Report rows received the repository report-card processor and super-event rows received deterministic cover crop and resize. Full prompts and reference provenance are recorded in `docs/assets/016_brilliant_scientist/prompts/016_reports_and_super_event_prompts.md`. Row-level hashes, dimensions, alpha, DDS header, and exact-length checks are in `docs/assets/016_brilliant_scientist/validation/016_reports_and_super_technical_validation.md`. Source, processed, and decoded-DDS contact sheets are in `docs/assets/016_brilliant_scientist/contact_sheets/`.

### Report-event images

| Asset | Narrative use | Source PNG | Processed PNG | Final DDS | Target size | Sprite | Target GFX | Status |
| --- | --- | --- | --- | --- | ---: | --- | --- | --- |
| `report_event_016_brilliant_scientist_evolution_1` | National scientific ascendancy demonstration. | `docs/assets/016_brilliant_scientist/source_png/report_events/report_event_016_brilliant_scientist_evolution_1_source.png` | `docs/assets/016_brilliant_scientist/processed_png/report_events/report_event_016_brilliant_scientist_evolution_1.png` | `gfx/event_pictures/016_brilliant_scientist/report_event_016_brilliant_scientist_evolution_1.dds` | `210x176` | `GFX_report_event_016_brilliant_scientist_evolution_1` | `interface/016_brilliant_scientist.gfx` | `complete; parent wiring pending` |
| `report_event_016_brilliant_scientist_evolution_2` | International scientific contest and recognition. | `docs/assets/016_brilliant_scientist/source_png/report_events/report_event_016_brilliant_scientist_evolution_2_source.png` | `docs/assets/016_brilliant_scientist/processed_png/report_events/report_event_016_brilliant_scientist_evolution_2.png` | `gfx/event_pictures/016_brilliant_scientist/report_event_016_brilliant_scientist_evolution_2.dds` | `210x176` | `GFX_report_event_016_brilliant_scientist_evolution_2` | `interface/016_brilliant_scientist.gfx` | `complete; parent wiring pending` |
| `report_event_016_brilliant_scientist_evolution_3` | Forbidden-science chamber opening. | `docs/assets/016_brilliant_scientist/source_png/report_events/report_event_016_brilliant_scientist_evolution_3_source.png` | `docs/assets/016_brilliant_scientist/processed_png/report_events/report_event_016_brilliant_scientist_evolution_3.png` | `gfx/event_pictures/016_brilliant_scientist/report_event_016_brilliant_scientist_evolution_3.dds` | `210x176` | `GFX_report_event_016_brilliant_scientist_evolution_3` | `interface/016_brilliant_scientist.gfx` | `complete; parent wiring pending` |
| `report_event_016_brilliant_scientist_evolution_4` | Sovereign laboratory district takeover. | `docs/assets/016_brilliant_scientist/source_png/report_events/report_event_016_brilliant_scientist_evolution_4_source.png` | `docs/assets/016_brilliant_scientist/processed_png/report_events/report_event_016_brilliant_scientist_evolution_4.png` | `gfx/event_pictures/016_brilliant_scientist/report_event_016_brilliant_scientist_evolution_4.dds` | `210x176` | `GFX_report_event_016_brilliant_scientist_evolution_4` | `interface/016_brilliant_scientist.gfx` | `complete; parent wiring pending` |
| `report_event_016_brilliant_scientist_directorate_dossier` | People-free directorate portfolio and intelligence dossier. | `docs/assets/016_brilliant_scientist/source_png/report_events/report_event_016_brilliant_scientist_directorate_dossier_source.png` | `docs/assets/016_brilliant_scientist/processed_png/report_events/report_event_016_brilliant_scientist_directorate_dossier.png` | `gfx/event_pictures/016_brilliant_scientist/report_event_016_brilliant_scientist_directorate_dossier.dds` | `210x176` | `GFX_report_event_016_brilliant_scientist_directorate_dossier` | `interface/016_brilliant_scientist.gfx` | `complete; parent wiring pending` |
| `report_event_016_brilliant_scientist_sovereignty_confrontation` | State and private laboratory perimeter confrontation. | `docs/assets/016_brilliant_scientist/source_png/report_events/report_event_016_brilliant_scientist_sovereignty_confrontation_source.png` | `docs/assets/016_brilliant_scientist/processed_png/report_events/report_event_016_brilliant_scientist_sovereignty_confrontation.png` | `gfx/event_pictures/016_brilliant_scientist/report_event_016_brilliant_scientist_sovereignty_confrontation.dds` | `210x176` | `GFX_report_event_016_brilliant_scientist_sovereignty_confrontation` | `interface/016_brilliant_scientist.gfx` | `complete; parent wiring pending` |

### Super-event images

| Visible ID | Asset | Narrative role | Source PNG | Processed PNG | Final DDS | Target size | Sprite | Target GFX | Status |
| ---: | --- | --- | --- | --- | --- | ---: | --- | --- | --- |
| 90 | `super_event_016_international_recognition` | The Endless Frontier, global scientific recognition. | `docs/assets/016_brilliant_scientist/source_png/super_events/super_event_016_international_recognition_source.png` | `docs/assets/016_brilliant_scientist/processed_png/super_events/super_event_016_international_recognition.png` | `gfx/super_events/016_brilliant_scientist/super_event_016_international_recognition.dds` | `457x328` | `GFX_super_event_016_international_recognition` | `interface/016_brilliant_scientist_super_events.gfx` | `complete; parent wiring pending` |
| 91 | `super_event_016_kruger_state_formation` | A New Order of Things, sovereign state formation. | `docs/assets/016_brilliant_scientist/source_png/super_events/super_event_016_kruger_state_formation_source.png` | `docs/assets/016_brilliant_scientist/processed_png/super_events/super_event_016_kruger_state_formation.png` | `gfx/super_events/016_brilliant_scientist/super_event_016_kruger_state_formation.dds` | `457x328` | `GFX_super_event_016_kruger_state_formation` | `interface/016_brilliant_scientist_super_events.gfx` | `complete; parent wiring pending` |
| 92 | `super_event_016_global_kruger_threat` | The Empire of Method, organized global project threat. | `docs/assets/016_brilliant_scientist/source_png/super_events/super_event_016_global_kruger_threat_source.png` | `docs/assets/016_brilliant_scientist/processed_png/super_events/super_event_016_global_kruger_threat.png` | `gfx/super_events/016_brilliant_scientist/super_event_016_global_kruger_threat.dds` | `457x328` | `GFX_super_event_016_global_kruger_threat` | `interface/016_brilliant_scientist_super_events.gfx` | `complete; parent wiring pending` |
| 93 | `super_event_016_laboratory_world` | All Things Possible, terminal administrative laboratory order. | `docs/assets/016_brilliant_scientist/source_png/super_events/super_event_016_laboratory_world_source.png` | `docs/assets/016_brilliant_scientist/processed_png/super_events/super_event_016_laboratory_world.png` | `gfx/super_events/016_brilliant_scientist/super_event_016_laboratory_world.dds` | `457x328` | `GFX_super_event_016_laboratory_world` | `interface/016_brilliant_scientist_super_events.gfx` | `complete; parent wiring pending` |
| 94 | `super_event_016_strategic_singularity` | The World Set Free, strategic-singularity terminal firing. | `docs/assets/016_brilliant_scientist/source_png/super_events/super_event_016_strategic_singularity_source.png` | `docs/assets/016_brilliant_scientist/processed_png/super_events/super_event_016_strategic_singularity.png` | `gfx/super_events/016_brilliant_scientist/super_event_016_strategic_singularity.dds` | `457x328` | `GFX_super_event_016_strategic_singularity` | `interface/016_brilliant_scientist_super_events.gfx` | `complete; parent wiring pending` |
| 95 | `super_event_016_qualifying_defeat` | Trustees of the Ruins, qualifying global defeat aftermath. | `docs/assets/016_brilliant_scientist/source_png/super_events/super_event_016_qualifying_defeat_source.png` | `docs/assets/016_brilliant_scientist/processed_png/super_events/super_event_016_qualifying_defeat.png` | `gfx/super_events/016_brilliant_scientist/super_event_016_qualifying_defeat.dds` | `457x328` | `GFX_super_event_016_qualifying_defeat` | `interface/016_brilliant_scientist_super_events.gfx` | `complete; parent wiring pending` |
