# Event 093 source and decision register

## Authority and scope

U1, the current user brief preserved in this package, controls the event's identity and requested gameplay. The supplied project instructions and planning skills govern the work method. The supplied catalogs are read-only snapshots of earlier repository state. Inspected repository files establish what was actually present at the pinned revision. Public historical sources inform the inspiration, not the exact modern game rule. New mechanics and numbers in the specification are proposed design decisions.

The original ZIP is `all-project-sources(20261002-180931).zip`. Its nested `subagents.zip` contains 20 readable role definitions. All 46 text files were read in full before specification drafting. The detailed source manifest and reading report identify them individually. No linked library or entire external repository is implied by that count.

## U1: current brief

The user specifies Event 093, the Galicia opening, a live Spanish Civil War bargain, persistent relationship consequences, four ordered evolutions, a dynamic geographic partition, faster regional integration, the exact faction name, and a two-sided world-end above 1000 Chaos. The current brief overrides the old catalog's Galicia-only description and absent cluster assignment.

## S: supplied project sources

The 46 S-series source IDs are assigned in the source manifest in sorted path order. They include AGENTS.md, CHAOS_REDUX_MECHANICS.md, README.md, all supplied skills, three complete CSV snapshots, shared helper documentation, config.toml, and all 20 role definitions. The manifest contains exact relative paths, hashes, line counts, and reading ranges.

The text files were actually read. Extraction, hashing, and the mechanically checked range manifest are supporting audit artifacts, not a substitute for reading. Early oversized output that was truncated was reread through bounded complete chunks.

## R1: legacy Galicia event

Path: `events/093_portugal_galicia.txt`.

Repository revision: `5212636eef9f9607691ddc1348bddade1bafe0dd`.

Blob SHA: `19163ed24cf7038455849a2ae6db3fc5db282f11`.

Source: `https://github.com/klimPaskov/Chaos-Redux/blob/5212636eef9f9607691ddc1348bddade1bafe0dd/events/093_portugal_galicia.txt`.

Fully fetched and read. The root is `chaosx.nr93.1`. The old event immediately gives Portugal a core on state 171, then asks the owner to accept or refuse. Its refusal branch can make Portugal declare a take-core-state war from the owner's response. The new design preserves the root identity while replacing those behaviors. State 171 is legacy evidence, not an approved universal map resolver.

## R2: legacy Galicia localization

Path: `localisation/english/093_portugal_galicia_l_english.yml`.

Blob SHA: `955ccd2715eacfd00f5fd4c91b20605b525d5a46` at the same revision.

Source: `https://github.com/klimPaskov/Chaos-Redux/blob/5212636eef9f9607691ddc1348bddade1bafe0dd/localisation/english/093_portugal_galicia_l_english.yml`.

Fully fetched and read. The main report descriptions are empty. The news wording and country-scope chain need replacement or review for the actual outcome. This is evidence of unfinished old content, not permission to copy its exact final strings into the new design.

## R3: actual World Claims implementation

Path: `events/086_world_claims.txt`.

Blob SHA: `3756bb7b2f33a10c5f8afba2d567fb4e9345f68d` at the same revision.

Source: `https://github.com/klimPaskov/Chaos-Redux/blob/5212636eef9f9607691ddc1348bddade1bafe0dd/events/086_world_claims.txt`.

Fully fetched and read. The current inspected script selects Germany and grants claims on every state. It does not implement the newer neighboring-claims design discussed in the project. Event 093's compatibility must preserve source ownership without assuming that later rework is already present.

## R4: universal discounted-cost framework

Path: `docs/systems/universal_cost_modifier.md`.

Blob SHA: `f053e8d76ef5d7232fd622a18b7ae7d9faa77e83` at the same revision.

Source: `https://github.com/klimPaskov/Chaos-Redux/blob/5212636eef9f9607691ddc1348bddade1bafe0dd/docs/systems/universal_cost_modifier.md`.

Fully fetched and read. The contract separates current quotes, affordability, actual debits, receipts, refunds, and settlement. It explicitly does not establish universal coverage or live consumer proof. This specification therefore requires real owner adapters and actual-paid refunds, especially for multi-resource actions.

## Repository excerpts that were not whole-file reads

Search results identified the Galicia picture mapping in `interface/chaosx_pictures.gfx` and the related news section in `events/_chaosx_news.txt`. Only those search excerpts were inspected. Neither complete file, the actual DDS, the entire event engine, nor the entire repository was read. These excerpts establish leads for implementation inspection, not completed asset or scope validation.

## H1: Treaty of Tordesillas primary text

Source: Yale Law School, Avalon Project, translation of the treaty of 7 June 1494, reproduced from Frances Gardiner Davenport's 1917 collection.

URL: `https://avalon.law.yale.edu/15th_century/mod001.asp`.

Accessed 2 October 2026. The treaty text's relevant boundary, mutual survey, restitution, and transit provisions were read. It places a north-south boundary 370 leagues west of Cape Verde, with Portuguese and Castilian sides. The public transcription contains an apparent 'degrees' error in one later passage, so that isolated wording is not used to define the game's line.

One verified short quote candidate is “for the sake of peace and concord”, from Article I. It is a research candidate, not approved final localization. The other quote directions are paraphrases of the reciprocal-return and joint-survey provisions. No broader historical quotation is reproduced here.

## H2: Treaty of Saragossa primary-text reproduction

