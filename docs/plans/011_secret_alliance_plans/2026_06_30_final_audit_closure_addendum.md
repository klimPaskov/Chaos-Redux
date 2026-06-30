# Event 011 Secret Alliance final audit closure addendum

Date: 2026-06-30
Owner: Chaos Redux improvement-loop planning subagent

## Closure position

Event 011 does not need another broad expansion pass. Direct reading of the current specs and implementation shows that the core Secret Alliance promise is already present: hidden founder selection, member arrays, public reveal, war-caused reveal, varied counterplay decisions, achievement hooks, Dossier Board assets, animated danger accents, and public pact creation all exist in the current implementation set.

This addendum is intentionally bounded to the remaining final audit gaps:

- State and route based mission objectives.
- Dynamic Dossier Board meter visual states.
- Public pact lifecycle cleanup, especially invalid public leader handling.
- Cost and AI validation closure.

Do not add a new mechanic, focus route, formable, country package, super-event variant, asset family, spreadsheet pass, or lore expansion to satisfy this addendum. If the parent accepts it, implement only the small closure tasks below, then fold the durable acceptance criteria into `docs/specs/011_secret_alliance_specs/` or `docs/events/011_secret_alliance.md`.

## Reading basis and unresolved prior plans

Directly read source design:

- `docs/specs/011_secret_alliance_specs/specs/011_secret_alliance_spec.md`
- `docs/specs/011_secret_alliance_specs/specs/011_secret_alliance_mechanics.md`
- `docs/specs/011_secret_alliance_specs/specs/011_secret_alliance_decisions_missions.md`
- `docs/specs/011_secret_alliance_specs/specs/011_secret_alliance_ai_balance_localisation.md`

Directly read current implementation surfaces:

- `common/decisions/011_secret_alliance_decisions.txt`
- `common/scripted_effects/011_secret_alliance_effects.txt`
- `common/scripted_triggers/011_secret_alliance_triggers.txt`
- `common/script_constants/011_secret_alliance_constants.txt`
- `common/scripted_guis/011_secret_alliance_dossier_board_scripted_gui.txt`
- `interface/011_secret_alliance_dossier_board.gui`
- `interface/011_secret_alliance.gfx`
- `common/on_actions/chaosx_on_actions.txt`
- `common/factions/templates/secret_alliance_public_pact.txt`
- `docs/events/011_secret_alliance.md`

Directly read current Event 011 handoffs:

- `docs/plans/011_secret_alliance_plans/subagent_handoffs/2026_06_30_decision_mission_cleanup_audit_handoff.md`
- `docs/plans/011_secret_alliance_plans/subagent_handoffs/2026_06_30_decision_mission_audit_patch_handoff.md`
- `docs/plans/011_secret_alliance_plans/subagent_handoffs/scripted_system_architecture_event_011.md`

No previous unresolved Event 011 improvement-loop addendum was found as a top-level plan file under `docs/plans/011_secret_alliance_plans/`. The existing entries are subagent handoffs and audit/patch handoffs. This file should be treated as the single remaining bounded closure addendum until it is implemented, folded into specs, explicitly queued with a reason, or rejected with a reason.

Repository instruction note: `AGENTS.md` was not present in the workspace or parent chain during this direct read. It was not touched.

## 1. State and route based mission objectives

### Current closure evidence

The five mission ids already exist and are correctly attached to the Event 011 decision categories:

- `guard_capital_network_mission`
- `secure_industrial_belt_mission`
- `keep_foreign_route_watched_mission`
- `expose_patron_hand_mission`
- `hold_border_public_crisis_mission`

The latest implementation improved mission pacing and basic functionality:

- Mission timers are no longer too short: 90, 120, 105, 150, and 120 days.
- Missions use success and timeout effects instead of passive reward buttons.
- Mission activation is gated by mission-start flags.
- The current effects clear mission flags and set success/failure memory flags.

This means the mission layer is functional enough to keep. It should not be replaced with a larger mission system.

### Remaining gap

The current mission readiness triggers are still abstract:

- `secret_alliance_guard_capital_network_ready` checks capital control, total divisions, and prior preparation flags.
- `secret_alliance_industrial_belt_ready` checks military factories, total divisions, and hardening/sabotage flags.
- `secret_alliance_foreign_route_watched` checks trains plus route/sealed/sabotage/infiltration flags.
- `secret_alliance_patron_hand_exposed` is route-like, but it only checks high evidence, patron existence, and one supporting flag.
- `secret_alliance_public_border_held` checks total divisions, fuel/prep flags, and not actual threatened border states.

That does not yet match the spec promise that the player must secure named capital, industrial, route, or border areas. The parent should refine the existing mission ids rather than add new missions.

### Parent implementation target

Keep the existing mission ids. Add a small target-state and route-objective helper layer owned by Event 011:

New or updated helper identifiers:

- `secret_alliance_clear_mission_state_flags`
- `secret_alliance_mark_capital_network_states`
- `secret_alliance_mark_industrial_belt_states`
- `secret_alliance_mark_foreign_route_states`
- `secret_alliance_mark_public_border_states`
- `secret_alliance_refresh_mission_objective_states`
- `secret_alliance_capital_network_states_secured`
- `secret_alliance_industrial_belt_states_secured`
- `secret_alliance_foreign_route_states_secured`
- `secret_alliance_public_border_states_secured`
- `secret_alliance_patron_hand_route_proven`

Recommended state flags:

- `secret_alliance_capital_network_objective_state`
- `secret_alliance_industrial_belt_objective_state`
- `secret_alliance_foreign_route_objective_state`
- `secret_alliance_public_border_objective_state`

Use those helpers to update the existing mission readiness triggers:

- `secret_alliance_guard_capital_network_ready` should require the capital network objective states to be controlled by the target and defended by a real local state objective, not only total division count. The capital state must always be part of the target set.
- `secret_alliance_industrial_belt_ready` should require control and defense of selected high-value industrial states. Prefer the target's states with military factories; if the country is too small, allow the capital industrial state as the fallback.
- `secret_alliance_foreign_route_watched` should become route based. If a neighboring hidden or exposed member exists, mark border or rail-route states toward that member. If no land route exists but the target has ports, mark a port route. If neither exists, keep the existing train and sealed-courier requirements as the fallback and record that fallback in docs.
- `secret_alliance_patron_hand_exposed` should remain route based rather than state based. It should require at least two evidence-route proofs, such as `secret_alliance_foreign_route_success_seen`, `secret_alliance_controlled_leak_used`, `secret_alliance_counter_pact_ready`, or a completed friendly-government rally route. Do not require arbitrary border states for a distant patron.
- `secret_alliance_public_border_held` should require public crisis border objective states when a public member borders the target. If no public member borders the target, use the existing fuel, preparedness, and public crisis plan checks as the documented fallback.

Acceptance criteria:

- The five existing mission ids remain the player-facing mission surface.
- At mission activation, Event 011 marks a bounded set of objective states and clears stale objective state flags when the mission completes, fails, cancels, the pact reveals, the pact closes, or the target is invalid.
- Capital and border missions no longer complete only because the target has enough total divisions somewhere in the country.
- Industrial belt and foreign route missions name or dynamically expose the current objective area through tooltip/scripted localisation when localisation is in scope.
- `docs/events/011_secret_alliance.md` no longer overstates mission quality unless the state/route checks are actually present.
- If HOI4 script cannot reliably check supplied divisions in marked states, the parent should use the strongest validated state-control and local-presence check available, then document the fallback. Do not invent an unvalidated trigger.

## 2. Dynamic Dossier Board meter visual states

### Current closure evidence

The asset side is already complete enough. `interface/011_secret_alliance.gfx` registers 25, 50, 75, and 100 fill sprites for all three meters:

- `GFX_secret_alliance_evidence_meter_fill_25`
- `GFX_secret_alliance_evidence_meter_fill_50`
- `GFX_secret_alliance_evidence_meter_fill_75`
- `GFX_secret_alliance_evidence_meter_fill_100`
- `GFX_secret_alliance_pressure_meter_fill_25`
- `GFX_secret_alliance_pressure_meter_fill_50`
- `GFX_secret_alliance_pressure_meter_fill_75`
- `GFX_secret_alliance_pressure_meter_fill_100`
- `GFX_secret_alliance_preparedness_meter_fill_25`
- `GFX_secret_alliance_preparedness_meter_fill_50`
- `GFX_secret_alliance_preparedness_meter_fill_75`
- `GFX_secret_alliance_preparedness_meter_fill_100`

