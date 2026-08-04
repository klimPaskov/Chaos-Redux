# Chaos Warfare Named Scientists and CBRN Advisors: Historical Source Audit

Audit date: 2026-08-04.

Status: complete for all twelve requested existing candidates, with bounded historical uncertainties recorded below.

Scope: verify existing runtime portrait basenames, `.gfx` sprite mappings, and startup-generated named scientist identities; then recommend a historically defensible role gate using institutional, primary, and academic sources where feasible.

This is an audit of existing inputs, not a visual-asset production request. No portrait DDS, source image, PNG, `.gfx` file, gameplay file, localisation file, or interface file was edited. No external portrait image was downloaded or generated, and no new portrait license or public-domain claim is made.

## Executive result

All twelve identities are already represented by a matching runtime DDS in `gfx/leaders/scientists/`, a matching sprite in `interface/_scientists_portraits.gfx`, and a matching startup-generated named scientist in `common/scripted_effects/chaosx_startup_history_effects.txt`.

The startup system dispatches the country grants once from `chaosx_apply_startup_history_grants` and assigns each generated scientist a name, large portrait, and `chaosx_scientist_*` flag.

Recommended no-doctrine technical theorists: Howard Florey and Alexander Fleming.

Recommended no-doctrine defensive advisors: none of these twelve is a clean pure-defensive fit; do not force the penicillin researchers into this slot when the technical-theorist slot is available.

Recommended Chaos-Warfare-doctrine-gated aggressive or dual-use weaponization specialists: Paul Fildes, Gerhard Schrader, Kurt Blome, Shiro Ishii, Masaji Kitano, Franciszek Witaszek, Ivan Mikhailovich Velikanov, Grigory Mairanovsky, Ira Baldwin, and Frank Olson.

No candidate should be excluded from the existing named-scientist roster solely on identity or portrait-wiring grounds. The roster does need the review notes for Witaszek's exact agent attribution, Blome's defensive-versus-offensive German program context, Mairanovsky's chemical/toxin rather than standard military-biological role, Olson's individual-versus-organizational offensive assignment, and Velikanov's existing second portrait consumer.

## Repository identity and portrait verification

