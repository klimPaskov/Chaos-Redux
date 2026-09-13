# Event 021 Random Civil War: late-stage release gate

Date: 2026-09-02.
Root event: `chaosx.nr21.1`.
Disposition: stop expansion; release remains blocked.
This is a bounded, plan-only gate handoff, not a completion certificate.

## Decision and ownership

No new gameplay mechanic, route, country, focus tree, GUI, formable, super-event, animation, or visual family is justified.
The existing design already supplies the required domestic-war, independence, exposure, settlement, reconstruction, and recurrence structure.
Remaining work consists of narrow integration corrections, strict asset-status resolution, and evidence for the final source.
Neither helper delivery nor an earlier source-complete statement proves release readiness.

Only this handoff was written by the planner.
Gameplay, assets, spreadsheets, configuration, existing plans/specs, and Git staging were not changed.
No game was launched and no commit was created under the user's read-only boundary.
The parent owns every proposed correction, final integration review, specialist routing, and completion decision.

The user requested that this review finish before further broad inspection.
Consequently, the evidence queues below are deliberately unresolved, including fresh focus/GUI/map certification and a complete final helper-source review.
This document does not represent a full re-audit of every implementation file or every inherited asset.

## Evidence and prior-plan disposition

The review read the complete Event 021 specification package, including its prompts, manifest, supporting matrices, research notes, and source-read ledger.
The master specification was checked to contain all ten numbered parts verbatim, and its remaining wrapper text was read separately.
The overview, acceptance evidence, active September 2 repair ledger, both named improvement-loop documents, the Event 021 event file, relevant current integration call sites, and the recent treaty, successor, and inherited-asset handoffs were reviewed.
Current call-site checks supersede older handoff statements that treaty and roster helpers have not been integrated.
They do not certify the integration's complete behavior.

`improvement_loop_addendum.md` is dispositioned as historical implementation-resolved design with certification pending.
`post_fix_improvement_loop_closure_addendum_2026-08-31.md` already rejects further expansion and queues proof.
The September 2 active repair ledger supersedes their stronger source-complete assertions wherever later defects are recorded.
Those accepted obligations remain open until the parent records their actual resolution.
This handoff consolidates that gate and does not create a second expansion layer for the same gaps.

Installed vanilla documentation was consulted for `start_civil_war`, `add_to_war`, `annex_country`, `white_peace`, event targets, and script constants, alongside the required offline wiki references and the annex/civil-war callback scope contract.
The documentation distinguishes war participation from annexation and troop transfer.
It does not establish that rebinding a front registry preserves actual wars.

## Findings: implement, queue, or reject

Classification (a) means an exact narrow correction or status disposition for the parent to implement.
Classification (b) means evidence-only work: do not change balance or gameplay merely because proof is missing.
Classification (c) means reject the proposed scope change.
Queued release-critical evidence still blocks release.

### G01 — (a) Implement: separate Event 006 local content access from its lifecycle

Current `common\scripted_triggers\006_independence_wave_triggers.txt` contains a durable `is_independence_wave_event021_package_country` branch in `is_independence_wave_package_content_active`.
However, `is_independence_wave_active_country` still correctly requires `independence_wave_active_origin`, and `is_independence_wave_event6_player_surface_allowed` both requires that strict origin and rejects the Event 021 adapter receipts.
Current country-local categories still use the strict predicate, including `independence_wave_bbx_epirus_council_category` in `common\decisions\categories\006_independence_wave_categories.txt`.
Thus preserving the completed adapter receipts does not by itself expose all promised package-local play.

Minimal patch: in the admitted-package local category and decision consumers identified by `subagent_handoffs\event006_reused_asset_crosswalk_2026-09-02.md`, replace only the lifecycle-only content-access test with the completed origin-neutral package branch, retaining package identity, setup, rights, and action-specific gates.
Use an explicit completed-package player-surface predicate for local formable/progression consumers that currently call `is_independence_wave_event6_player_surface_allowed`.
Do not expose the temporary `adapter_preparing` branch to player clicks.
Do not globally loosen either strict lifecycle predicate or mechanically replace every use.
The exact first regression fixture is an Event 021-origin `iw_028/BBX` actor satisfying its setup gate before and after reconstruction.

