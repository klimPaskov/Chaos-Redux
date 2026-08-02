# Reviewed Archetype: Clinic or Council

Clinic or Council is a dormant ordinary Fallout consequence chain for the fictional Congo Green Basin mutant polity. It begins after The Name We Choose closes its state memory. A clinic board, ward council, and foreign witness must decide who can authorize care, publish intake rules, and answer for a refusal during the first cold rain. The altered society is fictional high-chaos content. The chain does not present mutation as ordinary radiation science or as a medical diagnosis.

The chain uses `chaosx.fallout.880` through `chaosx.fallout.886`, candidate id `880`, transaction key `710097`, route `7226`, and Event Log history `9203`. It belongs to the Fallout-owned scheduler. Fallout itself remains outside the ordinary event log and evolution system.

## Candidate boundary

The candidate is eligible from campaign day `420` through day `7200`. The country must retain the mutant-polity government archetype and Congo Green Basin country memory. The selected state must be controlled by the country, retain a current survival identity row, durable Air Winter and Supply Access rows, living population, Shelter, Adaptation, bounded Disease Pressure, and a foreign neighbor. The state must carry the closed `fallout_event_873_memory_closed` flag from The Name We Choose. The country must retain Clinic Legitimacy, Outside Medicine Pressure, Medicine, Cohesion, Recognition, and one affordable branch.

The scheduler selects the lowest eligible state id. The registry freezes owner, controller, transition generation, state winter values, Supply Access, the care ledgers, and the lowest eligible foreign witness state. Every delayed lane revalidates those receipts. A changed state, owner, controller, witness, or generation cancels the chain and authenticated cleanup releases the reserved transaction rows.

## Branches

The four branches have distinct costs and civic consequences.

- Medical Oversight spends Food `1`, Medicine `4`, and Recognition `2`. It gives the clinic board one accountable register and lowers outside pressure when the board proves its intake rule.
- Elected Council spends Scrap `2`, Power `2`, and Recognition `3`. It moves care budgets into a public ward ledger and changes how remote districts can appeal.
- Joint Rule spends Fuel `2` and Recognition `2`, then accepts a Cohesion cost of `1`. It requires paired clinic and ward seals for each care decision.
- Reject Outside Medicine spends Food `3`, Medicine `1`, Fuel `1`, and Recognition `1`. It refuses the foreign medicine office while requiring the Basin to record reasons for every care refusal.

The opening uses human event `880` and hidden AI event `881`. The result uses human event `882` and hidden AI event `883`. The callback uses human event `884` and hidden AI event `885`. Cleanup is event `886`. Result delay is `35` days and the first-season review is `240` days later.

## Effects and memory

Each result grades state Supply Access, Shelter, Adaptation, Exposure, Disease Pressure, Medicine, Cohesion, Recognition, Clinic Legitimacy, Outside Medicine Pressure, Care Coherence, Care Trust, Clinic Migration Pressure, Clinic Generation Fatigue, and Clinic Cause Memory. Success, partial, and failure outcomes change Air Winter and Supply Access, write a distinct branch memory, apply bilateral opinion, and use bounded Deaths failure effects. The callback repeats the grading with a different timing window and closes the state memory only after both delayed transactions have settled.

The chain never requests Fallout, changes the government archetype, creates a country, transfers population between states, or registers Fallout itself as an ordinary event. It remains dormant and outside release-floor credit until the scheduler activation audit opens it.

## Wiring and assets

Runtime constants live in `common/script_constants/fallout_world_end_clinic_or_council_constants.txt`. Triggers and effects live in `common/scripted_triggers/fallout_world_end_clinic_or_council_event_triggers.txt` and `common/scripted_effects/fallout_world_end_clinic_or_council_event_effects.txt`. The candidate producer is `common/scripted_effects/fallout_world_end_event_candidate_effects.txt`. Dynamic modifiers, opinion modifiers, Event Log routing, events, and localisation use the dedicated Clinic or Council names.

The dedicated generated report art and manifest live under `docs/assets/880_clinic_or_council/`. Runtime art is `gfx/event_pictures/fallout/report_event_fallout_clinic_or_council.dds` registered as `GFX_report_event_fallout_clinic_or_council`.

## Review boundary

Static source review must verify event ids, candidate constants, predecessor memory gating, branch and delayed-result coverage, Event Log key coverage, dedicated art wiring, localisation encoding, and absence of stale Name We Choose tokens. Focused event inspection may document blocking diagnostics, but no HOI4 runtime claim is made in this tranche.
