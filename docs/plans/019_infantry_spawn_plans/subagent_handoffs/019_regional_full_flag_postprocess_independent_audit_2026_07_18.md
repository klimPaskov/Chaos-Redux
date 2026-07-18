# Event 019 regional full-flag post-production independent audit

Date: 2026-07-18  
Auditor: independent post-production visual/provenance auditor (not the producer)  
Scope: the 13 identities x 7 regions Event 019 regional full-flag matrix (91 tags, 273 runtime TGAs).  
Write scope: this handoff only; no asset, processor, GFX, gameplay, localisation, spreadsheet, or other documentation file was edited.

## Final verdict

**FAIL — do not approve or promote the candidate.**

The current 91-row visual/runtime candidate itself has no concrete row-level artwork failure in the reviewed ladders. It is not approvable as a package because current source-of-truth documentation still presents the superseded 2026-07-16 `regional_variants` motif-composite pipeline as the current source, the main manifest says `complete` while the current validation remains `candidate_requires_independent_visual_review`, and seven retained GHOST_BASE rows explicitly lack their exact original ImageGen prompt text. The parent may promote only after the remediation below and a fresh review of the corrected provenance/documentation surfaces.

## Review basis and visual evidence

I reviewed the relevant flag rules in `chaos-redux-event-assets/SKILL.md` (section 20: flat ImageGen-authored flag masters, readable 82x52/41x26/10x7 ladders, no fabric/poles/scenes/text/watermarks, and no locally drawn design). The parent-provided Event 019-only deterministic spot-colour exception was treated as the only allowed processing exception.

The following sheets were inspected visually, not accepted merely from machine PASS values:

- `docs/assets/019_infantry_spawn/contact_sheets/event_019_regional_full_flag_claimant_zombie_raw_contact_sheet.png` (35 raws; SHA-256 `e2d731418d9269080ba5e669bbffa80da87d2fce383f33ec930ec819820b2df9`).
- `docs/assets/019_infantry_spawn/contact_sheets/event_019_regional_full_flag_ghost_raw_contact_sheet.png` (28 raws; SHA-256 `9a85fde7dbd0f4b088c991b0c72c142dda01211f7b35ca5ca54e73be19a6bff1`).
- `docs/assets/019_infantry_spawn/contact_sheets/event_019_regional_full_flag_golem_raw_contact_sheet.png` (28 raws; SHA-256 `0fe26cd80a61a9f247c2ac44e6e5bb0ebaaad767ab19de33371f8369b21c2a5d`).
- `docs/assets/019_infantry_spawn/contact_sheets/event_019_regional_full_flag_raw_spot_contact_sheet.png` (raw + 820x520 spot-master pairs; SHA-256 `f0945b9e508e493372405b52a58806cc41ca950df1e654d054885382d89c6aa1`).
- `docs/assets/019_infantry_spawn/contact_sheets/event_019_regional_flag_contact_sheet.png` (normal/medium/small ladders; SHA-256 `e83e0b59c946828dd7d9ce46250d8218a93f8996f2db74bcea2cec367ce65837`).
- `docs/assets/019_infantry_spawn/contact_sheets/event_019_regional_flag_small_readability_contact_sheet.png` (all 91 10x7 outputs; SHA-256 `c65c163dbe1a558589dbb9c51cc7fadffd52d58942d982e37d463e58ef6b1d64`).

All 91 rows were checked across raw, spot-master, normal, medium, and small review surfaces. Every reviewed row is a flat/orthographic full-bleed design. The identity silhouette and regional accent remain visually distinct, family colour survives the ladder, and no row swap was observed. The raw and processed sheets show no human figure, real-world flag, readable text, watermark, fabric, pole, scenery, perspective, harmful noise, or processing artifact. Zombies read as undead/tally/crown/collective/spiral families; ghosts read as spectral anchor/crown/mask/moon-door families; golems read as mineral/rune/fist/boot/tile/colossus families.

## Row-level visual matrix

