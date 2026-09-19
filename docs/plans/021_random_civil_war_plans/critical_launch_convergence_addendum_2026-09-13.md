# Event 021 bounded improvement addendum: Critical launch convergence

## Disposition and authority

Disposition: `implemented`, limited to convergence of the existing Evolution III Critical launch contract; final event acceptance remains unresolved.
Broad mechanic expansion: `rejected` as unnecessary breadth.
Implementation status: owner-applied in the current source. The review-to-Critical handoff no longer dispatches every due country, Critical claims retain their queue row until terminal outcome, `chaosx.nr21.18` dispatches on the claimed recipient, and the queue exit enum/receipts are wired through lifecycle cleanup.
Acceptance basis: the parent applied this bounded follow-up under the user's explicit request to mark the rework complete for testing; the current release record remains `Needs Testing`, and final acceptance is separate and unresolved.
Design basis: source-spec part 6 requires Critical-country launches to use normal target safety, the shared opening systems, bounded capacity, separate repeatable-event accounting, and a recorded queue exit reason.
The existing probability matrix requires GLB-03 Stable countries to receive review without launch.
The implemented follow-up covers removal of unconditional due-review dispatch and the owner-aware Critical queue handoff; it is promoted into the current test-entry implementation with source and MCP evidence below.
Do not treat this bounded implementation evidence as final acceptance or live-game proof.

The earlier improvement-loop pass is disposed in `improvement_loop_disposition_2026-09-06.md` as an implementation-and-testing queue.
Its B05, B07, B08, and B10 evidence obligations remain accepted and queued because current-revision certification and lifecycle evidence are incomplete.
B03 and B04 remain blocked by the shared fixed-target dependency and inherited package evidence.
This addendum narrows the existing queue obligation rather than reopening the earlier expansion or proposing another mechanic layer.
Do not request another Event 021 planner pass until this proposal is implemented, promoted with acceptance, explicitly queued with a reason, or rejected with a reason.

## Review basis and depth verdict

The ten numbered specs, their compiled master, supporting specification documents, and package prompts establish substantial intended depth through archetype-specific openings, multi-front escalation, prevention, settlement, reconstruction, recurrence, and bounded Event 006 reuse.
The compiled master was checked by removing the exact trimmed contents of all ten numbered parts, leaving only its introduction and source separators.
Current implementation review concentrated on entry callbacks, target preparation, queue admission, indexed scheduler loops, opening transaction gates, prevention actions, and current repair handoffs.
This is not a completion audit of every inherited country package or every historical handoff claim.
The September 13 completion and probability continuation handoffs are evidence of remaining work, not certificates for subsequent parent repairs.

The current source already contains repairs that older reports described as missing.
`random_civil_war_critical_queue_country_valid` requires Critical pressure, dequeue uses actual array membership, the scheduler has indexed scan bounds, and secondary opening and scenario planning have additional precommit freeze helpers.
Do not turn those older findings into new expansion requirements.
The September 13 test-release handoff opens playability while retaining `Needs Testing` and separate final acceptance.
Do not restore a closed release gate merely because the September 6 disposition describes its older state.

Reject additional decisions, meters, GUI windows, countries, formables, focus routes, super-events, animation, or models for this pass.
The remaining design problem is a connection between implemented systems, not absence of another system.
This is not a clean closure certificate while accepted evidence obligations and dependencies remain open.

## Source repair record

In the current source, `event021_global_review_current_country` records no due-opening dispatch. It refreshes state and route evidence, may enqueue a Critical country, reviews fronts, and applies settlement or reconstruction; only the bounded Critical queue path can claim an opening.

`event021_launch_critical_country` now sets `random_civil_war_launch_in_progress`, saves `random_civil_war_launch_target`, marks only the selected country as pending, and retains its queue row and wait date while the callback runs. `event021_parent_reserved_critical_launch_valid` is the owner-aware capacity exception used by target preparation and transaction gates. The scheduler invokes `chaosx.nr21.18` on the saved recipient country, and that callback owns dispatch, terminal exit classification, dequeue, and lock release.

The source repair addresses these contract inconsistencies without adding another registry, world-wide loop, timeout, or balance surface. The remaining uncertainty is runtime confirmation of recipient scope and terminal engine behavior.

