# Event 032 Loyal-Force Recovery Contract

Status: `unresolved` read-only audit handoff. The parent owns implementation and the AI probability baseline/compare. No gameplay source, localisation, assets, tests, Git state, game process, logs, or agent tasks were changed or launched.

## Acceptance basis and scope

The parent supplied accepted scope at `docs/specs/032_missiles_specs/032_missiles_spec_part_5_decisions_missions_and_scenario.md:684-713`: sending loyal forces requires nearby supplied divisions or a concrete garrison condition, starts timed recovery, and carries site-damage/launch risk; the goal may require state control, a supplied-division count, maintained supply, and prevention of a launch.

The parent also specified ordinary decision-category presentation with a static picture and no dedicated GUI. This audit covers the force/supply contract, mission lifecycle, and AI actionability for `missiles_send_loyal_forces` and `missiles_site_recovery_mission`.

## Findings, sorted by severity

1. High: `missiles_site_recovery_mission.available` has an `is_ai = yes` success branch, so AI can complete recovery after the due date without any loyal division in the site state. The human branch requires `divisions_in_state` to exceed `@m32_mission_recovery_division_floor` (1, therefore two or more), but the AI branch bypasses that exact goal and its tooltip. This violates the accepted human/AI force parity and MISSION-04's two-division outcome.
2. High, conditional on literal supply being mandatory: the installed trigger and dynamic-variable documentation exposes no current local division-supply reader. The accepted concrete-garrison alternative is source-ready and precise, but it proves force ownership/count/location only; it cannot be described as proof that the divisions are supplied. Do not substitute national supply averages, `num_of_supply_nodes`, fuel, organization, or a railway by silently calling them live division supply.
3. High: if the shared two-division gate replaces the AI shortcut, no inspected documentation or vanilla precedent provides an AI order that targets this runtime-selected rogue state. The documented `put_unit_buffers` strategy takes a static `states = { <IDs> }` list; vanilla CHI uses literal state IDs. `front_control` modifies an existing frontline and does not assign divisions or create a front, so it is not an actionable order for a friendly rogue site. A same-gate implementation gives AI the same success test, but source review cannot establish that AI can move forces there.
4. Medium: the accepted prose leaves the force prerequisite at decision start underspecified. Part 5 says “nearby supplied divisions or a concrete garrison condition”; MISSION-04 says to send forces and station two divisions in the rogue state, describing the success objective but not a nearby-force count or radius at selection. The current decision can charge its costs without any force check. Do not invent a nearby radius or a second threshold.
5. Medium: `missiles_complete_site_recovery` checks target validity only around the site-recovery sub-effect; command-control gain, completion receipt, and incident closure then execute unconditionally. Normal mission availability also checks the goal, but the completion helper itself does not revalidate the active/due/garrison contract before publishing success. A stale or direct helper invocation could therefore record success after its target is invalid.
6. Medium cost edge: all three custom affordability checks use strict `>` against the displayed payment amounts. Exact balances of 15 command power, 1,200 manpower, and 140 infantry equipment are therefore rejected despite matching the quote. The cost uses three spendable types and has matching icons, so it is under the four-type cap; make the shared affordability check inclusive and keep display/payment aligned.

## Verified source-ready garrison condition

Use one country-scope helper for the accepted concrete-garrison route:

```text
missiles_recovery_garrison_is_present = {
	missiles_recovery_target_is_valid = yes
	divisions_in_state = {
		state = var:missiles_recovery_site_state
		size > @m32_mission_recovery_division_floor
	}
}
```

This is a presence test for at least two divisions belonging to the current country in the saved target state. The installed documentation says `divisions_in_state` is a COUNTRY-scope trigger and counts divisions in the specified state owned by the current country; the offline wiki documents `state = <scope> / <variable>`. Vanilla `POL_pacify_peasants_repeatable` uses `state = var:peasant_state_var` directly, and Event 032 already uses the same dynamic-state form. The installed documentation's `Supported Targets: none` describes the trigger target annotation; the variable is an argument to `state`, as confirmed by the wiki and vanilla precedent.

Use the same helper in mission completion availability and inside `missiles_complete_site_recovery` before granting the recovery result. Preserve the separate due-date gate. `missiles_begin_site_recovery` currently sets the local due date to 14 days; the native mission timeout is 30 days, so the successful goal has a 16-day resolution margin and no same-day timeout race. This accepted garrison condition does not require a second click after the goal is achieved.

