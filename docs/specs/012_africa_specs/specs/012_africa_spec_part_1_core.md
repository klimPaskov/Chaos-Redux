# Event 012 — Africa: Core Event Specification

## Event promise

Event 012 is a minor fire-once Formables event whose public fantasy is simple: **Africa is one**. A random valid country whose capital is in Africa becomes the centre of a continental unification attempt. The old one-line implementation concept gave that country all African cores, a cosmetic tag, and a continent-wide war. The rework keeps those required baseline beats, but turns the result into a playable continental system instead of an instant annexation snowball.

The event should feel like an impossible acceleration of Pan-African politics, anti-colonial war, regional congresses, liberation committees, military consolidation, and high-chaos myth. It should not read as a map repaint. The player should see a country, movement, congress, army, faction, and later a strange world-order actor forming under pressure.

The first public report is not “borders changed.” It is that a capital in Africa has started speaking in the name of the whole continent, and people across ports, rail yards, churches, mosques, shrines, mines, plantations, garrisons, universities, villages, trade unions, exiles, and colonial offices are reacting before anyone agrees what this means.

## Baseline non-negotiables carried from the catalog row

- Event ID: `12`.
- Entry event: `chaosx.nr12.1`.
- Type: Minor Fire-Once.
- Cluster: Formables / Various Anomalies.
- Chaos tier baseline: 4 in the catalog, but the baseline event can fire through normal fire-once selection when its target is valid; later evolutions use chaos state for intensity and weirdness.
- Select one random valid country whose capital state is in Africa.
- That country wants to unite Africa.
- The selected country receives the Africa event package: cosmetic identity, focus tree, decisions, continental preparation, staged integration, native/regional subject authorities, African-state cores, resource and industry routes, diaspora return route, portraits, frames, and major high-chaos extensions.
- The selected country’s cosmetic tag changes immediately after proclamation.
- The selected country receives cores on every African state as the catalog baseline requires. The gameplay design treats these as **paper cores** until integration work catches up, using state modifiers, spirits, integration meters, resistance, autonomy, compliance, and regional authority mechanics to prevent instant full benefit.
- If RSA is chosen and RSA is in the Allies faction, the event starts the RSA civil-war version instead of simply turning RSA into the African conqueror.
- If the RSA civil-war version is won by the African unifier side, the Allies must make peace with Africa.
- The unifier does not immediately try to conquer all native African countries. It first tries to create and lead a Pan-African faction against colonial holders, then gradually pressures, puppets, federates, or annexes African members through influence and integration mechanics. Strong African countries can resist, leave the faction, and declare war.

## Design guardrails

This event uses African history and myth as inspiration for alternate-history gameplay. It must not turn African cultures into caricatures. The high-chaos nonhuman and supernatural content must be clearly fictional, clearly separate from human African peoples, and registered as nonhuman or supernatural Chaos Redux actors where implemented.

Leader and court display names for Event 012-created or Event 012-recast identities can use the untranslated source-language joke pool listed in `specs/012_africa_country_packages_and_subjects.md`. Country, polity, institution, title, source, and historical notes remain serious and researched; the joke is a visible ruler/court mask, not an ethnonym or historical claim.

References to gorilla or chimpanzee polities must never imply human African countries are apes. If used at all, they are high-chaos, explicitly nonhuman rainforest guardian actors with their own classification, no human party politics, no ethnic substitution, and a clear ecological/supernatural framing.

## Target selection

### Valid target trigger

A country can be selected if all of these are true:

- It exists.
- Its capital state is on the African continent according to the game’s state/continent data.
- It is not an actual nonhuman country and is not a special chaos country that should be excluded from normal national politics.
- It controls or owns at least one state in Africa.
- It is not already the Africa unifier, an African continent formable, or a post-world-end tag.
- It is not a purely temporary release shell with no government unless the implementation deliberately treats it as a provisional congress host.
- It is not a subject unless the subject branch is allowed by high chaos or by a target-specific rule. A subject may still qualify if it is an African country at war against or being exploited by a colonial master, because this creates a strong liberation story.

If no valid target exists, Event 012 must show `N/A` in the event list and must not be rolled or manually fired except through an explicit triggerable scenario that creates a valid host.

### Target weighting

The selection should prefer a target that can carry the fantasy without breaking the map:

| Weight group | Examples | Reason |
| --- | --- | --- |
| Independent African capitals | Ethiopia, Liberia, South Africa when eligible, independent modded African states | They can plausibly proclaim a continental claim without first needing release logic. |
| African subject or colonial-administration capitals | African puppets, dominions, semi-autonomous protectorates | Strong liberation fantasy; should start with patron pressure and legitimacy problems. |
| African countries currently at war with a colonial holder | Any valid African country fighting a non-African occupier | The unifier can emerge as a rescue actor, not only a conqueror. |
| Recently released African states from other Chaos Redux events | Independence Wave tags, collapse tags, liberation tags | Event interaction and replay variety. |
| RSA while in Allies | South Africa in Allied faction | Triggers the civil-war variant. |

