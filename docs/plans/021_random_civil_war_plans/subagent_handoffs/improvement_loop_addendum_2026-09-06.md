# Event 021 bounded improvement-loop addendum — 2026-09-06

Status: planning handoff delivered; Event 021 acceptance remains incomplete.
Recommendation: stop broad expansion, reconcile the concrete source/design conflicts below, and finish the existing acceptance work.
This is not a clean closure certificate, permission to open the release gate, or an implementation-completion claim.
The user requested finalization without waiting for additional evidence; unreturned inspection work is recorded as unresolved rather than allowed to hold this handoff open.

## Ownership and disposition rules

Only this addendum is authored by this planning pass.
The parent owns source changes, acceptance decisions, shared-owner coordination, final integration, and the completion review.
No gameplay, localisation, workbook, asset, GUI, runtime configuration, or prior handoff is changed here.
All paths below are relative to `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux` unless explicitly absolute.

`unresolved` means that approval, implementation correctness, or required evidence is missing or conflicting.
`accepted-and-queued` is used only for an existing obligation supported by the parent repair ledger or completion audit, with the reason for the queue stated below.
It does not mean that the obligation can be omitted from full acceptance.
`not required` means that no additional Event 021 implementation is justified by the reviewed requirement and evidence; it does not discharge another event's separate obligation.
Proposed repairs in this document remain unresolved pending parent review, not accepted merely because this file exists.

The prior `improvement_loop_addendum.md` carries an implementation-resolution ledger, while `post_fix_improvement_loop_closure_addendum_2026-08-31.md` queues certification rather than requesting more mechanics.
The September 2 `active_repair_ledger_2026-09-02.md`, `late_stage_release_gate_handoff_2026-09-02.md`, and `subagent_handoffs\event_completion_parent_audit_2026-09-02.md` explicitly retain incomplete acceptance.
This addendum consolidates those obligations and identifies current contradictions; it does not create a second design layer for the same unresolved gap.
Prior probability, package, lifecycle, visual, and approval obligations remain unresolved or queued as described below.

## Review basis and depth verdict

