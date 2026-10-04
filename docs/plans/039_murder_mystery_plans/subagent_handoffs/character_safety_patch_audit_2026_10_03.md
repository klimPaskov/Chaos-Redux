# Event 039 bounded character-safety patch audit

Date: 2026-10-03.
Status: preliminary source audit delivered at the parent's request before pending MCP work completes.
Scope: the current parent character-safety patch and adjacent producer, capture, reconciliation, and cleanup boundaries.
This report does not certify opening succession, foreign-leader transactions, complete inheritance, Part 18, or the full event.
Only this handoff is written by this auditor.
Gameplay, localisation, assets, workbook, staging, commits, and game launch remain untouched by this auditor.
The parent owns every source fix and any isolated tranche commit decision.

## Preliminary blocking findings

No newly introduced P0 has been established by this source review.
The following P1 findings need parent disposition before the reviewed safety boundary can be considered finished.
These are source traces, not observed engine failures.

### P1-01: Founder resolution and registration failure do not abort country creation

Evidence: `common\scripted_effects\039_murder_mystery_integration_effects.txt:1632-1663,1676-1686,1705-1712` and `common\scripted_triggers\039_murder_mystery_runtime_triggers.txt:499-511`.
The new producer publishes the First Knife pointer only after `murder_mystery_ruling_character_resolved`, and the recruited-roster registration can independently fail.
The downstream country commit checks the created leader's name and territorial postconditions, but does not require the successful ruler-resolution receipt, `murder_mystery_first_knife_registered`, or the exact unused founder row owned by that candidate.
A stale anchor, zero matches, ambiguous matches, or exhausted registry can therefore leave the country-creation path able to commit without a capturable registered founder.
This is a gap at the new producer's integration boundary, rather than a defect in the helper's exactly-one gate.

Needed parent fix: require the current candidate's successful ruler resolution and exact founder registration as country-creation postconditions, and roll back the candidate when either fails.
Tie any consumed founder pointer to this attempt's resolved character and owner, rather than accepting only `has_event_target = murder_mystery_first_knife_character` at line 1645.
Exercise duplicate-anchor failure, no ruler, failed registration, and capacity exhaustion through the country-commit boundary.

### P1-02: The live-central receipt can remain true after territorial loss

Evidence: `common\scripted_effects\039_murder_mystery_character_effects.txt:116-129`, `common\scripted_effects\039_murder_mystery_integration_effects.txt:688,707,1097-1105,1180-1189,2033-2047`, and `common\scripted_effects\039_murder_mystery_runtime_effects.txt:2042-2071`.
The new shock helper clears and recalculates `murder_mystery_live_central_after_capture` only when called after a fresh successful core capture.
The permanent global core receipt blocks later core selection, so that refresh cannot be relied upon after the central country loses its land or disappears.
The late scheduling gate reads the saved actor flag, and the country-loss cleanup does not invalidate or recalculate it on that investigator.
Thus a receipt that correctly prevented inheritance while the state was alive can keep preventing it after the state is gone.
This is a new receipt-lifetime gap adjacent to the intentionally unfinished inheritance implementation.

Needed parent fix: establish current central existence and owned-land status at the scheduling or country-loss boundary, and invalidate the investigator's stale live-status receipt through an exact owner callback.
Preserve `murder_mystery_core_capture_committed` and the once-only shock receipt.
The complete inheritance rewrite remains separately open and is not certified by such a narrow repair.

### P1-03: Malformed positive-ID rows escape reconciliation

Evidence: `common\scripted_effects\039_murder_mystery_runtime_effects.txt:493-508,533-542`.
The rejection limit places the nonpositive-ID test beside an `OR` of invalid disposition, role, protection, used-state, and generation tests.
Those two siblings form an AND, so a positive-ID row with generation zero, invalid role, or invalid used-state does not satisfy the rejection limit.
The new selected-target validator rejects several such values correctly, but the malformed row remains in the registry and consumes capacity.
This predicate is already present in the supplied `.before` snapshot and is an adjacent existing defect, not a defect introduced by replacing CHARACTER-scope `exists`.

Needed parent fix: make the row-invalid test a union of the individual invalid conditions while preserving consumed tombstones with valid scalar fields.
Check a valid positive ID with invalid generation, role, protection, and used-state individually.
The current source-contract script does not test this behavior.

## Surface status

