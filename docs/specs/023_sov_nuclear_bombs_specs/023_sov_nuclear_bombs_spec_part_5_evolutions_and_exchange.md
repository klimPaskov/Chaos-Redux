# Event 023 specification, Part 5: Evolutions and nuclear exchange

## Evolution structure

Event 23 has one true evolution track with four logged stages.

Working track name: `nuclear_escalation`.

Baseline command, production, testing, and posture changes are ordinary event progression. They should not create evolution log rows. Only the four chaos-gated escalations below count as Event 23 evolutions.

Each evolution has two entry modes:

- Pre-fire opening mode, used when Event 23 first fires at a world state that already qualifies for the evolution.
- Active escalation mode, used when Event 23 has already fired and the campaign later reaches the required conditions.

Pre-fire mode applies the stronger opening package immediately and records every evolution stage already reached in the correct order. Active mode uses dynamic pacing and gives the incremental package for that stage.

## Arsenal reinforcement ladder

The following values are tuning anchors for the specification.

| Stage reached | Cumulative opening bomb grant | Increment after a baseline opening | Cumulative free reactor grant |
| --- | ---: | ---: | ---: |
| Baseline | 100 | 100 | 0 |
| Evolution I | 175 | 75 | 2 |
| Evolution II | 275 | 100 | 4 |
| Evolution III | 400 | 125 | 6 |
| Evolution IV | 600 | 200 | 8 |

The opening grant is additive to the Soviet stockpile. It does not overwrite existing bombs.

Incremental evolution grants should reconcile with the same ladder. A campaign that opens at baseline and later reaches all four evolutions receives the same total event-owned bomb and reactor package as a campaign where Event 23 first fires at Evolution IV.

Reactor placement is bounded by valid Soviet-owned and Soviet-controlled states. A failed placement does not convert into free factories or another reward. Unplaceable reactor grants remain a queued construction entitlement until valid sites exist or the event-owned cap is reduced through dismantlement.

## Evolution I: The wider nuclear race

### Chaos access

Evolution I requires at least 400 Chaos, the Rising Chaos tier.

### Design role

The Soviet breakthrough stops being a single hidden arsenal and becomes an international race. Foreign majors begin to treat nuclear capability as a strategic requirement. Soviet production shifts from one completed arsenal to a repeatable state program.

### Active pacing

Recommended base mean time to happen: 120 days after the Chaos gate is reached.

Faster factors include:

- Public Soviet test.
- Foreign private confirmation.
- Existing non-Soviet nuclear capability.
- High global tension.
- Soviet reactor construction.
- Event 76 later being implemented and entering a compatible preparation state.

Slower factors include:

- The arsenal remains Unknown.
- Atomic Moratorium is active.
- Low Soviet Readiness.
- Severe reactor or test accidents.
- No other major has a realistic research base.

### Soviet package

- Increase the event-owned cumulative grant to 175 bombs.
- Add or queue two reactors.
- Unlock sustained fissile production and larger assembly batches.
- Unlock public demonstration and foreign observer choices.
- Unlock stronger counterintelligence and site-hardening decisions.
- Enable neutral arms-race hooks for Event 32 and Event 76.
- Add the first evolution log entry with Soviet actor context.

### Foreign package

- Valid majors can receive strategic planning reports.
- Research and production AI may increase nuclear, bomber, air-defense, shelter, dispersion, or missile priority according to actual capabilities.
- No draft event is forced to fire.
- No country receives free nuclear technology solely because the evolution exists.

### Failure and restraint

The Soviet Union may answer the race with a moratorium, controlled observation, or continued secrecy. Refusing to expand should remain a valid choice, but it leaves the Soviet stockpile more vulnerable to a later race.

## Evolution II: Coercive doctrine

### Chaos access

Evolution II requires at least 600 Chaos, the Chaos tier.

### Design role

The arsenal becomes an active instrument of political pressure. The Soviet Union can threaten valid minors and breakaways outside an ordinary wartime warning. Coercion, credibility, foreign guarantees, and target counterplay become central.

