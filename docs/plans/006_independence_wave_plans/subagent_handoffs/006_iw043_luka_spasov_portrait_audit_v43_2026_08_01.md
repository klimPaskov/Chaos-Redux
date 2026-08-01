# IW-043 CHU Luka Semyonovich Spasov portrait audit v43

Date: 2026-08-01 (Europe/Kyiv).

Reviewer: `/root/event6_chu_spasov_audit_v43`, an independent sourced-visual audit subagent, separate from the package producer.

Scope: read-only audit of `docs/assets/006_independence_wave/chu_river_security_replacement_v41_2026_07_29/` against the real-person portrait gates in `chaos-redux-event-assets`.

No source, crop, repaint, processed PNG, review sheet, DDS, `.gfx`, character, history, localisation, or gameplay file was created, overwritten, or edited by this audit.

## Decision summary

`PASS` means the named gate is acceptable for this audit only and does not authorize runtime conversion or wiring.

| Gate | Verdict | Evidence and boundary |
|---|---|---|
| Commons and `PD-Russia-1996` rights | **PASS with provenance disclosure** | Commons raw metadata and API reconfirm `PD-Russia-1996`, `Public domain`, `Copyrighted=False`, and `AttributionRequired=false` for the 1938 `Ogoniok` scan; the author remains unknown, so retain the Commons URL and `Ogoniok` credit without inventing a photographer. |
| 1936 role and era fit | **PASS with era disclosure** | The archived Chuvash Encyclopedia records Spasov alive in 1936, Red Army service in 1919–1926, Chuvash ASSR SNK chairmanship in 1931–1932 and 1937–1938, and deputy chairmanship of the Nizhny Novgorod/Gorky regional executive committee in 1932–1937; the fictional River Security Directorate use is an institutional and Middle-Volga fit, not a claim that he historically held a river-police office or that the 1938 photograph is from 1936. |
| Immutable source master | **PASS** | The retained solo 1938 archival JPEG is intact, attributable to the Commons `Spasov LS` record, and is not a modern reenactment, film still, illustration, or substitute face. |
| Exact head-and-shoulders crop | **PASS** | The Pillow crop utility metadata proves decoded-pixel equality for rectangle `(50,10,850,1200)`; an independent Pillow replay also returned exact equality. |
| Source-locked identity-preserving ImageGen repaint | **PASS for visual likeness, subject to the separate evidence hold below** | The generation record states that the exact archival crop was the sole identity authority and that the leader reference was style-only; the repaint preserves the receding hairline, broad forehead, arched brows, deep-set unequal eyes, long straight nose, small moustache, compressed lips, rounded jaw, prominent right ear, apparent age, three-quarter pose, high collar, jacket, and shoulder angle without adding a second person, text, watermark, modern prop, or unsupported insignia. |
| HOI4 leader style | **PASS** | The candidate is a restrained muted painted full-size leader portrait with modeled facial planes, quiet background, period clothing, and no frame, UI, text, watermark, or photographic-only finish; the inspected role references are canonical leader portraits, not face sources. |
| Deterministic `156x210` candidate | **PASS** | The processed PNG decodes as opaque RGBA `156x210` with alpha extrema `255..255`; processing metadata records raw crop `[0,5,1077,1450]`, Lanczos scale to `156x210`, and the candidate hash. |
| Retained native and at-least-4x review evidence | **BLOCKED** | The retained `3120x840` sheet contains exact nearest-neighbour `4x` candidate and reference panels, but its metadata limits the `4x` claim to the candidate and canonical references; the archival crop and raw repaint occupy the first two fitted display slots and are not 4x nearest-neighbour panels. The skill requires the unchanged master, exact crop, raw result, candidate, and role references to be compared at native and at least `4x`, so a complete retained chain sheet is still required. |
| Ownership and collision scope | **PASS** | Exact and variant searches for `Spasov`, `Spassov`, `Spasoff`, `Luka Semyonovich Spasov`, and the Cyrillic forms found no same-person character, recruitment, portrait, GFX, interface, history, or localisation owner in the current project, installed vanilla, Kaiserreich `1521695605`, or approved mods `2265420196` and `1458561226`; incidental `Lukash`/`Lukas` hits are not identity matches. |
| Advisor, dossier, small, commander, and operative boundary | **PASS** | The consumer defines only a male `civilian.large` portrait and the package contains no advisor, high-command, dossier, `65x67`, `_small`, commander, operative, or navy derivative. No such art is authorized by this audit. |
| Durable ComfyUI portrait pair | **BLOCKED** | No matching source/prompt pair exists under `docs/assets/portraits/`; the duplicate raw PNG on `docs/assets/006_independence_wave/portraits_generated_png/` is not the required durable pair. |
| Runtime admission and DDS | **BLOCKED** | The candidate has no DDS in the package and the existing runtime DDS is an older untouched file at the stable path; standard conversion and wiring must wait for the retained review-evidence and durable-pair gates. |

