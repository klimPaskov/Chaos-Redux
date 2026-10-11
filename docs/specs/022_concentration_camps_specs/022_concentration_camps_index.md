# Event 22 Concentration Camps Specification Pack

This design handoff is not a current implementation or catalog-status certificate.
Acceptance requires an explicit user decision or parent acceptance under [CLAUDE.md](../../../CLAUDE.md#specs-and-plans).
Discover current tool schemas and capabilities before implementation.
`SHA256SUMS.txt` covers current local Markdown and is refreshed after each documentation audit.

## Package identity

- Event ID: `22`
- Event slug: `concentration_camps`
- Intended repository folder: `docs/specs/022_concentration_camps_specs/`
- Event type: Minor Repeatable
- Development status: To Be Reworked
- Intended cluster: Random Chaos (unregistered; see open question P-022-D)
- Event namespace: `chaosx.nr22`, with the entry event `chaosx.nr22.1`

This folder is the source design handoff for the complete Event 22 rework. It replaces the old Spain-specific concept. The event creates and develops camp networks in randomly selected countries, connects those networks to the shared Camps and Repression system, and gives every affected country a real crisis to manage.

## Design summary

A normal firing selects one eligible country and brings active concentration-camp coverage to 20 percent of that country's eligible states. Existing compatible camp buildings count toward the target. The selected country must respond through a compact decision set. It can freeze intake and close the network, place the sites under restrictive review, run them for forced labour, expand the network, conceal evidence, or, after Evolution I, convert part of the network into extermination sites.

Camp operation removes real state population and registers the exact applied loss in the Deaths system. Forced labour can provide strong short-term output, but the gains consume a finite detained workforce and create escalating deaths, resistance, sabotage, guard burdens, disease, evidence, foreign pressure, and postwar liability. Extermination sites focus on killing and terror. They do not become a stable production strategy.

The event is an entry and escalation layer. It reuses the shared camp buildings, the shared custody and monthly processor, the shared evidence and Condemnation sources, and the exact civilian-population-loss effects. It must not create a second parallel atrocity framework.

## Locked interpretations

The following points resolve ambiguities in the rough concept.
Points 1 to 4 carry the rough concept's numbers (20 percent opening, one-half conversion, the 1 percent and 2 percent shocks, 50 percent coverage) and stay unchanged.

1. The baseline 20 percent is calculated within one selected country, not across the whole world. Repeated firings spread the crisis to more countries or reactivate a former network.
2. Evolution III means that 50 percent of the selected country's eligible states contain camps in total. Those camp states are split as evenly as possible between concentration camps and extermination camps. It does not mean 100 percent state coverage.
3. Evolution II and Evolution III population percentages are one-time evolution shocks. They do not replace the continuing monthly death process of the shared camp processor.
4. When an active network progresses from Evolution II to Evolution III, its existing camp states can suffer the earlier 1 percent shock and the later additional 2 percent shock. A country whose first firing begins at Evolution III receives only the 2 percent opening shock, because the earlier in-play crisis never occurred.
5. "Genocide" is not used as a generic label for every camp death. The term applies only when the campaign establishes the required destructive intent against a qualifying protected group. Other conduct can still be mass detention, forced labour, persecution, mass killing, or crimes against humanity.
6. HOI4 does not contain a reliable ethnicity-demography model. Generic target selection therefore uses campaign markers such as occupied non-core populations, refugees, resistance detainees, ideological persecution, and country-specific historical registries. It must never invent race percentages from cores, ideology, or state ownership, and the player never receives a target menu for a protected group.
7. The rough idea's "controlled genocide" framing is rejected as a balance principle. A regime can obtain temporary coercive output or hardliner support. The design does not permit a sustainable, clean, or dominant atrocity strategy.
8. Ordinary prisoner-of-war camps and lawful civilian security internment are outside Event 22. The event requires arbitrary political detention, persecution, forced labour, extermination, or comparable abuse.
9. No rule in Event 22 reads the calendar. Dates may shift weights; the conditions the player and the campaign create decide validity (user brief, 10 October 2026, section 3.3). See the next section.

## Authority and dispositions

| Item | Disposition | Basis |
| --- | --- | --- |
| Rough concept numbers (locked interpretations 1 to 4) | accepted design | rough concept recorded by the original planning pass; unchanged by the 2026-10-10 audit |
| No rigid historical date gates; dates influence, gameplay conditions decide | accepted design, applies to this package | user brief, 10 October 2026, section 3.3 ("dates influence, gameplay conditions decide"); the package contained no calendar test and now states the rule in Part 1 |
| Part 5 plague, camp-care, migration and survivor-accounting passages | accepted | parent acceptance recorded in the 8 October review (handoffs/019_024.md, row 022) |
| Ownership by the shared camp system (monthly processor, custody, exact deaths, evidence, Condemnation) | accepted shared design, supersedes conflicting Event 22 tuning | [camp_institutional_mortality.md](../../systems/camp_institutional_mortality.md), [camp administration contract](../../../common/scripted_effects/camp_administration_effects.md) and the accepted national-administration contract in docs/plans |
| Everything else in Parts 1 to 5 and the maps | unresolved design handoff | no recorded user or parent acceptance beyond the rough concept; implementation status is none |
| 2026-10-10 consolidation proposals | proposed (spec audit 2026-10-10) | listed under Open questions; none is accepted until the parent or user accepts it |

## Current source status

- Event 22 is not implemented. `events/022_jews_massacre.txt` and `localisation/english/022_jews_massacre_l_english.yml` still hold the legacy Spain proposal under `chaosx.nr22`, and the event-name mapper still shows "Jews Massacre".
- The catalog still lists ID 22 as "Spain Antisemitism", Minor Fire-Once, To Be Reworked, with a membership in cluster 18 Military Preparation at severity High. No Random Chaos cluster exists.
- The shared camp system is implemented and under active development by a separate session (national administration, Ledger redesign, date-gate removal). Event 22 consumes its public contract and never forks it.
- Event 22 sits inside the Events 1 to 40 milestone of the 10 October 2026 brief, so this package is the implementation source for the rework.

## Shared-owner map

Event 22 registers sites and actors with these existing owners and adds no parallel rule.
Identifiers are quoted from current source; helpers marked "proposed" do not exist yet.

| Capability | Owner and identifiers | Event 22 role |
| --- | --- | --- |
| Site registration and responsibility | `camp_rework_register_active_site` with `camp_register_site_type` (`constant:camp_rework_site_type.*`); `genocide_register_concentration_site_for_root`, `genocide_register_extermination_site_for_root`, `genocide_register_gulag_site_for_root`; `genocide_build_concentration_camp_in_from_accepted`; `genocide_convert_one_concentration_camp_level`; `genocide_responsible_country` | create or activate sites for the selected country and convert sites for Evolution I and III |
| Custody, labour and recurring deaths | `camp_admin_initialize_site`, `camp_admin_admit_detainees` (needs a proven source cohort), `camp_admin_monthly_country` (28-day timer for countries in `global.camp_repression_active_countries`), `camp_admin_record_deaths` (the only physical debit; causes custody, labor, violence, institutional), `camp_admin_release_detainees`, `camp_admin_close_site`, `camp_admin_begin_reform`, `camp_admin_reform_site`, `camp_admin_reopen_site` | seed cohorts from a campaign source, request evolution shocks, close and reform; never run a private pulse |
| Policy controls | `camp_admin_mandate` (custody, coercive, radical), `camp_admin_priority` (industry, works, extraction), `camp_admin_budget` (maintenance, development, priority), site roles (custody, labor, penal, killing), `camp_admin_can_use_radical_mandate` | the opening policy sets these; there are no Event 22 assignments |
| Evidence and Condemnation | `genocide_register_hidden_condemnation_source`, `genocide_register_public_condemnation_source`, `genocide_register_hidden_coverup`, `condemnation_add_source` with `condemnation_source.atrocity` and `.coverup`, `condemnation_visibility.hidden` and `.public` | add one unique source per verified fact |
| Discovery and liberation | `genocide_try_discover_state_atrocity`, `genocide_liberate_discovered_camp`, `genocide_on_state_control_changed` | extend with Event 22 confidence steps and relief hooks |
| Legacy crisis decisions | `genocide_hide_evidence_from_foreign_observers`, `genocide_suppress_internal_reports`, `genocide_destroy_camp_evidence`, `genocide_cover_up_liberated_camps`, `genocide_deal_with_resistance_sabotage`, `genocide_handle_refugee_waves`, `genocide_manage_military_objections`, `genocide_redirect_trains_and_supplies`, `genocide_intensify_deportations` (each visible only to an AI country that has not initialized the camp administration); `genocide_build_extermination_camp`, `genocide_restricted_chemical_site_escalation`; foreign side `genocide_publicize_survivor_testimony`, `genocide_support_resistance_networks`, `genocide_prepare_tribunal_records` | reuse the effects; Event 22 adds no permanent concealment decisions and offers those choices as event options |
| Famine | `famine_adapt_camp_state` (camp deaths into famine pressure), `famine_food_stage_requires_mortality` | read the stage for the epidemic and famine incident; write nothing |
| Migration | independent migration system (living-cohort and reception contract, Part 5) | survivor movement only through its proved cohorts |
| Soviet Collapse | `camp_rework_soviet_apply_union_crisis_repression_bridge` | the Soviet adapter extends it |

## Player-facing mechanic

The routine management of an Event 22 network belongs to the shared Camps and Repression Ledger.
The Event 22 decision category carries only the choices the Ledger does not own (opening follow-up, evolution response, incident answers, liberated-site relief).
Event 22 shows two meters and one status line:

- Exposure, showing how close hidden evidence is to public verification
- Resistance Pressure, showing escape networks, sabotage, local opposition, and guard strain
- Network Reach, shown as a single line (operational sites of eligible states) and not as a meter

Reach still gates expansion and the evolutions, but no rule reads a Reach band, so the band ladder is dropped (proposal P-022-A).
The shared Condemnation value remains in the Chaos Meter and is not duplicated.
State tooltips show site type, operator, and one status; the full state ledger stays in the Ledger Locations view.

## File map

### Source specifications

- `022_concentration_camps_spec_part_1_core.md`
- `022_concentration_camps_spec_part_2_baseline_and_decisions.md`
- `022_concentration_camps_spec_part_3_evolutions_and_variants.md`
- `022_concentration_camps_spec_part_4_discovery_liberation_aftermath.md`
- `022_concentration_camps_spec_part_5_integrations_balance_presentation.md`

### Supporting matrices and handoffs

- `022_concentration_camps_event_chain_map.md`
- `022_concentration_camps_decision_map.md`
- `022_concentration_camps_ai_probability_matrix.md`
- `022_concentration_camps_achievements.md`
- `022_concentration_camps_asset_manifest.md`
- `022_concentration_camps_research_notes.md`
- `022_concentration_camps_catalog_handoff.md`
- `022_concentration_camps_acceptance_criteria.md`

### Implementation prompts

The prompts are build contracts for the first implementation.
`022_concentration_camps_goal_prompt.md` is the one current resume brief; the others are narrower templates that defer to the specs where they differ.

- `022_concentration_camps_goal_prompt.md`
- `022_concentration_camps_coding_prompt.md`
- `022_concentration_camps_decision_mission_prompt.md`
- `022_concentration_camps_asset_prompt.md`
- `022_concentration_camps_achievement_prompt.md`

## Open questions

Each item below is proposed (spec audit 2026-10-10), not accepted design, and needs parent or user acceptance before implementation.

### P-022-A. Two meters, one line

- Problem: Network Reach, Exposure and Resistance Pressure are three event-owned values with five-band ladders each, beside the shared Ledger and the Chaos Meter.
  Only Exposure and Resistance Pressure trigger distinct choices (discovery steps, escape missions).
  Reach is a count whose only rules are the expansion ceiling and the evolution targets.
- Proposal: keep Exposure and Resistance Pressure as the two meters, drop the Reach band ladder and show Reach as "sites of eligible states".
  Parts 2 and 5 keep the band text as the fallback if the parent keeps three values.
- Consequence: fewer labels to localise and tune, with no loss of a decision.
Accepted by parent 2026-10-11: Exposure and Resistance Pressure are the shared `camp_foreign_visibility` and `camp_resistance_pressure` values, and Reach is one status line.

### P-022-B. Decision and event consolidation

- Problem: the original maps hold 44 decisions, 9 missions and about 85 events, most of which restate shared camp actions (concealment, resistance, refugees, role conversion, reform) or per-state assignment micromanagement.
- Proposal: the decision map and event chain map now list the consolidated set, with a disposition table for every original working identifier.
  The count falls to 14 decisions, 7 missions and about 40 events.
- Consequence: the visible action budget (three to five, never more than six) becomes natural instead of enforced by hiding rows.
Accepted by parent 2026-10-11.

### P-022-C. Evolution shocks as clamped custody requests

- Problem: the shared contract forbids any camp death outside `camp_admin_record_deaths`, and that helper is bounded by the living custody row ledger, while the shocks are phrased as 1 percent and 2 percent of the whole state population.
- Proposal: the opening seeds each site's cohort through `camp_admin_admit_detainees` from a proven campaign source, up to the shared population-share ceiling.
  The shock is then requested as 1 or 2 percent of current state civilian population through `camp_admin_record_deaths` and recorded at the actual applied amount, so a small cohort produces a smaller shock.
  The marker is set whether the amount is zero or not.
- Open point for the camp owner: which shared cause (custody for detention sites, violence for killing-center sites) carries the shock.
- Consequence: the same people are never removed twice, and the shock cannot exceed the people the network actually holds.
Accepted by parent 2026-10-11: custody is the cause for detention sites and violence for killing sites.

### P-022-D. Random Chaos or an existing cluster

- Problem: a one-member Random Chaos cluster has no combination value.
  Domestic Unrest (cluster 16: events 1, 6, 31, 63) already covers internal instability, terrorism and civil conflict, which are Event 22's neighbours.
- Proposal: register Event 22 as a Severe member of Domestic Unrest and drop the new cluster.
  If the user keeps Random Chaos as a design decision, the catalog handoff already specifies how to register it.
Accepted by parent 2026-10-11: Event 22 is a Severe member of Domestic Unrest (cluster 16) and no new cluster is created.

### P-022-E. Achievement overlap

- Problem: "No Second Operator" and "Names Restored" duplicate the shared achievements 000_chaos_redux_60_inherit_the_ledger_close_the_ledger and 000_chaos_redux_61_papers_for_the_liberated.
- Proposal: drop those two and "From Camps to Care", extend the shared conditions where needed, and keep eight Event 22 achievements.
Accepted by parent 2026-10-11.

### P-022-F. Air cleanliness link

- Problem: Part 5 asks camps to read air cleanliness, but the air contamination ledger has no camp footprint and no state-level cleanliness value.
- Proposal: do not add a camp footprint.
  The camp epidemic incident may read the existing global air contamination level as one weight, with no new value.
Accepted by parent 2026-10-11: the epidemic incident reads global air contamination as one weight at most.

## Changelog

- 2026-10-10 spec audit (Pass 1 and Pass 2).
  - Index rewritten around authority and dispositions, current source status, the shared-owner map and open questions; the package identity names the real namespace `chaosx.nr22`.
  - Added the 3.3 rule (dates influence, conditions decide) to the locked interpretations and to Part 1.
  - Parts 2, 3 and 5 no longer define a private operation pulse, detained-capacity table, mortality bands, assignment effects or national caps; they point to the shared camp processor, custody ledger and constants, whose values disagree with the old tables by one to two orders of magnitude.
  - Per-state forced-labour assignments and intensity are replaced by the shared national mandate, economic priority and budget.
  - The extermination "target purpose" is derived from campaign facts and no longer a player menu, matching the shared package's rule that no protected-group selector exists.
  - Decision map, event chain map, AI matrix, acceptance criteria, catalog handoff, asset manifest and achievements aligned with the consolidated set; prompts condensed into one resume brief plus marked templates.
  - Stale links fixed: `AGENTS.md` to `CLAUDE.md`, `.agents/skills/` to `.claude/skills/`, ImageGen wording to the MCP image-generation workflow, `fork_turns` wording to context-complete subagent prompts.
  - Added proposals P-022-A to P-022-F under Open questions.
  - Superseded wording (the original 44-decision list, the 85-event list and the private tuning tables) was condensed to its still-valid intent; git history keeps the original.

## Historical provenance (planning environment)

All supplied project Markdown files, TOML files, CSV exports, spreadsheet skill files, and every subagent TOML contained in `subagents.zip` were read before this package was completed.

The custom Chaos Redux subagent runtime and the HOI4 MCP inspection tools were not available in that planning environment. No subagent execution or live MCP proof is claimed. Their prompts and audit requirements are incorporated into the implementation handoffs. The implementation remains responsible for the required probability, event, decision, asset, localisation, spreadsheet, completion, and improvement-loop passes.

### Supplied project files

The planning pass read these supplied sources in full:

- `AGENTS(7).md`
- `CHAOS_REDUX_MECHANICS(7).md`
- `chaos-redux-3d-model-pipeline(3).md`
- `chaos-redux-comfyui(2).md`
- `chaos-redux-debug-playtest(2).md`
- `chaos-redux-decisions-missions(3).md`
- `chaos-redux-event-assets(7).md`
- `chaos-redux-event-planning(20260813-152954).md`
- `chaos-redux-events(8).md`
- `chaos-redux-focus-trees(3).md`
- `chaos-redux-frame-animation(8).md`
- `chaos-redux-improvement-loop(8).md`
- `chaos-redux-subagents(8).md`
- `chaos-redux-super-events(7).md`
- `chaosx_dynamic_effects.md`
- `chaosx_dynamic_triggers.md`
- `config.toml`
- `chaos_redux_events_catalog(3).csv`
- `chaos_redux_clusters_catalog(3).csv`
- `chaos_redux_scenarios_catalog(3).csv`

The spreadsheet skill and its API quick-start reference were also read because the final implementation must update the authoritative XLSX and regenerate its CSV exports.

### Subagent files inside `subagents.zip`

The planning pass extracted and read all 20 supplied subagent definitions:

- `chaosx_3d_model_pipeline.toml`
- `chaosx_ai_probability_auditor.toml`
- `chaosx_asset_source_researcher.toml`
- `chaosx_country_package_auditor.toml`
- `chaosx_decision_mission_auditor.toml`
- `chaosx_documentation_curator.toml`
- `chaosx_event_completion_auditor.toml`
- `chaosx_event_ui_worker.toml`
- `chaosx_focus_tree_auditor.toml`
- `chaosx_generated_event_art.toml`
- `chaosx_icon_artist.toml`
- `chaosx_improvement_loop_planner.toml`
- `chaosx_localisation_auditor.toml`
- `chaosx_portrait_creator.toml`
- `chaosx_repo_explorer.toml`
- `chaosx_scripted_system_architect.toml`
- `chaosx_skill_maintainer.toml`
- `chaosx_spreadsheet_doc_worker.toml`
- `chaosx_super_event_audio_researcher.toml`
- `chaosx_super_event_text_researcher.toml`

The specifications use the relevant ownership and handoff rules from these definitions. No subagent execution is claimed in the planning environment.
- 2026-10-10 spec audit: pass 2 incomplete. The decision map, event chain map and parts 2, 3 and 5 were condensed; the unchanged files were not re-read.
