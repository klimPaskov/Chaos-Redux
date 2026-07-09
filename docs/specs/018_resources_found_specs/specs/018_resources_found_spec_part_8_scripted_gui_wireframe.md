# Event 018 Resources Found, Part 8 Scripted GUI Wireframe and Animated State Briefs

All names and labels are working labels only. They are not final localisation. The implementation agent writes final text after checking actual GUI patterns in the repository and vanilla references. This file defines what the field management interface should communicate and how buttons, cards, and animated assets should behave.

## Interface purpose

The resource field can be handled through ordinary decisions, but the event becomes clearer if the main decision category has a compact scripted GUI header or an optional mechanic window. The UI should show why the discovery is useful, why exploitation is risky, which countries are paying attention, and whether the site is becoming unsafe.

The UI should not spoil the Cave Host before public danger. Early stages should show ordinary economic information and uneasy site details. The deeper mechanics should become visible through missing workers, sickness, attacks, evacuation, and closure pressure.

## Layout model

Recommended surface: event-owned scripted GUI attached to the Event 018 decision category.

Recommended window size: medium mechanic panel that can sit above or beside ordinary decisions. The exact pixel size belongs to implementation. The art prompt should provide scalable panel pieces and state cards.

Panel structure:

| Area | Content | Visible stage | Purpose |
| --- | --- | --- | --- |
| Header strip | state name, owner flag, current resource icon, stage seal | all active field stages | tells the player which field is active |
| Resource card | discovered resource type, event-added amount, exploitation level | discovery onward | shows economic value and investment state |
| Extraction pressure card | pressure, safety, worker harm, incident stage | expanded field onward | shows the risk of deeper work |
| Foreign interest card | trade interest, concessions, border claims, smugglers | foreign pressure onward | shows diplomatic pressure and possible conflict |
| Public safety card | evacuation, hunts, city panic, visible attacks | public danger onward | shows the emergency without naming hidden future branches |
| Closure card | sealing readiness, resource sacrifice, failure risk direction | strange incidents onward, strongest at last closure window | gives final prevention path before breach |
| Cave Host card | origin score, stored origin army, current capacity, controlled resource states | only after breach | shows nonhuman country mechanic |

## Header strip

| Element | Direction | Dynamic content | Warning state |
| --- | --- | --- | --- |
| Field state name | Use the state name and current owner. | target state, owner country | red or urgent style if owner lost control recently |
| Resource icon | Use the resource type discovered. | oil, steel, aluminium, rubber, tungsten, chromium | cracked variant if unsafe depth is active |
| Stage seal | Shows stage with a symbol, not a final title. | stage id | animated warning if public danger or breach countdown is active |
| Close button | Opens or hides the mechanic panel. | none | disabled only when interface is not available |

Tooltip direction:

- Explain that the panel covers the event-created field in one state.
- State the resource and owner dynamically.
- Do not reveal Cave Host mechanics before breach.
- Show that closing the field removes event-added resources only after closure becomes visible.

## Resource card

| Field | Display direction | Tooltip direction |
| --- | --- | --- |
| Resource type | icon and resource name from scripted localisation | describe what was found and how exploitation affects trade interest |
| Event-added amount | integer value, no decimals | explain that this is the event-added deposit, not the whole state economy |
| Exploitation level | stage pips or short label direction | explain what actions increased extraction intensity |
| Local boom | temporary economic state | explain construction, local hiring, and trade benefits without listing hidden values |
| Stored resource memory | hidden until closure or breach needs it | explain only when resource removal or Host origin scoring becomes relevant |

Resource card buttons:

| Button working label | Visible from | Cost direction | Effect direction | AI equivalent |
| --- | --- | --- | --- | --- |
| Survey deeper seams | baseline discovery | civilian factory burden, command attention, or industry capacity | may add more resources or reveal richer field | AI uses if stable and not at war emergency |
| Expand extraction | survey stage | civilian capacity, trains, trucks, stability or local support | raises exploitation and pressure | AI uses if economy is weak or resource is strategic |
| Stabilize extraction | expanded field | support equipment, engineers, civilian capacity | lowers pressure and reduces worker harm | AI uses when pressure is high |
| Reserve state output | expanded field | temporary consumer goods or output burden | reduces foreign concessions and slows pressure | AI uses if border rival exists |

