# Event 006 SCO/WLS Release-Readiness Promotion — 2026-07-16

> **Portrait-specific supersession (2026-07-16):** The large and small
> portrait visual evidence in this promotion is superseded by the male-HOI4
> package manifest and final independent audit. Gameplay, formable, and
> admission findings remain historical evidence.

## Scope

This handoff records the exact admission transaction for IW-001 Scotland (`SCO`)
and IW-002 Wales (`WLS`). It does not attest any other Event 006 package.

## Repair evidence

The initial independent package audit found one shared blocker: both package
conferences paid their strategic costs, wrote completion proof, granted rewards,
and attempted final commitment without first running the shared formable
preparation transaction.

Commit `4884c0ef1` repairs both call sites. Each conference now:

- requires the exact stable package, capital, strategic cost, package-project
  lock, and shared formable-operation lock;
- calls `independence_wave_formable_begin_preparation` exactly once;
- records its package congress and grants network standing only after
  `independence_wave_formable_transaction_ready` exists;
- leaves the final proclamation to the shared formation decision; and
- applies package failure on invalid removal or cancellation without refund.

The same commit preserves the two Scotland family-choice readiness reloads,
corrects the commander dossier dimensions to `65x67`, and aligns FORM-01/02
documentation with their promoted identity and integration adapters.

## Focused re-audit

A fresh read-only staged-index audit passed both packages after the repair. It
confirmed:

- exact IW-001/SCO and IW-002/WLS dormant-tag bindings;
- protected host remnants, unique anchors, reservation groups, and Event 005
  separation;
- full package setup, validation, cleanup, forces, ideas, decisions, missions,
  five-focus country groups, seven AI strategies, leaders, commanders, and
  three advisor offices per package;
- FORM-01 and FORM-02 exact identities, complete flag families, consent,
  territory, integration, and rollback transactions;
- distinct human `156x210` HOI4-painted leaders and `65x67` commander/advisor
  dossiers with matching sprite and manifest evidence;
- zero direct formation-proof or commit bypass in the package conferences; and
- UTF-8 BOM and resolved package-local localisation references.

The audit was static and did not execute an in-engine wave.

## Admission changes

This change adds only IW-001 and IW-002 to
`common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`.
After the Level 2 corrections, the resulting total admission set is:

- automatic/content attestation: IW-001, IW-002, and IW-007;
- SCN-008 preflight: IW-001/SCO, IW-002/WLS, and IW-007/AGX.

The runtime allocator still must pass host survival, anchor ownership and
control, unique reservation, Event 005 collision, chaos band, and requested
wave-capacity checks. Admission is not stored in vanilla history.

## Level 2 admission correction

The same current audit cycle found that IW-006 Wallonia and IW-009 Bavaria are
binding Level 2 packages without the required country-specific focus group.
Their previous content attestations and SCN-008 branches were therefore
removed. These are fail-closed corrections, not substitutes for the missing
groups. IW-008 Rhineland remains closed for the same focus requirement and its
separate FORM-04 preparation defect. IW-007 Frisia remains admitted because it
is Level 1 and passed its package audit.

## Simplifications and blockers

No fallback or gameplay simplification was accepted for SCO or WLS. The
remaining AFX, RHI, and BAY blockers are recorded explicitly and do not weaken
the two promoted package gates.
