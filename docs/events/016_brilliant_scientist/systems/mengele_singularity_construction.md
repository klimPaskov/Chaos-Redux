# Directorate Singularity physical network

The registered Directorate constructs command nodes and power links through two paid, timed, state-targeted decisions in `mengele_clone_army_category`.
A qualifying target is an owned and controlled state with a land, air, nuclear, or biological facility.
Native Singularity component completion unlocks the corresponding site role with Gotterdammerung; the paid Prototype receipt unlocks both roles in the no-DLC decision route.

The decision reserves a private site row before it spends direct resources.
Its cost row is limited to affordability, and a separate requirement tooltip explains the route, facilities, controlled site, and free construction slot.
After the native timer may reserve the factories, the begin effect checks direct resources again without counting that reservation as a second factory cost.
It charges the same construction costs and waits the same duration as the existing Kruger actions, while native `civilian_factory_use` owns the temporary factory commitment.
Its callback matches the saved state, role, quantity, and direct-cost receipt before it can complete or refund a row.
An invalid provider, captured state, or lost facility cancels unresolved work and refunds its saved direct payment once.

Live network totals are rebuilt from aligned physical rows and current state ownership, control, and facilities.
The terminal requires at least two live command nodes and two live power links plus three qualifying controlled facilities.
Control loss suppresses a row's live contribution; intact recovery can restore it, while explicit destruction invalidates the row.
The source currently identifies no generic building-destruction callback, so a rebuilt qualifying facility can restore a row unless a destruction consumer calls the explicit invalidation effect.
Provider close, annexation, defeat, and terminal completion settle unresolved payment before retiring the private site rows, preserving durable construction history.
The existing Event 016 state-control hook refreshes private displayed totals only for a participant with a pending receipt or site rows.

## Asset wiring

Both construction decisions reuse `GFX_decision_generic_research`, defined in the vanilla `interface/decisions.gfx`, and add no mod texture or `.gfx` registration.
Their costs reuse the existing Event 016 command-node and power-link cost localisation; their titles and descriptions are in `localisation/english/016_mengele_singularity_construction_l_english.yml`.

## Future plans

An existing Directorate presentation surface could expose exact site locations, role, and live status if it derives every displayed value from the authenticated row ledger.
