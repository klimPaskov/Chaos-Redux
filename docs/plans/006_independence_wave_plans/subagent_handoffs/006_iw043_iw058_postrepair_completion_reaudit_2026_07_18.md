# IW-043 / IW-058 post-repair completion re-audit

Date: 2026-07-18
Auditor: `chaosx_event_completion_auditor` (`/root/iw043_iw058_postrepair_reaudit`)
Scope: Event 006 IW-043 Middle Volga / Volga Bulgaria on `CHU`, IW-058 Assyria on `ASY`, FORM-12/13/18, the IW-058 sovereign-autonomy alternative, their bounded country/focus/decision/event/AI/localisation/asset/documentation surfaces, exact runtime admission, and the two post-repair evidence handoffs.
Mode: read-only for gameplay and asset files. This handoff is the only file written by the audit.

## Post-fix terminal-exclusivity re-audit (2026-07-18)

**Static source verdict: PASS for the terminal-settlement exclusivity repair.**

This section supersedes the earlier high-severity branch-switch finding and
the related decision, FORM-18, AI, achievement, documentation, and next-action
statements below. The historical body is retained to show what the repair was
required to close. Bounded completion remains **HOLD only for the accepted
runtime/scenario evidence matrix**; whole Event 006 remains incomplete.

### Repair status by requested surface

| Surface | Post-fix status | Current source evidence |
| --- | --- | --- |
| Shared opening gate | Pass | `has_independence_wave_iw058_open_terminal_settlement_choice` rejects the permanent lock, either settlement mode, either transaction receipt/completion, active or applied FORM-18 state, and the already-written settlement proof (`common/scripted_triggers/006_independence_wave_iw043_iw058_package_triggers.txt:1204-1220`) |
| Branch finalization gates | Pass | `can_finalize_independence_wave_iw058_form18_terminal_settlement` rejects any sovereign-autonomy receipt/completion/mode, the lock, and final proof; `can_finalize_independence_wave_iw058_sovereign_autonomy_terminal_settlement` rejects any FORM-18 receipt/completion/applied/active state, federation mode, the lock, and final proof (`package_triggers.txt:1222-1247`) |
| FORM-18 begin and commit | Pass | `can_begin_independence_wave_form18_congress` requires the shared open-choice gate; `can_independence_wave_form18_iw058_commit` requires the FORM-18 readiness contract plus the FORM-18-specific finalization gate (`package_triggers.txt:1265-1273`, `1356-1359`) |
| FORM-18 decision | Pass | Visibility, availability, and custom cost all require the shared/can-begin gates. Activation writes the FORM-18 receipt immediately. Expiry commits only through the shared finalizer and, on attested success, writes federation mode plus the permanent lock (`common/decisions/006_independence_wave_iw043_iw058_decisions.txt:2051-2106`) |
| Sovereign-autonomy decision | Pass | Visibility, availability, and custom cost require the shared open-choice gate. Activation immediately writes the compact receipt. Expiry requires the sovereign-specific finalization gate before committing compact completion, sovereign-autonomy mode, and the permanent lock (`decisions.txt:2270-2297`, `2306-2310`, `2370-2380`) |
| Failed autonomy finalization | Pass | If partner work succeeds but terminal finalization fails closed, the rollback branch clears both definitive partner flags and the regional treaty-complete receipt; it then clears both pending partner flags after recording the applicable host-conflict or broken-talk consequence (`decisions.txt:2382-2396`). Cancellation clears the in-flight pending flags (`2416-2424`) |
| Permanent lock lifecycle | Pass | The only setters are successful FORM-18 and successful compact finalization. Repository-wide source search finds the only clear in exact IW-058 package cleanup (`decisions.txt:2102`, `2378`; `common/scripted_effects/006_independence_wave_iw043_iw058_package_effects.txt:2011`) |
| Final proof and `.5810` | Pass | `can_write_independence_wave_iw058_mesopotamian_settlement_complete` requires the permanent lock and exactly one valid settlement-mode branch (`package_triggers.txt:1361-1399`). The ratification focus remains the sole gameplay caller of `.5810`, and `.5810` calls the guarded writer (`common/scripted_effects/006_independence_wave_iw043_iw058_focus_effects.txt:492-498`; `events/006_independence_wave_iw043_iw058.txt:1162-1209`) |
| Exact package cleanup | Pass | The cleanup is guarded by original tag `ASY`, exact package id 58, and the IW-058 package flag. It removes both terminal decisions, clears the regional target, FORM-18 receipts/state, both modes, the permanent lock, regional and compact partner state, compact receipt/completion, final proof, and shared formable state (`package_effects.txt:1847-1883`, `1973-1985`, `2008-2050`, `2113-2166`) |
| AI visibility and selection | Pass in source | Both decisions use the same player/AI `visible`, `available`, and cost gates. Positive `ai_will_do` weights cannot expose a decision after either receipt or the permanent lock closes the shared gate. No separate scripted AI invocation of either decision identifier was found |

