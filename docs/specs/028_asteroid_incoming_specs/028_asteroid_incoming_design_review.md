# Asteroid Incoming: Design Review

## Review status

Every supplied upload was read in full, including the project Markdown files, three catalog CSV exports, `config.toml`, `subagents.zip`, and all 20 unpacked subagent TOML definitions.

The Windows Chaos Redux repository, offline Paradox wiki snapshot, installed vanilla game files, and vanilla documentation paths were not mounted in this chat environment. The project custom subagent invocation interface and HOI4 MCP tools were also unavailable. No project subagent was actually spawned, and no MCP event, GUI, map, or probability inspection was run.

The source package was reviewed manually against the fully read project subagent definitions and skill contracts. This is useful design evidence. It is not equivalent to repository inspection, required local engine-reference checks, implementation-time subagent work, or MCP evidence.

## Repo exploration lens

### Findings

- The current Event 28 catalog export is stale and conflicts with the supplied brief.
- Shared Deaths and exact population-loss helpers already support the required civilian transactions.
- Air Cleanliness can carry asteroid dust as a distinct source.
- Event 013 exposes a bounded disaster adapter suitable for secondary aftermath.
- Shared actual-nonhuman and special-country classifiers can prevent invalid target actors.
- Major-event pacing already defines the fire-once and reset behavior.

### Design response

The specification reuses those shared contracts and avoids a second generic disaster, death, contamination, or world-end framework.

## Scripted-system architecture lens

### Findings

The event needs one protected incident transaction with locked target data, shortest-path state rings, strongest-profile merging, country aggregation, and persistent crater registration.

### Design response

- All target and fragment centers lock before damage.
- Every state is processed once at the strongest profile.
- Population and building losses derive from current state values.
- Country reports are assembled after the transaction.
- Mineral bonuses derive from current site control and replace stale state.
- Dust uses event-driven and monthly changes. It adds no daily all-country scan.

The final helper design remains implementation work and requires HOI4 source and MCP review.

## Decision and mission audit lens

### Findings

A custom window would add presentation cost without improving the main choices. The aftermath can be read through one global dust stage, one national protection state, and exact state targets.

### Design response

- Use one ordinary category with a static category picture.
- Expose three to five actions per phase and one to three missions.
- Limit every spend action to four cost types.
- Use equipment, transport, fuel, manpower, construction, and route requirements.
- Hide obsolete phases and invalid targets.
- Give every important action an AI path and cleanup rule.

## AI probability audit lens

### Findings

The opening option is balance sensitive. Ordinary AI should favor the miss, while hostile use should remain possible under war, desperation, route identity, and high Chaos.

### Design response

Ten named four-option scenarios define expected ordering. Recovery and crater actions also have scenario expectations. Exact probabilities remain unresolved until `hoi4.probability_inspect` and the required evaluation and comparison tools run against the implemented full pool.

## Asset and presentation lens

### Findings

The event needs report, news, super-event, category, modifier, decision, and achievement assets. It does not need a new country identity or custom model to explain the mechanic.

### Design response

The asset prompt defines exact source modes, standard canvases, icon families, reference gates, final package evidence, and stable working names. The accepted baseline uses static category and stage art. Animation can be considered only after implementation proves it improves state clarity.

## Super-event research lens

### Findings

A global impact deserves one super-event. The miss does not. Final quote, remark, and audio cannot be responsibly selected without research and rights review.

### Design response

The package defines the impact role, dynamic target context, image direction, quote themes, and audio character. The super-event prompt requires verified text candidates and a unique licensed musical cue.

## Localisation lens

### Findings

The event can become repetitive or vague because many countries receive reports from one transaction.

### Design response

- Reports use dynamic country, state, region, death, and damage data.
- Final text directions identify viewpoint, visible information, uncertainty, tone, and language to avoid.
- Working labels are marked and cannot ship as final localisation.
- Impact text avoids cheap humor and generic apocalypse language.

## Improvement-loop review

### Playable promise

The event promises a directed global disaster with permanent strategic consequences. The first draft risked becoming one destructive popup followed by passive modifiers.

### Improvements accepted

- Locked country and state target cards
- Target-country emergency stance
- Backup-capital contract
- Strongest-profile adjacency merging
- Continuing but bounded rescue deaths
- One visible global dust state with national protection
- Phased recovery decisions and named missions
- Strategic crater-control actions
- Multiplayer transaction ownership
- Five route-specific achievements
- Detailed AI and probability scenarios
- Catalog reconciliation and source crosswalk

### Expansion rejected as bloat

- A dedicated asteroid mechanic window
- A full target-country focus tree
- New crater nations or tags
- A third evolution
- A terminal world-end route
- Ocean impacts and tsunami geometry
- Character death rolls
- A custom asteroid or crater 3D model
- Several competing dust currencies
- A manual triggerable scenario

These additions would expand maintenance and presentation without improving the accepted core enough to justify them.

### Stop condition

The source design is deep enough for implementation. Further broad expansion is not recommended before the accepted event is implemented and audited. Remaining work is implementation, asset production, probability evidence, super-event research, catalog alignment, and completion validation.

## Required implementation-time subagent and MCP work

The coding agent should still use the project routes that were unavailable here.

- `chaosx_repo_explorer` when current file locations or precedents remain unclear
- `chaosx_scripted_system_architect` for reusable transaction and control-refresh helpers
- `chaosx_decision_mission_auditor` after decision implementation
- `chaosx_ai_probability_auditor` before and after every weighted change
- `chaosx_generated_event_art` and `chaosx_icon_artist` for assets
- `chaosx_super_event_text_researcher` and `chaosx_super_event_audio_researcher`
- `chaosx_localisation_auditor` after broad text implementation
- `chaosx_spreadsheet_doc_worker` after final player-facing wording exists
- `chaosx_event_completion_auditor` before completion

All project subagents must use `fork_context=false` and context-complete prompts.
