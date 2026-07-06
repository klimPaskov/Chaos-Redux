# 006 Independence Wave Spec Part 5: Formables, Super-Events, Assets, and Achievements

## Formable web and endgame outcomes

Event 6 formables should make new states feel ambitious without turning every release into a bespoke empire route. The formable web uses regional templates, route gates, and origin-aware checks so one shared system can support ordinary republics, old border claimants, restored polities, federations, port leagues, indigenous confederations, and high-chaos claimants.

## Formable design promise

A formable is not only a tag swap. It should be the reward for making a newly released country survive long enough to prove that it can govern a wider region.

Every Event 6 formable should require most of the following:

1. Event 6 origin or explicit Event 6 participation.
2. Control of required state groups.
3. Local Control in key states.
4. Legitimacy high enough to convince domestic actors.
5. Recognition or an alternate high-chaos justification.
6. Border Heat below a safe level, unless the route is openly coercive.
7. Integration missions in archives, capitals, ports, rail hubs, or border districts.
8. Former host survival checks before any transfer effect.
9. A route commitment through the focus overlay or decision category.
10. Post-formation cleanup and new aftermath play.

A small release should not receive a unique formable only because it exists. It should either use a regional template, participate in a league outcome, or remain a survivor state with local ambitions.

## Origin and tag rules

The same tag can appear through different event systems, but formable logic must read the release origin. A country that appears through Event 6 can use Event 6 formation checks. The same tag created by Soviet Collapse or another system should not silently inherit Event 6 formation content unless it also receives an explicit Event 6 participation flag.

New Event 6 country tags, formable tags, cosmetic tags, and route split tags must end with `X`. Existing vanilla and registered Chaos Redux tags can be reused only after a repository audit confirms that reuse is safe.

Candidate tag values in this spec are planning labels. Implementation must confirm tag length, availability, collision risk, country file paths, localisation keys, flags, cosmetic tags, and focus loading before reserving them.

## Formation lifecycle

| Phase | Player state | Required work | Failure risk |
| --- | --- | --- | --- |
| Rumour | The country sees regional ambition hints through focus or decision conditions | Survive the initial wave and stabilize core values | Hidden path stays unavailable |
| Dossier | A decision or focus reveals the possible formation | Spend administrative, diplomatic, and military resources | Host anger and rival claimants rise |
| Integration | The country controls target groups and runs local missions | Raise Local Control and lower instability in key states | Resistance, sponsor debt, and border heat |
| Assembly | A congress, court, council, or federal vote prepares proclamation | Meet legitimacy, recognition, route, and peace checks | Partial formation or disputed identity |
| Proclamation | The formable is created as a tag, cosmetic tag, or route identity | Apply flags, cores or claims, ideas, focus branches, and AI strategy | Host backlash and league fracture |
| Settlement | The new formation proves it can govern | Hold capitals, protect supply, avoid puppet capture, settle claims | Crisis missions, war, or collapse |

## State-control model

A formable should never require a vague list of places. The implementation should define named state groups and show them through custom tooltips or scripted localisation.

| Requirement type | Use |
| --- | --- |
| Heartland group | Must usually be owned or controlled. The group contains the formation capital, identity center, or strongest state. |
| Anchor group | At least some anchors must be controlled. Anchors are ports, old capitals, river cities, courts, sacred sites, rail hubs, or archive districts. |
| Border belt | Needed for expansionist routes and defensive federations. Border belts often use claims before cores. |
| Disputed group | Optional or high-chaos. Control gives stronger form but raises Border Heat and Host Anger. |
| League member group | Used for federal league outcomes. Requires member consent or leader authority, not simple conquest. |
| Host-retained group | Always excluded from transfer if it would delete the host or strip the host capital without fallback. |

The first implementation pass should give each formable a minimum group, a strong group, and an overreach group. Minimum formation creates a modest state. Strong formation creates a larger state with better ideas. Overreach formation creates high-chaos claims and backlash.

## Integration requirements

Formables should use integration as a cost, not only map possession.

| Integration track | Typical requirement | Mechanical link |
| --- | --- | --- |
| Capital integration | Hold the chosen capital or provisional capital for a timed mission | Raises Legitimacy and Local Control |
| Archive integration | Control administrative or historic archive states | Reveals claims, lowers formation cost, raises Host Anger if seized from host |
| Rail integration | Hold rail hubs and supply corridors | Lowers post-formation instability and unlocks unit movement missions |
| Port integration | Hold ports for maritime and island formations | Raises Foreign Support and sponsor access, risks Patron Influence |
| Court or assembly integration | Complete legitimacy or regional consent missions | Needed for restoration, federation, or indigenous confederation routes |
| Border commission integration | Settle disputed districts or win arbitration | Lowers Border Heat for peaceful formation |
| Coercive integration | Use ultimata, garrisons, or compact pressure | Speeds formation, lowers Recognition, raises Aggressive Bloc Pressure |

## Reveal conditions

Formable decisions should not flood every newly released country.

A formable can be revealed by:

- a regional insert focus reaching an ambition opener
- an ambition package at spawn
- control of heartland and at least one anchor group
- Legitimacy above 45 and Local Control above 50
- Recognition above 25 for legal and diplomatic routes
- Aggressive Bloc Pressure above 55 for coercive routes
- League Authority above 55 for federal league routes
- a high-chaos evolution that allows unusual claimants
- a successful dossier decision
- a rare event after a country survives a host war

A hidden formable should show only a broad direction until revealed. The player should not see exact high-chaos surprises in ordinary tooltips.

## Former host safeguards

Formable decisions must respect host survival.

