# Event 008: Evolutions and Hidden Effect Map

This file expands the single `Diplomatic Fever` evolution track so the event does not become a flat table of world-tension numbers.
The [main spec](008_tensions_rising_spec.md) holds the stage values and the accepted corrections; this file covers stage availability, the hidden layers, and their limits.

## Evolution track: Diplomatic Fever

`Diplomatic Fever` is a mutation track rather than ordinary event stages: it changes what every future Event 8 firing means.

## Stage availability and logging

`get_tensions_rising_stage` maps the current Chaos tier to a stage (tier 1 to Stage I, tier 2 to Stage II, tier 3 to Stage III, tiers 4 and 5 to Stage IV) and falls back to the baseline packet when that stage's evolution checkbox is disabled.
A disabled stage sets no record flag and unlocks no follow-up.
`record_tensions_rising_evolution_if_needed` writes one evolution row the first time each stage's packet applies.

| Stage | Display tier | Event detail preview direction |
| --- | --- | --- |
| I | Gathering Storm | cable traffic and official denials begin to quicken later incidents |
| II | Rising Chaos | rumours become a market, and accusations begin shaping relations |
| III | Chaos Tier | general staffs and border commands react while diplomats deny |
| IV | Total Chaos | the world settles into a permanent alert, and every capital keeps its warnings active |

If Event 8 first fires at a high tier, it starts at the highest allowed stage; lower stages are not recorded as fired history, and the player never sees several evolution popups at once.

## Stage package table

| Field | Baseline | Stage I | Stage II | Stage III | Stage IV |
| --- | --- | --- | --- | --- | --- |
| Requested world tension | 2 | 3 | 5 | 8 | 12 |
| Chaos | none | 10 | 15 | 25 | 50 |
| Full-tension rule | requires tension below full | can fire at full | can fire at full | can fire at full | can fire at full |
| Timer pulse | none | 1 | 2 | 4 | 7 |
| Relation pairs | none | 1-2 | 2-3 | 3-5 | 5-8 |
| Follow-up chance | none | 30% | 50% | 75% | 90% |
| AI posture idea, selected AI countries | none | cautious alignment, 4 | alarmist rearmament, 6 | general staff fever, 8 | permanent alert, 12 |
| Border clash chance on clash incidents | none | none | none | 35% | 60% |
| Super-event | no | no | no | no | no |

All values live in `common/script_constants/008_tensions_rising_constants.txt`.

## Tension Pulse behavior

The pulse is global state read by the existing event timer: `tensions_rising_timer_pulse_active`, `global.tensions_rising_timer_pulse_strength`, `global.tensions_rising_timer_pulse_days`, and `global.tensions_rising_timer_pulse_expiry_date`.
It creates no repeated global loop.

1. With no pulse active, the new stage's strength and a duration from its band apply.
2. A stronger stage replaces a weaker pulse with its own strength and duration.
3. An equal stage converts the exact expiry-minus-today offset to remaining days, adds the stage extension, clamps to the stage cap, and sets a new exact expiry.
4. A weaker stage never lowers an active stronger pulse.
5. At expiry the strength returns to zero and the active flag clears.

Event 8 still counts as an ordinary Minor Repeatable for normal timer pressure; the pulse is an extra evolved-stage effect.

## Relation-pair selector

The selector prefers pairs that make diplomatic sense.

| Factor | Current handling |
| --- | --- |
| both countries exist and can conduct diplomacy | required |
| majors and faction leaders | preferred actors |
| capitulated countries, subjects, special chaos countries, direct war opponents, subject-overlord pairs | excluded |
| same-faction pairs | excluded at Stages I-II, allowed from Stage III as faction-splitting panic |
| actors hit within 150 days | avoided by the primary pass; fallback passes can still pick them |

Further plausibility factors from the original design (shared borders, claims, opposing factions, ideology rivals) are design intent not yet expressed in the selector.

