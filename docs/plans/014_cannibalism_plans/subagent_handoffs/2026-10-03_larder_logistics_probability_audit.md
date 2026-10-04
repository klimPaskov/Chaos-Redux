# Event 014 Larder Logistics Probability Baseline

Disposition: Read-only baseline captured; partial MCP audit; unresolved for engine acceptance and balance.

Date: 2026-10-04 (Europe/Kiev).

Scope: parent-accepted Event 014 reveal/unification Larder transfer and storage-cap proposal, plus only the directly connected Event71 option weights, unified Larder decision weights, and three CBL Larder-route focus weights.

Source state: No gameplay, AI, event, focus, decision, localisation, GUI, asset, spreadsheet, or runtime source was patched. No game, logs, or Git actions were used. The frozen source manifest is at docs/plans/014_cannibalism_plans/2026-10-03_larder_logistics_probability_audit/evidence/baseline/source_baseline_manifest.json; all ten listed files matched current raw bytes at handoff.

The accepted proposal is documented in [2026-10-04_accepted_code_proposal.md](C:/Users/klimp/OneDrive/Documents/Paradox%20Interactive/Hearts%20of%20Iron%20IV/mod/chaos_redux/docs/plans/014_cannibalism_plans/subagent_handoffs/2026-10-03_larder_logistics_owner_plan_evidence/2026-10-04_accepted_code_proposal.md). Its accepted capacity base is 1200, plus 100 per controlled state and 50 per development-score point, with the existing 5000 hard ceiling and 2000 ordinary-country ceiling. One state and zero score yields 1300; the earlier 1000-base proposal and 1100 one-state example are superseded history. The accepted proposal says contributing flags each add the existing five-point development score, and weights, reserves, and bonus predicates remain unchanged. This is accepted queued design, not installed code.

The parent’s eight fixture IDs and supplied values are preserved in the companion JSON. They are synthetic and unobserved. CBL is the host actor and CBA the donor; for Event71 option AI, the actual option decision-maker scope is the CBA donor. The fixture contract lacks several exact source inputs, including event divisions/alignment and flags, focus completion/war/strategy state, state IDs for capital distance, and the donor-versus-host stock scope for two fixtures.

## Audited weighted surfaces

Event chaosx.nr14.71 has four options: a submit while retaining command, b surrender the warband, c bargain for autonomy, and d resist. Their source bases are 40, 15, 25, and 20. The source modifiers include alignment, network-route, confederate, defiance, and division thresholds; the exact constants and predicates are listed in the companion evidence. Offline wiki documentation distinguishes these proportional ai_chance options from AI scores. Probability evaluation produced 32 option/scenario instances, of which 16 were eligible and 16 excluded, with 11 unresolved inputs. The MCP explicitly withheld normalized probabilities because the file-wide candidate pool was incomplete; source review confirms four options within Event71, but required alignment/division values, event gates, route/preparation flags, actor/recipient human-AI status, and target-generation state were absent. The reported “never eligible” status for options a and b applies only to these incomplete fixtures and does not prove gameplay impossibility.

The eight declared unified Larder actions are cannibalism_unified_centralize_larder, cannibalism_unified_convert_captured_workshop, cannibalism_unified_abandon_exhausted_frontier, cannibalism_unified_designate_feeding_capital, cannibalism_unified_rapid_consumption, cannibalism_unified_managed_consumption, cannibalism_unified_mobile_consumption, and cannibalism_unified_battlefield_consumption. Their source bases are 25, 25, 50, 25, 50, 10, 25, and 25 respectively. Their modifiers depend on Larder thresholds, route flags, war state, and state-target validity. The focused inspect reports this eight-action family as complete, but evaluation marked all 64 action/scenario instances ineligible and 49 unresolved because the fixture set does not declare category visibility, route flags, target-state validity, manpower/equipment, war, or operation-slot state. Treat the results as unresolved, not proof that these actions are impossible. These are AI willingness scores, not click probabilities.

The three connected focus weights are CBL_centralize_the_larder_quota (base 10, factor 0.75 below Larder 350), CBL_build_the_storage_network (base 16, factor 5 while at war), and CBL_continental_larder_doctrine (base 24, factor 0.75 below Larder 350). Focus evaluation returned 24 focus/scenario instances, 16 eligible, and 7 unresolved; the focus sensitivity pass used the seven fixtures with numeric host stocks and omitted stale_generation_no_transfer because its host stock was unspecified. The focus inspect route requires has_completed_focus, has_war, variable.cannibalism_larder, and focus.external_factors_complete. The adapter models a random score race and does not normalize these focus weights into probabilities. No exact route-selection chance or rank reversal is established.

## Current logistics, cap gates, and material risks

The current unified cap is the static global_larder_maximum of 5000; ordinary Larder consumers clamp to 2000. Eight global-ceiling clamp sites are frozen at effects source lines 4210, 6409, 12112, 12179, 12647, 14343, 15170, and 17922. The accepted owner proposal still needs to migrate those eight sites and route updates through its effective-capacity helper and approved transaction finalizers.

