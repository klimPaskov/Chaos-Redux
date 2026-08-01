# IW-030 Montenegro portrait source research handoff v53

Date: 2026-08-01

## Scope

This bounded source-research tranche covers the grounded male Montenegro roster for IW-030: `MNT_kristo_popovic`, `MNT_blazo_jovanovic`, and `MNT_blazo_dukanovic`. It does not edit gameplay, characters, history, `.gfx`, localisation, or spreadsheet files.

The grounded source-mode gate applies because MNT is a real historical polity and all three named consumers are real men. The current `MNT_kristo_popovic` texture is the generic `GFX_portrait_europe_generic_land_19`, which remains a hard visual blocker.

## Research result

| Consumer | Candidate | Status | Why |
| --- | --- | --- | --- |
| `MNT_blazo_jovanovic` | Blažo Jovanović, 1942 Livno group photograph | `visual_pass_linkage_pass_needs_rights_review` | High-resolution 1121x1509 Commons source; caption explicitly identifies him as the central subject in the three-person group, and the face matches the separately catalogued 1942 individual record. The raw HOI4 repaint and deterministic 156x210 candidate pass visual/style and source/crop linkage review; the unknown photographer keeps rights review open. |
| `MNT_blazo_dukanovic` | Blažo Đukanović, estimated 1938–1940 military portrait | `visual_pass_linkage_pass_needs_rights_review` | Single 443x599 male military portrait with explicit subject caption, period fit near the 1936 start, book/source credit, and Commons `PD-old`/Public Domain Mark. The raw HOI4 repaint and deterministic 156x210 candidate pass visual/style and source/crop linkage review; the unknown photographer/book reproduction keeps rights review open. |
| `MNT_kristo_popovic` | Krsto Zrnov Popović Commons portrait | `blocked_provenance` | Male uniform portrait is CC BY-SA 3.0 with VRTS permission confirmed, but author, source, and date are absent from the Commons record. It is not a defensible replacement until an archive/source/date record is found. |

## Exact source evidence

### Jovanović

- Commons file: <https://commons.wikimedia.org/wiki/File:Grupa_vojnih_rukovodilaca_u_oslobo%C4%91enom_Livnu.jpg>.
- Canonical original: <https://upload.wikimedia.org/wikipedia/commons/a/ab/Grupa_vojnih_rukovodilaca_u_oslobo%C4%91enom_Livnu.jpg>.
- Source credit: znaci.net wartime photo collection; unknown photographer.
- Commons source date: 1942.
- Commons rights statement: `PD-because`, linked to the znaci.net public-domain rationale; unknown photographer is retained as uncertainty.
- Identity caption: “S desna na levo: Milinko Đurović, Blažo Jovanović, Čedo Kapor.” Jovanović is the central standing subject.
- Master: `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v53_2026_08_01/source_masters/mnt_blazo_jovanovic_livno_1942.jpg` (1121x1509 RGB, SHA-256 `a66cf887c8b28f86c92dedd763b3cb6bd046c01f6dff0f63825c07f30c64c120`).
- Exact crop: `source_crops/mnt_blazo_jovanovic_livno_1942_head_shoulders.png` (420x770 RGB, crop `[300,80,720,850]`, SHA-256 `fd5834027ece9dce94c7dd0f5a7f9b0b74559a85c2653619bc890b3fe117b880`).
- Crop proof: `crop_metadata/mnt_blazo_jovanovic_livno_1942_crop.json`; Pillow utility v1.0 reports `exact_source_crop_verified`, `decoded_pixels_equal=true`, and matching RGBA hash `1276f4d33fcf19a16e07ca9e733240ed5da4fc8a3d8f0ff016d826586617e855`.
- Auxiliary identity evidence: `source_masters/mnt_blazo_jovanovic_portrait_1942.jpg` (235x358 RGB, SHA-256 `a6867d4c7fbf9cab555953cfc58c85840e0c7420c329fb2addba9c90e353a692`) from <https://commons.wikimedia.org/wiki/File:Bla%C5%BEo_Jovanovi%C4%87.jpg>; this is corroboration only and is too small to be the final runtime source.

