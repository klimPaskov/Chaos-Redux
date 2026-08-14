# IW-031 Kosovo sourced portrait source-placeholder handoff

Date: 2026-08-09.

## Scope and state

The three grounded male Kosovo portrait consumers are installed in explicit `source_placeholder` mode. Each identity uses an attributed archival source, an immutable Pillow exact crop, a deterministic 156x210 RGB candidate, and a one-level uncompressed BGRA DDS. No real-person likeness was generated or repainted, and RunPod was not accessed.

## Changed runtime files

- `common/characters/006_independence_wave_kosovo_characters.txt` defines `KOS_independence_wave_ferhat_draga` (civilian-large; centrism and oligarchism leader entries), `KOS_independence_wave_miladin_popovic` (civilian-large; marxism leader entry), and `KOS_independence_wave_shaban_polluzha` (civilian/army-large; despotism leader and mountain corps commander).
- `interface/006_independence_wave_iw031_kosovo_portraits.gfx` registers `GFX_portrait_KOS_independence_wave_ferhat_draga`, `GFX_portrait_KOS_independence_wave_miladin_popovic`, and `GFX_portrait_KOS_independence_wave_shaban_polluzha`.
- `localisation/english/006_independence_wave_kosovo_portraits_l_english.yml` provides names and descriptions in UTF-8 with BOM.
- `gfx/leaders/006_independence_wave/portrait_KOS_independence_wave_{ferhat_draga,miladin_popovic,shaban_polluzha}.dds` are the stable runtime textures.

The existing Kosovo package effects/triggers already reference these exact character tokens. No effects, triggers, events, focuses, decisions, country setup, history, flags, or unrelated UI were changed.

## Evidence and provenance

Active evidence: `docs/assets/006_independence_wave/iw031_kosovo_portrait_source_placeholder_2026_08_09/`.

Durable source archive: `docs/assets/portraits/006_independence_wave/iw031_kosovo_source_placeholders_2026_08_09/`.

The active manifest records source links, source dates, credits, rights statements, age/role/identity notes, crop boxes and hashes, candidate hashes, DDS hashes, owner-search results, review state, and replacement state. `research/commons_source_records.json` records Wikimedia Commons provenance and the installed-vanilla/current-project identity search. `crop_metadata/*.json` records `decoded_pixels_equal=true` from the required extraction utility. `review/iw031_kosovo_portraits_source_placeholder_native.png` and `review/iw031_kosovo_portraits_source_placeholder_4x_nearest.png` show candidate/DDS pairs; `review/dds_roundtrip_evidence.json` records decoded DDS pixel equality.

Source rows:

- Ferhat Bey Draga — Wikimedia Commons `File:Ferhat Bey Draga.png`, circa 1920, Public domain / PD-Yugoslavia; crop `[0,0,249,389]`.
- Miladin Popović — Wikimedia Commons `File:Miladin Popović i Enver Hodža.jpg`, circa 1943-1944, Public domain / PD other reasons; standing male at left; crop `[55,100,545,760]`.
- Shaban Polluzha — Wikimedia Commons `File:Shaban Polluzha.jpg`, named individual archival portrait reproduced in a 2021 exhibition photograph, Commons License: pd / Public domain with uploader/exhibition attribution and original photographer/date caveat; accepted crop `[0,0,3769,5070]`. The earlier group image `File:Shaban Polluzha me bashkëluftëtarë.jpg` (Commons PD-old-70 / PD-Art) and front-right crop `[1510,530,2110,1335]` are research-only and explicitly rejected because its caption says Polluzha is lying without a gun and does not identify that rifleman.

## Validation and review

- All three crops passed exact decoded-pixel equality against their masters.
- All candidates are `156x210` RGB and were produced by Pillow LANCZOS resize only; no recolour, retouch, padding, or repaint.
- All DDS files are `131168` bytes with valid `DDS ` magic, header size `124`, BGRA masks, `DDSCAPS_TEXTURE`, dimensions `156x210`, and alpha `255..255`; Pillow decoded round-trips equal their candidates.
- Rights/identity/age audit dispositions are explicit in `research/commons_source_records.json`: Ferhat and Miladin are PASS across all three checks; Shaban is PASS for identity, PASS WITH REPRODUCTION CAVEAT for rights, and PASS WITH DATE UNCERTAINTY for age. The independent visual sheet, `review/shaban_identity_position_review.png`, and `review/shaban_identity_position_review.md` confirm the accepted named individual portrait and the rejected group-image rifleman; the exhibition reproduction and unidentified original photographer/date remain documented caveats.
- No advisor, high-command, dossier, operative, small portrait, or gender-mismatched consumer exists.

## Replacement and blockers

`source_placeholder` is the accepted final state for this user request. The misidentified group-image front-right crop was removed from runtime and replaced at the same stable Shaban token by the clear individual Commons portrait. No source-placeholder consumer is blocked after that substitution. The later HOI4-style final gate remains fail-closed until the user supplies the replacement; the source archive must remain unchanged. Shaban's exhibition reproduction and unknown original date/photographer are the only remaining review qualifications.
