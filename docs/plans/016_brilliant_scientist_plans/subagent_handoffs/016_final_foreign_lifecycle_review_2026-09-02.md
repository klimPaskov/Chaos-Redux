# Event 016 foreign-operation lifecycle review

Date: 2026-09-02. This is a bounded source audit only. No gameplay, localisation, balance, or non-handoff documentation file was edited, and no commit was created.

## Scope and evidence boundary

Reviewed `common/decisions/016_brilliant_scientist_foreign_decisions.txt`, `common/scripted_effects/016_brilliant_scientist_foreign_effects.txt`, `common/scripted_triggers/016_brilliant_scientist_foreign_triggers.txt`, `common/script_constants/016_brilliant_scientist_foreign_constants.txt`, `events/016_brilliant_scientist_foreign_events.txt`, `docs/events/016_brilliant_scientist/systems/foreign_operations.md`, and `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md`.

F1-F6 from `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_final_lifecycle_owner_review_2026-09-02.md` are treated as accepted and are not repeated here. This review records one residual event-receipt risk, one source/documentation mismatch, and two lower-confidence hardening or contract questions.

The required offline Decision and Event modding references were consulted. The Decision modding page states that `complete_effect` runs on selection and starts the timer, `remove_effect` runs at expiry, and `cancel_trigger` invokes `cancel_effect` without `remove_effect` (Decision modding, lines 266, 323-339). It also states that `fire_only_once = yes` on a targeted decision is once per target (lines 496-521). The Event modding page states that an unset `timeout_days` defaults to 13 days and automatically selects the first option (lines 178-179). Vanilla `common/decisions/SIA.txt` uses `days_remove = constant:...` and `days_re_enable = constant:...` as the timer precedent.

## Severity-ranked findings

### P1: Host responses and actor reports are not bound to the operation receipt that created them

Evidence is in `common/scripted_effects/016_brilliant_scientist_foreign_effects.txt:57-81,184-230,234-315,1285-1498` and `events/016_brilliant_scientist_foreign_events.txt:11-475`.

`brilliant_scientist_foreign_start_operation` creates the live flag, operation type, host id, and start date, then increments the host incoming count. The resolution path saves regular actor and host event targets and opens host response events (`chaosx.nr16.100`, `.110`, `.120`, `.130`, `.140`, `.150`, `.160`, `.170`, `.180`, `.190`, `.193`) or actor reports (`.101`, `.111`, `.121`, `.131`, `.141`, `.151`, `.161`, `.171`, `.181`, `.191`, `.194`). The host response options and `brilliant_scientist_foreign_resolve_public_challenge` do not verify a live receipt, expected operation type, expected host, or an operation token. The actor report options call `brilliant_scientist_foreign_finish_operation` unconditionally, and `brilliant_scientist_foreign_continue_to_actor_report` only checks that an actor event target exists.

The only operation-specific event-option guard is `chaosx.nr16.100_c`, which checks `brilliant_scientist_is_transfer_ready`. It does not identify the invitation receipt. `foreign_finish_operation` mutates the saved host incoming count and resolved-target array using the actor's current live operation before clearing the receipt. `foreign_record_resolution` only protects the current receipt with `brilliant_scientist_foreign_operation_resolution_recorded`, which is cleared by the next operation.

If an operation is cancelled or terminal cleanup clears its receipt while a previously opened host or actor popup remains available, the actor can begin a later operation. Selecting the stale response can then write the old result into the new receipt, append the old host under the new operation type, decrement the old host or another active incoming count, and clear the newer live receipt. This is a source-level stale-event path. Native popup persistence across transfer, annexation, or cancellation is not documented by the available evidence, so the runtime incidence is not proven here, but the event boundary has no fail-closed check.

Minimal owner fix: snapshot an operation identity when dispatching each response chain and require the matching actor, host, operation type, and preferably a unique start token or equivalent receipt value in every host response helper, public-challenge resolver, continuation helper, actor report, and finish path. An invalid response must consume only its stale event context and must not call `foreign_record_resolution` or `foreign_finish_operation` against the current receipt. A live-flag-only check is insufficient because a later operation can be live at the time the stale event is selected.

### P2: History does not retain the start date or selected stage promised by the foreign-operations document

`foreign_operations.md:13,57` says every timed action stores its start date and selected project family, and that the selected family and stage remain recorded for follow-up descriptions and counter provenance. `foreign_start_operation` stores `brilliant_scientist_foreign_operation_started_date` and `brilliant_scientist_foreign_operation_host_id` only as live variables (`foreign_effects.txt:69-71`), and `foreign_finish_operation` clears them (`foreign_effects.txt:293-300`). `foreign_record_resolution` appends parallel host, type, result, detection, and family arrays (`foreign_effects.txt:191-228`), but no date or stage arrays. `brilliant_scientist_foreign_selected_project_stage` is also cleared at finish, and observation does not call `brilliant_scientist_foreign_prepare_project_target` (`foreign_decisions.txt:29-34` versus the project-bearing decisions at 100-356).

