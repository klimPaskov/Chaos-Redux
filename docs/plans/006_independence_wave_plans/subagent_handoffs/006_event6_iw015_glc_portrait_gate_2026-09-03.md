# Event 006 IW-015 GLC Castelao portrait gate

Date: `2026-09-03` (Europe/Kyiv; filesystem and Internet verification performed 2026-09-01).

Owner: `chaosx_portrait_creator`.

Scope: bounded audit of the existing Alfonso Daniel Castelao portrait consumer for Event 006 package `iw_015`, carrier `GLC`, anchor state `171`, including source attribution, rights/date/style terminology, source/crop/processed evidence, runtime DDS identity, portrait-specific GFX, and the current no-additive roster repair.

## Disposition

`NO-CHANGE / CURRENT CONSUMER RECONCILED / LIFECYCLE TERMINOLOGY HELD FOR PARENT`.

The current consumer is the existing vanilla GLC liberal country-leader role `Alfonso Daniel Castelao`, not an Event 006 additive corps commander. The 2026-08-30/31 exact-input authority records the selected GLC row as grounded `source_placeholder`, while the historical 2026-08-26 user-supplied audit records the same physically painted runtime output as `styled_final`. Both records are retained; this gate does not relabel evidence, promote a provider-backed final, set `replacement_pending`, alter image bytes, or widen package admission.

The portrait-specific runtime mapping is already safe at the identity level: `GFX_portrait_GLC_alfonso_daniel_castelao` points to the stable GLC DDS and is applied only during the package-generation roster checkpoint to the existing liberal Castelao role. Cleanup restores vanilla `GFX_portrait_Alfonso_Daniel_Castelao`. No new character, recruitment entry, GFX definition, runtime file, fallback, or substitute was created.

## Exact consumer and wiring evidence

- Vanilla `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/GLC - Galicia.txt:84-88` creates `Alfonso Daniel Castelao` with `picture = GFX_portrait_Alfonso_Daniel_Castelao`, `expire = "1965.1.1"`, and `ideology = liberalism`.

- Vanilla `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/_leader_portraits.gfx:7945-7948` defines `GFX_portrait_Alfonso_Daniel_Castelao` with the vanilla generic texture.

- `common/scripted_triggers/006_independence_wave_iberian_package_triggers.txt:68-69` proves the preserved non-ruling-only Fuco Gómez and Alfonso Daniel Castelao roles for IW-015; `:82-87` repeats the preserved roster contract and explicitly states that no second corps-command character is recruited.

- `common/scripted_effects/006_independence_wave_effects.txt:3246-3263` applies `GFX_portrait_GLC_alfonso_daniel_castelao` with `set_country_leader_portrait` once per package generation after the preserved roster proof.

- `common/scripted_effects/006_independence_wave_iberian_package_effects.txt:479-484` restores vanilla `GFX_portrait_Alfonso_Daniel_Castelao` during setup reset, and `:637-642` restores it during generation cleanup.

- `interface/006_independence_wave_portraits_registry.gfx:149-152` owns `GFX_portrait_GLC_alfonso_daniel_castelao` and points only to `gfx/leaders/006_independence_wave/portrait_GLC_alfonso_daniel_castelao.dds`.

- Current scans find no Castelao identity in `common/characters/006_independence_wave_characters_registry.txt` or `history/general/006_independence_wave_character_recruitment_registry.txt`; the former `GLC_independence_wave_alfonso_daniel_castelao` additive character/recruitment consumer is absent. `localisation/english/006_independence_wave_iberian_l_english.yml` has no named Event 006 Castelao character strings requiring change.

## Grounded source and provenance

Source page: <https://commons.wikimedia.org/wiki/File:Castelao_Vida_Gallega_442.png>.

Direct media: <https://upload.wikimedia.org/wikipedia/commons/9/91/Castelao_Vida_Gallega_442.png>.

The current Commons page returned HTTP 200 on 2026-09-01 and identifies the file as a portrait from `Vida gallega`, issue 442, with source record `Vida gallega : ilustración regional: Ano XXII Número 442 - 1930 marzo 10` and Galiciana/Biblioteca Dixital de Galiza attribution. The page exposes `Date: Unknown date` and `Author: Unknown author`, categories `Unknown date`, `Template Unknown (author)`, `CC-PD-Mark`, and `Author died more than 80 years ago public domain images`, and a Public domain/PD-old-80 notice. Its page-level HTML also carries a `rel=license` CC BY-SA 4.0 link; this is not treated as a file-specific release and does not resolve the unknown scan-chain rights.

