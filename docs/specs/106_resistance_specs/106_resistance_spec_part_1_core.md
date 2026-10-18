# 106 Resistance, Part 1: The worldwide wave

## The crisis

Occupied communities across the world begin resisting at the same moment. The change reaches a distant colony, a newly conquered border region, and an annexed homeland through the same rule. The occupier's size, ideology, faction, subject status, and human or AI control do not change the immediate addition.

Resistance puts pressure on the occupations that the campaign actually contains. An empire with many occupied states has more places to secure. A small country that has just conquered one foreign state still receives the full local shock. A country controlling only its own cores experiences the event through the wider world and any consequences for its allies or enemies.

The player manages the aftermath through the occupation systems already in use. Rising native resistance can worsen partisan activity, sabotage, and garrison losses. Later events can turn the same local conditions into political change. Event 106 itself applies the resistance wave. Occupation Revolt owns the scripted uprising response described in Part 3.

## Event identity

| Field | Required value |
| --- | --- |
| Event ID | 106 |
| Event name | Resistance |
| Event type | Minor Repeatable |
| Catalog status | To Be Reworked |
| Chaos level | 1 |
| Cluster | Domestic Unrest |
| Cluster member severity | Low |
| Event slug | `resistance` |

These are the current user-defined values. The conflicting supplied catalog rows are reconciled separately in the evidence and decisions file. They do not change this design.

## One activation, one worldwide addition

At the start of a logical firing, determine the highest active evolution and freeze its addition for the whole wave. Visit the occupied states that exist at that moment. Apply the addition once to each valid state, including territory controlled by AI minors, majors, subjects, human countries, and valid unusual or newly created controllers.

For a state with current resistance `R` and the wave's addition `A`, the result is:

`new resistance = min(100, R + A)`

`actual addition = new resistance - R`

All values in this design are percentage points on the player-facing 0 to 100 resistance scale. A baseline wave takes 25% resistance to 50%. It does not multiply 25% by 1.25, set every state to 25%, or change only the resistance target.

The direct addition happens before the public report can be acknowledged. The report's option acknowledges a completed event. It has no second application of the wave. A multiplayer client, an AI notification, or a reopened history entry cannot apply it again.

The logical firing uses one authoritative execution. If a real control or eligibility change occurs during resolution, the state must be revalidated immediately before its write. One state still receives at most one write for this firing. A stale country pointer must not redirect the addition into another state or cancel the remaining valid states.

## Which states are occupied for this event

The semantic target is a land state that can carry native occupation resistance against its current foreign controller under the active game rules. It needs a valid current state controller and an eligible native occupation relationship. It must not be a core of that controller. The occupied homeland may be dormant or annexed. A successful claimant lookup by a partner event is not required for the native wave.

The implementation must demonstrate this predicate against the installed game's occupation rules. The inspected reference material does not establish a complete exact trigger combination, particularly for resistance at zero. That technical gap cannot be resolved by narrowing the design. See evidence items E04 and E05.

| Campaign situation | Required result |
| --- | --- |
| Enemy non-core state under wartime control | Affected when native occupation resistance is valid |
| Annexed foreign non-core state whose owner and controller are the same country | Affected when native occupation resistance is valid |
| A valid occupied state currently at 0% resistance | Affected by the full addition |
| A valid occupied state with high compliance or a well supplied garrison | Affected by the same immediate addition |
| A valid occupied state already at 100% resistance | Visited and left at 100%, with actual addition zero |
| A subject occupying a foreign non-core state | Affected under that subject's own state controller identity |
| An overlord that merely has political authority over a subject's territory | Receives no duplicate write on the subject's behalf |
| Controller's core state, including a reconquered homeland core | Outside the occupation target set |
| Mixed province control inside a state | Uses the authoritative state controller and the verified native state rule |
| A state with an absent controller or no valid native occupation resistance relationship | Skipped without creating a political identity or resistance system |
| Occupation created after the completed wave | First becomes eligible for the next firing |

Neither `owner differs from controller` nor `resistance is currently nonzero` is sufficient as the event's selector. The first loses annexed non-core occupations. The second loses pacified occupations that the user explicitly intends later waves to disturb.

There is no country rank, ideology, faction, geography, or human-control filter. A shared classifier may help validate a controller, but it cannot invent an exemption for a valid occupation.

## Resistance and resistance target

The wave adds current resistance immediately. Existing resistance targets, growth and decay rules, occupation laws, compliance, garrison supply, and intelligence effects remain the causes of later native movement.

For example, a state at 10% resistance with a low resistance target reaches 35% in the baseline wave. It may then begin moving back toward its target under the game's normal rules. That later recovery is a meaningful consequence of good occupation control. It does not reduce the required immediate write.

Do not compensate for the wave with an automatic compliance grant, a scripted immediate resistance reduction, a blanket occupation-law change, or a temporary target modifier. Such compensation would obscure the event's central effect and weaken the connection to later uprisings.

## Evolutions

The event has one intensity track with three stages. The names below are supplied by the user. All additional explanatory text remains a localisation direction until implementation.

| Highest active stage | Chaos requirement for activation | Addition on future firings | Opening at 0% resistance |
| --- | ---: | ---: | ---: |
| Baseline | 0+ | +25 percentage points | 25% |
| I: Rising Resistance | 200+ | +50 percentage points | 50% |
| II: Mass Resistance | 400+ | +75 percentage points | 75% |
| III: Total Resistance | 600+ | +100 percentage points | 100% |

