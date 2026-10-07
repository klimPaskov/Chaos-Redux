# HQ temporary-output source regression

Disposition: implemented bounded source checks, independently reviewed and rerun by the parent with 292 cases passing; native execution remains unproved.
Acceptance basis: the parent assigned strict-frame before/after tests for its caller-owned HQ output allocations and confirmed the source patch and freeze before execution.
The architect's `2026-10-07_hq_helper_lifetime_audit.md` was read before the final run.
The parent owns gameplay, MCP evidence, final integration, and the commit.

## Artifacts and result

Only the three assigned new artifacts were written:

- `docs/testing/2026-10-07_cbrn_hq_lifetime_source_tests.js`
- `docs/testing/2026-10-07_cbrn_hq_lifetime_source_results.json`
- This handoff.

Run from the mod root:

```powershell
node docs/testing/2026-10-07_cbrn_hq_lifetime_source_tests.js
```

The final run at `2026-10-07T13:59:13.754Z` exited 0 with 292 passing cases and `passed_conservative_helper_frame_model`.
It reproduces 275 baseline missing-output failures.
The doctrine test suite and historical handoffs were not edited.

The existing exported VM and parser from `docs/plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js` are reused unchanged.
Its `run` method retains a lexical frame for every scripted-helper call, discards only newly created temporary names on return, and preserves changes to temporary names already owned by an ancestor caller.
No global lifetime shortcut was substituted.
The local adapter keeps separate regular-variable maps for one saved character and its OWNER country, while temporary storage remains unscoped as documented.
The JSON records the imported VM hash, every audited source hash, fixture inputs, exact captured consumers, baseline failures, and reference revisions.

## Source preservation

The full HQ effect AST retains every original statement and its ordering after removing exactly 129 literal zero allocations.
Placement checks prove sixteen exact slots at each of the five starter entries, nine exact slots at each of the five upkeep-wrapper entries, and four exact completed-output declarations immediately before mask, decontamination, instrument, and motorized debit calls.
The shared family completion name is allocated separately before both family calls.
The comparison permits no unrelated statement change or broad stat/effect whitelist.

All eight baseline files match `docs/testing/2026-10-07_cbrn_hq_lifetime/baseline_manifest.json` at baseline commit `269215ef29d8f5b5e4d09865b0b475c7c8869bda`.
The seven captured dependencies other than HQ effects remain byte-identical: HQ triggers, HQ constants, native abilities, HQ events, progression effects, progression triggers, and progression constants.
Therefore prices, thresholds, schedules, role IDs, AI, equipment order, ability calls, and policy source in those captured surfaces remain unchanged.

| HQ effect revision | SHA-256 |
| --- | --- |
| Before | `5c6c5a4d174de2baa933f093e0368752194bcf061f3a9a063d7cd40211300832` |
| After | `eef1bceafc226b303d3568e7081bf4e2286cbb9a109ff6389538991852039a11` |

## Exact exercised scope

| Cases | Actual source exercised and result |
| --- | --- |
| 252 activation cases | Every five-operation starter across light/standard/mass bands, readiness 0, 39.99999, 40, 59.99999, 60, 79.99999, and 80, with commander discount present/absent. Decontamination also tests both truck-wash designer branches. Actual setters, force triggers, preparation arithmetic, min/max/floor, CP remainder, common package debit, and timer consumers receive their expected inputs |
| 18 upkeep cases | Every operation across three committed bands, plus both decontamination designer branches. Actual wrappers deliver all nine package fields, including intentional zero-cost fields, to the common debit helper |
| 6 mixed-stock cases | Requested 0, 1, 6, 15, and 30 against twelve available items per family, plus a distinct mixed-stock fixture. Actual oldest-first loops debit fixture models and return completed amounts to country ledgers |
| 10 final-tick cases | Actual `cbrn_hq.2` immediate branches for every operation with affordability true/false. Failed payment awards no receipt, removes benefits, and clears ticks. Successful final eligible orders record one character receipt. Protective posture remains outside the actual eligible-service OR |
| Consecutive-operation and duplicate-receipt case | Three operation starts leave no new temporary names after return. A two-tick decontamination order awards no receipt after tick one, one after tick two, and no duplicate on a stale third invocation |
| Planned-end checks within final-tick cases | Actual no-posture trigger remains false while the character operation code survives successful or failed upkeep. Explicit invocation of actual `cbrn_hq.3` immediate cleanup clears that guard |

