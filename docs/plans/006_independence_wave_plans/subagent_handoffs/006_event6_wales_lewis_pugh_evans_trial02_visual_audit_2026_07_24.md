# Event 006 IW-002 Wales Lewis Pugh Evans trial 02 visual audit

Audit date: 2026-07-24.

Auditor: independent Chaos Redux country-package subagent.

Scope: read-only audit of the immutable Evans source master and explicit crop, trial 02 raw ImageGen repaint, deterministic `156x210` candidate, commander-family references, provenance and ownership evidence, stable WLS consumer, and current runtime surface.

No source, crop, raw ImageGen result, processed PNG, DDS, GFX, gameplay, character, history, localisation, advisor, dossier, `_small`, alternate, generic, female, navy, or fallback file was changed.

## Verdict

**FAIL closed — `blocked`; do not convert to DDS or wire.**

Trial 02 correctly uses only the archival Evans crop as the ImageGen identity input and records the corrected deterministic `--role-family commander` processor with Montgomery and Witzleben commander references.

The raw repaint and processed candidate nevertheless retain material identity drift at native size and at least `4x` nearest-neighbour enlargement, so the non-compensable likeness gate fails even though the commander style gate passes.

## Gate checklist

| Gate | Verdict | Evidence and finding |
|---|---|---|
| Provenance and rights | **PASS with caveat** | The immutable IWM `HU 93411` master and direct crop are retained, hash-verified, and byte-identical to the source package. The source records Wikimedia Commons Public Domain/Public Domain Mark treatment, IWM/Barnett attribution, and the remaining Crown-copyright/non-commercial territorial caveat; retain the credit and re-check target-territory treatment before release. |
| Male-only compliance | **PASS** | The archival master, crop, raw repaint, and `156x210` candidate each show one male-presenting subject only. No female, second person, advisor, dossier, institutional-body, or alternate portrait appears. |
| Historical and role fit | **PASS with wording caveat** | Lewis Pugh Evans was Welsh-born and commanded the 159th Welsh Border Infantry Brigade from 1933 through January 1938, so he was alive and in a Welsh formation command at the 1936 start. `mountain_frontier` is a package terrain and territorial-defence abstraction, not evidence of specialist mountain-branch service. |
| Explicit archival head-and-shoulders crop | **PASS** | `source_crops/WLS_lewis_pugh_evans_iwm_hu93411_head_shoulders.png` is the direct `(95,25)-(540,505)` source-pixel crop with cap, unobstructed face, neck, both shoulders, collar, and upper tunic. |
| Identity and likeness preservation | **FAIL** | The raw repaint and candidate open and brighten the source's small tired asymmetric eyes, regularise unequal ear exposure, shorten and round the long narrow nose, thicken and widen the pencil moustache, broaden and soften the long lean face and pointed chin, reduce source age lines, and move the wary off-centre gaze toward a brighter direct neutral expression. These changes remain visible in the candidate at native `156x210`; style cannot compensate. |
| HOI4 painted commander style | **PASS** | The raw repaint and candidate are subdued hand-painted military portraits with a quiet dark vignette, restrained khaki-brown palette, readable face, no text, watermark, modern prop, or meme treatment. `processing_metadata.json` records `role_family: commander`, the canonical commander directory, and Montgomery/Witzleben style references. |
| Head-and-shoulders framing | **PASS** | The candidate is exactly `156x210`, retains the full cap with top margin, neck, both shoulders, and upper field tunic, and has no frame or dossier border. |
| Portrait ownership | **PASS** | Exact and variant Evans searches found no active person, character, recruitment, portrait, GFX, or localisation owner in current Chaos Redux, installed vanilla, or approved reference mods. The rejected Thomas Wynford Rees material remains disclosure-only and is not reused. |
| Stable WLS consumer | **PASS for declaration** | `WLS_independence_wave_mountain_commandant` is generated as a male corps commander in `common/scripted_effects/006_independence_wave_scotland_wales_package_effects.txt:276-300`; `GFX_portrait_WLS_independence_wave_mountain_commandant` is declared at `interface/006_independence_wave_region_01_portraits.gfx:66-69` and assigned to civilian and army `large` only. The display localisation remains the generic `Mountain Commandant`, a downstream naming/identity risk that this visual audit does not edit. |
| Advisor, dossier, `_small`, and fallback absence | **PASS** | Trial 02 contains no advisor, dossier, `_small`, female, alternate, generic, navy, or fallback derivative. The current WLS declaration has no `_small` sprite or consumer. |
| Runtime readiness | **BLOCKED** | Trial 02 has no DDS by design and the failed likeness gate forbids conversion or wiring. The legacy `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_mountain_commandant.dds` is a valid `156x210` BGRA texture but decodes to an unrelated dark-haired man and must not be counted as Evans approval or used as a fallback. |

## Visual comparison record

I inspected the unchanged archival master, explicit crop, raw ImageGen result, processed candidate, and both commander references separately at native resolution and at `4x` nearest-neighbour enlargement.

The disposable enlarged inspection files were generated only under `%TEMP%\\wls_evans_trial02_audit_20260724` and were not added to the repository or used as runtime art.

