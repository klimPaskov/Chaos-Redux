# Event 016 D’Rhondan final country-package acceptance audit

Date: 2026-08-22

Scope: dormant fixed tag `DHR`, idempotent sovereignty formation, dynamic state transfer and claims, disconnected landing enclaves, existing-DHR joins, the three regime identities, the twelve-character roster, alien-infantry setup, country decisions and postwar integration, focus and AI wiring, assets, Event 016 log/details/news/achievement integration, and the required map/focus/event/technology/probability evidence.

Authority: `docs/specs/016_brilliant_scientist_specs/specs/016_alien_infantry_and_dhronda_addendum.md`, `docs/plans/016_brilliant_scientist_plans/016_alien_dhrondan_acceptance_scenarios.md`, the current source, and the dated country, focus, decision/mission, localisation, portrait, flag/event-art, icon, contact-chain, provider-508, unit-database, model, and improvement-loop handoffs listed below.

## Acceptance result

Country source and installed 2D package status: **conditional static acceptance**.

Overall Event 016/D’Rhondan acceptance: **blocked**. The required alien-infantry 3D package is still explicitly incomplete (`needs_user_review`) after a rifle-less Meshy 7 candidate was rejected; no accepted `alien_infantry_entity`, mesh, genuine action set, PDX reimport, or runtime sound wiring exists. Required custom probability-auditor evidence, dynamic state-transfer engine evidence, complete event rendering, and user-owned live acceptance also remain unresolved. No fallback or redesign was introduced.

The one local source correction made in this audit is narrow and behavior-preserving: `common/scripted_effects/016_dhrondan_country_effects.txt:126-130` now uses the documented `send_equipment` field `type = alien_laser_weapon_equipment_1` instead of `equipment = ...`. The destination, amount, full-stockpile transfer intent, cohort deletion behavior, and accepted max-15 force formula are unchanged.

## Required references read

- `AGENTS.md`.
- `.agents/skills/chaos-redux-subagents/SKILL.md`.
- `.agents/skills/chaos-redux-events/SKILL.md`.
- `.agents/skills/chaos-redux-focus-trees/SKILL.md`.
- `.agents/skills/chaos-redux-decisions-missions/SKILL.md`.
- `.agents/skills/chaos-redux-event-assets/SKILL.md`.
- `.agents/skills/chaos-redux-comfyui/SKILL.md`.
- Offline wiki pages: `Data structures`, `Triggers`, `Effects`, `Modifiers`, `Localisation`, `Scopes`, `On actions`, `Event modding`, `Decision modding`, `Idea modding`, `AI modding`, `Country creation`, `National focus modding`, `State modding`, `Map modding`, `Equipment modding`, `Division modding`, `Technology modding`, `Interface modding`, and `Scripted GUI modding` under `paradox_wiki/`.
- Installed vanilla documentation under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/`, including `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`, `dynamic_variables_documentation.md`, and the script-collection documents.
- Vanilla precedents for `send_equipment`, state transfer, state-targeted decisions, focus loading, locked division templates, `delete_units { disband = no }`, country history, technologies, and ordinary decision categories.
- Binding design and scenario documents: `docs/specs/016_brilliant_scientist_specs/specs/016_alien_infantry_and_dhronda_addendum.md` and `docs/plans/016_brilliant_scientist_plans/016_alien_dhrondan_acceptance_scenarios.md`.

## Files inspected

### Country and runtime

- `common/country_tags/016_dhrondan_country.txt`.
- `common/countries/Empire of D'Rhonda DHR.txt`.
- `common/countries/016_dhrondan_cosmetics.txt`.
- `history/countries/DHR - Empire of D'Rhonda.txt`.
- `history/units/016_dhrondan_dormant.txt`.
- `common/characters/016_dhrondan_characters.txt`.
- `common/country_leader/016_dhrondan_traits.txt`.
- `common/script_constants/016_dhrondan_country_constants.txt`.
- `common/scripted_triggers/016_dhrondan_country_triggers.txt`.
- `common/scripted_effects/016_dhrondan_country_effects.txt`.
- `common/scripted_localisation/016_dhrondan_country_scripted_localisation.txt`.
- `common/opinion_modifiers/016_dhrondan_opinion_modifiers.txt`.

### Focus, decisions, AI, and shared alien API

