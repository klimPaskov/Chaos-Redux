# Event 016 broader country settlement implementation handoff

Date: 2026-08-03

## Scope

The finite country settlement tranche adds authored assistant-conflict choices for `GER`, `FRA`, `ITA`, `CHI`, `POL`, and `CZE` inside the existing `chaosx.nr16.5` event. The original `ENG`, `USA`, `SOV`, and `JAP` choices remain in the same event, so the complete named surface is ten conditional options and the generic pool remains available to every host.

## Changed runtime surfaces

- `events/016_brilliant_scientist_context_events.txt` adds `.5.h_ger` through `.5.m_cze`, exact tag/context gates, AI factors, one-time resolution effects, and impossible-lecture scheduling.
- `common/scripted_effects/016_brilliant_scientist_context_effects.txt` adds six idempotent settlement resolvers and extends the mutually exclusive receipt guards.
- `common/scripted_triggers/016_brilliant_scientist_context_triggers.txt` centralizes the unresolved-receipt guard.
- `common/script_constants/016_brilliant_scientist_country_settlement_constants.txt` owns all six settlement deltas and the shared AI factors.
- `events/016_brilliant_scientist_host_reaction_events.txt` adds the six named receipt preferences and cautions to the existing `.7` and `.8` AI pools.
- `common/scripted_localisation/016_brilliant_scientist_host_flavor_scripted_localisation.txt` and `localisation/english/016_brilliant_scientist_directorate_outcomes_l_english.yml` add facility/custody clauses, option text, and direction-complete tooltips.

## Accepted vectors

The total vectors after each existing base resolver are, in Mandate, Dependence, Exposure, Project Capacity, Independent Capacity, and Grievance order:

- `GER` research board: `(+10, +20, -10, +20, -15, +20)`.
- `FRA` laboratories: `(+10, -10, +15, +5, +25, -20)`.
- `ITA` procurement compact: `(+20, +10, +15, +15, +5, -5)`.
- `CHI` technical bureau: `(+5, +25, -10, +20, -20, +15)`.
- `POL` university shelter: `(+15, 0, +10, +5, +15, 0)`.
- `CZE` research charter: `(+5, -15, +15, +15, +20, -15)`.

## Validation and boundary

Static checks found one event and one localisation key for every national option, balanced braces in all touched Clausewitz files, no unsupported `<=` or `>=` operators, no duplicate localisation keys, and a valid UTF-8 BOM on the English localisation file. The Event Inspector lint returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics; its workspace-wide helper projection was deferred by the tool. The package checksum ledger was refreshed and verifies cleanly.

No model, GUI, new event ID, evolution, project reward, country, or separate country chain was introduced. Targeted transfer/cleanup, probability, quantitative balance, and live consumer validation remain pending. The biological stockpile/delivery lifecycle is separately blocked by the native CBRN callback boundary recorded in `016_krg_biological_stockpile_delivery_reaudit_2026-08-03.md`.
