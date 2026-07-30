# Event 012 W3 Four-Mode Sponsorship Diplomacy Handoff

Date: 2026-07-30.

Scope: isolated W3 sponsorship effects, triggers, events, localisation, and integration instructions for the Event 012 host.

The host selects one grounded sponsorship mode before the candidate receives `africa_world_package.20`.

The candidate can accept, negotiate safeguards, or refuse without losing its sovereign country, focus tree, constituent congress, or independent package path.

The implementation never annexes, puppets, subordinates, creates a tag, writes party popularity, writes ideology, scans the world, or exposes `high_chaos`.

## Files added

- `common/scripted_effects/012_africa_world_sponsorship_effects.txt` contains the reusable offer, counterterms, mode fulfilment, default, military call, mediation, congress, guarantee, and cleanup helpers.
- `common/scripted_triggers/012_africa_world_sponsorship_triggers.txt` contains candidate, host, mode, duty, call, and cleanup gates.
- `events/012_africa_world_package_sponsorship.txt` owns namespace `africa_world_package` and events `.20` through `.31`.
- `localisation/english/012_africa_world_sponsorship_l_english.yml` contains UTF-8 BOM localisation for all event, decision, mission, and custom-cost keys.

No shared constants or decision files were edited in this isolated tranche.

## Helper map

| Helper | Scope | Inputs | Outputs and side effects | Intended call sites |
| --- | --- | --- | --- | --- |
| `africa_world_sponsorship_prepare_offer` | Candidate country | `africa_world_requested_sponsorship_mode`, current `africa_host` | Copies the requested grounded mode, charges the host once, marks the offer pending, and fires `.20` | Four host targeted offer decisions below |
| `africa_world_sponsorship_accept_offer` | Candidate country | Pending offer or pending counterterms | Installs the existing sponsored package, preserves the sovereign country, marks the selected duty, and gives a military guarantee when the mode is military | `.20.a` and `.23.a` |
| `africa_world_sponsorship_open_counterterms` | Candidate country | Pending offer | Saves a short-lived candidate target, opens counterterms, and fires host `.22` | `.20.b` or renegotiation decision |
| `africa_world_sponsorship_accept_counterterms_from_host` | Host country | Short-lived candidate target and 35 PP available | Charges counterterms and invokes candidate-side acceptance | `.22.a` |
| `africa_world_sponsorship_accept_counterterms_as_candidate` | Candidate country | Counterterms pending and host can pay | Charges the host, records safeguards, and invokes candidate-side acceptance | `.23.a` |
| `africa_world_sponsorship_close_offer` | Candidate country | Pending offer or counterterms | Closes the dossier, records refusal, reduces package legitimacy, and increases rivalry without installing a package | `.20.c`, `.22.c`, `.23.b`, close decision |
| `africa_world_sponsorship_remove_mode_decisions` | Host country | `PREV` candidate scope | Removes the four mode actions, four mode missions, and the legacy generic sponsorship mission | Fulfilment, default, actor-loss, and terminal cleanup |
| `africa_world_sponsorship_release_host_obligation` | Host country | `PREV` sponsored actor | Decrements overextension, removes the actor from the bounded sponsorship array, and removes mode decisions | Non-material fulfilment/default and cleanup |
| `africa_world_sponsorship_fulfil_current_mode` | Candidate country | One grounded active duty | Material mode delegates exactly once to `africa_world_fulfil_current_sponsorship_obligation`; diplomatic, military, and ideological modes apply distinct gains and close the host ledger | Four fulfil actions, `.29.a`, `.30.a`, `.31.a`, `.31.b` |
| `africa_world_sponsorship_default_current_mode` | Candidate country | One grounded active duty | Material mode delegates existing default logic; other modes create distinct rivalry, confidence, union-block, or sovereignty consequences and close the host ledger | Mode mission timeouts, `.29.b`, `.30.b`, `.31.c` |
| `africa_world_sponsorship_call_military_defence` | Candidate country | Military duty and an active war | Saves a short-lived candidate target, marks the call pending, and fires host `.29` | A bounded military call decision or parent war hook |
| `africa_world_sponsorship_open_diplomatic_mediation` | Host country | Short-lived candidate target and diplomatic duty | Marks mediation opened and fires `.30` | Diplomatic fulfil action |
| `africa_world_sponsorship_open_ideological_congress` | Host country | Short-lived candidate target and ideological duty | Marks congress opened and fires `.31` | Ideological fulfil action |
| `africa_world_sponsorship_record_ideological_capture` | Candidate country | Ideological duty | Records a sovereignty grievance and reduces both package legitimacy and authority without setting ideology or party popularity | `.31.b` |
| `africa_world_sponsorship_cleanup_active_state` | Candidate country | Active offer, counterterms, duty, or military call | Clears active flags, removes a military guarantee if present, and removes the actor from the host array and mode decisions | Parent actor-loss and terminal cleanup hooks |