| Risk | Required safeguard |
| --- | --- |
| Formation would annex all host states | Block the decision or shrink the transfer list. |
| Formation would take the host capital | Prefer to block. Allow only if the host already has another valid capital state and keeps at least one state. |
| Formation would take every host victory point | Block or convert some targets to claims. |
| Formation would annex a host through subject transfer | Block unless the host has already ceased to exist through non-Event 6 causes. |
| Formation would trap host armies without access | Add evacuation, access, or supply corridor cleanup. |
| Formation would give cores too early | Use claims, integration missions, or working local authority before cores. |
| Host has accepted a settlement | Peaceful formation must respect the settlement or reopen it through a clear route cost. |
| Host is protected by another event system | Event 6 must not override that system without explicit compatibility logic. |

A formable can be powerful, but it cannot use Event 6 as a deletion exploit against the former host.

## Regional formable families

### European republics and old border claimants

| Formable family | Candidate public identity | Candidate tag class | Normal route | High-chaos route |
| --- | --- | --- | --- | --- |
| River federation | Danubian Federation or Danubian Union | New X-ending tag if no existing safe tag | Arbitration, trade, rail integration | Border congress with coercive claims |
| Alpine compact state | Alpine Federation or Alpine Republics | New X-ending tag or cosmetic tag | Defensive neutrality and mountain forts | Fortified claimant state |
| Baltic federation | Baltic Confederation or Baltic Union | Existing tag only if safe, otherwise X-ending | Recognition and league charter | Hard border revision |
| Low Countries federation | Netherlands-Belgium style federation only if state setup supports it | Existing tag if safe | Legal congress and ports | Port blockade and sponsor-backed claims |
| Carpathian claimant union | Carpathian Federation | X-ending | Mountain defense and minority settlement | Claimant militias and host conflict |

European formables should use strong diplomatic requirements. They are usually not the strangest content in the event. Their depth comes from borders, legal claims, old parliaments, rail hubs, and host settlement pressure.

### Soviet-region overlap handled through Event 6 origin separation

| Formable family | Candidate public identity | Origin rule | Normal route | High-chaos route |
| --- | --- | --- | --- | --- |
| Volga restoration | Volga Bulgaria | Event 6 origin required for Event 6 content | River trade, Islamic legitimacy, treaty work | Wider Volga claimant route |
| Caucasus federation | Caucasus Federation | Event 6 origin or explicit participation | Mountain defense and arbitration | Militarized pass federation |
| Turkestan style union | Regional Central Asian union | Must not borrow Soviet Collapse route content | Recognition, rail corridors, local assemblies | Steppe congress with aggressive claims |
| North Caucasus restoration | Mountain Republic direction | Event 6 origin required | Defensive league and local control | Host-war route with high instability |

These routes must not become Soviet Collapse routes. If Event 5 releases a similar tag, Event 5 owns the content. If Event 6 releases it, Event 6 owns the mechanics, decisions, focus overlay, and formable path.

### Middle Eastern and Mesopotamian identities

| Formable family | Candidate public identity | Candidate tag class | Normal route | High-chaos route |
| --- | --- | --- | --- | --- |
| Mesopotamian federation | Mesopotamia or Mesopotamian Federation | New X-ending tag if no safe existing tag | River administration, irrigation, city integration | Ancient legitimacy claimant state |
| Assyrian restoration | Assyria | New X-ending tag if needed | Mountain and city diaspora route | Hidden restoration branch with wider claims |
| Levantine federation | Levantine Federation | X-ending or cosmetic route | Port cities, guarantees, confessional balance | Claimant congress and sponsor crisis |
| Jazira river state | Jazira Federation | X-ending | Rail, grain, and border settlement | Patron-backed border expansion |
| Gulf port federation | Gulf Federation or Coastal Emirates | X-ending or existing safe tag | Ports, convoys, recognition | Sponsor rivalry and naval protector clauses |

Mesopotamian and Assyrian routes need extra source checks for symbols and terminology. Ancient symbols, real religious emblems, and real flags must be sourced when used.

### African historical and local polity releases

| Formable family | Candidate public identity | Candidate tag class | Normal route | High-chaos route |
| --- | --- | --- | --- | --- |
| Kongo restoration | Kongo or Kongo Federation | Existing safe tag or X-ending route | Court legitimacy, river administration, foreign balancing | Royal restoration with regional claims |
| Benin route | Benin or Benin Federation | Existing safe tag if available | Court authority, regalia source work, city integration | Oba-centered claimant route |
| Swahili coast | Swahili Coast or Swahili League | X-ending | Ports, merchant houses, Indian Ocean trade | Maritime league with coercive port claims |
| Kilwa restoration | Kilwa or Kilwa Sultanate direction | X-ending | Port, trade, and island control | Hidden high-chaos coastal revival |
| Sahel confederation | Sahel Confederation | X-ending | Caravan routes, rail nodes, local assemblies | Hardline desert claimant route |
| Horn federation | Horn Federation | X-ending or existing safe tag | Ports, mountains, religious and clan balance | Sponsor-backed port and highland claims |

African formables should not be copy-pasted monarchy paths. Each should use regional institutions, ports, rivers, caravan routes, courts, local defense, and foreign pressure differently.

### South American indigenous and historical groups

| Formable family | Candidate public identity | Candidate tag class | Normal route | High-chaos route |
| --- | --- | --- | --- | --- |
| Mapuche confederation | Mapuche Confederation | X-ending unless safe existing tag | Terrain defense, autonomy, recognition | Wider frontier claimant route |
| Guarani union | Guarani Federation | X-ending | River communities, local defense, diplomacy | Basin claimant route |
| Aymara federation | Aymara Federation | X-ending | Highland communities and local assemblies | Highland restoration path |
| Andean confederation | Andean Confederation | X-ending or existing safe tag if available | Roads, highlands, negotiated integration | Imperial memory route, source-heavy |
| Patagonia federation | Patagonian Federation | X-ending | Sparse-state defense and port access | High-chaos frontier claims |

