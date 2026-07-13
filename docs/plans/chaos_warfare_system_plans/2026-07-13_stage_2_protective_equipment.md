# Chaos Warfare Stage 2 protective equipment

Date: 2026-07-13

Status: complete.

## Authority and scope

This tranche follows Stage 2 of `handoffs/staged_implementation_plan.md` and implements the accepted protective-equipment requirements from numbered specs 04 and 07. It covers producible gas-mask, decontamination, and CBRN-instrument equipment; technology progression; national reserve and military-issue ledgers; state civilian distribution; filters, fitting, losses, replacement demand, transfer cleanup, decisions, AI, UI/localisation, starting profiles, and type-correct assets.

It does not activate a chemical delivery route or approximate continuous air activity. The shared Stage 1 exposure contract remains fail-closed until a later route adapter supplies a real payload debit, equipment-backed protection, and verified conditions.

### Resolved package naming conflict

Numbered spec 04 names the 1940 and 1942 mask models `Advanced CBRN Protective Set` and `Sealed Protective Set`, and names the later decontamination models `Mobile Decontamination Plant` and `Advanced Rapid Decontamination Set`. The lower-priority subunit/equipment matrix and asset prompt instead use `Advanced Protective Set`, `Sealed Assault Set`, `Mobile Wash Column`, and `Rapid Decontamination Plant`. The numbered-spec names govern equipment and player-facing model localisation. The technology branch retains its distinct accepted technology names, including `Advanced Protective Clothing`, `Sealed Assault Protection`, `Mobile Wash Columns`, and `Rapid Decontamination Plants`; no model or technology is omitted because of the naming difference.

## Verified engine surfaces

Installed 1.19.2 documentation and vanilla examples confirm the following exact dynamic variables and effects:

| Surface | Use |
| --- | --- |
| `num_equipment@type` | Actual country stockpile of one model or archetype. |
| `num_equipment_in_armies@type` | Actual model or archetype deployed in divisions. |
| `num_target_equipment_in_armies@type` | Current fielded requirement for later shortage diagnostics. |
| `deployed_army_manpower_k` | Military issue demand; one crate per 100 deployed personnel uses `deployed_army_manpower_k * 10`. |
| `state_population_k` | Civilian issue demand; one crate per 1,000 residents uses the value directly. |
| `add_equipment_to_stockpile` | Model-specific additions and negative debits with dynamic amounts. |
| `send_equipment` | Model-family exports with a dynamic amount and explicit recipient. |
| `on_state_control_changed` | Controller transfer cleanup; ROOT is the new controller, FROM is the old controller, and FROM.FROM is the state. |

No stockpile estimator is retained.

## Stable identifiers

### Equipment

- `gas_mask_equipment_1` through `gas_mask_equipment_4`: Basic Respirator Crate, Improved Service Mask Crate, Advanced CBRN Protective Set, and Sealed Protective Set.
- `gas_mask_equipment_reconditioned`: a decision-only, non-producible stopgap model recovered from the damaged/rejected-mask cache; it never replaces a researched production model.
- `decontamination_equipment_1` through `decontamination_equipment_3`: Field Decontamination Kit, Mobile Decontamination Plant, and Advanced Rapid Decontamination Set.
- `cbrn_instrument_equipment_1` through `cbrn_instrument_equipment_3`: Field Detection Set, Mobile Sampling Laboratory, and Theater CBRN Command Set.

### Technologies

- Existing `basic_gas_masks`, `improved_gas_masks`, and `advanced_gas_masks` unlock the first three mask models without changing their compatibility identifiers.
- `sealed_assault_protection` unlocks the fourth model.
- `civil_defence_fitting_and_registration`, `military_filter_standardization`, `rapid_filter_replacement`, and `vehicle_overpressure_and_sealed_compartments` complete the numbered-spec applied-protection branch. They respectively reduce organized civilian distribution consumption, filter/exposure loss, filter-service consumption, and friendly armored-delivery crew exposure.
- `field_decontamination_kits`, `mobile_wash_columns`, and `rapid_decontamination_plants` unlock the decontamination chain.
- `chemical_detection_paper`, `mobile_sampling_laboratories`, and `theater_cbrn_command_set` unlock the instrument chain.

### Decision categories

- `cbrn_program_management_category`
- `cbrn_civil_defence_category`

