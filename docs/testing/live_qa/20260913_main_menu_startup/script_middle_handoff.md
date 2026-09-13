# Middle scripted effects startup repair handoff

Status: assigned source repairs complete and frozen for startup validation.
Mandatory root probability comparison and fresh startup acceptance remain pending.
Parent authorized startup repair and assigned Event 024, 025, 026, 028, 029 effects, trigger024, then trigger025 and the narrow CBRN shelter extraction.
No commit created because root owns the combined startup tranche.

## Files and behavior

- `common/scripted_effects/024_video_game_in_sweden_effects.txt`: consumed `video_game_in_sweden_reliance_delta` is reset through native `set_temp_variable` instead of unsupported `clear_temp_variable`.
- `common/scripted_triggers/024_video_game_in_sweden_triggers.txt`: six `divisions_in_state.size` fields use file-local `@reality_audit_min_divisions_per_region = 1`, preserving the shared constant's exact value and strict greater-than comparison.
- `common/scripted_effects/025_alien_technology_in_antarctica_runtime_effects.txt`: evaluates the existing same-day comparator effect before its result condition.
The comparator body and tie-break order are unchanged.
The two unsupported regular-target clears become documentation of chain lifetime, and every target consumer requires its country-owned `chaosx_nr25_rival_target` marker.
The resolver rebuilds the scope from the current durable target ID, clears the marker before search, and sets the marker from `PREV.id` inside ROOT to retain the selected participant ID.
- `common/scripted_triggers/025_alien_technology_in_antarctica_triggers.txt`: pre-winner exchange requires the same marker, preventing stale chain targets from authorizing it after cleanup.
- `common/scripted_effects/029_riches_found_cxt_effects.txt`: capital-state presence uses native `scope_exists` rather than country-only `exists`.
- `common/scripted_effects/cbrn_protection_decision_effects.txt`: extracted `cbrn_complete_civilian_shelter_movement` from the existing successful equipment-payment branch.
Both the ordinary caller and the already-paid Black Friday caller apply the identical timed shelter payload.
- `common/scripted_effects/cbrn_scripted_effects.md`: documents scope, payment precondition, timing input, state flag and modifier outputs, absence of additional debit, call sites, and natural timed cleanup.

## Cleanup and continuation proof

`video_game_in_sweden_reliance_delta` has arithmetic writes and one arithmetic consumption, with no existence test, scoped access, or localisation consumer in common/events/interface.
Twenty-three immediate callers initialize it before the call.
The remaining call is the incident wrapper, whose fourteen event-option callers initialize it before `video_game_in_sweden_mark_incident`, which neither modifies the delta nor schedules an event.
The post-consumption refresh and achievement paths do not read it.
Resetting it to zero preserves the explicit consumed-input intent without pretending `clear_variable` operates on temporary storage.

`chaosx_nr25_rival_target_scope` is written by decisions or the registry resolver, read only by the two trigger helpers and runtime action blocks, and never used by delayed event options or localisation.
Both cleanup sites already clear the target marker and ID.
The pre-winner continuation clamps values, refreshes the board, and updates achievements.
Terminal cleanup can schedule reports, but those reports do not read this target.
All target-consuming guards require the marker, while the resolver always reconstructs from the requested ID so a previous chain target cannot override a subsequent selection.
No regular target was converted to a global target.

## Validation and references

`script_middle_validation.json` records direct caller scan results, explicit incident-wrapper coverage, unchanged same-day comparator body, call-before-condition validation, exact extracted shelter success lines, debit-free completion, and preserved ordinary support/train payment gates.
The initial short-distance caller scan intentionally records one false result for the wrapper, with the explicit wrapper audit recorded separately.
Backups preserve original bytes under `baseline/scripts/<relative path>` before edits.

