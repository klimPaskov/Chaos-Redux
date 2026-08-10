# Event 016 Portal Raider and Black Plague documentation reconciliation

Date: 2026-08-09

Status: documentation-only reconciliation complete for the Event 016, Event 020, Mengele, portal-unit, project-registry, asset-status, and completion-boundary documents named by the parent. No gameplay, localisation, GUI, GFX, model, sound, tool, spreadsheet, or binary asset file was changed by this handoff.

## Follow-up correction, 2026-08-10

The native Portal Warfare surface is now documented as two target-specific raids. `brilliant_scientist_portal_facility_raid` targets hostile states containing factories, reactors, or rocket sites and calls `brilliant_scientist_portal_raid_extract_state_installation`; `brilliant_scientist_portal_special_project_facility_raid` targets exact `building = { tags = facility }` facilities and calls `brilliant_scientist_portal_raid_extract_installation`. Both require a six-battalion `portal_raider` formation, use seven-day preparation, ten Command Power, and sixty Teleportation Equipment, and consume the selected formation on success or critical success before reconstructing it in the captured target province. The exact facility raid's critical result may also extract one state installation.

The parent removed the optional `unit_model = { entity = portal_raider_entity }` and `portal_arrival` preview hooks from both raids because the rejected model package provides no accepted entity or action. The runtime raids remain mechanically functional; no model, preview, sound, or fallback wiring is implied.

Follow-up documentation files: `docs/events/016_brilliant_scientist/systems/portal_raider_api.md` and `docs/events/016_brilliant_scientist/systems/custom_technology_api.md`. The Event 016 README, package manifest, and core-runtime map still contain earlier single-surface wording where concurrent file locks prevented a safe replacement; their exact stale locations are recorded under Contradictions retained for parent review below.

## Current source-of-truth map

| Surface | Current accepted statement | Evidence |
| --- | --- | --- |
| Event 016 raid architecture | Native biological and Portal Facility Raids own preparation, reservation, cancellation, expiry, outcome, and raid history. The missing native CBRN callback blocks only the optional KRG biological stockpile and delivery ledger, not native Event 016 raids. No parallel ledger or free payload is approved. | `common/raids/016_brilliant_scientist_portal_raids.txt`, `common/scripted_effects/016_brilliant_scientist_raid_effects.txt`, `docs/events/016_brilliant_scientist/systems/portal_raider_api.md` |
| Portal Raider API | The generic API now exposes two native target surfaces: the state-targeted `brilliant_scientist_portal_facility_raid` calls `brilliant_scientist_portal_raid_extract_state_installation`, while exact `building = { tags = facility }` `brilliant_scientist_portal_special_project_facility_raid` calls `brilliant_scientist_portal_raid_extract_installation`; both use seven-day preparation, ten Command Power, sixty Teleportation Equipment, a six-battalion formation, and success/critical formation consumption plus reconstruction in the captured target province. | `common/raids/016_brilliant_scientist_portal_raids.txt`, `docs/events/016_brilliant_scientist/systems/portal_raider_api.md` |
| Portal Raider visual status | Counter art is complete and wired through `interface/portal_raider_system.gfx` at `gfx/interface/counters/divisions_large/unit_portal_raider_icon.dds` and `gfx/interface/counters/divisions_small/onmap_unit_portal_raider_icon.dds`. The runtime model/entity, actions, and sounds remain rejected and unwired after the failed semantic generation task and require user-approved paid recovery. | `docs/events/016_brilliant_scientist/systems/portal_raider_api.md`, `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/portal_raider_3d_model_handoff.md`, `gfx/entities` inventory |
| Clone visual status | The installed clone infantry model/entity package is reusable by generic consumers. This does not claim live playback, final action review, final GUI, or whole Event 016 completion. | `gfx/entities/clone_infantry.asset`, `gfx/entities/clone_infantry.gfx`, `gfx/models/units/clone_infantry/`, `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/clone_infantry_3d_model_handoff.md` |
| Black Plague access | Black Plague remains the native Event 020 project and runtime. A Kruger Directorate with Biological Weapons Theory can expose `black_plague_weaponization_program`; Mengele can expose it through the reusable Directorate special-project registry. It is present in the CBRN random/project registries. | `common/scripted_triggers/020_black_plague_weaponization_triggers.txt`, `common/scripted_effects/cbrn_project_effects.txt`, `common/scripted_effects/germany_mengele_effects.txt`, `docs/events/020_black_plague/overview.md`, `docs/events/germany_mengele/overview.md` |
| Registry invariant | Every future Chaos Redux special project must be reviewed for inclusion in the reusable CBRN random and project registries before acceptance as a new consumer. | Updated Event 016 project, Event 020, Mengele, project-family, and portal API documentation |

