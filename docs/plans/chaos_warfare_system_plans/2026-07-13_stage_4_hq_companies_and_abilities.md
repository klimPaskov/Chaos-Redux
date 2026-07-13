# Stage 4: CBRN Army Headquarters companies and commander abilities

Date: 2026-07-13

Status: source-complete and specialist-audited; live Army HQ scenarios remain assigned to Stage 14.

## Authority and tranche boundary

This tranche implements Stage 4 of `handoffs/staged_implementation_plan.md` against numbered spec 03 and `matrices/hq_and_ability_matrix.md`. It owns six Army Headquarters support companies, seven company-gated commander abilities, exact force-size command-power bands, equipment-backed activation and upkeep, bounded delayed preparation, active-duration state, cleanup, baseline HQ templates, ability AI, localisation, icons, and mechanic documentation.

The accepted doctrine rule remains fixed: doctrine may reduce Condemnation impact, but it does not erase evidence, attribution, deaths, contamination, medical saturation, confirmed-use history, or strategic and mass-casualty floors. Numbered spec 08 also keeps doctrine separate from camp and genocide infrastructure.

Stage 4 prepares and sustains an Army HQ order; it does not invent a target state or dispatch exposure. Stage 6 owns exact selected-agent and selected-delivery payload reservation, debit, and shared chemical exposure. Stage 7 owns biological operation dispatch. Stages 7 and 8 own exact selected-state containment, cleanup, evidence, deaths, contamination, and outbreak consequences. Stage 9 owns targeted nerve-agent suppression. No Stage 4 ability may create chemical contamination, an outbreak, deaths, evidence, attribution, or Condemnation by itself.

## Verified current-version engine contract

Installed version 1.19 provides the following exact surfaces:

- `allow_in_army_hq = yes`, `allow_in_non_army_hq = no`, `deployed_leader_modifiers`, `enable_ability`, `need`, and Army HQ support categories in vanilla `common/units/hq_support.txt`;
- four Army HQ support slots from `MAX_HQ_SUPPORT_WIDTH = 1` and `MAX_HQ_SUPPORT_HEIGHT = 4`;
- `requires_deployed_hq = yes`, `allowed`, `ai_will_do`, `cost`, `duration`, `cooldown`, and `one_time_effect` in vanilla Army HQ abilities;
- exact CHARACTER-scope `num_battalions_with_type@<subunit>` and `num_battalions` dynamic variables;
- delayed `unit_leader_event`, timed unit-leader traits, and order-wide timed trait modifiers;
- doctrine-root and mastery-reward `effect = { unlock_subunit = ... }`;
- country stock, fuel, manpower, command power, and script-variable gates and debits.

All six companies mirror the vanilla Army HQ-only support structure and require `Thunder at Our Gates`, the DLC that owns the current Army HQ surface. No non-HQ substitute is introduced for installations without that feature.

### Unsupported exact queries and deliberately deferred adapters

The current engine exposes aggregate equipment in the whole army under a commander, but no exact script query for the fulfillment ratio of one named support company inside that commander's deployed HQ. Aggregate army equipment is not a safe proxy. Therefore:

- company statistics and reinforcement use native matching `essential` and `need` equipment;
- ability activation and weekly upkeep use exact national reserve gates and real debits;
- HQ composition is checked exactly with HQ-only `num_battalions_with_type@...` variables;
- no per-HQ equipment-fill estimator is retained;
- documentation and tooltips do not claim that aggregate national stock is the deployed HQ company's fill ratio.

A commander ability also has no native selected-state target. It cannot identify the contaminated route, occupied state, or infection corridor intended by the player. Therefore Decontamination Corridor, Seal Operational Area, and Seal Infection Corridor receive their exact order-level status and costs here, while their cleanup, output, resistance, spread, and evidence effects remain wired to the exact selected-state adapters in Stages 7 and 8. No random state, every controlled state, capital state, or country-wide approximation is allowed.

## Stable identifiers and unlock ownership

| Player-facing company | Stable subunit identifier | Exact unlock owner | Ability exposure |
| --- | --- | --- | --- |
| CBRN Operations Section | `cbrn_hq_operations_section` | adoption of `integrated_chemical_operations` | Prepare Chemical Offensive; capstone visibility |
| Chemical Intelligence and Weather Cell | `cbrn_hq_intelligence_weather_cell` | Operations mastery 1, `operational_recon_grids` | Seal Operational Area |
| Protective Logistics Section | `cbrn_hq_protective_logistics_section` | Operations mastery 2, `signal_intelligence_fusion` | Theater Protective Posture; capstone gate |
| Mobile Decontamination Column | `cbrn_hq_mobile_decontamination_column` | Operations mastery 3, `countercontamination_routing` | Decontamination Corridor; capstone gate |
| Medical Countermeasure Directorate | `cbrn_hq_medical_countermeasure_directorate` | `mobile_cbrn_hospitals` | Mass Antidote Response |
| Biological Security Section | `cbrn_hq_biological_security_section` | Operations mastery 4, `air_surface_chemical_link` | Seal Operational Area and Seal Infection Corridor |