These formables should use hard terrain, supply strain, local control, and recognition problems. They should not become free core machines over huge areas.

### Asian regional polities

| Formable family | Candidate public identity | Candidate tag class | Normal route | High-chaos route |
| --- | --- | --- | --- | --- |
| Deccan federation | Deccan Federation | X-ending | Provincial councils, rail integration, local administration | Claimant congress with host conflict |
| Himalayan union | Himalayan Federation | X-ending or safe existing route | Mountain defense, monastery and border routes when sourced | Hidden mountain claimant path |
| Malay archipelago league | Malay Archipelago Federation | X-ending or existing safe tag | Ports, convoys, trade, island security | Maritime pressure route |
| Indochinese regional federation | Indochinese Federation | Existing safe tag only if not owned elsewhere, otherwise X-ending | Provincial autonomy and anti-puppet clauses | Sponsor-backed expansion |
| Inner Asian steppe union | Steppe Federation | X-ending | Cavalry, rail, and nomadic institutions | High-chaos steppe claimant path |

Asian formables need careful interaction with existing vanilla and mod tags. Many tags already exist or are used by other systems.

### Island and port polities

| Formable family | Candidate public identity | Candidate tag class | Normal route | High-chaos route |
| --- | --- | --- | --- | --- |
| Island federation | Island Federation | X-ending | Ports, convoys, naval guards, recognition | Anti-host maritime compact |
| Free port league | Free Ports Federation | X-ending cosmetic or faction identity | Trade and guarantees | Sponsor rivalry and blockade route |
| Mediterranean port union | Mediterranean Ports Federation | X-ending | Convoy access, coastal forts, neutral trade | Coercive port seizure path |
| Caribbean federation | Caribbean Federation | Existing safe tag if available, otherwise X-ending | Island defense and recognition | Maritime pressure and patron conflict |
| Pacific league | Pacific Islands Federation | X-ending | Convoy protection and naval access | High-chaos island chain claims |

These formations should make naval access, convoys, dockyards, ports, and outside sponsors matter.

### High-chaos niche and strange claimants

| Formable family | Candidate public identity | Candidate tag class | Reveal condition | Design limit |
| --- | --- | --- | --- | --- |
| Archive kingdom | Readable restored kingdom name by region | X-ending cosmetic or tag | High chaos, archive control, legitimacy route | Must still be human political content |
| Claimant republic | Readable republic or federation name | X-ending | Dossier success, border heat, host weakness | No joke tags as public names |
| River civilization route | Region name such as Mesopotamia | X-ending | Ancient legitimacy branch, high chaos | Source ancient symbols before use |
| City coalition | Readable city or port federation | X-ending or cosmetic | Several ports or cities released nearby | Do not replace every city with a tag |
| League federal successor | Free Nations Federation or regional equivalent | X-ending if tag needed | High League Authority, consent, recognition | Faction may be enough if full tag is too heavy |
| Coercive successor | Readable regional state name, not compact office name | X-ending if tag needed | Aggressive pressure, war success, low recognition route | Must create backlash and coalition risk |

High-chaos formables should be rare. They should feel alarming because they can reshape the region and provoke host or global reactions.

## Template formable tracks

### Defensive federation track

Used by European, Caucasus, island, and league-aligned formables.

Requirements:

- Legitimacy at least 55.
- Recognition at least 35.
- Border Heat below 55.
- Local Control at least 60 in the heartland and two anchor states.
- At least one settlement or arbitration success.
- Not in a coercive compact.
- Former host not reduced below survival guard.

Effects:

- Create formable tag or cosmetic identity.
- Convert selected claims into cores only after integration missions.
- Lower Aggressive Bloc Pressure.
- Raise League Cohesion if league member.
- Unlock common defense and recognition decisions.
- Add formation security mission for 180 to 270 days.

Partial success:

- Create weaker cosmetic identity or limited federation.
- Keep claims instead of cores.
- Raise instability and sponsor rivalry.
- Reveal follow-up integration missions.

### Restoration track

Used by Kongo, Benin, Kilwa, Volga Bulgaria, Assyria, and similar restored identities.

Requirements:

- Legitimacy at least 65 or restoration route focus completed.
- Local Control at least 65 in the historical or symbolic center.
- Recognition at least 25, or high-chaos route with strong military control.
- Archive, court, sacred, river, or port anchor mission completed.
- No unresolved host capital deletion risk.
- Historical symbol and flag asset source mode marked before implementation.

Effects:

- Apply restoration cosmetic tag or formable tag.
- Unlock restoration idea lifecycle.
- Unlock court, assembly, or religious authority decisions where appropriate.
- Raise Host Anger if former host owns disputed symbolic anchors.
- Unlock regional ambition focus insert.

Partial success:

- Restoration title is claimed but not fully recognized.
- More claims than cores.
- Recognition penalty or sponsor rivalry rise.
- Host receives response decisions.

### Indigenous confederation track

Used by Mapuche, Guarani, Aymara, and similar regional groups.

Requirements:

- Local Control at least 70 in heartland communities.
- Stability pressure under control.
- Defensive mission success in terrain anchors.
- Recognition at least 20, league support, or successful host settlement.
- No blanket cores over unrelated regions.

Effects:

- Create confederation identity.
- Unlock terrain defense, local autonomy, and community mobilization decisions.
- Add claims or cores only to integrated regions.
- Lower Patron Influence if self-rule route is chosen.
- Raise Border Heat if wider frontier claims are pressed.

Partial success:

- Confederation forms with low recognition.
- Local Control remains fragmented.
- Host or sponsor receives influence opportunities.

### Maritime league track

Used by Swahili, Kilwa, free port, island, Caribbean, Pacific, and archipelago formations.

Requirements:

- Control required ports.
- Convoy access or naval security mission completed.
- Foreign Support above 25 or domestic dockyard development.
- Local Control at least 55 in ports.
- Border Heat below 60 unless coercive route is active.

Effects:

- Unlock port integration decisions.
- Unlock convoy protection and dockyard reinforcement path.
- Raise Recognition through trade missions.
- Increase sponsor access risk.
- Enable league naval reserve decisions if in league.

Partial success:

- Maritime identity forms but patron influence rises.
- Convoy loss or blockade risk appears.

### Coercive formation track

Used by aggressive-bloc states and high-chaos claimant routes.

Requirements:

- Aggressive Bloc Pressure at least 65.
- Border Heat at least 55 or active claim conflict.
- Military readiness from army lane.
- At least one successful ultimatum, shock campaign, or border pressure mission.
- Recognition below 65 unless the country has a hardline ideological route that redefines recognition.
- Host survival guard still enforced.

Effects:

- Reveal stronger claims and war decisions.
- Add claims before cores.
- Raise Former Host Anger and Sponsor Rivalry.
- Lower Recognition and Coalition Trust unless in compact.
- Trigger super-event checks if enough members and territories are involved.

Partial success:

- The route gains claims but loses legitimacy.
- Members fracture or league sanctions appear.
- Host obtains emergency response missions.

## League endgame

The Independence League can remain a faction-like defensive system, become a loose diplomatic league, fracture into patron caucuses, or attempt a federal outcome.

| Endgame | Conditions | Outcome | Risks |
| --- | --- | --- | --- |
| Common front | Three or more members, Cohesion 55 or higher, Authority 35 or higher | Defensive faction or faction-like cooperation | Sponsor strings and unequal burden |
| Recognition bloc | Recognition campaign success, low Border Heat, several members | Shared recognition decisions, trade and guarantees | Weak military response if host attacks |
| Arbitration league | Multiple border settlements, Authority 45 or higher | Lowers Border Heat and prevents compact growth | Hardliners may defect |
| Federal congress | Cohesion 75 or higher, Authority 70 or higher, average Legitimacy 60 or higher, member consent | New X-ending federal tag or strong faction identity | Large integration burden and host fear |
| Patron caucus | Sponsor rivalry high, one sponsor dominates members | Members align under outside influence | Patron Influence crisis and league fracture |
| League collapse | Cohesion below 20 or failed defense of member | Faction dissolves, members return to local survival | Aggressive compact and host anger rise |

The league super-event should fire when the common front becomes globally meaningful, not when two weak releases sign a minor agreement.

## Federal league formation

A federal league formation should be rare.

Requirements:

- At least four Event 6 countries in the league.
- League Cohesion at least 75.
- League Authority at least 70.
- No member has Patron Influence above 65.
- No member is a puppet.
- Average Legitimacy at least 55.
- At least two successful league missions.
- Former host survival guard passes for every transfer.
- Every member consents through decision, AI consent, or route condition.

Outcomes:

- Create a federation tag only if the implementation has complete country package support.
- Otherwise apply a league-wide faction identity, shared ideas, and member cosmetic tags.
- Unlock shared defense reserves, common recognition tour, arbitration authority, and integration missions.
- Convert member territories gradually. Do not instantly absorb every member without consent and cleanup.
- Trigger a major league super-event if global thresholds are met.

AI should prefer faction identity over full federation unless it has high stability, low sponsor rivalry, and clear defensive need.

## Aggressive bloc endgame

The coercive compact is the high-chaos mirror of the league. It should be dangerous, but brittle.

| Endgame | Conditions | Outcome | Risks |
| --- | --- | --- | --- |
| Claim caucus | Pressure 45 to 64, two hardline members | Shared claim decisions | Low recognition and host anger |
| Coercive compact | Pressure 65 or higher, at least three members, host conflict active or likely | Faction-like aggressive bloc | Sponsor rivalry and global backlash |
| Partition congress | Pressure 80 or higher, high chaos, several disputed state groups | Coordinated ultimatums and partition plans | Super-event, war, and league response |
| Hegemon route | One member has much higher legitimacy and army strength | Leader directs compact pressure | Defectors and sanctions |
| Collapse through overreach | Failed war, pressure below 25, sponsor isolation | Compact breaks, members lose legitimacy | Host reclamation and league gains |

The compact should not use the public country name of an office or committee. If it forms a country, the country should be a readable regional state. The compact itself can be a faction, mechanic, or route label.

## Interaction between formables and league or compact systems

| Formable route | League effect | Compact effect |
| --- | --- | --- |
| Defensive federation | Raises Cohesion and Authority | Lowers Pressure unless hardliners are excluded |
| Restoration | League may recognize or arbitrate borders | Compact can turn restoration into maximalist claims |
| Indigenous confederation | League improves recognition and anti-puppet protection | Compact route is rare and should cause legitimacy strain |
| Maritime league | League gains naval reserve tools | Compact gains blockade and port seizure pressure |
| Federal league successor | Consumes or upgrades league mechanics | Compact treats it as a rival threat |
| Coercive formation | League sanctions or expels member | Compact gains pressure and super-event chance |

## Decision hooks

Formable decisions should use the formable preparation category from the decision and GUI file.

| Decision family | Formable use |
| --- | --- |
| Assemble regional dossier | Reveals formable, target groups, and route options. |
| Integrate claimant state | Converts controlled anchors into progress. |
| Neutralize rival claim | Removes rival legitimacy, reduces border heat, or causes backlash. |
| Convene formation assembly | Final pre-proclamation decision. |
| Formation security period | Post-formation mission that tests stability and control. |
| League arbitration panel | Peaceful route to disputed states. |
| Coordinated ultimatum | Coercive route to disputed states. |
| Host settlement offer | Former host can trade recognition, autonomy, demilitarization, or claims. |

