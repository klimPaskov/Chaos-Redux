# Normal destination bootstrap audit

> **Current-status disposition (2026-10-06): superseded by** [takeover_status_2026-10-06.md](../takeover_status_2026-10-06.md) for current famine and migration status.
> This dated document remains historical evidence, with its original acceptance basis, source snapshot, audit outcome, and validation limits scoped to the work described below.
> This reconciliation grants no new design acceptance and upgrades no historical evidence to current or native validation.

Date: 2026-10-03.
Disposition: food-observation recommendation accepted and implemented in source through `normal_food_observation_implementation_20261003.md`.
The source snapshot and causal reachability proof below describe the pre-implementation baseline.
Ordinary dormant foreign-host first-service/request activation remains unresolved.
Mode: read-only source audit and recommendation.
Only this handoff was added.
No gameplay, trigger, weighted pool, decision, CXT grant, Event 012 adapter, GUI, asset, or population source was edited.

## Conclusion

An ordinary previously untracked healthy state has no generic current migration-to-food observation path.
Normal destination selection and reception-capacity maintenance cannot establish its first food-safety receipt.
The ordinary paid reception action is circular because it requires that receipt before it can register the state's first services.
A second, separate gap prevents a dormant foreign host from establishing its first reception services even if food observation is repaired.

The absence of stored famine fields does not prove that the design lacks normal starting conditions.
The current famine model explicitly defines neutral zero loss-pressure defaults and computes known current hazard contributions.
Those are legitimate model starting conditions.
They are not measured calorie production, warehouse stocks, spare housing, or medical beds.
A bounded famine-owned observation can use that model without inventing a stockpile or treating infrastructure as proof of a route.

Calling the full famine evaluator from migration is not a safe bootstrap.
It changes reserve stock, pressure aging, stage timers, mortality and presentation, then immediately invalidates stable recovered food facts through retirement.
A separate assessment path is needed.

## Exact current causal reachability

| Boundary | Current source evidence | Result for a normal untracked state |
| --- | --- | --- |
| Food publisher | `famine_adapter_effects.txt:20-56` requires state validity and existing stage, pressure, transport, governance and production components. Rejection calls its invalidator. | No receipt. It does not initialize or observe the state. |
| Migration consumer | `migration_adapter_effects.txt:17-30` calls only that publisher and validates the versioned receipt. | Republishing cannot create first facts. |
| Reception candidate registration | `migration_capacity_effects.txt:10-37` registers an explicit state, marks its owner active/dirty, and writes candidate revision. | No famine observation, services, or food facts. |
| Shelter/medical service setters | `migration_capacity_effects.txt:82-115` store positive owner-proven service amounts and register the state. | No famine observation or food facts. The parent's canonical positive-proof correction does not resolve this gap. |
| Capacity recomputation | `migration_capacity_effects.txt:132-200` iterates only explicitly registered candidates and calls the food consumer before candidate validation. | Untracked candidate contributes no safe capacity. |
| Capacity candidate predicate | `migration_core_triggers.txt:334-346` requires food receipt, safe stage, candidate flag, positive population, shelter proof/capacity and medical proof/capacity. | Food and both service contracts are independently necessary. |
| Country capacity predicate | `migration_core_triggers.txt:349-363` requires current non-dirty positive capacity and at least one proven safe candidate. | Registering a country or setting policy is insufficient. |
| Normal adjacent prepass | `migration_destination_selection_effects.txt:316-336` republishes food for the origin and neighboring states. | It observes no new food model context and installs no services. |
| Internal/foreign destination gate | `migration_destination_selection_triggers.txt:191-295` requires food and native/hazard safety, then owner-country reception availability in every normal route branch. | Both internal and foreign destinations fail without an established food receipt and country capacity. |
| Ordinary open reception | `migration_decisions.txt:1242-1369` requires active migration country/phase and proven stable target food before its paid shelter/medical installation. | Cannot establish first food proof. A healthy active-origin country can only select an already tracked target. |
| Current CXT migration fixture | `migration_cxt_test_effects.txt:11-21` submits an aggregate capacity request and calls refresh. | No candidate or service is supplied. |
| Aggregate refresh | `migration_core_effects.txt:1153-1163` recalculates from registered service candidates, then resets the request. | Aggregate requested amount is not a capacity grant and cannot bootstrap the fixture. |