## Changed files

- `docs/specs/016_brilliant_scientist_specs/README.md`
- `docs/specs/016_brilliant_scientist_specs/package_manifest.md`
- `docs/specs/016_brilliant_scientist_specs/acceptance/016_acceptance_criteria.md`
- `docs/specs/016_brilliant_scientist_specs/handoffs/016_completion_status.md`
- `docs/specs/016_brilliant_scientist_specs/matrices/016_asset_inventory.md`
- `docs/specs/016_brilliant_scientist_specs/matrices/016_project_family_matrix.md`
- `docs/events/016_brilliant_scientist/overview.md`
- `docs/events/016_brilliant_scientist/systems/portal_raider_api.md`
- `docs/events/016_brilliant_scientist/systems/custom_technology_api.md`
- `docs/events/016_brilliant_scientist/systems/projects.md`
- `docs/events/020_black_plague/overview.md`
- `docs/events/germany_mengele/overview.md`
- `docs/plans/016_brilliant_scientist_plans/016_core_runtime_handoff_map.md`
- `docs/plans/016_brilliant_scientist_plans/016_source_of_truth_map.md`
- `docs/plans/016_brilliant_scientist_plans/016_brilliant_scientist_resume_packet.md`
- `docs/plans/016_brilliant_scientist_plans/016_brilliant_scientist_completion_audit_v2.md`
- `docs/plans/016_brilliant_scientist_plans/016_event19_generic_unit_family_3d_model_backlog.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_native_raid_integration_2026-08-03.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_portal_raid_beachhead_factory_theft_2026-08-03.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_krg_cbrn_callback_boundary_reaudit_2026-08-03.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_portal_calibration_documentation_reconciliation_2026-08-03.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_unit_model_backlog_reconciliation_2026-08-01.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/clone_infantry_3d_model_handoff.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/portal_raider_3d_model_handoff.md`
- `.tmp/016_brilliant_scientist_technologies_and_units.md`
- `docs/specs/016_brilliant_scientist_specs/package_checksums.sha256`

## Plan dispositions

| Statement or document | Disposition |
| --- | --- |
| Native raid framework as Event 016 architecture | Promoted to current source-of-truth wording. |
| “Missing native CBRN callbacks block Event 016 raids” | Superseded; the callback blocks only the optional KRG stockpile and delivery ledger. |
| Event 016 parallel CBRN ledger or free payload | Rejected and retained as a prohibited fallback. |
| Portal Raider seven-day, ten-Command-Power, sixty-equipment hostile seizure contract | Promoted to current API, overview, package, and handoff wording. |
| Portal Raider model/entity/actions/sounds | Queued behind user-approved paid recovery after the failed semantic generation task; no fallback model is accepted. |
| Portal Raider counter package | Promoted as complete and wired; this is separate from model/entity completion. |
| Clone infantry model/entity package | Promoted as installed and reusable; live playback and whole-event completion remain open. |
| Black Plague Kruger and Mengele access | Promoted as native Event 020 runtime access through Biological Weapons Theory and the reusable Mengele registry. |
| Future-special-project registry review invariant | Promoted to Event 016, Event 020, Mengele, project matrix, and portal API documentation. |

