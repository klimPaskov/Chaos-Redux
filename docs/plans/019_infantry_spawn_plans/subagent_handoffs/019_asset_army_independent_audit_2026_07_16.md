# Event 019 asset and army-scene independent audit

Date: 2026-07-16

Mode: independent read-only audit of gameplay and asset surfaces. This handoff is the only file written by the auditor.

Skills applied: `chaos-redux-event-assets`, `chaos-redux-frame-animation`, and `chaos-redux-subagents`.

## Verdict

Event 019 is **not visually complete against the current no-focal-person-anywhere constraint**. The required 27 fixed portrait-slot images themselves pass: all twenty claimant slots are distinct regional army/muster formations, all six derivative slots are massed fantastical hosts or councils-as-formations, and the neutral slot is an anonymous massed muster. However, several other live Event 019 asset families still place individual people in the focal foreground, including one of the eleven achievement icons.

No identifiable woman was found in the reviewed Event 019 contact sheets. The claimant and derivative character creation also retains male metadata. The technical word `portrait` is confined to engine-facing filenames, sprite/function/widget identifiers, and compatibility explanations; no player-facing Event 019 localisation value uses `portrait`, `woman`, `women`, or `female`.

Open findings: one P0 visual-contract blocker, one P1 source-policy blocker, and one P2 metadata/provenance issue. The achievement `.gfx` gap found during this audit was closed and narrowly reverified before handoff.

## Findings

### P0 - Open: live non-slot assets violate the explicit no-focal-human/person-anywhere rule

The fixed 27-slot army/host package is compliant, but the wider Event 019 asset package is not:

- `docs/assets/019_infantry_spawn/source_png/achievements/019_infantry_spawn_one_battalion_wonder_source.png` is constructed around one large, centered soldier holding a flag and rifle. The same focal soldier survives in `processed_png/achievements/019_infantry_spawn_one_battalion_wonder.png` and all three runtime achievement states, including `gfx/achievements/019_infantry_spawn_one_battalion_wonder.dds`.
- `contact_sheets/event_019_decision_icon_contact_sheet.png` shows `claimant_recognize` as a portrait-like individual officer and `claimant_accept` as a focal human arm/hand.
- `contact_sheets/event_019_focus_icon_contact_sheet.png` shows `crown_the_claimant` as a head-and-shoulders individual officer. Other focus icons use focal hands or foreground people even when the wider composition contains a host.
- `contact_sheets/event_019_report_source_contact_sheet.png` and `event_019_report_processed_contact_sheet.png` retain foreground individuals. The clearest examples are `report_event_019_infantry_spawn_claimant` (one lone man dominates the frame), `report_event_019_infantry_spawn_anomalous` (one armed man dominates the foreground), and `report_event_019_infantry_spawn_golem_release` (one running man dominates the lower foreground). The manifestation/organized/ghost/golem report families also contain prominent foreground people.

This is a direct current-user constraint failure, not an inference from filenames. I inspected the source and processed contact sheets at original detail with `view_image`, then opened the one-battalion source and final-size PNG separately. Replacing only the 27 fixed slots cannot close the package while these live assets remain.

Recommended closure: regenerate or source formation-, object-, archive-, or symbol-led replacements for every Event 019 panel with a focal person, preserve the existing runtime identifiers, rebuild corresponding PNG/DDS states, refresh contact sheets and provenance, and rerun a full-package visual pass. No fallback substitution is authorized.

### P1 - Open: the 91 regional flags do not satisfy the skill's per-design ImageGen-source rule

The regional flag files are technically sound, but their documented source model does not match the required generated-flag workflow:

- `chaos-redux-event-assets/SKILL.md:874` requires a separate `$imagegen` result for each visually distinct fictional or alternate-history flag design.
- `docs/assets/019_infantry_spawn/notes/regional_flag_generation_provenance_2026_07_16.md:63`-`73` records thirteen existing identity designs, only seven new regional-motif ImageGen calls, and deterministic local compositing of every motif onto every identity.
- The result is 91 distinct regional flags derived from 20 authored inputs rather than 91 separately generated flag designs.

The compositor does preserve authored geometry and does not locally draw primitives, so this is not a pixel-quality or runtime-file failure. It is nevertheless an explicit source-policy and completion-proof failure. The 91 high-resolution composites are processing outputs, not separate ImageGen generations.

Recommended closure: obtain one retained ImageGen source result for each of the 91 visually distinct regional designs, process each through the normal/medium/small ladder, preserve the 91 runtime tag names, and refresh the provenance, checksums, contact sheets, and validation JSON. Do not present the current composites as equivalent source evidence.

