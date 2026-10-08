# Event033 owned loop-break isolation patch, 2026-10-07

Disposition: `implemented` for the bounded source binding/reset repair, with gameplay and native-engine acceptance pending.
The initial patch and before-source capture were performed on 2026-10-07, and the interrupted checkpoint was verified and delivered on 2026-10-08.
Acceptance basis: the parent explicitly authorized private loop-break isolation in the four named Event033 effect files, extended the scope to documented numerical loops, and directed resumption without duplicating completed work.
The parent owns runtime/events/triggers/terminal hooks and final integration, while the UI worker owns GUI effects and scripted localisation.
No commit is made.

## Delivered scope

Three source files changed: `common\scripted_effects\033_acid_rain_aftermath_effects.txt`, `033_acid_rain_achievement_effects.txt`, and `033_acid_rain_preparedness_effects.txt`.
Each actual loop now has its own helper-and-ordinal temporary, a zero reset immediately before invocation, and an explicit `break = <private_temp>` binding.
There are 28 repaired loops in 20 existing helpers: eight `for_each_loop`, fourteen `for_each_scope_loop`, and six `for_loop_effect`.
No `while_loop_effect` exists in these owned files.
The fourth authorized source, `033_acid_rain_cxt_effects.txt`, has no applicable loop and remains byte-identical.

The new test is `.tools\validation\test_033_loop_break_owned_helpers.js`, SHA-256 `96a4b0e1fc91d3d5a546ba41d5e2126511d0cf8feca74800b8bb34f18e62b768`.
It contains exact frozen before bytes for all four files as gzip/base64 data, their decoded byte counts and SHA-256 hashes, precise insertion offsets/text, and the loop manifest.
The only new documentation is this handoff.
The prior Humanitarian and 19-boundary ABI handoffs remain historical and were not overwritten.

The source change is exclusively private binding/reset insertion.
Existing bodies, scope transitions, loop arrays, bounds, comparisons, increments, native numerical iteration caps, cursors, inputs, public output envelopes, persistent fields, receipts and queue operations are preserved.
No cost, AI weight, pool weight, tuning constant, cadence, target selection rule or cleanup mechanic is changed.
No shared helper, runtime, event root, trigger, GUI, workbook, asset or backend source is edited.

## Initial ownership, byte snapshots and hashes

The four owned source paths were clean in the shared checkout before capture.
Preparedness was captured at the committed operation-family repair baseline `BEE4526617BD15431E6356F0498B5CBC98CAF7BF0ED6E1432504EEA3D0F65600`, including the parent's `5abb80dd` repair.
The obsolete `1F6D` preparedness revision was not used for this patch.
The raw archives decode to 399876 bytes in total and preserve the original LF bytes, comments, ordering and complete source content.
The normal test verifies every decoded archive's length/hash, reconstructs the exact permitted after bytes from its recorded insertions, and requires the current source to match that reconstruction.
It also removes only the new private reset/binding nodes from the current AST and requires equality with the original AST.

| Source | Exact before SHA-256 | Verified after SHA-256 |
| --- | --- | --- |
| `common\scripted_effects\033_acid_rain_aftermath_effects.txt` | `2805a9af30ac54e332fb0ec09136c62c232f1b57083df9bee2cedebd6fcae09c` | `1be409c02132f47ab4330a3569fe38a888abca21498262abc9eee0d1201f0c88` |
| `common\scripted_effects\033_acid_rain_achievement_effects.txt` | `256d6a5b22675343cde0775f219b645520455f236fb28a744d5218bcf89e1e68` | `211189c5d72f929c4daac56f6b026338339754f74e9d430a3717b542044e312a` |
| `common\scripted_effects\033_acid_rain_preparedness_effects.txt` | `bee4526617bd15431e6356f0498b5cbc98caf7bf0ed6e1432504eea3d0f65600` | `eea8b037405ae54848d54020571df208314795b2b1394ade4a300590909853dc` |
| `common\scripted_effects\033_acid_rain_cxt_effects.txt` | `35867e2dd578320882675703f283b02d0dcc4e583106e775d788df29c535b49b` | `35867e2dd578320882675703f283b02d0dcc4e583106e775d788df29c535b49b` |

The current parent runtime hash `e455292b55d0443abb234a00506b9501b02f8c2a8df5afe298ff855f56cb406f` is parent-reported and outside this subagent's edited scope.
The parent's frozen probability/source-shape snapshots were not replaced.
The AST/byte preservation proof establishes unchanged authored weights and bounds, rather than native balance approval.
Removing inherited-break truncation can allow previously interrupted traversal to reach later entries, so runtime and probability acceptance remain parent-owned.

## Private loop manifest

Names use `<existing_helper>_loop_<ordinal>_break`.
All are unscoped temporary implementation controls, with `constant:acid_rain_runtime.zero` as their reset value.
Each reset is immediately before its loop in the same statement list, including repeated inner invocations.
No existing correctly bound loop was present to skip.
No intentional literal `break` writer or existing explicit stop binding was found in the owned before sources, so no gameplay stop consumer needed retargeting.
The source bodies were preserved without inventing early-exit behavior.

