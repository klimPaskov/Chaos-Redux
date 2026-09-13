# Event 028 Localisation Audit Handoff

> Historical localisation pass. Shared Air Cleanliness, super-event, and later Event 028 wording changes are covered by the current source and `../final_audit.md`; this handoff records the earlier audit boundary and is not the final completion evidence.

## Scope and changed files

- `localisation/english/028_asteroid_impact_l_english.yml`
- `common/scripted_localisation/028_asteroid_incoming_scripted_localisation.txt`
- `docs/plans/028_asteroid_incoming_plans/subagent_handoffs/chaosx_localisation_auditor.md`

No gameplay, workbook, asset, shared-localisation, or general-documentation file was edited.

## Coverage evidence

- Compared Event 028 localisation against `events/028_asteroid_impact.txt`, `_chaosx_news.txt`, the Event 028 decision/category, idea, dynamic-modifier and scripted-localisation sources, and the five achievement registrations in `common/achievements/chaos_redux_achievements.txt`.
- Audited 103 explicit localisation references, 50 implicit decision/mission/idea/dynamic-modifier name-and-description pairs, 33 Event 028 scripted-localisation output keys, all five achievements, all five missions, all 16 decisions, all 16 custom costs, and all 11 blocked-reason keys. No missing key remained in those sets.
- Added the seven parent-supplied shared-selector outputs: `asteroid_incoming.event_details.history.miss`, `.impact`, `.fail_closed`, and `asteroid_incoming.history.row.opening`, `.impact`, `.miss`, `.fail_closed`.
- The four history-row strings use the standard sequence, date, type and primary-actor arrays. The impact row also uses the secondary-actor array. They describe one evolving Major row and do not imply extra rows for reports, dust milestones, fragments, or the super-event.
- The impact detail exposes the saved country/state snapshot, impact date, affected-state and affected-country totals, deaths, fragment count, opening dust stage, and current dust score. Miss and fail-closed details state their physical outcomes explicitly.
- Target choice, confirmation, impact news, history, and super-event text use exact saved country, state, and continent objects. N/A behavior is present for an insufficient target pool, a missing report worst-state target, and a missing mission target-state pointer.
- `chaosx.nr28.5.d` is now a consolidated country report containing the N/A-safe worst state, strongest damage profile, actual country deaths, affected-state count, industrial/logistics/strategic levels lost, capital relocation count and status, opening/current dust stage, national protection, and recovery phase.
- Impact news doubles as the global impact/fragment summary and reports target state/country/continent, deaths, affected states/countries, opening dust, and a conditional fragment count. The no-fragment branch says so directly.
- Dust milestone text distinguishes Impact Winter, Global Dust Veil, Residual Haze, and Clear outcomes and states which worldwide penalties remain or end.
- Decision target text names `[FROM.GetName]`. All 16 custom-cost strings use live `asteroid_incoming_recovery` constants and resource icons. Blocked strings identify the failed state/control/war/dust/mission/resource condition. All five mission descriptions name the saved exact state and expose live infrastructure/railway floors or concrete site/factory requirements.
- All five achievement titles and tooltips are present and distinguish the near miss, original-target government recovery, crater-plus-fragment control, wartime crater seizure, and non-target worldwide dust recovery.
- Event Details now describes the premise and visible evolution consequences without formulas, target weights, or implementation history. The two evolution titles remain `Global Fragmentation` and `Extraordinary Minerals`; no Event 028-owned string calls either one Stage 2 after the registry split to types 2801 and 2802 at stage 1.
- Removed player-facing nuclear-separation wording. The owned localisation and scripted-localisation files contain no `nuclear`, `radioactive`, or `fallout` terminology.

## Scripted localisation changes

Added helpers for:

- worst-state name with N/A fallback
- strongest country damage profile
- opening and current dust stage names
- recovery phase
- national dust protection
- capital-relocation status
- conditional fragment-summary clause
- exact mission target-state name with N/A fallback
- current-capital clauses for all three target cards and the confirmation event

All helper output keys exist. Helper names are unique repository-wide within the `GetAsteroidIncoming*` family. Scripted-localisation braces are balanced, and no direct formatting control characters were placed in the scripted-localisation source.

## Duplicate keys