Producer controls preallocate only the documented output contract in a separate fixture VM and run the actual producer helpers.
The tested starter and upkeep calls receive no harness-preallocated output repair.
Their literal declarations must establish ownership themselves.
Character readiness is deliberately seeded differently from OWNER readiness, and owner stock ledgers are checked separately from character operation/service state.

In every baseline activation case, returning package outputs reach the package consumer as zero and preparation scheduling receives zero days.
In every baseline upkeep case, package debit outputs similarly vanish.
The revised calls retain exact package values, CP total minus native minimum, preparation days, active duration, preparing-trait duration, recovery event days, and preparation-completion days.
Medical and manpower restoration event IDs follow the committed band and capture the unchanged preparation-plus-active duration.
Preparation itself creates no completed-service flag.

The mixed-stock tests isolate the nested completed-output defect by supplying the same outer package inputs to both source versions.
Physical stock debits remain identical, but baseline country completion ledgers remain zero after returning helpers.
The revised distinct-family fixture credits masks 3, decontamination 5, instruments 9, and motorized 4 from different requested amounts and available models.
The two family totals remain separate despite sharing the temporary result name.
Nested scratch/output names disappear after the debit returns, while only the test's explicitly owned package inputs remain.

One illustrative revised mass decontamination case with readiness 80, commander discount, and truck-wash design sends masks 400, decontamination 84, support 60, trucks 6, and fuel 900 to the debit consumer.
It captures CP remainder -35, preparing-trait duration 2, recovery event 3 after 30 days, and preparation event 1 after 2 days.
These are source-model arguments rather than observed game results.

## References and limits

The local reads match the exact requested revisions: offline `Data structures:435-443`, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`, and installed `effects_documentation.md:7820-7827`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
The former states the scripted-helper return caveat, caller-preinitialization guarantee, unscoped temporaries, and scoped regular variables.
The latter permits temporary assignment in any scope and does not independently guarantee return lifetime.
The existing 2026-10-06 helper-output regression was read as the reuse pattern.

Affordability, valid command, assigned-army-leader identity, and designer availability are explicit fixture inputs where native gates lie outside the tested transaction.
Force-band triggers themselves run from actual source using fixture battalion counts 99, 100, and 200.
The harness therefore does not establish native equipment sufficiency, HQ fill, policy authorization, or those predicates' full engine behavior.

Equipment effects update only fixture stock maps.
Mask snapshot refresh is a no-op, and filter-condition loss is a narrow requested-loss stub.
The full mask-loss/replacement subsystem is not simulated.
Native command-power, fuel, manpower, meta effects, and scheduled country/leader events are argument captures, not native execution.
Rounding uses a positive half-up integer convention, with no claim of native tie behavior.
Achievement commitment and earned-trait refresh are explicit no-op boundaries, while the actual receipt eligibility, completion flag, and service counters are exercised.

The event immediate blocks are invoked directly under controlled states.
Actual event timing, cancellation, cross-save target persistence, duplicate target identity, timed-trait expiration, later `.20-.25` restoration effects, and game scheduling remain unproved.
The preserved planned-end source guard is tested without inventing an old-event collision or a generation-system requirement.
Parent MCP before/after evidence remains separate, including the architect's partial trace findings.
The parent reported whole-file `script_validate` with `valid=null`, 642 checked commands, zero findings, 37 unknown-scope roots, and 446 unchecked argument blocks.
Those coverage limits do not establish native execution or replace this bounded source-frame evidence.
No MCP probability call, game launch, log search, gameplay edit, shared-VM edit, index write, or commit was performed by this worker.

No gameplay fallback or simplification was introduced.
The fixture boundaries above are explicit validation limits.
This completes the assigned source regression and does not establish whole-HQ-service or live-game completion.
Skills applied remain `chaos-redux-events` and `chaos-redux-subagents`, with no skill changes.
