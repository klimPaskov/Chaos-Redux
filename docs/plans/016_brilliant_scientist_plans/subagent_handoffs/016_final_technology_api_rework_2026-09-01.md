# Event 016 Final Technology and API Rework Handoff

Date: 2026-09-01

Status: Reviewed source implementation complete for closure tranche 2; MCP post-change comparison remains blocked by the exact transport failure recorded below.

## Implemented surface

- Raised the conventional Theory, Prototype, Deployment, and Weaponization ladder to the accepted wonder-weapon scale through shared Event 016 constants and dynamic modifiers.
- Computation Deployment grants one idempotent research slot, and its disable, transfer, suspension, dismantling, and inheritance boundaries remove or restore that slot through the canonical project-family dispatcher.
- Added paid Predictive Campaign, Sensor Saturation, State Synthesis Works, High-Speed Strike, Long-Range Delivery Strike, Field Projector, Emergency Regeneration, and Epidemic Control decisions.
- Decision selection commits the exact equipment, fuel, manpower, and Command Power transaction; timer removal applies the outcome; invalidation runs the matching one-time refund. Factory time already consumed by a cancelled preparation is not restored.
- Healthy Biomedical Deployment and Weaponization contribute fifty response points each to the shared biological surveillance, containment, medical, and biosecurity calculation before its existing zero-to-one-hundred clamp.
- Raised the seven hidden operational technologies, seven weaponization technologies, and four mutually exclusive xenobiological control technologies to their accepted combat identities while preserving base Clone Infantry as the deliberate weaker exception.
- Added public technology query and reconciliation triggers, dependency-safe upgrades, deterministic xenobiological control repair, idempotent runtime rebuilding, and permanent encoded provenance receipts.
- The external alien-recovery bridge uses Event 016-owned recovery constants and therefore has no Event 025 constant-namespace or load-order dependency.
- Removed the simultaneous Kruger-versus-Mengele D’Rhondan expedition competition by making the Mengele route ineligible while Kruger is the current program owner.
- Migrated the paleogenetic, xenobiological, and temporal sub-unit and equipment identifiers to generic public identifiers across gameplay, Event 019, CXT, localisation, enums, tokens, documentation, and model handoffs.

## Public API contract

The preserved public effects are `chaosx_grant_custom_operational_technology`, `chaosx_grant_custom_technology_upgrade`, `chaosx_grant_random_custom_operational_technology`, and `chaosx_grant_custom_operational_technology_core`.

The new read-only queries cover selector validity, idempotent grant safety, strict upgrade eligibility, unowned operational families, and occupied xenobiological control channels. `chaosx_reconcile_custom_technology_runtime` restores the matching generic equipment, sub-unit, template, cap, and Event 019 consumers without creating Kruger project history, Directorate variables, facilities, incidents, or achievements.

Operational provenance is encoded in `chaosx_custom_technology_operational_provenance`; upgrade provenance is encoded in `chaosx_custom_technology_upgrade_provenance`. Each receipt stores `selector * 1000000 + source`, and array membership makes repeated grants from the same source idempotent. Learned technology is permanent when an external source later disappears.

## Meaningful validation

- A repository-wide exact-token scan found zero retired Kruger-specific generic-unit identifiers.
- All new action constant categories resolve, action and API braces balance, localisation retains UTF-8 BOM, and all reused decision sprites resolve to registered Event 016 project icons.
- The pre-change probability audit proved equal operational-family weights under all-unowned, single-eligible, and one-owned scenarios. It also recorded the prior D’Rhondan Kruger-first competition that this tranche removes.
- The bounded pre-change and migration technology inspections are linked from `016_final_technology_probability_baseline_2026-09-01.md` and `016_final_generic_unit_identifier_migration_2026-09-01.md`.

## MCP blocker

A fresh post-change `hoi4.tech_inspect` for `brilliant_scientist_clone_formations_tech` returned exactly `tool call failed for hoi4_agent_tools/hoi4.tech_inspect: Transport closed`. The same transport failure blocks the required post-change technology render/compare and technology-action probability evaluation. Source review is not presented as equivalent MCP evidence; the comparison must be rerun when the production server is available.

## Remaining ownership

- Unit/equipment production, manpower farming, trainability, capitulation conservation, and Event 019 formation behavior belong to closure tranche 3.
- Portal, biological deployment, and Alien landing transactions belong to closure tranche 4.
- The conventional action AI weights and D’Rhondan expedition eligibility require exact baseline/post-change probability comparison when MCP transport recovers.
