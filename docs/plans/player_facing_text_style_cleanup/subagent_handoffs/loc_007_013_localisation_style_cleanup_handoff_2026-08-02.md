# Localisation style cleanup handoff for 007–013

Scope: `localisation/english/007_random_expansion_l_english.yml`, `008_world_tension_rises_l_english.yml`, `009_white_peace_l_english.yml`, `010_death_l_english.yml`, `011_secret_alliance_l_english.yml`, every owned `012_*.yml` file, and `013_natural_disasters_l_english.yml`.

The pass used `AGENTS.md`, `.agents/skills/chaos-redux-events/SKILL.md`, the required offline Paradox wiki pages, and the vanilla localisation and script documentation. No gameplay scripts, keys, dynamic scopes, or effect values were changed.

## Changed files and keys

- `007_random_expansion_l_english.yml`: `chaosx.nr7.2.d`, `chaosx.news.7007.d`, `fury_hardened_doctrine_desc`, `fury_the_next_neighbor_desc`, `fury_no_second_fury_desc`, `fury_carry_the_orders_overseas_desc`, `chaosx.nr7.50.d`, `chaosx.nr7.51.d`, `chaosx.nr7.52.d`, `chaosx.nr7.60.d`, `chaosx.nr7.60.b`, `chaosx_super_event.59.d`, and `chaosx_super_event.60.d`.
- `008_world_tension_rises_l_english.yml`: baseline and stage descriptions, `chaosx.nr8.2.d` through `chaosx.nr8.12.d` where present, the three tension idea descriptions, the event-details body, and evolution stage 3 and 4 bodies.
- `009_white_peace_l_english.yml`: `chaosx.nr9.3.d`, `chaosx.nr9.4.d`, and `chaosx.nr9.5.d`.
- `010_death_l_english.yml`: `chaosx.nr10.2.d`, `chaosx.nr10.3.d`, `chaosx.nr10.20.d`, `chaosx.nr10.21.d`, `death_maritime_case_advice_confirmed`, `death_country_containment_category_aftermath_desc`, `death_raise_passive_hosts_desc`, `death_raise_hollow_hosts_desc`, and `death_call_living_conference_desc`.
- `011_secret_alliance_l_english.yml`: `chaosx.nr11.3.d`, `chaosx.nr11.14.d`, `chaosx.nr11.191.d`, `chaosx.nr11.193.d`, `chaosx.nr11.200.d`, `chaosx.nr11.201.d`, `secret_alliance_faction_manifest_desc`, `secret_alliance_known_enemy_plans_low_desc`, `super_event_73_desc_fractured`, all five `chaosx.scenarios.secret_alliance.desc.*` values, `secret_alliance_event_log_details_concealed`, `secret_alliance_evolution_three_body_concealed`, `secret_alliance_request_allied_consultation_desc`, and `secret_alliance_begin_limited_border_conflict_desc`.
- `012_african_union_l_english.yml`: five punctuation repairs in `africa_priority_member_natural_disaster_dynamic_cost`, `africa_record_compact_promotion_proof_desc`, `africa_promote_compact_host_desc`, `africa_decline_compact_promotion_desc`, and `africa_reopen_compact_promotion_docket_tt`.
- `012_africa_achievements_l_english.yml`: `africa_member_who_said_no_DESC` and the display value of `africa_beasts_but_not_caricatures_NAME`.
- `012_africa_event_log_l_english.yml`: package and World event-log title keys now use colon separators instead of em dashes.
- `012_africa_evolutions_l_english.yml`: `chaosx.nr12.403.d`.
- `012_africa_focus_l_english.yml`: fourteen republic, crown, Union, command, confederation, covenant, restoration, and council descriptions.
- `012_africa_priority_member_characters_l_english.yml`: `africa_priority_kongo_sovereign_desc`.
- `012_africa_priority_member_focus_l_english.yml`: `africa_priority_dynamic_overlap_aksum`.
- `012_africa_priority_member_l_english.yml`: `africa_priority_member_ratify_promoted_package_desc`, `africa_priority_manden_advance_mechanic_desc`, and `africa_priority_harar_advance_mechanic_desc`.
- `012_africa_rsa_l_english.yml`: `chaosx.nr12.1204.d`, `chaosx.nr12.1205.d`, and `africa_rsa.event_log.exile_continuation.detail`.
- `013_natural_disasters_l_english.yml`: six damage-fragment keys, three recovery keys, `chaosx_super_event.71.d`, `chaosx.nr13.126.d`, `chaosx.nr13.127.d`, `natural_disaster_chain_prevent_tsunami_desc`, `natural_disaster_cost_warning_air_tooltip`, and `natural_disaster_cost_warning_fuel_convoy_tooltip`.

