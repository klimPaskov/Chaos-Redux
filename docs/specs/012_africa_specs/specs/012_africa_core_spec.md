# Event 012 — Africa Core Specification

## Premise

A valid country whose capital is in Africa becomes the center of an impossible continental project. The public-facing fantasy is simple and terrifying: **Africa is one**. The selected country does not begin as a normal conquest AI with a list of war goals. It begins as a host for a continent-wide proclamation, a congress of anti-colonial committees, regional councils, veterans, dockworkers, teachers, chiefs, urban organizers, religious networks, soldiers, merchants, and diaspora emissaries. The world hears that Africa will no longer be divided by outside desks.

The event is a Minor Fire-Once anomaly in the Formables cluster, but it should be built like a large country-event package. It should create a playable unifier with a bespoke focus tree, deep decision systems, new subject and protectorate behavior, regional liberation wars, a living congress mechanic, a diaspora return mechanic, possible RSA civil-war variant, high-chaos mythic branches, post-unification continental sponsorship, and a terminal world-end route if all continent unifier projects converge.

The selected country receives a continental identity package immediately: a cosmetic tag, continental core rights on African states, event flags showing it is the African unifier, focus-tree access, AI strategy, event log actor mapping, and the first congress decisions. The raw fantasy says the country gains cores on every African state. The gameplay version should satisfy that fantasy while preventing one-click snowballing: the unifier gains continental core rights and legal core status, but actual administration, resistance suppression, manpower extraction, and subject integration are governed by the **Continental Congress** mechanics. If the implementation grants literal HOI4 cores immediately, the tree must also apply balancing spirits for administrative overload, congress legitimacy, and foreign backlash until the relevant regions are integrated.

## Valid host selection

The target is a random valid country whose capital state is in Africa. The implementation should build a reusable valid-host trigger because the event list must show `N/A` when no valid actor exists.

A valid host should normally:

- exist and not be a nonhuman/special terminal chaos country;
- have its capital in a state assigned to the Africa state group;
- not already be the African unifier or a completed later union;
- not be a capitulated country with no meaningful controlled territory unless the event is manually forced;
- not be a subject that cannot act unless the event explicitly has a subject-host route;
- have enough map presence to receive a focus tree and decisions;
- be able to own or control at least one state safely after event setup.

The host can be a major or minor country. Ethiopia, Liberia, Egypt, South Africa, colonial puppets, or modded African tags can all create interesting starts. The random picker should not hardcode a short list. The starting package should scale by host strength, chaos tier, war status, and nearby colonial pressure.

## Immediate public event

The first player-facing event should not read as a dry map update. It should open with the actor: a government, congress, general staff, council, or court announcing that Africa cannot survive in fragments. Foreign papers disagree on whether the proclamation is a revolt, a miracle, a coup, a delusion, or the first coherent answer to the colonial order. African neighbors receive messages of protection before ultimatums. Colonial capitals receive diplomatic notes that sound too organized to dismiss.

Option tone:

- For the selected country: grim, declarative, visionary. The option should carry a memorable reaction line but not use unsourced quotations.
- For outsiders: anxious, cynical, often hypocritical. The option can use bureaucratic irony about conferences, borders, and “order.”
- For high chaos: rumors, omens, and impossible coordination can leak into the option tone.

The event details window and spreadsheet details should describe the premise and situation, not list modifiers or rewards.

## Cosmetic identity ladder

The host should change cosmetic tag at baseline, then update dynamically as control and route identity change.

Working cosmetic identities, not final localisation:

