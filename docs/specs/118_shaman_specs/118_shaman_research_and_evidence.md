# Shaman research and evidence

This register separates complete reading of supplied project material, targeted repository investigation, cultural research and proposed game design.
Its status is a completed planning evidence record dated 23 October 2026.
Numerical game tuning in the specifications is proposed unless the text identifies an observed owner value.

## Supplied-source reading gate

The complete supplied-source gate passed before substantive specification writing.
The parent and three source readers processed every distinct supplied text or configuration file, including the current bundle, legacy bundle, standalone files and nested subagent archives.

| Coverage measure | Completed coverage |
| --- | ---: |
| Distinct text and configuration contents | 151 |
| Verified supplied and extracted paths | 193 |
| Unique source bytes | 3,209,743 |
| Archives inventoried and checked | 5 |
| Outstanding supplied-file reading gaps | 0 |

The evidence is in [118_shaman_source_review_evidence.json](../../plans/118_shaman_plans/imported_review/118_shaman_source_review_evidence.json).
It contains the full per-file hash, byte count, path list, reader, read method, coverage ranges, archive members and original reading receipts.
Its embedded evidence also retains the exact-span maps and independent coverage checks.

Reading was coordinated across the team.
Each unique file was fully processed by one or more readers.
Exact duplicate copies were verified by raw SHA-256 rather than redundantly reread.
Where two versions shared text, a gap-free exact equality map reused spans from an already completed reading, with every changed span separately read.
The independent coverage audit checked those dependencies, full range coverage, archive membership and the absence of circular reuse.
A summary, search result, file list or successful download did not count as a complete reading.
Output that was clipped during the required-source pass was recovered through bounded reads before the gate closed.

All 151 unique hashes and all 193 paths were checked again during final assembly.
This is a team-wide full-reading claim with disclosed exact-text reuse.
It is not a claim that the parent personally reread every duplicate byte, or that a single reader independently read all 193 copies.
The required project files were not shortened or skipped to accelerate the design.

The supplied skills were all processed, including families that do not create a surface in this event.
Their applicable rules informed scope, integration, art, costs, AI, timing, source ownership and delivery.
Reading a skill does not require adding an unrelated game system to Shaman.

## Version and authority decisions

| Source difference | Applied decision |
| --- | --- |
| Current modular bundle and older monolithic skills coexist | Current supplied `AGENTS.md`, current skill roots and current role exports govern where versions conflict. Legacy material remains reading evidence |
| Current `.claude/skills` and `assets/gfx_references` replace older paths | Implementation uses the current canonical paths and verifies actual consumers and reference families |
| Older instructions make unavailable MCP output an absolute blocker | Current bounded-retry and direct-source provisions govern. Unavailable checks limit the claim, while supported planning and source work continues |
| Current probability inspect/analyze schema differs from older separate tools | Use exposed live schemas and current documented analysis modes. The planning pass used exact local calculations because HOI4 tools were not exposed |
| Supplied role metadata names models and Windows environments | Roles were applied through self-contained available collaboration agents. Their metadata did not grant unavailable runtimes, model identities or installed files |
| Historical package evidence placed Shaman at 129 and locust at 118 | Parent-provided pre-migration snapshot also reports those identities, all four relevant records Unavailable, and no roots for the imported identities. The user has since approved adopting the uploaded identities and migrating the catalog; the parent owns that mutation in this turn. This review did not inspect the resulting workbook state |
| The imported package proposed To Be Reworked while the catalog record is Unavailable | The pre-migration catalog snapshot status was Unavailable. To Be Reworked is only a future proposal after an accepted migration and a corresponding root exists; Playable requires separate approval |
| Cluster IDs change between historical exports | Use current registry identities when implementing. No historical cluster number is inferred from a label |

The source readers also recorded conflicts within specialized 3D and character guidance.
Those conditional conflicts did not affect a selected Shaman surface and were not used to bypass current instructions.
Their original findings are preserved in the review evidence when relevant to later project work.

## Targeted repository investigation

The inspected repository was `klimPaskov/Chaos-Redux`, pinned to commit `41bc4e5045a7b5c131be69dda2f08079d478634c`.
[118_shaman_repository_evidence.json](118_shaman_repository_evidence.json) records exact file paths, revisions, fetched spans, actually read spans, source hashes and discovery-only reads.
A complete download is deliberately not labeled a complete reading unless the stated read span is full.

