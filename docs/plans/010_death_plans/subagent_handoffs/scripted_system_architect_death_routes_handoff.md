# Event 010 Death Route Helper Architecture Handoff

Date: 2026-06-15

Role: `chaosx_scripted_system_architect`

## Scope Audited

Allowed implementation files:

- `common/script_constants/010_death_constants.txt`
- `common/scripted_triggers/010_death_triggers.txt`
- `common/scripted_effects/010_death_effects.txt`
- `common/scripted_localisation/010_death_scripted_localisation.txt`
- `common/dynamic_modifiers/010_death_state_modifiers.txt`
- `events/010_death.txt`

Focused surfaces:

- Dark Methods / Black Book helpers
- Black Oath and Herald of Zol helpers
- Black Apostolate culmination helper
- Black Atlas scripted localisation
- stale active Spirit of War/Peace references inside the scoped files

## Files Changed

- `common/scripted_effects/010_death_effects.txt`
- `common/scripted_localisation/010_death_scripted_localisation.txt`
- `docs/plans/010_death_plans/subagent_handoffs/scripted_system_architect_death_routes_handoff.md`

## Helper Map

### `death_cleanup_forbidden_method_status`

Scope: country.

Inputs: current country state flags, ideas, and Black Book variables.

Outputs:

- clears active Black Book route flags: `death_black_book_opened`, `death_black_book_exposed`, `death_black_book_discredited`, `death_bound_unburied_used`, `death_interrogated_empty_road`, `death_sealed_names_in_iron`
- removes `death_black_book_offices` and `death_black_book_scandal`
- deletes `Black Book Bound Shade` units/template
- clears `death_black_method_exposure`, `death_bound_names`, and `death_mourning_debt`

Side effects: closes active Dark Methods state when the country becomes a Herald. It does not clear `death_black_book_burned`, because that is a deliberate completed-action blocker rather than an active office state.

Call sites changed:

- `death_make_herald_of_zol`

### `death_make_herald_of_zol`

Scope: country.

Change: made the transformation idempotent. The initial Herald package, global Herald count increment, route-cost variables, compact exit, war-state changes, and Black Oath super-event now run only if the country was not already a Herald. Repeated calls still clamp Herald variables and schedule the Friend of Zol check when applicable.

Inputs: current country, `DTH`, compact flags, Herald variables.

Outputs and side effects:

- sets `death_black_oath_taken`, `death_herald_of_zol`, cosmetic tag `death_herald_of_zol`, and idea `death_black_oath`
- increments `global.death_herald_countries` only once
- applies starting name debt, black favor, and living disgust only once
- leaves Living Compact once
- white peaces Death and triggers compact-member wars once
- emits Black Oath super-event once through the existing global flag

### `death_cleanup_herald_status`

Scope: country.

Change: expanded route cleanup for active Herald-only transient state.

Outputs and side effects:

- clears `death_herald_collection_cooldown`
- removes `death_herald_dead_port` from currently controlled states
- removes `death_herald_dead_port_state` dynamic modifiers from those states and refreshes dynamic modifiers

Achievement-ready flags such as `death_friend_of_zol_ready` and `death_black_apostolate_ready` were intentionally left untouched because achievement definitions read them as completed outcomes.

### `GetDeathAtlasCoastRisk`

Scope: scripted localisation trigger.

Change: the `DTH = { num_of_controlled_states < ... }` branch now first requires `death_country_exists = yes`.

Reason: avoids evaluating the exposed-coast branch against the Death tag before the country package exists.

## Constants and Tuning Table Plan

No constants were added or changed. The patched helpers reuse existing route constants:

- `death_decision_tuning.name_debt_start`
- `death_decision_tuning.black_favor_oath_gain`
- `death_decision_tuning.living_disgust_oath_gain`
- `death_spread.coastal_jump_contained_state_limit`

Follow-up candidate: `death_process_herald_debts` still uses a literal `value = 0` for positive black favor, and `death_mark_world_end_foothold_created` still uses a literal threshold for the six-continent achievement. These are outside the narrow patch and can be moved into constants in a later tuning pass.

## Event Target and Cleanup Plan

No new event targets were added.

Reviewed global event target cleanup in the scoped files:

- `death_living_compact_leader` is cleared on Death defeat.
- `death_current_reveal_state` is cleared on Death defeat.
- `death_trigger_actor` is cleared in triggerable scenario cleanup.

Remaining risk: `death_country` and `death_origin_state` are persistent global event targets saved by setup/origin helpers and are not cleared on defeat. That may be intentional because the DTH tag and origin state remain useful for aftermath/wasteland history, but it should be confirmed before any broader cleanup.

## Migration From Duplicated Logic

Implemented a local cleanup helper instead of duplicating Dark Methods cleanup in Herald conversion and future route exits.

No generic `chaosx_dynamic_effects` helper was added because the logic is event-specific and tied to Event 010 flags, ideas, units, and variables.

## Validation

Meaningful checks run:

- Scoped search for obsolete active Spirit of War/Peace references in the six allowed implementation files: no matches.
- Scoped search for unsupported `<=` / `>=` operators in the six allowed implementation files: no matches.
- Brace-balance check across the six allowed implementation files: all balanced.
- Checked existing repo usage of `clear_variable = <local_variable>` before using it in the new cleanup helper.
- Reviewed achievement definitions for `death_friend_of_zol_ready` and `death_black_apostolate_ready` before leaving those flags intact in route cleanup.

Skipped:

- Did not run game-load validation or inspect logs.
- Did not edit decisions, localisation YAML, GUI, assets, spreadsheets, or unrelated files per user scope.

## Risks and Follow-up

- `death_pay_bind_unburied_cost` and `death_pay_offer_prison_census_cost` gate on manpower but do not spend manpower. This may be intentional abstraction, but it should be reviewed with the decision owner because this audit was limited to helper architecture.
- Black Book `burned` remains a permanent blocker and is intentionally not cleared by Herald conversion cleanup.
- The worktree was already dirty, including Event 010 implementation files, before this patch. Diff against `HEAD` includes pre-existing changes outside this subagent's edits.