No exact helper for *live supplied divisions* is supported by the inspected docs. The `unit_organization` trigger is a per-division 0–1 organization ratio, not supply. Existing Chaos Redux patterns make the distinction explicit: Event 024's state-control, garrison, organization, and capital-rail rule is labelled a supplied-division proxy; Event 028 says no installed trigger reads division supply and uses a local capital-rail garrison proxy. Those are declared proxies, not proof of each division's current supply. If literal supply is an acceptance gate, the required engine reader or an explicit owner-approved proxy definition remains missing.

## Mission and category lifecycle

`missiles_program_management_category` is an ordinary category with `GFX_decision_cat_picture_032_missiles`, no dedicated scripted GUI, and category visibility gated by `missiles_country_can_manage_program`. The rogue phase exposes five action families in this source block: code rotation, isolation, loyal forces, negotiation, and scuttling; isolation/scuttling are targeted to the rogue site. The send decision hides while its recovery mission is active, preventing duplicate active recovery orders.

On selection, `missiles_begin_site_recovery` snapshots `missiles_rogue_site_state`, sets the 14-day due date, and marks recovery active; the caller then activates the native mission. The mission's non-selectable `available` condition is its success condition: the offline mission documentation says this condition executes `complete_effect`, while timer expiry runs `timeout_effect`. Cancellation covers loss of program authority, closure of the rogue crisis, loss of the recovery-active flag, or invalid target. Losing the troop-count condition does not cancel the mission; it simply prevents success until the 30-day timeout. Timeout clears the recovery project but leaves the rogue crisis available for its other responses/retry after cooldown.

The five-action phase is within the six-primary-action guidance, and this route adds one active mission at most. Player-facing values are limited to the clear two-division condition and the due date; there is no unexplained value dump or long prose. `missiles_site_recovery_mission_forces_tt` accurately states the human two-division/control condition but not the AI bypass. The decision's entry tooltip states only that the site must remain under national control, matching its current start gate. No supply status is shown or tested.

## Cost, localisation, AI, and cleanup notes

The quoted payment is 15 command power, 1,200 manpower, and 140 infantry equipment. The localisation uses `£command_power`, `£manpower_texticon`, and `£infantry_equipment_text_icon` for all three spendable types; no literal resource-name fallback or hidden fourth/fifth payment was found. The exact-balance strict-comparison issue is listed above.

The decision is phase/incident gated, requires the rogue state variable, and refuses a site outside national control or one that is scuttled. Its AI score is high and doubled in war. The mission's own `ai_will_do` is not the action path because `activation = { always = no }` and the decision activates it directly. The current AI bypass undermines both the force tooltip and the accepted AI criteria that AI can assault/secure. No probability analysis was run: the parent explicitly owns baseline and compare. `ROGUE-01`–`ROGUE-08` concern incident selection/probability, while `ROGUE-LIVE-03` checkpoints assault and MISSION-04 is the precise two-division recovery case; neither currently supplies an AI movement scenario.

Timeout/cancellation clears recovery-active state, due date, and target state; the retry remains incident-gated and cooldown-limited. No free-unit or repeated-success loop was found in this bounded path. Failure does not directly damage or launch from the site; it leaves the rogue crisis unresolved, so the other crisis responses and launch threat remain. Confirm that this persistent risk is the accepted failure consequence before adding a new consequence.

## GUI evidence and route limit

The required read-only GUI routes were attempted for `missiles_program_management_category`. `hoi4.gui_inspect` reported `inspectedElementCount = 0`, a missing-window validation diagnostic, and workspace-wide graph/diagnostic truncation; its artifact is [gui-inspect.6bbfa766d9e380e2.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a3053e6de91734b7664a0806a5e68abd565b7c8d718e027d31e4ab426544eccd/441cebd6b8d791476c743d9fa1008f5280f70dbebbbc4ce91beb4222a455f55e/gui-inspect.6bbfa766d9e380e2.json). `hoi4.gui_render` returned a 707-byte SVG and no inspectable category elements, not a decision-list visual; artifact: [missiles_program_management_category-full.svg](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5aec214eb23da73ee3f4f537197443153e7462df109375ee03062d41b3cbe12e/3acff190892cc4fc29b48ab80d7574f2e7b05b9b67969ae8deaf6e4377a710c6/missiles_program_management_category-full.svg). The ordinary static-picture category is not a scripted-GUI render target, so there is no valid in-game visual judgment or before/after comparison from these artifacts; this is a route limitation, not a claimed visual pass.

