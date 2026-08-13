# Coding-Agent Implementation Prompt for Event 018 Resources Found

Implement Chaos Redux Event 018, Resources Found, to the fullest extent of the source specification package. Treat every mapped mechanic, evolution, decision family, country surface, focus route, asset, achievement, super-event, AI behavior, log entry, documentation field, and validation scenario as acceptance criteria.

Do not implement a smaller fallback version. Do not replace the resource-field system with one popup and one modifier. Do not replace the cave country with a temporary enemy spawn. Do not omit AI, assets, localisation, closure, ownership transfer, focus routes, deployment rules, or world-end behavior. Report every blocked or simplified item.

## Required reading

Before editing, read:

- `AGENTS.md`
- the full Event 018 spec pack
- all matrices in this package
- the focus architecture
- the asset, super-event, achievement, and decision prompts
- `chaos-redux-events`
- `chaos-redux-event-assets`
- `chaos-redux-frame-animation`
- `chaos-redux-super-events`
- `chaos-redux-focus-trees`
- `chaos-redux-decisions-missions`
- `chaos-redux-improvement-loop`
- `chaos-redux-subagents`
- required offline Paradox wiki pages
- relevant vanilla documentation and precedents
- current Chaos Redux event, log, evolution, cluster, country, decision, focus, dynamic helper, super-event, audio, achievement, and spreadsheet patterns

Use `chaosx_repo_explorer` with `fork_context=false` if exact files, IDs, slots, tags, or precedents are unclear. The explorer is useful here because the task spans many systems. Pass it every path and constraint explicitly.

## Core implementation contract

Preserve these non-negotiable rules:

1. Event 018 remains Minor Repeatable and is an Economy (pos) member at Medium severity.
2. The ordinary event selects one valid state and one completely random standard strategic resource.
3. The baseline deposit is centered around 100.
4. Event-owned resource additions are stored separately for all six resource types.
5. Repeated firings can enrich the same field, including duplicate resource stacking.
6. Baseline discovery, appraisal, development, contracts, safety, suspension, transfer, and closure work with evolutions disabled.
7. Full closure removes only Event 018 additions.
8. Evolution I creates compound fields and international competition.
9. Evolution II creates gradual sickness, corrosion, deaths, and underground attacks.
10. Evolution III creates a huge all-resource field, public monsters, hunts, evacuation, and a guaranteed successful full-seal prevention route.
11. Evolution IV creates a complete playable actual nonhuman cave country.
12. Cave opening strength scales from 6 to 30 divisions from exploitation history.
13. The origin state is excluded from future captured capacity.
14. Each non-origin captured state gives floor(total strategic resources divided by 10), capped at 10.
15. Capacity activates after continuous control and spawns divisions automatically over time.
16. Cave units use no normal manpower or equipment, cannot train normally, move very slowly, have extreme armor, and are countered by serious hard attack.
17. The cave country declares war on all current and newly adjacent land neighbors.
18. The cave country has a real focus tree, decisions, AI, leader, flags, ideas, templates, and assets.
19. World end requires chaos above 1000 and verified control of every eligible origin-continent state.
20. World end creates stronger distributed footholds on other continents and freezes incompatible random-event progression.

## Suggested implementation order

### Phase 1: Repository map and design registration

- map current Event 018 files and status
- map event registration and default-enabled allowlist
- preserve Event 018's Economy (pos) mapping, member registration, and Medium severity
- map event-log and evolution surfaces
- reserve country tag, focus tree ID, decision IDs, helper names, achievement IDs, super-event slots, image sprites, and audio IDs
- write an implementation ledger under `docs/plans/018_resources_found_plans/`

### Phase 2: Core field helpers and tuning

Use `chaosx_scripted_system_architect` for reusable logic.

Create documented helpers for:

- valid owner and state selection
- random resource roll
- exact event-owned resource addition
- field initialization and lookup
- field selection
- resource composition display
- total and distinct resource calculation
- state ownership transfer
- suspension and closure subtraction
- value changes and thresholds
- contract validity
- claimant and foreign-interest scoring
- evolution pacing
- cave exploitation score
- captured-state capacity
- anchor activation and cleanup
- spawn queue and excess divisions
- neighbor-war refresh
- continent progress and eligible-state verification
- world-threat refresh

Centralize all tuning values. Document every new dynamic helper with scope, inputs, outputs, defaults, side effects, and examples.

### Phase 3: Baseline event and management system

Implement:

- canonical discovery event
- repeat enrichment
- persistent field record
- one random resource and approximately 100 production
- selected-field decision category and compact header
- four visible baseline values
- administration postures
- appraisal, development, transport, processing, labor, safety, security, extraction modes, suspension, and closure
- state transfer and occupation behavior
- event-log history and Event Details
- AI owner behavior

Do not continue to evolutions until exact ledger and closure behavior are proven.

### Phase 4: Trade, foreign pressure, and border system

Implement:

- foreign interest scoring
- shortlist bids
- contracts and lifecycle
- concessions and influence
- reserve and diversified access
- nationalization and compensation
- smuggling, espionage, sabotage, and exposure
- commission and demilitarization
- staged border crisis
- active frontier missions
- limited border war and state transfer
- foreign AI

Reuse shared border infrastructure when valid.

### Phase 5: Evolutions I through III

