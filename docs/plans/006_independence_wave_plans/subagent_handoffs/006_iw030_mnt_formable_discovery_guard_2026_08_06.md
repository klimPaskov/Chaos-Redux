# IW-030 MNT formable-discovery guard

## Scope

The Montenegro Balkan-corridor helper exposed the generic `independence_wave_unlock_formable_discovery` flag whenever a formable family was registered, even though the MNT readiness contract explicitly forbids family registration. The shared discovery trigger additionally requires a valid selected family, a matching loaded profile, readiness, and a discovery mode. This patch keeps the MNT helper fail-closed at its own boundary and prevents a stale or partial registry state from presenting an empty formable surface.

## Changed files

- `common/scripted_effects/006_independence_wave_montenegro_package_effects.txt`
  - `independence_wave_mnt_focus_open_balkan_corridor`
  - The unlock flag now requires `has_valid_independence_wave_formable_family_selection` and `independence_wave_formable_profile_matches_selected_family` in addition to registration.
- `docs/events/006_independence_wave/montenegro_package.md`
  - Documents the stricter registration, selection, and profile contract.

## Before and after

Before, a registered-family flag alone could set the generic discovery flag from the MNT corridor. After, the helper can set it only for a selected family whose profile matches the selection. MNT remains without a formable family and therefore does not expose generic discovery. No family is registered, no formable identity or tag is invented, and no central attestation or scenario allowlist is changed.

## Validation

The source trace was checked against `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt`. The shared discovery trigger already requires family registration, valid selection, commit readiness, and a matching discovery gate, so this local guard removes the only weaker writer in IW-030. The package remains fail-closed for portrait, rights, force/OOB, AI, runtime, and save/load evidence.

## Remaining gaps

IW-030 remains outside central attestation. No typed AI probability or live runtime evidence was produced, and no portrait, flag, history, OOB, or formable package was promoted.
