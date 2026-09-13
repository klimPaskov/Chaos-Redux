# CXT activation technology investigation

Disposition: implemented source change, runtime repair outcome unresolved.
The parent approved replacing `for_each_loop` value delivery with explicit bounded indexed database reads after the first investigation findings.
The source change preserves the full installed runtime inventory contract and native consumers; it does not establish the identity of the original rejected value or prove the runtime error is eliminated.

## New supplied evidence

Only `C:/Users/klimp/.codex/attachments/aa8d53ed-2c45-4e89-a77c-e821e9e4a388/pasted-text.txt` was read for this follow-up's runtime evidence.
It contains a `has_tech: Invalid tech` and `set_technology: Invalid tech` pair at 1936.01.01.12, a second pair at the same history timestamp, and another pair at receiver activation 1936.01.01.13.
It contains no `CXT_TECH_DIAGNOSTIC` values.
The pairs do not identify how many distinct database elements fail or the failing element's index, value, or identity.
Activation-time recurrence excludes removing or deferring the history calls as a complete repair.
No other game logs were sought or requested.

## Supported syntax versus unresolved representation

Installed `documentation/dynamic_variables_documentation.md:1048-1049` describes GLOBAL `technology` as an array of objects in the technology database.
Its country `researched_techs` entry at line 767 describes the researched technology array.
Installed `documentation/effects_documentation.md:4279-4294` establishes that `for_each_loop` delivers the selected array element into the named temporary `value` variable and the index into the named temporary `index` variable.
It does not establish the representation, validity, or token flag of each database array element.

Installed `documentation/effects_documentation.md:7805-7818` documents `set_technology` with technology IDs as keys and `popup = no`.
Installed `documentation/triggers_documentation.md:4882-4889` documents country-scope `has_tech`.
Actual approved Kaiserreich `common/scripted_effects/00_transfer_technology_effects.txt:652-695` loops `PREV.researched_techs` into temporary `technology`, tests `has_tech = var:technology`, and grants `set_technology = { var:technology = 1 popup = no }`.
This establishes a real native consumer precedent for researched technologies, not a safe conversion of the unidentified rejected entry in GLOBAL `technology`.
The existing shared repository union helper follows this researched-array pattern.

The offline Data structures token and array sections, Technology modding page, installed dynamic variables, effects, triggers, script concepts, and relevant actual vanilla technology definitions and silent research precedent were previously consulted and rechecked where relevant.
Installed script concept and dynamic variable documentation provides no documented typed technology-object-to-token conversion.
The offline statement that technology names are tokenizable is insufficient to establish that every database array value already has the token flag or how to reconstruct its name.
Returning to `GetTokenKey` interpolation would reproduce the previously rejected malformed meta path without new evidence.

Installed `documentation/triggers_documentation.md:5006-5013` says `has_variable` checks variable existence, not database object validity.
No installed documented technology validity trigger was found.
Neither a zero-value guard nor a variable-existence guard proves that no actual technology is excluded.
No sentinel meaning or type filter was invented.

The installed effect reference exposes `set_technology`, `inherit_technology`, research bonuses, and layout effects, but no documented effect to grant every technology directly.
`inherit_technology` inherits another country's technology and cannot establish complete installed inventory without a donor that already has the same unresolved full-grant requirement.
The earlier read-only definition audit found 679 valid named technology blocks across 12 mod and 13 vanilla files, matching the MCP source count.
There is no source evidence supporting technology-definition edits.

## Exact unresolved issue and preserved contract

At least one selected runtime value is rejected by the native country technology consumers, despite the engine documentation exposing the source database array.
The available evidence cannot distinguish an invalid database entry from a database object representation unsupported by those consumers, and cannot establish a lossless conversion or validity guard.
This uncertainty affects the complete dynamic inventory requirement directly.
A static generated list, researched-donor-only replacement, skipped history lifecycle, guessed null filter, or silently omitted technology would weaken that requirement and is not implemented.