## Extraction pressure card

| Value | Meaning | Tooltip direction | Color identity direction |
| --- | --- | --- | --- |
| Extraction pressure | how hard the field is being pushed | list recent causes such as expansions, concessions, and evolved incidents | red when high |
| Safety | protection, survey discipline, and worker evacuation | list safety actions and missing requirements | green or blue when strong |
| Worker harm | sickness, missing crews, corrosion, and deaths | describe visible harm without hidden monster labels too early | red or dark orange |
| Deep incident stage | how often strange events occur | describe site behaviour through observed incidents | purple or dark grey |

Pressure card buttons:

| Button working label | Visible from | Requirement direction | Effect direction | Failure or risk direction |
| --- | --- | --- | --- | --- |
| Fund safety commission | expanded field | civilian factories, support equipment, time | improves safety and lowers pressure growth | can fail if pressure already severe |
| Slow the shafts | unsafe depth | output sacrifice and trade disappointment | reduces worker harm and incidents | lowers economic benefit |
| Medical evacuation | unsafe depth | trains, trucks, manpower, medical support direction | reduces population loss and worker harm | weak if public danger already active |
| Conceal site incidents | unsafe depth | political cost, intelligence risk, stability | delays foreign panic and trade backlash | increases pressure if repeated |
| Open lower survey | unsafe depth or Evolution II | army XP or engineer investment | may identify tunnel threat and improve closure odds | can worsen incidents if greedy route is active |

## Foreign interest card

| Value | Meaning | Tooltip direction |
| --- | --- | --- |
| Trade interest | number or tier of countries interested in the field | show interested countries when known |
| Concession pressure | pressure to let foreign firms or governments operate | show current concessions and dependency risk |
| Border risk | nearby countries that may press claims or stage incidents | show border country if valid and not hidden |
| Smuggling | illegal extraction and black-market route | show resource loss and stability effect direction |

Foreign card buttons:

| Button working label | Visible from | Cost or requirement direction | Effect direction | AI direction |
| --- | --- | --- | --- | --- |
| Offer limited concession | foreign pressure | relations gate or trade agreement direction | lowers diplomatic pressure and adds economy benefit | AI accepts if resource deficit and not hostile |
| Refuse foreign survey teams | foreign pressure | stability or diplomatic cost | reduces foreign access and raises tension | AI uses if strong and isolationist |
| Invite foreign engineers | foreign pressure | relation, convoy, or civilian factory burden | improves extraction and safety but raises concession pressure | AI uses if weak or allied to interested country |
| Crack down on smugglers | foreign pressure | command power, infantry equipment, local support | reduces smuggling and may raise border tension | AI uses if internal stability is high |
| Demilitarized field talks | Evolution I pressure | border rival and diplomatic conditions | lowers war risk or creates temporary field limits | AI uses if weak near strong rival |

## Public safety card

This card appears only when incidents are visible enough that the public emergency is no longer only a workplace problem.

| Value | Meaning | Tooltip direction |
| --- | --- | --- |
| Public panic | local fear and flight from cities | show affected state or nearby city direction |
| Evacuation state | whether people are being moved away | show trains, trucks, manpower, or civilian capacity needs |
| Hunt pressure | military and police operations in the caves | show whether hunts reduce incidents or provoke them |
| City loss pressure | population danger in public areas | show that delays cost population and output |

Public safety buttons:

| Button working label | Visible from | Cost direction | Effect direction | Risk direction |
| --- | --- | --- | --- | --- |
| Evacuate exposed settlements | public danger | trains, trucks, manpower, civilian capacity | lowers population loss and panic | weakens local industry and may reduce state output |
| Military cordon | public danger | infantry equipment, command power, supplied divisions nearby | lowers escape incidents | can raise pressure if caves are attacked badly |
| Hunt lower chambers | public danger | army XP, equipment, manpower, local divisions | may reduce monster incidents | failure raises deaths and panic |
| Arm rescue crews | public danger | infantry equipment and support equipment | lowers worker death and improves closure odds | can worsen public fear |
| City shelter program | public danger | civilian capacity and trains | lowers city panic | expensive during war |

## Closure card

Closure is the key prevention route. It should be visible and clear once public danger or severe strange incidents begin. It should never be hidden behind a vague tooltip.

| Value | Meaning | Tooltip direction |
| --- | --- | --- |
| Sealing readiness | whether the owner can close the site | show missing resources, units, and safety prep |
| Resource sacrifice | event-added resources that will be removed | explain that closure sacrifices the field |
| Failure risk direction | danger that closure fails if pressure is high | show broad cause, not hidden dice details unless project style supports it |
| Last window | whether breach risk is near | urgent direction that does not say world-ending risk |

Closure buttons:

| Button working label | Visible from | Cost or requirement direction | Effect direction | Failure direction |
| --- | --- | --- | --- | --- |
| Seal upper shafts | strange incidents | engineers, support equipment, civilian capacity | lowers incident stage and improves later closure | can fail if exploitation remains high |
| Close the field | public danger or last window | major resource sacrifice, construction burden, local evacuation | removes event-added resources and prevents Cave Host if successful | field economic benefits end |
| Emergency collapse | last closure window | high manpower, equipment, command pressure, local state damage | strongest prevention attempt | may damage state and still fail if too late |
| Abandon the deep site | public danger | political and economic cost | pauses extraction and reduces pressure | smuggling and foreign pressure can continue |

## Cave Host card

The Cave Host card appears only after breach.

| Field | Display direction | Tooltip direction |
| --- | --- | --- |
| Origin state | state where the Host appeared | show origin state and stored origin army count |
| Origin army memory | initial divisions from exploited field, capped around 30 | explain that origin divisions do not count against later captured-state capacity |
| Controlled resource states | list or count of states feeding current capacity | explain one division per 10 total resources, cap 10 per non-origin state |
| Spawn queue | capacity not yet materialized into divisions | explain refresh timing and current bottleneck |
| Method | swarm or elder if focus route selected | explain route effect without normal manpower or equipment |

Cave Host card buttons should be limited. The Host should mainly use focuses and automatic refreshes. A few optional actions can help the player understand the system.

| Button working label | Visible from | Cost direction | Effect direction | AI equivalent |
| --- | --- | --- | --- | --- |
| Refresh captured seams | Host active | cooldown, controlled resource state | updates capacity and queue | AI calls on state control changes and monthly Host pulse |
| Pull broods inward | Host active | cooldown and resource network | shifts pressure to origin or resource cluster | AI uses when losing fronts |
| Mark rich ground | Host active | focus or hunger route requirement | highlights a nearby resource target | AI uses through target scoring |

## Button state table

| State | Visual direction | Tooltip direction | Click behavior |
| --- | --- | --- | --- |
| Hidden | no button shown | none | none |
| Locked | dim button with lock mark | explain broad unlock source, such as public danger or focus route | cannot click |
| Disabled | visible but unavailable | show unmet cost or requirement with icon-first lines | cannot click |
| Available | normal button | show cost, visible effect, and likely risk | can click |
| Hover | highlighted outline | show expanded tooltip and dynamic values | can click if available |
| Active | selected or pressed state | show ongoing mission or cooldown | cannot click again unless repeatable |
| Warning | pulsing or red frame | show danger and stronger consequence direction | can click if available, but risk is clear |
| Completed | check or sealed mark | show completed result and remaining aftereffects | cannot click unless designed as repeatable |
| Obsolete | faded or removed | show nothing unless the project uses historic action logs | no click |

