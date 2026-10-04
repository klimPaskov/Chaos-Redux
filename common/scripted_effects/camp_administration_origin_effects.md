# Camp physical-host provenance observer

Disposition: implemented bounded observer and custody/occupation owner integration, with parent-owned country/lifecycle/presentation integration and acceptance queued.
Acceptance basis: the parent accepted the joint physical-host observer and sticky freeze architecture on 2026-10-03 within the user's directly approved pause policy.
The parent authorized helper scaffolding followed by custody/occupation effects, their paired triggers/docs and narrow source-harness integration on 2026-10-03.
Country programme/reform effects, broader lifecycle adapters, GUI, localisation, costs, AI and final acceptance remain parent-owned.
This module does not establish integrated package completion.

## Publication boundary for the native-cleanup repair

The 2026-10-04 live-QA repair publishes this observer library, its inspection triggers/constants and its three exact row-consumer dependencies as passive definitions.
The scoped publication also guards removal of the existing national economy modifier.
The broader custody/occupation registration, country, terminal and interface integration described below remains in the shared working tree and is outside that repair commit.
No new recurring callback or admission/death route is activated by publishing these definitions alone.
Working-tree source scenarios and the supplied live errors are recorded in `../../docs/testing/live_qa/20261004_camp_native_cleanup/repair.md`; no agent-run live retest is claimed.

## Invariants and scope

All public effects and the public readiness/inspection triggers operate in the actual physical state scope.
Temporary variables are unscoped and use the `camp_origin_` namespace.
Persistent observation variables and flags belong to that state.
The inspector uses existing `camp_admin_responsible_country` and `camp_occ_responsible_country` pointers, custody state arrays and occupation country arrays filtered to the actual host.
It creates no event target, global target, global registry, row or periodic callback.
It calls no population-changing effect, Deaths registration, cause projection, admission, movement or release.
The observer/inspection/baseline APIs never change either family's rows or reservation.
The common reconciliation adapter delegates only the exact uniquely pending row to its existing custody or occupation owner, which commits conservative outside-removal metadata and acknowledges that receipt.

Mixed-origin outside loss sets sticky `camp_origin_ambiguous` before any owner may retire or consume original rows.
Repeated observation, natural growth, a closed site, an unrelated incoming credit and measured known-transaction adjustment cannot clear that flag.
Multiple positive rows are contained even if they share one original state because the selected exact row or root cannot be inferred from a territorial loss.
The inspector reports whether immutable lineages differ and keeps occupation and custody memberships distinct.
A unique positive row instead retains a separate pending conservative-retirement receipt, so a second observation cannot discard an unconsumed outside signal.
The acknowledgment for that unique row never clears mixed ambiguity.

## Public helper map