Family provenance is present for project-bearing routes through the parallel family arrays, and host attribution is present through the parallel host arrays. The missing date and stage are therefore a provenance and contract mismatch, not a demonstrated reward duplication defect.

Minimal owner fix: either add aligned history date and stage snapshots, including an explicit `none` value for non-project operations such as observation, or narrow `foreign_operations.md` to the currently retained host, type, result, detection, and family fields. Do not claim stage/date persistence until one of those changes exists.

### P2: The shared start effect does not enforce the actor and host cardinality invariants itself

The public decision route is correctly guarded. The route helpers at `common/scripted_triggers/016_brilliant_scientist_foreign_triggers.txt:214-387` all call `brilliant_scientist_foreign_actor_is_operation_ready` and `brilliant_scientist_foreign_target_is_current_host`. The latter checks `incoming_operation_count < constant:brilliant_scientist_foreign_limit.maximum_incoming_operations` at lines 63-74, and the constant is 2 at `common/script_constants/016_brilliant_scientist_foreign_constants.txt:95-118`. The decision entries all use those route helpers in their `available` blocks (`foreign_decisions.txt:10-399`).

`brilliant_scientist_foreign_start_operation` itself (`foreign_effects.txt:57-81`) sets the live receipt and increments the host count without a local guard. No public call site currently bypasses the route triggers, so this is not a demonstrated UI exploit. It remains a direct scripted-caller hazard if a future event, terminal callback, or integration helper calls the effect with an invalid actor or host.

Minimal owner fix: add a fail-closed limit wrapper to the private effect, or document and enforce that every caller must run both the actor-ready and current-host predicates. Do not change the public route gates or the strict two-incoming value.

### P2 conditional contract question: public challenge detection does not call the generic detected-risk helper

`brilliant_scientist_foreign_resolve_public_challenge` sets `last_operation_detected = one` and applies its six response-specific state changes (`foreign_effects.txt:1285-1386`), then records history and opens `.191`. Unlike `brilliant_scientist_foreign_resolve_covert_operation` (`foreign_effects.txt:1483-1498`), it does not call `brilliant_scientist_foreign_apply_detected_risk`. The generic document sentence at `foreign_operations.md:39` says detected operations cost additional Political Power and stability, raise host security alert, and create bilateral opinion penalties. The separate public-challenge section at line 43 instead says public detection is recorded in normal history and describes its own Mandate, Exposure, Dependence, Capacity, Grievance, and diplomatic consequences. The completion contract does not resolve whether the generic surcharge includes this deliberately public route.

Disposition: do not patch from source-only evidence. If line 39 is intended to include public challenge, call the generic helper exactly once. If the public route intentionally owns a distinct consequence set, narrow the document sentence to covert operations. The current source does at least record the detected bit and the public result once.

### P3: Defection and extraction success flags can outlive a failed transfer commit

`foreign_effects.txt:836-880` sets `brilliant_scientist_foreign_defection_success` or `brilliant_scientist_foreign_extraction_success` before `brilliant_scientist_foreign_attempt_selected_transfer`. When the transfer commit is not made, the helper changes the result to partial and sets `brilliant_scientist_foreign_transfer_race_prevented`, but does not clear the earlier route-success flag. The six audited files do not consume those flags elsewhere, and the actor report prioritizes the race-prevented state, so no live exploit is proven. If another surface treats either flag as a committed transfer receipt, clear or rename it on the non-commit branch. This is lower priority than the event identity gap.

## Lifecycle and timer disposition

The category contains eight timed decisions and three immediate response-opening decisions: observation, invitation, recruitment, theft, sabotage, defection, extraction, protection, assassination, counter-program, and public challenge (`foreign_decisions.txt:10-399`). All eight timed decisions use `days_remove = constant:...` and route completion to `remove_effect`; none uses `days_re_enable`, and all are `fire_only_once = yes` targeted decisions. Because vanilla executes `complete_effect` at selection, the live actor receipt and host incoming slot are acquired before the timer runs, not at expiry. This makes the one-live actor rule and two-incoming host rule effective during the timer for public callers.

Invalidation during a timed decision uses `cancel_trigger = { NOT = { brilliant_scientist_foreign_operation_target_remains_valid = yes } }`. The shared trigger requires the live flag, original host still current, Kruger alive, no transaction lock, and no world end (`foreign_triggers.txt:389-399`). The cancellation effect records a cancelled history row and finishes the operation (`foreign_effects.txt:302-315`). The native timer semantics therefore match the intended ownership. Sunk costs are not refunded on cancellation, and no refund effect exists; the foreign-operations document does not promise a refund.

