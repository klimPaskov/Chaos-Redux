# IW-050 / KOM portrait identity and source research — fail-closed handoff

Audit date: 2026-08-14.

Scope: `KOM_pavel_murashev` / Pavel Murashev and the fallback contract for an authentic archival image of the actual 1936 Komi institution.

## Exact verdict

**BLOCKED — no defensible 1936-period portrait source or rights basis was found for the exact vanilla identity, and no attributable archival image of the actual 1936 Komi institution was found.**

The package must remain fail-closed.

No portrait source placeholder, crop, generated face, processed PNG, DDS, GFX entry, character edit, central admission edit, or Join edit was created by this audit.

## Contract and local identity evidence

The source-of-truth research row is `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:51`.

That row requires a sourced real male leader valid for the release date, or authentic archival material for the actual provisional institution, and explicitly says to block the package until one is assigned.

The registered candidate is `IW-050,Komi,KOM` with compact anchor state `397,Syktyvkar` in `docs/specs/006_independence_wave_specs/research/006_candidate_country_registry.csv:51`.

Vanilla `common/characters/KOM.txt:3-13` defines `KOM_pavel_murashev`, display name `Pavel Murashev`, a civilian country leader with Stalinist ideology, expiry `1950.1.1.1`, and portrait key `GFX_portrait_Pavel_Murashev`, but gives no patronymic, biography, office, or 1936 date.

Vanilla `history/countries/KOM - Komi Republic.txt:101` recruits that character without adding identity evidence.

Vanilla `interface/_leader_portraits.gfx:5576-5579` maps `GFX_portrait_Pavel_Murashev` to the generic texture `gfx/leaders/Europe/Portrait_Europe_Generic_3.dds`; this is a generic runtime fallback, not an attributed historical source.

The vanilla character file comment says that very few Komi characters were found, which is not evidence for a portrait or an office assignment.

## Identity research

