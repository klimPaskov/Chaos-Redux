# Event 006 Completion Audit: Next Implementable Gap — 2026-08-27

## Scope and authority

This is a read-only completion audit of the current Event 006 worktree against the accepted specifications under `docs/specs/006_independence_wave_specs/` and the current implementation authority in `006_source_of_truth_map.md` and `006_independence_wave_resume_packet.md`.

The audit inspected current source and current handoffs rather than treating older completion statements as proof.

No gameplay, localisation, asset, spreadsheet, or runtime file was modified.

## Overall status

Event 006 remains **HOLD / PARTIAL**.

The established 32 content-attested selectable packages across 29 compatible reservation groups remain the current admission boundary.

The 40 runtime adapters and 161 unattested selectable rows remain distinct from content-complete admissions.

The highest-impact accepted implementation tranche that can begin next is the queued IW-095 Dahomey first-footprint package, but only as a package-local, fail-closed implementation before central admission.

## Completion status by surface

| Surface | Status | Current evidence |
| --- | --- | --- |
| Core release transaction and Event 006 chain | Partial | Current `hoi4.event_inspect` and `hoi4.event_render` passes covered `chaosx.nr6.1`, `chaosx.nr6.36`, `chaosx.nr6.360`, `chaosx.nr6.18`, `chaosx.nr6.11`, `chaosx.nr6.28`, `chaosx.nr006.9301`, `chaosx.nr006.4301`, `chaosx.nr006.5801`, and `chaosx.triggerable_scenarios.8`. Every pass returned partial evidence with zero selected blocking diagnostics, but workspace-wide helper projection and lifecycle analysis was deferred. This is not whole-event runtime proof. |
| Current Event 006 event files | Partial | `events/006_independence_wave.txt` and `events/006_independence_wave_support_events.txt` inspected and rendered at revision `f4498b37c697c07740140bb23b02d908df5473bdfcc019d7525da28cf9e54d1f`, graph hash `a7769ee9b5dfe64de2a119153942198763813bd1b5323539466907771e0b4f40`. Aggregate scan: 9,510 events, 14,700 options, 1,075 entries, 8,315 unresolved nodes, 7,651 terminals, 37,141 edges, 28,259 state accesses, 2,129 diagnostics, and zero blocking diagnostics. The MCP explicitly marked validation incomplete because large-workspace helper and lifecycle projections were deferred. |
| Event comparison | Blocked | Comparing the recorded prior revision `730a452a72e0a477b59c5cc2a817aa8781cdd5cb89f9ca3272636a23c3f9d31a` with the current revision failed with `EVENT_REVISION_NOT_CACHED`. Source diff is not equivalent comparison evidence. |
| Focus tree | Structurally complete, content breadth partial | Current `hoi4.focus_inspect` and `hoi4.focus_render` on `independence_wave_focus_tree` returned 184 focuses and 195 connectors with zero crossings, node intersections, long connectors, too-close pairs, or Event 006 diagnostics. This closes layout quality, not the absent package-specific route breadth or AI/balance proof. |
| Decisions and missions | Partial | The 2026-08-26 decision/mission receipt covers all 80 accepted rows and required columns, so older statements that this receipt is missing are stale. Direct decision/mission visual and runtime proof remains unavailable, and probability evidence is separately required. |
| Possible-country resolution | Source-repaired, runtime proof open | `006_event6_absent_target_release_validation_repair_2026-08-27.md` records the newer plan-array membership repair for dormant absent tags in `common/scripted_effects/chaosx_liberation_release_effects.txt` and the generic capital trigger. It explicitly does not establish live nonempty transaction, whole-event lifecycle, package attestation, probability, or GUI proof. The source-of-truth map and resume packet predate this narrow delta. |
| Statehood scripted GUI | Partial / current MCP blocked | The required named event-owned UI worker handoffs exist, so missing worker ownership is not the defect. A fresh current `hoi4.gui_inspect` and 14-state, three-resolution render attempt for `independence_wave_status_window` failed with `ARTIFACT_MANIFEST_INTEGRITY_FAILED: Artifact provenance manifest does not match its immutable address`. Older layout artifacts do not substitute for clean current inspect, render, hierarchy, click-region, overflow, rewrite, and compare evidence. |
| Package admission breadth | Partial | No current `iw095_*` gameplay identifiers or first-footprint package-local implementation files exist. The accepted 2026-08-26 first-footprint addendum remains queued rather than implemented or admitted. |
| Formables | Partial / blocked families | The admitted bounded families remain implemented, while much of FORM-06 through FORM-47 is still incomplete or fail-closed. FORM-42 remains blocked. FORM-48 remains structurally implemented but unreachable while FSM is unadmitted. |
| Super-events | Partial / blocked | SE23 remains blocked because the accepted London Brass recording lacks verified worldwide redistribution permission; it has no accepted WAV, wrapper, or firing path. SE24 is source-wired but reachability is still partial. No fallback is approved. |
| Portraits and identity assets | Partial / blocked | The current source map recognizes only NAV Aguirre and GLC Castelao as current styled final exact matches. IW-095 has no approved final grounded identity portrait package and its source research remains `needs_user_review`. |
| Flags and visual assets | Partial | Existing shared Event 006 asset families are largely source-wired, but consumer/provenance breadth remains partial. IW-095 has no approved 1936 identity flag family. The neutral vanilla DAH flag is a later Republic of Dahomey/Benin identity and is not an accepted 1936 baseline. |
| Custom 3D units, unit audio, and counters | Not in scope | Event 006 has no accepted custom 3D unit package, so the 3D model, sourced unit-audio, and bespoke counter completion gates do not apply to this event revision. |
| Catalog and player-facing documentation | Correctly partial | The workbook currently reports Event 006 and SCN-008 as `Needs Testing` and the Liberations cluster as `Partially Available`, which is consistent with the current incomplete state. The queued first-footprint design has not been promoted as implemented. |