### Active pacing

Recommended base mean time to happen: 120 days after the Chaos gate and Evolution I.

Faster factors include:

- An active Soviet war.
- Soviet Collapse or a breakaway holding registered devices.
- A Soviet core or nuclear facility under foreign control.
- Demonstrated arsenal.
- High Readiness.
- A recent Soviet conventional defeat.
- A successful prior public test.

Slower factors include:

- Atomic Moratorium.
- Low Integrity.
- Repeated failed threats.
- Strong international sanctions.
- No valid minor, breakaway, or wartime target.

### Soviet package

- Increase the event-owned cumulative grant to 275 bombs.
- Increase cumulative free reactors to four.
- Unlock Coercive Doctrine posture.
- Unlock direct ultimata against valid minors and Soviet breakaways.
- Unlock selected-target management and response missions.
- Unlock limited strike preparation against military and logistics profiles.
- Unlock credibility memory and stronger foreign guarantee reactions.
- Add the second evolution log entry.

### AI boundary

Soviet AI can begin bounded coercion. It may use a limited weapon against a nonnuclear enemy or breakaway only under the strict gates in Part 4 and Part 9. It cannot start a nuclear war with a nuclear major at this stage.

### Target protection

Evolution II must not convert every independent minor into a free subject. Target acceptance depends on the demand, Soviet conventional position, delivery credibility, foreign backing, target government, and prior Soviet behavior.

## Evolution III: Nuclear war becomes possible

### Chaos access

Evolution III requires at least 800 Chaos, the Totalen Chaos tier.

### Additional world-state gate

At least one of the following must hold:

- Two or more majors possess verified operational nuclear capability.
- The Soviet Union has suffered a confirmed nuclear strike.
- A nuclear major is at war with the Soviet Union and has a credible prepared strike.
- A prior Event 23 limited use has caused another major to enter an active retaliation state.

The evolution should remain pending when the world has only one operational nuclear power and no credible exchange opponent.

### Design role

Nuclear use can now become a multi-major conflict. Retaliation planning, survivable command, target deconfliction, reciprocal pauses, and exchange control become available.

### Active pacing

Recommended base mean time to happen: 180 days after the Chaos gate, Evolution II, and a valid world-state gate.

Faster factors include:

- Confirmed enemy nuclear use.
- Active major war.
- Capital threat.
- Multiple public nuclear powers.
- Repeated failed coercive crises.
- High global contamination.
- Low diplomatic contact.

Slower factors include:

- Active hotline or stand-down.
- Atomic Moratorium.
- Stable peace among nuclear majors.
- High Command Integrity with a scientific safety veto.
- Successful arms-control conference.

### Soviet package

- Increase the event-owned cumulative grant to 400 bombs.
- Increase cumulative free reactors to six.
- Unlock Retaliatory Release posture.
- Unlock major-target planning.
- Unlock reciprocal warning, hotline, limited retaliation, reserve preservation, and exchange stand-down actions.
- Unlock the first multi-major exchange super-event trigger.
- Add the third evolution log entry.

### AI boundary

Soviet AI may retaliate against a nuclear major after confirmed enemy nuclear use. It may prepare counterforce targets during an active nuclear crisis. It does not deliberately make the first major-to-major nuclear strike below 1000 Chaos.

A player may initiate the conflict after explicit confirmation, subject to all current target, delivery, and shared consequence gates.

## Evolution IV: Unrestrained release

### Chaos access

Evolution IV requires at least 1000 Chaos, the World Collapse tier.

### Additional world-state gate

At least two operational nuclear majors must exist or an active multi-major exchange must already be underway.

### Design role

AI first use against another nuclear major becomes possible. The world is already unstable enough that a government facing destruction may decide that waiting is more dangerous than striking.

### Active pacing

Recommended base mean time to happen: 90 days after the Chaos gate, Evolution III, and the additional world-state gate.

The stage can be recorded immediately when Event 23 first fires at 1000 or more Chaos and the world-state gate is already true.

Faster factors include:

- Soviet capital under direct threat.
- Soviet capitulation progress above the severe-loss threshold.
- Confirmed enemy launch preparation.
- Recent enemy nuclear use.
- Broken conventional fronts and severe command pressure.
- Enemy nuclear superiority.
- No working hotline or settlement channel.

Slower factors include:

- High Integrity and a strict custody doctrine.
- A valid reciprocal stand-down.
- Enemy nuclear forces are not at war with the Soviet Union.
- The Soviet Union is conventionally winning.
- No valid exact strategic target exists.
- Atomic Moratorium remains intact.

### Soviet package

- Increase the event-owned cumulative grant to 600 bombs.
- Increase cumulative free reactors to eight.
- Unlock Unrestrained Release posture.
- Unlock full first-use planning for the player.
- Permit Soviet AI major first use under the hard gates below.
- Unlock the widest exchange targeting profiles.
- Add the fourth evolution log entry.

## Soviet AI major first-use gate

Every condition below is required before Soviet AI may deliberately strike a nuclear major first:

- Evolution IV is active.
- Chaos is at least 1000.
- The Soviet Union is at war with the target.
- The target has verified operational nuclear capability or a credible prepared nuclear strike.
- The Soviet Union is suffering severe strategic loss, such as high capitulation progress, imminent capital loss, a broken major front, or a verified enemy launch preparation.
- Readiness meets the selected strike profile's high floor.
- Integrity is above the minimum needed for a valid central order, or a separately validated retaliation delegation exists.
- A lower-consequence military or logistics target exists, unless the target has already used nuclear weapons against populated Soviet territory.
- No active reciprocal stand-down, accepted settlement, or valid hotline pause exists.
- No duplicate launch or unresolved authorization is active.
- The probability audit confirms that first use remains rare in the qualifying scenario.

High Chaos, high stockpile, ideological hostility, or a large target score cannot replace these gates.

## Exchange crisis state

A multi-major exchange crisis begins when:

- A nuclear major uses a weapon against another nuclear major.
- A verified launch is detected and the target enters a retaliation window.
- A player authorizes first use against a nuclear major at Evolution III or IV.
- Soviet AI passes the Evolution IV first-use gate.

The crisis state records:

- Participating nuclear majors.
- The initiating actor.
- Confirmed strikes and attempted strikes.
- Current retaliation windows.
- Active stand-down proposals.
- Public exchange stage.
- Whether the first multi-major exchange super-event has fired.
- Whether the shared Fallout world-end route has become eligible or active.

The crisis is a consequence state, not a new world-end scenario.

## Exchange stages

### Nuclear confrontation

- At least two nuclear majors are in an active crisis.
- No confirmed cross-major detonation has occurred yet.
- Warnings, hotline actions, dispersal, interception, and stand-down remain available.

### Limited exchange

- One or a small number of strikes have occurred between nuclear majors.
- Retaliation is prepared, but broad target packages are not yet executing.
- The dedicated super-event fires at the first confirmed multi-major exchange.
- Third parties receive emergency diplomacy and protection reactions.

### Expanding exchange

- Multiple majors or multiple target profiles are involved.
- Retaliation windows shorten.
- Readiness rises through dispersal while Integrity can fall through delegation and damage.
- Military and logistics profiles remain available as off-ramps from broader countervalue use.

### General exchange

- Broad major target packages are active.
- AI willingness to continue rises only after confirmed enemy use, severe losses, or command decapitation.
- Shared contamination, deaths, condemnation, and Fallout readiness dominate the campaign.
- This stage still does not set `world_end` by itself.

## Exchange actions

### Establish an emergency hotline

- Requires a valid opposing nuclear major.
- Uses diplomatic access, communications, or a neutral intermediary.
- Extends decision time and can reveal false warnings.
- Does not force peace.
- AI prefers it when neither side has suffered a confirmed nuclear strike and both retain command.

### Propose a reciprocal stand-down

- Both sides pause new authorizations for a fixed period.
- Existing launched weapons or completed shared strikes are not reversed.
- Violating the stand-down damages credibility and makes later acceptance much less likely.

