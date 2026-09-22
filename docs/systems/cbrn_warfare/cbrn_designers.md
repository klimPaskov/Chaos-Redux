# CBRN Military Industrial Organizations

## Current accepted and source-backed contract

The user's explicit 2026-09-20 implementation request accepted three twelve-node generic MIO families, six historical national organizations, two fictional advanced organizations, and six broad industrial concerns. Current source defines `cbrn_chemical_protection_consortium` (masks and decontamination), `cbrn_biomedical_industry_directorate` (instruments and four biological bombs), and `cbrn_delivery_engineering_bureau` (nine exact chemical-agent payload archetypes, chemical artillery, and four chemical-air payloads). Their definitions live in `common/military_industrial_organization/organizations/cbrn_chemical_protection_organizations.txt`, `cbrn_biomedical_organizations.txt`, and `cbrn_delivery_organizations.txt`; national and advanced variants live in `cbrn_national_organizations.txt`. The exact owner evidence and identity/gate mapping are in `docs/plans/chaos_warfare_system_plans/subagent_handoffs/2026-09-20_cbrn_mio_industry_redesign_handoff.md`.

`interface/cbrn_mio_industry.gfx` registers eight organization logos, six concern cards, and 21 exact equipment badges. Each badge token follows `GFX_military_industrial_organization_<archetype>`; nine exact chemical-agent aliases share `gfx/interface/military_industrial_organization/cbrn_badges/chemical_agent_payload.dds`, while chemical artillery, four air payloads, masks, decontamination gear, instruments, and four biological bombs have separate textures. The handoff lists every exact filename. The icon artist owns binary completion, so sprite registration is not final art evidence. The owner reports +34% maximum dedicated capacity, +31% reliability, and +32% MIO research with no attack bonus; the parent still must check combined limits and runtime assignment.

The treatment constants are now 0.85 for six MIO harm/medical reductions and 1.30 for distributed-surveillance detection. The older interpretation of 40–60% standalone MIO treatment benefits is superseded. The biological lifecycle and exposure owners retain final combined treatment-floor review, and the probability auditor retains scenario evidence. The old six-family source files, generic `chemical_agent_payload` archetype target, and old organization sprites described below are retired. The following sections are a historical implementation account only and are not instructions for current gameplay, source paths, costs, AI, or assets.

The parent accepted the exact twelve-node biomedical tree on 2026-09-20: its existing `cbrn_medical_respiratory_care` foundation trait serves as **Respiratory and Burn Care**, with no thirteenth Burn Treatment node. Source in `common/military_industrial_organization/organizations/cbrn_biomedical_organizations.txt` defines that one trait; `common/scripted_triggers/cbrn_designer_triggers.txt` maps both the respiratory-care and burn-treatment checks to it. `common/script_constants/cbrn_designer_constants.txt` sets each relevant death multiplier to 0.85, consumed by `common/scripted_effects/cbrn_exposure_effects.txt` for choking deaths and `common/scripted_effects/cbrn_designer_effects.txt` for continuing blister deaths. The separate Burn Treatment trait description in the historical account below is superseded; the localisation auditor owns the combined player-facing label. Engine behavior and final combined treatment floors remain unverified here.

The current delivery MIO permits Persistent Agent Formulation after Stable Choking Fill; they are a parent-and-descendant pair, not exclusive alternatives. The stable trait's extra dose applies only to choking artillery, while the persistent trait's contamination and duration effects apply to blister attacks, so the two legal endpoint products in the doctrine guide are separate scenarios. The older six-family account below describes a different branch layout and is superseded.

## Superseded six-family implementation account

## Purpose

The CBRN designer layer uses the current Hearts of Iron IV Military Industrial Organization database. It contains six generic families: Chemical Munitions Combine, Aerosol and Air Delivery Bureau, Protective Equipment Consortium, Mobile Decontamination Works, Biological Security Directorate, and Medical Countermeasure Directorate. Each organization affects an exact custom equipment family and explicitly mapped completed-trait checks; none grants broad bonuses to ordinary artillery, aircraft, infantry equipment, trucks, or support equipment.

