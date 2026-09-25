# Event 016 private Singularity construction transactions

## Purpose and scope

The COUNTRY-scoped effects in `016_mengele_singularity_construction_effects.txt` pay for and settle the Directorate's state-targeted command nodes and power links.
The physical row belongs to `016_mengele_singularity_site_effects.txt`, while the native decision owns its temporary civilian-factory reservation and timer.
No effect writes a Kruger payment, site, stage, or terminal receipt.

## Inputs and outputs

Before a begin, finish, or cancel call, the decision saves `FROM` as the regular `mengele_event016_singularity_site_selected_state` target and supplies `mengele_event016_singularity_site_selected_role` and a quantity of one.
Each public role wrapper sets `mengele_event016_singularity_construction_expected_role` itself.
The begin core returns temporary `mengele_event016_singularity_construction_begin_applied` as zero or one; the finish core similarly returns `mengele_event016_singularity_construction_finish_applied`.
Absent or malformed direct-payment fields produce no reconstructed refund from current tuning constants.

## Transaction steps

The begin core checks the private provider, the role-specific unlock and live need, absence of another paid reservation, direct-resource affordability, and the exact selected state after the native timer may already have reserved civilian factories.
The visible cost row checks only factories and the five spendable resource amounts, while a separate requirement tooltip covers route, facility, selected site, and active construction state.
It reserves a private pending physical row first, rechecks direct-resource affordability without double-counting the native factory reservation, then snapshots the five direct costs and debits Political Power, Support Equipment, trucks, fuel, and manpower once.
If the reservation or affordability check fails, no payment remains and the pending row is cancelled.
The decision's `civilian_factory_use` reserves and releases factories through the native lifecycle; the scripted receipt never grants or refunds factories.

A matching callback must identify the original state, role, and quantity before clearing the payment receipt.
Completion additionally requires the registered provider, the matching physical pending row, and current control of a qualifying facility.
It clears the paid receipt before marking that row live; an invalid matching callback instead cancels the row and refunds the saved five amounts once.
An unrelated state or role callback leaves the current receipt untouched.
Provider closure and world-end cleanup call `brilliant_scientist_mengele_singularity_construction_cleanup` before `brilliant_scientist_mengele_singularity_site_retire_all`, preserving durable construction history and settling unresolved direct payment only once.

Example: after selecting a controlled facility state, the command-node decision saves its state target, role, and unit quantity and calls `brilliant_scientist_mengele_singularity_construction_begin_command_node = yes`; its matching native removal callback supplies the same state and calls `brilliant_scientist_mengele_singularity_construction_finish_command_node = yes`.

## Assets and future plans

Both decisions reuse vanilla `GFX_decision_generic_research` from the game's `interface/decisions.gfx`, so no new bitmap or mod sprite definition is needed.
They share the existing Event 016 command-node and power-link cost text and reuse the existing construction duration, cost, and AI constants.
Future presentation may expose the authenticated site ledger in the existing Directorate UI if it can show the exact state and live status without trusting stale aggregate counts.
