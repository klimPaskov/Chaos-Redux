# Fallout Second Dust Bowl Proof

Status: dormant reviewed tranche with source surfaces present, static opening and result repairs applied, and completion blockers in stale cleanup and runtime acceptance.

## Identity

- Candidate: `656`
- Human opening: `chaosx.fallout.656`
- Hidden AI opening: `chaosx.fallout.657`
- Human result: `chaosx.fallout.658`
- Hidden AI result: `chaosx.fallout.659`
- Human callback: `chaosx.fallout.660`
- Hidden AI callback: `chaosx.fallout.661`
- Cleanup: `chaosx.fallout.662`
- Opening transaction: `710065`
- Callback transaction: `710165`
- Scheduler route: `7165`
- Event Log history: `9171`
- Namespace: `chaosx.fallout`
- Region: `fallout_region.north_america`

The tranche has dedicated constants, triggers, effects, dynamic modifiers, localisation, report art, sprite registration, candidate producer row, events, Event Log routing, and a reviewed source specification. It does not reuse zombie ids, files, assets, audio, sprites, or paths. The producer stores the selected state in the dispatch envelope, and the opening gate rehydrates and rechecks that issued target. Static acceptance now covers the ordinary opening path, but runtime dispatch remains unproven.

## Engine-sensitive surfaces

The candidate requires a current produced Air Winter snapshot, a native `plains` terrain state, a rural, pastoral, or town pretransition category, current ownership and control, population of at least `3000`, infrastructure above zero, Supply Access from `10` through `100`, Food from `5` through `40`, Adaptation from `8` through `55`, Reclamation below `65`, Exposure from `20` through `75`, and Disease Pressure below `65`. The country gate requires North America, campaign days `365` through `1599`, country Food `14`, Clean Water `10`, Scrap `10`, Fuel `8`, Power `6`, Shelter Capacity `12`, Recognition `6`, and Cohesion `20`.

The delayed scheduler uses the approved Fallout wrappers for ordinary receipt consumption, fixed transaction keys, result and callback tickets, hidden AI dispatch, human-visible dispatch, cleanup dispatch, and token-authenticated release. The callback uses the same current country row, target state identity, state category, owner, controller, generation, and branch receipt. The dedicated registry also checks the paid-cost flag and frozen owner and controller values before delayed effects.

The Deaths surface is `apply_exact_state_civilian_population_loss` through the authenticated target state. Result failure requests `0.0014` of the current state population. Callback failure requests `0.0006`. Each request supplies the owner country, Fallout aftermath reason, minimum remaining population, and Deaths logging inputs. No result or callback adds Air Contamination, writes the natural-disaster reservoir, changes state category, or transfers population.

## Frozen receipt matrix

| Receipt | Frozen or authenticated surfaces |
| --- | --- |
| Opening | Candidate, owner, route, opening transaction, generation, target state id, terrain, category, branch, mode, event token, country survival resources, Cohesion, Stability, War Support, state Food, Supply Access, Adaptation, Reclamation, Exposure, Disease Pressure, infrastructure, population, and seven durable ledgers |
| Result | Issued result ticket, result outcome, branch, result generation, result cleanup ticket, payment flag, chain commitment, human or AI token, and delayed queue mode |
| Callback | Issued callback ticket, branch, callback transaction, callback mode, result commitment, callback outcome, callback cleanup ticket, and callback schedule receipt |
| Cleanup | Hidden cleanup token, candidate, route, opening transaction, target state, payment receipt, result commitment or schedule-error receipt, and matching result or callback cleanup ticket |

The registry reauthenticates the target state against the frozen category, current produced snapshot, live Air Winter values, owner, controller, and plains terrain before result or callback effects. The shared delayed dispatcher still requires current generation for terminal cleanup, and result or callback delivery still requires current target identity. The dedicated cleanup gate now uses only the generic country registry after a committed result or callback, so same-generation ownership, control, category, or terrain drift can release an already-scheduled cleanup row. Pre-result stale cancellation, generation drift, and save-recovery acceptance remain unproven.

## Branch and grading evidence

