# IW-177 Fiji/FIJ sourced visual clearance

## Scope

This handoff covers source research for the requested IW-177 Fiji country-leader or provisional-institution visual. It does not edit GFX, gameplay, country history, localisation, or event files, and it intentionally does not create ImageGen output or DDS because the parent prompt forbids those steps in this clearance pass.

## Outcome

The source gate is `needs_user_review`, not a runtime-ready pass. No exact 1936 Fiji Legislative Council or founding-congress image with defensible provenance was found in the searched source set, so this handoff preserves two attributable male candidates and records their different uncertainties rather than inventing a substitute.

The recommended source master is Ratu Sir Lala Sukuna. His identity, chiefly/constitutional role, archive provenance, and resolution are strong, but the National Archives of Fiji dates the photograph only to circa 1940s, later than the event's 1936-centered baseline. Parent approval is required before any source-locked repaint.

The period-valid alternate is Pt. Vishnu Deo. His 1929 publication portrait fits the Indo-Fijian communal/labor/constitutional lane, but the anonymous halftone is only 277x543 and he was not in Legislative Council office during the 1936 baseline. It is therefore a review alternate, not a production-safe full-size master.

## Candidate A: Ratu Sir Lala Sukuna

Ratu Sir Josefa Lalabalavu Vanayaliyali Sukuna (1888-1958) was a Fijian chief from Bauan chiefly lineage and served on the Legislative Council as representative for the Fijian people from 1932. He was active in chiefly, land, constitutional, and defense-relevant public life around 1936, making him a defensible bridge for an IW-177 institution that turns named communities into representation, veto, autonomy, revenue, and defense clauses. This is a real identity and role fit, not a generic "Fiji leader" placeholder.

