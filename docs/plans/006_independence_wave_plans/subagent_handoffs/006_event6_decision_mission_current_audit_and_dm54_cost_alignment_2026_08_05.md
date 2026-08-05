# Event 006 current decision and mission audit with DM-54 cost alignment

## Scope and current evidence

This audit used the live Event 006 decision, mission, trigger, effect, category, crisis, formable-registry, localisation, and specification sources after the CAT standalone-admission and supported-effect corrections.

It also used the offline Paradox wiki decision, mission, trigger, effect, scope, localisation, data-structure, event, on-action, modifier, idea, and AI references, plus the relevant vanilla documentation and decision precedents.

The inspected source includes 64 Event 006 `activation` surfaces and 19 selectable missions.

The shared decision-source AI inspection returned 54 mission candidates with zero unresolved inputs: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3699a57fafb5731b7c016e18d62df01331f22cfa0a8e5bf731e8369760a0e1ca/c1f505669f9c9a9c1108283aa60115e21200a48c272619f11b1f232c7e14a29e/probability-inspect-f84a0e082f6a.json`.

The current GUI graph inspection is recorded at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/762136c6c8202b854105d25d3d3ff2608fd76954f07b7d8a2997517a8330df8e/a85200afcf97e8ab0a4db3fed0f55b97b4e3cc928acf003eed03b880231bfc2b/gui-inspect.6f1c924ac2af501e.json`.

That GUI inspection found unrelated repository-wide sprite collisions outside Event 006 and no Event 006 decision-GUI patch was made.

## Issue list, sorted by severity

### Medium: fixed

`independence_wave_convene_formation_congress` used the shared `can_pay_independence_wave_strategic_cost` gate and `independence_wave_cost_strategic` player text, both of which specify the standard civilian-factory tier, while its active decision modifier consumed the major tier.

This made DM-54 reserve three civilian factories after displaying and checking the two-factory strategic tier.

### No current critical or high issue found

The CAT admission surface remains separate from FORM-07 readiness.

The shared cost triggers use the engine-supported manpower, army-experience, stability, war-support, equipment, factory, command-power, train, convoy, and fuel resource triggers introduced by the current supported-effect correction.

## Patch

Changed file:

- `common/decisions/006_independence_wave_decisions.txt`

Changed identifier:

- `independence_wave_convene_formation_congress` (DM-54)

Before the patch, DM-54 reserved `@CR_SC_INDEPENDENCE_WAVE_DECISION_COST_CIVILIAN_FACTORY_MAJOR` while its strategic gate and localisation used the standard tier.

After the patch, DM-54 reserves `@CR_SC_INDEPENDENCE_WAVE_DECISION_COST_CIVILIAN_FACTORY_STANDARD`, matching its availability gate, `independence_wave_cost_strategic`, and `independence_wave_decision_pay_strategic` resource transaction.

No localisation file changed because `localisation/english/006_independence_wave_decisions_l_english.yml` already expresses the standard strategic civilian-factory tier through `independence_wave_cost_strategic`, `independence_wave_cost_strategic_tooltip`, and `independence_wave_cost_strategic_blocked`.

## Decision-category lifecycle notes

The provisional, government, recognition, host-relations, patron, network, league, borders, formables, and high-chaos categories use state and route gates instead of passive political-power stores.

The main Event 006 cleanup effect removes active missions, clears target pointers and mandate state, and delegates the formable transaction cleanup to `independence_wave_formable_cleanup_runtime`.

Former-host decisions require a living saved host and refuse invalid target scopes.

Network decisions exclude the actor and hostile targets.

League operations use member-array alignment, active-crisis locks, stored target pointers where needed, and a cleanup path for expulsion, mandate, and formable state.

The formable registry requires discovery, selected profile, attested readiness, current carrier and member generations, transaction locking, and family-specific adapters before a commit can occur.

## Mission quality notes

