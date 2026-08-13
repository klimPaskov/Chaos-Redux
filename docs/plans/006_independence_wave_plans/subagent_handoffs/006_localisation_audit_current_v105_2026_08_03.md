# Event 006 localisation audit, current v105

Date: 2026-08-03.

Scope: read-only audit of the current Event 006 localisation, scripted localisation, event log, decision and mission text, focus and idea text, Statehood Ledger GUI, scenario surfaces, and catalog-facing wording.

I read `AGENTS.md`, the required `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents` skills, the required offline Paradox wiki pages, and the relevant installed vanilla documentation before inspecting the source.

No gameplay, localisation, asset, workbook, or interface source file was changed by this audit.

## Missing key list

- No missing Event 006 event title, description, option, event-log, evolution, decision, mission, category, focus, idea, country, achievement, scenario, or Statehood Ledger key was found in the current static scan.
- The 45 `localisation/english/006_*_l_english.yml` files contain 6,424 unique entries.
- The ten `events/006_independence_wave*.txt` files have no unresolved literal player-facing localisation reference in the inspected title, description, option, text, tooltip, and custom-tooltip fields.
- The 61 Event 006 decision-category definitions have matching category and description keys.
- The current decision sources contain 133 custom-cost bases, and every base has its base, `_tooltip`, and `_blocked` key.
- The four Event 006 focus files contain 319 focus `id` lines: 184 direct definitions, 134 shared definitions, and one `independence_wave_focus_tree` root. Every actual focus has a name and `_desc` key. The root does not require an `independence_wave_focus_tree_desc` key; treating that absent key as a defect is a parser false positive.
- The 236 Event 006 idea identifiers have matching name and `_desc` keys.
- The Statehood Ledger interface references 39 localisation keys at `interface/006_independence_wave.gui:33-68`; all 39 resolve. The refresh button uses `independence_wave_status_gui_refresh_tt` at `interface/006_independence_wave.gui:36`, and the key is present.
- The shared Event Log detail key `chaosx.events_log.window.event_details.independence_wave` is present at `localisation/english/chaosx_gui_l_english.yml:960`. The Event 006 name map `chaosx.event_name.6` is present at `localisation/english/chaosx_event_names_l_english.yml:8`.

## Duplicate key list

- No duplicate key occurs inside the 45 Event 006 English localisation files.
- A global scan of all 247 English localisation files found 54,617 entries and zero duplicate key groups.

## Scripted localisation issue list

- The 11 `common/scripted_localisation/006_independence_wave*.txt` files contain 348 `localization_key` references, 342 unique keys, and zero missing keys.
- The four non-Event-006 references are the shared scenario intensity keys `chaosx.scenarios.intensity.low`, `.medium`, `.high`, and `.maximum` at `common/scripted_localisation/006_independence_wave_scenario_scripted_localisation.txt:95,99,103,106`. They resolve in `localisation/english/chaosx_gui_l_english.yml:173-176` and are intentional shared scenario strings.
- Event 006 localisation and source calls to custom `[Get...]` functions resolve against the installed scripted-localisation definitions. No undefined Event 006 scripted-localisation call was found.
- The following selectors enumerate accepted values but have no unconditional final branch. This is a fail-safe blank-text risk if a value is unset or outside the current enum, not a proven defect under the current source attestation:
  - `GetIndependenceWaveCrisisResolution` in `common/scripted_localisation/006_independence_wave_crisis_localisation.txt:34-57`. It has an `unknown` value branch at `:56-57`, but no unconditional final branch.
  - `GetIndependenceWaveTransportFocusTitle` in `common/scripted_localisation/006_independence_wave_focus_scripted_localisation.txt:10-25`.
  - `GetIndependenceWaveEconomicProgramFocusTitle` in `common/scripted_localisation/006_independence_wave_focus_scripted_localisation.txt:28-36`.
  - `GetIndependenceWaveMilitaryProgramFocusTitle` in `common/scripted_localisation/006_independence_wave_focus_scripted_localisation.txt:38-49`.
  - `GetIndependenceWaveAmbitionFocusTitle` in `common/scripted_localisation/006_independence_wave_focus_scripted_localisation.txt:51-67`.
  - `GetIndependenceWaveFirstPowerCenterFocusTitle` in `common/scripted_localisation/006_independence_wave_focus_scripted_localisation.txt:69-79`.
  - `GetIndependenceWaveSecondPowerCenterFocusTitle` in `common/scripted_localisation/006_independence_wave_focus_scripted_localisation.txt:81-91`.
  - `GetIndependenceWaveForceTemplateName` in `common/scripted_localisation/006_independence_wave_scripted_localisation.txt:124-161`.
- The GUI band, founding-phase, host-status, patron-band, patron-name, and mission-status selectors do have explicit fallback text branches in `common/scripted_localisation/006_independence_wave_gui_scripted_localisation.txt`.

## Dynamic text opportunities

