# Event 008 Planning Context Digest

This package was built from the user-provided Event 008 rework brief and the uploaded Chaos Redux guidance files.

## User source of truth

- Event ID: `8`
- Event name: `Tensions Rising`
- Type: Minor Repeatable
- Baseline: `+100` world tension, only useful below `100%` world tension in Calm World
- Evolution I: Gathering Storm, `+10 chaos`, `+100` world tension, can fire at `100%` WT
- Evolution II: `+15 chaos`, `+200` world tension
- Evolution III: `+25 chaos`, `+500` world tension
- Evolution IV: `+50 chaos`, `+1000` world tension
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
- `hoi4-decisions-missions.md`
- `hoi4-focus-trees.md`
- subagent TOML files for scripted systems, assets, localisation, completion audit, spreadsheet worker, planner, and related roles
- `chaos_redux_events_catalog.xlsx` for the current row snapshot

## Workbook note

The uploaded catalog workbook still had Event 8 detail text equivalent to `Increase world tension by 5.` The user prompt supersedes that stale row for this source-spec package. The workbook itself was not modified. After implementation, the spreadsheet worker should update it from final in-game localisation and event-detail text.

## Design choices made

- Event 8 stays a global pressure event, not a country/focus/formable event.
- The hidden side effects are concentrated in a capped `Tension Pulse`, timed relation damage, delayed reports, and temporary AI posture pressure.
- Stage IV remains a high-pressure non-terminal event-log/evolution state and does not receive a super-event.
- `Diplomatic Panic` is kept as a small cluster note: for now one member, Event 8, with medium severity.
- Achievements reward rare timing and deep-stage consequences, not merely seeing the popup once.

## Files created

See `README.md` and `package_manifest.md` for the final package file list.