Line numbers in this table identify the frozen before source.

| File family | Existing helper | Ordinal | Loop kind | Before line | Private temporary |
| --- | --- | --- | --- | --- | --- |
| aftermath | `acid_rain_project_country_obligations` | 1 | `for_each_scope_loop` | 488 | `acid_rain_project_country_obligations_loop_1_break` |
| aftermath | `acid_rain_project_country_obligations` | 2 | `for_each_loop` | 492 | `acid_rain_project_country_obligations_loop_2_break` |
| aftermath | `acid_rain_country_water_context_changed` | 1 | `for_each_scope_loop` | 576 | `acid_rain_country_water_context_changed_loop_1_break` |
| aftermath | `acid_rain_refresh_active_consequences` | 1 | `for_each_scope_loop` | 585 | `acid_rain_refresh_active_consequences_loop_1_break` |
| aftermath | `acid_rain_refresh_active_consequences` | 2 | `for_each_scope_loop` | 586 | `acid_rain_refresh_active_consequences_loop_2_break` |
| achievement | `acid_rain_033_achievement_record_arrival` | 1 | `for_each_loop` | 1183 | `acid_rain_033_achievement_record_arrival_loop_1_break` |
| achievement | `acid_rain_033_achievement_record_severe_pulse` | 1 | `for_each_loop` | 1427 | `acid_rain_033_achievement_record_severe_pulse_loop_1_break` |
| achievement | `acid_rain_033_achievement_record_severe_protection` | 1 | `for_each_loop` | 1501 | `acid_rain_033_achievement_record_severe_protection_loop_1_break` |
| achievement | `acid_rain_033_achievement_record_severe_cell_closure` | 1 | `for_each_loop` | 1561 | `acid_rain_033_achievement_record_severe_cell_closure_loop_1_break` |
| achievement | `acid_rain_033_achievement_record_severe_cell_closure` | 2 | `for_each_loop` | 1592 | `acid_rain_033_achievement_record_severe_cell_closure_loop_2_break` |
| achievement | `acid_rain_033_achievement_settle_episode_evacuations` | 1 | `for_each_loop` | 2053 | `acid_rain_033_achievement_settle_episode_evacuations_loop_1_break` |
| achievement | `acid_rain_033_achievement_refresh_deadlines` | 1 | `for_each_scope_loop` | 2123 | `acid_rain_033_achievement_refresh_deadlines_loop_1_break` |
| achievement | `acid_rain_033_achievement_refresh_deadlines` | 2 | `for_each_scope_loop` | 2140 | `acid_rain_033_achievement_refresh_deadlines_loop_2_break` |
| achievement | `acid_rain_033_achievement_record_acute_closure` | 1 | `for_each_scope_loop` | 2202 | `acid_rain_033_achievement_record_acute_closure_loop_1_break` |
| achievement | `acid_rain_033_achievement_capture_action_start` | 1 | `for_each_scope_loop` | 2374 | `acid_rain_033_achievement_capture_action_start_loop_1_break` |
| achievement | `acid_rain_033_achievement_record_runtime_action` | 1 | `for_each_scope_loop` | 2416 | `acid_rain_033_achievement_record_runtime_action_loop_1_break` |
| achievement | `acid_rain_033_achievement_record_runtime_arrival` | 1 | `for_each_loop` | 2444 | `acid_rain_033_achievement_record_runtime_arrival_loop_1_break` |
| achievement | `acid_rain_033_achievement_schedule_deadline` | 1 | `for_each_scope_loop` | 2510 | `acid_rain_033_achievement_schedule_deadline_loop_1_break` |
| achievement | `acid_rain_033_achievement_schedule_deadline` | 2 | `for_each_scope_loop` | 2528 | `acid_rain_033_achievement_schedule_deadline_loop_2_break` |
| preparedness | `acid_rain_refresh_country_action_quotes` | 1 | `for_loop_effect` | 527 | `acid_rain_refresh_country_action_quotes_loop_1_break` |
| preparedness | `acid_rain_demobilize_emergency_apparatus` | 1 | `for_loop_effect` | 891 | `acid_rain_demobilize_emergency_apparatus_loop_1_break` |
| preparedness | `acid_rain_refresh_operation_state` | 1 | `for_loop_effect` | 974 | `acid_rain_refresh_operation_state_loop_1_break` |
| preparedness | `acid_rain_release_running_operations` | 1 | `for_loop_effect` | 1415 | `acid_rain_release_running_operations_loop_1_break` |
| preparedness | `acid_rain_release_running_operations` | 2 | `for_each_scope_loop` | 1433 | `acid_rain_release_running_operations_loop_2_break` |
| preparedness | `acid_rain_release_running_operations` | 3 | `for_each_scope_loop` | 1437 | `acid_rain_release_running_operations_loop_3_break` |
| preparedness | `acid_rain_cleanup_country_runtime` | 1 | `for_loop_effect` | 1488 | `acid_rain_cleanup_country_runtime_loop_1_break` |
| preparedness | `acid_rain_bind_operations_to_warning` | 1 | `for_loop_effect` | 1510 | `acid_rain_bind_operations_to_warning_loop_1_break` |
| preparedness | `acid_rain_bind_operations_to_warning` | 2 | `for_each_scope_loop` | 1526 | `acid_rain_bind_operations_to_warning_loop_2_break` |