`V` means visual PASS at raw/spot/82x52/41x26/10x7. There were no concrete art failures in the 91 cells. `V*` carries the separate GHOST_BASE prompt-provenance caveat below; it is not a visual defect.

| Identity | EUROPE | MIDDLE_EAST | AFRICA | ASIA | AUSTRALIA | NORTH_AMERICA | SOUTH_AMERICA |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CLAIMANT_BREAKAWAY | V | V | V | V | V | V | V |
| ZOMBIE_BASE | V | V | V | V | V | V | V |
| ZOMBIE_CLAIMANT | V | V | V | V | V | V | V |
| ZOMBIE_COLLECTIVE | V | V | V | V | V | V | V |
| ZOMBIE_SPECIES | V | V | V | V | V | V | V |
| GHOST_BASE | V* | V* | V* | V* | V* | V* | V* |
| GHOST_CLAIMANT | V | V | V | V | V | V | V |
| GHOST_COLLECTIVE | V | V | V | V | V | V | V |
| GHOST_SPECIES | V | V | V | V | V | V | V |
| GOLEM_BASE | V | V | V | V | V | V | V |
| GOLEM_CLAIMANT | V | V | V | V | V | V | V |
| GOLEM_COLLECTIVE | V | V | V | V | V | V | V |
| GOLEM_SPECIES | V | V | V | V | V | V | V |

### Row-level concerns

- **MEDIUM, provenance-only, seven rows:** `INFANTRY_SPAWN_GHOST_BASE_EUROPE`, `..._MIDDLE_EAST`, `..._AFRICA`, `..._ASIA`, `..._AUSTRALIA`, `..._NORTH_AMERICA`, and `..._SOUTH_AMERICA`. `prompts/regional_full_flag_ghost_prompts_2026_07_18.md` explicitly says the exact prior ImageGen call text was not preserved and the displayed prompt is a reconstruction from identity/region contracts. The retained ImageGen handles, raw bytes, dimensions, and hashes are exact, and the visual rows pass, but exact prompt provenance is not provable. Remediation: recover and retain the original prompt records if available; otherwise leave these seven rows explicitly provenance-incomplete and obtain parent/user acceptance before promotion. No regenerated or fallback source is authorized by this audit.

No other tag has a row-level visual, mapping, source-hash, or runtime-contract concern.

## Independent provenance and runtime checks

Evidence reviewed: `docs/assets/019_infantry_spawn/_tooling/process_event_019_regional_flags.py`, `regional_flag_validation_2026_07_18.json`, `regional_flag_checksums_2026_07_18.sha256`, the three 2026-07-18 prompt/provenance notes, and the three producer handoffs.

- Matrix mapping independently recomputed: 13 identities x 7 regions, 91/91 records; every record tag equals `INFANTRY_SPAWN_<identity>_<region>`, with 7 rows per identity and 13 rows per region. No accidental row swap.
- All 91 owned raws decode as opaque RGB PNGs. Every owned raw is byte-equal to its recorded built-in ImageGen result path and recorded SHA-256; all 91 raw hashes are distinct. Prompt record paths, tag references, handles, dimensions, modes, and raw paths resolve for all 91 rows.
- Current processor is the exact recorded `docs/assets/019_infantry_spawn/_tooling/process_event_019_regional_flags.py`, SHA-256 `d87e879184d5a28a52736b80af4bc0ce70abd9744de47210b1f6a7c3db15ece6`. Recorded runtime is Python 3.9.12, Pillow 11.1.0, NumPy 2.0.2, with 820x520 full-frame normalisation, 8-colour deterministic HSV-family collapse, hue bins 16, neutral saturation 64, dark value 48, minimum colour share 0.0005, no dithering, and nearest recorded spot-colour runtime resampling. The 7/18 command and arguments are present in the JSON evidence.
- All 91 spot masters exist at 820x520 RGB, are byte-distinct, and are the current processed masters. All 273 processed PNGs exist at exact 82x52/41x26/10x7 RGBA dimensions, are opaque, use only their recorded palette, and have no missing rows.
- All 273 runtime TGAs match their JSON hashes and the 273-line checksum file. Independent checks found exact type-2 uncompressed 32-bit headers, bottom-left origin (`descriptor = 8`, x/y origin zero), exact lengths (17074/4282/298 bytes), opaque alpha, and decoded pixel equality to each paired PNG. The 7/18 validator also records no `file(1)` top-origin markers; no current runtime path is a DDS or old-composite substitute.
- Current validation status is correctly `candidate_requires_independent_visual_review`; its machine checks are all true. Machine PASS was not used as visual approval.

