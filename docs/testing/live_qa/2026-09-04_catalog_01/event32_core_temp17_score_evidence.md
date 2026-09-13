# Event 032 core temporary score evidence

Status: the parent applied the six authorized terminal cleanup deletions after the prepatch baseline. This bounded report contains no gameplay source edit by this auditor. The prepatch source SHA-256 was `9C856BA8C0D13C2A4E19C4E5BCDCEB00BFB91CD342018B7F58F2B61AEBECFA64`. The current source SHA-256 is `35D8C85E0C6FD7B7E1826135968AD5B2A2E1982D41CE6FB1D8D7CA7B52650903`.

## Scope and scenario

Analyzed surface: `missiles_score_site_candidate` in `common/scripted_effects/032_missiles_effects.txt`, scratch identifier `missiles_infrastructure_component`, and its caller `missiles_select_best_site`.

Scenario ID: `E32-TEMP17-B0`, source-discovery baseline with no injected runtime state, seed, cadence, or stochastic pool. The matching postpatch inspection is `E32-TEMP17-P1`.

The scoped source change is deletion of the prepatch terminal `clear_temp_variable = missiles_infrastructure_component` at line 642. No score branch, constant, eligibility gate, target assignment, or selector mechanic was changed.

## Mandatory probability baseline

The parent’s prepatch read-only `hoi4.probability_inspect` used source `{path: "common/scripted_effects/032_missiles_effects.txt", identifier: "missiles_score_site_candidate"}` with `refresh = true` in workspace `mod_chaos_redux_ea3b2d67c2c0`.

It returned `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason = no_weighted_surfaces`, `adapters = 11`, `candidates = 0`, `availableCandidates = 0`, `requiredInputs = 0`, and `unresolved = 0`.

The prepatch MCP source revision is `4049efc4bb2927d356a51c14849e9fe4974e338745cae55fae4f4cfd9391dbcf`, the MCP source hash is `44e175efb8bc6c80a38edd5f12c18aca56bc6e6aaccbbc6047466e0e936f30c8`, and the artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/42cc8ac8c9e6718a012d448bcaea502a672f066f82292363c3e69835abe4c7e4/5327eeac71e836981ba668ce2a921801035872c7fb2535415c0762f2047958e3/probability-inspect-44e175efb8bc.json`.

The matching postpatch read-only inspection returned the same `PROBABILITY_SOURCE_DISCOVERED` and `no_weighted_surfaces` result with 11 adapters, zero candidates, zero required inputs, and zero unresolved fields. Its source revision is `d01b0cd3369af2a9668e16e52291e40febfac25cf342b749e141ca38f3261df8`, source hash is `c63d821d83b6a1f961a5b13476c8dd440a6357f1cc624cd323212075afd6a7dd`, and artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/557dfe527692512bbb21336b51096f760111d94bb6f8640ddf522f8ddc9dbf3e/86951d54700adff1dca35ae81bf3078a771aa61b75726f6976a0e6f246d0d045/probability-inspect-c63d821d83b6.json`.

Both inspections prove that the installed probability adapter does not represent this helper as a weighted surface. `probability_evaluate`, `probability_sweep`, `probability_compare`, `probability_simulate`, `probability_sequence`, and `probability_render` therefore have no valid input contract for these scenarios. No exact selection probability, timing distribution, rank reversal, dominance, starvation, repetition, or snowball conclusion is claimed.

## Exact score and scratch trace

The prepatch scorer initialized `missiles_candidate_score` from `constant:missiles_site_score.baseline` at line 592. The relevant scratch sequence was:

```text
606 set_temp_variable = { missiles_infrastructure_component = infrastructure_level }
607 multiply_temp_variable = { var = missiles_infrastructure_component value = constant:missiles_site_score.infrastructure_step }
608 add_to_temp_variable = { missiles_candidate_score = missiles_infrastructure_component }
642 clear_temp_variable = missiles_infrastructure_component
```

After the parent’s combined six-line cleanup, the same three score statements are at current lines 601-603 and the terminal cleanup is absent.

The exact infrastructure contribution is `infrastructure_level * 5`, because `missiles_site_score.infrastructure_step = 5` at `common/script_constants/032_missiles_constants.txt:1000`.

The scorer’s source constants are `baseline = -100000`, `existing_rocket_site = 1000`, `existing_event_site = 500`, `core = 40`, `infrastructure_step = 5`, `supply_connection = 20`, `air_defence = 12`, `radars = 10`, `strategic_depth = 25`, `industrial_access = 8`, `secure_control = 15`, `different_region = 30`, `capital_penalty = -25`, `frontline_penalty = -100`, `occupied_penalty = -200`, `damaged_penalty = -40`, `island_penalty = -20`, and `resistance_penalty = -30`.

The prepatch helper read `missiles_infrastructure_component` only at line 608 after its unconditional set and multiply. The current helper has no read after line 603. The prepatch runtime search found exactly three assignments or uses plus the terminal cleanup, and the postpatch runtime search finds only the three assignments or uses. No other runtime source reads or writes this identifier.

