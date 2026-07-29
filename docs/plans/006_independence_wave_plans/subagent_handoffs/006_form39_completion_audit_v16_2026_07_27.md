# Event 006 FORM-39 completion audit v16

Date: 2026-07-27

Audit mode: read-only completion audit of the current shared working tree at repository HEAD `afcbe6d54`. The MFX flag package is committed at `1405913b2`. The FORM-39 gameplay, registry, localisation, documentation, and reconciliation changes were uncommitted when inspected. No gameplay, asset, localisation, catalog, or source-of-truth file was edited by this audit.

## Verdict

**FORM-39 source tranche: PARTIAL PASS / RUNTIME HOLD.**

**Whole Event 006: HOLD.**

The exact FIJ/PNG/WPG transaction is materially implemented. Registry discovery, invitations, frozen ledgers, AI replies, readiness dispatch, commit proof, MFX identity dispatch, autonomous-member installation, anchor-only full integration, rollback, post-formation projects, dissolution, and cleanup all have named hooks. The implementation remains correctly fail-closed because none of the package, identity, or review gates is manufactured by the adapter.

FORM-39 is not ready for runtime promotion. IW-157 and IW-178 do not have accepted country-package surfaces or research-flag writers, IW-177 remains outside content attestation, the FIJ portrait date decision is unresolved, the MFX flag remains `needs_user_review`, and the current installed-tag auditor rejects MFX as an unreviewed Event 006 identity. Two post-formation decision lifecycle defects and one cost mismatch also block a decision-surface PASS.

The FORM-39 tranche does not change the whole-event admission set, allocator capacity, exact-ten blocker, or any other accepted Event 006 completion gap.

## Exact implemented contract

| Surface | Current source | Audit result |
| --- | --- | --- |
| Family profile | FORM-39 `melanesian_federation`, region 13, negotiated federation, 3 members, 3 consents, 3 anchors, low AI willingness, risk tier 4 | PASS at source |
| Carrier | `FIJ`, IW-177, anchor and capital state 636 | PASS at source, package admission closed |
| Member | `PNG`, IW-178, anchor and capital state 523 | Contract present, package and research gate absent |
| Member | `WPG`, IW-157, anchor and capital state 669 | Contract present, package and research gate absent |
| Identity | Cosmetic/formable identity `MFX`, applied to the FIJ carrier | Asset staged, tag and visual review HOLD |
| Founding ledger | Exactly FIJ, PNG, and WPG in three invitation rows, three member rows, and anchors 636, 523, and 669 | PASS at source |
| Consent | Human full integration, autonomous membership, or refusal, plus exact AI consent/refusal | PASS at source, execution unproved |
| Integration | Full integration ends only a frozen consenting origin and transfers only its controlled named anchor. Autonomous mode preserves tag, origin, territory, and focus tree | PASS structurally, execution unproved |
| Post-formation content | Two categories, seven decisions, two lifecycle ideas, and four clamped carrier ledgers | Present |
| Cleanup | Reciprocal relations are receipt-flagged, generation-bound, and removed before frozen ledgers are cleared | PASS structurally, subject to project defects below |

The seven decisions are three member replies, three paid and timed carrier projects, and one dissolution action. The four ledgers are maritime logistics, cultural autonomy, federal capacity, and member consent.

## Registry and transaction hook audit

The shared registry has the required FORM-39 branches:

- `is_valid_independence_wave_formable_founding_carrier` dispatches FORM-39 to the exact FIJ carrier.
- `has_valid_independence_wave_formable_founding_invitation` accepts only exact FORM-39 members.
- Invitation issuance filters through `is_independence_wave_form39_eligible_member` and calls the FORM-39 AI resolver.
- Member and anchor ledger construction excludes the generic and FORM-48 member path and uses the exact FORM-39 eligibility trigger.
- Readiness requires `independence_wave_form39_readiness_attested`.
- Commit eligibility requires `has_independence_wave_form39_runtime_commit_proof`.
- The generic meta dispatch resolves `independence_wave_formable_identity_adapter_39` and `independence_wave_formable_integration_adapter_39`.
- Transaction failure invokes FORM-39 identity rollback.
- Successful commit starts FORM-39 post-formation progression.
- Generic formable cleanup invokes FORM-39 cleanup before clearing member arrays and loaded profile state.

The order remains fail-closed. Mutation begins only after the shared commit gate. MFX is applied before integration, integration must set the shared committed receipt, and any missing identity or integration receipt falls into the shared failure path.

## Package and readiness boundary

The following required gates have no gameplay writer in the inspected source:

- `independence_wave_fij_melanesian_member_research_complete`
- `independence_wave_png_melanesian_member_research_complete`
- `independence_wave_wpg_melanesian_member_research_complete`
- `independence_wave_form39_x_tag_reserved`
- `independence_wave_form39_flag_package_ready`
- `independence_wave_form39_identity_review_complete`

This is the correct current fail-closed state, not completion evidence. `independence_wave_form39_register_readiness` can write the shared six readiness receipts and `independence_wave_form39_readiness_attested` only after all six inputs and the exact three researched member packages pass.

IW-177 FIJ remains outside canonical Event 006 compile-time content attestation. IW-157 WPG and IW-178 PNG also remain outside admission and do not have accepted named-community package implementations. FORM-39 therefore cannot be discovered, invited, prepared, or committed in an accepted runtime configuration.

The whole Event 006 allocator remains unchanged at ten attested package IDs and nine compatible reservation groups. The exact attested IDs remain IW-001, IW-004, IW-006, IW-007, IW-008, IW-009, IW-010, IW-017, IW-019, and IW-184. IW-008 and IW-010 still share `RG-RHINE-SAAR`.

## Blocking findings

### High: canceled carrier projects can strand their active receipt

Each paid project sets its active flag in `complete_effect` when the project begins:

- `independence_wave_form39_shipping_project_active`
- `independence_wave_form39_civil_service_project_active`
- `independence_wave_form39_plebiscite_project_active`

Each decision cancels when `is_independence_wave_form39_postformation_carrier` becomes false, but none has a `cancel_effect`. The active flag is cleared only by successful completion or full FORM-39 cleanup. A temporary loss of anchor control, carrier state, transaction state, or other post-formation proof can therefore cancel the timed decision while leaving the active flag set. `has_independence_wave_form39_project_active` then blocks every project indefinitely unless a full event cleanup happens.

Required disposition: add project-specific cancellation cleanup with an explicit failure outcome, or prove that every possible cancellation condition synchronously invokes full FORM-39 cleanup before the decision cancellation is evaluated.

### High: running projects do not revalidate bound members

Project availability requires `has_independence_wave_form39_bound_members`, but the `cancel_trigger` checks only the carrier proof. A project can continue and grant its full reward after PNG or WPG stops satisfying active, sovereign, generation-bound autonomous membership, provided the FIJ carrier remains otherwise valid.

Required disposition: revalidate the bound-member contract during the project and define the failure or refund rule. Do not silently grant the three-member federal reward after the member contract has collapsed.

### Medium: plebiscite command-power gate and spend do not match

All three project triggers require command power greater than `constant:independence_wave_formable_cost.civic_command_power`, which is 40. Shipping spends two standard command-power components through strategic plus administration. Civil service spends two through strategic plus diplomatic. Plebiscites spend strategic plus security-standard, but security-standard has no command-power payment. The plebiscite therefore gates at more than 40 command power while spending only the strategic component.

Required disposition: either use the actual plebiscite spend threshold, add the intended second command-power payment, or explicitly document and localise the reserve-only gate.

### Medium: two FORM-39 tuning fields have no consumer

`independence_wave_form39.minimum_integration_anchors` and `independence_wave_form39.congress_preparation_days` are declared but unused. Integration commits on `minimum_non_carrier_members`, while the congress uses the shared transaction timing. This does not open the fail-closed gate, but it leaves FORM-39-specific acceptance tuning disconnected from runtime.

Required disposition: wire the values to the intended transaction surfaces or remove them with an explicit design decision.

## Identity, flag, and tag audit

The MFX asset package contains source, processed normal/medium/small PNGs, DDS files, runtime TGAs, prompt evidence, a contact sheet, and manifests. The runtime TGA copies match the manifest hashes. The package remains explicitly `needs_user_review`. It supplies no advisor, dossier, or portrait asset.

The dated 2026-07-26 installed-mod audit listed MFX among unused `??X` candidates before MFX became a current Chaos Redux cosmetic definition. The current read-only command:

`python -B .tools/audit_hoi4_country_tags.py`

fails with:

`RuntimeError: Unreviewed Event 006 formable or cosmetic identity in common/countries/006_independence_wave_formable_cosmetics.txt: MFX`

This is a useful fail-closed result. It means the dated collision evidence cannot be promoted as a current MFX tag PASS. Independent flag review, explicit identity acceptance, current installed-mod collision output, and the three FORM-39 identity gate writers are still required.

## Localisation, icons, ideas, and documentation

The inspected English localisation contains all FORM-39 category, decision, description, tooltip, cost, idea, family-name, and MFX name/DEF/adjective keys. It has UTF-8 BOM and no duplicate keys in the file. All five reused decision icons and the reused league-membership idea sprite are registered and point to existing Event 006 assets.

