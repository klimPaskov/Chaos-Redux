# Automatic protection caller storage and military priority

Disposition: implemented within the two source files authorized by the parent.
The acceptance basis is the parent's bounded correction request under accepted overhaul specification 13, including automatic real-stock issue and replacement, military priority, derived readiness, and no worldwide iteration.
This handoff does not close the broader CBRN overhaul or establish native execution.

## Files and exact changes

Gameplay ownership was limited to `common/scripted_effects/cbrn_protection_effects.txt` and `common/scripted_effects/cbrn_protection_decision_effects.txt`.
No index changes or commit were made.
The parent owns final documentation integration, review, event comparison, and commit.

| Changed helper | Scope | Existing inputs and outputs | Bounded correction and call site |
| --- | --- | --- | --- |
| `cbrn_run_protection_maintenance_cycle` | Country | Real stock, current issued models, conditions, controlled-state need, and persisted cycle count | Run military filter service, military issue, civilian filter service, then civilian issue in that order. Only the two middle blocks moved. |
| `cbrn_replace_military_mask_filters` | Country | Military issued crates, filter condition, replacement technology, real five-model stock. Writes condition and replacement demand, then refreshes derived readiness. | Declare `cbrn_mask_stock_debit_completed` before `cbrn_debit_mask_stockpile_oldest_first`, preserving its returned service quantity for restoration. |
| `cbrn_replace_state_civilian_mask_filters` | State | State issued crates, filter condition, contamination, controller technology and real stock. Writes state condition and state/controller replacement demand. | Declare the same output in the state caller before entering `controller` for the debit. Temporary storage is unscoped. |
| `cbrn_complete_population_registration` | Country | Existing reserve-scaled fitting loss, capped by the existing tuning. Credits reconditionable material and schedules maintenance only after positive service. | Declare completed debit before the stock helper. This is the actual consumer near original line 90. There is no `cbrn_seed_reconditioning_pool` definition in these owned files. |
| `cbrn_distribute_requested_external_masks_to_state` | State | Existing four distribution inputs, valid donor event target, controller and real donor stock. Exports external proof and consumed/usable quantities. | Own `cbrn_distribution_usable_crates` before the internal distributor, so its positive-delivery proof and achievement call can read the returned quantity. |
| `cbrn_distribute_reserved_occupied_masks_to_state` | State | Existing distribution inputs and exact five-model occupied receipt. Exports reserved proof and consumed/usable quantities. | Own usable quantity before the internal distributor. Donor, ROOT, control, recovery checks and refund call remain unchanged. |
| `cbrn_distribute_reserved_external_masks_to_state` | State | Existing distribution inputs and exact five-model external receipt. Exports external proof and consumed/usable quantities. | Own usable quantity before the internal distributor. Donor selection, receipt checks, achievement and refund call remain unchanged. |
| `cbrn_complete_mask_reconditioning` | Country | Reconditionable cache and replacement demand. Produces real reconditioned models, then stores a positive recovered batch for the existing quality roll. | Declare `cbrn_recondition_recovered` before `cbrn_recondition_damaged_masks`. The entire positive guard and 20/80 random-list AST remain identical. |

The changes add caller storage for outputs that these specific callers read.
They do not reset an outer input, loop cursor, transaction ID, or tuning value.
These existing output names were already reset to zero by their producers, so defining storage earlier does not add a different reset policy.

## Helper documentation and tuning

Comments beside each declaration explain the storage requirement.
This handoff records the preserved helper contracts and validation limits.
The canonical helper reference is `common/scripted_effects/cbrn_scripted_effects.md`, which was outside the parent's allowed write paths.
The parent should add the caller declaration obligation to its debit, external/reserved distribution and reconditioning sections, and record the maintenance order in its routine-maintenance section.
Any outer caller that consumes `cbrn_mask_stock_debit_completed`, `cbrn_recondition_recovered`, `cbrn_distribution_usable_crates`, `cbrn_distribution_consumed_crates`, or the public proof outputs must declare its own storage before the corresponding helper.
Local storage fixes nested reads but does not make public temporaries persistent beyond an undeclared outer boundary.

No new helper or constant was introduced.
Existing tuning remains authoritative in `common/script_constants/cbrn_system_constants.txt`, with the readiness weights in `cbrn_doctrine_constants.txt`.
The suite exercises the unchanged 30-day maintenance delay, 12-cycle annual storage schedule, 25% issue increment, quarter-force historical reserve, 0.18 replacement ratio, 0.70 rapid-filter cost multiplier, contamination multiplier, and 0.45 reconditioning ratio.
These are existing gameplay calibration values, not newly established historical claims.
The defective/safe weights remain 20/80.

No flag, regular variable, event-target namespace, or target lifetime was added.
Existing receipt refunds and cleanup calls remain intact.
No worldwide scan or new periodic hook was introduced.
Migration consists of the direct caller declarations and the maintenance block order, with no framework replacement.

