# Event 006 signature portrait source follow-up

Date: 2026-10-06.

Disposition: `blocked` for the two new signature portraits and for fresh-source repair of the Gayaz Ishaki and Shaban Polluzha quality findings; `pending` for parent review of period/age fit if a source becomes retrievable. No runtime portrait, `.gfx`, character reference, or source raster was changed in this follow-up.

The source-mode gate remains unchanged. These are grounded real people. No real-person ImageGen, repaint, generic face, fictional substitute, RunPod operation, or reuse of a mismatched generic portrait was performed. An admitted grounded image remains `source_placeholder` until the user supplies a matching HOI4-style final.

## Files created

- `docs/assets/portraits/006_independence_wave/signature_people_20261006/manifest.md` records candidate identity, date, rights, retrieval, disposition, and planned runtime mappings.
- This handoff records the research trail, attempt outcomes, existing quality findings, and remaining inputs.

No original, lossless crop, crop JSON, 156×210 PNG, native-plus-4× contact sheet, DDS, or GFX file was created because no new portrait source bytes passed the required gates and retrieval attempts failed. No portrait-specific sprite or character wiring was added.

## DSX: Siyanbola Onikepe Ladigbolu I

The current source archive contains `docs/assets/portraits/012_africa/source_master_oyo_ladigbolu_i.jpg`, a 162×312 image whose caption identifies “Late Oba Siyanbola Ladigbolu (1911–1944).” A read-only byte comparison verified it is identical to Commons `File:Ladigbolu-1st photo.jpg`: 9,319 bytes, SHA-1 `31f216a690aece2e898819449ad129197c2a4d2d`; the local SHA-256 is `5d557fb79ea179370960f3f455aced41a9d13f322a8b1bfcf08cf5459cbaa4d7`. The Commons file page lists uploader `.PNG King`, a 22 May 2024 upload and CC BY-SA 4.0, but does not identify the original photographer, underlying photo source, or historical capture date. The reuse license on the uploader's copy does not establish rights in the underlying image, which is why prior IW-097 research held it.

A better identity lead is the Yoruba Cultural Heritage Centre's caption for the 1937 Conference of Yoruba Chiefs photograph. It explicitly identifies Siyanbola Ladigbolu I, seated between Daniel Adesanya and Adesoji Aderemi. The 1937 date and event are corroborated by the contemporary conference proceedings described in the historical record, but I found no primary archival catalog record or reuse license for the photograph itself. The post therefore confirms a source candidate and person position, not an image cleared for portrait use.

