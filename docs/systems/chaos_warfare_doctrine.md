# Chaos Warfare doctrine, institutions, and officer corps

## Purpose

Chaos Warfare is a conditional CBRN grand doctrine, not a universal attack tree. Adoption begins a national institution that must prove protective stock, fielded headquarters, and protected formations before offensive authority can expand. Four mastery tracks grant bounded unit, headquarters, logistics, and operation eligibility; actual chemical delivery remains equipment-backed and must use the shared exposure pipeline.

Doctrine may reduce the Condemnation impact of an accepted chemical or biological use. That reduction affects Condemnation only. It never discounts payload consumption, evidence, attribution, deaths, contamination, medical saturation, resistance trauma, domestic war-support penalties, use counters, confirmed-use history, or strategic and mass-casualty public-harm floors.

The implementation is split across:

- `common/doctrines/` for the grand doctrine and four mastery tracks;
- `common/script_constants/cbrn_doctrine_constants.txt` for shared gameplay tuning, with the existing `chem_integrated_operations.condemnation_mult` table retained as the single migration-safe 0.90/0.80/0.70 Condemnation ladder for chemical and biological callers;
- `common/scripted_triggers/cbrn_doctrine_triggers.txt` and `common/scripted_effects/cbrn_doctrine_effects.txt` for reusable gates and state changes;
- `common/decisions/cbrn_doctrine_decisions.txt` for establishment, institutional claims, policy, training, commissions, and exact-state cleanup;
- `common/ideas/cbw_spirits.txt`, `common/ideas/cbrn_high_command.txt`, and the leader-trait files for officer-corps content;
- `interface/cbrn_doctrine.gfx` and `interface/chaosx_traits.gfx` for final runtime assets.

## Adoption and establishment

Chaos Warfare is visible to every country but available only when at least one accepted capability route exists:

- Basic Gas Masks plus a supported chemical-agent technology;
- a completed mapped chemical special project;
- an established CBRN command flag;
- a mapped historical CBRN program profile; or
- an explicit scenario override.

Adoption costs 100 Army Experience. It initializes the shared CBRN model, records the post-adoption mask-production baseline, sets the Chemical Readiness cap to 39, raises readiness to at least 10, activates the Operations HQ Section and defensive support unlocks, grants doctrine-qualified technologies whose gates are already met, and starts a 90-day establishment mission.

Establishment succeeds only while the country has all of the following:

- 500 gas-mask equipment;
- 50 decontamination equipment;
- 100 support equipment;
- at least one fielded CBRN Operations HQ Section; and
- at least one fielded Gas Mask and Decontamination Detachment.

Success records the institution, raises readiness to at least 20, and raises decontamination capacity to at least 20. Timeout leaves the doctrine active, closes offensive gates, caps readiness at 9, and exposes a 14-day remediation decision costing 35 Political Power and 10 Command Power. Remediation repeats the exact establishment proof; it does not waive missing stock or formations.

## Institutional milestones

Native grand-doctrine milestone blocks can record only their corresponding completed track. Exact cross-track requirements therefore use one-time country decisions and no periodic polling.

| Institution | Exact proof | Result |
| --- | --- | --- |
| Protective Foundation | establishment complete; cumulative gas-mask production increased after adoption; 500 live masks; fielded Operations HQ | readiness cap 59; readiness minimum 30; decontamination minimum 30 |
| Delivery Integration | Protective Foundation; Hazard Assault, Contaminant Fire, or Toxic Armor at mastery 2; at least 100 of one supported payload; one successfully completed protected HQ order | readiness cap 74; readiness minimum 45; offensive HQ preparation eligibility |
| Theater Exploitation | Delivery Integration; any two tracks at mastery 3; decontamination capacity 40; fielded Intelligence and Weather Cell | readiness cap 89; readiness minimum 65; exact-state decontamination and theater HQ gates |
| Terminal CBRN Command | Theater Exploitation; all four tracks active; any track at mastery 5; Limited Battlefield Authority or higher; advanced protection technology or explicit equivalent project | readiness cap 100; readiness minimum 85; capstone command gates |