Overall disposition: **BLOCKED for runtime admission, not blocked on source rights, 1936 role fit, exact crop, visual identity, style, dimensions, ownership, or consumer boundary.** The candidate remains evidence-only until the complete review chain and durable portrait pair are supplied and independently re-admitted.

## Source rights and role evidence

The immutable source is `docs/assets/006_independence_wave/chu_river_security_replacement_v41_2026_07_29/source_files/chu_luka_spasov_1938_ogoniok.jpg`, native `900x1218` RGB JPEG, SHA-256 `C707F7F9C50DAE4F4EC0F91865E0DE97875367F95D0659039BC52F17B5799457`.

The Commons file page is <https://commons.wikimedia.org/wiki/File:Spasov_LS.jpg>, the direct original is <https://upload.wikimedia.org/wikipedia/commons/5/50/Spasov_LS.jpg>, and the raw metadata is <https://commons.wikimedia.org/w/index.php?title=File:Spasov_LS.jpg&action=raw>.

On 2026-08-01 the raw record returned HTTP 200 with `date=1938`, source `Журнал «Огонёк» № 3 от 1938 год`, author `unknown`, and license template `{{PD-Russia-1996}}`.

The Commons API also reported `900x1218`, `LicenseShortName=Public domain`, `UsageTerms=Public domain`, `Copyrighted=False`, and `AttributionRequired=false`.

The rights verdict is a Commons-recorded public-domain status, not a claim that the unknown photographer can be named or that a different jurisdiction has a separate licence requirement.

The archived Chuvash Encyclopedia record is <https://web.archive.org/web/20240518043403/http://enc.cap.ru/?t=prsn&lnk=4532>.

Its text identifies Luka Semyonovich Spasov as a state official born in 1899 and deceased in 1955, records Red Army service from 1919 to 1926, Chuvash ASSR SNK chairmanship from February 1931 to February 1932 and September 1937 to July 1938, and deputy chairmanship of the Nizhny Novgorod/Gorky regional executive committee from 1932 to 1937.

Those dates place him alive and active in the Middle-Volga/Chuvash administrative and military context in the 1936 baseline.

The retained `1938` source is two years after the baseline, but it is period-matching Soviet material and the subject was active in the baseline; it must not be described as a documented 1936 uniform photograph.

The package correctly avoids an unsupported personal-ethnicity claim and uses the River Security Directorate as a fictional institutional consumer.

## Immutable crop and processing evidence

| Evidence | Path | Dimensions and mode | SHA-256 |
|---|---|---|---|
| Source master | `docs/assets/006_independence_wave/chu_river_security_replacement_v41_2026_07_29/source_files/chu_luka_spasov_1938_ogoniok.jpg` | `900x1218` RGB JPEG | `C707F7F9C50DAE4F4EC0F91865E0DE97875367F95D0659039BC52F17B5799457` |
| Exact crop | `docs/assets/006_independence_wave/chu_river_security_replacement_v41_2026_07_29/source_crops/CHU_river_security_directorate_luka_spasov_head_shoulders.png` | `800x1190` RGB PNG | `E797C1C906F2DD3A3D1B37D0BFADB816B326C267DA060A07392622E5A06D096B` |
| Crop metadata | `docs/assets/006_independence_wave/chu_river_security_replacement_v41_2026_07_29/crop_metadata/CHU_river_security_directorate_luka_spasov_crop.json` | JSON, Pillow utility v1.0 | `6ACBCA3EB0410A5E7C1CD37E3027C3A7199935414DD33382793207DC3365484F` |
| Raw ImageGen repaint | `docs/assets/006_independence_wave/chu_river_security_replacement_v41_2026_07_29/repaints_raw/CHU_river_security_directorate_luka_spasov_hoi4_repaint_v1.png` | `1077x1460` RGB PNG | `BF2E248DF9DA63E9A3E0DEC9CB9289D2B8C3637F9E91BA9CB47DF7668EB9E627` |
| Processed candidate | `docs/assets/006_independence_wave/chu_river_security_replacement_v41_2026_07_29/repaints_processed/CHU_river_security_directorate_luka_spasov_156x210_candidate.png` | `156x210` RGBA PNG, alpha `255..255` | `48460E5F65017DF24D23596F8B6AB9E889ABDC3867C5ADB872283C6015381DE6` |
| Processing metadata | `docs/assets/006_independence_wave/chu_river_security_replacement_v41_2026_07_29/processing_metadata/CHU_river_security_directorate_luka_spasov_156x210.json` | JSON, candidate-pending status | `D682E81758F0A68CB63618D4053E617CC83C4A75AA17626E6AC4849FA08F90FC` |
| Review sheet | `docs/assets/006_independence_wave/chu_river_security_replacement_v41_2026_07_29/review/CHU_luka_spasov_source_raw_candidate_references_4x.png` | `3120x840` RGB PNG | `2A1F0C70FDB6D84E14315A965E7A4B2E7DA7D9F5EAE77F5B1893F41D70516221` |

