# Event 033 Humanitarian source retirement contract, 2026-10-07

Disposition: `unresolved` owner-interface proposal for parent review.
The bounded source audit and this handoff are delivered, while supported source retirement and independent consequence proof remain unimplemented.
Acceptance basis for amounts and source identity is `docs\plans\033_acid_rain_plans\agent_decisions_2026-10-04.md`, D5 and D14, under its recorded 2026-10-04 user grant of design authority.
The source-specific retirement requirement remains unresolved in `docs\specs\033_acid_rain_specs\specs\033_acid_rain_consequence_repair_acceptance_2026_10_03.md:22-24,79-82`.
The parent owns acceptance of this interface, owner coordination, implementation, and integration.

## Result and next safe implementation step

The current public addition adapter exists, but it is not a reversible source-33 interface.
`famine_adapt_acid_rain_state` validates positive envelope fields, submits the generic natural-disaster request, and renews the same disaster expiry used by Event 013.
The famine core stores aggregate shock plus a last-source label, without an accepted Event033 receipt, kind identity, source residual, or source-specific context expiry.
There is no established public endpoint that can remove only Acid Rain's registered contribution from that representation.
Neither generic famine retirement nor subtraction of an estimated Acid Rain amount is an acceptable substitute.

The next safe implementation step is a famine-owner patch to the existing adapter and its core accounting seams: persist source-owned accepted receipts, keep a private Event033 shock contribution and context, and publish the existing aggregate as a derived value.
First review the proof schema and full writer inventory below, then implement and test the owner contract before wiring Event033 recovery calls.
Event033 must continue to call only the public owner adapter and a proposed public retirement adapter.
No new public meter, migration cohort, population movement, generic removal API, central MCP router, or wrapper skill is proposed.

## Parent watermark repair already implemented

During this audit the parent repaired `acid_rain_register_humanitarian_pressure` and `acid_rain_register_aftermath_humanitarian_pressure`.
Current source is `common\scripted_effects\033_acid_rain_aftermath_effects.txt:614-679`, SHA-256 `2805a9af30ac54e332fb0ec09136c62c232f1b57083df9bee2cedebd6fcae09c`.
The registration helper resets and publishes caller-preinitialized `acid_rain_humanitarian_result`, and the tier watermark commits only when the famine result is one.
Do not implement that repair again.
I independently ran `node .tools/validation/test_033_humanitarian_receipts.js`, which passed its eight acceptance, rejection/retry, duplicate, higher-tier rejection/retry, older-tier, rounded-zero, and stale-frozen-state cases against that exact source hash.
Its famine acceptance and native arithmetic/scopes are explicit mocks.
It provides no famine accounting, persistent receipt, proof, retirement, migration, or save/reload evidence.

The pre-parent source hash was `c7d2be98f646c934b92d023f7fa474ff1420fa261eb0a88fb66aa718aedec0b5` with the wrapper at lines 612-645 and the prematurely committed watermark at line 658.
That finding is superseded by the verified parent repair.

## Producer and consumer findings

