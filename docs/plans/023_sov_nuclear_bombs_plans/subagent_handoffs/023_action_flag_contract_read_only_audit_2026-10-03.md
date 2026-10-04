# Event 023 action flag contract read-only audit, 2026-10-03

Status: source audit delivered with unresolved defects and MCP evidence blocked.
Role: `chaosx_scripted_system_architect`, explicitly read-only except for this handoff.
Workspace: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.
Acceptance basis for the bounded representation repair is the parent assignment and its subsequent addition of the shared non-yield guard.
This report does not approve a native bomber adapter, any approximation of delivery, or Event 023 completion.

## Prioritized findings

### Resolved source finding: Five known state-scoped exists checks corrected by parent

The parent's additional instruction authorized a bounded audit of the action-state positions and the two explicitly named local-site positions.
Fresh installed documentation at `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md:2708-2715` says `exists` supports COUNTRY, with no supported targets, and describes checking the current country.
Its raw file revision is `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29`.
It does not document STATE support.
The first added inspection found the following five already identified invalid STATE positions at the original audit revisions.
The parent then applied its announced corrections while this report was being finished, and a fresh source read verified all five corrections.

| Original position | Actual scope | Verified parent correction |
| --- | --- | --- |
| `common/scripted_triggers/023_sov_nuclear_bombs_runtime_triggers.txt:40` | `var:sov_nuclear_bombs_action_state` inside target validation | Removed exists, retaining impassable and exact owner/controller checks at current lines 40-44 |
| `common/scripted_triggers/023_sov_nuclear_bombs_runtime_triggers.txt:283` | `var:sov_nuclear_bombs_action_state` inside native country validation | Removed exists, retaining impassable at current line 282 |
| `common/scripted_effects/chaos_meter_effects.txt:6045` | `var:sov_nuclear_bombs_action_state` inside the non-yield accepted-receipt endpoint | Replaced exists with impassable = no at line 6045, retaining exact ID proof at 6046 |
| `common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:1072` | Actor-owned local custody state | Removed exists, retaining exact state ID and registration at current lines 1072-1073 |
| `common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:1168` | State-scoped breakaway delivery helper | Replaced exists with the registered-state trigger at current line 1167, retaining holder-country exists at 1170 |

No additional direct STATE-scoped `exists` consumer was found in the bounded stage/prepare/begin/demolition/receipt, reserve/execute/confirm/clear, action-validator, and shared non-yield guard surfaces.
The reserve-through-clear body at runtime-effect lines 339-971 contains no `exists` token.
The action-target pointers at original runtime-trigger lines 48 and 287, now lines 47 and 285, are country pointers, and their valid `exists` checks remain.
The OWNER/CONTROLLER checks at event-effect lines 717 and 721 are also country-scoped and must remain.
Likewise the country holder checks at original event-trigger lines 1083 and 1171, now lines 1082 and 1170, remain.
Do not replace the invalid state checks with `scope_exists` on a variable pointer because the installed section at lines 7450-7459 explicitly says variable scopes are always valid scopes.
Installed `triggers_documentation.md:5176-5183` explicitly supports impassable in STATE scope.
The corrected hashes and line mapping are recorded in the final revision addendum below.
No unsupported STATE-scoped exists remains in the authorized action surfaces or the two additional named positions at those revisions.
This is a source correction confirmation, without MCP or observed engine execution evidence.
No source patch was applied by this auditor.
These five corrections are representation-independent parent edits, and the original exclusive-flag mapping remains intact.

### P1: Reservation preflight requires the reservation it is supposed to create

`common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt:344` requires `sov_nuclear_bombs_action_context_is_valid` before reservation.
That context calls the target validator at `common/scripted_triggers/023_sov_nuclear_bombs_runtime_triggers.txt:210`, whose source-state test at lines 50-54 requires `sov_nuclear_bombs_site_reserved` to be at least one.
A newly registered source has reserved zero at `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt:313`.
The assigned and transferred reservation branches only increment the source state's reserved bucket after preflight, at lines 366 and 422 respectively.
Therefore an otherwise valid clean source with assigned one and reserved zero cannot enter the reservation branch.
The same circular prerequisite blocks a transferred source with reserved zero on the remote-demolition path.
This condition is present unchanged in the immutable before trigger and effect snapshots, so it is a retained contract defect rather than a flag-conversion delta.
It prevents a successful end-to-end action claim even though the flag representation itself is consistently converted.

Concrete parent fix: separate target geometry/identity validation from source reservation eligibility and post-reservation evidence.
Before reservation, validate the intended source using the existing assigned, operational, or permitted transferred branch predicates.
After reservation, require the matching reservation source and its applicable actor/state mirrors.
Do not manufacture a reserved device to satisfy the validator, remove all source evidence, grant a device, or alter ledger formulas.
Operational reservations need their own applicable mirror proof because their branch increments actor/global reserved counters at lines 374-378 without incrementing a site counter.
The parent should check clean assigned, clean transferred remote demolition, operational-source disposition, already-active reservation, rejection, and release after its bounded fix.
No fix was applied by this auditor.

### P2: Shared-contract documentation overstates delivery verification

`common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.md:97` describes a "verified deployed bomber route".
The actual dispatch at `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt:703-725` explicitly states that `launch_nuke` detonates and does not select an air wing or start a raid.
Installed `documentation\effects_documentation.md:4745-4760` documents a country-scoped detonation effect and optional device consumption, without a bomber dispatch or cancellation receipt.
The document's initial disclaimer does not make the line 97 verification claim supported.

Concrete parent fix: describe the existing capability checks as preflight inputs and explicitly retain the unverified real bomber-delivery adapter and native custody/cancellation receipts as outstanding acceptance evidence.
The flags do not fix delivery, and this audit neither designs nor approves a fallback.

### P2: Final non-detonating-path summary omits accepted non-yield accidents

`common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.md:261` says instrument-failure return and synchronous demolition are the only explicit non-detonating paths.
The same contract at lines 89-90 and the implemented classifier at `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:812-817` accept a non-yield test accident above the catastrophic Integrity threshold.
`common/scripted_triggers/023_sov_nuclear_bombs_runtime_triggers.txt:327-339` accepts that non-yield consumption path.
The failed test consumes a reserved device through runtime lines 510-515 and 557-565, rather than refunding it.

Concrete parent fix: name failed tests, non-yield test accidents, and demolition in the summary, and state that accepted tests consume the reserved device synchronously.
Keep the established threshold, consequences, costs, and outcome weights unchanged.

### Existing acceptance blocker outside the representation repair

The required native bomber adapter remains unresolved pending actual vanilla custody and cancellation receipts.
`launch_nuke` plus capability checks and an `on_nuke_drop` correlation is not proof of a real bomber route.
This known parent blocker is carried forward without a proposed substitute or another shared consequence.

## Representation verdict and complete changed-identifier inventory