`script_middle_mcp_before.json` records mandatory Event MCP trace and scope render artifacts for events 24, 25, 26, 28, and 29.
Installed selector schema requires `{kind: event, eventId: ...}`, rejecting `id`.
All returned partial analysis, explicitly deferring workspace-wide helper projection and lifecycle passes.
These are source-linked graph evidence and do not establish loader or runtime acceptance.
Event compare was attempted with the Event025 scope JSON artifact and current sources, then with its trace JSON artifact.
Both returned `EVENT_GRAPH_ARTIFACT_INVALID` with zero artifacts.
Comparison proof remains blocked because these inspector/render artifacts are not accepted graph snapshots.
The linked `nr25_expedition_board_window` read-only GUI inspection returned `windowName and scenario must be provided together`.
The existing approved scenario was not provided to this worker, so no scenario was invented and no GUI layout was edited.
The parent directed this worker to record that blocker and leave visual surfaces with the root GUI owner.

Required references consulted: AGENTS.md, the events/subagents/debug-playtest/decisions-missions skills, core offline wiki pages, especially Data structures regular event targets, installed effects documentation for temporary writes and target lifetime, triggers documentation for divisions_in_state, scope_exists, has_opinion and any_province_building_level, script concept constants section, native script_constants documentation, and existing dynamic helper registry.
No skills created or changed.

## Pending work and limitations

Root probability auditor baseline is required before Event028 victory-point score predicates and Event029 owned/control selection gate and opinion score predicates are patched.
The Event028 threshold is exactly zero, so native `any_province_building_level` with `limit_to_victory_point = yes`, bunker level greater than minus one can express existence of a positive-VP province without changing fort requirements.
This is only equivalent for the current zero threshold and must not be represented as arbitrary dynamic VP magnitude support.
Event029 static opinion values require file-local literals matching positive 25 and hostile minus25.
No weighted values have been changed in this tranche.

Event025 has_active_mission failures in error_after_stop.log use defined IDs from the mission file, and depend on the decision owner's category registration repair.
No mission cleanup was deleted.
Fresh startup validation remains root-owned.
No mechanics or successful payloads were removed and no null helpers were introduced.

## Released Event028/Event029 repair tranche

Parent released the held syntax-equivalent edits after the root auditor recorded Event028 `no_weighted_surfaces` and Event029 baseline candidate discoveries.
The parent explicitly accepted the documented zero-threshold VP-existence equivalence and retained MCP limitations.
Earlier pending-weighted notes above describe the pre-release state and are superseded by this section.

`common/scripted_effects/028_asteroid_incoming_runtime_effects.txt` replaces both unsupported state VP triggers with native `any_province_building_level` restricted to positive-VP provinces.
The bunker level greater-than-minus-one clause accepts every legal nonnegative fort level and imposes no fort requirement.
The current `minimum_victory_points = 0.00` threshold is exactly preserved as positive-VP existence.
The engine filter cannot express arbitrary VP magnitude thresholds, so a future change to that constant requires revisiting this implementation.
Both score additions remain unchanged.

`common/scripted_effects/029_riches_found_effects.txt` replaces unsupported `any_owned_controlled_state` with `any_owned_state` plus `is_owned_and_controlled_by = PREV`, retaining the preferred-state condition and every random-list weight.
`common/scripted_effects/029_riches_found_incident_effects.txt` replaces five unsupported static opinion constant operands with file-local macros 25 and minus25.
Strict operators and all score arithmetic are unchanged.

`script_middle_weighted_manifest.json` records exact before/after SHA256 hashes and original-byte baseline paths for all three files.
`script_middle_weighted_validation.json` verifies unchanged score arithmetic and selection weight tokens and provides named eligibility scenarios for the root auditor's mandatory comparison.
The named scenarios cover ownership/control/preference eligibility, opinions minus26/minus25/minus24/24/25/26, and zero/positive VP presence with zero or positive bunker levels.
These expectations are task-specific source contract checks, not claimed engine execution.
No further source edits are in progress and no commit was created.
