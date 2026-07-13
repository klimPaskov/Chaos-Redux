# Chaos Warfare Stage 5 doctrine and officer-corps asset manifest

Package: `docs/assets/chaos_warfare_system/stage_5_doctrine_officer_corps/`  
System: `chaos_warfare_system`  
Stage: 5 doctrine adoption, mastery rewards, milestones, officer-corps spirits, high-command roles, prepared-command trait, doctrine decisions, and CBRN chemical-operations category  
Production date: 2026-07-14

Visible concept count: **60** — 5 doctrine adoption icons, 20 mastery rewards, 4 milestone concepts, 6 officer-corps spirits, 4 institutional role portraits, 1 prepared-command trait, 17 decision/mission icons, 1 decision-category icon, and 2 doctrine technology icons. Runtime DDS count is **44** because the 20 rewards are four 10-frame strips and the four milestones are four 2-frame sheets.

## Production contract

- Source mode for every visible concept: built-in `$imagegen` generated source capture. No real people, archival photographs, or historical company logos were used.
- Full generation prompt set: [prompts/asset_prompts.md](prompts/asset_prompts.md). Each row below records the concept-specific prompt delta and its source PNG. All captures used a uniform `#00ff00` chroma-key background, then the official `remove_chroma_key.py` helper with border auto-key, soft matte, thresholds 12/220, and despill to create the alpha-bearing `_master.png` source.
- Exact-size processing: [notes/process_stage_5_assets.py](notes/process_stage_5_assets.py). The processor crops the alpha subject, fits it to the native canvas, preserves transparent unused pixels, creates explicit grayscale disabled states only where the runtime sheet requires them, assembles sheets, writes contact sheets, and exports DDS.
- DDS contract: uncompressed 32-bit BGRA/B8G8R8A8-style DDS; header flags `135183`, pixel-format flags `65`, fourcc `0`, bit count `32`, masks `00FF0000/0000FF00/000000FF/FF000000`, no mipmaps. All final icons use real alpha.
- Disabled reward and milestone frames are state derivatives of the matching generated concept, not separate visible concepts and not substitutes for any other icon type.
- Status vocabulary: `complete` means source PNG, alpha master, processed PNG(s), final runtime DDS, contact-sheet coverage, and GFX handoff are present. Parent wiring remains `planned` because this package did not edit `.gfx` files.

## A. Doctrine adoption icons — 64x64

| Concept / provenance prompt | Source PNG -> processed PNG | Final runtime DDS | Sprite / target `.gfx` | Related / frames / processing / status |
|---|---|---|---|---|
| **Chaos Warfare** — respirator command seal with filter, hose, weather vane, map fold | `source_png/doctrine/doctrine_chaos_warfare_source.png` -> `processed_png/doctrine/doctrine_chaos_warfare.png` | `gfx/interface/doctrines/icons/stage_5_chaos_warfare/doctrine_chaos_warfare.dds` | `GFX_doctrine_chaos_warfare_medium` / `interface/cbrn_doctrine.gfx` | Adoption icon; 64x64, 1 frame; transparent crop; complete |
| **Hazard Assault Formations** — sealed helmet/mask behind breaching shield and pioneer stake | `source_png/doctrine/doctrine_hazard_assault_formations_source.png` -> `processed_png/doctrine/doctrine_hazard_assault_formations.png` | `gfx/interface/doctrines/icons/stage_5_chaos_warfare/doctrine_hazard_assault_formations.dds` | `GFX_doctrine_extermination_columns_medium` / `interface/cbrn_doctrine.gfx` | Infantry-track adoption; 64x64, 1 frame; distinct generated concept; complete |
| **Toxic Armored Warfare** — sealed armored turret, delivery canister, track segment | `source_png/doctrine/doctrine_toxic_armored_warfare_source.png` -> `processed_png/doctrine/doctrine_toxic_armored_warfare.png` | `gfx/interface/doctrines/icons/stage_5_chaos_warfare/doctrine_toxic_armored_warfare.dds` | `GFX_doctrine_chemical_suppression_medium` / `interface/cbrn_doctrine.gfx` | Armor-track adoption; 64x64, 1 frame; mechanical silhouette; complete |
| **Contaminant Fire Support** — chemical shell, guarded loading cradle, projector nozzle | `source_png/doctrine/doctrine_contaminant_fire_support_source.png` -> `processed_png/doctrine/doctrine_contaminant_fire_support.png` | `gfx/interface/doctrines/icons/stage_5_chaos_warfare/doctrine_contaminant_fire_support.dds` | `GFX_doctrine_contaminant_firebases_medium` / `interface/cbrn_doctrine.gfx` | Combat-support adoption; 64x64, 1 frame; no explosion; complete |
| **Integrated CBRN Command** — command map case, weather mast, telephone, sealed sample canister | `source_png/doctrine/doctrine_integrated_cbrn_command_source.png` -> `processed_png/doctrine/doctrine_integrated_cbrn_command.png` | `gfx/interface/doctrines/icons/stage_5_chaos_warfare/doctrine_integrated_cbrn_command.dds` | `GFX_doctrine_integrated_chemical_operations_medium` / `interface/cbrn_doctrine.gfx` | Operations-track adoption; 64x64, 1 frame; complete |

