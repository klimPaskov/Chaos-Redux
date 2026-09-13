# Event 032 helper parser analysis

## Status

This is a read-only startup diagnosis for the Event 032 launch08 error batch dated 2026-09-04.

No gameplay source, weights, decisions, missions, assets, or event behavior were edited, staged, or committed.

The analysis is bounded to scripted helper registration and parser/reference errors in Event 032.

## Evidence and limits

The primary runtime evidence is docs/testing/live_qa/2026-09-04_catalog_01/logs/launch_08/logs/error.log.

The relevant source files are common/scripted_effects/032_missiles_operations_effects.txt, common/scripted_effects/032_missiles_scenario_effects.txt, common/scripted_effects/032_missiles_effects.txt, and common/scripted_triggers/032_missiles_operations_triggers.txt.

The required offline references were consulted in paradox_wiki/Effects - Hearts of Iron 4 Wiki.md, paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md, paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md, and paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md.

The installed vanilla references were consulted in C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md and C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md, together with vanilla scripted effect and trigger precedents.

The required narrow Event MCP inspection for chaosx.nr32.1 completed with EVENT_INSPECTED_PARTIAL at revision 1102e50fad94d2051bd32d8a7cd64c3429a191f53e98c50d02aeb60327e1dae8 and graph hash c6850dd8ad35035c9a83ff251c3df14e4e6123af303e2037d032ccbf5ea51b2e.

The inspection artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/da3ce893013911af3232361c4111ad6e8014fadd10b075d1ed3c4c7f70ab30f2/29fca77dadd2f93ac447d10ed17cc4629ab5523ed09b0e137b25d3569abae434/event-lint-1102e50fad94.json.

The read-only Event MCP overview render completed with EVENT_RENDERED_PARTIAL, layout hash d7e6211224e43181c240a4dc3a8a4a42912b53949c2cea32d53c09858b85164a, and artifact references hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/08d0267a6cae191c50ea8746cbf14e191281f0dd449ef512e221de2288349513/4ff080a6c6ab3afbbf7b1186530827e8c08a2e92f3017b584bcf849dc0964698/event-overview-1102e50fad94.json and hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/91e26006b8a8434beb33ab15ad166649dea05c8461dc98ba13608a1fb8d91d94/100138f052ba4d9b9ae4f05dbab735b72cc09203be0c2ee44448bf31a43e7a30/event-overview-1102e50fad94.svg.

Both MCP results are partial because helper expansion was disabled and the inline source inventory was truncated to 64 of 369 files, so they do not certify scripted helper registration.

An Event MCP compare request against the same before and after revision was blocked by EVENT_REVISION_NOT_CACHED; no compare artifact was produced.

## Root cause: one missing brace hides the operations declarations

common/scripted_effects/032_missiles_operations_effects.txt uses the valid top-level scripted-effect form described by the offline Effects page at lines 1270-1282, so the absence of a scripted_effects wrapper is not the cause.

A comment-aware brace scan finds the file ending at depth 1.

The first structural loss is inside missiles_score_target_country_candidate at source line 1634.

The limit block opened there contains ROOT = { ... } and any_controlled_state = { ... }, but it is not closed before add_to_temp_variable at line 1642.

The exact minimum parser repair is one closing brace immediately after current line 1641 and before add_to_temp_variable = { missiles_target_candidate_score = constant:missiles_target_score.strategic_depth }.

That brace closes the limit block while the existing line 1643 closes the surrounding if, and the existing line 1659 closes missiles_score_target_country_candidate.

This is a one-token structural repair that preserves every value, effect, trigger, and score weight.

The static declaration scan finds 62 valid root definitions before this point and 167 helper-shaped declarations in the file overall.

With that single brace restored, all 167 declarations return to root scope and the file balances at depth 0.

The launch08 Invalid effect and unknown-helper block beginning around log lines 2069-2278 is therefore a registration cascade.

The affected helpers are physically present later in the same file, including selection, preparation, payload dispatch, incident, retaliation, resolution, inheritance, site, and compatibility aliases.

The Event 032 event and scenario unknown-helper messages at log lines 2304-2307, 2348-2349, and 2862-2865 are downstream symptoms of the same hidden declarations.

## True registration/type mismatch

