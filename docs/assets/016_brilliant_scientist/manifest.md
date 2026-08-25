# Event 016 Brilliant Scientist asset and presentation manifest

Date: 2026-07-29

## Status

This is the current core-runtime asset manifest. Doctor Warren Kruger's stage-0 source package and all fourteen later leader/scientist and advisor states are produced, registered, and selected by the fixed character lifecycle. The six severe route sheets contain real frame-by-frame source art and have static fallbacks. The Directorate UI, focus tree, achievements, country flags, project and decision surfaces, report events, super-events, and sound package all resolve to registered runtime files.

Super-event text and audio are complete for all six packages. Six Event 016-owned WAV cues live under `sound/016_brilliant_scientist/`, and `sound/chaosx_sound.asset` registers tracks and settings-aware volume variants for visible IDs 90 through 95. Shared super-event image, title, quotation, button, description, sound, and settings selectors include all six IDs.

## Fixed inventory

| Family | Required count | Current final count | Wiring status |
| --- | ---: | ---: | --- |
| Super-event images | 6 | 6 | Runtime DDS present and shared presentation wiring complete |
| Achievement completed icons | 17 | 17 | Runtime DDS present and achievement registrations wired |
| Achievement grey icons | 17 | 17 | Runtime DDS present and achievement registrations wired |
| Achievement not-eligible icons | 17 | 17 | Runtime DDS present and achievement registrations wired |
| Severe Kruger portrait animation families | 6 | 6 | Real frame sheets registered for clone, machine, temporal, xenobiological, alien-revealed, and synthesis routes |
| Severe Kruger static fallbacks | 6 | 6 | Static fallbacks registered and selected when animation is disabled |
| Kruger stage-0 scientist or leader portrait | 1 | 1 | Registered and assigned to the fixed character |
| Kruger stage-0 advisor portrait | 1 | 1 | Registered and assigned to the fixed character |
| Kruger stages I through IV leader or scientist portrait states | 14 | 14 | Runtime DDS files present and registered; final state-selection review separate |
| Kruger stages I through IV advisor portrait states | 14 | 14 | Canonical template migration complete and registered; final state-selection review separate |
| Kruger State base and route flag triplets | 7 triplets | 7 triplets | Base and six route cosmetics present at normal, medium, and small sizes |
| Directorate UI art | 64 runtime DDS | 64 | Dashboard, meters, state cards, controls, animation sheets, and fallbacks registered |
| Report and news images | Specification-defined | 25 Event 016 reports / 7 Event 016 news | Twenty-five report DDS files are registered: the appointment card, four evolution cards, the dossier and sovereignty cards, three institutional cards, eight breakthrough-family cards, eight incident/security cards, four aftermath-family cards, and the shared remnant card. Seven public-milestone news DDS files are registered, including the regional-defeat headline. |
| Focus, idea, decision, category, project, technology, unit, and equipment icons | Specification-defined | 100 focus; 28 idea; 16 project; 40 KRG decision; 10 KRG category; 22 aftermath decision; 4 aftermath category | Runtime DDS and `.gfx` registrations present; the 21-icon KRG country-idea extension is documented under `krg_country_idea_icons/`; project-force model/entity art remains separate |
| Alien Infantry reusable 2D package | 2 counters; 1 equipment; 2 technologies; 2 tactics; 1 KRG production decision | 8 | Original runtime DDS files and `interface/alien_infantry_system.gfx` registrations are present; the retired family assets were removed. |
| D’Rhondan contact and country event art | 10 event images; 10 decision/category icons; 1 special-project icon; 2 country-interface pieces | 23 | Runtime DDS files and `interface/016_dhrondan_assets.gfx` registrations are present. |
| DHR flags and portraits | 4 flag identities in 3 sizes; 12 full portraits; 9 role cards | 12 flag files; 12 full portraits; 9 role cards | Runtime files and `interface/016_dhrondan_portraits.gfx` registrations are present. |
| DHR focus and spirit art | 88 focus icons; 11 lifecycle ideas | 99 | Runtime DDS files and 187 base, shine, and idea sprite registrations are present in `interface/016_dhrondan_focus_icons.gfx`. |
| Alien Infantry 3D model package | 1 entity; 7 genuine actions; synchronized sourced audio | 0 accepted runtime entity outputs; 5 accepted Meshy source roles | Meshy V10 preserves a firearm-bearing model and genuine idle, move, defend, retreat, and death source clips. Three distinct firearm presets failed the required aim-discharge-recoil-recovery gate; support attack and a stable muzzle locator are also unavailable. No fallback entity, partial action alias, `.mesh`/`.anim`, export, reimport proof, or sound binding is wired. The authoritative V10 handoff is `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_alien_infantry_meshy_v10_runtime_handoff_2026-08-26.md`. |

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

