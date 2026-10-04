# Observation, actual target, and reader source hunks

Disposition: proposed source hunks for parent review, not an applied or fully expanded implementation.
Insert definitions into Event014's existing owner files and call them only from the mapped report and committed result transactions.
The full reset and adapter coverage is specified in `owner_api_proposal.md`.
These hunks supersede the earlier suggestion to hide every foreign country without a private identity receipt.
Public warlord countries remain visible under their existing tab predicates without report delivery.
Country identity and public diplomacy are independent of secret field permission.
The parent must retain existing decision eligibility and costs.

## Viewer epoch and exact subject scope

Add this COUNTRY effect and call it in an explicit observer scope before a writer enters its subject.
Initialize absent storage only, and never reset an established epoch during report delivery.
Incarnation reset clears indexed observations and then increments the epoch, including for an ordinary human viewer.

```txt
cannibalism_ui_ensure_viewer_epoch = {
	if = {
		limit = { NOT = { has_variable = cannibalism_ui_viewer_epoch } }
		set_variable = { cannibalism_ui_viewer_epoch = constant:cannibalism_gui_value.one }
	}
}
```

Writer convention: enter the explicit observer COUNTRY, then enter the explicit subject COUNTRY or STATE directly.
`PREV` is that observer and `_@PREV` keys this transaction's subject record.
Readers in native rows use ROOT viewer and `_@ROOT`.
Do not insert another scope between observer and subject or key writers using a pulse anchor's ROOT.
Before writing fields, compare the previous record kind, observer epoch, subject identity, and source identity.
If any differ, clear that observer's complete old record on this subject before publishing the new record.
Otherwise update only fields genuinely observed by this transaction.
The `cannibalism_ui_clear_*_observation` helpers described in the API proposal must be applied with these writers, not left for a later cleanup pass.

## Exact warning receipt insertion

In `chaosx.nr14.60.immediate`, inside the existing successful guard at events:271–283, append the following after setting `cannibalism_warning_expected_spread_id` and the open flag.
This records that delivered warning for the recipient, and cannot discover foreign strength.
The explicit STATE target and root recipient are already supplied by the event.
Ensure the epoch on the observer, then use `cannibalism_ui_prepare_warning_observation` to clear a mismatched old record and update the two reciprocal STATE-pair memberships.
That preparer uses the identical direct observer-to-subject nesting below.

```txt
ROOT = {
	cannibalism_ui_ensure_viewer_epoch = yes
	event_target:cannibalism_spread_target_state = {
		# PREV is the actual report recipient COUNTRY.
		if = {
			limit = { cannibalism_ui_warning_snapshot_writable = yes }
			cannibalism_ui_prepare_warning_observation = yes
			set_state_flag = cannibalism_ui_identity_observed_@PREV
			set_variable = { cannibalism_ui_observer_epoch_@PREV = PREV.cannibalism_ui_viewer_epoch }
			set_variable = { cannibalism_ui_record_kind_@PREV = constant:cannibalism_ui_record_kind.warning }
			set_variable = { cannibalism_ui_subject_spread_id_@PREV = cannibalism_warning_expected_spread_id }
			set_variable = { cannibalism_ui_source_country_@PREV = cannibalism_inbound_spread_source_country }
			set_variable = { cannibalism_ui_source_generation_@PREV = cannibalism_inbound_spread_source_generation }
			set_state_flag = cannibalism_ui_route_observed_@PREV
			set_variable = { cannibalism_ui_observed_route_@PREV = cannibalism_inbound_spread_route }
			set_variable = { cannibalism_ui_route_observed_date_@PREV = global.date }
			set_state_flag = cannibalism_ui_incident_observed_@PREV
			set_variable = { cannibalism_ui_last_incident_@PREV = constant:cannibalism_ui_incident.inbound_warning }
			set_variable = { cannibalism_ui_last_incident_date_@PREV = global.date }
		}
	}
}
```

Strength/type flags are deliberately absent because a warning without an active node cannot establish them.
The separate writable guard below checks route/source presence and a positive exact expected ID before any preparer or field write.
The parent must reject incomplete inbound snapshots rather than assigning zero route or inventing a source.
Warning and node records are disjoint kinds, and replacement by a genuinely observed new node clears old warning fields first.

The guard and preparer definitions for that insertion are concrete:

```txt
# STATE with PREV observer COUNTRY. The source must still be the exact actor.
cannibalism_ui_warning_snapshot_writable = {
	PREV = { exists = yes check_variable = { cannibalism_ui_viewer_epoch > constant:cannibalism_gui_value.zero } }
	has_state_flag = cannibalism_spread_inbound_active
	has_variable = cannibalism_warning_expected_spread_id
	check_variable = { cannibalism_warning_expected_spread_id > constant:cannibalism_gui_value.zero }
	check_variable = { var = cannibalism_warning_expected_spread_id value = cannibalism_inbound_spread_id compare = equals }
	has_variable = cannibalism_inbound_spread_route
	check_variable = { cannibalism_inbound_spread_route > constant:cannibalism_spread_route.none }
	has_variable = cannibalism_inbound_spread_source_country
	check_variable = { cannibalism_inbound_spread_source_generation > constant:cannibalism_gui_value.zero }
	var:cannibalism_inbound_spread_source_country = {
		exists = yes
		check_variable = { var = cannibalism_actor_generation value = PREV.cannibalism_inbound_spread_source_generation compare = equals }
	}
}

# EFFECT only. Direct caller already passed the exact snapshot guard.
cannibalism_ui_prepare_warning_observation = {
	if = {
		limit = {
			NOT = {
				AND = {
					check_variable = { cannibalism_ui_record_kind_@PREV = constant:cannibalism_ui_record_kind.warning }
					check_variable = { var = cannibalism_ui_observer_epoch_@PREV value = PREV.cannibalism_ui_viewer_epoch compare = equals }
					check_variable = { var = cannibalism_ui_subject_spread_id_@PREV value = cannibalism_warning_expected_spread_id compare = equals }
					check_variable = { var = cannibalism_ui_source_country_@PREV value = cannibalism_inbound_spread_source_country compare = equals }
					check_variable = { var = cannibalism_ui_source_generation_@PREV value = cannibalism_inbound_spread_source_generation compare = equals }
				}
			}
		}
		cannibalism_ui_clear_state_observation = yes
	}
	if = {
		limit = { NOT = { is_in_array = { array = cannibalism_ui_observer_countries value = PREV } } }
		add_to_array = { cannibalism_ui_observer_countries = PREV }
	}
	PREV = {
		if = {
			limit = { NOT = { is_in_array = { array = cannibalism_ui_observed_state_entries value = PREV } } }
			add_to_array = { cannibalism_ui_observed_state_entries = PREV }
		}
	}
}

# STATE with PREV observer COUNTRY. No reads of a reset source are needed.
cannibalism_ui_clear_state_observation = {
	clr_state_flag = cannibalism_ui_identity_observed_@PREV
	clr_state_flag = cannibalism_ui_type_observed_@PREV
	clr_state_flag = cannibalism_ui_strength_observed_@PREV
	clr_state_flag = cannibalism_ui_route_observed_@PREV
	clr_state_flag = cannibalism_ui_incident_observed_@PREV
	clr_state_flag = cannibalism_ui_counteraction_selected_@PREV
	clear_variable = cannibalism_ui_observer_epoch_@PREV
	clear_variable = cannibalism_ui_record_kind_@PREV
	clear_variable = cannibalism_ui_subject_generation_@PREV
	clear_variable = cannibalism_ui_subject_node_id_@PREV
	clear_variable = cannibalism_ui_subject_spread_id_@PREV
	clear_variable = cannibalism_ui_source_country_@PREV
	clear_variable = cannibalism_ui_source_generation_@PREV
	clear_variable = cannibalism_ui_observed_node_type_@PREV
	clear_variable = cannibalism_ui_observed_strength_band_@PREV
	clear_variable = cannibalism_ui_observed_route_@PREV
	clear_variable = cannibalism_ui_last_incident_@PREV
	clear_variable = cannibalism_ui_counteraction_@PREV
	clear_variable = cannibalism_ui_counteraction_status_@PREV
	clear_variable = cannibalism_ui_strength_observed_date_@PREV
	clear_variable = cannibalism_ui_route_observed_date_@PREV
	clear_variable = cannibalism_ui_last_incident_date_@PREV
	clear_variable = cannibalism_ui_counteraction_date_@PREV
	remove_from_array = { array = cannibalism_ui_observer_countries value = PREV }
	PREV = {
		remove_from_array = { array = cannibalism_ui_observed_state_entries value = PREV }
	}
}
```

