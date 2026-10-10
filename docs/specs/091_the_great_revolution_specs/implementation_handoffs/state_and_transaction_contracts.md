# Event 091 state and transaction contracts

## Contract vocabulary

The names below are proposed planning identifiers.
Use owner-private Event 091 files for orchestration and lifecycle.
The implementation owner must reconcile names with existing definitions before creating them.
Shared classifiers, Deaths, cost APIs, date conversion, world threats, unit providers, and Event Logs retain their existing owners.

A generation identifies one proposal, committed opening, political request, operation, or recovery episode.
A receipt identifies one exact accepted mutation.
An array index is neither of those identities.
All asynchronous work carries the appropriate identity in normal saved storage and fails closed when it no longer matches.
Boolean state uses flags rather than numeric variables that only hold zero or one.
Numeric enums and counts use documented integer values.

## Event-level finite states

| Phase | Entry proof | Permitted work | Exit and preservation |
| --- | --- | --- | --- |
| Historically locked | No accepted whisper unlock | Event 001 progression only | Historic whisper unlock persists once earned |
| Eligible but not selected | Historic unlock, active spread, above-five-percent ordinary mean, Chaos level 5, no terminal conflict | Normal major-pool competition with stored weight | Selection proposes a frozen opening |
| Proposal reserved | Immutable inputs and random draws saved, no fired history | Nomination, union, viable-origin preflight, tag and actor proof | Either reject without firing or commit the same proposal |
| Rejected proposal retained | No viable origin or other exact feasibility blocker | Retain weight and proposal draws, omit candidate for that selection cycle | Relevant world-state change authorizes review, UI refresh and reload do not reroll |
| Opening applying | Successful preflight, proposal consumed once, snapshot sealed | Activate origin, setup, state-rights transactions, forces, wars, alignment, history, presentation | Close deferred callback refresh and enter active war |
| Active global war | Opening committed, Lenin actor continuity valid | Bounded participant operations, Influence, Momentum, commands, later local expansion | Terminal commit, defeat pending, or continuing war |
| Defeat pending | Body or origin compromised, anchor and territorial proof under review | Finite survival and counteraction missions, no duplicate opening | Recover through accepted finite contract or complete defeat |
| Red World | Shared strict terminal gate consumed | Terminal war, final choices, accelerated existing integration | Final absorption or a separately mapped terminal resistance outcome |
| Defeated and aftermath | Body secured and all anchors destroyed or severed, continuity failed | Reconstruction and explicit body-capture aftermath | Durable history remains and normal Major Event 091 cannot refire |

Proposal reservation must precede the generic fired-event recorder because that recorder can run before the event's immediate block.
An invalid proposal cannot consume a fire-once record, issue the opening Chaos premium, or play the signature announcement.
This requires a shared dispatcher pre-fire seam reviewed by the parent.
The proposal input signature includes exact country existence and eligible pool membership, frozen communist fractions, valid Event 001 lineage and levels, and the ownership, control, population, industry and actor-validity inputs that determine origin feasibility.
A changed source value in that relevant signature permits a new proposal review.
The passage of a day or month, menu activity, callbacks, and reload alone do not.
Revalidate a current leader for political commitment without rerolling unchanged territorial inputs.
Store actual accepted selections and fractional outcomes in addition to reservation identity, since an identity alone does not prove native random replay.

## Saved field ownership

