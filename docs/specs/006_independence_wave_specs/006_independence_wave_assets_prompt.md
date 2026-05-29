# Asset Prompt: Event 6 Independence Wave

Use `chaos-redux-event-assets`. Create, source, process, convert, wire, and document all assets required by Event 6 Independence Wave. Inspect the relevant reference folders before creating or sourcing assets.

## Reference folders

- ideas: `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/ideas`
- news event images: `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/news_event_images`
- report event images: `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/report_event_images`
- super-event images: `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/super_event_images`
- achievements: `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/achievements`
- decisions: `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/decisions`
- flags: `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/flags`
- focuses: `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/focuses`

## Source mode rules

- News images, report images, and super-event images use sourced period-matching images where possible.
- For World War II era photo assets, use roughly 1936 to 1945 period imagery. Do not use modern reenactments, film stills, tourist photos, or AI reconstructions.
- Real flags, real symbols, real leaders, real royal houses, real political figures, and real cultural symbols use sourced historical material.
- Fictional councils, strange leaders, invented high-chaos flags, focus icons, decision icons, ideas, achievements, faction emblems, and UI panels can use `$imagegen`.
- Transparent icons must have real transparency and no white halo.

## Event 005 separation

Assets for Event 006 must be documented as Independence Wave assets. If the same tag appears in Event 005 and Event 006, do not blindly reuse Event 005 art. Reuse only if the symbol is generic or historically sourced and does not imply the Soviet Collapse route. Otherwise create a distinct Event 006 cosmetic variant, especially for focus icons, idea icons, route emblems, formable seals, package flags, and animated route assets. Soviet republic style tags released by Event 006 need Event 006 presentation, not Event 005 collapse presentation.

## Event and report images

1. `GFX_report_event_independence_wave_petitions`: local officials, petitions, crowds, or border office. 210x176.
2. `GFX_report_event_independence_wave_suppression`: troops, police, closed assembly, or censorship office. 210x176.
3. `GFX_report_event_independence_wave_observers`: foreign observers, journalists, commission room, or border checkpoint. 210x176.
4. `GFX_report_event_independence_wave_release`: flags raised, provisional council, town hall, or border post. 210x176.
5. `GFX_news_event_independence_wave_league`: diplomatic congress of small states. 397x153.
6. `GFX_news_event_independence_wave_partition_week`: many new borders, maps, telegraph office, or newspaper montage. 397x153.
7. `GFX_report_event_independence_wave_old_state`: archive, old map, seal, palace, treaty, or archaeological motif. 210x176.
8. `GFX_report_event_independence_wave_land_congress`: land council, local assembly, elders, chiefs, or community defense. 210x176.
9. `GFX_report_event_independence_wave_impossible_state`: symbolic high-chaos state office, grave ledger, sealed ministry, or abnormal border guard. 210x176.

## Package asset families

### Ordinary releasable assets

Use existing flags and portraits if valid. Add generic Independence Wave decision icons and focus icons.

### Historical-return assets

Research before creating:

- Assyria: modern Assyrian symbols, diaspora or homeland imagery, Nineveh or Khabur references where appropriate.
- Mesopotamia: river, mandate-era, Iraqi administrative, or ancient-symbol references with care.
- Volga Bulgaria and Old Great Bulgaria: Volga-Kama and historical Bulgar references. Do not use Event 005 route art, republic-collapse art, or Soviet Collapse branch emblems for the Event 006 version.
- Sokoto, Kanem-Bornu, Darfur: emirate, sultanate, Sahel trade-route, or palace council symbols.
- Asante, Buganda, Barotseland, Zulu: kingdom or local authority symbols with sourced research.
- Herero and Nama: land recovery, community authority, and colonial-era context with careful sourcing.
- Mapuche Araucania, Aymara, Guarani, Charrua, Palmares, Maya, Itza, Nahua, Miskito, Inuit, Inca: use real historical or cultural symbols only when verified. Otherwise use fictional council emblems.

### Local-polity assets

Needed icon concepts:

- land congress
- treaty memory
- local guard
- community council
- protectorate renegotiation
- border across the mountains
- forest defense
- river settlement