- `common/national_focus/016_dhrondan_focus_tree.txt`.
- `common/scripted_effects/016_dhrondan_focus_effects.txt`.
- `common/scripted_triggers/016_dhrondan_focus_triggers.txt`.
- `common/ai_strategy/016_dhrondan_country_strategies.txt`.
- `common/ai_strategy_plans/016_dhrondan_focus_ai.txt`.
- `common/decisions/categories/016_dhrondan_country_categories.txt`.
- `common/decisions/016_dhrondan_country_decisions.txt`.
- `common/special_projects/projects/016_dhrondan_envoy_project.txt`.
- `common/scripted_effects/016_alien_infantry_api_effects.txt`.
- `common/scripted_triggers/016_alien_infantry_api_triggers.txt`.
- `common/script_constants/016_alien_infantry_api_constants.txt`.
- `common/units/016_brilliant_scientist_project_forces.txt`.
- `common/units/equipment/016_brilliant_scientist_project_force_equipment.txt`.
- `common/technologies/016_brilliant_scientist_project_technologies.txt`.
- `common/technologies/016_brilliant_scientist_project_force_technologies.txt`.
- `common/combat_tactics.txt`.

### Event 016 integration and presentation

- `events/016_dhrondan_country_events.txt`.
- `events/016_brilliant_scientist_dhrondan_contact_events.txt`.
- `common/scripted_effects/016_brilliant_scientist_effects.txt`.
- `common/scripted_effects/chaosx_events_log_effects.txt`.
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`.
- `common/achievements/chaos_redux_achievements.txt`.
- `common/scripted_triggers/016_brilliant_scientist_achievement_triggers.txt`.
- `common/on_actions/016_brilliant_scientist_achievement_on_actions.txt`.
- `localisation/english/016_dhrondan_country_l_english.yml`.
- `localisation/english/016_dhrondan_contact_l_english.yml`.
- `localisation/english/016_dhrondan_focus_l_english.yml`.
- `localisation/english/016_alien_infantry_api_l_english.yml`.
- `localisation/english/016_brilliant_scientist_achievements_l_english.yml`.
- `interface/016_dhrondan_assets.gfx`.
- `interface/016_dhrondan_portraits.gfx`.
- `interface/016_dhrondan_focus_icons.gfx`.
- `interface/alien_infantry_system.gfx`.
- `docs/events/016_brilliant_scientist/systems/dhrondan_country.md`.
- `docs/events/016_brilliant_scientist/systems/dhrondan_contact.md`.
- `docs/events/016_brilliant_scientist/systems/alien_infantry.md`.

### Prior handoffs reviewed

- `subagent_handoffs/016_dhrondan_country_package_handoff_2026-08-21.md`.
- `subagent_handoffs/016_dhrondan_final_focus_tree_audit_2026-08-22.md`.
- `subagent_handoffs/016_dhrondan_final_decision_mission_audit_2026-08-22.md`.
- `subagent_handoffs/016_dhrondan_final_localisation_audit_2026-08-22.md`.
- `subagent_handoffs/016_dhrondan_contact_chain_handoff_2026-08-21.md`.
- `subagent_handoffs/016_dhrondan_icon_asset_completion_handoff_2026-08-21.md`.
- `subagent_handoffs/016_dhrondan_flags_event_art_handoff_2026-08-21.md`.
- `subagent_handoffs/016_dhrondan_portrait_package_handoff_2026-08-21.md`.
- `subagent_handoffs/016_alien_infantry_unit_database_handoff_2026-08-21.md`.
- `subagent_handoffs/016_alien_infantry_provider508_api_handoff_2026-08-21.md`.
- `subagent_handoffs/alien_infantry_3d_model_handoff.md`.
- `subagent_handoffs/016_alien_dhrondan_improvement_loop_closure_handoff_2026-08-22.md`.
- `subagent_handoffs/2026-08-21_dhrondan_decision_mission_audit.md`.

## Coverage checklist

| Surface | Status | Evidence and identifiers |
| --- | --- | --- |
| Fixed tag and registration | Pass | `DHR` is registered once in `common/country_tags/016_dhrondan_country.txt`; country file and history use the same tag. |
| Dormant initialization | Pass, conditional on live load | `history/countries/DHR - Empire of D'Rhonda.txt` uses bootstrap `capital = 1`, empty dormant OOB, zero research slots/stability/war support, and no active state ownership. Runtime replaces the bootstrap capital on first viable marked landing. |
| Idempotent runtime | Pass source-level | `dhrondan_initialize_country_runtime`, `dhrondan_initial_force_consumed`, `dhrondan_initial_stores_granted`, `dhrondan_country_opening_grant_consumed`, role guards, focus-tree loading, and transaction lock prevent duplicate roles, grants, template creation, and opening force. |
| State transfer/controller/core/claim/capital | Pass source-level, engine evidence blocked | `dhrondan_release_and_transfer_landing_states` and `dhrondan_transfer_current_landing_state` add DHR cores, transfer host-owned states, preserve host cores, leave third-party controllers in place when ownership changes, claim marked states not owned by DHR, and set the first viable marked capital on first release. Dynamic state IDs are deliberately API-created, not a static map list. |
| Existing-DHR join | Pass source-level | A later revolt transfers newly marked host-owned states into the existing DHR, conserves host military assets after ownership is established, reinitializes roles/focus/API safely, and skips the one-time opening force through persistent guards. |
| Disconnected enclaves | Pass source-level, engine evidence blocked | `dhrondan_flood_fill_initial_enclave_component` uses state-neighbor traversal over DHR-owned/controlled marked states outside the home area; `dhrondan_deploy_initial_cohorts` gives one cohort per discovered component before capital remainder. |
| Max-15 force formula | Pass source-level; accepted design conflict retained | `max(5, min(15, marked_states + floor(arrivals / 2)))` is implemented with a subtract-two loop and safety cap. The queued extreme case of more than 15 disconnected components remains unresolved; no sixteenth cohort was added. |
| Host division deletion and stockpile transfer | Pass after local correction | `delete_units { division_template = "D’Rhondan Landing Cohort" disband = no }` deletes without refund; `send_equipment` sends all `num_equipment@alien_laser_weapon_equipment_1` to DHR. |
| Regimes and cosmetic identities | Pass source-level | Imperial Vael IX / `DHR_IMPERIAL`, Synod Sera Qel neutrality-mapped technocracy / `DHR_SYNOD`, and Covenant Ilyr Ren democratic / `DHR_COVENANT` are installed through guarded helpers. |
| Character roster | Pass static | Exactly 12 stable IDs: 3 leaders, 5 civilian advisors, 1 high-command advisor, and 3 corps commanders. Portrait paths resolve; no opposite-gender pool or female metadata mismatch was found. |
| Flags, portraits, icons, event art | Pass static 2D | Four flag ladders (`DHR`, `DHR_IMPERIAL`, `DHR_SYNOD`, `DHR_COVENANT`) have normal/medium/small DDS files; 21 portrait texture references resolve; 88 focus DDS and 11 lifecycle idea DDS files resolve; current `016_dhrondan_assets.gfx` registers the previously missing seven country/event/decision sprites plus special-project icon. |
| 3D entity/actions/audio | Blocked | `alien_infantry_entity` is required by the addendum, but no runtime entity, mesh, seven accepted skeletal actions, PDX export/reimport, or runtime sound asset is present. `subagent_handoffs/alien_infantry_3d_model_handoff.md` records the rifle-less candidate rejection and pending user-authorized recovery. No fallback is authorized. |
| Unit/equipment/template | Pass source-level, live visual evidence blocked | `alien_infantry` is inactive and uses `sprite = alien_infantry`; the API creates the locked non-recruitable ten-battalion `D’Rhondan Landing Cohort`; each battalion consumes 200 lasers, for exactly 2,000 per cohort, with zero human manpower/equipment. |
| Technology/tactics | Conditional | `brilliant_scientist_alien_infantry_tech` unlocks `alien_laser_weapon_equipment_1`; predictive tech depends on it and enables both alien tactics. The installed tech inspection was partial and the tech render timed out; no Technology Tree Viewer acceptance claim is made. |
| Politics/parties/laws | Pass source-level | Dormant neutrality setup, provisional Imperial head, route political popularities, elections, cosmetic tags, and route leader ideologies are wired; Synod neutrality mapping is intentional. |
| Starting military/industry/supply | Conditional | Dormant OOB is empty by design. First sovereignty grants host laser stockpile plus exact initial stores, then deploys only the formula-sized cohorts. Runtime grants three research slots, bounded host baseline tech, 100 PP, 45% stability, and 55% war support once. No ordinary alien training, production-line bootstrap, trains, convoys, or extra human manpower is created. Live supply/production behavior remains user-owned. |
| Focus tree | Conditional pass | 88 focuses with required category allocation, route loading, focus-created ideas, landing-network flags, no alien normal training, and exact landing-cost references. Current inspect/render confirms 88 nodes, 102 connectors, layout hash `6f6605398964d2a7b6fa02d051bab7a888e980f816c3bc48f4f6738b10773556`, and all DHR icon assets. Seven bounded DHR layout warnings remain. |
| Decisions and missions | Conditional pass | Reclamation, enclave bridge, postwar integration, and Two-World Compact are wired with source-reviewed costs, targets, cleanup, AI gates, and localisation. No dedicated GUI belongs to these ordinary decision categories; no standard decision/GUI route is exposed in the current MCP inventory. |
| Contact/landing/crisis | Conditional pass | Existing decision/mission audit confirms 2,000 reserve, 7-day reservation, 30/24/18/12 cooldown ladder, exact refund on invalidation, 5 Pact Strain, Honor cost 75 PP/180 days, country-scoped 90-day pulse, and 10/20/40 tier weights. Custom probability owner route remains unavailable. |
| Event 016 evolution/log/details/news | Pass source-level, MCP partial | Event 016 retains exactly four logged evolutions and no cluster. The DHR sovereignty news event is `.48`; compact response chain is `.49-.52`; Event Details resolves `GetDhrondanEventDetailClause` after sovereignty. |
| Achievement | Pass source-level | Existing hidden `016_brilliant_scientist_not_from_here` accepts either authenticated multi-source history or DHR’s postwar integration plus compact route through `dhrondan_existing_achievement_route_is_complete`. No new achievement ID or fallback icon was introduced. |
| Docs/catalog/manifests | Conditional | Country, contact, focus, unit, asset, portrait, model, and acceptance documents exist and the prior catalog handoffs report workbook/CSV alignment. Model reimport and live acceptance remain open. |