Operations mastery 5, `theater_intelligence_overmatch`, grants the doctrine-only `theater_cbrn_headquarters` technology. That technology is a capstone gate and cannot be researched directly.

The ability matrix contains an internal conflict: its ability row says Combined CBRN Overmatch needs Theater CBRN HQ technology plus two companies, while its combination row requires CBRN Operations plus one protection and one cleanup company. The stricter three-company combination wins because it is the matrix's explicit full-capstone composition and fits the verified four-slot HQ. The exact gate is:

- `theater_cbrn_headquarters`;
- `cbrn_hq_operations_section`;
- `cbrn_hq_protective_logistics_section`;
- `cbrn_hq_mobile_decontamination_column`.

## Company equipment and native passive contract

All six companies use `group = support`, current Army HQ categories, `regimental = no`, zero combat width, `active = no`, Army-HQ-only placement, and matching `essential` and `need` tables. Radios remain represented by vanilla support equipment; no unsupported signal-equipment archetype is invented. Medical stores remain scripted medical capacity backed by support equipment, trucks, protective equipment, and treatment technology; no medical-equipment archetype is invented.

| Company | Manpower | Standing essential equipment | Narrow native passive |
| --- | ---: | --- | --- |
| Operations | 350 | 60 support, 30 masks, 20 instruments | +4% planning speed; its gated offensive abilities receive 10% shorter preparation |
| Intelligence and Weather | 275 | 50 support, 30 instruments, 10 trucks | +10% reconnaissance factor |
| Protective Logistics | 400 | 80 support, 80 masks, 30 trucks | no generic protection proxy; exact CBRN benefit is ability/pipeline-owned |
| Mobile Decontamination | 550 | 100 decon, 60 trucks, 40 masks, 50 support | no all-terrain attrition proxy; contaminated-route benefit is adapter-owned |
| Medical Countermeasure | 400 | 70 support, 25 trucks, 30 masks | narrow wounded and sickness chance reduction |
| Biological Security | 450 | 60 support, 40 instruments, 40 decon, 25 trucks | narrow reconnaissance and sickness chance improvement |

The absence of a generic passive on the protective and decontamination companies is intentional. A broad organization, attack, or all-terrain attrition modifier would conceal the missing CBRN scope and would not be an exact implementation of assigned-order protection or contaminated-route cleanup.

## Ability identifiers and timing

| Ability | Stable identifier | Base preparation | Active duration | Cooldown | CP by affected battalions |
| --- | --- | ---: | ---: | ---: | --- |
| Prepare Chemical Offensive | `cbrn_prepare_chemical_offensive` | 14 days | 7 days | 90 days | 20 / 40 / 60 |
| Theater Protective Posture | `cbrn_theater_protective_posture` | 2 days | 28 days | 14 days | 10 / 22 / 35 |
| Decontamination Corridor | `cbrn_decontamination_corridor` | 4 days | 28 days | 30 days | 10 / 28 / 45 |
| Seal Operational Area | `cbrn_seal_operational_area` | 4 days | 30 days | 30 days | 10 / 22 / 35 |
| Mass Antidote Response | `cbrn_mass_antidote_response` | 1 day | 14 days | 30 days | 10 / 25 / 40 |
| Seal Infection Corridor | `cbrn_seal_infection_corridor` | 3 days | 60 days | 45 days | 15 / 30 / 45 |
| Combined CBRN Overmatch | `cbrn_combined_overmatch` | 20 days | 10 days | 180 days | 50 / 55 / 60 |

The three exact force bands use the commander's current `num_battalions` at activation:

- light order: fewer than 100 affected battalions;
- standard order: 100 to 199 affected battalions;
- mass order: 200 or more affected battalions.

The native ability cost charges the minimum band and the activation effect debits the exact remaining command power for the standard or mass band. The preflight trigger checks the full amount before activation, so a player cannot enter a negative command-power balance.

The selected band is then stored on the commander for the whole commitment. Weekly gates and debits use that stored band, so transferring divisions after activation cannot lower the paid upkeep package. Company and context validity are still rechecked against the command's current state.

