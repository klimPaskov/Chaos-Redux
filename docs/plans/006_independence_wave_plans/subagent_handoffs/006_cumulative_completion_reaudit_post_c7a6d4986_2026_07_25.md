# Event 006 cumulative completion re-audit after the treasury repair

Audit date: 2026-07-25.

Audit mode: read-only Event 006 completion audit.

Gameplay audit baseline: commit `c7a6d49867355e9bacff988b1024a0aaed6a5250`, including `a1cd50e9c` and the earlier DM-58 repair chain through `8a553adb0`.

The workspace contained unrelated pre-existing modified and untracked files.
No gameplay, localisation, asset, workbook, specification, or existing plan file was edited by this audit.

## Verdict

**INCOMPLETE.**

The economy-capstone source blocker from `006_focus_tree_completion_audit_2026_07_25.md` and `006_event_completion_audit_2026_07_25.md` is superseded and closed by `a1cd50e9c` plus `c7a6d4986`.
The capstone has a real continuing consumer, origin cleanup removes an active copy, and origin cleanup separately removes its re-enable cooldown.

The earlier DM-58 paid-failure and rollback-provenance blockers are also superseded at source level by `972037edd`, `893e4d2e4`, and `8a553adb0`.

Those closures do not make Event 006 complete.
Exact top-band allocation remains structurally impossible, most accepted package and formable coverage remains fail-closed, the shared focus tree still has fourteen blocking layout diagnostics, accepted package-specific focus depth is incomplete, super-event and visual-production blockers remain, and the required live scenario, AI, balance, playback, and achievement evidence is absent.

## Economy capstone re-audit

### Consumer

**PASS at source level.**

- `common/national_focus/006_independence_wave_focus.txt:376-392` defines `independence_wave_create_independent_treasury`, sets `independence_wave_economy_capstone_complete`, adds `independence_wave_independent_treasury`, and grants the stabilization reward.
- `common/decisions/006_independence_wave_decisions.txt:498-554` defines `independence_wave_treasury_backed_public_works`.
- Its visibility requires both an active Event 006 origin and `independence_wave_economy_capstone_complete`.
- Its availability requires capital control, no severe instability, remaining capacity or instability work, and `can_pay_independence_wave_strategic_cost`.
- It uses the established strategic payment helper, reserves civilian factories for 240 days, grants bounded capital infrastructure and country-ledger improvements on expiry, and has a 365-day re-enable period.
- `localisation/english/006_independence_wave_decisions_l_english.yml:99-102` provides the decision, description, requirement, and effect keys.
- `localisation/english/006_independence_wave_focus_l_english.yml:118` now discloses the continuing public-works programme in the focus tooltip.

This is a material recurring consumer rather than a passive flag check or decorative unlock.

### Active and cooldown cleanup

**PASS at source level.**

- `common/scripted_effects/006_independence_wave_decision_effects.txt:757-788` removes the active decision with `remove_decision` and removes its re-enable state with `remove_decision_on_cooldown`.
- `common/scripted_effects/006_independence_wave_effects.txt:307-312` invokes the decision-layer cleanup during current-generation reset before focus-runtime state is cleared.
- `common/scripted_effects/006_independence_wave_effects.txt:2701-2714` invokes the same cleanup when an active origin ends.
- `common/scripted_effects/006_independence_wave_focus_effects.txt:96-97` clears the capstone flag and removes the treasury idea.

Current vanilla `effects_documentation.md` states that `remove_decision` removes an active decision without running `remove_effect` or applying cooldown, while `remove_decision_on_cooldown` removes the re-enable/cooldown record.
The paired calls therefore cover the two distinct lifecycle states.

### Remaining economy validation boundary

No live decision run proves start, cost deduction, civilian-factory reservation, 240-day expiry, infrastructure-cap behavior, reward, cooldown, repeat, cancellation, or repeat-origin cleanup.
This is runtime evidence still missing for whole-event completion, not a remaining source-consumer defect.

## Completion status by surface

