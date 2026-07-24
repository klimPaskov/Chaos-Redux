# IW-002 Wales — Saunders Lewis age-appropriate source gate

Research date: 2026-07-24.

Status: `blocked`.

Asset: the full-size male country-leader portrait for `WLS_independence_wave_national_council`.

Source mode: `grounded_source_only` / internet-sourced real male photograph.

No candidate passed the combined identity, archival-photograph, age/era, rights/access, and ownership gates. This package deliberately contains no source master, crop, processed PNG, ImageGen result, DDS, GFX edit, advisor, dossier, `_small` derivative, gameplay edit, or localisation edit.

## Current consumer and ownership result

The current Chaos Redux consumer is the dynamically-created male civic leader `WLS_independence_wave_national_council`, assigned in `common/scripted_effects/006_independence_wave_scotland_wales_package_effects.txt:257-272`, displayed through `GFX_portrait_WLS_independence_wave_national_council` in `interface/006_independence_wave_region_01_portraits.gfx:63-64`, and named in `localisation/english/006_independence_wave_scotland_wales_l_english.yml:5-6`. No separate advisor, commander-miniature, dossier, or `_small` consumer is authorized for this role.

Exact and variant searches covered `Saunders Lewis`, `John Saunders Lewis`, `J. Saunders Lewis`, `Lewis Saunders`, `saunders_lewis`, `WLS_saunders_lewis`, and `WLS_independence_wave_national_council` across the current project's character, history, portrait, interface, and localisation surfaces and the installed vanilla `common/characters/`, `history/countries/`, `gfx/leaders/`, `interface/`, and `localisation/` roots. Vanilla has no Saunders Lewis character, recruitment, portrait, GFX, or localisation owner. The current Chaos Redux token above is the sole live owner.

The approved Kaiserreich reference mod has a same-person owner at `common/characters/WLS characters.txt:97-120`, `history/countries/WLS - Wales.txt:36`, `interface/kaiserreich/portraits/WLS_portraits.gfx:31-40`, and `localisation/english/KR_country_specific/WLS - Wales l_english.yml:208-210`. This is disclosure-only under the mutually-exclusive-mod policy; no Kaiserreich source, art, or character transfer is authorized and no guarded transfer contract exists. Approved reference mods `2265420196` and `1458561226` had no exact Saunders Lewis owner.

## Source leads and dispositions

| Lead | Source and evidence | Disposition |
|---|---|---|
| Saunders Lewis, *Y Drych*, 3 February 1916 | [Commons file](https://commons.wikimedia.org/wiki/File:Saunders-lewis-y-drych-1916.jpg) and [National Library of Wales newspaper scan](https://papuraunewydd.llyfrgell.cymru/view/3776384/3776392/60/). The pre-1931 publication basis is recorded as public-domain evidence. An unchanged local master already exists at `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/sco_wls_grounded_retry_01/source_masters/WLS/WLS_saunders_lewis_ydrych_1916.jpg`; it is not copied or reprocessed here. | Rejected for this gate. It shows Lewis at about 22-23, twenty years before 1936, and the two prior source-locked ImageGen trials failed the separate likeness gate. It cannot justify a younger/older invented reconstruction. |
| Dr Gwent Jones, October 1936 | The age-matched lead is identified in the scan of [*The Story of Plaid Cymru*](https://bibliotheque.idbe.bzh/data/cle_203/the__story__o__plaid__cymru.pdf): “Saunders Lewis writing his address to the jury in Caernarfon Crown Court,” photographed by Dr Gwent Jones in October 1936. | Blocked on rights/access. The scan is a later book reproduction; no direct archival original, photographer/estate permission, or rights-clear download was located. No PDF page or extracted image is retained as a source master. |
| Geoff Charles, 4 October 1973 | [Commons file 1520393](https://commons.wikimedia.org/wiki/File:Saunders_Lewis_(1520393).jpg), sourced from the National Library of Wales, CC BY-SA 4.0. Existing source-only evidence is retained in `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/wls_saunders_lewis_geoff_charles_1973_source/`. | Rejected as a 1936 runtime base. Lewis was approximately 79-80; preserving the source preserves the wrong age, while reconstructing a 1936 face violates the source-locked identity gate. |
| People's Collection Wales group photograph, originally dated 1960 | [Item 14040](https://www.peoplescollection.wales/items/14040), owner Plaid Cymru, creator unknown, Creative Archive Licence. | Rejected. Lewis was approximately 66-67, the image is a group scene rather than a clean head-and-shoulders source, and the page requires non-commercial use or direct rights-holder permission. |
| Swansea University Digital Collections, c.1973 | [Item 1521](https://collections.swansea.ac.uk/s/history-of-computing-collection/item/1521), “Saunders Lewis sitting at a desk,” rights holder University of Wales Press. | Rejected. Postwar age mismatch and no rights-clear runtime licence. |
| Famouspeople Wales / National Library of Wales page image | [Saunders Lewis page](https://famouspeople.wales/famous-people/saunders-lewis/). The page gives no archival date or underlying photographer and states ©2024 National Library of Wales, all rights reserved. | Rejected. Rights, date, and original-source chain are not clear. |
| Modern memorial crop | [Commons plaque photograph](https://commons.wikimedia.org/wiki/File:Llosgi%27r_Ysgol_Fomio_-_The_Burning_of_the_Bombing_School_-_geograph.org.uk_-_356846.jpg) and extracted “portrait” crop. | Rejected. This is a 2007 photograph of a memorial/plaque, not an archival photograph of Lewis; a CC BY-SA licence cannot change that identity failure. |
| Swansea Archives c.1920s drawing record | [University College Swansea record](https://archives.swansea.ac.uk/Record.aspx?id=UNI%2FSU%2FPC%2F9%2F1%2F2&src=CalmView.Catalog), item 39, “photograph of drawing of Saunders Lewis by Powys Evans, c.1920s.” | Rejected. The depicted work is a drawing, not a photograph of Lewis, and cannot serve as the identity master. |

The current [Commons Saunders Lewis category](https://commons.wikimedia.org/wiki/Category:Saunders_Lewis) contains the 1916 newspaper source, the six 1973 Geoff Charles photographs, and the modern memorial crop, but no newly identified 1920s-1940s rights-clear archival portrait.

## Processing boundary and reopening condition

The package stops at source research. Do not use the 1973 source, the 1916 source, the 1960 group photograph, the memorial crop, or any generated substitute as a runtime base. Do not create a source crop until a new unchanged archival photograph passes the source gate.

Reopen only when an actual photograph of Saunders Lewis from approximately 1920-1940, preferably near 1936, is acquired from an identifiable archive or photographer/estate with a defensible reuse licence or public-domain basis, the binary is preserved unchanged, and the owner search remains clear for the current Chaos Redux token. The reopened chain must then use `extract_portrait_source_crop.py` with retained exact-pixel JSON evidence before any later portrait processing or runtime work.
