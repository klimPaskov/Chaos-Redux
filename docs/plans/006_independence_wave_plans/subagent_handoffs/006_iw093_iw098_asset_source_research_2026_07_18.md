# Event 006 IW-093 Asante / IW-098 Sokoto asset-source research handoff

**Date:** 2026-07-18
**Scope:** sourced visual research only for the Asante (`DOX`) and Sokoto (`SOK`) package rows.
**Skill used:** `chaos-redux-event-assets` (source mode, historical flags, real-person portrait provenance, vanilla-reference compatibility).
**Status:** source packet delivered; no final art, DDS, `.gfx`, gameplay, localisation, or advisor outputs were created.

## Outcome at a glance

* **IW-093 / Asante:** Nana Otumfuo Agyeman Prempeh II has a period-matched, attribution-clear portrait candidate from the UK National Archives.  The 1935 Asante palette is well supported as gold/black/green, and the Busumuru Cap is documented as a crest, but I did **not** verify an authoritative primary description or scan establishing the exact 1935 flag stripe order, dimensions, or fimbriation.  A generated flat civic flag may be historically grounded, but it must not be labelled an exact attested 1935 flag without a primary flag source.
* **IW-098 / Sokoto:** Sultan Hasan dan Mu’azu Ahmadu is the correct opening-era Sultan (1930–1938), but the strongest archive image found has his face covered by a veil/scarf, so a recognizable real-person portrait is not currently cleared.  Sir Siddiq Abubakar III is a valid successor only from 17 June 1938; the available 1959 Smithsonian image has reuse restrictions.  No authoritative 1936 Sokoto civic/Caliphate flag specification was found.  The commonly reproduced “Flag of the Sokoto Caliphate” is explicitly self-made and unconfirmed and is excluded.
* **Vanilla compatibility:** vanilla has no Asante/DOX base flag family and no real Prempeh/Hasan/Siddiq portrait.  Vanilla has only ideological `SOK_communism`, `SOK_democratic`, `SOK_fascism`, and `SOK_neutrality` flag triplets; these are not a period-specific neutral/civic baseline and must not be treated as the requested historical flag.

## Source ledger

Confidence refers to the historical/provenance claim, not to final visual approval.  “Research-only” means the source may be cited for design direction but the image/object itself was not copied into the mod.