### Settlement-order proof

| Attempted order | Before `.5810` | After `.5810` |
| --- | --- | --- |
| Compact -> FORM-18 | Compact activation writes `iw058_sovereign_autonomy_compact_receipt`, immediately failing the shared opening gate and the FORM-18-specific finalization gate. Successful compact expiry additionally writes sovereign-autonomy mode, completion, and the permanent lock. FORM-18 therefore becomes invisible, unavailable, fails its custom cost, cannot begin, and cannot commit for either a human or AI | The lock and sovereign branch still reject FORM-18; the proof flag written by `.5810` is an additional rejection in both the opening and FORM-18 finalization gates |
| FORM-18 -> compact | FORM-18 activation writes `iw058_form18_federal_congress_receipt`, immediately failing the shared opening gate and the sovereign-specific finalization gate. Successful FORM-18 expiry additionally writes federation mode, active/applied formable state, completion, and the permanent lock. The compact therefore becomes invisible, unavailable, fails its custom cost, and cannot finalize for either a human or AI | The lock and federation branch still reject the compact; the proof flag written by `.5810` is an additional rejection in both the opening and sovereign finalization gates |

The narrow finalization gates also fail closed against a corrupted or legacy
state in which the opposite receipt appears while a mission is already in
flight. A failed FORM-18 attempt that writes no settlement and clears its own
receipt can return to the authored retry policy; that is not a committed
FORM-18-to-compact branch switch. A successful terminal settlement cannot be
reopened except by the exact package teardown that removes the entire IW-058
runtime package.

### Validation boundary, assets, and plan disposition

- The previous repair recommendation is implemented in current static source.
  The accepted improvement addendum's FORM-18/autonomy mutual-exclusion claim
  is now supported by the trigger and decision paths; no further design
  addendum is needed for this issue.
- Runtime remains explicitly unproven. No live human/AI crossover attempt,
  mission expiry, invalidation, `.5810`, cleanup/re-entry, ordinary release, or
  SCN-008 run was supplied in this re-audit. SCN-008 may therefore remain
  `Needs Testing`, and bounded completion remains on hold for that evidence.
- Repository-wide setter/clearer searches found two lock setters and one
  exact-cleanup clearer; the `.5810` caller search still found one gameplay
  caller.
- No fallback, weaker substitute, or undisclosed simplification was found in
  the terminal-exclusivity repair.
- The bounded IW-043/IW-058 package still contains exactly eight large
  institutional country-leader portraits. Its character file defines only
  civilian large portrait consumers, its portrait `.gfx` file defines no
  small/advisor sprite, and its manifest explicitly supplies no advisor,
  advisor portrait, advisor sprite, or dossier card. **Zero custom IW-043 /
  IW-058 advisor visuals are preserved.** No asset was created, requested,
  wired, converted, or modified by this re-audit.
