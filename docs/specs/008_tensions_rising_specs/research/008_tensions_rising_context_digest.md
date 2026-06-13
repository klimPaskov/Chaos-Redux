# Event 008 Planning Context Digest

This package was built from the user-provided Event 008 rework brief and the uploaded Chaos Redux guidance files.

## User source of truth

- Event ID: `8`
- Event name: `Tensions Rising`
- Type: Minor Repeatable
- Baseline: `+10` world tension, only useful below `100%` world tension in Calm World
- Evolution I: Gathering Storm, `+10 chaos`, `+10` world tension, can fire at `100%` WT
- Evolution II: `+15 chaos`, `+20` world tension
- Evolution III: `+25 chaos`, `+50` world tension
- Evolution IV: `+50 chaos`, `+100` world tension
- Creative hidden effects requested: temporary auto-event timer boost, worsening relations between random countries, delayed news/flavour events
- No world-end scenario

## Uploaded context read

- `AGENTS.md`
- `CHAOS_REDUX_MECHANICS.md`
- `chaos-redux-events.md`
- `chaos-redux-event-planning.md`
- `chaos-redux-improvement-loop.md`
- `chaos-redux-subagents.md`
- `chaos-redux-event-assets.md`
- `chaos-redux-super-events.md`
- `hoi4-decisions-missions.md`
- `hoi4-focus-trees.md`
- subagent TOML files for scripted systems, assets, localisation, completion audit, spreadsheet worker, planner, and related roles
- `chaos_redux_events_catalog.xlsx` for the current row snapshot

## Workbook note

The uploaded catalog workbook still had Event 8 detail text equivalent to `Increase world tension by 5.` The user prompt supersedes that stale row for this source-spec package. The workbook itself was not modified. After implementation, the spreadsheet worker should update it from final in-game localisation and event-detail text.

## Design choices made

- Event 8 stays a global pressure event, not a country/focus/formable event.
- The hidden side effects are concentrated in a capped `Tension Pulse`, timed relation damage, delayed reports, and temporary AI posture pressure.
- Stage IV receives one optional/required-if-accepted non-terminal super-event because evolved minor events can deserve super-event treatment when they become globally significant.
- A proposed `Diplomatic Panic` cluster is included as an implementation-ready expansion, but it can be queued if the implementation pass is constrained.
- Achievements reward rare timing and deep-stage consequences, not merely seeing the popup once.

## Files created

See `README.md` and `package_manifest.md` for the final package file list.
