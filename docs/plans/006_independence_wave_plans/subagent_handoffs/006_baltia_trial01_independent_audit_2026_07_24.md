# Event 006 AFX Wallonia Herman Baltia trial 01 independent portrait audit

Date: 2026-07-24  
Reviewer: independent sourced-visual audit subagent  
Package: `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_24/wallonia_herman_baltia_trial_01/`  
Disposition: **rejected and unwired; do not convert to DDS or wire at runtime**.

I audited the unchanged archival master, explicit crop, raw ImageGen result, deterministic candidate, prompt, processing metadata, review sheet, and canonical commander references without producing or repainting any asset.

## Verdict summary

| Gate | Verdict | Evidence |
|---|---|---|
| Provenance and rights | **PASS** | `source_masters/AFX_herman_baltia_1909_master.jpg` is an unchanged `389 x 473` direct upload with SHA-256 `73597E416240754B2F5A9C78AAC4798287B58642F1ABD93C920F3020D95A1B66`; the recorded Commons page identifies Public Domain Mark 1.0 and `PD-old`; the source, crop, prompt, raw result, candidate, metadata, and review hashes match the package ledger. |
| Male-subject compliance | **PASS** | The master, crop, raw result, and processed PNG each show one male subject; `common/characters/006_independence_wave_wallonia_frisia_characters.txt:53-62` sets `gender = male` and only full `civilian.large` / `army.large` portrait slots for `AFX_walloon_reserve_commander`; no female metadata or opposite-gender name pool is involved. |
| Historical-role fit | **PASS** | Baltia's Arlon-based 10th Line command and the 1933 Chasseurs Ardennais lineage support the parent-approved alternate-history senior territorial/reserve abstraction; the source remains disclosed as a 1909 pre-war uniform and Baltia as retired at the 1936 start. |
| Explicit head-and-shoulders crop | **PASS** | Independent Pillow comparison proves `master.crop((20,12,373,473))` equals `source_crops/AFX_herman_baltia_1909_head_shoulders_crop.png` exactly at `353 x 461` with zero differing pixels. |
| Identity and likeness preservation | **FAIL (non-compensable)** | Native and disposable 4x nearest-neighbour review show regularized unequal deep-set eyes, broadened and softened long facial planes, a shorter/broader nose, changed asymmetric handlebar-moustache curls, a filled or altered receding wavy hairline, and a rounder jaw/chin than the archival crop. The candidate remains an officer-like face but does not preserve the source-visible identity geometry strictly enough for runtime. |
| HOI4 commander style | **PASS** | The `156 x 210` candidate is a restrained painterly commander portrait with modeled planes, muted period field-service tunic, quiet background, no raw-photo finish, and no text, watermark, UI, modern prop, emblem, or unsupported insignia; its dark brown grade remains readable and within the subdued commander family. |
| `156 x 210` framing | **PASS** | `processed_png/portrait_AFX_walloon_reserve_commander.png` decodes as opaque RGBA `156 x 210`, with one full head-and-shoulders subject, safe head and shoulder margins, and no frame or dossier treatment. |
| Ownership and stable-consumer fit | **FAIL (runtime transfer not cleared)** | Exact and variant searches for `Herman Baltia`, `Baltia Herman`, `Herman_Baltia`, `BEL_herman_baltia`, `General Baltia`, and `general_baltia` found no active person owner in current Chaos Redux, vanilla, or approved reference roots, but `history/countries/AFX - Wallonia.txt:18` recruits the existing `AFX_walloon_reserve_commander`, `interface/006_independence_wave_region_01_portraits.gfx:14-15` points its stable sprite to the existing DDS, and `localisation/english/006_independence_wave_wallonia_frisia_l_english.yml:4` still names that token `Marcel Delcourt`; no guarded identity-transfer contract is present in this trial. |
| Absence of advisor, dossier, and `_small` assets | **PASS** | The trial directory contains no advisor, high-command, operative, dossier, or `_small` file; the character definition uses only the existing full `civilian.large` and `army.large` slots. |

Identity and style were evaluated as independent gates. The style pass does not compensate for the failed identity gate or the uncleared player-facing name transfer, so the package remains export-only.

## Evidence and deterministic processing

The explicit crop is `source_crops/AFX_herman_baltia_1909_head_shoulders_crop.png` from source rectangle `(20,12,373,473)` with SHA-256 `442658EC257566827290B77D7D3B8E7AF208CF9A999FFC1086DD61BC059BCB59`.