| Surface | Source-review status | Evidence and limit |
| --- | --- | --- |
| Actual validation actor | Source-reviewed | Runtime effects:549-590 saves `murder_mystery_target_validation_actor` and returns the owner receipt there. No stale ROOT read remains inside this validator. |
| COUNTRY existence and exact recruited CHARACTER identity | Source-reviewed | Character triggers:8-27 checks COUNTRY `exists` and `any_character` plus `is_character`. Named/opening registration and selected-target checks use these predicates. |
| Duplicate IDs, used-state, generation, role and protection bounds | Source-reviewed with reconciliation defect | Runtime effects:578,609,638-683 and runtime triggers:315-369 reject duplicate matches and consumed or mismatched selected rows. P1-03 affects reconciliation. |
| Protected and owner-managed dispositions | Source-reviewed | Runtime effects:628-649 marks protected dispositions and owner management. Runtime triggers:336-354 prevents named removal for those flags. Generic office handling does not retire a character. |
| Selection cleanup and preparation | Source-reviewed | Runtime effects:706-724 preserves the core-offender classification during preparation. Lines 789-809 clear selected used/generation/expected-generation, callback, and global selected targets. |
| Immutable baseline offender | Source-reviewed | Integration effects:705-737 restricts the baseline to the exact original host before any territorial state, without a founder pointer, and retains the original ID/generation between attempts. |
| Permanent capture receipt | Source-reviewed | Integration effects:787-789,804-806 records a global latch and selected ID/generation. Selection gates at 688 and 707 read that latch. No duplicate core removal is established along the reviewed immediate select/prepare/capture sequence. |
| Ruling-character anchor | Helper source-reviewed, producer partial | Character effects:13-51 requires authorization, refuses inherited anchors, uses native COUNTRY trait operations, counts exactly one recruited leader match, removes its added anchor before return, and consumes authorization. P1-01 leaves the producer/commit boundary incomplete. |
| Route successor before founder retirement | Source-reviewed | Character effects:56-111 installs and verifies the route-priority successor. Integration effects:772-789 revalidates ownership and recruitment before CHARACTER-scope retirement and writes receipts to the explicit capture actor. |
| Living central country continuation | Partial | Character effects:116-147 applies one bounded Cohesion/Reach shock and no Chaos, retirement, world scan, force removal, or runtime cleanup. Country existence and owned land prevent immediate permanent resolution. P1-02 affects later loss. |
| Early permanent resolution | Source-reviewed with lifecycle limits | Integration effects:1170-1178 records one permanent-resolution presentation receipt and calls `finalize_runtime`. Runtime effects:2108-2160 clears active registries and marks runtime resolved. This is not persistence or complete cleanup execution evidence. |
| Legacy inheritance | Explicitly open | Integration effects:1205-1315 retains random leader selection, CHARACTER-scope `exists`, ROOT retirement receipt, and country/global receipt mismatches. The parent explicitly excludes its completion from this tranche. |
| Opening, foreign-leader handling, Part 18, full event | Outside certification | Parent explicitly leaves these surfaces open. No grounded generic portrait fallback is accepted or inferred. |

## Validation performed and missing

Read the latest repository `AGENTS.md`, `chaos-redux-events`, `chaos-redux-subagents`, `chaos-redux-improvement-loop`, and `chaos-redux-event-planning`.
Their application here preserves the read-only boundary, explicit requirement dispositions, bounded source evidence, and separation of implementation facts from completion claims.
No additional asset or 3D skill is applied because asset production, visual review, and model packages are outside this assignment.

Read and ran `python -B docs\plans\039_murder_mystery_plans\validation\character_safety_2026_10_03\check_character_contracts.py`.
Result: PASS for its owner-local receipt, recruited-roster, used/generation, bounded-row, exact-ruler, immutable-baseline, successor-before-retire, core-receipt, and live-central source assertions.
The script explicitly reports that it simulates no Clausewitz engine behavior.
Its text-presence and ordering assertions do not cover the producer failure-to-commit path, stale live-status receipt, malformed-row logic, native retirement results, or save/reload persistence.

Compared the two named dirty working-tree `.before` snapshots against current source with read-only `git diff --no-index`.
HEAD is not the patch baseline.
The runtime and integration snapshots retain SHA-256 `8F4B63001770D286E1E9DE736A9ABFFC4378F02273D2CA0B782CCE0837D9085A` and `98928E7645082F7CC453FAD74FAE4DFDDA2D75381A5A266D569D5B9A3BADDFEC` respectively.
The source-contract PASS does not disposition the parent's prior objective work or other agents' changes.

