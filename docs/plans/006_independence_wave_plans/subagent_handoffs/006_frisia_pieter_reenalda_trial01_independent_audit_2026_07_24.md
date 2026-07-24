# Event 006 AGX Frisia Pieter Reenalda trial 01 independent portrait audit

Date: 2026-07-24
Reviewer: independent sourced-visual audit subagent
Package: `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_24/frisia_pieter_reenalda_trial_01/`
Disposition: **rejected and unwired; do not convert to DDS or wire at runtime**.

I audited the unchanged archival master, explicit crop, raw ImageGen result, deterministic candidate, prompt, processing metadata, review sheet, commander references, and the active Frisia consumer surfaces without producing or repainting any asset.

## Verdict summary

| Gate | Verdict | Evidence |
|---|---|---|
| Provenance and rights | **PASS** | `source_masters/AGX_pieter_reenalda_1919_uniform_master.jpg` is the unchanged `1206 x 1765` grayscale source with SHA-256 `8F93840B12ECDCB313279C6F0FD4027863F8C1C4C9232E699AA7A0A9D46668CE`; the manifest records the Tresoar collection record, 1919 date, unknown maker, and public-domain basis retained from the vetted Frisia source package. |
| Male-subject compliance | **PASS** | The master, crop, raw result, and processed PNG each show one male subject; `common/characters/006_independence_wave_wallonia_frisia_characters.txt:109-119` sets `gender = male` and only the full `army.large` portrait slot for `AGX_friesland_coastal_commander`; no female metadata or opposite-gender name pool is involved. |
| Frisian and maritime role fit | **PASS** | Pieter Reenalda is documented in the source package as a Frisian KPM first officer born in 1887, and the selected 1919 maritime uniform gives the AGX coastal-commander role a direct regional and maritime basis. The alternate office is not presented as a claim that he historically commanded an independent Frisian army. |
| Explicit head-and-shoulders crop | **PASS (geometry and identity)** | `source_crops/AGX_pieter_reenalda_1919_head_shoulders_crop.png` declares `left=203, top=130, right=1003, bottom=1207` and decodes as `800 x 1077`; independent comparison against the master rectangle found no offset, rescale, or visible retouching. A strict Pillow decoded comparison found only +/-1 grayscale-level deltas in 16,430 of 861,600 pixels (`max_abs=1`, mean absolute delta `0.019`), so a zero-delta re-export is recommended if the producer treats the source-pixel gate literally. |
| Identity and likeness preservation | **FAIL (non-compensable)** | Native and disposable nearest-neighbour 4x review show the repaint regularizing the source's unequal eye sizes, lids, and gaze; changing ear exposure and angle; broadening and softening the long narrow nose; widening the tapering lower face and enlarging/rounding the small chin; and altering the high forehead/side-parted hairline wave. The exceptionally long, dense handlebar moustache loses the source center mass and exact height, with shorter, lighter, more symmetric ends and a changed viewer-left lower asymmetry. The raw result also clarifies metallic-looking shoulder-board emblems and stripe contrast beyond source-supported neutral geometry, violating the prompt's ban on invented or unsupported insignia treatment. The processed `156 x 210` output retains these identity changes. |
| HOI4 commander style | **PASS** | The processed candidate is a subdued painterly full commander portrait with a dark desaturated maritime background, readable head-and-shoulders silhouette, period high collar, no text, watermark, UI, modern prop, dossier frame, or generic raw-photo finish; the commander sheet uses the recorded Montgomery and Witzleben references. Style quality does not compensate for the failed identity gate. |
| `156 x 210` framing | **PASS** | `processed_png/portrait_AGX_friesland_coastal_commander.png` decodes as opaque RGBA `156 x 210`, with one centered head-and-shoulders subject, safe head and shoulder margins, visible high collar, and no frame or dossier treatment. |
| Ownership and stable-consumer fit | **PASS (consumer mapping only)** | The intended owner is unambiguous: `history/countries/AGX - Frisia.txt:18` recruits `AGX_friesland_coastal_commander`; `common/characters/006_independence_wave_wallonia_frisia_characters.txt:109-114` defines the male corps commander; `interface/006_independence_wave_region_01_portraits.gfx:23-24` maps `GFX_portrait_AGX_friesland_coastal_commander` to the stable DDS path; and `localisation/english/006_independence_wave_wallonia_frisia_l_english.yml:6` names the token `Pieter Reenalda`. The pre-existing DDS at `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_commander.dds` has SHA-256 `07689A7045C145401E5AA7A2CFC1AE0949D59C62D4B64F144714E20197558BBA` and is not this trial; identity failure leaves this trial's runtime transfer uncleared. |
| Absence of advisor, dossier, and `_small` assets | **PASS** | The trial directory contains no advisor, high-command, operative, dossier, or `_small` derivative, and the character definition uses only the existing full `army.large` slot. |

Identity and style were evaluated as independent gates. The style pass, source rights, role fit, and correct consumer mapping do not compensate for the failed identity gate, so the package remains export-only and unwired.

## Evidence and deterministic processing

The immutable source master is `source_masters/AGX_pieter_reenalda_1919_uniform_master.jpg` at `1206 x 1765`, byte count `145,425`, SHA-256 `8F93840B12ECDCB313279C6F0FD4027863F8C1C4C9232E699AA7A0A9D46668CE`.

