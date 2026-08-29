# IW-179 FSM portrait source gate handoff (2026-08-29)

## Disposition

`BLOCKED / fail-closed`. The research tranche found a rights-cleared historical Pohnpeian image, but it does not establish that the named man was a 1936 civic officeholder or remained available for the Event 006 opening. No candidate is admitted to the FSM council-chair consumer, and `independence_wave_fsm_sourced_identity_ready` remains unset.

The current consumer is `FSM_independence_wave_inter_island_congress_chair`, whose existing large-leader path is `GFX_portrait_FSM_independence_wave_inter_island_congress_chair` -> `gfx/leaders/006_independence_wave/portrait_FSM_independence_wave_inter_island_congress_chair.dds`. The withdrawn fictional Elias Kihleng evidence portrait remains non-admissible and was not used as a fallback.

## Candidate gate review

| Candidate | Identity and regional fit | Adult and role evidence | 1936 period fit | Source and rights | Decision |
| --- | --- | --- | --- | --- | --- |
| Nanaua | Named as the nephew of King Rocha of Kiti, Pohnpei, in the source caption. | The scanned plate visibly shows one adult man in ceremonial dress seated on a `parror`, and the caption supplies an exact traditional/royal-kin role. | `HOLD`: the source is from an 1899 book and provides no evidence that Nanaua held a civic or council role, or survived, in the 1936 opening. | `PASS`: the Commons file page identifies the scan as Public domain under `PD-old-100-expired`; the stable IA page image is 1475x2439. | Not admitted because the required 1936 role/continuity gate is unproven. |
| Petrus Mailo | Micronesian/Chuukese political and chiefly lead. | Existing research records secretary of Moen in 1932, Chief of Nepukos in 1933, and Leader of Section No. 2 of Moen in 1936-38. | Role and period fit are strong. | `FAIL`: UHM items 22714 and 20273 are postwar Trust Territory archive material with no explicit reusable licence, and the exposed item material is not a stable rights-cleared full-resolution portrait. | Research lead only; no source admission. |
| Henry Nanpei | Exact Pohnpeian identity and historical political/religious prominence. | ScholarSpace figure 19 identifies Henry Nanpei at age 31 in 1891. | `FAIL`: the historical figure died before the 1936 opening, so he cannot represent the consumer. | `FAIL`: the source book is marked `CC BY-NC-ND 4.0`; the required crop/resize derivative is not licensed. | Rejected; no crop or archive copy. |
| Kabua Kabua | Marshallese paramount-chief lead, not a strong Pohnpeian/Carolinian identity match. | Role analogy is not an exact FSM civic/traditional match. | Unproven for the consumer. | Existing evidence is a small group thumbnail with ambiguous reuse terms. | Explicitly excluded and not substituted. |

## Nanaua source evidence

The source is Frederick William Christian, *The Caroline Islands; travel in the sea of the little lands* (London: Methuen & Co., 1899), the plate captioned `NANAUA, NEPHEW OF KING ROCHA OF KITI, SEATED ON HIS PARROR, OR CARPET OF CEREMONY`.

- Stable scanned page image: `https://archive.org/download/cu31924023239506/page/n188_w2000.jpg`.
- Source item and attribution: `https://archive.org/details/cu31924023239506` (Internet Archive identifier `cu31924023239506`, Cornell University Library scan, publication date 1899).
- Explicit rights page: `https://commons.wikimedia.org/wiki/File:The_Caroline_Islands;_travel_in_the_sea_of_the_little_lands_(IA_cu31924023239506).pdf` (Public domain, `PD-old-100-expired`, attribution not required).
- The inspected page image is 1475x2439 pixels, 528174 bytes, SHA-256 `dd8ab34ac6d8ac90d31fe9e3e512ce7482d3d2d442b9117e490170fd6dae6788`.
- The 1899 plate is a stable full-page archival source, but no crop was created because the period/role gate failed.

## Archive and runtime boundary

`docs/assets/portraits/006_independence_wave/` remains unchanged, including its `processed/` subfolder. No source master, crop, PNG, DDS, GFX entry, character definition, localisation, gameplay file, central admission, or source flag was changed. `convert_to_dds.py` was not run because there is no admitted runtime candidate.

The next safe tranche needs an explicitly documented 1936-continuity or exact civic-office source for an adult FSM/Pohnpeian/Carolinian man. Until that evidence exists, the package remains source-blocked and the fictional Elias portrait must stay withdrawn.

## Ownership and commit status

This handoff is the only repository file changed by this tranche. The parent requested a temporary commit hold while an unrelated Event 025 boundary is corrected, so no commit was created.
