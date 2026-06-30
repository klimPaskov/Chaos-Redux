# Event 011 Secret Alliance Decision and Mission Map

This file expands the player-facing decision layer for Secret Alliance. It uses a dossier category that opens at Evolution II and changes shape at Evolution III.

## Category phases

| Phase | Visibility | Player sees | Main actions |
| --- | --- | --- | --- |
| Rumor file | Before Evolution II, only through popup options | No standing category | Light event responses only |
| Dossier open | Evolution II | Suspicion, evidence quality, preparedness, suspected count, selected suspected country | Investigate, harden, trace funds, identify targets, prepare borders |
| Public compact | Evolution III or forced reveal | Faction members, cohesion, war readiness, weak members, current ultimatum or war timer | Split members, demand dissolution, prepare war, launch preemptive action |
| War state | Open war | War objectives, pact cohesion, member resolve, preparedness rewards | Emergency defense, propaganda, defector use, postwar conditions |
| Aftermath | Pact dissolved or defeated | Cleanup tasks and diplomatic settlement | Remove networks, inspect embassies, recover factories, settle with defectors |

## Display values

The category header or scripted GUI should show these values with consistent colors and integer formatting where appropriate.

| Value | Display direction | Cause and effect clarity |
| --- | --- | --- |
| Suspicion | Player knowledge that a pattern exists | Show what raised suspicion in recent entries |
| Evidence | Strength of proof | Shows whether exposure is reckless, plausible, or strong |
| Preparedness | Readiness to absorb sabotage and war | Shows how decisions and missions improve it |
| Known members | Count and selected country cards | Identified names appear, hidden members stay masked |
| Pact war readiness | Visible at public compact phase | Explains war timer pressure |
| Pact cohesion | Visible after reveal | Explains why splitter diplomacy works or fails |

## Selected target flow

Human players should not see a wall of decisions for every possible member. Use a selected-target pattern.

1. Show a selector decision for each suspected or identified target.
2. Selecting a target stores that country as the dossier target.
3. Target-specific actions appear only for the selected target.
4. A close target decision clears the selection.
5. AI can evaluate target decisions directly without needing the selector.
6. Cleanup clears selected target flags if the country leaves the compact, dies, joins the target faction, or becomes invalid.

## Investigation actions

| Working decision label | Availability | Cost and requirement direction | Success | Failure or risk | AI use |
| --- | --- | --- | --- | --- | --- |
| Trace diplomatic couriers | Dossier open, at least one suspected target | Civilian intelligence effort, trains or convoys if overseas, small PP only as support | Evidence gain, chance to identify courier country | Diplomatic incident raises pact aggression | AI target uses when evidence low and stability is safe |
| Audit foreign contracts | Dossier open and industrial states exist | Civilian factory days, political staff, possible consumer goods burden | Finds purse holder clues and lowers sabotage chance | Production delay if overused | AI uses when industry is large |
| Intercept coded traffic | Dossier open, target has radio or neighbor route | Command power under 60, support equipment, intelligence exposure risk | Identifies one member or lowers secrecy | Failed interception can harm relations with an innocent country | AI uses if target is high threat |
| Follow attaché circuits | Suspected target selected | Army XP, command power, officer time | Finds knife hand or border plan | Lowers army readiness briefly | AI uses when neighboring suspect exists |
| Recruit a defector | Identified minor, evidence medium or higher | PP, stability risk, money-flavored resource through civilian burden | Member becomes defector or provides major evidence | Defector can be false if secrecy remains high | AI rarely uses unless peaceful route preferred |

## Defensive hardening actions

| Working decision label | Availability | Cost and requirement direction | Effect | Tradeoff |
| --- | --- | --- | --- | --- |
| Guard arsenals and rail hubs | Dossier open | Place supplied divisions in named industrial, rail, or border states | Reduces sabotage damage and raises preparedness | Ties divisions away from fronts |
| Factory watch rotations | Dossier open, factories exist | Support equipment, manpower, temporary production efficiency hit | Protects one industrial region from sabotage | Costs output now for resilience later |
| Port and embassy screens | Overseas trade or coastline exists | Convoys or naval XP, small civilian burden | Reduces courier and smuggling incidents | Can lower trade opinion if aggressive |
| Emergency communications desk | Evolution II or later | Political staff, command power, consumer goods burden | Reduces surprise from threats and ultimata | Raises domestic unease if used repeatedly |
| Shield public figures | Assassination or intimidation pressure active | Infantry equipment, support equipment, stability | Prevents targeted intimidation from removing advisors or lowering stability | Can increase public panic if warnings are visible |

## Exposure actions

