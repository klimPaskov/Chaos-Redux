# Event 006 IW-177 Fiji portrait source and rights gate

Audit date: 2026-08-14.

Scope: read-only source, rights, identity, role/date, framing, and ownership audit for the exact 1936 opening-leader consumer `FIJ_independence_wave_founding_congress_chair` / Ratu Sir Lala Sukuna. This handoff does not edit gameplay, character identity, localisation, central attestation, Join, readiness, FORM-39, `.gfx`, or runtime assets.

## Disposition

**FAIL CLOSED / `needs_user_review`. No grounded source clears the strict 1936 gate.**

Event 006 remains outside the requested authority boundary: 40 runtime adapters, 32 content-attested packages, 29 compatible reservation groups, and 161 selectable rows still unattested. IW-177 remains adapter-only and must not be added to the central attestation or readiness surface from this audit.

The subject is grounded real person material (`grounded_source_only`). Native ImageGen is not an allowed identity source, and no new ImageGen or RunPod work was performed. An existing source-linked repaint/candidate is evidence only and is not approved or treated as a source substitute.

## Locked runtime consumer

| Surface | Existing value | Audit result |
| --- | --- | --- |
| Character | `common/characters/006_independence_wave_pacific_characters.txt` → `FIJ_independence_wave_founding_congress_chair` | Existing male country-leader record; unchanged |
| Name and role | `Ratu Sir Lala Sukuna`; founding-congress chair | Identity/role fit is strong for Sukuna, but source date fails the 1936 image gate |
| Sprite | `GFX_portrait_FIJ_independence_wave_founding_congress_chair` | Existing stable portrait-specific sprite; unchanged |
| `.gfx` | `interface/006_independence_wave_pacific_portraits.gfx` | Existing definition; unchanged |
| DDS | `gfx/leaders/006_independence_wave/portrait_FIJ_independence_wave_founding_congress_chair.dds` | Existing provisional consumer only; not admitted by this audit |
| Gender/name pool | male | Matches the grounded male source requirement |

The existing DDS is `156x210`, 32-bit uncompressed BGRA with a valid legacy header and SHA-256 `31fea5eb5c7c4b6f34ec138ed6a3168a7c6c39755a992bd6abf0296c5838d2c6`. It remains provisional and is not a source, rights, or package-admission pass.

## Candidate gate results

### Ratu Sir Lala Sukuna

**Identity and role:** Strong fit. Ratu Sir Josefa Lalabalavu Vanayaliyali Sukuna (1888–1958) is a real Fijian chiefly statesman and former soldier, and the retained research records him as the Fiji Legislative Council representative for Fijians from 1932. That supports the existing founding-congress-chair concept and the 1936 political activity window.

