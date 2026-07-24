# IW-179 FSM Micronesia civic source-clearance manifest

Status: **BLOCKED / no production-safe sourced candidate** as of 2026-07-24. The requested runtime consumer is `FSM_independence_wave_inter_island_congress_chair` (`GFX_portrait_FSM_independence_wave_inter_island_congress_chair`). The current Elias Kihleng image is a fictional generated adult male and does not satisfy the grounded-polity identity gate. No replacement person, sprite, processed portrait, DDS, or GFX handoff is approved.

## Acceptance gate

The requested replacement must be one identifiable real adult male from Pohnpei, the Caroline Islands, Micronesia, or a closely documented island-government/inter-island civic setting; the identity must be plausible for the 1936 game date; the photograph must be attributable to an archive or photographer; and the reuse basis must be explicit enough to permit a later source-locked portrait pipeline. A generic islander, an unnamed group photograph, a wrong-region subject, a post-1936 subject, or an image whose reuse requires an unresolved permission request fails closed.

## Candidate result

| Candidate | Identity and date evidence | Source and rights | Regional/role fit | Result |
| --- | --- | --- | --- | --- |
| Tem, Ibedul of Koror | `Traditional chiefs of Palau` lists Tem as Ibedul of Koror from 1917 to 1943, which covers 1936; this is a discovery lead, not a cleared identity source. | No attributable portrait of Tem was found in the searched archival/Commons records. | Palauan traditional-government role is temporally and institutionally plausible, but no image can be tied to Tem. | **No-pass: no portrait identity evidence.** |

There is no accepted candidate row because no source met both the identity and rights gates. Tem remains the best temporal/role lead only and must not be substituted into the character or localisation files without a named portrait source.

## Source audit register

| Source | Provenance | License or reuse basis | Date and era fit | Local research path | Sprite | Uncertainty and decision |
| --- | --- | --- | --- | --- | --- | --- |
| Tem, Ibedul of Koror | Succession chronology used as discovery lead from `Traditional chiefs of Palau`; no portrait object found. | Not applicable because no attributable image exists. | 1917–1943 office tenure; role fits 1936. | None. | None. | Identity cannot be tied to a face; **blocked/no-pass**. |
| `[ポナペ島民]` | Ezaki Teizō photograph in Kyushu University Library Collections, surfaced through NDL R100000092-I2324_2335335. | Advance application required to reuse; not ownership-clear. | First exhibited 1940; outside the 1936 target and title is generic. | `source/rejected_kyushu_2335335_canvas1.jpg`. | None. | Inspected canvas is an unnamed woman with two children; **reject**. |
| `酋長ト家族及部下 / 南洋ぽなぺ島` | Tanabe postcard collection, Kokushikan record 10135 / NDL R000000025-I012490000745614. | Repository flags private correspondence on addressed side; no clear reuse permission. | Showa-period image; visible caption says Aru Islands, not Pohnpei. | `source/26-115a.jpg`. | None. | Wrong region and unnamed group; **reject**. |
| `Koror chiefs in 1915` | Ryuzo Torii, University of Tokyo Digital Archive via Wikimedia Commons. | Commons lists PD-Japan-oldphoto, but the image has no individual labels. | 1915; pre-1936 and group-only. | None. | None. | Cannot identify Tem; **reject**. |
| Louch / Ilengelekei chiefly portraits | Wikimedia Commons attributed archival portraits. | Commons public-domain claims are recorded on the object pages. | Louch tenure ended 1917 and Ilengelekei tenure ended 1911; not plausible 1936 officeholders. | None. | None. | Deceased/era mismatch; **reject**. |

## Rejected source evidence

### Kyushu University and NDL `[ポナペ島民]`

