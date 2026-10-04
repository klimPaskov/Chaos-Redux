# Integrated identity source hunks for parent review

Disposition: proposed implementation under the parent's 2026-10-04 preparation authorization.
These are source replacements and insertions for review, not installed gameplay files.
Base: `common/scripted_effects/014_cannibalism_effects.txt`, SHA-256 `f045bfea8c075818f1cfd3959bc92f02d4708186eb5718834fe8f3305f79e563`, storage commit `a0a6825e7`.
Preserve the existing eight per-slot disposition branches and all 107 caller-owned storage allocations from that commit.
Do not extend the sixteen-output inheritance snapshot or reconstruct historical identities from a current CBA scope.

Insert this block at the beginning of the existing `cannibalism_record_integrated_warlord_slot` body.
The existing body continues after this block unchanged.
Required additional inputs are normal destination variables `cannibalism_integration_donor_generation` and `cannibalism_integration_origin_state`, assigned from the still-existing donor immediately before the record call.
The existing name/origin/region/slot/personality inputs already come from the captured donor inheritance fields, and disposition comes from the existing integration input.
The captured origin-state entry is a STATE pointer, with its stable state identity retained independently of the reusable country tag.

```txt
	if = {
		limit = {
			check_variable = { cannibalism_integration_donor_generation > constant:cannibalism_gui_value.zero }
			has_variable = cannibalism_integration_origin_state
			has_variable = cannibalism_integration_name_index
			has_variable = cannibalism_integration_origin
			has_variable = cannibalism_integration_region
			has_variable = cannibalism_integration_slot_index
			has_variable = cannibalism_integration_personality
			cannibalism_ui_integrated_arrays_aligned = yes
			NOT = {
				is_in_array = {
					array = cannibalism_integrated_warlord_generation_entries
					value = cannibalism_integration_donor_generation
				}
			}
		}
		add_to_array = { cannibalism_integrated_warlord_generation_entries = cannibalism_integration_donor_generation }
		add_to_array = { cannibalism_integrated_warlord_slot_entries = cannibalism_integration_slot_index }
		add_to_array = { cannibalism_integrated_warlord_name_entries = cannibalism_integration_name_index }
		add_to_array = { cannibalism_integrated_warlord_origin_entries = cannibalism_integration_origin }
		add_to_array = { cannibalism_integrated_warlord_region_entries = cannibalism_integration_region }
		add_to_array = { cannibalism_integrated_warlord_personality_entries = cannibalism_integration_personality }
		add_to_array = { cannibalism_integrated_warlord_origin_state_entries = cannibalism_integration_origin_state }
		add_to_array = { cannibalism_integrated_warlord_disposition_entries = cannibalism_integration_disposition }
		add_to_array = { cannibalism_integrated_warlord_date_entries = global.date }
	}
```

Keep all three existing `= yes` record calls and insert two input captures immediately before each call, before constructors and before donor preparation or annexation.

| Existing position | Exact source of the two new captures |
| --- | --- |
| E:12544, opening CBL host | `event_target:cannibalism_unification_host` |
| E:12711, later absorption | `event_target:cannibalism_absorbed_warlord` |
| E:18870, original-ZZZ merge | `event_target:cannibalism_primary_warlord_donor` |

Opening-host insertion:

```txt
clear_variable = cannibalism_integration_donor_generation
clear_variable = cannibalism_integration_origin_state
if = {
	limit = {
		event_target:cannibalism_unification_host = {
			exists = yes
			check_variable = { cannibalism_warlord_slot_generation > constant:cannibalism_gui_value.zero }
			has_variable = cannibalism_warlord_origin_state
		}
	}
	set_variable = { cannibalism_integration_donor_generation = event_target:cannibalism_unification_host.cannibalism_warlord_slot_generation }
	set_variable = { cannibalism_integration_origin_state = event_target:cannibalism_unification_host.cannibalism_warlord_origin_state }
}
cannibalism_record_integrated_warlord_slot = yes
clear_variable = cannibalism_integration_donor_generation
clear_variable = cannibalism_integration_origin_state
```

For the other two sites substitute only the explicit donor target from the table, preserving their existing integration assignments and call ordering.
The clear-before-capture prevents failed input validation from reusing a prior donor's inputs, and clear-after-record prevents these normal staging variables from leaking.
This uses documented variable reads and existing regular event targets and needs no additional scripted-effect parameter interpolation support.

The third call is an additional exact consumer found during the current read.
Its history remains hidden by the existing Wendigo visibility gate, but its donor identity must still be captured before that call.
No change to commander creation, integration counters, inheritance, payment, alignment, or result logic is proposed.

Add these trigger definitions to the owning `014_cannibalism_triggers.txt`.
The native numeric list must keep `change_scope = no`, `value = cannibalism_loyalty_generation`, and `index = cannibalism_loyalty_index`.

