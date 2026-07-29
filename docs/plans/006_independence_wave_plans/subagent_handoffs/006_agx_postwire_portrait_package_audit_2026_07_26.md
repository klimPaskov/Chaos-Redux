# IW-007 Frisia AGX post-wire portrait package audit

Date: 2026-07-26

Scope: bounded post-wire audit of the promoted trial-02 portraits for AGX/Frisia.
This audit covers the retained source masters, exact crops and equality JSON, raw ImageGen results, processed candidates, independent visual audit, promoted runtime DDS files, stable `.gfx` and character consumers, male-only role metadata, and the absence of advisor, dossier, or small-portrait derivatives.

Disposition: **PASS for the portrait/runtime tranche.** The promoted files are the approved trial-02 candidates at the stable runtime paths and do not invalidate the prior AGX country-package audit.

The prior package disposition remains **PARTIAL** for unrelated AGX surfaces, specifically the North Sea conference decision lane, the shared focus-tree geometry ledger, and the static-versus-live runtime attestation boundary recorded in `docs/plans/006_independence_wave_plans/subagent_handoffs/006_agx_country_package_reaudit_2026_07_26.md:7-11,37-44,131-150`.

## Evidence authority and file surface

| Surface | Evidence | Result |
| --- | --- | --- |
| Independent portrait gate | `docs/plans/006_independence_wave_plans/subagent_handoffs/006_agx_portrait_trial2_independent_audit_2026_07_26.md` (commit `17ee36e64`) | PASS for Douwe Kalma and Pieter Reenalda candidate-02 before conversion. |
| New civic-leader package | `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_26/frisia_douwe_kalma_trial_02/` | Source master, exact crop, raw repaint, processed `156x210` candidate, review sheet, metadata, and previous/promoted DDS review copies are present. |
| New commander package | `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_26/frisia_pieter_reenalda_trial_02/` | Source master, exact crop, raw repaint, processed `156x210` candidate, review sheet, metadata, and previous/promoted DDS review copies are present. |
| Runtime textures | `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_council.dds` and `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_commander.dds` | Both promoted files exist and match their retained promoted review copies byte-for-byte. |
| Stable sprite definitions | `interface/006_independence_wave_region_01_portraits.gfx:19-24` | Exactly one stable sprite definition per AGX portrait, with the expected runtime texture path. |
| Character consumers | `common/characters/006_independence_wave_wallonia_frisia_characters.txt:81-126` | AGX civic leader uses `civilian.large`, AGX commander uses `army.large`, and both are explicitly male. |
| Recruitment consumers | `history/countries/AGX - Frisia.txt:17-18` | Both intended character tokens are recruited by AGX. |
| Display names | `localisation/english/006_independence_wave_wallonia_frisia_l_english.yml:5-6` | Stable names remain Douwe Kalma and Pieter Reenalda. |

No gameplay, `.gfx`, localisation, character, history, map, flag, or asset source file was edited by this audit.

## Candidate and source checks

### Douwe Kalma civic leader

| Artifact | Path | Verified facts |
| --- | --- | --- |
| Immutable source master | `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_26/frisia_douwe_kalma_trial_02/source_masters/AGX_douwe_kalma_1917_master.jpg` | RGB `691x1013`, SHA-256 `38dafcbff7c3a67b6b29b9b637e69ff4c2f9d8caae076361200919a6bb36dbdf`. The source is the circa-1917 F. O. Strüpert/Tresoar public-domain portrait documented in the retained source ledger. |
| Exact source crop | `.../source_crops/AGX_douwe_kalma_1917_head_shoulders.png` and adjacent JSON | RGB `590x796`, crop `(50,80,640,876)`, `status = exact_source_crop_verified`, `decoded_pixels_equal = true`, equality hash `247524909d5b9cb82661b35a9f5f7b70f4411bd9b32b59f7b65ac1f74cbd94b4`. |
| Raw ImageGen result | `.../imagegen_results/AGX_douwe_kalma_identity_preserve_trial_02.png` | RGB `1080x1456`, SHA-256 `c6a4419f7604d939548831fcab520039c6440b9f964592b9de8fa08ec5192ea1`. The prompt identifies the archival male source as the sole identity authority and the leader reference as style-only. |
| Processed candidate | `.../processed_png/portrait_AGX_friesland_coastal_council.png` | RGBA `156x210`, fully opaque, SHA-256 `dec3eb32366e500da0b4016df6bc7a96d3a02686ab57858944790f1e83233f3c`. Metadata records `mode = leader`, `role_family = leader`, `source_kind = real`, and no advisor composition or validation. |
| Independent audit | `006_agx_portrait_trial2_independent_audit_2026_07_26.md` | Provenance, crop equality, male role fit, likeness, HOI4 leader style, framing, ownership, and forbidden-derivative gates all PASS. |
| Promoted runtime DDS | `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_council.dds` | SHA-256 `85240ff6700bbebaed9eeba838f9b503d9d42a7e55cef6df2d8c71dc86c33d1e`, `131168` bytes, and equal to `review/promoted_runtime_portrait_AGX_friesland_coastal_council.dds`. |

