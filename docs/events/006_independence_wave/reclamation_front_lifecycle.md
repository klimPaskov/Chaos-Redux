# Event 006 DM-58 Reclamation Front Lifecycle

DM-58, `independence_wave_coordinate_reclamation_fronts`, is the paid high-chaos league mission that converts a compliant league ledger into one synchronized set of finite reclamation fronts.

## Transaction

The country must be an active Event 006 carrier, a compliant league member, on the radical-revisionist league route, outside a league crisis, and backed by the minimum shared reserve.

The completed `independence_wave_focus_coordinate_reclamation_fronts` focus sets the explicit `independence_wave_focus_reclamation_fronts_authorized` gate, and the availability preflight proves the accepted three-member contract before selection. It finds three distinct compliant members, each paired with a legal claim-connected or bordering state whose external owner differs from the other two. Completion then runs the existing member loop, freezes one unique state and owner per member, and checks `can_declare_war_on` before any material cost is paid.

The mission pays the strategic and major security costs defined by the existing decision cost layer and applies the standard revisionist league deltas only after the exact minimum member/target set has been frozen. A pre-cost shortfall removes staged claims and finite wargoals, opens the failure branch, and charges no material cost.

The mission snapshots `global.independence_wave_league_member_country_entries` and resolves each living, compliant member independently, so a vanished or client-locked member cannot inherit a target from another member.

## Target and state reservation

`is_valid_independence_wave_reclamation_front_state` accepts only a living external owner that is not a league member, a state with a live controller, no current war, and a state that is adjacent to or claimed by the requesting member. The non-mutating preflight mirrors those member, owner, controller, state-reservation, claim-or-border, war-legality, and finite-wargoal guards. It explicitly excludes the first two selected members and owners before testing the third slot, so three isolated candidates sharing one owner do not expose DM-58. The member target is saved at the start of each paid loop iteration, so the resolver does not depend on `ROOT` surviving a `for_each_scope_loop` scope change.

The trigger rejects states already present in the synchronized state array, rejects state markers left by an existing front, and rejects an existing `take_state_focus` wargoal against the same owner. Capital preference remains part of the package's state-selection rules where a capital is the valid anchor; DM-58 never manufactures a capital-only fallback.

The scope proof uses `any_of_scopes` over the frozen member ledger, which evaluates each ledger country as a scope. Its nested path is member one, state one, owner one, member two, state two, owner two, member three, state three, owner three. The member comparison in member two and owner comparison in owner two each take three `PREV` hops. Member three and owner three each take three hops to their immediate predecessor and six hops to the first member or first owner respectively. The member checks execute in member scopes, while the owner checks execute in owner scopes, so every `tag` exclusion compares members only with members and owners only with owners.

The resolver saves the owner as a short-lived event target, rechecks the war legality through the saved member target, stamps the state with a generic used marker, and appends aligned entries to `global.independence_wave_reclamation_front_members`, `global.independence_wave_reclamation_front_states`, and `global.independence_wave_reclamation_front_targets`.

Claims are provenance-aware. A claim is added only when the member did not already claim the state, and that state receives `independence_wave_dm58_reclamation_front_claim_added` only when the transaction created the claim.

Each accepted state creates a `take_state_focus` wargoal with a 365-day expiry and a timed `independence_wave_reclamation_front_ready` flag for the member.

No member without a valid objective receives a generic target, a fallback state, or an unconditional war.

## Resolution and cleanup

The mission completes only when the configured minimum number of members succeeds; a partial result is rolled back before payment and opens a league crisis with the failure deltas rather than silently converting a one-member action into a coordinated front. The preflight rejects a known owner collision before the mission can begin, while a legal front that disappears after the check still follows this existing pre-cost rollback. Rollback walks the aligned member/state/owner arrays, removes only claims marked as created by this transaction, removes the finite wargoal created for that member/owner pair, clears the staged marker, and then clears the arrays.

The timeout path applies the existing major-loss deltas and enters the same league-crisis state without creating targets.

League phase transitions, dissolution, and generation reset call the shared operation cleanup, which clears the coordination flag, state markers, member-ready flags, aligned member/state/owner arrays, and count variable while leaving finite war goals to their explicit expiry. Individual country cleanup clears only that country's readiness receipt, and a member departure revalidates the minimum surviving ledger before cancelling the shared operation.

The mission title, description, cost text, category, and icon are registered in the existing Event 006 decision localisation and interface files; no new advisor or portrait asset is required.

## Source files

- `common/decisions/006_independence_wave_decisions.txt`
- `common/scripted_triggers/006_independence_wave_decision_triggers.txt`
- `common/scripted_effects/006_independence_wave_decision_effects.txt`
- `common/script_constants/006_independence_wave_decision_constants.txt`
- `localisation/english/006_independence_wave_decisions_l_english.yml`
