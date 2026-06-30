# Event 011 Secret Alliance decisions and missions specification

## Category life cycle

The decision category should appear only after the target has enough public reason to act. It can open through:

- Evolution II.
- A suspicion threshold reached during baseline or Evolution I.
- A captured agent event.
- A member leak.
- A serious sabotage or assassination attempt.

Before the category opens, the player sees reports and minor effects. After it opens, the player manages a counter-conspiracy system. The category should hide obsolete decisions after reveal and replace them with public crisis decisions.

## Category header values

The category header or attached Dossier Board should show:

- Suspicion.
- Evidence.
- Preparedness.
- Infiltration.
- Pact pressure.
- Estimated member count.
- Known members.
- Last incident type.

The values should use integer formatting where appropriate. Dynamic localisation should explain what raised or lowered a value in broad terms without revealing hidden future surprises.

## Dossier Board scripted GUI direction

A scripted GUI is useful because the player is managing hidden member cards, evidence, and preparedness. It should open from the decision category.

Recommended layout:

| Area | Content |
| --- | --- |
| Header | Target country emblem, warning seal, and current stage indicator |
| Left column | Known and suspected member cards |
| Center board | Evidence meter, pressure meter, and preparedness meter |
| Right column | Action buttons for investigation, diplomacy, defense, and war preparation |
| Footer | Last incident, next mission deadline, and active operation cap |

Member cards begin as unknown silhouettes. A member becomes partially known when evidence crosses a member-specific threshold. A fully exposed member card shows country name, role, confidence, and whether it is wavering, founder, patron, or public member.

Animated states should clarify danger:

- Radio pulse when an investigation can run.
- Red thread glow when pressure rises.
- Shaking file seal when reveal is near.
- Warning border around a known neighboring member that can start border operations.
- Static fallback for every animated asset.

## Action families

### Investigation actions

Investigation actions raise evidence, lower infiltration, and reveal members. They can fail and warn the pact.

| Action | Availability | Cost direction | Success | Failure |
| --- | --- | --- | --- | --- |
| Trace diplomatic pouches | Category open, at least one unknown member | Command power, agency strength, or civilian office burden | Evidence rises, chance to expose one member | Pact pressure rises and member confidence rises |
| Turn a courier | Courier circuit incident or enough suspicion | Political capital, money-like civilian burden, and operative access | Evidence rises strongly, member-specific exposure rises | Infiltration rises, possible assassination risk |
| Break the radio net | Requires agency or signal capacity | Air XP, support equipment, and command power | Lowers cohesion and reveals action timing | The pact changes ciphers and pressure rises |
| Audit foreign missions | Requires industrial survey or sabotage pattern | Civilian factory burden, stability risk, and time | Blocks next sabotage bonus | Diplomatic chill increases |
| Build the public dossier | Evidence near threshold | Political power plus press credibility or stability cost | Opens controlled evidence reveal | Weak dossier can harden pact members |

### Defensive actions

Defensive actions convert resources into preparedness and lower damage.

| Action | Availability | Cost direction | Result |
| --- | --- | --- | --- |
| Guard rail and port nodes | Any stage after category open | Infantry equipment, trains, command power, and tied-down divisions in key states | Preparedness rises and rail sabotage damage falls |
| Vet military staff | After first command incident | Army XP, command power, and temporary planning penalty | Assassination and leak effects weaken |
| Harden munitions plants | Industrial states in target country | Support equipment, trucks, and military factory output burden | Factory sabotage damage falls |
| Secure capital ministries | Low stability or high infiltration | Political power, stability cost, and local police pressure | Infiltration falls, chance to catch agents |
| Protect war industries | At war or high pact pressure | Army XP, support equipment, and fuel | First public war council effect weakens |

### Diplomatic actions

Diplomatic actions split members and control reveal timing. They should be weaker against fanatical members and stronger against wavering minors.

| Action | Availability | Cost direction | Result |
| --- | --- | --- | --- |
| Quiet talks with a suspected member | Partially known member | Political power, improved relations work, and trade concession | Can mark member wavering or lower confidence |
| Offer a face-saving exit | Wavering member | Civilian factory burden, temporary trade penalty, or non-aggression pledge | Member leaves or refuses and leaks attempt |
| Pressure neutral chancelleries | High evidence | Political power and diplomatic credibility | Makes future invitations harder |
| Publish a controlled leak | Evidence threshold met | Stability risk and media credibility | Reveals one member or lowers cohesion |
| Demand embassy expulsions | Public or near-public evidence | Political power, stability, and relations risk | Lowers infiltration and raises pressure |

### Border operations

Border operations appear only against neighboring pact members. They should be framed as limited military actions, not full wars. They can use border conflict mechanics if available.

