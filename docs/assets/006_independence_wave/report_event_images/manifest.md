# Event 006 Independence Wave Report Event Image Manifest

Package scope: bounded sourced report event image package for Event 006 Independence Wave only.

Current status: wired. `interface/006_independence_wave_report_event_images.gfx` exists and the current Event 006 report-event DDS texture references resolve. This package is not a current playable-wrap-up blocker; later package-specific report variants are optional future polish.

Reference inspection completed:
- `.agents/skills/chaos-redux-event-assets/assets/report_event_images/report_event_soldiers_marching.png`
- `.agents/skills/chaos-redux-event-assets/assets/report_event_images/report_event_soldiers_parade.png`
- `gfx/event_pictures/_report_event_template.psd`

DDS conversion note:
- Local conversion used `convert -define dds:compression=none`.
- Final DDS files validate locally at `210x176`.
- `file` reports each final DDS as `Microsoft DirectDraw Surface (DDS): 210 x 176, 32-bit color, ARGB8888`.

Report processing note:
- This tranche used sourced archival imagery only.
- Photoshop template placement was not used in this pass. Local ImageMagick processing handled crop, tonal shaping, mild sepia treatment, border/shadow treatment, PNG export, and DDS conversion.
- This deviation is intentional and documented rather than hidden.

No-flag note:
- No country flag files were created or modified in this tranche.
- The selected final thirteen non-strange report images do not require any new or edited flag assets.

## Assets

### `GFX_report_event_independence_wave_petitions`
- Asset type: report event image
- Intended in-game use: Event 006 Independence Wave petition / recognition pressure beat
- Related event id: `006`
- Related event slug: `independence_wave`
- Source mode: sourced archival image
- Source page: `https://www.loc.gov/pictures/item/2016889537/`
- Source download: `https://cdn.loc.gov/service/pnp/hec/35600/35624v.jpg`
- Author / archive: Harris & Ewing, Library of Congress Prints and Photographs Division
- License / rights: no known restrictions on publication
- Source date: `[1929 December]`
- Event006 fit: mass petition presentation with officials, baskets of signed petitions, and a large civic crowd reads as a coordinated independence-petition push without leaning on Event005 collapse imagery
- Source file: `docs/assets/006_independence_wave/report_event_images/source/report_event_independence_wave_petitions_source_loc_hec35624.jpg`
- Processed PNG: `docs/assets/006_independence_wave/report_event_images/processed_png/report_event_independence_wave_petitions.png`
- Final DDS: `gfx/event_pictures/report_event_independence_wave_petitions.dds`
- Target size: `210x176`
- Sprite name: `GFX_report_event_independence_wave_petitions`
- Asset status: `complete`
- Uncertainty: earlier than 1936, but period-compatible public-domain civic petition imagery and visually appropriate for HOI4 report art

### `GFX_report_event_independence_wave_suppression`
- Asset type: report event image
- Intended in-game use: Event 006 Independence Wave suppression / street security beat
- Related event id: `006`
- Related event slug: `independence_wave`
- Source mode: sourced archival image
- Source page: `https://www.loc.gov/pictures/item/2008677085/`
- Source download: `https://tile.loc.gov/storage-services/service/pnp/ppmsca/15500/15597r.jpg`
- Author / archive: Tina Modotti, Library of Congress Prints and Photographs Division
- License / rights: no known restrictions on publication
- Source date: `1929 May`
- Event006 fit: police with rifles moving against a rally crowd reads cleanly as assembly suppression and street-security enforcement rather than battle art
- Source file: `docs/assets/006_independence_wave/report_event_images/source/report_event_independence_wave_suppression_source_loc_ppmsca15597.jpg`
- Processed PNG: `docs/assets/006_independence_wave/report_event_images/processed_png/report_event_independence_wave_suppression.png`
- Final DDS: `gfx/event_pictures/report_event_independence_wave_suppression.dds`
- Target size: `210x176`
- Sprite name: `GFX_report_event_independence_wave_suppression`
- Asset status: `complete`
- Uncertainty: earlier than 1936, but period-compatible and visually aligned with civic suppression; the original source carried handwritten caption text, so the final crop was tightened to remove it

