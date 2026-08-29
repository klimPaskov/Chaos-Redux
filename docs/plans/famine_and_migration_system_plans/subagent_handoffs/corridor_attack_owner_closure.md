# Famine and Migration Corridor Attack Owner Closure

> **Superseded historical identifier banner (2026-08-25):** Any `fm_*` or `famine_migration_*` identifier quoted in this historical handoff is source-snapshot terminology only and is superseded; current authorities use separate `famine_*`, `migration_*`, or narrow neutral `civilian_transfer_*`/`humanitarian_*` names; see [source_of_truth_map.md](../source_of_truth_map.md).

## Status

This handoff records the bounded owner-callsite closure for the three existing project-owned border-war resolvers requested by the parent agent.

No event files, shared on-actions, mapmodes, GUI surfaces, population/death effects, AI weights, or central routers were changed.

The shared receipt entry point remains `famine_migration_corridor_handle_exact_state_attack` in `common/scripted_effects/famine_migration_corridor_effects.txt`.

## Helper map

| Owner resolver and scope | Exact proof guard | Attacker and target inputs | Receipt semantics and side effects |
| --- | --- | --- | --- |
| `infantry_spawn_achievement_resolve_combat_trial_attacker_win` and `infantry_spawn_achievement_resolve_combat_trial_attacker_loss` in country scope | The attacker callback has the active and started trial flags, and `infantry_spawn_achievement_combat_trial_frozen_pair_is_intact` validates the stored attacker state, defender state, defender country, division identity, trial type, and nonce-linked opponent marker. | The current callback country is saved as `famine_migration_corridor_exact_attacker`; `var:infantry_spawn_achievement_combat_trial_defender_state` is the exact attacked state. | The receipt is submitted before Event 019 cleanup and only for win/loss callbacks. The cancel resolver is unchanged because cancellation does not prove hostilities. |
| `resources_found_clear_border_conflict_runtime` in country scope | `resources_found_border_callback_is_owner_context` validates the current owner country, owner state, claimant state, and claimant country. An owner-victory state flag is additionally required so the same cleanup effect cannot convert the cancellation path into an attack receipt. | The current owner callback country is saved as `famine_migration_corridor_exact_attacker`; `var:resources_found_border_claimant_state` is the exact attacked state. | The receipt is submitted before the owner-victory cleanup clears the pair variables. The three Event 018 owner-victory option flags are accepted; the cancel and stale mission cleanup paths remain inert. |
| `resources_found_record_border_transfer_result` in country scope | `resources_found_border_callback_is_owner_context` validates the exact owner-side callback pair immediately before the claimant-victory transfer. | The current owner callback country is saved as `famine_migration_corridor_exact_attacker`; `var:resources_found_border_claimant_state` is the exact attacked state before transfer. | The receipt is submitted before state transfer and resolver cleanup. This is the only Event 018 claimant-victory route and is an actual border-war loss callback, not a generic state-control observation. |
| `secret_alliance_resolve_border_conflict_win` and `secret_alliance_resolve_border_conflict_loss` in country scope | The unresolved conflict flag and `secret_alliance_prepared_border_pair_is_current` require the prepared pair, current attacker ownership/control, current suspect ownership/control of the defender state, adjacency, and the post-callback no-border-war state. | The current owner callback country is saved as `famine_migration_corridor_exact_attacker`; `var:secret_alliance_border_defender_state` is the exact attacked state. | The receipt is submitted before `secret_alliance_clear_border_conflict_runtime`. Defender-side duplicate callbacks fail the owner-pair guard. The cancel resolver is unchanged. |

## Shared receipt contract

The shared helper saves the attacked state as `famine_migration_corridor_attacked_state`, checks that the state is the active corridor origin and that the active contract/front generation is valid, records the exact attacker country ID, and submits the receipt through the existing sparse active-displacement registry.

The helper remains fail-closed when no active corridor matches the exact state, so these adapters do not create corridor state or alter population, death, relief, evacuation, or migration ledgers.

The regular `famine_migration_corridor_exact_attacker` event target is created immediately before the target-state helper call and is chain-scoped; no global event target or new cleanup hook is required.

## Constants and tuning plan

No constants were added or changed.