## Tooltip direction by card

| Card | Required tooltip content | Content to avoid |
| --- | --- | --- |
| Header | state, owner, resource type, stage direction | final title-like text or hidden Cave Host spoilers before breach |
| Resource | resource amount, exploitation level, economy and trade direction | raw script effect list |
| Pressure | pressure causes, safety factors, worker harm | hidden future monster country name before public reveal |
| Foreign | interested countries, concessions, border tension | generic diplomacy filler |
| Public safety | evacuation, hunts, population danger | cheap comedy or direct world-end labelling |
| Closure | resource sacrifice, sealing readiness, failure risk direction | vague last chance text with no costs |
| Cave Host | origin army cap, captured-state capacity, no manpower or equipment | normal recruitment language |

## Animated asset briefs

All animations must follow the frame-animation skill. Every frame needs real source artwork or generated frame artwork. Do not make final animations by shifting, scaling, recolouring, blurring, or applying a glow filter to one still image.

| Asset working name | Surface | Target size | Frames | FPS | Loop | Static fallback | Source mode | State logic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| resource_field_stage_seal | header stage seal | 96x96 | 8 | 8 | yes | current stage seal | generated icon art | changes by field stage |
| deep_site_pressure_warning | pressure card | 128x48 | 6 | 6 | yes | static warning plate | generated UI art | visible when pressure high |
| public_panic_card_border | public safety card | 320x80 | 8 | 8 | yes | static panic border | generated UI art | visible when public panic active |
| closure_seal | closure card | 96x96 | 10 | 8 | yes | static closure seal | generated icon art | available, urgent, completed, or failed |
| breach_fissure_warning | header or closure card | 384x72 | 12 | 10 | yes | static fissure | generated UI art | breach countdown or last closure window |
| cave_host_leader_portrait | Cave Host country leader | 156x210 | 10 | 6 | yes | static nonhuman portrait | generated fictional portrait | Host active |
| cave_host_capacity_meter_frame | Cave Host card | 256x24 | 6 | 6 | yes | static meter frame | generated UI art | spawn queue has unfilled capacity |

### resource_field_stage_seal frame plan

| Frame | Visual state | Prompt delta direction | Loop note |
| --- | --- | --- | --- |
| 000 | clean deposit mark | stable mineral symbol, no cracks | rest |
| 001 | faint depth line | small dark seam visible | rising |
| 002 | deeper glow | seam glow grows | rising |
| 003 | cracked outer rim | rim stress visible | danger build |
| 004 | strongest fissure | central crack bright or dark | peak |
| 005 | mineral dust | dust falls around seal | falling |
| 006 | glow recedes | cracks remain visible | falling |
| 007 | returns near frame 000 | stable shape with subtle mark | loop close |

### deep_site_pressure_warning frame plan

| Frame | Visual state | Prompt delta direction | Loop note |
| --- | --- | --- | --- |
| 000 | dormant warning plate | dark metal and faint resource vein | rest |
| 001 | low pulse | small seam light | rising |
| 002 | mid pulse | warning marks brighten without readable text | rising |
| 003 | high pulse | fissure and dust peak | peak |
| 004 | aftershock | light fades, dust remains | falling |
| 005 | dormant return | close to frame 000 | loop close |

### public_panic_card_border frame plan

| Frame | Visual state | Prompt delta direction | Loop note |
| --- | --- | --- | --- |
| 000 | quiet border | dark frame, evacuation motif | rest |
| 001 | unsettled edge | small shadows at corners | rising |
| 002 | crowd motion symbol | blurred silhouettes drawn as source art, no text | rising |
| 003 | shelter lamps | small lamps flare | peak start |
| 004 | strongest panic | border looks strained but readable | peak |
| 005 | lamps dim | shadows recede | falling |
| 006 | edge settles | most motion gone | falling |
| 007 | quiet border | close to frame 000 | loop close |

### closure_seal frame plan

