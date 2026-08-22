# Famine and Migration System Completion Report

Date: 2026-08-22.

Verdict: incomplete. The shared core, decision surface, assets, localisation, historical profiles, and exactly two dedicated mapmodes are implemented in source, but completion cannot be claimed while the blockers below remain.

## Implemented source

The food-security score is `clamp(((1.15*production) + (1.10*transport) + (1.25*extraction) + (1.00*need) + (0.80*environment) + (0.90*vulnerability) + (0.95*governance) - (1.20*relief)) / 7.15, 0, 200)`. Stage entry thresholds are 25, 50, 75, and 100 for supply strain, acute shortage, famine, and catastrophic famine. Recovery uses 20, 40, 60, and 80 with longer hysteresis durations. Trapped-population need is normalized against live state population before it enters need and vulnerability.

Unmanaged severe famine derives each pulse from `state_population_k * constant:chaos_meter_deaths.people_per_k`, protects a dynamic population floor, and applies one exact state-population loss through `apply_exact_state_civilian_population_loss`. Famine deaths are recorded as `From famine`; supported forced-movement route deaths are recorded as `From forced displacement`. Movement itself is never registered as death.

The exact transfer contract measures actual origin debit and actual destination credit. Route deaths are included in origin debit but excluded from destination credit. If the destination credits fewer survivors than were removed, `famine_migration_restore_origin_population_residual` restores the residual to the origin and reconciles incidental manpower. A transfer succeeds only when `actual_origin_debit = route_deaths + survivor_credit`, the residual is zero, and the debit is positive. Nine decision consumers use this contract. The persistent aligned cohort ledger retains original state, current host, owner, amount, cause, and status; safe third-country resettlement rebinds an existing received row without another population transaction.

Implemented movement and durable-outcome surfaces cover internal displacement, cross-border flight, organized evacuation, deportation/forced movement, transit, trapped populations, reception, distribution, integration, third-country resettlement, voluntary return, and forced return. Closed-border choices create trapped-population, food, humanitarian, security, political, diplomatic, and mortality pressure rather than silently stopping movement.

The blockade predicate requires all accepted facts at once: island context, war, isolation, maritime dependence, route or port disruption, convoy or escort shortage, inadequate local supply, and no relief corridor.

The ordinary migration category is hidden at campaign start. Sustained exposure, repeated incidents, large flight, trapped population, or reception load reveals it. Its phases are emerging, active, resolution, and dormant. Food Security is the primary value; Displacement Load and Reception Capacity are the only supporting numeric values. There is no shared full scripted GUI.

The system declares 26 weighted decisions and three missions. Ideology is a bounded AI modifier after safety and policy gates; persecution, famine, bombing, camps, occupation conduct, and contamination can override affinity.

Runtime processing is hosted by the existing global-host coordinator and iterates only five explicit sparse registries. The package adds no recurring whole-world daily, weekly, or monthly scan.

Exactly 15 historical profiles are causally gated by state, date, owner/controller, policy, route, war, food, memory, or Air Cleanliness evidence. They supply starting context and never fixed historical death totals.

Event 149 `Immigrations` has no source, replacement event ID, pool registration, or pacing weight. The catalog workbook and exported CSV mark it retired, absorbed, unavailable, and not replaced by a random event.

## Dedicated mapmodes

The implementation owns exactly two new state mapmodes:

- `famine_state_map_mode`, showing stable supply, supply strain, acute shortage, famine, and catastrophic famine.
- `migration_state_map_mode`, prioritizing trapped population, active exodus, overcrowded reception, resettlement/return, and ordinary reception.

Both have selected and deselected final DDS buttons, GFX consumers, localisation, scripted tooltip detail, centralized colors, and state-level map sources. No combined or third famine/migration mode exists.

The final map MCP render passed state geometry, coastlines, ports, supply nodes, and railways at revision `080b7a870be68fd95ec8ed8cb464c2508b35d6b41abb1ea8c43f28a32c779841`; its PNG SHA-256 is `52b108966ee8fa0c47ca7458c9be87112fed5d84a5836a4c5f9bb313cb021685`. This proves the underlying map surface, not the scripted colors or buttons. The mapmode GUI route modeled zero useful hardcoded elements or returned indistinguishable tiny payloads, so dynamic colors, tooltips, and click regions are not engine-proven.

## Adapters