The important additional findings are these.

| Finding | Evidence and effect on the design |
| --- | --- |
| Event 013 publishes an official forecast on accepted disaster scheduling | The complete [Natural Disasters overview](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/docs/events/013_natural_disasters/overview.md) and targeted runtime bodies establish a known hazard, state, severity and date. True Sight adds a consequence hypothesis and preparation rather than presenting those public facts as secret information |
| The public disaster gateway creates danger | `call_natural_disaster` is an effectful scheduling API in the [013 owner](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/common/scripted_effects/013_natural_disasters_effects.txt). It cannot be used to observe a future event or make a prophecy true |
| A job snapshot is not future simulation | The inspected outcome-snapshot helper copies current or accumulated state. Its name does not authorize revealing future random results. New read-only risk and exact consequence contracts are specified explicitly |
| Disaster relief has real phased work | Inspected owner thresholds are rescue 3, stabilization 4 and reconstruction 5. The land rite's 3, 2 or 1 contribution is clamped through that owner. It does not set an unperformed evacuation or prevention flag |
| Famine uses real local food accounting | The [famine system](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/docs/systems/famine_system.md), API notes and targeted reserve bodies establish thousand-person-day units, reserve capacity, baseline initialization and actual addition. Shaman needs a new exact-source credit wrapper and a separate bounded spoilage adapter |
| A reserve grant is not an opened corridor | The famine relief-access API changes a route proof. A blessing cannot invoke it without a real route-opening fact |
| Broad hygiene is not local disease treatment | The inspected [shared outbreak measures](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/common/scripted_effects/biological_shared_outbreak_measure_effects.txt) are country policy. The [Black Plague action owner](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/common/scripted_effects/020_black_plague_shared_response_effects.txt) has an existing paid lifecycle. Neither is a generic free cure. Full acceptance requires an exact-outbreak assistance integration |
| Repair is a finite service | The [Event 012 industry contract](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/common/scripted_effects/012_africa_gods_industry_effects.md) provides a timed state-local repair precedent. It does not prove completed factory-days or make its private funding available to Shaman |
| Local military candidates exist, but installed semantics remain a gate | The [013 state modifier source](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/common/dynamic_modifiers/013_natural_disasters_state_modifiers.txt) uses local supply, controller movement and controller attrition. The offline reference identifies candidate state entrenchment and construction fields. The actual beneficiary and border behavior still need installed checks |
| The all-human modifier helper binds too broadly | The targeted [shared dynamic-effects body](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/common/scripted_effects/chaosx_dynamic_effects.txt) applies to every existing human country. Shaman requires one original-actor binding |
| Production commitment uses a factor | Event 013's paid decision precedent uses `consumer_goods_factor`. A factory-count gate is not a debit or fixed factory reservation. Costs therefore name the factor and duration honestly |
| Registration and catalog are separate | The targeted [logic registry](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/common/scripted_effects/chaosx_logic_effects.txt), event-directory metadata and `nr118` searches did not establish an existing Shaman root. [Spreadsheet authority](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/docs/spreadsheets/README.md) and the [shared reservation ledger](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/docs/specs/shared_identifier_registry.md) constrain the later migration |

The parent also inspected the opening of the Time Traveler design and the existing achievement framework as bounded precedents.
They informed uncertainty and integration questions without transferring their private mechanics into Shaman.
Exact read ranges appear in the JSON manifest.

## Geographic and visual evidence limits

The six selected regional profiles are grounded in the bibliography below, with source-specific qualifications in Part 4.
They are geographic design anchors, not certified installed state-ID mappings.
The inspected repository history tree did not include `history/states`.
A secondary Event 013 handoff mentions Jeju in state 1031, but no installed state file was read to certify that mapping.
The package deliberately does not guess the six final numeric footprints.

Contemporary cultural evidence can establish terminology, community roles, regional variation or a documented place.
It does not by itself establish a 1930s settlement layout, garment, transport item or historical person.
Period asset research remains assigned before production.
No cultural source certifies supernatural claims as real.
The game treats the visitor's powers as fictional uncertainty and uses the same hidden capability distribution across profiles.