Relevant records: [Yoruba Cultural Heritage Centre's 1937 photograph caption](https://www.linkedin.com/posts/yoruba-cultural-heritage-centre_prominent-yoruba-obas-in-1937-in-1937-activity-7087363131026329600-Yz9B), [Commons `Ladigbolu-1st photo.jpg`](https://commons.wikimedia.org/wiki/File:Ladigbolu-1st_photo.jpg), and the current read-only source copy under the 012 archive. The linked group photo's source author and rights are not established, and its copy was not downloaded or cropped.

The generic 012 character `africa_priority_oyo_sovereign` and its user output remain untouched. That office portrait is not evidence that the image depicts Siyanbola Ladigbolu I. No new Event 006 consumer mapping is installed. The planned parent mapping is `GFX_portrait_independence_wave_oyo_ladigbolu_i` → `gfx/leaders/006_independence_wave/portrait_independence_wave_oyo_ladigbolu_i.dds`, registered in the new `interface/006_independence_wave_signature_portraits.gfx` only after source admission.

## ATJ: Teungku Muhammad Daud Beureueh

The accepted role scope is his education and ulama work; no PUSA organization or title belongs before its documented founding on 5 May 1939. The Indonesian Ministry of Education and Culture encyclopedia records that Daud formed Jamiah Diniyah and founded Madrasah Sa'adah Abadiah in 1930, and dates PUSA's foundation to 5 May 1939. This supports his pre-PUSA education identity without assigning him an anachronistic organization role.

The nearest exact-dated rights-cleared image found is [Commons `Tgk. Moch. Daoed Beureueh, Gubernur Aceh.jpg`](https://commons.wikimedia.org/wiki/File:Tgk._Moch._Daoed_Beureueh,_Gubernur_Aceh.jpg). Its record identifies a 328×422 image, dated 31 December 1947, credits the Province Government of Aceh, and links to the official Aceh SIKN archival record `AC05-1-1-18`. The Commons page asserts public-domain status under Article 43 of Indonesian Law 28/2014 for government works. This is a valid identity-and-rights candidate, but it is eleven years after the opening date and depicts his later governor period; Daud was about 48 at the image date and about 36–37 in 1936. No younger exact portrait with verified period, creator, and reusable rights was found.

The official source link, [Aceh archive record](https://acehprov.sikn.go.id/index.php/ac05-1-1-18-gubernur-militer-atjeh-langkat-dan-tanah-karo-1947-1950-gubernur-aceh-1950-1951-1), was requested with a bounded 20-second HEAD request and timed out. Wikimedia's original-file endpoint had already returned HTTP 429 for a separate source image during this work session, so I did not retry through another mirror or route. The file bytes, metadata archive, crop, processed PNG, and runtime DDS could not be produced. The older Commons `File:Teuku Daud Beureueh.jpg` is explicitly unknown-date and reproduced from a 1998–1999 Ministry of Defense book, so it was not selected as a 1936 portrait. Later group images of Daud with Acehnese ulama are copyrighted reproductions or lack original-photo rights records and remain research-only.

Relevant records: [official Indonesian culture encyclopedia entry](https://esi.kemenbud.go.id/wiki/Teungku_Muhammad_Daud_Beureueh), [Commons 1947 government portrait](https://commons.wikimedia.org/wiki/File:Tgk._Moch._Daoed_Beureueh,_Gubernur_Aceh.jpg), [primary Aceh SIKN record](https://acehprov.sikn.go.id/index.php/ac05-1-1-18-gubernur-militer-atjeh-langkat-dan-tanah-karo-1947-1950-gubernur-aceh-1950-1951-1), and [unknown-date Commons portrait](https://commons.wikimedia.org/wiki/File:Teuku_Daud_Beureueh.jpg). Planned parent mapping is `GFX_portrait_independence_wave_aceh_daud_beureueh` → `gfx/leaders/006_independence_wave/portrait_independence_wave_aceh_daud_beureueh.dds`, registered in `interface/006_independence_wave_signature_portraits.gfx` only after an admitted source is available.

No existing 006 manifest declares a matching user-supplied final for either new identity. I did not guess filenames in user-output folders. The current 012 Oyo user output is explicitly for the generic sovereign office and was neither reviewed as Ladigbolu nor reused.

## Existing quality findings revisited

### Gayaz Ishaki, CHU federal presidium

The installed 156×210 source placeholder remains the D13-accepted book plate from Ahmet Kanlidere, *Reform within Islam*, and the existing runtime DDS remains unchanged at SHA-256 `6c8b42368648d52196bdd27084435eaf024dfd14cc37fb97d88748e13559ebb4`. The file page for [the 1938 Warsaw crop](https://commons.wikimedia.org/wiki/File:Ayaz_Ishaki_1938_(cropped).jpg) identifies Ishaki with Said Shamil and Usman Khoja, dates the photo to 1938, attributes the image to Miras.Info, and records unknown photographer and a PD-Poland/US rationale. A local alternative, [the 1931 Jerusalem conference crop](https://commons.wikimedia.org/wiki/File:Ayaz_Ishaki,_Said_Shamil_and_Musa_Jarullah_Bigi_at_the_Islamic_Conference,_Jerusalem,_1931.jpg), names Ishaki on the left with two named companions, dates the image December 1931, and cites the Warsaw periodical *Gorcy Kavkaza / Les Montagnards du Caucase* (1931). The 1931 candidate is five years before the 1936 start and Commons marks it public domain in Poland and the United States, although the page still requests first-publication details from its uploader.

The Commons API returned the 1931 candidate's exact original URL, 1,886×1,919 dimensions, 1,910,689-byte size, and SHA-1 `bc1e00d486a22a938dd1fab9b3afa93f1835fe5a`. A single bounded request to that exact original URL returned HTTP 429. The Commons page records the Warsaw 1931 periodical as the source and PD-Poland/US status but also asks its uploader to provide first-publication details. The Miras.Info source page returned HTTP 403, and the 1938 Commons original had already returned HTTP 429 in the prior takeover handoff. No alternate mirror, proxy, cache, or repeated CDN request was used. I did not alter the existing CHU DDS before parent review. The 1931 photo remains a review candidate only; neither source has local bytes for crop/framing inspection. No source-only crop or contrast edit was applied to the blurry installed book plate.

### Shaban Polluzha, KOS

The existing exact individual source and runtime are unchanged; the source contract records source original SHA-256 `708e3af6b821d9a428fcfe5a9b92d871d055b61aeecbf7cebd132043e7dba39c`, processed 156×210 PNG SHA-256 `49b9664814481ad3107a7d6ea04ef29b57286c5f996e57f14d5a17b036aeba31`, and runtime DDS SHA-256 `9a880d5933d07090205ff42d0176681851ef051698b809351e0341a1750bcf1c`. The independent family-history account says Polluzha's one known portrait remained under a barn beam from 1945 to 1990 and was badly damaged by damp; it distinguishes this authentic family portrait from an unidentified armed fighter image circulated online. That reinforces the current identity selection but does not provide a cleaner source scan. The source remains overexposed and no contrast edit, fake-face repair, or unidentified group crop was made.

References: [Bajram Mjeku on the Polluzha portrait's family history and the false armed-fighter image](https://inforculture.info/2022/02/23/loja-me-portretin-e-shaban-polluzhes/), [the original-source discussion](https://inforculture.info/2020/07/18/kush-ishte-shaban-polluzha-2/), and [current Commons individual source page](https://commons.wikimedia.org/wiki/File:Shaban_Polluzha.jpg).

## Scope and remaining gates

The two new sprites and the sprite file do not exist in the current worktree. No character reference, role, history, event, or gameplay file was changed. The current DSX generic office portrait and the existing ATJ vanilla `INS_alauddin_syah` portrait remain untouched. The 12-portrait prior source audit and GFX keys remain intact.

No new native-plus-4× contact sheet was produced because no candidate source raster was retrievable and no runtime portrait changed. No converter or game process was used. No RunPod, ImageGen, desktop app, or HOI4 was opened. The user remains the only creator of any requested styled finals. Live portrait consumer validation remains with the user.

Before either new portrait can be installed, the parent must resolve the missing source gates: acquire an attributable rights-cleared Ladigbolu individual image, and decide whether a retrievable 1947 Daud portrait is acceptable for an 11-year-earlier education/ulama portrayal or require a genuinely closer-period source. Before modifying the old CHU DDS, the parent must review a local, rights-cleared source and approve its 1931 date/context; the old KOS DDS should remain unchanged unless a cleaner authenticated source scan is found.

No simplification or fallback art was used. The work is incomplete due to exact missing source bytes, unresolved source attribution/rights, and period mismatch as recorded above.

## Skills and tools

Used `chaos-redux-event-assets` portrait-production guidance and `chaos-redux-subagents` ownership guidance. Web research used Commons metadata/pages, the Aceh Ministry of Culture encyclopedia, the Yoruba Cultural Heritage Centre caption, and the Polluzha family-history article. No source asset binary was downloaded or generated in this follow-up.
