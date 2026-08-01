# IW-018 ARX source-locked portrait independent audit v77

Audit date: 2026-08-01.

Scope: independent likeness, HOI4-style, provenance, rights, and role-fit review of the three source-locked portrait candidates in `docs/assets/006_independence_wave/iw018_arx_portrait_repaint_v76_2026_08_01/`.

This handoff is an asset audit only. It does not edit gameplay, character definitions, localisation, `.gfx`, DDS files, or the existing placeholder identities.

## Evidence reviewed

- The v76 manifest, audit, GFX handoff, per-subject processing metadata, source-locked prompts, raw repaints, processed 156x210 candidates, and both v76 review sheets.
- The unchanged v15 source masters, exact-crop PNGs, and decoded-pixel equality JSON files.
- The v75 source ledger and eligibility record for identity, birth, 1936 role, source date, rights, and placeholder-name disposition.
- Canonical vanilla leader references `den_thorvald_stauning.png` and `fin_carl_mannerheim.png` and canonical commander reference `ita_pietro_badoglio.png` under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/`.
- Each subject was compared source master -> exact crop -> raw repaint -> 156x210 candidate at native scale and in the enlarged v76 comparison sheet. The candidates were also compared against the applicable vanilla leader or commander family.

## Independent disposition summary

| Candidate and proposed consumer | Likeness | HOI4 style | Provenance | Rights | Role fit | Overall disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Emilio Lussu, `ARX_emilio_lussu` | `PASS` | `PASS` | `PASS` | `PASS_WITH_ATTRIBUTION` | `PASS` for the Sardinian civic/labor route | Complete as a source-locked visual candidate; parent package admission and runtime attribution remain pending. |
| Luigi Arborio Mella di Sant'Elia, proposed replacement for `ARX_vittorio_pala` | `PASS_WITH_MINOR_UNCERTAINTY` | `PASS` | `PASS` | `PASS_WITH_ATTRIBUTION` | `PASS_ONLY_AS_PROPOSED_CROWN_REPLACEMENT` | `NEEDS_USER_REVIEW`; do not relabel as Vittorio Pala. |
| Vittorio Vernè, proposed replacement for `ARX_gavino_piras` | `PASS_WITH_LOW_RESOLUTION_CAVEAT` | `PASS` | `PASS` | `PASS` | `PASS_ONLY_AS_SARDINIA_LINKED_COMMAND` | `NEEDS_USER_REVIEW`; blocked under a strict Sardinian-birth requirement and must not be relabelled as Gavino Piras. |

## Candidate findings

### Emilio Lussu

Likeness: `PASS`. The source crop shows the distinctive swept dark hair, wire-rim glasses, narrow moustache, pointed goatee, long face, and three-quarter pose. The repaint and 156x210 candidate retain those identity anchors, including the glasses, hairline, nose, moustache/goatee, jaw, and shoulder pose. Skin and eye planes are slightly smoothed for the painted treatment, but no unsupported facial feature or generic replacement is apparent at native or enlarged view.

HOI4 style: `PASS`. The muted brown-grey background, restrained gouache/oil planes, period suit and tie, quiet framing, and readable face fit the canonical leader family. The comparison uses `den_thorvald_stauning.png` and `fin_carl_mannerheim.png` from the canonical leaders directory.

Provenance: `PASS`. The immutable Senate master is `source_masters/emilio_lussu_senate_pre1958.jpg` (180x253, SHA-256 `23b0f650f56cb7aeeb017bcad7cde5186d190cb05f6bab99f8656efd895489a0`). The v15 exact crop is the complete frame `(0,0)-(180,253)` (SHA-256 `0440330b7d53bd8fa44b8af38e8452304b624208a5e0fbb89d416293a448c78b`) and its JSON records decoded-pixel equality. The raw repaint is 1054x1492 RGB (SHA-256 `2a97390107e5913e91d0dc546f6cc1ed6843496cdcec6d1daa6ea38c9e217a8d`). The deterministic output is `repaints_processed/portrait_ARX_independence_wave_emilio_lussu_156x210_candidate.png` (156x210 RGBA, fully opaque, SHA-256 `ce55b8db3567a2a665436519fdf7d9f2536ab38581c3898544c91c2bf4bf60c6`).

Rights: `PASS_WITH_ATTRIBUTION`. The v75 ledger identifies the Senate of the Republic source record via Commons `File:Emilio Lussu.jpg`, with CC BY 3.0 IT via `senato.it`. The capture is bounded only as before 1958, not precisely dated. Preserve the source URL, Senate credit, and CC BY 3.0 IT attribution in the release manifest before runtime use.

Role fit: `PASS`. Emilio Lussu is a real Sardinian-born statesman, soldier, and writer alive and politically active in 1936. The current consumer name is already `ARX_emilio_lussu`; no identity substitution is needed.

Disposition: source-ready visual candidate. Parent still owns DDS conversion, `.gfx` registration, character/localisation checks, and final package admission.

### Luigi Arborio Mella di Sant'Elia

Likeness: `PASS_WITH_MINOR_UNCERTAINTY`. The small 153x193 source is front-facing but readable. The repaint preserves the receding hairline, broad forehead, long narrow face, large ears, thin lips, frontal pose, decorated court uniform, sash, and visible medals. The eyes and skin planes are warmer and smoother than the source and the low source resolution leaves less certainty than Lussu, so retain a user-review gate rather than treating this as an unconditional identity pass.

HOI4 style: `PASS`. The finished candidate has the same subdued painted palette, neutral studio background, clear facial planes, and leader framing as the canonical leader references `den_thorvald_stauning.png` and `fin_carl_mannerheim.png`. Decorations remain source-visible; no unsupported medal or insignia is apparent.

Provenance: `PASS`. The immutable Senate master is `source_masters/luigi_mella_santelia_senate.gif` (153x193, SHA-256 `7ada408f2c89d94cd54e19ff9d6914311881df964b434b2aaf8a89a84148802e`). The v15 crop is the complete frame `(0,0)-(153,193)` (SHA-256 `530ed290cb842e435f61e6f796302bbedfe045627f7d36c465d2802fac8d0515`) and its JSON records decoded-pixel equality. The raw repaint is 1116x1409 RGB (SHA-256 `5846498cfd7a3b5c550557ef19a6d3eebe7b4473c2bff536233d52866ed468ae`). The deterministic output is `repaints_processed/portrait_ARX_luigi_mella_santelia_156x210_candidate.png` (156x210 RGBA, fully opaque, SHA-256 `654f63c265154bf777538f0bd6eea50b126ad6a44bed4c6e6c5f22387d3dcb0b`).

Rights: `PASS_WITH_ATTRIBUTION`. The v75 ledger identifies the Senate of the Republic source record `File:Mella di Sant'Elia.gif`, with CC BY 3.0 IT via `senato.it`. The source is latest-bounded before 26 June 1955 and does not provide an exact capture date. Preserve the source URL, Senate credit, and CC BY 3.0 IT attribution in the release manifest.

