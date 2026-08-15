# Event 006 IW-013 NAV / IW-015 GLC portrait gate audit

Date: `2026-08-12`.

Owner scope: read-only re-audit of the existing grounded source-placeholder portrait packages for IW-013 NAV José Antonio Aguirre and IW-015 GLC Alfonso Daniel Castelao. No gameplay, history, country, event, focus, decision, AI, localisation, character, GFX, DDS, or source asset was changed by this audit. No RunPod, ImageGen, ComfyUI, provider queue, or replacement operation was used.

## Disposition summary

| Package | Source identity/date/role | Rights/provenance | Crop/PNG/DDS/runtime bytes | Current-policy package gate | Placeholder admissibility |
| --- | --- | --- | --- | --- | --- |
| IW-013 `NAV` Aguirre | `PASS` | `PASS_WITH_CAVEAT` | `PASS` | `HOLD` | The `source_placeholder` mode is allowed in principle, but this installed package is not fully admissible until the durable archive contract, commander-role reference evidence, and stale replacement label are corrected. |
| IW-015 `GLC` Castelao | `PASS` | `PASS_WITH_CAVEAT` | `PASS` | `HOLD` | The `source_placeholder` mode is allowed in principle, but this package is not admissible as currently wired because the additive Castelao character duplicates the vanilla GLC Castelao identity without a guarded transfer; the archive, role-reference, and state-label issues also remain. |

The source-placeholder byte chains are not the reason for the holds. The holds are policy and identity-ownership failures that must remain fail-closed. A source placeholder is not a styled final, and no styled-final request is recorded for either subject.

## Current policy and reference reading

The audit read `.agents/skills/chaos-redux-comfyui/SKILL.md`, `.agents/skills/chaos-redux-event-assets/SKILL.md`, `AGENTS.md`, the offline Paradox wiki pages for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Character modding, Portrait modding, State modding, Country creation, and National focus modding, and the installed vanilla documentation files `effects_documentation.md`, `triggers_documentation.md`, `loc_objects_documentation.md`, `loc_formatter_documentation.md`, `modifiers_documentation.md`, and `script_concept_documentation.md`.

The installed vanilla country histories `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/NAV - Navarra.txt` and `GLC - Galicia.txt`, vanilla portrait registration `interface/_leader_portraits.gfx`, and the canonical Event Asset reference contact sheets for `portraits/leaders/` and `portraits/commanders/` were also inspected.

Current policy allows a grounded `source_placeholder` when explicitly selected: unchanged attributed source, exact lossless crop/equality proof, deterministic `156x210` output, DDS/runtime wiring, and preserved identity. It requires a durable co-located original, source crop, crop JSON, `156x210` candidate, and provenance contract, plus separate identity, framing, and provenance review. `replacement_pending` is allowed only after an explicit outstanding `styled_final` request. A real person already owned by a live roster cannot be cloned without an explicit guarded transfer.

## Gate matrix

