# Event 017 Random faction completion audit

Date: 2026-07-02
Agent role: `chaosx_event_completion_auditor`
Scope: Read-only completion audit for Event 017 `Random faction`

No project subagent was spawned from this pass. The requested `fork_context=false` constraint was therefore not invoked through a nested agent.

## Overall status

Event 017 is partially implemented, but it does not meet the full Event 17 spec package and should not be treated as complete.

The core event chain exists, dynamically discovers eligible minors and current faction leaders, offers one to four player options, uses shared saved option targets for AI resolution, applies the baseline join/shock/pressure package, registers Event 17 as repeatable, and wires event-log/detail/evolution/localisation/cluster/news/documentation/spreadsheet surfaces. However, several pass/fail requirements from `docs/specs/017_random_faction_specs/prompts/017_random_faction_goal_prompt.md:5` remain simplified or under-validated: full AI behavior, region-scoped Evolution I/III behavior, invalid-country/dead-faction cleanup, achievement disqualifiers, animated UI integration, and required subagent handoff coverage.

## Completion status by surface

| Surface | Status | Evidence |
| --- | --- | --- |
| Event registration and repeatable classification | Complete | `common/script_constants/chaosx_random_faction_constants.txt:14` sets ID 17; `common/scripted_effects/chaosx_logic_effects.txt:199` registers 17 in `global.repeatable_events`; `localisation/english/chaosx_event_names_l_english.yml:19` maps the name. |
| Dynamic eligible minor discovery | Mostly complete | `common/scripted_triggers/017_random_faction_triggers.txt:21` defines eligible minors; `common/scripted_effects/017_random_faction_effects.txt:64` prepares runtime context and `:94` saves `random_faction_target_country`. |
| Dynamic existing-faction discovery | Mostly complete | `common/scripted_triggers/017_random_faction_triggers.txt:66` defines living faction leaders and `:80` validates the leader against the selected country. No Axis/Comintern/fixed-tag hardcode was found by targeted `rg`. |
| Player one-to-four forced options | Mostly complete | `events/017_join_faction.txt:24` opens the player event; `:36`, `:41`, `:46`, and `:51` gate options 1-4; `common/scripted_effects/017_random_faction_effects.txt:134` collects options and `:159-200` saves up to four leader targets. The only extra visible option is the invalid-target recovery option at `events/017_join_faction.txt:57`, allowed by the fallback requirement in `spec_part_3_evolutions_ai_balance.md:262`. |
| AI same target option logic | Partial | `events/017_join_faction.txt:62` uses the hidden AI resolver and `:73-98` selects among the same saved option triggers, but the weighting is simplified compared to the AI matrix. |
| Baseline join, shock, leader memory, pressure | Mostly complete | `common/scripted_effects/017_random_faction_effects.txt:294` adds the target to the chosen faction; `:298` applies alignment shock; `:307` applies regional pressure; `:310` fires `chaosx.news.4`. |
| Evolution I Regional Bloc Race | Partial | Evolution I exists (`common/scripted_effects/017_random_faction_effects.txt:371`) but the pressure application schedules a follow-up for every eligible neighbor when unlocked (`:314-330`), conflicting with the spec cap at `spec_part_3_evolutions_ai_balance.md:63`. |
| Evolution II Pressured Neutrality | Partial | Evolution II pressure exists (`common/scripted_effects/017_random_faction_effects.txt:398`), but it is neighbor-only and does not fully express the spec's wartime/frontier pressure model and broader AI checks. |
| Evolution III Neutrality Collapse | Partial | Cascade caps exist through constants (`common/script_constants/chaosx_random_faction_constants.txt:38-39`) and loop code (`common/scripted_effects/017_random_faction_effects.txt:423-464`), but target selection is global pressure-neighbor based, not a tracked regional cascade. |
| Bloc Pressure decisions and missions | Mostly complete | The named decision families exist in `common/decisions/017_random_faction_decisions.txt:16-397`; the decision-audit handoff records cost/objective fixes. Corridor and target-browsing behavior remain simplified. |
| Decision AI behavior | Partial | Decisions have `ai_will_do` and PP hints in key places, but decision AI remains much thinner than the spec and matrix requirements for ideology, relations, threat, war state, proximity, faction strength, and neutrality resilience. |
| Cleanup and invalidation | Partial | Runtime refresh and pressure clear helpers exist (`common/scripted_effects/017_random_faction_effects.txt:808`), but the only Event 17 on-action cleanup is `on_leave_faction` for Four Doors (`common/on_actions/017_random_faction_on_actions.txt:8-16`). |
| Event log, details, evolutions | Mostly complete | Actor mapping uses `random_faction_target_country` in `common/scripted_effects/chaosx_events_log_effects.txt:159-162`; event detail and evolution selectors/localisation are present. Direct/manual event entry remains less certain than the settings dispatch path. |
| Cluster and news | Complete | Diplomatic Panic cluster wiring references Event 17 in `common/scripted_effects/chaosx_event_cluster_effects.txt:324` and `:424`; news event `chaosx.news.4` exists in `events/_chaosx_news.txt:183-192`. |
| Documentation | Mostly complete | `docs/events/017_random_faction.md` documents the implemented surfaces; `docs/plans/017_random_faction_plans/documentation_state.md` correctly says final completion remains blocked pending this audit. |
| Assets | Partial | Runtime DDS files and `.gfx` definitions exist, but animated seal/warning sprites are registered rather than wired into a visible GUI/scripted GUI surface. The asset manifest also records that the asset subagent stalled and main processing completed the package. |
| Achievements | Partial | Six achievement registrations exist in `common/achievements/chaos_redux_achievements.txt:2428-2485`, but several unlock/disqualifier implementations are simplified relative to the achievement prompt. |
| Spreadsheet | Aligned but overstates status | Read-only workbook check found row ID 17 with `Event Name = Random faction`, `Type = Minor Repeatable`, `Cluster ID = 3`, `Member Severity = Low`, and `Status = Implemented`; the wording matches current localisation. The `Implemented` status conflicts with this audit's partial-completion finding. |

