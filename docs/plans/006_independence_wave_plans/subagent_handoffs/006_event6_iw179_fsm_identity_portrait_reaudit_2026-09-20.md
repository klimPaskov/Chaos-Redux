# IW-179 FSM identity and portrait source re-audit handoff — 2026-09-20

Status: **blocked; source fail-closed; parent review required**.

This bounded re-audit covers only IW-179, the FSM tag, and Event 006 Independence Wave.

The accepted package contract requires an adult male Micronesian, Pohnpeian, or Carolinian identity with a defensible governing role in 1936, an attributable high-resolution source, explicit derivative or redistribution permission, and independent portrait suitability.

No researched candidate closes every gate.

## Runtime consumer baseline

- Character consumer: `FSM_independence_wave_inter_island_congress_chair` in `common/characters/006_independence_wave_characters_registry.txt`.
- Portrait key: `GFX_portrait_FSM_independence_wave_inter_island_congress_chair` in `interface/006_independence_wave_small_assets.gfx`.
- Existing runtime file: `gfx/leaders/006_independence_wave/portrait_FSM_independence_wave_inter_island_congress_chair.dds`.
- Existing DDS bytes: 131,168.
- Existing DDS SHA-256: `64DB23C13F8F3F488079EA24CA4D8EF9326BBB3FD9ABBC94EE9B9251B004AE29`.
- Existing DDS decoded dimensions: 156x210, with opaque alpha.
- The existing runtime portrait is the previously withdrawn fictional evidence and was not treated as a candidate source, replacement, or approval.
- The installed vanilla leader references and the offline portrait-modding reference confirm the standard 156x210 leader canvas and full leader framing.

## Candidate gate results

### King John Sigra, Na II, traditional chief of Kosrae

Identity and a bounded 1936 governing-role continuity are supported by the Rulers.org chronology, which lists Na II “King John” as Kosrae’s ruler from 1910 to 1946, born in 1875 and deceased in 1957.

