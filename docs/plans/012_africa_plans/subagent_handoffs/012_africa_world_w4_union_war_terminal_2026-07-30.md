# W4 union, continental war, successor, and terminal handoff

Status: implementation-ready isolated package delivered on 2026-07-30.

Scope: this handoff owns the non-model W4 protocol effects, triggers, events, and localisation only.

The accepted successor transfer in commit `433c22f4f` remains the sole owner of package-state and focus-tree transfer.

## Files changed

- `common/scripted_effects/012_africa_world_union_war_effects.txt` adds bilateral union, registered-war, settlement, successor-wrapper, breakup/exile, cleanup, and actor-by-actor terminal effects.
- `common/scripted_triggers/012_africa_world_union_war_triggers.txt` adds openability, eligibility, bilateral ratification, strain, war ledger, settlement, defeated review, and terminal proof triggers.
- `events/012_africa_world_package_union_war.txt` defines `africa_world_package.700` through `.759` as isolated country events.
- `localisation/english/012_africa_world_union_war_l_english.yml` contains all 60 event surfaces and reserved parent decision text, encoded UTF-8 with BOM.

## Helper map

### Union protocol

`africa_world_union_protocol_open` is a country effect on the proposing actor with `FROM` as the selected partner.

Inputs are two installed sovereign package actors, different continent IDs, no rival or active protocol, and no current war.

Outputs are the persistent global targets `africa_world_union_protocol_host` and `africa_world_union_protocol_partner`, the global open flag, bilateral approval variables, ballot counters, and the `union_convention` phase.

Side effects are proposal event `.700` on the partner and no automatic faction merge, annexation, core grant, or constituent coercion.

`africa_world_union_protocol_record_partner_acceptance`, `record_partner_negotiation`, `record_partner_refusal`, `record_host_acceptance`, and `record_host_refusal` are the two actor consent ledger effects used by `.700`, `.701`, and `.710`.

`africa_world_union_protocol_dispatch_constituent_ballots` loops each actor's own `africa_world_constituent_countries` array, excludes coerced, pending, withdrawn, and subject members, and sends `.702` or `.703` separately.

`africa_world_union_protocol_record_*_constituent_ballot_*` records each response in the member scope and increments only the owning actor's counters.

`africa_world_union_protocol_try_finalize_ballots` proves both ballots against the shared yes threshold and sends `.704` to the host.

`africa_world_union_protocol_ratify_constitution`, `ratify_defence_clause`, `ratify_resource_clause`, and `ratify_withdrawal_clause` require separate player-facing stages and preserve the autonomous partner.

`africa_world_union_protocol_record_faction_settlement` records an explicit distributed-command settlement before the clause sequence.

`africa_world_union_protocol_apply_strain`, `renegotiate`, `open_dissolution`, `dissolve_by_treaty`, and `open_contested_dissolution_war` provide the strain and peaceful or contested dissolution branches.

`africa_world_union_protocol_clear_pair` clears only the volatile union pair flags and global targets.

### Continental war protocol

`africa_world_continental_war_protocol_prepare`, `prepare_restore`, `prepare_break_compact`, and `prepare_constitutional_settlement` require an explicit `FROM` target and write one of the three goal values.

`africa_world_continental_war_protocol_start_war` maps the three goals to `liberate_wargoal`, `topple_government`, and `puppet_wargoal_focus`, then calls the bounded partner ledger.

`africa_world_continental_war_protocol_call_registered_partners` iterates only `africa_world_war_registered_partners` arrays on the registered attacker and defender.

`record_partner_join`, `record_partner_support`, and `record_partner_neutral` are explicit `.721` responses; union membership or faction membership alone never calls a partner into the war.

`offer_armistice`, `resolve_armistice`, `accept_constitutional_settlement`, `resolve_submission`, and `release_constituents` provide armistice, sovereignty-preserving submission, and constituent-release dispositions.

`cleanup` clears partner call flags, registered arrays, joined arrays, war flags, and global attacker/defender targets while retaining settlement flags and historical rivalry memory.

### Successor, exile, and breakup

`africa_world_union_war_open_defeated_review` calls the existing `africa_world_handle_package_actor_loss` helper so candidate nomination and validity remain centralized.

`africa_world_union_war_commit_first_successor` selects one bounded candidate and invokes `africa_world_union_war_commit_successor` with the selected candidate in `FROM`.