The candidate destination itself need not carry the reception-candidate flag if its owner already has valid capacity derived from another explicit service state.
That does not bypass the destination's own food receipt or route/hazard predicates.

### Closed bootstrap cycles

The food cycle is:

```text
untracked healthy target
  -> no famine food fields
  -> publisher invalidates
  -> open_reception target gate fails
  -> no paid services/candidate
  -> no safe capacity
  -> no ordinary destination
```

Even a valid external service owner that registers the exact state reaches the shorter cycle:

```text
explicit positive shelter/medical services
  -> capacity recomputation republishes missing food
  -> candidate rejected
  -> country capacity invalid
```

No amount of repeat publication or dirty-country recalculation breaks either cycle.

## Existing exceptions and why they do not constitute generic reachability

Food pressure owners can call `famine_apply_pressure_request`, which initializes and registers the exact impacted state at `famine_core_effects.txt:500-520`.
Explicit surface requests initialize/register at `:860-878`.
Historical profile resolution initializes at `:1214-1215`, and an accepted profile initializes/registers at `:1437-1657`.
Exact wartime island registration initializes and registers the affected country's true island states at `:2639-2658`.
Nuclear/reception-demand callbacks may register affected famine states at `:2668-2688` and `:2914-2923`.

These are real bounded cause, anchor, or wartime observation paths.
They do not seed every ordinary healthy internal/foreign destination.
An explicitly tracked but currently stable state may temporarily satisfy publication without ever reaching a visible famine stage.
Therefore the precise conclusion is absence of a generic ordinary destination/reception bootstrap, not a claim that only catastrophic famine states can ever be eligible.

A manual console call to an initializer or direct field assignment is not a reachable ordinary gameplay path.

The famine CXT fixture submits context only for its capital, at `famine_cxt_test_effects.txt:18-29`.
It does not create services for another destination, and it is not normal campaign bootstrap.

The dirty Event 012 `migration_install_gods_of_africa_reception_service` adapter was inspected read-only at `migration_adapter_effects.txt:376-416`.
It consumes/proves food at the capital before installing service.
It therefore inherits the food observation gap.
Its owner-specific service facts remain valid prospective inputs once food observation exists.
Its source and documentation were not edited.

## Stable retirement is a further loss of food reachability

The full evaluator publishes at `famine_core_effects.txt:2044` and then calls recovered-state retirement at `:2049`.
`famine_state_can_retire` at `famine_core_triggers.txt:128-142` permits a stable state with no food pressure, reception demand, or blockade candidate to retire.
`famine_retire_recovered_state` at `famine_core_effects.txt:1824-1857` calls cleanup.
`famine_cleanup_state_registration` at `:2811-2845` clears components and invalidates migration food safety.
`famine_unregister_active_state` at `:478-494` also clears food pressure and stage.

Thus an initialized healthy state's first full evaluation can publish and invalidate its receipt in the same effect chain.
A formerly affected state that recovers is not a durable solution for normal reception.
Migration membership does not intentionally keep famine simulation alive, preserving the separate-owner contract.
A normal observation solution must recreate current food assessment at bounded consumer boundaries after retirement rather than preventing unrelated famine retirement.

## Legitimate model baseline and available observation inputs

`famine_initialize_state` at `famine_core_effects.txt:795-856` fills missing input/profile/component/pressure fields with zero and the stage with stable.
It preserves existing fields.
Its food-reserve amount, initial amount and initialization proof default to zero.
There is no positive reserve grant in this initializer.

These numbers describe the pressure model.
Production zero means no modeled production-loss pressure, rather than proof of positive physical crop output.
Transport zero means no modeled transport-loss pressure, rather than proof of a navigable route.
The specification Part 2 explicitly avoids simulating every farm, calorie, or market transaction.

`famine_collect_surface_context` at `:1054-1209` derives bounded current contributions from occupation data, global air bands, Air Winter/fallout fields, contamination modifiers, active camps, site type, camp pressure, forced-labor quotas and explicit war/outbreak/disaster proof.
The existing model deliberately starts external contributions at zero and adds only supported observations.
The accepted source receipts and profile/input fields remain necessary wherever the collector has no authoritative native observation.