### Strange-state assets

Generated assets are allowed:

- grave census
- sealed ministry
- anti-mankind directorate emblem
- archive-state seal
- impossible border post
- dead labor registry

## Focus and decision icon families

Create reusable icon families:

- petitions and papers
- provisional council
- militia rifles
- depot inventory
- foreign observers
- recognition mission
- patron cabinet
- anti-patron audit
- border commission
- small-state congress
- league charter
- old archive
- land congress
- railway timetable
- grave census
- human renunciation

## Achievement icons

Create icons for achievement prompt entries and add package-specific icons if new achievements are implemented.

## Manifest requirements

For every asset, document:

- sprite name
- file path
- source mode
- source URL or generation prompt reference
- author or archive if available
- license or public domain status if available
- date or estimated date if sourced
- why it fits Event 006
- whether it is reused from existing mod assets
- whether it is specific to Independence Wave origin
- uncertainty or `needs_user_review`

## Expanded asset production brief

The asset pack should make the event feel like a system that moves from ordinary political crisis to high-chaos state mutation. Do not produce one generic petition image and reuse it everywhere. The event needs clear visual stages, route identities, package identities, and origin separation from Event 005.

### Asset families

| Family | Use | Source mode | Required depth |
| --- | --- | --- | --- |
| Dossier and report images | Normal popups during petition, suppression, negotiation, foreign attention, and release resolution | archival or period-matching source image where possible | enough images that repeated waves do not show the same visual each time |
| News images | major public-facing wave outcomes, league formation warning, patron crisis, border war | archival or period-matching source image where possible | separate normal, severe, and high-chaos variants |
| Super-event images | First League, Great Partition Week, First Old Name, First Impossible State, League War | source image for political and map-room events, generated symbolic art for impossible states | each super-event gets a distinct visual role |
| Decision category and decision icons | host crisis, breakaway survival, patron aid, coalition congress, border commission, old-state archives | generated icons unless a real symbol must be sourced | icon groups must be readable at HOI4 scale |
| Idea and spirit icons | provisional legitimacy, host pressure, foreign leverage, coalition cohesion, old-state memory, occult pressure | generated icons or adapted source symbols | each variable family gets a visual family |
| Focus icons | route anchors and branch families | generated icons by default, sourced real symbols only when culturally specific and safe | route-level icons, not one-off filler |
| Flags and cosmetic variants | high-chaos historical-return and local-polity packages | sourced when real, generated only for fictional or strange packages | must separate Event 006 origin from Event 005 where needed |
| Portraits and councils | historical figures, generic councils, patrons, brokers, strange administrators | real portraits must be sourced, fictional councils can be generated | avoid fake portraits for real people |
| Faction emblems | League of New States, patron congress, strange compact | generated unless based on a real movement | simple silhouettes and strong symbolic contrast |

### Required report image set

| Sprite | Moment | Visual direction | Notes |
| --- | --- | --- | --- |
| `GFX_report_event_independence_wave_petitions` | first dossier | crowd, municipal office, petition desk, or local clerks | baseline image |
| `GFX_report_event_independence_wave_committee` | candidate committees form | men and women around table, civic hall, improvised banner | should fit ordinary political route |
| `GFX_report_event_independence_wave_suppression` | host crackdown | closed assembly, troops at street corner, police cordon, censorship | not battle art |
| `GFX_report_event_independence_wave_observers` | foreign observers | border checkpoint, diplomatic cars, press desk, photographers | needed for peaceful route |
| `GFX_report_event_independence_wave_negotiation` | talks | conference table, papers, guards outside chamber | can reuse period diplomatic imagery if documented |
| `GFX_report_event_independence_wave_release` | countries become independent | flag raising, border post, oath scene, town square | use for normal release |
| `GFX_report_event_independence_wave_league` | small-state congress | many small flags, chamber, delegates | pre-super-event normal popup |
| `GFX_report_event_independence_wave_border_commission` | claims and arbitration | map table, surveyors, frontier posts | links to border decisions |
| `GFX_report_event_independence_wave_patron_brokers` | foreign client game | embassy office, military adviser, bank papers | links to patron leverage |
| `GFX_report_event_independence_wave_old_name` | historical-return package | archive room, old seal, antiquities, treaty desk | avoid fantasy art for normal old-state return |
| `GFX_report_event_independence_wave_local_polity` | local authority package | land council, traditional court, rural assembly, community guards | region-neutral unless package-specific |
| `GFX_report_event_independence_wave_impossible_state` | strange release warning | empty office, ledger, sealed room, unnatural border marker | generated symbolic art allowed |
| `GFX_report_event_independence_wave_host_rump` | host survives as rump | capital government, guarded ministry, emergency map | reinforces host survival rule |
| `GFX_report_event_independence_wave_failed_wave` | wave fizzles or settles | newspapers, closed petition boxes, police files | useful for failed or negotiated outcomes |