| Working decision label | Evidence need | Effect | Risk |
| --- | --- | --- | --- |
| Leak the pattern to friendly papers | Low evidence | Raises global suspicion and may force a member to pause incidents | Can be mocked if evidence is thin |
| Demand explanations from suspected states | Medium evidence or identified member | Lowers secrecy and can identify more members | Can push pact aggression up |
| Present the dossier to neutral observers | High evidence | Major secrecy hit, chance to split weak members | Requires relations and costs diplomatic capital |
| Name the convenor | Strong evidence and convenor identified | Forces reveal or collapse check | If wrong, the compact gains cohesion and the target loses credibility |
| Offer amnesty for testimony | Identified minor member | Can create defector and isolate member from war conversion | Costs legitimacy and may anger hardliners |

## Splitter diplomacy actions

| Working decision label | Target | Cost palette | Result |
| --- | --- | --- | --- |
| Security guarantee bargain | Weak or fearful minor | Guarantee risk, relations, political capital | Minor leaves or becomes isolated |
| Trade compensation package | Purse holder or economically weak member | Civilian factories, resource access, trade opinion | Lowers cohesion or buys exit |
| Ideological reassurance mission | Ideologically hostile but not committed member | Stability or party pressure risk | Reduces grievance and member commitment |
| Patron wedge talks | Minor under major influence | Intelligence exposure, relations with third parties | Weakens major patron control |
| Public absolution offer | Identified member with low commitment | Domestic legitimacy cost | Member defects and gives evidence |

## Border and military actions

Border actions should only appear if a pact member or suspected pact member neighbors the target or holds a connected contested border.

| Working decision or mission | Requirement | Effect |
| --- | --- | --- |
| Guard named border crossings | Place supplied divisions in border states for a timed mission | Raises preparedness and lowers border provocation success |
| Counter-raid patrols | Neighbor suspect, enough infantry equipment and command power | Can stop a provocation and identify knife hand |
| Border arbitration demand | Evidence medium, neighbor identified | Can delay border war and lower aggression |
| Controlled border war | Evolution II or later, identified neighbor, high evidence, not public faction war | Small border conflict with limited stakes. Win lowers member commitment and can isolate it |
| War cabinet preparation | Evolution II or public compact | Raises preparedness, reduces war shock, costs command power, army XP, equipment, and stability |
| Demand dissolution | Public compact, evidence high, preparedness medium | If accepted, pact dissolves or loses members. If rejected, war readiness rises and target gets justification |
| Strike first | Public compact and war option unlocked | Starts war on chosen terms. Preparedness determines opening bonuses |

## Mission examples

Timed missions should require real action, not passive stockpile checks.

| Mission | Owner | Duration band | Objective | Success | Failure |
| --- | --- | ---: | --- | --- | --- |
| Hold the rail screen | Target | 120 to 180 days | Keep supplied divisions in named rail and industrial states | Sabotage damage reduced and preparedness rises | Factory sabotage becomes more severe |
| Keep the border quiet | Target | 90 to 150 days | Maintain divisions in border states without launching reckless escalation | Border provocations weaken | Pact identifies a soft border and gains aggression |
| Protect the evidence chain | Target | 90 to 120 days | Keep stability above a dynamic threshold while funding intelligence actions | Evidence quality rises | A key witness disappears and secrecy rises |
| Break the purse line | Target | 120 to 180 days | Use contract audit and selected target diplomacy against purse holder | Purse holder loses commitment | Trade squeeze intensifies |
| Prepare the emergency reserves | Target | 120 to 180 days | Train or hold divisions and spend equipment into reserve readiness | War opening shock reduced | Pact war readiness rises faster |
| Keep the weak member talking | Target | 90 to 150 days | Maintain relations and avoid direct border escalation with selected weak member | Member can defect or become isolated | Member commits publicly to the pact |

## Compact-side hidden decisions

Pact members should run hidden or AI-only actions that change pact values.

| Hidden action | Actor | Result |
| --- | --- | --- |
| Host shadow conference | Convenor | Cohesion and invitations rise |
| Fund press syndicate | Purse holder | Target relations and suspicion change |
| Prepare border cells | Knife hand | Border incident chance rises |
| Share staff estimates | Any member | War readiness rises |
| Ask for patron guarantees | Minor member | Major invitation chance rises |
| Quiet arms pool | Major or arsenal | War readiness and member commitment rise |
| Burn exposed files | Identified member | Secrecy rises but cohesion can fall |
| Discipline a wavering member | Major patron | Weak member remains but public scandal risk rises |

## Cleanup rules

Every decision family needs cleanup when a target dies, leaves the compact, becomes public, joins the target faction, is annexed, or enters war with the target. Missions tied to selected countries should cancel or convert into public compact versions. Hidden-only decisions should close after reveal. Public compact decisions should close after defeat, dissolution, or target capitulation.
