# Event 021 / Event 006 portrait repair audit — 2026-09-25

Status: incomplete; candidate source packages are prepared for parent review, but no runtime portrait was replaced.

This is the expanded 65-consumer audit for all 32 Event 021-admitted Event 006 packages, not the earlier bounded portrait review. The accepted Event 021 crosswalk contains no Event 021-owned portrait rows; every subject below is an inherited Event 006 package consumer.

The original 65-row matrix remains [event021_event006_portrait_asset_audit_2026-09-25.json](event021_event006_portrait_asset_audit_2026-09-25.json) and retains exact character IDs, sprite names, GFX references, runtime paths, and baseline hashes. This refreshed row-by-row disposition is also machine-readable in [event021_event006_portrait_repair_audit_2026-09-25.json](event021_event006_portrait_repair_audit_2026-09-25.json).

## Audit outcome

- All 65 source-matrix rows were revalidated against current consumers and reviewed row by row; all 64 present DDS files still match their baseline SHA-256, and the only absent file remains Kuban’s declared large portrait.
- Existing runtime images were decoded and inspected at 156×210 and 4× nearest-neighbour; one row’s missing texture could not be reviewed. Contact sheets were supplementary only and were not used as row-level evidence.
- A fresh exact RGBA scan compared all existing runtime images with 262 archived 156×210 PNGs. It found 17 exact matches: the 14 legacy-generated portraits at rows 1, 2, 5–12, 14–15, 17–18; Shaban Polluzha at row 43; and the Samuel Wilder King and William D. Stephens repaint rows 64–65.
- The 29 current source-placeholder/review rows were left untouched. Their 186 referenced source/consumer evidence paths still exist; only row 43 had an exact archived PNG match. A non-match is not evidence of a wrong identity, and it does not invalidate a user-supplied styled final.
- Eleven identity-attributed source-candidate packages now contain untouched source copies, lossless crops, crop-equality metadata, deterministic 156×210 PNGs, 624×840 nearest-neighbour reviews, and completed provenance contracts. Five other legacy generated identities and the King repaint remain blocked by identity or rights evidence.
- No DDS conversion, runtime replacement, `.gfx` edit, character portrait-reference edit, or portrait-specific wiring was performed because the required independent review PASS has not been recorded; rights caveats remain for four candidate sources.

## Row-level dispositions

Rows below use the 1-based order of `portrait_rows` in the source matrix linked above. The current sprite and runtime path remain exactly those in the source matrix unless a candidate crosswalk is listed in the candidate table below.