- Object record: [NDL R100000092-I2324_2335335](https://ndlsearch.ndl.go.jp/books/R100000092-I2324_2335335).
- Persistent object handle: [Kyushu University handle 2324/2335335](http://hdl.handle.net/2324/2335335).
- IIIF manifest: [2335335 manifest](https://catalog.lib.kyushu-u.ac.jp/image/manifest/1/820/2335335.json).
- Canvas-1 source: [731958.tiff IIIF image](https://catalog.lib.kyushu-u.ac.jp/image/iiif/1/820/2335335/731958.tiff/full/max/0/default.jpg); the retained research copy is `source/rejected_kyushu_2335335_canvas1.jpg` with SHA-256 `D36739B51E8BC0B471C8143F78BD65914D78F6B08E957C3F33D1A2B62FC8CB16`.
- Metadata names `江崎, 悌三` (Ezaki Teizō) as photographer/author, not the people in the image, and describes the first appearance as the Emerging Asian Cultural Photography Exhibition in Fukuoka, 21–25 February 1940.
- The title is only `[ポナペ島民]` (“Pohnpei islanders”); the inspected canvas shows an unnamed woman with two children, not one identifiable adult male civic or traditional figure.
- The IIIF rights statement is “Advance application is required to reuse the material.” This is not an ownership-clear production source. Result: **reject for unnamed subject, female/children composition, and unresolved reuse permission**.

### Kokushikan / Tanabe postcard record `酋長ト家族及部下 / 南洋ぽなぺ島`

- NDL object: [R000000025-I012490000745614](https://ndlsearch.ndl.go.jp/books/R000000025-I012490000745614).
- Repository record/API: [Kokushikan record 10135](https://kokushikan.repo.nii.ac.jp/api/records/10135).
- Image URL: [26-115a.jpg](https://kokushikan.repo.nii.ac.jp/record/10135/files/26-115a.jpg); the retained research copy is `source/26-115a.jpg` with SHA-256 `DFD29329A1D5D35A9FFBD154048C9BE77292D6D1751B8919B14901E404FA229A`.
- The record title and keyword metadata mention Pohnpei, but the geolocation metadata identifies the Aru Islands and the visible English caption reads “King of Aru with his family and people.” The image is a group scene rather than an attributable individual portrait.
- The repository marks the postcard as not open because the addressed side contains private correspondence (`licensefree: 宛名面私信ありのため非公開`). Result: **reject for wrong region, group composition, and private/unclear reuse basis**.

### University of Tokyo / Commons `Koror chiefs in 1915`

- Object: [Commons File:Koror chiefs in 1915.jpg](https://commons.wikimedia.org/wiki/File:Koror_chiefs_in_1915.jpg).
- Direct image: [Koror chiefs in 1915](https://upload.wikimedia.org/wikipedia/commons/5/5b/Koror_chiefs_in_1915.jpg).
- The Commons record attributes the photograph to Ryuzo Torii, dated 1915, and points to the University of Tokyo “Digital archive of early photographs taken in eastern Asia and Micronesia” object [PCD3529 image 107](http://www.um.u-tokyo.ac.jp/cgi-bin/umdb/pcdview.cgi?volume=pcd3529&img=107&size=3&flip=). The image is a named-by-place group caption only; no subject labels identify Tem or any individual. Result: **reject for unnamed group identity**.

### Earlier Palauan chiefly portraits

- [Commons File:Louch and Palaun chiefs.png](https://commons.wikimedia.org/wiki/File:Louch_and_Palaun_chiefs.png) and [Commons File:Ibedul Louch.jpg](https://commons.wikimedia.org/wiki/File:Ibedul_Louch.jpg) identify Louch, Ibedul of Koror from 1911 to 1917; Louch died in 1917 and cannot serve as a plausible 1936 adult officeholder.
- Ibedul Ilengelekei is likewise documented as ending his tenure in 1911. These images are historically relevant but fail the 1936 era-fit gate.

## Ownership and collision scan

Exact-form scans were run for `Ibedul Tem`, `Tem Ibedul`, `Elias Kihleng`, and `Kihleng` across the current mod, vanilla HOI4, and approved Kaiserreich workshop roots (`1521695605`, `2265420196`, and `1458561226`). The current mod contains only the existing fictional Elias Kihleng character/localisation/docs references; no `Tem` or `Ibedul Tem` identity, portrait, sprite, or localisation binding was found in vanilla or the approved mods. This means there is no existing real-person ownership to reuse and no collision-free sourced asset to wire.

## Crop and downstream package status

No source passed the identity-and-rights gate, so the required unchanged-source head-and-shoulders crop was **not** run. There is no crop coordinate record, decoded-pixel JSON equality proof, source-locked repaint, processed PNG, final DDS, contact sheet, or `gfx_handoff.md` for this blocked package. This is intentional fail-closed behavior; creating a portrait from an unnamed or permission-restricted image would be an unsupported substitute.

## Next action

Keep the existing runtime binding unchanged and carry the source blocker. To resume, provide or locate one named adult male Micronesian/Pohnpeian/Carolinian civic or traditional figure with an attributable archival image, exact object URL, and explicit public-domain or reusable license basis. At that point this package can run the documented crop/equality gate before any later ImageGen repaint, deterministic PNG, DDS, or runtime wiring.
