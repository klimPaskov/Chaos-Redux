# Event039 retirement transaction fixture

Disposition: fixture implemented, 41 of 41 cases pass at the final recorded source hashes, with findings closed within the bounded source-execution model.
Authority is the parent request for validation files only on 2026-10-07.
Gameplay files, call sites, tuning constants, helper documentation, and Git index were not edited.
No commit was created.
Skills applied: `chaos-redux-events` and `chaos-redux-subagents`.

Changed files are `run_fixture.py`, generated `results.json`, and this `handoff.md`, all in this directory.
Run from the repository root with `python -B docs/plans/039_murder_mystery_plans/validation/retirement_transaction_2026_10_07/run_fixture.py`.
The process exits nonzero on a failed case or concurrent source change.
Each run reads the current source bytes, executes their parsed helper bodies, records SHA-256 hashes and helper source locations, then verifies that those bytes remain current at the end.
The result JSON records each case's row, roster, outcome receipt, executed helper scopes, native operation, and temp-frame cleanup.
It records cached `selected_target_retired` status separately from the fresh `target_consumption_committed` receipt.

## Initial findings and verified closure

The initial completed run passed 28 of 31 cases.
`stale_before_consumption_owner`, `stale_before_consumption_subject`, and `stale_before_consumption_role` failed.
In each case an injected registry mutation immediately before `murder_mystery_mark_selected_target_removed` still permitted consumption and retirement of the frozen victim.
The consume API matched ID, expected generation, disposition, protection, and used state, but did not compare owner, subject, or role against the validated selection.
The parent added exact owner and role comparisons in the matching row block, plus disposition-specific subject matching.
Named rows match their character, while generic-office and owner-managed rows match the recorded owner-country sentinel.
The parent reported the original 31 cases passing after that change at runtime-effects SHA-256 `63b6e982af58ba599c86eda7ab2512aefb994d4f81b938b898a7e527b926ee78`.
This subagent independently reran the expanded fixture against the same hash and obtained 35 of 35 passing cases with unchanged source bytes throughout execution.
The original three mutation cases passed in that rerun, closing the initial consume-identity findings within the fixture's stated model.
The four additional cases passed for matching and mismatching owner-country sentinels under both `generic_office_only` and `owner_managed` dispositions.
Each new case executes actual preparation, approval, eligibility predicates, and the same consume helper without entering ruling-character resolution or named retirement.
Matching sentinels consume only disposition, protection, and used fields and publish the consumption flag.
Mismatched sentinels leave the entire mutated registry unchanged and publish no consumption flag.
All four preserve every recruited roster and perform no native retirement.
These are adversarial API-boundary cases, and do not establish that the native engine yields or permits an asynchronous race at this boundary.

Public-selection overwrite during actual ruling-character helper execution and during the mocked native retirement both preserved the frozen victim outcome ID and generation.
Exact row rollback after failed native retirement, repeat rejection, and recursion guard preservation passed.
The first run's character-effects hash was `bd1a6ce62c1e1a4259939072a17d18b13d77205fb1947289ad6581b2722d66a1` and runtime-effects hash was `e65bd957dc1887c79743b589aa48aa5f77d07c52e8656a6b1b85c7bbd9722a19`.
Use `results.json` for the latest completed run's full hashes and individual results.

## R039-RET-01 audit finding and fresh-receipt verification

After the 35-case run, the parent reported an independent audit finding outside that run's coverage.
A used-only row or full tombstone introduced during ruling-character resolution could set cached `selected_target_retired` during revalidation and permit native retirement without calling the consume helper.
With a failed native no-op, rollback could then restore a tombstone created by another operation.
The earlier 35 passing cases did not cover either mutation at that boundary and did not establish safety for this path.
This subagent did not execute a pre-repair reproduction of R039-RET-01 because the parent requested waiting for the actual-source receipt repair before the final run.

The parent replaced the native-retirement gate with `murder_mystery_target_consumption_committed`.
The current source clears that receipt before the attempted mark, the actual mark clears its own inherited receipt and sets it only after consumption, and rollback clears it after restoring the transaction's row.
The parent also added the national-leadership role check at revalidation.
This subagent confirmed those actual source bodies before the final run, without injecting a repair or mocking mark success.

That verified run passed 40 of 40 cases with stable source bytes, retaining all four generic sentinel cases and adding role mutation at revalidation plus four R039-RET-01 variants.
Both used-only and full-tombstone mutations are injected inside the native trait-removal boundary while the actual ruling-character helper is executing.
Each mutation is tested with native retirement configured to remove the victim and with native retirement configured as a failed no-op.
Both configurations must reject before any native retire operation, so the failure setting is an adversarial environment configuration rather than an observed failed retire invocation.
Each variant also seeds an inherited stale consumption receipt during ruling resolution.
Assertions prove that revalidation's cached retired status is present, the fresh receipt is cleared, mark is never called, every roster is unchanged, no named-removal outcome identity is published, and the entire externally mutated registry remains unchanged.
The full-tombstone no-op case therefore explicitly checks that another operation's tombstone is never rolled back.