| Row | Tag | Named consumer | Current finding |
| ---: | :--- | :--- | :--- |
| 1 | SCO | R. B. Cunninghame Graham | Source candidate prepared; independent/parent review pending. |
| 2 | SCO | Victor Morven Fortune | Source candidate prepared from Commons/IWM archive with PD-scan/PD-UKGov basis; prior independent source audit exists, but this new direct source-placeholder crop needs separate review. |
| 3 | WLS | J. H. Thomas | Existing source placeholder unchanged; final still user-supplied; no exact PNG match found. |
| 4 | WLS | George Frederick Myddleton Cornwallis-West | Blocked: National Portrait Gallery source has unresolved third-party rights. |
| 5 | BRI | Régis de l’Estourbeillon | Blocked: no defensible named source with established reuse rights. |
| 6 | BRI | Henri-Léon Devin | Candidate prepared from the named Gallica/Agence Rol source; BnF reuse terms need rights review. |
| 7 | AFX | Jules Destrée | Blocked: public-domain claim lacks a verified author/date/jurisdiction chain. |
| 8 | AFX | Louis Hubert baron Ruquoy | Candidate prepared from named Gallica/Agence Rol group photo; BnF rights caveat and small face need review. |
| 9 | AGX | Douwe Kalma | Candidate prepared from exact Tresoar circa-1919 named portrait; independent/parent review pending. |
| 10 | AGX | Pieter Reenalda | Candidate prepared from exact Tresoar 1911 KPM officer portrait; original face is bright/low contrast. |
| 11 | RHI | Wilhelm Marx | Candidate prepared from LOC Bain collection; LOC “no known restrictions” is not a license grant. |
| 12 | RHI | Gustav-Adolf von Zangen | Blocked: available source is too small/group-context-heavy for dependable identity and framing review. |
| 13 | RHI | Josef Friedrich Matthes | Existing source placeholder unchanged; final still user-supplied; no exact PNG match found. |
| 14 | BAY | Heinrich Held | Candidate prepared from Bundesarchiv caption naming Held at right; CC BY-SA 3.0 DE recorded. |
| 15 | BAY | Friedrich Dollmann | Blocked and quarantined: retained source caption describes Isteiner Klotz/Oberrhein and does not identify Dollmann. |
| 16 | BAY | Rupprecht of Bavaria | Existing source placeholder unchanged; final still user-supplied; no exact PNG match found. |
| 17 | AJX | Walter Simons | Candidate prepared from Bundesarchiv Bild 102-12279; existing character token is unchanged. |
| 18 | AJX | Friedrich von Rabenau | Candidate prepared from Bundesarchiv Bild 183-C05190; image confirms identity but not a Saar-specific office. |
| 19 | ICE | Sveinn Björnsson | Installed vanilla portrait is named-subject-specific; retained. |
| 20 | ICE | Björn Sveinsson Björnsson | Installed vanilla portrait is named-subject-specific; retained. |
| 21 | CAT | Lluís Companys i Jover | Installed vanilla portrait is named-subject-specific; retained. |
| 22 | COR | Adolphe Landry | Existing source placeholder unchanged; final still user-supplied; no exact PNG match found. |
| 23 | COR | Jean Chiappe | Existing source placeholder unchanged; final still user-supplied; no exact PNG match found. |
| 24 | ARX | Emilio Lussu | Existing source placeholder unchanged; final still user-supplied; no exact PNG match found. |
| 25 | ARX | Luigi Mella Sant’Elia | Existing source placeholder unchanged; source/visual review note remains open; no exact PNG match found. |
| 26 | ARX | Vittorio Vernè | Blocked: displayed identity is Vernè, but current portrait depicts Gavino Piras and the backing character token is `ARX_gavino_piras`; no identity-correct replacement source was established. |
| 27 | ASX | Luigi Sturzo | Existing source placeholder unchanged; final still user-supplied; no exact PNG match found. |
| 28 | ASX | Pietro Lanza di Scalea | Existing source placeholder unchanged; final still user-supplied; no exact PNG match found. |
| 29 | ASX | Luigi Rizzo | Existing source placeholder unchanged; final still user-supplied; no exact PNG match found. |
| 30 | ASX | Vincenzo Di Benedetto | Existing source placeholder unchanged; source/visual review note remains open; no exact PNG match found. |
| 31 | TRA | Iuliu Maniu | Blocked: inherited vanilla generic art is not Maniu; possible source candidates have unresolved item-level rights/provenance. |
| 32 | AXX | Otto Roth | Existing source placeholder unchanged; final still user-supplied; no exact PNG match found. |
| 33 | MAC | Metodija Andonov-Cento | Existing source placeholder unchanged; final still user-supplied; no exact PNG match found. |
| 34 | BAX | Hristo Silyanov | Existing source placeholder unchanged; final still user-supplied; no exact PNG match found. |
| 35 | BBX | Georgios Christakis-Zografos | Existing source placeholder unchanged; final still user-supplied; no exact PNG match found. |
| 36 | BBX | Spyros Spyromilios | Existing source placeholder unchanged; final still user-supplied; no exact PNG match found. |
| 37 | BOS | Mehmed Spaho | Existing source placeholder unchanged; final still user-supplied; no exact PNG match found. |
| 38 | MNT | Krsto Popović | Existing source placeholder unchanged; final still user-supplied; no exact PNG match found. |
| 39 | MNT | Blažo Jovanović | Existing source placeholder unchanged; final still user-supplied; no exact PNG match found. |
| 40 | MNT | Mitar Martinović | Existing source placeholder unchanged; final still user-supplied; no exact PNG match found. |
| 41 | KOS | Ferhat Draga | Existing source placeholder unchanged; final still user-supplied; no exact PNG match found. |
| 42 | KOS | Miladin Popović | Existing source placeholder unchanged; final still user-supplied; no exact PNG match found. |
| 43 | KOS | Shaban Polluzha | Exact existing source-placeholder PNG/DDS match confirmed; unchanged; 4× grain/high contrast still needs user review. |
| 44 | KAR | Pēteris Irklis | Blocked: inherited vanilla generic art is not Irklis; no defensible named source found. |
| 45 | KAR | Ukki Vainamoinen | Installed vanilla portrait is named-subject-specific; retained. |
| 46 | KAR | Jalmari Takkinen | Installed vanilla portrait is named-subject-specific; retained. |
| 47 | RUT | Augustin Voloshyn | Existing source placeholder unchanged; final still user-supplied; no exact PNG match found. |
| 48 | RUT | Andriy Brodiy | Existing source placeholder unchanged; final still user-supplied; no exact PNG match found. |
| 49 | RUT | Ivan Mondok | Existing source placeholder unchanged; final still user-supplied; no exact PNG match found. |
| 50 | RUT | Dmytro Klympush | Existing source placeholder unchanged; final still user-supplied; no exact PNG match found. |
| 51 | KUB | Ivanis Vasily Nikolaevich | Blocked: declared NSB large DDS is missing; only the separate 65×67 idea icon exists. |
| 52 | CRI | Ilyas Tarkhan | Blocked: inherited vanilla generic art is not Tarkhan; no defensible named source found. |
| 53 | TAT | Aleksandr Mikhaylovich Alemasov | Blocked: inherited vanilla generic art is not Alemasov; Tatarica image reuse terms are unclear. |
| 54 | BSK | Yakov Bykin | Existing source placeholder unchanged; final still user-supplied; no exact PNG match found. |
| 55 | ARM | Drastamat Kanayan | Blocked: inherited vanilla generic art is not Kanayan; candidate source has unknown author/source rights. |
| 56 | ARM | Hovhannes Kajaznuni | Blocked: inherited vanilla generic art is not Kajaznuni; Armenian History Museum source requires written permission. |
| 57 | ARM | Grigor Harutyunyan | Blocked: inherited vanilla generic art is not Harutyunyan; available group image/date/identity evidence is uncertain. |
| 58 | GEO | Giorgi Kvinitadze | Installed vanilla portrait is named-subject-specific; retained. |
| 59 | GEO | Noe Zhordania | Installed vanilla portrait is named-subject-specific; retained. |
| 60 | GEO | George Bagration Mukhrani | Installed vanilla portrait is named-subject-specific; retained. |
| 61 | AZR | Mir Jafar Baghirov | Blocked: inherited vanilla generic art is not Baghirov; candidate archive source rights are unresolved. |
| 62 | AZR | Mammad Amin Rasulzade | Blocked: inherited vanilla generic art is not Rasulzade; available Commons image is low-resolution with unverified source metadata. |
| 63 | AZR | Gara Garabeyov | Blocked: inherited vanilla generic art is not Garabeyov; only group/low-resolution evidence with uncertain face identification was found. |
| 64 | HAW | Samuel Wilder King | Blocked: current DDS equals an ImageGen repaint; HSA source rights are unresolved, so no replacement candidate is installed. |
| 65 | HBX | William D. Stephens | Source candidate prepared from LOC Bain collection; “no known restrictions” is not a license grant, so rights review remains open. |

