# Chaos Warfare doctrine, institutions, and officer corps

> **Overhaul reconciliation in progress:** The user's accepted [2026-09-20 CBRN amendment](../../specs/chaos_warfare_system_specs/specs/13_2026_09_20_accepted_cbrn_overhaul.md) controls combined bonus caps, policy count, unit consolidation, and native CBRN High Command where this older current-system description conflicts. Do not treat the remaining older numerical examples as final overhaul validation until the parent reviews the complete source and balance evidence.

## Current source arithmetic and validation limit

The accepted 2026-09-20 ceilings apply to combined legal sources, not to each trait independently. The parent and technology owner retuned doctrine, spirits, High Command, and technology after the first audit. The completion auditor then recomputed strict all-independent upper bounds for separately legal scenarios; the table gives source arithmetic, not the engine's final stat formula. Controlled Retaliation, Theater Contamination, and Terminal Hazard share one `army_spirit` slot; Mask Discipline and Hazard Assault Cadres share one `division_command_spirit` slot. No effective-cap or engine acceptance is claimed here.

| Endpoint and legal posture | Strict all-independent source bound | Accepted ceiling |
| --- | ---: | ---: |
| Army attack with Terminal | +4.0375% | +5% |
| Army organisation with Controlled Retaliation and Mask Discipline | +4.5807% | +5% |
| Planning with Theater | +14.7368% | +15% |
| Coordination with Terminal | +7.7496% | +8% |
| Reinforcement | +2 percentage points in source | +2 percentage points |
| Line artillery doctrine soft attack; with legal global attack | +9.7980%; +14.2311% combined | +10% doctrine; +15% conventional |
| Support artillery doctrine soft attack; with legal global attack | +9.8246%; +14.2588% combined | +10% doctrine; +15% conventional |
| Two-tech projector soft/hard/defense/breakthrough | +32.8602% / +32.8455% / +34.0096% / +33.7780% | +35% dedicated static each |
| Projector organisation | +33.6309% | +35% dedicated static |
| Armored delivery soft/hard/defense/breakthrough/organisation | +26.4582% / +4.0375% / +21.5506% / +21.6201% / +26.3683% | +35% dedicated static each |
| Chaos Battalion soft/defense/breakthrough/organisation | +20.1633% / +10% / +33.2278% / +33.3404% | +35% dedicated static each |
| Protection Company attack/defense | +14.4413% / +10% | +35% dedicated static each |
| CBRN reconnaissance utility from three hidden weather technologies | +30% on base 4 | +35% dedicated static |

The strict source products include 1.5% Protected Assault mastery IV × 2.5% Terminal army attack for +4.0375%, four separate +1% organisation sources × the 0.5% Biological Security Director source for +4.5807%, and legal Theater planning sources 1% × 1% × 3% × 4% × 5% for +14.7368%. Terminal, Theater, and Controlled Retaliation are distinct scenarios. The 1942 Battalion technology adds 11 flat organisation on base 40; its strict combination with legal organisation sources is +33.3404%, not a flat 11% grant. `common/technologies/chaosx_technologies.txt` now gives each projector tier 2.5% soft attack, 13% hard attack, 5% defense, and 7.5% breakthrough, and the three hidden reconnaissance technologies add 0.2, 0.4, and 0.6 flat to base 4. The accepted ceilings are source-bounded under this conservative all-independent model, but engine aggregation and the `biological_operations_veteran` `defense_skill = 1` conversion remain unresolved.

