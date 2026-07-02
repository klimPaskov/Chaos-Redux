# Event 015 Utopia Manifesto Read-Only Completion Audit

Date: 2026-07-02
Agent role: `chaosx_event_completion_auditor`
Scope: read-only audit of Event 015 `utopia_manifesto` against the source specs, prompts, accepted plans, handoffs, implementation files, assets, localisation, super-event/audio docs, achievements, event log, and spreadsheet row.

## Summary

Event 015 is complete from this audit's file-evidence scope. I found no missing implementation surface that blocks the parent from treating `utopia_manifesto` as the replacement for the old Event 015 identity.

Two residual risks remain:

- No live HOI4 launch, in-game click-through, or engine parser validation was performed by this audit or the specialist handoffs I reviewed.
- The repository worktree is very dirty with many unrelated Event 011, Event 013, Event 014, shared-system, deleted, and untracked files. Event 015 staging should be reviewed carefully before any commit or completion claim tied to a clean change set.

No new `chaosx_improvement_loop_planner` pass is recommended. The existing improvement addendum is accepted and implemented, and I did not find a new depth gap that lacks an unresolved plan.

## Completion Status By Surface

| Surface | Status | Evidence |
| --- | --- | --- |
| Old event replacement | Complete | Live search found old `World Tension Subsides/Falls` references only in specs and historical plan notes, not in live event/gameplay/localisation/docs surfaces. Event name is `chaosx.event_name.15: "Utopian Manifesto"` in `localisation/english/chaosx_event_names_l_english.yml:17`. |
| Entry event | Complete | `events/015_utopia_manifesto.txt:11-18` defines `chaosx.nr15.1`, `is_triggered_only = yes`, and `fire_only_once = yes`. |
| Fire-once registration and N/A | Complete | `common/scripted_effects/chaosx_logic_effects.txt:161` registers event id 15 in `global.fire_once_events`; parent follow-up split the checks so automatic dispatch uses `utopia_manifesto_has_dispatchable_target_available`, while `common/scripted_effects/chaosx_events_log_effects.txt:3154-3155` keeps `N/A` tied to the hard-valid `utopia_manifesto_has_valid_target_available` check. |
| Targeting | Complete | `common/scripted_triggers/015_utopia_manifesto_triggers.txt:17-39` blocks majors, strong industry, large armies, too many controlled states, special/nonhuman countries, capitulated countries, and already routed countries. Target thresholds are centralized in `common/script_constants/015_utopia_manifesto_constants.txt:21-34`. |
| AI/human acceptance | Complete | `events/015_utopia_manifesto.txt:24-35` gives acceptance `ai_chance = { base = 100 }`, hides rejection from AI with `trigger = { is_ai = no }`, and wires accept/reject effects. |
| Acceptance/rejection lifecycle | Complete | `common/scripted_effects/015_utopia_manifesto_effects.txt:141-165` initializes ledger variables, sets acceptance flags, loads `utopia_manifesto_tree`, and gates tree loading through `utopia_manifesto_can_load_tree`; `:167-190` clears route flags, ledger visibility, variables, arrays, and active mission flags on rejection. |
| Focus tree | Complete | `common/national_focus/015_utopia_manifesto_focus_tree.txt` contains 105 focus blocks. Direct evidence includes opening trunk `utopia_open_the_manifesto` at `:29`, Living Humanism `:194`, Common Store State `:357`, Guild Commonwealth `:520`, Island Discipline `:679`, Needful Land `:1507`, geography adaptation `:1716-1789`, Marked Bounds `:1805`, and late outcomes `:1991-2130`. The final focus audit reports no duplicate IDs, no dangling prerequisites, all focus localisation, and icon coverage in `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/2026-07-01_final_focus_tree_audit.md:11-24`. |
| Ledger values and GUI | Complete | `common/scripted_triggers/015_utopia_manifesto_triggers.txt:65-74` requires Need, Consent, Surplus, Overreach, Vocation Balance, Foreign Suspicion, and League Confidence variables. `localisation/english/015_utopia_manifesto_l_english.yml:10-13` displays the ledger values, route, geography, projects, League Confidence, friends, League, and pressure. `interface/015_utopia_manifesto_ledger.gui:60-98` displays value/status text and `:138-172` wires ledger buttons. |
| Decisions and missions | Complete | `common/decisions/015_utopia_manifesto_decisions.txt` defines 28 Event 015 decision/mission entries including census, storehouses, vocation work, guard projects, Needful Land arbitration, marked survey, integration, League aid, and renunciation. Cost helpers in `common/scripted_effects/015_utopia_manifesto_effects.txt:1304-1381` use command power, equipment, trains, convoys, manpower, army XP, stability, and war support, not political power stores. |
| Needful Land claims | Complete | `common/scripted_triggers/015_utopia_manifesto_triggers.txt:268-297` gates Needful Land opening and safe targets. `common/scripted_effects/015_utopia_manifesto_effects.txt:1601-1694` resolves arbitration into claims, refusals, guarantees, Need/Suspicion/Overreach changes, and no instant cores. |
| Occupation and integration | Complete | `common/scripted_triggers/015_utopia_manifesto_triggers.txt:307-330` requires controlled non-core state context, local storehouse, household councils, compliance/ledger safety, and no active/completed duplicate project. `common/scripted_effects/015_utopia_manifesto_effects.txt:610-665` and `:1851-1865` complete storehouse, integration, and household council projects. |
| Dynamic units | Complete | Unit helper constants exist in `common/script_constants/015_utopia_manifesto_constants.txt:416-440`; dynamic spawn helpers exist for Household Guard, Storehouse Engineers, Craft Militia, Harbor Watch, Ring Watch, Surveyor Columns, and League Cadres in `common/scripted_effects/015_utopia_manifesto_effects.txt:863-1293`. |
| Ideas and amplified rewards | Complete | `common/ideas/015_utopia_manifesto_ideas.txt:43-210` contains route and late outcome ideas with substantial modifiers for Living Humanism, Common Store State, Guild Commonwealth, Island Discipline, Marked Bounds, New Utopia, Necessary Commonwealth, and Paper Utopia. |
| Achievements | Complete | 12 achievements are defined in `common/achievements/chaos_redux_achievements.txt:2304-2419`; ready/disqualifier flags are driven by `common/scripted_effects/015_utopia_manifesto_effects.txt:2039-2123` and trigger gates at `common/scripted_triggers/015_utopia_manifesto_triggers.txt:625-663`. `interface/chaosx_achievements.gfx:1336-1371` registers all achievement icon triplets; `gfx/achievements/015_utopia*.dds` contains 36 files. |
| Assets and animated GUI | Complete | `interface/015_utopia_manifesto.gfx:3-16` registers event/news/super-event images, `:19-997` focus icons and shine variants, `:1002-1222` idea/decision icons, and `:1238-1287` static plus animated GUI sprites. Runtime files exist for report, news, both super-event images, 109 focus DDS, 25 decision/category DDS, 31 idea DDS, 13 GUI DDS, and 36 achievement DDS. `docs/assets/015_utopia_manifesto/manifest.md:55-103` documents imagegen-backed focus/decision/idea sources with no primitive/white-square replacements; `:189-244` documents imagegen-backed runtime GUI animations with static fallbacks and per-frame packages. |
| Super-events and audio | Complete | `common/scripted_effects/015_utopia_manifesto_effects.txt:2103-2123` emits New Utopia and Marked Bounds super-events, sets `global.current_super_event_audio_id`, and calls `play_current_super_event_audio` when settings allow. `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt:248-254`, `:617-623`, `:873-879`, `:1129-1135`, and `:1385-1391` map Event 015 images, titles, quotes, buttons, and descriptions. `localisation/english/015_utopia_manifesto_l_english.yml:560-567` contains researched final text. Audio files and sources exist at `music/super_event_utopia_new_utopia.ogg`, `music/super_event_utopia_marked_bounds.ogg`, `sound/chaosx_super_event_utopia_new_utopia.wav`, `sound/chaosx_super_event_utopia_marked_bounds.wav`, and `docs/super_events/source_audio/015_utopia_manifesto/`. |
| Event log and details | Complete | Actor mapping exists in `common/scripted_effects/chaosx_events_log_effects.txt:159-162`; Event 015 name/details selectors exist in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:975-979` and `:4773-4774`; event details text is in `localisation/english/chaosx_gui_l_english.yml:516`. |
| Docs and spreadsheet | Complete | `docs/events/015_utopia_manifesto.md:5-154` documents targeting, focus tree, ledger, decisions, integration, dynamic units, assets, and super-events. `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, sheet `Events`, row 16 has ID `15`, name `Utopian Manifesto`, Minor Fire-Once type, detailed current text, and `Status = Implemented`. The spreadsheet worker handoff confirms Event 015-only workbook alignment in `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/2026-07-01_spreadsheet_doc_worker.md:22-48`. |