The long-lived sponsorship pointer is `africa_world_sponsorship_targets` on the host plus the candidate mode and duty flags.

`africa_world_sponsorship_candidate` is a regular event target only for the current offer, counterterm, fulfilment, call, mediation, or congress chain.

Any later targeted decision must save `FROM` as `africa_world_sponsorship_candidate` immediately before firing `.29`, `.30`, or `.31`; no regular target is relied on across the 180-day obligation.

## Trigger map

- `africa_world_sponsorship_mode_is_grounded` accepts only `diplomatic`, `material`, `military`, and `ideological`; `none` and the reserved `high_chaos` value fail.
- `africa_world_sponsorship_candidate_is_offerable` requires the existing candidate and implementation-ready flags, no refusal, and a current host.
- `africa_world_sponsorship_host_can_offer` reuses the existing sponsorship chaos gate and prevents a second offer while any bounded host target has an active obligation.
- `africa_world_sponsorship_host_can_renegotiate` exposes the host review action while an offer is pending without depending on a regular event target surviving the offer chain.
- Four mode-specific `..._obligation_is_due` triggers require an installed package, the generic due flag, the matching mode, and no default flag.
- `africa_world_sponsorship_host_can_honor_military_call`, `...host_can_mediate`, and `...host_can_hold_ideological_congress` require a short-lived candidate target and the corresponding mode due trigger.
- `africa_world_sponsorship_active_cleanup_is_needed` is intentionally narrow and never iterates over countries.

## Required script constants

Add this category to `common/script_constants/012_africa_world_order_constants.txt` in the parent integration change.

```text
africa_world_sponsorship_mode = {
	schema = {
		any_key = yes
		data = fixed_point
	}

	none = 0
	diplomatic = 1
	material = 2
	military = 3
	ideological = 4
	high_chaos = 5

	counterterm_pp_cost = 35
	diplomatic_offer_pp = 75
	material_offer_pp = 50
	military_offer_pp = 50
	military_offer_command_power = 25
	ideological_offer_pp = 100

	diplomatic_legitimacy_gain = 10
	diplomatic_authority_gain = 5
	military_capacity_gain = 15
	military_authority_gain = 10
	ideological_legitimacy_gain = 10
	ideological_capacity_gain = 5
	capture_legitimacy_loss = 15

	ai_accept_base = 40
	ai_accept_diplomatic = 12
	ai_accept_material = 10
	ai_accept_military = 8
	ai_accept_ideological = 6
	ai_accept_legitimacy_bonus = 12
	ai_accept_grievance_penalty = -20
	ai_negotiate_base = 30
	ai_negotiate_safeguard_bonus = 20
	ai_negotiate_material_bonus = 10
	ai_refuse_base = 20
	ai_refuse_grievance_bonus = 25
	ai_refuse_ideological_bonus = 10
	ai_notice_base = 1
	ai_counterterms_accept_base = 55
	ai_counterterms_accept_authority_bonus = 15
	ai_counterterms_revise_base = 30
	ai_counterterms_close_base = 15
	ai_counterterms_candidate_accept_base = 60
	ai_counterterms_candidate_refuse_base = 40
	ai_honor_military_base = 60
	ai_honor_military_authority_bonus = 15
	ai_contest_military_base = 40
	ai_mediate_base = 60
	ai_abandon_mediation_base = 40
	ai_congress_base = 60
	ai_capture_base = 25
	ai_cancel_congress_base = 15
	ai_offer_diplomatic_base = 45
	ai_offer_material_base = 45
	ai_offer_military_base = 35
	ai_offer_ideological_base = 30
	obligation_days = 180
}
```

