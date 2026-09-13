# Asset requirement matrix

## Asset authority

This matrix is the accepted requirement list for Event 38 planning. It authorizes the listed asset families and no others. Final files require the matching asset skill, reference inspection, source evidence, processing, runtime placement, manifests, and wiring. Temporary evidence belongs under `docs/assets/038_malta_crusaders/` while implementation is active and must be promoted and removed before a complete event claim.

Every new flag uses ImageGen. Historically attested flags and symbols first require source research, then a strict flat reconstruction. Every character portrait belongs to `chaosx_portrait_creator`. Every custom unit family needs bespoke counters and sourced sound roles. 3D work uses the Event 38 model pipeline contract and cannot start before its hard gates pass.

## Country identity assets

| Asset ID | Type | Variants | Source mode | Intended runtime family | Main consumer | Producer | Evidence gate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `038_malta_crusaders_flag` | flat flag | normal, medium, small, ideology variants where used | researched Malta and Order symbolism, then strict ImageGen reconstruction | `gfx/flags/` roots | Malta baseline | source researcher plus generated event art | tag locked, attested geometry reviewed, no fabric scene |
| `038_sovereign_order_flag` | flat flag | three sizes | generated flat design grounded in Order symbols | flag roots | centralized route | generated event art | distinct from baseline and other routes |
| `038_confederation_orders_flag` | flat flag | three sizes | generated | flag roots | confederal route | generated event art | approved order-symbol composition |
| `038_crusader_kingdom_flag` | flat flag | three sizes | generated with researched heraldic direction | flag roots | kingdom route | source researcher plus generated event art | no false claim of one exact historical flag |
| `038_holy_see_flag` | flat flag | three sizes and valid ideology variants | strict reconstruction of relevant Papal design after source review | flag roots | Holy See | source researcher plus generated event art | Vatican and Papal geometry verified |
| `038_kingdom_of_god_flag` | flat flag | three sizes | fictional generated | flag roots | Kingdom of God | generated event art | visually distinct from Holy See |
| `038_principality_*_flag` | flat flag family | three sizes for each persistent package | historical-symbol research where attested, otherwise fictional generated route design | flag roots | Jerusalem, Antioch, Tripoli, Cyprus, Aegean, Anatolian, North African packages | source researcher plus generated event art | exact package and tag locked before production |
| `038_atlantis_flag` | flat flag | three sizes and cosmetic variants | fictional generated | flag roots | Atlantis Germany | generated event art | no use of false archaeological evidence or readable generated text |
| `038_holy_world_flag` | flat flag | three sizes | fictional generated Papal terminal identity | flag roots | Holy World actor | generated event art | terminal route approved |
| `038_teutonic_faction_emblem` | faction emblem | static, optional animated reveal state if accepted | generated | event-scoped interface faction folder | Teutonic Order faction | generated event art | exact faction UI consumer inspected |
| `038_holy_world_faction_emblem` | faction emblem | static and terminal state variant | generated | event-scoped interface faction folder | believer bloc | generated event art | alpha and final size verified |

## Portrait assets

| Asset ID | Subject | Classification | Source mode | Runtime size | Consumer | Special rule |
| --- | --- | --- | --- | --- | --- | --- |
| `038_grand_master` | opening Grand Master | grounded | attributed archival male portrait through source-placeholder or user-requested styled-final workflow | `156x210` | Malta leader | final identity depends on scenario date and local ownership search |
| `038_pope` | Pope installed by route | grounded | attributed archival source for the valid current-period Pope | `156x210` | Holy See and Kingdom of God | exclusive ownership, no duplicate active ruler |
| `038_order_commanders_*` | named grounded commanders where defensible | grounded | attributed archival sources | role-specific vanilla sizes | commanders and high command | omit rather than invent when no defensible source exists |
| `038_order_council` | institutional council fallback | grounded institution | authentic institutional material | `156x210` or verified institutional consumer | confederal leadership | institutional name and no invented one-person face |
| `038_blessed_hitler` | transformed hidden-route figure | grounded named real person in fictional treatment | cannot generate or reconstruct identity, use source-placeholder and approved overlay treatment only | verified leader consumer | guarded hidden leadership arrangement | no face substitution, no duplicate ownership |
| `038_atlas_hitler` | Atlantis Germany leader treatment | grounded named real person in fictional propaganda identity | source-placeholder with separate fictional non-face overlays or user-supplied final if requested | verified leader consumer | Atlantis Germany | preserve real identity and record fictional route framing |
| `038_principality_leaders_*` | local rulers, councils, governors | package-dependent | grounded source or institutional source unless truly fictional high-Chaos identity | verified role sizes | principality packages | each candidate needs source classification and ownership search |