## Superseded or historical documents

The 2026-08-03 native-raid, portal-beachhead, CBRN-callback, and portal-calibration handoffs now carry dated scope-correction notices. Their original implementation evidence is retained, but current numeric and ownership statements are governed by the current portal API and this handoff. The 2026-08-01 unit-model backlog handoff and clone/Portal model handoffs now carry mixed-status notices. The resume packet and completion audit retain historical snapshots and point to the current core-runtime map.

## Contradictions retained for parent review

The core-runtime map and Event 019 model backlog contain older matrix cells that still say all seven model packages are deferred or that no entity package exists; dated current-status paragraphs supersede those cells, but the cells remain as historical planning evidence where a concurrent writer prevented a safe local replacement. The Event 019 backlog's Portal Raider row also still says `portal_raider_entity` is an active production job with authored portal-arrival actions; that row is historical and must not be read as current runtime or fallback wiring. Exact stale core-map lines observed during this pass are line 9 (single-surface Portal API wording), line 17 (`The seven model packages are deferred outside the current no-model scope`), line 21 (`the seven dedicated 3D packages remain deferred outside the current no-model scope`), line 79 (`No Event 016 unit or building ... entity package is accepted`), line 87 (`All seven consumers ... future 3D work`), line 155 (`all seven Event 016-specific 3D packages remain deferred`), line 218 (`Seven model packages remain a future approval-dependent backlog`), line 236 (`3D packages are deferred outside the no-model scope`), and line 260 (`These model packages are deferred outside the current no-model scope`). The Event 016 overview line 7, README line 9, and package manifest line 16 also retain the earlier single-surface summary. The core-runtime map also retains older rows that describe the KRG callback as a general Event 016 blocker; its dated status correction supersedes that claim. The parent should either replace these historical cells in a later quiet pass or leave them under the dated supersession notices.

The clone production handoff still records action-level review gates from its production audit. The accepted current statement is that the installed clone model/entity package is reusable, not that every action has live in-game acceptance. The parent removed the rejected Portal Raider entity and arrival-animation preview hooks from both native raids, so no unresolved runtime entity reference remains active; accepted 3D production, actions, sounds, and preview wiring remain pending and are not replaced by a fallback.

## Stale prompt or instruction list

The old Event 016 no-model wording remains in historical prompts and old plan prose, but current status pointers now identify the installed clone package, wired Portal Raider counters, rejected Portal Raider runtime model/entity, and queued remaining packages. No stale prompt was deleted because deletion was not authorized. The required next action remains parent-approved paid recovery or an explicit decision to keep the Portal Raider model rejected; no agent should silently substitute a different model.

## Markdown hard-wrap audit

The changed prose paragraphs were written as one physical line per sentence or paragraph, while headings, lists, tables, and code paths retain deliberate structure. No new mid-sentence hard-wrap was introduced. Existing historical documents retain their original line structure and are listed above when their stale wording was not safely replaced.

## MCP evidence and limitations