The review used the complete `docs\specs\021_random_civil_war_specs\` package, including its ten parts, assembled master, prompts, country matrix, probability matrix, research, reconciliation, role review, manifests, and subordinate handoff instructions.
Current Event 021 source, helper documentation, `docs\events\021_random_civil_war\`, and the repair/completion/asset/probability handoffs were reviewed against those requirements.
The requested event surface is actually `events\021_random_civil_war.txt`; there is no corresponding `common\events` directory to certify or repair.
Evidence is bounded source review plus the specific read-only MCP results below, not an exhaustive engine execution certificate.

The existing design is sufficiently deep: six opening archetypes, evidence-backed pressure, visible authority, connected theater preparation, ordinary and Event 006 adapters, same-tag contests, independently recorded fronts, three evolutions, separate relief and armed support, sponsor commitments, settlement obligations, reconstruction, recurrence, Wars-cluster coordination, and SCN-018 already provide substantial interaction.
Broad idea carriers and reused focus content are not inherently shallow when the underlying decisions, state receipts, and package routes carry the distinctions.
There is no present justification for another meter, route family, country package, parallel scheduler, generic claimant focus tree, dedicated Event 021 GUI, super-event, animation family, technology tree, or 3D package.

The important remaining gaps are disconnected or uncertified consumers, not a shortage of containers.
Most importantly, current Event 006 local-content gates contradict the claimed origin-neutral access repair, sponsor receipt preparation contains scoped temporary-variable writes, and successor registry continuity has not established actual war continuity.
Repeated pressure/authority rewards alone do not justify replacing existing actions: for example, communications protection and regional-administration review share relief behavior but have different resource contracts.
Require the existing decision audit to establish their distinct availability and usefulness; do not invent an additional subsystem or remove either action merely to make their effect blocks look different.

### Research and regional basis

The research basis remains `021_random_civil_war_research_notes.md`, the country-package matrix, and parts 2–8 of the existing spec, rather than a new historical expansion.
Their civil-conflict research supports keeping competing actor claims, external sponsorship, multi-party settlement obligations, and recurrence causally connected.
Civilian relief must remain distinct from armed sponsorship, with no claim that refugees inherently cause violence.
Existing regional package identity, former-host relationships, local institutions, and package-specific political paths supply the regional depth; the RHI/BAY findings below concern the provenance and consumers of already selected identities, not proposals for additional historical leaders.
No new historical attribution, territorial entitlement, political faction, or scientific mechanism is asserted by this addendum.
Required syntax references were the offline Paradox snapshot and installed vanilla documentation, including the separate civil-war, annexation, war-joining, scope, event-target, and constant contracts.
The vanilla Spain civil-war precedent establishes an explicit state/capital opening pattern, not permission to substitute a blanket half-country split or assume annexation transfers every war.

## Acceptance disposition map

| ID | Surface and status | Bounded action | Completion boundary |
| --- | --- | --- | --- |
| B01 | Event 006 local-content access: **unresolved** source/design conflict | Reconcile the current strict predicate with the promised origin-neutral local package content; repair only approved local consumers if that promise remains authoritative. | Must be reconciled before full acceptance; not a testing-only omission. |
| B02 | Sponsor receipt preparation: **unresolved** narrow correctness issue | Review and correct the scoped temporary-variable assignments and prove the selected recipient/front pair across the existing support paths. | Required parent source disposition and, if confirmed, repair before completion. |
| B03 | Shared fixed-target helper: **unresolved** shared contract; direct Event 021 call **not required** | Obtain the shared owner's actual contract and an explicit dependency disposition; do not invent or alias an API. | Cannot silently waive the dependency; other-event implementation may remain queued only with an explicit authorized scope decision. |
| B04 | Event 006 visuals/provenance: **unresolved** | Finish the existing 32-package consumer crosswalk and resolve pending portrait/source authority. | Missing assets or provenance are not replaced by a testing label; required for full package acceptance. |
| B05 | Probability certification: **accepted-and-queued**, with unresolved inputs/baselines; incident lifecycle: **unresolved** | Finish the existing named matrix and same-scenario comparisons against frozen current source; disposition the auditor's incident-expiry concern. | Certification may remain queued while Needs Testing; any confirmed lifecycle defect requires repair before completion. |
| B06 | Severity contract and nine inferred tuning groups: **unresolved** | Record parent acceptance or a bounded owner correction; align the retained spec and audit claims. | Approval and any resulting source changes precede completion. |
| B07 | Successor/treaty/lifecycle continuity: **accepted-and-queued** evidence obligation | Preserve integrated hooks; prove natural and scripted succession, surviving wars, exact signatories, and durable proof. | Queue testing without speculative war rewrites; any demonstrated break requires a bounded fix before completion. |
| B08 | Current event/focus/map/GUI MCP and runtime matrix: **accepted-and-queued**, affected conclusions **unresolved** | Record exact partial/timeout boundaries and obtain missing evidence through the existing owners. | No source-only substitution or completion claim. |
| B09 | Standalone Technology Tree Viewer: **unresolved package gap**; Event 021 technology expansion **not required** | Retain the verified package-local absence separately from exposed technology routes and service health. | Not an Event 021 gameplay implementation requirement. |
| B10 | Final audits, localisation/docs/catalog reconciliation: **accepted-and-queued** | Refresh the existing evidence and obtain missing final specialist reviews after the last owner patch. | May remain queued during testing; required before full acceptance. |
| B11 | Additional mechanics/assets and legacy-art deletion: **not required** | Preserve the bounded design and documented unused provenance files. | No expansion or destructive cleanup prerequisite. |

## B01 — Reconcile origin-neutral package access before accepting package completeness

Evidence paths:

- `docs\specs\021_random_civil_war_specs\021_random_civil_war_spec_part_7_event_006_country_packages_and_focus_handling.md` and `021_random_civil_war_country_package_matrix.md` promise complete admitted package content without importing the Event 006 lifecycle.
- `docs\plans\021_random_civil_war_plans\active_repair_ledger_2026-09-02.md` and `subagent_handoffs\event_completion_parent_audit_2026-09-02.md` state that local focus, category, and aggregate-decision gates were made origin-neutral.
- Current `common\scripted_triggers\006_independence_wave_triggers.txt` defines `is_independence_wave_event021_package_country` with completed adapter receipts and no Event 006 origin, but `is_independence_wave_event6_local_content_active` still requires `is_independence_wave_active_country`.
- The same file's `is_independence_wave_event6_player_surface_allowed` explicitly excludes completed Event 021 adapter receipts.
- `common\national_focus\006_independence_wave_focus.txt`, tree `independence_wave_focus_tree`, uses the strict local-content predicate in its country selector; `common\decisions\006_independence_wave_decisions.txt` also uses it in local action/cancellation gates.

This proves a current predicate/documentation contradiction, not a rendered proof that every manually loaded focus is inaccessible.
Do not attribute the conflict to a particular author or infer that a later user decision authorized it.
The parent must first establish whether an explicit newer decision intentionally restricts Event 006-origin surfaces.
If it does, record that decision and reconcile the Event 021 package promise; an old “resolved” heading is not approval to overwrite the restriction.

If complete origin-neutral local content remains accepted, proposed owner files are `common\scripted_triggers\006_independence_wave_triggers.txt`, the existing local consumers in `common\decisions\006_independence_wave_decisions.txt` and their current category files under `common\decisions\categories\`, and the existing focus selector only where necessary.
Use the already defined proven-package predicate rather than a new lifecycle flag or a duplicate focus tree.
Keep `is_independence_wave_active_country` and Event 006 network, league, congress, generation, fired-count, evolution, adapter-only, and public Event 006 history surfaces strict.
Do not blanket-replace every occurrence of the player-surface gate.

Acceptance cases are an ordinary Event 006 package, a completed Event 021-origin package, an adapter-preparing country, an incomplete/failed adapter, and a completed Event 021 package after reconstruction.
For each admitted package, show the intended local focus/decision/formable consumers, correct cancellation behavior, preserved meaningful focus handling, and no Event 006 origin/count/evolution/network publication.
The current focus MCP attempt timed out, so rendered reachability remains unresolved and the parent retains final implementation review.

## B02 — Finish the existing sponsor transaction, without adding a sponsor system

Current `common\scripted_effects\021_random_civil_war_decision_effects.txt`, `event021_prepare_exposure_sponsor_commitment`, assigns temporary inputs through `ROOT.event021_recipient_id` and `ROOT.event021_front_id` inside the exposure-target scope.
Repository scope rules explicitly prohibit scoping temporary variables.
The downstream `event021_record_sponsor_commitment` in `common\scripted_effects\021_random_civil_war_evidence_effects.txt` expects the unscoped inputs.
However, `event021_record_received_sponsor_commitment` later writes normal sponsor/recipient/front receipts on the actual receiving side and ROOT, so this observation does not prove that all final receipts are absent.

Proposed owner files are those two effect files and their existing helper documentation where the contract is documented.
Exact identifiers are `event021_prepare_exposure_sponsor_commitment`, `event021_record_sponsor_commitment`, `event021_record_received_sponsor_commitment`, `event021_apply_government_support_to_exposure_target`, and `event021_apply_opposition_support_to_exposure_target`.
Keep the existing support decisions, costs, cooldowns, and balance targets.
Resolve one actual receiving country and its matching front; initialize the transaction's temporary inputs, use unscoped temporary assignments, and reject invalid recipient context before recording a misleading commitment.
Do not let a previous helper invocation supply a stale recipient/front value.

Required cases: exposure anchored on government or opposition, support for either side, missing/dead recipient, a changed front, and repeated invocation in one effect chain.
The sponsor and recipient must agree on recipient ID, front ID, amount, and expiry; no invalid target may receive equipment or a completed receipt.
Any change to the guards used by AI scores also requires the same-scenario SPN comparison through `chaosx_ai_probability_auditor`.
This is a bounded correctness proposal pending parent review, not a new accepted balance requirement.

## B03 — Fixed-target shared helper: no invented contract

Evidence is `common\scripted_effects\individual_crisis_targeting_effects.md`, the corresponding effect/trigger sources, `subagent_handoffs\individual_crisis_dependency_restore_2026-09-02.md`, and `subagent_handoffs\scenario_ticket_count_ordering_repair_2026-09-06.md`.
`apply_individual_crisis_fixed_target_event_pressure` is named in shared documentation but remains undeclared and unconsumed in the reviewed source.
The documentation does not provide its inputs, output variable, or caller transaction.
No argument list, return value, timing model, probability formula, alias, or replacement identifier is specified here.

The shared documentation names fixed-target owners for Holy Realm/Tibet, Soviet Collapse, the Secret Alliance headline, Natural Disasters, Resources Found, and Video Game/Sweden.
That does not make Event 021 a fixed-target owner.
Event 021 uses the existing candidate-ticket helper `adjust_individual_crisis_candidate_ticket_weight` for its bounded selection pools.
The September 6 repair already moves `global.random_civil_war_scenario_eligible_count` behind the positive adjusted-ticket check in `event021_parent_add_scenario_target_to_weighted_pool`; do not reopen that implemented repair or alias it to the missing helper.

Proposed first change is documentation-only owner disposition in `common\scripted_effects\individual_crisis_targeting_effects.md` and the Event 021 active repair/acceptance ledger.
After the shared owner defines an accepted contract, the parent can name the actual implementation and fixed-owner call sites in a bounded implementation assignment.
The September 2 parent audit treats this as a release dependency, so the planner cannot silently downgrade it to not required.
It may remain accepted-and-queued outside Event 021 only if the parent records an authorized boundary decision, owner, reason, and the effect on the Event 021 completion claim.
Until then, its classification is unresolved; adding a direct Event 021 call is not required.

## B04 — Complete existing Event 006 visual and provenance obligations

Evidence paths are `subagent_handoffs\event006_reused_asset_crosswalk_2026-09-02.md` and `.json`, `subagent_handoffs\reused_rhi_bay_portraits_2026-09-02.md`, `docs\events\021_random_civil_war\reused_asset_individual_review.md`, and `docs\assets\021_random_civil_war\validation\reused_rhi_bay_portraits_2026-09-02\crosswalk.md`.
The denominator is 32 admitted Event 021 packages, not all 40 runtime adapters or the broader Event 006 catalog.
The retained crosswalk reports 46 portrait registration rows and ten admitted packages without a current mod portrait row; absence of a mod row is an unresolved consumer mapping, not automatic permission to generate ten replacement portraits.
Flag/cosmetic identities, specialized decision/idea/focus/formable families, and package-specific consumer renders remain incompletely reconciled.

The six reviewed RHI/BAY character consumers are `RHI_provisional_directorate`, `RHI_river_commandant`, `RHI_josef_friedrich_matthes`, `BAY_state_council`, `BAY_mountain_commandant`, and `BAY_rupprecht_of_bavaria`.
Their current evidence is provisional or blocked for grounded-source/repaint/mode authority; the Rupprecht source additionally has unresolved rights metadata.
Valid DDS dimensions and pixels do not establish final portrait or provenance approval.
Exact runtime consumers are in `common\scripted_effects\006_independence_wave_rhineland_bavaria_saar_package_effects.txt`, with registrations in `interface\006_independence_wave_portraits_registry.gfx` and `interface\006_independence_wave.gfx`.
The shorter Rhineland/Bavaria filename appearing in older prose is not the current consumer filename.

First proposed updates belong in the existing crosswalk and `docs\events\021_random_civil_war\owned_asset_crosswalk.md` / `reused_asset_individual_review.md`, naming every actual consumer and its source/final status.
Route any required portrait production or user-final installation through `chaosx_portrait_creator`; no planner portrait generation, silent relabeling, package removal, or RunPod operation is authorized.
Only after source/mode/rights and parent authority are resolved should that owner update the exact existing DDS/GFX/character consumer paths identified by the crosswalk.
Do not register a replacement asset family merely to avoid unresolved provenance.

The 40 Event 021-owned runtime textures already have their own review; that is not coverage of the inherited packages.
The thirteen shared focus-icon and eight idea-icon reviews remain usable for those exact pixels but are not a rendered tree or full package certificate.
The owned alpha repairs recorded in `docs\assets\021_random_civil_war\validation\alpha_edge_repair_2026-09-02\parent_promotion_v2.json` should not be redone absent a current defect.
Keep the disclosed alpha/chroma fallback history explicit; do not claim that no fallback ever occurred.
The fifteen unreferenced legacy achievement DDS files are documented provenance, not a required deletion or a missing active asset family.

## B05–B06 — Finish probability certification and resolve balance authority

The authoritative scenario inventory is `docs\specs\021_random_civil_war_specs\021_random_civil_war_probability_scenario_matrix.md`.
Evidence owners are `chaosx_ai_probability_auditor` and the parent implementation owner, not this planner.
This pass began weighted inspection with `hoi4.probability_inspect` and routed a read-only audit to `chaosx_ai_probability_auditor` (`01a0762b-9fb4-7943-bcf8-48610e269f2c`).
The specialist returned its final read-only handoff during document finalization: status not certified, no files written, and no new simulation or sequence analysis.
Its fresh helper/sponsor inspections produced no structured response within bounded waits and were terminated; no new current-repair MCP revision, scenario hash, or comparison artifact was produced.
The handoff confirms the implemented September 6 ticket-count ordering and the separately frozen Maximum pool without claiming either is probability-certified.

The parent must retain current full candidate membership, hard-zero reasons, source hashes, scenario bodies, acceptance bands, and the actual saved-before bodies for each comparison.
Existing target projection evidence is not a complete live country pool, and a source-only inspect is not a declared pool.
Historical evaluate results, deterministic parent reviews, diagnostic subpools, and seeded projections should remain labeled as such.
Do not reinterpret an unavailable old artifact as a pass or compare identical after-source snapshots while calling one the baseline.

Required bounded work covers the named target/archetype/severity, evolution timing, force/front, sponsor/AI decision and mission, settlement, recurrence, global queue, cluster, and scenario families already in the matrix.
Use existing `probability_*` routes for evaluation, applicable sweeps/seeded simulation/sequence analysis, and mandatory same-scenario comparison after owner changes.
The specialist identifies `TGT-01` through `TGT-10`, `ARC-01` through `ARC-08`, `SEV-01` through `SEV-06`, `EVO1-01/02`, `EVO2-01/02`, `EVO3-01/02`, `STR-01` through `STR-05`, `SPN-01` through `SPN-05` plus resource edges, `SET-01` through `SET-06`, `REC-01` through `REC-06`, `GLB-01` through `GLB-07`, and `CLU-01` through `CLU-05` as the existing family boundaries.
For the September 6 repair specifically, rerun `SCN-01` through `SCN-04` and `SCN-07`, cross-checked against the TGT family.
Do not treat decision raw scores as normalized action probabilities or a `no_weighted_surfaces` strategy-discovery result as proof that AI strategy source is absent.
Settlement, queue, and cluster behavior may use deterministic lifecycle/sequence tests only after the intended deterministic contract is explicitly accepted; do not invent normalized probability claims for them.
The current SCN ordering repair needs a fresh comparison with mixed capped and uncapped countries, zero tickets, uniqueness and requested/committed/skipped accounting, plus the separately frozen Maximum pool.
SCN-018 remains the implemented scenario identifier; an earlier suggested scenario number is not grounds for renumbering.
Immediate Maximum setup remains the accepted implementation absent measured evidence and authorization for the specified bounded delay; no seven-day fallback is proposed.

Retain the SPN-01 through SPN-05 resource-guard evidence in `subagent_handoffs\probability_sponsor_resource_guards_2026-09-02.md`.
Its partial comparison does not resolve direct political-power, command-power, surrender, or every convoy-isolation input.
The target baseline and current projection handoffs likewise do not certify the entire live registry.
Proposed evidence updates belong in `docs\events\021_random_civil_war\acceptance_evidence.md` and the existing family handoffs/snapshots, not another probability design document.

The specialist additionally reports that `event021_parent_roll_strange_incident` sets `random_civil_war_strange_incident_recent` and `random_civil_war_strange_incident_until` without finding a corresponding clear/read lifecycle in its current Event 021 search.
Treat this as an unresolved source concern requiring owner review, not as a proven permanent in-game suppression bug.
Exact proposed owner surface is the existing incident helper in `common\scripted_effects\021_random_civil_war_parent_effects.txt` and its existing bounded review/cleanup path in the parent or lifecycle effect file.
If confirmed, consume the existing expiry receipt and clear the cooldown in the appropriate bounded review/cleanup path; preserve the accepted cadence and probability targets rather than adding a new incident family or world scan.
Use `STR-01` through `STR-05` to cover first occurrence, active cooldown, expiry, cleanup, and recurrence/re-entry without stale suppression or duplicate rolls.
This narrow source concern is not waived by queuing the larger certification matrix.

Auditor-recorded current raw SHA-256 anchors are `BE9E51F4923F6D5BE3BBFFB548FB3E73FCBA2E859C6E6040C80BFC8A745B4787` for the parent effects, `A26F67E5CEEB80EB5BF26B431C0A51D86A26A0C93B82C77B52044B2D09A19E14` for the decisions, and `B02AE147CE8CE700792C2B9110D0BF34D5C65D1403BA15F685A968D8C1D09EC1` for the constants.
These are local source hashes, not MCP revisions.
The historical sponsor comparison `probability-248f44a08b739e9eaafee94a` remains partial with eight unresolved inputs and subsequent source drift; the historical recurrence comparison `probability-2e2594e85891304baa026a5d` remains limited to its frozen bodies and scenario hash.
The previously requested nonexistent `common\scripted_effects\021_random_civil_war_scenario_effects.txt` is a stale selector blocker, not a reason to create another scenario implementation file; current scenario logic is in the parent effects file.

The current severity selector is a deterministic pressure/viability ladder, while the old addendum describes weighted severity and certifies a four-entry pool.
The primary spec describes bands, and a past weighted fixture is not proof that the current selector is weighted.
Resolve the conflicting claims before selecting a test adapter or changing behavior; do not add randomness solely to conform to an old report.
The parent must explicitly accept the deterministic contract and supersede the weighted claim, or authorize a source correction with an actual baseline and comparison.

`subagent_handoffs\script_constant_completion_2026-09-02.md` lists nine provisional tuning groups: action economy, viability, actor size/severity, secondary allocation, anchor scores, target-ticket conversion, receipt duration/ownership, same-tag contest, and sponsor/incident tuning.
Resolved constant tokens are not balance acceptance.
The owner must confirm or correct each group, referencing `common\script_constants\021_random_civil_war_constants.txt` and the actual consumer in the parent/decision/evidence effects, triggers, MTTH, or AI files.
This planner proposes no new numeric target and no speculative API.

## B07 — Preserve integrated repairs; prove their actual lifecycle consequences

Current `common\scripted_effects\021_random_civil_war_parent_effects.txt` includes `event021_parent_prepare_annex_successor` and `event021_parent_promote_ordinary_successor`, with predecessor targets and successor roster preparation.
`common\on_actions\021_random_civil_war_cxt_on_actions.txt` includes the natural before-annex callback and the on-annex lifecycle/adoption route.
Do not issue another proposal to add hooks that already exist.
The current settlement path calls binding preparation and treaty capture before destructive cleanup, so the original helper-only handoff's unintegrated status is historical, not sufficient evidence of a missing call.

The remaining obligation is actual behavior, not merely copied history.
Use `common\scripted_effects\021_random_civil_war_successor_effects.txt`, `021_random_civil_war_lifecycle_effects.txt`, `021_random_civil_war_treaty_effects.txt`, their matching trigger/docs files, and the two September 2 successor/treaty handoffs as the existing implementation boundary.
Prove a scripted ordinary successor, a natural ordinary claimant victory, a remaining ordinary front, a remaining Event 006 front, and an external enemy.
Before and after the transition, record exact crisis/front identities, live host/actor links, real war relationships, role/receipt preservation, and cleanup ordering.
Reject self, dead, different-crisis, and stale successor pointers; do not grant original-player-government eligibility or duplicate old awards.

For settlements, prove each captured signatory's own front-bound obligation, nonempty agreement membership, freeze-before-cleanup, the shared hold date, breach and recurrence latches, legitimate successor rebinding, and AI/human parity.
One host receipt must not satisfy every signatory or terminate unrelated surviving fronts.
These tests are already accepted-and-queued by the parent ledger because source integration is not execution proof.
If the actual war relationship fails, the parent must implement a bounded pre-annex relationship capture and appropriate explicit transfer/join/verification in the existing successor transaction, after confirming the installed engine contract.
Do not invent a universal war-transfer API, declare unrelated wars speculatively, or treat `transfer_troops = yes` as sufficient proof.

## B08–B09 — MCP and runtime evidence limits at cutoff

All MCP work in this pass was read-only; no rewrite tool was used.
Current successful event/probability calls establish that some routes responded, not that every service route or standalone viewer is available.

| Route and exact scope | Result available at cutoff | Permitted conclusion |
| --- | --- | --- |
| `hoi4.event_inspect`, `chaosx.nr21` trace, both directions, depth 4, 100 nodes, 200 edges, helper expansion requested | `EVENT_INSPECTED_PARTIAL`, `validation.passed = false`; helper/lifecycle coverage deferred | Partial event graph evidence only; workspace-wide issue counts are not automatically Event 021 defects. |
| `hoi4.event_render`, same namespace, overview | `EVENT_RENDERED_PARTIAL`, same source revision; 100 selected nodes, 42,464 omitted; validation false | A graph artifact exists; it is not event-card, category, or complete lifecycle acceptance. |
| `hoi4.probability_inspect`, Event 021 core-effect source, custom weighted-pool adapter | `PROBABILITY_SOURCE_INSPECTED`, source inspection valid, `poolComplete = false`, zero declared candidates | No complete-pool or balance certificate. |
| `hoi4.focus_inspect`, `common/national_focus/006_independence_wave_focus.txt` | `timed out awaiting tools/call after 180s` | Current focus inspection conclusion unresolved. |
| `hoi4.focus_render`, same file | No structured result captured before the user-directed stop | No current rendered-tree conclusion. |
| `hoi4.map_inspect`, state 121, overview disabled | `timed out awaiting tools/call after 180s` | No new state/adjacency/supply proof. |
| `hoi4.map_render`, state layer, supply-node/railway/adjacency overlays, scale 0.2 | `timed out awaiting tools/call after 180s` | No new topology render; one map fixture would not certify every package anyway. |
| `hoi4.gui_inspect`, `events_log_event_details_window`, 1920×1080, scale 1 | No structured result captured before stop | Shared-window conclusion unresolved. |
| `hoi4.gui_render`, same window, normal/long-text/missing-localisation states | `timed out awaiting tools/call after 180s` | No current visual/click-region certificate. |

The initial GUI smoke request used `events_log_details_event_id = 21`; source review shows that real entry selection is array-driven through `global.events_log_open_event_detail_entries`, `events_log_open_event_detail_index`, and the existing open/tab flags.
Consequently, even a successful response to that smoke request would not certify an Event 021-populated fixture.
The parent must bind a source-backed scenario, not copy that unverified fixture input into acceptance evidence.
The earlier checked/unchecked-control overlap was already dispositioned as mutually exclusive states; this pass does not resurrect it as a proven simultaneous-control bug.
The shared Event Details window remains parent/shared-framework owned, not an Event 021 dedicated-UI worker assignment.

The current event source revision is `d845f43c97099a029173014ead16d7eef197a0351971daad8dc5c946aec7fb38`, graph hash `c23d0d5c23467cf6802ff631141a536b7f9b4571dcd929b251bc379392123e10`, and overview layout hash `85b384d4ca3b738daec072bf710849ecab4f44d2077454c1419c60dc617859cd`.
Retain these actual artifacts, without promoting them to a successful current comparison:

- Trace: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4c276c18c15eaa8fa6a105c2cad3e834bf50fa9a6041e4ae001f986bbaddd8b1/326aa6de2c90b29812c3a18e582f08ede822dcd8c49f4b669fcddaeba363f2be/event-trace-d845f43c9709.json`.
- Overview manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3478fec0c1bfe75d2e36ca68b6ada7d43a713aa5750c6c25719d419175fc528b/91dc79543dda3c86fac465ddf3d3af907bb8ff6aa4d4daebb2645a32f05d6ef5/event-overview-d845f43c9709-manifest.json`.
- Probability inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/84c83c48d4d9a5bdccfee6f560e99eba0d3c024656729fee7106f9990a01e474/ad63a2589c956e27210065c7f4a8f84f8655a50e46eab6f1547eb15aac875140/probability-inspect-cd42bdc15c52.json`.