`africa_world_union_war_commit_successor` calls `africa_world_commit_package_successor = yes` exactly once and does not copy its transfer arithmetic, focus loading, variables, arrays, or roster edits.

`africa_world_union_war_record_exile` calls `africa_world_record_exile_resolution = yes` only when the existing exile trigger proves a valid government-in-exile path.

`africa_world_union_war_record_breakup` calls `africa_world_record_package_breakup = yes` only when the existing no-candidate breakup trigger proves the path.

The wrappers add the W4 terminal disposition flag and cleanup but do not duplicate authority penalties, constituent withdrawal arithmetic, or terminal counters already owned by the accepted helpers.

### Terminal protocol

`africa_world_terminal_protocol_begin_unanimous_union` and `begin_last_standing` save a global host target and dispatch actor-by-actor events `.750` or `.753` from `africa_world_package_actors`.

`record_unanimous_actor_approval` requires the voluntary constituent quorum; `record_actor_terminal_proof` requires `africa_world_terminal_protocol_actor_disposition_is_proven`.

`try_finalize_unanimous` and `try_finalize_last_standing` send only one final-review event after every actor proves its branch.

`africa_world_terminal_protocol_finalize` sets `africa_world_terminal_political_proof_complete` and cleans volatile actor protocol flags but never calls `africa_form_terminal_world_identity`.

`africa_world_terminal_protocol_set_handoff_ready` sets only the political handoff marker and never sets `africa_the_world_super_event_package_ready`.

`cleanup_after_identity` is a parent-owned post-identity cleanup hook that preserves historical proof flags and counters while clearing volatile arrays and protocol flags.

## Constants to add to `common/script_constants/012_africa_world_order_constants.txt`

The following categories are referenced by the new isolated files and are intentionally not edited here.

```text
africa_world_union_protocol = {
	 schema = {
		 any_key = yes
		 data = {
			 {
				 any_key = yes
				 data = {
					 {
						 any_key = yes
						 data = int
					 }
				 }
			 }
		 }
	 }
	 status = {
		 proposed = 1
		 ballots = 2
		 ratified = 3
		 active = 4
		 strained = 5
		 dissolving = 6
		 dissolved = 7
	 }
	 approval = {
		 pending = 0
		 accepted = 1
		 negotiating = 2
		 refused = 3
	 }
	 tuning = {
		 constituent_yes_required = 1
		 strain_review_threshold = 60
		 strain_event_gain = 15
		 strain_repair = 20
		 strain_min = 0
		 strain_max = 100
	 }
}

# Append these two fixed-point keys to the existing `africa_world_package_protocol` category.
voluntary_quorum_large = 3
voluntary_quorum_sparse = 1

africa_world_war_protocol = {
	 schema = {
		 any_key = yes
		 data = {
			 {
				 any_key = yes
				 data = {
					 {
						 any_key = yes
						 data = int
					 }
				 }
			 }
		 }
	 }
	 status = {
		 proposed = 1
		 mobilising = 2
		 active = 3
		 armistice = 4
		 settled = 5
		 collapsed = 6
	 }
	 goal = {
		 restore_constituent_sovereignty = 1
		 break_rival_compact = 2
		 compel_constitutional_settlement = 3
	 }
	 tuning = {
		 support_infantry_equipment = 1500
		 support_equipment = 300
	 }
}

africa_world_terminal_protocol = {
	 schema = {
		 any_key = yes
		 data = int
	 }
	 required_actor_approvals = 6
}
```

`africa_world_package_phase` already contains `union_convention = 6`, `union_active = 7`, `war_active = 8`, `successor_review = 9`, `breakup_review = 10`, and `terminally_resolved = 11` in the current shared constants file.

## Parent decision call sites

Add targeted decisions to `common/decisions/012_africa_decisions.txt` with `target_array = africa_world_package_actors` and the existing Event 012 host ownership pattern.

The union opener should use `FROM = { africa_world_union_protocol_target_is_eligible = yes }` in `available`, charge a shared union convention political-power cost, and call `FROM = { ROOT = { africa_world_union_protocol_open = yes } }` from `complete_effect` or use the repository's standard targeted-decision ROOT/FROM shape.

The union sequence should expose `africa_world_ratify_union_constitution`, `africa_world_integrate_union_defence`, `africa_world_integrate_union_resource`, `africa_world_integrate_union_withdrawal`, `africa_world_review_union_strain`, and `africa_world_dissolve_union_by_treaty` only while the matching global pair flags and approval variables are true.

