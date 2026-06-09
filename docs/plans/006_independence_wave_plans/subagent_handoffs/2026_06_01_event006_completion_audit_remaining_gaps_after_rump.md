# Event 006 Completion Audit: Remaining Gaps After Rump Tranche

Status: incomplete. Event 006 has substantial implemented runtime, decision, focus, achievement, and super-event work, but the current worktree does not satisfy all accepted specs and queued plans.

Audit scope:

- Specs compared: `docs/specs/006_independence_wave_specs/006_independence_wave_spec.md`, `006_independence_wave_focus_trees.md`, `006_independence_wave_country_packages.md`, `006_independence_wave_decisions_ai.md`, `006_independence_wave_assets_prompt.md`, `006_independence_wave_super_event_prompt.md`, `006_independence_wave_achievements_prompt.md`, `006_independence_wave_coding_prompt.md`, `006_independence_wave_catalog_update.md`, `006_independence_wave_research_notes.md`.
- Plans compared: `docs/plans/006_independence_wave_plans/006_independence_wave_subagent_deployment_plan.md`, `006_independence_wave_improvement_loop_gate.md`, recent handoffs under `docs/plans/006_independence_wave_plans/subagent_handoffs/`, and the current implementation doc `docs/events/006_independence_wave.md`.
- Implementation inspected: `events/006_independence_wave.txt`, Event 006 files under `common/`, `interface/006_independence_wave_icons.gfx`, `interface/chaosx_super_events.gfx`, `interface/chaosx_achievements.gfx`, localisation, asset docs, super-event/audio/image handoffs, and current asset folders.

## Completion Status by Surface

- Release resolver and host survival: mostly implemented but not final-validated. `events/006_independence_wave.txt:31-105` scores candidate pools, validates `can_independence_wave_host_release_current_candidate_safely`, reserves a host state, performs reduced release, restores cores, and registers successful releases. `docs/events/006_independence_wave.md:5-9` documents the current host-survival model.
- Event 005 separation: implemented in Event 006 surfaces inspected. `common/scripted_triggers/006_independence_wave_triggers.txt:50-68` rejects known Event 005/Soviet Collapse origin flags for candidate tags, and `common/scripted_effects/006_independence_wave_effects.txt:727-738` sets Event 006 origin on releases. `docs/events/006_independence_wave.md:95-97` claims no Event 005 focus loaders are used.
- Focus tree: implemented as a large shared provisional tree, with package overlays and AI present, but not complete against the focus spec. Current count check found 60 focus blocks in `common/national_focus/006_independence_wave_focus.txt`; `docs/events/006_independence_wave.md:105` still says 57 focuses, so docs/count alignment is stale.
- Decisions and AI: implemented as decision-category surfaces with 86 decision blocks in `common/decisions/006_independence_wave_decisions.txt`; AI strategy file exists. Scripted GUI/value display remains absent.
- Country packages and formables: partial. Current docs list OGB, ASY, DNZ, UGA, SOK, GAR, CHR, and Timetable Authority as starter packages/routes in `docs/events/006_independence_wave.md:13-19` and `:68-79`, but the same doc states other packages and formables are incomplete at `:21` and `:291-299`.
- Super-events: the required major candidates appear wired after recent tranches. `docs/events/006_independence_wave.md:215-289` lists First League, Human Renunciation, League War, First Old Name, Great Partition Week, First Impossible State, and Rump That Endures with sprite/image/audio/text/gate references.
- Achievements: 19 achievement definitions were counted in `common/achievements/chaos_redux_achievements.txt`, and 57 achievement sprite references were counted in `interface/chaosx_achievements.gfx`. This exceeds the catalog prompt's older 16-count direction, but full unlock-path validation was not proven.
- Assets: partial. Decision, category, idea, focus, achievement, and super-event asset tranches exist. Report/news images, package-specific portraits/seals, many flag/cosmetic packages, and animated GUI/formation assets remain missing or queued.
- Docs/catalog: partial. `docs/events/006_independence_wave.md` is updated, but it still records future work and stale counts. The improvement addendum still queues catalog/spreadsheet/final audit alignment.

## Top 5 Remaining Blockers and Gaps