- Do not spawn `chaosx_improvement_loop_planner` for this repair. The accepted
  addendum already covers the intended depth; remaining work is runtime proof
  and evidence reconciliation, not an unresolved design-depth gap.

No gameplay, localisation, spreadsheet, GFX, image, portrait, advisor, or
other asset file was changed. This post-fix section is the only audit write.

## Verdict

**HOLD for bounded completion. Do not claim whole Event 006 completion.**

The regional-settlement-partner repair closes the earlier former-host-only
omission in static source. The autonomy compact now locks one counterpart,
records five treaty chapters, revalidates the locked counterpart at expiry and
again at final proof, and keeps `chaosx.nr006.5810` on one final-focus caller.
The parent non-portrait approval and catalog-alignment verification also close
their earlier evidence gaps. Exact IW-043/IW-058 compile-time admission remains
present for ordinary and SCN-008 dispatch.

One new high-severity completion blocker remains: **FORM-18 federation and the
sovereign-autonomy compact are not transactionally mutually exclusive.** Each
success clears the other *mode flag*, but the FORM-18 congress does not exclude
an existing sovereign compact and the compact does not exclude an existing or
completed FORM-18 federation. The player or AI can therefore complete one,
later complete the other, and overwrite the selected settlement mode. If the
final ratification focus has already written the settlement proof, that proof
is not revoked when the later transaction switches modes.

The accepted runtime matrix is also still unrecorded. Static inspection and the
partial Event Chain Viewer projection are not in-engine execution evidence.
SCN-008 remains `Needs Testing` in the authoritative workbook.

No gameplay fallback was found. No asset fallback was accepted. No custom
Event 006 advisor visual asset is present, which is the required bounded
outcome.

## Completion status by surface