## NoEngineEvidence

The connected `ALL_TOOLS` inventory exposes no `mcp__hoi4_agent_tools__hoi4_event_inspect`, `hoi4_event_render`, or `hoi4_event_compare` callable, and no tool-discovery route for loading them.
It also exposes no HOI4 reference or script-validation routes.
Only unrelated Blender HOI4 tools are exposed.
No confirmed live schema, server version/health, event revision, event graph, comparison artifact, render URI, or runtime scenario result is available to this auditor.
Mandatory narrow event inspect/render/compare is therefore blocked by route absence in this session, not by a timeout from an attempted event call.
No source-only result is equivalent engine or MCP evidence.

Parent-reported pending work is retained without duplicate requests: reference-context request with limit 4 and timeout 600, narrowed retry limit 2, reference-search request with limit 3 and timeout 600 with installed-document retry limit 1, and source-lookup validator definition request with limit 12.
No opaque continuation URI, request ID, or final result for those pending calls was supplied to this auditor.
Their completion remains pending parent reconciliation, and this preliminary handoff does not wait for them.

The weighted founder-selector pass is already routed through `chaosx_ai_probability_auditor` in `subagent_handoffs\character_selection_probability_2026_10_03.md`.
That handoff records baseline, after-source review, the latest integration hash `D48AEEC6EE032F110B6588E5CAA20AEAAED57EC9A482068330B566C303D11254`, and absent probability-inspect/compare routes.
The same named scenarios remain unresolved: `RULING_ONE_ROLE`, `RULING_WITH_OPPOSITION`, `FOUNDER_WITH_COPIED_ROSTER`, `NO_RULING_LEADER`, and `DUPLICATE_ANCHOR_FAIL_CLOSED`.
This auditor reuses that routed pass without inventing probabilities or reopening the excluded opening selector.
No new numeric AI/probability evaluation is claimed.

## Local reference evidence