## Accepted Plans And Disposition

| Plan or handoff | Disposition |
| --- | --- |
| `docs/plans/015_utopia_manifesto_plans/2026-07-01_final_depth_audit_addendum.md` | Accepted and implemented. It records closure for mission objectives, delayed Needful Land arbitration, Marked District survey, League Confidence, route unit families, cosmetic identities, assets, achievements, docs, and specs. |
| `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/2026-07-01_final_focus_tree_audit.md` | Implemented/pass. It records 105 focus blocks, route coverage, AI blocks, localisation, and icon coverage. |
| `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/2026-07-01_final_decision_mission_audit.md` | Implemented/pass after local decision/mission patches. |
| `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/2026-07-02_decision_mission_audit_small_patch.md` | Implemented/pass. It patched `decision_utopia_household_census` visibility behind `utopia_manifesto_household_census_ready` and left no further decision/mission fix recommended. |
| `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/2026-07-02_event015_asset_sidecar_handoff.md` | Implemented/pass from asset sidecar scope. It found no remaining primitive-shape, white-background, missing-DDS, missing-source, or missing-processed asset in the checked Event 015 asset surfaces. |
| `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/2026-07-01_super_event_text_research.md` | Implemented. Final titles, quotes, and button remarks are present in localisation and super-event scripted localisation selectors. |
| `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/2026-07-01_super_event_audio_research.md` | Implemented. Both researched source packages exist and final runtime OGG/WAV files are wired. |
| `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/2026-07-01_spreadsheet_doc_worker.md` | Implemented. Workbook row 16 currently matches the implemented event and status. |
| `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/2026-07-01_142930_event_completion_audit.md` | Superseded historical blocker snapshot. Its earlier Island Discipline and Common Administration caveats are resolved by later patches and the final re-audit. |

