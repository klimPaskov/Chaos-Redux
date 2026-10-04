# Event014 Larder logistics owner plan

Date: 2026-10-03.
Owner: `chaosx_scripted_system_architect`, resumed plan-only assignment after prior owner `01a10254` became unavailable.
Disposition: implemented source after the parent's 2026-10-04 baseline/application authorization, pending parent review and auditor comparison.
Current implementation and validation limits are in [the source handoff](2026-10-04_larder_logistics_implementation.md).
Acceptance basis: the parent's instruction in this assignment accepts retained part 7 lines 210–214 and the full route/distance loss plus territory/development capacity surface.
Acceptance update, 2026-10-04: the parent accepted structural placement, dispatched/received loss accounting, post-annex finalization and the separate generation guard within the full spec scope.
The parent accepted the owner adjustment `capacity_base = 1200`, retaining coefficients 100/50, the existing 5-point flag score and the 5000 ceiling, with no AI weight retune.
The parent selected a documented-component `meta_effect` implementation using frozen regular capital targets and true state `GetID` strings instead of the untested composite temporary-target argument.
The earlier source freeze was lifted explicitly by the parent after the captured partial baseline was delivered.
The completed lifetime repair `a0a6825e7` is preserved.
No source, GUI, data observation field, localisation, source gate, asset, workbook, Git index, commit, game, or log changes were made.

## Evidence and baseline synchronization

Evidence is [source inventory, reference excerpts, SHA-256 hashes, baseline synchronization and arithmetic](2026-10-03_larder_logistics_owner_plan_evidence/source_reference_and_baseline_evidence.json) and [connected MCP requests/results](2026-10-03_larder_logistics_owner_plan_evidence/mcp_evidence.json).
The [final follow-ups, exact domain requests and live schemas](2026-10-03_larder_logistics_owner_plan_evidence/mcp_final_followups.json) supersede any awaiting-result placeholder in the first MCP evidence file.
The [accepted code proposal](2026-10-03_larder_logistics_owner_plan_evidence/2026-10-04_accepted_code_proposal.md) and [acceptance/reference evidence](2026-10-03_larder_logistics_owner_plan_evidence/2026-10-04_acceptance_reference_evidence.json) supersede the original base-1000 arithmetic examples and temporary-target parser proposal.
The [accepted-construction MCP reference reads](2026-10-03_larder_logistics_owner_plan_evidence/2026-10-04_acceptance_mcp_reference_evidence.json) retain installed GetID/meta definitions, offline meta and namespace rules, exact line spans and source revisions.
The earlier evidence remains an unchanged record of the initial inspection and proposal.
All line references identify the inspected source hash, not guaranteed positions after another parent's edit.
The effects hash is `f045bfea8c075818f1cfd3959bc92f02d4708186eb5718834fe8f3305f79e563`.
The frozen baseline is `docs/plans/014_cannibalism_plans/2026-10-03_larder_logistics_probability_audit/evidence/baseline/source_baseline_manifest.json`.
All nine copied files match their manifest hashes.
Current events, effects, constants, decisions, MTTH, triggers, AI strategy and requirement localisation match their copied baseline bytes.
Only `localisation/english/014_cannibalism_l_english.yml` differs, at descriptions `chaosx.nr14.60.d` and `.62.d`, where colour markup was removed.
Its current hash is `5e555ec139c3540eb9432ecf9d2fa7a524c23ea366bdae18b5283b587ed61b36`.
This is consistent with the reported colour-only `87503` work and does not change the inspected economy sources.
No baseline file or manifest was replaced or refreshed.

Auditor `01a10385`, routed as `chaosx_ai_probability_auditor`, owns the baseline and future same-scenario comparison.
The inherited successful `probability-inspect-669879e6f1b5.json` is preserved.
This resumption also starts probability work with a successful narrow `hoi4.probability_inspect` for `cannibalism_unified_centralize_larder`.
That adapter returns decision scores, not normalized choice probabilities.
The successful inspection establishes discovery only, not completed baseline evaluation or balance acceptance.
The auditor's scenario fixture and completed evaluate/sweep evidence were not supplied in this interrupted assignment.
Do not patch weighted destination predicates, thresholds or costs until the parent confirms that baseline and the frozen `stale_generation_no_transfer` scenario.

## Findings that determine the design