Contact sheet: `contact_sheets/doctrine_contact_sheet_checker.png`.

## B. Mastery rewards — 20 unique 100x88 concepts in four 1000x88 strips

Frames 1-5 are active in mastery order; frames 6-10 are the matching disabled/grayed versions in the same order. Each row has its own generated source concept and two processed state PNGs. The final runtime DDS is the named strip with the row’s active/disabled frame slots.

### Hazard Assault Formations

| Concept / provenance prompt | Source PNG -> processed PNGs | Final strip / frame slots | Sprite / target `.gfx` | Related / status |
|---|---|---|---|---|
| **Mask Discipline** — fitted respirator, clipped filter, inspection brush | `source_png/rewards/mask_discipline_reward_source.png` -> `processed_png/rewards/hazard_assault/mask_discipline_reward_{active,disabled}.png` | `gfx/interface/doctrines/rewards/stage_5_chaos_warfare/hazard_assault_reward_strip.dds`; active 1, disabled 6 | `GFX_cbrn_doctrine_hazard_assault_reward_strip` / `interface/cbrn_doctrine.gfx` | Infantry M1; 100x88 each, strip 1000x88, 10 frames; complete |
| **Contaminated Terrain Movement** — tracked pioneer cart, stained route marker, sealed boot | `source_png/rewards/contaminated_terrain_movement_reward_source.png` -> `processed_png/rewards/hazard_assault/contaminated_terrain_movement_reward_{active,disabled}.png` | same strip; active 2, disabled 7 | same sprite / same `.gfx` | Infantry M2; complete |
| **Chaos Assault Battalion** — protected breaching shield, sealed visor, reinforced ram | `source_png/rewards/chaos_assault_battalion_reward_source.png` -> `processed_png/rewards/hazard_assault/chaos_assault_battalion_reward_{active,disabled}.png` | same strip; active 3, disabled 8 | same sprite / same `.gfx` | Infantry M3; complete |
| **Shock Exploitation Columns** — two sealed trucks and forward signal pennant | `source_png/rewards/shock_exploitation_columns_reward_source.png` -> `processed_png/rewards/hazard_assault/shock_exploitation_columns_reward_{active,disabled}.png` | same strip; active 4, disabled 9 | same sprite / same `.gfx` | Infantry M4; complete |
| **Terminal Hazard Offensive** — locked offensive canister, assault shield, command whistle | `source_png/rewards/terminal_hazard_offensive_reward_source.png` -> `processed_png/rewards/hazard_assault/terminal_hazard_offensive_reward_{active,disabled}.png` | same strip; active 5, disabled 10 | same sprite / same `.gfx` | Infantry M5; complete |

### Toxic Armored Warfare