Role fit: `PASS_ONLY_AS_PROPOSED_CROWN_REPLACEMENT`. Mella was born in Sassari, served as Grand Master of Court Ceremonies for Vittorio Emanuele III, and was alive in 1936, making him a strong crown-consultative substitute. He is not the person named Vittorio Pala, and the Senate appointment date begins in 1939, so the character must be described as a court official or royal confidant rather than a 1936 senator.

Disposition: `NEEDS_USER_REVIEW`. Parent must explicitly accept the identity/name change to Luigi Arborio Mella di Sant'Elia before any character, localisation, DDS, or `.gfx` wiring. Do not silently connect this candidate to `ARX_vittorio_pala`.

### Vittorio Vernè

Likeness: `PASS_WITH_LOW_RESOLUTION_CAVEAT`. The 1930s source is a low-resolution side profile. The repaint preserves the profile, nose/chin/ear silhouette, close hair, peaked service cap, collar stars, medal ribbons, and serious expression. The source cannot establish fine eye, cheek, or mouth detail, and the repaint necessarily smooths or fills those planes, so this remains a user-review likeness pass rather than an unconditional grounded-identity pass.

HOI4 style: `PASS`. The candidate has readable commander framing, restrained late-1930s palette, gouache/oil planes, and a quiet neutral background. The v76 sheet visibly compares it with the leader reference `fin_carl_mannerheim.png` and the commander reference `ita_pietro_badoglio.png`; the commander reference is appropriate to the role family. The v76 Vernè JSON does not document that exact pair correctly, as noted below.

