# Stage 5 doctrine and officer-corps GFX/path handoff

This package did not edit `.gfx`, `.gui`, gameplay, localisation, or decision files. Parent integration should register the exact sprite ids and texture paths below. All DDS files already exist at the listed paths and have been exported as uncompressed 32-bit BGRA with real alpha.

## Doctrine adoption icons

Target file: `interface/cbrn_doctrine.gfx`. All are single-frame `64x64` sprites.

| Sprite id | Exact texture path |
|---|---|
| `GFX_doctrine_chaos_warfare_medium` | `gfx/interface/doctrines/icons/stage_5_chaos_warfare/doctrine_chaos_warfare.dds` |
| `GFX_doctrine_extermination_columns_medium` | `gfx/interface/doctrines/icons/stage_5_chaos_warfare/doctrine_hazard_assault_formations.dds` |
| `GFX_doctrine_chemical_suppression_medium` | `gfx/interface/doctrines/icons/stage_5_chaos_warfare/doctrine_toxic_armored_warfare.dds` |
| `GFX_doctrine_contaminant_firebases_medium` | `gfx/interface/doctrines/icons/stage_5_chaos_warfare/doctrine_contaminant_fire_support.dds` |
| `GFX_doctrine_integrated_chemical_operations_medium` | `gfx/interface/doctrines/icons/stage_5_chaos_warfare/doctrine_integrated_cbrn_command.dds` |

Copy pattern:

```text
spriteType = {
	name = "GFX_doctrine_chaos_warfare_medium"
	texturefile = "gfx/interface/doctrines/icons/stage_5_chaos_warfare/doctrine_chaos_warfare.dds"
}
```

## Mastery reward strips

Target file: `interface/cbrn_doctrine.gfx`. Each DDS is `1000x88` with `noOfFrames = 10`; horizontal frames are 100x88. Frames 1-5 are active concepts in mastery order. Frames 6-10 are the matching disabled variants in the same order.

| Sprite id | Exact texture path | Mastery order |
|---|---|---|
| `GFX_cbrn_doctrine_hazard_assault_reward_strip` | `gfx/interface/doctrines/rewards/stage_5_chaos_warfare/hazard_assault_reward_strip.dds` | Mask Discipline; Contaminated Terrain Movement; Chaos Assault Battalion; Shock Exploitation Columns; Terminal Hazard Offensive |
| `GFX_cbrn_doctrine_toxic_armor_reward_strip` | `gfx/interface/doctrines/rewards/stage_5_chaos_warfare/toxic_armor_reward_strip.dds` | Sealed Crew Compartments; Armored Agent Delivery; Mobile Nerve Suppression; Protected Breakthrough Logistics; Catastrophic Shock Breakthrough |
| `GFX_cbrn_doctrine_contaminant_fire_reward_strip` | `gfx/interface/doctrines/rewards/stage_5_chaos_warfare/contaminant_fire_reward_strip.dds` | Projector Fire-Control Cells; Counterbattery Chemical Fire; Chemical Shell Logistics; Persistent Agent Distribution; Deep Contamination Fire Plan |
| `GFX_cbrn_doctrine_integrated_command_reward_strip` | `gfx/interface/doctrines/rewards/stage_5_chaos_warfare/integrated_command_reward_strip.dds` | Chemical Intelligence and Weather Cells; Protected Signal Networks; Countercontamination Routing; Air-Surface and Biological Coordination; Theater CBRN Overmatch |

Copy pattern:

```text
spriteType = {
	name = "GFX_cbrn_doctrine_hazard_assault_reward_strip"
	texturefile = "gfx/interface/doctrines/rewards/stage_5_chaos_warfare/hazard_assault_reward_strip.dds"
	noOfFrames = 10
}
```

## Grand-doctrine milestone sheets

Target file: `interface/cbrn_doctrine.gfx`. Each DDS is `212x83` with `noOfFrames = 2`; active is x=0 and disabled is x=106, each frame 106x83.

