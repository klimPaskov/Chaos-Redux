# IW-002 Wales commander source-clearance handoff: HU 126780 retry

Date: 2026-07-25

Status: blocked_identity_mismatch

Scope: source research and immutable evidence only for the requested male Major-General Gervase Thorpe mountain-commandant portrait. No ImageGen, processed `156x210` portrait, DDS, `.gfx`, localisation, gameplay or fallback asset was created.

## Decision

The already identified IWM HU 126780 source is not valid for the requested Major-General Gervase Thorpe. The IWM object page is titled **Second Lieutenant Gervase Thorpe Spendlove**, identifies the 2nd Battalion, The Prince of Wales' Volunteers (South Lancashire Regiment), and records that this namesake was killed on 17 November 1914. The requested Major-General Gervase Thorpe (1877-1962) is a separate identity, documented as GOC of the 53rd (Welsh) Infantry Division from 1935 to 1939 and alive in 1936. The IWM record contains no evidence linking the two men.

The source is therefore retained only as blocked provenance evidence. The crop is visually clear enough to show an adult male face, ears, brow, nose, mouth, jaw, hairline, cap, collar and both shoulder tops, but visual clarity cannot overcome the wrong-person identity gate. It is not usable as a 1936 WLS mountain-commandant identity master, and the package must not send it to ImageGen, deterministic processing or runtime wiring.

## Archive and licence evidence

