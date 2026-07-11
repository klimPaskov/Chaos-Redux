# Camp Repression Rework: Source-of-Truth and Completion Tracker

Feature id: `system_camp_repression_rework`

Curated: 2026-07-11

Purpose: provide one implementation ledger for the accepted package in `docs/specs/system_camp_repression_rework_specs/`, record active precedence, assign file ownership, and prevent partial implementation from being reported as complete.

This is a working plan, not a replacement for the accepted specs. The specs remain the source design except where the current user request and the package's current implementation prompts explicitly override older text. No gameplay, localisation, asset, or workbook implementation is evidenced by this document.

## Live implementation reconciliation, 2026-07-11

Status: **implementation complete; static contracts passed; engine-runtime scenario execution gap recorded**.

This section is the current implementation ledger. It supersedes the preimplementation observations and empty implementation-status columns retained later in this file. Those older rows remain useful as acceptance-history evidence, but they must not be used to infer that live files or surfaces are absent.

### Current implementation surfaces

| Surface | Live source |
| --- | --- |
| Shared lifecycle, registration, Deaths, evidence, cleanup, display cache, and GUI action routing | `common/scripted_effects/camp_repression_rework_effects.txt` |
| Unified player decision dispatcher | `common/scripted_effects/camp_repression_action_dispatcher_effects.txt` |
| Territorial pools, route gates, restricted-method gates, and mission outcome triggers | `common/scripted_triggers/camp_repression_rework_triggers.txt` |
| Generic player actions and generic missions | `common/decisions/camp_repression_generic_decisions.txt` |
| Germany, Japan, and Soviet actions and missions | `common/decisions/camp_repression_major_country_decisions.txt` |
| U.K./Raj, U.S.A., France/Vichy, Italy, and Belgium actions and missions | `common/decisions/camp_repression_colonial_country_decisions.txt` |
| Major-country effects, ideas, modifiers, projects, and events | `common/scripted_effects/camp_repression_major_country_effects.txt`, `common/ideas/camp_repression_major_country_ideas.txt`, `common/dynamic_modifiers/camp_repression_major_country_dynamic_modifiers.txt`, `common/special_projects/projects/japan_ishii_projects.txt`, `events/japan_ishii.txt`, and `events/soviet_gulag.txt` |
| Colonial-country effects and ideas | `common/scripted_effects/camp_repression_colonial_country_effects.txt` and `common/ideas/camp_repression_colonial_country_ideas.txt` |
| Germany focus reward lifecycle | `common/national_focus/germany_mengele_clone_army.txt` and `common/ideas/germany_mengele_ideas.txt` |
| Repression Ledger | `common/scripted_guis/camp_repression_ledger_scripted_gui.txt`, `common/scripted_localisation/camp_repression_ledger_scripted_localisation.txt`, and `interface/camp_repression_ledger.gui` |
| Presentation wiring | `interface/camp_repression_rework.gfx`, `interface/chaosx_super_events.gfx`, `interface/chaosx_achievements.gfx`, and `interface/special_projects/biowarfare.gfx` |

### Exact player-action inventory

The implemented decision files contain **84 verified player actions**: 29 major, 43 colonial, and 12 generic. Mission blocks and the Ledger open, close, show, and hide controls are not included in this count. The three closing actions are live as `fr_support_refugee_and_rescue_networks`, `bel_negotiate_colonial_strike_settlement`, and `generic_inspect_active_site`.

| Family | Count | Exact live actions |
| --- | ---: | --- |
| Germany | 7 | `germany_route_prisoner_labor_to_war_construction`, `germany_redirect_prisoner_labor_to_eastern_fortifications`, `germany_tighten_deportation_logistics`, `germany_increase_guard_allocation_to_ss_sites`, `germany_build_ss_laboratory_annex_at_auschwitz`, `germany_destroy_auschwitz_evidence_before_retreat`, `germany_dismantle_auschwitz_complex` |
| Japan | 13 | `japan_establish_pingfang_research_bureau`, `japan_expand_occupation_test_records`, `japan_shield_ishii_from_army_review`, `japan_redirect_records_to_army_medical_control`, `japan_invite_kwantung_army_medical_officers`, `japan_suppress_chinese_resistance_cells`, `japan_route_supplies_to_epidemic_prevention`, `japan_open_epidemic_containment_office`, `japan_destroy_pingfang_records`, `japan_evacuate_pingfang_research_staff`, `japan_submit_to_army_review`, `japan_remove_ishii_from_program_control`, `japan_shut_down_prisoner_experiments` |
| Soviet Union | 9 | `sov_transfer_prisoners_to_industrial_camps`, `sov_reinforce_nkvd_authority`, `sov_reduce_paranoia_through_party_review`, `sov_release_prisoners_for_military_service`, `sov_dismantle_overextended_gulags`, `sov_emergency_famine_relief`, `sov_conceal_famine_mortality`, `sov_admit_local_administrative_collapse`, `sov_authorize_extreme_periphery_repression` |
| U.K. and Raj | 10 | `uk_survey_raj_emergency_detention`, `uk_activate_raj_emergency_detention`, `uk_route_colonial_labor_to_military_construction`, `uk_expand_raj_detention_districts`, `uk_demand_indian_manpower_levy`, `uk_tighten_dominion_security_coordination`, `uk_allocate_additional_colonial_guards`, `uk_release_political_prisoners_for_negotiations`, `uk_reform_colonial_labor_administration`, `uk_dismantle_raj_detention_network` |
| U.S.A. | 8 | `usa_authorize_emergency_relocation_zones`, `usa_expand_interior_security_camps`, `usa_assign_detainee_labor_to_local_works`, `usa_strengthen_wartime_review_boards`, `usa_allow_court_review`, `usa_release_detainees_under_supervision`, `usa_terminate_relocation_authority`, `usa_establish_redress_commission` |
| France and Vichy | 9 | `fr_inspect_camp_legacy`, `fr_close_camp_legacy_sites`, `fr_expand_vichy_internment_administration`, `fr_route_north_africa_labor_to_rail_projects`, `fr_collaboration_transfer_records`, `fr_suppress_refugee_and_rescue_networks`, `fr_support_refugee_and_rescue_networks`, `fr_open_colonial_labor_review`, `fr_dismantle_north_africa_labor_network` |
| Italy | 8 | `ita_reopen_desert_camp_administration`, `ita_authorize_homeland_emergency_detention`, `ita_redirect_colonial_labor_to_roads_and_forts`, `ita_force_settlement_of_rebel_districts`, `ita_raise_colonial_security_battalions`, `ita_expand_desert_transport_guard`, `ita_close_desert_camps`, `ita_compensate_local_communities` |
| Belgium and Congo | 8 | `bel_expand_concession_labor_quotas`, `bel_route_labor_to_rubber_and_minerals`, `bel_build_congo_transport_corridors`, `bel_suppress_colonial_strikes`, `bel_negotiate_colonial_strike_settlement`, `bel_open_international_inspection`, `bel_reform_concession_system`, `bel_recognize_local_administration` |
| Generic | 12 | `generic_activate_detention_network`, `generic_expand_labor_quotas`, `generic_redirect_labor_to_construction`, `generic_redirect_labor_to_resource_extraction`, `generic_allocate_additional_guards`, `generic_reduce_labor_quotas`, `generic_inspect_active_site`, `generic_upgrade_existing_site_to_radicalized_atrocity_site`, `generic_restricted_contaminated_site_escalation`, `generic_destroy_evidence_before_retreat`, `generic_dismantle_detention_network`, `camp_repression_close_dormant_legacy_site` |

The major-country file owns 29 verified actions and 17 missions. The colonial-country file owns 43 verified actions and 19 missions. The generic file owns 12 verified actions and 5 missions. The total inventory is therefore 84 player actions, 41 missions, and four separate Ledger controls.

The final decision-and-mission re-audit passed after the bounded cooldown-parity correction. All 32 Ledger country action slots use the same native decision cooldown gates as their corresponding normal decisions. The full evidence is recorded in `subagent_handoffs/decision_mission_final_audit_2026-07-11.md`.

### Current action, pool, and route contracts

- `camp_rework_route_country_specific_action` is the unified country action bus. Decisions set `camp_rework_action_id`, and state actions use the normal country variable `camp_rework_action_state_id`.
- `camp_rework_prepare_selected_action_state` copies a human Ledger selection into the action pointer. `camp_rework_dispatch_prepare_colonial_selection` and `camp_rework_dispatch_restore_colonial_selection` let colonial helpers act on direct or subject-controlled states without overwriting the persistent Ledger selection.
- The host-owned monthly runtime processes the connected active-country and active-state arrays. State harm reduces real state population through the Chaos Meter Deaths pipeline rather than through a parallel counter or recruitable-population modifier alone.
- Active sites retain the stored responsible country. Evidence-based discovery and condemnation follow that stored authority across owner or controller changes and do not blame the discoverer.
- France uses `is_france_camp_legacy_pool_state`, `is_france_north_africa_labor_pool_state`, `is_france_vichy_internment_pool_state`, `is_france_other_colonial_labor_pool_state`, and `is_france_core_fallback_pool_state`.
- Italy uses `is_italy_libya_repression_pool_state`, `is_italy_east_africa_repression_pool_state`, `is_italy_balkan_occupation_pool_state`, `is_italy_colonial_project_pool_state`, and `is_italy_core_fallback_pool_state`. The project pool accepts Libya or East Africa. `ita_authorize_homeland_emergency_detention` is the explicit desperate homeland route and is not a colonial project shortcut.
- Fixed country packages do not inherit the generic fascist or communist restricted-method route. `camp_rework_country_can_use_restricted_method_route` requires the Germany full-permission and autonomy gate, the Japan Ishii project and influence gate, `sov_camp_extreme_escalation_available`, or an explicit extreme-doctrine gate for the colonial kits. Capability triggers also require the matching live stockpile.
- Restricted-method capacity is abstract. Chemical tiers are chlorine, phosgene, mustard, lewisite, tabun, sarin, and soman; biological tiers are anthrax, tularemia, plague, and smallpox. They resolve through stockpile, Deaths, contamination or outbreak, evidence, discovery, instability, and tribunal outcomes without operational instructions or protected-class selectors.

### Ledger, presentation, and catalog status