The current direct media is `620x634` RGB, `659580` bytes, SHA-256 `a47fa46b3b2aeb08af2b9292fc93099cc332471c3ac35d2749b8050495a16cbe`, with decoded RGBA pixel SHA-256 `b4562b09ca7b28e9e5defb02d1260cedcfe305a289f205301473173439400c68`. The durable archive master `docs/assets/portraits/006_independence_wave/portrait_GLC_alfonso_daniel_castelao_source.png` is `620x634` mode `L`, `309688` bytes, SHA-256 `e022556b94a983f590dc2accde2dc6d6261fbe19369f688e4cca2f0adcdaa242`, and has the same decoded RGBA pixel SHA-256, proving the archived source pixels match the currently fetched Commons media despite PNG encoding/channel-mode differences.

The exact source crop remains `docs/assets/006_independence_wave/source_placeholder_2026_08_05_iberian/crops/portrait_GLC_alfonso_daniel_castelao_source_crop.png`, `464x622` mode `L`, SHA-256 `1fb10ebf8c7f5d9e97f81d1ed93a7442cbf9f83561e911a1c65a09f68b8ff232`, extracted from half-open master rectangle `[88,8,552,630]`. Its metadata `metadata/portrait_GLC_alfonso_daniel_castelao_source_crop.json` has SHA-256 `96c478d707ae72613ca1f0ce4537696d4d2c01bb99cd84b309e718df39ac8f17`, reports `status = exact_source_crop_verified` and `decoded_pixels_equal = true`, and the durable archive currently retains the source master rather than a separate cropped file.

The deterministic source-placeholder processing record `processing_metadata/portrait_GLC_alfonso_daniel_castelao_156x210.json` has SHA-256 `d107a106b144f09e3cbbbd354e0402b03589684133b21158a62eaf596ae0ed29`; its direct LANCZOS resize output `processed_png/portrait_GLC_alfonso_daniel_castelao.png` is `156x210` RGB, SHA-256 `80f77a25c4c30fae67aefab7619aae390983afa22d2685d27746eb3d96df90c6`. The archived source-placeholder DDS is `131168` bytes, SHA-256 `33aa76c4bbcbb87e7f9ce1508beadee4799a558a429f92b4d5ac8fc09c4a4b7f`, and decoded RGBA SHA-256 `f4c5240dec022af29b5753606615589abd81e12e8aaa64850095569ca4949001`.

## Supplied runtime output and terminology evidence

The user-supplied PNG at `C:\Users\klimp\Documents\ComfyUI Workflows\HOI4\hoi4_portraits_output\output\156x210\iw\portrait_GLC_alfonso_daniel_castelao_source_00002.png` is `156x210` RGB, `103023` bytes, SHA-256 `5b99fdf9002e571a74d7e5d0b15ce3785f6e27cef878a69d55cde4706b418465`, and decoded RGBA SHA-256 `7299c7af5cf5e6ada7dc01d448d11835f54c25e8b9f3da131c3888928f102537`. Visual inspection shows a painted color head-and-shoulders portrait with period clothing and glasses, so it is not the unchanged monochrome source crop.

The matching user-supplied DDS at `C:\Users\klimp\Documents\ComfyUI Workflows\HOI4\hoi4_portraits_output\output\156x210\iw\dds\portrait_GLC_alfonso_daniel_castelao_source_00002.dds` and the stable runtime DDS are byte-identical: `156x210`, `131168` bytes, uncompressed 32-bit BGRA, pitch `624`, no mipmaps, opaque alpha, SHA-256 `15f9ca69d7536439d2421dd8d55c96e94b5c56f9cdeb5ae5ee6a6210aaf25237`, decoded RGBA SHA-256 `7299c7af5cf5e6ada7dc01d448d11835f54c25e8b9f3da131c3888928f102537`. The current runtime therefore contains the supplied painted output, not the archived source-placeholder DDS; this fact is recorded without resolving the parent-owned lifecycle vocabulary.

The supplied PNG embeds `workflow_id = hoi4_portrait_batch`, `revision = 0`, `Hoi4BatchInput`, the prompt `make this portrait hoi4_portrait style`, `Hoi4SaveDDS` `argb8888`, `master_size = 1024x1365`, `game_size = 156x210`, `base_model = flux-2-klein-9b-fp8.safetensors`, and `style_lora = hoi4_portrait_flux2_klein_9b_lora_000002500.safetensors`. No provider/job receipt or RunPod receipt is present, so this gate does not independently promote the output to a provider-backed `styled_final` under the portrait skill contract.

