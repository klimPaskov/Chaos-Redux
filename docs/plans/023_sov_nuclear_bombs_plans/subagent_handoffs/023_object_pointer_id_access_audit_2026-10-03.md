# Event 023 object-pointer ID access audit

Date: 2026-10-03.
Role: `chaosx_scripted_system_architect`, read-only syntax audit with this report as the only authorized write.
Workspace: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.
MCP workspace: `mod_chaos_redux_ea3b2d67c2c0`.
Disposition: bounded source audit completed, installed separator authority and runtime parser behavior unresolved.

## Finding and confidence

The offline Data structures rule explicitly distinguishes static scope access with a period from pointer-variable chaining with a colon.
Under that rule, `sov_nuclear_bombs_action_state:id`, `sov_nuclear_bombs_action_source_state:id`, and `sov_nuclear_bombs_backup_command_state:id` are the documented forms for reading the pointed-to state's internal ID.
Four direct normal-variable `.id` consumers violate that documented rule in the audited snapshot.
Three were named in the assignment and the fourth is the accepted-action target-state receipt at event effects line 1008.

Classification: four probable syntax defects, confirmed discrepancies against the offline documentation, zero confirmed engine parser failures.
I cannot establish an authoritative installed rule rejecting the dot form or a shipped vanilla example of a normal pointer variable followed by `:id`.
The installed script-concept document does not contain the variable-chain grammar, and the installed dynamic-variable document does not enumerate the state `id` getter.
The successful MCP source lookup confirms the dismantlement source token exists, but does not validate its parser semantics.
Do not promote this finding into observed engine failure or assume that undocumented compatibility syntax is impossible.

`THIS.id`, `ROOT.id`, `PREV.id`, `FROM.id`, `SOV.id`, and `event_target:alias.id` belong to the static/dual-scope access category and must not receive the proposed blanket substitution.
The scanned Event 023 consumers include the first four static spellings and event-target access, but no direct `SOV.id` occurrence.
`constant:sov_nuclear_bombs_event.id` is a constant category/key lookup, not object-pointer access.

## Exact references and vanilla evidence

Repository-relative paths below resolve under the workspace above.
Installed-relative paths resolve under `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`.
Line spans are inclusive, and SHA-256 revisions identify the bytes inspected.

| Source | Sections read | SHA-256 |
| --- | --- | --- |
| `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` | 425–459, 461–480, 263–328, 1479–1487, 1667–1674 | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| `paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md` | 245–270, including static scopes and `var:` | `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` |
| Installed `documentation\script_concept_documentation.md` | Entire document, lines 1–248, especially contextual localisation 125–154 and script constants 216–245 | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| Installed `documentation\dynamic_variables_documentation.md` | 1–18, 175–187, state section 1096–1175, targeted whole-file search for `id` and chaining rules | `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda` |
| Installed `documentation\effects_documentation.md` | Explicit pointer scope example 848–862, variable setters 7820–7839 and 7888–7907 | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| Installed `documentation\triggers_documentation.md` | `check_variable` 2110–2135, variable scope validity 7450–7471 | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| Installed `common\scripted_effects\SOV_scripted_effects.txt` | `SOV_start_civil_war`, definition begins 7802, relevant body 8280–8315 | `cc9e16837afa1428d11e053dc982446b35587980daa011a1df12114c3ace2bf4` |
| Installed `common\scripted_effects\00_scripted_effects.txt` | 1230–1243, `var:best_leader` scope entry | `93ddd0d2e9f7a1a5640cfdafbae6b9ff0e1b4ee57e829c81d13b0cac23ad90bf` |

Data structures line 449 says: `Variables must be chained using the : separator (rather than the usual dot)` and gives `ABC.capital:var_name`.
The same line gives `PREV.PREV.var_name` and `event_target:my_event_target.var_name` as period-separated static scope access.
Lines 429–431 distinguish object-pointer values and explicit `var:` scope entry.
Scopes line 270 gives `var:my_variable = { … }`.

Installed effects lines 858–861 use `var:my_country_var = { ... }`, and installed triggers lines 7467–7468 use `var:my_var = { ... }`.
The installed `check_variable` section supports comparison to another variable in any scope, without documenting chained variable grammar.
The installed script-concept rules for `[Object.Property]` concern contextual localisation, so they do not establish support for `value = stored_pointer.id` in engine script.
The script-constant rules at 216–245 explain why constant category/key periods remain separate from this audit.

