# Event016 Singularity native component receipt gap

Date: 2026-10-07.
Role: chaosx_scripted_system_architect, bounded read-only sidecar.
Root: C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux.
Disposition: source gap identified, with a concrete recommended parent patch contract.
Acceptance basis: the explicit sidecar assignment, approved exact literal output hooks, the instruction to preserve a matching paid timer, the accepted portfolio closure plan and final completion contract.
The recommendation preserves all six existing projects and their original native payloads.
It introduces no new project, technology, family, selection control, asset, model, focus, UI, weighted retune, global iteration or terminal design.
Only this handoff was written.
The finished nine-fixed-source tranche, all gameplay files, its tests and documentation, and the Git index were not edited.

## Findings

1. All six synchronous country outputs depend on completed-bit visibility.
Each output sets its literal existing component enum and calls `brilliant_scientist_register_singularity_component`.
The shared provider branch at `common\scripted_effects\016_brilliant_scientist_project_effects.txt:1503-1507` calls `brilliant_scientist_record_mengele_singularity_component`, whose bridge at `016_mengele_project_bridge_effects.txt:156-162` calls the private recorder.
The private recorder at `016_mengele_project_stage_effects.txt:1668-1698` gates its whole transaction on `brilliant_scientist_mengele_singularity_component_native_output_is_authentic`.
That trigger at `016_mengele_project_stage_triggers.txt:1565-1595` requires the matching exact project completed bit in every enum branch.
The identity mapping is exact, but it is a completion query rather than a synchronous output witness.
If that bit is not yet visible inside country_effects, a genuine literal output records nothing.
The installed output documentation establishes COUNTRY scope and FROM as the project, but does not guarantee when the completed query becomes visible.
This is a confirmed source dependency and conditional failure, not an observed engine timing defect.

2. Historical adoption is a distinct call site but lacks distinct receipt provenance.
The after-Theory driver at stage effects `1490-1526` preserves its outer transaction and iterates exactly six component codes through the same private recorder.
Its exact queries correctly reject another component's completed project.
It replays no native project output, payment or research.
Both fresh and historical registration write the same sparse component array, count and six private flags, with no source-mode record.
The existing native Prototype constants/effects/triggers do not provide a Singularity component witness or component mode array.
Do not classify this six-entry after-Theory reconciliation as a generic country/project scan.
Its current weakness is that it shares fresh authorization and has no separate mode.

3. Paid array preservation exists, but the private stage transition is insufficiently guarded.
The component recorder never clears, refunds or replaces an active paid receipt and writes no timer command.
However, its all-six branch at stage effects `1685-1693` applies Prototype without testing `brilliant_scientist_mengele_project_stage_receipt_is_empty`.
The output core at `919-929` checks output authorization, provider and predecessor, but does not itself check an empty paid receipt.
The Singularity predecessor at stage triggers `482-490` checks Theory, the component chain where DLC applies, and missing Prototype.
The final stage output at stage effects `1318-1322` sets the private Prototype flag and modifier.
Consequently, a sixth component can advance the private stage while a matching paid receipt remains active.
Preserving paid array bytes alone does not satisfy an unsettled matching-paid transition.
The missing guard must be fixed locally at the native component boundary and final Prototype adapter, without changing the paid finish/cancel core.

4. Component idempotence is present and must be retained.
Stage effects `1673-1683` appends only when the exact code is absent, derives count from array length, and sets the matching private flag.
The full-chain trigger at stage triggers `139-148` requires count six, array length six and all six flags.
Stage effects `43-56` rebuilds the legacy private component array from durable flags only when its schema flag is missing.
These ordinary writers preserve one receipt per exact component.
They do not establish provenance for arbitrary corrupted or externally modified arrays.
Do not change count to increment-on-callback or relax completion to count alone.

5. The bridge has a consumed temporary-result ownership gap.
Bridge `156-160` initializes its public project result but does not initialize `mengele_event016_native_component_recorded` before consuming the nested recorder's result.
The recorder creates that slot at stage effects `1669`.
Under conservative helper return semantics, a new private receipt can be written while the enclosing bridge reads zero.
The generic recorder already initializes `mengele_event016_native_component_recorded` at the start of `brilliant_scientist_mengele_record_native_project_prototype` in the supplied pre-tranche source.
That existing generic-consumer initializer is correct and must be preserved.
The missing initializer finding applies only to the separate bridge at `016_mengele_project_bridge_effects.txt:156-160`.
This is separate from the three noncustom hooks in the completed nine-source tranche, which correctly need no unused outer result export.
Initialize only genuinely consumed outputs in their consuming frames.

