# Event 006 resume packet

Updated: 2026-07-16 after the audited Mediterranean IW-017/IW-018/IW-019 and FORM-05 tranche

Status: **Event 006 is incomplete and the goal remains active.**

Committed portrait baseline: `95f7529c7`.

IW-005 is a committed, independently audited living-BEL overlay and remains
outside the selectable pool. IW-017 COR, IW-018 ARX, and IW-019 ASX have joined
the eight earlier packages in the exact audited selectable set.

## Read first

1. `006_source_of_truth_map.md`
2. `../../assets/006_independence_wave/portrait_regeneration_male_hoi4_2026_07_16/manifest.md`
3. `subagent_handoffs/006_event6_male_hoi4_portrait_final_independent_audit_2026_07_16.md`
4. `../../specs/006_independence_wave_specs/README.md`
5. `subagent_handoffs/006_transaction_architecture_resolution_2026_07_15.md`
6. `subagent_handoffs/006_form01_04_readiness_promotion_2026_07_16.md`
7. `subagent_handoffs/006_form03_promotion_reaudit_2026_07_16.md`
8. `subagent_handoffs/006_afx_agx_release_readiness_audit_2026_07_16.md`
9. `subagent_handoffs/006_iw003_cornwall_map_feasibility_2026_07_16.md`
10. `subagent_handoffs/006_iw005_flanders_independent_audit_2026_07_16.md`
11. `subagent_handoffs/006_bri_ajx_commit_readiness_reaudit_2026_07_16.md`
12. `subagent_handoffs/006_event6_advisor_icon_withdrawal_2026_07_16.md`
13. `tag_audit/006_installed_tag_collision_audit_2026_07_15.md`
14. `subagent_handoffs/006_mediterranean_country_package_audit_2026_07_16.md`
15. `subagent_handoffs/006_mediterranean_focus_tree_audit_2026_07_16.md`
16. `subagent_handoffs/006_mediterranean_form05_decision_mission_audit_2026_07_16.md`
17. `subagent_handoffs/006_mediterranean_localisation_audit_2026_07_16.md`
18. `subagent_handoffs/006_iw017_iw019_allocator_admission_audit_2026_07_16.md`
19. `subagent_handoffs/006_mediterranean_tranche_admission_closeout_2026_07_16.md`

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
- FORM-01 through FORM-05 are implemented, source-audited, and readiness-
  promoted. FORM-06 through FORM-48 remain fail-closed.
- IW-007 AGX remains promoted from `2912e0a46` for ordinary automatic and
  SCN-008 admission. The audit is static and is not an in-engine execution
  result.
- IW-006 AFX has an audited eight-focus Sambre-Meuse Level 2 lane, three
  incidents, unique art, and exact automatic/SCN-008 admission.
- IW-001 SCO and IW-002 WLS passed their repaired transaction audit and are
  admitted for ordinary automatic and SCN-008 execution.
- IW-008 RHI and IW-009 BAY have audited Level 2 lanes, incidents, unique art,
  and exact automatic/SCN-008 admission. RHI retains its binding FORM-04
  delegation gate; BAY retains its package-owned South German settlement.
- The current attested set is IW-001, IW-002, IW-004, IW-006, IW-007, IW-008,
  IW-009, IW-010, IW-017, IW-018, and IW-019. These eleven IDs span ten
  disjoint reservation groups; every other selectable package remains outside
  the compile-time admission set.
- Commit `a2c274d1e` contains the independently audited living-BEL IW-005
  Flanders overlay. It preserves Belgium and is not a selectable Event 006
  release package. Its one-day timeout versus `on_daily_BEL` edge remains a
  documented static ordering caveat because engine order is unspecified, and AI
  completion still depends on opportunistic placement of garrisons in states 6
  and 977.
- The 2026-07-16 male-HOI4 portrait package and Mediterranean portrait ledger
  are the current portrait authorities: twenty-eight male fictional large
  portraits and ten commander-small dossiers pass, while Rupprecht and Matthes
  remain protected. ACX and AEX are unregistered readiness-pool art only.
  Earlier portrait and army-small checksum ledgers are historical and
  superseded.
