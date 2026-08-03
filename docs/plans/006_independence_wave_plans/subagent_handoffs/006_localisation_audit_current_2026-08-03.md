# Event 006 current localisation audit

Date: 2026-08-03.

Scope: read-only audit of the current Event 006 English localisation, event popup and event-log/detail selectors, scripted localisation, Statehood Ledger GUI references, focus text, decision/category/mission text, scenario wording, and package-binding wording. The obsolete pasted flag-log was ignored. No gameplay or localisation source was patched by this audit.

## Verdict

Current static localisation coverage is PASS after the narrow FORM-08 cost-text repair already present in commit `9480e9acc` (`loc(event006): complete Danubian project cost text`). The audit initially identified the missing FORM-08 `_tooltip` and `_blocked` siblings; the current checkout now contains both, so this is a closed lead rather than a remaining missing-key blocker. The only remaining localisation-related concerns are non-blocking review items: enum-selector fallback robustness, possible Statehood Ledger panel overflow that the GUI artifact cannot isolate, and confirmation of the public timing of Evolution 5 wording.

## Evidence and coverage

| Surface | Current evidence |
| --- | --- |
| Event 006 English files | 46 `localisation/english/006_*_l_english.yml` files; 6,522 parsed keys; 6,522 unique in scope; all 46 begin with UTF-8 BOM; no scoped duplicate keys; no `:0` keys. |
| Event popups | Ten `events/006_independence_wave*.txt` files; 469 unique title/description/name/text/custom-tooltip references; all resolve in the full English key set. |
| Scripted localisation | Eleven Event 006 files; 50 `defined_text` names; 348 `localization_key` references (342 unique); no missing key references and no duplicate defined-text names. `GetIndependenceWaveLeaguePhase` at `common/scripted_localisation/006_independence_wave_scripted_localisation.txt:9` covers all 13 league constants plus `independence_wave_league_phase_unknown`. |
| Focus text | Four Event 006 focus files; 319 focus IDs; every actual focus has a name and `<id>_desc`; 318 explicit focus description/custom references resolve. |
| Decisions, categories, missions | 66 Event 006 decision/category source files; 1,474 unique name/description/custom-cost/custom-tooltip/custom-trigger references resolve. Mission-style timeout and cleanup text is covered by the same scan. |
| Statehood Ledger GUI | `interface/006_independence_wave.gui` exposes 39 text/button/tooltip references; all resolve. Existing dynamic selectors cover ledgers, host, patron, network, league phase, founding phase, mission status, formable commit cost, and rival-bloc details. |
| Event Log and Event Details | Event 006 Event Log references resolve across the five evolution title/body stages, history danger/crisis milestones, selected-evolution summary, and the shared detail key at `localisation/english/chaosx_gui_l_english.yml:960`. `chaosx.event_name.6` remains at `localisation/english/chaosx_event_names_l_english.yml:8`. |
| Current package wording | The current 206-row binding CSV contains 138 selectable rows with a bound anchor mode, 55 selectable unbound rows, and 13 non-selectable overlays. This matches the canonical package README; SCN-008 ready text intentionally describes the unique-homeland rule without hardcoding the snapshot counts. |

## Missing key list

- None at the current checkout for the inspected Event 006 surfaces.
- Historical audit lead, now closed by `9480e9acc`: `independence_wave_form08_project_cost_tooltip` and `independence_wave_form08_project_cost_blocked` were absent beside `independence_wave_form08_project_cost` at `localisation/english/006_independence_wave_formable_registry_l_english.yml:112` while the three FORM-08 decisions called the base key at `common/decisions/006_independence_wave_form08_decisions.txt:22,46,70`. Current lines `112-114` contain the base, blocked, and tooltip strings, with values driven by the shared `independence_wave_decision_cost` constants.

## Duplicate key list

- No duplicate key was found inside the current 46-file Event 006 English scope.
- The targeted all-English Event 006 namespace scan also found no duplicate definition. Repeated source references in decisions and event-log selectors are uses, not duplicate localisation definitions.

## Scripted localisation issue list

- No unresolved Event 006 scripted-localisation reference or duplicate `defined_text` name was found.
- A robustness review remains for selectors that enumerate accepted values but do not end with an unconditional neutral branch: `GetIndependenceWaveCrisisResolution` (`common/scripted_localisation/006_independence_wave_crisis_localisation.txt:34-57`), `GetIndependenceWaveTransportFocusTitle`, `GetIndependenceWaveEconomicProgramFocusTitle`, `GetIndependenceWaveMilitaryProgramFocusTitle`, `GetIndependenceWaveAmbitionFocusTitle`, `GetIndependenceWaveFirstPowerCenterFocusTitle`, and `GetIndependenceWaveSecondPowerCenterFocusTitle` in `common/scripted_localisation/006_independence_wave_focus_scripted_localisation.txt:10-91`, and `GetIndependenceWaveForceTemplateName` in `common/scripted_localisation/006_independence_wave_scripted_localisation.txt:124-161`. These are fail-safe blank-text risks only if an unset or out-of-enum value reaches the selector; they are not proven current blockers, and the inspected GUI selectors do have fallbacks.

## Dynamic text opportunities

