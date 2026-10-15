# Famine decision-owner start and paid-receipt triggers

These additions are COUNTRY-scope hidden Boolean guards for the existing famine decision actions. They read the current decision actor as `ROOT` and the selected state as `FROM`; they do not mutate state, resources, cohorts, contracts, or country flags.

## Reserve-release target

`famine_state_needs_reserve_release` (STATE scope) holds when the committed food stage is supply strain or worse (`famine_state_has_visible_food_problem`) or a live food shock is recorded (`famine_food_pressure` above zero). Blockade, occupation and historical-profile famines raise the stage without any shock, so the stage alone qualifies.

`famine_state_can_release_reserves` (STATE scope) adds a valid civilian state, the active food registration, an initialized reserve and stock above `famine_mission_contract.minimum_relief_grant`.
The Release Reserves decision uses it in `visible`, in the `available` tooltip `famine_release_reserves_target_tt`, and in `target_trigger`; `famine_release_reserves_can_start` uses the same trigger, so the AI and the player see one target rule.

No famine decision is hidden by another decision's country-wide target. Each action is shown or offered only by its own selected-state conditions, so Airlift Relief stays available beside Escort Relief and Continue Requisitions beside Conceal Hunger.

## Complete-action start predicates

Each `famine_<action>_can_start` predicate repeats that action's current visible, available, and selected-target prerequisites, confirms that `FROM` is still controlled by `ROOT`, and calls the action's exact inclusive `humanitarian_cost_*_is_affordable` bundle. The decision's `available` block retains the original player-facing non-cost requirements and uses the same cost profile; `custom_cost_trigger` also uses that exact profile. The `complete_effect` places its whole original body under this predicate so no setup, phase, payment, policy, service, mission, or report side effect runs after a stale or invalid start.

The action predicates are:

| Trigger | Existing action |
|---|---|
| `famine_release_reserves_can_start` | `famine_release_reserves` |
| `famine_emergency_imports_can_start` | `famine_emergency_imports` |
| `famine_repair_relief_route_can_start` | `famine_repair_relief_route` |
| `famine_escorted_relief_convoy_can_start` | `famine_escorted_relief_convoy` |
| `famine_emergency_airlift_can_start` | `famine_emergency_airlift` |
| `famine_evacuation_can_start` | `famine_evacuation` |
| `famine_requisition_safer_state_can_start` | `famine_requisition_safer_state` |
| `famine_conceal_crisis_can_start` | `famine_conceal_crisis` |
| `famine_maintain_extraction_can_start` | `famine_maintain_extraction` |

The paid airlift bundle includes transport aircraft5, fuel1000 and air XP10. Its cost component is separate from the unchanged AI-only strict 50-XP factor. The worker support50 prerequisite is migration-owned and remains separate from this API.

## Delayed paid-receipt guards

Each `famine_<action>_cost_receipt_is_valid` predicate requires its own selected-state paid flag, its stored payer to exist and equal callback `ROOT`, and the state still to be controlled by that payer. The state container supplies action/state identity; no country-global payment flag, action mapper, or generation UID is used.

All receipt predicates require only the exact selected state, that action's paid flag, the recorded payer to exist and equal callback `ROOT`, and the payer to remain the current controller. The foreign-relief decisions evaluate a separate exact-work guard before consuming their contract metadata: `famine_emergency_imports_cost_contract_is_current`, `famine_escorted_relief_convoy_cost_contract_is_current`, and `famine_emergency_airlift_cost_contract_is_current` each require the current route mode, actor, stored contract generation, and donor-state identity.

The three delivery callers snapshot the exact-work result before consuming the action receipt. They clear only their own flag, payer, generation, and donor fields; `famine_relief_deliver_contract` runs only on a proven matching contract. A same-payer callback with a missing, expired, replaced, or mismatched contract consumes only its paid metadata and cannot deliver against a different live contract.

The remaining delayed receipts protect release reserves, route repair, evacuation, safer-state requisition, concealment, and extraction maintenance. They do not repeat resource-affordability checks after those costs have already been debited; original route and transfer predicates remain in their current owner blocks. The evacuation receipt guard checks only the current payer and exact selected-state control before entering the original transfer body, so its existing measured-zero-origin-debit refund remains reachable when a route or cohort later fails.

When the receipt guard fails at removal because the state is no longer valid or controlled, a fallback branch still consumes that action's own paid flag and payer (and, for the three relief actions, its saved contract generation and donor) when the recorded payer is callback `ROOT`; it runs no work and grants no refund.

Each paid action's `cancel_effect` clears only its own state-local receipt when the recorded payer is callback `ROOT`, including the saved contract generation and donor for the three relief actions. The existing evacuation cancellation cleanup remains after that scoped receipt clear. No cancellation path refunds a fee or clears another action, payer, route contract, or cohort.

The exact-work guards compare the saved donor with the live contract donor from inside the saved donor's scope through `var:PREV.famine_relief_donor_state`, because both pointers are stored on the selected famine state rather than on the donor.

The decision `available` blocks keep these private flags inside `hidden_trigger`. Each player-facing requirement that relies on a hidden scripted trigger is wrapped in a `custom_trigger_tooltip` with a plain `famine_<action>_target_tt` or mission `_available_tt` key in `localisation/english/famine_l_english.yml`.

No receipt guard claims protection against an arbitrary same-payer ABA callback because the current decision callback surface exposes no activation UID. The action/state/payer contract is bounded to the native one-pending-action lifecycle and repeated callbacks before a new activation.

## Request Relief and physical transport

`famine_invite_relief_can_start`, `famine_invite_relief_cost_receipt_is_valid`, and `famine_invite_relief_cost_contract_is_current` retain the separate overland invitation’s exact state, payer, donor and generation contract.
Each famine start requires a visible food problem in its selected state.
The action-owned cost bundle combines genuine equipment with fuel and conditional sea convoys, charges no political power, and guards all following work on the successful transport payment receipt.
The API is documented in `common/scripted_effects/migration_transport_cost_effects.md`.

## Explicit action context

Scope-sensitive bodies have one `_in_context` implementation reading the mandatory unscoped temporary COUNTRY pointer `humanitarian_action_actor` and STATE pointer `humanitarian_action_target`.
The original helper name is a compatibility wrapper initializing those inputs from ROOT and FROM before a bare `= yes` call when no explicit context is proven.
A caller that supplies an explicit envelope also initializes temporary `humanitarian_action_context_proven = 1`, so nested legacy wrappers retain that exact actor and target.
Panel gates initialize the actor from their country context and the target from the exact selected state, and an immediate country event establishes the actor as ROOT for deep owner helpers.
These helpers accept no named arguments, have no implicit scope defaults, and publish no additional gameplay output beyond their documented owner body.
These adapters do not change tuning or create independent transaction owners.
See [the shared action lifecycle](../scripted_effects/humanitarian_gui_action_effects.md) for caller, pending, and cleanup contracts.
