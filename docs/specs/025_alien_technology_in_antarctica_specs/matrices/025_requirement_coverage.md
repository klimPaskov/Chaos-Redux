# Requirement coverage

This matrix records design/specification coverage, not final acceptance. `Covered` means the requirement is represented by the accepted specification package; it does not waive implementation, MCP, probability, spreadsheet, or live-runtime evidence.

| User or project requirement | Specification coverage | Status |
| --- | --- | --- |
| Alien craft crashes in Antarctica | Parts 001, 003, 010 | Covered |
| International expedition race | Parts 001 to 003 | Covered |
| AI majors and player country may participate | Parts 001, 002, 009 | Covered |
| Every human country can participate | Parts 001, 002, route matrix | Covered |
| Convoys, fuel, support equipment, scientists, personnel, and industry matter | Parts 002, 003, 005 | Covered |
| Distance changes cost and travel time | Parts 002, route matrix | Covered |
| Southern Ocean access lowers burden | Parts 002, route matrix, research | Covered |
| Staging ports and outposts | Parts 002, 003, 005 | Covered |
| Survey, signals, and fragments | Parts 002 to 005 | Covered |
| Rival raids, sabotage, theft, false information, and defense | Parts 005, 007, 009 | Covered |
| Baseline can be won without evolutions | Parts 001, 003, 004, acceptance | Covered |
| Winner secures main wreck | Parts 003, 006 | Covered |
| Winner gets random advanced Kruger-system technology without Kruger wording | Parts 006, 007, 012, 013 | Covered |
| Losing participants get partial rewards | Part 006, reward matrix | Covered |
| Clean Event 036 connection | Parts 006, 007, reward matrix | Covered |
| Evolution I active signal | Part 004, actions and entry matrices | Covered |
| Evolution II survivor | Part 004, actions and entry matrices | Covered |
| Evolution III militarisation | Part 004, Parts 005 and 007 | Covered |
| Evolution IV wreck breaks apart | Part 004, Parts 005 and 006 | Covered |
| Evolution V changes users | Part 004, Parts 006 and 008 | Covered |
| Full planning skill depth | Fourteen spec files, eight matrices, research, prompts, and handoffs | Covered |
| Dedicated GUI for a living expedition system | Part 008 | Covered |
| Decisions avoid political-power store design | Part 005 | Covered |
| At most four spendable costs | Part 005 and acceptance | Covered |
| Three main visible values | Parts 002 and 008 | Covered |
| AI strategy and probability scenarios | Part 009 and AI matrix | Covered |
| Major-event super-event | Part 010 | Covered |
| Achievements for a major event | Part 011 | Covered |
| Asset and animation coverage | Part 010 and asset matrix | Covered |
| No shallow extra countries or trees | README and Parts 001, 010 | Covered by deliberate scope |
| No recurring world scan | Parts 002, 013, acceptance | Covered |
| Event logs and evolutions | Parts 004, 007, 013, acceptance | Covered |
| Catalog alignment through XLSX only | Part 013, acceptance, spreadsheet prompt | Covered |
| Relevant subagent prompts | `prompts/` package | Covered |
| Honest process limitations | README and handoff | Covered |

## Current implementation evidence

The active Event 025 source, board assets, localised routes, five evolution families, shared Event 025/Event 036 ledger, and Event 016 owner-API bridge are present in the repository and are documented in docs/events/025_alien_technology_in_antarctica/overview.md and docs/assets/025_alien_technology_in_antarctica/visual_asset_audit.md.

The corrected sector hitbox is wired and mirrored at 384x58 with four 96x58 frames, and the board GUI now uses one map-level selected overlay instead of six repeated full-map overlays.

The following acceptance evidence is unresolved or blocked: the targeted hoi4.gui_inspect/render/compare route timed out after 180 seconds, the three targeted technology inspections timed out after 180 seconds, the latest event inspect was partial with deferred analysis, and baseline/post-patch probability auditor handoffs are pending.

The evolution overlays are real frame sheets, recorded in the visual audit.

The legacy UFO-race visual and decision aliases remain preserved for Event 016 compatibility and are excluded from the active Event 025 path.
