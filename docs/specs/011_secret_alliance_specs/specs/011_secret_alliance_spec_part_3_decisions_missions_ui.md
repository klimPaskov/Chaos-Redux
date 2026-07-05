# Event 011 Secret Alliance Spec, Part 3 Decisions, Missions, Dossier UI, and Player Tools

## Decision category purpose

The target decision category should open at Evolution II or after enough suspicion is visible. Working label, not final localisation: Counter-Conspiracy Dossier.

The category is not a store. It is the player's counter-intelligence and crisis preparation board. Each action should represent a real national commitment: investigators, rail guards, factory security, diplomats, intelligence liaisons, military observers, border units, and controlled leaks.

The category should remain compact. It should show a few current actions, a few suspect targets, and a clear summary of values rather than every possible country button.

## Visible values in the category

The category header or attached scripted GUI should show:

| Value | Player meaning | Visibility |
| --- | --- | --- |
| Suspicion | how clear the pattern has become | visible once category opens |
| Evidence | how close the target is to exposing the pact | visible once category opens |
| Counter-readiness | how prepared the target is for a reveal or war | visible once category opens |
| Pact readiness | how close the pact is to a public crisis | vague meter at first, clearer in Evolution III |
| Confirmed members | members proven by evidence | visible after discovery |
| Suspected members | countries with enough signs to inspect | visible as cards or target rows |
| Diplomatic leverage | ability to split members away or gain support | visible after first diplomatic action |

Use dynamic localisation and consistent colours. Suspicion can use amber, evidence blue, pact readiness red, counter-readiness green, and leverage purple. Exact colours should follow existing Chaos Redux conventions if they differ.

## Category phases

| Phase | Display rule | Player actions |
| --- | --- | --- |
| Dormant | no category | none, only background incidents |
| Rumour | optional compact category or event detail hint | passive security review only if desired |
| Dossier | category opens | investigate, protect, trace, brief allies, inspect suspects |
| Exposure | evidence high | public exposure, backchannel deals, split members, prepare war |
| Pact crisis | Evolution III or public reveal | ultimatum response, preemptive war, defensive mobilization, crisis settlement |
| War | formal pact war | wartime disruption, member fracture diplomacy, war preparation follow-up |
| Aftermath | pact defeated, dissolved, or target defeated | cleanup, legacy idea handling, achievement checks |

## Decision families

### Investigations

Investigations raise evidence and may identify members. They should cost a mix of political attention, civilian capacity, intelligence exposure, and specialized resources.

| Working decision label | Requirements | Costs and risks | Result direction | AI use |
| --- | --- | --- | --- | --- |
| Trace courier routes | suspicion above low threshold | small PP, trucks or trains, intelligence exposure risk | chance to reveal a suspect or raise evidence | high if evidence low |
| Audit foreign payments | target has civilian factories or trade access | civilian factory burden, PP, relation damage with suspects | exposes Financier activity or reduces operation tempo | high if sabotage occurred |
| Interrogate captured liaison | incident has generated a liaison flag | command power below cap, stability risk, legal backlash | evidence boost, possible false lead | medium, lower for democracies |
| Embassy registry sweep | one or more suspected countries | PP, diplomatic relation hit, possible member confidence rise | can confirm a suspect, can worsen foreign opinion if evidence weak | cautious |
| Decode meeting traffic | agency or enough suspicion | army XP or air XP if military signals are used, equipment cost for radios | evidence and suspect list expansion | high for majors and prepared states |

Investigations should not all be available at once. Use recent incident flags, suspect count, phase, and cooldowns.

### Protection and hardening

Protection decisions reduce damage and raise counter-readiness.

| Working decision label | Requirements | Costs and risks | Result direction |
| --- | --- | --- | --- |
| Guard rail junctions | rail or supply disruption risk | trains, infantry equipment, temporary supply strain | lowers railway sabotage and improves readiness |
| Shield critical factories | industrial states or sabotage flag | support equipment, civilian factory burden, reduced production for a short period | lowers factory damage and raises readiness |
| Protect public figures | assassination attempt risk or high pact readiness | command power under cap, stability cost, political adviser lock risk | reduces leader or adviser disruption |
| Secure border depots | pact neighbor exists | place divisions or spend equipment, mission-style objective | lowers border incident chance and improves war opening |
| Brief allied commands | target has allies or faction | PP, intel exposure, relations requirement | improves allied call willingness after reveal |

### Diplomacy and fracture

Diplomacy should let the player exploit the pact's hidden promises.

| Working decision label | Target | Costs and risks | Result direction |
| --- | --- | --- | --- |
| Backchannel with weak link | low-confidence member or suspected member | PP, civilian factory burden, relations, risk of pact learning | member confidence falls, possible exit |
| Publish a narrow dossier | suspect with evidence | evidence spent or exposure risk | confirms one member, reduces secrecy, can push readiness |
| Offer a border guarantee | neighbor suspect | stability, PP, diplomatic concession, no active war | can split defensive member away |
| Expose conflicting promises | two members with incompatible claims | evidence, intelligence exposure | lowers cohesion and may block new invitations |
| Sponsor public arbitration | several suspects known | PP, relations, high evidence | can turn public reveal into settlement instead of war |