### Decision icon set

| Sprite | Decision group | Icon direction |
| --- | --- | --- |
| `GFX_decision_independence_wave_category` | decision category | cracked border line around small flag |
| `GFX_decision_independence_wave_open_talks` | host negotiation | table, two folders, guarded door |
| `GFX_decision_independence_wave_offer_autonomy` | autonomy deal | small charter with regional stamp |
| `GFX_decision_independence_wave_deploy_garrison` | suppression | helmet over district map |
| `GFX_decision_independence_wave_invite_observers` | observers | camera, pass, border post |
| `GFX_decision_independence_wave_arm_loyalists` | loyalist support | armband and rifle crate |
| `GFX_decision_independence_wave_request_guarantee` | host asks help | large hand over capital seal |
| `GFX_decision_independence_wave_reserve_capital` | host survival boundary | locked capital star |
| `GFX_decision_independence_wave_guard_depot` | timed depot mission | crate, rail spur, sentry |
| `GFX_decision_independence_wave_hold_capital` | timed capital mission | city silhouette behind shield |
| `GFX_decision_independence_wave_recognition_mission` | recognition | stamp, passport, flag |
| `GFX_decision_independence_wave_send_volunteers` | coalition aid | two small flags and marching boots |
| `GFX_decision_independence_wave_charter_league` | league | ring of flags around signed charter |
| `GFX_decision_independence_wave_border_survey` | border claims | compass, survey chain, map |
| `GFX_decision_independence_wave_expose_brokers` | anti-patron | torn contract and hidden eye |
| `GFX_decision_independence_wave_archive_claim` | historical-return | seal, archive box, old map |
| `GFX_decision_independence_wave_local_land_council` | local polity | land marker, council stool, field boundary |
| `GFX_decision_independence_wave_occult_registry` | strange route | black ledger, unmarked stamp |
| `GFX_decision_independence_wave_necromantic_census` | necromantic route | census book and grave marker |
| `GFX_decision_independence_wave_human_renunciation` | anti-mankind route | broken human silhouette behind state seal |

### Idea and spirit icon set

| Sprite | Idea | Icon direction |
| --- | --- | --- |
| `GFX_idea_independence_wave_provisional_legitimacy` | provisional legitimacy | small flag over public square |
| `GFX_idea_independence_wave_unrecognized_state` | unrecognized state | blank passport and closed gate |
| `GFX_idea_independence_wave_host_pressure` | host pressure | capital seal under stress lines |
| `GFX_idea_independence_wave_crackdown_resentment` | radicalization after suppression | baton over petition |
| `GFX_idea_independence_wave_foreign_reporters` | foreign attention | camera flash at border |
| `GFX_idea_independence_wave_patron_leverage` | patron pressure | contract string tied to flag |
| `GFX_idea_independence_wave_small_state_cohesion` | coalition cohesion | small flags tied together |
| `GFX_idea_independence_wave_border_memory` | claim ambition | old boundary line under new map |
| `GFX_idea_independence_wave_old_state_memory` | historical-return pressure | old seal beneath modern stamp |
| `GFX_idea_independence_wave_local_land_authority` | local-polity legitimacy | land marker and council symbol |
| `GFX_idea_independence_wave_occult_pressure` | strange pressure | ledger with impossible margin |
| `GFX_idea_independence_wave_rump_host_government` | host survival consequence | capital tower with emergency lamps |

