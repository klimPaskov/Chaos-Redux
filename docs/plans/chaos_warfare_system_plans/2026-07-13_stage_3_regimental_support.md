# Stage 3: CBRN regimental support and Chaos Assault Battalion

Date: 2026-07-13

## Authority and tranche boundary

This tranche implements Stage 3 of `handoffs/staged_implementation_plan.md` against numbered specs 03 and 04, `matrices/regimental_support_matrix.md`, and `matrices/subunit_equipment_matrix.md`. It defines the division-layer units, their equipment-backed statistics, doctrine-only unlock technologies, baseline AI templates, legacy compatibility, localisation, icons, and documentation.

Stage 3 does not dispatch chemical or biological exposure. Offensive companies are standing delivery organizations; Stage 6 reserves and consumes the selected payload and calls the shared exposure pipeline, Stage 7 supplies biological operations, and Stage 9 supplies the targeted nerve-suppression decision. Until those adapters exist, the new units provide only their explicitly listed native statistics.

The accepted doctrine rule remains unchanged: doctrine may reduce Condemnation impact, but does not reduce evidence, attribution, deaths, contamination, or confirmed-use history. Numbered spec 08 also keeps doctrine separate from camp and genocide infrastructure.

## Stable identifiers

| Player-facing role | Stable subunit identifier | Unlock owner |
| --- | --- | --- |
| Gas Mask and Decontamination Detachment | `cbrn_gas_mask_decon_detachment` | `field_decontamination_kits` |
| Chemical Reconnaissance Detachment | `cbrn_chemical_recon_detachment` | `chemical_detection_paper` |
| Hazard Pioneer Detachment | `cbrn_hazard_pioneer_detachment` | `hazard_pioneer_formation` |
| Chemical Projector Battery | `cbrn_chemical_projector_battery` | `livens_projector_tech` |
| Chemical Ammunition Train | `cbrn_chemical_ammunition_train` | `chemical_artillery_shells` |
| Light Armored Chemical Delivery Detachment | `cbrn_light_armored_delivery_detachment` | `armored_agent_delivery` |
| Medium Armored Chemical Delivery Detachment | `cbrn_medium_armored_delivery_detachment` | `armored_agent_delivery` |
| Heavy Armored Chemical Delivery Detachment | `cbrn_heavy_armored_delivery_detachment` | `armored_agent_delivery` |
| Nerve Agent Suppression Detachment | `cbrn_nerve_suppression_detachment` | `nerve_agent_suppression_formation` |
| Field Epidemiology and Quarantine Detachment | `cbrn_field_epidemiology_detachment` | `field_epidemiology_teams` |
| Medical Countermeasure Detachment | `cbrn_medical_countermeasure_detachment` | `mobile_cbrn_hospitals` |
| Biological Security Assault Detachment | `cbrn_biosecurity_assault_detachment` | `biological_security_assault_formation` |
| Chaos Assault Battalion | retained public ID `chaos_battalion` | retained hidden ID `chaos_battalion_tech` |

The three armored definitions are chassis variants of one role, not agent variants. They share the same offensive-delivery exclusivity key, selected payload profile, scripted operation path, and player-facing family. This preserves designer-produced light, medium, and heavy flame-role chassis while eliminating the old agent-by-agent support-company explosion.

## Native equipment and shortage contract

All regimental support uses the current 1.19 structure: `group = support`, `allowed_battalion_groups`, `category_regimental_support_battalions`, and `divisional = no`. Every role declares `essential` archetypes and a `need` table. The engine therefore scales native statistics and reinforcement with actual equipment shortages.

The fully equipped first-pass targets stay inside the accepted matrix bands:

| Role | Manpower | Organization | Strength | Supply | Standing essential equipment |
| --- | ---: | ---: | ---: | ---: | --- |
| Mask and decon | 320 | 8 | 0.30 | 0.05 | masks, decon, support equipment |
| Reconnaissance | 220 | 8 | 0.25 | 0.06 | masks, instruments, support equipment, trucks |
| Hazard pioneer | 400 | 8 | 0.40 | 0.08 | masks, decon, instruments, support equipment, trucks |
| Projector | 320 | 3 | 0.30 | 0.10 | masks, decon, instruments, projector chassis, support equipment |
| Ammunition train | 400 | 3 | 0.40 | 0.14 | masks, decon, instruments, support equipment, trucks |
| Armored delivery | 320 | 8 | 0.55 | 0.10 plus chassis fuel | masks, decon, instruments, support equipment, eligible flame-role chassis |
| Nerve suppression | 400 | 3 | 0.40 | 0.12 | masks, decon, instruments, support equipment, trucks |
| Epidemiology | 340 | 8 | 0.30 | 0.08 | masks, instruments, support equipment, trucks |
| Medical countermeasure | 360 | 8 | 0.40 | 0.08 | masks, support equipment, trucks; scripted medical capacity is checked by operations |
| Biosecurity assault | 420 | 8 | 0.50 | 0.12 | masks, decon, instruments, support equipment, trucks |
| Chaos Assault Battalion | 1,050 | 28 | normalized infantry-scale strength | 0.32 | infantry equipment, support equipment, masks, decon, instruments, trucks |