The existing `africa_world_order.sponsorship_equipment`, `sponsorship_support_equipment`, `sponsorship_convoys`, `sponsorship_overextension_per_package`, and `negative_one` constants remain authoritative for material delivery and cleanup.

Do not add `defaulted` as a mode enum value.

The high-chaos value is reserved for later design and must remain unavailable in this tranche.

## Integration-ready offer decisions

Insert these four targeted decisions in `africa_world_order_actions_category` in `common/decisions/012_africa_decisions.txt`.

```text
africa_world_choose_diplomatic_sponsorship = {
	name = africa_world_choose_diplomatic_sponsorship
	desc = africa_world_choose_diplomatic_sponsorship_desc
	icon = GFX_decision_012_africa_charter_ledger
	target_array = africa_world_package_candidates
	target_root_trigger = { africa_world_sponsorship_host_can_offer = yes }
	target_trigger = { FROM = { africa_world_sponsorship_candidate_is_offerable = yes } }
	visible = { africa_world_sponsorship_host_can_offer = yes }
	available = { FROM = { africa_world_sponsorship_candidate_is_offerable = yes } political_power > constant:africa_world_sponsorship_mode.diplomatic_offer_pp }
	custom_cost_trigger = { political_power > constant:africa_world_sponsorship_mode.diplomatic_offer_pp }
	custom_cost_text = africa_world_sponsorship_diplomatic_offer_cost
	complete_effect = {
		FROM = {
			save_event_target_as = africa_world_sponsorship_candidate
			set_variable = { africa_world_requested_sponsorship_mode = constant:africa_world_sponsorship_mode.diplomatic }
			africa_world_sponsorship_prepare_offer = yes
		}
	}
	ai_will_do = { base = constant:africa_world_sponsorship_mode.ai_offer_diplomatic_base }
}

africa_world_choose_material_sponsorship = {
	name = africa_world_choose_material_sponsorship
	desc = africa_world_choose_material_sponsorship_desc
	icon = GFX_decision_012_africa_charter_ledger
	target_array = africa_world_package_candidates
	target_root_trigger = { africa_world_sponsorship_host_can_offer = yes }
	target_trigger = { FROM = { africa_world_sponsorship_candidate_is_offerable = yes } }
	visible = { africa_world_sponsorship_host_can_offer = yes }
	available = { FROM = { africa_world_sponsorship_candidate_is_offerable = yes } political_power > constant:africa_world_sponsorship_mode.material_offer_pp }
	custom_cost_trigger = { political_power > constant:africa_world_sponsorship_mode.material_offer_pp }
	custom_cost_text = africa_world_sponsorship_material_offer_cost
	complete_effect = {
		FROM = {
			save_event_target_as = africa_world_sponsorship_candidate
			set_variable = { africa_world_requested_sponsorship_mode = constant:africa_world_sponsorship_mode.material }
			africa_world_sponsorship_prepare_offer = yes
		}
	}
	ai_will_do = { base = constant:africa_world_sponsorship_mode.ai_offer_material_base }
}

africa_world_choose_military_sponsorship = {
	name = africa_world_choose_military_sponsorship
	desc = africa_world_choose_military_sponsorship_desc
	icon = GFX_decision_012_africa_charter_ledger
	target_array = africa_world_package_candidates
	target_root_trigger = { africa_world_sponsorship_host_can_offer = yes }
	target_trigger = { FROM = { africa_world_sponsorship_candidate_is_offerable = yes } }
	visible = { africa_world_sponsorship_host_can_offer = yes }
	available = {
		FROM = { africa_world_sponsorship_candidate_is_offerable = yes }
		political_power > constant:africa_world_sponsorship_mode.military_offer_pp
		command_power > constant:africa_world_sponsorship_mode.military_offer_command_power
	}
	custom_cost_trigger = { political_power > constant:africa_world_sponsorship_mode.military_offer_pp command_power > constant:africa_world_sponsorship_mode.military_offer_command_power }
	custom_cost_text = africa_world_sponsorship_military_offer_cost
	complete_effect = {
		FROM = {
			save_event_target_as = africa_world_sponsorship_candidate
			set_variable = { africa_world_requested_sponsorship_mode = constant:africa_world_sponsorship_mode.military }
			africa_world_sponsorship_prepare_offer = yes
		}
	}
	ai_will_do = { base = constant:africa_world_sponsorship_mode.ai_offer_military_base }
}

africa_world_choose_ideological_sponsorship = {
	name = africa_world_choose_ideological_sponsorship
	desc = africa_world_choose_ideological_sponsorship_desc
	icon = GFX_decision_012_africa_charter_ledger
	target_array = africa_world_package_candidates
	target_root_trigger = { africa_world_sponsorship_host_can_offer = yes }
	target_trigger = { FROM = { africa_world_sponsorship_candidate_is_offerable = yes } }
	visible = { africa_world_sponsorship_host_can_offer = yes }
	available = { FROM = { africa_world_sponsorship_candidate_is_offerable = yes } political_power > constant:africa_world_sponsorship_mode.ideological_offer_pp }
	custom_cost_trigger = { political_power > constant:africa_world_sponsorship_mode.ideological_offer_pp }
	custom_cost_text = africa_world_sponsorship_ideological_offer_cost
	complete_effect = {
		FROM = {
			save_event_target_as = africa_world_sponsorship_candidate
			set_variable = { africa_world_requested_sponsorship_mode = constant:africa_world_sponsorship_mode.ideological }
			africa_world_sponsorship_prepare_offer = yes
		}
	}
	ai_will_do = { base = constant:africa_world_sponsorship_mode.ai_offer_ideological_base }
}
```