This clearing helper also handles warning-to-node replacement before a new record is published.
The COUNTRY clear counterpart uses country flags and the observer's country-subject index with the same variable inventory.
Use the exact scope contract on every retirement/transfer caller rather than passing a viewer as ROOT and assuming PREV follows it.

Add this pure STATE trigger for warning readers.
It validates the stored source object and generation, not `scope_exists` on a variable.
Native source COUNTRY existence and generation are required without printing its hidden name.

```txt
cannibalism_ui_warning_observation_valid = {
	has_state_flag = cannibalism_ui_identity_observed_@ROOT
	ROOT = { check_variable = { cannibalism_ui_viewer_epoch > constant:cannibalism_gui_value.zero } }
	check_variable = { var = cannibalism_ui_observer_epoch_@ROOT value = ROOT.cannibalism_ui_viewer_epoch compare = equals }
	check_variable = { cannibalism_ui_record_kind_@ROOT = constant:cannibalism_ui_record_kind.warning }
	has_state_flag = cannibalism_spread_inbound_active
	check_variable = { cannibalism_ui_subject_spread_id_@ROOT > constant:cannibalism_gui_value.zero }
	check_variable = { var = cannibalism_ui_subject_spread_id_@ROOT value = cannibalism_inbound_spread_id compare = equals }
	check_variable = { var = cannibalism_ui_source_country_@ROOT value = cannibalism_inbound_spread_source_country compare = equals }
	check_variable = { var = cannibalism_ui_source_generation_@ROOT value = cannibalism_inbound_spread_source_generation compare = equals }
	has_variable = cannibalism_ui_source_country_@ROOT
	var:cannibalism_ui_source_country_@ROOT = {
		exists = yes
		check_variable = { var = cannibalism_actor_generation value = PREV.cannibalism_ui_source_generation_@ROOT compare = equals }
	}
}
```

The source scope in this trigger retains ROOT viewer and PREV state.
Add node and country counterparts using the exact fields in the owner API proposal.
Those counterparts are required before wiring their callers, and this warning hunk does not certify their execution.
An unrelated UI state selection is never a source for a report or mission receipt.

## Trigger-context route reader

For a STATE route field, add this branch to `GetCannibalismUiNetworkKnownRoute`.
It uses only commands listed in installed triggers documentation and keeps caller-owned temporary storage in this `text.trigger`.
Country rows use the corresponding country flag and actor-generation guard in separate branches.

```txt
text = {
	trigger = {
		OR = {
			cannibalism_ui_warning_observation_valid = yes
			cannibalism_ui_node_observation_valid = yes
		}
		has_state_flag = cannibalism_ui_route_observed_@ROOT
		set_temp_variable = { cannibalism_ui_row_route = constant:cannibalism_gui_value.zero }
		cannibalism_ui_load_state_route = yes
		check_variable = { cannibalism_ui_row_route = constant:cannibalism_spread_route.retreat }
	}
	localization_key = cannibalism_spread_route_retreat
}
```

The authoritative installed Event014 getter currently uses `retreat`, `prisoner_transfer`, `convoy`, `volunteer_return`, `occupation_turnover`, `deliberate_seed`, `conquest`, and `survivor`.
Read the exact constants before expanding the remaining branches, and do not add an alias to cover a mismatch.
The minimal trigger loader is:

```txt
cannibalism_ui_load_state_route = {
	OR = {
		cannibalism_ui_warning_observation_valid = yes
		cannibalism_ui_node_observation_valid = yes
	}
	has_state_flag = cannibalism_ui_route_observed_@ROOT
	set_temp_variable = { cannibalism_ui_row_route = cannibalism_ui_observed_route_@ROOT }
}
```

No `set_variable`, array mutation, `if.limit` effect block, `save_event_target_as`, or scripted-effect call belongs in this loader or a `defined_text.text.trigger`.
Do not assume trigger evaluator short-circuiting for unsafe pointer/index dereferences.
The parent must keep invalid subjects and numeric rows out of native lists and put the same validity guard in each consuming branch.
Unknown branches select literal localisation keys and do not consume a zero-initialized output as real information.
Uncertainty is stale on identity or epoch mismatch, partial when any secret required field lacks a receipt, and observed when the required receipts for that subject are present.
An unobserved public warlord still has a visible name with unknown secret cells.
No observation-age timer or inferred confidence score is proposed.

