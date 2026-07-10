# Documentation state

## Source-of-truth map

| Area | Current source |
| --- | --- |
| Core event design | `specs/011_secret_alliance_spec_part_1_core_and_hidden_pact.md` |
| Progression and evolutions | `specs/011_secret_alliance_spec_part_2_progression_and_evolutions.md` |
| Counterplay and decisions | `specs/011_secret_alliance_spec_part_3_counterplay_and_decisions.md` |
| Reveal, war, scenario, and super-event role | `specs/011_secret_alliance_spec_part_4_reveal_war_and_scenario.md` |
| AI, presentation, balance, and acceptance | `specs/011_secret_alliance_spec_part_5_ai_presentation_and_acceptance.md` |
| Event family map | `matrices/011_secret_alliance_event_chain_map.md` |
| Decision and mission detail | `matrices/011_secret_alliance_decision_mission_matrix.md` |
| AI behavior | `matrices/011_secret_alliance_ai_strategy_matrix.md` |
| Tuning relationships | `matrices/011_secret_alliance_tuning_model.md` |
| Asset coverage | `matrices/011_secret_alliance_asset_register.md` |
| Achievements | `matrices/011_secret_alliance_achievement_matrix.md` |
| Research basis | `research/011_secret_alliance_historical_research.md` and bibliography |
| Super-event text research | `research/011_secret_alliance_super_event_text_research.md` |
| Implementation direction | files under `prompts/` |
| Specialist disposition | files under `handoffs/` |

## Working-label policy

Names marked as working labels are not final localisation. This includes:

- route labels
- decision names
- achievement titles
- scenario public name
- super-event title direction
- internal helper proposals
- proposed sprite names not yet registered

The implementation agent must write or confirm final player-facing names and preserve stable engine identifiers once registered.

## Plan disposition

| Planning item | Disposition |
| --- | --- |
| Main five-part spec | Source design, ready to place under `docs/specs/011_secret_alliance_specs/` |
| Historical research | Supporting source note |
| Super-event quote research | Supporting source note, final title and audio still require implementation research |
| Focus-tree expansion | Rejected as bloat |
| New country package | Rejected as contrary to procedural design |
| Formable | Rejected as unrelated |
| World-end branch | Omitted because it is not part of the event design |
| Triggerable scenario | Accepted source design |
| One animated warning | Accepted source design |
| Additional animated UI | Rejected as readability cost |
| Improvement-loop review | Closed with no expansion addendum |

## Implementation documentation to create or update

- `docs/events/011_secret_alliance.md`
- `docs/plans/011_secret_alliance_plans/subagent_handoffs/`
- `docs/assets/011_secret_alliance/manifest.md`
- `docs/assets/011_secret_alliance/gfx_handoff.md`
- `docs/super_events/011_secret_alliance_super_event_research.md`
- triggerable-scenario system documentation
- music track table
- dynamic helper documentation when new helpers are added
- event catalog workbook

## Contradiction review

No contradiction remains between the user's catalog brief and the spec on:

- three initial minor founders
- preference for factionless countries
- no initial war with target
- hidden beginning
- continued invitations
- Evolution I through III
- major entry at Evolution II
- optional second major at Evolution III
- direct player counterplay at Evolution II
- public faction visibility at Evolution III
- immediate reveal and universal active-member war entry when one member enters war
- reveal super-event
- no event cluster
- direct coalition-war scenario

The design clarifies one edge case. “All pact members” at wartime reveal means all current valid active members after cleanup. A country that ceased to exist, joined the target faction, became an incompatible subject, or was explicitly removed is no longer an active member.

## Resume note

The next agent should start from the coding prompt and use the repo explorer handoff to confirm file paths and identifiers. It should not redesign the event before implementation unless a verified engine constraint conflicts with the source design.
