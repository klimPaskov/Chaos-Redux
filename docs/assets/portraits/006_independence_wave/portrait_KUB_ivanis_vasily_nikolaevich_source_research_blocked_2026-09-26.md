# KUB Ivanis source research and rights gate

Date: 2026-09-26.

Asset: Event 006 / IW-040 / KUB leader `KUB_ivanis_vasily_nikolaevich`, state 234 / Krasnodar.

Classification: `grounded_source_only`.

Requested mode: `source_placeholder`.

Disposition: `blocked`; no source image is cleared for archival or runtime use.

Manifest status: `blocked` before sourcing/production promotion.

Planned use: one 156x210 large country-leader portrait for the exact KUB character during the active Event 006 package only.

Planned runtime sprite: `GFX_portrait_KUB_ivanis_vasily_nikolaevich_independence_wave` in `interface/006_independence_wave_portraits_registry.gfx`.

Planned runtime texture: `gfx/leaders/006_independence_wave/portrait_KUB_ivanis_vasily_nikolaevich_independence_wave.dds`.

Acceptance basis: the accepted portrait amendment in [Part 5](../../../specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_5_country_packages_and_regional_overlays.md) authorizes research and preparation of an exact-identity source placeholder and expressly forbids a substitute identity or unsupported source. It does not waive the source-rights gate.

## Subject and vanilla consumer

The exact installed character is `KUB_ivanis_vasily_nikolaevich` in `common/characters/KUB.txt`. Vanilla uses `GFX_portrait_KUB_ivanis_vasily_nikolaevich` for the large army portrait and `GFX_idea_KUB_ivanis_vasily_nikolaevich` for the small portrait; both roles and all metadata remain owned by vanilla and were not edited.

The installed No Step Back definition in `dlc/dlc034_no_step_back/interface/nsb_portraits.gfx` maps the large sprite to `gfx/leaders/KUB/portrait_KUB_ivanis_vasily_nikolaevich.dds`, but the referenced large DDS is absent from the installed game tree. The installed No Step Back small definition in `dlc/dlc034_no_step_back/interface/nsb_ideas_characters.gfx` maps the small sprite to `gfx/interface/ideas/idea_KUB_ivanis_vasily_nikolaevich.dds`; that file exists at 65x67 RGBA, 17,548 bytes, SHA-256 `c215128b588ffff5b03fc1885e0619dcc66cac31798b6cc3b514f48f31a26e93`.

The canonical role reference inspected was `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/contact_sheet.png` and the native 156x210 `afg_mohammed_zahir_shah.png` sample. The actual installed 65x67 small Ivanis DDS was decoded and inspected separately.

The current project scan found no exact subject token in `common/characters/`, `history/countries/`, `interface/`, `gfx/`, or `localisation/`; no matching new Event 006 portrait sprite exists in the shared portrait registry; and no target runtime DDS exists. Existing KUB package references remain under the parent agent's ownership and were not changed.

## Source candidates reviewed

### One-person portrait: `Ivanys V.jpg`