Readiness modifies preparation exactly as accepted: below 40 uses 150%, 40 to 59 uses baseline, 60 to 79 uses 85%, and 80 to 100 uses 75%, rounded and clamped to the matrix range. The Operations Section shortens its two gated offensive preparations by 10%. Prepare Chemical Offensive and Combined CBRN Overmatch then apply the accepted further 5% high-protection reduction when the current military protection snapshot is at least 90. Every result is rounded and clamped to the ability's matrix range. Mass Antidote Response remains a one-day emergency preparation.

## Activation, upkeep, and cleanup state machine

1. The visible ability requires a deployed HQ, exact required company composition, no other CBRN preparation or active posture on the same commander, the mapped technology/policy/context, the full force-band command power, and real national operating stock.
2. Activation debits the force-band command-power remainder and the first operating-stock installment atomically, calculates readiness-adjusted preparation, applies the timed preparation status, and schedules one hidden CHARACTER event.
3. The delayed event rechecks the deployed HQ and required company composition. If valid, it replaces preparation with the ability's timed active status and schedules the first weekly upkeep event. Offensive preparation does not dispatch payload or exposure.
4. Each weekly hidden event rechecks the active status, exact company composition, context, and full weekly stock against the force band stored at activation. Successful upkeep debits real stock and reschedules itself. Failed upkeep removes the active status and stops the chain; the operation identity remains locked until the already scheduled final cleanup so a stale event cannot collide with a newer posture. No broad daily, weekly, or monthly country pulse is used.
5. Timed active traits expire without stale flags. Equipment-backed medical capacity and manpower commitments, where used, recover through targeted delayed country events with clamped restoration. Early supply failure still holds the committed capacity through its planned recovery date.

Preparation and active status traits are player-readable. They are not hidden implementation markers: they explain which order is preparing or sustaining a CBRN posture through the normal commander UI.

## Operating-stock ownership

Every ability consumes only resources whose exact identity is known in this tranche. Gas masks are debited oldest-first through the shared protective-equipment helper. Chemical preparation, sustained protective posture, and overmatch require a positive military-issued mask ledger and enough real filter condition for the exact selected force-band debit; filter-standardization technology reduces both the affordability threshold and the paid wear by the same centralized amount. The shared military-mask loss helper applies every assigned positive debit, and the operation records the condition actually consumed. Decontamination and instrument families receive model-aware oldest-first debit helpers. Support equipment, motorized losses, fuel, medical capacity, and temporary manpower commitments use exact typed debits.

Prepare Chemical Offensive and Combined CBRN Overmatch require a real supported payload stock signal, but Stage 4 does not debit an arbitrary agent. Stage 6 must reserve and debit the exact selected agent and delivery lot before an order can dispatch exposure. This preserves the single shared exposure pipeline and prevents an undisclosed generic-payload substitute.

Weekly operating packages are force-band scaled and ability-specific:

- protective posture consumes mask crates, military filter condition, and support stores at activation and each paid weekly installment;
- decontamination corridor consumes decon material, masks, support stores, vehicle attrition, and fuel;
- sealed operational area consumes support stores and reserves manpower;
- antidote response consumes support stores, masks, and medical capacity;
- infection corridor consumes decon material, instruments, masks, support stores, and commits medical capacity plus cordon manpower;
- overmatch consumes large protective, decon, instrument, support, vehicle, fuel, and medical packages, with exact payload added by Stage 6.

All amounts are gameplay tuning, not historical stockpile claims.

## AI contract

Baseline HQ templates extend `hq_role` without replacing vanilla's generic HQ:

- protected HQ: base HQ staff + Protective Logistics + Medical Countermeasure;
- chemical fire-plan HQ: base HQ staff + Operations + Intelligence/Weather;
- contaminated-theater HQ: base HQ staff + Operations + Mobile Decontamination;
- biological containment HQ: base HQ staff + Biological Security + Medical Countermeasure;
- capstone HQ: base HQ staff + Operations + Protective Logistics + Mobile Decontamination.

Each template requires its exact unlocks and a complete real standing-equipment bill. Ability `ai_will_do` uses current policy, war state, readiness, payload stock, actual contamination/outbreak/emergency signals, full operating stock, company composition, and command power. Offensive ability AI remains disabled under defensive-only policy. Stage 10 replaces baseline weights with the accepted route-aware country profiles; Stage 4 proves viable HQ construction and context-gated use without authorizing exposure.

## Asset contract

Each HQ company receives two independently composed two-frame unit-counter sheets:

- large division-counter sheet: `152x42` DDS, two purposeful `76x42` frames;
- small map-counter sheet: `60x12` DDS, two purposeful `30x12` frames.