## Consumer audit

All uses of `cbrn_mask_stock_debit_completed` were searched across scripted effects.
The three affected callers are the two filter-service helpers and population-registration completion.
`cbrn_hq_effects.txt` already declares the output before its debit and remains untouched.
The issue helper consumes its own `cbrn_mask_issue_completed` inside its defining helper, so no directly connected owned caller gap was found there.
The internal distributor consumes its own fitting, consumed and usable outputs within its defining helper.
`cbrn_complete_occupied_state_distribution` already owns consumed and usable output storage before the reserved wrapper.

Read-only checks of the dirty occupation and transaction owners found existing storage for the public outputs at the inspected direct consumers: the external occupation delivery caller declares external proof, consumed crates and usable crates, and the occupied transaction caller declares consumed crates, usable crates and reserved proof.
These inspected consumers require no additional patch for the outputs audited here.
No edits were made to occupation, shared transactions, achievements, HQ effects, native debit measurement, threat logic, decisions, event files, AI weights, project gates or other owners' sources.
This is a bounded consumer audit, not a proof that every public output in the wider system is declared correctly.

## Meaningful source validation

Run from the repository root:

```text
node docs/testing/2026-10-09_automatic_protection_repair/automatic_protection_source_tests.js
```

The final run passed 58 cases with zero failures.
It imports the existing parser and VM from `docs/plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js` without editing that harness.
`VM.run` retains its conservative lexical cleanup: inherited temporary names survive and helper-created names disappear at return.
The fixtures do not silently preseed the missing internal outputs.
Both exact original and current production helper ASTs execute under the same explicit modeled native inputs.
Ten unchanged production helper ASTs are compared exactly, as is the entire reconditioning positive guard and random-list body.
Dependency hashes and individual results are in `docs/testing/2026-10-09_automatic_protection_repair/source_test_results.json`.

The cases cover:

- Military and controller-paid state filter service with zero, partial and full stock, including proportional restoration and reduced state/country replacement demand.
- No repeated stock charge after complete restoration.
- All five replacement models in oldest-first order, total conservation, and stopping partway through an advanced-model stock.
- Unchanged rapid-filter and contaminated-state service costs.
- Original missing-output failures, including stock debit without restored filter condition and fitting loss without credited damaged material.
- Military shortage competing with civilian service for the same 90 crates, with 90 crates issued to the army after the order correction.
- Actual production snapshot and readiness arithmetic, including readiness increasing from 27.5 to 41.25 or 55 for partial or full military restoration in the declared fixture.
- Historical quarter-force reserve preservation without threat and release with a declared threat, plus the existing quarter-requirement issue increment.
- Annual storage service on the twelfth cycle, cycle reset, and one scheduled maintenance event at the unchanged 30-day delay.
- Zero and positive useful delivery through the three corrected external/reserved wrappers, including proof and achievement-call reachability.
- Reconditioning with zero or positive material, both explicitly selected existing quality branches, and repeated completion with depleted material producing no additional draw or stock.
- Bare helper output loss and explicit outer storage surviving the producer, preserving the caller obligation as a negative control.

Native stock reads/removal/addition, one country and one controlled capital state, existence/control/core relationships, event scheduling, and five-decimal arithmetic are explicit fixture models.
Initializers are no-ops because the fixture supplies initialized data.
Unrelated designer/profile/project predicates are false, public threat is a declared input, and civilian issue need is false in the service-competition fixture.
Ancillary decontamination and ordinary achievement refreshes are no-ops.
External aid achievement invocation is recorded, not executed as a complete achievement system.
Reserved-wrapper cases stop at refund entry, retaining the real call but not modeling the full native refund pipeline.
The separate owner tests remain responsible for native refund and receipt behavior.
Forced selection of each existing random branch verifies guarded reachability and branch effects, not statistical probabilities.
No native stock delta receipt was invented or added to gameplay.

## MCP and references

Connected `hoi4.reference_context`, `reference_search`, `reference_read`, `source_lookup`, and `script_validate` were confirmed and called directly.
The context result omitted general Modifiers and Scopes references due to its bound.
Those irrelevant modifier rules are not claimed as coverage, and the required controller rule was retrieved directly.
No helper-expansion, job, task-negotiation, GUI, focus or map route was used.

