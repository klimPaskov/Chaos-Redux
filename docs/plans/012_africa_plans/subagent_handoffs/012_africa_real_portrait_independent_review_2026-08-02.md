# Event 012 Africa real-person portrait independent review

Date: 2026-08-02.

Reviewer: `/root/event012_real_portrait_independent_review`, independent of the producer.

Scope: I compared the five current immutable source crops, the current raw source-locked repaint outputs, the processed `156x210` PNGs, the source manifest and handoff files, and the canonical country-leader references under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/`.

No source, crop, raw repaint, processed PNG, DDS, `.gfx`, gameplay, character, localisation, or source-package file was edited by this review except for this handoff.

## Review gate

`PASS` below means that the current raw repaint and processed PNG pass the independent visual likeness, age/expression, source-visible clothing or regalia, unintended-addition, plain-background, and HOI4 leader-style checks.

`FAIL` means that a non-compensable identity or source-visible-object/clothing violation is present and the current candidate must not be promoted.

`REVIEW` means that the available source or identity evidence cannot support an independent approval, or that a source-detail question must be resolved before promotion.

The source crops were checked at native size and at `4x` nearest-neighbour inspection scale against the raw and processed candidates. The current Harar raw output is the latest post-update file with SHA-256 `3ae77a266233f7f573a396185aeacc7975532d7644e90a360308a6bbe8adfa80`; earlier Harar repaints were not used.

## Evidence chain and current hashes

Every selected crop JSON reports `status: exact_source_crop_verified` and `equality.decoded_pixels_equal: true`.

| Row | Exact source crop | Current raw source-locked repaint | Processed candidate |
| --- | --- | --- | --- |
| Kanem-Bornu | `crops/kanem_bornu_sanda_kura_source_crop.png` (`550x740` RGB, `c2d103581f948323448a911b979b619eb43a560b3626a27723f9f765165d6bcb`) | `source_generated/portrait_012_africa_priority_kanem_bornu_sanda_kura_source_locked.png` (`1082x1453` RGB, `e283b96c00f7e14debbd8fde32707c251763070acd1246a2dd92583123159fbf5`) | `processed_png/portrait_012_africa_priority_kanem_bornu_source_locked.png` (`156x210` RGBA, `dd59ec4b1da98ec4f27280b2ea85623bb2c6a501ca0a9cc6db354904008a11c1`) |
| Harar | `crops/harar_emir_abdullahi_source_crop.png` (`450x605` RGBA, `a00c0a8158548b62d66faf28ee821e36654badf406984a2ba24ec15f1bf466aa`) | `source_generated/portrait_012_africa_priority_harar_abdullahi_source_locked.png` (`1085x1450` RGB, `3ae77a266233f7f573a396185aeacc7975532d7644e90a360308a6bbe8adfa80`) | `processed_png/portrait_012_africa_priority_harar_source_locked.png` (`156x210` RGBA, `0db62830d5f71df96eacd3521b2b341baf36b6c0485b72d5d03fe0486daa192f`) |
| Kongo | `crops/kongo_pedro_vii_source_crop.png` (`340x460` RGB, `c27251f2bddb66ad9fdcc627ea7deffa8b757a52086f9bc90fb7121e58c9b49e`) | `source_generated/portrait_012_africa_priority_kongo_pedro_vii_source_locked.png` (`1085x1450` RGB, `d25c4149517ebc5ae26a19a0588c51b891cb2e9ef2d11f4cf9f3df949889adc9`) | `processed_png/portrait_012_africa_priority_kongo_source_locked.png` (`156x210` RGBA, `7144850b6ed12ef7321dfc2916be188b78788f49b16993bd1ddccdebe37c5859`) |
| Buganda | `crops/buganda_mutesa_ii_source_crop.png` (`145x195` RGB, `3e0ff185d04bfc39d5c934c0b2ea3a6beb6cd72d982b5df854a951b63eb9a79b`) | `source_generated/portrait_012_africa_priority_buganda_mutesa_ii_source_locked.png` (`1024x1536` RGB, `b27df4b3494e94c48988a6f1e4b62b8e5212ba6580e1f8df8255d177c214d709`) | `processed_png/portrait_012_africa_priority_buganda_source_locked.png` (`156x210` RGBA, `370a5205be9890b25edb5fd7dc4e8e8366daa06acfacdea3e579be7e6a6d17e3`) |
| Merina | `crops/merina_ranavalona_iii_source_crop.png` (`1150x1550` RGB, `0e1e1f9c6688d5af92e99dc0404027434b01798fdad84ca59a1ac25a341a72f7`) | `source_generated/portrait_012_africa_priority_merina_ranavalona_iii_source_locked.png` (`1085x1450` RGB, `35f80f3d0a3ee7f8fecad2ad257db91eb910063affc09038d60fcae489f65136`) | `processed_png/portrait_012_africa_priority_merina_source_locked.png` (`156x210` RGBA, `d71b0cf0f9a31486b610dee2898b3a8eba4cd913ffa29a11db39b686daf0fafa`) |

The processed candidates are opaque RGBA images, matching the opaque canonical leader reference family. All five have a quiet painted background with no text or watermark. The existing `final_dds/` folder also contains five DDS derivatives, but DDS conversion and runtime admission were not approved or audited by this handoff.

The earlier Harar raw hash `88f5fb98248f980536cd47f8a89df80db5da00a6bf7891291c12e9db3b464afc` and processed hash `7b65b08273ac7d2d196e85a21959fb88e658eab37df9e1116fb5fbdd7569fed2`, and the earlier Kongo raw hash `2424fbecba4c10ece3a3fd48f3fefc1beebdce338fc3e0cc45c5caec78a3236b` and processed hash `7beb47c76ae7daab7890086c716a8bb3157eccb21ef5a9ebd4ef668d1153d7a7`, are superseded and must not be used for promotion.

## Per-row verdicts

### Kanem-Bornu — Shehu Sanda Kura

**Verdict: PASS for the independent visual gate.**

The raw repaint preserves the source's older face, deep-set eyes, broad nose, white beard, slight facial asymmetry, large wrapped white turban, light outer robe, dark embroidered inner robe, and the source-visible star-shaped chest medal. The age band and restrained, mildly smiling-to-neutral expression remain close enough for a source-locked painted interpretation, and the processed candidate keeps the face and medal readable at native `156x210` size.

No weapon, mask, animal head, face paint, crown, or other unsupported object is introduced. The brown-gold texture is a plain background and remains within the painted leader-family treatment, although it is warmer and more textured than the canonical neutral references.

The source/crop provenance is documented in `manifest.md` as the 1936 Shehu Sanda Kura source with exact crop equality and a public-domain Commons basis. The selected master is explicitly a vendor scan, so the parent must retain the Commons page and vendor URL rather than silently presenting the vendor byte as a direct Commons download.

Before promotion, record the current raw and processed hashes above in the manifest or durable event documentation, rename the synthetic character/localisation to Sanda Kura or Shehu Sanda Kura, and keep the source vendor-scan caveat. This visual PASS does not authorize the current DDS or runtime sprite by itself.

### Harar — Emir Abdullahi

**Verdict: PASS for the independent visual gate, with a low-resolution source caveat.**

The current direct-Common source crop shows a long, narrow, clean-shaven face with a direct gaze, thin mouth, and plain white turban and robe. The current raw repaint keeps the jaw clean-shaven, retains the long facial silhouette, direct gaze, narrow nose, thin mouth, and large wrapped turban, and uses painted shadow under the chin rather than inventing a beard. The processed PNG carries the same corrected identity treatment and remains readable at native `156x210` size.

The source is soft and low-resolution, so fine eye and cheek detail is reconstructed rather than provable pixel-for-pixel, but I found no material face substitution, unsupported facial hair, weapon, mask, crown, face paint, or clothing addition. The white turban, plain robe, quiet background, and restrained painted leader treatment pass.

The source chain is defensible: the current crop hash is `a00c0a...466aa`, the manifest identifies the direct Commons original and the Gallica frame-33 attribution, and the Commons record carries CC BY-SA 4.0. Before promotion, record the current raw and processed hashes above, retain the CC BY-SA attribution/share-alike note, and keep the exact Emir Abdullahi identity. This visual PASS does not independently authorize the existing DDS or runtime sprite.

### Kongo — Pedro VII Afonso

**Verdict: PASS for the independent visual gate.**

The current raw repaint retains the source moustache, round spectacles, peaked ceremonial hat and plume, staff, hand placement, dark embroidered robe, and broad cape silhouette. The corrected cape reads as pale ceremonial cloth with painted weave texture and source-visible dark spots, not fur or an animal pelt. The processed candidate carries the same source-supported clothing treatment and keeps the face, spectacles, moustache, plume, and staff readable at native `156x210` size.

No crown, animal head, spear, face paint, or other unsupported object is introduced. The plain background and restrained painted leader treatment pass. The source/crop provenance is documented as the named 1934 Pedro VII and Isabel photograph from the Lisbon Geographic Society with a public-domain Commons record and exact crop equality.

Before promotion, record the current raw and processed hashes above, use the exact Pedro VII Afonso identity, and retain only the source-visible pale cloth cape, plume, embroidery, staff, spectacles, moustache, and hand placement. This visual PASS does not independently authorize the existing DDS or runtime sprite.

### Buganda — Mutesa II

**Verdict: REVIEW, not an independent PASS.**

The raw repaint keeps the dark peaked cap, dark right-facing ceremonial or military-style uniform, belt, and general profile direction. The native processed card is readable but very dark, and it sharpens a cap badge, shoulder insignia, cross-body strap, buttons, and chest decorations that cannot be reliably established from the `145x195` source crop.

The source is the third person from the left in a four-kings group photograph, and the caption names that position as the Kabaka of Buganda. The crop is heavily shadowed and profile-obscured, so the exact eyes, nose, mouth, age, and expression cannot be independently confirmed from the image alone. This is the explicit group-photo identity warning in the source notes, not a minor style difference.

No leopard skin, royal drum, spear, crown, or face paint is added, and the UK National Archives/Crown Copyright expiry provenance and exact crop equality are documented. The parent must independently confirm the third-from-left identity or obtain a higher-resolution single-person source and must remove any uniform insignia or decorations that cannot be tied to the crop. Until that is done, do not promote the current raw, processed PNG, or DDS.

### Merina — Queen Ranavalona III

**Verdict: PASS for the independent visual gate.**

The raw repaint preserves the narrow left-facing face, braided hair, source-visible head ornament, lace collar, ruffled sleeves, dark embroidered gown, veil, and carved throne. The age band, gaze, and reserved expression remain close to the source, and the female identity reads clearly in the native processed card.

The enlarged head ornament is a stylized rendering of the ornament already visible on the source head. It is not the separate broad crown on the table in the full master, which is outside the exact crop and has not been moved onto her head. No scepter, weapon, face paint, military uniform, male facial treatment, or other unsupported object is introduced. The plain warm background and controlled painted treatment fit the country-leader reference family despite the more elaborate chair and gown, both of which are source-visible.

The source/crop provenance is documented as the University of Southern California Libraries ca. 1890–1895 photograph with a public-domain Commons record and exact crop equality. Before promotion, record the current raw and processed hashes above, change the synthetic Merina character to Queen Ranavalona III with female metadata and matching localisation, and preserve the separate-table-crown constraint. This visual PASS does not independently authorize the existing DDS or runtime sprite.

## Documentation and promotion blockers

The source manifest correctly labels the five rows as `source_ready_repaint_pending_audit` and records source links, era fit, license position, exact crop paths, hashes, and visible-regalia constraints. It does not yet record the current raw repaint paths, processed paths, hashes, deterministic processing record, or this independent review result.

`validation.md` and the source-ready text in `gfx_handoff.md` still state that no source-locked repaint, processed PNG, or DDS exists, but the current workspace contains all five raw outputs, all five processed candidates, and five DDS derivatives. The parent should reconcile those stale statements before treating any row as complete.

The four visual PASS rows are evidence-only until the parent updates the manifest, changes the grounded character identities and sex metadata where required, and performs the parent-owned ownership, localisation, `.gfx`, DDS, and runtime checks. The Buganda row remains REVIEW and has no runtime approval because its group-photo identity and added uniform detail are unresolved. No fallback or generic real-person substitute is approved by this review.