The helper charges the host inside `africa_world_sponsorship_prepare_offer`, so these decisions must not also use a normal `cost =` field.

## Integration-ready fulfil actions

Replace the legacy `africa_world_fulfil_sponsorship_obligation` presentation with these four targeted actions.

```text
africa_world_fulfil_diplomatic_sponsorship = {
	name = africa_world_fulfil_diplomatic_sponsorship
	desc = africa_world_fulfil_diplomatic_sponsorship_desc
	icon = GFX_decision_012_africa_charter_ledger
	target_array = africa_world_sponsorship_targets
	activation = { africa_is_current_host = yes }
	target_root_trigger = { africa_is_current_host = yes }
	target_trigger = { FROM = { africa_world_sponsorship_diplomatic_obligation_is_due = yes } }
	visible = { africa_is_current_host = yes }
	available = { FROM = { africa_world_sponsorship_diplomatic_obligation_is_due = yes } }
	cost = 0
	complete_effect = {
		FROM = { save_event_target_as = africa_world_sponsorship_candidate }
		africa_world_sponsorship_open_diplomatic_mediation = yes
	}
	ai_will_do = { base = constant:africa_world_sponsorship_mode.ai_mediate_base }
}

africa_world_fulfil_material_sponsorship = {
	name = africa_world_fulfil_material_sponsorship
	desc = africa_world_fulfil_material_sponsorship_desc
	icon = GFX_decision_012_africa_charter_ledger
	target_array = africa_world_sponsorship_targets
	activation = { africa_is_current_host = yes }
	target_root_trigger = { africa_is_current_host = yes }
	target_trigger = { FROM = { africa_world_sponsorship_material_obligation_is_due = yes } }
	visible = { africa_is_current_host = yes }
	available = {
		FROM = { africa_world_sponsorship_material_obligation_is_due = yes }
		has_equipment = { infantry_equipment > constant:africa_world_order.sponsorship_equipment }
		has_equipment = { support_equipment > constant:africa_world_order.sponsorship_support_equipment }
		has_equipment = { convoy > constant:africa_world_order.sponsorship_convoys }
	}
	cost = 0
	complete_effect = { FROM = { africa_world_sponsorship_fulfil_current_mode = yes } }
	ai_will_do = { base = constant:africa_world_sponsorship_mode.ai_offer_material_base }
}

africa_world_fulfil_military_sponsorship = {
	name = africa_world_fulfil_military_sponsorship
	desc = africa_world_fulfil_military_sponsorship_desc
	icon = GFX_decision_012_africa_charter_ledger
	target_array = africa_world_sponsorship_targets
	activation = { africa_is_current_host = yes }
	target_root_trigger = { africa_is_current_host = yes }
	target_trigger = { FROM = { africa_world_sponsorship_military_obligation_is_due = yes } }
	visible = { africa_is_current_host = yes }
	available = { FROM = { africa_world_sponsorship_military_obligation_is_due = yes } }
	cost = 0
	complete_effect = {
		FROM = {
			save_event_target_as = africa_world_sponsorship_candidate
			africa_world_sponsorship_fulfil_current_mode = yes
		}
	}
	ai_will_do = { base = constant:africa_world_sponsorship_mode.ai_honor_military_base }
}

africa_world_fulfil_ideological_sponsorship = {
	name = africa_world_fulfil_ideological_sponsorship
	desc = africa_world_fulfil_ideological_sponsorship_desc
	icon = GFX_decision_012_africa_charter_ledger
	target_array = africa_world_sponsorship_targets
	activation = { africa_is_current_host = yes }
	target_root_trigger = { africa_is_current_host = yes }
	target_trigger = { FROM = { africa_world_sponsorship_ideological_obligation_is_due = yes } }
	visible = { africa_is_current_host = yes }
	available = { FROM = { africa_world_sponsorship_ideological_obligation_is_due = yes } }
	cost = 0
	complete_effect = {
		FROM = { save_event_target_as = africa_world_sponsorship_candidate }
		africa_world_sponsorship_open_ideological_congress = yes
	}
	ai_will_do = { base = constant:africa_world_sponsorship_mode.ai_congress_base }
}
```