Actual vanilla SOV source at 8302 writes `set_variable = { ROOT.temp_target_state = THIS.id }`, enters ROOT at 8303, and supplies `var:ROOT.temp_target_state` to `target_state` at 8307.
This is positive vanilla evidence for an ID getter inside an explicit state scope and a stored value consumed as a state pointer.
It is not an example of normal-variable `.id` or `:id` chaining.
Actual vanilla `00_scripted_effects.txt` at 1240–1242 enters `var:best_leader` and fires an event there.

Targeted searches of installed `common` and `events` found no `:id` occurrence.
A wider installed text search over `.txt`, `.md`, `.info`, and `.yml` also found no `:id` or `var:<simple_name>.id` occurrence.
An initial general colon search produced `var:`, `event_target:`, `constant:`, `temp_var:`, flag-duration localisation, comments, and other namespaces, which do not prove normal-variable chaining.
These negative searches establish a missing precedent in the searched text set, not an engine prohibition.
The initially guessed `documentation\variables_documentation.md` does not exist in this installation.
The actual installed variable reference is `documentation\dynamic_variables_documentation.md`.
Installed build identifiers read from the game root are branch `1.19.2.0/develop` and revision `a729d47bd1c55457e6886b6eeb2fcdef4ac05057`.
These identify installed files, not the connected MCP server version.

## Four direct consumers and proposed changes

| Consumer | Current expression | Documented colon alternative | Trace and impact if the dot lookup fails |
| --- | --- | --- | --- |
| `common\scripted_effects\023_sov_nuclear_bombs_event_effects.txt:2923`, `sov_nuclear_bombs_complete_dismantlement` | `var = sov_nuclear_bombs_action_source_state.id` | `var = sov_nuclear_bombs_action_source_state:id` | Actor-owned pointer copied from the selected action state at 693 or 703, or from THIS state at 711 or 725. The dismantlement registration copies it at runtime 2070 and writes the comparison receipt through THIS.id at 2074. A failed lookup can reject the identity gate and take cancellation. No reservation/accounting proof is repeated here. |
| `common\scripted_effects\023_sov_nuclear_bombs_runtime_effects.txt:2176`, `sov_nuclear_bombs_reconcile_registry_state_change` | `var = sov_nuclear_bombs_backup_command_state.id` inside SOV | `var = sov_nuclear_bombs_backup_command_state:id` inside SOV | Registration at 1680 stores the state pointer on SOV from PREV. The comparison's current PREV.id is the changed state. A failed lookup can prevent clearing SOV's matching backup pointer at 2178. |
| `common\scripted_effects\chaos_meter_effects.txt:6046`, `chaos_meter_on_non_yield_test_accident` | `value = sov_nuclear_bombs_action_state.id` | `value = sov_nuclear_bombs_action_state:id` | Action staging stores an event-target state pointer at event effects 685 or 689 and writes the actor-owned action_state_id from THIS.id at 729. A failed lookup can block the accepted accident endpoint. Its downstream weights and consequences are outside this audit. |
| `common\scripted_effects\023_sov_nuclear_bombs_event_effects.txt:1008`, `sov_nuclear_bombs_record_action_receipt` | `sov_nuclear_bombs_last_target_state = sov_nuclear_bombs_action_state.id` | `sov_nuclear_bombs_last_target_state = sov_nuclear_bombs_action_state:id` | Runs after acceptance and pointer presence checks at 1006–1008. A failed lookup can record the wrong internal target identity. Another existing write at 2490 uses the valid static event-target form, which must remain intact. |

These are proposed owner changes, not accepted or applied patches.
The minimal proposal changes only the four normal-variable separators and retains every condition, operator, ledger field, nonce, receipt, route, and effect order.
Because installed separator authority remains missing, the more directly supported alternative is to enter the stored object with `var:` and use `THIS.id` there.
The following are exact equivalent source shapes proposed for owner review, with the surrounding guards retained.

For dismantlement, replace only the identity check with:

```text
var:sov_nuclear_bombs_action_source_state = {
	check_variable = { var = THIS.id value = PREV.sov_nuclear_bombs_dismantlement_source_id compare = equals }
}
```

For backup reconciliation, retain SOV's `exists` and `has_variable` checks and replace its identity check with:

```text
var:sov_nuclear_bombs_backup_command_state = {
	check_variable = { var = THIS.id value = PREV.PREV.id compare = equals }
}
```

That block remains inside the existing SOV block.
PREV is SOV after entering the pointer, while PREV.PREV is the original changed state.
Using PREV.id in this nested variant would compare against SOV's country identity and change behavior.

For the accident endpoint, fold the identity comparison into its existing pointer-state validation block and remove the separate direct chain check:

```text
var:sov_nuclear_bombs_action_state = {
	impassable = no
	check_variable = { var = THIS.id value = PREV.sov_nuclear_bombs_action_state_id compare = equals }
}
```

For the accepted-action target receipt, retain the existing pointer-presence guard and replace its assignment with:

```text
var:sov_nuclear_bombs_action_state = {
	set_variable = { PREV.sov_nuclear_bombs_last_target_state = THIS.id }
}
```

These explicit-block proposals use installed documented scope entry, installed documented variable operations, vanilla THIS.id precedent, and offline PREV scope semantics.
They are source-supported proposals and were not executed in game.
Do not introduce a generic helper for these four narrow accesses.
No new constants, tuning tables, targets, flags, variables, cleanup system, central router, native adapter, or ledger migration is needed for this syntax-only proposal.

## Identity units

Data structures line 1671 identifies state `id` as the internal object ID, which differs from `id = <number>` in a state history file.
Line 1484 gives the corresponding internal country ID.
The dismantlement receipt at runtime 2074 and action-state receipt at event effects 729 are already written using THIS.id.
The backup comparison uses PREV.id on the changed state, so its two intended operands are also internal state identities.
Keep that identity domain in either proposed repair.
Do not replace these comparisons with file state IDs, `GetID` localisation, arbitrary numeric constants, or a comparison against another country's id.
The last-target receipt at 2490 likewise uses an event target's internal id.
This audit does not certify the meaning of every other field ending in `_state_id` throughout Event 023.

## Complete bounded consumer inventory

The inventory scans all 19 `*023*.txt` files under `common` and `events`, then the named shared endpoint at chaos meter lines 6022–6046.
It classifies all literal `.id` or `:id` tokens in that set after discarding line comments.
Event 023 files contain 57 token occurrences: 3 direct normal-variable accesses, 25 static-scope accesses, 22 event-target accesses, and 7 constant category/key accesses.
The shared endpoint adds the fourth direct normal-variable access, yielding 58 tokens in the bounded inventory.
No direct normal-variable `:id` alternative is currently present in these files.
The four direct normal-variable accesses are fully listed above.

Static-scope consumers:

| File | Lines and tokens |
| --- | --- |
| `common\on_actions\023_sov_nuclear_bombs_on_actions.txt` | 104 THIS.id, 145 ROOT.id, 184 ROOT.id |
| `common\scripted_effects\023_sov_nuclear_bombs_runtime_effects.txt` | 1053 PREV.id, 1726 THIS.id, 2074 THIS.id, 2161 PREV.id, 2176 PREV.id, 2280 THIS.id, 2443 THIS.id, 2780–2784 THIS.id once per line |
| `common\scripted_effects\023_sov_nuclear_bombs_event_effects.txt` | 245 THIS.id, 262 THIS.id, 729 THIS.id, 740 THIS.id |
| `common\scripted_triggers\023_sov_nuclear_bombs_event_triggers.txt` | 686 THIS.id, 791 THIS.id, 1043 THIS.id and FROM.id, 1072 THIS.id |
| `common\decisions\023_sov_nuclear_bombs_decisions.txt` | 1124 FROM.id |

The classification above only clears the separator distinction.
It does not certify which object THIS or ROOT denotes at each unrelated call site, including the nested ROOT assignments at event effects 245 and 262.
Their surrounding semantics are outside the requested direct-variable-chain audit.

Event-target consumers, all with the literal `event_target:` prefix and a period before `id`:

| File | Lines and alias names |
| --- | --- |
| Runtime effects | 1702 `sov_nuclear_bombs_assembly_selection`, 1838 `sov_nuclear_bombs_disperse_source_state`, 1839 `sov_nuclear_bombs_selected_state` |
| Runtime effects | 2391/2554/2780 `sov_nuclear_bombs_test_state`, 2401/2564/2781 `sov_nuclear_bombs_selected_test_state`, 2411/2574/2782 `sov_nuclear_bombs_selected_state`, 2421/2584/2783 `sov_nuclear_bombs_pending_reactor_state`, 2431/2594/2784 `sov_nuclear_bombs_disperse_source_state` |
| Event effects | 1162/1996/2490 `sov_nuclear_bombs_selected_state`, 1246 `sov_nuclear_bombs_coercion_target` |

Constant consumers are `constant:sov_nuclear_bombs_event.id` at event effects 1812 and scripted localisation 307, 317, 327, 337, 347, 354.

The following scanned files contain no literal `.id` or `:id` consumer:

- `events\023_soviet_nukes.txt`
- `common\on_actions\023_sov_nuclear_bombs_cxt_on_actions.txt`
- `common\scripted_effects\023_sov_nuclear_bombs_cost_effects.txt`
- `common\scripted_effects\023_sov_nuclear_bombs_achievement_effects.txt`
- `common\scripted_effects\023_sov_nuclear_bombs_cxt_test_effects.txt`
- `common\mtth\023_sov_nuclear_bombs_mtth.txt`
- `common\scripted_triggers\023_sov_nuclear_bombs_runtime_triggers.txt`
- `common\scripted_triggers\023_sov_nuclear_bombs_cost_triggers.txt`
- `common\scripted_triggers\023_sov_nuclear_bombs_achievement_triggers.txt`
- `common\ideas\023_sov_nuclear_bombs_ideas.txt`
- `common\ideas\023_sov_nuclear_bombs_cxt_extension_ideas.txt`
- `common\decisions\categories\023_sov_nuclear_bombs_categories.txt`
- `common\script_constants\023_sov_nuclear_bombs_constants.txt`

The decisions and MTTH files were included only in this literal access inventory.
Decision design, costs, phases, AI weights, probability pools, GUI layouts, map topology, localisation content, and native adapters were not audited.
A targeted search for `sov_nuclear_bombs_<name>.id` across all `common` and `events` text confirmed the same four direct consumers, with event-target and constant matches classified separately.
The inventory does not claim coverage of dynamically constructed tokens, external packages, or every shared Event 023 integration.

## MCP evidence and limits

Live metadata exposes `mcp__hoi4_agent_tools__hoi4_reference_context`, `hoi4_reference_search`, `hoi4_reference_read`, and `hoi4_source_lookup` in this session.
All actual calls use the explicit MCP workspace ID above.
The live source-lookup schema supports `symbol`, `kind`, `includeReferences`, line bounds and revision, but does not expose `view` or `keyPath`.
No wrapper, local service modification, background job, helper expansion, or native MCP task was used.
Connected-server health/version and native task negotiation were not established, so job/helper-expansion routes were not invoked.
No `hoi4_script_validate` route is exposed in this session.