- Object page: https://www.iwm.org.uk/collections/item/object/205388980
- Exact archive image URL: https://media.iwm.org.uk/ciim5/439/54/large_000000.jpg
- Archive: Imperial War Museums, BOND OF SACRIFICE - FIRST WORLD WAR PORTRAITS COLLECTION, object `205388980`, catalogue number `HU 126780`.
- Retained page snapshot: `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_25/wales_two_role_clearance/source_page_snapshots/gervase_thorpe_iwm_hu126780_page.md` with SHA-256 `e67bb1221f535430cbc78a4b98c8b3a9a5c638c10d338c7518aff45d1ddc6c10`.
- Photographer and exact photograph date: not stated in the IWM record. IWM classifies the record as First World War production/content.
- Licence: [IWM Non-Commercial Licence](https://www.iwm.org.uk/corporate/policies/non-commercial-licence).
- Required attribution: `Image: IWM (HU 126780)`.
- Non-commercial terms recorded by the IWM page permit low-resolution download or embed for private non-commercial research/study and applicable local exceptions, information-led non-paywalled research websites, personal social media that does not promote a commercial activity, non-commercial education, offline viewing/listening and free exhibitions.
- Commercial use, high-resolution copies or uses outside the listed terms require a separate IWM licence. No public-domain claim is made.
- Licence compliance cannot cure the identity mismatch. Any later correctly identified IWM source must retain its own attribution and licence terms.

## Source master and current endpoint probe

- Immutable retained source master: `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_25/wales_two_role_clearance/source_masters/gervase_thorpe_spendlove_iwm_hu126780.jpg`.
- Retained source master: `612x800`, RGB JPEG, SHA-256 `7cdb3a70f983105f579c5f141cecc631c665eae16cdb71e2ee7266b924d7041d`.
- Lossless decoded master: `source_master_png/gervase_thorpe_commander_master.png`, `612x800`, RGB PNG, SHA-256 `cb76ddba4dba74304db6a1fd16933bc6d712c85de6b16f287f6feae572487bbe`.
- Retained decoded RGB/RGBA pixels: SHA-256 `6906566d7b0d5eaecb0abbb6f63d3a3f6483f900fefc4b2e0d82bf9f0457f6e0`.
- Direct URL probe date: 2026-07-25.
- Direct endpoint probe response: `image/jpeg`, `193301` bytes, `612x800` RGB, `Last-Modified: Thu, 19 Jan 2023 18:09:24 GMT`, ETag `31d9f-5f2a1d5368f14`, SHA-256 `b38bd04dc327bc94b64c3cf0472120cbab434c7511d63e51fe490ce70dbf7480`.
- The current endpoint's byte hash differs from the retained JPEG, but its decoded RGB/RGBA pixels equal the retained master (`6906566d7b0d5eaecb0abbb6f63d3a3f6483f900fefc4b2e0d82bf9f0457f6e0`). The retained master remains the immutable crop parent.

## Exact Pillow crop evidence

- Crop utility: `.agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py`, Pillow backend, tool SHA-256 `14fa178d6df999346874a7033e84f9b3ae988e7d845f3a4b2f8a44755e30641c`, version `1.0`.
- Exact head-and-shoulders crop rectangle in decoded master pixels: `[left=10, top=80, right=602, bottom=720]`.
- Crop output: `source_crops/gervase_thorpe_commander_crop.png`, `592x640`, RGB PNG, SHA-256 `016c1d5977507b01ba96e2326152ddd0f8517f813f7a85e70348b13867919f01`.
- Equality JSON: `source_crops/gervase_thorpe_commander_crop.json`.
- Equality result: `decoded_pixels_equal: true`; `master_crop_rgba_sha256` and `output_rgba_sha256` both equal `3f4666b6918993d3d2b2634cd24c9f6a3cad575f5f18301c7ec1134c45370fbf`; pixel count `378880`.
- The equality JSON records master dimensions `[612, 800]`, crop dimensions `[592, 640]`, RGB decode/output modes, Pillow `11.1.0`, normalized crop command and the tool hash. No resize, enhancement, recolour, retouch or ImageGen operation was applied.

## Ownership and runtime boundary

The ownership scan found no existing character or portrait consumer for the requested Gervase Thorpe terms in the checked roots, but that no-match result does not establish that the HU 126780 namesake is the requested person. The reserved runtime consumer remains `GFX_portrait_WLS_independence_wave_mountain_commandant` -> `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_mountain_commandant.dds`; this source must not be wired there.

The package does not authorize a generic, female, fallback or invented replacement. The parent must source an attributed photograph of the correct Major-General Gervase Thorpe or obtain explicit user approval for a different grounded identity before downstream portrait work.

## Owned package files

- `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_25/wales_two_role_clearance/metadata/gervase_thorpe_hu126780_source_clearance.json`
- `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_25/wales_two_role_clearance/source_masters/gervase_thorpe_spendlove_iwm_hu126780.jpg`
- `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_25/wales_two_role_clearance/source_master_png/gervase_thorpe_commander_master.png`
- `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_25/wales_two_role_clearance/source_crops/gervase_thorpe_commander_crop.png`
- `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_25/wales_two_role_clearance/source_crops/gervase_thorpe_commander_crop.json`
- `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_25/wales_two_role_clearance/source_page_snapshots/gervase_thorpe_iwm_hu126780_page.md`
- `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_25/wales_two_role_clearance/contact_sheets/wales_two_role_clearance_contact_sheet_v7.png`
- `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_25/wales_two_role_clearance/contact_sheets/wales_two_role_clearance_contact_sheet_v6.png` (superseded; stale source-ready label, do not use)
- `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_25/wales_two_role_clearance/manifest.json`
- `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_25/wales_two_role_clearance/manifest.md`
- `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_25/wales_two_role_clearance/ownership_scan.md`
- `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_25/wales_two_role_clearance/research/source_clearance.md`
- `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_25/wales_two_role_clearance/gfx_handoff.md`

## Validation and risks

The direct archive URL returned a live `612x800` image and the downloaded probe decoded pixel-identically to the retained source master. The Pillow crop utility was rerun independently against the retained PNG master and reproduced the committed output SHA and equality hashes. The v7 contact sheet visibly labels HU 126780 as a blocked namesake rather than a source-ready commander.

Primary risk: the requested identity was previously conflated with a similarly named IWM subject. Any downstream portrait made from HU 126780 would be an invented or substituted real-person likeness and would violate the grounded-source gate. Keep the package blocked until a correctly identified Major-General Gervase Thorpe source is found or the parent obtains explicit design direction.
