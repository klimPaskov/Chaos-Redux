# Independence Wave generic release AI

Every active Event 006 country that owns the shared `independence_wave_focus_tree` or the reviewed ICE additive carrier receives the additive profiles in `common/ai_strategy/006_independence_wave_generic.txt`. They are deliberately identity-neutral so other events can reuse an Event 006 registry tag without creating a second AI package.

The profiles read the public Event 006 values rather than storing a separate checklist:

- `independence_wave_generic_survival_profile` turns on when capacity is not functioning or instability is severe. It prioritizes army, infantry, support, artillery, trains, infrastructure, capital defense, and strong war restraint.
- `independence_wave_generic_recovery_profile` turns on after functioning capacity and de facto recognition when severe instability or a living former host still demands recovery. It shifts weight toward industry and infrastructure while retaining defensive restraint.
- `independence_wave_generic_consolidation_profile` turns on after functioning capacity, de facto recognition, prepared security, and a non-severe instability band. It raises army and industry priorities and permits limited outward development without forcing a war.

All numeric priorities live in `common/script_constants/006_independence_wave_constants.txt` under `independence_wave_generic_ai`. Package-specific strategy files remain additive and can override the baseline through their own route, regional, patron, host, or signature conditions. No profile creates a faction, starts a war, scans every country, or grants free equipment or divisions.

The profiles are source-level AI wiring. Final scenario weight, timing, and live AI observation remain outside the current non-live scope.
