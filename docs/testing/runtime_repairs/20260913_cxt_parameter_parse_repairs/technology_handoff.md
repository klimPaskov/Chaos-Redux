# CXT technology consumer investigation

Disposition: unresolved.
The failed token-text interpolation is removed, and the parent-authorized temporary diagnostics are implemented, but the original runtime database element rejection is not resolved.
This is a reviewable investigation patch, not a completed technology repair or a commit candidate.

## Scope and acceptance basis

The parent assigned only `common/scripted_effects/chaosx_test_country_technology_effects.txt`, this handoff, and technology evidence in this QA directory.
The parent explicitly authorized temporary diagnostics if no supported complete repair could be established.
No other source file was edited, no subagents were spawned, no changes were staged or committed, and Hearts of Iron IV was not launched or controlled.
Only the two supplied attachments were consulted for runtime errors.

## Evidence and correction of the premise

The earlier supplied attachment at `C:/Users/klimp/.codex/attachments/b699e2d1-5ac3-4f57-8bef-5603ce72bfc6/pasted-text.txt` contains one `has_tech: Invalid tech` message and one `set_technology: Invalid tech` message at 1936.01.01.13 and again at 1936.01.04.01.
It does not identify two distinct invalid objects.
Both consumers can reject the same loop element; its identity, index, raw value, and database-array size are absent.
The recurrence after game start means a history-only availability explanation is insufficient.

The current supplied attachment at `C:/Users/klimp/.codex/attachments/2124b3ce-d9fd-48b8-bd4f-81b8503c20dc/pasted-text.txt` contains the two same-date history invocations with `memfile:3` and `memfile:5` parser failures, invalid database tokens `.` and `=`, and invalid technology consumer messages.
Those punctuation diagnostics are not proof that the technology database contains punctuation-named technologies.
They are evidence that the generated meta text is malformed.
Its exact expansion is not present, so the conversion's underlying failure is unresolved.

## Primary documentation and precedents

- Installed `documentation/dynamic_variables_documentation.md:1048-1049` documents `technology` under GLOBAL as an array of objects in the technology database.
- Installed `documentation/effects_documentation.md:4279-4294` documents `for_each_loop`, its temporary `value`, and its temporary `index` fields.
- Installed `documentation/effects_documentation.md:7805-7818` documents country-scope `set_technology`, technology IDs as keys, and `popup = no`.
- Installed `documentation/triggers_documentation.md:4882-4889` documents country-scope `has_tech`, but supplies no explicit token-conversion guarantee.
- Installed `documentation/triggers_documentation.md:5006-5013` documents `has_variable` as variable existence, not technology database object validity.
No documented technology object validity trigger was found in that installed trigger reference.
A variable-existence guard does not establish that skipping an element preserves the full inventory, so no such guard or inferred sentinel filter is implemented.
- Installed `documentation/effects_documentation.md:4802-4809` documents localized `log` output.
- Installed `documentation/effects_documentation.md:4833-4851` documents `meta_effect` text injection, but does not establish that `GetTokenKey` converts every `global.technology` database object.
- Installed `documentation/script_concept_documentation.md` and `documentation/loc_objects_documentation.md` were checked; neither provided that conversion guarantee.
- Offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:735-746` describes token-valued variables and `GetTokenKey`, including tokenizable technologies.
This describes variables with the token flag and does not prove every runtime database array element is such a token.
Its array section at line 820 documents zero-based indexes and `array^num`.
- Offline `paradox_wiki/Technology modding - Hearts of Iron 4 Wiki.md` documents the `technologies` wrapper and effect-based silent research.
All required core wiki pages, the events skill, and the subagents skill were consulted.
- Installed `common/technologies/` has no separate documentation file.
Vanilla `infantry.txt` and `special_projects_tech.txt` were inspected as actual definition precedents.
- Actual vanilla `common/scripted_effects/zz_debug_effects.txt:112-120` uses `set_technology = { improved_infantry_weapons = 1 popup = no }` and technology diagnostics.
No installed vanilla `global.technology` complete-grant loop or dynamic technology `var:` grant example was found.
- Approved Kaiserreich `C:/Program Files (x86)/Steam/steamapps/workshop/content/394360/1521695605/common/scripted_effects/00_transfer_technology_effects.txt:652-695` uses `for_each_loop` over `PREV.researched_techs`, `value = technology`, `NOT = { has_tech = var:technology }`, and `set_technology = { var:technology = 1 popup = no }`.
This is a concrete native consumer precedent for researched technology objects, not proof about the unidentified element in the full database array.
No full database grant loop was found in the installed approved reference mods 1521695605 and 2265420196.
Reference-mod directory 1458561226 is absent.
- Existing repository `union_compatible_researched_technologies_from_donor` in `chaosx_dynamic_effects.txt:481-528` uses the same native consumers over `researched_techs`.
The matching helper documentation was consulted.

## Implemented helper map

Helper: `chaosx_test_country_complete_all_technologies`.
Scope: country.
Inputs: engine-owned `global.technology` array; no caller inputs or defaults.
Outputs: technologies granted to the current country and temporary `chaosx_test_country_technology_grant_applied`.
Temporary working values: `chaosx_test_country_current_technology` and `chaosx_test_country_current_technology_index`.
Side effects: silent native technology grants, existing completion callbacks, existing tree-layout refresh when a grant occurs, and temporary diagnostic output.

The failed `GetTokenKey` meta injection has been replaced with native `var:` consumers.
The array remains runtime-driven; every array element is attempted, with the existing `has_tech` idempotence check and `popup = no` preserved.
`GetTokenKey` remains only in diagnostic text and cannot generate malformed technology effect script.
The two temporary `CXT_TECH_DIAGNOSTIC` log statements report the country and database count once per invocation, then zero-based index, raw numeric value, and token text immediately before each consumer pair.
They intentionally do not assert a token exists or skip an element.
Remove these diagnostics once the underlying rejection is resolved.
They can produce hundreds of lines per pass; this is accepted temporary instrumentation rather than permanent behavior.

Call sites are unchanged: CXT history lines 24 and 27, and the CXT initial-setup, direct-start, refresh, and maintenance orchestration in `chaosx_test_country_effects.txt`.
The history preunlock/project/second-preunlock sequence and completion flag lifecycle are preserved.
No constants, tuning table, event target, persistent variable, flag, or cleanup helper was added.
No icons or localisation changes are needed because the patch adds no player-facing surface.

## Meaningful source and MCP validation

`technology_definition_audit.json` records a read-only token/depth audit of all 12 Chaos Redux and 13 installed vanilla technology definition files.
It found 679 named technology blocks, no punctuation/invalid IDs, no malformed mod wrapper children, and no unclosed definition blocks.
Reported vanilla wrapper assignments beginning with `@` are legitimate file-local macro definitions, not malformed technologies.
This audit does not execute the engine parser, model generated database entries, or serve as a static replacement inventory.

`hoi4.tech_inspect` scan succeeded for workspace `mod_chaos_redux_ea3b2d67c2c0`, revision `66b0b8041425390ebc9b25e0c679e95561e0c50f3ccdb53d93a775a5a6cff870`, graph hash `3a2953bd8a9ea20754a6be9e7c2440b463488aced056adffa6a9cd0ed50f939c`.
Its source technology count is also 679.
The scoped `explain` query for the actual mod technology `anthrax_bomb_delivery_systems` succeeded.
An exploratory query for `bio_basic_warfare` returned `TECHNOLOGY_NOT_FOUND`; it is not a technology ID used by this patch or evidence of a defect.

The authoritative scan artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bb4c67ddc456f12b0bab38287e55d33e2d186a0f908bc5432649ea8021520176/e284d9b521aeed868fa496560532f9cfb6ac5f17c7d91660f1bf784ce8c7b5dc/technology-scan-66b0b8041425.json`.
The source-scoped unresolved record is `TECH_DYNAMIC_GRANT_UNRESOLVED` for `chaosx_test_country_complete_all_technologies`, because dynamic technology keys cannot be resolved statically.
The service explicitly excludes meta-generated or variable technology identifiers from supported analysis.
Its aggregate validation did not pass: it reports 1396 blocking diagnostics across the broad source index, which includes unrelated source-reference diagnostics.
No broad diagnostic was attributed to the unidentified runtime array element or used to justify a filter.

