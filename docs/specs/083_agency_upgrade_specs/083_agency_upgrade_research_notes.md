# Event 83 research notes and bibliography

Research date: 22 September 2026.

## Evidence hierarchy

The user's Agency Upgrade brief controls event identity, worldwide recipients, the four package sizes, the evolution thresholds, Intelligence/Low membership, the fixed Evolution III suite, and the no-wasted-development direction. The supplied archive controls the project planning workflow and provides export-only catalog and mechanics snapshots.

Repository inspection was performed through the connected GitHub reader at commit `879b3007d3b6bf75c726c11635473fccda45c569`. That is a reproducible inspected state, not an assertion that it is the user's current local working tree. Installed vanilla definitions and generated game documentation remain the highest-priority evidence for exact scripting behavior and were unavailable here.

Offline wiki snapshots in the repository were used as secondary technical references. Their own warning that effect lists can be outdated remains material. A snapshot captured in September 2026 can contain older statements. The capture date is not the game version to which every documented behavior was verified.

## Existing Event 83

**E1. Existing event implementation, fully read.** `events/083_agency_upgrade.txt` at the pinned commit.

Source: `https://github.com/klimPaskov/Chaos-Redux/blob/879b3007d3b6bf75c726c11635473fccda45c569/events/083_agency_upgrade.txt`

The hidden root sends a recipient event to every country. The visible recipient uses `GFX_report_event_intel` and applies `gain_random_agency_upgrade` inside its option. This proves the current minimal behavior, not the new design. It motivates moving the award away from acknowledgment and retaining the existing namespace.

**E2. Existing localisation, fully read.** `localisation/english/083_agency_upgrade_l_english.yml` at the pinned commit.

Source: `https://github.com/klimPaskov/Chaos-Redux/blob/879b3007d3b6bf75c726c11635473fccda45c569/localisation/english/083_agency_upgrade_l_english.yml`

The existing file has baseline title, description, and option keys. This planning package gives replacement writing directions without treating the old minimal text as a complete narrative design.

## Native effect and modifier findings

**E3. Repository offline Effects snapshot, partially read.** `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md`, captured 19 September 2026, blob `afc9255950157681d0202484f20d06cea9bd747c`.

Source: `https://github.com/klimPaskov/Chaos-Redux/blob/879b3007d3b6bf75c726c11635473fccda45c569/paradox_wiki/Effects%20-%20Hearts%20of%20Iron%204%20Wiki.md`

The relevant useful-scripted-effects entry says that `gain_random_agency_upgrade` only creates an agency when one does not exist. It does not establish exhaustive coverage or safe exhaustion detection. The intelligence section documents `create_intelligence_agency`, `upgrade_intelligence_agency`, and `create_operative_leader`. The latter distinguishes bypassing recruitment from needing recruitment. Those facts motivate explicit agency creation and a separate proof of the requested immediate-recruitment behavior.

The full Effects file was fetched but its large response was truncated. Its introductory material, a variable-related window, and targeted intelligence, operative, and helper sections were read. Fetching it did not constitute reading its entire contents.

**E4. Repository offline Modifiers snapshot, partially read.** `paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md`, captured 19 September 2026.

Source: `https://github.com/klimPaskov/Chaos-Redux/blob/879b3007d3b6bf75c726c11635473fccda45c569/paradox_wiki/Modifiers%20-%20Hearts%20of%20Iron%204%20Wiki.md`

The relevant tables distinguish `operative_slot` capacity from `new_operative_slot_bonus` recruitment choices, percentage network gain from flat network gain, and agency decryption power from older decryption fields. They describe `intelligence_agency_defense` as flat. They describe legacy encryption and encryption-factor fields as inactive with La Résistance enabled. These are direct reasons not to equate superficially similar keys with the requested rewards.

The examined snapshot did not provide a verified operation-preparation-speed key or a verified agency-era encryption multiplier. Searches with no result are evidence of an unresolved adapter, not proof that a current engine feature is impossible. The introduction and focused intelligence and operative sections were read, not the whole file.

**E5. Runtime cluster constants, fully read.** `common/script_constants/event_cluster_constants.txt`, blob `e20fc9cc8d49f6eb6027199464250adb52c077eb`.

