# Event 019 Infantry Spawn spec part 4, Evolution III possessed generals and revolt logic

This file defines the Evolution III crisis layer. It uses working labels only.

## Evolution III identity

At Evolution III, the event should stop behaving like a helpful random spawn. Ordinary clean units no longer appear by default. Countries receive crisis pressure and must choose whether to request formations, organize existing units, discipline generals, or close the process.

This change makes the event a command crisis. The divisions are no longer only weak or strong. Their internal composition becomes unpredictable, and some officers behave as if the army has already promised them power.

## Random battalion logic

Each requested Evolution III formation should be built through a random template generator.

The generator should choose:

- total battalion count
- line battalion mix
- support company count
- support company mix
- equipment fill band
- starting training band
- oddity tag that affects name, tooltip, and later follow-up risk

The oddity tag is not final localisation. It is a design marker.

| Oddity tag | Meaning | Gameplay effect direction |
| --- | --- | --- |
| paper_regiment | Looks formal but lacks equipment | low fill, lower absurdity |
| village_host | Local population gathered into one formation | low training, lower revolt risk |
| depot_beast | Heavy equipment and poor logistics | high supply strain, chance of armor |
| impossible_company | The battalion mix violates military sense | high absurdity, unstable performance |
| commander_favorite | Linked to a general demand chain | higher strength, higher officer appetite |
| hollow_register | Unit records do not match the soldiers present | chance of ghost or later chaos hook if Evolution IV active |
| medical_exception | Unit contains strange support and weak line troops | support-heavy, low combat, lower deaths risk |
| parade_monster | Strong but politically visible | public alarm, higher stability pressure |

This system should not require the implementation agent to hand-author hundreds of templates. It should use a controlled pool of generated templates with registry-style routing, or meta effects if supported. If engine limits force a fixed template pool, the pool must still be broad enough to produce the classes above and the simplification must be reported.

## Possessed general pool

Evolution III introduces scary generic generals that look possessed. The asset package should generate twenty fictional portraits. They are not real historical people. They should be visually distinct enough that repeated events do not feel like one face.

Portrait and character requirements:

- twenty generated commander portraits
- 156x210 final DDS unless the existing commander portrait pattern needs another size
- apparent gender presentation recorded in the manifest
- matching name pools for any one-person characters
- no opposite-gender name assignment
- no real leader likenesses
- no generated readable text
- period military or emergency clothing
- eyes, posture, and expression can look unsettling, but not meme-like
- at least four silhouettes should read as staff officers, four as frontline commanders, four as militia leaders, four as logistics or depot officers, and four as strange high-chaos officers

The implementation can create a commander character when a country receives a demand seed. If a character cannot be created safely for every country, use a finite rotating pool and report the limitation.

## General demand chain

A possessed general demand chain should be country-specific and value-driven.

| Demand class | Trigger factors | Demand direction | Accept outcome | Refuse outcome |
| --- | --- | --- | --- | --- |
| More formations | high backlog, recent victory by spawned units | general wants more units raised | on-demand cooldown reduced, appetite rises | appetite rises, illegal regiment chance |
| Regional command | units concentrated in a region | general wants control over a state group | better defense there, local autonomy risk | mission to hold drill fields |
| Depot control | supply strain and depot disorder | general wants rail and equipment authority | lowers short-term supply strain, raises future revolt strength | depot sabotage or command confusion |
| Political seat | high appetite, low stability | general wants formal power | stability short-term, route lock risk | public crisis and mutiny risk |
| Chaos authorization | Evolution IV active and leakage high | general wants strange units | immediate chaos units, high leakage | chance of chaos splinter seed |

The player should not see hidden future branches in the text. Tooltips should describe visible consequences and risks, such as command autonomy, supply burden, and possible mutiny.

## Officer appetite thresholds

Officer appetite should be a country value that moves through decisions, victories, failed missions, and general events.

| Band | Meaning | Content unlocked |
| --- | --- | --- |
| Quiet | Generals are present but manageable | ordinary demands rare |
| Assertive | A general asks for resources or command | demand events and small missions |
| Entrenched | The general has loyal units and local staff | regional command missions and refusal risks |
| Mutinous | The general can rebel with linked units | revolt countdown and containment choices |
| Breakaway | The general forms a country or armed revolt | war, tag release, or civil conflict |

