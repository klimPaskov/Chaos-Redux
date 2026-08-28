# Event 006 completion gap audit after `182ed53cf`

Date: 2026-08-28

Mode: read-only Event 006 completion audit. This auditor changed no gameplay, localisation, asset, workbook, specification, or source-of-truth file. The parent applied the two-line source correction identified below in the shared worktree while this audit was active; this handoff records and verifies that parent-owned patch.

## Disposition

Event 006 remains **HOLD / PARTIAL**.

The single highest-impact safe tranche after `182ed53cf` was the former-host autonomy check immediately following absent-country instantiation. Commit `182ed53cf` correctly moved both release paths to candidate scope, then former-host scope, and used `release = PREV`, but both new checks used `PREV = { is_subject_of = THIS }`. After entering `PREV`, `THIS` is the candidate and `PREV` is the former host, so that expression asks whether the candidate is subject to itself. It fails and suppresses the intended `autonomy_free` conversion.

This is a source defect, not an MCP-only uncertainty. Official `effects_documentation.md:5724-5731` states that `release` releases the target **as a puppet**. Official trigger documentation states that `is_subject_of` checks the current country against the specified target. The offline scope reference defines `THIS` as the current scope and `PREV` as the containing scope. Vanilla `common/scripted_effects/TOA_scripted_effects.txt:1306-1313` uses the same nested-country shape and the exact expression `PREV = { is_subject_of = PREV }`.

Without correction, an absent Event 006 carrier can be instantiated and transferred its frozen territory but remain a subject of its former host. The same defect affects the Event 005 half of the shared Event 005+006 executor. That contradicts the Event 006 promise of sovereign releases and makes recognition, former-host settlement, league, patron, formable, focus, decision, and achievement behavior start from the wrong diplomatic state.

## Parent-applied bounded correction

The shared worktree now contains the exact safe correction:

- `common/scripted_effects/006_independence_wave_execution_effects.txt:503-518`, in `independence_wave_release_one_frozen_country`: `PREV = { is_subject_of = PREV }`.
- `common/scripted_effects/005_006_liberations_collision_effects.txt:1051-1065`, in `soviet_collapse_joint_release_one_frozen_country`: `PREV = { is_subject_of = PREV }`.

No unconditional autonomy change is needed. The corrected predicate scopes the candidate, tests it against the containing former host, and preserves the existing defensive `set_autonomy = { target = PREV autonomy_state = autonomy_free }` call. Dormant Event 006 shells still follow their separate state-transfer formation path and do not need the absent-tag `release` call.

This tranche must remain limited to those two target corrections plus the normal parent-owned handoff/source-of-truth reconciliation. It must not alter package admission, reservation ordering, exact counts, host remnants, Event 005/Event 006 origin ownership, force packages, AI weights, or the no-pre-event surface.

## Task-specific verification

Post-correction source checks find the intended `PREV = { is_subject_of = PREV }` at both callsites and no remaining `PREV = { is_subject_of = THIS }` in either executor.

The maintained source validators all pass after the parent patch:

- allocator: 149 publishers, 126 automatic/high-chaos candidates, 138 SCN-008-ranked candidates, 40 adapters, 32 attestations, 29 compatible reservation groups, and exact `3/4/5/7/10` automatic targets with World Collapse at 10;
- country API: 191 resolved unique carriers, no missing or duplicate carrier IDs;
- strict flag families: 102 of 102 complete;
- FORM-16: exact ARM/GEO/AZR member and cleanup contract preserved;
- SCN-008: all 32 mode/intensity cells and eight edge cases preserved.

These validators did not detect the original nested-scope error and therefore are regression evidence only, not proof of the autonomy semantics. The official docs and vanilla scope precedent are the decisive source evidence for this correction.

## Mandatory Event MCP evidence and limit

Fresh read-only calls now produce artifacts instead of the earlier `ARTIFACT_MANIFEST_INTEGRITY_FAILED` blocker, but remain partial:

- Event 006 lint for `chaosx.nr6.1`: `EVENT_INSPECTED_PARTIAL`, revision `c2878e0a5f2b2d2bbbaa42bbd299a378b5a6c1d4ef25b9c4f58df51bcc9a885a`, validation false, `helpers = 0`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8b1579f2f2d1a04f226665512d0fb29d5545c8a2eb2cf2ffc1f5d37e75214b85/a8cbd52f149857d4a90257d2451d2b3f9c6a26afa0af97d38a9efbc8daf28f61/event-lint-c2878e0a5f2b.json`.
- Event 006 scope render: `EVENT_RENDERED_PARTIAL`, two selected nodes, `helpers = 0`; manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dc954bf39a5f18cfd203dc9ea47f4870eb11265bc7cb2293f639fef6ca98b7c8/a2685dc242490bfc40e14e755b4f5314ae663a73d9583b781f8b5378ff6bc210/event-scope-c2878e0a5f2b-manifest.json`.
- Shared Event 005 root state-flow inspection: `EVENT_INSPECTED_PARTIAL`, the same revision, validation false, `helpers = 0`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0b299099e827846e24476ffea57ce1ef6837b7d4c29f1bbf06ad217e25dce282/3f0b30caa231baaf4874debe985e6059a1e380b5e479789caa1bce469bebe356/event-state_flow-c2878e0a5f2b.json`.
- Shared Event 005 root scope render: `EVENT_RENDERED_PARTIAL`, three selected nodes, `helpers = 0`; manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/918f62b4cb1c78472727633717b0f39c728bc86d6f59efa56b6e1275a57585a3/b6a748f8317feeba9479f86922f680600723593db9fb78e7f5728a1074bbec2c/event-scope-c2878e0a5f2b-manifest.json`.

