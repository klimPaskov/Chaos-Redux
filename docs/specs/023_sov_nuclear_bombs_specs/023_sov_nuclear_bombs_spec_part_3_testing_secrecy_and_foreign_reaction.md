# Event 023 specification, Part 3: Testing, secrecy, and foreign reaction

## Purpose of the testing layer

Testing converts a hidden stockpile into credible military knowledge. It proves that devices work, trains the delivery and command chain, exposes weaknesses, and changes what foreign governments believe.

A test should never be a decorative button. It should require a prepared site, a certified device, a functioning command chain, and a decision about secrecy. The result can improve Arsenal Readiness, damage Command Integrity, expose the program, contaminate the test region, kill people through an accident, or start the wider arms-race reaction.

Testing does not replace combat use. A test establishes demonstrated capability and foreign awareness. It does not count as a strike against a country, does not create a combat target, and does not grant automatic compliance from later threats.

## Public knowledge states

Foreign knowledge is tracked as a discrete global state for Event 23. The detailed evidence score may remain internal, but the player should see the current public knowledge state in the decision category.

| State | Meaning | Typical consequences |
| --- | --- | --- |
| Unknown | No foreign government has credible evidence | Foreign reaction remains limited to ordinary intelligence activity |
| Suspected | One or more governments have fragments, unexplained observations, or defectors | Counterintelligence pressure rises and some majors begin contingency planning |
| Confirmed in private | At least one major has reliable classified proof | Private warnings, espionage, and accelerated research hooks become possible |
| Demonstrated | A public test, acknowledged device, or unmistakable launch proves the arsenal | Global news, arms-race hooks, guarantees, sanctions, and strategic planning activate |
| Employed | A Soviet weapon has been used in conflict | Shared nuclear condemnation, death, contamination, and retaliation systems become the dominant foreign response |

Knowledge cannot normally move backward after Demonstrated or Employed. A successful cover-up can reduce current intelligence exposure while the arsenal is Unknown, Suspected, or Confirmed in private. It cannot make a witnessed public test disappear.

## Evidence and exposure

The event should keep one internal exposure score that summarizes how close the secret is to moving to the next public knowledge state.

Exposure rises through:

- Reactor construction in exposed or foreign-observed regions.
- Large rail movements between production, storage, and delivery sites.
- Poorly guarded storage.
- Foreign intelligence networks.
- Scientist defection or arrest.
- Missing documents.
- Test preparation visible from abroad.
- Atmospheric or surface testing.
- Accidents, fires, or contamination around a site.
- Public threats that imply a usable weapon.
- Soviet Collapse and disputed local custody.
- Captured facilities, devices, or technical personnel.

Exposure falls through:

- Counterintelligence sweeps aimed at a specific compromised site.
- Moving preparation away from borders and active fronts.
- Compartmentalizing transport and assembly.
- Repairing a known security breach.
- Returning missing documents or personnel.
- Canceling an exposed test before detonation.

Exposure should not become a third permanent player-managed meter. The category should show a short status such as secure, watched, penetrated, or public. Exact evidence sources belong in tooltips and reports.

## Test-site selection

A nuclear test needs an exact state. The site must be selected from a bounded pool of valid Soviet-owned and Soviet-controlled states.

A strong test site normally has:

- Low population density.
- No active land combat.
- Secure rail or infrastructure access.
- Distance from hostile borders.
- A secure route from a registered storage site.
- Enough local control to evacuate or restrict the area.
- No current occupation or breakaway custody dispute.

The implementation should prefer remote interior states and should avoid capitals, major population centers, dense industrial states, and states already suffering heavy contamination. The exact eligible state pool must be verified against the current map and current Soviet territory. No historical test-site state should be assumed without checking the installed map and state ownership.

A player-selected site should remain the target throughout preparation. The event must not silently substitute another state when the chosen site becomes invalid. The preparation mission should fail safely, return any uncommitted device, and explain the invalidation.

## Test preparation mission

Testing begins with a timed mission. The mission represents site construction, transport, instrumentation, exclusion zones, command rehearsals, and device certification.

Recommended duration bands:

- Laboratory-backed proof test preparation: 90 to 120 days.
- Concealed remote test preparation: 120 to 180 days.
- Public demonstration preparation: 90 to 150 days.
- Emergency wartime demonstration: 45 to 90 days, with much higher accident and exposure risk.

