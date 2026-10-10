# Event 030 Time Traveler Specification Part 3: Consultations and the International Intelligence War

Acceptance status: proposed design, disposition `unresolved`.

## Decision presentation

The custodian receives one main decision category with a static category picture and the compact three-value header from Part 2.
The category shows three to five actions in the current phase and never more than six.
Only one consultation mission is active at a time.
At most two defensive or crisis missions may coexist with it when foreign pressure is high.

Rivals act through one selected-target category that lists only the interested countries and only the operations their network can attempt.
No separate mechanic window is required.

## Consultation cycle

A consultation is a government commitment.
The player chooses a family, pays a cost, receives a concrete forecast, and gets a timed objective.
Completing the objective proves the government acted on the advice and grants the main reward.

Consultations share a cooldown of about 90 days.
The profile shortens the cooldown for its strongest families.
Indispensable Credibility unlocks the advanced variant of each family.
The Divergence band sets the forecast's precision.

A single action spends at most four cost types.
Costs scale from country capacity through script constants and use texticons.

## Consultation families

### Military forecast

The traveler identifies one operational risk or opportunity tied to a current enemy, border, front, sea region, air region, capital approach, or supply corridor.
Objectives include holding named states, placing supplied divisions in named states, protecting a named railway or supply hub, moving a fleet to a threatened sea region, gaining air superiority in a named region, or delaying a predicted losing offensive.
Costs may use army experience, command power, support equipment, fuel, or tied-down divisions.
Success gives a planning window, a revealed enemy weakness, or one doctrine result through Event 027 (Part 10).
Failure never deletes armies or forces a war.

### Industrial bottleneck

The traveler identifies a production, transport, resource, or construction failure the remembered government handled badly.
Objectives include repairing a named rail link, expanding a supply hub, port, or infrastructure line, shifting a production line before a predicted shortage, holding a stockpile of trucks, trains, convoys, or fuel to a deadline, or protecting a named industrial state.
Success gives a visible map improvement, retained production efficiency, or a spirit upgrade, never a generic construction-speed purchase.

### Scientific shortcut

The traveler explains which line of inquiry succeeds and which wastes years.
Objectives include starting or completing a valid technology in a named category, dedicating a special project slot, securing a research state, or choosing between a fast unstable prototype and a slow reliable program.
Rewards use research bonuses, special project progress, or the Event 016 custom technology API when an approved package exists.
No consultation grants an unrestricted ahead-of-time technology.

### Diplomatic forecast

The traveler identifies a likely betrayal, coalition failure, negotiation opening, or guarantee problem in live relations.
Objectives include reaching a relation threshold, negotiating access or a non-aggression arrangement, keeping a vulnerable ally in a faction, securing convoy access before a crisis, or exposing a rival offer.
Success changes a real relationship or unlocks a follow-up decision, never only an opinion modifier.

#### Remembered war variants

The legacy event's premise, a traveler who warns a government away from a war history says it will lose, survives as country-specific diplomatic forecasts.
They appear when the custodian is the named country or when the custodian shares that forecast with it.

| Country | Remembered war | Forecast offer |
| --- | --- | --- |
| Germany | the war against the Soviet Union | propose a Berlin-Moscow pact, which the Soviet Union may accept or refuse, with the faction, threat, and opinion consequences of the legacy chain |
| United States | the Pacific war against Japan | act on Japanese war plans, gaining intelligence on Japan and a Pacific defense objective |

These variants reuse the implemented legacy behavior as reference content and replace its unconditional firing and its player-facing wording.
Further countries can receive variants only through researched content.

### Counterintelligence map

The traveler describes an infiltration method, a future intelligence failure, or a compromised official.
Objectives include protecting the arrival site or records office, identifying one interested country, or turning a foreign operative through the existing agency systems.
Success exposes one foreign network, lowers Exposure, or makes the next counterintelligence sting cheaper.

### Domestic threat assessment

The traveler identifies a coup network, extremist movement, secession risk, assassination plot, or institutional fracture supported by current country state.
The player chooses a lawful, political, or coercive response, with an objective such as securing named states, changing an advisor or law, holding stability to a deadline, or settling a faction dispute.
Coercive success protects the government but can raise condemnation when abuses become public.
The consultation is never a free purge.

## What a consultation proves

Before payment, each offer names the recipient government, the objective, the deadline, the reward family, and whether its knowledge has already spread beyond the traveler.
The objective must be observable through the relevant owner system.
A forecast cannot force its crisis to occur merely to prove the traveler right.

The player's intervention can prevent the remembered result.
Holding the named corridor proves the defensive work even when the predicted offensive never comes.
The deadline alone provides no success, and a prediction's non-occurrence alone provides no failure.
An actor or state that becomes invalid returns through the cancellation path without fabricating a new target or keeping the payment.

