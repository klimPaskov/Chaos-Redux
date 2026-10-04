# Event 027 firing profile transaction review

Date: 2026-10-03.
Role: chaosx_scripted_system_architect.
Mode: bounded research and design, with this handoff as the only authorized write.
Disposition: unresolved implementation recommendation, with required MCP evidence blocked.
Acceptance basis: the parent explicitly states that every file in `docs/specs/027_doctrine_research_specs/` is user accepted, and specifically requests a single participant snapshot, one fixed firing profile, one pacing event and actorless History row, no recurring world on-action, and coherence across overlapping fires and delayed receivers.
This report does not establish Event 027 completion or approve a different gameplay design.

## Immediate recommendation

Use an Event 027 owner-specific direct dispatch in `fire_event_by_temp_id_no_cluster`, following the existing Random War owner-dispatch structure.
Have that dispatch run the complete owner transaction synchronously through scripted effects, then wake country-local receivers only after every participant batch and the History row have been committed.
Keep `chaosx.nr27.1` as the canonical registered identity and console bridge into that same transaction.
The shared dispatcher must not also enqueue `chaosx.nr27.1` or run a second fired-event handler for Event 027.

This is an explicit dispatch-path deviation from the current generic `country_event` dispatch.
It preserves the accepted event identity and behavior, but ordinary dispatcher fires execute the owner helper directly rather than executing the root event definition.
The parent must record this architectural choice explicitly rather than describe it as an unchanged entry path.
There is no gameplay simplification in the proposal.

Yes, make `doctrine_research_append_country_batch` append-only and move `doctrine_research_start_next_batch` into a country-local receiver.
A queued receiver is safe because its inputs are already stored in that country's batch rows.
Queuing alone is insufficient to prove that a receiver executes later.
The producer must finish all batch creation and History binding before it invokes any receiver, regardless of whether the engine subsequently executes that receiver immediately or later.

## Concrete transaction

1. At entry, initialize the existing adapter registry and capture the forced/debug origin before temporary dispatcher context is lost.
   Run `doctrine_research_prepare_firing_profile` exactly once and allocate a unique firing ID distinct from the existing per-country batch IDs.
   Copy stage, size, and firing date into a persistent envelope row immediately.
   These are stored values, not a pointer to `global.doctrine_research_current_stage` or to a country's mutable profile variables.
2. Execute exactly one `every_country` scan, limited by the existing live/valid-action trigger.
   Its body only records participant country IDs and any existing batch-start facts that must represent the snapshot.
   It performs no batch activation, doctrine mutation, AI resolution, country event dispatch, or receiver scheduling.
   Capture the full participant array before starting the append pass.
3. Iterate the captured country array with documented `for_each_scope_loop`, not another `every_country` pass.
   Append one complete country-owned batch per participant, with firing ID, captured stage, captured size, captured date, and the existing batch metadata.
   Remove the current append helper's immediate `start_next_batch` call.
   Do not rerun `country_has_valid_action` to change membership during delivery.
   Resolution later rebuilds doctrine options and can close an exhausted batch through the existing no-compensation path.
   Preserve the live-owner check and report corruption or invalid lifecycle state explicitly rather than silently dropping an accepted participant.
4. After every row is published, mark the envelope `batches_committed`.
   Load `events_log_history_payload_override_active` and `events_log_history_payload_override` from that envelope's captured size immediately before the single shared repeatable fired handler.
   Supply no primary or secondary actor.
   Call the existing shared repeatable bookkeeping once, preserving its normal cluster-member pacing behavior.
5. Add a narrow Event 027 binder inside the shared History recorder after the new row has been written and before downstream callbacks can start another firing.
   Bind the actual `global.events_log_history_sequence` to the exact owner firing ID and mark the envelope ready.
   Do not bind `global.events_log_history_sequence` after `on_repeatable_event_fired` returns, since that handler can invoke `random_stuff_cluster_try_after_minor_event` and another firing can advance the sequence.
   The binder must consume only a one-shot owner context supplied in the same effect chain and reset it after consumption.