Keep network, league/congress, evolution, origin registries, and scenario-ledger consumers on their existing lifecycle gates.
A local recognition or patron action needs its own call-chain review if it can enroll an actor in a global institution.
Acceptance requires local decisions, reinforcement, formation/formables, focus access, and AI to remain usable without firing `chaosx.nr6.1`, changing Event 006 weights/caps/counts/evolutions, or inserting Event 006 origin/network membership.
The remaining 32-package reachability proof is G07, not permission to widen the admitted package set.

### G02 — (a) Implement: finish successor preparation at the pre-destruction boundary

Current `event021_parent_prepare_annex_successor` calls `event021_prepare_successor_roster_adoption`, and `common\on_actions\021_random_civil_war_cxt_on_actions.txt` calls preparation, predecessor treaty/lifecycle handling, then `event021_adopt_successor_roster` inside `on_annex`.
Do not report those calls as missing.
However, the inspected `event021_parent_promote_ordinary_successor` path binds only `random_civil_war_history_predecessor`, performs `white_peace`, and then annexes without its own earlier roster preparation.
The delivered successor contract requires preparation before white peace or annexation while the predecessor's host roles, counters, and front receipts are intact.

Minimal patch in `common\scripted_effects\021_random_civil_war_parent_effects.txt`: within `event021_parent_promote_ordinary_successor`, bind the same explicit predecessor under `event021_history_predecessor` as well as the achievement-history target, then call `event021_prepare_successor_roster_adoption` after same-crisis successor proof and before the first destructive war/annex effect.
In `common\on_actions\021_random_civil_war_cxt_on_actions.txt`, provide the same idempotent preparation through the documented `on_civil_war_end_before_annexation` boundary for natural civil-war victory.
Keep the existing `on_annex` transfer/adoption sequence and stale-context guards.
Do not clear predecessor rows before `event021_handle_annexed_country` consumes them.

Acceptance: scripted settlement and natural victory each preserve the surviving ordinary and Event 006 front roster, exclude the successor from its own opposition, transfer once, reject a different-crisis actor, and close cleanly when no opponents remain.
This correction is not a war-transfer certificate; actual war continuity is separately queued in G05.

### G03 — (a) Implement: reconcile release and asset status without promoting placeholders

The current initializer still clears `random_civil_war_rework_ready`.
Preserve that closed gate and the absent default-enable entry until every release-critical item below is resolved.
The overview and acceptance document correctly lead with incomplete status but retain older prose asserting no actionable source defect, no portrait placeholder, or only certification remaining.
The latest inherited-asset evidence contradicts those blanket assertions.

Minimal documentation patch for the parent: reconcile `docs\events\021_random_civil_war\overview.md`, `acceptance_evidence.md`, and `docs\plans\021_random_civil_war_plans\active_repair_ledger_2026-09-02.md` against the current source and the six-row portrait handoff.
Label old certificates by their source/asset revision and mark helper integration present but not certified.
Correct the current severity description explicitly: `event021_parent_select_severity` delegates directly to `event021_prepare_opening_severity`, whose inspected current body assigns Limited/Serious/Severe/Critical through sequential conditions and forces the one-state case to Limited.
It does not execute the four-entry weighted draw claimed by older documentation.
The parent must reconcile that source/accepted-addendum discrepancy before treating historical normalized SEV results as evidence for current behavior.
Keep workbook Event 021 `To Be Reworked` and SCN-018 `Needs Testing`; change workbook facts only through its owner and required exporter.