| Surface | Status | Current evidence | Remaining issue |
| --- | --- | --- | --- |
| Accepted specifications and improvement addendum | Partial | All seven accepted Event 006 spec parts and the dated IW-043/IW-058 addendum describe the exact carriers, five proof writers, FORM-12/13/18 contracts, five autonomy treaty chapters, and bounded assets | The addendum checks FORM-18/autonomy mutual exclusivity as complete even though the current decision gates permit a later cross-mode transaction |
| Exact runtime admission | Pass in static source | `has_independence_wave_runtime_package_adapter_for_execution_id` and `has_independence_wave_runtime_package_content_attestation_for_execution_id` list only the exact `iw_043` and `iw_058` IDs among the admitted set; ordinary preflight binds them to `CHU` and `ASY`; scenario preflight uses the same content authority | Admission is source-backed, not a live ordinary-release or SCN-008 execution result |
| Exact carrier, origin, anchor, and collision gates | Pass in static source | IW-043 requires `CHU`, package 43, Event 006 origin, state 249, and the IW-043/IW-046 mutex; IW-058 requires `ASY`, package 58, Event 006 origin, and state 676. Both use origin-safe tag availability and host-remnant reservation | Live setup, host-remnant, optional state 256, cleanup, and fresh-generation re-entry are untested |
| Vanilla and Event 005 compatibility | Pass in static source | The exact negative compatibility guards keep active Event 006 CHU/ASY away from the vanilla Idel-Ural, Neo-Assyria, and Neo-Mesopotamia shortcuts while preserving ordinary and Soviet Collapse carriers | No live decision-card/load-order check is recorded |
| Country package, forces, ideas, politics, leaders | Pass in static source | Current setup/final validation writes force, cosmetic, institutional, political, focus-framework, adapter, and writer receipts. The country-package final audit covers exact politics, eight institutional characters, three idea slots per package, paid bounded forces, and cleanup | Repeated dispatch, conversion, cleanup, and no-duplication behavior remain untested in engine |
| Focus tree | Partial | 48 package focuses remain imported and structurally reachable; title/description/tooltip and icon coverage is present; final `.5810` presentation belongs to the ratification focus | The focus/decision terminal surface does not lock the two IW-058 settlement transactions against later cross-mode completion |
| Decisions and missions | **Blocked** | 38 decision IDs plus 2 categories cover package actions, paid congresses, reconciliation, six staged-integration actions, and the autonomy compact | FORM-18 and sovereign autonomy can be completed sequentially in either order; live timer, cancellation, anchor-loss, and retry behavior is also unproven |
| Event chain | Pass in static source | 26 triggered events remain present. Regional-guarantee option `.5807.a` saves the qualifying target; `.5810` is the final settlement presentation; `.5811` and FORM founding events retain explicit consent/sovereignty text | No live chain playthrough or bounded complete Event Chain Viewer result exists |
| FORM-12 / FORM-13 | Pass in static source | Exact carrier gates, 3 members / 3 consents / 3 distinct consenting anchors, paid 180-day frozen ledgers, terminal recount, carrier-only cosmetics, and staged sovereign integration are present. The two route proof setters are sole and mutually clearing | Human/AI reply mixes, exact-minimum/surplus ledgers, anchor loss, cancellation, and retry have no runtime record |
| FORM-18 | Partial | Exact carrier gates, 2 members / 2 consents / 2 distinct consenting anchors, paid 180-day ledger, defensive-method preflight, carrier-only cosmetic, and staged sovereign integration are present | Its congress availability does not exclude an autonomy receipt/compact/mode; success can overwrite sovereign-autonomy mode |
| Sovereign-autonomy partner transaction | Pass for the repaired counterpart lock; blocked as a settlement mode | Former-host and named regional-guarantor paths are reachable. Start deterministically chooses the valid former host first or the regional guarantor second, writes exactly one pending flag, and expiry follows only that pending branch | The compact can still start after FORM-18 because it does not exclude FORM-18 receipt/completion/formable state/federation mode |
| Five autonomy treaty records | Pass in static source | `has_independence_wave_iw058_autonomy_treaty_records` requires paired record/completion flags for boundary, return/protection, church-civil jurisdiction, transit/property, and security. The external helper writes four chapters; jurisdiction remains owned by `.5803` | Missing-one-chapter and cleanup behavior remain untested live |
| Stale counterpart rejection | Pass for current-state invalidation in static source | Regional final proof reuses `has_independence_wave_iw058_regional_settlement_partner`, which requires an existing independent target, bilateral peace, a live guarantee of ASY, and the accepted regional/tag boundary. The former-host proof requires the saved live host, completed security settlement, and bilateral peace | The global regional target has no separately stored partner-generation receipt; target death/revival and Event 006 partner re-entry remain an engine-runtime risk to test |
| `.5810` ownership | Pass | Repository search finds exactly one gameplay caller: `independence_wave_complete_focus_iw058_ratify_mesopotamian_settlement` in the IW-058 focus-effect file. It checks `can_write_independence_wave_iw058_mesopotamian_settlement_complete` first | A later cross-mode transaction can change the settlement after the one-time focus has already presented and written the proof |
| Sovereignty / shortcut audit | Pass in scoped source | The bounded decision, package-effect, focus-effect, and event files contain no annexation, autonomy/subject creation, state-owner transfer, blanket-core grant, OOB load, or unit-creation shortcut for FORM-12/13/18 or the compact. Members retain tags, territory, units, origin, and country content | Runtime scope behavior is unproven, but no prohibited source mutator was found |
| Signature achievements | Partial | Two IW-043 and three IW-058 proof flags each have one direct setter effect; client capture permanently clears and disqualifies the IW-058 proof set for the current generation | Settlement proof can survive a later FORM-18/autonomy cross-mode switch; positive and false-positive runtime cases remain unrecorded |
| AI | Partial | Sixteen exact strategy plans, decision `ai_will_do` blocks, and bounded consent scoring exist | Positive weights remain on both terminal settlement transactions and no cross-mode lock prevents AI from taking the later alternative; no AI runtime scenario is recorded |
| Bounded localisation | Pass | The repaired regional-guarantor alternative, five chapters, sovereignty, non-client status, final settlement, all 48 focuses, 38 decisions, 26 events, and both achievements have current English text coverage according to the final localisation audit and current source | No live decision/focus/event UI render is recorded |
| Bounded non-portrait assets | Pass | The dated parent approval records native/original review of 10 flag designs, 2 reports, 20 focus icons, 2 categories, 16 decision icons, 6 ideas, and the 3-state Assyria achievement family. Scoped asset/runtime paths show no later modification | Does not authorize wider Event 006 assets or whole-event completion |
| Event 006 advisor visual assets | Compliant absence | No scoped runtime filename, sprite registration, character consumer, or bounded manifest supplies a custom Event 006 advisor visual asset | None; do not create, request, wire, or document one for this tranche |
| Protected BAY/RHI portraits | Pass | Current SHA-256 values remain `7F0AF64FDF4FECD49DF454D1198935BB3CE6A8F74AFC1AC82F8223704EAAAD2B` and `AA61CC3A12FB6670B690C7685FEB9383383CE58599C9E6D6E7C14F20FAB3BCE2`, exactly matching the parent approval | None in this tranche |
| Event Details, evolutions, cluster, and catalog workbook | Pass | Direct read-only comparison confirms `Events!C7`, `Events!D7:H7`, `Scenarios!B9:E9`, and `Clusters!B3:C3` exactly match their localisation sources. Candidate/formable IDs are deliberately omitted from the generic Event Details under the accepted catalog direction | `Events` remains in progress and `Scenarios!F9` remains `Needs Testing`, correctly reflecting wider and runtime work |
| Documentation | Partial | The source-of-truth map, resume packet, system document, catalog verification, regional-partner repair handoff, and parent approval are present | Several current claims overstate mutual exclusion; some source comments and historical focus/localisation handoffs retain superseded fail-closed or `.5810` caller wording |
| Runtime/scenario proof | **Missing / blocker** | Static admission and source-chain evidence exist | No accepted high-value ordinary/SCN-008, human/AI, transaction, invalidation, cleanup, or achievement matrix is recorded |