### Focus icon groups

The implementation agent should not generate a unique icon for every focus unless the final tree needs it. Create reusable icons by branch family.

| Focus group | Minimum reusable icons | Visual language |
| --- | --- | --- |
| Opening trunk | 4 | council, petition, budget, barracks |
| Civic route | 5 | ballot, charter, rights, observers, recognition |
| Military survival | 5 | depot, militia, officers, defensive line, emergency command |
| Revolutionary route | 4 | workshop, workers guard, purged police file, red local committee |
| National directorate | 4 | broadcast tower, youth battalion, border memory, claim office |
| Patron cabinet | 5 | embassy, adviser, loan contract, staff mission, puppet strings |
| Anti-patron struggle | 4 | exposed broker, counter agents, burned debt ledger, league shield |
| Coalition congress | 5 | congress table, supply board, guarantee pact, volunteer rail, league charter |
| Border commission | 5 | survey team, petition border, arbitration map, ultimatum, frontier guard |
| Crisis branch | 5 | broken charter, street barricade, exile cabinet, last vote, martial seal |
| Historical-return overlay | 6 | archive, old seal, restoration compromise, capital memory, treaty claim, old army badge |
| Local-polity overlay | 6 | land council, community guard, oral testimony, protectorate dispute, river boundary, local federation |
| Strange modules | 6 | unmarked congress, grave census, human renunciation, sealed border, archive-state seal, non-human cabinet |

### Flag and cosmetic rules

1. Existing HOI4 or modded flags can be reused only for ordinary releasables when they fit the Event 006 origin.
2. Shared tags with Event 005 need an Event 006 cosmetic note even when the same base flag is reused.
3. Historical-return flags must be researched before use. If a symbol is contested, modern political, religious, or sensitive, document the uncertainty and provide a neutral alternate.
4. Local-polity packages should avoid flattening living peoples into fantasy empires. Use neutral civic, council, or land-authority variants when a historical flag is not clear.
5. Strange packages can use invented flags, but they should remain state-like. The horror should come from bureaucracy, law, borders, or citizenship, not random monster art.
6. If a package lacks safe flag research, mark it `asset_blocked_until_review` and provide a simple placeholder brief rather than inventing a real-looking symbol.

### Leader and portrait rules

| Actor type | Portrait source rule | Implementation note |
| --- | --- | --- |
| Real historical ruler or politician | sourced archival image only | do not generate |
| Real cultural or religious figure | sourced only, and avoid use if disrespectful or unclear | prefer council leader instead |
| Generic provisional council | generated portrait or council image | no real-person claim |
| Local land council | generated group portrait or symbolic seat | avoid caricature |
| Patron broker | generated unless based on named historical person | can be shadowed adviser |
| Strange administrator | generated symbolic portrait | use desk, seal, ledger, or silhouette |
| Military commander for ordinary releasable | existing HOI4 leader if available, otherwise generic officer | avoid over-specific false biography |

### Package-specific asset notes

| Package | Required specific assets | Notes |
| --- | --- | --- |
| Assyria | old seal direction, council portrait, recognition route icon | distinguish ancient Assyria memory from modern Assyrian people |
| Mesopotamia | river map emblem, mandate-era archive image direction, federation icon | avoid pretending one ancient identity maps cleanly to modern Iraq |
| Mapuche Araucania | land congress emblem, community defense icon, neutral flag variant | source symbols carefully |
| Guarani | river mission and language congress icons | do not use generic jungle imagery |
| Charrua | memorial council icon, small-state flag variant | use sparse, civic visual identity |
| Aymara | highland council icon, federation route emblem | avoid using modern political party marks without review |
| Palmares | fortified settlement icon, freedom charter spirit | source Quilombo history carefully |
| Buganda | kabaka court direction, lake-region council icon | real monarchy symbols need review |
| Asante | stool or court direction, modern compromise icon | real symbols need source review |
| Sokoto | caliphate archive direction, scholar council icon | religious symbol handling needs care |
| Kanem-Bornu | Lake Chad route map, court restoration icon | asset research required |
| Barotseland | floodplain council icon, protectorate dispute emblem | source Lozi and Barotse symbols carefully |
| Zulu restoration | regimental memory icon, royal council asset | avoid fantasy warrior stereotypes |
| Herero or Nama authority | land testimony icon, genocide memory caution note | use sober visuals |
| Volga Bulgaria | river trade seal, Volga archive icon, Event 006 origin marker | do not reuse Event 005 route art blindly |
| Circassia or Mountain Republic | mountain congress emblem, diaspora appeal icon | asset research required |
| Bukhara, Khiva, Kokand | emirate or khanate archive, oasis city emblem | real symbols and leaders require sourcing |

