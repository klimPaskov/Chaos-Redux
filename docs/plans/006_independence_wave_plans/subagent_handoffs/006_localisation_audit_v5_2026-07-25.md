# Event 006 localisation audit v5

Audit date: 2026-07-25.

Scope: read-only audit of Event 006 Independence Wave localisation, linked scripted localisation, Event Log selectors, Statehood Ledger GUI text, SCN-008 scenario text, super-event text, and current source-of-truth counts.

## Verdict

**HOLD for a clean localisation closeout.** Key coverage, duplicate-key hygiene, scripted-localisation resolution, custom-cost coverage, Event Log wiring, and UTF-8 BOM checks pass. The current SCN-008 launch-status sentence is stale against the canonical 206-row registry and the Event 006 writing rules are violated by 39 semicolon/em-dash values, including one evolution body that exposes hidden-route categories. No gameplay or localisation file was patched by this audit.

## Missing key list

- **PASS: none found in the scoped Event 006 surfaces.** All Event 006 decision `name`/`desc` keys, focus IDs and descriptions, event titles/descriptions/options, Statehood Ledger interface text and tooltips, and shared Event Details/event-name keys resolve in the complete English localisation set.
- **PASS: no missing scripted-localisation targets.** The ten `common/scripted_localisation/006_independence_wave*.txt` files contain 100 `localization_key` references and every reference resolves.
- **PASS: no missing custom-effect tooltip keys.** The 124 Event 006 gameplay source files contain 688 `custom_effect_tooltip` references and every Event 006 tooltip key resolves; the two `generic_skip_one_line_tt` references in the vanilla-compatibility file are intentionally outside this Event 006 localisation scope.
- **PASS: no missing custom-cost pair.** All 321 Event 006 `custom_cost_text` references have a base key, a `_tooltip` key, and a `_blocked` key.

## Duplicate key list

- **PASS: none.** A repository-wide English scan excluding the intentional `l_english` file headers found zero duplicate groups involving any Event 006 key.

## Scripted localisation issue list

- **PASS: no undefined Event 006 `Get...` names.** Every scripted-localisation getter referenced by Event 006 English values or the shared Event Details surface is defined in `common/scripted_localisation/`.
- **PASS: no unresolved Event Log selector keys.** The Event Log maps Event 006 evolution type, all five evolution titles and bodies, the evolution summary, the danger-milestone title and description, the generic Event Details description, and the Event 006 event name to existing localisation.
- **PASS: rival-bloc Event Details has safe dynamic fallbacks.** `GetIndependenceWaveRivalBlocEventDetails` and `GetIndependenceWaveRivalBlocEventDetailsMember` return active, leaderless, inactive, selected-member, first-member, or no-member text as appropriate in `common/scripted_localisation/006_independence_wave_rival_bloc_scripted_localisation.txt:23-58`.
- **PASS: no raw trigger fragments were found in scoped player-facing values.** The scan found no `has_`, `check_variable`, `NOT =`, country-flag, or equivalent script fragment exposed as prose.
- **OPEN dynamic opportunity: no human-readable league-phase getter exists.** `localisation/english/006_independence_wave_gui_l_english.yml:17` prints `League phase: [?global.independence_wave_league_phase|0]`, while `common/script_constants/006_independence_wave_mechanics_constants.txt:311-326` defines thirteen named phase values and `common/scripted_localisation/006_independence_wave_gui_scripted_localisation.txt` has no `GetIndependenceWaveLeaguePhase` equivalent.

## Dynamic text opportunities and wording findings

