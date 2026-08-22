# Systems player-facing copyedit handoff

Date: 2026-08-02

Scope: explicit player-facing, UI-facing, and localisation-mirroring prose under `docs/systems/**`.

This pass does not claim gameplay, localisation, workbook, asset, or live consumer completion. Gameplay identifiers, localisation keys, dynamic tokens, numeric values, route gates, and implementation contracts were preserved.

## Source-of-truth map

| Surface | Current authority | Disposition |
| --- | --- | --- |
| Shared system player-facing summaries | The current system notes in `docs/systems/air_cleanliness/air_contamination_mechanic.md`, `docs/systems/cbrn_warfare/biological_warfare/biological_sabotage.md`, `docs/events/020_black_plague/rat_route_modules.md`, `docs/systems/cbrn_warfare/cbrn_action_records.md`, `docs/systems/cbrn_warfare/cbrn_diplomacy_actions.md`, `docs/systems/cbrn_warfare/cbrn_operations_surface.md`, `docs/systems/cbrn_warfare/chaos_unit_family_registry.md`, `docs/systems/event_system/event_clusters.md`, `docs/systems/cbrn_warfare/genocide/genocide_crisis_system.md`, `docs/systems/chaosx_settings/settings_miscellaneous_menu.md`, `docs/systems/state_map_modes.md`, and `docs/systems/event_system/triggerable_scenarios.md` | Copyedited in place where the prose described a player-facing surface or mirrored localisation. |
| Accepted event and system design | Named specifications under `docs/specs/**` and the event-owned contracts referenced by the systems notes | Not rewritten. They remain design authority and require parent review when their wording is intentionally historical or prompt-like. |
| Event Log world-end catalog | `docs/systems/event_system/events_log_world_end_scenarios.md` and its live registry references | Left unchanged. The document already states that it supersedes partial Event 14 handoffs. |
| Runtime English localisation | Referenced `localisation/english/*.yml` files | Not edited by this subagent. Localisation owners retain responsibility for runtime parity. |
| Event catalog workbook | `docs/spreadsheets/chaos_redux_events_catalog.xlsx` | Not opened or edited. Spreadsheet alignment remains with the spreadsheet worker. |

## Files changed

- `docs/systems/air_cleanliness/air_contamination_mechanic.md`
- `docs/systems/cbrn_warfare/biological_warfare/biological_sabotage.md`
- `docs/events/020_black_plague/rat_route_modules.md`
- `docs/systems/cbrn_warfare/cbrn_action_records.md`
- `docs/systems/cbrn_warfare/cbrn_diplomacy_actions.md`
- `docs/systems/cbrn_warfare/cbrn_operations_surface.md`
- `docs/systems/cbrn_warfare/chaos_unit_family_registry.md`
- `docs/systems/event_system/event_clusters.md`
- `docs/systems/cbrn_warfare/genocide/genocide_crisis_system.md`
- `docs/systems/chaosx_settings/settings_miscellaneous_menu.md`
- `docs/systems/state_map_modes.md`
- `docs/systems/event_system/triggerable_scenarios.md`

The edits split sentence joins, removed the only em dash in `docs/systems/**`, replaced staged contrast framing with direct statements, and joined hard-wrapped prose in the touched Event 19 and provider-identity sections. Scenario counts, route names, state predicates, category names, asset identifiers, and evidence references remain unchanged.

## Unresolved plan and handoff disposition

