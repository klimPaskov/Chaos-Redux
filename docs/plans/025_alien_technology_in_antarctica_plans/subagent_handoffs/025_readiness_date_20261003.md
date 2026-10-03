# Event 025 first-readiness date repair, 2026-10-03

Disposition: implemented within the authorized deterministic recovery design.

The previous phase transition assigned a readiness date only to the expedition that advanced the global race phase.
Other expeditions could later submit a tied recovery with a zero date, incorrectly sorting ahead of a dated finalist.
That phase transition also did not prove all final-submission requirements.

Each expedition now records its first actual eligible recovery day independently.
The helper checks the existing progress/readiness/outpost/access thresholds, confirmed site and outpost flags, weather/crew state, participant validity and final phase.
It runs during participant pulses, phase advancement, final-mission preparation, and proof capture.
An existing first-readiness date is retained after deterioration or a later attempt.

Files: common/scripted_effects/025_alien_technology_in_antarctica_lifecycle_effects.txt, common/scripted_effects/025_alien_technology_in_antarctica_runtime_effects.txt, and .tools/test_event025_lifecycle.py.

Two additional source-execution tests cover later expeditions and an unprepared country that cannot claim an early date.
All suites pass: 9 recovery, 12 lifecycle and 4 delayed-callback tests.
Native mission scheduling, live campaign state, and domain MCP acceptance remain separate gates.
No cost, threshold, MTTH parameter, AI weight, route or reward family was changed.