## Evidence references

- Accepted basis supplied by parent: `docs/specs/032_missiles_specs/032_missiles_spec_part_5_decisions_missions_and_scenario.md:684-713`.
- Rogue-command design and AI: `docs/specs/032_missiles_specs/032_missiles_spec_part_4_evolutions.md:596-690,786-798`; AI/protection matrix `docs/specs/032_missiles_specs/032_missiles_spec_part_6_ai_and_probability.md:429-465`.
- Acceptance/test cases: `docs/specs/032_missiles_specs/032_missiles_acceptance_criteria.md:242-256`; `docs/specs/032_missiles_specs/032_missiles_test_matrix.md:328-360,578-586`.
- Current code: `common/decisions/032_missiles_decisions.txt:1416-1456`; `common/decisions/032_missiles_missions.txt:13-19,145-189`; `common/scripted_effects/032_missiles_operations_effects.txt:1687-1718,3612-3616`; `common/scripted_triggers/032_missiles_operations_triggers.txt:766-809`; `common/script_constants/032_missiles_constants.txt:432`; `localisation/english/032_missiles_decisions_l_english.yml:156,206,301-303,338-372`.
- Installed decision docs: `common/decisions/_documentation.md:18-22`, revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`.
- Installed trigger docs: `documentation/triggers_documentation.md:2648-2662` (`divisions_in_state`) and `:7686-7694` (`unit_organization`), revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`.
- Installed mission activation: `documentation/effects_documentation.md:661-670`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
- Offline wiki: `Triggers - Hearts of Iron 4 Wiki.md:1279` (`divisions_in_state`); `:147` (`any_state_division`); `Data structures - Hearts of Iron 4 Wiki.md:1608` (`num_armies_in_state`); `Decision modding - Hearts of Iron 4 Wiki.md:465-479` (mission success/timeout/activation); `AI modding - Hearts of Iron 4 Wiki.md:351,360` (`front_control`, `put_unit_buffers`). Revisions respectively `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06`, `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`, `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`, and `917cd261f7da51fe4d8687c5d7663e768a09c5c101ac130ce646bc64637aa818`.
- Vanilla precedent: `common/decisions/POL.txt:831-835` (`POL_pacify_peasants_repeatable` uses a stored state variable in `divisions_in_state`); `common/ai_strategy/CHI.txt:285-311` (`CHI_buffer_in_mainland` uses static state IDs for `put_unit_buffers`). MCP source lookup location revision `18e38bb0987105465caf1c3d50774669152ac064c2b2dd25b81508fe07def2b1` for POL and `f4db858cb8c1aa676788f5b87cec5f295835c747095e4e92e95c07acd104a802` for CHI.
- Existing proxy patterns: `common/scripted_triggers/024_video_game_in_sweden_triggers.txt:1185-1261` and `common/script_constants/024_video_game_in_sweden_constants.txt:239-250`; `common/scripted_triggers/028_asteroid_incoming_crater_triggers.txt:179-208`. MCP source lookup identifies the Event 028 helper at revision `6a66889b7bb44e0f04c162592eb2bcc7c50873faa9e8c54bb3ef1a66fc1a9058`.
- Targeted installed-doc search for division/state live supply returned no reader result; local search of installed `triggers_documentation.md` and `dynamic_variables_documentation.md` found supply-node/vehicle entries but no current division-supply getter. The limitation is bounded to documented script readers and is not a claim about undocumented engine internals.

## Handoff summary

Changed files: this handoff only. No decision, mission, helper, localisation, AI weight, or GUI source was changed. Before/after behavior is therefore unchanged: humans need two divisions in the rogue state after the 14-day due date; AI bypasses that requirement and can receive recovery; live local supply and dynamic AI movement remain unproven. No tests, probability baseline/compare, game launch, or runtime validation were run by this sidecar; probability work belongs to the parent, and live-game validation remains the user's responsibility. Remaining blockers are the literal local-supply reader (if required), a proven AI order for the runtime state target, and the accepted start-time interpretation of “nearby” forces.

## 2026-10-09 bounded post-implementation review