Owner-local calls are wired for Air Cleanliness/fallout, camps, gulags, forced labor, genocide, chemical aftermath, Black Plague outbreak, Event 013 natural disasters, nuclear strikes, and decision-owned Condemnation paths. Shared request APIs also exist for occupation, deportation, bombing, war, peace, events, clusters, scenarios, biological warfare, and blockade context.

Still missing are authoritative owner callbacks for occupation-law amount/actor transactions, strategic bombing, war/front aftermath, peace/return corridors, Events 5/6/14/15/21/28/33/50/95, and clusters. Events 118/120/131 have no source and were not fabricated. The shared exact-death wrappers for occupation repression and forced labor have no gameplay caller.

## AI evidence

The pre-change audit proves that the famine/migration decision pool did not exist. The post audit inspected 26 candidates through the MCP-supported `mission_ai_will_do` adapter and evaluated 20 named scenarios over 520 rows, but returned 59 unresolved inputs and no proven eligible candidate because typed `FROM`, target, neighbor, and other-country fixtures were unsupported. The recorded current/current comparison had zero changes but is not a genuine baseline/post comparison.

After the final source commit, mandatory inspection produced current source hash `62b30cfcbe4843be15c75cde4b6200b823c98aafaba768c88f12181df458faf0` and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5712c1607f325cf31162964e8cb82dd3eb03738ad7633287adb8b11f96bf5759/fcc46d28fb1c766e9e9adc702d44cbb5941a3ee378d85687be77a778680e4ee5/probability-inspect-62b30cfcbe48.json`. It again redirected the empty `decision_ai_will_do` adapter to `mission_ai_will_do`. The older 20-scenario report has source hash `c874297e...`, so all 20 named scenarios remain unresolved for the current revision and AI parity/balance is not completion evidence.

## Assets, achievements, and localisation

Final assets include the category picture/icon, nine state icons, ten decision icons, four mapmode buttons, two Deaths texticons, seven report images, and eight achievement normal/grey/not-eligible triplets. DDS manifests and round-trip evidence are recorded under `docs/assets/famine_and_migration_system/`. Category, state, decision, mapmode, Deaths, and achievement assets have GFX consumers. English localisation covers the live category, 26 decisions, three missions, costs, tooltips, modifiers, historical profiles, cohorts, routes, Deaths causes, achievements, reports, and both mapmodes, with UTF-8 BOM encoding.

All eight achievement IDs, predicates, assets, and localisation exist. Real evidence producers exist for blockade wasteland, blockade self-route rejection, conservation residual, manufactured corridor crisis, predatory requisition, and supported player tag switching. Completion remains blocked because protected internment, protected forced labor, corridor attack ownership, durable annexation history, and a complete A-to-B-to-A visit-cycle detector have no authoritative producer. Medical reception also lacks a durable later outbreak/overload invalidation window.

All seven report images are final DDS and registered sprites, but no gameplay `picture` consumer exists. A report event would require an event ID, while the accepted design forbids assigning this system an event ID and also forbids a shared full GUI. This carrier conflict requires a user-approved design decision; no fake consumer was added.

## Documentation and workbook

Permanent system documentation, dynamic effect/trigger contracts, mapmode documentation, CXT extension documentation, manifests, subagent handoffs, source-of-truth map, improvement review, probability reports, and this completion report are present. The editable workbook `docs/spreadsheets/chaos_redux_events_catalog.xlsx` is aligned and its event, cluster, and scenario CSV exports were regenerated. No system event, cluster, scenario, or mapmode row was invented.

## Validation and blockers

Source validation confirmed balanced blocks on the famine/migration scripts, nine exact-transfer decision consumers, exactly two dedicated famine/migration mapmode definitions, localisation BOMs, and no package-owned recurring world scan. The decision-file MCP lint request timed out after 180 seconds without diagnostics. Event inspection remained partial on the large workspace and does not provide current-revision event render/compare proof. In-game validation remains user-owned under repository policy.

Remaining simplifications, omissions, and blockers are:

1. Missing authoritative owner adapters and exact-death callers listed above.
2. Five achievement evidence families plus the durable medical-observation window.
3. Seven final report sprites without a legal gameplay carrier.
4. All 20 named AI scenarios unresolved on the final source revision and no genuine pre/post comparison.
5. No surface-specific MCP proof for the two mapmode buttons, scripted colors, tooltips, or click regions.
6. Event MCP lint/render/compare evidence is incomplete.
7. Relief decisions model bounded relief/pressure rather than a separate persistent food-reserve stockpile; the completion auditor classified this as an unresolved accepted-design decision.

No other intentional simplification or fallback was accepted. Completion may not be claimed.