The event graph revision did not change across the two-line scripted-effect correction because these projections expanded zero helpers. The MCP route therefore cannot verify this helper-level scope fix. `hoi4.event_compare` returns `EVENT_COMPARISON_BASELINE_REQUIRED: Provide a cached revision, graph artifact, or proposed source overlay`; no semantic before/after artifact exists, and source review is not presented as equivalent event-graph evidence.

No weighted value changed in this correction. The required Event 006 probability audit was routed to `chaosx_ai_probability_auditor`, then stopped at the parent finalization boundary without a new quantitative result. Existing typed probability and same-scenario comparison gaps remain open; this correction makes no balance claim.

## Completion status by surface

| Surface | Status after the parent correction | Evidence and remaining gap |
| --- | --- | --- |
| Root event, committed-only presentation, Event Log, Event Details, and no pre-event UI | **Source-complete; MCP partial** | `chaosx.nr6.1` remains hidden, presentation is committed-only, and the runtime-unlock gate keeps the thirteen overlays inert before Event 006. Current Event MCP projections are partial and expand zero helpers. |
| Exact allocator, reservation-first release, host survival, and Event 005 collision | **Source-strong for admitted packages; partial overall** | The exact `3/4/5/7/10` ladder, anchor-before-optional reservation order, protected remnants, origin-owner arrays, and corrected absent-tag release/freeing paths are present. Only 32 packages across 29 groups are attested, and no helper-level MCP transaction proof exists. |
| Event 005/Event 006 origin separation | **Source-present; MCP partial** | The shared plan stores per-country owners and applies separate origin packages. The autonomy-scope correction prevents the Event 005/006 release path from accidentally retaining former-host subject status, but the event viewer does not expand the helper chain. |
| Country packages and overlays | **PARTIAL / largest breadth gap** | The current boundary remains 32 content-attested packages, 40 adapters, and 161 unattested selectable rows out of 193 non-overlay rows. The eight adapter-only IDs remain fail-closed. Part 5 requires every admitted package to include identity, territory, host, leadership, ideas, forces, relations, AI, assets, and cleanup; most rows do not. |
| Shared mechanics, decisions, and missions | **Source-broad; acceptance partial** | The current receipt covers 80 accepted decision/mission rows, while direct decision/GUI evidence, density/exploit evidence, and typed probability remain incomplete. |
| Focus framework | **Bounded source/MCP geometry complete; package breadth partial** | The accepted shared tree has 184 focuses and 195 connectors with zero Event 006 layout diagnostics. Package-specific access, AI, and the 161-row breadth requirement remain incomplete. |
| Five evolutions | **Source-wired; MCP/probability partial** | Events `.360` through `.364`, paid decisions, ledgers, cleanup, and documentation exist. Per-family helper expansion, timing evaluation, and comparison evidence remain incomplete. |
| League and formables | **PARTIAL / blocked families** | Network/league and bounded formable systems exist, but FORM-06 through FORM-47 remain fail-closed except accepted bounded families, FORM-42 is blocked, and FORM-48 is unreachable until FSM is admitted. |
| SCN-008 | **Static matrix pass; event/MCP partial** | All 32 cells and eight edge cases pass the maintained validator. Candidate completeness is still limited by package admission, and the event viewer does not prove the scenario helper transaction. |
| Super-events | **23 blocked; 24 partial** | Super-event 23 lacks approved worldwide redistribution rights, final WAV/wrappers, and firing. Super-event 24 is source-wired but qualifying reachability depends on incomplete package/formable/league surfaces. |
| Achievements | **Source-present; reachability partial** | Sixteen definitions and 48 icon states exist; signature, league, formable, and package achievements inherit their owner-surface blockers. |
| Assets and portraits | **PARTIAL** | The strict 102-tag flag audit passes, but grounded package rosters, approved portrait consumers, remaining historical symbols, animations, and package admission evidence remain incomplete. No accepted Event 006 custom 3D unit is in scope. |
| Documentation and catalog | **Current bounded alignment; final closure absent** | The XLSX/CSV repair and Event 006 wording alignment are current, with Event 006 and SCN-008 still marked `Needs Testing` and the whole event still HOLD/PARTIAL. No final whole-spec completion report exists. |

## Accepted-plan disposition

- Exact `3/4/5/7/10` allocation and reservation-first locking: implemented for the admitted set; full 193-row admission remains queued.
- Synchronized absent-country creation: the `release = PREV` repair and this parent-owned subject-scope correction close the identified static execution defect; MCP helper/runtime proof remains unavailable.
- Absolute no-pre-event UI and thirteen post-event overlays: implemented in current source and must be preserved.
- Separate Event 005 origins: source-present and retained; shared Event 005 release now carries the same corrected autonomy check.
- Shared focus, mechanics, decisions/missions, five evolutions, SCN-008, achievements, and bounded formables: implemented in bounded tranches, not whole-spec complete.
- Complete playable country breadth, remaining formable families, league acceptance, package assets/portraits, probability/balance, super-event 23, and final completion evidence: unresolved, blocked, or queued.

## Recommended continuation after this correction

Do not widen the release transaction again unless a concrete failure receipt proves another defect. Reconcile the two-line parent patch into the current source-of-truth/resume handoffs, retain the partial MCP limitation, and return to the accepted package-admission queue one package at a time. IW-095 remains the most developed first-footprint candidate but cannot be centrally promoted until its exact DAH shell, identity/rights receipt, neutral symbol, approved portrait roster, adapter/publisher/preflight/Join wiring, typed probability evidence, and package audit are complete. IW-108, IW-136, IW-130, IW-086, and IW-073 remain behind their recorded identity, ownership, symbol, or package source gates and must not receive fallback identities.

## Files changed by this auditor

- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_post_182ed53_completion_gap_audit_2026-08-28.md`

No gameplay file was edited, staged, or committed by this auditor.
