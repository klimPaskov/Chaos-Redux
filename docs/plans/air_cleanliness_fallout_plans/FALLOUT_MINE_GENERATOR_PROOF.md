# Fallout Mine Generator Proof

Status: dormant reviewed tranche, static implementation repaired after audit, live validation pending.

## Identity

- Opening candidate: `642`.
- Human opening: `chaosx.fallout.642`.
- Hidden AI opening: `chaosx.fallout.643`.
- Human result: `chaosx.fallout.644`.
- Hidden AI result: `chaosx.fallout.645`.
- Human callback: `chaosx.fallout.646`.
- Hidden AI callback: `chaosx.fallout.647`.
- Cleanup: `chaosx.fallout.648`.
- Transaction key: `710063`.
- Candidate route: `7163`.
- Event Log history: `9169`.
- Namespace: `chaosx.fallout`.

The identities are dedicated to the Mine Generator and do not reuse zombie ids, files, assets, audio, sprites, or paths.

## Engine-sensitive surfaces

The direct admission surface is `fallout_event_642_state_has_native_resource_work` in `common/scripted_triggers/fallout_world_end_mine_generator_event_triggers.txt`.

It is a state-scoped `has_resources_amount` OR over coal, steel, tungsten, chromium, and aluminium with the fixed display priority coal, steel, tungsten, chromium, then aluminium. Each amount comparison uses the file-scoped zero required by the engine-facing trigger syntax.

The offline `triggers_documentation.md` reference records `has_resources_amount` on STATE scope with `resource =`, `amount >`, and an optional `delivered =` operand. The repository natural-disaster precedent uses the same trigger with a file-scoped integer because script constants are not accepted in this operand.

The same direct trigger is reached through `fallout_event_642_state_is_current` for candidate admission and opening revalidation, then through `fallout_event_642_state_receipt_is_current` for result, callback, and generation-abort authentication. The receipt trigger compares the selected resource class against the currently present deposit, so a surviving steel deposit cannot satisfy a frozen coal receipt.

The chain only reads native deposits as evidence and contains no resource deposit mutation, mine building creation, generator building creation, partner state, population transfer, tag change, government change, focus route, decision category, or recurring scheduler.

The event file keeps the Fallout namespace and appends the seven Mine Generator events without changing the existing event root format.

## Numerical contract

| Surface | Implemented value |
| --- | ---: |
| Visible scheduler budget | 2 |
| Result delay | 42 days |
| Callback delay | 270 days after result settlement |
| Result grade thresholds | Trade 60 or 40, Labor 64 or 44, Engineer 62 or 42, Evacuation 58 or 38 |
| Callback thresholds | 64 or 42 |
| Result failure Deaths request | 0.15 percent of current state population with minimum remaining 100 people |
| Callback failure Deaths request | 0.07 percent of current state population with minimum remaining 100 people |
| Infrastructure failure damage | 1 level, then one industrial complex level if infrastructure cannot be damaged |

Branch affordability and payment use the exact approved costs.

- Trade Mineral Shares spends Power 3, Scrap 2, and Recognition 2.
- Conscript the Labor Shift spends Food 3, Fuel 2, and Command Power 10.
- Establish Engineer Rule spends Power 4, Scrap 3, and Recognition 2.
- Evacuate the Works spends Fuel 4, Shelter Capacity 3, and Medicine 2.

The opening freezes country values, state Air Winter values, infrastructure, population, owner, controller, resource class, branch, mode, event token, the exact transaction key, the opening receipt ticket, route, Stability, and empty result and callback ticket slots before payment. The delayed result and callback tickets are written into those frozen slots only after their queue rows are accepted.

The result ticket is allocated first, the ordinary opening receipt is then consumed, and the chain commits only after both operations succeed. Each delayed entry compares its issued ticket against both the content-owned cleanup ticket and its frozen result or callback ticket.

Failed scheduling or receipt consumption cancels the delayed row, releases its cleanup row, reverses branch ledger settlement, refunds the exact paid cost, clears the state reservation, and cancels the ordinary receipt.

## State grading and callback

Branch settlement is applied before the grade is locked. The result grade uses frozen country Food, Power, Scrap, Recognition, Cohesion, Stability, state Food, Adaptation, Supply Access, Reclamation, Exposure, Disease Pressure, infrastructure, native resource evidence, and branch ledgers.

The callback does not recalculate the original result grade.

It reads current country Food, Power, Cohesion, current state Supply Access, Food, Reclamation, Exposure, Disease Pressure, infrastructure, and the durable Mine Generator ledgers. Scrap is reserved for result and callback effects rather than callback grading.

The selected native resource class is retained as `fallout_mine_last_resource_class` after cleanup for later country-memory consumers.

## Deaths and buildings

Failure effects use `apply_exact_state_civilian_population_loss` through the existing Deaths system with explicit reason, owner country, minimum remaining population, and event logging inputs.

No direct state population assignment is used.

Failure damage targets infrastructure first and industrial complex second without touching the native deposit.

## Cleanup proof

`fallout_event_642_abort_on_generation_change` reauthenticates generation, owner, controller, current Air Winter snapshot, the selected native resource class, and the issued event token.

