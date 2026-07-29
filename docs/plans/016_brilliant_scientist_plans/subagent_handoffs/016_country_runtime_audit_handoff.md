# Event 016 KRG country runtime audit handoff

## Scope and disposition

This is a current static country-package audit for fixed tag `KRG` and the Event 016 Kruger State formation/runtime surfaces. It prioritizes load and error blockers and is not an in-game completion claim. The shared worktree was heavily dirty; unrelated edits were preserved and no commit was created.

The package has the expected fixed-tag, dynamic-territory, leader, focus, decision, technology, force, AI, localisation, and asset surfaces. One narrow runtime defect was patched: route resets now clear `brilliant_scientist_route_sovereign_directorate`. No broad content, model, map, or identity redesign was made.

## Country package coverage checklist

| Surface | Status | Evidence / finding |
| --- | --- | --- |
| Tag registration | Pass | `common/country_tags/016_brilliant_scientist_country.txt` registers `KRG` once. Vanilla has no `KRG` tag. Workshop-wide uniqueness remains unresolved because the scan timed out. |
| Country definition | Pass | `common/countries/Kruger State KRG.txt` defines western-European graphical cultures and the KRG base colour. |
| Cosmetic tags | Covered with risk | `common/countries/016_brilliant_scientist_cosmetics.txt` defines `KRG_SCIENTIFIC_REPUBLIC`, `KRG_REPLICATED_STATE`, `KRG_MACHINE_STATE`, `KRG_TEMPORAL_CONTINUUM`, `KRG_XENOBIOLOGICAL_ASCENDANCY`, and `KRG_PROJECT_SYNTHESIS`. Formation/transform code also calls `set_cosmetic_tag = KRG`; base-tag cosmetic fallback semantics are not independently proven. |
| Country history | Pass | `history/countries/KRG - Kruger State.txt` supplies bootstrap capital `1`, dormant OOB, zero research slots, neutral politics, and zero starting stability/war support for an unreleased fixed tag. |
| Dormant OOB | Pass | `history/units/016_brilliant_scientist_dormant.txt` uses an empty `units = {}` block, matching vanilla empty-OOB precedent. |
| Formation territory | Pass, scenario-sensitive | `common/scripted_effects/016_brilliant_scientist_country_effects.txt` revalidates the frozen dynamic territory plan before transferring cores, ownership, control, and capital. No hardcoded Event 016 state-ID dependency was found. |
| Leaders and characters | Pass | Exactly one fixed `KRG_warren_kruger` character is defined in `common/characters/016_brilliant_scientist_characters.txt`; succession also defines institutional `KRG_continuity_network`. No duplicate fixed Kruger definition was found. |
| Focus assignment | Pass | Formation and takeover helpers load `brilliant_scientist_kruger_state_focus_tree` with `keep_completed = no`. |
| Decisions and missions | Pass, runtime depth delegated | Event 016 decision/category files and localisation are present; this audit checked load-facing names, descriptions, and icon references, not the separate decision-system balance audit. |
| Ideas and national spirits | Pass | Starting country ideas and project-force ideas have definitions and checked localisation; icons are present where specified. |
| Technologies | Covered, helper limitation | All Event 016 technology IDs referenced by the package resolve statically. The workspace technology scan was partial and no separate Technology Tree Viewer is installed, so complete tree projection remains unresolved. |
| Forces and equipment | Pass at load/control layer | Seven inactive bespoke battalions, six equipment archetype families plus variants, locked templates, guarded deployment, and bounded runtime effects are present. |
| AI plans | Pass at reference layer | KRG plan files and focus/trigger references resolve against the KRG focus tree and scripted triggers. |
| Localisation | Pass for checked package keys | Focus names/descriptions, decision names/descriptions, KRG leader/continuity keys, and checked country-spirit keys are present. |
| Flags and portraits | Pass for checked assets | Seven KRG flag triplets and all Event 016 portrait/focus/decision/idea texture references checked on disk. |

## File surface checklist

Core country files are `common/country_tags/016_brilliant_scientist_country.txt`, `common/countries/Kruger State KRG.txt`, `history/countries/KRG - Kruger State.txt`, and `common/countries/016_brilliant_scientist_cosmetics.txt`.

Identity files are `common/characters/016_brilliant_scientist_characters.txt`, `common/country_leader/016_brilliant_scientist_traits.txt`, `common/scientist_traits/016_brilliant_scientist_traits.txt`, `interface/016_brilliant_scientist.gfx`, and Event 016 portrait assets under `gfx/leaders/`.

