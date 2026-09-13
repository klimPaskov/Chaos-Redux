# Event 033 Acid Rain English Localisation Audit

## Result

Event 033 now has a dedicated English localisation package for its current reports, news events, four preparedness projects, five urgent actions, four recovery actions, dynamic cost displays, dynamic modifiers, dedicated GUI tooltips, Event Log staging text, formation super-event, and ten achievements.

The directly referenced and engine-inferred Event 033 surface contains 145 expected keys: 41 event and news keys, 31 decision keys, 24 active dynamic-modifier names, 14 GUI tooltip keys, four super-event keys, and 31 achievement keys. All 145 are present with one owner each.

The localisation work is complete within the permitted files, but the shared Event Log resolvers, decision requirement tooltips, conditional cost renderer, report payloads, and production GUI renderer leave integration or validation work outside this task's write scope. These gaps are listed below and are not treated as equivalent to completed localisation wiring.

## Sources inspected

- `AGENTS.md`, every file under `docs/specs/033_acid_rain_specs/`, Event 033 events and decisions, dynamic modifiers, achievement definitions and triggers, scripted effects and localisation, dedicated GUI and GFX files, super-event resolvers, and Event 033 text and audio manifests.
- The offline Paradox wiki pages required by `AGENTS.md`, including Localisation, Event modding, Decision modding, Interface Modding, and Scripted GUI Modding, were consulted together with the applicable core pages.
- The accepted audio remains the 80-second Carl Maria von Weber *Der Freischütz* Overture excerpt documented in `docs/assets/033_acid_rain/audio_manifest.json`. No audio wording or attribution was changed.

## Missing key list

None among the 145 directly referenced or engine-inferred current Event 033 keys.

The migration-only dynamic modifiers `acid_rain_state` and `acid_clouds_state` deliberately have no live English owner after removal of their obsolete shared rows. `common/dynamic_modifiers/033_acid_rain_dynamic_modifiers.txt` states that these definitions exist only so migration can remove them and that the current runtime never applies them.

## Duplicate key list

None in the Event 033 key namespace across `localisation/english/`.

The old shared owners were removed from `chaosx_decisions_l_english.yml` and `chaosx_ideas_l_english.yml`, leaving the dedicated Event 033 file as the sole owner of the current decision category and modifier keys.

## Scripted localisation issue list

1. Event 033 records evolution type 33 in `common/scripted_effects/033_acid_rain_effects.txt:1890`, but `GetEventsLogEvolutionTypeView`, `GetEventsLogEvolutionNameView`, the evolution body resolver, and the Event Details description resolver have no type-33 or event-33 branches. The keys `acid_rain.evolution.type`, `acid_rain.evolution.stage_1.title`, `acid_rain.evolution.stage_1.body`, `acid_rain.evolution.stage_2.title`, `acid_rain.evolution.stage_2.body`, `acid_rain.evolution.stage_3.title`, `acid_rain.evolution.stage_3.body`, and `acid_rain.event_details.description` are staged in the dedicated file but are currently unreachable.
2. The Event Log event-name branches for Event 33 are present and resolve to the existing `chaosx.event_name.33` owner. No duplicate event-name key was added.
3. `acid_rain_report_state` is valid for the state-bearing reports. In particular, the recovery helper saves the state target at `common/scripted_effects/033_acid_rain_preparedness_effects.txt:978` immediately before firing `chaosx.nr33.110` at line 985.
4. The three shared dynamic-cost keys reference real quote variables, but no scripted-localisation selector hides zero-valued resource families. A static localisation value cannot satisfy the decision source comment that zero fields should disappear.

## Dynamic text opportunities

- Add a scripted-localisation cost selector that emits only non-zero quote families and no more than the four spendable families permitted by the specification. The current strings display exact live duration and costs, but they also display zero-value political power, factories, manpower, support equipment, trains, convoys, trucks, or fuel when a row does not use them.
- Add report snapshot variables for the payloads required by Part 9 but not currently exposed at event time: destination region, arrival window, front and intensity, forecast-state count, severe building damage, evacuation status, exposure duration, remaining aftermath count and highest tier, global duration, global Event 33 deaths, touched-state count, lifetime contamination, severe-cell count, superstorm count, and unresolved global aftermath count.
- The departure and dissipation prose intentionally avoids nonexistent `acid_rain_aftermath_state_count`, `global.acid_rain_global_deaths`, and `global.acid_rain_touched_states` substitutions. Those facts should be restored only after gameplay-owned snapshots exist.
- Convert the dedicated GUI's hardcoded labels to localisation keys so abbreviations such as `PREP`, `AFTER`, and `SAVED`, and implementation-facing phrases such as `BOUNDED SUPERSTORM LIST`, can be reviewed and translated normally.

## Cross-surface mismatch notes

