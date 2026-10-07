# Event 032 current contract reconciliation, 2026-10-07

Disposition: `implemented` documentation reconciliation, with gameplay requirements and validation still unresolved or blocked as listed below.
This is the owned resume handoff, not a completion audit or approval of the later simplifications.

## Scope and acceptance basis

The current parent delegation explicitly supplies the user goal of implementing the fullest accepted `docs/specs/032_missiles_specs/` contract, with no simplifications and all named checks, assets, achievements, and catalog work.
It authorizes recommended spec-consistent choices, but does not authorize dropping accepted requirements.
That delegation establishes the source-contract basis used here independently of README status labels and historical agent approval claims.
`agent_decisions_2026-10-04.md:3-4` records an implementing agent's authority claim, which is evidence of its reasoning rather than a separate user decision accepting every exception.
Rejecting a proposed helper architecture does not reject the gameplay or validation requirement it was intended to satisfy.

Only this report was created after checking its absence twice immediately before writing.
No gameplay, localisation, skills, spreadsheets, other documentation, Git state, or assets were changed.
No agents were spawned, game launched, or logs searched or requested.
Physical reserve custody and launch allocation remain parent-owned and were not deeply audited here.
Source references below are repository-relative Windows paths and line anchors observed during this pass.

## Source-of-truth map

| Evidence | Use and disposition |
| --- | --- |
| Current parent delegation | Acceptance basis for the full source contract and the no-simplification boundary |
| `docs\specs\032_missiles_specs\032_missiles_spec_part_2_program_and_launch_sites.md`, parts 3 through 6, part 8, acceptance criteria, and requirement traceability | Accepted requirements under that delegation, with suggested tuning and conditional routes distinguished from unconditional requirements |
| `docs\plans\032_missiles_plans\agent_decisions_2026-10-04.md` | Later owner decisions and implementation claims, with conflicting rejections or deferrals remaining unresolved |
| `docs\plans\032_missiles_plans\032_missiles_test_results.md` | Historical validation ledger, explicitly partial/blocked, with later dated sections qualifying older present-tense claims |
| `docs\plans\032_missiles_plans\catalog_changes_pending.md` | Queued wording request, with its status exception unresolved independently of wording alignment |
| Evolution and ordinary-preparation probability handoffs and their saved fixtures | Historical scenario-specific evidence and baseline inputs, with missing compares still blocked |
| Current runtime definitions cited below | Evidence of implemented source behavior, without independently establishing design acceptance or engine execution |

## Prioritized remaining requirements

1. **P1: restore MTTH fidelity and remove the recurring global programme recount.**
   Part 4 `:29-62` requires an MTTH model, pressure sensitivity, and bounded evaluation at firing, threshold, or exact prerequisite boundaries.
   Part 6 `:527-550` requires the corresponding timing model and pressure scenarios, and part 8 `:627-642` forbids recurring global country scans.
   `common\scripted_effects\032_missiles_operations_effects.txt:655` samples a bounded multiplier once, then stores a rounded deadline.
   Constants `common\script_constants\032_missiles_constants.txt:818-824` define the `0.75` minimum, `0.50` width, and 30-day watch.
   The watch at operations effects `:983-1012` repeatedly calls the evaluator, which recounts every registered programme at `:543-594`, including a nested programme search for hostile endpoints.
   A programme registry can cover the same countries as a world scan, so absence of an `every_country` token does not establish compliance with the performance contract.
   The bounded jitter deadline does not establish the specified MTTH distribution, and its pressure multiplier is frozen when armed rather than continuously justified over changing conditions.
   Preserve the accepted first-high-Chaos short-delay exception, but have the owner implement and the probability auditor evaluate the ordinary stochastic timing contract and an exact or justified sparse observation strategy.
   The architecture recipe may remain rejected, while the underlying timing and performance requirements remain outstanding.

2. **P1: reserve chemical payload at preparation through its owning system.**
   Part 3 `:26-47`, especially pipeline step 7 at `:39`, requires reserving missiles and payload before preparation.
   `common\scripted_effects\032_missiles_operations_effects.txt:4221-4228` marks chemical reservation accepted after a stock check, without creating chemical escrow.
   `missiles_release_operation_payload` at `:4232` returns held nuclear or biological resources, while `missiles_check_chemical_payload_stock` at `:4261` is explicitly read-only.
   The launch recheck in `missiles_commit_operation` at `:6113` is a useful source guard but cannot stop another consumer spending the supposed reserved chemical stock during preparation.
   The note's `:90` and `:153` queue chemical holding for a future CBRN refund route, which leaves an accepted Event 032 requirement unfinished.
   Resolve the reservation and idempotent release API with the CBRN owner, then cover competing consumers, cancellation, invalidation, and committed use without duplicating its storage models inside Event 032.