The value should not rise from one decision alone. It should be the result of repeated concessions, reckless spawns, failures, or victories by units tied to the general.

## Revolt construction

A revolt should use actual units and territory when possible. The rebel should not be an empty tag.

Possible revolt forms:

| Revolt form | Conditions | Outcome |
| --- | --- | --- |
| Unit-only mutiny | parent is small, no safe state split | several spawned divisions switch sides or create hostile units in place |
| Regional barracks revolt | general has target region and enough units | one or more states transfer or become rebel-controlled with matching units |
| Depot breakaway | depot disorder high and a rail state is selected | rebel gains supply-heavy state and equipment-poor army |
| Capital challenge | appetite extreme and parent unstable | civil war style split centered near capital or highest-value controlled state |
| Chaos mutiny | Evolution IV active, leakage high | revolt uses chaos unit profile and may become a special splinter |

The revolt should be dangerous but scaled. A tiny country should not face an unbeatable major-sized army. A major at war can face a large serious mutiny, especially if it exploited the event.

## Human breakaway country package

Working country package label: Barracks State. This is not final map localisation.

A human mutiny that becomes a country should use a tag from a small event-owned tag pool. Final tags must be conflict-checked. The public country name should be short and map-readable, such as a regional military state or barracks republic direction. Do not use internal agency names as the public country name.

Starting package direction:

- states are selected from the revolt region, depot region, or a compact fallback around the highest risk state
- starting units include the revolting spawned units plus several dynamically scaled militia or guard formations
- equipment is limited by captured depots and parent stockpile context
- starting ideas include contested command, stolen depots, and unstable ranks
- politics default to a military or authoritarian emergency identity unless parent ideology and route demand another direction
- leaders use the possessed general portrait and name pool
- focus tree should be a shared crisis tree with human route overlays
- AI attacks parent first, then nearby weak countries if it survives and appetite remains high

## Shared crisis focus tree for breakaways

A breakaway that is expected to fight for more than a short revolt should get a shared tree with route overlays by profile. This prevents empty tags while avoiding a full bespoke tree for every possible mutiny.

Architecture map:

| Branch | Role | Key unlocks |
| --- | --- | --- |
| Opening survival trunk | Secure command, depots, and a capital | early factories, supply, basic units, officer legitimacy |
| Human command route | Barracks State and rogue generals | military laws, officers, discipline, expansion against parent |
| Irregular integration route | absorb strange human divisions | template cleanup, manpower, local support decisions |
| Depot economy route | live from captured stores | rail repair, military factories, equipment decisions |
| Expansion route | attack parent and claim nearby depots | claims, war goals, postwar integration missions |
| High-chaos route | invite stranger units if Evolution IV active | chaos leakage, chaos unit decisions, bigger revolt risk |
| Submission or settlement route | rare player or AI path | negotiated puppet, autonomy, reintegration, or ceasefire |

The tree should be non-linear. It should not be a straight ladder of army bonuses. Focuses should unlock decisions, missions, units, advisors, claims, and identity changes.

## Revolt containment for the parent

The parent country should receive containment actions.

- negotiate limited autonomy
- arrest the general if command coherence is high
- surround drill fields with loyal divisions
- cut depot access with train and support equipment costs
- offer amnesty to linked units
- purge false ranks at stability and army XP cost
- accept a temporary puppet or subject settlement if the revolt is too strong

Containment should have failure states. A failed arrest can strengthen the revolt. A failed negotiation can raise officer appetite elsewhere. A heavy purge can lower stability and war support.

## AI behavior for generals

Ordinary AI should prefer organization and containment. Desperate AI at war can empower generals if it is losing fronts, lacks divisions, or faces a capital threat. High-chaos AI can take more dangerous choices. AI with low stability should avoid political seat concessions unless a collapse is imminent.

Breakaway AI should be aggressive toward the parent, but it should avoid suicidal long-distance wars. If the parent dies, the breakaway seeks nearby depots, weak neighbors, or settlement depending on its route.