## Applied owner contract

1. Make due review a review operation, not an unconditional opening command.
Preserve `event021_review_current_country`, route and pool refresh, settlement, reconstruction, and recurrence-window maintenance.
After fresh eligibility and pressure checks, only a Critical country enters the Evolution III launch queue.
Stable, Exposed, and Fractured countries remain eligible for normal Event 021 selection where the existing target predicates permit it, without guaranteed launch on review date.
Recurrence memory, grace, cooldown, generation limits, and normal weighted selection remain intact.
Explicit normal event firing, Wars-cluster reservations, and SCN-018 retain their separate entry contracts.

2. Give one selected Critical country an explicit owned launch claim.
Retain `random_civil_war_launch_in_progress` and `random_civil_war_launch_target` as the global exclusion pair.
Add the country flag `random_civil_war_critical_launch_pending` only to the selected target.
Retain the queue row and its original `random_civil_war_critical_queue_date` during preflight rather than dequeueing on claim.
Use actual membership of `global.random_civil_war_critical_queue` as admission truth, synchronizing the queued flag without adding duplicate rows or resetting wait age.
Do not add a second registry, a world-wide pulse, or a fixed protected launch date.

3. Add the hidden recipient callback `chaosx.nr21.18` in `events\021_random_civil_war.txt`, calling COUNTRY helper `event021_parent_commit_critical_country`.
The scheduler calls it on the saved target, giving opening helpers recipient `ROOT` instead of relying on the global host's inline effect frame.
This callback has no player option, picture, or independent event-weight consumption.
It uses existing opening presentation and `event021_parent_record_system_log` after actual commit, recording the Evolution III launch origin rather than another random-event firing.

4. Add COUNTRY trigger `event021_parent_reserved_critical_launch_valid` beside the existing parent capacity predicate.
It requires the pending flag, a global launch target equal to `THIS`, the matching global launch lock, enabled event and Evolution III, fresh Critical pressure, normal human-country eligibility, valid route, expired grace and cooldown, generation allowance, current theater capacity, and no unrelated opening plan.
Only this owner may use the reserved admission alternative in target preparation and transaction start.
Keep `event021_parent_global_capacity_ready` closed for every unrelated country and ordinary, cluster, or scenario caller while the claim exists.
Do not use a blanket exception that makes any country pass because a Critical launch is pending somewhere.
Refresh through existing `event021_refresh_country_state` and `event021_parent_prepare_route_evidence` before testing the reserved predicate.

5. Keep the existing centralized limits unchanged.
`constant:event021_scheduler.maximum_review_scan` is 6, `maximum_critical_scan` is 3, and `constant:random_civil_war_capacity.critical_launch_batch` is 3 in the reviewed source.
Admission budget `global.random_civil_war_critical_queue_budget` and launch-attempt budget `global.random_civil_war_critical_launch_budget` are distinct.
Debit one launch-attempt token before callback dispatch, never again inside commit, and never refund a failed preflight within the pulse.
At most one attempt per country per scheduler pulse is permitted, including row removal and cursor wrap.
A proposed country date `random_civil_war_critical_last_attempt_date` can enforce that rule using the existing date-based pulse cadence, with unset values permitting the first attempt.
The pending owner must not receive a fresh budget merely because callback execution crosses batch cleanup.
Theater and front counters still increase only through existing successful opening registration.

6. Finish the claim from actual terminal opening outcomes, not immediately after the scheduler queues a callback.
Ordinary, Event 006, and same-tag routes use their existing actor, state, force, capital, diplomacy, and rollback machinery.
On committed host activation, dequeue once and record `launched` only after the existing opening transaction reaches its terminal cleanup.
On stabilization below Critical, dequeue once and record `stabilized` without actors or transferred states.
On lost human eligibility, route, enable state, or country existence, remove the row and record `invalidated` where its country scope survives.
On valid but rejected precommit planning, keep the row and original wait date, roll back existing reservations, clear the claim, and advance the bounded cursor.
Use country receipt `random_civil_war_critical_exit_reason`, with centralized non-balance enum values `launched = 1`, `stabilized = 2`, and `invalidated = 3` under `event021_critical_queue_exit`.
A retained row after a failed attempt has no exit reason.
All terminal paths clear the pending flag and call `event021_finish_critical_launch` exactly once.
Hook surviving-target cleanup and orphan-target cleanup through the existing bounded scheduler and country cleanup, without a new global iteration or an invented timeout.
Do not clear a still-live claim solely because callback execution has not yet returned.

