# Event 008: Evolutions and Hidden Effect Map

This file expands the single `Diplomatic Fever` evolution track for Event 008. It is meant to prevent the implementation from becoming a flat table of world tension numbers.

## Evolution track: Diplomatic Fever

`Diplomatic Fever` is a mutation track. It does not describe ordinary event stages. It changes what every future Event 8 firing means.

The stage should be determined from campaign state and logged according to the shared Chaos Redux evolution system. If an evolution is disabled, that stage’s extra behavior should not silently set stage-record flags or unlock follow-up logic. The baseline event can still fire according to its own rules.

## Stage availability and logging

| Stage | Display tier | Suggested unlock condition | Record timing | Event detail preview |
| --- | --- | --- | --- | --- |
| I | Gathering Storm | chaos value reaches Gathering Storm and Event 8 is enabled | first qualifying automatic or manual Event 8 run after threshold, or MTTH-style evolution check if shared system supports it | “Cable traffic and official denials begin to quicken later incidents.” |
| II | Rising Chaos | chaos value reaches Rising Chaos, Stage I known or implicitly bypassed by pre-fire opening | first qualifying Stage II packet | “Rumours become a market, accusations produce visible diplomatic costs.” |
| III | Chaos Tier | chaos value reaches Chaos Tier | first qualifying Stage III packet | “General staffs and border commands react before diplomats can finish denying anything.” |
| IV | Totalen Chaos | chaos value reaches Totalen Chaos | first qualifying Stage IV packet | “The world enters a permanent alert rhythm. Tension no longer needs room to rise.” |

If Event 8 first fires at a high chaos tier, it should start at the highest allowed stage for that tier. The lower stages should either be recorded as skipped-by-opening if the current event-log system supports that distinction, or simply not recorded and not presented as fired history. Do not spam four evolution popups at once.

## Stage package table

| Field | Baseline | Stage I | Stage II | Stage III | Stage IV |
| --- | --- | --- | --- | --- | --- |
| World tension | `+10` | `+10` | `+20` | `+50` | `+100` |
| Chaos | none | `+10` | `+15` | `+25` | `+50` |
| WT cap rule | requires WT < 100 | can fire at WT 100 | can fire at WT 100 | can fire at WT 100 | can fire at WT 100 |
| Timer pulse | none | light | medium | heavy | severe |
| Relation pairs | none | 1–2 | 2–3 | 3–5 | 5–8 |
| Delayed follow-up | none or very rare | low chance | moderate chance | high chance | very high chance |
| Temporary country modifier | none | no, unless follow-up | possible | likely for selected majors | likely for selected majors/faction leaders |
| Super-event | no | no | no | no | no |

## Tension Pulse implementation behavior

The Tension Pulse can be implemented through a helper that the existing event timer reads. It should not create a new repeated global loop.

### Variables and flags

Recommended global state:

- `global.tensions_rising_pulse_strength`
- `global.tensions_rising_pulse_days_remaining` or equivalent timed flag if supported by the existing timer logic
- `tensions_rising_stage_1_recorded`
- `tensions_rising_stage_2_recorded`
- `tensions_rising_stage_3_recorded`
- `tensions_rising_stage_4_recorded`

If the timer system already has a generic temporary modifier framework, use it instead of introducing these exact names. The names above define the design intent, not a required syntax recipe.

### Replacement logic

1. If no pulse is active, set the new stage’s strength and duration.
2. If a weaker pulse is active, replace it with the stronger pulse and its duration.
3. If the same pulse is active, extend remaining duration by a stage-specific extension amount, up to a cap.
4. If a stronger pulse is active, do not lower it, optionally extend it by a small amount only if the stage is close enough.
5. When pulse duration expires, set strength back to `0` and clear the active flag.

### Interaction with normal minor-event pressure

Event 8 remains a Minor Repeatable. It should still count as a minor event and affect normal minor-event timer pressure. The Tension Pulse is an additional evolved-stage effect, it should not replace the base event-system consequence.

## Relation-pair selector design

### Candidate scoring

Each possible pair should receive score from a compact set of factors.

