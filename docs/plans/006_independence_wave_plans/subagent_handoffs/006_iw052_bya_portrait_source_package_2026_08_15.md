# IW-052 BYA portrait source package handoff

Date: 2026-08-15.

Status: HOLD / Erbanov needs independent framing and rights review; the solo Markizov alternative needs parent identity selection and independent rights review.

This bounded task archived and reviewed a conditional exact-date grounded source for IW-052 Buryatia. It did not create a DDS, GFX entry, character file, character reference, parent-owned identity flag, gameplay change, localisation change, or central-admission change. RunPod was never opened or operated.

## Candidate and source

The candidate is Mikhei (Michei) Nikolayevich Erbanov, a Buryat-born Soviet party and state official documented as first secretary of the Buryat-Mongol regional committee from December 1929 through October 1937. The Russian Wikipedia API capture also records that he led the Buryat-Mongol delegation at the 27 January 1936 Kremlin reception, matching the Event 006 opening date.

The source is Wikimedia Commons File:Erbanov Markizova.JPG:

- Commons page: https://commons.wikimedia.org/wiki/File:Erbanov_Markizova.JPG
- Original URL: https://upload.wikimedia.org/wikipedia/commons/1/1c/Erbanov_Markizova.JPG
- Description: I. Stalin, M. Erbanov and E. Markizova.
- Depiction date: 1936-01-27.
- Publication credit: Газета “Цемент” №1 от 1 января 1938 года.
- Photographer: Mikhail Mikhailovich Kalashnikov.
- Original dimensions: 473x640.
- Original bytes: 41,073.
- Original SHA-256: 0af52ae1f993dcd60324202996eea3f29336f326f7207a7d77c6ac16600585e6.
- Commons SHA-1: d4e21d7cc343f53bfda47ced02ba64d5d1db23e9.

Commons records Public domain / PD-Russia metadata, UsageTerms Public domain, License pd, Copyrighted False, and AttributionRequired false. The same Commons record categorizes the image as Works copyrighted in the U.S.; the package therefore preserves a conditional rights status and requires independent jurisdiction-specific review before runtime use.

Source evidence captures:

- docs/assets/portraits/006_independence_wave/processed/iw052_bya_mikhei_erbanov_source_commons_api_2026_08_15.json, SHA-256 096aa9f183a4b26e9ce13a8e2c48bb12b9507f19f92866d0652cbaaf80d3c455.
- docs/assets/portraits/006_independence_wave/processed/iw052_bya_mikhei_erbanov_source_identity_russian_wikipedia_api_2026_08_15.json, SHA-256 61a6eada8c435fade5f6d2e8b75b4ce7bae0d7547d1b8896a2d9a35fc998ff81.

## Crop and framing evidence

YuNet found three faces and the automatic extractor failed closed rather than guessing: [225,58,78,102], [119,87,92,126], and [403,131,70,107]. Manual crop override [340,90,473,269] selects the right-hand adult described as M. Erbanov by the Commons caption.

The lossless crop is:

- docs/assets/portraits/006_independence_wave/processed/iw052_bya_mikhei_erbanov_source_research_2026_08_15__portrait_BYA_mikhei_erbanov_source_crop.png.
- Dimensions: 133x179.
- SHA-256: 94eacbe3563c8c75817d4d4b03f774c1b7251d0868ea6ff8aab0de05d261b1cf.
- Decoded RGBA equality hash: de88c949e025dc5d5d2cfe8aa009b7e2f70f666a245d6a4b36dbbc38e0937234.
- Crop JSON: docs/assets/portraits/006_independence_wave/processed/iw052_bya_mikhei_erbanov_source_research_2026_08_15__portrait_BYA_mikhei_erbanov_source_crop.json.

The crop retains the right-hand adult’s face, mustache, bald crown, tie, and shoulders. The source is still a group photograph, the original right edge is the crop’s right edge, and a narrow dark neighboring-subject sliver remains at the crop’s left edge. The candidate is defensibly attributable for source review, but framing remains HOLD until an independent reviewer accepts or rejects that composition.

The 4x nearest review preview is docs/assets/portraits/006_independence_wave/processed/iw052_bya_mikhei_erbanov_source_research_2026_08_15__portrait_BYA_mikhei_erbanov_source_review_4x_nearest.png, 532x716, SHA-256 8d5d35495c4907b09ac425ba67ad9858502d8e82fe96f81e37a82bfadbe6d845.

## Archive and ownership boundary

The untouched original is directly under docs/assets/portraits/006_independence_wave/:

docs/assets/portraits/006_independence_wave/iw052_bya_mikhei_erbanov_source_research_2026_08_15__portrait_BYA_mikhei_erbanov_original.jpg

All crop, provenance, review, manifest, and JSON evidence is flat under the existing processed directory. No subfolder was created. No 156x210 PNG is retained anywhere in the durable archive.

The durable provenance contract is docs/assets/portraits/006_independence_wave/processed/metadata__iw052_bya_mikhei_erbanov_source_research_2026_08_15__portrait_BYA_mikhei_erbanov.txt. The package manifest is docs/assets/portraits/006_independence_wave/processed/metadata__iw052_bya_mikhei_erbanov_source_research_2026_08_15__manifest.json. The review record is docs/assets/portraits/006_independence_wave/processed/metadata__iw052_bya_mikhei_erbanov_source_research_2026_08_15__review.md.

No DDS or portrait-specific GFX entry was created. No existing character portrait reference was changed. The parent-owned identity flag remains unset, and the installed vanilla BYA generic portraits remain untouched.

## Review disposition and parent action