The material action checks stores but does not duplicate stockpile effects.

The existing material helper remains the only place that removes 1,500 infantry equipment, 300 support equipment, and 15 convoys.

The military action is the host's routine guarantee or training closeout; the helper also supports a separate defensive call event while the duty remains due.

## Integration-ready mission and response actions

Use these mission skeletons with `days_mission_timeout = constant:africa_world_sponsorship_mode.obligation_days`.

```text
africa_world_sponsorship_diplomatic_obligation = {
	name = africa_world_sponsorship_diplomatic_obligation
	desc = africa_world_sponsorship_diplomatic_obligation_desc
	icon = GFX_decision_012_africa_charter_ledger
	activation = { africa_is_current_host = yes }
	target_array = africa_world_sponsorship_targets
	target_trigger = { FROM = { africa_world_sponsorship_diplomatic_obligation_is_due = yes } }
	days_mission_timeout = constant:africa_world_sponsorship_mode.obligation_days
	is_good = no
	available = { always = no }
	cancel_trigger = { OR = { has_global_flag = world_end FROM = { NOT = { africa_world_sponsorship_diplomatic_obligation_is_due = yes } } } }
	timeout_effect = { FROM = { africa_world_sponsorship_default_current_mode = yes } }
}

africa_world_sponsorship_material_obligation = {
	name = africa_world_sponsorship_material_obligation
	desc = africa_world_sponsorship_material_obligation_desc
	icon = GFX_decision_012_africa_charter_ledger
	activation = { africa_is_current_host = yes }
	target_array = africa_world_sponsorship_targets
	target_trigger = { FROM = { africa_world_sponsorship_material_obligation_is_due = yes } }
	days_mission_timeout = constant:africa_world_sponsorship_mode.obligation_days
	is_good = no
	available = { always = no }
	cancel_trigger = { OR = { has_global_flag = world_end FROM = { NOT = { africa_world_sponsorship_material_obligation_is_due = yes } } } }
	timeout_effect = { FROM = { africa_world_sponsorship_default_current_mode = yes } }
}

africa_world_sponsorship_military_obligation = {
	name = africa_world_sponsorship_military_obligation
	desc = africa_world_sponsorship_military_obligation_desc
	icon = GFX_decision_012_africa_charter_ledger
	activation = { africa_is_current_host = yes }
	target_array = africa_world_sponsorship_targets
	target_trigger = { FROM = { africa_world_sponsorship_military_obligation_is_due = yes } }
	days_mission_timeout = constant:africa_world_sponsorship_mode.obligation_days
	is_good = no
	available = { always = no }
	cancel_trigger = { OR = { has_global_flag = world_end FROM = { NOT = { africa_world_sponsorship_military_obligation_is_due = yes } } } }
	timeout_effect = { FROM = { africa_world_sponsorship_default_current_mode = yes } }
}

africa_world_sponsorship_ideological_obligation = {
	name = africa_world_sponsorship_ideological_obligation
	desc = africa_world_sponsorship_ideological_obligation_desc
	icon = GFX_decision_012_africa_charter_ledger
	activation = { africa_is_current_host = yes }
	target_array = africa_world_sponsorship_targets
	target_trigger = { FROM = { africa_world_sponsorship_ideological_obligation_is_due = yes } }
	days_mission_timeout = constant:africa_world_sponsorship_mode.obligation_days
	is_good = no
	available = { always = no }
	cancel_trigger = { OR = { has_global_flag = world_end FROM = { NOT = { africa_world_sponsorship_ideological_obligation_is_due = yes } } } }
	timeout_effect = { FROM = { africa_world_sponsorship_default_current_mode = yes } }
}
```