The four human branches are Shelter the Fields, Move the Farms, Seed Cold Crops, and Abandon the Open Plains. Costs are sourced from `fallout_event_656_cost` and paid only after the authenticated opening receipt passes. The visible costs are Scrap `4`, Fuel `2`, Shelter Capacity `2` for Shelter the Fields, Fuel `4`, Food `2`, Shelter Capacity `3` for Move the Farms, Food `4`, Scrap `2`, Power `2` for Seed Cold Crops, and Fuel `3`, Shelter Capacity `4`, Medicine `2` for Abandon the Open Plains.

The result grade combines frozen country resources, state Food, Supply Access, Adaptation, Reclamation, infrastructure, inverse Exposure, inverse Disease Pressure, Dust Load, and all seven durable branch ledgers. A small branch-preparation delta is applied to the frozen ledgers before grade calculation, while the settled outcome applies its durable ledger delta after resolution. Success and partial thresholds are `60` and `40` for Shelter the Fields, `62` and `42` for Move the Farms, `64` and `44` for Seed Cold Crops, and `58` and `38` for Abandon the Open Plains. The delayed planting callback uses current state values, current infrastructure, all seven durable ledgers, and thresholds `63` and `41`.

Result and callback effects apply distinct Topsoil Retention, Windbreak Coverage, Farm Mobility, Cold-Crop Adoption, Displacement Pressure, Rural Trust, Dust Load, Food, Supply Access, Adaptation, Reclamation, Exposure, Disease Pressure, infrastructure, Cohesion, Stability, War Support, and timed branch modifiers. Abandon success reduces Food output while raising Shelter Capacity. Result failure and callback failure use their separate low Deaths rates. No branch uses a political-power store, harmless failure, reward loop, or variable-only population loss.

The AI lane applies archetype rules. Continuity, Bunker, and Scavenger prefer Shelter the Fields when affordable. Food Compact, Technate, and Machine Protocol prefer Seed Cold Crops when Food and Power are strong. Nomad Convoy and Maritime Remnant prefer Move the Farms. Warlord Command prefers Move the Farms during war and Shelter the Fields otherwise. Quarantine State, Religious Refuge, and Mutant Polity prefer Abandon the Open Plains under high Exposure or Disease Pressure. The deterministic tie order is Shelter the Fields, Seed Cold Crops, Move the Farms, and Abandon the Open Plains. Invalid or unaffordable choices receive priority `-1000`.

## Event Log and asset evidence

History `9171` is recorded as `event_system_event_type.fallout_country_memory` with the country as primary actor and the authenticated state as secondary actor. The dedicated scripted localisation maps four opening-choice payloads, twelve branch outcome payloads, three callback payloads, and authenticated cancellation. Central detail and history-name routers point to `fallout.event_log.second_dust_bowl`.

The report package is `docs/assets/656_second_dust_bowl/`.

The authoritative workbook is `docs/spreadsheets/chaos_redux_events_catalog.xlsx`. Exported row `FALLOUT-656` is present at `docs/spreadsheets/chaos_redux_events_catalog.csv:613` with `Needs Testing` status. The export covers the four branch choices, twelve result outcomes, three callback outcomes, authenticated cancellation, and visible budget cost `3`. The wording pass removed internal state-variable references and matches the current player-facing terms.

- Source SHA-256: `a7b4542648af14b3d4dd9c766819397e6f4030b8a14e2993ec1e3952d205287b`
- Processed PNG SHA-256: `cd5738165e2d1bed925117a8c28079d7233ce857945ee62a50e4738127d54526`
- Runtime DDS SHA-256: `2c8e2044a94ff07de7dd95d7d23d5375d2dfeeae6cc96b3263150f41c78a352d`
- Runtime DDS geometry: `210` by `176`, `147968` bytes
- Runtime sprite: `GFX_report_event_fallout_second_dust_bowl`
- Runtime path: `gfx/event_pictures/fallout_world_end/report_event_fallout_second_dust_bowl.dds`

The asset depicts a fictional cold North American plains settlement with blowing soil, improvised windbreaks, covered seed rows, trucks, and farm families beneath an ash-darkened sky. No real person, flag, readable brand, zombie asset, animation, or audio is used.