All response events omit `timeout_days`, so the offline Event modding precedent gives them the 13-day default. The first option in each host response leads to a valid helper and the first option in each actor report calls `foreign_finish_operation`, which prevents an indefinitely held response in the documented native path. This does not solve the stale-popup identity gap above.

## Cost and requirement audit

The source-level payment count is within the four-cost maximum. The regular decision cost is Political Power and is paid by the native decision at selection. The counter program additionally removes 250 `support_equipment` in its `complete_effect` (`foreign_decisions.txt:326-367`), immediately when selected, not at timer expiry. The removal is a single debit and is not repeated by the result or response helpers. Detected covert operations apply the separate intended -20 Political Power consequence (`foreign_effects.txt:690-721`), and accepted protection grants equipment rather than charging it.

| Operation | Upfront payment | Timer | State or route requirements |
| --- | --- | --- | --- |
| Observation | 15 Political Power | 30 days | Interest threshold, current host, one live actor operation |
| Formal invitation | 25 Political Power | Immediate | Diplomatic access and invitation gate |
| Assistant recruitment | 30 Political Power | 45 days | Project, access, assistant capacity, prior route gates |
| Archive theft | 45 Political Power | 60 days | Project, intelligence access, hostile route, unstolen family |
| Project sabotage | 55 Political Power | 75 days | Project, intelligence access, hostile motive, undamaged family |
| Encourage defection | 45 Political Power | 60 days | Access, transfer readiness, invitation/recruitment/grievance evidence |
| Extraction | 70 Political Power | 75 days | Intelligence access, transfer readiness |
| Protection offer | 35 Political Power | Immediate | Diplomatic access, no war, no active or prior protection partner |
| Assassination | 100 Political Power | 90 days | Intelligence agency, strong operative threshold, strategic project, hostile route |
| Counter-Kruger program | 60 Political Power plus 250 Support Equipment | 120 days | Intelligence access, active project, prior evidence or strategic project |
| Public challenge | 35 Political Power | Immediate | Public-interest threshold, access, and host evidence |

Requirements are separated from payments in the decision triggers. No duplicate PP, equipment, reward, or support refund path was found in the audited helpers. `fire_only_once` plus per-operation resolved-target arrays prevents an ordinary same-target reroll, including after a cancellation. Source-only cost/icon coverage of the localisation row is not certified because the localisation file and GUI are outside this handoff scope.

## Route, AI, and provenance notes

Actor-ready and current-host predicates are present in every public route helper, with route-specific intelligence, diplomacy, project, hostile-motive, transfer, prior-operation, ideology, security, and capacity requirements in `foreign_triggers.txt:77-387`. The public challenge evidence OR and counter-program prior-evidence OR match the foreign-operations document. The counter selects the host's most advanced eligible family through `foreign_prepare_project_target`; theft and sabotage set the appropriate unstolen or undamaged requirement before selection. No invalid public target bypass was found.

The decisions use MTTH-backed `ai_will_do` entries and event options use constant-backed `ai_chance` entries. Probability and balance are intentionally not certified here because the separate probability auditor owns that evidence. No mission is defined in the six audited source surfaces, so mission owner, category, region, duration, success, failure, and duplicate-risk fields are not applicable.

## Cognitive load, localisation, and cleanup

The source category has eleven decision definitions, but actual visible targeted rows depend on the current-host array and route gates. This bounded review did not inspect the full decision category GUI, so the six-row density rule is not visually certified. There are no active missions in this family. Cost and duration values are centralized in foreign constants, and all decision entries use custom requirement or effect tooltip keys. No raw nested trigger dump was found in the audited decision or event source. Texticon coverage and rendered decision-row layout remain a localisation/GUI audit responsibility.

Normal success, partial, failure, detection, host response, actor report, and cancellation paths are wired. Transfer, death, sovereignty, and terminal cleanup changes from the accepted F1-F6 owner review are not re-audited here. The residual cleanup concern is only that an already-dispatched native event has no receipt identity guard after another helper clears the live receipt.

## Bounded MCP evidence and limitations