6. Only after the binder confirms both batch publication and History publication, replay the captured participant array to issue country-local wake events.
   A wake carries no stage, size, or numeric envelope pointer through temporary variables.
   It checks the country's persisted active/queued batch state and calls `doctrine_research_start_next_batch` only when appropriate.
   Existing active batches remain active and later firings remain ordered queued batches.
   Receiver scheduling and prompting need separate guards so an early wake or duplicate wake cannot open duplicate pages.
7. Clear transaction scratch arrays and working inputs after wake publication.
   Retain the small immutable firing envelope and History association as evidence, or retire them only under a documented policy that preserves every consumer's required identity.
   Country batch rows remain authoritative for delayed resolution.

The same owner transaction is called by `chaosx.nr27.1` for direct console invocation.
That bridge must include the single shared History/bookkeeping step itself if it represents a complete Event 027 firing.
It must not invoke `fire_event_by_temp_id_no_cluster`, which would recurse into the owner dispatch.
Manual and cluster origins must be transferred into the owner transaction before recording achievement origin state.

## Profile immutability and overlap

An envelope is ordinary persistent numeric data indexed by a firing ID, preferably aligned arrays consistent with the current ledgers.
Suggested fields are firing ID, captured stage, captured size, captured date, History sequence, and lifecycle status.
Add a country batch firing-ID column alongside the existing country batch arrays.
Keep batch IDs distinct, because one global firing produces many country batches.

No numeric value is treated as an invented immutable engine scope.
No scripted helper is called with a named argument block.
No temporary variable is expected to survive `country_event`.
No receiver reads `global.doctrine_research_firing_stage`, `global.doctrine_research_firing_size`, `global.doctrine_research_last_firing_size`, or the live evolution stage.

The parent's alternative of pre-fire row publication followed by the canonical root starting already published country chains preserves the snapshot only if the root acts as an idempotent wake and never captures or appends again.
It still needs a verified association between dispatched roots and pending work when roots overlap or arrive late.
A singleton root receipt marker can be consumed by the wrong overlapping root, and a regular event target pointing to mutable country globals does not solve that problem.
Dynamic nonce event-target packets have no verified syntax or runtime precedent in this review.
For that reason the primary recommendation excludes dispatcher root enqueueing entirely and reports the console-bridge deviation explicitly.

The transaction can use temporary profile inputs during its uninterrupted capture and append phases because no asynchronous consumer is invoked there.
Declare required working inputs in the outer effect before helper use, following the documented temporary-variable lifetime caveat.
Persistent envelope and country-row copies are the cross-event contract.
Do not retain one mutable launcher-country `current_firing_id` as the only association if the shared handler can reenter before binding.
Give the recorder its exact firing ID in the same chain and finish binding before any release or follow-up can overwrite working context.

Two firings A and B therefore create distinct immutable envelope rows and distinct country batch rows.
History A gets size A even if B becomes the latest live stage or the latest firing.
A receiver that runs after B resolves its country's existing FIFO queue and never reconstructs A from B's profile.
All country rows for A exist before any AI action for A begins.
This preserves equal grants and prevents AI doctrine sharing or owner-system effects from altering eligibility partway through the recipient scan.

## Proposed helper map

| Helper | Scope and inputs | Outputs and side effects | Direct call sites |
| --- | --- | --- | --- |
| `doctrine_research_dispatch_global_firing` | Valid country caller, same-chain manual/cluster origin | Owns capture, all-country batch publication, exactly one shared fired handler, and History release | Event 027 branch of shared dispatcher and `chaosx.nr27.1` console bridge |
| `doctrine_research_prepare_firing_profile` | Existing owner context | Computes stage and size once, immediately copied to envelope | Owner transaction only |
| `doctrine_research_capture_firing_recipients` | Producer context, declared working array | One filtered world scan, captured country array and snapshot-only metadata | Owner transaction before append pass |
| `doctrine_research_append_country_batch` | Participant country, declared captured firing/profile inputs | Existing queued batch rows plus firing ID, no activation or AI | Captured-recipient replay only |
| `doctrine_research_bind_firing_history` | Recorder context, exact same-chain owner firing ID | Binds committed History sequence, advances lifecycle state, releases wakes only after all batches exist | Narrow Event 027 hook in shared History recorder |
| `doctrine_research_wake_country_batches` | Recipient country, persisted country queue | Idempotent start or no-op, controller-specific flow through existing start helper | New bounded hidden receiver in existing event namespace |

