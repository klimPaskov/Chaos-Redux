# Exact population caller repairs

Date: 2026-10-03.
Repository: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.
Disposition: authorized caller repairs implemented, Migration mortality-floor policy accepted and queued for owner resolution, MCP validation blocked.
Acceptance basis: the parent reviewed `..\validation\033_acid_rain_exact_helper_caller_review_2026_10_03.md` and explicitly authorized the 12 storage repairs, unconditional Famine owner-floor assignment, five invalid temporary reads or credits, and two cleared-cause proof repairs.
The parent's later floor clarification explicitly permits the missing-policy gap to remain queued and forbids borrowing movement policy or forcing zero.
The parent owns review, isolated staging, and commit.
No Git staging or commit was performed.

## Completed source changes

Seven existing gameplay files changed, all under `common\scripted_effects\`.
The six authorized caller files received existing public output declarations immediately before their 12 exact-helper calls.
`020_black_plague_effects.txt` received only its authorized cause-proof assignment.
No helper, scripted trigger, script constant, public parameter, runtime generator, random weight, rate, choice, Event 033 source, GUI, or `.tools` file was added or changed.

The two declarations are:

```txt
set_temp_variable = { state_civilian_population_loss_applied = constant:chaos_meter_deaths.zero }
set_temp_variable = { state_civilian_population_loss_result = constant:chaos_meter_deaths.zero }
```

They create caller-owned storage for the measured applied receipt and result without changing a request, cursor, target, logging switch, or reason.
The gateway's existing output resets and return semantics remain authoritative.

| Caller file | Named caller | Post-patch exact call line |
| --- | --- | --- |
| `020_black_plague_scenario_effects.txt` | `black_plague_scenario_seed_state` | 314 |
| `029_riches_found_harm_effects.txt` | `riches_found_apply_harm_record` | 45 |
| `famine_adapter_effects.txt` | `famine_apply_related_state_deaths_exact` | 569 |
| `famine_core_effects.txt` | `famine_apply_mortality` | 2635 |
| `migration_adapter_effects.txt` | `migration_apply_related_state_deaths_exact` | 64 |
| `fallout_consolidated_effects.txt` | `fallout_event_230_apply_movement_shares` | 38624 |
| `fallout_consolidated_effects.txt` | `fallout_orientation_record_country_deaths` | 60178 |
| `fallout_consolidated_effects.txt` | `fallout_orientation_record_state_deaths` | 60226 |
| `fallout_consolidated_effects.txt` | `fallout_orientation_apply_capital_evacuation` | 60428 |
| `fallout_consolidated_effects.txt` | `fallout_event_100_apply_requisition_failure_deaths` | 70630 |
| `fallout_consolidated_effects.txt` | `fallout_event_243_apply_failure_deaths_and_damage` | 80520 |
| `fallout_consolidated_effects.txt` | `fallout_event_499_apply_migration` | 107813 |

Additional authorized hunks:

- `famine_adapter_effects.txt:566` assigns `state_civilian_population_loss_minimum_remaining = humanitarian_related_deaths_minimum_remaining` unconditionally.
  The former positive-only `if` wrapper was removed.
  The supplied owner value is preserved, including an explicitly supplied zero.
  No replacement floor constant, inferred policy, or new API input was introduced.
- `fallout_consolidated_effects.txt:60218,60227` reads the existing unscoped `fallout_orientation_state_death_request`.
  The persistent destination `ROOT.fallout_orientation_deaths_requested` remains scoped.
- `fallout_consolidated_effects.txt:60420` reads the existing unscoped `fallout_orientation_migration_total_request`.
- `fallout_consolidated_effects.txt:38634,60438` credits the existing destination state using unscoped temporary `fallout_event_230_population_moved` and `fallout_orientation_migration_movement`.
  Destination pointers and computed amounts are unchanged.
- `020_black_plague_effects.txt:1451` sets `famine_adapter_cause_proven = constant:chaos_meter_deaths_reason.black_plague`.
- `fallout_consolidated_effects.txt:4044` sets `famine_adapter_cause_proven = constant:chaos_meter_deaths_reason.air_winter_exposure`.
  Each constant matches the corresponding reason already supplied to the exact gateway in that same named block.
  This preserves the cause after the gateway's existing input cleanup.

The zero-log split-accounting callers retain their existing zero logging switch and separately owned Deaths bookkeeping.
No second Deaths registration or population debit was added.
`migration_adapter_effects.txt` received only the two output declarations.

## Shared helper and documentation boundary

The parent-owned `chaosx_dynamic_effects.txt` source SHA-256 remains `8b4db4f595a607d041d0f072de65dd906cdb10c40246690f78d3e4305dab4d49`.
The helper's state scope, seven existing temporary inputs, two existing public outputs, logging policy, reason settings, physical transaction, and cleanup were preserved.
The existing `chaosx_dynamic_effects.md:261–299` storage and observed-loss contract was read and not edited.
No new helper requires API documentation.
This handoff documents the repaired call sites and remaining input-policy gap.
No cleanup hook, event target, constant, or tuning table was added.

## Meaningful source-only validation

Command from the mod root:

```powershell
node docs/plans/033_acid_rain_plans/validation/caller_repairs_source_tests_2026_10_03.js
```

The actual-source tests passed.
They use separate temporary and saved-variable storage and conservative helper-frame cleanup.
The native population transaction is stubbed with an explicit observed receipt.
They do not execute HOI4, prove native population precision, or test the parent's physical-transaction implementation.

- All 12 callers retain their measured receipts for the sequence zero, 17, 101, zero.
  Caller input and cursor sentinels remain unchanged.
  Stale output sentinels are overwritten correctly.
  The captured before-source negative controls lose the receipt in all 12 cases, demonstrating the boundary defect rather than assuming a flat global temporary dictionary.
- Famine floor assignment passed 15 cases across owner-supplied floors zero, 300, 1000, 1500, and negative 10, each with missing, zero, and stale 777 ambient floor storage.
  Mathematical floor-boundary fixtures use a 1000-person population and 900-person request.
  These fixtures verify forwarding and contract boundaries, with native mutation stubbed.
- Eleven repaired callers freshly assign all seven gateway fields on their exact call path.
  Migration freshly assigns six and leaves the floor unresolved.
  This distinction is explicit in the result artifact.
- The Migration fixture shows that a cold missing floor fails the existence part of the existing gateway guard.
  A floor left as zero by a previous helper passes that existence check.
  `has_variable` therefore does not establish fresh mortality-policy input.
  No source gate or fallback was invented to conceal this gap.
- Five unscoped temporary reads or credits resolve to the actual temporary amount 80 even when unrelated saved ROOT variables hold 999.
  The captured before-source references resolve to the wrong saved-variable namespace in this source model.
- The two cause-proof assignments retain their intended cause constants after the shared input reason has been cleared to unknown.
- Exact call count remains 213.
  No Fallout generation was run.

The ownership check reconstructed all seven full pre-edit file byte streams by reversing only the authorized changes in their 14 captured named blocks.
Each reconstructed SHA-256 matched its captured pre-edit file hash.
This verifies preservation of concurrent changes already present in the snapshot, including unrelated dirty-file content.
Patch-local original line endings were restored by a guarded formatting pass after `apply_patch` edits.
No source values were changed by that formatting pass.
The test rejects later owned-block changes or unrelated byte drift, so the parent should treat its results as evidence for the recorded snapshot.

## Queued Migration mortality floor

Status: accepted and queued for owner policy input.
The exact missing input is the approved protected population floor for `migration_apply_related_state_deaths_exact` as a separate forced-displacement physical-death transaction.
The adapter documentation at `migration_adapter_effects.md:13–14` marks that API as owner-fed and API-only.
The wrapper supplies a reason and delegates, without a documented mortality floor.
No gameplay producer supplying that floor was found by the bounded caller search.

The read-only references named by the parent were checked:

- `migration_core_constants.txt:71` defines `migration_core_reconciliation.protected_population_share = 0.15`.
  `migration_core_effects.txt:681–712` uses it for Famine-survivor flight reservation, alongside existing population reservations.
- `migration_spontaneous_movement_constants.txt:27` defines `minimum_origin_population_k = 1` for spontaneous living movement.
  Its surrounding comments describe an origin remainder for that movement system.

Neither establishes the mortality policy for the separate forced-death adapter.
Coincident values or nearby owner logic do not authorize reuse.
The existing missing floor remains untouched.
The output-storage repair is independent and completed.
Full gateway caller compatibility remains open, particularly for a warm call with ambient zero floor storage.
The parent may review and isolate the transaction-first and output-repair tranche while carrying this explicit policy gap.

## MCP attempts and limits

Artifact: `..\validation\caller_repairs_mcp_attempts_2026_10_03.json`.
The exposed connected routes were checked before work.

The current narrow `reference_context`, `reference_search`, and exact-gateway `source_lookup` requests each returned `timed out awaiting tools/call after 600s`.
The `reference_read` dependency could not be satisfied because the reference routes returned no source ID and revision.
Pertinent local wiki and installed documentation were read directly under the repository route-gap rule.

The event-impact schema was established through two actual validation responses, which are preserved in the artifact.
The valid request used `impactSubject = { kind: "helper", name: "apply_exact_state_civilian_population_loss" }`, two nodes, two edges, and depth one.
That valid request also returned `timed out awaiting tools/call after 600s`.
The invalid-schema attempts are not counted as inspection evidence.

A narrower source lookup retry for `migration_apply_related_state_deaths_exact`, one definition and five lines without references, was started.
It also returned `timed out awaiting tools/call after 600s`, and that final error is recorded in the MCP artifact.
No successful current MCP inspection result, event graph, render, comparison, source revision, or engine validation is claimed.
`hoi4.script_validate` was absent from the connected tool list.
Matching event render or comparison could not be grounded in a returned inspection result.
The parent retains these MCP and native validation limits.

## Byte identities and evidence

| Changed caller file | Captured before SHA-256 | Validated after SHA-256 |
| --- | --- | --- |
| `020_black_plague_scenario_effects.txt` | `da1af5181b2c7346ef100ba509d8b63531857ac297d4a114968cb1372b64a030` | `192fa69e16c97a98ef46f2616df78cf21be6bcb3ff57489ca61086265115a023` |
| `029_riches_found_harm_effects.txt` | `d0046e3a9c0f7d1b5f118e1571fb61ff0697683c647c7ceac492b3215790fc60` | `69929480afffcf2882d7d4cf3c08280a221f03918adf1bc096391fef6d650010` |
| `famine_adapter_effects.txt` | `09bf27c2f784bbdcbd1883dfa7192b796ef8e18cad3d622820c131b18145fea0` | `9acc155670eb518d902f5eb750db5f40e103df105b68a3d4aff8960d25828108` |
| `famine_core_effects.txt` | `095974659833ac0c8a6d6bc0b40bce34a545754976c83b78cfe1007d97a1025d` | `d598b18998b93d9ab1632cba01b7530b93fd059a907a9d45e48438057233edbf` |
| `migration_adapter_effects.txt` | `37aad37c1b3aa4a31cc24dd6cc0c789b9c0648ff7070acb473c62e890c4d7c7a` | `d85735fa71656e37cfe79695d8ef998cea175f45afd65dc9cfc41a912d9f8398` |
| `fallout_consolidated_effects.txt` | `2217d7d893b5d9d476ed7e4645ebb14e3ab7697fd3421b9b8fa85d2e4a0132a6` | `d3938ffa248fb5f625bd4c9fe8daa511c84c233c552e9a5353ba247286c2c2bb` |
| `020_black_plague_effects.txt` | `6a74a8e8b96abb53957a45af7761e4123696c292e1158ec15516a68326e473d0` | `dc9da24d16ed0bf826a21fb7f6650eaf6b2d1a9a3473a0190b814004a0bc0d6a` |

Durable artifacts under `..\validation\`:

- `caller_repairs_2026_10_03_before_blocks.json` contains the actual pre-edit named blocks, their spans and hashes, and full pre-edit file hashes.
- `caller_repairs_2026_10_03_evidence.json` records exact before and after owned hunk substitutions, after file and block hashes, references, and the queued floor disposition.
- `caller_repairs_source_tests_2026_10_03.js` is the read-only actual-source replay and preservation test.
- `caller_repairs_source_results_2026_10_03.json` records the passed source checks and queued Migration policy case.
- `caller_repairs_mcp_attempts_2026_10_03.json` preserves delivered tool errors, schemas learned, and the narrow retry disposition.

Reference revisions, expressed as SHA-256 over local file bytes:

| Reference | SHA-256 |
| --- | --- |
| `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md` | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\script_concept_documentation.md` | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\script_constants\documentation.md` | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\scripted_effects\00_scripted_effects.txt` | `93ddd0d2e9f7a1a5640cfdafbae6b9ff0e1b4ee57e829c81d13b0cac23ad90bf` |
| `common\scripted_effects\migration_adapter_effects.md` | `01526ff96c417f2fe65225f4acb24a181a67adc46d3949b204a346ab6944702a` |
| `common\script_constants\migration_core_constants.txt` | `47145391c8a5aa82e333091dd2f7eb424a7b00dab34c916bfab2ffabbc66db9b` |
| `common\script_constants\migration_spontaneous_movement_constants.txt` | `c55e19d3e4d4ae91ae616e6dd5b49e83c85437e948eda0641b135fa321f08da2` |

