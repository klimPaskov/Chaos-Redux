# Event 006 completion audit refresh - 2026-08-20

> Historical snapshot notice (2026-08-22): This dated audit preserves its 2026-08-20 HOLD/PARTIAL evidence and remains historical. Use the 2026-08-22 authority override in `006_source_of_truth_map.md` and `006_independence_wave_resume_packet.md` for current routing and exact replacement counts. Do not treat this audit's at-time source revision, MCP revision, or dated blocker list as current runtime evidence; live release and terminal receipts remain unproven.

## Disposition

**HOLD / PARTIAL.** Event 006 is not complete against `docs/specs/006_independence_wave_specs/`.

The pre-event crisis surface is fully retired at source. The current manual `chaosx.nr6.1` path has no remaining source defect proven to suppress every admitted country. The last concrete planner defect in the requested delta was the IW-057 FER row calling a retired bulk-content gate. That defect is fixed in the effective tree, but FER still correctly receives zero allocation weight because it has no central runtime content attestation.

This was a read-only gameplay, asset, localisation, and workbook audit. This handoff is the only file edited by this auditor. No file was staged or committed.

## Revision boundary and concurrent-tree drift

The parent requested an audit against `5eda32a6f96df80f9c82094cb3b11028c154bc05` plus an uncommitted Region 05 IW-057 gate.

During the audit another owner committed that delta as `bd8e436c244442c3a09d0dbfe872f68d0a94560c` (`Harden IW-057 FER package reachability`). The effective tree therefore contains:

- Commit `97383c514`, which removes the active Event 006 crisis annex callback and hardens the retirement audit.
- Commit `5eda32a6f`, which rejects stale joint-delivery markers at `chaosx.nr6.1` and repairs invalid formable capital tests.
- Commit `bd8e436c2`, which changes IW-057 planning to the exact FER/408-409 wrapper and adds the package-local FER anchor-owned project guard.

The findings below are against the effective `bd8e436c2` source tree. The Event MCP graph revision remains `98ac244e0b194a88389dbe53658d4876e5d76d2c5eb52b52ff572abea77b4fe3` because the IW-057 trigger-only delta does not change the parsed event graph.

## Decisive findings

### 1. Pre-event crisis surface is fully retired at source

The previous audit finding about a live annex callback is superseded.

- `common/on_actions/006_independence_wave_crisis_on_actions.txt` is absent after `97383c514`.
- `common/scripted_triggers/006_independence_wave_crisis_triggers.txt:9-37` makes occupation pressure, stability pressure, combined pressure, barrier release, crisis opening, and crisis-cost compatibility triggers return `always = no`.
- `events/006_independence_wave.txt:101-123` keeps `chaosx.nr6.3` hidden, triggered-only, and cleanup-only. It clears stale state and performs no release, cost, pressure, queue, history, or player-facing action.
- Repository source search found the names `independence_wave_queue_crisis_release`, `independence_wave_resolve_pre_wave_crisis`, `independence_wave_cancel_pre_wave_crisis`, and `independence_wave_recover_crisis_requester_loss` only inside `common/scripted_effects/006_independence_wave_crisis_effects.txt`. The remaining calls are internal to that compatibility file. There is no external event, on-action, history, interface, or other common-source entry.
- `.tools/audit_event6_allocator.py` now requires the retired on-action file to be absent and rejects external recovery call sites.

Compatibility effect definitions remain in source, but no live source edge reaches them and every public compatibility trigger fails closed. This is a complete source retirement claim, not a live-engine or save-migration claim.

### 2. Manual `chaosx.nr6.1` entry is source-coherent after `5eda32a6f`

`events/006_independence_wave.txt:12-62` now treats `independence_wave_joint_presentation_pending` as a delivery receipt only when the joint plan was executed, the shared plan is committed, the owner is joint, and the frozen presentation count is positive. Any orphaned marker is cleared before `independence_wave_prepare_and_execute_standalone_incident` runs.

The standalone transaction in `common/scripted_effects/006_independence_wave_execution_effects.txt:618-699` then captures the chaos ladder, opens an Event 006 plan, enters allocation, selects and expands packages, executes the frozen plan, and presents `chaosx.nr6.2` only after commit.

The current allocator audit proves a static 1936-style standalone witness of 20 admitted packages and a selectable target ladder of `3/4/5/7/10`. This makes a universal zero-country outcome inconsistent with the current static source witness, but it does not simulate the live country, state, controller, reservation, or plan-phase state used by a manual console call.

