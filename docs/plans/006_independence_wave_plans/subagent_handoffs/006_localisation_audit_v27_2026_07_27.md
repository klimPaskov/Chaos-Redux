# Event 006 localisation audit v27

Audit date: 2026-07-27.

Audit basis: current worktree after the parent Event 006 localisation additions, including the uncommitted FORM-05 cost triplets. The scoped English surface contains 34 `006_*_l_english.yml` files and 5,717 parsed key rows.

## Verdict

**PASS for the bounded localisation audit.** The two narrow patches below remove the remaining Event 006 implementation-label leaks and a sentence-punctuation issue. This localisation result does not clear the wider Event 006 package, runtime, asset, or live-consumer HOLD recorded by the source-of-truth documents.

## Missing key list

- **PASS: none in the 34 scoped Event 006 English YML files.** The scoped key scan found 5,717 unique rows and no unresolved duplicate or key-shape issue.
- **PASS: event surface.** The Event 006 event source contains 51 unique `title`, `desc`, `name`, and custom-tooltip localisation references, all resolved in the full English set.
- **PASS: decision surface.** The 1,400 scoped `name`, `desc`, `custom_cost_text`, and custom-tooltip references represent 1,106 unique keys, all resolved in the full English set.
- **PASS: custom-effect tooltips.** The current Event 006 source scan found 837 references and 776 unique keys, with no missing full-English targets.
- **PASS: scripted localisation targets.** The ten `common/scripted_localisation/006_*` files contain 100 `localization_key` references and 94 unique targets. Four shared scenario-intensity keys sit outside the 34 scoped files, but all four resolve in `localisation/english/chaosx_gui_l_english.yml`.
- **PASS: focus IDs.** The 309 Event 006 focus IDs all have base localisation keys. The only generated `_desc` false positive is the focus-tree container ID `independence_wave_focus_tree`, which does not require a player-facing focus description key.

## Duplicate key list

- **PASS: none.** The 34-file scan found zero duplicate localisation keys.

## Scripted localisation issue list

- **PASS: `GetIndependenceWaveLeaguePhase` is complete and wired.** Its thirteen phase branches and fallback resolve to named labels, and the Statehood Ledger calls the selector rather than exposing a raw phase value.
- **PASS: `GetIndependenceWaveSelectedFormableName` covers the registered family branches, including the West African Federation, Sahel Confederation, and Melanesian Federation.** Its explicit `independence_wave_formable_name_unknown` fallback remains a fail-closed runtime guard and was not changed.
- **PASS: no raw trigger fragments are exposed.** The scoped values contain no `check_variable`, `has_*`, `NOT =`, `custom_effect_tooltip`, `custom_trigger_tooltip`, or scripted-effect fragments.

## Dynamic text opportunities

- **PASS: no new bounded opportunity was found.** The Statehood Ledger uses named league-phase, actor, and patron selectors. Scenario summaries and ledger package identifiers use dynamic values. Event 006 custom costs retain dynamic constant tokens and complete base, tooltip, and blocked text.
- The former FORM-24 and FORM-25 focus tooltips exposed internal decision IDs and implementation wording. They now use the registered family names and player-facing preparation wording while retaining the same unlock meaning.

## Custom costs

- **PASS: all 334 Event 006 `custom_cost_text` references are covered.** They represent 104 unique base keys, and every base key has a matching `_tooltip` and `_blocked` key in the current English set.
- No scoped cost triplet value is empty. The parent FORM-05 additions remain intact and are included in this count.

## Working-label and punctuation findings

- **FIXED:** `independence_wave_iw093_prepare_form24_west_african_federation` and its `_tt` key now say "West African Federation" rather than `FORM-24`, and `independence_wave_iw098_prepare_form25_sahel_confederation` and its `_tt` key now say "Sahel Confederation" rather than `FORM-25`.
- **FIXED:** `independence_wave_form39_invitation_category_desc` no longer uses a semicolon between player-facing sentences.
- **PASS:** no `FORM-[0-9]+` or `IW-[0-9]+` implementation labels remain in scoped localisation values. The retained `SCN-008` and dynamic `IW-00x` package identifiers belong to the scenario ledger and are intentionally player-visible registry labels.
- **PASS:** no semicolon or em-dash values remain. Seven en-dashes remain only in intentional compound labels such as Kazan-Cheboksary, Church-Civic, and Mountain-River.

