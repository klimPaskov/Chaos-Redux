# Source of Truth Map

The user's explicit 2026-09-20 implementation request accepts [`specs/13_2026_09_20_accepted_cbrn_overhaul.md`](../specs/13_2026_09_20_accepted_cbrn_overhaul.md) as the controlling amendment for any conflict in the older surface map below. Acceptance applies to the design, while current implementation remains tracked in [`2026-09-20_cbrn_overhaul_requirement_ledger.md`](../../../plans/chaos_warfare_system_plans/2026-09-20_cbrn_overhaul_requirement_ledger.md) pending source and MCP evidence.

| Surface | Source of truth after acceptance |
| --- | --- |
| Core gameplay and values | `specs/01_core_system_and_gameplay_loop.md` |
| Doctrine paths and technologies | `specs/02_doctrine_architecture.md` and `matrices/doctrine_and_tech_matrix.md` |
| Army HQ and regimental support | `specs/03_hq_command_and_regimental_support.md`, HQ and support matrices |
| Equipment and subunits | `specs/04_equipment_tech_and_subunits.md`, subunit matrix |
| Chemical delivery and casualty model | `specs/05_chemical_delivery_and_battlefield_effects.md`, chemical and balance matrices |
| Biological warfare | `specs/06_biological_warfare_and_outbreaks.md`, biological matrix |
| Gas masks and starting reserves | `specs/07_gas_masks_civil_defence_and_population_protection.md`, stockpile matrix |
| Suppression and occupation | `specs/08_suppression_occupation_and_nerve_agents.md` |
| Deaths, Air Cleanliness, Condemnation | `specs/09_condemnation_deaths_air_cleanliness_and_diplomacy.md` |
| AI, country profiles, designers | `specs/10_ai_country_programs_and_designers.md`, AI and country matrices |
| Balance and consistency | `specs/11_balance_tuning_and_consistency_rework.md` |
| UI, localisation, assets, achievements | `specs/12_ui_localisation_assets_achievements.md` and prompts |
| Implementation order | `handoffs/staged_implementation_plan.md` |
| Completion test | `handoffs/completion_audit_checklist.md` |

Existing repository docs are evidence of current behavior. Once this design is accepted, contradictory current documentation should be updated or marked superseded. Existing implementation is not automatic authority over the accepted rework.

## Current-state documentation authority

The current native chemical land source `common/raids/cbrn_chemical_land_raids.txt` defines 55 raid types in the single `chemical_raids` category: nine cylinder, nine projector, nine artillery, 27 armored, and one Phantom Mist. This source count supersedes older 36-type inventories but does not prove native AI probability behavior or engine payment results; the accepted two-category rule and unresolved validation remain in the [overhaul ledger](../../../plans/chaos_warfare_system_plans/2026-09-20_cbrn_overhaul_requirement_ledger.md).

Use `docs/plans/chaos_warfare_system_plans/2026-09-20_cbrn_overhaul_requirement_ledger.md` for the accepted overhaul's requirement-row status. The 2026-07-13 ledger remains a bounded historical migration record.

Use `docs/plans/chaos_warfare_system_plans/documentation_state.md` for the reconciled current-state map, unresolved plan and handoff dispositions, contradiction register, and stale-document register.

Use `docs/plans/chaos_warfare_system_plans/2026-09-20_documentation_cleanup_handoff.md` for this overhaul's documentation-curator handoff; it is not gameplay or runtime completion proof. The unqualified `documentation_cleanup_handoff.md` remains an earlier snapshot.

The later explicit user constraints recorded on 2026-07-29 supersede older optional-estimator wording: continuous chemical-air contamination remains fail-closed without a verified current-version mission hook, no estimator or other fallback is allowed, selected-state chemical raids must use the shared exposure pipeline, and idle chemical-capable aircraft never contaminate.

The later explicit doctrine clarification also supersedes broader mitigation wording: doctrine may increase physical CBRN harm and the resolved killing efficiency of an already authorized camp network and may reduce only Condemnation impact; it never erases evidence, attribution, deaths, contamination, trauma, responsibility, history, or authorization for camps.