- The report and news keys now follow the current `chaosx.nr33.101` through `.114` and `.201` through `.205` scripts. The obsolete `.2`, `chaosx.news.37`, and `chaosx.news.38` prose is no longer the dedicated file's content.
- The Event Details and evolution prose exists, but the shared resolver still routes only other registered evolution types, including Natural Disasters. Event 033 therefore has Event Log identity through `chaosx.event_name.33` but no Event 033-specific detail or evolution presentation.
- Every decision uses raw `available`, `target_trigger`, and `custom_cost_trigger` blocks without `custom_trigger_tooltip`, `custom_override_tooltip`, or `custom_effect_tooltip`. The localisation describes requirements and consequences, but the disabled-state UI can still expose mechanical trigger text instead of concise player-facing requirements.
- The decision specification limits each cost row to four spendable resource families. The current three static custom-cost strings contain all eight physical or temporary resource families plus duration because the missing conditional renderer cannot suppress zeros.
- The dedicated GUI contains hardcoded English text in `interface/033_acid_rain.gui`, while only its 14 `pdx_tooltip` references are localisation-backed. This prevents full translation and leaves terse labels outside the localisation owner.
- The achievement descriptions and tooltips match the accepted stored conditions, including eligibility baselines, strict percentage thresholds, required receipts, continuous durations, deadlines, and administrative disqualifiers. Hidden random weights are not exposed.

## File encoding concerns

None in the four touched localisation files. Each begins with UTF-8 BOM bytes `EF BB BF`, uses the `l_english:` namespace, and contains no `:0` version suffix.

## Prose-quality issue list

### Vagueness

The prototype described generic fear, havoc, optimism, and resilience without identifying the responsible systems or player response. The replacement names corrosive exposure, poisoned runoff, damaged transport, shelter work, water protection, medical response, evacuation, and recovery.

### Bloat

The obsolete dissipation news repeated relief, sunlight, normalcy, hope, gratitude, resilience, and rebuilding. The replacement confirms that acute rain stopped and states the concrete damage that remains.

### Obvious explanation

GUI tooltips no longer begin by merely narrating that a panel “shows” a value. They define the timer, contamination ledger, preparedness weighting, coverage rule, forecast period, and update behavior.

### Repetition

Project and action descriptions separate duration, effect window, consumed resources, reserved manpower, temporary factory commitments, and refund behavior without repeating their titles or restating the same consequence in several forms.

### Overcomplication

Internal phrases such as “bounded repair progress,” “runtime ledgers,” and the hidden guaranteed-dissipation ladder were removed from player-facing text. Long descriptions were split into direct sentences while preserving every material commitment and target rule available to localisation.

### Writing-style violations

Unsourced causal claims about industrial emissions and deforestation were removed because Event 033's origin remains unknown. No implementation-history wording, hidden random weights, prompt fragments, semicolons, or unsourced em dashes remain. The only em dashes are part of the two user-mandated sourced super-event attributions.

## Sourced-quotation preservation notes

- `chaosx_super_event.117.q` preserves the exact Robert Angus Smith sentence, including both commas and the final period, followed by the requested attribution `Robert Angus Smith, Air and Rain (1872), p.444`.
- `chaosx_super_event.117.a` preserves Shakespeare's period spelling `raineth` and final period, followed by the requested attribution `Shakespeare, Twelfth Night`.
- The text-research manifest identifies both underlying works as public domain, reports no normalized match in the existing super-event quote or button inventory, and records no unverified fallback.
- The user-mandated attribution punctuation takes precedence over nearby older super-event files that use parentheses, hyphens, or uncurled quotation marks.

## Patch summary

### Changed files

- `localisation/english/033_acid_rain_l_english.yml`
- `localisation/english/chaosx_decisions_l_english.yml`
- `localisation/english/chaosx_ideas_l_english.yml`
- `localisation/english/chaosx_achievements_l_english.yml`
- `docs/plans/033_acid_rain_plans/validation/033_acid_rain_localisation_audit.md`

### Changed keys

- Events and news: `chaosx.nr33.1.t`, shared report/news acknowledgment keys, every `.t` and `.d` from `chaosx.nr33.101` through `.114`, and every `.t` and `.d` from `chaosx.nr33.201` through `.205`.
- Decisions: `chaosx_acid_rain_decision_category` and `_desc`, all four `chaosx_acid_rain_project_*` pairs, all five `chaosx_acid_rain_urgent_*` pairs, all four `chaosx_acid_rain_recovery_*` pairs, and the three `acid_rain_*_dynamic_cost` keys.
- Modifiers: every active `acid_rain_state_*`, `acid_rain_aftermath_*`, `acid_rain_recovery_*`, `acid_rain_action_commitment_one`, and `acid_rain_project_commitment_*` name, with explanatory descriptions for the acute, aftermath, recovery, and emergency-commitment modifiers.
- GUI: all 14 `acid_rain_gui_*_tt` keys referenced by the dedicated interface.
- Event Log staging: `acid_rain.evolution.type`, all three stage title/body pairs, and `acid_rain.event_details.description`.
- Super-event: the exact four keys `chaosx_super_event.117.t`, `.q`, `.a`, and `.d`.
- Achievements: `acid_rain_033_achievement_eligible_tooltip` plus `_NAME`, `_DESC`, and `_tooltip` for all ten Event 033 achievement IDs.
- Removed obsolete shared rows: `chaosx_acid_rain_decision_category`, `chaosx_acid_rain_decision_category_desc`, `chaosx_acid_rain_timeout`, `chaosx_acid_clouds_timeout`, `acid_rain`, `acid_clouds`, `acid_clouds_desc`, `acid_rain_state`, and `acid_clouds_state`.