`cannibalism_apply_inherited_host_identity_to_cbl` clamps and publishes twice at effects lines 12112–12113 and 12179–12180.
CBL receives the donor's capital state at 12485–12488 and explicitly sets that same capital at 12493, but annexes the remaining donor at 12563–12566.
Applying the effective territory cap during identity inheritance would use only that initial transferred state and discard stores before the remaining territory arrives.

Later absorption credits and clamps the host through `cannibalism_add_current_warlord_larder_to_unified_host` at 12640–12650 before annexation at 12752–12755.
Autonomy uses that same credit helper at 12799 and creates a subject at 12800, without annexing its land.
These transaction types need different finalization placement, not estimated extra states inside a generic clamp.

`cannibalism_unified_refresh_contract_capacities` rebuilds the existing development score at 12907 onward.
Its 50 Larder flag contributions at 12986–13035 add `constant:cannibalism_unified_contract.point`, which is 5, not 1.
The proposed coefficient of 50 therefore adds 250 storage per contributing flag.
The score includes completed route/unlock contracts and some risk flags, so it is an existing contract-depth proxy, not a measured count of storage buildings or network nodes.
The storage operation's state flag `cannibalism_unified_storage_network_active` at 14671 does not independently add this score.
Do not introduce a second state-storage ledger or silently reinterpret the score as a flag count.

The shared actor pulse has a local 2000 clamp at 2264 and can include active unified countries.
Replacing only the eight global-ceiling sites would leave a later pulse capable of reducing a large unified stockpile to 2000.
The shared foreign-seed debit at 11125 also needs a caller-scope review and route-aware finalization wherever a unified caller reaches it.

## Proposed helpers and country API

These are owner-private Event014 helpers in `common/scripted_effects/014_cannibalism_effects.txt`.
The existing shared dynamic registry has no matching Larder helper.
No central router, wrapper skill or global helper relocation is proposed.

| Helper | Scope | Inputs and defaults | Outputs | Side effects and direct call sites |
| --- | --- | --- | --- | --- |
| `cannibalism_refresh_larder_effective_capacity` | Any existing country | Current controlled states and refreshed existing contract score for CBL/transformed Wendigo, with missing score interpreted as zero | Country regular `cannibalism_larder_effective_capacity`, plus bounded territory and development contributions for an owner API if the parent accepts those optional breakdown fields | Rebuilds unified contract score before reading it, calculates capacity, never changes stores, never publishes the global Larder mirror. Ordinary countries receive the existing local cap of 2000. Call from the existing profile refresh owner, constructor finalization and transaction clamp. |
| `cannibalism_clamp_and_publish_current_larder` | Country | Existing stores and the capacity API, no inferred transaction inputs | Clamped country Larder and, for the legitimate unified host only, `global.cannibalism_global_larder` | Refreshes capacity and clamps once. Ordinary country branch retains its existing local bound and does not overwrite the global mirror. Use at audited gain/debit/pulse boundaries and after territory transactions. |
| `cannibalism_prepare_larder_transfer_quote` | Explicit donor country | Explicit regular source/destination country targets, frozen pre-annex source/destination capital state pointers, caller-provided existing route fraction | Caller-owned unscoped temporary dispatch, received amount, distance, loss fraction and result | Quote only. Missing or invalid endpoints fail closed, with no zero-distance fallback. Call before annexation from opening inheritance, later absorption and autonomy. |
| Existing `cannibalism_add_current_warlord_larder_to_unified_host` | Donor country | Successful prepared quote and explicit destination target | Existing country store mutations | Debit dispatch once and credit received once. Remove its premature recipient clamp for absorption. Autonomy finalizes immediately after tribute/subject transaction. Preserve donor local clamp. |
| Proposed generation guard inside `cannibalism_has_valid_unification_destination` | Any existing caller of the trigger | Existing global host pointer and positive expected host generation | Boolean validity only | No state writes. Preserve current destination predicates and add expected/live generation proof. This is a separate baseline-sensitive change. |

The normal-country effective-capacity API is required so the parent can show a correct capacity in existing tooltips and GUI data projections.
It must not replace `cannibalism_unified_larder_capacity`, which remains a contract score used by category gates.
The GUI/data API proposal `2026-10-03_gui_required_fields_data_api.md` is another owner's proposal and remains unchanged.
The parent chooses its exact display field wiring after review.
No new visible mechanic value, layout or control is introduced by this plan.

