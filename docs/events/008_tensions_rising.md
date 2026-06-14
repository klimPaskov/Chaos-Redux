# Event 008: Tensions Rising

Event 008 Tensions Rising is a minor repeatable diplomatic-pressure event. In calm campaigns it is a straightforward world-tension incident; once the Chaos Meter reaches evolved tiers, the same report becomes a staged global panic system with direct chaos gain, relation damage, timer pressure, delayed reports, AI posture pressure, achievements, event-log evolution rows, and a one-time non-terminal super-event.

## Runtime Flow

1. `chaosx.nr8.1` fires from the standard repeatable random-event pool. Event 8 remains registered in `global.repeatable_events`.
2. `tensions_rising_prepare_random_event_fire` blocks only the calm-world baseline if world tension is already full. Evolved stages can still fire at full world tension.
3. `get_tensions_rising_stage` maps the current Chaos Meter tier to Stage I-IV. Calm world stays at baseline stage `0`.
4. Baseline firings add `+10` world tension and update the global highest-world-tension tracker.
5. Evolved firings record the current Diplomatic Fever milestone if it has not already been logged, add the staged world-tension and chaos packet, apply the temporary timer pulse, select timed relation-shock pairs, apply AI posture ideas, schedule one delayed report, update achievement tracking, and trigger the Stage IV super-event if it has not already appeared.

## Stage Values

| Stage | Chaos gate | World tension | Chaos | Notes |
| --- | --- | ---: | ---: | --- |
| Baseline | Calm World | `+10` | `0` | blocked at full world tension |
| Stage I | Gathering Storm | `+10` | `+10` | light relation and timer pressure |
| Stage II | Rising Chaos | `+20` | `+15` | broader relation shocks and delayed reports |
| Stage III | Chaos Tier | `+50` | `+25` | heavy relation pressure and Thin Wire tracking |
| Stage IV | Totalen Chaos | `+100` | `+50` | strongest pressure and first-fire super-event |

The world tension trigger uses HOI4's documented `0-1` `threat` scale. The full-tension gate is centralized as `constant:tensions_rising_gate.full_world_tension`.

## Timer Pulse

The evolved Tension Pulse uses `tensions_rising_timer_pulse_active`, `global.tensions_rising_timer_pulse_strength`, and `global.tensions_rising_timer_pulse_days`. Stronger stages replace weaker active pulses. Equal-stage repeats add only the stage extension amount to the duration budget and clamp it to the stage cap before refreshing the timed flag. The event timer reads the active strength in `calculate_next_timer_value` through `apply_tensions_rising_timer_pressure_to_next_timer`, so no new daily, weekly, or monthly global loop is introduced.

## Diplomatic Shocks

Stage I-IV firings select a small number of country pairs through `select_tensions_rising_relation_pairs`. Selection prefers major or faction-leader actors, avoids capitulated, subject, zombie-outbreak, and recent relation actors, and avoids direct war opponents. Relation modifiers are timed through the existing opinion system:

- Stage I: `tensions_rising_leaked_cables`
- Stage II: `tensions_rising_mobilization_suspicion`
- Stage III: `tensions_rising_border_alarm`
- Stage IV: `tensions_rising_permanent_alert` for twelve months

The global active-opinion counter is decremented by the hidden expiry event `chaosx.nr8.21`, which supports the Diplomatic Blackout achievement without making the opinion modifiers permanent.

## Delayed Reports

Evolved firings can schedule one delayed report from `chaosx.nr8.2` through `chaosx.nr8.12`. These reports describe cable traffic, embassy side doors, calm-map denial, neutral insurance rates, rumours, staff cars, fleet silence, border lamps, and the final normal briefing. They do not recurse into the main event effect and do not create direct war goals.

## AI Posture

AI posture hooks apply short timed national spirits to selected AI countries that are majors, faction leaders, or already at war:

- `tensions_rising_cautious_alignment`
- `tensions_rising_alarmist_rearmament`
- `tensions_rising_general_staff_fever`
- `tensions_rising_permanent_alert`

These ideas nudge diplomacy, readiness, and defensive behavior without creating war goals, new countries, cores, focus trees, or formables.

## Event Log and Cluster

The event-log detail body is `chaosx.events_log.window.event_details.tensions_rising`. The Diplomatic Fever evolution type uses `constant:tensions_rising_event_log.evolution_type`, records one milestone for each reached stage, and exposes stage title/body text through the history, evolution view, event-detail preview, and selected-evolution panes.

`Diplomatic Panic` is registered as repeatable event cluster `constant:event_cluster_id.diplomatic_panic`. Its current member list is intentionally small: Event 8 is the required member with medium danger and a Tier II minimum. Cluster history and settings surfaces use `chaosx.event_cluster.diplomatic_panic.name` and `chaosx.events_log.window.cluster_details.description.diplomatic_panic`.

## Super-Event

Stage IV can trigger the one-time non-terminal super-event `The Red Line Disappears`.

- Super-event slot: `62`
- Image sprite: `GFX_super_event_tensions_red_line`
- Image file: `gfx/super_events/super_event_tensions_red_line.dds`
- Music file: `music/super_event_008_red_line_disappears.ogg`
- Sound-channel file: `sound/chaosx_super_event_008_red_line_disappears.wav`
- Sound definition: `chaosx_super_event_008_red_line_disappears_track`
- Quote/title/description scripted localisation: `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`

The branch sets `tensions_rising_stage_4_super_event_seen` and does not set `world_end`.

## Achievements

Event 008 adds six achievements:

- `achievement_tensions_thin_wire`: remain at peace through the Stage III+ full-world-tension watch.
- `achievement_tensions_only_headlines`: see three Stage II+ Event 8 firings while the world has no active wars.
- `achievement_tensions_insurance_market`: receive the insurance follow-up while at peace with at least `30` convoys.
- `achievement_tensions_red_line`: witness the first Stage IV super-event before any world-end scenario is active.
- `achievement_tensions_one_denial`: receive the denial follow-up during the active relation-damage window.
- `achievement_tensions_blackout`: have at least ten active Event 8 timed opinion modifiers at once.

Achievement icons are generated final DDS triplets under `gfx/achievements/` and are registered in `interface/chaosx_achievements.gfx`.

## Assets

- Report image: `GFX_report_event_tensions_rising`, backed by `gfx/event_pictures/report_event_tensions_rising.dds`
- News image: `GFX_news_event_tensions_red_line`, backed by `gfx/event_pictures/news_event_tensions_red_line.dds`
- Super-event image: `GFX_super_event_tensions_red_line`, backed by `gfx/super_events/super_event_tensions_red_line.dds`
- Achievement source, processed PNGs, contact sheet, and DDS manifest: `docs/assets/008_tensions_rising/`
- Super-event audio source and attribution: `docs/super_events/008_tensions_rising_super_event_research.md` and `docs/super_events/super_event_audio_packages.md`

## Boundary Rules

Event 008 does not add direct war goals, declare wars, create countries, load focus trees, add cores, create formables, or start a world-end scenario. Its pressure stays indirect: world tension, chaos, temporary timer compression, timed opinion damage, delayed reports, AI posture ideas, event-log milestones, cluster history, achievements, and the non-terminal Stage IV super-event.

## Future Plans

- Add pair-specific named follow-up reports only if the event-log UI later supports short-lived relation-pair references cleanly.
- Consider adding a generic relation-pair helper if other event families need the same timed diplomatic-shock pattern.
- Expand Diplomatic Panic with additional fully implemented diplomatic incidents only after they have their own localisation, event-log detail, and cooldown behavior.