No duplicate key exists inside the owned Event 028 localisation file, and no duplicate `GetAsteroidIncoming*` defined-text name exists.

Three owned keys still collide with shared English localisation:

- `chaosx.event_name.28`: owned Event 028 text is `Asteroid Incoming`; `localisation/english/chaosx_event_names_l_english.yml` currently says `Asteroid Impact`. Per parent instruction, the owned wording remains and the shared duplicate was not edited.
- `asteroid_prediction_correct`: owned Event 028 text is `Asteroid Prediction`; `localisation/english/chaosx_ideas_l_english.yml` contains the legacy `Asteroid Prediction Correct`.
- `asteroid_prediction_correct_desc`: owned Event 028 prose describes the research benefit; the shared ideas file contains the legacy first-person sentence.

The parent should remove or align those three shared definitions. Keeping the Event 028 definitions preserves the audited wording until that shared cleanup lands.

## Prose-quality changes

- Vagueness: replaced abstract forecast, report, dust, decision, mission, and blocked-reason text with named actors, states, resources, thresholds, damage categories, and outcomes.
- Bloat: compressed the country report into seven data-bearing lines and removed explanatory implementation language.
- Obvious explanation: replaced tooltips that merely said an action was recorded or a report was filed with the actual effect, requirement, mission opened, or display behavior.
- Repetition: consolidated global impact and fragment facts into one summary and removed repeated “selected/recorded state” phrases.
- Overcomplication: split overloaded history/detail information into labelled lines and simplified bureaucratic reserve and recovery wording.
- Style repair: removed sentence semicolons and all non-quotation em dashes, removed update-history wording, and retained direct active prose.

## Quote and super-event preservation

- Preserved the verified quotation exactly: `Nature to be commanded must be obeyed. — Francis Bacon`.
- Preserved the sourced remark meaning exactly through the unchanged line `The Earth remembers the blow.`
- Preserved the title `The Stone's Verdict`.
- Reworked only the description so it names the saved target state, country, continent, opening dust stage/score, and conditional fragment outcome.

## Validation and artifacts

- UTF-8 result: `028_asteroid_impact_l_english.yml` begins with `EF BB BF` and uses repository key style without `:0`. The scripted-localisation `.txt` is UTF-8 without BOM, matching the repository's shared scripted-localisation files.
- Localisation square-bracket tokens balance 186/186 and colour-format openings/resets balance 102/102. Scripted-localisation braces balance 105/105.
- Repository scans found zero missing explicit references, zero missing implicit name/description pairs, zero missing achievement title/tooltip pairs, and zero missing scripted-localisation outputs in the audited Event 028 sets.
- Event 028 lint artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6d49f583e06062c0aa47f87e3ed75be17d0ce2d94987ba23274d2df125832426/b641774f903942928a363e54234aec2e0e7ed7084cf1cd27f9a950009e8d2e04/event-lint-3f736fd93d99.json`.
- Entry-options render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f2aee7d1d0a8631f8ed76a0213b3cdf5e0dca6517c76427c113f7fa8de345ead/2a97423fba1ce73b62017aeb3db66c2d28880c08336035434b6de6ccd986f9fe/event-options-a6f75bb40101-manifest.json`.
- Country-report options render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/366abe845c95def9e02a336839395410153ad4fd2aee006240e236b3739cf8ed/d525329bd54380f6f0adb08f400e7750f4936fce06eb52a35fa4a10f9b917dbc/event-options-a6f75bb40101-manifest.json`.
- Super-event lint artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/310f170642b1409bc95d037ad4d8a48a95f630c0a446c3c4af413d6df9c9925c/41dbdb9b9fb0ff9ad214805b761519818f0625ca225577204421e69c89d9e47c/event-lint-a6f75bb40101.json`.

## Remaining gaps and uncertainty

- The installed HOI4 MCP event renderer produces a structural event-chain graph, not a one-to-one event-popup or vanilla decisions-panel layout. No supported event-popup/ordinary-decision visual route was available, and Event 028 has no dedicated scripted GUI. Source lengths were tightened, especially the country report, but in-game clipping and wrapping remain unverified by MCP.
- The three shared duplicate keys listed above require parent-owned cleanup.
- No workbook wording was changed because the workbook is outside this ownership boundary.
- No simplification or fallback was introduced in the owned localisation behavior.
