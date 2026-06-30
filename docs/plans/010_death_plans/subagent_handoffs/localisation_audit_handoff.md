# Event 010 Death Localisation Audit Handoff

Date: 2026-06-15

Role: Chaos Redux localisation subagent

## Scope

Audited Event 010 Death localisation and scripted localisation without relying on parent context.

Primary files inspected:

- `localisation/english/010_death_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`
- `localisation/english/chaosx_event_names_l_english.yml`
- `localisation/english/chaosx_achievements_l_english.yml`
- `localisation/english/chaosx_ideas_l_english.yml`
- `localisation/english/chaosx_music_l_english.yml`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_scenarios.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_debug.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_chaos_meter.txt`
- Event/decision/focus/idea/achievement ids touching Death.

Repo instructions and skills used:

- `AGENTS.md`
- `chaos-redux-events`
- `hoi4-decisions-missions`
- `hoi4-focus-trees`
- `chaos-redux-super-events`
- `chaos-redux-improvement-loop`
- `chaos-redux-subagents`

Required local references consulted:

- Offline wiki: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding, Scripted GUI modding, Interface modding, Achievement modding, Music modding, Sound modding.
- Vanilla docs/examples: `documentation/loc_formatter_documentation.md`, `documentation/loc_objects_documentation.md`, `common/scripted_localisation/00_scripted_localisation.txt`, `common/decisions/_documentation.md`, `common/scripted_guis/_documentation.md`.

## Patch Applied

Tiny unambiguous fix made during audit:

- `common/scripted_localisation/chaosx_scripted_localisation_chaos_meter.txt`
  - Added `constant:chaos_meter_deaths_reason.death_consumption` dispatch to `GetChaosMeterDeathsSelectedCause`.
  - Added `constant:chaos_meter_deaths_reason.death_consumption` dispatch to `GetChaosMeterDeathsDetailCause`.
- `localisation/english/chaosx_chaos_meter_l_english.yml`
  - Added `chaos_meter.deaths.cause.death_consumption: "Death consumption"`.

Before:

- Death-consumption rows had a breakdown tooltip line, but the selected/latest row and detailed history rows displayed cause `Unknown`.

After:

- Death-consumption selected/latest rows and detailed history rows display `Death consumption`.

Note: both touched files already had related uncommitted working-tree changes before this audit, including the Death-consumption tooltip line and tooltip body wiring. This patch only adds the missing selected/detail cause display.

## Missing Key List

No confirmed missing player-facing Death keys found in the audited active surfaces.

Key coverage confirmed:

- Event ids: `chaosx.nr10.1.t`, `chaosx.nr10.2.t`, `chaosx.nr10.2.d`, `chaosx.nr10.2.a`, `chaosx.nr10.3.t`, `chaosx.nr10.3.d`, `chaosx.nr10.3.a`, `chaosx.nr10.10.t`.
- Decisions/categories/custom cost/custom tooltip keys in `common/decisions/010_death_decisions.txt` and `common/decisions/categories/010_death_categories.txt`.
- Focus tree key `death_focus_tree` and all focus title/desc keys in `common/national_focus/010_death_focus_tree.txt`.
- Death ideas in `common/ideas/chaosx_ideas.txt`.
- Death achievements in `common/achievements/chaos_redux_achievements.txt`.
- Super-event keys `chaosx_super_event.62` through `chaosx_super_event.65` title/quote/button/description.
- Music display keys `chaosx_super_event_62_*` through `chaosx_super_event_65_*`.

Expected non-issues:

- `chaosx.nr10.1` and `chaosx.nr10.10` are hidden events and do not require visible desc/option keys.
- `chaosx.scenarios.entry.id.death: "#006"` is the triggerable scenario number, not the Event 010 number, and matches the scenario handoff convention.

## Duplicate Key List

No duplicate keys found across the targeted English localisation files:

- `010_death_l_english.yml`
- `chaosx_gui_l_english.yml`
- `chaosx_event_names_l_english.yml`
- `chaosx_achievements_l_english.yml`
- `chaosx_ideas_l_english.yml`
- `chaosx_music_l_english.yml`
- `chaosx_chaos_meter_l_english.yml`

## Scripted Localisation Issues

Fixed:

- `common/scripted_localisation/chaosx_scripted_localisation_chaos_meter.txt`
  - Death-consumption cause was not dispatched in selected/detail death-row labels.

Confirmed wired:

- Event log event-name mapping for Event 10 resolves to `chaosx.event_name.10`.
- Event details mapping for Death resolves to `chaosx.events_log.window.event_details.death`.
- Death evolution title/body dispatches exist for selected, history, and event-detail contexts.
- Super-event slots 62-65 dispatch image/title/quote/button/description keys.
- Scenario scripted localisation dispatches Death scenario name/desc/type/impact keys.

Potential scripted-localisation risk:

- Generic event-log placeholder dispatches still exist in `chaosx_scripted_localisation_events_log.txt`, but Death has specific event and evolution detail dispatches, so the Death surfaces should not fall through to placeholder text.

## Reveal and Spoiler Findings

These were not patched because they affect player-facing reveal policy and may need parent design approval.

Pre-mainland decision text reveals Death:

- `localisation/english/010_death_l_english.yml`
  - `death_send_survey_boat_tt` says the early survey can force war "if Death can be found".
  - `death_quiet_quarantine_notice_tt` says it lowers "Death spread pressure before public reveal".
  - `death_file_under_weather_tt` says "Death spread pressure increases".

Recommendation:

- Before public mainland reveal, reword these to use "the source", "the island pattern", "the silence", or "spread pressure" without naming Death.

Achievement text is spoiler-heavy if achievements are visible from game start:

- `localisation/english/chaosx_achievements_l_english.yml`
  - `death_no_one_heard_the_first_boat_DESC`
  - `death_no_one_heard_the_first_boat_tooltip`
  - `death_last_ferry_DESC`
  - `death_last_ferry_tooltip`
  - `death_counted_every_name_DESC`
  - `death_before_the_name_DESC`
  - `death_before_the_name_tooltip`

Recommendation:

- If achievements are visible before Event 010 fires, either accept this as a meta spoiler surface or rename/describe pre-reveal achievements obliquely until the system supports dynamic hidden achievement text.

Event details and evolution details reveal the full Death arc if visible before discovery:

- `localisation/english/chaosx_gui_l_english.yml`
  - `chaosx.events_log.window.event_details.death`
  - `chaosx.events_log.window.evolution_details.death.body.event_detail`
  - `chaosx.events_log.window.evolution_details.death.body.stage_1` through `.stage_5`

Recommendation:

- Confirm the event details window hides Event 010 details until discovered/fired. If not, add a gated pre-reveal detail string or hide the entry until `death_public_reveal`/equivalent state.

Scenario picker text intentionally reveals Death:

- `localisation/english/chaosx_gui_l_english.yml`
  - `chaosx.scenarios.death.*`

Recommendation:

- Treat this as acceptable only if triggerable scenarios are an explicit debug/manual-start surface. If the scenario picker is player-facing in normal play, it conflicts with "do not reveal Death before mainland reveal".

## Old Spirit, War-Peace, Placeholder, and Planning Wording

No active Event 010 player-facing references found for:

- `Spirit of War`
- `Spirit of Peace`
- `War or Peace`
- `war_or_peace`
- `010_war_or_peace`
- `Dark Methods`
- `Black Oath`
- planning role labels
- implementation-history wording tied to Death

Remaining placeholder hits are generic framework/UI placeholders, not Death-specific:

- `chaosx.events_log.window.event_details.entry_placeholder.generic`
- `chaosx.events_log.window.evolution_details.placeholder.generic`
- `events_log_event_detail_entry_placeholder`

Risk:

- Those placeholder keys are player-facing if any event/evolution lacks a specific dispatch. Death does not currently rely on them.

## Super-Event Title, Quote, Button, and Music Finality

Confirmed present and final-looking:

- `chaosx_super_event.62`: `His Name Was Death`
- `chaosx_super_event.63`: `No More Life`
- `chaosx_super_event.64`: `The Unfinished Work`
- `chaosx_super_event.65`: `There Was No Man`

Scripted dispatch and music display keys exist for all four super-event slots.

Asset/text naming note:

- Slot 64 image scripted localisation uses `GFX_super_event_death_defeat`, and the sprite points to `gfx/super_events/010_death/super_event_death_defeat_aftermath.dds`. Text/audio/music use the "defeat aftermath" meaning. This is functionally wired, but the sprite name is less explicit than the asset/audio names.

Uncertainty:

- I did not re-research quote attribution externally. This audit only checked that quote/button/title/description keys are present, non-placeholder, and wired.

## Dynamic Text Opportunities

Recommended improvements:

- Decision cost strings in `010_death_l_english.yml` are static resource lists without amounts:
  - `death_survey_boat_cost_text`
  - `death_telegraph_cost_text`
  - `death_quiet_quarantine_cost_text`
  - `death_recognize_war_cost_text`
  - `death_call_compact_cost_text`
  - `death_join_compact_cost_text`
  - `death_patrol_cost_text`
  - `death_wasteland_gear_cost_text`
  - `death_share_gear_cost_text`
  - `death_port_lit_cost_text`
  - `death_dead_zone_outpost_cost_text`
  - `death_black_census_cost_text`

- Event detail text hardcodes thresholds that appear to have script constants:
  - "more than 100,000 people" in `chaosx.events_log.window.event_details.death`
  - "Chaos is beyond 1000" in `chaosx.events_log.window.evolution_details.death.body.stage_4`

Recommendation:

- Add scripted localisation or scripted GUI value helpers so the event details and decision cost text read from the same constants/variables as the gameplay.

## Cross-Surface Mismatch Notes

- Event 010 active localisation has replaced the old Spirit of War/Peace naming on the audited player-facing surfaces.
- Death event name, scenario name, super-event titles, achievement family, ideas, event details, and music display keys consistently use Death.
- Main mismatch is reveal timing, not naming: early decisions, achievements, scenario picker, and event details can expose Death before the mainland reveal if those surfaces are visible.
- `chaosx.scenarios.entry.id.death: "#006"` looks inconsistent with Event 010 at first glance, but appears to be the scenario catalog id and should remain unless the scenario system is renumbered.

## File Encoding Concerns

No encoding concern found in the targeted localisation files. All checked files start with UTF-8 BOM:

- `localisation/english/010_death_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`
- `localisation/english/chaosx_event_names_l_english.yml`
- `localisation/english/chaosx_achievements_l_english.yml`
- `localisation/english/chaosx_ideas_l_english.yml`
- `localisation/english/chaosx_music_l_english.yml`
- `localisation/english/chaosx_chaos_meter_l_english.yml`

## Recommended Fixes

High priority:

- Reword pre-reveal decision text in `localisation/english/010_death_l_english.yml`:
  - `death_send_survey_boat_tt`
  - `death_quiet_quarantine_notice_tt`
  - `death_file_under_weather_tt`

- Decide spoiler policy for achievements in `localisation/english/chaosx_achievements_l_english.yml`:
  - If visible from game start, obfuscate pre-reveal Death names.
  - If hidden until conditions/reveal, current wording is acceptable.

- Confirm event log/detail visibility before reveal:
  - If visible early, gate or obfuscate `chaosx.events_log.window.event_details.death` and Death evolution detail body keys in `localisation/english/chaosx_gui_l_english.yml`.

Medium priority:

- Add dynamic value/cost localisation for Event 010 decision costs and threshold text.

Low priority:

- Consider renaming internal sprite `GFX_super_event_death_defeat` to a more explicit defeat-aftermath name only if the parent is already touching super-event assets/scripts. It is currently functionally wired.

## Validation Run

Meaningful checks run:

- Targeted UTF-8 BOM check across the audited Death and related English localisation files.
- Targeted duplicate-key check across the audited English localisation files.
- Targeted key coverage pass for Event 010 events, decisions, focuses, ideas, achievements, super-events, music names, event log, scenarios, and Death-related scripted localisation dispatches.
- Active-surface search for old Spirit/War-Peace names, `Dark Methods`, `Black Oath`, planning/update wording, and placeholder fallthrough risks.
- Manual inspection of Death super-event scripted localisation slots 62-65 and music display keys.
- Manual inspection of Death event/decision/focus/idea/achievement ids.

Validation result:

- No confirmed missing Death player-facing keys.
- No duplicates in the targeted localisation files.
- All targeted localisation files preserve UTF-8 BOM.
- One scripted-localisation display bug found and patched: Death-consumption causes now resolve outside tooltip breakdowns.

Skipped validation:

- No in-game validation was run.
- No external quote/source research was performed.
- No broad wording patch was made for reveal timing because the correct spoiler policy needs parent confirmation.

## Risks and Unresolved Decisions

- Biggest unresolved risk: Death is named before mainland reveal in some player-facing text if those decision/achievement/event-log/scenario surfaces are visible early.
- Achievement spoiler handling needs a design decision because achievements are often global/meta UI and may not support dynamic concealment cleanly.
- Event details spoiler handling depends on whether the Event Details UI is hidden until the event is discovered.
- Static cost/threshold text can drift from gameplay constants.
- Existing generic placeholder keys remain in the framework and are still player-facing for any event without specific dispatch, though Death itself is covered.

## Handoff Path

`docs/plans/010_death_plans/subagent_handoffs/localisation_audit_handoff.md`