| State | Working identity | Used when |
| --- | --- | --- |
| Baseline proclamation | Provisional African Congress | Event fires; host has not consolidated a region. |
| Early military route | African Liberation Command | Militarized route or large war against colonizers. |
| Federal route | African Continental Federation | Federal Congress route has high cohesion and member autonomy. |
| Socialist route | African Peoples' Union | Syndicalist/socialist route dominates the congress. |
| Royal/council route | Council of African Crowns | Heirs of Kings route wins the legitimacy struggle. |
| High-chaos mythic route | Mandated Africa | Mythic Mandate branch is public and accepted. |
| Continent secured | Africa Is One | All required African state groups secured or integrated. |
| Africa + Middle East | African-Middle Eastern Union | Africa and Middle East unifiers merge without wider Asia. |
| Africa + Asia | Afro-Asian Union | Africa and Asia merge, including Middle East if it is already part of Asia's union. |
| Africa + Europe | Afro-Eurasian Union | Africa, Europe, and Asia/Middle East are merged. |
| Africa + Americas | Afro-Atlantic Union | Africa merges with one or both American continental unifiers. |
| All continents | World Congress / The World Is One | Terminal path; final name research and localisation gated. |

The implementation can use cosmetic tags, dynamic scripted localisation, or tag switch only when safe. Names should vary by route and controlled continent set. Flag changes must be asset-backed; do not swap to missing flags.

## Continental core and state model

The event needs a comprehensive **African state group** definition. The implementation should include the African mainland, islands relevant in HOI4 state data, and colonial enclave states that should count for the formation. It should define sub-groups for missions and tooltips:

- North Africa and Maghreb;
- Nile Corridor;
- Horn of Africa;
- West Africa and Gulf of Guinea;
- Sahel and Sahara routes;
- Congo Basin and Central Africa;
- Great Lakes and East Africa;
- Southern Africa;
- Indian Ocean Africa and Madagascar;
- Atlantic islands / colonial naval stations if represented.

The unifier's legal claim is continent-wide, but state integration should occur through tiered statuses:

1. **Declared African Core** — the proclamation says this state belongs to Africa; used for war goals, event details, and high-level fantasy.
2. **Liberated Administration** — state is controlled by the unifier, a subject congress, or a friendly league member; resistance is still possible.
3. **Chartered Region** — local administration has signed a charter; unlocks lower resistance, supply projects, and local recruitment.
4. **Integrated Region** — full economic and manpower integration; literal core benefits are stable and long-term.
5. **Mandated Region** — high-chaos supernatural route has fused local administration with mythic/nature mandates; powerful but diplomatically destabilizing.

If the literal HOI4 implementation cannot separate legal core from usable integration, use national spirits and dynamic modifiers to simulate administrative overload until regions pass integration missions.

## Core mechanics

### Continental Legitimacy

Represents whether Africans, diaspora networks, and foreign observers believe the proclamation is more than a military grab.

Rises from:

- liberating colonial-held African states;
- defending African countries at war with colonizers;
- protecting member autonomy in the Federal route;
- successful regional charters;
- diaspora-return success;
- defeating foreign punitive expeditions;
- honoring postwar settlement choices.

Falls from:

- attacking independent African countries without prior congress breakdown;
- annexing strong members too quickly;
- failed integration missions;
- heavy-handed occupation;
- puppet abuse;
- losing the capital or continental congress seat;
- high-chaos disaster powers used recklessly.

Legitimacy thresholds unlock better faction invitations, peaceful integration, stronger volunteers, and final unification recognition. Low legitimacy causes member resistance, foreign propaganda, and possible breakaways.

### Congress Cohesion

Represents member trust inside the African faction. It is distinct from legitimacy. A country can be legitimate to outsiders but still have a fractured congress.

Rises from shared wars, relief convoys, member defense, balanced influence, congress votes, and fair regional charters. Falls from unilateral wars, forced annexations, broken promises, member capitals lost, exploitative resource projects, and route shocks.

Cohesion should be visible in the decision category or scripted GUI. It should govern:

- member willingness to join wars;
- shared reserve decisions;
- integration success chance;
- member resistance and exit risk;
- faction name and leader confidence;
- whether strong African countries accept puppet, federation, or annexation terms.

### Liberation Readiness

Measures whether the unifier can start wars and interventions without becoming a hollow paper state.