Implement separate pre-fire and active entries for every evolution. Use dynamic MTTH pacing and shared evolution logging.

Evolution I:

- 2 to 4 pre-fire rolls
- compound-field active enrichment
- multi-resource administration
- international rush and DMZ routes

Evolution II:

- 3 to 5 pre-fire rolls
- gradual sickness and corrosion incidents
- visible Disturbance reveal
- shared Deaths integration
- restricted workings, survey, concealment, and closure

Evolution III:

- very large all-resource opening
- gradual inherited Evolution II sequence
- public breach and visible Breach Pressure
- hunts, evacuation, aid, urban crisis
- partial closure
- full sealing that removes all Event 018 resources and permanently blocks Evolution IV

Disabled later evolutions must leave clean stabilization and closure routes.

### Phase 6: Cave country

Use country, focus, decision, localisation, and asset subagents in bounded passes.

Implement:

- one stable tag
- safe state transfer and former-owner aftermath
- literal cave-monster leader with original name
- country names, party, sub-ideology, flags, portraits
- shared special-chaos and actual-nonhuman classification
- origin state supply and idea package
- 6 to 30 dynamic starting divisions
- no normal manpower, equipment, training, trade, faction, navy, or air system
- slow armored templates and hard-attack counterplay
- resource-anchor capacity with origin exclusion
- continuous-control activation
- paced automatic spawning
- capacity loss and Unfed Broods
- neighbor-war refresh
- complete focus tree from architecture
- phased cave decisions
- route-aware AI

### Phase 7: Anti-cave response, continent, and world end

Implement:

- neighbor mobilization
- anti-armor aid and research
- resource denial
- activation-window recapture
- anchor cleanup and resource restoration
- cave world-threat source
- origin-continent eligible state group
- visible progress
- 25, 50, and 75 percent milestones as ordinary progress events
- full-continent verification
- chaos above 1000 gate
- terminal world-end effect
- stronger cross-continent footholds
- terminal cave identity and AI
- regional defeat cleanup
- global defeat aftermath only when justified

### Phase 8: Assets, super-events, achievements, text, docs, spreadsheet

Produce and wire the full asset package. Do not use placeholders.

Research and wire unique emergence and world-end super-events. Implement global defeat super-event only when its severity gate exists.

Implement the achievement set with tracking, disqualifiers, icon triplets, GFX, localisation, docs, and tests.

Write final localisation from the spec direction. Do not paste working labels as final text. Do not expose hidden mechanics in Event Details.

Update:

- event script and all companion systems
- event registration and default enablement
- event log and evolution log
- cluster mapping
- scripted GUI and GFX
- country, focus, decision, ideas, AI, templates, traits, history
- super-event text, images, audio, and music docs
- achievements
- `docs/events/018_resources_found/overview.md`
- helper docs
- asset and super-event manifests
- catalog workbook through `chaosx_spreadsheet_doc_worker`

## Required subagent passes

All project subagents use `fork_context=false` and receive explicit paths, IDs, constraints, and current status.

Use as appropriate:

- repo explorer before broad editing
- scripted system architect for helpers and tuning
- decision and mission auditor after categories are built
- focus tree auditor after the cave tree is built
- country package auditor after the cave tag is complete
- localisation auditor after broad text is written
- generated event art and icon artist for assets
- super-event text and audio researchers
- documentation curator after several handoffs
- spreadsheet worker after final in-game wording exists
- event completion auditor before completion claim

Before near completion, run `chaosx_improvement_loop_planner`. Resolve its addendum or closure handoff. Do not stack another unresolved plan.

## Writing rules

Final player-facing text must:

- use no em dash
- use no semicolon in sentences
- avoid staccato drama
- avoid dialectical hedging and staged contrast formulas
- avoid generic disaster filler
- describe observed actors, work, fear, violence, and consequences
- keep ordinary discovery positive and practical
- keep early horror uncertain
- avoid cheap humor around sickness and deaths
- keep cave-country language original and readable
- avoid achievement language outside achievement UI
- keep Event Details free of mechanical effects and hidden spoilers

## Balance and meaningful validation

Run and document every scenario in `matrices/acceptance_criteria.md`, especially:

- exact resource addition and closure subtraction
- repeated duplicate rolls
- contract transfer
- border settlement and border-war state transfer
- high-safety versus low-safety Evolution II outcomes
- successful Evolution III full seal
- maximum 30-division breach
- capacity results at 0, 9, 10, 48, 100, and over 100 resources
- origin exclusion
- activation interruption
- capacity loss and excess divisions
- cave AI target selection and hard-attack response
- continent eligibility and chaos gate
- cross-continent foothold validity
- regional and global defeat cleanup

Do not fill the completion report with boilerplate syntax checks. Report task-specific evidence, findings, balance changes, and unresolved risks.

## Completion report

The final report must list:

- files changed by surface
- event, decision, focus, country, helper, asset, super-event, achievement, and localisation IDs
- route coverage
- decision and mission coverage
- country package coverage
- AI behavior
- exact resource and capacity validation
- assets created and wired
- audio sources and licenses
- documentation and spreadsheet updates
- accepted plan dispositions
- meaningful validation scenarios and results
- every simplification, omission, fallback, blocker, or skipped validation

If any requested surface is incomplete, state that the event is incomplete. Do not present partial work as full completion.