The representative invitation chain was inspected with `hoi4_event_inspect` for `chaosx.nr16.100` downstream at max depth 3, max nodes 80, and max edges 120, with helper expansion disabled. The tool returned `status: ok`, code `EVENT_INSPECTED_PARTIAL`, revision `65f53c2f4a099c16d11d6ab9960f409df2c881e6ad4b02f663cc098b6d5137bd`, graph hash `55dcd8960c2bd627731619ebee30060c151e6e8594bde4b0bc9a750493a67657`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b9ad5ff3848d6f3a5b9ba07bc0f62fcfcb6c91120da0d2d5de84f31630c9843b/36663ec016946d6accedd8b21aef39aff0ad5fb7978383a31ffb715aa19aa7c0/event-trace-65f53c2f4a09.json`.

The matching `hoi4_event_render` returned `status: ok`, code `EVENT_RENDERED_PARTIAL`, the same revision and graph hash, layout hash `3838ce44ec8e7259bf263a21dfdd18aae2561fc4f12416e726c5132c95936b8f`, selected seven nodes, omitted 42,476 nodes, and rendered zero branch variants. The render manifest is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/998f3faa9e4cbc5a8bd47b574006347e2a2dbd3cbd624796c2fcdadba2f11f09/f47eec6dbefb419ded4d90677aafb9e5f6c563e1ec4fc60ecbbcbd66518517ad/event-options-65f53c2f4a09-manifest.json`.

Both MCP calls reported the workspace-wide `MCP_INLINE_FILES_TRUNCATED` diagnostic and deferred helper/lifecycle validation. They are representative partial source artifacts, not live gameplay proof, not a complete branch comparison, and not proof that native popup persistence across terminal state changes behaves as assumed. No game was launched, no logs were requested, and no probability or GUI audit was run.

## Final hashes and acceptance limits

| File | SHA-256 |
| --- | --- |
| `common/decisions/016_brilliant_scientist_foreign_decisions.txt` | `7D76A5B4A6E33B26C8DD3162530547598B183F54F4E9C2273E0D5A6D286D3408` |
| `common/scripted_effects/016_brilliant_scientist_foreign_effects.txt` | `6192259E7D657C77B951E40871ECEF2CF691D3FE008BEDA40832A9C1FCFB66A9` |
| `common/scripted_triggers/016_brilliant_scientist_foreign_triggers.txt` | `EFF7C2FBCD5FAD75CC1E983CEB3EE988C4CFBB4ED1734FA039221FD868CD90C9` |
| `common/script_constants/016_brilliant_scientist_foreign_constants.txt` | `94E00EEE79916D7BAF17C4A18C5BB96A330296C711C8A938D9019EE515816557` |
| `events/016_brilliant_scientist_foreign_events.txt` | `AE97BF2AEC5E2E0E49A7EC933C8857B577484CBBF1AF155A4CA18DAD632C686C` |
| `docs/events/016_brilliant_scientist/systems/foreign_operations.md` | `6806E381FCE0DA5B56630C559019B7C2A8828FFFBEC0F5250920A850F6547BA7` |
| `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md` | `64CDD10921199726325D0534B442DC8CA7E569ECB031EACA1EA5229DA9E1EFE5` |

The source is not lifecycle-complete for certification until the stale response/report receipt boundary is either guarded or explicitly proven impossible by the owning runtime contract. The history date/stage mismatch and public-detection consequence question remain documentation or owner decisions, not silently accepted facts.

## Follow-up design check: fixed operation type plus original actor and host targets

### Uniqueness result

The fixed operation type plus the regular original actor and host event targets are sufficient to identify a response conditionally, without an event-local numeric snapshot, provided the shared start effect enforces the permanent type-specific resolved-target check and every cancellation records the target before clearing the live receipt.

The current public routes already provide the needed uniqueness inputs. Every decision in `foreign_decisions.txt:11-399` is targeted, has `fire_only_once = yes`, and uses one fixed operation identity from `foreign_constants.txt:10-37`. Every route helper checks the actor-ready and current-host predicates (`foreign_triggers.txt:214-387`). `foreign_cancel_operation` records a cancelled result before `foreign_finish_operation` appends the original host to the operation-specific resolved-target array (`foreign_effects.txt:302-315,234-300`). The resolved arrays are never cleared in the audited foreign effects, and each route's `available` trigger rejects its own array entry (`foreign_triggers.txt:222-386`).

Under those conditions, a later live operation cannot have the same actor, host, and operation type as an earlier response chain. A later operation against another host fails the host-id check, and a later operation against the same host with another type fails the fixed-type check. A response guard may compare the existing actor `brilliant_scientist_foreign_operation_host_id` to `event_target:brilliant_scientist_foreign_operation_host.id`; this uses the already stored start variable at `foreign_effects.txt:69-71`, not a new event-local snapshot. The repository already uses `check_variable` comparisons against `event_target:...id` in equivalent receipt checks.