| API | Kind and scope | Inputs | Outputs | Persistent side effects and defaults |
|---|---|---|---|---|
| `camp_origin_initialize_host` | State effect | Existing state population, shared territorial Deaths and row registry | Common opening observation fields | Initializes once. Empty valid host uses current totals. Existing live host can adopt its nonnegative occupation observation pair. Existing living membership without that pair gets an unverified-baseline reason and sticky ambiguity, with zero invented loss |
| `camp_origin_inspect_host_rows` | State effect with read-only trigger body | Existing aligned rows and authority pointers | `camp_origin_rows_valid`, live row count, mixed-lineage result, family sums, physical shortfall and first-row identity/history | Temporary writes only. Invalid or absent required registry proof returns zero validity. An entirely empty unregistered host is valid |
| `camp_origin_host_rows_valid` | State trigger | Same registry input | Boolean, plus the same temporary inspection outputs | Temporary writes only. Resets all public inspection outputs on each call and fails closed on malformed or over-limit arrays |
| `camp_origin_host_provenance_ready` | State trigger | Initialized common baseline and current rows | Boolean | No persistent writes. Requires no sticky ambiguity, unverified baseline, unresolved records, pending unique-row retirement, fresh unobserved decline/shared counter change or current physical shortfall |
| `camp_origin_observe_host` | State effect | Common baseline, current physical totals and rows | `camp_origin_observation_ready`, `camp_origin_observed_net_decline_k`, `camp_origin_observed_shared_loss_k`, `camp_origin_observed_outside_signal_k`, counter-regression output and inspection outputs | Consumes the observation interval once, sets containment reasons before owner row mutation and advances the physical baseline. Unique-row retirement stays pending until acknowledged |
| `camp_origin_adjust_known_receipt` | State effect | Complete temporary measured before/after snapshots, contract and expected sequence | `camp_origin_known_adjustment_accepted`, then fresh residual observation outputs on acceptance | Updates only the common baseline from the measured receipt, increments its sequence and observes remaining unexplained change. Rejects missing/stale/malformed receipts and consumes all request inputs on either path |
| `camp_origin_reconcile_host_membership` | State effect | Current physical host and existing owner arrays | `camp_origin_reconciled_custody_k`, `camp_origin_reconciled_occupation_k` | Observes once, delegates an exact sole-row retirement to the owning family and exports its accepted actual receipt. Mixed rows remain frozen |
| `camp_origin_quarantine_transaction` | State effect | Actual endpoint after preserved incomplete transaction measurements | Sticky transaction/ambiguity flags and a separate raw checkpoint | Preserves the canonical verified opening and checkpoints subsequent physical territory changes without counting the incomplete movement as outside loss |
| `camp_origin_commit_endpoint_observation` | Internal state effect | Required `open_sequence`, `open_population_k`, `open_state_deaths_people`, `after_population_k`, `after_state_deaths_people` script parameters naming caller tokens | Known baseline result and residual observation | Used only after complete commit/inverse, delegates measured adjustment, quarantines an endpoint if its baseline receipt rejects |
| `camp_origin_occupation_host_ready_for_reform` | State trigger, PREV is owner country | Existing owner's bounded `camp_occ_states` entry | Boolean | Consumes an explicit temporary owner binding to inspect the actual owner registry when host markers are missing. Rejects live rows with missing proof and permits structurally valid empty history without generating a release |
| `camp_origin_acknowledge_single_origin_reconciliation` | State effect | Unique-row pending record, temporary contract, expected sequence and completed owner retirement amount | `camp_origin_single_reconciliation_accepted` | Verifies the exact row identity, surviving amount, outside-removal increment and unchanged death/release history. Clears only the unique-row pending record after a full valid ledger receipt, otherwise remains inert. Consumes all request inputs |
| `camp_origin_mark_ambiguous` | Internal state effect | Current common observation sequence | Sticky flag and first ambiguity sequence | Idempotent and preserves the first ambiguous epoch. No clear counterpart exists |
| `camp_origin_accumulate_inspection_row` | Internal trigger in the scanner's current scope | Staged `camp_origin_candidate_*` temporary fields | First lineage/history, family sums, row count and mixed-lineage result | Temporary arithmetic only. Its true result lets the bounded scanner finish. It is not a public cohort validator |

Each inspection result is temporary and can be overwritten by a later host inspection in the same chain.
Copy an output into a caller-specific temporary or durable owner receipt before inspecting another host.
This namespace deliberately avoids the existing selected custody row, occupation active-row index, source/debit/bind receipts and transfer targets.

## Registry validation

Custody validation checks every existing aligned array, `camp_admin_row_count`, the next monotonic ID, a maximum 1,000-row count, sequential append-only IDs, legal current status, nonnegative membership, original state object, root and immutable authority.
Active custody rows must belong to the state's recorded responsible authority.
Inactive custody rows carry zero living membership.
Native custody root-zero rows remain distinct by immutable row ID.

Occupation validation checks the existing responsible country's array alignment, count, next ID, maximum row count and sequential append-only IDs.
It validates current row status and nonnegative membership, then reads positive active rows only where the recorded host equals the actual inspected state.
At that host, the original authority must be the country's recorded row owner, the root must be positive and the original pointer must resolve to an actual state.
The occupation host sum must equal state `camp_occ_remaining_k`, and the custody sum must equal `camp_admin_detainees_k`.
The monotonic-ID check matches the current append-only production registry and lets a later acknowledgment resolve the selected row by `id - 1` without confusing identity with a mutable index.
If a future registry removes/reorders elements, this contract must be updated before that change becomes consumable.