1. Country-package depth is still incomplete.
   - Spec requirement: `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md:414-425` calls for a satisfying first implementation with Evo IV support for at least six historical-return or local-polity packages from at least three continents and Evo V support for at least two strange packages and one containment path.
   - Current evidence: `docs/events/006_independence_wave.md:13-19` lists only the verified starter packages, while `docs/events/006_independence_wave.md:21` and `:291-299` explicitly say other package-specific countries, formables, dormant tags, additional city states, protectorates, additional historical-return packages, local-polity packages, hidden formables, and deeper strange packages are not complete.
   - Matrix gaps remain visible in `006_independence_wave_country_packages.md:295-321` and `:340-348`, including Mesopotamia, Circassia, Mountain Republic, Bukhara, Khiva, Kokand, Asante, Kanem-Bornu, Darfur, Barotseland, Zulu, Herero, Nama, Palmares, Mapuche, Aymara, Tupi Coastal, and Andes communes.

2. Scripted GUI/value-display surfaces are not implemented.
   - Spec requirement: `docs/specs/006_independence_wave_specs/006_independence_wave_coding_prompt.md:323-330` requires useful mechanic windows for Independence Dossier Board, New States Congress, Patron Ledger, and Formation Ledger, with costs, tooltips, triggers, effects, AI equivalents, cleanup, localisation, and validation.
   - Asset requirement: `docs/specs/006_independence_wave_specs/006_independence_wave_assets_prompt.md:365-417` lists required scripted-GUI visual families for Dossier Board, Congress, Patron Ledger, and Formation Ledger.
   - Current evidence: `rg --files common/scripted_guis interface | rg '006|independence_wave|independence'` returned only `interface/006_independence_wave_icons.gfx`. `docs/events/006_independence_wave.md:297` still queues scripted GUI conversion.

3. Presentation asset coverage is not complete.
   - Spec requirement: `docs/specs/006_independence_wave_specs/006_independence_wave_assets_prompt.md:141-158` requires report images for petitions, committee, suppression, observers, negotiation, release, league, border commission, patron brokers, old name, local polity, impossible state, rump host, and failed wave. `:222-242` requires flag/cosmetic and portrait sourcing rules. `:435-449` requires asset coverage for every implemented formable.
   - Current evidence: `find docs/assets/006_independence_wave -maxdepth 2 -type d` shows asset folders only for achievement icons, decision category icons, decision icons, focus icons, idea icons, and super-events. There are no report/news image, flags, or portraits folders. `rg` found no `GFX_report_event_independence_wave_*` or `GFX_news_event_independence_wave_*` implementation references in inspected gameplay/interface/localisation/docs/assets paths.
   - Current docs also acknowledge missing work: `docs/events/006_independence_wave.md:205-213` queues animated category art, Patron Ledger icons, Formation Ledger seals, additional railway art, package-specific focus icons, portraits, seals, achievement icons, real source frames, frame sheets, DDS output, static fallbacks, manifests, and `.gfx` handoffs.

4. Strange/Evo V fulfillment is a bounded first module, not complete package depth.
   - Spec requirement: `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md:364-375` defines distinct strange packages such as Necromantic Custodianship, Anti-Mankind Directorate, Archive-State, and Railway Cult; `:424-425` requires at least two strange packages and one containment path for Evo V.
   - Current evidence: `docs/events/006_independence_wave.md:33` says the strange module "remains a bounded first module" and does not create strange country tags, super-event claims, or final strange visual assets. The improvement addendum queues deeper strange identities at `docs/plans/006_independence_wave_plans/006_independence_wave_improvement_addendum_post_focus_formation_tranche.md:31`.
   - Implemented Human Renunciation and First Impossible State super-events do not by themselves satisfy the package-design, asset, route-validation, and multi-package depth requirement.

5. Final validation, catalog/spreadsheet alignment, and audit gates are not closed.
   - Spec requirement: `docs/specs/006_independence_wave_specs/006_independence_wave_coding_prompt.md:214-231` requires event docs, event log entries, event details, localisation, asset manifests, achievement docs, super-event docs, catalog spreadsheet, focus docs, decision docs, and final report alignment before completion.
   - Plan requirement: `docs/plans/006_independence_wave_plans/006_independence_wave_improvement_addendum_post_focus_formation_tranche.md:541-552` requires resolver/helper, focus, decision, country package, localisation, asset, super-event/audio, and completion audits before any completion claim.
   - Current evidence: the same addendum queues catalog/spreadsheet/final audit alignment at `:32-33`; `docs/events/006_independence_wave.md:291-299` still lists future work; current docs and implementation counts disagree on focus count.

## Accepted Plans and Disposition