missiles_can_pay_reserve is defined at common/scripted_effects/032_missiles_operations_effects.txt:784, but its body consists entirely of trigger clauses:

    missiles_can_pay_reserve = {
    	has_variable = missiles_reserve_payment_request
    	check_variable = { var = missiles_reserve_payment_request value = constant:missiles_program_value.zero compare = greater_than }
    	check_variable = { var = missiles_operational_reserve value = missiles_reserve_payment_request compare = greater_than_or_equals }
    }

Its only custom consumer is a limit at common/scripted_effects/032_missiles_operations_effects.txt:2204.

The exact behavior-preserving migration is to move this unchanged definition from the scripted-effects file to common/scripted_triggers/032_missiles_operations_triggers.txt.

The identifier and all three trigger clauses remain unchanged, and no reserve value or default is introduced.

This is independent of the missing brace because the helper is in the wrong registry even after the operations file balances.

## Scenario file: independent parser and reference defects

common/scripted_effects/032_missiles_scenario_effects.txt is balanced at depth 0 and has no wrapper defect.

The following proposals preserve existing constants, comparisons, targets, flags, and effects.

| Source | Current token or form | Exact parser/reference proposal |
| --- | --- | --- |
| line 283 | is_at_war = yes | Use the documented trigger has_war = yes. |
| lines 287, 316, 682 | has_global_event_target = ... | Use has_event_target = ...; retain the existing target names. |
| lines 483, 501, 526, 629 | check_variable = { global.<name> value = ... compare = greater_than } | Add the required long-form selector: check_variable = { var = global.<name> value = ... compare = greater_than }. |
| line 496 | ROOT.global.missiles_scenario_command_damage | Use global.missiles_scenario_command_damage; the ROOT. prefix is invalid for this global variable reference. |
| line 691 | clear_event_target = missiles_scenario_warning_recipient | Remove the unsupported clear operation. The target was created with save_event_target_as at line 546 and regular event targets auto-clear when the originating effect chain ends. Do not replace it with a global clear. |

The first scenario unknown-helper messages for missiles_allocate_incident_id at line 532, missiles_initialize_root_incident at line 538, and missiles_close_root_incident at line 684 are cascades from the operations registration loss, not absent mechanics.

missiles_scenario_warning_root is saved globally by the scenario code, so the operations cleanup at common/scripted_effects/032_missiles_operations_effects.txt:4241 should use has_event_target = missiles_scenario_warning_root while retaining clear_global_event_target = missiles_scenario_warning_root.

## Unsupported temporary-variable cleanup

clear_temp_variable appears throughout the operations, scenario, and core Event 032 effect files.

The installed vanilla effects documentation contains clear_temp_array but no clear_temp_variable, and no vanilla precedent for that effect was found.

These errors are independent parser failures and are not the cause of the hidden helper declarations.

A blanket replacement with clear_variable is unsafe because the Data structures page distinguishes temporary variables from persistent scoped variables.

Each occurrence needs an owner-reviewed decision about whether removing the unsupported cleanup is safe after checking same-block reuse; no blanket migration is proposed here.

## Direct core-effects finding

common/scripted_effects/032_missiles_effects.txt:944 and :948 use check_variable directly as the body of else_if effect blocks.

The documented effect structure requires the trigger in limit = { ... } and the increment as the effect body.

The exact local parser proposal is to wrap each existing check_variable clause in limit = { ... } and leave its existing add_to_variable effect unchanged.

This finding is separate from helper registration and was not edited.

## Definition and consumer spot checks

The following declarations exist in the operations file and become registered once the missing brace is restored.

| Helper | Definition | Representative consumer(s) |
| --- | --- | --- |
| missiles_allocate_incident_id | operations line 3685 | operations line 260 and scenario line 532 |
| missiles_prepare_operation | operations line 2266 | operations lines 1185, 2274, 2280, 2286, 2292, and 4211 |
| missiles_initialize_root_incident | operations line 3749 | operations line 3783 and scenario line 538 |
| missiles_set_retaliation_posture_off | operations line 3915 | events/032_missile_crisis.txt:220 |
| missiles_set_retaliation_posture_supervised | operations line 3924 | events/032_missile_crisis.txt:226 |
| missiles_close_root_incident | operations line 4224 | scenario line 684 and events/032_missile_crisis.txt:393 |
| missiles_commit_operation | operations line 4283 | Event 032 operation resolution consumers |
| missiles_abort_operation | operations line 4301 | Event 032 operation failure consumers |
| missiles_cleanup_operation | operations line 4312 | Event 032 operation cleanup consumers |
| missiles_grant_next_technology_step | operations line 5158 | compatibility alias consumers |
| missiles_build_site_candidate_pool | operations line 5162 | compatibility alias consumers |
| missiles_select_site | operations line 5166 | compatibility alias consumers |
| missiles_create_site | operations line 5170 | compatibility alias consumers |
| missiles_upgrade_site | operations line 5174 | compatibility alias consumers |
| missiles_damage_site | operations line 5178 | compatibility alias consumers |