| Concept / provenance prompt | Source PNG -> processed PNGs | Final strip / frame slots | Sprite / target `.gfx` | Related / status |
|---|---|---|---|---|
| **Sealed Crew Compartments** — armored hatch gasket, overpressure valve, filter housing | `source_png/rewards/sealed_crew_compartments_reward_source.png` -> `processed_png/rewards/toxic_armor/sealed_crew_compartments_reward_{active,disabled}.png` | `gfx/interface/doctrines/rewards/stage_5_chaos_warfare/toxic_armor_reward_strip.dds`; active 1, disabled 6 | `GFX_cbrn_doctrine_toxic_armor_reward_strip` / `interface/cbrn_doctrine.gfx` | Armor M1; 100x88 each, strip 1000x88; complete |
| **Armored Agent Delivery** — low-profile delivery vehicle, shielded cylinders, hose coupling | `source_png/rewards/armored_agent_delivery_reward_source.png` -> `processed_png/rewards/toxic_armor/armored_agent_delivery_reward_{active,disabled}.png` | same strip; active 2, disabled 7 | same sprite / same `.gfx` | Armor M2; complete |
| **Mobile Nerve Suppression** — locked canister, respirator hood, blank warning pennant | `source_png/rewards/mobile_nerve_suppression_reward_source.png` -> `processed_png/rewards/toxic_armor/mobile_nerve_suppression_reward_{active,disabled}.png` | same strip; active 3, disabled 8 | same sprite / same `.gfx` | Armor M3; complete |
| **Protected Breakthrough Logistics** — tracked supply carrier, fuel drum, filter crate | `source_png/rewards/protected_breakthrough_logistics_reward_source.png` -> `processed_png/rewards/toxic_armor/protected_breakthrough_logistics_reward_{active,disabled}.png` | same strip; active 4, disabled 9 | same sprite / same `.gfx` | Armor M4; complete |
| **Catastrophic Shock Breakthrough** — armored ram, sealed gate, locked payload case | `source_png/rewards/catastrophic_shock_breakthrough_reward_source.png` -> `processed_png/rewards/toxic_armor/catastrophic_shock_breakthrough_reward_{active,disabled}.png` | same strip; active 5, disabled 10 | same sprite / same `.gfx` | Armor M5; complete |

### Contaminant Fire Support

| Concept / provenance prompt | Source PNG -> processed PNGs | Final strip / frame slots | Sprite / target `.gfx` | Related / status |
|---|---|---|---|---|
| **Projector Fire-Control Cells** — twin projector tubes, elevation wheel, field telephone | `source_png/rewards/projector_fire_control_cells_reward_source.png` -> `processed_png/rewards/contaminant_fire/projector_fire_control_cells_reward_{active,disabled}.png` | `gfx/interface/doctrines/rewards/stage_5_chaos_warfare/contaminant_fire_reward_strip.dds`; active 1, disabled 6 | `GFX_cbrn_doctrine_contaminant_fire_reward_strip` / `interface/cbrn_doctrine.gfx` | Fire M1; 100x88 each, strip 1000x88; complete |
| **Counterbattery Chemical Fire** — shell, counterbattery compass, shielded distant muzzle | `source_png/rewards/counterbattery_chemical_fire_reward_source.png` -> `processed_png/rewards/contaminant_fire/counterbattery_chemical_fire_reward_{active,disabled}.png` | same strip; active 2, disabled 7 | same sprite / same `.gfx` | Fire M2; complete |
| **Chemical Shell Logistics** — sealed-shell rack, handling gloves, unreadable crates | `source_png/rewards/chemical_shell_logistics_reward_source.png` -> `processed_png/rewards/contaminant_fire/chemical_shell_logistics_reward_{active,disabled}.png` | same strip; active 3, disabled 8 | same sprite / same `.gfx` | Fire M3; complete |
| **Persistent Agent Distribution** — guarded round, filling nozzle, hose loop | `source_png/rewards/persistent_agent_distribution_reward_source.png` -> `processed_png/rewards/contaminant_fire/persistent_agent_distribution_reward_{active,disabled}.png` | same strip; active 4, disabled 9 | same sprite / same `.gfx` | Fire M4; complete |
| **Deep Contamination Fire Plan** — shell, weather vane, layered unmarked plotting sheets | `source_png/rewards/deep_contamination_fire_plan_reward_source.png` -> `processed_png/rewards/contaminant_fire/deep_contamination_fire_plan_reward_{active,disabled}.png` | same strip; active 5, disabled 10 | same sprite / same `.gfx` | Fire M5; complete |

### Integrated CBRN Command