Diplomacy should not be a safe universal escape. Every public action can raise pact readiness if evidence is weak.

### Border missions and border wars

Border play only appears when a pact member or high-confidence suspect neighbors the target or a target subject.

Mission examples:

| Mission | Requirement | Duration | Success | Failure |
| --- | --- | --- | --- | --- |
| Watch the suspect frontier | supplied divisions in named border states | medium duration | evidence, readiness, lower incident risk | border incident chance and pact readiness rise |
| Hold the customs corridor | control border rail or port route | medium duration | reveals arms flow and reduces shipment operations | railway sabotage and relation damage |
| Contain a staged clash | active provocation | short emergency duration | prevents escalation and exposes Provocateur | border war or readiness spike |
| Prepare local defense plans | pact neighbor confirmed | long preparation duration | war opening bonus if reveal war begins | wasted resources and public panic if pact dissolves |

Border war decisions should become available at Evolution II for confirmed neighboring members or at Evolution III for publicly exposed members. Border wars should be risky and should not bypass the core reveal logic. If a border war becomes a direct war between target and member, war reveal fires.

### Exposure actions

Exposure actions are high-impact decisions unlocked by evidence.

| Working decision label | Requirements | Result direction |
| --- | --- | --- |
| Expose the secret protocol | high evidence | public reveal, member confidence checks, possible faction visibility |
| Demand signatory lists | high evidence and leverage | chance to reveal all members or force partial admission |
| Invite neutral observers | evidence and diplomatic access | lowers pact readiness and supports settlement route |
| Issue counter-ultimatum | Evolution III and readiness high | gives player initiative and war-preparation bonus, but can trigger reveal war |
| Strike first | public pact crisis | player starts war against pact and triggers formal reveal |

The player should not get a clean one-button solution. Exposure should be strongest after targeted work.

## Scripted GUI direction

The decision category should attach a compact Dossier Board scripted GUI if implementation capacity allows. It should improve clarity, not replace decision gameplay.

### Dossier Board layout

The board should show:

- top strip with four meters: Evidence, Pact Readiness, Counter-readiness, Cohesion
- left panel with the target country seal and current stage
- center panel with up to six country cards for confirmed and suspected members
- right panel with recent incident list
- bottom panel with current objectives and one recommended next action

Country cards should show:

- country flag
- status: unknown, suspected, confirmed, wavering, patron, exposed, at war
- role if confirmed: Convener, Financier, Provocateur, Patron, Recruit, Broker
- confidence level if known
- last known activity
- action buttons for investigation, backchannel, pressure, and border watch where valid

The GUI should not show hidden members with exact data before the player has evidence. Unknown cards can appear as blank silhouettes or sealed folders only when the player knows there are missing signatories.

### Animated presentation pass

The Dossier Board should have animated state assets when they clarify state changes.

| Asset | State logic | Suggested frame plan | Static fallback |
| --- | --- | --- | --- |
| Dossier seal pulse | evidence is high enough for exposure | 8 frame real source glow loop | non-glowing seal |
| Readiness warning frame | pact readiness near war threshold | 8 frame warning pulse | static red frame |
| Exposed member card glow | member confirmed this month | 6 frame highlight | highlighted static card |
| War countdown ticker | public crisis active | 10 frame clock or telegraph loop | static warning icon |
| Hidden protocol overlay | super-event reveal or public exposure | 8 frame page and shadow loop | static sealed protocol |

Every animated asset must follow the frame animation workflow with real source frames, a horizontal sheet, static fallback DDS, preview GIF for review only, and `frameAnimatedSpriteType` handoff.

## Player-facing text direction

The early text should show habits and consequences without naming the conspiracy. Use witness-like public details: identical slogans appearing in distant newspapers, the same foreign officers appearing near separate ministries, shipments delayed by unrelated paperwork, quiet meetings in neutral cities, and nervous border officials.

Evolution II text can become more direct. It should describe proof, damage, suspects, and public fear. It should not reveal hidden members before evidence supports it.

Evolution III text can name the public pact if it has been exposed. The tone should feel like a private mechanism becoming a public machine.

Option text should avoid bland buttons. It can use dry official confidence, angry military practicality, frightened restraint, or bitter diplomatic irony depending on ideology and route. Final wording belongs to implementation localisation, not this spec.

## Balance and exploit notes

- Evidence gain should be strongest after real incidents, not through spamming one cheap button.
- Member-splitting decisions should have cooldowns and target limits.
- War-preparation decisions should not stack forever.
- Public exposure with weak evidence should create risks.
- Border war actions should be restricted to real neighbors and should not create free war goals against distant members.
- Pact member recruitment should respect caps and cleanup.
- The player should not be able to farm endless relation bonuses by exposing dummy members.
- AI should not click human-only GUI buttons. It needs equivalent scripted effects or decisions.