A source-wide Event 032 assignment-style scan found no other genuinely absent custom missiles_* effect or trigger definition after accounting for the operations registration loss.

The sole true helper registry mismatch identified in this bounded pass is missiles_can_pay_reserve.

## Classification and owner boundary

The primary root cause is the missing closing brace in missiles_score_target_country_candidate.

The large unknown-helper block is a cascade caused by that brace and does not justify adding replacement mechanics or defaults.

The reserve helper is a true type mismatch and needs an unchanged move to the operations trigger file.

The scenario aliases, malformed check_variable forms, invalid global variable scope, unsupported event-target clear, and unsupported temporary-variable cleanup are independent parser issues to apply in a coordinated parser pass.

The common/decisions/032_missiles_decisions.txt and common/decisions/032_missiles_missions.txt surfaces remain with the decision worker and were not changed.

No edits were made to the parent-owned Event 024 effect file or to any concurrent Event 032 gameplay file.

## Recommended repair order

1. Apply the single brace insertion after operations source line 1641, with a diff guard around the surrounding block.
2. Move the unchanged missiles_can_pay_reserve block to the operations scripted-trigger file; this is completed in the registry repair addendum below.
3. Apply the documented scenario token repairs and the ROOT.global correction.
4. Review each clear_temp_variable occurrence by scope and lifetime instead of changing it mechanically.
5. Repair the two else_if limit wrappers in 032_missiles_effects.txt.
6. Rerun the startup parser and classify the next log batch after the registration cascade is removed.

## Simplifications, omissions, and blockers

No missing mechanics, defaults, gameplay values, weights, assets, or event options were authored.

The original diagnosis phase was read-only; the registry repair addendum below records the only source change in this task.

The Event MCP compare route was unavailable because the requested revision was not cached, so no before-and-after graph comparison is claimed.

The MCP inspect and render routes were partial and helper expansion was disabled, so source inspection and launch08 log evidence remain the authority for this parser diagnosis.

The unsupported clear_temp_variable family remains unresolved pending owner review of temporary-variable lifetime.

## Handoff

Parent review should use the one-brace insertion as the minimum Event 032 helper parser repair and preserve all existing helper bodies and values.

After that repair, a fresh parser log is required to distinguish the independent scenario and core-effects syntax errors from any newly exposed issues.

## Registry repair addendum

Date: 2026-09-05.

Parent authorization covered only the independent registry repair for missiles_can_pay_reserve.

Exact pre-edit bytes for both immediate source files were archived under docs/testing/live_qa/2026-09-04_catalog_01/pre_patch_event32_registry/ before the move.

| Source | Archived SHA-256 | Post-move SHA-256 | Byte delta |
| --- | --- | --- | --- |
| common/scripted_effects/032_missiles_operations_effects.txt | 76FC77FC600B68B78062851488090CB41F1F7D758AE3820A33A5D261ED5B0812 | FAE1419206A62C6C89559A2383115ECA1961CEF26E33960A8956A544AE670FCD | -341 |
| common/scripted_triggers/032_missiles_operations_triggers.txt | 2BE33F272B14C703BD8965F1DF308C28B4017CCBEE9CBCB99139D6D47A5EF518 | CA234711E3A6146260E2A1A312E34D9867D197AA573C222D3091BA9C45C5FBAB | +341 |

The 340-byte definition body was removed from common/scripted_effects/032_missiles_operations_effects.txt and inserted unchanged before missiles_operation_can_be_committed at trigger source line 87.

A byte-equivalent relocation check reconstructed both post-move files from the archived originals and the exact body move, with no other source bytes changed.

The effects file now has zero definitions for missiles_can_pay_reserve, the triggers file has exactly one definition at line 81, and the sole runtime caller remains the existing trigger-limit call at common/scripted_effects/032_missiles_operations_effects.txt:2198.

No missing-brace repair, scenario edit, clear_event_target deletion, temporary-variable cleanup, effect keyword change, or gameplay/default change was made in this tranche.

The source move is ready for the parent-owned launch09 parser check. No further gameplay source writes are planned from this subtask.
