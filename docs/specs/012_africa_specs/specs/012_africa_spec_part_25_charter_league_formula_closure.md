# 012 Africa spec part 25, Charter League and integration formula closure

This file closes the Charter League design at the planning level. It expands formulas, target states, refusal logic, rival bloc behavior, member routes, and cleanup rules. It remains design-facing and avoids final script constants.

## League values

The Charter League should track each important member or target through dynamic values. These values can live as variables, scripted localisation, decision category headers, or a compact scripted GUI if implementation chooses one.

| Value | Meaning | Rises from | Falls from | Unlocks |
| --- | --- | --- | --- | --- |
| `member_confidence` | Trust that the unifier protects autonomy and survival | Defense aid, aid convoys, honored autonomy, shared victories, low resistance | Coercion, failed defense, ignored demands, heavy occupation, rival influence | Federation votes, regional projects, voluntary integration |
| `unifier_influence` | Practical pull over a member or target | Advisors, rail projects, arms aid, war aid, cultural missions, sponsor absence | Rival aid, ideological mismatch, autonomy fear, foreign guarantees | Puppet route, integration talks, member law harmonization |
| `autonomy_demand` | Member desire to retain separate institutions | Strong local history, restored polity identity, high confidence, regional power | Long war dependence, economic dependency, low ruling stability | Federal member route, autonomy charter, refusal if ignored |
| `rival_appeal` | Attraction to a rival bloc or breakaway league | Coercion, foreign pressure, ideological mismatch, stronger neighbor, low confidence | Protection, aid, shared enemies, internal settlement | Rival bloc creation, League exit, anti-unifier coalition |
| `resistance_pressure` | Local backlash against absorption | Forced annexation, low compliance, disease blowback, cultural insult, state damage | staged integration, local support, restored polity privileges, regional investment | revolts, stalled cores, failed integration missions |
| `league_cohesion` | Whole-League durability | successful defense, common projects, fair burden sharing | rival blocs, defeats, coercion, broken autonomy promises | joint war declarations, continental negotiations, League super-event thresholds |

## Member confidence formula direction

Use a component model. Implementation can store components or compute a temporary score. The player should see a readable breakdown.

`member_confidence = base + protection + aid + autonomy + victory + local_support + ideology_fit - coercion - losses - resistance - rival_pressure - exhaustion`

| Component | Direction |
| --- | --- |
| base | Higher for small threatened members, lower for strong independent members |
| protection | Rises when the unifier defends the member from a coloniser or hostile outside power |
| aid | Rises from equipment, construction, rail, port, convoy, and food missions |
| autonomy | Rises if the unifier grants route-appropriate local institutions |
| victory | Rises after successful joint wars or defended capitals |
| local_support | Rises when regional support projects complete |
| ideology_fit | Small bonus when route and member politics align |
| coercion | Large penalty from forced annexation, ultimatums, or command route pressure |
| losses | Penalty from member casualties and state devastation |
| resistance | Penalty from high resistance or failed coring missions |
| rival_pressure | Penalty from rival bloc influence and foreign sponsor activity |
| exhaustion | Penalty from long wars, convoy losses, and repeated emergency levies |

## Target-state phases

Every African country that is not immediately hostile should move through target states.

| State | Entry condition | Player tools | AI behavior | Exit paths |
| --- | --- | --- | --- | --- |
| `uncontacted` | Valid African capital country not yet approached | Scout diplomacy, anti-colonial signal, contact mission | AI waits, evaluates threat | contacted, hostile, protected |
| `contacted` | Unifier opens talks or offers aid | Recognition, observer mission, first aid | AI accepts if threatened or ideologically compatible | observer, refusal, rival contact |
| `observer` | Country accepts low-risk League contact | Small aid, shared intelligence, port or rail surveys | AI tests benefits | associate, refusal, rival contact |
| `protected` | Target is at war with a coloniser or outside power and receives aid | Intervention, volunteers, equipment convoys, defense guarantee | AI values survival over autonomy if threatened | member, associate, puppet pressure, resentment |
| `associate` | Target joins a loose League layer | Member confidence work, joint projects | AI joins League votes cautiously | member, rival bloc, exit |
| `member` | Target becomes normal League member | confidence projects, shared defense, regional integration | AI considers federation or autonomy route | federal member, puppet, annexation crisis, exit |
| `federal_member` | Member chooses negotiated federal route | autonomy charter, local government, staged cores | AI uses high confidence and autonomy guarantee | integrated region, permanent autonomous member |
| `dependent_member` | Member relies heavily on unifier aid | protection, rail, security, budget support | AI may accept puppet route | puppet, federal member, exit if overpressured |
| `rival_contact` | Target receives rival influence | counter-influence, exposure, concessions | AI may form rival bloc | rival bloc, reconciliation, war |
| `hostile` | Target rejects or attacks | border defense, war prep, mediation | AI considers war or foreign sponsor | war, truce, forced settlement |
| `integration_crisis` | Member is pushed too fast | emergency negotiations, stand down, coercion, autonomy | AI tests unifier weakness | federal deal, puppet deal, revolt, secession |