### Contact sheet expectations

The asset worker should produce contact sheets by family.

- `contact_sheet_report_images.png`
- `contact_sheet_decision_icons.png`
- `contact_sheet_ideas.png`
- `contact_sheet_focus_icons.png`
- `contact_sheet_flags_event006.png`
- `contact_sheet_super_events.png`
- `contact_sheet_achievements.png`

Each sheet should label sprite names clearly. The final handoff must list source mode, source confidence, file path, target format, and blocker status.

### Asset manifest fields

Every asset should have a manifest row with:

| Field | Meaning |
| --- | --- |
| sprite_name | exact GFX name |
| asset_family | report, news, super-event, decision, idea, focus, flag, portrait, achievement, faction |
| source_mode | sourced, generated, existing, placeholder, blocked |
| source_link | source link if sourced |
| source_author_or_archive | known author, archive, or institution |
| license_status | public domain, compatible, unknown, generated, existing mod asset |
| date_or_period | especially for report and news images |
| cultural_sensitivity | none, review, high review |
| event_origin | Event 006 Independence Wave |
| package_or_route | ordinary, patron, league, historical-return, local-polity, strange, specific package |
| final_png_path | processed preview |
| final_dds_path | in-game texture |
| gfx_sprite_path | expected sprite definition file |
| localisation_or_docs_link | where the asset is referenced |
| uncertainty_note | anything the implementer must not hide |

### Blocking rules

Mark assets blocked instead of substituting poor fits when:

- the only available image is modern and the event needs period-compatible art
- a real person portrait cannot be sourced
- a real flag or symbol is contested and the spec has no neutral fallback
- the asset would confuse Event 006 with Event 005
- a generated image creates fake historical material
- a transparent icon has a white square, halo, or fake checkerboard
- the source license is unclear for final inclusion

### Sprite naming discipline

Use `independence_wave` in every Event 006 asset name unless the sprite is a shared generic icon already documented for reuse. Shared tags such as Volga Bulgaria can use the tag name only after the event origin string.

Preferred pattern:

- `GFX_report_event_independence_wave_*`
- `GFX_decision_independence_wave_*`
- `GFX_idea_independence_wave_*`
- `GFX_focus_independence_wave_*`
- `GFX_achievement_independence_wave_*`
- `GFX_flag_independence_wave_<package>_*`
- `GFX_super_event_independence_wave_*`

Avoid names such as `GFX_volga_collapse_*` for Event 006.

### Asset validation

Before completion, verify:

1. Every referenced sprite exists or is marked blocked with a reason.
2. Every real symbol or portrait has a source note.
3. Event 006 shared-tag assets are not mislabeled as Event 005.
4. Report images are period-compatible or explicitly marked generated only when impossible or symbolic.
5. DDS files are present for final assets.
6. Icons are readable at HOI4 decision, idea, achievement, and focus sizes.
7. Transparent icons have real alpha.
8. The asset manifest, docs, and coding prompt agree on required sprite names.

## Updated animated asset requirements

Use `chaos-redux-frame-animation` together with `chaos-redux-event-assets` for every animated Independence Wave asset.

Animated final assets must include:

- source frames
- processed frames
- horizontal sheet PNG
- sheet DDS
- static fallback DDS
- GIF preview for review only
- contact sheet when useful
- manifest entry
- gfx handoff
- frame count
- timing
- loop behavior
- source mode per frame
- state that controls the animation

