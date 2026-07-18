# IW-043 / IW-058 final decision and transaction audit

## Documentation reconciliation note (2026-07-18, post-audit wiring)

The transaction findings below remain current for paid congresses, consent and
anchor ledgers, defensive-method preflight, cleanup, and sovereignty
preservation. A later source wiring pass changes only the terminal presentation
ordering described by older audit text: the sovereign-autonomy decision locks
either the completed former-host settlement or a named sovereignty-bound
regional guarantor, writes the compact and mode records without firing 5810,
and the final ratification focus is the sole `.5810` caller after revalidating
the locked partner and all five treaty chapters. The exact
CHU/ASY attestation and proof-writer status is operational for this bounded
tranche; whole-Event 006 runtime simulation and closeout remain pending.

## Scope and outcome

Audited the final transaction surface for FORM-12, FORM-13, and FORM-18: the paid congress decisions, invitation/consent ledgers, exact candidate and anchor gates, keyed identity/integration adapters, six staged-integration decisions, IW-058 military-settlement receipts, sovereign-autonomy route, achievement-writer call sites, and the generic DM-54/DM-55 exclusions.

Two local defects were fixed. The shared parent changes for action-time AI consent and the IW-058 defensive-war receipt writer were reviewed as live behavior and are sound under their stated contracts. No Independence Wave advisor asset, portrait, sprite, or dossier surface was created or wired.

## Issues, sorted by severity

### High — fixed: opposed observers could satisfy the distinct-anchor proof

`independence_wave_iw_formable_capture_generation_receipts` rebuilt the unique-anchor receipt array from every valid ledger row. The consent count itself was correct, but an opposed or observing member with a third anchor could make the FORM-12/FORM-13/FORM-18 unique-anchor threshold pass even when the consenting members did not own distinct anchors.

The receipt loop now reads the aligned consent entry and considers its anchor only when that row is `consenting_member`. The unique-anchor receipt is therefore tied to the members who actually join the transaction.

### High — fixed: military FORM-18 could start before its method evidence existed

`can_begin_independence_wave_form18_congress` previously reached the generic invitation gate without applying the military method policy. A selected military settlement could therefore reserve its cost and open the 180-day congress before the defensive-victory, sovereign-anchor, and corridor-control receipts existed, then fail only during finalization.

`has_independence_wave_iw058_form18_pre_congress_method_policy` now gates FORM-18 before payment. Negotiated federation remains available immediately; military settlement requires the three earned defensive receipts and no offensive-pretext flag. It deliberately does **not** require `iw058_form18_member_consent_receipt`, because consent must be generated after invitations are issued. The existing final method policy remains stricter and still requires the consent receipt before commit.

### Medium — reviewed parent fix: action-time AI consent now enters the ledger

`independence_wave_formable_evaluate_candidate_consent` now re-reads the accepted/withheld flags immediately after `independence_wave_iw_formable_score_ai_consent`. The temporary row value therefore becomes consenting or opposed in the same ledger rebuild; human replies remain immutable country-generation-family-sequence declarations.

### Medium — reviewed parent fix: military receipt writer is defensive and cleanup-bound

`independence_wave_achievement_resolve_country_peace` writes the FORM-18 defensive-war, sovereign-anchor, and corridor-control receipts only after the tracked former-host war has ended, ASY was recorded as the defender, ASY is sovereign and uncapitulated, Mosul is owned and controlled, corridor fortification exists, and security meets the stable threshold. An ASY-initiated former-host war records the war but not the defensive flag, so it cannot satisfy this policy. The exact package and achievement cleanup paths clear the three receipts and the offensive-pretext flag.

### Low — remaining documentation discrepancy

At the time of this audit, `docs/systems/006_independence_wave_iw043_iw058_signature_packages.md` and the earlier decision audit handoff still said FORM-12/13/18 were fail-closed because the attestation flags were unwritten. The current setup writes the IW-043 writer/Form-12/Form-13 flags and the IW-058 writer/Form-18 flags in `independence_wave_apply_iw043_package_setup` and `independence_wave_apply_iw058_package_setup`; this documentation pass records that promotion. Gameplay is not fail-closed for the exact CHU/ASY carriers.

## Decision-category lifecycle and mission quality

