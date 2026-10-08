# IW-076 Hadhramaut portrait source manifest

Status: `source candidate prepared; runtime blocked on unresolved first-publication/studio attribution/distribution-rights and succession coverage`.

The parent viewed the original and V2/V3 comparison on October 8 and accepts V3's preserved upper source area and visible face/shoulder tops for the archived source candidate.
This framing acceptance does not clear provenance, distribution rights, successor coverage, DDS conversion, runtime wiring or admission.

## Parent decision, identity, and date boundary

On 2026-10-08 the parent accepted Umar bin Awadh al-Qu'aiti as a conditional sourced candidate for the 1 January 1936 opening only. His recorded office is Sultan of Shihr and Mukalla, a distinct Qu'aiti coastal polity with Mukalla inside state 659. This is not a claim that he ruled all Hadhramaut; the later QDL catalogue treats Qu'ayti and Kathiri as separately named political parties.

The contemporary 1931 Government of India Aitchison volume, vol. XI, pp. 31-35, records Umar's succession and office and British recognition in 1923. The archived University of Queensland genealogy is secondary evidence that he reigned 1922-1936 and died on 6 March 1936. This supports the parent's conditional 1 January candidate only. Do not carry his leadership beyond 6 March 1936; before full package admission, the implementation must cover Salih/later openings after that date. The parent-supplied QDL catalogue describes Sultan Salih in a 1937 treaty record but does not establish his exact accession date. No successor portrait or leadership logic was researched or implemented in this bounded tranche.

## Grounded source and rights discovery

