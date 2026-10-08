# FORM-48 bound dynamic ledger display

Date: 2026-10-08.
Role: chaosx_scripted_system_architect, assigned R3 presentation-only implementation.
Acceptance basis: the parent adopted the three residual findings and explicitly assigned only the FORM-48 category display correction under accepted D34/D38, with the follow-up instruction to use a native boolean result and no numeric validity marker.
Disposition: implemented, source-tested and parent reviewed; its scoped Git commit is the publication receipt, and native localisation acceptance remains open.
The full Event 006 goal is not closed by this handoff.

## Result and exact owned hunks

The category description resolves its viewer's own or specifically bound live carrier and captures that carrier's name pointer and six ledger values.
It no longer reads the static HBX template.
The verified package is IW-184 California, not IW-177; the existing post-formation proof requires original HBX, anchor/capital 378 owned and controlled, family 48, PFX identity, and committed integration flags.
Invalid, stale, missing, ended, or unbound viewers select localized `N/A` without formatting a fake carrier or zero ledger.
The valid branch preserves the original labels, paragraph, section colors, constant denominators, and `|0` numeric formatting.

| Changed file | Owned hunk |
| --- | --- |
| `common/scripted_triggers/006_independence_wave_form48_display_triggers.txt` | New isolated display-only file; two COUNTRY predicates, no gameplay writes |
| `common/scripted_localisation/006_independence_wave_scripted_localisation_registry.txt` | Appended only `GetIndependenceWaveForm48Ledger`, at 2453-2473; seven caller-initialized outputs, validated live key and N/A key |
| `localisation/english/006_independence_wave_pacific_l_english.yml` | Existing category desc at 178 becomes the getter call; added live-desc key at 311 retaining the original text with dynamic substitutions, and unavailable key at 312 |
| `common/scripted_effects/chaosx_dynamic_effects.md` | Added only the `independence_wave_form48_display` owner API index row at 485, linking this contract |
| This handoff | New implementation/evidence document only |

The original FORM-48 trigger file, including its 78-108 R2 ledger and all existing gates, was not edited.
Its whole-file SHA-256 stayed `342a0fb96aed1def1ba0b766e000a46092ba3d6a0a814f1f2e79644645f17c44`.
The R1 decision file stayed `c6c1df3711f44269543fcc2d093a6f7f968bc2932aca113aa887663d371e13f6`.
No R1 reachable-partner trigger, AI expression, availability, category visibility, price, reward, admission, asset, workbook, or other document was edited.
No Git or index operation was performed.

## Display API

Public getter: `[GetIndependenceWaveForm48Ledger]`, evaluated in the category viewer's COUNTRY scope.
Its valid branch initializes every public temporary before calling `capture_independence_wave_form48_display`.
The capture helper returns the native trigger boolean; no `display_valid` scalar, saved flag, or persistent validity state exists.
The seven public outputs are:

| Temporary output | Valid value |
| --- | --- |
| `independence_wave_form48_display_carrier` | Exact live carrier country pointer, formatted through the existing D38 `[?pointer.GetName]` pattern |
| `independence_wave_form48_display_shipping` | Carrier shipping coordination |
| `independence_wave_form48_display_industry` | Carrier industrial specialization |
| `independence_wave_form48_display_defense` | Carrier defense readiness |
| `independence_wave_form48_display_autonomy` | Carrier member autonomy |
| `independence_wave_form48_display_strain` | Carrier compact strain |
| `independence_wave_form48_display_cycles` | Carrier completed program cycles |

Defaults/rejection: the caller and capture helper reset all seven outputs to `constant:independence_wave_value.minimum` before lookup; a false result selects the separate `independence_wave_form48_display_unavailable` key (`N/A`), so default values and pointer zero are never used as a substitute ledger or country.
Only a true return authorizes formatting these outputs.
No new tuning constants were added; the helper reuses the existing minimum, first-array index, package, family, and consent constants.