Every temporary quote output must be allocated inline in the actual consuming constructor, absorption owner or autonomy owner before nested helper calls and before either country scope.
Helpers overwrite these existing output slots rather than introducing storage in an inner helper frame.
Use unscoped temporary names and never `ROOT.temp`, `PREV.temp` or a scoped temporary country token.
Keep all 107 completed caller allocations and the 67 source projections from the lifetime repair intact.

## Constants and tuning table

Add one `cannibalism_larder_logistics` fixed-point schema group to `common/script_constants/014_cannibalism_constants.txt` after the baseline is approved.
Accepted keys are `capacity_base = 1200`, `capacity_per_controlled_state = 100`, `capacity_per_development_point = 50`, `distance_loss_divisor = 10000`, `distance_loss_maximum = 0.60`, `zero = 0`, `one = 1`, and `minus_one = -1`.
Keep the existing `cannibalism_unification.global_larder_maximum = 5000` as the single hard-ceiling authority and retain the existing ordinary `cannibalism_consumption.larder_max = 2000`.
Do not duplicate either ceiling in the new group.
All existing route fractions and preparation/relief bonuses remain in their current groups.
No AI weight or on-action tuning is added.

`effective_capacity = min(5000, 1200 + 100 * current_num_of_controlled_states + 50 * refreshed_cannibalism_unified_larder_capacity)`.
`distance_retention = 1 - min(0.60, max(0, frozen_capital_distance) / 10000)`.
`received = dispatch * distance_retention`, where `dispatch = donor_store * existing_route_fraction_with_existing_contract_bonus`.
Clamp the route fraction to the existing valid 0–1 transaction range before applying it, so invalid inputs cannot mint stores or over-debit a donor.
Use variable arithmetic and existing fixed-point precision, with no unsolicited integer rounding.

| Current states | Existing score | Accepted effective cap |
| --- | --- | --- |
| 0 | 0 | 1200 |
| 1 | 0 | 1300 |
| 2 | 0 | 1400 |
| 1 | 5, one flag | 1550 |
| 10 | 0 | 2200 |
| 10 | 50, ten flags | 4700 |
| 40 | 0 | 5000 |

The base is chosen to produce a minimum one-controlled-state host cap of 1300 instead of the former proposal's 1100.
That host can hold the unchanged AI reserve `800 + 400 = 1200` and can exceed the strict 1200 countdown-bonus threshold without first gaining territory or a development flag.
This adjustment changes storage capacity only and does not retune weights, reserve predicates or bonus thresholds.

| Distance units | Retention | Submission .85 | Surrender .65 | Autonomy .20 |
| --- | --- | --- | --- | --- |
| 0 | 1.00 | .85 | .65 | .20 |
| 1000 | .90 | .765 | .585 | .18 |
| 3000 | .70 | .595 | .455 | .14 |
| 6000 or more | .40 | .34 | .26 | .08 |

Submission preparation adds the existing .10 before the distance multiplier.
Autonomy manipulation applies its existing relief before the distance multiplier.
Opening-host inheritance retains its existing 1.00 route factor.
Distance is an engine map-distance value whose physical unit is not stated by the cited documentation.
Do not label the divisor as kilometres without additional evidence.

## Exact transaction placement

1. Opening CBL creation captures the selected donor country and its capital before the capital's existing owner/controller transfer.
   Reuse `cannibalism_unification_capital_state`, which is explicitly assigned as CBL's capital by current source.
   Both frozen endpoints are that state, so opening-host distance is exactly zero by the existing transaction's capital policy, not an invalid-endpoint fallback.
   Quote before donor cleanup, preserve identity/route/bootstrap additions and defer both Larder clamps and both global publications inside `cannibalism_apply_inherited_host_identity_to_cbl`.
   Feed the quote's received amount into the existing identity assignment once, without an additional call to the later-donor credit helper.
   Finalize in CBL immediately after `annex_country` returns at 12566, with a fresh contract score and actual CBL controlled-state count, before publishing the host/continuing reports.
2. Later retained-command and surrendered-warband absorption capture the real donor and unified recipient capitals before migration, tag switch or slot preparation.
   Keep the existing migration-success prerequisite.
   Debit dispatch and credit the distance-adjusted received amount once before donor teardown, retaining current route identity and history handling.
   Defer the recipient clamp in the credit helper and finalize in the explicit recipient scope immediately after annexation at 12755.
   Never count donor-owned or donor-controlled states by projection or addition before the engine transaction finishes.