The source master shows small deep-set eyes with unequal lids, unequal ear exposure, a long straight narrow nose, a short thin pencil moustache, hollow cheeks, a long lean face with a pointed chin, visible forehead and under-eye age lines, and a restrained slightly off-centre wary gaze.

The raw repaint remains a plausible commander-family portrait, but its eye openings and catchlights are brighter and more uniform, its ears read more evenly exposed, its nose and moustache are fuller, its cheek and jaw planes are softer, and its expression is more direct and neutral than the source.

The deterministic candidate preserves the raw repaint's identity drift rather than correcting it, and the differences remain legible at the native game canvas.

The retained review sheet `review/WLS_lewis_pugh_evans_commander_style_sheet.png` correctly uses the commander family and shows the processor input crop, processed candidate, `eng_bernard_montgomery.png`, and `ger_erwin_von_witzleben.png`; its first panel is not the archival crop and does not replace the independent provenance comparison.

## Evidence hashes and dimensions

| Evidence | Dimensions and mode | SHA-256 |
|---|---:|---|
| `source_masters/WLS_lewis_pugh_evans_iwm_hu93411_c1918.jpg` | `605x800` RGB | `FDFDE87660F50EB9A2112186878FB8EE93B7C1F0E2CB9F533CA9B2C41C26012C` |
| `source_crops/WLS_lewis_pugh_evans_iwm_hu93411_head_shoulders.png` | `445x480` RGB | `B16812C1B58AF568EAC7E74EC64E592CC34DD793CC2DB3A8D261D85168A2C064` |
| `imagegen_results/WLS_lewis_pugh_evans_identity_preserve_trial_02.png` | `1208x1302` RGB | `5F61603CCEA5C3BF302DDC2D37184654CBDB14573D0A080D8E9EE3D0789B45D2` |
| `processed_png/portrait_WLS_independence_wave_mountain_commandant.png` | `156x210` RGBA, opaque alpha | `3758F42C8E0C2A8DA2AEC8BF097C69C22DB2388C46D12EEB24C9260DC2D2EE44` |
| `review/WLS_lewis_pugh_evans_commander_style_sheet.png` | `1344x464` RGBA | `8F008E7E0322C078F41122C72071DA4BB6E9757D4D26FB7CF39C05C5219426D3` |
| Commander reference `eng_bernard_montgomery.png` | `156x210` RGBA | `39B03871D7451CA96712A5CCF3C056528693F82642776E6C5E297E041943944E` |
| Commander reference `ger_erwin_von_witzleben.png` | `156x210` RGBA | `10F4A1108F9D440213F70FB5802349A2291F298F9D132644241119561577D5B6` |

All entries in trial 02 `hashes.sha256` match current bytes, and the trial master and crop are byte-identical to the source-package copies.

`processing_metadata.json` records processor `the retired portrait-processing utility` version `5.0`, `mode: leader` for the backward-compatible full-size export, `role_family: commander`, commander reference directory, normalized commander references, and output size `156x210`.

## Country-package and runtime surface boundary

The only live gameplay consumer inspected was the stable WLS character and portrait declaration listed above.

No tag registration, state ownership, map, politics, party, focus, decision, idea, advisor, military, technology, industry, supply, production, AI, or localisation surface was changed by this portrait audit.

The current generic display key `WLS_independence_wave_mountain_commandant: "Mountain Commandant"` should be reviewed separately if the parent intends the sourced Evans identity to appear by name; it does not waive the failed likeness gate.

## Changed files

- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_24/wales_lewis_pugh_evans_trial_02/manifest.md`: changed only the status from `candidate_pending_independent_audit` to `blocked` and added the failed independent-audit verdict.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_wales_lewis_pugh_evans_trial02_visual_audit_2026_07_24.md`: added this handoff.

No source, process, image, DDS, GFX, gameplay, localisation, character, history, advisor, dossier, `_small`, alternate, generic, female, navy, or fallback file was changed.

## Validation and skipped checks

Meaningful validation included SHA-256 and dimension/mode checks for the source master, crop, raw result, processed candidate, style sheet, and role-specific references; trial/source master and crop byte equality; exact and variant ownership searches across current Chaos Redux, installed vanilla, and approved reference mods; stable WLS consumer and absence of live `_small` registration searches; and read-only legacy DDS header/decode inspection.

The legacy DDS is `131168` bytes with valid one-level BGRA header dimensions `156x210`, but its decoded subject is unrelated to Evans and it remains an unapproved stale runtime asset.

DDS conversion, runtime wiring, gameplay load testing, and any source or processing rerun were skipped because the likeness gate fails and the task explicitly forbids runtime advancement for a blocked candidate.

## Remaining blockers and next step

A future trial must preserve the source eye-lid asymmetry and tired gaze, unequal ear exposure, long narrow nose, thin pencil moustache, lean cheek and jaw planes, pointed chin, source age texture, head angle, and wary expression while retaining the commander-family painted finish.

Do not use the legacy runtime DDS as a fallback, and do not create advisor, dossier, `_small`, female, generic, alternate, or navy derivatives.

Final disposition: **`blocked` / `FAIL`; no runtime advancement.**