| Factor | Score direction |
| --- | --- |
| both countries exist and are independent enough for diplomacy | required |
| both are majors | strong positive |
| one is a major and one is a regional rival | positive |
| border each other | positive |
| have claims, cores, or active disputes | strong positive |
| opposing factions | strong positive |
| opposing ideology families | positive |
| same faction | negative at Stage I–II, neutral or slight positive at Stage IV only for faction-splitting panic |
| subject-overlord | negative unless special colonial panic follow-up is selected |
| already recently hit by Event 8 | negative, unless Stage IV repeat shock selected |
| one country is special nonhuman or terminal actor | excluded unless explicitly allowed by shared special-country logic |

### Pair diversity

The same pair should not receive a new Event 8 relation modifier every time the event fires unless enough time has passed or Stage IV deliberately repeats the pressure. Use cooldown flags or check existing timed opinion modifiers where possible.

### Directionality

Opinion damage should usually be mutual. Some follow-ups can be one-way if the story requires it, such as an accusation by one country against another.

## Temporary country modifiers

These are optional but valuable at Stage II+.

### Modifier family: Alarmist Press Cycle

Best for democracies, neutral countries, or high-stability countries.

Visible story:

- Newspapers demand readiness.
- Opposition parties accuse the cabinet of complacency.
- Public meetings fill with maps and casualty predictions.

Effect direction:

- modest war support gain
- modest stability loss
- optional consumer goods or political power cost if existing mechanics support it
- high chance to expire cleanly after 45–90 days

### Modifier family: Mobilization Draft Rooms

Best for majors, faction leaders, authoritarian countries, or high-chaos stages.

Visible story:

- Staff offices prepare documents that no minister wants to sign.
- Border units receive contradictory readiness orders.
- Logistics clerks are told to check rail timetables twice.

Effect direction:

- war support or mobilization speed direction
- stability or political trust penalty
- temporary AI interest in defensive/hostile preparation

### Modifier family: Market of Alarms

Best for trade-heavy or convoy-heavy countries.

Visible story:

- Insurance and shipping firms price risk before governments define it.
- Neutral merchants react faster than foreign ministries.

Effect direction:

- small temporary trade/convoy anxiety if the repo already has a compatible modifier
- otherwise flavour-only report with no direct modifier

## Delayed report scheduling

Follow-up reports should be scheduled sparingly. The best model is one delayed follow-up per Event 8 firing, selected by weighted stage, world tension, active wars, navies, borders, and recent relation damage.

### Follow-up selection table

| Follow-up | Stage weights | Extra conditions | Direct effect allowed |
| --- | --- | --- | --- |
| The Telegram Nobody Signed | high at I, medium at II | none | none |
| Embassy Side Doors | high at I–II | at least two majors or faction leaders alive | none |
| The Calm Map Says Nothing | high if WT already 100 | WT = 100 | none, maybe log detail |
| Insurance Rates Jump in Neutral Ports | high at II–III | at least one major trading/convoy country exists | tiny trade/convoy anxiety only if existing modifier supports it |
| The Rumour That Arrived Twice | high at II–III | no active world-end | possible extra small relation hit if safe |
| Staff Cars After Midnight | high at III–IV | at least one major alive and not capitulated | temporary AI posture, not direct war |
| Fleets Keep Radio Silence | medium at III–IV | naval majors or active sea zones relevant | possible naval panic modifier only if supported |
| Border Lamps | high at III–IV | valid border-rival pair | relation hit or report only |
| The Last Normal Briefing | one-time Stage IV | Stage IV first firing | report only |

## Stage IV presentation

Stage IV stays inside the normal event popup, option tooltip, event log, evolution detail, achievements, and delayed-report surfaces. It does not trigger a super-event and does not create a world-end branch.

## Anti-exploit rules

- Do not let relation modifiers stack infinitely on the same pair.
- Do not let timer pulse stack additively.
- Do not let delayed reports schedule additional Event 8 firings.
- Do not apply national spirits to countries that are invalid, dead, capitulated in a way that makes the modifier meaningless, or excluded by special-country logic.
- Do not give war goals, cores, claims, or free units from Event 8.
