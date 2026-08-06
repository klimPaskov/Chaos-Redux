# Event 006 attested-carrier capacity repair

## Scope

The automatic Liberations capacity trigger now evaluates the three already-attested adapters that were present in the package registry and regional planners but missing from the central capacity transaction: IW-023 (TRA, anchor state 84), IW-033 (KAR, anchor state 146), and IW-041 (CRI, anchor state 137).

## Changed files

- `common/scripted_triggers/006_independence_wave_triggers.txt`
  - Added exact runtime preflight wrappers for IW-023, IW-033, and IW-041.
  - Added capacity reservation functions with package, country, anchor, host-survival, Event 005 collision, and reservation-group guards.
  - Added the three functions to the Liberations capacity transaction.
- `common/scripted_effects/006_independence_wave_scenario_effects.txt`
  - Replaced unsupported shared script-constant tokens in `distance_to` fields with file-scoped literal mirrors, matching existing repository precedent.

## Validation

- `python -B .tools/audit_event6_allocator.py` passed.
- `python -B .tools/audit_event6_scenario_matrix.py` passed.
- `python -B .tools/audit_event6_flags.py` passed with 102 complete families.
- `python -B .tools/audit_chaosx_country_tags.py` passed with zero scoped external collisions.
- `python -B .tools/audit_event6_gui_matrix.py` passed.
- Touched trigger file has no duplicate top-level scripted-trigger identifiers or unsupported ordered operators.

## Remaining limits

This repair does not promote any unattested package, change the accepted package registry, or provide live-game evidence. Typed probability evidence, full package admission, formable reachability, super-event 23 firing/audio, and the broader Event 006 completion gates remain tracked separately.