- Commit `7368cc0bf` contains the bounded IW-004 BRI and IW-010 AJX packages and
  the repaired FORM transaction integration. Exact promotions are committed in
  `5d17e55b3` and `f64d9640e`.
- Static icon families, current male-HOI4 portraits and commander-small
  dossiers, country flags, FORM-01 through FORM-04 flags, report scenes,
  super-event art, and final `6002` audio files materially exist. Gameplay
  advisor offices are asset-neutral after the user-directed withdrawal of all
  custom Event 006 advisor icons.
- `6002` OGG, WAV, music wrappers, sound wrappers, zero-random station entry,
  slot-24 localisation/image dispatch, five factual predicates, Event Log
  payload, and settings-aware queued presentation are implemented. Packages 1,
  2, 3, and 5 are reachable; package 4 is dormant behind fail-closed FORM-42
  and FORM-48 carriers.
- `6001` remains blocked on exact recording rights. No fallback is authorized.

## Current package gates

| Package | Current state | Resume rule |
| --- | --- | --- |
| IW-006 AFX | Promoted | Preserve its audited Level 2 Sambre-Meuse lane, three incidents, and exact automatic and SCN-008 gates |
| IW-007 AGX | Promoted | Preserve exact automatic and SCN-008 gates. Reopen only for a concrete audit defect |
| IW-001 SCO | Promoted | Preserve exact automatic and SCN-008 gates. Reopen only for a concrete audit defect |
| IW-002 WLS | Promoted | Preserve exact automatic and SCN-008 gates. Reopen only for a concrete audit defect |
| IW-008 RHI | Promoted | Preserve its audited Level 2 lane, incidents, exact runtime gates, and binding FORM-04 delegation gate |
| IW-009 BAY | Promoted | Preserve its audited Level 2 lane, incidents, exact runtime gates, and package-owned South German settlement |
| IW-003 Cornwall | Hard blocked | Preserve ACX as reserved and dormant. Do not invent a state fallback |
| IW-005 Flanders | Committed and independently audited living-BEL overlay | Preserve `BEL` and `BEL_flanders`. Do not treat it as a selectable release package. Carry the timeout-ordering and opportunistic-garrison risks |
| IW-004 BRI | Promoted | Preserve the exact automatic and SCN-008 gates admitted in `5d17e55b3` |
| IW-010 AJX | Promoted | Preserve the exact automatic and SCN-008 gates admitted in `f64d9640e` |
| IW-017 COR | Promoted | Preserve dormant-vanilla identity safety, anchor 1, generic-tree protection, Mediterranean package mechanics, FORM-05 access, and exact automatic/SCN-008 gates |
| IW-018 ARX | Promoted | Preserve the distinct Sardinian identity, anchor 114, Italian host survival, Mediterranean package mechanics, FORM-05 access, and exact automatic/SCN-008 gates |
| IW-019 ASX | Promoted | Preserve the distinct Sicilian identity, anchor 115, Italian host survival, Level 2 package, FORM-05 access, and exact automatic/SCN-008 gates |
| Other package IDs | Fail-closed | Implement and audit individually before promotion |

Eleven compile-time attestations do not guarantee a valid wave. The allocator
must still satisfy exact host, anchor, reservation, Event 005 collision,
chaos-band, and wave-size gates. Ten disjoint reservation groups can
structurally supply every 3-, 4-, 5-, 7-, and 10-country band. World Collapse
remains exactly ten and still fails closed when runtime availability cannot
satisfy the synchronized frozen plan.

## Completed tranches not to repeat

- Core mechanics, event lifecycle, evolutions, focus and decision framework.
- Dynamic force registry and package allocator.
- Synchronized Event 005 and Event 006 release transaction.
- Anchor-first correction and rollback hardening.
- Durable sponsorship transaction.
- All-countries scenario framework.
- Liberations cluster integration.
- Installed-map binding and installed-mod tag audits.
- FORM-01 through FORM-05 implementation, tags, flags, identity aliases, and
  readiness promotion.
- Male-HOI4 portrait regeneration and final independent acceptance under the
  2026-07-16 package, plus explicit custom-advisor-icon withdrawal. The
  2026-07-15 fictional portrait and army-small packages are superseded.