1. **SCN-008 ready status is stale and must be corrected.** `localisation/english/006_independence_wave_scenario_l_english.yml:31` says “all 149 current-map-bound registry packages” and “57 packages without unique current-map bindings.” The canonical registry has 206 rows, while `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md:104` and `006_independence_wave_resume_packet.md:75-77` define 138 selectable bound packages, 55 selectable unbound packages, and 13 overlay rows; the allocator audit separately reports 149 publishers, 126 automatic/high-chaos candidates, and 138 SCN-008 ranked packages. The current sentence conflates planning-publisher counts with selectable-map counts and should use the canonical 138/55/13 split or a dynamic count surface.
2. **Evolution 5 may reveal hidden routes too early.** `localisation/english/006_independence_wave_evolutions_l_english.yml:12` names “Hidden unions, radical sovereignty projects, reclamation campaigns, and ambitious sponsor-backed states” in a player-facing evolution body. The event skill forbids exposing hidden routes or future surprises in public history text; either keep this as an explicitly post-World-Collapse reveal or replace the category list with non-spoiler language.
3. **The Statehood Ledger patron line violates the punctuation rule.** `localisation/english/006_independence_wave_gui_l_english.yml:15` uses an em dash between the dynamic patron name and influence value; use a colon, comma, or separate line if this surface is retained.
4. **The Event 006 report network fallback violates the punctuation rule.** `localisation/english/006_independence_wave_l_english.yml:12` uses a semicolon in `independence_wave_presentation_network_first`.
5. **The full scoped Event 006 English set contains 39 style violations under the event skill’s “no em dash or semicolons” rule.** The exact key groups are `006_independence_wave_brittany_l_english.yml:79` (`independence_wave_bri_celtic_congress_effect_tt`); `006_independence_wave_decisions_l_english.yml:58,126,168,170,188,218` (`independence_wave_cost_pacific_island_strategic_tooltip`, `independence_wave_raise_emergency_units_desc`, `independence_wave_request_border_arbitration_desc`, `independence_wave_rescue_threatened_member_desc`, `independence_wave_request_charter_war_mandate_desc`, `independence_wave_coordinate_reclamation_fronts_desc`); `006_independence_wave_evolutions_l_english.yml:12` (`independence_wave.evolution.5.body`); `006_independence_wave_form01_02_04_l_english.yml:79,148,169` (`independence_wave_form01_ratify_celtic_compact_desc`, `chaosx.nr6.330.d`, `chaosx.nr6.342.d`); `006_independence_wave_gui_l_english.yml:15` (`independence_wave_status_gui_patron`); `006_independence_wave_iw043_iw058_decisions_l_english.yml:260` (`independence_wave_iw058_ratify_sovereign_autonomy_compact_desc`); `006_independence_wave_iw043_iw058_events_l_english.yml:199,213` (`chaosx.nr006.4311.desc`, `chaosx.nr006.5811.desc`); `006_independence_wave_iw093_iw098_focus_l_english.yml:55,64,128,131` (`independence_wave_iw093_proclaim_sovereign_asante_confederacy_tt`, `independence_wave_iw093_prepare_form24_west_african_federation_tt`, `independence_wave_iw098_authorize_frontier_command_tt`, `independence_wave_iw098_prepare_form25_sahel_confederation_tt`); `006_independence_wave_l_english.yml:12` (`independence_wave_presentation_network_first`); `006_independence_wave_pacific_l_english.yml:117,154,190,199,208` (`independence_wave_cost_pacific_island_strategic`, `independence_wave_haw_settle_base_and_property_accounts_focus_desc`, `independence_wave_form48_convoy_defense_deadline_desc`, `independence_wave_form48_procurement_deadline_desc`, `independence_wave_form48_basing_deadline_desc`); `006_independence_wave_rhineland_bavaria_l_english.yml:89,120,143,145` (`independence_wave_rhi_entrust_workers_councils_desc`, `independence_wave_bay_restore_the_crown_desc`, `independence_wave_rhi_high_chaos_effect_tt`, `independence_wave_bay_high_chaos_effect_tt`); `006_independence_wave_rival_bloc_l_english.yml:57` (`independence_wave_rival_bloc_challenge_leadership_desc`); `006_independence_wave_saar_l_english.yml:49` (`independence_wave_ajx_saar_category_desc`); `006_independence_wave_scenario_l_english.yml:8-10,14-15,17,21,49` (three Universal Belligerence titles, four scenario descriptions, and `independence_wave_scenario_ledger_category_desc`); and `006_independence_wave_scotland_wales_l_english.yml:133` (`independence_wave_sco_settle_crown_and_convention_focus_desc`).

## Cross-surface mismatch notes

- **Current Event 006 documentation counts are reconciled.** `docs/events/006_independence_wave/overview.md:13-23`, `006_source_of_truth_map.md:104`, and `006_independence_wave_resume_packet.md:11,75-77,95-107` consistently describe the ten attested IDs, 149 publishers, 126 automatic/high-chaos candidates, 138 SCN-008 ranked packages, and 138/55/13 map-binding split; the older runtime-count warning in `006_localisation_audit_decision_focus_treasury_2026-07-25.md` is superseded and should not be repeated.
- **Scenario launch status remains the live mismatch.** The ready key still presents the superseded 149/57 split even though the current docs and binding CSV use 138/55 selectable packages plus 13 overlays.
- **Event Details wording is intentionally non-spoiler and aligned.** `localisation/english/chaosx_gui_l_english.yml:956` describes the synchronized wave, surviving hosts, recognition, institutions, forces, borders, and patrons, then appends guarded rival-bloc dynamic detail; this matches the current Event Details description in `docs/events/006_independence_wave/overview.md` and does not expose registry or attestation mechanics.
- **Main report wording is dynamically aligned.** `localisation/english/006_independence_wave_l_english.yml:3` uses the presentation country count and armed, region, host, and network getters, and `chaosx.event_name.6` remains “Independence Wave” at `localisation/english/chaosx_event_names_l_english.yml:8`.
- **No source-level mismatch remains for the previously reported DM-58 or reclamation-focus wording.** The current decision description at `006_independence_wave_decisions_l_english.yml:220` describes claim-connected finite fronts and crisis outcomes, the complete/failure/timeout keys are at `:219-221`, and the focus tooltip at `006_independence_wave_focus_l_english.yml:384` explicitly authorizes the paid mission.