The one-shot artifact transport produced a malformed stringified JSON envelope; bounded base64 byte-range reads recovered 101721 bytes through the final tail and parsed the reconstructed JSON.
`technology_mcp_evidence.json` records exact ranges, transport metadata, analysis boundaries, graph metadata, and the source-scoped unresolved record.
The declared artifact SHA256 is recorded; no independent cryptographic digest of the recovered bytes was computed.
The scoped explain artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/aa424401c02504d6e91b68ecff5a16a7fe960322c3c32905e6075c1b6016fbc8/363869bf2e613f8ec549dd8009d0095fbd0801f75b629add8a738aa4b90836ed/technology-explain-66b0b8041425.json`.

No technology tree definition, layout, bonus, unlock, or asset was changed, so graph rendering and tree comparison would not validate the helper's runtime consumer behavior.
They were not presented as proof of the repair.
Standalone Technology Tree Viewer availability was not independently verified; the callable MCP inspector is available, and a standalone viewer remains unverified.
Runtime full coverage, native object consumption for the failing element, and callback/idempotence behavior could not be executed by this read-only service.
No game process or live test was run.

## Files, baseline, and recovery

- Changed source: `common/scripted_effects/chaosx_test_country_technology_effects.txt`.
- Documentation added: this handoff.
- Evidence added: `technology_definition_audit.json` and `technology_mcp_evidence.json`.
- Ignored baseline: `baseline/technology_effects.before.txt`, copied byte-for-byte before editing.
- Before SHA256: `FC43CC2B98F4050BBB827414EA764CF0B90AFAC0D4E5196E11E5324D687381CF`.
- After source SHA256: `3E77A358755B797DF592951282ACCBF7E2CF04727767EC9A1BFB2C52CD3F53DE`.

Recovery is a literal copy of the baseline into the assigned source file if the parent rejects the investigation patch.
The parent owns further changes and final integration.

## Simplifications, omissions, and blockers

The full repair is incomplete because neither attachment identifies the failing element and available installed documentation does not establish how to convert or validate that unidentified database entry while preserving every technology.
No static inventory substitute, sentinel/type filter, history omission, mechanic omission, or unapproved provider fallback was introduced.
The complete runtime grant contract remains attempted but unproven and still contains the original unresolved consumer failure.
Temporary diagnostics are retained under the parent's explicit instruction and must be removed after resolution.
Do not commit or describe this technology plan as complete.

Skills used: `chaos-redux-events` and `chaos-redux-subagents`.
No skills were created or updated.