Source: `https://github.com/klimPaskov/Chaos-Redux/blob/879b3007d3b6bf75c726c11635473fccda45c569/common/script_constants/event_cluster_constants.txt`

At the inspected commit, runtime cluster ID 8 is Diseases. Intelligence is not defined in that constants list. Separate enums distinguish member role from member danger. The supplied CSV's Intelligence ID 8 therefore cannot be pasted directly into runtime registration. The shared registry, saved history, and current workbook need a coordinated semantic mapping.

**E6. MTTH skill, fully read.** `.agents/skills/chaos-redux-mtth/SKILL.md`, blob `7d86c0fe166a23264fcb2a9f512994977f372a80`.

Source: `https://github.com/klimPaskov/Chaos-Redux/blob/879b3007d3b6bf75c726c11635473fccda45c569/.agents/skills/chaos-redux-mtth/SKILL.md`

The skill distinguishes MTTH-derived values from verified timing models and requires probability-tool evidence for audits. Its referenced project MTTH implementation file was not read in this session. This event's package selection and overflow weights do not justify inventing an event-specific MTTH timer.

## Catalog reconciliation

**E7. Three supplied catalog CSVs, fully read.** File-level hashes are recorded in the source ledger.

Event 83's exported premise describes political power rather than agency development. Its event row does not provide the intended Intelligence membership. The National Breakthroughs cluster export lists Event 83 as a Low member. The Intelligence export lists Events 39 and 52 and uses a fire-once type even though Event 52's event row is repeatable. These are conflicting snapshots, not permission to change the user's requested membership or another event's repetition rule.

The intended correction is semantic: Agency Upgrade becomes Intelligence/Low and the premise reflects the agency event. Do not equate workbook identifiers with runtime IDs, turn every Intelligence member repeatable, or perform unrelated catalog cleanup under this task. Final catalog prose must be derived from final in-game localisation after implementation.

## Primary historical and game-design references

**H1. Paradox Development Studio, Intelligence Agency development diary, 30 October 2019.** Read the diary section in the official Steam announcement archive.

Source: `https://store.steampowered.com/news/posts/?appids=394360&enddate=1573658704&feed=steam_community_announcements`

The original design presents agency investment, operatives, cryptology, branches, and defensive work as related choices. Its discussion of spy-master concentration also provides historical design context for why worldwide slot expansion can change campaign balance. This is a 2019 design reference, not current API documentation or evidence of current caps.

**H2. GCHQ, centenary of women's service in the UK armed forces.** Read the page's historical account of wartime intelligence work.

Source: `https://www.gchq.gov.uk/information/centenary-womens-service-uk-armed-forces`

The account describes women serving across varied wartime intelligence and supporting roles. The art direction therefore includes technical and language work, with women as ordinary professional staff. The reference informs occupational variety rather than assigning a British historical identity to every agency. Its photographs are not included in this package and are not presumed licensed for reuse.

**H3. CIA, The Origins of Foreign Language at CIA, 8 June 2022.** Fully read the article.

Source: `https://www.cia.gov/stories/story/origins-of-foreign-language-at-cia/`

The article's wartime OSS material illustrates the operational importance of language skills. Only that wartime context informs this event. Its later discussion of CIA language institutions belongs to the postwar period and must not be imported into a 1930s or 1940s agency illustration as though already established.

**H4. Official La Résistance product descriptions.** Product-level pages were reviewed to confirm the association between the expansion and the agency-centered espionage feature set.

Sources: `https://www.paradoxinteractive.com/games/hearts-of-iron-iv/add-ons/hearts-of-iron-iv-la-resistance` and `https://store.steampowered.com/app/1158100/`

These pages do not establish the current scripting behavior when the feature is disabled. The installed-game capability test still controls that question.

## What this research does not establish

It does not establish the installed full upgrade roster, exact current operative recruitment hooks, a current percentage counter-intelligence adapter, current encryption or preparation-speed modifier names, achievement callbacks, native asset-style equivalence, multiplayer determinism in the game, or successful in-game execution. The source ledger and readiness report identify those remaining reads and tests explicitly.