The small composition is not a resize of the large one. Each of the seven abilities receives a dedicated `34x33` DDS icon. `theater_cbrn_headquarters` receives a dedicated `64x64` technology icon. Source masters, processed PNGs, exact runtime DDS files, prompts, manifest, contact sheets, and GFX handoff live under `docs/assets/chaos_warfare_system/stage_4_hq_command/`. The twenty runtime textures are registered through the existing subunit, ability, and technology GFX files under the stable identifiers used by gameplay.

## Validation scenarios

1. Each company appears only in an Army HQ support slot after its mapped unlock and cannot enter a normal division support slot.
2. Removing one required HQ company removes or blocks its ability; Combined CBRN Overmatch requires all three strict capstone companies and the Theater technology.
3. Light, standard, and mass commands pay the mapped full CP amount and the matching operating package based on exact affected battalions. Reorganizing the command afterward does not lower weekly upkeep below its stored activation band.
4. Readiness produces the mapped preparation bands; no active status appears before the delayed preparation event.
5. Weekly stock succeeds while all resources exist, wears real issued-filter condition where mapped, and terminates the active status at the first unpaid installment without leaving a rescheduling loop. Filter standardization reduces the condition loss.
6. Offensive preparation with no Stage 6 selected-payload debit creates no exposure, contamination, deaths, evidence, attribution, or Condemnation.
7. State-facing abilities create no random or country-wide state effect before their exact selected-state adapters are present.
8. AI creates only fully unlocked and supplied HQ templates and does not use offensive abilities under defensive-only policy or without real payload stock.
9. All preparation, active, cooldown, capacity-restoration, and manpower-restoration paths clean themselves without a broad periodic pulse; Infection Corridor restores both its medical and manpower commitments at the planned end.

## Source-audit evidence

- Static contract review resolves all 276 `cbrn_hq_*` script-constant leaves exactly once and finds no unresolved or unused Stage 4 constant. All 43 new scripted effects and 60 new scripted triggers are called, explicitly documented with scope/contracts, and free of unresolved helper references.
- The completion specialist found that the first filter-wear implementation could skip the condition debit when the military mask aggregate was empty and did not preflight exact condition affordability. The corrected contract adds fail-closed issued-mask and exact base/standardized condition gates for all nine operation/force-band combinations, removes the silent-skip branch, and records the actual condition consumed. The follow-up completion audit verified the same 85-percent technology reduction in affordability and debit paths and returned `COMMIT` with no remaining exact defect.
- Six company identifiers, seven ability identifiers, eight status-trait identifiers, their localisation contracts, and all twenty runtime sprite registrations match exactly. Every registered Stage 4 texture path resolves and no new sprite identifier collides with another registration.
- The bounded event-chain report contains no blocker. It reports nine `EVENT_UNREACHABLE_IN_SELECTION` warnings for `cbrn_hq.1`, `.2`, `.3`, and `.20` through `.25` because their callers are delayed through scripted helpers that the static graph does not discover. A redundant cleanup-variable gate found by the first pass was removed. Two unrelated event-analysis sources were skipped by the tool, so this evidence is not represented as a whole-repository pass.
- The localisation specialist found missing cooldown disclosure, incomplete active penalties, repeated undefined force-band language, two overly broad Condemnation phrases, and one grammar defect. The final text now exposes all seven cooldowns, exact active modifiers, one shared force-band definition, and the accepted rule that doctrine mitigates Condemnation only without erasing evidence or attribution.
- The asset specialist delivered and checked six large two-frame counters, six independently composed small two-frame counters, seven ability icons, and one technology icon. Parent review rejected no final runtime file; three flawed generations had already been discarded and regenerated before integration. All twenty DDS headers, dimensions, frame counts, alpha ranges, and registered paths match the manifest.

Live Army HQ designer, reinforcement-shortage, force-band, delayed-chain, AI-use, and cleanup scenarios remain explicitly owned by Stage 14 and are not claimed by this source audit.

## Later-stage integration

- Stage 5 completes doctrine bonuses, doctrine-only visibility, officer corps, traits, and doctrine balance while preserving these unlock IDs.
- Stage 6 makes prepared chemical orders reserve and consume the exact selected payload and call the shared exposure pipeline.
- Stage 7 connects Biological Security and Infection Corridor to distinct-agent detection, spread, containment, and treatment.
- Stage 8 gives exact selected states cleanup, sealing, evidence-preservation, contamination, medical, death, and Condemnation consequences.
- Stage 9 connects targeted nerve suppression without reusing the headquarters ability as a country-wide occupation proxy.
- Stage 10 differentiates HQ templates and ability preferences by country profile and route.
- Stages 13 and 14 perform the specialist audits and live scenario matrix before any overall completion claim.
