# Event 015 final completion audit

Subagent: `chaosx_event_completion_auditor`

Scope: Read-only completion audit for Event 015 `utopia_manifesto`. This audit inspected implementation, specs, accepted plans, handoffs, docs, assets, super-event documentation, audio wiring, achievements, and the event catalog workbook. No gameplay, localisation, asset, spreadsheet, or existing documentation files were patched.

## Superseded status

This audit is retained as the earlier blocker snapshot that drove the final Event 015 closure pass. Its blockers were dispositioned by later parent patches and final specialist audits:

- `2026-07-01_final_focus_tree_audit.md`
- `2026-07-01_final_decision_mission_audit.md`
- `2026-07-01_final_localisation_audit.md`
- `2026-07-01_final_country_package_audit.md`
- `2026-07-01_spreadsheet_doc_worker.md`
- `2026-07-01_final_depth_audit_addendum.md`

Read the final completion audit written after these handoffs for the current completion verdict. The remaining-blocker section below is historical, not the current Event 015 status.

## Overall status

Event 015 is substantially implemented, but this is not a clean closure audit.

The old `World Tension Subsides` implementation is gone from the live Event 015 surfaces, and `utopia_manifesto` has a real Minor Fire-Once event package, target selection, acceptance/rejection behavior, focus tree, ledger values, decisions/missions, Needful Land/integration hooks, dynamic unit families, achievements, assets, animated GUI resources, researched super-events, audio wiring, event-log text, docs, and a workbook row.

Blockers and unresolved completion risks remain:

- The accepted final depth addendum is internally stale/contradictory: it says accepted and implemented, but still states that decision/mission audit findings remain unresolved and that the event should not be called complete until several items are addressed or rejected.
- The Utopian Ledger scripted GUI remains display-only. It shows core values and League Confidence, but not route, geography, active projects, trends, League members, action buttons, costs, or AI-equivalent GUI actions promised by the deeper decision/GUI spec.
- Needful Land arbitration is no longer instant, but the implementation is still simpler than the user goal's full arbitration model: there is no separate target acceptance/refusal/compensation/guarantee outcome layer.
- The Event 015 plans folder has no focus-tree auditor handoff, country-package auditor handoff, or spreadsheet-worker handoff. The workbook row is updated, but remains `Needs Testing`.
- Several animated GUI assets are registered with static fallbacks, but only the ledger seal is confirmed wired into a live GUI surface. Other animated pieces are documented as registered for future overlays.

## Completion by surface

Core event identity and replacement: mostly complete.

- `events/015_utopia_manifesto.txt:11` defines `chaosx.nr15.1`; the old `events/015_world_tension_falls.txt` and old localisation file are absent.
- Shared event naming maps Event ID 15 to `Utopian Manifesto` in `localisation/english/chaosx_event_names_l_english.yml:17`.
- A targeted search found no live old Event 015 `World Tension Subsides`, `world_tension_falls`, `World Tension Falls`, or `015_world_tension` references outside specs/plans/handoff notes.

Minor Fire-Once registration, target selection, and N/A behavior: implemented.

- Event 15 is in `global.fire_once_events` as `UTOPIAN MANIFESTO` in `common/scripted_effects/chaosx_logic_effects.txt:160`.
- Event availability marks Event 15 unavailable when no valid target exists in `common/scripted_effects/chaosx_logic_effects.txt:522` and `common/scripted_effects/chaosx_events_log_effects.txt:3086`.
- Target selection prepares a target pool, selects one event target, and dispatches the event to that target in `common/scripted_effects/015_utopia_manifesto_effects.txt:12` and `common/scripted_effects/chaosx_settings_effects.txt:4584`.

Target gating: implemented with one audit caveat.

- `is_valid_utopia_manifesto_target` blocks majors, special/nonhuman countries, capitulated countries, world-end states, already accepted/rejected countries, incompatible event-created focus trees, strong industry, too many controlled states, too many divisions, and uncontrolled capitals in `common/scripted_triggers/015_utopia_manifesto_triggers.txt:17`.
- AI automatic targets additionally block player enemies and unstable subject wartime cases in `common/scripted_triggers/015_utopia_manifesto_triggers.txt:46`.
- This audit did not run live candidate-pool simulation across country tags, so balance around "strong industry" thresholds remains code-inspected rather than scenario-proven.

Acceptance/rejection: implemented.

- AI has forced acceptance through option weights and a human-only reject option in `events/015_utopia_manifesto.txt:23`.
- Acceptance sets the accepted state, opens the ledger, initializes variables, applies starting ideas, prepares AI weights, and loads `utopia_manifesto_tree` only for the accepting scope when allowed in `common/scripted_effects/015_utopia_manifesto_effects.txt:139`.
- Rejection sets the rejected state, clears the ledger and route variables, removes opening ideas, clears arrays, and cleans active target pointers in `common/scripted_effects/015_utopia_manifesto_effects.txt:160`.

Focus tree: implemented, but unaudited at specialist level.

