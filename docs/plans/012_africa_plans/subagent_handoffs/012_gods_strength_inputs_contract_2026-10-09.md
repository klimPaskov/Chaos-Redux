# Event 012 Strength input owner helper handoff

Disposition: `implemented` for the bounded owner helpers and source scenarios.
Parent call-site integration, full Strength fidelity and weighted-consumer comparison remain pending.
This report replaces the earlier recommendation as the current conclusion.
The earlier contract and original six-case collector bytes are retained in the owned evidence child's before snapshots.

## Acceptance and exact scope

The implementation-phase instruction explicitly selects deployed world army manpower, world-share anchor 0.10, multiplier 0.75 + 0.25 normalized share, zero actual army/division suppression and the 50/50 political/physical continent blend.
Physical extent is host-secured plus eligible-member-secured host cores divided by every African state.
Current division divisor 20, sustainment equipment/fuel shares 0.6/0.4, readiness arithmetic, outer weights, Chaos normalization, evolution, smoothing and doctrine ceilings are unchanged.
The 20% strategic subcomponent is `accepted and queued`, with province-port aggregation and owner-roster semantics still indispensable.
Capital, port, rail, resource and active-base source families remain open under the full goal and have no invented implementation here.

Written files:

- `common/scripted_effects/012_africa_gods_strength_inputs_effects.txt` and matching `.md`.
- New `common/scripted_triggers/012_africa_gods_strength_inputs_triggers.txt`.
- New `common/script_constants/012_africa_gods_strength_inputs_constants.txt`.
- Extended `.tools/validation/test_012_gods_strength_inputs.js`.
- This current handoff and owned `012_gods_strength_inputs_2026-10-09_evidence/owner_helpers/` child.

No main Gods, world-order, host-transfer, on-action, GUI, localisation, workbook, Git or game surface was changed.
Source updates used expected-byte-hash checks and atomic replacement within the assigned files.
No new recurring hook, event scheduler, public metric, icon, reward, payment or tool wrapper was created.
Parent wiring is deliberately outside this disjoint patch.

## Public effect API

Every effect is invoked with `gods_of_africa_<name> = yes`.
All are COUNTRY object scope.
Temporary component inputs are bare and preinitialized by the caller, never ROOT/PREV scoped.

| Name | Required inputs/context | Outputs and lifetime |
| --- | --- | --- |
| `initialize_strength_census` | Explicit current host, existing one-time census boundary. | Clears roster and samples, sets initialized receipt and host ID/generation/origin/size. No iteration. This is an intentional census reset, not a refresh call. |
| `remember_strength_country` | Any named country object, current initialized host census. | Deduplicated insertion in host `gods_of_africa_strength_countries`. No existence, humanity, special-country, candidate or settlement filter. New insertion invalidates the army/application receipts. |
| `finish_strength_census` | Host census identity current, actual retained row count equal to `global.countries^num`, host retained. | Complete receipt on exact count, otherwise explicit coverage-incomplete flag. |
| `measure_strength_armies` | Complete current census proof. | World sum, host sample, processed rows, host/generation/origin tuple, sample day/due day and validity flag. Reads every retained row, counting existing or government-in-exile armies. No separate host addition. |
| Existing `measure_territorial_control` | Explicit current host. | Same native Africa state pass and unchanged direct-host fields/score, plus separate member-core/occupied counts, combined physical score and dated owner tuple. |
| `apply_strength_input_factors` | Current army/territory proofs and preinitialized `gods_of_africa_strength_military` / `gods_of_africa_strength_continent` temporary variables. | Overwrites those two caller outputs only on success, with an explicit application-valid flag. Failure leaves outputs untouched and cannot authorize publication. |
| `clear_strength_input_sample` | Specified host object, including revoked/departing host. | Clears all army/territory samples and application flags. Discovery roster, census identity/receipts and coverage metadata remain available to the existing recovery/transfer owner. |

The full parameter/default/output/side-effect contract and usage timing are in the matching owner `.md`.
Census/measurement effects have no caller numeric parameters.
The factor helper has no implicit component defaults.
No new helper requires an authority epoch during early census initialization, and none grants Gods authority.

## Pure guards and the corrected ROOT defect

Public current-owner guard: `gods_of_africa_strength_host_is_current`.
It executes the actual `africa_has_current_host` dependency, local unifier/commit flags, host generation/origin and Event 012 active flag, plus explicit `tag = event_target:africa_host`.
It never compares the host to native ROOT.

The parent's staged territorial guard used `africa_is_current_host`, whose source enters the host target and compares `tag = ROOT`.
The old six-case VM replaced that whole predicate with object equality, hiding the foreign-ROOT defect.
The source guard is corrected locally, and the tests load the actual new guard plus actual existing host/member/cooperation trigger bodies.