| Sprite id | Exact texture path | Related milestone |
|---|---|---|
| `GFX_cbrn_doctrine_milestone_protective_foundation` | `gfx/interface/doctrines/milestones/stage_5_chaos_warfare/protective_foundation.dds` | Protective Foundation |
| `GFX_cbrn_doctrine_milestone_delivery_integration` | `gfx/interface/doctrines/milestones/stage_5_chaos_warfare/delivery_integration.dds` | Delivery Integration |
| `GFX_cbrn_doctrine_milestone_theater_exploitation` | `gfx/interface/doctrines/milestones/stage_5_chaos_warfare/theater_exploitation.dds` | Theater Exploitation |
| `GFX_cbrn_doctrine_milestone_terminal_command` | `gfx/interface/doctrines/milestones/stage_5_chaos_warfare/terminal_command.dds` | Terminal Command |

Copy pattern:

```text
spriteType = {
	name = "GFX_cbrn_doctrine_milestone_protective_foundation"
	texturefile = "gfx/interface/doctrines/milestones/stage_5_chaos_warfare/protective_foundation.dds"
	noOfFrames = 2
}
```

## Officer-corps spirits

Target file: `interface/cbrn_doctrine.gfx`. Every DDS is one transparent, unframed `45x45` sprite.

| Sprite id | Exact texture path | Related spirit |
|---|---|---|
| `GFX_idea_chemical_command_reagent_optimization_spirit` | `gfx/interface/officer_corp/spirits/stage_5_chaos_warfare/controlled_retaliation_doctrine.dds` | Controlled Retaliation Doctrine |
| `GFX_idea_cbrn_theater_contamination_doctrine_spirit` | `gfx/interface/officer_corp/spirits/stage_5_chaos_warfare/theater_contamination_doctrine.dds` | Theater Contamination Doctrine |
| `GFX_idea_cbrn_terminal_hazard_doctrine_spirit` | `gfx/interface/officer_corp/spirits/stage_5_chaos_warfare/terminal_hazard_doctrine.dds` | Terminal Hazard Doctrine |
| `GFX_idea_cbrn_mask_discipline_spirit` | `gfx/interface/officer_corp/spirits/stage_5_chaos_warfare/mask_discipline.dds` | Mask Discipline |
| `GFX_idea_cbrn_hazard_assault_cadres_spirit` | `gfx/interface/officer_corp/spirits/stage_5_chaos_warfare/hazard_assault_cadres.dds` | Hazard Assault Cadres |
| `GFX_idea_chemical_division_contamination_command_spirit` | `gfx/interface/officer_corp/spirits/stage_5_chaos_warfare/contaminant_fire_coordination.dds` | Contaminant Fire Coordination |

## Generic high-command role idea portraits

Target file: `interface/cbrn_doctrine.gfx`. Every DDS is a transparent `60x68` institutional emblem; none depicts an invented person.

| Sprite id | Exact texture path | Related role |
|---|---|---|
| `GFX_idea_cbrn_operations_director` | `gfx/interface/ideas/stage_5_chaos_warfare/cbrn_operations_director.dds` | CBRN Operations Director |
| `GFX_idea_cbrn_civil_defence_coordinator` | `gfx/interface/ideas/stage_5_chaos_warfare/civil_defence_coordinator.dds` | Civil Defence Coordinator |
| `GFX_idea_cbrn_chemical_logistics_inspector` | `gfx/interface/ideas/stage_5_chaos_warfare/chemical_logistics_inspector.dds` | Chemical Logistics Inspector |
| `GFX_idea_cbrn_biological_security_director` | `gfx/interface/ideas/stage_5_chaos_warfare/biological_security_director.dds` | Biological Security Director |

## Prepared-command trait

Target file: `interface/chaosx_traits.gfx`. One transparent `23x33` sprite.

| Sprite id | Exact texture path |
|---|---|
| `GFX_trait_chemical_operations_commander` | `gfx/interface/traits/stage_5_chaos_warfare/trait_cbrn_operations_commander.dds` |

## Doctrine decisions and missions

