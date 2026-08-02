# Asset Inventory

> Runtime reconciliation, 2026-08-02: the accepted runtime identity is exactly two tags, reusable `RTA` and separate `RTX`. The former twelve-design Rat Nation pool is historical planning residue and must not be produced or wired. Current flag production covers the two live identities plus route/cosmetic variants owned by `RTX`; no bespoke 3D model is required or planned for Event 020.

Every name is a proposed stable working name. Preserve any live-repository sprite name that already exists. Final files must follow the event-scoped asset folder rules.

## Disease and crisis board assets

| Asset | Type | Size | Source mode | Proposed use | Animation | Owner |
| --- | --- | --- | --- | --- | --- | --- |
| `idea_black_plague_strain` | disease or idea icon | 64 by 64 | generated icon | selected disease identity and state modifier family | static | icon artist |
| `disease_selector_black_plague` | disease selector icon | exact live disease-selector size | generated icon | Black Plague entry inside the shared disease board | static | icon artist |
| `status_black_plague_threatened` | UI status icon | live UI pattern | generated icon | Threatened state | static | icon artist |
| `status_black_plague_incubating` | UI status icon | live UI pattern | generated icon | known Incubating state | static | icon artist |
| `status_black_plague_infected` | UI status icon | live UI pattern | generated icon | Infected state | static | icon artist |
| `status_black_plague_severe` | UI status icon | live UI pattern | generated icon | Severe Crisis | static | icon artist |
| `status_black_plague_collapsed` | UI status icon | live UI pattern | generated icon | Collapsed state | static | icon artist |
| `status_black_plague_contained` | UI status icon | live UI pattern | generated icon | Contained state | static | icon artist |
| `status_black_plague_recovery` | UI status icon | live UI pattern | generated icon | Recovery state | static | icon artist |
| `status_black_plague_cured` | UI status icon | live UI pattern | generated icon | Cured and monitored | static | icon artist |
| `status_black_plague_weaponized` | UI status icon | live UI pattern | generated icon | known weapon provenance | static | icon artist |
| `status_black_plague_rat_controlled` | UI status icon | live UI pattern | generated icon | Rat-Controlled state | static | icon artist |
| `black_plague_countermeasure_stage_1_6` | progress-state family | live UI pattern | generated UI art | countermeasure milestones | static variants | generated art or icon artist |
| `black_plague_crisis_seal` | scripted GUI seal | size from live board | generated icon art | active crisis header | 8 real frames plus static fallback | icon artist and frame animation |
| `black_plague_black_fog` | map or UI overlay prototype | engine dependent | generated non-icon art | state disease fog | 8 to 12 real frames plus static fallback | generated art and frame animation |
| `black_plague_board_background` | UI panel art | live GUI size | generated UI art | shared board enhancement | static | generated art |
| `black_plague_value_icons` | UI icon family | live GUI size | generated icons | load, mortality, spread, containment, treatment, relapse | static | icon artist |

## Human decision icon families

Each 32 by 32 decision icon needs its own source art rather than a resized focus or idea icon.

- surveillance lens and medical ledger
- medical reserve crate
- rail inspection post
- border cordon gate
- port inspection lantern
- troop route restriction marker
- field hospital tent
- civilian travel restriction
- quarantine barricade
- army cordon
- emergency hospital
- relief convoy
- burial and sanitation crew
- vector control trap or sealed shelter
- city rat-clearing team
- sealed granary and warehouse
- sewer and burrow clearance
- flea and bedding treatment
- rail-yard and dock vermin purge
- demolition of infested blocks
- treatment distribution
- sealed transport hub
- evacuation train
- controlled reopening
- residual tracing
- household recovery
- foreign medical mission
- cure research
- publish findings
- intelligence theft
- weapon project safety
- weapon project acceleration
- stockpile destruction
- anti-rat fortification
- purge warrens and burrow clearance
- armored clearance
- air reconnaissance
- royal node strike

## Event picture package

