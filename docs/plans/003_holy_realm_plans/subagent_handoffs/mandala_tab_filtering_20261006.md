# Event003 Mandala Tab Filtering Handoff - 2026-10-06

## Acceptance and scope

Parent authorized a bounded release-QA presentation change in the existing main Mandala decision category. The five tab buttons and their country flags already existed in `common/scripted_guis/003_holy_realm_scripted_guis.txt`; this change only uses those five flags to filter the existing decision list. No GUI control, category, decision id, `available` condition, cost, effect, or `ai_will_do` value was added or removed. The four hidden status-row entries remain hidden.

## Filtering API

Five country-scope scripted triggers were added to `common/scripted_triggers/003_holy_realm_triggers.txt`: `holy_realm_mandala_refuge_tab_actions_visible`, `holy_realm_mandala_arhats_tab_actions_visible`, `holy_realm_mandala_diplomacy_tab_actions_visible`, `holy_realm_mandala_doctrine_tab_actions_visible`, and `holy_realm_mandala_warnings_tab_actions_visible`.

Each trigger returns true for AI countries. For human countries, Arhats, Diplomacy, Doctrine, and Warnings require their corresponding existing tab flag. Refuge is the default when none of the other four tab flags is set; an explicit Refuge click also leaves the other four clear, so the same helper covers both states. Each main-category action now calls exactly one matching helper from its existing `visible` block while retaining its original route, stage, and target conditions.

`THR_close_refuge_roads` is the only additional route-visibility cleanup. Humans see it after the existing Bodhisattva-path unlock, or while its existing `holy_realm_memory_closed_refuge_roads` marker preserves an active timer. AI retains the old `is_holy_realm_country` and not-Buddha-path visibility through the explicit AI branch. Its availability, effects, cost, cooldown, and AI weight are unchanged.

## Action map and counts

The main category contains 51 entries: four hidden status rows and 47 decisions. The prior TIB refuge-entry source inventory had nine initial visible actions. Tab filtering partitions that baseline as Refuge 3, Arhats 2, Diplomacy 1, Doctrine 3, and Warnings 0; Refuge remains selected when no other tab flag exists. Counts are source-projected and do not claim a live-engine render.

The nine initial actions are `THR_repair_high_pass_storehouses`, `THR_open_refuge_roads`, and `THR_register_refugee_lineages` under Refuge; `THR_assign_arhat_overseers` and `THR_investigate_arhat_abuses` under Arhats; `THR_send_quiet_envoys` under Diplomacy; and `THR_choose_restraint_doctrine`, `THR_choose_peacekeeping_doctrine`, and `THR_choose_coercive_pacification` under Doctrine. Warnings has no initial action.

The full-route action-definition inventory maps to Refuge 12, Arhats 9, Diplomacy 16, Doctrine 5, and Warnings 5. This is the late-route catalog count per tab, not a claim that all 47 actions are simultaneously available in one save; existing route gates continue to determine which members can appear.

- **Refuge (12):** `THR_repair_high_pass_storehouses`, `THR_white_scarf_relief_caravans`, `THR_snow_line_signal_posts`, `THR_second_refuge_register`, `THR_open_refuge_roads`, `THR_register_refugee_lineages`, `THR_close_refuge_roads`, `THR_mandala_open_refuge_corridors`, `THR_mandala_open_granaries`, `THR_hold_dharma_teaching`, `THR_bodhisattva_mission_refuge_circuit`, and `THR_secure_outer_pass_roads`.
- **Arhats (9):** `THR_mandala_ledger_scribes`, `THR_assign_arhat_overseers`, `THR_assign_arhat_to_province`, `THR_assign_arhat_to_army`, `THR_question_false_attainment`, `THR_investigate_arhat_abuses`, `THR_arhat_road_audit`, `THR_register_outer_valleys`, and `THR_great_mandala_stabilize_registers`.
- **Diplomacy (16):** `THR_mandala_white_flag_congress`, `THR_mandala_demand_anti_puppet_clauses`, `THR_mandala_joint_defense_of_passes`, `THR_form_great_mandala`, `THR_form_silent_mandala`, `THR_great_mandala_refresh_compact_vows`, `THR_mandala_arbitration_letters`, `THR_mandala_observer_mission`, `THR_mandala_development_mission`, `THR_bodhisattva_mission_white_scarf_envoys`, `THR_bodhisattva_mission_wounded_border`, `THR_send_quiet_envoys`, `THR_mandala_border_courts`, `THR_offer_mediation_to_war_torn_state`, `THR_stand_between_armies`, and `THR_pressure_border_courts`.
- **Doctrine (5):** `THR_demand_pacification_settlement`, `THR_choose_restraint_doctrine`, `THR_choose_peacekeeping_doctrine`, `THR_choose_coercive_pacification`, and `THR_renounce_final_silence`.
- **Warnings (5):** `THR_audit_foreign_target_ledgers`, `THR_prepare_realm_shelters_for_nonreturn`, `THR_send_global_final_warning`, `THR_arm_final_silence`, and `THR_launch_final_silence`.

The map follows each decision's completion effects and route identity: refuge works, domestic shelter, and relief are Refuge; civil administration is Arhats; envoys, mediation, faction compacts, and aid abroad are Diplomacy; governance/doctrine choices are Doctrine; target audits, final notices, shelters for the final route, and launch are Warnings.

## Localisation

The five existing `holy_realm_panel_tab_*_tt` keys now explain that selecting a tab filters its action list and name the panel value or route information relevant to that tab. Tab labels and contextual body text remain unchanged.

## AI invariance evidence

Every new tab trigger returns true on `is_ai = yes`, independent of tab flags. The existing non-tab visible predicates remain byte-content-equivalent after whitespace normalization for all 47 action blocks except the specifically adjusted human route gate on `THR_close_refuge_roads`; that action's original AI-visible path is preserved explicitly. AI weights and availability/effect blocks were not edited.

The pre-change decision snapshot is `docs/plans/003_holy_realm_plans/source_snapshots/mandala_tab_filtering_20261006/003_holy_realm_decisions.txt.before`. An automated comparison of all 47 main-category decision blocks found no non-visible source changes and no missing decision ids.

Final current-source SHA-256 values are `common/decisions/003_holy_realm_decisions.txt` `95CB8C92154516359F5320FCAAC24F7F19D25BF00F60DC6FA64297A981707926`, `common/scripted_triggers/003_holy_realm_triggers.txt` `78EF4C4FB77E5BE5393E1EF1ED1D33B280B8D4CC19AE17BCBA677D49E4D91968`, and `localisation/english/003_the_holy_realm_l_english.yml` `A2AEBC312C760A4E06336ACFC4D51A60B23C8CDEA3D0E678992FEB6E8E732B23`.

## Validation and limits

One narrow `hoi4.decision_inspect` attempt for `THR_open_refuge_roads` returned `Transport closed`. No retry was made. The tab state contract was read from the existing GUI source; no GUI file was edited. The parent owns the mandatory GUI render and final visual evidence.

No scenario probability, AI weight, game balance, action cost, completion effect, or target availability claim was changed. No new global loop or effect was introduced. No commit was made.
