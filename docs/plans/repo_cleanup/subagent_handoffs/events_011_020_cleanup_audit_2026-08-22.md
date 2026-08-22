# Events 011–020 repository-cleanup audit

Date: 2026-08-22

Mode: read-only audit; no gameplay, localisation, interface, GUI, asset, spreadsheet, or shared-system source was modified.

## Scope and verdict

This audit covers Event roots `chaosx.nr11.1` through `chaosx.nr20.1`, the Event 020 weaponization chain `chaosx_nr20_weaponization.1`, event-owned decisions, focuses, ideas, on-actions, helpers, localisation, documentation, catalog rows, and the shared settings/event-log systems they call.

Events 021 and later were not inspected except where an exact shared-infrastructure reference was needed to determine whether an Event 011–020 identifier was live.

The repository is not ready for a blanket Events 011–020 cleanup-complete claim.

The audit found four high-confidence bounded patch groups: restore Event 013 in two shared name selectors, prune two proven-dead Event 020 helper families, centralize four Event 020 weighted literals without changing their values, and replace three player-facing implementation-jargon strings.

A larger Event 016 orphan/reserved-helper family requires explicit plan disposition before deletion.

Documentation and reproducibility claims for seven event asset workspaces do not match the current tree, while Events 016, 018, and 020 already retain explicit completion blockers.

No `interface/*.gui` visual layout or coordinate change is recommended.

## Evidence boundary

The audit read `AGENTS.md`, the repository-cleanup master prompt, and the complete `chaos-redux-events`, `chaos-redux-subagents`, `chaos-redux-improvement-loop`, `chaos-redux-event-planning`, `chaos-redux-decisions-missions`, `chaos-redux-focus-trees`, and `xlsx` skills.

The required offline wiki pages were consulted for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, and National focus modding.

Installed vanilla documentation was consulted for script concepts/constants, effects, triggers, modifiers, and on-action behavior.

Vanilla precedents included the Poland event chain, vanilla targeted decisions including the African Union decision family, and installed `00_on_actions.txt` registrations.

