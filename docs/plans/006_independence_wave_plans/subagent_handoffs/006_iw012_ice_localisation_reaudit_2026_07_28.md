# Event 006 IW-012 Iceland localisation re-audit

Date: 2026-07-28

Scope: Static localisation audit after IW-012 implementation commit `d7cee911c`. The audit covers the Iceland decision category, six projects, one mission, four Iceland route focuses, five Iceland ideas, Event 006 shared focus and decision text, Statehood Ledger GUI text, scripted localisation, event log and evolution surfaces, formable and achievement text, scenario text, and super-event text. No gameplay or source localisation file was patched in this audit.

## Result

The direct IW-012 key surface is complete. The six decisions and one mission resolve 26 unique direct localisation references, the Iceland category resolves its description, all four Iceland route focus keys resolve, all five idea IDs have matching name and description keys, and the two Event 006 scripted-localisation files resolve 79 unique localisation keys with no missing key found.

All 42 `localisation/english/006*.yml` files are UTF-8 with BOM. The scoped parser found 6,094 keys, no duplicate keys, no `:0` keys, no unbalanced square-bracket placeholders, and no unresolved direct GUI or scripted-localisation references. The only colour-marker balance findings are the two malformed category descriptions listed below.

No player-facing Event 006 localisation contains a stale hardcoded ten-package or eleven-package count. The only word `Ten` match is the valid achievement title `One Capital, Ten Years` in `006_independence_wave_achievements_l_english.yml:64`. Current implementation documentation distinguishes 11 attested packages from 10 compatible reservation groups, while the automatic wave ladder remains 3, 4, 5, 7, and 10. No count text correction is required.

## Missing key list

None found in the scoped Event 006 direct decision, category, focus, idea, GUI, scripted-localisation, event log, evolution, and super-event surfaces.

## Duplicate key list

None found across all 42 Event 006 English localisation files. A scoped prefix review of Event 006 keys in shared localisation also found no collision requiring repair.

## Scripted localisation issue list

No broken `localisation_key` reference was found in `common/scripted_localisation/006_independence_wave_gui_scripted_localisation.txt` or `common/scripted_localisation/006_independence_wave_scripted_localisation.txt`. The Statehood Ledger GUI references resolve to `006_independence_wave_gui_l_english.yml`, and the event log maps the Independence Wave event ID and danger milestone to existing shared keys.

The following text overstates or exposes implementation details and should be patched by the owning agent.

1. `localisation/english/006_independence_wave_ice_l_english.yml:3`, key `independence_wave_ice_hold_the_harbour_desc`, says `Iceland's first Event 006 winter`. Replace with `Iceland's first winter under emergency rule` or `Iceland's first winter as an emergency republic`.

2. `localisation/english/006_independence_wave_ice_l_english.yml:22`, key `independence_wave_ice_project_failure_effect_tt`, says `Event 006 ledgers deteriorate`. Replace with `Iceland's public statehood and separation ledgers deteriorate`.

3. `localisation/english/006_independence_wave_scenario_l_english.yml:14`, key `chaosx.scenarios.independence_wave.desc.sovereign_scatter`, says `Every researched Event 6 independence movement`. Replace with `Every researched independence movement`.

4. `localisation/english/006_independence_wave_scenario_l_english.yml:19`, key `chaosx.scenarios.independence_wave.desc.universal_nearby_nonleague`, says `outside the Event 6 league`. Replace with `outside the independence league` or `outside the league formed by this wave`.

5. `localisation/english/006_independence_wave_scenario_l_english.yml:34`, key `chaosx.triggerable_scenarios.80.d`, says `The Event 6 record preserves`. Replace with `The incident record preserves`.

6. `localisation/english/006_independence_wave_scenario_l_english.yml:59`, key `independence_wave_scenario_reject_living_tag`, says `Event 6 never overwrites`. Replace with `This incident never overwrites`.

7. `localisation/english/006_independence_wave_formable_registry_l_english.yml:99`, key `independence_wave_form39_authorize_full_integration_desc`, says `Their Event 006 origin is recorded`. Replace with `Their origin in this independence wave is recorded`.

8. `localisation/english/006_independence_wave_formable_registry_l_english.yml:147`, key `independence_wave_form39_invitation_category_desc`, says `No response overwrites its Event 006 origin`. Replace with `No response overwrites its originating movement`.

9. `localisation/english/006_independence_wave_formable_registry_l_english.yml:154`, key `independence_wave_form39_autonomous_compact_desc`, says `retains its Event 006 origin`. Replace with `retains its original institutions, territory, and local authority`.

These strings are not missing scripted localisation, but they violate the player-facing rule against implementation-history labels.

## Dynamic text opportunities

The Iceland category description already exposes all five Iceland state variables, eight former-host ledgers, network standing, and five league ledgers with dynamic values. The project cost strings resolve shared dynamic constants.