Target file: `interface/cbrn_doctrine.gfx`. Every DDS is an independent transparent `32x32` one-frame icon. The source concepts were separately generated for decision-scale readability.

The parent supplied the exact sprite id, runtime DDS path, source path, and processed path for the institutional-review asset.

| Sprite id | Exact texture path | Related decision/mission |
|---|---|---|
| `GFX_decision_cbrn_chaos_warfare_establishment_mission` | `gfx/interface/decisions/stage_5_chaos_warfare/cbrn_chaos_warfare_establishment_mission.dds` | cbrn_chaos_warfare_establishment_mission |
| `GFX_decision_cbrn_complete_delayed_establishment` | `gfx/interface/decisions/stage_5_chaos_warfare/cbrn_complete_delayed_establishment.dds` | cbrn_complete_delayed_establishment |
| `GFX_decision_cbrn_claim_protective_foundation` | `gfx/interface/decisions/stage_5_chaos_warfare/cbrn_claim_protective_foundation.dds` | cbrn_claim_protective_foundation |
| `GFX_decision_cbrn_claim_delivery_integration` | `gfx/interface/decisions/stage_5_chaos_warfare/cbrn_claim_delivery_integration.dds` | cbrn_claim_delivery_integration |
| `GFX_decision_cbrn_claim_theater_exploitation` | `gfx/interface/decisions/stage_5_chaos_warfare/cbrn_claim_theater_exploitation.dds` | cbrn_claim_theater_exploitation |
| `GFX_decision_cbrn_claim_terminal_command` | `gfx/interface/decisions/stage_5_chaos_warfare/cbrn_claim_terminal_command.dds` | cbrn_claim_terminal_command |
| `GFX_decision_cbrn_hazard_assault_training` | `gfx/interface/decisions/stage_5_chaos_warfare/cbrn_hazard_assault_training.dds` | cbrn_hazard_assault_training |
| `GFX_decision_cbrn_set_defensive_preparation_policy` | `gfx/interface/decisions/stage_5_chaos_warfare/cbrn_set_defensive_preparation_policy.dds` | cbrn_set_defensive_preparation_policy |
| `GFX_decision_cbrn_set_retaliation_authority_policy` | `gfx/interface/decisions/stage_5_chaos_warfare/cbrn_set_retaliation_authority_policy.dds` | cbrn_set_retaliation_authority_policy |
| `GFX_decision_cbrn_set_limited_battlefield_policy` | `gfx/interface/decisions/stage_5_chaos_warfare/cbrn_set_limited_battlefield_policy.dds` | cbrn_set_limited_battlefield_policy |
| `GFX_decision_cbrn_set_strategic_release_policy` | `gfx/interface/decisions/stage_5_chaos_warfare/cbrn_set_strategic_release_policy.dds` | cbrn_set_strategic_release_policy |
| `GFX_decision_cbrn_set_unrestricted_policy` | `gfx/interface/decisions/stage_5_chaos_warfare/cbrn_set_unrestricted_policy.dds` | cbrn_set_unrestricted_policy |
| `GFX_decision_cbrn_commission_sealed_tank_crews` | `gfx/interface/decisions/stage_5_chaos_warfare/cbrn_commission_sealed_tank_crews.dds` | cbrn_commission_sealed_tank_crews |
| `GFX_decision_cbrn_commission_persistent_shell_filling` | `gfx/interface/decisions/stage_5_chaos_warfare/cbrn_commission_persistent_shell_filling.dds` | cbrn_commission_persistent_shell_filling |
| `GFX_decision_cbrn_commission_nerve_suppression` | `gfx/interface/decisions/stage_5_chaos_warfare/cbrn_commission_nerve_suppression.dds` | cbrn_commission_nerve_suppression |
| `GFX_decision_cbrn_commission_biological_security_assault` | `gfx/interface/decisions/stage_5_chaos_warfare/cbrn_commission_biological_security_assault.dds` | cbrn_commission_biological_security_assault |
| `GFX_decision_cbrn_assign_decontamination_corridor` | `gfx/interface/decisions/stage_5_chaos_warfare/cbrn_assign_decontamination_corridor.dds` | cbrn_assign_decontamination_corridor |
| `GFX_decision_cbrn_convene_institutional_review` | `gfx/interface/decisions/stage_5_chaos_warfare/cbrn_convene_institutional_review.dds` | cbrn_convene_institutional_review |