The protected-order history flag is written only after Theater Protective Posture completes preparation successfully. Starting an order that later fails does not qualify.

## Mastery tracks

Each track costs 100 Army Experience. Native mastery comes from fielded mapped units and uses the current doctrine system. Track modifiers are deliberately modest; strong outcomes are operation-, stock-, readiness-, and policy-gated.

| Compatibility ID | Player-facing track | Mastery content |
| --- | --- | --- |
| `extermination_columns` | Hazard Assault Formations | Mask Discipline; contaminated-terrain movement; Chaos Assault Battalion qualification; shock exploitation; terminal hazard-operation eligibility |
| `chemical_suppression` | Toxic Armored Warfare | sealed crews; armored agent delivery; costed nerve-suppression formation; protected breakthrough logistics; synchronized shock eligibility |
| `contaminant_firebases` | Contaminant Fire Support | projector fire control; counterbattery coordination; Chemical Artillery Shells; persistent-agent shell commission; deep-contamination operation eligibility |
| `integrated_chemical_operations` | Integrated CBRN Command | Intelligence and Weather Cell; Protective Logistics; Mobile Decontamination Columns; Chemical Air Interdiction and Biosecurity; Theater CBRN Headquarters |

The legacy `chemical_suppression` track grants no camp, extermination-site, experiment-site, genocide, or Concentration occupation-law infrastructure. Nerve-agent suppression is only an eligibility path; its later operation must consume equipment and record deaths, contamination, resistance trauma, evidence, and severe diplomatic consequences.

### Equipment-backed Hazard Assault Training

Hazard Assault Training requires Hazard Assault Formations, a fielded protected formation, 100 masks, and 10 Army Experience. It removes masks oldest-first, records the actual mask debit, and grants 0.25 daily mastery to Hazard Assault Formations for 30 days. The decision re-enables after 90 days. It does not authorize live-agent use or create exposure.

### Doctrine-only technologies

The doctrine grants or commissions the following non-researchable technologies only after their exact mastery, institution, project, policy, and protection gates are met:

- Hazard Pioneer Formation;
- Chemical Artillery Shells;
- Persistent Agent Shell Filling;
- Armored Agent Delivery;
- Sealed Tank Crews;
- Nerve Agent Suppression Formation;
- Chaos Assault Battalion and Improved Chaos Assault Equipment;
- Mobile Decontamination Columns;
- Chemical Air Interdiction;
- Theater CBRN Headquarters; and
- Biological Security Assault Formation.

Sealed Tank Crews, Persistent Agent Shell Filling, Nerve Agent Suppression, and Biological Security Assault use seven-day commissions costing 25 Political Power and 5 non-refundable Command Power. Losing the prerequisite before completion cancels the grant.

Chemical Air Interdiction is an eligibility marker only in this stage. It creates no passive regional effect, makes no estimate of sortie activity, and cannot contaminate a state. A later selected-state operation must prove execution, consume the selected payload, resolve protection and conditions, and call the shared exposure record. Idle chemical-capable aircraft never contaminate a region.

## Use policy

Policy changes are decisions with a 90-day reassessment lock. Political Power is the native decision cost; Command Power, readiness, institution, and payload stock are checked and debited by the shared doctrine helpers.

| Policy | Political Power | Command Power | Readiness floor | Additional gate |
| --- | ---: | ---: | ---: | --- |
| Defensive Preparation | 15 | 0 | 0 | doctrine adopted |
| Retaliation Authority | 25 | 5 | 10 | doctrine adopted |
| Limited Battlefield Authority | 50 | 15 | 40 | Delivery Integration; 100 of one supported payload |
| Strategic Release Authority | 75 | 25 | 65 | Theater Exploitation; 250 of one supported payload |
| Unrestricted Chaos Warfare | 100 | 40 | 85 | Terminal CBRN Command; 500 of one supported payload |

