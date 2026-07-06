# Follow-Up Coding Prompt: Event 011 Secret Alliance

Implement Event 011 Secret Alliance from the source specs in `docs/specs/011_secret_alliance_specs/`.

Required skills before editing:

- `chaos-redux-events`
- `hoi4-decisions-missions`
- `hoi4-mtth`
- `chaos-redux-super-events` when wiring the reveal super-event
- `chaos-redux-event-assets` when wiring icons or report/super-event art

Required local references:

- offline `paradox_wiki/` pages listed in `research/011_secret_alliance_source_review_manifest.md`
- vanilla docs under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation`
- vanilla faction template and WTT border conflict examples
- Event 017 Random Faction specs and implementation patterns

Implementation goals:

- keep entry event root `chaosx.nr11.1`
- replace the Event 011 unavailable placeholder
- initialize exactly three valid hidden founders or fail cleanly
- keep the pact hidden until reveal or Evolution III public bloc state
- add Evolution I, II, and III behavior with active-event and pre-fire paths
- add player countermeasures at Evolution II
- use dynamic variables, constants, MTTH entries, scripted triggers, and scripted effects
- use `create_faction_from_template` at reveal
- trigger the reveal super-event and call valid members into the player war
- update event logs, event details, localisation, docs, assets, and spreadsheet/catalog alignment

Hard constraints:

- no broad `on_daily`, `on_weekly`, or `on_monthly` iteration without explicit user approval
- no raw `create_faction`
- no fallback static faction name unless dynamic naming is proven impossible and the user approves the replacement
- no magic-number tuning scattered through effects and decisions
- no final completion claim without localisation, icons, logs, details, cleanup, AI, and meaningful audits

Useful package files:

- `specs/011_secret_alliance_spec_part_1_core_pact.md`
- `specs/011_secret_alliance_spec_part_2_evolutions.md`
- `specs/011_secret_alliance_spec_part_3_decisions_sabotage.md`
- `specs/011_secret_alliance_spec_part_4_ai_balance_assets_acceptance.md`
- `matrices/011_secret_alliance_scripted_system_architecture.md`
- `matrices/011_secret_alliance_decision_map.md`
- `matrices/011_secret_alliance_implementation_handoff.md`

