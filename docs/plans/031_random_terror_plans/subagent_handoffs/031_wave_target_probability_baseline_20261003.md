# Event 31 wave-target probability baseline

Status: interim read-only source baseline and named scenario fixture delivered before the parent ROOT/helper-output patch. No gameplay, AI, weight, or balance source was edited. No source-only conclusion is presented as an MCP probability result.

## Scope and authority

The scope is the Event 31 automatic wave country-ticket curve, ROOT/THIS scope preservation, state-site eligibility, provider-load factors, self-provider exclusion, temporary helper outputs, reservations, successful-site accounting, and shared scenario callers.

The architecture findings and source receipts are in [031_wave_scope_and_helper_contract_audit_20261003.md](031_wave_scope_and_helper_contract_audit_20261003.md). That handoff was read in full before this audit. Its planned ROOT and helper-output edits remain recommendations only. Parent commit `04689ecb13f203945be130d461fdf4eb957c043b` already owns the `random_terror_wave_target_count` caller initialization and it is not proposed again.

The named scenario fixture is [031_wave_scope_probability_scenarios_20261003.json](../evidence/031_wave_scope_probability_scenarios_20261003.json), SHA-256 `C211340E65576247901EDEA1CB8308A0EB65718575F83FD7194CDBFCF3401B18`. It preserves all required `wave_*` IDs and adds bounded `wave_load_case_0` through `wave_load_case_3` direct-curve traces.

The fixture uses only the known `schemaVersion`, `id`, `scenarios`, `label`, and primitive `state` envelope. Typed R/A/B/C country scopes, state owners/controllers, and provider-predicate bindings appear descriptively in labels because the connected probability route exposes `scenarioSet` as `unknown` and did not return a nested accepted schema. Do not treat the labels as analyzer scope bindings.

## Immutable before-source receipts

All eight parent-created physical before copies were present and were hashed without overwrite. Each hash matched its current worktree source at the start of this audit, and the scoped `git status` check reported no wave-source edits.

| Before and corresponding current source | SHA-256 |
| --- | --- |
| `common\scripted_effects\031_random_terror_effects.txt` | `8EDD15C352B0B4A8143B7A391078B5B6C0A01A41FE64FEA73CC86CED7B68B37A` |
| `common\scripted_triggers\031_random_terror_triggers.txt` | `3848A99005E8111A45B4BD49EF9C0821ACCD0C41029AAA5B1440182A685089C7` |
| `common\scripted_effects\individual_crisis_targeting_effects.txt` | `903562C1DC27BF9367E5A8AB8A807047A798FB16DE0BD8E1DF2841B6A2C40B16` |
| `common\scripted_effects\individual_crisis_targeting_effects.md` | `014ABB19AEF88D1821A10EC63BA16BE0A35A96B85D5B65B5A1B27DC0F62B8155` |
| `common\scripted_triggers\individual_crisis_targeting_triggers.txt` | `AF537F93E969948CA5CB35E1D06C504F6797CCBAAF659A13C9A661DB8E510B70` |
| `common\script_constants\individual_crisis_targeting_constants.txt` | `8B4471A8412E3A883570743E0EE17037129DCEAA889D63781AC8FC2C3529E002` |
| `common\script_constants\031_random_terror_constants.txt` | `84AECCA5BE338433A9A9BF2BFBA5682BE8256D790A6940E1C5561D7705EA09B8` |
| `events\031_terrorist_attack.txt` | `8EA0D99D25C62DE0A4BE6F8D9A64CD827E7F575E158A01C6832A038B84C311BE` |

Repository `HEAD` was `e5ff42fed484247230567e3f64ce71790bbe1f15` at the source check. The parent-provided copies remain the later comparison `before.path` authority; the matching live files are the after paths only after a reviewed owner patch. Do not compare the identical current files to themselves.

## MCP ledger and classification

The first required request was `hoi4.probability_inspect` with adapter `custom_weighted_pool`, source `{path:"common/scripted_effects/031_random_terror_effects.txt"}`, and `refresh:true`. It returned `timed out awaiting tools/call after 600s` and produced no artifact, source revision, candidate pool, or scenario hash.

