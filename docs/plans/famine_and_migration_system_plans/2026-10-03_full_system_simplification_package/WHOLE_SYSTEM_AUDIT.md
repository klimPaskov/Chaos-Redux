# Whole-system source audit

Disposition: `unresolved` audit findings and redesign recommendations.
The system's implementation goal remains incomplete in the existing completion report.
This audit does not certify completion or authorize a patch.

## What already deserves preservation

Current famine simulation composes production, transport, extraction, need, environment, vulnerability, governance, and relief into a state condition, with reserves, exposure, recovery hysteresis, blockade proof, and population-scaled mortality.
Current migration simulation retains living cohorts, historical origins, present hosts, exact routes, reception load/capacity, persecution, custody, visit history, and durable outcomes.
The neutral transaction measures physical debit and credit, separates route deaths, reverses failed accounting, and quarantines a failed inverse.
These are valuable safeguards and causal depth; simplifying the public loop must not flatten them into a generic population penalty.

Two categories already expose three canonical values each and use phase/role filters.
The old source-density audit reports at most six primary actions per valid state context.
That is useful structural evidence, but does not prove six rows across a country with many state-targeted copies, readable native costs, understandable priorities, or a low number of interventions over time.
The package must measure those separately.

## Findings that change the redesign

| ID | Finding and current evidence | Player implication | Disposition / required evidence |
| --- | --- | --- | --- |
| A01 | `common/scripted_effects/migration_capacity_effects.txt:88,105` requires shelter/medical proof strictly greater than `migration_capacity.one`. Normal producers submit one in `common/decisions/migration_decisions.txt:1349–1362,1425–1426`; the current Gods of Africa adapter explicitly works around this by adding one twice. | A paid reception action can fail to create its advertised service; more shelter buttons cannot solve a rejected owner contract. | High-priority source contract defect. Reconcile producer/consumer semantics first, then exercise zero, one, stale, and valid proof cases. Do not spread the private workaround. |
| A02 | `famine_core_constants.txt` clamps each harm component to 100, uses positive weights totaling 7.15, normalizes by 7.15, and places catastrophic entry at 100. The evaluator reclamps blockade additions and subtracts nonnegative relief. | Catastrophic famine normally requires every harm component at its ceiling with zero relief for the candidate duration. A blockade or severe policy famine cannot reach it through its defining pressures alone. | Confirmed algebraic reachability bottleneck, not proof of observed campaign frequency. Sweep the reachable domain and redesign the severe threshold/trigger explicitly. |
| A03 | `famine_repair_relief_route` pays at activation and its resolution clears `civilian_transfer_route_damaged` and marks relief access. It does not repair the native railway. `civilian_transfer_refresh_route_damage_projection` recreates the marker from `damaged_building_level@rail_way`. | A repair promise can briefly override a projection while the real transport bottleneck remains. It invites confusing mission success or relapse. | Confirmed source disconnect. Repair success must follow a physical repair/control receipt, not flag clearing. Native outcome unverified. |
| A04 | `famine_emergency_imports` explicitly requires `famine_relief_route_mode.land` yet charges/debits ten convoys with PP and fuel. Most action prices are fixed file constants regardless of population or distance. | Payment fails to communicate what logistical capacity the action actually uses, and minor/major countries pay identical equipment packets. | Confirmed route/payment mismatch. Give land, sea, and air contracts distinct quotes and transport commitments. |
| A05 | Ten famine and eighteen migration weighted actions exist, plus two famine and four migration missions. Ordinary action durations range from 10/14 through 45 days, with reenable bands from 45 through 120 days. | Strategic action is fragmented into resource packets, waits, and follow-up buttons. Low simultaneous density does not guarantee a short or satisfying loop. | Design diagnosis, not a measured user-experience result. Record interventions per 60-day crisis and retain actions only when they change a strategic outcome. |
| A06 | `famine_release_reserves` resolves after 21 days. Reserve stock already contributes relief in the evaluator; explicit release consumes stock into another bounded relief contribution. | The urgent action can feel slower than the crisis, and its marginal benefit is unclear when stock already provides relief. | Audit marginal benefit, release saturation, and time-to-first-help. Replace the repeat click with a bounded rationing/stock-release policy that has an immediate meaningful result. |
| A07 | `humanitarian_corridor_offer_pending` hides primary rows country-wide in both decision files. Famine role selectors also suppress a role when another response target exists elsewhere. | One pending migration negotiation or a valid route in one state can prevent unrelated famine intervention and force a misleading single national priority. | Confirmed source coupling in presentation. Scope suppression to the exact action subject; reserve capacity where genuinely shared. Preserve a readable priority list. |
| A08 | Local integration requires country-wide resolution and no active migration flag. Its effect integrates the cohort and releases reception load in `complete_effect`, while the 45-day timer is separate. | A safe host may be unable to settle one ready cohort because another origin crisis persists, and a long integration timer can imply work that is already finalized. | Confirmed timing/gating mismatch. Resolve by exact hosted cohort readiness; persist progress and commit terminal accounting at the declared end. Recheck post-result ordering. |
| A09 | Vulnerable and worker evacuation lanes share the same basic five-percent request and organized-evacuation role in their ordinary branches. The worker lane adds requirements/costs, but the distinction needs a documented durable consumer. | A moral/industrial choice can collapse into two similar buttons with different payment. | Partly confirmed structural similarity. Trace both branches, priority metadata, mortality, labor, and achievement consumers before declaring them equivalent. Merge only if no meaningful distinction exists; proposed future priority terms define that distinction. |
| A10 | Many `available` blocks carry route checks while resource checks reside in `custom_cost_trigger`; proof values and fixed prices are duplicated across display/debit sources. Five delayed movement lanes have zero-debit refunds; other delayed relief, distribution, and settlement paths require a fresh receipt/payment audit. | A visible quote may not fully explain affordability, failed work, cancellation, or where committed resources went. | Source risk, not a claim that every action overdraws. Test exact affordability, stale resolution, partial delivery, cancellation, and actor loss for every action. |
| A11 | The destination selector favors safe internal movement and fail-closed food projections. Candidate services require explicit registration and both shelter/medical evidence; absent food evidence is never implicitly safe. | Honest safety can leave the system with no usable destination until reception setup works. Adding destinations or weakening safety would conceal the foundational issue. | Preserve safety. Prove a bounded domestic reception bootstrap and a valid scarcity route without manufacturing stocks or safe facts. |
| A12 | Eight achievements and durable totals observe exact receipts; old docs and handoffs retain combined identifiers, event language, dead callers, and old counts behind clarification banners. | Contradictory documentation can make implementation expand retired layers or tune toward impossible outcomes. | Consolidate accepted current facts, reject stale instructions explicitly, and preserve provenance. Achievement reachability must survive merged action IDs. |

