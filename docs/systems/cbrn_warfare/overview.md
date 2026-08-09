# CBRN Warfare System

## Purpose

The CBRN Warfare System coordinates Chaos Warfare doctrine, protective production, Army Headquarters preparation, regimental support, chemical delivery, biological outbreaks, civilian defence, evidence, attribution, deaths, contamination, Condemnation, sanctions, and recovery.

The accepted design source is `docs/specs/chaos_warfare_system_specs/`. Working implementation and audit evidence lives in `docs/plans/chaos_warfare_system_plans/`.

## Current implementation boundary

The shared Stage 1 data model defines Chemical Readiness, policy, capacities, contamination and attribution classes, protection layers, agent and route profiles, and a fail-closed chemical action-record calculator.

The Stage 2 protective-equipment layer adds four producible respirator/protective-set models, one non-producible reconditioned model, three decontamination models, three instrument models, their technology branches, real national reserves, model-specific military issue, population-scaled state distribution, fitting, filter condition, loss, replacement, reconditioning, transfer cleanup, starting profiles, production AI, decisions, event handling, localisation, and type-specific assets. Existing chemical abilities now read equipment-backed respiratory and skin protection instead of treating technology ownership as protection.

Medical response remains an institutional capacity backed by support equipment, trucks, field hospitals, and mapped treatment technologies. No unsupported standalone medical-equipment archetype is introduced.

The exact-state chemical air-raid adapter and exact-state camp chemical method consume real payloads, resolve the applicable equipment-backed protection receipt, and pass their result through the shared consequence dispatcher. Gas-Chamber Saturation Drills strengthen nerve-agent use inside an already active camp transaction; they do not create camp infrastructure or depend on the unavailable legacy occupation-operation estimator. The shared calculator remains fail-closed for any route that cannot prove an exact target state, real payload debit, resolved protection, and every route-required condition. Continuous ordinary-air missions are rejected because the installed engine exposes no verified eligible-activity hook; idle chemical-capable aircraft cannot enter the exposure path.

Military mask accounting keeps two native surfaces distinct: protection reads actual respirator models deployed in divisions through `num_equipment_in_armies@<model>` plus the model-specific military-issue ledger, while loss and filter replacement debit the non-reclaimable issue ledger because the installed script surface has no current-version effect for removing a selected equipment model from deployed divisions. The system does not fabricate a fielded-unit removal or retain an undisclosed synthetic damage estimator.

## Final gameplay loop

1. Establish a national program and choose a use policy.
2. Produce masks, filters, decontamination equipment, instruments, payloads, and route-specific stores.
3. Issue military protection, build civilian reserves, and distribute protection to selected states.
4. Equip regimental support and Army Headquarters companies.
5. Prepare a route-specific operation with command cost, duration, cooldown, target, payload, forecast, and cleanup plan.
6. Debit payload, resolve protection and conditions, and create one exposure record.
7. Apply disruption, deaths, contamination or outbreak pressure, medical saturation, evidence, attribution, Condemnation, and sanctions through shared adapters.
8. Replace filters, treat casualties, contain outbreaks, decontaminate states and routes, manage inspections, and absorb diplomatic consequences.

## Layers

### National

- Chemical Readiness, 0 to 100, capped by actual milestones and institutions
- one use policy: defensive, retaliation, battlefield, strategic, or unrestricted
- decontamination, medical, biological-security, attribution-control, and command-integration capacities
- real protective and offensive stockpiles
- differentiated AI program posture and country profile

### Army Headquarters

Army Headquarters is the theater layer. Six CBRN companies provide operations planning, intelligence and weather, protective logistics, mobile decontamination, medical direction, and biological security. Their abilities require equipment, preparation, command power, duration, cooldown, AI use, and cleanup.

### Division

Regimental support is the division layer. Ten role-based detachments replace agent-by-agent unit duplication. Strong scripted benefits scale or disappear with essential-equipment shortages.

### State

Affected states store only active values: chemical contamination, outbreak state, civilian protection, decontamination progress, medical saturation, evidence, attribution, and movement controls. Recovery removes stale values. No all-state initialization or broad all-country periodic pulse is used.

## Shared chemical exposure

Every chemical route must eventually call `cbrn_prepare_chemical_action_record` after proving:

- an exact target state
- real payload consumption
- resolved protection
- resolved conditions

The calculator returns one consistent result for disruption, military/civilian deaths, contamination, medical burden, evidence, attribution, Condemnation base, and friendly risk. A later single dispatcher owns all persistent consequence changes. This keeps Deaths, Air Cleanliness, Condemnation, contamination, and operation history synchronized.

Protection is layered. Respirators dominate choking-agent defence; blister and nerve defence additionally depend on skin protection, decontamination, antidotes, medical response, warning, and training. Doctrine has its own bounded Condemnation multiplier, separate from retaliation and target-relationship context. It can reduce impact through discipline and precision, but cannot erase evidence, attribution, confirmed-use history, deaths, or visible contamination.

## Biological boundary

Ordinary biological warfare will use separate profiles for anthrax, plague, tularemia, and smallpox, with agent-specific incubation, detection, spread, containment, treatment, safety, and attribution. Weaponized zombies remain a separate weapon class and lifecycle. They may share only explicitly approved evidence, death, Air Cleanliness, and consequence adapters.

