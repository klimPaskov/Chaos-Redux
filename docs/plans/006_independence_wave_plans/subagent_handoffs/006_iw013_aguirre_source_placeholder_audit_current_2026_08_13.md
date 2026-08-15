# Event 006 IW-013 NAV Aguirre source-placeholder audit

Date: `2026-08-13`.

## Scope and verdict

This is a portrait-only audit of the existing IW-013 NAV José Antonio Aguirre source-placeholder package. No source artwork, PNG, DDS, `.gfx`, character, gameplay, history, country, flag, localisation, event, focus, decision, AI, attestation, Join, RunPod, ImageGen, ComfyUI, provider queue, or replacement operation was changed.

Verdict: **source_placeholder mode is allowed in principle, but the current IW-013 package is HOLD / not fully admissible under the current portrait contract**.

The source identity, 1933 date fit, source-visible framing, exact crop equality, deterministic `156x210` processing, DDS payload, stable runtime path, and unique NAV consumer pass this bounded audit. Admission remains blocked by the incomplete durable archive contract, the role-reference mismatch, the unresolved rights-version discrepancy, and the stale `replacement_pending` label. These are narrow portrait-package gates; this handoff does not authorize central IW-013 package attestation or any country-package promotion.

No final HOI4-style portrait was requested or supplied. The correct state is `source_placeholder`; `replacement_pending` must not be inferred from a raw source placeholder and may be used only after an explicit outstanding styled-final request.

## Policy and references consulted

The audit read `AGENTS.md`, `.agents/skills/chaos-redux-comfyui/SKILL.md`, `.agents/skills/chaos-redux-event-assets/SKILL.md`, the offline Paradox wiki pages for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Character modding, Portrait modding, Graphical asset modding, Country creation, State modding, and National focus modding, and the installed vanilla documentation for effects, triggers, modifiers, localisation objects/formatting, dynamic variables, and script concepts.

The installed vanilla `history/countries/NAV - Navarra.txt`, vanilla `interface/_leader_portraits.gfx`, the project character consumer, and the canonical role-reference families `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/` and `portraits/commanders/` were inspected. The commander family has native full `156x210` references and its contact sheet is `portraits/commanders/contact_sheet.png`.

## Identity, source, date, and rights

The subject is the grounded real person José Antonio Aguirre y Lecube, so `grounded_source_only` and attributed unchanged-source handling are required. The source master is `docs/assets/portraits/006_independence_wave/portrait_NAV_jose_antonio_aguirre_source.jpg`, `669x1024`, RGB JPEG, SHA-256 `1d34f7b23459f750dcbfcb8e300dc3d41f7087c4b24caf544d6ab2f8671e6bc9`.

The archived source page is `docs/assets/006_independence_wave/source_placeholder_2026_08_05_iberian/source_pages/commons_jose_antonio_agirre_aberri_1933.html`, corresponding to <https://commons.wikimedia.org/wiki/File:Jose_Antonio_Agirre,_Aberri_Eguna_1933.jpg>; the direct media URL is <https://upload.wikimedia.org/wikipedia/commons/2/2c/Jose_Antonio_Agirre%2C_Aberri_Eguna_1933.jpg>. The page describes José Antonio Agirre at the 1933 Aberri Eguna in Donostia-San Sebastián, identifies Pascual Marín and the Marín Collection/GureGipuzkoa photo 1112433, and records the source date as 1933.

Independent identity/date review: `PASS`. The source-visible face, swept hair, clean-shaven appearance, dark suit, white shirt, tie, lapel items, expression, speaking pose, and urban outdoor setting remain identifiable in the crop and processed candidate. Aguirre was born in 1904, was alive in 1936, and became the first Basque Lehendakari and head of defense during the Spanish Civil War, so the source is period-compatible with the role's 1936 baseline.

Rights/provenance review: `PASS_WITH_CAVEAT`, not unconditional clearance. The Commons page body and category declare CC BY-SA 3.0, while the archived page's machine-readable `rel=license` and JSON-LD advertise CC BY-SA 4.0. Preserve author attribution, source link, change notice, and ShareAlike obligations, and keep the version discrepancy explicit until a parent-owned rights review resolves or accepts it; public-domain status must not be claimed.

The repository ownership search covered `common/characters/`, `history/countries/`, `gfx/leaders/`, `interface/`, `localisation/`, and vanilla character/portrait consumers for `Aguirre`, `Agirre`, `José Antonio`, `Jose Antonio`, `Lecube`, and related name-order variants. No existing vanilla or Chaos Redux consumer for José Antonio Aguirre y Lecube was found; the unrelated vanilla Aguirre surnames do not establish identity ownership. The additive NAV consumer is therefore unique in this bounded ownership search.