### `GFX_report_event_independence_wave_observers`
- Asset type: report event image
- Intended in-game use: Event 006 Independence Wave observers / commission room beat
- Related event id: `006`
- Related event slug: `independence_wave`
- Source mode: sourced archival image
- Source page: `https://commons.wikimedia.org/wiki/File:Potsdam_conference_1945-8.jpg`
- Source download: `https://commons.wikimedia.org/wiki/Special:FilePath/Potsdam%20conference%201945-8.jpg`
- Author / archive: Army Signal Corps Collection in the U.S. National Archives; Wikimedia Commons host copy
- License / rights: public domain U.S. federal government work; Public Domain Mark 1.0 on Commons host copy
- Source date: `~July 1945`
- Event006 fit: seated principals and standing foreign ministers/advisors read as a formal observer or commission setting for outside scrutiny of new-state negotiations
- Source file: `docs/assets/006_independence_wave/report_event_images/source/report_event_independence_wave_observers_source_potsdam_conference_1945_8.jpg`
- Processed PNG: `docs/assets/006_independence_wave/report_event_images/processed_png/report_event_independence_wave_observers.png`
- Final DDS: `gfx/event_pictures/report_event_independence_wave_observers.dds`
- Target size: `210x176`
- Sprite name: `GFX_report_event_independence_wave_observers`
- Asset status: `complete`
- Uncertainty: the scene is a high-level diplomatic conference rather than literal field journalists or checkpoint inspectors, so it is a commission-room interpretation of the brief

### `GFX_report_event_independence_wave_release`
- Asset type: report event image
- Intended in-game use: Event 006 Independence Wave release / independence ceremony beat
- Related event id: `006`
- Related event slug: `independence_wave`
- Source mode: sourced archival image
- Source page: `https://commons.wikimedia.org/wiki/File:Indonesia_declaration_of_independence_17_August_1945_(cropped).jpg`
- Source download: `https://commons.wikimedia.org/wiki/Special:FilePath/Indonesia%20declaration%20of%20independence%2017%20August%201945%20(cropped).jpg`
- Author / archive: Frans Mendur; Wikimedia Commons host copy attributed to Presidential Documents / National Library of Indonesia source trail
- License / rights: public domain in Indonesia; public domain in the United States under Commons `PD Indonesia Old` / `PD-1996`
- Source date: `17 August 1945`
- Event006 fit: formal proclamation scene reads as an independence ceremony or oath-like release moment without relying on Soviet-collapse framing
- Source file: `docs/assets/006_independence_wave/report_event_images/source/report_event_independence_wave_release_source_indonesia_declaration_1945_cropped.jpg`
- Processed PNG: `docs/assets/006_independence_wave/report_event_images/processed_png/report_event_independence_wave_release.png`
- Final DDS: `gfx/event_pictures/report_event_independence_wave_release.dds`
- Target size: `210x176`
- Sprite name: `GFX_report_event_independence_wave_release`
- Asset status: `complete`
- Uncertainty: source scan is contrast-limited, so fine facial detail is softer than ideal at full resolution; the proclamation framing still reads clearly at report-event size

### `GFX_report_event_independence_wave_committee`
- Asset type: report event image
- Intended in-game use: Event 006 Independence Wave committee-formation beat
- Related event id: `006`
- Related event slug: `independence_wave`
- Source mode: sourced archival image
- Source page: `https://commons.wikimedia.org/wiki/File:Lot-1945-2_(34595887332).jpg`
- Source download: `https://commons.wikimedia.org/wiki/Special:FilePath/Lot-1945-2%20(34595887332).jpg`
- Author / archive: National Museum of the U.S. Navy Flickr upload of an Office of War Information home-front committee photo, courtesy of the Library of Congress
- License / rights: Public Domain Mark review on Commons host copy; `PD-USGov-Military-Navy` on Commons page
- Source date: `1 October 1942` for the photographed committee meeting; Commons upload date `2017-05-19`
- Event006 fit: a crowded table of civilian committee members reads cleanly as provisional committees forming in improvised civic rooms
- Origin specificity: U.S. wartime labor-policy committee rather than a literal independence committee
- Source file: `docs/assets/006_independence_wave/report_event_images/source/report_event_independence_wave_committee_source_womens_policy_committee_1942.jpg`
- Processed PNG: `docs/assets/006_independence_wave/report_event_images/processed_png/report_event_independence_wave_committee.png`
- Final DDS: `gfx/event_pictures/report_event_independence_wave_committee.dds`
- Target size: `210x176`
- Sprite name: `GFX_report_event_independence_wave_committee`
- Asset status: `complete`
- Uncertainty: representative committee-room imagery rather than a sovereignty committee; still period-safe and visually exact to the brief