| Concept / provenance prompt | Source PNG -> processed PNGs | Final strip / frame slots | Sprite / target `.gfx` | Related / status |
|---|---|---|---|---|
| **Chemical Intelligence and Weather Cells** — anemometer, barometer, balloon reel, sample jar | `source_png/rewards/chemical_intelligence_weather_cells_reward_source.png` -> `processed_png/rewards/integrated_command/chemical_intelligence_weather_cells_reward_{active,disabled}.png` | `gfx/interface/doctrines/rewards/stage_5_chaos_warfare/integrated_command_reward_strip.dds`; active 1, disabled 6 | `GFX_cbrn_doctrine_integrated_command_reward_strip` / `interface/cbrn_doctrine.gfx` | Command M1; 100x88 each, strip 1000x88; complete |
| **Protected Signal Networks** — field telephone, switchboard plugs, shielded cables | `source_png/rewards/protected_signal_networks_reward_source.png` -> `processed_png/rewards/integrated_command/protected_signal_networks_reward_{active,disabled}.png` | same strip; active 2, disabled 7 | same sprite / same `.gfx` | Command M2; complete |
| **Countercontamination Routing** — wash hose, route stakes, wheeled spray cart | `source_png/rewards/countercontamination_routing_reward_source.png` -> `processed_png/rewards/integrated_command/countercontamination_routing_reward_{active,disabled}.png` | same strip; active 3, disabled 8 | same sprite / same `.gfx` | Command M3; complete |
| **Air-Surface and Biological Coordination** — aircraft silhouette, command board, sample vial, radio | `source_png/rewards/air_surface_biological_coordination_reward_source.png` -> `processed_png/rewards/integrated_command/air_surface_biological_coordination_reward_{active,disabled}.png` | same strip; active 4, disabled 9 | same sprite / same `.gfx` | Command M4; complete |
| **Theater CBRN Overmatch** — integrated command case with respirator, weather, shell, medical, decon cues | `source_png/rewards/theater_cbrn_overmatch_reward_source.png` -> `processed_png/rewards/integrated_command/theater_cbrn_overmatch_reward_{active,disabled}.png` | same strip; active 5, disabled 10 | same sprite / same `.gfx` | Command M5; complete |

Contact sheets: `contact_sheets/rewards_contact_sheet_checker.png` plus the family-wide review sheet for active/disabled states. Runtime strips are the four exact 1000x88 DDS files above.

## C. Grand-doctrine milestone sprites — 106x83 active + 106x83 disabled

| Concept / provenance prompt | Source PNG -> processed states / sheet | Final runtime DDS | Sprite / target `.gfx` | Frame layout / related / status |
|---|---|---|---|---|
| **Protective Foundation** — respirator issue table, filter crates, inspection seal | `source_png/milestones/protective_foundation_source.png` -> `processed_png/milestones/protective_foundation_{active,disabled}.png`, `protective_foundation_milestone_sheet.png` | `gfx/interface/doctrines/milestones/stage_5_chaos_warfare/protective_foundation.dds` | `GFX_cbrn_doctrine_milestone_protective_foundation` / `interface/cbrn_doctrine.gfx` | 212x83, active x=0, disabled x=106; complete |
| **Delivery Integration** — armored delivery vehicle coupled to shell cart | `source_png/milestones/delivery_integration_source.png` -> `processed_png/milestones/delivery_integration_{active,disabled}.png`, `delivery_integration_milestone_sheet.png` | `gfx/interface/doctrines/milestones/stage_5_chaos_warfare/delivery_integration.dds` | `GFX_cbrn_doctrine_milestone_delivery_integration` / `interface/cbrn_doctrine.gfx` | 212x83, active x=0, disabled x=106; complete |
| **Theater Exploitation** — wash lane, weather mast, unmarked map, convoy | `source_png/milestones/theater_exploitation_source.png` -> `processed_png/milestones/theater_exploitation_{active,disabled}.png`, `theater_exploitation_milestone_sheet.png` | `gfx/interface/doctrines/milestones/stage_5_chaos_warfare/theater_exploitation.dds` | `GFX_cbrn_doctrine_milestone_theater_exploitation` / `interface/cbrn_doctrine.gfx` | 212x83, active x=0, disabled x=106; complete |
| **Terminal Command** — hardened command table, respirator, telephone, locked hazard case | `source_png/milestones/terminal_command_source.png` -> `processed_png/milestones/terminal_command_{active,disabled}.png`, `terminal_command_milestone_sheet.png` | `gfx/interface/doctrines/milestones/stage_5_chaos_warfare/terminal_command.dds` | `GFX_cbrn_doctrine_milestone_terminal_command` / `interface/cbrn_doctrine.gfx` | 212x83, active x=0, disabled x=106; complete |

Contact sheet: `contact_sheets/milestones_contact_sheet_checker.png`.

## D. Officer-corps spirits — 45x45 transparent, unframed