The historical context references used for this role check are [Lala Sukuna](https://en.wikipedia.org/wiki/Lala_Sukuna) and the [iTaukei Land Trust Board history](https://tltb.com.fj/our-history/). They are context references only; the selected image provenance remains the National Archives of Fiji source recorded below.

The preserved original is `docs/assets/006_independence_wave/fiji_source_clearance_2026_07_27/ratu_sir_lala_sukuna_source.jpg` (2520x3128, SHA-256 `8cf20454f59f8644b3c34dd9ea40a7e98cdf5b56113cd8bb918f893fc6cff5e5`). The Commons source page is [File:Ratu Sir Lala Sukuna.jpg](https://commons.wikimedia.org/wiki/File:Ratu_Sir_Lala_Sukuna.jpg), and the direct original is [upload.wikimedia.org/.../Ratu_Sir_Lala_Sukuna.jpg](https://upload.wikimedia.org/wikipedia/commons/7/73/Ratu_Sir_Lala_Sukuna.jpg). Commons credits the National Archives of Fiji and links its archive post at [National Archives of Fiji](https://www.facebook.com/NationalArchivesOfFiji/photos/a.124204611046400/124206027712925/).

Commons labels the image Public domain under `PD-Fiji`. The [PD-Fiji template](https://commons.wikimedia.org/wiki/Template:PD-Fiji) records the Fiji copyright basis and the photograph term, but the archive metadata does not identify a more precise capture date or photographer. Keep the "circa 1940s" qualifier in every downstream manifest and do not describe it as a 1936 photograph.

The exact head-and-shoulders source crop is `docs/assets/006_independence_wave/fiji_source_clearance_2026_07_27/ratu_sir_lala_sukuna_crop.png`, coordinates `(300,250)-(2220,2550)`, 1920x2300. `ratu_sir_lala_sukuna_crop.json` records `status: exact_source_crop_verified`, decoded pixel equality, source hash, crop hash, and the normalized invocation of `.agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py`.

## Candidate B: Pt. Vishnu Deo

Pt. Vishnu Deo (1900-1968) was a Fiji-born Indo-Fijian political and communal leader, Arya Samaj leader, Fiji Samachar editor, and associate of the Fiji Indian National Congress founded at Lautoka in 1929. He served on the Legislative Council in 1929 and again from 1937. His community and constitutional role is useful for a Fiji bridge that must not collapse all representation into chiefly institutions, but the 1936 in-office Council fit is not exact.

The historical context reference used for this role check is [Vishnu Deo](https://en.wikipedia.org/wiki/Vishnu_Deo). It is a context reference only; the selected image provenance remains the anonymous *The Modern Review* publication recorded below.

The preserved original is `docs/assets/006_independence_wave/fiji_source_clearance_2026_07_27/vishnu_deo_fiji_source.jpg` (277x543, SHA-256 `680ae01b3e87937335321369c197a2d63f56b469608e700781639e2d0f1b8719`). The Commons source page is [File:Vishnu Deo Fiji.jpg](https://commons.wikimedia.org/wiki/File:Vishnu_Deo_Fiji.jpg), and the direct original is [upload.wikimedia.org/.../Vishnu_Deo_Fiji.jpg](https://upload.wikimedia.org/wikipedia/commons/7/7a/Vishnu_Deo_Fiji.jpg). Commons credits *The Modern Review*, October 1929, with an unknown author.

Commons labels the image Public domain under `PD-India`. The [PD-India template](https://commons.wikimedia.org/wiki/Template:PD-India) supplies the pre-1958 photograph term used for the anonymous 1929 publication. Because the source is a small halftone and the photographer is unknown, retain both limitations and do not imply a higher-resolution original.

The exact source crop is `docs/assets/006_independence_wave/fiji_source_clearance_2026_07_27/vishnu_deo_fiji_crop.png`, coordinates `(25,35)-(252,330)`, 227x295. `vishnu_deo_fiji_crop.json` records `status: exact_source_crop_verified`, decoded pixel equality, source hash, crop hash, and the same normalized crop utility provenance.

## Evidence package

- `docs/assets/006_independence_wave/fiji_source_clearance_2026_07_27/source_manifest.json` records source URLs, archive/publication credit, rights basis, date, role/community fit, hashes, crop metadata, uncertainty, and ownership search results.
- `docs/assets/006_independence_wave/fiji_source_clearance_2026_07_27/fiji_portrait_source_contact_sheet.png` compares both originals, exact crops, and deterministic 156x210 review previews.
- `docs/assets/006_independence_wave/fiji_source_clearance_2026_07_27/gfx_handoff.md` records suggested future sprite naming and the intentionally absent DDS path.
- The 156x210 preview PNGs are evidence-only review thumbnails, not runtime assets.

## Ownership and collision check

The terms `Sukuna`, `Lala Sukuna`, `Josefa Lalabalavu`, `Vishnu Deo`, and `Vishnu_Deo` were searched under the Chaos Redux `common`, `history`, `gfx`, and `interface` roots and the same targeted vanilla roots under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`. No existing character, leader, or portrait ownership match was returned on 2026-07-27.

## Parent decision and next gate

Choose whether the circa-1940s Sukuna image is acceptable for an around-1936 visual consumer. If yes, use the preserved source crop as the only identity reference for a later source-locked repaint, then require an independent likeness/style/provenance audit before DDS and runtime wiring. If strict contemporaneous 1936 imagery is required, keep the asset blocked and continue archive research. Do not use Deo as a final full-size portrait without explicit approval of the low-resolution halftone limitation.

## Explicit simplifications and blockers

- No final DDS was produced because the parent prompt explicitly forbids DDS conversion in this source-clearance pass.
- No ImageGen repaint was produced because this subtask owns sourced visual evidence only and the parent prompt explicitly forbids generation here.
- No exact 1936 institutional congress photograph was found in the bounded search, so no institutional substitute is claimed.
- Overall source clearance remains `needs_user_review`; the circa-1940s date uncertainty and Deo's resolution/role limitations are the remaining blockers.