The raw ImageGen result is `imagegen_results/AFX_herman_baltia_identity_preserve_trial_01.png` at `1098 x 1433` with SHA-256 `EBC8CAADC8F4438B50D6A444136EC0D5235A57C153C7D9317938CE32FA2E10A0`.

The prompt is `identity_repaint_prompt.md` with SHA-256 `68710A71B2D3EEFE15AA38B7DF0B7220B2BDF0CA106FD12503B32D85A4466B2A`.

The deterministic processor is `.agents/skills/chaos-redux-event-assets/tools/advisor_icon_processing.py` version 5.0 with SHA-256 `1ADB521B43238EE971E093DAE90007C4C44C600435EBB897C6482BA3B64B96EC`, positional mode `leader`, role family `commander`, and recorded Python `3.9.12` / Pillow `11.1.0` runtime.

The processed candidate is `processed_png/portrait_AFX_walloon_reserve_commander.png` at `156 x 210` with SHA-256 `A0ABD0E129F150F534B024C06FFB66D14D8E4DFDC86BDB581252588D769244A7`.

The processor metadata is `processing_metadata.json` with SHA-256 `D367E37C34575856E4F1F147EF8BEEA9729024ECB6404F9A0E391D415D78E4B4`.

The review sheet is `review/AFX_herman_baltia_commander_style_sheet.png` at `1344 x 464` with SHA-256 `5C840F3C55000CEEE680D3EDEA39E35163031439FB85F593020EED3D1A28423B`.

The processor selected the commander references `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/commanders/eng_bernard_montgomery.png` with SHA-256 `39B03871D7451CA96712A5CCF3C056528693F82642776E6C5E297E041943944E` and `ger_erwin_von_witzleben.png` with SHA-256 `10F4A1108F9D440213F70FB5802349A2291F298F9D132644241119561577D5B6`.

All eight entries in `hashes.sha256` matched on audit, and the processor hash plus metadata-recorded candidate/review hashes matched the files on disk.

The processor sheet is a 2x full-size style sheet, and its first panel is the processor input crop of the raw ImageGen result rather than the immutable archival crop; I therefore compared the archival master, exact crop, raw result, processed candidate, and role references separately.

I also inspected disposable normalized nearest-neighbour 4x enlargements outside the repository and removed them after review; no audit image was added to the trial or used as a runtime asset.

## Identity defects requiring a source-only retry

The retry must use the unchanged `source_masters/AFX_herman_baltia_1909_master.jpg` and exact crop as the only identity authority and must not use this failed repaint as an identity reference.

The retry must preserve the narrow forehead, receding wavy side-parted hair, long lean face, unequal deep-set eyes and heavy lids, long straight narrow nose, asymmetric upward-curled handlebar moustache, unequal ears, long jaw and rounded-pointed chin, stern reserved expression, head angle, neck length, and shoulder slope visible in the immutable crop.

The retry may keep the plain symbol-free Belgian field-service tunic and subdued commander painting direction, but it must not beautify, widen, symmetrize, open the eyes, fill the hairline, shorten the nose, regularize the moustache, round the jaw, invent hidden detail, or substitute a generic officer face.

Before any future conversion, the parent must also change the player-facing `AFX_walloon_reserve_commander` localisation from `Marcel Delcourt` to the accepted Baltia identity and explicitly record the guarded token transfer, then run a fresh independent identity, style, and consumer audit.

## Runtime and scope disposition

No DDS, GFX edit, gameplay edit, localisation edit, advisor asset, dossier card, `_small` derivative, or fallback was created by this audit.

The existing stale DDS at `gfx/leaders/006_independence_wave/portrait_AFX_walloon_reserve_commander.dds` is not this candidate and is not approved by this trial.

The trial manifest was updated to `rejected_identity_runtime_hold`, and no source or generated image was modified.

## Remaining risks

The source is rights-clear and role-defensible only under the explicit alternate-history retired-general abstraction; it must not be described as 1936 active Walloon command or as a 1936 uniform photograph.

The candidate's style is acceptable as a commander-family painting, but its identity drift is non-compensable and blocks any DDS or runtime use.

No fallback, generic person, opposite-gender pairing, advisor/dossier derivative, or unrelated consumer is authorized.