### P1 - Closed during audit: Event 019 achievement sprite aliases were absent

Initial evidence:

- The eleven achievement definitions and all 33 DDS files existed, but `interface/` contained zero `GFX_achievement_019_infantry_spawn_*` aliases or Event 019 achievement texture paths.
- `chaos-redux-event-assets/SKILL.md:842` explicitly requires `interface/chaosx_achievements.gfx` alignment when achievement IDs are added.
- Event 017 and Event 018 immediately preceding the insertion point each register completed, grey, and not-eligible triplets.
- The former `manifest.md:14` and `gfx_handoff.md:259` incorrectly claimed that `.gfx` registration was unnecessary.

Parent remediation was applied before handoff. Narrow recheck result:

- 33 Event 019 `spriteType` aliases now exist in `interface/chaosx_achievements.gfx`.
- All 33 names are unique and all 33 texture paths exist.
- The false no-`.gfx` claims are absent from both `manifest.md` and `gfx_handoff.md`; each now points to `interface/chaosx_achievements.gfx`.

Status: closed; do not count this as a remaining blocker.

### P2 - Open: the manifest still cites removed project-reference folders

`docs/assets/019_infantry_spawn/manifest.md:9` says the package inspected `.agents/skills/chaos-redux-event-assets/assets/{report_event,decisions,ideas,focuses,achievements,flags}`. All six cited directories are absent. Current references live under `assets/vanilla_reference/` and are routed through the skill catalog.

This does not alter runtime pixels, but it weakens reproducibility and makes the reference record factually stale. Replace the brace-expanded paths with the exact existing catalog/reference paths actually inspected.

## Required fixed-slot audit

### Visual result

I inspected these contact sheets at original detail:

- `event_019_claimant_source_contact_sheet.png`
- `event_019_claimant_processed_contact_sheet.png`
- `event_019_derivative_portrait_source_contact_sheet.png`
- `event_019_derivative_portrait_processed_contact_sheet.png`
- `event_019_unassigned_muster_source_contact_sheet.png`
- `event_019_unassigned_muster_processed_contact_sheet.png`

Results:

- 20/20 claimant slots read as distinctive regional armies or musters: railhead, frozen bridgehead, oasis ring, monsoon port, horse-artillery arrowhead, floodplain crossing, forest echelons, highland pack artillery, industrial tram-square, winter industrial grid, plateau defence, amphibious wave, coastal batteries, machineworks blocks, savanna mobile echelon, desert crescent, bicycle host, ski envelopment, delta defence, and outback motor host.
- 6/6 derivative slots read as massed fantastical formations: zombie wall, three-host zombie council, spectral spearhead, three-host spectral council, quarry golem host, and three-cohort golem council.
- 1/1 neutral slot reads as an anonymous radial-and-column muster without a flag, emblem, claimant, landmark, or regional terrain.
- 0/27 has an individual focal human/person. No identifiable woman appears.

### Independent file result

- Source PNGs: 27 present, 27 unique SHA-256 hashes.
- Processed PNGs: 27 present, 27 unique hashes, all exactly 156x210.
- Runtime DDS: 27 present, 27 unique hashes, all exactly 156x210 and 131168 bytes.
- All 27 DDS files use the expected legacy uncompressed 32-bit BGRA masks and decode pixel-for-pixel equal to their paired processed PNG.
- The 27-row source -> processed -> DDS -> sprite crosswalk in `notes/claimant_portrait_asset_crosswalk_2026_07_16.md` has zero path, dimension, or hash mismatches.
- `interface/019_infantry_spawn.gfx:51`-`156` registers all twenty claimant, one neutral, and six derivative slots exactly once.
- Every registered slot has at least one non-definition consumer. Claimants are selected by `GetInfantrySpawnClaimantPortraitSprite` and the Muster Board property at `common/scripted_guis/019_infantry_spawn_muster_board_scripted_gui.txt:231`; derivatives are used by country-leader creation and scenario/event picture selection; the neutral muster is the scripted-localisation terminal default and Event 019 evolution-log image.
- Claimant creation uses the dynamic selected sprite at `common/scripted_effects/019_infantry_spawn_claimant_identity_effects.txt:198`-`210` with `female = no`; derivative leader creation uses the six host/council sprites with `female = no` at `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:387`-`445`.

## Real-frame animation audit

All three requested animations pass the frame-animation contract:

| Package | Source frames | Processed frames | Frame size | Sheet size | FPS | Result |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| `muster_seal_pulse` | 8/8 unique | 8/8 unique | 64x64 | 512x64 | 8 | pass |
| `critical_command_border` | 8/8 unique | 8/8 unique | 156x210 | 1248x210 | 6 | pass |
| `anomalous_registry_emblem` | 10/10 unique | 10/10 unique | 64x64 | 640x64 | 5 | pass |

Evidence:

- The three frozen source atlases and processed contact sheets visibly contain authored crack, relief, seam, fold, aperture, clamp, and highlight changes. They are not translated, scaled, rotated, recoloured, blurred, or filtered copies of one still.
- Each package contains source frames, processed frames, a horizontal PNG sheet, static PNG, GIF preview, contact sheet, brief, and frame plan with per-frame hashes.
- All 26 source frames and all 26 processed frames are package-locally hash-unique.
- Each static PNG is byte/pixel-equivalent to processed frame `000`; each sheet begins with that same frame.
- The three sheet DDS and three static DDS files have the declared dimensions, valid BGRA headers, and decoded-pixel equality with their PNG masters.
- `interface/019_infantry_spawn.gfx:162`-`203` registers the 8/8/10 frame counts and 8/6/5 FPS values plus three static fallbacks.
- `interface/019_infantry_spawn_muster_board.gui:33`-`61` consumes all six sprites. `common/scripted_guis/019_infantry_spawn_muster_board_scripted_gui.txt:137`-`154` makes the animated and static versions mutually exclusive under the animation-disable flag and retains the critical/anomalous state gates.

## Achievement triplet audit

Technical package result after parent remediation:

- 11 separate source PNGs.
- 33 processed PNGs and 33 runtime DDS files: completed, grey, and not-eligible for every ID.
- All images are 64x64; each state family has 11 unique hashes.
- All grey variants are true grayscale. All not-eligible variants retain the red-X state visible in the contact sheet.
- All 33 DDS files have valid uncompressed BGRA headers and decode pixel-for-pixel equal to the paired PNG.
- `common/achievements/chaos_redux_achievements.txt` contains 11 Event 019 definitions.
- `localisation/english/chaosx_achievements_l_english.yml` contains all 22 required `_NAME`/`_DESC` keys.
- `interface/chaosx_achievements.gfx` now contains all 33 unique aliases with no missing texture path.

Visual-contract exception: `one_battalion_wonder` is technically valid but remains part of the open P0 because its composition is dominated by a lone soldier.

## Flag audit

Runtime and visual results:

- Thirteen unsuffixed compatibility identities and 91 regional identities exist at each tier: 104 normal, 104 medium, and 104 small TGAs (312 total).
- Required dimensions are exact: 82x52 normal, 41x26 medium, and 10x7 small.
- All 104 files are hash-unique within each tier; all 91 regional files are independently unique within each tier.
- All files are uncompressed type-2, 32-bit, bottom-left-origin TGA. The thirteen legacy compatibility files per tier include a valid 26-byte `TRUEVISION-XFILE` footer; the 91 regional files use exact header-plus-pixel length.
- Every TGA decodes pixel-for-pixel equal to its paired processed PNG.
- All 91 regional tags have `TAG`, `TAG_DEF`, `TAG_ADJ`, and ideology aliases in Event 019 localisation.
- `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:222` builds the exact `INFANTRY_SPAWN_[IDENTITY]_[REGION]` token used by the 91 regional filenames.
- Original-detail review of the base, 13x7 regional, small-readability, and motif-source contact sheets shows legible identity and regional marks at each tier.

Runtime validation passes. Source-policy validation fails for the reason recorded under the open P1.

## References and method

Before examining repo assets I read `AGENTS.md`, all three selected skills, the required offline wiki core pages, Graphical Asset Modding, Interface Modding, Scripted GUI Modding, and Character Modding. I also consulted vanilla `documentation/script_concept_documentation.md`, `interface/alerts.gfx`, character portrait definitions, `common/achievements.txt`, `interface/achievements.gfx`, and vanilla achievement triplets.

Technical checks were independent read-only Python/Pillow/hash/header audits; no package processor was run in a write mode. Visual conclusions came from direct original-detail `view_image` inspection of the fixed-slot, animation, achievement, flag, decision, focus, idea, UI, GUI-background, and report-event contact sheets.

## Ownership and remaining risks

- Auditor changed only this handoff.
- Parent changed the achievement registry and associated documentation during the audit; that narrow change was rechecked and is closed above.
- P0 and regional-flag P1 remain open. Event 019 should not receive a complete/no-simplifications asset claim until both are resolved and visually re-audited.

