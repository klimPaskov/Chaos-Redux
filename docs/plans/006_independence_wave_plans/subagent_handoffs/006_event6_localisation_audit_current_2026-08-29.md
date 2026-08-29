# Event 006 current localisation audit

Date: 2026-08-29

Mode: read-only audit. This handoff is the only file added by this task.

## Verdict

Event 006 is not localisation-complete in the current source state. The most serious defect is that 1,880 entries in nine dedicated Event 006 localisation files have leading whitespace before the key. This violates the repository localisation contract and the offline localisation reference format. It affects whole decision, leader, GUI, minor-overlay, western, Balkan, Bashkir/Mari, Siberian, Udmurt, Komi, and scripted-localisation result sets.

When keys are normalized by trimming leading whitespace for audit purposes, every explicit Event 006 title, description, name, tooltip, event option, focus, character, and scripted-localisation reference inspected has a matching English value. No duplicate Event 006 key remains after the same normalization. This normalization was diagnostic only and was not written to source.

The event also retains widespread implementation-facing wording, 140 numeric cost strings that do not read script constants dynamically, large repeated prose families, and several exceptionally dense category and effect tooltips. The super-event quotation strings match the approved source handoff and must remain verbatim.

## Scope and references

The audit compared the current implementation with:

- `docs/specs/006_independence_wave_specs/`, especially spec Parts 1 through 7, the candidate registry, decision/mission map, achievement matrix, super-event text research, acceptance checklist, and current simplification notes.
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` and `006_independence_wave_resume_packet.md`.
- Event sources `events/006_independence_wave.txt` and `events/006_independence_wave_support_events.txt`.
- All `localisation/english/006_independence_wave*_l_english.yml` files and the Event 006 portions of `chaosx_gui_l_english.yml`, `chaosx_event_names_l_english.yml`, `chaosx_achievements_l_english.yml`, and `chaosx_formable_state_puzzles_l_english.yml`.
- Event 006 decisions, categories, focuses, characters, achievements, formables, scripted GUI, scripted localisation, scenario, event-log, and super-event selectors.
- The offline Paradox wiki localisation, data-structure, trigger, effect, modifier, scope, event, decision, focus, country, idea, on-action, and AI references, plus installed vanilla documentation.

## Missing key list

### Structurally malformed keys

The following files contain 1,880 indented keys. Their text exists, but the key form is invalid under the repository contract (`key: "Text"` at column one). These entries must be treated as missing/unreliable until the indentation is removed.

| File | Affected keys | Evidence |
| --- | ---: | --- |
| `localisation/english/006_independence_wave_minor_overlay_l_english.yml` | 468 | line 3 `independence_wave_iw005_flanders_category` through line 521 `independence_wave_iw204_restoration_charter_desc` |
| `localisation/english/006_independence_wave_balkan_l_english.yml` | 439 | line 3 `AXX_independence_wave_municipal_charter` through line 485 `independence_wave_tra_network_effect_tt` |
| `localisation/english/006_independence_wave_siberian_l_english.yml` | 333 | line 3 `ALT_independence_wave_constitutional_party` through line 354 `independence_wave_yak_cost_strategic` |
| `localisation/english/006_independence_wave_bashkiria_mari_l_english.yml` | 259 | line 3 `BSK_independence_wave_constitutional_party` through line 272 `independence_wave_mel_focus_open_volga_finnic_corridor` |
| `localisation/english/006_independence_wave_western_l_english.yml` | 208 | line 3 `BRI_independence_wave_civic_delegate` through line 234 `independence_wave_ice_north_atlantic_category_desc` |
| `localisation/english/006_independence_wave_gui_l_english.yml` | 101 | line 2 `independence_wave_status_gui_title` through line 102 `independence_wave_gui_mission_none` |
| `localisation/english/006_independence_wave_udm_l_english.yml` | 66 | line 2 `independence_wave_udm_industrial_forest_category` through line 67 `UDM_independence_wave_emergency_party_long` |
| `localisation/english/006_independence_wave_decisions_l_english.yml` | 4 | lines 276-279, the resolved/fallback former-host name selectors |
| `localisation/english/006_independence_wave_komi_l_english.yml` | 2 | lines 55-56, `independence_wave_komi_cost_strategic` and `_blocked` |

Direct consequences include 682 explicit decision/category name or description references, 13 character name/description keys, two western package character names, and the entire 101-key Statehood Ledger GUI text set relying on indented entries. Representative consumers include:

- `common/characters/006_independence_wave_characters_registry.txt:78` -> `AXX_independence_wave_banat_presidium`, whose indented value is at `006_independence_wave_balkan_l_english.yml:65`.
- `common/characters/006_independence_wave_characters_registry.txt:792` -> `MNT_independence_wave_mitar_martinovic`, whose indented value is at `006_independence_wave_balkan_l_english.yml:354`.
- `common/decisions/006_independence_wave_balkan_decisions.txt:1626-1627` -> `independence_wave_tra_codify_danube_settlement` and `_desc`, whose indented values are at `006_independence_wave_balkan_l_english.yml:473-474`.
- `common/scripted_localisation/006_independence_wave_scripted_localisation_registry.txt:1440-1535` -> the Statehood Ledger band, phase, host, patron, and mission strings, all currently indented in `006_independence_wave_gui_l_english.yml`.

### Actually absent keys after diagnostic normalization

None found among explicit references. The audit resolved all explicit event title/description/option keys, decision/category name/description/tooltips, 319 focus IDs, character name/description references, and Event 006 scripted-localisation branch keys after trimming indentation only for comparison. `independence_wave_focus_tree` has no `_desc`, which is normal for a focus-tree identifier rather than a focus.

Seventeen deliberately dormant reserved tags have no country-name localisation because they are fail-closed research reservations: DJX, DMX, DNX, ENX, EXX, EYX, FPX, GDX, GGX, GHX, GLX, HHX, HMX, HQX, HTX, HWX, and HXX. Their inert mapping is explicit in `common/country_tags/006_independence_wave_countries.txt:50-117`. This is not a current missing-key defect unless another change makes one of those tags visible or playable.

## Duplicate key list

No duplicate Event 006 English key was found after normalizing leading whitespace. This check included every English localisation file, not only files named for Event 006.

## Scripted localisation issues

1. Seventy `localization_key` branches in `common/scripted_localisation/006_independence_wave_scripted_localisation_registry.txt` depend on indented entries and are therefore structurally unsafe. The affected groups are:
   - former-host resolved and fallback names at lines 242-258;
   - IW-005 institutional status at lines 439-449;
   - league-phase results at lines 462-512;
   - Statehood Ledger legitimacy, recognition, capacity, security, instability, founding phase, host status, patron status/name, and mission status at lines 1440-1535.
2. All other Event 006 `localization_key` branches inspected resolve after diagnostic whitespace normalization. No broken selector name or missing fallback branch was confirmed in source.
3. The scenario selector still defines package-ID display strings at `localisation/english/006_independence_wave_scenario_l_english.yml:64-66`, even though the current scenario text no longer displays them. They are compatibility leftovers rather than active player text and should be removed only after confirming no external consumer remains.
4. No raw `§` or `£` formatting character was found inside the scripted-localisation source itself. Formatting remains in ordinary YML values, where it is allowed.

## Dynamic text opportunities and cost disclosure

The audit found 140 numeric cost-localisation keys without a `[?constant:...]` token. They are concentrated in:

- `006_independence_wave_iw043_iw058_l_english.yml`: 78 keys, especially lines 303-338 and 426-467;
- `006_independence_wave_iw093_iw098_l_english.yml`: 39 keys, especially lines 47-67 and 133 onward;
- `006_independence_wave_transcaucasus_l_english.yml`: 22 keys;
- `006_independence_wave_form03_l_english.yml:208`: one tooltip wrapper with a numeric label.

Representative static triplets include `independence_wave_iw043_cost_guard`, `_blocked`, and `_tooltip` at `006_independence_wave_iw043_iw058_l_english.yml:321-323`, and `independence_wave_iw098_cost_cavalry_screen`, `_blocked`, and `_tooltip` at `006_independence_wave_iw093_iw098_l_english.yml:133-135`. These should use the current script constants or existing cost selectors so the visible, blocked, and explanatory forms cannot drift apart.

Additional opportunities:

- `006_independence_wave_l_english.yml:98-102` describes the voluntary transition with “at least half” while the Event Details surface uses dynamic reduction and state-count constants. The popup should use the same dynamic thresholds or a selector derived from the actual eligibility result.
- `006_independence_wave_transcaucasus_l_english.yml:99` says a project applies its “configured minor, standard, or major ledger gain.” This is tuning language and does not tell the player what their selected action will change. Use the action's actual dynamic values.
- `006_independence_wave_scotland_wales_l_english.yml:117-122` says “package authority” and “package-specific national spirit.” Replace those implementation categories with the current country, government, and visible spirit names.
- `006_independence_wave_decisions_l_english.yml:267` says “valid future candidate” and “next release plan.” Use the selected movement/country and its concrete preparation consequences.

## Cross-surface mismatch notes

1. Event Details are aligned: `chaosx.events_log.window.event_details.independence_wave` at `chaosx_gui_l_english.yml:1074` matches Event 006 `Details` in the catalog export, including both rival-bloc selectors.
2. Evolution title/body selectors in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:2783-2814`, `3892-3911`, `7401-7420`, and `8158-8654` point to the same `independence_wave.evolution.*` keys used in the catalog. The five exported evolution bodies match `006_independence_wave_evolution_l_english.yml:10-22`.
3. The Liberations cluster description matches between `chaosx_gui_l_english.yml:418` and the cluster catalog export.
4. The cluster workbook/export member field is stale or malformed: `docs/spreadsheets/chaos_redux_clusters_catalog.csv` lists `Members (ID): 5, 6, 6, 6`, while the source spec and acceptance checklist describe the Liberations cluster as Events 5 and 6. The editable workbook must be corrected, then exports regenerated. Do not edit the CSV directly.
5. SCN-008 name, Sovereign Scatter description, type list, and four intensity descriptions match `006_independence_wave_scenario_l_english.yml:2-26` and the scenario catalog export.
6. Current country names were compared with the candidate registry. Nine differences from its explicitly non-final `working_name_not_final_localisation` field were found: BWX, CJX, DAX, DBX, EMX, GRX, HDX, HGX, and HKX. Their current names are more resolved and specific, and no stale-name defect was confirmed from that comparison.
7. The Event 006 achievement source at `common/achievements/chaos_redux_achievements.txt:622-707` resolves to the name, description, and tooltip set in `006_independence_wave_l_english.yml:124-188`. The empty Event 006 marker in `chaosx_achievements_l_english.yml:328-329` is only a historical registry marker, not an absent achievement set.