| Surface | Exact source evidence | Implication |
| --- | --- | --- |
| Mortality producer | `common\scripted_effects\033_acid_rain_effects.txt:3070-3102,3115-3149` | One population-first helper supplies the actual positive loss, the state records its before/after amounts, and a positive-receipt count becomes the humanitarian revision. The Deaths target is CONTROLLER. The rolling positive-receipt arrays are appended after the humanitarian call and do not store that revision, so they cannot reconstruct every rejected request later. |
| Aftermath producer | `common\scripted_effects\033_acid_rain_aftermath_effects.txt:225-275,653-679` | Tier assessment invokes registration when the tier rises. Current parent repair prevents rejection from committing the watermark. Merely leaving the watermark uncommitted does not establish a scheduled retry after an unchanged assessment. |
| Evacuation producer | `common\scripted_effects\033_acid_rain_preparedness_effects.txt:1200-1218,1270-1308` | A completed, valid state operation supplies the operation key and 2% estimate only at population at least 500k. Completion flags are set before the adapter call, and the operation is later released, so failed humanitarian registration requires a separately frozen request to retry. There is no destination or survivor credit here. |
| Event033 bridge | `common\scripted_effects\033_acid_rain_aftermath_effects.txt:614-649` | Source 33, Acid Rain cause, current generation and revision are supplied. Kind is set by producers but is not forwarded or validated by famine. Request id is the date. Actor is OWNER while readiness is read on CONTROLLER. These are distinct roles requiring explicit recorded identities. |
| Generic envelope validator | `common\scripted_effects\famine_adapter_effects.txt:496-541` | Exact state and actor binding plus positivity checks are supported. Positivity does not verify source 33, Acid Rain cause, current frozen generation, kind, receipt uniqueness, amount provenance, or physical food/transport evidence. |
| Addition endpoint | `common\scripted_effects\famine_adapter_effects.txt:794-819` | Calls `famine_request_disaster_pressure`, then `famine_open_disaster_food_context` on success, and clears the one-shot envelope. It does not persist a consumed composite. |
| Core acceptance | `common\scripted_triggers\famine_core_triggers.txt:50-58`, `common\scripted_effects\famine_core_effects.txt:569-594,650` | Converts people to a bounded normalized shock, adds/clamps aggregate pressure, writes `natural_disaster` as last source and registers famine. No Event033 identity reaches persistent core accounting. |
| Shared context | `common\scripted_effects\famine_adapter_effects.txt:712-718,760-819`, `common\scripted_effects\famine_core_effects.txt:1305-1314,3199` | Event013 and Event033 renew the same expiry. Clearing it for Acid Rain would also remove Event013's context. |
| Decay and aggregate consumers | `common\scripted_effects\famine_core_effects.txt:600-627,2039,2196`, `common\scripted_triggers\famine_core_triggers.txt:140-174` | A single normalized shock decays at most once per date. Aggregate pressure contributes to need and blocks generic retirement. These semantics must remain intact. |
| Generic cleanup | `common\scripted_effects\famine_core_effects.txt:547-563,1966` | Unregistering famine clears aggregate pressure and stage. Event033 cannot use it to retire its source. |
| Event033 recovery/cleanup | `common\scripted_effects\033_acid_rain_aftermath_effects.txt:547-604`, `common\scripted_effects\033_acid_rain_preparedness_effects.txt:1545-1585`, `common\scripted_effects\033_acid_rain_effects.txt:78-129,891-903` | Paid recovery settles Event033 burden, evacuation closure removes Event033 protection, and state clearing erases source identity. No source-specific famine retirement is called at these edges. |
| Additional aggregate writers | `common\decisions\famine_decisions.txt:1856,1968` | Famine concealment and extraction add pressure directly. A projection conversion that overlooks these writers would lose other pressure. Their owner must adapt these two write seams or provide a verified equivalent accounting path. This audit does not review their gates, costs or AI. |

Existing helper guidance was inspected in `common\scripted_effects\chaosx_dynamic_effects.txt:633-665` and its paired markdown at `263-301`, plus `famine_core_effects.md` and `famine_adapter_effects.md`.
The shared exact-loss helper already owns the physical debit and Deaths registration, so neither new adapter may call it again.
The famine adapter documentation explicitly says the generic validator does not persist a consumed composite and leaves replay prevention to the source owner.

## Real proof and frozen transaction envelope

Keep the accepted D14 amounts unchanged: actual positive observed mortality, a newly reached tier 2 at 0.5% of the relevant population snapshot, tier 3 at 1%, and a completed evacuation at 2% for a state with at least 500k people.
The people estimate is a pressure-sizing input, not a claim that those people became refugees or moved.
Water readiness, transport readiness, general Preparedness and `proof_floor = 1` do not independently prove a food loss, disrupted food route, or actual environmental consequence.
The existing famine validator accepting those positive values establishes only syntactic envelope acceptance.

Recommended Event033-specific proof schema:

- Exact state pointer and ID, source 33, Acid Rain cause enum, immutable generation, kind, revision, producer receipt identity and production date.
- Captured OWNER and CONTROLLER identities with their distinct roles, and the actual producer actor when that differs.
- A valid, exact frozen-state membership/generation check at registration and a generation-local lifecycle state that permits that transaction.
- Mortality: actual positive helper result, actual loss amount, matching before/after observation, pulse identity and no population-contract fault.
- Aftermath: committed assessed tier and newly reached tier identity, matching consequence generation/window evidence, exact population snapshot used for sizing, and the already recorded impact/burden evidence.
- Evacuation: completed valid paid operation, exact state and generation, operation key and payer, completion receipt/date, population snapshot and the 500k boundary. Forecast or merely started operations fail this branch.
- Separate, documented food, environment, transport and policy evidence with an explicit validity field for each. A valid factual zero must be distinguishable from absent evidence. Reusing readiness as positive consequence proof is unsupported.

The last proof item needs famine-owner acceptance of which Event033 measurements establish these dimensions for each kind.
The existing source does not demonstrate physical crop loss or a food-route measurement for every mortality pulse or evacuation.
The owner must either verify supported measurements/owner receipts already available or implement the narrow missing proof producer within the accepted feature.
Do not replace this missing seam with a generic positive token, nominal railway level, a forecast, wartime status, or a fabricated affected population.
Do not silently disable an accepted D14 kind because its proof is missing.
That is an explicit incomplete integration until the owner contract is resolved.

Freeze the entire producer envelope in normal state-owned fields or aligned pending rows before the producer releases/overwrites its native receipt.
Registration rejection must retain that immutable pending transaction for a bounded retry at an existing Event033 worker/changed-state edge, without repeating mortality or completing another operation.
A retry uses the original population denominator, amount, kind, generation, revision and actor snapshots, with explicit current authority/lifecycle revalidation.
Recalculating the request from a later population or current tier is not an exact retry.
Old-generation pending registrations may not be relabeled with the new global generation.
Unaccepted terminal requests remain explicit failures, rather than fabricated success or retrospective reconstructed pressure.

## Proposed helper map

These names are proposals, not existing verified endpoints.
Retain the existing addition name as the public compatibility boundary.
Invoke scripted effects with `= yes` and one-shot input variables, rather than unsupported named argument blocks.

| Helper | Scope and inputs | Outputs/defaults | Side effects and direct call sites |
| --- | --- | --- | --- |
| `famine_adapt_acid_rain_state` | STATE. Frozen exact-kind producer envelope above, including population denominator and real consequence proof. | Caller-initialized `famine_adapter_result = 0`, accepted receipt ID, admitted normalized delta, duplicate indicator and reason. Public result stays one for an accepted new receipt or verified identical already-accepted receipt. | Famine owner validates and commits one source receipt, changes only its private source contribution/context, republishes total and uses its existing exact-state registration. Called through `acid_rain_register_humanitarian_pressure`. |
| `famine_retire_acid_rain_state` | STATE. Exact source/cause/generation, selected accepted receipt IDs or an exact recorded selection boundary, expected ledger revision, a unique retirement operation and supported recovery/shutdown proof. | Caller-initialized result zero, retired receipt count, retired residual and reason. A proven duplicate retirement succeeds with zero additional change. | Sets only the selected source residuals/context obligations terminal and republishes total. Never unregisters aggregate famine or clears another source. Called from Event033 paid recovery, evacuation closure when its pressure obligation is proven ended, full local recovery reconciliation, and administrative generation cleanup before identity erasure. |
| `famine_validate_acid_rain_receipt` | STATE. Current producer request or exact immutable pending row. | Caller-initialized valid zero and reason. | Read/validation only. Enforces kind-specific producer proof, source/cause/state/generation identity, exact duplicate payload and authority contract. Internal addition adapter call. |
| `famine_initialize_source_shock_partition` | STATE. Existing valid aggregate, current decay date and schema marker. | Initialization success or explicit corruption/migration failure. | Once only, copies existing aggregate into an unattributed legacy bucket and creates empty Event033 buckets. No pressure added or removed. Used before all owner shock write/decay seams. |
| `famine_publish_source_shock_total` | STATE. Valid legacy bucket and Event033 residual buckets. | Existing `famine_food_pressure` projection and validity result. | Recomputes total from authoritative buckets, bounded by the existing cap. Does not infer a residual by subtracting Event033 from old aggregate. Internal registration, decay and retirement seams. |
| `famine_decay_source_shocks` | STATE. Existing date, relief/stage facts and all valid residual buckets. | Existing at-most-once decay date and updated residuals/total. | Applies one shared existing decay budget across the owned buckets, then publishes the total. Replaces only the accounting body of `famine_decay_pressure`, under its current guards and cadence. |

