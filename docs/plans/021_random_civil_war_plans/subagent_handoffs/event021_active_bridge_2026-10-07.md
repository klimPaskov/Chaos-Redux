# Event 021 active bridge handoff, 2026-10-07

Disposition: `implemented` for the bounded helper implementation and its documentation/tests, with the validation limits below.
Parent wrapper integration is `implemented` by the parent and confirmed in the refreshed source under the explicit retry prompt.
The narrow active cleanup and larger Event 006 footprint correction remain parent/planner-owned outstanding work.
Full Event 021 completion remains unresolved and is not claimed here.

## Ownership and reconciliation

The retry found an untracked `common/scripted_effects/021_random_civil_war_active_bridge_effects.txt` containing a complete-looking save/restore pair from the interrupted attempt.
The parent's follow-up explicitly assigned this path and confirmed that the parent had not edited it.
A read-only tracked-file check found no HEAD/index file for that path.
The inherited bytes had SHA-256 `ce913a31574fb744abed2ba617563a973a5175d2d95ae75b3c3eb14c8a5f754b`.
They were preserved and reconciled through an Update File patch, with one additional global commit-lock presence mirror at save-entry cleanup, capture, restoration and final private cleanup.
No ambiguous external ownership was found.
No staging, commit, game, desktop, log search, balance edit or write outside the four permitted paths was performed.

## Changed files and API

| File | Change |
| --- | --- |
| `common/scripted_effects/021_random_civil_war_active_bridge_effects.txt` | Reconciled prior output and completed commit-lock presence preservation |
| `common/scripted_effects/021_random_civil_war_active_bridge_effects.md` | Added helper map, explicit field coverage, migration sequence, cleanup ownership, exclusions and limits |
| `.tools/test_event021_active_bridge.py` | Added source-executing restoration and destructive-cleanup boundary tests |
| `docs/plans/021_random_civil_war_plans/subagent_handoffs/event021_active_bridge_2026-10-07.md` | This implementation and evidence handoff |

The helpers are `event021_parent_save_active_transaction_bridge` and `event021_parent_restore_active_transaction_bridge`.
Both accept COUNTRY scope on the same reviewing government and native `= yes` invocation only.
Save captures original presence/value of 30 global scalars, seven global country/state target pointers and eight global flag presences into normal country variables and country flags.
Restore preserves zero as present, clears originally absent globals, restores pointer identities and flag presence, then consumes all private snapshots.
Restore without the country's `event021_active_transaction_bridge_saved` flag changes nothing.
The frame is synchronous, one per government and deliberately not reentrant.
The matching markdown file contains the full names, scopes, inputs, outputs, side effects and defaults.

Call sites changed: none, by explicit ownership restriction.
The parent has replaced `event021_parent_save_active_commit_bridge` and `event021_parent_restore_active_commit_bridge` with calls to these helpers.
Refreshed source shows save before overwriting the commit-owner target, dynamic activation guard or commit lock, and restore after every row's cleanup and after releasing the transaction's own owner/guard/lock slots.
No unconditional clearing follows restore.

Constants and tuning tables added or updated: none because the helpers make no numeric decision or arithmetic adjustment.
Cleanup added: complete private normal-variable and flag consumption after restore, stale private-copy removal before capture and no-op restoration without a frame.
No country package, CXT grants, visible localisation, icon or GUI surface is added.

## Closure coverage

The reviewed owner source included:

- `021_random_civil_war_active_evolution_effects.txt`: outer commit, per-row commit, old save/restore pair, row markers, active secondary loader and transfer receipt validation.
- `021_random_civil_war_parent_effects.txt`: ordinary secondary starter, native child initializer, rejection, broad force cleanup, preplanned cleanup, Event 006 selection/capture/capital helpers, package preparation, success, abort, package cleanup and host identity preservation.
- Direct downstream Event 021 binding/priority helpers, the Event 006 adapter registry and package-only entry/dispatch, and missile split preflight for destructive-effect review.
- Existing `chaosx_dynamic_effects.txt` and its markdown registry before retaining this event-owned contract.

Snapshot coverage is five serial identity fields, four primary force scratch fields cleared by broad cleanup, ten ordinary secondary/preplanned fields, ten Event 006 pending/planned fields, seven targets and eight flags.
The scalar total is `5 + 4 + 10 + 10 = 29`.
The explicit manifest and source contract test verify the exact field names against the direct mutating closure.
Every global mutation in the bounded direct bodies is covered except the deliberately durable next-front-ID allocation.
The broad static helper traversal over-approximates unreachable legacy branches and package dispatch, so it is reconnaissance only and not proof that every downstream branch executes.