3. Autonomy captures both countries and capitals before changing disposition.
   Debit the existing tribute dispatch from the donor and credit only the distance-adjusted amount to the recipient.
   Transit loss is `dispatch - received` and is removed, rather than silently left in the donor as if the convoy never departed.
   The donor retains the remainder after dispatch and its current local clamp.
   Finalize the recipient after its existing puppet transaction using only the recipient's own controlled states.
   No donor territory credit, equipment transfer, population transfer or researched-technology union occurs on this route.
4. Initial transformed Wendigo captures its in-place destination capital and the selected primary donor capital before `cannibalism_prepare_wendigo_merge_identity` and before annexation.
   Apply distance only to the inherited donor Larder, then retain current identity/bootstrap/route rewards.
   Preserve the existing identity assignment rather than adding a second primary-donor credit or adding the transformed country's previous stores to a snapshot that currently replaces them.
   Defer identity clamps exactly as for CBL.
   For absorbable donors, finalize after the existing primary-donor annexation at 18890 and once at constructor return if needed to cover a failed migration without premature discard.
   For the two-human branch, preserve `cannibalism_inherited_larder = 0` and `cannibalism_primary_warlord_donor_can_be_absorbed = 0` at 18966–18969, and finalize against the transformed country's actual territory after the nonabsorbing constructor path.
   Skip the donor quote/debit/credit commit entirely on this branch, so a prepared quote cannot accidentally restore the overridden zero snapshot.
   Do not reinterpret that zero as a missing snapshot, add the nonabsorbed human's stores or add their territory.

No intermediate helper should trigger the effective-cap clamp while an annex transaction is open.
Prefer explicit finalization placement and avoid a persistent defer flag.
If a parent implementation needs a temporary defer input for the shared identity helper, every caller must allocate it and pass it explicitly, and its default must remain safe for existing standalone callers.
Do not let nested consumption, profile rebuilding or presentation calls accidentally finalize the construction transaction.
Keep technology union, troop transfer, history receipts, population ledgers, route rewards and equipment/fuel additions in their existing transaction owners.
This proposal adds no population operation, consumption event or resource duplication.

## All clamp and refresh hooks

The bounded source inventory finds eight global-ceiling clamps and eight local clamps in the owner file.
No other engine source contains a Larder clamp or global mirror write.
The only external global mirror reference is the achievement trigger at triggers line 144, and the ceiling definition is in constants line 1785.
The evidence file retains all 26 clamp/mirror sites, all 27 direct Larder mutations and the refresh/annex hook inventory.

| Existing helper and line | Required migration |
| --- | --- |
| `cannibalism_consume_current_state`, 4210–4211 | Unified branch finalizes with fresh effective capacity. Ordinary branch 4215 retains its local cap. Keep the exact population transaction and measured outputs unchanged. |
| `cannibalism_pay_focus_closure_larder_cost`, 6406–6411 | Use the country-aware finalizer after the existing debit. |
| `cannibalism_apply_inherited_host_identity_to_cbl`, 12112 and 12179 | Defer clamps/publications to each constructor's final territory transaction. |
| `cannibalism_add_current_warlord_larder_to_unified_host`, 12644–12648 | Retain the donor local clamp and move recipient finalization to the absorption/autonomy owner. |
| `cannibalism_unified_pay_current_larder_cost`, 14343–14344 | Finalize after the existing cost debit. |
| `cannibalism_unified_execute_convoy_harvest`, 15170–15171 | Finalize after its existing grant. |
| `cannibalism_pay_wendigo_larder_and_command_cost`, 17919–17924 | Finalize after the existing Larder debit without changing command payment. |
| `cannibalism_process_current_actor_pulse`, 2264 | Replace this mixed-scope local clamp with country-aware finalization in the existing bounded actor pulse. Do not add a new daily/world loop. |
| `cannibalism_execute_deliberate_foreign_seed`, 11125 | Review all reachable actor types and use country-aware finalization for shared unified callers, retaining the exact ordinary debit and cap. |
| Warlord-only local helpers, 16764, 16791, 17023 and 17077 | Preserve their existing local clamps after confirming the current warlord predicates. |