## Existing-system integration

- Deaths: one operation or continuing-death period creates one shared record and real population loss.
- Air Cleanliness: chemical contamination changes the global value only when a state crosses a contamination class; biological contribution follows outbreak bands.
- Condemnation: chemical, biological, atrocity, and coverup sources remain distinct; latent attribution pays only the unpaid public share as evidence rises.
- Chaos: existing Deaths and Air Cleanliness rules remain authoritative; ordinary CBRN use does not add a second large direct chaos gain.
- Sanctions: later tiers affect offensive production, imported materials, research, aircraft, trucks, and instruments while humanitarian carve-outs can preserve defensive aid.

## Source files

| Surface | File |
| --- | --- |
| Shared constants | `common/script_constants/cbrn_system_constants.txt` |
| Shared triggers | `common/scripted_triggers/cbrn_triggers.txt` |
| Protection/readiness effects | `common/scripted_effects/cbrn_protection_effects.txt` |
| Exposure/action effects | `common/scripted_effects/cbrn_exposure_effects.txt` |
| Helper contract evidence | `docs/plans/chaos_warfare_system_plans/2026-07-13_stage_1_shared_data_model.md` |
| Protective equipment | `common/units/equipment/cbrn_protective_equipment.txt` |
| Protective technology | `common/technologies/chaosx_technologies.txt` |
| Protection decisions | `common/decisions/cbrn_protection_decisions.txt` |
| Protection decision effects | `common/scripted_effects/cbrn_protection_decision_effects.txt` |
| Protection triggers | `common/scripted_triggers/cbrn_protection_triggers.txt` |
| Starting profiles | `common/scripted_effects/cbrn_starting_protection_effects.txt` |
| Protection production AI | `common/ai_strategy/cbrn_protection_production.txt` |
| Maintenance/events | `events/cbrn_protection_events.txt` |
| Stage 2 sprites | `interface/cbrn_protection.gfx` |
| Stage 2 implementation evidence | `docs/plans/chaos_warfare_system_plans/2026-07-13_stage_2_protective_equipment.md` |

The mapped units, Army Headquarters layer, doctrine, officer corps, route adapters, payloads, biological lifecycle, designers, achievements, and consequence dispatcher have separate implementation and audit records under `docs/plans/chaos_warfare_system_plans/`. The five-tab operational GUI and several visual-animation surfaces remain explicitly tracked there as audit items rather than being represented as completed by this overview.

## Asset registry

Stage 2 assets live under `docs/assets/chaos_warfare_system/stage_2_protective_equipment/`. `interface/cbrn_protection.gfx` registers purpose-built final DDS art for eleven technologies, fourteen equipment/model cards, two decision categories, nineteen decisions, five exact-state response modifiers, and the defective-reconditioned-batch report event. No placeholder or cross-type resized substitute is used.

Before each later visible stage is implemented, stable gameplay and sprite identifiers must be registered and produced through `chaos-redux-event-assets`; animation also requires `chaos-redux-frame-animation`.

The complete required families are:

- doctrine: grand doctrine, four track adoptions, twenty mastery rewards, four milestones
- technology: four gas-mask models; decontamination, instruments, treatment, delivery, HQ, and biosecurity technologies
- unit: six Army HQ companies, ten regimental companies, Chaos Assault Battalion, required counter/text variants
- equipment: four protective sets, three decontamination models, three instrument models, class payloads, shell lots, and air payload lots
- decisions: five categories and all program, distribution, operation, containment, inspection, retaliation, suppression, and occupation actions
- ideas/officer corps: readiness, policies, reserve/shortage, medical/safety, retaliation, and six mapped spirits
- state modifiers: five chemical contamination classes, civilian protection, decontamination corridor, medical saturation, quarantine, and biological states
- designers: six mapped CBRN MIO families
- UI: window/background/header, five tab-state families, meters, severity frames, attribution markers, operation cards, warning overlays
- animation: readiness seal, Severe/Catastrophic warning border, operation-preparation indicator, each with real frames and static fallback
- achievements: completed, grey, and ineligible 64x64 assets for the eleven supported achievements; four unsupported proposals remain archive-only and unregistered

Chemical special-project prototype rewards use the exact, already-registered agent project icons `GFX_sp_sarin_bomb`, `GFX_sp_soman_bomb`, `GFX_sp_malodor_bomb`, and `GFX_sp_aphrodisiac_bomb`. They remain on the special-project project-icon surface and do not replace the preserved raid icons under `gfx/interface/military_raids/`.

Working sources belong under `docs/assets/chaos_warfare_system/`. Final DDS paths and sprite names will be recorded in that package's manifest and `gfx_handoff.md`; GFX registration will use type-specific interface files, never resized cross-type substitutes.

## Future implementation stages

- consolidated regimental support and protected assault battalion
- Army Headquarters companies and abilities
- doctrine, technologies, officer corps, and command roles
- chemical route migration and exact-state raids
- biological lifecycle and targeted self-scheduling
- unified consequences, diplomacy, and sanctions
- nerve suppression and bounded occupation policy
- differentiated AI, country programs, and current-schema designers
- final UI, localisation, assets, achievements, audits, and thirty balance scenarios

These are required implementation stages, not optional ideas. The system is incomplete until the package completion audit proves every stage.
