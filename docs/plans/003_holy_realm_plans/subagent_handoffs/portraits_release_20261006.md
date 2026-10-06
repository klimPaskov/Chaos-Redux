# Event003 portrait release handoff

Date: 2026-10-06. Owner: `chaosx_portrait_creator`. Scope: the ten active static portrait DDS files and two active portrait animation DDS files under `gfx/leaders/003_holy_realm/`. The inactive `portrait_THR_final_silence.dds` is explicitly excluded. No GFX, character, scripted effect, scripted localization, GUI, event, focus, gameplay, country, or spreadsheet files were changed. Per the parent's final instruction, the exact owned release set of 147 paths was force-added to the Git index; no commit was created.

## Status

The fictional-supernatural art package is installed: original ImageGen outputs, exact prompts and tool receipts, processed 156x210 static PNGs, eight authored source frames per animation, 2496x210 sheets, GIF review previews, native and 4x contacts, candidate DDS files, and verification evidence are archived at `docs/assets/portraits/003_holy_realm/release_20261006/`. The parent accepted the whole twelve-DDS package on 2026-10-06, and those exact candidate bytes were copied to their stable runtime paths. The replaced legacy files remain preserved as unverified originals.

The force-added set contains the 134 files in the unique portrait release archive, the twelve installed runtime DDS files listed below, and this handoff. No unrelated staged or unstaged work was added to the selection.

The parent first accepted Godly Figure v1 and Refuge Bodhisattva v1 as original identity/style seeds. After review of all ten static native/4x crops and all sixteen playback positions for each animation at native/4x size, the parent accepted the full package for installation on 2026-10-06. The review and acceptance are recorded in `notes/candidate_review_log.md`.

## Owned runtime file list

The accepted candidate files in `candidate_dds/` were installed by identical basename at these exact active paths:

| Runtime path | Target size |
| --- | --- |
| `gfx/leaders/003_holy_realm/portrait_THR_godly_figure.dds` | 156x210 |
| `gfx/leaders/003_holy_realm/portrait_THR_refuge_bodhisattva.dds` | 156x210 |
| `gfx/leaders/003_holy_realm/portrait_THR_bodhisattva_pramudita.dds` | 156x210 |
| `gfx/leaders/003_holy_realm/portrait_THR_bodhisattva_acala.dds` | 156x210 |
| `gfx/leaders/003_holy_realm/portrait_THR_bodhisattva_dharmamegha.dds` | 156x210 |
| `gfx/leaders/003_holy_realm/portrait_THR_arhat_administration.dds` | 156x210 |
| `gfx/leaders/003_holy_realm/portrait_THR_buddha_mandate.dds` | 156x210 |
| `gfx/leaders/003_holy_realm/portrait_THR_divine_sovereignty.dds` | 156x210 |
| `gfx/leaders/003_holy_realm/portrait_THR_false_buddha.dds` | 156x210 |
| `gfx/leaders/003_holy_realm/portrait_THR_empty_seat.dds` | 156x210 |
| `gfx/leaders/003_holy_realm/portrait_THR_buddha_mandate_animated.dds` | 2496x210, sixteen 156x210 frames |
| `gfx/leaders/003_holy_realm/portrait_THR_empty_seat_animated.dds` | 2496x210, sixteen 156x210 frames |

All registered sprite names and consumers remain stable in `interface/chaosx_characters.gfx`, `common/scripted_effects/003_holy_realm_effects.txt`, and `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`. No `.gfx` or character reference edit is necessary.

## Source mode and art evidence

The active consumers create an anonymous leader named “The Bodhisattva”; none names a historical person. The parent explicitly authorized one unnamed fictional supernatural incarnation and its stages, excluding Siddhartha Gautama, Padmasambhava, any other historical or living person, and sourced religious-painting identity. The source classification is therefore `fictional_high_chaos`, using native ImageGen. No RunPod or grounded source-placeholder workflow applies.

The first Godly Figure generation used the installed vanilla `Portrait_USA_Generic_land_4.dds` only as a painterly finish and framing reference. The face, clothing, symbols, and background were excluded. `portrait_SOV_supreme_soviet.dds` was also inspected as a full-canvas leader/council composition comparison. The backdrop reference contact sheet was inspected only after those installed vanilla references and was not attached to ImageGen or used as portrait pixels. Research for robe construction and the Acala ritual prop is documented in `notes/prop_research.md`; its pages did not supply a portrait identity or image input.

All ten static source PNGs and fourteen generated animation-frame PNGs are preserved under `source_png/`; the two `000` animation seed sources are exact copies of the two static sources used as frame zero. Prompts, input roles, exact tool output paths, and the connected tool's absent model selector are in `notes/native_imagegen_receipts.md`. Candidate preview links are in `preview_index.md`.

## Validation evidence

The all-static native and 4x contacts are `contact_sheets/portrait_THR_static_candidate_contact_native.png` and `contact_sheets/portrait_THR_static_candidate_contact_4x.png`. Each animation has a native and 4x contact covering all sixteen playback positions. Each loop has eight separately authored states followed by the same states in reverse; the frame sheets contain no transform-generated motion. The 4 fps playback order, frame notes, per-frame source and processed hashes, and native-size differences are in the animation briefs, frame plans, and frame-validation JSON files.

The required repository converter produced ten 156x210 candidate DDS files of 131,168 bytes and two 2496x210 animation DDS files of 2,096,768 bytes. Every candidate passed one-level legacy BGRA header checks, has alpha extrema 255–255, and decodes pixel-identically to its processed PNG source. The twelve active runtime DDS files now match the accepted candidate bytes exactly and also decode pixel-identically to those PNG sources. Full candidate and installed runtime hashes are in `notes/candidate_dds_validation.json` and `notes/runtime_installation_validation.json`; static source and processed hashes are in `notes/static_asset_inventory.json`.

Before candidate creation, all twelve active legacy DDS files were copied under `legacy_unverified/`. Their SHA-256 hashes matched the then-current runtime bytes; the 12-file snapshot is in `notes/legacy_runtime_baseline.json`. The unused final-silence DDS was not copied or changed.

## Review and remaining work

Portrait art was visually reviewed at full source resolution and native 156x210 size by the producer and at native/4x contact scale by the parent. Parent acceptance covers all ten static portraits, all eight authored poses in each animation, both mirrored 16-position loops, and installation at the twelve stable DDS paths. Current runtime hashes match candidate hashes, and runtime DDS round trips match their processed PNGs.

No live-game portrait render was performed; the user owns live-game validation. There is no source-placeholder branch, user-supplied HOI4-style final, GFX edit, animation frame fallback, or source substitution in this fictional workflow. The sole animation frame-count reduction is the parent-authorized eight-authored-pose mirrored loop, which preserves the existing sixteen playback positions.