At `cannibalism_unified_refresh_operational_profiles` line 14320, calculate the capacity API after rebuilding contract depth and before any consumer reads it.
The capacity helper must not recursively call the full operational-profile refresh.
Existing `cannibalism_unified_focus_finalize_reward` already rebuilds contracts and profiles at 14329–14332, so route it through the same capacity update without duplicating the full profile calculation.
Refresh after store mutations, completed contract flag changes, constructor/absorption territory changes, and through the existing actor pulse to catch external control gain/loss.
An on-demand tooltip/data projection can call the calculation-only API for freshness without clamping or writing the global mirror.
State construction/storage operations continue their existing record/profile path and do not acquire an invented capacity ledger.

## Separate host-generation guard

Proposed change at `common/scripted_triggers/014_cannibalism_triggers.txt:5348` keeps `has_event_target` and the current `cannibalism_is_valid_unification_destination` predicate.
Add `has_variable = global.cannibalism_unification_host_generation` and require that value to be strictly above zero.
Inside the explicit host scope require `has_variable = cannibalism_actor_generation` and exact equality to the positive expected global value.
This follows the existing equality pattern in `cannibalism_selected_unification_host_is_valid` at 3480–3492, with the requested additional positive expected-generation proof.
The donor selector sets expected generation at 12034, clears it before reselection at 12040, the CBL constructor republishes its generation at 12572, and the transformed Wendigo constructor publishes its own generation at 19008.
The primary Wendigo constructor uses its own explicit destination validation while forming the host, so do not insert the post-reveal guard before its generation publication and accidentally block construction.
Audit every consumer of the common guard, including absorption, autonomy, resistance, challenge and terminal integration.
`stale_generation_no_transfer` must prove no debit, recipient credit, annexation, technology transfer, subject creation or slot retirement against a mismatched recycled host.
Keep triggers frozen until the auditor has the named baseline, then require same-scenario `hoi4.probability_compare` through `chaosx_ai_probability_auditor`.

## Paid gates, reachability and early softlock risks

The low proposed unified cap differs from the unchanged ordinary cap, so small unified hosts need explicit threshold scenarios before values are finalized.
Current main unified Larder costs are 25–100, with hostility surcharge values 25, 50 or 75 chosen by tier.
Their individual Larder requirements fit the proposed minimum capacity, but all manpower, equipment, command, target and category gates still apply.
Storage projects spend manpower, support equipment and trains at 14664–14669, with no Larder debit, so the proposed cap creates no direct pay-Larder-to-grow-cap circularity for that action.
Its category still requires contract score 50 and the existing category/storage flags at triggers 3747–3755 and 4049–4055.
With point value 5, that gate means ten contributing flags, not fifty storage projects.
Do not retune those gates in this owner plan.

Wendigo lock/countdown minimum is 800 and the largest inspected launch/acceleration payment is 400.
The existing AI reserve helper at triggers 5077–5085 requires `800 + payment`, so a 400-cost action needs 1200 Larder.
An undeveloped one-state unified host now has the accepted cap 1300, so that capacity permits the existing inclusive 1200 reserve requirement.
At exactly 1200 stores the reserve is satisfied, while the strict bonus remains false, and at 1201 or 1300 stores the bonus can be true if its other conditions hold.
This resolves the earlier capacity-only reachability constraint without changing AI weights, but does not guarantee a host can actually obtain the stores or meet every other gate.
The countdown bonus at effects 19189 uses a strict `Larder > 1200`, which one-state and two-state zero-score hosts can attain under the accepted cap.
A zero-state zero-score host remains capped at 1200 and cannot earn that bonus, consistent with the accepted adjustment targeting hosts with controlled territory.
The existing world-end Larder threshold 750 and functional-Larder achievement threshold 400 fit the proposed minimum, but this does not prove their other terminal conditions or progression.

Test costs after inherited-route discounts, hostility refresh, depleted equipment/fuel, exact inclusive affordability, post-payment reserves, territorial loss and capacity saturation.
Do not claim broad balance or cost reachability from the arithmetic table alone.
The one cold-host decision inspection is partial and has unbound inputs, so it does not close those scenarios.

## Targets, cleanup and syntax boundary