- FORM-08 is now complete: the base cost summary, the constant-backed blocked requirement string, and the explanatory tooltip are all present at `localisation/english/006_independence_wave_formable_registry_l_english.yml:112-114`.
- The five Statehood Ledger panel values at `localisation/english/006_independence_wave_gui_l_english.yml:50-54` are approximately 130-160 characters while their text boxes at `interface/006_independence_wave.gui:64-68` use `maxWidth = 386 maxHeight = 42`. A visual acceptance pass should confirm wrapping and truncation; source inspection alone does not establish overflow.
- Scenario readiness text at `localisation/english/006_independence_wave_scenario_l_english.yml:31` is deliberately rule-based rather than a hardcoded 138/55/13 snapshot. If the UI later requires live counts, add a source-backed scripted getter instead of freezing current CSV counts in localisation.
- Existing dynamic localisation already exposes ledgers, bands, actors, states, timers/mission status, formable commit cost, league phase, and rival-bloc members; no further safe static-to-dynamic conversion was justified.

## Cross-surface mismatch notes

- Event name, Event Details, event-log actor mapping, evolution selectors, and the five evolution stages are aligned. Event Details remains non-spoiler and appends the dynamic rival-bloc detail lines.
- The 13 league-phase constants in `common/script_constants/006_independence_wave_mechanics_constants.txt` align with the 13 `GetIndependenceWaveLeaguePhase` branches and their localisation keys.
- Focus, decision, category, mission, event popup, GUI, scenario, and Event Log references all resolve against the current English key set.
- Current package CSV counts (138 bound selectable, 55 unbound selectable, 13 overlays) agree with the canonical specification README. The current scenario ready string does not repeat these counts and therefore has no count contradiction.
- Evolution 5 body wording mentions dangerous routes and sovereignty projects. Static inspection cannot prove whether that body is shown before the intended World Collapse reveal; the owning event agent should confirm timing before changing player-facing text.
- No player-facing raw trigger fragment, event-target syntax, semicolon, em dash, or implementation-history wording was found in the scoped current values.

## File encoding concerns

- All 46 scoped Event 006 English YML files begin with UTF-8 BOM bytes `EF BB BF` and contain no forbidden `:0` suffixes.
- Scripted-localisation and gameplay `.txt` files were checked for key resolution and structure, not asserted to require a YML BOM; no encoding defect was observed in the inspected text.

## Recommended fixes

1. Keep the FORM-08 base, `_tooltip`, and `_blocked` trio at `localisation/english/006_independence_wave_formable_registry_l_english.yml:112-114` and retain the shared `independence_wave_decision_cost` constants as the single tuning source; no further patch is required for this lead.
2. Add unconditional neutral fallback branches to the enum selectors listed above only if the owning script contract permits an unknown value; reuse existing unknown keys where available rather than inventing route lore in localisation.
3. Render the Statehood Ledger at the inspected resolutions with representative long values and confirm whether the five `maxHeight = 42` panels wrap or truncate. Do not treat the current GUI artifact diagnostics as an Event 006 defect without an isolated reproduction.
4. Confirm the reveal timing of `independence_wave.evolution.5.body` before changing its wording.

## GUI artifact and uncertainty

The read-only GUI inspect used workspace `mod_chaos_redux_ea3b2d67c2c0` and produced `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f0b33c37561fae36987e3fb9764a7467f653c89557b6a4569d69d90ae40898f4/8a5d2fdd13aae4bfd84f7849877191e7c3575b4bf30659222c996d3a2d550087/gui-inspect.abdf359582c5b7a7.json`. The corresponding render fidelity artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0860cb0ae3e9f16fd9528a736f82498978fbc96c8dd7f38517c93b68005284b6/6cdf6641072a7a2e9f9f9289834e84b76c7b5a10a97437930176e7d7a6fcbeb0/independence_wave_status_window-fidelity.json`. The tool reported a global graph condition with 1,886 blocking diagnostics and 75 visible overlaps across the workspace, so it did not isolate an Event 006 overflow or prove a local GUI defect. No live game or save/load test was run.

## Patch and handoff record

- Changed files: only this dated handoff file.
- Changed gameplay/localisation keys: none by this audit.
- Dynamic localisation added or fixed by this audit: none; the current FORM-08 pair is present from `9480e9acc`.
- Behaviour/display before and after this audit: unchanged by this audit; current checkout displays the FORM-08 base, blocked, and tooltip surfaces.
- Handoff path: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_localisation_audit_current_2026-08-03.md`.

## Meaningful validation performed

- Parsed the current 46-file Event 006 English scope for key count, duplicates, BOM, and `:0` suffixes.
- Compared Event 006 event, decision/category/mission, focus, scripted-localisation, GUI, scenario, and Event Log references against the current English key set; the counts and resolutions are recorded above.
- Rechecked the FORM-08 custom-cost trio after commit `9480e9acc`.
- Used the read-only GUI inspect/render artifacts recorded above; the global diagnostic condition limits any overflow conclusion.

## Skipped meaningful validation and why

- No Hearts of Iron IV launch, live event firing, save/load, or consumer GUI test was run because repository policy assigns live validation to the user.
- No gameplay, localisation, interface, or workbook source was patched; the request was a read-only audit and handoff.

## Unresolved wording decisions

- Whether the enum selectors should gain neutral fallback text under their current value contracts.
- Whether the Statehood Ledger panel prose needs shorter variants after visual acceptance.
- Whether Evolution 5 wording is public before its intended reveal.

## Simplifications, omissions, and blockers

No localisation simplification or gameplay fallback was introduced. The whole Event 006 package remains subject to the separate package admission, formable, asset, AI/balance, `6001`, and runtime-evidence blockers in the current completion authority; those blockers are outside this localisation audit.
