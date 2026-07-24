# IW-179 FSM Micronesia civic source-clearance research log

Date: 2026-07-24. Scope was limited to a sourced real male identity for `FSM_independence_wave_inter_island_congress_chair`. No gameplay, character, localisation, interface, GFX, ImageGen, DDS, or runtime files were edited.

## Required references inspected

- Repository instructions: `AGENTS.md`.
- Event-asset workflow: `.agents/skills/chaos-redux-event-assets/SKILL.md`.
- Canonical leader reference root: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/README.md`, `CATALOG.md`, `leader_portraits/README.md`, and `leader_portraits/REFERENCE_MANIFEST.md`.
- Canonical leader contact sheets were visually inspected with `view_image` to confirm the large-leader portrait framing and head/shoulder expectations.

## Discovery and verification notes

### Tem / Ibedul of Koror

The [Traditional chiefs of Palau](https://en.wikipedia.org/wiki/Traditional_chiefs_of_Palau) page was used only as a discovery lead for the succession chronology: Tem is listed as Ibedul of Koror from 1917 to 1943, which covers the 1936 scenario. Wikimedia Commons searches for `Tem`, `Ibedul Tem`, `Koror Tem`, and `Mariur` found no named portrait that could identify Tem. The available 1915 `Koror chiefs` group image has no individual labels, so it cannot be used to infer Tem's face. This remains a temporal/role lead, not an accepted person source.

### NDL / Kyushu University Pohnpei image

The NDL record [R100000092-I2324_2335335](https://ndlsearch.ndl.go.jp/books/R100000092-I2324_2335335) and the [Kyushu IIIF manifest](https://catalog.lib.kyushu-u.ac.jp/image/manifest/1/820/2335335.json) identify a 1940 exhibition image titled `[ポナペ島民]`, with 江崎悌三 (Ezaki Teizō) as photographer. The record's rights field requires advance application to reuse. The inspected canvas depicts an unnamed woman and two children and carries no civic/traditional identity. The source copy is retained only as rejected evidence at `source/rejected_kyushu_2335335_canvas1.jpg`.

### NDL / Kokushikan postcard image

The NDL object [R000000025-I012490000745614](https://ndlsearch.ndl.go.jp/books/R000000025-I012490000745614), [Kokushikan API record 10135](https://kokushikan.repo.nii.ac.jp/api/records/10135), and [26-115a.jpg](https://kokushikan.repo.nii.ac.jp/record/10135/files/26-115a.jpg) were inspected. Although the Japanese title includes “Pohnpei island,” the repository geolocation says Aru Islands and the visible English caption says “King of Aru with his family and people.” The image is a group scene, not an individual portrait. The repository also marks the item as unavailable because the addressed side contains private correspondence. It is retained only as rejected evidence at `source/26-115a.jpg`.

### Japanese period photo books

NDL's [南洋群島写真帖](https://dl.ndl.go.jp/info:ndljp/pid/1688640) (二葉屋, 1933) was checked through its item metadata and page index. The Pohnpei and Palau entries are generic place or meeting-house captions, with no named individual who could satisfy the identity gate. The item therefore contributes period/context evidence but no production candidate.

### Earlier chiefly portraits

Commons records for Louch and Ilengelekei were checked against the Palau chiefly succession. Both figures' documented tenures ended before 1936 (Louch died in 1917; Ilengelekei's tenure ended in 1911), so they were rejected even where image attribution was available.

## Ownership scan results

The exact forms `Ibedul Tem`, `Tem Ibedul`, `Elias Kihleng`, and `Kihleng` were scanned with `rg` across the current mod, vanilla HOI4, and approved Kaiserreich workshop roots. The current mod returned only existing Elias Kihleng references; vanilla and all three approved workshop roots returned no matching candidate identity. No existing portrait ownership or collision was found for Tem because no Tem asset exists in those roots.

## Fail-closed decision

The package is **BLOCKED / no-pass**. Identity and rights evidence are insufficient for every reviewed image, and no crop/equality proof is possible without first clearing a named person source. A guessed face, generic “Pohnpei islander,” unnamed chief group, or wrong-region Aru photograph would violate the grounded real-person asset rules.
