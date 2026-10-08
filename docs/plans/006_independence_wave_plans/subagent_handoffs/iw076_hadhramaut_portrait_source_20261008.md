# IW-076 Hadhramaut portrait source handoff - 2026-10-08

Status: `source candidate prepared; runtime blocked on unresolved first-publication/studio attribution/distribution-rights and succession coverage`.

## Conditional identity decision and date boundary

The parent accepted Umar bin Awadh al-Qu'aiti as a sourced candidate for 1 January 1936 only. The documented office is Sultan of Shihr and Mukalla, the Qu'aiti coast polity at Mukalla; do not claim that he ruled all Hadhramaut. The 1931 Government of India Aitchison volume, vol. XI, pp. 31-35, supports his succession/office and British recognition in 1923. The archived University of Queensland genealogy is secondary evidence for his reign through 1936 and death on 6 March 1936. The parent explicitly requires sourced leadership coverage for Salih/later openings after that date before full package admission; never keep Umar alive after the date by assumption. D34 remains closed.

The parent-supplied QDL catalogue describes Sultan Salih in a 1937 draft treaty and separately names Sultan Ja'far bin Mansur al-Kathiri of Seiyun in 1939 records. This corroborates later separate treaty parties but does not establish Salih's exact accession date or resolve the succession implementation gate.

## V3 crop and review

V1 and V2 are preserved byte-for-byte as unselected variants. V3 uses manual crop `[0,0,424,571]` from the unchanged 424x1056 source. Its lossless crop is 424x571 RGB, SHA-256 `767972e6b5052890eaafc85af015398dd5323297c3812672c7e649d812307a0d`; the standard crop tool JSON confirms exact decoded-pixel equality and matching source/crop RGBA hash `bcf2a0f1e52970ead23c23f7e99bb6e3cc7b27ce41f15efb10fef4f3daeae48e`. The deterministic candidate PNG is 156x210 RGB, SHA-256 `7ed65a5f788459c9545cf9b5a19c87fa07d52a4648c04bc84427aac4284f2814`.

I reviewed the V3 frame at native size and 4x nearest-neighbour. The face and shoulder tops remain visible, with tighter shoulder margin than V2. The light-toned feature above the headwear in source rows 0-29 is retained in V3; it is not identified or reconstructed. The [full-source/V2/V3 sheet](../../../assets/portraits/006_independence_wave/iw076_hadhramaut_20261008/CXX_hadhramaut_incumbent_framing_review_v3.png) is 1700x1080 PNG, SHA-256 `701e80ca3f56987318644a0da3836db8f0f63b2fdf28f114364186fa8e91f5ef`. V3 is selected as the source candidate for parent framing review only.

## Rights discovery from the archived source

Parent review on October 8 selects V3 for archival candidate framing after viewing the unchanged original and V2/V3 sheet.
The review accepts preservation of the upper source area and visible face/shoulder tops without identifying or reconstructing the light feature.
Runtime remains blocked on the recorded provenance/rights and successor coverage; no historical leader, source placeholder or styled final is installed by this review.

I checked the [Commons file history](https://commons.wikimedia.org/w/index.php?title=File:Umar_bin-Awad_al-Quaiti_(r1922-36).jpeg&action=history) and the initial description revision 1146461798. Its fields match the current page: press photograph, before 1936, `?Deen Dayal & Sons (Hyderabad)`, and PD-India. The latest revision 1282297471 adds only a bot structured-data JPEG media-type claim. Neither revision links an original publication, archive collection, or verified studio identity. No better publication/studio proof was found within the archived Commons source. Keep attribution and first-publication uncertainty; rights beyond the Commons PD-India claim remain unresolved. Do not infer that the uploader or the `Lala Deen Dayal` category identifies the actual photographer.

## Source and package evidence

Unchanged original: 424x1056 RGB JPEG, SHA-256 `8071e8729bd88972ccc9604dd9370ccf13ecac2190c475e3a45ee86d1bd94aeb`. V3 crop source copy is byte-identical. V3 metadata and contract hashes are recorded in the package manifest. The updated Commons history note and parent-supplied QDL catalogue note are in `source_record_commons.txt` and `source_record_qdl_catalog.txt`, respectively. The [manifest](../../../assets/portraits/006_independence_wave/iw076_hadhramaut_20261008/manifest.md) lists V3 dimensions and hashes and supersedes prior selection labels; V1/V2 artifact bytes were not changed.

## Runtime and skipped work

No DDS was produced, by parent decision. No runtime portrait, `.gfx` entry, character portrait reference, gameplay, admission, localisation, or history file was changed. Parent-reserved future path/sprite remain `gfx/leaders/CXX/CXX_hadhramaut_incumbent.dds` and `GFX_portrait_CXX_hadhramaut_incumbent`. No ImageGen, retouch, source-face alteration, RunPod, game, logs, or Git writes were used. A later HOI4-style final must be supplied by the user; no styled final is claimed.

The parent must resolve first-publication/studio attribution/distribution-rights and sourced successor coverage before runtime promotion or full admission. Direct Commons history was readable, the parent-supplied narrow QDL search returned after an earlier HTTP 409, and direct QDL page/folio requests in this worker returned HTTP 403. The parent-supplied QDL details are preserved with that provenance distinction.