The narrower retry used the same adapter with source `{path:"common/scripted_effects/individual_crisis_targeting_effects.txt"}` and `refresh:true`. It returned the same 600-second timeout. No candidate-specific retry can be grounded because neither inspect returned candidate identifiers. The shared helper file is the smallest source-only weighted adapter target identified from the handoff; inventing `candidatePool` or `customPoolManifest` fields would not be valid evidence.

A `hoi4.probability_evaluate` request was submitted for adapter `custom_weighted_pool`, that exact shared-helper source path, the parsed on-disk fixture object, metric `raw_value`, and outputs `json`, `matrix`, and `unresolved`. It returned `timed out awaiting tools/call after 600s` and produced no artifact, source revision, or scenario hash.

No `probability_sweep`, `probability_simulate`, `probability_sequence`, `probability_compare`, or `probability_render` artifact exists. Sweeps and normalized pool claims are blocked by the missing complete live candidate pool, typed scope/provider binding schema, and transitive provider-definition freeze. No sequence manifest or cadence was asserted. The custom `beforeManifest` helper closure is unvalidated and remains unresolved.

The fixture's candidate sets are complete only as declared synthetic test cases in their labels. They are not a complete campaign-world country pool. The four-candidate load case is a complete synthetic A/B/C/D ticket example, but owner/controller bindings and the other thirteen provider results have not been accepted by MCP. No exact selection probability or normalized share is claimed.

## Exact source-contract findings

### Candidate scope and ROOT

In `events\031_terrorist_attack.txt`, hidden entry event `chaosx.nr31.1` receives a country ROOT. The event calls `random_terror_run_global_wave` once; its country loop then changes THIS to candidate country C. Calling a scripted effect or trigger does not re-root the event, so ROOT remains receiver R and THIS is C.

`random_terror_country_is_normal_target` enters `any_owned_state` for C but checks `is_controlled_by = ROOT`. `random_terror_country_has_valid_state` repeats that receiver-relative controller test. After country C is chosen, `random_owned_controlled_state` selects a state owned and controlled by C, but `random_terror_state_is_valid_target` then tests ownership/control against ROOT. For distinct R and C, this can admit C only through a state controlled by R and then reject C's ordinary C-controlled site.

The architecture handoff grounds this scope contract in offline `Scopes` lines 260-263, `Effects` scripted-helper lines 4683-4695, `Triggers` helper lines 2359-2395, and installed vanilla precedents `events/WTT_Germany.txt` 3919-3944 plus `common/scripted_effects/00_scripted_effects.txt` 109-124, and `events/BBA_ItaloEthiopianWar.txt` 697-726 plus `common/scripted_triggers/00_scripted_triggers.txt` 308-319. This is source, offline-reference, and installed-precedent evidence; no live MCP scope trace returned.

### Ticket curve and self-provider exclusion

`random_terror_add_current_country_to_wave_target_pool` sets `individual_crisis_candidate_base_weight` to `constant:random_terror_value.one` for each eligible country. It selects the existing-provider helper for a country with an active Event 31 package and the ordinary helper otherwise, then appends one repeated country ticket per adjusted whole weight.

`individual_crisis_targeting_constants.txt` sets the fixed curve to `load_zero_tickets = 4`, `load_one_tickets = 2`, `load_two_tickets = 1`, and `active_cap = 3`. The shared helper uses the load-zero, load-one, or load-two curve only while derived load is below three; load three or more contributes no candidate tickets. These are exact raw source ticket settings, not normalized selection probabilities.

The existing-provider public helper sets `individual_crisis_exclude_random_terror = one`, calls the shared worker, then resets it to zero. `individual_crisis_load_is_below_cap` adds the Event 31 package as one boolean provider marker only when exclusion is not set. Two active Event 31 states therefore contribute one provider marker, and an existing Event 31 package excludes that one contribution once while preserving every other provider marker.

The derived load checks fourteen provider lifecycle markers: Holy Realm, Soviet Collapse origin, Fury, Secret Alliance, Natural Disaster, Utopia Manifesto, Brilliant Scientist host, Resources Found, Random Civil War, Video Game in Sweden, Riches Found mine, Time Traveler, Random Terror, and Murder Mystery original host. Several are transitive scripted predicates or state scans. The supplied before set contains the shared load trigger, not a frozen copy of every transitive provider definition, so the dependent helper closure and protected-identity proof remain incomplete.

### Site validity, reservations, and pacing