### `GFX_report_event_independence_wave_negotiation`
- Asset type: report event image
- Intended in-game use: Event 006 Independence Wave negotiation / talks beat
- Related event id: `006`
- Related event slug: `independence_wave`
- Source mode: sourced archival image
- Source page: `https://commons.wikimedia.org/wiki/File:80-G-347701.jpg`
- Source download: `https://commons.wikimedia.org/wiki/Special:FilePath/80-G-347701.jpg`
- Author / archive: Official U.S. Navy photo `80-G-347701`; Commons host copy from Naval History and Heritage Command source page
- License / rights: `PD-USGov-Military-Navy`
- Source date: `1945-09-09`
- Event006 fit: a guarded surrender table inside a formal chamber reads as hard-edged negotiations under military pressure
- Origin specificity: Japanese surrender ceremony in Seoul rather than a civilian independence negotiation
- Source file: `docs/assets/006_independence_wave/report_event_images/source/report_event_independence_wave_negotiation_source_seoul_surrender_1945.jpg`
- Processed PNG: `docs/assets/006_independence_wave/report_event_images/processed_png/report_event_independence_wave_negotiation.png`
- Final DDS: `gfx/event_pictures/report_event_independence_wave_negotiation.dds`
- Target size: `210x176`
- Sprite name: `GFX_report_event_independence_wave_negotiation`
- Asset status: `complete`
- Uncertainty: the source is a surrender ceremony, so the mood is harsher than an ordinary conference-table compromise

### `GFX_report_event_independence_wave_league`
- Asset type: report event image
- Intended in-game use: Event 006 league / council / congress beat
- Related event id: `006`
- Related event slug: `independence_wave`
- Source mode: sourced archival image
- Source page: `https://commons.wikimedia.org/wiki/File:UnitedNationsconference.jpg`
- Source download: `https://commons.wikimedia.org/wiki/Special:FilePath/UnitedNationsconference.jpg`
- Author / archive: unknown photographer; Truman Library source trail via Commons host copy
- License / rights: `PD-USGov`
- Source date: `1945-06-26`
- Event006 fit: a formal dais with delegates, guards, and national flags reads as a league or congress chamber for small-state recognition politics
- Origin specificity: United Nations Conference opening scene rather than a literal small-state league
- Source file: `docs/assets/006_independence_wave/report_event_images/source/report_event_independence_wave_league_source_un_conference_1945.jpg`
- Processed PNG: `docs/assets/006_independence_wave/report_event_images/processed_png/report_event_independence_wave_league.png`
- Final DDS: `gfx/event_pictures/report_event_independence_wave_league.dds`
- Target size: `210x176`
- Sprite name: `GFX_report_event_independence_wave_league`
- Asset status: `complete`
- Uncertainty: the image centers a speech podium rather than delegates seated around a smaller council table

### `GFX_report_event_independence_wave_border_commission`
- Asset type: report event image
- Intended in-game use: Event 006 border commission / map-table arbitration beat
- Related event id: `006`
- Related event slug: `independence_wave`
- Source mode: sourced archival image
- Source page: `https://commons.wikimedia.org/wiki/File:8th_Air_Force_officers_inspect_map_(204882163).jpg`
- Source download: `https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/8th_Air_Force_officers_inspect_map_%28204882163%29.jpg/1280px-8th_Air_Force_officers_inspect_map_%28204882163%29.jpg`
- Author / archive: United States Army Air Forces; NARA image `204882163` via Commons host copy
- License / rights: `PD-scan` of `PD-USGov-Military-Army`
- Source date: `between 1944 and 1945`
- Event006 fit: three officers over a route map gives a strong survey, frontier, and arbitration-map reading at report-event scale
- Origin specificity: air-force operations map in England rather than a literal boundary commission
- Source file: `docs/assets/006_independence_wave/report_event_images/source/report_event_independence_wave_border_commission_source_8th_air_force_map_1944_1945.jpg`
- Processed PNG: `docs/assets/006_independence_wave/report_event_images/processed_png/report_event_independence_wave_border_commission.png`
- Final DDS: `gfx/event_pictures/report_event_independence_wave_border_commission.dds`
- Target size: `210x176`
- Sprite name: `GFX_report_event_independence_wave_border_commission`
- Asset status: `complete`
- Uncertainty: saved source file uses the 1280px Commons derivative after direct original-file fetches were rate-limited; still comfortably above target resolution

