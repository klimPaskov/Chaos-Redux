# Decision and mission prompt for Air Cleanliness and Fallout

Canonical status: accepted baseline prompt, subject to the corrected ownership and living-world source specs in this package.

Use `chaos-redux-decisions-missions` before implementation. This prompt covers state-targeted air cleanup and post-Fallout survival decisions.

Decision systems to implement from the spec:

1. Air Cleanliness state response decisions for mask drives, clinic expansion, ash clearing, rail protection, greenhouse conversion, shelter agriculture, evacuation, and treaty operations.
2. Air mapmode selected-state actions tied to winter phase and fallout exposure.
3. Pre-Fallout seasonal missions for seed vaults, ports, waterworks, rail spines, reactor cooling, and shelter capacity.
4. Post-Fallout Survival Ledger with resources: Food, Clean Water, Medicine, Scrap, Fuel, Power, Filters, Shelter Capacity, Recognition.
5. State Recovery category for reconstruction, decontamination, category restoration, and abandonment.
6. Salvage Expedition category for dead cities, reactor keeps, depots, battlefields, and forbidden zones.
7. Refugee and Population category for admission, screening, recruitment, settlement, and expulsion.
8. Mutant Policy category for quarantine, citizenship, weaponization, truce, purge, and worship routes.
9. Diplomacy and Recognition category for radio contact, compact formation, convoy routes, aid, trade, and war claims.
10. Late Ambition category for archetype capstones and formables.

Costs must use equipment, manpower, trains, convoys, fuel, support equipment, trucks, medicine variables, filters, food, water, shelter capacity, stability, war support, units in states, route control, and time. Do not make the system a political power store.

Large categories need clutter control. Show only selected states or active priorities. AI must have equivalent actions without relying on human-only selection clicks.

After implementation, run `chaosx_decision_mission_auditor` and patch local cost, tooltip, AI, cleanup, or exploit issues.
