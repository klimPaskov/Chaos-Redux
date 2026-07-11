# Camp Repression Rework Improvement Addendum

Feature id: `system_camp_repression_rework`

Document type: improvement-loop closure handoff

Audit snapshot: 2026-07-11, after the bounded Repression Ledger row and array correction

Authority: the accepted package under `docs/specs/system_camp_repression_rework_specs/` remains the source design. This addendum does not replace or broaden those specs. It separates remaining accepted-package completion gates from optional ideas that are not required for the current goal.

## Closure disposition after final reconciliation

This disposition supersedes the open-state wording in section 1 while preserving that table as the dated closure plan that guided the final tranche.

- `CLOSE-01` is closed: the final inventory is 84 player actions, split 29 major, 43 colonial, and 12 generic. France refugee aid, Belgium strike negotiation, and generic site inspection are live.
- `CLOSE-02` is closed: the final decision-and-mission audit passed at 41 missions and four Ledger controls. All 32 Ledger country actions now use their native decision cooldown gates.
- `CLOSE-03` is closed at the static-contract evidence level: all 13 Part 7 scenarios plus the two cross-cutting contracts passed with `ScenarioContracts=15 Failed=0`. No engine-runtime scenario execution occurred in this environment; that validation gap is recorded in `scenario_contract_validation_report.md` and remains for the parent completion disposition.
- `CLOSE-04` is closed: runtime registration and consumer prose are reconciled. All 24 generated Ledger sprites have live consumers, including scripted visibility for evidence and reform seals.
- `CLOSE-05` is closed by the final parent review: the engine-runtime validation gap is carried explicitly, and the scoped commit is the closing repository action for this tranche.

No optional queue below was promoted. In particular, authored Ledger frame animation remains an optional enhancement rather than a completion requirement.

## Improvement-loop disposition

Broad expansion should stop.

The implemented playable promise is already substantial. A country route turns territorial reach into explicit state selection, administrative and material costs, local population loss, country Deaths responsibility, evidence and discovery pressure, reform choices, and control-sensitive dismantlement. Germany, Japan, the Soviet Union, the U.K. and Raj, the U.S.A., France and Vichy, Italy, Belgium and Congo, and generic authoritarian users each receive distinct routes, limits, aftermath behavior, and AI handling. The Repression Ledger exposes the shared loop and country-specific values without replacing the normal decision layer.

Another large action family, another country package, or another escalation tier would mostly duplicate existing choices and increase balance, localisation, and maintenance burden. At this audit snapshot, the remaining gaps were closure, evidence, and documentation tasks. They were not missing design depth.

This handoff did not claim implementation completion at the time it was written. The later closure disposition above controls current status. No protected-class selector, operational chemical or biological instruction, or broader restricted-method route is proposed here.

## 1. Archived mandatory accepted-package gaps

The table below records the earlier closure plan. Its present-tense gaps and stale-document references are historical evidence; the final disposition above supersedes them.