MIO instances are created at game start because the current engine loads organizations only when a campaign is created. They remain hidden until an ordinary country has the matching program, technology, or special project; actual nonhuman outbreak countries are excluded. Scripted effects query completed traits directly through `any_military_industrial_organization`; no country-wide polling action is used.

## Chemical Munitions Combine

Supported equipment:

- `chemical_agent_payload`;
- `chemical_artillery_ammunition`.

The initial filling-line trait raises production learning while lowering handling reliability. Stable Choking Fill and Persistent Agent Formulation are mutually exclusive. The stable branch improves choking-agent shell conversion but lowers choking artillery dose only. The persistent branch raises blister contamination, duration, and evidence. Rapid Front Distribution shortens shell-profile changes while trading away reliability. Standardized Fuzes improve shell reliability but increase artillery evidence. The high-output capstone raises production at a further reliability cost and requires operational Chemical Readiness.

## Aerosol and Air Delivery Bureau

Supported equipment:

- `choking_chemical_air_payload`;
- `blister_chemical_air_payload`;
- `nerve_chemical_air_payload`;
- `incapacitating_chemical_air_payload`.

Lightweight Payload Assemblies and Sealed Bomb-Bay Interfaces are mutually exclusive. Lightweight Payload Assemblies unlocks exact agent-specific aircraft rack variants with 25 percent lower rack weight, 25 percent lower rack agility burden, and 20 percent lower native payload value. Sealed Bomb-Bay Interfaces instead improves prepared-payload reliability and lowers friendly-exposure risk. Controlled Dispersal narrows partial and catastrophic dose bands while extending profile-change time. Its final choice is Long-Range Payload or Precision Release.

Long-Range Payload unlocks exact agent-specific rack variants with 20 percent aircraft range and 25 percent more agility burden than the corresponding standard or lightweight rack. A country that completed both Lightweight and Long-Range directions receives a third combined variant for each available agent. Precision Release instead lowers civilian exposure and area contamination through the shared chemical-air action record.

The MIO does not target CAS or tactical-bomber airframe archetypes. Current MIO equipment filters cannot require a particular aircraft module, so applying native weight, agility, or range bonuses to those airframes would benefit conventional designs without a chemical rack. The implementation uses hidden, grant-only technologies instead. Trait completion and exact agent access must both be true before one matching module is enabled; later agent research or special-project completion resynchronizes only that agent. No broad airframe modifier, payload-line proxy, strategic-dose proxy, friendly-risk proxy, neutral multiplier, or estimator remains.

The variant modules remain limited to the verified CAS and tactical-bomber surface. They do not authorize strategic bombers. Their native stats change only aircraft designs that install the exact rack, and neither base nor variant racks can release toxic payload during ordinary missions. The active selected-state chemical-air raid adapter requires the exact agent module ID, reserves the matching payload, and passes the selected state into the shared exposure pipeline. Continuous-air activity and any route that cannot prove every accepted condition input remain fail closed.

## Protective Equipment Consortium

Supported equipment:

- `gas_mask_equipment`.

The initial trait lowers mask production cost. Durable Filter Canisters raises reliability and reduces filter losses, while the mutually exclusive Mass Civilian Pattern makes population-scaled civilian distribution more efficient at the expense of military protection. Protective Clothing Sets is limited to advanced and sealed mask models and improves blister protection through the shared protection resolver. Low-Resistance Facepiece lowers the penalties of the active Theater Protective Posture. Sealed Assault Ensemble requires Sealed Assault Protection, is limited to the sealed model, and improves nerve and vehicle protection.

## Mobile Decontamination Works

Supported equipment:

- `decontamination_equipment`.

Truck-Mounted Wash Systems lowers equipment cost, preparation time, and supported decontamination-equipment consumption. Low-Water Process improves exact cleanup in arid or low-infrastructure states; Vehicle Recovery Teams instead lowers vehicle attrition from controlled chemical contamination. Rapid Route Clearance improves theater decontamination assignments.