3. **P1: remove the recovery AI force exemption or supply a proven concrete garrison equivalent.**
   Part 5 `:684-713` requires nearby supplied divisions or a concrete garrison condition for loyal-force recovery.
   `common\decisions\032_missiles_missions.txt:145-188` permits success through `is_ai = yes` instead of any force presence at `:159-165`.
   The human branch proves a division count, but the inspected block does not establish supplied forces either.
   `missiles_send_loyal_forces` at decisions `:1416` does spend manpower, infantry equipment, and command power, but `missiles_begin_site_recovery` at operations effects `:1703` stores only the target and timer rather than a local garrison proof.
   `localisation\english\032_missiles_decisions_l_english.yml:372` tells players two divisions must be stationed in the named state.
   The note's `:30` cites AI difficulty rather than an accepted exemption or a garrison proof.
   Retain a common successful recovery requirement and implement an AI path that can satisfy it, with explicit supply or equivalent garrison evidence and named recovery scenarios.

4. **P1: complete the explicit Event 5/6 succession bridge.**
   `docs\specs\032_missiles_specs\032_missiles_system_connections.md:13-59` requires an Event 5 succession call after frozen state allocation and before military cleanup, plus the Event 6 inherited-site helper and infrastructure-aware transfer validation.
   Acceptance criteria `:282-286` retain those bridges.
   Literal gameplay-call searches found no invocation of `missiles_prepare_planned_inheritance`, `missiles_finalize_controlled_planned_inheritance`, or `missiles_transfer_inherited_site` in `common\` or `events\`.
   Their definitions exist at operations effects `:6272`, `:6410`, and `:7006`, but definition existence does not establish integration.
   Generic release hooks at `common\on_actions\032_missiles_on_actions.txt:185-195` call `missiles_reconcile_released_country_sites` at operations effects `:6602`, which excludes planned-inheritance states and routes other sites through capture handling.
   The note's round-2 decision at `:154` leaves planned-inheritance helpers uncalled.
   Have the parent inspect the exact Event 5/6 allocator boundaries and wire or prove the required succession contract there, preserving those owners' package rules.
   This finding concerns call-site coverage only, not the reserve arithmetic reserved to the parent.

5. **P2: restore survey failure settlement and resolve the broader construction-refund claim precisely.**
   Part 5 `:222-224` explicitly says survey failure returns resources according to progress.
   Survey payment is debited in `common\decisions\032_missiles_decisions.txt:88-98`, while `missiles_cancel_site_survey` at operations effects `:3571-3575` only clears project fields.
   Secondary construction similarly debits resources at decisions `:454-465` and only clears fields at operations effects `:3577-3581`.
   The note's `:33` rejects both refunds because the fee is small and constants would need moving, which does not discharge the survey requirement.
   Part 5 `:404-423` specifies secondary construction but does not itself specify an exact progress-refund schedule, so do not invent one or claim that schedule has been accepted.
   Implement the explicit survey settlement from an exact paid receipt, and separately resolve secondary cancellation settlement with its owner under the full-contract boundary.

6. **P2: reopen captured-site diplomacy as a conditional requirement, not a rejected feature.**
   Part 5 `:251-261` lists five resolutions, including explicit diplomatic transfer.
   Part 2 `:375-383` conditions ally or overlord transfer on a safe scripted route.
   The four current paths and final guard/study resolution are visible at decisions `:1171` onward and operations effects `:6634-6677`.
   The note's `:43` rejects transfer because its lead named four resolutions and transfer localisation is absent, without recording an engine or owner limitation proving the conditional route impossible.
   Have the owner establish a safe target and transaction route or record the exact blocker before reducing the accepted resolution list.
   Preserve the explicit mutual-exclusion contract, and do not silently turn guarded or studied sites into later integration choices.

7. **P1 validation: complete the specialist baseline/patch/compare cycle before any completion claim.**
   Part 6 `:552-586` and acceptance criteria `:298-305` require named scenarios, complete pools where relevant, sweeps, and final same-scenario compares.
   The later note records new or altered decision, option, targeted-site, rogue-scuttle, retaliation-isolation, and timing surfaces with `INTERNAL_ERROR` or no further probability attempt at `:37`, `:50`, `:81`, `:92`, `:104`, `:168`, and `:217`.
   The 83-scenario matrix is not satisfied by source tests or the older command-power comparison, whose unbound inputs are explicitly recorded in test-results `:100-110`.
   Preserve `032_evolution_gate_probability_baseline_2026-10-03.md` and its 22-scenario fixture, `032_probability_matrix_audit_2026-10-03.md`, and `032_ordinary_preparation_probability_audit_2026-10-03.md` with its distinct strike/target fixture.
   The parent must use `chaosx_ai_probability_auditor` rather than treat this curator's discovery call as a specialized audit.
   Existing October snapshots do not automatically provide the immediately preceding source baseline for every later weight change.
   Recover exact earlier sources where necessary, preserve source bytes and scenario identities, and retain an exact blocker for any missing baseline or unbound route rather than self-compare current source.

## Retaliation acceptance edge and secondary decisions

The current source improves the old underguarded unlock: `common\scripted_triggers\032_missiles_operations_triggers.txt:1081` requires 900 Chaos, no `world_end`, two operational programmes, and a hostile witness.
The witness recount at operations effects `:574-583` proves an actual war relation, while the responder predicate at operations triggers `:1027` requires Advanced stage, command control, reserve, and a secure controlled site.
It omits the hostile-but-not-at-war and severe-tension alternatives listed in part 4 `:832-839`.
`missiles_pressure_hostile_pairs` counts qualifying responding endpoints rather than distinct unordered pairs, so two responders in one bilateral war can contribute two to the high-pressure threshold.
The stronger complete-line maturity and endpoint technology/chain qualification requirement is attributed to a prior parent delegation in `032_evolution_pacing_architecture_2026-10-03.md:5-8` and `:249-260`.
That handoff is evidence of the prior parent requirement, but the original self-contained delegation is not supplied here, so its exact strengthened acceptance remains unresolved.
The later note `:100` explicitly substitutes Advanced for Complete because the stronger gate would be rare, while `common\scripted_triggers\032_missiles_triggers.txt:116` defines mature as Complete.
The parent should resolve that basis and test the war, non-war hostility, pair-count, maturity, technology, and response-resource endpoints separately in `EVO-10`.

Lead decision `agent_decisions_2026-10-04.md:12` also groups changing the participating site with optional preparation effort under one rejection.
Part 5 `:120-125` attaches "where allowed" to increasing effort, not to the separate pre-commitment site-change bullet.
Retaliation redirect is expressly qualified by validity in acceptance criteria `:265`.
Keep these three dispositions separate and require a precise validity limitation before rejecting the unconditional-looking site-change path.

## Plan and handoff dispositions for resume

| Document or decision | Reconciled disposition and reason |
| --- | --- |
| Later recovery exemption, survey refund rejection, and chemical deferral | `unresolved` departures from accepted requirements, with current source evidence above |
| Captured-site transfer rejection | `unresolved` conditional-route omission without an exact safety blocker |
| Rejected evolution architecture recipe | `rejected` owner implementation proposal, without rejection of the accepted timing, eligibility, and performance requirements |
| Existing evolution and ordinary-preparation probability handoffs | `blocked` or unresolved validation, preserving their specific scenarios, baselines, and historical route failures |
| Catalog `D33` and `H33` wording | `accepted and queued` under the current alignment goal because it matches localisation `032_missile_crisis_l_english.yml:85,97`, with workbook application and export still assigned to its owner |
| Catalog `M33 = Needs Testing` | `unresolved` exception because the event skill's post-20 existing-root rule uses `To Be Reworked` and `032_event_catalog_status_review_2026-10-03.md:3-4` records that rule's prior parent review |
| Conditional scripted strike route | Retained source-contract choice supported independently at part 8 `:411-434`, with native raid icons conditional on an actual native consumer |
| Old lint and scope repairs, warning cleanup, and log wiring | Historical implementation evidence to preserve, without treating passing source pins as proof of the outstanding gameplay contract |

## Documentation contradictions and stale instructions

`032_missiles_test_results.md:18` says the default-enable completion gate is restored, while its later gameplay section and `common\scripted_triggers\chaosx_settings_triggers.txt:32` enable Event 032 before its accepted validation gaps are closed.
Acceptance criteria `:20-21` and requirement traceability's catalog section require the disabled-until-complete boundary.
Default enablement and catalog status are separate decisions, and one does not justify changing the other.

Test-results `:45-47` describes firing-only deterministic evaluation as current, while the implemented watch and randomized delay above supersede that description.
Preserve it as dated baseline history and state the actual remaining fidelity gap.
The old probability handoffs' `32_N_1` toggle suggestions are also historical, while round-3 decisions `:228` onward and current source use type `32` with catalog stages, yielding `32_32_N` keys.
Do not reapply the stale toggle recipe or overwrite immutable baseline fixtures with current key names.
Part 4 `:64-76` calls its distinct-type mapping recommended, so preserve five-track functionality and reconcile its presentation mapping with the current shared-log contract rather than infer a mandatory rollback from that table alone.

`agent_decisions_2026-10-04.md:17` asks for fresh-log attribution and retaining temporary markers, which is stale operational direction under this parent's no-log-search boundary.
The pending catalog note's status exception and its blanket "accepted and queued" label must be separated from its verified wording edits.
No duplicate document was merged or deleted, and no shared document was patched.
The named historical probability and architecture handoffs should remain evidence, with current disposition notices supplied by the parent where useful.

## Bounded MCP evidence and limits

Exposed event, technology, and probability routes were verified in the connected tool metadata before calls.
No standalone Technology Tree Viewer availability was verified, and no general service-health claim is made.

The bounded `hoi4.event_inspect` trace for `chaosx.nr32.191` returned `EVENT_INSPECTED_PARTIAL`, revision `4969042f8122a553c30402d067b14cdc9c731bc3674b68dd419cb0813fb913a7`, graph hash `60323e4fbfff191e6014b7974139c7ab25f78ed1404cd7311f444ed4bf70b43f`, focused analysis, zero helpers, one blocking workspace diagnostic, and failed validation.
Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4c17c506e5032033c70f6edde0e54824a8f9e03bb57444af789f45551e49251b/47a9e509a524aba56ffcbba479eaf14a584d5410ac9e671fecab9a8bf9334be5/event-trace-4969042f8122.json`.
It does not establish helper or lifecycle coverage.

