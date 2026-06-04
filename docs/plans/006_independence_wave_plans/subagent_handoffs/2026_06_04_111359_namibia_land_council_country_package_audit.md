# Event006 Namibia Land Council Country-Package Audit

Timestamp: 2026-06-04 11:13:59 UTC

Role: bounded country-package audit for the vanilla-backed `NMB` Namibia Land Council tranche.

## Scope

Audited the Namibia package surface named in the parent prompt:

- `can_independence_wave_seed_namibia_package`
- `is_independence_wave_namibia_package`
- `has_independence_wave_namibia_land_control`
- `can_independence_wave_open_namibia_land_records`
- `can_independence_wave_map_namibia_land_petitions`
- `can_independence_wave_proclaim_namibia_land_council`
- `has_independence_wave_namibia_land_council_failure`
- Namibia package constants, startup classification, reduced release anchor, focus/decision chain, idea, AI strategy hook, package/event-log localisation, docs, and asset stance.

## References Consulted

Required offline Paradox wiki pages were consulted before reading the package files:

- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Effect - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Idea modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Country creation - Hearts of Iron 4 Wiki.md`

Vanilla documentation and precedent consulted:

- `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`
- `~/projects/Hearts of Iron IV/documentation/triggers_documentation.md`
- `~/projects/Hearts of Iron IV/documentation/modifiers_documentation.md`
- `~/projects/Hearts of Iron IV/documentation/loc_formatter_documentation.md`
- `~/projects/Hearts of Iron IV/documentation/loc_objects_documentation.md`
- `~/projects/Hearts of Iron IV/documentation/script_concept_documentation.md`
- `~/projects/Hearts of Iron IV/common/script_constants/documentation.md`
- `~/projects/Hearts of Iron IV/history/countries/NMB - Namibia.txt`
- `~/projects/Hearts of Iron IV/history/states/541-South West Africa.txt`
- Vanilla release/load-focus precedents in `common/on_actions/04_mtg_on_actions.txt`, `events/BBA_Italy.txt`, and `common/decisions/BEL.txt`.

Verified vanilla facts:

- Vanilla `NMB - Namibia.txt` sets `capital = 541` and recruits NMB characters.
- Vanilla state `541-South West Africa.txt` has `add_core_of = NMB`.
- Vanilla localisation has `STATE_541: "Khomas"` and full `NMB` country, ideology, DEF, and ADJ keys.
- Vanilla provides `NMB` ideology flag files under base, `medium`, and `small` flag folders.

## Findings

No package-surface correctness defects were found.

The package can enter the candidate pool:

- `can_independence_wave_use_candidate_tag` includes the `NMB` exception path and calls `can_independence_wave_seed_namibia_package`.
- `can_independence_wave_seed_namibia_package` gates high chaos tier IV/V, inactive `NMB`, non-capital state `541`, host control of `541`, host survival state count, and host weakness.
- `independence_wave_seed_verified_package_candidates` adds `NMB` to `global.independence_wave_candidate_pool` when the Namibia seed trigger passes.
- `can_independence_wave_candidate_enter_local_polity_pool` also fits vanilla state `541` because Khomas is an NMB core and vanilla marks the state as `pastoral`.

The reduced-territory anchor correctly prefers Khomas:

- `independence_wave_try_package_reduced_release_anchor` has a package-specific `tag = NMB` branch that checks state `541`, requires it to be owned and controlled by the current host, requires it to be an NMB core, and saves it as `independence_wave_reduced_release_anchor_state` before the generic fallback anchor logic can select another NMB core.
- Since vanilla NMB only has the relevant Khomas core in this audited package path, the anchor matches the intended vanilla-backed start.

The package classifies as local-polity:

- `independence_wave_setup_released_country` sets `independence_wave_package_namibia`, `independence_wave_package_local_polity_candidate`, package id `constant:independence_wave_package.namibia`, package type `constant:independence_wave_startup.local_polity_package`, formation family `formation_family_namibia_land_council`, and adds `independence_wave_namibia_land_council_spirit`.
- `common/ai_strategy/006_independence_wave.txt` includes `independence_wave_package_namibia`, `independence_wave_namibia_land_records_opened`, and `independence_wave_namibia_land_council_proclaimed` in the local-polity defense hook.

The focus/decision chain is wired:

- Focuses `independence_wave_namibia_land_records` and `independence_wave_namibia_land_petitions` exist, have icons, availability, bypasses, rewards, unlock tooltips, and AI weights.
- Decisions `independence_wave_open_namibia_land_records`, `independence_wave_map_namibia_land_petitions`, `independence_wave_proclaim_namibia_land_council`, and mission `independence_wave_integrate_namibia_land_council` exist.
- Trigger gates require the NMB package, Khomas ownership/control where needed, opened records, mapped petitions, independence, local-polity cohesion, and legitimacy.
- Integration succeeds by timeout through `independence_wave_finish_namibia_land_council_integration` and fails while available through `has_independence_wave_namibia_land_council_failure` into `independence_wave_discredit_namibia_land_council`.

The event log is wired:

- `independence_wave_open_namibia_land_records_effect` records `independence_wave_record_namibia_land_records_package_log_entry`.
- `independence_wave_proclaim_namibia_land_council_effect` records `independence_wave_record_namibia_land_council_formation_log_entry`.
- Constants `namibia_land_records_package_type = 69` and `namibia_land_council_formation_type = 68` exist.
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` maps both constants to GUI localisation keys and includes them in package/formation detail body routing.
- `localisation/english/chaosx_gui_l_english.yml` has both GUI event-log type keys.