| Conditional endpoint | Largest source stack in a separate country- and spirit-slot-legal scenario | Source arithmetic |
| --- | --- | ---: |
| Choking artillery dose | Fire support 1.04 × Integrated Command 1.04 × Terminal Hazard 1.05 × stable-choking MIO 1.03 × one chemical advisor 1.03 | 1.204843 × base |
| Chemical air dose | Fire support 1.04 × Integrated Command 1.04 × air link 1.02 × Terminal Hazard 1.05 × one chemical advisor 1.03 | 1.193145 × base |
| Choking contamination | Choking artillery dose 1.204843 × three 1.03 contamination factors × one advisor factor 1.02 | 1.342896 × base |
| Blister contamination | Base doctrine dose 1.04² × Terminal Hazard dose 1.05 × one advisor dose 1.03 × three 1.03 contamination factors × one advisor contamination 1.02 × persistent MIO 1.02 | 1.329858 × base |
| Air or blister duration | Fire support 1.03 × Integrated Command 1.03 × air link 1.10 × Terminal Hazard 1.10 × persistent MIO 1.15 | 1.476242 × base |
| Soviet toxicological casualty pressure | Choking artillery dose 1.204843 × Terminal Hazard casualty factor 1.10 × toxicological director 1.05 | 1.391594 × base |
| Japanese or American biological seed potency | Terminal Hazard 1.20 × Integrated Command 1.10 × strategic-dissemination MIO 1.02 × two compatible advisors 1.02² | 1.400795 × base |
| Exact-state cleanup output | Theater Contamination 1.10 × low-water MIO 1.15 × rapid-route MIO 1.15 | 1.454750 × base |

The earlier doctrine handoff's 1.03² chemical-advisor and 1.02⁵ biological-advisor products pooled country-locked appointments from different countries and are superseded for legal scenario maxima. `common/characters/cbrn_historical_specialists.txt` permits the chemical theorist only for GER and toxicological director only for SOV; the largest biological actor combinations have two compatible potency appointments, in JAP or USA after their date gates. `common/script_constants/cbrn_historical_advisor_constants.txt` and `common/scripted_effects/cbrn_historical_advisor_effects.txt` define and apply their factors. The choking and blister rows are separate endpoint scenarios: Stable Choking Fill affects choking artillery dose, while Persistent Agent Formulation affects blister contamination and duration. Persistent Agent Formulation is a descendant of Stable Choking Fill in `common/military_industrial_organization/organizations/cbrn_delivery_organizations.txt`; they are not mutually exclusive. The chemical-readiness generation maximum from one eligible advisor is 1.20, not the old 1.20². The core owner removed the orphan `cbrn_doctrine_advisor` planning/organisation constant blocks; their former values are not active bonuses. Conditional scenario and revised static technology source arithmetic are bounded as shown, while probability, MCP, and engine checks remain open.

The dated numerical detail below is retained as an implementation-history account where it has not yet been reconciled line by line. Its obsolete five-policy ladder, spirit magnitudes, unit names, and older global-bonus examples do not override the current source arithmetic above, the three-policy table below, or the accepted amendment. The parent must review any remaining historical detail against current source before using it as an implementation instruction.

## Purpose

Chaos Warfare is a conditional CBRN grand doctrine, not a universal attack tree. Adoption begins a national institution that must prove protective stock, fielded headquarters, and protected formations before offensive authority can expand. Four mastery tracks grant bounded unit, headquarters, logistics, and operation eligibility. Actual chemical delivery remains equipment-backed and must use the shared exposure pipeline.

Doctrine may reduce the Condemnation impact of an accepted chemical or biological use. That reduction affects Condemnation only. It never discounts payload consumption, evidence, attribution, deaths, contamination, medical saturation, resistance trauma, domestic war-support penalties, use counters, confirmed-use history, or strategic and mass-casualty public-harm floors.

The implementation is split across:

- `common/doctrines/` for the grand doctrine and four mastery tracks
- `common/script_constants/cbrn_doctrine_constants.txt` for shared gameplay tuning, with the existing `chem_integrated_operations.condemnation_mult` table retained as the single migration-safe 0.75/0.55/0.35 Condemnation ladder for chemical and biological callers
- `common/scripted_triggers/cbrn_doctrine_triggers.txt` and `common/scripted_effects/cbrn_doctrine_effects.txt` for reusable gates and state changes
- `common/decisions/cbrn_doctrine_decisions.txt` for establishment, institutional claims, policy, training, commissions, and exact-state cleanup
- `common/ideas/cbw_spirits.txt`, `common/ideas/cbrn_high_command.txt`, and the leader-trait files for officer-corps content
- `interface/cbrn_doctrine.gfx` and `interface/chaosx_traits.gfx` for final runtime assets.