Verified character-effects SHA-256: `5034eed846bfa74d7e9726b298f7270a5d2c79d30a26a8d0d4a5cd889df7018c`.
Verified runtime-effects SHA-256: `ccfffd52c3ae4fe2f0d78a0f43296fd8bf8069cad63bfaa6cb112a433c4bcd36`.
The initial consume-identity closure and R039-RET-01 closure are separate evidence claims with separate source hashes.

## Final unique-ID consume invariant

The parent strengthened actual mark to count matching IDs before any registry mutation, require exactly one match, then validate the complete payload at the resolved index.
The added `duplicate_ID_before_MARK_rejected_without_mutation` case changes only the second row's ID to the current selected ID immediately before actual MARK invocation.
The second row retains its different generation, owner, subject, protection, and other payload fields.
The scenario therefore tests ID uniqueness independently of full-payload uniqueness, while the first row remains an otherwise valid consumption candidate.
Assertions verify that MARK executes once, both complete registry rows remain exactly as injected, neither row becomes used, no roster changes, no native retire operation executes, no consumption or named-removal success receipt is published, and the private fields and helper-created temps are cleaned up.
The result JSON now retains both complete registry rows for every case.

The final run passed 41 of 41 cases with source bytes unchanged throughout execution, retaining R039-RET-01 and generic4 coverage.
Final character-effects SHA-256: `d555e20b0ea68b5e363af0456632a96e03cb4dee169c986a724a67ac25f89c0e`.
Final runtime-effects SHA-256: `39ac5ebab51c69a5b830fbd046bf5eb4a2d94b3c11ce208e5c69e59240bd3fcd`.
Hashed integration boundary SHA-256: `8637b23cb3b6ba35757fcaaef1e63ddf5e110f204cc5c43fe1f1abd0990c4d87`.
No pre-strengthening duplicate-ID reproduction was executed by this subagent.
This final case establishes the explicit unique registry ID invariant at the consume API only within the stated mock execution model.

## Executed cases

- Different calling country, victim owner, and ROOT, plus owner calling with unrelated ROOT.
- Successful native roster removal and registry consumption, followed by rejection of a second call.
- Stale expected generation, protected, temporarily protected, permanently protected, owner-managed, disposed, and used target rejection.
- Unresolved successor and successor identical to victim rejection.
- Failed native retirement preserves the roster and restores the entire registry, including the exact original row protection.
- Registry generation, owner, subject, role, disposition, and protection mutate during ruling resolution before frozen-selection revalidation.
- R039-RET-01 used-only and full-tombstone mutation during ruling resolution under native-removal and failed-native-no-op configurations, with stale receipt clearing and external tombstone preservation.
- Registry generation, owner, subject, role, disposition, protection, and used status mutate immediately before consumption.
- A duplicate selected ID is introduced in the second row immediately before actual MARK, retaining different generation and owner, and neither row is consumed.
- Public selection overwritten at ruling resolution and native retirement, with immutable outcome ID and generation assertions.
- Recursive entry at ruling resolution and native retirement, with checks that the inner rejection preserves the outer guard and private saved inputs.
- Caller-preinitialized temp storage survives nested helper returns and is then cleared by its caller, while helper-created temps disappear.
- Matching and mismatching owner-country sentinels for generic-office and owner-managed consumption, with no character selection or retirement.
- The fixture rejects an unsupported statement even inside an unreachable branch.

All transactional success and rejection assertions include cleanup checks for normal private `murder_mystery_removal_*` fields, the global guard, ruler authorization, the native anchor trait, and helper-created temps.
Regular private event-target aliases deliberately persist for the owning effect chain, as documented, and are not claimed to be manually cleared at helper return.

## Bounded environment and assumptions

The six effect bodies executed are `murder_mystery_retire_selected_leader`, `murder_mystery_mark_selected_target_removed`, `murder_mystery_capture_current_ruling_character`, `murder_mystery_prepare_safe_target_action`, `murder_mystery_validate_selected_target`, and `murder_mystery_approve_selected_target_owner`.
Their seven selected scripted-trigger dependencies also execute from actual source, including recruited-roster identity, named/generic eligibility, registry alignment, and runtime flags.
No external scripted helper in this selected closure is replaced by an unconditional success stub.
An added helper outside that explicit closure or an unsupported statement or argument block fails validation rather than being ignored.
The reused `.tools/3d_pipeline/runtime/clausewitz.py` parser is read-only and preserves repeated keys and source lines.