| Closure id | Current evidence and exact surfaces | Required closure proof |
| --- | --- | --- |
| `CLOSE-01` Live inventory and status reconciliation | The live decision inventory is 84 player actions, excluding missions and the four Ledger controls. The three last accepted actions are present as `fr_support_refugee_and_rescue_networks`, `bel_negotiate_colonial_strike_settlement`, and `generic_inspect_active_site` in `common/decisions/camp_repression_colonial_country_decisions.txt` and `common/decisions/camp_repression_generic_decisions.txt`. Their dispatcher constants, effects, localisation, icons, and AI weights are also live. `docs/plans/system_camp_repression_rework_plans/source_of_truth_and_completion_tracker.md`, `docs/plans/system_camp_repression_rework_plans/completion_report.md`, and `docs/systems/genocide_crisis_system.md` still describe an 81-action baseline and the three actions as in progress. Live-status prose also remains in `docs/specs/system_camp_repression_rework_specs/README.md`, `package_index.md`, and Parts 2, 5, and 7. | Reconcile the current-state sections to 29 major, 43 colonial, and 12 generic actions. Mark the three exact additions implemented only after the parent confirms their full surfaces. Promote the corrected Ledger requirements `GUI-006`, `GUI-007`, and `GUI-016` in the tracker. Preserve accepted design history and do not rewrite unrelated spec requirements. |
| `CLOSE-02` Final decision and mission audit | Maintained-logistics triggers, failure resolution, and control-sensitive dismantlement are present in `common/scripted_triggers/camp_repression_rework_triggers.txt`, `common/decisions/camp_repression_generic_decisions.txt`, `common/decisions/camp_repression_colonial_country_decisions.txt`, `common/scripted_effects/camp_repression_rework_effects.txt`, and `common/scripted_effects/camp_repression_colonial_country_effects.txt`. The tracker still records this audit as open. | Complete the dedicated decision and mission audit. Verify availability, target validity, maintained requirements, timeout and cancellation outcomes, AI parity, cleanup, and player-facing effects for every accepted mission family. Any finding must be corrected and re-audited before the tracker can close this gate. |
| `CLOSE-03` Part 7 scenario evidence | Every `SCN-*` row in `docs/plans/system_camp_repression_rework_plans/source_of_truth_and_completion_tracker.md` remains pending. Code readback supports the intended paths but does not replace the accepted scenario matrix. | Record task-specific evidence for every scenario listed below, including expected deltas, target validity, cleanup, popup silence, safety boundaries, and full Ledger parity. Move a row to implemented only when its full expected result has evidence. |
| `CLOSE-04` Asset handoff prose reconciliation | Runtime GFX and event wiring is live, but `docs/assets/system_camp_repression_rework/manifest_icons.md` still says all sprite registration is pending. `docs/assets/system_camp_repression_rework/gfx_handoff_icons.md` still instructs the main owner to append the registrations. `docs/assets/system_camp_repression_rework/manifest_colonial_generic_event_art.md` still says runtime wiring is pending. | Reconcile those producer handoffs with `interface/camp_repression_rework.gfx` and the live event and decision consumers. Record the exact registration files and final wired status without erasing asset provenance or production history. |
| `CLOSE-05` Final parent gate and scoped commit | Closed. The parent reviewed the combined implementation after the country-package and decision-mission audit passes. The tracker and completion report match the final runtime, assets, localisation, docs, and workbook; the absent engine-runtime scenario evidence is recorded without being overstated. | Create the final scoped commit as the closing repository action for this tranche. |

### Decision and mission identifiers that require final readback

The final audit should explicitly cover these maintained-requirement and control helpers:

- `camp_rework_generic_labor_project_requirements_met`
- `camp_rework_uk_security_line_requirements_met`
- `camp_rework_uk_military_works_requirements_met`
- `camp_rework_france_rail_project_requirements_met`
- `camp_rework_italy_road_project_requirements_met`
- `camp_rework_italy_security_sweep_requirements_met`
- `camp_rework_belgium_quota_requirements_met`
- `camp_rework_belgium_corridor_requirements_met`
- `camp_rework_state_is_actor_responsible_controlled`
- `is_valid_camp_dismantlement_state`
- `camp_rework_all_responsible_sites_currently_closable`

For the associated decision and mission blocks, the proof must distinguish successful timeout resolution from cancellation or failure resolution. Dismantlement must remain limited to sites that the responsible actor or its subject currently controls.

### Required Part 7 scenario ids

- `SCN-GER-AUSCHWITZ`
- `SCN-GER-CORE-FALLBACK`
- `SCN-JAP-OCCUPIED-CHINA`
- `SCN-SOV-HIGH-PARANOIA`
- `SCN-UK-RAJ`
- `SCN-USA-PACIFIC`
- `SCN-VICHY-NORTH-AFRICA`
- `SCN-ITA-LIBYA`
- `SCN-BEL-CONGO`
- `SCN-GENERIC-OCCUPATION`
- `SCN-DISCOVERY-CONTROL`
- `SCN-DISMANTLEMENT-CLEANUP`
- `SCN-NO-MONTHLY-SPAM`

