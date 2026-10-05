# Event 006 catalog changes pending

The event catalog workbook is edited only by its owner. These are the Event 006 rows and fields that need updating from the implemented source; wording below is copied from the in-game localisation.

## 2026-10-04: foreign reactions (D3)

Disposition: `accepted and queued` for the catalog owner; implementation is committed.

New event rows (namespace `chaosx.nr6`):

| ID | Type | Title | Notes |
| --- | --- | --- | --- |
| `.64` | Hidden | (router) | Dispatches each foreign government's one reaction per wave; answers patron offers for AI new states |
| `.65` | Country | A New Neighbor | Neighbor profile: Watch the frontier / Recognize and open a liaison office / Sponsor border talks / Stand with the former host |
| `.66` | Country | A Shift in the Regional Balance | Regional profile: Withhold support / Guarantee its independence / Offer to mediate / Invest in the transit corridor |
| `.67` | Country | A Question of Precedent | Great-power profile: Abstain / Extend recognition and limited aid / Offer an arms channel / Organize containment |
| `.68` | Country | A Younger State | Earlier-wave profile: Stand aside / Recognize it and share our institutions / Send aid / Contest its standing |
| `.71` | Country | A Foreign Offer | New state answers a patron offer: Refuse the offer / Accept the offer / Accept a smaller arrangement |
| `.72` | Hidden | (deadline) | Closes a foreign reaction queue whose receipts outlived every answer |

Event details text: no change. The in-game Event Details text (`chaosx.events_log.window.event_details.independence_wave`) already says "Former hosts, neighboring powers, and rival movements decide whether to recognize or challenge them," which the foreign reactions now implement.

New Event 6 history entries (Event Log): recognition, guarantee, mediation, containment, aid; text in `localisation/english/006_independence_wave_foreign_reaction_l_english.yml` (`independence_wave.history.foreign.*`).

## 2026-10-04: remnant petitions (D4)

Disposition: `accepted and queued` for the catalog owner; implementation is committed.

| ID | Type | Title | Notes |
| --- | --- | --- | --- |
| `.69` | Country | A Petition for Protection | Recipient answers a remnant former host: Decline the petition / Guarantee the host |
| `.70` | Country | An Answer to Our Petition | Host learns whether the guarantee was given, declined or lapsed |

New decision for remnant former hosts: "Petition [recipient] for a Guarantee" in the category "A Foreign Guarantee".

New Event 6 history entry: remnant guarantee (`independence_wave.history.foreign.remnant_guarantee`).

## 2026-10-04: Iberian packages and FORM-07 (D7)

Disposition: `accepted and queued` for the catalog owner; implementation is committed.

- IW-013 Basque Country (NAV) and IW-015 Galicia (GLC) can now appear in Independence Waves.
- FORM-07 "Iberian Federation" can now be formed by CAT, NAV and GLC; the federation takes the name "Iberian Federation" and a new flag.

## 2026-10-04: Don Host package (D5)

Disposition: `accepted and queued` for the catalog owner; implementation is committed.

- IW-039 Don Host (DON) can now appear in Independence Waves, with Millerovo as its capital and Volgodonsk as optional territory; it never appears alongside Event 005's Don Host Republic, and it shares one wave slot with the Kuban package.

## 2026-10-04: SCN-008 failure result (D9)

Disposition: `accepted and queued` for the catalog owner; implementation is committed.

| ID | Type | Title | Notes |
| --- | --- | --- | --- |
| `chaosx.triggerable_scenarios.81` | Country | No Banner Rises | Sent to the launching player when an Every Banner Rises launch releases no country or is called off; one option "The old borders stand." |

- Basque Country (IW-013) and Galicia (IW-015) can now be chosen by ordinary Independence Waves, not only by the scenario.


## 2026-10-05: Middle Volga and Assyria packages (D13)

Disposition: `accepted and queued` for the catalog owner; implementation is committed.

- IW-043 Middle Volga (CHU) and IW-058 Assyria (ASY) can now appear in high-chaos Independence Waves and Every Banner Rises launches. Middle Volga never appears in the same wave as Tatarstan.
- Their federations FORM-12 "Volga-Ural Federation", FORM-13 "Idel-Ural" and FORM-18 "Mesopotamian Federation" can now be formed.
- Assyria's civic route is led by Mar Shimun XXI Eshai, its guardianship route by Mar Shimun with the Levies, and its popular route by Benjamin Arsanis.


## 2026-10-05: Package incidents (D15)

Disposition: `accepted and queued` for the catalog owner; implementation is committed.

New country events `chaosx.nr6.101` to `.142`, two for each of Scotland, Wales, Brittany, Catalonia, Transylvania, Macedonia, Bosnia, Karelia, Crimea, Ruthenia, Kuban, Tatarstan, Bashkiria, Armenia, Georgia, Azerbaijan, Hawaii, California, the Basque Country, Galicia and the Don Host. The first arrives about 45 days after a released country chooses its founding posture, the second about 150 days after the first is answered. Titles are listed in `docs/events/006_independence_wave/package_incidents.md`.


