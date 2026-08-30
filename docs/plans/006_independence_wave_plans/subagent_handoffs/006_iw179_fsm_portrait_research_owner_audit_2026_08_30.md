# IW-179 FSM portrait research-owner audit (2026-08-30)

## Disposition

`BLOCKED / fail-closed`. No named adult male Micronesian, Pohnpeian, or Carolinian civic or traditional governing figure reviewed for IW-179 simultaneously clears identity, adult and 1936 role continuity, stable full-resolution attribution, explicit derivative/reuse rights, and the unchanged-source portrait pipeline.

The admission flag `independence_wave_fsm_sourced_identity_ready` remains unset. The withdrawn fictional `Elias Kihleng` identity is not a grounded substitute, and no regional generic portrait is authorized.

## Exact consumer and ownership boundary

The current consumer is `FSM_independence_wave_inter_island_congress_chair` in `common/characters/006_independence_wave_characters_registry.txt:1086-1099` with the male metadata and civilian-large sprite `GFX_portrait_FSM_independence_wave_inter_island_congress_chair` in `interface/006_independence_wave_small_assets.gfx:93-94`.

The existing runtime path is `gfx/leaders/006_independence_wave/portrait_FSM_independence_wave_inter_island_congress_chair.dds`, exactly `156x210`, `131168` bytes, SHA-256 `64db23c13f8f3f488079ea24ca4d8ef9326bbb3fd9abbc94ee9b9251b004ae29`. It is a withdrawn generated evidence asset, not source-placeholder admission evidence.

The source gate is enforced by `common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt:225-245`, which requires `independence_wave_fsm_sourced_identity_ready` before setup can expose or promote the consumer. No gameplay, character, localisation, interface, GFX, runtime, or central-admission file was changed by this audit.

## Reference review