## Exact source and proposed literal wrapper map

All wrappers execute in the completing COUNTRY scope and take no caller selectors.
Each suffix below denotes the existing full project ID.
The proposed name is `brilliant_scientist_mengele_native_completion_<full project ID>`.

| Component | Existing enum | Dense mode index | Existing country output lines | Exact project ID |
| --- | --- | --- | --- | --- |
| command_core | 1 | 0 | 946-952, literal selector 949 | sp_brilliant_scientist_singularity_command_core |
| power_link | 2 | 1 | 1025-1031, literal selector 1028 | sp_brilliant_scientist_singularity_power_link |
| containment_lattice | 3 | 2 | 1104-1110, literal selector 1107 | sp_brilliant_scientist_singularity_containment_lattice |
| temporal_authenticator | 4 | 3 | 1183-1189, literal selector 1186 | sp_brilliant_scientist_singularity_temporal_authenticator |
| delivery_architecture | 5 | 4 | 1262-1268, literal selector 1265 | sp_brilliant_scientist_singularity_delivery_architecture |
| fail_deadly_governor | 6 | 5 | 1341-1347, literal selector 1344 | sp_brilliant_scientist_singularity_fail_deadly_governor |

These enums already exist at `common\script_constants\016_brilliant_scientist_constants.txt:972-985`.
Family Singularity is the existing ID 15 and paid/prototype family index 14.
Do not add component source codes 21-26 to the finished native Prototype enumeration.
A component enum plus the fixed project whitelist already identifies its single exact source.

## Smallest recommended implementation

Keep component-owned helpers and their documentation in the existing Mengele stage effect/trigger files.
Add six literal project-country-output hooks, an explicit historical adapter, pure evidence predicates, and a narrow final Prototype settlement helper.
Update only the necessary bridge compatibility entry points and matching documentation.
The prior nine-source core requires no implementation change.

| Proposed or retained helper | Inputs/defaults | Outputs and side effects | Call sites |
| --- | --- | --- | --- |
| Six `brilliant_scientist_mengele_native_completion_sp_brilliant_scientist_singularity_<component>` wrappers | COUNTRY, no inputs. Own family 15, exact existing `brilliant_scientist_singularity_component`, new temporary witness `mengele_event016_native_component_output_source`, mode fresh_output and result storage. | Always set `mengele_event016_native_observed_singularity_<component>`. Attempt accepted private component registration through strict gates. Never query completed for fresh authorization or replay native payload. | Beginning of the six existing project_output.country_effects blocks, before preserved original consumers. |
| `brilliant_scientist_mengele_singularity_component_source_is_supported` | COUNTRY trigger, family/component defaults none. | Pure exact six-pair whitelist, rejects none, fractional and unsupported component values. | Both modes before schema initialization. |
| `brilliant_scientist_mengele_singularity_component_exact_source_is_completed` | COUNTRY trigger, supported component. | Pure six literal project queries keyed to that exact enum. | Historical mode only. |
| `brilliant_scientist_mengele_singularity_component_evidence_is_valid` | COUNTRY trigger, component, mode and witness, default none. | Fresh requires exact matching synchronous witness. Adopted requires witness none and exact completed project. All other modes fail. | Private recorder. |
| `brilliant_scientist_mengele_record_singularity_component`, refactored locally | COUNTRY, explicit whitelisted family/component/mode/witness. Strict provider, Theory and empty matching paid family receipt. | Existing changed marker `mengele_event016_native_component_recorded` zero/one, exact private component flag, de-duplicated sparse array, derived count and first-acceptance mode. Calls final Prototype helper through its own guarded frame. | Six wrappers and explicit adoption adapter only. |
| `brilliant_scientist_mengele_adopt_exact_completed_singularity_component` | COUNTRY, caller-owned exact component. Explicit adopted_completed and witness none. | Exact historical acceptance without an observed-output flag or native replay. Same result contract and strict gates. | Existing six-entry after-Theory loop, replacing its direct fresh/ambiguous recorder call. |
| `brilliant_scientist_mengele_try_settle_singularity_native_prototype` | COUNTRY, no inferred project identity. Own family 15, stage Prototype, index/output/authorization slots. | Require provider, Theory, all six exact private components, missing Prototype and empty matching paid receipt, then use the existing private output core once. Never complete a later stage or terminal. | Component recorder after registration or an idempotent duplicate, and the explicit bounded adoption boundary. |

