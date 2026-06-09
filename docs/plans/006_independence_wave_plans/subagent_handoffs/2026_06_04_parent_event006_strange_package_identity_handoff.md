# Event006 Strange Package Identity Handoff

## Scope

Parent implementation tranche for the Event006 Evo V strange package depth gap.

## Implemented wiring

- Split the generic tier-V strange package marker into two first-pass package identities:
  - `independence_wave_package_archive_state`
  - `independence_wave_package_necromantic_custodianship`
- Added package IDs and event-log package types for Archive-State and Necromantic Custodianship.
- Added `independence_wave_classify_strange_package_identity` to classify valid strange releases after package scoring.
- Added readable scripted triggers:
  - `is_independence_wave_archive_state_package`
  - `is_independence_wave_necromantic_custodianship_package`
- Hooked Archive-State proof into `independence_wave_open_sealed_archive_audit_effect`.
- Hooked Necromantic Custodianship proof into `independence_wave_conduct_quiet_dead_census_effect`.
- Added package event-log recorders:
  - `independence_wave_record_archive_state_package_log_entry`
  - `independence_wave_record_necromantic_custodianship_package_log_entry`
- Added package labels, event-log labels, decision AI biases, and subtype AI strategy overlays.
- Updated `docs/events/006_independence_wave.md` and the country-package source spec with implemented status.

## Asset and tag constraints

- No new country tags, country files, history files, or flag assets were added.
- No Event005 files were edited by this tranche.
- No new visual assets were produced. Current strange identity wiring uses existing Sealed Dossier decision icons and report/super-event assets.

## Remaining risks

- The Necromantic Custodianship classifier uses rural, pastoral, or wasteland state categories as the first grave-register heuristic because Event006 does not currently track battlefield, plague, or mass-death state history for release candidates.
- Archive-State and Necromantic Custodianship are now gameplay package identities, but final strange portraits, seals, animated dossier states, and bespoke strange flags remain asset work before the strange package family can be called visually complete.