The strongest period-specific identity source located is the Komi Republican State Archive of Social-Political Movements guide hosted by EastView: [Первые секретари Коми рескома (обкома) партии](http://guides.eastview.com/browse/guidebook.html?bid=7&sid=1122).

That guide identifies **Мурашев Павел Иванович** as first secretary of the Komi regional VKP(b) committee from **November 1937 through June 1938**, born in Mednoe in the Tver Governorate, and arrested in June 1938.

This does not establish a 1936-start portrait identity: the documented Komi office begins almost two years after the game start, the vanilla character omits the patronymic, and the guide gives no portrait or image-rights record.

The National Library of Russia “Returned Names” record [Мурашев Павел Иванович](https://visz.nlr.ru/person/show/69672) instead gives a 1900 birth year and describes him as acting first secretary of the Komi regional committee; it exposes no image or portrait-rights statement.

The related [Open List record](https://ru.openlist.wiki/%D0%9C%D1%83%D1%80%D0%B0%D1%88%D0%B5%D0%B2_%D0%9F%D0%B0%D0%B2%D0%B5%D0%BB_%D0%98%D0%B2%D0%B0%D0%BD%D0%BE%D0%B2%D0%B8%D1%87_(1900)) gives the 1900 birth year and 21 June 1938 arrest date, but has no portrait and no reproducible image-rights grant.

The conflicting 1890/1900 birth data, absent patronymic in vanilla, office dates beginning in 1937, and lack of a period image make it unsafe to equate the underspecified vanilla key with a 1936 portrait source.

## 1936 institutional fallback research

The Presidential Library catalog entry [От Коми Авт. области к Коми АССР](https://www.prlib.ru/item/750113) identifies a genuine 1936 publication by the Komi Oblast Executive Committee for the XI Oblast Soviet Congress: `Сыктывкар : Коми обисполком, 1936`, 48 pages.

The catalog marks the item **Доступно только в Электронных читальных залах** and exposes no public image file, archival image identifier, or reproduction license.

The National Electronic Library catalog result [RU+NBRKOMIBIBL0000019009](https://nebrk.ru/docs/common/RU+NBRKOMIBIBL0000019009) describes the same 1936 booklet as `От Коми Авт. Области к Коми АССР : (к XI Областному съезду Советов)` by the Komi Oblast Executive Committee, but its public page did not expose a portrait or a downloadable institutional photograph.

The official National Museum of the Republic of Komi collection page [Документальные источники и кино-фото-фоно фонд](https://museumkomi.ru/?page_id=1235) confirms that the museum holds photographs and documents from republican events, organizations, and private persons, including 1920s–1930s material, but does not expose an attributable 1936 Komi institutional image on the page.

The museum’s exhibition article [У истоков зырянского парламентаризма](https://museumkomi.ru/?p=28278) dates the first Supreme Soviet of the Komi ASSR to 26 June 1938 and discusses 1920s–1930s documents, but the web images are modern exhibition documentation rather than a 1936 institution photograph.

The nearest visual historical lead, [Край, область, республика](https://ourreg.ru/2021/08/26/kraj-oblast-respublika/), explicitly captions its archival group image as delegates of the **I Congress of Soviets of the Komi Autonomous Oblast, 22–29 January 1922**, from National Museum funds; it is not a 1936 image and cannot satisfy this contract.

No “provisional institution” was silently invented from these records. A future acceptable institutional source would need an explicitly named 1936 body, archive or collection attribution, date or period basis, an image that actually depicts that body, and a rights/reproduction basis.

## Rejected image and runtime candidates

The image-search result at [epp.genproc.gov.ru](https://epp.genproc.gov.ru/ru/proc_10/activity/veterans-rights/sovet/veterans/e5518389/) is **Pavel Romanovich Murashev**, born 1914 in Karelia, a World War II veteran and prosecutor; it is not Pavel Ivanovich Murashev of the Komi regional committee. The reviewed file URL was `https://epp.genproc.gov.ru/upload/iblock/f9f/szy1x5g18vylbwohok3rwqn4wb6ka2dc.jpg`, dimensions `142x199`, bytes `6363`, SHA-256 `EA7DC1875B31CBBE9B464E5A710A4659069E75A568D9FC4985F0619EDAD341C3`. It was not archived or cropped because identity, 1936 relevance, and reproduction rights all fail.

The installed vanilla generic texture at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/leaders/Europe/Portrait_Europe_Generic_3.dds` is `156x210`, bytes `87368`, SHA-256 `1E1A7C0B6A20B1D2C8C26FE32538F704E43A61F2953BBD9A306CDA4397B74499`. It is the generic texture named by vanilla GFX and is not a source placeholder.

The existing Event 005 institutional texture at `gfx/leaders/005_soviet_collapse/KOM_leader.dds` is `156x210`, bytes `131168`, SHA-256 `7E4FA7228B12F0CACACD3CC57033CECACDB4D73E3B60E89B3567DA473D1F2460`. It belongs to the fictional Event 005 “Mine and River Committee” consumer and is not an authentic 1936 person or institution source.

The modern museum exhibition files reviewed but rejected were `IMG_0324.png` (SHA-256 `314ECBF451AE9C23F65E1AB024F60E992E6C044BD14E0D9145643D7D44D0D6B`), `IMG_0372.png` (SHA-256 `C1B18BD41F6FDB1575895C901AAD877124554A32B75360DB2D40EAADE31D5778`), and `IMG_02742.jpg` (SHA-256 `92D323A2865776DDAE007171C1516925C6D8ED3402CE7D8AED8D67DC983B7942`). They depict the modern 2018 exhibition and display material, not the historical institution, and no reuse license was exposed.

## Search ledger

Searches were run on 2026-08-14 using exact English and Russian name variants, `Коми АССР`, `Коми АССР 1936`, `Коми АССР 1936 съезд`, `Коми АССР 1936 обком`, `Павел Иванович Мурашев фото`, and `Мурашев Коми обком фото`.

Wikimedia Commons API exact-name and Russian-name searches returned no matching file; category checks for the history of Komi, Syktyvkar, Komi people, and Komi ASSR exposed no 1936 institution portrait.

Internet Archive advanced search returned no Pavel Murashev image and no 1936 Syktyvkar institutional portrait; Komi ASSR results were books, maps, and unrelated documents.

Russian State Library search returned `Ничего не найдено` for `Павел Мурашев`, `Коми АССР 1936`, and `Сыктывкар 1936`.

National Museum of the Republic of Komi site searches for `Павел Мурашев`, `Мурашев`, `съезд`, `Коми АССР`, and `1936` returned historical context and modern exhibition pages but no attributable 1936 portrait image.

Image-search matches were manually rejected when they were modern people, other Murashev/Murashov individuals, later Komi leaders, unrelated historical people, or images without a source caption and rights basis.

## Archive, processing, and wiring state

No IW-050, KOM, Murashev, or Pavel source file was present in the existing flat `docs/assets/portraits/006_independence_wave` archive or its existing single `processed/` directory at audit time.

No source URL record, provenance JSON, crop JSON, source crop, exact `156x210` placeholder, review sheet, processed PNG, DDS, portrait-specific GFX entry, or replacement marker was added.

`replacement_pending` is not set because no source was accepted.

The existing generic vanilla texture remains only a vanilla runtime reference; this handoff did not wire it, replace it, or change any character or gameplay file.

## Skipped checks and blocker

Crop/equality review, 4x nearest processing, PNG metadata review, DDS conversion, decoded-DDS comparison, portrait GFX wiring, and runtime portrait inspection were correctly skipped because the source and identity gates failed.

No native ImageGen or RunPod work is authorized for this grounded real-person/institution contract.

The blocker is either an attributable exact Pavel Ivanovich Murashev image with a defensible 1936-period basis and usable rights, or an explicitly named actual 1936 Komi institutional image with archive attribution, date, and reproduction rights.

Until one is supplied and verified, keep IW-050/KOM fail-closed and do not substitute the generic vanilla portrait, Event 005 art, another Murashev/Murashov, the 1922 congress image, a later leader, or a generated face.