Source page: [Wikimedia Commons file record](https://commons.wikimedia.org/wiki/File:Ivanys_V.jpg).

Direct source: `https://upload.wikimedia.org/wikipedia/commons/7/7b/Ivanys_V.jpg`.

The Commons file description names the subject in Ukrainian as “Іванис Василь” (Vasyl Ivanys), and its subject category is `Vasyl Ivanys`. The local review download was a 343x458 JPEG, 38,551 bytes, SHA-256 `ACC3E81BA099FA0C96A69A9896D3139CAC2F0E7F3A8A9B21DE62663061DC1B23`. The source is a well-framed, readable one-person portrait and visually suitable for considering a deterministic country-leader crop.

The Commons file description records `Author=unknown`, `Source=фото` (“photo”), and `Date=unknown`. Its `PD-Ukraine` notice claims the work was published before 1 January 1952 and that the author, if known, died before that date. The file's own date field remains unknown, and no publication, archive, photographer, or permission record substantiating the pre-1952 publication claim was found. This is an unresolved rights claim, so this image was not archived as a source package or used for a crop.

Identity corroboration: the [Internet Encyclopedia of Ukraine biography](https://www.encyclopediaofukraine.com/display.asp?linkpath=pages%5CI%5CV%5CIvanysVasyl.htm) identifies Vasyl Ivanys, dates him 1888–1974, and records his Kuban government roles. Its [portrait page](https://www.encyclopediaofukraine.com/picturedisplay.asp?linkpath=pic%5CI%5CV%5CIvanys%20Vasyl.jpg&page=pages%5CI%5CV%5CIvanysVasyl.htm&id=5100&pid=13816&tyt=Ivanys%2C%20Vasyl) labels the displayed image “Vasyl Ivanys.” The encyclopedia does not provide a photographer, underlying archive, date, or reuse license for that portrait; the page supports identity but does not clear reuse rights.

### Contemporary group portrait: Government of South Russia, 1920

Source page: [Wikimedia Commons file record](https://commons.wikimedia.org/wiki/File:Government_of_South_Russia_1920_cropped.JPG).

Direct source: `https://upload.wikimedia.org/wikipedia/commons/2/2c/Government_of_South_Russia_1920_cropped.JPG`.

The file page dates the photograph to 1920 and its caption identifies the sixth seated person as “Deputy Kuban Ataman engineer V. N. Ivanis.” The source is 1400x1000 JPEG, 484,480 bytes, SHA-256 `95EC10893224D20A63DC624D43BCAE4DD8AD686E56E4A1EB62862F17D3203475`. The page lists an unknown author, links only to a LiveJournal user root as its source, and applies `PD-old` plus the Public Domain Mark. No photographer, source archive, author-death evidence, or first-publication date supporting the `PD-old` claim was located. The image is a multi-person seated group; a temporary crop study still included neighboring people and was not accepted as a portrait crop. Neither its rights nor its crop was cleared.

### Licensed group portrait: Senate at Poděbrady, 1942

Source page: [Wikimedia Commons file record](https://commons.wikimedia.org/wiki/File:%D0%A1%D0%B5%D0%BD%D0%B0%D1%82_%D0%A3%D0%93%D0%90_%D0%B2_%D0%9F%D0%BE%D0%B4%D1%94%D0%B1%D1%80%D0%B0%D0%B4%D0%B0%D1%85.png).

The file record identifies the 1942 book *Ukrainian Emigration* by S. Narizhnyi as the source, credits “Studio Museum of the Liberation Struggle of Ukraine, vol. 1,” and states CC BY-SA 4.0. The local review download was a 521x327 PNG, 120,681 bytes, SHA-256 `26FCADAE3D68F8ED8F2310646E235D25E69BF7184674A28EA0EFB2D6EC04134E`.

Its caption identifies a group as `Сенат УГА в Подєбрадах` (“Senate of UGA in Poděbrady”) but does not name Ivanis or identify his position in the group. The Commons category `Vasyl Ivanys` alone does not establish which of the several men is him, and visual comparison against the one-person portrait was not conclusive enough to assign the face. It therefore cannot serve as an exact-identity portrait without an identified person-level caption or a reliable source mapping him to one figure.

### Additional identity record

The [RIA 1914 personnel profile](https://ria1914.info/index.php?title=%D0%98%D0%B2%D0%B0%D0%BD%D0%B8%D1%81_%D0%92%D0%B0%D1%81%D0%B8%D0%BB%D0%B8%D0%B9_%D0%9D%D0%B8%D0%BA%D0%BE%D0%BB%D0%B0%D0%B5%D0%B2%D0%B8%D1%87) corroborates the name, life dates, and Kuban service. Its linked file [Фото.jpg](https://ria1914.info/index.php?title=%D0%A4%D0%B0%D0%B9%D0%BB:%D0%A4%D0%BE%D1%82%D0%BE.jpg) has no original photographer, date, or license statement; its 2013 digitization and 2014 modification metadata describe the digital file, not the historical photograph. It does not resolve source rights.

## Rights decision and exact missing evidence

No reviewed source combines both an unambiguous exact-person identification and a defensible, independently checkable reuse basis. The strongest one-person portrait is identified but has an unsupported public-domain date claim. The 1920 group photo names Ivanis but its author and public-domain basis are unsubstantiated, and its crop is crowded. The 1942 image has an explicit CC BY-SA 4.0 license but does not identify Ivanis among the people shown.

To reopen production, provide or locate either an exact-person image with an explicit license/permission or a primary archive/catalog record that identifies the photographer or collection and establishes the relevant public-domain term. For the 1942 licensed group image, a page-level caption, list, or reliable archive record must identify Ivanis and map him to a specific person in the photograph. A Commons category, an unexplained public-domain tag, or a visual guess is insufficient.

No candidate source bytes were copied into this repository because the rights gate failed. Candidate source dimensions and hashes above refer to research-only downloads; they are not shipped or archived asset files.

## Independent recheck by portrait subagent (2026-09-26)

The direct [Commons record for Ivanys V.jpg](https://commons.wikimedia.org/wiki/File:Ivanys_V.jpg) and its original file were fetched again. The original remains 343x458 JPEG, 38,551 bytes, SHA-256 `ACC3E81BA099FA0C96A69A9896D3139CAC2F0E7F3A8A9B21DE62663061DC1B23` as initially recorded above; visual inspection confirms a clear single-person portrait. The record still says author unknown, source “фото”, and date unknown. Its `PD-Ukraine` template asserts publication before 1 January 1952, but the page supplies no publication or archive evidence for that condition. The subject identity is corroborated because the Ukrainian biography uses this exact file in its infobox, but that does not resolve the rights gap.

The [Internet Encyclopedia of Ukraine biography](https://www.encyclopediaofukraine.com/display.asp?linkpath=pages%5CI%5CV%5CIvanysVasyl.htm) and [portrait page](https://www.encyclopediaofukraine.com/picturedisplay.asp?linkpath=pic%5CI%5CV%5CIvanys%20Vasyl.jpg&page=pages%5CI%5CV%5CIvanysVasyl.htm&id=5100&pid=13816&tyt=Ivanys%2C%20Vasyl) identify the person, while the site footer states that the Canadian Institute of Ukrainian Studies retains all rights. These pages remain identity corroboration, not reusable source authorization.

The direct [1920 Government of South Russia image](https://upload.wikimedia.org/wikipedia/commons/6/6f/Government_of_South_Russia_1920.JPG) was also re-fetched and visually reviewed at 1022x794 JPEG, 280,948 bytes, SHA-256 `5BE0C69AD374D6CBC0F9E4A45BAC14022C23FB0BCF63C4612BBF054DD9E81B6F`. Its Commons record attributes the photographer as unknown, credits only a LiveJournal user root, and does not document the publication or author-death facts needed to substantiate its public-domain claim. The identified person remains within a crowded group, so this is not an acceptable portrait crop.

The installed vanilla ownership and consumer checks were repeated: only the existing KUB character owns this exact portrait token, the large vanilla DDS remains absent, and the existing small idea DDS remains 65x67 RGBA with SHA-256 `C215128B588FFFF5B03FC1885E0619DCC66CAC31798B6CC3B514F48F31A26E93`. The canonical leader contact sheet, a native 156x210 leader reference, and the decoded small idea portrait were inspected. No newly surfaced source clears both identity and rights; disposition remains `blocked`, with no source archived or art processed.

## Requested primary-source, catalog, and license follow-up (2026-09-26)

The direct [Internet Encyclopedia of Ukraine portrait page](https://www.encyclopediaofukraine.com/picturedisplay.asp?linkpath=pic%5CI%5CV%5CIvanys%20Vasyl.jpg&page=pages%5CI%5CV%5CIvanysVasyl.htm&id=5100&pid=13816&tyt=Ivanys%2C%20Vasyl) labels the image “Vasyl Ivanys,” but gives no image-level photographer, archive, publication date, or reuse license; the site footer says “©2001–2026 Internet Encyclopedia of Ukraine. All rights reserved.” This corroborates identity only and does not authorize copying the encyclopedia-hosted image.

The Commons file-history API for `File:Ivanys V.jpg` confirms that the page was imported from Ukrainian Wikipedia's `File:Ivanys_V.jpg`; the file description remains `Author=unknown`, `Source=фото`, and `Date=unknown`, with only the `PD-Ukraine` template's unsubstantiated pre-1952-publication assertion. The Russian Wikipedia article API resolves the exact biography and embedded 343x458 original, but supplies no independent image provenance or rights record. A Wikidata search for `Василий Иванис` returns Q4195740, confirming a matching biographical identity but no source-photo evidence.

Exact catalog and source searches: Wikimedia Commons `Category:Vasyl Ivanys` returned the three candidate files described above; Openverse query `Vasyl Ivanys` returned zero results; Internet Archive query `title:(Ivanis) OR creator:(Ivanis)` returned six unrelated records, `title:("Українська еміграція") AND creator:(Наріжний)` returned zero, and `title:(Ukrainian emigration) AND creator:(Naryzhny)` returned zero; Open Library query `Naryzhny Ukrainian emigration 1942` returned zero; and the Google Books API query `"Українська еміграція" Наріжний` was rejected with HTTP 429 quota exhaustion. The Library of Congress Books API query `Naryzhny Ukrainian emigration 1942` returned a Cloudflare challenge page, so it yielded no catalog result.

The default web-search attempts used the exact queries `"Ivanis" "Vasily Nikolaevich" photograph`, `Иванис Василий Николаевич фотография портрет`, `Василий Николаевич Иванис Wikimedia Commons`, `Василий Николаевич Иванис архив фотография 1930`, and `"Василий Иванис" фото`; those requests timed out. Direct source-page and API checks above were used instead. No primary archival record, library record, author attribution, or publication evidence surfaced for the one-person Commons portrait.

The 1942 [Senate at Poděbrady Commons file](https://commons.wikimedia.org/wiki/File:%D0%A1%D0%B5%D0%BD%D0%B0%D1%82_%D0%A3%D0%93%D0%90_%D0%B2_%D0%9F%D0%BE%D0%B4%D1%94%D0%B1%D1%80%D0%B0%D0%B4%D0%B0%D1%85.png) explicitly declares CC BY-SA 4.0 and attribution required, and credits S. Narizhnyi's 1942 book and “Studio Museum of the Liberation Struggle of Ukraine, vol. 1.” Its description only names the group as the UGA Senate at Poděbrady; Ivanis appears only as a Commons category, not as a captioned or mapped individual. The listed license is a potential reuse basis for the group file, but neither its grant authority nor an exact person-level identification was substantiated, so it cannot clear this portrait.

The 1920 Government of South Russia group photo does provide a caption-level identification of Ivanis as the sixth seated person, but its page still lists an unknown photographer and a LiveJournal user root as source; no archive, first-publication record, or author-term evidence was found to substantiate its `PD-old` claim. Thus it does not clear the exact-person rights gate.
