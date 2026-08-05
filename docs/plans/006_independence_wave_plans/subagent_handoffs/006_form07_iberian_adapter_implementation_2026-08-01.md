# FORM-07 Iberian Federation adapter implementation handoff — 2026-08-01

> Historical snapshot notice (2026-08-05): The body below records the pre-IW-013/IW-015 adapter state and remains preserved as dated implementation evidence. The current source-wired NAV/GLC package state and unchanged fail-closed gates are recorded in the amendment at the end of this file.

## Scope and disposition

This tranche adds the bounded FORM-07 registry surface for the installed CAT/NAV/GLC map crosswalk while keeping identity attestation fail-closed.

No X-ending cosmetic tag, source-approved flag triplet, identity commit, CAT content-attestation entry, or package-content attestation OR was added.

The family remains HOLD until an independent identity review supplies the required evidence and the absent NAV/GLC package adapters are implemented.

## Files changed

- `common/script_constants/006_independence_wave_formable_constants.txt`
- `common/scripted_triggers/006_independence_wave_form07_triggers.txt`
- `common/scripted_effects/006_independence_wave_form07_effects.txt`
- `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt`
- `common/scripted_effects/006_independence_wave_formable_registry_effects.txt`
- `common/scripted_effects/006_independence_wave_form01_02_04_effects.txt`

## Helper map

| Helper | Scope | Inputs | Outputs and side effects | Call sites |
| --- | --- | --- | --- | --- |
| `is_independence_wave_form07_member_candidate` | Country | Active Event 006 country, FORM-07 selected, setup-complete flag, exact original tag and package ID | Accepts only CAT/IW-014, NAV/IW-013, or GLC/IW-015 candidates and rejects autonomous rows | Generic invitation and frozen member-ledger passes |
| `has_independence_wave_form07_exact_member_anchor` | Country | Candidate helper, anchor variable, owner/control of state 165/172/171 | Proves the installed CAT/NAV/GLC anchor crosswalk | Carrier and member gates, corridor proof, integration adapter |
| `has_independence_wave_form07_compatible_route` | Country | Final constitutional or popular route helper | Rejects traditional, emergency, patron-client, and radical routes | Carrier, invitation, runtime commit proof |
| `is_independence_wave_form07_registered_carrier` and `has_independence_wave_form07_exact_carrier_anchor` | Country | Candidate, exact anchor, profile, regional-power state, route, identity lock | Provides the founding carrier proof without reserving a cosmetic identity | Generic founding-carrier allowlist |
| `has_independence_wave_form07_method_compatibility` | Country | Selected method and registry-derived support flags | Allows negotiated federation or revolutionary union only | Runtime readiness and commit proof |
| `has_independence_wave_form07_consent_compatibility` | Country | Selected method and consent rule | Allows negotiated voluntary/unanimous or revolutionary voluntary only | Runtime readiness and commit proof |
| `has_independence_wave_form07_declared_consent` and `has_independence_wave_form07_connection_to_root` | Candidate country with ROOT carrier | Frozen accepted invitation, family, exact anchor, and treaty/border connection | Prevents an unrecorded or disconnected member from entering integration | FORM-07 integration loop |
| `has_independence_wave_form07_corridor_proof` | Carrier country | Exact CAT, NAV, and GLC package/anchor predicates | Requires all three reviewed installed-map members; absent NAV/GLC adapters keep it false | Runtime readiness and commit proof |
| `has_independence_wave_form07_identity_runtime_contract` and `can_independence_wave_form07_register_readiness` | Carrier country | Explicit `independence_wave_form07_identity_attested`, `...x_tag_reserved`, and `...flag_package_ready` flags | Keeps all generic readiness flags cleared until a source-approved identity contract exists | FORM-07 readiness registration |
| `has_independence_wave_form07_runtime_readiness` and `has_independence_wave_form07_runtime_commit_proof` | Carrier country | Identity contract, generic readiness, carrier/route/method/consent/corridor/ledger proofs | Strict family-specific commit proof with no identity fallback | Generic commit allowlist |
| `independence_wave_formable_identity_adapter_7` | Carrier country | Mutation prevalidation | Sets only a transaction-local blocked marker; it does not set an X tag, global identity lock, or generic identity-committed flag | Existing generic meta-effect dispatcher |
| `independence_wave_formable_integration_adapter_7` | Carrier country | Mutation prevalidation, identity committed by a future reviewed adapter, frozen member arrays, and corridor proof | Integrates only explicitly authorized exact anchors; all other consenting rows receive bilateral autonomous relations | Existing generic meta-effect dispatcher |
| `independence_wave_form07_rollback_identity` | Carrier country | Generic integration state | Clears only the family7 blocked/global identity markers because no cosmetic identity exists | Generic transaction failure |
| `independence_wave_form07_cleanup_runtime` and member cleanup helpers | Carrier or autonomous member | Frozen ledger, family/generation pointers, directional relation flags | Removes only relations created by this adapter and clears family7 runtime state | Generic formable cleanup |

