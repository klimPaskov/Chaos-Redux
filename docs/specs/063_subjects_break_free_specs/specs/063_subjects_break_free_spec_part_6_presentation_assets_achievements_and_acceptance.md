# Event 063: Subjects Break Free

## Part 6: Presentation, assets, achievements, and acceptance

## Presentation hierarchy

Event 063 can affect several countries in one firing. Presentation must show the scale without opening one global popup for every release.

### One global report per firing

The global report identifies:

- completed release count
- number of former overlords affected
- negotiated or recognized separations
- contested separations
- independence wars opened
- whether one coordinated cohort formed
- the main actor country

The main actor should normally be the highest-weight released country, the largest released country, or the war leader when a compound war begins. The choice should follow the event's most important visible outcome, not always state count.

The report should name a bounded set of important countries and summarize the remaining releases by count. It should not produce an unreadable list when six or eight countries are freed.

### Direct affected-country notices

Every human-controlled released country receives one direct settlement event. A human former overlord receives one batch reaction event. AI countries resolve through hidden events or effects and do not create popup spam.

Human players not directly affected receive the global report only.

### News events

Global news is reserved for the first occurrence of a major Event 063 threshold:

- the first coordinated same-overlord breakaway cohort
- the first compound independence war
- the first successful Liberation Pact congress

Later occurrences use reports, country events, and Event Logs unless a separate campaign development justifies news through another owner system.

## Event Logs integration

## Event catalog row

Event Details should present:

- the premise that several existing subjects can become independent
- the scaling release batch
- preserved country state
- mixed peaceful and hostile settlements
- cooperation with Independence Wave and compatible Soviet successors
- the three evolution directions
- Liberations cluster membership and Medium severity

The premise text should not list hidden weights, exact AI formulas, or future secret outcomes.

## Event history row

One normal Event 063 history row is recorded per firing. The row should include:

- Event ID 63
- Minor Repeatable type
- firing date
- main actor country
- completed release count
- affected former-overlord count
- outcome summary
- active evolution context

The detail view can list each released country, former overlord, settlement mode, and whether the country entered a coordinated cohort or independence war.

## Evolution history

Evolution rows use the real defining actor:

- first coordinated cohort member for Evolution I
- first breakaway war leader for Evolution II
- Pact founder for Evolution III

Catalog evolution descriptions must not display fake dates or actors.

## Cluster history

When the Liberations cluster fires, the cluster row records Event 063 as fired or skipped with a reason. Event 063 still records its own event history and released countries.

## Weight display

Event 063 displays `N/A` when no valid subject exists. A zero numeric weight would wrongly imply an available event with a low roll chance.

## Localisation direction

Final player-facing wording is written during implementation. The following rules define viewpoint, information, and tone.

### Main report

Viewpoint: international observers and governments processing several declarations at once.

Visible information:

- dependent ministries now issuing independent orders
- local armed forces receiving national command
- border posts and diplomatic offices changing authority
- former overlords choosing recognition, negotiation, or coercion
- the number and location of important releases

Tone: factual, tense, and specific. The report can show uncertainty about each settlement without pretending that independence itself is uncertain.

Avoid:

- generic map-change language
- triumphant slogans applied to every country
- claims that all subjects share one ideology or movement
- administrative phrases that sound like developer notes
- broad moral conclusions that ignore hostile or opportunistic breakaways

### Released-country event

Viewpoint: the new independent government's cabinet, officers, and civil service.

Visible information:

- independence has already taken effect
- which agreements remain unsettled
- whether the former overlord recognized the change
- immediate risks involving access, forces, borders, trade, or war

Tone varies by posture:

- conciliatory text stresses continuity and practical settlement
- guarded text stresses control and caution
- defiant text stresses resolve and military preparation

The option wording can use restrained official language, bitter understatement, or a country-appropriate political register. Cultural references require research before use.

### Former-overlord batch event

Viewpoint: a government facing several lost subject relationships.

Visible information:

- the released countries
- strategic ties at risk
- military and faction implications
- whether force is practical

Tone varies by government and campaign state. A collapsing wartime government should sound pressured. A strong coercive government can sound possessive or threatening. A pragmatic government should focus on influence, access, and alliances.

The event should not frame recognition as passive surrender when it preserves useful relations. It should not hide the real risk of a restoration policy.

### Coordinated cohort news

Viewpoint: foreign observers identifying deliberate cooperation among several former subjects of one government.

Visible information:

- declarations were coordinated
- members recognize or support each other
- the former overlord now faces a group settlement

Tone: organized political rupture, not a random list of released tags.

### Independence war news

Viewpoint: reports from mobilization points, ports, rail lines, and divided commands.

Visible information:

- the former overlord rejected the settlement
- several breakaway states may be acting together
- foreign liberated states are considering support

Tone: serious and concrete. Avoid cheap humour, heroic certainty, and generic claims that the whole world has entered war.

### Liberation Pact news

Viewpoint: states attending or observing a congress.

Visible information:

- independent states adopted a practical charter
- the Pact concerns recognition, aid, and defense
- membership crosses at least one release origin when applicable
- other factions and former overlords are evaluating the bloc

Tone: institutional and strategic. Avoid presenting the Pact as a world government or a guaranteed ideological alliance.

### Decision and mission text

Every action should state:

- the target
- the public purpose
- the real cost
- the immediate visible result
- the condition that blocks it

Do not reveal hidden candidate weight, intervention weight, or future AI behavior. Support actions should clearly distinguish recognition, aid, guarantee, volunteers, and direct intervention.

### Achievement text

Final achievement names and descriptions should be short and tied to the completed feat. Working labels in the achievement plan are identifiers, not final localisation.

## Static decision-category presentation

The decision category uses:

- one small category icon
- one static `114x101` category picture, subject to the verified active consumer
- phase-specific dynamic description text
- Liberation Cohesion and its band after Pact formation
- the staged Pact Charter spirit as the visual state for cohesion

The category picture should show a period documentary scene of delegates, border officials, or newly national command structures. It must not contain fake buttons, fake meters, or generated text.

## Asset coverage matrix

All names below are working asset identifiers. Final runtime names can follow repository conventions while preserving one-to-one coverage.

### Report and news images

| Requirement ID | Working asset | Surface | Size | Direction | Source mode |
| --- | --- | --- | ---: | --- | --- |
| 063-IMG-01 | `report_event_063_subjects_break_free` | Main report | 210x176 | Officials or soldiers transferring local command at a border post, ministry, railway office, or barracks. The scene should support several regions without using a readable real flag as the main subject. | Generated fictional period documentary image, then standard report-card processing |
| 063-IMG-02 | `news_event_063_coordinated_breakaway` | First coordinated cohort news | 397x153 | Delegates or officers from several newly independent governments meeting over maps and dispatches. | Generated fictional period-news image |
| 063-IMG-03 | `news_event_063_independence_war` | First compound war news | 397x153 | Mobilization and divided command around a rail junction, frontier, port, or depot. | Generated fictional period-news image |
| 063-IMG-04 | `news_event_063_liberation_pact` | First Pact congress news | 397x153 | A formal congress of several states signing or exchanging a charter without readable generated text. | Generated fictional period-news image |

Report and news images should use black-and-white documentary treatment. The report image receives the Chaos Redux sepia card process. News images stay black and white.

### Decision-category assets

| Requirement ID | Working asset | Surface | Direction |
| --- | --- | --- | --- |
| 063-CAT-01 | `decision_category_063_liberation_affairs` | Small category icon | Broken chain integrated with a plain diplomatic document or border seal. No text. |
| 063-CAT-02 | `decision_category_picture_063_liberation_affairs` | Static category picture | Period delegates, border officials, or command transfer. One strong subject, no fake controls. |

The asset worker must inspect the canonical decision-category icon and picture references. The reference picture family uses `114x101`, but the live consumer decides the final canvas.

### Decision and mission icons

| Requirement ID | Working asset | Intended use | Direction |
| --- | --- | --- | --- |
| 063-DEC-01 | `decision_063_recognition` | Recognition and diplomatic acceptance | Diplomatic seal, opened gate, or exchanged credentials |
| 063-DEC-02 | `decision_063_settlement` | Negotiated separation and mediation | Two documents or hands across a border line |
| 063-DEC-03 | `decision_063_command` | Secure national command | Officer insignia, dispatch case, or command baton |
| 063-DEC-04 | `decision_063_frontier` | Frontier preparation | Border post, field fortification, or guarded crossing |
| 063-DEC-05 | `decision_063_guarantee` | Guarantee or collective pledge | Shield beside a small document or linked emblems |
| 063-DEC-06 | `decision_063_material_aid` | Equipment and logistics support | Crate, rail wagon, or convoy package |
| 063-DEC-07 | `decision_063_advisers` | Advisers and volunteers | Staff map, cap badge, or officer group symbol |
| 063-DEC-08 | `decision_063_supply_corridor` | Open a supply route | Rail and ship route crossing a frontier |
| 063-DEC-09 | `decision_063_mediation` | Mediation and ceasefire | Balanced documents, table, or neutral seal |
| 063-DEC-10 | `decision_063_independence_support` | Support a remaining subject | Open chain link with a small rising banner shape, without a real flag |
| 063-DEC-11 | `decision_063_congress` | Call the Pact congress | Circular table, charter folder, or grouped seals |
| 063-DEC-12 | `decision_063_membership` | Invite member, partner, or observer | Linked emblems with one open place |
| 063-DEC-13 | `decision_063_collective_defense` | Coordinate Pact defense | Several shields around one central shield |
| 063-DEC-14 | `decision_063_ultimatum` | Restoration ultimatum | Sealed demand beside a mobilization order |