## Pre-event wording audit

No active pre-event crisis localisation surface was confirmed. `python .tools/audit_event6_allocator.py` reports the crisis category, mission, cost, and queue retired, and the current source-of-truth map records the global runtime gate for the 13 living overlay families.

However, `006_independence_wave_l_english.yml:29-95` contains dozens of internal collection labels such as “Event 006 Owned New Tags,” “Selectable Unbound Carriers,” “Overlay Route Carriers,” and regional registry names. They are working labels, not in-world text. They should remain hidden from ordinary player surfaces or receive a separate developer-only namespace. MCP rendering was unavailable, so their visibility could not be proven.

## Prose-quality issue list

### Vagueness and mechanically opaque wording

- `006_independence_wave_transcaucasus_l_english.yml:99` uses “configured minor, standard, or major ledger gain,” which exposes tuning categories without the actual result.
- `006_independence_wave_scotland_wales_l_english.yml:117-122` uses “package authority,” “selected shared route,” and “package-specific national spirit.” These are implementation abstractions rather than country-facing consequences.
- `006_independence_wave_frontier_l_english.yml:57` and similar host-loss strings say the ledger “closes locally” and that “no bilateral host values change.” This describes script bookkeeping instead of the political situation.

### Bloat

- `006_independence_wave_ruthenia_l_english.yml:121` (`independence_wave_rut_network_effect_tt`) is 1,073 characters and combines many unrelated effects in one tooltip.
- `006_independence_wave_kosovo_l_english.yml:92` and `:99` are 986 and 992 characters.
- `006_independence_wave_balkan_l_english.yml:332` and `:339` are 1,015 and 976 characters.
- `006_independence_wave_scenario_l_english.yml:34` (`chaosx.triggerable_scenarios.80.d`) is 944 characters before any resolved dynamic text.
- The 1,510-character Iceland category description at `006_independence_wave_western_l_english.yml:234` is a dashboard and therefore needs substantial data, but it still requires a production render to prove wrapping and hierarchy.