The runtime large DDS is byte-identical to the approved tracked source and has SHA-256 `5D0CF3F973B6099DB895C96A6FED9544F30873076985DDF885032793C5183075`. The advisor DDS has SHA-256 `53AEAE1168CFA8B20A5DF4DAB33F13D218939ACDCADC68A3D898CB4520A02802`. Vanilla scientist characters use one `portraits = { army = { large = ... small = ... } }` family. The `156x210` large portrait therefore serves the scientist and later leader surfaces without a redundant second scientist DDS. The advisor derivative uses the verified vanilla `65x67` small-character surface rather than a guessed `64x64` icon.

The stage-0 advisor card uses `.agents/skills/chaos-redux-event-assets/tools/create_advisor_icon.py` SHA-256 `0080C7BA20C7A19B50C49885B66B775C1967B2CAAAEDCB63230725CB3656E0B0` and canonical template SHA-256 `8F594EF62AFBA6FDEC58DE66A80609350DCFE884320B11E6CB6220F1A0E19F58`. The runtime composition has exactly two layers: the transformed portrait first and the untouched `65x67` `advisor_template.png` on top. The complete `156x210` portrait is used without a crop and resized to the native `65x67` advisor canvas before receiving transformed size `33x46`, rotation `-6`, offset `1` left and `1` up from template opening center `25 32.5`, final portrait center `24 31.5`, and sepia strength `0.18`. No separate frame, paper, shadow, threshold, blur, edge, or component reconstruction remains. An eight-candidate coarse study and six-candidate fine study selected this placement for opening coverage, face readability, head and shoulder retention, left rotation, and paper overlap. The processed review PNG has SHA-256 `EEEA4A4C058722ACEBE1FECE6B45274C574BCB32E671F5EAEA6C4FCF03B08A60`.

Independent visual-fit review passed in `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_stage0_simple_advisor_visual_review.md`. The review confirmed complete-source use, native first resize, opening coverage, face centering, paper clearance, template retention, and alpha integrity.

GFX and character wiring details are in `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_base_portrait_source_handoff.md`. Commit `43125d91a` registered the two stage-0 sprites. The later Stage I through IV sprite contracts in `interface/016_brilliant_scientist.gfx` now resolve to existing leader or scientist and advisor DDS files. The fourteen later advisor cards use the same complete-source, native-first, no-warp template compositor as Stage 0, with content-sensitive `33x46`, `36x50`, or `39x54` transformed sizes. Exact transforms, hashes, validation, and independent review are recorded in `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_advisor_template_migration_handoff.md` and `docs/assets/016_brilliant_scientist/advisor_candidates/metadata/kruger_advisor_template_migration.json`.

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
| 90 | International recognition | Selected and sourced | Complete DDS present | Final WAV present | Shared image, text, sound, and trigger wiring complete |
| 91 | Kruger State formation | Selected and sourced | Complete DDS present | Final WAV present | Shared image, text, sound, and trigger wiring complete |
| 92 | Global Kruger threat | Selected and sourced | Complete DDS present | Final WAV present | Shared image, text, sound, and trigger wiring complete |
| 93 | Laboratory World | Selected and sourced | Complete DDS present | Final WAV present | Shared image, text, sound, and trigger wiring complete |
| 94 | Strategic Singularity | Selected and sourced | Complete DDS present | Final WAV present | Shared image, text, sound, and trigger wiring complete |
| 95 | Qualifying defeat aftermath | Selected and sourced | Complete DDS present | Final WAV present | Shared image, text, sound, and trigger wiring complete |

Text evidence: `docs/super_events/016_brilliant_scientist/text_research.md`.

Audio evidence and exact final paths: `docs/super_events/016_brilliant_scientist/audio_research.md` and `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_super_event_audio_research_handoff.md`.

International recognition and defeat are conditional at runtime. They remain required production packages.

Live reservation supersession, 2026-07-14: Event 015 occupies visible super-event slots 85 through 89, so Event 016 uses slots 90 through 95. Event 016 world-end scenario IDs remain 11 and 12.

## Severe portrait packages

