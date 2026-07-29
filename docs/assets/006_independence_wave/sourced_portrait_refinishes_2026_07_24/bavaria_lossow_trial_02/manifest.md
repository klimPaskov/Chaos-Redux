# IW-009 Bavaria Otto von Lossow trial 02

Status: `blocked` (`independent_audit_provenance_gate_failed`).

This is a candidate package only.

It creates no DDS and changes no sprite, character, gameplay, localisation, readiness, or runtime file.

## Identity and ownership

The candidate is Otto Hermann von Lossow, a real male Bavarian officer alive in 1936 and a researched alternative for the stable `BAY_independence_wave_mountain_commandant` consumer.

The source and ownership package is `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/otto_von_lossow_source_retry/`.

The ownership scan found no vanilla or Chaos Redux character, portrait, recruitment, or meaningful existing-tree consumer for Lossow.

The source package records one provenance caveat: the 1923 Wikimedia Commons page identifies Bain News Service and public-domain United States status but does not provide an exact Library of Congress catalog identifier for this scan.

That caveat must receive a separate provenance verdict before runtime use.

## Exact archival crop

The immutable master is `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/otto_von_lossow_source_retry/source_masters/OTTO_von_lossow_bain_1923_original.jpg`, `8980x13470`, SHA-256 `AD5B0F11C107EB58FBA5BD00975E7A64B046234CC16D61299D8EA6F49D28192F`.

The exact crop was recreated with `.agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py` at decoded-master rectangle `(1300,0)-(7763,8700)`.

The retained lossless crop is `source_crops/BAY_otto_von_lossow_exact_head_shoulders_1300_0_7763_8700.png`, `6463x8700`, SHA-256 `5C5D8600B19F12DCA29A43B1E457A74D39CC704F50CE0718A0C9FE73084FD043`.

The retained JSON evidence is `source_crops/BAY_otto_von_lossow_exact_head_shoulders_1300_0_7763_8700.json`, SHA-256 `FA3CC0A97B732FED33A7CB0C079A51D1A9C3294CFA8DAC1D845A7BA1D1117879`.

It records `decoded_pixels_equal = true`; the decoded master rectangle and reopened crop share RGBA SHA-256 `163869E327A6760C03E49D460320816EE663AB0FE6AE9636E5A9F414D5CAC3AD`.

## ImageGen repaint

The built-in ImageGen tool used only the exact crop as the identity and composition input.

The retained raw output is `imagegen_results/BAY_otto_von_lossow_identity_preserve_trial_02.png`, `1080x1456`, SHA-256 `71129DCDEA0EACA5F13BA7066B4901C16E12499E3DAF478AA513E6D16170DEEF`.

The exact prompt is retained in `identity_repaint_prompt.md`.

The canonical commander references were not identity inputs.

They are used only by the deterministic processor review sheet.

## Deterministic candidate

The candidate was processed with `retired_advisor_card_processor_REMOVED leader --role-family commander`.

The processed candidate is `processed_png/portrait_BAY_independence_wave_mountain_commandant.png`, `156x210`, SHA-256 `3185DDE35415BF58FD31E5152A01F6E05AA3A64F4B1607874D028BC9106B6B47`.

The processor review sheet is `review/BAY_otto_von_lossow_commander_style_sheet.png`, SHA-256 `13E4D4E3288C3538FDCECD95E800E7BDA4F4C77DBD79CC2382E6755C16642487`.

The processing record is `processing_metadata.json`, SHA-256 `63B026072D60410D6CCF451BC07BA9FCC864A5CD2755A176768140B97EA83B74`.

The metadata records `role_family = commander`, the Montgomery and Witzleben style references, deterministic artifact hashes, and `candidate_requires_visual_approval`.

## Audit boundary

An independent reviewer who did not produce the candidate must compare the immutable master, exact crop, raw ImageGen result, processed candidate, and commander references at native and at least 4x nearest-neighbour scale.

Likeness, HOI4 commander style, and provenance are separate pass/fail gates.

Style quality cannot compensate for identity drift.

DDS conversion and runtime wiring are forbidden until all three gates pass.

## Independent audit — 2026-07-24

Reviewer: independent parent-scope reviewer; the candidate producer did not approve this package.

The unchanged master, exact crop, raw ImageGen repaint, deterministic `156x210` candidate, and canonical commander references were inspected at native size and at least `4x` nearest-neighbour scale. The retained processor review sheet is `1344x464` and contains the input crop, candidate, and the two selected references; the independent `4x` comparison was generated only in a temporary review location and was not added to the package.

