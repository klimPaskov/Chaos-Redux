# Legacy cost core implementation, 2026-10-03

> **Current-status disposition (2026-10-06): superseded by** [takeover_status_2026-10-06.md](../takeover_status_2026-10-06.md) for current famine and migration status.
> This dated document remains historical evidence, with its original acceptance basis, source snapshot, audit outcome, and validation limits scoped to the work described below.
> This reconciliation grants no new design acceptance and upgrades no historical evidence to current or native validation.

Disposition: implemented bounded core, pending parent integration and native/probability evidence.
Acceptance basis: the parent accepted [legacy_cost_affordability_parent_acceptance_20261003.md](../legacy_cost_affordability_parent_acceptance_20261003.md), reviewed the [architecture handoff](legacy_cost_transaction_architecture_20261003.md), and explicitly assigned this agent only the five new core/API files and this new report.
The source audit and [probability baseline](legacy_cost_affordability_probability_20261003.md) were read before editing.
The wider cost correction and famine/migration goal are not claimed complete.

## Files changed and ownership

All six files are new.

| File | Owned result |
|---|---|
| `common/script_constants/humanitarian_legacy_cost_constants.txt` | One fixed-point category with 15 positive fees and 15 paired debit values |
| `common/scripted_triggers/humanitarian_legacy_cost_triggers.txt` | 15 pure inclusive resource predicates and 18 complete spent-tuple predicates |
| `common/scripted_triggers/humanitarian_legacy_cost_triggers.md` | Complete Boolean API contract, component table, 18-profile/25-decision mapping and examples |
| `common/scripted_effects/humanitarian_legacy_cost_effects.txt` | One COUNTRY display-only quote projection effect |
| `common/scripted_effects/humanitarian_legacy_cost_effects.md` | Explicit effect scope, inputs, outputs, defaults, side effects, lifecycle, examples and limits |
| This handoff | Acceptance, implementation, test results and remaining owner/evidence boundaries |

No existing source, selectors, YML, phase provider, receipt helper, workbook, completed handoff, index, or commit was edited by this agent.
No debit primitive, flag, global target, cleanup hook, paid-action registry, framework, AI factor or cost retune was added.
No staging or commit was performed.
The decision owner and parent retain their concurrent work.

## Final identifiers and behavior

The category is `humanitarian_legacy_cost`.
Its complete positive key set is `pp_light`, `pp_standard`, `pp_heavy`, `train_light`, `train_heavy`, `convoy_light`, `convoy_heavy`, `support_light`, `support_heavy`, `infantry_light`, `infantry_heavy`, `fuel_light`, `fuel_heavy`, `transport_planes`, and `air_xp`.
Each has a `<key>_debit` entry equal to its negative.
Values retain 10/20/35 PP, 5/10 trains, 5/10 convoys, 50/100 support equipment, 100/250 infantry equipment, 500/1000 fuel, 5 transport planes and 10 air XP.
No new value or spend type was introduced.

Each component is `humanitarian_cost_<key>_is_affordable` and each complete tuple is `humanitarian_cost_<profile>_is_affordable`.
All have COUNTRY payer scope, Boolean calls with `= yes`/`= no`, no parameters or temporary outputs, no stored-quote input, no implicit payer/default amount and no side effects.
They use one `NOT` around one native less-than resource comparison per component.
Every profile AND-composes the exact component set.
Native equipment tokens stay `train_equipment`, `convoy`, `support_equipment`, `infantry_equipment` and `transport_plane_equipment`.
No model-specific equipment token was substituted.

The final profile labels are:

```text
pp20_support50_fuel500
pp20_convoy10_fuel500
pp10_train5_fuel1000
pp20_convoy10_support50_fuel1000
pp20_planes5_fuel1000_airxp10
pp20_convoy5_fuel500
pp20_train10_fuel1000
pp20_train5_fuel500
pp10_infantry100_fuel500
pp10_train5_fuel500
pp20_infantry250_fuel1000
pp20_train10_fuel500
pp35_infantry100_fuel500
pp20_support100_infantry100
pp10_convoy5_fuel500
pp20_support100_fuel500
pp35_train5_convoy5_fuel500
pp35_train10_fuel1000
```