The crop JSON records master-to-crop rectangle `(50,10,850,1200)`, decoded RGBA equality, and equal decoded-pixel hashes `551a7ce4e393cf8209d72b6542510c4a947cc5bef94424be4df5526a354c8821` for the expected crop and output.

An independent Pillow replay decoded the JPEG as RGB, applied that same rectangle, decoded the retained PNG as RGB, and returned `equal=True` for all `952000` pixels.

The raw ImageGen record is `docs/assets/006_independence_wave/chu_river_security_replacement_v41_2026_07_29/CHU_luka_spasov_imagegen_record.md`, SHA-256 `40650AB72400735B53AD83709B693B206412F247B04562A45C998EC0972ECAF5`.

The raw result is also duplicated byte-for-byte at `docs/assets/006_independence_wave/portraits_generated_png/CHU_river_security_directorate_luka_spasov_hoi4_repaint_v1.png` with the same SHA-256 `BF2E248DF9DA63E9A3E0DEC9CB9289D2B8C3637F9E91BA9CB47DF7668EB9E627`; that duplicate is evidence only and is not a runtime file or durable ComfyUI pair.

## Independent visual review

The source and exact crop show one identifiable male with the distinctive receding dark hairline, broad forehead, arched brows, unequal deep-set eyes, long straight nose, small moustache, compressed mouth, rounded jaw, prominent viewer-right ear, three-quarter orientation, high collar, jacket, and shoulder line.

The raw repaint preserves those source-visible cues and the same shoulder angle and expression while removing only the newspaper halftone texture for a painted strategy-game treatment.

At native `156x210`, the candidate remains readable as a head-and-shoulders leader portrait and does not become a generic modern officer when the hair and coat are discounted.

The candidate is darker and more heavily brushed than the inspected references, but it remains within the subdued painted leader family and retains facial readability.

The reviewed style-only references are `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/den_thorvald_stauning.png`, `156x210` RGBA, SHA-256 `08732002182BDCB2BFF3D78B142CC2B3D75ADBDB29D4115F9E89CA5BDC6A21B6`, and `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/fin_carl_mannerheim.png`, `156x210` RGBA, SHA-256 `7E78E33E0B691B96B584393F2D363C07A302320F7E6300BDA0FFF261AA98D49E`.

The canonical leader reference contact sheet inspected before this audit is `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/contact_sheet.png`, `1200x498` RGBA, SHA-256 `8966AE351D1FE8FC13D47CA1C59EC3D8A34DA9101CE5FD65F7ACFF3421BD0401`.

No facial substitution, beautification, eye opening, invented decoration, unsupported rank mark, text, watermark, modern UI, or second subject was observed in the raw repaint or candidate.

The visual likeness and HOI4-style verdicts therefore pass for this independent read, but the retained evidence package still fails the separate all-five native-plus-`4x` review-evidence gate described below.

## Review-sheet evidence limitation

Exact pixel search of the retained sheet finds the candidate's nearest-neighbour `4x` enlargement at sheet x=`1248`, the Thorvald Stauning reference at x=`1872`, and the Carl Mannerheim reference at x=`2496`, each `624x840` from a native `156x210` source.

The first two `624x840` display slots contain the archival crop and raw repaint fitted to the sheet height, while the source crop is native `800x1190` and the raw repaint is native `1077x1460`.

The package metadata explicitly says `4x nearest-neighbour for candidate and canonical references`, not for the unchanged master, exact crop, or raw ImageGen result.

The source, crop, raw result, candidate, and references were each inspected as separate native files for this audit, but the skill requires retained native and at-least-`4x` comparisons for every member of the chain.

This is an evidence-completeness blocker rather than a finding that the face has failed likeness.