| Record | Owning scope | Required fields | Cleanup rule |
| --- | --- | --- | --- |
| Proposal header | Global Event 091 ledger | Monotonic proposal identity, input signature, phase, reserved random identity, rejection reason | Retain rejected draw identity until authorized change, replace only through explicit proposal lifecycle |
| Committed episode | Global Event 091 ledger | Opening identity, encoded firing date, immutable firing month, actor pointer, origin pointer, phase, Momentum | Never clear durable firing history or month |
| Country opening row | Participant country or aligned global rows | Country pointer, frozen ideology and leader proof, popularity fraction, pool membership, target, inherited count, nomination count, overlap count, alignment request identity | Retain minimal outcome history, retire working arrays after all dispositions settle |
| Physical state row | State plus sparse global identity index | Exact state pointer, frozen owner/controller, nominations, Event 001 lineage, inherited level, final rights, unit-source contribution, transaction phase | Preserve origin and historical claimant provenance, clear active projections on retirement |
| Event 001 rebel lineage | Event 001 owner | Exact original host, original episode, originating states and levels, rebel identity, observed asset receipts | Preserve through transfer, absorption, refusal, and aftermath |
| Influence participant | Joined country | Episode pointer, affiliation status, Influence, critical due day, subject receipt, annex due day, active operation identities, transformed leader identity, last accepted concession day, end day of each concession family's latest agreement | Independence closes future pressure and annex work, durable history survives |
| Autonomous partner | Protected country | Permanent crisis-specific Trotsky protection receipt and partnership identity | Never remove through ordinary Influence cleanup or leader replacement |
| Regional command and anchor | Event 091 sparse slot registry and anchor state | Fixed continental slot, site pointer, custodian, generation, activation, loss, destruction or severance receipts | Permanent destruction closes slot, no relabelled replacement command |
| Muster | Event 091 owner plus donor receipt | Operation identity, donor and cohort, actual reserved manpower, actual equipment vector, selected templates, actual delivery, source kind | Consume on actual delivery, refund only its own undelivered reservation |
| Civilian harm | Shared population and Deaths owners | Exact state, observed actual loss, responsible actor, reason, one-shot receipt | Event 091 retains incident reference and never reapplies physical loss |
| Rule denominator | Global Event 091 ledger with state weights | Unique state pointers, positive opening population weights, fixed summed denominator | Preserve throughout war, terminal transition and defeat history |

Normal saved variables hold durable state pointers and country pointers where documented.
Regular event targets carry exact short-lived scopes inside one synchronous chain.
Global event targets are reserved for genuinely persistent pointers with explicit stale-target cleanup.
Do not key state or country identities by undocumented arithmetic on scope values.

## Nomination and physical-claim invariants

| Invariant | Required proof |
| --- | --- |
| One pool member per country and state | Deduplicated membership before counting `N_i` |
| Exact proportional arithmetic | `T_i` uses one whole part and one fractional Bernoulli draw from frozen current popularity |
| No fixed territorial minimum | Zero is valid, including one-state countries |
| Preservation precedes addition | All valid inherited members belong to the country's nomination before any additional selection |
| Inheritance excess is preserved | Nomination count equals `max(T_i, G_i)` with no extra popularity selection when `G_i` exceeds target |
| No underfilled nomination | Additional selection continues without replacement until its exact residual is filled or preflight rejects the proposal |
| One physical claim | One state receipt and one physical union membership regardless of number of nominations |
| Overlap is explicit | `affected_i = size(pool_i intersect physical_union)` and `overlap_excess_i = affected_i - nomination_count_i` |
| No duplicate force grant | The physical state contributes once to a muster source, independent of its claimant count |
| No origin minimum | Choose a viable origin from the inherited and nominated union, otherwise reject before firing |
| No reroll fishing | Rejected proposal draws remain saved across callback, refresh, reopened UI, and reload |

If some inherited state is associated with several countries, record every proven association but preserve one physical state and one actual force package.
The original Event 001 host remains lineage rather than a guess based on its present controller.
Special-actor occupied states require a valid cross-owner capture contract before direct mutation, even when an ordinary participant owns the legal title.

### Abstract nomination pseudocode