The external owner callback and successor installer are preconditions, not executed helpers.
The fixture seeds an approved owner callback and a registered founder row whose ID is 390003 and generation is 17, while keeping a distinct untouched second row.
This deliberately exercises the existing cross-country founder authorization using the actual validation code.
It does not establish that a real callback or successor installer produces those preconditions.
The generic cases instead use the owner as caller, a separate dynamic row ID, the cabinet role, and the owner-country subject sentinel.
They run actual validation and callback approval before direct consumption, with a mismatching case replacing only the subject sentinel with another valid country after preparation.
No character target or prevalidated eligibility is seeded for those cases.
Mismatching generic cases also seed an inherited consumption receipt before direct mark, which must clear it and refuse to publish a new receipt.
These cases prove bounded registry consumption and do not execute casualty accounting or the external callback that grants approval.
All fixture characters are assumed to have a country-leader role, and only the configured ruler receives the temporary selection-anchor trait.
The native country trait operations affect that configured ruler synchronously.
An unresolved ruler makes those native trait operations no-ops for the explicitly declared failure case.
`any_character` and `every_character` enumerate the configured recruited roster, and character identity uses exact mock object identity.
Country existence is explicitly configured through the mock country/roster objects.
Native CHARACTER `retire = yes` either synchronously removes the exact character from its roster or is an injected no-op failure.
No native job safety, retirement side effects, successor promotion, ideology handling, event scheduling, save persistence, or live engine behavior is inferred from these operations.
The synchronous hooks are adversarial mutations or recursion injections at named source/helper/native boundaries.
They are scenario inputs, not discovered engine callbacks.

ROOT is fixed to a third country across all scope entries, PREV tracks actual scope nesting, normal variables and flags belong to their current country or character, global registry arrays are separate, and temporary variables are unscoped.
Every scripted effect or trigger call snapshots existing temp keys and discards only temps first created in that returning frame.
Existing caller-owned temp modifications persist through nested calls.
The explicit caller-storage case clears its own temps only when its owning caller lifetime ends.
There are no temporary arrays in this selected helper closure.
Regular and global event-target stores are separate.
Regular targets survive helper returns within the mock caller's effect chain, while global target clearing only clears the global store.
Arithmetic in the executed transaction is integer comparison and increment over two rows.
This fixture provides no fixed-point range or precision evidence for unrelated math.
The native 1000-iteration loop ceiling is enforced, and an independent fixture instruction budget fails closed on nontermination.

## Caller boundary and limits

`common/scripted_effects/039_murder_mystery_integration_effects.txt:549-557` invokes retirement and publishes opening leader removal/successor flags only under `murder_mystery_named_removal_committed`.
The opening commit at lines 562-584 checks those published flags before setting opening transaction receipts and applying mapped opening Chaos.
That integration file is hashed in the latest results but its opening chain and Chaos helper are not executed by this fixture.
This is a source boundary observation, not an accounting execution result.
No probability, focus, GUI, map, Part18, or full-character-safety completion claim is made.
No gameplay simplification or fallback was applied.
The mock-native limitations above are deliberate fixture bounds authorized by the parent request.

## Reference and MCP evidence limits

Connected metadata exposed `hoi4.event_inspect`, `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, and `hoi4.source_lookup`.
The attempted read-only batch requested `event_inspect` with `mode = trace`, selector `{ kind: event, eventId: chaosx.nr39.1 }`, depth 1, ten nodes and ten edges.
It also requested event reference context for temp lifetime, ROOT/PREV, and character retirement, wiki search for `Temporary variables`, and installed-doc search for `retire_character`.
The batch remained pending without returning observable results and was terminated after repeated bounded waits.
Individual completion and service health therefore remain unresolved.
No returned MCP artifact, source revision, render, comparison, or engine validation is claimed.
Required reference rules were read locally, with file SHA-256 used as the local revision identity.
No standalone viewer, job, native task, or fallback engine analysis was used.

Local sections read:

| Source | Lines | SHA-256 |
| --- | --- | --- |
| `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` | 263-290, 300-315, 436-448 | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md` | 251-265 | `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` |
| `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md` | 4683-4702 | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` |
| Installed `documentation/effects_documentation.md` | 1008-1021, 5946-5957, 6427-6457, 6496-6517, 7820-7841 | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| Installed `documentation/triggers_documentation.md` | 1272-1289, 5345-5353 | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| Installed `documentation/script_concept_documentation.md` | 216-258 | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| Installed `common/script_constants/documentation.md` | 1-55 | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` |
| Installed `common/scripted_effects/SOV_scripted_effects.txt` | 4218-4234 | `cc9e16837afa1428d11e053dc982446b35587980daa011a1df12114c3ace2bf4` |

Installed paths are under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`.
The vanilla precedent applies `retire = yes` inside the named character's scope.
These references support the stated mock contract and do not verify its native execution.
No fixture failure remains at the recorded source hashes.
Remaining parent work is to review the explicit assumptions and retain the missing MCP evidence separately from fixture evidence.
Native engine behavior, generic casualty accounting, opening Chaos accounting, Part18, and full-character-safety completion remain outside this fixture's evidence boundary.