| Package / asset | Proposed identity or use | Source and provenance | Date / era fit | Rights / reuse status | Confidence and production disposition |
|---|---|---|---|---|---|
| IW-093 flag palette | Gold, black, green state colours | Helena R. Asamoah-Hassan, KNUST thesis, `https://dspace.knust.edu.gh/bitstream/123456789/4693/1/Helena%20R.%20Asamoah-Hassan.pdf`; text reports the restored Asante flag colours and attributes the Busumuru Cap crest to Manhyia Palace | Restoration context, 1935; later thesis records the colours | Thesis/figure is research evidence; no permission to copy the figure or any modern rendering was established | **High for palette; medium for crest attribution.** Use as constrained design evidence only. Exact band order, proportions, and fimbriation remain unverified.
| IW-093 flag / restoration context | Asante Confederacy restoration, Prempeh II, National Stool and court ceremony | University of Ghana repository, *A Full and Illustrated Report of the Proceedings of the Restoration of the Ashanti Confederacy*, Isaac T. A. Wallace-Johnson, The West African Sentinel, 31 Jan–4 Feb 1935: item `https://ugspace.ug.edu.gh/items/3a6e427d-3e8d-45ba-9a2f-bb0eca8b478a`; PDF `https://ugspace.ug.edu.gh/server/api/core/bitstreams/2141daaf-b7ac-454c-8306-9bb400a21db5/content` | Exact requested period; compiled through courtesy of Prempeh II | Repository scan is a historical source, not a cleared image license | **High for period/institutional context.** The pass did not locate a reliably citable flag plate or exact geometry. Do not claim this report proves a particular stripe layout.
| IW-093 symbol ownership | Golden Stool / Asante court regalia, political and spiritual sovereignty | Metropolitan Museum, “Gold in Asante Courtly Arts,” `https://www.metmuseum.org/de/essays/gold-in-asante-courtly-arts`; British Museum, “Asante gold regalia,” `https://www.britishmuseum.org/about-us/british-museum-story/contested-objects-collection/asante-gold-regalia` | Long-lived Asante institution; directly relevant to a 1935 restoration route | Museum pages provide context, not permission to copy object photography or sacred regalia designs | **High for ownership/context.** Treat a stool/regalia mark as culturally sensitive, restrained, and route-attributed; never use as decorative clip art.
| IW-093 later motif lead | Forest/cocoa/porcupine (Kotoko) nationalist motifs | “The Youngmen and the Porcupine,” `https://docslib.org/doc/5751783/the-youngmen-and-the-porcupine-class-nationalism-and-asantes`; article synthesizes later Asante nationalism and describes green forest, gold resources, black ancestral stools, cocoa imagery, and the porcupine | Later nationalist context, not proof of the exact 1935 restoration flag | Research-only article; no image reuse implied | **Medium and date-limited.** May inform a separate civic/labour route only after identity review; do not present cocoa/porcupine geometry as the 1935 flag.
| IW-093 leader portrait | Nana Otumfuo Agyeman Prempeh II, installed Asantehene in 1935 | National Archives UK / Africa Through a Lens, catalogue CO 1069/44, 31 Jan 1935: `https://www.flickr.com/photos/nationalarchives/5416372614`; Commons record `https://commons.wikimedia.org/wiki/File:Nana_Otumfuo_Agyeman_Prempeh_II.jpg`; related OGL record `https://commons.wikimedia.org/wiki/File:The_National_Archives_UK_-_CO_1069-44-13.jpg` | Exact period: restoration day, 31 Jan 1935 | National Archives material is released under the Open Government Licence v1.0 where the record states it; preserve TNA catalogue/attribution. Licence text: `https://www.nationalarchives.gov.uk/doc/open-government-licence/version/1/` | **High historical and provenance confidence; portrait crop feasible.** Male, face/eyes/hair and shoulders are visible in the archival portrait. Future processing must use the original source, an explicit head-and-shoulders crop, identity-preserving HOI4 painted treatment, and the required 156×210 output. No processed portrait was made in this pass.
| IW-093 conditional portrait reference | Prempeh II in Asante war costume | British Museum object record/image, 2 Mar 1936, photograph by Mary S. R. Sinclair: `https://www.britishmuseum.org/collection/image/47975004`; collection context `https://www.britishmuseum.org/collection/term/AUTH240832` | 2 Mar 1936; visually close to opening period | Non-commercial CC BY-NC-SA 4.0 museum image terms; not cleared for unrestricted mod redistribution | **High identity/era, restricted reuse.** Keep as a visual cross-check only unless the project accepts the museum’s non-commercial terms and records them. The National Archives candidate is the preferred source.
| IW-098 institutional motif | Sokoto successor sultanate, emirate federation, Islamic court/legal and educational institutions, Hausa civic/commercial and Fulani dynastic identities | Library of Congress, *Nigeria: a country study*, Federal Research Division, text `https://tile.loc.gov/storage-services/master/frd/frdcstdy/ni/nigeriacountryst00metz_0/nigeriacountryst00metz_0_djvu.txt`; National Library of Nigeria *Studies in the history of the Sokoto caliphate*, `https://nigeriareposit.nln.gov.ng/items/d0ff7cd7-3a7b-41e5-973b-d644b7a47b2b`; official history lead `https://sokotostate.gov.ng/history-of-sokoto/religion/` | Caliphate founded 1804; 1936 route is a successor sultanate/native-administration setting, not an unqualified restoration of the independent caliphate | Institutional research pages; use as historical context, not as image licences | **High for institutional direction; no exact flag geometry.** A generated flag should use restrained civic/federal geometry and keep Hausa/Fulani and Islamic/legal motifs distinct. Do not invent a sacred inscription.
| IW-098 flag candidate (excluded) | “Flag of the Sokoto Caliphate” reconstruction | Commons `https://commons.wikimedia.org/wiki/File:Flag_of_the_Sokoto_Caliphate.svg` | Uploaded 21 May 2008; not a period source | File is marked own work/public domain by uploader, but the page expressly says the insignia is unconfirmed because the source is missing | **Rejected.** This is not evidence of a 1936 flag and must not be copied or cited as historical geometry.
| IW-098 leader portrait | Sultan Hasan dan Mu’azu Ahmadu, Sultan 1930–1938 | E. H. Duckworth Photograph Collection, Northwestern University Digital Collections, `https://dc.library.northwestern.edu/items/ac89793d-6016-42b0-8f66-ac86cf7bd51f`; Commons record `https://commons.wikimedia.org/wiki/File:Sultan_Hasan_dan_Muazu_(cropped).jpg` | Correct opening-era ruler; archive capture date is not stated, generally 1930s | Commons states a Nigerian photographic-work public-domain rationale; retain Northwestern / E. H. Duckworth credit. The underlying archive/term interpretation should still be recorded in the final manifest | **High historical/provenance, low portrait feasibility.** The high-resolution image has Hasan’s face substantially obscured by a white veil/scarf. A head-and-shoulders crop would not provide a dependable recognizable face. Mark `needs_user_review`; seek a face-visible 1930s archive photo or explicit archive guidance before any portrait processing. No final portrait was made.
| IW-098 conditional leader portrait | Hasan dan Mu’azu in the 1934 London group photograph | Commons `https://commons.wikimedia.org/wiki/File:The_sultan_of_Sokoto_and_the_emirs_of_Gwandu_and_Kano_at_the_London_Zoological_Gardens_with_Frederick_Lugard.png`; source caption cites a Guardian reproduction / Ochonu (2022) | June 1934; correct pre-opening period | Commons PD claim conflicts with the 1934 date and unclear photographer/source provenance; do not treat as cleared | **Conditional only; not production-ready.** The annotated Hasan face is visible but small in a group composition. Rights/date conflict and crop quality require independent review. Do not process without written resolution.
| IW-098 successor portrait | Sir Siddiq Abubakar III, Sarkin Musulmi from 17 Jun 1938 | Commons `https://commons.wikimedia.org/wiki/File:Sir_Siddiq_Abubakar_III,_Sarkin_Musulmi.jpg`; Smithsonian/Eliot Elisofon rights lead `https://www.si.edu/object/archives/sova-eepa-1973-001` | 1959 image; valid only for the post-17 Jun 1938 branch, not the 1936 opening | Commons Nigerian-PD claim is contradicted by the Smithsonian/Elisofon metadata warning and permission requirement; request written Smithsonian clearance before reuse | **Blocked.** Date-gated and rights-conflicted. Do not use for the opening Sultan or copy into the mod absent permission.
| IW-098 alternative person (not a portrait clearance) | Ahmadu Bello as a later/district-level civic figure, not Sultan | Package research specification identifies him as a possible district/council figure, not the 1936 Sultan. No rights-cleared, period-matched portrait was established in this pass | 1934 district-head context can fit a secondary role; no image clearance | No source/licence packet completed | **Research lead only.** Do not substitute Bello for Hasan as Sultan and do not create a generic portrait in his place.