The probability inspection source revision is `2b07f5480cce52f51b0b2c4816568c3e5738bb8e2fd6bad2c148435d0e5536af` and source hash `cd42bdc15c52344d0a754dcd11ba9b95f697d62030d4870cc1f388ef3b20d046`.
These route-specific revisions do not imply an immutable whole-worktree snapshot or certify changes made afterward.
No current matching event before/after comparison was obtained; this remains part of the existing evidence queue.

Standalone Technology Tree Viewer verification was separate: the installed `C:\Users\klimp\AppData\Roaming\npm\hoi4-agent-tools.cmd` resolves into package version 3.0.8 under `C:\Users\klimp\AppData\Local\hoi4-agent-tools\3.0.8\node_modules\hoi4-agent-tools`.
Its package/bin inventory provides stdio, HTTP, and setup entry points; its README and `docs\technology.md` describe read-only technology MCP routes, not a standalone viewer application.
No standalone viewer entry point was found in that installed package.
This is a verified package-local gap, not a claim that no unrelated viewer exists anywhere on the computer.
Technology routes are exposed, but their health was not independently tested here because Event 021 adds no technology/doctrine tree.
Do not invent standalone launch commands or expand Event 021 to exercise an otherwise out-of-scope capability.

The existing runtime queue remains: six opening archetypes, one-state/all-island safety, ordinary inherited-focus handling, all 32 admitted package launches, multifront survival, actual successor wars, treaty/recurrence sequences, Wars collisions, four scenario types by four intensities, cleanup and repeated invocation, and performance budgets.
No game was launched and no user-owned live-consumer evidence was manufactured.
Required MCP routes that timed out or lacked a result remain exact evidence blockers; source checks are not their substitute.