| Package | Frames | Static fallback | Manifest | Contact sheet | Preview | GFX handoff |
| --- | --- | --- | --- | --- | --- | --- |
| Clone Kruger | 10 source and processed frames; `processed_png/animations/doctor_warren_kruger_stage_4_clone_sheet.png` and registered runtime sheet DDS present | `gfx/leaders/KRG/leader_doctor_warren_kruger_stage_4_clone.dds` present and registered | `package_records/portrait_animation_package.json` route entry | `contact_sheets/doctor_warren_kruger_stage_4_clone_contact_sheet.png` | `previews/doctor_warren_kruger_stage_4_clone_preview.gif` | `interface/016_brilliant_scientist.gfx` `GFX_kruger_directorate_portrait_stage_4_clone_animated` |
| Machine-linked Kruger | 10 source and processed frames; `processed_png/animations/doctor_warren_kruger_stage_4_machine_sheet.png` and registered runtime sheet DDS present | `gfx/leaders/KRG/leader_doctor_warren_kruger_stage_4_machine.dds` present and registered | `package_records/portrait_animation_package.json` route entry | `contact_sheets/doctor_warren_kruger_stage_4_machine_contact_sheet.png` | `previews/doctor_warren_kruger_stage_4_machine_preview.gif` | `interface/016_brilliant_scientist.gfx` `GFX_kruger_directorate_portrait_stage_4_machine_animated` |
| Temporal Continuum Kruger | 12 source and processed frames; `processed_png/animations/doctor_warren_kruger_stage_4_temporal_sheet.png` and registered runtime sheet DDS present | `gfx/leaders/KRG/leader_doctor_warren_kruger_stage_4_temporal.dds` present and registered | `package_records/portrait_animation_package.json` route entry | `contact_sheets/doctor_warren_kruger_stage_4_temporal_contact_sheet.png` | `previews/doctor_warren_kruger_stage_4_temporal_preview.gif` | `interface/016_brilliant_scientist.gfx` `GFX_kruger_directorate_portrait_stage_4_temporal_animated` |
| Xenobiological or alien Kruger | 10 source and processed frames in each evidence-gated output; `processed_png/animations/doctor_warren_kruger_stage_4_xenobiological_sheet.png` and `processed_png/animations/doctor_warren_kruger_stage_4_alien_revealed_sheet.png` plus registered runtime sheet DDS files present | `gfx/leaders/KRG/leader_doctor_warren_kruger_stage_4_xenobiological.dds` and `gfx/leaders/KRG/leader_doctor_warren_kruger_stage_4_alien_revealed.dds` present and registered | `package_records/portrait_animation_package.json` two route entries | `contact_sheets/doctor_warren_kruger_stage_4_xenobiological_contact_sheet.png` and `contact_sheets/doctor_warren_kruger_stage_4_alien_revealed_contact_sheet.png` | `previews/doctor_warren_kruger_stage_4_xenobiological_preview.gif` and `previews/doctor_warren_kruger_stage_4_alien_revealed_preview.gif` | `interface/016_brilliant_scientist.gfx` `GFX_kruger_directorate_portrait_stage_4_xenobiological_animated` and `GFX_kruger_directorate_portrait_stage_4_alien_revealed_animated` |
| Synthesis Kruger | 12 source and processed frames; `processed_png/animations/doctor_warren_kruger_stage_4_synthesis_sheet.png` and registered runtime sheet DDS present | `gfx/leaders/KRG/leader_doctor_warren_kruger_stage_4_synthesis.dds` present and registered | `package_records/portrait_animation_package.json` route entry | `contact_sheets/doctor_warren_kruger_stage_4_synthesis_contact_sheet.png` | `previews/doctor_warren_kruger_stage_4_synthesis_preview.gif` | `interface/016_brilliant_scientist.gfx` `GFX_kruger_directorate_portrait_stage_4_synthesis_animated` |

The table records five binding package families represented by six runtime sheets. Xenobiological and alien-revealed are separate evidence-gated outputs within the combined xenobiological-or-alien family, and transformation alone must not make either output imply extraterrestrial provenance. The package record resolves the source frames, processed frames, sheets, runtime DDS files, static fallbacks, previews, and contact sheets listed above. Live GUI animation and state-selection acceptance remains a separate user-owned gate.

## KRG country-idea icon extension

The 21 previously unassigned visible Kruger State lifecycle and project ideas now have bespoke 64x64 ImageGen source masters, processed RGBA previews, final uncompressed BGRA DDS files, decoded review images, contact sheets, prompts, hashes, and header validation under `docs/assets/016_brilliant_scientist/krg_country_idea_icons/`. The parent-owned `common/ideas/016_brilliant_scientist_country_ideas.txt` and `interface/016_brilliant_scientist_idea_icons.gfx` wiring maps every one of the 28 visible KRG idea IDs to a unique `GFX_idea_brilliant_scientist_*` sprite. No icon is a resized substitute for another surface, and no model or fallback asset is used.

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

Every final audio package needs source URL, author or performer, work and recording identity, rights evidence, access date, duration, source file, final WAV, proposed live identifier, sound definition, volume behavior, settings-aware playback, and documentation. No generic or shared fallback track is authorized.

## Open gates and deferred scope