| Surface | Owner/category/region | Requirement and duration | Success | Failure, cancellation, duplicate risk |
|---|---|---|---|---|
| FORM-12 accession congress | CHU, IW-043 federal, Middle Volga | Exact federal carrier, active terminal, 3 external exact-package consenting members with 3 distinct controlled anchors; 180 days | Paid transaction commits, carrier-only cosmetic identity and staged sovereignty-preserving integration, then `chaosx.nr006.4313` | Failed/invalid ledger rolls back without refund, clears ledgers and proposal, applies 45-day family cooldown; active/receipt flags clear |
| FORM-13 compact congress | CHU, IW-043 restoration, Middle Volga | Exact restoration carrier, same external-member and distinct-anchor policy; 180 days | Same transaction discipline, then `chaosx.nr006.4314` | Same bounded reset/cooldown path |
| FORM-18 federal congress | ASY, IW-058, Mesopotamian corridor | Exact carrier, negotiated method or earned defensive-settlement preflight, then 2 exact external consenting members with 2 distinct controlled anchors; 180 days | Paid transaction commits, carrier-only cosmetic identity and staged sovereignty-preserving integration, then `chaosx.nr006.5812` | Rollback preserves spent cost, clears proposal/ledger/receipts, applies 45-day cooldown; route/subject cancellation is guarded |
| Six staged integrations | Formed carrier, three family-specific decision surfaces | Two 90-day charter decisions followed by two 120-day defense/revenue decisions; carrier remains sovereign and controls the named anchors | `independence_wave_iw_formable_advance_staged_members` moves only this carrier/family's staged consenting members through integration flags | Visibility/cancel triggers remove stale carrier or subject surfaces; no passive checklist mission, unit grant, annexation, or origin-ending call |
| Sovereign autonomy compact | ASY, non-guardianship route, Mesopotamia | Completed peaceful former-host settlement or named sovereign regional guarantor, plus boundary/protection/jurisdiction/transit/security records; 180 days | Commits the paid transaction, locks exactly one counterpart mode, and selects sovereign autonomy; the final ratification focus later owns `chaosx.nr006.5810` after revalidating that partner and all five records | Rollback and bounded host or regional pressure; no subject or client relationship is created |

## Costs, requirements, AI, and route locks

- Congresses are 180 days through `independence_wave_iw043.settlement_mission_days` or `independence_wave_iw058.settlement_mission_days`; integration uses central 90/120-day constants; retry uses the central 45-day constant.
- Congress costs use the existing paid-transaction helpers: command power, manpower, civilian-factory commitment, and where relevant equipment/transport inputs. There is no direct political-power store or refundable equipment loop. The negative stockpile effects are payments, not grants.
- FORM-12/13 accept only the exact active external TAT/BSK/MEL/UDM/KOM packages; FORM-18 accepts only exact active KUR/CJX. Candidate triggers reject subjects, war, other formable transactions, dead/stale packages, and invalid ownership/control. Carriers are not counted as members.
- Human replies use `chaosx.nr006.4311`, `.4312`, and `.5811`; AI scoring now persists and immediately maps to the rebuilt ledger. Congress and integration `ai_will_do` values are positive only with the relevant reserve/readiness conditions.
- Generic DM-54 and DM-55 explicitly exclude signature families, so their generic congress/commit path cannot collide with FORM-12/13/18.

## Cleanup and exploit review

- Proposal close/reset clears frozen invitation snapshots, member/anchor/consent arrays, stage state, receipts, temporary operation flags, and only the matching carrier generation/family proposal. Retry flags prevent immediate failure/cancel cycling.
- Commit adapters retain each consenting country's tag, sovereignty, Event 006 origin, focus content, and territory. The audited adapter/effect surface contains no annexation, subject creation, blanket cores, state transfer, `load_oob`, or unit-creation effect.
- The military method cannot be obtained from an offensive former-host war. The preflight policy blocks payment before the 180-day congress; the final policy adds the invitation-earned consent receipt.

## Changed files and identifiers

1. `common/scripted_effects/006_independence_wave_iw043_iw058_package_effects.txt`
   - `independence_wave_iw_formable_capture_generation_receipts`
   - Unique anchors now require the aligned ledger row to be `independence_wave_formable_consent.consenting_member`.
2. `common/scripted_triggers/006_independence_wave_iw043_iw058_package_triggers.txt`
   - Added `has_independence_wave_iw058_form18_pre_congress_method_policy`.
   - Added it to `can_begin_independence_wave_form18_congress`.
3. `common/decisions/006_independence_wave_iw043_iw058_decisions.txt`
   - `independence_wave_iw058_hold_form18_federal_congress` now exposes its method gate through a custom trigger tooltip.
4. `localisation/english/006_independence_wave_iw043_iw058_decisions_l_english.yml`
   - Added `independence_wave_iw058_form18_pre_congress_method_policy_tt`.

## Meaningful validation

- Static transaction assertions confirmed the consent-only anchor gate; the FORM-18 preflight wire; exclusion of member consent from the pre-invitation method policy; consent inclusion in the final method policy; the parent AI action-time consent map; and all defensive-war receipt prerequisites.
- Confirmed all 38 decision names resolve in their decision localisation, and all 171 decision/event custom-cost, custom-effect, and custom-trigger tooltip keys resolve in English localisation. The touched localisation retains UTF-8 BOM.
- Confirmed zero prohibited formable mutators (`annex_country`, subject/puppet creation, core grant, state transfer, unit creation, or OOB loading) in the package transaction effect surface.
- Read-only Event MCP lint was not used as completion evidence: its file selector expanded to a full 4,060-source workspace report with unrelated diagnostics. No decision-owned scripted GUI belongs to this surface, so no GUI inspection/render artifact applies.

## Skipped validation and residual risks

- No engine runtime simulation was available for the exact sequence: human/AI reply mix, loss of an anchor during the 180-day mission, former-host defensive peace, and retry expiry. Static checks prove the wiring but cannot prove Clausewitz runtime scope behavior.
- The two stale documentation files above need reconciliation. No gameplay fallback or simplification was introduced, and no plan handoff was written.