The relevant canonical asset reference was inspected at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/`. Its `README.md`, `CATALOG.md`, and `REFERENCE_MANIFEST.md` identify `portraits/advisors/` as the native advisor/theorist dossier family and show 65x67 advisor examples. The existing scientist entries below are 156x210 full portraits used through the startup `army.large` field, so this audit does not propose a canvas change.

All hashes below are SHA-256 hashes of the existing runtime DDS at audit time. Every candidate DDS reported a `DDS ` header and 156x210 dimensions.

| Identity | Existing runtime portrait and SHA-256 | Existing sprite mapping | Startup-generated named scientist evidence |
| --- | --- | --- | --- |
| Howard Walter Florey (AST) | `gfx/leaders/scientists/portrait_AST_howard_florey.dds`<br>`98dc7c95278658a08820e1aab6465283574d694e57de568d6f80d05303a127e2` | `GFX_portrait_AST_howard_florey` -> same DDS in `interface/_scientists_portraits.gfx:59-60` | `common/scripted_effects/chaosx_startup_history_effects.txt:121-142`; name `AST_howard_florey`; large portrait matches; flag `chaosx_scientist_ast_howard_florey`; `specialization_biowarfare = 3`; `scientist_trait_fast_learner`. |
| Paul Fildes (ENG) | `gfx/leaders/scientists/portrait_ENG_paul_fildes.dds`<br>`5baf538b7eb09733e2387424c18885c5c854c9bd926dcce8a020e8b9457af1e5` | `GFX_portrait_ENG_paul_fildes` -> same DDS in `interface/_scientists_portraits.gfx:47-48` | `common/scripted_effects/chaosx_startup_history_effects.txt:230-250`; name `ENG_paul_fildes`; large portrait matches; flag `chaosx_scientist_eng_paul_fildes`; `specialization_biowarfare = 2`; `scientist_trait_bright`. |
| Alexander Fleming (ENG) | `gfx/leaders/scientists/portrait_ENG_alexander_fleming.dds`<br>`a4ec2e9656c029dc01843d0d659daa72efe666477d9a88d9f366d679577cdd44` | `GFX_portrait_ENG_alexander_fleming` -> same DDS in `interface/_scientists_portraits.gfx:51-52` | `common/scripted_effects/chaosx_startup_history_effects.txt:252-271`; name `ENG_alexander_fleming`; large portrait matches; flag `chaosx_scientist_eng_alexander_fleming`; `specialization_biowarfare = 2`; no additional startup trait declared. |
| Gerhard Schrader (GER) | `gfx/leaders/scientists/portrait_GER_gerhard_schrader.dds`<br>`08e168b09d16f6a8b972f6ee9a873c283aa13356c0e7fc02aa0533107dd95af6` | `GFX_portrait_GER_gerhard_schrader` -> same DDS in `interface/_scientists_portraits.gfx:15-16` | `common/scripted_effects/chaosx_startup_history_effects.txt:374-394`; name `GER_gerhard_schrader`; large portrait matches; flag `chaosx_scientist_ger_gerhard_schrader`; `specialization_cw = 3`; `scientist_trait_brilliant_theorist`. |
| Kurt Blome (GER) | `gfx/leaders/scientists/portrait_GER_kurt_blome.dds`<br>`02ba623450b7645114e9473ce8490c558d35c10dad802a85f2abf10c5d7fb4e2` | `GFX_portrait_GER_kurt_blome` -> same DDS in `interface/_scientists_portraits.gfx:19-20` | `common/scripted_effects/chaosx_startup_history_effects.txt:396-416`; name `GER_kurt_blome`; large portrait matches; flag `chaosx_scientist_ger_kurt_blome`; `specialization_biowarfare = 3`; `scientist_trait_fast_learner`. |
| Shiro Ishii (JAP) | `gfx/leaders/scientists/portrait_JAP_shiro_ishii.dds`<br>`ba806c1ba5c12cfd8c79e5e207f96501b704bc2022f44cbb40296ef74588a985` | `GFX_portrait_JAP_shiro_ishii` -> same DDS in `interface/_scientists_portraits.gfx:3-4` | `common/scripted_effects/chaosx_startup_history_effects.txt:651-671`; name `JAP_shiro_ishii`; large portrait matches; flag `chaosx_scientist_jap_shiro_ishii`; `specialization_biowarfare = 4`; resourceful, fast learner, brilliant theorist, genius, and inhumane traits. |
| Masaji Kitano (JAP) | `gfx/leaders/scientists/portrait_JAP_masaji_kitano.dds`<br>`ab11d4d4ab13bfd906f76f63b7c68b078a52af1ea4fdf292ec130cb7440a4421` | `GFX_portrait_JAP_masaji_kitano` -> same DDS in `interface/_scientists_portraits.gfx:7-8` | `common/scripted_effects/chaosx_startup_history_effects.txt:673-693`; name `JAP_masaji_kitano`; large portrait matches; flag `chaosx_scientist_jap_masaji_kitano`; `specialization_biowarfare = 2`; `scientist_trait_inhumane`. |
| Franciszek Witaszek (POL) | `gfx/leaders/scientists/portrait_POL_franciszek_witaszek.dds`<br>`720bc822c3c8ae285573a0267fbcf2aea1b2a19ba5b698635fc9baa7a48a6670` | `GFX_portrait_POL_franciszek_witaszek` -> same DDS in `interface/_scientists_portraits.gfx:75-76` | `common/scripted_effects/chaosx_startup_history_effects.txt:802-822`; name `POL_franciszek_witaszek`; large portrait matches; flag `chaosx_scientist_pol_franciszek_witaszek`; `specialization_biowarfare = 2`; `scientist_trait_resourceful`. |
| Ivan Mikhailovich Velikanov (SOV) | `gfx/leaders/scientists/portrait_SOV_ivan_mikhailovich_velikanov.dds`<br>`053752e40a48c28ad69780a8f229ea233d6eda05be9c2abcec6df01194315445` | `GFX_portrait_SOV_ivan_mikhailovich_velikanov` -> same DDS in `interface/_scientists_portraits.gfx:87-88` | `common/scripted_effects/chaosx_startup_history_effects.txt:944-964`; name `SOV_ivan_mikhailovich_velikanov`; large portrait matches; flag `chaosx_scientist_sov_ivan_mikhailovich_velikanov`; `specialization_biowarfare = 3`; `scientist_trait_genius`. The same sprite is also used by `history/countries/UWR - Unconventional Warfare Republic.txt:42-43` for the UWR country leader, so no new clone or simultaneous second owner should be introduced. |
| Grigory Mairanovsky (SOV) | `gfx/leaders/scientists/portrait_SOV_grigory_mairanovsky.dds`<br>`a6b219a9cde2a93ca76030a69a74dc135f606f7a187dab85c47f65e282f28038` | `GFX_portrait_SOV_grigory_mairanovsky` -> same DDS in `interface/_scientists_portraits.gfx:83-84` | `common/scripted_effects/chaosx_startup_history_effects.txt:922-942`; name `SOV_grigory_mairanovsky`; large portrait matches; flag `chaosx_scientist_sov_grigory_mairanovsky`; `specialization_biowarfare = 2`; brilliant theorist and inhumane traits. |
| Ira Baldwin (USA) | `gfx/leaders/scientists/portrait_USA_ira_baldwin.dds`<br>`9ea3896726d4748b4e6fd7b90fdaf876d8281a0036aa6230e0e4cba4ab36edc2` | `GFX_portrait_USA_ira_baldwin` -> same DDS in `interface/_scientists_portraits.gfx:67-68` | `common/scripted_effects/chaosx_startup_history_effects.txt:1067-1087`; name `USA_ira_baldwin`; large portrait matches; flag `chaosx_scientist_usa_ira_baldwin`; `specialization_biowarfare = 3`; `scientist_trait_resourceful`. |
| Frank Olson (USA) | `gfx/leaders/scientists/portrait_USA_frank_olson.dds`<br>`898520be5692a36956dc5ebfd8e3638abeded4c3a7b48d9175ab9f95ab426feb` | `GFX_portrait_USA_frank_olson` -> same DDS in `interface/_scientists_portraits.gfx:63-64` | `common/scripted_effects/chaosx_startup_history_effects.txt:1045-1065`; name `USA_frank_olson`; large portrait matches; flag `chaosx_scientist_usa_frank_olson`; `specialization_biowarfare = 2`; `scientist_trait_bright`. |

The startup dispatcher is `common/scripted_effects/chaosx_startup_history_effects.txt:10-41`, where the AST, ENG, GER, JAP, POL, SOV, and USA grants are called behind the one-time `chaosx_startup_history_grants_applied` global flag.

## Historical role audit

The recommendations below are role-fit decisions, not claims that the existing gameplay traits are historically authoritative.

| Identity | Historically defensible role evidence | Recommendation | Confidence | Sensitive-history and wording note |
| --- | --- | --- | --- | --- |
| Howard Walter Florey | Australian-born pathologist and Oxford researcher who, with Ernst Chain and colleagues, turned penicillin into a usable therapeutic drug and helped establish its clinical production. | Technical theorist available without Chaos Warfare doctrine. | High. | Do not describe Florey as an offensive CBRN researcher; his defensible fit is antimicrobial medicine and medical logistics. |
| Paul Fildes | Head of the British Biology Department at Porton Down from 1940; led research on anthrax, botulinum toxin, biological aerosols, and planned retaliatory weapons, including Operation Vegetarian material that was not used. | Aggressive weaponization advisor/theorist requiring Chaos Warfare doctrine. | High. | The program was state offensive/retaliatory research; do not claim that the planned anthrax cattle cakes were deployed or that every later claim about clandestine operations is proven. |
| Alexander Fleming | Discovered penicillin's antibacterial action and shared the 1945 Nobel Prize with Florey and Chain for the discovery and therapeutic use of penicillin. | Technical theorist available without Chaos Warfare doctrine. | High. | Keep Fleming's role medical and bacteriological; do not credit him alone with the Oxford scale-up or turn penicillin discovery into a weaponization claim. |
| Gerhard Schrader | IG Farben chemist whose work led to the discovery of tabun and sarin; IG Farben's wartime history documents production of tabun and construction of sarin facilities. | Aggressive chemical-weaponization advisor/theorist requiring Chaos Warfare doctrine. | High for chemical role. | His discovery arose from insecticide research and does not by itself prove personal field use or command; note IG Farben's Nazi rearmament, forced-labor, and chemical-weapons context without assigning unsupported personal crimes. |
| Kurt Blome | Nuremberg records place him in charge of German research for measures against biological warfare; academic review evidence says his cancer-research cover also examined offensive plague, cholera, and typhoid possibilities. Nazi directives officially emphasized defense and Germany did not field a ready biological arsenal. | Aggressive/dual-use weaponization advisor/theorist requiring Chaos Warfare doctrine, with a conditional review flag. | Medium-high. | Do not present him as a proven battlefield deployer or as personally proven to have conducted human experiments. Record his Nazi medical establishment role, the Posen institute, the defensive/offensive dispute, and his 1947 acquittal separately. |
| Shiro Ishii | Japanese Army physician and head of Unit 731; archival and academic sources document his leadership of a biological-warfare program and Unit 731's human experimentation and weapons work. | Aggressive weaponization advisor/theorist requiring Chaos Warfare doctrine. | High. | This is a war-crimes-sensitive identity. Do not glamorize Unit 731 or use unsupported exact victim totals; note postwar U.S. immunity negotiations as a separate historical fact. |
| Masaji Kitano | Former director/second commander of the Japanese biological-warfare organization; U.S. archival material records his interrogation, and academic histories identify him as Ishii's successor during the wartime Unit 731 program. | Aggressive weaponization advisor/theorist requiring Chaos Warfare doctrine. | High for command/program fit. | Human experimentation and postwar immunity are central context. Avoid treating his postwar pharmaceutical career as exculpatory or using unverified casualty totals. |
| Franciszek Witaszek | Polish resistance doctor and microbiologist associated with the WKZO/Union of Retaliation CBW sabotage program; the academic account identifies him as responsible for producing agents while also trying to limit indiscriminate use. | Aggressive weaponization advisor/theorist requiring Chaos Warfare doctrine, but with a resistance-context caveat. | Medium-high for CBW sabotage; low for the exact typhus-bacteria wording. | Do not equate anti-occupation sabotage with Unit 731 or Nazi extermination policy. The reviewed academic source supports chemical/biological sabotage and production, but this pass did not establish the exact typhus attribution; keep that phrase needs-review or omit it. |
| Ivan Mikhailovich Velikanov | Oxford Academic identifies him as the lead scientist of the Soviet Union's offensive biological-warfare program before his arrest and execution during the Great Terror. | Aggressive weaponization advisor/theorist requiring Chaos Warfare doctrine. | High. | Mention the offensive program and political repression without implying that his arrest or execution was a judicial finding of weapons crimes. The existing portrait is also a UWR leader input and requires ownership care. |
| Grigory Mairanovsky | Sources identify him as a director of the Soviet secret-police poison laboratory and a developer of lethal toxins for covert operations; the best-supported role is chemical/toxin development rather than ordinary military biological research. | Aggressive chemical/toxin weaponization advisor/theorist requiring Chaos Warfare doctrine. | Medium-high. | Human experimentation and state assassination are sensitive. Exact victim lists, delivery methods, and individual killings vary across memoir and secondary accounts; do not make those claims part of the basic role text. |
| Ira Baldwin | Civilian scientific director of the U.S. biological-warfare program at Camp Detrick; sources document work on large-scale botulinum-toxin and anthrax production, testing, and continuing advisory involvement. | Aggressive weaponization advisor/theorist requiring Chaos Warfare doctrine. | High. | Keep the civilian scientist distinction, while acknowledging that the program combined defensive preparation with offensive production research and animal testing. |
| Frank Olson | U.S. government records identify him as an aerobiology expert in the Special Operations Division at the Army Biological Center/Camp Detrick; the division's documented functions included vulnerability assessment, offensive biological-weapons techniques, and CIA biological research. | Aggressive/dual-use weaponization advisor/theorist requiring Chaos Warfare doctrine, with an individual-assignment caveat. | High for CBRN/SOD affiliation; medium for personal offensive assignment. | Keep his later MKULTRA LSD incident and disputed death separate from his wartime CBRN role. Do not state murder as settled fact; do not infer that every SOD function was personally directed by Olson. |

## Source links and provenance notes

The links in this section are textual historical sources only. No linked page was used as a portrait image source, and no image license is inferred from any of them.

### Howard Florey

- [Nobel Prize, Sir Howard Florey biographical](https://www.nobelprize.org/prizes/medicine/1945/florey/biographical/) (award-era biography and institutional record of his penicillin work).
- [University of Oxford Dunn School, The Discovery of Penicillin](https://www.path.ox.ac.uk/centenary/our-history/the-discovery-of-penicillin/) (institutional history of Florey's therapeutic and production work).

### Paul Fildes

- [PBS American Experience, Paul Fildes](https://www.pbs.org/wgbh/americanexperience/features/weapon-biography-paul-fildes/) (institutional historical overview of Porton Down and the British biological-weapons program).
- [Scientists and the history of biological weapons: A brief historical overview](https://pmc.ncbi.nlm.nih.gov/articles/PMC1490304/) (academic review describing Fildes's offensive interpretation and anthrax-bomb work).
- [Botulinum Toxin in WW2 German and Allied Armies](https://karger.com/ene/article/84/1/53/125498/Botulinum-Toxin-in-WW2-German-and-Allied-Armies) (academic review using British National Archives material and separating plans, tests, and actual fielding).

### Alexander Fleming

- [Nobel Prize, Sir Alexander Fleming questions and answers](https://www.nobelprize.org/prizes/medicine/1945/fleming/questions-and-answers/) (institutional record of the penicillin discovery and therapeutic use).
- [Royal Society catalogue, Fleming certificate of election](https://catalogues.royalsociety.org/CalmView/Record.aspx?id=EC%2F1943%2F07&src=CalmView.Catalog) (institutional biographical and scientific record).

### Gerhard Schrader

- [BASF Corporate History, IG Farben](https://www.basf.com/global/en/who-we-are/history/IG-Farben) (corporate historical account of Schrader's sarin discovery and IG Farben tabun/sarin production context).
- [Springer, Reconstruction of Production and Storage Sites for Chemical Warfare Agents](https://link.springer.com/chapter/10.1007/978-3-319-51664-6_16) (academic treatment of the tabun and sarin development history).

### Kurt Blome

- [Harvard Law School Nuremberg Trials Project, NMT 1 Medical Case transcript](https://nuremberg.law.harvard.edu/transcripts/1-transcript-fornmt-1-medical-case?seq=4691) (primary trial record covering Blome's biological-warfare research position and his defensive account).
- [Karger, Botulinum Toxin in WW2 German and Allied Armies](https://karger.com/ene/article/84/1/53/125498/Botulinum-Toxin-in-WW2-German-and-Allied-Armies) (academic review describing the official defensive ban, Blome's reported offensive study, and the absence of a ready German battlefield arsenal).
- [Harvard Law School Nuremberg transcript, verdict sequence](https://nuremberg.law.harvard.edu/transcripts/1-transcript-for-nmt-1-medical-case?seq=11604) (primary record of the tribunal's not-guilty finding; acquittal is not treated as proof that every historical allegation was false).

### Shiro Ishii

- [U.S. National Archives, Japanese Interim Report](https://www.archives.gov/iwg/reports/japanese-interim-report-march-2002-1.html) (archival description of SCAP/Fort Detrick investigations into Ishii and Unit 731 biological-warfare experiments).
- [Oxford Academic, Unit 731: Where Entomology Became Evil](https://academic.oup.com/ae/article/69/4/54/7479678) (academic overview of Ishii's Unit 731 leadership and biological-weapons role).
- [PBS American Experience, Shiro Ishii](https://www.pbs.org/wgbh/americanexperience/features/weapon-biography-shiro-ishii/) (institutional historical overview with a caution about destroyed records and postwar immunity).

### Masaji Kitano

- [U.S. National Archives, Select Documents on Japanese War Crimes](https://www.archives.gov/files//iwg/japanese-war-crimes/select-documents.pdf) (archival collection including the 1946 Kitano statement and Unit 731 roster material).
- [The history of biological warfare](https://pmc.ncbi.nlm.nih.gov/articles/PMC1326439/) (academic historical overview identifying Kitano as Ishii's successor and discussing wartime research publications).
- [U.S. Army report on Japanese biological-warfare activities](https://www.bulletpicker.com/pdf/Report-on-Japanese-Biological-Warfare-Activities-1946.pdf) (transcribed/declassified report naming Ishii and Kitano as former directors interviewed about the Japanese BW R&D organization).

### Franciszek Witaszek

- [Robert Petersen, The covert battlefield: Doctor Witaszek, the WKZO, and the Polish use of biological and chemical warfare](https://doi.org/10.1080/10736700.2020.1866321) (academic article on the Polish resistance CBW sabotage program and Witaszek's production and restraint role).
- [Institute of National Remembrance, Dr Franciszek Witaszek](https://przystanekhistoria.pl/pa2/tematy/nauka-i-technika/78835,Dr-Franciszek-Witaszek.html) (Polish institutional biography of his medical, microbiological, resistance, and wartime fate).
- [Wielkopolskie Museum of Independence, Franciszek Witaszek](https://www.wmn.poznan.pl/cpt_kalendarium/urodzil-sie-doktor-franciszek-witaszek/) (regional museum record of his resistance identity and death under German occupation).

### Ivan Mikhailovich Velikanov

- [Oxford Academic, The Rise and Fall of a Working-Class Hero: Ivan Mikhailovich Velikanov](https://academic.oup.com/book/4364/chapter-abstract/146298118) (Anthony Rimmington, *Stalin's Secret Weapon*, Oxford University Press, 2018; explicitly identifies Velikanov as lead scientist of the Soviet offensive BW program).
- [Oxford Academic, Stalin's Secret Weapon](https://academic.oup.com/book/4364) (book-level context for the early Soviet biological-weapons program and its repression).

### Grigory Mairanovsky

- [Taylor & Francis, Poisonous affairs: Russia's evolving use of poison in covert operations](https://www.tandfonline.com/doi/abs/10.1080/10736700.2023.2229691) (academic history of the Soviet poison-laboratory lineage and covert toxicology).
- [The Guardian, Russia's Lab X](https://www.theguardian.com/world/2018/mar/09/russia-lab-x-poison-factory-that-helped-silence-soviet-critics) (reported history based on former Soviet intelligence accounts and Mairanovsky's documented association with the laboratory).

### Ira Baldwin

- [PBS American Experience, Ira Baldwin](https://www.pbs.org/wgbh/americanexperience/features/weapon-biography-ira-baldwin/) (institutional history using University of Wisconsin archival material and describing Baldwin as civilian scientific director at Camp Detrick).
- [Consortium for History of Science, Technology and Medicine, Making Danger](https://www.chstm.org/news/making-danger-biological-weapons-research-biosafety-and-management-microbial-life-1940-1990) (academic research summary based on the Ira Baldwin collection).
- [U.S. Army history PDF, General employment of toxic munitions](https://history.army.mil/portals/143/Images/Publications/catalog/10-1.pdf) (official military history referencing Baldwin and the creation of Camp Detrick).

### Frank Olson

- [CIA FOIA, Project MKULTRA report](https://www.cia.gov/readingroom/docs/PROJECT%20MKULTRA%2C%20THE%20CIAS%5B12885086%5D.pdf) (official declassified report identifying Olson as an aerobiology expert assigned to the Special Operations Division and describing that division's defensive and offensive functions).
- [CIA FOIA, CIA activities at Fort Detrick](https://www.cia.gov/readingroom/document/00146162) (official declassified description of the Camp Detrick CIA/Army BW-CW research arrangement).
- [Gerald R. Ford Presidential Library, Olson briefing paper](https://www.fordlibrarymuseum.gov/sites/default/files/pdf_documents/library/document/0047/phw19750721-01.pdf) (official archival record of the later LSD incident and the limits of what should be inferred about his death).

## Parent handoff and remaining review points

- The parent can wire the existing runtime basenames exactly as listed above; no new sprite name or DDS path is proposed.
- Treat Florey and Fleming as medical/antimicrobial technical theorists available without Chaos Warfare doctrine.
- Treat Fildes, Schrader, Ishii, Kitano, Velikanov, Baldwin, and Olson as doctrine-gated offensive or dual-use specialists, with Olson's personal assignment caveat.
- Treat Blome as doctrine-gated only if the design accepts a dual-use/offensive-research category; otherwise he is the strongest candidate for a defensive-without-doctrine fallback, but that fallback would understate the offensive aspects documented by the academic review.
- Keep Witaszek doctrine-gated if the roster represents actual CBW sabotage and production; do not make the exact typhus-bacteria claim without a stronger source.
- Keep Mairanovsky in a chemical/toxin branch rather than presenting him as an ordinary biological-warfare scientist.
- Do not introduce a second Velikanov character or portrait owner without resolving the existing UWR country-leader consumer.
- No candidate is blocked on identity or source availability, and no candidate is excluded outright. The open items are wording and doctrine-gate choices, not missing portraits or missing startup characters.
