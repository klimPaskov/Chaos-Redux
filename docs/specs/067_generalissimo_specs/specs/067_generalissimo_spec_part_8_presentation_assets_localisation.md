# Event 067 Presentation, Assets, Localisation, and Achievements

## Presentation strategy

Event 067 uses several focused presentation surfaces. Each surface has a clear role.

### Crisis decision category

The normal event uses an ordinary decision category with:

- one event-owned compact attached display
- one Influence meter
- Generalissimo portrait
- current command authority state
- current Influence band and trend
- one active demand or mission summary
- a changing category picture

The category remains the home of player actions. It does not open a separate full-screen mechanic window.

### Focus-tree inlay

After takeover, the Generalissimo focus tree uses a small read-only inlay with:

- portrait
- regime structure
- Command Cohesion meter
- current Cohesion band
- route emblem
- next important threshold or blocked condition

The inlay contains no decisions or hidden controls.

### Event popups and news

Event popups handle:

- initial appearance
- evolution activation
- important demands
- removal outcomes
- ultimatum
- peaceful submission
- revolt
- civil-war resolution

News events handle internationally visible outcomes, such as the Generalissimo becoming ruler, the civil war, and the world-end movement.

### Super-events

Two super-event roles are justified:

1. Generalissimo becomes ruler through peaceful submission or final junta victory.
2. The Generalissimos' World begins.

The revolt start itself uses an event and news package. It does not need a third super-event.

## Event-owned compact GUI

The attached crisis display and focus inlay are event-owned scripted GUI surfaces. They require `chaosx_event_ui_worker` for layout implementation and MCP visual evidence.

Working identifiers:

- GUI file: `interface/067_generalissimo.gui`
- GFX file: `interface/067_generalissimo.gfx`
- scripted GUI file: `common/scripted_guis/067_generalissimo_scripted_guis.txt`
- crisis container: `generalissimo_crisis_attached_display`
- crisis scripted GUI: `generalissimo_crisis_attached_scripted_gui`
- focus inlay container: `generalissimo_focus_inlay_container`
- focus inlay scripted GUI: `generalissimo_focus_inlay_scripted_gui`

The implementation agent may adjust exact filenames to match repository naming conventions, but stable runtime identifiers should remain clear and event-owned.

### Crisis display states

- hidden before Event 067 fires
- visible for the selected host while the crisis is active
- normal state during managed coexistence
- warning state when Influence reaches the State Within the State band
- critical state when the ultimatum is ready
- hidden after permanent removal, peaceful submission, or civil-war transfer

### Focus inlay states

- hidden before takeover
- visible only for a Generalissimo-led country using the dedicated tree
- Personal Command emblem state
- Officer Directorate emblem state
- National Emergency Council emblem state
- warning state at low Command Cohesion
- strong state at high Command Cohesion

### GUI clarity rules

- No raw variables.
- No debug text.
- No more than one persistent number.
- No painted fake buttons.
- No decorative overlay may block input.
- Meter fill, threshold markers, and labels must agree.
- Tooltips should remain concise.
- The attached display must not crowd ordinary decision rows.
- The focus inlay must occupy reserved tree space.
- Supported resolutions need before-and-after MCP renders.

## Static progression pictures

Animation is not required. Static state variants communicate the crisis more clearly and reduce maintenance.

The crisis category uses five generated full-canvas picture variants:

| Working asset ID | Influence state | Visual direction |
| --- | --- | --- |
| `generalissimo_category_asset` | 0 to 24 | One exceptional commander among a normal staff, with ordinary government symbols still present |
| `generalissimo_category_indispensable` | 25 to 44 | Officers and press attention center increasingly on him |
| `generalissimo_category_supreme_command` | 45 to 64 | National command room organized around his chair and insignia |
| `generalissimo_category_state_within_state` | 65 to 84 | Parallel headquarters, guards, and armament staff clearly answer to him |
| `generalissimo_category_ultimatum` | 85 to 100 | Military columns and senior officers prepare for a transfer of power without showing the final outcome |

The pictures contain no readable generated text, fake meter, button, number, or UI frame.

The asset worker must inspect the canonical decision-category picture references and current consumer size before production.

## Character portrait

### Source classification

- Subject: fictional and impossible
- Classification: `fictional_high_chaos`
- Gender: male
- Public identity: the Generalissimo
- Source mode: native ImageGen through `chaosx_portrait_creator`

### Portrait direction