## Actual mission counteraction hook

Inside the successful start transaction for `cannibalism_start_investigation_mission`, after `activate_mission`, add a direct adapter from the existing target STATE.
Caller checks `cannibalism_investigation_target_is_valid` and enters the acting country immediately before its state target.
The subject preparer publishes the matching node identity when captured, or an own-subject fact record when no node identity exists.
It must never interpret a no-node investigation as discovery of a hidden node.

```txt
if = {
	limit = { cannibalism_investigation_target_is_valid = yes }
	THIS = {
		cannibalism_ui_ensure_viewer_epoch = yes
		var:cannibalism_investigation_target_state = {
			cannibalism_ui_prepare_investigation_observation = yes
			set_state_flag = cannibalism_ui_counteraction_selected_@PREV
			set_variable = { cannibalism_ui_counteraction_@PREV = constant:cannibalism_ui_counteraction.investigation }
			set_variable = { cannibalism_ui_counteraction_status_@PREV = constant:cannibalism_ui_action_status.active }
			set_variable = { cannibalism_ui_counteraction_date_@PREV = global.date }
		}
	}
}
```

For `complete`, `partial`, and `fail_investigation_mission`, insert the analogous status/result writer immediately before the existing `cannibalism_clear_investigation_mission` call, after gameplay consequences.
Cancellation writes `cancelled` only if a previously recorded order and exact subject identity still match, then clears runtime normally.
Result adapters publish the incident enum and date as well as last order status.
Failure alone reveals no strength, type, or route.
Success/partial may snapshot node strength/type only on the mission's validated actual node and accepted outcome disclosure.
The hooks table in the owner proposal covers all six targeted mission families and both screening payments.
Do not select a counteraction when a tab or card is clicked.

## Controlled state and committed campaign hunks

Add `cannibalism_gui_rebuild_command_view` and call it from initial command setup, an information-only refresh, and existing owned transfer handlers.
The scope wrapper prevents a different caller ROOT from receiving the array.

```txt
cannibalism_gui_rebuild_command_view = {
	clear_array = cannibalism_command_gui_state_entries
	save_event_target_as = cannibalism_ui_command_owner
	every_controlled_state = {
		event_target:cannibalism_ui_command_owner = {
			add_to_array = { cannibalism_command_gui_state_entries = PREV }
		}
	}
	add_to_variable = { cannibalism_command_gui_dirty = constant:cannibalism_gui_value.one }
}
```

The regular target above is transaction-local and does not persist between GUI ticks.
Rows read native THIS state, recheck `is_controlled_by = ROOT`, and show the actual owner/controller and existing state-stage/exhaustion/recovery facts.
Keep recruitment capacity separate.
The live warlord list additionally captures aligned actor generation and slot generation arrays on refresh.
Read current identity/disposition only when those captured values still match, and hide a tag-reused row before its refresh.

At the end of `cannibalism_unified_execute_campaign_operation`, after `create_wargoal`, modifier and committed result updates, add:

```txt
set_variable = { cannibalism_ui_last_campaign_country = event_target:cannibalism_unified_decision_target }
set_variable = { cannibalism_ui_last_campaign_date = global.date }
set_variable = { cannibalism_ui_last_campaign_viewer_epoch = cannibalism_ui_viewer_epoch }
```

Ensure the viewer epoch first, and capture a target-specific epoch before allowing this record to survive country tag reuse.
For Event014 actors use their positive actor generation.
For other public countries use a UI-owned country identity epoch initialized at actual commitment, incremented by known reset/release hooks, with the unsupported external-reset coverage explicitly retained.
Do not pretend an ordinary target has an Event014 actor generation of zero.
The parent must resolve complete external incarnation detection before claiming reuse-proof ordinary-country receipts.
The record is the last committed real `FROM` passed as `cannibalism_unified_decision_target`, distinct from any optional view-only selection.
The active raid API similarly requires an actual decision-owner target and commit hook.
The present non-targeted paid march modifier supplies neither, so its required card remains unresolved until the parent decision owner implements targeted gameplay.
No own-state substitute, fabricated raid receipt, or zero-data completion branch is proposed.