The exact 18-profile to 25-decision mapping and constituent component keys are in [the trigger API](../../../../common/scripted_triggers/humanitarian_legacy_cost_triggers.md#profiles-and-direct-decision-consumers).
The parsed-source test independently declared that same expected mapping and rejected a missing, extra or reordered tuple component.
The airlift profile explicitly includes the 10-XP component.
Workers' profile contains PP20/train10/fuel500 only, leaving the strict support50 non-spend prerequisite to its unchanged owner.
The separate strict AI-only50XP modifier is outside this API and unchanged.

The sole new effect is `humanitarian_project_legacy_cost_quote = yes` in COUNTRY scope.
It assigns 15 normal country variables `humanitarian_cost_quote_<key>` from their fresh corresponding positive constants.
It has no caller inputs, return temporaries or default inference.
It overwrites only those display fields, can be repeated at unchanged tuning, and repairs stale display values.
Affordability and owner payment/refund paths must read fresh constants, never these cached display fields.
It has no payment, policy, reveal, receipt, service or population effect.

## Meaningful validation run

An in-memory Python test parsed the actual three production TXT files into Clausewitz-style key/operator/value ASTs.
It evaluated the production component/profile bodies with mocks limited to native PP, fuel, air-XP and equipment reserve readers.
It processed the actual quote body's `set_variable` assignments in separate mock country dictionaries.
The evaluator rejected unsupported commands instead of replacing a helper with a no-op.
No test or helper file was created outside the explicit ownership list.

The first invocation failed before running tests because Windows command-line quoting damaged a double-quoted token regex passed through `python -c`.
The corrected invocation piped the same bounded test program through standard input with `python -`, avoiding native argument quoting, and completed with exit code 0.
This was a test-launch correction, not a source change or passing native-engine result.

| Production-source check | Result |
|---|---|
| Central first-entry schema, exact 30-key census, preserved 15 positive values and positive/debit negation | 15 pairs pass |
| Every component at zero, one short, exact and one above | 60 cases pass, blocked/blocked/ready/ready |
| Every profile with all reserves zero, all one short, full exact tuple and all one above | 72 cases pass |
| Each individual profile component at zero or one short with every other component exact | 114 cases pass |
| Exact profile with every display quote poisoned to -999 | 18 cases pass, cached quote cannot affect the parsed gate |
| Every profile after positive tuning is increased by 7, exact then first component one short | 36 cases pass, predicates read the changed central values |
| Actual quote assignments match the exact 15 positive table entries and changed central table | Pass, 15 distinct normal display writes |
| Repeated quote projection, separate-country isolation and stale quote repair | Pass |
| Actual 33-trigger identifier set and independent 18-profile composition map | Pass |

The combined profile boundary/poisoned-quote count is 204, separate from the 36 central-mutation cases.
These are source-level reserve boundary results.
They establish no native parser, engine stockpile aggregation, paid action, transfer, callback, native click, layout fit or AI probability outcome.
Payment, receipt and refund cases are not tested here because their source ownership belongs to the decision worker.

Production TXT SHA-256 revisions tested:

| Path | SHA-256 |
|---|---|
| `common/script_constants/humanitarian_legacy_cost_constants.txt` | `44ebd402a9b1868e26863666f8aeff5da70d2b5b862f6e0721507229f19d0496` |
| `common/scripted_triggers/humanitarian_legacy_cost_triggers.txt` | `f8aef44112e5cce33a0213a3877b555a3678deb3343c0291c8e56bbbe6a72eaf` |
| `common/scripted_effects/humanitarian_legacy_cost_effects.txt` | `61dc8c2a4251c197bcfae5072799f837e43de537248d29aa48100e740276e38e` |

## References and MCP limits

Reference sections were read in the architecture pass and applied here.
Offline `Triggers:2359-2400` and `Effects:4683-4715` document Boolean scripted helpers, while `Data structures:435-449` distinguishes normal scoped display variables from temporary storage.
Installed `documentation/script_concept_documentation.md:216-245` and complete `common/script_constants/documentation.md` document shared fixed-point constant support and first-entry schema.
Installed `documentation/triggers_documentation.md:3073-3081,3835-3842,3957-3966,4547-4554` documents the exact COUNTRY native readers.
The current Open Reception precedent is `migration_reception_preparation_triggers.txt:4-10` and the existing bounded quote precedent is `migration_decision_phase_effects.txt:6-17`.
The relevant source paths and exact reference revisions remain in [the architecture evidence table](legacy_cost_transaction_architecture_20261003.md#evidence-unsupported-fields-and-limits).

The connected tool list exposes the reference, source, decision and probability routes, but no `hoi4.script_validate` route is exposed in this session.
No expensive reference/MCP retry was made after the parent's recorded reference timeouts and accepted source-only tranche.
The baseline `decision_ai_will_do` source discoveries returned `requested_adapter_empty`, and the one suggested mission adapter returned `INTERNAL_ERROR`.
The before archive is committed at `e6ec73bcf26a43e400353a4e2d07ba9b8d35aea8`, with all 12 raw blobs verified by the parent.
These results, the artifact URIs and the mandatory comparison obligation are preserved in [the probability baseline](legacy_cost_affordability_probability_20261003.md).
No same-named probability comparison is established here, and source tests do not waive it.

## Remaining owner work and limitations

The decision owner received the fixed IDs and APIs before integration.
It owns all 25 decision gate/debit consumers, complete start guards, 20 delayed paid receipts, negotiation pending/deferred guards, exact relief setup stock checks and cleanup.
The parent owns all 15 resource selectors and ready/blocked YML values, quote phase/registration call sites, public API index/permanent docs integration, final review, required source/engine evidence and publication.
This core adds no call site to an existing file because the explicit ownership division assigns those consumers to the parent and decision owner in this same authorized tranche.
It is not standalone scaffold completion of the wider repair.

Native constant parsing for the specific reader fields and actual stockpile archetype aggregation remain unverified.
Click-time revalidation, native callback identity/exclusivity, same-payer ABA, failed-click cooldown, delayed cancellation and inline presentation remain outside this core's evidence.
No game or logs were accessed.
No fallbacks, fee reductions, hidden resource omissions or simplifications were made in this bounded core.
There are no new icons, assets, categories or public metrics.

Skills applied: `chaos-redux-events`, `chaos-redux-decisions-missions` and `chaos-redux-subagents` from the preceding architecture work.
No skill was changed.
