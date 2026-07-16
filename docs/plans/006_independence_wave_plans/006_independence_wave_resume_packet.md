# Event 006 resume packet

Updated: 2026-07-16 after committed baseline `7368cc0`

Status: **Event 006 is incomplete and the goal remains active.**

Committed baseline: `7368cc0bf`.

IW-005 is a committed, independently audited living-BEL overlay. IW-004 BRI and
IW-010 AJX are committed, bounded country packages with commit-readiness proof.
These facts do not add any of the three surfaces to a selectable release pool.

## Read first

1. `006_source_of_truth_map.md`
2. `../../specs/006_independence_wave_specs/README.md`
3. `subagent_handoffs/006_transaction_architecture_resolution_2026_07_15.md`
4. `subagent_handoffs/006_form01_04_readiness_promotion_2026_07_16.md`
5. `subagent_handoffs/006_form03_promotion_reaudit_2026_07_16.md`
6. `subagent_handoffs/006_afx_agx_release_readiness_audit_2026_07_16.md`
7. `subagent_handoffs/006_iw003_cornwall_map_feasibility_2026_07_16.md`
8. `subagent_handoffs/006_iw005_flanders_independent_audit_2026_07_16.md`
9. `subagent_handoffs/006_bri_ajx_commit_readiness_reaudit_2026_07_16.md`
10. `subagent_handoffs/006_event6_advisor_icon_withdrawal_2026_07_16.md`
11. `tag_audit/006_installed_tag_collision_audit_2026_07_15.md`

The seven specification parts remain the design authority. Use the source-of-
truth map for current implementation status and handoff dispositions.

## Safe current facts

- The event source and localisation are substantial implementations, not
  placeholders.
- The 206 accepted packages resolve to 102 reserved `X` tags, 91 reused vanilla
  tags, and 13 overlay rows.
- The 2026-07-15 installed-mod audit found zero collision for all 102 reserved
  tags in the scanned environment.
- The installed-map registry has 138 selectable bound packages, 55 selectable
  unbound packages, and 13 overlays.
- Trabzon state 354 and Kashmir state 441 have implemented cross-group
  reservation protection. Their old unresolved status is superseded.
- The synchronized Event 005 and Event 006 release transaction, rollback ledger,
  point-of-no-return, sponsorship transaction, and Liberations cluster capacity
  surface are implemented.
- FORM-01 through FORM-04 are implemented, source-audited, and readiness-
  promoted. FORM-05 through FORM-48 remain fail-closed.
- IW-007 AGX remains promoted from `2912e0a46` for ordinary automatic and
  SCN-008 admission. The audit is static and is not an in-engine execution
  result.
- IW-006 AFX's earlier admission was revoked after the binding Level 2 focus
  group was found missing.
- IW-001 SCO and IW-002 WLS passed their repaired transaction audit and are
  admitted for ordinary automatic and SCN-008 execution.
- IW-009 BAY's earlier admission was revoked after the binding Level 2 focus
  group was found missing.
- The current attested set is IW-001, IW-002, and IW-007. Every other
  package remains outside the compile-time admission set.
- Commit `a2c274d1e` contains the independently audited living-BEL IW-005
  Flanders overlay. It preserves Belgium and is not a selectable Event 006
  release package. Its one-day timeout versus `on_daily_BEL` edge remains a
  documented static ordering caveat because engine order is unspecified, and AI
  completion still depends on opportunistic placement of garrisons in states 6
  and 977.
- Commit `45bee09d2` completed the exact five-line ACX, AEX, AFX, AGX, and AJX
  army-small checksum alignment.
- Commit `7368cc0bf` contains the bounded IW-004 BRI and IW-010 AJX packages and
  the repaired FORM transaction integration. Both exact immutable identity
  helpers and both runtime-preflight ID/tag branches are present. Neither exact
  ID has compile-time content attestation or a SCN-008 admission branch.
- Static icon families, portraits, army-small dossiers, country flags, FORM-01
  through FORM-04 flags, report scenes, super-event art, and final `6002` audio
  files materially exist. Gameplay advisor offices are asset-neutral after the
  user-directed withdrawal of all custom Event 006 advisor icons.
- `6002` OGG, WAV, music wrappers, sound wrappers, and station entry are complete.
  Event 006 gameplay still does not assign audio ID `6002` and fire the
  settings-aware presentation path.
- `6001` remains blocked on exact recording rights. No fallback is authorized.

## Current package gates