| Concept / provenance prompt | Source PNG -> processed PNG | Final runtime DDS | Sprite / target `.gfx` | Related / processing / status |
|---|---|---|---|---|
| **Controlled Retaliation Doctrine** — balanced respirator, shield, closed valve | `source_png/spirits/controlled_retaliation_doctrine_source.png` -> `processed_png/spirits/controlled_retaliation_doctrine.png` | `gfx/interface/officer_corp/spirits/stage_5_chaos_warfare/controlled_retaliation_doctrine.dds` | `GFX_idea_chemical_command_reagent_optimization_spirit` / `interface/cbrn_doctrine.gfx` | Army command spirit; 45x45, transparent/unframed; complete |
| **Theater Contamination Doctrine** — canister, route fold, decon hose | `source_png/spirits/theater_contamination_doctrine_source.png` -> `processed_png/spirits/theater_contamination_doctrine.png` | `gfx/interface/officer_corp/spirits/stage_5_chaos_warfare/theater_contamination_doctrine.dds` | `GFX_idea_cbrn_theater_contamination_doctrine_spirit` / `interface/cbrn_doctrine.gfx` | Army command spirit; complete |
| **Terminal Hazard Doctrine** — locked case, visor, command bolt | `source_png/spirits/terminal_hazard_doctrine_source.png` -> `processed_png/spirits/terminal_hazard_doctrine.png` | `gfx/interface/officer_corp/spirits/stage_5_chaos_warfare/terminal_hazard_doctrine.dds` | `GFX_idea_cbrn_terminal_hazard_doctrine_spirit` / `interface/cbrn_doctrine.gfx` | Army command spirit; complete |
| **Mask Discipline** — fitted respirator, clipped filter, inspection tab | `source_png/spirits/mask_discipline_source.png` -> `processed_png/spirits/mask_discipline.png` | `gfx/interface/officer_corp/spirits/stage_5_chaos_warfare/mask_discipline.dds` | `GFX_idea_cbrn_mask_discipline_spirit` / `interface/cbrn_doctrine.gfx` | Division command spirit; complete |
| **Hazard Assault Cadres** — breaching shield, sealed visor, pioneer ram | `source_png/spirits/hazard_assault_cadres_source.png` -> `processed_png/spirits/hazard_assault_cadres.png` | `gfx/interface/officer_corp/spirits/stage_5_chaos_warfare/hazard_assault_cadres.dds` | `GFX_idea_cbrn_hazard_assault_cadres_spirit` / `interface/cbrn_doctrine.gfx` | Division command spirit; complete |
| **Contaminant Fire Coordination** — projector, shell, telephone, command cable | `source_png/spirits/contaminant_fire_coordination_source.png` -> `processed_png/spirits/contaminant_fire_coordination.png` | `gfx/interface/officer_corp/spirits/stage_5_chaos_warfare/contaminant_fire_coordination.dds` | `GFX_idea_chemical_division_contamination_command_spirit` / `interface/cbrn_doctrine.gfx` | Division command spirit; complete |

Contact sheet: `contact_sheets/spirits_contact_sheet_checker.png`.

## E. Generic high-command role idea portraits — 60x68

These are institutional role emblems, not invented people or portraits.

| Concept / provenance prompt | Source PNG -> processed PNG | Final runtime DDS | Sprite / target `.gfx` | Related / status |
|---|---|---|---|---|
| **CBRN Operations Director** — command desk, respirator, map case, telephone, director seal | `source_png/roles/cbrn_operations_director_source.png` -> `processed_png/roles/cbrn_operations_director.png` | `gfx/interface/ideas/stage_5_chaos_warfare/cbrn_operations_director.dds` | `GFX_idea_cbrn_operations_director` / `interface/cbrn_doctrine.gfx` | Generic high-command role; 60x68, transparent; complete |
| **Civil Defence Coordinator** — mask issue table, shelter lantern, medical cross plate | `source_png/roles/civil_defence_coordinator_source.png` -> `processed_png/roles/civil_defence_coordinator.png` | `gfx/interface/ideas/stage_5_chaos_warfare/civil_defence_coordinator.dds` | `GFX_idea_cbrn_civil_defence_coordinator` / `interface/cbrn_doctrine.gfx` | Generic high-command role; complete |
| **Chemical Logistics Inspector** — sealed shell crate, calipers, filter canister, inspection lamp | `source_png/roles/chemical_logistics_inspector_source.png` -> `processed_png/roles/chemical_logistics_inspector.png` | `gfx/interface/ideas/stage_5_chaos_warfare/chemical_logistics_inspector.dds` | `GFX_idea_cbrn_chemical_logistics_inspector` / `interface/cbrn_doctrine.gfx` | Generic high-command role; complete |
| **Biological Security Director** — specimen cabinet, microscope, medical seal, security key | `source_png/roles/biological_security_director_source.png` -> `processed_png/roles/biological_security_director.png` | `gfx/interface/ideas/stage_5_chaos_warfare/biological_security_director.dds` | `GFX_idea_cbrn_biological_security_director` / `interface/cbrn_doctrine.gfx` | Generic high-command role; complete |