One offensive chemical delivery company is enforced with a shared `same_support_type`. Armored delivery also shares vanilla's `flame` support type and cannot parachute. Medical Countermeasure and Biological Security Assault share the vanilla `field_hospital` support type to prevent duplicate medical-role stacking. Chaos Assault Battalion remains a special-forces line unit and has no chemical or biological payload requirement.

## Payload and operation eligibility

Numbered spec 04 has priority over the matrix wording where the engine cannot express a selected payload family in a single `need` block. A subunit `need` table cannot express “one of choking, blister, nerve, or incapacitant payload,” and current documentation exposes no per-division trigger for the fulfillment ratio of one named essential archetype.

Accordingly:

- standing masks, decon, instruments, support equipment, vehicles, and projector/chassis needs use native reinforcement and shortage scaling;
- the selected class or agent remains country/order operation state, so changing agent never requires rebuilding a template;
- Stage 6 checks, reserves, consumes, and debits the exact selected payload before any chemical effect;
- no new offensive role can cause chemical effects without that successful debit;
- the accepted 0/25/55/80/100 scripted-effect bands are applied by operation adapters where exact country/order stock and preparation are script-readable;
- no per-division equipment-ratio estimator is introduced.

This is an engine boundary, not a fallback: the standing unit and operational munition are deliberately separate logistics layers as specified by numbered spec 04.

## Technology contract

Researchable support unlocks attach to their existing equipment or specialist branches. Doctrine-only technologies remain impossible to research directly and are granted by the doctrine milestones in Stage 5 after all prerequisites are met:

- `hazard_pioneer_formation`
- `chaos_battalion_tech`
- `chaos_battalion_1942` (Improved Chaos Assault Equipment; retained legacy ID)
- `chemical_artillery_shells`
- `persistent_agent_shell_filling`
- `armored_agent_delivery`
- `sealed_tank_crews`
- `nerve_agent_suppression_formation`
- `biological_security_assault_formation`

The old `chaos_battalion_1939` identifier remains a hidden no-bonus compatibility alias. It is not a researchable progression step.

`persistent_agent_shell_filling` and `sealed_tank_crews` are exact operation gates, not generic unit-stat proxies. The chemical-artillery adapter owns persistence control and the armored-delivery adapter owns friendly crew-exposure reduction plus the sealed-operation equipment burden. Improved Chaos Assault Equipment is limited to the matrix-mapped organization and breakthrough improvement; its better-protection effect is resolved by the shared exposure layer when that route is wired.

## Legacy migration

- All old Livens and chemical-tank subunit IDs remain defined and inactive so templates that reference them still parse.
- Every retained Livens definition shares `cbrn_offensive_delivery`. Every retained chemical-tank definition shares both `cbrn_offensive_delivery` and vanilla's `flame` key, and all retained chemical tanks have `can_be_parachuted = no`. Existing templates therefore cannot bypass the consolidated one-offensive-role, flame-role, or airborne restrictions.
- Agent technologies stop unlocking legacy subunits. New starts and AI templates use only the consolidated family.
- Stage 6 migrates the old units' delivery checks to the shared exposure adapter before their compatibility definitions can be retired.
- There is no documented effect that safely removes or replaces one named subunit inside every arbitrary player template. Destructive whole-template replacement is forbidden. Existing arbitrary templates therefore retain their resolvable hidden compatibility IDs; no undisclosed template rewrite is attempted.
- The public `chaos_battalion` ID is retained and its definition is replaced in place, so templates receive the coherent Chaos Assault Battalion without identifier churn.

## AI template contract

Dedicated role tokens avoid overriding vanilla or country-specific role-level templates:

- `cbrn_protected_infantry`
- `cbrn_chemical_assault`
- `cbrn_armored_assault`
- `cbrn_containment`

Target templates are enabled only when their unlock technologies and real standing equipment gates are met. Offensive templates also require battlefield-use policy, an actual chemical payload stock signal, an active Army-HQ operation plan, and an exact target receipt. Until the Stage 6 adapter exposes that receipt through a supported country-scope surface, offensive artillery and armored template adoption is fail-closed; a generic enemy-country check is not accepted as a substitute. Role ratios are bounded and self-disabling when prerequisites disappear. Mask, decontamination, and instrument equipment each have a registered `script_enum_equipment_category`, so their production-factor strategies target the intended family rather than the broad support pool. Stage 10 replaces the baseline weights with the full route-aware country profiles; Stage 3 proves that the AI can build valid templates and does not request unavailable units.

