# IW-048 UDM force crosswalk resolution — 2026-09-20

Disposition: implemented evidence-only reconciliation. No gameplay source, central admission surface, asset, workbook, or exported CSV changed.

The earlier IW-048 completion tranche treated the `industrial_security` versus `industrial_breakaway` wording as an unresolved force-contract mismatch. A direct source crosswalk shows that these identifiers belong to separate dimensions of the accepted package contract and do not require a new archetype token.

The accepted force mapping row in `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv` assigns IW-048 force profile `industrial_security` and military tradition p48.

The package planner in `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt` assigns IW-048 candidate package archetype `industrial_breakaway` while loading the UDM carrier and state 399 anchor.

The shared constants in `common/script_constants/006_independence_wave_constants_registry.txt` define `independence_wave_force_profile.industrial_security` and `independence_wave_package_archetype.industrial_breakaway` in separate enums. The shared setup effects consume the package archetype for the industrial capacity/security opening values, while the dynamic starting-force effects consume the force profile for budget, military influence, stockpile, and template behavior.

The UDM prepared-package trigger preserves the same separation: `common/scripted_triggers/006_independence_wave_udm_package_triggers.txt:145` checks the package archetype `industrial_breakaway`, while `:174-175` checks force profile `industrial_security` and military tradition p48 after the force mapping has been loaded.

This is consistent with existing industrial packages such as IW-006 and IW-010, which use the shared `industrial_breakaway` package-archetype token while independently checking their `industrial_security` force profile. No new `industrial_security` package-archetype constant, alias, or gameplay crosswalk was added.

The resolution closes only the wording/type-mapping finding from the 2026-09-19 UDM completion tranche. IW-048 remains package-local and fail-closed because identity and portrait rights, current state-399/former-host retention evidence, typed probability fixtures and same-scenario comparison, and central admission proof remain open.

No simplification, fallback identity, portrait, flag substitution, map rewrite, AI-weight change, central admission, or live-game claim was made.