Keep these helpers in the Event 027 owner file and document their contracts in the matching owner reference or `docs/events/027_doctrine_research/overview.md`.
The existing dynamic helper registry describes owner-owned APIs and contains no matching immutable firing transaction helper in the reviewed definitions.
Do not move this event-specific transaction into a central router or replace doctrine behavior with its technology-union helper.

## Constants and tuning

Reuse `doctrine_research_event.base_batch_size` and the four existing evolution batch-size constants without changes.
Reuse the existing stage identities, event ID, invalid index, and first index constants.
If needed, add a small `doctrine_research_firing_status` category with named states such as `captured`, `batches_committed`, `history_committed`, `released`, and `blocked`.
Use lifecycle enum values for multi-state records and flags for Boolean scheduling state.
No AI weights, random pools, evolution pacing, mastery transitions, repeatable cap factor, or cluster participation chance is redesigned here.
Their ongoing baseline audit remains a separate owner/auditor dependency.

## Event targets and cleanup

A regular event target can carry the recipient country's scope through a wake event chain.
It cannot snapshot that country's numeric variables.
The target is optional when the receiver's ROOT is already the intended batch owner.
If used, save a specifically named regular owner target and validate the actual country with the existing live trigger, rather than interpreting `has_event_target` as proof that the country still exists.
Do not use a global event target for the firing envelope and do not attempt manual clearing of regular event targets.

Annexation cleanup must remove the new batch firing-ID column together with every existing aligned batch array and scheduling flag.
An annexed country later released must not resume old choices from a delayed wake.
The receiver must never create a batch, so a late wake with no surviving batch is harmless.
The parent must verify that the existing removal hook runs before reactivation and that civil-war creation does not inherit a usable batch without the original ownership proof.
These are engine lifecycle checks, not established by `exists = yes` alone.

Normal final batch closure keeps its existing receipt/achievement policy and clears only obsolete scheduling state.
Do not clear a pending receiver's scheduling flag merely because synchronous work consumed the current queue, since a later firing can otherwise enqueue a duplicate receiver before the original arrives.
Clear queued-delivery state in the receiver, then decide whether current persisted work needs a prompt or AI continuation.

## Migration plan

1. Add envelope and country firing-ID metadata and update all aligned-array initialization, schema migration, validation, and cleanup consumers.
   Existing batches without a firing ID need an explicit legacy/unknown identity, not invented historical profile or History association.
2. Refactor append into pure queue publication and update its direct consumer.
3. Capture one profile and participant array in the owner transaction and remove the root's second profile calculation.
4. Add the owner-specific dispatcher branch and preserve the root console bridge.
   Exclude Event 027 from generic root enqueueing and generic second bookkeeping.
5. Add the History size producer and narrow sequence binder, then publish country wake events only after binding.
6. Reuse the parent's already wired nine scripted-localisation selectors and four preview rows.
   The five existing History payload branches read captured sizes 1 through 5 and need their missing producer, not a replacement preview design.

## Source-supported findings and references

