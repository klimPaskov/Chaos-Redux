# Event 006 milestone effects

Source: `006_independence_wave_milestone_effects.txt`. Mechanic documentation: `docs/events/006_independence_wave/milestones.md`.

Every milestone effect is idempotent: it checks its own permanent global flag first, so repeated calls from the same transaction do nothing.

## independence_wave_milestone_record_history

Scope: the milestone actor (country).

Inputs: caller-set temporary `independence_wave_milestone_payload_input`; optionally `independence_wave_milestone_secondary_input` (a country id) with `independence_wave_milestone_has_secondary_input` set to one, which the caller must set to zero when there is no secondary actor.

Side effects: appends one Event 006 history row through `record_events_log_system_history_entry` and refreshes the Event Logs views, then zeroes the shared `events_log_system_*` inputs.

## independence_wave_milestone_refresh_country

Scope: the refreshed Event 006 country; called at the end of `independence_wave_achievement_refresh_country_state`.

Fires the broad recognition milestone (treaty-backed recognition) and the one-state major milestone (one-anchor opening, major, not a formed union).

## independence_wave_milestone_record_peaceful_treaty

Scope: the released country; called at the end of `independence_wave_set_host_outcome`.

Fires when the outcome is recognized separation and the living former host is not at war with the country. Writes `global.independence_wave_milestone_treaty_host`.

## independence_wave_milestone_record_host_annexation

Scope: the annexed country (FROM in `on_annex`). Input: event target `independence_wave_achievement_annexer`.

Fires when the annexer is the country's own former host. Writes `global.independence_wave_milestone_annexed_country`; the annexer carries the news and history row.

## independence_wave_milestone_record_regional_formable

Scope: the country that has just formed a union; called from the shared formable commit and the FORM-05 proclamation.

## independence_wave_milestone_record_collective_rescue

Scope: the rescuing member. Input: event target `independence_wave_rescue_member`. Called at the end of `independence_wave_achievement_record_rescue`. Writes `global.independence_wave_milestone_rescued_country`.

## independence_wave_milestone_refresh_league and independence_wave_milestone_publish_cross_regional_league

Scope: any; called at the start of `independence_wave_achievement_refresh_cross_regional_clock`.

Fires when a formal, durable or reformed League has members from `cross_regional_regions` regions. The League leader carries the news, or a random active member when no live leader is recorded.

## independence_wave_milestone_record_radical_bloc

Scope: the country completing DM-58 or DM-59.

## independence_wave_milestone_refresh_survivors

Scope: any; called after `independence_wave_achievement_initialize_committed_wave` in `independence_wave_finalize_frozen_country_origins`.

Counts active entries of `global.independence_wave_active_countries`, writes `global.independence_wave_milestone_survivor_count`, and fires the highest threshold reached.