The closure reuses existing corridor runtime constants and the existing owner-system pair and nonce fields; it does not add a new probability, score, duration, cost, or balance surface.

## Event-target and cleanup plan

Each resolver saves the current attacker owner as a regular event target immediately before entering the exact attacked state.

The three project resolvers retain their existing cleanup order after the receipt call.

Event 019 clears its trial flags and nonce-linked unit markers after the receipt; Event 018 clears frontier pair variables after owner or claimant outcome handling; Event 011 clears the prepared pair and unresolved global flag after the owner callback.

No global target is introduced, and cancellation-before-hostilities paths do not submit receipts.

## Migration from duplicated logic

There was no prior duplicated corridor receipt logic in these three resolver files.

The migration is therefore a narrow owner-first adapter closure: each authoritative project callback now saves the exact attacker and delegates the exact target state to the existing shared helper, while generic state-control, war-status, and cancellation paths remain untouched.

## Risks and unsupported proof surfaces

Event 018 does not carry a dedicated nonce; its owner-context trigger and exact owner/claimant state-country pair are the strongest existing resolver proof available in the allowed file boundary.

Event 011 does not carry a dedicated nonce; its unresolved global conflict plus prepared exact pair and current ownership/control checks are the strongest existing proof available, and defender-side duplicate callbacks fail closed.

Event 019 receipt submission additionally requires the started flag and the frozen pair trigger; if the engine removes one of the trial division markers before the attacker resolver runs, the adapter intentionally submits no receipt rather than guessing.

Ordinary land combat, generic `on_border_war_lost`, strategic bombing, generic war status, state control, and cancellation remain unsupported because they do not prove the exact attacker and exact attacked state for the corridor contract.

## Validation and MCP evidence

PowerShell brace counts were balanced for all three changed scripted-effect files: Event 019 `1024/1024`, Event 018 `2174/2174`, and Event 011 `5296/5296`.

`git diff --check` completed without diff errors for the three scripted-effect files.

The post-edit narrow `hoi4.event_inspect` lint for `chaosx.nr18.26` returned `EVENT_INSPECTED_PARTIAL` with no blocking diagnostics and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/acb0e308c9745f7ea9faabff139f69ec82d9a95de0572d51457ea16fb8e0c13e/a274d0fe3a4beceb722c1ca4343caf625fabce1c4eda3366f829ade00809b87a/event-lint-655620ee867d.json`.

Post-edit `hoi4.event_inspect` for `chaosx.nr19.920` and `chaosx.nr11.30` timed out after 180 seconds in the installed MCP route, even with focused lint parameters.

Post-edit narrow `hoi4.event_render` for `chaosx.nr19.920`, `chaosx.nr18.26`, and `chaosx.nr11.30` timed out after 180 seconds each at `view=scope`, downstream direction, `maxDepth=2`, and `maxNodes=40`.

The pre-edit narrow inspections for all three event roots were also partial, with no blocking diagnostics. The pre-edit artifact references were `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/59a02205e605d37e8fbfada841f55b6deeb2455d68459ef951d288762afeae05/b6c905fc85e50c918cd0683da55794898561da9e1978fe50831359b26e78c491/event-lint-655620ee867d.json` for Event 019, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/acb0e308c9745f7ea9faabff139f69ec82d9a95de0572d51457ea16fb8e0c13e/a274d0fe3a4beceb722c1ca4343caf625fabce1c4eda3366f829ade00809b87a/event-lint-655620ee867d.json` for Event 018, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4e2ca429689ca8ec17f2a774073f1bd8e889253377ea5e6e21b971377e93a5e9/3deaa54c6833e4c777f6ed9fe5cc5f69eb3f45b05892d048edde2beb579805ee/event-lint-655620ee867d.json` for Event 011.

The post-edit MCP cache reused the same workspace revision for the successful Event 018 lint, so the linked lint artifact is evidence for the event surface and source graph availability rather than a byte-level diff report.

## Remaining gaps

No generic ordinary-combat receipt was added because the available vanilla hooks do not expose a reliable exact attacker plus attacked state pair.

No cancellation receipt was added because a cancelled border war can end before hostilities and is not attack proof.

The MCP render timeout is an inspection-route blocker, not a source fallback; the parent should treat the source guards and the successful Event 018 lint as the available evidence and retain the timeout record above.