The capture helper freezes viewer ID, viewer generation, viewer anchor, requested carrier ID, and requested carrier generation in private unscoped temporary storage.
It uses the documented `any_of` array iterator with distinct `value` and `index` outputs to validate the viewer's exact country/generation row and the requested carrier's exact country/generation row in aligned `global.independence_wave_active_countries` / `global.independence_wave_active_country_generation_entries`.
It does not invent an index parameter for `any_of_scopes`.
It never takes another HBX origin merely because it appears first.

Nested COUNTRY predicate: `has_independence_wave_form48_display_carrier_for_viewer`, called in the selected carrier scope.
Its inputs are the capture helper's frozen viewer/carrier IDs and generations, frozen viewer anchor, and the two matched registry-row indices.
It repeats the exact carrier ID and paired generation-row comparisons, proves the current HBX/IW-184/PFX/378 carrier, and requires all six actual metric variables.
It validates aligned frozen member arrays, including this carrier's own ID/generation/anchor row and the viewer's ID/generation/anchor/consent row.
The capture caller initializes the two scratch outputs `independence_wave_form48_display_member_country` and `independence_wave_form48_display_member_index` before each nested proof invocation.
These scratch values are not formatted or returned as public outputs.

Carrier and member generations are distinct identities.
For HAW/FSM, the installed normal carrier-generation snapshot must match the actual carrier generation, while the member's current generation must match its own global registration and frozen member-ledger row.
The display does not require a member's own generation to equal the carrier's generation.
It reuses the existing active-autonomous-member predicate and checks the frozen pointer/generation against the current member binding without changing that predicate.

Directional receipt contract: a present member-to-carrier access/guarantee receipt requires that exact relation to remain present in that direction; a present carrier-to-member receipt is checked by scoping to the frozen requested carrier and testing the viewer target.
Absent receipts are not fabricated or required: the installer legitimately omits an ownership flag when a relation already existed.
The capture conditional copies outputs only for a validated proof and then returns that proof's native boolean with fresh caller-owned scratch at the second nested boundary.
All private inputs and public outputs stay within this display evaluation; no normal country/global variable, flag, event target, array, relation, weight, or availability is written.

Example caller (the actual scripted-localisation trigger follows this contract):

```text
set_temp_variable = { independence_wave_form48_display_carrier = constant:independence_wave_value.minimum }
set_temp_variable = { independence_wave_form48_display_shipping = constant:independence_wave_value.minimum }
set_temp_variable = { independence_wave_form48_display_industry = constant:independence_wave_value.minimum }
set_temp_variable = { independence_wave_form48_display_defense = constant:independence_wave_value.minimum }
set_temp_variable = { independence_wave_form48_display_autonomy = constant:independence_wave_value.minimum }
set_temp_variable = { independence_wave_form48_display_strain = constant:independence_wave_value.minimum }
set_temp_variable = { independence_wave_form48_display_cycles = constant:independence_wave_value.minimum }
capture_independence_wave_form48_display = yes
```

## Source cases and preservation evidence

Thirty-five actual-source cases passed using an in-memory Clausewitz subset evaluator that loads the production display predicates, production scripted-localisation caller, actual existing active/post-formation/member/alignment predicates, and the relevant actual constant categories.
Native country/state, flag, variable, array, and directional relation primitives are supplied fixture semantics.
The evaluator conservatively discards temporary keys first created in a returning helper while retaining modifications to caller-owned storage, and asserts scratch ownership at the nested proof boundary.
It asserts no persistent world-state mutation and no private display temporary escaping the outer helper return.
This is source contract evidence, not native engine, localisation rendering, or game/save observation.

| Case group | Result |
| --- | --- |
| Carrier self, bound HAW and bound FSM | Return the correct live key, carrier pointer, and all six values, with distinct carrier/member generations accepted |
| Another HBX first, including the same generation | Never replaces the explicitly requested carrier |
| Stale carrier/global viewer row, stale member frozen generation, stale binding generation | N/A with reset public outputs |
| Unbound member, missing carrier object, ended carrier/viewer, carrier absent from registry | N/A |
| Registry or member-array misalignment | N/A |
| Wrong IW-177 package, lost carrier anchor control, wrong family, missing metric | N/A |
| Viewer absent from ledger, carrier self-row missing/stale, pointer redirected to another carrier's copied ledger | N/A |
| Four correct directional receipts | Correct live ledger |
| Each receipt loses its direction; reverse access cannot satisfy member-to-carrier receipt | N/A |
| Pre-existing bidirectional relations without owned receipts | Correct live ledger; no invented receipt requirement |
| Valid -> unbound -> valid repeated lookup in one temporary context | Public values reset to defaults on rejection and recover fresh values; no stale name or numeric capture |