## B10–B11 — Final reconciliation, no new expansion layer

The parent should update the existing `active_repair_ledger_2026-09-02.md`, `source_of_truth_map.md`, `docs\events\021_random_civil_war\overview.md`, and `acceptance_evidence.md` after reviewing this addendum.
Reconcile the origin-neutral gate conflict, severity claims, integrated successor/treaty call sites, outstanding fixed-target dependency, and inherited portrait status.
Retain historical handoffs as dated evidence and explicitly supersede their stale implementation claims instead of treating every earlier “resolved” or “unintegrated” label as current truth.

The September 2 parent/workbook handoff records Event 021 and SCN-018 as Needs Testing; the earlier To Be Reworked wording must not be presented as a fresh workbook observation.
No workbook change is made or certified in this planning pass.
Any later catalog update must use `docs\spreadsheets\chaos_redux_events_catalog.xlsx` and the required exporter; never edit CSV exports directly.
Localisation and event-details/evolution/cluster wording must follow the accepted implemented behavior, not a proposal or implementation-history narrative.

After the last source repair, obtain the missing/current bounded decision-mission, focus/country-package, localisation, probability, and event-completion specialist reviews through the existing routing rules.
The September 2 parent audit explicitly reports unavailable final completion and decision-auditor handoffs; parent source review is not an independent specialist pass.
Keep `random_civil_war_rework_ready` and automatic availability subject to the parent release gate; this planning handoff does not enable them.