Disposition: `implemented` parent survey/recovery source tranche, with full Event 032 acceptance and native evidence still open.
The preceding 2026-10-08 findings describe historical source and are retained unchanged.
This appendix supersedes their current-status conclusions for the accepted scope.

Acceptance basis: the parent reviewed the initial report and explicitly selected the accepted concrete garrison of two country-owned divisions in the exact rogue state at both order entry and due success.
The current user instruction confirms that choice, the ordinary category/static-picture surface, and parent ownership of final acceptance and probability work.
This route does not claim a local division-supply measurement or an AI movement order.
The source design and implementation record are `docs/events/032_missiles/systems/site_work_transactions.md` and `docs/plans/032_missiles_plans/032_site_work_implementation_2026-10-09.md`.

### Current findings and resolved history

No remaining concrete defect was found in the bounded payment, refund, funding, duplicate, recovery-context, scope, cleanup, AI-parity, or player-text paths after the final zero-return correction.
This is a source review conclusion with the limits below, not whole-event or native-engine acceptance.

- Original findings 1, 4, 5 and 6 are `implemented`: the AI troop exemption is removed; the entry condition is the accepted two-owned-division garrison; every recovery reward/site restoration/closure is inside `missiles_recovery_goal_is_satisfied`; all three recovery costs use inclusive gates and one payment owner.
- Original findings 2 and 3 are superseded as blockers for this accepted route: the parent chose the specified concrete-garrison alternative, which AI can use when its divisions are already present.
No supply proxy or dynamic movement order is introduced.
- The two survey guard defects observed in an intermediate source are `implemented` by the parent: invalid negative pre-observation blocks native debit/credit; quarantine blocks the later credit components of the same pass.
`missiles_quarantine_survey_observation` preserves the first normal anomaly fields and zeroes the uncertain observed output.
These fixes were reread at raw SHA `ee7e5c6c2adc40d9625f926b9112f479acba355077f45749b8f26de174458a23`; they remain in the final source.
- The additional zero-return edge found during this review is accepted and `implemented` by the parent: `missiles_credit_survey_component` now initializes observed credit to zero and enters its query/mutation path only when the requested amount is positive.
A completed or otherwise zero-return survey therefore does not read native stock, create quarantine, or retain a zero pending return.
The final wrapper was reread at raw SHA `e088046c3a372ff849aed03c5484a26cd5fbd04b4f49cdd07dd98e3024ba6c9c`.
The sidecar made none of these source or test edits.

### Actual cost, funding, settlement and scope

Survey display, selection and entry use the centralized 300-manpower/40-support-equipment/250-fuel ordinary quote.
The per-resource colour selectors invoke the same inclusive affordability components, while entry refreshes the quote and rechecks project/target authority before its single measured payment sequence.
The decision wrapper has no second debit.
Recovery likewise uses one inclusive 15-command-power/1,200-manpower/140-infantry-equipment gate before its sole payment owner.

The survey receipt freezes generation, actual payer ID, FROM state pointer/ID, start date, bought duration, quotes and observed removals.
Funding additionally requires a current positive receipt, full-payment flag and positive paid amounts equal to every frozen quote.
Missing, partial, mismatched and quarantined proof cannot establish a funded mission.
The payment owner stops after an incomplete component, and its immediate rollback uses only observed removal.

Cancellation derives unused work from the frozen purchase, rounds elapsed days up and integer returns down, and retires active paid proof before credit.
The 60-day/30-day case yields 150 manpower, 20 support equipment and 125 fuel.
Pending returns require the exact closed payment/settlement ID and actual payer; nonnegative credited-plus-pending amounts cannot exceed each recorded observed payment.
A retry credits only the fixed remaining balance, without repricing or recomputing work.
Duplicate cancellation/completion cannot reopen the retired receipt or mint another return.
Quarantined and malformed holds remain retained rather than being assigned to another payer.
Credit also requires that the recorded country still exists; removal does not invent a successor refund.

The stored survey-state identity uses the previous COUNTRY scope for its receipt comparison, while native mutation stays in the current payer country.
Recovery snapshots the actual current country ID, exact rogue site ID and the context allocated by the existing incident-ID owner.
Entry and goal both use country-scope `divisions_in_state` on the exact state, with centralized minimum 2 converted to the supported strict floor 1.
Foreign divisions do not count.
The due gate is 14 days; the native recovery timeout remains 30 days.
All success effects are inside the matching actor/site/context, current active receipt, due-date and garrison guard.
Rogue closure removes the recovery mission and clears its private receipt/context fields.
The state consumer helpers retain their documented ROOT=programme-country contract at the native decision/mission entry points; refund ownership does not depend on a surviving state or a foreign ROOT.

