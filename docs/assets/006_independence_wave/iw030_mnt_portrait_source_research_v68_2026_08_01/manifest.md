# IW-030 Montenegro sourced male portrait roster v68 (2026-08-01)

This is a bounded source-and-evidence package for the grounded vanilla `MNT` roster used by Event 006 IW-030.
It does not edit characters, history, events, `.gfx`, localisation, GUI, spreadsheets, or gameplay files.
It does not promote a DDS or create a runtime texture.
No advisor, high-command, dossier, small, operative, or female portrait asset is included.

## Source-mode and roster gate

Montenegro is a real historical polity, so the source mode is `grounded_source_only` and every one-person portrait must use an attributed archival photograph of the named man.
The vanilla roster has three male consumers in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/characters/MNT.txt`: `MNT_kristo_popovic`, `MNT_blazo_jovanovic`, and `MNT_blazo_dukanovic`.
The same file assigns each man both a country-leader and corps-commander role; no `female = yes` metadata is present.
Vanilla history recruits all three ids and the Event 006 roster handoff remains parent-owned.
The subject-ownership search found no cross-country character, commander, operative, or officeholder consumer for these identities.

| Consumer | Named subject and role fit | Source status | Portrait gate status | Runtime disposition |
| --- | --- | --- | --- | --- |
| `MNT_blazo_jovanovic` / `GFX_portrait_Blazo_Jovanovic` | Blažo Jovanović (1907–1976), Montenegrin partisan leader and corps commander; the selected 1942 image shows him at age 35 in wartime active life. | Commons identifies the central man in a three-person Livno group and dates the photograph to 1942; source credit is znaci.net and the photographer is unknown. | Exact crop `PASS`; source/crop linkage `PASS`; likeness `PASS`; male/framing/artifacts `PASS`; HOI4 leader style `PASS`; rights/provenance `NEEDS_USER_REVIEW` because the public-domain rationale does not identify the photographer. | Evidence-only 156x210 candidate; no DDS or runtime wiring. |
| `MNT_blazo_dukanovic` / `GFX_portrait_MNT_blazo_dukanovic` | Blažo Đukanović (1883–1943), Yugoslav military officer, fascist-route country leader, and corps commander; the selected portrait is estimated 1938–1940 and is close to the 1936 scenario start. | Commons explicitly identifies the subject and credits *Generali i admirali Kraljevine Jugoslavije: 1918–1941* (Mile S. Bjelajac, 2004); the photographer is unknown. | Exact crop `PASS`; source/crop linkage `PASS`; likeness `PASS`; male/framing/artifacts `PASS`; HOI4 leader style `PASS`; rights/provenance `NEEDS_USER_REVIEW` because the Commons `PD-old` assertion and book-reproduction chain need independent legal review. | Evidence-only 156x210 candidate; no DDS or runtime wiring. |
| `MNT_kristo_popovic` / `GFX_portrait_europe_generic_land_19` | Krsto Zrnov Popović (1881–1947), Montenegrin Army general, oligarch-route country leader, and corps commander; alive in 1936. | The Commons portrait is male and visually plausible but has no machine-readable author, source, or date; the Montenegrina scan has an article attribution but no image credit/date and the site expressly prohibits further distribution or unauthorized exploitation. | No accepted archival source, crop, or repaint; provenance/rights/date gate `BLOCKED`. | Keep the generic consumer blocked; do not relabel a Jovanović or Đukanović face as Popović. |

## Selected source A: Blažo Jovanović, Livno 1942

- Commons record: <https://commons.wikimedia.org/wiki/File:Grupa_vojnih_rukovodilaca_u_oslobo%C4%91enom_Livnu.jpg>.
- Original image URL: <https://upload.wikimedia.org/wikipedia/commons/a/ab/Grupa_vojnih_rukovodilaca_u_oslobo%C4%91enom_Livnu.jpg>.
- Download fallback used because Wikimedia upload throttled direct retrieval: <https://i0.wp.com/upload.wikimedia.org/wikipedia/commons/a/ab/Grupa_vojnih_rukovodilaca_u_oslobo%C4%91enom_Livnu.jpg>.
- Archive/source credit: <http://www.znaci.net/fotogalerija/fotogalerija06.html>.
- Commons caption identifies the ordering as “from right: Milinko Đurović, Blažo Jovanović, Čedo Kapor,” making Jovanović the central standing man.
- Source date: 1942, contemporary wartime image; this is later than the 1936 start but is a period-authentic active-life portrait of a named MNT leader.
- Author: unknown.
- Rights note: Commons presents the file as public domain under a `PD-because` rationale; the photographer remains unidentified, so this package records rights as review-pending rather than approved.
- Immutable source master: `source_masters/mnt_blazo_jovanovic_livno_1942.jpg`, 1121x1509 RGB, SHA-256 `a66cf887c8b28f86c92dedd763b3cb6bd046c01f6dff0f63825c07f30c64c120`.
- Exact head-and-shoulders crop: `source_crops/mnt_blazo_jovanovic_livno_1942_head_shoulders.png`, rectangle `[300,80,720,850]`, 420x770 RGB, SHA-256 `fd5834027ece9dce94c7dd0f5a7f9b0b74559a85c2653619bc890b3fe117b880`.
- Crop proof: `crop_metadata/mnt_blazo_jovanovic_livno_1942_crop.json`, Pillow utility v1.0, `status=exact_source_crop_verified`, `decoded_pixels_equal=true`, matching RGBA equality hash `1276f4d33fcf19a16e07ca9e733240ed5da4fc8a3d8f0ff016d826586617e855`.
- Corroborating identity image: `source_masters/mnt_blazo_jovanovic_portrait_1942_corroboration.jpg`, 235x358 RGB, SHA-256 `a6867d4c7fbf9cab555953cfc58c85840e0c7420c329fb2addba9c90e353a692`; this is evidence only and is too small to anchor the runtime pipeline.

## Selected source B: Blažo Đukanović, 1938–1940

- Commons record: <https://commons.wikimedia.org/wiki/File:Bla%C5%BEo_%C4%90ukanovi%C4%87.jpg>.
- Original image URL: <https://upload.wikimedia.org/wikipedia/commons/7/77/Bla%C5%BEo_%C4%90ukanovi%C4%87.jpg>.
- Download fallback used because Wikimedia upload throttled direct retrieval: <https://i0.wp.com/upload.wikimedia.org/wikipedia/commons/7/77/Bla%C5%BEo_%C4%90ukanovi%C4%87.jpg>.
- Source credit: Mile S. Bjelajac, *Generali i admirali Kraljevine Jugoslavije: 1918–1941: studija vojne elite i biografski leksikon*, Institut za savremenu istoriju Srbije, Dobro, Beograd, 2004.
- Source date: estimated 1938–1940 on Commons, near the 1936 scenario and within the subject’s active military life.
- Author: unknown.
- Rights note: Commons applies `PD-old` and Public Domain Mark language, but the unknown-photographer book-reproduction chain requires independent legal review before promotion.
- Immutable source master: `source_masters/mnt_blazo_dukanovic_1938_1940.jpg`, 443x599 RGB, SHA-256 `b099dff0ad5b45d8dd33a10c9a0ccc113d4e08afa8ca1fa7c2d5fe68b76a8be8`.
- Exact head-and-shoulders crop: `source_crops/mnt_blazo_dukanovic_1938_1940_head_shoulders.png`, rectangle `[30,20,420,475]`, 390x455 RGB, SHA-256 `b626fe6089e3483f89a7fc0d553b69b16fa52ce8116b696d2f6e3362ec318cd9`.
- Crop proof: `crop_metadata/mnt_blazo_dukanovic_1938_1940_crop.json`, Pillow utility v1.0, `status=exact_source_crop_verified`, `decoded_pixels_equal=true`, matching RGBA equality hash `34f6357c79cf89a7b2eb1705da16474c81e2273a7bbed8e0e44ff14d5d47ded7`.

## Popović replacement research and blocker

- Commons candidate: <https://commons.wikimedia.org/wiki/File:Krsto_Zrnov_Popovic.jpg> with original <https://upload.wikimedia.org/wikipedia/commons/2/25/Krsto_Zrnov_Popovic.jpg>.
- Retained rejected source: `rejected_candidates/mnt_krsto_popovic_commons_undated.jpg`, 791x1182 RGB, SHA-256 `4b4a74e01d285dd22b90a21bf0f5a7f58d4c65372fa702501c42c6b6551b23fa`.
- Commons license is CC BY-SA 3.0 with VRTS permission confirmed, but the record is categorized as having no machine-readable author and no machine-readable source and supplies no capture date or era evidence.
- Montenegrina article candidate: <https://montenegrina.net/pages/pages1/istorija/cg_izmedju_1_i_2_svj_rata/general_krsto_zrnov_popovic.htm> with image URL <https://montenegrina.net/images/istorija/krsto_zrnov_popovic.jpg>.
- Retained rejected source: `rejected_candidates/mnt_krsto_popovic_montenegrina_undated.jpg`, 380x481 RGB, SHA-256 `e8e40eb143ae5e9a18ea4885149cdbc0b976e52fc95586ff5d88cc8a7fe30ee7`.
- The article is credited to Novak Adžić and establishes Popović’s historical identity and life dates, but it gives no image author, capture date, or reuse license.
- The Montenegrina project page states that material is for education and must not be used for further distribution, sale, public performance, or unauthorized exploitation, so this image cannot be treated as a runtime source without written permission.
- Both candidates are retained as research evidence only; no crop or ImageGen repaint was made for Popović, and no generated substitute is permitted.

## ImageGen, processing, and audit evidence

- Raw source-locked HOI4 repaints are retained under `raw_imagegen/` with SHA-256 `4022dee805b4be1364d51f7fa481b66e706e93b7a1239c39931ca697e358e989` (Jovanović, 926x1698 RGB) and `af610f67ae7001d1348b6fda966f2c9e2e570dd670c25a992d0df3dfcf271874` (Đukanović, 1162x1354 RGB).
- `raw_imagegen/portrait_MNT_blazo_jovanovic.txt` and `raw_imagegen/portrait_MNT_blazo_dukanovic.txt` are name-free `hoi4_portrait` prompts for the durable ComfyUI pair; matching durable files are under `docs/assets/portraits/006_independence_wave/`.
- Deterministic candidates use RGB cover crops and Pillow `Image.Resampling.LANCZOS` to 156x210; Jovanović output SHA-256 `769ae8ccd0fc3bd4ddd2ced1918b21ae37c1c281bd644c8c6df231d20c684b72`; Đukanović output SHA-256 `b5535b51c6cca13ad5dba381ad032e690c1ae3100a360e5b0c6fad646f3d73ae`.
- Candidate processing records are `processed_candidates/portrait_MNT_blazo_jovanovic_156x210_candidate.json` and `processed_candidates/portrait_MNT_blazo_dukanovic_156x210_candidate.json`.
- Role references are the canonical leader family under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/`; package copies are `references/vanilla_leaders_contact_sheet.png` and `references/curated_leaders_contact_sheet.png`.
- Independent review evidence is `review/mnt_v68_audit_native.png` and `review/mnt_v68_audit_4x.png`; the broader comparison sheet is `review/mnt_v68_roster_contact_sheet.png`.
- The reviewer is `/root/event6_mnt_portraits_research_v68`, distinct from the prior v53 producer; review date is 2026-08-01.
- Separate verdicts are recorded in `audit_v68.md`; identity/style gates pass for Jovanović and Đukanović, while rights/provenance remain review-pending and therefore block DDS/runtime promotion.

## Status and forbidden actions

Jovanović and Đukanović are `needs_user_review` evidence candidates with source/crop linkage and visual gates passed.
Popović is `blocked_provenance` and must not be replaced with a relabelled face or generated portrait.
No DDS was converted, no `.gfx` file was edited, and no runtime path points into this package.
The parent may promote only after separate rights review, full-roster admission, and the normal parent-owned runtime wiring gates.