Formation and map mutation are in `common/scripted_effects/016_brilliant_scientist_country_effects.txt`, `common/scripted_triggers/016_brilliant_scientist_country_triggers.txt`, the territory-planner scripted files, and Event 016 formation events.

Focus surfaces are `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt`, `common/scripted_triggers/016_brilliant_scientist_focus_triggers.txt`, `common/scripted_effects/016_brilliant_scientist_focus_effects.txt`, `common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt`, and the corresponding focus/interface/localisation files.

Decision surfaces are the Event 016 files under `common/decisions/`, `common/decisions/categories/`, `common/scripted_effects/`, `common/scripted_triggers/`, `interface/`, and `localisation/english/`.

Force and technology surfaces are `history/units/016_brilliant_scientist_dormant.txt`, `common/units/016_brilliant_scientist_project_forces.txt`, `common/units/equipment/016_brilliant_scientist_project_force_equipment.txt`, `common/technologies/016_brilliant_scientist_project_technologies.txt`, `common/technologies/016_brilliant_scientist_project_force_technologies.txt`, and related force effects/ideas.

## Findings and patch

### Patched stale route identity

`brilliant_scientist_clear_sovereign_route_identity` in `common/scripted_effects/016_brilliant_scientist_country_effects.txt:894-905` cleared six route flags but omitted `brilliant_scientist_route_sovereign_directorate`. That flag is set by `common/scripted_effects/016_brilliant_scientist_focus_effects.txt` and consumed by Event 016 AI/decision logic.

The helper now begins with `clr_country_flag = brilliant_scientist_route_sovereign_directorate`, so all seven mutually exclusive route flags are cleared before another route identity is applied. Before the patch, a route switch could leave stale sovereign-directorate triggers, AI weights, or decisions. After the patch, reset covers `sovereign_directorate`, `human_technocracy`, `clone_sovereignty`, `machine_ascendancy`, `temporal_continuum`, `xenobiological_ascendancy`, and `project_synthesis`.

### Map and state setup

The fixed KRG history intentionally uses bootstrap capital `1`; formation replaces it through the verified dynamic territory transaction. `brilliant_scientist_form_kruger_state_from_verified_plan` performs plan revalidation, state transfer, capital assignment, portfolio snapshot, KRG initialization, and focus loading in order. `brilliant_scientist_transfer_selected_state_to_kruger_state` uses state-scope core/claim/owner/controller effects and does not embed a stale fixed state list.

No missing fixed KRG state, port, railway, resource, building, or victory-point surface was found because Event 016 selects territory dynamically. Retain scenario checks for an empty/invalid plan, lost controller, and fully occupied takeover host.

### Politics, leaders, portraits, flags, advisors, and parties

`KRG_warren_kruger` is the single personal Kruger identity with the stage-0 portrait/idea portrait pair. `KRG_continuity_network` is an institutional machine successor and uses an institutional identity rather than a random personal pool. Kruger country-leader and scientist traits resolve to Event 016 trait files. Advisor/director roles are created through Event 016 scripted role effects and use the same identity token; no second fixed Kruger character was found.

The KRG country file has a valid colour and graphical culture. Flags exist for `KRG` and all six cosmetic tags in normal, medium, and small sizes. No missing checked portrait or GFX texture path was found. Party setup is supplied by history and route effects; route effects set ruling party, popularity, elections, ideology, and cosmetic identity.

One engine/style risk remains: Event 016 scripted effects use `recruit_character` in existing role/formation paths, while repository guidance discourages recruit-character calls in scripted effects/on-actions. This existing package pattern was not broadly rewritten in this load-focused audit.

### Focus, decision, idea, and asset surfaces

The KRG focus inspection found 100 focus nodes, zero tree diagnostics, zero layout crossings, and 108 connectors for `brilliant_scientist_kruger_state_focus_tree`. Every focus name and description was found in `localisation/english/016_brilliant_scientist_focus_l_english.yml`, and all normal/shine focus texture references resolve through `interface/016_brilliant_scientist_kruger_state_focus.gfx`.

Event 016 decision/category definitions have checked name and description localisation coverage. The eleven icon IDs not supplied by Event 016 GFX are generic vanilla sprite IDs, not missing KRG assets. Starting ideas include `brilliant_scientist_improvised_laboratory_state`, `brilliant_scientist_inherited_project_portfolio`, `brilliant_scientist_fragmented_command`, `brilliant_scientist_experimental_supply_chain`, and conditional `brilliant_scientist_scientific_exodus`; definitions and checked localisation are present.

