# Event 016 Singularity construction transaction effects

## Purpose

This file provides the payment and callback transaction boundary for the existing Singularity command-core and power-link construction decisions.

The physical-site ledger in `016_brilliant_scientist_singularity_site_effects.txt` owns the selected state row, physical validity, live counts, and durable site history.

This file owns one country-scoped private resource receipt and the shared `brilliant_scientist_project_stage_in_progress` flag for that receipt.

The effect set does not add a project family, stage, component, timer, decision, facility, model, GUI, probability rule, or AI weight.

## Scope and caller contract

Every public effect runs in the paying construction country scope.

Before a begin, finish, or callback-cancel call, the parent decision/callback supplies the regular event target `brilliant_scientist_singularity_site_selected_state` and temporary `brilliant_scientist_singularity_site_selected_role` and `brilliant_scientist_singularity_site_selected_quantity` values.

The selected role is `constant:brilliant_scientist_singularity_component.command_core` or `constant:brilliant_scientist_singularity_component.power_link`.

The selected quantity is exactly one; multiple paid rows at the same valid state remain possible through separate transactions.

The role-specific wrapper supplies an expected role only in a temporary variable and never overwrites the caller's selected role, state target, or quantity.

## Receipt schema

All receipt fields below are ordinary country variables, not temporary variables.

| Field | Meaning |
| --- | --- |
| `brilliant_scientist_singularity_construction_receipt_active` | Country flag proving this construction transaction owns the shared stage flag and a pending physical row. |
| `brilliant_scientist_singularity_construction_receipt_state` | Persistent state-scope pointer copied from the selected event target. |
| `brilliant_scientist_singularity_construction_receipt_role` | Exact command-core or power-link role ID. |
| `brilliant_scientist_singularity_construction_receipt_quantity` | Exact paid quantity, currently one. |
| `brilliant_scientist_singularity_construction_receipt_political_power` | Positive PP quote charged at begin. |
| `brilliant_scientist_singularity_construction_receipt_support_equipment` | Positive support-equipment quote charged at begin. |
| `brilliant_scientist_singularity_construction_receipt_trucks` | Positive motorized-equipment/truck quote charged at begin. |
| `brilliant_scientist_singularity_construction_receipt_fuel` | Positive fuel quote charged at begin. |
| `brilliant_scientist_singularity_construction_receipt_manpower` | Positive manpower quote charged at begin. |

No civilian-factory receipt field exists.

The native decision's `civilian_factory_use` modifier owns CIC occupation and automatic release when its timed decision ends or is cancelled.

These effects never call `add_factories`, `remove_factories`, or refund a fabricated CIC balance.

## Source-of-truth cost and duration map

| Role | PP | Support | Trucks | Fuel | Manpower | CIC occupation | Native duration |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Command core | `constant:brilliant_scientist_project_board.singularity_node_political_power` | `...singularity_node_support_equipment` | `...singularity_node_trucks` | `...singularity_node_fuel` | `...singularity_node_manpower` | `...singularity_node_civilian_factories` | `constant:brilliant_scientist_singularity.core_construction_days` |
| Power link | `constant:brilliant_scientist_project_board.singularity_link_political_power` | `...singularity_link_support_equipment` | `...singularity_link_trucks` | `...singularity_link_fuel` | `...singularity_link_manpower` | `...singularity_link_civilian_factories` | `constant:brilliant_scientist_singularity.delivery_construction_days` |

The cost constants are defined in `common/script_constants/016_brilliant_scientist_project_constants.txt`.

The duration constants are defined in `common/script_constants/016_brilliant_scientist_constants.txt`.

The existing `brilliant_scientist_pay_singularity_command_node` and `brilliant_scientist_pay_singularity_power_link` effects remain the resource debit source for support equipment, trucks, fuel, and manpower.

The wrapper snapshots the same positive constants before calling those pay helpers and separately debits the PP quote with `add_political_power` multiplied by `constant:brilliant_scientist_directorate_value.negative_one`.

## Effects and interfaces

### Internal metadata effects

`brilliant_scientist_singularity_construction_clear_receipt` clears only the private receipt flag and ordinary receipt variables.

It does not clear the selected event target or temporary callback inputs because the physical-site effect still needs them.

`brilliant_scientist_singularity_construction_snapshot_receipt` copies all five positive resource values into temporary refund values before receipt clearing.

It marks `brilliant_scientist_singularity_construction_refund_snapshot_complete` as zero if any receipt amount is absent, so malformed data cannot cause a recomputed or partial refund.

`brilliant_scientist_singularity_construction_refund_snapshot` refunds one complete temporary snapshot and never reads current cost constants.

### Begin

`brilliant_scientist_singularity_construction_begin_command_node` and `brilliant_scientist_singularity_construction_begin_power_link` are the public role wrappers.

They call `brilliant_scientist_singularity_construction_begin_core` after setting the expected role temporarily.

The core first requires `brilliant_scientist_project_board_is_ready`, no active private receipt, exact selected role, and quantity one.

The board-ready trigger supplies the current-host, primary-facility, no-terminal, no-world-end, no-existing-stage, and no-incident gates.

The core calls `brilliant_scientist_singularity_site_reserve_construction` before evaluating `brilliant_scientist_can_pay_singularity_command_node` or `brilliant_scientist_can_pay_singularity_power_link`.

If reservation succeeds but affordability fails, it calls the authoritative physical cancellation effect and charges nothing.

On success it snapshots the selected state, role, quantity, and exact five resource quotes into the ordinary receipt, sets the private receipt flag, calls the existing four-resource pay helper, debits PP exactly once, then sets the shared stage flag.

Temporary output `brilliant_scientist_singularity_construction_begin_applied` is one only after all payment and both receipt flags have been set.

### Finish

