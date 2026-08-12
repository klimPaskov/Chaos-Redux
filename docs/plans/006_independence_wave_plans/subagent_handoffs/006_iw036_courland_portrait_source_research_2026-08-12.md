# IW-036 Courland (BJX) portrait-source research handoff

Research date: 2026-08-12.

Scope: grounded male Courland/Kurzeme leadership and authentic Liepāja institutional portrait candidates for Event 006 IW-036. No gameplay, character, `.gfx`, localisation, runtime portrait, DDS, or source-archive files were changed. The downloaded research copies remain outside the repository in `C:\Users\klimp\AppData\Local\Temp\iw036_portrait_research\`.

## Gate and reference contract

IW-036 is a grounded historical regional package. The bounded plan requires a period institution joined to a provisional cabinet/municipal administration and says that portraits must use a sourced real male officeholder or authentic archival material; a generated personal portrait is not an allowed fallback. The candidate is therefore blocked unless identity, source chain, date fit, and rights are independently defensible.

Portrait role references inspected before research:

- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/contact_sheet.png` and its male leader references (`den_thorvald_stauning.png`, `fin_carl_mannerheim.png`, `ice_sveinn_bjornsson.png`, `ire_eamon_de_valera.png`). All canonical leader textures are full `156x210` portraits.
- Offline `paradox_wiki/Portrait modding - Hearts of Iron 4 Wiki.md`: portraits are normally `156x210`; portrait sprite definitions belong in a `.gfx` file and point to the leader texture.
- Vanilla `interface/_leader_portraits.gfx` and `common/characters/FIN.txt` (Mannerheim precedent): large leader portrait points to `gfx/leaders/<TAG>/portrait_<tag>_<name>.dds`; small idea art is a separate surface and must not be inferred for this package.

## Candidate dispositions

### 1. Leonhards Lapa — recommended source lead, runtime HOLD pending crop/rights review