The portrait handoff reports four live grounded named-person repaints, not harmless institutional placeholders: Wilhelm Marx, Gustav-Adolf von Zangen, Heinrich Held, and Friedrich Dollmann.
Their consumer is `common\scripted_effects\006_independence_wave_rhineland_bavaria_effects.txt`, with the four sprite rows in `interface\006_independence_wave_portraits_registry.gfx` and Matthes/Rupprecht rows in `interface\006_independence_wave.gfx`.
The two latter rows remain blocked for promotion because source-placeholder authority and the selected external processed chain are not reconciled; Rupprecht also has a recorded rights-basis conflict.
All six remain non-final for this gate.

Required asset resolution belongs to the existing portrait owner and parent, using valid source/mode authority and user-supplied styled finals where required.
No safe art replacement is selected by this review.
Do not rename a generated named person into an institution, relabel an external output `styled_final`, quietly remove admitted packages, or accept correct DDS headers as provenance approval.
Those missing inputs remain blockers, not an approved fallback.

### G04 — (b) Queue evidence-only: treaty, settlement, reconstruction, and recurrence

Current parent call sites include `event021_treaty_prepare_signatory_obligations` and `event021_treaty_capture_settlement` in `event021_parent_apply_settlement`, outcome-proof calls, proof freezing, agreement review, recurrence marking, and annex rebinding.
`random_civil_war` achievement readiness now delegates to `event021_treaty_terms_hold_valid` in `common\scripted_triggers\021_random_civil_war_triggers.txt`.
The earlier unintegrated-helper handoff is therefore not a current missing-call finding.

Certify the actual order across `021_random_civil_war_parent_effects.txt`, `021_random_civil_war_treaty_effects.txt`, `021_random_civil_war_treaty_triggers.txt`, and `event021_cleanup_decision_state`.
Required cases: host plus two signatories with different real obligations; one AI signatory missing proof; unrelated front/sponsor exclusion; same-tag agreement; proof frozen before cleanup; one signatory breaching or recurring before the shared hold date; recurrence after the hold date; valid succession and conflicting successor; repeated review; and a second crisis after narrow reset.
No caller-only flag may satisfy another signatory's obligation or award The Terms Hold.
Reconstruction must finish without losing durable treaty/history/package state.
Recurrence must obey grace, earliest/latest dates, generation/cap refusal, and cleanup, while durable negotiated peace remains achievable.
No extra settlement type, public meter, or perpetual maintenance action is requested.

### G05 — (b) Queue evidence-only: actual successor war continuity

The successor helper explicitly owns roster adoption, not war transfer.
The reviewed parent/lifecycle source has no demonstrated complete predecessor-enemy snapshot and verified war-handoff result.
An external-war-at-opening flag, rebound front row, or `transfer_troops = yes` cannot prove ongoing hostility.

Required fixture: predecessor H, ordinary successor S, two unresolved internal actors including an Event 006 actor, and one external enemy.
Capture actual hostile relations before destruction and compare them after scripted promotion and natural victory with `has_war_with` checks, alongside front/host bindings.
Also test an already-settled front, a dead enemy, and a different crisis so the fixture cannot pass by starting unrelated wars.
If engine behavior does not preserve a required relation, the parent must add only the documented, explicit war handoff for that relation at the existing succession boundary and rerun the same fixture.
Do not blindly declare new wars or join every faction war to compensate for missing proof.

### G06 — (b) Queue evidence-only: bounded scheduling and target/route/severity safety

Retain `event021_parent_global_scheduler_pulse`, the global-host/same-date guard, registered-country cursors, bounded Critical queue, and existing release/committed-campaign maintenance boundary.
Prove one pulse owner, no duplicate same-date work, cursor wrap/removal fairness, a capacity-blocked Critical row allowing later rows to progress, and Evolution III disablement draining launch state without abandoning committed-crisis cleanup.
Record actual work bounds and queue liveness, not merely the presence of a loop limit.