This is conditional rather than currently true because `brilliant_scientist_foreign_start_operation` does not yet check the resolved array itself (`foreign_effects.txt:57-81`). A future direct caller, or any terminal cleanup that clears a live receipt without running `foreign_cancel_operation`, can reuse the same actor-host-type triple while an old popup remains open. That is the concrete reuse collision that makes the existing source insufficient. Country-scope identity reuse after annexation and re-release is also not documented by the available engine evidence, so an old target pointer and a later scope with the same numeric id cannot be claimed generation-safe. The accepted F1-F6 cleanup is not re-litigated here.

### Shared start guard design

The common start effect should fail closed before setting `brilliant_scientist_foreign_operation_live`, incrementing `brilliant_scientist_foreign_incoming_operation_count`, or changing any operation state. Its gate should require a known operation type, no existing live receipt, a valid original host and no terminal or transaction lock, host incoming count below the constant maximum, and a type-specific `NOT is_in_array` check against the permanent resolved-target array.

The type-to-array mapping is:

| Operation type | Permanent resolved-target array |
| --- | --- |
| `observation` | `brilliant_scientist_foreign_observation_resolved_targets` |
| `formal_invitation` | `brilliant_scientist_foreign_invitation_resolved_targets` |
| `assistant_recruitment` | `brilliant_scientist_foreign_recruitment_resolved_targets` |
| `archive_theft` | `brilliant_scientist_foreign_theft_resolved_targets` |
| `project_sabotage` | `brilliant_scientist_foreign_sabotage_resolved_targets` |
| `encourage_defection` | `brilliant_scientist_foreign_defection_resolved_targets` |
| `extraction` | `brilliant_scientist_foreign_extraction_resolved_targets` |
| `protection_offer` | `brilliant_scientist_foreign_protection_resolved_targets` |
| `assassination_attempt` | `brilliant_scientist_foreign_assassination_resolved_targets` |
| `public_challenge` | `brilliant_scientist_foreign_public_challenge_resolved_targets` |
| `counter_program` | `brilliant_scientist_foreign_counter_program_resolved_targets` |

A static `if` or `else_if` branch on the existing `brilliant_scientist_foreign_operation_type` can select the corresponding array. An unknown or missing type must not enter the mutation body. This closes direct scripted callers and same-type reuse without changing costs, route weights, rewards, timers, or the one-live/two-incoming cardinality.

### Typed response and report guard map

Use one shared receipt-scope check for the presence of the regular actor and host targets, the actor live flag, and equality between the actor's stored `operation_host_id` and the original host target id. Use static operation-specific wrappers for the fixed type and do not pass a temporary event-local operation number.

| Host response event | Actor report event | Fixed operation type | Guard placement |
| --- | --- | --- | --- |
| `chaosx.nr16.100` | `chaosx.nr16.101` | `formal_invitation` | Guard all three host helpers before effects; retain the existing transfer-ready check on `.100_c`; guard the report before typed finish. |
| `chaosx.nr16.110` | `chaosx.nr16.111` | `protection_offer` | Guard all three host helpers before state or equipment effects; guard the report before typed finish. |
| `chaosx.nr16.120` | `chaosx.nr16.121` | `observation` | Guard both secure and diplomatic host options before effects and typed continuation; guard the report before finish. |
| `chaosx.nr16.130` | `chaosx.nr16.131` | `assistant_recruitment` | Guard both host options before effects and typed continuation; guard the report before finish. |
| `chaosx.nr16.140` | `chaosx.nr16.141` | `archive_theft` | Guard both host options before effects and typed continuation; guard the report before finish. |
| `chaosx.nr16.150` | `chaosx.nr16.151` | `project_sabotage` | Guard both host options before effects and typed continuation; guard the report before finish. |
| `chaosx.nr16.160` | `chaosx.nr16.161` | `encourage_defection` | Guard both host options before effects and typed continuation; guard the report before finish. |
| `chaosx.nr16.170` | `chaosx.nr16.171` | `extraction` | Guard both host options before effects and typed continuation; guard the report before finish. |
| `chaosx.nr16.180` | `chaosx.nr16.181` | `assassination_attempt` | Guard both host options before effects and typed continuation; guard the report before finish. |
| `chaosx.nr16.190` | `chaosx.nr16.191` | `public_challenge` | Guard all six host options before `foreign_resolve_public_challenge`; guard the report before finish. |
| `chaosx.nr16.193` | `chaosx.nr16.194` | `counter_program` | Guard both host options before secure or diplomatic effects and typed continuation; guard the report before finish. |

For host responses, the typed guard should require the pending phase plus the route-specific resolution state: immediate `.100`, `.110`, and `.190` open before resolution is recorded, while detected covert `.120-.180` and `.193` open after it is recorded. For actor reports, it should require that the receipt is resolution-recorded and no longer host-response-pending. This prevents a duplicate host response from applying state twice and prevents a report from finishing a receipt that has not reached a result. The guard must not require that the host is still the current host, because the accepted transfer, death, and sovereignty paths may retain the original host target for final settlement.