| Gate | Verdict | Evidence and disposition |
| --- | --- | --- |
| Likeness / identity | **PASS** | Lossow remains recognizable from the unchanged source through the raw repaint and candidate. The tall narrow skull and very high bald forehead, thin side hair, round wire-rim glasses and placement, unequal eyes and off-centre gaze, long narrow nose, compact moustache, thin closed lips, lean cheeks, angular jaw and small chin, visible ear asymmetry, age, reserved expression, three-quarter head angle, neck, and shoulder slope are all retained. No generic face, beautification, frontalization, symmetrization, face substitution, or invented hidden identity detail was observed. Identity passes as a separate non-compensable gate. |
| HOI4 commander style | **PASS** | The candidate is an opaque, subdued oil-painted `156x210` commander portrait with period clothing, controlled contrast, quiet dark background, and visible brush texture. It belongs to the canonical commander family represented by Montgomery and Witzleben, and is not a raw photograph, sepia conversion, advisor card, dossier, or modern concept-art finish. |
| Provenance / rights | **FAIL — blocked** | The unchanged source is the 1923 Bain News Service photograph published through Wikimedia Commons under `PD-US`. Commons does not establish worldwide public-domain status, and the source page supplies no exact Library of Congress catalog/LCCN/digital ID for this scan. Do not relabel it as the separately catalogued LOC `Gen. Lossow` record `2014716720` (dated 1900). The disclosed jurisdiction and archive-identity caveat remains unresolved; obtain user/legal acceptance or stronger object-level rights evidence before runtime distribution. |
| Male and historical/role fit | **PASS with abstraction caveat** | The source is a real male Otto Hermann von Lossow, alive in 1936 and documented as a Bavarian/German general, Wehrkreis VII commander, 7th Division commander, and Bavarian Landeskommandant during the 1923 crisis. The IW-009 passes-and-depots commandant is an alternate-history territorial-command abstraction, not a claim that he historically held that named 1936 office or a specialist mountain branch. |
| Exact crop | **PASS** | Half-open source rectangle `(1300,0)-(7763,8700)` on the immutable `8980x13470` master produces a `6463x8700` crop. The retained JSON records `decoded_pixels_equal = true`; direct Pillow recomputation also matched the master rectangle byte-for-byte in RGBA. |
| Framing | **PASS** | The candidate is a deterministic full `156x210` commander portrait with head, neck, both shoulders, source-supported collar and shoulder decoration, and no clipping or dossier framing. |
| Ownership / consumer mapping | **PASS — not admitted** | The upstream ownership scan found no Lossow character, portrait owner, recruitment, GFX owner, or meaningful existing consumer in current Chaos Redux, vanilla, or the approved reference roots. The proposed stable consumer is the existing male corps-commander token `BAY_independence_wave_mountain_commandant`, sprite `GFX_portrait_BAY_independence_wave_mountain_commandant`, and reserved path `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_mountain_commandant.dds`. Current localisation still names that token Eugen Ritter von Schobert, so a future admission would require parent-owned identity/localisation reconciliation; this audit does not wire it. |
| Advisor/dossier/`_small` derivatives | **PASS** | No advisor, high-command dossier, operative, or `_small` derivative exists in this candidate package or the Lossow source/ownership package. The candidate remains full-size commander art only. |

### Exact artifact hashes

All hashes below are SHA-256. The candidate processor's decoded RGBA hash includes its repository-specific `chaos-redux-decoded-rgba-v1` prefix and dimensions.

| Artifact | Dimensions | File SHA-256 |
| --- | ---: | --- |
| Immutable master `source_masters/OTTO_von_lossow_bain_1923_original.jpg` | `8980x13470` | `AD5B0F11C107EB58FBA5BD00975E7A64B046234CC16D61299D8EA6F49D28192F` |
| Exact candidate crop `source_crops/BAY_otto_von_lossow_exact_head_shoulders_1300_0_7763_8700.png` | `6463x8700` | `5C5D8600B19F12DCA29A43B1E457A74D39CC704F50CE0718A0C9FE73084FD043` |
| Raw ImageGen repaint `imagegen_results/BAY_otto_von_lossow_identity_preserve_trial_02.png` | `1080x1456` | `71129DCDEA0EACA5F13BA7066B4901C16E12499E3DAF478AA513E6D16170DEEF` |
| Deterministic candidate `processed_png/portrait_BAY_independence_wave_mountain_commandant.png` | `156x210` | `3185DDE35415BF58FD31E5152A01F6E05AA3A64F4B1607874D028BC9106B6B47` |
| Review sheet `review/BAY_otto_von_lossow_commander_style_sheet.png` | `1344x464` | `13E4D4E3288C3538FDCECD95E800E7BDA4F4C77DBD79CC2382E6755C16642487` |
| Canonical `eng_bernard_montgomery.png` | `156x210` | `39B03871D7451CA96712A5CCF3C056528693F82642776E6C5E297E041943944E` |
| Canonical `ger_erwin_von_witzleben.png` | `156x210` | `10F4A1108F9D440213F70FB5802349A2291F298F9D132644241119561577D5B6` |

The candidate's processor metadata records decoded RGBA SHA-256 `892e9df0e22d85e626dd0d712aec8cfb5ce7a582c6f947ab34a84a878fbdb4d0`; its alpha channel is fully opaque (`255..255`). The exact-crop decoded RGBA SHA-256 is `163869e327a6760c03e49d460320816ee663ab0fe6ae9636e5a9f414d5cac3ad`, matching the master rectangle and retained crop JSON.

### Admission decision

Overall disposition: **BLOCKED — provenance/rights fail closed.** Likeness, commander style, role fit, framing, exact crop, ownership mapping, and derivative-boundary gates pass, but the rights caveat is non-compensable for runtime distribution. Do not create DDS, edit `.gfx`, replace the current Schobert runtime texture, or wire this candidate until the PD-US jurisdiction and missing exact-LOC identity caveat are resolved. No fallback is authorized.