All relative paths below resolve under `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.
Hashes identify physical bytes observed during this shared-tree review, not an immutable checkout or MCP revision.
Line spans must be refreshed if another agent edits the file.

| Source | Lines | Evidence | SHA-256 |
| --- | --- | --- | --- |
| `events\027_doctrine_research.txt` | 12-20 | Canonical hidden root invokes global batch helper | `D61145D94A54D6EF542999EA120973D2BBA4A1DB877DD10E47DADEAF3A2AB2D1` |
| `common\scripted_effects\027_doctrine_research_effects.txt` | 1948-1958, 1999-2059, 2062-2099 | Current profile globals, origin helper, world fanout, append metadata, immediate activation and AI resolution | `B1C32460A261B06712B2FC3C39A5B7A37759251F70641C1F757A0B4F4BAF8663` |
| `common\scripted_effects\chaosx_settings_effects.txt` | 4339-4343, 4361-4364, 4474-4503 | Event 027 pre-fire hook, Random War owner dispatch, generic event enqueue and type handler | `355FED2A358B6DA41FE534D6439B0319E8A6853A3D6C45F26B8B817D6481B5E7` |
| `common\scripted_effects\chaosx_logic_effects.txt` | 1204-1246 | Shared repeatable accounting, cluster pacing guard, recorder, subsequent cluster follow-up | `C28EE6EAB4A2CEEA866C81CFFD6488E04A0B9D9ED509F650CFDDCC3F49B7548E` |
| `common\scripted_effects\chaosx_events_log_effects.txt` | 677-708, 796-819 | Payload override consumed, sequence written, existing owner bind callbacks and override reset | `5F9F99BE4AA88DFDDB17EB1F7A171DFBF6D49283CA51A2EE54B60940D2A770CE` |
| `common\scripted_localisation\chaosx_scripted_localisation_events_log.txt` | 5726-5778 | Five Event 027 historical size branches and ordinary detail branch | `641A78580E2291C97C0F45FF8EFC0397E26812CAD39A25C9A6B759BF34DCDB8A` |
| `common\scripted_triggers\027_doctrine_research_triggers.txt` | 177-186, 1371-1382 | Live-owner semantics and registered-domain action predicate | `DDD97111AD7C8170CE210071D65365C7061C7D197E87ADC7FC1C3F14D790DF3D` |
| `common\script_constants\027_doctrine_research_constants.txt` | 9-43 | Existing five batch sizes and identifiers | `D24BA6D1C77F76880BE4297F01CD848859466AC806643B29B41561376861D87A` |
| `docs\specs\027_doctrine_research_specs\027_doctrine_research_acceptance_criteria.md` | 17-33, 95-110, 123-136, 197-215 | Single snapshot, fixed profile, persistence, one History row, no actor, cluster pacing | `F72DB5AB8D265128F7815E8FF2EF811244E77FBD09F879BA326FB515C29CC181` |
| `docs\specs\027_doctrine_research_specs\027_doctrine_research_spec_part_1_core.md` | 71-88, 189-248 | Snapshot and country ownership, queue, History contract | `9946DE19C50CC35BA2AC4052ED651EBFE921D31826AB7983250F23358910970E` |
| `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` | 303-327, 429-449, 551-553, 1069-1088 | Regular event-target chain lifetime, temporary variable limits, numeric targeting, persistent arrays | `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4` |
| `paradox_wiki\Event modding - Hearts of Iron 4 Wiki.md` | 25-35, 180-218 | Scope and target transfer, nonexistent-country backlog, immediate block and event-effect forms | `96327B896298420D84058394A44ED08BE7EB518726B8F207B392FEA71F05D43D` |

Installed documentation base: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`.

| Installed source | Lines | Evidence | SHA-256 |
| --- | --- | --- | --- |
| `documentation\effects_documentation.md` | 2278-2290, 2713-2721, 2943-2966, 4279-4328, 6016-6029, 6496-6512, 7888-7907 | Array append/cleanup, country-event fields, array scope replay, event targets, numeric value copying | `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF` |
| `documentation\triggers_documentation.md` | 3844-3851 | `has_event_target` presence check | `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29` |
| `documentation\script_concept_documentation.md` | 216-245 | Shared constants and explicit supported-field restriction | `884BFE9F9207EA4B25B36B5129D0F77D11D4B2F7EB0592587767EC58D24930C7` |
| `common\script_constants\documentation.md` | 1-32 | Constant category schema | `E2812EFBDDC7961038E1F1F2B6DD6B059BDC70704EC87D1FE530835D9141BE1C` |
| `common\scripted_effects\NORDIC_scripted_effects.txt` | 1-15 | Vanilla collects country scopes then replays an array with `for_each_scope_loop` | `DABBC05C1D76C7469E3431582F83A5C2D054678C3B2EC19209B21C4AF9682707` |
| `common\scripted_effects\00_scripted_effects.txt` | 1227-1242 | Vanilla scalar country-event dispatch precedent | `93DDD0D2E9F7A1A5640CFDAFBAE6B9FF0E1B4EE57E829C81D13B0CAC23AD90BF` |