```txt
cannibalism_ui_integrated_arrays_aligned = {
	check_variable = { var = cannibalism_integrated_warlord_slot_entries^num value = cannibalism_integrated_warlord_generation_entries^num compare = equals }
	check_variable = { var = cannibalism_integrated_warlord_name_entries^num value = cannibalism_integrated_warlord_generation_entries^num compare = equals }
	check_variable = { var = cannibalism_integrated_warlord_origin_entries^num value = cannibalism_integrated_warlord_generation_entries^num compare = equals }
	check_variable = { var = cannibalism_integrated_warlord_region_entries^num value = cannibalism_integrated_warlord_generation_entries^num compare = equals }
	check_variable = { var = cannibalism_integrated_warlord_personality_entries^num value = cannibalism_integrated_warlord_generation_entries^num compare = equals }
	check_variable = { var = cannibalism_integrated_warlord_origin_state_entries^num value = cannibalism_integrated_warlord_generation_entries^num compare = equals }
	check_variable = { var = cannibalism_integrated_warlord_disposition_entries^num value = cannibalism_integrated_warlord_generation_entries^num compare = equals }
	check_variable = { var = cannibalism_integrated_warlord_date_entries^num value = cannibalism_integrated_warlord_generation_entries^num compare = equals }
}

cannibalism_ui_integrated_row_valid = {
	cannibalism_ui_integrated_arrays_aligned = yes
	check_variable = { var = cannibalism_loyalty_index value = constant:cannibalism_gui_value.zero compare = greater_than_or_equals }
	check_variable = { var = cannibalism_loyalty_index value = cannibalism_integrated_warlord_generation_entries^num compare = less_than }
	check_variable = { cannibalism_loyalty_generation > constant:cannibalism_gui_value.zero }
	check_variable = { var = cannibalism_integrated_warlord_generation_entries^cannibalism_loyalty_index value = cannibalism_loyalty_generation compare = equals }
}

# COUNTRY host, numeric row context. Caller initializes consumed outputs first.
# False means no row, and callers must never consume outputs from a false call.
cannibalism_ui_load_integrated_warlord_row = {
	cannibalism_ui_integrated_row_valid = yes
	set_temp_variable = { cannibalism_ui_loyalty_generation = cannibalism_integrated_warlord_generation_entries^cannibalism_loyalty_index }
	set_temp_variable = { cannibalism_ui_loyalty_slot = cannibalism_integrated_warlord_slot_entries^cannibalism_loyalty_index }
	set_temp_variable = { cannibalism_ui_loyalty_name = cannibalism_integrated_warlord_name_entries^cannibalism_loyalty_index }
	set_temp_variable = { cannibalism_ui_loyalty_origin = cannibalism_integrated_warlord_origin_entries^cannibalism_loyalty_index }
	set_temp_variable = { cannibalism_ui_loyalty_region = cannibalism_integrated_warlord_region_entries^cannibalism_loyalty_index }
	set_temp_variable = { cannibalism_ui_loyalty_personality = cannibalism_integrated_warlord_personality_entries^cannibalism_loyalty_index }
	set_temp_variable = { cannibalism_ui_loyalty_origin_state = cannibalism_integrated_warlord_origin_state_entries^cannibalism_loyalty_index }
	set_temp_variable = { cannibalism_ui_loyalty_disposition = cannibalism_integrated_warlord_disposition_entries^cannibalism_loyalty_index }
	set_temp_variable = { cannibalism_ui_loyalty_date = cannibalism_integrated_warlord_date_entries^cannibalism_loyalty_index }
}
```

The parent must place the validity checks before every array dereference and retain the positive-generation condition on row visibility even if the native trigger evaluator evaluates independent commands eagerly.
Use a conditional valid branch in `defined_text`, with the row guard first, and keep malformed rows invisible.
Do not resize unequal arrays to manufacture history.
The append path preserves old records and rejects repeated generations through native membership.
Its inability to recover an already-lost historical identity is an explicit limit, not a license to snapshot the current tag.

Each defined-text field initializes all outputs that it consumes in its own `text.trigger` before calling the loader.
For example, a disposition branch has this legal trigger-context form.
Other fields repeat this caller-owned initialization with their own consumed outputs.

```txt
defined_text = {
	name = GetCannibalismUiIntegratedWarlordDisposition
	text = {
		trigger = {
			cannibalism_ui_integrated_row_valid = yes
			set_temp_variable = { cannibalism_ui_loyalty_disposition = constant:cannibalism_gui_value.zero }
			cannibalism_ui_load_integrated_warlord_row = yes
			check_variable = { cannibalism_ui_loyalty_disposition = constant:cannibalism_warlord_disposition.host_commander }
		}
		localization_key = cannibalism_ui_loyalty_host_commander
	}
	# Add one guarded branch for each existing disposition enum.
	text = { localization_key = cannibalism_ui_identity_unavailable }
}
```

This is an exact branch hunk, not a complete disposition getter.
The owner API proposal lists every required getter and its consumer, and the parent supplies final English and the remaining enum branches during application.
The loader's other outputs first allocated internally are discarded at return unless that caller preinitialized them, which is safe because this example consumes disposition alone.
An aggregate card must initialize all ten outputs before its call.

Add an effect `cannibalism_ui_clear_integrated_history` clearing all nine arrays by name.
Call it only from the recipient incarnation reset after any validated host replacement has copied all nine arrays as one transaction.
Never call it from donor slot release, node cleanup, Network close, view refresh, or ordinary donor annexation.
Historical rows remain immutable, including their original disposition and date.
Live autonomy, resistance, and pending response belong to the separate current-country list.
No per-history numeric iteration or new global allocator is needed.