The component aggregation at `:1869-1930` and weighted score at `:1959-1980` combine input, accepted profile and collected context using existing weights.
No alternate food formula is required to assess a normal baseline.

The native population, infrastructure, railway damage, recent bombing and current control/occupation surfaces are available.
They do not measure food stocks, household capacity or medical bed counts.
Existing destination route/hazard triggers remain responsible for rail, bombing, infrastructure, adjacent geometry, owner/controller and policy checks.
Observation must not promote one of those values into route, people-impact, shelter or medical proof.

### Why full evaluation is unsafe as a query

At `:1864-1867`, full evaluation initializes, activates historical contexts, collects current inputs and decays pressure.
At `:1933`, it calls `famine_update_reserve`.
The reserve updater at `:2142-2251` can replenish positive stock from its live-population/logistics model, even when initial stock was zero.
The evaluator also advances stage candidate/recovery timers, can commit stages and survivor-flight requests, applies mortality at `:2041`, refreshes modifiers/achievements and retires stable states.

Those are normal simulation effects.
A destination query must not trigger them merely because a state is considered for evacuation.

## Minimal bounded food-observation recommendation

This is a proposal, not accepted gameplay implementation.

Add one famine-owned public observation seam for an explicit valid state.
Reuse a small extraction of the existing component aggregation and score calculation so the observer and normal evaluator cannot drift.
Keep reserve mutation, pressure decay, stage transition/hysteresis, mortality, survivor-flight generation, report/category reveal and retirement exclusively in the ordinary famine evaluator.

The observer should:

1. Validate the exact state and its current owner/controller and positive native population.
Treat invalid state/scope or a missing mandatory owner receipt as invalid.

2. Preserve all existing inputs, accepted profile fields, pressure, stock, exposure, stage and timers.
Use the existing missing-value neutral baseline only for an uninitialized normal pressure-model field.
Do not reset a crisis, profile, or negative observation.

3. Call the existing current-context collector and shared component/score helpers.
Read existing proven stock and relief inputs when relevant, but do not initialize, replenish, release, import or transfer stock.

4. For a newly observed normal state with no material food pressure, establish a famine-owned assessment snapshot and publish it through the existing versioned projection contract.
Stable assessment creates no famine modifier, phase, report or player category.
It is model observation, not a food delivery or physical-supply guarantee.

5. If fresh observation discovers material pressure or cannot establish a safe first assessment, invalidate its destination receipt and enqueue only that exact state through the existing famine registry.
Let the normal evaluator own stage timing and mortality.
Do not copy the initializer's stable stage into a proven receipt before the observed context has been evaluated.
The parent should choose and document the conservative first-observation guard using existing stage thresholds, without bypassing hysteresis or reducing known pressure.
For already tracked crises, preserve the established simulation-stage contract and fail closed on stale/missing assessment.

6. Refresh only explicitly registered reception states, registered migration origin states and exact adjacent states under an active destination prepass.
No new global scan or permanent famine registration of all normal states is necessary.

7. On invalid scope/control change or famine retirement, clear observation proof or mark the exact observation dirty.
A later bounded observation may recreate it from current context.
Keep projection invalidation separate from migration services, cohorts and reception ledgers.

### Proposed helper map

| Helper | Scope | Inputs | Outputs | Side effects/call sites |
| --- | --- | --- | --- | --- |
| `famine_observe_migration_candidate_food_context` | Exact state | Current native state, existing famine input/profile/pressure and accepted owner context | Explicit temporary valid/invalid result plus a current famine-owned assessment receipt | Initializes only missing neutral model facts after real observation. Invalidates unsafe/missing receipt. May enqueue that exact materially affected state. Called before existing migration food publication at bounded candidates. |
| `famine_rebuild_food_components` | State | Existing inputs/profile/pressure, collector outputs, already proven relief/stock effects | Existing bounded components | Extract from current evaluator and share with observation. No reserve or population mutation. |
| `famine_calculate_food_score` | State/temporary model frame | Existing component values and existing constants | Existing raw score/requested stage calculation | Extract current formula. No stage commit, hysteresis, mortality, registry or presentation mutation. |

