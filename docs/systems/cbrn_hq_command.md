# CBRN Army Headquarters command system

## Purpose

Army Headquarters is the theater layer of the CBRN system. Six HQ-only support companies expose seven paid commander abilities for chemical planning, protection, decontamination, cordons, medical response, biological containment, and a doctrine capstone. Regimental CBRN companies remain the division layer.

This layer prepares and sustains an order. It does not select a state, choose an agent, release a payload, create contamination or an outbreak, record deaths or evidence, or change Condemnation by itself. Exact delivery and selected-state adapters remain owned by the shared exposure, biological, and consequence stages.

Doctrine may reduce the Condemnation impact of an operation. That mitigation does not erase evidence, attribution, casualties, contamination, medical saturation, confirmed-use history, or the strategic and mass-casualty floors.

## Headquarters companies

All six companies are `group = support`, Army-HQ-only, zero-width, non-regimental subunits using the current 1.19 `Thunder at Our Gates` HQ surface. Matching `essential` and `need` tables make their native statistics scale with real reinforcement shortages.

| Company | Standing manpower and equipment | Unlock | Ability |
| --- | --- | --- | --- |
| CBRN Operations Section | 350 manpower; 60 support, 30 masks, 20 instruments | adopt Integrated Chemical Operations | Prepare Chemical Offensive; Combined CBRN Overmatch visibility |
| Chemical Intelligence and Weather Cell | 275 manpower; 50 support, 30 instruments, 10 trucks | Operational Recon Grids | Seal Operational Area |
| Protective Logistics Section | 400 manpower; 80 support, 80 masks, 30 trucks | Signal Intelligence Fusion | Theater Protective Posture |
| Mobile Decontamination Column | 550 manpower; 100 decon, 60 trucks, 40 masks, 50 support | Counter-Contamination Routing | Decontamination Corridor |
| Medical Countermeasure Directorate | 400 manpower; 70 support, 25 trucks, 30 masks | Mobile CBRN Hospitals | Mass Antidote and Casualty Response |
| Biological Security Section | 450 manpower; 60 support, 40 instruments, 40 decon, 25 trucks | Air-Surface Chemical Link | Seal Operational Area; Seal Infection Corridor |

Protective Logistics and Mobile Decontamination do not receive generic organization, attack, or all-terrain attrition substitutes. Their CBRN-specific results belong to the protection and exact-state adapters.

## Ability lifecycle

1. The ability checks a deployed Army HQ, exact required company composition, current policy/context, no existing CBRN HQ commitment, full force-band command power, and a complete real operating package.
2. The native ability charge pays the light-band minimum. Its one-time effect pays the exact standard/mass remainder, debits real stores, stores an operation identity, calculates readiness-scaled preparation, applies a timed preparation status, and schedules bounded hidden events.
3. Preparation completion rechecks the deployed command, exact company, and current context. A failed recheck removes benefits but retains the commitment lock until its planned end, preventing stale delayed events from colliding with another operation.
4. A valid operation applies one timed active status. A finite persistent tick budget schedules only the weekly installments that occur before the exact active end date.
5. Each installment rechecks active status, company, context, and the full weekly package for the force band stored at activation. Reorganizing the army therefore cannot lower a commitment after it is placed. A failed payment removes benefits and stops the chain. Medical or manpower committed at activation remains unavailable until the planned recovery date.
6. One targeted final leader event clears the operation identity and status. Targeted country events restore the exact committed medical or manpower amount. There is no daily, weekly, monthly, or other all-country pulse.

## Force bands, preparation, and costs

The commander’s exact `num_battalions` selects the band:

- light: fewer than 100 battalions;
- standard: 100 through 199;
- mass: 200 or more.