## MCP evidence and exact limitations

All calls used workspace `mod_chaos_redux_ea3b2d67c2c0`.

### Country route

No `hoi4.country_*` inspection route is exposed in the installed callable tool inventory. Country behavior is therefore source-reviewed only; no source-only result is presented as engine-backed country evidence.

### Map/state route

- `hoi4.map_inspect` on `stateIds = [1]` returned `MAP_INSPECTED` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/924c2091d5426bb71b0c757e930b5d9866268771afe83ce3aa85ff16a492f1ec/6b0ac001a1828f2867955bd9727f6578595a4877f0522bc17fe9bf2e1e340574/map-inspect.8782abad4ca34d1c.json`. Static definitions, bitmap, state-region links, and network checks passed for the bounded request. Existing map-wide building-position and port-adjacency diagnostics were present and truncated; they do not identify a DHR-owned static state defect.
- The static map contains no DHR landing states because landing markers and state ownership are created dynamically by the alien-infantry API. This is expected source design, not evidence of a missing fixed state.
- `hoi4.map_render` was attempted with owner/coast/ports/supply/railway/adjacency overlays and timed out after 180 seconds. No map write was made; therefore no dry-run/apply/rollback evidence is applicable.

### Focus route

- `hoi4.focus_inspect` returned `FOCUS_INSPECTED` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/35af0eb7500c4f98febc6ca9a2f19c363d1b70b9d079cab3f53dbe777e13c319/4c0271a84d1630ac73273218083a6c227844e8cf7420dc93154e9933b342eeac/focus-inspect.2e0cd5f123a01c94.json`. It confirms 88 focuses, 102 connectors, the accepted layout hash, and current DHR icon resolution.
- `hoi4.focus_render` returned `FOCUS_RENDERED` with HTML `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7ce59e0587d9ec76bf59e6b6450ad68994231715757c168e01d6e242cb5b1fb5/4b1b283df996c37ed0f4cbb6f85f9b7d0fe6d1e906c041c19292272f84ac0a94/dhrondan_focus_tree.focus.html`, SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3311d16279d92d222a8c2e2fc3e4da643495a499ca87613a6dc1a305d26bf22e/89e7824e14aa302ed8752a96a119fcd4e15b33c78ce166e723ac6eea4c1bc4b0/dhrondan_focus_tree.focus.svg`, and JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b5df8123186d1b54ccdb48326b5c7cf6046cd7b3d535e57b0a86c25b7a00a597/2205b618cb21fc35150896cbfdfe39dd3047a7849302b9e9251f32fcd294cb41/dhrondan_focus_tree.focus.json`.
- The render marks validation false with 14 blocking focus diagnostics. The listed missing-icon errors are imported vanilla continuous-focus entries under `game:common/continuous_focus/generic.txt`, not DHR nodes. DHR-specific diagnostics are two linear-detour warnings and five same-row-spacing warnings. No focus rewrite was justified.