Use the existing `mengele_event016_native_prototype_mode` constants none/fresh_output/adopted_completed.
Add one dense six-slot `mengele_event016_singularity_component_mode_entries` array, keyed by component enum minus one, independently of the sparse completion-array append order.
Append missing mode slots with none, never truncate or guess old receipt modes.
Only a newly accepted exact private component writes its mode.
A repeated fresh output or later historical query must preserve the original accepted mode.
Legacy flags and sparse receipts with missing provenance retain mode none and are documented as unsupported historical provenance.
They must not silently become fresh.

The native private boundary should use the same empty-paid-family policy as the existing unselected native core.
When any matching family paid stage is active, keep the genuine observed-output flag but leave accepted component array/count/flags/modes and Prototype unchanged.
Do not clear or refund paid state, shorten or replace the timer, or create a retry scheduler.
A subsequent authorized exact historical reconciliation may use adopted mode.
This recommendation adds no cancellation-time adoption policy and waives no native lifecycle requirement.

Give the recorder and final helper independent frame-owned storage for every temporary they read after nested helpers.
Initialize `mengele_event016_native_component_recorded` in the legacy bridge/generic consumer if that consumer remains callable.
Fresh or historical callers that do not consume a result need no outer export initializer.
Clear component, witness, mode, private family/stage/index and authorization on every exit while preserving a caller-owned changed marker.
Retain the after-Theory outer snapshots/restoration at stage effects `1507-1515` and `1580-1588`.

The preserved original `brilliant_scientist_register_singularity_component` call must continue serving the host.
After a new literal provider hook returns and clears its mode/witness, the original generic provider branch must be a no-op for private acceptance.
Guard the provider bridge/private recorder against mode none so the original callback cannot re-adopt a blocked paid completion or fabricate fresh evidence.
The generic Singularity branch at stage effects `1661-1663` must likewise not bypass explicit evidence.
This can be done in provider-owned compatibility helpers without editing the shared host file or its foreign working hunk.
Do not use family-wide OR completion scans, unrelated project callbacks, availability reconciliation, world iteration or periodic polling as receipt writers.

## Parent migration and acceptance checks

1. Preserve immutable full before-project bytes and all original costs, rewards, AI, iteration outputs, country payload and facility payload.
Add only the six owned hidden literal hooks and retain full-file equality after stripping those hooks.
2. Replace the native component authenticity gate with explicit source/mode evidence, preserving exact enum validation and strict provider/Theory gates.
Add the empty-paid gate before accepted component writes and again before native Prototype settlement.
3. Split historical entry from fresh entry at the existing bounded after-Theory loop, preserve its outer transaction, and block no-mode compatibility calls.
4. Preserve exact de-duplication and derived count, add the six-slot mode migration without guessing old provenance, and document flags, defaults, outputs and cleanup.
5. Validate all six fresh outputs before completed-bit visibility, wrong component/family/witness/mode, unrelated completed objects, every historical subset, all six orderings relevant to a sixth-component finish, repeat/idempotent retry, provider/Theory loss, busy paid Prototype, cold result consumers and unchanged host state.
Check that each mode slot follows component ID rather than array append order.
Test initialized/uninitialized and short/oversized provenance arrays without truncation.
6. Confirm no accepted component or Prototype transition occurs during a matching paid receipt, with every paid cost, active stage and timer identity preserved.
Keep actual native payment, timer, cancellation/reselection and callback-generation acceptance separate from source fixtures.

No cost, duration, threshold, AI or probability tuning table is needed.
No event target or persistent project pointer is needed for six fixed sources.
Observed output facts, private completed receipts, modes and learned history remain durable through provider cleanup.
Cleanup removes temporary authorization only and preserves the existing paid cleanup owner.
Terminal/Fallout integration, availability design, no-DLC progression and the full causal arming chain are separate parent-owned surfaces, not certified by this sidecar.

## Meaningful evidence and limitations

Eighteen bounded source-model checks were run read-only.
Six cases reject registration when the matching completed bit is absent.
Six cases preserve identical array/count/flags on repeated exact completed registration.
Four active-stage fixtures append the sixth component and write Prototype while keeping all active/cost arrays identical.
The matching Prototype fixture is the required transaction counterexample.
The other active-stage fixtures are robustness states and do not prove ordinary campaign reachability.
Two conservative-frame cases show a private component is written in either case, while the bridge returns zero without preowned component-result storage and one with it.