## Crop, processing, framing, and hashes

The lossless crop is `docs/assets/006_independence_wave/source_placeholder_2026_08_05_iberian/crops/portrait_NAV_jose_antonio_aguirre_source_crop.png`, `232x275`, RGB PNG, SHA-256 `960948067a1478798f82da673099fff1d34bf9ca23b29bfa7fc8490ebf80f366`. Its half-open decoded-master rectangle is `[268,235,500,510]`.

The crop receipt is `docs/assets/006_independence_wave/source_placeholder_2026_08_05_iberian/metadata/portrait_NAV_jose_antonio_aguirre_source_crop.json`, SHA-256 `2affa4e61cf9cfb6fd25fa9898923f3fff5724965ec6da1ade95f5e3911d2126`. It reports `status=exact_source_crop_verified`, `decoded_pixels_equal=true`, matching RGBA hashes, and `63800` decoded pixels. The durable flat archive crop `docs/assets/portraits/006_independence_wave/portrait_NAV_jose_antonio_aguirre.png` is byte-identical to this crop.

Framing review: `PASS` for source-visible framing and identity preservation. The crop keeps the head, shoulders, suit, hands, and speaking pose without repaint, face substitution, genericization, beautification, symmetrization, invented detail, or unsupported insignia. It is a source crop rather than a HOI4 repaint, so it intentionally retains monochrome documentary texture and background detail.

The deterministic processed candidate is `docs/assets/006_independence_wave/source_placeholder_2026_08_05_iberian/processed_png/portrait_NAV_jose_antonio_aguirre.png`, `156x210`, RGB PNG, SHA-256 `15fab20a126a5201f95dfc8b70096cbe670731002680396d76e812051f810cc0`. `processing_metadata/portrait_NAV_jose_antonio_aguirre_156x210.json` records direct Pillow LANCZOS resize from the exact crop with no repaint, enhancement, recolour, retouch, filter, or alpha framing.

The package review sheet is `review/portrait_NAV_jose_antonio_aguirre_comparison_sheet.png`, and the native `4x` nearest-neighbour processed-versus-DDS comparison is `review/portrait_NAV_jose_antonio_aguirre_native_4x_processed_vs_dds.png`. The existing review compares the source master, crop, processed candidate, DDS round-trip, and three leader references; this audit also inspected the canonical commander contact sheet because the live consumer is a corps commander.

## DDS and runtime wiring

The evidence DDS is `docs/assets/006_independence_wave/source_placeholder_2026_08_05_iberian/final_dds/portrait_NAV_jose_antonio_aguirre.dds`, and the runtime DDS is `gfx/leaders/006_independence_wave/portrait_NAV_jose_antonio_aguirre.dds`. Both are `131168` bytes and SHA-256 `8f38eefc44b92fbd2f55ca9bc1752fc4569050a4b8d1721ccb2bb587bc35ef73`; the evidence and runtime copies are byte-identical.

The DDS receipt is `review/portrait_NAV_jose_antonio_aguirre_dds_validation.json`, SHA-256 `5bcd38da5fbacf3b76af37e22ab79d822692c9af64c577cd2bc61b6c376ad091`. Independent header/payload checks confirm `DDS ` magic, 124-byte header, `156x210` dimensions, exact length `128 + 156*210*4`, pixel-format size `32`, flags `65`, 32-bit BGRA masks `(0x00ff0000,0x0000ff00,0x000000ff,0xff000000)`, `DDSCAPS_TEXTURE` `0x1000`, zero mipmaps, and alpha range `255..255`. The decoded RGBA payload SHA-256 is `a46c355acd11daa0fb736a8ec6bf39e771c899aa90f9e1ac0cd8d62f937852a5`, and it is pixel-identical to the processed PNG.

Portrait-specific wiring is present in `interface/006_independence_wave_iberian_portraits.gfx`:

```text
GFX_portrait_NAV_jose_antonio_aguirre
 -> gfx/leaders/006_independence_wave/portrait_NAV_jose_antonio_aguirre.dds
```

No runtime path points into `docs/assets/portraits/` or the temporary source-placeholder workspace. The stable sprite and DDS path require no change for a future accepted replacement.

## Live consumer and role gate