| Frame | Visual state | Prompt delta direction | Loop note |
| --- | --- | --- | --- |
| 000 | open ring | unsealed cave-ring symbol | rest |
| 001 | ring tightens | stone bands move closer as drawn state | rising |
| 002 | first brace | support struts appear | rising |
| 003 | pressure mark | cracks press against seal | danger |
| 004 | full pressure | strongest closure strain | peak |
| 005 | lock mark | seal almost shut | peak hold |
| 006 | dust fall | pressure relaxes slightly | falling |
| 007 | stable shut state | closure succeeds variant base | variant close |
| 008 | fracture state | closure failing variant base | variant close |
| 009 | return state | chosen variant loops to current state | loop close |

The implementation can split success and failure into separate sprite sheets if the engine surface handles state swaps better than a single mixed loop.

### breach_fissure_warning frame plan

| Frame | Visual state | Prompt delta direction | Loop note |
| --- | --- | --- | --- |
| 000 | hairline fissure | narrow crack, no creature | rest |
| 001 | deeper crack | small dust and pressure | rising |
| 002 | stone edge opens | slight widening | rising |
| 003 | lower light | underground glow or darkness appears | rising |
| 004 | falling gravel | stronger debris | danger |
| 005 | pressure wave | strongest warning state | peak |
| 006 | distant shape suggestion | no clear monster if before breach | peak |
| 007 | crack trembles | drawn frame variation | falling |
| 008 | dust cloud | light partly hidden | falling |
| 009 | crack narrows slightly | returns toward start | falling |
| 010 | aftershock | small stones fall | loop close |
| 011 | hairline fissure | close to frame 000 | loop close |

### cave_host_leader_portrait frame plan

The Cave Host leader is fictional and nonhuman, so generated art is appropriate. The portrait should be a leader portrait, not a monster splash image. It needs a clear head or governing body focal point, a readable silhouette, and HOI4 portrait framing.

| Frame | Visual state | Prompt delta direction | Loop note |
| --- | --- | --- | --- |
| 000 | still stone leader | nonhuman cave leader, low eye light | rest |
| 001 | dust breath begins | small dust at shoulders and mouth area | rising |
| 002 | eye light rises | stronger eye or core light | rising |
| 003 | stone skin shifts | subtle drawn fissure change | rising |
| 004 | full breath | dust and light peak | peak |
| 005 | held weight | same posture, heavy presence | peak hold |
| 006 | light recedes | dust falls | falling |
| 007 | fissures darken | return toward still state | falling |
| 008 | final dust | almost still | loop close |
| 009 | still stone leader | close to frame 000 | loop close |

The portrait handoff must record that the leader is nonhuman and should use an actual-ish Cave Host personal or monstrous name pool only if the implementation treats it as an individual. A collective leader portrait should use an institutional leader name instead.

## GUI cleanup and lifecycle

| End state | Required UI behavior |
| --- | --- |
| Field closed | Hide public danger, pressure, and closure buttons. Keep only aftermath or remove category if no other field exists. |
| Field owner changes | Rebuild owner-scoped view and move decisions to new owner. |
| Primary deep site invalid | Clear event targets and hide panel. |
| Cave Host emerges | Replace owner field management with Host card and human response categories. |
| Cave Host defeated | Hide Host card, show aftermath if designed, clear threat displays. |
| World-end fires | Gate ordinary field management and show terminal branch systems only. |

## UI acceptance criteria

The UI design is complete only if:

- The player can identify the active state, owner, resource type, and stage.
- Pressure, safety, foreign interest, public danger, and closure readiness are visible when relevant.
- Buttons explain nonstandard costs and missing requirements.
- The closure path clearly states that resources are sacrificed.
- Cave Host capacity is visible after breach and never described as normal recruitment.
- Each animated sprite has a static fallback and frame-source plan.
- AI has equivalent non-human-click paths for every meaningful action.
- The panel cleans up after closure, ownership change, breach, Host defeat, and world-end.