Representative copy pattern:

```text
spriteType = {
	name = "GFX_decision_cbrn_hazard_assault_training"
	texturefile = "gfx/interface/decisions/stage_5_chaos_warfare/cbrn_hazard_assault_training.dds"
}
```

```text
spriteType = {
	name = "GFX_decision_cbrn_assign_decontamination_corridor"
	texturefile = "gfx/interface/decisions/stage_5_chaos_warfare/cbrn_assign_decontamination_corridor.dds"
}
```

```text
spriteType = {
	name = "GFX_decision_cbrn_convene_institutional_review"
	texturefile = "gfx/interface/decisions/stage_5_chaos_warfare/cbrn_convene_institutional_review.dds"
}
```

Package source: `source_png/decisions/cbrn_convene_institutional_review_source.png`; alpha master: `source_png/decisions/cbrn_convene_institutional_review_master.png`; processed preview: `processed_png/decisions/cbrn_convene_institutional_review.png`. The source is an independent built-in `$imagegen` capture, keyed from `#ff00ff` because the olive/teal subject conflicted with green keying. No `.gfx` file was edited here.

## Decision-category icon

Target file: `interface/cbrn_doctrine.gfx`. Verified category canvas is `52x40`, one transparent frame. The concept is a wide institutional sealed chemical-operations desk/map, distinct from doctrine medallions and every 32x32 decision.

| Sprite id | Exact texture path | Related category |
|---|---|---|
| `GFX_decision_category_cbrn_chemical_operations` | `gfx/interface/decisions/stage_5_chaos_warfare/cbrn_chemical_operations_category.dds` | cbrn_chemical_operations |

Copy pattern:

```text
spriteType = {
	name = "GFX_decision_category_cbrn_chemical_operations"
	texturefile = "gfx/interface/decisions/stage_5_chaos_warfare/cbrn_chemical_operations_category.dds"
}
```

## Doctrine technology icons

Target file: `interface/cbrn_doctrine.gfx`. Both DDS files are independent transparent `64x64` one-frame technology icons.

| Sprite id | Exact texture path | Related technology |
|---|---|---|
| `GFX_mobile_decontamination_columns_medium` | `gfx/interface/technologies/stage_5_chaos_warfare/cbrn_mobile_decontamination_columns.dds` | mobile_decontamination_columns |
| `GFX_chemical_air_interdiction_medium` | `gfx/interface/technologies/stage_5_chaos_warfare/cbrn_chemical_air_interdiction.dds` | chemical_air_interdiction |

Copy pattern:

```text
spriteType = {
	name = "GFX_mobile_decontamination_columns_medium"
	texturefile = "gfx/interface/technologies/stage_5_chaos_warfare/cbrn_mobile_decontamination_columns.dds"
}
```

```text
spriteType = {
	name = "GFX_chemical_air_interdiction_medium"
	texturefile = "gfx/interface/technologies/stage_5_chaos_warfare/cbrn_chemical_air_interdiction.dds"
}
```

## Review surfaces and risk

- Contact sheets: `contact_sheets/doctrine_contact_sheet_checker.png`, `rewards_contact_sheet_checker.png`, `milestones_contact_sheet_checker.png`, `spirits_contact_sheet_checker.png`, `roles_contact_sheet_checker.png`, `trait_contact_sheet_checker.png`, `decisions_contact_sheet_checker.png`, `category_contact_sheet_checker.png`, `technology_contact_sheet_checker.png`.
- `notes/dimension_alpha_validation.tsv` records every processed PNG’s exact dimensions and alpha extrema.
- No assets are blocked or marked `needs_user_review`. Parent-owned `.gfx` registration and gameplay references are the only remaining integration steps; the runtime paths and sprite ids above are authoritative.