## Event, report, news, and super-event art

| Asset ID | Surface | Source mode | Visual direction | Consumer | Required variants |
| --- | --- | --- | --- | --- | --- |
| `038_event_opening` | report event | generated period-authentic documentary scene | knights and order banners moving through a 1930s Mediterranean fortress and port, with the force as subject | entry popup | one final DDS plus source and preview |
| `038_news_crusade_begins` | news | generated period press style | Mediterranean crusader landings and public reaction | bounded news event | one final DDS |
| `038_event_council_crisis` | report | generated | competing military orders in a fortress council, concrete emblems, no fake text | council incident family | base and severe state if justified |
| `038_event_principality` | report | generated | chartering a new crusader government in a real regional setting | principality creation | regional variants only where authorized and useful |
| `038_event_relic` | report | generated | disputed object, guarded procession, uncertain authenticity | relic events | discovery, dispute, theft states |
| `038_event_eleventh_crusade` | report | generated | surviving knights and transports rebuilding on Malta | failure route | opening and relaunch variants |
| `038_super_teutonic_order` | super-event | generated | Malta, Nazi Germany, and Holy Realm alliance ritual shown as fictional propaganda and political theatre | hidden faction super-event | unique image |
| `038_super_final_crusade` | super-event | generated | multinational regional crusade machinery, period weapons and medieval-modern formations | operation milestone | unique image |
| `038_super_atlantis` | super-event | generated | Nazi Atlantis transformation as fabricated imperial spectacle, Berlin motifs and oceanic symbolism | Atlantis reveal | unique image |
| `038_super_holy_world` | world-end super-event | generated | Papal terminal proclamation with Rome, multinational armies, and industrial crusader forces | Holy World activation | unique image |
| `038_super_eleventh_return` | optional major comeback milestone | generated only if final trigger justifies a super-event | return landing after genuine recovery | Eleventh Crusade return | unique image only after role approval |

## Decision category and mechanic UI assets

| Asset ID | Type | Target consumer | State set | Source mode | Producer | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `038_crusade_council_category` | category icon | decisions | static | generated transparent | icon artist | separate from focus and idea art |
| `038_crusade_council_picture` | category picture | decisions | baseline, crisis, Papal if animated presentation is approved | generated full-canvas | generated event art and frame animation for real state changes | no fake buttons or meters painted into picture |
| `038_council_panel` | UI panel | dedicated event GUI | baseline | generated painted panel | generated event art | event-owned UI only |
| `038_authority_meter` | UI meter family | council GUI | empty to full or threshold states | generated or designed alpha-backed UI | icon artist or generated event art according to consumer | visual identity must remain clear without color alone |
| `038_cohesion_meter` | UI meter family | council GUI | empty to full or threshold states | generated | same | distinct icon and frame language |
| `038_legitimacy_meter` | UI meter family | council GUI | empty to full or threshold states | generated | same | distinct icon and frame language |
| `038_order_cards_*` | GUI cards and emblems | council GUI | inactive, active, dominant, demanding, hostile | generated transparent | icon artist and generated event art | one authorized family per active order |
| `038_demand_warning` | warning animation | council GUI | real per-frame warning states | generated frame sequence | icon artist plus frame animation | static fallback mandatory |
| `038_relic_cards_*` | GUI icons | relic details | unknown, held, disputed, stolen, exposed | generated transparent | icon artist | do not imply authenticity through art state |
| `038_principality_status_*` | GUI icons | selected subject details | loyal, cooperative, guarded, defiant, rebellious | generated transparent | icon artist | qualitative state, not an extra public meter |
| `038_holy_world_continent_*` | selection icons or map pieces | terminal preparation | locked, available, selected, proven, lost | verified map-derived graphics where interactive | icon artist | exact geometry from local map inspection |