No accepted Event 015 plan was found that remains unimplemented, unqueued, unrejected, or unpromoted into docs/specs.

## Missing Or Simplified Requirements

No missing authoritative requirement was found in current file evidence.

Disclosed and accepted simplifications/design choices:

- Acceptance replaces the focus tree only on the accepting eligible country rather than creating a bespoke new country package. This remains a deliberate country-package design risk, not an unreported blocker, per `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/2026-07-01_final_event_completion_audit.md:70`.
- Late identity changes are cosmetic tags, not full new country packages with bespoke leaders. This is documented in the accepted improvement addendum and current implementation at `common/scripted_effects/015_utopia_manifesto_effects.txt:387-404`.
- The asset sidecar notes `interface/015_utopia_manifesto.gfx` uses `animation_rate_fps = 12` while the prompt requested 8 FPS. It did not find this to break runtime wiring; parent may decide whether exact prompt-rate normalization is desirable.
- The old primitive asset tooling remains under `docs/assets/015_utopia_manifesto/_tooling/complete_utopia_assets.py`, but the current runtime assets and manifest use imagegen-backed sources. The sidecar explicitly says that old tooling should not be treated as final-art evidence.

## Validation Performed Or Missing

Meaningful checks performed for this audit:

- Re-read source specs, acceptance checklist, prompts, accepted plans, final handoffs, and current implementation files.
- Searched live Event 015 surfaces for old `World Tension Subsides/Falls` identities.
- Checked current workbook row 16 in `docs/spreadsheets/chaos_redux_events_catalog.xlsx` directly with `openpyxl`.
- Checked runtime file presence for report/news images, super-event images, super-event source audio, runtime OGG/WAV files, focus/decision/idea/GUI DDS counts, and achievement DDS count.
- Rechecked current git status for staging/worktree risk.

Validation still missing:

- No HOI4 runtime launch, parser run, in-game event firing, focus-tree click-through, scripted GUI interaction test, achievement unlock test, or audio playback test was performed.
- No full repository-wide parse was attempted because the workspace is heavily dirty and this audit was scoped to Event 015 completion evidence.

## Asset And Documentation Gaps

No current asset or documentation gap was found for Event 015.

The following asset/audio/docs evidence is especially relevant to recent user corrections:

- `docs/assets/015_utopia_manifesto/manifest.md:55-103` says the focus, decision/category, and idea icons were regenerated from actual imagegen source art and not primitive/white-square placeholders.
- `docs/assets/015_utopia_manifesto/manifest.md:189-244` says the Ledger panels and all five animated GUI pieces were regenerated from imagegen source art with discrete per-frame packages and static fallbacks.
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/2026-07-02_event015_asset_sidecar_handoff.md` validates 178 registered textures, expected dimensions, source/processed proof, and no missing DDS files.
- `docs/super_events/super_event_audio_packages.md:308-338` records the Utopian Manifesto audio source/licensing package; `docs/super_events/super_event_quote_sources.md:30-54` records quote and button source proof.

## Remaining Blockers

No implementation blocker was found.

Remaining non-blocking risks:

- Missing live game validation.
- Dirty worktree and broad unrelated changes make final staging/commit review necessary.
- Exact animation FPS prompt alignment is unresolved as a polish decision, not a wiring blocker.

## Recommended Next Actions

1. Stage/review only the intended Event 015 files and handoffs before committing, because the current worktree includes many unrelated dirty and untracked files.
2. Run a live HOI4 validation pass for Event 015 when feasible: fire Event 015 as an eligible minor/player, verify N/A with no valid target, accept/reject paths, open Ledger, complete representative focuses/decisions, trigger both late super-events, and confirm audio/settings behavior.
3. Decide whether to normalize the five Event 015 animated sprites from 12 FPS to the prompt's 8 FPS, or document 12 FPS as the accepted runtime playback rate.
4. Do not spawn `chaosx_improvement_loop_planner` for Event 015 unless live testing reveals a new depth/design gap. The current accepted improvement-loop addendum is already implemented.

## Skills Used

- `chaos-redux-events`
- `hoi4-focus-trees`
- `hoi4-decisions-missions`
- `chaos-redux-event-assets`
- `chaos-redux-frame-animation`
- `chaos-redux-super-events`
- `chaos-redux-subagents`
- `chaos-redux-improvement-loop`

No skills were created or updated by this read-only audit.
