# The First Unmasked Day

The First Unmasked Day is a reviewed Fallout ordinary-event chain in `chaosx.fallout`. It opens during the soot retreat when the normal map has produced an Air Winter thaw record and the global atmosphere has fallen below the severe winter band without becoming clean. The chain remains dormant until the Fallout scheduler proves activation.

The scheduler owns candidate `471`, transaction `710041`, route `7141`, and Event Log history `9146`. Event ids `chaosx.fallout.471` through `.477` are defined in `events/fallout_world_end_events.txt` under the Fallout namespace.

The candidate selects the lowest valid owned state with current Fallout identity and resources, surviving population, thaw-eligible normal-map provenance, intact infrastructure, low supply access, high disease pressure, and a contaminated atmosphere between the spread and severe-winter thresholds. The state also needs enough adaptation and reclamation to make a measured exposure test credible. State selection uses the native state id as a deterministic tie break.

The opening offers four government-aware policies.

- Open the schoolyard for one hour lets families test the air under a clinic watch.
- Require masked work shifts restores production while children remain sheltered.
- Let the clinic test daylight makes independent dawn readings the basis of the first opening.
- Keep the shelter sealed until clear protects the youngest shelters while preserving a trusted record.

The chain freezes public exposure, mask stock, clinic confidence, shelter memory, child memory, Food, Medicine, Recognition, and Cohesion before a 35-day result. Result success and partial lanes update Air Winter adaptation, reclamation, exposure, water security, disease pressure, supply access, infrastructure, manpower, stability, war support, and the five exposure ledgers. Failure damages rail when present or infrastructure otherwise and applies Deaths-system civilian loss through the exact state population contract.

The 365-day callback revisits the same exposure memory. It uses the same deterministic result for human and hidden AI lanes, records an Event Log payload, and releases the shared scheduler transaction through authenticated cleanup. Every branch has distinct outcome text, state modifiers, and delayed consequences. Durable branch and exposure-failure state flags preserve the public memory after the transaction is released.

The dedicated report asset is registered as `GFX_report_event_fallout_first_unmasked_day` in `interface/fallout_world_end.gfx` and lives at `gfx/event_pictures/fallout/report_event_fallout_first_unmasked_day.dds`.

Global contamination remains a gate and is not silently reduced by this event. The atmosphere must cross the existing spread threshold and remain below the existing severe-winter threshold before the chain can open.

Native scheduler delivery, host authority, save recovery, multiplayer delivery, full-screen Fallout blackout, runtime Event Log delivery, and native population relocation remain engine-surface boundaries. The chain does not claim those surfaces.