- The focus file contains 106 `utopia_*` focus IDs, within the 85-115 focus target.
- Required major route IDs are present, including Living Humanism, Common Store State, Guild Commonwealth, Island Discipline, Reinforcement Paths, League of Need, Needful Land, Boundary Arbitration, Compliance Before Core, Adapt the Commonwealth, Marked Bounds Clause, Paper Utopia, New Utopia, Necessary Commonwealth, and The Manifesto Survives.
- The tree has AI weights throughout, but no `chaosx_focus_tree_auditor` handoff exists in `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/`. The route structure is therefore code-present but not independently audited for route balance, reward depth, mutual exclusion, and AI pathing.

Ledger values: implemented, with GUI simplification.

- Core values are initialized/refreshed in `common/scripted_effects/015_utopia_manifesto_effects.txt:193` and `common/scripted_effects/015_utopia_manifesto_effects.txt:273`.
- The six required values and League Confidence are displayed through `localisation/english/015_utopia_manifesto_l_english.yml:10` to `localisation/english/015_utopia_manifesto_l_english.yml:13`.
- The GUI itself is only a visible decision-category panel with text and icons: `common/scripted_guis/015_utopia_manifesto_scripted_gui.txt:1` and `interface/015_utopia_manifesto_ledger.gui:46`. It has no clickable scripted GUI action definitions, trend rows, route readout, geography readout, active project count, or League member list.

Decisions and missions: partially complete.

- The decision file defines concrete equipment/command/stability costs through custom cost text and cost triggers; it does not use a PP store.
- Mission IDs exist for harvest rotation, household guard, boundary arbitration, marked district survey, League aid corridor, and renunciation vote.
- Needful Land arbitration now starts `mission_utopia_boundary_arbitration` and only resolves to a claim on timeout if objective triggers still pass; see `common/decisions/015_utopia_manifesto_decisions.txt:398` and `common/scripted_effects/015_utopia_manifesto_effects.txt:1281`.
- Marked Bounds similarly starts a timed survey and only adds a risky claim on successful resolution in `common/decisions/015_utopia_manifesto_decisions.txt:451` and `common/scripted_effects/015_utopia_manifesto_effects.txt:1352`.
- Missing/simplified: arbitration success is a direct claim plus opinion modifier, while failure is ledger penalties; I found no separate refusal, compensation, guarantee, or negotiated settlement branch in the Event 015 implementation.

Occupation and integration: implemented at core level, still needs behavior audit.

- Integration grants a core only through compliance/Consent/Overreach gates in `common/scripted_effects/015_utopia_manifesto_effects.txt:525`.
- Needful Land and integration are represented in decisions, focuses, ideas, docs, and localisation.
- No country-package audit exists to verify cosmetic identity tags, flags, controlled-state integration behavior, and country package side effects as a whole.

Dynamic unit families: implemented.

- Six unit-family spawn helpers exist: Household Guard, Storehouse Engineers, Craft Militia, Harbor Watch, Surveyor Columns, and League Cadres, with centralized caps in `common/script_constants/015_utopia_manifesto_constants.txt:407`.
- Focuses call those helpers across the military, route, Needful Land, League, and late branches; examples include `common/national_focus/015_utopia_manifesto_focus_tree.txt:1217`, `common/national_focus/015_utopia_manifesto_focus_tree.txt:1377`, and `common/national_focus/015_utopia_manifesto_focus_tree.txt:1528`.

Achievements: implemented.

- All 12 Event 015 achievements are defined in `common/achievements/chaos_redux_achievements.txt:1805`.
- Localisation exists in `localisation/english/chaosx_achievements_l_english.yml:425`.
- Runtime achievement icon sprite triplets are registered in `interface/chaosx_achievements.gfx:1267`.

Assets and animation: mostly complete, with one presentation gap.

- `interface/015_utopia_manifesto.gfx` registers the Event 015 report picture, news image, super-event images, focus icons, decision/category icons, idea icons, and animated/static ledger resources.
- The user-required icon regeneration appears satisfied: focus, decision/category, idea, achievement, and cosmetic flag handoffs state imagegen-backed regeneration and no placeholder/white-square artifacts; see `docs/assets/015_utopia_manifesto/manifest.md:53`, `docs/assets/015_utopia_manifesto/manifest.md:90`, and `docs/assets/015_utopia_manifesto/manifest.md:131`.
- Animated sheets and static fallbacks are documented in `docs/assets/015_utopia_manifesto/icon_animation_handoff.md:80`.
- Gap: only `GFX_utopia_ledger_seal_animated` is confirmed wired in `interface/015_utopia_manifesto_ledger.gui:20`. Other animated GUI pieces are documented as registered for future scripted GUI or overlays in `docs/assets/015_utopia_manifesto/manifest.md:189`.

Super-events and audio: complete by audit evidence.

