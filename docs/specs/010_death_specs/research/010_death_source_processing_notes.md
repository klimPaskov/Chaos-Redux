# Event 010 Death — Source Processing Notes

This is a planning/source note, not a gameplay spec.

## User-provided design constraints processed

- Event ID 10 is renamed/reworked into `Death`.
- `Spirit of War Peace` is obsolete and should be deleted entirely.
- Death appears quietly on a random remote small ocean island.
- Country name is `Death`, leader is `Zol`, map color is complete black.
- Death has no starting units and should look peaceful/inactive at first.
- The world should not receive an initial notification.
- Delayed reports months later mention disappearances or missing island contact without naming Death.
- Every state controlled/consumed by Death becomes a wasteland: industry deleted, population set to zero, deaths recorded, strategic value removed, attrition/movement/strength-loss hazards, dark/foggy visual if possible, Death cores states.
- Death should consume low-population areas first, then islands, then mainland.
- Reveal occurs when a mainland state over 100,000 population is consumed.
- After reveal, Death can wither neighboring undefended states and declares war on neighbors.
- Coastal jump recovery exists with cooldown if Death is pushed back.
- Ghost divisions unlock around 600 tier, strengthen around 800, and become aggressive/infantry-equivalent at world-end.
- World-end starts when Death consumes an entire continent and Chaos is above 1000; then it creates footholds on all continents.
- Whole-world consumption gets a super-event and achievement.
- Player response systems include special decisions, coalition/faction/compact, containment, dark necromancy, and joining Death.

## Project files processed

- `AGENTS.md`
- `CHAOS_REDUX_MECHANICS.md`
- `chaos-redux-event-planning.md`
- `chaos-redux-events.md`
- `chaos-redux-subagents.md`
- `chaos-redux-improvement-loop.md`
- `chaos-redux-event-assets.md`
- `chaos-redux-frame-animation.md`
- `chaos-redux-super-events.md`
- `hoi4-focus-trees.md`
- `hoi4-decisions-missions.md`
- Subagent TOML files for repo exploration, scripted-system architecture, decisions/missions, country package, localisation, completion audit, spreadsheet worker, generated art, icon art, super-event text, super-event audio, sourced assets, focus audit, documentation curation, and improvement-loop planning.
- `chaos_redux_events_catalog.xlsx`, sheet `Main Sheet`, row ID 10. The row currently lists `Spirit of War/Peace`, details `Random country gets options to either be a symbol of war or a symbol of peace.`, type `Minor Fire-Once`, status `To Be Reworked`, and no cluster fields.

## Planning decisions made

- Death remains `Minor Fire-Once` with no event cluster.
- Ordinary crisis stages are separated from evolutions. Island origin/spread/mainland reveal are baseline stages; Empty Shoreline Whispers, The Inland Smell, First Ghost Muster, Black Tide Recovery, and a world-end-readiness milestone are evolution/mutation milestones. Exact super-event titles remain research-owned.
- Death uses consumed population as its main scaling source rather than normal manpower or industry.
- Death itself does not receive normal politics. A fixed-purpose branch/progression tree is specified for method, shroud, hunger, census, wasteland, coastal recovery, ghosts, and endgame.
- The Living Containment Compact is preferred over always forcing a new faction, because it can coexist with existing alliance structures.
- Dark Methods and Black Oath are specified as optional but must be fully implemented or fully hidden/queued. Half-visible placeholders are explicitly forbidden.
- The Black Atlas UI is recommended after reveal because it clarifies a living map threat. Animated state assets are specified with static fallbacks and frame-sheet requirements.

## Items intentionally left for implementation or specialist subagents

- Exact state IDs/state groups for island-origin and continent-consumed checks.
- Exact scripted effect/trigger names and script constant categories.
- Exact super-event quotes and cultural remarks; these require verified research.
- Exact super-event audio tracks; these require license verification and conversion.
- Final generated assets and DDS/TGA conversion.
- Exact tag conflict check for `DTH`.
- Exact engine-supported method for dark/foggy state visuals and strength-loss pulses.