Any result consumed after a helper return must be declared in its caller, including forwarded nested outputs.
Both adapters reset outputs on entry and consume their one-shot envelopes on success and rejection without erasing published results.
Keep a fresh mutation receipt separate from historical accepted/retired status.
Reset it before consumption and set it only when this invocation changes the exact owned row, so a duplicate or rejected request cannot trigger another irreversible effect or roll back an earlier tombstone.
Use a separate result/reason for absent source, saturated acceptance, duplicate acceptance, stale generation and corrupt/ambiguous receipt.
A valid registration at an already full cap may admit zero normalized shock while recording acceptance and its genuine context, matching the current core's acceptance behavior.
A zero people request fails registration without committing an accepted receipt or tier watermark.
Retirement is a separate operation that can legitimately remove a source whose residual is already zero.

## Persistent identity and lifecycle

Canonical registration key is `(state_id, source=33, cause=acid_rain, generation, kind, revision)`.
Store its fields separately, without numerically packing them or using the date as unique identity.
Actor identity is immutable payload/authority evidence, not a way to create another copy of the same state transaction after controller change.
The date is evidence, so several kinds and several mortality receipts can be accepted on the same day.

The smallest durable design is a state-owned accepted-key set plus state/generation/kind shock and context buckets.
Accepted-key payload includes requested people, population denominator, producer receipt, actor snapshots, admitted delta, acceptance status and retirement status.
Bucket fields include exact generation and kind, current residual, latest applicable context expiry and lifecycle status.
If aligned arrays are used, all key/payload arrays append and retire at the same index, and every bucket/receipt lookup must resolve exactly one row.
Two rows for one key, misaligned arrays, fractional identity fields or inconsistent projection are corruption, so refuse the transaction before changes.
Do not cap away or evict active-generation consumed keys to satisfy a loop limit.
Use bounded pages or keyed storage if the receipt set exceeds the engine's 1000-iteration effect limit.
For pending recovery, pop only the selected bounded batch and append unresolved rows behind the unvisited suffix, retaining every unacknowledged receipt.
Clear a pending receipt only after its exact owner acknowledgment, and test more than 1000 rows across repeated passes and unresolved-row rotation.

An identical accepted key returns its original accepted status without another shock or context renewal, even after another key B intervened.
Changed amount, denominator, kind payload, cause or actor under the same key is rejected.
Retired receipt tombstones remain consumed through the generation's callback lifetime.
Local recovery retires the selected accepted contributions and their context obligations, while keeping duplicate protection.
It does not close the whole generation, because a fresh later mortality pulse or evacuation in that generation may still be legitimate.
The accepted once-per-generation aftermath watermark remains monotonic and is not reset by retirement.
Administrative generation closure can reject every later registration for that generation, retaining a closed-generation tombstone before compacting receipts.
Never rely on the rolling mortality history arrays to provide this lifetime.

Existing Event033 frozen flags and matching registry/consequence generation supply useful identity evidence, but an arbitrary positive generation argument cannot establish it.
Normal state variables persist across controller changes and save/reload.
Preserve the original actor snapshots and source residual on controller change, validate fresh registration against the supported current authority seam, and retire by exact stored source ownership.
Cleanup must still be able to close its own proven rows if population has reached zero or the original actor no longer exists.
Using the positive-population `humanitarian_state_is_valid` predicate as the sole retirement gate would strand those rows.
Use documented actual STATE identity plus the owned persistent receipt for cleanup, without COUNTRY-only existence predicates in STATE scope or `scope_exists` as variable-pointer validation.
An old-generation retirement must select that stored generation explicitly and cannot touch a newer generation's buckets.

## Cap, decay and disaster-context preservation

Preserve the existing normalization: `delta = clamp(100 * requested_people / frozen_population_people / 0.20, 0, 100)`.
At each accepted write, admit only available aggregate headroom into its owned bucket.
For example, other pressure 98 and a requested Acid Rain delta 5 admit exactly 2, leaving total 100.
Retiring that receipt recomputes total as 98, preserving other pressure.
Do not retain the rejected excess as latent shock that resurfaces when another source recovers.
Store people and normalized values separately, and use a conservative fixed-point model for intermediate arithmetic and rounding before implementation acceptance.