| Gate | IW-013 NAV | IW-015 GLC | Evidence and reason |
| --- | --- | --- | --- |
| Grounded classification | `PASS` | `PASS` | Both are real historical people and use `grounded_source_only`; no generated likeness was used. |
| Identity and source-visible likeness | `PASS` | `PASS` | Independent audit compared each unchanged master, exact crop, processed candidate, DDS decode, and source page. Aguirre's face, hair, suit, expression, and speaking pose remain source-visible; Castelao's face, glasses, hair, jacket, and halftone structure remain source-visible. |
| Date and 1936 role fit | `PASS` | `PASS` | Aguirre source: 1933 Aberri Eguna photograph; Aguirre lived 1904–1960 and became first Basque Lehendakari/head of defense in October 1936. Castelao source: *Vida gallega* issue 442 dated 10 March 1930; Castelao lived 1886–1950 and was active in the 1936 Galician Statute campaign. Both were alive at the 1936 baseline. |
| Rights/provenance | `PASS_WITH_CAVEAT` | `PASS_WITH_CAVEAT` | Aguirre Commons page body/category says CC BY-SA 3.0 while its machine-readable `rel=license` says CC BY-SA 4.0; attribution, licence link, and ShareAlike obligations must be preserved and the discrepancy remains unresolved. Castelao Commons marks CC-PD-Mark/PD-old-80, but the original author and scan-chain jurisdiction are unknown; public-domain status is therefore a caveated claim, not an unconditional clearance. |
| Exact crop and equality | `PASS` | `PASS` | Both metadata records report `status=exact_source_crop_verified` and `decoded_pixels_equal=true`; archive crop copies are byte-identical to the active crop outputs. |
| Deterministic processed PNG | `PASS` | `PASS` | Pillow LANCZOS direct resize, no repaint, enhancement, recolour, retouch, filter, or alpha framing; both outputs are RGB `156x210`. |
| DDS header/payload | `PASS` | `PASS` | Both runtime files are one-level uncompressed BGRA: `DDS ` magic, header 124, `156x210`, 32-bit masks `(0x00ff0000,0x0000ff00,0x000000ff,0xff000000)`, flags 65, texture caps `0x1000`, zero mipmaps, exact length `131168`, alpha `255/255`, and decoded pixels equal the processed PNG. |
| Runtime GFX path | `PASS` | `PASS` | `interface/006_independence_wave_iberian_portraits.gfx` points `GFX_portrait_NAV_jose_antonio_aguirre` and `GFX_portrait_GLC_alfonso_daniel_castelao` to the stable `gfx/leaders/006_independence_wave/*.dds` paths. No runtime reference points into `docs/assets/portraits/`. |
| Actual live consumer role | `PASS` | `HOLD` | NAV's additive `NAV_independence_wave_jose_antonio_aguirre` is a unique corps commander. GLC's additive `GLC_independence_wave_alfonso_daniel_castelao` is a second Castelao identity while vanilla `GLC - Galicia.txt` already creates the country leader Alfonso Daniel Castelao; no guarded transfer or ownership invalidation exists. |
| Role-reference family | `HOLD` | `HOLD` | The live consumers in `common/characters/006_independence_wave_iberian_commanders.txt` are army corps commanders, but the package manifest and comparison sheets identify and compare the country-leader reference family. The canonical `portraits/commanders/` family was inspected during this audit, but a commander-family comparison record and corrected role metadata are absent. |
| Durable archive contract | `HOLD` | `HOLD` | `docs/assets/portraits/006_independence_wave/` has the unchanged master, a crop PNG, and a prompt-like `.txt`, but lacks the required co-located `<basename>_source_crop.json` and deterministic `<basename>_156x210.png`. The complete crop/processing/provenance records exist only in the active `docs/assets/006_independence_wave/source_placeholder_2026_08_05_iberian/` workspace. The `.txt` files are person-only prompts, not the required URL/license/hash/crop/reviewer/verdict provenance contracts. |
| Replacement state | `HOLD` | `HOLD` | The package manifest and `gfx_handoff.md` list `source_placeholder, replacement_pending`, but the same manifest and current resume authority state that no explicit styled-final request exists. Under current policy these must be `source_placeholder` only; `replacement_pending` cannot be inferred from a raw placeholder. |

## IW-013 NAV evidence

Source page: <https://commons.wikimedia.org/wiki/File:Jose_Antonio_Agirre,_Aberri_Eguna_1933.jpg>. Direct media: <https://upload.wikimedia.org/wikipedia/commons/2/2c/Jose_Antonio_Agirre%2C_Aberri_Eguna_1933.jpg>. The archived Commons page identifies a 1933 Aberri Eguna image from GureGipuzkoa photo 1112433, Pascual Marín, Marín Collection. The source master is `docs/assets/portraits/006_independence_wave/portrait_NAV_jose_antonio_aguirre_source.jpg`, `669x1024` RGB JPEG, SHA-256 `1d34f7b23459f750dcbfcb8e300dc3d41f7087c4b24caf544d6ab2f8671e6bc9`.

The exact crop is `[268,235,500,510]`, `232x275` RGB PNG, SHA-256 `960948067a1478798f82da673099fff1d34bf9ca23b29bfa7fc8490ebf80f366`. Its equality receipt is `docs/assets/006_independence_wave/source_placeholder_2026_08_05_iberian/metadata/portrait_NAV_jose_antonio_aguirre_source_crop.json`, SHA-256 `2affa4e61cf9cfb6fd25fa9898923f3fff5724965ec6da1ade95f5e3911d2126`.