The pending-return retry is reached through bounded programme/status interactions and exact lifecycle transactions, not a new periodic world/country refund observer.
The parent source still treats actual native stock visibility, equipment producer/variant restoration, mission timing and registration/construction as separate evidence boundaries.
A registration request in the source VM does not establish physical construction or a native acknowledgement.

### Category, mission, cost and text audit

The ordinary category/static picture and five rogue response families are preserved.
The send action hides while the recovery mission is active, and entry refuses another active recovery receipt/native mission.
Survey entry similarly refuses active work, a native survey mission, an unsettled return or quarantine.
Each reviewed action has three spendable cost types with matching native texticons; no hidden fourth/fifth payment, extra category meter or primary action was introduced.
Non-consumed state/garrison requirements remain separate from payment.
The existing `missiles_rogue_command_active` flag has player-facing localisation in `032_missiles_requirement_flags_l_english.yml:14`.

The recovery requirement and goal text now name country-owned divisions and the exact state, matching human/AI source conditions.
The survey description explains progress returns and distinguishes settled, pending and unreconciled holdings.
Its settlement notice displays three actually returned quantities with icons rather than raw receipt values or a telemetry dump.
The native cost base/blocked/tooltip keys are present; blocked aliases reuse the per-resource colour quote.
No additional text-density or cost-icon defect was found in this bounded source slice.
Actual target-row count, spacing, clipping and native UI fit remain unobserved; the accepted full candidate-pool/highest-score requirement also remains open.
No new unsupported GUI request or redesign was made during this review.

### Evidence and validation limits

The parent reports 18 current site-work source cases after the final zero-return change.
The reviewer read the actual separate unavailable-before/same-pass test and the new `test_zero_return_does_not_query_native_stock_or_quarantine_success`.
The latter queues unreadable facts for all three currencies, completes the funded survey at day 60, and asserts unchanged wallets/native-call count, unconsumed query queues, success, no quarantine and no pending return.
The retained unavailable-before case asserts no native debit or credit, unchanged wallet, all three fixed pending balances retained, and unchanged first anomaly.
These are actual-helper source VM checks with injected native facts; this sidecar did not execute tests.

At review time `parent_final_checks_20261009.json` records 176 full Event 032 tests, 43 CBRN cases and 11 claimant cases.
Those aggregate counts precede the final added zero-return case; no final aggregate 177-test pass is inferred.
The latest 18-case rerun is the direct parent/user report.
Native wallet/world queries and effects, mission callbacks, registration/presentation, game precision and actual AI unit placement remain explicit VM limits.