## Adoption and establishment

Chaos Warfare is visible to every country but available only when at least one accepted capability route exists:

- Basic Gas Masks plus a supported chemical-agent technology
- a completed mapped chemical special project
- an established CBRN command flag
- a mapped historical CBRN program profile
- an explicit scenario override.

Adoption costs 100 Army Experience. It initializes the shared CBRN model, records the post-adoption mask-production baseline, sets the Chemical Readiness cap to 39, raises readiness to at least 10, activates the Operations HQ Section and defensive support unlocks, grants doctrine-qualified technologies whose gates are already met, and starts a 90-day establishment mission.

Establishment succeeds only while the country has all of the following:

- 500 gas-mask equipment
- 50 decontamination equipment
- 100 support equipment
- at least one fielded CBRN Operations HQ Section
- at least one fielded Gas Mask and Decontamination Detachment.

Success records the institution, raises readiness to at least 20, and raises decontamination capacity to at least 20. Timeout leaves the doctrine active, closes offensive gates, caps readiness at 9, and exposes a 14-day remediation decision costing 35 Political Power and 10 Command Power. Remediation repeats the exact establishment proof. It does not waive missing stock or formations.

## Institutional milestones

Native grand-doctrine milestone blocks can record only their corresponding completed track. Exact cross-track requirements therefore use one-time country decisions and no periodic polling.

| Institution | Exact proof | Result |
| --- | --- | --- |
| Protective Foundation | establishment complete<br>cumulative gas-mask production increased after adoption<br>500 live masks<br>fielded Operations HQ | readiness cap 59<br>readiness minimum 30<br>decontamination minimum 30 |
| Delivery Integration | Protective Foundation<br>Hazard Assault, Contaminant Fire, or Toxic Armor at mastery 2<br>at least 100 of one supported payload<br>one successfully completed protected HQ order | readiness cap 74<br>readiness minimum 45<br>native chemical raid eligibility subject to its own gates |
| Theater Exploitation | Delivery Integration<br>any two tracks at mastery 3<br>decontamination capacity 40<br>fielded Intelligence and Weather Cell | readiness cap 89<br>readiness minimum 65<br>exact-state decontamination and theater HQ gates |
| Terminal CBRN Command | Theater Exploitation<br>all four tracks active<br>any track at mastery 5<br>Battlefield Authorization or higher<br>advanced protection technology or explicit equivalent project | readiness cap 100<br>readiness minimum 85<br>capstone command gates |

The protected-order history flag is written only after Theater Protective Posture completes preparation successfully. Starting an order that later fails does not qualify.

## Mastery tracks

Each track costs 100 Army Experience. Native mastery comes from fielded mapped units and uses the current doctrine system. Track adoption and mastery provide deliberately strong combat, protection, logistics, and command returns, while live-agent outcomes remain operation-, stock-, readiness-, and policy-gated.

| Compatibility ID | Player-facing track | Mastery content |
| --- | --- | --- |
| `extermination_columns` | Hazard Assault Formations | Mask Discipline<br>contaminated-terrain movement<br>Chaos Assault Battalion qualification<br>shock exploitation<br>terminal hazard-operation eligibility |
| `chemical_suppression` | Toxic Armored Warfare | sealed crews<br>armored agent delivery<br>costed nerve-suppression formation<br>protected breakthrough logistics<br>synchronized shock eligibility |
| `contaminant_firebases` | Contaminant Fire Support | projector fire control<br>counterbattery coordination<br>Chemical Artillery Shells<br>persistent-agent shell commission<br>deep-contamination operation eligibility |
| `integrated_chemical_operations` | Integrated CBRN Command | Intelligence and Weather Cell<br>Protective Logistics<br>Mobile Decontamination Columns<br>Chemical Air Interdiction and Biosecurity<br>Theater CBRN Headquarters |

