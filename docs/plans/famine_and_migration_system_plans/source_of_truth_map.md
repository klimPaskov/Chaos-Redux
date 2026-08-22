# Famine and Migration Source-of-Truth Map

Status: This map reconciles documentation against the current source snapshot and does not approve gameplay completion.

## Authority order

1. `docs/specs/famine_and_migration_system_specs/` is the accepted design source unless a parent decision explicitly supersedes a claim.
2. `common/scripted_effects/chaosx_famine_migration_effects.txt` and `common/scripted_effects/famine_migration_adapter_effects.txt` are implementation evidence for reusable contracts and owner seams.
3. `common/decisions/famine_migration_decisions.txt` and `common/decisions/categories/famine_migration_categories.txt` own the ordinary decision and mission surface.
4. `common/map_modes/chaosx_state_map_modes.txt` owns the two dedicated famine and migration mapmode definitions.
5. `common/scripted_effects/chaosx_dynamic_effects.md`, `docs/systems/famine_and_migration_system.md`, and `docs/systems/state_map_modes.md` are permanent public documentation reconciled to the source and clearly mark unresolved gates.
6. `docs/plans/famine_and_migration_system_plans/subagent_handoffs/` records bounded evidence and risks, while `handoff_dispositions.md` records parent-facing dispositions.
7. `docs/assets/famine_and_migration_system/manifest.csv` owns asset inventory evidence, while runtime `.gfx` files remain implementation evidence and spreadsheet files remain outside this worker's write scope.

## Current surface map

| Surface | Canonical implementation | Current documentation status | Open evidence or decision |
| --- | --- | --- | --- |
| Food score and stage | `famine_migration_evaluate_food_security` in `common/scripted_effects/chaosx_famine_migration_effects.txt` | Formula, thresholds, hysteresis, and trapped normalization documented. | Balance and runtime behavior remain parent-owned. |
| Famine mortality | `famine_migration_apply_famine_mortality` | One `From famine` owner and one exact population debit documented. | No live transaction proof in this pass. |
| Exact transfer | `famine_migration_transfer_civilians_exact` and `famine_migration_restore_origin_population_residual` | Origin debit, route deaths, survivor credit, short-credit origin restoration, manpower correction, and conservation residual documented. | Parent must review all decision callers. |
| Decision reveal | `famine_migration_refresh_decision_phase_from_state` and `chaosx_famine_migration_category` | Hidden start and emerging thresholds documented. | Parent runtime/UI review remains open. |
| Dormant-country retirement | `famine_migration_retire_inactive_displacement_country` | Scheduler removal and durable-ledger preservation documented. | Long-run save behavior remains unproven. |
| Sparse jobs | `famine_migration_process_registered_runtime` and existing host-only Chaos Meter hook | Five registry arrays and no broad world scan documented. | Parent should retain host/runtime review. |
| Decisions and missions | `common/decisions/famine_migration_decisions.txt` | 26 decisions and three missions listed. | Probability compare remains queued after timeout. |
| Active adapters | Famine pressure, exact transfer, reception, projection, integration, return, resettlement, and five condemnation decision paths | Active source call sites separated from public API seams. | Owner-local cross-system calls remain incomplete. |
| API-only seams | `famine_migration_adapter_effects.txt` and request adapters | No fabricated owner sources; pending surfaces explicitly listed. | Parent needs owner routing decisions. |
| Historical profiles | `famine_migration_select_historical_profile_id`, resolver, constants, and scripted localisation | Exactly 15 profile mappings documented. | Source eligibility is not observed gameplay evidence. |
| Dedicated mapmodes | `common/map_modes/chaosx_state_map_modes.txt` | Exactly `famine_state_map_mode` and `migration_state_map_mode`. | GUI/render route did not provide visual artifact. |
| Mapmode presentation | `docs/systems/state_map_modes.md` and `interface/mapmodes_interface.gfx` | Stage/role priority and score-tooltip distinction documented. | Unrelated map locator diagnostics remain open. |
| Achievements | `common/achievements/chaos_redux_achievements.txt` and famine achievement effects | Eight IDs, predicates, assets, and localisation documented. | Disqualifier producers, lifecycle evidence, and unlock behavior await achievement-audit review. |
| Assets | `docs/assets/famine_and_migration_system/manifest.csv` and package GFX files | 46 assigned category/state/decision/achievement/Deaths rows plus report assets documented, including the two wired Deaths-reason texticons. | Report-picture carrier and event consumers are not identified. |
| CXT fixture | `common/scripted_effects/famine_migration_cxt_test_effects.txt` and `docs/testing/chaosx_test_country.md` | Bounded test setup and non-gameplay scope documented. | Live CXT verification remains external. |
| Event 149 | No implementation source; catalog row 149 | Retired/absorbed with no replacement ID or pacing weight, and exported catalog wording now matches. | No replacement source is permitted. |