- Super-event emitters set slots 151 and 152, set `global.current_super_event_audio_id`, and call current super-event audio playback for human countries in `common/scripted_effects/015_utopia_manifesto_effects.txt:1645`.
- Title, quote, remark, and description selectors are wired for slots 151 and 152 in `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt:555`, `:781`, `:1007`, and `:1233`.
- Localisation uses researched titles/quotes/remarks in `localisation/english/015_utopia_manifesto_l_english.yml:515`.
- Audio files exist at `music/super_event_utopia_new_utopia.ogg`, `music/super_event_utopia_marked_bounds.ogg`, `sound/chaosx_super_event_utopia_new_utopia.wav`, and `sound/chaosx_super_event_utopia_marked_bounds.wav`.
- Music and sound asset wiring exists in `music/chaosx_super_event_music.asset:916` and `sound/chaosx_sound.asset:489`.
- Quote and audio package documentation exists in `docs/super_events/super_event_quote_sources.md:20` and `docs/super_events/super_event_audio_packages.md:229`.

Documentation and spreadsheet: partially complete.

- `docs/events/015_utopia_manifesto.md` documents the implemented event, ledger, focus routes, decisions, integration, units, assets, and super-events.
- Source specs exist under `docs/specs/015_utopia_manifesto_specs/`.
- The workbook row for ID 15 in `docs/spreadsheets/chaos_redux_events_catalog.xlsx` is updated to `The Utopian Manifesto`, `Minor Fire-Once`, with detailed route text. The row status remains `Needs Testing`.
- No spreadsheet-worker handoff exists, even though the spec routing handoff requires `chaosx_spreadsheet_doc_worker` after final wording exists.

## Accepted plans and disposition

- `docs/plans/015_utopia_manifesto_plans/2026-07-01_final_depth_audit_addendum.md`: disposition is unresolved/stale. The header says "accepted and implemented", but the same file still says the decision/mission audit remains unresolved and lists completion gates that must be addressed or explicitly rejected before closure. Some items are now implemented in code, but the addendum has not been reconciled.
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/2026-07-01_decision_mission_audit.md`: partly superseded by later code, but not formally closed. Its GUI finding remains true: the ledger is still display-only.
- `2026-07-01_scripted_system_architect.md`: mostly implemented. Target dispatch, registry integration, focus tree load, N/A availability, decision/focus ledger helpers, and unit helpers are present. Earlier handoff risks about event-history logging appear addressed by dispatcher bookkeeping after Event 015 target dispatch.
- `2026-07-01_super_event_text_research.md` and `2026-07-01_super_event_audio_research.md`: implemented. I found no remaining super-event wording or audio blocker.
- Asset regeneration handoffs for focus icons, decision/idea icons, achievement icons, and cosmetic flags: implemented by manifest and sprite/runtime evidence.
- `2026-07-01_localisation_audit.md`: completed and patched localisation. Its dynamic-cost localisation opportunity remains a future improvement, not a completion blocker by itself.

## Meaningful validation factored into this audit

- Read and applied `AGENTS.md`, event, subagent, improvement-loop, asset, frame-animation, super-event, focus-tree, decision/mission, and spreadsheet skills.
- Consulted the required offline wiki and vanilla documentation before inspecting Chaos Redux files.
- Verified old Event 015 live file absence and live old-reference absence outside specs/plans/handoff notes.
- Inspected Event 015 dispatch, target gates, acceptance/rejection, focus ID coverage, mission effects, Needful Land resolution, GUI wiring, unit helper families, achievement definitions, asset registration, super-event text/audio wiring, docs, plans, and workbook row.
- Factored in the user's provided local validation: brace balance, unsupported-operator search, localisation BOM/duplicate-key checks, required key coverage, sprite coverage, asset dimensions, animated sheet dimensions, and super-event audio format checks.

Missing meaningful validation:

- No `chaosx_focus_tree_auditor` handoff for the 106-focus tree.
- No `chaosx_country_package_auditor` handoff for late cosmetic identities and country-package effects.
- No spreadsheet-worker handoff after final in-game wording.
- No live scenario or parser run is documented by this audit for AI route selection, decision mission behavior over time, or late outcome paths.

## Remaining blockers

1. Reconcile or close the accepted final depth addendum. Either update it to reflect implemented items and explicitly reject/queue remaining scope, or leave Event 015 marked incomplete.
2. Decide whether the display-only ledger GUI is acceptable. If not, implement route/geography/project/trend/League readouts and scripted GUI actions or document a deliberate scope rejection.
3. Decide whether Needful Land arbitration must include target refusal, compensation, guarantee, or negotiated settlement outcomes. Current code provides timed proof and no instant core, but not that full diplomatic model.
4. Run or obtain the missing focus-tree, country-package, and spreadsheet-worker audits.
5. Update the event catalog status if the parent considers the implementation past testing; otherwise keep `Needs Testing` as an honest residual status.

## Recommended next actions

1. Treat Event 015 as "implemented with unresolved completion blockers", not final-complete.
2. Close the existing final depth addendum before spawning more planning.
3. Run focused audits for the focus tree, country package/cosmetic identities, and spreadsheet alignment.
4. If the parent accepts the display-only ledger and simplified arbitration model, record those explicit rejections/acceptances in the plans/specs so completion claims no longer conflict with the accepted design.

## Improvement-loop recommendation

Do not spawn `chaosx_improvement_loop_planner` again for Event 015 yet. An unresolved accepted improvement-loop addendum already exists for this event. The next step is disposition: implement, reject with reasons, or queue the remaining addendum items.