## Missing or simplified requirements

### AI target choice is simplified

The spec requires AI to use ideology, proximity, threat, relations, and military/faction strength (`017_random_faction_ai_matrix.md:7`, `spec_part_3_evolutions_ai_balance.md:169`, `:190`). Current option preference triggers only check ideology match and regional pull (`common/scripted_triggers/017_random_faction_triggers.txt:172-216`), with resolver weights in `events/017_join_faction.txt:75-93`. Relations, faction strength, threat, distance, common enemies, and neutral resilience are not visible in the option scoring.

### Evolution I can over-schedule regional follow-ups

The spec says one baseline firing should schedule at most one delayed neighboring response unless a cluster expands it (`spec_part_3_evolutions_ai_balance.md:63`). Current baseline pressure loops every eligible neighbor and schedules `chaosx.nr17.30` for each when Evolution I is unlocked (`common/scripted_effects/017_random_faction_effects.txt:314-330`). This can create broader follow-up pressure than the accepted design.

### Evolution III is capped, but not region-scoped enough

The spec and catalog matrix call for capped regional cascades (`017_random_faction_catalog_handoff.md:15`, `spec_part_4_implementation_assets_acceptance.md:189`). Current Evolution III uses a global `any_country/random_country` pool of `is_random_faction_pressure_neighbor` targets and a global cascade counter (`common/scripted_effects/017_random_faction_effects.txt:423-464`). It caps follow-ups at 5, but it does not persist or enforce a region/continent/sea-region bucket. The `Not Everyone Signed` achievement check also looks for any pressure neighbor outside a faction, not the original cascade region (`common/scripted_effects/017_random_faction_effects.txt:921-930`).

### Island and isolated regional pressure is not implemented beyond neighbor logic

The spec explicitly says island minors and isolated countries can be selected, and their regional pressure should use sea-region, continent, or faction-reach buckets rather than neighbor-only logic (`spec_part_3_evolutions_ai_balance.md:270`). The current pressure spread and cascade logic use `every_neighbor_country`, `any_neighbor_country`, and `is_random_faction_pressure_neighbor` (`common/scripted_effects/017_random_faction_effects.txt:314-330`; `common/scripted_triggers/017_random_faction_triggers.txt:33-43`). This leaves isolated valid minors with a thinner pressure/evolution surface.

### Cleanup is runtime-refresh based, not full lifecycle cleanup

The spec requires cleanup for invalid countries, dead faction leaders, subjecting, faction changes, and source disappearance (`017_random_faction_decision_mission_prompt.md:14`; `017_random_faction_scripted_system_architecture.md:49`). Current cleanup helpers can clear pressure state and rebuild runtime arrays, but broad lifecycle hooks are missing. `common/on_actions/017_random_faction_on_actions.txt:8-16` only handles leaving a faction for the Four Doors achievement candidate. There are no Event 17 on-action hooks for subject creation, capitulation, annexation/release, dead faction leaders outside runtime refresh, special chaos conversion, world-end state, or mission-owner invalidation.

### Corridor mission remains a weak proof objective