Do not use a GIF as the final HOI4 asset. Do not create final motion by shifting, scaling, rotating, recoloring, pulsing, blurring, or filtering one still image. Every meaningful visual state needs its own source frame.

## Required scripted GUI and decision-category visual families

### Independence Dossier Board

Assets:

- `decision_category_independence_wave_dossier`
- `independence_wave_dossier_board_bg`
- `independence_wave_dossier_pressure_meter`
- `independence_wave_dossier_pressure_meter_warning`
- `independence_wave_dossier_candidate_card`
- `independence_wave_dossier_candidate_card_selected`
- `independence_wave_dossier_candidate_card_locked`
- `independence_wave_protected_capital_seal`
- `independence_wave_protected_capital_seal_animated`
- `independence_wave_warning_pulse_animated`

### New States Congress

Assets:

- `decision_category_independence_wave_congress`
- `independence_wave_congress_table_bg`
- `independence_wave_congress_vote_card`
- `independence_wave_congress_vote_card_selected`
- `independence_wave_congress_cohesion_meter`
- `independence_wave_congress_charter_seal`
- `independence_wave_congress_charter_seal_animated`

### Patron Ledger

Assets:

- `decision_category_independence_wave_patron_ledger`
- `independence_wave_patron_ledger_bg`
- `independence_wave_patron_track_arms`
- `independence_wave_patron_track_industry`
- `independence_wave_patron_track_intelligence`
- `independence_wave_patron_track_recognition`
- `independence_wave_patron_warning_shimmer_animated`

### Formation Ledger

Assets:

- `decision_category_independence_wave_formations`
- `independence_wave_formation_ledger_bg`
- `independence_wave_formation_state_card`
- `independence_wave_formation_state_card_met`
- `independence_wave_formation_state_card_missing`
- `independence_wave_formation_seal`
- `independence_wave_formation_seal_animated`
- `independence_wave_hidden_formable_seal_locked`

## Animated leader portrait package candidates

Create animated portrait packages only when the implemented route uses them.

Priority candidates:

| Portrait | Source mode | Motion direction | Trigger |
| --- | --- | --- | --- |
| First Old Name council | generated or sourced depending on package | light over archival seal, map shadow, slow office glow | first historical-return formation completed |
| Anti-mankind directorate | generated | cold eye-light, registry glow, particle drift | first anti-mankind state becomes public |
| Necromantic custodianship | generated | candle flicker, grave-paper movement, spectral dust | necromantic route completes |
| Railway corridor authority | generated | signal light sweep, map-line glow | railway formation completed |
| Rump host survivor | sourced or generated depending on leader | capital window light or candle flicker | The Rump That Endures fires |

Real people must use sourced portrait bases. Fictional, symbolic, supernatural, and collective leaders may use generated frame art.

## Formable nation asset coverage

Every implemented formable needs:

- flag normal, medium, and small
- ideology variants when relevant
- cosmetic-tag flag when used
- formation decision icon
- formation focus icon family
- post-formation idea icon if a new institution appears
- leader or council portrait
- animated portrait when route impact justifies it
- formation seal static fallback
- formation seal animated sheet if the Formation Ledger uses animation
- super-event image only for region-changing, hidden, strange, or major formation

Historical or attested formable symbols require source review. If no direct symbol exists, document the uncertainty and build a historically grounded alternate-history symbol rather than inventing unrelated art.

## Asset subagent routing

Spawn asset subagents with `fork_context=false` and explicit prompts.

Use:

- `chaosx_asset_source_researcher` for real flags, real symbols, archival report images, real portraits, and sourced animated portrait bases
- `chaosx_generated_event_art` for fictional UI panels, impossible-state images, fictional portraits, and generated animated non-icon frames
- `chaosx_icon_artist` for decision icons, focus icons, achievement icons, formation seals, small animated button sprites, and category icons

Every asset subagent must write manifest and gfx handoff notes. The main agent owns final `.gfx`, `.gui`, gameplay, docs, and spreadsheet wiring.