**Attributed source and rights:** The strongest retained source is the National Archives of Fiji portrait published through [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Ratu_Sir_Lala_Sukuna.jpg), with the [direct original](https://upload.wikimedia.org/wikipedia/commons/7/73/Ratu_Sir_Lala_Sukuna.jpg) and the credited [National Archives post](https://www.facebook.com/NationalArchivesOfFiji/photos/a.124204611046400/124206027712925/). Commons records a `PD-Fiji` public-domain basis ([template](https://commons.wikimedia.org/wiki/Template:PD-Fiji)); this is a bounded Commons metadata claim, not a fresh permission statement from the archive. Archive credit must remain attached to any future documentation.

**Date gate:** **FAIL.** The source metadata says **circa 1940s**, not 1936 or earlier. No retained metadata supplies a precise capture date or photographer. The source must not be described as a 1936 photograph or used as silent evidence of Sukuna's 1936 appearance.

**Retained source evidence:**

- Flat durable original: `docs/assets/portraits/006_independence_wave/portrait_FIJ_ratu_sir_lala_sukuna_source.jpg`, `2520x3128` RGB, SHA-256 `8cf20454f59f8644b3c34dd9ea40a7e98cdf5b56113cd8bb918f893fc6cff5e5`.
- Source-clearance copy: `docs/assets/006_independence_wave/fiji_source_clearance_2026_07_27/ratu_sir_lala_sukuna_source.jpg`, byte-identical to the flat original.
- Existing exact crop evidence: `ratu_sir_lala_sukuna_crop.png`, `1920x2300`, crop rectangle `(300,250)-(2220,2550)`, decoded-pixel equality `true`, crop SHA-256 `c19b8c31fcee03457645a4d35e5ad0453fffeeb76823a6da032fc14ac85faf7e` on the current file.
- Existing deterministic `156x210` review candidate: `ratu_sir_lala_sukuna_hoi4.png`, SHA-256 `71062c2efe0e98d3de1de5e7d5600e2bc746b92f6560c44d62242c107b26951d`; evidence-only and not a durable archive output or admission.
- Existing independent visual handoff: `006_iw177_fiji_sukuna_portrait_visual_audit_2026_07_27.md`; bounded identity, male framing, crop, style, and provenance checks pass, while the circa-1940s date remains the controlling blocker.

### Pt. Vishnu Deo

**Identity and date:** The retained [Internet Archive scan](https://archive.org/details/dli.calcutta.09841) is the October 1929 *Modern Review* page 459, captioned “Mr. Vishnu Deo”; the [high-resolution page image](https://archive.org/download/dli.calcutta.09841/page/n474_w4000.jpg) is period-valid for a 1936-centered visual.

**Role gate:** **FAIL for the exact consumer.** Vishnu Deo is a defensible Fiji-born Indo-Fijian political and communal leader, but the retained research records Legislative Council service in 1929 and again from 1937, not during the 1936 baseline. He cannot silently replace the existing named Sukuna founding-congress-chair role. Admitting him would require an explicit parent design change to the identity, role, and localisation, which is outside this audit.

**Rights and likeness:** The image is an anonymous halftone reproduction. Wikimedia Commons identifies the publication and applies a `PD-India` public-domain claim, but no photographer or higher-resolution original is identified. The rights/likeness chain remains bounded and is not sufficient for runtime admission without independent review and an explicit role decision.

**Retained source evidence:**

- Flat durable original: `docs/assets/portraits/006_independence_wave/portrait_FIJ_vishnu_deo_source.jpg`, `277x543` RGB, SHA-256 `680ae01b3e87937335321369c197a2d63f56b469608e700781639e2d0f1b8719`.
- Higher-resolution period scan: `docs/assets/006_independence_wave/sources/fij_vishnu_deo_2026_08_01/n474_w4000.jpg`, `4248x5866` RGB, SHA-256 `9e94a391473850efbcec3f08c3ccbc08ba588e1a52af908fe08727cc2ae658c5`.
- Existing exact crop: `vishnu_deo_modern_review_crop.png`, `1040x1460`, rectangle `(2520,1060)-(3560,2520)`, decoded-pixel equality `true`, SHA-256 `a3e427e0a2ede7bdb72736c4e9d372188003a0e6142548d1884951507d76b3d0`.
- Existing 1929 review thumbnail and source-linked repaint evidence remain review-only; no FIJ runtime replacement is authorized.

### Other retained Sukuna images

The Fiji Times/Fiji Museum library image has no capture date or reusable license. The iTaukei Affairs ceremony image has no capture date or reuse permission; its modern EXIF save date is not a capture date. Ministry/USP commemorative graphics are modern composites, and the Find a Grave image depicts a monument rather than the person. None clears the grounded source gate.

## Ownership and reference checks

The exact and variant terms `Sukuna`, `Lala Sukuna`, `Josefa Lalabalavu`, `Vanayaliyali Sukuna`, `Vishnu Deo`, and `Vishnu_Deo` were checked across project and targeted installed-vanilla `common/characters`, `history/countries`, `gfx/leaders`, `interface`, and `localisation` roots. No pre-existing vanilla or Chaos Redux character/portrait owner was found. The only project localisation match is the existing FIJ consumer itself. No transfer or clone is authorized.

The canonical installed-vanilla country-leader reference family was inspected at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/`, including the `156x210` leader references and contact sheet. The retained Sukuna visual audit compares against `den_thorvald_stauning.png` and `fin_carl_mannerheim.png`; this confirms framing/style only and does not supply identity or rights.

The offline Paradox portrait and graphical-asset pages confirm the full `156x210` leader surface and `.gfx` `spriteType`/`texturefile` relationship. Vanilla documentation was consulted for `set_country_leader_portrait`, `set_leader_portrait`, and portrait sprite usage. These engine references do not waive source, date, or rights gates.

## Archive and output state

The durable portrait parent remains flat at `docs/assets/portraits/006_independence_wave/`: FIJ Sukuna and Vishnu originals are at the parent root, and the `processed/` directory contains no FIJ processed outputs. No `156x210` archive file was created. Existing event-scoped review evidence remains under `docs/assets/006_independence_wave/`; it is not copied into the durable flat archive by this fail-closed audit.

No files other than this handoff were changed by this audit. No new source download, crop, PNG, DDS, `.gfx` entry, character reference, manifest, attestation, Join branch, or central authority edit was made.

## Skipped checks and exact blockers

The following were intentionally not advanced because no candidate cleared the source/rights/role/date gate:

- no new `extract_portrait_source_crop.py` run or archive promotion;
- no source-placeholder selection for the exact FIJ consumer;
- no user-supplied styled-final validation and no `replacement_pending` state;
- no DDS conversion through `convert_to_dds.py` and no runtime promotion;
- no final portrait wiring or runtime replacement;
- no central attestation/readiness/Join or FORM-39 change;
- no RunPod access or operation.

The controlling unblock request is a high-resolution National Archives of Fiji, Fiji Museum, or iTaukei archival scan of Sukuna (or an explicitly accepted role-equivalent male Fiji representative) with a documented capture date no later than 1936 and reusable rights. If the parent accepts the circa-1940s exception or changes the exact identity/role to Vishnu Deo, that must be an explicit design decision with a fresh independent source/identity/framing/provenance review; neither candidate is admitted by this handoff.