The scripted GUI already controls the animated danger accents:

- `secret_alliance_thread_glow_visible`
- `secret_alliance_radio_pulse_visible`
- `secret_alliance_seal_crack_visible`
- `secret_alliance_border_warning_visible`

No new art is needed.

### Remaining gap

`interface/011_secret_alliance_dossier_board.gui` currently hardwires:

- `secret_alliance_evidence_meter_fill` to `GFX_secret_alliance_evidence_meter_fill_75`
- `secret_alliance_pressure_meter_fill` to `GFX_secret_alliance_pressure_meter_fill_75`
- `secret_alliance_preparedness_meter_fill` to `GFX_secret_alliance_preparedness_meter_fill_75`

The text values are dynamic, but the visual fill state does not track `pact_evidence`, `pact_pressure`, or `pact_preparedness`.

### Parent implementation target

Use the existing sprites. Replace each single hardwired fill icon with four stacked fill elements controlled by scripted GUI visibility triggers.

Recommended GUI element ids:

- `secret_alliance_evidence_meter_fill_25`
- `secret_alliance_evidence_meter_fill_50`
- `secret_alliance_evidence_meter_fill_75`
- `secret_alliance_evidence_meter_fill_100`
- `secret_alliance_pressure_meter_fill_25`
- `secret_alliance_pressure_meter_fill_50`
- `secret_alliance_pressure_meter_fill_75`
- `secret_alliance_pressure_meter_fill_100`
- `secret_alliance_preparedness_meter_fill_25`
- `secret_alliance_preparedness_meter_fill_50`
- `secret_alliance_preparedness_meter_fill_75`
- `secret_alliance_preparedness_meter_fill_100`

Recommended scripted GUI trigger ids:

- `secret_alliance_evidence_meter_fill_25_visible`
- `secret_alliance_evidence_meter_fill_50_visible`
- `secret_alliance_evidence_meter_fill_75_visible`
- `secret_alliance_evidence_meter_fill_100_visible`
- `secret_alliance_pressure_meter_fill_25_visible`
- `secret_alliance_pressure_meter_fill_50_visible`
- `secret_alliance_pressure_meter_fill_75_visible`
- `secret_alliance_pressure_meter_fill_100_visible`
- `secret_alliance_preparedness_meter_fill_25_visible`
- `secret_alliance_preparedness_meter_fill_50_visible`
- `secret_alliance_preparedness_meter_fill_75_visible`
- `secret_alliance_preparedness_meter_fill_100_visible`

Threshold direction:

- Evidence should use existing constants: below `evidence_medium` shows 25, at `evidence_medium` shows 50, at `evidence_high` shows 75, and at `public_reveal_evidence` shows 100.
- Pressure should use existing constants: low pressure shows 25, pressure approaching the campaign reveal band shows 50, at `pressure_high` shows 75, and at `campaign_reveal_pressure` or above shows 100.
- Preparedness should use existing constants: low readiness shows 25, mid readiness shows 50, at `preparedness_high` shows 75, and a value at or above the evidence/public crisis preparation ceiling used by the final implementation shows 100. If no stronger constant exists, add one tuning constant rather than scattering a magic number.

Acceptance criteria:

- The Dossier Board no longer displays a permanent 75 percent fill for all meters.
- Exactly one fill tier is visible per meter at a time.
- The visual tier changes when the underlying value crosses the relevant threshold.
- No new art or animation request is made; use the already registered fill sprites.
- Existing animated danger accents continue to use the current visibility triggers.

## 3. Public pact lifecycle cleanup and invalid public leader handling

### Current closure evidence

The latest cleanup pass already fixed several important lifecycle gaps:

- `secret_alliance_close_compact_state` now clears target/category flags, active/reveal globals, target ideas, arrays, member flags, selected member, patron, public leader, war trigger, and target event targets.
- `secret_alliance_cleanup_invalid_members` removes invalid members, rebuilds arrays, and closes the compact when the member count drops below one.
- `secret_alliance_select_public_leader` now chooses a valid patron first, then a valid founder, then any valid public member.
- `secret_alliance_reveal_public_pact` syncs `pact_known_member_count` to `pact_member_count` on reveal.
- `secret_alliance_member_valid_for_public_faction` blocks capitulated countries, subjects, countries in the target faction, special chaos countries, and actual nonhuman countries.