- period 1936 to 1945 officer portrait language
- no copied real uniform or insignia package
- no resemblance to a named real leader
- full 156 by 210 framing after reference inspection
- restrained expression and direct command presence
- event-owned insignia that can recur on flags and icons
- no modern tactical equipment
- no fantasy armor
- no visible text

The same canonical portrait can serve the army leader and country leader when the consumer permits it. Separate resized or cropped variants may be produced through the portrait workflow, but they represent the same person.

## Event art inventory

### Report-event art

| Working asset ID | Role | Direction |
| --- | --- | --- |
| `generalissimo_report_appearance` | Initial manifestation | The unknown commander arrives before a skeptical but attentive senior staff |
| `generalissimo_report_demand` | Supreme Command demand | Senior officers visibly defer to him while civilian authority remains present |
| `generalissimo_report_removal` | Removal operation | Loyal guards, headquarters corridors, or a controlled transit scene without revealing success in advance |
| `generalissimo_report_revolt` | Failed removal or refusal | Units and headquarters split, with military command breaking into rival centers |
| `generalissimo_report_government_victory` | Junta defeated | Disarmed headquarters and surviving legal command, with visible military exhaustion |

### News-event art

| Working asset ID | Role | Direction |
| --- | --- | --- |
| `generalissimo_news_appearance` | International report of the commander | Period press-photo composition focused on the figure and the surrounding officer corps |
| `generalissimo_news_civil_war` | Military revolt begins | Columns, rail stations, command posts, or city approaches divided by competing orders |
| `generalissimo_news_rule` | Military government established | Generalissimo publicly assumes national authority |
| `generalissimo_news_world_movement` | World-end opening | Several capitals and military proclamations shown as one coherent global movement, with maps only as secondary props |

Generated report and news art should look like period documentary material, not modern cinematic concept art.

## Super-event images

### Generalissimo ruler super-event

Working asset ID: `generalissimo_super_event_rule`

Direction:

- the Generalissimo has become head of state
- the scene should show command converted into government
- military and state symbols are merged
- the image should work for peaceful submission and civil-war victory
- no specific real country architecture that would make the art invalid for other hosts
- no readable generated text

### The Generalissimos' World super-event

Working asset ID: `generalissimo_super_event_world`

Direction:

- military governments and rival officer centers emerge across several regions
- the original Generalissimo is a visual center without appearing to control everyone already
- civilian resistance and rival command are visible in the composition
- no single map-table scene
- no modern equipment
- no real leader likeness

## Icon inventory

All transparent icon families require native ImageGen transparency, preserved alpha, final-size readability, dark silhouette support where appropriate, and separate source art per asset type.

### Country-leader trait icons

- `generalissimo_trait_supreme_command`
- `generalissimo_trait_master_of_operations`
- `generalissimo_trait_logistical_dominion`
- `generalissimo_trait_arsenal_state`

Each icon should use a distinct symbol. The four cannot be one master icon resized or recolored.

### Starting idea icons

- `generalissimo_idea_government_at_gunpoint`
- `generalissimo_idea_army_of_the_generalissimo`
- `generalissimo_idea_command_economy`
- `generalissimo_idea_army_reconstruction`

Route upgrade forms can reuse the same coordinated family only when the visual state changes clearly and the exact consumer permits one staged icon family.

### Decision category icon

- `generalissimo_category_icon`

Direction: event-owned command insignia, readable at the inspected category-icon size.

### Crisis decision icons

Required coordinated but distinct icons:

- expand national command
- grant Supreme Command
- return to reserve
- public promotion
- appointment authority
- military budget
- loyal officer protection
- transfer operational planning
- transfer armament boards
- internal security command
- emergency powers
- foreign-policy veto
- military officers in government
- rotate regional commands
- civilian oversight
- remove loyal appointees
- loyal reserve command
- disperse guard formations
- move arsenals
- separate military intelligence
- negotiate retirement
- dismiss from command
- arrest at headquarters
- capture in transit
- assassination

The final internal filenames should use stable lowercase event-prefixed identifiers.

### Mission icons

- hold the command centers
- win the campaign
- secure the civilian chain of command
- build the loyal reserve
- postwar officer settlement
- restore national supply command

### Junta decision icons

- Officer Class Mobilization
- Requisition the Arsenals
- Regional Command Levies
- Integrate Defecting Formations
- Foreign Officer Missions
- Generalissimo Guard
- officer reconciliation
- officer purge
- capital command
- subject settlement
- faction settlement
- client junta support
- civilian restoration

### Focus icon families

The focus tree needs separate source art for every final focus. The exact final count follows the implemented tree.

At minimum, unique anchor icons are required for:

- secure capital command
- issue oath of command
- restore ministries
- reopen rail command
- fate of old government
- choose shape of command
- define Generalissimo strategy
- Personal Command opener and capstone
- Officer Directorate opener and capstone
- National Emergency Council opener and capstone
- Decisive Command opener and capstone
- Army of the Nation opener and capstone
- Fortress Command opener and capstone
- Naval Command opener and capstone when present
- Air Command opener and capstone when present
- Arsenal State opener and capstone
- Mobilized Construction opener and capstone
- Rule Through Garrisons opener and capstone
- Rule Through Service opener and capstone
- Officer Solidarity opener and International Command capstone
- Fortress Sovereignty opener and capstone
- Supreme Strategic Sphere opener and capstone
- postwar integration opener and permanent-government convergence
- world-end branch opener and global military-order capstone

The implementation asset manifest should expand this list to one row per final focus.

### Faction and bloc emblems

- `generalissimo_faction_international_command`
- `generalissimo_faction_civil_authority_compact`
- one rival military-bloc emblem family if the world-end implementation uses a dedicated visible faction identity

The International Command emblem should echo the Generalissimo's insignia. The civilian emblem must have a distinct institutional identity.

### Focus inlay assets

- compact inlay background panel
- Generalissimo portrait frame
- Command Cohesion meter frame
- Command Cohesion fill or masked texture
- low-Cohesion warning frame
- Personal Command emblem
- Officer Directorate emblem
- National Emergency Council emblem
- neutral unresolved structure emblem

No animation is required. Static state changes are preferred.

## Flag inventory

Three fictional flat flag families are required:

- Personal Command
- Officer Directorate
- National Emergency Council

Each family needs:

- normal flag
- medium flag
- small flag

The opening civil-war junta uses Personal Command. Route completion can change the flag.

The designs should share one event-owned insignia language while remaining visibly different.

### Flag direction

Personal Command:

- centralized single-command symbol
- strongest use of the Generalissimo insignia
- rigid composition

Officer Directorate:

- several coordinated military elements or a council structure
- balanced composition
- less leader-centered

National Emergency Council:

- military protection combined with a civic or state symbol
- less aggressive composition
- no direct copying of a real national emblem

All flags use ImageGen as flat graphic designs. They must not show fabric, folds, flagpoles, scenes, lighting, gradients, perspective, fake lettering, or invented historical claims.

## Achievement set

Working titles below are direction labels. Final titles and descriptions must be written during implementation from the stated role.

### `067_generalissimo_civilian_command`

**Title direction**

A state proves that command remains subordinate to government.

**Eligibility**

Original host country.

**Unlock conditions**

- Evolution II active
- Influence at least 65 before the operation
- Generalissimo permanently removed without revolt
- no use of peaceful submission

**Disqualifiers**

- manual scenario immediate-war setup
- save state already marked by junta victory

**Difficulty**

Hard.

**Icon direction**

A military baton placed beneath a civilian seal or locked command chain.

### `067_generalissimo_refuse_the_ultimatum`

**Title direction**

The legal government refuses the final demand and survives the war.

**Eligibility**

Original host country.

**Unlock conditions**

- Evolution III ultimatum received at Influence 85 or higher
- refuse
- win the civil war as the original government
- Generalissimo permanently removed

**Disqualifiers**

- peaceful submission
- foreign country completes most of the war through annexation of the junta

**Difficulty**

Very hard.

**Icon direction**

A government seal standing against crossed marshal batons.

### `067_generalissimo_barracks_to_capital`

**Title direction**

The revolt takes the state at maximum military backing.

**Eligibility**

Generalissimo junta.

**Unlock conditions**

- revolt begins at Influence 90 or higher
- junta wins and reunifies the country
- no foreign volunteers or expeditionary forces used by the junta

**Disqualifiers**

- peaceful submission
- scenario Low intensity

**Difficulty**

Very hard.

**Icon direction**

A field headquarters transforming into a national capital silhouette.

### `067_generalissimo_total_command`

**Title direction**

Personal rule and decisive warfare reach their complete form.

**Eligibility**

Generalissimo-led country.

**Unlock conditions**

- peaceful submission or junta victory
- complete Personal Command political route
- complete Decisive Command military route
- complete Supreme Strategic Sphere route
- capitulate two valid major enemies after takeover

**Disqualifiers**

- switch to another political structure
- use console or scenario completion markers not permitted by the normal achievement framework

**Difficulty**

Very hard.

**Icon direction**

One baton over a command globe with offensive arrows kept symbolic and readable.

### `067_generalissimo_first_among_generals`

**Title direction**