## Equipment and allocation contract

The national reserve is the real equipment stockpile. Research never supplies protection by itself.

Military issue debits real stock and enters non-reclaimable, model-specific ledgers. Division equipment later contributes through `num_equipment_in_armies@model`; it is not duplicated in the general-issue ledger. Raw coverage is measured against current deployed-manpower demand. Respiratory, skin, and warning protection then use the lower of that usable coverage and the weighted average quality of the masks actually issued. Exposure and alert posture consume filters and create replacement demand.

Civilian distribution is state scoped. It debits real model stock, stores raw issued crates and model-quality points, and calculates coverage from the current state population. Priority issue, full issue, emergency issue, filter replacement, old-stock reconditioning, occupation supply, and export remain distinct actions. Distributed stock cannot be reclaimed at full value or converted into free equipment.

State control transfer removes the old controller's aggregate distributed total, assigns the surviving stock to the new controller, and applies the accepted turnover/occupation loss. It never credits the national reserve.

## Population and condition scaling

- Priority distribution targets 50 percent of state need.
- Full distribution targets 95 percent.
- Emergency distribution targets 35 percent effective coverage. Its raw allocation target is derived from that effective target after the emergency fitting and filter multipliers, so the decision does not stop after issuing too few crates; with the current 0.65 fitting and 0.65 filter factors it allocates 82.84 percent of raw state need.
- Capital, urban, infrastructure, registration, civil-defence institution, occupation, and verified active-raid state affect cost or effective coverage.
- An active-bombing modifier may be supplied only by a verified raid-alert flag. Ordinary air presence, idle chemical aircraft, and region estimates do not qualify.

## Starting stock methodology

Starting totals are gameplay tuning inside `matrices/gas_mask_starting_stockpile_matrix.md` bands, not precise historical inventories. Relative historical confidence is retained separately from exact-total confidence. Britain receives the largest reserve and strongest civilian distribution. France and Germany receive large mixed basic/improved stocks; the Soviet Union and Japan are military-first; the United States begins with a moderate industrial reserve and low public distribution; First World War and exposed secondary powers receive smaller differentiated stocks; most small minors receive no automatic reserve.

Starting stock, military issue, and civilian distribution are separate. Military issue targets use the matrix's fielded-need percentages, including values above 100 percent for training, mobilization and replacement stocks; the protection result remains capped. Every debit is limited by the exact tuned starting stock, and civilian distribution receives only the real stock remaining after military issue. A technology grant never implies a full reserve or distribution program.

## Production tuning

Gas-mask model IC ratios are exactly 1.00, 1.35, 1.80, and 2.50 from the accepted spec. The base cost is tuned below infantry equipment because one item represents a standardized crate, while population-scale demand makes the total program expensive. Reliability is exactly 0.70, 0.82, 0.90, and 0.94.

Decontamination and instrument chains are tuned against vanilla support equipment. Their cost rises with mobility, sealed handling, laboratory capability, and command communications. These are gameplay values and will be revisited during the required low/normal/high-chaos scenario pass.

## Mask-production AI

The engine exposes static `equipment_production_factor` and `equipment_production_min_factories_archetype` AI strategies; it does not accept a calculated percentage as an AI-strategy value. The accepted 4 to 10 percent mask-production band is therefore mapped to non-overlapping military-industry ranges:

| Military factories | Minimum respirator factories | Share across the band |
| ---: | ---: | ---: |
| 10 to 24 | 1 | 4.2 to 10 percent |
| 25 to 49 | 2 | 4.1 to 8 percent |
| 50 to 74 | 4 | 5.4 to 8 percent |
| 75 to 99 | 6 | 6.1 to 8 percent |
| 100 or more | 8 | 8 percent at 100, with profile and urgent production factors controlling further allocation |

Countries below ten military factories use procurement, reconditioning, conversion, licence, and allied-aid decisions instead of an unaffordable forced production line. Minimum-factory pressure stops when profile-specific military coverage, reserve/replacement demand, and eligible civilian-distribution targets are met.

Production starts only with Basic Service Respirators and a real signal: an established reserve, field shortage, replacement backlog, enemy capability or confirmed use, public world use, Chaos Warfare posture, exact raid alert, or an allied request. Mass-civil-defence, prepared-power, military-first, industrial-reserve, civil-defence network, exposed/fragmented, limited, and minimal profiles receive distinct target and production weights. Confirmed use, an exact alert, or military coverage below 50 percent adds an urgent production factor.

