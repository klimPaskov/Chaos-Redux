# Event 032 agent decisions — 2026-10-04

Authority: the user granted the implementing agent full authority to take the recommended, spec-consistent option and record it here.
Each entry is an agent decision with its acceptance basis; implementation evidence is linked where it exists.

## Lead decisions carried into this round

1. The stopped thread's uncommitted fixes for the seven routed lint defects are adopted rather than rewritten. Basis: they match the routed fixes, use the shared `chaosx_convert_days_to_date_offset` and `chaosx_convert_date_offset_to_days` helpers with the output temporaries preset, and every `.tools/test_event32_*.py` test passes. Disposition: `implemented`.
2. Evolution pacing uses one bounded delayed job per track, armed when the track first becomes eligible, with a randomised delay derived from its base MTTH and shortened by pressure; firings remain a fallback. The architect's full pressure ledger, hostile-pair registry and hazard-clock worker from `subagent_handoffs/032_evolution_pacing_architecture_2026-10-03.md` are `rejected` for this round. Basis: spec part 4 allows bounded delayed evolution jobs created when a threshold is first met, and the larger design adds maintenance cost with no player-visible difference.
3. Saturation doctrine and retaliation posture are explicit country decisions, and an unlock grants access only. Basis: spec part 4 lets a country decline or delay adoption and requires posture adoption to carry requirements, costs and a cooldown.
4. Missing decision families reuse the existing localisation keys, cost keys and same-family decision icons. No new art and no scripted GUI. Basis: spec decision 4.
5. `rejected` optional scope: changing the participating site or increasing preparation effort for a prepared operation (part 5 says "where allowed"), and redirecting the retaliation target after new evidence (the decision prompt allows it only when the accepted spec and engine proof permit it).
6. The physical custody model stays: the aggregate reserve is authoritative with a greedy whole-missile projection onto sites. Only the equal-split operation allocation is fixed.
7. No native raid route or icon is added; the accepted conditional scripted route in spec part 8 stands.
8. Event 032 returns to the default-enabled list only after the priority 1 and 2 gameplay items land. The catalog status change is staged in `catalog_changes_pending.md`; the workbook and CSV exports are not edited.
9. HOI4 MCP is used only with narrow queries, and timeouts are recorded as exact blockers rather than retried.
10. The duplicate native id stays a live-only item, and the temporary allocation markers remain until a fresh log attributes the error.

## Implementation decisions taken during the round

- The stray `.tools/commit_event32_scn015_qa_message_temp.txt` commit-message scratch file from the SCN-015 repair is removed; it was never part of the mod.
- The untracked probability-matrix audit handoff and its evolution-gate scenario fixture from 2026-10-03 are adopted as finished read-only evidence. Their legacy-toggle findings were already repaired by `032_evolution_toggle_binding_repair_2026-10-03.md`; the handoff stays as dated evidence.

## Item 2: project missions with reachable success paths

Disposition: `implemented` (source evidence below; live behaviour `needs_live_game`).