| Action | Availability | Objective | Cost direction | Success | Failure |
| --- | --- | --- | --- | --- | --- |
| Sweep the frontier safehouses | Neighbor member partly exposed | Place supplied divisions in border states | Command power, infantry equipment, and local supply | Member exposure rises, border provocation blocked | Pressure rises and member confidence rises |
| Seal the courier pass | Neighbor member with courier route | Hold named border or rail states for deadline | Trains, trucks, and tied-down divisions | Cohesion falls, evidence rises | Infiltration rises |
| Limited border reprisal | Evolution II, high evidence, neighbor member | Win a restricted border operation | Army XP, command power, equipment, and war support risk | Member preparedness weakens and target preparedness rises | Immediate reveal chance rises |
| Border war readiness mission | Evolution III near reveal | Keep divisions, supply, and fuel ready | Fuel, equipment, and time | Improves first war defense | Weak readiness gives pact opening bonus |

### War preparation actions

War preparation opens after Evolution II and becomes stronger after reveal.

| Action | Availability | Cost direction | Result |
| --- | --- | --- | --- |
| Draft emergency contingency plans | Evolution II | Army XP and command power | Preparedness rises and first public crisis penalty falls |
| Secure fuel reserves | Evolution II or III | Fuel and civilian factory burden | War readiness rises, temporary consumer goods burden |
| Mobilize local defense committees | High pressure | Manpower, infantry equipment, stability risk | Defensive temporary units or state modifiers after reveal |
| Rally friendly governments | High evidence | Diplomatic credibility and relations | Can generate guarantees or volunteer routes |
| Prepare public war case | Evidence high | Political power and time | Reduces stability hit from preemptive war option |

### Post-reveal actions

After public reveal, hidden actions are replaced by direct crisis actions:

- Demand pact disbandment.
- Call friendly governments.
- Launch preemptive strike if war case and preparedness are high.
- Accept a limited settlement if the pact revealed through ultimatum and enough members are wavering.
- Isolate the patron with evidence and diplomatic pressure.
- Prepare for simultaneous declarations.

The war option should be available in Evolution III. It should be stronger when the player prepared and riskier when evidence is weak.

## Mission design

Timed missions should require action rather than passive waiting.

### Guard the capital network

The player must hold the capital state, keep local divisions on the state, and complete one relevant security action. The capital state should also have a route asset or city category so the mission tests a real network point. Success raises preparedness and blocks one assassination or sabotage incident. Failure raises infiltration.

### Secure the industrial belt

The mission targets a controlled factory state with infrastructure and local divisions. The target also needs a plant-security action such as hardened munitions plants or blocked sabotage. Success lowers sabotage damage. Failure creates an industrial incident.

### Keep the foreign route watched

This mission appears after a courier route is suspected. It requires trains, a sealed or audited route, and a guarded rail, port, air, or frontier route when one exists. If the target has no foreign route objective state, the mission can resolve through the investigation work alone. Success raises evidence. Failure increases pact cohesion.

### Expose the patron's hand

This mission appears when a major patron is suspected. It requires high evidence, the identified patron, diplomatic or leak work, and a guarded route file when a route objective exists. Success can stop a second major from joining. Failure raises patron confidence.

### Hold the border during public crisis

This mission appears at Evolution III against neighboring public members. It requires fuel, a defense plan, and local divisions in a controlled core state that borders a public member. If no neighboring public member exists, the mission can resolve through national readiness alone. Success weakens the pact's first offensive. Failure gives the pact momentum.

## Active mission cap

The category should show at most a small number of active missions. A good target is one investigation mission, one defensive mission, and one border or diplomacy mission at a time. The implementation can use a priority pool so the player sees relevant actions rather than a wall of similar objectives.

## Costs and sacrifice palette

Major action families should not rely on political power alone. Use:

- Command power for military attention.
- Army XP for planning, vetting, and border operations.
- Air XP for signal and reconnaissance efforts where appropriate.
- Infantry equipment, support equipment, trucks, trains, convoys, and fuel for physical security.
- Manpower for guard committees and border watch.
- Stability and war support for public fear and militarized response.
- Civilian factory burden for ministry work, concessions, and industrial security.
- Tied-down divisions in states for guard missions.
- Relations and trade concessions for diplomatic exits.
- Evidence and preparedness values as requirements, not only as outputs.

Costs should scale with country size and target importance. A small country should face a painful but possible burden. A large country should pay more and cover more state targets.

## Success, failure, and partial outcomes

Every significant action should have distinct success and failure behavior. Partial success should be common enough to make choices interesting.

Examples:

- A courier is captured, but the pact changes route and pressure rises.
- A suspected member is exposed, but the major patron accelerates public reveal.
- An industrial survey is blocked, but diplomatic relations worsen.
- A border operation succeeds, but member confidence turns into open hostility.
- A public dossier forces two minors to leave, but the remaining members become more committed.

## Exploit controls

- Investigation actions need cooldowns and active caps.
- Member exit routes should not farm repeated rewards.
- Border operations should not grant free cores or permanent conquest.
- War case preparation should not allow war goal spam.
- Defensive missions should not create infinite temporary units.
- Failed actions should not be harmless. Repeated failures should make the pact more dangerous.
- AI should not click expensive actions when the target state set or member scope is invalid.
