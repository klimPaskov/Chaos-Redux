# Fallout New Year Without Fireworks Proof

Status: dormant reviewed tranche with static wiring complete and live validation pending.

## Identity

- Candidate: `649`
- Human opening: `chaosx.fallout.649`
- Hidden AI opening: `chaosx.fallout.650`
- Human result: `chaosx.fallout.651`
- Hidden AI result: `chaosx.fallout.652`
- Human callback: `chaosx.fallout.653`
- Hidden AI callback: `chaosx.fallout.654`
- Cleanup: `chaosx.fallout.655`
- Opening transaction: `710064`
- Callback transaction: `710164`
- Scheduler route: `7164`
- Event Log history: `9170`
- Namespace: `chaosx.fallout`

The tranche has dedicated constants, triggers, effects, dynamic modifiers, localisation, report art, sprite registration, candidate producer row, events, Event Log routing, workbook row, and exported catalogue CSV. It does not reuse zombie ids, files, assets, audio, sprites, or paths.

## Engine-sensitive surfaces

The candidate is country-only. The producer appends target type `none` and target `0`, so it does not fabricate a state or province target. The admission trigger reuses the current Fallout identity row, durable survival row, exact East Asia region, campaign window, resource floors, Cohesion floor, and branch affordability.

The delayed scheduler uses the approved Fallout wrappers for ordinary receipt consumption, fixed transaction keys, result and callback tickets, hidden-AI dispatch, human-visible dispatch, cleanup dispatch, and token-authenticated release. The callback uses the same current country row and exact branch receipt.

The Deaths surface is `apply_exact_state_civilian_population_loss` through `every_owned_state`. Result failure requests `0.0015` of each current state population. Callback failure requests `0.0007`. Each request supplies the owner country, Fallout aftermath reason, minimum remaining population, and Deaths logging inputs.

## Frozen receipt matrix

| Receipt | Frozen or authenticated surfaces |
| --- | --- |
| Opening | Candidate, owner, route, opening transaction, generation, target none, target zero, branch, mode, event token, country survival resources, Cohesion, Stability, Exposure, Disease Pressure, and seven durable ledgers |
| Result | Issued result ticket, result outcome, branch, result generation, result cleanup ticket, payment flag, chain commitment, human or AI token, and delayed queue mode |
| Callback | Issued callback ticket, branch, callback transaction, callback mode, result commitment, callback outcome, callback cleanup ticket, and callback schedule receipt |
| Cleanup | Hidden cleanup token, candidate, route, opening transaction, branch, issued ticket, payment receipt, result commitment or schedule-error receipt, and matching result or callback cleanup ticket |

Cleanup deliberately does not require current generation, ownership, or region. A stale chain may release only its own delayed rows. It cannot clear a replacement transaction because the candidate, route, branch, token, ticket, and payment checks remain exact.

## Branch and grading evidence

The four human branches are Quiet Remembrance, Hold a Ration Feast, Stage a Military Ceremony, and Leave the Night to Local Festivals. Costs are sourced from `fallout_event_649_cost` and applied only after the result reservation is accepted. The result grade uses the frozen receipt and branch thresholds `58` or `38`, `62` or `42`, `63` or `43`, and `60` or `40`. The callback grade uses the current ledgers with thresholds `64` or `42`.

Result and callback effects apply distinct branch memory ledgers, Food, Clean Water, Fuel, Medicine, Shelter Capacity, Recognition, Cohesion, Stability, War Support, Disease Pressure, and timed branch modifiers. Result failure and callback failure use their separate low Deaths rates. No branch uses a political-power store, harmless failure, reward loop, or variable-only population loss.

## Event Log and asset evidence

History `9170` is recorded as `event_system_event_type.fallout_country_memory` with the country as primary actor. The dedicated scripted localisation maps all twelve branch outcome payloads and three callback payloads. The central detail and history-name routers point to `fallout.event_log.new_year_without_fireworks`.

The report package is `docs/assets/649_new_year_without_fireworks/`.

- Source SHA-256: `35de80ad3a67fa847f6a31ca782c7de18ab6c217c7c2afa2abf68d6a64f5826f`
- Processed PNG SHA-256: `8be3a5ded625b05349a87c2178dfa1a0a5645f997058b2275a6f6fbebf6a6b71`
- Runtime DDS SHA-256: `bc48046b0f5cb7a387f32e1e0317174271ff2b46697cb45640658535c4ace5b7`
- Runtime sprite: `GFX_report_event_fallout_new_year_without_fireworks`
- Runtime path: `gfx/event_pictures/fallout_world_end/report_event_fallout_new_year_without_fireworks.dds`

The asset depicts a fictional cold East Asian settlement with covered lamps, a ration table, memorial ribbons, civilians, and guards. No real person, flag, readable script, religious marker, fireworks, zombie asset, animation, or audio is used.

## Static audit scenarios

| Scenario | Expected result |
| --- | --- |
| Generation changes before opening receipt consumption | Ordinary receipt fails and no paid branch remains. |
| Duplicate result delivery | Issued delayed ticket and result token checks block a second settlement. |
| Callback delivery to the human lane from an AI token | Mode and token checks block the event. |
| Callback delivery after result commitment is absent | Callback trigger fails. |
| Callback scheduling failure after committed result | Result cleanup still releases its own row and does not refund the committed result. |
| Stale cleanup after ownership or region change | Candidate, route, branch, ticket, token, and payment checks release only the owned stale row. |
| Duplicate cleanup delivery | No matching cleanup row remains after the first release. |
| Result failure | The Deaths contract requests `0.0015` of each owned state population. |
| Callback failure | The Deaths contract requests `0.0007` of each owned state population. |
| Manual scenario population sweep | The separate Fallout manual scenario still records the exact engine-native sweep blocker and the approved 90 to 95 percent population-loss contract. |

## Validation boundary

The candidate, event, scheduler, Event Log, workbook, and asset wiring have been reviewed statically. No HOI4 process was launched. Live event delivery, save recovery, multiplayer host authority, normal-map presentation, and the exact all-valid-province thermonuclear sweep remain runtime boundaries. The Fallout release-floor count does not claim this dormant tranche until activation review and user validation pass.

## Read-only event-inspector evidence

A read-only `hoi4_event_inspect` query for selector `{kind:event,eventId:chaosx.fallout.649}` with `expandHelpers=false`, depth `1`, max nodes `20`, max edges `40`, and refresh enabled returned status `ok` with code `EVENT_INSPECTED_PARTIAL` and an artifact. The response reported workspace-wide counts of `8939` events, `22905` issues, and `6616` blocking diagnostics, with `validation.passed=false` and `MCP_INLINE_FILES_TRUNCATED` as the only listed diagnostic. This is unresolved tooling evidence and is not a validation pass or runtime acceptance.