### Event route

- `hoi4.event_inspect` on the DHR country event file returned `EVENT_INSPECTED_PARTIAL` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3c72914915f4ceb6dce9781a96ad6c2ede625d78da7f0340c7a947308c0ea956/0263ecc66ea6f973a652c51eadfc0a4d221eea93538aff3ac92034a2741bd645/event-lint-2af1fa63424e.json`. It returned zero blocking diagnostics but deferred large-workspace helper/lifecycle projections; this is partial evidence only.
- A narrow `.48` event inspection also returned `EVENT_INSPECTED_PARTIAL` with no blocking diagnostics and a linked lint report. Both scans were workspace-heavy despite bounded selectors.
- `hoi4.event_render` for `.48` and the DHR country event file timed out after 180 seconds. No event source rewrite was made.

### Technology route

- `hoi4.tech_inspect` for `brilliant_scientist_alien_infantry_tech` returned `TECH_INSPECTED_PARTIAL` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fecb9fcbcfb0fbe874827b493e518de1ce11332da8136a62b6825a16ac3fee91/7905ede4a885944545a197b85b8b477e0ef627d0d61687fec99af00fc9d0543c/technology-trace-2d46633f1ca7.json`; the large scan reported 663 technologies, 3 unresolved nodes, and deferred helper projections.
- `hoi4.tech_render` timed out after 180 seconds. The installed package does not expose a separate accepted Technology Tree Viewer route, so the required technology-tree visual acceptance remains unresolved even though the partial tech-inspect route exists.