- Each project owns a separate state pointer and due date: `missiles_survey_site_state`, `missiles_secondary_site_state`, `missiles_repair_site_state`, and `missiles_recovery_site_state`. The shared `missiles_pending_site_state` is retired so a survey, construction, repair, and recovery can never overwrite each other.
- New timing constants: `survey_mission_days = 60` (spec part 5 asks for a short survey) and `site_recovery_mission_days = 14`. Secondary construction keeps 90 days, repair 45, verification 3, and restoration 60. Every due date is shorter than its native mission timeout.
- The rogue-site recovery mission timeout is 30 days, aligned with `missiles_rogue_tuning.crisis_window_days`; after that the rogue crisis resolves through its own timeout event and the mission cancels. Recovery needs more than `@m32_mission_recovery_division_floor = 1` divisions in the rogue site's state; AI countries are exempt from the division test because the AI cannot be ordered to garrison a named state.
- A successful repair clears all damage, applies one capacity-recovery step, and returns the site to service. A cancelled or expired repair returns the suspended site to service in its current condition. Suspension uses the new state flag `missiles_site_suspended`, which `missiles_site_can_launch` rejects, and can target wrecked (`damaged_beyond_use`) sites that previously had no repair route.
- Suspension is offered in the incident and maintenance phases (target array: the country's own site registry), because a damage incident can be inspected and closed before repair starts.
- Survey and secondary-site failure refunds are `rejected`: spec part 5 suggests returning resources according to progress, but the survey fee is small and represents completed field work, and refund arithmetic would need the decision-file cost literals moved into script constants. Failure clears only the project's own pointer, flag, and due date.
- Secondary-site construction is justified by a single working site, by stored missiles exceeding total site capacity, or by the existing mature-program signal, below the four-site cap and with Command Control at least the operation minimum.
- `missiles_establish_command_authority` is repeatable on its medium cooldown while Command Control is not yet secure, so a program whose first attempt fell short of the secure gate is not left in the establishment phase.
- Severing the network through the warning event option also starts the restoration mission, matching the decision. A completed restoration returns the network to Supervised when the evolution is available and otherwise leaves posture at Off.
- HOI4 MCP: `hoi4.decision_inspect` (inspect, `missiles_launch_state_survey_mission`, scenario `survey_due_valid`) returned `DECISION_ANALYZED_PARTIAL` at source revision `bfdfaa1e04dc…`, report `decision-21180934b5bdb71d…`: activation `always = no`, timeout 120 from `@m32_mission_survey_days`, completion/cancel/timeout effects present, and the due-date and state-pointer gates unresolved because the scenario model cannot bind `global.date` or a state-valued variable. `hoi4.probability_inspect` (`decision_ai_will_do`, four changed decisions, source `common/decisions/032_missiles_decisions.txt`) returned `INTERNAL_ERROR`; it was not retried. The AI weight changes (core-state and capital factors on survey and secondary-site targets, zero weight for suspension during a prepared operation, reduced restoration weight below secure Command Control) are therefore unaudited by the probability route.

## Item 3: captured-site resolution

Disposition: `implemented` (source evidence; live behaviour `needs_live_game`).

- The four existing key families map to spec part 5's resolutions: guard is "hold inactive", study is "secure and inspect" (with the existing guidance-training gain), integrate, and scuttle. The "transfer through an explicit diplomatic route" resolution is `rejected` for this round; the lead's acceptance names four resolutions and no transfer localisation exists.
- Resolutions are final per state: guard and study mark `missiles_site_capture_resolved`, integrate clears the capture, and scuttle retires the site. A guarded or studied site keeps its sealed missiles in `missiles_captured_reserve_held`; it cannot later be integrated. This keeps the decisions mutually exclusive as accepted.
- One captured state is shown at a time through the one-entry array `missiles_captured_site_focus`, so the incident phase shows at most four resolution actions plus neutral-victim compensation. Incident inspection and site suspension hide while a captured site awaits resolution.
- Integration requires a guided national program (not a capture-only shell), matching the existing effect's technology rule.
- AI weights follow the stored doctrine profile: integration is preferred by guided programs and at war, halved for brittle command; scuttling is preferred at war by programs that cannot integrate, by brittle command, and for sites in foreign-owned states; guarding is preferred in peace by programs that cannot integrate and by restrained deterrents; studying is preferred by programs that cannot integrate and by counterforce guardians.
- Pre-existing ROOT-binding defects found in the capture path are repaired here because they decide whether the former controller's captured-site marker clears: the former controller and a scuttled site's controller now refresh through the new immediate receiver `chaosx.nr32.7`; `missiles_cleanup_operation` compares against `PREV.missiles_active_operation_id`; `missiles_scuttle_site` records the removed site id from the state (`PREV.id`) instead of the country.
- Network totals use controlled states and skip unresolved captured sites, so integrated sites in occupied states count toward site count and capacity.
- MCP probability inspection for the new AI weights was not re-attempted after the `INTERNAL_ERROR` recorded under item 2.

## Item 4: wartime maintenance and war/peace phase refresh

Disposition: `implemented` (source evidence; live behaviour `needs_live_game`).

- The four maintenance actions use `missiles_maintenance_actions_are_visible`: always in the maintenance phase, and in the operations phase when no strike can be prepared, when a human has neither selected a target nor opened the country selector, or for the AI. The AI has no decision-list budget, so it can replenish and secure codes during a war without first exhausting its reserve.
- Human operations view without a target: the target selector plus four maintenance actions, plus network restoration when severed, is at most six actions. Once a human opens the selector or picks a target, maintenance steps aside for selection and preparation.
- `on_war_relation_added` refreshes the phases of ROOT and FROM when they own a program; `on_peace` refreshes the country making peace and clears an unfinished target choice (`missiles_clear_target` keeps the target of an operation already in preparation). No world iteration is added.
- Replenishment, readiness, guidance, and launch-code effects refresh phases, and `missiles_resolve_warning_queue_receipt` refreshes phases instead of forcing the operations view, which previously put a peacetime country into the operations phase after a warning closed.