## Refusal logic

Refusal should not be random. A strong member can refuse because it has real reasons.

A target should refuse or resist when several of these are true.

- It has high industry or manpower compared with the unifier.
- It controls a defensible capital and is not at war with a coloniser.
- It has strong autonomy demand and the unifier route ignores autonomy.
- It has an incompatible ideology and no shared enemy.
- Its member confidence is low.
- Rival appeal is high.
- It has foreign guarantees or a powerful sponsor.
- The unifier recently used coercive annexation.
- League cohesion is low.
- It has a restored polity identity that expects special treatment.
- It remembers failed defense or abandoned aid missions.

## Rival bloc formation

A rival bloc should form only when there is enough political substance. It should not appear from one refusal.

Minimum formation direction:

1. At least one strong African country or restored polity has high rival appeal.
2. At least two associate or member states have low confidence, or one strong state has foreign backing.
3. The unifier has used coercion, failed a defense, or pushed integration before member confidence is ready.
4. The rival bloc has a public claim, such as autonomy protection, anti-command resistance, anti-monarchy stance, anti-revolutionary defense, or anti-high-chaos containment.

Rival bloc outcomes:

| Outcome | Trigger direction | Consequence |
| --- | --- | --- |
| Negotiated rival bloc | Rival appeal is high, but war exhaustion is high too | Creates a competing African faction with reconciliation decisions |
| Armed rival bloc | Rival appeal is high and foreign backing or unifier coercion is high | Starts border incidents, exits League, may declare war |
| Restoration bloc | Multiple restored polities fear absorption | Creates autonomy pact and demands federal guarantees |
| Anti-chaos bloc | Deep Green or disaster pressure is visible | Locks high-chaos diplomacy, invites containment |
| Foreign-backed bloc | Outside power pressure is high | Triggers Scramble reaction tree early |

## Member route outcomes

| Route | Requirements | Effects direction | Risk |
| --- | --- | --- | --- |
| Voluntary federation | high confidence, low rival appeal, autonomy charter, shared project success | staged cores, member institutions, strong cohesion | slowest route |
| Autonomous federation | high autonomy demand and positive confidence | member remains visible or semi-subject, shares defense and projects | weaker central control |
| Protectorate | dependent member, low confidence but high threat | subject status, defense and aid projects | later resentment |
| Puppet absorption | dependent member, high unifier influence, route supports central control | puppet then integration missions | rival appeal and resistance |
| Coercive annexation | low confidence, command or high-chaos route, military success | rapid control, claims, delayed cores | revolt, foreign reaction, League cohesion damage |
| Exit and reconciliation | member confidence recovers after exit | renewed observer or associate status | requires concessions |
| Secession war | rival appeal and hostility overwhelm confidence | war, foreign involvement, postwar settlement | can cascade |

## Cleanup rules

The League system must clean itself when scopes become invalid.

| Cleanup case | Required cleanup |
| --- | --- |
| Member annexed by third party | remove member flags, cancel missions, clear target selectors |
| Member annexed by unifier | convert to region integration state, clear membership values only after missions finish |
| Unifier changes tag or cosmetic tag | preserve League ownership and variables through event targets or saved owner state |
| Civil war splits the unifier | assign League leadership to continental side if RSA branch or to winner if normal civil war |
| League member leaves | remove shared defense missions, keep memory flag for reconciliation or rival appeal |
| Rival bloc forms | migrate relevant members, hide incompatible League decisions, reveal counter-bloc category |
| World-end route starts | close normal League growth and preserve only continental war systems |
| High-chaos route unlocks | apply nonhuman and disaster safety gates before any member action can target humans by caricature |

## Regional selector rules

Selectors should use region groups, not raw state id lists in player text. The exact state ids remain implementation work, but the player should see readable region names.

| Selector | Uses |
| --- | --- |
| `north_africa_selector` | Mediterranean, Nile, Sahara, Maghreb projects |
| `west_africa_selector` | Gulf of Guinea, Sahel trade, Black Star return, Asante, Oyo, Benin or Edo |
| `sahel_selector` | Garamantes, Kanem-Bornu, Songhai, Sokoto, Futa routes |
| `nile_horn_selector` | Kush, Nubia, Makuria, Alodia, Aksum, Red Sea routes |
| `swahili_indian_ocean_selector` | Kilwa, Zanzibar, Swahili city states, island lanes |
| `central_forest_selector` | Kongo, Kuba, Luba, Lunda, Kazembe, Deep Green safety |
| `southern_africa_selector` | Zulu, Great Zimbabwe, Mutapa, Rozwi, RSA civil war, Barotse |
| `island_selector` | Madagascar, Comoros, Mauritius, Seychelles, returnee island lanes |

## Implementation acceptance

The implementation is incomplete if the League only invites countries, annexes them, or gives flat bonuses. It must have target states, member confidence, refusal logic, rival bloc formation, route-specific integration outcomes, cleanup, and AI behavior.