No additional asset generation, route, country, formable, event-owned GUI, super-event, animation, doctrine, technology, model, or new global polling loop is proposed.
No accepted package should be silently removed to reduce the validation denominator.
No simplification or missing evidence is approved by this addendum.
Existing documented fallback/provisional assets remain disclosed and unresolved wherever approval is missing.

## Parent handoff and promotion rule

Completed planning work: one dated, bounded addendum identifying current source conflicts, existing acceptance obligations, exact consumer/helper identifiers, evidence paths, and explicit MCP/runtime/provenance limits.
Blocked work: full package acceptance, fixed-target dependency disposition, balance authority/certification, current visual/lifecycle evidence, and final specialist/runtime acceptance remain incomplete.
Uncertainty: whether a newer explicit decision authorizes the strict Event 006 gates; whether later receipt writes fully mask the sponsor temporary-input defect; whether actual engine succession preserves every required war; and whether outstanding source/mode/rights decisions permit final inherited portrait acceptance.

Implementation order is B01/B02 parent review, B03/B06 authority resolution, narrowly accepted owner repairs, then existing probability/consumer/lifecycle evidence and documentation reconciliation.
Testing-only items may remain accepted-and-queued while the event remains Needs Testing, with named owners and missing evidence recorded.
Missing design authority, missing source contracts, unapproved visual substitutes, or confirmed gameplay defects must not be relabeled as testing-only.

Keep this file in `docs\plans\021_random_civil_war_plans\subagent_handoffs\`.
Do not promote the entire addendum as accepted source design.
If the parent accepts a bounded repair, record its explicit acceptance basis and fold only the changed contract into the relevant existing spec part: package access in part 7, sponsor behavior in parts 3/5, shared targeting/severity/AI boundaries in parts 2/8, visual obligations in part 9, and acceptance limits in part 10.
Evidence refreshes belong in the acceptance ledger and handoffs, not duplicated spec layers.
Do not request another broad improvement-loop pass for these same gaps while their dispositions remain open.

Guidance used: `chaos-redux-improvement-loop`, `chaos-redux-event-planning`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-focus-trees`, `chaos-redux-event-assets`, `chaos-redux-scripted-gui`, `chaos-redux-mtth`, and `chaos-redux-subagents`.
Their scope and evidence rules kept this pass to planning, existing consumers, read-only inspection, specialist probability routing, and explicit stop-expansion boundaries.
No skill was created or changed.

The parent should finish the bounded tasks and final validations, and consider completion only when no unresolved accepted plan, unapproved simplification, missing required consumer, or certification blocker remains.
Event 021 is not declared complete.