The nested country-obligation loops use distinct ordinals one and two.
The active-consequence copy and reconciliation loops also use separate controls.
All six numerical loops retain their exact original `start`, `end`, `compare`, `add` and `value` arguments.
No source helper or public call site is added or renamed.
No global event target, flag lifecycle, source-retirement API or constant category is introduced.

## Tests run and what they execute

Run from the mod root:

```text
node .tools/validation/test_033_loop_break_owned_helpers.js
```

Before editing, `--before` verified all four raw current-source archives and reproduced inherited-default-break interruption in all 28 source loop envelopes.
After editing, the normal regression passed against the after hashes above, and it passed again after checkpoint resumption.
The test retains the archived before-source negative controls on every normal run.
The final numerical assertion checks the complete authored iteration sequence against an independent range-size formula, rather than accepting merely two visits.

| Evidence | Result |
| --- | --- |
| Exact-byte reconstruction and AST preservation | All four sources match the permitted before-to-after transformation, with CXT unchanged. |
| Archived before-source inherited `break = 1` negative controls | All 28 loop envelopes fail full traversal in the control model. |
| Actual-source private/default break stress and two repeated helper frames | 56 isolated source-envelope cases pass, with every private variable seeded to one and delegated nested helpers mutating the default break to one. |
| Actual nested obligation-loop pair with two outer objects and two inner receipts | Four unique inner visits occur, including resetting the inner private break again before the second outer invocation. |
| Foreach traversal over 1205 typed fixture objects | Both foreach kinds complete all 1205 visits on each of two invocations, for four repeated cases, with no invented foreach ceiling. |
| Unresolved observer receipt and retained suffix | The fixture retains 1204 unacknowledged entries after an intentional interruption, preserves that suffix on repeat, then records each eligible observer acknowledgment once when the synthetic blocked receipt becomes eligible. |
| Documented numerical cap controls | Synthetic for/while control cases stop at 1000, and a synthetic intentional private stop still stops after one iteration. |

The test parses the actual owned source and executes only the selected reset, break binding, and iterator envelope.
It uses separate temporary call frames, preserves caller-existing storage on helper return, and keeps typed fixture objects as objects rather than inventing numeric scope IDs.
The original gameplay bodies and their conditional gates are delegated observation boundaries.
They are not executed or replaced with successful famine, mortality, payment, receipt-settlement, building, callback or achievement implementations.
The nested traversal case extracts the actual loop pair and tests its control envelopes, without asserting that the surrounding gameplay eligibility tests succeed.
The suffix test's acknowledgments are synthetic observer bookkeeping, not actual Event033 receipt acceptance or population accounting.
There is no production queue-clear mutation in this patch, and byte/AST preservation independently verifies that all original queue/body statements are unchanged.
The test does not prove native ROOT/FROM authority, HOI4 variable arithmetic, actual state ownership, native foreach implementation details, save/reload, multiplayer or gameplay completion.

The fixture's break guard is a control-model interpretation of the documented nonzero termination rule.
The before result proves failure to complete the modelled traversal, not an observed native engine count before its first break check.
Numerical cap tests enforce the documented 1000 bound only for numerical loops.
The absence of a stated foreach ceiling in the cited sections is not presented as native evidence of unlimited foreach execution.
No game, model/debug launcher, log collection or new role was used.

## References and MCP evidence

Required guidance was read: `AGENTS.md`, `chaos-redux-events`, `chaos-redux-subagents`, and the complete `.agents\skills\chaos-redux-events\references\loop-break-isolation.md`.
The specific loop-isolation reference and the parent's explicit numerical-loop extension govern the distinction between foreach and numerical caps.
No skill was created or updated.

All domain calls used explicit workspace `mod_chaos_redux_ea3b2d67c2c0`.
The connected tool list exposed reference context/search/read, source lookup and `hoi4.script_validate`.
No separately named `validate_scope` route was exposed, so the available script validator was used with explicit effect kind and COUNTRY scope.
No helper expansion, job or native task was used, because version/health/client task negotiation was not independently established.