The Part 7 matrix contains these 13 scenarios. Two additional cross-cutting
acceptance traces should be recorded alongside them because they validate
mandatory package boundaries rather than additional Part 7 rows:

- `SCN-ABSTRACT-CHEM-BIO`
- `SCN-FULL-LEDGER`

The scenario closeout must preserve two hard limits. Restricted chemical and biological behavior remains an abstract capability, stockpile, evidence, contamination, and Deaths multiplier system. State selection remains territorial, legal, political, and control-based, with no protected-class selector.

## 2. Optional future depth ideas outside the accepted package

Every item in this section is explicitly queued. None is required for completion of `system_camp_repression_rework`. None should begin before the mandatory gates above close. Promotion would require a separate accepted spec and a fresh balance, AI, localisation, asset, and cleanup contract.

| Queue id | Optional module | If promoted later |
| --- | --- | --- |
| `QUEUE-ANIM-01` | Repression Ledger state animation | Create authored frame packages for `GFX_repression_ledger_warning_frame`, `GFX_repression_ledger_evidence_seal`, `GFX_repression_ledger_reform_seal`, `GFX_repression_ledger_selected_state_frame`, and `GFX_repression_ledger_critical_frame`. Each package would need separate source frames, a contact sheet, preview, manifest, and GFX handoff. The accepted static sprites remain the final current presentation. |
| `QUEUE-ARCHIVE-01` | Postwar archive and tribunal diplomacy | After discovery or dismantlement, a responsible country could choose domestic archival custody, international evidence transfer, or controlled public release. The choice could trade reform credit, foreign condemnation, tribunal severity, and diplomatic access. AI preference would follow government, defeat status, and exposure level. |
| `QUEUE-RELIEF-01` | Rehabilitation and reparations aftermath | A bounded post-closure mission could convert administrative capacity and civilian resources into prisoner release, rehabilitation, local reconstruction, and reparations. The local owner would receive the recovery benefit while the responsible country carries the political and fiscal cost. Targeting would remain territorial and responsibility-based. |
| `QUEUE-SUCCESSOR-01` | Successor-state records and rescue-network handoff | Decolonization or regime succession could create a records claim between the former responsible authority and the local successor. Preserving records or recognizing rescue networks could improve discovery quality and lower displacement pressure, while concealment could raise later liability. This would be an aftermath module, not another repression route. |

These queues are intentionally smaller than a new country package. They deepen aftermath and presentation without adding more coercive action families. They must not introduce protected-group targeting or operational chemical and biological content.

## 3. Sufficiently deep areas with evidence