The model interprets the actual component recorder, exact predicate, bridge wrapper and private Prototype output core.
Provider validity and non-host status are explicit inputs.
Native payment, clock, decision timers, full payloads, availability reconciliation and dynamic modifier refresh are not executed.
No live engine observation, save, game launch, weighted audit or source mutation occurred.
The source-model check of the entire after-Theory loop was not completed because the reused evaluator lacks add_to_temp_variable support.
Its bounded six-entry path, exact project queries and outer restoration were inspected directly in source instead.
No unsupported evaluator result is presented as engine evidence.

## MCP route gap and local reference reads

Live tool metadata confirms reference_context, reference_search, reference_read, source_lookup and script_validate schemas.
A bounded initial batch requested event reference context with limit 4, is_special_project_completed search with limit 2, country_effects search with limit 2, and an exact record_singularity_component definition with references false and maxLines 70.
No returned result was observed before the exec observation cell 51 was terminated.
A separate revision-bound reference_read requested installed project documentation at lines 191-220, id 807fc917dd0a099abdf2ac367b4a56dc88af85bd5a41d47dcae6b7e955d0018f, revision 16879504bc72aa357f1d3c0f1093e94a3946f8c35e7942f65ac9a5d3bcd6c643.
It remained pending before observation cell 55 was terminated.
Terminating observation does not establish cancellation or failure of the server operations.
No task/job negotiation or retry of a mutation was involved.
There are no successful current-sidecar MCP artifact URIs or server revision results to cite.
The previous tranche's successful reference deliveries do not establish current service health.

Per AGENTS.md's reference-route-gap rule, the answering local sections below were read directly and hashed.
These local references and source findings do not replace required integrated domain MCP or engine evidence.
No broad event graph, helper expansion, task, render/compare or probability operation was started.
The bounded read-only helper-inspection route remains an explicit missing evidence delivery.

Relevant direct sections: installed special-project project-output COUNTRY/FROM documentation 191-212, installed completed-project trigger 6243-6257, installed is_in_array 5672-5685, installed add_to_array 2278-2292, installed temporary variables 7820-7827, installed script constants 216-222 and constants schema 1-34.
Offline sections: Triggers 885-886, Data structures temporary lifetimes 435-443 and arrays 1069-1086, Scopes 25-42.
The vanilla reactor country-output precedent at nuclear_projects.txt:21-37 was read.
The shared dynamic registry header and documentation were read and identify these adapters as event-owned orchestration rather than neutral cross-system helpers.
Skills applied: chaos-redux-events and chaos-redux-subagents.
No skill or generic tooling change is proposed.

Completed here: exact source-path and call-site review, paid/idempotence/cold-frame counterexamples, local reference reads and this patch contract.
Parent implementation, integrated domain validation and engine acceptance remain open.
No simplifications are proposed.
The full Event016 goal remains incomplete.

## Parent checkpoint retained

The parent identifies the finished nine-fixed-source commit as `9a80334164a5d6c6e84c89065247c0d8f81fbe8f`.
Its separate narrowed one-node event comparison timed out after 600 seconds and is recorded in `adf77c6d2`.
No extra graph operation is needed for this read-only sidecar, and no result from that timeout is inferred.
Parent evidence already retains installed project documentation 198-215 and offline Data structures 440-443 for exact output scope and nested temporary lifetime.
This recommendation does not modify or reopen the completed nine-source tranche.

## Bounded source-model result

```json
{
  "cases": 18,
  "results": [
    {
      "case": "before_completed_bit",
      "component": 1,
      "count": 0
    },
    {
      "case": "idempotent_repeat",
      "component": 1,
      "count": 1
    },
    {
      "case": "before_completed_bit",
      "component": 2,
      "count": 0
    },
    {
      "case": "idempotent_repeat",
      "component": 2,
      "count": 1
    },
    {
      "case": "before_completed_bit",
      "component": 3,
      "count": 0
    },
    {
      "case": "idempotent_repeat",
      "component": 3,
      "count": 1
    },
    {
      "case": "before_completed_bit",
      "component": 4,
      "count": 0
    },
    {
      "case": "idempotent_repeat",
      "component": 4,
      "count": 1
    },
    {
      "case": "before_completed_bit",
      "component": 5,
      "count": 0
    },
    {
      "case": "idempotent_repeat",
      "component": 5,
      "count": 1
    },
    {
      "case": "before_completed_bit",
      "component": 6,
      "count": 0
    },
    {
      "case": "idempotent_repeat",
      "component": 6,
      "count": 1
    },
    {
      "case": "active_paid_stage",
      "stage": 1,
      "prototype_applied": true,
      "paid_arrays_unchanged": true,
      "authorization_leaked": 0.0
    },
    {
      "case": "active_paid_stage",
      "stage": 2,
      "prototype_applied": true,
      "paid_arrays_unchanged": true,
      "authorization_leaked": 0.0
    },
    {
      "case": "active_paid_stage",
      "stage": 3,
      "prototype_applied": true,
      "paid_arrays_unchanged": true,
      "authorization_leaked": 0.0
    },
    {
      "case": "active_paid_stage",
      "stage": 4,
      "prototype_applied": true,
      "paid_arrays_unchanged": true,
      "authorization_leaked": 0.0
    },
    {
      "case": "bridge_cold_component_result",
      "caller_owns_component_result": false,
      "component_count": 1,
      "bridge_result": 0
    },
    {
      "case": "bridge_cold_component_result",
      "caller_owns_component_result": true,
      "component_count": 1,
      "bridge_result": 1
    }
  ],
  "limits": [
    "provider and non-host are declared fixture inputs",
    "native payload, clocks, decision timer, reconciliation and modifier refresh not executed",
    "actual private recorder, output core, bridge and predicates interpreted under conservative temporary return semantics"
  ]
}
```


