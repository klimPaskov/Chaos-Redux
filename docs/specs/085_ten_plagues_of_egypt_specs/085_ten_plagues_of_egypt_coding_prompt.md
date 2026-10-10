# Event 085 — Full Implementation Prompt

Implement Ten Plagues of Egypt from `docs/specs/085_ten_plagues_of_egypt_specs/`.
Read the README (authority table, canonical homes, implementation gates, open questions), the original brief, all eighteen parts and the narrative source notes before editing.
The brief is the user's explicit direction; accepted and proposed design are distinguished in the README.
Do not implement an open question's proposal as settled design without the user's decision; where the README names an implementation default, keep it easy to change.

Follow the repository rules (`CLAUDE.md`) and the `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-subagents`, `chaos-redux-event-assets`, `chaos-redux-super-events`, `chaos-redux-mtth` and `chaos-redux-improvement-loop` skills.
No country, focus tree, formable, doctrine, technology, portrait or 3D unit is part of this design.

## Start from current source

- Read the relevant offline wiki and installed documentation sections through the reference workflow for events, decisions, ideas and dynamic modifiers, scopes, on actions, localisation and AI.
- Read the current owner documentation and code for Deaths (`apply_exact_state_civilian_population_loss`), Famine (adapter and Hunger Lines precedent), Migration (incident adapter, passage and reception actions), the biological outbreak owner, Natural Disasters (`call_natural_disaster`), Evolutions, scenarios, world-end catalog, world-threat sources, Condemnation records and achievements.
- Inspect the legacy `events/085_xp.txt`, its registration, localisation and catalog row; replace the XP event at ID 85 without renumbering neighbors.

## Implement

- One global episode from `chaosx.nr85.1`; Major, Chaos level 3, Natural Disasters Severe member only, fire-once natural and cluster entry, Major pacing committed once (Part 1).
- The ten plagues in order with the Part 1 calendar in script constants, local footprints, warnings that are never shortened, and phase effects through one crisis spirit within the Part 15 ceilings.
- Divine Wrath, Harden Our Hearts and the conduct rules in Part 2, including the Condemnation link.
- The fourteen action families and cost model in Part 14, with full, partial, failure and cleanup paths.
- Darkness for 72 hours with a real global visual (Part 7); Passover status per state; the tenth plague settled once per state from the shared deadline with the remaining firstborn share (Part 8).
- Evolutions, Exodus requests, global Wrath weighting, recurrence, the world-end branch with its world-threat source, and escape (Parts 9 and 10).
- Mourning, political directions and Reconstruction Coordination (Part 11).
- SCN-032 with the four Part 12 profiles in the shared scenario registry.
- The Part 13 Chaos impact map with its guards; deaths add Chaos only through Deaths.
- Event log, event details, history, cluster membership, localisation and catalog alignment through the events skill.
- The package-owned idempotent CXT setup registration required by the repository rules.

## Implementation gates

Resolve these with the owning system rather than substituting a flat national effect: the non-weapon outbreak entry (Part 13), the composite Hail and Fire call (Part 6) and the global Darkness presentation (Part 7).
If one cannot be built, record the exact missing owner capability and stop for the user's decision; README open question 2 covers the outbreak case.

## Assets, super-events and achievements

- Assets: the [asset prompt](085_ten_plagues_of_egypt_asset_prompt.md) and Part 16 inventory of 91 static outputs.
- Super-events: the [super-event prompt](085_ten_plagues_of_egypt_super_event_prompt.md); unresearched text and placeholder audio stay blocked.
- Achievements: the [achievement prompt](085_ten_plagues_of_egypt_achievement_prompt.md) and Part 18.
- Decisions and missions: the [decision and mission prompt](085_ten_plagues_of_egypt_decision_mission_prompt.md).

Player-facing text is concrete and free of implementation or tuning wording; localisation files are UTF-8 with BOM.

## Delegation and checks

Route bounded work through `chaos-redux-subagents` with self-contained prompts: systems to `chaosx_scripted_system_architect`, decisions to `chaosx_decision_mission_auditor`, weights to `chaosx_ai_probability_auditor` using the Part 15 anchors, localisation to `chaosx_localisation_auditor`, art and super-event research to their named roles.
Use `chaosx_event_ui_worker` only if the Darkness presentation becomes an Event 085-owned interface layer.
Use HOI4 MCP inspection where it answers a concrete question, within the repository retry limits; when a tool or specialist is unavailable, do the review directly and record the limit.
Cover the Part 15 acceptance cases and the Part 18 negative cases.
Near completion, run `chaosx_improvement_loop_planner` and resolve its handoff, then `chaosx_event_completion_auditor`.
Do not launch the game; live validation belongs to the user.

## Documentation and catalog

Write `docs/events/085_ten_plagues_of_egypt/overview.md` and keep working evidence under `docs/plans/085_ten_plagues_of_egypt_plans/`.
Update `docs/spreadsheets/chaos_redux_events_catalog.xlsx` and the Natural Disasters cluster row through the spreadsheet worker after final wording exists, then run `python .tools/export_event_catalog_csv.py`; never edit the CSV exports.

Keep iterating until the accepted specification is implemented to its fullest extent, and report every simplification, unresolved gate and changed file.
