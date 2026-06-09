# Event 006 Completion Audit: Next Gaps

Status: **incomplete**. This audit did not edit gameplay, localisation, assets, country files, history files, flag files, Event 005 files, or docs outside this handoff.

Scope constraints applied:
- Event 006 must remain independent from Event 005. Same tags can appear in both events, but Event 006 releases must not enter Soviet Collapse systems.
- Do not touch country flags, flag assets, flag wiring, `common/countries`, `history/countries`, or `gfx/flags`.
- Script flags are safe to discuss, but no implementation changes were made.

## Top 5 Remaining Concrete Gaps

### 1. The accepted improvement addendum is partially implemented but still open

Value/boundedness: high value, very bounded. This blocks a clean completion claim and blocks another improvement-loop planner pass unless the addendum is closed, folded into specs, queued with reasons, or explicitly rejected.

Spec/plan evidence:
- `docs/plans/006_independence_wave_plans/006_independence_wave_improvement_addendum_post_focus_formation_tranche.md:3` still marks the addendum as an open implementation plan.
- `docs/plans/006_independence_wave_plans/006_independence_wave_improvement_addendum_post_focus_formation_tranche.md:535-546` says the plan should remain open until implemented/folded/queued/rejected and that Event 006 should not be marked complete while it remains unresolved.
- `docs/plans/006_independence_wave_plans/006_independence_wave_improvement_loop_gate.md:17-29` requires accepted plans to be implemented or queued with a reason before closure.
- `docs/plans/006_independence_wave_plans/006_independence_wave_subagent_deployment_plan.md:35-42` says not to spawn another improvement-loop planner for the same event while the previous addendum is unresolved.

Current implementation evidence:
- `docs/events/006_independence_wave.md:11-67` shows many addendum items are now implemented: the instant release resolver, host survival safeguards, verified package/formable routes, decision categories, regional compact, First League super-event, patron ledger, AI overlay, and achievements.
- The addendum itself has not been marked closed, folded into the specs, or split into queued/rejected follow-up items.

Bounded next action:
- Do a plan-closure pass: map each addendum section to implemented, queued, rejected, or promoted-to-spec status. Do not spawn another improvement-loop planner until this is done.

### 2. Non-flag visual assets and manifests are still mostly pending

Value/boundedness: high value, bounded if limited to existing Event 006 surfaces and non-flag assets.

Spec/plan evidence:
- `docs/specs/006_independence_wave_specs/006_independence_wave_assets_prompt.md:28-39` requires event/report/news image coverage.
- `docs/specs/006_independence_wave_specs/006_independence_wave_assets_prompt.md:82-102` requires reusable focus and decision icon families.
- `docs/specs/006_independence_wave_specs/006_independence_wave_assets_prompt.md:160-220` requires decision, idea, and focus icon sets.
- `docs/specs/006_independence_wave_specs/006_independence_wave_assets_prompt.md:265-340` requires contact sheets, manifest notes, and validation.
- `docs/specs/006_independence_wave_specs/006_independence_wave_assets_prompt.md:365-418` requires Dossier Board, New States Congress, Patron Ledger, and Formation Ledger visual families.
- `docs/specs/006_independence_wave_specs/006_independence_wave_assets_prompt.md:435-451` requires formable-specific non-flag assets such as formation decision icons, focus icon families, idea icons, portraits, and seals.

Current implementation evidence:
- `docs/events/006_independence_wave.md:98-136` documents that current focus/category visuals still use generic vanilla sprites and lists pending Event 006 sprite names and animated asset needs.
- `common/decisions/categories/006_independence_wave_categories.txt:8-80` registers the Event 006 categories, but they all use the generic `GFX_decision_category_political` icon.
- Current asset files found for Event 006 are mainly achievement icons and the First League super-event image. I found no equivalent completed non-flag icon/manifest set for the implemented Dossier Board, Congress, Patron Ledger, Border Commission, Formation Ledger, or package focus/decision surfaces.

Bounded next action:
- Produce and wire only non-flag Event 006 presentation assets for already implemented surfaces. Keep flag assets, flag wiring, country files, history files, and Event 005 files out of scope.

### 3. Scripted GUI/value-display surfaces are not built; current surfaces are decision categories

Value/boundedness: medium-high value. Bounded if treated as a display pass over existing variables, but risky if it expands mechanics at the same time.

Spec/plan evidence:
- `docs/specs/006_independence_wave_specs/006_independence_wave_assets_prompt.md:365-418` requires visual families for the Dossier Board, New States Congress, Patron Ledger, Formation Ledger, and animated protected-capital/congress/formation state.
- `docs/plans/006_independence_wave_plans/006_independence_wave_improvement_addendum_post_focus_formation_tranche.md:418-462` calls for a GUI/asset data model after the decision data stabilizes.

Current implementation evidence:
- `docs/events/006_independence_wave.md:21-29` identifies the current Dossier Board, Congress, Patron Ledger, Formation Ledger, Border Commission, and Sealed Dossier as decision-category surfaces.
- `common/decisions/006_independence_wave_decisions.txt:40-2072` implements those surfaces as decisions.
- `common/decisions/categories/006_independence_wave_categories.txt:8-80` registers the categories.
- No Event 006 scripted GUI implementation was found under `common/scripted_guis`, and the current interface references found for Event 006 are achievements and the First League super-event rather than these value-display panels.

Bounded next action:
- Either queue the scripted GUI pass with a reason or implement a small first panel that only reads existing Event 006 variables and flags. Do not create new release systems, country packages, flag assets, or Event 005 links as part of the GUI work.

### 4. Strange/Evo V package depth is still first-pass, not full package fulfillment

