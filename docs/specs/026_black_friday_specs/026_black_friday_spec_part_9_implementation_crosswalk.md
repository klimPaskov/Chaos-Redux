# Implementation crosswalk and completion contract

## Current repository replacement

The pre-implementation repository snapshot used Event 26 for a desert-industry event through `events/026_industry_to_desert.txt` and `localisation/english/026_industry_to_desert_l_english.yml`. The snapshot's fire-once registry comment also identified Event 26 as moving industry to the desert; those surfaces are replacement targets, not current runtime content.

Implementation must replace that identity completely while keeping the stable namespace and entry ID.

Recommended file changes include:

| Current surface | Required Event 26 result |
| --- | --- |
| Pre-implementation `events/026_industry_to_desert.txt` | Replace with `events/026_black_friday.txt`, preserving `chaosx.nr26.1` as the entry |
| Pre-implementation `localisation/english/026_industry_to_desert_l_english.yml` | Replace with Event 26 Black Friday localisation in a matching event-owned file |
| Pre-implementation Event 26 news call and desert news localisation | Remove stale Event 26 ownership and verify that no unrelated news ID is damaged |
| Event registry comment | Change to Black Friday while keeping ID 26 in the fire-once array |
| Default disabled rework list | Keep disabled during implementation, then remove ID 26 from the rework-disabled allowlist in the completion change |
| Manual trigger routing | Route ID 26 to the new entry and preserve normal versus force behavior |
| Event name and debug selectors | Map ID 26 to Black Friday |
| Event Details | Add premise, status, and Evolution I preview |
| Catalog workbook | Replace the old ID 26 row and resolve the no-ID duplicate |

Search the repository for every old identifier and phrase before completion, including `026_industry_to_desert`, `Desert Industry`, `Move Industry to desert`, `Operation Desert Forge`, `GFX_report_event_desert`, and Event 26 comments.

## Event-owned files

Recommended event-owned surfaces are:

- `events/026_black_friday.txt`
- `common/script_constants/026_black_friday_constants.txt`
- `common/scripted_effects/026_black_friday_effects.txt`
- `common/scripted_triggers/026_black_friday_triggers.txt`
- `common/on_actions/026_black_friday_on_actions.txt` only for a narrow event-owned hook that is called from an existing bounded global pulse
- `common/ideas/026_black_friday_ideas.txt` for the temporary human-player status marker
- `common/dynamic_modifiers/026_black_friday_dynamic_modifiers.txt` only when a verified native cost modifier requires it
- `common/scripted_localisation/026_black_friday_scripted_localisation.txt`
- `localisation/english/026_black_friday_l_english.yml`
- `interface/026_black_friday.gfx`
- `docs/events/026_black_friday.md`
- `docs/systems/universal_cost_modifier.md`

Each new script file needs a short overview at the top.

## Shared event-system files

Inspect and update these shared surfaces as required:

- `common/scripted_effects/chaosx_logic_effects.txt`
- `common/scripted_effects/chaosx_settings_effects.txt`
- `common/scripted_effects/chaosx_events_log_effects.txt`
- `common/scripted_guis/chaosx_scripted_gui_events_log.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_debug.txt`
- `localisation/english/chaosx_event_names_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`
- the existing global event-system daily pulse in `common/on_actions/chaosx_on_actions_system.txt` or its current authoritative equivalent

Shared files should call event-owned helpers. They should not absorb the entire Black Friday implementation.

## Shared cost framework files

The scripted system architect should determine whether the public quote and payment API belongs in:

- the existing `common/scripted_effects/chaosx_dynamic_effects.txt` and matching documentation
- a new shared `common/scripted_effects/universal_cost_modifier_effects.txt` with matching system documentation
- a combination of shared public helpers and event-owned source registration

The selected structure must centralize:

- source IDs and payment ratios
- cost-family IDs
- rounding quanta
- quote outputs
- affordability checks
- payment and refund contracts
- source display data
- achievement family recording

Every new public helper must have documented scope, inputs, outputs, defaults, side effects, and a usage example.

## Owner-file coverage changes

The implementation will touch many cost owner files. The cost registry is the authority for that list.

For each owner file:

1. Identify the logical action.
2. Classify its cost and payment path.
3. Select coverage strategy A, B, C, or D.
4. Patch display and payment together.
5. Preserve AI and lifecycle behavior.
6. Add a task-specific test.
7. Record the final status in the registry.