```text
reserve_proposal(current_world_inputs)
for each frozen ordinary participant:
    pool := unique eligible owned or controlled states plus exact rebel lineage
    raw_target := size(pool) times frozen communist fraction
    target := floor(raw_target) plus one stored fractional draw
    inherited := unique valid Event 001 states in pool
    nominated := inherited
    residual := maximum of zero and target minus size(inherited)
    choose exactly residual additional local states without replacement
    seal country nomination receipt
union := unique states across all sealed nominations and standalone inheritance
origin := highest priority viable origin inside union
if no origin exists:
    reject before firing and retain draw identity
otherwise:
    publish proposal ready
```

The pseudocode describes behavior and does not authorize named-argument scripted effects or unsupported script constructs.
Standalone inheritance means observed rebel territory that must remain represented even when exact historic host linkage is unavailable.
It does not permit a second ordinary popularity roll for the rebel.

## Atomic execution and interrupted work

Capture the whole opening proposal synchronously before mutation.
If native iteration cannot reliably cover the installed state map within that boundary, the snapshot path is blocked until a documented iterator or equivalent complete approach is verified.
A partial snapshot taken across different game days is not equivalent.

Each physical-state transaction separates ownership-right and controller-right completion under one state claim identity.
An ordinary late alignment response can resolve the remaining right without transferring the already completed right again.
Current military capture supersedes stale physical authority.
A late click cannot teleport a state back to a country merely because it appeared in the frozen pool.
Its nomination and history remain immutable while current control determines whether the remaining disposition is valid, contested, or closed by military outcome.

Before nested helper work, freeze actor, state, donor, generation, receipt and outer cursor into private normal storage.
Temporary variables and regular target aliases can be overwritten by nested calls.
At the final mutation gate, read the frozen frame and revalidate exact identity and current authority.
Clear the frame on success and rejection while leaving public result outputs available.

When a processor uses a native numeric loop, its bounded batch must remain below the verified iteration ceiling.
Do not clear a pending queue and reconstruct only the visited prefix.
Pop selected rows before work, append unresolved rows behind the unvisited suffix, and consume each recovery receipt only after acknowledgement.
No periodic unscoped world scan is introduced for repair.

## Helper map

Every helper uses the documented variable or token input convention and `= yes` invocation.
Each caller preinitializes every scalar and array output it consumes after return, including forwarded outputs at every nested boundary.
Helpers reset result outputs at entry, clear one-shot input envelopes on every exit, and preserve published results until the caller consumes them.

| Proposed helper | Scope and inputs | Outputs | Side effects and callers |
| --- | --- | --- | --- |
| `revolution_reserve_opening_proposal` | Dispatcher country, current eligibility, requester context if manual | Proposal identity and ready or rejected status | Saves immutable proposal, no fired history, territory or Chaos, normal and manual pre-fire seams |
| `revolution_snapshot_participant` | Country, exact proposal identity | Pool and frozen country row | Saves current inputs only, reservation orchestrator |
| `revolution_nominate_participant_states` | Country, sealed pool, inherited set, stored actual draws and selected-state history | Target, nomination, exact residual proof | Applies Part 3's numeric positive weights and sequential weighted selection without replacement, resumes the local selected graph, saves selected set, no physical mutation |
| `revolution_union_physical_claims` | Owner ledger, all completed country rows | Unique state registry, overlap proofs, viable-origin status | Creates one state row per union state, no transfer |
| `revolution_commit_state_rights` | State, exact physical claim and political response receipts | Actual owner/control result, contested reason, fresh commit receipt | Applies only valid unconsumed rights, opening and late-response consumers |
| `revolution_accept_alignment` | Country, request, current leader and ideology, frozen episode | Joined, refused, autonomous or invalid result | One faction and war transaction, state-right resolution and aid request |
| `revolution_quote_muster` | Donor country and exact regional source set | Quoted people and equipment vector, affordable and valid proof | Read-only quote for focus, decision and reinforcement callers |
| `revolution_execute_muster` | Exact quoted source and current resource proof | Actual consumption and delivered formation receipts | One payment and delivery owner, no duplicate unit creation |
| `revolution_refresh_momentum` | Global owner with maintained inputs | Exact bounded Momentum and current stage | Publishes sole global public value and phase effects, no repeated milestone grants |
| `revolution_apply_influence_outcome` | Joined country, accepted concrete action receipt | Applied change and current stage | Changes sole country public value once, rejects autonomous and independent participants |
| `revolution_resolve_subject_binding` | Country, full Influence and exact sovereignty request | Native subject or verified equivalent binding receipt | Starts annex deadline only after real result |
| `revolution_declare_independence` | Country, active participation or subject receipt | Closed Influence and annex generation, war receipt | Free decisive exit, no further influence, player and AI path |
| `revolution_review_anchor` | Exact registered slot and site | Active, compromised, destroyed, severed or invalid result | Closes only its own anchor and records finite milestone |
| `revolution_try_terminal_commit` | Country and global owner, exact rule proof and settings | Fresh terminal receipt or rejection | Calls shared terminal owner once, no public row recreation |
| `revolution_resolve_defeat` | Event owner, body and all anchor outcomes | Fresh defeat receipt and aftermath identity | Cancels only active event work, preserves history and unrelated systems |

