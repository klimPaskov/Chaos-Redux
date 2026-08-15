# FORM-12/13 MEL state-256 fail-closed hardening

## Superseded by the exact state-833 rebind

The temporary fail-closed guard described below was the safe intermediate state. The current FORM-12/13 consumer specs, manifests, generated assets, GUI, scripted localisation, and qualification helpers now use installed Mari El state 833. State 256 remains Chuvashia and is no longer used as a MEL proxy. This handoff remains as historical evidence for the intermediate safety patch.

## Scope

The FORM-12 and FORM-13 state-puzzle helpers named `state_256` previously accepted an invited `MEL` member through the generic IW-043 candidate trigger without proving that the member actually owned, controlled, and used state 256 as its capital.

## Change

`common/scripted_triggers/006_independence_wave_formable_state_puzzle_triggers.txt` now requires `MEL` to own and control state 256 and have its capital in state 256 for both `independence_wave_formable_state_puzzle_form12_state_256_qualifies` and `independence_wave_formable_state_puzzle_form13_state_256_qualifies`.

This follows the existing exact-state consumer pattern used by FORM-03 and FORM-05. It does not rename the slot, alter the GUI, regenerate assets, or rebind the live MEL package anchor.

## Disposition

The current MEL package uses state 833 while the FORM-12/13 geometry and manifests use state 256. The new checks therefore keep MEL fail-closed for those formable slots until the family-owned 256-to-833 rebind is designed and regenerated. No central attestation, normal/scenario preflight, or deterministic Join entry was added.

## Evidence and limits

Static source review confirms state 256 is Chuvashia and state 833 is Mari El. Existing map and grouped GUI MCP receipts remain workspace-wide/partial and do not authorize a formable rebind. A fresh GUI or map rewrite was not attempted because this bounded change only tightens the source trigger and does not modify layout or geometry.
