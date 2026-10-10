# 007 Fury spec, part 1: core event

## Event identity

| Field | Value |
| --- | --- |
| Event ID | `7` |
| Event name | Fury |
| Replaces | obsolete `expansionism` event |
| Type | Minor repeatable |
| Status target | Reworked |
| Cluster | Wars |
| Player selection | Player countries are excluded from becoming Fury |
| Baseline target safety | Player countries are valid Fury targets when they meet the normal target gates; player countries are excluded only from Fury actor selection |
| Triggerable scenario | `The World in Fury`, see separate scenario spec |
| Main fantasy | A tiny state starts moving faster than the map can explain |

Fury is a repeatable war pressure event where one small AI country becomes an expansion actor.
It receives a special idea, a shared Fury focus tree, a decision system, an initial army package, a finite hidden reinforcement reserve, and a target-selection loop.
It declares war on a weaker eligible neighbor without warning.
After the first neighbor falls, it chooses another weaker neighbor.
This loop continues until it has no valid land neighbors left, it becomes contained, or it capitulates.

Fury should be readable as a strange war event, not as a normal focus-tree claim branch.
The selected country is still the same country on the map.
Its name and flag can remain familiar at first, but its behavior changes visibly through national spirits, decisions, focus tree content, news, and later faction identity.

## Player-facing promise

The first player-facing impression should be simple.

A small country suddenly mobilises columns it could not ordinarily sustain and begins attacking its neighbours.
One immediate opening World News announces each successful ordinary or manual preparation batch, using the first new actor and the frozen count of actors actually created.
The first genuine territorial gain has its own campaign-once conquest news.
Nearby defenders learn the danger through these two distinct moments, mobilisation and captured foreign ground.

The event should create tension without giving the player a free expansion tool.
Fury must never select the player as the Fury actor.
The ordinary Fury loop can declare on a player country when that country is a valid target; the player exclusion applies to Fury actor selection, not Fury target selection.

## Campaign role

Fury gives an existing AI country a persistent expansion identity through its army, finite reserve, occupation work, focus tree, decisions, and later faction role.
Its first wars should be locally credible, while accumulated conquest can make it a continental problem.
Familiar country names and flags keep that transformation legible.
The player responds through defence, containment, diplomacy, and the manual challenge rather than receiving Fury's opening package.

## Baseline event loop

The baseline loop has seven steps.

1. Select an eligible AI minor with a mainland capital, few states, and at least one weaker eligible land neighbor.
2. Apply the Fury package.
3. Give a starting army package and first stockpile support.
4. Start finite weekly Fury reinforcement from a hidden reserve pool.
5. Pick one weaker eligible neighbor and declare war without warning.
6. Record the campaign-once news after the first genuine territorial gain. When the current neighbour is defeated, run its eligible conquest settlement.
7. Pick the next weaker neighbor, or enter the no-neighbor branch if no valid target remains.

The loop repeats until one of these end states occurs.

| End state | Result |
| --- | --- |
| Fury capitulates | Remove Fury growth, record defeat, keep aftermath flags for achievements |
| Fury has no valid neighbor | Unlock the end-of-continent branch and possible world-end branch |
| Fury becomes major | Fire the major-Fury super-event and raise world threat state |
| Fury overextension wins | Extreme occupation pressure pauses target selection and starts the occupation crisis mission so neighbours can recover; internal collapse remains a proposal |
| World-end branch begins | Fury spreads to other continents and forms or leads the main Fury faction |

## Selection design

The candidate must be a dynamic minor, not a hardcoded country.

### Required candidate traits

A candidate should normally meet all of these conditions.

| Trait | Design requirement |
| --- | --- |
| AI control | Must not be controlled by a human player |
| Minor status | Must not be a major at selection |
| Few states | Keep Fury focused on minor countries and weight smaller candidates higher during ordinary actor selection |
| Mainland presence | Capital must have a land route or direct land neighbor candidate. Pure island states are excluded |
| Alive and sovereign | Must exist, must not be capitulated, must not be a subject unless the scenario type explicitly allows subject breakage |
| Normal country | Exclude special chaos countries that should not behave like normal states |
| Valid target | Must have at least one eligible neighbor. Player-controlled countries can count as targets, but cannot become Fury actors. |
| No fresh cooldown | Must not have recently been Fury, defeated Fury, or blocked by a local Fury cooldown |
| Focus suitability | Prefer countries with generic or light trees so the shared Fury tree can be loaded cleanly |