The Nordic example contains differing array names in its clear and append statements.
It supports the collect/replay syntax and is not a correctness template to copy literally.
The offline wiki calls scalar event dispatch instant, while installed country-event documentation lists supported fields without specifying the call-stack precedence required here.
Neither source establishes that omitting delay guarantees the root's entire helper body finishes before the caller records History.
Do not invent `immediate = yes` inside the `country_event` effect or rely on a temporary profile surviving into its immediate block.

## MCP evidence and limits

The subagent's exposed tool inventory contains no HOI4 tools.
Package metadata at `C:\Users\klimp\AppData\Roaming\npm\node_modules\hoi4-agent-tools\package.json` reports version `3.6.0`.
The parent reports a healthy production handshake and 60-second `reference_context`/root `source_lookup` timeouts.
Those parent observations do not establish a working connection in this subagent.

Fresh configured stdio initialization through the existing client timed out after 30 seconds.
A sequential direct production Node client also returned `MCP_TIMEOUT_30S` before an initialize response.
A narrower initialize-only retry returned `MCP_INITIALIZE_TIMEOUT_60S` before an initialize response.
Only client-owned processes were closed by those clients.
No live schemas or health result were obtained, so reference, source lookup, event inspect/render/compare, GUI inspect, and script validation could not be called through a verified connection.
There are no fresh MCP artifact URIs or engine-analysis revisions from this review.
Local source/reference evidence above is explicitly not a substitute for required MCP lifecycle evidence.

No probability pool or score was designed or patched.
No additional probability audit was started while the parent's baseline audit is ongoing.
Native event timing, interruption atomicity, controller transitions, delayed wake survival, annexation/release cleanup, and exact shared-recorder reentrancy remain runtime proof limits.
No game was launched.

The parent additionally reports finite scan limits in the append-only batch and receipt ledgers.
Current `start_next_batch` uses `for_loop_effect` over `doctrine_research_batch_ids^num` at owner effect lines 2066-2074.
AGENTS.md states that `for_loop_effect` and `while_loop_effect` stop after 1,000 iterations.
This review does not redesign those ledgers, and moving start into a receiver does not remove their limit.
Avoid adding another unbounded historical-ledger scan to resolve the firing profile, and do not claim unlimited queue reachability or recovery from this design.
The full captured-recipient replay must also be checked against the installed iterator's actual coverage limits before claiming that every snapshot recipient is published.

## Meaningful owner validation

The parent should verify these transaction cases after implementation, through working read-only MCP routes and task-specific source checks.

- Two overlapping firings with sizes 2 and 4 preserve distinct firing IDs and country batch rows, and History payloads remain 2 and 4 after later stage changes.
- Every captured recipient has its row before the first country wake is invoked, including mixed human and AI participants.
- A delayed or duplicate wake starts no additional batch, consumes no extra choice, and never rereads live profile globals.
- Automatic, manual, cluster-member, and direct console routes each execute exactly one owner transaction and one appropriate shared bookkeeping/History path.
- The History binder records the actual row sequence before cluster follow-up can create another row.
- A country created after the scan receives no row, and a removed/released or civil-war country cannot inherit or resurrect earlier pending choices.
- New firing-ID columns stay aligned across initialization, old-state migration, validation, final closure, and removal cleanup.

## Delivery status

Completed: bounded source-supported architecture recommendation, exact inspected syntax references, observed file hashes, overlap and delayed-receiver reasoning, explicit dispatch deviation, and this handoff.
Changed files: this handoff only.
Gameplay, shared files, index, commit, AI tuning, mastery behavior, and GUI layout were not changed.
Blocked: required fresh MCP inspection/render/comparison and scope validation.
Unresolved: parent adoption of the direct dispatch architecture and the listed engine proof limits.
No fallback or gameplay simplification was implemented.
Skills used: `chaos-redux-events` and `chaos-redux-subagents`, both read completely.
No skills were created or updated.