Durable front registry IDs, row/capacity counters, statuses, arrays, priority publication, actor membership and log history are deliberately excluded.
Event 006 fired/weight/cap/evolution/league state and the earlier lifetime-fix commits `545c509bf` and `ce8d2e825` are unchanged by this worker.
No probability-bearing definition is introduced or edited, so a new AI probability audit is outside this bounded change.
The parent's broader probability and completion obligations still apply.

## Parent-owned destructive paths

1. The old preplanned cleanup enters `random_civil_war_preplanned_secondary_anchor_state` and removes `random_civil_war_secondary_transfer_state`.
   Global restoration cannot reconstruct that STATE flag.
   Keep the parent's narrow active cleanup and protect old marker overlap with `event021_parent_clear_active_front_row_markers` too.
2. Event 006 package cleanup enters chain-local `random_civil_war_event6_selected_actor` before the active row loads its new selection and clears that actor's prior-generation copy and setup flags on target presence alone.
   Protect initial cleanup from a stale actor target through an exact current ownership/receipt check or a narrowly separated scratch-only cleanup.
3. `event021_bind_front_plan_row` prefers global `random_civil_war_front_plan_ready` over its active branch, and `event021_reject_pending_front_plan_row` writes the global planned status array.
   Verify active registration and Event 006 rejection against an unrelated pre-existing opening plan, especially colliding IDs.
   Do not undo valid durable rows through this snapshot.
4. Keep legacy second-secondary activation and recursion excluded under `random_civil_war_dynamic_front_activation_active`.
   Its separate globals and STATE cleanup are not part of the active adapter contract.
5. Missile preflight can abort and clean an existing missile operation and mark sites pending before native split.
   ROOT-dependent source/site receipts require owner review when the split source is a different country from the reviewing government.
   Native transfer, annexation, capital rollback and package setup also require their own owner validation.
6. Regular Event 006 selection targets are shared within the chain and cannot be cleared by a global-target clear.
   Preserve validity and owner checks, and rebind before use.
   The seven snapshotted global names currently have no regular target declarations with the same names in the inspected `common/` and `events/` sources.

The requested borrowed-preplanned-flag review found active-first branches in the secondary loader, secondary span copier, opening receipt copier and secondary validator.
The branch-selection test evaluates those current native limits with borrowed `secondary_front_preplanned`, `secondary_route_prepared` and `front_plan_ready` flags present and absent.
Those branches continue to use the active receipt.
Legacy `event021_parent_try_secondary_front` is guarded out of ordinary child recursion during dynamic activation.
This does not resolve the separate global plan binding and rejection risks.

The parent additionally reports a larger Event 006 footprint gap: native release for 29 carrier tags transfers all owned cores, including uncontrolled states, and removes source cores, while active package freezing/appending records only the anchor/count one.
That finding and its full-footprint architecture belong to the planner.
This worker has not independently audited all 29 release definitions and does not change the Event 006 registry or implement an anchor-only fallback.
Full adapter completion therefore remains explicitly blocked on that owner work and validation.

## Meaningful validation

`python -B .tools/test_event021_active_bridge.py` passed eight tests.
The restoration test contains 24 combinations across ordinary success/rejection and Event 006 success/rejection, with absent, zero, present and three mixed-presence patterns.
Tests execute the actual bridge and current parent cleanup source.
Declared adapter overwrites and durable publication are the only manufactured inputs in that round trip.
Separate stores cover country/global scalars, country/global flags, global/regular target pointers, country/global arrays, temporary scalars and temporary arrays.
The suite verifies dormant COUNTRY and STATE pointer identity, same-name country/global separation, no rounding of copied fractional/negative values, private cleanup, repeated/wrong-country/unsaved restore, stale-copy replacement and conservative dropping of helper-created temporaries.
Durable next-ID allocation, array growth and priority publication survive restoration.
A dedicated actual-source test demonstrates that old STATE markers and stale actor generation copies can be deleted despite successful global restoration.
That test defines the bridge boundary and does not certify that the parent has fixed those paths.
The refreshed wrapper test executes both actual parent wrapper bodies and confirms save-before-claim and restore-after-release ordering from the current outer source.
The active-first branch test covers borrowed legacy flags without executing the native civil war or package release.

MCP `hoi4.script_validate` whole-file result: `SCRIPT_CHECK_PARTIAL`, `valid = null`, 455 checked commands, zero reported findings, 67 unchecked argument blocks, two unknown-scope roots.
Requested file-level `kind`/`scope` was rejected with `-32602` because the file route infers these fields, then the corrected path-only request succeeded with that partial result.
Additional explicit COUNTRY snippet checks with typed pointer-scope bindings returned partial results too.
Save checked 182 commands and reported 37 unresolved argument blocks.
Restore checked 249 commands and reported 30 unresolved argument blocks.
Their returned finding limits omitted passed findings and some unresolved entries, so no complete semantic validation claim follows from them.
The installed documentation bundle revision was `9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b`.