The implementation should avoid selecting a non-African colonial overlord with a capital outside Africa. If a European empire controls half the continent but its capital is in Europe, it is not the unifier.

## Immediate event flow

### `chaosx.nr12.1` — The Continental Claim

The entry event should be a report-style popup to the selected country and a news or diplomatic event to major observers. The selected country receives the first decision category and focus-tree package immediately. The public tone is frantic and uncertain: diplomats cannot tell whether this is a constitutional congress, a revolutionary proclamation, a royal restoration, a liberation command, or a mass hallucination of continental politics.

Player-facing option tone:

- For the selected country: grand, dangerous, and self-aware. The option should sound like an oath rather than “OK.”
- For African neighbours: wary. They see help against colonial powers but fear absorption.
- For colonial holders: alarm, denial, or contempt.
- For high-chaos observers: rumours mention drums, old roads, red dust, impossible animal movements, sudden port strikes, and maps refusing to stay folded.

The event immediate block should:

1. Save the selected country as the Africa unifier event target.
2. Set a country flag such as `africa_unifier_active`.
3. Set a global flag such as `event_012_africa_fired`.
4. Change the selected country to the baseline Africa cosmetic tag.
5. Add African cores as required, but also add the unintegrated-core burden package.
6. Load or activate the Africa focus package.
7. Unlock the Continental Congress decision category.
8. Create the initial Pan-African Charter faction path, but do not forcibly invite every African country on day one.
9. Prepare event log actor mapping to show the selected unifier in Event Details and history.
10. If RSA is selected and RSA is in Allies, branch into the RSA civil-war setup before the ordinary unifier package completes.

### Cosmetic tag baseline

The selected country changes to a cosmetic tag that uses dynamic localisation based on route and progress.

Early baseline names:

- `African Congress` for democratic/federal opening.
- `Pan-African Liberation Authority` for revolutionary opening.
- `Continental Defence Congress` for military emergency opening.
- `African Crown Congress` for monarchy/traditional authority opening.
- `The Green Covenant of Africa` for high-chaos nature/supernatural opening after later evolution.

The baseline cosmetic tag should be visually distinct but not yet absurd. Higher chaos changes the name, flag, leader title, portraits, and frames into stronger fantasy forms.

### Paper cores

The baseline must satisfy the catalog instruction that the unifier gains cores on every state in Africa. To keep the campaign playable, those cores are not treated as fully integrated in the design.

Implementation expectation:

- Grant cores on all African states through the required core effect.
- Add a national spirit, state modifiers, or scripted state flags that mark uncontrolled/unintegrated African states as `paper_core` or equivalent.
- Paper cores should not give full benefit until the region is integrated through congress decisions, focus rewards, local authority work, or military occupation settlement.
- Paper-core penalties should scale with how much of Africa is nominally claimed but not governed.
- Conquered African land should pass through states: Claimed in Congress → Protected or Occupied → Regional Authority → Integrated Member → Full Continental Administration.

Paper core gameplay is important because it lets the event keep the direct fantasy while still requiring decisions, missions, faction politics, and regional integration.

## The first year of play

The first year should not be a simple war declaration spree. The intended flow is:

1. **Proclamation shock.** The unifier becomes publicly recognizable and gains its first continental claims, cores, and burden.
2. **Charter offers.** Nearby African states and African states at war with colonial powers receive offers for protection, aid, faction membership, or observer status.
3. **Colonial alarm.** Non-African holders of African states gain alarm and can issue protests, sanctions, counter-propaganda, reinforcements, naval patrols, or emergency conferences.
4. **Regional congresses.** The player chooses where to concentrate: West Africa, Maghreb/Sahara, Nile-Horn, Congo Basin, Great Lakes, East Africa, Zambezi/Southern Africa, Indian Ocean islands.
5. **Aid before absorption.** If an African country is fighting a colonizer, the unifier can help with volunteers, equipment, advisors, convoys, and faction invitation. This is cheaper and more legitimate than immediate annexation.
6. **Influence and integration.** Faction members gain influence scores, obligations, and regional-trust variables. The unifier can pressure members toward protectorate, puppet, federation, or annexation. Stronger states resist if pressure is too aggressive.
7. **First colonial war.** The unifier usually fights a non-African colonial holder before it fights a fellow African state.
8. **First split.** A strong African member may reject integration and leave the faction, creating the first African-on-African conflict only after diplomacy and pressure have built up.

## RSA special branch

### Condition

The RSA civil war happens only if:

- RSA is the selected event target.
- RSA is in the Allies faction.

