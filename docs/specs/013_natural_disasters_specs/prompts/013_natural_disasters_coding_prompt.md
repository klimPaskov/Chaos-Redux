# Coding Prompt for Event 013 Natural Disasters

Implement Event 013 according to all five spec files in `docs/specs/013_natural_disasters_specs/` or this extracted package. Follow `AGENTS.md`, `chaos-redux-events`, `chaos-redux-event-planning`, `hoi4-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-frame-animation`, `chaos-redux-super-events`, `chaos-redux-subagents`, and relevant HOI4 references.

## Must implement

- Event 013 as a minor repeatable disaster season.
- One Event 013 firing creates one Event Log row, even when the season contains multiple disaster pulses.
- Delayed disaster pulses, with baseline five to ten day delays and compressed delays for larger seasons.
- Unique disaster family mechanics for earthquakes, floods, tropical cyclones, thunderstorms, hailstorms, extreme winds, wildfires, drought, sand and dust storms, blizzards, heat waves, cold waves, dry and wet mass movements, volcanic eruptions, tsunamis, meteor showers, global rupture, massive eruptions, and storm corridors.
- Building damage and real population loss through the Deaths system.
- Disaster reports and news digests that identify affected areas without spamming Evolution II global seasons.
- Disaster Response and Reconstruction decisions and missions with concrete costs beyond political power.
- Reusable scripted effects and triggers so other events can call individual disaster families cleanly.
- Disaster Barrage scenario SCN-007 using the same sequence controller.
- Special Natural Disasters cluster behavior with several delayed Event 013 member seasons and higher chaos unlocks.
- Evolution I, Evolution II, and Evolution III exactly as mapped.
- Evolution III super-event thresholds for meteor shower, global rupture, massive eruption, and moving storm corridor.
- Scripted GUI and animated asset handoff for the moving storm corridor and abnormal disaster map.
- Event 046 Earth Earthquake converted to placeholder after its concept is integrated as global rupture.
- Event 099 Sandstorm converted to placeholder after sand and dust behavior is owned by Event 013.
- Event 051 Heat Wave remains separate and Event 013 heat-wave modifiers must not stack with it.
- Achievements, assets, localisation, docs, and spreadsheet alignment after final localisation exists.

## Text and research

Planning files provide direction only. Write final event, report, news, decision, mission, GUI, achievement, event-detail, and spreadsheet-facing text during implementation. Do not paste working labels as localisation.

Super-event titles, button text, quotes, cultural remarks, and audio are blockers until researched through `chaos-redux-super-events` and documented. Do not use placeholder audio or generated tone tracks as final.

## Validation

Before claiming completion, run task-specific checks proving delayed pulses, one Event Log entry per sequence, Deaths integration, family-specific damage, report throttling, recovery cleanup, direct API calls, scenario launch, cluster launch, heat-wave non-stacking, placeholder conversion for Events 046 and 099, abnormal GUI state, and super-event research or blockers.

Report every simplification, omission, placeholder, missing asset, missing AI behavior, missing localisation, missing GUI animation, or skipped validation. Do not claim completion while any mapped requirement is missing.