Reaching an eligible threshold grants the corresponding stage through the event's evolution registration. A pre-fire check catches up any qualifying stages before the first or a later firing. This is the planning skill's instantaneous opening-intensity case. It does not introduce an MTTH wait before the stated amount becomes available.

Stage activation changes future wave strength and its recorded evolution history. It adds no resistance and no Chaos by itself. Existing resistance, completed wave receipts, and earlier reports retain their original values.

Only the highest active stage supplies `A`. At Stage III a state at zero gains 100 points once. It does not receive 25 + 50 + 75 + 100, and activation of three stages does not produce three waves.

### Persistence and settings

The following persistence rule is a parent-selected expansion of the brief, whose wording does not specify what happens when Chaos later falls.

A granted stage remains unlocked for that campaign. Falling Chaos alone does not remove it. The active stage is the highest granted stage that is currently enabled through the existing evolution controls. If all granted stages are disabled, future firings use the baseline. Disabling a stage does not undo past resistance or erase its historical activation.

A disabled ungranted stage is not granted or logged while disabled. Once enabled, it can be granted when the current Chaos requirement is met. A previously granted stage becomes available again when enabled, without a new activation record or a wave. A higher stage may activate at its own threshold even when a lower stage is disabled.

When Chaos jumps over several thresholds, record each newly granted eligible stage once through the shared history contract. Use the actual grant date. Do not fabricate earlier activation dates. The wave then uses the highest active stage once.

### Sampling and feedback order

Before starting a new wave, complete any still-unobserved containment or achievement checkpoints due at that exact elapsed-day boundary under Part 4's finite scheduling contract. This order is the same whether the ordinary callback or the wave's pre-write check reaches the due record first. Then resolve the wave's stage and native writes. A missed earlier checkpoint is not a due observation that can be reconstructed now.

Resolve stage grants and freeze the active addition before changing any state's resistance and before awarding this wave's Chaos gain. Every state in a wave receives the same nominal addition. If the wave's own consequences push Chaos across the next threshold, the new stage affects the next firing.

For a fresh campaign with no previous stage grants, a baseline firing beginning at 199 Chaos adds 25 points. If its accepted Chaos gain takes the world beyond 200, Stage I may then activate, but the completed wave stays at 25 points. A first firing at 600 Chaos starts at Stage III and adds 100 points.

## Arithmetic examples

| Resistance before | Baseline +25 | Stage I +50 | Stage II +75 | Stage III +100 |
| ---: | ---: | ---: | ---: | ---: |
| 0 | 25 | 50 | 75 | 100 |
| 10 | 35 | 60 | 85 | 100 |
| 24.5 | 49.5 | 74.5 | 99.5 | 100 |
| 25 | 50 | 75 | 100 | 100 |
| 50 | 75 | 100 | 100 | 100 |
| 75 | 100 | 100 | 100 | 100 |
| 90 | 100 | 100 | 100 | 100 |
| 100 | 100 | 100 | 100 | 100 |

The decimal example is a design oracle for supported native precision. Implementation must verify the engine scale and observed precision rather than introducing rounding to match a guessed token convention.

## Repetition follows the map

Each later firing rebuilds the eligible set from current occupations. It never replays a cached list of countries or states.

A state can move from 0 to 25 to 50 through two baseline waves. If occupation measures later reduce it to 15, another baseline wave takes it to 40. A territory conquered after those waves joins the next wave at its own current value. A state restored to its controller's cores or otherwise removed from native occupation is no longer a target.

A wave at 100% leaves the state at 100%. It may still appear in a truthful count of eligible occupations. It does not create a positive addition, a new material-wave receipt, or another force bonus for Occupation Revolt. Native resistance at 100 remains a strong live input to that event's ordinary local evaluation.

## Firing and report cases

Natural selection should require at least one valid occupied state. This gate includes valid states at zero resistance and at the cap. The shared repeatable selection and cluster systems determine when a firing occurs. Event 106 adds no separate automatic recurrence schedule.

A supported direct invocation with an empty target set completes once as an empty result. It creates no replacement target, no extra resistance, no Chaos gain, and no local interaction receipt. The shared firing history records the invocation truthfully. The implementation must not secretly turn this into the dormant-claimant behavior of another event.

One world history entry represents one firing. Human recipients see the ordinary report appropriate to their situation. An occupier's report can describe the effects in its controlled occupations. A dispossessed country can receive the occupied-homeland viewpoint only when that relationship is valid. Other recipients receive the worldwide observer viewpoint. These variants change presentation, not the wave's mechanics.

The moment of the wave remains clear in every case. A report should distinguish the nominal addition from saturation, and should not claim that every eligible state increased when some were already at 100%.

## What the event sets in motion

The useful uncertainty is what happens after the immediate surge. A well supplied occupation can bring resistance down. A stretched empire may lose equipment and control across several homelands. A later Occupation Revolt can find more local movements ready to act and can give those movements stronger locally supported forces.

106 directly releases no country and starts no independence war. High native resistance can still have engine-owned consequences. The developer's public description of the native system explicitly discusses garrison losses and large uprisings, while the exact installed thresholds remain a required runtime check. Evidence item E06 separates that native behavior from the scripted responsibilities of 106 and 095.

The remaining parts specify the local memory, the cross-event response, recovery and Chaos feedback, achievements, presentation, and acceptance conditions.
