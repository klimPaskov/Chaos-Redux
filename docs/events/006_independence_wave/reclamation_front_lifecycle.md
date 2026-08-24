# Event 006 DM-58 Reclamation Front Lifecycle

DM-58, `independence_wave_coordinate_reclamation_fronts`, is the paid high-chaos league mission that converts a compliant league ledger into one synchronized set of finite reclamation fronts.

## Transaction

The country must be an active Event 006 carrier, a compliant league member, on the radical-revisionist league route, outside a league crisis, and backed by the minimum shared reserve.

The completed `independence_wave_focus_coordinate_reclamation_fronts` focus sets the explicit `independence_wave_focus_reclamation_fronts_authorized` gate, and the availability preflight proves the accepted three-member contract before selection. It finds three distinct compliant members, each paired with a legal claim-connected or bordering state whose external owner differs from the other two. Completion calls `independence_wave_execute_reclamation_front` once at the activating country scope, freezes the first exact witness through nested member and state searches, and checks `can_declare_war_on` before any material cost is paid.

The mission pays the strategic and major security costs defined by the existing decision cost layer and applies the standard revisionist league deltas only after the exact minimum member/target set has been frozen. A pre-cost shortfall removes staged claims and finite wargoals, opens the failure branch, and charges no material cost.

The resolver snapshots `global.independence_wave_league_member_country_entries` through the persistent ledger array and searches only living, compliant members, so a vanished or client-locked member cannot inherit a target from another member.

## Target and state reservation

`is_valid_independence_wave_reclamation_front_state` accepts only a living external owner that is not a league member, a state with a live controller, no current war, and a state that is adjacent to or claimed by the requesting member. The non-mutating preflight mirrors those member, owner, controller, state-reservation, claim-or-border, war-legality, and finite-wargoal guards. It explicitly excludes the first two selected members and owners before testing the third slot, so three isolated candidates sharing one owner do not expose DM-58. The effect resolver restores its generic member event target after each nested probe, so every state predicate is evaluated against the intended member rather than a stale inner-loop scope.

The trigger rejects states already present in the synchronized state array, rejects state markers left by an existing front, and rejects an existing `take_state_focus` wargoal against the same owner. Capital preference remains part of the package's state-selection rules where a capital is the valid anchor; DM-58 never manufactures a capital-only fallback.

The scope proof uses `any_of_scopes` over the frozen member ledger, which evaluates each ledger country as a scope. Its nested path is member one, state one, owner one, member two, state two, owner two, member three, state three, owner three. The member comparison in member two and owner comparison in owner two each take three `PREV` hops. Member three and owner three each take three hops to their immediate predecessor and six hops to the first member or first owner respectively. The member checks execute in member scopes, while the owner checks execute in owner scopes, so every `tag` exclusion compares members only with members and owners only with owners.

The resolver writes aligned member, state, and owner rows only after all three member and owner inequality checks pass, then `independence_wave_apply_reclamation_front_witness` revalidates each saved owner and member before applying any state flag, claim, or wargoal effect.

## Effect-side witness planner

`independence_wave_execute_reclamation_front` is called once from the activating country scope and takes no arguments. It clears the three staging arrays and count, scans the frozen member ledger with nested `for_each_scope_loop` and `every_state` blocks, and writes exactly three aligned rows only after a complete witness exists.

The search is mutation-free until the witness rows are written. Completion and three loop-break variables guard every nested scan, and the generic member event target is restored after each inner loop before the containing state predicate is reused.

`independence_wave_apply_reclamation_front_witness` consumes the aligned rows in reverse index order and revalidates the current owner, member eligibility, controller, connectivity, war relation, and finite-wargoal legality before setting markers, adding a claim, or creating a wargoal. Its only persistent outputs are the aligned arrays, the count, state and country staging flags, and the provenance receipts used by rollback.

The witness event targets are regular effect-chain targets and are not required after the effect returns. Persistent arrays and state flags carry the active operation across save and load, while the shared cleanup clears those arrays and receipts when the operation ends.

The planner is bounded to the ledger size and stops after the first witness, but a no-witness activation can still scan every state for each nested member tuple. No live runtime performance or save/load matrix was available to this source-level handoff.

Claims are provenance-aware. A claim is added only when the member did not already claim the state, and that state receives `independence_wave_dm58_reclamation_front_claim_added` only when the transaction created the claim.

Each accepted state creates a `take_state_focus` wargoal with a 365-day expiry and a timed `independence_wave_reclamation_front_ready` flag for the member. The state receives `independence_wave_dm58_reclamation_front_wargoal_added` only after this transaction creates that finite wargoal, so rollback never removes an unrelated wargoal with the same type and target.

No member without a valid objective receives a generic target, a fallback state, or an unconditional war.

## Resolution and cleanup

The mission completes only when the configured minimum number of members succeeds; a partial result is rolled back before payment and opens a league crisis with the failure deltas rather than silently converting a one-member action into a coordinated front. The preflight rejects a known owner collision before the mission can begin, while a legal front that disappears after the check still follows this existing pre-cost rollback. Rollback walks the aligned member/state/owner arrays, removes only claims marked as created by this transaction, removes a finite wargoal only when its transaction receipt is present, clears staged and ready receipts, and then clears the arrays and count.

The timeout path applies the existing major-loss deltas and enters the same league-crisis state without creating targets.

League phase transitions, dissolution, and generation reset call the shared operation cleanup, which clears the coordination flag, coordinator target, state markers, claim and wargoal provenance receipts, member-ready flags, aligned member/state/owner arrays, and count variable while leaving successful finite war goals to their explicit expiry. Successful completion also saves the activating country as the coordinator and schedules `chaosx.nr6.309` for the same 365-day duration as the coordination flag. That callback runs only for the still-current coordinator and clears the operation after natural expiry; an older callback cannot erase a later operation owned by another country. Individual country cleanup clears only that country's readiness receipt. If an exiting country is present in the frozen participant array, the shared operation is cancelled and cleaned up even when the remaining league still meets the minimum; finite war goals are left to their explicit expiry.

The mission title, description, cost text, category, and icon are registered in the existing Event 006 decision localisation and interface files; no new advisor or portrait asset is required.

## Source files

- `common/decisions/006_independence_wave_decisions.txt`
- `common/scripted_triggers/006_independence_wave_decision_triggers.txt`
- `common/scripted_effects/006_independence_wave_decision_effects.txt`
- `common/script_constants/006_independence_wave_constants_registry.txt`
- `localisation/english/006_independence_wave_decisions_l_english.yml`
