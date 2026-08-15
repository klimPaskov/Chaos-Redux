# Event 016 Directorate compact art handoff

Status: `needs_user_review` pending the parent-owned MCP GUI render of the compact consumer. The requested runtime background is complete and no blocker or substitute was used.

## Scope and ownership

The existing native ImageGen Directorate source was deterministically reprocessed into the compact runtime background. No new art was generated. No `.gfx`, `.gui`, localisation, gameplay, event, focus, decision, or spreadsheet file was edited. The parent owns final GFX/GUI wiring review and live consumer acceptance.

## Changed files

- `docs/assets/016_brilliant_scientist/directorate_ui/compact_refresh/source_png/directorate_background_master_v2.png` is the byte-identical retained source copy.
- `docs/assets/016_brilliant_scientist/directorate_ui/compact_refresh/processed_png/directorate_background.png` is the processed `500x360` preview.
- `gfx/interface/016_brilliant_scientist/directorate/directorate_background.dds` is the final `500x360` runtime DDS at the unchanged path.
- `docs/assets/016_brilliant_scientist/directorate_ui/compact_refresh/decoded_dds/directorate_background.png` is the decoded runtime preview.
- `docs/assets/016_brilliant_scientist/directorate_ui/compact_refresh/contact_sheets/directorate_background_safe_regions.png` is the safe-region processing review.
- `docs/assets/016_brilliant_scientist/directorate_ui/compact_refresh/contact_sheets/directorate_background_roundtrip_contact.png` is the processed-versus-decoded review.
- `docs/assets/016_brilliant_scientist/directorate_ui/compact_refresh/evidence/validation.json` records source, processed, runtime, header, alpha, dimensions, decoded equality, safe-region, and compact-header preservation evidence.
- `docs/assets/016_brilliant_scientist/directorate_ui/compact_refresh/process_compact_background.py` and `validate_compact_background.py` retain the deterministic processing and validation commands.
- `docs/assets/016_brilliant_scientist/directorate_ui/compact_refresh/manifest.md`, `gfx_handoff.md`, and `requirement_to_runtime.md` document the compact runtime row and parent boundary.
- `docs/assets/016_brilliant_scientist/directorate_ui/manifest.json` now points the active background row to the compact evidence and records `500x360`, current hashes, processing mode, and this handoff.
- `docs/assets/016_brilliant_scientist/directorate_ui/validation/row_validation.tsv` now records the active background row as `500x360`.
- `docs/assets/016_brilliant_scientist/directorate_ui/gfx_handoff.md` now identifies the compact `500x360` background and links the compact evidence.
- The earlier `background_refresh` manifest, crosswalk, and GFX handoff are marked superseded for the live background row while retaining the 500x620 historical candidate evidence.

## Runtime identity and hashes

| Item | Value |
| --- | --- |
| Sprite | `GFX_kruger_directorate_background` |
| Final DDS | `gfx/interface/016_brilliant_scientist/directorate/directorate_background.dds` |
| Target `.gfx` | `interface/016_brilliant_scientist_directorate.gfx` |
| Runtime dimensions | `500x360` |
| Runtime byte length | `720128` |
| Source PNG SHA-256 | `C748CECBB9D01ABF2B85F8B2D8A8987070D15ECE46F22C8CAA108039B471CF30` |
| Processed PNG SHA-256 | `381E2BA8C1A0B6DB21F2CEFC72BB6DA5DB30FE4FEB43B7A3DC5AC0AB51725056` |
| Runtime DDS SHA-256 | `C981DF3D82FEF7D8CBE7806FD4EBFE4E27908B6FA23A96F07F32F8ABE0984FF4` |

The compact header was not modified. `gfx/interface/016_brilliant_scientist/directorate/directorate_compact_header.dds` remains `500x58` with SHA-256 `F9ADEB2EE628DBBC5FD3F343E3D831930B133259E100932D2B92C43565791624`, matching the prior active manifest hash.

## Processing and conversion evidence

The source was resized to width `500` with aspect-preserving Lanczos resampling, producing a `500x619` intermediate, then deterministically top-sliced to `500x360`. A softened crop of the generated dark field was used as source-derived interior matte, and every locked functional rectangle was re-pasted from that same matte. The final PNG was converted with only `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` using `--width 500 --height 360`.

`evidence/validation.json` confirms the legacy uncompressed BGRA contract: magic `DDS `, header size `124`, width `500`, height `360`, pitch `2000`, pixel format offset `76`, pixel-format size `32`, flags `65`, zero fourCC, 32 bits, masks `0x00FF0000/0x0000FF00/0x000000FF/0xFF000000`, `DDSCAPS_TEXTURE=0x1000`, exact file length `720128`, and no mipmaps. Processed and decoded alpha ranges are `255..255`, and decoded DDS pixels equal the processed PNG exactly.

## Safe-region review

The locked rectangles were reviewed in window-local pixels: header title/subtitle `x=36..412/y=10..64`, collapse control `x=420..468/y=10..50`, portrait/frame `x=38..158/y=80..226`, portrait name `x=32..164/y=234..256`, meter rows `x=176..458/y=82..114`, `x=176..458/y=126..158`, `x=176..458/y=170..202`, and `x=176..458/y=214..246`, role/control line `x=36..464/y=270..300`, and footer direction line `x=36..464/y=322..346`.

Every locked rectangle is a quiet source-derived matte with no readable text, high-contrast ornament, fake control, painted meter, card, tab, or animation marker. Measured luminance ranges are `0..1` across all locked rectangles, with no rectangle exceeding a one-level range. Decorative apparatus is retained only on the outer frame and outside the locked rectangles. Cyan rectangles appear only in review contact sheets and are absent from the runtime PNG and DDS.

## Risks and parent review

The runtime background dimension changed from the earlier 500x620 candidate to the requested compact 500x360 surface, so the parent must render the named compact GUI consumer and check border alignment, clipping, and the supplied safe rectangles at the actual consumer resolution. The compact header remains preserved but was not recropped to the new background because the parent explicitly required retaining the compatible existing header.