## High-severity finding: settlement-mode branch switching remains possible

The accepted source contract is explicit:

- Part 3 calls sovereign autonomy a mutually exclusive bilateral settlement
  mode and says the final presentation follows the complete federal or
  sovereign transaction.
- The improvement addendum says FORM-18 writes federation mode, the compact
  writes sovereign-autonomy mode, and the two mode flags are mutually
  exclusive. Its exit checklist marks that requirement complete.
- The current system document and source-of-truth map repeat the same claim.

The source only enforces exclusivity at each writer:

1. `independence_wave_iw058_hold_form18_federal_congress` is visible when its
   own receipt is absent and no shared formable is active. It does **not**
   exclude `iw058_sovereign_autonomy_compact_receipt`, compact completion, or
   sovereign-autonomy mode. On success it sets federation mode and clears the
   sovereign-autonomy mode.
2. `independence_wave_iw058_ratify_sovereign_autonomy_compact` is visible when
   its own receipt is absent. It does **not** exclude the FORM-18 receipt,
   completed congress, active Mesopotamian federation, or federation mode. On
   success it sets sovereign-autonomy mode and clears federation mode.
3. The shared paid-transaction lock prevents simultaneous payment, but it does
   not prevent the second transaction after the first has committed.
4. The final focus is one-time. Its proof flag is not invalidated if the other
   settlement transaction later overwrites the mode.

Consequences:

- compact -> FORM-18 can replace the sovereign mode with federation;
- FORM-18 -> compact can replace federation mode with sovereign autonomy while
  the formable remains active;
- either sequence can occur before final ratification, and a later switch can
  also leave an already-written settlement proof describing the earlier mode.

This is not merely a documentation issue. It violates an accepted route lock,
creates an achievement false-positive path, and gives AI two sequentially
available terminal transactions.