Opinion damage is mutual: each selected pair receives the stage modifier in both directions, counted once per directed stage-and-partner record.
The same pair cannot stack the same stage modifier while its counting flag is active.

## Temporary AI posture

Each evolved root applies one hidden, timed posture idea to a stage-scaled number of AI majors, faction leaders, or countries at war that were not recently selected.
Durations are 45, 75, 100, and 140 days by stage.

| Idea | Stage | Direction |
| --- | --- | --- |
| `tensions_rising_cautious_alignment` | I | cheaper guarantees and stronger alliance desire |
| `tensions_rising_alarmist_rearmament` | II | adds war support and arms production at a small stability cost |
| `tensions_rising_general_staff_fever` | III | stronger rearmament, planning speed, and faster enemy justification against the country |
| `tensions_rising_permanent_alert` | IV | the strongest version of the same pressure |

The earlier modifier families (Alarmist Press Cycle, Mobilization Draft Rooms, Market of Alarms) were consolidated into these four AI-only ideas and the insurance incident; no player country receives a posture idea.

## Delayed incident scheduling

One delayed follow-up may come from the first effectful evolved root of each report batch, selected by stage, world tension, and recent relation damage.
Incidents apply smaller real bundles and never fire Event 8 again.

`select_tensions_rising_followup_event` checks these pools in order and uses the first that applies:

| Order | Condition | Pool (equal or listed weights) |
| --- | --- | --- |
| 1 | Stage IV and the Last Normal Briefing not yet seen | The Last Normal Briefing |
| 2 | Stage II+ with recent Event 8 relation damage | One Denial Too Many, Border Lamps, Fleets Keep Radio Silence, The Rumour That Arrived Twice |
| 3 | world tension full | Unease Along the Frontier, Fleets, Border Lamps, One Denial |
| 4 | Stage I | Telegram 45, Embassy Side Doors 35, Unease 20 |
| 5 | Stage II | Insurance Rates 30, Rumour 25, One Denial 25, Staff Cars After Midnight 20 |
| 6 | Stages III-IV | Fleets, Border Lamps, Staff Cars, One Denial |

| Incident | Effect |
| --- | --- |
| The Telegram Nobody Signed | small tension, Chaos, and one opinion shock |
| Embassy Side Doors | small aftershock plus AI posture |
| Unease Along the Frontier | small aftershock |
| Insurance Rates Jump in Neutral Ports | small aftershock and the Insurance Market hook |
| The Rumour That Arrived Twice | two opinion shocks |
| Staff Cars After Midnight | AI posture and opinion pressure |
| Fleets Keep Radio Silence | AI posture and opinion pressure |
| Border Lamps | heavier opinion damage and a possible non-transfer clash at Stage III+ |
| One Denial Too Many | heavier opinion damage and a possible clash at Stage III+ |
| The Last Normal Briefing | strongest bundle and the highest clash chance |

Because every Stage II+ root applies relation damage, branch 2 usually wins at Stage II and above, so the Stage II pool (the only source of the insurance incident) and Staff Cars are rarely reached.
Numerical reachability remains unresolved with the probability owner, and a proposal in the README turns recent damage into a weight instead of a priority branch.

## Stage IV presentation

Stage IV stays inside the normal report, option tooltip, event log, evolution detail, achievements, and incident surfaces.
It triggers no super-event and creates no world-end branch.

## Anti-exploit rules

- Relation modifiers never stack on the same pair and stage while their counting flag is active.
- The timer pulse never stacks additively.
- Delayed incidents never schedule additional Event 8 firings.
- Posture ideas go only to valid, living AI countries outside special-country exclusions.
- Event 8 grants no war goals, cores, claims, or free units.
- Stage III+ clash incidents start only non-transfer clashes between safe independent adjacent rivals and respect the global and per-country cooldowns.
- Incident world-tension packets stay below their stage's root packet (see the main spec's Aftershock scale).