Live `hoi4.reference_context/search/read` verified installed `dynamic_variables_documentation.md:385-387,469-471,557-559` at revision `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda`.
Fuel and manpower readers use thousands and are multiplied by 1,000; the country equipment reader uses the support-equipment archetype.
The offline Data structures sections `1516,1592,1615`, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`, corroborate current fuel, total manpower and country stockpile equipment.
The manpower reader includes army and reserve, so it is not described as a reserve-only getter.
The shared native cost branch source and API documentation were read for the three survey resources.
The offline State-targeted decisions section `576-586` and installed vanilla examples corroborate `state_target = any_owned_state`; no syntax defect was inferred from the older installed decision document's differing heading.

Focused `hoi4.source_lookup` read the guarded payment and recovery-success helpers at source revision `3d64bfe8b1d21978ab8ad19d2fd9ba2f22b473a429ea876318ff4035c85e5396`.
The narrow country-scope payment check returned `SCRIPT_CHECK_PARTIAL`, `valid = null`: syntax/kind/scope checks only, with helper resolution and native argument blocks still unresolved.
It reported 33 findings, 25 omitted inline, 16 unresolved commands and 11 unchecked argument blocks at documentation revision `9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b`.
This is not a full script/native validation claim.
The final credit-only zero guard was source-read and covered by the parent's current source case.

The canonical probability records remain four same-fixture comparisons and six sweeps/42 partial points.
Numeric weight bodies remain unchanged, but the fixture lacks complete eligible paid-survey/garrison worlds and cannot certify native selection or balance.
The latest continuity appendix matches scenario hashes and compact result counts; candidate-score row continuity remains unresolved because resource retrieval reports `Artifact provenance manifest is unavailable`.
Its dependency observation stops at intermediate survey-effects hash `01d379679a43827c06458082b68b3ed5450ec37ca58556e72a6a8ea4362e634c`; it does not certify the final `e088...` dependency.
The parent should retain the final source identity and current guard-test evidence beside that explicitly partial record.
No new probability or agent call was made by this sidecar.

The event comparison remains blocked by `EVENT_GRAPH_ARTIFACT_LIMIT` (96,944,773-byte global graph versus 67,108,864-byte ceiling).
The viewed eight-node options graph contains no project-helper coverage.
The original ordinary-category GUI artifacts remain a missing-window/zero-element route result and provide no native visual acceptance.

### Current raw source identities

The table pins the source reviewed here, including the final parent zero-return correction.

| File | Raw SHA-256 |
| --- | --- |
| `common/script_constants/032_missiles_survey_constants.txt` | `9089b1ac51a34531da95478d5b5f8eed449dfbd2c7da945b70d9bd0f8d90fb9d` |
| `common/script_constants/032_missiles_recovery_constants.txt` | `247e057072c2187b64e03c32a0bf7b1e3957199f704ea77bbd418bdb005c000f` |
| `common/scripted_triggers/032_missiles_survey_triggers.txt` | `e77071d12c2631c5baaa69034620e429009ccca0af4e2c43e984cce51c144410` |
| `common/scripted_triggers/032_missiles_recovery_triggers.txt` | `f657bafa38deeb067aa8681e28300bc7c1ace57a6f319201bc39eadcf769421e` |
| `common/scripted_effects/032_missiles_survey_effects.txt` | `e088046c3a372ff849aed03c5484a26cd5fbd04b4f49cdd07dd98e3024ba6c9c` |
| `common/scripted_effects/032_missiles_recovery_effects.txt` | `cf7e3f65265dbbd3e36c69162eb84fc1159abce9148815e314ff19a0ef160071` |
| `common/scripted_localisation/032_missiles_site_work_localisation.txt` | `7b4aae9de25f381b5c9ab1b710a32930fa3b387f59951d4b2c7ce06e32275b9f` |
| `common/decisions/032_missiles_decisions.txt` | `8011714d946f7f14730458226e3c13e7e821ae0fba58d08148e792dc762bb527` |
| `common/decisions/032_missiles_missions.txt` | `d647ccba132c5a5ec5673bb5d5e1ebfe1a076423de6634cf1d5d46dca5594bcf` |
| `common/scripted_effects/032_missiles_operations_effects.txt` | `e2c6de2c648318652b3cae08852357a64ac4be5d0550dd619b77368866696be3` |
| `common/scripted_effects/032_missiles_effects.txt` | `fe869ff0a30da3fbdfc291aa1526c546bc2eedac1a002d6b66620b9b99097d53` |
| `common/scripted_triggers/032_missiles_operations_triggers.txt` | `fe6bba308fe0b92380d4573f5eec8637a804395f245a907ceb86b2848229b430` |
| `localisation/english/032_missiles_decisions_l_english.yml` | `50328cd4a443c9781612a964e42303c91deff4fed8d6288b631f4c4308d67842` |
| `.tools/test_event32_site_work_transactions.py` | `b2b2dea90bfdd2e517cd768af03b7cd56da5c4b4793fe2469573419cc88a49ed` |

### Open work and sidecar disposition

The complete frozen survey candidate pool/highest-score selection is `accepted and queued` within the full goal; this bounded transaction tranche does not implement or discharge it.
Native construction/registration, native payment/reader/mission physics, ordinary-category visual evidence and complete eligible AI probability scenarios remain open.
Broader Event 032 payload, scenario, asset, achievement and catalog acceptance remains parent-owned and is not closed by this appendix.
No gameplay simplification is accepted or introduced by this review.

Only this original handoff was appended.
No gameplay source, tests, localisation, assets, Git operations, game process, logs or agent tasks were written or run by this sidecar.
Skills reused: `chaos-redux-decisions-missions` and `chaos-redux-subagents`; no skill was created or updated.
Final acceptance remains with the parent, and live game evidence remains user-owned.

