# Event 016 final Directorate background art candidate handoff

Status: needs_user_review pending user-owned live in-game acceptance; parent visual review and runtime installation are complete.

Task scope: corrective art only for the Event 016 scripted-GUI expanded background. No gameplay, GUI, GFX, localisation, config, stage, or runtime file was edited by this worker. The parent installed the selected v3 binary at the existing runtime path after visual review.

Selected candidate files:

- Source PNG: docs/assets/016_brilliant_scientist/directorate_ui/closure_background_2026_09_02/source_png/directorate_background_closure_edit_source_v3.png
- Processed PNG: docs/assets/016_brilliant_scientist/directorate_ui/closure_background_2026_09_02/processed_png/directorate_background_closure_candidate_v3.png
- Converter-ready DDS: docs/assets/016_brilliant_scientist/directorate_ui/closure_background_2026_09_02/dds/directorate_background_closure_candidate_v3.dds
- Decoded DDS evidence: docs/assets/016_brilliant_scientist/directorate_ui/closure_background_2026_09_02/evidence/directorate_background_closure_candidate_v3_decoded.png
- Contact sheet: docs/assets/016_brilliant_scientist/directorate_ui/closure_background_2026_09_02/contact_sheets/directorate_background_closure_contact_sheet_v3.png
- Manifest: docs/assets/016_brilliant_scientist/directorate_ui/closure_background_2026_09_02/manifest.md
- Machine-readable validation: docs/assets/016_brilliant_scientist/directorate_ui/closure_background_2026_09_02/evidence/validation.json
- GFX handoff evidence: docs/assets/016_brilliant_scientist/directorate_ui/closure_background_2026_09_02/gfx_handoff.md

Native generation:

- Official built-in ImageGen was used in edit mode.
- v1 native output default path was C:\Users\klimp\.codex\generated_images\01a06279-b130-7d13-bc83-148376ec433b\exec-07176572-5de9-471f-aa28-656c8dd41683.png and was copied unchanged to the candidate source folder with SHA-256 F03A8AB15B47639E9C3D50C5536C5068B19BF356A98153E6D3BFFD89F0C78137.
- v2 native output default path was C:\Users\klimp\.codex\generated_images\01a06279-b130-7d13-bc83-148376ec433b\exec-82809901-6703-4eba-8e34-237c0749526d.png and was copied unchanged to the candidate source folder with SHA-256 D42582D1D16A24F132AE69911E81982CF6016A2B0B60FFF622EC9581DFE96D25.
- v3 native output default path was C:\Users\klimp\.codex\generated_images\01a06279-b130-7d13-bc83-148376ec433b\exec-2faf5553-d553-4f6e-a62f-4d8e7b019d37.png and was copied unchanged to the candidate source folder with SHA-256 EE5535A9EE6ACA89C3DC59CCB05241200BD24A94BC915D246C068986A80D356.
- v1 prompt SHA-256 is 50AAC20A22A571CACF113783A6815FD23E0AE79B2A2946DC59593B4C5D82F310.
- v2 prompt SHA-256 is D44CD859A5FC48C2D5EB2B33ACB06471F9D61A4E0C90DBC979EF64BA76673F68.
- v3 prompt SHA-256 is 4B28753A5788B6554B585E8BB58A7AB9E17905674C775287E62CEFA207146502.
- The v1, v2, and v3 source outputs are all 1478x1064 opaque RGB ImageGen PNGs.
- v1 direct resize and v2 direct resize remain rejected alternatives. Parent visual review specifically rejected v2 because both lower circular gauges were cut in half by the crop, leaving the outer frame visually cut off.

Selected output evidence:

- The parent-rejected v2 processed PNG remains 500x360 RGBA, all alpha bytes 255, SHA-256 923BA7A44655E519AD1C01E9BC835E4556F3EB3496ABCA74007022AFF7B722B1.
- The selected v3 processed PNG is 500x360 RGBA, all alpha bytes 255, SHA-256 EB35B3C4159BA58D1981E113B3AEE722E6BD8CA7DAAB7A288D9C18C6AC75DE66.
- The selected v3 DDS is 500x360 legacy uncompressed 32-bit BGRA, pitch 2000, exact file length 720128 bytes, all alpha bytes 255, SHA-256 C476E06B722EE6C41A07B85AFDD257B2232744F9D50185A2D0AD5068D080026D.
- DDS header validation passed for magic DDS, header size 124, pixel format size 32, flags 65, fourCC 0, 32 bits, BGRA masks, texture caps 0x1000, and exact payload length.
- Decoded DDS RGBA pixels equal the processed RGBA pixels exactly.
- The parent-rejected v2 decoded PNG SHA-256 is 146EACE2D169F0D09738A626627E5E12CB65708E9FEA2BD91B846575011F9CF3.
- The selected v3 decoded PNG SHA-256 is 0BC6F1C5C60A757F6BF192555828EC540FADF270F70C24E5CD05A44E2A56B4BB, and its decoded RGBA pixels equal the v3 processed RGBA pixels exactly.
- The v2 contact sheet SHA-256 is B90B8D4EE277727CFBFA447DE221B3531C3FC6F8FB76B08540C32BE8B5F9FC82.
- The selected v3 contact sheet SHA-256 is FC93C675773D4D7E61EB4BD3BC77B1EF52163BCF89E184BE48D1EB4B25C0A7A6.

Reference evidence:

- Source master: docs/assets/016_brilliant_scientist/directorate_ui/source_masters/directorate_background_master_v2.png, 1127x1396, SHA-256 C748CECBB9D01ABF2B85F8B2D8A8987070D15ECE46F22C8CAA108039B471CF30.
- Current processed and decoded compact PNGs: docs/assets/016_brilliant_scientist/directorate_ui/compact_refresh/processed_png/directorate_background.png and compact_refresh/decoded_dds/directorate_background.png, both SHA-256 381E2BA8C1A0B6DB21F2CEFC72BB6DA5DB30FE4FEB43B7A3DC5AC0AB51725056.
- Historical pre-repair runtime DDS baseline was SHA-256 380F0AF0B9A77D19A692B2A86B8D31D12BC14DA3B297F996A80B61A0F7563534.
- Parent-installed active runtime DDS at gfx/interface/016_brilliant_scientist/directorate/directorate_background.dds is SHA-256 C476E06B722EE6C41A07B85AFDD257B2232744F9D50185A2D0AD5068D080026D and matches the selected v3 DDS.
- Nearest canonical family inspected: .agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/report/contact_sheet.png, SHA-256 A50A2532A14E129584F21EA67B847A0E329C245187B57D5C577D10A265C0AEA4. It was consulted only for opaque canvas/background treatment because the canonical shelf has no dedicated scripted-GUI panel family.

Processing:

- The parent-rejected v2 export used ffmpeg crop=1478:1000:0:0 followed by scale=500:360:flags=lanczos and is retained only as comparison evidence.
- The selected v3 export used ffmpeg scale=500:360:flags=lanczos and pix_fmt=rgba on the complete 1478x1064 native ImageGen output, with no crop.
- The v3 lower border and both lower corners remain complete and fully inside the 500x360 canvas, with no partial circular gauges or machinery extending below the image. The observed trim begins around y=344 and remains subdued behind the footer while side rails stay within approximately x=0..25 and x=475..499.
- This was ordinary full-canvas resize/export only; no Python reconstruction, local repainting, background removal, alpha keying, or drawing substitute was used.

Parent wiring boundary:

- Parent-owned intended runtime path: gfx/interface/016_brilliant_scientist/directorate/directorate_background.dds.
- Parent-owned existing sprite name: GFX_kruger_directorate_background.
- Parent-owned suggested target GFX file: interface/016_brilliant_scientist_directorate.gfx.
- Parent-owned consumer: kruger_directorate_container expanded branch and kruger_directorate_full_panel.
- Preserve exact 500x360 geometry and all existing title, close control, portrait, name, meter, value, role, and footer rectangles.
- Parent visual review of the selected v3 candidate is complete and the parent installed the binary at the existing runtime path.
- The user owns live in-game acceptance; this worker did not launch the game and makes no live consumer acceptance claim.
