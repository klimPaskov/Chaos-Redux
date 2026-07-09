# Event 018 Resources Found, Part 10 Repo Exploration and Spreadsheet Handoff

This file records implementation-side handoffs that could not be completed inside the planning sandbox because the actual Chaos Redux repository, offline Paradox wiki snapshot, vanilla Hearts of Iron IV documentation, and workbook were not mounted. It does not claim repo confirmation. It tells the next implementation agent exactly what must be verified before code, asset, and spreadsheet work are treated as complete.

## Repo confirmation status

| Area | Status in this pass | Required next action |
| --- | --- | --- |
| Existing resource effect syntax | Not confirmed from repo or vanilla docs | Run repo explorer and vanilla documentation pass before implementing resource add and cleanup. |
| Existing helper patterns | Not confirmed from repo | Inspect dynamic effects, event log effects, and any existing random state helper. |
| Event log arrays | Not confirmed from repo | Map current history, evolution, event-detail, and actor arrays before editing. |
| Scripted GUI patterns | Not confirmed from repo | Inspect existing Chaos Redux scripted GUI and vanilla GUI examples before wiring. |
| Cave Host tag and country package files | Not confirmed from repo | Choose conflict-free tag, country files, history, flags, leader, and focus tree loading only after repo scan. |
| Super-event slots and audio helper | Not confirmed from repo | Inspect current super-event scripted localisation, GFX, audio ids, music assets, and settings-aware playback helper. |
| Spreadsheet workbook | Not mounted here | Update only after final in-game localisation exists. |

## Repo explorer prompt packet

Use the `chaosx_repo_explorer` subagent with fork context disabled. Pass every path explicitly. The prompt should ask for a saved report under `docs/plans/018_resources_found_plans/subagent_handoffs/018_resources_found_repo_explorer_handoff.md`.

Required scout scope:

- Event 018 random event registration and current classification.
- Existing resource modification syntax and cleanup patterns.
- Existing state selection helpers and random valid-state patterns.
- Existing event-owned decision category files and scripted GUI patterns.
- Existing evolution log and event-details patterns.
- Existing world threat source patterns.
- Existing nonhuman country classification triggers.
- Existing focus-tree loading for event-created countries.
- Existing super-event slots, audio ids, and settings-aware playback helper.
- Existing achievement registration patterns.
- Existing asset folder and GFX patterns for event-owned assets.
- Existing spreadsheet alignment workflow and row 18 source data.

Expected report sections:

| Section | Required content |
| --- | --- |
| Primary files | Exact repo paths and identifiers that Event 018 must edit. |
| Existing patterns | Closest Chaos Redux examples for random states, resource effects, decisions, evolutions, world threats, countries, focus trees, super-events, and assets. |
| Vanilla precedents | Exact vanilla files or documentation pages that prove syntax. |
| Edit order | Recommended implementation order to avoid stale docs or broken cross-surface wiring. |
| Validation checks | Task-specific grep checks, duplicate id checks, sprite path checks, localisation key checks, and manual scenario checks. |
| Blockers | Missing patterns, missing helper support, or syntax uncertainty that should stop implementation. |

## Implementation dependency order after repo confirmation

| Step | Dependency | Purpose |
| --- | --- | --- |
| 1 | Repo explorer report | Confirm paths, syntax, helper patterns, and current Event 018 status. |
| 2 | Scripted system architecture | Define field memory, resource add and removal helpers, Cave Host capacity helpers, and cleanup helpers. |
| 3 | Core event and field setup | Implement random valid state discovery, owner popup, around 100 random resource deposit, and field state memory. |
| 4 | Decision category and GUI | Implement exploitation, safety, concession, public danger, closure, and Cave Host cards if GUI is approved. |
| 5 | Evolutions | Add pre-fire and active-event behavior for Evolutions I through IV. |
| 6 | Cave Host country package | Add tag, leader, flags, nonhuman classification, origin state transfer, starting army cap, and no-manpower rules. |
| 7 | Cave Host focus tree | Implement the focus blueprint from Part 7 with AI and capacity hooks. |
| 8 | Human response systems | Add evacuation, hunt, anti-armor, resource denial, and coalition response decisions where designed. |
| 9 | Super-events and assets | Produce final images, audio, quotes, buttons, and wiring only after research and asset handoffs. |
| 10 | Achievements | Add difficult tracking hooks and final icons. |
| 11 | Docs and spreadsheet | Align event docs, manifests, super-event docs, music table, and workbook row 18 with final in-game text. |
| 12 | Completion audit | Run focus, decision, localisation, country package, and event completion audits before claiming completion. |