| Working asset | Type | Size | Source mode | Direction |
| --- | --- | --- | --- | --- |
| `report_event_020_black_plague_origin` | report image | 210 by 176 | generated period-documentary | crowded neglected district, improvised care, no readable text, 1936 to 1945 visual technology |
| `report_event_020_black_plague_severe` | report image | 210 by 176 | generated period-documentary | mass illness, blocked street, overwhelmed crews, severe and respectful |
| `news_event_020_black_plague_overseas` | news image | 397 by 153 black and white | generated period-news | port quarantine, ships held offshore, period press composition |
| `report_event_020_rat_emergence` | report image | 210 by 176 | generated fictional documentary | organized rat movement in ruined street or sewer entrance, no comedy |
| `news_event_020_rat_nations` | news image | 397 by 153 black and white | generated fictional press photo | fortified human line facing mass rat formations |
| `super_event_020_rat_king_coronation` | super-event image | 457 by 328 | generated fictional art | sentient sovereign and brood court in ruined civic interior |
| `super_event_020_rat_king_world_end` | super-event image | 457 by 328 | generated fictional art | Rat King over conquered human capital, organized global dominion |
| `super_event_020_rat_king_defeat` | optional super-event image | 457 by 328 | generated fictional art | ruined throne and surviving human relief, reflective not triumphal | 

Report images must receive the project report-card treatment. News images must be black and white.

## Base Rat Nation portraits

| Portrait | Size | Source mode | Leader type | Direction |
| --- | --- | --- | --- | --- |
| `leader_rat_urban_brood` | 156 by 210 | generated | institutional collective | dominant brood in sewer or ruined city |
| `leader_rat_field_brood` | 156 by 210 | generated | institutional collective | brood among grain, earth, and riverbank |
| `leader_rat_dock_brood` | 156 by 210 | generated | institutional collective | brood in warehouse or quay interior |
| `leader_rat_war_brood` | 156 by 210 | generated | institutional collective | mutated brood in trench or depot ruins |
| `leader_rat_proto_sentient_*` | 156 by 210 | generated optional variants | institutional or emerging council | organized central figure without duplicating Rat King |

## Rat King portraits

| Portrait | Size | Animation | Direction |
| --- | --- | --- | --- |
| `leader_rat_king_static` | 156 by 210 | static fallback | sentient one-person rat sovereign, period regalia, subdued painterly treatment |
| `leader_rat_king_animated_sheet` | 1560 to 1872 by 210 depending 10 to 12 frames | real source frames | subtle breathing, whiskers, eyes, cloak and fog, no transform-only animation |
| `leader_rat_king_council_variant` | 156 by 210 | optional static or animated | sovereign framed by distributed council symbols |
| `leader_rat_king_hierophant_variant` | 156 by 210 | optional static or animated | plague ritual identity, no readable symbols |
| `leader_rat_king_world_end_variant` | 156 by 210 | optional high-chaos variant | final sovereign identity after terminal readiness |

Every one-person portrait handoff must record apparent presentation and matching nonhuman name-pool metadata.

## Flags

### Base Rat Nation pool

Produce one unique fictional flag set for each live runtime identity. Current target: two complete base designs, one for `RTA` and one for `RTX`, with only explicitly earned `RTX` route/cosmetic variants listed below.

Required sizes for each design:

- normal 82 by 52
- medium 41 by 26
- small 10 by 7

Design family:

- common rat and plague identity
- unique primary motif per brood
- tails, teeth, burrow spirals, grain, harbor hooks, broken rails, trenches, or disease marks
- no text
- no palette-only variants

### Rat King

- base Rat King flag set
- Absolute Crown route flag set when identity changes
- Council route flag set when identity changes
- Hierophancy route flag set when identity changes
- world-end cosmetic flag set

## Base Rat Nation focus icon families

All focus icons are 94 by 86 and need focus-specific source art.

