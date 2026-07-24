# Event 006 IW-009 Bavaria Otto von Lossow trial 02 independent audit

Audit date: 2026-07-24.

Audited commit: `efc8eb0c2` (`Add exact-crop Bavaria portrait retries`).

Reviewer mode: independent read-only visual/provenance audit; the candidate producer did not approve this result.

## Scope and disposition

The audited candidate is `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_24/bavaria_lossow_trial_02/`.

The immutable source and ownership evidence is `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/otto_von_lossow_source_retry/`.

The candidate remains **BLOCKED** because the provenance/rights gate fails closed on the disclosed Commons/Bain/`PD-US` and missing exact-LOC identity caveat.

No DDS was created, no `.gfx` or runtime file was edited, no gameplay/localisation file was edited, and no protected BAY Rupprecht or RHI Matthes portrait was touched.

## Separate verdicts

| Gate | Verdict | Independent finding |
| --- | --- | --- |
| Likeness / identity | **PASS** | The source, raw repaint, and `156x210` candidate preserve the tall narrow skull, very high bald forehead, thin side hair, round wire-rim glasses and placement, unequal eyes and off-centre gaze, long narrow nose, compact uneven moustache, thin closed lips, lean cheeks, angular jaw and small chin, visible ear asymmetry, age, reserved expression, three-quarter head angle, neck, and shoulder slope. The candidate remains a specific recognizable Lossow and shows no genericization, beautification, symmetrization, frontalization, face substitution, or invented hidden identity detail. Identity was judged separately and not compensated by style. |
| HOI4 commander style | **PASS** | The result is a full opaque `156x210` oil-painted commander portrait with controlled contrast, quiet dark background, restrained brush texture, period clothing, and no text, watermark, UI, modern prop, advisor frame, or dossier paper. It fits the canonical commander family represented by `eng_bernard_montgomery.png` and `ger_erwin_von_witzleben.png`. |
| Provenance / rights | **FAIL — blocking** | The source package documents a 1923 Bain News Service photograph from Wikimedia Commons with `PD-US` status, but Commons does not establish worldwide public-domain status and the exact scan has no LOC catalog/LCCN/digital ID on its page. The source must not be relabelled as the separately catalogued LOC `Gen. Lossow` record `2014716720`, dated 1900. Obtain user/legal acceptance of the jurisdiction caveat or stronger object-level rights/archive evidence before runtime distribution. |
| Male and historical/role fit | **PASS with abstraction caveat** | Otto Hermann von Lossow is a real male Bavarian/German general, alive in 1936, documented as commander of Wehrkreis VII and the 7th Division and as Bavarian Landeskommandant during the 1923 crisis. The IW-009 passes-and-depots commandant is an alternate-history territorial-command abstraction and must not be described as a literal historical 1936 office or specialist mountain-branch post. |
| Exact crop | **PASS** | The candidate crop uses half-open source rectangle `(1300,0)-(7763,8700)` on the immutable `8980x13470` master and is `6463x8700`. The retained JSON says `decoded_pixels_equal = true`, and direct Pillow comparison reproduced the same RGBA pixels from the master rectangle. |
| Framing | **PASS** | The candidate is deterministic full-size commander art at `156x210`, retaining head, neck, both shoulders, source-supported collar/shoulder decoration, and the requested head-and-shoulders composition without clipping or dossier framing. |
| Ownership / consumer mapping | **PASS — not admitted** | The upstream scan found no Lossow character, portrait owner, recruitment, GFX owner, or meaningful existing consumer in current Chaos Redux, installed vanilla, or approved reference roots. The proposed stable target is the male corps-commander token `BAY_independence_wave_mountain_commandant`, sprite `GFX_portrait_BAY_independence_wave_mountain_commandant`, and reserved runtime path `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_mountain_commandant.dds`. Current localisation still names that token Eugen Ritter von Schobert, so parent-owned identity/localisation reconciliation would be required after a future admission. |
| Advisor/dossier/`_small` derivatives | **PASS** | No advisor, high-command dossier, operative, or `_small` derivative exists in the candidate package or the Lossow source/ownership package. The candidate is full-size commander art only. |

Because provenance fails, the overall disposition is blocked even though likeness, style, role, crop, framing, ownership mapping, and derivative-boundary gates pass.

## Visual comparison evidence

The unchanged master, exact crop, raw ImageGen repaint, deterministic candidate, and canonical commander references were inspected at native size and at least `4x` nearest-neighbour scale.

The retained processor sheet `review/BAY_otto_von_lossow_commander_style_sheet.png` is `1344x464` and shows the processor input crop, candidate, Montgomery reference, and Witzleben reference.