## 2026-10-05: Statehood incidents (D16)

Disposition: `accepted and queued` for the catalog owner; implementation is committed.

New country events `chaosx.nr6.151` to `.181` and the hidden pulse `chaosx.nr6.150`. Every released country now meets recurring incidents about every three to five months for as long as it survives: founding troubles (currency, clerks, railway junctions, refugees), recognition (envoys, conditional recognition, a failed vote), security (militias, defecting guards, officers), government (the constituent assembly, emergency rule, provincial councils, foreign-backed ministers), League business (arms requests, a motion for collective war, a rights charter) and union-building (flags, congress seats, a single command). Each evolution adds two or three incidents of its own. Titles are listed in `docs/events/006_independence_wave/statehood_incidents.md`.


## 2026-10-05: World milestones (D17)

Disposition: `accepted and queued` for the catalog owner; implementation is committed.

Ten one-time world news events (`chaosx.nr6.190` to `.199`) now mark the independence wave's turning points: the first new state received abroad as a full state, the first peaceful separation treaty, the first new state retaken by its former host, the first union of new states, the first rescue of a member by the League, the first League spanning three regions, the first radical bloc, ten and then twenty-five new states standing at once, and a one-province state becoming a great power. Each also appears in the Event Logs history. Titles are listed in `docs/events/006_independence_wave/milestones.md`.


## 2026-10-05: Asante and Sokoto packages (D19)

Disposition: `accepted and queued` for the catalog owner; implementation is committed.

- IW-093 Asante (DOX) and IW-098 Sokoto (SOK) can now appear in high-chaos Independence Waves, Join conversions and Every Banner Rises launches. They are the first Event 006 countries in West Africa.
- Asante is led by the Asantehene Prempeh II. Sokoto is led by Sultan Hasan dan Mu'azu until June 1938, when the new event "A New Sultan in Sokoto" (`chaosx.nr006.9811`) installs Siddiq Abubakar III.


## 2026-10-05: Volga and Siberian packages (D20)

Disposition: `accepted and queued` for the catalog owner; implementation is committed.

- Mari El (MEL), Udmurtia (UDM), Komi (KOM), Yakutia (YAK), Buryatia (BYA), Altai (ALT) and Khakassia (KHA) can now appear in Independence Waves, Join conversions and Every Banner Rises launches, each led by its own vanilla leaders.
- The Far Eastern Republic package remains unavailable.


## 2026-10-05: Fiji package (D21)

Disposition: `accepted and queued` for the catalog owner; implementation is committed.

- Fiji (FIJ) can now appear in Independence Waves, Join conversions and Every Banner Rises launches, led by Ratu Sir Lala Sukuna.
- Micronesia (FSM) remains unavailable, so the Pacific federation formable (FORM-48) cannot form yet.


## 2026-10-05: Kurdistan and Dahomey packages (D22)

Disposition: `accepted and queued` for the catalog owner; implementation is committed.

- Kurdistan (KUR) can now appear in Independence Waves, Join conversions and Every Banner Rises launches, released from Iran around Sanandaj and led by its own vanilla leaders.
- Dahomey (DAH) can now appear in the same launches, led by its vanilla government.


## 2026-10-05: Danubian Confederation formable (D23)

Disposition: `accepted and queued` for the catalog owner; implementation is committed.

- Transylvania and the Banat can now form the Danubian Confederation together, under its own name and flag.


## 2026-10-05: Cossack Host Federation formable (D24)

Disposition: `accepted and queued` for the catalog owner; implementation is committed.

- The Don and Kuban hosts, released in different waves, can now form the Cossack Host Federation together under its own name and flag, with a charter that balances civilian control, cavalry integration and the rights of non-Cossack residents. Rostov stays outside the federation.
- Countries invited to the Danubian Confederation, the Balkan Federation, the Volga-Ural and Idel-Ural federations and the Mesopotamian Federation can now answer their invitations, and released Balkan countries can now join or lead the Balkan Federation.


## 2026-10-05: Levant and Arabia packages (D25)

Disposition: `accepted and queued` for the catalog owner; implementation is committed.

- The Hejaz, Hadhramaut, the Imamate of Oman, Lebanon and Palestine can now appear in Independence Waves, Join conversions and Every Banner Rises launches.
- The Hejaz, the Imamate of Oman, Lebanon and Palestine each have a starting problem, their own decisions and two incidents of their own.
- Najd, Jabal Shammar, Mahra, Jabal al-Druze and the Syrian coast remain unavailable.


## 2026-10-05: North Africa and Sahara packages (D26)

Disposition: `accepted and queued` for the catalog owner; implementation is committed.

- The Rif and Tripolitania can now appear in Independence Waves, Join conversions and Every Banner Rises launches.
- The Rif has a starting problem, its own decisions and two incidents of its own.
- Kabylia, Fezzan, the Tuareg confederation, Darfur, Wadai, the Toubou state and the Amazigh Atlas state remain unavailable.


