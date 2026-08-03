# Event 006 FORM-08 ledger and identity-gate repair

Date: 2026-08-03.

Scope: bounded source implementation tranche for the existing Danubian Confederation adapter. This handoff does not promote a country package, resolve the accepted member-geography mismatch, or claim live runtime evidence.

## Implemented

- The Danubian decision-category description now exposes federal cohesion, arbitration capacity, transport authority, and minority settlement as live `0-100` ledgers.
- Charter promotion now requires all four ledgers to reach the coordinated threshold, and all four to reach the integrated threshold. Transport authority and minority settlement therefore affect the lifecycle idea instead of remaining write-only values.
- FORM-08 identity admission now fails closed if the vanilla Austria-Hungary formation flag is set, if another Event 006 carrier already holds the identity lock, or if any living country currently carries the vanilla `HUN_EMPIRE` cosmetic identity.
- The system and source-of-truth documentation record the current adapter boundary and the unresolved registry reconciliation instead of presenting the narrower TRA/AXX/MAC implementation as the accepted Transylvania/Banat/Vojvodina/Slavonia geography.

## Files

- `common/scripted_effects/006_independence_wave_form08_effects.txt`
- `common/scripted_triggers/006_independence_wave_form08_triggers.txt`
- `localisation/english/006_independence_wave_formable_registry_l_english.yml`
- `docs/systems/006_independence_wave_form08_danubian_confederation.md`

## Focused checks

- `python -B .tools/audit_event6_gui_matrix.py`
- `python -B .tools/audit_event6_allocator.py`
- `python -B .tools/audit_event6_flags.py --strict`
- `python -B .tools/audit_event6_scenario_matrix.py`
- `python -B .tools/audit_chaosx_country_tags.py --surface-scan`

All five checks passed. These are static source checks only; no game launch, save/load, AI, or runtime coexistence observation is claimed.

## Remaining gates

FORM-08 still requires researched Vojvodina and Slavonia member/package adapters, the installed-map crosswalk decision, and independent HUN_EMPIRE coexistence evidence before the accepted registry geography can be admitted. No new member, tag, flag, leader, advisor, history file, or fallback was added by this tranche.