Contact sheet: `contact_sheets/roles_contact_sheet_checker.png`.

## F. Prepared-command leader trait — 23x33

| Concept / provenance prompt | Source PNG -> processed PNG | Final runtime DDS | Sprite / target `.gfx` | Related / status |
|---|---|---|---|---|
| **CBRN Operations Commander** — whistle, respirator filter, map-pin cluster on brass badge | `source_png/trait/trait_cbrn_operations_commander_source.png` -> `processed_png/trait/trait_cbrn_operations_commander.png` | `gfx/interface/traits/stage_5_chaos_warfare/trait_cbrn_operations_commander.dds` | `GFX_trait_chemical_operations_commander` / `interface/chaosx_traits.gfx` | Prepared-command leader trait; 23x33, transparent; complete |

Contact sheet: `contact_sheets/trait_contact_sheet_checker.png`.

## G. Doctrine decisions and missions — 32x32

All entries below are independent generated decision concepts, not resized doctrine, category, milestone, spirit, or idea art.

| Decision / provenance prompt | Source PNG -> processed PNG | Final runtime DDS | Sprite / target `.gfx` | Related / status |
|---|---|---|---|---|
| **Chaos Warfare Establishment Mission** — opened respirator crate, checklist shapes, commissioning seal | `source_png/decisions/cbrn_chaos_warfare_establishment_mission_source.png` -> `processed_png/decisions/cbrn_chaos_warfare_establishment_mission.png` | `gfx/interface/decisions/stage_5_chaos_warfare/cbrn_chaos_warfare_establishment_mission.dds` | `GFX_decision_cbrn_chaos_warfare_establishment_mission` / `interface/cbrn_doctrine.gfx` | Establishment mission; 32x32; complete |
| **Complete Delayed Establishment** — latched sealed crate, fitted mask, field clock | `source_png/decisions/cbrn_complete_delayed_establishment_source.png` -> `processed_png/decisions/cbrn_complete_delayed_establishment.png` | `gfx/interface/decisions/stage_5_chaos_warfare/cbrn_complete_delayed_establishment.dds` | `GFX_decision_cbrn_complete_delayed_establishment` / `interface/cbrn_doctrine.gfx` | Establishment completion; complete |
| **Claim Protective Foundation** — respirator, filter crate, foundation plate, seal | `source_png/decisions/cbrn_claim_protective_foundation_source.png` -> `processed_png/decisions/cbrn_claim_protective_foundation.png` | `gfx/interface/decisions/stage_5_chaos_warfare/cbrn_claim_protective_foundation.dds` | `GFX_decision_cbrn_claim_protective_foundation` / `interface/cbrn_doctrine.gfx` | Milestone claim; complete |
| **Claim Delivery Integration** — armored hose coupling, shell cart, integration pin | `source_png/decisions/cbrn_claim_delivery_integration_source.png` -> `processed_png/decisions/cbrn_claim_delivery_integration.png` | `gfx/interface/decisions/stage_5_chaos_warfare/cbrn_claim_delivery_integration.dds` | `GFX_decision_cbrn_claim_delivery_integration` / `interface/cbrn_doctrine.gfx` | Milestone claim; complete |
| **Claim Theater Exploitation** — wash column, route stake, convoy wheel, map fold | `source_png/decisions/cbrn_claim_theater_exploitation_source.png` -> `processed_png/decisions/cbrn_claim_theater_exploitation.png` | `gfx/interface/decisions/stage_5_chaos_warfare/cbrn_claim_theater_exploitation.dds` | `GFX_decision_cbrn_claim_theater_exploitation` / `interface/cbrn_doctrine.gfx` | Milestone claim; complete |
| **Claim Terminal Command** — locked command case, visor, terminal brass bolt | `source_png/decisions/cbrn_claim_terminal_command_source.png` -> `processed_png/decisions/cbrn_claim_terminal_command.png` | `gfx/interface/decisions/stage_5_chaos_warfare/cbrn_claim_terminal_command.dds` | `GFX_decision_cbrn_claim_terminal_command` / `interface/cbrn_doctrine.gfx` | Milestone claim; complete |
| **Hazard Assault Training** — two protected training helmets behind hazard-field exercise lane, stakes, whistle | `source_png/decisions/cbrn_hazard_assault_training_source.png` -> `processed_png/decisions/cbrn_hazard_assault_training.png` | `gfx/interface/decisions/stage_5_chaos_warfare/cbrn_hazard_assault_training.dds` | `GFX_decision_cbrn_hazard_assault_training` / `interface/cbrn_doctrine.gfx` | Unique infantry training mission; 32x32; complete |
| **Set Defensive Preparation Policy** — closed valve, respirator, shelter lantern | `source_png/decisions/cbrn_set_defensive_preparation_policy_source.png` -> `processed_png/decisions/cbrn_set_defensive_preparation_policy.png` | `gfx/interface/decisions/stage_5_chaos_warfare/cbrn_set_defensive_preparation_policy.dds` | `GFX_decision_cbrn_set_defensive_preparation_policy` / `interface/cbrn_doctrine.gfx` | Policy decision; complete |
| **Set Retaliation Authority Policy** — shielded mask, balanced command scale, sealed response envelope | `source_png/decisions/cbrn_set_retaliation_authority_policy_source.png` -> `processed_png/decisions/cbrn_set_retaliation_authority_policy.png` | `gfx/interface/decisions/stage_5_chaos_warfare/cbrn_set_retaliation_authority_policy.dds` | `GFX_decision_cbrn_set_retaliation_authority_policy` / `interface/cbrn_doctrine.gfx` | Policy decision; complete |
| **Set Limited Battlefield Policy** — shell inside narrow boundary, closed shelter lamp | `source_png/decisions/cbrn_set_limited_battlefield_policy_source.png` -> `processed_png/decisions/cbrn_set_limited_battlefield_policy.png` | `gfx/interface/decisions/stage_5_chaos_warfare/cbrn_set_limited_battlefield_policy.dds` | `GFX_decision_cbrn_set_limited_battlefield_policy` / `interface/cbrn_doctrine.gfx` | Policy decision; complete |
| **Set Strategic Release Policy** — shell, aircraft silhouette, guarded release lever, map | `source_png/decisions/cbrn_set_strategic_release_policy_source.png` -> `processed_png/decisions/cbrn_set_strategic_release_policy.png` | `gfx/interface/decisions/stage_5_chaos_warfare/cbrn_set_strategic_release_policy.dds` | `GFX_decision_cbrn_set_strategic_release_policy` / `interface/cbrn_doctrine.gfx` | Policy decision; complete |
| **Set Unrestricted Policy** — open release lever, payload canisters, dark command lamp | `source_png/decisions/cbrn_set_unrestricted_policy_source.png` -> `processed_png/decisions/cbrn_set_unrestricted_policy.png` | `gfx/interface/decisions/stage_5_chaos_warfare/cbrn_set_unrestricted_policy.dds` | `GFX_decision_cbrn_set_unrestricted_policy` / `interface/cbrn_doctrine.gfx` | Grave policy warning; complete |
| **Commission Sealed Tank Crews** — hatch gasket, filter housing, inspection wrench | `source_png/decisions/cbrn_commission_sealed_tank_crews_source.png` -> `processed_png/decisions/cbrn_commission_sealed_tank_crews.png` | `gfx/interface/decisions/stage_5_chaos_warfare/cbrn_commission_sealed_tank_crews.dds` | `GFX_decision_cbrn_commission_sealed_tank_crews` / `interface/cbrn_doctrine.gfx` | Armor commission; complete |
| **Commission Persistent Shell Filling** — guarded shell rack, filling nozzle, hose valve | `source_png/decisions/cbrn_commission_persistent_shell_filling_source.png` -> `processed_png/decisions/cbrn_commission_persistent_shell_filling.png` | `gfx/interface/decisions/stage_5_chaos_warfare/cbrn_commission_persistent_shell_filling.dds` | `GFX_decision_cbrn_commission_persistent_shell_filling` / `interface/cbrn_doctrine.gfx` | Fire-support commission; complete |
| **Commission Nerve Suppression** — locked canister, hood, heavy key | `source_png/decisions/cbrn_commission_nerve_suppression_source.png` -> `processed_png/decisions/cbrn_commission_nerve_suppression.png` | `gfx/interface/decisions/stage_5_chaos_warfare/cbrn_commission_nerve_suppression.dds` | `GFX_decision_cbrn_commission_nerve_suppression` / `interface/cbrn_doctrine.gfx` | Occupation-use commission; complete |
| **Commission Biological Security Assault** — sealed visor, medical seal, breach bar, specimen case | `source_png/decisions/cbrn_commission_biological_security_assault_source.png` -> `processed_png/decisions/cbrn_commission_biological_security_assault.png` | `gfx/interface/decisions/stage_5_chaos_warfare/cbrn_commission_biological_security_assault.dds` | `GFX_decision_cbrn_commission_biological_security_assault` / `interface/cbrn_doctrine.gfx` | Biological-security commission; complete |
| **Assign Decontamination Corridor** — selected route/state, route pin, stakes, mobile wash column | `source_png/decisions/cbrn_assign_decontamination_corridor_source.png` -> `processed_png/decisions/cbrn_assign_decontamination_corridor.png` | `gfx/interface/decisions/stage_5_chaos_warfare/cbrn_assign_decontamination_corridor.dds` | `GFX_decision_cbrn_assign_decontamination_corridor` / `interface/cbrn_doctrine.gfx` | Unique route assignment decision; 32x32; complete |