A stable officer order accepts the original Generalissimo's leadership.

**Eligibility**

Generalissimo-led Officer Directorate.

**Unlock conditions**

- Command Cohesion at least 90
- lead International Command
- at least five independent members
- at least two members are majors
- no member leaves for one year

**Disqualifiers**

- Personal Command route
- faction formed through a non-Event 067 bypass

**Difficulty**

Very hard.

**Icon direction**

One senior star surrounded by several distinct officer stars in a council ring.

### `067_generalissimo_guardian_state`

**Title direction**

A military guardian preserves the state without pursuing conquest.

**Eligibility**

Generalissimo-led National Emergency Council.

**Unlock conditions**

- complete the National Emergency Council route
- complete Fortress Command
- fight no offensive war for five years after permanent government proclamation
- maintain Cohesion at least 70
- remain independent

**Disqualifiers**

- fabricate or execute an offensive Event 067 expansion action
- become subject

**Difficulty**

Hard.

**Icon direction**

A shielded civic building beneath a military star.

### `067_generalissimo_world_against_the_barracks`

**Title direction**

Civilian governments defeat the original Generalissimo during the world-end campaign.

**Eligibility**

Original host government or a qualifying civilian major in the Civil Authority Compact.

**Unlock conditions**

- The Generalissimos' World active
- lead or become the principal military contributor to the Civil Authority Compact
- defeat the original Generalissimo's state
- restore civilian government in at least three countries
- at least one restored country is a major

**Disqualifiers**

- country previously submitted to the Generalissimo
- country currently under military government

**Difficulty**

Extreme.

**Icon direction**

Several civilian seals breaking a ring of marshal batons.

### `067_generalissimo_no_second_shot`

**Title direction**

A desperate removal operation succeeds at the last possible stage.

**Eligibility**

Original host country.

**Unlock conditions**

- Evolution III ultimatum active
- Influence at least 90
- choose final removal
- operation succeeds
- no earlier failed dismissal

**Disqualifiers**

- scenario immediate-war type
- operation chance artificially overridden by debug state

**Difficulty**

Extreme and chance-sensitive, with preparation required.

**Icon direction**

A stopped clock beside a broken command insignia, without showing graphic violence.

## Achievement asset rules

Each achievement needs:

- completed 64 by 64 icon
- grey variant
- not-eligible variant
- exact achievement ID filename
- source ImageGen evidence
- separate prompt and icon composition
- tracking and disqualifier documentation

The icons cannot be resized focus icons.

## Super-event package 1

### Role

The Generalissimo has become ruler after peaceful submission or junta victory.

### Trigger

- peaceful submission completes, or
- junta wins and reunifies the host

The super-event fires once. A civil-war start does not fire it.

### Title direction

Short title about military command becoming state authority. The final title must be researched or written through the super-event workflow and must fit both takeover routes.

### Description direction

Show that government departments, officers, and public institutions now answer to one military command. Mention the host dynamically. Do not list bonuses or focus routes.

### Quote direction

Research public-domain, historical, political, or military writing about armies taking political power, command, obedience, or rule by soldiers.

### Button or cultural remark direction

A short cold staff phrase, old military idiom, or sourced literary allusion. Avoid a generic reaction.

### Audio direction

A unique licensed musical recording with military, processional, or severe orchestral character. It should be between one and two minutes after editing unless a documented exception is approved.

### Image direction

Use `generalissimo_super_event_rule`.

## Super-event package 2

### Role

The Generalissimos' World begins.

### Trigger

The public Event 067 world-end branch commits at 1000 or higher Chaos.

### Title direction

The accepted world-end scenario name is the primary title candidate. Final slot fit still needs research and UI review.

### Description direction

Show military establishments abandoning or replacing civilian authority across several countries. Make rival juntas and civilian resistance visible. Do not imply that the original Generalissimo already controls the whole world.

### Quote direction

Research sourced writing about military rule, civil authority, men on horseback, command, force, or the political danger of armies.

### Button or cultural remark direction

A short sourced allusion about command or government by soldiers. No invented quote.

### Audio direction

A unique licensed musical recording with broad international and military character. It cannot reuse the first Generalissimo super-event track.

### Image direction

Use `generalissimo_super_event_world`.

## Super-event research gates

The implementation must treat these items as blocked until sourced:

- final super-event title where not directly accepted by the user
- final quote
- quote attribution
- final button or cultural remark
- final audio recording
- audio creator or composer
- recording rights
- final audio duration and edit

No generated tone, drone, beep, noise bed, placeholder, or undocumented track can close the super-event work.