| Mission | Owner/category/region | Requirement and duration | Success and failure | Duplicate-risk control |
| --- | --- | --- | --- | --- |
| `independence_wave_open_host_crisis` | Eligible host / crisis / host state | Occupation pressure above the configured threshold or stability below the configured threshold; 120-day timer | Success queues a bounded release attempt; timeout while pressure remains queues it, otherwise records the blocked consequence; voluntary cancellation records abandonment | Active, cooldown, global queue, release-barrier, and requester-loss guards |
| `independence_wave_convene_formation_congress` | Regional Event 006 carrier / formables / selected profile region | Prepared, attested, non-signature family with member consent and strategic capacity; configured congress window | Pays the strategic cost and resolves the preparation and congress transaction; timeout or valid cancellation calls `independence_wave_formable_fail_transaction` | Active-formable-operation, failed-congress, proposal, ledger, readiness, and commit-pending locks |
| `independence_wave_coordinate_reclamation_fronts` | Radical charter member / high chaos / league-wide front | Valid three-member war-legal preflight, reserve, strategic and major-security costs; configured long timer | Exact witness applies claims and finite war goals, or rolls staging back and enters a league crisis; timeout creates the documented failure result | Global coordinated flag, active-league-crisis lock, staging rollback, and current-member checks |

All 19 current selectable Event 006 missions declare both a timeout and cancellation trigger.

The two `visible` blocks discovered on activated rival-bloc surfaces belong to ordinary timed decisions with `days_remove`, not selectable missions, so the mission-visible no-op described by the wiki is not present in the current shared mission set.

## Cost and requirement clarity

DM-54 is now aligned with the strategic cost contract: stability, war support, command power, transport stockpile, and the standard civilian-factory reservation all agree between trigger, modifier, payment, and player text.

The crisis mission uses a separate security-plus-command-power payment and localisation that lists manpower, army experience, infantry equipment, support equipment, command power, and stability impact.

DM-58 charges its strategic and major-security resources only after freezing its valid witness, preventing payment for an invalid front.

## AI validity and route-lock notes

The shared decision inspection found no unresolved mission AI inputs.

DM-54 AI is disabled unless `should_independence_wave_ai_pursue_selected_formable` is true and receives a bounded popular-council preference.

Host, network, patron, league, and formable target helpers check existence, self-target exclusion where applicable, war status, Event 006 activity, generation, route compatibility, and lifecycle locks.

The CAT Mediterranean Network cancellation now closes if the league route disappears, and CAT admission cannot open the unimplemented FORM-07 branch without commit readiness.

## Localisation and tooltip notes

The existing strategic cost keys accurately describe DM-54 after the patch, so no new player-facing key was required.

The crisis and reclamation-front actions retain custom trigger or effect tooltips for their nontrivial world-state requirements and outcomes.

## Cleanup and exploit-risk notes

The crisis system distinguishes success, blocked timeout, voluntary cancellation, unknown queue recovery, and annexed-requester recovery, then clears queue, runtime, retry, and requester state on the corresponding path.

The formable registry clears founding invitations, ledgers, loaded profiles, consent declarations, mission state, transaction flags, and family-specific runtime during origin cleanup.

DM-58 rolls back transaction-marked claims, war goals, state flags, and staging arrays if its witness cannot complete before charges are made.

No free-unit loop, equipment-farming loop, unbounded core grant, reusable war-goal loop, or unguarded target pointer was found in the reviewed shared surfaces.

## Validation

The targeted post-patch inspection confirmed that DM-54 still uses the strategic availability helper and cost text, now reserves the standard factory tier, has no remaining major factory reservation, and retains its formable-failure cancellation lifecycle.

`hoi4.probability_inspect` completed successfully against the current shared decision source with zero unresolved mission-AI inputs.

The task-specific diff check completed without a patch-format error.

No live HOI4 session was launched, as required.

## Remaining issues and ownership

No further narrow source defect in the audited shared Event 006 decision and mission surface was safe to patch without changing accepted balance or designing a new subsystem.

No plan handoff was written because the identified issue was local and is repaired here.

This handoff does not alter the parent-owned super-event normalization work or any unrelated active worktree changes.