## State, actor, resource, and AI interactions

Queue admission itself transfers no owner, controller, core, capital, unit, manpower, or equipment.
Successful dispatch uses existing `global.random_civil_war_plan_states`, `global.random_civil_war_reserved_states`, `random_civil_war_host_country`, and `random_civil_war_anchor_state` rather than choosing another map or actor package.
Failed precommit planning must leave state ownership, capitals, stockpiles, forces, generation, and recurrence consumption unchanged after rollback.
No new state group is proposed.
In an ordinary territorial fixture, use the existing plan's protected parent capital and disjoint connected actor states.
In an Event 006 fixture, preserve the selected human package, origin separation, and grace rather than setting Event 006 global firing or league state.
A same-tag fixture must preserve country identity and state ownership while using its existing takeover machinery.

`event021_protect_communications` spends command power and trains, calls `event021_decision_protect_communications`, and applies centralized pressure relief and authority gain before refreshing state.
`event021_review_regional_administration` spends political power and manpower and performs the equivalent administrative prevention refresh.
`event021_review_loyalty` spends command power, army experience, and political power, with its existing hardliner-specific downside rather than unconditional relief.
Convergence makes a successful fall below Critical cancel forced queue launch, without refunding action costs or guaranteeing immunity from normal future selection.
Keep current costs, relief values, cooldowns, icons, and category size.
If current tooltip wording promises inevitability or protection until a fixed date, correct only that contradiction in the corresponding Event 021 localisation.

AI uses the same decisions and queue eligibility as the player, without free prevention effects.
Keep current weights and shortage gates rather than choosing new balance targets in this plan.
The auditor must check capital-supply-risk communications priority, failing-authority administration priority, hardliner loyalty consequences, and recurrence eligibility under the same pre/post scenarios.
Selection and timing conclusions remain unresolved until that specialist evidence exists.

## Implementation surfaces and acceptance evidence

Parent-owned surfaces are `events\021_random_civil_war.txt`, `common\scripted_effects\021_random_civil_war_parent_effects.txt`, `common\scripted_effects\021_random_civil_war_effects.txt`, `common\scripted_triggers\021_random_civil_war_parent_triggers.txt`, and the queue-exit enum in `common\script_constants\021_random_civil_war_constants.txt`.
Existing decisions and their effect file are scenario consumers, not authorized cost or AI rewrites from this addendum.
Update `docs\events\021_random_civil_war\overview.md` and `acceptance_evidence.md` only after owner implementation facts are available.
No workbook change is part of this planner pass.

Use the existing GLB-01 through GLB-07 and REC-01 through REC-06 names, extending their manifests rather than replacing the scenario matrix.
Each fixture must declare the scheduler host, recipient countries, human classification, pressure and authority, route predicates, grace, enable state, queue rows and dates, cursor, budgets, capacities, and frozen opening inputs.
Compare the same fixture before and after the owner patch.

| Evidence case | Required outcome |
| --- | --- |
| GLB-03 with a viable route and a due Stable, Exposed, or Fractured country | Review alone creates no actor or forced opening and spends no launch token, while normal eligible selection remains possible. |
| GLB-01 with six due review rows and three queued Critical targets | Review, admission, and launch limits remain distinct, with no more than three attempts and no due-review bypass. |
| GLB-01 recipient differs from scheduler host | Callback `ROOT` is the recipient, its owned claim passes preparation and transaction start, and a second country cannot enter through the lock. |
| GLB-04 at full theater capacity, followed by prevention and then released capacity | Original queue age persists while Critical, a genuine fall below Critical exits without opening, and released capacity does not launch the recovered country. |
| GLB-01 with one valid precommit failure | One token is consumed, no same-pulse retry occurs, the valid row retains its wait date, reservations are cleaned, and state and resource outputs are unchanged. |
| GLB-05 plus a missing queued flag, row removal, and cursor wrap | Membership, count, flags, dates, and cursor converge without duplication, skipped retained rows, or orphan launch target and lock. |
| GLB-06 and GLB-07 with ordinary and same-tag controls | Eligible human reuse preserves package and origin contracts, actual nonhuman targets remain excluded, and each committed route records only one Evolution III launch. |
| REC-01 through REC-06 with review due below Critical | Removing forced due dispatch does not erase conditional recurrence, bypass grace, consume generation on rejection, or permit a nonhuman successor. |
| Queued callback interrupted before terminal cleanup | A live claim remains exclusively owned until its terminal outcome, and cancellation or absent target cleanup cannot leave a permanent lock or grant another launch budget. |