Provenance: `PASS`. The immutable Commons master is `source_masters/vittorio_verne_commander_commons.jpg` (200x250, SHA-256 `de94df14318398914a51aa0fb6601f9c31f916cc98d3803b313fe33be15f1417`). The v15 crop is `(7,0)-(193,250)` (186x250, SHA-256 `752046992ffb8c244b1b480b728f1d79988d3683e1d61532903e374027f42b09`) and its JSON records decoded-pixel equality. The raw repaint is 1081x1455 RGB (SHA-256 `8eda9fa779b0668ace9b5c277333f56a5bb672bfa9748acb85e685952554f6c5`). The deterministic output is `repaints_processed/portrait_ARX_vittorio_verne_156x210_candidate.png` (156x210 RGBA, fully opaque, SHA-256 `3c699067912e15df3469c6ceda1a82e12326f808ef838fd896589a5cee2fe1d9`).

Rights: `PASS`. The v75 ledger identifies the anonymous 1930s Commons source `File:Vittorio Vernè.jpg` with PD-Italy plus PD-1996. Preserve the Commons URL and source credit in the release manifest even though the source record is public-domain marked.

Role fit: `PASS_ONLY_AS_SARDINIA_LINKED_COMMAND`. Vernè has a documented 1936 divisional-command fit, but the source ledger records him as born in Rome. He is only Sardinia-linked through institutional or formation history, not Sardinian-born. This candidate is therefore eligible only if the parent explicitly accepts a Sardinia-linked commander interpretation and changes the authored identity. It fails a strict Sardinian-birth requirement. The processed asset is commander-family only; parent must not reuse it for a civilian or country-leader portrait consumer without an explicit role decision.

Disposition: `NEEDS_USER_REVIEW` under the conditional role interpretation; otherwise `BLOCKED`. Do not label it Gavino Piras and do not wire it to `ARX_gavino_piras` without an explicit roster/name decision.

## Identity-name boundary

`Vittorio Pala` remains `BLOCKED_NAME_ONLY`. The v75 exact-name search found no attributable historical identity, era-fit biography, or rights-cleared portrait. Luigi Arborio Mella di Sant'Elia is a researched real-person replacement candidate, not Vittorio Pala.

`Gavino Piras` remains `BLOCKED_NAME_ONLY`. The v75 exact-name search found no attributable historical identity, era-fit mountain-command biography, or rights-cleared portrait. Vittorio Vernè is a conditional Sardinia-linked replacement candidate, not Gavino Piras.

No generated, generic, or relabelled face may be used to keep either placeholder name.

## Package integrity and documentation findings

- All three v76 metadata chains point to existing source masters, crops, raw repaints, flat original-size masters, processed candidates, and review sheets. The flat original-size masters are byte-identical to their raw repaint hashes.
- All three processed candidates are 156x210 RGBA with alpha extrema `(255,255)`; no unintended transparency was found.
- The v15 source-crop JSON files record exact decoded-pixel equality for all three crops.
- The Lussu and Mella reference lists correctly point to existing canonical leader files.
- The v15 Vernè crop JSON preserves the correct pixels and hash, but its recorded `master.path` points to the earlier 2026-07-26 source copy while the v76 metadata points to the 2026-07-29 v15 copy. The copies have the same SHA-256; the final attribution manifest should canonicalize one source path instead of leaving two apparent masters.
- The Vernè metadata has two additional documentation defects that must be corrected before runtime promotion: `processing_metadata/portrait_ARX_vittorio_verne_156x210.json` records the subject as literal `Vittorio Vern?`, and its `reference_dir` is the commander directory while `selected_references` lists `fin_carl_mannerheim.png`, which exists only in the leaders directory. The review sheet additionally shows `ita_pietro_badoglio.png` as the commander reference. These are provenance-documentation issues, not a reason to alter the source or repaint.
- The v76 package contains no final DDS and makes no `.gfx`, character, or localisation edits. Runtime promotion remains held until the parent resolves the two proposed identity/name changes, carries attribution, corrects the Vernè metadata, and completes the country-package audit.
- No advisor, `_small`, operative, dossier, or alternate commander derivative is cleared by this audit.

## Parent handoff

1. Admit `ARX_emilio_lussu` only after the parent carries the CC BY 3.0 IT Senate attribution and confirms the pre-1958 source-date uncertainty is acceptable for the civic route.
2. Treat Mella as a proposed replacement only. If accepted, rename and describe the crown character as Luigi Arborio Mella di Sant'Elia and retain the role wording supported by his 1936 court connection.
3. Treat Vernè as a proposed Sardinia-linked commander only. If the design requires Sardinian birth, keep the candidate blocked and do not substitute it for Gavino Piras.
4. Correct the Vernè metadata subject and selected-reference paths before any final manifest or `.gfx` handoff.
5. Keep the exact Pala/Piras placeholders blocked unless the parent makes an explicit identity/name decision; no silent relabelling is permitted.
