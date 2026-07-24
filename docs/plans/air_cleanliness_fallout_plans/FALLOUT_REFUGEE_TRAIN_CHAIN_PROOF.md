# Fallout Refugee Train chain proof

## Ownership and identifiers

- Namespace: `chaosx.fallout`
- Opening, AI, result, result AI, callback, callback AI, and cleanup: `415` through `421`
- Candidate: `415`
- Transaction key: `710033`
- Route: `7133`
- Event Log history: `9138`
- The chain uses Fallout-owned files, identifiers, localisation, and report art. No zombie file, id, sprite, audio path, or asset is referenced.

## Authored mechanics

The producer selects the lowest owned native rail state with a current Air Winter snapshot, surviving population, and current-generation Fallout rows. The country gate carries recognition pressure, food, cohesion, campaign-day limits, and a current owner check. Four policies admit families, redirect the column, quarantine the train, or recruit specialists. The delayed result freezes survival and migration ledgers, applies branch-specific outcomes and state effects, records arrival cohorts, and routes failure population loss through `apply_exact_state_civilian_population_loss`. The callback runs after 365 days, updates family memory, border legitimacy, integration cohesion, bilateral trust, state supply, exposure, and reclamation, then releases authenticated cleanup receipts. Human and hidden AI lanes share the same scheduler helpers.

## Static checks

- `events/fallout_world_end_events.txt` contains one definition for each id `415` through `421`.
- The new constants, triggers, effects, scripted localisation, and dynamic modifiers are brace-balanced and contain no unsupported comparison operators.
- The new English localisation is UTF-8 with BOM. Its event, tooltip, result, callback, Event Log name, and Event Log detail keys are present.
- The GFX container is brace-balanced and registers `GFX_report_event_fallout_refugee_train` to the dedicated DDS path.
- Source SHA-256: `D310E71C5CCDAC9EFCD8B79515D6C262A671441EB432284F6457C6A81484505E`
- Processed PNG SHA-256: `9C406524F26395332538CB1FA3935554CEE7077453ABD62AF3D1130EE1DC5841`
- DDS SHA-256: `689E1D7A27AB65A3726B441A6D061DAD959E6706CB33B4FA7651ED763015D9D2`
- DDS header: 210 by 176, pitch 840, uncompressed BGRA payload, 147968 bytes.
- Workbook row `FALLOUT-415` was written to `docs/spreadsheets/chaos_redux_events_catalog.xlsx` and exported with `.tools/export_event_catalog_csv.py`. The workbook and exports remain unstaged because they contain unrelated user edits.

## Runtime boundary

No HOI4 runtime was launched, per the user instruction. The candidate remains dormant and contributes zero countable release-floor blocks until scheduler activation proves host authority, save recovery, multiplayer delivery, full-screen blackout ownership, and runtime Event Log delivery.
