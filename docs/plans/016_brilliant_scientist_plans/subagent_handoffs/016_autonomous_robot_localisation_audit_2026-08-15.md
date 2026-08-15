# Autonomous Robot Localisation Audit

Date: 2026-08-15

## Scope

This audit covers the shared Autonomous Robot tranche across the Event 016 project stages, the `autonomous_robot` subunit, `autonomous_robot_equipment`, `brilliant_scientist_robot_formations_tech`, `brilliant_scientist_robot_formations_weaponization_tech`, and Event 019 family and provider ID 505 text.

The audit followed `AGENTS.md`, `chaos-redux-events`, and `chaos-redux-subagents`. It also consulted the offline Localisation, Technology Modding, Equipment Modding, and Unit Modding wiki pages, the vanilla localisation formatter documentation, and vanilla mechanized and modern-tank localisation precedents.

## Files changed by this audit

- `localisation/english/016_brilliant_scientist_projects_l_english.yml`
- `localisation/english/019_infrantry_spawn_l_english.yml`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_autonomous_robot_localisation_audit_2026-08-15.md`

`localisation/english/016_brilliant_scientist_country_l_english.yml` already contained concurrent robot-key changes when this audit began. Those lines were reviewed and preserved without further edits.

## Changed keys

### Event 016 project text

- `brilliant_scientist_robotics_theory_desc`
- `brilliant_scientist_advance_robotics_theory_desc`
- `brilliant_scientist_robotics_prototype_desc`
- `brilliant_scientist_robotics_deployment_desc`
- `brilliant_scientist_advance_robotics_deployment_desc`
- `brilliant_scientist_robotics_weaponization_desc`
- `brilliant_scientist_advance_robotics_weaponization_desc`
- `brilliant_scientist_robotics_incident_desc`
- `brilliant_scientist_robotics_incident_mission_desc`
- `brilliant_scientist_resolve_robotics_incident`
- `brilliant_scientist_resolve_robotics_incident_desc`

### Event 019 family 505 text

- `infantry_spawn_family_sustainment_cost_profile_autonomous_robot`
- `infantry_spawn_family_request_cost_profile_autonomous_robot`
- `brilliant_scientist_event19_robot_host`
- `brilliant_scientist_event19_robot_host_desc`

## Before and after display

The Event 016 project text previously mixed `frame`, `robot`, and abstract `bounded robotic support` terminology. It now consistently describes inspectable machine cognition, autonomous combat robots, audited command limits, and a separated military command network.

The weaponization description previously exposed the tuning-oriented phrase `no free equipment`. It now describes the visible military purpose and safety boundary without discussing implementation or reward suppression.

The robotics incident previously returned to `autonomous frames` after the unit and equipment had been renamed. It now describes a hidden command propagating through autonomous robots and workshop systems. The response text identifies isolating the robots and severing the corrupted network as the concrete action.

The Event 019 hidden host idea previously used the internal phrases `provider-owned receipt` and `Event 016 parent identity`. It now reads as an in-world logistics charter that permits isolated robot production and sustainment.

The Event 019 request and sustainment cost strings previously displayed the generic label `robot equipment`. They now nest `$autonomous_robot_equipment_1$`, so the visible cost follows the actual equipment name `Autonomous Combat Robot` if that key changes later. All numeric constants and `|0` integer formatters were preserved.

## Dynamic localisation added or fixed

- Added nested localisation through `$autonomous_robot_equipment_1$` in the family 505 request and sustainment cost profiles.
- Preserved all political power, command power, manpower, and equipment constant references.
- Preserved `[This.GetBrilliantScientistHostFlavorClause]` in the incident mission description.

## Gameplay and source evidence

- `common/units/016_brilliant_scientist_project_forces.txt` defines `autonomous_robot` as both armor and mechanized, with armored and infantry categories. This supports the formation description's mechanized-infantry and armored-assault role.
- `common/units/equipment/016_brilliant_scientist_project_force_equipment.txt` gives the robot equipment 70 armor, 60 breakthrough, 88 percent hardness, 30 hard attack, 75 piercing, and 92 percent reliability. This supports the strong armor, anti-armor, breakthrough, and reliability language.
- `common/technologies/016_brilliant_scientist_project_technologies.txt` shows that `brilliant_scientist_robot_formations_tech` unlocks `autonomous_robot_equipment_1` and the `autonomous_robot` subunit.
- `common/technologies/016_brilliant_scientist_project_force_technologies.txt` shows that the weaponization technology increases robot hard attack, breakthrough, and reliability factor by the defined values. The concurrent weaponization description matches those effects.
- `common/script_constants/016_brilliant_scientist_project_constants.txt` lines 558 through 593 match all three visible robotics stage cost strings.
- `common/script_constants/016_brilliant_scientist_project_force_constants.txt` lines 422 through 450 define family and provider ID 505, its four-battalion template, and the request and sustainment costs used by Event 019.

## MCP evidence

Workspace ID: `mod_chaos_redux_ea3b2d67c2c0`

Event 019 inspection and render:

- Event scan: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fd36dc771150c9819554daab4b50b12e97229490b8b2961737b4dea904375437/619e2b7d85507b91e4d6e50849fb79362d3643666d9a0489d75022ff7c664398/event-scan-31ce73bb988b.json`
- Event trace from `chaosx.nr19.1`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1d83a5024cfaea607aec4a8efc56232ba46a259ba1144e39281cdd6a38188dc7/5324ea1f15ccb95df9f3300c9774a3eb2b380df866278b6fe4f4b4cd3e8d4212/event-trace-31ce73bb988b.json`
- Event neighborhood manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0a713a79329ec894e7e8a8addd2033c9f6c0684c366260845c3c66908ad943e4/7101476fa8c338062187fe595567e71b2e11ca036331ccc21af040a4f87767a9/event-neighborhood-31ce73bb988b-manifest.json`
- Event neighborhood PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/140f59e251a21f6cb5adc65665e1ed2c880032cf24137a7d391d4272b8a17056/65e678ca9f9c10565dfcd41b78343ffce72fe83bd5df91ce849918c0a9e802f6/event-neighborhood-31ce73bb988b.png`

Technology inspection and render:

- Base technology unlock report: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/324b5ad4b1868b7f1d32204cb423a26c5422f4b6f78aac53f42f5b8e8bf21cad/87710c647f821a3b672790b98a16d40aaccc76a25aab0ab4c96231fbfaff5086/technology-unlocks-b4bc22a92a03.json`
- Weaponization unlock report: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/22f14e92c9635dfa179cbc4787967fb01a2e2a82da912c2ae5f54cd5594dd003/fb88cb3fd8c4eb79295583308171d59e216a9ee51c4465956acc2721ddd3fad4/technology-unlocks-b4bc22a92a03.json`
- Base technology render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fa6118f886f8b49b0ce8a1b05f2a09e3f6c47972c3b17cc22ce05f878e552d6b/65f6054ea1d67f5c8599316d73e45315ee63b7ebedf2593e053570c6b6a245ef/technology-technology-b4bc22a92a03.png`
- Weaponization technology render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/264c44e95610a13cb68319d81e27fce2708e1dba6255ac35700ce2d1e19daa8b/db5b87a7ac1bca1172d1e79dfd53422878793c543d32e5f23272ff3acc92e4d3/technology-technology-b4bc22a92a03.png`

The technology route was available and read-only. The Event 019 muster-board scripted GUI has been archived in the current source, so no active family-505-specific GUI layout exists for an overflow render. The cost profiles are consumed through scripted localisation and ordinary wrapped tooltips. Source inspection confirms their locations, but this pass cannot claim live font-wrap evidence for those tooltip consumers.

## Audit results

### Missing keys

None in the 40-key robot scope. The expected subunit, equipment, technology, project-stage, incident, Event 019 cost-profile, and hidden host-idea keys each resolve once.

### Duplicate keys

None among the 40 scoped keys across `localisation/english`.

### Scripted localisation issues

None remaining. The two family 505 cost-profile selectors point to existing keys, all referenced constant paths exist, integer values retain `|0`, and the newly nested equipment key exists exactly once.

### Dynamic text opportunities

Implemented the safe equipment-name nesting described above. No additional dynamic value was added because the remaining visible numbers already come from script constants.

### Cross-surface mismatches

Resolved the stale `frame` terminology inside the Event 016 robotics project and incident text. The current subunit, equipment, technology, and Event 019 family text now use `Autonomous Robot` or `Autonomous Combat Robot` consistently.

No remaining mismatch was found between the player-facing cost claims and their source constants.

### File encoding concerns

None. All three audited localisation files retain the UTF-8 BOM.

### Prose-quality issues

- Vagueness: replaced `bounded robotic support` and a generic machine network with concrete assembly, maintenance, frontline assault, and network-isolation actions.
- Bloat: no broad rewrite was performed. Repeated project-board capacity and cost sentences were preserved because they are shared mechanical context across all project families.
- Obvious explanation: removed `no free equipment`, which described reward implementation rather than the project.
- Repetition: kept repeated base wording in the matching `advance_*` descriptions so the project summary and decision description remain aligned.
- Overcomplication: simplified `machine-cognition and frame-control programme` into inspectable machine cognition and robot-control systems.
- Style-rule repair: removed internal provider and parent-identity language from family 505 text. No em dashes, sentence semicolons, staged contrasts, staccato chains, or prompt fragments remain in the changed text.

### Sourced quotation preservation

No sourced or attributed quotation appears on any inspected robot surface. No quotation was altered.

## Meaningful validation

- Compared the three robotics stage cost strings with `brilliant_scientist_project_stage_cost` constants. All values match.
- Compared family 505 request and sustainment dynamic constant paths with the provider effect and family constants. All paths and gameplay costs match.
- Scanned all English localisation for the 40 expected robot keys. Result: 40 found, zero missing, zero duplicates.
- Scanned runtime source and localisation for the retired `kruger_robot_frame` and `kruger_robot_equipment` identifiers. No remaining runtime or localisation reference was found.
- Confirmed UTF-8 BOM on all three audited localisation files after the patch.
- Confirmed the nested `$autonomous_robot_equipment_1$` target exists exactly once.

## Skipped validation and uncertainty

- No live Hearts of Iron IV session was run. Live consumer validation belongs to the user.
- No active family-505-specific scripted GUI is present to render for exact pixel overflow. Ordinary tooltip wrapping remains a live-consumer uncertainty.
- The visual wording `twin arm-mounted machine guns` and `twin forearm machine guns` was already present in concurrent localisation when this audit began. It matches the current approved robot direction supplied through the parent task, but this localisation-only pass did not inspect or modify 3D assets.

## Remaining issues and parent follow-up

No unresolved wording decision remains inside the assigned robot key set. The parent should preserve the concurrently added country-file keys when integrating the broader runtime tranche and carry the tooltip font-wrap uncertainty into final live review.

## Simplifications, omissions, and blockers

No localisation fallback or simplification was used. The only unavailable evidence is live tooltip wrapping for the archived muster-board consumer, as recorded above.