## Localisation direction

The planning package gives direction only. It does not provide pasteable final event, decision, focus, achievement, GUI, or super-event text.

### Baseline event

Viewpoint:

- target government and senior officers

Visible information:

- unknown provenance
- verified military ability
- immediate appointment
- no political demand

Tone:

- controlled disbelief
- professional military attention
- limited dry irony is acceptable in one response direction

Avoid:

- explaining the supernatural cause
- generic staff report framing
- claims that the world has changed forever
- comparisons to a named real dictator

### Evolution I

Viewpoint:

- government confronting a commander whose victories have created authority

Visible information:

- officer deference
- public prestige
- formal demand for command

Tone:

- political pressure expressed through military behavior
- no direct statement that a coup is inevitable

### Evolution II

Viewpoint:

- institutions discovering that appointments, security, production, and regional commands answer to his network

Visible information:

- loyal officers
- armament control
- internal-security access
- government difficulty issuing independent orders

Tone:

- concrete institutional loss
- serious and restrained

### Evolution III ultimatum

Viewpoint:

- head of government receiving a final demand backed by the armed forces

Visible information:

- submit, refuse, or attempt removal
- immediate military consequence of failure or refusal

Tone:

- direct and clear
- no hidden mechanical spoilers beyond the public choice
- no cheap joke

### Failed removal

Viewpoint:

- headquarters and formations reacting in real time

Visible information:

- operation failed
- Generalissimo has declared the government illegitimate
- revolt begins now

Tone:

- urgent but complete prose
- no chain of tiny dramatic sentences

### Peaceful submission

Viewpoint:

- transfer of state authority

Visible information:

- military government established
- Generalissimo takes control
- old institutions remain only where accepted

Tone:

- formal military certainty
- public unease

### Civil-war victory and defeat

Junta victory should show reunification and permanent military rule. Government victory should show military exhaustion, disarmament, and the difficult reconstruction of command.

Neither should read as a reward list.

### World-end

Viewpoint:

- international observers, governments, soldiers, and civilians

Visible information:

- coups, emergency governments, rival juntas, civilian resistance
- original Generalissimo as one major center

Tone:

- global political transformation
- no claim that every country follows one leader immediately

## Decision localisation direction

Decision names should state the action. Descriptions should explain:

- what institution or force the government is using
- the visible cost
- the public result
- the risk of failure when relevant

Removal tooltips must clearly state when failure starts an immediate revolt.

Dynamic state missions must name the capital, arsenal region, headquarters, rail hubs, ports, or supply states involved.

## Focus localisation direction

Each route needs a distinct voice:

- Personal Command uses direct leader-centered military authority.
- Officer Directorate uses professional staff, council, and unity language.
- National Emergency Council uses emergency charter, administration, and guardianship language.
- Decisive Command uses operational timing and concentration.
- Army of the Nation uses reserves, training, and national service.
- Fortress Command uses zones, supply, depth, and protected approaches.
- Officer Solidarity uses staff missions, recognition, and military governments.
- Fortress Sovereignty uses deterrence and protected independence.
- Supreme Strategic Sphere uses strategic access, protectorates, and regional command.

Final focus text must describe visible action and direction without revealing secret future events.

## Event Details and spreadsheet wording

Event Details and workbook fields should use the same finished in-game wording for:

- event premise
- evolution summaries
- world-end premise
- manual scenario details
- type and intensity descriptions
- cluster role

They should not include implementation notes, hidden variables, source history, or rework language.

## Asset workspace and final placement

Temporary evidence belongs under:

```text
docs/assets/067_generalissimo/
```

Final runtime files belong in event-scoped folders under the correct asset categories, such as:

- `gfx/leaders/067_generalissimo/`
- `gfx/event_pictures/067_generalissimo/`
- `gfx/interface/ideas/067_generalissimo/`
- `gfx/interface/decisions/067_generalissimo/`
- `gfx/interface/goals/067_generalissimo/`
- `gfx/interface/067_generalissimo/`
- `gfx/super_events/067_generalissimo/`
- root flag folders using engine naming
- root achievement folder using exact achievement IDs
- `sound/067_generalissimo/`

Before final completion, durable provenance and wiring facts move into permanent event documentation, final runtime assets are verified, and the temporary event asset workspace is deleted.

## Asset exclusions

The event does not require:

- custom land unit art
- custom unit counters
- custom unit voice or combat sound
- 3D model
- skeletal animation
- animated portrait
- animated decision category picture
- state-puzzle map

Static progression pictures and the compact meters communicate the changing state more clearly.