No missed legacy variable consumer was found in `common`, `events`, `interface`, or `localisation` for actor proof, authorization, remote-recovery permission, or the old detonation enum.
A broader script/document search outside immutable plans, skills, and offline wiki references found only the three Event 023 script files, the shared Chaos Meter effect, and the two current contract documents for these identifiers.
The constructor scan found no `sov_nuclear_bombs_action_` identifier built through bracket substitution, targeting, or dollar substitution in the runtime search roots.
This is source-search coverage, not engine-index or runtime evidence.

For the table below, E is `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt`, R is `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt`, T is `common/scripted_triggers/023_sov_nuclear_bombs_runtime_triggers.txt`, and C is `common/scripted_effects/chaos_meter_effects.txt`.
The inventory and lifecycle line references below refer to the original flag-only audit hashes.
The final revision addendum records the later parent-only state-check edits and the resulting trigger-line shifts.

| Identifier | Setters | Consumers | Cleanup |
| --- | --- | --- | --- |
| `sov_nuclear_bombs_action_actor_proven` | E:728 | T:107,262 and R:749 | R:949 |
| `sov_nuclear_bombs_action_authorized` | E:729 | T:108,263 and R:750 | R:950 |
| `sov_nuclear_bombs_action_remote_recovery_authorized` | E:1894, explicitly inside ROOT country scope | T:151 and R:392,406 | R:963 |
| `sov_nuclear_bombs_action_detonating` | E:744,819 set it and clear the opposite flag | T:97,98,174,248,274,360, R:801, and C:6036 | E:734,742,810,817 clear it when classifying non-yield, and R:954 clears it on close |
| `sov_nuclear_bombs_action_non_detonating` | E:734,742,810,817 set it and clear the opposite flag | T:97,98,177,181,186,220,225,315,332,363,367,372, E:855,868, R:668, and C:6035 | E:744,819 clear it when classifying yield, and R:955 clears it on close |
| `sov_nuclear_bombs_action_yield_profile_is_valid` | One trigger definition at T:95-100 | T:112,267,344 and R:754 | No stored state to clean |
| Removed variable `sov_nuclear_bombs_action_detonation` | No current runtime setter | No current runtime consumer | Replaced by cleanup of both yield flags |

The old detonation constants remain declared at `common/script_constants/023_sov_nuclear_bombs_constants.txt:583-584`.
They are not surviving old-enum consumers and no constant removal or tuning change is needed for this audit.

## Helper map, scope, and lifecycle

| Helper | Scope and inputs | Outputs and side effects | Direct relevant callers |
| --- | --- | --- | --- |
| `sov_nuclear_bombs_stage_action_context` | SOV country scope under the known owner-root call paths, pending action type and selected state targets | Persists exact action/source/target pointers, proof and authorization flags, exactly one yield flag, next nonce, and requests existing one-device reservation | E:1062,1085,2324,2481,2544,2642,2695,2887 |
| `sov_nuclear_bombs_prepare_test_outcome` | Country scope with test type and action nonce | Selects the existing outcome and rewrites both yield flags as an exclusive pair | E:1099 |
| `sov_nuclear_bombs_action_yield_profile_is_valid` | Country scope, two yield flags, absent flags mean false | Read-only Boolean result, no variables, defaults, grants, target changes, or other effects | T:112,267,344 and R:754, outbound inherits through T:246 |
| `sov_nuclear_bombs_begin_action` | Country actor, pending type, command unlocked | Stages and executes, records synchronous accepted receipt, clears only when delivery is not pending | E:1895 |
| `sov_nuclear_bombs_demolish_selected_site` | Acting SOV country, selected global state target | Sets permission on ROOT after entering state scope, returns to ROOT for begin action, then clears selected state | Decision caller at `common/decisions/023_sov_nuclear_bombs_decisions.txt:954` |
| `sov_nuclear_bombs_reserve_device_for_action` | Country scope with complete context | Existing source-specific one-device movement, holder pointer, active reservation flag and transaction sequence | E:748 |
| `sov_nuclear_bombs_execute_shared_action` | Country scope with staged context and reservation | Existing synchronous commit or pending detonation dispatch, accepted/rejected status, shared non-yield endpoint only for accepted accident | E:1063,1100,2697,2726,2911 |
| `sov_nuclear_bombs_confirm_native_delivery` | Launcher country after exact callback state/nonce checks | Native stockpile observation, existing one-device commit or dispute, pending close and confirmed flag | `common/on_actions/023_sov_nuclear_bombs_on_actions.txt:109` |
| `sov_nuclear_bombs_record_action_receipt` | Country with accepted unrecorded nonce and valid exclusive profile | Records outcome and progression receipts before context cleanup | E:1006,1066,1103,2700,2729,2914 |
| `sov_nuclear_bombs_clear_action_context` | Actual calling country, optional live reservation | Releases eligible unlaunched reservation and clears all five migrated flags and context variables only without native pending | E:1037,1067,1108,1116,1659,1695,2474,2487,2500,2554,2701,2730,2748,2895,2916,2956 and R:907,3116 |

`sov_nuclear_bombs_classify_test_action_yield` has no definition or call site in the audited source.
The assigned classification behavior is currently inline in `sov_nuclear_bombs_prepare_test_outcome` at E:808-819, with initial staging classification at E:732-744.
This is an identifier-location clarification, not a recommendation to add an unused helper.

The caller crosswalk shows SOV decision and mission-owner country entry points for the action paths.
The wartime demonstration wrapper at E:2661 calls public-test preparation, which stages the demonstration at E:2642.
No focus or scripted-GUI call site for the migrated identifiers was found, and no focus/GUI/map design was performed.
Decision/mission call sites were traced for owner scope and lifecycle only, without auditing their unrelated costs, weights, presentation, or depot-stage mechanics.

### ROOT and PREV

The one changed setter reached from state scope is E:1894.
It explicitly enters `ROOT = { ... }` for `set_country_flag`, correctly preserving the same SOV owner that the previous `ROOT.<variable>` assignment targeted.
Inside that state block PREV would be the calling country, but the explicit ROOT is valid on the observed SOV decision call chain and should not be blindly replaced.
The flag reads at R:392,406 and T:151 execute in the acting country before the nested source/holder scopes.
They do not read permission from the physical holder.
Other changed flag setters, reads, and clears execute in country scope.
The native callback has launcher ROOT and struck-state FROM, and enters ROOT again before confirmation/finalization at on-actions lines 98-110.
Annex cleanup operates on its actual country argument and uses unscoped flag cleanup, rather than trying to clear the callback winner's flags.
The unchanged ROOT-qualified pointer and ledger accesses are not certified as safe for arbitrary foreign-root calls to these helpers.

### Pending survival, permission sequence, and cleanup