The formatting test reverses only the two name and six metric substitutions and reconstructs the exact original English file bytes, proving that the original labels, color tokens, narrative, bounds, and numeric formats are unchanged and all unrelated English keys are preserved.
Removing only the appended getter reconstructs the exact pre-edit scripted-localisation registry hash `e6745d4798177920905e672cc398e4cf92408dda95894d93e8d47aa9dd087548`.
Removing only the owned API row reconstructs the exact pre-edit dynamic-docs hash `f8fe39f34ed3bfd5737c125d200610f9e9e8c1eae4ec49655672aa1a4f73a9cd`, preserving the unrelated dirty hunks that already existed.
No broad generator, durable test/report tooling, or gameplay fixture was added to the repository.

## References and MCP gates

Skills applied: current AGENTS.md, events, subagents, and the existing D38 localisation/helper-output patterns.
The category metadata was inspected at `common/decisions/categories/006_independence_wave_categories.txt:666-676`; it remains visible for the existing post-formation carrier or active autonomous-member contexts.
The existing FORM-05 caller-owned capture pattern was read at `common/scripted_localisation/006_independence_wave_scripted_localisation_registry.txt:352-415`.
Vanilla `common/scripted_localisation/00_scripted_localisation.txt:1-16` supplies the installed COUNTRY `defined_text`, text-trigger, and localisation-key precedent.

| Read reference | Lines | Revision |
| --- | --- | --- |
| Offline Data structures, temporary lifetime/unscoped semantics | 435-443 | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| Offline Data structures, `any_of` value/index and unchanged scope | 1148 | Same Data structures revision |
| Offline Localisation, text ordering and temporaries available during formatting | 672-685 | `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064` |
| Installed triggers documentation, `any_of` | 1515-1530 | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| Installed triggers documentation, set_temp_variable | 7482-7488 | Same triggers revision |
| Installed effects documentation, set_temp_variable | 7820-7827 | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| Installed triggers documentation, gives_military_access_to | 2994-3002 | Same triggers revision above |

Reference_context identified a result-limited omitted Data structures source; the targeted Variable types and any_of search/read calls above supplied that required coverage.
Initial guessed array-helper names `find_in_array` and `any_in_array` had zero reference matches and were not used.
The installed live `any_of` route explicitly documents both temporary value and index outputs, which the final code uses.

Source lookup at indexed revision `fbbd991cfa7e2f67a6855a70cb8d4944dc6678d1517455d7e96854df4df7a9ee` returned complete non-shadowed definitions for the unchanged member predicate at `mod:common/scripted_triggers/006_independence_wave_form48_triggers.txt:306-329`, installer at `mod:common/scripted_effects/006_independence_wave_form48_effects.txt:57-86`, and active-array alignment at `mod:common/scripted_triggers/006_independence_wave_triggers.txt:599-601`.
The installer read is the basis for conditional directional-receipt ownership and its carrier-generation snapshot.
The existing named FORM-05 localisation source_lookup returned zero definitions; its actual source was read directly, without claiming that namespace indexing or native formatting was validated.

New capture source_lookup at indexed revision `d4d4ac67190675e8035bcc4e96b0381f0206768b2567b01f1e61b95f2c51345d` found one non-shadowed COUNTRY scripted-trigger definition at `mod:common/scripted_triggers/006_independence_wave_form48_display_triggers.txt:94-160`.
The bounded tool excerpt retained 94-111 with nextLine 112; the complete local body was read by the source evaluator, and no full MCP helper expansion is claimed.
Reference discovery remains incomplete (`referencesComplete = false`, 20,220 unresolved workspace references); the caller chain was checked directly in the appended source.
Script/source calls returned no artifact URI; these read-only outcomes and revisions are the retained evidence.