If RSA is selected but is not in Allies, RSA can still become the African unifier through the ordinary baseline route, though it should start with sharper legitimacy, apartheid, labour, and army-disloyalty problems.

### Civil-war premise

The proclamation does not simply transform the Union of South Africa into a continental unifier. Instead, the country fractures. The Allied-aligned Union government, settler political institutions, segments of the Union Defence Force, mining interests, and imperial networks oppose a rapidly forming African Congress authority backed by labour organizers, anti-apartheid movements, African soldiers, port workers, sympathetic officers, rural networks, and returning volunteers.

The branch should not trivialize South African racial politics or turn apartheid into a joke. It is a violent rupture over the future of the country and continent.

### Civil-war sides

| Side | Role | Gameplay identity |
| --- | --- | --- |
| African Congress Provisional Authority | The Event 012 unifier side. | Lower starting industry, high manpower potential, strong legitimacy growth, faction formation after victory, anti-colonial diplomacy. |
| Allied Union Government | Existing RSA or loyalist successor. | Better initial equipment, Allied diplomatic support, ports/navy access, colonial recognition, internal stability problems. |

The unifier side should receive a temporary civil-war focus branch before the full continental tree opens. Winning the civil war unlocks the ordinary Africa tree and sets the selected side as the Africa unifier.

### Allied peace rule

If the African Congress side wins the RSA civil war:

- The Allies make peace with Africa.
- Allied guarantees or faction-war side effects caused solely by the civil-war branch are cleared.
- The victorious Africa unifier can choose whether to seek recognition, demand reparations, expel Allied missions, or accept a transitional settlement.
- If global chaos is high, the Allies may retain colonial alarm and later join the Second Scramble crisis, but they must not remain in the civil-war war because the user explicitly requested peace after victory.

### Loss outcome

If the loyalist side wins:

- Event 012 is still considered fired.
- The loyalist government receives a temporary “Continental Claim Suppressed” spirit and anti-colonial unrest.
- African states and colonial holders get a news event explaining that the first continental attempt failed.
- The event should not immediately re-fire for another country, because it is fire-once. Later high-chaos systems may reference the failed attempt as a memory, but they do not replay the same event.

## African faction: Pan-African Charter League

The unifier’s first faction should be a League, Congress, Charter, Front, Covenant, or Defence Pact depending on route. It is not just a vanilla faction name. It has rules.

### Membership conditions

An African country can join if:

- Its capital is in Africa, or it controls/owns African states and is locally recognized as an African authority.
- It is at war with a non-African colonial holder, under direct colonial threat, recently liberated, or ideologically sympathetic.
- It is not an actual nonhuman country unless the high-chaos route explicitly allows a pact.
- It is not already a major power faction leader unless a special diplomatic focus unlocks negotiated dual leadership.

### Membership states

| State | Meaning | Typical effects |
| --- | --- | --- |
| Observer | Watches the congress, can receive small aid, not bound to war. | Low obligation, low influence growth. |
| Protected member | The unifier can intervene if it is attacked by a colonial holder. | Moderate cohesion gain, aid decisions, defensive calls. |
| Charter member | Full faction member with votes and obligations. | Shared wars, influence, integration pressure. |
| Regional authority | Semi-autonomous subject or puppet created by the unifier. | Can be integrated over time, provides local units and administration. |
| Integrated member | Has accepted federation or annexation terms. | Regional trust increases, paper-core burden decreases. |
| Resistant member | Refuses further pressure. | Can leave, trigger crisis, join rival patron, or declare war. |

### Faction values

The League uses visible values:

- **Continental Legitimacy** — why Africans accept the unifier’s claim.
- **Congress Authority** — ability to enforce policy and coordinate war.
- **Charter Cohesion** — faction willingness to remain under the unifier’s leadership.
- **Liberation Momentum** — success against colonial holders and external occupiers.
- **Regional Trust** — per-region acceptance of integration.
- **Colonial Alarm** — external reaction pressure that drives the Second Scramble.

These values should be visible in the decision category header and in a custom Continental Congress interface when implemented.

## Regional state groups

The implementation agent must map these to exact HOI4 state ids using existing continent and state data. The spec uses region names so the gameplay is clear without hardcoding state lists.