Source: Davenport, European Treaties Bearing on the History of the United States and its Dependencies to 1648, Document 16, reproduced on Wikisource.

URL: `https://en.wikisource.org/wiki/European_Treaties_bearing_on_the_History_of_the_United_States_and_its_Dependencies_to_1648/Treaty_of_Saragossa`.

Accessed 2 October 2026. The introduction and relevant settlement and boundary passages were read, not the entire collection. The dated agreement is 22 April 1529 and addresses the competing Asian claims. It must not be represented as a simple verified antipode of the event's chosen Atlantic line. The exact 46.5 degrees west and 133.5 degrees east pair is a game-design convention.

## H3: Portuguese non-intervention declaration context

Source: U.S. Department of State, Foreign Relations of the United States, 1936, volume II, document 446, dated 27 August 1936.

URL: `https://history.state.gov/historicaldocuments/frus1936v02/d446`.

Accessed 2 October 2026. The short primary telegram concerning Portuguese restrictions on exports and transit to Spain was inspected. It supports diplomatic non-intervention pressure as context. It is not proof that Portugal made a historical Galicia-for-aid bargain. That bargain is the user's fictional event premise.

## A1: Portuguese musical reference

Source page: `https://commons.wikimedia.org/wiki/File:A_Portuguesa.ogg`.

The file page identifies Alfredo Keil's composition and a U.S. Navy Band performance, and displays composition and performance public-domain notices. Summary, licensing, source links, and file metadata were inspected on 2 October 2026. This is a preliminary reference. No listening, excerpt selection, production-rights clearance, or repository uniqueness check was performed.

## A2: Spanish musical reference

Source page: `https://commons.wikimedia.org/wiki/File:Marcha_Real-Royal_March_by_US_Navy_Band.ogg`.

The page identifies the composition and U.S. Navy Band performance separately and provides licensing notices and an archived source link. Relevant metadata and licensing sections were inspected on 2 October 2026. Arrangement details, route-appropriate use, actual sound, and reuse remain unverified. This recording is not selected as final audio.

## Other research boundaries

Searches also surfaced museum descriptions, secondary treaty explanations, and literary or audio leads. Only the sources above are used as load-bearing research. A Camões translation was searched but no verified final literary quote was selected, and the complete book was not read. The actual historical documents' dates must not be confused with the date of this fictional twentieth-century restoration.

## Accepted design decisions for this draft

| ID | Decision | Basis and consequence |
| --- | --- | --- |
| D01 | Keep the opening local and complete | U1, Galicia remains playable without later evolution |
| D02 | Replace immediate Portuguese core with a claim | U1 plus R1 correction, later integration remains meaningful |
| D03 | Portugal chooses its own escalation | U1 plus R1 correction, no forced war from Spain's response |
| D04 | One live assistance contract with actual delivery | U1, avoids promises or dead tags granting territory |
| D05 | Earned obligation differs from unearned renegotiation | New explicit design, makes contribution matter |
| D06 | Confidence cannot erase a breach | U1 and planning skill, diplomacy remains political |
| D07 | Preserve two sovereign powers and existing identities | U1, no automatic union or replacement trees |
| D08 | Use an explicit two-meridian game convention | U1 plus H1/H2, avoids false historical precision |
| D09 | Generate state assignments from actual geography | U1, no modern-country partition list |
| D10 | Protect fixed metropolitan sets and special Galicia | U1, prevents mutual homeland claims and core farming |
| D11 | Regions integrate in batches | U1, faster path without per-state repetition |
| D12 | Conquest and integration are separately necessary | U1, no token second crown in the world-end |
| D13 | Freeze readiness weights at activation | New anti-exploit rule, losses and construction cannot shrink or manufacture the task |
| D14 | Count existing legitimate cores but not false project achievements | Cross-system compatibility, no unnecessary removal of other systems' results |
| D15 | Respect legal ownership and donor consent in restitution | U1 plus H1 inspiration, occupation is not ownership |
| D16 | One native patron per subject | Required sovereignty consistency, cross-sphere final settlement remains explicit |
| D17 | No new tags, leaders, flags, 3D units, raids, or animation | Deliberate scope fit, not unfinished required content |
| D18 | One actual world-end super-event | Scale-sensitive presentation, no evolution presentation quota |
| D19 | Direction-only final localization | Supplied planning skill, source research precedes final strings |
| D20 | Keep catalog status unreworked until implementation proof | Supplied source authority and inspected old script |
| D21 | No actual subagent or MCP completion claims | Tool availability, all such passes remain openly unperformed |

## Unavailable authority and references

`CHAOS_REDUX_PROJECT_SOURCE_PROTOCOL.md` was absent from the archive. Project-file searches and a repository search returned no matching result. This means it was not found or read, not that its global nonexistence is proven.

The canonical asset reference library, reference catalog, contact sheets, actual achievement templates, and production processors were not supplied. A fetch of `.agents/skills/chaos-redux-event-assets/assets/gfx_references/README.md` at the pinned revision returned 404. Required installed vanilla documents, the actual map, native Spanish and Portuguese files, current GUI and focus consumers, music registry, and authoritative XLSX were not available for full inspection.

Those missing inputs prevent claims of full external-reference coverage, implementation readiness, final asset compliance, or independent specialist validation. They do not justify changing the user's creative brief or inventing the unavailable evidence.