Final identifiers and durable observation fields should be selected by the parent implementation owner and documented with the actual defaults.
A small proof/schema/revision/date or dirty marker may be appropriate if the existing projection cannot distinguish evaluated observation from mere initializer defaults.
Do not invent an actor, route, receipt generation or physical stock to satisfy the contract.
No global event target is required.
Any temporary input/result must be reset on both acceptance and rejection.

Existing script constants remain the tuning source.
No new balance value is required for zero-pressure baseline, component bounds, stage thresholds, or weights.
A shared observation freshness category is warranted only if an actual dated cache is introduced.
An observation receipt must not imply that absent external owners supplied their missing exact people or food facts.

### Migration call-site placement

The existing food consumer is the natural bounded connection seam for registered capacity states and adjacent destination prepasses.
An additional exact candidate-discovery assessment must happen before `migration_open_reception` target availability is evaluated.
Its current trigger must remain read-only.
Do not initialize persistent model fields inside a per-frame `available` or target trigger.

For an already problem-active country, a bounded queued assessment request can target explicit selected/adjacent safe receiver states before the ordinary paid action runs.
Registration in an observation/candidate set should not grant shelter/medical services or capacity.
Any once-per-country owned-state candidate discovery needs an explicit parent-reviewed scope/performance contract.
Do not hide a repeated whole-world sweep behind the observer.

Changing candidate availability through these call sites alters a weighted target surface even if no numeric weight is edited.
The parent must preserve a real pre-edit source baseline and run `chaosx_ai_probability_auditor` inspect/baseline/compare with the same named internal/foreign scenarios before applying those call-site or target changes.
No weighted or target patch was made by this audit.

## Separate unresolved ordinary-host service design

Food observation repairs only food reachability.
Current ordinary service allocation requires `migration_open_reception`, whose `visible` block requires `migration_decision_active` and `migration_displacement_country_active`.
A dormant safe foreign country has neither from normal candidate consideration.
The category's offer-only exception does not solve this, because open reception also suppresses itself while an offer is pending.

A first humanitarian offer cannot reliably reveal the needed service action either.
`humanitarian_corridor_front_destination_is_safe` at `humanitarian_corridor_triggers.txt:89-119` demands positive current reception capacity before preparation.
The offer is submitted only after preparation/route validity at `:206-254` and `humanitarian_corridor_effects.txt:268-300`.
Therefore ordinary first capacity is a prerequisite to the offer that might reveal a migration category.

The absent facts are:

- an authoritative ordinary destination-state shelter service amount and proof;
- an authoritative ordinary destination-state medical service amount and proof;
- a real bounded host activation or pending-request fact that permits the paid preparation action before the first admitted cohort;
- a non-circular request/response lifecycle for a host that has no prior migration problem.

Current native population, infrastructure and civilian factories can contribute to quality or scale.
They are not existing shelter/medical service-owner receipts.
The current paid action's 0.40 shelter and 0.10 medical population shares are accepted outputs of that action, not permission to grant the same service freely during a query.

Possible remedies require parent design acceptance.
One is an exact prospective migration reception request that represents a real origin cohort and selected adjacent host, reveals only its preparation/response actions, allows the host to pay for services, and permits route acceptance only after capacity and all original route proofs pass.
Another is a documented legitimate native baseline service model with explicit receipts and exclusions, if the parent accepts such a model.
This audit does not choose either, fabricate capacity, widen categories for mere observation, or lower route safety requirements.

## Meaningful validation and acceptance cases

The causal source census found no initializer, collector, reserve-safe observation or service install in the ordinary food consumer, adjacent destination prepass, candidate registrar or aggregate CXT capacity request.
The registry scheduler processes only registered states/countries and does not discover healthy normal receivers.
The previous migration setter proof defect was corrected by the parent, but positive canonical proof still cannot create food facts or missing services.

Before implementing the food seam, the parent should validate:

- untracked healthy internal state under a real origin problem becomes observable without receiving stock, mortality, a modifier or a famine category;
- the same state with native/owned contamination, camp, occupation, outbreak or disaster context is not coerced healthy;
- initialized active famine retains exact inputs, stage, exposure, stock and timers across repeat destination queries;
- recovered/retired state can be observed afresh without keeping famine simulation registered;
- repeated same-date observation cannot replenish reserves or repeat a death/flight pulse;
- explicit positive services plus observed safe food produce a valid capacity revision, while missing either service remains invalid;
- a dormant foreign state remains unable to receive until an accepted service/request design supplies its real receipts;
- control/owner changes invalidate exact cached assessment and host authority;
- CXT aggregate request alone remains a negative control, rather than a free service grant;
- source-only candidate checks and weighted scenario results are reported separately from live engine behavior.

