# IW-093 Asante — Prempeh II portrait rejection manifest

**Package date:** 2026-07-18
**Related event:** Event 006 — Independence Wave
**Package row:** IW-093 Asante (`DOX`)
**Package scope:** source and rejected-candidate evidence for one proposed large civilian country-leader portrait
**Asset status:** `blocked` — parent visual review rejected the candidate; no runtime DDS or sprite handoff exists.

## Rejection outcome

The deterministic processor preserved Prempeh II's identity, but the parent
review found that the result remained a sharpened grayscale archival photograph
and did not match the painted, colour HOI4 country-leader family shown by the
canonical references. The previously converted DDS was therefore deleted from
`gfx/leaders/006_independence_wave/` and must not be registered or used.

No replacement was produced in this follow-up. The archival source, lossless
source decode, rejected candidate, processor metadata, and comparison sheet are
retained only as source/research/rejection evidence.

## Source and rejected-candidate entry

| Field | Value |
|---|---|
| Asset name | Nana Otumfuo Agyeman Prempeh II |
| Asset type | Rejected real historical country-leader portrait candidate |
| Intended use | IW-093 Asante civilian leader / Asantehene Prempeh II; currently unresolved |
| Subject role and gender presentation | Male civilian country leader; personal identity, not a council or generic portrait |
| Source mode | Internet-sourced archival photograph; deterministic real-person leader processing |
| Source description page | `https://commons.wikimedia.org/wiki/File:Nana_Otumfuo_Agyeman_Prempeh_II.jpg` |
| Official archive page | `https://www.flickr.com/photos/nationalarchives/5416372614` |
| Author / archive / collection | The National Archives UK; Colonial Office photographic collection; Africa Through a Lens |
| Catalogue reference | CO 1069-44-12, part of CO 1069/44 |
| Source date | 31 January 1935 |
| Licence | Open Government Licence v1.0; Commons records VRT ticket `2012050210007172` and requires attribution to The National Archives UK |
| Licence URL | `https://www.nationalarchives.gov.uk/doc/open-government-licence/version/1/` |
| Era fit | Exact restoration-day subject; no reenactor, actor, postwar substitute, or reconstructed likeness |
| Original archival download | `source_image/CO_1069-44-12_prempeh_ii_1935.jpg` (`393x563`, RGB) |
| Lossless source PNG | `source_png/CO_1069-44-12_prempeh_ii_1935.png` (`393x563`, pixel-equal decode of the retained JPEG) |
| Attempted crop | `[105, 5, 275, 234]` in source pixels; `170x229` head-and-shoulders region |
| Processing record | `prompts/portrait_DOX_prempeh_ii_processing_brief.md` |
| Rejected processed PNG | `processed_png/portrait_DOX_prempeh_ii.png` — review evidence only; never wire or convert again without a new approval |
| Runtime DDS | **None.** `gfx/leaders/006_independence_wave/portrait_DOX_prempeh_ii.dds` was deleted after rejection |
| Target size | Required future replacement remains `156x210` |
| Sprite | **None authorized.** Former proposal `GFX_portrait_DOX_prempeh_ii` is reserved only and must not be registered against this candidate |
| `.gfx` owner | None; no interface file was edited |
| Related character consumer | Unwired; the parent-owned `DOX` Prempeh II character still lacks an approved custom portrait |
| Rejected comparison sheet | `contact_sheets/portrait_DOX_prempeh_ii_process_review.png` |
| Processor metadata | `metadata/portrait_DOX_prempeh_ii_processing.json` |
| Parent rejection record | `validation/visual_review.md` |
| Historical conversion record | `validation/dds_validation.md` — evidence that the deleted DDS matched the rejected PNG, not approval |
| GFX disposition | `gfx_handoff.md` — blocked/do-not-wire notice |
| Localisation key | Not inspected or edited |

## Source and licence evidence

The Commons record identifies the subject as Nana Otumfuo Agyeman Prempeh II,
dates the photograph to 31 January 1935, identifies The National Archives UK as
the source/author, and traces it to CO 1069-44-12 / CO 1069/44. It licenses the
file under OGL v1.0 with National Archives attribution and records a Wikimedia
VRT confirmation. The official Flickr archive page independently gives the
same subject, date, catalogue reference, Colonial Office collection, and
Africa Through a Lens provenance.