Required parent evidence is current-revision source review, helper-expanded event inspection and rendering, a valid cached baseline and `hoi4.event_compare`, fixture-specific queue and transaction traces, and existing task-specific completion audits.
Map acceptance requires inspection and rendered evidence of actual planned capital, connected actor states, remnant, supply, and reservation collisions for the fixtures, not a world map alone.
User-owned live consumer evidence remains separate from planner source observations.
Any owner-applied probability-bearing change requires the read-only `chaosx_ai_probability_auditor` baseline and mandatory `hoi4.probability_compare` on the same named scenarios.

## MCP evidence and exact limitations

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.
Read-only event trace for `chaosx.nr21.1` returned `EVENT_INSPECTED_PARTIAL`, revision `ece7356e35dcc9c2d4ab28eee66f573503821339c977879ef556cc72a00e18a8`, with helper and lifecycle projection deferred and validation false.
Read-only neighborhood rendering returned `EVENT_RENDERED_PARTIAL` at that revision.
The inspected PNG contains only the entry event and an unresolved dispatch-helper node, not the queue lifecycle or a player event card.
Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/89ef3dfd55c8f624309c40889e6ee5ba66fd1124a38b07ca41156c2551328d1f/5393d9fce090fe3b7bef56b75bcc175d872ba257d3eb041c4c45a687e6f9d23d/event-neighborhood-ece7356e35dc.png`.
Full refreshed `state_flow` inspection failed with `INTERNAL_ERROR` and message `Unexpected internal error`, returning no artifacts.
Read-only event comparison using the trace revision failed with `EVENT_REVISION_NOT_CACHED` and message `Requested event graph revision is not cached`.
Do not call source-only review equivalent lifecycle or engine evidence.

Read-only `hoi4.probability_inspect` on `common/decisions/021_random_civil_war_decisions.txt`, surface `decision_ai_will_do`, returned `PROBABILITY_SOURCE_INSPECTED` with 18 candidates, zero available candidates, 12 required inputs, and `poolComplete = false`.
Its source revision is `79f682b25251c50e9d5adc48ea29008f02db2761ef58bb5b9b89a2eb2b5cb292`.
The current specialist route is constrained by the user's explicit no-agent instruction, so this planner did not spawn or impersonate `chaosx_ai_probability_auditor`.
Use the existing `subagent_handoffs\ai_probability_audit_continuation_2026-09-13.md` and `probability_current_2026-09-12.md` as bounded historical specialist evidence only.
They do not provide a current convergence certificate or resolve incomplete pools.
Fresh timing, AI, and pre/post probability conclusions are blocked for this pass.

Read-only map inspection of state 121 returned `MAP_INSPECTED`, revision `6144a92ecf747ed346912e8d9a834b6a2199d6457dab10cdd241a0b84cf984f5`.
Membership and network checks passed, while positions, ports, and entities failed with diagnostics truncated by 2654 omitted errors.
Those workspace diagnostics are not automatically Event 021 defects.
Recovered integer-scale rendering returned `MAP_RENDERED`, and the complete 361772-byte PNG was assembled from verified byte ranges and visually inspected.
It shows a world-wide state/network representation, not a verified Event 021 partition for state 121.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/753f3fd786736597a134c1054beec6c95c109ee897d29b006c51ee936abbd08c/c5ec0dfdf5186f0b4611e756ceaf5458d8a9d2a9ddfd20b0741abd1869bb11c7/map-state.png`.
No new GUI, focus, technology, or doctrine surface is included or certified by this addendum.