### `GFX_report_event_independence_wave_patron_brokers`
- Asset type: report event image
- Intended in-game use: Event 006 patron-brokers / foreign financial negotiation beat
- Related event id: `006`
- Related event slug: `independence_wave`
- Source mode: sourced archival image
- Source page: `https://commons.wikimedia.org/wiki/File:WhiteandKeynes.jpg`
- Source download: `https://commons.wikimedia.org/wiki/Special:FilePath/WhiteandKeynes.jpg`
- Author / archive: International Monetary Fund
- License / rights: `PD-imf.org`
- Source date: `1946-03-08`
- Event006 fit: Harry Dexter White and John Maynard Keynes provide a clean foreign-finance and outside-broker reading for patron negotiations
- Origin specificity: IMF inaugural meeting in Savannah rather than an embassy office scene
- Source file: `docs/assets/006_independence_wave/report_event_images/source/report_event_independence_wave_patron_brokers_source_white_keynes_1946.jpg`
- Processed PNG: `docs/assets/006_independence_wave/report_event_images/processed_png/report_event_independence_wave_patron_brokers.png`
- Final DDS: `gfx/event_pictures/report_event_independence_wave_patron_brokers.dds`
- Target size: `210x176`
- Sprite name: `GFX_report_event_independence_wave_patron_brokers`
- Asset status: `complete`
- Uncertainty: slightly postwar and more monetary than embassy-office in tone, but still a strong near-period patron-broker fit

### `GFX_report_event_independence_wave_old_name`
- Asset type: report event image
- Intended in-game use: Event 006 old-name / archival treaty-claim beat
- Related event id: `006`
- Related event slug: `independence_wave`
- Source mode: sourced archival image
- Source page: `https://www.loc.gov/pictures/item/2016870852/`
- Source download: `https://cdn.loc.gov/service/pnp/hec/13400/13494v.jpg`
- Author / archive: Library of Congress Prints and Photographs Division
- License / rights: historical document scan from Library of Congress; explicit rights statement was not captured in this tranche, so rights should be treated as public-domain-likely but recorded with uncertainty
- Source date: `1814-12-24`
- Event006 fit: treaty signatures with hanging wax seals read immediately as archival legitimacy, old compacts, and antique state-name claims
- Origin specificity: Treaty of Ghent signatures rather than a region-specific old-name dossier
- Source file: `docs/assets/006_independence_wave/report_event_images/source/report_event_independence_wave_old_name_source_treaty_of_ghent_signatures_1814.jpg`
- Processed PNG: `docs/assets/006_independence_wave/report_event_images/processed_png/report_event_independence_wave_old_name.png`
- Final DDS: `gfx/event_pictures/report_event_independence_wave_old_name.dds`
- Target size: `210x176`
- Sprite name: `GFX_report_event_independence_wave_old_name`
- Asset status: `complete`
- Uncertainty: well outside the 1936-1945 window, but the brief explicitly called for archive, seal, treaty-desk, and antiquities material; rights note should be user-reviewed if stricter provenance wording is required

### `GFX_report_event_independence_wave_local_polity`
- Asset type: report event image
- Intended in-game use: Event 006 local-polity / community assembly beat
- Related event id: `006`
- Related event slug: `independence_wave`
- Source mode: sourced archival image
- Source page: `https://commons.wikimedia.org/wiki/File:Officials_at_a_Tribal_Council_meeting_-_NARA_-_295176.jpg`
- Source download: `https://commons.wikimedia.org/wiki/Special:FilePath/Officials%20at%20a%20Tribal%20Council%20meeting%20-%20NARA%20-%20295176.jpg`
- Author / archive: U.S. National Archives, Record Group 75, Bureau of Indian Affairs, Navajo Area Office
- License / rights: `PD-USGov`
- Source date: `undated in record; file unit spans ca. 1934-ca. 1951`
- Event006 fit: a formal community-floor council gives a respectful local-court or land-council reading without caricature
- Origin specificity: Navajo tribal council setting rather than one of Event006's specific local-polity packages
- Source file: `docs/assets/006_independence_wave/report_event_images/source/report_event_independence_wave_local_polity_source_tribal_council_nara_295176.jpg`
- Processed PNG: `docs/assets/006_independence_wave/report_event_images/processed_png/report_event_independence_wave_local_polity.png`
- Final DDS: `gfx/event_pictures/report_event_independence_wave_local_polity.dds`
- Target size: `210x176`
- Sprite name: `GFX_report_event_independence_wave_local_polity`
- Asset status: `complete`
- Uncertainty: exact date is not stated on the NARA page and the source is region-specific, so it should be read as respectful documentary stand-in imagery

