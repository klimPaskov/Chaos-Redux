# Reviewed Archetype: Mixed Settlement Petition

Mixed Settlement Petition is the first-year residence chain for the fictional Congo Green Basin mutant polity. It follows Clinic or Council after that chain closes its state memory. River households and altered survivors ask to share a pump road, while district clerks and a foreign witness disagree over whether common ground is a right, a boundary, a supervised promise, or a line that cannot be crossed. The altered society is fictional high-chaos content. The chain does not present mutation as ordinary radiation science or as a medical diagnosis.

The chain uses `chaosx.fallout.887` through `chaosx.fallout.893`, candidate id `887`, transaction key `710098`, route `7228`, and Event Log history `9204`. It belongs to the Fallout-owned scheduler. Fallout itself remains outside the ordinary event log and evolution system.

## Candidate boundary

The candidate is eligible from campaign day `720` through day `9000`. The country must retain the mutant-polity government archetype and Congo Green Basin country memory. The selected state must be controlled by the country, retain a current survival identity row, durable Air Winter and Supply Access rows, living population, Shelter, Adaptation, bounded Disease Pressure, and a foreign neighbor. The state must carry the closed `fallout_event_880_memory_closed` flag from Clinic or Council. The country must retain Settlement Legitimacy, Settlement Boundary Pressure, Medicine, Cohesion, Recognition, and one affordable branch.

The scheduler selects the lowest eligible state id. The registry freezes owner, controller, transition generation, state winter values, Supply Access, the settlement ledgers, and the lowest eligible foreign witness state. Every delayed lane revalidates those receipts. A changed state, owner, controller, witness, or generation cancels the chain and authenticated cleanup releases the reserved transaction rows.

## Branches

The four branches have distinct costs and civic consequences.

- Equal Citizenship spends Food `2`, Medicine `2`, and Recognition `3`. It extends the Basin charter to every resident and publishes one shared district register.
- Separate Districts spends Scrap `3`, Power `1`, and Recognition `2`. It protects separate assemblies while building a narrow corridor for water and winter supplies.
- Supervised Integration spends Fuel `2` and Recognition `2`, then accepts a Cohesion cost of `2`. It appoints paired stewards for every mixed settlement road.
- Refuse Settlement spends Food `3`, Medicine `2`, Fuel `1`, and Recognition `1`. It refuses permanent shared districts while issuing a recorded transit rule.

The opening uses human event `887` and hidden AI event `888`. The result uses human event `889` and hidden AI event `890`. The callback uses human event `891` and hidden AI event `892`. Cleanup is event `893`. Result delay is `42` days and the first-year review is `300` days later.

## Effects and memory

Each result grades state Supply Access, Shelter, Adaptation, Exposure, Disease Pressure, Medicine, Cohesion, Recognition, Settlement Legitimacy, Settlement Boundary Pressure, Settlement Cohesion, Settlement Trust, Settlement Migration Pressure, Settlement Generation Fatigue, and Settlement Cause Memory. Success, partial, and failure outcomes change Air Winter and Supply Access, write a distinct branch memory, apply bilateral opinion, and use bounded Deaths failure effects. The callback repeats the grading with a different timing window and closes the state memory only after both delayed transactions have settled.

The chain never requests Fallout, changes the government archetype, creates a country, transfers population between states, or registers Fallout itself as an ordinary event. It remains dormant and outside release-floor credit until the scheduler activation audit opens it.

## Wiring and assets

Runtime constants live in `common/script_constants/fallout_consolidated_constants.txt`. Triggers and effects live in `common/scripted_triggers/fallout_consolidated_triggers.txt` and `common/scripted_effects/fallout_consolidated_effects.txt`. The candidate producer is `common/scripted_effects/fallout_consolidated_effects.txt`. Dynamic modifiers, opinion modifiers, Event Log routing, events, and localisation use the dedicated Mixed Settlement names.

The dedicated generated report art and manifest live under `docs/assets/887_mixed_settlement/`. Runtime art is `gfx/event_pictures/fallout/report_event_fallout_mixed_settlement.dds` registered as `GFX_report_event_fallout_mixed_settlement`.

## Review boundary

Static source review must verify event ids, candidate constants, predecessor memory gating, branch and delayed-result coverage, Event Log key coverage, dedicated art wiring, localisation encoding, and absence of stale Clinic or Council tokens. Focused event inspection may document blocking diagnostics, but no HOI4 runtime claim is made in this tranche.
