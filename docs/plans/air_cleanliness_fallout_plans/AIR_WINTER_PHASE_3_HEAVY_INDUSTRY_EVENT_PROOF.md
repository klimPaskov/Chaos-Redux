# Air Winter Phase 3 Heavy Industry Event Proof

## Review and implementation boundary

The accepted source contract is `AIR_WINTER_PHASE_3_HEAVY_INDUSTRY_EVENT_ADDENDUM.md`. This proof covers the manually authored heavy-industry opening, its delayed furnace result, state-local routing, AI, Deaths integration, temporary production loss, repairable damage, transaction cleanup, and asset reuse.

The tranche adds no scheduler family, state scan, country scan, periodic callback, Fallout formula, treaty policy, scenario row, successor, or post-Fallout consumer. The reserved living-world suffixes `100` through `126` remain untouched.

This is a static source proof for Hearts of Iron IV 1.19.2.0. Hearts of Iron IV was not launched.

## Implemented event surface

The implementation adds two event blocks to `events/fallout_world_end_events.txt`:

- `chaosx.fallout.36` is the two-choice furnace opening.
- `chaosx.fallout.37` is the three-option deterministic result.

The five added options all carry effects and repeat the required target or branch validation at click time. The Air Winter pilot therefore contains 46 event blocks, 137 options, 136 effect-bearing options, and 48 delayed-result schedules. The one remaining effect-free option is the existing stale-order acknowledgement in `chaosx.fallout.203`.

Both blocks use `GFX_report_event_air_winter_phase_3`. The sprite and final DDS already exist. No new art, sprite, audio, or asset path was created.

## State identity and route order

`air_winter_event_is_heavy_industry_state` accepts a state through either of two identities:

- positive state coal
- at least four operational military and civilian factories in total

The factory identity uses `non_damaged_building_level` for `arms_factory` and `industrial_complex`. The exact five-case ladder is:

| Operational military factories | Operational civilian factories |
| --- | --- |
| at least 4 | any amount |
| at least 3 | at least 1 |
| at least 2 | at least 2 |
| at least 1 | at least 3 |
| any amount | at least 4 |

Installed but fully damaged factories do not satisfy the identity. Positive coal is an independent route, so a coal-only state is intentionally eligible.

Within a selected Phase 3 state, `air_winter_event_select_unseen_phase_route` applies this order:

1. reactor
2. hydroelectric dam
3. oil or refinery
4. coal or heavy industry
5. transport
6. clinic and heat

Heavy industry precedes transport so industrial states with railways or infrastructure can reach their identity route. The bounded country scheduler remains unchanged. It compares family priority, origin cycle, frozen phase and pressure score, then state id. The shared `air_winter_event_seen_phase_3` memory still permits one ordinary Phase 3 chain per country.

The opening trigger and both opening click guards recheck Phase 3 and the complete coal-or-factory identity. The result deliberately does not recheck Phase 3, coal, or the four-factory ladder. Legitimate state changes during the 30-day delay do not invalidate an owner-bound result.

## Full furnace shifts

The full-shift opening applies:

- Adaptation plus 2
- Exposure plus 2
- Building Damage Pressure plus 15
- a civilian loss request equal to 0.00015 of the remaining state population
- national Stability minus 0.01

The population request enters `air_winter_event_apply_deaths`. That helper uses `apply_exact_state_civilian_population_loss`, reason `constant:chaos_meter_deaths_reason.air_winter_exposure`, the shared Deaths setting gate, the protected incident floor, and the returned applied amount for Air Winter loss memory. The Stability reduction is a consequence and is not an affordability gate.

The result arrives after 30 days. `air_winter_event_furnace_full_shifts_succeeds` requires Adaptation at least 40 and Building Damage Pressure no more than 55 at result time.

A success applies:

- Adaptation plus 4
- Reclamation plus 2
- Building Damage Pressure minus 8

A failure applies:

- 0.50 repairable damage to one operational military factory, otherwise one operational civilian factory, otherwise local infrastructure
- Exposure plus 2
- Building Damage Pressure plus 25
- a further civilian loss request equal to 0.00010 of the remaining state population
- national Stability minus 0.005

`air_winter_event_damage_heavy_industry` uses a fixed `if`, `else_if`, `else_if` ladder. It damages at most one surface. If no operational military factory, civilian factory, or infrastructure remains, no physical building damage is issued. Exposure, pressure, Deaths, and Stability consequences still apply. No substitute damage surface is invented.

## Full shutdown

The shutdown opening applies:

- Adaptation plus 2
- Exposure minus 3
- Building Damage Pressure minus 15
- `air_winter_furnace_shutdown_industry_state` when at least one operational civilian or military factory remains
- `air_winter_furnace_shutdown_coal_state` when the state has positive coal

The industry modifier uses `local_factories = -0.50`. The coal modifier uses `state_resources_coal_factor = -0.25`. Each modifier lasts 31 days. A factory-only state receives the industry modifier, a coal-only state receives the coal modifier, and a state with both identities receives both.

The result is scheduled for day 30. The result `immediate` block removes both modifiers from a valid shutdown branch when the popup is delivered. Each result option calls the same removal again through `air_winter_event_clear_furnace_pending_branch`. The repeated removal is idempotent. The 31-day automatic expiry protects a branch whose result is lost or invalid.

The fixed restart result applies:

- Reclamation plus 2
- Exposure minus 1
- Building Damage Pressure minus 8

The shutdown route applies no immediate civilian loss or Stability loss. Its disclosed cost is the temporary factory and coal-output interruption.

## AI inverse

The full-shift option uses base weight 30. The shutdown option uses base weight 60.

`air_winter_event_furnace_full_shifts_ai_is_plausible` requires pre-choice Adaptation at least 38 and Building Damage Pressure no more than 40. The opening then adds 2 Adaptation and 15 pressure. Those exact deltas produce the delayed success boundaries of 40 and 55.

Full shifts gain weight at war, under fascism, with high War Support, and when the state passes the plausibility trigger. They lose weight when the state fails that trigger or national Stability is low. Shutdown gains weight at peace, under democratic or communist government, with low Stability, and when the state fails the full-shift plausibility trigger. It loses weight when full shifts are mechanically plausible.

Government and war preferences remain separate from the state-ledger predicate. The delayed result exposes exactly one option for the stored branch and deterministic outcome, so AI and human resolution use the same live state test.

## Branch transaction and cleanup

Each opening option performs the accepted transaction in this order:

1. revalidate the regular country and state targets, Phase 3, and the heavy-industry identity
2. call `air_winter_event_clear_furnace_memory`, which clears both branch flags, both shutdown modifiers, and all five durable furnace memories
3. apply the route consequences
4. set exactly one furnace branch flag and one opening memory
5. call `air_winter_event_refresh_state`, which binds the generic pending-result flag and original owner
6. call `air_winter_event_refresh_country_cooldown`
7. schedule `chaosx.fallout.37` after 30 days

The cooldown call is directly adjacent to the delayed `country_event` call in both options. The country cooldown lasts 46 days, which preserves the result buffer even when a human leaves the opening popup unresolved.

`air_winter_event_has_full_shifts_branch` and `air_winter_event_has_shutdown_branch` each require their own flag and reject the opposite flag. `air_winter_event_has_exact_furnace_branch` is their exclusive disjunction. The result trigger requires this exact branch contract. `air_winter_event_reconcile_pending_chain` also cancels a row that carries both furnace flags.

Every result option repeats `air_winter_event_targets_are_valid` and its exclusive branch. The full-shift options repeat the exact success predicate or its negation. Every result removes both shutdown modifiers, clears both branch flags, writes one result memory, and refreshes the state. The shared refresh then reconciles the generic pending-result flag and stored owner after no branch remains.

`air_winter_event_cancel_pending_chain` removes both shutdown modifiers and both furnace branch flags. Ownership loss, invalid stored owner, state reset, active Fallout, and an active Fallout transition therefore fail closed. `air_winter_event_clear_state_memory` also clears all five furnace opening and result memories.

The chain uses the regular `air_winter_event_country` and `air_winter_event_state` targets already saved by the bounded scheduler. It adds no temporary or global event target.

## Fallout snapshot isolation

`fallout_take_world_snapshot` freezes each Air Winter state row before it calls `air_winter_event_cancel_pending_chain` inside the existing state pass. The cancellation removes the furnace modifiers and branches. The snapshot routine then validates the completed rows before it can set `fallout_world_snapshot_complete`.

`air_winter_event_targets_are_valid` rejects both `fallout_transition_active` and `fallout_active`. A delayed furnace result therefore cannot mutate the frozen Fallout row after cancellation. No new iterator or callback was added.

## Static engine and vanilla proof matrix

