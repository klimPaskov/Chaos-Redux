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

Fury is a repeatable war pressure event where one small AI country becomes an expansion actor. It receives a special idea, a shared Fury focus tree, a decision system, an initial army package, a finite hidden reinforcement reserve, and a target-selection loop. It declares war on a weaker eligible neighbor without warning. After the first neighbor falls, it chooses another weaker neighbor. This loop continues until it has no valid land neighbors left, it becomes contained, or it capitulates.

Fury should be readable as a strange war event, not as a normal focus-tree claim branch. The selected country is still the same country on the map. Its name and flag can remain familiar at first, but its behavior changes visibly through national spirits, decisions, focus tree content, news, and later faction identity.

## Player-facing promise

The first player-facing impression should be simple.

A minor country that should not matter starts winning wars too quickly. Observers cannot agree whether it is a coup, a mass mobilization, a staff-office obsession, or a country losing all sense of limit. The player sees the first warning through a report event or news note only after the first conquest, unless the player is close to the region or has intelligence access.

The event should create tension without giving the player a free expansion tool. Fury must never select the player as the Fury actor. The ordinary Fury loop can declare on a player country when that country is a valid target; the player exclusion applies to Fury actor selection, not Fury target selection.

## What Fury is not

Fury is not a generic random war.

A random war picks an attacker and a defender. Fury creates an actor with memory, growth, occupation tools, coring pressure, capped military reinforcement, a focus tree, and evolving behavior. The country becomes a campaign problem until it is stopped or until it runs out of nearby targets.

Fury is not a formable country by default.

The selected state does not become a new hardcoded tag. It becomes a Fury actor through flags, ideas, decisions, and a shared focus tree. This preserves the dynamic nature of the event and allows Luxembourg, Uruguay, or any similar country to be valid examples rather than hardcoded cases.

Fury is not a player reward.

The player can fight Fury, contain Fury, manipulate Fury indirectly, or trigger the custom challenge scenario. The player does not receive the Fury package, finite reinforcement reserve, or the Fury focus tree from ordinary random play.

## Baseline event loop

The baseline loop has seven steps.

1. Select an eligible AI minor with a mainland capital, few states, and at least one weaker eligible land neighbor.
2. Apply the Fury package.
3. Give a starting army package and first stockpile support.
4. Start finite weekly Fury reinforcement from a hidden reserve pool.
5. Pick one weaker eligible neighbor and declare war without warning.
6. When that neighbor is defeated, run conquest settlement and fire the first-conquest news if this is the first victory.
7. Pick the next weaker neighbor, or enter the no-neighbor branch if no valid target remains.

The loop repeats until one of these end states occurs.

| End state | Result |
| --- | --- |
| Fury capitulates | Remove Fury growth, record defeat, keep aftermath flags for achievements |
| Fury has no valid neighbor | Unlock the end-of-continent branch and possible world-end branch |
| Fury becomes major | Fire the major-Fury super-event and raise world threat state |
| Fury overextension wins | Pause target selection, create internal collapse risk, and allow neighbors to recover |
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

Ordinary Fury actor selection should use one eligible pool and choose a weighted random country from it. Every safe eligible minor should remain possible, but the lottery should favor one-state and two-state countries, weak industry, low fielded armies, low manpower, and several valid neighboring targets. Stronger eligible minors should keep a base chance while losing relative weight for more states, more factories, and larger armies.

Do not broaden into player countries. Do not use islands that have no practical neighbor. Do not select majors simply because there are no minors left.

## Target selection design

The target must be weaker in practical war strength, not only smaller on paper. Fury should attack the country it can plausibly overwhelm after its current Fury package.

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
- not protected by a major faction unless the Fury actor has already become a major or the campaign is in a higher evolution.

### Target preference order

Fury prefers targets in this order.

1. Small eligible neighbor with one or two states.
2. Weakened eligible neighbor already at war elsewhere.
3. Eligible neighbor that lost divisions recently.
4. Eligible neighbor that owns claims or cores near the Fury country.
5. Larger eligible neighbor only if Fury momentum is high.
6. Major or major-backed target only in late Fury state or world-end state.

The implementation should avoid targets that pull half the world into an early local war unless that is the purpose of an evolution or the world-end branch.

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

The opening package should create several small divisions based on dynamic factors.

Baseline division families:

| Template family | Role | Notes |
| --- | --- | --- |
| Fury Columns | small infantry assault units | baseline opening unit and reserve-spawned reinforcement |
| Border Runners | low-supply infantry with speed support | used in rough terrain or low supply states |
| Capital Guard | defensive unit for capital and depot states | limits instant collapse |
| Depot Cadres | support-heavy garrison and occupation unit | appears after first conquest or occupation branch |

Starting strength bands:

| Opening strength | Conditions | Expected package |
| --- | --- | --- |
| Weak | low chaos, candidate has little industry, target is very weak | 3 to 5 Fury Columns, light stockpile |
| Normal | ordinary candidate and target | 5 to 8 Fury Columns, 1 Capital Guard |
| Severe | higher chaos, high local war tension, candidate has useful factories | 8 to 12 Fury Columns, 1 to 2 Capital Guard units |
| High chaos | evolved opening or triggerable high intensity | 12 or more better-equipped units, some support equipment, possible artillery |

These are design bands. The implementation should use constants and dynamic variables rather than hardcoding the same number for every country.

### Hidden reinforcement reserve

Fury must not receive infinite free weekly divisions. Each Fury actor receives a hidden finite reinforcement reserve pool when selected. Weekly reinforcement consumes one unit from that pool each weekly tick. When the pool reaches zero, weekly free spawning stops completely for that actor. Fury can still recruit normally through the base game. Scripted weekly reserve grants are capped at 100 total divisions per Fury actor.

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