The country candidate gates require a surviving ordinary target, no reservation or incompatible route, and at least one positive-population owned state outside cooldown and controlled by the candidate. The state-site helper checks positive population, cooldown, lost-local-control, and an owner/controller relationship to ROOT. That last relationship conflicts with the later candidate-owned-and-controlled state iterator for a country C distinct from receiver R.

`random_terror_select_and_apply_wave_target` rebuilds the weighted country array for each attempt, selects one country, sets its two-day reservation before selecting a valid owned-and-controlled state, applies an incident if a valid state is found, and clears the array. A failed final state selection can therefore reserve a country without increasing the successful-application count.

`random_terror_run_global_wave` uses one `for_loop_effect` whose source endpoint is exclusive, with tier attempt counts 3, 5, 7, 10, 15, and 20 and a scenario override. A short candidate pool or failed site application can yield fewer successes than attempts. History and pacing remain on the single root event path; this audit does not add a pulse per candidate or per incident.

## Findings by named scenario

| Scenario | Explicit semantic inputs | Pool/completeness and source baseline |
| --- | --- | --- |
| `wave_three_countries_root_a` | R=AAA; complete synthetic candidate set AAA/BBB/CCC; each has one positive-population matching-owner/controller site; provider load zero. | Synthetic pool declared complete, typed bindings unaccepted. Current ROOT tests favor R and can suppress BBB/CCC. No normalized share. |
| `wave_root_ineligible` | R=AAA has no valid site; BBB/CCC do. | Synthetic pool declared complete, typed bindings unaccepted. Current receiver-rooted site checks can yield an empty pool. |
| `wave_foreign_owned_root_occupied` | R=AAA controls BBB-owned `B_OCCUPIED`; BBB also has `B_HOME` owned/controlled by BBB. | Synthetic candidate BBB declared, owner/controller bindings unaccepted. Candidate admission and final site validation can disagree. |
| `wave_load_0_1_2_3` | A/B/C/D have base one and provider loads 0/1/2/3 respectively; all sites otherwise valid. | Four-candidate synthetic pool declared. Source raw tickets are 4/2/1/0; transitive provider results, typed scopes, and normalized shares unresolved. |
| `wave_load_case_0` through `wave_load_case_3` | Direct helper inputs base one and active-load value 0, 1, 2, or 3. | Bounded direct-curve inputs only; not live provider-state proof. |
| `wave_existing_provider_exclusion` | BBB has an active Event 31 package in two states plus one other provider marker. | Confirms the source contract of one boolean self-provider exclusion; scope/provider evaluation unresolved. |
| `wave_helper_return_frames` | Tests absent nested temp/output and array storage against conservative caller-owned frames. | No engine lifetime proof; result unresolved. |
| `wave_helper_return_frames_caller_owned` | Describes initialized caller outputs and caller-created-then-cleared pool storage. | Proposed safe call-frame fixture, not current source or runtime proof. |
| `wave_identity_invariance` | Pair differs only by religion, ethnicity, nationality, refugee status, and ordinary ideology. | Direct curve has no such fields. Transitive provider closure and paired MCP comparison unresolved. |
| `wave_population_cohort_invariance` | Pair differs only in positive population and cohort sizes. | Base is a constant one; population is a validity gate in direct source, not a ticket multiplier. Transitive MCP proof unresolved. |
| `wave_site_rejections` | Separates zero population, cooldown, lost control, reservation, incompatible/special target, and valid site. | Synthetic outcomes declared; typed state bindings and full-world completeness unresolved. |
| `wave_short_pool` | Three attempts; only two valid site-capable countries. | Successful count should be bounded by real successful sites; selection trace unresolved. |
| `wave_distinct_countries_once_pacing` | One root firing, three attempts, three valid countries, two-day reservation. | Static one-firing case only. Cadence/removal/reset/terminal manifest incomplete, so no `probability_sequence` claim. |
| `wave_scenario_shared_callers` | Scenario host RRR differs from target countries AAA/BBB/CCC; scenario target, extra-state, and actor-parent paths. | Caller scopes and complete scenario pools unresolved; preserve each caller's existing scenario semantics. |

For all scenarios, the fixture records narrative typed bindings in labels because no accepted typed-scope schema was returned. External provider results, state owner/controller bindings, complete campaign candidate pools, and helper-return allocation state are unresolved rather than defaulted.