Staging does nothing while native delivery or a reservation is active at E:666-670.
Dispatch retains the action proof, authorization, and exclusive yield flags while marking native delivery pending at R:713.
`begin_action` and test resolution skip context cleanup while pending at E:1065 and E:1102.
The cleanup helper itself guards every flag clear and pointer removal with no native pending at R:947.
Therefore even cancellation callers of that helper retain the action flags while a native receipt remains unresolved.
Confirmation commits under the pending country validator, clears pending at R:933, records the outcome at E:1006, and only then clears context at E:1037.
Timeout/dispute instead moves the existing reservation to missing custody, clears pending and reservation at R:904-906, and clears context at R:907.
Annex disposition calls that dispute path before cleanup at R:3114-3116.

Remote permission is set before staging/reservation at E:1894-1895.
Its transferred-source consumers bind the physical holder at R:407-414.
Commit/release thereafter use the stored reservation-holder pointer, not a newly inferred holder.
On the synchronous demolition path, recording precedes cleanup at E:1066-1067, which clears permission at R:963.
Rejected unlaunched actions release before cleanup.
An already-pending native request remains unresolved and is not treated as refundable by this representation repair.
No additional permission setter or independent flag-clear path was found.

### Event targets and constants

No event target was added or reclassified by this repair.
Existing global selected-state targets are copied into actor-owned action pointers during staging.
The action pointer survives pending delivery independently of later selection cleanup.
`sov_nuclear_bombs_clear_action_context` clears actor-owned context pointers, and existing selected-state helpers clear their named global targets separately at E:1043-1052.
No numeric tuning table, threshold, duration, weight, grant, cost, or ledger formula was changed in the three snapshot comparisons.
The Integrity threshold remains `constant:sov_nuclear_bombs_tuning.test_accident_catastrophic_integrity_threshold`, currently 10 at constants line 313.
No new engine flag was introduced merely for a tooling fixture.

## Source equivalence and malformed-profile rejection

All three immutable snapshots were compared with current files locally.
The differences are 47 old representation-bearing source lines, split as 11 event-effect lines, 11 runtime-effect lines, and 25 trigger lines, plus the new exclusive-profile helper and its integration.
An in-memory comparison removed the explicitly owned identifier-bearing lines from each side and the entire newly added profile-helper block from current triggers, normalized line endings for that comparison only, and found the remaining content equal in all three pairs.
The reviewed local diffs supply the meaning of the removed lines.
These checks establish bounded source preservation only and are not MCP or engine proof.
The snapshots were retained without edits.

For valid old inputs, proven/authorized/remote numeric one maps to its corresponding set flag, and false/absent permission maps to no flag.
Old detonation-required maps to detonating-only, and old non-detonating maps to non-detonating-only.
Every classification setter also clears the opposite profile.

| Detonating | Non-detonating | Exclusive-profile result |
| --- | --- | --- |
| Absent | Absent | Reject |
| Absent | Set | Accept profile only |
| Set | Absent | Accept profile only |
| Set | Set | Reject |

The complete action context, native outbound request through context, native callback validator, and accepted receipt validator require this exclusive profile.
Standalone geometry, route, and stockpile leaf predicates are not claimed to independently validate the entire contract.
Unlaunched malformed input reaches the runtime missing-context rejection at R:754-758 and existing release path at R:828.
Malformed pending input fails the native country validator, retains unresolved custody until the existing dispute/timeout disposition, and cannot be recorded as an accepted receipt.
The new receipt requirement also removes reliance on a missing old enum reading as zero for a non-yield receipt.

| Path | Preserved source behavior, conditional on a valid reservation |
| --- | --- |
| Failed test | Non-detonating-only, synchronous one-device expenditure, no native launch and no non-yield-accident endpoint |
| Test accident above threshold | Non-detonating-only, synchronous expenditure, one accepted shared non-yield consequence, no native detonation |
| Test accident at or below threshold | Detonating-only, existing pending detonation/callback contract |
| Successful or partial-yield test | Detonating-only, existing pending detonation/callback contract |
| Demonstration, combat strike, standalone accident | Detonating-only, existing pending detonation/callback contract |
| Demolition | Non-detonating-only, synchronous dismantled disposition and existing source-specific native-device spend rules |

This table is a source-flow classification and does not overcome the P1 reservation preflight defect or certify native outcomes.
No outcome probability analysis was duplicated, and the separately assigned probability auditors retain assembly/local-custody evidence ownership.

## Shared non-yield endpoint guard

Only the explicitly added representation guard in `common/scripted_effects/chaos_meter_effects.txt:6035-6036` was audited as a change:

```text
has_country_flag = sov_nuclear_bombs_action_non_detonating
NOT = { has_country_flag = sov_nuclear_bombs_action_detonating }
```

It rejects missing, contradictory, and detonating-only profiles while accepting non-detonating-only input subject to all the existing accepted-action, nonce, state, transaction-sequence, and no-pending/no-reservation guards at lines 6025-6050.
The nonce stamp still precedes consequences at line 6052, so a repeated same-nonce call fails the existing strict-newer-nonce check at lines 6047-6050.
The runtime call occurs only after the accepted synchronous non-yield accident commit at R:657-670.
`docs/systems/chaos_meter/nuclear_chaos_ladder.md:54` names the same required country flags and their absence condition.
No other mixed Chaos Meter work was audited or modified.
No immutable before snapshot of this shared endpoint was supplied, and its entire endpoint is added relative to repository HEAD, so that HEAD diff cannot establish byte equivalence to the immediate pre-repair endpoint.
The parent reports its consequence body and nonce idempotence are unchanged.
This audit verifies the current guard and current nonce sequence, but independent before/after byte proof for the shared consequence body remains unavailable.

## MCP exposure and exact evidence limits

Unlike the reported parent exposure, this session's `ALL_TOOLS` contained `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, `hoi4.source_lookup`, `hoi4.event_inspect`, `hoi4.event_render`, and `hoi4.event_compare` with executable schemas.
All live requests used workspace `mod_chaos_redux_ea3b2d67c2c0`.
Initial parallel bounded reference context/search/source lookup and event-state inspection produced no completed result before the still-running orchestration was terminated.
Each reference request was retried once with a narrower request and a 20-second bound.
Context with `surface = event`, limit 2 and question `Country flags`, search `clr_country_flag` with limit 1, and source lookup of the profile helper with no references, one definition and ten lines all returned no result within that retry bound.
No server-reported timeout, source revision, artifact, or coverage result was returned.
No claim is made about the eventual server-side disposition of abandoned read-only calls.

The exposed event schema describes `stateSubject` and `selector` as unknown.
The live validator rejected a string state subject and required maxDepth at least one.
It then revealed the selector discriminator and exact event key through validation errors.
A schema-corrected request used `mode = state_flow`, `selector = { kind = event, eventId = chaosx.nr23.101 }`, maxDepth 1, maxNodes 2, maxEdges 2, and no helper expansion.
That request likewise returned no result within 20 seconds.
No event inspect graph or lifecycle artifact was obtained.
Read-only event render/compare are consequently unperformed and unresolved, rather than replaced with local diffs.
Revision-bound reference_read could not be formed from a returned context/search citation because no such id/revision was returned.
The exact local reference sections below were read under the documented route-gap rule.
No helper-expansion, job, native-task, router, wrapper skill, game launch, or log search was used.