Those are closure evidence. Do not duplicate them.

### Remaining gap

The remaining lifecycle risk is after public faction creation. If `event_target:secret_alliance_public_leader` later capitulates, becomes invalid, leaves the pact state, or otherwise stops being a valid public leader while other public members remain valid, the system can record valid public members without reselecting or transferring leadership.

This is not a reason to redesign public pact behavior. It needs a narrow public-leader lifecycle refresh.

### Parent implementation target

Add a small helper and call it from the existing lifecycle path:

New helper identifier:

- `secret_alliance_refresh_public_leader_lifecycle`

Required behavior:

- Runs only while `secret_alliance_is_public = yes`.
- If `event_target:secret_alliance_public_leader` exists and is still a valid public pact leader, do nothing.
- If the saved public leader is invalid, clear its `secret_alliance_public_leader` flag if scoped safely, clear the stale event target, and reselect from valid `secret_alliance_public_member` countries.
- Prefer the same order as creation when possible: valid patron, valid founder, then valid public member.
- If a valid replacement exists, mark it with `secret_alliance_public_leader` and save it as `event_target:secret_alliance_public_leader`.
- If the engine supports safe faction leadership transfer for this situation, transfer the public faction to the new leader. If not, leave the scripted event target and flags coherent and document the engine limitation in the handoff.
- If no valid public member remains, call the existing closure path instead of keeping a leaderless public pact.

Call sites:

- `secret_alliance_refresh_lifecycle`, after `secret_alliance_cleanup_invalid_members` and before public-pact defeat/closure checks.
- A targeted on-action hook if the parent already has a safe public lifecycle hook available, such as capitulation or faction leadership changes. Keep it gated by `secret_alliance_active` or `secret_alliance_public_revealed`; do not add an ungated world scan.

Acceptance criteria:

- A capitulated, invalid, subject, target-faction, special chaos, or nonhuman country cannot remain as `event_target:secret_alliance_public_leader`.
- If at least one valid public member remains, the system has a valid saved public leader after lifecycle refresh.
- If no valid public member remains, `secret_alliance_close_compact_state` or the existing public-pact defeat path closes the active gameplay surface.
- Existing history and achievement flags such as `secret_alliance_founder`, public reveal route flags, and achievement-ready flags are preserved where the current cleanup contract already preserves them.
- No duplicate public faction creation occurs during refresh.

## 4. Cost and AI validation closure

### Current closure evidence

The cost and AI surface is already much stronger than the original spec minimum:

- Decision costs use `custom_cost_trigger` and `custom_cost_text` across the Event 011 decision surface.
- Costs are varied across command power, political power, stability, army XP, air XP, support equipment, infantry equipment, trucks, trains, fuel, and manpower.
- Actual spends exist in Event 011 effect helpers, including `secret_alliance_complete_trace_diplomatic_pouches`, `secret_alliance_complete_turn_courier`, `secret_alliance_complete_break_radio_net`, `secret_alliance_complete_guard_rail_port_nodes`, `secret_alliance_complete_fuel_reserve_security`, and `secret_alliance_complete_local_defense_committees`.
- PP-heavy decisions have `ai_hint_pp_cost` values where relevant.
- Decision `ai_will_do` blocks exist and include state-based modifiers for stability, evidence, public reveal, preparedness, pressure, and division gates.
- Candidate and public member triggers block major invalid routes such as target war, target faction, subject status, special chaos countries, and nonhuman countries.
- The latest handoff reports custom cost localisation coverage and brace-balance checks.

This is closure evidence. Do not add a new AI strategy system unless validation finds a concrete failure.

### Remaining closure work

The remaining work is validation, not design expansion.

Parent validation checklist:

- Scan every Event 011 decision with `custom_cost_trigger` and confirm the matching complete effect actually pays the same resource family.
- Confirm every `custom_cost_text` key and `_blocked` key exists after any final localisation edits.
- Confirm command power costs stay within the decision guidance cap of 60 command power.
- Confirm no AI-only path can click `launch_preemptive_strike`, `limited_border_reprisal`, `face_saving_exit`, `seal_courier_pass`, or public disbandment when the required member, public leader, target, evidence, or war-case state is invalid.
- Confirm AI does not take manpower/fuel/equipment decisions when the cost trigger fails.
- Confirm state/route mission objective updates do not make AI missions impossible by requiring player-only GUI selection. AI must be able to satisfy the mission through the same map/control/resource state.
- Run the strongest available script validation for Event 011 files, then run an in-game HOI4 parser/load check if available before final completion.

Acceptance criteria:

- Validation output records pass/fail evidence for cost-trigger to spend alignment, AI invalid-route blocking, custom cost localisation coverage, brace balance, and at least one parser/runtime check or a clear reason it could not be run.
- Any failed validation creates a targeted patch or a documented blocker. Do not mark Event 011 complete with a known cost/AI failure.
- If validation passes, no extra cost redesign is needed.

## What should not be added

Do not add:

- New Event 011 decision categories.
- New mission families beyond the five existing ids.
- New Dossier Board art or animated assets.
- New focus trees, focus routes, formables, or country packages.
- New public-pact ideology branches.
- A new super-event variant.
- Spreadsheet or localisation edits as part of this planning subagent output.
- A daily or monthly world scan for public pact cleanup. Use existing lifecycle hooks or tightly gated active-event refresh only.

## Promotion guidance

Keep this file in `docs/plans/011_secret_alliance_plans/` until the parent resolves it.

If accepted and implemented:

- Fold the durable mission objective and lifecycle criteria into `docs/specs/011_secret_alliance_specs/specs/011_secret_alliance_decisions_missions.md` and `docs/specs/011_secret_alliance_specs/specs/011_secret_alliance_mechanics.md`.
- Update `docs/events/011_secret_alliance.md` only after implementation matches the described state/route mission behavior and dynamic meter visual behavior.
- Mark this plan as implemented or superseded in the parent completion handoff.

If queued:

- Record that this is a final audit closure addendum, not a broad expansion request.
- Do not run another Event 011 improvement-loop pass until this addendum is implemented, promoted, queued with a reason, or rejected with a reason.

## Parent handoff

Design problem:

Event 011 is deep enough to stop expanding, but four audit-level closure gaps remain: abstract mission objectives, static Dossier Board meter fills, public leader invalidation after reveal, and final cost/AI validation evidence.

Proposed closure:

Implement the narrow state/route objective helpers, dynamic meter fill visibility, public leader lifecycle refresh, and validation checklist above. Treat already implemented cleanup, costs, AI weights, public reveal, and asset registration as closure evidence rather than rework targets.

Research basis and historical/regional connections:

No additional historical research is needed for this addendum. The final gaps are implementation fidelity and UI/lifecycle closure issues, not missing regional or cultural design. Adding historical branches here would bloat the event.

Files written:

- `docs/plans/011_secret_alliance_plans/2026_06_30_final_audit_closure_addendum.md`

Implementation surfaces affected if accepted:

- `common/decisions/011_secret_alliance_decisions.txt`
- `common/scripted_effects/011_secret_alliance_effects.txt`
- `common/scripted_triggers/011_secret_alliance_triggers.txt`
- `common/script_constants/011_secret_alliance_constants.txt`
- `common/scripted_guis/011_secret_alliance_dossier_board_scripted_gui.txt`
- `interface/011_secret_alliance_dossier_board.gui`
- `docs/events/011_secret_alliance.md`
- Localisation only when the parent implements visible objective area text or meter tooltip changes.

Open questions:

- Which exact HOI4 trigger pattern in this repo is safest for local state unit presence or supplied-division checks? If unavailable, use controlled state flags plus validated local presence/control checks and document the fallback.
- Does the engine support a safe dynamic public faction leadership transfer for this Event 011 faction template after the original leader becomes invalid? If not, keep scripted leader state coherent and document the engine limitation.

Prior addendum status:

No unresolved prior Event 011 improvement-loop addendum was found. This addendum should remain the only open Event 011 improvement-loop plan until resolved.

Plan/spec status:

Remain in `docs/plans` for now. Promote only after the parent accepts and implements or explicitly folds the closure criteria into `docs/specs`.