The following targeted-decision blocks are integration-ready skeletons using the repository's existing ROOT/FROM ownership pattern.

```text
africa_world_open_union_convention = {
	icon = GFX_decision_012_africa_charter_ledger
	target_array = africa_world_package_actors
	activation = { africa_is_current_host = yes }
	target_root_trigger = { africa_world_package_is_installed = yes }
	target_trigger = { FROM = { africa_world_union_protocol_target_is_eligible = yes } }
	cost = constant:africa_world_order.union_pp_cost
	complete_effect = { FROM = { ROOT = { africa_world_union_protocol_open = yes } } }
	ai_will_do = { base = constant:africa_world_order.ai_normal }
}

africa_world_ratify_union_constitution = {
	icon = GFX_decision_012_africa_charter_ledger
	visible = { has_global_flag = africa_world_union_protocol_open has_country_flag = africa_world_union_protocol_ballots_complete }
	available = { africa_world_union_protocol_ratification_is_proven = no }
	cost = constant:africa_world_order.union_pp_cost
	complete_effect = { africa_world_union_protocol_ratify_constitution = yes }
	ai_will_do = { base = constant:africa_world_order.ai_normal }
}

africa_world_prepare_continental_war_restore = {
	icon = GFX_decision_012_africa_charter_ledger
	target_array = africa_world_package_actors
	activation = { africa_is_current_host = yes }
	target_root_trigger = { africa_world_continental_war_protocol_can_prepare = yes }
	target_trigger = { FROM = { africa_world_continental_war_protocol_target_is_registered = yes } }
	cost = constant:africa_world_order.war_launch_pp_cost
	complete_effect = { FROM = { ROOT = { africa_world_continental_war_protocol_prepare_restore = yes } } }
	ai_will_do = { base = constant:africa_world_order.ai_high }
}

africa_world_open_defeated_package_review = {
	icon = GFX_decision_012_africa_charter_ledger
	visible = { africa_world_continental_war_protocol_can_open_defeated_review = yes }
	available = { africa_world_continental_war_protocol_can_open_defeated_review = yes }
	cost = constant:africa_world_roster.successor_review_pp
	complete_effect = { africa_world_union_war_open_defeated_review = yes }
	ai_will_do = { base = constant:africa_world_order.ai_normal }
}

africa_world_open_unanimous_union_review = {
	icon = GFX_decision_012_africa_charter_ledger
	visible = { africa_is_current_host = yes NOT = { has_global_flag = africa_the_world_super_event_package_ready } }
	available = { africa_world_terminal_protocol_cleanup_is_complete = yes }
	cost = constant:africa_world_order.terminal_pp_cost
	complete_effect = { africa_world_terminal_protocol_begin_unanimous_union = yes }
	ai_will_do = { base = constant:africa_world_order.ai_low }
}

africa_world_prepare_terminal_handoff = {
	icon = GFX_decision_012_africa_charter_ledger
	visible = { has_global_flag = africa_world_terminal_political_proof_complete }
	available = { has_global_flag = africa_world_terminal_political_proof_complete }
	cost = constant:africa_world_order.terminal_pp_cost
	complete_effect = { africa_world_terminal_protocol_set_handoff_ready = yes }
	ai_will_do = { base = constant:africa_world_order.ai_normal }
}
```

The war opener should expose three explicit variants that set `africa_world_continental_war_goal` and call `africa_world_continental_war_protocol_prepare_restore`, `prepare_break_compact`, or `prepare_constitutional_settlement` with the selected target in `FROM`.

The war ledger should expose `africa_world_call_registered_continental_partners`, `africa_world_offer_continental_armistice`, `africa_world_impose_constitutional_settlement`, `africa_world_release_contested_constituents`, and `africa_world_open_defeated_package_review` with triggers from the matching new scripted triggers.

Update the existing successor decision to call `africa_world_union_war_commit_successor` so the accepted transfer remains the only implementation of replacement state. Add sibling decisions for `africa_world_certify_package_exile` and `africa_world_certify_package_breakup` that call the wrappers in this file.

Add terminal decisions `africa_world_open_unanimous_union_review`, `africa_world_open_last_standing_review`, `africa_world_commit_terminal_political_proof`, and `africa_world_prepare_terminal_handoff` using `africa_world_terminal_protocol_can_finalize` and the new protocol flags.

