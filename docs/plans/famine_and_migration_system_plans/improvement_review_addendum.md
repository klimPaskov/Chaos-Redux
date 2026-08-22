# Famine and Migration Improvement Review Addendum

Date: 2026-08-22.

Status: closure deferred. The implemented shared system is already broad and mechanically deep enough that another expansion layer would add bloat. Completion still requires a bounded set of accepted-design integrations, evidence producers, and audit gates. This addendum does not authorize new gameplay breadth.

## Disposition vocabulary

- `required-before-completion` means the accepted specification or repository completion rules already require the item. It is not an optional expansion.
- `optional-future` means the current accepted design can close without it.
- `rejected-by-spec` means it must not be added as part of this system.

## Review conclusion

Do not add another mechanic family, country package, focus route, formable, full scripted GUI, mapmode, historical casualty target, or random event.

The accepted system already supplies a dynamic eight-component food-security model, stage hysteresis, population-scaled famine mortality, exact state-to-state transfer accounting, persisted cohort identity, reception capacity, integration, resettlement, voluntary and forced return, closed-border consequences, 26 decisions, three missions, eight achievements, fifteen historical profiles, and exactly two dedicated state mapmodes.

The current implementation also closes the important earlier handoff defects. `famine_migration_rebind_cohort_destination_safe` in `common/scripted_effects/chaosx_famine_migration_effects.txt` and its predicate in `common/scripted_triggers/chaosx_famine_migration_triggers.txt` provide the safe third-country rebind contract, while `famine_migration_refresh_reception_context`, `famine_migration_record_state_resettlement_projection`, and `famine_migration_record_state_return_projection` provide live mapmode projection producers. The parent has also corrected emerging-category lifecycle, dormant-country retirement, reception debit and credit ownership, forced-return proof, and trapped-population food pressure. Those older findings are superseded and must not be reopened as new expansion work.

The correct next step is to close the required findings below, rerun their owner audits, and then use a system completion audit. A second broad improvement-loop pass is not warranted.

## Required-before-completion findings

### FM-R1: active owner systems still do not reach the public adapters

Classification: `required-before-completion`.

Design evidence: `docs/specs/famine_and_migration_system_specs/famine_and_migration_system_integration_matrix.csv` assigns explicit owner-to-shared and bidirectional seams, while `famine_and_migration_system_spec_part_7_cross_system_connections.md` requires every listed active connection to use a shared adapter and forbids duplicated food, movement, or death transactions. The architect handoff and the reconciled `docs/systems/famine_and_migration_system.md` both identify the occupation, camp, gulag, forced-labor, deportation, bombing, nuclear, fallout, outbreak, disaster, war, peace, event, Air Cleanliness, chemical, biological, cluster, scenario, and blockade request families as API-only or owner-call-site dependent.

Current implementation evidence: a repository search for `famine_migration_(submit|request|apply|condemn|register|handle|mark|achievement|rebind|transfer)` outside the shared famine effects, famine triggers, famine decisions, achievement helpers, and lifecycle on-actions finds no owner-local pressure calls. `common/scripted_effects/famine_migration_adapter_effects.txt` defines the direct-death and Condemnation wrappers, but definitions are not consumer reach. `famine_migration_collect_surface_context` can read occupation and Air/fallout facts only after a state is already registered; it does not make the authoritative owner transaction call.

Implementation surfaces:

- Air and fallout owners: `common/scripted_effects/fallout_consolidated_effects.txt` and their exact-state aftermath effects.
- Camps, genocide, forced labor, and deportation owners: `common/scripted_effects/camp_repression_rework_effects.txt`, `common/scripted_effects/genocide_crisis_effects.txt`, and their decision/event transaction points.
- Chemical and biological owners: the existing chemical and biological warfare/outbreak scripted effects and their exact target-state aftermaths.
- Nuclear and bombing owners: existing strike, fallout, and strategic-damage effects after direct owner deaths resolve.
- Natural disaster owner: `common/scripted_effects/013_natural_disasters_effects.txt` and the resolved Event 13 state aftermath.
- Existing event owners named by the matrix: Event 5, Event 6, Event 14, Event 15, Event 20, White Peace, and other currently implemented owner paths only where an exact actor, state, cause, amount, and proof already exist.
- Shared consumers: `famine_migration_request_*_pressure`, `famine_migration_request_*_flow`, `famine_migration_apply_*_deaths_exact`, and the six `famine_migration_condemn_*` wrappers.