The two lifecycle ideas are visible carrier and autonomous-member states. No advisor or portrait consumer is implied.

`docs/events/006_independence_wave/form39_melanesian_federation.md`, the current source-of-truth map changes, and the current resume-packet changes accurately distinguish implemented adapter source from runtime admission. They retain the IW-157/IW-178, MFX review, collision, and FIJ source-date gates. No workbook change is required because FORM-39 does not alter the shared Event Details, evolution, cluster, or SCN-008 mirror text, and the catalog remains `In progress` / `Needs Testing`.

A dedicated independent FORM-39 localisation audit and a current tag-audit handoff are still absent. Static key coverage does not replace those promotion gates.

## Whole-event reconciliation

FORM-39 narrows one accepted formable implementation gap but does not close Event 006. The whole-event HOLD remains supported by the current source-of-truth documents and allocator result.

Remaining accepted gaps include:

- 196 of 206 candidate packages remain outside the exact ten-ID runtime attestation set.
- Exact-ten waves remain unreachable because ten admitted IDs expose only nine compatible reservation groups.
- FIJ, PNG, WPG, HAW, FSM, CHU, ASY, DOX, SOK, WLS, ARX, Cornwall, and other accepted package or asset paths retain documented admission blockers.
- FORM-01 through FORM-05 are readiness-promoted. FORM-39 is implemented but closed. FORM-12, FORM-13, FORM-18, and FORM-48 remain unreachable through their current package sets. FORM-24 and FORM-25 remain incomplete. Other accepted families remain missing or fail-closed, including FORM-42.
- The shared focus framework retains fourteen blocking layout diagnostics, unreachable generic additive and post-formation overlays, and incomplete route-aware AI evidence.
- Decision, mission, league, rival-bloc, formable, rollback, timeout, AI-resource, exploit, and save/load execution matrices remain incomplete.
- SCN-008 still lacks the six-type by four-intensity execution matrix, collision sweep, and deterministic seed evidence.
- Super-event 6002 lacks predicate-by-predicate playback and reachability proof. Super-event 6001 remains blocked by recording redistribution rights with no approved fallback.
- Sixteen achievements exist at source, but the complete qualification and disqualification matrix and several reachable routes remain missing.
- Statehood Ledger transition animations, grounded package assets, final AI, balance, host-survival, resource-safety, and representative runtime evidence remain incomplete.

No accepted whole-event requirement should be weakened or marked complete because FORM-39 source now exists.

## Meaningful validation

- Traced the exact FORM-39 carrier, member, invitation, frozen-ledger, readiness, meta-dispatch, integration, rollback, post-formation, dissolution, and cleanup hooks through the shared registry.
- Confirmed that all six package and identity admission inputs remain writerless and that no accidental readiness setter bypasses them.
- Re-ran the allocator audit. It passed with 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, ten attested packages, nine compatible reservation groups, the 3/4/5/7/10 ladder, all six scenario types, all four intensities, anchor-first order, and Event 005-first joint order.
- Ran the current country-tag audit without report writes. It stopped on unreviewed MFX, so no current tag-collision PASS is claimed.
- Checked the FORM-39 and touched registry source for balanced blocks, current localisation coverage, BOM, duplicate keys, registered icons, and the MFX runtime hash crosswalk.

No HOI4 executable, save, or live consumer was launched. No optional MCP inspection was needed for this bounded non-event-chain source audit. Human/AI consent, full-integration, autonomous-member, abort, rollback, dissolution, member-loss, project-cancel, save/load, host-survival, and Event 005 collision scenarios remain unproved.

## Required next actions

1. Repair and audit the three post-formation project cancellation and member-invalidation contracts, then reconcile the plebiscite command-power gate and dead tuning fields.
2. Complete independently audited IW-157 PNG and IW-178 WPG package research, identities, anchors, host safety, forces, decisions or focus content, AI, localisation, cleanup, and exact content-attestation decisions.
3. Resolve the IW-177 Sukuna circa-1940s source-date gate without treating the current portrait as a 1936 image.
4. Independently accept or reject the MFX flat flag, register the identity through a reviewed source-owned gate, and rerun the installed-mod tag audit against the current registry.
5. Run bounded country-package, decision/mission, localisation, formable transaction, Event 005 collision, host-survival, and save/load audits before setting any FORM-39 readiness input.
6. Keep FORM-39, IW-157, IW-177, IW-178, the exact-ten bands, and whole Event 006 fail-closed until those gates and the remaining accepted whole-event requirements pass.