The terminal handoff decision must not set `africa_the_world_super_event_package_ready` and must not call `africa_form_terminal_world_identity`; the separate terminal identity package retains ownership of those gates.

## Parent on-action call sites

In `common/on_actions/012_africa_world_order_on_actions.txt`, add a bounded `on_capitulation` branch for a package actor that calls `africa_world_union_war_open_defeated_review = yes` once and leaves candidate selection to `.740`.

Add an `on_war_relation_added` branch that only checks the global war protocol and whether `ROOT` or `FROM` equals the registered attacker or defender event target; do not iterate all countries or infer partner calls from union flags.

Add an `on_peace` branch that fires `.734` or invokes `africa_world_continental_war_protocol_cleanup = yes` only when the global attacker and defender targets are no longer at war.

The bounded on-action shape is:

```text
effect = {
	if = {
		limit = {
			has_global_flag = africa_world_continental_war_protocol_open
			africa_world_package_is_installed = yes
			has_country_flag = africa_world_package_actor
		}
		africa_world_union_war_open_defeated_review = yes
	}
}
```

For `on_war_relation_added` and `on_peace`, add the same `has_global_flag` guard plus explicit attacker or defender event-target equality checks, then call only the matching war effect. Do not replace those checks with `every_country`, `any_country`, or a recurring on-action.

Do not add recurring `on_daily`, `on_weekly`, or `on_monthly` world iterations for this protocol.

## Event-target and cleanup plan

The union pair uses global targets because ballots and clause events persist across multiple country events; `africa_world_union_protocol_clear_pair` is the only pair-target cleanup.

The war pair uses global attacker and defender targets because partner calls and settlement events outlive one effect chain; `africa_world_continental_war_protocol_cleanup` clears both targets and all bounded arrays.

The terminal host uses one global target for actor-by-actor proof; `cleanup_after_identity` clears it after the parent identity package commits.

Regular candidate targets are used only inside the successor wrapper chain and are explicitly cleared after the accepted transfer call.

## Migration from duplicated logic

Replace old union action kernels with the new bilateral consent, ballot, ratification, strain, and dissolution call sites instead of copying their effects into decisions.

Replace direct continental-war declarations in W4 decisions with the three goal-specific prepare effects and the common start-war effect.

Replace direct successor transfer edits with `africa_world_union_war_commit_successor`, which delegates to the accepted `africa_world_commit_package_successor` helper.

Replace direct breakup arithmetic or constituent release loops with the existing `africa_world_record_package_breakup` and `africa_world_record_constituent_withdrawal` helpers through the wrappers.

## Risks and unsupported surfaces

The new files intentionally reference shared constants, decisions, and on-actions that are not part of this isolated patch; the parent must integrate those call sites before claiming the complete W4 package.

Clausewitz event-target scopes are supported by the offline Effects and Triggers documentation, but the parent should inspect the rendered targeted decisions after wiring ROOT/FROM ownership.

The accepted successor helper does not need to be duplicated; any future extension should preserve its single transfer call and its `keep_completed = yes` focus-tree behavior.

No fallback world scan, generic partner inference, annexation, blanket core grant, model asset, high-chaos activation, or terminal readiness setter was added.

## Validation performed

- Balanced braces were checked in all three script files.
- Event definitions cover every ID from `africa_world_package.700` through `.759` exactly once.
- The localisation file was rewritten with a UTF-8 BOM and contains no `:0` keys.
- The new script files contain no unsupported `<=` or `>=` operators.
- `white_peace`, `add_to_war`, `save_global_event_target_as`, and `clear_global_event_target` forms were cross-checked against the offline wiki, vanilla documentation, and existing Chaos Redux precedents.

Live Hearts of Iron IV execution was not run because repository policy assigns live consumer validation to the parent and user.

## Known limitations and follow-up

The parent must add the shared constant categories, targeted decisions, on-action branches, and any existing scripted-GUI bindings that expose these protocol effects.

The parent should promote the helper descriptions into `common/scripted_effects/chaosx_dynamic_effects.md` if the project wants the W4 protocol helpers indexed in the shared dynamic-effect catalog.

The W4 terminal protocol records political proof and handoff readiness only; it intentionally leaves the separate identity and super-event package gates untouched.