Use the existing TGT/ARC/SEV/EVO/STR/REC/GLB cases and source-bound probability manifests.
Preserve exact exclusions for actual nonhumans, incompatible crises, creation/successor locks, incomplete/duplicate Event 006 packages, invalid capitals/remnants, occupied third-party states, and capacity failures.
Check player/AI parity, reduced major targeting, same-tag safety, weighted-ticket quantization, route receipts, per-front uniqueness, and fail-closed rollback.
A correct six-route or four-severity inner pool is not proof of the outer target/viability gates or actual global event probability.
In particular, current severity dispatch is deterministic in the inspected source, while the historical accepted P0.2 addendum calls for weighted severity.
Queue source-to-manifest reachability and parent design-disposition evidence for that discrepancy; do not silently certify the old pool or choose replacement balance weights in this gate.
If the weighted contract remains accepted, restoring its existing four-band selector belongs to the parent implementation repair, with baseline and same-scenario comparison, rather than a new expansion plan.
Nine provisional tuning groups and final target/sponsor changes require owner-approved targets and matching comparison evidence; this planner chooses no balance numbers.

### G07 — (b) Queue evidence-only: Event 006 package reuse and visual crosswalk

Use the existing 32 admitted IDs, not the larger adapter-only registry, as the completion denominator.
The inherited crosswalk is explicitly partial: 46 portrait sprite rows are not 46 accepted characters, ten admitted packages lack a complete mod portrait-row mapping, and flag/cosmetic and specialized consumer coverage remains incomplete.
The 40 Event 021-owned texture references and limited inherited focus/idea icon reviews cannot certify the entire reused package set.

For every reachable consumer, join package/route, exact character or sprite consumer, original source and authority, processed file, runtime DDS/hash, individual visual review, and final/pending status.
Carry the alpha-edge repair and native-alpha fallback history forward, including the exact promoted runtime hashes.
Finish required source/native/enlarged/decoded reviews and consumer checks without deleting provenance or treating contact-sheet existence as acceptance.
Keep the asset workspace while release is blocked.

The package matrix must prove safe identity/character ownership, initialization idempotence, opening forces, local decisions and AI, focus loading and one-time rewards, formation/formables, former-host outcomes, post-cleanup play, and nested eligibility after grace.
Snapshot Event 006 lifecycle state before/after each representative transaction and reconcile all admitted packages' content readiness.
No missing package may silently fall back to a generic tree, portrait, flag, or empty tag.

### G08 — (b) Queue evidence-only: SCN-018 and shared Wars integration

Preserve `SCN-018`, The Fracture Cascade, and `constant:triggerable_scenario_id.random_civil_war`.
Current shared scenario localisation/dispatch references use that constant; the prior proposal to reserve SCN-014 is historical, not a new ID request.
Certify registry initialization/rebuild/filter/selection, displayed ID/name, four types, four intensities, launch-button/effect gate equivalence, confirmation, and final receipt reconciliation together.
Use frozen eligible pools of 1, 2, 3, 7, 10, 11, and 100 to test rounding, no replacement, requested/committed/skipped accounting, and exact failure reasons.
Maximum must freeze all eligible normal humans at confirmation, exclude actors created during that run, preserve absolute actor/map safety, clear bypass/locks, leave `world_end` untouched, and disqualify achievements.
Immediate setup remains required because no measured one-frame failure authorizes the seven-day batching contingency.

Preserve Wars row 1003, Cluster 1, Medium severity, and Events 004/007/021 as distinct members.
Run CLU-01 through CLU-05 for low-chaos separation of all aggressor/target roles, narrowly allowed Rising Chaos overlap, newly created/recent Fury exclusion, package/tag/anchor reservation collision, delayed stale reservations, exact skipped-row reasons, and one global pacing update.
Confirm Event 021 is absent from the obsolete Domestic Unrest membership and that shared individual-crisis pressure is consumed consistently rather than bypassed.
No cluster rewrite or second random-war system is requested.