- The live Ledger has five tabs: **Overview**, **State Pools**, **Active Sites**, **Country System**, and **Discovery & Reform**.
- Its header displays `[ROOT.GetName]: [GetCampCountryPanelName]` plus the current phase and discovery state. All 24 generated Ledger sprites have live consumers, including scripted visibility for the evidence and reform seals.
- The 24 DDS sprites are derived from frozen ImageGen sources in `docs/assets/system_camp_repression_rework/source/ui_imagegen/`. Prompts are recorded in `docs/assets/system_camp_repression_rework/prompts/repression_ledger_imagegen_prompts.md`; `docs/assets/system_camp_repression_rework/tools/build_ledger_ui_assets.py` is the deterministic processor. This is the maintained static presentation, not a fallback or simple-shape substitute.
- Germany, Japan, the Soviet Union, the U.K./Raj, the U.S.A., France/Vichy, Italy, Belgium/Congo, and generic country kits are live.
- Germany's focus reward lifecycle has at most three stable lane spirits before convergence and exactly one final world-order spirit after convergence. The core variant preserves exact science-and-force totals; stage-specific variants preserve the exact highest completed optional territorial stage through reclamation, continental dominance, the command spine, or full world dominance. No new command prerequisite was added.
- Super-event slots `12`, `74`, `75`, `76`, and `77` use audio IDs `45`, `44`, `46`, `47`, and `48` respectively. Each slot has live text, a unique sprite, a unique final audio track, and settings-aware playback.
- The static asset tranche is present. It includes 24 Ledger UI assets, 102 live icon DDS files, 17 major report and super-event identities, 10 colonial or generic report and news identities, and achievement triplets for IDs `60` through `69`.
- The optional animated Ledger warning, evidence, reform, selected-state, and critical frames remain **queued** as an enhancement. The accepted static presentation is live and complete for the current scope.
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx` remains the event catalog. This package is a system rework and does not create a new standalone ChaosX event identity. The existing Soviet Collapse row `Events!C6` matches the live 1,148-character Event Details text.

### Completion disposition

- No accepted gameplay, decision, mission, Ledger, country-kit, asset, localisation, achievement, super-event, or audio implementation item remains open in this tracker.
- All 13 Part 7 scenarios plus `SCN-ABSTRACT-CHEM-BIO` and `SCN-FULL-LEDGER` passed static contract trace with `ScenarioContracts=15 Failed=0`. The evidence is in `scenario_contract_validation_report.md`.
- No engine-runtime scenario execution occurred in this environment. Rendered GUI behavior, timed mission outcomes, AI choices, and numeric runtime deltas therefore remain an explicit validation gap rather than a claimed pass.
- The final parent review is complete with the engine-runtime validation gap carried explicitly. The scoped commit is the closing repository action for this tranche.
- No fallback or simplification was used. Optional authored Ledger frame animation remains queued as an enhancement and is not a runtime blocker.

## Status discipline

Every requirement has exactly one plan disposition:

- **Pending**: required work has no reviewed completion evidence in this tracker.
- **Implemented**: final files and task-specific evidence have been reviewed and recorded.
- **Queued with reason**: accepted but intentionally deferred or conditional; the reason is mandatory.
- **Blocked with evidence**: cannot proceed; concrete repository or external evidence is mandatory.
- **Rejected with reason**: deliberately excluded because it conflicts with a higher-precedence instruction or an accepted boundary.

Pre-existing behavior is not automatically marked implemented. Existing buildings, Deaths helpers, camp arrays, discovery hooks, and Mengele integration are a baseline to preserve and audit during the rework. A row can move to implemented only after its final call sites, player-facing surfaces, AI, cleanup, and task-specific scenario evidence agree.

No implementation blocker is recorded at tracker creation. Missing final GUI dimensions, stable sprite names, final localisation, and super-event research are sequencing dependencies, not blockers.

## Source-of-truth map and precedence

### Precedence order

| Rank | Authority | How it governs implementation |
| ---: | --- | --- |
| 1 | Current user request and current parent task | Requires the full Repression Ledger GUI; requires the narrow abstract chemical/biological killing-efficiency override described below; requires honest dispositions and complete country/surface tracking. |
| 2 | `prompts/system_camp_repression_rework_goal_prompt.md`, `coding_prompt.md`, and `validation_prompt.md` | Current implementation and acceptance commands. Their repeated chemical/biological efficiency requirement overrides older package text only within the narrow abstract-gameplay boundary below. |
| 3 | Accepted specs Parts 1–7 | Primary system design. More detailed later parts control their own surface: Part 5 for country kits, Part 6 for GUI data/UI structure, Part 7 for implementation surfaces and scenarios. |
| 4 | Companion decision, GUI, asset, super-event, and achievement prompts | Specialist handoffs. They cannot weaken the current user request or contradict the accepted system invariants. |
| 5 | Four matrices | Coverage and tuning cross-checks. They clarify repeated requirements but do not silently remove detailed Part 3 or Part 5 content. |
| 6 | `README.md` and research notes | Purpose, historical anchors, and safety context. Their older absolute ban on abstract efficiency values is superseded only as recorded below; all bans on protected-class selectors and operational recipes remain controlling. |
| 7 | `source_review/read_files_manifest.md` | Provenance and source limitations only. It is not implementation evidence for the live repository. |
| 8 | `continuation/continuation_prompt.md` | Final handoff record only. It explicitly says it is not part of the spec. |

### Package file roles

| File | Role in the source of truth |
| --- | --- |
| `README.md` | Package purpose, baseline, design boundary, and planning completion statement. |
| `package_index.md` | Canonical package inventory. |
| `source_review/read_files_manifest.md` | Uploaded-source and package-read provenance. |
| `research/historical_anchor_notes.md` | Germany/Japan/Soviet/colonial historical design anchors and non-player-facing source direction. |
| `research/continuation_historical_sources.md` | Detailed U.S., U.K./Raj, France/Vichy, Italy, Belgium, Japan, and Soviet research anchors. |
| `specs/...part_1_core_loop.md` | Shared loop, phases, state-pool order, values, Deaths/discovery/dismantlement invariants. |
| `specs/...part_2_country_systems_major_powers.md` | Broad Germany, Japan, Soviet, U.K., U.S., France, Italy, Belgium, and generic country packages. |
| `specs/...part_3_germany_japan_soviet_deepening.md` | Detailed Germany/Mengele, Japan/Ishii, and Soviet paranoia/famine/Union Crisis requirements. |
| `specs/...part_4_ui_ai_assets_acceptance.md` | UI summary, AI principles/caps, asset families, achievement concepts, super-event candidates, and acceptance criteria. |
| `specs/...part_5_country_decision_kits_focus_hooks.md` | Exact U.K./Raj, U.S., France/Vichy, Italy, Belgium, and generic decisions, missions, ideas, focus hooks, AI, discovery, dismantlement, and asset ids. |
| `specs/...part_6_scripted_gui_wireframe_value_display.md` | Full ledger wireframe, header, values, arrays, buttons, visibility, cleanup, and GUI asset ids. |
| `specs/...part_7_implementation_checklist_validation.md` | File map, helper map, implementation order, checks, scenario matrix, and completion proof. |
| `matrices/values_and_pressure_model.md` | Core values, site types, dynamic death factors, state-pool order, and resource-cost palette. |
| `matrices/country_ai_matrix.md` | Country and generic AI activation, preferred behavior, caps, and reform direction. |
| `matrices/decision_mission_matrix.md` | Cross-country decision/mission family coverage. |
| `matrices/country_decision_kits_matrix.md` | Part 5 country-kit, decision-family, duration, discovery, and exact asset-id summary. |
| `prompts/...goal_prompt.md` | Current full-package implementation entry point and chemical/biological override source. |
| `prompts/...coding_prompt.md` | Current implementation surfaces, coding requirements, and chemical/biological override source. |
| `prompts/...validation_prompt.md` | Current completion criteria, including abstract nerve-agent outcome validation. |
| `prompts/...decision_mission_prompt.md` | Decision-layer implementation and cost/tooltip requirements. |
| `prompts/...gui_prompt.md` | GUI specialist handoff; its older header-first/full-window-if-needed wording is superseded by the current user request. |
| `prompts/...asset_prompt.md` | Asset families, source modes, final-file bundle, and stable-sprite sequencing. |
| `prompts/...super_event_prompt.md` | Conditional super-event roles and research/wiring rules. |
| `prompts/...achievement_prompt.md` | Ten achievement concepts and required icon/tracking/localisation/doc surfaces. |
| `continuation/continuation_prompt.md` | Non-spec resume record; read last and used only to confirm no planning section remains. |

### Archived repository surface observations at initial curation

This subsection records the preimplementation snapshot only. It is superseded by the live reconciliation above and must not be read as a claim that the Ledger or country surfaces are still absent.

- All core candidate files named in Part 7 exist, including the genocide-crisis constants, decisions/categories, effects, triggers, on-actions, modifiers, ideas, AI, Germany/Mengele integration, system documentation, and event catalog workbook.
- At initial curation, no genocide-crisis-specific scripted GUI file or `interface/genocide_crisis.gui` existed, so the full Ledger required a new intentional surface. That surface is now live in the files listed in the current implementation table above.
- The matching custom focus inventory contains the Germany/Mengele tree and Soviet-collapse trees, but no dedicated U.K., U.S., France/Vichy, Italy, or Belgium tree files. Their Part 5 route flags/decision gates are the current accepted hook surface unless the parent separately approves new bespoke trees.
- These observations establish likely ownership and sequencing only. They are not completion evidence and do not mark any gameplay row implemented or blocked.

## Resolved contradictions and active overrides

| Id | Conflict | Active resolution | Pending | Implemented | Queued with reason | Blocked with evidence | Rejected with reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `PRECEDENCE-CHEM-BIO` | README, research, Parts 1/4/5/6, and the values matrix say no efficiency curve or optimization; current goal/coding/decision/GUI/validation prompts and continuation require chemical/biological killing-efficiency mechanics, including nerve agents. | Implemented as abstract capability and stockpile tiers feeding Deaths, contamination or outbreak, evidence, discovery, instability, and tribunal outcomes. No recipes, synthesis, dosage, delivery engineering, operational procedures, protected-class selectors, or real-world optimization guidance are present. | [ ] | [x] | — | — | — |
| `PRECEDENCE-GUI` | Parts 4/6/7 and older coding/GUI prompts allow the full GUI to be optional or deferred behind a header. | Implemented as the full five-tab `repression_ledger_window` plus a country/panel/phase/discovery header. All 24 generated static sprites are consumed; the result is not header-only or a simple-shape fallback. | [ ] | [x] | — | — | — |
| `PRECEDENCE-FOCUS` | Part 5 permits route flags when the live repo has no relevant custom country tree; repository rules forbid unapproved fallbacks. | Implemented through the accepted country route flags and decision gates where no bespoke tree exists. Germany's custom focus reward lifecycle is consolidated to at most three stable spirits and exactly one conditional final variant with preserved arithmetic; the optional command branch remains optional. No whole vanilla tree was silently replaced. | [ ] | [x] | — | — | — |
| `PRECEDENCE-ANIMATION` | Part 6 recommends animation but accepts static presentation; the full GUI is now mandatory. | The generated static GUI is implemented and maintained. Authored frame animation remains optional and outside the accepted completion gate. | [ ] | [ ] | [x] Optional enhancement; the complete static presentation remains live. | — | — |
| `REJECT-HEADER-ONLY` | Header-only implementation could previously satisfy a deferred GUI tranche. | Header-only completion cannot satisfy the current request. | [ ] | [ ] | — | — | [x] Full Repression Ledger is required. |
| `REJECT-OPERATIONAL-CHEM-BIO` | A literal reading of “optimization” could invite operational detail. | Operational recipes, production instructions, dosages, delivery procedures, or real-world targeting guidance are outside the accepted abstract game design. | [ ] | [ ] | — | — | [x] Only abstract game values and consequences are accepted. |
| `REJECT-PROTECTED-SELECTOR` | Country/state history includes persecution context. | No player-operated selector by ethnicity, religion, nationality, or other protected class. | [ ] | [ ] | — | — | [x] State pools must remain territorial, legal, political, occupation, colonial, periphery, prison-labor, or crisis based. |
| `REJECT-WORLD-LOOP` | A separate daily/weekly/monthly world scan would simplify refresh logic. | Use the existing registered active-site array, host-only monthly path, state-control hooks, decisions, GUI-open refresh, and bounded country/state events. | [ ] | [ ] | — | — | [x] AGENTS.md and Part 6/7 forbid a new broad loop. |

## Archived preimplementation requirement ledger

All checkbox matrices from this heading through the final scenario matrix are frozen planning-time acceptance evidence. Their `Pending`, `Implemented`, and `Queued` cells are not current implementation status and must not be used for completion claims. The live reconciliation at the top of this file, `completion_report.md`, and `scenario_contract_validation_report.md` supersede them; the archived rows remain only to prove that no accepted requirement disappeared during implementation. In particular, archived pending GUI rows do not mean the five-tab Ledger is absent, and archived pending `SCN-*` rows do not override `ScenarioContracts=15 Failed=0` static trace evidence.

### Core system requirements

| Id | Accepted requirement | Implementation surfaces | Pending | Implemented | Queued with reason | Blocked with evidence | Rejected with reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `CORE-001` | Rework the existing system; preserve unique `concentration_camp`, `extermination_camp`, and `gulag_labor_camp_network` definitions without creating a parallel system. | `common/buildings/chaosx_buildings.txt`; genocide-crisis decisions/effects/triggers/docs. | [x] | [ ] | — | — | — |
| `CORE-002` | Store `genocide_responsible_country` on every active site and retain responsibility across owner/controller change until explicit cleanup. | `common/scripted_effects/genocide_crisis_effects.txt`; discovery/on-action helpers. | [x] | [ ] | — | — | — |
| `CORE-003` | Register active sites exactly once in `global.genocide_active_camp_states`; dormant markers do not register or process; dismantlement and invalidation unregister. | Scripted effects, triggers, host-only monthly pulse, cleanup paths. | [x] | [ ] | — | — | — |
| `CORE-004` | Route all camp, colonial labor, gulag, experiment, radicalized, contaminated, famine, and override deaths through Chaos Meter Deaths helpers. | `genocide_crisis_effects.txt`; `chaosx_on_actions_chaos_meter.txt`; existing bio/chemical Deaths wrappers. | [x] | [ ] | — | — | — |
| `CORE-005` | Reduce real state population through state-linked civilian-death effects; do not use only recruitable-population modifiers or a parallel counter. | Deaths helpers and monthly state processing. | [x] | [ ] | — | — | — |
| `CORE-006` | State-pool order is occupied non-core, colonial/subject, non-core integrated, country periphery/borderland/security/opposition marker, then punitive core fallback. | `common/scripted_triggers/genocide_crisis_triggers.txt`; country pool triggers; tooltips/GUI. | [x] | [ ] | — | — | — |
| `CORE-007` | Core fallback has lower output and higher stability, legitimacy, revolt, reform, and internal-backlash penalties. | Script constants; `camp_rework_apply_core_fallback_penalties`; ideas/tooltips/AI. | [x] | [ ] | — | — | — |
| `CORE-008` | Implement phases: dormant infrastructure; active detention/forced labor; expanded labor; radicalized atrocity; restricted contaminated/chemical/biological escalation; discovery/reform/dismantled states. | Buildings/flags, scripted effects/triggers, ideas/dynamic modifiers, decisions, GUI phase localisation. | [x] | [ ] | — | — | — |
| `CORE-009` | Expanded networks provide meaningful construction/extraction/control pressure but consume varied equipment, transport, manpower, factory, command, supply, stability, war-support, compliance, or autonomy costs. | Constants; decisions/missions; effects; tooltips; AI resource checks. | [x] | [ ] | — | — | — |
| `CORE-010` | Radicalized escalation is liability-heavy: severe Deaths/population loss, resistance/refugee pressure, stability/support loss, supply/guard/rail strain, evidence, tribunal, coup/revolt/collapse risk; hardliner/fear benefits are limited. | Decisions, ideas/dynamic modifiers, monthly effects, events, AI caps, GUI. | [x] | [ ] | — | — | — |
| `CORE-011` | Abstract chemical/biological efficiency override: capability and stockpile, including nerve-agent capability, can increase abstract Deaths and lower short-term resistance; every use consumes stockpile/logistics and increases contamination, evidence, instability, discovery, reaction, and tribunal pressure. | Genocide/chemical/bio constants and helpers; decisions; Deaths; AI; localisation; validation. | [x] | [ ] | — | — | — |
| `CORE-012` | Implement the core national values and state evidence/burden fields from Parts 1 and 5 through central constants and reusable helpers. | Script constants, scripted effects/triggers, dynamic modifiers, scripted localisation. | [x] | [ ] | — | — | — |
| `CORE-013` | Monthly loss scales dynamically from state population and context: site type, reach, overreach, occupation/non-core status, famine, permission, experiment/contamination flags, guards, supply/rail, chaos, retreat, and relief/reform. | Constants and monthly state effect; no scattered fixed tiny values. | [x] | [ ] | — | — | — |
| `CORE-014` | Routine play remains quiet: dormant sites are silent; category and GUI hide without meaningful action; no recurring leak, report, sabotage, refugee, or minor flavor popup from monthly processing. | Category visibility, event call sites, monthly effects, GUI visibility/cleanup. | [x] | [ ] | — | — | — |
| `CORE-015` | Reserve events/popups for first activation/escalation, breakdown, contaminated escalation, major discovery, tribunal threshold, country thresholds, colonial revolt, and dismantlement completion. | `events/genocide_crisis_events.txt`; Germany/Japan/Soviet and colonial event hooks. | [x] | [ ] | — | — | — |
| `CORE-016` | Every expandable route has inspection, relief, dismantlement, reform, redress, compensation, or post-authoritarian cleanup; cleanup stops registration and converts ideas without automatically reactivating after failure. | Decisions/missions, effects, ideas, discovery/regime-change hooks, AI. | [x] | [ ] | — | — | — |
| `CORE-017` | Discovery is physical/evidence-based: state capture, capitulation, records opening, tribunal, observer/survivor threshold, contamination/experiment exposure, and country-specific legal/colonial exposure. | On-actions, triggers/effects, events/news, country decisions. | [x] | [ ] | — | — | — |
| `CORE-018` | Discovery calculates severity from site/evidence/repeat discovery/contamination/experiments/reach, condemns the stored responsible country, updates Deaths/Condemnation, and bounds discoverer/responsible/news events. | Discovery effect, opinion modifiers, Chaos Meter integration, events/localisation. | [x] | [ ] | — | — | — |
| `CORE-019` | World-end hooks remain indirect except an existing terminal country chain such as the Angelic World Order. | Germany/Mengele world-threat helpers; super-event/world-end integration. | [x] | [ ] | — | — | — |
| `CORE-020` | Use reusable scripted triggers/effects, bounded arrays, state selection, script constants, and existing dynamic helpers; document any new dynamic helper in its required companion documentation. | `genocide_crisis_*`; `chaosx_dynamic_effects.txt/.md`; Part 7 helper map. | [x] | [ ] | — | — | — |
| `CORE-021` | AI uses the same valid pools/actions as players, has country/route caps, and reforms/dismantles after route change, discovery, defeat, or postwar scrutiny. | AI strategy, decision `ai_will_do`, shared cap/target effects, route flags. | [x] | [ ] | — | — | — |
| `CORE-022` | Implement bespoke Germany, Japan, Soviet, U.K./Raj, U.S., France/Vichy/North Africa, Italy/Libya, Belgium/Congo, and conservative generic packages; do not substitute copied generic content. | Country integration files and shared dispatcher. | [x] | [ ] | — | — | — |
| `CORE-023` | Keep visible decision/mission/idea/GUI/event localisation, icons, tooltips, costs, effects, and docs synchronized; player text is in-world and hides formulas/debug/future surprises. | English localisation, scripted localisation, GFX/GUI, docs. | [x] | [ ] | — | — | — |
| `CORE-024` | Update the event catalog workbook only after implementation facts and final in-game wording exist. | `docs/spreadsheets/chaos_redux_events_catalog.xlsx` through spreadsheet worker. | [x] | [ ] | — | — | — |
| `CORE-025` | Final completion proof includes route coverage, final helper names, Deaths/population/responsibility evidence, AI/UI/assets/docs/workbook status, task-specific scenarios, and every simplification or omission. | Completion report and final audits. | [x] | [ ] | — | — | — |

## Values, fields, helpers, and tuning inventory

| Id | Package | Required identifiers or fields | Primary surfaces | Pending | Implemented | Queued with reason | Blocked with evidence | Rejected with reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `VALUES-CORE` | Shared country values | `camp_network_reach`, `camp_labor_output`, `camp_coercive_control`, `camp_population_loss_index`, `camp_resistance_pressure`, `camp_stability_damage`, `camp_evidence_level`, `camp_overstretch`, `camp_foreign_visibility`, `camp_tribunal_severity`, `camp_hardliner_pressure`, `camp_democratic_legitimacy_damage`, `camp_reform_pressure` | Constants, effects, ideas/dynamic modifiers, GUI display refresh. | [x] | [ ] | — | — | — |
| `VALUES-STATE` | Shared state fields | site type; responsible country; evidence depth; monthly death pressure; local labor output; local resistance pressure; observer exposure; destroyed evidence; failed cover-up; liberated evidence; experiment-linked; contaminated evidence; active/dormant/discovered/invalid registration | State variables/flags/arrays and scripted effects/triggers. | [x] | [ ] | — | — | — |
| `VALUES-GER` | Germany | `racial_policy_radicalization`, `ss_archive_control`, `occupied_deportation_pressure`, `poland_transfer_pressure`, `mengele_autonomy`, `mengele_permission_level`, `auschwitz_evidence_depth`, `foreign_atrocity_awareness`, `hardliner_pressure` | Germany/Mengele constants, effects, triggers, decisions/events, GUI. | [x] | [ ] | — | — | — |
| `VALUES-JAP` | Japan | `imperial_occupation_reach`, `kwantung_autonomy`, `ishii_influence`, `occupation_test_records`, `bio_research_gain`, `bio_project_pressure`, `outbreak_accident_risk`, `chinese_resistance_pressure`, `occupation_evidence_depth`, `evidence_depth_china`, `tribunal_biowarfare_severity`, `pingfang_facility_level`, `imperial_army_review_pressure` | Shared/country effects/triggers/decisions/projects/GUI. | [x] | [ ] | — | — | — |
| `VALUES-SOV` | Soviet Union | `gulag_network_reach`, `nkvd_authority`, `paranoia_pressure`, `forced_labor_quota`, `grain_extraction_burden`, `famine_pressure`, `republic_fear`, `old_movement_grievance`, `camp_administrator_corruption`, `union_crisis_suppression_relief`, `union_crisis_terminal_severity` | Genocide-crisis and Soviet/Union Crisis integration. | [x] | [ ] | — | — | — |
| `VALUES-UK` | U.K./Raj | `imperial_detention_reach`, `raj_labor_burden`, `dominion_control_pressure`, `indian_autonomy_resistance`, `colonial_legitimacy_damage`, `imperial_manpower_pressure` | Shared/country decisions, ideas, effects, GUI. | [x] | [ ] | — | — | — |
| `VALUES-USA` | U.S.A. | `wartime_security_reach`, `civil_liberties_damage`, `court_challenge_pressure`, `democratic_legitimacy_damage`, `relocation_population_disruption`, `redress_pressure` | Shared/country decisions, ideas, missions, GUI. | [x] | [ ] | — | — | — |
| `VALUES-FR` | France/Vichy | `french_camp_legacy`, `vichy_collaboration_reach`, `north_africa_labor_burden`, `refugee_pressure`, `free_french_reform_credit` | Shared/country decisions, ideas, missions, GUI. | [x] | [ ] | — | — | — |
| `VALUES-ITA` | Italy | `colonial_repression_reach`, `desert_camp_burden`, `libyan_resistance_pressure`, `colonial_logistics_output`, `postwar_colonial_claim_damage` | Shared/country decisions, ideas, missions, GUI. | [x] | [ ] | — | — | — |
| `VALUES-BEL` | Belgium/Congo | `congo_extraction_pressure`, `concession_labor_burden`, `colonial_resource_output`, `congo_population_damage`, `colonial_unrest_pressure`, `postwar_accountability_pressure` | Shared/country decisions, ideas, missions, GUI. | [x] | [ ] | — | — | — |
| `VALUES-DIRECTORATE` | Mengele Directorate | `clone_manpower_output`, `laboratory_state_reach`, `numbered_army_growth`, `foreign_clone_network_strength`, `world_threat_source_mengele`, `internal_overwrite_pressure` | Germany/Mengele coup/victory effects, ideas, AI, docs. | [x] | [ ] | — | — | — |
| `HELPERS-TRIGGERS` | Shared helper triggers | `is_valid_camp_active_site_state`, `is_valid_camp_dormant_marker_state`, `is_valid_camp_discovery_state`, `is_valid_camp_dismantlement_state`, `is_valid_camp_enemy_proximity_state`, `has_active_camp_network`, `has_visible_camp_reform_work`, `has_camp_category_visible_action`, plus all country pool triggers listed below | `common/scripted_triggers/genocide_crisis_triggers.txt`. | [x] | [ ] | — | — | — |
| `HELPERS-EFFECTS` | Shared helper effects | `camp_rework_register_active_site`, `camp_rework_unregister_inactive_site`, `camp_rework_clean_invalid_active_sites`, `camp_rework_apply_monthly_state_effects`, `camp_rework_apply_country_monthly_pressure`, `camp_rework_rebuild_display_values`, `camp_rework_rebuild_gui_arrays`, `camp_rework_select_state_for_display`, `camp_rework_clear_selected_state`, `camp_rework_apply_discovery`, `camp_rework_attempt_evidence_destruction`, `camp_rework_start_dismantlement`, `camp_rework_complete_dismantlement`, `camp_rework_apply_core_fallback_penalties`, `camp_rework_apply_ai_cap`, `camp_rework_route_country_specific_action` | `common/scripted_effects/genocide_crisis_effects.txt` or reviewed closer existing helpers. | [x] | [ ] | — | — | — |
| `CONSTANTS-GROUPS` | Tuning | `camp_rework_common`, `camp_rework_costs`, `camp_rework_ai`, `camp_rework_mission_days`; include display bands, site loss factors, pool output factors, fallback penalties, costs, caps, durations, and abstract chemical/biological/nerve-agent outcome factors | `common/script_constants/genocide_crisis_constants.txt` and narrowly related chemical/bio constant files where ownership requires. | [x] | [ ] | — | — | — |

## Country content inventory

Working labels without script ids are kept as labels; the implementing owner must record the final id here before marking the row implemented. Part 5 ids are implementation ids unless the live repository requires a reviewed naming adjustment.

### State pools and route gates

| Id | Package | Required pools/gates | Primary surfaces | Pending | Implemented | Queued with reason | Blocked with evidence | Rejected with reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `POOLS-GER` | Germany | Occupied/non-core Europe first; occupied Poland preferred for Auschwitz transfers; Auschwitz state `88`; German cores only if no higher pool, with punitive fallback. | Genocide and Mengele triggers/effects/decisions/GUI. | [x] | [ ] | — | — | — |
| `POOLS-JAP` | Japan | Controlled China, Manchuria, and colonial states first; home islands only in desperate high-chaos/doomsday fallback, with lower benefit and higher stability/military-obedience damage. | Genocide triggers/effects/decisions/projects/GUI. | [x] | [ ] | — | — | — |
| `POOLS-SOV` | Soviet Union | Remote Siberian, Far Eastern, northern, Kazakh, Central Asian, industrial, borderland, periphery, deportation, and political-opposition route pools; extreme route requires critical paranoia/extreme ideology/high chaos/collapse desperation. | Genocide/Soviet triggers, decisions, Union Crisis bridge. | [x] | [ ] | — | — | — |
| `POOLS-UK` | U.K./Raj | `is_uk_raj_detention_pool_state`, `is_uk_indian_ocean_security_pool_state`, `is_uk_colonial_emergency_pool_state`, `is_uk_core_fallback_pool_state`; local owner/Raj receives burden while Britain retains responsibility. | Shared triggers/effects/decisions/GUI. | [x] | [ ] | — | — | — |
| `POOLS-USA` | U.S.A. | `is_usa_wartime_security_zone_state`, `is_usa_overseas_security_pool_state`, `is_usa_interior_relocation_site_state`, `is_usa_core_emergency_fallback_state`; activation requires war, homeland/Pacific threat, sabotage fear, or high chaos. | Shared triggers/effects/decisions/GUI. | [x] | [ ] | — | — | — |
| `POOLS-FR` | France/Vichy | `is_france_camp_legacy_state`, `is_vichy_collaboration_pool_state`, `is_france_north_africa_labor_pool_state`, `is_france_colonial_labor_pool_state`, `is_france_core_fallback_pool_state`; store Vichy and German-linked responsibility separately. | Shared triggers/effects/decisions/GUI. | [x] | [ ] | — | — | — |
| `POOLS-ITA` | Italy | `is_italy_libya_repression_pool_state`, `is_italy_east_africa_repression_pool_state`, `is_italy_balkan_occupation_pool_state`, `is_italy_colonial_logistics_project_state`, `is_italy_core_fallback_pool_state`; colonial decisions cannot use Italian cores. | Shared triggers/effects/decisions/GUI. | [x] | [ ] | — | — | — |
| `POOLS-BEL` | Belgium/Congo | `is_bel_congo_concession_pool_state`, `is_bel_congo_transport_project_state`, `is_bel_colonial_emergency_pool_state`, `is_bel_core_fallback_pool_state`; Congo package never uses Belgian cores; exile use requires continuing control/subject validity. | Shared triggers/effects/decisions/GUI. | [x] | [ ] | — | — | — |
| `POOLS-GENERIC` | Generic | `is_generic_occupied_camp_pool_state`, `is_generic_colonial_camp_pool_state`, `is_generic_noncore_security_pool_state`, `is_generic_political_opposition_pool_state`, `is_generic_core_fallback_pool_state`; activation gated by ideology, war, occupation, resistance, chaos doctrine, or severe crisis. | Shared triggers/effects/decisions/GUI. | [x] | [ ] | — | — | — |

### Decision requirements

| Id | Package | Every accepted decision/decision-family item | Primary surfaces | Pending | Implemented | Queued with reason | Blocked with evidence | Rejected with reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `DEC-GER` | Germany | Centralize SS Camp Administration;<br>Expand Occupied Poland Camp Administration;<br>Route Prisoner Labor to War Construction;<br>Redirect Prisoner Labor to Eastern Fortifications;<br>Tighten Deportation Logistics / Assign Rail Capacity to Deportation Logistics;<br>Increase Guard Allocation / Increase Guard Allocation to SS Sites;<br>Restrict SS Autonomy;<br>Military Review of Auschwitz;<br>Close Auschwitz Program;<br>Transfer Prisoners to Experiment Sites / Transfer Prisoners to Auschwitz Experiments;<br>Build SS Laboratory Annex at Auschwitz;<br>Classify Eastern Records;<br>Purge SS Medical Offices;<br>Destroy Evidence During/Before Retreat;<br>Dismantle the Network after Regime Change / Dismantle Auschwitz Complex after Regime Change. | `common/decisions/germany_mengele_decisions.txt`; shared decisions/effects; final ids recorded here. | [x] | [ ] | — | — | — |
| `DEC-JAP` | Japan | Expand Forced Labor Camps in Occupied China;<br>Intensify Occupation Reprisals;<br>Transfer Prisoners to Experimental Facilities / Army Medical Research;<br>Fund Pingfang Research Infrastructure / Establish Pingfang Research Bureau;<br>Shield Ishii from Army Review;<br>Redirect Records to Army Medical Control;<br>Expand Occupation Test Records;<br>Invite Kwantung Army Medical Officers;<br>Suppress Chinese Resistance Cells;<br>Route Supplies to Epidemic Prevention;<br>Open Epidemic Containment Office after Accident;<br>Destroy Experiment Evidence During Retreat / Destroy Pingfang Records;<br>Evacuate Research Staff Before Soviet Advance;<br>Submit to Army Review;<br>Remove Ishii from Program Control;<br>Shut Down Prisoner Experiments. | Shared or reviewed Japan decision file; projects/events/effects; final ids recorded here. | [x] | [ ] | — | — | — |
| `DEC-SOV` | Soviet Union | Expand Remote Gulag Network;<br>Transfer Prisoners to Industrial Camps;<br>Intensify Forced Labor Quotas;<br>Confiscate Grain from Disloyal Regions;<br>Deport Suspected Opposition Networks;<br>Purge Camp Administrators;<br>Reinforce NKVD Authority;<br>Reduce Paranoia Through Party Review;<br>Release Prisoners for Military Service;<br>Dismantle Overextended Camps;<br>Destroy Records During Retreat;<br>Emergency Famine Relief;<br>Conceal Famine Mortality;<br>Admit Local Administrative Collapse. | Shared or reviewed Soviet decision file; paranoia/famine/Union Crisis effects; final ids recorded here. | [x] | [ ] | — | — | — |
| `DEC-UK` | U.K./Raj | `uk_survey_raj_emergency_detention`;<br>`uk_activate_raj_emergency_detention`;<br>`uk_route_colonial_labor_to_military_construction`;<br>`uk_expand_raj_detention_districts`;<br>`uk_demand_indian_manpower_levy`;<br>`uk_tighten_dominion_security_coordination`;<br>`uk_allocate_additional_colonial_guards`;<br>`uk_release_political_prisoners_for_negotiations`;<br>`uk_reform_colonial_labor_administration`;<br>`uk_dismantle_raj_detention_network`. | Shared or reviewed U.K. decision file and helper effects. | [x] | [ ] | — | — | — |
| `DEC-USA` | U.S.A. | `usa_authorize_emergency_relocation_zones`;<br>`usa_expand_interior_security_camps`;<br>`usa_assign_detainee_labor_to_local_works`;<br>`usa_strengthen_wartime_review_boards`;<br>`usa_allow_court_review`;<br>`usa_release_detainees_under_supervision`;<br>`usa_terminate_relocation_authority`;<br>`usa_establish_redress_commission`. | Shared or reviewed U.S. decision file and helper effects. | [x] | [ ] | — | — | — |
| `DEC-FR` | France/Vichy | `fr_inspect_camp_legacy`;<br>`fr_close_camp_legacy_sites`;<br>`fr_expand_vichy_internment_administration`;<br>`fr_route_north_africa_labor_to_rail_projects`;<br>`fr_collaboration_transfer_records`;<br>`fr_suppress_refugee_and_rescue_networks`;<br>`fr_open_colonial_labor_review`;<br>`fr_dismantle_north_africa_labor_network`. | Shared or reviewed France/Vichy decision file and helper effects. | [x] | [ ] | — | — | — |
| `DEC-ITA` | Italy | `ita_reopen_desert_camp_administration`;<br>`ita_redirect_colonial_labor_to_roads_and_forts`;<br>`ita_force_settlement_of_rebel_districts`;<br>`ita_raise_colonial_security_battalions`;<br>`ita_expand_desert_transport_guard`;<br>`ita_close_desert_camps`;<br>`ita_compensate_local_communities`. | Shared or reviewed Italy decision file and helper effects. | [x] | [ ] | — | — | — |
| `DEC-BEL` | Belgium/Congo | `bel_expand_concession_labor_quotas`;<br>`bel_route_labor_to_rubber_and_minerals`;<br>`bel_build_congo_transport_corridors`;<br>`bel_suppress_colonial_strikes`;<br>`bel_open_international_inspection`;<br>`bel_reform_concession_system`;<br>`bel_recognize_local_administration`. | Shared or reviewed Belgium decision file and helper effects. | [x] | [ ] | — | — | — |
| `DEC-GENERIC` | Generic | `generic_activate_detention_network`;<br>`generic_expand_labor_quotas`;<br>`generic_redirect_labor_to_construction`;<br>`generic_redirect_labor_to_resource_extraction`;<br>`generic_allocate_additional_guards`;<br>`generic_upgrade_existing_site_to_radicalized_atrocity_site`;<br>`generic_restricted_contaminated_site_escalation` plus abstract chemical/biological/nerve-agent variants required by the current prompts;<br>`generic_destroy_evidence_before_retreat`;<br>`generic_dismantle_detention_network`;<br>show/hide managed-network controls where the category pattern needs them. | `common/decisions/genocide_crisis_decisions.txt`; shared helpers/localisation/AI. | [x] | [ ] | — | — | — |

### Mission and timed-chain requirements

| Id | Package | Every accepted mission/timed-chain item | Primary surfaces | Pending | Implemented | Queued with reason | Blocked with evidence | Rejected with reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `MISSION-GER` | Germany | No exact new mission ids are fixed in the source. Required timed/threshold chains: military review; prisoner/rail transfer pressure; retreat evidence crisis; dismantlement; Directorate pre-revolt warnings; emergency isolate/reclaim/truce response. Final mission/event ids must be recorded before implementation status changes. | Germany decisions/events/effects/triggers. | [x] | [ ] | — | — | — |
| `MISSION-JAP` | Japan | No exact new mission ids are fixed. Required timed/threshold chains: Ishii independence; Army review; containment after outbreak; Soviet/Allied approach evacuation/evidence crisis; experiment shutdown; postwar exposure. Final mission/event ids must be recorded. | Japan decisions/events/effects/projects. | [x] | [ ] | — | — | — |
| `MISSION-SOV` | Soviet Union | No exact new mission ids are fixed. Required timed/threshold chains: quota/extraction cycle; famine pressure and relief; administrator purge/corruption; Union Crisis suppression cap; overextended-camp dismantlement; retreat records; collapse aftermath. Final mission/event ids must be recorded. | Soviet decisions/events/effects/Union Crisis integration. | [x] | [ ] | — | — | — |
| `MISSION-UK` | U.K./Raj | `uk_hold_raj_security_line` (150 days);<br>`uk_complete_raj_military_works` (180);<br>`uk_postwar_raj_review` (365);<br>`uk_negotiate_indian_release_terms` (270); cap at one security and one reform/construction mission. | Decisions/missions, constants, effects, AI. | [x] | [ ] | — | — | — |
| `MISSION-USA` | U.S.A. | `usa_court_review_period` (180);<br>`usa_security_authority_sunset` (270);<br>`usa_redress_commission_work` (365). | Decisions/missions, constants, effects, AI. | [x] | [ ] | — | — | — |
| `MISSION-FR` | France/Vichy | `fr_gurs_legacy_review` (180);<br>`fr_north_africa_rail_labor_project` (180);<br>`fr_refugee_pressure_response` (150);<br>`fr_post_liberation_reckoning` (365). | Decisions/missions, constants, effects, AI. | [x] | [ ] | — | — | — |
| `MISSION-ITA` | Italy | `ita_desert_road_labor_project` (180);<br>`ita_colonial_security_sweep` (150);<br>`ita_desert_camp_closure` (270);<br>`ita_postwar_colonial_compensation` (365). | Decisions/missions, constants, effects, AI. | [x] | [ ] | — | — | — |
| `MISSION-BEL` | Belgium/Congo | `bel_congo_resource_quota_cycle` (120);<br>`bel_congo_transport_corridor_project` (210);<br>`bel_colonial_strike_response` (150);<br>`bel_concession_reform_mandate` (365); cap one quota cycle and one transport project. | Decisions/missions, constants, effects, AI. | [x] | [ ] | — | — | — |
| `MISSION-GENERIC` | Generic | `generic_labor_project_cycle` (120–180);<br>`generic_network_overstretch_crisis` (150);<br>`generic_reform_and_dismantlement` (270–540);<br>`generic_retreat_evidence_crisis` (30–60). | Shared decisions/missions, constants, effects, AI. | [x] | [ ] | — | — | — |
| `MISSION-COMMON-COSTS` | All | Emergency activation/inspection 90–120; project 120–180; suppression 120–210; reform/dismantlement 180–365; major settlement 270–540. Costs draw from political power, command power, infantry/support equipment, trucks/trains/convoys, manpower, civilian-factory burden, stability, war support, supply, compliance/autonomy, army XP where appropriate; political power is never the only default cost. | Script constants and all decision/mission files/tooltips. | [x] | [ ] | — | — | — |

### Idea lifecycle requirements

| Id | Package | Every accepted idea/lifecycle item | Primary surfaces | Pending | Implemented | Queued with reason | Blocked with evidence | Rejected with reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `IDEA-GER` | Germany/Directorate | Country-specific staged ideas for dormant SS camp legacy, active administration, Auschwitz experiment/facility linkage, Mengele laboratory autonomy, overextension/discovery/reform pressure, and Directorate laboratory-state economy/unit state. Exact new ids are not fixed in the package and must be recorded. | `common/ideas/genocide_crisis_ideas.txt`, Germany idea files, dynamic modifiers. | [x] | [ ] | — | — | — |
| `IDEA-JAP` | Japan | Country-specific staged ideas for dormant occupation apparatus, active forced-labor/experiment network, Ishii influence, Kwantung autonomy, outbreak/tribunal pressure, overextension, review/shutdown, and postwar exposure. Exact new ids must be recorded. | Shared/Japan ideas and dynamic modifiers. | [x] | [ ] | — | — | — |
| `IDEA-SOV` | Soviet Union | Country-specific staged ideas for dormant gulag legacy, active gulag/NKVD authority, forced-labor output, corruption/overextension, famine pressure, republic fear/grievance, reform/dismantlement, and collapse aftermath. Exact new ids must be recorded. | Shared/Soviet ideas and dynamic modifiers. | [x] | [ ] | — | — | — |
| `IDEA-UK` | U.K./Raj | `uk_imperial_detention_legacy`;<br>`uk_imperial_detention_administration`;<br>`uk_overextended_imperial_detention`;<br>`raj_colonial_labor_burden`;<br>`uk_imperial_reform_credit`;<br>`uk_colonial_reckoning_pressure`. | Shared/U.K. idea files and local-state modifiers. | [x] | [ ] | — | — | — |
| `IDEA-USA` | U.S.A. | `usa_wartime_security_authority`;<br>`usa_contested_relocation_authority`;<br>`usa_civil_liberties_damage`;<br>`usa_relocation_population_disruption`;<br>`usa_redress_pressure`;<br>`usa_reform_credit`. | Shared/U.S. idea files and state modifiers. | [x] | [ ] | — | — | — |
| `IDEA-FR` | France/Vichy | `fr_camp_legacy`;<br>`vichy_collaboration_repression`;<br>`fr_north_africa_labor_burden`;<br>`fr_refugee_pressure`;<br>`free_france_reform_credit`;<br>`fr_post_liberation_reckoning`. | Shared/France idea files and state modifiers. | [x] | [ ] | — | — | — |
| `IDEA-ITA` | Italy | `ita_colonial_repression_legacy`;<br>`ita_desert_camp_administration`;<br>`ita_libyan_resistance_pressure`;<br>`ita_colonial_logistics_output`;<br>`ita_postwar_colonial_claim_damage`;<br>`ita_colonial_reform_credit`. | Shared/Italy idea files and state modifiers. | [x] | [ ] | — | — | — |
| `IDEA-BEL` | Belgium/Congo | `bel_congo_concession_labor_system`;<br>`bel_congo_extraction_pressure`;<br>`congo_concession_labor_burden`;<br>`bel_colonial_resource_output`;<br>`bel_postwar_accountability_pressure`;<br>`bel_congo_reform_credit`. | Shared/Belgium idea files and state modifiers. | [x] | [ ] | — | — | — |
| `IDEA-GENERIC` | Generic | `generic_detention_network_administration`;<br>`generic_expanded_labor_network`;<br>`generic_overextended_repression_network`;<br>`generic_radicalized_atrocity_policy`;<br>`generic_reform_pressure`;<br>`generic_reformed_legacy`; include an abstract contaminated/chemical/biological consequence stage if separate representation is needed. | `common/ideas/genocide_crisis_ideas.txt`; dynamic modifiers. | [x] | [ ] | — | — | — |

### Focus, route-flag, and special-project hooks

| Id | Package | Every accepted focus/project hook | Primary surfaces | Pending | Implemented | Queued with reason | Blocked with evidence | Rejected with reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `FOCUS-GER` | Germany | Existing Auschwitz/Mengele route hooks; camp-linked values in `common/national_focus/germany_mengele_clone_army.txt`; `sp_mengele_cloning` unlock requires full/bypass permission, high/critical autonomy, facility, active experiment site, archive/review state, and hidden project progress; no direct project completion. | Germany focus, special project, effects/triggers/events/decisions. | [x] | [ ] | — | — | — |
| `FOCUS-JAP` | Japan | Route hooks for Pingfang/Ishii/Kwantung authority and the five project working labels: Pingfang Records Office, Kwantung Medical Intelligence, Occupation Test Ledger, Epidemic Mapping Bureau, Cherry Blossom Dossier. Final project/focus ids must be recorded. | Japan/biowarfare projects, route flags, decisions/effects/events. | [x] | [ ] | — | — | — |
| `FOCUS-SOV` | Soviet Union | Route hooks into existing paranoia, purge, gulag, reform/de-Stalinization, Union Crisis, famine, and collapse systems; final focus/flag ids must be recorded. | Soviet/Union Crisis focus and shared route flags/effects. | [x] | [ ] | — | — | — |
| `FOCUS-UK` | U.K./Raj | `uk_focus_imperial_security_board`;<br>`uk_focus_wartime_raj_logistics`;<br>`uk_focus_indian_manpower_question`;<br>`uk_focus_dominion_coordination`;<br>`uk_focus_colonial_reform_committee`;<br>`uk_focus_indian_self_government_settlement`. | Existing tree if present; otherwise accepted route flags/decision gates, reported as hooks. | [x] | [ ] | — | — | — |
| `FOCUS-USA` | U.S.A. | `usa_focus_wartime_security_authority`;<br>`usa_focus_home_front_security_review`;<br>`usa_focus_supreme_court_review`;<br>`usa_focus_civil_liberties_restoration`;<br>`usa_focus_redress_commission`. | Existing tree if present; otherwise accepted route flags/decision gates, reported as hooks. | [x] | [ ] | — | — | — |
| `FOCUS-FR` | France/Vichy | `fr_focus_legacy_review_commission`;<br>`fr_focus_refugee_aid_networks`;<br>`vichy_focus_national_revolution_security`;<br>`vichy_focus_north_africa_labor_projects`;<br>`vichy_focus_collaboration_records`;<br>`free_france_focus_republican_reckoning`. | Existing tree if present; otherwise accepted route flags/decision gates, reported as hooks. | [x] | [ ] | — | — | — |
| `FOCUS-ITA` | Italy | `ita_focus_fourth_shore_security`;<br>`ita_focus_libyan_road_works`;<br>`ita_focus_colonial_security_corps`;<br>`ita_focus_east_africa_emergency_labor`;<br>`ita_focus_postwar_colonial_reform`;<br>`ita_focus_abandon_colonial_camps`. | Existing tree if present; otherwise accepted route flags/decision gates, reported as hooks. | [x] | [ ] | — | — | — |
| `FOCUS-BEL` | Belgium/Congo | `bel_focus_congo_resource_office`;<br>`bel_focus_exile_economy_congo`;<br>`bel_focus_congo_transport_corridors`;<br>`bel_focus_colonial_inspection_mandate`;<br>`bel_focus_reform_concession_system`;<br>`bel_focus_local_administration_recognition`. | Existing tree if present; otherwise accepted route flags/decision gates, reported as hooks. | [x] | [ ] | — | — | — |
| `FOCUS-GENERIC` | Generic | `unlocked_generic_detention_network`;<br>`unlocked_generic_labor_quota_expansion`;<br>`unlocked_generic_radicalized_atrocity_escalation`;<br>`unlocked_generic_reform_and_dismantlement`;<br>`unlocked_generic_evidence_destruction`; any focus using a hook also needs visible explanation, AI route weight, costs, and cleanup. | Shared route flags and calling focus trees. | [x] | [ ] | — | — | — |

### AI coverage and caps

| Id | Package | Required AI behavior and caps | Primary surfaces | Pending | Implemented | Queued with reason | Blocked with evidence | Rejected with reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `AI-GER` | Germany | Fascist/war/Poland activation after 1939; Auschwitz escalation after 1940 while controlling state `88`; experiment transfers rise with permission; evidence destruction only near approaching enemies and undiscovered evidence; cap by manpower/trains/war state; dismantle only on non-fascist, military review, defeat, discovery, or collapse routes. | AI strategy, decision weights, target/cap helpers. | [x] | [ ] | — | — | — |
| `AI-JAP` | Japan | China/occupation war activation; Ishii/project decisions only with relevant research/projects; Kwantung autonomy raises escalation; evidence destruction/evacuation near Soviet/Allied approach; no Germany-style or home-island route except accepted desperation gates; reform on review/defeat/outbreak. | AI strategy, decision/project weights, target/cap helpers. | [x] | [ ] | — | — | — |
| `AI-SOV` | Soviet Union | Stalinist/high-paranoia activation; quotas/deportation/grain actions respond to paranoia, war, borderland resistance, and Union Crisis; suppression relief stops scaling at high crisis; reform after de-Stalinization/reform/collapse/famine; cap extreme escalation. | AI strategy, decision weights, paranoia/Union Crisis helpers. | [x] | [ ] | — | — | — |
| `AI-UK` | U.K./Raj | Peace stable `expansion=0/reform=20`; world war low India pressure `25/5`; world war high unrest/Burma threat `45/10`; democratic postwar `0/80`; discovery/decolonization `0/100`; non-democratic high-chaos `55/5`; no normal extermination escalation/core fallback; one labor-construction mission. | AI strategy and decision/mission weights. | [x] | [ ] | — | — | — |
| `AI-USA` | U.S.A. | Peacetime `0/0/0`; war without homeland/Pacific pressure `activation=5/expansion=0/reform=10`; Pacific/homeland raids `25/10/5`; invasion/extreme chaos `40/20/5`; court review `0/0/65`; postwar/threat low `0/0/100`; no radicalized/economy route and terminate after threat. | AI strategy and decision/mission weights. | [x] | [ ] | — | — | — |
| `AI-FR` | France/Vichy | Democratic pre-collapse `expansion=0/reform=30`; Free France `0/70`; Vichy aligned/war `45/5`; Vichy high resistance/German pressure `60/0`; route change `0/90`; condemnation/enemy approach `0/60`; democratic/Free France never expand; Vichy capped below Germany scale. | AI strategy and decision/mission weights. | [x] | [ ] | — | — | — |
| `AI-ITA` | Italy | Fascist Libya low pressure `expansion=20/reform=0`; wartime/high colonial resistance `55/0`; losing North Africa `25/10`; non-fascist regime `0/85`; discovery/condemnation `0/70`; no colonial control `0/0`; limited projects, no cores, evidence destruction only near enemy. | AI strategy and decision/mission weights. | [x] | [ ] | — | — | — |
| `AI-BEL` | Belgium/Congo | Congo stable `expansion=15/reform=10`; war/exile shortage `50/0`; democratic foreign pressure `10/55`; discovery/accountability `0/90`; Congo independent `0/80`; non-democratic high chaos `65/0`; one quota and transport cycle; no extermination/core fallback. | AI strategy and decision/mission weights. | [x] | [ ] | — | — | — |
| `AI-GENERIC-FASCIST` | Generic fascist | Major war and occupied high resistance: limited activation; radicalized escalation only with route/site/war/valid-pool gates; losing war/discovery promotes evidence action or dismantlement. | AI strategy, decision weights, shared caps. | [x] | [ ] | — | — | — |
| `AI-GENERIC-COMMUNIST` | Generic communist | Internal crisis/occupation/high chaos can enable forced labor/repression; remains shallower than Soviet route; reform/collapse/route change dismantles. | AI strategy, decision weights, shared caps. | [x] | [ ] | — | — | — |
| `AI-GENERIC-DEMOCRATIC` | Generic democratic | Expansion near zero except severe emergency; inherited sites trigger legal review/dismantlement; no radicalized or abstract chem/bio escalation under ordinary democratic AI. | AI strategy, decision weights, shared caps. | [x] | [ ] | — | — | — |
| `AI-GENERIC-NEUTRAL` | Generic neutral | Avoid unless rare chaos doctrine/civil war; local detention only; dismantle after crisis; radicalized/contaminated gates remain strict. | AI strategy, decision weights, shared caps. | [x] | [ ] | — | — | — |

### Country dismantlement, discovery, and aftermath coverage

| Id | Package | Required route completion | Primary surfaces | Pending | Implemented | Queued with reason | Blocked with evidence | Rejected with reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `AFTERMATH-GER` | Germany/Directorate | Military review/closure/purge/dismantlement reduce autonomy; occupied pools remain prioritized; discovery is catastrophic; Directorate revolt transfers valid lab/site states, scales units/ideas, supports emergency responses, and retains corrupted network economy after victory. | Germany decisions/events/effects/triggers/ideas/focus/docs. | [x] | [ ] | — | — | — |
| `AFTERMATH-JAP` | Japan | Army review, containment, evidence evacuation/destruction, Ishii removal, shutdown, and postwar/Soviet/Allied exposure; owner-linked Deaths and Japan responsibility. | Japan decisions/events/effects/projects/ideas/docs. | [x] | [ ] | — | — | — |
| `AFTERMATH-SOV` | Soviet Union | Relief/reduced quotas/supply/paranoia/aid/paused deportations lower famine; high crisis caps suppression; overuse hardens successor hostility; reform/dismantlement and discovery/collapse records remain connected. | Soviet decisions/events/effects/Union Crisis/ideas/docs. | [x] | [ ] | — | — | — |
| `AFTERMATH-UK` | U.K./Raj | Freeze expansion, review, release/reclassify, compensation/conversion, unregister, replace ideas; discovery by capture, autonomy crisis, postwar review, or decolonization; Britain receives condemnation/reckoning and Raj receives autonomy/local consequences. | U.K. decisions/missions/effects/ideas/events/AI. | [x] | [ ] | — | — | — |
| `AFTERMATH-USA` | U.S.A. | Freeze expansion, court/sunset review, release/termination, unregister/remove disruption, redress, reform credit; legal/postwar/overseas/high-chaos exposure; early cleanup cheaper than forced late redress. | U.S. decisions/missions/effects/ideas/events/AI. | [x] | [ ] | — | — | — |
| `AFTERMATH-FR` | France/Vichy | Inspect/close legacy, aid survivors/refugees, dismantle North Africa, replace burdens, unregister; liberation/capture/review/tribunal discovery; responsibility remains regime-specific. | France decisions/missions/effects/ideas/events/AI. | [x] | [ ] | — | — | — |
| `AFTERMATH-ITA` | Italy | Stop projects, closure mission, convert/disband security battalions, compensate, unregister, reform credit; discovery by Allied capture/uprising/review/capitulation. | Italy decisions/missions/effects/ideas/events/AI. | [x] | [ ] | — | — | — |
| `AFTERMATH-BEL` | Belgium/Congo | Inspection, stop quota/suppression loops, reform mandate, recognize local administration, unregister/remove burdens, reform/accountability memory; exposure by capture/rebel control/inspection/decolonization/tribunal. | Belgium decisions/missions/effects/ideas/events/AI. | [x] | [ ] | — | — | — |
| `AFTERMATH-GENERIC` | Generic | Freeze expansion, close prioritized sites, pay long costs, handle local resistance/compensation, unregister, apply reformed legacy; discovery by control change/capitulation/review/visibility with bounded events. | Shared decisions/missions/effects/ideas/events/AI. | [x] | [ ] | — | — | — |

## Repression Ledger and decision-header requirements

| Id | Required UI/data item | Implementation surfaces | Pending | Implemented | Queued with reason | Blocked with evidence | Rejected with reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `GUI-001` | Required compact decision-category header/launcher with country kit, phase, reach, active pool/site counts, labor output, population-loss pressure, stability drag, resistance/subject pressure, evidence/discovery state, guard/transport burden, reform progress, country-appropriate dormant/reform substitutions, and tooltips for recent value components. | Decision category, scripted localisation, display refresh effect, GUI localisation. | [x] | [ ] | — | — | — |
| `GUI-002` | Required full `repression_ledger_window`; player-opened only, close button, country/phase header, summary strip, tabs/left navigation, selected content, bottom actions. | New/reviewed scripted GUI file; interface `.gui`; GFX; localisation. | [x] | [ ] | — | — | — |
| `GUI-003` | Visibility/cleanup: active/dormant/reform/discovery/country route/mission gates; human/open-button gate; no auto-open; close on tag/annexation; clear invalid state/tab/action; refresh on monthly pulse, actions, state control, discovery, dismantlement, regime change, and open. | Scripted GUI triggers/effects, shared cleanup helpers, on-actions. | [x] | [ ] | — | — | — |
| `GUI-004` | Tabs: Overview; State Pools; Active Sites; Country System; Discovery and Reform. | Interface layout, scripted GUI contexts, arrays, localisation/icons. | [x] | [ ] | — | — | — |
| `GUI-005` | Overview cards: `repression_ledger_reach_card`, `repression_ledger_output_card`, `repression_ledger_damage_card`, `repression_ledger_burden_card`, `repression_ledger_evidence_card`, `repression_ledger_reform_card`, each with component tooltips. | GUI/interface, scripted localisation, display variables. | [x] | [ ] | — | — | — |
| `GUI-006` | State Pools columns: state, pool type, controller, owner receiving population loss, responsible country, eligibility/block reason, burden band, available actions; severe core-fallback warning. | Bounded pool arrays, scripted localisation, GUI rows/buttons/tooltips. | [x] | [ ] | — | — | — |
| `GUI-007` | Active Sites columns: state, site type, registration, monthly loss band, labor output, resistance, evidence state, enemy proximity, action; invalid registration cleanup. | Bounded active-site arrays, GUI rows, cleanup effects. | [x] | [ ] | — | — | — |
| `GUI-008` | Country panels for Germany, Japan, Soviet Union, U.K., U.S., France/Vichy, Italy, Belgium, and generic users with all Part 6 values and route buttons; only one panel at a time. | Country display refresh, scripted GUI visibility/effects, localisation. | [x] | [ ] | — | — | — |
| `GUI-009` | Discovery/Reform cards: `repression_discovery_status_card`, `repression_condemnation_card`, `repression_deaths_card`, `repression_reform_route_card`, `repression_retreat_risk_card`; tribunal values only here. | GUI/interface, Deaths/Condemnation links, scripted localisation. | [x] | [ ] | — | — | — |
| `GUI-010` | Core display variables: `display_camp_network_reach`, `display_camp_active_site_count`, an implementation-named active eligible-pool count, `display_camp_concentration_sites`, `display_camp_radicalized_sites`, `display_camp_gulag_sites`, `display_camp_experiment_sites`, `display_camp_contaminated_evidence_sites`, `display_camp_labor_output`, `display_camp_coercive_control`, `display_camp_population_loss_pressure`, `display_camp_stability_drag`, `display_camp_resistance_pressure`, `display_camp_guard_burden`, `display_camp_rail_burden`, `display_camp_evidence_risk`, `display_camp_foreign_visibility`, `display_camp_tribunal_severity`, `display_camp_reform_pressure`, `display_camp_overstretch`. | `camp_rework_rebuild_display_values`; scripted localisation/GUI/header. | [x] | [ ] | — | — | — |
| `GUI-011` | Country display variables: `display_mengele_autonomy_band`, `display_mengele_permission_band`, `display_auschwitz_site_status`, `display_ishii_influence_band`, `display_kwantung_autonomy_band`, `display_pingfang_facility_level`, `display_outbreak_accident_risk_band`, `display_gulag_reach`, `display_paranoia_band`, `display_famine_pressure_band`, `display_union_crisis_repression_relief_band`, `display_raj_labor_burden_band`, `display_indian_autonomy_resistance_band`, `display_civil_liberties_damage_band`, `display_court_challenge_pressure_band`, `display_vichy_collaboration_reach_band`, `display_north_africa_labor_burden_band`, `display_desert_camp_burden_band`, `display_congo_extraction_pressure_band`, `display_congo_accountability_pressure_band`. | Country refresh effects, scripted localisation, GUI. | [x] | [ ] | — | — | — |
| `GUI-012` | Bands: `camp_band_none`, `camp_band_low`, `camp_band_medium`, `camp_band_high`, `camp_band_severe`, `camp_band_critical`; consistent consequence colors and no deaths-as-optimization table. | Constants, scripted localisation, GUI/GFX. | [x] | [ ] | — | — | — |
| `GUI-013` | Scripted localisation: `GetCampNetworkPhaseName`, `GetCampPoolTypeName`, `GetCampSiteTypeName`, `GetCampEvidenceBandName`, `GetCampOverstretchBandName`, `GetCampPopulationLossPressureName`, `GetCampReformRouteName`, `GetCampCountryPanelName`, `GetCampBlockedCostSummary`, `GetCampSelectedStateActionSummary`, plus header display helpers. | New/reviewed genocide-crisis scripted localisation and English localisation. | [x] | [ ] | — | — | — |
| `GUI-014` | Buttons: `camp_gui_select_state`, `camp_gui_expand_selected_pool`, `camp_gui_start_labor_project`, `camp_gui_allocate_guards`, `camp_gui_reduce_quotas`, `camp_gui_inspect_selected_site`, `camp_gui_dismantle_selected_site`, `camp_gui_destroy_evidence`, `camp_gui_country_specific_primary`, `camp_gui_close_window`; each has cost/block tooltip and decision/effect/AI equivalent. | Scripted GUI effects/triggers, shared effects, decisions, AI. | [x] | [ ] | — | — | — |
| `GUI-015` | Selected-state pattern: `camp_selected_state_id`; short-lived `camp_selected_state` event target only when useful; no persistent global target without documented cleanup. | Shared effects/triggers, GUI selection, decisions. | [x] | [ ] | — | — | — |
| `GUI-016` | Bounded arrays: `camp_gui_pool_state_ids`, `camp_gui_pool_type_ids`, `camp_gui_pool_eligibility_ids`, `camp_gui_active_site_state_ids`, `camp_gui_active_site_type_ids`, `camp_gui_active_site_evidence_ids`, `camp_gui_active_site_pressure_ids`, `camp_gui_active_site_action_ids`, `camp_gui_country_value_ids`, `camp_gui_country_value_band_ids`; never all world states. | GUI rebuild effect and scripted GUI lists. | [x] | [ ] | — | — | — |
| `GUI-017` | Rebuild order: clean invalid sites; site counts; country values; pool counts; output/burden/damage/evidence/reform; selected state; arrays; localisation. Debug raw scores/weights/pointers/constants/rolls remain development-gated and absent from ordinary UI. | Shared display/GUI effects and debug gate. | [x] | [ ] | — | — | — |
| `GUI-018` | Abstract chemical/biological controls appear only as capability/stockpile/outcome/consequence actions; no operational detail and no optimization table. | Country/generic panel buttons, decisions/effects, tooltips, Deaths link. | [x] | [ ] | — | — | — |

## Asset inventory

Final art begins only after stable sprite names, exact dimensions, and target files are registered. Every final item requires source PNG, processed PNG, final DDS, manifest, and GFX handoff. Real leaders, flags, and attested symbols are sourced; fictional UI/icons/composite alternate-history scenes may be generated; generated readable text is prohibited.

| Id | Asset requirement | Exact ids or required family | Pending | Implemented | Queued with reason | Blocked with evidence | Rejected with reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ASSET-SHARED-CATEGORY` | Category/open controls | `GFX_decision_category_repression_ledger`, `GFX_decision_open_repression_ledger`; Gulag/Mass Repression and Colonial Labor Burden category icons only if separate categories are actually implemented. | [x] | [ ] | — | — | — |
| `ASSET-SHARED-DECISIONS` | Shared decision icons | expand labor network; guard allocation; dismantle network; inspect site/tribunal; evidence destruction; emergency relief; prisoner transfer to experiment site; colonial labor quota; redress/compensation; military review; contaminated/abstract chem-bio consequence site. Stable ids must be registered before art. | [x] | [ ] | — | — | — |
| `ASSET-SHARED-IDEAS` | Shared/major-power idea icons | active forced-labor network; network overreach; democratic legitimacy damage; colonial labor burden; gulag authority; famine pressure; Ishii influence; Mengele laboratory autonomy; tribunal pressure; dismantlement reform. Stable ids must be registered before art. | [x] | [ ] | — | — | — |
| `ASSET-SHARED-REPORTS` | Report/news images | first severe discovery; Auschwitz/experiment-linked discovery; Pingfang exposure; Soviet famine crisis; colonial labor exposure; tribunal preparation. Stable ids and source mode must be recorded. | [x] | [ ] | — | — | — |
| `ASSET-UK` | U.K./Raj | `GFX_decision_uk_raj_detention`, `GFX_decision_uk_colonial_labor_works`, `GFX_idea_uk_imperial_detention_administration`, `GFX_idea_raj_colonial_labor_burden`, `GFX_report_event_raj_detention_discovery`, `GFX_news_event_colonial_reckoning`. | [x] | [ ] | — | — | — |
| `ASSET-USA` | U.S.A. | `GFX_decision_usa_emergency_relocation`, `GFX_decision_usa_court_review`, `GFX_decision_usa_redress_commission`, `GFX_idea_usa_wartime_security_authority`, `GFX_idea_usa_civil_liberties_damage`, `GFX_report_event_usa_relocation_review`. | [x] | [ ] | — | — | — |
| `ASSET-FR` | France/Vichy | `GFX_decision_fr_camp_legacy_review`, `GFX_decision_vichy_internment_admin`, `GFX_decision_fr_north_africa_labor`, `GFX_idea_fr_camp_legacy`, `GFX_idea_vichy_collaboration_repression`, `GFX_report_event_fr_liberated_camp_records`, `GFX_news_event_vichy_reckoning`. | [x] | [ ] | — | — | — |
| `ASSET-ITA` | Italy | `GFX_decision_ita_desert_camp_admin`, `GFX_decision_ita_colonial_road_labor`, `GFX_decision_ita_camp_closure`, `GFX_idea_ita_desert_camp_administration`, `GFX_idea_ita_libyan_resistance_pressure`, `GFX_report_event_libyan_camp_discovery`. | [x] | [ ] | — | — | — |
| `ASSET-BEL` | Belgium/Congo | `GFX_decision_bel_congo_concession_quota`, `GFX_decision_bel_congo_transport_corridor`, `GFX_decision_bel_colonial_inspection`, `GFX_idea_bel_congo_extraction_pressure`, `GFX_idea_congo_concession_labor_burden`, `GFX_report_event_congo_labor_discovery`, `GFX_news_event_congo_colonial_reckoning`. | [x] | [ ] | — | — | — |
| `ASSET-GENERIC` | Generic | `GFX_decision_generic_expand_labor_network`, `GFX_decision_generic_dismantle_network`, `GFX_decision_generic_destroy_evidence`, `GFX_decision_generic_guard_allocation`, `GFX_idea_generic_detention_network`, `GFX_idea_generic_overextended_repression_network`, `GFX_report_event_generic_camp_discovery`, `GFX_news_event_global_atrocity_evidence`. | [x] | [ ] | — | — | — |
| `ASSET-GUI-STATIC` | Required full ledger static UI | `GFX_repression_ledger_window_bg`, `GFX_repression_ledger_tab_overview`, `GFX_repression_ledger_tab_state_pools`, `GFX_repression_ledger_tab_sites`, `GFX_repression_ledger_tab_country`, `GFX_repression_ledger_tab_discovery`, `GFX_repression_ledger_population_pressure`, `GFX_repression_ledger_labor_output`, `GFX_repression_ledger_evidence_risk`, `GFX_repression_ledger_reform_pressure`, `GFX_repression_ledger_guard_burden`, `GFX_repression_ledger_rail_burden`; also pool/state cards, action button states, warning frame, evidence seal, reform progress frame/bar, and required static fallbacks. | [x] | [ ] | — | — | — |
| `ASSET-GUI-ANIMATED` | Optional frame animation | `GFX_repression_ledger_warning_frame` + `_static`; `GFX_repression_ledger_evidence_seal` + `_static`; `GFX_repression_ledger_reform_seal` + `_static`; `GFX_repression_ledger_selected_state_frame` + `_static`; `GFX_repression_ledger_critical_frame` + `_static`; real frame sheets/contact sheet/preview/manifest/GFX handoff required. | [ ] | [ ] | [x] Optional until the required static GUI and exact dimensions are stable. | — | — |
| `ASSET-SUPER-EVENT` | Conditional images | severe global discovery; Angel of Death Directorate revolt; Soviet famine catastrophe; Pingfang exposure; colonial reckoning. | [ ] | [ ] | [x] Created only for accepted/warranted super-events after dedicated research. | — | — |
| `ASSET-ACHIEVEMENTS` | Achievement variants | One 64x64 color icon plus grey and not-eligible variants where required for each of the ten achievement ids/concepts below. | [x] | [ ] | — | — | — |