Compute the current existing daily decay once: base 0.25, relief-access bonus 0.75, and settled-stable bonus 0.50 where the existing stage/score guard applies.
Do not apply that entire decay independently to every source bucket.
Recommended partition is proportional allocation of the one aggregate decay budget to current residuals, with deterministic bounded rounding and the final residual correction assigned within a bucket that can cover it.
At residuals 60 and 40 with decay 1.5, the result is 59.1 and 39.4, total 98.5.
The allocation rule is a proposed owner choice because the old aggregate supplies no attribution rule.
It preserves total decay/cap semantics, while per-source attribution and fixed-point rounding still require owner review and exact tests.
Retirement zeros the proven source residual and recomputes the projection, rather than subtracting a requested people estimate or historical delta from the shared total.
Other contributions remain subject to their ordinary decay, not recovery of Acid Rain.

Give Event033 a private generation/kind disaster context expiry, retaining the old `famine_disaster_context_until_date` for Event013/legacy contributions.
The collector at `famine_core_effects.txt:1305-1314` applies its existing disaster production/transport/need amounts once when either the legacy context or a live source-33 context is valid.
Overlapping contexts must not double those component amounts.
Retirement updates only source-33 context obligations and recomputes their private maximum expiry, while Event013's existing expiry is preserved.
The existing last-source field remains a display/attribution hint, not evidence authorizing cleanup.
Do not change unrelated stage, reserve, demand, modifier, migration or environmental-provider fields through these adapters.

## Constants and tuning table

| Existing tuning | Value | Proposed treatment |
| --- | --- | --- |
| `acid_rain_humanitarian.source_id`, kind IDs | 33, 1/2/3 | Preserve, forward and enforce exact identity. |
| `aftermath_tier_two_share`, `aftermath_tier_three_share` | 0.005, 0.010 | Preserve full per-new-tier amounts. Tier 2 then tier 3 remains two accepted requests, rather than replacing 1% with an invented 0.5% delta. |
| `evacuation_share`, `evacuation_large_population_k` | 0.020, 500 | Preserve, snapshot and test the inclusive population boundary. |
| `famine_food_shock.population_share_for_maximum` | 0.20 | Preserve normalization. |
| `famine_food_component.maximum` | 100 | Preserve aggregate cap and admitted-headroom semantics. |
| Existing shock decay | 0.25 + applicable 0.75/0.50 | Preserve a single date-scoped budget. |
| `famine_surface_context.disaster_context_days` and component values | 60 days, production 30, transport 15, need 20 | Preserve duration conversion and single-application collector behavior. |
| `acid_rain_humanitarian.proof_floor` | 1 | Do not treat it as sufficient consequence proof in the resolved owner API. |