The live consumer is `NAV_independence_wave_jose_antonio_aguirre` in `common/characters/006_independence_wave_iberian_commanders.txt`. It defines `gender = male`, `army.large = GFX_portrait_NAV_jose_antonio_aguirre`, and a `corps_commander` block; hidden event `chaosx.nr6.350` recruits the additive commander. No `army.small` dossier portrait is defined, so the full `156x210` texture is the correct runtime size and no fabricated `50x67` substitute is involved.

Role gate: `HOLD`. The source-placeholder manifest and comparison sheet classify the candidate under the country-leader reference family, while the live consumer is an army corps commander. This is a metadata/evidence mismatch, not a face-identity failure. The parent must attach commander-family style-control evidence and update the role metadata before claiming a complete portrait gate.

## Durable archive contract gate

Durable archive gate: `HOLD`. The current flat archive contains `portrait_NAV_jose_antonio_aguirre_source.jpg`, `portrait_NAV_jose_antonio_aguirre.png` (the crop), and a 321-byte prompt-like `portrait_NAV_jose_antonio_aguirre.txt`. It does not contain the required co-located `portrait_NAV_jose_antonio_aguirre_original.jpg`, `portrait_NAV_jose_antonio_aguirre_source_crop.png`, `portrait_NAV_jose_antonio_aguirre_source_crop.json`, `portrait_NAV_jose_antonio_aguirre_156x210.png`, and full provenance contract under the exact runtime basename. The complete crop, processing, DDS, review, and source-page evidence exists only in the active temporary workspace, so the durable archive is not yet a current-policy source package.

The durable `.txt` is only a person-only prompt record and does not record the required source URL, attribution, license/version caveat, source/crop/processed/runtime hashes, crop coordinates, mode/state, reviewer/date, separate identity/framing/provenance verdicts, runtime path, sprite, or commander-role metadata.

## Replacement state and admission boundary

The current `manifest.md`, `gfx_handoff.md`, and `.gfx` header comment pair `source_placeholder` with `replacement_pending`, but no explicit styled-final request, provider output, `832x1120` master, job evidence, or RunPod operation exists. Under current policy the portrait state must be `source_placeholder` only. A future user-requested styled final would be a separate parent/user-owned operation at the same stable runtime basename; it is not required to admit the unchanged source placeholder once the evidence gates are repaired.

The portrait package itself is **not admissible as fully complete today** because the durable archive and commander-reference gates are open and the rights version discrepancy remains unresolved. The source-placeholder mode may be admitted after those narrow portrait-owned corrections and an independent review record; no repaint or generated replacement is necessary for that mode.

IW-013 country/package admission remains separately fail-closed. This handoff does not change NAV history, tags, flags, leader selection, command-roster mechanics, central attestation, formables, AI, probability evidence, MCP artifacts, Join, or any other package gate.

## Narrow parent-owned fixes

1. Normalize the durable archive under `docs/assets/portraits/006_independence_wave/` into a subject package with the exact runtime basename and co-located original bytes, `_source_crop.png`, `_source_crop.json`, deterministic `_156x210.png`, and a full provenance contract; preserve the existing source and evidence hashes.
2. Add the commander-role metadata and a commander-family comparison/review record using `portraits/commanders/contact_sheet.png` and selected full `156x210` commander references; do not use the leader family as the live role gate.
3. Correct the stale `replacement_pending` wording in the portrait manifest, handoff, and comments to `source_placeholder` unless the user explicitly requests a styled final later; do not silently initiate or imply a provider workflow.
4. Preserve the CC BY-SA 3.0 body declaration versus CC BY-SA 4.0 machine-readable discrepancy in the provenance contract and obtain parent-owned rights acceptance or clarification before any final distribution/admission claim.
5. Keep `GFX_portrait_NAV_jose_antonio_aguirre`, the runtime DDS basename/path, and the unique NAV commander ownership stable; no gameplay or central-attestation patch is needed for these portrait fixes.

## Evidence and skipped checks

Evidence reviewed: archived Commons and Wikipedia source pages, source master, exact crop and JSON equality receipt, deterministic processing JSON, temporary and durable crop copies, processed PNG, evidence/runtime DDS, DDS validation JSON, decoded DDS PNG, comparison sheet, native `4x` comparison, portrait-specific `.gfx`, NAV character consumer, and ownership-search results.

Skipped by scope: RunPod/provider work, ImageGen, ComfyUI, styled-final validation, DDS regeneration, gameplay or country-package audits, flag/attestation/Join changes, MCP engine validation, live game/save testing, and all GLC or unrelated portrait packages.

No simplification or fallback was introduced. The only changed file in this audit is this durable handoff.