## File encoding concerns

- **PASS: all 34 Event 006 English YML files are UTF-8 with BOM.** Every file begins with bytes `EF BB BF`, `utf-8-sig` decoding succeeds, no scoped key uses the forbidden `:0` suffix, and the shared `chaosx_gui_l_english.yml` and `chaosx_event_names_l_english.yml` files also carry BOM bytes.
- **No encoding repair was made.** The three unrelated working-tree localisation changes in `006_independence_wave_form01_02_04_l_english.yml`, `006_independence_wave_form05_l_english.yml`, and `006_independence_wave_pacific_l_english.yml` were preserved and not rewritten.

## Recommended fixes with paths and keys

1. Update `chaosx.scenarios.launch_status.independence_wave.ready` in `localisation/english/006_independence_wave_scenario_l_english.yml:31` to describe 138 selectable bound packages, 55 selectable unbound packages, and 13 overlays, or route those counts through scripted localisation sourced from the allocator ledger.
2. Add a named league-phase scripted getter in `common/scripted_localisation/006_independence_wave_gui_scripted_localisation.txt` and replace the raw `global.independence_wave_league_phase` number in `independence_wave_status_gui_network` at `localisation/english/006_independence_wave_gui_l_english.yml:17`.
3. Decide whether Evolution 5 is a post-reveal surface; if it is public before World Collapse, revise `independence_wave.evolution.5.body` at `localisation/english/006_independence_wave_evolutions_l_english.yml:12` to avoid listing hidden route families.
4. Replace the 39 semicolon/em-dash values listed above with periods, commas, colons, or separate sentences while preserving mechanics and dynamic tokens.
5. Keep the current DM-58, reclamation-focus, treasury, Event Details, and Event Log wording unless gameplay owners change the linked source behavior; their earlier audit findings are closed in the current tree.

## Patch and handoff record

- **Changed files:** only this dated handoff file, `docs/plans/006_independence_wave_plans/subagent_handoffs/006_localisation_audit_v5_2026-07-25.md`.
- **Changed localisation keys:** none.
- **Dynamic localisation added or fixed:** none; this was explicitly read-only.
- **Before/after display behavior:** unchanged by this subagent; the handoff records current source behavior and recommended owner fixes.
- **Fallbacks or simplifications introduced:** none.
- **Plan handoff path:** no separate implementation plan was written because the remaining issues are bounded localisation/source-of-truth fixes for the parent-owned Event 006 surfaces.

## Validation run

- Scanned 34 Event 006 English YMLs plus the shared Event Details and event-name files for BOM, malformed key shape, `:0` suffixes, and duplicate keys.
- Compared 100 Event 006 scripted-localisation `localization_key` references, 688 Event 006 custom-effect tooltip references, and 321 custom-cost references with the English key set.
- Compared all Statehood Ledger interface `text`, `buttonText`, and `pdx_tooltip` references in `interface/006_independence_wave.gui`; all 36 references resolve.
- Re-read the current registry and binding CSVs and the source-of-truth/resume documents to reproduce the 206-row, 138/55/13 split and the 149/126/138 allocator counts.
- Re-read the Event Log scripted-localisation selectors for Event 006 evolution, danger-milestone, generic Event Details, and event-name routing.
- No Hearts of Iron IV process was launched and no live consumer validation was run, as repository instructions assign in-game validation to the user.

## Skipped meaningful validation and why

- No GUI render or live Event Log playback was run because the parent requested a read-only source audit and no linked read-only artifact was supplied.
- No localisation patch was applied because the parent explicitly reserved gameplay/localisation edits and requested the dated handoff only.

## Unresolved wording decisions

- Whether SCN-008 ready status should expose the 138/55/13 canonical map-binding split or use a dynamic summary getter.
- Whether Evolution 5’s hidden-route categories are acceptable only after its World Collapse reveal or should be made non-spoiler.
- Which human-readable labels should be used for the thirteen league phases in the Statehood Ledger.
- Whether all 39 punctuation violations should be corrected in one mechanical localisation pass or staged by regional tranche.