### G09 — (b) Queue evidence-only: final specialist, MCP, presentation, and performance proof

Refresh only the affected certificates against final file hashes after parent corrections.
Required owners remain the probability, decision/mission, country-package, focus where loading is affected, localisation, asset/portrait, documentation/workbook, and completion auditors.
Do not claim that a current direct-event revision hashes every helper or inherited asset.
Final evidence must cover concurrent theaters, capital/depot/rail objective identity, annex/settlement recurrence sequences, scenario load, late high-country-count scheduling, and multiplayer-relevant deterministic receipts.
Live game and consumer evidence remains user-owned; this handoff neither performs it nor directs an agent to launch HOI4.

### G10 — (c) Reject: scope expansion and proof substitutes

Reject a dedicated Event 021 GUI, public Fracture Pressure meter, animation, super-event, 3D package, technology/doctrine branch, generic claimant focus tree, broad Event 006 rewrite, extra country/portrait family, new settlement system, or second scheduler.
They do not resolve the demonstrated access, lifecycle, provenance, or certification gaps.
Reject unrestricted recurring world scans, duplicate Event 006 lifecycle firing, silent package removal, unmeasured delayed scenario batching, and treating source-only reasoning as engine evidence.
Keep the accepted standard static decision category, one visible State Authority value, separate civilian relief and military aid, bounded strange incidents, and existing six achievements.

## MCP evidence boundary

Fresh Event 021 trace: `EVENT_INSPECTED_PARTIAL`, focused mode, revision `be06dbd18a1cbdfd71a4575935079960cc7d7dfd05af41c7bfbc620aaa538fd9`, graph hash `4dc33d125e067b05cedc9a5c6e77da78d012a55c4a75c2d2781970c9fb04a496`.
The source inventory reports 368 event/on-action paths and zero expanded helpers; validation is false because helper/lifecycle projections are deferred.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ce13ccfa435e5a1fc81152eba77d67a9075d53b4b49b3b1b2a66bf21d98ad534/f0a75ea400ad7be1b089c031b7a152423ecded0f61d1a892b0f78109541d8b78/event-trace-be06dbd18a1c.json`.

Fresh read-only options render for `chaosx.nr21.3`: `EVENT_RENDERED_PARTIAL` at the same revision, layout hash `65ca522a6561e620620510767d112d7d310fd586ac60c58cb064b626bc42ff5e`.
Its inspected JSON has `complete=false` and exactly the event, its option, and terminal nodes.
This is a graph, not report-card visual acceptance or treaty/successor proof.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1ce0f05f90bebeb75a2ca727e7d76c4e448a6a54da3b71773196aed198b52402/5a38825f2cbf2e753c7a046188ccb441e5201e132af2d7f90617962237ace84a/event-options-be06dbd18a1c.json`.

Probability began with `hoi4.probability_inspect` on `events\021_random_civil_war.txt`, source hash `cbe0edbc76d13d701b130733dddcfb5d50271749e6d896e9c3b7544d893c96a8`.
That was source discovery, not scenario evaluation.
The read-only final review was routed to `chaosx_ai_probability_auditor` with `fork_context=false`; its final result returned after the user's bounded-stop instruction.
Its verdict is closed/incomplete, with no files changed and no new evaluate, sweep, compare, or probability-render artifacts.
It confirms that target and recurrence diagnostics are scores, sponsor values are willingness scores, the final target comparison and full timing/route/severity comparison sets remain incomplete, and direct sponsor PP/CP/surrender resource cases remain unresolved.
It also identified the deterministic current severity dispatch, which the planner checked directly against the two source helpers named above.
Its retained Stable/Weak target values 122/916 and REC values 0/100/0/55/60/0 are historical diagnostic evidence, not a fresh final-source global selection certificate.
No new probability certificate or comparison is claimed.

