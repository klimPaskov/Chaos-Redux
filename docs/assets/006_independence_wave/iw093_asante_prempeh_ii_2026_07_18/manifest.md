# IW-093 Asante — Prempeh II country-leader portrait manifest

**Package dates:** 2026-07-18 source recovery; 2026-07-19 final portrait pass
**Related event:** Event 006 — Independence Wave
**Package row:** IW-093 Asante (`DOX`)
**Asset status:** archival source approved; former ImageGen-based runtime visual withdrawn

## Final asset

| Field | Value |
|---|---|
| Subject | Nana Otumfuo Agyeman Prempeh II |
| Consumer type | Male civilian country leader; never an advisor |
| Source photograph | `source_image/CO_1069-44-12_prempeh_ii_1935.jpg` |
| Historical ImageGen master | `source_png/portrait_DOX_prempeh_ii_imagegen_master.png` |
| Withdrawn PNG | `processed_png/portrait_DOX_prempeh_ii_hoi4.png` |
| Runtime DDS | `gfx/leaders/006_independence_wave/portrait_DOX_prempeh_ii.dds` |
| Runtime dimensions | `156x210`, uncompressed BGRA, one mip level |
| Sprite | `GFX_portrait_DOX_prempeh_ii` |
| Character | `DOX_prempeh_ii` |
| Superseded visual review | `contact_sheets/portrait_DOX_prempeh_ii_hoi4_review.png` and `validation/visual_review.md` |
| Processing metadata | `metadata/portrait_DOX_prempeh_ii_hoi4_processing.json` |
| Generation prompt | `prompts/portrait_DOX_prempeh_ii_imagegen_prompt.md` |

The installed image is an identity-preserving ImageGen edit of the attributed
1935 photograph. That production method is no longer allowed for a real-person
portrait. The unchanged TNA/OGL source remains valid and must be used for a new
explicit head-and-shoulders crop and deterministic HOI4 painted finish. The
historical ImageGen master, PNG, DDS, sprite, and review sheet remain provenance
and consumer evidence only; they do not grant visual or package readiness.

## Historical source and rights

| Field | Value |
|---|---|
| Description page | `https://commons.wikimedia.org/wiki/File:Nana_Otumfuo_Agyeman_Prempeh_II.jpg` |
| Official archive page | `https://www.flickr.com/photos/nationalarchives/5416372614` |
| Archive | The National Archives UK, Colonial Office photographic collection, Africa Through a Lens |
| Catalogue reference | CO 1069-44-12, part of CO 1069/44 |
| Source date | 31 January 1935 |
| Licence | Open Government Licence v1.0; Wikimedia VRT ticket `2012050210007172` |
| Licence URL | `https://www.nationalarchives.gov.uk/doc/open-government-licence/version/1/` |
| Era fit | Exact restoration-day subject |

Required attribution:

> The National Archives UK, CO 1069/44 (CO 1069-44-12), 31 January 1935; used under the Open Government Licence v1.0.

## Style references

The final visual review uses the skill-local canonical leader family under
`.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/`.
The generation pass specifically referenced the male vanilla-style examples
`eth_haile_selassie.png`, `afg_mohammed_zahir_shah.png`, and
`africa_generic_1.png`. These references control style and composition only;
the archival photograph controls identity.

## Hash ledger

| Artifact | SHA-256 |
|---|---|
| Archival JPEG | `98a1109e23751f0ad64d970044c1c1eca3040333d7e16da357804b484587f144` |
| Lossless archival PNG | `0ed4560bab1a38d5ba20f55c56b5ee9e7bb5afba66ca0ddb40589c357806a699` |
| ImageGen master | `5f4769bb6a290a0399cd4190757f2821e82b1ebe9d059f3e6f5ca8997f5ad86d` |
| Approved `156x210` PNG | `4f3ac8ecba82b41679a499bc56551440f5dad2772abaef8db0bd9570300f38a6` |
| Final review sheet | `0b55d9fc378ca202796d9dcd7fabf719051473810233a66c3998f0bd48ef49f6` |
| Final processing metadata | `9e819fe89bac8d72d875b7f0e51bfcbe76250b2fd5dd3ba72417115866217085` |
| Runtime DDS | `5fcab91f052810e66f3795734c55219488a592e513ab06f737dcbfb5cabbb26e` |

The decoded PNG and DDS RGBA byte streams both hash to
`33f8cbc6a5bbf90ebd6f543d75fa9f5acab16646218d343c1e6cb3cba77455b6`.

## Superseded candidate

`processed_png/portrait_DOX_prempeh_ii.png`,
`contact_sheets/portrait_DOX_prempeh_ii_process_review.png`, and
`metadata/portrait_DOX_prempeh_ii_processing.json` are retained as the rejected
grayscale-processing attempt. They are evidence only and must never be wired.
The 2026-07-19 asset supersedes that rejection without erasing its audit trail.

## Scope exclusions

No advisor icon, advisor portrait, dossier, advisor sprite, advisor manifest,
commander-small portrait, operative portrait, flag, or second leader portrait
was created in this package.