Localisation is present:

- Required Namibia package label, focus names/descriptions, decision names/descriptions, idea name/description, trigger tooltip, mission failure/success tooltip, and event-log GUI keys were all present.
- No new localisation was added.

No Event005 helper or file dependency was found in the Namibia package surface:

- The broad Event006 files still contain existing Event005 separation guards and docs that reject Soviet Collapse-origin state. These are separation checks, not calls into Event005 helper files or content.
- No Namibia-specific decision, focus, effect, trigger, idea, or log row uses an Event005 helper, Event005 focus tree, Event005 decision, or Event005 package file.

Asset stance is truthful:

- No new NMB flag or country asset is required. Vanilla provides NMB country history, characters, country localisation, and ideology flags.
- Namibia uses existing Event006 sprites:
  - `GFX_focus_independence_wave_local_land_council`
  - `GFX_focus_independence_wave_border_commission`
  - `GFX_decision_independence_wave_open_talks`
  - `GFX_decision_independence_wave_border_survey`
  - `GFX_decision_independence_wave_recognition_mission`
  - `GFX_idea_independence_wave_guarani_land_congress`
- The referenced Event006 sprite definitions and DDS files exist.

## Checks Run

- `rg -n "<=|>=" ...` across the named Event006 script/localisation/docs files: no unsupported operators found.
- `rg -n "Event 005|Event005|event005|005_soviet|soviet_collapse|Soviet Collapse|005_" ...` across the named files: broad separation guards/docs found, no Namibia package dependency found.
- Brace-count script across the named Event006 script and localisation files: final balance `0`, minimum balance `0` for all checked files.
- Localisation key audit for Namibia package label, focus, decision, idea, tooltip, mission, and event-log GUI keys: no missing keys.
- Vanilla verification for `NMB` history, state `541`, `STATE_541`, `NMB` country localisation, and vanilla NMB flag files.
- Existing Event006 icon audit for the Namibia focus, decision, and spirit picture references.

## Changes Made

Only this audit handoff was added.

No gameplay, localisation, GUI, flag, or asset files were patched.

## Skipped Validation

No in-game validation was run. This audit is static/script-level only.

No Clausewitz parser or full mod load validation was run in this subagent pass.

## Remaining Risks

- The surrounding Event006 files contain unrelated formatting scars and broader generated-content complexity outside the Namibia tranche. The audited files were brace-balanced globally, but this handoff does not certify the whole Event006 implementation.
- The actual release outcome still depends on live resolver runtime state: chaos tier IV/V, state `541` host control, host weakness, host survival-state thresholds, and candidate-pool random selection.
- The Event005 references found in broad Event006 files are separation guards/documentation. If the parent wants a stricter zero-string-reference policy, that is a broader Event006 architecture decision and not a Namibia package defect.
