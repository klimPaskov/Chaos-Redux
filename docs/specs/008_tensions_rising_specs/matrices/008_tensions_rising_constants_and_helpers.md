# Event 008: Scripted Systems, Constants, and Helper Map

Disposition: implemented; this file maps the installed helpers and tuning blocks so later work edits the right owner.
The planning-era helper proposals and their numeric tables (including the superseded `+100` to `+1000` world-tension ladder and suggested opinion ranges) were removed because source now owns them.
Current behavior and validation limits are in `docs/events/008_tensions_rising/overview.md` and [the owner state map](../../../plans/008_tensions_rising_plans/documentation_state_2026-10-05.md).

## Source files

| File | Role |
| --- | --- |
| `events/008_tensions_rising.txt` | hidden root `.1`, batch report `.16`, incidents `.2`-`.10` and `.12`, clash results `.13`-`.15`, Thin Wire `.20`, opinion expiry `.21` |
| `common/scripted_effects/008_tensions_rising_effects.txt` | every helper below |
| `common/scripted_triggers/008_tensions_rising_triggers.txt` | full-tension, peace, availability, evolution, follow-up, actor, posture, and clash triggers |
| `common/script_constants/008_tensions_rising_constants.txt` | all tuning |
| `common/opinion_modifiers/008_tensions_rising_opinion_modifiers.txt` | five timed opinion modifiers |
| `common/ideas/008_tensions_rising_ideas.txt` | four hidden AI posture ideas |
| `common/on_actions/008_tensions_rising_on_actions.txt` | war-relation hook for One Denial and Thin Wire cancellation |

## Helper map

| Helper | Role |
| --- | --- |
| `tensions_rising_prepare_random_event_fire` | automatic availability and manual-force contexts |
| `get_tensions_rising_stage` | Chaos tier to stage, with disabled-stage fallback to baseline |
| `apply_tensions_rising_event_effect` | root controller: stage capture, evolution record, packets, pulse, pairs, posture, follow-up, achievements |
| `apply_tensions_rising_distributed_world_tension` | splits a packet into equal named-threat slices and returns the observed change |
| `apply_tensions_rising_timer_pulse` and `apply_tensions_rising_timer_pressure_to_next_timer` | capped pulse and its read hook in `calculate_next_timer_value` |
| `select_tensions_rising_relation_pairs` and `apply_tensions_rising_relation_pair` | pair choice, stage modifiers, counting flags, One Denial eligibility |
| `apply_tensions_rising_ai_posture` | stage posture idea on selected AI countries |
| `schedule_tensions_rising_followup` and `select_tensions_rising_followup_event` | one follow-up per batch and its pool order |
| `apply_tensions_rising_incident_*` | incident bundles, never recursing into the root effect |
| `try_tensions_rising_incident_border_war` and `select_tensions_rising_border_war_pair` | safe non-transfer clash attempts |
| `update_tensions_rising_achievement_tracking`, `tensions_rising_on_war_relation_added` | achievement tracking |

## Constant blocks

| Block | Tunes |
| --- | --- |
| `tensions_rising_world_tension_gain` | root packets 2/3/5/8/12 and the minimum country slice |
| `tensions_rising_chaos_gain` | root Chaos 10/15/25/50 |
| `tensions_rising_timer_pulse` | pulse strengths, duration bands, extensions, caps |
| `tensions_rising_relation_pairs`, `tensions_rising_opinion_duration_days` | pair counts, selector cooldown, modifier durations |
| `tensions_rising_followup` | follow-up chances, delays, recent-damage window |
| `tensions_rising_incident_*` | incident tension, Chaos, pairs, posture, and clash odds |
| `tensions_rising_border_war_result` | clash outcome effects |
| `tensions_rising_ai_posture` | posture durations and country counts |
| `tensions_rising_achievement` | achievement thresholds and the Thin Wire watch |
| `tensions_rising_reporting` | report scale and the 30-day automatic cadence |

Timed-flag durations that reject constants use file-scoped `@` mirrors in the effects file; keep each mirror equal to its constant.

## State lifecycle

- Persistent: one evolution record per stage and the Last Normal Briefing flag.
- Timed: the pulse expiry, relation counting flags, actor cooldown and One Denial flags, posture ideas, the recent-shock cadence flag, the recent-damage window, and the clash cooldowns.
- Report batch: recipient-country report fields and per-batch flags clear on acknowledgement.
- No global event target outlives its effect chain.

## Remaining source work

Two items affect this map and are listed in the coding prompt: the incident world-tension block must be rescaled below the root ladder, and the relation selector's cooldown-bypassing fallback passes are a recorded limitation with a README proposal.
