# Event 006 current English localisation audit

Audit date: 2026-07-26.

Audit basis: current tree after `d8cc2ec99` and the parent follow-up indentation repair in `c242def71`.

## Verdict

**PASS.** Event 006 English localisation has no remaining key-coverage, duplicate-key, scripted-localisation, custom-cost, punctuation, SCN-008 count, or named league-phase display blocker in the audited tree.

## Missing key list

- **PASS: none in the 34 scoped Event 006 English YML files.** The files contain 5,575 parsed localisation keys, and all scoped event, decision, focus, idea, GUI, Event Details, evolution, scenario, country, and report surfaces resolve in the complete English localisation set.
- **PASS: no missing scripted-localisation targets.** The ten `common/scripted_localisation/006_independence_wave*.txt` files contain 100 `localization_key` references, 94 unique targets, and zero unresolved targets.
- **PASS: no missing Event 006 custom-effect tooltip keys.** The 688 `independence_wave_*` custom-effect tooltip references, 53 `chaosx.nr6.*` references, and 68 `chaosx.nr006.*` references resolve. The two `generic_skip_one_line_tt` references are in the vanilla-compatibility decision file and intentionally use a vanilla key outside this Event 006 localisation set.
- **PASS: no missing interface localisation keys.** `interface/006_independence_wave.gui` contains 36 `text`, `buttonText`, and tooltip references, all of which resolve.

## Duplicate key list

- **PASS: none.** The scoped 34-file scan found zero duplicate keys.
- A repository-wide targeted scan of Event 006 namespace keys found 3,529 unique rows and zero duplicate groups.

## Scripted localisation issue list

- **PASS: `GetIndependenceWaveLeaguePhase` is defined and wired.** `common/scripted_localisation/006_independence_wave_scripted_localisation.txt:9` maps all thirteen `independence_wave_league_phase` constants to named localisation keys and includes the unresolved fallback.
- **PASS: the Statehood Ledger uses the named selector.** `localisation/english/006_independence_wave_gui_l_english.yml:17` uses `[GetIndependenceWaveLeaguePhase]` rather than exposing the raw phase integer.
- **PASS: no raw trigger fragments are exposed.** The scoped values contain no `check_variable`, `has_*`, `NOT =`, country/global flag, or scripted-effect fragments.
- **PASS: the d8 GUI indentation outlier is closed.** `c242def71` restored the two-space indentation on `independence_wave_status_gui_patron` in `localisation/english/006_independence_wave_gui_l_english.yml:15`.

## Dynamic text opportunities

- **PASS: no open dynamic opportunity was found in this bounded audit.** Mechanic counters use explicit integer or fractional formatters, Statehood Ledger actor and patron values use scoped getters, SCN-008 uses scripted summary values, and the league phase is now named dynamically.

## Custom costs

- **PASS: all 321 Event 006 `custom_cost_text` references are covered.** They represent 100 unique base keys, and every base key has a matching `_tooltip` and `_blocked` key in English localisation.
- Cost text preserves the dynamic `constant:` tokens used by shared decision tuning and the accepted fixed text for the bounded IW-093/IW-098 package tranche.

## Punctuation findings

- **PASS: zero semicolon or em-dash values remain in the 34 scoped Event 006 English files.** The seven retained en-dashes are intentional compound labels such as the Kazan-Cheboksary, Church-Civil, and Mountain-River labels, not sentence punctuation.

## SCN-008 counts

- **PASS: the ready status is aligned with the current map-binding ledger.** `localisation/english/006_independence_wave_scenario_l_english.yml:31` states 138 selectable packages with unique current-map bindings, 55 selectable packages without a unique current-map binding, and 13 accepted non-selectable route overlays.
- The current binding CSV has 206 rows and reproduces the same 138 bound, 55 unbound, and 13 overlay split. The separate allocator counts of 149 publishers, 126 automatic/high-chaos candidates, and 138 SCN-008 ranked packages remain distinct source-of-truth metrics and are not conflated by the ready sentence.

## Cross-surface mismatch notes

- **PASS: Event Details and evolution wording are aligned.** The generic Event Details description remains non-spoiler and the Evolution 5 body no longer lists hidden route families before their reveal.
- **PASS: Event Log selectors resolve.** Event 006 event name, evolution type, five evolution titles and bodies, evolution summary, danger-milestone title/description, and generic Event Details all point to existing English keys.
- **PASS: HAW retry wording is documentation-only and consistent.** The 2026-07-26 retry handoff records the exact adult visual match at Digital Archives record `ark:70111/47Nx`, failed rights clearance, and no crop, repaint, DDS, or runtime override. No player-facing localisation key or gameplay display should change until a rights-cleared, identity-valid source is approved.

## File encoding concerns

- **PASS: all 34 scoped Event 006 English YML files begin with UTF-8 BOM bytes `EF BB BF`.** UTF-8 decoding succeeds and no scoped key uses the forbidden `:0` suffix.
- The shared `localisation/english/chaosx_gui_l_english.yml` and `localisation/english/chaosx_event_names_l_english.yml` files also retain UTF-8 BOM bytes.

## Recommended fixes

- **No localisation fix remains required for the audited scope.** The only post-d8 hygiene issue found, the missing indentation on `independence_wave_status_gui_patron`, is already fixed by `c242def71`.
- Keep the SCN-008 ready sentence at `localisation/english/006_independence_wave_scenario_l_english.yml:31` synchronized with the 138/55/13 map-binding ledger if the registry changes.
- Keep HAW's retry disposition in the documentation handoffs only until rights and identity gates pass. Do not create a generic portrait, fallback crop, repaint, or runtime override.

## Patch and handoff record

- **Changed gameplay/localisation files:** none.
- **Changed keys:** none by this audit. The parent's `c242def71` changed only indentation for `independence_wave_status_gui_patron` and did not change its key or display semantics.
- **Dynamic localisation added or fixed:** verified `GetIndependenceWaveLeaguePhase` and its GUI call site; no edit was made by this audit.
- **Before and after display behavior:** the patron line now has consistent YAML indentation after c242def71 with the same colon wording and dynamic patron/influence values; the league phase remains a named label instead of an integer.
- **Fallbacks or simplifications:** none introduced.
- **Unresolved wording decisions:** none in the audited localisation scope.
- **Plan handoff path:** this file.

## Meaningful validation

- Parsed all 34 scoped YML files for BOM, key shape, duplicate keys, `:0` suffixes, semicolon/em-dash punctuation, and scoped key count.
- Compared all Event 006 scripted-localisation references, custom-effect tooltip references, custom-cost triplets, and Statehood Ledger GUI localisation references with the English key set.
- Recomputed SCN-008 map-binding counts from `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv`.
- Re-read the current league-phase constants, selector branches, GUI call site, scenario ready text, Event Log selectors, and HAW retry handoff.

## Skipped meaningful validation

- No Hearts of Iron IV process, live GUI playback, or live Event Log playback was run. This was a source-level read-only audit, and live consumer validation remains with the user and parent completion audit.