No game was launched and no logs were read.
No source Boolean matrix is claimed as native decision availability or engine execution.

## MCP and references

The current general `hoi4.reference_context` request for state food-context observation returned:

```text
tool call error: tool call failed for hoi4_agent_tools/hoi4.reference_context
Caused by: timed out awaiting tools/call after 600s
```

The current exact `hoi4.source_lookup` request for `famine_evaluate_food_security` returned the same 600-second timeout for that route.
No citation IDs or artifacts were delivered, so no `reference_read` result or helper closure is claimed.
The preceding mapmode audit's narrow map inspection also returned a 600-second timeout, and no direct model-execution evidence is substituted.

Local references read directly:

| Source | Span | SHA-256 |
| --- | --- | --- |
| Installed `documentation/dynamic_variables_documentation.md` | 1118-1143 and 1168-1179 | 538525747F0C285062C9CE8DB14B4E07C3CF6BAC1013115FA4F57291CB4EBDDA |
| Installed `common/decisions/_documentation.md` | 1-45, scopes/evaluation frequency/target narrowing | 5E7E686B5582F32C38D898D805E17171E88F3BFEEE4A030DEB1884F9726DE019 |
| Installed `common/decisions/AST.txt` | 113-126, exact target-array/FROM precedent | AAD50DA745F5A93C5F7470E06ED990A49A5416C81810849C8A2312600E81F4F2 |
| Offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` | 436-450 and 1670-1694 | 62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4 |
| Offline `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md` | Targeted-decision state/root/target sections around 570-605 | 7713B9BCEE5F3818D63AAFBD45D18E812A9173A7C59AB238384B57DB60DB6162 |

Installed variable-set/clear and trigger/scope rules read in the immediately preceding mapmode audit remain recorded in `current_mapmode_projection_audit_20261003.md`.
The current Part 2 food-security specification, relevant Part 3 internal/foreign destination and reception-capacity sections, owner docs and source were consulted.
No Paradox wiki web access was used.

## Audited source identities

| Source | SHA-256 |
| --- | --- |
| `famine_core_effects.txt` | 9E57983FF15737321F4F31B2471F3BEA4B438432EF8F521E4DA0C87906F42B1F |
| `famine_adapter_effects.txt` | 05E5855A19BE1B4999BD52F61E8D2208C288005E0A2B7F0F26B5D698E9C460F1 |
| `migration_capacity_effects.txt` | 62CE76598B5EE2FCD7517613370C52A8899B23347DF289872C44B31DB1AE607B |
| `migration_destination_selection_effects.txt` | F20084BF1FE1B12A885710B0A3E081E251F3AEFD3505ACA4C65925421CAEB9FF |
| `migration_core_triggers.txt` | 00031F2DBCC7549E0D1FD2EBD40613809EB97332D9CD4B8EC68F8266BC7864FE |
| `migration_decisions.txt` | 279487DC7F2FCEF921F7294FD207BA8C1C33F871C652280EBB31D2D1FD2A3E8B |
| `migration_cxt_test_effects.txt` | 98C87728125B3ED6E267ECB58039255DC3391364D6D1AA8164BBD0863688ED23 |

Files above live under their matching `common/scripted_effects`, `common/scripted_triggers`, or `common/decisions` directories.
Hashes identify the current audited source, including concurrent parent-owned corrections.

## Parent decision required

Accept or reject the bounded famine-owned observation seam and its first-material-observation guard before implementation.
Choose how an ordinary dormant host establishes the first explicit shelter/medical service and a real preparation request.
Keep the existing food publisher fail-closed and preserve all original route, transfer, policy and receipt gates.
The food-only seam must not be presented as completion of foreign-host bootstrap.

Skills used: chaos-redux-events, chaos-redux-state-ledgers, chaos-redux-subagents and chaos-redux-decisions-missions.
No skill was changed.
No commit was made.