## Completion audit reconciliation

The 2026-07-27 completion audit found that this proof must remain a blocked static record rather than a completion claim.

- Candidate selection now carries the issued state target into the opening gate, which rechecks the live state rather than relying on the cleared producer scratch variable.
- Result state deltas and timed state-modifier duration now use unscoped temporary variables inside the state block.
- Result and callback delivery require current generation and mutable owner, controller, category, and terrain gates. Cleanup after a committed result or callback uses the generic country registry so same-generation target drift can release its already-scheduled row. Pre-result stale cancellation and generation drift remain open.
- Callback grading now includes infrastructure and all seven durable ledgers. The result grade also includes all seven ledgers, with a branch-preparation delta applied to the frozen score before the result is locked and the settled outcome delta applied afterward.
- High Exposure or Disease AI preference now enters the issued target state scope before reading live pressure. The hidden-AI lane scores every affordable branch, adds the authored archetype and pressure factors, selects the highest score in the documented tie order, and records the selected score in the priority ledger. The invalid-option `-1000` value remains the score floor for unaffordable branches.
- Eighteen dedicated dynamic modifiers now have localisation keys, and opening tooltips name the issued target state and result timing.
- The visible budget is `3` in the source constant, accepted spec, workbook, and export. A focused search found no stale visible-budget value of `2` in the Second Dust Bowl source surfaces.

These findings supersede generic wording that could be read as proof of runtime candidate delivery or stale cleanup. Event Log selector coverage is static and complete after the parent cancellation patch, but runtime reachability remains blocked.

## Static audit scenarios

| Scenario | Expected result |
| --- | --- |
| Candidate state becomes non-plains before opening | The issued opening gate fails its live plains recheck and no opening effects apply. |
| Candidate state category changes before result | Registry reauthentication fails and no result effects apply. |
| Generation changes before opening receipt consumption | Ordinary receipt fails and no paid branch remains. |
| Duplicate result delivery | Issued delayed ticket, branch, token, target, and registry checks block a second settlement. |
| Callback delivery to the human lane from an AI token | Mode and token checks block the event. |
| Callback delivery after result commitment is absent | Callback trigger fails. |
| Callback scheduling failure after committed result | Result cleanup keeps its own commitment and does not refund a settled result. |
| Stale cleanup after a generation, ownership, control, category, or terrain change | Same-generation drift after a committed result or callback has a generic-country cleanup route. Pre-result drift and generation changes remain blocked and have no runtime acceptance. |
| Duplicate cleanup delivery | No matching cleanup row remains after the first release. |
| Result failure | The Deaths contract requests `0.0014` of the authenticated state population. |
| Callback failure | The Deaths contract requests `0.0006` of the authenticated state population. |
| Manual scenario population sweep | The separate Fallout manual scenario still records the exact engine-native sweep blocker and the approved 90 to 95 percent population-loss contract. |

## Validation boundary

The candidate producer, event chain, Event Log, localisation, constants, dynamic modifiers, documentation, and asset wiring have been reviewed statically. Dedicated scripts have balanced braces and no em dashes, semicolons, or unsupported comparison operators. The localisation file is UTF 8 with BOM. No HOI4 process was launched. Live candidate delivery, save recovery, multiplayer host authority, normal-map presentation, terrain trigger acceptance, stale cleanup, and exact all-valid-province thermonuclear sweep remain runtime boundaries. The Fallout release-floor count does not claim this dormant tranche until activation review and user validation pass.

## Read-only event-inspector evidence

A read-only `hoi4_event_inspect` query for selector `{kind:event,eventId:chaosx.fallout.656}` with `expandHelpers=false`, depth `1`, max nodes `20`, max edges `40`, and refresh enabled returned workspace-wide partial diagnostics rather than a validation pass. The response reported `validation.passed=false` and `MCP_INLINE_FILES_TRUNCATED`. This is unresolved tooling evidence and is not runtime acceptance.

A later refreshed lint request for the same event with helper expansion and a bounded graph closed the MCP transport before returning a result. This is an additional tooling boundary and does not establish parser, dispatch, terrain, cleanup, or runtime acceptance.
