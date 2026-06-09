# Event 006 Dossier Board Host Tools Tranche Handoff

## Scope

Expanded the Event 006 Independence Dossier Board with host-targeted tools for the releases that came from that host. This tranche does not touch flag assets, country definitions, history files, or Event 005 Soviet Collapse systems.

## Files Changed

- `common/script_constants/006_independence_wave_constants.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/decisions/006_independence_wave_decisions.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `docs/events/006_independence_wave.md`

## Identifiers

- Host release ledger array: `independence_wave_host_released_countries`
- Shared target gate: `can_independence_wave_host_target_release`
- Decisions:
  - `independence_wave_offer_local_autonomy`
  - `independence_wave_arrest_committee_couriers`
  - `independence_wave_arm_loyalist_councils`
- Triggers:
  - `can_independence_wave_offer_local_autonomy`
  - `can_independence_wave_arrest_committee_couriers`
  - `can_independence_wave_arm_loyalist_councils`
- Effects:
  - `independence_wave_offer_local_autonomy_effect`
  - `independence_wave_arrest_committee_couriers_effect`
  - `independence_wave_arm_loyalist_councils_effect`

## Behavior

- Each successful release is added to the former host's `independence_wave_host_released_countries` array during `independence_wave_register_successful_release`.
- Host Dossier Board targeted decisions use that host-scoped array, so hosts act only against their own Event 006 releases.
- Autonomy offers lower target pressure and radicalization, raise target legitimacy, and reduce host anger at a stability cost.
- Courier arrests spend host command power, reduce target legitimacy, raise target radicalization and foreign attention, and reduce host anger.
- Loyalist councils spend host command power and infantry equipment, then add target loyalist pressure, pressure, radicalization, and foreign attention while reducing target legitimacy.

## Validation Notes

- Decision audit completed in `2026_05_30_event006_dossier_board_host_tools_audit_patch_handoff.md`.
- Audit patched the shared target gate to require host-ledger membership and reject capitulated releases, guarded host-ledger registration against duplicate entries, and added blocked/hover custom-cost localisation for courier arrests and loyalist councils.
- Static validation completed after the audit patch: brace balance passed for the Event 006 decision, decision-category, constants, trigger, effect, and event files; bounded Clausewitz scan found no unsupported `<=` or `>=`; Event 006 localisation is UTF-8 with BOM and has no `:0` keys.
- No flag asset, country-definition, history, or Event 005 paths are part of this change.

## Remaining Risks

- This is a bounded first pass. It does not create civil-war loyalist tags, state-level loyalist districts, border transfers, or guarantee negotiations.
- Existing saves from before this change will not have the host-scoped release ledger for already-created releases.
- Runtime UI validation has not been performed.
