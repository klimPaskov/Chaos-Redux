# Holy Realm Focus Tree Path Specification

The Holy Realm needs a real focus tree or a major overlay branch on Tibet, Bhutan, or Nepal, depending on repository implementation. If the target country already has a meaningful tree and was not event-created, do not blindly replace it. Add an event-specific branch or load the new tree only when the event created or transformed the country.

The design target is a playable long-lived tree with around 75 to 95 focuses. The implementation agent owns exact count, layout, coordinates, prerequisites, bypasses, and final focus names. The final tree must preserve the path logic below.

## Tree identity

The tree is about the tension between ruling a threatened state and seeking liberation from worldly grasping. It must not be a flat reward ladder. Political, teaching, meditation, anti-chaos, diplomacy, industry, military, and Final Silence paths should interact.

A good layout:

- Opening trunk in the center.
- Teaching and meditation paths rise upward like two sides of a wheel.
- Governance and diplomacy branch to the left.
- Industry and sanctuary logistics branch to the lower left.
- Guardian military and anti-chaos defense branch to the right.
- Buddhahood and Final Silence branch at the top, locked until requirements are met.
- Hidden Schism branch appears to the far right or below the mandala if triggered.

## Focus filters

Add focus search filters or tags where the existing repo supports them.

| Filter | Meaning |
| --- | --- |
| `FOCUS_FILTER_HOLY_REALM_BODHI` | Bodhi Progress and Buddhahood requirements |
| `FOCUS_FILTER_HOLY_REALM_TEACHING` | Teaching missions and envoys |
| `FOCUS_FILTER_HOLY_REALM_MEDITATION` | Dhyana Depth, Meditation Charge, mandala GUI |
| `FOCUS_FILTER_HOLY_REALM_SANCTUARY` | Refugees, healing, infrastructure, defensive supply |
| `FOCUS_FILTER_HOLY_REALM_COMPACT` | Sangha Compact diplomacy and aid |
| `FOCUS_FILTER_HOLY_REALM_ANTI_CHAOS` | Powers and combat against chaos countries |
| `FOCUS_FILTER_HOLY_REALM_NIRVANA` | Buddhahood and Final Silence |
| `FOCUS_FILTER_HOLY_REALM_HIDDEN` | Schism and rare routes |

## Opening trunk

Purpose: introduce the Holy Realm, make the country survivable, and unlock the first decisions.

Anchor focuses:

| Focus group | Role | Reward direction |
| --- | --- | --- |
| Hear the Bell in the Mountains | Event start and identity | Adds Fragile Sangha and Remote Sanctuaries, unlocks event details |
| Gather the Sangha | First institution | Adds advisors, small political capacity, unlocks teaching category |
| Protect the Monastery Roads | Early defense | Forts or infrastructure in core mountain states, guard mission unlock |
| Open the Mandala Chamber | GUI unlock | Opens mandala panel and Bodhi display |
| The Bodhisattva's Vow | Route lock into spiritual progression | Adds Bodhi mechanics, unlocks first teaching missions |
| Shelter the First Refugees | Humanitarian branch opener | Refugee mission and Compassion gain |
| Survey the Sacred Valleys | Industry and state-target setup | Identifies named state groups for later construction |
| The World Sends Questions | Diplomacy opener | Unlocks foreign teaching and compact preparation |

Opening tradeoff: rushing defenses should help survival but slow Bodhi. Rushing teaching should improve Bodhi but leave the realm exposed. The player should feel this early.

## Teaching path

Purpose: earn Bodhi Progress through active missions.

Path logic:

- Starts from `The Bodhisattva's Vow`.
- Unlocks mission slots and mission families.
- Later focuses improve teaching reach, target selection, and foreign reaction.
- Requires mission success for later gates.

Focus groups:

| Group | Mechanical content | Notes |
| --- | --- | --- |
| Send the First Envoys | Unlock `Send Dhamma Envoys` | Cost should include support equipment or convoys |
| The Translation Houses | Improve mission reach | Adds civilian or radio infrastructure, not only a modifier |
| Teach Under Bombardment | Target countries at war with chaos | Strong Bodhi reward, high risk |
| The Refuge Vows | Shelter refugees | Adds manpower or stability tradeoff and Compassion |
| The Four Directions | Unlock more mission slots | Requires success in multiple regions |
| The Wheel in Foreign Courts | Diplomatic recognition of teaching | Improves relations and compact eligibility |
| The Teacher Does Not Conquer | Penalizes ordinary conquest | Gives Detachment and clean-route tracking |
| Many Lamps, One Flame | Capstone before Buddhahood | Requires many teaching successes and unlocks final transformation gate |

Avoid turning this path into repeated political power purchases. It should use mission objectives, corridors, supplies, and target conditions.

## Meditation path

Purpose: unlock Dhyana Depth and Meditation Charge.

Path logic:

- Starts after mandala panel unlock.
- Each Dhyana focus should require both focus progress and a completed meditation action.
- Dhyana Depth is not only a focus reward.
- The path gates Buddhahood and powers.

Focus groups:

| Group | Mechanical content | Tradeoff |
| --- | --- | --- |
| Sit Beneath the Prayer Flags | Unlock First Dhyana vow | Short opportunity cost |
| The Breath Does Not Break | Meditation Charge cap 25 | Lower offensive momentum while active |
| The Second Quiet | Unlock Second Dhyana | More stable teaching, higher retreat cost |
| Lay Down the Iron Bell | Reduce Defilements | Costs equipment or military readiness |
| The Third Quiet | Unlock Third Dhyana | Stronger sanctuary defense, slower expansion |
| The Fourth Quiet | Unlock Fourth Dhyana | Required for Buddhahood, difficult if at war |
| The Unshaken Seat | Final pre-Buddha focus | Requires Bodhi 108, low Defilements, Dhyana 4 |

The path should include visible mandala and portrait changes after major focuses.

## Governance branch

Purpose: decide how the Holy Realm handles state power.

This branch should create internal politics without turning the realm into ordinary ideology routes. It should still affect leaders, advisors, party names, laws, and decision behavior.

Suggested route choices:

| Route | Meaning | Mechanical style | Tradeoff |
| --- | --- | --- | --- |
| The Council of Abbots | Collective spiritual governance | Better teaching, stable Detachment, weaker rapid mobilization | Slow response to war |
| The Protector Regent | A worldly regent shields the Bodhisattva | Better military and diplomacy, higher Defilements risk | Can create Schism pressure |
| The Pilgrim Assembly | Lay and monastic representatives | Strong refugee and compact route | Less powerful powers and slower discipline |

These can be soft route locks rather than hard mutual exclusions if implementation needs flexibility. At least one governance choice should change the displayed country identity or ruling party name.

Anchor focuses:

- Convene the Council of Abbots.
- Name the Protector Regent.
- Seat the Pilgrim Assembly.
- Seal Worldly Offices.
- The State Serves the Path.
- The Path Does Not Serve the State.

## Industry and sanctuary logistics branch

Purpose: make the Holy Realm playable and grounded in terrain.

This branch must build on the map. Avoid only national spirits.

Focus groups:

| Group | Map effect | Linked decisions |
| --- | --- | --- |
| Mountain Granaries | Add infrastructure and supply capacity in core states | Shelter refugees |
| Pilgrimage Roads | Rail and infrastructure links | Guard pilgrimage route |
| Monastery Workshops | Military and support equipment production | Equip guardian units |
| The Paper and Radio Houses | Civilian industry, radio or agency support | Translate the Wheel |
| Snowline Clinics | Support equipment, field relief | Heal the Terrified |
| Fortress Without Hatred | Forts and anti-air in sanctuary states | Defensive vow missions |
| Storehouses for the World | Supply hubs or logistics bonuses | Sangha relief decisions |

Capstone: `The Sanctuary That Feeds Armies` should give strong supply and support to compact members fighting chaos, not only factories.

## Guardian military branch

Purpose: make a defensive military route that fits the Holy Realm.

This branch should not glorify aggression. It builds guardians, mountain defense, relief columns, and anti-chaos formations.

Focus groups:

| Group | Military content | Notes |
| --- | --- | --- |
| Temple Guards | Unlock small elite guard template | Defensive, limited count |
| Mountain Pass Detachments | Mountain infantry bonuses and units | State-specific if possible |
| The Bell and Rifle | Convert irregulars into regulars | Costs infantry equipment and army XP |
| Guard the Pilgrimage Columns | Tied to convoy or escort missions | Works with teaching path |
| No Blade for Anger | Defensive doctrine and lower Defilements from war | Reduces offensive war tools |
| Wrathful Protection | Emergency anti-chaos route | Requires chaos threat or capital danger |
| The Unbroken Pass | Fortified sanctuary capstone | Strong defense against chaos |

Unit rewards should be route-specific, such as Temple Guards, Pilgrimage Escorts, Mountain Pass Detachments, and Relief Columns. Do not repeat generic infantry division rewards.

## Diplomacy and Sangha Compact branch

Purpose: create a faction or compact only when diplomacy and crisis justify it.

The Sangha Compact is a defensive humanitarian bloc. It should not form just because the Holy Realm exists.

Membership rules:

- Must not be a chaos country.
- Must be threatened by chaos, aligned by teaching, or diplomatically prepared.
- Must not be a current ordinary conquest target of the Holy Realm.
- Ideology compatibility should matter, but humanitarian crisis can override it.
- Minimum membership or at least one real crisis should be required for formal creation.

Focus groups:

| Group | Unlock | Failure or risk |
| --- | --- | --- |
| Letters to the Lowlands | Recognition missions | Rejection lowers cohesion |
| The Refugee Mandate | Aid corridors | Supply strain |
| Convene the Sangha Compact | Faction or compact creation | Requires members or crisis |
| The Shared Granary | Shared relief decisions | Factory or convoy burden |
| The War Council of Compassion | Anti-chaos coordination | Risk of militarizing the path |
| No Puppet Shall Wear the Robe | Anti-puppet clauses | Patron pressure from major powers |
| Witnesses to the Final Wheel | Final Silence support | Needed for clean aftermath |

The compact needs cohesion, shared decisions, and AI behavior. A member that is ignored during chaos invasion can leave or lose faith.

## Expansion and liberation branch

A large tree needs an expansion or regional ambition branch, but for the Holy Realm it should not be a normal conquest tree. Use liberation, sanctuary protection, pilgrimage corridors, and anti-chaos intervention.

Route name: `The Pilgrimage Mandala`.

Possible ambitions:

- Secure named sanctuary corridors near the Himalayas.
- Protect Buddhist or refugee sites if the repo has state groups for them.
- Liberate compact members from chaos occupation.
- Demand safe passage for envoys.
- Create protectorates only after severe chaos collapse or explicit compact vote.
- Integrate territories slowly through local support and missions.

Focus groups:

| Group | Action | Postwar handling |
| --- | --- | --- |
| Mark the Pilgrimage Roads | Claims or access requests on corridor states | No instant cores |
| Send the Bell Across the Passes | Border incident or guarantee decisions | Defensive focus |
| Protect the Sacred Valleys | War goal or intervention only against chaos occupiers | Local autonomy missions |
| Mandala Protectorates | Protectorate decisions for rescued microstates | Compact cohesion checks |
| The High Road to Peace | Postwar settlement and demobilization | Reduces Defilements |
| No Empire of the Wheel | Capstone that blocks predatory conquest | Clean route reward |

This branch should create visible map and diplomacy outcomes, but it must avoid free core spam.

## Anti-chaos powers branch

Purpose: prepare and improve powers after Buddhahood.

Most focuses should be locked until the Buddha exists or until a high-chaos emergency creates a preview.

Focus groups:

| Group | Unlock | Requirements |
| --- | --- | --- |
| Read the Pattern of Suffering | Better chaos targeting | Pattern evolution or world threat |
| Powers Are Not Toys | Lowers ordinary-war abuse | Detachment threshold |
| One Becomes Many | Power upgrade | Buddhahood and Meditation Charge use |
| Path Through Walls | Power upgrade | Chaos enemy fought or fort state target |
| Lotus Bridge | Walking on Water upgrade | River or coastal rescue need |
| Vanishing from Sight | Evacuation and resistance upgrade | Occupied compact member or chaos border |
| Seated in the Sky | Emergency redeploy | Compact capital threat |
| Touch the Sun and Moon | Global anti-chaos capstone | High World Suffering |