Historical exact blockers remain recorded in the active ledger and acceptance evidence: helper-expanded Event analysis `INTERNAL_ERROR`/180-second timeout/transport closure, revision comparison `EVENT_REVISION_NOT_CACHED`, and report-artifact comparison `EVENT_GRAPH_ARTIFACT_INVALID`.
Do not erase successful narrower historical probability evaluations, but do not promote them to a final all-family certificate either.
The September 2 sponsor-resource comparison still records unresolved PP/CP/surrender inputs and a confounded support case; these are not exact real-state zero proofs.

Fresh matching focus, shared GUI, and map inspect/render cycles were not completed before the user requested this review stop.
Their current conclusions remain unresolved, rather than being replaced with source-only certification or an assertion that the tools are unavailable.
Retained evidence includes the older 184-focus tree inspection, state/adjacency/supply/rail inspection, and shared Event Details multi-state renders; the September 2 inherited-asset handoff reports later focus/render timeouts without artifacts.
Shared checked/unchecked controls were previously dispositioned as mutually exclusive; that is not authority to dismiss a new visible clipping or click-region defect.
Any defect in Event Details or scenario/settings layout belongs to the shared owner, not an Event 021 UI worker.

Event and Technology Tree Viewers are read-only.
The installed package has no standalone Technology Tree Viewer workflow; available technology MCP tools are a separate capability.
No technology/doctrine graph is changed or certified here, so this limitation does not justify adding one.
No rewrite tool was used.

## Research basis and scope restraint

The accepted research notes already link organized governmental/territorial claims, state capacity, exclusion and mobilization, cross-border armed networks, external sponsorship, fragmented bargaining, and credible postwar guarantees to the existing mechanics.
Those connections support distinct regional/command fronts, named capital and transport objectives, separate civilian protection, recipient-bound aid, all-signatory obligations, and conditional recurrence.
This gate makes no new historical attribution and does not revalidate the research notes' external empirical claims.
Package-specific institutions, leaders, symbols, and territorial claims remain Event 006 research responsibilities.
Fictional strange incidents remain uncertain inspiration, not claims about real communities.

## Parent closure checklist

- [ ] Resolve G01 local-content consumers without altering Event 006 lifecycle ownership.
- [ ] Resolve G02 preparation timing and G05 actual war continuity on both successor paths.
- [ ] Certify G04 all-signatory proof, cleanup, second-crisis reset, reconstruction, and recurrence.
- [ ] Complete G06 final target/timing/sponsor comparisons and bounded scheduler fixtures.
- [ ] Resolve G03's six blocked portrait rows and G07's complete admitted-package consumer/provenance matrix without placeholders or silent substitutions.
- [ ] Certify G08 SCN-018 and Wars transactions, including immediate Maximum load evidence and exact failure accounting.
- [ ] Finish G09 current-revision specialist/MCP/presentation/performance evidence and reconcile all old assertions, asset handoffs, and workbook status.
- [ ] Record each prior accepted obligation as implemented and proven, explicitly rejected with authority, or still queued with its release consequence.
- [ ] Only when no blocker, unapproved fallback, placeholder, or unresolved accepted obligation remains, open the existing release/default-enable gates and allow the parent completion review.

Files changed by this planner: `docs\plans\021_random_civil_war_plans\late_stage_release_gate_handoff_2026-09-02.md` only.
Keep this file in `docs\plans`; do not promote it wholesale into `docs\specs`, because it introduces no expansion design.
If the parent accepts a necessary contract clarification, fold only that clarification into the existing numbered spec and its compiled copy, preserving one design source of truth.

Skills used: improvement-loop, event-planning, events, decisions-missions, event-assets, and subagents.
They enforce the design stop, strict evidence/provenance status, bounded ownership, and probability-auditor route; no skill was changed.
No implementation simplification was introduced by this planner.
The bounded inspection and outstanding proof are explicit limitations, and Event 021 is not declared complete.