- Identity and role: the Latvian municipal-history article [`Liepājas pašvaldības vadītāju uzskaitījums`](https://lv.wikipedia.org/wiki/Liep%C4%81jas_pa%C5%A1vald%C4%ABbas_vad%C4%ABt%C4%81ju_uzskait%C4%ABjums) lists Leonhards Lapa as Liepāja city head from 1928–1934. Liepāja is the principal Kurzeme/Courland regional city, so this is a real regional officeholder immediately preceding the 1936 start rather than a fabricated claimant.
- Source: [Commons `File:Leonhards Lapa.jpg`](https://commons.wikimedia.org/wiki/File:Leonhards_Lapa.jpg), direct original URL `https://upload.wikimedia.org/wikipedia/commons/9/93/Leonhards_Lapa.jpg`.
- Commons metadata: description “Liepājas pilsētas galva 1928-1934”; unknown author; date “between 1928 and 1935”; license marked Public domain (Commons categories include `Author died more than 70 years ago public domain images` and `PD-old missing SDC copyright status`); original `516x618` JPEG.
- Research copy: SHA-256 `F884EADFB38463F092944AF0F5BB78AF2B620BAE7E4B9C26027288AD83192C1F`, 103,010 bytes, decoded `516x618`.
- Visual review: genuine period black-and-white group photograph; Lapa is centered, large, and readable in suit and tie, but neighboring figures remain at both edges. A deterministic head-and-shoulders crop is feasible; no portrait crop or DDS was made.
- Verdict: identity **PASS**; era fit **PASS** (office term ends two years before 1936); source/rights **CONDITIONAL PASS** (Commons public-domain marking, but unknown author/source chain needs an explicit provenance review); framing **HOLD** until crop coordinates and decoded-pixel equality are recorded. This is the best current one-person lead.
- Next step: parent approves Lapa as the source-placeholder subject, then portrait worker archives the unchanged original, records the Commons metadata and rights caveat, produces an exact crop/equality JSON, and independently reviews the `156x210` candidate. Do not repaint or generate a substitute face.

### 2. Ēvalds Rimbenieks — identity/1936 fit PASS, rights HOLD

- Identity and role: [`Ēvalds Rimbenieks`](https://lv.wikipedia.org/wiki/%C4%92valds_Rimbenieks) identifies him as Liepāja domes chair in 1922–1928 and 1934–1940, making him the strongest direct 1936 officeholder lead; he was born in Aizvīķi in the Courland Governorate.
- Portrait source: [Latvian Wikipedia `File:Ēvalds Rimbenieks.png`](https://lv.wikipedia.org/wiki/Att%C4%93ls:%C4%92valds_Rimbenieks.png), an archival scan credited to *Nedēļa* no. 22 (29 May 1925), `382x480` PNG.
- Rights metadata: the file page explicitly marks the image as copyrighted and available only under Latvian Wikipedia fair-use conditions. It is not a rights-clear runtime source. The separate Commons monument photograph is CC BY 3.0 but is a statue/monument and cannot serve as a personal identity master.
- Verdict: identity **PASS**; 1936 role fit **PASS**; source/date **PASS**; rights **HOLD/BLOCKED**. Do not download into the portrait shelf, crop, repaint, or wire.
- Next step: locate a rights-clear original photograph or a documented public-domain archive scan of Rimbenieks. If none can be found, keep the institutional baseline without a personal portrait and report the portrait gate blocked.

### 3. Teodors Breikšs — identity PASS, source/date provenance HOLD

- Identity and role: [`Teodors Breikšs`](https://lv.wikipedia.org/wiki/Teodors_Breik%C5%A1s) identifies him as the first Latvian Liepāja city head, serving 1914–1915, with long municipal, education, and civic work in Liepāja.
- Source: [Commons `File:Teodors Breikšs.jpg`](https://commons.wikimedia.org/wiki/File:Teodors_Breik%C5%A1s.jpg), direct original URL `https://upload.wikimedia.org/wikipedia/commons/a/ad/Teodors_Breik%C5%A1s.jpg`.
- Commons metadata: description “Former mayor of Liepāja”; uploader `Binsalminsh`; license CC BY-SA 4.0; upload date 2022-02-11; no depicted-image date or underlying source supplied; original `300x383` JPEG.
- Research copy: SHA-256 `1EDDF9A79212BA494F7D566D9C982EC10C602E5CAB2FF43AE6B64A8F3E7B9262`, 24,174 bytes, decoded `300x383`.
- Visual review: clean oval archival portrait of a bearded man in civic dress; head and shoulders are isolated and readable, but the underlying publication/archive and date are undocumented.
- Verdict: identity **PASS**; visual framing **PASS candidate**; license **CONDITIONAL PASS** (CC BY-SA 4.0 applies to the Commons file); source/date provenance **HOLD**. The unknown source chain prevents immediate runtime promotion.
- Next step: recover the original publication/archive and depicted date, then perform independent identity/provenance review. If the source chain remains undocumented, keep as rejected research evidence rather than a runtime portrait.

### 4. Kristians Heinrihs Cinks — identity PASS, source/date provenance HOLD

- Identity and role: the municipal-history list records Cinks as Liepāja city head in 1902–1906 and again in 1908–1910.
- Source: [Commons `File:Kristians Cinks.jpg`](https://commons.wikimedia.org/wiki/File:Kristians_Cinks.jpg), direct original URL `https://upload.wikimedia.org/wikipedia/commons/0/0c/Kristians_Cinks.jpg`.
- Commons metadata: description “Former mayor of Liepāja”; uploader `Binsalminsh`; license CC BY-SA 4.0; upload date 2022-02-10; no depicted-image date or underlying source supplied; original `294x389` JPEG.
- Research copy: SHA-256 `3ED0E9865172B2C5E1A704490C6076110C2C9B14D660E37EADA7443E534F910B`, 25,071 bytes, decoded `294x389`.
- Visual review: clean oval archival portrait, centered head and shoulders, no modern artifacts.
- Verdict: identity **PASS**; visual framing **PASS candidate**; license **CONDITIONAL PASS**; source/date provenance **HOLD**. It is an early-20th-century institutional predecessor, not a direct 1936 officeholder.
- Next step: only pursue after Lapa/Rimbenieks source searches fail and the underlying archival source can be identified.

### 5. Additional Liepāja municipal names — research leads only

The same municipal list identifies Alberts Volgemūts (1910–1914), Viljams Dreiersdorfs (1906–1908), Kārlis Gotlībs Ūlihs (1878–1880), and Ādolfs fon Bagehūvuds (1882–1886). Commons search returns small CC BY-SA 4.0 files for Volgemūts, Dreiersdorfs, Ūlihs, and Bagehūvuds, each uploaded by `Binsalminsh` in February 2022 with no underlying source/date metadata. They remain **HOLD** for source-chain and date evidence and are weaker than Lapa or the active-1936 Rimbenieks lead.

## Authentic institutional-material fallback

The municipal-history list and Liepāja civic/education history provide defensible institutional identity evidence, but a text list or city monument is not a portrait source. No rights-clear 1934–1936 Liepāja council group photograph with named sitters was found in this bounded sweep. Do not substitute a monument, illustration, generic Latvian leader, or generated officeholder.

## Final disposition and parent handoff

Recommended path is **Lapa source-placeholder research PASS / runtime HOLD pending explicit crop and independent rights review**. Rimbenieks is the best 1936 identity lead but is **rights-blocked** by a fair-use-only scan. Breikšs and Cinks are visually usable archival leads with CC BY-SA file licenses but **source/date provenance HOLD**. The Courland package must remain portrait-blocked until the parent accepts one of these evidence states and the portrait worker completes the unchanged-source archive contract. No RunPod or ImageGen action was taken, and no runtime asset was generated or installed.