### `GFX_report_event_independence_wave_host_rump`
- Asset type: report event image
- Intended in-game use: Event 006 host-rump / pressured capital cabinet beat
- Related event id: `006`
- Related event slug: `independence_wave`
- Source mode: sourced archival image
- Source page: `https://commons.wikimedia.org/wiki/File:Photograph_of_Truman_Cabinet_meeting_at_the_White_House_-_NARA_-_199145.jpg`
- Source download: `https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Photograph_of_Truman_Cabinet_meeting_at_the_White_House_-_NARA_-_199145.jpg/1280px-Photograph_of_Truman_Cabinet_meeting_at_the_White_House_-_NARA_-_199145.jpg`
- Author / archive: Abbie Rowe via Harry S. Truman Library / NARA Commons host copy
- License / rights: `PD-USGov`
- Source date: `1945-08-10`
- Event006 fit: a full cabinet table under wartime administrative pressure reads cleanly as the rump-state capital trying to hold together
- Origin specificity: Truman cabinet meeting rather than a collapsing host government
- Source file: `docs/assets/006_independence_wave/report_event_images/source/report_event_independence_wave_host_rump_source_truman_cabinet_1945.jpg`
- Processed PNG: `docs/assets/006_independence_wave/report_event_images/processed_png/report_event_independence_wave_host_rump.png`
- Final DDS: `gfx/event_pictures/report_event_independence_wave_host_rump.dds`
- Target size: `210x176`
- Sprite name: `GFX_report_event_independence_wave_host_rump`
- Asset status: `complete`
- Uncertainty: saved source file uses the 1280px Commons derivative after direct original-file fetches were rate-limited; scene shows a functioning cabinet rather than overt panic

### `GFX_report_event_independence_wave_failed_wave`
- Asset type: report event image
- Intended in-game use: Event 006 failed-wave / abandoned petition and press-wire beat
- Related event id: `006`
- Related event slug: `independence_wave`
- Source mode: sourced archival image
- Source page: `https://commons.wikimedia.org/wiki/File:Wire_room_of_the_New_York_Times_newspaper._8d22682v.jpg`
- Source download: `https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Wire_room_of_the_New_York_Times_newspaper._8d22682v.jpg/1280px-Wire_room_of_the_New_York_Times_newspaper._8d22682v.jpg`
- Author / archive: Marjory Collins; Library of Congress FSA/OWI collection via Commons host copy
- License / rights: no known restrictions; LOC FSA/OWI rights advisory mirrored on Commons
- Source date: `1942-09`
- Event006 fit: the wire-room printout and bare machinery read as paperwork, dispatches, and initiatives reduced to file traffic rather than public triumph
- Origin specificity: newspaper wire room rather than a literal shuttered nationalist office
- Source file: `docs/assets/006_independence_wave/report_event_images/source/report_event_independence_wave_failed_wave_source_nyt_wire_room_1942.jpg`
- Processed PNG: `docs/assets/006_independence_wave/report_event_images/processed_png/report_event_independence_wave_failed_wave.png`
- Final DDS: `gfx/event_pictures/report_event_independence_wave_failed_wave.dds`
- Target size: `210x176`
- Sprite name: `GFX_report_event_independence_wave_failed_wave`
- Asset status: `complete`
- Uncertainty: saved source file uses the 1280px Commons derivative after direct original-file fetches were rate-limited; the image implies stalled paper traffic rather than a visibly abandoned petition office

### `GFX_report_event_independence_wave_impossible_state`
- Asset type: report event image
- Intended in-game use: Event 006 impossible-state / strange release warning beat
- Related event id: `006`
- Related event slug: `independence_wave`
- Source mode: generated symbolic documentary image
- Generation prompt reference: `docs/assets/006_independence_wave/report_event_images/prompts/report_event_independence_wave_impossible_state_prompt.txt`
- Generation contact sheet: `docs/assets/006_independence_wave/report_event_images/contact_sheets/report_event_independence_wave_impossible_state_contact_sheet.png`
- Event006 fit: an empty ministry file room, abstract registry ledger, and nested impossible border map frame the horror as state paperwork, borders, and citizenship logic rather than combat or occult spectacle
- Origin specificity: specific to Event 006 strange-state dossier logic and intentionally separate from Event 005 collapse presentation
- Source file: `docs/assets/006_independence_wave/report_event_images/source/report_event_independence_wave_impossible_state_source.png`
- Processed PNG: `docs/assets/006_independence_wave/report_event_images/processed_png/report_event_independence_wave_impossible_state.png`
- Final DDS: `gfx/event_pictures/report_event_independence_wave_impossible_state.dds`
- Target size: `210x176`
- Sprite name: `GFX_report_event_independence_wave_impossible_state`
- Asset status: `complete`
- Uncertainty: `needs_user_review` only for subjective tone choice between the three generated variants; the selected final image avoids readable text and modern props, but generated filing-box labels remain tiny abstract marks rather than fully blank surfaces