Sources: [Rulers.org Micronesian traditional rulers](https://rulers.org/micrtrad.html), [Micronesian Seminar record](https://micsem.org/librarysearchphoto/king-john-sigra-chief-of-kosrae-stands-in-front-of-the-church/), and the [indexed collection result](https://micsem.org/search-photos-results/page/82/).

The Micronesian Seminar record identifies “King John Sigra, Chief of Kosrae stands in front of the church,” with a collection record indexed as 1936 `[BM01009]`, while the item page exposes a conflicting 1953 date; the date requires confirmation before use.

The collection record is marked `Restricted`, no full-resolution bytes were exposed, and the Micronesian Seminar footer states `© 2010-2019 all rights reserved`.

Gate result: identity pass; bounded role/date pass with a date conflict; source-byte, derivative-rights, and redistribution-rights fail; independent portrait review not run.

No dimensions or hash are recorded because no lawful full-resolution source bytes were retrieved.

### Petrus Mailo

Prior repository research records Petrus Mailo as a named Micronesian and Chuukese chief or political figure, with Secretary of Moen in 1932, Chief of Nepukos in 1933, and Leader of Section No. 2 Moen from 1936 to 1938.

The attributable University of Hawaiʻi item is [Petrus Mailo, N-001-304](https://digital.library.manoa.hawaii.edu/items/show/22714), with its [IIIF manifest](https://digital.library.manoa.hawaii.edu/iiif/22714/manifest) and [retrieved image service](https://digital.library.manoa.hawaii.edu/iiif-img/24839/full/465%2C456/0/default.jpg).

The item is credited to the Department of Public Affairs, Public Information Office, in the Trust Territory Archives Photograph Collection, circa 1958–1975, so it does not provide a 1936-compatible portrait record.

The directly retrieved image was 465x456 JPEG, 8,959 bytes, SHA-256 `21252AB881DCEFC88CCD558F3BB2F3913B97C924C3392AEA992C1F79A3B0C8C4`.

The related [1921 reel index](https://libweb.hawaii.edu/digicoll/ttp/ttp_htms/1921.html) exposes [192109.jpg](https://libweb.hawaii.edu/digicoll/ttp/ttp_jpg/192109.jpg) at 333x471, 14,950 bytes, SHA-256 `B4E77A5FD38EDB780C492CB5D60B62D75A0C42E7FE9CB25827972A860BF2670B`, and [192110.jpg](https://libweb.hawaii.edu/digicoll/ttp/ttp_jpg/192110.jpg) at 638x437, 17,673 bytes, SHA-256 `52DE4C27AACC9931BD1DC0CC9ADF6245B7C5F4CD83AC53A3E15E9F0AEB33E838`; the reel material is labelled 1965–1975 in the prior source audit and is not a 1936 portrait source.

The [University of Hawaiʻi copyright policy](https://manoa.hawaii.edu/library/research/scholarly-communication/repositories/policies-guidelines/copyright-policy/) permits research, education, and private study, warns that other uses require consultation and consent of the copyright holders, and does not grant derivative or mod redistribution permission.

Gate result: identity and 1936 role continuity pass on prior role evidence; contemporaneous portrait-source fail; explicit derivative/redistribution-rights fail; independent portrait review not run.

### Moses Hadley, Nanmwarki of Madolenihmw

Rulers.org lists Moses Hadley as Nanmwarki of Madolenihmw from 1931 to 1966, born in 1894, giving a defensible 1936 governing role.

The attributable University of Hawaiʻi item is [1976 UN Day celebration, item 18073](https://digital.library.manoa.hawaii.edu/items/show/18073), with its [IIIF manifest](https://digital.library.manoa.hawaii.edu/iiif/18073/manifest) and [retrieved image service](https://digital.library.manoa.hawaii.edu/iiif-img/20227/full/635%2C472/0/default.jpg).

The image is a named group scene credited to the Department of Public Affairs, Publication Division, in the Trust Territory Archives Photograph Collection, and the item metadata places the collection circa 1958–1975 even though the event title is 1976.

The directly retrieved image was 635x472 JPEG, 37,980 bytes, SHA-256 `5C03E2D38B106E9BB11F63B4AE7C60875F5BDAD4AA9F21EFAA33C60FEDAE6`.

The UHM copyright policy provides no mod redistribution or derivative grant for this item.

Gate result: identity and 1936 role pass; post-1936 group-scene suitability fail; explicit derivative/redistribution-rights fail; independent portrait review not run.

### Other Pohnpeian traditional rulers surfaced by the chronology

Rulers.org lists Kalio Artui as Sokehs ruler from 1934 to 1972, born in 1908; Sigismundo as Kitti ruler through 1946; Saturlino as Nett ruler through 1946; Joel as Mwoakilloa ruler from 1904 to 1941; and Deved as Kapingamarangi ruler from 1929 to 1949.

Bounded searches of the public chronology, Bing results, Micronesian Seminar indexing, and Wikimedia Commons did not produce an attributable, rights-cleared, independently usable portrait source for these names.

Gate result: role/date leads exist for some names, but source bytes, explicit derivative/redistribution rights, and independent suitability remain unresolved; none may be promoted or genericized.

### Henry Nanpei

Henry Nanpei is a named Pohnpeian political and religious figure with an era-relevant Micronesian Seminar catalog lead.

The [PN01036 search record](https://micsem.org/library/search-photos-results?region=Pohnpei&subject=Henry%20Nanpei) identifies a circa-1920 black-and-white photograph but served only the no-image placeholder.

The [HF01005 search record](https://micsem.org/library/search-photos-results?region=Pohnpei&eras=japanese&subject=Nanpei) identifies “Portrait of Henry Nanpei,” catalogued 1933, and marks it `Not Restricted`, but only the 120x168 thumbnail was available at `https://micsem.org/library_img/photo/thumbnails/hf/01/hf_01_005_tmb.jpg`, SHA-256 `9f3e4ee25e6294dea68cb042593a257bdcf71d195dbf5ff979e33036f92861bc`.

`Not Restricted` is not an explicit public-domain, Creative Commons, derivative, or redistribution license, and the site footer states all rights reserved.

Gate result: named era lead pass; full-resolution source fail; explicit derivative/redistribution-rights fail; exact 1936 governing-role evidence remains incomplete; independent review not run.

### Nanaua

The [Internet Archive scan](https://archive.org/details/cu31924023239506) and [Commons file record](https://commons.wikimedia.org/wiki/File:The_Caroline_Islands;_travel_in_the_sea_of_the_little_lands_(IA_cu31924023239506).pdf) provide a rights-positive, attributable source for Nanaua, identified in the 1899 Frederick William Christian travel account as a nephew of King Rocha of Kiti.

The directly retrieved scan page was 1475x2439 JPEG, 528,174 bytes, SHA-256 `DD8AB34AC6D8AC90D31FE9E3E512CE7482D3D2D442B9117E490170FD6DAE6788`.

The Commons record identifies Christian, Frederick William, 1867–, marks the work `PD-old-100-expired` and `CC-PD-Mark`, and reports public-domain status with no attribution requirement.

Nanaua is not documented as a 1936 governing office-holder, and the 1899 relationship description does not satisfy the accepted governing-role continuity gate.

Gate result: source attribution, dimensions, and rights pass; 1936 governing-role and continuity fail; no crop or derivative was created.

### Previously rejected regional alternatives

- Tem Ibedul has a prior role chronology as a Palauan high chief through 1943, but no attributable, rights-cleared, independently usable full-resolution portrait was found; the regional and source gates remain unresolved.
- Kabua Kabua is Marshallese rather than a Pohnpeian or Carolinian identity, and the prior Micronesian Seminar lead was a 120x91 four-person thumbnail with no explicit redistribution license; it fails regional fit, independent suitability, and rights.
- Erhart Aten, John Mangefel, Andon Amaraich, and Bethwel Henry were born in 1932–1934 in the prior candidate review and therefore fail the adult-in-1936 gate.
- Unnamed period group photographs and generic “native” portraits fail the named-identity gate and cannot be substituted for FSM’s accepted contract.

## Rights and source-gate conclusion

The strongest role leads are King John Sigra, Petrus Mailo, Moses Hadley, Henry Nanpei, and the Pohnpeian ruler names in the chronology.

The strongest rights-positive image is the 1899 Nanaua scan, but it fails the 1936 governing-role gate.

The strongest 1936-role candidates with attributable images are blocked by restricted or non-licensing collection terms, postwar or post-1936 imagery, incomplete source access, group composition, or insufficient resolution.

No candidate is eligible for a source placeholder, user-supplied HOI4-style replacement, styled final, or runtime installation.

The exact missing clearance for a viable candidate is a named adult male with documented 1936 governing continuity plus a retrievable high-resolution portrait and written or explicit permission covering unchanged crop/resize, derivative processing, mod redistribution, attribution, and any required edit notice.

For King John Sigra specifically, parent review would need confirmation from the holding institution of the 1936 versus 1953 date and written permission from the Micronesian Seminar or Bishop Museum covering those uses before any source bytes are archived.

## Processing, wiring, and replacement state

- No source bytes were archived under `docs/assets/portraits/006_independence_wave/` because no candidate cleared all gates.
- No crop JSON, 156x210 PNG, runtime DDS, contact sheet, or portrait manifest was created or changed.
- `convert_to_dds.py` was not run because there is no approved source input.
- No portrait-specific `.gfx`, character, localisation, gameplay, country, central-attestation, allocator, or package-promotion file was changed.
- No ImageGen was used because FSM requires a grounded real identity and no fictional fallback is permitted.
- RunPod was not opened, operated, configured, queued, or monitored.
- Replacement state remains blocked and fail-closed; `independence_wave_fsm_sourced_identity_ready` remains unset.

## Evidence and checks intentionally skipped

Crop/framing review, source-to-crop equality, PNG processing, DDS conversion, independent visual review, runtime portrait inspection, and user-supplied RunPod replacement validation were intentionally skipped because the identity, rights, and/or source-availability gates failed first.

The required offline repository guidance was consulted before this handoff, including `AGENTS.md`, the offline Portrait Modding page and core wiki pages, the installed vanilla documentation, the Chaos Redux event-assets skill, its portrait-production reference, and the installed vanilla leader portrait references.

## Changed files

Only this dated handoff was added.

This is an incomplete, blocked handoff with no completion claim and no authorization request to substitute, genericize, generate, wire, or promote a portrait.