## Regional partner repair verification

### Passed in source

- `.5807.a` first writes the sovereignty-safeguarded guarantee and external
  security record, clears any prior regional target, and saves the named target
  only when `is_independence_wave_iw058_legitimate_regional_settlement_partner`
  passes.
- The legitimate-partner trigger requires existence, independence, bilateral
  peace, a live guarantee of ASY, and either the accepted same-region Event 006
  contract or the reviewed explicit regional tag set.
- Compact start uses an `if`/`else_if`: a valid completed peaceful former-host
  settlement is locked first; otherwise the valid regional target is locked.
  It sets one pending flag and clears the other.
- Expiry reads only the pending flag. It cannot silently choose the other
  counterpart if the locked one becomes invalid.
- The regional expiry path rechecks the saved target and sovereignty-safeguard
  records before writing the four external chapters and the regional treaty
  receipt.
- Final proof requires the matching completed partner-mode flag. The regional
  branch calls the full live-target trigger again; the former-host branch
  rechecks the saved host, security settlement, and bilateral peace.
- Setup and exact package cleanup clear the package-owned global regional
  target; cleanup clears all partner, treaty, mode, and compact receipts.

Thus a currently dead, subject, hostile, or non-guaranteeing regional target
cannot pass final proof in the inspected source, and the compact cannot switch
from one pending counterpart branch to the other. The remaining target-
generation and timing uncertainty is runtime evidence, not a discovered
current-state bypass.

## Five treaty chapters and terminal proof

The compact proof requires these five paired chapters:

1. boundary;
2. return/protection;
3. church-civil jurisdiction;
4. transit/property;
5. security.

`independence_wave_record_iw058_autonomy_external_treaty_terms` writes only
chapters 1, 2, 4, and 5 after exact ASY sovereignty, all four community
guarantees, and Mosul ownership/control. Chapter 3 is written only by the
church-civil competence event and must already exist before compact start and
regional completion. The final writer trigger requires all ten paired flags;
no helper can manufacture the jurisdiction record.

The only gameplay call to `chaosx.nr006.5810` is at
`common/scripted_effects/006_independence_wave_iw043_iw058_focus_effects.txt:495`.
The two `.5810` options call the same guarded settlement writer effect. No
decision, integration stage, or FORM-18 founding event calls `.5810`.

## Exact runtime admission and scenario disposition

Static ordinary admission is exact:

- the compile-time adapter and content-attestation OR lists include package
  IDs 43 and 58 explicitly;
- ordinary preflight binds 43 to original tag `CHU` and 58 to `ASY`;
- IW-043 and IW-058 package availability uses origin-safe dormant carriers;
- IW-043 automatic weight is high-chaos-only and reserves 249 plus optional
  safe 256; IW-058 automatic weight is high-chaos-only and reserves 676;
- SCN-008 preflight mirrors the same content attestation and exact tag wrappers;
- the scenario ranking list contains both package IDs.

This is compile-time admission, not runtime attestation. No dated evidence runs
the accepted scenario matrix. The authoritative workbook correctly records
SCN-008 as `Needs Testing`.

Minimum remaining runtime cases affecting confidence:

1. ordinary high-chaos and SCN-008 release/setup for exact CHU and ASY,
   including living-carrier rejection, host remnant, optional 256, collision,
   cleanup, and fresh eligible generation;
2. FORM-12/13/18 exact-minimum and surplus member/consent/anchor ledgers with
   human replies, AI replies, timeout, cancellation, anchor loss, and cooldown;
3. FORM-18 negotiated and defensive methods, including offensive-pretext
   rejection and member sovereignty after both integration stages;
4. autonomy former-host and regional-guarantor paths, with target death,
   subjection, bilateral war, guarantee withdrawal, and target invalidation at
   start, during the mission, after expiry, and before the final focus;
5. each of the five autonomy chapters missing in turn;
6. attempted FORM-18/autonomy crossover in both orders, before and after final
   ratification;
