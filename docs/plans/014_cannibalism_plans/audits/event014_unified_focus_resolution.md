# Event 014 Unified-Focus Gameplay Resolution

## Status

The unified CBL focus audit findings are resolved in gameplay script. The public reveal loads the CBL focus tree explicitly, all 108 focus rewards refresh a concrete operational contract ledger, the previously inert reward flags have consumers, and the four terminal capstones require proof from paid gameplay instead of focus completion alone.

No focus IDs were added, removed, or renamed. The tree remains at 108 unique `CBL_` focus IDs. The ordinary terminal contract still requires Chaos to be strictly greater than `constant:cannibalism_evolution_threshold.world_end_chaos`, which is 1000 in the Event 014 tuning table.

## Required references consulted

The implementation was checked against the offline Paradox wiki snapshot pages for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, and National focus modding.

Vanilla documentation consulted:

- `documentation/effects_documentation.md`, including `load_focus_tree`, event targets, building construction, flags, equipment, fuel, experience, dynamic modifiers, unit creation, and war goals
- `documentation/triggers_documentation.md`, including manpower, command power, experience, fuel, equipment, state control, ownership, and event-target checks
- `documentation/modifiers_documentation.md` for every modifier used by the paid operations
- `documentation/script_concept_documentation.md`, Script Constants
- `common/script_constants/documentation.md`

The vanilla `BFTB_Greece.txt` focus-tree transfer was used as the structural precedent for `load_focus_tree = { tree = ... keep_completed = no }`. Existing Event 014 targeted decisions, missions, exact Deaths-backed consumption, scripted recruitment, and payment helpers were used as the closer repository precedents.

## Resolution summary

### Public reveal and transfer safety

`cannibalism_create_unified_country_from_selected_host` now loads `cannibalism_unified_focus_tree` inside CBL after `cannibalism_reveal_complete` is set and before any player tag transfer. This preserves pre-reveal Hannibal secrecy and guarantees that the event-created country receives the intended tree.

The missing `cannibalism_unified_focus_tree` localisation key is defined as "The Continental Host" in the Event 014 English localisation file.

The same effect initializes the unified decision counters and capacities. Player achievement ledgers are captured in the human source country and applied in CBL immediately before each `change_tag_from`. The selected human host marks CBL with `achievement_cannibalism_player_unification_host`. CBL begins with one integrated named commander, and every retained or host commander created during later absorption increments `cannibalism_integrated_named_commander_count`.

The earlier player choice to follow a newly emerged warlord uses the same source-capture and destination-apply sequence before its human `change_tag_from`, so the Event 014 achievement ledger survives every player tag transfer in this route family.

### Reward-consumer ledger

Every focus completion calls `cannibalism_unified_focus_finalize_reward`. That effect rebuilds eight capacities from the permanent reward flags and refreshes terminal-package proof.

| Contract | Reward flags consumed | Maximum reachable capacity |
|---|---:|---:|
| Command | 66 across exclusive routes | 165 |
| Larder | 50 across exclusive methods | 115 |
| Army | 28 | 140 |
| Navy | 16 | 80 |
| Air | 14 | 70 |
| Cells | 16 | 80 |
| Campaign | 9 | 45 |
| Counterwar | 9 | 45 |
| Total | 208 | 740 |

Each capacity reward flag contributes five capacity. Capacity gates the decision families and continuously determines temporary operation duration, so rewards beyond the first unlock threshold remain material. The four terminal-gate flags also gate package readiness, the three final-mobilization flags directly control the world-end category and terminal decision, and the world-end completion marker remains consumed by the existing super-event bridge. The four operational-package flags introduced by this resolution are consumed by the final readiness trigger.

Risk and burden contracts also retain their downside. State exhaustion, organized resistance, hostage defection, purge resistance, anchorage discovery, fear-bombing escalation, and false-surrender failure raise World Hostility when their associated action is used. The mobile escort burden adds a support-equipment payment. Legion and Bone Guard cap upgrades change the real recruitment caps.

The reward-consumer audit found no original unified-focus reward flag without a consumer. It also confirmed one finalizer call in each of the 108 focus rewards.

### Implemented decisions and missions

Five phased categories expose 21 paid actions and four maintained missions:

- Continental Command: autonomous-warlord absorption, route-aware governor appointment, resistant-rival purges, a repeatable route-aware order, and a three-order command mission
- Continental Larder: centralization, one feeding-capital designation, one exact Deaths-backed consumption action for each of the four exclusive Larder routes, and a three-action Larder mission
- War Machine: a paid air-program foundation for inherited countries without an air base, air experience, or airframes, exact Deaths-backed Cannibal Legion and Bone Guard recruitment, and paid army, naval, and air operations with a three-action mission
- Campaigns Without Borders: foreign-cell disruption, paid global campaign preparation, one-time postwar state integration, enemy counterwar disruption, and a three-operation counterwar mission
- Final Global Mobilization: exact Deaths-backed terminal consumption after the final-mobilization focus, required before the final world-end focus

The accepted minimum action IDs are present as `cannibalism_unified_absorb_warlord`, `cannibalism_unified_appoint_governor`, `cannibalism_unified_purge_rival`, `cannibalism_unified_centralize_larder`, `cannibalism_unified_create_cannibal_legion`, `cannibalism_unified_launch_continental_hunt`, `cannibalism_unified_seed_major_enemy_army`, `cannibalism_unified_designate_feeding_capital`, `cannibalism_unified_destroy_coalition_hub`, and `cannibalism_unified_begin_terminal_mobilization`.

All units start at zero manpower and zero equipment. Recruitment converts only the exact population removed through the Deaths pipeline into manpower. Infantry, support equipment, artillery, motor transport, trains, convoys, aircraft, fuel, command power, and service experience are either reserve gates or explicit paid costs. No decision grants recruitment equipment.

### Route awareness

The continental command order resolves through both exclusive route families:

- Keep the Lieutenants improves alignment and authority.
- Break the Warlords increases authority at the cost of hostility.
- Chain the Rivals increases authority and network reach.
- One Command adds direct authority.
- Many Jaws strengthens alignment.
- Ritual Administration expands network reach.

The four Larder methods have separate state-population requirements, exact population losses, command costs, and transport or support costs. Their player-facing text states the exact Deaths amount.

### Operational terminal proof

The four capstone focus flags no longer complete terminal readiness by themselves.

| Package | Required gameplay proof |
|---|---|
| Larder | Larder capstone plus 5 paid storage or consumption actions |
| Army | Army capstone plus 5 Cannibal Legions, 1 Bone Guard, and 5 paid army operations |
| Expansion | Expansion capstone plus 5 prepared campaigns, 3 postwar state integrations, and 5 foreign-cell operations |
| Counterwar | Counterwar capstone plus 5 paid enemy-command disruption operations |

Each completed package contributes 25 terminal progress. `cannibalism_terminal_route_ready` and `cannibalism_terminal_route_complete` are set only when all four operational-package flags exist on ordinary CBL. `cannibalism_can_complete_ordinary_world_end` checks the package set directly in addition to the existing strict Chaos, network, state, consumed-population, and Larder requirements.

`CBL_final_global_mobilization` then opens `cannibalism_unified_begin_terminal_mobilization`. The action must remove exactly 100,000 population through Deaths and spend 25 Command Power before `CBL_dismantle_the_ordinary_world` becomes available.

### Air branch validity

`CBL_repair_the_captured_airframes` requires at least one controlled air base, more than five Air Experience, or more than 25 small airframes. Its AI weight falls to zero while that requirement is false. A paid War Machine decision can build one capital air-base level from manpower, support equipment, and fuel after captured-equipment conversion, preventing a host with no inherited air capability from becoming permanently blocked.

## Balance review

The values are centralized in `common/script_constants/014_cannibalism_unified_decision_constants.txt`. The main late-game proof costs are deliberately substantial:

- Five Legions remove 125,000 population through Deaths and spend 375 Larder before the Bone Guard and army-operation requirements.
- One Bone Guard removes 20,000 population through Deaths and spends 100 Larder.
- Five army operations spend 100 Command Power, 75 Army Experience, and 2,500 fuel.
- Five foreign-cell operations spend 125 Larder, 500 support equipment, and 75 Command Power.
- Five prepared campaigns spend 250 Larder, 2,500 infantry equipment, and 100 Command Power.
- Three postwar integrations spend 30,000 manpower, 300 support equipment, and 30 trains.
- Five counterwar operations spend 750 support equipment, 500 trucks, 3,750 fuel, 100 Command Power, and 50 Army Experience.
- Terminal mobilization removes another 100,000 population through Deaths and spends 25 Command Power before the last focus.

These costs sit behind the late unified tree and the existing greater-than-1000 Chaos gate. Army, naval, air, command, cell, campaign, and counterwar bonuses are temporary and their duration is bounded at 365 days. Postwar state integration is permanent but costs resources, applies only to an owned and controlled non-core state, and can be completed only once per state.

## Files changed