The independent `4x` nearest-neighbour comparisons were generated only in a temporary location for this audit and were not added to the package, consistent with the parent restriction to update only the candidate manifest and this handoff.

At native and enlarged sizes, the candidate reads as the same man rather than a generic bald officer: the high forehead, glasses, narrow nose, moustache, asymmetrical eyes/gaze, ear, lean jaw/chin, age, and three-quarter angle remain coherent.

The source-visible uniform collar and shoulder decorations remain source-supported details; no unsupported insignia or new identity-bearing decoration was observed.

The candidate is opaque RGBA with alpha range `255..255`.

## Exact hashes

All file hashes below are SHA-256.

| Artifact | Dimensions | SHA-256 |
| --- | ---: | --- |
| Immutable master `source_masters/OTTO_von_lossow_bain_1923_original.jpg` | `8980x13470` | `AD5B0F11C107EB58FBA5BD00975E7A64B046234CC16D61299D8EA6F49D28192F` |
| Candidate exact crop `source_crops/BAY_otto_von_lossow_exact_head_shoulders_1300_0_7763_8700.png` | `6463x8700` | `5C5D8600B19F12DCA29A43B1E457A74D39CC704F50CE0718A0C9FE73084FD043` |
| Exact-crop JSON `source_crops/BAY_otto_von_lossow_exact_head_shoulders_1300_0_7763_8700.json` | schema 1 | `FA3CC0A97B732FED33A7CB0C079A51D1A9C3294CFA8DAC1D845A7BA1D1117879` |
| Raw ImageGen `imagegen_results/BAY_otto_von_lossow_identity_preserve_trial_02.png` | `1080x1456` | `71129DCDEA0EACA5F13BA7066B4901C16E12499E3DAF478AA513E6D16170DEEF` |
| Deterministic candidate `processed_png/portrait_BAY_independence_wave_mountain_commandant.png` | `156x210` | `3185DDE35415BF58FD31E5152A01F6E05AA3A64F4B1607874D028BC9106B6B47` |
| Processing metadata `processing_metadata.json` | schema 5 | `63B026072D60410D6CCF451BC07BA9FCC864A5CD2755A176768140B97EA83B74` |
| Review sheet `review/BAY_otto_von_lossow_commander_style_sheet.png` | `1344x464` | `13E4D4E3288C3538FDCECD95E800E7BDA4F4C77DBD79CC2382E6755C16642487` |
| Canonical commander `eng_bernard_montgomery.png` | `156x210` | `39B03871D7451CA96712A5CCF3C056528693F82642776E6C5E297E041943944E` |
| Canonical commander `ger_erwin_von_witzleben.png` | `156x210` | `10F4A1108F9D440213F70FB5802349A2291F298F9D132644241119561577D5B6` |

The processor metadata's repository-specific decoded RGBA SHA-256 for the candidate is `892e9df0e22d85e626dd0d712aec8cfb5ce7a582c6f947ab34a84a878fbdb4d0`.

The exact-crop decoded RGBA SHA-256 is `163869e327a6760c03e49d460320816ee663ab0fe6ae9636e5a9f414d5cac3ad`, matching the decoded master rectangle and retained JSON equality evidence.

## Provenance and rights blocker

The upstream source package records the Commons title `General Otto von Lossow 01.jpg`, Bain News Service as source agency, 1923 as date, unknown author, and `PD-US` public-domain status in the United States.

It also explicitly records that the Commons page does not provide an exact LOC catalog number, LCCN, digital ID, persistent LOC image URL, or worldwide rights statement for this 1923 scan.

The Commons page must not be collapsed into the distinct LOC `Gen. Lossow` record `2014716720`, which is dated 1900 and is not evidence that this exact scan is an LOC object.

This caveat is not silently waived: the source is acceptable identity evidence and a reproducible processing input, but it is not admitted runtime art until the jurisdiction/rights question is resolved.

## Runtime and ownership boundary

The candidate proposes the stable consumer `BAY_independence_wave_mountain_commandant` / `GFX_portrait_BAY_independence_wave_mountain_commandant` / `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_mountain_commandant.dds`.

The current runtime consumer remains the existing Schobert-labelled BAY token and existing runtime texture; this candidate has not replaced it.

No DDS, `.gfx`, character, gameplay, localisation, advisor, dossier, operative, or `_small` output was created by this audit.

The protected BAY Rupprecht and RHI Matthes portraits were not read or modified.

## Required parent action

Keep the candidate status `blocked` and do not wire it.

Resolve the Commons `PD-US` jurisdiction caveat and missing exact-LOC identity evidence, or obtain a separately rights-clear source, before any DDS conversion or runtime admission.

No fallback, generic portrait, raw-photo resize, advisor/dossier card, `_small` derivative, or gameplay substitution is authorized by this audit.