## Cross-surface mismatch notes

- **PASS:** the Event 006 catalog-facing name remains `Independence Wave`, and the Event Details paragraph and five evolution titles and bodies remain aligned with the Event 006 row in `docs/spreadsheets/chaos_redux_events_catalog.csv`. The event-log localisation appends dynamic rival-bloc detail lines by design. No workbook wording changed, so no workbook export was required.
- **PASS:** the SCN-008 ready sentence remains aligned with the documented 138 bound, 55 unbound, and 13 overlay package split. Keep it synchronized if the package-binding ledger changes.
- **PASS:** the formable family display names and the IW-093/IW-098 focus labels now agree on West African Federation and Sahel Confederation.
- **PASS:** the Event 006 advisor-art prohibition is preserved. No advisor portrait, sprite, custom art, or asset localisation was added. The `006_independence_wave_nwe_advisors_l_english.yml` file remains role and description text only. Other "asset ledger" matches are in-world property wording, not advisor art.

## File encoding concerns

- **PASS:** all 34 scoped Event 006 English YML files begin with UTF-8 BOM bytes `EF BB BF`, decode as UTF-8, and contain no forbidden `:0` key suffix.
- The BOM was preserved in both touched localisation files.

## Recommended fixes

- No further bounded localisation patch is required.
- Parent runtime review should confirm that `independence_wave_formable_name_unknown` cannot appear for a valid player-facing family and that the queued FORM-24 and FORM-25 decision surfaces remain gated as intended.
- Keep SCN-008 counts and catalog-facing evolution wording synchronized with their source rows and package-binding ledger.

## Patch and handoff record

- **Changed files:**
  - `localisation/english/006_independence_wave_formable_registry_l_english.yml`
  - `localisation/english/006_independence_wave_iw093_iw098_focus_l_english.yml`
- **Changed keys:**
  - `independence_wave_form39_invitation_category_desc`
  - `independence_wave_iw093_prepare_form24_west_african_federation`
  - `independence_wave_iw093_prepare_form24_west_african_federation_tt`
  - `independence_wave_iw098_prepare_form25_sahel_confederation`
  - `independence_wave_iw098_prepare_form25_sahel_confederation_tt`
- **Dynamic localisation added or fixed:** no new scripted-localisation branch was needed. Existing phase, actor, patron, scenario, and cost selectors were verified. The two focus tooltip strings now use player-facing family names instead of internal IDs.
- **Before and after display behavior:** the FORM-39 invitation description now uses two sentences with the same meaning. The IW-093 and IW-098 focus labels and tooltips no longer show FORM-24 or FORM-25, and now name the corresponding regional project while retaining the preparation and paid-decision behavior.
- **Fallbacks or simplifications introduced:** none.
- **Unresolved wording decisions:** none in the bounded localisation surface. The unknown-formable fallback visibility is a runtime guard concern and remains intentionally fail-closed.
- **Plan handoff path:** this file.

## Meaningful validation

- Parsed all 34 scoped YML files for BOM, UTF-8 decoding, duplicate keys, `:0` suffixes, semicolon and em-dash punctuation, implementation-label leakage, and key count.
- Compared Event 006 event, decision, focus, custom-tooltip, scripted-localisation, and custom-cost references against the complete English key set.
- Rechecked all 104 Event 006 custom-cost bases for base, `_tooltip`, and `_blocked` coverage.
- Rechecked the Event Details and evolution names against the Event 006 catalog row and preserved the documented SCN-008 counts.

## Skipped meaningful validation

- No Hearts of Iron IV process, live GUI playback, Event Log playback, or game save validation was run. This was a source-level localisation audit, and live consumer validation remains with the parent and user.
- No workbook edit or CSV export was run because the catalog-facing Event 006 wording did not change.