### 3. Concrete source defect in the requested IW-057 delta is fixed, but it was not the global manual-entry blocker

At `5eda32a6f`, `can_plan_independence_wave_package_iw_057` used `FER = { is_independence_wave_candidate_tag_available = yes }`. The generic predicate at `common/scripted_triggers/006_independence_wave_package_triggers.txt:74-77` requires `independence_wave_package_content_ready`, and no current setter exists for that retired bulk flag. The package-local FER planner row was therefore unreachable through its own gate.

Commit `bd8e436c2` changes `common/scripted_triggers/006_independence_wave_packages_region_05_triggers.txt:104-117` to `is_independence_wave_exact_package_iw_057_tag_available`. That is a concrete and correct package-local source repair.

It does not admit FER. The central attestation trigger at `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:159-202` still omits IW-057. `independence_wave_calculate_candidate_allocation_weight` initializes every candidate at zero and assigns positive weight only when that attestation passes at `common/scripted_effects/006_independence_wave_package_planner_effects.txt:484-529`. `independence_wave_begin_package_reservation` repeats the same attestation before any reservation at lines 95-108.

Therefore IW-057 cannot receive a positive weight, cannot be selected by the regional or global `random_list`, and cannot poison or starve the admitted pool. Its current fail-closed state is intentional.

### 4. No current source bug is proven to block all admitted countries on manual entry

The source review found no remaining concrete defect that explains every admitted country failing to appear after a first manual `chaosx.nr6.1` call on a resettable plan.

The following previously proven blockers are source-repaired:

- `d6abc3792` recomputes the joint Event 005 plus Event 006 expected count after both selections.
- `7f81b10c1` repairs partial-release candidate and fixed-state depth checks.
- `0c894d449` admits only the planned dormant existing shell during execution preflight.
- `ca48f5485` skips the no-op `release` call for an existing empty shell, then transfers its planned states and sets its capital.
- `5eda32a6f` prevents a stale joint-presentation marker from swallowing a standalone call.

Source-only review cannot replace the missing runtime transaction receipt. A zero-country manual result can still come from current live state, including a non-resettable shared plan phase, no eligible host/anchor after runtime controller checks, or a failure during reservation, execution, transfer, package finalization, or rollback. The existing terminal flags and `global.liberation_plan_last_failure` distinguish these classes, but no live values were supplied and agents do not launch the game.

## Highest-impact bounded next tranche

### Manual-entry invariant and failure-receipt tranche

The safest next source-backed tranche is not another package admission. It is a narrow manual-entry regression and observability tranche around the existing transaction.

Owner scope:

1. Extend `.tools/audit_event6_allocator.py` with direct assertions for the complete `chaosx.nr6.1` standalone call contract, including the stale joint-marker guard, fallback call, committed-only presentation, dormant-shell release bypass, planned state transfer, and capital finalization.
2. In `common/scripted_effects/006_independence_wave_execution_effects.txt`, freeze a compact non-player-facing terminal receipt before cleanup can reset selected counts or arrays. Reuse existing plan phase, last-failure, selected, instantiated, transferred, prepared, validated, activated, and initialized values. Do not add a decision, mission, popup, cost, queue, or pre-event UI.
3. Keep `events/006_independence_wave.txt` player-facing behavior unchanged except for any minimal receipt reset needed before a fresh standalone transaction.
4. Do not widen `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`. IW-057 remains unadmitted until its identity, portrait, flag, rights, roster, and typed probability evidence passes independent review.

Required evidence:

- Narrow pre-change and post-change `hoi4.event_inspect` for `chaosx.nr6.1` with helper expansion.
- Narrow pre-change and post-change `hoi4.event_render` state views for `chaosx.nr6.1`.
- `hoi4.event_compare` between the freshly cached before and after revisions.
- The strengthened allocator audit, with exact source assertions for each receipt field and transaction gate.
- No probability comparison is needed if this tranche changes no weights, MTTH, `ai_chance`, decision score, strategy factor, or random-list candidate. Any weighted change must be routed through `chaosx_ai_probability_auditor` with identical named scenarios before and after.

This tranche is bounded, preserves the retired pre-event contract, and produces the evidence needed to distinguish allocation failure from release, transfer, setup, finalization, or stale-plan failure without admitting incomplete content.

## Completion status by surface