## Flag geometry and visual-design handoff

### IW-093 Asante / `DOX`

1. The safe historical constraints are the gold/black/green palette, the 1935 restoration context, and Asante court/state ownership of stool/regalia symbolism. The KNUST thesis also names the Busumuru Cap as a crest, but it does not establish an exact stripe order, band height, or border treatment in text.
2. A final route flag may therefore be a **generated, flat, orthographic civic design** constrained by these sources. It must be documented as “historically grounded generated design” unless a primary 1935 flag plate or description is recovered.
3. If the route uses the Golden Stool or a related court mark, simplify it as an intentional civic seal and record the sensitivity note; do not trace a museum photograph or present a sacred object as generic decoration.
4. Keep a traditional/royal Asante route visually distinct from constitutional, labour, federal, or military routes. Later cocoa/porcupine imagery is not a substitute for a 1935 attested flag.
5. If the parent requires an exact historical flag rather than a grounded generated design, the asset is **blocked pending primary evidence** from the 1935 University of Ghana report or Manhyia Archives. Manhyia archive leads: Prempeh II private secretary records, `https://www.manhyiaarchives.org/records/mag2`; Kumase Traditional Council records, `https://mail.manhyiaarchives.org/records/mag1`.

### IW-098 Sokoto / `SOK`

1. No authoritative 1936 neutral/civic flag was identified. The unconfirmed Commons reconstruction is explicitly excluded. Do not backdate the modern Sokoto State flag, use generic black jihad banners, or add unverified Arabic/Islamic text.
2. A generated flat design should communicate the successor sultanate/emirate federation, Islamic legal/educational court, Hausa civic/commercial life, and Fulani dynastic/native-administration structure without collapsing those identities into one generic “Islamic” symbol.
3. Treat the flag as a historically grounded generated identity, not an attested flag, unless a primary archival description is found. Preserve a distinct design for the civic/federal route and any later successor route.

