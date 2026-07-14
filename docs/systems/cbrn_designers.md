# CBRN Military Industrial Organizations

## Purpose

The CBRN designer layer uses the current Hearts of Iron IV Military Industrial Organization database. The first implemented families are the Chemical Munitions Combine and the Aerosol and Air Delivery Bureau. They affect exact custom chemical equipment archetypes and completed-trait checks; they do not grant broad bonuses to ordinary artillery, CAS, tactical bombers, or support equipment.

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

The variant modules remain limited to the verified CAS and tactical-bomber surface. They do not authorize strategic bombers. Their native stats change only aircraft designs that install the exact rack, and neither base nor variant racks can release toxic payload during ordinary missions. A future active raid adapter must require the exact module ID, reserve the matching payload, and pass the selected state into the shared exposure pipeline. Until the route can also prove every accepted condition input, release remains fail closed.

## Consequence boundary

Designer traits are read before the shared action calculator finalizes its outputs. They may change the exact supported route inputs named above, but they never modify doctrine's Condemnation multiplier and never reduce evidence. Persistent Agent Formulation and Standardized Fuzes increase evidence; confirmed strategic and mass-casualty Condemnation floors remain downstream and intact. No designer trait changes attribution thresholds, confirmed-use history, deaths ledgers, medical-saturation history, or treaty-response memory.

## AI identity

MIO-level weights follow the accepted country matrix. France and the Soviet Union prefer the munitions family; Germany and Italy also value it. The United States strongly prefers the air-delivery family, Britain and Germany value it after access, and defensive profiles prefer stable, sealed, and precision branches. Battlefield and unrestricted profiles prefer persistent, rapid, high-output, and long-range branches. AI receives no free traits, equipment, readiness, or policy.

## Source map

| Surface | File |
| --- | --- |
| MIO definitions and native bonuses | `common/military_industrial_organization/organizations/cbrn_organizations.txt` |
| Scripted trait effects | `common/script_constants/cbrn_designer_constants.txt` |
| Completed-trait queries | `common/scripted_triggers/cbrn_designer_triggers.txt` |
| Exact module-unlock effects | `common/scripted_effects/cbrn_designer_effects.txt` |
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
- `GFX_cbrn_aerosol_air_delivery_bureau` at `gfx/interface/ideas/cbrn_designers/cbrn_aerosol_air_delivery_bureau.dds`.

The completed production package is under `docs/assets/chaos_warfare_system/stage_6_chemical_designers/` and contains independent source PNGs, processed 64x64 PNGs, archive and runtime DDS files, a checkerboard contact sheet, prompt records, manifest, validation record, and GFX handoff. Trait nodes reuse exact vanilla MIO symbols for reliability, production, range, and release-control stats; no placeholder icon is used.

Both runtime files are one-level, uncompressed 64x64 BGRA DDS textures with real transparency and exact 16,512-byte payloads. Archive and runtime copies are byte-identical. The Chemical Munitions Combine hash is `504a34fbb2f5359deb4f066fb4b6b5ba640815290d4ea4b7bde36ab86dae4edf`; the Aerosol and Air Delivery Bureau hash is `9653875f1eef0ff6010c0ff078aa94e01afed7d01a1a518831f9886cb1db4732`.

## Future work and open validation

- Add the Protective Equipment Consortium, Mobile Decontamination Works, Biological Security Directorate, and Medical Countermeasure Directorate in their mapped implementation stages.
- Add sourced country-specific names only where a verified existing institution or firm is appropriate; generic national names remain correct elsewhere.
- Verify organization visibility, equipment-line assignment, trait dependencies, mutual exclusions, native modifiers, and differentiated AI selection in a new campaign.
- Finish and validate the independent 27-icon exact rack-variant asset package, then register every `GFX_EMI_*` identifier.
- Wire active selected-state raid types only after exact condition and module-specific route gates are proven. Variant aircraft remain incapable of toxic release until that gate is complete.