## Focus hooks

| Focus route | Formable effect |
| --- | --- |
| Recognition route | Lowers recognition requirements and unlocks legal formation. |
| Host settlement route | Lowers Border Heat requirements and makes cores safer. |
| Army route | Unlocks formation security mission bonuses and coercive readiness. |
| League route | Opens federal league and common defense formables. |
| Neutrality route | Unlocks defensive federations without offensive claims. |
| Restoration route | Opens court, archive, river, or sacred center formation tasks. |
| Aggressive route | Opens coercive formation, wider claims, and compact outcomes. |
| High-chaos hidden route | Reveals unusual claimant identities and harsher backlash. |

## AI formable behavior

AI formable pursuit should be conservative unless the AI is strong, threatened, or route-committed.

| AI type | Preferred formable behavior |
| --- | --- |
| Survival AI | Avoids formables until legitimacy and local control are safe. |
| Legalist AI | Pursues recognition and settlement formables. |
| Militarist AI | Pursues army-backed formables if it can defend borders. |
| League AI | Supports federal or defensive formation when cohesion is high. |
| Patron-aligned AI | Forms only if sponsor supports it, risking dependency. |
| Hardline AI | Pursues coercive formation under high chaos and host weakness. |
| Host AI | Opposes formations that threaten capital, core regions, or strategic corridors. |

AI must stop formable pursuit if required targets become invalid, host survival guard fails, sponsor domination becomes too high for the selected route, or the country is near collapse.

## Formable cleanup

- Remove obsolete formation missions after proclamation, collapse, annexation, or route lock.
- Clear target state markers when owners change outside Event 6 logic.
- Replace working claims with permanent claims, cores, or removed claims based on integration outcome.
- Remove aggressive claim decisions after settlement routes close them.
- Stop duplicated formable attempts if another country already formed the same identity.
- If a tag is annexed, preserve only historical flags needed for achievements or event log memory.
- If a member joins another event system, Event 6 formable decisions must pause until origin compatibility is checked.

## Formable exploit prevention

| Exploit | Guard |
| --- | --- |
| Free core spam | Claims become cores only through integration missions or route capstones. |
| Host deletion | Mandatory host survival and capital retention checks. |
| Tag farming | Formable decisions require origin and one-time global or regional flags. |
| War-goal spam | Cooldowns, route locks, border heat caps, and target validity checks. |
| Puppet bypass | Puppet status blocks independent formables unless the route is a puppet compromise. |
| Sponsor exploit | Patron Influence can block anti-puppet and legal formation routes. |
| League absorption exploit | Member consent and authority checks before federation. |
| Compact snowball | Backlash missions, host response, recognition loss, and sponsor rivalry. |
| Scenario overload | Release-all scenario uses simplified formation reveal and active caps. |

## Release-all scenario formable behavior

The triggerable scenario can release all possible Event 6 countries. Formables should not all reveal on day one.

| Scenario type | Formable behavior |
| --- | --- |
| Independent releases | Each country uses normal reveal rules with shorter dossier cooldowns. |
| Common league | Defensive and federal routes reveal earlier, compact routes are suppressed unless high intensity allows fractures. |
| War with former hosts | Coercive and defensive routes reveal faster, legal routes require survival first. |
| War with everyone | Only survival and compact routes reveal early. Peaceful formables require stabilization first. |
| Partition congress | Hidden and aggressive formables are allowed, but host survival guard remains mandatory. |

Scenario intensity should scale starting territory, units, stockpiles, local control, instability, and reveal speed. It should not disable integration requirements entirely.

## Acceptance criteria for formables

The formable web is complete when the implementation agent can answer:

1. Which formable families exist by region.
2. Which formables are hidden, rare, ordinary, league-based, or coercive.
3. Which Event 6 origin checks protect overlap tags.
4. Which new tag, cosmetic tag, and route tag candidates need the X suffix.
5. Which state groups are required, optional, disputed, and protected.
6. Which values gate each route.
7. Which decisions and focuses reveal, build, and complete formation.
8. How former hosts are protected.
9. How league and compact outcomes alter formable routes.
10. How AI pursues or avoids each formation.
11. How formables create post-proclamation play.
12. What cleanup prevents duplicate, stale, or exploit formation logic.

## Super-event, asset, achievement, and documentation architecture

Independence Wave should reserve major presentation for moments that reshape the campaign. Ordinary release waves should use normal event, news, report, log, decision, and GUI presentation. Super-events should mark league formation, coercive compact escalation, frightening high-chaos partition shocks, rare formable proclamations, or scenario-wide outcomes that the whole world would notice.

## Super-event philosophy

A super-event should fire only when the wave has become a world-order moment.

Do not use a super-event for:

- every automatic wave
- every normal release package
- every small regional formable
- every local host settlement
- every sponsor recognition decision

Use a super-event for:

- a large Independence League becoming a meaningful global actor
- a coercive compact forming with several aggressive Event 6 countries
- a high-chaos release wave tearing several hosts at once
- a federal league successor forming through consent and authority
- a hidden high-chaos formation becoming a major regional threat
- the release-all scenario producing a globally visible settlement, war, or compact
- a former host or league defeating a major compact after a long crisis

## Super-event candidates

