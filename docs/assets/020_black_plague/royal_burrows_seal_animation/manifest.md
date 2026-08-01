# Event 020 Royal Burrows Seal Animation

This package supplies the source-frame animation used by the shared `Seal the Royal Burrows` decision and the linked last-response refuge surface. It is a 2D decision-sprite package; it does not add a country tag, disease category, scripted GUI, or 3D model.

## Runtime contract

- Sprite: `GFX_decision_black_plague_seal_royal_burrows_animated`
- Definition: `interface/020_black_plague_response.gfx`
- Texture: `gfx/interface/animated/020_black_plague/royal_burrows_seal/black_plague_royal_burrows_seal_animation_sheet.dds`
- Sheet: 320x64 DDS, five 64x64 RGBA frames, 5 FPS, looping, played on show.
- Consumers: `black_plague_shared_seal_royal_burrows`, `black_plague_shared_start_last_response_refuge`, and `black_plague_shared_last_response_refuge_mission` in `common/decisions/020_black_plague_shared_response_decisions.txt`.
- Static fallback: `GFX_decision_black_plague_seal_royal_burrows` remains registered against `gfx/interface/decisions/020_black_plague/decision_seal_royal_burrows.dds`.

## Frame provenance

Frame 01 is the approved Royal Burrows seal source at `docs/assets/020_black_plague/source_png/decision_seal_royal_burrows_imagegen_source.png`. Frames 02-05 are individually generated source-frame variants from that image: sealing pulse, peak crown/eye glint, receding glow, and quiet reset. Each source is retained unchanged under `source_png/`; the vivid green backing is removed only in the processed runtime PNGs.

The animation is authored from independent image frames. It is not a transform-only animation, recolour, blur, or filter of one still image.

## Processing and evidence

- Processed frames: `processed_png/black_plague_royal_burrows_seal_frame_01.png` through `_05.png`.
- Processed sheet SHA-256: `d6306aa7e43cc107c70ebddd576c366306dce415db8d272e1c4ad74f6c9b390e`.
- Runtime DDS SHA-256: `0cdcc93742df0fd81c40aa6a362fd39f8b11c2ed9006b1bf65a4a85715b621a3`.
- Runtime DDS header: `DDS `, header size 124, flags 4111, height 64, width 320, pitch/linear size 1280.
- Review files: `previews/black_plague_royal_burrows_seal_contact_sheet.png` and `previews/black_plague_royal_burrows_seal_animation.gif`.

The source-frame package is complete for the current decision consumer. The remaining Event 020 blockers are gameplay depth, native-mission API review, release attribution, and focused live validation; no rat model production is required by the accepted scope.