Required attribution if the source is used in future approved work:

> The National Archives UK, CO 1069/44 (CO 1069-44-12), 31 January 1935; used under the Open Government Licence v1.0.

The retained archival file is the verified `393x563` Commons copy. A fresh
download attempt during production received HTTP 429 from Wikimedia; the file
already retained by the preceding source-research pass was copied into this
package and pinned by SHA-256. No higher-resolution copy was available on the
Commons record.

## Rejected processor evidence

* Processor: `.agents/skills/chaos-redux-event-assets/tools/advisor_icon_processing.py`
* Processor version: `5.0`
* Leader render version: `2.0`
* Processor SHA-256: `e248979f21784c016e69c5458b9925c32177d6af29f2cca1a82bfaaffbe1f23c`
* Runtime: CPython `3.9.12`; Pillow `11.1.0`
* Source kind: `real`
* Deterministic seed payload SHA-256: `34ee10ecf18027211e20ba49b08a6531b877eb4c538a5ed2cc180633f05b2dff`
* Normalized processor-argument SHA-256: `35513db6783cec8f38ed6d25da4a97cf99585253e05379f50c4a2a19ef2c072b`
* Metadata-integrity payload SHA-256: `ab06949eef8aaabaf9ade6e0cf8c3d4b036c6c56abe71a32f7076ac0cc6a6adf`
* Processor metadata status: `candidate_requires_visual_approval`
* Parent visual verdict: **rejected**; mechanical processing did not achieve the required painted/colour HOI4 leader style.

The metadata remains unchanged as provenance for the rejected attempt. Its
recorded output paths and hashes describe the candidate at the time it was
processed; they do not constitute approval.

## Retained evidence hashes

| Evidence artifact | SHA-256 |
|---|---|
| Retained archival JPEG | `98a1109e23751f0ad64d970044c1c1eca3040333d7e16da357804b484587f144` |
| Lossless source PNG | `0ed4560bab1a38d5ba20f55c56b5ee9e7bb5afba66ca0ddb40589c357806a699` |
| Rejected processed PNG | `f113cefba729b8a852252d48c81965cce9a89595d3c1487a085056edc2ea9941` |
| Rejected process-review sheet | `6c0e7c91a37182968a51d0b21fd6c9a29c12cb0ff991e90610e6dc2cbf7bcad5` |
| Processing metadata JSON | `8d0b00c429b888a2fc0f63d61cd2c9d517fd5c027e550f4679dd540471eadf78` |

Deleted runtime artifact record: DDS SHA-256
`0e028b3ec9823fa356aa7c4618123215e06040d1092f37413dab5b2cc2b0ea0f`.
The hash is retained for audit only; that file no longer exists and is not an
approved asset.

## Requirement-to-runtime coverage

| Requirement | Accepted source | Source package evidence | Runtime registration | Live consumer | Audit evidence | Status |
|---|---|---|---|---|---|---|
| IW-093 Prempeh II civilian leader portrait | Event 006 IW-093/IW-098 source-research handoff, 2026-07-18 | CO 1069-44-12 source and this rejected-candidate package | None; rejected DDS deleted and sprite registration forbidden | None; Prempeh II remains without an approved custom portrait | Processor metadata, rejected comparison sheet, parent rejection in `validation/visual_review.md` | `blocked` |

## Unresolved blocker

The approved archival source supports a recognizable Prempeh II likeness, but
the current deterministic leader processor does not turn this monochrome
photograph into the painted, colour HOI4 leader style required by the parent.
The real-person rules forbid generating or reconstructing his face with
ImageGen, and no fallback or generic portrait is authorized.

Resolution requires one of the following before production resumes:

1. an approved identity-preserving real-person painting workflow that produces
   a genuinely painted HOI4 finish without generating or reconstructing facial
   features; or
2. a better attributed, rights-cleared source that can survive an approved
   real-person painted treatment while preserving Prempeh II's identity.

Implementation may continue only with this portrait requirement explicitly
open. It may not silently use a generic Africa portrait, the rejected candidate,
or another person.

## Scope exclusions

No advisor icon, advisor portrait, dossier, advisor sprite, commander-small
portrait, commander portrait, operative portrait, or second leader portrait
was created. No interface, character, history, event, focus, decision,
localisation, GUI, spreadsheet, or gameplay file was edited.