Components:

- army readiness;
- equipment stockpile;
- supply and rail access;
- command obedience;
- port and convoy security;
- intelligence on colonial garrisons;
- regional staging networks.

Readiness unlocks liberation operations, reduces war-preparation mission length, and controls AI willingness to attack colonial powers. Low readiness blocks expansion decisions with icon-first requirements such as equipment, trains, supply hubs, or divisions in staging states.

### Integration Authority

Measures administrative capacity to turn liberated states and subject congresses into one country. It is gained through industry, bureaucracy, census, rail, courts, education, radio, tax offices, and local governments.

Integration should not be a political power store. It should require:

- held capitals and regional hubs;
- supplied divisions or military police in named regions;
- trains and convoys;
- support equipment and infantry equipment;
- stability and local support;
- completed charters;
- low resistance or compliance thresholds;
- focus route compatibility.

### Colonial Backlash / Scramble Pressure

Represents outside powers deciding whether the project can be contained by diplomacy, sanctions, expeditionary war, proxy governments, or a revived scramble.

Rises from:

- rapid colonial losses;
- controlling strategic ports, Suez-adjacent states, Cape routes, or resource regions;
- diaspora return propaganda;
- high-chaos supernatural incidents;
- annexing colonial subjects;
- rejecting foreign conferences.

Falls from:

- negotiated evacuations;
- recognition deals;
- slow regional integration;
- foreign guarantees traded for neutrality;
- defeating punitive expeditions decisively.

When Africa is fully secured, this pressure should trigger the **Scramble for Africa** reaction: outside colonizing powers attempt a diplomatic crisis, sanctions, guarantees of remaining enclaves, or coordinated war pressure. This should be a serious moment, possibly a super-event if the campaign state justifies it.

### Diaspora Return

Represents return migration, volunteer travel, shipping lines, cultural networks, and technical cadres from the African diaspora.

It should be staged:

1. **Letters and Newspapers** — small legitimacy and event flavour.
2. **Black Star Shipping Offices** — convoy/port decisions, small trickle of volunteers.
3. **Cadre Return** — engineers, teachers, medical workers, officers; unlocks advisors and industry decisions.
4. **Settlement Convoys** — manpower and skilled labor, but requires housing and stability.
5. **Diaspora Congress Seat** — diplomatic legitimacy, route-specific advisors, possible achievement.

Costs and requirements include convoys, ports, relations or foreign access, stability, consumer goods burden, civilian factories, and housing decisions. Failure creates overcrowded ports, foreign obstruction, or legitimacy loss.

### Mythic Charge

High-chaos only. This is not normal politics. It measures the strength of impossible omens, nature mandates, animal messengers, storms, river warnings, spider-web intelligence, thunder courts, and living forests. It must be optional, route-locked, and risky.

Uses:

- predict or redirect natural disasters;
- sabotage colonial infrastructure through impossible weather;
- empower elite units and elephant formations;
- unlock Great Forest nonhuman allies;
- create spectacular but dangerous report/news events;
- increase Scramble Pressure and World-End eligibility.

Guardrail: mythic content is fictionalized and must not portray real traditions as primitive or monstrous. Use respectful source notes and generated fictional assets.

## Baseline event flow

### Stage A — Proclamation

The selected host becomes the Provisional African Congress. It receives the continental legal claim/core package, opening focus tree, starting spirits, and Congress mechanics. Neighboring African countries receive a hidden relationship context: potential member, wary member, rival, colonial subject, colonized territory, or strong independent actor.

Initial spirits:

| Spirit | Role | Lifecycle |
| --- | --- | --- |
| Continental Mandate | Positive/unstable identity spirit giving legitimacy and war justification. | Upgrades into route-specific final identity. |
| Improvised Congress | Mixed spirit: political momentum but administrative overload. | Mitigated by early congress focuses and Integration Authority. |
| Liberation Without Roads | Negative logistics/industry spirit. | Reduced by rail, port, and supply focuses. |
| Diaspora Listening | Small positive legitimacy spirit with potential. | Becomes Black Star networks or fades if neglected. |
| Foreign Papers Laugh | Temporary diplomatic penalty and propaganda pressure. | Replaced by Foreign Papers Fear after first major victory. |