7. `.5810` and all five proof writers on positive and false-positive paths,
   including permanent client-capture rejection;
8. repeated political/leader dispatch and transaction cleanup without a
   duplicate force, refund, or stale proof receipt.

## Asset and catalog disposition

The parent non-portrait visual approval is accepted evidence for the bounded
families. No scoped asset/runtime file is currently modified after that review,
and the two protected portrait hashes still match exactly. The separate large
institutional portrait review remains its own authority.

The catalog-alignment verification is also confirmed directly against the
workbook rather than inferred from the CSV exports. Exact comparisons passed
for the generic Event Details, five evolutions, eight scenario type labels,
four intensity descriptions, and Liberations cluster fields. The deliberate
absence of candidate/formable IDs from generic Event Details follows the
accepted player-facing direction and is not a gap.

The bounded package contains no custom Event 006 advisor visual asset. This is
the accepted scope boundary, not an asset omission.

## Documentation discrepancies

1. `006_source_of_truth_map.md:93`, the resume packet, the bounded system
   document, and the addendum checklist claim FORM-18/autonomy mutual
   exclusivity. Current transaction gates do not support that completion claim.
2. `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`
   still comments that optional FORM-12/13/18 adapters remain fail-closed even
   though exact package setup now writes their attestation flags.
3. The header comment in
   `common/scripted_triggers/006_independence_wave_iw043_iw058_package_triggers.txt`
   repeats the same fail-closed adapter claim.
4. `quality/spec_acceptance_checklist.md` still lists sovereign-autonomy
   ordering review and catalog alignment as remaining gates. Catalog alignment
   is now closed; ordering ownership is closed, but transactional mutual
   exclusion is not.
5. Historical focus/localisation handoffs contain superseded body text about a
   decision-owned `.5810` call or “40 actual decisions.” Current source has one
   focus-owned caller and 38 decisions plus 2 categories.

The older event-completion re-audit has an explicit post-audit resolution note
and correctly delegates the new bounded verdict to a later audit; its historical
body should not be read as current authority.

## Accepted plan and handoff disposition

| Accepted plan/evidence | Disposition |
| --- | --- |
| `006_iw043_iw058_signature_packages_improvement_addendum_2026_07_18.md` | Implemented for most exact-carrier package surfaces; **not closed** because the checked FORM-18/autonomy mutual-exclusion requirement is false in current source and runtime scenarios remain open |
| Regional settlement-partner audit | Repair accepted in static source for counterpart selection, live validity, five records, and final proof revalidation; its live target lifecycle cases remain queued |
| Parent non-portrait visual approval | Implemented / PASS for the bounded reviewed families; no wider Event 006 completion implied |
| Catalog alignment verification | Implemented / PASS; direct workbook/localisation comparison reconfirmed; SCN-008 test status remains open |
| Country-package final audit | Current for exact carriers, politics, leaders, forces, assets, and cleanup; static-runtime limitation retained |
| Focus closeout audit | Current for 48-node structure, localisation, icons, and final-focus `.5810` ownership; its completion wording is narrowed by the settlement-mode branch-switch finding |
| Final decision/transaction audit | Current for consent-only anchors, defensive preflight, paid ledgers, cleanup, and sovereignty preservation; must be rerun after the mutual-exclusion repair |
| Final localisation audit | Current for bounded key coverage and wording; its decision count should be read as 38 decisions plus 2 categories |
| Whole Event 006 plans and audits | Queued / incomplete; this bounded re-audit does not promote any other package, formable, asset family, scenario result, or whole-event completion claim |

## Meaningful validation performed

- Traced `.5807.a` through the persistent regional target, compact start lock,
  180-day expiry branches, five-record trigger, final focus, `.5810`, and the
  guarded settlement proof writer.
- Searched the complete repository for `.5810` gameplay callers and found one.
- Enumerated the five proof-flag setter sites and confirmed one setter effect
  for each of the two IW-043 and three IW-058 proofs.