Live reference context reported omitted sources at its bound, so it was not used as complete rule coverage.
Targeted searches and revision-bound reads covered the relevant installed and offline loop sections.
Installed authority: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
The read sections are `for_each_loop:4279-4295`, `for_each_scope_loop:4296-4311`, `for_loop_effect:4312-4330`, and `while_loop_effect:8573-8587`.
Each documents default temporary `break` and nonzero termination, with foreach-scope traversal also documenting the element scope change.
Offline authority: `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md:1216-1220`, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
Those rows explicitly give the 1000 default bound for numerical loops and state no such bound in the foreach rows.
Temporary lifetime/unscoped storage is documented at lines 440-442 of the same snapshot.
The installed numerical define remains `common\defines\00_defines.lua:25`, `MAX_EFFECT_ITERATION = 1000`.
No Paradox web source was used.

Pre-change `hoi4.source_lookup` identified the unshadowed `acid_rain_project_country_obligations` definition at aftermath 483-527, workspace-index revision `c35170e8b2b7bedc5b62b31f3b165ce16665a771425b7b8746e62ffb2f1e8409`.
The bounded text returned through line 508 with a continuation, so no complete gameplay-body evidence was claimed from that read.
Post-change structure lookup identified the same unshadowed definition at 483-531, revision `ca6ddb815d70394ce8b27aeb1c14cf580f90603b348ed00cdcf5c272c9556275`.
It returned complete root child structure with no skipped source, showing the new reset at line 488 immediately before the outer loop at 489.
Definition structure is read-only source evidence, not native loop execution.
On resumption, a revision-bound child lookup returned `SOURCE_REVISION_STALE`, with current workspace index `e48072d49d9032bcd239a6c3e1f0b0b8b02741a1b9fdcf519630dc7a080b36f8`.
One fresh bounded lookup after that terminal response returned `timed out awaiting tools/call after 600s`.
That additional child-structure observation remains unavailable.
The previously returned root structure is retained with its own revision, and the four current file hashes still match the passing byte/AST checkpoint.
The stale index and timed-out lookup are not treated as evidence of changed owned source or as native validation.

Four loop-control snippets were checked through `hoi4.script_validate` under explicit COUNTRY effect scope.
All four returned `SCRIPT_CHECK_PARTIAL`, `valid = null`, `parametersChecked = false`, and `SCRIPT_ARGUMENT_BLOCK_UNCHECKED` for the reset and loop argument blocks.
Their performed checks were syntax, command kind and declared scope, with both commands supported under the cited documentation.
The documentation aggregate revision was `9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b`.
The source arrays, scalar parameters and nested gameplay bodies were not validated by those snippet results.
The detailed native argument syntax was read directly instead of claiming a successful full engine/scope validation.
The results returned no artifact URI.
The initial task routes returned results, while the resumed child lookup encountered the exact stale-index and terminal timeout limitations recorded above.
No broader service-health claim is inferred from these mixed observations.

## Reviewed exact source hunks

These are the reviewed source-only hunks for this tranche.
The frozen raw archives and recorded insertions in the test are the byte-level preservation authority.

