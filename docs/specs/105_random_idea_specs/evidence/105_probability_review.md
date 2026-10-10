# Event 105 Random Idea probability design review

Status: design-only review completed, engine probability audit unresolved.
The parent accepted the final tuning in this report within the user-authorized expansion scope.
No gameplay files were edited.
The repository metadata supplied by the parent pins revision `a3ef485c5da7e2337122eca04ac65c175050f251`.
That revision is provenance for the planned integration, not evidence that a proposed selector exists or works in the engine.

## Evidence boundary and consulted sources

The supplied global source-reading gate reports `gate_passed: true` at `/workspace/scratch/f3ee004562dc/source_reading/global_source_gate.json`.
This review read the supplied probability role `/workspace/scratch/f3ee004562dc/source_reading/current/subagents/chaosx_ai_probability_auditor.toml`, the complete current `AGENTS.md`, and the relevant specialist probability and event evidence sections listed below.
The live tool registry was independently filtered for HOI4 and probability routes and returned no matching tools.
Consequently `hoi4.probability_inspect`, `hoi4.probability_evaluate`, `hoi4.probability_sweep`, `hoi4.probability_compare`, `hoi4.probability_render`, `hoi4.event_inspect`, and `hoi4.event_render` were not called.
No MCP analysis IDs, artifact URIs, scenario hashes, comparisons, rendered engine evidence, or live observations exist for this review.
The missing callable HOI4 routes are the exact blocker, rather than a demonstrated service failure.

References supporting the review contract:

- `source_reading/current/AGENTS.md`, sections 0, 1, 5, and 6: mandatory probability evidence, central tuning, loop limits, and truthful completion claims.
- `source_reading/current/chaos-redux-subagents.md`, lines 80, 223–229, and 287–323: read-only probability role, immutable before-source evidence, named scenarios, live-schema checks, and comparison input rules.
- `source_reading/current/chaos-redux-events.md`, lines 382–408: event and probability evidence boundaries, comparison sources, complete local pools, and unresolved external factors.
- `source_reading/current/chaos-redux-event-planning.md`, lines 955–980, and `chaos-redux-improvement-loop.md`, lines 138–155: scenario-specific intended ordering and probability audit routing.
- `research/offline_refs/idea_modding.md`, lines 28–46, 102–115, 218–245, 313–321, and 344–361: category distinctions, explicit idea assignment, callbacks, cancellation, and the wiki's statement that manual assignment bypasses the `allowed` check.
- `research/offline_refs/effects.md`, lines 700–719: random-variable bounds are described as minimum-inclusive and maximum-exclusive, and nearest-integer rounding is distinct from floor or ceiling.