## Prepared source candidates

Each candidate contract records complete original/crop/processed paths, source and processed SHA-256, source dimensions, exact crop box and decoded-pixel equality, mode, role/reference review, source rights, stable sprite/runtime DDS crosswalk, producer review, and outstanding independent verdicts. Candidate previews are raw 624×840 nearest-neighbour enlargements of the processed 156×210 RGB PNGs.

The [row-specific candidate review sheets](../../../assets/portraits/006_independence_wave/event021_event006_portrait_audit_2026-09-25/portrait_candidate_review_sheets_2026-09-25.md) show each candidate beside its unchanged source, exact crop, native PNG, nearest-neighbour 4× image, and canonical role-family vanilla reference; every provenance contract links to its matching section anchor. These are producer reviews, not independent approval.

| Row / subject | Source record and rights state | Crop L,T,R,B | Runtime sprite → DDS | Package contract |
| --- | --- | --- | --- | --- |
| 1 Cunninghame Graham | [Rijksmuseum, Alexander Bassano, RP-F-2001-7-67-30](https://www.rijksmuseum.nl/en/collection/object/Portret-van-Robert-Bontine-Cunninghame-Graham--58d50c7b9bd272d04b216d7494101918); public domain/CC0 per Rijksmuseum. | 1075,565,2720,2780 | `GFX_portrait_SCO_independence_wave_civic_convention` → `gfx/leaders/006_independence_wave/portrait_SCO_independence_wave_civic_convention.dds` | [contract](../../../assets/portraits/006_independence_wave/event021_event006_portrait_audit_2026-09-25/SCO_cunninghame_graham/portrait_SCO_independence_wave_civic_convention.txt) |
| 2 Victor Fortune | [Commons Fortune Victor Morven](https://commons.wikimedia.org/wiki/File:Fortune_Victor_Morven.jpg) and [51st Highland Division archive](https://51hd.co.uk/photos/img110); Commons records PD Mark 1.0 and PD-scan/PD-UKGov for the IWM image. The older independent source audit passed identity/rights/role with the 1940-after-1936 disclosure; current source-crop review remains pending. | 7,0,193,250 | `GFX_portrait_SCO_independence_wave_territorial_commandant` → `gfx/leaders/006_independence_wave/portrait_SCO_independence_wave_territorial_commandant.dds` | [contract](../../../assets/portraits/006_independence_wave/event021_event006_portrait_audit_2026-09-25/SCO_victor_morven_fortune/portrait_SCO_independence_wave_territorial_commandant.txt) |
| 6 Henri-Léon Devin | [Gallica item btv1b53236203v](https://gallica.bnf.fr/ark:/12148/btv1b53236203v), Agence Rol; PD claim in the source record, with BnF reuse terms unresolved. | 637,400,5682,7200 | `GFX_portrait_BRI_independence_wave_coastal_commandant` → `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_coastal_commandant.dds` | [contract](../../../assets/portraits/006_independence_wave/event021_event006_portrait_audit_2026-09-25/BRI_henri_leon_devin/portrait_BRI_independence_wave_coastal_commandant.txt) |
| 8 Ruquoy | [Gallica item btv1b531010537](https://gallica.bnf.fr/ark:/12148/btv1b531010537), Agence Rol; PD claim in associated record, with BnF reuse terms unresolved. | 3470,1000,4880,2900 | `GFX_portrait_AFX_walloon_reserve_commander` → `gfx/leaders/006_independence_wave/portrait_AFX_walloon_reserve_commander.dds` | [contract](../../../assets/portraits/006_independence_wave/event021_event006_portrait_audit_2026-09-25/AFX_louis_hubert_ruquoy/portrait_AFX_walloon_reserve_commander.txt) |
| 9 Douwe Kalma | [Tresoar/Commons circa-1919 record](https://commons.wikimedia.org/wiki/File:Douwe_Kalma_yn_'e_Provinsjale_Bibleteek_yn_Ljouwert,_1919_ca._archiefnr_1990.jpg); catalog says no copyright/public domain. | 270,475,900,1323 | `GFX_portrait_AGX_friesland_coastal_council` → `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_council.dds` | [contract](../../../assets/portraits/006_independence_wave/event021_event006_portrait_audit_2026-09-25/AGX_douwe_kalma_tresoar_1919/portrait_AGX_friesland_coastal_council.txt) |
| 10 Pieter Reenalda | [Tresoar/Commons 1911 record](https://commons.wikimedia.org/wiki/File:Eerste_officier_KPM_Pieter_Reenalda_in_uniform,_1911,_archiefnr_318-29.jpg); catalog says no copyright/public domain. | 400,150,900,823 | `GFX_portrait_AGX_friesland_coastal_commander` → `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_commander.dds` | [contract](../../../assets/portraits/006_independence_wave/event021_event006_portrait_audit_2026-09-25/AGX_pieter_reenalda_tresoar_1911/portrait_AGX_friesland_coastal_commander.txt) |
| 11 Wilhelm Marx | [Library of Congress item 2014716800](https://www.loc.gov/pictures/item/2014716800/), Bain collection, circa 1920; “no known restrictions” advisory is not a license. | 10,54,730,1024 | `GFX_portrait_RHI_independence_wave_provisional_directorate` → `gfx/leaders/006_independence_wave/portrait_RHI_independence_wave_provisional_directorate.dds` | [contract](../../../assets/portraits/006_independence_wave/event021_event006_portrait_audit_2026-09-25/RHI_wilhelm_marx/portrait_RHI_independence_wave_provisional_directorate.txt) |
| 14 Heinrich Held | [Bundesarchiv Bild 102-01176](https://commons.wikimedia.org/wiki/File:Bundesarchiv_Bild_102-01176,_Heinrich_Held_(rechts).jpg); CC BY-SA 3.0 DE; Held is explicitly captioned at right. | 310,45,540,355 | `GFX_portrait_BAY_independence_wave_state_council` → `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_state_council.dds` | [contract](../../../assets/portraits/006_independence_wave/event021_event006_portrait_audit_2026-09-25/BAY_heinrich_held/portrait_BAY_independence_wave_state_council.txt) |
| 17 Walter Simons | [Bundesarchiv Bild 102-12279](https://commons.wikimedia.org/wiki/File:Bundesarchiv_Bild_102-12279,_Walter_Simons.jpg); CC BY-SA 3.0 DE; existing character token preserved. | 55,45,520,650 | `GFX_portrait_AJX_friedrich_hoffmann` → `gfx/leaders/006_independence_wave/portrait_AJX_saar_municipal_neutral_commission.dds` | [contract](../../../assets/portraits/006_independence_wave/event021_event006_portrait_audit_2026-09-25/AJX_walter_simons/portrait_AJX_saar_municipal_neutral_commission.txt) |
| 18 Friedrich von Rabenau | [Bundesarchiv Bild 183-C05190](https://commons.wikimedia.org/wiki/File:Bundesarchiv_Bild_183-C05190,_Friedrich_v._Rabenau.jpg), photo Dorneth; CC BY-SA 3.0 DE; Saar-specific office not attested by source. | 20,30,540,730 | `GFX_portrait_AJX_karl_becker` → `gfx/leaders/006_independence_wave/portrait_AJX_saar_industrial_security_commissioner.dds` | [contract](../../../assets/portraits/006_independence_wave/event021_event006_portrait_audit_2026-09-25/AJX_friedrich_von_rabenau/portrait_AJX_saar_industrial_security_commissioner.txt) |
| 65 William D. Stephens | [Library of Congress item 2014715011](https://www.loc.gov/pictures/item/2014715011/), Bain collection, circa 1920–1925; “no known restrictions” advisory is not a license. | 75,130,685,940 | `GFX_portrait_HBX_independence_wave_civic_convention` → `gfx/leaders/006_independence_wave/portrait_HBX_independence_wave_civic_convention.dds` | [contract](../../../assets/portraits/006_independence_wave/event021_event006_portrait_audit_2026-09-25/HBX_william_d_stephens/portrait_HBX_independence_wave_civic_convention.txt) |

All eleven source crop JSON files report exact decoded crop equality and preserve original-source, crop, and processed PNG SHA-256 values. Full dimensions and hashes, including nearest-4× preview hashes, are in the companion JSON and co-located contracts.

## Remaining blockers and required input

- Five of the 15 legacy generated grounded-polity rows have no source package suitable for installation: Cornwallis-West (NPG third-party rights), de l’Estourbeillon (no defensible cleared portrait), Destrée (unverified public-domain claim), von Zangen (available group image too weak), and Dollmann (source caption/identity mismatch). The exact missing input is a verifiable named archival portrait plus attributable reuse rights, except for Dollmann, where an identity-correct source is required.
- The HAW King repaint must not remain accepted as a real-person replacement: the Hawaii State Archives source has unresolved reuse rights and cannot grant/deny reuse for this item. A rights-cleared source or documented permission is needed.
- The ten inherited generic rows are TRA Iuliu Maniu, KAR Pēteris Irklis, CRI Ilyas Tarkhan, TAT Aleksandr Alemasov, ARM Drastamat Kanayan, ARM Hovhannes Kajaznuni, ARM Grigor Harutyunyan, AZR Mir Jafar Baghirov, AZR Mammad Amin Rasulzade, and AZR Gara Garabeyov. They violate the accepted named-subject package requirement and remain blocked rather than silently passing as identity-correct.
- Maniu has possible Commons/Historic.ro leads but no cleared item-level rights chain; Irklis and Tarkhan lack a defensible source; Alemasov’s Tatarica image has unclear reuse terms; Kanayan’s available source lacks reliable author/source rights; Kajaznuni’s museum image requires written permission; Harutyunyan’s group image has uncertain subject/date; Baghirov’s archive lead has unresolved rights; Rasulzade’s available image is low-resolution with weak provenance; and Garabeyov is only visible in an uncertain low-resolution group image.
- Row 26 requires a user identity decision: should the displayed portrait identity be Vittorio Vernè or Gavino Piras? The audit will not change the character token, localization identity, or transfer one real person’s portrait to another. A rights-cleared source for the confirmed intended subject is also required.
- Row 51’s No Step Back GFX declares `gfx/leaders/KUB/portrait_KUB_ivanis_vasily_nikolaevich.dds`, but the installed DLC does not contain it; only `gfx/interface/ideas/idea_KUB_ivanis_vasily_nikolaevich.dds` exists. No substitute or guessed path was used.
- Rows 25 and 30 retain their existing user-review notes; row 43’s exact archived source placeholder remains unusually grainy/high-contrast at 4×. No image was altered to conceal these concerns.
- The source-candidate rights state remains conditional for Devin and Ruquoy (BnF reuse terms) and Marx and Stephens (LOC “no known restrictions” is not a grant). Reenalda’s source framing also remains conditional due to facial overexposure; von Rabenau’s source proves the person, not the Saar-specific office.

## Changed-file inventory and processing state

The eleven active candidate packages are under `docs/assets/portraits/006_independence_wave/event021_event006_portrait_audit_2026-09-25/`. Each contains the listed basename with these suffixes: `_original.jpg`, `_source_crop.png`, `_source_crop.json`, `_156x210.png`, `_156x210_nearest4x.png`, and `.txt` provenance contract.

| Candidate folder | Basename | Portrait ID |
| --- | --- | --- |
| `SCO_cunninghame_graham` | `portrait_SCO_independence_wave_civic_convention` | SCO civic convention |
| `SCO_victor_morven_fortune` | `portrait_SCO_independence_wave_territorial_commandant` | SCO territorial commandant |
| `BRI_henri_leon_devin` | `portrait_BRI_independence_wave_coastal_commandant` | BRI coastal commandant |
| `AFX_louis_hubert_ruquoy` | `portrait_AFX_walloon_reserve_commander` | AFX reserve commander |
| `AGX_douwe_kalma_tresoar_1919` | `portrait_AGX_friesland_coastal_council` | AGX coastal council |
| `AGX_pieter_reenalda_tresoar_1911` | `portrait_AGX_friesland_coastal_commander` | AGX coastal commander |
| `RHI_wilhelm_marx` | `portrait_RHI_independence_wave_provisional_directorate` | RHI provisional directorate |
| `BAY_heinrich_held` | `portrait_BAY_independence_wave_state_council` | BAY state council |
| `AJX_walter_simons` | `portrait_AJX_saar_municipal_neutral_commission` | AJX municipal commission |
| `AJX_friedrich_von_rabenau` | `portrait_AJX_saar_industrial_security_commissioner` | AJX industrial commissioner |
| `HBX_william_d_stephens` | `portrait_HBX_independence_wave_civic_convention` | HBX civic convention |

Three retained folders are not install candidates: `AGX_douwe_kalma` and `AGX_pieter_reenalda` are older unattributed candidates now marked superseded, and `BAY_friedrich_dollmann` is quarantined for identity mismatch. Their provenance `.txt` and source-crop JSON hashes were updated to reflect the new dispositions; their source evidence remains preserved.

The SCO folder also retains rejected inscription-crop evidence as `portrait_SCO_independence_wave_civic_convention_source_crop_candidate01_with_inscription.png`, `portrait_SCO_independence_wave_civic_convention_source_crop_candidate01_with_inscription.json`, `portrait_SCO_independence_wave_civic_convention_156x210_candidate01_with_inscription.png`, and `portrait_SCO_independence_wave_civic_convention_156x210_candidate01_with_inscription_nearest4x.png`; the selected candidate crop removes that margin note and is the package crop recorded in the contract.

The durable evidence additions are the eleven candidate packages above, their row-specific comparison sheet, and the refreshed source-crop JSON/contract hash links. The audit deliverables are this handoff and its JSON. Superseded AGX and quarantined Dollmann evidence, plus the rejected Cunninghame Graham inscription crop, remain archived with their dispositions recorded. No runtime DDS, `.gfx`, character file, event/package gameplay, localization, or Event 021 portrait asset changed. DDS output count is zero, and no runtime wiring has been installed.

All files beneath `docs/assets/` are ignored by `.gitignore`; they remain present in the worktree, are not staged, and need the parent’s decision on force-adding. No files were staged or committed.

## Handoff

The parent should independently inspect all eleven candidate source/crop/processed packages and decide whether the conditional rights evidence is sufficient, then obtain or record the required independent identity/framing/provenance review before invoking `convert_to_dds.py`, promoting any placeholder, or editing portrait-only `.gfx`/character references. User-supplied HOI4-style finals remain the user’s responsibility; RunPod was never opened or operated.

No claim of whole-event asset completion is made; the audit remains incomplete with the blockers above.
