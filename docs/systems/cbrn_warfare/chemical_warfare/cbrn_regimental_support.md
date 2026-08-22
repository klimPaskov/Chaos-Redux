# CBRN regimental support and Chaos Assault Battalion

## Purpose

CBRN regimental support is the division layer of the conditional warfare system. Army Headquarters owns theater preparation and abilities; these units put protection, reconnaissance, decontamination, delivery organization, medical response, and biosecurity inside individual divisions.

Standing formation loads and operational expenditure are separate. Offensive delivery companies carry a generic strategic-agent or filled-shell archetype alongside respirators, decontamination equipment, instruments, support equipment, trucks, projectors, or a flame-role chassis. That standing load creates native shortage scaling but does not identify the agent released. Chemical operations must still select, reserve, and consume the exact national payload before calling the shared exposure pipeline.

Doctrine may reduce the Condemnation increment produced by a valid operation. It does not reduce or erase evidence, attribution, deaths, contamination, medical saturation, or confirmed-use history.

## Division-layer roles

| Role | Identifier | Unlock | Standing purpose |
| --- | --- | --- | --- |
| Gas Mask and Decontamination Detachment | `cbrn_gas_mask_decon_detachment` | `field_decontamination_kits` | primary protection, filter discipline, local cleanup |
| Chemical Reconnaissance Detachment | `cbrn_chemical_recon_detachment` | `chemical_detection_paper` | detection, warning, samples, evidence support |
| Hazard Pioneer Detachment | `cbrn_hazard_pioneer_detachment` | `hazard_pioneer_formation` | contaminated-route and protected breaching work |
| Chemical Projector Battery | `cbrn_chemical_projector_battery` | `livens_projector_tech` | consolidated close-delivery organization |
| Chemical Ammunition Train | `cbrn_chemical_ammunition_train` | `chemical_artillery_shells` | shell-lot handling and artillery preparation |
| Light Armored Chemical Delivery | `cbrn_light_armored_delivery_detachment` | `armored_agent_delivery` | light flame-role delivery chassis |
| Medium Armored Chemical Delivery | `cbrn_medium_armored_delivery_detachment` | `armored_agent_delivery` | medium flame-role delivery chassis |
| Heavy Armored Chemical Delivery | `cbrn_heavy_armored_delivery_detachment` | `armored_agent_delivery` | heavy flame-role delivery chassis |
| Nerve Agent Suppression Detachment | `cbrn_nerve_suppression_detachment` | `nerve_agent_suppression_formation` | gated occupation formation for a later targeted operation |
| Field Epidemiology and Quarantine | `cbrn_field_epidemiology_detachment` | `field_epidemiology_teams` | outbreak detection, tracing, and containment |
| Medical Countermeasure Detachment | `cbrn_medical_countermeasure_detachment` | `mobile_cbrn_hospitals` | treatment, antidote, and mass-casualty organization |
| Biological Security Assault | `cbrn_biosecurity_assault_detachment` | `biological_security_assault_formation` | safe facility capture and evidence preservation |
| Chaos Assault Battalion | `chaos_battalion` | `chaos_battalion_tech` | protected line special force for difficult and contaminated approaches |

The three armored definitions are chassis variants of one role, not separate agent variants. All offensive chemical-delivery companies share `same_support_type = cbrn_offensive_delivery`, so a division cannot stack projector, armored, and nerve-suppression delivery roles. Armored delivery also shares vanilla's `flame` support type and cannot parachute. The Medical Countermeasure and Biological Security Assault detachments share the vanilla `field_hospital` support type, preventing medical-role stacking while allowing mask/decon and epidemiology support to coexist with them.

## Equipment and shortage behavior

The regimental definitions use the current 1.19 contract: `group = support`, `allowed_battalion_groups`, `category_regimental_support_battalions`, `divisional = no`, `essential`, and `need`. Native reinforcement therefore scales the unit's ordinary statistics when its essential standing equipment is missing.

The exact fully equipped bills and centralized values are in `common/units/cbrn_regimental_support.txt`. They follow the accepted manpower, organization, strength, supply, and equipment bands from the package matrices. The Projector Battery carries 60 strategic-agent lots, the Chemical Ammunition Train carries 120 filled shell lots, each Armored Delivery Detachment carries 60 strategic-agent lots, and the Nerve Suppression Detachment carries 40 strategic-agent lots. The Chaos Assault Battalion consumes infantry equipment, support equipment, masks, decontamination equipment, instruments, and trucks; it has no chemical or biological payload need.

The engine does not expose a division trigger for the fulfillment ratio of one named essential archetype, and one `need` block cannot express “one selected payload class from several alternatives.” No estimator is used. Operation adapters instead validate country/order preparation and exact selected payload stock, apply the accepted 0/25/55/80/100 scripted-effect bands, debit payload, and only then dispatch exposure.

## Technology and doctrine ownership

Researchable defensive support is attached to the equipment and medical branches. Doctrine-only entries have `allow = { always = no }` and are granted by mapped mastery rewards:

- `hazard_pioneer_formation`
- `chaos_battalion_tech`
- `chaos_battalion_1942`
- `chemical_artillery_shells`
- `persistent_agent_shell_filling`
- `armored_agent_delivery`
- `sealed_tank_crews`
- `nerve_agent_suppression_formation`
- `biological_security_assault_formation`