| Region | Main design role |
| --- | --- |
| Maghreb and Sahara | Desert logistics, old empires, ports, French/Italian/Spanish colonial interests, Arab-African identity tension. |
| West African Coast | Pan-African congress politics, ports, trade unions, gold/cocoa/resource routes, diaspora return entry point. |
| Sahel and Upper Niger | Caravan authority, cavalry/motorized columns, Mali/Songhai/Ghana historical echoes, drought and supply challenge. |
| Nile and Horn | Ethiopia/Aksum/Kush/Nile legitimacy, Red Sea ports, mountain warfare, Italian/British/French interests. |
| Great Lakes | Regional diplomacy, lakeside supply, monarchies/republics, manpower, internal federation questions. |
| Congo Basin | Rainforest logistics, rubber/minerals, river transport, high-chaos nonhuman/nature actors. |
| Swahili Coast and East Africa | Indian Ocean ports, rail corridors, coastal trade, askari veterans, anti-colonial campaigns. |
| Zambezi and Stone Cities | Great Zimbabwe/Mutapa references, copper/coal/resources, rail construction, southern front. |
| South African Industrial Belt | Mining, industry, RSA civil war, labour politics, southern ports. |
| Indian Ocean Islands | Madagascar, Comoros, Mauritius, Seychelles and naval/convoy routes. |

## Regional authorities and native African subject layer

The event should create many African regional authorities, not instantly annex everything. These are not placeholders; they are local administrations, federated governments, provisional councils, or restored regional institutions that help the cause before integration.

Suggested authority tags are placeholders and must be checked for conflicts:

| Working tag | Authority | Inspiration and role |
| --- | --- | --- |
| `WAC` | West African Congress Authority | Pan-African congress politics, unions, ports, gold/cocoa, Ghana-Mali-Songhai memory. |
| `SAH` | Sahel Caravan Authority | Sahel logistics, old caravan routes, cavalry/motorized columns, oasis defence. |
| `MAG` | Maghreb Coastal Congress | North African ports, Sahara supply, anti-colonial and Arab-African diplomacy. |
| `NAH` | Nile-Horn League | Nile, Kush, Aksum, Ethiopian/Horn legitimacy, Red Sea corridor. |
| `EAC` | East African Railway Congress | East African rail, askari veterans, Indian Ocean ports, anti-colonial campaigns. |
| `GLC` | Great Lakes Council | Lake logistics, regional kingdoms, manpower, internal diplomacy. |
| `CBC` | Congo Basin Charter | Congo river system, rainforest logistics, resource sovereignty, nature high-chaos entry. |
| `ZSC` | Zambezi-Stone Cities Authority | Great Zimbabwe/Mutapa/Maravi references, southern rail and resource route. |
| `SLC` | South African Liberation Congress | RSA civil-war branch, labour, mines, anti-apartheid politics. |
| `IOC` | Indian Ocean Congress | Madagascar and island routes, convoy security, naval access. |

Each authority should be releasable as a subject or faction member and later integrated. They can provide local units, advisors, construction missions, regional legitimacy, and route-specific events. They should not all use the same leader, flag, idea stack, or focus tree text.

## Early news and foreign awareness

Evolution I explicitly requests early news so other countries know why wars started. The baseline should already include a small news pulse:

- Major powers receive a news event when the unifier proclaims the Continental Claim.
- African countries receive a separate invitation/concern event.
- Colonial holders receive a colonial alarm event if they own or control African states.
- Countries with African diaspora hooks receive rumours about return missions and political agitation.

News text should not list mechanical effects. It should describe public confusion, sudden congresses, port strikes, desert messengers, railway guards, speeches, and colonial offices trying to decide whether to laugh or mobilise.

## Failure and containment states

The event needs failure states, not just growth.

| Failure state | Cause | Result |
| --- | --- | --- |
| Congress fracture | Charter Cohesion collapses. | Members leave; strong members can start a counter-faction or declare war. |
| Administrative overreach | Too many paper cores and too little integration. | Stability/consumer goods/supply penalties, regional unrest, slower integration. |
| Liberation exhaustion | Many failed colonial wars. | Legitimacy falls, colonial alarm rises, faction members become resistant. |
| Regional revolt | Pressure on a strong African member without trust. | Member leaves, gains foreign patron, may declare war. |
| Second Scramble defeat | Outside powers defeat the unifier after Africa is mostly unified. | African Union may splinter into regional authorities; event remains fired but post-defeat aftermath persists. |
| RSA loyalist victory | RSA branch civil war lost. | Unifier attempt fails; unrest remains as memory. |

## Success states

| Success state | Requirement | Result |
| --- | --- | --- |
| Charter League | Several African countries join or become protected. | Unifier becomes faction leader and can fight colonial holders with legitimacy. |
| Continental War Command | Major colonial holder defeated in Africa. | Liberation Momentum grows; more regional authority options open. |
| Africa Is One | All African states are controlled/integrated or held by loyal regional authorities. | `Africa is one` super-event role label fires after research/wiring; Second Scramble crisis unlocks. |
| Continental Pole | Africa survives the Second Scramble or wins a global anti-colonial showdown. | Africa can sponsor other continent unifiers. |
| The World Is One | All required continent unifiers exist, complete their post-unification routes, and world chaos is terminal. | World-end scenario path unlocks. |