- The local Event 016 evidence workspace was compacted on 2026-08-26. Approximately 3.15 GB across 4,248 files was reduced to 2,014,398,979 bytes across 4,022 files by removing only ignored failed, rejected, superseded, temporary, and exact-duplicate generation binaries. Accepted source art, runtime-facing packages, Meshy neutral lineage, actual-byte reimports, Quaternius evidence, hashes, licences, manifests, and provenance were retained; the detailed inventory and deletion record is `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_asset_workspace_cleanup_2026-08-26.md`. The workspace remains intentionally retained because the event package is still incomplete.
- The KRG biological stockpile and delivery design remains queued and blocked until the native CBRN raid system exposes a stable idempotent reservation, outcome, cancellation, and expiry callback. No Event 016 fallback or parallel ledger is authorized.
- Quantitative balance, targeted transfer and cleanup scenarios, and user-owned live state-selection, GUI interaction, audio, and super-event playback acceptance remain unrecorded.
- The durable portrait source queue under `docs/assets/portraits/016_brilliant_scientist/` currently has fifteen tracked PNG deletions in the working tree while the runtime leader DDS files and active processed portrait package remain present. Queue ownership or restoration is unresolved and must not be inferred from the runtime DDS status.
- The reusable Alien Infantry 3D entity is in the accepted D’Rhondan scope and remains a completion blocker pending approved failure recovery. The remaining project-force 3D packages stay queued under `docs/plans/016_brilliant_scientist_plans/016_event19_generic_unit_family_3d_model_backlog.md` and are outside this D’Rhondan tranche.
- Broader country-specific chains and additional project-specific presentation expansion beyond the twenty-five registered report cards are closed or rejected as filler under `docs/plans/016_brilliant_scientist_plans/016_nonmodel_content_closure_handoff_2026-08-03.md`. The seven public-milestone news images and the breakthrough, incident/security, and aftermath report cards are present and wired under `report_news_expansion/`.
- External redistribution rights for the copied stage-0 base remain unresolved. Internal Event 016 use is explicitly user-authorized.

## 2026-07-24 report and super-event image tranche

All rows in this tranche use source mode `$imagegen` for fictional alternate-history period documentary art. Report rows received the repository report-card processor and super-event rows received deterministic cover crop and resize. Full prompts and reference provenance are recorded in `docs/assets/016_brilliant_scientist/prompts/016_reports_and_super_event_prompts.md`. Row-level hashes, dimensions, alpha, DDS header, and exact-length checks are in `docs/assets/016_brilliant_scientist/validation/016_reports_and_super_technical_validation.md`. Source, processed, and decoded-DDS contact sheets are in `docs/assets/016_brilliant_scientist/contact_sheets/`.

Current-runtime reconciliation: the historical `parent wiring pending` status cells in the production handoff tables below are superseded. All twenty-five report sprites are registered and consumed by Event 016 events. All six super-event sprites, localisation blocks, sound variants, settings selectors, and trigger helpers are wired.

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

## Kruger State decision and decision-category icon package

Date: 2026-07-24

The current eight KRG decision files parse to exactly 130 decision or mission IDs. This package provides exactly 40 distinct decision-family icons at `32x32` and exactly 10 distinct category icons at the verified vanilla `50x40` category size. All 50 rows have retained ImageGen source masters, alpha/keyed evidence, processed PNGs, one-level uncompressed BGRA DDS files, contact-sheet review evidence, hashes, and manifest records.

| Family | Source and processed evidence | Runtime DDS folder | Sprite prefix | Coverage |
| --- | --- | --- | --- | ---: |
| Decision icons | `source_png/decision_icons/`, `alpha_png/decision_icons/`, `processed_png/decision_icons/` | `gfx/interface/decisions/016_brilliant_scientist/decisions/` | `GFX_decision_brilliant_scientist_krg_` | 40 |
| Decision-category icons | `source_png/decision_categories/`, `alpha_png/decision_categories/`, `processed_png/decision_categories/` | `gfx/interface/decisions/016_brilliant_scientist/categories/` | `GFX_decision_category_brilliant_scientist_krg_` | 10 |

The 130-row semantic decision assignment ledger is `package_records/decision_assignment_ledger.tsv`; the 10-row category ledger is `package_records/decision_category_assignment_ledger.tsv`. The machine-readable asset manifest is `package_records/decision_category_icon_manifest.json`. Prompt and provenance details are in `prompts/decision_category_icon_generation_record.md`. Technical validation is in `validation/decision_category_icon_validation_detailed.tsv` and is generated by `package_records/validate_decision_category_icons.py`; it checks dimensions, alpha and corners, DDS header/masks/caps/length, decoded pixel identity, source uniqueness, assignment completeness, and orphan sprites.

Parent-owned `.gfx` wiring is documented in `gfx_handoff.md` and the bounded handoff under `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_decision_category_icon_asset_handoff.md`.