The complete Yup'ik book was not accessible and was not read.
The Tày article was consulted at abstract and metadata level only because its full text did not load.
Some other papers were read in relevant accessible sections rather than cover to cover.
Those additional research limits are identified individually below.
They do not change the completed supplied-project-file gate.

## What was not executed

No installed Windows game documentation, native game map files, HOI4 MCP operation, rendered game consumer or live campaign was available or executed during this planning task.
No gameplay, catalog workbook, localisation or final art was implemented.
Source existence does not prove native runtime behavior.
The acceptance matrix describes required future evidence and is not a table of passed gameplay tests.

No source requirement was silently removed to obtain a quicker plan.
The current design retains the difficult natural-forecast and civilian-disease integrations as required work.
The finite roster, one rite, one value and three-vision cap are deliberate design bounds accepted after the improvement review, not substitutes for missing implementation.

## Cultural source register

The following entries preserve the exact consulted pages and their actual reading scope.
No video was watched and no archival image was downloaded or accepted as final art.
Source titles are bibliographic identifiers, not proposed localisation.

### B1. Olkhon fieldwork

Aleksandra Wierucka, **Modern forms of Buryat shaman activity on the Olkhon Island**, Anthropological Notebooks 19(3), 2013.
Source: [consulted page](https://anthropological-notebooks.zrc-sazu.si/Notebooks/article/view/214) Consulted PDF: [research paper](https://anthropological-notebooks.zrc-sazu.si/Notebooks/article/download/214/189/624) Primary basis: author's 2010 field research.
Read scope: abstract, introduction, regional context, and distinctions among local and organized forms in the consulted early PDF sections.
Used for the Olkhon anchor and diversity of contemporary practice.
Limit: later ritual detail was not fully read and the paper does not establish a complete game-period asset reference.

### B2. Buryat museum collections

Russian Museum of Ethnography, **Народы Великой степи: буряты, калмыки**.
Source: [consulted page](https://ethnomuseum.ru/events1/exhibitions/current/narody-velikoj-stepi-buryaty-kalmyki/) Primary basis: museum account of its own collection and exhibition.
Read scope: exhibition description and collection content.
Used for separate Buryat material traditions and the distinction between shamanic and Buddhist collection material.
Limit: an exhibition summary does not establish object-level provenance for any asset or permission to reproduce sacred objects.

### B3. Buryat terminology comparison

Mátyás Balogh, **Introduction to the Present-Day Shamanic Practices of the Buryats in Mongolia**.
Source: [consulted page](https://www.academia.edu/1476929/Introduction_to_the_Present_Day_Shamanic_Practices_of_the_Buryats_in_Mongolia) Primary basis: author-uploaded research based on 2004 and 2005 fieldwork, interviews, and recordings.
Read scope: opening methodology, dialect qualification, and relevant terminology in the accessible text.
Used only to corroborate böö in a related Buryat setting and to retain the dialect caution.
Limit: this is Mongolia rather than Olkhon and does not authorize transferring a detailed ritual repertoire to the Baikal profile.

### E1. Evenki field and archival research

Nikolai Ssorin-Chaikov, **Evenki Shamanistic Practices in Soviet Present and Ethnographic Present Perfect**, Anthropology of Consciousness 12(1), 2001.
Source: [consulted page](https://www.academia.edu/11766939/Evenki_Shamanistic_Practices_in_Soviet_Present_and_Ethnographic_Present_Perfect) Primary basis: original fieldwork in 1988 to 1989 and 1993 to 1995, with archival research.
Read scope: accessible introduction, local setting, archival discussion, and terminology.
Used for the Podkamennaya Tunguska anchor, taiga context, saman, and historical change.
Limit: its findings belong to the studied communities and do not define every Evenki group.

### E2. Evenki community and museum collaboration

Pitt Rivers Museum, **Wandering in Other Worlds: Evenki Cosmology and Shamanic Traditions**.
Source: [consulted page](https://www.prm.ox.ac.uk/event/wandering-in-other-worlds) Primary basis: the museum's collection and exhibition collaboration with Evenki participants, including the Council of Elders.
Read scope: complete exhibition description.
Used for diversity across Evenki settings and provenance of historical museum material.
Limit: the described modern collaboration involves Chirinda and Tura, not the precise E1 field locality.

### E3. A provenanced Evenki object

Russian Museum of Ethnography, **Shaman's headdress.
Evenki**.
Source: [consulted page](https://catalog.ethnomuseum.ru/entity/OBJECT/259562) Primary basis: museum object record REM 5589-39.
Read scope: object date, location, material, and interpretation.
Used to demonstrate that specific historical material can be sourced without making it a universal costume.
Limit: a single object from the Yenisei region does not establish the outfit of the fictional visitor.

### J1. Jeju local cultural account

So-jeon Kang, **Jeju Chilmeoridang Yeongdeunggut**, ICH Courier, volume 47, June 2021.
Source: [consulted page](https://ichcourier.unesco-ichcap.org/board.es?act=view&bid=A102&list_no=573&mid=a10501000000) Primary basis: a Jeju National University scholar's local heritage account published by ICHCAP.
Read scope: complete article text.
Used for simbang, Geonip-dong, community purposes, seasonal context, and the shrine's later relocation.
Limit: a contemporary account does not establish an unchanged 1930s ceremony, wardrobe, or port layout.

### Y1. Yup'ik community terminology and memory

Calista Corporation and Calista Education and Culture, **Yup'ik Teaching Moment: Tuunraq**, September and October 2025.
Source: [consulted page](https://www.calistacorp.com/news/yupik-teaching-moment-tuunraq/) Primary basis: community cultural account provided by Alice Cucuaq Rearden.
Read scope: complete relevant article.
Used for the plural angalkut and remembered community roles.
Limit: beliefs reported by community speakers are not evidence that supernatural claims are scientifically established.

### Y2. Yup'ik oral histories

Alice Rearden and Marie Meade, edited by Ann Fienup-Riordan, **Angalkut/Shamans in Yup'ik Oral Tradition**, 2025.
Source: [consulted page](https://www.jstor.org/stable/jj.25433746) Primary basis: bilingual first-person community recollections gathered through Calista Education and Culture.
Read scope: publisher description, accessible chapter excerpts, geographic and terminology passages, and early twentieth century recollections.
Used for angalkuq, regional distinctions, and historical memory.
Limit: the complete book was not accessible and was not read.
No participant's personal identity or story is adapted as the fictional visitor.

### Y3. Community place knowledge

Exchange for Local Observations and Knowledge of the Arctic, **The names they carry: The continued efforts of Yupik elders to pass down knowledge**, 15 April 2020.
Source: [consulted page](https://eloka.nsidc.org/our-work/stories-events/names-they-carry-continued-efforts-yupik-elders-pass-down-knowledge) Primary basis: institutional account of its own collaboration with Yup'ik elders and Calista.
Read scope: complete article.
Used for lower Kuskokwim and delta route knowledge.
Limit: the contemporary atlas and educational project are not game-period technologies or direct proof of an individual's knowledge.

### H1. Hmong community research in Luang Prabang

PhotoForward and Traditional Arts and Ethnology Centre, **Laos: SOS Community Research Project**.
Source: [consulted page](https://www.photoforward.org/laos-sos-community-research-project.html) Primary basis: community-directed interviews and photography produced with TAEC.
Read scope: project description and the Hmong shaman research section associated with Pouxang village.
Used for the local geographic anchor and community research provenance.
Limit: no videos were watched and no photograph was accepted as a period asset.

### H2. Hmong practitioner interviews

Religions in Minnesota, Carleton College, **Washoua & Bao**.
Source: [consulted page](https://religionsmn.carleton.edu/exhibits/show/hmong-religiosity/portraits-of-hmong-shamans/washoua---bao) Primary basis: original interviews with practitioners.
Read scope: complete page.
Used for txiv neeb and variation between families.
Limit: contemporary Minnesota testimony has a different location and date from the proposed home region.

### H3. Luang Prabang livelihood context

Official Website for Tourism Luang Prabang, **Cultural Diversity**.
Source: [consulted page](https://tourismluangprabang.org/about-luangprabang/cultural-diversity/) Primary basis: local institutional account of regional communities.
Read scope: body sections distinguishing named groups, livelihoods, and housing.
Used narrowly for upland rice and the need to distinguish named communities.
Limit: tourism summaries simplify variation and do not establish period-specific clothing or all village practices.

### H4. Hmong material variation

Traditional Arts and Ethnology Centre, **Hmong**.
Source: [consulted page](https://www.taeclaos.org/featured_item/hmong/) Primary basis: museum interpretation of the community and its material culture.
Read scope: complete concise page.
Used for clothing variation and caution about contemporary special-occasion dress.
Limit: no particular pattern or garment is approved for reproduction by this research pass.

### T1. Northern Vietnamese heritage geography

Vietnam Government News, **Then practice recognized as UNESCO Intangible Cultural Heritage of Human**, 13 December 2019.
Source: [consulted page](https://en.baochinhphu.vn/then-practice-recognized-as-unesco-intangible-cultural-heritage-of-human-11136911.htm) Primary basis: official heritage recognition record and geographic summary.
Read scope: complete article body.
Used for the listed northern provinces, including Cao Bằng and Lạng Sơn.
Limit: an institutional summary is not a complete village ethnography or proof of every local historical form.

### T2. Tày practitioner distinctions

David Holm, **Literate Shamanism: The Priests Called Then among the Tày in Guangxi and Northern Vietnam**, Religions 10(1), 64, 2019.
Source: [consulted page](https://www.researchgate.net/publication/330487098_Literate_Shamanism_The_Priests_Called_Then_among_the_Tay_in_Guangxi_and_Northern_Vietnam) DOI: [publisher record](https://doi.org/10.3390/rel10010064) Primary basis: author's original fieldwork in Vietnam and Guangxi.
Read scope: abstract and bibliographic metadata only.
Used for Tày identity, practitioner terminology, gender variation, and textual repertoire.
Limit: the full text did not load through the consulted publisher and author-copy routes.
No detailed ritual sequence is inferred from the abstract.

### T3. Then heritage record

UNESCO Multimedia Archives, **Practices of Then by Tày, Nùng and Thái Ethnic Groups in Viet Nam**.
Source: [consulted page](https://www.unesco.org/archives/multimedia/document-4956) Primary basis: the archive's description of a 2018 Vietnamese Institute for Musicology documentary.
Read scope: catalog description and production metadata.
Used for stated community purposes and musical accompaniment, with the oral-transmission qualification discussed above.
Limit: the film was not watched and the nomination dossier was not accessible.

### A1. Alutiiq reserve

Alutiiq Museum and Archaeological Repository, **Alutiiq Word of the Week: Shaman**.
Source: [consulted page](https://alutiiqmuseum.org/collection/Detail/word/442) Primary basis: community museum interpretation and terminology.
Read scope: complete entry.
Used for the two attested titles and stated twentieth century continuity.
Limit: the entry does not resolve the game's Kodiak state boundary or license reuse of its depicted object.

### A2. Tlingit reserve and sacred-object boundary

Sealaska Heritage Institute, **New book details Tlingit shamanism**, 21 July 2026.
Source: [consulted page](https://sealaskaheritage.org/new-book-details-tlingit-shamanism/) Primary basis: the community institution's own research publication and cultural protocols.
Read scope: complete announcement.
Used for íx̱t', historical roles, and restrictions surrounding sacred objects.
Limit: an announcement is not the full book and does not identify a game-period visitor.

### M1. Mongolian sacred-site record

UNESCO Multimedia Archives, **Mongolian Traditional Practices of Worshipping the Sacred Sites**.
Source: [consulted page](https://www.unesco.org/archives/multimedia/document-4668) Primary basis: catalog record for a 2016 production by Mongolia's Research and Information Center for Sacred Sites.
Read scope: archive description and production metadata.
Used only to identify a research limitation concerning modern revival and to avoid equating all sacred-site practice with one practitioner type.
Limit: no video was watched.

### M2. Burkhan Khaldun landscape record

UNESCO World Heritage Centre, **Great Burkhan Khaldun Mountain and its surrounding sacred landscape**.
Source: [consulted page](https://whc.unesco.org/en/list/1440) Primary basis: official heritage designation and landscape record.
Read scope: description, significance, authenticity, and management text.
Used for the Khentii setting, mixed religious context, and the explicit continuity limitation.
Limit: a sacred-landscape designation does not establish the required local practitioner and period profile.
