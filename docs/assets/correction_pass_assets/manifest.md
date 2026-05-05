# Correction Pass Asset Manifest

## Overview

This pass replaces confirmed unknown or missing placeholder references with valid art already present in vanilla Hearts of Iron IV. Vanilla icons are referenced directly instead of being copied into Chaos Redux.

## Genocide System

| Use | GFX name | Final path | Source asset |
| --- | --- | --- | --- |
| Mengele Aryan race leader portrait | `portrait_GER_perfect_aryan` | `gfx/leaders/scientists/portrait_GER_perfect_aryan.dds` | `gfx/leaders/GER/Portrait_Germany_Generic_land_4.dds` |
| Concentration camp building icon | `GFX_building_concentration_camp` | vanilla direct reference | `gfx/interface/buildings/building_fort_icon.dds` |
| Extermination camp building icon | `GFX_building_extermination_camp` | vanilla direct reference | `gfx/interface/buildings/building_intel_icon.dds` |
| Camps/Gulag decision category icon | `GFX_decision_category_chaos_doom` | existing Chaos Redux sprite | `gfx/interface/decisions/decision_category_chaos_doom.dds` |

Map entities for `building_concentration_camp` and `building_extermination_camp` are registered in `gfx/entities/chaosx_buildings.asset` and reuse vanilla `building_bunker` and `building_stronghold_network` meshes.

## Communist Insurgency

| Use | GFX name | Final path | Source asset |
| --- | --- | --- | --- |
| National communist pressure | `GFX_idea_communist_state_control_pressure` | vanilla direct reference | `gfx/interface/ideas/idea_generic_secret_police.dds` |
| Agitation zone | `GFX_idea_communist_agitation_zone` | vanilla direct reference | `gfx/interface/ideas/generic_communism_drift_bonus.dds` |
| Insurgent stronghold | `GFX_idea_communist_insurgent_stronghold` | vanilla direct reference | `gfx/interface/ideas/idea_MEN_communist_revolutionaries.dds` |
| Lockdown | `GFX_idea_communist_lockdown` | vanilla direct reference | `gfx/interface/ideas/idea_generic_purge.dds` |
| Post-crackdown scars | `GFX_idea_communist_post_crackdown_scars` | vanilla direct reference | `gfx/interface/ideas/idea_generic_army_problems.dds` |
| Worker ritual fear | `GFX_idea_communist_worker_ritual_fear` | vanilla direct reference | `gfx/interface/ideas/idea_generic_fascist_workers.dds` |
| Emergency disruption | `GFX_idea_communist_emergency_disruption` | vanilla direct reference | `gfx/interface/ideas/FRA_factory_strikes.dds` |

## Still Worth Reviewing

These are not confirmed unknown placeholders in this pass, but they are likely candidates for custom replacement art:

- `gfx/event_pictures/communism_spread/*.dds`: final communist insurgency report-event images.
- Holy Realm report-event images if their current DDS files are temporary.
- Holy Realm stage-specific leader portraits if politics-view portraits should change, not only the Mandala Panel leader frame.
- Holy Realm optional super-event art and dedicated audio for Vow against Annihilation, Divine Sovereignty, and Mandala Break.
- Dedicated custom 3D meshes for `concentration_camp` and `extermination_camp`; this pass wires real vanilla map meshes under stable custom entity names.

## Holy Realm

| Use | GFX name | Final path | Source asset |
| --- | --- | --- | --- |
| Holy Mandala decision category | `GFX_decision_category_holy_mandala` | vanilla direct reference | `gfx/interface/decisions/decision_category_generic_mountain_fortification.dds` |
| Final Ledger decision category | `GFX_decision_category_final_ledger` | `gfx/interface/decisions/holy_realm/decision_category_final_ledger.dds` | `gfx/interface/decisions/decision_category_generic_crisis.dds` |
| Holy doctrine balance category | `GFX_decision_category_holy_doctrine_balance` | vanilla direct reference | `gfx/interface/decisions/decision_category_generic_political_actions.dds` |