The Toxic Armored Warfare track commissions protected nerve-suppression formations but grants no camp, extermination-site, experiment-site, genocide, or Concentration occupation-law infrastructure by itself. Gas-Chamber Saturation Drills are the accepted camp route: once that mastery is active, the camp needs only a researched and stocked nerve agent. Every use consumes payload and records deaths, contamination, resistance trauma, evidence, and severe diplomatic consequences.

### Equipment-backed Hazard Assault Training

Hazard Assault Training requires Hazard Assault Formations, a fielded protected formation, 100 masks, and 10 Army Experience. It removes masks oldest-first, records the actual mask debit, and grants 0.25 daily mastery to Hazard Assault Formations for 30 days. The decision re-enables after 90 days. It does not authorize live-agent use or create exposure.

### Doctrine-only technologies

The doctrine grants or commissions the following non-researchable technologies only after their exact mastery, institution, project, policy, and protection gates are met:

- Hazard Pioneer Formation
- Chemical Artillery Shells
- Persistent Agent Shell Filling
- Armored Agent Delivery
- Sealed Tank Crews
- Nerve Agent Suppression Formation
- Chaos Assault Battalion and Improved Chaos Assault Equipment
- Mobile Decontamination Columns
- Chemical Air Interdiction
- Theater CBRN Headquarters
- Biological Security Assault Formation.

Sealed Tank Crews, Persistent Agent Shell Filling, Nerve Agent Suppression, and Biological Security Assault use seven-day commissions costing 25 Political Power and 5 non-refundable Command Power. Losing the prerequisite before completion cancels the grant.

Chemical Air Interdiction is an eligibility marker only in this stage. It creates no passive regional effect, makes no estimate of sortie activity, and cannot contaminate a state. A later selected-state operation must prove execution, consume the selected payload, resolve protection and conditions, and call the shared exposure record. Idle chemical-capable aircraft never contaminate a region.

## Use policy

Policy changes are decisions with a 90-day reassessment lock and a five-Command-Power cost. The current decisions have zero native Political Power cost and call the shared policy effect after their exact availability gates pass. Doctrine progression does not change national policy automatically.

| Policy | Command Power | Reassessment | Source decision |
| --- | ---: | --- | --- |
| Retaliation Only | 5 | 90 days | `cbrn_choose_retaliation_only` |
| Battlefield Authorization | 5 | 90 days | `cbrn_choose_battlefield_authorization` |
| Unrestricted Authorization | 5 | 90 days | `cbrn_choose_unrestricted_authorization` |

Policy permits delivery adapters to pass authorization checks. It never spends a payload or creates exposure by itself. The inactive selected-state coercive-security operation retains its separate authorization gate for compatibility, but it is not the accepted camp implementation. Gas-Chamber Saturation Drills use the camp network directly and require no Chaos Warfare doctrine or occupation-policy prerequisite beyond the researched and stocked nerve agent.

## Condemnation-only doctrine mitigation

`cbrn_prepare_chemical_action_record` owns the doctrine lookup so every accepted chemical delivery route receives one consistent multiplier:

- Operations mastery 1: 0.75
- Operations mastery 4: 0.55
- Operations mastery 5: 0.35
- otherwise: 1.00.

The shared exposure calculation applies this value only to the Condemnation base before attribution and public-harm floors. Evidence and attribution are calculated independently. The old Theater Contamination and Terminal Hazard numerical catalogue in this guide was superseded by the 2026-09-20 combined-cap retune; the current compatible endpoint maxima are in the source-arithmetic table above. Physical payload debit, evidence, attribution, deaths and death history, contamination and contamination history, medical saturation and medical history, confirmed-use history, domestic war-support penalties, biological-use counters, accident records, resistance trauma, and public-harm floors remain fully recorded.