## Focus icons

Every major focus group needs its own icon family. The matrix authorizes these groups:

- opening command and survival
- Hospitaller, Templar, Teutonic tradition, Lazarite, naval order, and siege brotherhood routes
- centralized command and confederation
- Holy Land, Levant, Aegean, Anatolian, and North African campaigns
- Mediterranean logistics and fortress network
- principality charter, direct commandery, local restoration, and Papal administration
- Church and Crown, Holy See, Kingdom of God
- relic and Blessed formation routes
- Eleventh Crusade survival, rebuilding, and return
- hidden Teutonic alliance and regional campaigns
- hidden Atlantis transformation and regional programs
- Holy World preparation, continent proof, and terminal campaign

Focus icons must be separate `94x86` source designs. Idea or decision icons cannot be resized focus icons.

## Idea, national spirit, technology, and decision icons

| Family | Required examples | Asset rule |
| --- | --- | --- |
| starting and staged ideas | fragmented expedition, fortress Malta, competing orders, Mediterranean network, Papal supremacy, terminal command | separate `64x64` idea art, with lifecycle variants designed as a family |
| order ideas | each active order tradition and dominant-order final form | separate art for each institution |
| military technologies | armour workshop, warhorse armour, ranged development, incendiary siege, anti-tank lance, carrier development, holy armour | technology-specific art and `hoi4.tech_*` asset evidence |
| equipment | armour kit, knight horse set, bows, crossbows, siege equipment, engineer tools, carrier equipment | equipment and technology art based on exact consumer precedent |
| decisions | council, campaign, settlement, relic, principality, Eleventh Crusade, Holy World, Teutonic, Atlantis | `32x32` decision-specific silhouettes |
| missions | hold Jerusalem, protect corridor, rebuild fleet, pilgrimage, continent proof, defend Rome | mission-specific icons using the mission reference family |
| achievements | all accepted achievements in `19_achievements.md` | complete achievement triplets in root achievement folder |

## 3D model packages

Each row is a separate bounded model job unless a verified family-batch route is approved by the 3D skill.