| Surface | Status | Current evidence | Remaining completion gap |
| --- | --- | --- | --- |
| Root event and manual entry | Partial | `chaosx.nr6.1` stale-joint guard and standalone call are source-wired. Event MCP inspect/render report zero selected blocking diagnostics. | No live transaction receipt or successful manual release evidence. MCP helper/lifecycle projection remains partial. |
| Pre-event crisis surface | Complete at source | On-action file absent, all compatibility triggers fail closed, `.3` cleanup-only, no external compatibility-effect callers. | No live save-migration claim. Stale docs still mention a crisis queue. |
| Allocator and execution | Partial | Static allocator audit passes 149 publishers, 32 attestations, 29 groups, 20-package witness, and `3/4/5/7/10` ladder. Dormant-shell and partial-release repairs are present. | Weighted runtime scenarios and live atomic transaction evidence remain incomplete. |
| Country package registry | Partial | 32 centrally attested packages and 40 adapters exist. | 161 selectable rows remain unattested. Eight adapter-only rows fail closed. Package-local source is not central availability. |
| IW-057 FER | Package-local partial and fail-closed | Exact FER/408-409 planner gate and anchor-owned project guard are present. | No central attestation. Identity, grounded portrait, neutral flag, rights, roster, and typed probability evidence remain blocking. |
| Decisions and missions | Partial | Shared and admitted-package surfaces exist. The retired crisis decision/category remain absent. | Many unadmitted package surfaces remain incomplete or intentionally unreachable. Current typed AI/timing evidence is incomplete. |
| Focus tree | Partial | Shared Event 006 tree remains source-wired with prior MCP inspect/render evidence. | Authored diagnostic closure, icon issues, and final probability/runtime evidence remain open. |
| Evolutions and incidents | Partial | Source wiring exists for admitted and source-complete tranches. | Reachability depends on admitted packages and formables. No current complete lifecycle comparison exists. |
| Formables | Partial and fail-closed | Generic registry and multiple dedicated formable families exist. FORM-16 static audit passes. | Accepted formable families remain incomplete or intentionally gated. FORM-48 and other late families remain conditional. |
| Event Log and Event Details | Partial | Root, detail, and history wiring exist for the current admitted baseline. | Full package, evolution, formable, and runtime availability remains narrower than accepted design. Stale crisis wording remains in docs. |
| Statehood Ledger GUI | Partial | Static semantic matrix passes and the required event-owned UI handoff exists. | Runtime render, state, resolution, hierarchy, click-region, save/load, and accepted post-change comparison remain incomplete. |
| Formable state-puzzle GUI | Partial and visually blocked | Dedicated event-owned GUI handoff and current aggregate MCP inspection exist. | Family-isolated state and click acceptance is not proven. Aggregate overlap diagnostics remain. |
| SCN-008 | Partial | Static matrix passes 32 scenario cells and 8 edge cases. | Availability remains limited by package and transaction gates. Runtime scenario probability evidence is incomplete. |
| Super-event 23 | Blocked | Visual and text registration exist. | Exact audio redistribution rights remain blocked. No fallback is authorized. |
| Super-event 24 | Partial | Audio, visual, definition, localisation, history, and queued playback source exist. | Hidden-formable reachability and runtime playback evidence remain incomplete. |
| Achievements | Partial | Definitions, localisation, assets, and proof-writer source exist. | Campaign reachability depends on unfinished package, formable, League, scenario, and super-event surfaces. |
| Assets and portraits | Partial | Structural flag-family coverage exists for the registered set. | Structural filenames do not prove identity or provenance. Every grounded character still needs accepted portrait-creator evidence. IW-057 remains blocked here. |
| Custom 3D, unit audio, counters | Not in accepted scope | No accepted Event 006 custom 3D unit package was found. | None. Do not invent this surface. |
| Localisation | Partial | Current admitted baseline is substantially wired. | Whole-event current audit and stale crisis/package wording reconciliation remain open. |
| Workbook and catalog | Aligned to partial availability | Existing authority records Event 006 and Liberations as partially available and SCN-008 as unavailable. | Update only after gameplay availability changes, using the workbook as sole editable source. |
| Documentation | Stale in bounded places | Current handoffs preserve counts and fail-closed package boundaries. | Source map still mentions a crisis queue, misstates `.350` recruitment, and retains stale FER dormant-capital wording. |
| Probability and AI | Partial and evidence-limited | Source attestation makes IW-057 weight zero. A bounded probability-auditor refresh is recorded below when available. | Full same-scenario allocator, mission, option, and AI comparison evidence remains incomplete. |

## Current authority counts