Each `all_of` scan is guarded by `constant:camp_origin_value.maximum_row_scan = 1000` before reading elements.
A larger registry fails closed rather than treating a scanned prefix as complete.
The shape and original-state checks use installed-documented `all_of`, conditional triggers, temporary arithmetic, variable scopes and `state = var:<pointer>`.
The tests mock those primitives and do not prove their live Clausewitz execution.

Physical shortfall uses the existing family population floors with the combined occupation and custody reservation.
It does not equate a building-capacity or population-share intake limit with proof of an outside death.
Occupation-only membership uses its existing `0.001k` floor, and a positive custody membership uses its existing `1k` floor.
No floor or mortality rate is changed by this module.

## Opening baseline and observation

The parent must call initialization after preparing a valid empty owner registry and before the first membership append.
That preserves ordinary fresh admission without guessing any prior interval.

```text
# Actual state. Existing owner initializes an empty aligned registry first.
camp_origin_initialize_host = yes
# Existing owner then performs its already validated admission or row append.
camp_origin_observe_host = yes
```

For an already living host, an existing nonnegative `camp_occ_observed_population_k` plus `camp_occ_observed_state_deaths` pair can be adopted once.
Initialization preserves the pending interval represented by that pair rather than replacing it with current physical totals.
This adoption does not prove that old sibling-family transactions were already excluded from the pair, so an unexplained mixed-host delta is conservatively contained.
A living custody-only host with no verified opening pair gets `camp_origin_baseline_unverified` and ambiguity without an observed loss amount.
The parent explicitly accepted this fail-closed baseline reason on 2026-10-03 and owns any future verified adoption contract.
Current totals alone cannot repair the missing interval.
Inherited `camp_occ_origin_estimated`, `camp_admin_origin_estimated` or state unknown-origin removal totals are retained as unverified evidence and never promoted into verified cohort rows.

Observation computes `max(previous_population_k - current_population_k, 0)` and `max(current_shared_deaths_people - previous_shared_deaths_people, 0) / people_per_k` separately.
Their maximum is returned as `camp_origin_observed_outside_signal_k` for the owner, and it is not an exact original-cohort victim count.
Growth can mask the first quantity while the shared Deaths delta still detects the loss.
Do not add the two quantities together because they can describe the same physical loss.
State cumulative and unresolved counters retain those facts separately.
Physical headroom shortfall is a current value, not a repeatedly accumulated loss.
A decreasing shared cumulative counter gets `camp_origin_counter_regressed`, preserves its prior counter value once and fails closed without inventing a positive death delta.

The common observation sequence advances when population, the shared counter or current physical shortfall changes.
Repeated identical observations are inert.
The first ambiguity sequence remains unchanged after further observations.
Last verified membership quantities update only on a clear fully reconciled observation or an accepted unique-row acknowledgment.
They stay frozen when ambiguity or conservative retirement is pending.

## Unique-row conservative retirement

On a positive outside signal or headroom shortfall at exactly one positive valid row, observation sets `camp_origin_single_origin_reconciliation_pending` and records that row's family, ID, original state, root, authority and before image.
`camp_origin_pending_single_removal_k` retains the conservative retirement budget, capped by the recorded before membership.
Repeated identical observation does not increase it.
A new observed interval can add its outside signal, while a persistent headroom shortfall is only a lower bound on the current pending amount.
This amount belongs to one verified original row and is a non-spendable reconciliation request, not an unknown-origin population pool.

The parent-owned outside-retirement helper must consume that exact row by its positive immutable ID, update its outside-removal total and family aggregate, and acknowledge the completed amount in the same effect chain.
It must not make a physical population change, record a camp death/cause or use newest-first selection across rows.
The module performs no retirement itself.

