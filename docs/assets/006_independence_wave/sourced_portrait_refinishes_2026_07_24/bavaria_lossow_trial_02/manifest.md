# IW-009 Bavaria Otto von Lossow trial 02

Status: `candidate_requires_independent_likeness_style_provenance_audit`.

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

The candidate was processed with `.agents/skills/chaos-redux-event-assets/tools/advisor_icon_processing.py leader --role-family commander`.

The processed candidate is `processed_png/portrait_BAY_independence_wave_mountain_commandant.png`, `156x210`, SHA-256 `3185DDE35415BF58FD31E5152A01F6E05AA3A64F4B1607874D028BC9106B6B47`.

The processor review sheet is `review/BAY_otto_von_lossow_commander_style_sheet.png`, SHA-256 `13E4D4E3288C3538FDCECD95E800E7BDA4F4C77DBD79CC2382E6755C16642487`.

The processing record is `processing_metadata.json`, SHA-256 `63B026072D60410D6CCF451BC07BA9FCC864A5CD2755A176768140B97EA83B74`.

The metadata records `role_family = commander`, the Montgomery and Witzleben style references, deterministic artifact hashes, and `candidate_requires_visual_approval`.

## Audit boundary

An independent reviewer who did not produce the candidate must compare the immutable master, exact crop, raw ImageGen result, processed candidate, and commander references at native and at least 4x nearest-neighbour scale.

Likeness, HOI4 commander style, and provenance are separate pass/fail gates.

Style quality cannot compensate for identity drift.

DDS conversion and runtime wiring are forbidden until all three gates pass.
