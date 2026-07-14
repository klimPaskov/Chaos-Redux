# Chaos Unit Family Registry

The Chaos unit family registry is the opt-in contract used by Event 19 and future systems that need to discover unusual battalion families without maintaining their own family lists.

## Ownership model

Each family owns one registration effect, one startup registration call, and a provider effect set. Event 19 reads the aligned `global.chaos_unit_family_*` rows and dispatches through the stored provider ID. Adding a future family therefore does not require an Event 19 edit.

The shared registry never infers eligibility from a unit token and never substitutes a different family. A missing provider, duplicate family ID with conflicting ownership, unsupported contract version, or misaligned table sets `chaos_unit_family_registry_invariant_failure` and prevents the affected Event 19 operation.

## Registration fields

Every row records:

- family, provider, and source-event IDs;
- trainable, spawn-only, or combined availability;
- Event 19 family-lot and ordinary-mix policy;
- derivative, sustainment, containment, AI, visual, cleanup, and parent-isolation profiles;
- spawn weight and contract version.

Family-specific values and static unit tokens remain in provider-owned files. The shared registry contains only contracts and aligned rows.

## Provider contract

An Event 19-capable provider implements:

- `chaos_unit_family_provider_N_event19_evaluate_eligibility`;
- `chaos_unit_family_provider_N_event19_build_template`;
- `chaos_unit_family_provider_N_event19_spawn_unit`;
- `chaos_unit_family_provider_N_event19_evaluate_management`;
- `chaos_unit_family_provider_N_event19_pay_management_action`;
- `chaos_unit_family_provider_N_event19_refund_management_action`;
- `chaos_unit_family_provider_N_event19_reconcile_sustainment`;
- `chaos_unit_family_provider_N_event19_setup_derivative`;
- `chaos_unit_family_provider_N_event19_cleanup`.

Static-token operations are selected with `meta_effect` using the recorded provider ID. Registration is idempotent, so startup initialization cannot duplicate a row.

`event19_evaluate_management` reports provider-owned train and spawn eligibility, costs, and weights through the shared temporary-variable contract. `event19_pay_management_action` must set `infantry_spawn_family_management_payment_success` only after every provider-owned cost has been paid. If template creation or unit spawning then fails, Event 19 calls `event19_refund_management_action`; that hook must restore exactly the resources consumed by the selected action. Shared political-power, command-power, cooldown, Muster Control, and per-generation escalation costs remain Event 19-owned and are accounted separately.

## Event 19 isolation

The initial providers expose only base `zombies`, `death_weak_ghost_host`, and `coal_golem`. Base zombies may be trainable. Ghosts and golems are spawn-only. Provider code may reuse the unit token but must not call the parent event's country setup, evolution, super-event, or world-end helpers.