- `common/national_focus/014_cannibalism_unified_focus.txt`
- `common/scripted_effects/014_cannibalism_unified_focus_effects.txt`
- `common/scripted_effects/014_cannibalism_unification_effects.txt`
- `common/scripted_effects/014_cannibalism_unified_decision_effects.txt`
- `common/scripted_triggers/014_cannibalism_triggers.txt`
- `common/scripted_triggers/014_cannibalism_unified_decision_triggers.txt`
- `common/decisions/categories/014_cannibalism_categories.txt`
- `common/decisions/014_cannibalism_unified_decisions.txt`
- `common/script_constants/014_cannibalism_unified_decision_constants.txt`
- `common/dynamic_modifiers/014_cannibalism_unified_decision_modifiers.txt`
- `events/014_cannibalism.txt`
- `localisation/english/014_cannibalism_l_english.yml`
- this report

## Asset and icon wiring

The 25 decision entries reuse 13 existing Event 014 sprites whose registrations and DDS textures resolve through `interface/014_cannibalism.gfx`. The five unified categories are wired to dedicated unified category sprites registered in the same file, but their ten referenced DDS binaries are not present in the workspace. The active unified-focus asset handoff owns only the 108 focus icons and does not own these category icons or panels. Category-art production, its manifest, and final asset validation therefore remain a parent-integration blocker outside this gameplay patch.

| Surface | Registered sprite families | Texture location and owner |
|---|---|---|
| Unified category icons | `GFX_decision_category_cannibalism_unified_{command,larder,war_machine,global_campaign,world_end}` | `gfx/interface/decisions/014_cannibalism/decision_category_cannibalism_unified_*.dds`; five binaries still required |
| Unified category panels | `GFX_cannibalism_unified_{command,larder,war_machine,global_campaign,world_end}_category_panel` | `gfx/interface/decisions/014_cannibalism/cannibalism_unified_*_category_panel.dds`; five binaries still required |
| Unified decisions | Existing `GFX_decision_cannibalism_*` command, corridor, feeding, recruitment, convoy, screening, infiltration, and mission sprites | `gfx/interface/decisions/014_cannibalism/`; gameplay patch reuses registered assets |

## Meaningful validation scenarios

1. A selected human host reaches public reveal. The global reveal flag precedes CBL creation, CBL receives the unified tree with no inherited focus completions, the player ledger moves before the tag change, the host achievement flag exists, and the named-commander count begins at one.
2. A later human warlord is absorbed. Its player ledger is captured before the tag change, applied to CBL, and a retained or host commander increments the integrated named-commander count.
3. Each exclusive Larder route exposes only its own population action. A successful action removes the exact stated population through Deaths, updates Larder through the common consumption pipeline, pays its non-population costs, and advances both the mission and package counters.
4. A Legion and Bone Guard are raised. The chosen state loses the exact population, the same loss enters the manpower pool, the unit is created at zero manpower and equipment, existing stockpiles supply it, and the per-state cooldown prevents immediate reuse.
5. A CBL with no inherited air capability sees the air focus requirement fail and the paid air-foundation project appear. Completing the project pays all costs, builds the air-base level, and makes the focus valid.
6. Completing the four terminal capstones without the operational counts leaves terminal progress below 100 and `CBL_final_global_mobilization` unavailable. Meeting each paid package adds exactly 25 progress. The final-mobilization focus then opens the exact Deaths-backed terminal decision, and only that successful transaction opens `CBL_dismantle_the_ordinary_world`.
7. The reward-consumer scan reports 208 unique capacity mappings, direct consumers for every terminal and operational-package flag, zero missing focus-set flag consumers, and 108 focus finalizers.

## Future extensions

- Display the eight capacity totals and four operational-package checklists in a dedicated scripted GUI if a later UI plan authorizes that surface.
- Add more target-specific cell and campaign outcomes while preserving the same paid costs and capacity-duration contract.
- Add bespoke decision icons only if the Event 014 asset plan later replaces the currently registered reusable icon set.

## Simplifications, omissions, and blockers

None in the gameplay scope. All audited unified-focus gameplay findings were implemented. The focus count, strict terminal Chaos comparison, reveal secrecy, Deaths accounting, and no-free-equipment rule were preserved. No fallback mechanic, placeholder decision, missing localisation, missing AI weight, or unreported gameplay reduction remains.

The whole Event 014 audit is not yet complete because the five dedicated category icons and five category panels referenced by the current category and `.gfx` wiring are missing. They are not part of the active 108-focus-icon handoff and require a separate asset assignment before completion can be claimed.

## Skills used

- `hoi4-focus-trees`
- `hoi4-decisions-missions`
- `chaos-redux-events`
