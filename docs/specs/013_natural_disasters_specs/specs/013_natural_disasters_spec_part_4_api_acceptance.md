# Event 013 Natural Disasters Spec, Part 4, Scripted System Architecture and Acceptance Criteria

## Scripted system architecture

Event 013 should be implemented as a reusable scripted system. The event file should call helpers. It should not contain repeated family damage blocks for every disaster.

Recommended core helpers, using working names:

| Helper | Expected scope | Inputs | Outputs and side effects |
| --- | --- | --- | --- |
| `natural_disasters_start_sequence` | ROOT country or global caller | intensity, family pool, target mode, news policy, caller id, scenario flags | Creates sequence state, logs one Event 013 firing, schedules first pulse |
| `natural_disasters_select_family` | controller scope | pool id, evolution tier, target profile, caller restrictions | Sets current family variable and family flags |
| `natural_disasters_select_target` | controller scope | family id, target mode, preferred actor, region seed | Saves target state, target country, area group, and fallback reason |
| `natural_disasters_schedule_next_pulse` | controller scope | sequence length, current pulse index, delay policy | Schedules next event with dynamic delay |
| `natural_disasters_apply_family_to_target` | target state or country | family id, severity, follow-up policy, recovery policy | Applies damage, deaths, modifiers, and aftermath |
| `natural_disasters_apply_state_damage_profile` | state scope | damage profile id, severity, neighbor factor | Damages buildings and sets state aftermath |
| `natural_disasters_record_deaths` | state or country | family id, civilian death estimate, delayed flag | Feeds shared Deaths system and applies population loss |
| `natural_disasters_open_recovery` | country scope | affected states, disaster family, severity | Opens category, activates decisions, sets recovery variables |
| `natural_disasters_schedule_report` | country or global scope | target area, family id, severity, news policy | Schedules one to two day delayed report when needed |
| `natural_disasters_schedule_followups` | controller scope | family id, target context, severity | Queues aftershock, flood, tsunami, famine, refugee, or other chains |
| `natural_disasters_cleanup_sequence` | controller scope | sequence id | Clears temporary targets, flags, selected state, and invalid decisions |
| `natural_disasters_call_direct_family` | caller scope | family id, target, intensity, news policy | Public API for other events |

The public API should be documented in `common/scripted_effects/chaosx_dynamic_effects.md` or the matching Natural Disasters helper doc when implemented. The implementation should include examples for a random event call, a direct targeted earthquake, a divine-power targeted flood, a manual scenario barrage, and a storm corridor movement step.

## Event targets and variables

The sequence system needs persistent enough state to schedule delayed pulses without leaking stale targets.

Required state concepts:

- sequence id
- current pulse index
- pulse total
- active family id
- intensity value
- evolution profile id
- news policy id
- recovery policy id
- caller event id
- caller country, if any
- target country, if any
- target state, if any
- target region id or area group id
- origin state for follow-up families
- storm corridor current state group
- storm corridor next predicted state group
- abnormal disaster cooldowns
- recently hit state cooldowns

Event targets should be used for short chains when needed. Global event targets should be avoided unless a GUI or delayed sequence needs persistence beyond the immediate event chain. Any global event target must have explicit cleanup.

Use flags for true or false states. Use variables for counters, ids, severity, cooldown values, and dynamic weights. Do not store boolean state in variables unless a UI array or engine surface requires it.

## Constants and tuning tables

The implementation should centralize tuning in script constants or documented tuning helpers.

Recommended categories:

- `natural_disaster_sequence` for pulse counts, delay bands, compression factors, and caps.
- `natural_disaster_damage` for building damage ratios and severity multipliers.
- `natural_disaster_deaths` for mortality floors, caps, and delayed death bands.
- `natural_disaster_family_weight` for family pools by baseline, evolution, scenario type, and region.
- `natural_disaster_followup` for chained family chances.
- `natural_disaster_news` for report thresholds and digest cooldowns.
- `natural_disaster_recovery` for mission durations, cost multipliers, and recovery reductions.
- `natural_disaster_ai` for response priority and decision weights.
- `natural_disaster_gui` for map state ids, animation state ids, and panel thresholds.
- `disaster_barrage_scenario` for intensity stops and scenario type ids.

Timed flags or fields that reject script constants should use file-scoped literal constants or meta effects according to the repository rules. Do not scatter magic numbers across the event file.

## Recovery decision architecture

Recovery decisions should be grouped by active family and active state. If many states are affected, use priority filtering or a selected-target flow.

Decision data model:

- affected state saved or indexed
- family id
- severity
- recovery phase
- delayed death risk
- infrastructure damage risk
- supply risk
- follow-up risk
- active mission id
- country response score

The response score can reduce delayed deaths, shorten modifiers, and lower future target weight. It should not remove all damage instantly. Reconstruction should take time.

## AI behavior architecture

