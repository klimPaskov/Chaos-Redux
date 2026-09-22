# CBRN unit consolidation and AI-template integration handoff

Status: implemented in the shared working tree, pending parent integration and the required post-change audits.

Acceptance basis: the user's 2026-09-20 CBRN request, recorded in `docs/specs/chaos_warfare_system_specs/specs/13_2026_09_20_accepted_cbrn_overhaul.md`, with requirements CBRN-05, CBRN-06, and CBRN-08 tracked in `docs/plans/chaos_warfare_system_plans/2026-09-20_cbrn_overhaul_requirement_ledger.md`.

## Source surfaces

The shared unit result preserves three active headquarters sections: `cbrn_hq_operations_section`, `cbrn_hq_protective_logistics_section`, and `cbrn_hq_medical_countermeasure_directorate`.

The regimental roster retains the six distinct field roles represented by the existing stable IDs: `cbrn_gas_mask_decon_detachment` (the Protection Company), `cbrn_medical_countermeasure_detachment` (the Field Medical Company), `cbrn_chemical_recon_detachment`, `cbrn_chemical_projector_battery`, `cbrn_chemical_ammunition_train`, and `cbrn_biosecurity_assault_detachment`, together with `chaos_battalion` and the three light, medium, and heavy armored-delivery variants.

The visible company names remain in `localisation/english/chaosx_units_l_english.yml`: `cbrn_gas_mask_decon_detachment` is `CBRN Protection Company` and `cbrn_medical_countermeasure_detachment` is `CBRN Field Medical Company`.

Nerve suppression is an operation-only certification and has no standing `cbrn_nerve_suppression_detachment` enablement in units, technology, CXT, or AI templates.

The eighteen agent-specific chemical tank definitions remain inactive compatibility IDs in `common/units/chemical_tank_support.txt`; a source scan found no retired IDs in normal technologies, AI templates, CXT grants, or CXT decisions.

The unit-scope source surfaces reviewed or updated in the shared result are:

- `common/units/cbrn_hq_support.txt`
- `common/unit_leader/cbrn_hq_traits.txt`
- `common/units/cbrn_regimental_support.txt`
- `common/units/chemical_tank_support.txt`
- `common/technologies/cbrn_hq_technologies.txt`
- `common/technologies/cbrn_regimental_support_technologies.txt`
- `common/ai_templates/cbrn_hq_support.txt`
- `common/ai_templates/cbrn_regimental_support.txt`
- `common/scripted_triggers/cbrn_regimental_support_triggers.txt`
- `common/scripted_triggers/cbrn_scripted_triggers.md`
- `common/scripted_effects/chaosx_test_country_effects.txt`
- `common/scripted_effects/chaosx_test_country_stockpile_effects.txt`
- `docs/systems/cbrn_warfare/cbrn_unit_consolidation.md`

No change to `common/units/equipment/cbrn_payload_equipment.txt` was required because the consolidated units consume the existing payload and support equipment models.

## Technology and CXT behavior

`hazard_pioneer_formation` is grant-only with `allow = { always = no }`, no visible folder position, and no positive research AI factor; the doctrine/project grant still supplies its Protection Company upgrade and specialization effects.

`field_epidemiology_teams` uses the normal 0.75 relative research-cost band, and `mobile_cbrn_hospitals` remains in the advanced 1.0 band.

The CXT setup no longer writes a synthetic `chemical_readiness = 100` value. `cbrn_refresh_country_mask_snapshot = yes` runs after the real registered-equipment and stockpile grants in `chaosx_test_country_initial_setup` and the refill path, deriving readiness from actual mask stock and the deployed issue ledger.

## AI gating

The former impossible `cbrn_country_has_verified_chemical_force_target = { always = no }` gate is replaced by a country-scope programme-or-war and real strategic-agent-stock gate in `common/scripted_triggers/cbrn_regimental_support_triggers.txt`.

Chemical artillery and armored-delivery callers still require current policy, an active operation plan, and their complete standing equipment bill; the bill thresholds serve as the standing quota for adoption. Native operations retain exact selected-target validation before payload release because the country-scope template surface cannot see an Army-HQ-to-target-state pointer.

Armored delivery has separate light, medium, and heavy template variants with matching generic and flame-chassis thresholds. A medium bill cannot be satisfied by light or heavy chassis stock.

`common/ai_templates/cbrn_hq_support.txt` now describes five context-specific variants built from the three consolidated HQ sections, correcting the stale five-role header.

The equal-IC and exposure analysis is documented in `docs/systems/cbrn_warfare/cbrn_unit_consolidation.md`. It uses the installed 1939 infantry-equipment model at 0.58 IC, compares clean, unprotected, protected, and shortage conditions, and states that protection is country-wide rather than a division-specific hazard advantage.