- 149 publishers.
- 126 automatic/high-chaos selectable rows.
- 138 SCN-008-ranked rows.
- 40 runtime adapters.
- 32 centrally content-attested packages across 29 compatible reservation groups.
- 8 adapter-only fail-closed rows: IW-013, IW-015, IW-043, IW-058, IW-093, IW-098, IW-177, and IW-179.
- 161 unattested selectable rows.
- Static standalone witness of 20 admitted packages.
- Automatic ladder `3/4/5/7/10`, with World Collapse at 10.

The centrally admitted set remains IW-001, IW-002, IW-004, IW-006, IW-007, IW-008, IW-009, IW-010, IW-012, IW-014, IW-017, IW-018, IW-019, IW-023, IW-024, IW-026, IW-027, IW-028, IW-029, IW-030, IW-031, IW-033, IW-038, IW-040, IW-041, IW-044, IW-045, IW-070, IW-071, IW-072, IW-173, and IW-184.

## Accepted-plan disposition

| Accepted plan family | Current disposition |
| --- | --- |
| Core allocator, API, ladder, and 32-package admission authority | Implemented at source, static PASS, runtime and complete probability evidence still open. |
| Dormant-shell, partial-release, joint-count, and stale-entry repairs | Implemented at source through `5eda32a6f`. The current audits should add direct regression assertions. |
| Pre-event crisis removal | Implemented at source through `97383c514`. Older live-callback findings are superseded. |
| IW-057 exact planner and anchor-owned project gate | Implemented package-locally in `bd8e436c2`. Central admission remains blocked. |
| IW-047, IW-048, IW-050, IW-051, IW-052, IW-053, IW-054, IW-057, and IW-060 package-local families | Queued or package-local. None is silently promoted by this audit. |
| IW-043/IW-058 and IW-093/IW-098 signature addenda | Adapter/source work exists. All four remain fail-closed centrally. |
| FORM-48 Pacific Federation | Bounded source work exists. Gameplay reachability remains conditional on unadmitted member and identity proof. |
| Shared focus diagnostic closure | Partial. Current source and MCP evidence do not support whole-tree completion. |
| Super-event 23 | Blocked on exact audio rights. No fallback approved. |
| Super-event 24 | Source-wired. Runtime and reachability proof remain partial. |

No fallback, design simplification, or package promotion was approved by this audit.

## Documentation and catalog gaps

- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md:167` still tells the parent to preserve a crisis queue sentence. That instruction is superseded by the fully retired source contract.
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md:99` still says `chaosx.nr6.350` recruits NAV/GLC commanders. Current recruitment is owned by the relevant history/general source, while `.350` is a readiness checkpoint.
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md:7` and `docs/events/006_independence_wave/far_eastern_republic_package.md:11` retain stale wording that the FER pre-release gate tolerates dormant capital 563. Current exact planning uses ordered available anchors 408 or 409 and shared execution reanchors before setup.
- `docs/specs/006_independence_wave_specs/quality/simplifications_omissions_and_blockers.md:13` calls FER outside gameplay. Current wording should distinguish package-local implementation from central runtime admission, which remains absent.
- The workbook should not change for the IW-057 exact gate because player-facing availability did not change.

## Meaningful validation performed

- `.tools/audit_event6_allocator.py`: PASS with 149 publishers, 126 automatic/high-chaos rows, 138 SCN-008 rows, 40 adapters, 32 attestations, 29 groups, 161 unattested rows, a 20-package witness, retired crisis assertions, and the `3/4/5/7/10` ladder.
- `.tools/audit_event6_country_api.py`: PASS with 242 broad unique tags, 191 resolved unique carriers, 34 Soviet rows, 45 Africa rows, and no missing or duplicate entries.
- `.tools/audit_event6_scenario_matrix.py`: PASS with 32 cells and 8 edge cases.
- `.tools/audit_event6_form16.py`: PASS for ARM/GEO/AZR exact state, consent/refusal, mutation, rollback, cleanup, and readiness contracts.
- `.tools/audit_event6_gui_matrix.py`: PASS for static Statehood Ledger declarations only. It explicitly does not prove runtime rendering or save/load behavior.
- Source search confirms the crisis on-action file is absent and compatibility helper names have no external callers.

These are source assertions, not live engine receipts.

## Mandatory Event MCP evidence and exact limits

Narrow `hoi4.event_inspect` and `hoi4.event_render` were run for both the active root `chaosx.nr6.1` and retired compatibility event `chaosx.nr6.3`.

Current graph revision: `98ac244e0b194a88389dbe53658d4876e5d76d2c5eb52b52ff572abea77b4fe3`.

Root `chaosx.nr6.1` inspection returned `EVENT_INSPECTED_PARTIAL` with zero selected blocking diagnostics. Artifact:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/aa3fac6aa0c70f5372dfd63aaad853f6d1e1e0adb91c2cc02c6f8376b7068d48/145be9e669ff590d568ecbf83ab5864966cd038f86dac05479932cd8a64a32da/event-lint-98ac244e0b19.json`