Helper `chaosx_test_country_complete_all_technologies` remains country-scoped and runtime-driven over every `global.technology` element, with `popup = no`, the existing `has_tech` idempotence check, and existing conditional layout refresh.
History receipts, the two history preunlock calls, receiver activation, registered extensions, and all call sites remain unchanged by this worker.
No constants, flags, persistent variables, event targets, tuning, assets, localisation, or cleanup changes were introduced.
The helper captures `global.technology^num` in temporary `chaosx_test_country_technology_count`, initializes a dedicated temporary `chaosx_test_country_technology_loop_break` to zero, and loops index zero up to the count with `compare = less_than`.
Each iteration explicitly assigns `global.technology^chaosx_test_country_current_technology_index` to temporary `chaosx_test_country_current_technology` before the unchanged native technology consumers.
It does not depend on `for_each_loop` value delivery or its inherited default break variable.
An empty array produces no element reads or consumer calls.
There is no token-value filter, inferred sentinel, generated inventory, omitted index, or intentional early break.
The previous diagnostic output is retained, the begin count uses the captured runtime count, and a temporary count/index diagnostic immediately precedes the direct array read.
Remove the temporary diagnostics after resolution.

Dynamic-end vanilla precedent: installed `events/LAR_occupation.txt:247-254` computes temporary `num_units_to_create` and uses `for_loop_effect = { end = num_units_to_create ... }`.
Dynamic-index vanilla precedent: installed `common/scripted_effects/operation_strat_effects.txt:218` assigns an indexed token array value with `set_variable = { generic_operation_type_to_run = operation_types^i }`.
Existing repository exact structural precedent: `common/scripted_effects/chaosx_logic_effects.txt:161-165` loops `end = global.all_events^num`, stores the loop index, and explicitly reads `global.all_events^event_chaos_level_registry_index` into a temporary variable.
Offline Data structures also provides an array-sized `for_loop_effect` with dynamic `scored_array^s` access in its scorer example.
These precedents and installed `for_loop_effect` documentation establish the implemented index/dynamic-end syntax without asserting that the rejected runtime object is already known.

`technology_index_boundaries.json` records source-derived zero, one, and installed-count 679 scenarios: zero reads for empty, index zero for one entry, and indexes zero through 678 for 679 entries.
This is source-boundary evidence, not execution of the engine loop or technology consumers.
Installed vanilla `common/defines/00_defines.lua:25` sets `NGame.MAX_EFFECT_ITERATION = 1000`.
The current 679 named-source technology inventory is below that limit; future database inventories above the configured loop limit require a separate bounded continuation design to maintain full coverage.
No define was changed by this worker.

## Evidence, baseline, and validation limits

Source before SHA256: `3E77A358755B797DF592951282ACCBF7E2CF04727767EC9A1BFB2C52CD3F53DE`.
Source after SHA256: `90AE4B1FCFE0A27A51E87A5CFE99003DCA77E4B522DFDB9FCF657ABAEF3442D8`.
The current source was preserved byte-for-byte at ignored `baseline/technology_effects.before.txt` before the investigation.
The earlier handoff and source/MCP evidence remain at `docs/testing/runtime_repairs/20260913_cxt_parameter_parse_repairs/technology_handoff.md`, `technology_definition_audit.json`, and `technology_mcp_evidence.json`.
Those source and inspector artifacts cannot execute the technology helper or prove runtime full coverage.
The required scoped MCP `explain` query for the actual mod technology `anthrax_bomb_delivery_systems` succeeded again; its result is recorded in adjacent `technology_mcp_evidence.json`, revision `1fdcc4c6e84177fe0165f1cab7074479dbc485dd3b7ed31a417b3d6bd16a8b97`.
The known inspector analysis boundary excludes variable and meta-generated technology identifiers, and the earlier scoped helper record is `TECH_DYNAMIC_GRANT_UNRESOLVED`.
Standalone Technology Tree Viewer availability remains independently unverified; inspector exposure does not establish it.

No game process, live validation, new broad scan, transport investigation, subagent, staging, or commit was performed.
No extra source ownership was used.
Files changed in this follow-up: the assigned technology source helper, this handoff, `technology_mcp_evidence.json`, and `technology_index_boundaries.json`.
The indexed source implementation is complete, but this investigation remains unverified as a runtime error repair and must not be reported as proof that the original invalid technology is eliminated.
Skills applied: `chaos-redux-events` and `chaos-redux-subagents`; neither was changed.