| Document or work item | Disposition | Reason |
| --- | --- | --- |
| Systems copyedit pass recorded here | Implemented | The scoped documentation edits are present in the twelve files above. |
| `docs/plans/player_facing_text_style_cleanup/subagent_handoffs/documentation_cleanup_handoff.md` | Left unchanged | It covers `docs/events/**`, `docs/specs/**`, and `docs/super_events/**`, which are outside this subagent's ownership. |
| `docs/plans/player_facing_text_style_cleanup/subagent_handoffs/super_event_draft_copyedit_handoff_2026-08-02.md` | Left unchanged | It covers plan-side super-event drafts rather than systems notes. |
| Existing biological, camp, CBRN, 001 to 004, 006, and 014 to 017 localisation handoffs in the same folder | Left unchanged | Those handoffs own runtime English localisation and preserve the split ownership boundary. |
| `docs/systems/event_system/event_clusters_spec.md` | Queued for parent decision | The file is titled `Chaos Redux Event Cluster System Prompt` and still uses imperative implementation language. The current implementation narrative is in `docs/systems/event_system/event_clusters.md`. |
| `docs/systems/cbrn_warfare/genocide/genocide_mechanics_spec.md` | Superseded notice already present | Its opening note identifies the implemented authority and explains which older concepts are superseded. |

## Contradictions and stale-source findings

- `docs/systems/event_system/event_clusters_spec.md` reads as an implementation prompt while `docs/systems/event_system/event_clusters.md` reads as the current implementation contract. This is a source-role conflict, not a gameplay change introduced by this pass. The parent should decide whether to retain the prompt as historical design or add a superseded notice that links to the implementation note.
- `docs/systems/event_system/triggerable_scenarios.md` and `docs/systems/cbrn_warfare/genocide/genocide_crisis_system.md` contain historical audit and completion statements. They were preserved as evidence. The parent should confirm their dates and status before a release documentation freeze.
- The CBRN operations note retains a fail-closed engine-boundary statement. This is consistent with the documented route boundary, but the parent should keep that statement aligned with any later runtime-hook audit.
- No incompatible player-facing route names, counts, state predicates, or category names were found in the scoped copy.

## Duplicate or superseded document list

- No duplicate current systems summary was found among the twelve edited files.
- `docs/systems/event_system/events_log_world_end_scenarios.md` explicitly supersedes partial Event 14 public-details handoffs. No additional notice was needed.
- `docs/systems/cbrn_warfare/genocide/genocide_mechanics_spec.md` is an historical concept document with an existing superseded-content notice.
- `docs/systems/event_system/event_clusters_spec.md` is the only systems file that still presents itself as a prompt. It remains queued for the parent decision listed above.

## Stale prompt or instruction list

- `docs/systems/event_system/event_clusters_spec.md` contains direct instructions such as `Implement an event cluster system` and `Keep iterating`. Those instructions are not player-facing copy and were not silently rewritten. They should be archived, marked historical, or promoted into the accepted specification by the parent.
- Asset prompt, manifest, and handoff references in the systems notes are provenance links. They were left unchanged because they are not visible game text.
- Runtime and parent-agent instructions in `docs/systems/3d_model_pipeline/overview.md` are outside this copyedit scope and remain unchanged.

## Contradictions not resolved by this pass

The source-role issue around `event_clusters_spec.md` remains open. Historical completion claims remain open for parent confirmation. No player-facing wording conflict required a design choice during this pass.

## Validation

- An em-dash scan across `docs/systems/**` returned no matches after the copyedit.
- Focused semicolon review of the twelve touched files found remaining semicolons only in technical paragraphs, list separators, table data, or process notes outside the scoped player-facing copy. The remaining engine-boundary example is `docs/systems/cbrn_warfare/cbrn_operations_surface.md`.
- `git diff --check` for the twelve touched systems files completed without whitespace errors.
- A manual diff review confirmed that identifiers, route names, counts, dynamic references, and implementation claims were not changed by the prose edits.
- No game launch, runtime localisation test, workbook export, asset inspection, or gameplay validation was run because this handoff owns documentation surfaces only.

## Remaining risks and parent actions

- Runtime English localisation and workbook wording may still diverge from the cleaned system summaries. The owning localisation and spreadsheet agents must reconcile those surfaces.
- The parent should decide the disposition of `event_clusters_spec.md` before final documentation freeze.
- The parent should recheck dated completion statements when integrating this handoff. This subagent did not claim those implementation results.
- No gameplay simplification or fallback was introduced in this documentation pass.

No commit was created. The parent agent retains final integration and commit ownership for the shared worktree.