### Probability and AI route

- The required `chaosx_ai_probability_auditor` is not callable in this runtime (`ALL_TOOLS` contains no such custom auditor). This is a mandatory owner-routing blocker, not permission to substitute source-only evidence.
- Direct `hoi4.probability_inspect` on `common/decisions/016_dhrondan_country_decisions.txt` returned `PROBABILITY_SOURCE_DISCOVERED` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/59777d29d9142b2d705fd2c9d2b7da611f69129518439347d7817b6a53a28732/5b34994a7b7604717e40ab545a0819864b0645140af0e2521648e32933a233d1/probability-inspect-293ed1a55ed4.json`; it discovered four country decision/mission candidates and zero unresolved source inputs.
- Direct inspect on `common/ai_strategy/016_dhrondan_country_strategies.txt` returned `PROBABILITY_SOURCE_DISCOVERED` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ff9b03d85538685bdaab7fc1648c7689ad7db73dcd26558e0aeb08e6ec52e6c9/eb028d67d271b3d3c529cbcb660ba2e95d5971123ba251e70d754e13b88f4143/probability-inspect-031d04120381.json`; it correctly found no adapter-recognized weighted surfaces because the file contains `role_ratio` strategy entries rather than a supported score-race adapter.
- Focus-source probability inspection returned `INTERNAL_ERROR`; event-source probability inspection returned `INTERNAL_ERROR`; the AI-strategy adapter timed out after 180 seconds. The prior focus audit’s direct inspect/evaluate artifacts remain partial evidence only and explicitly lack the custom auditor pass.
- No probability-bearing source was changed in this audit, so no `probability_compare` was claimed. Named campaign probability acceptance remains unresolved until the custom auditor route is available.

### Decision/GUI route

No standard `hoi4.decision_inspect`, ordinary decision-category render, or dedicated DHR GUI route is exposed in the current tool inventory. The country decisions use the ordinary decisions surface and do not introduce a scripted GUI. The prior final decision/mission audit records the supported probability tier artifacts, unavailable custom auditor, and GUI limitations. No GUI rewrite or map write was made.

## Exact findings

### Fixed local issue

`common/scripted_effects/016_dhrondan_country_effects.txt:126-130` changed from:

```text
send_equipment = {
	target = DHR
	equipment = alien_laser_weapon_equipment_1
	amount = num_equipment@alien_laser_weapon_equipment_1
}
```

to:

```text
send_equipment = {
	target = DHR
	type = alien_laser_weapon_equipment_1
	amount = num_equipment@alien_laser_weapon_equipment_1
}
```

