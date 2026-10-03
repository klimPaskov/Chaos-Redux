# Event 31 measured casualty receipt repair

## Disposition and accepted basis

Implemented as a bounded accounting repair under the user's Event 31 implementation request and the accepted achievement and civilian-loss contracts.
This does not change the threshold, target selection, incident weights, population transaction, or Deaths logging policy.
Event 31 remains incomplete.

## Repair

`random_terror_apply_exact_state_loss` initializes both shared-helper outputs in its own caller frame before invoking `apply_exact_state_civilian_population_loss`.
The major-loss state and country receipts now require the measured `state_civilian_population_loss_applied` amount to exceed `constant:random_terror_tuning.achievement_major_loss_deaths`.
The country counter records that measured amount rather than `random_terror_civilian_death_request`.
The existing strict greater-than threshold remains 400 people.
A requested loss which is prevented by the population floor or does not occur cannot create a major-loss receipt.

Changed gameplay file: `common/scripted_effects/031_random_terror_effects.txt`, `random_terror_apply_exact_state_loss`.
No shared population helper was modified for this repair.

## Source evidence

The current shared helper at `common/scripted_effects/chaosx_dynamic_effects.txt:629-730` measures state population before and after the transaction and returns their nonnegative difference in people.
Its API at `common/scripted_effects/chaosx_dynamic_effects.md:261-300` explicitly requires caller-owned initialization of both outputs and distinguishes measured loss from requested loss.
The installed effects documentation's `set_temp_variable` section at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md:7820-7840` and the offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:435-445` supply the temporary-variable reference.
The installed source revision is SHA-256 `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF` and the offline source revision is `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4`.
The detailed sections were read during the parent implementation, rather than relying on a reference-context bundle.
Current Event 31 effects SHA-256 after this repair is `0F673544C04424C84EF7DAFADAE1A01F01B075904A5B8C7F4AE52177704972A2`.

## Meaningful checks and limits

A source-anchored boundary model holds the request at 500 people and tests measured amounts of 0, 300, 400, and 450 people.
The first three cannot produce a major-loss receipt.
The final case produces a receipt and records 450, not 500.
The helper invocation is preceded by both output declarations and both receipt consumers use the measured output.
Repository consumer search found the major-loss flags in achievement tracking and no probability or AI consumer of the changed counter or flags.
This is a source and contract test, not an observed engine population transaction or a multiplayer achievement test.

The prior parent MCP attempts for the relevant temporary-variable references timed out at 600 seconds, including a narrower installed-documentation-only retry.
The route blocker is retained in `docs/events/031_random_terror/031_random_terror_mcp_evidence.md`.
No engine validation or probability artifact is claimed for this repair.
No game was launched and no logs were requested.

## Simplifications, omissions, and blockers

No fallback or simplification was used in this bounded repair.
Full achievement scenario coverage and engine evidence remain required for Event 31 completion.