| Area | Evidence of sufficient depth |
| --- | --- |
| Shared lifecycle and accountability | `common/scripted_effects/camp_repression_rework_effects.txt` contains `camp_rework_register_active_site`, `camp_rework_unregister_inactive_site`, `camp_rework_prepare_monthly_state_death_profile`, `camp_rework_apply_monthly_state_effects`, `camp_rework_register_exact_state_deaths`, `camp_rework_apply_discovery`, `camp_rework_start_dismantlement`, and `camp_rework_complete_dismantlement`. `common/scripted_triggers/camp_repression_rework_triggers.txt` preserves responsible-country and current-control checks. The loop therefore joins state population harm, Deaths attribution, evidence, discovery, reform, and cleanup instead of presenting disconnected modifiers. |
| Player choice and country differentiation | The live inventory contains 84 player actions, split into 29 major, 43 colonial, and 12 generic actions. `common/decisions/camp_repression_major_country_decisions.txt`, `common/decisions/camp_repression_colonial_country_decisions.txt`, `common/decisions/camp_repression_generic_decisions.txt`, `common/decisions/genocide_crisis_decisions.txt`, and `common/decisions/germany_mengele_decisions.txt` provide country routes, timed projects, reform choices, evidence choices, and dismantlement. Missions and four Ledger controls are excluded from the action count. |
| Country state and focus integration | `camp_rework_refresh_colonial_focus_hooks` in `common/scripted_effects/camp_repression_colonial_country_effects.txt` maps the accepted U.K., U.S., France and Vichy, Italy, and Belgium route flags to live vanilla focuses. `common/ideas/camp_repression_major_country_ideas.txt`, `common/ideas/camp_repression_colonial_country_ideas.txt`, and `common/ideas/camp_repression_rework_ideas.txt` provide staged active, burden, reform, and aftermath lifecycles. |
| AI behavior and limits | `common/ai_strategy/genocide_crisis_ai_strategy.txt` provides active, exposed, cap-reached, reform, Japanese, and Soviet strategies. `common/script_constants/camp_repression_rework_constants.txt` centralizes route-specific AI weights. `camp_rework_country_under_ai_site_cap`, `camp_rework_country_under_ai_project_cap`, `camp_rework_country_under_ai_radicalized_cap`, `camp_rework_country_under_ai_restricted_method_cap`, and `camp_rework_soviet_under_ai_extreme_cap` prevent uncontrolled expansion. |
| Mission and dismantlement implementation | The maintained-requirement helpers listed under `CLOSE-02` are live, and project decisions use cancellation paths that resolve the relevant outcome helpers. `camp_rework_state_is_actor_responsible_controlled`, `is_valid_camp_dismantlement_state`, and `camp_rework_all_responsible_sites_currently_closable` give dismantlement a current-control contract. This is mechanically deep enough. Only the final independent audit evidence remains open. |
| Repression Ledger | The live window has Overview, State Pools, Active Sites, Country System, and Discovery and Reform tabs. `common/scripted_effects/camp_repression_rework_effects.txt` builds the exact bounded `camp_gui_pool_*`, `camp_gui_active_site_*`, and `camp_gui_country_value_*` arrays. `common/scripted_guis/camp_repression_ledger_scripted_gui.txt` provides six pool and six site selection and visibility gates, with pool rows consuming `camp_gui_pool_states` and site rows consuming `camp_gui_active_site_states`. `interface/camp_repression_ledger.gui` consumes six rows for each list. `localisation/english/camp_repression_rework_l_english.yml` uses the same bounded GUI arrays and exposes controller, population owner, responsibility, eligibility, burden, registration, population loss, labor output, resistance, evidence, enemy proximity, and available action columns. The legacy `camp_ledger_site_states` array remains compatibility data in the rebuild effect, not the active GUI row source. |
| Presentation and campaign milestones | `interface/camp_repression_rework.gfx` registers the Ledger, decision, report, and news assets. Super-event slots `12`, `74`, `75`, `76`, and `77` use audio ids `45`, `44`, `46`, `47`, and `48`. `common/achievements/chaos_redux_achievements.txt` and `interface/chaosx_achievements.gfx` provide achievements `60` through `69` with normal, grey, and not-eligible variants. The accepted static presentation is complete enough for closure. |
| Safety and scope discipline | `camp_rework_country_can_use_restricted_method_route` limits restricted methods to explicit route authority, and the state capability triggers require valid active sites and matching stockpiles. Territorial pool triggers use control, occupation, colonial, subject, core, resistance, crisis, and route state. The trigger file explicitly excludes protected-class selectors. No broader or more operational version is needed. |

## Stop recommendation and handoff

Do not create another improvement addendum for this package unless a final auditor discovers a genuinely new design gap that is not covered by the accepted specs or this closure handoff.

The main implementation should finish the existing plan in this order:

1. Resolve every final package auditor finding.
2. Close the decision and mission readback.
3. Record all Part 7 scenario evidence.
4. Reconcile live inventory, GUI status, asset handoffs, system documentation, tracker, and completion report.
5. Review the final scoped diff and create the required plan commit.

No broad expansion is recommended. No unapproved simplification was identified by this improvement-loop audit. The current package should move toward validation and closure, not another mechanic tranche.