Completed meaningful checks are the full changed-identifier consumer/setter/cleanup inventory, source-root constructor search, exact scoped call-chain review, four-case profile truth table, threshold-path review, reservation-order review, shared nonce/guard review, local immutable snapshot comparison, stable final hashes of the six current audited files, and the added direct STATE-versus-COUNTRY exists review.
MCP/model evaluation, engine script validation, observed asynchronous flag persistence, native stockpile receipt behavior, real bomber custody/cancel receipts, and save/reload execution remain unverified.
The circular preflight finding is a direct source-order deduction, not an observed game failure.
No gameplay simplification or fallback was implemented.
The only file written by this auditor is this handoff.
No gameplay, localisation, asset, workbook, snapshot, skill, index, or commit was written.
Skills used: `chaos-redux-subagents`, `chaos-redux-events`, and `chaos-redux-decisions-missions` for the bounded caller-scope crosswalk.
No skill was created or updated.

## Audited source identities

Hashes are SHA-256 of raw filesystem bytes, not Git normalized blobs.
The original six audited current file hashes were unchanged across the initial repeated read.
Three files subsequently changed through the parent's authorized state-check correction, and their final identities are recorded below separately.

| File | SHA-256 |
| --- | --- |
| `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt` | `57DF338E7C974D2BD4F0466437B60D80462A4D41A86E57856A4AFE17614CB2EB` |
| `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt` | `2BD130BC9C4F079A5D73456A077CDF12EBA04ADE12E3FAE19C923388A1F012B0` |
| `common/scripted_triggers/023_sov_nuclear_bombs_runtime_triggers.txt` | `2F19E4A3B1C7255ADFF32EA1EECAC5109741C6C43A41006BB428FFAC7BAF10CC` |
| `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.md` | `76C813F9031CD467B3DA37EC671E6358C256E1CE113A4346BEAF94E45F5C3FB4` |
| `common/scripted_effects/chaos_meter_effects.txt` | `0A785927F9D5C9944987182DAC2FB4B5694721366B0E2177193B1CC683FD44EC` |
| `docs/systems/chaos_meter/nuclear_chaos_ladder.md` | `8BD5B40922F0A57E145893FC0E14C89A48F2853301648BE7369AC0725A1957F0` |
| `common/on_actions/023_sov_nuclear_bombs_on_actions.txt` | `B8B9E20220CE345540C2160B8948D9D21376618DE9AAD0C54D9ED6B4B61DC39E` |
| `common/script_constants/023_sov_nuclear_bombs_constants.txt` | `5BCF3F563B9ABEEC59C8A93A73FA1F89A7AF3FB1EF9B9D4B9D7FDE90B40E54FC` |
| `common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt`, bounded additional positions only | `B09ED078E9FBA26628488CA1BC51656CC5FCE7F301492263E545D74948B168DD` |

The following paths are relative to `docs/plans/023_sov_nuclear_bombs_plans/probability_source_snapshots/action_flags_2026-10-03/`.

| Immutable file | SHA-256 |
| --- | --- |
| `before_event_effects.txt` | `7899FFCDD5550FDD7D870FA7CF9A107E1B2E5D7C3F56889A72EFBC43369DA2E7` |
| `before_runtime_effects.txt` | `641690B1B093E55995CDA3F4CBBC3D43660A637F63E243E459106DDED817A36B` |
| `before_runtime_triggers.txt` | `8162F160C37D6D4BEE905AC1FF1E0F87670107EE7F1385B83B9523A0D177E666` |

## Local reference sections read and revisions