Policy permits later adapters to pass authorization checks; it never spends a payload or creates exposure by itself. No Chaos Warfare use-policy tier grants nerve-suppression occupation authority. The later CBRN Coercive Security occupation policy is the sole owner of `cbrn_nerve_suppression_policy_authorized`, so the Nerve Agent Suppression Formation commission remains fail-closed until that distinct requirement is present.

## Condemnation-only doctrine mitigation

`cbrn_prepare_chemical_action_record` owns the doctrine lookup so every accepted chemical delivery route receives one consistent multiplier:

- Operations mastery 1: 0.90;
- Operations mastery 4: 0.80;
- Operations mastery 5: 0.70;
- otherwise: 1.00.

The shared exposure calculation applies this value only to the Condemnation base before attribution/public-harm floors. Evidence and attribution are calculated independently. The legacy biological adapter uses the same 0.90/0.80/0.70 ladder only on its Condemnation base; outbreak potency and duration remain at 1.00, Command Power refunds remain zero, use counters increment fully, and domestic war-support penalties remain full-strength.

## Exact-state decontamination assignment

An active Army HQ Decontamination Corridor plus Theater Exploitation exposes a state-targeted assignment decision. It requires a controlled state with actual chemical contamination and permits one national assignment every 28 days. Cleanup output depends on the current contamination class:

- Trace or Local: 10 points;
- Serious: 8 points;
- Severe: 5 points;
- Catastrophic: 3 points.

The Theater Contamination Doctrine spirit multiplies this output by 1.25. The effect calls the state contamination ledger and records only the amount actually removed. It does not erase evidence, attribution, deaths, Condemnation, or confirmed-use history. Current script cannot bind one active HQ order to several simultaneous state decisions safely, so the national 28-day assignment lock is the conservative exact-state boundary.

## Officer corps and high command

The Army Command slot contains three mutually exclusive postures:

- Controlled Retaliation Doctrine: +1 percent army organization, +10 maximum Command Power, 5 percent lower military mask/filter consumption, 15 percent lower friendly exposure risk for prepared actions, and 15 percent better evidence recovery when the country is the victim. It never suppresses attacker evidence.
- Theater Contamination Doctrine: +5 percent planning speed, -5 percent attrition, +5 percent supply consumption, +5 percent prepared dose, and +25 percent exact-state cleanup output.
- Terminal Hazard Doctrine: +5 percent army attack, +3 percent coordination, +10 percent supply consumption, +10 percent operational effect, +15 percent deaths, and +25 percent Condemnation. Evidence and attribution remain unchanged.

The Division Command slot contains three mutually exclusive postures:

- Mask Discipline: +1 percent army organization, -5 percent organization loss while moving, and 10 percent lower military mask/filter consumption;
- Hazard Assault Cadres: +2 percent special-forces cap, +3 percent army experience gain, and +5 percent attack/defence for Chaos Assault Battalions and Hazard Pioneers;
- Contaminant Fire Coordination: +3 percent artillery attack and +5 percent reliability for Livens and supported chemical payload equipment.

Four generic institutional high-command offices avoid inventing historical personnel:

- CBRN Operations Director: +3 percent planning speed and +5 maximum Command Power;
- Civil Defence Coordinator: +2 percent stability and -1 percent consumer-goods factor;
- Chemical Logistics Inspector: -3 percent attrition and -3 percent supply consumption;
- Biological Security Director: +1 percent army organization and -2 percent resistance growth.

The `chemical_operations_commander` leader trait costs 500 and requires Chaos Warfare, Protective Foundation, and a fielded Operations HQ Section. It reduces preparation time for the seven CBRN HQ abilities by 10 percent, after the ability's normal readiness and company adjustments. It grants no free release ability.

## AI behavior

AI adoption and track preference use actual program profiles, industry, war, enemy chemical use, and explicit route flags. Ordinary defensive democracies receive a strong first-use penalty. Limited and strategic first-use policies start at zero weight unless an accepted aggressive route/profile adds weight. Unrestricted policy starts at zero and requires an explicit unrestricted route; nonhuman countries receive zero weight.