## Achievement requirements

Each row also requires a final achievement id, tracking flags, `possible`/`happened`/disqualifier logic, localisation, color/grey/not-eligible icons as applicable, docs, and spreadsheet alignment.

| Id | Working concept | Required condition/disqualifier | Primary surfaces | Pending | Implemented | Queued with reason | Blocked with evidence | Rejected with reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ACH-01` | Inherit the Ledger, Close the Ledger | Start with dormant historical infrastructure; dismantle every active site before severe discovery/tribunal threshold. | Achievements, effects/flags, localisation, GFX, docs/workbook. | [x] | [ ] | — | — | — |
| `ACH-02` | Papers for the Liberated | Democratic major documents several severe sites before responsible capitulation; disqualify operation of an active radicalized site. | Same achievement surfaces. | [x] | [ ] | — | — | — |
| `ACH-03` | The Doctor Loses His War | Germany allows the Directorate revolt, defeats it, and dismantles every laboratory-linked site. | Same achievement surfaces plus Germany flags. | [x] | [ ] | — | — | — |
| `ACH-04` | No Pingfang Shadow | Japan removes Ishii, shuts experiment-linked sites, and prevents a major outbreak. | Same achievement surfaces plus Japan flags. | [x] | [ ] | — | — | — |
| `ACH-05` | Grain Before Fear | Soviet Union survives Union Crisis without famine reaching critical. | Same achievement surfaces plus Soviet/Union Crisis flags. | [x] | [ ] | — | — | — |
| `ACH-06` | Dominion Without Chains | U.K. keeps Raj loyal while dismantling expanded detention infrastructure. | Same achievement surfaces plus U.K./Raj flags. | [x] | [ ] | — | — | — |
| `ACH-07` | Redress Before Victory | U.S.A. terminates relocation authority and completes redress/court review before war ends. | Same achievement surfaces plus U.S. flags. | [x] | [ ] | — | — | — |
| `ACH-08` | Congo Reformed | Belgium reforms the concession labor system before international exposure. | Same achievement surfaces plus Belgium/Congo flags. | [x] | [ ] | — | — | — |
| `ACH-09` | Roads Without Camps | Italy retains Libya after dismantling colonial camps and relying on conventional garrison/infrastructure decisions. | Same achievement surfaces plus Italy/Libya flags. | [x] | [ ] | — | — | — |
| `ACH-10` | Gurs Closed | France/Free France dismantles Vichy camp legacy and prevents a tribunal-severity spike. | Same achievement surfaces plus France/Vichy flags. | [x] | [ ] | — | — | — |

## Conditional super-event requirements

These are accepted candidates, not automatic mandatory events. Each remains queued until gameplay proves its trigger is warranted and separate quote, cultural remark, button, audio, image, and source research is completed. If accepted for implementation, settings-aware playback, unique final audio unless reuse is approved, full localisation, image/audio docs, and track-list updates become mandatory.

| Id | Candidate | Trigger identifier/role | Pending | Implemented | Queued with reason | Blocked with evidence | Rejected with reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `SE-01` | Severe Global Discovery | `first_severe_radicalized_or_contaminated_discovery_high_evidence` | [ ] | [ ] | [x] Conditional candidate; requires dedicated research and gameplay trigger review. | — | — |
| `SE-02` | Angel of Death Directorate Revolt | `germany_mengele_directorate_coup_or_emergency_lab_revolt` | [ ] | [ ] | [x] Conditional candidate; existing revolt integration must be stable first. | — | — |
| `SE-03` | Soviet Famine Catastrophe | `sov_famine_critical_and_high_paranoia_or_war_or_union_crisis` | [ ] | [ ] | [x] Conditional candidate; famine balance/trigger must be validated first. | — | — |
| `SE-04` | Pingfang Exposure | `allied_or_soviet_discovery_major_japan_biowarfare_network` | [ ] | [ ] | [x] Conditional candidate; requires evidence-route and source research. | — | — |
| `SE-05` | Colonial Reckoning | `colonial_network_exposed_after_major_war_or_decolonization_or_capital_loss` | [ ] | [ ] | [x] Conditional candidate; requires route-selection and source research. | — | — |

## Localisation, documentation, manifest, and workbook ledger

| Id | Requirement | Primary surfaces | Pending | Implemented | Queued with reason | Blocked with evidence | Rejected with reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `DOC-TRACKER` | Create this source-of-truth, precedence, ownership, audit, commit, and scenario tracker without changing accepted specs or non-doc surfaces. | `docs/plans/system_camp_repression_rework_plans/source_of_truth_and_completion_tracker.md` | [ ] | [x] This document. | — | — | — |
| `LOC-DECISIONS` | Final in-world localisation for every visible category, decision, mission, cost, requirement, success/failure, show/hide control, and custom tooltip. | `localisation/english/chaosx_decisions_l_english.yml` and reviewed country files. | [x] | [ ] | — | — | — |
| `LOC-IDEAS` | Final localisation for every idea and dynamic modifier, including country/local burden and reform stages. | `chaosx_ideas_l_english.yml`, `chaosx_modifiers_l_english.yml`. | [x] | [ ] | — | — | — |
| `LOC-GUI` | Header, full ledger, tabs, cards, rows, bands, buttons, costs, block reasons, Deaths/Condemnation links, and country panels. | `chaosx_gui_l_english.yml`; scripted localisation file. | [x] | [ ] | — | — | — |
| `LOC-EVENTS` | Threshold, discovery, breakdown, reform, country-chain, achievement, and any accepted super-event text; no monthly minor-report spam. | `_chaosx_events_l_english.yml`, country event localisation, achievements/super-event localisation. | [x] | [ ] | — | — | — |
| `DOC-SYSTEM` | Update current-system documentation with mechanics, interactions, tuning sources, state pools, cleanup, AI, GUI, assets/icons and paths, future suggestions, and abstract chem/bio boundary. | `docs/systems/genocide_crisis_system.md`; related Deaths/Mengele/chemical/bio docs. | [x] | [ ] | — | — | — |
| `DOC-DYNAMIC` | Document every new reusable dynamic helper with scope, inputs/outputs/defaults/side effects/example. | `common/scripted_effects/chaosx_dynamic_effects.md` when new helpers are added there. | [x] | [ ] | — | — | — |
| `DOC-ASSETS` | Keep one manifest and GFX handoff per asset package; record source mode, source, processing, dimensions, alignment, sprite/file paths, and remaining gaps. | Asset manifests and `gfx_handoff.md` under the selected asset package folders. | [x] | [ ] | — | — | — |
| `DOC-SPECS-INDEX` | Do not edit accepted specs for ordinary progress. If the current override becomes permanent design text, parent must deliberately fold it into the source specs and update package index/manifest rather than silently rewriting history. | Accepted package README/index/specs/manifest. | [ ] | [ ] | [x] Await parent decision after implementation; this tracker currently records the override. | — | — |
| `DOC-WORKBOOK` | Update event/evolution/cluster fields only after final in-game wording and implementation facts exist; match localisation exactly and preserve workbook structure. | `docs/spreadsheets/chaos_redux_events_catalog.xlsx`. | [ ] | [ ] | [x] Sequenced after final gameplay/localisation facts. | — | — |

## File ownership map

Only one patch owner should edit a shared file in a tranche. The parent integrator reviews every handoff, resolves overlaps, wires cross-surface behavior, and owns commits and completion claims.

| Surface | Primary file(s) | Planned owner | Required handoff/evidence |
| --- | --- | --- | --- |
| Shared constants/tuning | `common/script_constants/genocide_crisis_constants.txt` | `chaosx_scripted_system_architect` or parent | Final constant groups, call sites, unsupported-field mirrors, abstract chem/bio factors. |
| Building preservation | `common/buildings/chaosx_buildings.txt`; `interface/chaosx_buildings.gfx` | Parent | Unique definitions and unchanged/migrated references. |
| Shared triggers/effects | `common/scripted_triggers/genocide_crisis_triggers.txt`; `common/scripted_effects/genocide_crisis_effects.txt` | `chaosx_scripted_system_architect` | Final helper names, inputs/outputs, array/target cleanup, Deaths/responsibility behavior. |
| Monthly/discovery hooks | `common/on_actions/genocide_crisis_on_actions.txt`; `common/on_actions/chaosx_on_actions_chaos_meter.txt` | Parent | Existing host-only path, bounded active sites, no new broad loop. |
| Shared/category decisions | `common/decisions/genocide_crisis_decisions.txt`; `common/decisions/categories/genocide_crisis_categories.txt` | Parent or bounded decision implementer; audited by `chaosx_decision_mission_auditor` | IDs, costs, missions, visibility, AI, cleanup, effect equivalents. |
| Ideas/modifiers/opinions | `common/ideas/genocide_crisis_ideas.txt`; `common/dynamic_modifiers/genocide_crisis_dynamic_modifiers.txt`; `common/opinion_modifiers/genocide_crisis_opinion_modifiers.txt` | Parent | Lifecycle ids, modifiers, responsibility-attributed reactions. |
| AI | `common/ai_strategy/genocide_crisis_ai_strategy.txt` and decision/focus weights | Parent; audited by decision/focus auditors | Country table coverage, caps, valid target proof, reform behavior. |
| Germany/Mengele | `events/germany_mengele.txt`; `germany_mengele_constants.txt`; `germany_mengele_effects.txt`; `germany_mengele_triggers.txt`; `germany_mengele_decisions.txt`; `mengele_cloning_projects.txt`; `common/national_focus/germany_mengele_clone_army.txt` | Parent | Auschwitz `88`, transfer priority, autonomy/permission, unlock, coup/victory/dismantlement evidence. |
| Japan/Ishii | Existing/shared Japan decisions, events, projects, effects, triggers, ideas | Parent | Final paths/ids, China/Manchuria pools, Ishii/project/outbreak/evidence handoff. |
| Soviet/gulag | Existing/shared Soviet decisions, events, effects, triggers, ideas, Union Crisis files | Parent | Final paths/ids, paranoia/famine/relief-cap/collapse handoff. |
| U.K./U.S./France/Italy/Belgium/generic decisions | Shared or verified country-specific decision/idea files | Parent; audited by decision and country-package auditors | Part 5 id coverage and no generic substitution. |
| Focus hooks | Verified national-focus files or accepted route flags | Parent; audited by `chaosx_focus_tree_auditor` | Exact hook ids, route visibility, AI weights, cleanup, report whether hooks or bespoke branches. |
| Full Repression Ledger | New/reviewed `common/scripted_guis/genocide_crisis_scripted_guis.txt`; `interface/genocide_crisis.gui`; related shared GUI/GFX files | Parent | Window/tabs/cards/buttons/arrays/cleanup; header parity; screenshots or equivalent state evidence. |
| Localisation/scripted localisation | English localisation files; new/reviewed `chaosx_scripted_localisation_genocide_crisis.txt` | Parent or `chaosx_localisation_auditor` | Keys changed, dynamic output parity, encoding, no debug/formula/operational prose. |
| Gameplay icons/UI art | Registered GFX paths and `gfx/` outputs | `chaosx_icon_artist` for icons; `chaosx_generated_event_art` for fictional UI/non-icon art; `chaosx_asset_source_researcher` for real material | Source/process/final bundle, manifest, contact sheet/QA, GFX handoff. Parent wires `.gfx`/`.gui`. |
| Animated GUI candidates | Frame sheets/static fallbacks/manifests | Asset agent with `chaos-redux-frame-animation` | Separate real frames, static fallback, contact sheet, preview, frame/GFX handoff. |
| Achievements | `common/achievements/chaos_redux_achievements.txt`; achievements localisation/GFX/docs | Parent plus icon artist | Ten condition/disqualifier rows, tracking flags, three icon states where required. |
| Super-events | Existing super-event scripted GUI/interface/GFX/audio/localisation/docs | Parent; text/audio/source/image specialist agents | Trigger acceptance, research, settings-aware playback, unique audio, full docs. |
| System docs/plans | `docs/systems/...`; this plan; handoffs/manifests | `chaosx_documentation_curator` | Promoted/queued/rejected/superseded/unresolved map and resume packet when needed. |
| Event catalog workbook | `docs/spreadsheets/chaos_redux_events_catalog.xlsx` | `chaosx_spreadsheet_doc_worker` after final facts | Exact in-game wording and preserved workbook structure. |
| Final completion audit | Whole feature, read-only | `chaosx_event_completion_auditor` plus focus/decision/country/localisation auditors | Spec-versus-final-repo report; parent resolves all findings before completion. |

## Audit cadence

| Gate | When | Required audit/review | Exit condition |
| --- | --- | --- | --- |
| `AUDIT-00` | Before implementation | Parent confirms precedence/override and locks first-tranche file ownership. | No unresolved design ambiguity about full GUI or abstract chem/bio boundary. |
| `AUDIT-01` | After constants/helpers/Deaths registration | Scripted-system review. | One registration path, responsibility persistence, Deaths/population path, bounded processing, cleanup documented. |
| `AUDIT-02` | After generic route/category | Decision/mission audit. | Visibility, costs, target pools, AI equivalence, reform, and popup silence verified. |
| `AUDIT-03` | After Germany/Japan/Soviet tranche | Decision, country-package, focus, and targeted completion review. | All three deep packages pass their value/pool/chain requirements without copied generic content. |
| `AUDIT-04` | After U.K./U.S./France/Italy/Belgium tranche | Decision/mission and country-package audits. | Every Part 5 id is implemented or disposed with reason; local owner/responsibility and reform routes agree. |
| `AUDIT-05` | After AI/focus hooks | Focus-tree and decision AI audits. | Country/generic caps, valid targets, route change cleanup, and hook-vs-branch reporting are complete. |
| `AUDIT-06` | After full GUI | Parent UI review plus localisation audit. | Required window, header parity, arrays, buttons, cleanup, readable values, and no optimization/operational display gaps. |
| `AUDIT-07` | After static assets/localisation | Asset manifest/GFX review and localisation audit. | Every visible sprite/key resolves; exact GUI dimensions/alignments are checked; no placeholders. |
| `AUDIT-08` | After achievements and any accepted super-event | Achievement condition review; super-event research/wiring review where applicable. | All ten achievements complete; every accepted super-event has complete research/media/settings/docs. |
| `AUDIT-09` | After docs/workbook | Documentation curator and spreadsheet worker readback. | Docs describe final mechanics; workbook matches final player-facing wording. |
| `AUDIT-FINAL` | Final repo state | Event completion audit plus unresolved findings from all specialist audits. | Every row is implemented, explicitly queued, blocked with evidence, or rejected with reason; no unreported simplification. |

## Commit tranche checklist

The parent owns commits. Each commit contains only its tranche and is created only after the corresponding audit gate has no unresolved blocking finding.

| Tranche | Commit scope | Required pre-commit proof | Status |
| --- | --- | --- | --- |
| `COMMIT-00` | This tracker only | Parent diff review; no accepted spec or non-doc change included. | Pending parent commit. |
| `COMMIT-01` | Shared constants, triggers/effects, registration, Deaths/population, discovery responsibility, cleanup | `AUDIT-01`. | Pending. |
| `COMMIT-02` | Generic route, category visibility/header data, popup-call cleanup | `AUDIT-02`. | Pending. |
| `COMMIT-03` | Germany/Mengele package | Germany scenarios and focused audit evidence. | Pending. |
| `COMMIT-04` | Japan/Ishii and Soviet/gulag/famine/Union Crisis packages | Japan/Soviet scenarios and focused audit evidence. | Pending. |
| `COMMIT-05` | U.K., U.S., France/Vichy, Italy, Belgium kits | Part 5 route-coverage table and `AUDIT-04`. | Pending. |
| `COMMIT-06` | AI caps, country target logic, focus/project/route-flag hooks | `AUDIT-05`. | Pending. |
| `COMMIT-07` | Required full Repression Ledger, header parity, scripted localisation, GUI cleanup | `AUDIT-06`. | Pending. |
| `COMMIT-08` | Final static icons/UI/report assets and complete visible localisation | `AUDIT-07`. | Pending. |
| `COMMIT-09` | Ten achievements and any individually accepted super-events | `AUDIT-08`; split super-events into separate commits if substantial. | Pending. |
| `COMMIT-10` | Final docs, manifests, workbook, completion-audit fixes | `AUDIT-09` and `AUDIT-FINAL`. | Pending. |

## Final scenario matrix

This table intentionally uses internal identifiers and expectation tokens only. It is not player-facing prose.

The checkbox state below is the frozen preimplementation snapshot. Current evidence is `ScenarioContracts=15 Failed=0` for static trace across all rows. No engine-runtime execution occurred; see `scenario_contract_validation_report.md`.

| Scenario id | Setup identifiers | Expectation identifiers | Pending | Implemented | Queued with reason | Blocked with evidence | Rejected with reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `SCN-GER-AUSCHWITZ` | `GER`; `fascist`; `year_ge_1940`; `controls_state_88`; `experiments_authorized` | `auschwitz_shared_node`; `deaths_pipeline_delta`; `real_state_population_delta`; `mengele_values_affect_pressure`; `cloning_unlock_gated` | [x] | [ ] | — | — | — |
| `SCN-GER-CORE-FALLBACK` | `GER`; `active_route`; `no_occupied_noncore_pool` | `core_fallback_selected`; `output_lower`; `stability_damage_higher`; `internal_backlash_higher` | [x] | [ ] | — | — | — |
| `SCN-JAP-OCCUPIED-CHINA` | `JAP`; `war_with_china`; `controls_china_or_manchuria_pool` | `occupied_pool_selected`; `local_owner_population_delta`; `JAP_responsibility`; `ishii_route_valid` | [x] | [ ] | — | — | — |
| `SCN-SOV-HIGH-PARANOIA` | `SOV`; `paranoia_high`; `gulag_route_active` | `gulag_expansion_valid`; `famine_pressure_delta`; `union_crisis_bridge_delta`; `suppression_relief_capped_high_crisis` | [x] | [ ] | — | — | — |
| `SCN-UK-RAJ` | `ENG`; `at_war`; `raj_or_india_pool_valid` | `raj_decisions_visible`; `ENG_limited_output`; `RAJ_burden_delta`; `autonomy_pressure_delta` | [x] | [ ] | — | — | — |
| `SCN-USA-PACIFIC` | `USA`; `at_war`; `pacific_or_homeland_threat_valid` | `relocation_authority_visible`; `court_review_valid`; `redress_valid`; `AI_expansion_rare` | [x] | [ ] | — | — | — |
| `SCN-VICHY-NORTH-AFRICA` | `VIC_or_authoritarian_FRA`; `controls_north_africa_pool` | `vichy_expansion_visible`; `north_africa_labor_valid`; `free_or_democratic_reform_valid` | [x] | [ ] | — | — | — |
| `SCN-ITA-LIBYA` | `ITA`; `fascist`; `controls_libya`; `war_or_resistance_pressure` | `roads_forts_security_valid`; `closure_valid`; `compensation_valid`; `no_italian_core_colonial_target` | [x] | [ ] | — | — | — |
| `SCN-BEL-CONGO` | `BEL`; `controls_congo`; `war_or_exile_resource_pressure` | `quota_valid`; `transport_project_valid`; `resource_or_infrastructure_delta`; `congo_burden_delta`; `accountability_delta` | [x] | [ ] | — | — | — |
| `SCN-GENERIC-OCCUPATION` | `authoritarian_generic`; `controls_high_resistance_noncore` | `generic_activation_valid`; `labor_route_valid`; `AI_cap_applied`; `no_protected_selector` | [x] | [ ] | — | — | — |
| `SCN-DISCOVERY-CONTROL` | `enemy_captures_active_site`; `stored_responsible_country_valid` | `bounded_discovery`; `condemnation_to_responsible`; `deaths_history_state_linked`; `discoverer_not_blamed` | [x] | [ ] | — | — | — |
| `SCN-DISMANTLEMENT-CLEANUP` | `regime_change`; `active_network`; `dismantlement_complete` | `active_sites_unregistered`; `ideas_converted`; `stale_decisions_hidden`; `category_hidden_when_no_work`; `selected_state_cleared` | [x] | [ ] | — | — | — |
| `SCN-NO-MONTHLY-SPAM` | `multiple_active_sites`; `monthly_pulse_elapsed` | `deaths_delta`; `variables_modifiers_delta`; `no_minor_leak_report_popup` | [x] | [ ] | — | — | — |
| `SCN-ABSTRACT-CHEM-BIO` | `valid_active_site`; `relevant_capability`; `stockpile_available`; `abstract_escalation_selected` | `deaths_scaled_by_abstract_factor`; `resistance_short_term_down`; `stockpile_logistics_consumed`; `contamination_evidence_tribunal_up`; `no_operational_detail`; `no_protected_selector` | [x] | [ ] | — | — | — |
| `SCN-FULL-LEDGER` | `human_country`; `category_visible`; `active_or_reform_route`; `open_ledger_action` | `full_window_opens`; `five_tabs_present`; `header_value_parity`; `bounded_arrays`; `button_AI_equivalence`; `cleanup_after_invalid_state`; `header_not_substitute` | [x] | [ ] | — | — | — |

## Completion gate

The archived checklist below remains the accepted completion contract, but its frozen pending boxes no longer control current status. The implementation and decision/mission audit are reconciled. Static contract trace passed all 15 scenarios; engine-runtime execution remains unperformed. Final completion therefore rests on the parent review of that explicit validation gap and the final scoped commit.

The accepted completion contract requires:

- all active-site creation/removal paths audited for exactly-once registration and stored responsibility;
- Deaths-tab and real state-population changes demonstrated for every active damage family;
- every country/generic AI route able to find a valid target in at least one scenario and unable to select invalid targets;
- every visible decision, mission, idea, GUI element, event, achievement, and accepted super-event localised and asset-complete;
- the full Repression Ledger implemented, with header parity but not header substitution;
- abstract chemical/biological/nerve-agent outcome mechanics implemented without operational recipes or protected-class selectors;
- recurring minor camp flavor events disconnected from ordinary monthly processing;
- docs/manifests/workbook aligned with final facts;
- all specialist audit findings resolved or dispositioned, and every simplification/omission reported.