MCP `hoi4.event_inspect` for `chaosx.nr21.1`, trace depth 2, nodes 12, edges 16 returned `EVENT_INSPECTED_PARTIAL`, focused analysis, zero helpers, one blocking boundary diagnostic and revision `8f4a82aa5d847df22b40a90e209f8bd0e27f3d6ebe79d13e4fb3dbaf45dc33b0`.
Its report artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f6d84b0bcc444f95c45ce6d97aac6d70123d9ffc8e3bc76784dbe691f4ad99d6/c43adab83a747c6652b4ac5ae83784426d8e11c51fcbabd142bb9c59960a347a/event-trace-8f4a82aa5d84.json`.
The 1,079,918-byte artifact was not read in full and is not used as helper-closure or lifecycle proof.
No event render/compare was run because this worker does not change the event graph or integrate the call sites.
Those parent validation surfaces remain pending after wiring.
No native helper expansion or MCP job/task route was used because server-version/task-negotiation support was not established in this bounded pass.
No live game execution was performed.

## Reference evidence

Connected `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, `hoi4.source_lookup`, `hoi4.event_inspect` and `hoi4.script_validate` routes answered live in workspace `mod_chaos_redux_ea3b2d67c2c0`.
No route timeout occurred.
Context returned omitted topic sources, so the exact variable/target/flag commands were searched and read separately instead of treating context as complete reference coverage.

| Source | Sections read | Source revision |
| --- | --- | --- |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md` | `clear_global_event_target` 2733–2741, `save_global_event_target_as` 6505–6513, `set_global_flag` 7085–7093, `set_variable` 7888–7895 | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md` | `has_event_target` 3844–3852, `has_variable` 5006–5014 | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` | Global event targets 272–302, variable pointer/scoping/lifetime 425–465, native set shorthand 563, zero presence 567 | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md` | Dual `event_target:` and `var:` scopes 269–283 | `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` |
| `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md` | Global target clearing 359, boolean scripted-effect invocation 4683–4698 | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` |
| `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md` | Regular/global target presence 646 | `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06` |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md` | Math/scoped-value and Script Constants 184–251, local direct read | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/scripted_effects/NOR_scripted_effects.txt` | Native country pointer assignment and `var:` re-entry around 934–949, local direct read | `97b420cacc1628f6aca85b6608d8f98accba2b22eaa5a0a5cbccd354d321a57a` |

Source lookup resolved `event021_parent_clear_event6_package_transaction` at `mod:common/scripted_effects/021_random_civil_war_parent_effects.txt:5128–5164` with no shadowing and complete definition lookup coverage.
The initial source inventory revision was `25aa08e3d106be33d916a8be936a34d81c70a5b56f7196385e007f88b9dfbbc6` and the final continuation revision was `4ed1f54f350e35b7a937fb1192ffb5ac3ddf6422613f5bb748cf5bb2081b7c6f` as the shared workspace changed.
An attempted root keyPath returned `SOURCE_PATH_UNKNOWN` because the selected definition's child navigation does not repeat its root key.
The corrected symbol plus `fromLine = 5160` completed the remaining definition through 5164 with `nextLine = null`.

## Artifact identities and remaining work

Helper source SHA-256: `c47ad5f82b629e03616ea25e581d05084b9249410a8e367a736b53959d93a32e`.
Final test source SHA-256 after the eight-test run: `388f9fe99a41026108e8de5ac795933be5fedcaea98c9f7d7046bedbcca94ec5`.
Read owner source hashes at evidence capture were active `8bafbbd065091e2778042fbb048e4a07fe5b55c47f29263cc7da9c79aa7db759` and parent `80caece3e6882ad9f89bdf2ff943f955d470471d169085675df48523e065b661`.
They are read snapshots of concurrently parent-owned files and are not a claim that those bytes remain final.

Completed: scoped reusable bridge, inherited-output reconciliation, explicit helper documentation, exact named field manifest, source tests and this handoff.
Completed parent work observed during refresh: wrapper wiring/ordering and primary force cleanup guard.
Pending parent work: narrow marker cleanup, stale actor cleanup validation, global opening-plan versus active-row binding/rejection review, full Event 006 release footprint, final integration/source and MCP evidence.
Blocked proof: full engine semantics and integrated adapter outcomes remain unverified because MCP does not validate native variable argument semantics and the source harness does not execute native civil wars.
No simplification or unapproved fallback was used in the bounded bridge implementation.
The source checks are complementary evidence and are explicitly not substituted for engine proof.
Skills used: `chaos-redux-events` and `chaos-redux-subagents`.
No skill was created or updated under this exclusive-write scope.
