# Event 016 D’Rhondan Survival Marker Consumption Handoff

## Scope

This owner-applied patch closes the DHR focus audit gap in which four survival milestones were set by completed focuses but were not consumed by any live behavior.
No focus IDs, routes, costs, landing eligibility, equipment amounts, or country-transfer rules changed.

## Changed files

- `common/scripted_triggers/016_dhrondan_focus_triggers.txt` adds four country-scoped capability readers for counted landing states, secured scattered enclaves, audited expedition stores, and restored landing beacons.
- `common/script_constants/016_alien_infantry_api_constants.txt` centralizes the three landing AI factors at `1.10`, `1.25`, and `1.20`.
- `common/script_constants/016_dhrondan_country_constants.txt` centralizes the enclave-support AI factor at `1.50`.
- `common/decisions/016_alien_infantry_landing_decisions.txt` consumes the counted-state, audited-store, and restored-beacon readers as DHR-only landing AI modifiers.
- `common/decisions/016_dhrondan_country_decisions.txt` consumes the secured-enclave reader as an AI modifier on `dhrondan_establish_enclave_supply_bridge`.
- `docs/events/016_brilliant_scientist/systems/016_dhrondan_focus_tree.md` documents the live consumers and preserves the optional-branch contract.

## Behavior

Completing `DHR_count_the_landing_states` makes the DHR AI modestly more willing to call the existing paid landing decision.
Completing `DHR_inventory_the_expedition_stores` makes the same landing decision more attractive after its stockpile and logistics audit.
Completing `DHR_restore_the_landing_beacons` makes the landing decision more attractive after beacon restoration.
Completing `DHR_secure_the_scattered_enclaves` increases the AI priority of the existing state-targeted enclave-supply bridge when the enclave crisis is active.
These modifiers stack with the existing network, reserve-priority, guarded-descent, near-space, component, orbital-office, and laboratory-route factors.
They never grant equipment, bypass the two-thousand-gun reservation, create formations, or change human-manpower rules.

## Validation and remaining review

Source references are complete and the constants are scoped to their existing decision families.
The current DHR focus MCP inspect/render evidence remains valid because the focus graph itself is unchanged.
The weighted MCP post-patch inspect/compare is delegated to the current probability auditor with the same named landing/enclave scenarios; any unresolved typed state, receipt, equipment, or target inputs must remain explicitly recorded rather than inferred.
Live in-game AI behavior remains user-owned acceptance.