## State and resource implementation plan requiring confirmation

The preferred design remains:

- Store the field state target.
- Store the original owner and current owner.
- Store the rolled resource type.
- Store event-added amount by resource type if the engine supports reliable cleanup.
- Add around 100 of the random resource to the selected state for baseline discovery.
- Track additional event-added deposits for evolved openings and exploitation decisions.
- Remove event-added deposits when the field is closed before Evolution IV.
- If exact removal by stored resource amount is impossible after repo and vanilla inspection, stop and report the blocker instead of inventing a silent fallback.

Needed helper roles:

| Helper role | Why it matters |
| --- | --- |
| Select valid resource state | Prevents invalid state targets and special country issues. |
| Roll resource type | Keeps random resource selection consistent and visible. |
| Add resource deposit | Centralizes baseline and evolved resource adds. |
| Store resource memory | Enables closure cleanup and origin army calculation. |
| Remove event resources | Makes closure sacrifice real. |
| Refresh field owner | Keeps decisions valid after state transfer. |
| Calculate origin army | Preserves user cap around 30 based on exploitation. |
| Refresh Cave Host capacity | Enforces captured-resource division rule. |
| Clear field state | Prevents stale targets and duplicate primary deep sites. |

## Spreadsheet update packet

The event catalog workbook should not be updated from planning direction. It should be updated after final in-game localisation exists.

Future spreadsheet worker instructions:

| Field | Source of truth | Rule |
| --- | --- | --- |
| Event name | final event-name localisation | Use final player-facing name. |
| Details | Event Details window localisation | Mirror final premise text, not effects. |
| Evo I | final evolution detail text | Describe larger and more political resource discovery. |
| Evo II | final evolution detail text | Describe unsafe deep extraction and worker harm. |
| Evo III | final evolution detail text | Describe public monster attacks and closure choice. |
| Evo IV | final evolution detail text | Describe Cave Host emergence and resource-based army. |
| World-End Scenario | final world-end detail text | Describe continental Host end-state if implemented. |
| Type | event classification | Minor Repeatable unless implementation changes with user approval. |
| Cluster ID | final cluster assignment | Economy positive cluster and medium severity if cluster catalog supports it. |
| Member Severity | final cluster row | Medium if cluster integration is implemented. |

Blocked until:

- Final localisation exists.
- Event Details text exists.
- Evolution detail text exists.
- World-end text exists if world-end branch is implemented.
- Cluster integration is implemented or explicitly queued.
- Spreadsheet worker can open the actual workbook.

## Audits required before completion

| Audit | Required reason |
| --- | --- |
| Repo explorer | Confirms file map and syntax before implementation. |
| Scripted system architect | Prevents duplicated resource and capacity logic. |
| Decision mission auditor | Checks field decisions, closure, AI, costs, and exploit risk. |
| Focus tree auditor | Checks Cave Host route coverage and focus rewards. |
| Country package auditor | Checks nonhuman tag, leader, flags, history, focus loading, units, and AI. |
| Localisation auditor | Checks final text, keys, dynamic values, and research gates. |
| Event completion auditor | Compares final implementation against this full spec pack. |
| Spreadsheet worker | Updates workbook only after final text is implemented. |

## Completion blocker statement

The current planning package is deeper after this pass, but repo-confirmed implementation details remain blocked outside this sandbox. Any future agent must not claim that the resource cleanup method, super-event audio wiring, Cave Host tag package, scripted GUI surface, or workbook update is complete until it has inspected and edited the real repository or workbook.