Evidence-class summary for every named scenario: the raw ticket constants, base weight, trigger gates, and scope call sites are exact source observations. Each end-to-end pool result, eligibility trace, distinct-target count, provider-derived load, or selection probability remains unresolved. The `wave_load_case_*` entries are bounded declared input cases only, not sampled results. No normalized, sampled, or sequence evidence was produced.

## Exact owner-patch direction, not implemented

1. Change `is_controlled_by = ROOT` to candidate-scope `PREV` only inside the mapped country iterators in `random_terror_country_is_normal_target` and `random_terror_country_has_valid_state`.
2. Separate intrinsic state eligibility (population, cooldown, lost-local-control) from owner/controller checks. Use the intrinsic predicate only inside iterators that already guarantee candidate ownership/control. Preserve the explicit ROOT contract in action-target helpers and unrelated callers.
3. Move `random_terror_target_reserved` until after a valid site and incident are successfully applied, with a caller-owned success receipt or equivalent cleanup if selection fails. Preserve the numeric two-day cooldown and inject a fixed literal duration through a verified `meta_effect`; do not pass a temporary variable to the timed-flag `days` field.
4. Initialize `individual_crisis_candidate_adjusted_weight` in the candidate caller and at each public forwarding boundary before invoking the private worker. Initialize `individual_crisis_active_load` in the private worker before calling its hidden-trigger calculator.
5. Establish the candidate-pool array in its owning selector before clearing it and entering nested helpers, using a harmless create-then-clear entry if the installed array contract requires it. Do not treat `clear_temp_array` as proof of allocation.
6. Initialize `random_terror_resolved_evolution` in `random_terror_resolve_evolution` before the nested evolution identifier helper. Retain commit `04689ecb13f203945be130d461fdf4eb957c043b`'s existing `random_terror_wave_target_count` caller initialization without repeating it.
7. Keep base ticket weight one, curve factors/ticket constants, active cap three, provider definitions, tier attempt counts, cooldown value, and event pacing unchanged in the owner patch. Do not select a balance target or modify country generation, GUI, or AI weights.

The source snapshots and current after paths are byte-identical today, so no comparison was attempted. The parent must freeze any changed after-source and dependent helper closure before the future same-scenario `probability_compare`; never compare the current source path to itself.

## MCP blockers and remaining uncertainty

The connected `hoi4.probability_inspect` custom-pool request on the Event 31 effects file timed out after 600 seconds. The narrower custom-pool retry on `individual_crisis_targeting_effects.txt` also timed out after 600 seconds. Neither returned an artifact URI, source revision, candidate list, custom-pool manifest schema, or scenario hash.

The `probability_evaluate` request for adapter `custom_weighted_pool`, the shared-helper source, the parsed fixture, `raw_value`, and JSON/matrix/unresolved outputs returned `timed out awaiting tools/call after 600s`. No exact numeric result is claimed.

No sweeps, seeded simulation, sequence, probability render, or comparison were run. The exact source ticket curve is not a normalized probability. The live candidate pool and transitive provider predicates are incomplete; the typed R/A/B/C bindings, state scopes, provider results, and conservative helper-frame observations are not confirmed by the connected adapter. No full identity-invariance claim is made.

Event `inspect`/`render` structural MCP evidence is pending as recorded below. Local reference retrieval through MCP was not run in this interim handoff; scope behavior is supported by the architecture handoff's offline wiki source receipts and installed vanilla precedents, which do not replace the missing MCP evidence.

A narrow `hoi4.event_inspect` trace for selector `{kind:"event",eventId:"chaosx.nr31.1"}` and `hoi4.event_render` scope view for the same selector were submitted with downstream direction and bounded node/depth limits. Neither had returned by handoff time. Their transport outcomes are unverified, not cancelled, and no event graph/render artifact or revision is claimed.

No `beforeManifest`/`afterManifest` was created because the custom pool candidate and dependency schema was not returned. The handoff does not invent manifest fields.

The after-copy/immutable-before SHA-256 table above is the baseline for the owner patch. The original snapshots were not overwritten. Only the two requested audit artifacts were created: this handoff and the JSON scenario fixture. No game launch or log search was performed, and no commit was made.