Reuse the existing regular source/destination country targets where their roles match exactly, and keep opening CBL's `cannibalism_unification_capital_state`.
Add transaction-private regular `cannibalism_larder_source_capital` and `cannibalism_larder_destination_capital` targets for the frozen endpoints.
Do not use a temporary state pointer as the `distance_to` target argument.
Regular event targets clear with the effect chain, and this transaction needs no new global target.
Capital capture must return positive proof from each actual native capital-state scope into caller-owned temporary storage before a quote can run.
A positive scalar state pointer alone is not object-validity proof, and `scope_exists` must not be used to validate variable scopes.
Overwrite every transaction input on each call, reset output/result slots in the owning caller before capture, and retain no permanent distance or donor receipt cache.
Only existing host targets/generation persist under their existing owner cleanup.
The country effective-capacity field is derived and must be refreshed on control changes and cleared by the existing owner cleanup/slot reset if present there.
Never clear unrelated global targets.

Installed documentation confirms state `distance_to`, country `capital`, country `num_of_controlled_states`, variable clamp bounds, fixed-point `constant:` access, state `GetID` and `meta_effect` parameter substitution.
Offline Data structures lines 429–451 confirm object-valued temporary variables, `var:` scope use and caller lifetime.
Lines 551 and 1460 cover targeting rules, and line 1681 specifies a state target for `distance_to`.
The accepted expression injects the two frozen regular state targets' true IDs into a meta text block.
Its exact body is `[SOURCE] = { set_temp_variable = { cannibalism_transfer_distance = distance_to@[DESTINATION] } }`, with `SOURCE = "[cannibalism_larder_source_capital.GetID]"` and `DESTINATION = "[cannibalism_larder_destination_capital.GetID]"`.
For source state 123 and destination state 124 this expands to `123 = { set_temp_variable = { cannibalism_transfer_distance = distance_to@124 } }`.
Installed `loc_objects_documentation.md:629–647` defines state `GetID`, and `effects_documentation.md:4833–4851` defines meta substitution into an executable scope block.
Offline Effects lines 4617–4646 establish evaluated localisation-string meta parameters, Data structures line 301 establishes the omitted `event_target:` namespace prefix, and lines 1671/1681 distinguish the internal state pointer from true state ID and specify the distance state target.
The exact saved-target `.GetID` meta parameter pattern exists in `common/scripted_effects/006_independence_wave_decision_effects.txt:1065–1075`.
These establish the namespace and parameter construction using documented components, without a composite dynamic target argument or zero-distance fallback.
Caller-owned `cannibalism_transfer_distance` must be allocated before capture/helper/meta scopes, initialized to the negative sentinel, and overwritten by the generated static state read.
Negative or unwritten distance leaves the quote rejected, while a documented same-state zero distance remains valid.
Runtime execution and the complete future transaction still require their apply-phase validation and are not claimed from this proposal.

Vanilla's primary precedent is `common/operations/00_operations.txt:1468–1482` and `1632–1646`, plus `POL_historical_operations.txt:218–232`.
Their operation `target_weight` blocks read distance in the state candidate scope with `distance_to@ROOT.capital`, then divide/clamp/multiply it.
Mirror the state-to-state calculation structure and replace their reliable operation ROOT with explicit transaction endpoints here.
Do not copy their target weights, balance numbers or ROOT assumption.

## MCP coverage, limitations and implementation sequence

Connected routes are verified from live tool metadata and actual narrow calls.
Reference context/search/read, probability inspection, source lookup, unified focus inspection and event-response trace returned.
The context bundle omitted Triggers, Effects, Modifiers and Scopes because of its limit, so it alone does not establish detailed coverage.
The retained direct installed/offline excerpts cover the specific planned variable, clamp, scope and target operations.
Detailed reference-read results and their source revisions are retained separately.
The event-response trace is `EVENT_INSPECTED_PARTIAL`, with whole-workspace helper projections/lifecycle analysis deferred and helpers unexpanded.
The unified focus inspection reports 108 focuses and no tree-specific diagnostic, with a separate vanilla continuous-focus localisation warning.
The linked Wendigo focus inspection also returned, covering 28 focuses with no tree-specific diagnostic and the same separate vanilla continuous-focus warning.
The exact source lookup returned the credit helper at 12640–12650, but indexed references were incomplete with 18450 unresolved references, so the direct owner hook inventory supplies source coverage without claiming complete MCP consumers.
The event trace and decision artifacts have truncated inline inventories and have not been fully retrieved for whole-workspace review.
They are linked evidence, not exhaustive acceptance.
The mistaken initial selector for event `.210` is retained as an attempt only, and the corrected relevant selector is event `.71`.