The offline effect schema and current vanilla precedents accept `type` for this transfer surface. The change does not alter the exact full-stockpile amount, destination, or no-refund division deletion.

### State and map risks

The runtime state transaction is dynamically marked by `set_state_flag = dhrondan_landing_state` in `common/scripted_effects/016_alien_infantry_api_effects.txt`, then consumed by the DHR transfer helpers. No static state ID list exists to inspect, which is correct for the accepted state-targeted landing design but prevents a bounded static map artifact from proving revolt ownership/controller/core/capital behavior. Third-party occupations are preserved by the source branch that uses `set_state_owner_to = DHR` when the host does not control the state.

The accepted max-15 versus “one cohort per disconnected component” conflict remains queued for parent/spec reconciliation in the extreme case of more than 15 components. I did not weaken the cap or add a sixteenth cohort.

### Politics, leaders, portraits, flags, advisors, and parties

The dormant tag, country file, history, cosmetic tags, leader traits, and role promotion helpers are internally consistent. The 12 characters are recruited once in dormant history and promoted/role-attached idempotently after release. Three regime leaders, five civilian advisors, one high-command advisor, and three corps commanders have distinct stable IDs, portraits, traits, and route gates. The fictional native-ImageGen portrait handoff reports no source placeholders and no RunPod use. All 21 portrait GFX texture paths resolve. The four route flag ladders and all country/event/decision GFX references resolve to current DDS files.

### Focus, decisions, ideas, and assets

The focus source has exactly 88 IDs with the required `8/24/10/12/8/8/12/6` category allocation and loads through `dhrondan_focus_tree`. Focus rewards install route flags, lifecycle ideas, landing-network gates, and no alien normal-training path. The current focus MCP render preserves all DHR icon references. The seven DHR layout warnings are bounded polish findings owned by the focus audit; imported vanilla continuous-focus missing icons are out of scope.

The four country decisions (`dhrondan_reclaim_landing_site`, `dhrondan_establish_enclave_supply_bridge`, `dhrondan_integrate_reclaimed_landing_site`, and `dhrondan_offer_two_world_compact`) have source-level targets, costs, durations, cooldowns, AI gates, postwar cleanup, and localisation. The final decision/mission audit reports no P0/P1 gameplay defect. Ordinary decision GUI evidence remains unavailable.

The 88 focus icons, 11 lifecycle icons, country decision/category icons, news/report art, special-project icon, counters, flags, and portraits are present and registered. The achievement route intentionally reuses the existing hidden Event 016 achievement ID; no new DHR-specific achievement icon is required by the current accepted route.

### Starting military, technology, industry, supply, and production

The dormant OOB is intentionally empty. On revolt, the DHR runtime inherits only the bounded host baseline technology, grants three research slots and one opening grant, transfers the host’s full laser stockpile, grants exact formula-sized stores, and materializes locked 2,000-laser cohorts through the shared API. No ordinary alien training, human manpower, ordinary equipment charge, production-line bootstrap, train, convoy, or free cohort path was found. Live stockpile/supply and production behavior remains unverified without a game run.

The public alien IDs and exact unit/equipment/tactic values match the addendum, and the predictive technology dependency is wired. The technology-tree route is only partial and has no accepted separate Technology Tree Viewer evidence.

### AI and playability

The route-specific AI strategy files and focus plans exist, with Imperial/Synod/Covenant role ratios and route focus priorities. Landing, contact, reclamation, enclave support, integration, and compact decisions have source-reviewed gates and AI values. The direct decision source inspection found four candidates, while the strategy file’s `role_ratio` entries are outside the current supported weighted adapter. The mandatory custom auditor, complete named scenario evaluation, and post-patch comparison are unavailable; no balance or normalized AI probability claim is made.

### Crisis, postwar, achievement, news, event log, and event details

The DHR sovereignty news event `.48`, compact events `.49-.52`, reclamation/integration/compact flags, achievement hook, and DHR Event Details clause are wired. Event 016’s existing evolution logging remains exactly four entries with no cluster or fifth evolution. The DHR detail clause is presentation-only and activates after `dhrondan_sovereignty_formed`; it does not create another log row. Postwar integration sets `dhrondan_postwar_integration_completed`, compact acceptance sets `dhrondan_diplomatic_compact_concluded`, and the existing achievement trigger accepts the documented DHR route.

## Changed files and identifiers

