# Event 006 shared decision trigger helpers

This file documents the shared package triggers in `006_independence_wave_decision_triggers.txt`.
Package decisions, focuses, and scripted effects call these triggers directly instead of a per-tag copy.

## Cost palettes

| Trigger | Requirement |
| --- | --- |
| `can_pay_independence_wave_administration_light_cost` | Light civilian factory, command power, and manpower reserves. Emergency administration openings for the one-state packages use this palette because their only spare civilian factory pays for founding civil work. |
| `can_pay_independence_wave_administration_standard_cost` | Standard civilian factory, command power, and manpower reserves |
| `can_pay_independence_wave_strategic_cost` | Standard civilian factories, stability, and the standard diplomatic cost |
| `can_pay_independence_wave_strategic_war_support_cost` | The strategic palette plus minor war support |

## Former host and league state

| Trigger | Meaning |
| --- | --- |
| `has_independence_wave_unsettled_host` | No living former host exists, or the former host is at war with the calling country (`PREV` inside the host scope) |
| `has_independence_wave_unsettled_host_root` | No living former host exists, or the former host is at war with `ROOT` |
| `has_independence_wave_live_league_phase` | The global league phase is between regional conferences and the reformed league, the phases in which the shared league-value writer is active |
| `has_independence_wave_formal_league_phase` | The global league phase is formal, durable, or reformed, the phases that hold a ratified charter outside crisis and rival leagues |

All of these run in country scope except the league phase trigger, which reads only global state.
Package actions that promise league-wide values expose the league phase trigger in their availability so the promise is visible while the writer is inert during the informal network phase.
`has_independence_wave_tat_unsettled_host` keeps its own name because it carries a localisation key for its tooltip; its body delegates to `has_independence_wave_unsettled_host_root`.