Officer-corps and high-command choices use the same defensive, battlefield, logistics, and outbreak profiles. Nonhuman AI receives zero selection weight for these institutional appointments and spirits. Every HQ ability retains the full player-equivalent composition, readiness, policy, stock, and Command Power gate. AI receives no hidden payload, readiness, or contamination shortcut.

## Compatibility and migration

The grand doctrine and four track IDs remain stable for save/script compatibility. Legacy atrocity-facing names and broad permanent bonuses are replaced. The old academy and chemical-air spirit IDs remain hidden, unavailable, and AI-disabled so saves can resolve them without exposing a substitute mechanic. Random academy trait grants and the old cylinder abilities are removed. Legacy Integrated Operations biological potency, duration, and Command Power bonuses are neutralized; only the accepted Condemnation multiplier remains.

`on_startup` performs the migration for new campaigns but is not called when an existing save is loaded. A country that already has Chaos Warfare but lacks the institutional adoption flag therefore sees a one-time, zero-cost §YConvene CBRN Institutional Review§! decision. Human and AI countries can execute the same idempotent migration without a global periodic pulse. It reconstructs only native track/mastery facts, clears obsolete occupation-law authority, initializes the establishment review, and grants only independently eligible doctrine technologies; it never fabricates cross-track institutions, stock, fielded formations, protected orders, payload use, or consequences.

Static doctrine definitions use file-local `@` macros because current installed doctrine documentation does not declare global `constant:` support for those parser fields. The local values mirror the centralized `cbrn_doctrine_cost`, `cbrn_doctrine_mastery`, `cbrn_doctrine_modifier`, and `cbrn_doctrine_ai` tables. Scoped effects, triggers, decisions, ideas, and variables continue to use global script constants.

## Verified engine limits

- Native grand-doctrine milestones map one-for-one to tracks and cannot express cross-track institutional proof; exact claim decisions provide that layer.
- Native mastery measures eligible fielded units but exposes no exact per-unit equipment-fill check. Hazard Assault Training is the explicit equipment-backed mastery source; native combat mastery still relies on the doctrine engine's unit participation model.
- Script exposes cumulative gas-mask production but no documented current production-line trigger. Protective Foundation therefore proves production after adoption plus a live reserve, without estimating factory assignment.
- Combat tactics expose no verified activation effect that can reserve payload and dispatch the shared exposure record. Prepared Chemical Barrage remains weight zero and fail-closed until a payload-consuming adapter exists.
- Chemical Air Interdiction has no continuous ordinary-air hook. No estimator or passive contamination fallback is retained.
- Commander abilities do not expose a selected state. Exact decontamination uses a separate player-selected state decision tied to a currently active corridor.
- The Army Headquarters surface is DLC-owned. No ordinary-division substitute is provided.

## Assets and runtime wiring

Final sources, processed PNGs, DDS files, contact sheets, validation inventory, and provenance prompts are under `docs/assets/chaos_warfare_system/stage_5_doctrine_officer_corps/`. Runtime sprites are registered in `interface/cbrn_doctrine.gfx`; the leader-trait sprite is registered in `interface/chaosx_traits.gfx`. All 45 DDS files use the standard 128-byte uncompressed BGRA header, texture caps, real alpha, exact declared dimensions, and no mipmaps.

### Doctrine, milestone, and technology sprites