The shared `brilliant_scientist_foreign_continue_to_actor_report` should be reached through typed wrappers for observation, recruitment, theft, sabotage, defection, extraction, assassination, and counter-program. The typed wrappers recheck the same receipt after the host helper and before firing `.121`, `.131`, `.141`, `.151`, `.161`, `.171`, `.181`, or `.194`. Each report event's sole option should call a type-specific finish wrapper that rechecks the receipt and then invokes the existing `foreign_finish_operation`. An invalid stale event may close without calling any current-receipt mutator.

The eight timed decision `remove_effect` and `cancel_effect` call sites should use the corresponding fixed-type resolver or cancellation wrapper as well. The existing common resolver and cancellation helpers remain the stateful implementation, while the static wrappers bind observation, recruitment, theft, sabotage, defection, extraction, assassination, and counter-program to the decision that dispatched them. This prevents a delayed callback for one type from acting on a later type even if native decision cleanup ordering is unusual.

### Aligned permanent history recommendation

Extend the existing actor and host parallel ledgers in `foreign_record_resolution` (`foreign_effects.txt:191-228`) with `operation_history_started_dates` and `operation_history_stages`, appending both exactly once under the existing `operation_resolution_recorded` guard before `foreign_finish_operation` clears live values. The host side should copy the actor's start date and selected stage through the existing actor event target. Observation must write the explicit `brilliant_scientist_project_stage.none` value because it does not call `foreign_prepare_project_target`; immediate non-project operations should use the same none sentinel. Project-bearing routes should append the selected stage captured before resolution.

This preserves one index across host, type, result, detection, family, start date, and stage without changing any payment, route weight, reward, timer, or cardinality. The existing host and actor history arrays remain the provenance pointers, and the new fields correct the documentation mismatch identified above.

### Follow-up disposition

Fixed type plus original actor and host targets is an adequate minimal receipt identity only after the shared start gate and all typed response/report boundaries are applied. The current source still has the same-type reuse path through an unguarded direct start or cleanup that skips cancellation history, so the earlier P1 remains open. No gameplay patch was made in this follow-up.

## Correction: covert host-response ordering and pending receipt

The prior follow-up paragraph that required a host response to have `NOT resolution_recorded` is rejected for the detected covert route. `brilliant_scientist_foreign_resolve_covert_operation` calculates and applies the result, applies detected risk, calls `brilliant_scientist_foreign_record_resolution`, and only then calls `brilliant_scientist_foreign_dispatch_covert_events` (`common/scripted_effects/016_brilliant_scientist_foreign_effects.txt:1483-1498`). Therefore `.120`, `.130`, `.140`, `.150`, `.160`, `.170`, `.180`, and `.193` legitimately open with `resolution_recorded = yes`.

Use the actor-owned `host_response_pending` receipt as the phase marker, set immediately before dispatching any host response and consumed exactly once before the host option mutates state. The phase requirements are: `.100`, `.110`, and `.190` require the fixed actor/host/type identity, `host_response_pending = yes`, and `resolution_recorded = no`; detected covert `.120-.180` and `.193` require the same identity, `host_response_pending = yes`, and `resolution_recorded = yes`. After a host option consumes the pending receipt, its continuation to `.121`, `.131`, `.141`, `.151`, `.161`, `.171`, `.181`, `.194`, or `.191` must recheck the fixed identity with `resolution_recorded = yes` and `host_response_pending = no`.

Every actor-report option must use that latter report guard before typed finish. A stale host event therefore fails after pending has been consumed, while a stale report fails after finish clears the receipt or after a newer operation changes the fixed identity. The pending receipt must be cleared by cancellation and terminal cleanup as well as by the one successful host-option consumption. This correction supersedes only the earlier `NOT resolution_recorded` host-response condition; the report-side `resolution_recorded = yes` condition remains valid.

## Bounded terminal check: incoming host-array reservations

The exact source evidence shows no consumer or reconciliation of `incoming_operation_actors` other than the append in `brilliant_scientist_foreign_start_operation` and the removal in `brilliant_scientist_foreign_finish_operation` (`common/scripted_effects/016_brilliant_scientist_foreign_effects.txt:57-81,234-300`). `brilliant_scientist_foreign_clear_foreign_relationships` clears bilateral framework flags and global relationship targets only (`foreign_effects.txt:1192-1219`); it does not clear `incoming_operation_actors`, `incoming_operation_count`, or the actor's live receipt. This is a source-level orphan risk, not evidence that every normal popup remains forever.

