# The Ship That Will Not Dock chain proof

## Ownership

- Event namespace: `chaosx.fallout`
- Human and AI blocks: `chaosx.fallout.422` through `.428`
- Candidate id: `422`
- Transaction key: `710034`
- Route: `7134`
- Event Log history: `9139`
- Dedicated constants: `common/script_constants/fallout_consolidated_constants.txt`
- Dedicated effects: `common/scripted_effects/fallout_consolidated_effects.txt`
- Dedicated triggers: `common/scripted_triggers/fallout_consolidated_triggers.txt`
- Dedicated dynamic modifiers: `common/dynamic_modifiers/fallout_consolidated_dynamic_modifiers.txt`

## Static proof

The state trigger requires a current produced Air Winter snapshot, current-generation ownership and control, a surviving population, coastal geography, a non-damaged naval base, a valid Fallout state grade, exposure in the reviewed band, reclamation below its ceiling, and local Supply Access below its ceiling. The candidate producer stores the lowest matching state id and its non-damaged naval-base level. The country gate requires durable current-generation rows, minimum Food, Recognition, and Cohesion, and the campaign-day window.

The four human options have distinct government and resource gates. The AI route chooses deterministically from port legitimacy, quarantine cohesion, diaspora memory, and Recognition. The delayed result uses the shared Fallout scheduler receipt. The callback returns after 270 days and the cleanup block releases result and callback receipts independently.

The result records branch-specific passenger shares, state population through `add_manpower`, state and country maritime ledgers, Reclamation, Exposure, Supply Access, timed modifiers, repairable building damage, Stability, War Support, and exact Deaths-system population loss on failure. The Event Log payload uses history `9139` and shared name and detail routing.

The dedicated report package has source SHA-256 `9BA839BE7228221F50084CD819FF0EB5C3F1D1510D277593A56125DC7CBFA6CF`, processed SHA-256 `32BEC52060F18BA2492219ADDA066C77505F77D4F98A17B78E0DE2A9E89A5C4A`, and DDS SHA-256 `F92EB6040B59114383B1B4AB9EF02E946D0B0F752B7DD7BCB5ACF988B38FF032`. The DDS is 210 by 176 uncompressed BGRA with an 840-byte row pitch.

The editable event catalog row is `FALLOUT-422` in `docs/spreadsheets/chaos_redux_events_catalog.xlsx`. The export was regenerated after the workbook update. The Events CSV SHA-256 is `8FA1C3C9C00737E575287FE87E0E07A35D906446CA60013612C9ACA81A2396E9`.

## Dormant boundary

The row remains dormant and contributes zero countable blocks. Scheduler activation, host authority, save recovery, multiplayer delivery, full-screen Fallout blackout, live bilateral partner reservation, successor allocation, focus and decision consumers, and runtime Event Log delivery remain unproven. No HOI4 runtime was launched for this proof.