Hardened Mobile Plant is omitted from the active trait tree. Its accepted direction requires reducing exact decontamination-equipment losses caused by verified strategic bombing and facility capture, but Hearts of Iron IV 1.19.2 exposes no transaction carrying the lost equipment model, loss amount, producer, and production-line context. The user authorized unsupported features to be skipped. No reliability substitute, stockpile estimator, arbitrary national deduction, `days_since_last_strategic_bombing` proxy, or unrelated capture modifier remains.

## Biological Security Directorate

Supported equipment:

- `anthrax_bomb_equipment`;
- `plague_bomb_equipment`;
- `tularemia_bomb_equipment`;
- `smallpox_bomb_equipment`.

Sealed Sample Chain improves biological stockpile safety and lowers exact captured-facility release risk. Distributed Surveillance improves ordinary outbreak detection, while Mobile Containment Team reduces onward spread from an exact captured-facility release. Stable Weaponization gives every ordinary agent the same covert-operation reliability gain and only changes the attacker-accident branch after a failed strategic raid; it does not change native raid success factors. Accelerated Cultivation raises payload output and accident risk. Strategic Dissemination raises the physical potency, evidence, and Condemnation of every ordinary agent equally. Fail-Safe Facilities can prevent an otherwise eligible ordinary stockpile accident but cannot prevent sabotage, bombing, captured-facility releases, or doomsday use.

The directorate preserves the accepted weapon hierarchy `Tularemia < Anthrax < Plague < Smallpox`. Only Smallpox is the severe ordinary weapon tier. Native strategic and battlefield raid probabilities remain the same for all four agents; agent identity changes consequences after release, not delivery success.

## Medical Countermeasure Directorate

Supported equipment:

- `cbrn_instrument_equipment`.

The historical six-family plan named Respiratory Care and Burn Treatment separately. The accepted twelve-node biomedical tree combines their choking and continuing-blister treatment effects in Respiratory and Burn Care; Antidote Production remains a separate nerve-agent treatment. The remaining Vaccine Scale, Mobile Casualty Sorting, and International Medical Mission descriptions in this historical plan do not define the current node layout or implementation status. Treatment does not erase deaths already recorded, evidence, attribution, contamination history, or use history.

## Consequence boundary

Designer traits are read by the exact protection, exposure, decontamination, biological lifecycle, stockpile-safety, and sanctions-compliance paths mapped above. They may change only supported inputs or outputs, never doctrine's Condemnation multiplier, and never reduce evidence. Persistent Agent Formulation, Standardized Fuzes, Stable Weaponization, and Strategic Dissemination increase evidence; confirmed strategic and mass-casualty Condemnation floors remain downstream and intact. No designer trait changes attribution thresholds, confirmed-use history, deaths ledgers, medical-saturation history, or treaty-response memory.

## AI identity

MIO-level weights follow the accepted country matrix and route profiles. France and the Soviet Union prefer the munitions family; Germany and Italy also value it. The United States strongly prefers the air-delivery family, while Britain and Germany value it after access. Britain, France, and the United States value protective production; exposed and battlefield profiles value decontamination. Japan strongly values the biological directorate, while the United States, Britain, and the Soviet Union value it after agent access. Defensive profiles and outbreak controllers prefer the medical directorate. Defensive profiles favor stable, sealed, surveillance, containment, treatment, and precision branches; battlefield and unrestricted profiles favor persistent, rapid, high-output, cultivation, and strategic-dissemination branches. AI receives no free traits, equipment, readiness, policy, or raid success.

## Source map