```text
camp_origin_observe_host = yes
if = {
	limit = {
		has_state_flag = camp_origin_single_origin_reconciliation_pending
		NOT = { has_state_flag = camp_origin_ambiguous }
	}
	# Parent uses camp_origin_pending_single_family and _row_id to retire exactly
	# camp_origin_pending_single_removal_k through its existing outside helper.
	# All aligned row and state aggregate changes must already be committed here.
	set_temp_variable = { camp_origin_single_reconcile_contract = constant:camp_admin_value.one }
	set_temp_variable = { camp_origin_single_reconcile_sequence = camp_origin_observation_sequence }
	set_temp_variable = { camp_origin_single_reconcile_amount_k = camp_origin_pending_single_removal_k }
	camp_origin_acknowledge_single_origin_reconciliation = yes
}
```

The acknowledgment checks the original row identity, new amount `before - retired`, outside-removal total `before_removed + retired`, unchanged deaths/releases and a valid current aggregate.
It also requires no later unobserved decline/shared loss and no current physical shortfall.
A partial, wrong-sequence or matching-amount receipt with fabricated row death remains rejected.
The required value-one contract token is set to zero after acceptance and rejection.
Its sequence and amount remain temporary snapshots, overwritten completely by every provider before rearming the token.
No caller tests their absence or reads them outside the guarded acknowledgment.
If all membership was retired, the append-only historical row still provides the identity proof.
There is no acknowledgment path from `camp_origin_ambiguous`, so this API cannot restore mixed provenance or clear an unverified opening interval.

## Measured known transaction adjustment

One-shot temporary inputs are `camp_origin_known_contract`, `camp_origin_known_observation_sequence`, `camp_origin_known_before_population_k`, `camp_origin_known_after_population_k`, `camp_origin_known_before_state_deaths_people` and `camp_origin_known_after_state_deaths_people`.
All are required, including explicit zero shared changes for movement and inverse receipts.
The expected sequence and before totals must match the host's common observation baseline.
After totals must be nonnegative, shared Deaths cannot decrease, and the shared receipt cannot exceed the current actual shared counter.
The signed population delta is bounded by the existing maximum receipt, and population/shared changes must resolve to whole people.
All requests default to rejection, and the required value-one contract token is set to zero on both paths.
The other five input snapshots remain temporary values and are completely overwritten by every provider before the next authorized call.
The zero token rejects an unarmed repeated call even though the snapshots still exist; this is an explicit authorization sentinel, not a claim that zero is equivalent to variable absence.

The caller must observe and obtain clear provenance before starting the operation, then capture its common sequence and before totals.
Stage actual local measurements from the physical operation and its single shared projection.
Commit all relevant row metadata before the adjustment calls the residual observer.
The adjustment updates the baseline to the measured after image, not a blindly copied current total.
An additional unexplained difference after that measured receipt remains visible to the observer and may contain the host.

```text
# Actual state, before a source-validated death or one movement endpoint.
camp_origin_observe_host = yes
if = {
	limit = { camp_origin_host_provenance_ready = yes }
	set_temp_variable = { camp_origin_known_contract = constant:camp_admin_value.one }
	set_temp_variable = { camp_origin_known_observation_sequence = camp_origin_observation_sequence }
	set_temp_variable = { camp_origin_known_before_population_k = state_population_k }
	set_temp_variable = { camp_origin_known_before_state_deaths_people = chaos_state_civilian_deaths_total }
	# Parent performs the existing measured physical operation, one projection
	# when applicable, and commits its exact row/aggregate receipt.
	set_temp_variable = { camp_origin_known_after_population_k = measured_local_after_population_k }
	set_temp_variable = { camp_origin_known_after_state_deaths_people = measured_local_after_state_deaths_people }
	camp_origin_adjust_known_receipt = yes
}
```