The matching installed-Vanilla leader reference family was inspected at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/`, including its labeled contact sheet and `CATALOG.md`. The shelf contains eight full `156x210` leader references extracted from Vanilla HOI4 build `Operation Postern v1.19.2.0.a729 (d245)`, and the inspected contact sheet is `1200x498`, SHA-256 `8966ae351d1fe8fc13d47ca1c59ec3d8a34da9101ce5fd65f7acff3421bd0401`.

These references control only full-leader framing, scale, transparency, and restrained HOI4 presentation. They are not identity sources and cannot justify reusing a Vanilla face or a regional generic.

## Candidate gate review

| Candidate or lead | Identity and role evidence | Image, rights, and period gate | Disposition |
| --- | --- | --- | --- |
| Petrus Mailo | Named Micronesian/Chuukese chief and politician; existing chronology places him as secretary of Moen in 1932, Chief of Nepukos in 1933, and Leader of Section No. 2 of Moen in 1936-1938. | UHM item `22714` and its IIIF manifest expose a circa-1958-1975 Trust Territory archive portrait context, not a 1936-compatible source; the exposed Wikipedia file is only `280x353` and marked fair use/non-free. UHM's copyright policy provides no open reuse grant and places permission determination on the user. | Strong role lead only; rights, era-image, and full-resolution derivative gates fail. |
| Nanaua | Named Pohnpeian traditional/royal kin, captioned as nephew of King Rocha of Kiti. | The Internet Archive/Cornell 1899 plate is stable at `1475x2439`, SHA-256 `dd8ab34ac6d8ac90d31fe9e3e512ce7482d3d2d442b9117e490170fd6dae6788`, and the Commons record identifies `PD-old-100-expired`. The image provides no evidence that Nanaua held a civic or council role, or remained alive and available, in 1936. | Rights and source resolution pass; 1936 role/continuity gate fails. No crop or placeholder. |
| Henry Nanpei | Exact Pohnpeian political and religious figure; the available source identifies him at age 31 in 1891. | The Micronesian Seminar PN01036 source is image-unavailable. The visible HF01005 record is a `120x168` thumbnail with catalog-only “Not Restricted” wording and no explicit derivative licence; the source figure also cannot represent the 1936 opening under the documented life chronology. | Period/continuity, source-resolution, and derivative-rights gates fail. |
| Tem Ibedul | Named Palauan high-chief lead with a documented 1917-1943 service window, but not an exact Pohnpeian/Carolinian FSM identity. | No attributable, stable, full-resolution, rights-cleared portrait was found. | Research lead only; image and rights gates fail. |
| Kabua Kabua | Named Marshallese paramount-chief and later Congress/Council of Iroij figure, but Marshallese rather than the preferred Pohnpeian/Caroline identity. | The Micronesian Seminar c1930 `RR01026` object is a four-person `120x91` thumbnail, prior SHA-256 `1ea0e66227a54e56f403f1e1f3a1f627e158bd24508d7c5f653e9fa8f749c812`; “Digital, Not Restricted” is catalog metadata, not a reuse licence, and no original scan is exposed. | Explicitly excluded; weak regional fit, group composition, source resolution, and rights fail. |
| Erhart Aten, John Mangefel, Bethwel Henry, Andon Amaraich | Named Micronesian politicians, but their documented births in 1932-1934 make them children during the 1936 opening; their public careers are postwar. | No period portrait search can repair the adult/role failure. | Rejected at adult and 1936 role gate. |
| UHM “Mok” and Commons/NDL period groups | UHM's one-word “native chief, Mok” caption and the period Chuuk/Pohnpei scans identify a role or unnamed group, not the IW-179 named chair. | The UHM source is 1944 and lacks an explicit reuse grant; public-domain or CC scans still cannot authorize assigning an unnamed person to a grounded leader token. | Rejected as identity-invention or rights-risk sources. |

The source URLs and earlier research records remain available in `006_iw179_fsm_portrait_source_gate_retry_2026_08_30.md`, `006_iw179_fsm_portrait_source_gate_2026_08_29.md`, `006_event6_fsm_petrus_mailo_source_research_current_2026_08_03.md`, `006_iw179_micronesia_kabua_kabua_source_closure_2026_08_01.md`, and `006_iw179_micronesia_henry_nanpei_source_retry_2026_07_26.md`.

Primary source links used by those records are [UHM item 22714](https://digital.library.manoa.hawaii.edu/items/show/22714), [UHM IIIF manifest](https://digital.library.manoa.hawaii.edu/iiif/22714/manifest), [UHM copyright policy](https://manoa.hawaii.edu/library/research/scholarly-communication/repositories/policies-guidelines/copyright-policy/), [Micronesian Seminar Kabua search](https://micsem.org/library/search-photos-results?subject=Kabua%20Kabua), [Internet Archive/Cornell Caroline Islands scan](https://archive.org/details/cu31924023239506), and the [Commons public-domain record](https://commons.wikimedia.org/wiki/File:The_Caroline_Islands;_travel_in_the_sea_of_the_little_lands_(IA_cu31924023239506).pdf).

## Withdrawn generated evidence state

The existing generated Elias Kihleng package remains evidence only and is not a source packet. Its retained ImageGen master is `1080x1456` RGB, `2385980` bytes, SHA-256 `9bb42598ddca666a9f5bdedf5ccafcf5bb1d6a12c9a0f93bf894bf7188e7d52c`; the processed candidate is `156x210` RGBA, `71038` bytes, SHA-256 `0ab2385c51562af1557bf3839dbe3fedcf9f5bc19a1a76564709fe997cc68310`; and the package/runtime DDS hash is the value recorded above. The package manifest already marks this portrait withdrawn, and its fictional prompt cannot be converted into a grounded identity.

No `docs/assets/portraits/006_independence_wave/` source package was created for a rejected candidate. The current durable portrait archive contains no FSM source master, crop, crop-equality JSON, provenance contract, or accepted processed candidate. The prior Kabua proxy path cited by the 2026-08-01 handoff is not present in the current checkout, so its recorded hash is retained only as historical rejection evidence.

## Gate result and skipped production checks

No candidate clears every gate. Therefore no source was archived as an accepted durable portrait, no lossless crop or decoded-pixel equality JSON was created, no ImageGen call was made, no provider/RunPod operation was performed, no `156x210` source-placeholder PNG was admitted, and `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` was not run for a grounded candidate.

No independent likeness/framing/provenance review, DDS round-trip review, `gfx_handoff.md`, source-placeholder replacement, or live HOI4 consumer validation can be claimed. The existing GFX path remains technically present but withdrawn, and there is no `replacement_pending` state because no explicit styled-final request is outstanding; the portrait state is `blocked`.

## Next owner and required transition

The next source owner must obtain a named adult male Pohnpeian or Carolinian civic/traditional governing figure, or a precisely documented Micronesian figure whose role and 1936 continuity are defensible, together with an attributable stable full-resolution image and explicit public-domain/open licence or written derivative/reuse permission.

After that evidence arrives, `chaosx_portrait_creator` should preserve the unchanged original under `docs/assets/portraits/006_independence_wave/` using the exact runtime basename, run `extract_portrait_source_crop.py` with exact crop/equality evidence, obtain independent identity/framing/provenance approval, create the deterministic source-placeholder PNG and DDS, and hand the parent the provenance/runtime packet. Only the parent may review central admission and set `independence_wave_fsm_sourced_identity_ready` after the complete package gates pass.

## Files changed and commit

Only this dated research-owner handoff was added. No runtime asset, source archive, manifest, GFX, character, localisation, gameplay, or readiness flag changed.