| Gate | Result |
| --- | --- |
| Exact-date Buryat-Mongol officeholder | CONDITIONAL PASS |
| Attributed source and source bytes | PASS |
| Rights | CONDITIONAL / jurisdiction caveat |
| Exact crop/equality | PASS |
| Identity framing | HOLD pending independent review |
| Source-placeholder candidate | HOLD / needs_user_review |
| Runtime replacement | Not created |

The parent must independently review the 4x crop against the untouched original and review the Commons rights caveat. If the group composition or edge crop cannot defensibly identify Erbanov, mark the candidate blocked and research another source. Do not invent, repaint, genericize, or substitute a real person.

## Skipped checks and blockers

- DDS conversion skipped because parent scope explicitly forbids DDS/runtime wiring in this source package and the candidate is not independently approved.
- GFX and character wiring skipped by scope; no exact Event 006 consumer or parent identity assignment is admitted.
- RunPod skipped and never operated.
- In-game/MCP validation skipped because this is source evidence only and no runtime surface was changed.
- Independent framing reviewer and rights reviewer are pending.
- If independent review rejects the crop, the candidate is blocked; no fallback portrait was used.

## Source-only continuation: solo period-fit alternative

On 2026-08-15 a bounded follow-up search found a stronger non-group source candidate: Ardan (Ardan Angadakovich) Markizov, a Buryat-Mongol party and state official. The Russian Wikipedia API capture records him as agriculture commissar of the Buryat-Mongol ASSR and second secretary of the Buryat-Mongol regional committee in 1936-1937, and records his presence in the official Buryat-Mongol delegation at the Kremlin reception on 1936-01-27 led by Mikhei Erbanov. He is therefore valid for the requested opening date as a period-fit regional officeholder and delegation member, but he is not the top regional leader.

The source is Wikimedia Commons File:Ardan Markizov.jpg: https://commons.wikimedia.org/wiki/File:Ardan_Markizov.jpg. Commons records a solo 278x385 portrait, image date `1930s`, credit `БНЦ СО РАН`, unknown author, Public domain / PD-Russia-1996 metadata, license `pd`, `Copyrighted=False`, and `AttributionRequired=False`. The untouched original is archived directly at `docs/assets/portraits/006_independence_wave/iw052_bya_ardan_markizov_source_research_2026_08_15__portrait_BYA_ardan_markizov_original.jpg` with SHA-256 `06e8c6cc3c5749ee6f637432fd52b5810b4563a82866f84f705938a122b9a136`.

All alternative-source evidence is flat under the existing `docs/assets/portraits/006_independence_wave/processed/` directory. The lossless automatic YuNet crop detects one face `[69,79,169,211]`, retains `[0,0,278,374]`, and is archived as `iw052_bya_ardan_markizov_source_research_2026_08_15__portrait_BYA_ardan_markizov_source_crop.png` with SHA-256 `83470a476d3db91382d5a064decf7cf4fe1b53f84db3bb36af15dd7366327155`; the decoded RGBA equality hash is `c4558eb30d0c03bf3ccc1a569aaebf67078960d380b7d6360180d89ed2849726`. The 4x nearest review preview is 1112x1496 with SHA-256 `828ac53532b99eeae101298152c6388ded05f11bf1f5caf08ab2044fe168648a`. No 156x210 derivative was retained.

The alternative evidence files are `iw052_bya_ardan_markizov_source_commons_api_2026_08_15.json`, `iw052_bya_ardan_markizov_source_commons_page_2026_08_15.html`, `iw052_bya_ardan_markizov_source_identity_russian_wikipedia_api_2026_08_15.json`, the crop JSON, `metadata__iw052_bya_ardan_markizov_source_research_2026_08_15__portrait_BYA_ardan_markizov.txt`, `metadata__iw052_bya_ardan_markizov_source_research_2026_08_15__review.md`, `metadata__iw052_bya_ardan_markizov_source_research_2026_08_15__manifest.json`, and `iw052_bya_portrait_followup_search_2026_08_15.json`. The manifest remains `source_placeholder_candidate_hold` with runtime paths null and `parent_identity_flag` null.

This solo source clears the current Erbanov group-framing problem for source review, but it does not silently replace the parent-owned identity decision. The parent must explicitly choose whether the BYA opening provisional institution may use a 1936-valid second secretary/agriculture commissar and official delegation member, or whether the exact top regional leader is mandatory and Erbanov must remain the only conditional candidate. If Markizov is not accepted as the consumer, keep both source candidates fail-closed and document the required identity decision; do not relabel Markizov or a vanilla generic portrait as Erbanov. Independent rights review remains required before any runtime promotion.

The bounded negative search is recorded in `docs/assets/portraits/006_independence_wave/processed/iw052_bya_portrait_followup_search_2026_08_15.json` (SHA-256 `7105494975ad451fb12250347e876fec9fd1cf4cd4892d6db7730f2575cefbd4`). Exact-name and prefix Commons searches found no solo Erbanov source beyond the known three-person photograph; the Dampilov solo candidate did not clear its conflicting rights metadata. If the parent requires the actual top regional leader rather than a 1936-valid regional officeholder and delegation member, the package remains fail-closed pending a new solo Erbanov or authentic institutional source.

## Archive count receipt

At completion of this source-only tranche on 2026-08-15, `docs/assets/portraits/006_independence_wave/` contained 53 direct regular files and its only child directory was `processed/`; `processed/` contained 169 direct regular files and the archive contained 222 regular files recursively. The IW-052 subset was 2 direct parent originals and 18 flat processed evidence files matching `*iw052_bya*`. The archive had zero nested directories beyond `processed/`, zero `156x210` filename matches, zero DDS files, and zero GFX files.