The example measurement names belong to the owner and are not module-created variables.
For two-endpoint movement, retain each endpoint's opening sequence and before image in distinct caller storage and stage the shared request names only when invoking its endpoint adjustment.
Do not inspect either endpoint as an outside interval between physical transfer stages and final commit or inverse completion.
A complete physical inverse can submit a zero-net before/after image, which advances the sequence once and prevents replay.
A failed inverse remains parent-quarantined with its measured residual and existing rollback flags at both endpoints.
The preview rejects the existing occupation transfer/custody rollback-failure flags, and observation promotes those flags into sticky `camp_origin_transaction_unresolved` and ambiguity without calling their measured movement a new outside death.
The parent must still preserve and mark the affected destination before its same-chain target expires because existing rollback flags may be present only on the source.
A failed transaction quarantine rejects known baseline adjustment because its physical and metadata inverse is incomplete.
Its canonical verified opening remains intact, while separate `camp_origin_transaction_observed_population_k` and `camp_origin_transaction_observed_state_deaths_people` checkpoints observe later territory changes.
A complete inverse may submit its measured zero-net receipt before any failure quarantine is established.
This accounting never authorizes another action at a quarantined endpoint.

`camp_origin_known_adjustment_accepted = 1` proves only that a bounded baseline receipt matched the staged sequence and snapshots.
It is not a transfer, source debit, destination credit, bind, death or release success result.
The existing physical and row receipts remain authoritative.
The helper cannot authenticate an arbitrary caller's declared measurements or identify an external loss from a boolean contract token.
The parent must bind these inputs to the existing measured transaction and inspect the resulting provenance readiness before another action.

## Persistent fields and cleanup

Observation fields are `camp_origin_observation_sequence`, `camp_origin_observed_population_k`, `camp_origin_observed_state_deaths_people`, `camp_origin_total_observed_net_decline_k`, `camp_origin_total_observed_shared_loss_k`, `camp_origin_unresolved_net_decline_k`, `camp_origin_unresolved_shared_loss_k`, `camp_origin_current_shortfall_k`, `camp_origin_last_verified_occupation_k` and `camp_origin_last_verified_custody_k`.
Reason fields are `camp_origin_ambiguity_sequence` and optional `camp_origin_regressed_from_state_deaths_people`.
Flags are `camp_origin_observation_initialized`, `camp_origin_ambiguous`, `camp_origin_baseline_unverified`, `camp_origin_records_unresolved`, `camp_origin_counter_regressed`, `camp_origin_transaction_unresolved`, `camp_origin_ambiguity_terminal` and `camp_origin_single_origin_reconciliation_pending`.
The unique-row pending before-image fields use the `camp_origin_pending_single_` prefix for family, original, authority, root, row ID, amount, outside-removal, death and release history.
Acknowledgment clears its before-image fields and pending flag and sets its request amount to zero.
Sticky ambiguity and its outside/baseline/transaction/counter reason/history fields are never cleared by this module.
`camp_origin_records_unresolved` reflects current structural validity when no outside signal occurred, so a valid reinspection can clear that availability error without clearing any existing ambiguity.
Malformed data accompanied by a physical/shared signal or an unverified opening remains sticky and cannot recover through an ordinary row repair.
Terminal closure must preserve them and stop owner operations through the existing package lifecycle.
There is no expiry, restoration action or complete external-loss provider here.

## Parent-owned caller map

| Existing owner seam | Required new calls |
|---|---|
| Empty custody initialization and occupation registration | Initialize the common host baseline before first living membership mutation, then observe the accepted new registry |
| `camp_occ_reconcile_external_population` and `camp_admin_refresh_capacity` | Observe once before any row retirement. Mixed/unverified/invalid host returns through containment without proportional, newest-first or unknown-pool continuation. Unique row uses exact conservative retirement plus acknowledgment |
| Exact death helpers and their selected/generic row consumers | Observe, reconcile a unique pending row if applicable, require fresh readiness before the physical debit, commit rows and the one shared receipt, then adjust the common measured baseline |
| Both endpoints of occupation movement and custody import | Observe/readiness before quotation and execution. Preserve endpoint opening measurements, commit or inverse completely, then adjust each endpoint from its measured receipt |
| Releases and reform | Require the same readiness in all affected state preflights and execution, including occupation-only hosts. No physical baseline adjustment is needed for ledger-only release |
| Workforce and institution output/progress | Deny frozen or pending living membership to productive consumers without hiding the operational site from observation or country all-site checks |
| Capture, unregister and terminal annexation | Preserve sticky evidence and freeze records while parent containment stops operations, outputs and project/selected references before active arrays are removed |
| Existing native decisions, Locations actions and Records | Parent wires readiness, meaningful blocked reasons and honest uncertainty wording in its own files. Hide implementation flags behind the owner custom-trigger tooltip |
| Existing CXT site setup | The same empty site initialization caller should establish this baseline. No separate fixture registry or periodic grant is added |