- `006_independence_wave_subagent_deployment_plan.md`: followed in shape. Handoffs exist under the required folder, and the current report is the read-only completion audit called for at `:51-55`.
- `006_independence_wave_improvement_loop_gate.md`: closure conditions are not met. The gate requires no known simplifications, complete package identity/assets/AI, GUI button validation, animation manifests, and aligned docs/catalog/assets at `:17-29`.
- `006_independence_wave_improvement_addendum_post_focus_formation_tranche.md`: accepted work is partly implemented and partly queued. The addendum explicitly says not to close Event 006 yet at `:3-6`, rejects a new broad planner pass at `:35-38`, and queues non-flag assets, scripted GUI/value display, package depth, Mapuche/PRA blockers, deeper strange packages, super-event catalog alignment, and achievement/catalog alignment at `:25-33`.
- Recent super-event handoffs for First Impossible State and Rump That Endures appear represented in `docs/events/006_independence_wave.md:269-289` and in the asset/audio/text handoff filenames, but those tranches do not close the broader package, GUI, asset, catalog, or validation gaps.

## Validation Performed

- Read required repo skills and relevant HOI4 wiki/vanilla documentation before auditing.
- Compared the named specs, plan files, current event doc, current handoff folder, and current implementation files.
- Mechanical checks:
  - No `<=` or `>=` tokens found in inspected Event006 gameplay/interface/localisation surfaces.
  - Coarse aggregate brace count over inspected Event006 script/gfx files returned balanced braces; this is not a full HOI4 parser check.
  - Localisation files sampled for Event006/achievements/gui/music report UTF-8 with BOM.
  - Counted 60 focus blocks, 86 decision blocks, 19 achievement definitions, and 57 Event006 achievement sprite references.
  - Absence checks found no Event006 scripted GUI file, no report/news image sprite references, and no Event006 report/news asset folders.

Validation still missing:

- No live HOI4 load, error-log parse, or scenario-run validation was performed in this read-only audit.
- No full scripted scope parser was run for every new Event006 file.
- No full missing-localisation key audit was completed after the Rump tranche.
- No country-package audit was proven for every starter package after the newest GAR/CHR/strange/rump work.
- No final catalog spreadsheet verification was performed beyond inspecting the spec prompt and current docs.
- No asset manifest audit proved that every registered sprite and every required animated major-route state has final DDS, source/fallback, manifest, and `.gfx` handoff.

## Asset and Documentation Gaps

- Missing implemented report/news image family despite required `GFX_report_event_independence_wave_*` set.
- Missing package-specific portrait/seal/flag/cosmetic coverage for current and future packages; only OGB flag files were found in the repo flag search for the sampled package tags.
- Missing scripted GUI asset families and animated state assets for Dossier Board, Congress, Patron Ledger, and Formation Ledger.
- `docs/events/006_independence_wave.md` remains honest about future work, but it is not a completion document yet and contains at least one stale implementation count.
- Catalog spreadsheet alignment is claimed for the primary row in `docs/events/006_independence_wave.md:91-93`, but the accepted addendum still queues final spreadsheet/catalog/event-detail alignment.

## Remaining Blockers

- Do not claim Event006 completion until package depth, scripted GUI disposition or implementation, report/news assets, package-specific presentation assets, catalog/spreadsheet alignment, and final validation audits are closed or explicitly queued with accepted reasons.
- Do not spawn another broad `chaosx_improvement_loop_planner` pass now. The existing addendum already covers the major depth gaps and explicitly rejects another broad planner pass until queued work is handled.
- Mapuche remains blocked until a real tag/state package is accepted. PRA remains queued until Event005 railway baggage is separated. New flag assets must still go through an asset subagent.

## Recommended Next Bounded Implementation Tranche

Run a "presentation and closure hardening" tranche before adding more broad mechanics:

1. Close the non-flag presentation gap for the already implemented starter set: report/news images, package portraits or council images, formation seals, and missing manifests for OGB, ASY, DNZ, UGA, SOK, GAR, CHR, Timetable Authority, and strange/rump presentation.
2. Either implement one stable scripted GUI surface, preferably a read-only Dossier Board or Formation Ledger display that calls existing helper effects, or write a narrow accepted deferral that explicitly keeps these as decision categories for this milestone.
3. Reconcile docs/catalog counts and rows after the asset tranche: focus count, super-event slots, achievement count, asset manifests, event details, and current package list.
4. Then run focused audits in order: asset handoff audit, localisation audit, decision/focus sanity audit, country-package audit for the seven starter packages plus Timetable Authority, and final completion audit.

This should be bounded to already implemented surfaces. Do not add new country packages or flag work in the same tranche unless an asset subagent first supplies the required researched assets and handoff.