| Surface | Current status | Evidence and remaining boundary |
| --- | --- | --- |
| Entry event, presentation, Event Log, Event Details, and five evolutions | **Finished at source level; runtime proof missing** | The entry chain, representative actor, log payload, detail selectors, and five evolution mirrors remain implemented. Their current live repeated-wave and cleanup behavior is unproved. |
| Release transaction, rollback, host survival, and Event 005-first collision order | **Finished at source level; runtime proof missing** | The synchronized reservation and transaction architecture remains in source. The DM-58 repair is no longer an implementation blocker, but ordinary, joint, rollback, and terminal-failure runtime matrices are still absent. |
| Economy capstone | **Finished at source level; runtime proof missing** | `a1cd50e9c` adds the real consumer and active cleanup; `c7a6d4986` adds cooldown cleanup and player-facing focus disclosure. |
| Automatic allocator and exact bands | **Partial; top bands blocked** | The structural audit passes the 3/4/5/7/10 contract, but the ten content-attested IDs occupy only nine mutually compatible reservation groups. |
| Country package coverage | **Partial** | Exactly ten package IDs are content-attested. The accepted registry contains 206 package rows; other adapters, overlays, and packages remain dormant, unadmitted, map-blocked, asset-blocked, or audit-blocked. |
| Shared focus framework | **Fail for completion** | Current `hoi4.focus_inspect` reports 176 focuses, 214 connectors, 49 crossings, 18 node intersections, 26 long connectors, and fourteen blocking diagnostics. The economy-consumer finding is closed, but layout and package-depth findings remain. |
| Package-specific focus coverage | **Partial** | Bespoke and imported modules exist for a bounded set. The admitted IW-007/AGX package has no AGX- or Frisia-named focus identifier, and most accepted package rows have no demonstrated package-specific focus module. |
| Decisions and missions | **Materially implemented; runtime and balance proof missing** | The treasury consumer and DM-58 source repairs close the two prior concrete implementation findings. Broad AI/resource-safety, league, route, and scenario validation remains absent. |
| Formables | **Partial and broadly blocked** | FORM-01 through FORM-05 are implemented and readiness-promoted. FORM-12/13/18 have operational exact-carrier contracts but their IW-043/IW-058 carriers are not content-attested. FORM-06 through FORM-47 otherwise remain fail-closed, including FORM-42. FORM-48 remains unreachable because HAW/FSM are unadmitted. |
| SCN-008 Every Banner Rises | **Partial** | All intensities and accepted scenario types exist, and the allocator attempts the ranked surface through the normal gates. Actual execution remains limited by content admission and live compatibility; no intensity/type runtime matrix exists. |
| Super-event 6002 | **Implemented at source level; reachability and playback unproved** | Slot 24, audio 6002, exact OGG/WAV, image, localisation, Event Log payload, five predicates, and settings-aware FIFO submission exist. The exact ten-country predicate is structurally blocked and the hidden-formable path lacks a compliant carrier set. No predicate or playback scenario has live proof. |
| Super-event 6001 | **Blocked** | ASSET-005 static art remains, but audio 6001, slot-23 dispatch, localisation/firing package, and the specified recording are absent. Exact recording redistribution rights remain unresolved; no substitute is authorized. |
| Achievements | **Partial** | All sixteen definitions, English pairs, completion triggers, and three-state icon triplets are present. Several package, formable, radical-bloc, and full-scenario proofs are unreachable or unproved. No live completion/invalidation matrix exists. |
| Static assets | **Materially produced but incomplete** | Admitted packages and bounded signature/formable tranches have substantial final files. Other grounded packages still fail sourced-roster, flag, formable-identity, map, or package-audit gates. |
| Animation assets | **Blocked** | ASSET-040 through ASSET-043 still lack locked production inputs, authored source frames, processed frames/sheets, static fallbacks, previews, manifests, and GUI/runtime handoffs. |
| Documentation and catalog | **Catalog alignment closed; commit-state cleanup partial** | The workbook matches current Event Details, five evolutions, Liberations cluster, and SCN-008 wording. `In progress / Needs Testing` correctly reflects real incompletion. The current working copies of the source-of-truth map and resume packet correct obsolete nine-package/IW-006 wording, but those corrections were uncommitted at audit baseline `c7a6d4986`. |

## Exact counts and reservation-group blocker

`common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:55-76` admits exactly:

| Package | Tag | Anchor | Reservation group |
| --- | --- | ---: | --- |
| IW-001 Scotland | SCO | 121 | `RG-121-120-133` |
| IW-004 Brittany | BRI | 14 | `RG-14` |
| IW-006 Wallonia | AFX | 34 | `RG-34` |
| IW-007 Frisia | AGX | 36 | `RG-36` |
| IW-008 Rhineland | RHI | 51 | `RG-RHINE-SAAR` |
| IW-009 Bavaria | BAY | 52 | `RG-52-53-54` |
| IW-010 Saar | AJX | 42 | `RG-RHINE-SAAR` |
| IW-017 Corsica | COR | 1 | `RG-1` |
| IW-019 Sicily | ASX | 115 | `RG-115` |
| IW-184 California | HBX | 378 | `RG-378` |

The current reservation CSV permits one automatic package per group.
IW-008 and IW-010 share `RG-RHINE-SAAR`, so ten IDs provide nine compatible groups.

| Band | Exact target | Maximum compatible groups before live checks | Result |
| --- | ---: | ---: | --- |
| Calm World | 3 | 5 eligible by band | Conditionally viable |
| Gathering Storm | 4 | 8 eligible by band | Conditionally viable |
| Rising Chaos | 5 | 9 | Conditionally viable |
| Chaos Tier | 7 | 9 | Conditionally viable |
| Totalen Chaos | 10 | 9 | Structurally impossible |
| World Collapse | 10 | 9 | Structurally impossible |

The lower bands are not runtime passes.
They can still fail through a living tag, missing host or anchor, Event 005 reservation, host-survival limit, invalid force/package finalization, or other live transaction condition.

Completion requires a separately audited package in a tenth compatible group or explicit acceptance of a map-valid rebinding.
Reducing the exact count or permitting the RHI/AJX collision would be an unauthorized fallback.

## Focus, layout, and package coverage

