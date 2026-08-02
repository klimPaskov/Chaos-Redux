# Localisation style cleanup handoff for Events 014 through 017

Date: 2026-08-02

Agent scope: `localisation/english` files whose names begin with `014_`, `015_`, `016_`, or `017_`.

This pass changed player-facing prose only and preserved localisation keys, dynamic tokens, colour markup, event slots, route meaning, and gameplay effects.

## Required references

- `AGENTS.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline Paradox wiki pages for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding.
- Vanilla documentation for localisation formatting, localisation objects, dynamic variables, and script concepts.
- Event 014 source alignment plan at `docs/plans/014_cannibalism_plans/014_super_event_text_research.md`.
- Existing Event 014 and Event 017 localisation audit handoffs for secrecy and hidden-event handling.

## Files changed and keys

### Event 014

`localisation/english/014_cannibalism_l_english.yml` changed these keys:

- `chaosx.nr14.2.d`, `chaosx.nr14.20.d`, `chaosx.nr14.61.d`, `chaosx.nr14.70.d`, `chaosx.nr14.72.d`, `chaosx.nr14.76.a`
- `chaosx.events_log.window.event_details.cannibalism.pre_reveal`
- `cannibalism_raise_network_cadre_desc`, `cannibalism_humane_route_screening_effect_tt`, `cannibalism_submit_surrender_warband_effect_tt`
- `cannibalism_warlord_secure_the_first_larder_desc`, `cannibalism_warlord_council_of_hosts_desc`, `cannibalism_warlord_mobile_larder_desc`, `cannibalism_warlord_raid_the_neighboring_states_desc`
- `CBL_take_their_heirs_desc`, `CBL_preserve_the_working_herds_desc`, `CBL_interdiction_markers_desc`, `CBL_host_theaters_without_borders_desc`, `CBL_measure_world_hostility_desc`
- `cannibalism_international_response_category_desc`, `cannibalism_break_wendigo_terminal_hunt_desc`
- `chaosx_super_event.49.d`, `chaosx_super_event.52.d`

The slot 49 and slot 52 descriptions now match the selected wording in `docs/plans/014_cannibalism_plans/014_super_event_text_research.md`.

### Event 015

`localisation/english/015_utopia_manifesto_l_english.yml` changed `utopia_manifesto_ledger_gui_callings_left` and `utopia_manifesto_ledger_gui_callings_right` by replacing em-dash label separators and a semicolon with readable punctuation while keeping all metrics and scripted getters.

`localisation/english/015_utopia_manifesto_decision_completion_l_english.yml` changed `utopia_manifesto_league_category_desc`, `decision_utopia_send_surplus_abroad_desc`, `decision_utopia_prove_league_not_mask_desc`, `decision_utopia_end_the_auxiliary_contract_desc`, and `decision_utopia_publish_corrected_tenure_tables_desc`.

`localisation/english/015_utopia_manifesto_events_l_english.yml` changed `chaosx.nr15.55.d`, `chaosx.nr15.121.d`, `chaosx.nr15.161.d`, `chaosx.nr15.206.d`, and `chaosx.nr15.207.d`.

`localisation/english/015_utopia_manifesto_evolution_consumption_l_english.yml` changed `decision_utopia_stock_bounded_self_sufficiency_desc`.

`localisation/english/015_utopia_manifesto_focus_l_english.yml` changed `utopia_manifesto_the_coastal_refuge_desc`.

`localisation/english/015_utopia_manifesto_country_package_l_english.yml` changed `utopia_manifesto_trait_civic_engineer_desc`.

### Event 016

`localisation/english/016_brilliant_scientist_achievements_l_english.yml` changed `brilliant_scientist_publish_conclusive_provenance_dossier_desc`.

`localisation/english/016_brilliant_scientist_aftermath_l_english.yml` changed `chaosx.nr16.302.d`, `chaosx.nr16.302.a`, `chaosx.nr16.310.d`, `chaosx.nr16.311.d`, and `chaosx.nr16.313.d`.

`localisation/english/016_brilliant_scientist_containment_l_english.yml` changed `chaosx.nr16.31.laboratory_uprising.d`, `chaosx.nr16.31.institutional_takeover.d`, `chaosx.nr16.31.noncountry_crisis.d`, and `brilliant_scientist_sovereignty_policy_clause_military_seizure`.

`localisation/english/016_brilliant_scientist_country_l_english.yml` changed `brilliant_scientist_exotic_guard_weaponization_tech_desc`.

The same country file contains shared-worktree advisor and country-package additions that were not authored by this pass and were left intact.

`localisation/english/016_brilliant_scientist_directorate_outcomes_l_english.yml` changed `chaosx.nr16.5.default.d`, `chaosx.nr16.5.school.d`, `chaosx.nr16.6.electronics.d`, `chaosx.nr16.6.teleportation.d`, `chaosx.nr16.6.robotics.d`, `chaosx.nr16.6.paleogenetics.d`, `chaosx.nr16.6.default.d`, `chaosx.nr16.10.transformed_personnel.d`, `chaosx.nr16.11.staff_refusal.d`, `chaosx.nr16.12.democratic.d`, `chaosx.nr16.12.communist.d`, and `chaosx.nr16.13.major.d`.

`localisation/english/016_brilliant_scientist_focus_l_english.yml` changed `KRG_a_council_of_project_commanders_desc`, `KRG_standardize_frame_repair_desc`, `KRG_the_temporal_continuum_desc`, and `KRG_a_state_without_friends_desc`.

`localisation/english/016_brilliant_scientist_foreign_l_english.yml` changed `chaosx_nr16_150_desc`, `chaosx_nr16_180_desc_continuity`, and `chaosx_nr16_194_desc_partial`, and removed the duplicate `brilliant_scientist_reaction_operation_unknown` definition.

`localisation/english/016_brilliant_scientist_kruger_state_decisions_l_english.yml` changed `KRG_continuity_network_desc`, `brilliant_scientist_krg_origin_clause_enclave`, and `chaosx.brilliant_scientist_krg.63.d`.

`localisation/english/016_brilliant_scientist_l_english.yml` changed `chaosx.nr16.2.evolution_iv.d`, `chaosx.nr16.3.evolution_iii.d`, `chaosx.nr16.15.public.d`, `chaosx.nr16.15.secret.d`, `chaosx.nr16.15.default.d`, `brilliant_scientist_news_project_army_clause_xeno`, `chaosx.nr16.16.current.d`, `chaosx.nr16.16.archived.d`, `chaosx.nr16.17.recovered.d`, and `chaosx.nr16.17.archived.d`, plus one explanatory comment comma.

`localisation/english/016_brilliant_scientist_projects_l_english.yml` changed `brilliant_scientist_select_xeno_control_researched_desc`.

The newly appearing shared-worktree file `localisation/english/016_brilliant_scientist_recovery_l_english.yml` was included in the 016 prose pass and changed only `brilliant_scientist_reconstruct_independent_research_desc`, `brilliant_scientist_secure_abandoned_archive_desc`, `brilliant_scientist_offer_amnesty_to_assistants_desc`, and `brilliant_scientist_request_international_inspection_desc`.

`localisation/english/016_brilliant_scientist_super_events_l_english.yml` changed `chaosx_super_event.92.d`, `chaosx_super_event.93.d`, `chaosx_super_event.94.d`, and `chaosx_super_event.95.d`.

### Event 017

`localisation/english/017_join_faction_l_english.yml` changed `random_faction_neutrality_exhaustion_desc` and `chaosx.events_log.window.event_details.random_faction`.

The hidden resolver and diagnostic labels for `chaosx.nr17.20` and `chaosx.nr17.81` through `chaosx.nr17.86` remain unchanged because the corresponding events are `hidden = yes` and prior Event 017 audit evidence classifies them as internal.

## Display behavior before and after

- Event 014 bodies no longer use staged “some versus others” or “not X, but Y” constructions for command reveal, surrender, route screening, and terminal-hunt outcomes. Dynamic state, route, actor, and constant tokens remain unchanged.
- Event 014 super-event slots 49 and 52 now use the researched direct descriptions while retaining the public Hannibal reveal and global-aftermath meaning.
- Event 015 GUI prose now uses colon or sentence punctuation instead of em-dash separators and a semicolon. League, aid, demobilization, tenure, and event text state the action and consequence directly.
- Event 016 descriptions now identify evidence, authority, institutional conflict, and route consequences directly. Staccato assistant factions, repeated “more than” constructions, and rhetorical “rather than” framing were reduced without changing mechanics.
- Event 016 recovery archive text now names the selected state dynamically through `[FROM.GetName]`, so the target is visible in the decision description.
- Event 017 visible neutrality and Event Details prose now states the government position and exposure risk directly. Hidden AI resolver labels remain internal.

## Audit findings

### Missing keys

No missing localisation keys were found in the scoped scripted-localisation coverage scan.

The scan covered the 12 relevant scripted-localisation files whose names begin with `014_`, `015_`, `016_`, or `017_`, plus the shared events-log, super-event, and base scripted-localisation files used by these surfaces.

One empty value remains intentionally: `brilliant_scientist_directorate_gui_ledger_hidden` is an explicit blank suppression key for a hidden ledger row.

### Duplicate keys

No exact duplicate keys remain in the 27 owned English files after excluding the repeated `l_english` headers.

The case-insensitive scan still reports the intentional pair `KRG_XENOBIOLOGICAL_ASCENDANCY` in `016_brilliant_scientist_country_l_english.yml` and `KRG_xenobiological_ascendancy` in `016_brilliant_scientist_focus_l_english.yml`. The case distinction separates a cosmetic country identity key from a focus identifier and must not be collapsed.

The duplicate `brilliant_scientist_reaction_operation_unknown` definition was removed from `016_brilliant_scientist_foreign_l_english.yml`; the surviving definition is `brilliant_scientist_reaction_operation_unknown: "an unclassified foreign operation"` in `016_brilliant_scientist_directorate_outcomes_l_english.yml`, and `common/scripted_localisation/016_brilliant_scientist_foreign_scripted_localisation.txt` resolves to it.

### Scripted-localisation issues

The scoped `localisation_key` reference scan reported zero missing outputs.

No undefined `GetCannibalism`, `GetUtopiaManifesto`, `GetBrilliantScientist`, `GetRandomFaction`, event-log, or super-event localisation result was found in the inspected call set.

No raw trigger, effect, variable, event-target, or scripted-effect syntax appears in the owned English localisation values.

### Dynamic text opportunities

Existing dynamic text already covers Event 014 actors, states, routes, costs, counterpressure, and terminal thresholds, Event 015 ledger values and route or project states, Event 016 host, recipient, facility, route, and project-family context, and Event 017 offer, leader, faction, target, cost, and timer values.

The Event 016 recovery archive description now uses `[FROM.GetName]` for the targeted former laboratory state, following the vanilla state-target decision pattern.

An optional future Event 016 flavour tranche could add the current host-country name to the `.4` and `.5` body variants, but that would be a deliberate content expansion rather than a missing-key repair.

### Cross-surface mismatch notes

- Event 014 slot 49 and slot 52 runtime descriptions now match the source recommendations in `docs/plans/014_cannibalism_plans/014_super_event_text_research.md`.
- Event 014 pre-reveal wording remains spoiler-safe and no post-reveal name was introduced into pre-reveal surfaces.
- Event 015 changes affect decision, focus, event, idea, and GUI descriptions but no event-catalog detail fields, so no workbook row or CSV export was required.
- Event 016 foreign scripted localisation now resolves one operation-unknown key. The intentional uppercase and lowercase Xenobiological Ascendancy pair remains valid.
- Event 016 country-package advisor additions present in the shared worktree have matching localisation and were not rewritten here.
- Event 017 hidden resolver and diagnostic labels remain internal, as verified against `events/017_join_faction.txt` and the prior Event 017 localisation audit.

### File encoding concerns

All 27 owned English localisation files, including the newly appearing Event 016 recovery file, begin with the required UTF-8 BOM.

No owned key uses a `:0` suffix.

No direct `§` or `£` format character was introduced in scripted localisation, and no em dash or semicolon remains in the owned English values after this pass.

### Recommended fixes

- No mandatory localisation fix remains in the audited key set.
- If the parent wants a future Event 016 flavour tranche, add the current host-country name through existing dynamic context in `chaosx.nr16.4.wartime.d`, `chaosx.nr16.4.public.d`, `chaosx.nr16.4.industrial.d`, `chaosx.nr16.4.default.d`, `chaosx.nr16.5.school.d`, `chaosx.nr16.5.security.d`, `chaosx.nr16.5.industrial.d`, and `chaosx.nr16.5.default.d` in `localisation/english/016_brilliant_scientist_directorate_outcomes_l_english.yml` rather than adding static country text.
- Keep the intentional case-sensitive Xenobiological Ascendancy pair and the blank `brilliant_scientist_directorate_gui_ledger_hidden` suppression key.
- Keep the Event 017 hidden resolver/check labels technical unless an event is made visible by a gameplay change.
- Stage the newly appearing `localisation/english/016_brilliant_scientist_recovery_l_english.yml` with its owning gameplay changes after parent review.

## Validation performed

- BOM scan across all 27 owned files returned zero missing BOMs.
- Case-sensitive duplicate-key scan returned zero exact duplicate groups.
- Scoped scripted-localisation reference scan returned `MISSING_COUNT=0`.
- Raw trigger and effect syntax scan returned zero hits.
- Targeted style scan returned zero em dashes, semicolons, `without pretending`, `not merely`, staged `Some ... Others`, `in reality`, `truth lies`, `less ... than`, or `question is not` matches.
- Event 017 hidden-event verification confirmed `hidden = yes` for the resolver and diagnostic events.
- Event 014 slot 49 and slot 52 strings were re-read against the source alignment plan after patching.
- Event 016 recovery decision names and custom effect tooltips all resolve to the new recovery localisation file, with zero missing keys.

## Skipped meaningful validation

No Hearts of Iron IV launch, live event popup, GUI render, focus render, or consumer-session test was run because live validation belongs to the parent and user.

No workbook readback or CSV export was run because this pass changed no event-catalog workbook fields.

No new gameplay mechanic or dynamic scripted helper was required, so no plan handoff for a missing mechanic was written.

## Unresolved wording decisions

- Event 016 selected super-event button remarks `No one has won.` and `Inspection begins where victory ends.` remain accepted canonical text from the existing research handoff and were not changed.
- Event 014 historical quotations remain source-controlled copy and were not modernized.
- Event 017 hidden resolver labels remain technical by design because their events are not player-facing.
- The optional Event 016 host-country flavour opportunity is queued for a future content decision and does not block this cleanup.

## Simplifications, omissions, and blockers

No gameplay meaning, route logic, cost, timer, dynamic token, secret gate, or event slot was simplified or omitted.

The only shared-worktree uncertainty is authorship of the additional Event 016 country-package advisor keys and the timing of the new Event 016 recovery file. The advisor keys were preserved, and the recovery file was copyedited only at the three requested contrast joins.

No plan handoff was written for a missing mechanic.

## Parent review path

`docs/plans/player_facing_text_style_cleanup/subagent_handoffs/loc_014_017_localisation_style_cleanup_handoff_2026-08-02.md`