Weekly reinforcement draw should stay finite rather than unlimited. The current implementation creates one small Fury Column every weekly tick while reserve remains. Momentum, country size, evolution state, scenario intensity, decisions, and focuses may affect direct reward waves or unit quality, but they must not directly multiply weekly free divisions.

Baseline Fury should have a small initial force and a small reserve pool. Evolution I increases unit quality and reserve size, but remains capped. Evolution II creates two Fury countries, so each individual reserve pool should be smaller than if only one Fury existed. Evolution III creates three Fury countries and stronger openings, but weekly spawning remains capped. The World in Fury scenario intensity changes initial army size and reserve pool size, not infinite spawning.

Limited extra weekly reserves may come from evolutions, scenario setup, or world-end setup, but every weekly reserve refill must be capped by script constants and must respect the maximum reserve clamp. Focuses and decisions may still create direct one-time reinforcement waves. Overextension, equipment shortages, low manpower, high resistance, and capital threat should reduce quality, reduce weekly draw, or pause the best units. They are brakes on a finite reserve, not substitutes for a cap.

## Fury values

Fury should use a few readable values rather than many hidden numbers.

| Value | Color direction | Meaning | Increases from | Decreases from |
| --- | --- | --- | --- | --- |
| Fury Momentum | red | confidence and pace of expansion | victories, captured capitals, completed expansion focuses, high chaos | defeats, stalled wars, casualties, overextension |
| Fury Overextension | orange | administrative strain and risk | too many non-core states, multiple wars, high resistance, low supply | integration decisions, compliance, occupation focuses, peace time |
| Fury Compliance Drive | green | ability to absorb conquered land | occupation decisions, depot cadres, compliance focuses, high momentum | resistance, occupation losses, harsh extraction |
| Fury Reach | purple | ability to start distant or world-end spread | no-neighbor state, becoming major, world-end focuses, other Fury actors | Fury defeat, containment, lack of ports or routes |
| Fury Pact Cohesion | yellow | cooperation between Fury states | pact type, shared wars, cooperation focuses | target disputes, hostile type, rival Fury wars |

The player does not need to see every value in a custom window. Event details, decision tooltips, national spirits, and news text should reveal the practical state. If a future UI is added, these values are the core meters.

## Conquest settlement

Fury should not rely only on ordinary peace conference behavior. The event needs a controlled settlement layer so the expansion loop is consistent.

When a Fury actor defeats its target, the settlement should:

1. confirm the defeated country is AI and safe to process.
2. identify states controlled by Fury or contiguous to the Fury front.
3. transfer or annex the defeated target where appropriate.
4. add compliance to newly captured territory.
5. add claims or cores only through the integration system.
6. raise momentum.
7. raise overextension based on the amount taken.
8. fire first-conquest news if this is the first Fury victory.
9. queue next target selection after a short delay.

If the defeated target is in a larger war or has complicated faction ties, Fury should get a clean occupation reward without breaking unrelated player wars. The settlement must avoid stealing player-occupied land.

## First-conquest news event

A news event should fire when any Fury country defeats its first neighbor.

Purpose:

- make the system visible to the world.
- show that this is not an ordinary random war.
- warn nearby powers without revealing the world-end branch.

Tone:

- factual and unsettled.
- newspapers focus on the speed of the fall.
- diplomats argue whether the fall was planned or improvised.
- generals treat it as a local anomaly at first.

Player-facing direction:

Title direction: `A Border Vanishes`.

Description direction: A small country defeats a neighbor before outside observers agree on the cause. Reports emphasize sudden mobilization, improvised columns, and new officials moving into captured administrative buildings.

Button direction: short, cold, and uneasy. Example direction: `Count the next border`.

The exact text belongs in localisation during implementation.

## Major-Fury super-event threshold

A super-event should fire when a Fury country becomes a major or crosses an equivalent power threshold.

Trigger options:

- the Fury country becomes a major by vanilla status.
- the Fury country controls enough factories, states, and divisions to count as a Fury major.
- the Fury country controls a large share of its continent and has won at least three Fury wars.
- only one super-event should fire for the first Fury major unless the implementation explicitly supports later repeats.

Purpose:

- mark the moment when the event stops being a local curiosity.
- warn that ordinary containment failed.
- unlock stronger anti-Fury and world-threat responses.
- prepare the world-end branch without revealing it too early.

This super-event is distinct from the world-end super-event. A Fury major is a major escalation. The world-end branch is a terminal campaign state.

## Repeatability

Fury is repeatable, but active counts should be controlled.

Baseline active count:

- one active Fury actor at a time during ordinary event fire.
- a new ordinary Fury can fire after the previous Fury is defeated, contained, or after a long cooldown if the first Fury is still local and not major.
- Evolution II raises ordinary active count to two.
- Evolution III raises ordinary active count to three.
- The triggerable scenario and world-end branch can create more than this because they are explicit setup or terminal systems.

Repeat firing should remember previous Fury countries. A country that recently failed as Fury should not immediately be selected again unless the scenario explicitly chooses it.

## Cluster role

Fury belongs in the Wars cluster as a medium danger member.

## Player interaction

In ordinary random play, the player mainly interacts with Fury as an observer, neighbor, or potential firefighter. The player should not gain the Fury package.

Player-facing hooks:

- news after first conquest.
- super-event after major threshold.
- event details entry.
- possible anti-Fury decisions when a Fury major exists or when Fury borders the player.
- possible achievements for containing Fury.
- possible triggerable challenge scenario.

Anti-Fury decisions should be limited. The event is minor repeatable at baseline, so ordinary countries should not gain a large permanent system every time Fury appears. Strong anti-Fury content belongs after major-Fury or world-end thresholds.