## Constants and tuning

`independence_wave_form07` centralizes the 165 Catalonia, 172 Navarre, and 171 Galicia anchors plus the three-member, three-consent, three-anchor, and two-additional-member thresholds.

The state IDs are also exposed as file-scoped `@FORM07_*_ANCHOR` values in the trigger/effect files because static state fields do not consistently accept `constant:` tokens in the installed Clausewitz parser.

## Migration and lifecycle

The generic registry now routes family 7 through the exact carrier/invitation/prepare/readiness/commit branches, and its member-ledger pass excludes family 7 from the broad non-Pacific/non-Melanesian branch.

The existing meta-effect dispatchers resolve `independence_wave_formable_identity_adapter_7` and `independence_wave_formable_integration_adapter_7` without adding a central router.

Failure calls the family7 rollback helper before generic transaction failure state is written, and normal cleanup calls the generation-safe family7 cleanup before loaded-profile variables are discarded.

## Validation

- Read the required offline Paradox wiki core pages and the vanilla effects, triggers, script-concept, script-math, and script-constant documentation before editing.
- Reused the existing FORM-01/02/03/04, FORM-39, and FORM-48 carrier, frozen-ledger, diplomatic-relation, meta-effect, and cleanup precedents.
- Ran a focused brace-balance and unsupported-operator scan across all six changed Clausewitz files; every file balanced and no `<=` or `>=` token was introduced.
- Ran `git diff --check` on the tracked changed files; no whitespace error was reported.
- Confirmed no `set_cosmetic_tag`, CAT attestation, or content-attestation OR was added by the tranche.

## Limitations and follow-up

Identity remains intentionally blocked because no source-approved FORM-07 X tag and flag triplet exists in the repository.

NAV/IW-013 and GLC/IW-015 currently have binding rows but no complete runtime package setup/adapters, so the all-three corridor proof remains false.

No FORM-07-specific post-formation progression, idea, localisation, GUI, or decision surface was invented; those require a separate approved design and identity package.

## Current amendment — 2026-08-05

The dated implementation body remains historical for its missing-adapter wording and does not describe the current runtime source surface.

IW-013/NAV now uses installed-map state 792 (País Vasco) as its compact anchor, with states 172 (Navarra) and 806 (French Basque) retained as optional extension objectives; IW-015/GLC uses state 171 (Galicia).

Source-level NAV and GLC setup, final-validation, and cleanup adapters are wired through `common/scripted_effects/006_independence_wave_iberian_package_effects.txt` and the central package dispatch, while the shared generic Event 006 framework and package-specific ledgers, routes, decisions, AI, forces, host/network/league/formable hooks, and generation-safe cleanup remain package-owned surfaces.

Central execution and scenario admission remain fail-closed because independent source, identity, flag, portrait, and country-package audits are not promoted and neither IW-013 nor IW-015 is in the central content-attestation set.

No advisor icons or advisor portrait assets were created or authorized, and FORM-07 remains fail-closed pending its researched Iberian X identity, flag package, and member/integration contract.
