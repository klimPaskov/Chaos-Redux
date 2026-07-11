# Event 005 Selected-Target Lifecycle Handoff

**Date:** 2026-07-11
**Mode:** bounded patch handoff
**Scope:** Soviet and foreign selected-target lifecycle, terminal target actions, live corridor missions, operational posture priority, release-cause scope, UWR and KMB hooks, and related AI and localisation.

## Files changed by this patch

- `common/decisions/005_soviet_collapse_decisions.txt`
- `common/scripted_triggers/005_soviet_collapse_triggers.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/script_constants/005_soviet_collapse_constants.txt`
- `localisation/english/005_soviet_collapse_l_english.yml`
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_07_11_soviet_selected_target_lifecycle_handoff.md`

Integration dependencies reviewed but not authored in this bounded patch:

- `common/decisions/categories/005_soviet_collapse_categories.txt` already exposes the Moscow desk through `is_soviet_collapse_aftermath_active` and exposes the foreign desk through the refactored patron surface.
- `events/005_soviet_collapse.txt` was patched by the parent so the first `soviet_collapse_activate_opening_objectives` call runs in event `after`, once the chosen posture flag and option deltas exist.

These gameplay files contained concurrent Command and Corridors work. Edits were kept to the identifiers and call sites listed below.

## Selected-target lifecycle corrections

- All 17 preterminal foreign actions now have one matching substantive `can_target_*` gate, one matching `can_pay_*` gate, and one family requirement tooltip inside `available`.
- Human selection only controls which target row is displayed. AI target rows use an explicit AI branch and still rely on `available` for action validity.
- `has_soviet_collapse_selected_foreign_patron_target_from_root` now requires the sponsor menu pointer, target selection flag, and target-side sponsor owner variable to agree.
- Selection flags no longer satisfy breakaway identity, route, cooldown, Soviet pressure, League, acceptance, or dependency gates.
- The aid, major aid, volunteer, construction, aid-corridor, League aid, protection treaty, adviser privilege, and client cabinet gates were stripped of selected-target fast paths.
- Political contact and potential, normal, major, and League routes no longer accept selection as a route substitute.
- `soviet_collapse_select_moscow_republic_target` and `soviet_collapse_select_foreign_patron_target` no longer activate targeted decisions.
- The normal hide effects no longer remove targeted decisions.
- The obsolete `activate_targeted_decision` helper definitions were removed. Target rows now come entirely from `target_array` plus target visibility.
- Exact removal helpers remain only for resolution and terminal cleanup:
  - `soviet_collapse_remove_moscow_republic_target_decisions_for_prev`
  - `soviet_collapse_remove_foreign_patron_target_decisions_for_prev`
- `soviet_collapse_reset_selected_target_desks_for_breakaway` resets Moscow and the exact stored foreign sponsor before clearing target-side selection state.
- `soviet_collapse_cleanup_resolved_breakaway_target` removes an array member and decrements both counts only once, then uses shared target-state cleanup. Repeated calls cannot decrement again.
- `soviet_collapse_handle_breakaway_defeat` now delegates registry and desk cleanup to the shared cleanup effect instead of decrementing independently.
- Federal reintegration and single-target defeat paths retain full cleanup.
- Reconquest no longer removes members from the array while iterating it. It resets desks and target state during iteration, then clears the registry and already-reset counters afterward.
- Terminal transition resets all selected desks and removes obsolete prewar and terminal target rows without resolving the surviving republic registry.

## Terminal target actions

### Moscow

- Added `soviet_collapse_coordinate_reclamation_front`.
- Gate: SOV, terminal collapse, selected registered republic at war with SOV, and at least one selected-republic controlled original Union state with a supply node, railway, or infrastructure.
- Cost: reuses `can_pay_soviet_collapse_cut_rebel_supply_routes_cost` and `soviet_collapse_cut_rebel_supply_routes_cost_text`.
- Effect: `soviet_collapse_apply_terminal_reclamation_front` selects one valid state with no fallback, spends fuel and trains, damages supply node first, then railway, then infrastructure, records a timed state trace, and adds targeted conquer and antagonize strategy toward `FROM`.
- Central tuning is in `soviet_collapse_selected_target_aftermath`.

### Foreign patrons

- Added `soviet_collapse_sustain_terminal_republic_front`.
- Gate: terminal collapse, eligible major or regional-style patron, selected registered republic at war with SOV but not with the patron, and the existing aid-corridor target and cost gates.
- Effect: reuses `soviet_collapse_apply_foreign_aid_corridor`.
- AI patrons receive target rows through `can_show_soviet_collapse_foreign_patron_target_decisions`, while human rows remain selection-bound.

### Phase presentation

- The six Moscow negotiation, administration, ultimatum, and punitive rows now require `is_soviet_collapse_active`.
- The 17 original foreign intervention rows now require `is_soviet_collapse_active` in both visibility and root targeting.
- Moscow and foreign category text describes both the preterminal desk and terminal wartime use.
- The undefined `GFX_decision_soviet_collapse_settlement_goal` reference was replaced with registered `GFX_decision_soviet_collapse_cleanup_goal`.

## Live corridor and compromise corrections

- Added shared state-bound project triggers:
  - `has_soviet_collapse_selected_corridor_rail_project`
  - `has_soviet_collapse_selected_corridor_depot_project`
  - `has_soviet_collapse_selected_corridor_border_project`
  - `has_soviet_collapse_selected_corridor_logistics_project`
- All 21 Corridor and Depots missions now include the appropriate project trigger in `available`.
- All 21 missions now cancel and queue the existing refill when their selected state or required state geography becomes invalid. Cancellation does not register success or failure.
- Invalid corridor pointers now call `soviet_collapse_select_corridor_state_candidate` unconditionally. Its clear-first design removes a stale pointer even when no replacement exists.
- `can_pay_soviet_collapse_corridors_and_depots_compromise_cost` requires a live selected corridor state.
- Corridor and settlement compromises use `ai_hint_pp_cost` from the same script constants as their payment effects.
- All three compromise AI blocks account for war state and use the supported objective-activation grace flag as a board-age approximation when no exact mission-time-remaining trigger is available.

## Posture and crisis priority corrections

- Crisis bands are monotonic at Authority `50`, Obedience `48`, Republic `42`, and Depot `30`.
- Posture offsets are centralized in `soviet_collapse_operational_priority`.
- `soviet_collapse_compute_operational_family_priorities` applies and clamps these offsets after calm, contested, or crisis band selection:
  - Indivisible Union raises the Authority and Obedience safety floors.
  - Autonomy Settlement lowers the safe Republic ceiling.
  - Isolate Separatists lowers the Republic and Depot ceilings.
  - Restore Discipline Quietly raises the Authority and Obedience floors.
- The parent-owned event move ensures these offsets and the option deltas exist before the first board is filled.

## Release-cause and sponsor corrections

- `soviet_collapse_record_dominant_release_cause` now runs before the current release adds counts and Moscow pressure consequences.
- `soviet_collapse_apply_release_cause_neighbor_reactions` saves the released country as regular event target `soviet_collapse_release_actor` and reads all cause flags from that target inside the neighbor iterator.
- Unconsumed pending and last-cause neighbor metadata was removed. Neighbor component reactions occur immediately and are clamped once.
- All 17 foreign actions consume `soviet_collapse_release_sponsor_interest_active` through the same `@soviet_collapse_ai_pressure_multiplier` AI modifier.
- Resolution clears the cause flags, numeric cause, and sponsor-interest state.

## UWR and KMB corrections

- `soviet_collapse_uwr_contaminate_neighbor_front` saves the UWR actor as a regular event target and calls `soviet_collapse_mark_uwr_contaminated_state_for_aftermath` immediately after the anthrax or plague application in the victim state.
- The aftermath marker stores the UWR actor rather than the victim owner.
- UWR focus descriptions state that contaminated states are recorded in the wider Union crisis without promising later cleanup.
- Added reusable KMB concession triggers:
  - `has_soviet_collapse_kmb_valid_concession_target`
  - `has_soviet_collapse_kmb_superior_concession_target`
  - candidate-scope helpers used by the random neighbor selection
- KMB concession targets exclude self, faction members, current war opponents, and illegal declarations. Superiority uses `constant:soviet_collapse_kmb_ai.superiority_ratio`.
- `kmb_force_mining_concession` uses the shared trigger in availability, target selection, and AI weighting, then calls `soviet_collapse_apply_kmb_concession_crisis_hook` only after a target succeeds.
- `kmb_sign_resource_treaty` calls `soviet_collapse_apply_kmb_treaty_corridor_crisis_hook`.
- All six KMB decision costs use their existing `soviet_collapse_kmb_balance` constants.
- The treaty tooltip reports KMB depot control plus wider Soviet corridor and foreign pressure.

## Target-path proof

- Base republic: explicit base tag or live breakaway flag plus global registry membership satisfies the shared registered-target gate.
- TAJ: TAJ remains explicit in the base and breakaway tag sets and follows the same selected-target gates.
- Dynamic non-base republic: setup assigns `soviet_collapse_breakaway` or `soviet_collapse_event_created_republic` and registry membership, so no static tag exception is required.
- UWR and KMB high-chaos successors: `soviet_collapse_high_chaos_successor` satisfies registered-target identity and both can use the common lifecycle.
- Postterminal republic: selectors require terminal collapse and war with SOV. Prewar rows are hidden, while the two terminal actions apply their own war, route, state, and payment gates.

## Meaningful static validation

- A brace-aware block audit of the 17 foreign actions returned `target=1`, `pay=1`, `requirement tooltip=1`, and `sponsor AI consumer=1` for every action.
- The decision file contains exactly 21 selected-corridor cancel triggers and 21 matching project predicates across the audited corridor mission list.
- No `activate_targeted_decision` call remains in the Event 005 effects file.
- Direct inspection of all four normal select and hide effects found no activation on select and no removal on hide.
- New terminal, corridor, KMB, and cleanup scripted identifiers each have exactly one definition.
- KMB has six constant-backed decision costs, both hook call sites, and the shared superior-target consumer in availability and AI.
- The UWR aftermath marker has a live contamination call site.
- Script brace counts remain equal in every touched gameplay file.
- English localisation retains UTF-8 BOM bytes `239,187,191`.

## Remaining risks

- Runtime behavior was not observed from this subagent. The patch was validated structurally against the offline wiki, current vanilla documentation, and vanilla targeted-decision, state-flag, cancellation, and building-damage precedents.
- The five target-path proofs are static scope proofs. Final integration still needs the parent to review the complete shared diff because the effects, triggers, decisions, constants, and localisation files also contain concurrent Command and Corridors changes.
- Existing individual corridor mission requirement strings still describe their named strategic geography. The category displays the live corridor state and gameplay uses the new state-bound project gates, but the 21 legacy requirement strings were not individually rewritten to repeat that selected-state condition.

## Simplifications, omissions, and blockers

- No gameplay fallback, hardcoded target state, tag exception, skipped target class, or reduced terminal outcome was introduced.
- No route, cooldown, acceptance, League, dependency, payment, or state-geography gate is bypassed by selection.
- The only omission in this bounded patch is the per-mission repetition of the selected live-state wording noted above. This is a localisation presentation follow-up, not a gameplay simplification.
- No commit was created because these files are part of the parent's concurrent Event 005 integration tranche.

## Skills used

- `chaos-redux-events`
- `chaos-redux-subagents`
- `hoi4-decisions-missions`

No skill was created or updated.