| Working role label | Trigger direction | Main actor | Effect role | Reuse rule |
| --- | --- | --- | --- | --- |
| League founding | At least four Event 6 countries, League Cohesion 65 or higher, League Authority 40 or higher, and global relevance from war, industry, population, or affected hosts | League leader or strongest eligible member | Creates faction-like global announcement, improves recognition access, opens common front goals | Fire once per campaign |
| Federal league proclamation | League Cohesion 75 or higher, Authority 70 or higher, average Legitimacy 55 or higher, no puppet members, and consent checks passed | League congress leader | Upgrades league into federation or strong faction identity | Fire once per federal outcome |
| Coercive compact | Aggressive Bloc Pressure 70 or higher, at least three hardline Event 6 members, active border conflict or prepared ultimatum | Compact leader | Announces aggressive bloc, raises host response and global fear | Fire once per compact |
| Great partition shock | Automatic wave creates ten releases, high chaos, at least three affected hosts, and average Host Anger high | Global event controller | Marks a frightening high-chaos wave | Fire once per campaign |
| Hidden restoration shock | A rare high-chaos formable controls a large enough region and follows a hardline route | Formable leader | Announces a regional power that looks larger than a normal release | Fire once per candidate family, with global cap |
| Host counterstroke | Former host defeats or reverses a major compact threat without being deleted | Former host | Marks old-state recovery after a dangerous wave | Fire once per host family or global cap |
| Scenario world release | Release-all scenario creates a league, all-host war, all-world war, or partition congress at high intensity | Scenario controller | Marks manual scenario outcome | Fire only from scenario path |

## Super-event threshold details

### League founding threshold

Required:

- Four or more Event 6 origin countries in the same league.
- League Cohesion at least 65.
- League Authority at least 40.
- At least one member has Recognition 45 or higher, or the league has completed a recognition mission.
- At least two former hosts are affected, or one major host is affected.
- No member has Patron Influence above 80.
- The event has not already fired.

Optional strengthening factors:

- A member is at war with a former host.
- A member controls a strategic port, rail hub, or capital anchor.
- The league has completed common defense or common recognition missions.
- High chaos raises visibility and lowers the member count requirement only for scenario paths.

Effects:

- Show super-event if settings allow.
- Add event log milestone.
- Unlock or strengthen league category decisions.
- Raise League Authority modestly.
- Raise Recognition for members with low recognition, capped to prevent free diplomacy.
- Raise Former Host Anger for affected hosts.
- Check achievement tracking.

### Federal league proclamation threshold

Required:

- Four or more members.
- Cohesion at least 75.
- Authority at least 70.
- Average Legitimacy at least 55.
- No member is a puppet.
- Consent checks complete.
- Sponsor Rivalry below 65.
- Border Heat average below 55, unless the federal route is defensive wartime unity.

Effects:

- Create a federation tag only if country package support exists.
- Otherwise strengthen league as a faction identity with member cosmetics.
- Unlock integration and common army missions.
- Set post-proclamation stability challenge.
- Fire super-event if global visibility threshold is met.

### Coercive compact threshold

Required:

- Three or more hardline Event 6 countries.
- Aggressive Bloc Pressure at least 70.
- At least one active host dispute, border incident, or ultimatum preparation.
- Average Recognition below 60, or a hardline route that rejects normal recognition.
- League route not dominant for those members.
- Former host survival guard remains active for every compact war or demand.

Effects:

- Form compact faction or faction-like pressure system.
- Raise Host Anger for every affected host.
- Lower global trust in Event 6 countries.
- Unlock synchronized claims, ultimata, and shock campaign missions.
- Fire compact super-event.
- Enable anti-compact league and host decisions.

### Great partition shock threshold

Required:

- Automatic wave count reaches ten.
- At least three hosts lose territory, or one major host loses several coherent packages.
- Chaos tier is Totalen Chaos or higher, or another strong chaos flag is active.
- The wave includes at least one ambition, partition, or high-chaos niche package.
- Global cap not already used.

Effects:

- Fire high-chaos wave super-event.
- Raise global chaos by an implementation-tuned amount.
- Increase sponsor rivalry and host anger in affected regions.
- Reveal more formable dossiers for eligible ambition packages.
- Add mission pressure to hosts and releases.

### Hidden restoration shock threshold

Required:

- Candidate is Event 6 origin.
- Candidate controls heartland and strong group.
- Candidate has completed restoration or coercive formation track.
- Candidate has enough industry, divisions, or controlled population to be more than a flavour state.
- High chaos or rare route flag active.
- Source mode for real symbols is recorded before asset work.

Effects:

- Fire a rare super-event if not blocked by global cap.
- Unlock late ambition branch.
- Raise host fear and regional diplomacy pressure.
- Add special achievement tracking.

## Super-event text direction

All super-event text should be direction-only at specification time. Implementation should research final wording and avoid pasted placeholders.

| Role | Title direction | Description direction | Button or cultural remark direction | Quote research direction |
| --- | --- | --- | --- | --- |
| League founding | Short, institutional, hopeful with tension | New states gathering under a shared charter, with host fear and sponsor attention visible | restrained diplomatic irony or congress register | self-determination, congresses, covenants, public-domain political speeches, treaty language |
| Federal proclamation | Formal and constitutional | A federation or common front becoming durable through consent and institutions | solemn, constitutional, or civic | federalism, liberty, assemblies, civic duty, public-domain political writing |
| Coercive compact | Ominous and martial | Released countries using independence as a claim weapon | cold military or legalistic menace | conquest, partition, revolutionary war, public-domain military or political texts |
| Great partition shock | Frightening, global, and concrete | Many borders breaking through petitions, archives, guards, and rail hubs | stunned press or diplomatic panic without generic warning labels | partition, empires, maps, borders, public-domain memoirs or speeches |
| Hidden restoration | Region-specific and symbolic | A restored name becoming a modern state with old symbols and new armies | route-specific, serious, not cheap comedy | sourced regional literature, chronicles, religious or court texts where appropriate |
| Host counterstroke | Stern recovery | A former host preventing a compact from consuming the region | grim administrative relief or military understatement | state survival, sovereignty, restoration, public-domain speeches or legal texts |
| Scenario world release | Broad and severe | The world filled with new governments at once | scenario-specific and stark | self-rule, collapse, congresses, world order, public-domain sources |