```diff
diff --git a/common/scripted_effects/033_acid_rain_achievement_effects.txt b/common/scripted_effects/033_acid_rain_achievement_effects.txt
index 8dc2bfa9c..7c85620cc 100644
--- a/common/scripted_effects/033_acid_rain_achievement_effects.txt
+++ b/common/scripted_effects/033_acid_rain_achievement_effects.txt
@@ -1180,7 +1180,9 @@ acid_rain_033_achievement_record_arrival = {
 			set_temp_variable = { acid_rain_033_achievement_warning_match = @acid_rain_033_achievement_no_row }
 			if = {
 				limit = { has_variable = acid_rain_033_achievement_warning_visit_row_count }
+				set_temp_variable = { acid_rain_033_achievement_record_arrival_loop_1_break = constant:acid_rain_runtime.zero }
 				for_each_loop = {
+					break = acid_rain_033_achievement_record_arrival_loop_1_break
 					array = acid_rain_033_achievement_warning_visit_ids
 					index = acid_rain_033_achievement_warning_index
 					value = acid_rain_033_achievement_row_value
@@ -1424,7 +1426,9 @@ acid_rain_033_achievement_record_severe_pulse = {
 				set_temp_variable = { acid_rain_033_achievement_severe_pulse_row = @acid_rain_033_achievement_no_row }
 				if = {
 					limit = { has_variable = acid_rain_033_achievement_severe_target_row_count }
+					set_temp_variable = { acid_rain_033_achievement_record_severe_pulse_loop_1_break = constant:acid_rain_runtime.zero }
 					for_each_loop = {
+						break = acid_rain_033_achievement_record_severe_pulse_loop_1_break
 						array = acid_rain_033_achievement_severe_target_state_ids
 						index = acid_rain_033_achievement_severe_index
 						value = acid_rain_033_achievement_row_value
@@ -1498,7 +1502,9 @@ acid_rain_033_achievement_record_severe_protection = {
 				set_temp_variable = { acid_rain_033_achievement_protection_row = @acid_rain_033_achievement_no_row }
 				if = {
 					limit = { has_variable = acid_rain_033_achievement_severe_target_row_count }
+					set_temp_variable = { acid_rain_033_achievement_record_severe_protection_loop_1_break = constant:acid_rain_runtime.zero }
 					for_each_loop = {
+						break = acid_rain_033_achievement_record_severe_protection_loop_1_break
 						array = acid_rain_033_achievement_severe_target_state_ids
 						index = acid_rain_033_achievement_protection_index
 						value = acid_rain_033_achievement_row_value
@@ -1558,7 +1564,9 @@ acid_rain_033_achievement_record_severe_cell_closure = {
 			set_temp_variable = { acid_rain_033_achievement_episode_protection = @acid_rain_033_achievement_zero }
 			if = {
 				limit = { has_variable = acid_rain_033_achievement_severe_target_row_count }
+				set_temp_variable = { acid_rain_033_achievement_record_severe_cell_closure_loop_1_break = constant:acid_rain_runtime.zero }
 				for_each_loop = {
+					break = acid_rain_033_achievement_record_severe_cell_closure_loop_1_break
 					array = acid_rain_033_achievement_severe_target_state_ids
 					index = acid_rain_033_achievement_episode_index
 					value = acid_rain_033_achievement_row_value
@@ -1589,7 +1597,9 @@ acid_rain_033_achievement_record_severe_cell_closure = {
 			set_temp_variable = { acid_rain_033_achievement_episode_row = @acid_rain_033_achievement_no_row }
 			if = {
 				limit = { has_variable = acid_rain_033_achievement_severe_episode_row_count }
+				set_temp_variable = { acid_rain_033_achievement_record_severe_cell_closure_loop_2_break = constant:acid_rain_runtime.zero }
 				for_each_loop = {
+					break = acid_rain_033_achievement_record_severe_cell_closure_loop_2_break
 					array = acid_rain_033_achievement_severe_episode_ids
 					index = acid_rain_033_achievement_episode_summary_index
 					value = acid_rain_033_achievement_row_value
@@ -2050,7 +2060,9 @@ acid_rain_033_achievement_close_runtime_episode = {
 # COUNTRY SCOPE. Inspect the frozen evacuation rows for the episode just closed.
 # Threshold zero records a missing design input and cannot produce an award.
 acid_rain_033_achievement_settle_episode_evacuations = {
+	set_temp_variable = { acid_rain_033_achievement_settle_episode_evacuations_loop_1_break = constant:acid_rain_runtime.zero }
 	for_each_loop = {
+		break = acid_rain_033_achievement_settle_episode_evacuations_loop_1_break
 		array = acid_rain_033_achievement_evacuation_state_scopes
 		value = acid_rain_033_achievement_evacuation_scope
 		index = acid_rain_033_achievement_evacuation_index
@@ -2120,7 +2132,9 @@ acid_rain_033_achievement_refresh_deadlines = {
 		limit = { acid_rain_033_achievement_generation_is_current = yes }
 	set_variable = { acid_rain_033_achievement_recovery_resolved_count = @acid_rain_033_achievement_zero }
 	set_variable = { acid_rain_033_achievement_tier3_resolved_count = @acid_rain_033_achievement_zero }
+	set_temp_variable = { acid_rain_033_achievement_refresh_deadlines_loop_1_break = constant:acid_rain_runtime.zero }
 	for_each_scope_loop = {
+		break = acid_rain_033_achievement_refresh_deadlines_loop_1_break
 		array = acid_rain_033_achievement_recovery_state_scopes
 		if = {
 			limit = {
@@ -2137,7 +2151,9 @@ acid_rain_033_achievement_refresh_deadlines = {
 			}
 		}
 	}
+	set_temp_variable = { acid_rain_033_achievement_refresh_deadlines_loop_2_break = constant:acid_rain_runtime.zero }
 	for_each_scope_loop = {
+		break = acid_rain_033_achievement_refresh_deadlines_loop_2_break
 		array = acid_rain_033_achievement_tier3_state_scopes
 		if = {
 			limit = {
@@ -2199,7 +2215,9 @@ acid_rain_033_achievement_record_acute_closure = {
 		divide_variable = { acid_rain_033_achievement_closure_death_ceiling = @acid_rain_033_achievement_five_state_death_denominator }
 		multiply_variable = { acid_rain_033_achievement_closure_death_ceiling = @acid_rain_033_achievement_five_state_death_numerator }
 		set_variable = { acid_rain_033_achievement_closure_tier3_count = @acid_rain_033_achievement_zero }
+		set_temp_variable = { acid_rain_033_achievement_record_acute_closure_loop_1_break = constant:acid_rain_runtime.zero }
 		for_each_scope_loop = {
+			break = acid_rain_033_achievement_record_acute_closure_loop_1_break
 			array = acid_rain_033_achievement_responsible_states
 			if = { limit = { check_variable = { var = acid_rain_state_aftermath_tier value = @acid_rain_033_achievement_tier3 compare = greater_than_or_equals } } add_to_variable = { PREV.acid_rain_033_achievement_closure_tier3_count = @acid_rain_033_achievement_one } }
 		}
@@ -2371,7 +2389,9 @@ acid_rain_033_achievement_capture_action_start = {
 	set_variable = { acid_rain_033_achievement_active_action_visit = @acid_rain_033_achievement_zero }
 	if = {
 		limit = { check_variable = { var = acid_rain_selected_action value = constant:acid_rain_action.recovery_transport compare = less_than } }
+		set_temp_variable = { acid_rain_033_achievement_capture_action_start_loop_1_break = constant:acid_rain_runtime.zero }
 		for_each_scope_loop = {
+			break = acid_rain_033_achievement_capture_action_start_loop_1_break
 			array = acid_rain_033_achievement_responsible_states
 			if = {
 				limit = { has_state_flag = acid_rain_warning_pending check_variable = { var = PREV.acid_rain_033_achievement_active_action_visit value = @acid_rain_033_achievement_zero compare = equals } }
@@ -2413,7 +2433,9 @@ acid_rain_033_achievement_record_runtime_action = {
 	}
 	if = {
 		limit = { check_variable = { var = acid_rain_selected_action value = constant:acid_rain_action.urgent_shelter compare = equals } }
+		set_temp_variable = { acid_rain_033_achievement_record_runtime_action_loop_1_break = constant:acid_rain_runtime.zero }
 		for_each_scope_loop = {
+			break = acid_rain_033_achievement_record_runtime_action_loop_1_break
 			array = acid_rain_033_achievement_responsible_states
 			if = {
 				limit = { OR = { has_state_flag = acid_rain_severe_cell_target has_state_flag = acid_rain_superstorm_target } }
@@ -2441,7 +2463,9 @@ acid_rain_033_achievement_record_runtime_arrival = {
 	set_temp_variable = { acid_rain_033_input_arrival_day = global.date }
 	CONTROLLER = {
 		acid_rain_033_achievement_record_arrival = yes
+		set_temp_variable = { acid_rain_033_achievement_record_runtime_arrival_loop_1_break = constant:acid_rain_runtime.zero }
 		for_each_loop = {
+			break = acid_rain_033_achievement_record_runtime_arrival_loop_1_break
 			array = acid_rain_033_achievement_pending_action_keys
 			value = acid_rain_033_pending_action_key
 			index = acid_rain_033_pending_action_index
@@ -2507,7 +2531,9 @@ acid_rain_033_achievement_record_runtime_evacuation_completion = {
 # Tier-3 downgrade must precede day 180 and is audited on day 180 itself.
 acid_rain_033_achievement_schedule_deadline = {
 	set_temp_variable = { acid_rain_033_deadline_candidate = @acid_rain_033_achievement_zero }
+	set_temp_variable = { acid_rain_033_achievement_schedule_deadline_loop_1_break = constant:acid_rain_runtime.zero }
 	for_each_scope_loop = {
+		break = acid_rain_033_achievement_schedule_deadline_loop_1_break
 		array = acid_rain_033_achievement_recovery_state_scopes
 		if = {
 			limit = { NOT = { has_state_flag = acid_rain_033_achievement_state_recovery_resolved } }
@@ -2525,7 +2551,9 @@ acid_rain_033_achievement_schedule_deadline = {
 			}
 		}
 	}
+	set_temp_variable = { acid_rain_033_achievement_schedule_deadline_loop_2_break = constant:acid_rain_runtime.zero }
 	for_each_scope_loop = {
+		break = acid_rain_033_achievement_schedule_deadline_loop_2_break
 		array = acid_rain_033_achievement_tier3_state_scopes
 		if = {
 			limit = {
diff --git a/common/scripted_effects/033_acid_rain_aftermath_effects.txt b/common/scripted_effects/033_acid_rain_aftermath_effects.txt
index b4df5af5d..4903c6c82 100644
--- a/common/scripted_effects/033_acid_rain_aftermath_effects.txt
+++ b/common/scripted_effects/033_acid_rain_aftermath_effects.txt
@@ -485,11 +485,15 @@ acid_rain_project_country_obligations = {
 	set_variable = { acid_rain_033_achievement_tier3_row_count = constant:acid_rain_aftermath.zero }
 	set_variable = { acid_rain_033_achievement_tier3_resolved_count = constant:acid_rain_aftermath.zero }
 	set_temp_variable = { acid_rain_next_obligation_deadline = constant:acid_rain_aftermath.zero }
+	set_temp_variable = { acid_rain_project_country_obligations_loop_1_break = constant:acid_rain_runtime.zero }
 	for_each_scope_loop = {
+		break = acid_rain_project_country_obligations_loop_1_break
 		array = acid_rain_tier3_history_states
 		if = {
 			limit = { check_variable = { var = acid_rain_consequence_generation value = global.acid_rain_generation_id compare = equals } }
+			set_temp_variable = { acid_rain_project_country_obligations_loop_2_break = constant:acid_rain_runtime.zero }
 			for_each_loop = {
+				break = acid_rain_project_country_obligations_loop_2_break
 				array = acid_rain_tier3_entry_days
 				index = acid_rain_obligation_row
 				value = acid_rain_obligation_entry_day
@@ -573,7 +577,9 @@ acid_rain_record_paid_recovery_consequence = {
 
 # COUNTRY SCOPE. Exact project/action completion hook, with unchanged payment.
 acid_rain_country_water_context_changed = {
+	set_temp_variable = { acid_rain_country_water_context_changed_loop_1_break = constant:acid_rain_runtime.zero }
 	for_each_scope_loop = {
+		break = acid_rain_country_water_context_changed_loop_1_break
 		array = acid_rain_033_achievement_responsible_states
 		if = { limit = { check_variable = { var = acid_rain_consequence_generation value = global.acid_rain_generation_id compare = equals } } acid_rain_reconcile_state_consequences = yes }
 	}
@@ -582,8 +588,10 @@ acid_rain_country_water_context_changed = {
 # Host checks only the current union footprint. Copy before removing any members.
 acid_rain_refresh_active_consequences = {
 	clear_temp_array = acid_rain_active_consequence_snapshot
-	for_each_scope_loop = { array = global.acid_rain_active_consequence_states add_to_temp_array = { array = acid_rain_active_consequence_snapshot value = THIS } }
-	for_each_scope_loop = { array = acid_rain_active_consequence_snapshot acid_rain_reconcile_state_consequences = yes }
+	set_temp_variable = { acid_rain_refresh_active_consequences_loop_1_break = constant:acid_rain_runtime.zero }
+	for_each_scope_loop = { break = acid_rain_refresh_active_consequences_loop_1_break array = global.acid_rain_active_consequence_states add_to_temp_array = { array = acid_rain_active_consequence_snapshot value = THIS } }
+	set_temp_variable = { acid_rain_refresh_active_consequences_loop_2_break = constant:acid_rain_runtime.zero }
+	for_each_scope_loop = { break = acid_rain_refresh_active_consequences_loop_2_break array = acid_rain_active_consequence_snapshot acid_rain_reconcile_state_consequences = yes }
 }
 
 # One state transaction: advance the preceding interval before sampling replacements.
diff --git a/common/scripted_effects/033_acid_rain_preparedness_effects.txt b/common/scripted_effects/033_acid_rain_preparedness_effects.txt
index dc51c05cd..4a5f76c84 100644
--- a/common/scripted_effects/033_acid_rain_preparedness_effects.txt
+++ b/common/scripted_effects/033_acid_rain_preparedness_effects.txt
@@ -524,7 +524,9 @@ acid_rain_refresh_country_action_quotes = {
 	set_temp_variable = { acid_rain_component_quote = constant:acid_rain_runtime.zero }
 
 	set_temp_variable = { acid_rain_action_quote_loop_end = constant:acid_rain_runtime.action_loop_end }
+	set_temp_variable = { acid_rain_refresh_country_action_quotes_loop_1_break = constant:acid_rain_runtime.zero }
 	for_loop_effect = {
+		break = acid_rain_refresh_country_action_quotes_loop_1_break
 		start = constant:acid_rain_runtime.one
 		end = acid_rain_action_quote_loop_end
 		value = acid_rain_action_quote_index
@@ -888,7 +890,9 @@ acid_rain_cancel_project = {
 # grants a bounded repair-speed bonus while the crews return to normal work.
 # Consumed equipment and political power remain spent.
 acid_rain_demobilize_emergency_apparatus = {
+	set_temp_variable = { acid_rain_demobilize_emergency_apparatus_loop_1_break = constant:acid_rain_runtime.zero }
 	for_loop_effect = {
+		break = acid_rain_demobilize_emergency_apparatus_loop_1_break
 		start = constant:acid_rain_runtime.one
 		end = constant:acid_rain_runtime.five
 		value = acid_rain_demobilize_project_index
@@ -971,7 +975,9 @@ acid_rain_resolve_operation_family = {
 acid_rain_refresh_operation_state = {
 	set_temp_variable = { acid_rain_running_operations = acid_rain_evacuations_active }
 	add_to_temp_variable = { acid_rain_running_operations = acid_rain_recovery_ops_active }
+	set_temp_variable = { acid_rain_refresh_operation_state_loop_1_break = constant:acid_rain_runtime.zero }
 	for_loop_effect = {
+		break = acid_rain_refresh_operation_state_loop_1_break
 		start = constant:acid_rain_runtime.one
 		end = constant:acid_rain_action.family_rows
 		value = acid_rain_op_scan_family
@@ -1412,7 +1418,9 @@ acid_rain_release_state_operation = {
 # power stay spent. Input: temporary acid_rain_keep_recovery_operations, one
 # to keep recovery work and demobilization running through acute dissipation.
 acid_rain_release_running_operations = {
+	set_temp_variable = { acid_rain_release_running_operations_loop_1_break = constant:acid_rain_runtime.zero }
 	for_loop_effect = {
+		break = acid_rain_release_running_operations_loop_1_break
 		start = constant:acid_rain_runtime.one
 		end = constant:acid_rain_action.family_rows
 		value = acid_rain_op_release_family
@@ -1430,11 +1438,15 @@ acid_rain_release_running_operations = {
 		}
 	}
 	clear_temp_array = acid_rain_op_release_states
+	set_temp_variable = { acid_rain_release_running_operations_loop_2_break = constant:acid_rain_runtime.zero }
 	for_each_scope_loop = {
+		break = acid_rain_release_running_operations_loop_2_break
 		array = acid_rain_op_states
 		add_to_temp_array = { array = acid_rain_op_release_states value = THIS }
 	}
+	set_temp_variable = { acid_rain_release_running_operations_loop_3_break = constant:acid_rain_runtime.zero }
 	for_each_scope_loop = {
+		break = acid_rain_release_running_operations_loop_3_break
 		array = acid_rain_op_release_states
 		if = {
 			limit = {
@@ -1485,7 +1497,9 @@ acid_rain_cleanup_country_runtime = {
 	if = { limit = { exists = no } acid_rain_033_achievement_mark_country_ceased = yes }
 	set_temp_variable = { acid_rain_keep_recovery_operations = constant:acid_rain_runtime.zero }
 	acid_rain_release_running_operations = yes
+	set_temp_variable = { acid_rain_cleanup_country_runtime_loop_1_break = constant:acid_rain_runtime.zero }
 	for_loop_effect = {
+		break = acid_rain_cleanup_country_runtime_loop_1_break
 		start = constant:acid_rain_runtime.one
 		end = constant:acid_rain_runtime.five
 		value = acid_rain_cleanup_project_index
@@ -1507,7 +1521,9 @@ acid_rain_cleanup_country_runtime = {
 # so an action started before a warning can still be credited for finishing
 # before that warning's arrival. Each operation binds to at most one visit.
 acid_rain_bind_operations_to_warning = {
+	set_temp_variable = { acid_rain_bind_operations_to_warning_loop_1_break = constant:acid_rain_runtime.zero }
 	for_loop_effect = {
+		break = acid_rain_bind_operations_to_warning_loop_1_break
 		start = constant:acid_rain_runtime.one
 		end = constant:acid_rain_action.family_demobilize
 		value = acid_rain_op_bind_family
@@ -1523,7 +1539,9 @@ acid_rain_bind_operations_to_warning = {
 			set_variable = { acid_rain_op_warning_day_entries^acid_rain_op_bind_family = acid_rain_033_input_warning_day }
 		}
 	}
+	set_temp_variable = { acid_rain_bind_operations_to_warning_loop_2_break = constant:acid_rain_runtime.zero }
 	for_each_scope_loop = {
+		break = acid_rain_bind_operations_to_warning_loop_2_break
 		array = acid_rain_op_states
 		if = {
 			limit = {
```