## Exact dedicated mapmode inventory

The system owns exactly these two new mapmodes:

- `famine_state_map_mode`
- `migration_state_map_mode`

`contaminated_states_map_mode`, `deaths_state_map_mode`, and `air_winter_state_map_mode` are existing neighboring crisis mapmodes and are not additional famine or migration mapmodes.

## Historical profile IDs

The source and documentation use exactly these 15 profile IDs:

`hist_soviet_1932_memory`, `hist_china_henan_1942`, `hist_china_policy_famine`, `hist_bengal_1943`, `hist_vietnam_1944`, `hist_java_1944`, `hist_greece_1941`, `hist_leningrad_siege`, `hist_dutch_hunger_winter`, `hist_spain_early_1940s`, `hist_ireland_memory`, `hist_brazil_ceara`, `hist_congo_interaction`, `hist_ethiopia_policy`, and `hist_nuclear_winter_global`.

The complete mapping table and proof contracts are in `docs/systems/famine_and_migration_system.md` and the accepted architect handoff.

## Current evidence references

The current bounded map MCP artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/34498d56d4bf765796f793b12431c8e42bf07506d9484b1c7f3a961900f58b1d/66c0aca0d881147df54e388a8d987bf4f8422ed0c1b6fa779fc8ea008ddb3eb0/map-inspect.456c28c5a8e6bad1.json`.

That artifact confirms the requested state records and core map geometry but retains unrelated `map/buildings.txt` locator diagnostics.

The probability baseline is pre-change absence evidence. The older post audit completed a partial 20-scenario `mission_ai_will_do` evaluation with 59 unresolved inputs and only a current/current comparison. A final mandatory inspect on source hash `62b30cfcbe4843be15c75cde4b6200b823c98aafaba768c88f12181df458faf0` again redirected the empty decision adapter to the mission adapter. Because the older scenario artifacts use source hash `c874297e...`, all 20 named scenarios remain unresolved for the current revision and no genuine baseline/post comparison exists.

The mapmode GUI route modeled zero hardcoded `mapmodes` elements and timed out during render, so source evidence is not represented as a complete visual runtime proof.

## Reconciliation rules for future edits

Do not add a third famine or migration mapmode without a new accepted specification decision.

Do not convert API-only owner seams into gameplay claims until an owner call site and matching evidence exist.

Do not describe the food score as a visual intensity band because the famine mapmode colors by stage and exposes score through authorized tooltips.

Do not clear integration, resettlement, or return ledgers when documenting dormant scheduler cleanup.

Do not invent an Event 149 source or replacement ID; the spreadsheet worker has reconciled the exported retirement wording and unavailable status.

Do not claim historical profile activation, achievement unlocks, weighted balance, or visual mapmode completion from source presence alone.

The authoritative closure status is `docs/plans/famine_and_migration_system_plans/completion_report.md`. Adapter and achievement closure handoffs supersede earlier descriptions of those workers as pending, but their recorded missing producers remain blockers.

Ideology remains a bounded AI modifier only after policy, destination, and route gates pass; persecution, famine, bombing, camps, occupation conduct, and contamination override affinity and no ideology can authorize an unsafe route.