Value/boundedness: medium-high value. Bounded if limited to script-only route identity and containment follow-through, but full fulfillment would require additional assets and possibly later super-events.

Spec/plan evidence:
- `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md:370-373` defines the strange package matrix: Necromantic Custodianship, Anti-Mankind Directorate, and Railway Cult.
- `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md:424-425` says Evo V should have at least two strange packages and one containment path.
- `docs/specs/006_independence_wave_specs/006_independence_wave_super_event_prompt.md:101-130` specifies the First Impossible State super-event path.
- `docs/specs/006_independence_wave_specs/006_independence_wave_super_event_prompt.md:159-169` includes `first_impossible_state` and `human_renunciation` in the required super-event table.

Current implementation evidence:
- `docs/events/006_independence_wave.md:33` says the Sealed Dossier has a first surface and strange follow-through module, but explicitly says there are no strange country tags, super-event claims, or final strange visual assets.
- `common/decisions/006_independence_wave_decisions.txt:1916-2072` implements Sealed Dossier decisions.
- `common/national_focus/006_independence_wave_focus.txt:1142-1299` implements a strange follow-through focus module.

Bounded next action:
- Add a script-only strange route differentiation pass only if it can avoid country/history/flag edits. Otherwise keep the full strange package and First Impossible/Human Renunciation pieces queued with explicit blockers.

### 5. Super-event and achievement coverage remains partial after First League

Value/boundedness: medium value. Bounded only if one super-event or one achievement cluster is selected at a time.

Spec/plan evidence:
- `docs/specs/006_independence_wave_specs/006_independence_wave_super_event_prompt.md:159-169` lists required super-event candidates: `independence_wave_first_league`, `great_partition_week`, `first_old_name`, `first_impossible_state`, `league_war`, `human_renunciation`, and `the_rump_that_endures`.
- `docs/specs/006_independence_wave_specs/006_independence_wave_achievements_prompt.md:138-158` lists the expanded achievement catalog, including league-war and human-renunciation achievements.

Current implementation evidence:
- `docs/events/006_independence_wave.md:46` says only the First League super-event is wired.
- `interface/chaosx_super_events.gfx:116-117` defines `GFX_super_event_independence_wave_first_league`.
- `common/scripted_effects/006_independence_wave_effects.txt:1851-1855` contains `independence_wave_show_first_league_super_event`.
- `docs/events/006_independence_wave.md:56` lists implemented achievements and notes remaining league-war/final-settlement achievements as follow-up.
- `common/achievements/chaos_redux_achievements.txt:624-731` and `:875-892` contain the current Event 006 achievement blocks, including `cr_impossible_recognition`, but the full prompt catalog is not all implemented or dispositioned.

Bounded next action:
- Pick one missing super-event or one achievement cluster and close it end-to-end. Do not combine this with package, flag, or country-history work.

## Recommended Next Tranche

Recommended tranche: **Event 006 non-flag presentation and plan-closure tranche**.

Bounded scope:
- Close or fold the open improvement addendum by mapping each accepted addendum item to implemented, queued, rejected, or promoted-to-spec status.
- Update Event 006 docs/catalog notes to match current implementation status without claiming completion.
- Register and wire non-flag Event 006 icons/images for already implemented surfaces: Dossier Board, New States Congress, Patron Ledger, Border Commission, Formation Ledger, Sealed Dossier, and already implemented package/formable routes.
- Produce or document manifests/contact sheets for those non-flag assets.
- Explicitly queue the full scripted GUI pass if only decision-category presentation is retained.

Forbidden in this tranche:
- No `gfx/flags`, country flag assets, flag wiring, `common/countries`, `history/countries`, or Event 005 files.
- No Soviet Collapse system integration.
- No new improvement-loop planner until the current addendum is closed/folded/queued/rejected.

Why this tranche:
- It resolves the strongest completion blocker, improves the most visible stale presentation gap, and avoids the forbidden country/flag/history/Event 005 surfaces.

## Improvement Addendum Disposition

The previous improvement addendum appears **partially implemented but still queued/open**.

Implemented or mostly implemented from the addendum:
- Instant release resolver, host survival safeguard, release package scoring, regional compact, First League super-event, Border Commission, Patron Ledger, Congress decisions, several package/formable routes, and achievement wiring are reflected in current implementation files and `docs/events/006_independence_wave.md:11-67`.

Still unresolved or not closed:
- Addendum status remains open.
- Mapuche remains unimplemented while other packages were implemented instead.
- Full scripted GUI/value display remains unbuilt.
- Non-flag visual asset and manifest coverage remains incomplete.
- Strange package depth, additional super-events, and remaining achievement clusters remain partial or queued.

Recommendation:
- Close/fold the addendum before spawning `chaosx_improvement_loop_planner` again. A new planner pass is not recommended until this disposition is recorded.

## Validation Risks For The Recommended Tranche

- Confirm no files under `gfx/flags`, `common/countries`, `history/countries`, or Event 005 paths are touched.
- Confirm new non-flag `.gfx` sprite names point to existing DDS files and use stable names referenced by decisions/focuses/localisation/docs.
- Confirm category and focus icon replacements do not introduce missing-sprite errors.
- Confirm localisation remains UTF-8 with BOM, uses no `:0`, and avoids update-history wording.
- Confirm asset manifests list source, processed file, DDS destination, sprite name, usage surface, and remaining placeholder status.
- Confirm catalog/docs say Event 006 remains in progress and do not claim completion.
- Confirm no new release path sets Soviet Collapse/Event 005 origin flags or calls Event 005 scripted effects/triggers.
- If any scripted GUI work is included, validate it only reads existing Event 006 state and does not become a second mechanics implementation.