Current reveal construction copies inherited donor Larder, adds the 300 starting-global-Larder constant, then clamps to the static 5000 ceiling. Later submit/surrender/autonomy transfer dispatches donor Larder multiplied by the route fraction after existing contract bonus/relief. The destination adds the dispatch and clamps to 5000. Distance loss is not currently applied. The defined constant cannibalism_unification.host_larder_transfer_factor equals 1.00 and has no consumer in the frozen source files.

cannibalism_unified_larder_capacity is a recomputed contract-flag score, not a physical storage-volume limit. Each counted flag contributes five points; the Larder decision category stages are 50, 80, and 110. The early CBL route shows why treating every score point as physical capacity needs review: classify-the-consumption-states opens two counted flags; build-the-storage-network opens two and adds controlled-route infrastructure; boards-of-captured-industry opens two; continental-larder-doctrine opens two. CBL_centralize_the_larder_quota opens the quota decision and authority but is not itself a counted capacity flag. The score also counts route, decision, mission, and capstone flags, so the owner should map the accepted development term to explicit storage/economic development inputs or document why each counted flag contributes.

Storage project costs/gates are 10,000 manpower, 100 support equipment, and 10 trains; the target must be controlled, passable, and lack an active storage network. The decision category must be open and the Larder capacity score must meet stage 1 (50); storage projects must be opened, the manpower/equipment gates met, and an operation slot be available. The project creates one infrastructure level and a 90-day storage modifier. These are source facts, not evaluated campaign timing.

The selection-time host guard at cannibalism_selected_unification_host_is_valid checks the expected host generation. The later cannibalism_has_valid_unification_destination trigger at triggers line 5348 only checks that the target exists, has not capitulated, is revealed, and has a valid unified/Wendigo identity; it does not compare actor identity or expected generation. The accepted owner plan’s separate generation guard is necessary for stale_generation_no_transfer before debit, credit, autonomy, annexation, or slot retirement.

Source indicates both-human preservation zeros the inherited Larder snapshot at reveal; the two submission/surrender options are hidden when both donor and destination are human. The named fixture still needs its explicit owner-path scenario after implementation.

## MCP evidence and limits

The complete adapter inspections, scenario hashes, source revisions, evaluation/sweep IDs, artifact URIs, reference citations, candidate completeness, and exact blockers are in evidence/probability_baseline_evidence.json.

The Event71 adapter inspection found a file-wide inventory of 40 ai_chance options and two random-list entries; only the four Event71 options are in this audit. The random list at events source line 772 concerns character outcome selection and is outside the Larder transfer scope. No relevant MTTH-backed weight was found in the targeted Event71/decision/focus blocks; no timing adapter or simulation was run.

Event inspect and options render returned partial outputs over a workspace graph of 9,859 events. The event render selected 16 nodes but omitted 42,971; the trace and render share one graph hash. Structural focus inspect/render was not run before this handoff cutoff. A decision_inspect request for one decision expanded to a partial workspace-wide report (7,949 decisions, 1,972 categories, 218 unresolved definitions) and is excluded from conclusions.

Probability evaluations and sweeps emitted ranking, matrix, waterfall, sensitivity, threshold, and unresolved artifact links. Separate probability_render calls returned PROBABILITY_ANALYSIS_NOT_CACHED. A bounded artifact read returned “Artifact provenance manifest is unavailable.” This leaves linked payload inspection incomplete, although the tool-returned summaries and URIs are preserved.

The Event71 and decision sweeps used one numeric anchor per scenario and returned eight points; they do not prove a threshold crossing or rank reversal. The focus sweep returned seven scenario points and five unresolved items. Initial sweep calls without numeric values, and calls using arrays as numeric alternatives, returned PROBABILITY_SWEEP_RANGE_REQUIRED. Do not treat the partial sweep status as a successful threshold proof.

No probability_compare was run because no owner patch exists. The same eight scenario IDs must be compared after the accepted proposal is applied. No simulation was run because no uncertain-input distribution or seed was declared. No probability_sequence was run because no complete cadence-driven weighted pool was declared. No exact selection probability, sampled estimate, campaign balance, or engine behavior is claimed.

## Recommended owner follow-up

1. Implement the accepted 1200-base effective-capacity calculation, preserve the 5000 hard ceiling and 2000 ordinary cap, and migrate all eight listed global clamp sites at transaction/finalization boundaries.
2. Define which real storage, network, and development flags feed the development score; avoid assuming the full contract capacity score is physical storage.
3. Apply the accepted distance quote to constructor inheritance, post-reveal absorption, and autonomy, with actual source/destination capitals and valid capture proofs. Missing targets or negative distance must reject mutation instead of falling back to zero distance.
4. Add the accepted host-generation and actor-identity guard to the later destination validation before any irreversible transfer or lifecycle change.
5. Define and test stock handling when territory loss lowers effective capacity, including the cap_loss fixture.
6. After the source patch, run probability_compare through this auditor on all three adapters using the same named fixture contract, then resolve incomplete candidate pools, flags, target validity, focus completion, war, and external strategy factors before claiming engine acceptance.

Skills applied: chaos-redux-events, chaos-redux-subagents, chaos-redux-mtth, chaos-redux-decisions-missions, chaos-redux-event-planning, and chaos-redux-focus-trees. No skill was created or updated.