- IW-003 Cornwall feasibility audit and no-fallback blocker.
- AGX's coordinated static promotion remains admitted. AFX received its missing
  Level 2 Sambre-Meuse lane, three incidents, unique art, and a fresh exact-ID
  audit before admission was restored.
- Living-BEL IW-005 Flanders overlay implementation and independent re-audit in
  `a2c274d1e`.
- Five-line army-small checksum alignment in `45bee09d2` remains historical
  implementation evidence; the 2026-07-16 runtime ledger is current.
- Bounded IW-004 BRI and IW-010 AJX package implementation and commit-readiness
  closeout in `7368cc0bf`, followed by their exact promotions in `5d17e55b3`
  and `f64d9640e`.
- RHI and BAY Level 2 lanes, incidents, unique art, and exact admission, with
  RHI's FORM-04 delegation gate and BAY's package-owned South German settlement.
- SCO/WLS congress preparation repair in `4884c0ef1`, followed by exact IW-001
  and IW-002 content-attestation and SCN-008 promotion.
- Mediterranean IW-017 through IW-019 packages, eight male HOI4-style large
  portraits, historical flat flag families for real countries, and sovereign
  charter-driven FORM-05 implementation, followed by country, focus,
  decision/mission, localisation, collision, host-survival, and admission
  audits. No advisor icons were created.
- Round-number progression, force, scenario, evolution, idea, and AI tuning in
  `879e511cc`, including the corrected negative Wallonia/Frisia war restraint
  and distinct standard versus major focus rewards.

## Immediate continuation order

1. Preserve the eleven admitted package gates and ten disjoint capacity groups
   so World Collapse can continue to attempt exactly ten releases.
2. Rerun exact-ID audits
   whenever shared planner or dispatch logic changes.
3. Preserve and re-audit the implemented Event 006 slot-24/`6002` package as
   later league, scenario, formable, sponsorship, and achievement work lands.
   Keep `6001` absent.
4. Implement the accepted FORM-48 plan with HBX as carrier, autonomous HAW/FSM
   members, and collision-cleared PFX identity; keep FORM-42 and every other
   unfinished family fail-closed. Then continue the remaining packages with
   bespoke gameplay, AI, localisation, assets, and audits.
5. Produce the remaining real frame-sequence assets ASSET-040 through ASSET-043
   only after their GUI sizes, states, frame plans, and consumers are locked.
6. Reconcile event logs, event details, documentation, asset manifests, and the
   event workbook after the active gameplay tranche settles.
7. Run the relevant country-package, decision/mission, localisation, and Event
   006 completion audits before any overall completion claim.

## Hard blockers and missing completion evidence

- IW-003 has no legal current-map state binding.
- `6001` lacks verified redistribution rights for the specified recording.
- All sixteen accepted Event 006 achievements remain without gameplay
  definitions or localisation. Fifteen have complete three-state icon triplets;
  the Assyria survival icon is the only missing art package. Radical Bloc has a
  qualification record only and cannot yet award.
- ASSET-040 through ASSET-043 have no authored frame packages.
- FORM-06 through FORM-48 remain incomplete and fail-closed.
- Super-event 6002's hidden-formable route cannot fire until FORM-42 or FORM-48
  and a valid carrier package are fully implemented and readiness-promoted.
- The event workbook and every event-log/detail surface have not been reconciled
  against the current implementation.
- No final balance and Event 006 completion audit covers the whole accepted spec.

## Do not infer

- A tag, history shell, portrait, flag, focus, or adapter does not make a package
  runtime-ready.
- ACX and AEX visual files do not authorize standalone releases.
- No 2026-07-15 fictional portrait, BRI portrait, mixed NWE portrait, or
  army-small hash/approval record is current portrait authority.
- The IW-005 living-BEL overlay is not a selectable release package.
- The eleven exact package attestations remain binding runtime gates; a broad
  identity helper or preflight branch does not admit any additional package.
- A static source audit is not an in-engine execution result.
- Historical handoff completion wording is not current when a later audit,
  commit, or `006_source_of_truth_map.md` narrows it.
- Do not rewrite accepted specs to match partial implementation.
- Do not add a fallback for Cornwall or `6001` without explicit user approval.