### Pieter Reenalda coastal commander

| Artifact | Path | Verified facts |
| --- | --- | --- |
| Immutable source master | `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_26/frisia_pieter_reenalda_trial_02/source_masters/AGX_pieter_reenalda_1919_uniform_master.jpg` | Grayscale `1206x1765`, SHA-256 `8f93840b12ecdcb313279c6f0fd4027863f8c1c4c9232e699aa7a0a9d46668ce`. The source is the 1919 Tresoar maritime-uniform portrait documented in the retained source ledger. |
| Exact source crop | `.../source_crops/AGX_pieter_reenalda_1919_head_shoulders.png` and adjacent JSON | Grayscale `800x1077`, crop `(203,130,1003,1207)`, `status = exact_source_crop_verified`, `decoded_pixels_equal = true`, equality hash `c78c6344d50152e9a51303f0c495fcb0035fdb5afbe80e2f94348ebbbcece0db`. |
| Raw ImageGen result | `.../imagegen_results/AGX_pieter_reenalda_identity_preserve_trial_02.png` | RGB `1082x1454`, SHA-256 `3c9d6d44410d9001c791ac6a700689a94fc61fc6b62e7de06947ff1e67145e4d`. The prompt identifies the archival male source as the sole identity authority and the commander reference as style-only. |
| Processed candidate | `.../processed_png/portrait_AGX_friesland_coastal_commander.png` | RGBA `156x210`, fully opaque, SHA-256 `840e5708fa1c9f5424d5524bb93d661c39a5d888f85a34cad96d74cbcedbf856`. Metadata records `mode = leader`, `role_family = commander`, `source_kind = real`, and no advisor composition or validation. |
| Independent audit | `006_agx_portrait_trial2_independent_audit_2026_07_26.md` | Provenance, crop equality, male role fit, likeness, HOI4 commander style, framing, ownership, and forbidden-derivative gates all PASS. |
| Promoted runtime DDS | `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_commander.dds` | SHA-256 `e84d790ab245f5e14baadb71d0c66438dcb04586131f4b98893b0a4cbc8e8137`, `131168` bytes, and equal to `review/promoted_runtime_portrait_AGX_friesland_coastal_commander.dds`. |

The new source masters are byte-identical to the selected masters retained in the 2022-07-22 retry workspace, so the promotion did not silently replace source identity evidence.

## Promoted DDS header and pixel checks

Both runtime textures were parsed directly from disk.

| Check | Civic leader DDS | Commander DDS |
| --- | --- | --- |
| Magic and header | `DDS `, header size `124` | `DDS `, header size `124` |
| Declared dimensions | `156x210` | `156x210` |
| Pixel format | size `32`, flags `65`, fourCC `0`, 32-bit BGRA masks `0x00FF0000`, `0x0000FF00`, `0x000000FF`, `0xFF000000` | Same |
| Caps and length | `DDSCAPS_TEXTURE = 0x1000`, no secondary caps, exact length `128 + 156*210*4 = 131168` | Same |
| Alpha | Actual payload alpha min/max `255/255` | Actual payload alpha min/max `255/255` |
| Review-copy equality | Runtime equals promoted review DDS byte-for-byte | Runtime equals promoted review DDS byte-for-byte |
| Processed-PNG pixel identity | BGRA payload reordered to RGBA equals the processed PNG decoded pixels | BGRA payload reordered to RGBA equals the processed PNG decoded pixels |

The promoted hashes differ from the previous runtime review copies, which confirms that the parent promotion replaced the old bytes at the same stable paths.

- Previous civic runtime hash: `2a98ecb576b331915e2b626c9ccc6dc03af4012a411717b73d2f5253358e15a2`.
- Previous commander runtime hash: `07689a7045c145401e5aa7a2cfc1ae0949d59c62d4b64f144714e20197558bba`.

## Stable consumer and male-only gate

