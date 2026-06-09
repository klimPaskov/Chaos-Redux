# Event 006 Sealed Dossier Tranche Handoff

## Scope

Implemented a first-pass Sealed Dossier decision category for strange or occult-pressure Event 006 releases. This tranche does not touch flag assets, country definitions, history files, Event 005 Soviet Collapse systems, or visual assets.

## Files Changed

- `common/decisions/categories/006_independence_wave_categories.txt`
- `common/script_constants/006_independence_wave_constants.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/decisions/006_independence_wave_decisions.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `docs/events/006_independence_wave.md`

## Identifiers

- Category: `independence_wave_sealed_dossier_category`
- Category gate: `can_independence_wave_open_sealed_dossier`
- Decisions:
  - `independence_wave_open_sealed_archive_audit`
  - `independence_wave_conduct_quiet_dead_census`
  - `independence_wave_convene_unmarked_congress`
  - `independence_wave_seal_impossible_registry`
- Triggers:
  - `can_independence_wave_open_sealed_archive_audit`
  - `can_independence_wave_conduct_quiet_dead_census`
  - `can_independence_wave_convene_unmarked_congress`
  - `can_independence_wave_seal_impossible_registry`
- Effects:
  - `independence_wave_clamp_occult_pressure`
  - `independence_wave_open_sealed_archive_audit_effect`
  - `independence_wave_conduct_quiet_dead_census_effect`
  - `independence_wave_convene_unmarked_congress_effect`
  - `independence_wave_seal_impossible_registry_effect`
  - `independence_wave_complete_containment_review_effect`
  - `independence_wave_fail_containment_review_effect`
- Mission:
  - `independence_wave_hold_containment_review`

## Behavior

- The category appears only for independent Event 006 releases that have the strange package marker, an open sealed audit, or enough occult pressure, and closes after the impossible registry is sealed or the Unmarked Congress reveals the route.
- The archive audit opens the file, lowers occult pressure, and gives limited legitimacy and foreign attention.
- The quiet dead census trades legitimacy for manpower, occult pressure, and foreign attention.
- The Unmarked Congress requires higher occult pressure and marks the strange route as revealed through `chaosx_iw_strange_revealed`.
- Sealing the impossible registry starts `independence_wave_hold_containment_review`; timeout success contains the registry, lowers occult pressure and radicalization, and closes the category, while early failure marks `independence_wave_containment_review_failed` and reveals the strange file.

## Validation Notes

- Decision audit completed in `2026_05_30_114209_event006_sealed_dossier_audit_patch_handoff.md`.
- Audit patched all four decisions with `fire_only_once = yes` and completed-state visibility blockers, and expanded the category gate to accept either `independence_wave_package_strange_candidate` or `independence_wave_package_type = strange_package`.
- Containment review audit completed in `2026_05_30_event006_containment_review_audit_patch_handoff.md`.
- Containment review audit patched the seal decision with an explicit review-start tooltip and made `independence_wave_hold_containment_review` explicitly non-selectable with `selectable_mission = no`.
- Static validation completed after the audit patch: brace balance passed for the Event 006 decision-category, decision, constants, trigger, effect, and event files; bounded Clausewitz scan found no unsupported `<=` or `>=`; Event 006 localisation is UTF-8 with BOM and has no `:0` keys.
- No flag asset, country-definition, history, Event 005, or asset paths are part of this change.

## Remaining Risks

- This is a bounded first pass. It does not implement full strange focus modules, necromantic or anti-mankind country packages, strange coalitions, world-threat hooks, super-events, or custom art.
- Future strange-package work still needs to decide whether `chaosx_iw_strange_revealed` alone unlocks deeper reveal content after non-pressure containment failure.
- Runtime UI validation has not been performed.