The unit audit confirms `cbrn_chemical_projector_battery` has base soft attack 12, hard attack 4, defense 4, and breakthrough 10, `chaos_battalion` has base breakthrough 18 and organization 40, and `cbrn_chemical_recon_detachment` has base recon 4. Technology corrections belong to the technology owner: Livens values use percentage fractions 0.05/0.15/0.075/0.075 per technology, the Chaos Battalion 1942 breakthrough value is 0.15, its flat organization increase is 11 (+27.5%), and hidden weather recon grants use 0.2/0.4/0.6. With the parent's global-organization tuning, the strict effective organization stack is approximately +33%, below the +35% cap. The legal source sums are projector 35/35/35/30% for soft/hard/defense/breakthrough, Battalion 30% breakthrough, and Recon +30% utility. The corrected values are reflected in the equal-cost documentation without editing the technology owner's file.

An exposure-hook audit found no supported division/template/unit-modifier consumer for Protection Company-specific hazard reduction. `cbrn_protection_effects.txt` resolves the military casualty and disruption multipliers from countrywide mask coverage and response layers, and `cbrn_exposure_effects.txt` consumes those values for the exact target state. A per-division hazard bonus would therefore be an unapproved mechanic; the handoff claims only native unit statistics and national coverage.

## Evidence and validation

The required probability baseline was inspected before the gate edit with `hoi4.probability_inspect`, adapter `custom_weighted_pool`, source revision `5b1228abaf1a54c9bb91c17aafa496c2310f3bd84e8c26967919b339e0388ac`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d19363e2d0970317d1ce4a2e27dea04272af9f77b864b61cd384fc4e729b0e61/df0ef56ba5c0581e5ee1bba54e30ed5edb53e08a661d24b1e5b1fc50357f2d2f/probability-inspect-57c54669a21e.json`.

The post-edit probability inspection returned `PROBABILITY_SOURCE_INSPECTED` at source revision `77bb9a6747b5184fedfa385498b3804f06aa3ef9c1fffacf9b44b52e044fb076` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c6dea2b68bf9982e60a2c57db3825b2c9f8e068043231bfc31b5ff4f77a5df72/1d17ea841671bbb4b4e49609b6ef7409f10271d5000d269c5a8fdf3f520a5aac/probability-inspect-38cd23fe2f8f.json`.

Both inspections reported `candidates=0`, `poolComplete=false`, and no available adapters, so no adoption ranking or same-scenario probability compare is available for this custom AI-template surface. The parent must route `chaosx_ai_probability_auditor` with the named scenarios `CBRN_DOC_PEACE_DEFENDED_MAJOR`, `CBRN_DOC_LOW_CAPACITY_MINOR`, `CBRN_DOC_THREATENED_DEFENDER`, `CBRN_DOC_AUTHORIZED_OFFENSIVE_RESERVES`, `CBRN_DOC_OUT_OF_STOCK_ATTACKER`, `CBRN_DOC_HIGH_CONDEMNATION_AGGRESSOR`, and `CBRN_DOC_HUMAN_AI_PARITY`, and must report the adapter gap rather than presenting source inspection as a probability result.

Pre-edit technology inspection had succeeded for `theater_cbrn_headquarters` and `armored_agent_delivery` at source revision `95444b...` with the recorded technology-unlock artifacts in the parent audit trail. Post-edit targeted technology inspection returned `INTERNAL_ERROR`, and subsequent render attempts returned `Transport closed`; a standalone Technology Tree Viewer was not exposed. Technology render/compare therefore remains blocked and is not claimed here.

Local source checks found balanced braces in every touched unit, technology, AI, trigger, and CXT file, no remaining direct synthetic readiness assignment in CXT setup files, and no retired agent-tank IDs in normal technology, AI, or CXT surfaces. The game was not launched and no logs were requested or used.

## Coordination and remaining risks

After coordination with `core_integration`, the HQ offensive-preparation cleanup is complete: `cbrn_prepare_chemical_offensive` and `cbrn_combined_overmatch` were removed from `common/units/cbrn_hq_support.txt`, while `cbrn_seal_operational_area` and all three active HQ IDs remain. The dedicated status traits `cbrn_hq_active_chemical_offensive` and `cbrn_hq_active_combined_overmatch`, plus their unused local constants, were removed from `common/unit_leader/cbrn_hq_traits.txt`, eliminating the separate paid offensive-preparation path.

The exact armored chassis IDs and variant equipment consumers remain coordinated with `raid_integration`; this handoff records only the light, medium, and heavy threshold separation.

Large and on-map consolidated unit icons are wired through the existing CBRN sprite registrations. The small text-icon registrations still reuse inherited chemical-tank aliases, so a bespoke icon pass remains an asset risk and is not claimed complete here.

The removed offensive ability IDs still have inherited unused sprite registrations in `interface/chaosx_ability.gfx`; no gameplay file references them after the HQ cleanup. Removing or retaining those compatibility assets should be decided by the icon owner rather than mixed into the unit patch.

The older `docs/systems/cbrn_warfare/chemical_warfare/cbrn_regimental_support.md` still contains legacy wording for several absorbed role IDs and should be reconciled by the documentation owner. This handoff records the current source result without broadening the unit patch into unrelated historical documentation.

No commit was created. Parent review, the probability-auditor same-scenario attempt, and the blocked technology MCP render/compare remain required before a package-level completion claim.