## Before and after display behavior

The copy now uses direct in-world narration for Fury, World Tension, White Peace, Death, Secret Alliance, Africa, and Natural Disaster surfaces. Event detail text states the premise and consequence without exposing implementation gates or scenario setup rules. Mechanical tooltips retain their requirements, costs, dynamic scopes, and result wording where those details are necessary for a decision or scripted GUI action.

The natural-disaster damage and recovery fragments now concatenate cleanly without semicolon artifacts. Africa event-log titles use a stable colon separator. Several constitutional and focus descriptions now describe consent, representation, sovereignty, and institutional limits in concrete terms instead of staged contrast formulas.

The achievement key `africa_beasts_but_not_caricatures_NAME` now displays as `Beasts with Rights`. The key itself and its achievement mechanics are unchanged. The documentation audit found no remaining copy of the old display title in the relevant Africa specs or event docs.

## Required audit output

### Missing keys

No missing keys were found in the changed-key and owned-file checks. A complete repository-wide reference scan was not run because the all-English OneDrive tree exceeded the available command window. Parent review should still run the project’s broader localisation reference audit if one is available.

### Duplicate keys

The owned 007–013 scope contains 6,910 parsed localisation entries and zero duplicate key groups across 23 files.

### Scripted localisation issues

No scripted-localisation definition was added, removed, or renamed. No malformed custom localisation reference was found in the owned files. Dynamic actor, state, event-target, variable, colour, icon, and line-break tokens were preserved.

### Dynamic text opportunities

- Dynamic actors and state names remain present in Secret Alliance, Africa event-log, South African, Death, and Natural Disaster strings.
- The 008 event-detail and evolution bodies intentionally remain premise-focused while retaining the existing dynamic category and stage selectors.
- The 013 report and cost strings retain all dynamic state, severity, date, constant, icon, and scripted-localisation calls.
- No new dynamic helper was invented because the inspected generic lines did not expose a missing value that the owning gameplay scripts already provide.

### Cross-surface mismatch notes

- The achievement display title change should be reflected in any external achievement presentation or spreadsheet if a later audit finds one. Relevant Africa specs and event docs currently contain no old-title match.
- `secret_alliance_issue_final_private_warning`, its final-warning requirement key, and the partial-dossier tooltip still use warning terminology. This is a deliberate unresolved wording choice because the mechanics describe an actual warning and the owning decision surface may rely on that term.
- The 012 event-log World detail strings still use the older `completed the public proof` and `became the actor named` phrasing. They are stylistically serviceable but remain candidates for a later concise pass.
- Requirement and commitment labels in the long Africa action descriptions remain explicit by design. They are player-facing cost and outcome summaries, not lore prose.

### File encoding concerns

All 23 owned localisation files begin with the UTF-8 BOM bytes `EF BB BF` after the edits. Git reports its normal LF-to-CRLF working-copy warning for these OneDrive files. No non-BOM file was introduced.

## Validation

- Parsed all 23 owned files for duplicate localisation keys: zero duplicate groups.
- Compared old and current values for changed keys and checked bracketed dynamic tokens, colour markers, icon markers, and escaped line breaks: zero lost tokens across 115 changed keys.
- Scanned the owned scope for em dashes and semicolons: no remaining matches.
- Checked current BOM bytes for all owned files: all 23 passed.
- No Hearts of Iron IV process was launched, and no in-game validation was attempted per repository instructions.

## Unresolved wording and blocked refinements

OneDrive intermittently refused writes to `011_secret_alliance_l_english.yml` and `012_africa_event_log_l_english.yml` after successful patches. The following small refinements remain uncommitted in source and are listed for parent review if the lock clears:

- `secret_alliance_preempt_coalition` could be shortened from `Preempt the Coordinated Threat` to `Preempt the Coalition`.
- `secret_alliance_begin_limited_border_conflict_tt` could mirror the new positive concealment wording used by its description.
- `secret_alliance_release_partial_dossier_tt` could say `institutional awareness` instead of `institutional warning`.
- `africa.event_log.package.exile.detail` and the three World detail keys could receive the concise event-log wording described in the cross-surface notes.

No gameplay fallback or mechanical simplification was introduced. No plan handoff was needed because all identified issues were local wording, punctuation, or display-title repairs within the owned scope.