Only receipt schema/status/reason enumerations need proposed new constants, in an owner-owned `common\script_constants\` category with first-entry schema.
No balance target, AI weight, MTTH helper, new meter or duration change is proposed.
Probability auditing remains with the separately assigned AI auditor, including any owner patch that later changes a weighted surface.

## Recovery, event targets and migration

Use `acid_rain_record_paid_recovery_consequence` after its exact accepted operation proof, `acid_rain_close_state_evacuation` before it clears completion identity, and `acid_rain_reconcile_state_consequences` for exact full local settlement.
Recommended conservative recovery eligibility is proven settlement of the associated Event033 obligation, not modifier expiry, controller change, warning expiry, date passage alone, or disappearance of the current tier flag.
Full local source retirement requires no remaining acute/forecast obligation, resolved retained burden and ended evacuation obligation, with an exact accepted recovery/closure receipt.
The exact timing for partial tier-3-to-tier-2 retirement is not established by D5/D14, so do not invent fractional relief or automatic downgrade subtraction.
The endpoint can select exact kind/receipt obligations when the parent accepts their supported resolution proof.

Generation shutdown and runtime state clearing must call retirement before clearing `acid_rain_registry_generation`, operation keys, actor pointers and source receipts.
Freeze the retirement selection and expected owner ledger revision before any nested helper.
A concurrent fresh accepted receipt invalidates an outdated blanket selection rather than being silently retired.
On refusal, preserve the owner cleanup request and report it incomplete, while independently safe weather/UI cleanup remains parent-owned.
No success-only cleanup receipt may commit after a failed owner response.

Retain regular `famine_adapter_actor` for the immediate chain, with explicit actor validity and identity checks.
It is not a durable identity or a transaction frame, and nested helpers can replace it.
Persist original state/actor pointers and receipt identity in normal owner fields before asynchronous work or nested dispatch.
No additional global event target is needed, so no global-target cleanup API is proposed.

The migration boundary remains closed for Event033's pressure estimates.
No origin debit, destination credit, survivor amount, receiving-country load or route-death slice is proven by this adapter.
Neither registration nor retirement creates, reduces or retires a refugee cohort.

## Migration limits and implementation order

1. The famine owner verifies the proposed real-proof schema and current writer inventory, including the two direct decision writes, using its surface guidance and MCP inspection.
2. Implement the owner partition/schema initializer, accepted-key bookkeeping, source context, aggregate projection, admitted-headroom writes and single-budget decay in the existing famine files with paired helper documentation.
3. Preserve existing mixed aggregate and disaster expiry as unattributed legacy state at initialization, without guessing an Event033 share or clearing Event013 history.
4. Change the existing Acid Rain adapter to the exact source-owned path and append its narrow retirement endpoint. Verify source, cause, kind, frozen generation and duplicate payload before committing.
5. Event033 freezes new producer/pending envelopes and forwards kind plus real proof through its existing registration helper. Keep the parent's success-only watermark repair. Add bounded retry only at existing worker/changed-state seams.
6. Wire exact recovery/evacuation/shutdown retirement calls before Event033 identity erasure. Update `famine_adapter_effects.md`, `famine_core_effects.md` and the Event033 integration documentation in the owner's eventual implementation tranche.
7. Run the source contract cases below, required MCP source/event evidence and owner review before claiming the dependency resolved.

Historical source contributions cannot be safely unmixed from aggregate pressure and a last-source label after clamping, shared decay and shared expiry renewal.
The initialization above preserves them, but only new exact receipts acquire reversible attribution.
The rolling Event033 history is insufficient for historical reconstruction, and multiplying historical deaths by today's population denominator is invalid.
Existing accepted tier watermarks must not be reset to replay already-mixed old shock.
Old-generation rows cannot be manufactured from a global generation number.
Mark pre-contract registration/retirement coverage as unresolved legacy provenance, rather than reporting balanced historical source retirement.
If exact historical records are unavailable, this limitation remains a completion blocker for claims requiring that reconstruction.
The proposed legacy partition is explicit preservation of unattributed state, not an approved fallback for the full Event033 requirement.

## Validation and evidence limits

Completed: actual producer/consumer and owner writer source trace, exact existing public adapter lookup, reference context/search calls, local primary-document section reads, current-source parent regression rerun, and independent decimal design calculations.
The five design calculations checked cap admission 98+5 -> 100 with source admission 2, retirement leaving other pressure 98, shared 60/40 decay -> 59.1/39.4, D14 shares -> normalized 2.5/5/10, and kind-separated A/B/A keys -> two identities.
These are contract arithmetic/key examples, not execution of a missing famine API or HOI4.

Required owner cases remain unexecuted: exact registration/proof rejection, same-key changed payload, A/B/A, duplicate ledger keys, same-day kinds, saturated acceptance, zero request versus zero residual retirement, frozen pending retry, partial and full recovery, duplicate retirement, generation replacement, stale callback, save/reload, distinct OWNER/CONTROLLER, dead actor or zero population cleanup, shared context overlap, other pressure preservation and fixed-point decay/cap rounding.
For source-specific absence, retirement must distinguish a proven generation with no accepted receipt from unknown/missing legacy provenance.
No game launch, desktop control, log search, save inspection or additional role spawn occurred.
No complete-event gate or AI baseline audit is duplicated here.

## MCP evidence ledger

Connected metadata exposed `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, `hoi4.source_lookup`, `hoi4.event_inspect`, `hoi4.event_render` and `hoi4.event_compare` schemas.
Regular read-only calls were used, with no helper-expansion/job/native-task assumptions.
No exposed health/version route was found, so the connected process version and task negotiation remain unverified.
Repository configuration uses `npx.cmd --yes --prefer-online hoi4-agent-tools@latest`, repository cwd and 600-second tool timeout.
Configured `HOI4_AGENT_CONFIG` is `C:\Users\klimp\AppData\Roaming\hoi4-agent-tools\config.json`, with installed game root and offline workspace sources.
There are both global and npx-cached running executables, so a process inventory does not identify this connection's version.