These helpers remain in Event 091 owner files.
Only neutral behavior with real cross-system callers belongs in the shared dynamic registry.
The shared registry can index an Event 001 to Event 091 gateway without copying its implementation.

## Canonical proposed Momentum formula

Initial tuning uses six bounded components whose maximum contributions sum to one hundred.

`Momentum = 45 × territorial + 15 × military + 15 × political + 10 × commands + 10 × transformation + 5 × objectives`

| Component | Proposed normalized proof | Behavior on loss and anti-farming |
| --- | --- | --- |
| Territorial | Clamp current unique ruled share divided by 0.50 to zero through one | Forty-five points are attainable at fifty percent rule, actual liberation removes current credit |
| Military | Clamp net active strategic-victory weight divided by a tuned goal of twenty to zero through one | Unique capital objective weight five, major regional supply or industrial objective weight one, permanent command losses create weight-five debt, same site or objective identity cannot award repeated capture credit |
| Political | Clamp uniquely credited functioning institutional weight divided by 0.25 to zero through one | Direct councils and contributing partners share the same frozen state lineage, preserve absorbed institutions once, suspend contribution on destruction or actual loss of cooperation, autonomous Trotsky contributes cooperation without adding ruled territory |
| Commands | Active operational regional slots divided by number of inhabited eligible continental slots | Permanently destroyed or severed commands lose credit, same slot cannot recur as another reward |
| Transformation | Clamp unique proven living transformed person-equivalents divided by 100,000 to zero through one | Real civilian conversion, verified transformed formations and finite manifestation receipts contribute once, deaths and cohort retirement remove living credit, captive humans are not automatically converted |
| Objectives | Current earned valid objective weight divided by total accepted finite objective weight | Map and institutional objectives have stable identities, revoke current-condition credit where the objective requires ongoing control |

Freeze political weights from ordinary legal ownership at the successful opening snapshot.
Let `P_total` be the sum of their state population in thousands and `F_total` be the sum of their actual fixed civilian and military factory counts.
Each physical state's legal ownership is counted once, regardless of foreign occupation, and a factory is counted only in its actual state, never again through a country total.
With both denominators positive, its weight is `0.50 × P_state / P_total + 0.50 × F_state / F_total`.
The frozen country weight is the sum of its state weights.
These weights sum to one across the frozen ordinary lineage.
If the factory denominator is zero, use population share alone.
If population is zero but industry is positive, use industry share alone for this political normalization, while the separately required inhabited world-rule denominator still requires positive population.
If both are zero, the opening proposal fails feasibility rather than inventing a positive weight.
The political goal is 0.25 of this frozen total weight.
This is an initial balance proposal, not a forced territorial minimum or a compulsory ally requirement.

