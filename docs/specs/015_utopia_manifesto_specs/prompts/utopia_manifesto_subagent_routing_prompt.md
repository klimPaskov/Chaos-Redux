# Utopia Manifesto subagent routing prompt

Use this routing handoff when implementing Event 015 `utopia_manifesto`.

All project custom subagents must be spawned with `fork_context=false`. The parent prompt must pass explicit context. Do not rely on inherited conversation state.

## Mandatory near-completion loop

`chaosx_improvement_loop_planner` is mandatory for this goal because Event 015 changes event design, focus trees, decisions, subject mechanics, assets, super-events, achievements, and implementation handoffs.

Run it after a meaningful implementation tranche and before the final completion audit. The prompt must pass:

- event id `015`
- slug `utopia_manifesto`
- current goal
- user constraints
- source spec paths under `docs/specs/015_utopia_manifesto_specs/`
- implemented surfaces
- unresolved blockers
- accepted plans
- queued plans
- rejected plans
- asset and super-event status
- exact question: identify remaining shallow systems, disconnected mechanics, missing route depth, missing AI, missing asset states, missing aftermath, or scope bloat

The planner may return an expansion addendum or a closure handoff. Resolve it before any completion claim.

Valid dispositions:

- implement the addendum now
- fold accepted content into `docs/specs/015_utopia_manifesto_specs/`
- queue it with a clear reason
- reject it with a clear reason
- record the closure handoff and finish only the final tasks it lists

If the loop subagent cannot be spawned because the tool is unavailable, record that as a blocker and do not claim full completion.

## Routing table

| Surface | Subagent | Use timing | Parent owns |
| --- | --- | --- | --- |
| File mapping if uncertain | `chaosx_repo_explorer` | before broad implementation only when touched files or precedent are unclear | final edit order and implementation |
| Reusable helpers and dynamic values | `chaosx_scripted_system_architect` | before duplicating Need Ledger, subject, target, or cleanup logic | final wiring and design fidelity |
| Focus tree | `chaosx_focus_tree_auditor` | after the tree exists or has a large implemented tranche | route coverage, fixes, final layout quality |
| Decisions and missions | `chaosx_decision_mission_auditor` | after Need Ledger, enforcement, and subject decisions exist | final decision balance and cleanup |
| Country and subject packages | `chaosx_country_package_auditor` | after subject forms, cosmetic identities, and any tag work exist | final package validity and gameplay use |
| Localisation | `chaosx_localisation_auditor` | after broad player-facing text exists | final tone, research gates, and key alignment |
| Visual source assets | `chaosx_asset_source_researcher` | for real printed material, real symbols, or sourced images | final wiring and source acceptance |
| Generated non-icon art | `chaosx_generated_event_art` | for fictional portraits, flags, panels, and scene art | final wiring and manifest review |
| Icons | `chaosx_icon_artist` | for focus, idea, decision, category, achievement, and small GUI icons | final sprite wiring and icon coverage |
| Super-event text | `chaosx_super_event_text_researcher` | before final super-event title, quote, button remark, or reference wording | final localisation and implementation |
| Super-event audio | `chaosx_super_event_audio_researcher` | before final audio wiring | final audio wiring and docs |
| Documentation cleanup | `chaosx_documentation_curator` | after several handoffs or near the end if docs may conflict | source-of-truth decisions |
| Spreadsheet | `chaosx_spreadsheet_doc_worker` | after implementation wording exists | event catalog alignment |
| Final completion | `chaosx_event_completion_auditor` | after the improvement loop has a recorded disposition | final completion claim |

## Required ordering near completion

1. Finish the main implementation tranche.
2. Run focused auditors for surfaces that now exist.
3. Resolve small audit patches or queued plans.
4. Spawn `chaosx_improvement_loop_planner` with `fork_context=false`.
5. Resolve the loop output.
6. Run final completion audit.
7. Finish docs, spreadsheet, assets, and completion report.

Do not reverse steps 4 and 6. The final completion audit must see the loop output and its disposition.
