# Populated installed-vanilla GUI references

Disposition: two populated, route-plausible HOI4 MCP source renders archived and visually reviewed; neither is an engine screenshot or click receipt.
Acceptance basis: the user's request to inform the Administration, Locations and Records design with visible vanilla Decisions and Occupied Territories references.

Installed HOI4 MCP 3.5.1 rendered the vanilla `countrydecisionview` and `countryoccupationview` at 1920×1080, 100% UI scale.
Both windows used their installed `show_position = { x = -6 y = 78 }` endpoint and appeared onscreen with a measured 544×1002 root at x=0, y=78, replacing the earlier blank/offscreen attempts.
The exact [manifest](manifest.json) records scenario files, source revisions, installed-game file hashes, twelve original MCP artifact URIs, lengths and verified SHA-256 values.
No `GUI_MISSING_LOCALISATION` or zero-size root was returned; the occupation layout retains one `GUI_SCROLLBAR_CONTAINER_BOUNDARY_MISSING` warning, whose actual native wheel and clipping behavior is unverified.

| Vanilla view | Populated image | Click overlay | Declared source state |
| --- | --- | --- | --- |
| Decisions | [Political Actions crop](rendered/vanilla_eng_1937_worker_conditions_visible/countrydecisionview-cropped.png) | [regions](rendered/vanilla_eng_1937_worker_conditions_visible/countrydecisionview-click-regions.png) | ENG, 1937-01-01, democratic, 70% stability, 150 Political Power; one Improved Worker Conditions decision at its vanilla 100 Political Power cost. |
| Occupied Territories | [Poland crop](rendered/vanilla_ger_pol_two_state_occupation_declared/countryoccupationview-cropped.png) | [regions](rendered/vanilla_ger_pol_two_state_occupation_declared/countryoccupationview-click-regions.png) | GER, 1944-10-01, explicitly controlling Polish states 87 Łódź and 88 Kraków in a two-state alternative campaign remnant; vanilla Forced Labor occupation law; release and return-territory actions hidden. |

The [decision scenario](requests/vanilla_eng_1937_worker_conditions_visible.json) uses only one source-backed decision, avoiding a catalog image that combines incompatible options.
Installed `common/decisions/_generic_decisions.txt` lines 65–101 makes `improved_worker_conditions` visible and available when stability is below 1, with a 100 Political Power cost and `generic_industry` icon.
The declared 70% stability and 150 Political Power satisfy that source condition and quote; no engine state or actual player decision is inferred.
The category and decision name resolve through installed `wtt_decisions_l_english.yml`, and the icon resolves through installed `interface/decisions.gfx`.

The [occupation scenario](requests/vanilla_ger_pol_two_state_occupation_declared.json) supplies actual state IDs and controller tags as explicit alternate-history facts rather than assuming a particular save.
It uses installed `common/occupation_laws/occupation_laws.txt` lines 355–385 for `forced_labor_occupation` and installed `resistance_and_occupation_l_english.yml` line 79 for “Forced Labor.”
The law has no general political prerequisite in its definition; this reference does not claim that the engine selected it in a historical campaign.
Runtime resistance, compliance, manpower, industrial capacity, resources and foreign support remain dashes rather than fabricated measurements.
The source window lists Poland and its two declared occupied state rows; it is a composition reference, not a complete country-wide 1944 control map or casualty estimate.

Both originals were opened at full resolution and their click overlays inspected.
Text, source icons, list rows and native hit regions are legible without visible clipping or overlap; the occupation row's vertical scrollbar remains within the vanilla frame.
Installed `interface/countrydecisionview.gui` and `interface/countryoccupationview.gui` contain their root names and `show_position` at lines 4–6; their exact raw hashes, along with decision, law, GFX and localisation sources, are in the manifest.
The offline `paradox_wiki/Interface modding - Hearts of Iron 4 Wiki.md` button and container sections and installed `common/scripted_guis/_documentation.md` and decision files were consulted for the same native family; the connected `hoi4.reference_*` and `source_lookup` routes were absent from this task's callable list, so local source paths and hashes are retained here.

These successful populated captures were obtained after the first four generated Chaos Redux design images and some native GUI edits.
They close the missing populated-vanilla-artifact gap, but do not change that earlier sequence or prove exact in-game visual parity.
The Chaos Redux three-view source renders and their scenario-specific limits remain in [the 45-case review](../current_click_matrix_3_5_1/README.md), [the resource-locked review](../locations_resource_locked_actions_2026-09-27.md) and [the selected-release review](../../selected_release_row_integrity_2026-09-27.md).