### Dynamic localisation added or fixed

- State-bearing reports use `[acid_rain_report_state.GetName]` only where the source saves that target.
- National reports use the existing `acid_rain_preparedness`, `acid_rain_event_deaths`, `acid_rain_prevented_deaths`, and `acid_rain_active_exposed_states` variables.
- Dynamic costs use the existing duration, political-power, factory, manpower, support-equipment, train, convoy, motorized-equipment, and fuel quote variables.
- Invalid departure and dissipation substitutions for counters not created by the source were removed instead of displaying broken tokens or fabricated zeros.

### Display before and after

- Before: Event 033 exposed obsolete event IDs, stale generic disaster prose, duplicate shared decision and idea owners, no current decision/action descriptions, no GUI tooltip text, no current modifier names, no current super-event text, and no achievement names or measurable conditions.
- After: all current referenced keys resolve from dedicated or established owners, decision text states durations and commitment/refund rules, reports use available live facts, modifiers identify their concrete effects, GUI tooltips explain the visible ledgers, the exact accepted quotations are installed, and all ten achievements state measurable accepted conditions.

## Validation evidence

- A repository-wide English key-owner scan found zero duplicate Event 033 keys and zero missing keys among the 145 directly referenced or engine-inferred current keys.
- A stale-row scan found none of the nine obsolete Event 33 rows in the two shared owner files.
- A dynamic-token scan confirmed that every remaining variable used by the dedicated localisation exists in the Event 033 scripted effects or decisions.
- The event MCP inspection completed with partial shared-helper projection status and no blocker. Workspace revision: `6d777debfa1f3690688885a2172196d2dd66154ab0219592bc1c2401e1ba2bef`. Graph hash: `33eb336d444ddc9ca80399973b3f8d9cd3374033681997b70ab351ebdfb4e325`.
- Event trace artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bca893e9887dfa7fe956e3168723ef62908e63528d5f9030ec830d64404f77de/9f0de819531466237e5e37a8fe2afa7f42f28742e9b3b75fd4e6636c160db110/event-trace-6d777debfa1f.json`.
- Event overview manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9706487acec44aab8ab0115fbffed8d05676b8a9b893cf75b0a5a78d99ef3695/b3feb14bde7da9078d140978c4c73dcd72c73e8701913028907ce454fe2779d3/event-overview-6d777debfa1f-manifest.json`.
- Event overview PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/278dd896c655c34224bd00a60f36f92d33ede98aed5c4dc7f1725354243adda3/5b85ae7f7cbd92b00f8921479b1452caa8e8d233fc4c242f553b2996e27c86c3/event-overview-6d777debfa1f.png`.

## Skipped meaningful validation and exact blocker

The mandatory production GUI inspection and render could not produce evidence. `hoi4.gui_inspect` for `acid_rain_world_window` timed out with `timed out awaiting tools/call after 180s`. A second `hoi4.gui_render` attempt at 1920 by 1080 for normal, long-text, and missing-localisation states failed with the same 180-second timeout. No GUI artifact URI was returned, so localisation overflow, clipping, wrapping, and one-to-one production alignment remain unverified. Source inspection is not treated as equivalent render evidence.

No in-game validation was run because repository agents do not launch Hearts of Iron IV.

## Recommended follow-up fixes

1. Add Event 033 branches in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` for evolution type 33 and event ID 33, pointing to the eight staged Event 033 keys.
2. Add conditional cost scripted localisation and point the three custom-cost surfaces in `common/decisions/033_acid_rain_decisions.txt` to it so zero families disappear and no row displays more than four spendable families.
3. Replace raw decision availability and target output with concise custom requirement tooltips and add custom effect tooltips where the description cannot expose the exact completion result.
4. Add the missing Part 9 report snapshots in the gameplay-owned Event 033 effects, then restore those values to the departure and dissipation reports.
5. Replace hardcoded English GUI labels in `interface/033_acid_rain.gui` with localisation keys and rerun both mandatory MCP GUI routes after the server timeout is resolved.

## Unresolved wording decisions

None inside the patched localisation. The Event Details and evolution wording is final prose but remains unreachable until the shared resolver is wired. The departure and dissipation reports deliberately omit unavailable counters rather than invent values.

## Simplifications, omissions, and blockers

No placeholder or fallback text was used. The permitted localisation files were completed without gameplay, UI, asset, or spreadsheet edits. Full Event Details/evolution display, conditional zero-free costs, custom decision requirement/effect tooltips, missing report payloads, and rendered GUI fit remain incomplete for the explicit integration and timeout reasons above.

This file is the localisation audit and follow-up handoff path. No separate mechanic plan was created.