| Model ID | Profile | One-image reference direction | Required action roles | Runtime consumer | Counter and sound requirement |
| --- | --- | --- | --- | --- | --- |
| `038_armored_knight` | humanoid unit | grounded professional game or tabletop design, full armour, 1930s-compatible weapon exceptions declared | idle, walk, run, melee attack or role-appropriate attack, hit, death, selected acknowledgement | Armored Knights | bespoke large and map counters, sourced armour and movement audio |
| `038_mounted_knight` | humanoid plus mounted or vehicle-equivalent profile after capability review | complete rider and armoured horse design | idle, walk, run, charge or attack, hit, death | Mounted Knights | bespoke counters, sourced horse and equipment audio |
| `038_archer` | humanoid unit | complete bow and combat-ready hand relationship | idle, walk, run, aim, release, recovery, hit, death | Archers | counters, sourced bow and movement audio |
| `038_crossbowman` | humanoid unit | complete crossbow and hand relationship | idle, walk, run, aim, fire, reload or recovery, hit, death | Crossbows | counters, sourced crossbow audio |
| `038_siege_catapult` | vehicle or articulated attachment | complete period-fantasy siege engine | idle, travel if used, aim, release, recoil or settle, destruction | catapult equipment and entity | bespoke counter and sourced wood, mechanism, impact audio |
| `038_siege_trebuchet` | vehicle or articulated attachment | complete trebuchet | idle, wind, release, settle, destruction | trebuchet equipment and entity | same requirements |
| `038_crusader_engineer` | humanoid unit | period engineer with medieval-order identity | idle, walk, run, work or tool action, hit, death | engineer specialist where map model is authorized | counters and sourced tool or movement audio |
| `038_naval_order_infantry` | humanoid unit | naval crusader with 1930s amphibious equipment | idle, walk, run, attack, hit, death | naval order infantry | counters and sourced selection, movement, attack, death roles |
| `038_mechanized_knight_carrier` | vehicle_land | medieval-modern carrier with declared anachronistic design | idle, move, attack if armed, destruction | advanced carrier family | land counters and sourced engine, movement, attack, destruction audio |
| `038_blessed_crusader` | humanoid unit or route variant | use distinct equipment and silhouette, no primitive glow-only reskin | full combat action set | Blessed formation | distinct counters and sourced audio, no synthetic holy sound substitute |
| `038_supreme_papal_knight` | humanoid or mechanized terminal unit | industrial late-game Papal knight | full combat action set | terminal Papal family | bespoke terminal counters and sourced audio |
| `038_atlantean_supreme_tank` | vehicle_land | fictional heavy fast Atlantis tank, period-exception declared | idle, move, attack, recoil, destruction | Atlantis Supreme armour | bespoke counters and sourced engine, gun, movement, impact, destruction audio |

No model may proceed from a multi-view board. Meshy receives exactly one approved prepared source image. Every humanoid requires vanilla source-mesh and entity scale calibration. Every vehicle requires exact domain reference and runtime-scale proof.

## Unit counter inventory

Every used unit surface requires original counters. At minimum audit and produce:

- large land-unit counters
- land map counters
- division-template emblems where the custom family uses them
- any support-unit or special interface counter consumed by the final implementation

The icon artist must inspect the exact installed-vanilla consumer, DDS, canvas, frame order, alpha treatment, and matching skill-local family. The palette must be sampled from the approved vanilla green reference. Renamed or reused counters do not satisfy the requirement.

## Sound inventory

Every custom unit needs a source-only sound package. Required roles depend on the consumer, but the complete inventory should consider:

- selection
- acknowledgement
- movement
- idle or engine loop
- attack or special action
- impact
- death or destruction

Every file needs source URL, title, creator, license, original checksum, derived checksum, editing record, and animation synchronization point. Generated, synthesized, recorded-by-agent, placeholder, test-tone, and unclear-license audio are forbidden.

## Super-event audio inventory

Each accepted super-event needs a unique final musical cue unless the user explicitly approves exact reuse. Research packages are required for:

- Teutonic Order reveal
- Operation The Final Crusade, if retained as a separate super-event
- Atlantis transformation
- Holy World terminal activation
- Eleventh Crusade return, only if retained as a super-event

The final cue must be a licensed or public-domain musical recording. It must be converted, registered through the settings-aware wrappers, documented in the canonical music catalogue, and connected to the exact super-event audio ID.

## Animation inventory

The following animation families are authorized only when they clarify state:

- council demand warning
- dominant-order card reveal
- relic stolen or disputed state transition
- Holy World readiness seal
- Atlantis reveal emblem
- optional non-face overlays for hidden transformed leaders

Every animation needs independently generated or sourced frames, a horizontal frame sheet, static fallback, GIF review preview, `.gfx` handoff, state trigger, and final runtime consumer. Transform-only animation is forbidden.

## Asset completion crosswalk

Before completion, implementation must publish a requirement-to-runtime table with:

- requirement ID
- final asset basename
- asset type
- source mode
- source and license record
- source PNG or original path
- processed PNG path
- final DDS, WAV, mesh, or animation path
- sprite, sound, entity, or equipment consumer
- review status
- static fallback where needed
- temporary workspace disposition
- blocker or approved exception

No visible placeholder, missing final file, or undocumented source may remain in a completion claim.