### Stage B — First Ring

The unifier consolidates nearby African states by diplomacy, protectorate invitations, or limited border operations. The first ring should favor rescuing African countries from colonial wars and building a faction, not instant wars on native states.

Actions:

- invite nearby African countries to a liberation compact;
- guarantee African countries fighting colonial powers;
- prepare first colonial ultimatum;
- release one or more provisional regional authorities in controlled colonial territory;
- begin Black Star correspondence;
- open the Congress Board UI.

### Stage C — League War

Once ready, the unifier can fight colonial holders. It should target colonizers and colonial subjects first. Independent African countries become future integration targets only after the congress has enough legitimacy and the member has had choices.

War flow:

1. Select colonial region target.
2. Run staging mission: hold ports/rails, place divisions, spend equipment/convoys/trains.
3. Issue ultimatum or support local uprising.
4. If refused, gain war goal or trigger colonial incident.
5. On victory, choose between regional subject, direct military administration, federal charter, or delayed integration.

### Stage D — Congress Pressure

Faction members accumulate influence relationships with the unifier. Friendly weak members can request protection or integration. Stronger members can demand autonomy. The unifier may pressure members into puppet status, then annexation, but this should be a process with clear costs and failure states.

Integration paths:

- **Federal integration**: slow, high legitimacy, member keeps local institutions; fewer revolts.
- **Command integration**: fast, military readiness gain, high resistance and breakaway risk.
- **Syndicate integration**: worker councils, strong factories, ideology struggle.
- **Crowned/council integration**: elder/royal compromise, stability and compliance, slower socialist/democratic reforms.
- **Mythic integration**: high-chaos, powerful, destabilizes outside diplomacy.

A strong member that resists can leave the faction and declare war on the unifier. The player should see warning meters before this happens.

### Stage E — Africa Is One

When all required Africa state groups are controlled, subject-chartered, or integrated, the unifier can fire the continent-secured event and change to the final Africa identity. This should unlock:

- final cosmetic tag;
- post-unification focus branch;
- Scramble for Africa reaction;
- continental economy/manpower consolidation;
- global anti-colonial diplomacy;
- sponsorship of other continent unifiers;
- possible super-event role label: `africa_is_one_super_event`, final title/quote/audio research required.

## RSA special branch

If South Africa is selected and is in the Allies, the event should not simply convert RSA into the continental unifier. It should start a civil war.

### Branch trigger

Conditions:

- selected host is RSA;
- RSA is in the Allies faction;
- no existing terminal world-end state blocks civil war;
- RSA is not already in a civil war unless manual force mode explicitly handles it.

### Civil-war sides

- **Dominion Government / Allied loyalists**: controls the established state, naval facilities, parts of the army, and Allied access.
- **African Congress Rising**: controls event-scaled territory and starts with militias, labor formations, anti-colonial volunteers, mine and rail networks, and diaspora sympathy.
- Optional third pressure, not always a full tag: **Neutralist Republican Bloc** around Hertzogite neutrality, Afrikaner republicanism, and anti-war politics. This should create decisions, sabotage risks, or leader events, not necessarily a third civil-war country unless the implementation can support it cleanly.

### Civil-war mechanics

The African Congress side receives a compressed version of the Africa package: legitimacy starts lower internationally but higher among anti-colonial networks; liberation readiness is improvised; Allied intervention risk is high.

The Dominion side receives Allied material support, naval security, and legitimacy with existing Allied powers, but domestic cohesion problems.

Winning as African Congress:

- fires a victory event;
- switches to the Provisional African Congress identity;
- makes peace with the Allies through an evacuation/recognition treaty if the Allies were only in the war through the civil-war branch;
- unlocks the normal Africa focus tree, but with South African-specific opening focuses about mines, ports, racial law dismantling, and Allied peace.

Winning as Dominion:

- suppresses the Africa event for RSA;
- applies a lingering anti-colonial underground modifier;
- can still face later Pan-African pressure from another host if the event is manually or alternate-path fired before normal fire-once removal, but automatic fire-once should be consumed unless design chooses otherwise.

## Evolution structure

Event 012 has four main evolutions plus the terminal world-end gate. These are true evolutions, not normal baseline phases. Each evolution must support active-event evolution and pre-fire evolved opening.

### Evolution I — First Continental Ring

Trigger direction: Gathering Storm or enough early victories / several African states in the congress. The selected unifier begins consolidating nearby states and receives clearer flavor around proclaiming itself a new African power.

Active-event changes:

- unlocks early news events for neighboring and colonial powers;
- adds regional first-ring missions;
- opens faction invitation and rescue tools;
- strengthens initial focus branch.

Pre-fire evolved opening:

- first firing begins with extra nearby influence, one active regional charter mission, and stronger opening news.

### Evolution II — Union-in-Arms

Trigger direction: Rising Chaos or control over a large share of Africa. The state gains stronger tools to push continental unification.

Active-event changes:

- unlocks temporary military/economic buffs tied to Liberation Readiness;
- unlocks elephant unit branch and other strange formations;
- expands cores/claims cleanup and integration authority;
- cosmetic name and leader/title flavor become more dramatic once a large part of Africa is controlled.

Pre-fire evolved opening:

- first firing can start with a stronger unifier, a wider faction invitation radius, and one regional subject already forming in nearby colonial territory if valid.

### Evolution III — Continental Sponsor

Trigger direction: Chaos Tier / high control / Scramble Pressure. Africa becomes a larger global-chaos actor, not only an African regional event.

Active-event changes:

- unlocks broader anti-colonial war goals;
- opens global support decisions for Middle East, Asia, Europe, South America, and other continent unifier movements;
- adds foreign-reaction events;
- begins world-threat interaction if other continent unifiers exist.

Pre-fire evolved opening:

- first firing begins with wider global reaction, foreign volunteers, and colonial powers on higher alert.

### Evolution IV — Africa Is One

Trigger direction: Totalen Chaos / Africa secured / Scramble for Africa fired or imminent. Africa becomes a major world-chaos pole.

Active-event changes:

- unlocks final continent identity;
- triggers Scramble for Africa response;
- enables dynamic annexation/merger with successful continent unifiers;
- opens the world-unity ambition if all other conditions are met.

Pre-fire evolved opening:

- a late first firing begins as a shock: the host receives multiple regional congresses, stronger starting forces, faster integration, and immediate Scramble Pressure.

## World-end scenario — The World Is One

This is terminal and must not be treated as a normal escalation. It can only become available if:

- Africa is fully unified;
- the world is already in extreme chaos / World Collapse conditions;
- the **Africa Is One** super-event/state has fired;
- all other continental unifiers exist;
- each other continental unifier has pursued its post-unification path;
- each other continental unifier has unlocked or accepted its world-end path;
- no incompatible terminal scenario has already started.

The world-end route should not simply annex every country instantly. It should be a final sequence: continental unifiers either submit to a global congress, merge through dynamic union names, or resist and trigger the final wars. Once the terminal scenario is chosen, normal random events should be frozen or gated by the world-end rules.

Super-event role label: `the_world_is_one_world_end_super_event`. Final title, quote, button text, image, and audio require super-event research.

## Event cluster role

Event 012 belongs to the Formables cluster. The cluster is currently new and has only this event. In cluster display, the event should be described as a severe formable anomaly: a state tries to turn a whole continent into one political body and can later merge with other continent formables.