Public combined sample proof: **`gods_of_africa_strength_input_sample_is_current`**.
It combines current census/army proof with same-day territory proof.
Public post-application proof: **`gods_of_africa_strength_input_factors_applied`**.
The parent must use the latter after factor application and before publishing Strength.
Its successful flag is `gods_of_africa_strength_input_factors_valid`.
Local supporting pure predicates are census-owner/completion, army-sample, territory-sample and member-eligibility checks.

## Exact normal fields for parent wiring

All following suffixes share prefix **`gods_of_africa_strength_`**.

Census array and receipts:

- `countries` country-scope array.
- `census_initialized`, `census_complete`, `world_coverage_incomplete` country flags.
- `census_size`, `census_host_id`, `census_generation`, `census_origin_host_id` normal variables.

Army sample:

- `world_army_k`, `host_army_k_sample`, `army_processed_count`.
- `army_sample_day`, `army_sample_due_day`.
- `army_sample_host_id`, `army_sample_generation`, `army_sample_origin_host_id`.
- `army_sample_valid`, `army_read_invalid` flags.
- Due day uses the existing `gods_of_africa_timing.owner_tick_days` of 30, with inclusive freshness through that date.

Existing territorial outputs remain `african_state_total`, `african_owned_states`, `african_controlled_states`, `african_secured_states`, `african_core_total`, `african_secured_cores`, `territorial_control`, `territory_observation_day`.
Additional outputs are `member_states`, `member_core_states`, `occupied_states`, `physical_control`, `territory_host_id`, `territory_generation`, `territory_origin_host_id` and the `territory_sample_valid` flag.

Direct `territorial_control` remains 100 × host-secured cores / all Africa states.
Combined `physical_control` is 100 × (host-secured cores + eligible member-secured host cores) / all Africa states.
Member eligibility requires its actual host relationship-array entry, current member generation, cooperative relationship, existence, no capitulation and exclusion of the host itself.
The member must own and control its state, using native `is_owned_and_controlled_by = OWNER`.
Member territory never becomes direct host ownership.
Allied cross-control is excluded from secured buckets.
Occupied diagnostics count host-core or host/member-owned African states under outsider control.

## Parent integration sequence

1. Existing world-order initializer around lines 820–825 calls `initialize_strength_census` once.
2. Inside the existing `for_each_scope_loop array = global.countries` around lines 905–915, call `remember_strength_country` before candidate filtering, and call `finish_strength_census` after the pass.
3. Existing named onboarding callbacks independently remember their supplied country scopes before candidate/settlement gates. Duplicate names do not invalidate samples. A genuinely appended object invalidates the sample and must be measured on an allowed owner boundary.
4. Activation around main helper lines 621–623 and due owner refresh around 138–155 sample armies before refreshing Strength. Use the existing owner cadence only.
5. Replace main refresh's ROOT-dependent outer identity guard with `gods_of_africa_strength_host_is_current`, retaining original Gods mandate checks in their existing parent gates.
6. Main refresh calls the territorial collector on the current host, calculates current legacy military/continent temps, then applies the factor helper. Gate publication on `gods_of_africa_strength_input_factors_applied`.
7. Cleanup calls `clear_strength_input_sample`. Parent transfer stages/restores the census array and receipts/size, clears copied measurement samples, and explicitly rebinds `census_host_id`, `census_generation`, `census_origin_host_id` to the legitimate successor before finishing census proof. Copying a roster does not confer original-owner Gods mandate.
8. Re-finish coverage and resample only when the existing authority/rebind lifecycle permits. Both predecessor and successor remain single world rows. Do not add the new host separately or replay a world census.

Between samples the factor helper computes corrected W as `world_army_k - host_army_k_sample + deployed_army_manpower_k`.
Foreign changes remain sampled until the existing owner refresh.
Invalid/stale/partial input clears success and leaves component temps unchanged, so the parent must not publish that failed result.
Zero measured world and zero host army are valid, distinct from missing sample fields.

## Constants and arithmetic evidence

New unique schema-first fixed-point category `gods_of_africa_strength_inputs` has exactly five tuning entries:

| Key | Value |
| --- | ---: |
| world_share_anchor | 0.10 |
| military_absolute_share | 0.75 |
| military_relative_share | 0.25 |
| continent_political_share | 0.50 |
| continent_physical_share | 0.50 |

Military output is its existing post-sustainment input multiplied by `0.75 + 0.25 × clamp(host/world / 0.10, 0, 1)`.
Zero deployed army or nonpositive controlled division count forces military output zero despite readiness.
Continent output is half existing political value plus half measured physical value.
No strategic term is mixed in.

The source VM executes the production helper bodies and actual pinned legacy military/continent arithmetic, with typed native getters and a stated five-decimal truncation assumption.

