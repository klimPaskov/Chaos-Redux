# Event 067 Generalissimo Planning Completion Report

## Final status

The Event `067` Generalissimo planning specification is complete as a parent-authored design pack.

The pack fully expands the accepted rough event into an implementation-ready event system. It does not claim gameplay implementation, MCP validation, asset production, audio production, workbook editing, or in-game testing.

One required process item remains blocked. The active environment did not expose a working custom-subagent invocation route, so no independent project subagent executed during this planning pass. Two Codex Native discovery attempts failed with HTTP 429 and HTTP 404 responses. Every supplied subagent definition was still read in full and converted into explicit implementation routing and handoff requirements.

## Source reading

The following source sets were read in full before the specification was written:

- all 23 supplied project files, including the accepted rough event, mechanics guide, repository rules, skills, configuration, README, three complete catalog CSV exports, and the subagent ZIP
- all 20 TOML subagent definitions extracted from the ZIP

No supplied source file was skipped. No truncated attachment preview was used as a substitute for the local full file. File sizes, line counts, SHA-256 hashes, and read status are recorded in `quality/067_generalissimo_source_reading_manifest.md`.

## Package contents

The final package contains:

- 9 specification parts
- 8 implementation prompts
- 2 research files
- 1 state-machine diagram
- 4 implementation handoffs
- 3 quality records
- 1 package README

Total package size and text counts are recorded in the generated package statistics below.

## Design coverage

The specification covers the complete Event 067 lifecycle:

- target selection among valid majors and player-controlled countries
- one canonical fictional Generalissimo character
- maximum safe commander capability and trait audit requirements
- hidden pre-evolution service record
- one public pre-coup value, Generalissimo Influence
- four command-authority states
- paced evolutions at 200, 400, and 600 or higher Chaos
- demands, concessions, counterweights, missions, and permanent removal
- immediate revolt after specified failed coercive removal methods
- dynamic revolt strength, army share, commanders, territory, factories, stockpiles, navy, and air allocation
- peaceful submission without a second country
- host-derived military-government package
- one public post-takeover value, Command Cohesion
- a complete host-adaptive focus-tree architecture
- postwar integration and government outcomes
- triggerable scenario Generalissimo's Coup
- public world-end branch The Generalissimos' World
- Event 019 and Event 065 integration
- Event Logs, Event Details, cluster, Chaos, multiplayer, cleanup, and AI contracts
- complete static visual asset inventory
- two super-event packages
- eight achievements
- named probability scenarios for every weighted surface

## Key resolved design decisions

### Character identity

One stable fictional male character token is used across commander, field marshal-rank commander, and ruler roles. Clones are prohibited.

### Civil-war identity

A dynamic civil-war side is the preferred route. A fixed tag is blocked unless current engine evidence proves that it is required and the full current collision audit passes.

### Public mechanic values

Generalissimo Influence is the only public pre-coup value. Command Cohesion replaces it after takeover. The player never manages both values at once.

### Presentation

The event uses an ordinary decision category with a compact attached display, five static phase pictures, and a small read-only focus inlay. A full-screen event window and final animation package are outside the accepted design.

### Unit and model scope

No custom unit, equipment family, technology tree, doctrine tree, 3D model, unit counter, or unit audio package is required. The event uses host forces and ordinary equipment.

### World-end structure

The terminal branch creates several military and civilian outcomes through a bounded actor registry. It does not run a recurring whole-world scan and does not create copies of the original Generalissimo.

## Catalog findings

The supplied Events export identifies Event `067` as Generalissimo, Minor Fire-Once, Chaos Level 1, and To Be Reworked. Its cluster fields are blank.

The accepted event source assigns Event `067` to Military Preparation as a High member. The supplied Clusters export has no Military Preparation row. The specification follows the accepted source and requires implementation to reconcile the runtime registry and authoritative workbook.

The supplied Scenarios export reaches `SCN-014` and omits `SCN-004`, while the mechanics guide still documents `SCN-004` Final Silence. `SCN-015` is therefore a proposed Event 067 scenario ID, not a confirmed free registry slot. Implementation must verify it against the workbook and live registry before registration.

## Research use

External research was used to sharpen the design of coup coordination, officer alignment, coup-proofing, parallel command structures, and military-government stability. Research claims, source details, confidence, and design use are recorded in the two research files.

The main design inference is that revolt strength should depend on coordinated command, communication, officer expectations, and institutional control. Grievance alone is insufficient. Counterweights should reduce coup capacity while creating a military-performance cost.

## Subagent routing

`handoffs/067_generalissimo_subagent_routing_matrix.md` assigns the implementation work to the correct narrow project roles. It includes the mandatory audit, patch, compare, improvement-loop, asset, audio, workbook, and completion routes.

The parent-authored improvement review resolves the major depth gaps and recommends stopping broad expansion. It does not replace the mandatory independent `chaosx_improvement_loop_planner` pass against the implemented event.

## Quality checks

The final package passed these planning-specific checks:

- every README-indexed file exists
- no file is empty
- all specification parts use padded Event ID `067`
- the goal prompt contains 3,941 characters, within the required 3,500 to 4,000 character range
- the achievement prompt defines eight unique achievement IDs
- no em dash character appears in the package
- no semicolon character appears in the package
- no prohibited comparison template appears in the package
- all event labels use the padded ID `067`
- every proposed `SCN-015` use states or inherits the confirmation requirement

These checks validate package structure and writing constraints. They do not prove HOI4 engine behavior.

## Simplifications, omissions, and blockers

### Design simplifications

No accepted event surface was deliberately removed, merged into a weaker substitute, or shortened for speed.

The exclusion of a full-screen GUI, custom units, 3D models, animated assets, a fixed junta tag, and extra public meters is intentional design scope supported by the improvement review. These are not fallback implementations.

### Omitted implementation work

Gameplay code, localisation, visual assets, final quotes, licensed audio, workbook edits, and MCP evidence are not part of this planning-only deliverable. The prompts define the exact implementation and audit work required.

### Blocker

Independent custom-subagent execution was unavailable in this environment. The final implementation goal must run the required subagents, especially the improvement-loop planner and completion auditor, before any event completion claim.

## Package statistics

- Total files: `28`
- Markdown lines: `10244`
- Markdown words: `53092`
- Markdown characters: `372894`
- Goal prompt characters: `3941`
- Specification parts: `9`
- Implementation prompts: `8`
- Unique achievement IDs: `8`

## Completion judgment

The planning design is complete and has not been truncated. It is ready to extract into `docs/specs/067_generalissimo_specs/` and use as the implementation source.

The process record remains explicit about the missing independent subagent execution. That limitation prevents a claim that every requested planning process was executed exactly as intended, but it does not leave an event design surface unspecified.
