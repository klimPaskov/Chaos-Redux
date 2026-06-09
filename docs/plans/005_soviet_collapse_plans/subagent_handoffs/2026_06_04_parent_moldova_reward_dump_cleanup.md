# Event 005 parent Moldova reward dump cleanup

Date: 2026-06-04

Scope: parent cleanup pass for one audited visible focus reward dump in the Moldova Soviet Collapse tree. Flag assets were explicitly out of scope and were not opened or edited.

## Changed files

- `common/national_focus/005_soviet_collapse_republics.txt`
- `localisation/english/005_soviet_collapse_regional_focus_l_english.yml`

## Focus changed

- `moldova_soviet_collapse_romanian_aid_without_annexation`

## Behavior

The focus still applies the same gameplay payload:

- marks Romanian aid without annexation
- applies the foreign-channel and foreign-supply focus packages
- increases Prut statute support
- increases patronage strain
- increases recognition progress
- increases independence resilience
- improves infrastructure in one controlled core state
- applies the Soviet foreign-pressure reaction

The visible reward surface is now one clear route-specific tooltip:

- `moldova_soviet_collapse_romanian_aid_without_annexation_tt`

The implementation payload is inside `hidden_effect`, so the player no longer sees a long list of internal variables, flags, route-pressure helpers, and random-state implementation details.

## Validation

- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt localisation/english/005_soviet_collapse_regional_focus_l_english.yml`
- `rg -n "<=|>=" common/national_focus/005_soviet_collapse_republics.txt localisation/english/005_soviet_collapse_regional_focus_l_english.yml`
- localisation BOM check for `005_soviet_collapse_regional_focus_l_english.yml`: `efbbbf`
- tooltip wiring check: key appears once in the focus file and once in localisation
- brace-depth check:
	- `common/national_focus/005_soviet_collapse_republics.txt`: `brace_level 0`
	- `localisation/english/005_soviet_collapse_regional_focus_l_english.yml`: `brace_level 0`
- `git status --short -- gfx/flags interface/flags`: no output

## Remaining work

This removes one audited reward dump. The broader reward cleanup remains incomplete, especially the ancient restoration envoy/patrol focuses, `DSC_witness_officers`, `ICD_commissars_of_last_addresses`, `TSC_the_committee_of_instruments`, `RMC_communes_of_witnesses`, `MFR_workers_own_the_arsenal`, and Ukraine League reward surfaces.