- Inspected both FORM-18 and compact visibility, availability, transaction,
  success, cancellation, mode, and receipt gates; this found the cross-mode
  branch-switch blocker.
- Inspected exact ordinary and SCN-008 compile-time admission for package IDs
  43/58 and their CHU/ASY wrappers.
- Searched the bounded transaction/event/effect files for annexation, subject,
  autonomy, state-owner, blanket-core, OOB, and unit-creation shortcuts; none
  was found.
- Read the authoritative workbook directly and compared its bounded Event,
  Evolution, Scenario, and Cluster fields to current localisation; every
  comparison passed. Confirmed SCN-008 remains `Needs Testing`.
- Recomputed the protected BAY/RHI SHA-256 hashes; both match the parent
  approval record exactly. Scoped runtime and asset filename/registration scans
  confirm the required absence of a custom Event 006 advisor visual asset.
- Ran a narrow `hoi4.event_inspect` trace from `.5807`. It returned
  `EVENT_INSPECTED_PARTIAL` with artifact
  `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/032908ec1dce57983181dcf368da4842f05a3e72c0e23846c482406e1f13ddc0/d61d1d806f66a312a8a7f517a5a5989e66135225dbe0c782a945fac21da2082b/event-trace-dbe9f90593f0.json`.
  The 34 MB artifact projects 4,062 sources and reports a partial graph, so it
  is recorded as a tool limit and not used as completion evidence.

## Remaining blockers and recommended next actions

1. Add one shared, fail-closed IW-058 settlement-mode lock and enforce it at
   both terminal transaction visibility/availability and completion. FORM-18
   must reject an active/received/completed sovereign compact; the compact must
   reject a FORM-18 proposal/receipt/completion/active formable. Preserve the
   one `.5810` caller.
2. Re-audit achievement proof lifecycle after that repair. A later mode change
   must not leave `independence_wave_assyria_mesopotamian_settlement_complete`
   describing an abandoned settlement.
3. Run the minimum runtime matrix above, prioritizing counterpart invalidation,
   both attempted settlement-order switches, `.5810`, human/AI congress
   ledgers, client-capture disqualification, and cleanup/re-entry.
4. Rerun the decision-mission and event-completion audits after the route lock.
5. Reconcile the source-of-truth map, resume packet, addendum checklist, system
   document, stale trigger comments, and quality checklist only after source
   and runtime evidence agree.
6. Keep the catalog workbook unchanged unless player-facing localisation
   changes; its bounded mirror is already aligned.

## Improvement-loop recommendation

**Do not spawn `chaosx_improvement_loop_planner` for IW-043/IW-058 now.** The
accepted addendum already supplies the intended depth and explicitly forbids a
parallel pass while its closeout is unresolved. The remaining work is a narrow
transactional route lock, runtime proof, and evidence reconciliation—not a
design-depth gap.

## Simplifications, omissions, and blockers

- No gameplay or asset fallback was found.
- The regional partner repair is present and no current-state stale target can
  pass its inspected final proof.
- The FORM-18/autonomy mutual-exclusion claim is overstated and blocks bounded
  completion.
- The accepted runtime/scenario evidence is absent and blocks bounded and
  whole-event completion.
- Catalog/event-detail alignment and bounded non-portrait visual approval are
  closed.
- The required absence of a custom Event 006 advisor visual asset is preserved.
- Whole Event 006 remains incomplete.

## Files changed by this audit

- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw043_iw058_postrepair_completion_reaudit_2026_07_18.md`

No gameplay, localisation, spreadsheet, GFX, image, portrait, advisor, or other
asset file was changed.

## Skills used

- `chaos-redux-events`
- `chaos-redux-improvement-loop`
- `chaos-redux-subagents`
- `chaos-redux-event-planning`
- `chaos-redux-event-assets`
- `hoi4-decisions-missions`
- `xlsx` (read-only workbook verification)

No skill was created or updated.