| Surface | Official installed documentation | Vanilla precedent | Chaos Redux source |
| --- | --- | --- | --- |
| Direct coal comparison | `documentation/triggers_documentation.md`, `resource_count_trigger`, supports state scope and lists coal | `common/technologies/industry.txt` uses direct `coal > 0` resource comparisons | `air_winter_event_is_heavy_industry_state` and the `.36` descriptions use direct state coal checks |
| Operational factory identity | `documentation/triggers_documentation.md`, `non_damaged_building_level`, supports state scope and gives an `arms_factory` example | `common/resistance_activity/resistance_activity.txt` checks operational `arms_factory` and `industrial_complex` levels | `air_winter_event_is_heavy_industry_state` implements the five exact factory partitions |
| Repairable building damage | `documentation/effects_documentation.md`, `damage_building`, supports state scope and fractional damage | `common/resistance_activity/resistance_activity.txt` damages military factories, civilian factories, and infrastructure after operational checks | `air_winter_event_damage_heavy_industry` applies the accepted 0.50 fixed-order damage |
| Timed state dynamic modifiers | `documentation/effects_documentation.md`, `add_dynamic_modifier` and `remove_dynamic_modifier`, support state scope | `common/resistance_activity/resistance_activity.txt` adds the timed `sabotaged_resources` state modifier, while `events/AAT_Finland.txt` removes a dynamic modifier in explicit state scope | `air_winter_event_apply_furnace_shutdown`, `air_winter_event_clear_furnace_shutdown`, and shared cancellation own both modifiers |
| State factory output | `documentation/modifiers_documentation.md`, `local_factories`, lists the state category | `common/dynamic_modifiers/wuw_dynamic_modifiers.txt`, `GER_overburdened_state_modifier`, uses negative `local_factories` | `air_winter_furnace_shutdown_industry_state` uses the accepted negative 0.50 value |
| Coal output factor | `documentation/modifiers_documentation.md`, `state_resources_<Resource>_factor`, lists the state category and coal among the generated resource types | `common/dynamic_modifiers/wuw_dynamic_modifiers.txt` uses generated per-resource factors for oil and steel, while `common/resistance_activity/resistance_activity.txt` supplies the timed coal-sabotage state precedent | `air_winter_furnace_shutdown_coal_state` uses `state_resources_coal_factor = -0.25` |
| Regular targets in a delayed event | `documentation/effects_documentation.md` documents `save_event_target_as` and delayed `country_event`, while the offline Data structures page states that regular targets carry into events fired by the same effect chain | `events/Generic.txt` saves `alliance_inviter` and `alliance_applicant`, schedules `news.289` after 12 hours, and `events/NewsEvents.txt` reads `event_target:alliance_inviter` in that delayed event | The scheduler saves `air_winter_event_country` and `air_winter_event_state`, then `.36` schedules `.37` in the same chain |
| Snapshot cleanup in the existing state pass | `documentation/effects_documentation.md`, `every_state`, documents child effects in state scope | `common/scripted_effects/NOR_scripted_effects.txt`, `NOR_apply_resistance_to_fascists`, supplies a vanilla all-state effect precedent | `fallout_take_world_snapshot` freezes the row, cancels pending furnace state, validates all rows, then permits the snapshot-complete flag |

The established Deaths and exact state-population contract remains documented in `AIR_WINTER_MODIFIER_AND_DEATHS_PROOF.md`. The furnace chain supplies only the accepted loss percentages and uses the existing shared helper unchanged.

## Static validation and analyzer limitation

Static source inspection establishes the typed ids, route order, exact coal-or-factory identity, five-case factory ladder, 40 and 55 result gate, 38 and 40 AI inverse, two conditional 31-day modifiers, day-30 delivery cleanup, repairable fixed-order damage, no-target exhaustion, Deaths calls, exclusive branch transaction, refresh path, reset coverage, Fallout snapshot cancellation, and 46-day cooldown adjacency.

A scoped source count before the Fallout coordinator event range returns 46 top-level Air Winter ids, 137 option blocks, 136 option `hidden_effect` blocks, and 48 delayed day schedules. This matches the pilot totals above.

A narrow `hoi4.event_inspect` request for `chaosx.fallout.36` was attempted in lint and refresh mode and in scan and cached mode. The installed server returned `ARTIFACT_STORAGE_LIMIT` before producing a graph in both attempts. It supplied no diagnostic and is not part of the proof basis.

## Runtime and completion boundary

Static source review does not prove live popup presentation, popup ordering, delayed regular-target retention, AI choice frequency, state modifier arithmetic, timed expiry, building repair behavior, Deaths rounding, save recovery, or multiplayer behavior. No runtime acceptance is claimed.

This proof does not claim full Air Winter completion, full Fallout completion, living-world event-floor progress, or a working Fallout world rewrite. No fallback or simplification is approved by this tranche.