Chemical Readiness modifies preparation: below 40 takes 150 percent, 40–59 is baseline, 60–79 takes 85 percent, and 80–100 takes 75 percent. The Operations Section shortens Prepare Chemical Offensive and Combined CBRN Overmatch by ten percent, and those two preparations receive a further five-percent reduction at 90 or more military respiratory protection. Theater Contamination Doctrine then multiplies only those two offensive preparation times by 0.90; Terminal Hazard Doctrine multiplies them by 0.80. Every result is rounded and clamped to the ability range.

| Ability | Preparation | Active | Cooldown | Full command power by band |
| --- | ---: | ---: | ---: | ---: |
| Prepare Chemical Offensive | 7–21 days | 7 days | 90 days | 20 / 40 / 60 |
| Theater Protective Posture | 1–3 days | 28 days | 14 days | 10 / 22 / 35 |
| Decontamination Corridor | 3–7 days | 28 days | 30 days | 10 / 28 / 45 |
| Seal Operational Area | 2–7 days | 30 days | 30 days | 10 / 22 / 35 |
| Mass Antidote Response | 1 day | 14 days | 30 days | 10 / 25 / 40 |
| Seal Infection Corridor | 2–5 days | 60 days | 45 days | 15 / 30 / 45 |
| Combined CBRN Overmatch | 14–30 days | 10 days | 180 days | 50 / 55 / 60 |

Operating packages are centralized in `common/script_constants/cbrn_hq_constants.txt`. Gas masks, decontamination models, and instrument models are removed oldest-first. Chemical preparation, protective posture, and overmatch require a positive military-issued mask ledger and enough real military filter condition for the entire force-band debit before activation or upkeep. The shared mask-loss helper then consumes that condition, including the exact reduction from filter-standardization technology, and records the amount actually paid. Support equipment, trucks, fuel, Medical Capacity, and reserved cordon manpower use exact typed debits. Seal Infection Corridor commits both medical capacity and force-band cordon manpower for its planned duration. All amounts are gameplay tuning rather than historical inventory claims.

Prepare Chemical Offensive and Combined CBRN Overmatch require a positive supported chemical-payload stock signal, but they do not remove an arbitrary generic payload. The delivery adapter must reserve and consume the player-selected agent before calling the shared exposure pipeline.

The doctrine-gated `chemical_operations_commander` trait reduces preparation for all seven CBRN HQ abilities by ten percent after the normal readiness, Operations Section, and high-protection adjustments. The mutually exclusive offensive doctrine multiplier applies after that commander adjustment and only to Prepare Chemical Offensive and Combined CBRN Overmatch. Neither effect grants release authority or reduces equipment, Command Power, upkeep, duration, or cooldown.

## Doctrine and technology wiring

Integrated CBRN Command owns the five doctrine companies. Each mastery reward unlocks its mapped company. Counter-Contamination Routing grants the non-researchable `mobile_decontamination_columns` technology, Air-Surface CBRN Link grants the `chemical_air_interdiction` eligibility marker, and Theater Intelligence Overmatch qualifies the non-researchable `theater_cbrn_headquarters` technology. Mobile CBRN Hospitals owns the medical directorate.

Delivery Integration's protected-order history is recorded only when Theater Protective Posture completes preparation successfully. Starting the ability, paying its activation package, or later failing preparation does not satisfy the institutional proof.

Combined CBRN Overmatch follows the stricter matrix composition: Theater CBRN Headquarters plus Operations, Protective Logistics, and Mobile Decontamination. This occupies the mandatory HQ staff slot plus three CBRN support slots and fits the verified four-slot Army HQ.

## Exact-state decontamination assignment

While at least one commander has an active Decontamination Corridor and Theater Exploitation is established, `cbrn_assign_decontamination_corridor` can target one controlled state with actual chemical contamination. The assignment removes 10 points from Trace/Local contamination, 8 from Serious, 5 from Severe, or 3 from Catastrophic, records the amount actually removed through the state ledger, and applies a 28-day state and national assignment lock. Theater Contamination Doctrine multiplies cleanup output by 1.25.

