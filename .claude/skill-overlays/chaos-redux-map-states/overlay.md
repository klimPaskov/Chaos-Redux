---
description: Use when creating, editing, auditing, or scripting Chaos Redux map and state work: startup history grants, the generated map/buildings.txt override, custom spawn buildings, state-scope effects, triggers and iteration, victory points, supply and railways, famine and migration state data, exact state-to-state civilian transfers, cohort registries, reception ledgers, state map modes, or the MCP map tools.
---

### In Chaos Redux Map and States

Guidance for the Hearts of Iron IV map and state system as used in Chaos Redux: what each map file does, how a state is defined, how script changes states at runtime, how population moves between states, and which engine mistakes fail silently. (Chaos Redux wording differs from the kit)
This skill also owns the exact civilian transfer, cohort registry, reception ledger, and state map mode contracts in [references/state-ledgers.md](references/state-ledgers.md).

### In Contents

- Chaos Redux specifics, including state ledgers (references/state-ledgers.md)

### In Source map

`GAME` means `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV`. (Chaos Redux wording differs from the kit)

### In Decision procedure: which mechanism

5. Change the map geometry (new province, state split, new strategic region): use the Agent Nudger MCP routes (`hoi4_map_inspect` with `layer`, `overlays`, `scale`, `tile`, or `area` for renders, and `hoi4_map_rewrite`) rather than hand-editing BMPs and CSVs. See MCP map tools. (Chaos Redux wording differs from the kit)

### In Buildings (common/buildings) and building models

Definitions live in `common/buildings/*.txt` under `buildings = { name = { ... } }` (`GAME/common/buildings/00_buildings.txt`). Fields verified in the vanilla file and `WIKI/Building modding`: (Chaos Redux wording differs from the kit)


### In Flags, variables, and modifiers on states

- State variables: `set_variable`, `add_to_variable`, and friends executed in state scope write that state's variable. Read another state's variable with a numeric prefix (`123.my_var`), a stored scope (`var:target_state.my_var`), or a chain (`province_controllers^1234:capital:my_var`) per `WIKI/Data structures`. Temporary variables have no scope. (Chaos Redux wording differs from the kit)

### In Map modes and map GFX

- A working repository precedent is `common/map_modes/chaosx_state_map_modes.txt` with its sprite wiring in `interface/*.gfx`.

### In MCP map tools

- `hoi4_map_inspect` with render selectors (`layer`, `overlays`, `scale`, `tile`, or `area`): layers `province`, `state`, `strategic-region`, `terrain`, `continent`, `owner`, `controller`, `cores`, `claims`, `coast`; overlays `coastlines`, `ports`, `victory-points`, `resources`, `state-buildings`, `province-buildings`, `supply-nodes`, `railways`, `adjacencies`, `building-positions`, `unit-positions`, `weather-positions`; restrict with `area` (state, region, province ids) or a pixel `tile`. (Chaos Redux wording differs from the kit)

### In Chaos Redux specifics

The `CLAUDE.md` coding, constants, dynamic-effect, and localisation rules apply and are not repeated here, including the 1,000-iteration loop cap (use a scope iterator or bounded batches over larger sets) and the whole-world iteration permission rule. (Chaos Redux wording differs from the kit)

**What the mod does and does not ship**

- Chaos Redux does not copy vanilla `history/states`, `map/` geometry, or vanilla country and OOB history, because a copy overrides other mods and freezes older vanilla data. Additive setup runs from `on_startup` through `chaosx_apply_startup_history_grants` (`common/scripted_effects/chaosx_startup_history_effects.txt`, tuning in `startup_history_constants.txt`, one global idempotence flag), which dispatches tag-specific facilities, technologies, stockpiles, characters, and projects by explicit country scope (`docs/systems/startup_history_compatibility.md`). New starting content goes there.
- The one map file is `map/buildings.txt`, a generated override that preserves the complete installed vanilla table and adds coordinates for the custom `chaosx_*_spawn` buildings (`common/buildings/chaosx_buildings.txt`, `chaosx_3d_model_spawns.txt`, `chaosx_3d_model_pilots.txt`). Regenerate it instead of hand-editing, and again after a game update. A dynamic custom spawn pool without complete coordinate coverage must keep automatic nudging on (`docs/systems/3d_model_pipeline/chaosx_3d_runtime_contract.md`).

**State-scoped systems**

- Famine and migration drive state flags, dynamic modifier families (`common/dynamic_modifiers/famine_state_modifiers.txt`, `migration_state_modifiers.txt`) that a refresh effect removes and re-adds on every stage change, and two of the five scripted state map modes in `common/map_modes/chaosx_state_map_modes.txt` (`docs/systems/state_map_modes.md`). Read the owner documents (`docs/systems/famine_system.md`, `migration_system.md`) before touching their state data.
- Formable state puzzles use exact state-control proof with a state registry: `docs/formables/` and the `templates/formable_state_puzzle/` folder of `chaos-redux-decisions-missions`.
- Reuse the state helpers in `common/scripted_effects/chaosx_dynamic_effects.md` before writing new ones: `damage_state_building_dynamic`, `damage_buildings_in_random_states`, `get_random_sea_region`, and the population helpers `apply_exact_state_civilian_population_loss`, `apply_state_population_loss_without_recruitable_manpower_gain`, and `apply_state_population_gain_without_recruitable_manpower_gain`. Population arithmetic uses `state_population_k`.

**Moving people between states**

Exact civilian transfers, cohort registries, reception ledgers, custody receipts, and transaction-time map projections follow [references/state-ledgers.md](references/state-ledgers.md). Read it before adding any code that debits or credits state population, keeps a cohort across effect chains, or feeds a state map mode. One transfer owner (`civilian_transfer_*`) holds the only physical debit and credit path; owners submit proof and never move population themselves.