### Military, technology, industry, supply, and production

The dormant KRG OOB is intentionally empty until formation. The conventional guard helper creates a locked Laboratory Guard template and computes a bounded grant, with route/takeover guards and technology-gated engineer/recon support. Project-force effects define locked templates and guarded one-time materialisation for portal, clone, robot, paleogenetic, xenobiological, exotic, and temporal families. The package uses inactive bespoke battalions and guarded equipment variants rather than globally enabling them.

Grant-only Event 016 technology IDs and weaponisation IDs referenced by force effects resolve statically. Vanilla IDs such as `tech_engineers`, `tech_recon`, `infantry_weapons`, and `tech_support` also resolve. Equipment and force IDs were cross-checked against definitions and no unresolved Event 016 reference was found. Repeatable free-unit loops were not found in the checked dispatch path; family receipts, operational gates, caps, and one-time package flags guard materialisation.

The current package supplies opening/setup logic, not a new industrial economy. Production, supply, fuel, manpower, and later maintenance remain bounded by the existing scripted package and should be exercised by the parent decision/force audit.

### AI and playability

`common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt` contains origin, project, route, takeover, and terminal plan surfaces. KRG focus references and `brilliant_scientist_kruger_focus_*` trigger references were checked against the 100-focus tree and Event 016 scripted triggers. No unknown KRG focus identifier was found.

Event 019 generic unit-family integration is not present in the current tree. The Event 019 registry describes future families as self-registering in their own integration surface, so no KRG registry edit was invented or backported. Re-audit if a KRG family integration lands later.

## Validation evidence and limits

- `hoi4.focus_inspect` on `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt` returned `FOCUS_INSPECTED`, 100 KRG focuses, tree diagnostic count 0, and no layout crossings. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bc390d7fb860da8c66a431e4535f69b0746c1413397fb7b00b8f04b701f9429c/7963f299e0870fc8684e61084f5c47388d3e28a23b8a52fdb7c71ce2d0dc9e27/focus-inspect.0a0ba01a9e3b0361.json`.
- `hoi4.event_inspect` lint for `chaosx.nr16.1` returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics in the focused response. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2b332f3cb761a07df2ba54ac54f22f0ab75c11f1ea20cd644071f8c6f5a78a7d/a03b319bd5ac64356a234e80bbdec77a11ced4fc703e1cb28672e7cb403a4c68/event-lint-b9117f0642fd.json`.
- Static identifier checks resolved Event 016 focus IDs, decision name/description keys, starting idea IDs, leader/portrait keys, force/equipment IDs, technology IDs, and checked GFX texture paths.
- Workspace focus diagnostics also reported 14 unrelated generic vanilla continuous-focus icon issues; none belonged to the KRG tree.
- A workshop-wide `KRG` collision scan timed out after 124 seconds. Vanilla collision search found no KRG registration; workshop uniqueness is unresolved rather than asserted.
- The workspace technology scan was partial and no separate Technology Tree Viewer is installed. Complete projected technology-tree validation was skipped because the installed helper did not provide a bounded KRG-only tree view.
- No Hearts of Iron IV process was launched and no in-game runtime scenario was run, per task boundary.

## Simplifications, omissions, and remaining risks

No broad redesign, new country package, new focus route, new model, or Event 019 integration was added. Remaining review items are explicit:

1. Confirm whether `set_cosmetic_tag = KRG` is valid as a base-tag cosmetic reset in the target game build, or replace it only with a documented intended cosmetic-tag operation.
2. Complete a bounded workshop collision check if tag uniqueness across installed workshop mods is required.
3. Complete KRG-specific technology projection once a Technology Tree Viewer or narrower helper is available.
4. Exercise dynamic territory and takeover edge cases in a parent-owned runtime scenario review.
5. Reconcile any future Event 019 unit-family integration against the self-registration contract before claiming cross-event readiness.

## Parent review handoff

Changed gameplay file: `common/scripted_effects/016_brilliant_scientist_country_effects.txt` (one added `clr_country_flag` for `brilliant_scientist_route_sovereign_directorate`).

Changed documentation file: `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_country_runtime_audit_handoff.md` (this handoff).

No commit was created because the shared worktree contains unrelated concurrent changes. Parent should review the one-line route-reset diff, retain the unresolved-risk list, and run final integrated validation within the parent-owned plan.
