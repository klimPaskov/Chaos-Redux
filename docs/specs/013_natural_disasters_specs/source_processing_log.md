
# Source processing log

This log records the inputs inspected before the package was written.

## Uploaded project files inspected

- `AGENTS.md`
- `CHAOS_REDUX_MECHANICS.md`
- `chaos-redux-events.md`
- `chaos-redux-event-planning.md`
- `chaos-redux-event-assets.md`
- `chaos-redux-frame-animation.md`
- `chaos-redux-super-events.md`
- `chaos-redux-improvement-loop.md`
- `chaos-redux-subagents.md`
- `hoi4-decisions-missions.md`
- `hoi4-focus-trees.md`
- all uploaded `chaosx_*.toml` subagent definition files
- `chaos_redux_events_catalog.xlsx`

## Spreadsheet inspection

The active workbook in `/mnt/data/chaos_redux_events_catalog.xlsx` was inspected with the spreadsheet skill and `artifact_tool`. The Event 13 row in the active workbook has Natural Disasters as a Minor Repeatable event, Cluster ID 5, Low member severity, and To Be Reworked status, with empty detail and evolution fields. The scenario table has SCN-007 present but blank in the active workbook, so the package recommends using it for Disaster Barrage if still free during implementation.

The file search index also contained older or alternate workbook snapshots where Event 13 and Disaster Barrage had draft text. The user-provided brief and the active workbook were treated as source truth for this package.

## Web research consulted

- EM-DAT disaster classification documentation.
- EM-DAT overview.
- Our World in Data natural disasters article.
- NASA Earthdata natural hazards topic.

These sources were used only for taxonomy and scale calibration. The gameplay design remains a Chaos Redux event design.

## User correction on population deaths

After the first package, the user clarified that some disasters can cause millions of deaths and that no state should ever have a fixed death amount. The revised package treats every immediate and follow-up disaster death calculation as a dynamic percentage of the affected state population. Dense states, including dense Chinese states, naturally produce higher absolute deaths under the same final loss rate.


## V3 correction after user feedback

The user rejected the previous package as too shallow and clarified that old Sandstorm, Meteor Shower, and Heat Wave event code cannot be used as Event 13 logic because those events are also to be reworked. The source specs now include an external event boundary file that forbids using unreworked disaster adjacent events as logic sources. The user also clarified that all big disasters should feel big and unique, and that countries directly hit by big disasters should receive disaster specific decision categories instead of one generic recovery list. The package now adds individual playbooks for flood, cyclone, severe storm, hail, wind, moving storm corridor, earthquake, great rupture wave, tsunami, volcano, massive eruption, wildfire, drought, heat, cold, sandstorm, mass movements, meteor shower, meteor storm, and famine or displacement chains.