Decision icons are `32x32` and must remain readable at native size. Related decision families should share shape language without reusing one icon for several unrelated actions.

### Idea and cohesion-state icons

| Requirement ID | Working asset | State | Direction |
| --- | --- | --- | --- |
| 063-IDEA-01 | `idea_063_contested_sovereignty` | Disputed independence | Split seal, disputed border document, or incomplete recognition mark |
| 063-IDEA-02 | `idea_063_former_authority_disputed` | Former-overlord pressure | Cracked authority seal or broken administrative chain |
| 063-IDEA-03 | `idea_063_independence_war_mobilization` | Breakaway wartime condition | Mobilization paper, depot, and national command symbol |
| 063-IDEA-04 | `idea_063_pact_charter_fractured` | Cohesion 0 to 24 | Separated charter pages or disconnected emblems |
| 063-IDEA-05 | `idea_063_pact_charter_consultative` | Cohesion 25 to 49 | Several emblems around an open table |
| 063-IDEA-06 | `idea_063_pact_charter_coordinated` | Cohesion 50 to 74 | Linked charter and shield forms |
| 063-IDEA-07 | `idea_063_pact_charter_united` | Cohesion 75 to 100 | Complete linked shield and charter composition |

Idea icons are `64x64`. The four Pact states must read as one progression family.

### Faction emblem

| Requirement ID | Working asset | Surface | Direction |
| --- | --- | --- | --- |
| 063-FAC-01 | `faction_063_liberation_pact` | Liberation Pact identity | Several open chain links arranged around a shield or charter. Avoid a globe, specific continent, or one ideology's symbol. |

The final canvas and frame behavior must follow the canonical faction-emblem reference and live consumer.

### Achievement icon triplets

Each achievement needs completed, grey, and not-eligible states at `64x64`, using the repository achievement templates and unchanged red not-eligible overlay.

| Requirement ID | Achievement ID | Icon direction |
| --- | --- | --- |
| 063-ACH-01 | `chaosx_achievement_063_independence_secured` | A recognized seal beside a broken chain and a small support crate |
| 063-ACH-02 | `chaosx_achievement_063_pact_founder` | A complete charter ring with six linked emblems |
| 063-ACH-03 | `chaosx_achievement_063_independence_war_victory` | A defensive shield holding against a restored chain or crown-like authority mark, without a real state emblem |
| 063-ACH-04 | `chaosx_achievement_063_peaceful_release` | Several open chain links placed beside a signed settlement document |

## Achievement design

## Achievement 1: Independence Secured

Working ID: `chaosx_achievement_063_independence_secured`

Eligible country:

- a country freed by Event 063

Conditions:

- remain independent for at least 730 days after the release
- secure recognition from the former overlord
- materially support another active liberated state through equipment, logistics, guarantee, volunteers, or successful mediation
- remain existent and not subject at completion

Disqualifiers:

- force-trigger or scenario setup where shared achievement rules disallow achievements
- re-subjugation during the required period
- support satisfied only by a trivial diplomatic click with no material effect

Difficulty: Medium.

Why it is not trivial: the player must survive, settle the former-overlord dispute, and help another breakaway.

## Achievement 2: Pact Founder

Working ID: `chaosx_achievement_063_pact_founder`

Eligible country:

- the founder or later valid leader of the Event 063 Liberation Pact

Conditions:

- form the Pact after Evolution III becomes active
- reach at least six full members
- include at least two liberation origins among full members
- maintain Liberation Cohesion at 75 or higher for 365 continuous days
- have no full member in subject status at completion

Disqualifiers:

- partner states counted as full members
- members created only through force setup where shared achievement rules disallow the run
- cohesion duration interrupted by falling below 75

Difficulty: Hard.

Why it is not trivial: formation, cross-origin recruitment, defense commitments, and sustained cohesion are all required.

## Achievement 3: Independence War Victory

Working ID: `chaosx_achievement_063_independence_war_victory`

Eligible country:

- breakaway war leader in an Evolution II independence war

Conditions:

- win or secure a peace that preserves independence against a stronger former overlord at war start
- fight with at least one other former subject from the same coordinated cohort
- receive material or military support from at least one external liberated state
- remain independent after the peace

Disqualifiers:

- the former overlord was not stronger at the frozen war-opening snapshot
- the external supporter was already the same country or a duplicate support hook
- the result restores subject status

Difficulty: Hard.

Why it is not trivial: the achievement requires a disadvantaged compound war and cross-network support.

## Achievement 4: Peaceful Release

Working ID: `chaosx_achievement_063_peaceful_release`

Eligible country:

- a former overlord affected by Event 063

Conditions:

- recognize at least four subjects released from one Event 063 firing
- begin no restoration war against them for 730 days
- do not re-subjugate them during that period
- maintain positive relations with at least three of the released countries at completion

Disqualifiers:

- recognition occurs only after the former overlord is defeated in an independence war
- a proxy or subject controlled by the player performs the forbidden restoration action
- the batch did not contain four completed releases

Difficulty: Medium to Hard.

Why it is not trivial: the player gives up direct control and must preserve useful post-independence relations.

## Achievement tracking

Tracking should use bounded country and transaction records:

- release transaction ID and date
- former overlord
- cohort membership
- war-opening relative strength snapshot
- external supporter identity
- recognition date
- independence continuity
- full Pact member count and origin mix
- cohesion threshold start date
- forbidden restoration or re-subjugation flags

A save and reload must preserve all progress. Repeated event firings must not overwrite an active achievement attempt with an unrelated later release.

## Acceptance criteria

## Core release

- release count scales with the frozen valid pool
- existing subject countries become independent in place
- country state remains intact
- selected countries are reserved before release
- selection does not change after the first country becomes independent
- failed late candidates do not reverse successful releases
- no valid candidate produces `N/A` weight

## Settlement

- independence cannot be vetoed
- human subject and former-overlord choices resolve without multiplayer deadlock
- peaceful, recognized, contested, and armed outcomes are distinct
- agreements follow the outcome matrix
- common-war topology blocks unsafe direct conflict
- restoration war aims target subject restoration, not default annexation
- claims stay narrow and are cleaned after settlement

## Cooperation and Pact

- Event 063, Event 006, and compatible Event 005 countries retain distinct origins
- first origin survives later Event 063 release
- informal recognition and support remain bounded
- factioned countries remain in their existing factions and become Pact partners
- congress formation needs a viable group
- Liberation Cohesion is the only persistent public Event 063 value
- cohesion affects decisions and obligations
- leadership, admission, exit, expulsion, suspension, and dissolution work

## Evolutions and clusters

- each evolution supports active-event and pre-fire entry
- evolution activation adds no direct Chaos
- Evolution I creates a bounded cohort
- Evolution II permits at most two new war theaters per firing across one compound cohort war and any individual armed refusal
- Evolution III requires a congress
- Liberations cluster reservations prevent release collisions
- Event 063 keeps its own history inside a cluster firing
- Domestic Unrest integration waits for a registered stable ID

## Decisions and AI

- decision category remains phased and readable
- costs use appropriate real resources
- active decisions and missions stay within visibility caps
- AI passes the named probability scenario ordering
- material aid is more common than direct intervention
- invalid, distant, or impossible routes receive zero or near-zero practical weight
- aid, cohesion, claims, war goals, and release cycles cannot be farmed

## Presentation and assets

- one global report appears per firing
- directly affected human countries receive the correct event
- AI countries do not create popup spam
- first-use news thresholds fire once
- Event Logs show actor, count, outcome, and evolution context
- every accepted asset row has a source, processed output, runtime registration, consumer, and audit status
- icons remain readable at native size
- final text follows the viewpoint and information rules without copying working labels as localisation

## Documentation

- the authoritative event workbook row is updated
- the Liberations cluster member list includes Event 063 at Medium severity
- CSV exports are regenerated from the workbook
- event docs, decision docs, asset manifests, and shared-system docs agree
- implementation completion reports all blocked or changed design points instead of silently simplifying them
