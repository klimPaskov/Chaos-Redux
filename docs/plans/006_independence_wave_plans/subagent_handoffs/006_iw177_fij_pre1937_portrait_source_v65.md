# IW-177 FIJ pre-1937 male portrait source handoff

Date: 2026-08-01

Scope: source research and evidence only. No gameplay, GFX, localisation, DDS, advisor asset, admission-gate, or ImageGen files were edited.

## Bounded result

No fully release-ready 1936 FIJ leader portrait was found. Pt. Vishnu Deo is a defensible pre-1937 civic candidate and is retained as `needs_user_review`, not `complete`: his source is a contemporary 1929 archival male photograph with a public-domain claim, but he was not a Legislative Council member during the 1936 baseline (he returned in 1937), and the surviving image is a halftone reproduction whose facial detail is limited. The existing Ratu Sir Lala Sukuna source remains blocked by its explicit circa-1940s date.

## Candidate: Pt. Vishnu Deo

Role fit: Fiji-born Indo-Fijian political and communal leader; Arya Samaj leader and *Fiji Samachar* editor; associated with the Fiji Indian National Congress founded at Lautoka in 1929. The 1929 *Modern Review* page itself names “Mr. Vishnu Deo” among the six candidates for the three Indian Legislative Council seats, documenting a real civic/constitutional role before the 1936 start. Secondary biographical context records his 1929 election, 1932 ineligibility, and return to the Council in 1937; therefore the 1936 office-state gap must remain visible in any consumer decision.

Sources:

- Internet Archive item [The Modern Review, Vol. 46 (July–December 1929)](https://archive.org/details/dli.calcutta.09841), page image [n474 at native 600-dpi dimensions](https://archive.org/download/dli.calcutta.09841/page/n474_w4000.jpg). The scan is printed p. 459, *The Modern Review for October, 1929*, and captions the portrait “Mr. Vishnu Deo.”
- Wikimedia Commons [File:Vishnu Deo Fiji.jpg](https://commons.wikimedia.org/wiki/File:Vishnu_Deo_Fiji.jpg) and [direct original](https://upload.wikimedia.org/wikipedia/commons/7/7a/Vishnu_Deo_Fiji.jpg) independently identify the same 1929 *Modern Review* image, credit the publication, mark the anonymous photograph Public domain under `PD-India`, and identify the author as unknown.
- Role context: [Vishnu Deo](https://en.wikipedia.org/wiki/Vishnu_Deo) and [Legislative Council of Fiji](https://en.wikipedia.org/wiki/Legislative_Council_of_Fiji). These are context references, not substitutes for the archival image provenance.

Retained source/evidence files (ignored temporary asset workspace):

- Source page: `docs/assets/006_independence_wave/sources/fij_vishnu_deo_2026_08_01/n474_w4000.jpg` (4248x5866 RGB; SHA-256 `9e94a391473850efbcec3f08c3ccbc08ba588e1a52af908fe08727cc2ae658c5`).
- OCR corroboration: `modern_review_1929_v46_djvu.txt` (SHA-256 `0503d86750e3878839633778a93688a7e833fd66b08532937dd26ac43ce048b`).
- Exact head-and-shoulders crop: `vishnu_deo_modern_review_crop.png` (1040x1460 RGB; SHA-256 `a3e427e0a2ede7bdb72736c4e9d372188003a0e6142548d1884951507d76b3d0`). Crop rectangle is `(left=2520, top=1060, right=3560, bottom=2520)` in the unchanged page scan.
- Exact crop proof: `vishnu_deo_modern_review_crop.json` (`status: exact_source_crop_verified`; Pillow decode/reopen equality true; output RGBA SHA-256 `0d39d728065f90056213b603adcd64e3185b6aa11fb19822e46745e5407491a3`; crop utility SHA-256 `14fa178d6df999346874a7033e84f9b3ae988e7d845f3a4b2f8a44755e30641c`).
- Deterministic 156x210 review thumbnail: `vishnu_deo_preview_156x210.png` (SHA-256 `fe1eb17a90c3cba2f5053bfe27f6b7ba3e917bda6f2983471459b491078ac2ae`); evidence only, not a runtime portrait.

## Rights, era, and identity notes

- Era fit is strong for a 1936-centered event: the image was published in October 1929, seven years before the release baseline, and depicts a named adult male civic candidate.
- Commons' `PD-India` claim is based on an anonymous photograph first published in India in 1929; author identity is unknown. Preserve the Commons/Internet Archive links and the unknown-author limitation in any later manifest. Do not claim a photographer or a higher-resolution original.
- The page scan is visibly a halftone reproduction. It is identity evidence and a possible source-locked repaint input, not a final HOI4 texture by itself.
- No modern reenactment, film still, generated face, statue, or substitute identity was used. No real-person ImageGen repaint or DDS was produced in this evidence-only handoff; the parent scope and agent role prohibit generated real portraits here.
- The existing FIJ source manifest records a 2026-07-27 ownership sweep for `Vishnu Deo`/`Vishnu_Deo` with no Chaos Redux or targeted vanilla character/portrait ownership match. This handoff does not change that result or wire a consumer.

## Gate disposition

`needs_user_review` / not admitted. Parent approval is required for the 1936 consumer to use a leader who was not in Legislative Council office that year and for the halftone source's likeness quality. If strict 1936 office continuity or higher-resolution identity evidence is mandatory, keep FIJ blocked and request a National Archives of Fiji/Fiji Museum scan with a dated 1936-or-earlier capture and explicit reuse permission. Do not silently substitute the circa-1940s Sukuna photograph or generate an invented grounded leader.