## Exact-state decontamination assignment

An active Army HQ Decontamination Corridor plus Theater Exploitation exposes a state-targeted assignment decision. It requires a controlled state with actual chemical contamination and permits one national assignment every 28 days. Cleanup output depends on the current contamination class:

Each assignment is paid at the point of use. It costs 5 Political Power, 4 Command Power, 40 Decontamination Equipment, 100 Gas Masks, 20 Support Equipment, 2 Motorized Equipment, and 300 Fuel. Decontamination stock and masks are debited from the oldest available progression tiers, while support equipment, motorized equipment, fuel, and command power use the native stockpiles. A shortage prevents the assignment from starting; the assignment does not create free cleanup capacity.

- Trace or Local: 10 points
- Serious: 8 points
- Severe: 5 points
- Catastrophic: 3 points.

The current Theater Contamination source multiplier for this output is 1.10 before the compatible MIO cleanup factors shown above. The effect calls the state contamination ledger and records only the amount actually removed. It does not erase evidence, attribution, deaths, Condemnation, or confirmed-use history. The national assignment lock preserves the exact-state boundary; its current duration requires source and engine review before acceptance.

## Officer corps and high command

The three mutually exclusive Army Command postures are Controlled Retaliation, Theater Contamination, and Terminal Hazard. Controlled Retaliation contributes 1% army organisation in its legal organisation scenario. Theater Contamination contributes 3% planning in its legal planning scenario and supports exact-state cleanup. Terminal Hazard contributes 2.5% army attack and 0.5% coordination in its separate offensive scenario. Current `common/ideas/cbw_spirits.txt`, doctrine constants, and the source-arithmetic tables above govern the remaining effects; the older high-magnitude spirit and paid offensive HQ preparation examples are superseded. Evidence and attribution remain recorded independently of the posture.

The historical Gas-Chamber Saturation Drills numerical example is superseded by the accepted combined-cap retune; the current legal authored nerve-camp mortality specialization reaches 1.495 times base according to the doctrine owner's source arithmetic. The hook runs only inside the camp system's state death calculation and uses its stored responsible-country pointer. It does not create, reveal, authorize, or unlock a camp, extermination building, experiment site, restricted chemical site, or occupation law, and it does not alter camp evidence, discovery, resistance, trauma, Condemnation, or responsibility records. Unrestricted Authorization remains the governing national use policy.

The earlier flat-stat explanation for Chemical Projector Batteries and the Chaos Battalion is superseded because technology subunit bonus fields are multiplicative toward the unit. Current `common/technologies/chaosx_technologies.txt` gives each projector tier 2.5% soft attack, 13% hard attack, 5% defense, and 7.5% breakthrough; the 1942 Battalion technology grants 15% breakthrough and 11 flat organisation. The strict legal all-independent upper bounds are in the current source table above, while exact engine aggregation remains unresolved.

The auditor found that the earlier reconnaissance technology values added flat `recon` values of 2, 3, and 5 to a base of 4, or +250%. The parent resolved the accepted +35% dedicated-static ceiling to include this reconnaissance utility. The technology owner verified fractional `recon` syntax against installed vanilla `common/technologies/infantry.txt` and changed the three grants in `common/technologies/chaosx_technologies.txt` to 0.2, 0.4, and 0.6. Their +1.2 sum on base 4 is +30% in source arithmetic; the engine result remains unverified.

Chemical Operations Commander is earned from completed qualifying Headquarters service. Chemical Operations Academy grants +3 percent army experience gain and does not award the trait. The two paid offensive HQ preparation orders are retired; five protective orders remain. A country's first confirmed chemical exposure applies a defender-side command shock without an attacker buff.