### Đukanović

- Commons file: <https://commons.wikimedia.org/wiki/File:Bla%C5%BEo_%C4%90ukanovi%C4%87.jpg>.
- Canonical original: <https://upload.wikimedia.org/wikipedia/commons/7/77/Bla%C5%BEo_%C4%90ukanovi%C4%87.jpg>.
- Source credit: Mile S. Bjelajac, *Generali i admirali Kraljevine Jugoslavije: 1918–1941: studija vojne elite i biografski leksikon*, Institut za savremenu istoriju Srbije, Dobro, Beograd, 2004.
- Commons source date: between 1938 and 1940.
- Commons rights statement: `PD-old` / CC-PD-Mark with an unknown photographer and a note that the author is dead more than 70 years; this assertion needs independent review because the photographer is not identified.
- Identity caption: “Photo of Blažo Đukanović.” The image is a clear adult male military portrait with uniform and medals.
- Master: `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v53_2026_08_01/source_masters/mnt_blazo_dukanovic_1938_1940.jpg` (443x599 RGB, SHA-256 `b099dff0ad5b45d8dd33a10c9a0ccc113d4e08afa8ca1fa7c2d5fe68b76a8be8`).
- Exact crop: `source_crops/mnt_blazo_dukanovic_1938_1940_head_shoulders.png` (390x455 RGB, crop `[30,20,420,475]`, SHA-256 `b626fe6089e3483f89a7fc0d553b69b16fa52ce8116b696d2f6e3362ec318cd9`).
- Crop proof: `crop_metadata/mnt_blazo_dukanovic_1938_1940_crop.json`; Pillow utility v1.0 reports `exact_source_crop_verified`, `decoded_pixels_equal=true`, and matching RGBA hash `34f6357c79cf89a7b2eb1705da16474c81e2273a7bbed8e0e44ff14d5d47ded7`.

### Popović replacement lead and blocker

- Commons file: <https://commons.wikimedia.org/wiki/File:Krsto_Zrnov_Popovic.jpg>.
- Commons metadata: 791x1182 male uniform portrait, CC BY-SA 3.0, VRTS permission confirmed.
- Blocker: the page is marked “files with no machine-readable author” and “files with no machine-readable source,” and no date is supplied. Do not use it as a final source without archive provenance, date/era fit, and attribution/ShareAlike review.

## Ownership search

Exact and variant identity searches covered the current Chaos Redux tree and installed vanilla `common/characters/`, `history/countries/`, `gfx/leaders/`, `interface/`, and `localisation/` roots for all three names and ids. Only the intended vanilla MNT character definitions and the Event 006 MNT recruitment/route consumers were found; no cross-country character, commander, operative, or officeholder owner was found. The singular owner remains the vanilla MNT roster, so no transfer guard is needed for same-owner source replacement.

## Files created

- `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v53_2026_08_01/manifest.md` records source links, provenance, license/date/era notes, hashes, crop evidence, ownership audit, and blocker status.
- `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v53_2026_08_01/gfx_handoff.md` records stable existing sprite names, proposed source candidates, and the no-wire boundary.
- `source_masters/` retains the two selected masters plus auxiliary Commons candidates for review.
- `source_crops/` and `crop_metadata/` retain the exact Pillow crops and decoded-pixel equality JSON proofs.
- `review/mnt_portrait_source_contact_sheet.png` is a contact sheet for the selected crops and comparison candidates; it is review-only.
- `repaint_source_lock_2026_08_01.md` links exact crop/master hashes to the two raw ImageGen outputs, prompt-pair hashes, and evidence candidates.
- `processed_candidates/` contains deterministic 156x210 PNGs plus JSON metadata; these are evidence-only and are not in the flat source shelf.