## Package-level documentation failures and remediation

These are the reasons for the overall FAIL despite the 91-row visual/runtime PASS.

1. **HIGH — current manifest presents superseded sources as current for all 91 rows.** `docs/assets/019_infantry_spawn/manifest.md` lines 105–121 describe the 7/16 regional-motif compositing pipeline, say it produced the 91 `source_png/flags/regional_variants/` composites, and point to the 7/16 motif prompt/provenance records. The 91 files under `regional_variants/` do exist, but they are old 820x520 RGBA composites; the 7/18 processor actually consumes the 91 unmodified full-flag ImageGen raws under `source_png/flags/regional_full_flag_raw/` and writes 91 spot masters under `processed_png/flags/regional_spot_colour_masters/`. The old composites are not used by the current processor or runtime hashes, but the manifest currently presents them as the current source. Remediation: rewrite this section to name the 7/18 raw/spot-master pipeline and label old `regional_variants` assets and 7/16 motif notes as superseded archival evidence; do not delete them as a substitute for retaining the 7/18 raws.
2. **HIGH — manifest completion/status and validator references are stale.** `manifest.md` line 3 says `Status: complete` and line 148 points to `regional_flag_validation_2026_07_16.json` and `regional_flag_checksums_2026_07_16.sha256`, while the current 7/18 JSON is still `candidate_requires_independent_visual_review`. Remediation: point the manifest to the 7/18 evidence, reflect the candidate/review state, and only change to complete after separate approval evidence exists.
3. **MEDIUM — GFX handoff validation command is wrong for this tranche.** `docs/assets/019_infantry_spawn/gfx_handoff.md` line 275 instructs running `_tooling/process_event_019_generated_art.py`, which is not the regional flag processor and does not reproduce the 7/18 regional flag validation. Remediation: point the regional flag validation ownership to `_tooling/process_event_019_regional_flags.py` with the exact recorded arguments and current JSON/checksum outputs.
4. **MEDIUM — superseded 7/16 docs are not marked superseded.** `notes/regional_flag_generation_provenance_2026_07_16.md`, `prompts/regional_flag_motif_prompts_2026_07_16.md`, the 7/16 validation/checksum pair, and the old motif/composite contact sheet remain adjacent to current assets without a clear archival/superseded banner. Remediation: add an explicit superseded notice and a link to the 7/18 source-of-truth records, or otherwise segregate them as historical evidence.

## Remediation required before approval

- Update `manifest.md` and `gfx_handoff.md` to make the 7/18 full-flag raw -> 820x520 spot master -> native PNG -> TGA chain the sole current source/runtime chain; label `regional_variants` and 7/16 records archival/superseded.
- Replace stale 7/16 validator references and the `Status: complete` claim with the current candidate state and 7/18 validation/checksum paths. Do not self-promote from machine PASS.
- Resolve or explicitly accept the exact-prompt gap for the seven GHOST_BASE rows with separate parent/user provenance evidence. Do not regenerate, recolour, or substitute these rows without new authorization.
- After those documentation/provenance remediations, rerun the independent visual review against the unchanged 91 current outputs and produce separate approval evidence linked to the exact current candidate hashes.

**Disposition:** current artwork/runtime rows are visually acceptable but this package is **FAIL / not approved** until the listed documentation and provenance blockers are remediated. The parent must not promote the candidate on this handoff.