One state lineage can receive institutional credit once through a functioning direct council, an integrated institution, or its contributing partner government.
The proposed initial review period is thirty continuous days of valid administration and functioning institutions, followed by a completed real contribution through a prescribed army, equipment, civilian production, reconstruction, or shared campaign-objective recipe.
The recipe must require its actual quoted resources or delivered outcome and publish its completion receipt.
A mere allegiance flag, an empty army, a renamed council, or a promise of aid earns no credit.
An active credited institution must continue functioning and complete a prescribed contribution within each rolling ninety-day review interval.
The action owner selects and quotes the concrete recipe, and this component consumes its proven completion instead of creating another payment system.
Domestic institutions can satisfy these conditions through ordinary human administration and production without civilian transformation or outside government cooperation.
Crediting the same lineage through a partner and a direct council cannot add its weight twice.
Annexation retains functioning supporter institutions through exact lineage, so incorporation does not reduce political Momentum merely because a native country disappears.
An independent breakaway removes its former binding credit unless it completes a new valid voluntary cooperation arrangement.
Protected Trotsky cooperation can contribute political credit while contributing zero ruled territory.

Transformation's initial goal is one hundred thousand unique living person-equivalents.
The First Coming seed and three later finite manifestations at the first earned crossings of forty, sixty and eighty Momentum provide at most forty thousand person-equivalents, credited once per actual living manifestation receipt. A terminal power override cannot mint a skipped manifestation receipt.
The remaining footprint must come from actual tracked people or real transformed formations.
The same person cannot count as both a civilian cohort and a formation, and reconstruction moves or consumes an existing finite cohort rather than minting a second contribution.
Death, permanent destruction, retirement, or proven reversal removes the corresponding current living contribution.
This is an internal accounting proof, not another public species meter.
The numeric goals require future balance scenarios and engine arithmetic validation before implementation acceptance.

The finite objective component uses eight equal-weight slots as initial tuning: a supplied opening connection, the chosen political settlement, a successful cell program, a sustained army-standardization program, a functioning red foundry, a functioning international or domestic congress arrangement, one completed regional-command campaign, and the protected research exchange.
Each slot contributes at most one eighth of this component. Mutually exclusive route variants fill the same slot and cannot expand its denominator or duplicate credit.
A terminal scenario is not an objective slot, and this component never requires all six commands.
Use the relevant focus and mission anchors to prove each slot, retaining current control or functioning requirements where their design depends on them.
Repeated deliveries or repeated captures cannot create new slots.

The collective human-preservation route can earn ninety points without the ten transformation points.
It can reach the eighty-point apotheosis band through territory, military objectives, voluntary cooperation, commands, and earned campaign objectives.
Mass civilian conversion is therefore not a mandatory route to high Momentum.
The sovereignty-preserving route must have objectives and political targets that are attainable without forced annexation.

Calculate stage from the exact internal value before display rounding.
Display the integer floor or a decimal value consistent with the threshold.
Never show eighty when the actual value is 79.9 and the eighty gate fails.
Milestone manifestation and Chaos receipts use attained thresholds once per episode rather than current stage transitions.

## Influence, dates, and native missions

The Influence stages, the 180-day critical mission and its expiry table, the binding gate, the 120-day annex interval and the Red World final-response timing are defined once, in Parts 5, 8 and 9.
This section adds only the technical requirements for those rules.
There is no hidden ninety-five cap, and automatic growth can reach one hundred inside the critical mission while automatic binding stays blocked until its deadline.
Only a separate explicit voluntary-submission receipt permits earlier binding, and an ordinary institutional concession is never that receipt.
Ordinary alignment uses the native thirteen-day response window with refusal as the default and no consent inferred from silence.
Stalin and Trotsky Soviet routes resolve immediately from the current active leader when alignment commits.
The terminal pause and snapshot belong to one terminal request generation and cannot refresh through UI, a leader change, a callback or reload.
The free independence action remains valid throughout every resumed or newly created annex interval, including its completion day, until the exact annex transaction consumes authority.