## Completion boundary and blockers

At the source-research boundary no ImageGen repaint, deterministic 156x210 candidate, audit, DDS, durable ComfyUI pair, or `.gfx` edit had been produced because the parent requested source research only. The parent subsequently copied the two raw HOI4-style repaint masters into `docs/assets/006_independence_wave/portraits_generated_png/`, recorded the source-lock record, and produced deterministic 156x210 evidence candidates; the independent visual audit and source/crop linkage PASS are recorded below. No DDS, durable ComfyUI pair, or `.gfx` edit exists. The two selected sources are not runtime-ready because rights/provenance and complete-roster admission remain open.

`MNT_kristo_popovic` remains blocked on missing archive source/date evidence; do not fabricate or silently relabel a Jovanović or Đukanović face to satisfy that consumer. Parent may either source a separate Krsto Popović archival image or narrow/reassign the route semantics after an explicit design decision.

## Independent raw-repaint visual/provenance audit (2026-08-01)

The two raw HOI4-style repaint masters were independently inspected against their immutable crops, crop-equality JSON, and the canonical country-leader reference family under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/`. The reviewer was the Chaos Redux source-research subagent `/root/event6_mnt_portrait_research_v53` on 2026-08-01. At the time of the initial audit the copied PNGs had no producer-side linkage record; the later `repaint_source_lock_2026_08_01.md` record now supplies matching crop/master hashes, ImageGen output ids/hashes, prompt-pair hashes, and deterministic-candidate hashes, while producer identity and rights remain separate review gates.

| Candidate | Raw repaint dimensions / SHA-256 | Source crop dimensions / SHA-256 | Visual identity | Male/framing/artifacts | HOI4 painted style | Source/crop linkage | Rights/provenance |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `portrait_MNT_blazo_jovanovic_hoi4_master.png` | 926x1698 RGB / `4022dee805b4be1364d51f7fa481b66e706e93b7a1239c39931ca697e358e989` | 420x770 RGB / `fd5834027ece9dce94c7dd0f5a7f9b0b74559a85c2653619bc890b3fe117b880`; master SHA `a66cf887c8b28f86c92dedd763b3cb6bd046c01f6dff0f63825c07f30c64c120`; equality JSON SHA `16c1623457fa044ea4860a7ee40ca4063cfec5e91867ad306016240849c2c018` | `PASS`: the raw repaint preserves the source-visible cap with star, moustache, eye spacing, nose, jaw, ears, age presentation, and three-quarter facial geometry without face substitution or genericization. | `PASS`: one male subject, restrained bust/head-and-shoulders portrait, no extra people, readable text, watermark, logo, or border artifact observed. | `PASS`: subdued dark background, painterly brushwork, controlled contrast, and military clothing read as the vanilla HOI4 country-leader family when compared with the canonical leader references. | `NEEDS_USER_REVIEW`: visual correspondence to the exact crop is strong, but no generation prompt, source-lock record, or producer-side hash linkage was supplied with the copied PNG. | `NEEDS_USER_REVIEW`: the archival source has a Commons public-domain rationale but unknown photographer; no final rights or runtime admission is claimed here. |
| `portrait_MNT_blazo_dukanovic_hoi4_master.png` | 1162x1354 RGB / `af610f67ae7001d1348b6fda966f2c9e2e570dd670c25a992d0df3dfcf271874` | 390x455 RGB / `b626fe6089e3483f89a7fc0d553b69b16fa52ce8116b696d2f6e3362ec318cd9`; master SHA `b099dff0ad5b45d8dd33a10c9a0ccc113d4e08afa8ca1fa7c2d5fe68b76a8be8`; equality JSON SHA `0fdf3ed1a06876c4d16a0eff0298d954f1d6f31e8df4c508b1705ff7e84161e5` | `PASS`: the raw repaint preserves the source-visible high hairline, light hair, broad face, eyes, nose, mouth, ears, jaw, age presentation, and military-collar silhouette without a substituted face. | `PASS`: one male subject in a restrained bust/head-and-shoulders frame, no extra people, readable text, watermark, logo, or border artifact observed. | `PASS`: subdued dark background, painterly treatment, period military clothing, and controlled contrast match the canonical HOI4 country-leader family. | `NEEDS_USER_REVIEW`: visual correspondence to the exact crop is strong, but no generation prompt, source-lock record, or producer-side hash linkage was supplied with the copied PNG. | `NEEDS_USER_REVIEW` (not PASS): Commons asserts `PD-old`/Public Domain Mark for the unknown-photographer book reproduction, but the rights uncertainty explicitly remains open. |

The native-context comparison is retained at `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v53_2026_08_01/review/mnt_repaint_audit_native_2026_08_01.png` (SHA-256 `8e9b4fc45f27dfbe6e21a4c7752fce2e36315af682137df6f0f6eb1f8692806a`). The 4x nearest-neighbour inspection is retained at `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v53_2026_08_01/review/mnt_repaint_audit_4x_2026_08_01.png` (SHA-256 `120ef1348410a3c20433e5f771358424a82e658fe506030c3f3ea78e5687c21c`). Both sheets are review evidence only and are not runtime assets.

## Source/crop linkage addendum (2026-08-01)

The later `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v53_2026_08_01/repaint_source_lock_2026_08_01.md` record was independently checked against the current files. The source-master hashes, exact-crop hashes and coordinates, crop-equality JSON references, ImageGen output ids and hashes, durable prompt TXT hashes, raw repaint copies, and deterministic candidate source/output hashes all match byte-for-byte. The source/crop linkage dimension is therefore `PASS` for both candidates.

- **Jovanović source/crop linkage: `PASS`.** Master `a66cf887c8b28f86c92dedd763b3cb6bd046c01f6dff0f63825c07f30c64c120`; crop `fd5834027ece9dce94c7dd0f5a7f9b0b74559a85c2653619bc890b3fe117b880`; raw output `4022dee805b4be1364d51f7fa481b66e706e93b7a1239c39931ca697e358e989`; prompt TXT `e9bb311f28204f5fced24b4ff7c9fc50fb285f3a7dd728178009e4dab6a33a46`; deterministic candidate `769ae8ccd0fc3bd4ddd2ced1918b21ae37c1c281bd644c8c6df231d20c684b72` and matching candidate JSON source hash.
- **Đukanović source/crop linkage: `PASS`.** Master `b099dff0ad5b45d8dd33a10c9a0ccc113d4e08afa8ca1fa7c2d5fe68b76a8be8`; crop `b626fe6089e3483f89a7fc0d553b69b16fa52ce8116b696d2f6e3362ec318cd9`; raw output `af610f67ae7001d1348b6fda966f2c9e2e570dd670c25a992d0df3dfcf271874`; prompt TXT `feaf3ff9e1756cc1800fa06c2b461d09c0a0aed8dea10359b67366cff1457a2`; deterministic candidate `b5535b51c6cca13ad5dba381ad032e690c1ae3100a360e5b0c6fad646f3d73ae` and matching candidate JSON source hash.

This linkage `PASS` does not change rights or overall provenance status. Jovanović rights/source provenance remains `NEEDS_USER_REVIEW` because the archival photographer is unknown; Đukanović rights/source provenance remains `NEEDS_USER_REVIEW` and explicitly not `PASS` because the unknown-photographer book reproduction's Commons PD-old assertion is unresolved. No runtime DDS or `.gfx` admission is authorized.

This audit does not authorize DDS conversion or `.gfx` wiring. The Jovanović candidate is visually acceptable and source/crop-linked, but remains provenance/source-rights review pending; the Đukanović candidate is visually acceptable and source/crop-linked, but remains explicitly rights/provenance `NEEDS_USER_REVIEW`. Both require final admission review, not further source/crop linkage work.