`brilliant_scientist_singularity_construction_finish_command_node` and `brilliant_scientist_singularity_construction_finish_power_link` are the public role wrappers.

They call `brilliant_scientist_singularity_construction_finish_core` with the expected role held temporarily.

The core's first branch is the exact construction callback identity guard: the active private receipt, the persistent selected state, expected role, selected role, selected quantity, quantity one, and all five stored resource amounts must be present and match.

When a physical pending receipt still exists, its physical callback identity must also match; when a lifecycle hook has already consumed that row, physical-row absence is accepted so the private receipt can still take the refund path.

A wrong state or role callback is a no-op and cannot clear either receipt or the shared stage flag.

For a matching callback, the core snapshots the receipt and clears its own active metadata before invoking any physical completion/cancellation output.

If `brilliant_scientist_project_context_is_valid` and `brilliant_scientist_singularity_site_pending_callback_is_valid` both hold, it calls `brilliant_scientist_singularity_site_complete_pending_construction`.

A completion output of one clears the shared stage flag and sets temporary `brilliant_scientist_singularity_construction_finish_applied` to one without refunding any cost.

If current host, control, facility validity, or the physical pending row is lost, the core calls physical cancellation and refunds the exact snapshot once.

The refund path sets temporary `brilliant_scientist_singularity_construction_finish_refunded` to one.

The unexpected physical-completion-zero branch is also treated as invalid and refunded, so no reward is granted without a physical completion output.

### Callback cancellation

`brilliant_scientist_singularity_construction_cancel_command_node` and `brilliant_scientist_singularity_construction_cancel_power_link` call the shared callback cancellation core with the expected role.

The core performs the same construction-receipt identity-first guard as finish, then snapshots and clears the receipt before invoking physical cancellation.

Only a matching callback refunds the exact five-value receipt and clears `brilliant_scientist_project_stage_in_progress`.

Temporary outputs are `brilliant_scientist_singularity_construction_cancel_applied` and `brilliant_scientist_singularity_construction_cancel_refunded`.

### Lifecycle cleanup

`brilliant_scientist_singularity_construction_cleanup` is an authoritative owner cleanup for capture, annexation, terminal shutdown, and other owner-loss paths.

It requires only this transaction's private active flag.

It deliberately does not require a selected callback target, current ownership, control, or an intact facility.

It snapshots and clears the private receipt, calls physical cancellation, refunds a complete exact snapshot, and clears the shared stage flag.

It cannot clear or cancel an unrelated board stage because it does nothing when this construction receipt flag is absent.

Temporary outputs are `brilliant_scientist_singularity_construction_cleanup_applied` and `brilliant_scientist_singularity_construction_cleanup_refunded`.

## Integrated call-site map

The decision owner sets the selected state target, selected role, and selected quantity before begin and before callback finish/cancel calls.

The native construction `complete_effect` blocks use the matching begin wrapper, the exact timed callbacks use the matching finish wrapper, and callback cancellation uses the matching role-specific wrapper.

The decisions use their `custom_cost` path so PP is not charged once by the decision and again by this transaction.

The existing `modifier = { civilian_factory_use = ... }`, `days_remove`, and score factors are preserved; visibility uses live physical room and the AI receives the matching 100-PP custom-cost hint.

Lifecycle and terminal owners call `brilliant_scientist_singularity_construction_cleanup` from the paying country scope, including annexation and pre-annex civil-war cleanup.

No ordinary relationship cleanup should invoke this effect unless it is an actual construction-owner lifecycle boundary.

## Scenario traces

### Successful begin and finish

The begin wrapper reserves one valid physical row, snapshots the role and current cost constants, calls the existing four-resource pay helper, debits 100 PP, sets both active flags, and returns `begin_applied = 1`.

The matching finish callback clears the private receipt before physical output, marks the exact pending row live/history-constructed, clears the shared stage flag, and returns `finish_applied = 1` with no refund.

### Duplicate begin

A second begin while the private receipt or shared board stage is active fails the board-ready/no-receipt guard and cannot append a second pending row or debit resources.

### Wrong-role or wrong-state callback

A command-core wrapper receiving a power-link role or a different state target fails the construction-receipt identity guard before any clear, physical mutation, refund, or shared-flag mutation.

The still-live original callback remains owned by its original receipt.

### Captured owner or lost facility at expiry

If the receipt identity still matches but the host, control, selected facility, terminal context, or physical pending row is invalid, finish clears its private receipt, cancels the pending physical row if present, refunds the exact snapshot once, clears the shared stage flag, and grants no physical completion.

### Authoritative capture/annexation cleanup

When a lifecycle owner cleanup runs after ownership loss and callback context is unavailable, the cleanup effect still finds its own active receipt, clears and cancels it, refunds once from the stored receipt, and clears only the shared flag owned by that receipt.

### Repeated stale callback

After finish, callback cancellation, or lifecycle cleanup clears the private receipt, the same callback has no active receipt identity and becomes a no-op.

### Malformed receipt

If any stored resource field is missing, finish and callback cancellation fail closed before settlement; authoritative cleanup still clears the private active receipt and physical pending state but marks the refund snapshot incomplete and does not invent a replacement amount.

## Validation and limits

Repository source review checked the existing role-specific constants, pay helpers, board-ready and affordability triggers, physical-site interfaces, and native decision duration/CIC fields.

The new file was checked for balanced Clausewitz braces and unsupported comparison operators.

No Hearts of Iron IV process was launched, no game logs were read, and no live consumer acceptance is claimed; the user performs live validation.

Receipt absence is a cancellation condition for both native timers, so a begin-time revalidation failure cannot strand an empty 1080-day or 720-day decision.

The physical-site file and its triggers are separate owned work; this transaction layer depends on their documented interfaces and does not duplicate their arrays or reconciliation.
