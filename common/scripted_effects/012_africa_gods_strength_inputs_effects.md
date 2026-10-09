# Gods Strength input owner API

Disposition: the selected fundamental owner helpers and parent callers are implemented in source.
The full Strength contract remains incomplete for the queued strategic families and native evidence.
The implementation-phase instruction selects the world deployed-army ratio, 10% anchor, 75/25 military multiplier, zero-actual-army rule and 50/50 continent blend.
Capital, port, rail, resource and active-base factor families remain outside this bounded patch.
The strategic 20% proposal is accepted and queued pending province-port aggregation and owner-roster semantics.
No strategic-site contract, hook, public counter, icon, reward or payment is installed here.

All effects are COUNTRY scope and called with `= yes`.
No `$PARAM` expansion or named argument API is used.
All stored measurements are normal host variables.
Temporary inputs are unscoped and caller-owned, with no ROOT/PREV prefix.
The matching triggers are pure reads and require no Gods authority epoch during census initialization.
These helpers prove shared host identity and sample identity, and do not grant or replace the original-owner Gods mandate.
The parent must retain its existing authority gates.

## Identity and validity triggers

`gods_of_africa_strength_host_is_current` uses the real ROOT-independent `africa_has_current_host`, country existence, explicit `tag = event_target:africa_host`, unifier/commit flags, host generation, origin ID and active Event 012 global flag.
The former collector's `africa_is_current_host` dependency compared the target with native ROOT.
The corrected collector and tests execute this explicit object guard with foreign native ROOT.

`gods_of_africa_strength_census_owner_is_current` additionally matches the initialized census host ID/generation/origin to current owner fields.
`gods_of_africa_strength_census_is_complete` requires its complete receipt, matching retained and current native country cardinality, and the host row.
A cardinality match cannot detect a same-size identity substitution.

`gods_of_africa_strength_army_sample_is_current` requires complete census proof, a valid sample, matching host ID/generation/origin, processed-row cardinality, all required fields, nonnegative and internally consistent sums, and a date within the sample's inclusive 30-day owner interval.
`gods_of_africa_strength_territory_sample_is_current` requires positive Africa cardinality, matching sample identity and an observation on the current day.
`gods_of_africa_strength_input_sample_is_current` combines these proofs.
`gods_of_africa_strength_input_factors_applied` also requires the explicit successful-application flag.
The parent uses the latter after applying factors and before publishing Strength.
No invalid-input path fabricates zero world power or silently bypasses the chosen factors.

## Census effects

`gods_of_africa_initialize_strength_census = yes` runs only on the current host.
It clears samples and the measurement roster, sets `gods_of_africa_strength_census_initialized`, records current `_census_host_id`, `_census_generation`, `_census_origin_host_id` and `_census_size`, and clears complete/coverage receipts.
It deliberately resets the roster and must be called at the existing one-time census boundary, not from a refresh or recurring hook.
It supplies no country iteration.
Missing host identity rejects initialization.

`gods_of_africa_remember_strength_country = yes` runs on each country object supplied by that existing census, before the candidate filter.
Its only required context is an initialized, current census at the authoritative host target.
It inserts THIS once in `gods_of_africa_strength_countries`.
It accepts dormant, nonhuman, special and host objects independently of participant/settlement eligibility.
Named onboarding callbacks may use the same effect to append a newly supplied object.
Insertion invalidates the army/application flags.
For a previously completed census, insertion rechecks completion against current native cardinality.
Duplicate insertion makes no change and preserves the cache.

`gods_of_africa_finish_strength_census = yes` is the explicit post-pass completion boundary.
It clears complete first and sets it only if actual retained count equals `global.countries^num`, census owner identity is current, and the host is retained.
Failure sets `gods_of_africa_strength_world_coverage_incomplete`.
A missing pre-filter insertion or a cut-short pass never earns completion.

## Army measurement and lifetime

`gods_of_africa_measure_strength_armies = yes` requires complete current census proof.
It walks only `gods_of_africa_strength_countries`.
Every row increments `gods_of_africa_strength_army_processed_count`, including dormant rows.
Every existing country or documented `is_government_in_exile` country contributes its `deployed_army_manpower_k`.
Nonhuman, special, minor and capitulated living armies are included.
Dormant nonexile objects contribute zero regardless of fixture/stale getter contents.
The host is already in this sum and is never added separately.

Normal host outputs share prefix `gods_of_africa_strength_`:

- `world_army_k`, the complete measured total in thousands.
- `host_army_k_sample`, the host value at that observation.
- `army_processed_count`, the observed row count.
- `army_sample_day` and `army_sample_due_day`, using existing `gods_of_africa_timing.owner_tick_days`.
- `army_sample_host_id`, `army_sample_generation`, `army_sample_origin_host_id`.
- `army_sample_valid` country flag after full processing and valid numeric reads.
- `army_read_invalid` and `world_coverage_incomplete` flags on invalid/incomplete measurement.

Required negative getter evidence is rejected rather than clamped into an invented army total.
No undocumented numeric upper bound is imposed.
Zero host and zero world armies are valid observations.
Absent fields are invalid, distinct from observed zero.
A failed measurement can leave partial numbers for diagnosis, but its validity flag is clear and the parent must not consume them.
After correcting a coverage/iteration issue, explicitly re-finish the census and resample.
The helpers do not repair an unchanged external tool or perform another world discovery scan.

The parent samples at activation, the existing due owner review, or legitimate owner rebind.
Cached foreign armies remain unchanged between those observations.
During factor application, current world total is corrected as `sample_world - sample_host + current_host`.
This reflects host losses and gains immediately without self-double-counting.
It is a sampled foreign-army comparison, not instantaneous worldwide combat telemetry.

## Territorial measurement

`gods_of_africa_measure_territorial_control = yes` requires the current host and uses one native `every_collection_element` pass with `input = collection:states_in_africa`.
PREV within each state is its host context, independently of native ROOT.
It recounts normal host fields from zero.

The existing outputs remain:

- `african_state_total`, every native African state.
- `african_owned_states` and `african_controlled_states`, independent ownership and control counts.
- `african_secured_states`, owned and controlled by the host.
- `african_core_total`, African host cores regardless of owner/controller.
- `african_secured_cores`, host-owned and host-controlled African host cores.
- `territorial_control`, unchanged direct-host score: secured host cores divided by all African states, scaled to 100.
- `territory_observation_day`.

Additional private outputs are:

- `member_states`, member-owned and member-controlled African states.
- `member_core_states`, those member states which are host cores.
- `occupied_states`, host-core or host/member-owned African states controlled by an outsider.
- `physical_control`, host-secured plus eligible-member-secured host cores divided by all African states, scaled to 100.
- `territory_host_id`, `territory_generation`, `territory_origin_host_id`.
- `territory_sample_valid` flag for a positive geographic denominator.

The pure `gods_of_africa_strength_member_is_eligible` predicate requires an existing non-capitulated country distinct from the host, current member generation, cooperative relationship and membership in the host's actual `africa_relationship_countries` array.
It runs the existing generation/cooperation predicates without native ROOT dependence.
Protected, associate, chartered, autonomous federal and integrated relationships qualify.
Outside, resistant, leaving, rival, occupied-settlement, stale and unregistered objects do not.
Native `is_owned_and_controlled_by = OWNER` requires the member to hold its own state.
Allied cross-control remains separate, with no unaccepted reward.
Member ownership is never attributed to the host.
A small host holding every home core receives only its actual continental extent.

Empty geography records zero and leaves territory validity clear.
Calls on a former/uncommitted host leave existing territorial fields unchanged.
Every authorized new observation clears an earlier application-success flag.
Homeland retention can be read from secured-core/core-total counts, but is not substituted for the continental denominator.

## Selected factor application

`gods_of_africa_apply_strength_input_factors = yes` consumes the two preinitialized caller temporary variables:

- `gods_of_africa_strength_military`, the existing division/readiness component after its clamp and 60/40 equipment/fuel sustainment multiplier.
- `gods_of_africa_strength_continent`, the existing political component after recognition and its clamp.

It overwrites only those caller-owned component outputs and sets `gods_of_africa_strength_input_factors_valid` on success.
Scratch temps are local to this invocation.
On stale/incomplete/missing proofs or missing caller component fields, outputs stay unchanged and validity is clear.
Do not publish unchanged components on that failed path.

For q = current host deployed army / corrected cached world deployed army:

`military_out = military_in × (0.75 + 0.25 × clamp(q / 0.10, 0, 1))`.

An actual zero host army or nonpositive controlled division count forces military output to zero even with readiness above zero.
Observed zero world skips division safely and still follows that zero-army rule.
The multiplier never exceeds one and cannot bypass the existing physical/readiness/sustainment ceiling.

`continent_out = 0.50 × political_in + 0.50 × physical_control`.

Constants are centralized in schema-first fixed-point category `gods_of_africa_strength_inputs`.
Existing division divisor 20, sustainment floor/span and shares, outer component weights, Chaos normalization, evolution amplifiers, ordinary smoothing and doctrine ceilings are untouched.
The world getter measures deployed land manpower, with no claim about foreign equipment quality, supply, fleet or air capability.

