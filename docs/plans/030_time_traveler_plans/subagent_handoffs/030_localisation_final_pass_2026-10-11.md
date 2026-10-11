# Event 30 localisation final pass (loc3, 11 Oct 2026)

Scripted change: `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`, `GetEventsLogSelectedEvolutionSummary`. The two Time Traveler rows (stage 1 and 2) returned `concentration_camps.evolution.3.summary`. They now return `time_traveler.evolution.1.summary` and `time_traveler.evolution.2.summary`, which already existed in `localisation/english/030_time_traveler_l_english.yml`. The change reached HEAD inside commit 83f1dba05 because another session committed the whole file.

Text changes: see commits e01f0bdcc and b08a4a664. Four opinion modifiers (`time_traveler_goodwill`, `time_traveler_abduction`, `time_traveler_rejected_offer`, `time_traveler_exposed_cell`) had no localisation and showed raw identifiers. They now have names. Unverified in game.