## Ownership and consumer boundary

The current consumer is `CHU_independence_wave_river_security_directorate` in `common/characters/006_independence_wave_iw043_iw058_characters.txt:41-49`.

It declares `gender = male` and only `portraits = { civilian = { large = GFX_portrait_CHU_independence_wave_river_security_directorate } }`.

The stable sprite is `GFX_portrait_CHU_independence_wave_river_security_directorate` in `interface/006_independence_wave_iw043_iw058_portraits.gfx:23-25`, pointing to `gfx/leaders/006_independence_wave/portrait_CHU_independence_wave_river_security_directorate.dds`.

The current route promotes the character for the emergency-guard and emergency-military branches in `common/scripted_effects/006_independence_wave_iw043_iw058_package_effects.txt:396-402`.

Exact and variant ownership searches covered current `common/characters`, `history/countries`, `gfx/leaders`, `interface`, and `localisation`, installed vanilla equivalents, Kaiserreich `1521695605`, and approved mods `2265420196` and `1458561226`.

No exact or transliterated `Spasov`/`Spassov`/`Spasoff` owner was found, and no Cyrillic `Спасов`/`Лука Сем` owner was found in those owner and consumer roots.

The existing stable runtime DDS is `gfx/leaders/006_independence_wave/portrait_CHU_independence_wave_river_security_directorate.dds`, `131168` bytes, decoded by Pillow as `156x210` RGBA DDS, SHA-256 `1F18B313E52B81FB7F74CEA957D94DFF6667D22D84C68E7E6B1ED7C31D2FFD79`.

That DDS was not created or replaced by this audit and must not be counted as approval of the candidate.

No ownership transfer guard is needed for Spasov because no same-person owner was found in the scanned roots, but the parent still owns final consumer admission and must preserve the one-character, one-civilian-large boundary.

## Advisor and small-art exclusion

The package file list contains only the immutable JPEG, exact crop, raw repaint, `156x210` candidate, review sheet, metadata, and source records.

No advisor template, high-command card, dossier frame, `65x67` texture, `_small` portrait, `50x67` commander source, operative texture, or unrelated derivative is present or authorized.

The current character definition confirms that no advisor or small-art consumer exists for this subject.

## Parent next steps

1. Preserve the source master, exact crop, raw repaint, processed candidate, metadata, review sheet, and their hashes without replacement.

2. Retain a compliant comparison package containing the unchanged archival master, exact crop, raw ImageGen result, `156x210` candidate, and both role references at native and at least `4x` nearest-neighbour scale, then obtain a fresh independent likeness/style/provenance verdict.

3. Create the required durable ComfyUI source/prompt pair under `docs/assets/portraits/006_independence_wave/` using the exact runtime basename `portrait_CHU_independence_wave_river_security_directorate`; use a lossless high-resolution subject PNG and a name-free prompt derived from the portrait-description instruction, while retaining the immutable source and provenance separately.

4. After the review-evidence and durable-pair gates pass, run only the repository-standard converter on the processed `156x210` PNG to the existing stable DDS path, validate the DDS header, dimensions, exact length, and alpha, and keep the existing sprite name and `.gfx` path stable.

5. Update the manifest and handoff state from `processed_audit_pending` only after those gates are actually complete, and remove the stale instruction that the already-created exact crop still needs to be created.

No fallback identity, generic portrait, advisor/small derivative, cross-mod art, DDS, `.gfx` edit, localisation edit, or gameplay edit is authorized by this audit.

## Audited package documentation hashes

| File | SHA-256 |
|---|---|
| `docs/assets/006_independence_wave/chu_river_security_replacement_v41_2026_07_29/manifest.md` | `F887FDB1041410151B24EA86D2C53512138B75C69D74E5DA244774EF2BF9DA28` |
| `docs/assets/006_independence_wave/chu_river_security_replacement_v41_2026_07_29/gfx_handoff.md` | `2EC4CF44220FFBA481BFD709AE31A930422044C20A89158A39C01604528397F4` |
| `docs/assets/006_independence_wave/chu_river_security_replacement_v41_2026_07_29/source_records/commons_spasov_metadata.md` | `EB5F92A3A185913DC1E84EF875F88C435930F34240FB50E3BE4690680A0F60D0` |
| `docs/assets/006_independence_wave/chu_river_security_replacement_v41_2026_07_29/source_records/chuvash_encyclopedia_spasov.md` | `AE1E8DE62EAF305F945E58C6FA6052A7BCCBAEF88BF17AF7B7D6EDC978AF77AF` |