## Completion boundary and parent follow-up

Completed: private reset/binding repair for every actual loop in the four authorized sources, exact before-byte/hunk preservation, all-source AST checks, the repeat/nesting/large-foreach/numerical-cap control regression, and this handoff.
Skipped because there was nothing to change: CXT and owned while loops, with their zero inventory verified.
No existing source intentional stop was removed or redirected.
No simplification, fallback, body rewrite, new grant hook or queue clearing was implemented.

Remaining: native execution and scope/argument behavior, actual gameplay-body outcomes, full lifecycle/receipt accounting, and any parent/auditor probability comparison.
The parent's runtime source, frozen AA/source-shape evidence and UI worker's loop/visual work remain outside this patch.
Recheck the after hashes before final parent integration in the shared checkout.
Native/source-wide Event033 goals remain pending, and this handoff makes no full Event033 completion claim.

Changed files in this tranche are exactly the three effect files, the owned test and this handoff.
The fourth source file was reviewed and is unchanged.
No commit, backend, game, log, cost/AI/weight, workbook, asset or shared-helper write was made.

## Parent integration review, 2026-10-08

The parent reviewed the complete owned source diff and executable test logic, reran all twenty-eight frozen negative controls and fifty-six repeat-frame cases, and confirmed exact byte/AST preservation.
Only an extra blank line at the test's end was removed before staging, without changing its embedded before archives or executable logic.
The resulting reviewed test SHA-256 is `df694af8562ea3723061ebf03434025c433d465b336a3a1cfb462416b17eaba1`, while the producer's earlier hash above remains historical.
The parent runtime has since received the independent log-context repair and is `94c0c9d3c8b8b63f57878033648bb71b1f34ac89739d279a299ec3f163c1a510`.
The three delivered helper hashes are unchanged by parent integration.
The exact current test output is retained in `../validation/owned_loop_parent_review_2026_10_08.json` and no native, financial, Humanitarian or full-event gate is promoted by this review.