- `common/scripted_effects/016_dhrondan_country_effects.txt:126-130`: `send_equipment` key `equipment` → `type`; no tag, state, leader, party, focus, localisation, formable, AI weight, or map identifier changed.
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_dhrondan_final_country_audit_2026-08-22.md`: this handoff.
- No commit was created. The country runtime source is an existing untracked shared-worktree file; the parent must preserve/stage it together with the parent’s related DHR package changes.
- Existing unrelated worktree modifications were preserved.

## Meaningful validation completed

- Read the required repo/skills/wiki/vanilla documentation and precedents before reviewing the package.
- Reviewed the binding addendum, acceptance scenarios, current country runtime, API, focus, decision, event, localisation, asset, portrait, model, and prior audit handoffs.
- Verified the current DHR GFX asset registrations against DDS existence: 12 DHR flag DDS files, 88 focus DDS files, 11 lifecycle idea DDS files, 21 portrait texture references with zero missing paths, all country/event/decision/special-project DDS references, and both alien counter DDS files.
- Verified exactly 12 character IDs, the 3/6/3 leader-advisor/commander role split, exact 88 focus IDs, locked ten-battalion cohort structure, exact 2,000 reserve/debit, and the max-15 force formula in source.
- Ran `hoi4.map_inspect`, `hoi4.focus_inspect`, `hoi4.focus_render`, `hoi4.event_inspect`, `hoi4.tech_inspect`, and direct `hoi4.probability_inspect` routes before treating MCP results as evidence.
- Confirmed the one local transfer-key correction against offline effect documentation and current vanilla `send_equipment` precedents.

## Skipped or blocked meaningful validation

- No Hearts of Iron IV process, save, or live campaign was launched; live revolt transfer, stockpile, controller, supply, production, AI, decision, and map consumer acceptance belong to the user/parent.
- No map write was attempted; dynamic state IDs and ownership are not valid targets for a static declarative map rewrite.
- `hoi4.map_render` and `hoi4.event_render` timed out after 180 seconds.
- `hoi4.tech_render` timed out after 180 seconds; the separate Technology Tree Viewer acceptance route is not installed/available.
- The custom `chaosx_ai_probability_auditor` is absent from the callable tool inventory. Direct probability inspections are retained as bounded evidence only and are not an equivalent replacement. Focus/event probability attempts returned internal errors; strategy-factor inspection timed out.
- No `hoi4.probability_compare` was run because this audit made no weighted-source patch. A future weighted change still requires the mandatory auditor baseline/patch/compare cycle under identical named scenarios.
- No standard decision inspector or ordinary decision-category GUI route is exposed. No dedicated Event 016 DHR scripted GUI exists or needs a rewrite.
- No 3D model, audio, or fallback production was attempted. The model handoff explicitly requires user authorization for failure-driven extra Meshy spend.

## Remaining risks, simplifications, and blockers

### Blockers

1. `alien_infantry_entity` and the required rifle-bearing Meshy 7 model/action/reimport/runtime sound package remain incomplete. See `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/alien_infantry_3d_model_handoff.md` and `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/manifest.md`.
2. No callable `chaosx_ai_probability_auditor` exists, so the mandatory probability owner pass and final AI/probability acceptance are not complete.
3. Dynamic state-transfer behavior lacks country/state-flow MCP evidence because no country route is exposed and map rendering timed out.
4. Event render, technology render, and map render timed out; technology-tree visual acceptance remains unresolved.
5. User-owned live acceptance has not occurred.

### Accepted limitations and queued follow-up

- The max-15 versus every-disconnected-component extreme case remains explicitly queued; no sixteenth cohort or cap weakening was introduced.
- Two DHR linear-detour and five same-row focus-spacing warnings remain queued for bounded layout polish; no route redesign was made.
- No event-log row or cluster was added for DHR sovereignty; the design requires exactly four Event 016 evolutions and a presentation-only Event Details clause.
- Ordinary DHR decisions intentionally use the standard decision UI and do not own a scripted GUI.
- No source fallback, placeholder portrait, neutral 3D substitute, free equipment, free manpower, normal alien training, or broad balance change was introduced.

## Handoff status

This audit is complete as a source/package review and records the only local correction made. The DHR country package is conditionally accepted for static country/2D coverage, but the overall Event 016 acceptance claim must remain withheld until the listed model, probability, MCP, dynamic state-flow, and live-consumer blockers are resolved by their owning scopes.