The mission should require a real commitment. Appropriate costs include one certified bomb, support equipment, trains, fuel, civilian factory burden, air experience, or a temporary diversion of technical capacity. No test action may use more than four spendable cost types.

The bomb should be reserved when the mission begins and consumed only when the test detonates or the device is destroyed in an accident. A canceled preparation should return the reserved device after a short accounting delay. This prevents cancel-and-duplicate exploits.

## Test profiles

### Instrumented proof test

This is the least visible full detonation available to the Soviet Union.

- Requires a secure remote site.
- Uses extensive instrumentation and a controlled exclusion zone.
- Gives a strong Readiness gain.
- Has the lowest normal exposure among detonating tests.
- Still creates shared test contamination and can be detected.
- Does not unlock public coercive doctrine by itself unless foreign detection becomes conclusive.

### Concealed field test

This profile prioritizes secrecy over safety and data quality.

- Uses a remote surface, tower, or shallow containment arrangement validated against the current nuclear system.
- Gives a moderate Readiness gain.
- Creates higher accident and venting risk.
- Can leave local contamination and deaths if evacuation or containment fails.
- May move foreign knowledge directly from Unknown to Suspected or Confirmed in private.

### Public demonstration test

This profile deliberately reveals the arsenal.

- The Soviet Union chooses whether to invite observers, issue advance notice, or reveal the test only after detonation.
- Gives a major Readiness and credibility gain.
- Sets public knowledge to Demonstrated.
- Opens Demonstrative Deterrence.
- Activates foreign arms-race hooks and the global news event.
- Adds condemnation only through the shared nuclear-test consequence route and any current international rules. It does not use the same severity as a combat strike.

### Wartime demonstration

This profile is performed during a live conflict to pressure an enemy without striking its populated territory.

- The exact test state remains Soviet controlled or another verified uninhabited demonstration location supported by the shared adapter.
- The targeted enemy receives a specific report and a limited response window.
- The action may improve threat credibility, but it does not force compliance.
- Failure, interception, or a visible accident sharply reduces credibility and Integrity.
- AI uses this only when a valid enemy demand is active and a limited demonstration is safer than immediate combat use.

## Test outcome families

Tests should resolve through a weighted result model that is audited with named scenarios. The outcome depends on Readiness, Integrity, custody doctrine, site quality, preparation time, technical capacity, war disruption, exposure, and the chosen test profile.

### Clean success

- The device detonates as intended.
- Readiness rises strongly.
- Technical confidence and delivery preparation improve.
- Shared test contamination and any local deaths apply.
- Exposure follows the chosen profile.

### Partial yield or poor instrumentation

- The device detonates, but useful data is limited.
- Readiness rises modestly.
- Another test becomes more attractive.
- Foreign observers may still treat the arsenal as demonstrated.
- Local contamination may be worse than the military benefit suggests.

### Failed detonation

- The reserved bomb is consumed or rendered unusable according to the shared test adapter.
- Readiness falls.
- Integrity may fall if commands concealed the failure or blamed each other.
- Foreign knowledge can remain uncertain unless the site was observed.
- A recovery and investigation mission opens.

### Premature accident

- The device or its high-explosive components fail during transport or preparation.
- The shared death and contamination systems receive an accident profile, not a nuclear strike profile, unless a true nuclear yield occurs.
- The storage or test state may become exposed.
- Command Integrity falls sharply.
- The player must choose between evacuation, cover-up, technical investigation, and public admission.

### Foreign observation

This can occur alongside another result.

- One or more majors gain Confirmed in private knowledge.
- A public leak can move the state to Demonstrated.
- Counter-program and diplomatic reactions begin.
- The Soviet Union receives a report that indicates the source of exposure without revealing hidden foreign calculations.

## Test safety decisions

The test layer should expose no more than three to five primary actions at one time.

Useful actions include:

- Survey a remote test state.
- Prepare the selected site.
- Strengthen evacuation and instrumentation.
- Conduct the chosen test.
- Cancel and recover the device.
- Investigate a failed or compromised test.

The player should not choose safety through several tiny purchases. One stronger preparation action can trade time and equipment for lower accident risk and better data.

## Secrecy incidents

Secrecy incidents are event-driven and bounded. They should not require a recurring whole-world scan.

### Missing physicist

A scientist fails to report or is detained abroad.