The current 2026-08-30 wiring reconciliation and 2026-08-31 portrait consumer gate call selected exact-input rows grounded `source_placeholder` and explicitly retain the older 2026-08-26 `styled_final` wording as a parent decision. The 2026-08-26 user-supplied audit remains historical evidence of the painted output and its embedded ComfyUI process metadata; neither record was rewritten here.

## Framing and review

The existing review files `review/portrait_GLC_alfonso_daniel_castelao_comparison_sheet.png` (SHA-256 `c62e90dc4335a82a3a2edce2616a3855cece7d0d4f4946f67d26a6c51b079f34`) and `review/portrait_GLC_alfonso_daniel_castelao_native_4x_processed_vs_dds.png` (SHA-256 `1c1f3acd04cbff621969e7837af9f971a3052d8406972c6e13bb20f7ed34db70`) compare the source master, exact crop, source-placeholder processed/DDS round-trip, and canonical installed leader references at native and enlarged scale. The source-placeholder crop and DDS round-trip preserve the source-visible face, glasses, halftone texture, and head-and-shoulders framing; the supplied runtime output is visibly painted and retains a matching glasses/bow-tie/jacket presentation. The installed role family was checked against `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/` and its canonical `156x210` leader contact sheet.

No independent likeness, framing, or rights reviewer is assigned. The visual review is producer evidence only; the exact source crop equality and DDS validation are machine-checked evidence.

## Rights, date, and admission blockers

- Rights remain `PASS_WITH_CAVEAT / NEEDS_USER_REVIEW`: Commons exposes a Public domain/CC-PD-Mark/PD-old-80 notice, but records the original author as unknown and does not establish the exact scan-chain jurisdiction. The supplied painted output adds no licence grant.

- Date evidence is period-compatible through the Galiciana source record's 10 March 1930 issue date, but Commons' structured Date field is `Unknown date`; no stronger capture-date receipt was found. The preserved vanilla 1936 Castelao role is an existing package identity proof, not a new independent source/date receipt.

- Lifecycle terminology remains a parent decision because the current matrix says `source_placeholder` while the older supplied-output audit says `styled_final`; no evidence was silently relabelled and no new `replacement_pending` request was inferred.

- GLC Alexandre Bóveda remains an unmapped supplied input and cannot be substituted onto the Castelao key. IW-015 remains adapter-only and fail-closed for independent rights, package, AI/probability, MCP, central-attestation, and related country/flag gates.

## Changed files and skipped checks

Changed only portrait documentation and this handoff: `docs/assets/006_independence_wave/source_placeholder_2026_08_05_iberian/manifest.md` received a dated current-consumer/lifecycle amendment, `docs/assets/006_independence_wave/source_placeholder_2026_08_05_iberian/gfx_handoff.md` received a dated current-consumer clarification, and this file was added. The two asset documentation files are under the repository's ignored `docs/assets/` path; no image bytes were changed.

No character, recruitment, scripted effect, scripted trigger, country history, localisation, GFX definition, runtime DDS, source master, crop, processed PNG, or admission/attestation surface was changed. No fallback, invented identity, generic substitute, source relabelling, RunPod operation, ImageGen call, live game/MCP execution, or commit/staging action was performed.

The existing DDS validation JSON reports `status = pass` for the archived source-placeholder conversion, including `156x210`, exact `131168` byte length, 32-bit BGRA masks, no mipmaps, opaque alpha, evidence-copy equality for that historical conversion, and decoded-pixel equality to its processed PNG. Its recorded historical runtime-copy hash is not validation of the current runtime DDS, whose independently inspected hash is `15f9ca69d7536439d2421dd8d55c96e94b5c56f9cdeb5ae5ee6a6210aaf25237` and whose decoded pixels match the supplied user DDS. The converter `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` was not rerun because this gate made no byte or mapping change; no new conversion evidence is claimed.

Required offline Paradox wiki core pages and relevant vanilla effects/triggers documentation were consulted for the country-leader/portrait consumer contract. No HOI4 MCP route was invoked because this was a portrait-only documentation audit with no in-scope event, GUI, map, focus, or weighted-logic edit.

The default web page/search adapter timed out during this audit; a direct read-only HTTPS fetch of the cited Commons page and original media returned HTTP 200 and supplied the current page/media evidence recorded above. No Paradox wiki web access was used.