AI should not ignore disasters. AI also should not spend itself into collapse for every small hit.

AI priorities:

1. Capital hit.
2. High population state.
3. Supply hub or rail corridor hit during war.
4. Port or naval base hit for island and naval countries.
5. Factory-heavy state.
6. Follow-up risk with delayed tsunami, wildfire, famine, or storm corridor.
7. Ordinary rural damage.

AI should scale spending by economy, war state, stability, available equipment, and disaster severity. AI should use low-cost emergency actions when weak and save expensive reconstruction for important states.

The AI for other events that call the disaster API should not need to know every family detail. The family helper should set recovery priorities and AI decision visibility.

## Integration with Event Logs

Event 013 logging should happen once per fired sequence. If a cluster launches three Event 013 members over a month, those are three Event 013 firings. If one Event 013 sequence contains twelve disasters, it is still one Event 013 Event Log row.

The log detail window should describe the premise of Natural Disasters and current evolution availability. It should not display every hidden damage profile. It can mention that disasters can hit states, regions, countries, or global corridors and that affected countries can receive recovery decisions.

Evolution log entries should record actual evolution milestones only. Baseline disaster seasons and ordinary sequence stages are not evolutions.

## Integration with Deaths, Chaos, and Air Cleanliness

Deaths:

- Every family with mortality should call the shared deaths system.
- Deaths should be civilian unless a specific military casualty hook is added for units caught in disaster states.
- Death source should identify natural disaster family where supported.

Chaos:

- Deaths already increase chaos through the shared death scaling. Event 013 can add small direct chaos only when a disaster is abnormal, global, or politically destabilizing.
- Ordinary disasters should not inflate chaos solely because they fired.

Air cleanliness:

- Wildfire smoke, volcanic ash, dust storms, and meteor skyfall may optionally interact with an air quality or sky condition concept if the existing Air Cleanliness system supports non-weapon sources.
- They should not be treated as chemical contamination or condemnation.

## Implementation surfaces

Expected touched surfaces for coding:

- Event file for Event 013 and subevents.
- Placeholder conversion for Event 046 and Event 099.
- Random-event registration and Event Details.
- Event log names and evolution names.
- Scripted effects and triggers for disaster system.
- Script constants for tuning.
- Decisions and categories for recovery.
- Scripted localisation for dynamic area, family, cost, and summary text.
- GUI and GFX for disaster map when Evolution III is implemented.
- Super-event scripted localisation, GFX, and audio wiring for abnormal thresholds.
- Deaths system call sites.
- Cluster registry and member mapping.
- Triggerable scenario registry and launch logic for Disaster Barrage.
- Docs, asset manifests, and spreadsheet alignment after implementation.

## Validation expectations

Implementation validation should include task-specific checks. Do not rely only on load success.

Required meaningful checks:

- Manual trigger of baseline Event 013 creates one Event Log row and schedules delayed pulses.
- A sequence with multiple disaster pulses does not create multiple Event Log rows.
- A disaster reduces real state population through the Deaths system when that system is enabled.
- Building damage differs by family.
- Reports identify the affected area and do not fire for every small Evolution II disaster.
- Recovery category appears only for affected countries and cleans up after recovery.
- Direct API calls from another event can trigger a named disaster family against a selected state or country.
- Event 046 and Event 099 no longer run old logic after their content is folded or retired.
- Event 051 heat-wave modifiers do not stack with Event 013 heat-wave modifiers.
- Disaster Barrage scenario reads type and intensity, then uses the same controller.
- Cluster-fired Natural Disasters members schedule delayed Event 013 seasons and respect special cooldowns.
- Evolution III storm corridor updates GUI state and applies damage to the current path.
- Abnormal super-events use researched text and licensed audio, not placeholders.
- The spreadsheet worker updates catalog fields after final localisation exists.

## Simplification blockers

The following simplifications would violate the spec unless the user explicitly approves them.

- One generic disaster effect for all families.
- Cosmetic damage only.
- No real population loss.
- No recovery decisions.
- All disasters firing on the same day.
- Every disaster creating an Event Log entry.
- Evolution II report spam for every global disaster.
- Evolution III abnormal disasters without super-event treatment.
- Storm corridor without a real moving state system.
- Scripted GUI that only decorates and does not support gameplay choices.
- Direct API calls that cannot target an individual disaster cleanly.
- Leaving Event 046 or Event 099 active with old logic.
- Stacking Event 013 heat waves with the separate Heat Wave event.
- Manual Disaster Barrage implemented as a separate copied script.

## Completion definition

The rework is complete when the event can fire normally, fire through clusters, launch through Disaster Barrage, be called by other events, show clear reports, damage states meaningfully, kill population through the Deaths system, open recovery decisions, evolve through the three defined stages, support abnormal super-event thresholds, update GUI state for moving hazards, and leave the docs and spreadsheet aligned.