### Obvious explanation

- `006_independence_wave_scenario_l_english.yml:59-63` repeats the previous, next, and close button actions in each description. The descriptions add almost no requirement or consequence beyond the titles.
- Several tooltip pairs repeat the same text under both an action and `_effect_tt`, for example `006_independence_wave_form03_l_english.yml:109-110`, `:113-114`, and `:121-122`.

### Repetition and generic route voice

- The exact community-council description is reused across Banat, Epirus, Macedonia, and Thrace at `006_independence_wave_balkan_l_english.yml:38`, `:170`, `:242`, and `:393`.
- The network-corridor description is reused across seven Balkan routes at lines 54, 120, 186, 258, 326, 409, and 476.
- “Put the emergency chain of command...” is reused across six packages at lines 48, 114, 180, 252, 403, and 470.
- Numerous Siberian, frontier, Ruthenian, and Tatar route spirits reuse the same council, agrarian, host-loss, sovereignty, and emergency-command prose. This makes distinct peoples and routes read like reskinned templates.

### Overcomplication

- `006_independence_wave_transcaucasus_l_english.yml:5` compresses three live ledgers, two thresholds, member requirements, multiple route requirements, and three capital-control requirements into one paragraph.
- `006_independence_wave_form03_l_english.yml:124-126` repeatedly explains sovereign-member status, federal language scope, two values, and a ratification window across description and tooltip.
- `006_independence_wave_iw043_iw058_l_english.yml:780` and `:818` stack long lists of guarantees, institutions, consent conditions, and staged integration into single sentences.