`hoi4.script_validate` is not exposed in this connected tool list.
Advanced helper expansion, job inspection/cancellation and native MCP tasks were not used because server health/version and client task negotiation were not verified.
No map rewrite or map topology helper is proposed.
GUI inspection is required only for its linked data consumer and does not authorize GUI edits or visual acceptance claims.
The GUI route's final result and scenario limits are recorded in the evidence rather than treated as a completed render review.
The revealed-command retry returned `GUI_INSPECTED`, scenario `E014_LARDER_OWNER_REVEALED_20261003`, revision `e414e00683b9537578a5227500bc43278470f165f782e079318ac11f9637f135`, inspecting 17 elements.
It leaves seven fidelity facts unresolved and three unsupported, including the unbound global Larder display in the identifier-only scenario.
It also reports overlap, static-fallback, partial-animation, zero-size and clipping warnings which remain parent/UI-worker review findings, with no visual acceptance claim or edits to protected assets.
The exact narrow Wendigo GUI request for `cannibalism_wendigo_command_window` with scenario `E014_LARDER_OWNER_WENDIGO_20261003` had no observed final result before client observation ended for this prompt delivery.
Its state is unresolved, not a proven service failure or unavailable route, and no server job cancellation is claimed.
Consequently its linked-consumer evidence remains open for the parent before any consumer implementation or acceptance.
No event/focus/GUI render comparison, probability evaluate/sweep/compare or in-game observation was claimed for this plan-only delivery.

Parent implementation sequence:

1. Retain the parent's accepted structural placement, dispatch-loss accounting and base-1200 tuning, and preserve the unchanged reserve and strict bonus predicates.
2. Obtain the auditor's completed frozen baseline and exact named scenarios, preserving the trigger snapshot and stale-generation scenario.
3. Use the documented frozen regular-target `GetID` meta construction in the accepted evidence proposal when source application is authorized, then implement the private capacity/quote/finalization helpers and their caller storage.
4. Move constructor and absorption clamps to post-annex finalization, finalize autonomy without land credit, and preserve the two-human zero branch.
5. Migrate all audited gain/debit/pulse hooks and the separate generation guard, then update owner helper documentation with scope, inputs, outputs, defaults, side effects, cleanup and complete usage examples.
6. Add the Event014 owner API entry to matching dynamic-helper documentation without moving private orchestration into the shared registry, and coordinate existing GUI/tooltip consumers with their owners.
7. Have the probability auditor evaluate, sweep and compare identical scenarios against immutable before sources, including zero/one/two-state hosts, one/ten development flags, distance 0/1000/3000/6000/10000, preparation/relief contracts, stale generations, autonomy, both-human Wendigo and post-annex actual-state counts.
8. Recheck failed migration, repeated transactions, wrong ROOT, donor capital relocation, unavailable endpoints, capacity shrink, profile refresh ordering, and exact population/equipment/technology preservation before the parent claims implementation complete.

## Delivered work and remaining work

Delivered files are this owner plan, its accepted code proposal and its bounded source/reference/baseline, acceptance and MCP evidence files.
Helpers, constants, call sites and cleanup were designed only and have not been implemented.
Meaningful completed checks are the complete owner clamp/mutation inventory, transaction-order source review, frozen-baseline byte synchronization, exact localisation-only diff, development-score arithmetic and early reserve/bonus reachability analysis.
Skipped validation is the implementation compare cycle, full weighted scenario audit, runtime execution of the documented static meta expansion, visual before/after review and engine observations, because this assignment is plan-only and source remains frozen.
The composite temporary-target parser is excluded from implementation and needs no apply-phase verification.
Skills used are `chaos-redux-events`, `chaos-redux-subagents`, `chaos-redux-decisions-missions`, `chaos-redux-focus-trees` and the linked-consumer guidance in `chaos-redux-scripted-gui`.
No skill was created or updated.
No gameplay simplification, new story route, country/package, AI weight, world daily loop, model or portrait work was introduced.
All seven model packages, 56 native portraits and four protected Hannibal portraits remain outside this assignment.
The plan's source implementation is delivered in the 2026-10-04 implementation handoff, with parent review, probability comparison and engine acceptance still open.