[Commons source page](https://commons.wikimedia.org/wiki/File:Umar_bin-Awad_al-Quaiti_(r1922-36).jpeg), page revision 1282297471. The unchanged 424x1056 RGB JPEG is archived at `CXX_hadhramaut_incumbent_original.jpeg`, SHA-256 `8071e8729bd88972ccc9604dd9370ccf13ecac2190c475e3a45ee86d1bd94aeb`. Commons describes it as a press photograph dated before 1936 and gives author `?Deen Dayal & Sons (Hyderabad)`; the question mark is preserved.

The initial Commons description revision 1146461798 (12 January 2026, 08:34) repeats the same fields and contains no original publication, archive collection, or verified studio identity. The current revision 1282297471 (1 October 2026, 20:39) is an Emijrpbot structured-data media-type claim for JPEG, not source or rights evidence. The Commons `PD-India` template claims public-domain status in India only; no first-publication date or wider jurisdiction status was found in the archived source record/history. No actual publication or studio identity proof was found. Do not make a wider legal guess.

The 1931 Aitchison primary source and archived succession chronology are linked in the prior citations below. The parent supplied [QDL catalogue item IOR/L/PS/12/1450 Coll1/12](https://www.qdl.qa/en/archive/81055/vdc_100000000517.0x0003ac): it describes a 1937 treaty draft with Sultan Salih bin Ghalib al-Qu'ayti, a separate 1939 draft with Sultan Ja'far bin Mansur al-Kathiri of Seiyun, and a 1939 Qu'ayti-Kathiri agreement. The parent-supplied details and route observation are preserved in `source_record_qdl_catalog.txt`; the catalogue does not resolve image rights or prove January 1936 admission.

## Crop candidates and framing review

The untouched source is 424x1056 RGB JPEG with no EXIF. Source crop production uses `.agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py` v2.0 and retains exact decoded-pixel equality evidence.

V1 `[0,70,424,641]` and V2 `[0,30,424,601]` remain byte-for-byte immutable and are now unselected variants. Their older contracts are retained unchanged as historical candidate receipts; this manifest controls the current selection. V1 clips the upper headwear. V2 preserves more shoulder area but excludes source rows 0-29.

V3 `[0,0,424,571]` is the selected source candidate for parent framing review, conditional on visible face and shoulder framing. At 156x210, the full face, collar, and shoulder tops remain visible; the shoulder margin is tight. The source-visible feature in rows 0-29 is preserved exactly and is not interpreted as a knob, feather, or artifact. The new contact sheet compares the full source with V2 and V3 at 4x nearest-neighbour: `CXX_hadhramaut_incumbent_framing_review_v3.png`, 1700x1080, SHA-256 `701e80ca3f56987318644a0da3836db8f0f63b2fdf28f114364186fa8e91f5ef`. Parent review of the V3 sheet remains outstanding.

The source scan remains soft and grainy at native portrait size; this is a raw source-placeholder candidate, not a HOI4-style final. No sharpening, retouching, repainting, background edit, or face reconstruction was applied. The Vanilla leader contact sheet and installed Mohammed Zahir Shah portrait were inspected first; the Vanilla texture is 156x210 and maps from `common/characters/AFG.txt` to `GFX_portrait_Mohammed_Zahir_Shah` in `interface/_leader_portraits.gfx`. It was used only as a role/style reference and was not copied. No portrait-backdrop reference was used.

## Ownership and planned runtime mapping

Searches of mod and installed Vanilla `common/characters/`, `history/countries/`, `gfx/leaders/`, `interface/`, and `localisation/` used `Umar bin Awadh`, `Umar bin Awad`, `Omar bin Awadh`, `Omar bin Awad`, `Umar al-Quaiti`, `Umar bin Awadh al-Quaiti`, and `Quaiti Sultan Umar`; no matching owner, portrait, or consumer was found.

Parent-reserved future mapping only: neutral `country_leader`; `gfx/leaders/CXX/CXX_hadhramaut_incumbent.dds`; sprite `GFX_portrait_CXX_hadhramaut_incumbent`. No DDS, runtime file, `.gfx` entry, or character portrait reference was created. No advisors or small portraits were produced. Human-supplied HOI4-style final is still required for a later installed source placeholder; no styled-final request is active. RunPod was never operated.

## V3 package files and key hashes

- Source: `CXX_hadhramaut_incumbent_original.jpeg`, 424x1056 RGB, SHA-256 `8071e8729bd88972ccc9604dd9370ccf13ecac2190c475e3a45ee86d1bd94aeb`.
- V3 source copy: `CXX_hadhramaut_incumbent_manual_v3_original.jpeg`, byte-identical to source, SHA-256 `8071e8729bd88972ccc9604dd9370ccf13ecac2190c475e3a45ee86d1bd94aeb`.
- V3 lossless crop: `CXX_hadhramaut_incumbent_manual_v3_source_crop.png`, 424x571 RGB, SHA-256 `767972e6b5052890eaafc85af015398dd5323297c3812672c7e649d812307a0d`; exact coordinates `[0,0,424,571]`.
- V3 crop metadata: `CXX_hadhramaut_incumbent_manual_v3_source_crop.json`, SHA-256 `2d4836d09c2828c22d7385952652abd00900a752bd5ab0befce92ff31340edc4`; decoded-pixel equality true, matching RGBA hash `bcf2a0f1e52970ead23c23f7e99bb6e3cc7b27ce41f15efb10fef4f3daeae48e`.
- V3 processed PNG: `CXX_hadhramaut_incumbent_manual_v3_156x210.png`, 156x210 RGB, SHA-256 `7ed65a5f788459c9545cf9b5a19c87fa07d52a4648c04bc84427aac4284f2814`.
- V3 contract: `CXX_hadhramaut_incumbent_manual_v3.txt`, SHA-256 `b7e27a92c1a15a086ae98769befa6456baa05655f082573dca5dde5ca10602de`.
- V3 comparison sheet: `CXX_hadhramaut_incumbent_framing_review_v3.png`, 1700x1080 PNG, SHA-256 `701e80ca3f56987318644a0da3836db8f0f63b2fdf28f114364186fa8e91f5ef`.
- Source history record: `source_record_commons.txt`, SHA-256 `cee02dc56eea97b6444c818ff2e51154732d5f363b3be57e6d54088210e309ae`.
- QDL catalogue record: `source_record_qdl_catalog.txt`, parent-supplied, SHA-256 `0e20b5bcced5f23454d97e2858c33308240e7bb325cbe5d4dab4a0ffe04fd820`.
- Previous V1/V2 files remain unchanged; their complete prior hashes remain in the preserved candidate JSON and previous manifest revisions.

## Rights, successor, and runtime blockers

Runtime status is exactly: `source candidate prepared; runtime blocked on unresolved first-publication/studio attribution/distribution-rights and succession coverage`. The exact individual is accepted only for the 1 January 1936 candidate; full Event006 admission remains blocked until leadership coverage after Umar's 6 March 1936 death is sourced and implemented. The 1937 QDL catalogue item places Salih as Sultan by that treaty draft, but does not supply an exact succession date or portrait license. Rights remain blocked on unresolved first-publication/studio attribution/distribution status beyond PD-India. No DDS conversion, `.gfx` wiring, character wiring, or gameplay edits were made by parent decision. D34 remains closed.

Direct Commons page-history and initial-revision reads were successful. The parent-provided narrow QDL search returned after an earlier `search_session_locked` HTTP 409. Direct QDL catalogue and folio fetches in this worker returned HTTP 403; the parent-supplied catalogue contents are explicitly marked as such in the source note. The earlier broad web search calls in this worker timed out. No game, logs, ImageGen, RunPod, DDS conversion, runtime, or Git write was used.