Root state render returned `EVENT_RENDERED_PARTIAL`, selected 3 nodes, omitted 41,147 graph elements, and reported zero selected blocking diagnostics. Manifest:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6a99e3ab7f04ba321430ff9379cdceda37a03cf52774f76b82d1c0eb8f805e96/be69664f5d1f58679988c09e043b653b63e4300b9f76859c0f2eb3aa9b82d308/event-state-98ac244e0b19-manifest.json`

Retired `chaosx.nr6.3` inspection returned `EVENT_INSPECTED_PARTIAL` with zero selected blocking diagnostics. Artifact:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0e989ab55767be761f402171b264161708a1282a156ec2d04e56ad50e1976a3d/5779f99e90a3ed2c2e59353e861884933fa64174aa35263946888ea415f7ce6d/event-lint-98ac244e0b19.json`

Retired `.3` state render returned `EVENT_RENDERED_PARTIAL`, selected 1 node, omitted 41,149 graph elements, and reported zero selected blocking diagnostics. Manifest:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/64180089b14078ea0982f7cb1be3cb453a099493ee825481c142517673e2abb3/219166e5a643eb4b2b57105e68ef3e84aa38567f21dbd73d286cdd3f86cf6377/event-state-98ac244e0b19-manifest.json`

Both routes are partial because the large workspace deferred workspace-wide helper projection and lifecycle passes. The source inventory is also truncated inline. MCP source analysis is not live-game execution evidence.

`hoi4.event_compare` was attempted from the previously recorded baseline revision `56319b626db35b6868af821d757627f0054085fc107d0e22b7a8df13e25f37cd` to the current revision. It returned the exact blocker `EVENT_REVISION_NOT_CACHED`. No comparison artifact exists, and source diff review is not equivalent evidence.

## Probability evidence

The automatic package allocator is a weighted surface. A bounded refresh was routed through `chaosx_ai_probability_auditor` for the manual `chaosx.nr6.1` pool and IW-057 only. The worker did not return a final report or artifact before this audit was required to finalize, including after an explicit immediate-final request, so the worker was stopped. This is an evidence blocker, not a probability pass.

The existing direct FER pool inspection recorded in `006_iw057_fer_country_package_audit_2026-08-20.md` reports `poolComplete=false`, `candidates=0`, and `availableCandidates=0`. That structural result is consistent with the missing IW-057 central attestation, but it is not a worker-backed scenario evaluation and cannot support dominance, starvation, MTTH, seeded distribution, or quantitative balance claims.

## Remaining blockers and next actions

1. Complete the bounded manual-entry invariant and terminal-receipt tranche before widening package admission.
2. Preserve the fully retired crisis boundary and remove stale crisis-queue documentation wording in a docs-only pass.
3. Keep IW-057 centrally fail-closed until its identity, portrait, flag, rights, roster, and typed probability contracts are accepted.
4. Obtain isolated event-owned GUI state, resolution, hierarchy, click-region, and comparison evidence for the Statehood Ledger and formable puzzle surfaces.
5. Close the remaining shared focus diagnostics and probability evidence without treating unrelated vanilla diagnostics as Event 006 completion.
6. Preserve Super-event 23 as blocked until exact redistributable audio is accepted. Do not substitute generated, synthesized, placeholder, or unlicensed audio.
7. Reconcile the bounded stale documentation statements. Change the workbook only after player-facing availability changes.

## Skills and references applied

This refresh applied `chaos-redux-events`, `chaos-redux-improvement-loop`, `chaos-redux-subagents`, and `chaos-redux-event-planning`. The prior full audit also applied the relevant decisions, focus, asset, super-event, and portrait workflows. Required offline Paradox wiki event, effect, trigger, scope, localisation, on-action, decision, idea, and AI references were used with the installed vanilla documentation and vanilla source precedents. The 3D pipeline was not invoked because no accepted Event 006 custom unit surface exists.

No gameplay simplification or substitute was made. All remaining omissions and blockers are explicit above.