For the documented ordinary path, native timing is sufficient: the timed decision reaches `remove_effect` or `cancel_effect`, and a response event with no explicit `timeout_days` receives the documented 13-day default before its first option auto-selects. Thus an intact host/actor chain should eventually reach typed report and finish. The offline documentation does not establish what happens when the event recipient is destroyed, annexed, or loses the saved scope before that timeout, so native timeout alone is not proof for terminal-country cases.

The minimal bounded remediation is a host-scoped reconciliation invoked by the existing terminal/invalidation callback, not a world-wide pulse. Inspect only that host's `incoming_operation_actors` entries and remove an entry when the actor no longer has a live foreign receipt or its saved `operation_host_id` no longer equals the host id; decrement `incoming_operation_count` exactly once per removed entry and clamp at zero. Do not zero the array or count wholesale. Leave every matching live receipt in place until its actor-side resolver, cancellation, or typed report calls `foreign_finish_operation`, especially an `encourage_defection`, `extraction`, or `assassination_attempt` receipt whose real outcome may still need to be recorded. Also preserve a matching receipt with `resolution_recorded = yes` while `host_response_pending = yes`, because the host response may still be the settlement gate.

If the host is irrecoverably gone and no native callback can settle the event, actor-side terminal cleanup must first record a typed cancellation or completed result and clear the actor receipt; only then may host reconciliation remove the now-stale array entry. Do not let `clear_foreign_relationships` blindly clear a matching live entry before the resolver/finish ordering is known. The ordering of terminal cleanup versus timed completion and event dispatch is engine-unknown in this source-only audit, so this is a bounded P2 robustness requirement rather than a claim that ordinary timeout behavior is broken.

No gameplay files were edited in this correction. The previously listed gameplay hashes and MCP limitations remain unchanged; no new MCP, game launch, or log evidence was obtained.

## Postreview: fixed-receipt checkpoint against baseline `1ddbd30d1d983cd6046d594026e980cca4914261`

This bounded postreview covers the current foreign decisions, effects, triggers, events, constants, and completion contract. No gameplay file was edited.

### Disposition and acceptance findings

The earlier P1 receipt-identity finding is resolved in the current checkpoint. There is no new P0 or P1 source defect in the reviewed paths.

- All eleven starts in `common/decisions/016_brilliant_scientist_foreign_decisions.txt` bind a fixed `brilliant_scientist_foreign_operation_type` before calling the shared `brilliant_scientist_foreign_start_operation` (`complete_effect` sites for observation, formal invitation, recruitment, theft, sabotage, defection, extraction, protection, assassination, counter-program, and public challenge). `brilliant_scientist_foreign_start_is_valid` (`common/scripted_triggers/016_brilliant_scientist_foreign_triggers.txt:391-440`) maps each type to its public route gate, including the permanent type-specific resolved-target exclusion; the counter-program support debit occurs only after that gate succeeds in `foreign_start_operation` (`common/scripted_effects/016_brilliant_scientist_foreign_effects.txt:59-124`).

- All eight timed decision `cancel_effect` and `remove_effect` boundaries bind their own expected type before invoking cancellation or resolution. All twenty-two foreign events supply a fixed expected type at every host-response and actor-report option before invoking a helper. The shared callback/event receipt guards (`foreign_callback_matches_active_operation`, `foreign_event_receipt_matches_active_operation`) require the live actor receipt, original actor/host targets, matching host id, and the fixed expected type (`common/scripted_triggers/016_brilliant_scientist_foreign_triggers.txt:443-464`). This covers stale same-type, different-type, and cross-actor/provider callbacks without an event-local numeric snapshot.

- Host response phase checks are aligned with the actual ordering. Immediate invitation, protection, and public-challenge responses require `host_response_pending` and an unrecorded result; detected covert responses (`chaosx.nr16.120`, `.130`, `.140`, `.150`, `.160`, `.170`, `.180`, `.193`) require the same pending receipt and an already recorded result because `foreign_resolve_covert_operation` records before `foreign_dispatch_covert_events` (`foreign_host_response_is_pending`, `foreign_resolve_covert_operation`, `foreign_dispatch_covert_events`). A successful host helper consumes pending before mutating state, so a repeated host response cannot apply a second mutation.

- Actor reports (`chaosx.nr16.101`, `.111`, `.121`, `.131`, `.141`, `.151`, `.161`, `.171`, `.181`, `.191`, `.194`) require the matching recorded receipt and no pending host response (`foreign_actor_report_is_ready`, `common/scripted_effects/016_brilliant_scientist_foreign_effects.txt:1594-1633`). Invalid response context calls `foreign_cancel_operation` only for the matching receipt; cancellation preserves an already recorded result and still finishes the matching operation (`foreign_cancel_operation`, `common/scripted_effects/016_brilliant_scientist_foreign_effects.txt:401-414`). A stale report or timer therefore cannot clear or finish a newer receipt.