Quote research must compare several candidates, verify wording, attribution, source, date, public-domain or licensing confidence, and fit. Do not use unsourced quote-site copy. Do not invent quotes. Keep modern copyrighted fragments very short or avoid them.

## Super-event audio direction

Audio research should be done only when a specific super-event is selected for implementation.

| Role | Audio direction | Source mode |
| --- | --- | --- |
| League founding | restrained march, solemn civic hymn, chamber brass, or period congress music | public domain, Creative Commons, official archive, or approved existing track |
| Federal proclamation | warmer civic march or dignified ceremonial piece | same as above |
| Coercive compact | tense martial rhythm, dark brass, or austere drum cadence | same as above, no unclear recordings |
| Great partition shock | anxious orchestral or newsreel-like cue, not bombastic fantasy music | same as above |
| Hidden restoration | region-aware instrumentation only when licensing and cultural fit are clear | same as above, with extra source checks |
| Host counterstroke | stern military or state ceremony cue | same as above |
| Scenario world release | large, severe cue that can support global map transformation | same as above |

Required audio research record:

- track title
- composer and performer when known
- source URL
- license and usage terms
- composition rights and recording rights status
- duration
- original source path
- final game-ready path
- suggested sound id
- editing notes
- why the track fits the exact role
- uncertainty or blocker

Do not call default or placeholder audio complete.

## Super-event image direction

| Role | Image direction | Source mode |
| --- | --- | --- |
| League founding | delegates, flags, improvised congress hall, maps as secondary props, anxious guards outside | generated unless a real archival image is intentionally used as a generic congress reference |
| Federal proclamation | shared banners, guarded assembly, rail or port symbols, mixed uniforms | generated for fictional federation, sourced only for real archive references |
| Coercive compact | hardline leaders, border posts, armed councils, rail maps as props, compact troops moving | generated fictional or symbolic |
| Great partition shock | crowds at stations, border offices overwhelmed, new flags on government buildings, not a flat map | generated documentary-style or sourced archival crowd material if generic and licensed |
| Hidden restoration | region-specific court, river, port, mountain, or symbolic assembly | sourced for real symbols and real regalia, generated for fictional route scenes |
| Host counterstroke | recovered capital, host troops at rail hubs, reclaimed offices, civilians returning | generated or sourced archive-style depending on exact country |
| Scenario world release | wall of new flags, ports, rail stations, assembly halls, global disorder | generated symbolic documentary composition |

Super-event images should use 457x328 final size. They need strong central composition and enough contrast for the super-event UI.

## Visual asset package directions

### Global Event 6 assets

| Asset family | Needed assets | Size direction | Source mode |
| --- | --- | --- | --- |
| Report event image | Wave release report, host response report, league report, compact report | 210x176 | generated documentary style unless a real archive scene is selected |
| News event image | Major league or compact news images | 397x153 black and white | generated or sourced depending on role |
| Super-event images | one per approved super-event role | 457x328 | generated for fictional or alternate-history moments, sourced for real historical material |
| Decision category icons | provisional statecraft, local control, recognition, host response, league, compact, formable preparation | 32x32 | generated icons |
| Idea icons | legitimacy crisis, recognition question, unsettled borders, host pressure, patron dependency, league charter, compact pressure | 64x64 | generated icons unless historical symbol is used |
| Focus icons | survival, recognition, army, local administration, league, compact, restoration, formable | 94x86 | generated icons with HOI4 focus style |
| Scripted GUI pieces | ledger panel, meters, state cards, warning seals, league and compact emblems | surface-specific | generated UI art, animated only if source frames exist |
| Achievement icons | completed, grey, and not-eligible variants for each achievement | 64x64 | generated icons |

### Country package assets

| Country package tier | Required assets |
| --- | --- |
| Seed | flag set, basic leader or council portrait, shared idea icons, shared focus icons |
| Compact | above plus route-specific decision and focus icons where visible |
| Regional | above plus regional insert icons, regional flag variants when route changes identity |
| Partition | above plus host dispute icons, border warning icon, possible cosmetic flag |
| Ambition | above plus formable flag, formable icon, ambition route icons, super-event candidate art if global threshold can be met |
| Special high-chaos | above plus generated or sourced unusual route art, extra icon variants, possible animated GUI or emblem plan |

### Flag rules

- Historical flags and well-attested historical symbols require sourced visual work.
- Fictional route flags, alternate-history flags, league emblems, compact emblems, and invented high-chaos flags can use generated art.
- Every new Event 6 custom tag, formable tag, cosmetic tag, or route split tag must end with `X`.
- Flag filenames must follow HOI4 tag and ideology conventions.
- Flags should remain readable at 82x52, 41x26, and 10x7.
- Cosmetic tags should not use office names as public country names.

### Leader and portrait rules

- Real leaders require sourced portraits.
- Fictional one-person leaders can use generated portraits with region-aware name pools and correct gender metadata.
- Councils, committees, juntas, courts, assemblies, or symbolic bodies should use institutional portraits and institutional names.
- Generated portraits should fit the 1936 to 1945 era unless the route intentionally uses a surreal or high-chaos presentation.
- Do not fabricate real people.

### Animated asset direction

Use animation sparingly.

Possible animated assets:

- league charter seal in scripted GUI
- compact warning seal in scripted GUI
- high-chaos formable emblem
- route-state glow for hidden restoration
- sponsor rivalry warning meter

Every animated asset must have real source frames, a frame sheet, a static fallback, and verified GUI or GFX surface support. Do not create final motion by moving one still image.

## Achievement suite

Achievement entries below use implementation-oriented ids and direction. They are not final player-facing titles or descriptions.

