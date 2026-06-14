# Event 008: Scripted Systems, Constants, and Helper Handoff

This is a design handoff for the scripted-system architecture pass. It is not final Clausewitz code.

## Helper map

| Helper | Scope | Inputs | Outputs | Side effects | Call sites |
| --- | --- | --- | --- | --- | --- |
| `apply_tensions_rising_event_effect` | global/root event context | current chaos tier, current world tension, event enable state | applies direct WT/chaos, dispatches hidden packages | calls timer pulse, relation pair selector, delayed report scheduler | Event 8 main option/immediate effect |
| `get_tensions_rising_stage` | global | current `chaos_tier` flag and event flags | sets a temp or global stage variable for this firing | none | event effect and event detail rebuild |
| `record_tensions_rising_evolution_if_needed` | global | stage variable, enabled evolution state | evolution log entry when appropriate | sets stage recorded flags only when enabled | event effect before stage package |
| `apply_tensions_rising_timer_pulse` | global | stage variable | active pulse strength and duration | replaces/extends capped pulse | event effect |
| `select_tensions_rising_relation_pairs` | global with country loops/arrays as existing patterns allow | stage variable, valid countries | list or immediate pair calls | saves temporary pair targets if needed | event effect stage I+ |
| `apply_tensions_rising_relation_pair` | country-to-country context | source country, target country, stage variable | timed opinion modifiers | optional pair cooldown flags | relation pair selector |
| `schedule_tensions_rising_followup` | global/event context | stage variable, world tension, optional pair context | delayed report/news event | schedules one delayed subevent | event effect stage I+ |
| `apply_tensions_rising_country_pressure` | selected country | stage variable, country score | temporary national modifier | war support/stability/AI posture effect | Stage II+ selector |

## Script constant groups

Recommended script constant category names:

### `tensions_rising_world_tension_gain`

| Key | Value |
| --- | ---: |
| `baseline` | 100 |
| `stage_1` | 100 |
| `stage_2` | 200 |
| `stage_3` | 500 |
| `stage_4` | 1000 |

### `tensions_rising_chaos_gain`

| Key | Value |
| --- | ---: |
| `stage_1` | 10 |
| `stage_2` | 15 |
| `stage_3` | 25 |
| `stage_4` | 50 |

### `tensions_rising_timer_pulse`

| Key | Value direction |
| --- | --- |
| `stage_1_strength` | 1 |
| `stage_2_strength` | 2 |
| `stage_3_strength` | 4 |
| `stage_4_strength` | 7 |
| `stage_1_min_days` / `max_days` | 45 / 75 |
| `stage_2_min_days` / `max_days` | 75 / 120 |
| `stage_3_min_days` / `max_days` | 120 / 180 |
| `stage_4_min_days` / `max_days` | 180 / 240 |
| `extension_cap_days` | stage-specific, recommended 120/180/240/300 |

### `tensions_rising_relation_pairs`

| Key | Value direction |
| --- | ---: |
| `stage_1_min` / `max` | 1 / 2 |
| `stage_2_min` / `max` | 2 / 3 |
| `stage_3_min` / `max` | 3 / 5 |
| `stage_4_min` / `max` | 5 / 8 |
| `recent_pair_cooldown_days` | 120–240 depending on implementation |

### `tensions_rising_relation_hit`

| Key | Value direction |
| --- | --- |
| `stage_1_min` / `max` | -10 / -15 |
| `stage_2_min` / `max` | -15 / -25 |
| `stage_3_min` / `max` | -25 / -40 |
| `stage_4_min` / `max` | -40 / -75 |

### `tensions_rising_followup`

| Key | Value direction |
| --- | --- |
| `stage_1_chance` | 25–35 |
| `stage_2_chance` | 40–55 |
| `stage_3_chance` | 65–80 |
| `stage_4_chance` | 85–95 |
| `stage_1_delay_min` / `max` | 5 / 15 |
| `stage_2_delay_min` / `max` | 4 / 12 |
| `stage_3_delay_min` / `max` | 3 / 10 |
| `stage_4_delay_min` / `max` | 2 / 8 |

## State lifecycle

### Persistent flags

- `tensions_rising_stage_1_recorded`
- `tensions_rising_stage_2_recorded`
- `tensions_rising_stage_3_recorded`
- `tensions_rising_stage_4_recorded`

### Timed or expiring state

- active timer pulse flag or remaining-days variable
- recent pair cooldown flags or country-pair memory if repo has a generic relation-pair helper
- temporary country pressure modifiers
- optional delayed follow-up scheduled flags if needed to prevent duplicates

### Cleanup expectations

- Pulse state expires naturally or is read as inactive at zero strength.
- Pair cooldowns expire.
- Temporary national modifiers expire.
- No global event target for a relation pair should persist beyond a single effect chain unless a delayed named follow-up genuinely requires it, if global targets are used, they must be cleared.

## Duration field caution

If timed flags reject script constants or variable tokens in the current engine version, use a file-scoped literal constant in the event script for that timed flag and mirror the value in script constants documentation. Do not silently hardcode disconnected magic numbers.

## Event target plan

Use regular event targets for short-lived pair or country contexts inside the current event chain. Prefer generic delayed reports that do not need exact pair names. This avoids multiple delayed follow-ups overwriting one global pair target.

If a delayed report must name exact countries, schedule it from inside the same event chain with saved event targets that are carried safely into the delayed event. Do not use one global target for all pending reports.

## Integration points

### Event file

- `events/008_tensions_rising.txt` or current repo naming pattern.
- The canonical start remains `chaosx.nr8.1` if the repo follows the `chaosx.nr<ID>.1` convention.

### Event registration

- Keep ID `8` in the Minor Repeatable array.
- Keep debug and event-log names aligned.
- Make sure manual firing respects the evolved gating and force-trigger behavior.

### Event details and evolutions

- Add Event 8 main detail row.
- Add `Diplomatic Fever` evolution entries and stage text.
- Record evolution entries only when enabled.

### Timer system

- Add a single read hook for active Tension Pulse if existing timer logic supports a modifier input.
- Avoid new daily/weekly world loops.

### Relation system

- Prefer a small generic helper if no relation-pair helper exists.
- Document new helper if it belongs in `chaosx_dynamic_effects`.

### Cluster system

- If registering `Diplomatic Panic`, keep the current member note simple.
- For now one member: Event 8 `Tensions Rising`, required, medium severity.
- If not implementing, keep it as queued documentation.

## Validation notes for implementer

Task-specific checks after implementation should include:

- Event ID 8 remains Minor Repeatable.
- Baseline cannot auto-fire at WT 100 before Stage I.
- Stage I+ can fire at WT 100.
- Stage IV remains non-terminal and does not trigger a super-event.
- No direct war goals, countries, focus trees, cores, or formables are created.
- Timer pulse replacement/cap works under repeated firings.
- Delayed reports do not recursively fire Event 8.
- Relation modifiers are timed and do not stack endlessly on one pair.
- Event log detail and evolution surfaces show the correct stage text.