If the cluster later gains other formables, Africa should be a required or high-severity member only when selected directly. It should not casually fire as an optional side effect of a smaller formable without explicit cluster design.

## Connections with other Chaos Redux systems

- **Chaos Meter**: High chaos increases evolution intensity, Mythic Charge, Scramble Pressure, and chance of extreme integration outcomes.
- **Event Logs**: The unifier should be the actor in event history and evolutions. Detail views need a clean explanation of baseline and evolution tracks.
- **Event Details**: Describe the fantasy and progression without listing modifiers.
- **Super-events**: Africa Is One, Scramble for Africa, RSA victory, and The World Is One are possible roles; final presentation must be researched.
- **World Threat**: If Africa becomes a global pole and other continent unifiers are active, consider integrating with the world-threat framework as a source of global cooperation/hostility.
- **Natural Disasters**: High-chaos mythic powers can predict or redirect natural disasters, but should not use them as a free win button.
- **Deaths / Condemnation / Air Cleanliness**: Ordinary liberation wars should not automatically touch these systems except through existing warfare. Mythic disaster decisions can touch deaths/air cleanliness only when implemented as actual disasters with consequences.

## Design guardrails

- The event should not portray Africa as empty, simple, or culturally uniform.
- The unifier should initially prefer liberating African countries from colonizers and forming a faction, not instantly declaring on native African countries.
- Subject/provisional regional governments should appear often enough that the map feels like a living liberation coalition, not one blob.
- Strong African states should have agency: they can join, negotiate autonomy, resist integration, leave, or fight.
- High-chaos great ape or supernatural countries must be nonhuman fantasy chaos actors, never coded as African human peoples.
- Real leaders and real symbols require sourcing. Fictional leaders use generated portraits with route-appropriate name pools, institutional names, or the source-language court-name joke pool where Event 012 recasts the public display.
## Authority Atlas update

The updated package adds an Authority Atlas layer. The Atlas is a living catalogue of niche regional offices, restoration subjects, specialist schools, historical memory routes, and high-chaos impossible actors. It sits below broad regional authorities and above individual state integration.

Core rule: broad regional authorities keep the map manageable; the Authority Atlas gives those regions distinct identity. The unifier should never receive all atlas content instantly. It reveals through surveys, focus routes, local mandate, state control, and chaos-tier escalation.

At minimum, implementation should support:

- historical offices/restoration subjects for at least twelve researched anchors;
- specialist schools for cavalry, guards, desert, highland, river, port, and elephant/forest support routes;
- high-chaos impossible branches for at least five actors or monument chains;
- nonhuman/sanctuary actors that cannot be annexed, conscripted, or treated as normal human countries.

## V2 expansion: regional memory and absurd escalation

The event should now include a large candidate pool of historically anchored **niche seats** inside the regional authority system. These seats let the unifier invite, protect, empower, integrate, or alienate local authorities based on older political memories, trade networks, cities, courts, ports, rivers, mountains, forests, deserts, and island systems.

Implementation should read `specs/012_africa_niche_polities_and_absurd_paths.md` as source design. The key addition is a **Regional Memory and Living Seats** layer:

- Broad regional authorities remain the normal first layer.
- Niche seats appear from regional control, focus routes, high legitimacy, local crises, or high chaos.
- Most niche seats should be sub-authorities or limited subjects rather than permanent map spam.
- Seat selection must be capped and AI-controlled so the decision category stays readable.
- Each active niche seat changes decisions, local forces, integration costs, regional trust, and potential resistance.
- Historical seats are not magic by default. Their absurd paths unlock only through Evolutions II–IV and Green Covenant/high-chaos gates.
- Nonhuman/supernatural actors are explicitly nonhuman/supernatural and must use special classification and safe localisation.

This expansion makes Africa feel like many places being pulled into one impossible project. “Africa is one” remains the public fantasy; the mechanics prove unity by making local seats argue, help, resist, bargain, and sometimes become terrifyingly strange.