Acceptance criteria:

1. Each currently implemented owner listed in the matrix calls one bounded adapter at its authoritative exact-state transaction boundary.
2. Each call supplies actor, state, cause, positive dynamic amount, and family-specific proof; missing proof fails closed.
3. Direct deaths remain owned and debited by the source system, while famine mortality, movement debit/credit, and route deaths remain owned by the shared contracts.
4. No owner call introduces `every_state`, `every_country`, or another periodic world scan.
5. Catalog-only concepts 118, 120, and 131 remain unwired until a real owner source exists. Do not fabricate an event or route to satisfy a matrix row.
6. The completion audit traces every active adapter from owner call site to bounded shared result and cleanup.

Implementation status at handoff: the parent has routed this finding to the active `famine_adapter_wiring` worker. Treat FM-R1 as pending until that worker names the final owner callsites and the completion audit proves their adapter chains; the existence of an in-progress patch is not closure evidence.

### FM-R2: accepted incident and report presentation has assets but no gameplay consumer

Classification: `required-before-completion`.

Design evidence: `famine_and_migration_system_spec_part_6_decisions_ai_presentation.md` requires food-security incident reports, civilian-flight incident reports, bounded foreign responses, and political consequence events. It specifically requires early incident options to teach the system before the standing decision category appears. These are system reports, not a random-event catalog entry.

Current implementation evidence: `interface/famine_and_migration_system_event_pictures.gfx` registers seven `GFX_report_event_famine_migration_*` sprites and `localisation/english/famine_migration_l_english.yml` supplies seven matching report labels. A source search finds those sprite identifiers only in that `.gfx` file and no `picture = GFX_report_event_famine_migration_*` consumer in `events/` or `common/`. The generated-art and documentation-curator handoffs explicitly leave report consumers unresolved.

Implementation surfaces:

- Existing shared report/notification carrier, if the parent can identify one that needs no new system event ID.
- `famine_migration_transition_food_stage`, blockade resolution, closed-border trapped result, exact evacuation/arrival, relief recovery, nuclear evacuation, and voluntary-return transaction boundaries.
- The seven registered report sprites and their existing localisation labels.

Acceptance criteria and blocker:

1. Every delivered report asset has at least one bounded, non-duplicative consumer at an accepted transaction boundary.
2. Threshold/source reports name the actual state, controller, dominant cause, and relevant immediate response; foreign response reaches only directly relevant countries.
3. Reports do not add an event-pool row or pacing weight.
4. This addendum does not propose a new event ID, as explicitly forbidden by the review scope. If no existing report or notification carrier can satisfy the accepted incident-event requirement without a new ID, the implementation route is unresolved and the parent must obtain a design decision rather than silently omitting the accepted surface.

### FM-R3: achievement predicates contain unproducible disqualifiers and incomplete lifecycle proof

Classification: `required-before-completion`.

Design evidence: `famine_and_migration_system_achievement_prompt.md` requires all eight achievements to use persistent transaction evidence, enforce every disqualifier, resist transfer cycling and debug/scenario shortcuts, and survive cleanup, annexation, and identity changes.

Current implementation evidence at the review snapshot:

- `famine_migration_achievement_record_protected_internment`, `famine_migration_achievement_record_protected_forced_labor`, and `famine_migration_achievement_record_transfer_cycle_failure` exist only as definitions in `common/scripted_effects/famine_migration_achievement_effects.txt` and have no caller in `common/` or `events/`.
- `famine_migration_achievement_blockade_predatory_requisition`, `..._blockade_wasteland`, `..._blockade_self_route_exploit`, `..._corridor_attacked`, `..._corridor_manufactured_crisis`, and `..._tag_switch_disqualified` are read in `common/scripted_triggers/famine_migration_achievement_triggers.txt` but have no producer in current gameplay source.
- `famine_migration_achievement_record_reception_safe` writes the medical `no_outbreak` and `not_overloaded` evidence at the same safe-reception observation. The completion audit must prove that later overload or outbreak can invalidate or withhold the durable outcome rather than allowing an early stale success flag.

Implementation surfaces:

- Exact protected-cohort internment/forced-labor owner transactions.
- Transfer/cohort visit-history or another bounded anti-cycle evidence contract; do not infer cycling from population alone.
- Corridor mission attack/failure and manufactured-crisis evidence.
- Blockade requisition, wasteland, and self-route exploit evidence.
- Country/tag identity lifecycle and achievement persistence/disqualification ownership.
- `famine_migration_achievement_record_reception_safe`, durable-outcome recording, and the eight achievement completion predicates.

Acceptance criteria:

1. Every positive requirement and disqualifier in all eight predicates has an authoritative producer, cleanup policy, and ordinary success/failure scenario.
2. A disqualifying action cannot be erased by category retirement, cohort cleanup, tag/cosmetic-tag change, annexation, or a later safe action.
3. Medical reception remains pending until the accepted observation window or durable resolution proves no host outbreak and no catastrophic overload.
4. The achievement audit covers ordinary success, each disqualifier, save/reload persistence, host/origin annexation, cohort cleanup, and no historical-memory auto-unlock.

Implementation status at handoff: the parent has routed this finding to the active `famine_achievement_hooks` worker. Treat FM-R3 as pending until that worker names every final producer and a focused audit proves the ordinary and disqualifying paths; the existence of an in-progress patch is not closure evidence.

### FM-R4: AI parity and weighted balance are not proven

Classification: `required-before-completion`.

Design evidence: `famine_and_migration_system_probability_scenarios.csv`, `famine_and_migration_system_spec_part_6_decisions_ai_presentation.md`, and `famine_and_migration_system_spec_part_8_balance_acceptance.md` require the same twenty named scenarios for player/AI parity, availability, ranking, cleanup, and post-change comparison.

Current implementation evidence: all 26 decisions have constant-backed `ai_will_do` blocks and the three missions use the ordinary AI-bearing decision surface. The post-implementation AI auditor started with `hoi4.probability_inspect` and obtained a complete 26-candidate pool with twelve required inputs and zero inspect-time unresolved inputs in `probability-inspect-c874297e02df.json` at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e291df9e026a268d85629ad9ffbca80b1afdecdc2b1b941df247495bac8c73a8/789f4c520bc0d1427ed53e779d3e783483625cb0ef2229b8fe34e17a1969ef7c/probability-inspect-c874297e02df.json`. MCP classifies these blocks as `mission_ai_will_do` and exposes raw score/rank only, not normalized click probabilities.

The exact twenty-scenario evaluation completed only as `PROBABILITY_ANALYZED_PARTIAL`: 520 rows, 59 unresolved items, and twenty diagnostics in `probability-27f3952bc314506bb9f685f5.json` at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ad819f65fad7b1d96cf62ad5ec0bb8491aed28a1343178f0298c81067f308978/ff7122146a44b03e4defe5c2c5181ad4793eacb387192a62e2cb7738d153465a/probability-27f3952bc314506bb9f685f5.json`. Every scenario retained 23 unresolved candidates and three explicit false outcomes because the flat fixture schema could not represent scoped `FROM` and target objects, route and donor validity, destination validity, stockpiles, cooldowns, or complete cost and prerequisite state. A twenty-point food-pressure sweep produced no rank reversal but retained the same 59 unresolved items. A same-fixture current/current compare produced zero changes, but it is not the required pre/post comparison because `docs/plans/famine_and_migration_system_plans/ai_probability_baseline.md` has no source or executable baseline artifact.

Required probability workflow:

1. Start from `hoi4.probability_inspect` on the current decision and mission sources.
2. Evaluate the exact twenty scenario IDs from the CSV without renaming or collapsing them.
3. Prove player/AI availability parity separately from candidate ranking.
4. Use sweep or sequence evidence for relief-versus-neglect, humanitarian-versus-coercive border policy, corridor completion, integration/return, and cleanup where one snapshot cannot prove the path.
5. Supply a supported typed fixture for country, state, `FROM`, and target scopes, including route, destination, donor, capacity, stockpile, ideology, exposure, cooldown, prerequisite, and cost state. Until the adapter supports those scopes, the affected eligibility and ranking conclusions remain unresolved.
6. Run `hoi4.probability_compare` against a genuine before/after source pair using the same named scenarios. The current/current comparison artifact at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6fa6b0695f2e8e83553b8266831a2c46babfd452c1534dcd728029a55c7f0f8c/a7fe0003e1dff35960086c0d13c6d5c683ae8592794ca98ee4ca007090328b51/probability-e7b9a0a14bc5741afdc6f63e.json` proves only fixture identity. Do not invent a numeric balance target merely to make the tool pass.
7. Keep the auditor's “never eligible” diagnostics for `fm_conceal_crisis`, `fm_enforce_closure`, and `fm_forced_repatriation` unresolved until valid scoped fixtures distinguish unreachable gameplay from unrepresentable context.
8. Do not treat `ai_will_do` score as selection probability, use hand arithmetic to replace unresolved MCP evidence, or use unrelated event `ai_chance` as shared-system evidence. The AI auditor is read-only; balance choices remain parent-owned.

### FM-R5: Event 149 retirement required catalog alignment and was resolved during this review

Classification: `required-before-completion`.

Evidence: no `chaosx.nr149.*` definition, invocation, or event-pool registration exists in current `events/` or `common/`, and no replacement event chain exists. At the initial review snapshot, `docs/spreadsheets/chaos_redux_events_catalog.csv:311` still described `Immigrations` as a random major-country population drain even though its status was `Unavailable`. `famine_and_migration_system_spec_part_7_cross_system_connections.md` requires Event 149 to stop applying a competing flat effect and requires docs/catalog wording to reflect final behavior.

Implementation surfaces:

- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, edited only through the spreadsheet owner.
- Export-only event/cluster/scenario CSVs regenerated with `.tools/export_event_catalog_csv.py` after the workbook change.
- Any event-detail or catalog-facing description that still promises the flat random drain.

Resolution evidence:

1. Commit `b09a91d59ced71f9a976c2d2c5c4910dd0688096` updates workbook row 149 to “Retired and absorbed into the shared dynamic famine and migration system. Unavailable as a random event.” and regenerates the CSV exports.
2. No new event ID, compatibility event, event-pool registration, or pacing weight was added.
3. A final source search must still confirm no competing Event 149 gameplay transaction, but no further design or implementation work is required unless that search finds a consumer.

### FM-R6: the two mapmodes are source-comprehensive, but the visual evidence gate remains incomplete

Classification: `required-before-completion` for evidence only; no new mapmode or mechanic is required.

Source evidence:

- `common/map_modes/chaosx_state_map_modes.txt` contains exactly `famine_state_map_mode` and `migration_state_map_mode` for this package.
- Famine exposes stage colors and authorized score, exposure, eight component ledgers, and recorded deaths through `GetFamineStateMapModeStage` and `GetFamineStateMapModeDetail`.
- Migration covers active origin/flight, trapped population, state reception load, overcrowding, resettlement destination, and return destination. Current producers are `famine_migration_refresh_reception_context`, `famine_migration_record_state_resettlement_projection`, and `famine_migration_record_state_return_projection`.
- The migration mapmode deliberately does not scan global cohort arrays or claim route-arrow geometry. Exact route, destination, amount, and cohort identity remain transaction-ledger data, which is the correct boundary for the engine's two flat state layers.

Current MCP evidence:

- `hoi4.map_inspect` for states 195, 430, and 935 returned `MAP_INSPECTED` with artifact `map-inspect.456c28c5a8e6bad1.json` at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7c630120c9208173110e3e4255096aeb9f879ab8f29e96c3840304a93f508842/1203073f4a3bdfcce300c3d1da3568dc443f1fa0d6df5391efb00ed4082fa797/map-inspect.456c28c5a8e6bad1.json`. It also retained unrelated `map/buildings.txt` locator errors and a diagnostic-ceiling blocker; those do not belong to this mapmode package.
- `hoi4.map_render` returned `MAP_RENDERED` with `map-state.png` at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/52b108966ee8fa0c47ca7458c9be87112fed5d84a5836a4c5f9bb313cb021685/0c6368da5905bb6f489e5e304abcbe40b97ed169b3c85e144ec06f03be49793f/map-state.png`. This proves base state geometry, not dynamic scripted-mapmode values.
- A current famine `hoi4.gui_inspect` request timed out at 180 seconds. The migration request returned `GUI_INSPECTED` with a 56 MB artifact, `gui-inspect.4a7b909e843b8b82.json`, but inline collections and hard diagnostics were truncated.
- Current `hoi4.gui_render` calls for both named mapmode scenarios returned `GUI_RENDERED`, but both produced the same 635-byte `mapmodes-full.svg` payload hash and the famine artifact could not be read because its provenance manifest was unavailable. This hardcoded-window approximation is not surface-specific visual proof.

Acceptance criteria:

1. Keep exactly the two current mapmode IDs and four current selected/deselected sprites.
2. Retain the public qualitative versus owner/controller detailed disclosure boundary.
3. Obtain a readable, surface-specific engine artifact for both modes if the installed MCP route becomes capable of modelling the hardcoded window. Until then, keep the exact limitation unresolved and require the parent completion audit to verify source consumers and user-owned live visual validation.
4. Do not add route arrows, fake path geometry, a third mapmode, or a full scripted GUI to compensate for the tooling limitation.

### FM-R7: report, adapter, achievement, and probability gaps require documentation reconciliation after implementation

Classification: `required-before-completion`.

Evidence: `docs/systems/famine_and_migration_system.md` and `docs/plans/famine_and_migration_system_plans/source_of_truth_map.md` list API-only adapters, unresolved report consumers, the probability timeout, and mapmode evidence limitations, but they must be reconciled against the final adapter and achievement patches and the completed Event 149 workbook retirement. The final acceptance checklist in `famine_and_migration_system_spec_part_8_balance_acceptance.md` forbids stale event rows, missing AI behavior, unresolved accepted designs, missing assets/consumers, and hidden simplifications.

Implementation surfaces:

- Permanent system documentation and affected owner-system/event docs after their adapters exist.
- `handoff_dispositions.md` and the source-of-truth map, updated to mark each item implemented, explicitly queued with reason, or rejected with reason.
- Final system completion audit covering every adapter, death reason, decision family, AI scenario, asset consumer, localisation surface, cleanup path, and accepted improvement finding.

Acceptance criteria: the final documentation must describe actual call sites and consumers, not merely available helpers. No plan may remain ambiguously accepted and unresolved when completion is claimed.

## Accepted depth that should not be expanded

### Meaningful player tradeoffs

Classification: `rejected-by-spec` for another completion-scope decision family; `optional-future` only after a separately accepted owner mechanic creates a concrete new need.

The ordinary category already covers preparation, reserve release, imports, route repair, convoy and airlift relief, evacuation, extraction, requisition, concealment, corridor negotiation, open/controlled/transit/closed reception, distribution, integration, resettlement, voluntary return, enforcement, and forced repatriation. Costs draw from political power, trains, convoys, equipment, fuel, aircraft, and air experience, while outcomes trade stability, war support, reception load, famine pressure, Condemnation, and population safety. `fm_requisition_safer_state`, `fm_conceal_crisis`, `fm_maintain_extraction`, `fm_enforce_closure`, and `fm_forced_repatriation` provide materially different harmful or coercive alternatives rather than cosmetic variants.

Do not add another decision family until the existing twenty AI scenarios prove that these choices are reachable and meaningfully ranked.

### Cohort, route, closed-border, and blockade integrity

Classification: `rejected-by-spec` for another route/cohort layer or weaker proof contract; retain audit coverage of the accepted implementation.

The aligned global cohort arrays preserve origin, current host, destination, owner, amount, source, and status. Safe resettlement rebinds the actual destination without creating population, voluntary return requires persisted origin and eight safety/protection proofs, and forced return uses a separate unsafe-policy contract. Exact transfer requires the conservation identity `origin debit = route deaths + survivor credit` and logs route deaths without a second debit.

Closed borders no longer erase a flow. `fm_close_border` resolves one persisted cohort, derives a trapped share, registers trapped population, submits famine pressure, applies political costs, and records relief-obstruction evidence. The blockade trigger requires valid state, owner and controller at war, island, isolation, maritime dependence, route or port disruption, convoy or escort shortage, no humanitarian corridor, and insufficient local food. This is sufficient proof depth; do not weaken it to a single island or at-war flag.

### Historical and regional connections

Classification: `optional-future` only under FM-O2; additional profiles are not required for current completion.

The fifteen profiles already connect the mechanical system to Soviet 1932 memory, Henan 1942 and policy famine, Bengal 1943, Vietnam and Java 1944, Greece 1941, Leningrad, the Dutch Hunger Winter, early-1940s Spain, Irish memory, Ceará, Congo extraction, Ethiopian occupation/policy, and nuclear winter. These cover extraction, wartime transport, blockade/siege, occupation, environmental shock, colonial policy, institutional memory, and regional vulnerability without imposing fixed casualty totals.

The research bibliography and historical-profile matrix provide an adequate basis. Memory profiles require live pressure, historical-window profiles require map/date/controller and causal proof, policy analogues require current policy structure, and nuclear winter requires explicit registered state and Air evidence. Do not add more historical profiles merely to lengthen the list. A future profile is justified only when a concrete implemented owner system exposes a distinct causal seam not represented by the current fifteen.

## Optional-future extensions

### FM-O1: additional owner-specific narrative variants after all required adapters close

Classification: `optional-future`.

After FM-R1 and FM-R2 are implemented and audited, an existing owner may add a small narrative variant for a genuinely distinct local institution, treaty, relief network, border memory, or political faction. It must reuse the shared pressure, cohort, and report contracts; it must not create a parallel meter, fixed death total, or new random-event registration. No such variant is needed for current completion.

### FM-O2: more historical profiles only from concrete new mechanics

Classification: `optional-future`.

A future event or system may supply a new map/date/policy profile if research and an exact owner adapter prove a distinct causal structure. Catalog-only concepts, uncertain state mappings, and historical totals are not sufficient. The present fifteen-profile matrix is complete enough for this implementation.

## Rejected-by-spec proposals

Each item below is classified `rejected-by-spec`:

- A full shared famine or migration scripted GUI.
- A third famine/migration mapmode for routes, cohorts, reception, or return.
- A new shared random-event ID, Event 149 replacement ID, event-pool registration, or pacing weight.
- A whole-world periodic state or country scan.
- Fixed historical mortality, migration, or survivor totals.
- Placeholder report art or an unwired asset presented as implementation completion.
- Random-neighbor, arbitrary-destination, or otherwise fake migration routes.
- Movement counted as a death, route deaths debited twice, or population credited without a measured origin debit.
- A country package, focus tree, formable, super-event, portrait, 3D model, or unit package for this shared system without a separately accepted need.
- Fabricated sources for catalog-only Events 118, 120, or 131.

## MCP evidence boundaries

The review used the required read-only MCP routes and no rewrite tool.

- Event 149: current `hoi4.event_inspect` for `chaosx.nr149.1` timed out after 180 seconds. `hoi4.event_render` returned `EVENT_RENDERED_PARTIAL`, but its selector fell back to unrelated vanilla `AAT_Sweden` nodes rather than the absent target. Therefore MCP does not prove Event 149 retirement; direct source absence and the catalog row are the current evidence, and the event-engine conclusion remains unresolved at this route.
- Ordinary decisions: current `hoi4.gui_inspect` for `decision_view` timed out after 180 seconds. `hoi4.gui_render` returned `GUI_RENDERED`, but its readable SVG metadata says `GUI window decision_view was not found` and models no elements. This is not layout or click-region acceptance.
- Exactly two mapmodes: current inspection and render evidence is recorded in FM-R6. The installed package has no dedicated scripted-mapmode inspection/render route, so base map geometry and hardcoded GUI approximation remain separate evidence.
- Weighted logic: the mandatory `chaosx_ai_probability_auditor` completed inspect, twenty-scenario evaluation, one sensitivity sweep, and a current/current compare. FM-R4 records their exact artifacts and unresolved typed-fixture boundary; no source-only balance claim is made.
- Technology trees: no technology or doctrine surface belongs to this system. The installed package has no Technology Tree Viewer; no technology conclusion or replacement evidence is claimed.

## Parent implementation order

1. Finish the currently routed achievement evidence and active owner-adapter patches, then rerun their focused audits.
2. Resolve the report-consumer ownership conflict without adding a random-event ID or pool entry.
3. Run the complete twenty-scenario probability inspect/evaluate/sequence/compare pass through the read-only AI probability auditor and patch only evidence-backed parity or ranking defects.
4. Retain the completed Event 149 retirement and confirm the final source still contains no competing runtime transaction.
5. Rerun completion, localisation, decision/mission, adapter/country, achievement, and documentation audits against the final source snapshot.
6. Retain the mapmode MCP limitation explicitly unless readable surface-specific artifacts become available.
7. Mark the goal complete only if no accepted plan, adapter, report consumer, achievement disqualifier, AI scenario, catalog row, or cleanup path remains unresolved.

## Parent handoff

Design problem: the shared system is deep enough, but its public API reaches too few authoritative owner transactions at the review snapshot, its report-art family lacks gameplay consumers, several achievement disqualifiers lack producers at the review snapshot, and weighted AI comparison is incomplete. Event 149 retirement was a required finding but was resolved during this review.

Recommendation: do not expand. Treat this as a closure-with-blockers handoff, close FM-R1, FM-R2, FM-R3, FM-R4, FM-R6, and FM-R7, and retain the already completed FM-R5 retirement.

Research basis: the accepted bibliography and fifteen-profile matrix already connect famine and movement to extraction policy, siege/blockade, colonial and occupation systems, wartime transport, environmental shock, institutional memory, and regional vulnerability. No additional research branch is necessary before closure.

Implementation surfaces affected: existing owner event/effect transaction points, shared famine adapters, achievement evidence effects/triggers, existing report assets and an already-approved carrier if one exists, current decision AI weights, two existing mapmodes, and final documentation/audits. The authoritative workbook row 149 is already aligned.

Open questions:

1. Which existing non-pool report or notification carrier can satisfy the accepted incident/report requirement without allocating a new event ID?
2. Which currently implemented integration-matrix owners will be completed in this tranche, and which are genuinely absent catalog concepts that must remain unwired?
3. Can the installed probability route complete the exact twenty scenarios and compare, or must the unresolved timeout remain a completion blocker?
4. Can the hardcoded mapmode consumer yield readable, surface-specific GUI evidence, or must that evidence boundary remain external?

Prior addendum status: the planning-stage improvement closure is resolved as design guidance and should not trigger another expansion pass. This file is the only current post-implementation improvement addendum for this system.

Promotion recommendation: keep this file in `docs/plans/famine_and_migration_system_plans/` while FM-R1 through FM-R7 are open. Do not copy the optional or rejected material into the source specification. After implementation, fold only any accepted design clarification needed to resolve the report-carrier conflict into `docs/specs/famine_and_migration_system_specs/`; record completed implementation facts in permanent system documentation and then close or supersede this plan.