The decision audit improved corridor from a passive wait mission, but the current objective only requires leader visibility, convoys, and any stored guaranteed target (`common/scripted_triggers/017_random_faction_triggers.txt:321-327`). The spec decision map asks for route or supply plausibility (`017_random_faction_decision_map.md:9`, `:13`). The decision effect also clears and stores a local target array at decision time (`common/scripted_effects/017_random_faction_effects.txt:683-705`), but no real supply route, access corridor, sea access, rail, or target-state condition is checked.

### Achievement conditions are simplified

The achievement prompt says not to unlock achievements merely because the event fires and defines specific disqualifiers (`017_random_faction_achievement_prompt.md:12`, `:17`). Current achievement registrations are flag-based (`common/achievements/chaos_redux_achievements.txt:2428-2485`), and several flag setters do not encode the full criteria:

- `017_random_faction_liaison_web` uses a supported-minors counter (`common/scripted_effects/017_random_faction_effects.txt:908-917`) rather than verifying three different supported targets and disqualifying target capitulation or direct enemy status.
- `017_random_faction_frontier_commitment` sets/checks a timed candidate around Evo II and war state, but the hidden check only verifies the candidate flag, capital control, not capitulated, and not subject (`events/017_join_faction.txt:247-255`). The spec asks for capital and all core border states for 180 days.
- `017_random_faction_not_everyone` is global pressure-neighbor based (`common/scripted_effects/017_random_faction_effects.txt:921-930`), not tied to the cascade region.
- `017_random_faction_hold_the_line` starts from border-post success (`common/scripted_effects/017_random_faction_effects.txt:863-871`) but does not visibly require Evolution I+ in the check and does not encode every disqualifier described by the spec.

### Animated assets are produced but not visible in an in-game UI surface

The asset prompt asks for an animated seal on the decision category or scripted GUI header (`017_random_faction_asset_prompt.md:31`, `:43`) and a warning border (`:33`). The `.gfx` file registers frame animated sprites (`interface/017_random_faction.gfx:27-44`), and the manifest lists source/frame-sheet/static fallback assets (`docs/assets/017_random_faction/manifest.md:45-48`). A repository-wide reference check only found those sprites in docs and `.gfx`; gameplay/category code uses only the static category icon and picture (`common/decisions/categories/017_random_faction_categories.txt:8-12`). No `.gui` or scripted GUI surface places the animated seal or warning border on screen.

### Required handoff coverage is incomplete

The coding prompt requires, at minimum, scripted-system, decision, localisation, asset/icon, spreadsheet, documentation, and completion audit handoffs (`017_random_faction_coding_prompt.md:34`). Existing plan handoffs cover decision, localisation, spreadsheet, and documentation. The plans folder does not contain a scripted-system architect handoff or icon-artist/asset subagent handoff. The asset manifest documents a partial asset subagent output and local main-agent processing after the asset subagent stalled (`docs/assets/017_random_faction/manifest.md:9`).

## Accepted plans and disposition

| Plan or prompt package | Disposition |
| --- | --- |
| Four-part source spec under `docs/specs/017_random_faction_specs/specs/` | Accepted source of truth. Implemented partially; several behavioral requirements remain unmet as listed above. |
| `017_random_faction_ai_matrix.md` | Accepted supporting design. Not fully implemented; AI scoring remains simplified. |
| `017_random_faction_decision_map.md` | Mostly implemented through the current decisions and the decision-audit patch; corridor proof, dynamic cost scaling, target browsing, and richer AI remain simplified. |
| `017_random_faction_scripted_system_architecture.md` | Implemented with renamed helpers, but no scripted-system architect handoff exists under `docs/plans`, and cleanup/AI architecture is incomplete. |
| `017_random_faction_catalog_handoff.md` | Superseded by localisation plus spreadsheet worker handoff; workbook row now matches current wording. |
| Asset prompt and icon artist prompt | Asset files were produced and documented, but the planned asset subagent route was superseded by local processing after a stall. Animated assets are not wired into visible UI. |
| Decision audit handoff | Implemented patch handoff. Some previous findings are superseded by later localisation/docs, but corridor proof and cost-scaling limitations remain relevant. |
| Localisation audit handoff | Implemented patch handoff. Its spreadsheet stale note is superseded by the spreadsheet handoff. |
| Spreadsheet handoff | Implemented; read-only audit confirmed row 17 exists and matches current text, but workbook status says `Implemented` despite this audit's partial status. |
| Documentation state/cleanup handoffs | Useful state ledger; correctly says final completion remained blocked pending completion audit. |
| Improvement planner addendum | None found under `docs/plans/017_random_faction_plans/`. |

