# Event 17 Manual Target Exclusion Handoff

## Outcome

Event 17 manual triggers can no longer select the requesting country. If no other eligible country exists, the trigger fails closed.

## Implementation

Event Details and Settings manual triggers set the shared manual-dispatch marker around `fire_event_by_temp_id_no_cluster`. The Event 17 route then sets `random_faction_exclude_dispatch_requester` only while `random_faction_prepare_runtime_context` runs. The requester is excluded during pool construction, the weighted array selection, and final target validation. Automatic timer and cluster dispatch do not set the exclusion flag and retain their existing eligible-country pool.

The repair is implemented in `common/scripted_effects/017_random_faction_effects.txt`, `common/scripted_triggers/017_random_faction_triggers.txt`, `common/scripted_effects/chaosx_settings_effects.txt`, and `common/scripted_guis/chaosx_scripted_gui_events_log.txt`.

## Probability Evidence

Declared equal-weight manual fixtures produced a requester probability of zero. With three eligible non-requesters, each received one third; with one eligible non-requester, it received probability one; with none, dispatch selected no country. The matching automatic fixture retained four equal candidates at one quarter each, including the caller when otherwise eligible.

The installed probability adapter cannot normalize the live dynamic temporary-array pool and reports `PROBABILITY_CANDIDATE_POOL_INCOMPLETE`. The declared fixtures and three independent source guards provide the bounded evidence; they are not represented as live runtime simulation.

No fallback target or player-country substitution was introduced.