These are local supplied sources, and the offline wiki was not accessed on the web.
Installed vanilla documentation under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/` was not available in this Linux workspace and was not claimed as read.
The offline wiki does not establish the installed engine's effective NATIONAL classification, complete loaded definition set, or callback semantics.
Those conclusions remain unresolved pending the parent-owned architecture and engine review.

One inherited catalog discrepancy requires parent reconciliation: `source_reading/current/chaos_redux_events_catalog.csv:228` labels 105 “Anti-player ideology.”
The explicit parent assignment for Event 105 Random Idea is authoritative for this design review.
No catalog file was changed.

## Audited surfaces and acceptance basis

The in-scope proposed surfaces are `chaosx.nr105.1` and its planned bundle-count selector, loaded-NATIONAL identity selector, direct-grant provenance refresh, and callback-sensitive grant loop.
Exact implementation helper identifiers and engine-relative files are not yet supplied, so this report does not invent them.
There are no player or AI choices, currency costs, management actions, usefulness preferences, or country-specific weighting in the accepted design.
Country validity is the parent-owned target-scope contract.
Every valid country receives its own selection process.
Ideas selected for one country remain selectable for another country.

The user baseline is uniform selection over every unique effective loaded, technically addable NATIONAL idea identity, including adverse, foreign, incongruous, staged, mutually awkward, or otherwise unhelpful ideas.
Current exact ownership and within-bundle repeated identity are the only gameplay exclusions stated here.
The type boundary excludes laws, designers, advisors, and other non-NATIONAL categories because they are outside the requested candidate type, not because they would be undesirable.
Whether a particular hidden category belongs to the engine's NATIONAL type requires category evidence, not an invented blanket include or exclude rule.

The parent explicitly rejected burden scaling for the lower tiers because the user requires two at 200 and three at 400 for every country.
The parent also retained Collision at four through six.
The initial unapproved proposal with a Storm center floor of one allowed high-burden Storm one through three and contradicted global Chaos monotonicity at 799 to 800.
That proposal is superseded.
The accepted center floor of five resolves the conflict, and the final parent refinement changes the pressure constant from 12 to 24 to preserve a longer dynamic range.

## Accepted final requested bundle counts

`C`, the complete valid-recipient roster, and every recipient's `B` are snapshotted globally before any Event 105 grant dispatch executes.
`B` is a nonnegative whole-number count of the intersection between that country's distinct prior Event 105 direct-dispatch receipt identities and its exact current ownership at this global pre-grant snapshot.
A receipt records one direct dispatch after technical preflight, rather than proven native grant success unless engine evidence establishes success.
Historical receipt records and current burden are separate, so an absent identity contributes zero to `B` without converting its old dispatch into a proven failure.
`B` excludes native or other-event ideas unless that exact identity also has a prior Event 105 direct-dispatch receipt and is currently held at the snapshot.
Callbacks' indirect grants do not automatically become direct Event 105 dispatch receipts.
An exact definition identity contributes one regardless of repeated receipts, modifier strength, localisation name, or historical attempts.
The effective loaded candidate universe is fixed for this firing, while exact current ownership and the remaining eligible set are refreshed for each draw.
Earlier recipients' callbacks can change later eligibility but cannot change their snapshotted bundle quantity.

| Chaos snapshot | Requested count distribution |
| --- | --- |
| Below 200 | Exactly 1 |
| 200 through below 400 | Exactly 2 |
| 400 through below 600 | Exactly 3 |
| 600 through below 800, Collision | Uniform integer 4 through 6 |
| 800 and above, Storm | Formula below |

For Storm define:

`S = 8 + floor((clamp(C, 800, 1600) - 800) / 100)`

`d = 24 + B`

`T = max(5, ceil(24*S / d))`

`L = T - 1`

`U = min(16, T + 2)`

`K ~ UniformIntegerInclusive(L, U)`.

The exact whole-number arithmetic equivalent is `T = max(5, floor((24*S + d - 1) / d))`, assuming whole `S`, whole nonnegative `B`, and exact arithmetic.
This avoids a fractional `1+B/24` intermediate and avoids nearest-integer rounding.
It is a mathematical specification, not a claim about an installed Clausewitz implementation.
Fixed-point precision, modulo behavior, dynamic random bounds, and overflow require installed-documentation review.
Centralize 200/400/600/800 thresholds, the 1600 intensity ceiling, pressure 24, center floor 5, 100-point step, offsets, and per-bundle maximum 16 as tuning values.
The ceiling at 1600 caps intensity and the maximum 16 caps one requested bundle, neither caps total retained burden.

For any ideal inclusive uniform integer range, every listed count has probability `1/(U-L+1)` and mean `(L+U)/2`.
If the engine primitive is half-open as described in the supplied wiki, an inclusive range requires a verified upper bound of `U+1`.
Rounding a continuous random number to the nearest integer would give unequal endpoint probabilities and is unsuitable.

### Requested counts and means

Each cell gives the inclusive range and its abstract mean.
This table assumes a sufficiently large eligible pool and successful direct grants, with no callback changes.

| Retained direct burden B | C=800, S=8 | C=1000, S=10 | C=1200, S=12 | C=1600 or higher, S=16 |
| --- | --- | --- | --- | --- |
| 0 | 7–10, mean 8.5 | 9–12, mean 10.5 | 11–14, mean 12.5 | 15–16, mean 15.5 |
| 6 | 6–9, mean 7.5 | 7–10, mean 8.5 | 9–12, mean 10.5 | 12–15, mean 13.5 |
| 12 | 5–8, mean 6.5 | 6–9, mean 7.5 | 7–10, mean 8.5 | 10–13, mean 11.5 |
| 24 | 4–7, mean 5.5 | 4–7, mean 5.5 | 5–8, mean 6.5 | 7–10, mean 8.5 |
| 48 | 4–7, mean 5.5 | 4–7, mean 5.5 | 4–7, mean 5.5 | 5–8, mean 6.5 |
| 96 | 4–7, mean 5.5 | 4–7, mean 5.5 | 4–7, mean 5.5 | 4–7, mean 5.5 |

The floor is reached precisely when `B >= ceil(24*S/5) - 24`.
The thresholds for S=8 through 16 are respectively B=15, 20, 24, 29, 34, 39, 44, 48, and 53.
At Chaos 800 the mean falls from 8.5 at B=0 to 5.5 at B≥15, approximately a 35.3% reduction.
At Chaos 1600 the mean falls from 15.5 at B=0 to 5.5 at B≥53, approximately a 64.5% reduction.
The floor is a positive ongoing grant rate, not asymptotic cessation.

### Monotonicity classification

Classification: exact abstract mathematical ordering, conditional on the specified count distributions, not engine evidence.
At fixed B, S is nondecreasing in C, so T, L, and U are nondecreasing in C.
An inclusive uniform integer distribution is first-order stochastically nondecreasing when both its endpoints are nondecreasing.
One proof couples quantiles with `L + floor(q*(U-L+1))` for a common uniform q in [0,1), considering endpoint increases one at a time.
At the 800 boundary the smallest Storm distribution is uniform 4–7, which stochastically dominates Collision's uniform 4–6.
The preceding exact 1, exact 2, exact 3, and uniform 4–6 tier boundaries also preserve the ordering.
Therefore the requested-count distribution is globally nondecreasing with Chaos at every fixed B.

At fixed C in Storm, increasing B cannot increase T, L, or U, so requested counts are stochastically nonincreasing with burden.
Lower tiers are burden-independent, which is weak monotonicity rather than a strict reduction.
Plateaus are deliberate consequences of integer rounding, the center floor, and the 1600 intensity ceiling.
Higher Chaos does not guarantee a larger realized roll in an independent firing.

A small local exact-rational CDF check verified 34,025 comparisons across every distinct Chaos threshold, adjacent boundary values, B=0 through 1000, and Storm burden increments.
This is an abstract arithmetic check with declared uniform integer assumptions, not `probability_sweep`, an engine simulation, a pool completeness check, or validation of campaign balance.
The proof covers arbitrary nonnegative whole B beyond the checked range.

## Uniform definitions and selection without replacement

Let the effective loaded universe be `U_loaded`, with one row per unique resolved NATIONAL identity after load-order overrides and replacement rules.
Do not count source occurrences, overridden definitions, localisation aliases, or file buckets as additional candidate weight.
A definition with a distinct identity remains distinct even when it shares a displayed name or modifiers with another definition.
The parent must establish the actual loaded universe and technically addable type membership.
No blacklist for foreign provenance, ideology, national theme, usefulness, mutually awkward mechanics, or system compatibility is authorized.

With a stable held set H and no grant callbacks changing eligibility, the eligible pool is `E = U_loaded \ H`.
If A is its size and k distinct direct identities are drawn without replacement, every ordered k-tuple has probability `1/(A*(A-1)*...*(A-k+1))`.
Every unordered k-subset has probability `1/binomial(A,k)`.
Each eligible identity's inclusion probability is k/A, or `E[min(K,A)]/A` after a count roll and natural exhaustion.
These are exact conditional mathematical facts for a complete stable pool and ideal uniform draws.
They do not describe retained engine outcomes after unknown failures or callbacks.

Selecting a random source file and then a random definition within it is biased.
With F files and n_f definitions in the chosen file, a definition's probability is `1/(F*n_f)` under uniform file selection.
Flatten and deduplicate the effective definitions first.
A correctly weighted hierarchy can reproduce flat sampling, but introduces avoidable normalization and override risks.

An indexed eligible-pool draw followed by removing the chosen identity is conceptually the clearest exact sampler.
A uniform random permutation of the stable eligible pool and consumption of its first k entries is equivalent.
A standard reservoir sample of size k over a stable complete pool yields a uniform unordered subset, but its incidental storage order is not a uniform grant order unless shuffled.
Grant order matters when callbacks exist.
Repeated one-item reservoir sampling from the current eligible pool can provide uniform conditional draws with a refreshed pool, at a greater scanning cost.
Implementation feasibility and batching across the documented 1,000-iteration effect-loop limit remain the architect's responsibility.

## Exhaustion, retries, and callback-sensitive eligibility

When A<K and eligibility stays stable, grant every available identity once and report natural exhaustion.
No duplicate filler, foreign-category filler, forced replacement, first-entry fallback, or cross-country allocation is justified.
For A=0, no fresh identity exists and zero direct grants is the correct exhaustion result.
Thus fixed requested counts of two or three cannot promise two or three successful fresh grants in an exhausted pool.
At A=2, every Storm request results in two grants under ideal static conditions.
This is pool exhaustion rather than a burden cap.

Uniform rejection sampling over all N loaded identities can be correct conditional on an acceptance, but is inefficient when few eligible identities remain.
With a fixed eligible size A and R independent attempts, the probability of no acceptance is `(1-A/N)^R`.
For the illustrative abstract N=10,000, A=10, R=100 case it is about 90.5%.
After j successful distinct grants, expected proposal attempts for the next acceptance are `N/(A-j)` if rejected held and previously selected identities remain in the proposal universe.
These numbers are examples, not measured pool sizes.

A finite retry budget alone does not necessarily bias accepted identity shares under a static pool and symmetric rejection, but it changes achieved bundle sizes and can create country-specific underfill.
Fallback to the first valid identity, cyclic scanning from a random start, asymmetric candidate retry budgets, or per-source retry policies can also bias identity selection.
Prefer a finite exact pool traversal or proper without-replacement draw rather than claiming arbitrary bounded retries implement the requested distribution.

The supplied idea wiki describes `on_add`, `on_remove`, `swap_ideas`, and automatic cancellation.
These mechanisms make a static held-set assumption insufficient for engine outcomes.
The design should recheck exact ownership immediately before every direct grant and should refresh the current eligible set after synchronous effects when those effects may add, remove, or replace ideas.
Keep a bundle-local set of already directly selected or attempted identities so an idea removed by a later callback is not selected a second time within the same bundle.
A freshly removed pre-existing identity may become eligible for a later draw if it has not already been attempted in that bundle.

The dynamic specification is uniform conditional selection from the complete currently unheld and bundle-unattempted identity set at each step.
If callbacks change that set, the final bundle generally is not a uniform k-subset of the initial eligible pool.
A frozen initial permutation with ownership rechecks can avoid granting a now-held identity, but does not automatically preserve this dynamic specification when initially held identities are removed or skipped identities become eligible later.
That algorithm needs an explicitly accepted snapshot contract or a refresh mechanism, not a false equivalence claim.

Distinguish requested count, selected identity, attempted direct grant, confirmed immediate retention, and end-of-chain retention.
Unknown engine failures or cancellation mean a uniform selected identity does not prove a uniform retained identity.
Do not refill solely because an idea self-cancels or removes another grant unless the finite refill policy and its changing pool are explicitly designed and audited.
Repeated retries of the same failed identity can invoke callbacks more than once or create a nonterminating loop.
Treat an unconfirmed native grant as unresolved outcome evidence, and never silently substitute a useful or safe idea.
The accepted implementation contract records technically preflighted direct dispatch receipts and performs no post-add success retry.
A receipt is not a native-success certificate.
The next global pre-grant burden refresh counts only prior-receipt identities that are then held, while historical dispatch receipts remain separate evidence.
The precise observability and timing of immediate cancellation remain engine questions.

## RNG independence and deterministic replay

Each valid country must make its own count and identity draws, and cross-country repeated identities are allowed.
Do not roll one idea or one bundle globally and distribute it to every country.
Do not reset every country's generator to a common seed, or reseed each draw with time or the same event value.
A normal advancing engine RNG stream can support distinct per-country draws without a new seed-management mechanic.
Statistical independence and unbiased integer mapping still require evidence from the actual primitive.
Country-specific eligibility means identical RNG values need not mean identical outputs, but differing outputs alone do not prove independence.

For deterministic audit replay, freeze the loaded universe revision and override resolution, stable identity ordering, initial per-country held sets and prior dispatch receipts, the global pre-grant recipient roster, global C, every recipient's global pre-grant B snapshot, target-country iteration order, date and scope state, starting RNG state or declared seed fixture, and all callback transitions and additional RNG consumption.
Changing file order, callback consumption, or country iteration order can change subsequent output under a shared stream.
Count and burden snapshots must not be recomputed mid-bundle.
The parent-accepted refinement captures C, the roster, and all recipients' B globally before any grants, then refreshes current ownership and eligible identities per draw.
Earlier countries' callbacks therefore cannot change later requested-count distributions within this firing, although they can change the later countries' eligible pools and retained outcomes.
Those order-dependent eligibility mutations must be declared rather than ignored.
No custom per-country seed framework is proposed here.

## Accepted risks and unresolved limitations

- Positive grants continue at high burden when fresh eligible identities exist, including Storm four through seven at its floor.
  With unchanged retention and no depletion, the abstract additional count at that floor averages 5.5 per firing.
  This is ongoing accumulation, not a hard total limit or proof of balance.
- Native removal, replacement, cancellation, and finite unique-definition exhaustion can reduce retained growth, but their frequencies and effects are unknown.
  They must not be described as a guaranteed balancing mechanism.
- Adverse effects, unrelated national systems, mutually awkward ideas, country-invalid callback assumptions, and indirect grants are accepted consequences of the requested unfiltered NATIONAL pool.
  Do not fix them with usefulness or system-compatibility filtering.
- Burden measures retained direct identity count, not effect power or callback-generated burden.
  Equally sized bundles can have very different consequences, which is intentional randomness rather than an equal-power claim.
- Monotonic requested counts do not establish monotonic successful or retained outcomes across different countries, eligible pool sizes, callback paths, or failure rates.
  Under the same stable pool, natural `min(K,A)` exhaustion preserves the count ordering.
- The complete effective candidate universe, engine RNG distribution, integer arithmetic support, cancellation timing, and callback outcome probabilities remain unresolved.

## Future scenario-specific HOI4 audit route

Start with the actual exposed live schemas and `hoi4.probability_inspect` on the eventual Event 105 source and its selector helpers.
Do not invent an adapter name, accepted argument field, engine-relative path, or candidate pool manifest before inspection confirms it.
Use `hoi4.event_inspect` and `hoi4.event_render` for source-linked callback and scope structure, without treating focused event inspection as full helper lifecycle proof.

| Scenario ID | Required complete inputs and expectation | Future probability evidence |
| --- | --- | --- |
| `e105_counts_grid_p24` | The table's four Chaos values by six burden values, global pre-grant C/roster/all-B snapshot, all count branches, integer endpoints and rounding rules, stable sufficient pool | `probability_evaluate`, `probability_render` |
| `e105_chaos_boundaries` | Adjacent values at 199/200, 399/400, 599/600, 799/800 and every Storm 100-point step, matched B and pool | `probability_evaluate`, `probability_sweep` |
| `e105_burden_thresholds` | Each S=8..16 floor onset plus adjacent B values, matched C and pool | `probability_sweep`, `probability_render` |
| `e105_unique_loaded_pool` | Complete effective definition list and categories, overridden duplicates, equal identity weights, unequal file sizes | `probability_inspect`, `probability_evaluate` |
| `e105_owned_and_bundle_distinct` | Exact held sets including same-name different-ID ideas, explicit no-replacement transitions | `probability_evaluate` |
| `e105_pool_exhaustion` | A=0,1,2,3,4,7,16 and sufficient-pool cases, all stop rules | `probability_evaluate`, `probability_render` |
| `e105_country_rng` | At least two countries with identical then differing pools, declared engine stream or seed fixture, country order, callback RNG consumption | `probability_evaluate`, with `probability_simulate` only for explicitly declared uncertain inputs |
| `e105_callbacks_mutate_held` | Concrete callbacks that add a future candidate, remove an initially held identity, remove a prior grant, swap identities, self-cancel, fail, or change later recipients' held sets while all B remain snapshotted | `probability_evaluate` for supported declared transitions, otherwise unresolved |
| `e105_repeated_firings` | Complete custom pool manifest, actual cadence, refresh, removals, resets, exhaustion and terminal states | `probability_sequence` only once these inputs are complete |
| `e105_before_after_p24` | Immutable real before-source bytes and hash, implemented after source, identical saved scenarios and complete pools | `probability_compare`, `probability_render` |

Scenario IDs in this report are proposed fixture names, not generated MCP hashes or executed scenarios.
For the comparison, provide real before/after source objects or complete before/after custom-pool manifests under the identical scenario set, following the verified live schema.
An analysis ID is for `probability_render` when supported and is not a source identifier for `probability_compare`.
Preserve source revisions and byte hashes separately unless the discovered schema explicitly accepts them.
If the eventual adapter cannot represent dynamic loaded categories, callback transitions, exact held identities, or shared RNG state, retain the blocker and classify the affected selection or retention probability unresolved.

No engine balance conclusion, exact live selection probability, or implementation completion claim is made.