## Cleanup and successor contract

`gods_of_africa_clear_strength_input_sample = yes` runs on a specified host object, including revoked/departing owners.
It clears every army/territory measurement, identity/date field and sample/application flag, preserving the discovery array, initialized/complete census receipts, census identity/size and coverage receipt.
It grants nothing and never changes the global host target.
Parent transfer stages/restores the discovery array and census receipts, clears copied measurements, rebinds census host ID/generation/origin to the legitimate current owner, re-finishes coverage, and resamples only when existing Gods authority permits.
The same retained roster includes both predecessor and successor once.
No census replay, separate successor addition to W, or copied sample validity is allowed.
The parent owns final Event 012 roster teardown, authority gates and callback integration.

## Evidence and pending work

The validation file `.tools/validation/test_012_gods_strength_inputs.js` executes parsed production bodies and pure trigger dependencies.
It retains the six parent territorial cases and adds registration, dormant/exile/nonhuman/special/host rows, native-getter fixtures, successor proofs, incomplete/truncated processing, cache corrections, zero armies, stale identity/date, member-core occupation and actual pinned baseline arithmetic.
The five-decimal truncation model does not prove native arithmetic range, loaded map cardinality, reserved dynamic-object identity reuse or iterator limits.
`MAX_EFFECT_ITERATION = 1000` is not assumed away.
The tests simulate truncated native body processing and require processed-row equality before validity.

Installed references already retained by the parent include collections `:303–312`, collection context `:20–41`, COG dormant-country array patterns and the exact `input` iterator precedent.
Additional live reference reads confirmed installed `triggers_documentation.md:5618–5626` and offline Triggers `:978` for the exile predicate.
Existing local Data structures `:1779–1787,1591–1594` and installed dynamic variables `:271–272,972–975` establish the country universe and manpower units.
Exact reference results and helper baseline/post-source manifests belong to the owned evidence child.

Unknown future dynamic objects not retained or named by existing callbacks remain an explicit coverage limitation.
Current native country cardinality detects growth but cannot prove same-cardinality identity preservation.
No proposed strategic-site contracts are installed.
Main refresh, census call sites, transfer, callbacks, UI/localisation and the weighted-consumer baseline/compare remain parent-owned.
The helper patch is not a claim that the complete Strength specification or full Event 012 goal is complete.

## Parent caller integration

The existing World census initializes this roster, remembers every supplied object before tribute eligibility filters, and finishes the census after that same pass.
Named onboarding remembers measurement objects independently of participant enrollment.
Activation and the existing due owner tick recheck census cardinality, then sample armies before Strength refresh.
The ROOT-independent refresh measures current territorial control and applies selected factors to its caller-owned military and continent temporaries.
The original weighted sum, penalties, smoothing, band, public observer and credibility emitter run only after the actual successful-input proof.
An invalid sample sets the private publication-block receipt and produces no fresh global Strength or observer state.
Relevant African control-change callbacks refresh land through the actual host object without resampling foreign armies.
Host succession preserves the discovery roster, binds its census to the successor and discards predecessor measurements without granting a Gods mandate.
Cleanup and revocation clear measurements and publication-block state while retaining discovery for the existing recovery lifecycle.

The 26 owner cases and 57 actual-source integration cases cover these paths under SourceNoNativeProof.
The integration audit executes 51 production bodies and three caller subtrees, with 24 hash-bound inputs.
The matched seven-scenario weighted-root comparison excluded all 14 candidate-case rows with 392 unresolved traces.
It holds public Strength fixed and cannot establish campaign Strength effects, numeric score equivalence or selection probabilities.
Native arithmetic, collection execution, allocation completeness, callback order and the clean live error log remain unproved.
The integration evidence is in docs/plans/012_africa_plans/subagent_handoffs/012_gods_strength_integration_review_2026-10-09.md.

## Foreach isolation

The army sampler binds its own break temporary and resets it immediately before each traversal.
The one-time census, recognition pass, succession arrays and related Gods receipt/recovery loops use distinct helper-owned break storage.
An inherited default break or a previously set private break cannot truncate the next invocation, and the caller's unrelated default break remains intact.
The maintained iterator regression executes poisoned-break census, sampler, nested cleanup and settlement paths, including 2,014 visits across two 1,007-object samples without imposing a foreach ceiling.
Its 13 cases preserve the original 26 input and 57 consumer cases under SourceNoNativeProof.