The narrow `hoi4.probability_inspect` request for `direct_random`, candidate `missiles_arm_evolution_track`, returned `PROBABILITY_SOURCE_DISCOVERED` rather than the historical `INTERNAL_ERROR`.
It found zero requested candidates with `discoveryReason = requested_adapter_empty`, suggested `random_list`, and listed 19 other candidates, so neither timing coverage nor a numeric result exists.
Source revision was `c8c7e4d386bb68f789448fd5c1f371697aa4539f8f5f7b1420724b1fbb76acf5`, with inspected source hash `b1054d959a45f2c4df751e9a3ac31f5f50bb0d86a0e11195f8b978d7a86c17f5`.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7e1c95a2d2a38933339bcd33313c5917e2a3f4efacdd23d10610dacb150a105e/aa4cc3a6a57f881065a17b24280f15b9a48a748f3d97752be8a83f4a05e401e3/probability-inspect-b1054d959a45.json`.
The final source read had a different hash after concurrent parent work, so this cached inspect is not current-source coverage.

A technology trace for `improved_rocket_engines`, depth 1 and 8 nodes, yielded without a domain result.
The observation cell was terminated to avoid a long MCP wait under the parent constraint.
No result, artifact, or server-side cancellation was verified, and the server outcome remains unresolved.
No full helper expansion, GUI, focus, map, render, or compare pass was attempted because those would exceed this bounded reconciliation or concern surfaces not edited here.

## Validation and handoff limits

Targeted source reads verified each listed departure and its call-site or predicate evidence.
Literal inheritance caller searches, current toggle/default-enable searches, and catalog-to-localisation wording checks were run.
A prose hard-wrap scan of the decisions note, test-results, pending catalog note, README, traceability, and acceptance criteria found no candidate accidental mid-sentence joins.
No existing hard wraps were corrected because shared-doc writes were prohibited, and this report preserves headings, paragraphs, lists, and table rows with prose sentences on separate physical lines.

The observed operations-effects SHA-256 was `493d25cca870f7b01f71346cac06126f0fca87eb5fae4fca1666351969690b5e`, and operations-triggers SHA-256 was `424e1749a463c7621c89f8a881eccfd05109f78b8911f6598601c7d324948504` after the concurrent source change.
Line anchors were rechecked for the changed helper positions, but this shared tree can change after handoff.
The offline Event modding MTTH section `paradox_wiki\Event modding - Hearts of Iron 4 Wiki.md:130-145` was read with SHA-256 `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d`.
Installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\mtth\mtth_variables.txt:1-13` documents computed MTTH variables and was read with SHA-256 `0cd46aff2dc43cb167269064f68741fd03090404b6becc398e32344ceb34b6fd`.
Neither reference establishes runtime parity for Event 032's custom scheduler.

No gameplay tests were rerun because this is a read-only reconciliation and the known source pins encode several questioned choices.
No workbook or binary asset was opened, and no asset, achievement, or live-game completion claim is made.
The eight achievement registry definitions at `common\achievements\chaos_redux_achievements.txt:4364-4403` exist, while the historical 82-asset ledger remains evidence to be reviewed by the parent rather than a fresh asset audit.
The parent should finish the listed accepted work, reconcile the acceptance edges, obtain the required specialist and MCP evidence, then assign final wording and workbook/export alignment to the catalog owner.
Skills used: `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-mtth`.
No skills were changed.