Read installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md:1008-1021,3010-3029,3743-3761,5946-5959,6427-6447,6496-6512`.
Read installed `triggers_documentation.md:1272-1279,2708-2715,3640-3652,4951-4958,5345-5352,5408-5415` in the same documentation directory.
These establish the documented COUNTRY trait operation, COUNTRY roster traversal, CHARACTER identity/trait/retirement scopes, leader-name criteria, and event-target scope support.
The documented same-name `create_country_leader` behavior supports reuse of a role, without proving native postconditions for this patch.
The document SHA-256 values are `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF` and `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29` respectively.

Read offline wiki `Scopes - Hearts of Iron 4 Wiki.md:260-267,401-405`, `Effects - Hearts of Iron 4 Wiki.md:136,2940-2942`, `Data structures - Hearts of Iron 4 Wiki.md:263-275,303-327,434-448`, and `Triggers - Hearts of Iron 4 Wiki.md:1759,2054`.
Their SHA-256 values are respectively `18EF5249E4991F5427ECA9EC4A2F66DD47F51E26A491C730ADC622F1F5DB1B49`, `997DDB09BFD63EFB41A425149C46BD812D5F8953217A403386B2F6C85196AA0C`, `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4`, and `ABC51AD18A2C46E46D47BAA795C5A840EBAF7C4AE3E777426C64A9F4C0C0CE06`.
These are local fallback reads, not MCP-returned source revisions.

Read approved Kaiserreich `C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\1521695605\events\FNG events (Fengtian).txt:6829-6872`, SHA-256 `F17DDF705B71ABD94B6B30BE765065E42B12D966E46AC38D5C4290A208381F2F`.
It directly uses `is_character = event_target:leaker` in CHARACTER scope.
The parent also reports vanilla Germany focus lines 8090-8103 as a dynamic-character precedent, which was not independently reopened as a focus-tree audit in this bounded task.

## Accepted-plan disposition and documentation limits

The current parent instruction accepts the bounded safety requirements and explicitly leaves global inheritance and grounded opening succession unfinished.
`docs\events\039_murder_mystery.md:7-13` records package implementation authority and incomplete status.
Part 3's exact ownership, disposition, safe succession, and duplicate-targeting requirements remain applicable to this tranche.
The helper/validator work is implemented in source with the partial status and validation limits above.
The architecture handoff `capture_inheritance_repair_architecture_2026_10_03.md` records its algorithms as unresolved proposals pending parent review.
This audit does not promote those proposals into accepted specs.

Opening random selection and a generic fictional individual used for grounded opening succession remain explicit blockers from parent context and the separate opening audit.
Legacy inheritance remains explicit unfinished work, rather than an accepted fallback.
Asset provenance, portrait replacement, broad event logs/details/evolutions, catalog alignment, and workbook content are not audited here.
No claim that those surfaces are finished follows from this source tranche.

## Reviewed current source identities

| Source | SHA-256 |
| --- | --- |
| `common\scripted_effects\039_murder_mystery_runtime_effects.txt` | `CB807179ED96C0B2C55743F7BE482CAF04B9EBBAA74CD6381EA18087FCD223E2` |
| `common\scripted_effects\039_murder_mystery_integration_effects.txt` | `D48AEEC6EE032F110B6588E5CAA20AEAAED57EC9A482068330B566C303D11254` |
| `common\scripted_effects\039_murder_mystery_character_effects.txt` | `564DDF1FB860A856BDA4159332087B0F28E4419121B7662D0806EB4DAE9DB654` |
| `common\scripted_effects\039_murder_mystery_character_effects.md` | `EC7648FC1354A9549065838677ED8A23A62C5CC4D85D3ADAC4B5B15BEF24261F` |
| `common\scripted_triggers\039_murder_mystery_runtime_triggers.txt` | `A0DC14AB68F4F946C8006972011875EC0E00A187E476EA95BCF5CC4ED634D0DC` |
| `common\scripted_triggers\039_murder_mystery_character_triggers.txt` | `DDB55A57B58A3BD45003EF4C7EE3E209C392110B61EAB937C0AD20773990BDF3` |
| `common\country_leader\039_murder_mystery_character_traits.txt` | `B920BB855782B1BF78172DF2EB84DD122AD404195C52718FF6E0397F8AB5700A` |
| `common\script_constants\039_murder_mystery_character_constants.txt` | `988B843A7D4B14D7E81DA8714BBE72334624ED2207CF0B08DF6DAB33FD93F4FC` |
| `validation\character_safety_2026_10_03\check_character_contracts.py` | `4E0BE3D0CD9EAF86AED8FF9CA2A5FFF198854B819F8DD7575F1C82F7FBADC564` |

Refresh hashes and line anchors after parent fixes.
Append later MCP results only when their actual final results and artifact identities are available.

## Follow-up dispositions after the actual owner patch

Date: 2026-10-03.
This follow-up reads the actual current files after the parent's reported successful patch.
The earlier failed atomic patch attempt and its accompanying message are not implementation evidence.
The findings above remain as historical preliminary findings, and these dispositions supersede their source-blocker status for the revisions below.

| Finding | Current disposition | Refreshed source evidence |
| --- | --- | --- |
| P1-01, founder failure allowed country commit | Implemented in source, source blocker closed | Integration effects:1709-1720 now requires the candidate's ruling-character resolution, First Knife registration, successful target registration, founder pointer, and exact recruited-roster membership. Failure reaches rollback at 1765-1766. Successful registration at 1648-1661 remains bound to the fixed founder ID and current owner. |
| P1-02, stale live-central flag at inheritance scheduling | Implemented in source, scheduling blocker closed | Integration effects:1180-1183 refreshes the live-central result for any actor retaining `murder_mystery_final_capture_success`, before the inheritance gate at 1184-1193. Character effects:117 clears the stale flag, then 120-129 recomputes current country existence and owned land. The shock remains protected by its global once-only receipt at 131-132, so this refresh does not duplicate the Cohesion/Reach loss or add Chaos. |
| P1-03, malformed positive-ID rows retained | Implemented in source, source blocker closed | Runtime effects:493-508 places the bad-ID check inside the same OR as every other malformed scalar condition. Positive IDs with invalid generation, role, protection, or used-state now reach the aligned removal at 533-542. Valid used tombstones retain the existing liveness-check exemption at 510-513. |

No new blocking source defect was found in this bounded follow-up.
This conclusion covers the three owner repairs and their immediate scope, receipt, failure, tombstone, and repeated-shock behavior.
It is not approval of an isolated commit, engine acceptance, full cleanup/persistence certification, or completion of Event 039.
The remaining central-country-loss dispatcher and complete inheritance algorithm remain within the parent's explicitly open inheritance work.
The fix closes the stale receipt at the inspected scheduling boundary and does not prove autonomous delivery after every possible country-loss callback.

The parent owns the announced source-contract rerun.
At this follow-up read the checker bytes remain `4E0BE3D0CD9EAF86AED8FF9CA2A5FFF198854B819F8DD7575F1C82F7FBADC564`, and no post-fix test result is inferred from the earlier PASS.
No gameplay, localisation, asset, workbook, staging, commit, or game launch was performed by this auditor.

### Updated revision inventory

| Source | Current SHA-256 |
| --- | --- |
| `common\scripted_effects\039_murder_mystery_runtime_effects.txt` | `DA3AA251824E87329B8B694C4A06D514C95756396B384967E8BD1CAE17FD163C` |
| `common\scripted_effects\039_murder_mystery_integration_effects.txt` | `532969142D44691BA1F695D0D18C6905B227FE478C77C719DAA01E86B850899D` |
| `common\scripted_effects\039_murder_mystery_character_effects.txt` | `564DDF1FB860A856BDA4159332087B0F28E4419121B7662D0806EB4DAE9DB654` |
| `common\scripted_triggers\039_murder_mystery_runtime_triggers.txt` | `A0DC14AB68F4F946C8006972011875EC0E00A187E476EA95BCF5CC4ED634D0DC` |

The two original dirty working-tree baseline hashes were rechecked and remain unchanged.
The earlier probability auditor's latest integration hash is an older revision after these three repairs.
Its blocked results remain evidence of the previous routed attempt, and are not a comparison against the current revised file.
No numeric weights were changed by these three repairs.

### MCP availability update

The follow-up tool inventory now exposes `hoi4.event_inspect`, `hoi4.event_render`, and `hoi4.event_compare`, along with reference and probability routes.
Their live tool declarations were read.
This supersedes the earlier route-absence observation for the current session.
Exposure does not establish service health or successful results, and no new graph, render, comparison, scenario, or engine proof has yet been returned at the time this source disposition is appended.
The bounded MCP evidence pass is pending separately from the source dispositions above.
The parent's pending reference queries are not duplicated.
NoEngineEvidence remains in force pending actual final tool results.

### Follow-up MCP requests pending at handoff cutoff

The source dispositions were authored before waiting for any MCP result.
Read the installed nested request definitions at `C:\Users\klimp\AppData\Roaming\npm\node_modules\hoi4-agent-tools\dist\hoi4_agent_tools\schemas\event.js` to resolve fields typed as `unknown` in the exposed live declarations.
The event selector shape is also evidenced by the prior live request in `scenario_registration_audit_2026_10_03.md:84`.
No helper-expansion mode, job control, native task, rewrite, or game launch was used.

| Collector | Request or preparation | Status at this cutoff |
| --- | --- | --- |
| `functions.exec` cell `43` | `hoi4.event_inspect`, `mode = trace`, selector `{ kind: "event", eventId: "chaosx.nr39.32" }`, downstream, depth 1, nodes 12, edges 16, helpers false | Request pending. No final tool result or artifact. |
| `functions.exec` cell `44` | `hoi4.event_render`, the same selector, `view = state`, downstream, depth 1, nodes 12, helpers false, HTML false | Request pending. No render artifact or visual conclusion. |
| `functions.exec` cell `45` | Prepare `hoi4.event_compare`, the same selector, chain/render bounds 12, render false, current-to-before overlays for the two named `.before` files with the current runtime/integration hashes as expected-source guards | Baseline reads and request preparation remain pending at this cutoff, so successful comparison submission or completion is not inferred. |

Focused trace/render requests do not establish helper or lifecycle coverage even if they return successfully.
The proposed comparison is limited to the two preserved baseline files and cannot establish an exact before revision for the new untracked helper, trigger, trait, or constant files.
The original byte hashes remain the immutable baseline identities.
Any eventual overlay result must disclose its decoded-text transport and returned source coverage, and must not be described as a byte-identical baseline upload without verifying that identity.
These collector cell IDs are execution continuations, not MCP artifact URIs, native task IDs, or proof of completion.
The parent may collect their final results and append a further evidence disposition.
NoEngineEvidence remains in force.

## Updated post-transfer founder boundary audit

Date: 2026-10-03.
This addendum reviews the parent's later move of founder resolution and registration into `murder_mystery_register_candidate_founder`.
It supersedes the earlier candidate-creator line anchors and any inference that successful founder registration was possible before the candidate owned land.
The parent explicitly supplies the boundary rule that COUNTRY `exists` is false for the landless carrier.
The installed trigger documentation describes `exists` as a COUNTRY existence check at `triggers_documentation.md:2708-2715`.
No native execution was observed here.

### P1-04: Two pre-transfer COUNTRY existence gates still prevent the corrected boundary from being reached

Evidence: `common\scripted_effects\039_murder_mystery_integration_effects.txt:1653-1667` and `common\scripted_effects\039_murder_mystery_runtime_effects.txt:1480-1494`.
The commit wrapper still requires `event_target:murder_mystery_assassin_state_candidate = { exists = yes }` at integration line 1657 before calling the transaction begin effect or transferring the reserved states.
The begin effect independently repeats the same candidate existence gate at runtime line 1487 before publishing the open transaction.
Under the supplied landless-carrier rule, the first gate fails, and simply repairing that gate leaves the second gate blocking the transfer.
Consequently the source's correct transfer-to-register ordering does not make the founder producer reachable for a fresh landless candidate.
This is an existing upstream defect exposed by the corrected boundary, not a claim about other country or force setup surfaces.

Needed parent fix: validate the reserved candidate through the current creation attempt and its provenance before land transfer, then use COUNTRY `exists` for the post-transfer proof.
Repair both pre-transfer gates together.
Do not substitute `scope_exists` on a variable scope as existence evidence.
Add a source-contract case that rejects pre-transfer COUNTRY-existence prerequisites on this fresh-carrier path, alongside the existing ordering checks.
The exact native activation and transfer behavior still requires separate engine evidence.

### Verified current source facts

| Boundary | Current source evidence | Disposition |
| --- | --- | --- |
| Candidate creator no longer snapshots or registers founder | Integration effects:1636-1640 clears ruling, founder, and registration success receipts. The creator contains no ruler-anchor or safe-target registration call. | Implemented in source. |
| Producer runs inside candidate COUNTRY after transfer-applied receipt | Integration effects:1663-1668 calls transfer, checks `murder_mystery_assassin_state_transfer_applied`, enters the candidate target, and invokes the founder helper. | Correct local ordering, reachability blocked by P1-04. |
| Exact ruling-founder proof and registry registration | Character effects:55-93 clears success receipts, checks COUNTRY existence, Assassin identity and the explicit ruling First Knife name, invokes the native anchor, and registers the resolved character using fixed founder ID and current transaction generation. | Source-reviewed for the documented candidate caller. |
| Founder generation receipt | Character effects:83-85 publishes `murder_mystery_first_knife_generation` only after registration success. | Implemented output. A bounded common/events search found its writer but no reader, so no additional generation-validation strength is inferred from this new mirror. Existing selected-row generation checks remain separate. |
| Candidate commit requires founder receipts and recruited roster | Integration effects:1685-1696 requires candidate existence, leader name, ruling resolution, founder registration, successful registration, saved founder pointer, and exact `any_character` membership. | Earlier P1-01 failure-to-commit safeguard remains implemented, conditional on reaching this block. |
| Founder pointer clear | Character effects:59 clears the event-owned global founder target unconditionally before the helper's limit. The sole inspected call is integration:1667 in the candidate block. | Exact source fact, not proof of an owner check for other callers. No other actor or country-creation contract is certified. |
| Earlier malformed-row and live-status repairs | Runtime effects retain SHA-256 `DA3AA...`, and the live-status refresh precedes the inheritance scheduling gate. The shock helper now starts at character effects:159 after the added founder helper. | Earlier P1-02 and P1-03 source dispositions remain closed. |

No source mutation was performed by this auditor.
Only this handoff is appended.
The bounded updated producer/commit boundary remains partial because P1-04 is unresolved.
The earlier statement of no new blocking source defect concerned the prior three-fix revision and does not clear this newly examined activation boundary.
Opening, complete inheritance, other actor packages, force setup, and full Event 039 completion remain outside certification.

### Updated source-contract result and identities

Read and ran the updated checker with `python -B docs\plans\039_murder_mystery_plans\validation\character_safety_2026_10_03\check_character_contracts.py`.
Result: PASS, with its explicit no-engine limitation.
The updated assertions check transfer-applied text before the founder registration call and require founder/ruling receipt text in the commit body.
They do not test whether pre-transfer existence gates prevent that ordering from executing.
Manual source tracing establishes that omitted boundary case.

| Source | SHA-256 at this follow-up |
| --- | --- |
| `common\scripted_effects\039_murder_mystery_character_effects.txt` | `117E074E59FB1B4AD7682EF6391B5B2DBB4C74B066458DFBDF23209AA9F69801` |
| `common\scripted_effects\039_murder_mystery_integration_effects.txt` | `C6CE4909E1CF0120D36D0FFFC774E5EF07B5CEDA097F2D3D641F9658B139DBBB` |
| `common\scripted_effects\039_murder_mystery_runtime_effects.txt` | `DA3AA251824E87329B8B694C4A06D514C95756396B384967E8BD1CAE17FD163C` |
| `common\scripted_effects\039_murder_mystery_character_effects.md` | `BCB4FD59720D6C622A78F86302185AB84F74D8570C3962565DE70778237267A1` |
| `validation\character_safety_2026_10_03\check_character_contracts.py` | `E56A47EE298ACECA6AE0DE041A2030407DEB11699048E2E01ACF5D054013C91E` |

The original dirty working-tree snapshots remain the recorded baseline.
This move changes helper call placement and registration timing, without introducing numeric selection weights.
The previously routed probability handoff remains limited to its captured revisions and unavailable scenario results.

### MCP continuation status

Collector cells 43, 44, and 45 were each polled once with a 1 ms wait and remained running without output.
No duplicate event or parent-reference request was started.
No final inspect, render, compare, source revision, or artifact identity is available from those collectors.
Their earlier request revisions cannot be assumed to cover this later founder-boundary edit.
The prepared comparison's expected integration hash is the previous `532969...` revision, so its final result must be checked for a stale-source rejection or earlier-revision coverage.
NoEngineEvidence remains in force.

## Reservation-provenance repair and P1-04 disposition

Date: 2026-10-03.
This follow-up reads the actual owner repair replacing both pre-transfer COUNTRY-existence gates and moving capital assignment after transfer.
The latest `AGENTS.md` and events/subagents skill hashes match the previously read guidance, which remains in effect.
The review remains read-only and bounded to the candidate/founder activation boundary.

**P1-04 disposition: implemented in source, source blocker closed.**
Both integration effects:1658 and runtime effects:1486 now call `murder_mystery_assassin_candidate_is_reserved` rather than requiring the landless candidate's COUNTRY existence before transfer.
The predicate in `common\scripted_triggers\039_murder_mystery_character_triggers.txt:29-41` is pure.
It checks the exact saved candidate target, positive global allocation generation, `original_tag = AXS`, the candidate flag, a present country allocation mirror equal to the global allocation generation, absence of the active-country flag, and absence of the global Assassin State existence flag.
It contains no COUNTRY existence check or `scope_exists` substitute.
The checks reject missing provenance, mismatched allocation, wrong original tag, active candidates, and an already published Assassin State at source-contract level.
This does not establish native evaluation results for a landless country object.

Allocation is published by integration effects:1581-1588, where the creator advances the transaction sequence, freezes a separate global allocation generation, and mirrors it onto the newly created candidate.
The begin transaction's subsequent sequence increment at runtime effects:1488-1489 does not invalidate reservation provenance, because the reservation predicate compares the country mirror to the frozen allocation generation rather than to the changing transaction sequence.
Founder registration later uses the current transaction sequence, and those two distinct generation roles are preserved.

Integration effects:1664-1669 now orders state transfer, the transfer-applied gate, candidate COUNTRY scope, capital assignment, and founder registration.
There is no `set_capital` in the creator.
The post-transfer COUNTRY existence proof remains at integration effects:1688.
The previous pre-land founder-registration and capital-assignment problems are therefore resolved in the inspected source path.

### Founder receipt and pointer strengthening

Integration effects:1694-1701 requires ruling resolution, founder registration, successful registry registration, country-local `murder_mystery_first_knife_generation` equal to the current global transaction sequence, both character pointers, equality of the resolved character to the global founder, and exact recruited-roster membership in the candidate.
This is a CHARACTER-scope `is_character` comparison inside a candidate COUNTRY block, followed by COUNTRY roster traversal.
No CHARACTER-scope COUNTRY-existence check was introduced there.
The previous note that the new founder-generation mirror had no reader is superseded by this postcondition.
The founder helper at character effects:55-93 publishes the generation only on registration success, and the commit requires the accompanying success receipts.

### Exact defect status at this revision

| Finding | Source disposition |
| --- | --- |
| P1-01, founder failure allowed commit | Closed. Current postconditions require the exact founder receipts, generation, pointer equality, and roster membership. |
| P1-02, stale live-central scheduling receipt | Closed at the previously reviewed scheduling boundary. Complete country-loss dispatch and inheritance remain explicitly outside certification. |
| P1-03, malformed positive-ID reconciliation | Closed. The disjunctive malformed-field predicate remains implemented. |
| P1-04, landless candidate blocked before transfer | Closed. Both early gates use allocation provenance, and capital assignment occurs after transfer. |

No additional blocking source defect was found in this bounded provenance, transfer-order, and founder-postcondition follow-up.
This is not broad country viability, force setup, rollback/retry completeness, other actor ownership, opening succession, full inheritance, save/reload, or Event 039 completion certification.
The helper's event-owned founder-pointer clear remains reviewed only through its documented reserved-candidate caller.
No unrelated actor or generic grounded portrait fallback is approved.

### Updated meaningful validation

Read and ran the updated source-contract checker using `python -B docs\plans\039_murder_mystery_plans\validation\character_safety_2026_10_03\check_character_contracts.py`.
Result: PASS with its explicit no-engine limitation.
Its additional assertions now exclude the former candidate COUNTRY-existence expression from the wrapper's pre-transfer portion and the begin body, require the reservation predicate in both, exclude `set_capital` from the creator, and order capital assignment after the transfer-applied gate.
Manual source review separately checked the reservation predicate's exact target and allocation mirror, and the founder generation and character-pointer postconditions.
The checker still does not execute native country activation, land transfer, roster traversal, or runtime persistence.

| Current source | SHA-256 |
| --- | --- |
| `common\scripted_effects\039_murder_mystery_runtime_effects.txt` | `9BCD439ABC9FAA71CF357D8518CD7FA68D28A9068F70B6685433FC8DAEFA4661` |
| `common\scripted_effects\039_murder_mystery_integration_effects.txt` | `40F3017AB353936456F7EF75A5DC12811FF26D8CFEB1F36B5AD63AE28F759881` |
| `common\scripted_effects\039_murder_mystery_character_effects.txt` | `117E074E59FB1B4AD7682EF6391B5B2DBB4C74B066458DFBDF23209AA9F69801` |
| `common\scripted_triggers\039_murder_mystery_runtime_triggers.txt` | `A0DC14AB68F4F946C8006972011875EC0E00A187E476EA95BCF5CC4ED634D0DC` |
| `common\scripted_triggers\039_murder_mystery_character_triggers.txt` | `E4ADD526F07512119F21851C5A876A2E67725806B815CF516557816F9834A7C6` |
| `validation\character_safety_2026_10_03\check_character_contracts.py` | `83B95C9E49A421632DC9990A9F47673FAF784C353955C1CD3E7FEBF63D42B469` |

### Final first-attempt MCP results and narrower retry

The first-attempt collectors completed with tool-level errors.
Read each final result, rather than inferring success from collector completion.

| Collector | Final result |
| --- | --- |
| 43, narrow Event 039.32 trace | `tool call failed for hoi4_agent_tools/hoi4.event_inspect`, caused by `timed out awaiting tools/call after 600s` |
| 44, narrow Event 039.32 state render | `tool call failed for hoi4_agent_tools/hoi4.event_render`, caused by `timed out awaiting tools/call after 600s` |
| 45, current-to-before comparison | `tool call failed for hoi4_agent_tools/hoi4.event_compare`, caused by `timed out awaiting tools/call after 600s` |

No graph, render, comparison artifact, scenario result, or returned source revision accompanied those errors.
The first comparison's raw console reads had transport-added trailing newlines, so they cannot be claimed as byte-identical baseline overlays even independently of the timeout.
The original snapshot files and their hashes remain intact.

Submitted narrower retries without delaying these source dispositions:

| Collector | Retry | Cutoff status |
| --- | --- | --- |
| 55 | Event inspect trace, same exact event selector `chaosx.nr39.32`, depth 1, nodes 4, edges 4, downstream, helpers false | Pending. |
| 56 | Event render scope view, same selector, depth 1, nodes 4, downstream, helpers false, HTML false | Pending. |
| 57 | Prepare comparison limited to the integration file, same selector, chain/render bounds 4, render false, current-to-before using snapshot `98928E...`, guarded by current integration hash `40F3017...` | Preparation/request pending at cutoff. |

The comparison retry decodes the immutable UTF-8 snapshot through JSON serialization to avoid adding the console's trailing newline to the proposed source.
That request covers only the integration overlay and does not compare the new predicate or helper against an unavailable exact before revision.
All focused helper/lifecycle coverage limits remain applicable.
No parent reference query was duplicated, and no source was written through MCP.
NoEngineEvidence remains in force.