Relevant sections read: offline Data structures lines 435–452, especially temporary lifetime at 440–442, installed effects documentation 7820–7841, installed Script Constants 216–249, installed constants schema 1–36, and the vanilla helper/state-iterator precedent in `00_scripted_effects.txt:1–35`.
The original audit contains additional state-population and Deaths registrar references that remain applicable.
No Paradox wiki web request was used.

## Remaining work and exclusions

The requested source-repair tranche is implemented.
Migration mortality-floor policy remains queued as explicitly authorized.
Native temporary lifetime, physical population execution, runtime target validity, and MCP event coverage are not proven by this source-only handoff.
Transitive wrapper output lifetime outside these exact call boundaries remains outside this tranche.

Event 031 request-based achievement accounting and Fallout 579 requested-as-applied accounting remain owner audit notes and were not patched.
The seven-file byte-reversal check confirms the Fallout 579 source was preserved.
No shared Deaths policy, state-map coverage, random behavior, asset, localisation, GUI, spreadsheet, generator, or broader mechanic was changed.
No gameplay fallback or simplification was implemented.
The queued floor is an explicit missing-policy limitation, not an approved replacement policy.

Skills used: `chaos-redux-events` and `chaos-redux-subagents`.
The events storage-lifetime guidance determined the caller declarations and conservative frame-cleanup fixtures.
The subagents ownership guidance kept edits within the exact authorized hunks and retained parent commit ownership.
No skill was created or edited by this worker.