### Candidate randomness

Ordinary Fury actor selection should use one eligible pool and choose a weighted random country from it.
Every safe eligible minor should remain possible, but the lottery should favor one-state and two-state countries, weak industry, low fielded armies, low manpower, and several valid neighboring targets.
Stronger eligible minors should keep a base chance while losing relative weight for more states, more factories, and larger armies.

Do not broaden into player countries.
Do not use islands that have no practical neighbor.
Do not select majors simply because there are no minors left.

## Target selection design

The target must be weaker in practical war strength, not only smaller on paper.
Fury should attack the country it can plausibly overwhelm after its current Fury package.

The target score should consider:

- target divisions.
- target fielded manpower.
- target military factories.
- target civilian factories.
- target war state and already stretched fronts.
- target faction backing.
- target guarantees.
- target terrain and supply.
- Fury current divisions and equipment.
- Fury momentum.
- Fury overextension.
- current evolution stage.

### Baseline target rules

Baseline Fury attacks one target at a time.

The target must be:

- AI or player-controlled when normal target gates allow it.
- not already capitulated.
- not already at war with Fury.
- a land neighbor of Fury or a directly connected strait neighbor when the event has no pure land target.
- weaker than Fury by the target score.
- not a major unless the Fury actor has already become a major or the world-end branch is active; faction backing lowers the score rather than excluding the target.
- not a subject and not in a faction with the Fury actor.

### Target preference order

Fury prefers targets in this order.

1. Small eligible neighbor with one or two states.
2. Weakened eligible neighbor already at war elsewhere.
3. Eligible neighbor that lost divisions recently.
4. Eligible neighbor that owns claims or cores near the Fury country.
5. Larger eligible neighbor only if Fury momentum is high.
6. Major or major-backed target only in late Fury state or world-end state.

The implementation should avoid targets that pull half the world into an early local war unless that is the purpose of an evolution or the world-end branch.
The implemented score (`fury_score_current_target_candidate`, tuned in the `fury_target_score` constant block) expresses this order through state count, industry, divisions, manpower, war state, faction, major status, terrain, supply, preparation, evolution, rivalry, and last-target churn; the [AI matrix](../matrices/007_fury_ai_balance_matrix.md) lists the factors.
Subjects are never valid targets, and a major is valid only once the actor is itself a major or the world-end branch is active.

## Starting Fury package

When selected, the country receives a clear opening package.

### National spirit

Working name: `National Fury`.

Role:

- attack and breakthrough bias for early wars.
- recruitable population support.
- faster mobilization.
- supply grace for first wars.
- compliance gain in conquered territory.
- stability and diplomacy penalties.
- resistance growth risk if overextended.
- AI attack confidence.
- unlocks Fury decisions and the shared tree.

The baseline idea should be strong enough that a one-state country can fight a weaker neighbor, but it should not let the country defeat a major without building momentum first.

### Starting units

The opening package creates one shared template, `Fury Column` (six infantry battalions and an engineer company), and spawns columns from it with a scaled stockpile.
The opening count is tuned in the `fury_units` script-constant block: a small opening for a candidate with fewer than two controlled states, a baseline opening, a larger Hardened opening, and the largest Evolution III opening.
Every opening also seeds the actor's hidden reserve (see below).

The earlier planning bands named Border Runner, Capital Guard, and Depot Cadre templates and Severe or High-chaos tiers.
They were not adopted: one readable template whose quality improves through focuses keeps the actor legible, and capital defence comes from the `Capital Guard` focus rather than a separate template.
Do not reintroduce extra template families without a decision that gives each one a distinct battlefield role.

### Hidden reinforcement reserve

Fury must not receive infinite free weekly divisions.
Each Fury actor receives a hidden finite reinforcement reserve pool when selected.
Weekly reinforcement consumes one unit from that pool each weekly tick.
When the pool reaches zero, weekly free spawning stops completely for that actor.
Fury can still recruit normally through the base game.
Scripted weekly reserve grants are capped at 100 total divisions per Fury actor.

The reserve pool should use script constants for:

- baseline pool size.
- weekly draw amount.
- per-evolution quality and pool-size modifiers.
- scenario intensity pool-size modifiers.
- conquest refill caps.
- evolution and scenario refill caps.
- direct focus and decision reward sizing.
- maximum 100-division reserve clamp.

No decision, focus, event, evolution, or scenario setting may create an uncapped unit loop.

Weekly reinforcement draw should stay finite rather than unlimited.
The current implementation creates one small Fury Column every weekly tick while reserve remains.
Momentum, country size, evolution state, scenario intensity, decisions, and focuses may affect direct reward waves or unit quality, but they must not directly multiply weekly free divisions.

Baseline Fury should have a small initial force and a small reserve pool.
Evolution I increases unit quality and reserve size, but remains capped.
Evolution II creates two Fury countries, so each individual reserve pool should be smaller than if only one Fury existed.
Evolution III creates three Fury countries and stronger openings, but weekly spawning remains capped.
The World in Fury scenario intensity changes initial army size and reserve pool size, not infinite spawning.

Limited extra reserves may come from evolutions, scenario setup, world-end setup, and the Depot Cadres and Depot Officers focuses, but every refill is capped by script constants and respects the lifetime clamp.
The automatic weekly draw stays fixed at one column per tick while reserve remains.
Brakes act on the one-time direct reinforcement waves instead: high and extreme occupation pressure each subtract columns from a focus or decision wave, which is clamped between one and the `fury_units.direct_spawn_max_units` ceiling.

## Fury values

Fury is AI-only, so its values are internal decision drivers for the actor and the target loop, not a player-facing meter.
No tooltip, report, or Event Details row shows their numbers.
The player reads the same situation through visible consequences: the `Fury Overextension` national spirit, the occupation crisis mission, stalled fronts, and the news and report beats.

| Internal value | Meaning | Current sources | Current consumers |
| --- | --- | --- | --- |
| `fury_momentum` | confidence and pace of expansion | starting value, a weekly gain, first conquest, Hardened Fury, paid depot and rivalry actions, terminal fronts | direct reinforcement-wave size and a target-score bonus |
| `fury_overextension` | administrative strain | conquered non-core states at settlement, a weekly gain while at war, a weekly loss at peace, coring and terminal relief | target-score penalty, the target-selection decision gate, and the seed of `fury_occupation_pressure` |
| `fury_occupation_pressure` | weekly recomputed occupation load | overextension plus non-core states, active war, and resistance, minus registered and rail-registered states and garrison capacity | the `Fury Overextension` idea, the occupation crisis, direct-wave brakes, and the target-validity block at extreme pressure |

Occupation strength is expressed through actual state compliance, garrison capacity, supplies, and the existing Compliance Drive idea.
Target preparation records work on the current legal opponent.
Cooperation and rivalry use their existing route flags, project-pact membership, and physical reserve sharing.
These mechanisms retain their distinct choices without a separate Compliance Drive, Reach, or Pact Cohesion counter.

A cooperation choice spends real resources on eligible partners and locks the rival route.
A rivalry choice locks cooperation and influences the score of a legal third-country target also pursued by a non-allied rival.
Attacks on another Fury actor wait until ordinary legal neighbours are exhausted, except in the explicit Hostile Fury challenge.

Two weaknesses in the current value model are recorded as proposals in the README's open questions: momentum rises every week regardless of success, so it behaves as a clock rather than a signal, and overextension and occupation pressure are two overlapping strain values with separate thresholds.

## Conquest settlement

Territory changes hands through the ordinary peace conference.
Fury adds a settlement layer on top of it rather than a hidden state transfer:

1. When the current target capitulates or leaves the war, the weekly tick clears the target and queues the next target selection after a short delay.
2. The first qualifying territorial gain registers every owned, controlled, non-core state, adds compliance, raises momentum, and adds overextension per registered state.
3. Later captured states enter the same register through the `Prepare an Occupied State` decision and the occupation branch.
4. Claims and cores come only through the two coring decisions after compliance and control requirements are met.
5. The settlement never transfers player-controlled or player-occupied land.

