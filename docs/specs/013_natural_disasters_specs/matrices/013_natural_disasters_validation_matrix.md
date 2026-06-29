
# Event 013 validation matrix

This matrix lists meaningful checks for the implementation pass. It avoids boilerplate checks and focuses on failures that would matter for Event 13.

| Validation area | Check | Why it matters |
| --- | --- | --- |
| Event logging | Fire one Event 13 baseline sequence and confirm exactly one random-event history row is recorded for the sequence. | Prevents subevent log spam. |
| Delay pacing | Fire baseline sequence and confirm subdisasters do not all arrive the same day unless sequence size is one. | Preserves the delayed disaster identity. |
| Cluster repetition | Trigger Natural Disasters cluster and confirm multiple Event 13 member slots can queue separate sequences with separate Event 13 rows and member skip reasons. | Confirms special cluster behavior. |
| News throttle | Trigger Evolution II with many impacts and confirm only meaningful news events appear. | Prevents global spam. |
| Deaths integration | Hit a populated state and confirm real state population changes and civilian death log entries update from `current_state_population * final_dynamic_loss_rate`. | Core user requirement. |
| Population scaling | Fire the same severity and family against a sparse state and a dense state, including a dense Chinese state if available. Confirm the dense state produces much larger absolute deaths without using any fixed casualty amount. | Ensures percentage-based deaths and realistic dense-state scaling. |
| Multi-million severe disasters | Fire an Evolution III massive quake-wave, tsunami chain, meteor shower, or moving storm corridor against dense states. Confirm multi-million civilian deaths are possible when the dynamic rate and state populations justify it. | Prevents hidden absolute caps and timid high-chaos effects. |
| Building damage | Compare flood, earthquake, cyclone, drought, and sandstorm impacts. Confirm family-specific damage pools differ. | Prevents flat factory-loss design. |
| Recovery costs | Inspect decisions and confirm most major recovery actions use physical resources or objectives, not only political power. | Follows decision skill and user direction. |
| Recovery success | Complete a rail, port, shelter, fire, drought, ash, or aftershock mission and confirm aftermath reduces or clears. | Ensures decisions matter. |
| Recovery failure | Let at least one mission fail and confirm family-specific follow-up occurs. | Confirms aftermath chain. |
| Heat wave interaction | With Heat Wave active, attempt an Event 13 extreme heat incident and confirm no duplicate heat stacking. | Required event interaction. |
| Sandstorm migration | Confirm separate Sandstorm active gameplay is disabled or routed through Event 13. | Required migration. |
| Event 46 migration | Confirm Event 46 is an inactive unknown placeholder and seismic content resolves through Event 13. | Required migration. |
| Evolution I | At its unlock state, confirm expanded families and warning decisions become available. | Evolution fidelity. |
| Evolution II | At its unlock state, confirm regional state damage, supply penalties, recovery category, and aftermath chains appear. | Evolution fidelity. |
| Evolution III | At its unlock state, confirm abnormal families can fire and no world-end flag is set. | High-chaos design and no terminal branch. |
| Manual scenario | Launch Disaster Barrage at each intensity and type. Confirm it bypasses ordinary chaos prerequisites and clears bypass flags after setup. | Scenario contract. |
| Manual override safety | Queue a normal delayed Event 13 controller, force-launch Disaster Barrage before it fires, finish the manual season, and confirm the old normal delivery cannot mutate the cleared context. Repeat with a second manual force launch while a prior manual delayed controller is pending. | Prevents stale delayed controller collisions. |
| Scripted GUI | Open map, select active state, use a button, then close and cleanup. Confirm AI equivalents exist for button effects. | UI correctness. |
| Animated assets | Confirm every animated sprite has source frames, sheet DDS, static fallback, manifest, and no GIF path used in `.gfx`. | Animation skill contract. |
| Localisation | Audit missing keys and dynamic state names. Confirm no raw triggers are exposed. | Player-facing clarity. |
| Spreadsheet | After final wording exists, workbook fields match in-game event detail, evolution detail, cluster detail, and scenario detail. | Catalog alignment. |
| Completion audit | Run event completion audit against this spec package before claiming complete. | Prevents hidden omissions. |

## V3 depth validation additions

| Validation area | Check | Why it matters |
| --- | --- | --- |
| Old disaster code boundary | Grep implementation for calls or copied helpers from unreworked Event 51 Heat Wave, Event 99 Sandstorm, Event 28 Asteroid Incoming, Event 43 Massive Flood, Event 46 Unknown Placeholder, Event 47 BOOM, and any separate Meteor Shower placeholder. Confirm Event 13 does not use them as logic sources. | Prevents Event 13 from inheriting shallow unreworked disaster code. |
| Sandstorm placeholder | Confirm Event 99 has no independent active disaster damage, deaths, recovery, evolution, or news spam. It may be inactive or a wrapper into Event 13 only. | Required migration from old Sandstorm to Event 13. |
| Heat non stacking | With Event 51 active, fire Event 13 heat selection and confirm duplicate heat modifiers do not stack. Confirm conversion to drought, wildfire, water emergency, or unique heat aftermath when needed. | Prevents double heat penalties and respects separate Heat Wave rework. |
| Meteor separation | Confirm Event 13 meteor shower and meteor storm never call Event 28 Asteroid Incoming logic. | Keeps meteor shower distinct from single asteroid prediction event. |
| Big category coverage | Fire serious flood, earthquake, tsunami, volcano, cyclone, drought, wildfire, heat, cold, sandstorm, mass movement, meteor shower, and moving corridor cases. Confirm each opens its family category. | Ensures big disasters are unique and not a generic recovery list. |
| Category cleanup | Resolve each family disaster and confirm category flags, missions, selected states, forecast states, and GUI markers clear. | Prevents stale disaster UI and invalid target decisions. |
| Category cost depth | Inspect family categories and confirm each uses physical resources, logistics, XP, manpower, stability, war support, local objectives, or access. | Prevents political power store design. |
| Family identity | Compare flood, quake, tsunami, volcano, cyclone, drought, wildfire, heat, cold, sandstorm, meteor, and corridor effects. Confirm target logic, buildings hit, aftermaths, and missions differ. | Ensures disasters are big and unique. |