The current inspector reproduced the unchanged layout hash `3e5996acbdbed97ab085d52cd058861f2fbd21acc896f859268b204a9c81a5a2`.
Validation failed with fourteen blocking connector-crossing diagnostics.
Artifact:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/aab0179d8eb7b39ce24509713324d1b4edbb1a19467b9fe66e4fd29345a3096d/bf2358173475bb3c41e9b84eef90c6596a5ce35133418b6df9bc8f71aa2c9793/focus-inspect.003bc8a7691a4355.json`

The blocking clusters remain in the founding/economy fan-out and the professional-defense convergence.
The rejected broad coordinate nudge recorded in `006_event6_shared_focus_layout_closeout_2026_07_25.md` worsened the layout and was correctly reverted.
A coupled-cluster authored reflow remains required.

The economy capstone is no longer a focus-contract blocker.
The remaining focus completion gap is accepted breadth and identity:

- package-specific focus depth exists only for a bounded package set;
- the admitted AGX package receives shared and regional content but no AGX/Frisia-named focus module;
- imported IW-043/IW-058, IW-093/IW-098, and Pacific modules do not prove runtime coverage while their corresponding packages remain unadmitted;
- most accepted package rows still rely on the generic framework without demonstrated package-specific route depth or the accepted breadth of institutional naming.

## Formable blockers

- FORM-01 through FORM-05 are the finished readiness-promoted tranche.
- FORM-12, FORM-13, and FORM-18 have exact operational CHU/ASY contracts, paid congresses, consent/anchor ledgers, staged sovereignty-preserving integration, and exact proof writers, but IW-043 and IW-058 remain outside content attestation because their grounded portrait packages do not satisfy the current sourced-real-person gate.
- FORM-24 and FORM-25 remain incomplete with IW-093/IW-098: final carriers/members, identity, sovereignty/integration policy, flags, sourced leaders/commanders, and final package/scenario audits are unresolved.
- FORM-42 remains hard fail-closed because the accepted founding set has no legal current-map contract.
- FORM-48 source and bounded assets exist without an annexation fallback, and HBX is admitted, but HAW and FSM are unadmitted. The family therefore cannot satisfy its complete member contract.
- Other FORM-06 through FORM-47 families remain fail-closed pending exact identity, territory, member, integration, tag, flag/emblem, route, consumer, and audit readiness.

## Super-event, asset, and documentation gaps

### Super-events

- `6002` is a real runtime source package, not a design-only placeholder. Its remaining blocker is acceptance evidence and predicate reachability, not missing source wiring.
- Its exact ten-country route inherits the nine-compatible-group blocker.
- Its hidden-formable route inherits the FORM-42/FORM-48 blockers.
- The remaining source-reachable predicates and settings-aware FIFO path have no recorded live playback evidence.
- `6001` remains a disclosed hard blocker. The exact London Brass Players recording lacks verified United States redistribution rights. No fallback recording is authorized.

### Assets

- `docs/assets/006_independence_wave/manifest.md:218-234` still records ASSET-040 through ASSET-043 as unproduced real animation tasks.
- Grounded packages must not be promoted on generated, generic, or identity-soft portrait evidence. Current unresolved examples include the withdrawn IW-043/IW-058 rosters, the HAW/FSM FORM-48 member packages, and the IW-093/IW-098 leader/commander roster and period-flag requirements.
- FORM-06 through FORM-47 identity flags and emblems remain blocked except for already promoted bounded families.
- No transform-only animation or generic formable-art fallback was found or authorized.

### Documentation and catalog

- Commit `eea4de04f` closes the bounded catalog alignment task. Read-only workbook inspection confirms Event 6 is in the `Liberations` cluster with members `5, 6`, and the Event 6 and SCN-008 player-facing fields are populated.
- `In progress` for Event 6 and `Needs Testing` for SCN-008 are accurate status values until the implementation and runtime blockers close.
- At commit `c7a6d4986`, committed source-of-truth/resume prose still contains obsolete current-nine-package and IW-006-pending statements. The working tree already contains narrow corrections, but those edits require their own review and commit before commit-scoped documentation is clean.
- The prior completion audit's claim that the separate generic `Formables` cluster row was the Event 6 cluster mirror is superseded. Event 6 correctly belongs to `Liberations`; the separate `Formables` row is not the Event 6 membership row.

## Accepted-plan disposition

| Plan or prior finding | Current disposition |
| --- | --- |
| Seven-part Event 006 specification | Accepted source of truth; partially implemented. |
| Prior economy-capstone consumer finding | **Superseded and closed** by `a1cd50e9c`. |
| Treasury active-decision cleanup | **Implemented** by `a1cd50e9c`. |
| Treasury cooldown cleanup | **Implemented** by `c7a6d4986`. |
| DM-58 pre-cost atomic repair | **Implemented and source-level closed** by `972037edd`, `893e4d2e4`, and `8a553adb0`; live multi-member scenarios remain pending. |
| Catalog/Event Details/evolutions/Liberations/SCN-008 alignment | **Implemented and closed** by `eea4de04f`; completion statuses intentionally remain open. |
| Shared focus layout repair | **Unresolved**; fourteen blocking diagnostics remain after the unsafe broad nudge was rejected. |
| Package-specific focus-depth requirement | **Partially implemented and unresolved** across the accepted registry. |
| FORM-01 through FORM-05 plans | **Implemented and promoted** for their bounded source tranches. |
| IW-043/IW-058 improvement addendum and FORM-12/13/18 | **Gameplay implemented; runtime admission queued/blocked** on sourced portrait completion and parent-wide scenarios. |
| IW-093/IW-098 improvement addendum and FORM-24/25 | **Partially implemented; final identity, assets, formable linkage, admission, and audit work queued.** |
| FORM-48 Pacific plan | **System implemented; runtime completion blocked** by HAW/FSM admission. |
| FORM-06 through FORM-47 broad registry | **Fail-closed and unresolved**, with FORM-42 hard map-blocked. |
| Super-event 6002 production plan | **Implemented at source level; runtime predicate/playback evidence pending.** |
| Super-event 6001 plan | **Blocked** on exact-recording rights; no fallback authorized. |
| ASSET-040 through ASSET-043 animation handoff | **Not implemented.** |

No accepted plan was silently treated as complete merely because a framework, adapter, asset fragment, or source branch exists.

## Meaningful validation performed

1. Traced the focus flag and treasury idea to the new decision consumer and followed its visibility, availability, material cost, duration, reward, cancellation, cooldown, and AI blocks.
2. Traced both generation reset and active-origin termination into `independence_wave_cleanup_decision_layer`, then traced focus-runtime cleanup of the flag and idea.
3. Compared active and cooldown removal semantics with current vanilla `effects_documentation.md` and vanilla `remove_decision_on_cooldown` precedents.
4. Ran `.tools/audit_event6_allocator.py`; it passed 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, exact 3/4/5/7/10 counts, all accepted scenario types/intensities, anchor-before-optional ordering, and Event 005-first joint ordering.
5. Enumerated the ten exact content-attestation IDs and compared their current map-binding and reservation-group rows, confirming ten IDs but nine compatible groups.
6. Ran current `hoi4.focus_inspect`; it reproduced 176 focuses and fourteen blocking layout diagnostics.
7. Reconciled the current formable readiness trigger with the source-of-truth map and current package admission gate.
8. Inspected the `6001`/`6002` research, production, dispatch, and current reachability records.
9. Inspected the authoritative workbook read-only under the `xlsx` guidance and confirmed the Event 6, Liberations, and SCN-008 catalog surfaces.
10. Reviewed the post-audit commit chain and current DM-58 source/handoffs to distinguish closed findings from remaining runtime evidence.

## Meaningful validation still missing

- live ordinary 3/4/5/7 execution across representative host, tag, reservation, and Event 005 collision states;
- explicit fail-closed top-band runs until compatible capacity exists;
- joint Event 005/Event 006 collision, rollback, host-capital, and terminal-finalization scenarios;
- SCN-008 Low through Maximum across every accepted type;
- repeat-wave, evolution, used-package, origin-reset, treasury cooldown, and cleanup behavior;
- admitted-package force, politics, technology, focus, decision, AI, host, and cleanup scenarios;
- league, patron, rival-bloc, sponsorship, expulsion, transformation, crisis, and dissolution behavior with human and AI members;
- DM-58 distinct-member/owner/state, pre-existing claim, target loss, rollback, expiry, and AI resource-safety scenarios after the final repair chain;
- an authored focus reflow followed by zero-blocker inspection/render;
- route-selection, invalidation, paid-action resource safety, formable consent, and final whole-event balance sweeps;
- FORM-01 through FORM-05 success/failure/rollback/repeat runs and any later-family runtime reachability;
- every `6002` predicate, Event Log actor, settings toggle, FIFO interaction, and playback;
- `6001` production and playback after rights clearance;
- all achievement completion, visibility, invalidation, and impossible-route scenarios;
- ASSET-040 through ASSET-043 preview, fallback, sprite, GUI-state, and runtime-consumer validation after production.

Repository policy assigns live Hearts of Iron IV validation to the user.
This audit did not launch the game and does not infer live acceptance from static source.

## Remaining blockers and recommended next actions

1. Admit and independently audit one package in a tenth compatible reservation group, or obtain explicit approval for a legal map rebinding, then rerun exact-band capacity and live allocation evidence.
2. Perform a coupled-cluster authored focus reflow for the founding/economy and professional-defense crossings, then rerun `hoi4.focus_inspect` and `hoi4.focus_render`.
3. Select the next bounded package tranche and close its full map, identity, focus, decision, force, AI, localisation, asset, Event 005 collision, cleanup, and audit contract without weakening the sourced-portrait or no-fallback gates.
4. Implement or explicitly disposition FORM-06 through FORM-47; complete HAW/FSM admission for FORM-48 and the IW-043/IW-058 and IW-093/IW-098 requirements for their accepted families.
5. Clear the exact `6001` recording rights or request a user decision; do not substitute another recording without approval.
6. Produce ASSET-040 through ASSET-043 through the frame-animation workflow with authored frames, static fallbacks, manifests, previews, and GUI/runtime handoffs.
7. Commit the current source-of-truth/resume reconciliation after review so commit-scoped documentation no longer carries the superseded nine-package/IW-006 wording.
8. Run and record the missing ordinary, joint, SCN-008, economy, DM-58, league, formable, AI, balance, super-event, and achievement live matrices.
9. Request fresh focus, country, decision, localisation, asset, and completion audits only after the next accepted implementation tranche and its handoffs are committed.

## Simplifications, omissions, and fallback status

No new simplification or fallback was accepted by this audit.

Current generic framework coverage is weaker than the accepted package-specific breadth and must remain reported as partial.
Fail-closed package, formable, audio, and top-band gates are safeguards, not completion substitutes.
The event must not be marked complete while the exact ten-country bands are impossible, the focus layout fails, accepted package/formable/asset surfaces remain unavailable, or meaningful runtime and balance evidence is missing.