| Surface | File |
| --- | --- |
| Chemical and air-delivery MIO definitions | `common/military_industrial_organization/organizations/cbrn_organizations.txt` |
| Protection, decontamination, biological, and medical MIO definitions | `common/military_industrial_organization/organizations/cbrn_protection_biological_organizations.txt` |
| Scripted trait effects | `common/script_constants/cbrn_designer_constants.txt` |
| Completed-trait queries | `common/scripted_triggers/cbrn_designer_triggers.txt` |
| Exact module-unlock effects | `common/scripted_effects/cbrn_designer_effects.txt` |
| Protection and issue effects | `common/scripted_effects/cbrn_protection_effects.txt` |
| Decontamination and vehicle recovery | `common/scripted_effects/cbrn_decontamination_effects.txt`, `common/scripted_effects/cbrn_designer_effects.txt` |
| Biological lifecycle, safety, and facility capture | `common/scripted_effects/biological_lifecycle_effects.txt`, `common/scripted_effects/biological_stockpile_safety_effects.txt`, `common/scripted_effects/biological_facility_capture_effects.txt` |
| Exact state-control refresh | `common/on_actions/cbrn_designer_on_actions.txt` |
| Sanctions-compliance medical contribution | `common/scripted_effects/condemnation_sanctions_effects.txt` |
| Hidden exact-agent module gates | `common/technologies/cbrn_aerosol_module_variant_technologies.txt` |
| Base chemical racks | `common/units/equipment/modules/chemical_air_bomb_modules.txt` |
| Designer rack variants | `common/units/equipment/modules/chemical_air_bomb_variant_modules.txt` |
| Shell conversion and profile timing | `common/scripted_effects/cbrn_payload_effects.txt` |
| Air outcome bands | `common/scripted_effects/cbrn_chemical_raid_effects.txt` |
| Exposure, evidence, contamination, and friendly risk | `common/scripted_effects/cbrn_exposure_effects.txt` |
| Sprite registration | `interface/cbrn_designers.gfx` |
| Player text | `localisation/english/cbrn_designers_l_english.yml` |

## Assets

Required runtime sprites:

- `GFX_cbrn_chemical_munitions_combine` at `gfx/interface/ideas/cbrn_designers/cbrn_chemical_munitions_combine.dds`;
- `GFX_cbrn_aerosol_air_delivery_bureau` at `gfx/interface/ideas/cbrn_designers/cbrn_aerosol_air_delivery_bureau.dds`;
- `GFX_cbrn_protective_equipment_consortium` at `gfx/interface/ideas/cbrn_designers/cbrn_protective_equipment_consortium.dds`;
- `GFX_cbrn_mobile_decontamination_works` at `gfx/interface/ideas/cbrn_designers/cbrn_mobile_decontamination_works.dds`;
- `GFX_cbrn_biological_security_directorate` at `gfx/interface/ideas/cbrn_designers/cbrn_biological_security_directorate.dds`;
- `GFX_cbrn_medical_countermeasure_directorate` at `gfx/interface/ideas/cbrn_designers/cbrn_medical_countermeasure_directorate.dds`.

The chemical and air-delivery package is under `docs/assets/chaos_warfare_system/stage_6_chemical_designers/`. The four later families are under `docs/assets/chaos_warfare_system/stage_6_cbrn_designers/`. Both contain independent source PNGs, processed 64x64 PNGs, archive and runtime DDS files, checkerboard contact sheets, prompt records, manifests, validation records, and GFX handoffs. Trait nodes reuse exact vanilla MIO symbols for reliability, production, range, treatment, and release-control stats; no placeholder or resized cross-type substitute is used.

Both runtime files are one-level, uncompressed 64x64 BGRA DDS textures with real transparency and exact 16,512-byte payloads. Archive and runtime copies are byte-identical. The Chemical Munitions Combine hash is `504a34fbb2f5359deb4f066fb4b6b5ba640815290d4ea4b7bde36ab86dae4edf`; the Aerosol and Air Delivery Bureau hash is `9653875f1eef0ff6010c0ff078aa94e01afed7d01a1a518831f9886cb1db4732`.

## Open validation and engine limit

- Verify all six organizations' visibility, equipment-line assignment, trait dependencies, mutual exclusions, native modifiers, and differentiated AI selection in the package scenarios.
- Reintroduce Hardened Mobile Plant only if a future exact engine transaction can prove the affected equipment and loss. No fallback is authorized.
- Add sourced country-specific names only where a verified existing institution or firm is appropriate; generic national names remain correct elsewhere.
- The independent 27-icon exact rack-variant asset package is complete: every source, processed PNG, archive DDS, runtime DDS, and `GFX_EMI_*` registration is present. Package-scenario validation remains.
- Active selected-state raid types are wired through exact condition and module-specific route gates. Continuous-air activity and any route without a verified condition receipt remain incapable of toxic release.
