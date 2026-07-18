# Event 006 IW-093 / IW-098 scripted-system architecture handoff

**Date:** 2026-07-18
**Scope:** architecture only; no gameplay source, localisation, country, focus, decision, character, visual, or asset files were changed.

## Decision and readiness

IW-093 (Asante, `DOX`, anchor state `274`) and IW-098 (Sokoto, `SOK`, anchor state `902`) remain **fail-closed and not admitted**. Their region-09 loaders, weights, and reservation rows are present, but exact runtime adapters, package content attestation, setup/final-validation/cleanup dispatch, and complete country surfaces are not. The implementation must not grant `independence_wave_package_content_ready` as a shortcut.

The 2026-07-18 installed-tag audit reports zero reserved collisions. `WFX` and `SFX` are in the collision-free unused `??X` replacement pool, so they are provisional candidates only: no definitions, identity readiness flags, or family adapters may claim them until the formable identity package is complete and a new reservation record is recorded.

## Existing surfaces and call boundaries

The shared call chain is already:

1. `independence_wave_initialize_country_origin` in `common/scripted_effects/006_independence_wave_effects.txt` dispatches package setup and then final validation.
2. `independence_wave_dispatch_package_setup`, `independence_wave_dispatch_package_final_validation`, and `independence_wave_dispatch_package_cleanup` in `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt` are the only package-family dispatch points.
3. `independence_wave_reset_current_generation` calls package cleanup before clearing shared generation state.
4. Region-09 loaders and reservations live in `common/scripted_effects/006_independence_wave_packages_region_09_effects.txt`; exact package preflight is in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` and candidate availability is in `common/scripted_triggers/006_independence_wave_package_triggers.txt`.

No new world-iterating on-action is permitted. The existing frozen Event 006 transaction remains the owner of ownership, controller, core, capital, host-remnant, rollback, and finalization mutations.

## Reusable helper map

Names below are the intended implementation contract; they are not implemented by this handoff.

| Helper | Scope and inputs | Output / side effects | Call sites |
|---|---|---|---|
| `is_independence_wave_exact_package_iw_093_tag_available` | Country; fixed `original_tag = DOX`, generic origin-available checks | Boolean only; no mutation | Region-09 IW-093 candidate trigger and runtime preflight |
| `is_independence_wave_exact_package_iw_098_tag_available` | Country; fixed `original_tag = SOK`, generic origin-available checks | Boolean only; no mutation | Region-09 IW-098 candidate trigger and runtime preflight |
| `independence_wave_dispatch_iw093_package_setup` / `_final_validation` / `_cleanup` | Country; package id 93, active Event 006 generation, host and frozen anchor | Setup/final result is `selected` or `no_candidates`; setup records only package-local flags/variables; cleanup removes only package-owned state | The three central package dispatch effects |
| `independence_wave_dispatch_iw098_package_setup` / `_final_validation` / `_cleanup` | Country; package id 98, active Event 006 generation, host and frozen anchor | Same result contract; no mutation on failed preflight | The three central package dispatch effects |
| `independence_wave_iw093_prepare_kumasi_capital_transaction` | Released `DOX` after shared release/finalization; fixed anchor state 274 | Validates frozen anchor and target capital policy; sets target capital to state 274 only after ownership transfer; preserves host survival through the shared ledger | IW-093 setup/final validation, after `independence_wave_release_one_frozen_country` |
| `independence_wave_iw098_select_sultan_by_date` | Released `SOK`; package id 98 and Event 006 generation required; one succession cutover constant | Selects the date-appropriate ruler role; records an Event-006-owned role-installed flag and prior-role state for cleanup; no mutation for non-Event-006 SOK | IW-098 setup and final validation |
| `is_independence_wave_form24_member_candidate` / `_form25_member_candidate` | Country; exact family profile, active Event-006 generation, valid region-09 anchor, consent route, no living/unattested package | Boolean only; excludes assumed or placeholder members | Formable member-ledger builder and founding-invitation trigger |
| `is_independence_wave_form24_exact_carrier_anchor` / `_form25_exact_carrier_anchor` | Carrier country plus frozen anchor/region profile | Boolean only; prevents a carrier from borrowing another family’s anchor | Carrier trigger, pre-commit validation |
| `independence_wave_formable_identity_adapter_24` / `_25` | Carrier plus frozen family profile, carrier generation, and provisional `WFX`/`SFX` identity reservation | Atomic identity transaction; sets family identity-committed flag only after all checks; no flag/visual claim before package attestation | Generic `independence_wave_formable_dispatch_identity_adapter` meta-effect |
| `independence_wave_formable_integration_adapter_24` / `_25` | Carrier plus frozen member country/generation/anchor/consent arrays | Integrates only frozen rows under the family consent policy, then sets integration-committed flag | Generic integration dispatch meta-effect |
| `has_independence_wave_form24_runtime_commit_proof` / `_25_runtime_commit_proof` | Carrier; family, generation, identity, integration, member, anchor, and frozen-ledger proofs | Boolean final commit gate | `has_independence_wave_formable_commit_readiness`, `can_independence_wave_commit_selected_formable` |
| `independence_wave_form24_cleanup_runtime` / `_25_cleanup_runtime` | Carrier/member scopes with matching family and generation | Reverts only family-owned identity/integration/runtime state; clears stale generation-bound bindings before generic registry cleanup | `independence_wave_formable_cleanup_runtime` |

The generic formable registry must gain FORM-24/25 branches only when these family helpers and family readiness attestations exist. It must continue to dispatch adapters with its existing meta-effect names; do not add a second router.

## Constants and tuning plan

Reuse existing script constants rather than duplicating literals:

- `independence_wave_package_id.iw_093 = 93`, `.iw_098 = 98`.
- `independence_wave_region.west_central_africa = 9`.
- `independence_wave_package_depth.signature`, `independence_wave_package_archetype.agrarian_regional`.
- Reservation groups `rg_ghana_asante_fante` and `rg_nigeria_coarse`.
- Existing pool dispositions `high_chaos_only` and `automatic_if_not_living`.
- Existing FORM-24/25 profile constants, including minimum members/consents/anchors.

Add a subsystem constants file only when implementation starts, for the fixed package values and tunable policy:

- IW-093 anchor state `274`, Kumasi victory-point identity, capital-protection rule, and host-remnant minimum.
- IW-098 anchor state `902`, the succession cutover date (17 June 1938), and role-selection policy.
- FORM-24/25 family identity reservation names (`WFX`/`SFX`), member/consent policy, integration stage, and route masks.

Date comparisons should follow the existing `global.date`/`check_variable` pattern, with the cutover represented by one constant or one set date value. No unary-negative variables, `<=`, `>=`, or cross-file `@` constants.

## Setup, final validation, and cleanup contract

### Setup

Each package setup helper must first verify: exact package id, exact fixed tag, active Event-006 origin/generation, host and anchor event scopes, unplanned origin, no Soviet/Event-006 duplicate origin, reservation group ownership, state ownership/controller, and the package-specific anchor. It then records only package-local setup state. Ownership and capital mutation belongs to the shared frozen transaction, not setup.

IW-093 setup must require state 274 as the frozen anchor and defer the Kumasi capital move until the shared release/finalization barrier. IW-098 setup must require state 902 and the not-living automatic route. A living vanilla `SOK` is never duplicated or transformed by this path.

### Final validation

Final validation must prove setup completion, exact tag/package identity, frozen ledger/host-survival proof, force and route receipts, capital policy, date-aware role selection, and all package-local cleanup metadata. It may set the runtime content attestation only after every required country surface is present. It must not attest a missing leader role, missing country identity, missing force/focus/decision surface, or missing visual package.

### Cleanup

Package cleanup runs before the shared generation reset. It clears package-owned decisions, ideas, flags, variables, route state, role-installed markers, and regular short-lived targets. It must not clear `africa_priority_member_focus_tree_loaded`, Event 012 lifecycle flags, or vanilla SOK state unless this generation recorded that Event 006 itself changed that surface. Stale family member bindings are cleared only when their stored generation matches the ended transaction; generic formable cleanup runs afterward.

## Fixed preflight, origin safety, and transaction details

- DOX admission is an exact fixed-tag contract. Reject a living tag, reserved country/state, prior rejected plan, Soviet origin, duplicate Event-006 origin, or a second package using the same reservation group.
- SOK admission is also exact (`original_tag = SOK`) and only for the automatic-not-living release path. Existing vanilla SOK remains untouched when alive; Event 012 work remains additive.
- The shared release helper must mask and restore original host cores, release the fixed target tag, set free autonomy, and transfer only frozen planned states. No package adapter may write ownership or controllers before the finalization barrier.
- The host survival ledger must preserve at least one valid unplanned host state and must not designate the package anchor as the protected remnant.

### Kumasi capital transaction

After the shared release transaction has transferred state 274 to DOX, the IW-093 helper may set DOX’s capital to state 274. Before that point it must preserve the host’s original capital in the shared ledger. Final validation must prove DOX’s capital is 274 and the former host still has a surviving capital; a failed proof returns `no_candidates` and leaves no partial package state.

### Date-aware Sokoto succession

`independence_wave_iw098_select_sultan_by_date` is an Event-006-generation-scoped selector. Before 17 June 1938 it requires the pre-cutover role surface to be attested; on/after that date it retains or installs the post-cutover role surface. There is no fallback from a missing pre-cutover surface to the later ruler. Any retirement/recruitment or role replacement must be recorded as Event-006-owned and reversed only by matching-generation cleanup. Non-Event-006 SOK, including vanilla history and Event 012 promotion play, is out of scope.

## Event 012 compatibility

`africa_priority_member_ensure_focus_tree_loaded` sets `africa_priority_member_focus_tree_loaded` and loads `africa_priority_member_focus_tree` as an overlay. IW-098 must not call the full Event-006 focus-tree replacement helper and must not clear that flag or its lifecycle flags. Use an additive Event-006 decision/route overlay. If a future implementation absolutely requires a temporary focus assignment, it must record the previous tree and restore it only when an Event-006-owned assignment flag is present; the preferred implementation is no replacement at all. IW-093 may use the full Event-006 framework only after its own package attestation and only with provenance-aware cleanup.

## FORM-24 / FORM-25 carrier and frozen-ledger transaction

Use the existing generic registry ledgers: carrier generation, family id, proposal sequence, invited/member entries, member generations, anchors, consent rows, and frozen copies. Discovery and eligibility must be route- and generation-bound; do not absorb living or unaudited countries automatically.

- FORM-24 (West African Federation) may use DOX or another fully attested west-central-African Event-006 carrier. Candidate members are only exact active package origins with family-compatible route, anchor, and consent proof. Do not infer Fante or other members from names alone.
- FORM-25 (Sahel Confederation) may use SOK or another fully attested Sahel carrier. Route-only candidates such as DVX may participate only with their own active generation and frozen anchor/consent proof; IW-098’s reservation group remains collision-checked.
- The identity adapter reserves `WFX` for FORM-24 and `SFX` for FORM-25 only after a complete family identity package is ready. The audit proves these tags are currently unused, not that a country/flag package exists.
- Integration iterates frozen rows only. Identity and integration commit flags are set atomically and are prerequisites to the family commit proof. Any missing member, consent, anchor, identity, or integration receipt leaves the family uncommitted and invokes family cleanup.

## Validation evidence and blockers

Read-only evidence used: the 2026-07-18 country-package readiness audit; region-09 loaders/triggers; package dispatch effects/triggers; shared Event-006 execution and rollback effects; formable registry constants/effects/triggers; Event 012 focus/effect sources; the 2026-07-18 installed-tag collision audit; required offline wiki pages; and vanilla script/effects/triggers/constants documentation.

No HOI4 MCP inspection was available in this subagent context, so linked GUI/map/event rendering was not performed. No gameplay files were patched and no live-game validation was possible. The package remains blocked by missing complete country surfaces and attestation, missing verified leader/identity implementation, Event 012-safe additive wiring, formable family adapters/ledgers, and the absence of an installed visual package. No fallback or simplification was introduced.

End of architecture handoff.