- `chaosx.scenarios.launch_status.independence_wave.ready` at `localisation/english/006_independence_wave_scenario_l_english.yml:31` is intentionally generic and does not expose the current 138 bound selectable, 55 unbound selectable, and 13 overlay map-binding counts. If the ready-state panel needs those numbers, add a source-backed scripted getter rather than hardcoding the current snapshot into localisation.
- The Statehood Ledger already exposes dynamic founding values, bands, former-host values, patron influence, network standing, league phase, founding phase, and active mission status through `localisation/english/006_independence_wave_gui_l_english.yml:2-112`; no additional safe static-to-dynamic conversion was identified.
- Scenario outcome, failure reason, type, intensity, territory, force tier, package identifier, country name/tag, and rival-bloc detail are already dynamic in `localisation/english/006_independence_wave_scenario_l_english.yml:34-49` and the scenario scripted-localisation file.
- Evolution 5 uses `independence_wave.evolution.5.body` at `localisation/english/006_independence_wave_evolutions_l_english.yml:12`. Its text mentions dangerous routes and new sovereignty projects. Static source review did not prove whether this body is visible before the World Collapse reveal, so the owning event agent should confirm reveal timing before changing wording.

## Cross-surface mismatch notes

- Event Details and the five evolution title/body pairs are aligned with the current catalog mirror. The runtime Event Details key at `chaosx_gui_l_english.yml:960` appends dynamic rival-bloc lines that are intentionally excluded from the static workbook paragraph.
- SCN-008 scenario names, descriptions, impact paragraphs, ledger labels, and rejection reasons are present and match the current catalog alignment handoff. No wording contradiction was found in the inspected scenario surface.
- The catalog status schema remains a documentation/status mismatch, not a missing localisation key: `Events!M7` and `Clusters!G3` remain `Partially Available`, while `Scenarios!F9` remains `Playable`, and the current whole-event authority remains `HOLD / PARTIAL`. The latest catalog handoff records that these validation-list labels were not changed without an accepted status decision.
- The event-log routing is internally consistent: `chaosx.event_name.6` supplies the event name, `chaosx.events_log.window.event_details.independence_wave` supplies Event Details, and the evolution incident events `chaosx.nr6.360` through `.364` have complete title, description, and option strings.
- No player-facing raw trigger fragment, implementation label, event-target syntax, or working label was found. Hits for words such as `unresolved`, `working`, `draft`, and `implementation` describe in-world institutions or statehood, not process notes.

## File encoding concerns

- All 45 Event 006 English localisation files begin with UTF-8 BOM bytes `EF BB BF` and decode successfully as `utf-8-sig`.
- No scoped key has the forbidden `:0` suffix.
- A proper Unicode scan found zero em-dash characters and zero semicolon characters in the 45 Event 006 localisation values. Eleven ordinary en-dash route-name uses remain and are not encoding defects.

## Recommended fixes with file paths and keys

1. Consider adding unconditional neutral fallback branches to the eight enum selectors listed above. Reuse existing unknown keys where available, and add new `*_unknown` keys only after the owning gameplay agent confirms wording and the value contract. This is a robustness recommendation, not a required admission fix.
2. If scenario readiness counts are player-facing requirements, add a scripted getter for the current allocator/binding summary and use it from `chaosx.scenarios.launch_status.independence_wave.ready` at `localisation/english/006_independence_wave_scenario_l_english.yml:31`. Do not hardcode the current 138/55/13 snapshot.
3. Confirm that `independence_wave.evolution.5.body` is gated behind its intended reveal. If not, replace only the premature route wording after the event owner confirms the public design.
4. Do not change the catalog status strings until the owner resolves whether the workbook validation lists should accept `In progress` and `Needs Testing`.

## Patch and handoff record

- Changed files: only this handoff file.
- Changed localisation keys: none.
- Dynamic localisation added or fixed: none.
- Before/after display behavior: unchanged; this was a read-only audit.
- No gameplay, asset, fallback, or wording simplification was introduced.
- Handoff path: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_localisation_audit_current_v105_2026_08_03.md`.

## Meaningful validation performed

- Parsed all 45 Event 006 English localisation files for BOM, malformed key shape, duplicate keys, `:0` suffixes, raw working labels, em dashes, and semicolons.
- Parsed all English localisation files for global duplicate keys.
- Compared Event 006 event, decision, category, focus, idea, scripted-localisation, and Statehood Ledger references against the global English key set.
- Compared Event 006 scripted-localisation `localization_key` references and custom `[Get...]` calls against the available localisation and scripted-localisation definitions.
- Re-read the current Event 006 completion authority, current catalog alignment handoff, scenario localisation, GUI localisation, event-log mapping, and evolution localisation.

## Skipped meaningful validation and why

- No Hearts of Iron IV launch, live event firing, save/load, GUI render, or Event Log interaction was run because repository policy assigns live consumer validation to the user and this was a static localisation audit.
- No workbook edit/export was required because no catalog wording correction was justified by the current source evidence.

## Unresolved wording decisions

- Whether the enum selectors should receive unconditional neutral fallback text.
- Whether SCN-008 ready-state text should expose dynamic 138/55/13 map-binding counts.
- Whether Evolution 5 wording is public before or only after its World Collapse reveal.
- Whether the workbook status vocabulary should be expanded to represent the current `HOLD / PARTIAL` authority directly.

## Simplifications, omissions, and blockers

No localisation simplification or fallback was introduced. Whole Event 006 remains incomplete for the package-admission, compatible-capacity, formable, asset, AI/balance, `6001`, and runtime-evidence blockers recorded by the current completion authority; those blockers are outside this localisation audit.