- `reference_context`, event surface, question about normal pointer scope access, limit 4: `OK`, missing list empty, omitted count 6, `omittedSources` includes Data structures and Scopes. Those relevant sources were subsequently searched/read directly. Unrelated omitted topics are not claimed as covered.
- `reference_search`, `variable scope`, game_doc/wiki, limit 4: `OK`, total 285, returned dynamic-variable section headers. This was discovery only.
- `reference_search`, `Variables must be chained`, wiki, limit 1: `OK`, returned Data structures Scoping, section 444–480, ID `338680a6b2bbd220717fbd8fc7571aabe2c63519431acc3aa41e5e5440df1822`, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
- Matching `reference_read`, start 444, maxLines 16: `OK`, returned 444–459 including the complete separator rule. `nextLine = 460` was not needed for that rule, and local lines 461–480 were additionally read.
- `reference_search`, `check_variable`, game_doc, limit 1: `OK`, section 2110–2135, ID `eba1cc3a7863a60b1ffcb1293508be9a3228770609e2e9569a2cec95215f8a2c`, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`.
- Matching `reference_read`, start 2110, maxLines 26: `OK`, complete cited section, no continuation.
- `source_lookup`, symbol `sov_nuclear_bombs_complete_dismantlement`, includeReferences false, maxDefinitions 1, maxLines 12, maxReferences 0: `OK`, source index revision `7c82a33c34d7c3d040e8ef9b0808549e6ba2d9cabcf2b9cd9893e725b6dc4be1`, one non-overridden mod scripted-effect definition at 2913–2967, returned 2913–2924 including suspect 2923, `nextLine = 2925`. The remaining relevant body was read locally. Definitions complete and skippedSourceCount 0. References were deliberately excluded and referencesComplete false, so this lookup is not a consumer-coverage claim.

The reference service reports 50 installed-documentation files and 54 offline wiki files available, with `script_doc` unavailable and zero files.
All successful reference/source calls above return zero artifacts and no tool blockers.
No artifact URI or runtime validation result should be inferred from those responses.

Event inspection used no helper expansion.
The tool metadata types selector as unknown, so two requests received schema errors: the first omitted `selector.kind` and supplied maxDepth 0, the second used `selector.id` instead of `selector.eventId`.
The corrected bounded request uses `mode = trace`, `selector = { kind: event, eventId: chaosx.nr23.1 }`, maxNodes 1, maxEdges 1, maxDepth 1, expandHelpers false.
The corrected trace returned `tool call error: tool call failed for hoi4_agent_tools/hoi4.event_inspect`, caused by `timed out awaiting tools/call after 600s`.
A narrower root-only retry uses the same exact event selector and bounds with `mode = roots` and expandHelpers false.
The root-only retry returned the identical `timed out awaiting tools/call after 600s` error.
Exact MCP gap: neither the bounded event trace nor its narrower root-only retry delivered an event-domain result, artifact, source revision, or coverage diagnostics.
This is a failed observation through the connected route, and does not prove a server-side analysis outcome or an engine syntax failure.
An event trace would establish graph coverage only and would not settle normal-variable separator acceptance.

## Source snapshot and shared-tree limitations

The three directly relevant implementation files were hashed repeatedly with unchanged bytes, most recently at `2026-10-03T18:17:42+03:00`.
Line references describe that inspected snapshot and must be rechecked if other agents subsequently change these files.

| File | SHA-256 |
| --- | --- |
| `common\scripted_effects\023_sov_nuclear_bombs_event_effects.txt` | `ee30908e201fa955ddef39a1b4278969225fc2b3362c22138b6da1f552bc12e6` |
| `common\scripted_effects\023_sov_nuclear_bombs_runtime_effects.txt` | `0958b4367a454661b1f60d0814bb2d8316671a661df42dc88c7558f846831e57` |
| `common\scripted_effects\chaos_meter_effects.txt` | `c00446add013dbac77f73be962328730f4a493c6af61ad3e50ac1ff1f7d96293` |

Required instructions were read fully: AGENTS.md, 446 lines, hash `38e479cb75828ba888860be8bc3739f9286c0d925cc7d8de5ecd3b8dadec46cf`, events skill, 906 lines, hash `e9e6ee4c875ffd6a92ee91885a8a4a40d35801e651228e9604e8a1e603b2789b`, and subagents skill, 406 lines, hash `06079fb7e7c01bf09a5fea1ffabdfbb73b99fcecddd28ef7720415fbbceeda61`.
The skills governed read-only ownership, exact source evidence, and the separation of source coverage from runtime claims.
No skill was created or updated.

## Completed, unresolved, and owner follow-up

Completed: documented separator distinction, actual vanilla explicit-scope precedent, complete bounded literal-consumer inventory, pointer writers and matching receipt units, four exact proposed substitutions, and scope-block alternatives with correct PREV nesting.
Unresolved: authoritative installed variable-chain grammar, acceptance or rejection of the current dot form by the actual engine, live outcomes of the four consumers, and event-domain inspection coverage after both 600-second transport timeouts.
Meaningful validation performed: reference reads tied to revisions, exact source lookup, whole bounded token classification, inspection of pointer writers and ID receipt writers, vanilla precedent inspection, and repeated hashes of the three finding files.
Meaningful validation skipped: engine parser execution and live consumer tests, because the task forbids game execution and provides no runtime evidence. Installed script validation is unavailable.
No ledger, reservation, cost, phase, AI, weight, native adapter, asset, localisation, workbook, skill, or Git change was made.
No design simplification or gameplay fallback was applied.
The only created file is this requested report.

Owner follow-up is limited to reviewing the four proposed access changes, choosing the documented colon form or the explicitly scoped form, and retaining the existing internal-ID domain and exact actor/state nesting.
Do not change every `.id`, and do not expand this report into a reservation audit or Event 023 completion claim.