`hoi4.reference_context` first rejected a question longer than 160 characters with MCP `-32602`.
The corrected narrower question succeeded for `general`, workspace `mod_chaos_redux_ea3b2d67c2c0`.
Its limit omitted Triggers and Modifiers and reported no missing files, so it is not claimed as complete detailed reference coverage.
Targeted searches/reads and local sections cover the rules actually used in this proposal.

`hoi4.source_lookup(famine_adapt_acid_rain_state)` returned `OK`, index revision `7abc85ca35fa2c47f7ac6ee728d65cd28ecf7262a727df724d8f25a216350aa2`, one unshadowed definition at `mod:common/scripted_effects/famine_adapter_effects.txt:794-819`, complete definition coverage and no truncation.
The query included references, but returned zero references with `referencesComplete = false` and `unresolvedReferenceCount = 19823`.
That is not proof of no consumers, so the producer callsites above were read directly.
This index result does not certify the parent's later Event033 watermark bytes.
No artifact URI was returned by these successful reference/lookup calls.

The symbolic `famine_apply_pressure_request` lookup failed terminally with `timed out awaiting tools/call after 600s`.
One narrower retry at `common/scripted_effects/famine_core_effects.txt:569` succeeded with source-location revision `d58c2988ac8056c8c436cc8c1217478f64bc7f90d3419b1bea02c9809f124b87`.
It identifies the unshadowed owner `famine_apply_pressure_request:569-594` and root key occurrence zero/index 66, with structure available and no skipped source, but returns `definitionCount = 0` and no body text beyond the declaration line.
The core body was therefore read locally, not claimed as an MCP-expanded consumer proof.
Separate symbolic lookups of the Event033 bridge, decay helper, disaster-context helper, generic receipt validator and vanilla `store_core_states_on_game_start` also returned that exact 600-second terminal timeout.
No repeated successful query or guessed helper expansion was used to hide those gaps.

The `Script Constants` and `add_to_array` dual-source searches each returned the same terminal 600-second timeout.
One narrower game-document-only retry for each succeeded, locating script concepts at lines 216-222 and effects at lines 2278-2292 under the revisions cited below.
Revision-bound reads succeeded for installed `save_event_target_as:6496-6504`, wiki Scopes `260-271`, wiki Effects event-target row `357`, wiki variable types `435-443`, installed `check_variable:2110-2134`, installed Script Constants `216-222` and installed `add_to_array:2278-2292`.
These are detailed rule reads, rather than context titles alone.
An additional observation of the installed event-target read returned the terminal 600-second timeout, while the earlier revision-bound read succeeded and supplied the section text.
That inconsistent route observation does not invalidate the retrieved section or establish general service health.
The narrower constant search id is `c859ab9d6a857bfc830f89b36b004514b78ee454e001a80238a9d1f7b355ccd0` and array search id is `b11098707fca8123566864381393f908217da93ca48203f5731a100d0143c95d`.

