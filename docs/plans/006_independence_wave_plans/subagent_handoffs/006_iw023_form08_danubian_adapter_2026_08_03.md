# Event 006 FORM-08 adapter handoff - 2026-08-03

## Scope

Implemented the researched Danubian Confederation adapter and connected it to the existing Transylvania package without admitting unresearched Banat or Macedonia packages.

## Changed files

* `common/scripted_triggers/006_independence_wave_form08_triggers.txt`
* `common/scripted_effects/006_independence_wave_form08_effects.txt`
* `common/script_constants/006_independence_wave_form08_constants.txt`
* `common/ideas/006_independence_wave_form08_ideas.txt`
* `common/decisions/categories/006_independence_wave_form08_categories.txt`
* `common/decisions/006_independence_wave_form08_decisions.txt`
* `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt`
* `common/scripted_effects/006_independence_wave_formable_registry_effects.txt`
* `common/scripted_triggers/006_independence_wave_form01_02_04_triggers.txt`
* `common/scripted_effects/006_independence_wave_form01_02_04_effects.txt`
* `common/scripted_effects/006_independence_wave_transylvania_package_effects.txt`
* `common/scripted_triggers/006_independence_wave_transylvania_package_triggers.txt`
* `localisation/english/006_independence_wave_formable_registry_l_english.yml`
* `docs/systems/006_independence_wave_form08_danubian_confederation.md`

## Contract

FORM-08 uses existing vanilla `HUN_EMPIRE` cosmetic/flag identity, so there is no new tag or asset collision. It admits only TRA state 84, AXX state 82, and MAC state 106 as researched anchors, preserves the HUN-origin Vojvodina overlay outside the Event 006 pool, and requires the registry minimum of three members, three anchors, and three consents before commit. The generic formation congress owns transaction locking and host/collision safety.

## Validation and remaining risk

Validation completed in the parent workspace: `python -B .tools/audit_event6_flags.py --strict` reports 102/102 complete flag families; `python -B .tools/audit_event6_allocator.py` passes the 6/8/10/14/20 ladder, 126 automatic/high-chaos selectable packages, and SCN-008 counts; `python -B .tools/audit_event6_scenario_matrix.py` passes all 32 cells and 8 edge cases; `python -B .tools/audit_chaosx_country_tags.py --surface-scan` reports zero external country-definition or identity-surface collisions. The targeted changed-file Clausewitz brace/quote/comparator audit and UTF-8 BOM/localisation-key audit also pass. No live game or save/load validation is claimed. FORM-08 remains unreachable until the AXX and MAC package adapters are researched and registered; this is intentional fail-closed behavior, not a fallback.