Possible directions:

- Quiet recovery through intelligence assets.
- Public accusation and diplomatic pressure.
- Internal purge, which can protect secrecy while lowering technical capacity and Integrity.
- Acceptance that a foreign major now has Confirmed in private knowledge.

### Compromised rail manifest

A transport record reveals unusual guarded movements.

Possible directions:

- Reroute the convoy at a readiness cost.
- Continue and risk exposure.
- Create a decoy shipment at an equipment and rail cost.
- Move the device into a temporary site, which weakens custody security.

### Foreign aircraft over the site

An aircraft, reconnaissance mission, or neutral observer sees preparation.

Possible directions:

- Cancel the test.
- Accelerate it before more evidence is gathered.
- Invite selected observers and convert the incident into a controlled demonstration.
- Issue a denial and accept that suspicion remains.

### Contaminated workers

Workers or soldiers leave a restricted area with visible illness or contamination.

Possible directions:

- Medical isolation and compensation.
- Coercive confinement, which raises atrocity or cover-up evidence if exposed.
- Public safety admission without revealing the full arsenal.
- Destruction of records, which can add hidden cover-up evidence.

### Captured device component

An enemy or breakaway obtains a component, document, or damaged device.

Possible directions:

- Recovery raid.
- Negotiated return.
- Public claim that the material is industrial.
- Emergency redesign and authentication changes.

## Foreign reaction framework

Foreign reactions should depend on what is known, not on the hidden opening alone.

### Major powers

A major that reaches Confirmed in private knowledge may:

- Increase intelligence activity against Soviet nuclear sites.
- Shift research priorities toward nuclear weapons, air defense, strategic bombers, missiles, shelters, or dispersion.
- Seek private talks.
- Warn allies and selected minors.
- Prepare sanctions or guarantees that activate after a public reveal.
- Create a future hook for Event 76 without firing or implementing that event.

A public demonstration may add:

- A news event.
- Emergency strategic planning.
- Public condemnation or calls for inspection.
- Counter-test preparation if Event 76 later exists and is valid.
- Stronger guarantees for threatened countries.
- Pressure to create an arms-control conference.

### Minor countries

Minor reactions should focus on survival and alignment.

They may:

- Seek a guarantee from a nuclear or conventional major.
- Join a faction.
- Offer access, resources, or diplomatic support to the Soviet Union.
- Disperse industry and command.
- Build shelters or emergency plans through shared systems when available.
- Publicize Soviet threats to increase the cost of coercion.

### Soviet allies and subjects

Allies should not automatically receive weapons or command access.

They may:

- Request protection under a Soviet nuclear guarantee.
- Offer test or storage access only if current rules support exact safe custody.
- Fear becoming targets of retaliation.
- Demand consultation before Soviet use from their territory.
- Distance themselves after civilian targeting or repeated threats.

## Arms-race hook activation

Event 23 should expose neutral hooks for later content.

Recommended hook moments:

- Foreign private confirmation.
- First public Soviet test.
- First acknowledged Soviet threat.
- First combat use.
- First breakaway custody crisis.
- First multi-major exchange.

The hook records the moment and the relevant actor. It must not grant another event's technology, fire another draft event, create an unverified cluster, or assume that Event 32, Event 76, or Event 47 is implemented.

## News and report presentation

The hidden opening remains a Soviet country event.

Use report events for:

- Test-site selection.
- Preparation incidents.
- Failed or partial tests.
- Foreign penetration.
- Internal safety disputes.

Use global or regional news for:

- A public demonstration test.
- A test detected beyond credible denial.
- A public Soviet nuclear ultimatum.
- The first Soviet combat use.
- A breakaway arsenal seizure that becomes public.

The first multi-major exchange uses the dedicated nonterminal super-event defined later in this package.

## Writing direction

Testing text should focus on the physical work, restricted zones, technical uncertainty, frightened workers, military impatience, and the consequences of evidence escaping the site.

Avoid generic staff-table scenes, empty declarations that history has changed, and final wording that calls an event a warning. Public reaction should mention concrete behavior such as evacuations, cancelled trains, embassy departures, unusual aircraft patrols, and foreign mobilization.

Humour should be absent from accidents, contamination, and deaths. A dry bureaucratic tone can appear in internal cover-up options when it exposes the cruelty or absurdity of the policy.