## Meaningful validation evidence

Performed during this audit:

- Read the full Event 17 spec package, required Event 17 prompt, required skills, Event 17 gameplay surfaces, docs/assets handoffs, current docs, and existing plan handoffs.
- Ran targeted no-hardcode search for Axis/Comintern/fixed major tags across Event 17 implementation surfaces; no implementation hardcode was found.
- Verified representative Event 17 runtime DDS files exist for report images, animated sheets/static fallbacks, and achievement icons.
- Opened `docs/spreadsheets/chaos_redux_events_catalog.xlsx` read-only and confirmed row `ID = 17` exists with current Event 17 name/type/cluster/status/details/evolution text.
- Checked references for animated seal/warning sprites and found them registered/documented but not placed by GUI/scripted GUI/gameplay surfaces.

Validation still missing or not evidenced:

- No live HOI4 launch, parser log, in-game event firing, decision UI screenshot, or event-log UI screenshot is documented in the handoffs.
- No scenario proof that a human selected minor receives 1-4 valid options across 1, 2, 3, and 4+ live faction pools.
- No scenario proof that an invalid saved faction option reopens the same-country choice safely in a live game.
- No scenario proof that AI uses only saved option targets under all fallback paths.
- No scenario proof that Evolution I cannot over-chain, Evolution III remains region-scoped, or cascade caps behave as intended in a dense faction map.
- No scenario proof that corridor/border missions cannot be exploited by immediate target state, stale target flags, or simultaneous faction-leader pressure.
- No scenario proof that achievement disqualifiers match the prompt.

## Asset and documentation gaps

- Runtime asset files and manifests exist, and `docs/assets/017_random_faction/gfx_handoff.md:67` reports no missing runtime DDS paths.
- The asset manifest discloses the asset-subagent stall and local main-agent processing (`docs/assets/017_random_faction/manifest.md:9`), so this is documented rather than hidden.
- Animated UI sprites are not visibly integrated into a decision category header or scripted GUI surface.
- `docs/events/017_random_faction.md` describes current implementation behavior, but some claims are more complete than the code evidence supports, especially the regional cascade description and cleanup breadth.
- Workbook row 17 is aligned to current wording but marks status as `Implemented`, which is premature under this audit.

## Remaining blockers

- Full spec completion is blocked on AI scoring depth, regional follow-up/cascade scoping, lifecycle cleanup, achievement-disqualifier fidelity, animated UI integration, and task-specific validation.
- Required handoff coverage is incomplete for scripted-system architecture and icon/asset subagent work.
- The event technically has a working core, but the living Bloc Pressure/evolution system is not yet at the intended depth.

## Recommended next actions

1. Patch AI option selection to include the accepted matrix factors: ideology, proximity/geography, threat, relations, faction strength, war state, and neutrality resilience.
2. Rework Evolution I scheduling so one baseline firing schedules at most one delayed neighbor response unless a cluster-expanded path explicitly opens more.
3. Add a real regional/continent/sea-region/faction-reach pressure bucket for Evolution III and `Not Everyone Signed`, then tie cascade cap/resistance checks to that bucket.
4. Extend cleanup with targeted lifecycle hooks or scoped refresh calls for subjecting, annex/release, capitulation, invalid faction leaders, special chaos conversion, world-end state, and stale mission/target state.
5. Strengthen corridor proof beyond convoy presence and target flag, or document and explicitly accept the current abstraction as a simplification.
6. Align achievement flag setters/checks with the achievement prompt disqualifiers, especially Liaison Web distinct targets, Frontier Commitment border-state control, and Not Everyone regional persistence.
7. Wire the animated seal/warning assets into a visible UI surface, or explicitly reject the animated presentation requirement and document why.
8. Add or recover scripted-system and icon/asset handoffs, or document why those prompt requirements were superseded.
9. Update the workbook status away from `Implemented` until this audit's blockers are resolved.
10. After fixes, run task-specific validation scenarios for option counts, dead faction fallback, AI option reuse, Evolution I cap, Evolution III region cap, mission exploit resistance, event-log/detail display, and achievement disqualifiers.

## Improvement loop recommendation

Route `chaosx_improvement_loop_planner` before a final completion claim unless the main agent directly patches the full spec gaps above. No unresolved Event 17 improvement addendum was found in `docs/plans/017_random_faction_plans/`, and the current implementation works at the core-event level but does not yet meet the intended depth for Bloc Pressure, regional cascades, AI behavior, and achievement proof.