## Reviewed source revisions

| Path | SHA-256 of reviewed bytes |
| --- | --- |
| `common\special_projects\projects\016_brilliant_scientist_projects.txt` | `f1e00642739e8577a374171299155b74b4eb599f6c3512e849f007126278bfea` |
| `common\scripted_effects\016_mengele_project_stage_effects.txt` | `1a8ec6cafaf1ec425a99925cbe85f9523e58e5c801bcc5e559a9405132d475a5` |
| `common\scripted_triggers\016_mengele_project_stage_triggers.txt` | `5ab7041ce22f13fbfecf641f4ca9e6fc7d693ddf366da14e631a3dfa498e537c` |
| `common\scripted_effects\016_mengele_project_bridge_effects.txt` | `a7646197bf43a62c21ec4b6fd44aae1dba80fa134fa0bc273193b1d70660f9e5` |
| `common\script_constants\016_mengele_native_prototype_constants.txt` | `6b4281095d61d6ac7c297eeb00ee12c5cb1f229b0aba8c183fbcc0b4efa0fc68` |
| `common\scripted_effects\016_mengele_native_prototype_effects.txt` | `de333685409502bbb9b1a870891cdd0dcdfa31802c6771b9ad17e26b27db415c` |
| `common\scripted_triggers\016_mengele_native_prototype_triggers.txt` | `c6571fa872dd74baf8d813b54c5fe1fdb122b76d8ae7b35822bd22ebcaf6d7cc` |
| `common\scripted_effects\016_brilliant_scientist_project_effects.txt` | `7588dcb2090e25fdca3c863cc19878b417f13d5bdf5281d5295a78e1acc3de0f` |
| `common\script_constants\016_brilliant_scientist_constants.txt` | `adfee7fe6093933c394c34c8a6a162795d4bdb4575512c476b417c1173b6e4a6` |
| `common\script_constants\016_mengele_project_stage_constants.txt` | `527499b80909a5f7f2544940d6db51a6145ff2634c4c3c0792cbeff22cdacd71` |
| `docs\plans\016_brilliant_scientist_plans\016_final_mengele_portfolio_closure_plan_2026-09-02.md` | `469453c56d356def807e6a9ec50fceab4430c4519900b5953ae62fed4802b377` |
| `docs\specs\016_brilliant_scientist_specs\specs\016_final_completion_contract.md` | `3bfe2f50fdb3151edac843842077eb299410fd311522c0a9627be66050b87fb9` |

## Direct local reference revisions

These hashes identify the directly read local snapshots after current MCP delivery remained unresolved.

| Path | Read lines | SHA-256 |
| --- | --- | --- |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\special_projects\projects\documentation.md` | 191-212 | `16879504bc72aa357f1d3c0f1093e94a3946f8c35e7942f65ac9a5d3bcd6c643` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md` | 5672-5685 and 6243-6257 | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md` | 2278-2292 and 7820-7827 | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\script_concept_documentation.md` | 216-222 | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\script_constants\documentation.md` | 1-34 | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` |
| `paradox_wiki\Triggers - Hearts of Iron 4 Wiki.md` | 885-886 | `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06` |
| `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` | 435-443 and 1069-1086 | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| `paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md` | 25-42 | `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\special_projects\projects\nuclear_projects.txt` | 21-37 | `b822068268cf848ba9dc9000d762c7005bdde4f6773dd5509e17ce895165e83f` |