The four Iceland route focus tooltips omit the actual gate values. If the owning focus pass wants stronger clarity, add the relevant dynamic threshold to the tooltip while preserving the existing trigger semantics: civic cohesion 60 for the Constitutional Republic route, Port Authority 45 for Traditional Restoration, Coastwatch Readiness 55 for Emergency Military, and Compact Support 45 plus observed Network Standing for Patron Client.

`independence_wave_ice_compact_effect_tt` currently says the North Atlantic Compact route is open to formation, while the effect only sets `independence_wave_unlock_formable_discovery` and `independence_wave_ice_compact_delegation_ready`. Recommended text: `Network standing and league cohesion improve. Discovery of the North Atlantic Compact is open, but formation still requires consent and ratification.`

`independence_wave_ice_municipal_charter_effect_tt` only mentions Civic Cohesion and recognition even though the effect also raises Port Authority, Shipping Security, Compact Support, Capacity, and Legitimacy, and reduces Instability. Recommended wording should at least name Port Authority and Civic Cohesion, then state that recognition and institutional capacity improve and instability falls. Exact values should remain dynamic if shown.

`independence_wave_ice_accept_patron_mandate_tt` says a `patron ledger` is secured, but the availability trigger checks Compact Support and observed Network Standing and has no patron-ledger predicate. Replace `patron ledger` with `compact support and recognition standing`, or add a connected gameplay predicate before using that term.

## Cross-surface mismatch notes

The Statehood Ledger title is `North Atlantic Republic`, while the IW-012 package document uses `Icelandic Emergency Republic`. This is not a missing key, but the owning agent should decide whether the category title and package documentation should use one player-facing name.

The category and GUI use dynamic state values correctly. The four focus routes, six decisions, project failure, host settlement, compact delegation, and armed neutrality all have dedicated tooltips. No hidden route name was found in the direct Iceland surface.

The event log and evolution localisation are shared Event 006 surfaces and have matching keys. The super-event danger milestone has matching title and description keys and does not contain a stale package count.

## Additional wording and formatting findings

`localisation/english/006_independence_wave_iw022_dalmatia_l_english.yml:23`, key `independence_wave_iw022_charter_dalmatian_municipal_authority_effect_tt`, uses a semicolon between complete effect clauses. Replace the semicolon with a period or comma.

`localisation/english/006_independence_wave_iw022_dalmatia_l_english.yml:28`, key `independence_wave_iw022_entrust_coastal_security_compact_effect_tt`, uses the same semicolon pattern. Replace it with a period or comma.

`localisation/english/006_independence_wave_iw093_iw098_categories_l_english.yml:3`, key `independence_wave_iw093_asante_compact_category_desc`, has an unmatched trailing `§!` after each variable and a final `!` on Host Settlement. The labels close with `§!`, but the values are not opened with a colour marker. Use `§Y[?iw093_confederated_authority|0]§!`, `§Y[?iw093_court_cabinet_balance|0]§!`, `§Y[?iw093_cocoa_rail_throughput|0]§!`, and `§Y[?iw093_host_settlement|0]§!`.

`localisation/english/006_independence_wave_iw093_iw098_categories_l_english.yml:5`, key `independence_wave_iw098_sokoto_compact_category_desc`, has the same unmatched colour markers. Use `§Y[?iw098_emirate_compact|0]§!`, `§Y[?iw098_court_civic_balance|0]§!`, `§Y[?iw098_caravan_livestock_network|0]§!`, and `§Y[?iw098_frontier_security|0]§!`.

No em dash was found in the 42 Event 006 English localisation files. No working labels, TODO markers, or placeholder labels were found. The `N/A` values in the FORM-03 unavailable-state keys are intentional display values, not unresolved placeholders.

## Recommended fixes

Apply the nine implementation-label wording fixes, the compact formation wording correction, the patron trigger wording correction, and the municipal charter effect clarification in their listed files. Repair the two colour-marker category descriptions and remove the two Dalmatia semicolons during the next bounded localisation pass. Keep all numeric values dynamic and do not add a static ten or eleven package count.

## Patch and validation record

Changed files: this handoff only.

Changed keys: none in gameplay or localisation source files.

Dynamic localisation added or fixed: none.

Meaningful validation run: UTF-8 BOM check on all 42 Event 006 English localisation files, duplicate-key parser, scoped direct-reference coverage for ICE decisions, category, ideas, GUI, scripted localisation, event log, evolution, and super-event keys, placeholder balance scan, implementation-label scan, semicolon and em dash scan, and stale ten versus eleven scan.

Skipped meaningful validation: no live game or GUI render was run because runtime validation belongs to the parent and user. No gameplay patch was attempted.

Unresolved wording decisions: choose one player-facing Iceland category name, choose whether to show the four route threshold values in focus tooltips, and choose the final phrase for the event-specific league in the universal nearby-war scenario description.

Plan handoff path: this file.