## 2026-10-05: West and Central Africa packages (D27)

Disposition: `accepted and queued` for the catalog owner; implementation is committed.

- Oyo, Kanem-Bornu, the Aro Confederacy and the Biafran regional state can now appear in Independence Waves, Join conversions and Every Banner Rises launches; a wave releases at most one Nigerian country.
- Oyo and Kanem-Bornu each have a starting problem, their own decisions and two incidents of their own.
- Fante, the Benin Kingdom, the Hausa Federation, Luba and Lunda remain unavailable.


## 2026-10-05: East Africa, Horn and Great Lakes packages (D28)

Disposition: `accepted and queued` for the catalog owner; implementation is committed.

- Buganda, Rwanda, Burundi, Harar, the Afar state, Somaliland and Tigray can now appear in Independence Waves, Join conversions and Every Banner Rises launches.
- Buganda, Rwanda, Burundi, Harar, Somaliland and Tigray each have a starting problem, their own decisions and two incidents of their own.
- Bunyoro, Ankole, Zanzibar, Kilwa, the Maasai regional state and the Oromo regional federation remain unavailable.


## 2026-10-05: Southern Africa and Indian Ocean packages (D29)

Disposition: `accepted and queued` for the catalog owner; implementation is committed.

- Barotseland, Madagascar, the Comoros and Mauritius can now appear in Independence Waves, Join conversions and Every Banner Rises launches.
- Barotseland and Madagascar each have a starting problem, their own decisions and two incidents of their own.
- The Hejaz, Hadhramaut, Tripolitania, Oyo, Kanem-Bornu, the Aro Confederacy, the Comoros and Mauritius open under a named council of their own.
- The Zulu, Ndebele, Xhosa, Basotho, Eswatini, Herero, Nama and Ovambo states remain unavailable.


## 2026-10-05: South Asia and Himalaya packages (D30)

Disposition: `accepted and queued` for the catalog owner; implementation is committed.

- Punjab, Sindh, Balochistan, Pashtunistan, Kashmir, Hyderabad, Mysore, the Madras States, Assam, Manipur and Sikkim can now appear in Independence Waves, Join conversions and Every Banner Rises launches.
- Every one of them except Sikkim has a starting problem, its own decisions and two incidents of its own; Punjab and Assam open under their legislative assemblies.
- Bengal, Khalistan, Travancore, the Dravidian Federation, the Naga state and the Himalayan Confederation remain unavailable.


## 2026-10-05: Southeast Asia, East Asia and Oceania packages (D31)

Disposition: `accepted and queued` for the catalog owner; implementation is committed.

- Aceh, Minangkabau, the Bugis state, Bali, the Shan federation, Mon State, the Kachin state, Laos, Champa, East Turkestan, Inner Mongolia, Ryukyu and Samoa can now appear in Independence Waves, Join conversions and Every Banner Rises launches.
- Every one of them except the Bugis state and Champa has a starting problem, its own decisions and two incidents of its own; the six new custom states open under a named council.
- Riau, Pattani, the Dayak, Karen, Chin, Hmong, Arakan, Wa, Ainu, Aotearoa Maori, Papuan, West Papuan and Tongan states and the Moluccan federation remain unavailable.


## 2026-10-05: Americas packages (D32)

Disposition: `accepted and queued` for the catalog owner; implementation is committed.

- Quebec, Newfoundland, Texas, Yucatan, the Guarani state and the Patagonian state can now appear in Independence Waves, Join conversions and Every Banner Rises launches.
- Quebec, Newfoundland, Texas and Yucatan each have a starting problem, their own decisions and two incidents of their own; Newfoundland, Texas and Patagonia open under a named assembly or congress.
- Acadia, Cascadia, the Cherokee, Haudenosaunee, Lakota, Dine, Pueblo, Maya, Oaxaca, Miskito, Garifuna, Aymara, Quechua, Muisca, Gran Chaco, Amazonian and Maroon states remain unavailable.


## 2026-10-05: Europe, Persia and Caucasus packages (D33)

Disposition: `accepted and queued` for the catalog owner; implementation is committed.

- Occitania, Venice, the Trieste Free State, Courland, Polesia, Galicia-Lodomeria, Khuzestan, Circassia, Chechnya and Dagestan can now appear in Independence Waves, Join conversions and Every Banner Rises launches.
- Venice, Circassia, Chechnya and Dagestan each have a starting problem, their own decisions and two incidents of their own; the six new custom states open under a named assembly or council.
- Khuzestan completes the membership of the Council of Communities formable.
- Cornwall, the Faroe Islands, Slavonia, Ingria, Chuvashia, Mordovia, the Nenets and Evenk states, the Far Eastern Republic, Luristan, Bakhtiari, Lazistan, Pontus and Cilicia remain unavailable.