Installed game paths below are under `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\`.
Offline wiki paths are under the workspace's `paradox_wiki\`.
These are exact local-section reads with byte revisions, not MCP citation artifacts.

| Reference | Relevant complete sections or exact token entries read | File SHA-256 |
| --- | --- | --- |
| `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` | Flags 102-125, event targets 263-328 | `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4` |
| `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md` | Dual scopes 245-328, PREV usage 811-872 | `18EF5249E4991F5427ECA9EC4A2F66DD47F51E26A491C730ADC622F1F5DB1B49` |
| `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md` | Flow control 329-440, country flag/event-target entries 643-646, scripted triggers 2359-2401 | `ABC51AD18A2C46E46D47BAA795C5A840EBAF7C4AE3E777426C64A9F4C0C0CE06` |
| `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md` | Country flag setters/clearers 897-899 | `997DDB09BFD63EFB41A425149C46BD812D5F8953217A403386B2F6C85196AA0C` |
| `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md` | Native nuclear callback scope entry and example 505-524 | `6822ADC85A374A1C1364F2DEF6F32C6D66DA9FB0280319DDD6AF4B84B33D882A` |
| `documentation/effects_documentation.md` | Global target cleanup 2733-2750, country flag clear 2792-2799, launch_nuke 4745-4760, event-target saves 6496-6512, country flag set 6730-6737 | `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF` |
| `documentation/triggers_documentation.md` | Country flag 3624-3638, event target 3844-3851, complete exists entry 2708-2715, variable scope_exists limitation 7450-7459, complete impassable entry 5176-5183 | `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29` |
| `documentation/script_concept_documentation.md` | Script constants 216-248 | `884BFE9F9207EA4B25B36B5129D0F77D11D4B2F7EB0592587767EC58D24930C7` |
| `common/script_constants/documentation.md` | Entire schema and examples file | `E2812EFBDDC7961038E1F1F2B6DD6B059BDC70704EC87D1FE530835D9141BE1C` |
| `common/on_actions/00_on_actions.txt` | Installed native nuclear callback and launcher flag precedent 384-412 | `52A751456F1774AD5001C86D41D4E46494F751D79B6C224B6CD4C0EEBB615EB9` |

## Final revision addendum after the parent's state-check patch

| File | Final SHA-256 |
| --- | --- |
| `common/scripted_triggers/023_sov_nuclear_bombs_runtime_triggers.txt` | `24F399FAE41805C73A1973CBDD4483577E4536A42F252EBFBDA377B6A706CB4B` |
| `common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt`, only two named state-check positions audited | `CEB815D55B2357A5EF477C1749D60B9BFBAC50F86DE3F63649254034CE2CF973` |
| `common/scripted_effects/chaos_meter_effects.txt`, only accepted non-yield guard and named state check audited | `C00446ADD013DBAC77F73BE962328730F4A493C6AF61AD3E50AC1FF1F7D96293` |

All other original source hashes remained unchanged at this addendum read.
For runtime triggers, original lines after 40 through the original second state check shift down one, and lines after original 283 shift down two.
Current helper positions are yield-profile definition 94, context definition 101, native-country definition 255, receipt definition 341, and direct exclusive-profile calls 111,266,342.
The open reservation prerequisite is now at runtime-trigger line 52 and the context's target-validator call is at line 209.
The shared migrated flag guard remains exactly at lines 6035-6036 and its nonce stamp remains at line 6052.
The current three-source comparison was rerun against the immutable snapshots, accounting only for the original representation edits and the two removed state-scoped exists lines in runtime triggers.
The remaining source content again compared equal in all three pairs.
This final comparison is still local source evidence only.
The P1 circular reservation prerequisite and both P2 contract-document findings remain open.

## Parent follow-up

Review and resolve the circular reservation preflight separately from accepting the representation mapping.
Retain the five source-corrected state checks and the preserved valid country checks.
Correct the two contract-document claims without promoting unresolved native delivery to verified status.
Obtain required bounded event inspect/render/compare and engine/model evidence when the connected routes return results.
Retain the separately owned probability audits and actual native bomber custody/cancellation receipt blocker.
Preserve the immutable before-source bytes and compare against the exact current hashes when further source changes land.
This report supplies no full completion claim.

## Reservation-preflight owner repair recheck addendum

Disposition: the original circular-preflight P1 and both original documentation P2 findings are resolved at source level in the owner-applied revision inspected here.
Two malformed-reservation findings remain open below.
This addendum supersedes the earlier current-status statements for those three original findings while retaining the earlier source identities and inventory as historical evidence.
Authorization is the parent's explicit read-only recheck request for the same bounded contract and its exact new immutable before-P1 snapshots.
Only this handoff was appended by the auditor.

### Open P1: Remote post-reservation proof can substitute the actor when the holder pointer is missing

`common/scripted_triggers/023_sov_nuclear_bombs_runtime_triggers.txt:116` accepts a transferred reservation with no `sov_nuclear_bombs_action_reservation_holder` when the initiating actor's reserved count is positive.
This branch does not require remote-recovery permission to be absent.
The unreserved predicate at lines 80-85 correctly separates non-remote actor custody from remote physical-holder custody, but the post-reservation predicate does not preserve that separation.

Concrete malformed case: demolition, remote permission set, transferred source discriminator, registered source site reserved one, global reserved one, transaction sequence present, physical holder reserved one, missing reservation-holder pointer, and initiating SOV actor reserved one from a different reservation or stale record.
The actual new post predicate returns true through line 116.
The outer context can also pass its existing actor/global reserved branch at lines 188-190, so it does not repair the missing-holder rejection.
The commit helper then follows the no-holder actor branch at `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt:582-588`, debiting SOV instead of the physical holder.
The source/global device closes while the holder's reserved entry remains.
This was reproduced for the new predicate body in the source evaluator described below and traced through the actual surrounding source.
It is a source counterexample, not observed native execution.

Concrete proposed parent fix: add `NOT = { has_country_flag = sov_nuclear_bombs_action_remote_recovery_authorized }` to the no-holder actor branch at trigger line 116.
For remote transferred reservations, require the already stored reservation-holder pointer, a living holder country, and its reserved count.
Keep the stored holder as the debit authority rather than rebinding it to a possibly changed present-day site holder.
Mirror the same remote/non-remote distinction in rollback validation and preserve the incomplete context when holder proof is missing.
Do not substitute another actor's positive counter or create a replacement mirror.

### Open P1: Rejected malformed active reservations still reach unvalidated rollback

The new post predicate correctly rejects missing/zero global, actor, or source-state mirrors and a missing source discriminator.
However, rejected execution at `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt:832` calls release whenever the active flag exists.
The release helper at lines 445-449 checks only that active flag and no native pending marker.
It does not require the new source-specific reservation proof before crediting a source and decrementing reserved counters.

Concrete case: assigned reservation discriminator, active flag set, global reserved one, actor reserved zero, registered source site reserved zero.
The new predicate rejects that context, but release still credits assigned and decrements the actor/site reserved counters to minus one at lines 452-459.
With a missing or unknown source discriminator, the generic final `else` at lines 486-490 instead credits the operational pool without proving that operational was the original source.
The helper clears active at line 492, and cleanup removes the source pointer, holder pointer and nonce at lines 952-973, erasing the unresolved reservation context.
Missing source/holder pointers can likewise permit a global reversal without the corresponding state/holder reversal.
The rollback body is unchanged from the immutable before-P1 runtime snapshot, so this is a retained recovery limitation exposed by the requested stale/missing-mirror audit.
A correct clean reservation still releases normally and idempotently.

Concrete proposed parent fix: validate source-specific reservation mirrors before every rollback debit/credit, using the corrected reservation proof or a narrowly scoped rollback proof that permits cancellation after target, ownership, route, or eligibility changes.
Do not use full action-context validity as the rollback gate because legitimate cancellation must work after target or route invalidation.
If reservation proof is incomplete, retain the active flag and its actor/source/holder/nonce context and record the existing reconciliation dispute rather than refunding an uncertain source.
Guard context clearing so it does not discard a still-active reservation after a refused release.
Do not use an unconditional final operational fallback for an unknown source discriminator.
No rollback formula or dispute policy was changed by this auditor.

### Resolved findings and helper map

The target validator at runtime-trigger lines 36-53 now checks target geometry and country identity plus a registered source, without a prior site-reserved requirement.
Context at lines 181-185 selects unreserved eligibility before debit and reservation proof after the active marker is set.
Native country validation at lines 327-330 directly requires post-reservation proof, without incorrectly calling the outbound no-pending context validator.
The original reservation preflight circularity is therefore removed.

| Helper or call site | Scope and inputs | Output and side effects | Current consumer |
| --- | --- | --- | --- |
| `sov_nuclear_bombs_action_target_is_valid`, trigger lines 36-53 | Acting country with action-state, target-country and source-state pointers | Read-only geometry, live target-country and registered-source result | Context at line 281, rejection reason through runtime effect line 798 |
| `sov_nuclear_bombs_action_unreserved_source_is_valid`, trigger lines 57-91 | Acting country, exact source pointer, existing assigned/operational/transferred counts, optional remote permission and physical holder | Read-only pre-debit eligibility, no grants or mirror creation | Context else at line 185 |
| `sov_nuclear_bombs_action_reservation_is_valid`, trigger lines 95-121 | Acting country, active flag, source discriminator, transaction-sequence presence, global and applicable actor/state/holder reserved mirrors | Read-only post-debit proof, with the missing remote-holder exception above | Context at line 183 and native country validator at line 330 |
| Operational source identity selection, event-effect lines 717-727 | SOV owner-root country, absent assigned source pointer, positive actor/global operational pool | Stores one existing registered owned/controlled state's identity, adds no device or site mirror | Staging before reservation at event-effect line 762 |
| Reserve guards, runtime-effect lines 348-405 | Same source types and counters as new pre-debit predicate | Existing source-specific debit/credit formulas and active receipt | `sov_nuclear_bombs_reserve_device_for_action` |

The assigned pre-debit path requires actor/global assigned at least one and the exact registered source owned and controlled by ROOT with site assigned at least one.
The operational path requires actor/global operational at least one and the exact registered source owned and controlled by ROOT.
The transferred demolition path requires site/global transferred at least one.
Without remote permission it requires the actor's transferred count.
With remote permission it requires the actual site's living physical holder and that holder's transferred count, and cannot fall back to the actor's own transferred count.
The reserve branches now mirror these eligibility checks, including the country-scoped holder exists check.

Assigned/transferred post proof requires the reserved site mirror plus the applicable actor/holder and global reserved counts.
Operational post proof requires actor/global reserved counts and does not invent a site-reserved entry.
The source discriminator and transaction sequence must exist.
The post helper checks sequence presence, not equality to the latest global sequence, and this audit does not impose such equality because unrelated legitimate transactions can advance the global sequence.
No unused helper or new engine flag was added for test fixtures.

The new operational fallback is reached only when staging has no action-source pointer after the existing assigned-source selection and both operational aggregates are positive.
It uses installed native `random_owned_controlled_state` with the existing registered-site predicate and writes only `ROOT.sov_nuclear_bombs_action_source_state = THIS`.
No eligible owned/controlled registered depot leaves the source absent and preflight fails without reserving or granting a device.
The source-pool eligibility addition remains separately probability-bearing and is not accepted as probability-complete by this architecture audit.

### Task-specific source scenarios

A read-only in-memory evaluator parsed the two new predicate bodies from the actual runtime-trigger file, resolving source discriminators from the current constants file rather than retyping their enum values.
It implemented their AND/OR/NOT, scoped normal variables, country flags, country exists, ownership/control and check_variable semantics.
The existing registered-state helper was modeled by its exact single state-flag meaning.
There were no file writes, runtime engine flags, probability fixtures, or game execution.
The tested source hash was `27B882DBDA13565455D0F7F30F6A8C79731ABC7F8EF48AFB1F1A9F5E75C76A0D`.

| Case | Actual predicate result |
| --- | --- |
| Clean assigned one, site reserved zero | Pre-debit true |
| Clean remote transferred one, site reserved zero | Pre-debit true |
| Operational actor/global pool one, site reserved zero | Pre-debit true |
| Assigned source missing global assigned count | Pre-debit false |
| Ordinary assigned source lost control | Pre-debit false |
| Remote physical-holder transferred zero, own transferred one | Pre-debit false |
| Remote physical-holder pointer missing, own transferred one | Pre-debit false |
| Clean assigned reservation after debit | Post-debit true |
| Clean remote reservation after debit | Post-debit true |
| Clean operational reservation after debit, site reserved still zero | Post-debit true |
| Assigned reservation missing site reserved mirror | Post-debit false |
| Assigned reservation actor reserved zero | Post-debit false |
| Operational reservation global reserved zero | Post-debit false |
| Remote holder reserved zero with own reserved one | Post-debit false |
| Remote holder pointer missing with own reserved zero | Post-debit false |
| Remote holder pointer missing with own reserved one | Post-debit true, the open P1 counterexample |
| Missing transaction sequence | Post-debit false |
| Missing source discriminator | Post-debit false |

These 18 checks execute the actual two predicate bodies in a bounded source model.
The illustrative reserve transition used to prepare post-debit fixtures is a model of the existing branch movements, not execution of the effect file.
Complete context eligibility, effect mutation, native callbacks and campaign behavior were reviewed separately as source call chains and are not claimed as model coverage.

The active-reservation stage guard at event-effect lines 666-670 prevents restaging or a second nonce while active.
The reserve helper at runtime-effect line 345 prevents a second debit while active.
For clean assigned, remote transferred and operational reservations, release returns the corresponding source once and clears active, so a second clean release has no movement.
Operational reserve/release uses actor/global mirrors and leaves site reserved zero.
These idempotence and release claims are source-order deductions, bounded by the malformed rollback finding above.

Native pending continues to prevent restaging, refund and context clearing at event-effect line 668 and runtime-effect lines 448 and 951.
Native validation uses post proof at trigger line 330.
Confirmation clears pending only after commit at runtime-effect line 937.
Event receipt recording precedes cleanup in finalization, and the five migrated flags remain under the no-pending cleanup guard.
The previous malformed-yield rejection, failed-test, non-yield-accident, true-yield, combat and demolition classification branches remain unchanged.
No remaining STATE-scoped exists was introduced by these new predicates or reserve guards, and their living-holder exists checks are country-scoped.

The parent's documentation updates landed during this recheck and were read fresh.
Runtime documentation lines 97-98 now distinguish capability inputs from actual bomber delivery and retain preparation/cancellation custody receipts as outstanding.
Lines 271-273 now name failed tests, non-yield accidents and demolition and describe synchronous device consumption.
Both original documentation P2 findings are resolved at this document revision.
Lines 100-107 document the new helpers, their input proofs, no-grant behavior and caller examples.
The documented failure default remains subject to the open missing-holder post-proof defect until that defect is corrected.

### Source preservation and new immutable snapshots

New immutable before-P1 source files were found at the exact supplied folder:
`docs/plans/023_sov_nuclear_bombs_plans/probability_source_snapshots/reservation_preflight_2026-10-03/`.
They were read and retained without edits.

| Immutable file | Raw-byte SHA-256 |
| --- | --- |
| `before_event_effects.txt` | `57DF338E7C974D2BD4F0466437B60D80462A4D41A86E57856A4AFE17614CB2EB` |
| `before_runtime_effects.txt` | `2BD130BC9C4F079A5D73456A077CDF12EBA04ADE12E3FAE19C923388A1F012B0` |
| `before_runtime_triggers.txt` | `24F399FAE41805C73A1973CBDD4483577E4536A42F252EBFBDA377B6A706CB4B` |

Local three-file diffs show the new operational identity-selection block, source eligibility/reservation predicates, context/native integration and aligned reserve guards.
The runtime parsed numeric mutation inventory contains 644 matching before/after operations for set/add/subtract/multiply/divide/clamp normal variables and native bomb addition.
All those mutation bodies compare identical, including the existing ledger formulas and amounts.
Parsed release, commit, confirm and clear helper bodies also compare identical to before-P1.
The event-file delta adds only the operational fallback's source-pointer assignment and its eligibility/selection block.
Its existing costs, outcomes, timing and weights remain unchanged in the inspected diff.
No probability equivalence is inferred from those source comparisons.

| Inspected current source | Raw-byte SHA-256 |
| --- | --- |
| `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt` | `EE30908E201FA955DDEF39A1B4278969225FC2B3362C22138B6DA1F552BC12E6` |
| `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt` | `561A0FF35877ABB392B9CA4FC94504DCD8419472E5CA9AD6C023AB3C4967192E` |
| `common/scripted_triggers/023_sov_nuclear_bombs_runtime_triggers.txt` | `27B882DBDA13565455D0F7F30F6A8C79731ABC7F8EF48AFB1F1A9F5E75C76A0D` |
| `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.md` | `91B41C6BC144DC258157AC4224C26FD1A4B4CAA83CD8F2BA4E278F9F3542EAC4` |
| `common/scripted_effects/chaos_meter_effects.txt`, existing guard only | `C00446ADD013DBAC77F73BE962328730F4A493C6AF61AD3E50AC1FF1F7D96293` |
| `common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt`, earlier two named state positions only | `CEB815D55B2357A5EF477C1749D60B9BFBAC50F86DE3F63649254034CE2CF973` |

New helper consumers were searched across common/events/interface/localisation.
There is one definition of each new helper, one unreserved-context call, and two reservation-proof calls at trigger lines 183 and 330.
The old migrated variable consumers remain absent.
The event file's pre-existing positions after the staging insertion shift down by 14 lines, and runtime-effect positions after the changed reserve guards shift down by four.
The shared non-yield endpoint flag guard, state passability, state-ID and nonce stamp remain unchanged at lines 6035-6052.

### Required reference and MCP limits for this recheck

The existing complete skill/reference reads remain applicable, and fresh AGENTS.md was consulted before the recheck.
New native selector rules were read from installed `documentation/effects_documentation.md:5512-5520`, which documents COUNTRY scope and execution on a random owned and controlled state fulfilling the limit.
The file revision remains `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF`.
Offline wiki `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md:538` and its selector example at lines 619-625 confirm the same scope/limit structure under revision `18EF5249E4991F5427ECA9EC4A2F66DD47F51E26A491C730ADC622F1F5DB1B49`.
Installed vanilla precedent `common/scripted_effects/00_scripted_effects.txt:25-38` uses the selector in a country helper with a state limit and ROOT ownership check.
Its SHA-256 is `93DDD0D2E9F7A1A5640CFDAFBAE6B9FF0E1B4EE57E829C81D13B0CAC23AD90BF`.
These references establish syntax and scope, not selection probability or real bomber delivery.

Actual exposure was verified again for reference context/search/read/source lookup, event inspect and probability inspect.
The probability route was attempted first for the operational eligibility-bearing source, using `source = { path = common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt }` and workspace `mod_chaos_redux_ea3b2d67c2c0`.
It returned no result within a bounded 20-second initial call and no result within the bounded 20-second retry.
Event state_flow used the already verified discriminated event selector, and reference context/search/source lookup used bounded explicit workspace requests.
All four routes returned no result within their initial 20-second bounds and narrower 20-second retries.
No artifact, source revision, server error, graph, candidate pool, or probability result was returned.
Revision-bound reference_read remains blocked by the lack of returned id/revision citations.
Event render/compare and the required probability comparison/evidence pass through `chaosx_ai_probability_auditor` remain pending.
This architecture recheck did not choose scenarios or duplicate the separately owned assembly/local-custody audits.
The operational candidate eligibility change needs its own complete baseline/after candidate proof through that auditor.
No jobs, helper expansion, native tasks, central router, wrapper skill, game launch or log search was used.

The real native bomber adapter and actual vanilla custody/cancellation receipts remain unresolved.
Source flags, selector syntax and passing modeled predicates do not establish aircraft assignment or native bomber delivery.
No fallback, simplification, numerical tuning or gameplay patch was applied by this auditor.
The parent must resolve the two malformed-context P1 findings and obtain the outstanding MCP/probability/native evidence before making a broader completion claim.

## Guarded rollback and remote-holder repair final source recheck

Disposition: both malformed-reservation P1 findings from the preceding addendum are resolved in the owner-applied source revision recorded here.
No additional gameplay defect was found in the requested zero/unknown source, missing-holder, zero mirror, valid cancellation, repeated cleanup, and native-pending cases.
This supersedes the preceding addendum's open-P1 disposition while retaining its counterexamples and earlier hashes as before evidence.
The documentation follow-up and external validation limits below remain unresolved.
The parent reported a momentary multi-file apply failure followed by a targeted runtime retry.
Fresh reads verify the new guards in both runtime triggers and runtime effects, so this conclusion does not rely on the earlier apply result or the parent's retry statement alone.
Only this handoff was appended by the auditor.

### Verified remote-holder proof

`common/scripted_triggers/023_sov_nuclear_bombs_runtime_triggers.txt:116` now requires remote permission to be absent before accepting a transferred reservation without a holder pointer.
Line 117 requires remote permission, the stored reservation-holder pointer, a living country at that pointer, and that stored holder's positive reserved count.
The remote missing-holder case with a positive initiating-actor reserved count now rejects.
A non-remote transferred receipt with an unexpected holder pointer also rejects.
The proof never rebinds to the site's current holder.
The source-model case that changed the current site holder while retaining the valid recorded reservation holder correctly released back to the recorded holder.
The native-country proof continues to use this validator at line 331.

### Verified release, retention, and cleanup ordering

`common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt:449` now requires `sov_nuclear_bombs_action_reservation_is_valid` before reversal.
It does not require the complete action context, so missing target or invalid route does not prevent cancellation of a proven reservation.
The successful rollback still uses the same assigned, transferred, or operational formulas and amounts.
Its 19 parsed numeric mutation operations compare identical to the successful branch in the existing immutable before-P1 runtime snapshot.
Commit and confirmation parsed bodies also remain identical to that snapshot.

An active, non-pending receipt that fails proof enters lines 498-504.
It sets the real actor-owned `sov_nuclear_bombs_action_reservation_disputed` flag, writes the existing global reconciliation disputed enum, and writes the existing registered source site's reconciliation disputed enum when that source pointer is available.
It performs no bucket movement, refund, native stockpile grant, nonce clear, source/holder pointer clear, or active-marker clear.
It does not infer another source or manufacture missing mirrors.

Cleanup at lines 958-989 calls release at line 962 and then checks that active has actually closed at line 964 before clearing fields.
Malformed active receipts therefore retain all existing action variables, nonce, pointers, proof/authorization/yield/remote flags and active marker.
The outbound context rejects the disputed flag at runtime-trigger line 170.
A subsequently proven release clears the actor dispute flag at runtime-effect line 494, and closed-context cleanup clears it at line 986.
Release proof deliberately does not depend on that dispute flag being absent, so the actor can close a previously disputed receipt once its exact mirrors are valid.

The old final operational `else` at runtime-effect lines 487-491 remains in source, but the preceding proof recognizes only the three declared source discriminators.
Assigned and transferred are handled by the preceding branches, so only a proven operational discriminator reaches that `else`.
Zero and unknown discriminators cannot enter it and are retained as disputed instead.
This is a validated source-specific reversal, without an unapproved fallback.

Native pending remains an outer barrier to release at line 448 and to cleanup at line 961.
Even a malformed pending source remains untouched by these cancellation helpers.
The new dispute flag is not written by the release rejection branch while pending.
No new cost, mission, loop, selection, consequence, or stockpile grant was introduced by this guard repair.

### Meaningful actual-source model checks

The read-only in-memory evaluator was extended to parse and execute the actual post-reservation predicate, release, clear-context, and ledger/actor initialization bodies.
It resolved constants from the current constant file, retained separate country/state/global normal variables and scope pointers, implemented conditional effect chaining, and enforced country/state flag and country-exists scopes.
Fixtures represented an already initialized active ledger and used existing gameplay identifiers only in memory.
No test file, script file, probability fixture, engine flag, or gameplay state was written.

`sov_nuclear_bombs_refresh_ledger_reconciliation` was intentionally bypassed after successful release.
Therefore the checks establish the scoped reversal, guard, retention and cleanup behavior in this bounded source model, and do not certify the wider aggregate reconciliation algorithm, final global/site reconciliation projection after recovery, engine execution, native receipt ordering, or save/reload behavior.
The complete context was not emulated, but its actual disputed-flag entry condition was evaluated separately and returned false for a disputed receipt.

| Case | Observed bounded-model result |
| --- | --- |
| Clean assigned release | Closed, one assigned reversal, nonce/context cleared |
| Clean operational release with site reserved zero | Closed, actor/global reversal, site reserved remains zero |
| Clean non-remote transferred release | Closed to initiating actor and source |
| Clean remote transferred release | Closed to stored holder and source |
| Current site holder changed, recorded holder still valid | Closed to recorded holder without rebinding |
| Valid reservation with target missing and route invalid | Closed, cancellation remains possible |
| Valid mirrors with actor dispute already set | Closed and actor dispute cleared |
| Source discriminator zero | No movement, active/context retained, disputed |
| Source discriminator unknown | No operational fallback, active/context retained, disputed |
| Remote holder pointer missing with own reserved one | Rejected, no actor substitution, retained disputed |
| Remote stored holder dead with own reserved one | Rejected, retained disputed |
| Remote holder reserved zero with own reserved one | Rejected, retained disputed |
| Non-remote transferred receipt with unexpected holder pointer | Rejected, retained disputed |
| Actor reserved zero, site/global reserved one | No negative debit, retained disputed |
| Site reserved zero, actor/global reserved one | No negative debit, retained disputed |
| Actor/site reserved zero with global reserved one | No debit or refund, retained disputed |
| Global reserved zero | No debit or refund, retained disputed |
| Assigned source pointer missing | No partial global reversal, retained disputed |
| Native pending with valid proof | Entire modeled state unchanged |
| Native pending with unknown discriminator | Entire modeled state unchanged |

Every one of these 20 cases invoked cleanup twice.
The second invocation left the resulting modeled state unchanged, including repeated refused cleanup and repeated pending cleanup.
For malformed non-pending cases, all bucket counters and all original action inputs/permissions remained unchanged apart from the explicit dispute markers and existing reconciliation enums.
For clean release, the expected original bucket regained one device and reserved mirrors lost exactly one.
The model used no guessed holder, substitute source, compensating grant, or approximation of a native bomber route.

### New dispute-state documentation follow-up

The inspected `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.md` still has SHA-256 `91B41C6BC144DC258157AC4224C26FD1A4B4CAA83CD8F2BA4E278F9F3542EAC4`.
It documents the source predicates but does not mention `sov_nuclear_bombs_action_reservation_disputed` or the refused-release retention path.
Its release/cleanup registry rows at lines 43 and 52 and contract/integration prose need the bounded lifecycle update.
The parent should document which source mirrors authorize release, that invalid target/route can still cancel a proven receipt, that missing/mismatched proof retains active and all inputs, that the disputed flag blocks outbound context, and that only verified closure clears that flag and context.
Also distinguish actor dispute-marker clearing from broader global/site reconciliation, which this model did not validate.
This is a remaining documentation obligation, without a new gameplay fix proposed.

The complete new flag inventory in runtime search roots is the setter at runtime-effect line 502, clears at lines 494 and 986, and outbound context consumer at runtime-trigger line 170.
No other consumer/setter was found in common/events/interface/localisation.
The flag is a real unresolved-reservation marker, not a tool-only fixture flag.

### Final source identities and evidence limits

| Inspected source | Raw-byte SHA-256 |
| --- | --- |
| `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt` | `0958B4367A454661B1F60D0814BB2D8316671A661DF42DC88C7558F846831E57` |
| `common/scripted_triggers/023_sov_nuclear_bombs_runtime_triggers.txt` | `89BB122F6A4E4CB5EB8238D234342EEA38B861DFF146416F8E76BFC1C8C9DFFF` |
| `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt` | `EE30908E201FA955DDEF39A1B4278969225FC2B3362C22138B6DA1F552BC12E6` |
| `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.md` | `91B41C6BC144DC258157AC4224C26FD1A4B4CAA83CD8F2BA4E278F9F3542EAC4` |

These source hashes remained stable across the closing recheck.
The earlier immutable before-P1 snapshots were retained without modification.
No exact immediate-before guard-repair snapshot was supplied in this request, so the preceding addendum's source hashes remain its recorded prior identities rather than an invented byte baseline.

Exposed reference context/search/read/source lookup and event inspect routes were verified again.
Reference context/search/source lookup and schema-correct bounded event state_flow each returned no result within a 15-second initial call and a 15-second narrower retry under workspace `mod_chaos_redux_ea3b2d67c2c0`.
No artifact, source revision, coverage report, or server error was returned.
Reference-read remains dependent on unavailable id/revision citations, and event render/compare remain unresolved.
Local source/model comparisons are not presented as equivalent MCP or engine evidence.

Applicable installed country-flag set/clear/check entries and the complete offline flag rule section were reread directly under the route-gap rule.
Installed effects sections are `documentation/effects_documentation.md:2792-2799` and `6730-6737`, revision `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF`.
Installed flag trigger is `documentation/triggers_documentation.md:3624-3638`, revision `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29`.
Offline flags are `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:102-125`, revision `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4`.
The existing skill reads and scope/variable references remain applicable.

The operational-source candidate eligibility probability pass remains pending with the dedicated probability auditor.
The required real native bomber adapter and actual vanilla custody/cancellation receipts remain unresolved.
No separate probability scenarios, new tuning, fallback, simplification, game launch, log search, gameplay write, skill write, workbook write, Git write, or broader Event 023 audit was performed.
The parent receives source-level resolution of the two P1 counterexamples, a concrete remaining documentation update, and explicit validation limits.
No full feature completion claim is made.