- The nested transfer helper `foreign_attempt_selected_transfer` is not an independent public entry point, but every current call site is inside the typed formal or guarded covert resolver chain (`common/scripted_effects/016_brilliant_scientist_foreign_effects.txt:936-1011, 1148-1181, 1253-1281, 1702-1716`). The source review found no unguarded route that can debit or settle a different actor/host/type receipt. Failed transfers clear the success flags and retain the existing partial result path.

- `foreign_finish_operation` uses the saved regular original-host target for incoming-array removal and history resolution, while generic covert settlement permits the former host where the contract requires it. Immediate diplomatic response helpers retain their current-living-host requirement. This preserves original-host settlement without weakening actor/type/host-id receipt identity.

- `foreign_record_resolution` and `foreign_align_history_metadata` append aligned peers, actor/host roles, started dates, and selected stages exactly once under the recorded-result guard (`common/scripted_effects/016_brilliant_scientist_foreign_effects.txt:229-324`). Non-project routes use explicit none values and old rows receive the specified invalid `-1` padding; `brilliant_scientist_foreign_history_role` remains actor `1` and host `2` with no tuning change (`common/script_constants/016_brilliant_scientist_foreign_constants.txt`).

### Remaining lifecycle limitation

The destroyed or annexed host/actor orphan case remains an unresolved P2 requirement and is intentionally not claimed fixed by this checkpoint. `incoming_operation_actors` is appended only by `foreign_start_operation` and removed only by `foreign_finish_operation`; `foreign_clear_foreign_relationships` does not reconcile that array, its count, or the actor's live receipt. Native event timeout is sufficient for an intact chain with the documented default event timeout, but the available source and offline documentation do not prove cleanup when the saved recipient scope is destroyed or annexed. A future bounded terminal reconciliation must preserve a matching live transfer, extraction, or assassination receipt until its typed result can be recorded, then remove only stale host-array entries; this is not a request to broaden the current checkpoint.

### Evidence limits

The parent-supplied full `hoi4_event_inspect` state-flow request for selector `{kind:event,eventId:chaosx.nr16.100}` failed with `INTERNAL_ERROR` and no artifact or diagnostics. The focused `hoi4_event_render` options request returned `EVENT_RENDERED_PARTIAL`, revision `be06dbd18a1cbdfd71a4575935079960cc7d7dfd05af41c7bfbc620aaa538fd9`, graph hash `4dc33d125e067b05cedc9a5c6e77da78d012a55c4a75c2d2781970c9fb04a496`, unchanged layout hash `3838ce44ec8e7259bf263a21dfdd18aae2561fc4f12416e726c5132c95936b8f`, helpers `0`, selected nodes `7`, branch renders `0`, and `validation=false`; it is not complete lifecycle or live gameplay evidence. The requested before/after event comparison was also reported as `EVENT_REVISION_NOT_CACHED`. No game was launched, no logs were requested, and no probability or GUI certification is claimed here; AI/cost/timer/reward formulas were checked as unchanged in source and remain subject to their owning audits.

### Current reviewed-source hashes

| File | SHA-256 |
| --- | --- |
| `common/decisions/016_brilliant_scientist_foreign_decisions.txt` | `EB163AE804104D01D68B2E2DFC4E76896FD6069812039E33E1A072F829052D62` |
| `common/scripted_effects/016_brilliant_scientist_foreign_effects.txt` | `4EEDD265AA1760C3EA4852BA5C499F8A06E78283A526A8B452ABB9F3FE2B5AAF` |
| `common/scripted_triggers/016_brilliant_scientist_foreign_triggers.txt` | `624D229BDB637CC25188766AC26543A431A5DE63282C0CCC7C2F232DBCF09D80` |
| `events/016_brilliant_scientist_foreign_events.txt` | `2B6629FC445F8D495867FBA26B85B44D5EB4715665D14690AF412E874D763264` |
| `common/script_constants/016_brilliant_scientist_foreign_constants.txt` | `9FA0E9CA054C4B9C2911A9E9F9910298C652347EE34F6E742809D197E71B8B72` |
| `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md` | `6941241431EAD953B4FF278BEA3C5CA22AA48B86669D8E14C1A1ABF0BCCA32EA` |

The current receipt-guard checkpoint is source-consistent for normal foreign operation chains, but it is not a whole-foreign lifecycle completion certification while the destroyed-country incoming-array cleanup and the stated MCP/runtime evidence limits remain open.