The parent installer must activate only the matching mode mission when `PREV` has the selected mode.

The legacy generic mission may remain as a migration cleanup target, but it must not be activated for a new W3 mode.

## Renegotiation and refusal review decisions

The requested IDs can use these bounded target actions.

```text
africa_world_renegotiate_sponsorship_safeguards = {
	name = africa_world_renegotiate_sponsorship_safeguards
	desc = africa_world_renegotiate_sponsorship_safeguards_desc
	icon = GFX_decision_012_africa_charter_ledger
	target_array = africa_world_package_candidates
	target_root_trigger = { africa_world_sponsorship_host_can_renegotiate = yes }
	target_trigger = { FROM = { africa_world_sponsorship_offer_is_pending = yes } }
	visible = { africa_world_sponsorship_host_can_renegotiate = yes }
	available = { FROM = { africa_world_sponsorship_offer_is_pending = yes } }
	cost = 0
	complete_effect = { FROM = { africa_world_sponsorship_open_counterterms = yes } }
	ai_will_do = { base = constant:africa_world_sponsorship_mode.ai_negotiate_base }
}

africa_world_close_sponsorship_after_refusal = {
	name = africa_world_close_sponsorship_after_refusal
	desc = africa_world_close_sponsorship_after_refusal_desc
	icon = GFX_decision_012_africa_charter_ledger
	target_array = africa_world_package_candidates
	target_root_trigger = { africa_is_current_host = yes }
	target_trigger = { FROM = { has_country_flag = africa_world_sponsorship_refused } }
	visible = { africa_is_current_host = yes }
	available = { FROM = { has_country_flag = africa_world_sponsorship_refused } }
	cost = 0
	complete_effect = { FROM = { set_country_flag = africa_world_sponsorship_refusal_reviewed } }
	ai_will_do = { base = constant:africa_world_sponsorship_mode.ai_notice_base }
}
```