In the prepatch line map, the caller initializes `ROOT.missiles_best_site_score` at line 695, iterates the dynamically filtered `every_owned_state` pool at lines 696-705, and invokes the scorer at line 706. After the six cleanup deletions, these caller points are current lines 689, 690-699, and 700. The scorer replaces the best value only under strict `greater_than` at prepatch line 637 and current line 632, saves the value at prepatch line 639 and current line 634, and saves the selected state as `missiles_selected_site` at prepatch line 640 and current line 635. The caller clears the regular best-score variable at prepatch line 708 and current line 702. The created-site path consumes only the saved event target at prepatch lines 778-781 and current lines 772-775.

This is a deterministic score race with first-iteration tie retention. It is not probability-proportional sampling. The actual runtime state pool and its iteration order were not supplied to an adapter, so selection probabilities and candidate rankings remain unresolved.

## Cleanup finding

The installed vanilla effects documentation documents `clear_variable` at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md:2773` and documents `set_temp_variable` at line 7820. Neither installed effects nor triggers documentation contains `clear_temp_variable`.

The offline `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md` variable table states that `clear_variable` can only be used on regular variables. The offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` variable-type section states that temporary variables live within their enclosing effect or trigger block and are not regular scoped variables.

The parent’s source check at `docs/testing/live_qa/2026-09-04_catalog_01/event32_core_temp17_source_checks.json` reports `exact_inverse = true` and `unchanged_other_bytes = true` for the combined six-line patch. Its patch record at `docs/testing/live_qa/2026-09-04_catalog_01/event32_core_temp17.patch` shows the Event 032 deletion as the exact prepatch line 642 statement.

The before and after source evidence supports an exact source data-flow and score-only equivalence for this scoped cleanup. The set, multiply, add, best-score comparison, target save, eligibility gates, constants, and caller continuation are unchanged. Every scorer invocation initializes the scratch before its only read. Replacing the unsupported command with `clear_variable` would be invalid for this temporary identifier.

## Candidate pool and external factors

The source declares the candidate eligibility filter, but no concrete state list was supplied to the probability adapter. Candidate-pool completeness is therefore incomplete for normalization and probability analysis.

The scorer’s external factors are the caller country scope, owned and controlled state status, impassability, existing rocket and Event 032 site flags, core and occupation status, neighbor ownership, infrastructure, supply node, anti-air, radar, railway, factories, capital status, island status, resistance, damage, strategic-region variables, and strict loop order. Their runtime values are unknown in `E32-TEMP17-B0`.

No scheduled state change, cadence, seed, uncertain-input distribution, or terminal sequence state applies to this scratch cleanup. The helper runs when called by the site-selection effects.

## Structural MCP context and limits

A read-only `hoi4.event_inspect` lint for selector `{kind: event, eventId: chaosx.nr32.1}`, both directions, helper expansion, depth 2, 25 nodes, and 40 edges returned `EVENT_INSPECTED_PARTIAL` at revision `410c82bea077b36a7e01b4ed11eb4927d40357359aad54622f2b2adf58fea5cb` with graph hash `49a5660f0be3001d24dbe45578fc9e8569b749750351677b102b889284c0ca79`. Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/92ee90530fbd4c49a5d6c43675267cc6e353e7610800811197fec43b4ceca37d/a93623a277207e723ad092d452eb0efa363eb1b0667fd1122c857f5b9273e939/event-lint-410c82bea077.json`.

That route deferred workspace helper and lifecycle projections, reported one blocking diagnostic, and exposed zero helper nodes in its bounded data. It is structural context only and does not prove the temporary-variable cleanup semantics. The exact source data flow above is the evidence used for this bounded recommendation.

## Skipped analyses and remaining uncertainty

`probability_evaluate`, `probability_sweep`, `probability_compare`, `probability_simulate`, `probability_sequence`, and `probability_render` were skipped for both scenarios because both mandatory inspections discovered no weighted adapter, no candidate pool, and no stochastic inputs. This is an exact MCP route limitation, not a substituted source-only probability claim.

The deletion’s score and current scratch consumer contract are resolved by source comparison. Live engine parsing and gameplay behavior remain outside this audit. Selection probability, timing, rank reversal, repetition, dominance, starvation, and exploit severity remain unresolved because the deterministic max selector has no installed probability adapter representation and no concrete runtime state pool was supplied.

## Parent startup acceptance

The parent subsequently reported completed, stopped, and archived native launch 18 with source SHA-256 `35D8C85E0C6FD7B7E1826135968AD5B2A2E1982D41CE6FB1D8D7CA7B52650903` stable.
All twelve repeated parser records for the six removed cleanup statements were absent, with no new diagnostic family beyond the aggregate-count record.
Live reserve-package and site-selection behavior remain untested.