## Asset contract

Each stable subunit sprite receives two separately composed two-frame sheets:

- large division counter: `152x42` DDS, two purposeful `76x42` frames;
- small on-map counter: `60x12` DDS, two purposeful `30x12` frames.

The small composition is not a resize of the large one. Every doctrine-only or specialist technology uses a dedicated `64x64` technology icon. Source masters, processed PNGs, runtime DDS files, manifest, contact sheet, and GFX handoff live under `docs/assets/chaos_warfare_system/stage_3_regimental_support/`. Runtime sprites are registered in `interface/chaosx_subuniticons.gfx` and `interface/chaosx_techtree.gfx` before final wiring.

## Validation scenarios

1. A division with full standing equipment receives the intended native role statistics; removing masks, decon, instruments, support equipment, or vehicles lowers strength/stat contribution through native shortages.
2. An offensive company with no selected payload cannot pass a Stage 6 operation adapter and cannot create contamination, deaths, evidence, or Condemnation.
3. Projector and armored delivery cannot coexist in one division; armored delivery is unavailable to parachute templates.
4. Medical Countermeasure, Biological Security Assault, and vanilla Field Hospital cannot stack; mask/decon and epidemiology support can coexist with any one of those medical-role choices.
5. Chaos Assault Battalion consumes the special-forces cap, functions at infantry-scale width and organization, and carries no biological bomb need.
6. AI roles stay disabled without technologies/equipment/policy, then select valid consolidated templates when all gates are satisfied.
7. Every old subunit identifier still resolves, but no current technology or AI template newly selects an agent-specific legacy support company.

## Implementation evidence and audit closure

The Stage 3 completion audit found three closure gaps. Each source defect was resolved in this tranche:

- legacy projector and chemical-tank compatibility definitions now use the consolidated exclusion keys, and the six old light chemical tanks can no longer parachute;
- the obsolete Extermination Columns document and stale on-action header now describe the bounded equipment-backed Chaos Assault Battalion and prohibit passive release;
- the asset package contains source captures, alpha-bearing masters, processed PNGs, exact runtime DDS files, readable contact sheets, a manifest, and the final GFX/path handoff.

Task-specific contract checks produced these results:

| Scenario | Recorded result |
| --- | --- |
| Designer placement | All twelve regimental definitions use `group = support`, `category_regimental_support_battalions`, and `divisional = no`; each declares both `essential` and `need`. This is the current-version engine contract for the regimental row. |
| Standing shortages | Every regimental role and the Chaos Assault Battalion has matching essential/need ownership. No scripted offensive consequence is granted by formation presence; operation-level payload bands remain explicitly owned by Stage 6. |
| Offensive and medical exclusions | Five consolidated offensive definitions, seven retained Livens definitions, and eighteen retained chemical-tank definitions share `cbrn_offensive_delivery`; all twenty-one current/legacy armored definitions share `flame`; both medical-role definitions share `field_hospital`; no retained chemical tank remains parachutable. |
| Chaos Assault Battalion | The stable unit is special forces, width 2, organization 28, manpower 1,050, equipment-backed, and has no chemical or biological payload need. Search found no active caller of its retired passive dispersal/Condemnation helpers. |
| AI construction and cessation | Four dedicated role templates use complete real-stock and technology gates. The standing bills match one target template exactly, role-ratio strategies use `abort_when_not_enabled = yes`, and offensive roles require policy plus real supported payload stock without dispatching exposure. |
| Legacy safety | All legacy IDs remain defined, current agent technologies no longer unlock them, and their compatibility constraints match the consolidated family. No arbitrary player template is destructively replaced. |
| Assets | Thirteen large 152x42 two-frame DDS sheets, thirteen separately composed small 60x12 two-frame DDS sheets, and eleven dedicated 64x64 technology DDS files have valid headers/dimensions and resolving GFX texture paths. All three contact sheets were visually reviewed. |

These checks close the source and compatibility findings. Actual rendered designer placement, live shortage-stat response, AI template selection/cessation, and comparative field behavior remain part of the final package scenario run in Stage 14; they are not claimed as runtime-verified here and cannot support final goal completion until recorded.

## Later-stage integration

- Stage 4 assigns theater-level HQ preparation and abilities.
- Stage 5 grants doctrine-only technologies and completes doctrine/officer-corps balance.
- Stage 6 supplies exact payload reservation, consumption, selected-profile exposure, cooldown, and cleanup.
- Stage 7 activates epidemiology and biosecurity scripted effects.
- Stage 9 activates targeted nerve suppression and its full consequence record.
- Stage 10 differentiates country AI ratios and route preferences.