If already distributed knowledge lets a mission continue after custody changes, the result belongs to the government that committed it.
The new custodian cannot collect the same completed advice again.

## Consultation results

| Result | Meaning | Effect |
| --- | --- | --- |
| Success | the objective was met | full reward and Credibility gain, with a precision bonus in a Recognizable timeline |
| Partial | part of the objective was met | reduced reward and a follow-up choice |
| Failed | the objective was missed | the tooltip names the cause: a recorded timeline change costs little Credibility, a planted forgery opens an investigation, and an ignored objective costs the most |

Forgery is the cause only when a recorded forged-advice operation exists.

## Foreign interest registry

The event keeps a sparse registry of interested countries, capped by the Exposure band in Part 2.
It prefers existing majors, player countries, countries with strong intelligence agencies, enemies and strategic rivals of the custodian, close allies seeking access, and countries linked to a returned figure or visitor.
The registry is rebuilt only after public revelation, custody transfer, a new evolution, or a country becoming invalid, never through a recurring world scan.

## Foreign operations

Each interested country holds a hidden network level against the program.
Operations raise it, the host's countermeasures lower it, and it never appears as a number.

### Infiltrate the program

The default operation for rivals and curious allies.
Success advances the network one step.
The first step yields schedules and staff names, the second recruits a staff member and grants a Future Fragment, and the third steals the archive and copies one completed consultation specialty.
The custodian learns of a compromised staff member and can dismiss, turn, or watch them.
Theft never recreates direct access.

### Plant forged advice

Available from the Suspected band to hostile countries with an established network.
The forgery names a plausible decision and creates a testable consequence.
If the custodian exposes it, the attacker's network collapses and Credibility rises.
If the custodian acts on it, the attacker gains a strategic benefit and the custodian suffers a concrete setback.

### Offer asylum

Available from the Suspected band.
The traveler weighs the arrangement, their treatment, ideological fit, host stability, the offering country's credibility, and safe travel.
A trusted traveler under a respectful arrangement rarely defects, while a confined one defects far more easily.

### Seize the traveler

Available only in the Public band, with a mature network and a viable route.
The sponsor chooses abduction or, only when it sees the traveler as an existential threat and has no acquisition route, assassination.
Outcomes include failure, capture of a double, a wounded traveler, a successful transfer, an exposed sponsor, or disappearance before either side arrives.
A successful assassination ends the original traveler but leaves copied knowledge and the temporal disturbance.

## Host countermeasures

### Relocate the traveler

Moves the traveler to another valid secure state.
It interrupts consultations, costs transport and security capacity, and lowers Exposure if the route stays secret.
It cannot repeat while a consultation or operation is active.

### Assign a guard detail

Commits command power, support equipment, manpower, and optionally divisions near the site.
It sharply reduces seizure success but raises Exposure because more people know the secret.

### Run a counterintelligence sting

Runs decoy meetings and false schedules against one interested country.
Success lowers that country's network and can capture its cell or lure it into seizing a double.
The sting event can escalate into using the traveler as bait, which exposes several networks on success and risks injury, abduction, or scandal on failure.

### Share a forecast with an ally

Gives one ally one verified forecast or completed consultation result.
The ally gains a Future Fragment and, where one exists, its remembered war variant.
Sharing lowers that ally's theft pressure, improves coordination, and raises Timeline Divergence.
The ally never gains custody.

## The double

A captured double is a prepared decoy who survives initial questioning.
The captor receives a short investigation chain to expose the deception, trade the double, publish a false claim, or mistakenly build policy around fabricated knowledge.
The double never becomes a second traveler and never grants consultations.

## Custody transfer

A successful transfer moves the character, the main category, the arrangement review, the individual-crisis slot, and the Exposure state to the new custodian.
Credibility is recalculated from available evidence and the transfer method.
The old custodian keeps its legacy stage, completed records, and a grievance against the captor where appropriate.
Missions that require the traveler close cleanly, and missions whose knowledge already spread may continue.

## Multiplayer

Only one country holds the original traveler.
Every valid player country can be an interested country and uses the same operations as AI rivals.
The custodian does not see an operation's sponsor until evidence exposes it.
A human custodian receives the category immediately, and a human former custodian keeps its legacy and recovery options.
No player receives a ghost copy of the traveler.

## Baseline AI

The custodian AI chooses an arrangement from war state, stability, intelligence capacity, research capacity, ideology, and leader security.
Foreign AI chooses infiltration, forgery, asylum, seizure, or restraint from relations, intelligence capacity, ideology, proximity, threat, and whether it already holds a Future Fragment.
It never repeats a low-chance seizure attempt.
Part 10 owns the probability scenarios.