## Highest-impact concrete next gap

Implement the accepted IW-095 Dahomey first-footprint package as a package-local, fail-closed tranche without changing central admission counts, readiness lists, dispatch, scenario capacity, or join routing.

The accepted file ownership is:

- `common/scripted_effects/006_independence_wave_first_footprint_package_effects.txt`
- `common/scripted_triggers/006_independence_wave_first_footprint_package_triggers.txt`
- `common/decisions/006_independence_wave_first_footprint_decisions.txt`
- `common/ai_strategy/006_independence_wave_first_footprint_ai_strategy.txt`
- Existing Event 006 ideas, characters, script constants, localisation, and focus files only where the accepted IW-095 callbacks and rewards require integration.

The accepted player-facing identifiers are:

- Mission: `independence_wave_iw095_reconcile_abomey_and_porto_novo`
- Projects: `iw095_convene_abomey_council`, `iw095_reopen_coastal_customs`, `iw095_register_palm_and_market_revenue`, `iw095_organize_civic_guard`
- Settlements: `iw095_ratify_civic_compact`, `iw095_restore_council_authority`, `iw095_authorize_emergency_directorate`
- Network action: `iw095_open_west_african_trade_mission`
- Focus callbacks: `independence_wave_iw095_focus_*`
- Formable relationship: FORM-24 remains gated until its wider family is admitted.

The current map binding must remain state 776.

The older research baseline 556 is stale and must not enter runtime effects, tooltips, tests, or admission evidence.

This tranche is safe to implement behind the existing fail-closed admission boundary because it can establish package mechanics, cleanup, idempotence, focus callbacks, AI ownership, and static receipts without making DAH selectable.

## Admission blocker that requires user disposition

IW-095 must not be centrally admitted until its identity package is resolved.

The current asset research leaves the historical 1936 baseline blocked and the alternate-history civic flag route at `NEEDS_USER_REVIEW`.

The leader and authentic institution research also remains `needs_user_review`; Justin Aho is conditional evidence for a royal or customary institution, not proof of a 1936 government, while other candidates have date, metadata, or licence conflicts.

The parent should obtain an explicit user choice between the source-attested Abomey institution route and an explicitly alternate-history civic identity brief, then route the grounded portrait and flag package through the required asset specialists.

No generic, later-era, copied, or unlicensed fallback should be wired.

## Accepted-plan disposition

- `006_event6_first_footprint_admission_improvement_addendum_2026_08_26.md`: **accepted and queued; not implemented**. IW-095 remains first, followed by IW-108 Buganda, IW-136 Sindh, IW-130 Madagascar, IW-086 Tripolitania, and IW-073 Hejaz.
- The 80-row decision/mission validation receipt: **implemented documentation evidence; older missing-receipt gap is stale**.
- `006_event6_absent_target_release_validation_repair_2026-08-27.md`: **current narrow source repair; not yet folded into the older source map/resume packet and not whole-event proof**.
- IW-095 map reconciliation: **accepted current binding is state 776; the 556 research baseline is superseded for runtime use**.
- SE23 audio: **blocked, not queued for fallback wiring**.
- Unadmitted formable and package families: **remain intentionally fail-closed, not complete**.

## Required validation after the next implementation tranche

Before central IW-095 admission, the parent should require:

1. Package-local source review proving setup idempotence, cleanup, branch exclusivity, mission expiry behavior, focus callback ownership, force preservation, and absence of magic tuning outside the accepted constants table.
2. Current map evidence for state 776 and current focus inspect/render evidence after IW-095 callbacks are introduced.
3. Current event inspect/render evidence for the DAH path and a successful event comparison against a retained pre-admission revision.
4. A probability audit and same-scenario comparison for every new `ai_will_do`, mission score, event `ai_chance`, strategy factor, or weighted selection surface.
5. Approved final flag triplet and grounded portrait/institution handoffs with provenance and consumer wiring evidence.
6. One atomic central admission change only after every package-local and asset gate passes, followed by recomputed admission, reservation, adapter, and unattested-row counts.

## Recommended parent action order

1. Review and implement the package-local IW-095 fail-closed tranche using the exact accepted identifiers above.
2. Ask the user for the IW-095 historical-versus-alternate identity disposition and route approved portrait and flag work; do not choose a fallback silently.
3. Repair or retry the HOI4 GUI artifact-manifest route so current Statehood evidence can be produced.
4. Preserve the current 32-package admission boundary until the IW-095 mechanics, identity assets, and required MCP/probability evidence are complete.
5. Admit IW-095 atomically and recompute all boundary counts only after those gates pass, then continue the fixed first-footprint order.

## Remaining completion blockers

- No live whole-event transaction and lifecycle proof.
- Event helper and lifecycle analysis remains deferred by the current large-workspace MCP pass.
- The recorded event comparison revision is unavailable from the current MCP cache.
- Current Statehood GUI MCP provenance-manifest integrity failure prevents clean evidence.
- IW-095 identity, flag, and portrait disposition is unresolved.
- SE23 worldwide redistribution rights are unresolved.
- Broad unadmitted package and formable families remain incomplete or fail-closed.
- Final weighted-logic evidence is pending the dedicated probability audit.