The explicit crop is `source_crops/AGX_pieter_reenalda_1919_head_shoulders_crop.png` from source rectangle `(203, 130, 1003, 1207)` at `800 x 1077` with SHA-256 `653437B6CBA46027CE630AB8EBC70D7355C1B86A7F3D64631BAFDC2E82D3AF71`.

The raw ImageGen result is `imagegen_results/AGX_pieter_reenalda_identity_preserve_trial_01.png` at `1081 x 1455` with SHA-256 `4EBE0BDFF3AC39D89387E887BF22499975D520A6D1B409F06989C44C5B4BFFA2`.

The identity-preserving prompt is `identity_repaint_prompt.md` with SHA-256 `353C12A05A1187572C305B66DD3B9C42C44BACA200766604148315FE0A08293B` and explicitly locks the high forehead, uneven eyes and ears, long narrow nose, tapering face and small chin, exact moustache mass/length/asymmetry, source-supported uniform geometry, and no invented insignia.

The deterministic processor is `.agents/skills/chaos-redux-event-assets/tools/advisor_icon_processing.py` version 5.0 with SHA-256 `1ADB521B43238EE971E093DAE90007C4C44C600435EBB897C6482BA3B64B96EC`, positional mode `leader`, role family `commander`, and recorded Python `3.9.12` / Pillow `11.1.0` runtime.

The processed candidate is `processed_png/portrait_AGX_friesland_coastal_commander.png` at `156 x 210` with SHA-256 `C683EEB6E71FE5EF118843F3748DB9C66136ACBC5C120C8B82F35FC55CE3789C`.

The processor metadata is `processing_metadata.json` with SHA-256 `841E4DECAEF783D988F9FEC9DB836FAED63399CD444E05B521AC21EB7C7C665D`; its recorded source, candidate, processor, and review hashes matched the files on disk.

The review sheet is `review/AGX_pieter_reenalda_commander_style_sheet.png` with SHA-256 `AC44475681DE159973EEADD8A7140AE3848D3EDE74B5DD1444A914B93EE8A167`.

The processor selected `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/commanders/eng_bernard_montgomery.png` with SHA-256 `39B03871D7451CA96712A5CCF3C056528693F82642776E6C5E297E041943944E` and `ger_erwin_von_witzleben.png` with SHA-256 `10F4A1108F9D440213F70FB5802349A2291F298F9D132644241119561577D5B6`.

All eight entries in `hashes.sha256` matched on audit. The processor hash matched the checked-in tool, and the metadata-recorded source, output, and review hashes matched the files on disk.

The processor review sheet is a 2x full-size style sheet whose first panel is the processor input crop of the raw ImageGen result rather than the immutable archival crop; I therefore compared the archival master, explicit crop, raw result, processed candidate, and role references separately at native and enlarged sizes.

I used disposable nearest-neighbour 4x comparison sheets outside the repository for the identity review and removed them after inspection; no audit image was added to the trial or used as a runtime asset.

## Identity defects requiring a source-only retry

The retry must use the unchanged `source_masters/AGX_pieter_reenalda_1919_uniform_master.jpg` and a zero-delta re-export of the declared crop as the only identity authority and must not use this failed repaint as an identity reference.

The retry must preserve the high broad forehead and uneven side-parted hairline, the unequal eye sizes/lids/gaze, unequal ears and angles, long narrow straight nose, tapering face and small rounded-pointed chin, exact apparent age/expression/head angle, and the exceptionally long dense horizontal moustache with its source center mass, height, thin ends, and viewer-left lower/longer asymmetry.

The retry may keep the subdued maritime commander background and period painterly finish, but it must not open or symmetrize the eyes, reshape the ears, widen or shorten the nose, broaden the lower face, enlarge the chin, shorten/curl/symmetrize the moustache, polish the hairline into a generic side part, or clarify/colorize shoulder-board insignia beyond source-supported neutral geometry.

## Country-package consumer surface checklist

| Surface | Status | Finding |
|---|---|---|
| Tag and character registration | **PASS** | `AGX` is the stable country tag and the intended `AGX_friesland_coastal_commander` character is defined and recruited once. |
| Portrait sprite and path | **PASS (mapping only)** | The existing `.gfx` mapping is stable and points to the expected `006_independence_wave` DDS path; no `.gfx` edit was made. |
| Player-facing name and gender | **PASS** | Localisation names the male token Pieter Reenalda and does not use a female metadata/name pool. |
| Runtime transfer | **BLOCKED** | The current trial fails identity; the pre-existing DDS is not evidence for this trial and must remain untouched by this audit. |

No focus, decision, idea, advisor, technology, army, production, supply, AI, map, state, flag, or country-identity redesign was in scope for this bounded portrait audit.

## Runtime and scope disposition

No DDS, `.gfx` edit, gameplay edit, localisation edit, advisor asset, dossier card, `_small` derivative, or fallback was created by this audit.

The trial manifest is marked `rejected_identity_runtime_hold`. The pre-existing DDS from the prior candidate at `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_commander.dds` is not this candidate and is not approved by this trial.

## Remaining risks

The source is rights-clear and role-defensible under the documented Frisian KPM-maritime alternate-history abstraction, but the rejected repaint must not be described as an accepted 1936 active Frisian army portrait.

The candidate's style and framing are acceptable as commander-family treatment, but the identity drift and unsupported shoulder-board clarification are non-compensable and block any DDS conversion or runtime use.

No fallback, generic person, opposite-gender pairing, advisor/dossier derivative, or unrelated consumer is authorized.