The bounded event trace used selector `{kind: event, eventId: chaosx.nr33.1}`, depth 1, nodes 8, edges 12 and helpers off.
It returned `EVENT_INSPECTED_PARTIAL`, revision `8f4a82aa5d847df22b40a90e209f8bd0e27f3d6ebe79d13e4fb3dbaf45dc33b0`, graph hash `d494c41cf68a6eb896650d0f95ea38572ce93b8c83273a07a92d60c74eb41ceb`, `analysisMode = focused`, zero helpers and one blocking diagnostic, with `validation.passed = false`.
Its 403-path inventory was limited to 64 inline paths, and the diagnostic details were not supplied inline.
Authoritative artifact reference: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/50a4917eec212859671bab141b6054123510b55e2b5ad2e573309fab1b70e14b/c2d295da135f1ad3f25b0781f840a24b03a1144f5b2bd6db160db09201b8fb55/event-trace-8f4a82aa5d84.json`, declared size 1088174 bytes.
A bounded resource read failed with MCP `-32603: Artifact provenance manifest is unavailable`, and the artifact was not found at the configured local storage candidate.
The complete artifact, source inventory and blocking diagnostic could not be verified.
Focused event analysis cannot establish helper lifecycle coverage in any case.
No render or comparison is claimed for this read-only API proposal, because no event source overlay or lifecycle implementation was supplied.
MCP helper/consumer coverage and event lifecycle validation remain explicitly incomplete.

## Primary reference citations

All references are local, with no web Paradox wiki access.
`paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md:263-305,425-442,1069-1089` documents regular/global targets, variable pointer persistence, temporary output lifetime and aligned array semantics, SHA-256 `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
`paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md:245-270` distinguishes THIS/ROOT/PREV/OWNER/CONTROLLER and variable/target scopes, revision `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49`.
`paradox_wiki\Triggers - Hearts of Iron 4 Wiki.md:570-590` documents scoped variable checks, while `paradox_wiki\Effects - Hearts of Iron 4 Wiki.md:4617-4645` documents meta token injection.
The wiki Effects event-target row at line 357 was located by MCP search, revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`.

Installed authority is `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\`.
`documentation\effects_documentation.md:2278-2291,4833-4850,6016-6029,6496-6512` documents array operations, meta effects and targets, SHA-256 `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
`documentation\triggers_documentation.md:2110-2134,7588-7596` documents variable comparison and STATE-only population in thousands, SHA-256 `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`.
`documentation\script_concept_documentation.md:216-244` documents fixed-point constant access and load injection, SHA-256 `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7`.
`common\script_constants\documentation.md:1-31` documents the mandatory first-entry schema, SHA-256 `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c`.
Vanilla precedent `common\scripted_effects\00_scripted_effects.txt:4345-4353`, `store_core_states_on_game_start`, persists exact scoped states in an array through PREV.
`common\defines\00_defines.lua:25` sets `MAX_EFFECT_ITERATION = 1000`, so a long receipt set needs bounded iteration or keyed storage.
These references establish available scripting primitives, not execution of the proposed contract or unsupported physical-food proof.

## Source hashes and delivery boundary

| Source | SHA-256 |
| --- | --- |
| `common\scripted_effects\famine_adapter_effects.txt` | `1172f9f69ed5c727443781801ed3ba80ee461089c49ef07a637b66455df539c5` |
| `common\scripted_effects\famine_core_effects.txt` | `d105449dcb8baf379e93c707c28b621646b7e9fd389a1adecd678a6154aa976e` |
| `common\scripted_effects\033_acid_rain_effects.txt` | `f0cb9c24b684b7cccd66e90adc7128bf68b2db29b859b3e302c7d8a96f50766d` |
| `common\scripted_effects\033_acid_rain_preparedness_effects.txt` | `1f6d6534ab595972e3ffa6d8a509e25c9bd04db87043a0db02549f824f422fa6` |
| `common\scripted_triggers\famine_core_triggers.txt` | `ff91666b07487a9ef02e878ea1cff5c3cdb5b5abca34485a938248d3b7bd7e31` |
| `common\scripted_triggers\033_acid_rain_triggers.txt` | `f2ec10e0cc2c3894dd2caf03d877cc62a8a4637e8bd60437d48314afb12ebaa7` |
| `common\script_constants\famine_core_constants.txt` | `c6cf6b2827d93e47f9fe94b3abc8381cd6f9ae3f9725521d5fbcfb6955b77a82` |
| `common\script_constants\033_acid_rain_constants.txt` | `58deff691f6e43f7de79cf60a5757dfdcb9e003b77d7104bd064ec7a5a83137c` |

Only this new handoff file is changed by this subagent.
Gameplay files, helper documentation, callsites, constants, cleanup logic, assets and other docs are unchanged by this subagent.
No commit is made, as requested.
Skills used: `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-state-ledgers`.
No skill is created or updated.
No simplification or fallback has been implemented.
Supported source retirement, real consequence proof and historical attribution remain explicit incomplete work for the parent and famine owner.