The Division Command slot contains mutually exclusive Mask Discipline, Hazard Assault Cadres, and Contaminant Fire Coordination postures. Mask Discipline contributes 1% army organisation in the Controlled Retaliation organisation scenario. Hazard Assault Cadres instead contributes 10% role-specific attack and defense to the Chaos Battalion and Protection Company route and cannot coexist with Mask Discipline. Current spirit source controls the remaining effects; the older +35% artillery attack example is superseded.

Chemical Operations Commander supplies native CBRN High Command specialist, expert, and genius ranks. The current `common/country_leader/cbrn_high_command_traits.txt` source grants +1/+3/+4 percent planning speed and +5/+10/+15 maximum Command Power across those ranks. Civil Defence Coordinator, Chemical Logistics Inspector, and Biological Security Director retain their distinct institutional offices; Biological Security Director contributes 0.5% army organisation and -15% resistance growth.

The `chemical_operations_commander` leader trait is awarded through completed service and grants no free release ability. Its remaining protective order effects require the active HQ source and engine review.

## AI behavior

AI adoption and track preference use actual program profiles, industry, war, enemy chemical use, and explicit route flags. Ordinary defensive democracies receive a strong first-use penalty. Battlefield Authorization starts at zero weight unless an accepted aggressive route/profile adds weight. Theater Contamination adds further first-use weight only after those exact gates pass. Unrestricted Authorization starts at zero and requires an explicit unrestricted route. Terminal Hazard adds further unrestricted-use weight only within that route. Native chemical raids and the surviving protective HQ orders have their own exact gates; the two former paid offensive HQ abilities are retired. Nonhuman countries receive zero weight. These source descriptions are not scenario-specific probability proof.

Officer-corps and high-command choices use the same defensive, battlefield, logistics, and outbreak profiles. Nonhuman AI receives zero selection weight for these institutional appointments and spirits. Every HQ ability retains the full player-equivalent composition, readiness, policy, stock, and Command Power gate. AI receives no hidden payload, readiness, or contamination shortcut.

## Compatibility and migration

The grand doctrine and four track IDs remain stable for save and script compatibility. Legacy atrocity-facing names and broad permanent bonuses are replaced. The Chemical Operations Academy remains an active officer-corps route that grants +3 percent army experience gain, while the old chemical-air spirit ID remains hidden and unavailable for save compatibility. Chemical Operations Commander is earned from completed qualifying Headquarters service; no academy trait roll, periodic country scan, or passive chemical activity grants it. Legacy Integrated Operations biological bonuses are neutralized. The dedicated Theater Contamination and Terminal Hazard spirits provide the accepted biological escalation, deployment refund, and Condemnation behavior.

`on_startup` performs the migration for new campaigns but is not called when an existing save is loaded. A country that already has Chaos Warfare but lacks the institutional adoption flag therefore sees a one-time, zero-cost §YConvene CBRN Institutional Review§! decision. Human and AI countries can execute the same idempotent migration without a global periodic pulse. It reconstructs only native track/mastery facts, clears obsolete occupation-law authority, initializes the establishment review, and grants only independently eligible doctrine technologies. It never fabricates cross-track institutions, stock, fielded formations, protected orders, payload use, or consequences.

Static doctrine definitions use file-local `@` macros because current installed doctrine documentation does not declare global `constant:` support for those parser fields. The local values mirror the centralized `cbrn_doctrine_cost`, `cbrn_doctrine_mastery`, `cbrn_doctrine_modifier`, and `cbrn_doctrine_ai` tables. Scoped effects, triggers, decisions, ideas, and variables continue to use global script constants.

## Verified engine limits

