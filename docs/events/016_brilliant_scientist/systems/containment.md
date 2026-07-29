# Event 016 Containment and Sovereignty

## Purpose

The sovereignty board is the final hosted Directorate crisis. It does not select an outcome by a new random roll. Every action is resolved against the institutions, facilities, security posture, project history, foreign relationships, Dependence, Independent Capacity, and Grievance produced during the preceding chain.

The board is decision-led and remains inside the host's existing national-focus tree. It opens after the fourth and final logged evolution, `Sovereign Science`, unless the disabled-evolution safety route has already concluded the chain through the regional compact.

## Sequence

1. Evolution IV records one response: charter, concession, military seizure, foreign containment, or refusal. Concession is offered only after institutional capture is already proven.
2. `brilliant_scientist_start_sovereignty_deadline` prepares a live territory plan, selects one valid exile recipient, calculates the opposing hidden strength scores, and activates the visible sovereignty mission.
3. The host can execute one timed decision. Every decision occupies production, consumes Political Power and the relevant physical resources, and sets a single in-progress lock.
4. Completion rechecks every mutable fact. Release, exile, charter, and concession must still satisfy their legal or causal contract. Coercive actions recalculate both strength scores immediately before resolution.
5. A valid result is recorded once, the mission and persistent exile target are cleared, and the outcome report is fired. If a route has become invalid, no land or custody changes; event `.32` reopens the board for another explicit choice.
6. If the deadline expires, event `.30` executes the response selected during Evolution IV against the same current-state checks. The timer does not introduce a random alternative.

## Visible actions and costs

| Decision | Time | Concrete burden | Governing risk |
|---|---:|---|---|
| Release Doctor Kruger | 21 days | 25 Political Power, light production disruption, stability | Only a low-dependence, low-autonomy, small-site Directorate can leave cleanly |
| Arrange Exile | 30 days | 40 Political Power, 10 convoys, 5 trains, 100 Support Equipment, stability | Recipient and transfer validity are rechecked atomically |
| Arrest Doctor Kruger | 30 days | 55 Political Power, 400 Support Equipment, 1,500 Infantry Equipment, 12,000 manpower, 15 Army Experience, stability | Government and Kruger strength scores decide custody, defection, uprising, or crisis |
| Shut Down the Directorate | 45 days | 65 Political Power, 300 Support Equipment, 150 trucks, 10 trains, 1,000 fuel, stability | Strong independent production and dangerous projects can resist demolition |
| Ratify the Sovereign Charter | 45 days | 75 Political Power, 20 convoys, 15 trains, 250 trucks, 300 Support Equipment, stability | The laboratory territory and former-host viability must both pass revalidation |
| Launch the Military Seizure | 21 days | 85 Political Power, 700 Support Equipment, 3,000 Infantry Equipment, 300 trucks, 2,500 fuel, 25,000 manpower, 30 Army Experience, stability | The largest government bonus, but high autonomy and weaponized projects can still defeat it |
| Request Allied Containment | 30 days | 65 Political Power, faction membership, 25 convoys, 350 Support Equipment, 20 Command Power, stability | Faction support strengthens containment while foreign contacts create a defection route |
| Concede Institutional Authority | 30 days | 50 Political Power, 200 Support Equipment, 10 trains, stability | Available only when the Directorate already controls the host's institutions |

The costs are centralized in `common/script_constants/016_brilliant_scientist_containment_constants.txt`. The decision descriptions deliberately describe present facts and consequences rather than expose the numeric hidden scores.

## Causal resolution

The government score derives from Mandate, low Dependence, low Independent Capacity, independently replicated scientific families, public or military oversight, state security, military guards, hardened facilities, foreign or faction backing, and the chosen coercive preparation.

Kruger's score derives from Independent Capacity, Dependence, Grievance, the number of actual facility states, deployed and weaponized project families, private guards, sovereign authority, compromised government control, dangerous incidents, failed assassination attempts, and a multi-site network.

The score margin has four useful regions:

- decisive government control permits confinement or shutdown;
- a smaller government edge can still succeed after bounded resistance;
- sufficient Kruger strength plus a viable enclave creates a laboratory uprising;
- decisive Kruger strength plus a viable broader plan creates the Kruger State, while proven institutional capture can transform the host without secession.

When Kruger can resist but no viable country territory exists, the result is a noncountry laboratory crisis. This is its own specified outcome and does not transfer arbitrary land.

## Persistent history and cleanup

The host records the selected action, action date, outcome, outcome date, and an irreversible `ever_*` flag for the exact result. Project learning already reproduced by national institutions remains available to aftermath consumers. Personal project history remains on `KRG_warren_kruger`. Active Directorate facility markers become former-site markers on nonsovereign departure, preserving later theft, cleanup, and aftermath hooks.

The same Kruger token is transferred through the existing guarded transaction. It cannot be recruited twice, cannot move into an invalid recipient, cannot transfer while assigned to an active special project, and does not replay the original appointment reward.

## Assets and wiring

- Report sprite: `GFX_report_event_016_brilliant_scientist_sovereignty_confrontation`
- Runtime DDS: `gfx/event_pictures/016_brilliant_scientist/report_event_016_brilliant_scientist_sovereignty_confrontation.dds`
- Sprite registration: `interface/016_brilliant_scientist.gfx`
- Events: `events/016_brilliant_scientist_containment_events.txt`
- Decisions: `common/decisions/016_brilliant_scientist_containment_decisions.txt`
- Localisation: `localisation/english/016_brilliant_scientist_containment_l_english.yml`

Decision icons currently use registered vanilla political-discourse, operation, oppression, industry, and civil-war preparation sprites. Dedicated project and Kruger State art is tracked in the Event 016 asset manifest and is not substituted by an unregistered sprite.

## Future extensions

- Foreign governments that materially funded containment can receive post-settlement reparations or laboratory-access negotiations.
- Former laboratory sites can develop cleanup, black-market, or restoration decisions based on their exact project-family history.
- A peaceful charter can gain bilateral border commissions distinct from the hostile former-host crisis route.
- A noncountry laboratory crisis can expose regional intelligence operations without granting a country until a later viable territorial seizure occurs.
