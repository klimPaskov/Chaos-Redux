# Event 20 last-response missions

The last-response surface opens only after Evolution V has earned its terminal route. It extends the existing `chaosx_disease_containment_category`; it does not create a new disease category or cure a Black Plague state.

## Hold the Line

`black_plague_shared_start_last_response_hold` is a human-only start decision. The country must still control at least one established, non-rat-controlled Black Plague state, keep the Rat King active, and have the reserved equipment, trains, fuel, manpower, command power, civilian factories, stability, and war support. The start spends 180 support equipment, 90 motorized, 300 infantry equipment, 2 trains, 1,600 fuel, 4,500 manpower, 15 command power, 3 civilian factories, 2% stability, and 3% war support.

The start activates `black_plague_shared_last_response_hold_mission` for 120 days. The event-owned country pulse adds weekly progress for an active war against `RTX`, countermeasure progress at or above 50, and held established states. At 100 progress, terminal preparation falls by 18, countermeasure progress rises by 8, and one held state gains 10 containment. Timeout raises terminal preparation by 14, Rat King Hunger by 6, and incoming exposure by 12 in surviving human-held established states.

## Secure the Refuge

`black_plague_shared_start_last_response_refuge` uses the same human and route gates, but also requires a held established terminal capital, refuge node, or city. It spends 220 support equipment, 120 motorized, 350 infantry equipment, 4 trains, 1,900 fuel, 5,000 manpower, 18 command power, 4 civilian factories, 3% stability, and 4% war support.

The start activates `black_plague_shared_last_response_refuge_mission` for 120 days. Holding the qualifying node adds weekly progress in addition to the war, countermeasure, and held-state terms. At 100 progress, terminal preparation falls by 24, countermeasure progress rises by 10, and the qualifying node gains 14 containment. Timeout raises terminal preparation by 18, Rat King Hunger by 8, and incoming exposure by 16 in surviving human-held established states.

## Runtime and UI contract

Both start decisions and missions are registered in `common/decisions/020_black_plague_shared_response_decisions.txt`. Their costs come from `common/script_constants/020_black_plague_terminal_response_constants.txt`; country gates and cancellation triggers are in `common/scripted_triggers/020_black_plague_terminal_response_triggers.txt`; payment, progress, outcomes, reports, and teardown are in `common/scripted_effects/020_black_plague_terminal_response_effects.txt`. The seven-day response pulse calls the progress effect, while terminal takeover removes both missions idempotently.

Both mission blocks are native `activate_mission`/`days_mission_timeout` declarations in `common/decisions/020_black_plague_shared_response_decisions.txt`; the event-owned pulse supplies progress and the terminal cleanup removes them idempotently. The player-facing decision and mission text is in `localisation/english/020_black_plague_response_l_english.yml`; outcome reports `.66` through `.69` are in `localisation/english/020_black_plague_reports_l_english.yml` and `events/020_black_death.txt`. The existing disease interface displays the projects alongside the rest of the shared category.

## Future extension

Additional last-response narratives can add state-specific reports or new cost packages without changing the mission contract. Any future expansion must keep both projects human-only, preserve the two-tag `RTA`/`RTX` boundary, and retain the no-instant-cure and no-Evolution-V-bypass rules.