- Native grand-doctrine milestones map one-for-one to tracks and cannot express cross-track institutional proof. Exact claim decisions provide that layer.
- Native mastery measures eligible fielded units but exposes no exact per-unit equipment-fill check. Hazard Assault Training is the explicit equipment-backed mastery source. Native combat mastery still relies on the doctrine engine's unit participation model.
- Script exposes cumulative gas-mask production but no documented current production-line trigger. Protective Foundation therefore proves production after adoption plus a live reserve, without estimating factory assignment.
- Combat tactics expose no verified activation effect that can reserve payload and dispatch the shared exposure record. Prepared Chemical Barrage remains weight zero and fail-closed until a payload-consuming adapter exists.
- Chemical Air Interdiction has no continuous ordinary-air hook. No estimator or passive contamination fallback is retained.
- Commander abilities do not expose a selected state. Exact decontamination uses a separate player-selected state decision tied to a currently active corridor.
- The Army Headquarters surface is DLC-owned. No ordinary-division substitute is provided.

## Assets and runtime wiring

Final sources, processed PNGs, DDS files, contact sheets, validation inventory, and provenance prompts are under `docs/assets/chaos_warfare_system/stage_5_doctrine_officer_corps/`. Runtime sprites are registered in `interface/cbrn_doctrine.gfx`. The leader-trait sprite is registered in `interface/chaosx_traits.gfx`. All 45 DDS files use the standard 128-byte uncompressed BGRA header, texture caps, real alpha, exact declared dimensions, and no mipmaps.

### Doctrine, milestone, and technology sprites

| Sprite | Runtime DDS |
| --- | --- |
| `GFX_doctrine_chaos_warfare_medium` | `gfx/interface/doctrines/icons/doctrine_chaos_warfare.dds` |
| `GFX_doctrine_extermination_columns_medium` | `gfx/interface/doctrines/icons/chaos_warfare_doctrine_style/doctrine_hazard_assault_formations.dds` |
| `GFX_doctrine_chemical_suppression_medium` | `gfx/interface/doctrines/icons/chaos_warfare_doctrine_style/doctrine_toxic_armored_warfare.dds` |
| `GFX_doctrine_contaminant_firebases_medium` | `gfx/interface/doctrines/icons/chaos_warfare_doctrine_style/doctrine_contaminant_fire_support.dds` |
| `GFX_doctrine_integrated_chemical_operations_medium` | `gfx/interface/doctrines/icons/chaos_warfare_doctrine_style/doctrine_integrated_cbrn_command.dds` |
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
| `GFX_idea_cbrn_civil_defence_coordinator` | `gfx/interface/ideas/stage_5_chaos_warfare/civil_defence_coordinator.dds` |
| `GFX_idea_cbrn_chemical_logistics_inspector` | `gfx/interface/ideas/stage_5_chaos_warfare/chemical_logistics_inspector.dds` |
| `GFX_idea_cbrn_biological_security_director` | `gfx/interface/ideas/stage_5_chaos_warfare/biological_security_director.dds` |
| `GFX_trait_chemical_operations_commander` | `gfx/interface/traits/stage_5_chaos_warfare/trait_cbrn_operations_commander.dds` |

### Decision and category sprites

Every decision icon below is an independent 32-by-32 concept in `gfx/interface/decisions/stage_5_chaos_warfare/`. The category is an independent 52-by-40 composition.

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

- implement the selected-state Chemical Air Interdiction operation through the shared payload/exposure pipeline
- connect doctrine operation flags to every ground, raid, and suppression delivery adapter without free contamination
- extend the ordinary-pathogen lifecycle to any later approved battlefield, sabotage, or doomsday delivery adapters with exact payload and state proof
- implement equipment-consuming nerve-agent suppression and its full resistance/evidence/consequence record
- add route-specific country profiles beyond the Stage 5 safe baseline
- integrate milestone sprites into the dedicated CBRN command UI
- run live doctrine, designer, shortage, policy, AI, cleanup, Condemnation-floor, and migration scenarios.

Possible depth after the accepted package is complete includes after-action doctrine history, theater-specific staff reports, and a dedicated CBRN institutional summary. None may bypass exact payload, state, protection, evidence, or consequence accounting.