`africa_world_close_sponsorship_after_refusal` is a review marker and must not clear the historical refusal, rivalry memory, or independent candidate state.

## Installer migration

Update `africa_world_install_current_package` in `common/scripted_effects/012_africa_world_order_effects.txt` so a newly accepted W3 package activates only its matching mode mission.

Keep the old `africa_world_sponsorship_obligation` activation as a migration branch only when no grounded sponsorship mode exists.

The existing generic material helper and its exact array removal remain in place.

Route the old `africa_world_fulfil_sponsorship_obligation` decision to `africa_world_fulfil_material_sponsorship` and the existing `africa_world_fulfil_current_sponsorship_obligation` through the new wrapper.

Do not copy the stockpile subtraction into the new effect file.

On actor loss, world-end, terminal resolution, or package removal, invoke `africa_world_sponsorship_cleanup_active_state` in the candidate scope before removing the candidate from the host's `africa_world_sponsorship_targets` array.

The cleanup helper removes a military guarantee only when `africa_world_sponsorship_guarantee_active` is present.

## Validation and evidence

Read the repository instructions, `chaos-redux-events`, `hoi4-decisions-missions`, and `chaos-redux-subagents` skills before editing.

Read the required offline Paradox wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, and AI modding.

Read the vanilla effects, triggers, modifiers, and script-constant documentation under `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation`.

Read the linked existing Event 012 package installer, generic sponsorship helper, generic sponsorship decisions, and vanilla/BBA event precedents.

Read-only `hoi4.event_inspect` evidence was collected for `africa_world_order.102` and vanilla `bba_african_union.1`.

The new `.20` event was also lint-inspected read-only at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3ec7cce3aa69d7bfd6034ebc474f7104495cb7f35528fcf7b10a8863093237d0/56b32be3476004053af904b2bfafacf3e7b1702f267fa1d0f02b6a2978925f8a/event-lint-8698fd27aef8.json`.

Artifacts: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/733ddbdf346bc618afb725118f68e129ec73e8b4097028c8788d4c835ca87b2a/9090985aec290ce750862c8bdbdd7ff7f6f9759d1a99b7bd9e76c80e6d38e654/event-scan-f84da2c23776.json`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f4056674345cae872342382be710512f5626f10424c198eb020b1aa93f30d049/743e9fad701bf1b47797d4b65e5303d37ca6e244e0795b3543d72be20a51175d/event-state_flow-f84da2c23776.json`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b904c989362e6c6d843aded7c753aeae3bca6c627a2c5e5e1016a9644d94c419/3250bfbecaad28bbc0cde0ef86c08426bc66bd8e1c67d989d818f308a37f463a/event-scan-f84da2c23776.json`.

The MCP projections were read-only and partial because workspace-wide helper projections deferred unresolved nodes and reported workspace issue inventory `issues=2054` for the new lint pass and `issues=2022` for the earlier linked event scans; no blocking diagnostic was returned for the inspected event surfaces.

Task-specific local checks completed: brace counts match in all three script files, new scripts contain no unsupported `<=` or `>=`, all requested event IDs `.20` through `.31` are present, and the localisation file begins with UTF-8 BOM bytes `239,187,191`.

The game was not launched, and no in-game consumer validation was performed.

## Known limitations and follow-up

The isolated-file boundary does not include a dedicated opinion-modifier definition, so diplomatic sponsorship records protected conference status and legitimacy or authority gains but does not yet apply a new bilateral opinion modifier.

If the parent wants a true opinion delta, add a dedicated modifier under `common/opinion_modifiers/` and apply it from the diplomatic fulfilment branch while retaining the current protected-conference flag.

The host-side legitimacy field is not a shared Event 012 variable in the inspected package code, so diplomatic default reduces existing `africa_member_confidence` when present and always raises `africa_global_rivalry`.

The parent must wire the military war hook that calls `africa_world_sponsorship_call_military_defence`; no unrestricted `on_daily` or world iteration was added.

No high-chaos mode, tag creation, model work, fallback tree, or duplicated material store effect was added.