If a South American Fury actor capitulates a South American target, `fury_on_capitulation` annexes that target immediately.
This keeps regional intervention or Monroe Doctrine white-peace handling from undoing the conquest before the weekly target loop can react.
The settlement then sends `chaosx.nr7.60` to the United States when a declaration is legal, offering an annexation war on the Fury actor; the AI United States takes the war option in nearly every case.

## First-conquest news event

The first-conquest news fires once across the campaign after an actor gains foreign controlled territory above its starting footprint or completes an eligible annexation.
Starting with several states does not prove conquest.
The report describes captured foreign ground when a war is still ongoing, and names an annexation only when that settlement actually completed.

Purpose:

- make the system visible to the world.
- show that this is not an ordinary random war.
- give nearby powers a reason to prepare without revealing later routes.

Tone:

- factual and unsettled.
- newspapers focus on the speed of the fall.
- diplomats argue whether the fall was planned or improvised.
- generals treat it as a local anomaly at first.

Player-facing direction:

Title direction: identify the territorial breakthrough without treating a controlled-state gain as a completed annexation.

Description direction: name the Fury actor and the foreign territory actually taken.
Describe improvised columns, displaced defenders, and the speed of the advance.

Button direction: an uneasy practical reaction from an observer who now has a concrete reason to prepare.

The exact text belongs in localisation during implementation.

## Major-Fury super-event threshold

A super-event fires once per campaign when the first Fury actor controls more states than `fury_balance.major_super_event_state_threshold`, provided the world-end branch has not started.
The same state threshold, vanilla major status, or an active world-end branch keeps `world_threat_source_fury` active.
Earlier trigger options based on factories, divisions, or continental share were not adopted; one readable territorial threshold is enough to mark the escalation.

Purpose:

- mark the moment when the event stops being a local curiosity.
- warn that ordinary containment failed.
- unlock stronger anti-Fury and world-threat responses.
- prepare the world-end branch without revealing it too early.

This super-event is distinct from the world-end super-event.
A Fury major is a major escalation.
The world-end branch is a terminal campaign state.

## Repeatability

Fury is repeatable, but active counts should be controlled.

Baseline active count:

- one active Fury actor at a time during ordinary event fire.
- a new ordinary Fury can fire after the previous Fury is defeated, contained, or after a long cooldown if the first Fury is still local and not major.
- Evolution II raises ordinary active count to two.
- Evolution III raises ordinary active count to three.
- The triggerable scenario and world-end branch can create more than this because they are explicit setup or terminal systems.

Repeat firing should remember previous Fury countries.
A country that recently failed as Fury should not immediately be selected again unless the scenario explicitly chooses it.

## Cluster role

Fury belongs in the Wars cluster through two logical membership rows at Medium and High severity.

## Shared-system connections

Fury needs no bespoke hook for these shared systems because its wars already pass through their generic owners:

| Shared system | Current connection |
| --- | --- |
| Chaos Meter | Every Fury declaration is a new war relation counted by `chaos_meter_on_war_relation_added`; the per-attacker same-day minor-war cap keeps Evolution III all-neighbour declarations from multiplying Chaos. |
| Deaths | Fury fronts produce combat civilian deaths through the shared daily casualty pipeline, and harsh occupation laws produce the ordinary occupation deaths. |
| Migration and famine | Each hostile capture runs `humanitarian_handle_hostile_capture`, which submits bounded war-flight pressure for that state and queues one famine food-safety assessment. |
| World threat | `fury_update_world_threat_source` maintains `world_threat_source_fury` for a major-sized or terminal actor. |

Condemnation, camps, CBRN, and fallout have no natural Fury connection and none should be invented.
One optional connection, harsh coring as a migration cause, is recorded as a proposal in the README.

## Player interaction

In ordinary random play, the player mainly interacts with Fury as an observer, neighbor, or potential firefighter.
The player should not gain the Fury package.

Player-facing hooks:

- immediate opening news for each successful preparation batch.
- campaign-once news after the first genuine territorial gain.
- super-event after major threshold.
- event details entry.
- anti-Fury decisions after the major super-event or world-end branch, for countries bordering a Fury actor and for majors.
- possible achievements for containing Fury.
- possible triggerable challenge scenario.

Anti-Fury decisions should be limited.
The event is minor repeatable at baseline, so ordinary countries should not gain a large permanent system every time Fury appears.
Strong anti-Fury content belongs after major-Fury or world-end thresholds.