Use one documented day-count clock for business deadlines and separately store encoded calendar dates for historical display.
Do not add raw days to `global.date`.
Where encoded date arithmetic is required, call `chaosx_convert_days_to_date_offset` and `chaosx_convert_date_offset_to_days` with caller-preinitialized outputs.
Where native mission timeouts are used, synchronize actual mission remaining time against the stored day deadline after activation and every accepted extension or one-time terminal pause and resumption.
Native timeout callbacks and recovery events share the active receipt and consume it once.

## Finite survival timing

Distributed survival activates at sixty Momentum with a proven active anchor network.
When the body and origin are secured by opponents and Momentum remains below forty, begin a ninety-day severance objective.
Each surviving registered anchor must be permanently destroyed or individually proven severed by the end of that objective before full defeat can be declared.
Dropping below forty does not erase an active supernatural command by itself.
Rising to forty or losing custody of the body or origin invalidates continuous low-Momentum proof and resets that interval without granting anything.

One body reconstitution is allowed per campaign from a pre-existing surviving anchor.
It requires 180 days, the exact anchor generation, actual World Revolution or bound-subject command authority, a paid finite living transformed cohort, real equipment, and valid continuing territorial control.
Reserve and consume the cohort once through the muster owner.
No new campaign manifestation seed is created for reconstruction.
Trotsky, autonomous allies, a newly fabricated anchor, a dead site, or a stale country pointer cannot fund it.
Preparation failure refunds only undelivered reserved resources and leaves the one-time reconstruction allowance unconsumed until actual reconstruction, subject to anti-repeat reservation guards.
The enemy receives a counterpart site objective and AI priority, so the 180 days are active conflict.

After reconstruction, the next secured body and severed network resolve final defeat.
When the body remains captured while surviving anchors operate, the crisis stays active without cloning a second living Lenin.
Exact actor and leader presentation during that period requires the country and character owner to verify native continuity.

## Population invariants

| Fact | Native population mutation | Deaths registration | Required accounting |
| --- | --- | --- | --- |
| Living worker transformation | None merely for classification | None | Exact living cohort changes state without creating recruits |
| Real manpower recruited or formation transferred | Only the documented native military transaction | Native military casualties separately | Observe actual reserve debit and unit manpower, no second debit inferred from desired strength |
| Civilian conversion failure | One measured exact state loss | Observed actual civilian loss once | Shared exact-loss helper and reason metadata |
| Civilian movement or evacuation | Shared migration transfer only | Route-death slice once if people die | Origin debit, survivor credit and residual conservation |
| Captured equipment delivery | One actual native stock debit and measured credit | None | Original donor and equipment type retained |
| Supernatural finite manifestation | No invented civilian loss | None | Consume one of the parent's finite person-equivalent milestone receipts |
| Liberation, cure or institutional removal | No population creation merely for an outcome | None | Update living cohort state and real available manpower only through proven native rules |

Use `state_population_k` and documented manpower-in-thousands readers for arithmetic.
Avoid deprecated raw manpower getters and avoid a guessed universal variable maximum.
People, thousands of people, percent fractions, whole equipment, and encoded date units must each have explicit dimensional labels in API docs.
Review intermediate fixed-point operations rather than assuming a later division makes an unsafe product safe.

## Cleanup invariants

Close active operations before clearing their targets.
Cancel obsolete native missions using actual mission state independently of stale private flags.
Preserve actual paid, refund, report, settlement, and achievement receipts until their owner acknowledges the matching terminal outcome.
Do not run normal reward or timeout logic on an authority-loss cancellation.
Remove only Event 091 active projections and foreign-control institutions when their own recovery contract proves removal.
Do not clear another living actor's target during dead-actor cleanup.
Never clear Event 001 history, the world denominator, other threat sources, recorded Deaths, or shared contamination merely because Lenin is defeated.