- Event 016 read-only inspection: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c7f814d5d485735c584e3a1b03e7e670ff6cade9e43c46e0ad5e7d293e14d9d7/b6724d768043dc33782d83903690be10c81ee512fadadab887ce436a5a534ddb/event-lint-550da12aba6a.json`, status `EVENT_INSPECTED_PARTIAL`, zero blocking diagnostics, validation deferred for workspace-wide helper projections.
- Follow-up Event 016 read-only inspection after the split raid surfaces: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bc509a49e9b9ee97c4af129306b5f2ff0570eb3002c5b62eb8a083d892318a3e/78e6bee1ae2261f2a505c854d9ac8fd2145a6bf5781e88110aa54ce1d050d170/event-lint-d0c3016e0598.json`, status `EVENT_INSPECTED_PARTIAL`, zero blocking diagnostics, whole-workspace helper projections and lifecycle passes deferred.
- Event 020 read-only inspection: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/893c65f4a67e0ff720b015c3b2402a15c4dba06f66942004bb205202094b4eb9/9490c86433db53a2947b4473816d4436564f66e2990897c4c1c995bede116132/event-lint-550da12aba6a.json`, status `EVENT_INSPECTED_PARTIAL`, zero blocking diagnostics, validation deferred for workspace-wide helper projections.
- Portal weaponization technology read-only inspection: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ae28b87c0fb039a40f34419b85e36ec66ed2a8ea901a6894d4520e8b77e11fd3/5d9102cad2437d662c5321e4925bdfd0ecaf254328b6e25a992d6523137bff7e/technology-lint-61ed306ee86d.json`, status `TECH_INSPECTED_PARTIAL`, no blockers, helper projections deferred.
- Kruger State national-focus read-only inspection: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7fe03c23a5db5a9243857a5922ad3692b5e1dbe0329e5b034ff57f9a6c8cd061/fcd1574d64c94b5a1bca6cc067a68c9de58ba530bc9036e73ba961ddf736f9e7/focus-inspect.c989b0c3d20866d7.json`, target tree `brilliant_scientist_kruger_state_focus_tree` has 100 focuses, layout hash `2051c203ebb08be69fbdf861193ea1b0d14345c6f393f7f331809834c78e2633`, and zero target-tree diagnostics; the global inspection surfaced 14 unrelated vanilla continuous-focus icon/localisation diagnostics.
- CBRN random/project registry inspection: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/628f5cb32e9c4a3757c58408c6afb50aaee749322b3d1e502d98aca5d7581d53/1aaa7c59d48e5a002ec0c77fe43e392b54ba140e901f4903fdb878497222ebdf/probability-inspect-3122a369c161.json`, adapter `random_list`, complete pool, eight candidates, zero unresolved inputs.
- Mengele registry inspection: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f658c91073bfc7f49b524412cb4a9832f2d6c863b56c0c17c916e5e5771b2e34/86e8eb4368c1b246625206673866a72a9d9c9f9745ebec9b07df634f14535c53/probability-inspect-8cc2a5e03682.json`, adapter `random_list`, seventeen candidates, one unresolved input, no diagnostics; normalized dynamic odds are not claimed.
- The custom-weighted-pool adapter against `common/scripted_effects/germany_mengele_effects.txt` returned `INTERNAL_ERROR`; the successful random-list inspection is retained, and no custom-pool probability claim is made.

## Checksums and validation

The Event 016 SHA-256 ledger now has 64 entries and zero mismatches, including both Portal API docs and this handoff. The refresh also records concurrent edits to existing frozen-set files; those files are not claimed as authored by this reconciliation. The portal evidence package retains the failed-task hashes in `portal_raider_3d_model_handoff.md`; no generated model hash is promoted as a runtime asset. Targeted `rg` checks covered obsolete callback-blocker wording, stale Portal Raider counter paths, split raid identifiers and extraction effects, removed entity/preview hooks, Black Plague registry names, and the future-registry invariant. No Hearts of Iron IV process was launched, no binary asset was inspected or changed, and no live GUI or campaign validation is claimed.

## Remaining risks for the parent

- No active Portal Raider entity or arrival-preview hook is registered after the parent removed the rejected references; accepted runtime model/entity/actions/sounds and preview production remain pending under the parent-owned model boundary.
- User approval is required before any paid Portal Raider model recovery attempt; no unapproved fallback is allowed.
- The optional KRG biological stockpile and delivery ledger still requires an idempotent native CBRN reservation/outcome/cancellation/expiry callback and must not become a parallel ledger.
- Live event, technology, weighted-registry, provider, GUI, audio, model playback, transfer, balance, and campaign evidence remain parent-owned and open.
- This handoff does not claim model, final GUI, or full Event 016 completion.