The assignment never clears evidence, attribution, deaths, Condemnation, or confirmed-use history. The national lock is the conservative current-version binding: commander abilities do not expose a stable selected-state pointer, so no unsupported random-state, capital-state, or multi-state substitute is used.

## AI behavior

The baseline AI extends vanilla `hq_role` with five targets rather than replacing the generic HQ:

- protected HQ: HQ staff, Protective Logistics, Medical Countermeasure;
- chemical fire-plan HQ: HQ staff, Operations, Intelligence/Weather;
- contaminated-theater HQ: HQ staff, Operations, Mobile Decontamination;
- biological-containment HQ: HQ staff, Biosecurity, Medical Countermeasure;
- overmatch HQ: HQ staff, Operations, Protective Logistics, Mobile Decontamination.

Every target requires exact unlocks, relevant policy/context, and a complete standing bill. The common infantry-equipment bill is 420: four vanilla infantry battalions at 100 each plus 20 for the mandatory HQ staff. Ability AI is disabled by default and gains positive weight only when the full player-equivalent activation trigger passes. Theater Contamination and Terminal Hazard add offensive-preparation weight only after that trigger succeeds. Offensive AI cannot prepare under defensive-only policy or without supported payload stock. Country-profile differentiation remains a later AI stage; these safety and supply gates remain authoritative.

## Verified engine limits

- Current 1.19 script can query exact HQ company presence but cannot query the fulfillment percentage of one named support company inside the deployed HQ. Native `essential`/`need` scaling handles company statistics, while abilities use exact national reserve gates and real debits. No aggregate-army fill estimator is retained.
- A commander ability exposes no selected-state target. Decontamination therefore uses the separate player-selected assignment above; cordon resistance, spread, evidence, and containment changes still require their own later exact-state adapters. No random, capital-state, every-state, or country-wide substitute is used.
- The Army HQ surface is DLC-owned. No non-HQ fallback company or hidden ordinary-division substitute is provided.
- Ordinary continuously assigned chemical-capable aircraft receive no contamination hook here. Only a verified eligible-activity hook may add that behavior later; idle aircraft can never contaminate a region.

## Assets and wiring

The asset package under `docs/assets/chaos_warfare_system/stage_4_hq_command/` retains source frames, independent large/small compositions, processed PNGs, contact sheets, manifest, and handoff.

Runtime wiring:

- six two-frame `152x42` HQ counter sheets in `gfx/interface/counters/divisions_large/`;
- six independently composed two-frame `60x12` map-counter sheets in `gfx/interface/counters/divisions_small/`;
- seven dedicated `34x33` ability icons in the runtime ability icon folder;
- one dedicated `64x64` Theater CBRN Headquarters technology icon in `gfx/interface/technologies/`;
- company sprites in `interface/chaosx_subuniticons.gfx`;
- ability sprites in `interface/chaosx_ability.gfx`;
- technology sprite in `interface/chaosx_techtree.gfx`.

No runtime asset may be a placeholder or a resized cross-type substitute.

## Future integration and suggestions

Required later-stage integration:

- reserve and debit the exact selected chemical agent and delivery lot before a prepared order can dispatch exposure;
- attach cordon, resistance, spread, evidence, and containment benefits to exact selected-state decisions/adapters while retaining the implemented decontamination assignment;
- attach Biosecurity and Infection Corridor to distinct-agent detection, incubation, spread, containment, and treatment;
- extend route-aware country AI profiles while preserving hard safety gates;
- migrate legacy ability and company identifiers without losing active or unlocked state;
- run live Army HQ designer, shortage, force-band, preparation, upkeep-failure, AI-use, and cleanup scenarios.

Possible depth after the accepted package is complete: commander history entries for major CBRN commitments, theater-specific after-action reports, and designer UI summaries of the selected operating package. These suggestions must not bypass exact payload/state selection or introduce a global periodic pulse.
