# Event 006 IW-009 Bavaria post-wire country-package audit

Audit date: 2026-07-24.

Scope: fresh static audit of the current working tree after the Friedrich Dollmann runtime portrait promotion and consumer-localisation reconciliation.

Mode: read-only country-package audit; this handoff is the only file changed by this subagent.

## Executive verdict

IW-009 Bavaria is package-complete for compile-time content attestation and automatic/scenario admission, subject to the parent adding the existing exact package-ID attestation entry described below.

No package-specific blocker was found in the post-wire BAY identity, map binding, host/origin contract, runtime adapter, focus ownership, decisions, ideas, AI, localisation, forces, or asset surfaces.

Promotion is authorized for the parent to add `check_variable = { independence_wave_execution_package_id = constant:independence_wave_package_id.iw_009 }` to `has_independence_wave_runtime_package_content_attestation_for_execution_id` in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`, and to update that trigger's explanatory comment to include IW-009.

This authorization is limited to the exact attestation gate; it does not claim that Event 006 as a whole is complete or that live-engine execution has been tested.

## Country package coverage checklist

| Surface | Result | Evidence and identifiers |
| --- | --- | --- |
| Tag and package identity | PASS | `is_independence_wave_bay_package` in `common/scripted_triggers/006_independence_wave_rhineland_bavaria_package_triggers.txt` requires `original_tag = BAY`, active-country scope, and `independence_wave_package_id.iw_009`; the exact setup contract is `can_initialize_independence_wave_iw_009_package`. |
| Dormant/living-country safety | PASS | `is_independence_wave_runtime_package_preflight_ready` in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` requires `exists = no`, clears active-origin/Soviet-origin paths, and maps only `iw_009` to `original_tag = BAY`; no dormant vanilla history or country file was changed. |
| Map binding | PASS | `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv` binds IW-009 to anchor state 52, compact states 52|53|54, host GER, protected host state 64, and reservation group `RG-52-53-54`; the reservation CSV marks this group as IW-009-only. |
| Vanilla state coherence | PASS | Vanilla `history/states/52-Wuttemberg.txt`, `53-Oberbayern.txt`, and `54-Bayreuth.txt` are owner/controller GER at 1936, carry BAY cores, and contain the expected Bavarian victory points/buildings; no Event 006 map rewrite is present. |
| Anchor/capital setup | PASS | `can_initialize_independence_wave_iw_009_package` and `has_prepared_independence_wave_iw_009_package_setup` require event-target anchor state 52 to be owned and controlled by BAY and `capital_scope = { state = 52 }`. |
| Former-host/origin separation | PASS | The setup contract requires an event-target former host distinct from ROOT; the runtime preflight blocks existing active/Soviet origins; the installed collision ledger has no 52/53/54 conflict row, and the host-remnant contract is GER=64. |
| Runtime adapter | PASS | IW-009 is already present in the adapter registry in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`; `006_independence_wave_execution_effects.txt` dispatches through the package adapter surface rather than a new country-specific execution path. |
| Reservation/allocator safety | PASS | `RG-52-53-54` is a single-package reservation group with a host-remnant test; package binding uses fixed current IDs and no cross-group state collision is recorded. |
| Setup lifecycle | PASS | `independence_wave_setup_iw_009_bavaria` in `common/scripted_effects/006_independence_wave_rhineland_bavaria_package_effects.txt` clears transient setup state, prepares the roster, initializes politics/AI/lifecycle/founding incident, loads p9 forces, closes German reunification, and sets `independence_wave_iw_009_setup_complete`; the paired prepared/complete triggers require those proofs. |
| Host reunification safety | PASS | Prepared setup requires `independence_wave_bay_south_german_ambition`, `independence_wave_bay_no_competing_german_claim`, and no German reunification choice/preserved claim; completion requires `independence_wave_bay_german_reunification_closed`. |
| One-time opening forces | PASS | IW-009 uses force mapping `p9`, profile `regular_defectors`, and `independence_wave_force_package_for_current_generation`/`independence_wave_force_package_applied` guards in the package setup and prepared trigger; no daily/on-action free-unit loop or bespoke history army was added. |
| Shared focus ownership | PASS with shared-tree warning | `independence_wave_assign_focus_framework` in `common/scripted_effects/006_independence_wave_focus_effects.txt` loads `independence_wave_focus_tree` only for explicit full-framework assignment; BAY is gated by the package trigger and does not overwrite a living country's meaningful tree. |
| BAY bespoke focus route | PASS | `common/national_focus/006_independence_wave_focus.txt` contains the eight package-owned focuses `independence_wave_bay_broker_civic_settlement_focus`, `...reconcile_landesbank_accounts_focus`, `...bind_rail_and_pass_authorities_focus`, `...seat_landtag_and_court_focus`, `...entrust_mountain_guardians_focus`, `...open_alpine_network_office_focus`, `...convene_south_german_settlement_focus`, and `...ratify_german_host_compact_focus`; each has BAY package gating, prerequisites/mutual exclusion, reward logic, AI weight, icon, and localisation. |
| Focus MCP inspection | WARN, not a BAY admission blocker | `hoi4_focus_inspect` found 176 focuses and 14 blocking shared-tree layout diagnostics (long connectors/intersections in common branches); no package-specific BAY ownership or prerequisite defect was identified. Artifact SHA: `dac8d6184d9475f8d2f2732c9ccdb8dd58222425c13228fff3237b65be9bb830`. |
| Decisions and mission | PASS | `independence_wave_bay_state_category` in `common/decisions/006_independence_wave_rhineland_bavaria_decisions.txt` contains the BAY state mission `independence_wave_bay_hold_the_state_together` plus the ten active-project IDs enumerated by `has_independence_wave_bay_active_package_project`: `reconcile_district_treasuries`, `organize_mountain_passes`, `settle_wittelsbach_host_ledgers`, `integrate_mountain_companies`, `ratify_constitutional_compact`, `entrust_workers_districts`, `restore_the_crown`, `establish_mountain_guardians`, `convene_south_german_estates`, and `negotiate_alpine_supply_accord`; costs, capital-control checks, one-active-project locking, cancellation/failure effects, and cleanup are present. |
| Ideas and lifecycle | PASS | `common/ideas/006_independence_wave_rhineland_bavaria_ideas.txt` supplies the BAY starting alternatives `bay_disputed_state_inheritance` and `bay_estates_and_districts_settlement` plus route/lifecycle ideas; the prepared trigger requires one starting idea and cleanup removes BAY-owned temporary ideas. |
| Politics and leaders | PASS | BAY setup installs constitutional, labor, traditional, and emergency government lanes; the traditional lane uses guarded `BAY_rupprecht_of_bavaria` when available and otherwise the institutional `BAY_independence_wave_state_council`; the emergency lane promotes `BAY_independence_wave_mountain_commandant` as the male corps commander. |
| Character ownership | PASS | The independent Dollmann audit found no `BAY_independence_wave_mountain_commandant` owner in the project, vanilla, or approved reference mods; vanilla Rupprecht is the only existing character token and is guarded by `has_independence_wave_bay_rupprecht_available` plus `GER = { NOT = { has_character = BAY_rupprecht_of_bavaria } }`, so transfer cannot duplicate active ownership. |
| Portrait provenance | PASS | Approved Dollmann trial 03 is documented in `docs/plans/006_independence_wave_plans/subagent_handoffs/006_bavaria_dollmann_trial03_independent_portrait_audit_2026_07_24.md`; the runtime DDS is `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_mountain_commandant.dds`, SHA-256 `332D8578F4BDEDE1A9FEAD234B361AA8C9FD786D5261CB45DBEA56475754DBAB`, and the consumer localisation is `BAY_independence_wave_mountain_commandant: "Friedrich Dollmann"`. |
| Protected portraits | PASS | Existing approved Rupprecht runtime hash `7F0AF64FDF4FECD49DF454D1198935BB3CE6A8F74AFC1AC82F8223704EAAAD2B`, Matthes hash `AA61CC3A12FB6670B690C7685FEB9383383CE58599C9E6D6E7C14F20FAB3BCE2`, and Held runtime hash `999857d191f7b088e11daa78fb29eadd0b514dc6da494a0102423c635e736e95` remain unchanged in the current working tree. |
| Advisor/dossier/forbidden asset scope | PASS | BAY has three office/advisor character and idea tokens (`BAY_independence_wave_district_finance_administrator`, `BAY_independence_wave_estates_constitutional_liaison`, `BAY_independence_wave_alpine_supply_inspector`) but no Event 006 advisor portrait, dossier, `_small`, or female asset/consumer; the Event 006 Rupprecht consumer overrides only the large portrait and leaves the vanilla `_small` definition untouched. |
| Flags and country presentation | PASS | BAY remains on the vanilla BAY tag/flag and no Event 006 cosmetic-tag or replacement flag is claimed; package-specific names, parties, leaders, advisors, ideas, focuses, decisions, and event text are covered by `localisation/english/006_independence_wave_rhineland_bavaria_l_english.yml`. |
| AI and playability | PASS | `common/ai_strategy/006_independence_wave_rhineland_bavaria.txt` contains the BAY profiles `independence_wave_bay_mountain_survival`, `...founding_restraint`, `...host_threat`, `...civic_state_policy`, `...restoration_court`, `...mountain_guardians`, and `...high_chaos_command`; enable conditions reference setup completion, host threat, route flags, and high-chaos state, with dynamic constants for army/production/defence priorities. |
| Technology/starting setup | PASS for unchanged scope, runtime limitation recorded | BAY retains vanilla starting army, navy, air, technology, industry, supply, manpower, laws, and production setup; Event 006 adds only guarded runtime forces and package effects. No technology-tree edit was made, and the installed package exposes no Technology Tree Viewer, so tech-tree visualization remains unresolved. |
| Event/report integration | PASS | `events/006_independence_wave_rhineland_bavaria.txt` contains BAY founding, route, estates, and host-compact incidents with package triggers, one-shot resolution flags, and report picture `GFX_report_event_006_bay_state_incidents`; localisation and report assets are present in the BAY package surfaces. |
| Cleanup | PASS | BAY cleanup in `common/scripted_effects/006_independence_wave_rhineland_bavaria_package_effects.txt` removes package decisions/missions/ideas/variables/flags and restores protected Rupprecht portrait state; no persistent Event 006 advisor/portrait residue is intentionally left behind. |

## File-surface checklist

The audited package surfaces are `common/scripted_triggers/006_independence_wave_rhineland_bavaria_package_triggers.txt`, `common/scripted_effects/006_independence_wave_rhineland_bavaria_package_effects.txt`, `common/scripted_effects/006_independence_wave_force_effects.txt`, `common/script_constants/006_independence_wave_force_package_constants.txt`, `common/scripted_effects/006_independence_wave_focus_effects.txt`, `common/national_focus/006_independence_wave_focus.txt`, `common/decisions/006_independence_wave_rhineland_bavaria_decisions.txt`, `common/decisions/categories/006_independence_wave_rhineland_bavaria_categories.txt`, `common/ideas/006_independence_wave_rhineland_bavaria_ideas.txt`, `common/ai_strategy/006_independence_wave_rhineland_bavaria.txt`, `common/characters/006_independence_wave_nwe_advisors.txt`, `events/006_independence_wave.txt`, `events/006_independence_wave_rhineland_bavaria.txt`, `interface/006_independence_wave_region_01_portraits.gfx`, `interface/006_independence_wave_rhineland_bavaria_assets.gfx`, `localisation/english/006_independence_wave_rhineland_bavaria_l_english.yml`, and the runtime portrait directory `gfx/leaders/006_independence_wave/`.

The audited package-binding surfaces are `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv`, `006_current_map_reservation_groups.csv`, and `006_current_map_state_collisions.csv`.

## Current content-attestation and admission state

`has_independence_wave_runtime_package_adapter_for_execution_id` already admits the IW-009 adapter, and the normal preflight already maps exact `iw_009` to `BAY`.

`is_independence_wave_scenario_package_preflight_ready` already has the IW-009 exact-tag branch, so no new scenario branch is required.

Only `has_independence_wave_runtime_package_content_attestation_for_execution_id` is missing IW-009; its current exact attested set is IW-001, IW-004, IW-007, IW-008, IW-017, and IW-019.

After adding the one exact IW-009 check, normal release preflight will require the already-present adapter, content attestation, origin safety, exact package/tag mapping, host/anchor reservation, and `exists = no` target proof.

After the same attestation addition, SCN-008's scenario candidate path can admit IW-009 through its existing exact-tag branch when the current-map binding, host-remnant, reservation, and scenario availability checks pass.

Content capacity increases from six admitted packages to seven; a seven-package automatic/scenario band becomes capacity-possible, but it remains subject to dynamic reservation, host-remnant, origin, and collision gates, while ten-package bands remain below content capacity.

## Validation evidence and limitations

The read-only `hoi4_map_inspect` query covered states 42, 51, 52, 53, 54, and 64 and reported zero unknown provinces, zero missing geometry, valid state/region membership, and valid adjacency/supply/railway data; artifact SHA `6927a073aca2d02e2f907742e699e5163392878393ff7e1d2e81b2ce083c054e`.

The same map artifact reported unrelated global map-position/port/entity-locator diagnostics; those are not tied to states 52-54 or this package and were not treated as an IW-009 blocker.

The read-only focus inspection found the shared-tree layout diagnostics recorded above; this audit did not rewrite the shared tree or claim those global diagnostics resolved.

Source-level checks covered exact tag/package IDs, setup/prepared/complete trigger chains, map bindings, host state, force profile, decision/mission IDs, focus IDs, AI profile IDs, localisation consumers, portrait hashes, and cleanup references.

A seeded AI/probability sweep and live-engine release/scenario run were not performed because this bounded handoff is a static post-wire audit and the parent explicitly requested no wait for live-engine tests; weighted runtime behavior remains an unvalidated risk, not a discovered BAY package defect.

## Simplifications, omissions, and blockers

No IW-009 gameplay, map, focus, decision, AI, localisation, or asset simplification was introduced by this audit.

Event 006 remains globally incomplete outside this package; this handoff does not promote any other package or alter the global allocator.

Shared focus-tree connector/layout diagnostics, unrelated global map-position diagnostics, unavailable Technology Tree Viewer coverage, and absent live-engine execution are the remaining validation limitations.

## Parent handoff

Promotion authorization: add the exact IW-009 content-attestation check to `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`, update the attestation comment, and rerun the parent-owned compile-time gate, allocator capacity, and SCN-008 admission checks.

Do not add new adapter, scenario, map, country, portrait, advisor, or focus branches for IW-009; those surfaces are already present and independently audited.

If the parent-owned rerun finds a changed Dollmann runtime hash, stale `Schobert` consumer, active Rupprecht ownership in GER, a failed host-remnant check, or a new BAY-specific focus/decision/asset diagnostic, withdraw this authorization and keep IW-009 fail-closed pending a new audit.