Decontamination and instrument production ratios remain queued for Stages 3 and 4, when their real regimental-support and Army Headquarters requirements exist. They are not assigned speculative stock targets in Stage 2.

## Asset contract

The asset workflow owns separate, purpose-built technology, equipment-card, category, state-modifier, and decision art. Its 51-row icon manifest is closed: 11 technology icons, 14 equipment cards/archetype icons, two category icons, 19 decision icons, and five state-modifier icons each have a source PNG, processed PNG, packaged DDS, runtime DDS, exact gameplay identifier, and registered sprite. A separate 210x176 report-event image has source, processed master, final mipmapped DDS, contact sheet, manifest, and registered sprite. Existing gas-mask technology art remains valid only for its existing technology-card type; it was not resized or reused as equipment or decision art.

## Meaningful validation and audit findings

The protection calculation was exercised at the accepted model boundaries. Reconditioned masks cap protection at 38.5 under full coverage; Basic Service Respirators provide 25, 35, and 50 protection at those partial coverage levels and cap at 55 at full issue; improved, advanced, and sealed models cap full issue at 75, 90, and 100. Emergency state distribution from an empty ledger derives an 82.84 percent raw allocation and resolves to the intended 35 percent effective coverage with a basic-mask score of 35. A degraded-ledger scenario that already had 50 percent raw issue but only 12.5 percent effective coverage exposed a raw-gap no-op; the shared distributor now derives the effective gap first and grosses the issue request up through current fitting and filter factors, producing a 37.5 percent request in that case.

The decision/mission audit tightened exact-state response gating, made alert categories visible when a real state alert is registered, and starts the recipient/controller maintenance lifecycle after exports or state-control inheritance. The exact-state alert registration helper remains intentionally fail-closed until a later chemical-delivery adapter supplies a verified selected-state raid alert; country-wide confirmed use is not accepted as a substitute.

The localisation audit covers all 19 decisions, seven custom-cost key triplets, two decision categories, five dynamic modifiers, one opinion modifier, the visible event, three equipment archetypes, eleven equipment models, three technology categories, and fourteen technologies. It found no missing or duplicate target keys, preserved UTF-8 BOM encoding, and confirmed that every scripted-localisation and dynamic-constant reference resolves.

The generated asset set has been visually reviewed by type. The current DDS surfaces are 32x32 decision icons, 52x40 category icons, 64x64 technology/state icons, 131x52 equipment cards following the repository equipment-card precedent, and a 210x176 report-event image with mipmaps. All 52 registered sprite names are unique and every referenced runtime texture exists; the icon manifest has no missing source, processed, packaged, or runtime file and all 19 decision gameplay identifiers match their scripts.

The 30 starting profiles were checked against all 20 matrix-listed countries: every matrix country has an exact profile, the ten additional profiles are deliberate exposed/secondary cases, and Britain's 45,000-crate reserve is the largest. Shared script-constant references resolve through all nested categories, every Stage 2 scripted-effect and scripted-trigger call resolves, and all newly introduced or modified public helpers are documented in the dynamic helper references. The mask-production AI's factory bands are centralized as file-local tuning constants rather than embedded trigger thresholds.

## Simplifications, omissions, and blockers

There are no Stage 2 simplifications, omissions, fallbacks, estimators, or placeholder assets. Exact-state raid-alert registration intentionally remains fail-closed until the mapped chemical-delivery stage can call it from a verified selected-state route; activating that later adapter is outside this tranche and no country-wide or regional approximation was retained.

## Exit requirements

- All ten production models are producible only after their mapped technology unlock; the separate reconditioned model is non-producible and can enter stock only through the recovery decision.
- Stockpile, issue, state distribution, quality, filter loss, replacement demand, and transfer cleanup are real and inspectable.
- Every legacy protection check uses equipment-backed coverage rather than technology ownership.
- Starting profiles follow the accepted matrix and Britain is strongest.
- AI production and allocation use differentiated route/country profiles.
- Localisation, sprites, documentation, and `common/script_enums.txt` are aligned.
- No placeholder asset, broad country pulse, estimator, fallback, or undisclosed approximation remains.