`GFX_portrait_AGX_friesland_coastal_council` occurs once in the `.gfx` file and points to the promoted civic DDS.

`GFX_portrait_AGX_friesland_coastal_commander` occurs once in the `.gfx` file and points to the promoted commander DDS.

`AGX_friesland_coastal_council` is recruited once in AGX history, has `gender = male`, uses `civilian.large`, and has only centrism, socialism, and oligarchism country-leader roles.

`AGX_friesland_coastal_commander` is recruited once in AGX history, has `gender = male`, uses `army.large`, and has the intended corps-commander role.

The explicit names `Douwe Kalma` and `Pieter Reenalda` are localized character names, not random name-pool outputs.

No AGX-specific `female = yes`, female name pool, opposite-gender name assignment, or generated startup name path was found in the checked character, history, country, names, or general-character surfaces.

The role metadata and source/candidate review therefore satisfy the male-only requirement for both runtime consumers.

## Forbidden derivative and stale-surface checks

The active 2026-07-26 trial workspaces contain no advisor portrait, high-command card, operative portrait, dossier card, `50x67` output, `_small` derivative, female asset, generated-generic substitute, or alternate-person asset.

The processed metadata invokes the shared `the retired portrait-processing utility` implementation in `leader` mode, but `advisor_composition`, `advisor_validation`, all overlay and paper fields, and all advisor manifests are `null`, so the processor filename is not an advisor-card consumer.

The runtime source search finds only the two intended full-size AGX portrait sprites and their two `large` character consumers.

The older 2022-07-22 `frisia_retry_02/gfx_handoff.md` is now explicitly marked
historical and superseded, while the 2026-07-26 manifests, promoted review
copies, runtime hashes, and `.gfx` paths show the current state.

## Existing AGX package gates and non-portrait surfaces

The IW-007 adapter and static content attestation remain present at `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-20,55-68,90-104`, with `iw_007` paired to `original_tag = AGX`.

The command-roster predicate still requires both AGX characters at `common/scripted_triggers/006_independence_wave_wallonia_frisia_package_triggers.txt:72-75`.

Tag registration, state 36 and RG-36 binding, politics, parties, flags, ideas, focus assignment, decisions, force mapping, technology inheritance, industry, supply, production, AI, formable hooks, cleanup, and localisation were not changed by this portrait promotion.

The prior country-package audit remains the authority for those surfaces and still records AGX as PARTIAL because the conference decision lane and shared focus geometry remain HOLD, while live allocation and save-load evidence remain unproven.

No map or state setup issue was introduced, and no advisor or dossier requirement exists in the accepted AGX portrait contract.

## Validation and skipped checks

Meaningful checks run for this post-wire audit were:

- Recomputed SHA-256 hashes and Pillow dimensions for both source masters, exact crops, raw results, processed candidates, review sheets, and promoted runtime DDS files.
- Recomputed exact crop equality from each immutable master and confirmed both JSON records report `exact_source_crop_verified` and `decoded_pixels_equal = true`.
- Parsed both runtime DDS headers, masks, caps, exact lengths, and actual alpha extrema.
- Reordered each BGRA runtime payload to RGBA and confirmed decoded pixel identity with its promoted processed PNG.
- Confirmed each runtime DDS equals its promoted review copy and differs from its retained previous-runtime copy.
- Counted the stable `.gfx` sprite definitions and traced both character tokens through character definitions, AGX history recruitment, localisation, and runtime texture paths.
- Searched active runtime and 2026 trial surfaces for female metadata, opposite-gender name paths, advisor, dossier, `_small`, `50x67`, generated-generic, and alternate-person derivatives.
- Inspected both independent review sheets at native review scale and relied on the producer-separate trial-02 audit for the required native and `4x` likeness/style/provenance comparisons.

Skipped live HOI4 loading, save-load validation, scenario allocation, and MCP render checks because this audit is restricted to post-wire portrait evidence and the parent owns live consumer validation.

Skipped broad AGX gameplay re-audit because the current `006_agx_country_package_reaudit_2026_07_26.md` remains the accepted authority and the portrait promotion did not touch those files.

No fallback, simplification, or replacement identity was used.

## Handoff to parent

The portrait/runtime tranche is **PASS** and may remain admitted under the existing IW-007 static package gate.

The parent should retain the promoted runtime hashes above, treat the older deferred-conversion handoff as historical documentation debt, and keep the unrelated AGX decision, shared-focus, and live-attestation findings from the prior package audit unchanged.

Changed files in this audit: this handoff only.