### Limit retaliation

- Restricts the next response to a military or logistics profile.
- Preserves the ability to retaliate while reducing immediate escalation.
- Requires sufficient command control to enforce the restriction.

### Preserve the reserve

- Moves part of the arsenal away from immediate launch status.
- Lowers rapid retaliation capacity.
- Protects against losing every device in a first strike.
- Can raise Integrity through tighter accounting.

### Delegate retaliation authority

- Improves survivability after command decapitation.
- Raises unauthorized use and disputed-order risk.
- Should be one of the sharpest Readiness versus Integrity tradeoffs.

### Suspend release orders

- Freezes new Event 23 authorizations while diplomatic talks continue.
- Does not remove enemy preparations or shared contamination.
- A player can restore release after a delay if talks fail.

### Enter Atomic Moratorium

- Ends ordinary Event 23 targeting and exchange planning.
- Requires accounting for reserved weapons and active missions.
- Can become bilateral or multilateral through later shared content.

## Retaliation timing

Retaliation must give enough time for command decisions without making response meaningless.

Recommended windows:

- Confirmed enemy strike with intact command: 3 to 14 days.
- Suspected launch or false-warning state: 7 to 21 days.
- Command damage or disputed order: 14 to 30 days while authentication is restored.

The implementation should use the current delivery system's real timing where it is stricter. It should never create an instant AI retaliation on the same tick before shared consequences, target validity, and authorization state are recorded.

## False warnings and ambiguous detection

A rare high-chaos incident can report a possible enemy launch without confirmed detonation.

The Soviet player may:

- Wait for confirmation.
- Disperse and raise Readiness.
- Contact the suspected actor.
- Prepare a response without final authorization.
- Launch immediately only at Evolution IV and with explicit confirmation.

AI should almost always seek confirmation unless command is already damaged, enemy launch preparation is verified, and the Evolution IV first-use gate is otherwise satisfied.

A false-warning incident should create pressure and possible costly mobilization. It should not randomly launch a nuclear war through an unbounded chance.

## Super-event threshold

The dedicated Event 23 super-event fires once when a confirmed nuclear detonation by one major is answered by, or occurs during an active exchange with, another major.

The threshold requires a real multi-major exchange. The following do not qualify by themselves:

- A Soviet test.
- A strike against a nonnuclear minor.
- A single major striking a nonmajor.
- A failed launch.
- A public ultimatum.
- A storage accident.

The super-event is nonterminal. It records the shift from nuclear monopoly or limited use to an exchange among major powers. It does not set `world_end` and does not replace the shared Fallout presentation.

## Shared Fallout relationship

Every strike continues to feed shared contamination, Air Cleanliness, deaths, condemnation, and Chaos.

If shared contamination reaches the Fallout terminal threshold and the shared Fallout route passes its own gates, Fallout owns the world-end transition. Event 23 should stop incompatible targeting and exchange actions after the shared terminal state begins.

Event 23 must not create a second Fallout branch, a duplicate Event Details row, or a private shortcut around the shared 100 percent contamination requirement.

## Evolution disable behavior

Each evolution can be disabled through the shared evolution controls.

- Disabling Evolution I leaves the baseline arsenal playable with limited production and testing.
- Disabling Evolution II removes peacetime coercion and minor or breakaway ultimata, while preserving wartime warning and baseline use.
- Disabling Evolution III removes the Event 23 major-exchange expansion, while shared nuclear systems may still process nuclear use from other sources.
- Disabling Evolution IV preserves retaliation and player-controlled Evolution III access but blocks Event 23 AI major first use.

Disabled stages must not set recorded flags, grant bombs or reactors, unlock posture, or block clean baseline progression.

## Writing direction

Evolution text should describe changes in actual behavior: reactor compounds expanding, foreign bomber patrols, dispersed command, armed delivery crews, breakaway depots, shortened response time, and the first confirmed exchange.

Avoid generic claims that the world has entered a new age. The player should understand escalation through visible preparations, decisions, targets, evacuations, and consequences.