Standalone Technology Tree Viewer availability was checked separately from exposed tools and successful event service calls.
The npm shim points into `C:\Users\klimp\AppData\Roaming\npm\node_modules\hoi4-agent-tools`, whose inspected package is 3.0.7.
The separate local 3.0.8 and 3.0.9 package inventories likewise contain stdio, HTTP, and setup entrypoints, with no standalone viewer binary entrypoint.
The 3.0.9 technology documentation describes read-only MCP technology viewer routes, not a separate application entrypoint.
Record this verified package-local standalone-viewer absence as a package gap, not proof that no viewer exists anywhere on the machine or that the running technology service is healthy.
It is not an Event 021 acceptance dependency because this proposal adds no technology tree.

## Source anchors, research, and promotion

These SHA-256 anchors identify the reviewed source capture rather than the entire changing worktree.
Parent repairs continued during review, so the source hashes in this historical addendum require comparison with the current checkout before relying on them.

| Source | SHA-256 |
| --- | --- |
| `common\scripted_effects\021_random_civil_war_parent_effects.txt` | `a007b3b87e582e2fb1c3383d8a1a74940a90b47b60f9465bcf822895c70db95a` |
| `common\scripted_effects\021_random_civil_war_effects.txt` | `a70c458b96b2796de57657e852466dd86c72b809b2dab2b6f449fc7e5aa56b62` |
| `common\scripted_triggers\021_random_civil_war_parent_triggers.txt` | `019dfa864dfab233d8e760017ce243251264d1df3e252c502bf653be8697f670` |
| `common\scripted_triggers\021_random_civil_war_triggers.txt` | `781e383f6a4e9a085c7a44ac42366e2687d8c98218cd6780c15e6306911a0391` |
| `events\021_random_civil_war.txt` | `78d8eb2bb5e3cbb0a5e113789df73d03690b7fd895d1fe58bda43f8e72e33bd8` |

Research basis is the complete existing Event 021 research and design package, current source, current parent repair handoffs, required offline wiki pages, and vanilla event-target, scope, event-dispatch, and script-constant documentation.
Vanilla `events\Spain.txt` supplies a concrete explicit-capital and explicit-state civil-war precedent, not proof of this custom scheduler's concurrency behavior.
The regional connection remains the accepted distinction between functioning communications, administrative reach, command loyalty, and organized opposition in a real territorial plan.
No new historical or cultural claim, named faction, border narrative, or country package is proposed, so this bounded contract repair does not require inventing additional historical research or uncertain attribution.

Skills used are `chaos-redux-improvement-loop`, `chaos-redux-event-planning`, `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`.
Their influence is the rejection of breadth, explicit ownership and disposition, resource-to-state causality, and unresolved evidence boundaries.
No skill was created or updated.

## Parent disposition

The parent has promoted this bounded convergence into the test-entry implementation with the explicit limit that final acceptance remains unresolved.
The queue contract and callback integration are implemented in the current source, and the GLB/REC fixtures remain evidence obligations because MCP lifecycle projection and live terminal behavior are not proven.
No new gameplay surface is introduced by this disposition.

The queue contract is promoted into source-spec part 6, callback integration is represented in part 8, and the unchanged GLB/REC acceptance matrix remains a part 10 and scenario-matrix test obligation.
The older direct-due-dispatch review is superseded by this owner-aware queue decision, while its runtime risks remain listed below.
Current source evidence is recorded in `docs/events/021_random_civil_war/acceptance_evidence.md`; the current Event MCP result is partial and does not establish live or helper-expanded acceptance.

Remaining risk is recipient scope, lock and callback lifetime, budget reset timing, queue cursor mutation, rollback conservation, and below-Critical recurrence after convergence.
Independent inherited risks remain the shared fixed-target contract, Event 006 package evidence, complete probability certification, lifecycle continuity, and final acceptance documentation.
The shared dependency remains owned by the other event owners described in `subagent_handoffs\individual_crisis_fixed_target_contract_2026-09-13.md`.
This proposal neither supplies a substitute helper nor declares those obligations complete.
Parent handoff: accept, explicitly queue, or reject this one connection repair, finish the existing accepted obligations, and do not add broader event content solely to prolong the improvement loop.

Delivery status: the queue repair is implemented and the test-entry status is recorded as `Needs Testing`; the current source hashes and MCP evidence are maintained in the acceptance ledger. No live gameplay, save/reload, or performance claim is made.