| Reference path | Read lines | Source revision | Rule used |
| --- | --- | --- | --- |
| `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` | 435–443 | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` | Caller-declared temporary storage survives helper modification and remains unscoped. |
| Same Data structures snapshot | 425–434 | Same revision | Variable precision and object-reference semantics. Five decimals are a declared model limit rather than native execution proof. |
| `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md` | 2253 | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` | Dynamic equipment amount and stockpile removal, including producer/unlock caveats. |
| Same Effects snapshot | 272 | Same revision | State `controller` enters country scope. |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md` | 1252–1266 and 7820–7827 | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` | Country stockpile removal with negative variable amount, and any-scope temporary declaration. |
| Installed `documentation/script_concept_documentation.md` | 184–215 and 216–222 | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` | Fixed-point math-expression qualification and shared constants. |
| Installed `common/script_constants/documentation.md` | 1–34 | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` | Constant access and category/schema structure. |
| Installed `documentation/dynamic_variables_documentation.md` | 1112–1114 | `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda` | Controller reference. |
| Vanilla `common/scripted_effects/NOR_scripted_effects.txt` | 178–191 | MCP source-location revision `8d5050bb5b20466af83ecd46d3a46928bd8c136338e40101db44cab3cce02051` | `NOR_alt_dem_prep_start` uses a variable stockpile amount in an explicit country scope. |

The offline paths above resolve below `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/`.
Installed relative paths resolve below the stated vanilla game directory.
The parent captured the event baseline before edits at revision `283a550085362183c930b3e9508acd4051d381fab0d6edd4f1b8afac59de6889` and owns the graph/render artifacts and final comparison.
Its narrowed `cbrn_protection.1` render reported one node and zero helper projections, so it is partial structural evidence and does not establish helper lifecycle coverage.

Full military and state filter-service bodies were submitted to `hoi4.script_validate` under explicit country and state scopes.
The result is `SCRIPT_CHECK_PARTIAL`, `valid = null`, with syntax/command-kind/declared-scope checks only, unchecked parameter semantics, unresolved scripted helper names and omitted findings.
The connected tool accepts at most 32 findings, so requests above that bound were rejected rather than establishing additional coverage.
The qualified full-body packets are retained in `mcp_script_validation.json`.
An initial attempt incorrectly used a truncated `source_lookup` excerpt as a full snippet and returned unclosed-block diagnostics.
Those rejected excerpts are separately retained in `discarded_extract_validation.json`, and the complete local source bodies were then validated without those syntax errors.
No failure from the incomplete excerpt is attributed to production source.

The parent routed the restored reconditioning path to `/root/protection_reconditioning_probability` before its declaration patch.
That auditor owns the exact named conditional scenarios, immutable baseline, comparison and probability artifacts.
Its baseline reports an exact complete two-entry conditional pool at 20% defective and 80% safe, and explicitly excludes helper temporary-lifetime execution.
The source tests supply the bounded lifetime/reachability evidence, while the auditor supplies conditional odds evidence.
Its standalone render reported stale analysis because snapshot and workspace revisions differed, so no successful standalone probability render is claimed here.

## Exact bytes and recovery

Original raw bytes were captured before gameplay edits.
Both gameplay paths had unspecified `text` and `eol` attributes at capture.
Scoped evidence `.gitattributes` sets `*.before`, `*.after`, and `*.pre_reconditioning` to `-text` for byte-preserving archival, with no gameplay attribute changes.

| Source | Original SHA-256 | Final SHA-256 |
| --- | --- | --- |
| `cbrn_protection_effects.txt` | `278bbd01add94610a81b453ce3e2fbcd12003e737ed4a06eeb6af4184377d8f4` | `acb8cff1fa5d61392799aee62f2a3f98625f55c4dda36b806c22e91beaf75c4b` |
| `cbrn_protection_decision_effects.txt` | `3931110c80d36dce6379fb10dd87386720d391222f2ffbcdcaed659ece129b1b` | `bee3a3f81726bd9093e1244ce1bcc7c61d45081bb522994e3b2c5d56b627f506` |

The `.before` and `.after` files, unified diffs, byte counts and line-ending counts are in `docs/testing/2026-10-09_automatic_protection_repair/`.
Windows rejected direct truncate/write of the decision helper while a mapped section was open.
The source remained intact at the verified intermediate hash `c6e3916506961d312e759c7f7b00f8f3b8abf41b0c19054f039b59e726041637`.
A guarded same-volume `System.IO.File.Replace` installed the fully prepared source, retained `cbrn_protection_decision_effects.pre_reconditioning`, and verified the final hash above.
No process or game control was used.
Recovery details are in `source_metadata.json`.

## Simplifications, omissions, and blockers

No gameplay simplification was made.
The existing tuning, reserve policy, annual schedule, per-cycle issue increment, service cost formulas, donor/receipt gates, project gates and random weights are preserved in source and covered by the bounded cases and AST comparisons described above.
No source work within the authorized two-file patch remains blocked.
Canonical helper-documentation integration and parent-owned event/probability comparison review remain with the parent.
Native equipment behavior, actual callback scheduling, full refund execution, complete achievement effects, global helper-lifecycle coverage and in-game outcomes remain unproved.
The fixture assumptions and partial MCP coverage are validation limits, not alternate gameplay implementations.
HOI4 was not launched, and no logs or live-game action were requested.

Skills used: `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`.
Existing shared dynamic helper source and documentation were inspected before retaining the owner-specific helper family.
No skill was created or changed.
