# Event 006 vanilla-formable compatibility reconciliation

Date: 2026-08-02

## Decision

The durable authority is the tracked `common/decisions/formable_nation_decisions.txt` mirror. It is byte-for-byte equivalent to the installed vanilla decision source except for three intended Event 006 guard insertions:

- `can_access_vanilla_chu_formable_shortcuts = yes` in `form_idel_uralic_republic`.
- `can_access_vanilla_asy_formable_shortcuts = yes` in `neo_assyrian_empire_decision`.
- `can_access_vanilla_asy_formable_shortcuts = yes` in `neo_mesopotamia_decision`.

The former narrow `zz_006_independence_wave_vanilla_formable_compatibility_decisions.txt` adapter is removed. Keeping a second copy of the same decision IDs would create duplicate decision definitions, so the full mirror is the single owner.

## Contract

The two scripted triggers in `common/scripted_triggers/006_independence_wave_vanilla_formable_compatibility_triggers.txt` remain negative guards. They deny only the normal vanilla shortcut while the exact Event 006 IW-043 or IW-058 package is active. They do not attest a package, change formable effects, alter Event 005 behavior, or open FORM-12, FORM-13, or FORM-18.

## Validation

- Compared the three guarded decision blocks against the installed vanilla file after removing the guard lines. All three normalized blocks match.
- Confirmed the mod mirror has exactly three added guard lines and no other semantic diff from the installed vanilla source.
- Confirmed the Event 006 scripted-trigger definitions remain present and referenced by all three guarded decisions.
- No HOI4 process was launched.

## Remaining boundary

The compatibility contract is source-reproducible. IW-043 and IW-058 remain outside the fourteen-package runtime-attestation set until their independent identity, rights, and package gates pass.