| Sprite | Runtime DDS |
| --- | --- |
| `GFX_doctrine_chaos_warfare_medium` | `gfx/interface/doctrines/icons/stage_5_chaos_warfare/doctrine_chaos_warfare.dds` |
| `GFX_doctrine_extermination_columns_medium` | `gfx/interface/doctrines/icons/stage_5_chaos_warfare/doctrine_hazard_assault_formations.dds` |
| `GFX_doctrine_chemical_suppression_medium` | `gfx/interface/doctrines/icons/stage_5_chaos_warfare/doctrine_toxic_armored_warfare.dds` |
| `GFX_doctrine_contaminant_firebases_medium` | `gfx/interface/doctrines/icons/stage_5_chaos_warfare/doctrine_contaminant_fire_support.dds` |
| `GFX_doctrine_integrated_chemical_operations_medium` | `gfx/interface/doctrines/icons/stage_5_chaos_warfare/doctrine_integrated_cbrn_command.dds` |
| `GFX_cbrn_doctrine_hazard_assault_reward_strip` | `gfx/interface/doctrines/rewards/stage_5_chaos_warfare/hazard_assault_reward_strip.dds` |
| `GFX_cbrn_doctrine_toxic_armor_reward_strip` | `gfx/interface/doctrines/rewards/stage_5_chaos_warfare/toxic_armor_reward_strip.dds` |
| `GFX_cbrn_doctrine_contaminant_fire_reward_strip` | `gfx/interface/doctrines/rewards/stage_5_chaos_warfare/contaminant_fire_reward_strip.dds` |
| `GFX_cbrn_doctrine_integrated_command_reward_strip` | `gfx/interface/doctrines/rewards/stage_5_chaos_warfare/integrated_command_reward_strip.dds` |
| `GFX_cbrn_doctrine_milestone_protective_foundation` | `gfx/interface/doctrines/milestones/stage_5_chaos_warfare/protective_foundation.dds` |
| `GFX_cbrn_doctrine_milestone_delivery_integration` | `gfx/interface/doctrines/milestones/stage_5_chaos_warfare/delivery_integration.dds` |
| `GFX_cbrn_doctrine_milestone_theater_exploitation` | `gfx/interface/doctrines/milestones/stage_5_chaos_warfare/theater_exploitation.dds` |
| `GFX_cbrn_doctrine_milestone_terminal_command` | `gfx/interface/doctrines/milestones/stage_5_chaos_warfare/terminal_command.dds` |
| `GFX_mobile_decontamination_columns_medium` | `gfx/interface/technologies/stage_5_chaos_warfare/cbrn_mobile_decontamination_columns.dds` |
| `GFX_chemical_air_interdiction_medium` | `gfx/interface/technologies/stage_5_chaos_warfare/cbrn_chemical_air_interdiction.dds` |

### Officer corps, high command, and leader trait

| Sprite | Runtime DDS |
| --- | --- |
| `GFX_idea_chemical_command_reagent_optimization_spirit` | `gfx/interface/officer_corp/spirits/stage_5_chaos_warfare/controlled_retaliation_doctrine.dds` |
| `GFX_idea_cbrn_theater_contamination_doctrine_spirit` | `gfx/interface/officer_corp/spirits/stage_5_chaos_warfare/theater_contamination_doctrine.dds` |
| `GFX_idea_cbrn_terminal_hazard_doctrine_spirit` | `gfx/interface/officer_corp/spirits/stage_5_chaos_warfare/terminal_hazard_doctrine.dds` |
| `GFX_idea_cbrn_mask_discipline_spirit` | `gfx/interface/officer_corp/spirits/stage_5_chaos_warfare/mask_discipline.dds` |
| `GFX_idea_cbrn_hazard_assault_cadres_spirit` | `gfx/interface/officer_corp/spirits/stage_5_chaos_warfare/hazard_assault_cadres.dds` |
| `GFX_idea_chemical_division_contamination_command_spirit` | `gfx/interface/officer_corp/spirits/stage_5_chaos_warfare/contaminant_fire_coordination.dds` |
| `GFX_idea_cbrn_operations_director` | `gfx/interface/ideas/stage_5_chaos_warfare/cbrn_operations_director.dds` |
| `GFX_idea_cbrn_civil_defence_coordinator` | `gfx/interface/ideas/stage_5_chaos_warfare/civil_defence_coordinator.dds` |
| `GFX_idea_cbrn_chemical_logistics_inspector` | `gfx/interface/ideas/stage_5_chaos_warfare/chemical_logistics_inspector.dds` |
| `GFX_idea_cbrn_biological_security_director` | `gfx/interface/ideas/stage_5_chaos_warfare/biological_security_director.dds` |
| `GFX_trait_chemical_operations_commander` | `gfx/interface/traits/stage_5_chaos_warfare/trait_cbrn_operations_commander.dds` |