### Style-rule repair needed

- No em dash or semicolon was found in the dedicated Event 006 localisation files.
- Implementation words still appear in player text: “receipt” at `006_independence_wave_transcaucasus_l_english.yml:16`, `:27`, `:38`, `:97`, and `:101`; “synchronized transaction” and “generic target” at `006_independence_wave_decisions_l_english.yml:271-273`; “accession receipt” at `006_independence_wave_iw043_iw058_l_english.yml:570`; and “package” wording at `006_independence_wave_scotland_wales_l_english.yml:117-122`.
- These should be rewritten as completed arbitration, recorded consent, coordinated military action, government authority, or the actual institution named by the route.

## Sourced-quotation preservation notes

The following quotation-bearing surfaces were inspected and match the approved text verification exactly:

- `006_independence_wave_l_english.yml:115`, Wilson Point XIV excerpt and attribution for super-event 23.
- `006_independence_wave_l_english.yml:119`, Hosea 8:7 KJV excerpt and attribution for super-event 24.

Their titles, descriptions, buttons, and quote strings match `docs/plans/006_independence_wave_plans/super_event_research/006_super_event_text_verification.md:98-101` and `:136-139`. Do not modernize, shorten, or repunctuate the quotations during the later prose pass. The button “They have sown the wind.” is documented as a source-derived allusion and should also be preserved unless the source handoff is revised.

No other attributed quotation was found in the dedicated Event 006 English localisation set.

## File encoding concerns

All 41 inspected Event 006/shared English files have an UTF-8 BOM and begin with `l_english:`. No encoding failure was found. The leading-key indentation is a format problem independent of BOM encoding.

## MCP evidence and exact blocker

Required Event, focus-tree, and GUI MCP inspection/render routes were unavailable in this agent runtime. The callable tool registry exposed no `hoi4_agent_tools`, `hoi4.event_inspect`, `hoi4.event_render`, `hoi4.focus_inspect`, `hoi4.focus_render`, `hoi4.gui_inspect`, or `hoi4.gui_render` route. Therefore:

- no production render could verify the 1,510-character Iceland category, 1,091-character Pacific Federation category, 944-character SCN-008 summary, or Event 006 status GUI for clipping and wrapping;
- no event/focus artifact URI was produced;
- source review and validators are not presented as equivalent engine evidence.

