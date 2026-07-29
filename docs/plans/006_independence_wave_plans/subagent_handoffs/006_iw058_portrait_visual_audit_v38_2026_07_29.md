# IW-058 ASY sourced leader portrait visual audit v38

Audit date: 2026-07-29. Scope: independent audit of the three grounded real-person ASY/IW-058 leader portrait candidates in `docs/assets/006_independence_wave/asy_roster_clearance_v37_2026_07_29/`. Reviewed the current manifest, GFX handoff, `imagegen_generation_record.md`, source masters, exact-crop PNGs and JSON evidence, raw ImageGen masters, processed 156x210 candidates, three processing review sheets, source contact sheet, hashes, and the canonical skill reference contact sheet at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/contact_sheet.png` with its eight 156x210 leader references.

This is an independent visual/provenance audit, not runtime approval. No DDS promotion or `.gfx` change is authorized until every gate below is PASS and the route-specific historical blockers are resolved. The processing review sheets show the candidate and two selected vanilla references, but do not provide a separate 4x nearest-neighbour comparison panel; native/original-size files were inspected directly for this audit.

## Gate summary

| Subject and consumer | Source/provenance/rights | Identity and likeness | HOI4 painted leader style | Crop/readability at 156x210 | Historical/role suitability | No vanilla/KR/approved-mod ownership collision | Overall |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Ignatius Afram I Barsoum — `ASY_independence_wave_concordat_council` | **FAIL** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | **BLOCKED / needs_user_review** |
| Rev. Joel E. Werda/Warda — `ASY_independence_wave_civic_national_assembly` | **PASS** | **FAIL** | **PASS** | **PASS** | **FAIL** | **PASS** | **BLOCKED / needs_user_review** |
| Malik Ismail II of Upper Tyari — `ASY_independence_wave_levies_guardianship` | **PASS** | **PASS** | **PASS** | **PASS** | **FAIL** | **PASS** | **BLOCKED / needs_user_review** |

The repository's prefixed decoded-RGBA contract is verified for every candidate, raw repaint, and review PNG, so no decoded-hash blocker remains. The aggregate source/provenance/rights gate is FAIL only for Afram because the Commons PD-Syria rationale has an explicit jurisdiction-review requirement; Werda and Malik have complete recorded source, rights, crop, generation, and hash evidence for this gate.

## Cross-package provenance and processing finding

The source masters match the package ledger and `hashes.sha256`, and all three crop JSON records report Pillow exact-pixel equality. The common generation record documents the identity-preserving ImageGen constraints and style-only reference use. The processor's decoded-RGBA contract prefixes `b"chaos-redux-decoded-rgba-v1\0"`, then appends 4-byte little-endian width and height followed by RGBA bytes; recomputation with Pillow 11.1.0 matches every candidate, raw-master, and review-sheet decoded hash recorded in the package. No hash repair or provenance-integrity blocker remains.

| Subject | Candidate decoded RGBA SHA | Raw-master decoded RGBA SHA | Review decoded RGBA SHA | Contract result |
| --- | --- | --- | --- | --- |
| Ignatius Afram I Barsoum | `5649d3d739536735a5c9d3def404bcd8dc3316371fc678602377bda406398e52` | `cd9d4db617dc8a8b519433518624e8da0afb64747bd61c265eb9ec132110a269` | `df11d9255bd4fafd13f203afbf4a2be1a7f34e3ac69d06d72a46f838ec7977ca` | **PASS** |
| Rev. Joel E. Werda/Warda | `c089b2a38ed48e00a9e8c19a8606bdd070deefd781bb3dc6829c31bd3e307b20` | `2a29c717247968e0067c4b7c934421101e13c09bdfd2610a9cfe9f3e1eb9ef80` | `6a49c60f4474bb09177bf176c890c54588ccee2ef42392b15074a38af1946ebb` | **PASS** |
| Malik Ismail II | `eaf582d0828c7e70ac316616017f0f1828b5b5ef11fb2e9aa5eb3517ff0d3a61` | `4ad5f01ecd109d1cf610d831f485a74e82b2d419dd018b669681c2a58dba1d46` | `af05e318fa6346999fe23735dd1bf6fa4ca95196e83ce1b724ec9200560db93f` | **PASS** |

The source-rights subchecks are documented as follows: Afram is a Commons PD-Syria assertion with unknown image date and an explicit jurisdiction-review note; Werda is a Commons PD-US-expired assertion for the 1921 publication with unknown author; Malik is a PCUSA/Commons Public Domain Mark assertion. The latter two source-rights records are sufficient for PASS in this audit; Afram remains conditional on the explicit jurisdiction review.

## Ignatius Afram I Barsoum

| Gate | Verdict | Evidence and strict finding |
| --- | --- | --- |
| Source/provenance/rights | **FAIL** | The 500x656 Commons/eSyria source is hash-matched, the `(70,20)-(430,540)` crop has exact Pillow equality, the generation record identifies the source-locked repaint, and the prefixed decoded-RGBA hashes recompute exactly. The Commons PD-Syria rationale has unknown image date/author and explicitly needs jurisdiction review, so the rights gate remains conditional. |
| Identity and likeness preservation | **PASS** | The archival source, crop, raw repaint, and 156x210 candidate retain the broad black ecclesiastical headwear, long white beard, facial proportions, central gaze, dark robes, and visible medal arrangement. I found no face substitution, generic officeholder face, or unsupported military insignia in the repaint. The colorized painterly treatment changes tone but not the distinctive identity geometry. |
| HOI4 painted leader style | **PASS** | The raw and processed portraits use subdued period colour, controlled contrast, a quiet textured background, head-and-shoulders framing, and a coherent painted finish that sits comfortably beside the Stauning and Mannerheim references in the canonical leader contact sheet. |
| Crop/readability at 156x210 | **PASS** | The immutable crop is a verified 360x520 RGB crop, and the processed candidate is exactly 156x210 RGBA with an opaque canvas. Hat, eyes, beard, robe silhouette, and enough medals remain legible at native size. The review sheet is a comparison aid only and lacks a dedicated 4x panel, but direct inspection shows no unreadable face or destructive crop. |
| Historical/role suitability | **PASS** | Ignatius was a real 1936-active Syriac Orthodox patriarch, and the current manifest explicitly defines the concordat route as multi-church with a distinct Syriac Orthodox chamber rather than treating him as the sole voice of all Assyrian communities. The route framing is historically and institutionally suitable as recorded. |
| No exact vanilla/Kaiserreich/approved-mod character ownership collision | **PASS** | The current manifest records a scan across Chaos Redux, installed vanilla, and approved workshop mods `1521695605`, `2265420196`, and `1458561226`, with no owner for this identity and no transfer guard needed. The listed Shimun, Dawid Shimun, Yusuf Malek, Malik Yaqo, Yosip Khoshaba, Qambar Warda, and Benjamin Arsanis collisions are rejected alternatives, not this subject. |

Disposition: **BLOCKED / needs_user_review**. Keep the source, crop, raw repaint, processed PNG, and evidence; do not convert or wire until the PD-Syria jurisdiction note is accepted. The route-level multi-church representation and decoded metadata are accepted by the current package design and processor contract.

## Rev. Joel E. Werda/Warda

| Gate | Verdict | Evidence and strict finding |
| --- | --- | --- |
| Source/provenance/rights | **PASS** | The 283x378 L source hash matches the ledger, the Commons record gives circa-1920 attribution to the 1921 *Babylon* publication and a PD-US-expired claim, the full-frame source crop has exact Pillow equality, the common generation record is present, and the prefixed decoded-RGBA hashes recompute exactly for the raw, candidate, and review artifacts. The low source resolution is recorded under identity, not rights/provenance. |
| Identity and likeness preservation | **FAIL** | The raw repaint and candidate retain the broad round face, heavy brow, close period haircut, suit, tie, and lapel pin, but the archival source is only 283x378 and visibly soft. The repaint invents high-frequency facial detail and smooths the expression enough that exact asymmetry, age, and small identity markers cannot be proven from the supplied master. This remains a low-resolution identity candidate, not a compensable style pass. |
| HOI4 painted leader style | **PASS** | The raw and processed portraits have the correct restrained bust framing, muted painted modelling, neutral background, controlled contrast, and no text/frame. The candidate is visually in-family with the canonical leader references despite the source softness. |
| Crop/readability at 156x210 | **PASS** | The source file is itself the Commons-supplied single-person crop, and the exact-crop JSON proves the retained full-frame rectangle without decode drift. The raw repaint then uses a subject-focused crop, and the 156x210 candidate keeps the face, suit, tie, and lapel pin readable at native size. The low-resolution softness is an identity-evidence problem recorded separately, not a destructive crop or unreadable runtime canvas. |
| Historical/role suitability | **FAIL** | The Paris Peace Conference/Assyrian National Association evidence supports the civic-national assembly concept, but no reliable birth/death or later-life record was established for a 1936 baseline. Living/officeholder status at the actual IW-058 event date must be established before this named leader can be admitted. Werda/Warda spelling must also be normalized in the consumer. |
| No exact vanilla/Kaiserreich/approved-mod character ownership collision | **PASS** | The manifest's current-project, vanilla, and approved-mod scan reports no owner for Joel E. Werda/Warda and no transfer guard requirement. The Qambar Warda collision listed in the manifest is a different rejected person. |

Disposition: **BLOCKED / needs_user_review**. Do not promote this candidate without a low-resolution identity review that can support exact likeness and a verified 1936 life/office date. The supplied crop, 156x210 readability, and decoded metadata are acceptable.

## Malik Ismail II of Upper Tyari

| Gate | Verdict | Evidence and strict finding |
| --- | --- | --- |
| Source/provenance/rights | **PASS** | The 1042x1669 PCUSA/Commons source is hash-matched and carries a Public Domain Mark note; the `(180,70)-(860,1200)` crop has exact Pillow equality, the generation record pins the Tyari-specific preservation constraints, and the prefixed decoded-RGBA hashes recompute exactly for the raw, candidate, and review artifacts. |
| Identity and likeness preservation | **PASS** | The archival source, crop, raw repaint, and candidate preserve the tall Tyari headwear, narrow face, moustache, eyes and wrinkles, embroidered dress, dark outer garment, and visible cane/dagger hilt. The repaint does not add British rank marks, invented medals, or a replacement face, and the processed candidate remains recognisably the same subject. |
| HOI4 painted leader style | **PASS** | The candidate has a subdued painterly treatment, controlled dark background, clear facial modelling, restrained bust crop, and strong silhouette consistent with the canonical leader-family examples. |
| Crop/readability at 156x210 | **PASS** | The immutable crop is a verified 680x1130 RGB crop centered on the subject, and the candidate is exactly 156x210 RGBA with an opaque canvas. Hat, face, moustache, embroidered shirt, and cane remain readable at native size; edge figures are not carried into the repaint. |
| Historical/role suitability | **FAIL** | Malik Ismail II is directly role-suitable as an Assyrian Tyari malik/chieftain and commander-in-chief of Assyrian volunteers, but the source record places his death in 1936 without pinning the exact date. The IW-058 event date must be proven to fall while he could still hold the office; until then the candidate cannot pass the historical gate. |
| No exact vanilla/Kaiserreich/approved-mod character ownership collision | **PASS** | The manifest's scan across Chaos Redux, installed vanilla, and approved workshop mods found no current owner for Malik Ismail II and no transfer guard requirement. The Malik Yaqo, Dawid Shimun, and other listed collisions are separate rejected candidates. |

Disposition: **BLOCKED / needs_user_review**. Confirm the event date against Malik Ismail II's death/office timeline before DDS conversion or runtime admission; the source, crop, generation, and decoded metadata evidence are otherwise coherent.

## Parent actions required

1. Resolve the remaining route-specific gates: PD-Syria jurisdiction for Afram, 1936 life/office status for Werda/Warda, and the exact IW-058 date relative to Malik Ismail II's 1936 death.
2. Keep all three candidates at `candidate_requires_visual_approval` or `needs_user_review`; do not overwrite DDS files or alter stable `.gfx` sprites until each row has a fresh independent PASS across all six gates.

No gameplay, GFX, localisation, DDS, source, repaint, manifest, or skill files were edited by this audit. Only this handoff was added.