### Required future runtime outputs

The parent implementation/art agent owns final generation and wiring. When approved, flags must be orthographic and flat at the skill’s standard sizes: normal `82×52`, medium `41×26`, and small `10×7`, then converted to TGA with the repository converter and bottom-left origin. Do not reuse the vanilla SOK ideology triplets as a neutral historical substitute.

## Portrait handoff and blockers

### Prempeh II (preferred IW-093 leader)

* Use the National Archives UK CO 1069/44 source as the preferred candidate. It is male, dated 31 Jan 1935, and has a readable face with shoulders and period Asante cloth/regalia.
* The future crop should be an explicit head-and-shoulders crop from the original archive image; keep the face, eyes, hair, age, and clothing identity. Do not include a generic body or replace the face with a generated likeness.
* Future final master target: full `156×210` leader/commander portrait, with source URL, archive, OGL terms, crop box, processor metadata, and review evidence in the asset manifest. This handoff does not approve a final portrait.

### Hasan dan Mu’azu (opening IW-098 Sultan)

* Historical identity is correct, and the Northwestern/Duckworth source is the strongest provenance lead, but the face is obscured. The source is therefore `needs_user_review`, not cleared for portrait production.
* The 1934 London group photograph is only a conditional lead: the subject is small and the Commons PD assertion conflicts with the 1934 date and unclear photographer/source chain.
* Do not replace Hasan with a generic Africa portrait or with Siddiq. Seek a face-visible, permission-clear archival image before processing.

### Siddiq Abubakar III (post-17 Jun 1938 branch only)

* The 1959 Smithsonian/Eliot Elisofon portrait is chronologically usable only after the succession date, but it is rights-blocked. It cannot be copied into the mod without written permission and a manifest-linked rights record.

## Vanilla and current-mod compatibility findings

* Canonical vanilla references under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/` include generic Africa leader/commander portraits at `156×210`, but no identity portrait for Prempeh II, Hasan, or Siddiq. A generic reference is not an acceptable real-person substitute.
* Vanilla Hearts of Iron IV contains `SOK_communism`, `SOK_democratic`, `SOK_fascism`, and `SOK_neutrality` flag families in normal/medium/small sizes, but no unsuffixed `SOK.tga` baseline. These are ideological assets and have no evidence of representing a 1936 Sokoto civic flag.
* No vanilla `DOX`, `GHA`, or Asante-specific flag family was found, and the current mod has no `DOX.tga`/`SOK.tga` route-specific base family or relevant identity portrait. The parent owns any new filenames and `.gfx` wiring; this source pass intentionally did not edit them.

## Sensitivity and exclusion notes

* Asante Golden Stool and royal regalia are political, cultural, and spiritual institutions. British Museum documentation also describes contested/looted regalia histories. Do not use museum object photographs as unlicensed textures or reduce a sacred institution to decorative clip art.
* Asante route material should acknowledge the restoration/colonial context rather than imply that a later modern civic flag is automatically the 1935 flag.
* Sokoto’s 1936 setting is a successor sultanate under colonial/native administration; avoid anachronistically describing it as an independent 1804–1903 Caliphate restoration.
* Keep Hausa civic/commercial and Fulani dynastic identities distinct. Do not use generic jihad banners, unverified calligraphy, or modern Sokoto State symbols.
* `SOK` Hasan source, 1934 London group source, Siddiq source, and any exact Asante flag geometry remain `needs_user_review`/blocked as described above. No fallback identity or fabricated historical claim was used.

## Files and retention

* Created: this markdown handoff/source ledger only.
* No source image, processed PNG, DDS, contact sheet, manifest JSON, or `.gfx` file was added to the repository.
* Three images were downloaded only to an OS temporary folder for visual inspection (`prempeh.jpg`, `hasan.jpg`, `hasan_london_group.png`); they are not runtime inputs and should not be treated as committed source assets. No source download is retained in the mod package.

## Completion statement

The requested source research is complete for the currently available evidence. Prempeh II is the only portrait candidate that is both period-matched and sufficiently rights-clear for a future processing pass. Hasan likeness, Siddiq rights/date, exact Asante 1935 flag geometry, and exact Sokoto 1936 flag geometry remain explicit blockers. No simplification or fallback was silently substituted.