| Achievement id | Player role | Unlock direction | Disqualifiers | Icon direction |
| --- | --- | --- | --- | --- |
| `chaosx_006_survive_the_first_year` | Released country | Survive one year after Event 6 release with Legitimacy 45 or higher and capital held | becoming a puppet or losing origin capital | provisional flag over guarded capital |
| `chaosx_006_recognized_without_strings` | Released country | Reach Recognition 70 with Patron Influence below 25 | accepting puppet status or major patron concession | diplomatic seal with broken strings |
| `chaosx_006_settle_the_border` | Released country or host | Resolve a major Event 6 border dispute through settlement or arbitration without war | starting a reclamation war for the same dispute | border marker and signed file |
| `chaosx_006_first_common_front` | League member | Create a meaningful Independence League and complete a common defense mission | league collapses before mission completion | several small flags under shield |
| `chaosx_006_no_member_left_behind` | League leader | Win or survive a host war with all league members independent and no member puppeted | any member becomes puppet during the war | convoy and flags behind fort line |
| `chaosx_006_federal_congress` | League leader | Complete federal league formation through consent and authority | compact route active or sponsor domination | assembly hall and federation seal |
| `chaosx_006_compact_of_claimants` | Hardline release | Form the coercive compact and complete the first shock campaign | compact collapses before campaign completion | dark border files and bayonets |
| `chaosx_006_break_the_compact` | Host or league opponent | Defeat or dissolve a major coercive compact | compact never reaches major threshold | shattered compact emblem |
| `chaosx_006_host_still_stands` | Former host | Survive multiple Event 6 releases while keeping capital and at least one settlement path open | capital lost through Event 6 transfer | old capital under guarded flag |
| `chaosx_006_treaty_host` | Former host | Settle several Event 6 breakaways without deleting them and without triggering reclamation war | annexing a released country before settlement | treaty table with capital skyline |
| `chaosx_006_regional_formable` | Released country | Form any normal Event 6 regional formable and complete formation security | formable created by non-Event 6 origin | new regional flag over railway |
| `chaosx_006_hidden_restoration` | Released country | Form a hidden high-chaos restoration and survive the backlash mission | accepting puppet compromise during backlash | old symbol and modern rifles |
| `chaosx_006_port_league` | Maritime release | Create a maritime or port federation with convoy route secured | losing required port before mission ends | lighthouse, convoy, and flag |
| `chaosx_006_clean_wave` | Any player or scenario controller | Complete a ten-country wave with every host survival guard intact | any host deleted by Event 6 | map pins around protected capital, not a full map icon |
| `chaosx_006_all_flags_still_fly` | Release-all scenario | In a release-all scenario, keep every released capital controlled by its release for the first global mission | any release loses capital before mission end | many small flags around a guarded globe |
| `chaosx_006_no_master_no_puppet` | Released country | Reject puppet status, keep Patron Influence below foothold, and reach stable legitimacy | becoming subject or accepting patron concession | broken chain and official seal |
| `chaosx_006_old_name_new_state` | Ambition package | Complete restoration route with sourced or generated route assets wired and state integration finished | route abandoned or origin mismatch | old emblem remade as modern state seal |
| `chaosx_006_arbitrator` | League leader or neutral release | Resolve several member disputes through arbitration while keeping cohesion high | member war between league members | scales, flags, and border posts |

Achievements must have tracking flags or variables, unlock triggers, disqualifiers, localisation, icons, docs, and any route or formable hooks. Do not turn difficult achievements into automatic unlocks.

## Achievement tracking architecture

| Tracking need | Suggested implementation direction |
| --- | --- |
| Release origin | Set on created Event 6 country at release and preserve through tag switch. |
| Former host identity | Store host target for settlement, reclamation, and achievements. |
| Capital held | Track original Event 6 capital state and current control. |
| Puppet disqualifier | Set permanent disqualifier if subject status is accepted after release. |
| Patron influence cap | Track peak Patron Influence for relevant achievements. |
| League membership | Track league founding, member count, cohesion, authority, and common mission success. |
| Compact threshold | Track pressure, members, and first campaign mission. |
| Formable origin | Formation must read Event 6 origin before unlocking achievement. |
| Scenario path | Release-all scenario sets variant flags and enables scenario achievements. |
| Host survival | Track every Event 6 transfer against host deletion and capital retention. |

## Documentation outputs

Implementation should create or update:

- source spec files under `docs/specs/006_independence_wave_specs/`
- event documentation under `docs/events/006_independence_wave.md` or the existing event doc pattern
- event detail and evolution detail sources after final localisation exists
- event log entries for release waves, league formation, compact formation, major formables, host settlement, and scenario outcomes
- asset documentation under `docs/assets/006_independence_wave/`
- super-event research records for quotes and audio once selected
- achievement documentation and icon records
- country package registry with tag status, source mode, and implementation status
- validation notes for host survival, origin separation, release counts, scenario variants, and cleanup

Spreadsheet rows should be updated only after implementation wording exists, because spreadsheet fields that mirror in-game text should use the in-game text as source.

## Acceptance criteria for presentation and achievements

This layer is complete when the implementation agent can answer:

1. Which super-events can fire and which ordinary outcomes do not deserve one.
2. What thresholds and values trigger each super-event.
3. What role each super-event plays.
4. What quote, button, and description research direction fits each role.
5. What audio research direction fits each role.
6. What visual source mode applies to every major asset.
7. Which flags, portraits, icons, GUI pieces, and achievement assets are required.
8. Which historical flags, symbols, and real portraits require sourced work.
9. Which fictional, symbolic, alternate-history, and high-chaos assets can be generated.
10. Which achievements exist, who can earn them, and what disqualifies them.
11. How achievement tracking reads Event 6 origin, host survival, league, compact, formable, and scenario state.
12. Which documentation and catalog surfaces must align after implementation.