For an uncommitted opening whose dispatched state is no longer current, the abort route snapshots `fallout_event_dispatch_issued_target` into `fallout_event_642_target_state_id` before cancelling the ordinary receipt. Only an accepted cancellation records the Mine Generator cancellation history, reverses branch settlement, refunds the paid branch cost, clears the state reservation and committed state flag, and clears the frozen row. This keeps stale reservation release bound to the state that issued the receipt instead of whichever state happens to be inspected after reset.

The delayed cleanup gate separately authenticates the frozen transaction key, opening receipt ticket, result ticket, route, mode, branch, opening token, selected resource class, cost-paid receipt, and either the committed-chain or result-commitment receipt. It does not require current ownership, control, generation, or native-resource presence, so a stale chain can clean itself without touching a replacement transaction.

It cancels stale opening receipts, result tickets, callback tickets, and cleanup tickets only when they belong to Mine Generator identity tokens.

When a callback exists, stale cleanup prepares and releases both the callback row and the retained result row.

Unrelated issued dispatches block Mine Generator flag clearing. Outcome modifiers are split into state and country surfaces, and cleanup leaves their authored durations intact.

Cleanup is idempotent because each delayed ticket is authenticated before release and the final close requires the exact result and callback release state.

## Event Log and localisation

History `9169` records the four opening choices, branch-specific success, partial, and failure payloads, callback success, partial, and failure, and cancellation.

The country is recorded as the primary actor and the authenticated state as the secondary actor.

The event, result, callback, modifier, and Event Log localisation is in `localisation/english/fallout_world_end_mine_generator_l_english.yml` with a UTF-8 BOM.

The Event Log detail router is `GetFalloutEvent642EventLogDetail` and is connected to the central event log name and detail routers.

## Asset proof

The dedicated package is `docs/assets/642_mine_generator/`.

- Source PNG: `source_generated.png`, 1536 by 1024, SHA-256 `49EA5B72886D4B55DE552A0E1FC1B4DCCE68C7188733BF368B97AAEEDB2C36F4`.
- Processed PNG: `processed_210x176.png`, 210 by 176 RGBA, SHA-256 `F6009C921689291E952F197391F46D45F52120838BEB359EE9D7D0FA29921271`.
- Package DDS and runtime DDS: `report_event_fallout_mine_generator.dds`, 210 by 176 BGRA, SHA-256 `FA95B93840CC9003C4FF101E9C014B76486E4CC34F13940A6772F1D1AF8D1DA0`.
- Sprite: `GFX_report_event_fallout_mine_generator`.
- Runtime path: `gfx/event_pictures/fallout_world_end/report_event_fallout_mine_generator.dds`.

The art is a fictional ash-darkened Sub-Saharan mining settlement with a generator shed, ore stores, workers, guarded machinery, and sparse food stores.

## Static validation

Brace counts match for the Mine Generator constants, triggers, effects, dynamic modifiers, Event Log scripted localisation, event file, and GFX file.

The event and Event Log localisation references have no missing Mine Generator keys.

The dedicated gameplay and localisation files contain no unsupported comparison operators, em dashes, or semicolons.

The focused review matrix is recorded below. These rows are static authentication scenarios until the user validates live queue delivery.

| Scenario | Expected proof surface |
| --- | --- |
| Generation reset before choice | The ordinary receipt is cancelled and no cost is committed. |
| Generation reset after delayed result allocation but before ordinary receipt consume | The delayed row is cancelled, branch settlement is reversed, the paid cost is refunded, and the state reservation is released. |
| Ownership or control loss after result commitment | The result or callback row is cancelled through Mine Generator tokens, the result commitment flag blocks a refund, and cleanup releases only matching rows. |
| Selected coal deposit loss while steel survives | `fallout_event_642_state_resource_class_is_current` fails the receipt, so the result or callback cannot enter. |
| Duplicate result delivery | The issued result ticket must equal both the frozen result ticket and result cleanup ticket. A repeated row cannot apply effects twice. |
| Duplicate callback delivery | The issued callback ticket must equal both the frozen callback ticket and callback cleanup ticket, and the result commitment receipt must exist. A repeated row cannot apply effects twice. |
| Receipt consume failure | Delayed scheduling is cancelled, settlement is reversed, the exact cost is refunded, and the ordinary receipt is cancelled. |
| Committed result with callback scheduling failure | The result commitment remains durable, cleanup is prepared, and the branch cost is not refunded. |
| Duplicate cleanup delivery | The cleanup ticket is released once. A second cleanup token has no matching live cleanup ticket and cannot clear a newer transaction. |
| Replacement transaction after target loss | The frozen transaction key, route, branch, mode, opening token, cost receipt, and commitment receipt prevent a replacement transaction from inheriting the chain. |
| Replacement state after target loss | The authenticated state id, owner, controller, generation, and selected resource class prevent a replacement state from inheriting the chain. |

## Runtime boundary

Live scheduler dispatch, delayed queue delivery, invalid target behavior, Event Log rendering, save recovery, multiplayer delivery, host authority, and player-visible art remain unobserved until user validation in HOI4.

No HOI4 process was launched for this tranche.

The Mine Generator remains dormant and contributes no release-floor event-block credit until its activation review and runtime validation pass.