The event catalog was inspected from `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, the sole editable source; exported CSV files were not used as authority and were not edited.

`interface/*.gui`, GUI assets, and `common/scripted_guis` were inspection-only references.

Functional selector, content, toggle, and binding defects remain in scope, but visual layout and coordinate changes are outside this audit and are not recommended.

The worktree contained concurrent edits owned by other agents.

All findings below were rechecked against the current working tree immediately before this report was written.

## Completion status by event

| Event | Current source/completion status | Cleanup disposition | MCP evidence status |
|---|---|---|---|
| 011 Secret Alliance | Gameplay and shared-log integration are materially implemented according to the current completion handoff, but the documented durable asset archive is absent. | No confirmed gameplay deletion; reconcile or restore the missing asset/provenance workspace. | Root inspect produced a partial trace; root render timed out; weighted option inspect succeeded but returned an incomplete 45-candidate pool. |
| 012 Africa Is One | Current docs call this a release candidate with source certification complete for counted surfaces, while owner decisions and evidence/future-pool boundaries remain. | Preserve deliberate dormant world packages and save aliases; clean player-facing catalog prose separately. | Root inspect produced a partial trace; root render timed out; four event-option source inspections succeeded with incomplete pools and three world-package inspections timed out. |
| 013 Natural Disasters | Static completion evidence is extensive, but Event 013 is missing from two live shared settings name selectors, the claimed restored asset archive is absent, and catalog status lacks a documented promotion from the audit's `Needs Testing` boundary. | One safe selector patch; asset/status reconciliation required; do not infer a balance change from repeated cluster membership. | Root inspect and render timed out; probability inspect timed out and decision inspection ended with `Transport closed`. |
| 014 Cannibalism | Prior source audits report the gameplay package as implemented; the currently claimed `docs/assets/014_cannibalism/` icon/manifests workspace is absent, although a separate portrait-replacement archive exists. | Preserve meta-effect-dispatched helper families; reconcile the missing general asset archive. | Root inspect returned `INTERNAL_ERROR / Unexpected internal error`; root render timed out; probability transport was unavailable before this event could be inspected. |
| 015 Utopia Manifesto | Current source-of-truth docs present the event as implemented, but the referenced manifest, visual index, validators, and production archive under `docs/assets/015_utopia_manifesto/` are absent. | No confirmed gameplay cleanup defect; restore or explicitly supersede the absent evidence paths. | Root inspect and render timed out; probability transport was unavailable before this event could be inspected. |
| 016 Brilliant Scientist | Explicitly partial: the README leaves targeted transfer, cleanup, probability, balance, Event 019 isolation, and presentation validation open, with further 3D packages queued or rejected. | Resolve a substantial definition-only helper family and clean two player-facing character-token strings; do not mass-delete until accepted-plan ownership is dispositioned. | Root inspect and render timed out; one evolution option inspection succeeded with an incomplete 18-candidate pool, while other probability inspections returned internal errors. |
| 017 A Faction Comes Calling | Gameplay audits report a passing package, but the entire documented asset workspace and its named processing tool are absent from the current tree. | Runtime art may remain usable, but reproducibility and prior completion claims need correction or archive restoration. | Root inspect and render timed out; option inspection succeeded with an incomplete 17-candidate pool. |
| 018 Resources Found | Current authority says implementation-current and static-positive, but unconditional completion fails on the open probability gate and missing durable cave-monster 3D/action visual proof. | Clean one implementation-jargon tooltip and reconcile the invalid catalog status; no authored gameplay defect is proven. | Root inspect and render timed out; prior bounded probability artifacts cover prefire and cave-brood scenarios, while full event/focus/decision pools remain incomplete. |
| 019 Soldiers from Nowhere | Current README describes a fully functional package, but provider-pool odds remain unresolved in the same document and the claimed asset manifest/handoff workspace is absent. | Keep dynamic provider callbacks; clean catalog implementation prose; do not centralize or delete weighted logic without MCP evidence. | Root inspect and render timed out; all new event-option and decision probability calls timed out after 180 seconds. |
| 020 Black Plague | Explicitly partial: sound-definition wiring, counter review, model/audio acceptance, broader presentation, attribution, balance, and live/runtime validation remain open; no Event 020 portrait-worker handoff was found. | Two dead helper families and four literal weights are bounded cleanup candidates; the previously reported absorption no-op is resolved and must not be removed. | Both root chains timed out in inspect/render; one complete two-option pool and one weaponization inspection were produced, but named-scenario evaluation timed out and one dynamic construct remained unresolved. |

## Safe bounded patches

### 1. Restore Event 013 in the shared settings name selectors

`common/scripted_localisation/chaosx_scripted_localisation_settings.txt:1616` defines `GetSettingsEventName`.

Its sequence maps Event 011 at lines 1658–1659 and Event 012 at lines 1662–1663, then skips directly to Event 014 at lines 1666–1667.

`common/scripted_localisation/chaosx_scripted_localisation_settings.txt:5617` defines `GetLastEventName` and repeats the same omission between lines 5663–5664 and 5667–5668.

This is not a dead event or missing localisation key.

`localisation/english/chaosx_event_names_l_english.yml:15` defines `chaosx.event_name.13`, `common/scripted_localisation/chaosx_scripted_localisation_debug.txt:73-74` maps Event 013, and `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:976`, `:9704`, and `:11984` consume the same event name.

The shared dispatcher prepares the event through `natural_disaster_prepare_random_event_fire` at `common/scripted_effects/chaosx_settings_effects.txt:4562-4576` and dynamically fires its root at lines 4820–4829.

Recommended bounded patch: add a `settings_event_id = 13` / `chaosx.event_name.13` branch to `GetSettingsEventName` and a `global.last_fired_event_id = 13` / `chaosx.event_name.13` branch to `GetLastEventName`.

This is a functional scripted-localisation correction and does not require any interface layout change.

### 2. Remove the proven-dead Event 020 response-target wrappers

The following scripted triggers have exactly one source reference each—their own definitions at `common/scripted_triggers/020_black_plague_response_triggers.txt:729-779`—across `common`, `events`, `interface`, and `localisation`:

- `black_plague_country_has_clean_city_rats_target`
- `black_plague_country_has_seal_food_stores_target`
- `black_plague_country_has_clear_sewers_target`
- `black_plague_country_has_flea_control_target`
- `black_plague_country_has_transport_purge_target`
- `black_plague_country_has_demolition_target`
- `black_plague_country_has_emergency_hospital_target`
- `black_plague_country_has_quarantine_target`
- `black_plague_country_has_cordon_target`
- `black_plague_country_has_treatment_target`
- `black_plague_country_has_warren_purge_target`
- `black_plague_country_has_countermeasure_target`
- `black_plague_country_has_doctor_wu_target`

No meta-effect or scripted-localisation construction of the `black_plague_country_has_*_target` identifier family was found.

Recommended bounded patch: delete these definition-only one-line wrappers and remove any documentation that still describes them as live target-discovery helpers.

### 3. Remove the superseded Event 020 evolution helpers

The following identifiers are definition-only in current gameplay source:

- `black_plague_rat_set_initial_evolution_ready_day` at `common/scripted_effects/020_black_plague_rat_effects.txt:93`.
- `black_plague_rat_load_evolution_log_context` at `common/scripted_effects/020_black_plague_rat_effects.txt:1022`.
- `black_plague_rat_record_current_evolution` at `common/scripted_effects/020_black_plague_rat_effects.txt:1038`; its only body call is to the dead loader above.
- `black_plague_rat_evolution_i_is_eligible` through `black_plague_rat_evolution_v_is_eligible` at `common/scripted_triggers/020_black_plague_rat_triggers.txt:595-699`.

The active replacement is the dedicated evolution subsystem: `black_plague_evolution_record_stage` begins at `common/scripted_effects/020_black_plague_evolution_effects.txt:117`, and `black_plague_evolution_runtime_pulse` begins at line 934.

The replacement calls `black_plague_rat_schedule_next_evolution_check` at line 983, so that scheduler and its MTTH entries are live and must be retained.

Recommended bounded patch: delete only the exact superseded identifiers above and update current Event 020 helper documentation.

### 4. Centralize Event 020 weighted literals without changing balance

The probability audit confirmed four source-level centralization candidates:

- `events/020_black_death.txt:377-380` uses `factor = 75`.
- `events/020_black_death.txt:397-400` uses `factor = 25`.
- `common/scripted_effects/020_black_plague_weaponization_effects.txt:66-69` uses `18/82`.
- `common/scripted_effects/020_black_plague_weaponization_effects.txt:283-286` uses `2/98`.

Event 020 otherwise uses named script constants for related tuning.

Recommended bounded patch: move the exact existing values into Event 020 script constants and substitute `constant:` references only where the fields accept them.

This is a centralization cleanup, not a balance recommendation; the two-option scenario evaluation timed out and the weighted modifiers are conditional.

### 5. Replace player-facing implementation jargon

Three current strings expose implementation mechanics instead of the world state:

- `localisation/english/016_brilliant_scientist_foreign_l_english.yml:87` says “fixed character identity”.
- `localisation/english/016_brilliant_scientist_foreign_l_english.yml:164` says “fixed character token has been retired”.
- `localisation/english/018_resources_found_decisions_l_english.yml:186` says “bounded field target, offer flags, and stored commercial interest”.

Recommended bounded patch: rewrite these lines as direct in-world outcomes while preserving their gameplay meaning.

This is localisation-only cleanup and does not require GUI source or layout changes.

### 6. Catalog cleanup owned by the spreadsheet workflow

Current workbook inspection found:

- `Events!C13` for Event 012 contains release-candidate, runtime-package, parameterized-action, source-record, and live-validation implementation prose instead of concise player-facing event-detail content.
- `Events!C20` for Event 019 contains registry, provider, and accounting implementation language.
- `Events!C17` contains mojibake in `D�Rhondan`, while current localisation uses `D’Rhondan`.
- `Events!M19` for Event 018 and `Clusters!G10` for Cluster 7 use status `Implemented`, but the workbook Legend defines only `Unavailable`, `Partially Available`, and `Playable`.

Recommended bounded patch: route the two detail rewrites and mojibake correction through `chaosx_spreadsheet_doc_worker`, then regenerate all export CSVs with `.tools/export_event_catalog_csv.py`.

The two invalid status cells need owner-approved mapping because Event 018 is implementation-current but completion-blocked and Cluster 7 inherits that ambiguity; this audit does not guess between `Partially Available` and `Playable`.

## Accepted-plan disposition gaps

### Event 016 reserved helpers have no current gameplay caller

Exact source searches across `common`, `events`, `interface`, and `localisation` found only definitions for the following Event 016 helpers:

- Effects: `brilliant_scientist_select_secondary_facility`, `brilliant_scientist_clean_invalid_facility_targets`, `brilliant_scientist_calculate_formation_power_score`, `brilliant_scientist_load_capped_force_count`, `brilliant_scientist_lose_temporal_anchor`, `brilliant_scientist_disqualify_achievement_setup`, `brilliant_scientist_weaponize_inherited_portfolio`, `brilliant_scientist_setup_project_force_packages`, `brilliant_scientist_rebuild_project_force_packages`, `brilliant_scientist_destroy_singularity_component`, and `brilliant_scientist_event19_record_project_force_manpower_obligation`.
- Triggers: `brilliant_scientist_has_singularity_route_seed`, `brilliant_scientist_has_low_grievance`, `brilliant_scientist_has_extreme_grievance`, `brilliant_scientist_project_independently_replicated_to_requested_stage`, `brilliant_scientist_project_can_advance`, `brilliant_scientist_can_form_multi_site`, `brilliant_scientist_can_form_by_institutional_capture`, `brilliant_scientist_singularity_terminal_is_ready`, `brilliant_scientist_directorate_sovereignty_surface_is_available`, `brilliant_scientist_formation_territory_plan_is_invalid`, and `brilliant_scientist_can_materialize_alien_arms_project_force`.

Representative definitions are `common/scripted_effects/016_brilliant_scientist_effects.txt:946`, `:976`, `:3482`, `:3512`, and `:3723`; `common/scripted_triggers/016_brilliant_scientist_triggers.txt:274`, `:286`, `:406`, `:474`, `:829`, `:840`, `:990`, and `:1043`; and `common/scripted_triggers/016_brilliant_scientist_territory_triggers.txt:534`.

Historical handoffs claim or reserve some of these helpers, including `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_scripted_system_architecture_handoff.md:149` and `:239`, `docs/plans/016_brilliant_scientist_plans/016_territory_planner.md:158`, and `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_project_reuse_identifier_map.md:343`.

The current README instead says targeted transfer, cleanup, probability, balance, and Event 019 isolation remain pending.

Disposition: do not delete this family in one mechanical patch.

The Event 016 owner should classify each identifier as `wire into an accepted current route`, `retain as an explicitly documented compatibility/reserved contract`, or `reject and prune with the stale handoff claim`.

Definitions rejected from the current design should be deleted together with their obsolete documentation assertions.

### Event 013 catalog status lacks a recorded promotion

`docs/plans/013_natural_disasters_plans/013_event_completion_final_audit.md:41` and `:68` say Event 013, Cluster 5, Event 099, and SCN-007 remain `Needs Testing` because live-engine scenario evidence was unavailable.

The current workbook uses `Playable`, while the Legend no longer includes `Needs Testing`.

No current document reviewed by this audit records the promotion decision.

Disposition: either record the evidence/authority that promoted the rows or revise the current source-of-truth status using the workbook's supported taxonomy.

This is a documentation/status decision, not a request to reinstate an obsolete label mechanically.

## Documentation and asset-evidence mismatches

At the current tree snapshot, `Test-Path` returns false for the following event workspaces:

- `docs/assets/011_secret_alliance`
- `docs/assets/013_natural_disasters`
- `docs/assets/014_cannibalism`
- `docs/assets/015_utopia_manifesto`
- `docs/assets/017_random_faction`
- `docs/assets/018_resources_found`
- `docs/assets/019_infantry_spawn`

This does not prove that corresponding runtime DDS, WAV, mesh, animation, or interface registrations are absent.

It does prove that current completion and reproducibility claims pointing to those exact durable workspaces cannot be independently verified from the present repository.

Examples include:

- Event 011's completion audit says `docs/assets/011_secret_alliance/` retains verified asset facts at `docs/plans/011_secret_alliance_plans/subagent_handoffs/completion_audit.md:73`.
- Event 013's completion audit says a 1,035-file archive was restored under `docs/assets/013_natural_disasters/` at `docs/plans/013_natural_disasters_plans/013_event_completion_final_audit.md:9` and `:69`.
- Event 014's README points to 38 unified-decision icons and current manifests under `docs/assets/014_cannibalism/` at `docs/specs/014_cannibalism_specs/README.md:18` and `:40`.
- Event 015's source-of-truth map identifies `docs/assets/015_utopia_manifesto/manifest.md` and `gfx_handoff.md` as its visual index at `docs/plans/015_utopia_manifesto_plans/015_utopia_manifesto_source_of_truth_and_resume_2026_07_15.md:20`.
- Event 017's completion audit says completed source/processed frames and a processing tool exist under `docs/assets/017_random_faction/` at `docs/plans/017_random_faction_plans/subagent_handoffs/017_random_faction_event_completion_audit_handoff.md:113`; neither the directory nor named tool exists now.
- Event 018's current depth addendum says its bounded cave-monster reconstruction tranche remains present until genuine closure at `docs/plans/018_resources_found_plans/018_resources_found_implementation_depth_addendum.md:32`, but the workspace is absent while the final completion audit still leaves the 3D visual-evidence gate open.
- Event 019's README names `docs/assets/019_infantry_spawn/manifest.md` and `gfx_handoff.md` as live evidence at `docs/specs/019_infantry_spawn_specs/README.md:72`.

Recommended next action: restore the documented archives from a known durable source where possible.

If restoration is not possible or the workspaces were intentionally removed, update the current README, completion, manifest, and handoff authorities to state exactly which runtime artifacts remain and which provenance, source, regeneration, or visual-review evidence was lost.

Do not fabricate regenerated evidence or preserve unconditional completion claims that depend on files no longer present.

Event 020's general asset and portrait source directories are present, including six portrait PNG sources under `docs/assets/portraits/020_black_plague/`, but no Event 020 `chaosx_portrait_creator` handoff or portrait manifest was found.

The current Event 020 completion audit already records this missing production handoff at `docs/plans/020_black_plague_plans/subagent_handoffs/2026-08-06_event020_completion_audit_handoff.md:46` and `:101`.

This remains a completion blocker under the current portrait workflow even though source PNG and runtime DDS files exist.

## Rejected cleanup candidates

- Do not delete `africa_compact_access_failure` merely because it is only cleared at `common/scripted_effects/012_africa_effects.txt:1595`; the current Event 012 handoff retains it as a save-compatibility alias, and no save-migration authority exists in this cleanup.
- Do not delete Event 012 world-focus packages gated by `africa_world_package_implementation_ready`; current focus handoffs identify them as deliberately dormant package infrastructure.
- Do not delete Event 014 one-reference spawn/recruitment helpers such as the specialist and regional warlord template families; `common/scripted_effects/014_cannibalism_effects.txt:5017-5022` and `:16367-16379` invoke those identifiers through `meta_effect` construction.
- Do not delete Event 018/019 `chaos_unit_family_provider_*_event19_*` callbacks based on static reference counts; the shared registry builds and invokes provider identifiers dynamically.
- Do not repeat the old claim that `black_plague_rat_try_absorb_adjacent_brood` is a no-op. It is implemented at `common/scripted_effects/020_black_plague_rat_effects.txt:2170` and called from `common/decisions/020_black_plague_rat_decisions.txt:41` plus Event 020 pulses at lines 1829 and 2370. The prior cleanup finding is stale and rejected.
- Do not delete `black_plague_rat_schedule_next_evolution_check`; the active replacement evolution subsystem calls it at `common/scripted_effects/020_black_plague_evolution_effects.txt:983`.
- Do not treat Event 013's repeated Cluster 5 membership `13, 13, 13, 13, 13` as an accidental duplicate. It may be intentional weighting and needs probability-authority disposition.
- Do not treat Event 019 scenario `factor = 1` / `factor = 0` fixtures as gameplay AI evidence; they occur in the scenario test file, not the runtime selection contract.
- Do not recommend any `interface/*.gui` visual layout or coordinate cleanup in this tranche.

## Dynamic-reference and probability uncertainties

The mandatory probability audits were routed through `chaosx_ai_probability_auditor` for Events 011–015 and Events 016–020.

No probability patch is authorized by this report.

Confirmed MCP results and limits are:

- Event 011 event options: 45 candidates, incomplete pool, four required inputs, one unresolved input. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9f62073effae768ad6e924a416546050ced7a5b4293848de6fd120cc65bf03bc/c2dc63102a18a265a83e64be5c0f7f9e34310eb6e690cdb6c6fa34fd3f4128b8/probability-inspect-893bcd88de1f.json`.
- Event 012 diaspora, priority-member, promoted-Tier-A, and RSA inspections succeeded, but all four pools were incomplete and each retained an unresolved input. The world-order and two world-package calls timed out after 180 seconds.
- Event 013 event-option inspection timed out after 180 seconds; decision inspection failed with `Transport closed`.
- Events 014–015 received no adapter evidence after the probability transport closed. Their event, decision, MTTH, focus, and AI-strategy weights remain source-only observations.
- Event 016 evolution options: 18 candidates, incomplete pool, nine required inputs, one unresolved input. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d3e25351e895f681d6a208920bc62f4a74ef3c05dfd7900c13fe7da06fec03b2/ab5717220786646b49f121daf60c12226b973e2791ff02f56c72517d1cc33797/probability-inspect-991079c10600.json`.
- Event 017 event options: 17 candidates, incomplete pool, 25 required inputs, one unresolved input. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eec508000d4167ee7d86b3a269771465a7c0d3a662f4ca3747d354422c3a511b/ad93b1dfe787001a0174e5536a0796360e99c7731e4c46f5e15414611c6eb877/probability-inspect-fa6b2ff6204e.json`.
- Event 018's retained bounded evidence evaluates prefire scenarios at 60/40 and proves the five-candidate cave-brood pool in two named scenarios, but event-option, focus, and decision pools remain incomplete. No cleanup or balance defect is established.
- Event 019 event-option and both decision adapters timed out after 180 seconds. All weighted Event 019 cleanup conclusions remain unresolved.
- Event 020's `chaosx.nr20.46.a/b` inspection found a complete two-candidate pool with zero unresolved constructs. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9c287c5002b964c0072f23b1d010e246b0202459808514e3b3c21a5e97ad7b7f/4a0d107d906c692ceff25b22d30176be50d5b293e707b43d42bbd8a55893cf12/probability-inspect-a04ba2efd8da.json`. Evaluation of `E020_HUNGER_CRISIS_BASE` timed out after 180 seconds, so the audit does not claim normalized scenario odds.
- Event 020 weaponization inspection produced an artifact but retained one unresolved dynamic construct: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cbc8056b63aa5d04954ffb5abf0594b889361a82a822cde0b89007d9d8cb1f53/213f139e1be100659d08fa6618db31f7b72eb0d52b64733a32a45cc309f4de1e/probability-inspect-362254a8e39a.json`.
- Event 020's last-response decisions at `common/decisions/020_black_plague_shared_response_decisions.txt:81` and `:98` use `ai_will_do = { base = 0 }`. This may be intentional AI disablement or a dead weighted surface; decision inspection failed, so it remains unresolved rather than a deletion recommendation.

Repeated normalized `ai_chance` structures in Events 016, 017, and 019 are helper-centralization candidates, not safe automatic rewrites.

Event 016 has identical option blocks in `events/016_brilliant_scientist.txt:112`, `:133`, `:262`, and `:284` plus repeated aftermath families in `events/016_brilliant_scientist_aftermath_events.txt`.

Event 017 repeats one conditional shape across its first four options in `events/017_join_faction.txt:75-138`.

Event 019 repeats acknowledgement/incident shapes throughout `events/019_infantry_spawn.txt:71-714`.

Because the engine consumes option-local `ai_chance` blocks and the current adapter evidence is incomplete, any consolidation needs a supported reusable pattern and same-scenario pre/post probability comparison.

## Event MCP inspection, render, and compare evidence

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.

Current revision observed during the structural event pass: `bc0062fc8506`.

- `hoi4.event_inspect` for `chaosx.nr11.1` succeeded with a partial trace: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3d2dbf5f03198bd9060bbfca27a5bd7a1076d0e5371b64012940560c676d661d/ca2af16c414c6e4933d5d2c5efb90f67cdb2fa99f2185276fe46369d2ac04945/event-trace-bc0062fc8506.json`.
- `hoi4.event_inspect` for `chaosx.nr12.1` succeeded with a partial trace: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2df6c582dd9b15fd720fe3a937b3e7121fe110aa04bb5255a09933d08bbf8185/fa8ea90b19d5e1cb255e2a7a1f9bbcd9e9f9f08a102660dc723da9b3ceda1c5e/event-trace-bc0062fc8506.json`.
- `hoi4.event_inspect` for `chaosx.nr13.1` and `chaosx.nr15.1` through `chaosx.nr20.1` each failed with `timed out awaiting tools/call after 180s`.
- `hoi4.event_inspect` for `chaosx.nr14.1` returned `INTERNAL_ERROR / Unexpected internal error`.
- `hoi4.event_render` overview calls for all ten root chains failed with `timed out awaiting tools/call after 180s`; no render artifacts were returned.
- Separate inspect and render calls for `chaosx_nr20_weaponization.1` also failed with `timed out awaiting tools/call after 180s`.
- Later probability work observed `Transport closed`, which is recorded separately rather than being treated as equivalent to the earlier successful partial traces.

Source review is not presented as equivalent MCP evidence for any failed route.

`hoi4.event_compare` was not applicable because this read-only current-source audit had no baseline/proposed revision pair and made no source patch.

No comparison result is claimed.

## Broader migrations to defer

- Event 016's reserved/helper architecture needs an owner disposition pass, not a mechanical bulk deletion.
- Event 016/017/019 repeated option-weight shapes should be consolidated only if a supported helper pattern can preserve option-local behavior and the probability auditor can compare identical named scenarios before and after.
- Event 012's 199 controlled-pool candidates and dormant packages are accepted future/dormant scope, not repository clutter to erase during cleanup.
- Event 018's probability adapter and cave-model visual-evidence gaps are evidence/tooling work, not justification for speculative balance or gameplay rewrites.
- Event 020's 3D sound-definition, licensed-audio acceptance, bespoke-counter review, and portrait-worker handoff need their owning specialist workflows; they are not helper cleanup.
- Asset archive restoration for Events 011, 013, 014, 015, 017, 018, and 019 is a provenance/recovery tranche. If recovery is impossible, documentation must be explicitly downgraded rather than silently regenerated.
- Focus-tree geometry and interface visual-layout cleanup are outside this report. No `interface/*.gui` coordinate or layout edit should be included in follow-up patches from this handoff.

## Recommended patch order

1. Apply the Event 013 two-selector functional fix and verify both settings-selected and last-fired text paths.
2. Remove the exact Event 020 dead wrapper/evolution identifiers, re-run full static reference searches including dynamic/meta construction, then inspect the Event 020 root and weaponization chains when the MCP transport is available.
3. Centralize the four Event 020 literal weights without changing values, then require `hoi4.probability_compare` through `chaosx_ai_probability_auditor` using the same named scenarios.
4. Patch the three localisation strings and route workbook text/status work through the localisation and spreadsheet owners.
5. Run an Event 016 owner disposition pass over the exact definition-only helper inventory before deleting anything.
6. Reconcile or restore the seven missing asset workspaces and the Event 020 portrait-worker handoff, carrying every unrecoverable evidence loss into current completion documents.
7. Retry the failed structural event inspect/render routes and the incomplete/failed probability scenarios after the MCP transport is healthy; do not promote source-only conclusions to engine proof.

## Simplifications, omissions, and blockers

No implementation fallback or simplification was introduced because this audit was read-only.

The audit did not modify source, repair the findings, regenerate missing evidence, alter balance, edit the workbook, or change any interface/GUI surface.

Mandatory structural render evidence is blocked for every in-scope root by repeated 180-second timeouts, and structural inspect evidence is partial or blocked as recorded above.

Mandatory probability evidence is incomplete for most in-scope weighted surfaces because candidate pools were incomplete, calls timed out, the transport closed, or required dynamic inputs were unresolved.

No final completion claim should be made until the safe patches, accepted-plan dispositions, missing-evidence reconciliation, and required MCP reruns are complete.
