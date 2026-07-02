# Event 013 completion audit resolution

## Resolved in implementation

- Public API expanded from family-only direct calls to state, country, regional-seed, and world calls with persisted target mode, report policy, recovery permission, deaths permission, super-event permission, total pulse override, and delay override.
- Family target selection now validates against `natural_disaster_target_current_family`; invalid exact/country/regional calls do not fall back to generic unrelated states.
- Report policy is throttled by profile and policy. Direct calls report by default; baseline and Evolution I keep early/important reports; Evolution II, Evolution III, and SCN-007 report only first, player, major, capital, severe, or abnormal hits unless a caller forces another policy.
- First meaningful disaster-specific news bypasses the global news cooldown once, so a scenario or abnormal headline cannot suppress the player's first family-specific world report. Later family news remains throttled. Family headlines carry the affected state as a regular event target into immediate human-country delivery, avoiding a shared delayed global news target.
- Baseline, Evolution I, Evolution II, Evolution III, and SCN-007 pulse/delay bands now match the source spec matrix.
- Dynamic pulse and report delays are emitted through meta effects, so event and timed-flag `days` fields receive concrete integers instead of variable tokens.
- Evolution Event Log detail records are gated behind `is_current_evolution_enabled`, while the display variables are still prepared before the gate for the shared details window.
- Random family pools now include all twenty non-abnormal families before Evolution III, while Evolution III and Disaster Barrage include all twenty-four families.
- Dry mass movement, wet mass movement, avalanche, glacial outburst, sinkhole, and limnic eruption now have separate damage and aftermath modifier paths.
- Moving storm corridors now mark an impact state and neighboring path states for GUI visibility and evacuation, and follow-up hazards use the original impact state as a regional seed.
- Recovery decisions now set response flags that reduce later death percentages during follow-up or warning-state hits, and AI weights react to family, capital, war, population, and abnormal/severe conditions.
- The scripted GUI now includes a compact four-slot operations board for active aftermath and warning states. It reuses Event 013 state flags, AI priority, global event targets with cleanup, and the existing concrete recovery effects for action buttons.
- The documented super-event audio handoff path now exists, and the meteor quote verification caveat is documented as accepted evidence for current wiring.

## Architecture notes

- Report events use reusable sequence-slot events so individual disasters inside a season do not create separate Event Log entries. Family identity, report priority, news eligibility, and localisation are resolved dynamically; registered art supports report, news, decision, and super-event surfaces.
- Event 046 and Event 099 remain reserved placeholders after their logic is integrated into Event 013.
- Event 051 Heat Wave remains separate, and Event 013 heat targeting continues to avoid its active `heat_wave` idea.