Contact sheet: `contact_sheets/decisions_contact_sheet_checker.png`.

## H. Decision-category icon — 52x40

| Concept / provenance prompt | Source PNG -> processed PNG | Final runtime DDS | Sprite / target `.gfx` | Related / processing / status |
|---|---|---|---|---|
| **CBRN Chemical Operations category** — horizontal sealed command desk with unmarked theater map, telephone, weather instrument, capped shell case, brass command seal | `source_png/category/cbrn_chemical_operations_category_source.png` -> `processed_png/category/cbrn_chemical_operations_category.png` | `gfx/interface/decisions/stage_5_chaos_warfare/cbrn_chemical_operations_category.dds` | `GFX_decision_category_cbrn_chemical_operations` / `interface/cbrn_doctrine.gfx` | Verified category canvas 52x40, 1 frame; deliberately wider desk/map composition, not reused from doctrine or decision art; complete |

Contact sheet: `contact_sheets/category_contact_sheet_checker.png`.

## I. Doctrine technology icons — 64x64

These are separately generated technology concepts, not resized HQ support, doctrine, decision, category, or raid icons.

| Technology / provenance prompt | Source PNG -> processed PNG | Final runtime DDS | Sprite / target `.gfx` | Related / processing / status |
|---|---|---|---|---|
| **Mobile Decontamination Columns** — truck-mounted wash/decontamination column with pump, coiled hoses, spray manifold, and marked clean corridor | `source_png/technology/cbrn_mobile_decontamination_columns_source.png` -> `processed_png/technology/cbrn_mobile_decontamination_columns.png` | `gfx/interface/technologies/stage_5_chaos_warfare/cbrn_mobile_decontamination_columns.dds` | `GFX_mobile_cbrn_decontamination_columns_medium` / `interface/chaosx_techtree.gfx` | 64x64, 1 frame; truck/wash machinery emphasized over HQ command; complete |
| **Chemical Air Interdiction** — aircraft silhouette, sealed payload canister, protected air-ground board, exact-state target marker | `source_png/technology/cbrn_chemical_air_interdiction_source.png` -> `processed_png/technology/cbrn_chemical_air_interdiction.png` | `gfx/interface/technologies/stage_5_chaos_warfare/cbrn_chemical_air_interdiction.dds` | `GFX_chemical_air_interdiction_medium` / `interface/chaosx_techtree.gfx` | 64x64, 1 frame; deliberate selected-state planning, not passive air-region contamination; complete |

Contact sheet: `contact_sheets/technology_contact_sheet_checker.png`.

## Review and validation files

- Contact sheets: `contact_sheets/doctrine_contact_sheet_checker.png`, `rewards_contact_sheet_checker.png`, `milestones_contact_sheet_checker.png`, `spirits_contact_sheet_checker.png`, `roles_contact_sheet_checker.png`, `trait_contact_sheet_checker.png`, `decisions_contact_sheet_checker.png`, `category_contact_sheet_checker.png`, `technology_contact_sheet_checker.png`.
- Exact processed PNG dimension/alpha inventory: [notes/dimension_alpha_validation.tsv](notes/dimension_alpha_validation.tsv).
- Processing source: [notes/process_stage_5_assets.py](notes/process_stage_5_assets.py).
- Parent wiring handoff: [gfx_handoff.md](gfx_handoff.md).
- No unresolved source, processing, dimension, alpha, naming, or path risks remain in this bounded package. `.gfx` registration, gameplay references, localisation, and GUI integration remain parent-owned and intentionally untouched.