### Decision and category sprites

Every decision icon below is an independent 32-by-32 concept in `gfx/interface/decisions/stage_5_chaos_warfare/`; the category is an independent 52-by-40 composition.

| Sprite | Runtime DDS |
| --- | --- |
| `GFX_decision_category_cbrn_chemical_operations` | `cbrn_chemical_operations_category.dds` |
| `GFX_decision_cbrn_convene_institutional_review` | `cbrn_convene_institutional_review.dds` |
| `GFX_decision_cbrn_chaos_warfare_establishment_mission` | `cbrn_chaos_warfare_establishment_mission.dds` |
| `GFX_decision_cbrn_complete_delayed_establishment` | `cbrn_complete_delayed_establishment.dds` |
| `GFX_decision_cbrn_claim_protective_foundation` | `cbrn_claim_protective_foundation.dds` |
| `GFX_decision_cbrn_claim_delivery_integration` | `cbrn_claim_delivery_integration.dds` |
| `GFX_decision_cbrn_claim_theater_exploitation` | `cbrn_claim_theater_exploitation.dds` |
| `GFX_decision_cbrn_claim_terminal_command` | `cbrn_claim_terminal_command.dds` |
| `GFX_decision_cbrn_hazard_assault_training` | `cbrn_hazard_assault_training.dds` |
| `GFX_decision_cbrn_set_defensive_preparation_policy` | `cbrn_set_defensive_preparation_policy.dds` |
| `GFX_decision_cbrn_set_retaliation_authority_policy` | `cbrn_set_retaliation_authority_policy.dds` |
| `GFX_decision_cbrn_set_limited_battlefield_policy` | `cbrn_set_limited_battlefield_policy.dds` |
| `GFX_decision_cbrn_set_strategic_release_policy` | `cbrn_set_strategic_release_policy.dds` |
| `GFX_decision_cbrn_set_unrestricted_policy` | `cbrn_set_unrestricted_policy.dds` |
| `GFX_decision_cbrn_commission_sealed_tank_crews` | `cbrn_commission_sealed_tank_crews.dds` |
| `GFX_decision_cbrn_commission_persistent_shell_filling` | `cbrn_commission_persistent_shell_filling.dds` |
| `GFX_decision_cbrn_commission_nerve_suppression` | `cbrn_commission_nerve_suppression.dds` |
| `GFX_decision_cbrn_commission_biological_security_assault` | `cbrn_commission_biological_security_assault.dds` |
| `GFX_decision_cbrn_assign_decontamination_corridor` | `cbrn_assign_decontamination_corridor.dds` |

No runtime asset is a placeholder, a cross-type resize, or a reused substitute.

## Future integration and suggestions

Required later package work:

- implement the selected-state Chemical Air Interdiction operation through the shared payload/exposure pipeline;
- connect doctrine operation flags to every ground, raid, and suppression delivery adapter without free contamination;
- complete distinct-agent biological incubation, spread, detection, treatment, containment, accident, and attribution paths;
- implement equipment-consuming nerve-agent suppression and its full resistance/evidence/consequence record;
- add route-specific country profiles beyond the Stage 5 safe baseline;
- integrate milestone sprites into the dedicated CBRN command UI;
- run live doctrine, designer, shortage, policy, AI, cleanup, Condemnation-floor, and migration scenarios.

Possible depth after the accepted package is complete includes after-action doctrine history, theater-specific staff reports, and a dedicated CBRN institutional summary. None may bypass exact payload, state, protection, evidence, or consequence accounting.
