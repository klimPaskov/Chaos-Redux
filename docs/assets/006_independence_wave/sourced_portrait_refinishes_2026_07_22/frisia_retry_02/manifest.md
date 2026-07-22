# IW-007 Frisia portrait refinishes — retry 02

Date: 2026-07-22

Package status: `approved_wired_pending_country_package_reaudit`.
This package is an identity-preserving edit pass for two grounded real-person
portraits. AGX/Frisia is a plausibly historical regional polity, so the source
mode remains `grounded_source_only`; ImageGen was used only to apply the HOI4
painted finish to an unchanged, attributed source master. No fictional face,
generic substitute, gender swap, advisor portrait, `_small` portrait, flag, or
runtime/GFX edit was made.

The selected source masters are copied byte-for-byte from the committed source
package. The 1915 and 1911 Reenalda images are comparison/context only and were
not supplied to ImageGen and are not runtime identities in this package.

## Source identity and ownership gate

The source package recorded exact-person searches for `Douwe Kalma`,
`Kalma, Douwe`, `Douwe_Kalma`, `Pieter Reenalda`, `Reenalda, Pieter`,
`Pieter_Reenalda`, and `Reenalda`. It reports no vanilla character, leader,
commander, operative, portrait, interface, or localisation consumer for either
person. Chaos Redux has only the intended AGX display strings and the AGX
character owners; both are explicitly male. No transfer/availability guard is
needed because no origin roster owns either person. See the source authority at
`docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/frisia_retry_02/manifest.md`.

The selected masters and attribution are:

- Douwe Kalma, circa 1917, F.O. Strüppert/Tresoar, public domain: [Commons file page](https://commons.wikimedia.org/wiki/File:Portret_fan_Douwe_Kalma,_1917_ca._archiefnr_1990.jpg), [unchanged original](https://upload.wikimedia.org/wikipedia/commons/d/d6/Portret_fan_Douwe_Kalma%2C_1917_ca._archiefnr_1990.jpg), [Tresoar record](https://tresoar.nl/zoeken/collectie/cf64b17f-5d0c-46f9-9209-a7f60c185068).
- Pieter Reenalda, 1919 maritime-uniform portrait, unknown maker/Tresoar, public domain: [Tresoar record](https://tresoar.nl/zoeken/collectie/4fddaece-1058-470b-be2a-29e4e9e236ac). The source manifest identifies this as the selected retry master and records the archive/Commons public-domain basis.

## Asset rows

### IW-007 civic leader — Douwe Kalma

- Identity/role: real male Douwe Kalma; AGX civic leader `AGX_friesland_coastal_council`.
- Stable sprite: `GFX_portrait_AGX_friesland_coastal_council`.
- Source mode: `grounded_source_only` + identity-preserving ImageGen edit.
- Exact source master: `source_masters/AGX_douwe_kalma_1917.jpg`; native `691x1013`, RGB; SHA-256 `38dafcbff7c3a67b6b29b9b637e69ff4c2f9d8caae076361200919a6bb36dbdf`.
- Source crop box (left, top, right, bottom; source pixels): `(48, 62, 643, 864)`.
- ImageGen prompt: `prompts/leader_douwe_kalma_identity_preserve.txt`.
- Style-only reference: `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/leaders/den_thorvald_stauning.png`, native `156x210`; no identity transfer.
- Raw ImageGen master: `raw_masters/leader_douwe_kalma_imagegen_2026-07-22.png`; native `1069x1472`, RGB; SHA-256 `222c7f75bbf24a4167151bb96aa3f256b4f50938f14dc4739de7df6fa2f53238`.
- Raw result crop box: `(34, 58, 1035, 1405)`.
- Processed PNG preview: `processed_png/AGX_friesland_coastal_council.png`; `156x210`, RGBA opaque; SHA-256 `644e37c3ffbcfa871af22bcb6cf9e575cbfa16bdd2cc30b253e2f65c440277a8`.
- Native comparison sheet: `contact_sheets/native_source_result_style_comparison.png` (source, raw result, and style reference shown at native scale).
- Visual self-review: the face, direct gaze, center pose, swept hair, forehead source mark, collar, patterned tie, jacket, and shoulder silhouette remain recognizable in a direct source/result comparison. The edit is full-color and restrained rather than sepia or monochrome. Possible subtle eye/jaw symmetry drift remains; **status `needs_independent_visual_audit`**, not approved.
- Runtime/DDS: converted after independent PASS to `final_dds/AGX/portrait_AGX_friesland_coastal_council.dds` and copied byte-for-byte to the authoritative existing texture path `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_council.dds`; SHA-256 `2A98ECB576B331915E2B626C9CCC6DC03AF4012A411717B73D2F5253358E15A2`. The stable sprite definition was not renamed.

### IW-007 coastal commander — Pieter Reenalda

- Identity/role: real male Pieter Reenalda; AGX coastal commander `AGX_friesland_coastal_commander`.
- Stable sprite: `GFX_portrait_AGX_friesland_coastal_commander`.
- Source mode: `grounded_source_only` + identity-preserving ImageGen edit.
- Exact selected source master: `source_masters/AGX_pieter_reenalda_1919_uniform.jpg`; native `1206x1765`, grayscale `L`; SHA-256 `8f93840b12ecdcb313279c6f0fd4027863f8c1c4c9232e699aa7a0a9d46668ce`.
- Source crop box (left, top, right, bottom; source pixels): `(0, 48, 1206, 1672)`.
- Review-only source crop preview: `processed_png/AGX_friesland_coastal_commander_source_crop_preview.png`; `156x210`, RGBA opaque; SHA-256 `b1894163b1e94b2ed1b50460fc6e1d840ed5aa0c0616826ddc83a45fdee20bdf`. This is the unchanged grayscale source crop, not a runtime candidate.
- ImageGen prompts: `prompts/commander_pieter_reenalda_identity_preserve_candidate_01.txt` and `prompts/commander_pieter_reenalda_identity_preserve_candidate_02.txt`.
- Style-only references: `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/commanders/generic_africa_navy_2.png` (candidate 01) and `generic_africa_navy_1.png` (candidate 02), both native `156x210`; no identity transfer.
- Raw candidate 01: `raw_masters/commander_pieter_reenalda_imagegen_candidate_01_2026-07-22.png`; native `1081x1455`, RGB; SHA-256 `cdc0c7fb893ee980ec5be0e94cfb8df0aabcf455252c90aee4c62e2cd58ef2d1`.
- Candidate 01 crop box: `(0, 0, 1081, 1455)`.
- Candidate 01 processed preview: `processed_png/AGX_friesland_coastal_commander_candidate_01.png`; `156x210`, RGBA opaque; SHA-256 `e6e2e20791823f4f21edf5cf295fbfbbde68382619111c2431ab91e093df9647`.
- Candidate 01 status: **`blocked`** for visible identity drift in the eye/cheek proportions and more assertive invented shoulder-board color; retained only for independent comparison, never as the runtime result.
- Raw candidate 02 (selected retry result): `raw_masters/commander_pieter_reenalda_imagegen_candidate_02_2026-07-22.png`; native `1080x1456`, RGB; SHA-256 `eb5d9e6ee35ba6a44ddf9b2e307c42da1b0f5bdaf7df273487350e5c6ad5a8b3`.
- Candidate 02 crop box: `(0, 0, 1080, 1454)`.
- Candidate 02 processed PNG preview: `processed_png/AGX_friesland_coastal_commander.png`; `156x210`, RGBA opaque; SHA-256 `25a3c29b6b9deeda87d0e96699beb44d2d2d7051a5335af61f630cb5d918c968`.
- Native comparison sheet: `contact_sheets/native_source_result_style_comparison.png` (source, both raw candidates, and the style reference shown at native scale).
- Visual self-review of candidate 02: the broad face, direct gaze, side-parted hair, large horizontal moustache, centered head, high-collared maritime uniform, buttons, pocket chain, and shoulder-board silhouette remain recognizable. Color stays muted and uncertain insignia are neutral rather than assigned national colors. Eye/cheek proportions and fine moustache geometry may still be subtly altered; **status `needs_independent_visual_audit`**, not approved.
- Runtime/DDS: converted after independent PASS to `final_dds/AGX/portrait_AGX_friesland_coastal_commander.dds` and copied byte-for-byte to the authoritative existing texture path `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_commander.dds`; SHA-256 `07689A7045C145401E5AA7A2CFC1AE0949D59C62D4B64F144714E20197558BBA`. The stable sprite definition was not renamed.

## Review evidence and conversion boundary

- Source-vs-result-vs-style evidence: `contact_sheets/native_source_result_style_comparison.png`.
- Dimensions, crop boxes, and SHA-256 values for every retained source/raw/processed file are in `hashes.sha256`.
- Both unchanged selected source copies are retained under `source_masters/`; the source package's 1915/1911 Reenalda files were deliberately not reused as edit inputs.
- The official built-in ImageGen edit workflow was used. No rejected prior ImageGen portrait was refined or reused.
- The independent audit at `docs/plans/006_independence_wave_plans/subagent_handoffs/006_frisia_retry_02_independent_visual_audit_2026_07_22.md` passes Kalma and Reenalda candidate 02 and keeps candidate 01 fail-closed. The two approved processed PNGs were converted with the repository-standard converter to one-level uncompressed BGRA DDS files. Both runtime DDS files are `156x210`, 131168 bytes, opaque, and decode pixel-identically to their processed PNGs. IW-007 still requires a fresh country-package re-audit before compile-time content attestation.