Final `hoi4.script_validate` requests used actual body strings, kind trigger, explicit COUNTRY scope, installed documentation, and explicit COUNTRY bindings for `var:...display_viewer`, `var:...display_registry_carrier`, and `var:...display_requested_carrier`.
They report only `syntax`, `command_kind`, and `declared_scope` under documentation aggregate revision `9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b`, with parametersChecked false.

| Final check | Commands checked | Unresolved total / argument blocks unchecked | Omitted findings | Result |
| --- | --- | --- | --- | --- |
| Whole capture body | 28 | 28 / 24 | 34 | SCRIPT_CHECK_PARTIAL, valid null |
| Whole nested proof body | 45 | 20 / 14 | 41 | SCRIPT_CHECK_PARTIAL, valid null |
| Bounded capture-selection suffix | 12 | 12 / 8 | 0 | SCRIPT_CHECK_PARTIAL, valid null |
| Bounded capture country block | 12 | 13 / 11 | 4 | SCRIPT_CHECK_PARTIAL, valid null |
| Bounded viewer country/relation block | 25 | 8 / 5 | 10 | SCRIPT_CHECK_PARTIAL, valid null |
| Final seven-output scripted-localisation caller trigger | 7 | 8 / 7 | 0 | SCRIPT_CHECK_PARTIAL, valid null |

Unexpanded custom calls are explicitly unresolved: `is_independence_wave_active_country`, `independence_wave_active_country_arrays_are_aligned`, `independence_wave_formable_member_arrays_are_aligned`, `is_independence_wave_form48_postformation_carrier`, `is_independence_wave_form48_active_autonomous_member`, `has_independence_wave_form48_display_carrier_for_viewer`, and `capture_independence_wave_form48_display` at their respective callers.
Unvalidated native argument blocks include set_temp_variable, check_variable, and any_of, including the nested paired-row/member-ledger portions that the root checker does not expand.
Omitted findings are not treated as checked parameter coverage or validated compound gates.
The bounded selection and caller checks expose all their unresolved findings; other bodies retain the stated omissions and their actual source review.
No native scope/type failure was silently substituted with a no-op helper or suppressed finding.
The client rejected an oversized validation limit (maximum 32) and a reserved PREV scope-binding request; both were corrected, and neither request-shape rejection is an engine defect or a validation pass.

## Review limits and final identities

No weights or availability changed, so this display patch does not alter the frozen R1/R2 probability surfaces or require a coefficient comparison.
No persistent cleanup logic was needed: all introduced storage is temporary and reset before capture; no global event target or receipt was introduced.
Native locality, temporary survival during real formatting, and the actual category text consumer remain unobserved; no HOI4 process, save, or log was requested or opened.
The source fixtures deliberately model committed FORM-48 state without bypassing or changing the current IW-179 admission gate, and are not evidence that current normal admission can produce that full formation.
No layout, GUI button, animation, or asset was changed or rendered; color/text preservation is exact source evidence, not an in-game screenshot claim.
No simplification or fallback identity was applied; the requested existing-style localized N/A branch is deliberate invalid-viewer presentation.
The parent owns final review and commit, R1/R2 patches and AI audits, and the full Event 006 completion claim.

| Owned source | Final SHA-256 |
| --- | --- |
| Display trigger file | `0a88413354580e3daad68d9a74417f202a5fa83c9d6032595ddbaac31607f175` |
| Scripted localisation registry | `cc2c3e2648b179a1ffeb6ce2938bc8c259195a2121f48d52cb34ce6d737ed0ce` |
| English Pacific localisation | `83dbe8154346181a406c640a667f0df99b2740f33e6a98ca4f316460f269c2ed` |
| Dynamic docs with owned index row | `84498a90f1c2ba1a7c39d4f3e99d471e0a13b9b6d95d728a8231e967e3d0551e` |