| Representative case | Military old → selected | Continent old → selected | Raw weighted Strength delta |
| --- | --- | --- | ---: |
| Weak, 20 divisions, readiness 20, world share 1%, extent 5% | 10.5 → 8.1375 | 60 → 32.5 | -6.09062 |
| Strong, 800 divisions, readiness 80, world share 20%, extent 80% | 60 → 60 | 80 → 80 | 0 |
| World anchor, 400 divisions, readiness 60, world share 10%, extent 80% | 40 → 40 | 60 → 70 | +2 |
| Same host, larger foreign armies, share 4% | 40 → 34 | 60 → 70 | +0.5 |
| Occupation reduces secured-core extent to 30% | 40 → 40 | 60 → 45 | -3 |
| Zero actual army, readiness 60 | 30 → 0 | 60 → 70 | -5.5 |
| Existing sustainment floor with strong land | 16 → 16 | 60 → 70 | +2 from land only |

These are deterministic component calculations before unchanged smoothing and other components/penalties.
They are not campaign probabilities.
The host-row correction case gives 7.6255 under the stated sequential five-decimal truncation model.
No native numeric maximum or engine-precision certification is inferred from those results.

## Meaningful validation and limits

The extended test file passed **26 source scenarios**, retaining the six territorial cases and adding actual foreign-ROOT proof, each missing host witness, dormant/exile/nonhuman/special inclusion, no host duplication, allocation growth/named repair, cached-row correction, zero army/world, thousand-unit boundaries, stale host/generation/origin/date, missing and negative getter evidence, incomplete census/body processing, succession conservation, all five eligible relationship states, departed/stale/hostile/member occupation, cleanup and unknown-helper rejection.
It uses no independent financial model and preserves the native Africa-definition extraction needed by the existing parser.

Native scope/array operations remain fixtures.
The MAX_EFFECT_ITERATION scenario deliberately simulates 1000 processed rows in a 1003-row roster and requires failure, then verifies the corrected full-row fixture after explicit census re-finish.
It does not certify that the native scope iterator bypasses the numeric loop cap.

Additional live reference search/read confirmed installed `triggers_documentation.md:5618–5626` and offline Triggers `:978` for `is_government_in_exile`.
Both result revisions/path/spans are retained in `owner_helpers/exile_reference_evidence.json`.
Local country/manpower, collection, constant and scope rules and vanilla COG/iterator precedents remain linked through the parent's `initial_reference_evidence.json` and the owner API document.

A script-validation file request initially supplied explicit kind/scope and was rejected because file checks infer those values.
The one corrected request used only the owned effects path.
It returned `SCRIPT_CHECK_PARTIAL`, `valid = null`, 149 commands checked, zero findings, 69 unchecked argument blocks and seven unknown-scope roots.
Its `checksPerformed` are syntax, command kind, declared scope and event popups, with parameter semantics unchecked.
This is partial documentation coverage, not a passed native effect or scope check.
Both attempts are retained in `owner_helpers/script_validation.json`.
No more retry is permitted for this unchanged coverage issue.
A later retry requires a validator/input change that actually resolves the unsupported scope/argument coverage.

Remaining limits are unknown future dynamic objects that neither belonged to the retained set nor reach existing named callbacks, same-cardinality object identity replacement, actual native getter/iterator/arithmetic execution, and parent scheduling/transfer/publication wiring.
The documented exile predicate explicitly covers exiled-government objects, without assuming that `exists` alone describes them.
No full-world recurring scan or fake major/candidate denominator is used.

Parent owns the weighted-consumer baseline/compare through the already assigned `chaosx_ai_probability_auditor` route beginning `01a12086`.
This handoff supplies exact before/after owner sources and component cases for that review.
No independent probability-auditor completion is claimed here.
No simplification was made to the selected bounded helper implementation.
Full Strength completion remains unclaimed because parent integration and the explicitly queued source families remain open.

Skills used: `chaos-redux-events` and `chaos-redux-subagents`.
No skill edits, new delegation, Git commit or game launch were performed.

## Preserved parent acceptance and guard review

The following parent checkpoint is retained as historical acceptance evidence.
The current owner-helper implementation status above supersedes its in-progress status while leaving parent integration pending.

Disposition: fundamental census, competition-only military multiplier, explicit zero-army guard and 50/50 political/physical continental blend are `accepted and queued` by parent selection on 2026-10-09 within the full-Gods goal.
The capital/port strategic proposal is `accepted and queued` pending verified province-port aggregation and owner/site semantics.
Rail/resource/base families and unknown-object coverage remain unresolved rather than being replaced with proxies.
The fundamental owner-helper patch is in progress, with final parent integration and required checks outstanding.
This is a source plan, not an implementation or Event 012 completion claim.

Parent source review also identified the existing `africa_is_current_host` predicate as ROOT-dependent.
The input owner must use an exact COUNTRY-object predicate against `event_target:africa_host`, and the integration must avoid borrowing native ROOT from unrelated callback/scenario countries.
The prototype's six typed territorial cases cover counting but its first authorization fixture hid this legacy predicate behavior.
The owner implementation must execute its actual corrected authorization predicate before claiming ROOT-independent acceptance.
