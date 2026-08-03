# IW-177 Fiji sourced-asset research and admission recommendation (2026-08-03)

## Scope

This handoff covers only the sourced visual-asset gate for Event 006 / IW-177 (FIJ). It does not edit gameplay, country history, tags, readiness, localisation, GFX, or runtime files. The question is whether a defensible real male Fiji identity and historical-symbol source can be admitted for the 1936-centered package.

## Admission decision

**Status: BLOCKED / needs_user_review. Do not admit FIJ/IW-177 to the sourced-content attestation yet.**

No currently identified portrait candidate passes all of the strict gates at once: grounded identity, role/community fit for the FIJ package, an attributed source, and a capture date no later than the 1936 baseline. The strongest role match is Ratu Sir Lala Sukuna, but the only attributed source currently retained is explicitly dated “circa 1940s.” The only period-valid image found in the current sweep is Pt. Vishnu Deo in an October 1929 publication; he is a defensible Indo-Fijian civic/community alternate, but he was not a Fiji Legislative Council member in 1936 (he returned in 1937), and the retained source is an anonymous halftone. Neither candidate may be silently promoted as a 1936 FIJ Council-chair portrait.

## Candidate review

| Candidate | Identity and package fit | Source and rights | Date / era fit | Gate result |
| --- | --- | --- | --- | --- |
| **Ratu Sir Josefa Lalabalavu Vanayaliyali Sukuna (1888–1958)** | Fijian chiefly/Bauan lineage; Fiji Legislative Council representative for Fijians from 1932; constitutional and communal bridge; former soldier. This is the strongest fit for the existing FIJ founding-congress-chair role and the current localisation. | Wikimedia Commons page [File:Ratu Sir Lala Sukuna.jpg](https://commons.wikimedia.org/wiki/File:Ratu_Sir_Lala_Sukuna.jpg); direct source [original JPG](https://upload.wikimedia.org/wikipedia/commons/7/73/Ratu_Sir_Lala_Sukuna.jpg); credited to the National Archives of Fiji via [National Archives post](https://www.facebook.com/NationalArchivesOfFiji/photos/a.124204611046400/124206027712925/); Commons rights template [PD-Fiji](https://commons.wikimedia.org/wiki/Template:PD-Fiji). | Commons/source note is **circa 1940s**; no precise capture date or photographer is supplied. It must not be described as a 1936 photograph. | **Needs user review / blocked under strict 1936 gate.** Role and identity are strong; date is outside the requested baseline. |
| **Pandit Vishnu Deo (1900–1968)** | Fiji-born Indo-Fijian political and communal leader; Arya Samaj leader; *Fiji Samachar* editor; associated with the Fiji Indian National Congress (Lautoka, 1929). Period-valid as a civic/community voice, but he was not a Council member during 1936 and returned to the Council in 1937. | Commons page [File:Vishnu Deo Fiji.jpg](https://commons.wikimedia.org/wiki/File:Vishnu_Deo_Fiji.jpg); direct Commons JPG [Vishnu Deo Fiji.jpg](https://upload.wikimedia.org/wikipedia/commons/7/7a/Vishnu_Deo_Fiji.jpg). Higher-resolution period scan: Internet Archive item [dli.calcutta.09841](https://archive.org/details/dli.calcutta.09841), page image [Modern Review p. 459 scan](https://archive.org/download/dli.calcutta.09841/page/n474_w4000.jpg), printed *Modern Review*, October 1929, caption “Mr. Vishnu Deo,” author unknown. Commons records the India public-domain route [PD-India](https://commons.wikimedia.org/wiki/Template:PD-India); publication/author chain remains uncertain. | **1929**, safely before the 1936 baseline. Source is an anonymous halftone; the IA page scan improves resolution but does not change the original attribution uncertainty. | **Needs user review / blocked for the current FIJ role.** Date passes; Council-role fit does not. It can only be considered if the design deliberately changes the identity/role to a pre-1937 Indo-Fijian civic representative and the parent accepts the halftone/anonymous-source limitations. |

## Existing source and processing evidence

No new source image, repaint, DDS, GFX definition, or gameplay file was created in this research pass. Existing evidence remains in the source-clearance package:

- Source-clearance root: `docs/assets/006_independence_wave/fiji_source_clearance_2026_07_27/`.
- Sukuna source master: `ratu_sir_lala_sukuna_source.jpg` (2520x3128, SHA256 `8cf20454f59f8644b3c34dd9ea40a7e98cdf5b56113cd8bb918f893fc6cff5e5`). Existing exact crop, crop metadata, 156x210 preview, source manifest, contact sheet, and `gfx_handoff.md` are retained there.
- Sukuna exact crop: `ratu_sir_lala_sukuna_crop.png`, rectangle `(300,250)-(2220,2550)`, 1920x2300. Existing raw repaint and normalized candidate are provisional evidence only; they do not clear the circa-1940s date gate.
- Vishnu Deo Commons source: `vishnu_deo_fiji_source.jpg` (277x543, SHA256 `680ae01b3e87937335321369c197a2d63f56b469608e700781639e2d0f1b8719`), with the exact crop and metadata in the same root.
- Vishnu Deo period scan retained by the pre-1937 source handoff: `docs/assets/006_independence_wave/sources/fij_vishnu_deo_2026_08_01/n474_w4000.jpg` (4248x5866 RGB, SHA256 `9e94a391473850efbcec3f08c3ccbc08ba588e1a52af908fe08727cc2ae658c5`). Exact crop `vishnu_deo_modern_review_crop.png` uses `(2520,1060)-(3560,2520)`; the source handoff records the crop proof hash and provenance.
- The existing Sukuna DDS and sprite path are provisional runtime consumers only. This handoff does not admit or rewire them. Existing source manifests and visual-audit handoffs remain the authoritative processing record.

If a candidate is eventually admitted, the real-person pipeline still requires the attributed source, exact head/shoulders crop with equality metadata, source-locked identity-preserving repaint, deterministic 156x210 output, independent likeness/style/provenance audit, and only then the repository-standard DDS conversion. No generic or generated substitute is acceptable for a grounded Fiji identity.

## Historical flag and symbol provenance

The FIJ package currently reuses the installed vanilla FIJ flag triplets (`FIJ_democratic`, `FIJ_communism`, `FIJ_fascism`, and `FIJ_neutrality`, with their medium/small variants). No new flag asset is required for this admission review, and no flag file was edited.

The historically appropriate colonial design for a 1936 setting is the Fiji Blue Ensign used from 1924 to 1970: blue field, Union Jack canton, and the Fiji coat of arms toward the fly. Useful design references are [Commons File:Flag of Fiji (1924–1970).svg](https://commons.wikimedia.org/wiki/File:Flag_of_Fiji_(1924%E2%80%931970).svg) and its [direct SVG](https://upload.wikimedia.org/wikipedia/commons/8/85/Flag_of_Fiji_%281924%E2%80%931970%29.svg). The SVG records the 1000x500 geometry, blue field, Union Jack canton, and centered coat-of-arms motif, but it is a **modern reconstruction** credited to Simitukidia and Lokal Profil with a Commons CC BY-SA 3.0 declaration and contradictory category metadata (including CC-Zero). It is therefore a historical design reference, not a clean runtime-source clearance.

The Commons [File:Flag of Fiji (1924–1970).gif](https://commons.wikimedia.org/wiki/File:Flag_of_Fiji_(1924%E2%80%931970).gif) is tagged Public Domain / PD-Fiji, but its metadata credits a vector-images.com source and does not resolve the underlying reconstruction provenance. Treat it as reference-only unless rights are independently cleared. The related [File:Coat of arms of Fiji.svg](https://commons.wikimedia.org/wiki/File:Coat_of_arms_of_Fiji.svg) is a 2004 vector recreation by Simi Tukidia with CC BY-SA 3.0; [File:Arms of Fiji 2.png](https://commons.wikimedia.org/wiki/File:Arms_of_Fiji_2.png) carries a PD-Fiji claim but its first-publication chain was not independently verified in this pass. These references support the historical motif and geometry only; they do not justify copying a new flag into the package.

**Flag conclusion:** keep the existing vanilla FIJ triplets as the package source of truth. A separate new historical-symbol asset would require a fresh flat-asset source/rights workflow and should not be made to solve the unresolved portrait admission.

## Exact blockers and requested resolution

1. Sukuna is the correct role/community identity for the existing FIJ chair concept, but the retained National Archives of Fiji image is “circa 1940s,” not a documented 1936-or-earlier capture.
2. Vishnu Deo is the only currently retained pre-1936 image, but the 1929 halftone depicts a civic/communal leader who was not on the Council in 1936; his publication author and original rights chain are not fully identified.
3. Any grounded portrait must still pass the exact-crop, identity-preserving repaint, independent likeness/style/provenance audit, and DDS gates before runtime admission. Existing repaint evidence is not a waiver for the source/date or role gates.
4. FIJ remains outside the content attestation/readiness set (including the existing FORM-39 / Melanesian federation gate state). This research does not change those package decisions.
5. No advisor, operative, commander, or additional small portrait was requested or sourced. Do not invent or substitute one.
6. No new flag is required. If a new flag/symbol becomes a user requirement, the modern-reconstruction license ambiguity above must be resolved before any runtime copy is made.

## Recommendation to parent

Keep `FIJ`/IW-177 **closed and `needs_user_review`**. The best admission path is to obtain an attributed National Archives of Fiji, Fiji Museum, or iTaukei archival scan of Sukuna (or another role-equivalent male Fiji representative) dated no later than 1936 with reusable rights. If the parent explicitly accepts a circa-1940s Sukuna image for a 1936-centered presentation, record that as a deliberate era exception in the source manifest and retain the user-review status until the exception is approved. If the parent instead changes the role to a pre-1937 Indo-Fijian civic/community representative, Vishnu Deo is the period-valid review alternate, but the anonymous halftone and role change must be documented; it cannot be silently used for the current Council-chair localisation.

Canonical reference material consulted for the visual gate included `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/CATALOG.md`, the leader contact sheet at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/contact_sheet.png`, and the canonical leader portrait/flag ladders. These references were used only to confirm HOI4 sprite dimensions and visual fit; no canonical asset was copied or wired.

## Parent handoff summary

**Use:** this file plus the existing source-clearance, pre-1937 Vishnu Deo, Sukuna visual-audit, and FIJ country-package handoffs for the final Event 006 admission review.

**Do not do:** add a generic portrait, generate a real-person likeness without source lock, copy the modern reconstructed flag as a new runtime asset, or edit FIJ gameplay/readiness/localisation/GFX from this source-research result.