The score ceiling proof for A02 is `sum(harm weights × 100) / 7.15 = 100`.
Any harm below its ceiling or positive relief reduces that value.
The nominal score cap of 200 does not enlarge the reachable domain of this particular formula.
This conclusion is source algebra; fixed-point rounding and actual reachable input combinations remain engine/model evidence questions.

## Strategic diagnosis

The best tension is already present: deliver food where people live, or move people to a place that can sustain them, while the military needs the same transport.
The interface should foreground that choice.
At present the player can instead encounter reserve release, imports, route repair, convoy, airlift, invitation, evacuation, safer-state requisition, concealment, and extraction as separate transactions with similar PP/equipment/fuel structure.
Migration adds preparation, departure policy, two evacuation priorities, negotiation, border policy, services, distribution, transit, and four terminal outcomes.
Some are distinct policies, some are modes of one operation, and some are routine upkeep that should continue under an already chosen policy.

The recommendation is not to remove aftermath or regional identity.
Make logistics and durable outcomes deeper while requiring fewer clicks: choose a response, fund a finite term, resolve one physical obstacle, then choose where the remaining people belong.
Political consequence should follow sustained actions and responsibility rather than award another small stability packet for each successful timer.

## Ledger, integration, and performance audit

Keep exact physical movement below the redesign layer.
One accepted operation slice must resolve one origin debit, one route-death slice, one measured survivor credit, one state/country reception delta, one cohort/history update, and one terminal receipt.
A policy toggle, report, integration milestone, or administrative progress variable must not add population.
Operation completion must not expose terminal status before reception accounting can finish; inject failure between each stage.
Multiple co-located cohorts must either be selected by exact identity or processed as bounded separate transactions, never aggregated into an ambiguous state row.

Audit replay after reload, repeat target selection, A→B→A cycling, annexation, actor/controller change, partial inverse, simultaneous famine/migration obligations, safe food proof invalidation, service replacement by an external owner, and deadline expiry after a terminal receipt.
For automation, aggregate UI summaries without merging ledger identities.
Keep no-result queues inert and avoid per-day recompilation of every country's options.

Current scheduler work is host-only over registered famine anchors/candidates/states, migration states/reception candidates/countries, and relief donors.
Retirement is mechanic-owned; famine recovery must not delete migration obligations.
The redesign must add jobs only to these bounded owners and preserve independent retirement.
Every report refresh should follow a material transition or an operation receipt, not create an event/pacing pulse.

## Existing unresolved obligations

The older completion report explicitly leaves exact-owner integration, probability certification, and dynamic mapmode execution open.
Generic occupation-law changes, strategic bombing, war/peace, and cluster/scenario metadata often lack a complete state/actor/amount/generation/replay receipt.
Some connected hazard calls also lack the full proof envelope.
Events 118, 120, and 131 were absent in the old recovery audit; reconstructing them is a separate event-design task, not famine/migration cleanup.
The old definition-only API census must be refreshed against current external owners before treating it as current absence.
Current source includes a Gods of Africa reception service adapter and ongoing external-owner work, so historical call counts are not final truth.

Missing integrations are not optional polish, but cannot be closed by fabricating people, using total state population as proof of affected people, or reusing a direct death receipt as a displacement receipt.
For every old accepted requirement, record `implemented`, `accepted and queued`, `blocked`, `rejected`, or `superseded` with actual basis.
Do not turn this plan into an implementation closure claim while any accepted requirement remains unresolved.

## What additional size would weaken

Do not add an administrative simulation, worldwide food market, additional standing meters, per-cause ministries/categories, generic incident events, a new shared full window, or a new famine focus/country/formable layer.
The existing fifteen profiles should produce distinct combinations of choices and constraints through the same small action grammar.
Additional historical flavor is worthwhile only when it changes routes, concessions, priority, recovery, or durable outcomes.
New artwork should solve a communication gap demonstrated in native presentation, not accompany every policy term.

## Audit coverage limit

Named specs and supporting matrices were consulted as design/history; current source excerpts and owner documentation establish the findings above.
The package does not claim exhaustive symbolic execution of every helper or inspection of every asset pixel.
The current MCP non-returning routes leave focus-independent map geography, native category layout, event-adapter tracing, and numeric AI conclusions unresolved.
Use the complete future audit assignment in `AUDIT_PROMPT.md` to close those evidence gaps at the then-current revision.