| Package | Current state | Resume rule |
| --- | --- | --- |
| IW-006 AFX | Prior admission revoked | Add the binding Level 2 focus group and re-audit before restoring content attestation or SCN-008 admission |
| IW-007 AGX | Promoted | Preserve exact automatic and SCN-008 gates. Reopen only for a concrete audit defect |
| IW-001 SCO | Promoted | Preserve exact automatic and SCN-008 gates. Reopen only for a concrete audit defect |
| IW-002 WLS | Promoted | Preserve exact automatic and SCN-008 gates. Reopen only for a concrete audit defect |
| IW-008 RHI | Fail-closed | Add the binding Level 2 focus group and repair FORM-04 preparation, then run a fresh exact-ID audit |
| IW-009 BAY | Prior admission revoked | Add the binding Level 2 focus group and re-audit before restoring content attestation or SCN-008 admission |
| IW-003 Cornwall | Hard blocked | Preserve ACX as reserved and dormant. Do not invent a state fallback |
| IW-005 Flanders | Committed and independently audited living-BEL overlay | Preserve `BEL` and `BEL_flanders`. Do not treat it as a selectable release package. Carry the timeout-ordering and opportunistic-garrison risks |
| IW-004 BRI | Bounded package implemented and commit-audited | Exact identity helper and runtime-preflight branch are present. Run a separate exact-ID content-attestation and SCN-008 admission audit before promotion |
| IW-010 AJX | Bounded package implemented and commit-audited | Exact identity helper and runtime-preflight branch are present. Run a separate exact-ID content-attestation and SCN-008 admission audit before promotion |
| Other package IDs | Fail-closed | Implement and audit individually before promotion |

Three compile-time attestations do not guarantee a valid wave. The allocator
must still satisfy exact host, anchor, reservation, Event 005 collision,
chaos-band, and wave-size gates. Higher bands need more audited packages.

## Completed tranches not to repeat

- Core mechanics, event lifecycle, evolutions, focus and decision framework.
- Dynamic force registry and package allocator.
- Synchronized Event 005 and Event 006 release transaction.
- Anchor-first correction and rollback hardening.
- Durable sponsorship transaction.
- All-countries scenario framework.
- Liberations cluster integration.
- Installed-map binding and installed-mod tag audits.
- FORM-01 through FORM-04 implementation, tags, flags, identity aliases, and
  readiness promotion.
- Character portrait regeneration, explicit custom-advisor-icon withdrawal,
  and army-small dossier correction.
- IW-003 Cornwall feasibility audit and no-fallback blocker.
- Historical AFX and AGX coordinated static promotion; AFX is subsequently
  revoked fail-closed while AGX remains admitted.
- Living-BEL IW-005 Flanders overlay implementation and independent re-audit in
  `a2c274d1e`.
- Five-line army-small checksum alignment in `45bee09d2`.
- Bounded IW-004 BRI and IW-010 AJX package implementation and commit-readiness
  closeout in `7368cc0bf`.
- SCO/WLS congress preparation repair in `4884c0ef1`, followed by exact IW-001
  and IW-002 content-attestation and SCN-008 promotion.
- Round-number progression, force, scenario, evolution, idea, and AI tuning in
  `879e511cc`, including the corrected negative Wallonia/Frisia war restraint
  and distinct standard versus major focus rewards.

## Immediate continuation order

1. Audit IW-004 BRI for exact-ID compile-time content attestation and SCN-008
   admission. Keep this separate from AJX.
2. Audit IW-010 AJX for exact-ID compile-time content attestation and SCN-008
   admission. Keep this separate from BRI.
3. Implement the missing AFX, RHI, and BAY Level 2 focus groups, repair RHI's
   FORM-04 congress preparation, and re-audit each package before admission.
4. Expand the audited automatic pool until every accepted wave band has enough
   mutually compatible candidates. Preserve reservation-first planning and
   Event 005 collision checks.
5. Wire Event 006 super-event presentation and settings-aware `6002` playback.
   Keep `6001` absent.
6. Continue package and FORM-05 through FORM-48 implementation with bespoke
   identities, gameplay, AI, localisation, assets, and audits.
7. Produce the remaining real frame-sequence assets ASSET-040 through ASSET-043
   only after their GUI sizes, states, frame plans, and consumers are locked.
8. Reconcile event logs, event details, documentation, asset manifests, and the
   event workbook after the active gameplay tranche settles.
9. Run the relevant country-package, decision/mission, localisation, and Event
   006 completion audits before any overall completion claim.

## Hard blockers and missing completion evidence

- IW-003 has no legal current-map state binding.
- `6001` lacks verified redistribution rights for the specified recording.
- The Assyria survival achievement lacks an approved exact motif and ownership
  decision.
- ASSET-040 through ASSET-043 have no authored frame packages.
- FORM-05 through FORM-48 remain incomplete and fail-closed.
- IW-004 and IW-010 still lack exact-ID content-attestation and SCN-008 admission
  audits. Their committed package and preflight plumbing does not close that
  evidence gap.
- The event workbook and every event-log/detail surface have not been reconciled
  against the current implementation.
- No final balance and Event 006 completion audit covers the whole accepted spec.

## Do not infer

- A tag, history shell, portrait, flag, focus, or adapter does not make a package
  runtime-ready.
- ACX and AEX visual files do not authorize standalone releases.
- The IW-005 living-BEL overlay is not a selectable release package.
- BRI and AJX exact identity helpers and runtime-preflight branches are
  non-authorizing prerequisites, not admission proof.
- A static source audit is not an in-engine execution result.
- Historical handoff completion wording is not current when a later audit,
  commit, or `006_source_of_truth_map.md` narrows it.
- Do not rewrite accepted specs to match partial implementation.
- Do not add a fallback for Cornwall or `6001` without explicit user approval.