The processed source placeholder is `docs/assets/006_independence_wave/source_placeholder_2026_08_05_iberian/processed_png/portrait_NAV_jose_antonio_aguirre.png`, `156x210` RGB PNG, SHA-256 `15fab20a126a5201f95dfc8b70096cbe670731002680396d76e812051f810cc0`. Processing metadata is `processing_metadata/portrait_NAV_jose_antonio_aguirre_156x210.json`, SHA-256 `c2a4562c40def7aaa94b6f0c843de05eddd306cadb1e183fc65f6c6662b93326`.

The runtime DDS is `gfx/leaders/006_independence_wave/portrait_NAV_jose_antonio_aguirre.dds`, SHA-256 `8f38eefc44b92fbd2f55ca9bc1752fc4569050a4b8d1721ccb2bb587bc35ef73`. Its validation receipt is `review/portrait_NAV_jose_antonio_aguirre_dds_validation.json`, SHA-256 `5bcd38da5fbacf3b76af37e22ab79d822692c9af64c577cd2bc61b6c376ad091`; the decoded RGBA payload SHA-256 is `a46c355acd11daa0fb736a8ec6bf39e771c899aa90f9e1ac0cd8d62f937852a5`, equal to the source PNG payload. The temporary DDS copy and runtime DDS are byte-identical.

NAV has no vanilla Aguirre/Agirre character or portrait owner in the inspected project and vanilla roots. The additive `NAV_independence_wave_jose_antonio_aguirre` commander is recruited by hidden event `chaosx.nr6.350` and uses `GFX_portrait_NAV_jose_antonio_aguirre`; that unique ownership path is source-safe. The current package still fails the durable-archive and commander-reference gates above.

## IW-015 GLC evidence

Source page: <https://commons.wikimedia.org/wiki/File:Castelao_Vida_Gallega_442.png>. Direct media: <https://upload.wikimedia.org/wikipedia/commons/9/91/Castelao_Vida_Gallega_442.png>. The archived Commons page identifies a Galiciana/Biblioteca Dixital de Galiza scan from *Vida gallega*, issue 442, 10 March 1930, with the original author recorded as unknown. The source master is `docs/assets/portraits/006_independence_wave/portrait_GLC_alfonso_daniel_castelao_source.png`, `620x634` grayscale PNG, SHA-256 `e022556b94a983f590dc2accde2dc6d6261fbe19369f688e4cca2f0adcdaa242`.

The exact crop is `[88,8,552,630]`, `464x622` grayscale PNG, SHA-256 `1fb10ebf8c7f5d9e97f81d1ed93a7442cbf9f83561e911a1c65a09f68b8ff232`. Its equality receipt is `docs/assets/006_independence_wave/source_placeholder_2026_08_05_iberian/metadata/portrait_GLC_alfonso_daniel_castelao_source_crop.json`, SHA-256 `96c478d707ae72613ca1f0ce4537696d4d2c01bb99cd84b309e718df39ac8f17`.

The processed source placeholder is `docs/assets/006_independence_wave/source_placeholder_2026_08_05_iberian/processed_png/portrait_GLC_alfonso_daniel_castelao.png`, `156x210` RGB PNG, SHA-256 `80f77a25c4c30fae67aefab7619aae390983afa22d2685d27746eb3d96df90c6`. Processing metadata is `processing_metadata/portrait_GLC_alfonso_daniel_castelao_156x210.json`, SHA-256 `d107a106b144f09e3cbbbd354e0402b03589684133b21158a62eaf596ae0ed29`.

The runtime DDS is `gfx/leaders/006_independence_wave/portrait_GLC_alfonso_daniel_castelao.dds`, SHA-256 `33aa76c4bbcbb87e7f9ce1508beadee4799a558a429f92b4d5ac8fc09c4a4b7f`. Its validation receipt is `review/portrait_GLC_alfonso_daniel_castelao_dds_validation.json`, SHA-256 `0197ee726bfd7331284a3ff76ef7b9590cde51f3afc34169dcfe514b349641ac`; the decoded RGBA payload SHA-256 is `f4c5240dec022af29b5753606615589abd81e12e8aaa64850095569ca4949001`, equal to the source PNG payload. The temporary DDS copy and runtime DDS are byte-identical.