`chaos_battalion_1939` remains a hidden no-bonus compatibility identifier. Improved Chaos Assault Equipment is deliberately bounded: the unit receives a small organization and breakthrough improvement rather than the former universal-arsenal scaling. Its better-protection requirement belongs to the shared exposure calculation and is not approximated with generic combat statistics.

## AI behavior

`common/ai_templates/cbrn_regimental_support.txt` defines four dedicated roles without overriding vanilla infantry or armor role templates:

- `cbrn_protected_infantry`
- `cbrn_chemical_assault`
- `cbrn_armored_assault`
- `cbrn_containment`

The complete target division bill is checked before a role activates. Offensive roles additionally require battlefield-use policy and positive supported chemical payload stock. This stock signal does not authorize an operation. Role ratios abort when their prerequisites disappear. Production strategies raise the registered `decontamination_equipment` and `cbrn_instrument_equipment` category priorities only after a program, emergency, contamination, or outbreak signal; they create no broad periodic country pulse.

Livens research, projector production, armored-delivery variant production, and their template-design pressure all use `cbrn_ai_can_expand_offensive_cbrn_production`. The shared gate requires a stable protective base, sufficient industry, no conventional infantry/support/artillery/motorized deficit, and an accepted retaliatory, battlefield, strategic, or desperate posture. Armored-delivery pressure targets the exact light, medium, and heavy flame-role chassis required by the three consolidated detachments through the vanilla `equipment_variant_production_factor` pattern; it does not increase ordinary tank-chassis minimum factories.

Stage 10 adds the final route-aware country profile weights, preferred delivery/agent posture, and economic stop conditions.

## Legacy safety

Legacy agent-specific projector and chemical-tank identifiers stay parseable for existing templates, but current agent technologies no longer unlock them. Retained Livens definitions share `cbrn_offensive_delivery`; retained chemical tanks share both `cbrn_offensive_delivery` and vanilla's `flame` key and cannot parachute. An old template therefore cannot bypass the consolidated exclusions when it is edited. The stable `chaos_battalion` ID is redefined in place. Passive combat presence of that battalion is not a chemical-release trigger; its former on-action calls are disconnected so no exposure or Condemnation can occur without payload proof.

There is no documented effect that safely removes one named subunit from every arbitrary player template. The compatibility definitions therefore remain inactive and resolvable until the Stage 6 adapter migration is complete. No whole-template replacement or hidden conversion is performed.

## Visual assets and wiring

Source masters, processed PNG files, final DDS files, manifest, contact sheets, and the GFX handoff are stored under `docs/assets/chaos_warfare_system/stage_3_regimental_support/`.

For each of the 13 unit identifiers in the role table:

- large two-frame sheet: `gfx/interface/counters/divisions_large/unit_<identifier>_icon.dds`, 152×42, with separate purposeful 76×42 frames;
- small two-frame sheet: `gfx/interface/counters/divisions_small/onmap_unit_<identifier>_icon.dds`, 60×12, with separately composed 30×12 frames;
- GFX names: `GFX_unit_<identifier>_icon_medium` and `GFX_unit_<identifier>_icon_medium_white`;
- registration file: `interface/chaosx_subuniticons.gfx`.

The small composition is not a resized large icon.

Dedicated 64×64 technology DDS files are registered in `interface/chaosx_techtree.gfx`:

| Technology sprite | DDS path |
| --- | --- |
| `GFX_chaos_battalion_tech_medium` | `gfx/interface/technologies/chaos_battalion.dds` |
| `GFX_chaos_battalion_1942_medium` | `gfx/interface/technologies/chaos_battalion3.dds` |
| `GFX_hazard_pioneer_formation_medium` | `gfx/interface/technologies/cbrn_hazard_pioneer_formation.dds` |
| `GFX_chemical_artillery_shells_medium` | `gfx/interface/technologies/cbrn_chemical_artillery_shells.dds` |
| `GFX_persistent_agent_shell_filling_medium` | `gfx/interface/technologies/cbrn_persistent_agent_shell_filling.dds` |
| `GFX_armored_agent_delivery_medium` | `gfx/interface/technologies/cbrn_armored_agent_delivery.dds` |
| `GFX_sealed_tank_crews_medium` | `gfx/interface/technologies/cbrn_sealed_tank_crews.dds` |
| `GFX_nerve_agent_suppression_formation_medium` | `gfx/interface/technologies/cbrn_nerve_agent_suppression_formation.dds` |
| `GFX_field_epidemiology_teams_medium` | `gfx/interface/technologies/cbrn_field_epidemiology_teams.dds` |
| `GFX_mobile_cbrn_hospitals_medium` | `gfx/interface/technologies/cbrn_mobile_hospitals.dds` |
| `GFX_biological_security_assault_formation_medium` | `gfx/interface/technologies/cbrn_biosecurity_assault_formation.dds` |

## Future integration

- Army Headquarters companies and commander abilities supply the theater layer.
- Doctrine rewards grant all doctrine-only support technologies after their mapped prerequisites.
- Chemical artillery, projector, armored, raid, and other delivery adapters reserve and consume exact payload before the shared exposure pipeline.
- Biological operations activate epidemiology, quarantine, medical, and facility-capture effects while remaining separate from weaponized zombie systems.
- Nerve suppression becomes a targeted occupied-state operation with equipment debit, deaths, contamination, resistance trauma, evidence, attribution, Condemnation, cooldown, and cleanup.
- Route-aware AI, achievements, scripted GUI, final documentation, migration, and package scenario audits complete the later stages.