The current source-of-truth map separately records earlier MCP attempts as partial or blocked by `ARTIFACT_MANIFEST_INTEGRITY_FAILED`; this audit did not receive a callable route with which to reproduce or supersede that evidence.

## Validation run

- Explicit localisation-reference audit: zero actually absent keys after diagnostic whitespace normalization; 1,880 malformed indented keys without normalization.
- Duplicate audit across all English files: zero duplicate Event 006 keys after whitespace normalization.
- Scripted-localisation branch audit: 70 Event 006 registry branches depend on indented keys; zero actually absent branch values after normalization.
- Focus coverage audit: 319 focus IDs inspected; all focus names and descriptions resolve, excluding the normal tree identifier without `_desc`.
- BOM/header audit: 41 inspected Event 006/shared files all have UTF-8 BOM and `l_english:`.
- `python .tools/audit_event6_allocator.py`: passed, including the retired pre-event crisis surface.
- `python .tools/audit_event6_country_api.py`: passed with no missing or duplicate country API entries.
- `python .tools/audit_event6_flags.py`: passed for all 102 registered tag flag families.
- `python .tools/audit_event6_form16.py`: passed.
- `python .tools/audit_event6_gui_matrix.py`: passed semantic source coverage but explicitly does not claim runtime rendering.
- `python .tools/audit_event6_scenario_matrix.py`: passed all 32 scenario cells and eight edge cases.

## Recommended fixes

1. First run a bounded mechanical patch that removes leading whitespace before all 1,880 keys in the nine files listed above. Do not rewrite their values in the same change. Re-run explicit reference, duplicate, and scripted-localisation coverage checks afterward.
2. Re-run the required Event, focus, and GUI MCP inspections/renders once the server route is available. Treat every visible clipping or wrapping defect as a source defect.
3. Replace the 140 hardcoded numeric cost strings with current script constants or existing dynamic cost selectors. Compare each visible/blocked/tooltip triplet with its decision payment effect.
4. Rewrite the implementation-facing receipt, package, transaction, generic-target, and configured-gain text cited above while preserving gameplay meaning and dynamic tokens.
5. Split the longest effect tooltips into requirement, cost, and consequence blocks where their consumer supports line breaks. Do not remove concrete values.
6. Give repeated Balkan and Siberian route descriptions country-specific institutions, places, actors, and material consequences. This is a broad writing pass and should be reviewed route by route, not bulk-generated.
7. Correct the Liberations `Members (ID)` cell in `docs/spreadsheets/chaos_redux_events_catalog.xlsx` or the appropriate Clusters sheet to the intended Event 5/Event 6 membership, then run `python .tools/export_event_catalog_csv.py`.
8. Keep the two sourced super-event quotations and the Hosea-derived button unchanged.

## Skipped meaningful validation

- Production event, focus, and GUI MCP rendering: blocked because no HOI4 MCP route was callable in this runtime.
- Live in-game text display: belongs to the user and was not attempted.
- Workbook visual inspection: the task was a localisation audit, and the export rows were sufficient to identify the cluster-member mismatch. The workbook itself was not edited.

## Unresolved wording decisions

- Whether “ledger” is an in-world institution or implementation shorthand varies by package. Public account books, customs ledgers, and shipping registers can remain. “The former-host ledger closes locally,” “league ledger is active,” and similar state-machine phrases should be rewritten.
- The internal collection labels at `006_independence_wave_l_english.yml:29-95` may be acceptable in developer tooling but are not acceptable in ordinary player UI. Their actual visibility needs MCP or live-consumer evidence.
- The 17 dormant reservation tags should remain unlocalised only while their fail-closed visibility is guaranteed.

## Changes made

- Added this audit handoff only.
- No gameplay, localisation, scripted localisation, GUI, focus, decision, country, achievement, scenario, super-event, workbook, or export file was changed.

## Simplifications, omissions, and blockers

No prose or key fix was applied because the assigned mode was read-only except for this handoff. The MCP visibility/overflow portion remains blocked by the unavailable HOI4 MCP routes. No unapproved fallback or invented replacement text was used.