The vanilla `GLC - Galicia.txt` history already creates country leader `Alfonso Daniel Castelao` with `GFX_portrait_Alfonso_Daniel_Castelao`. The Event 006 file separately defines `GLC_independence_wave_alfonso_daniel_castelao` and the hidden roster event recruits it as a corps commander. This is a simultaneous duplicate of a real-person identity, not a guarded transfer, so the current GLC portrait consumer is fail-closed under the subject-ownership gate. A different identity or an explicit transfer/role architecture is required before this portrait can be admitted.

## Runtime wiring verification

| Surface | Current evidence | Result |
| --- | --- | --- |
| Sprite registration | `interface/006_independence_wave_iberian_portraits.gfx` defines both stable sprite names and points to `gfx/leaders/006_independence_wave/`. | `PASS` |
| NAV character consumer | `common/characters/006_independence_wave_iberian_commanders.txt` uses `large = GFX_portrait_NAV_jose_antonio_aguirre`; `events/006_independence_wave.txt` recruits it at `chaosx.nr6.350`. | `PASS` for unique ownership; role-family evidence remains `HOLD`. |
| GLC character consumer | The same character file uses `large = GFX_portrait_GLC_alfonso_daniel_castelao`; `events/006_independence_wave.txt` recruits it at `chaosx.nr6.350`; vanilla history already owns Castelao as a country leader. | `HOLD` for duplicate ownership. |
| Archive separation | `rg` over project script/GFX/history surfaces found no runtime path into `docs/assets/portraits/`; both runtime DDS files are present at the stable paths. | `PASS` |

## Replacement state, omissions, and blockers

- No explicit styled-final request, RunPod output, `832x1120` master, or provider/job evidence exists for either subject; neither should be called `styled_final` or `replacement_pending`.
- The existing `manifest.md` and `gfx_handoff.md` contain the stale pair `source_placeholder, replacement_pending`; this contradicts the current policy and the same manifest's statement that no styled-final request was recorded.
- The durable flat archive is not a current-policy co-located portrait package because its prompt `.txt` files are not provenance contracts and the crop JSON plus deterministic `156x210` candidate remain only in the temporary workspace.
- The package was produced and reviewed under the country-leader reference family, while the live character consumers are army corps commanders; corrected commander-family evidence is required.
- GLC's additive Castelao character duplicates the vanilla Castelao country-leader identity without a guarded transfer. This is an independent `HOLD` even if the source rights caveat is later resolved.
- NAV's source identity and unique ownership are sufficient for a conditional source-placeholder review, but the durable archive, commander-reference, and state-label issues keep the installed package `HOLD`.
- The current Event 006 country-package admission remains `HOLD` for both tags; this portrait handoff does not alter flags, package adapters, central attestation, MCP evidence, AI balance, or live gameplay gates.

## Parent actions required

1. Keep IW-013 and IW-015 outside central content attestation and automatic package promotion.
2. Normalize each durable archive under `docs/assets/portraits/006_independence_wave/` to the current co-located basename contract, including original, `_source_crop.png`, `_source_crop.json`, `_156x210.png`, and a full provenance `.txt` contract with reviewer/date and separate identity/framing/provenance verdicts.
3. Reclassify both consumers as army corps commanders and attach canonical `portraits/commanders/` comparison evidence rather than country-leader references.
4. Correct the stale `replacement_pending` labels to `source_placeholder` unless the user later explicitly requests a styled final.
5. Resolve GLC Castelao ownership before any admission by removing the duplicate or implementing an explicit guarded transfer that prevents simultaneous vanilla and Event 006 ownership; do not silently keep both identities.
6. Preserve Aguirre's CC BY-SA version discrepancy and Castelao's unknown-author/scan-chain caveat in the final provenance records; no rights caveat may be silently converted into public-domain clearance.

## Final outcome

Both source-to-crop-to-PNG-to-DDS chains and portrait-specific runtime registrations are intact and independently reviewable. The grounded source identity, date, framing, and byte evidence pass, with rights/provenance caveats recorded. The current project-level portrait packages nevertheless remain `HOLD` and fail-closed because the durable archive contract and commander-role evidence are incomplete, and GLC additionally violates the real-person ownership gate through a duplicate Castelao consumer. No replacement was invented or requested, and no gameplay file was changed.