Custody initialization/capacity/admission/death/release/close, occupation enrollment/reconciliation/death, both exact movement endpoints and the custody import/bind path call these APIs.
The existing country reform readiness trigger checks the complete custody/occupation registry union, including lost host markers and valid empty historical entries.
Country-wide effect sequencing, programme/research consumers, terminal adapter contracts, interface projection, Records wording and AI/cost evidence remain parent-owned.
The parent must review every new API use, test actual existing row retirement and payment paths, and retain all source/destination scope and actor checks.

## Endpoint wrapper and quarantine examples

The internal endpoint wrapper requires all five script parameters, naming retained measured caller variables.
Its default result is the underlying zero acceptance, and a rejected receipt quarantines the endpoint without undoing a committed physical transaction.
It is called by both owned movement completion adapters after physical/row commit or a complete inverse.

```text
camp_origin_commit_endpoint_observation = {
	open_sequence = retained_endpoint_sequence
	open_population_k = retained_endpoint_open_population_k
	open_state_deaths_people = retained_endpoint_open_shared_people
	after_population_k = measured_endpoint_after_population_k
	after_state_deaths_people = retained_endpoint_open_shared_people
}
```

The example supplies zero shared change for movement and its inverse.
A death owner supplies its measured shared receipt separately after the single actual projection.
For a failed inverse, persist the owner's measured partial debit/credit/bind/inverse receipts and other endpoint in normal state variables first, then call the following in each actual endpoint scope.

```text
camp_origin_quarantine_transaction = yes
```

This preserves the verified opening, establishes the separate raw checkpoint and never changes row identity or claims a death/release.
There is no default recovery or clear path.

`camp_origin_occupation_host_ready_for_reform` belongs inside the existing country owner's bounded occupation registry loop.
PREV supplies the exact registry owner, and its temporary override is consumed by inspection without writing any state authority pointer.

```text
all_of_scopes = {
	array = camp_occ_states
	camp_origin_occupation_host_ready_for_reform = yes
}
```

Missing/malformed positive row proof rejects, while a structurally valid empty entry with no sticky ambiguity cannot publish a survivor release and therefore does not require an unrelated fresh territorial interval.

## Validation and remaining work

The companion `origin_observer_helper_source_tests.py` executes these parsed production helper bodies using the existing foundation source harness with mocked engine primitives.
Its archived result covers 24 scenarios, including mixed A/B 10k hosts, mixed families, growth-masked shared loss, headroom-only mismatch, missing/estimated opening records, unique-row acknowledgment, exact own death/residual, inverse replay, failed-inverse source quarantine, counter regression and malformed or oversized registries.
The unique-row caller retirement in that suite is explicitly mocked because this worker does not own or edit its existing production implementation.
The module's no-physical/no-row/no-Deaths boundary is checked alongside those scenarios.

Reference/MCP evidence is the preceding architecture's `occupation\origin_ambiguity_mcp_2026-10-03\` directory and the implementation handoff's local section citations.
Direct server initialization previously confirmed 3.6.0 with SDK 1.30.0 and reference reads succeeded.
Map/helper source lookups and corrected decision/GUI inspections timed out, while event inspection returned partial helper/lifecycle coverage.
No `hoi4.script_validate` route was exposed.
Joined owned-production scenarios additionally verify actual sole-row retirement/repeat, mixed execution rejection, real transfer/destination death, complete and failed inverse, union reform and terminal capture behavior.
There is no matching successful post-integration MCP comparison, live engine proof, click proof or save persistence evidence under the recorded route timeouts.
The parent owns the source matrix against actual callers, balance/eligibility audits, presentation, full restoration-provider verification and final acceptance.
Loss masked by both growth and an absent shared Deaths receipt remains undetectable.
No attribution fallback is implemented.