Do not place all static variants in one unrelated Event 26 decision file. Keep variants with the owning system or use a verified shared adapter that preserves ownership.

## Assets and achievements

Required runtime assets include:

- `gfx/event_pictures/026_black_friday/<report_basename>.dds`
- `gfx/interface/ideas/026_black_friday/<status_icon_basename>.dds`
- the Event 26 achievement triplet in `gfx/achievements/`

Update:

- `interface/026_black_friday.gfx` or the selected event-owned sprite file
- `common/achievements/chaos_redux_achievements.txt`
- achievement localisation
- event and status idea references

The asset worker provides source, processed PNG, DDS, manifest, contact sheet, and handoff. The parent wires non-portrait sprites.

## Authoritative catalog update

Edit only `docs/spreadsheets/chaos_redux_events_catalog.xlsx`. After saving, run `python .tools/export_event_catalog_csv.py` from the mod root.

The implementation change should mark Event 26 as `Needs Testing` until the requested live acceptance scenarios pass. A later live-tested completion can move it to the project's accepted playable status.

## Required repository and engine review

Before coding, the implementation agent must inspect:

- the required offline wiki pages listed in `AGENTS.md`
- installed Vanilla documentation for events, effects, triggers, modifiers, decisions, ideas, characters, intelligence, cost fields, and script constants
- at least one Vanilla precedent for each native cost strategy used
- current Chaos Redux quote, pay, refund, reserve-floor, static-variant, and event-log patterns
- current HOI4 MCP event-chain and probability routes

A missing MCP route remains an explicit validation blocker for that surface.

## Implementation order

1. Create the Event 26 constants, state machine, triggers, and event-owned helpers.
2. Add the reservation adapter to the random-event system and existing daily pulse.
3. Implement the universal cost source and quotation contract.
4. Build the complete cost surface registry from the current repository and installed Vanilla data.
5. Patch dynamic and static cost owners in bounded families.
6. Add the event popup, active status, event-log, Event Details, evolution, and debug mappings.
7. Add AI validity checks and run probability audits for changed weighted surfaces.
8. Create and wire assets and the achievement.
9. Update event docs, system docs, and the authoritative workbook.
10. Run structural, task-specific, and live acceptance scenarios.
11. Run decision, localisation, probability, and event completion audits.
12. Remove the Event 26 rework-disabled default only when all required surfaces are ready for normal selection.

## Required subagent handoffs during implementation

Use project subagents with `fork_context=false` when the implementation environment exposes them.

Required or likely handoffs are:

- `chaosx_scripted_system_architect` for the universal cost framework and reservation adapter
- `chaosx_decision_mission_auditor` for cost owners, static variants, cleanup, and exploits
- `chaosx_ai_probability_auditor` for every changed weighted surface
- `chaosx_generated_event_art` for the report image
- `chaosx_icon_artist` for the status icon and achievement art
- `chaosx_localisation_auditor` for all Event 26 and cost text
- `chaosx_spreadsheet_doc_worker` for the authoritative workbook and CSV export
- `chaosx_event_completion_auditor` before any completion claim

A dedicated event UI worker is used only if implementation adds an accepted Event 26-owned scripted GUI. This specification uses the existing event and status surfaces.

## Completion evidence

The completion report must include:

- files changed
- final Event 26 state machine and timer behavior
- complete cost registry with every row dispositioned
- list of native, scripted, static, and inaccessible surfaces
- cost composition and rounding evidence
- AI audit scenario results
- event-chain MCP evidence
- Friday and save-reload live results
- multiplayer results or exact blocker
- assets created and wired
- achievement implementation and test
- Event Details, event log, and evolution evidence
- workbook row and exporter result
- removal of stale desert-industry references
- every blocker, omission, and simplification

## Hard completion blockers

Do not mark Event 26 complete when any of these remain:

- the old desert event can still fire
- Event 26 can reserve twice
- reservation stalls ordinary event timers
- activation counts as two events
- displayed and paid prices differ
- a positive cost can become zero
- refund returns more than the paid amount
- normal and discounted variants appear together
- the active ratio changes with chaos after activation
- expiry removes another source or leaves a stale discount
- a discovered cost owner lacks a registry disposition
- a strategy D surface is hidden from the report
- AI evaluates duplicate variants or invalid cheap actions
- Event Details, event logs, evolution, docs, or workbook are stale
- required assets are missing or unwired
- the default rework-disabled state is removed before the feature is ready