| Family | Motifs | Approximate coverage |
| --- | --- | ---: |
| Awakening and Survival | first burrow, defended nest, first pulse, ruined street | 6 to 8 |
| Urban Warren | sewers, towers, cracked pavement, city tunnel | 4 to 6 |
| Field Brood | grain, riverbank, hedgerow, field path | 4 to 6 |
| Dock Brood | crates, rope, harbor tunnel, ship hold | 4 to 6 |
| War Brood | trench, depot, broken rail, battlefield carrion | 4 to 6 |
| Hierarchy | dominant beast, many nests, captured map | 6 to 8 |
| Mutation | swarm mass, brute silhouette, burrow claws | 8 to 10 |
| Plague Economy | feeding province, consumed city, nest network | 6 to 8 |
| Military Method | flood front, strongpoint break, road hunt, nest defense | 8 to 10 |
| Rival Absorption | entwined tails, contested nest, merged brood | 5 to 7 |
| Proto-Sentience | symbols, map, radio, command gesture | 6 to 8 |

The implementation can reuse a coherent family across analogous focus roles, but cannot use one identical icon for every node.

## Rat King focus icon families

| Family | Motifs | Approximate coverage |
| --- | --- | ---: |
| Coronation | crown, throne nest, unified tails, royal guard | 8 to 10 |
| Absolute Crown | scepter-like tail, guard, central command, punishment | 10 to 14 |
| Council | brood delegates, circular nest, shared map, distributed signal | 10 to 14 |
| Hierophancy | plague incense, dark shrine, ritual mask, death mark | 10 to 14 |
| Administration | rail ruins, ports, feeding provinces, royal nodes | 10 to 14 |
| Military Castes | royal swarm, crown brute, deep road, tail guard | 12 to 16 |
| Plague Mastery | infection wave, countermeasure adaptation, port plague | 10 to 14 |
| Captured Knowledge | radio, archive, map, intercepted code, scientist shadow | 10 to 14 |
| Population Policy | preserved district, emptied city, selective harvest | 8 to 10 |
| Continental Campaign | interior corridor, harbor closure, capital objective | 12 to 16 |
| World-End Path | crowned continent, global burrow, terminal sovereign | 10 to 14 |

## Idea and spirit icons

Separate 64 by 64 source art for:

- Uncounted Brood
- Born of Pestilence
- Fractured Instinct
- Crowned Brood
- Plague Dominion
- Stolen Mind
- route and failure variants when the icon meaning changes materially

Do not resize focus icons to fill this need.

## Rat decision and mechanic icons

Separate 32 by 32 art for:

- Brood Mass
- Hunger
- Coherence
- burrow node
- pulse timer
- concentration and scattering
- rival challenge and resistance
- absorption
- Dominion
- Sentience
- Brood Cohesion
- royal pulse doctrines
- population policies
- intelligence operations
- continent target
- capital objective
- Crown the Continent
- world-end readiness

## Achievement assets

Fourteen completed 64 by 64 icons plus grey and not-eligible variants. Exact concepts are in the achievement matrix.

## Super-event audio assets

| Super-event | Final requirement | Research direction |
| --- | --- | --- |
| Rat King coronation | unique 44.1 kHz stereo WAV, one to two minutes, unique audio ID and sound wrapper | dark processional or chant, verified license, not reused |
| Rat King world end | unique 44.1 kHz stereo WAV, one to two minutes, unique audio ID and sound wrapper | final judgment or ritual piece, public-domain `Dies Irae` lead requires final validation |
| optional Rat King defeat | unique track only if aftermath super-event eligibility is implemented | reflective memorial or lament, not triumphal |

## Manifest and handoff requirements

Every visual asset entry needs:

- event ID and slug
- asset type
- intended use
- source mode
- prompt or source link
- source path
- processed PNG path
- final DDS path
- target size
- sprite name
- target GFX file
- status
- uncertainty
- frame count, timing, loop, anchor, static fallback, and source note for animation

No asset is complete at the prompt or source-PNG stage. Final DDS, exact dimensions, manifest, and GFX handoff are required.
