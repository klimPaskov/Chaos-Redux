# Event 006 world milestones

## What it is

Ten once-per-campaign news events mark the turning points of the independence wave, as listed under Rare milestone events in Part 2.
Each fires from the transaction that proves it, never from a scan, sets a permanent global flag, records an Event 006 history row in the Event Logs, and sends a major news event to every country.
The danger milestone (super-event 24) and the first League congress news (`chaosx.nr6.35`) remain separate and unchanged.

## Event map

| News | Milestone | Fired from | Global flag | History payload |
| --- | --- | --- | --- | --- |
| `chaosx.nr6.190` A New State Takes Its Seat | first country with treaty-backed recognition (60) | state refresh, through `independence_wave_achievement_refresh_country_state` | `independence_wave_milestone_broad_recognition` | 40 |
| `.191` Separation by Treaty | first recognized separation while not at war with the former host | `independence_wave_set_host_outcome` | `independence_wave_milestone_peaceful_treaty` | 41 |
| `.192` The Old Flag Returns | first active country annexed by its own former host | `on_annex` in `006_independence_wave_achievement_on_actions.txt` | `independence_wave_milestone_host_annexation` | 42 |
| `.193` A Union Is Proclaimed | first completed regional formable | `independence_wave_formable_commit_selected_family` and the FORM-05 proclamation | `independence_wave_milestone_regional_formable` | 43 |
| `.194` The League Answers a Call | first DM-44 rescue of a League member | `independence_wave_achievement_record_rescue` | `independence_wave_milestone_collective_rescue` | 44 |
| `.195` A League Across Continents | first formal, durable or reformed League with members from at least three regions | `independence_wave_achievement_refresh_cross_regional_clock`, run with every League value change | `independence_wave_milestone_cross_regional_league` | 45 |
| `.196` The Radical Bloc | first DM-58 coordinated reclamation fronts or DM-59 radical charter | the two decision completions | `independence_wave_milestone_radical_bloc` | 46 |
| `.197` The Tenth Flag | ten live Event 006 countries at once | `independence_wave_finalize_frozen_country_origins` after a successful wave commit | `independence_wave_milestone_ten_survivors` | 47 |
| `.198` The Twenty-Fifth Flag | twenty-five live Event 006 countries at once | same | `independence_wave_milestone_twenty_five_survivors` | 48 |
| `.199` From One Province to a Great Power | a country that opened with one anchor state becomes a major, unless it formed a union | state refresh | `independence_wave_milestone_one_state_major` | 49 |

When one wave crosses both survivor thresholds, only the twenty-five news is sent and the ten milestone is recorded as passed.
The survivor count walks only the bounded active-country registry and counts entries that are still active origins.

## Actors and history

The milestone actor carries the news (FROM in the news text) and is the history row actor: the recognized country, the released country of the treaty, the annexing former host, the new union, the rescuing member, the League leader (or a random active member when no leader is recorded), the bloc leader, a random active country for the survivor counts, and the new major.
The treaty host, the annexed country and the rescued member are stored in `global.independence_wave_milestone_treaty_host`, `global.independence_wave_milestone_annexed_country` and `global.independence_wave_milestone_rescued_country` for the news text, and are written as the history row's secondary actor.
The Event Logs history detail shows one sentence per milestone through new payload branches in `chaosx_scripted_localisation_events_log.txt`.

## AI

Statehood incident AI reads the milestone flags: after the first host annexation, security answers are twice as likely; after the first rescue, sending arms to a League member; after the first broad recognition, paying for a full diplomatic reception or lobbying; after the first peaceful treaty, the conciliatory host answers; after the first radical bloc, the motion for collective war; after the first union, the neutral union flag and equal congress seats.

## Assets

All pictures are registered news pictures: vanilla `GFX_news_event_generic_sign_treaty1`, `_generic_handshake`, `_soldiers_marching`, `_generic_rally`, `_generic_lend_lease`, `_generic_rally2`, `_generic_parliament`, `_generic_rally_3`, `_generic_army`, and the Event 006 `GFX_news_event_006_asset_004_league_congress`.

## Files

- `events/006_independence_wave_milestone_events.txt`
- `common/scripted_effects/006_independence_wave_milestone_effects.txt` and `.md`
- `common/script_constants/006_independence_wave_milestone_constants.txt`
- `localisation/english/006_independence_wave_milestones_l_english.yml`

## Limitations

- Achievement proofs are unchanged. The milestone hooks run in the same transactions as the matching achievement proofs, so the news and the achievement record the same events, but no achievement requires a milestone flag.
- Super-event thresholds do not read the milestone flags yet.

## Future expansion

- Let foreign governments react to the first host annexation and the first radical bloc through the foreign-reaction contract.
- Give the first union and the first great power a short follow-up decision for neighbouring Event 006 countries.
