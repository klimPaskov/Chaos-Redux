# CBRN battlefield operations

## Purpose

The battlefield operation family is the exact-state ground delivery layer for chemical weapons. It is implemented as native raids in `common/raids/cbrn_chemical_land_raids.txt`, so the engine owns target selection, preparation timers, cooldowns, essential-equipment reservation, and Command Power payment.

The family defines four route types, each with one variant per agent and armored delivery with light, medium, and heavy chassis variants:

- Cylinder Release uses a prepared supply node and an enemy target state.
- Projector Barrage reserves projector equipment and a fortified or supply target.
- Artillery Fire Plan reserves chemical artillery ammunition against enemy formations.
- Armored Delivery reserves sealed armored-delivery equipment.

The raids are not aircraft proxies, combat estimators, or country-wide pulses. Each raid starts at a supply node, assigns a qualifying land division that includes a Gas Mask and Decontamination Detachment, and requires a real selected target state, an enemy controller, the applicable use policy, the selected agent's project, and real national equipment.

## Resolution flow

1. The player or the raid AI selects one agent-specific raid variant when its technology and policy gates pass. The AI scores each variant from the `cbrn_battlefield_operation_ai` constants.
2. The native raid reserves the exact payload, masks, decontamination equipment, instruments, support equipment, and route equipment through `essential_equipment` and pays Command Power at launch. No script helper debits or refunds that stock.
3. When the raid resolves, each success level saves the actor country, target state, victim country, and one marker per route, agent, outcome, and Phantom Mist variant as event targets and fires the hidden country event `cbrn_land_raid_bridge.1` in `events/cbrn_land_raid_bridge_events.txt`.
4. The bridge event restores the actor country as `ROOT` and calls `cbrn_resolve_chemical_land_raid_country_outcome`, described in `common/scripted_effects/cbrn_chemical_land_raid_effects.md`, which classifies the agent and route, checks the exact-target policy, and builds the condition receipt through the helpers in `common/scripted_effects/cbrn_battlefield_operation_effects.txt`.
5. The shared CBRN chemical exposure dispatcher receives the exact state, agent, class, route, severity, protection receipt, and condition receipt only when the native outcome is limited success, success, or critical success.
6. Resolution records disruption, military and civilian deaths, contamination, medical saturation, evidence, attribution, Condemnation, and history through the shared consequence pipeline.
7. A failed or invalid raid produces no release. Equipment the native raid reserved is not fabricated back into stock by script.

Shortage-ready routes use the explicit lower equipment floors from the `cbrn_battlefield_operation_constants.txt` tables and receive the centralized command, release-efficiency, and friendly-risk scaling. Doctrine can raise operational harm and reduce Condemnation within the shared doctrine floor; it does not remove evidence, attribution, deaths, contamination, medical history, resistance trauma, or responsibility.

## Engine boundary

The current version exposes no verified exact-state receipt for continuous chemical air missions, so continuous air missions stay out of this family and idle chemical-capable aircraft never contaminate a region. Air-delivered chemical raids are defined separately in `common/raids/cbrn_chemical_air_raids.txt`. The old general-wide commander cylinder abilities remain disabled for the same reason. The native raid carries the selected target state to the outcome effect, and that state is not a condition estimator or proxy.

## Files and tuning

| Surface | File |
| --- | --- |
| Native raid types, timings, equipment reservations, and AI scoring | `common/raids/cbrn_chemical_land_raids.txt` |
| Central timing, costs, condition receipts, and AI factors | `common/script_constants/cbrn_battlefield_operation_constants.txt` |
| Exact target and equipment gates | `common/scripted_triggers/cbrn_battlefield_operation_triggers.txt` |
| Raid condition and agent-class receipt helpers | `common/scripted_effects/cbrn_battlefield_operation_effects.txt` |
| Raid outcome adapter | `common/scripted_effects/cbrn_chemical_land_raid_effects.txt` |
| Country-root bridge event | `events/cbrn_land_raid_bridge_events.txt` |
| Dedicated interface registrations | `interface/cbrn_battlefield_operations.gfx` |

Numeric values are gameplay tuning. Historical confidence is low to moderate because a route cost represents an operation-sized preparation and supply package rather than a fixed historical tonnage. The selected chemical agent changes the shared exposure profile; native battlefield operation gates do not use agent-specific success odds.

## Asset contract

The five registered sprites are:

- `GFX_decision_cbrn_battlefield_cycle_agent`
- `GFX_decision_cbrn_battlefield_cylinder_release`
- `GFX_decision_cbrn_battlefield_projector_barrage`
- `GFX_decision_cbrn_battlefield_artillery_fire_plan`
- `GFX_decision_cbrn_battlefield_armored_delivery`

They belong under `gfx/interface/decisions/stage_6_chemical_delivery/battlefield_operations/` and are registered by `interface/cbrn_battlefield_operations.gfx`. Existing Chaos Redux raid icons under `gfx/interface/military_raids/` are preserved and are not overwritten or used as cross-type substitutes. The five DDS outputs are packaged at the dedicated runtime paths, with source-art, alpha extraction, processed PNG, archive DDS, runtime DDS, hash, and final-size contact-sheet evidence in `docs/assets/chaos_warfare_system/stage_6_chemical_delivery/`. No placeholder or resized cross-type asset is accepted.

## Future extensions

An exact current-version Army Headquarters target receipt could connect a prepared command ability to a selected state. A verified continuous-air mission hook could then add an explicit mission-activity condition without a region estimator. Neither extension should be enabled until the engine proof is documented and tested against the installed version.