## Buddhahood and Final Silence branch

This branch sits at the top and should be visually distinct.

Focus sequence:

1. `The Unshaken Seat`: checks Bodhi, Dhyana, Defilements, and teaching successes.
2. `The Awakened One`: fires transformation if not already fired.
3. `Show the Powers`: unlocks first power display event and buff.
4. `The Last Wheel`: unlocks Final Silence ritual decisions.
5. `Witnesses Gather`: requires compact, teaching network, or global crisis witnesses.
6. `Extinction of Defilements`: requires low Defilements and high Meditation Charge.
7. `The Final Silence`: starts ritual or completes final stage depending on implementation.
8. `The Empty Seat`: aftermath focus if non-terminal completion occurs.

The Final Silence branch should not be available from focus alone. It must require the decision or mission ritual.

## Hidden Schism branch

The False Buddha Schism branch appears only if the evolution triggers.

Possible path outcomes:

| Path | Meaning | Result |
| --- | --- | --- |
| Debate the Pretender | Resolve through teaching | Defilements decrease, slower progress |
| Exile the Echo | Remove immediate risk | Schism can return abroad |
| Break the False Mandala | Military suppression | Fast, but raises Defilements and disqualifies clean achievements |
| Absorb the Shadow | High-chaos shortcut | Strong powers, corrupted route, no clean Final Silence |

This branch should not be a free power route. It creates replay value and danger.

## Idea lifecycle

| Idea | Start or unlock | Starting role | Mitigation | Upgrade | Failure |
| --- | --- | --- | --- | --- | --- |
| Fragile Sangha | Start | Weak state capacity | Opening focuses | Council of Abbots or Pilgrim Assembly | Schism worsens it |
| Remote Sanctuaries | Start | Defense and isolation | Pilgrimage Roads | Sealed Valleys or Open Sanctuaries | Supply strain under refugees |
| Worldly Burden | Start | Defilements from state action | Renunciation focuses | Removed at Buddhahood | Turns into Worldly Mandala under abuse |
| The Awakened Seat | Buddhahood | Permanent leader identity | Not removed | Power branch upgrades | Corrupted if schism wins |
| Revealed Powers of the Buddha | First power display | Timed anti-chaos buff | Renewed by meditation | Upgraded by powers branch | Disabled by ordinary-war abuse |
| Empty Seat | Final Silence aftermath | Successor order | Stabilized by compact | Guardianship of the Wheel | Broken if ritual fails |

## AI focus behavior

AI Holy Realm should prioritize survival and teaching early. It should not rush Final Silence without the required state. It should choose governance based on situation:

- Weak and threatened AI prefers Protector Regent.
- Peaceful AI with high stability prefers Council of Abbots.
- Refugee-heavy AI prefers Pilgrim Assembly.
- High chaos AI may unlock Wrathful Protection.
- AI should avoid ordinary conquest unless threatened or route-corrupted.
- AI should only start Final Silence when chaos is very high, requirements are met, and capital is safe.

AI weights must read war state, stability, Dhyana Depth, Defilements, compact status, chaos threat, and enemy proximity. Flat weights are not acceptable.

## Route coverage requirement for implementation report

The implementation agent must include a route coverage table with these required routes:

| Required route | Must exist in implementation |
| --- | --- |
| Opening survival trunk | Yes |
| Teaching mission path | Yes |
| Meditation and Dhyana path | Yes |
| Governance route family | Yes |
| Industry and sanctuary logistics | Yes |
| Guardian military | Yes |
| Sangha Compact diplomacy | Yes |
| Liberation or pilgrimage expansion | Yes |
| Anti-chaos powers | Yes |
| Buddhahood and Final Silence | Yes |
| Hidden Schism branch | If evolution triggers are implemented |

Missing, merged, simplified, or fallback routes must be reported clearly.
