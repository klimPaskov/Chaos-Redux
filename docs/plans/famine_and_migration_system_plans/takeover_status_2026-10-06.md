# Famine and migration takeover status

Review date: 2026-10-06.
Verdict: incomplete.
This record supersedes the six stopped-thread checkpoint documents for current status without modifying their existing dirty hunks.
It distinguishes committed source repairs, preserved round-3 drafts, and missing engine evidence.

## This pass

| Commit | Result |
| --- | --- |
| `f3148c8e7df5a3101e89938557cbfbd1d4fda453` | Caller-owned return storage for famine profiles/adapters, occupation conduct, migration recording/resolution, and shared transfer reception deltas. Continuous stage clocks, retirement clock cleanup, conserved reserve release, and a once-only zero-consumption fee refund. |
| `8540b5be9fe129783bc84ea5abbc3ae69a8ebb43` | Shorter famine/migration decision names and plain report, requirement, and achievement prose. |
| `562b9afcb60488573eed9b834fad84c7c15e4c3c` | First status/reference/draft-review checkpoint and six-case source regression baseline. This document's final revision supersedes that checkpoint's test count and source inventory. |
| `0bca71eb15cfc2af783be2bafcc21378e7a5d8b6` | Outermost decision callback storage for movement/relief/corridor results and proofs, consistent temporary relief-delivery copies across donor/recipient scopes, and the seventh regression case. |
| This document's commit | Current status, reference evidence, design decisions, inherited-draft review, source regressions, and the spec README status pointer. Resolve its exact hash with `git log -1 --format=%H -- docs/plans/famine_and_migration_system_plans/takeover_status_2026-10-06.md`. |

The implementing agent reviewed each published commit with `git show`.
The commit workflow used a temporary index based on the observed HEAD, owned paths or isolated hunks, `commit-tree`, a compare-and-swap ref update, and reconciliation of only the affected real-index entries.
No workbook, exported CSV, unrelated staged hunk, desktop window, or game session was changed.

Design reasons are in [agent_decisions_2026-10-05.md](agent_decisions_2026-10-05.md).
Direct reference sections, paths, line spans, source hashes, and the baseline save inspection are in [source_review_2026-10-06.md](source_review_2026-10-06.md).

Published runtime files: `common/decisions/famine_decisions.txt`; `common/scripted_effects/famine_core_effects.txt`, `famine_adapter_effects.txt`, `humanitarian_capture_effects.txt`, `migration_core_effects.txt`, `migration_decision_owner_effects.txt`, `migration_forced_movement_effects.txt`, and `migration_adapter_effects.txt`; the surgical four-line shared edit is `common/scripted_effects/civilian_transfer_effects.txt`.
The callback follow-up also touches `common/decisions/migration_decisions.txt`, `common/scripted_effects/famine_relief_effects.txt`, and a single caller declaration in `common/scripted_effects/humanitarian_corridor_effects.txt`.
API documentation updated: the Markdown pairs for famine core/adapters, humanitarian capture, migration core, migration decision owners, and migration forced movement.
Player prose updated: `localisation/english/famine_l_english.yml` and `migration_l_english.yml`.
Review artifacts updated: this status, the decisions/reference/draft-review records, `.tools/test_famine_takeover_20261006.py`, and the spec README's status link.
Existing report pictures, category icons, map sprites, and achievement DDS assets are reused, with no asset file change.

## Verification of takeover claims

| Takeover claim | Current source result and evidence |
| --- | --- |
| All 18 static inbox defects | Their intended fixes remain in the current decision nesting, country/state guards, neighbour tests, and shared date-helper calls. Publication: `7cbd3faea`, `fa46d0deb`, `705cd90c4`. |
| Country-wide migration policy scope | Open Departure, Restrict Departure, and Controlled Medical Reception keep country-wide preflight, without a fictional selected state. `4759ff8bc`. |
| Inclusive cost bundles and paid continuation | The 25 legacy-cost actions and the separate Open Reception action retain their complete affordability/debit bundles. Existing five measured-zero-origin refunds remain, alongside Open Reception's failed-setup refund. Reserve release adds a sixth measured-zero-origin/consumption outcome and does not refund after positive stock consumption. |
| Reception intent and privacy | Submit, preparation, acceptance, measured passage, rejection/expiry, and front control cleanup retain their owner-specific row handling. Requested/prepared/agreed presentation is present. `705cd90c4`, `b62afd492`. Native colour and hover acceptance remains open. |
| Exact population-loss ownership | The current famine mortality caller declares shared loss result/applied fields and reads the observed debit once. `0cfdf83c2`. |
| Integration terminalization | Whole-group state and national reception debit, completed status with zero amount, and national integration credit in that order remain in source. Invalid ownership or insufficient loads fail preflight. `c3de4fd62`, `b62afd492`. |
| Hostile capture and liberation | The existing control-change callback dispatches bounded flight and one food assessment with minimum population/request and date-based cooldown. Owner recapture creates no extra flight. Conduct output storage is repaired in this pass. `3f7d984e6`. |
| Relief obstruction condemnation | Refusal or an unanswered deadline condemns only a receiver that could have accepted the whole request. A hostile interruption of relief attributes the obstruction to the capturing country, once per generation. `e5e7354b2`, `90ea4334c`, `b62afd492`. |
| First group of displaced people | The history count is initialized before the first group and the repair flag clears only after aligned reconciliation. `112204230`. Further return-storage gaps identified by this pass are repaired separately. |
| Food scores and reserves | The 2.50 normalizer, half-target starting stores, shortage draw, exhaustion contribution, one-step stages, and mortality severity cap remain in source. `cce88b947`. Continuous qualifying intervals and removal of dormant elapsed time are repaired in this pass. |
| Hunger Lines integration | The famine-owned adapter is called only after Event 014 reports successful setup, reads its bounded live node registry/intensity, and applies one 120-day context and flight request per state/window. `22f54df93`, `216e825e0`. |
| Stage-sensitive reserve response and AI | The shared reserve gate accepts visible strain or shock. All 28 non-mission decisions retain AI blocks. Stage flags are mutually exclusive. `5d7e331ba`. No numeric AI weight changed in this pass. |
| Regional war-profile causes | Local-war checks, Bengal's joint food region, and Leningrad's local front requirement remain in source. `8f29ac0f6`, `216e825e0`. |
| Event 149 and popup spam | Event 149 remains retired. Famine and migration are event-free systems. Their owned chains generate zero report/news popups, and report selector flags change the standing category header. |

The older `inbox_fix_results.json` describes the state before the takeover published the cost and reception-intent drafts.
Its working-tree-only wording is historical rather than a current source gap.
The stopped Codex thread's famine `last` field is empty and supplies no independent completion verdict.

## Preserved round-3 work

Disposition: unresolved publication ownership.
At task start, five gameplay files already contained uncommitted round-3 changes dated 2026-10-05.
The user's shared-tree instruction says to leave hunks written by other agents alone, so those changes were preserved and excluded from this pass's commits while their ownership was queried.

| Preserved file | Draft behavior |
| --- | --- |
| `common/script_constants/famine_core_constants.txt` | Dated outbreak/disaster context tuning and associated component contributions. |
| `common/scripted_effects/famine_core_effects.txt` | Local-war collector, expiring food contexts, shared profile gates, concealed-blockade mortality dispatch, context cleanup, and transition clock resets. |
| `common/scripted_effects/famine_adapter_effects.txt` | Accepted outbreak/disaster context setters. |
| `common/scripted_triggers/famine_core_triggers.txt` | Shared China/Ceara/Congo cause gates. |
| `common/scripted_effects/humanitarian_achievement_effects.txt` | Credited-country `PREV` comparisons and tracked concealed-mortality disqualification. |

The source completion auditor found no remaining confirmed defect in these draft behaviors after the separate caller and clock fixes.
[round3_draft_review_2026-10-06.md](round3_draft_review_2026-10-06.md) gives their exact API, cause, and achievement contracts and the permanent documentation still needed when they are published.
The local-war collector's new caller-storage line remains with its unpublished dependent hunk.
This report does not label the round-3 source or its missing paired API/system documentation as committed completion.

The stopped-thread checkpoint docs, mapmode audit hunk, nine untracked handoffs, and the Event 012 owner's `migration_adapter_effects.md` hunk remain untouched.

## Meaningful checks and evidence limits

Command: `python .tools/test_famine_takeover_20261006.py`.
All seven bounded production-source tests pass against the current working tree.
They cover conservative helper-return storage, the three cause gates, context expiry and recovery, stage-clock reversal and fresh recovery steps, stock conservation at the relief limit, rejected reserve requests, and the exact refund branch replayed on the same country/state.
An isolated raw-source snapshot of commit `0bca71eb15cfc2af783be2bafcc21378e7a5d8b6` passes the five tests for published repairs and explicitly skips the two tests requiring unpublished round-3 cause/context definitions.
The additional case executes the real reserve transfer and the production donor-copy/recipient-publication slices, checking equal measured debit/credit, conserved stock, unscoped temporary returns, and correct durable delivery amounts.
The fixture reuses the existing Event 035 parser/runtime and fails on unknown reached commands.
It models scoped native facts and conservative temporary call frames, while registry, report/modifier/achievement consumers, map adjacency, daily reserve simulation, mortality, and live engine execution remain outside this bounded fixture.
The context score arithmetic is therefore a source model, not proof of full daily outcome timing.

The report-colour audit ran with JSON output against the current tree and found no famine, migration, or Event 149 report/news reachability findings.
Direct inspection also confirms all seven owned report-header summary keys are plain text.
The two header layouts and their existing DDS/sprite wiring remain intact, with no asset production or GUI layout change in this pass.

The decision auditor verified the payment profiles and existing refund guards and independently reviewed the added reserve conservation/refund behavior.
The completion auditor verified selector/mapper agreement, the 1936 live-shock gates, exact blockade identity/generation attribution, caller storage, and clock cleanup.
Those are source audits rather than native gameplay results.

MCP outcomes in the Luna specialist sessions:

- One `reference_context` result successfully identified the offline Data structures temporary-variable section, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
- A bounded decision reference context call did not return after more than 115 seconds and was caller-terminated. Detailed relevant sections were read directly.
- Famine header `gui_inspect` with explicit scene/dormant flags, three separate scenario IDs, normal state, and generated scenarios disabled did not return after more than 64 seconds and was caller-terminated.
- The matching `gui_render` at 1920 by 1080, scale 1, did not return within the 52-second caller bound. No PNG, crop, annotation, or validation JSON was returned. Header visual acceptance is unresolved.
- The two source-scoped `decision_ai_will_do` probability inspections, one per decision file with `refresh:false`, remained pending through approximately 124 seconds of observed yields plus unclocked review time and were caller-terminated. Neither returned an artifact, revision, hash, or tool error.
- No current evaluate/sweep/compare result exists. The older GER/FROM-state-64 cost cases returned partial decisions with unresolved scope/native inputs and unresolved custom cost. The mandatory same-scenario comparison remains blocked, not waived.

The exposed specialist inventories have no health/version/task-negotiation route.
No helper expansion, repository-wide state-flow query, unsupported HTTP route, or server modification was used.

## Exact orchestrator live checks

Use separate copies of `qa_001_fresh_head.hoi4`, inspected as USA on `1936.1.1.12`, normal difficulty, installed version 1.19.2.
The preserved draft scenarios below require the current working tree including those explicitly listed drafts, and cannot be presented as acceptance of a clean checkout of only this pass's commits.
Console probes are fixture setup, and direct field setup does not prove natural campaign reachability.
Do not combine the independent fixtures into one accumulating campaign.

### 1. Quiet start and category headers

Load the baseline as USA and run one day without firing a scenario.
Open Famine and Migration map modes, then Decisions.
USA must have no food/displacement category merely because historical memory anchors exist, and neither system must open an incident popup.
On a crisis fixture, inspect every category-header scene at 1920 by 1080 and scale 1: famine generic/blockade/relief and migration wartime/closed-border/nuclear/return.
Only one picture/title/summary may show in each header, text must fit, and no raw localisation or flag key may appear.
The shorter selected-state and requesting-country titles must also fit with a long state or country name.

### 2. Hunger Lines Low and Maximum

In separate baseline copies, open Settings, select scenario #010 The Hunger Lines, and launch it once at Low and once at Maximum.
Use the owner's ordinary valid target setup rather than setting its launcher flag by hand.
Expected: successful Event 014 setup yields live node states, food reserves and daily food scores there, flight pressure, and real migration groups when the minimum 1,000-person movement is reached.
Low should show supply strain after roughly a week with half-target starting stores, then acute shortage as stores run down.
Maximum should pass through the visible warning stages toward famine over roughly six weeks without relief.
The Famine map must colour the stages, affected owners must see their food category, and Migration must distinguish origin pressure from actual hosted arrivals.
Repeat launch inside the same state's 120-day context window: that state's food/flight request must not stack again.
If Event 014 cannot set up a valid node registry, Settings must report the reason or choose a valid target through that owner's preflight.
The previous live snapshot set `cannibalism_manual_scenario_setup_failed` before famine was called, so a repeated failure is an Event 014 owner item.

### 3. Hostile capture, first group, and owner recapture

Load the baseline and use `tag ITA`.
Check `eval_trigger 842 = { is_controlled_by = ETH }` and `eval_trigger ITA = { has_war_with = ETH }`.
Then run `eval_effect ITA = { set_state_controller = 842 }` and advance several days.
Expected: one bounded war-flight request, one queued food assessment, a first aligned displaced group when a safe destination exists, and no lasting ambiguous/misaligned registry flag.
`global.migration_cohort_history_count` must exist and group count must increase without double debiting population.
Restore control with `eval_effect ETH = { set_state_controller = 842 }`.
Expected: no additional capture-flight request from owner recapture.
Compare one capture under protective conduct and one under harsh conduct in separate fixtures: conduct must change flight even if occupier ideology is shared.

### 4. Reserve release and six refund paths

Use an affected state with stores and enough resources for its quoted release fee: 20 political power, 50 support equipment, and 500 fuel.
Record its stock and resources, take Release Food Stores, and let its three-day work complete.
Expected: one fee debit, a stock debit matching rationed food, protected rationing, relief presentation, and the existing relief mission behavior.
Repeat with rationing relief already at 32 points and a request of ten days: only two days of food can be accepted at 1.5 relief points per day, with unused stock retained.
For a paid action whose relief reaches 35 points before completion, expect zero stock debit and exactly one full fee return.
Repeat the callback or wait another day: it must grant no second refund.
At one resource short, the complete fee line must be red and the decision unavailable.
Repeat the five existing zero-origin failures for famine evacuation, migration evacuation of vulnerable people, evacuation of workers, voluntary return, and forced repatriation: the quoted fee returns only when the measured origin debit is zero.
Positive movement, cancellation, lost control, or failed funded foreign delivery must not invent a blanket refund.

For emergency imports, escorted sea relief, and airlift, record donor and recipient stores before the funded delivery completes.
Expected: equal measured donor debit and recipient credit, positive recipient `famine_relief_last_delivery_debit` and `famine_relief_last_delivery_credit`, the relief proof and header, and the existing mission/achievement progression.
The delivery must not move native population or add Deaths, and a failed route must produce no false delivery success.
Repeat a protected corridor relief delivery to verify the same result survives its extra wrapper call.

### 5. Continuous stage intervals and retirement

In a baseline copy run:
`eval_effect 362 = { famine_initialize_state = yes set_variable = { famine_input_production = 100 } set_variable = { famine_input_transport = 100 } set_variable = { famine_input_need = 100 } famine_register_active_state = yes }`
Advance one day at a time.
Expected: at most one committed stage per qualifying interval, with no collapse through several stages on consecutive days.
Lower the three inputs to zero for fewer than the current recovery days, then raise them again, and later lower them again.
Recovery must need a fresh uninterrupted interval after the renewed shortage, and renewed escalation must not reuse a preceding candidate clock.
After full stable recovery and retirement, start the same fixture again.
Expected: the next candidate starts from a fresh clock, with no credit for time spent dormant.

### 6. Outbreak/disaster contexts and three profile gates

These fixtures cover the preserved round-3 drafts.
In separate baseline copies set one exact registered state's food shock through its real outbreak/disaster owner and verify the adapter accepts its complete food proof.
Expected: outbreak context ends 30 days later, disaster/Acid Rain context ends 60 days later, repeated accepted requests extend the date without adding a second copy of each component, and recovery follows expiry.
Quiet states outside the active registry must remain untouched.

For gate-only checks, run these independent console probes, then select and apply the profile in that state:

```text
eval_effect 607 = { famine_initialize_state = yes set_variable = { famine_food_pressure = 10 } set_state_flag = famine_extraction_active famine_select_historical_profile_id = yes famine_apply_historical_profile_context = yes }
eval_effect 935 = { famine_initialize_state = yes set_variable = { famine_food_pressure = 10 } set_variable = { famine_last_pressure_source = constant:humanitarian_pressure_source.natural_disaster } famine_select_historical_profile_id = yes famine_apply_historical_profile_context = yes }
eval_effect 295 = { famine_initialize_state = yes set_variable = { famine_food_pressure = 10 } famine_select_historical_profile_id = yes famine_apply_historical_profile_context = yes }
```

Expected: Henan under CHI/PRC gets profile 3, Ceara under BRA gets 12, and non-core colonial Congo under BEL/FRA gets 13.
Reset food pressure to zero and reassess: each cause gate must fail and no date-only crisis may start.
A non-Chinese Henan, non-Brazilian Ceara, or non-Belgian/French Congo must fail the corresponding tag gate.
For natural reachability, repeat with extraction/concealment/movement restriction, drought, and colonial/war/camp causes supplied by their actual owners rather than console fields.

### 7. Blockade concealment and country attribution

These checks cover the preserved achievement draft.
Create a genuine tracked blockade famine, conceal its crisis, and let a positive famine loss apply.
Expected: the credited owner's `humanitarian_achievement_blockade_concealed_mortality` flag is set for the exact state/generation, and Break the Blockade cannot unlock after later relief/recovery.
A different controller is disqualified only when its own tracked blockade identity matches.
Run the same starvation from a different chain ROOT to confirm it does not credit or disqualify that unrelated ROOT country.
An unconcealed pulse, zero applied loss, wrong state, or wrong generation must not set the flag.
Starting a new tracked blockade attempt must clear the previous attempt's disqualifiers according to its existing generation contract.
Also repeat the extraction/recovery/logistics recorders with a different ROOT and verify the actual credited country receives their progress.

### 8. Reception, integration, safe return, and forced movement

Create two hosted groups in one country with real origin/host identities through the actual evacuation paths.
Offer passage through one enemy front, prepare that exact receiver's services, and accept the request.
Expected: requested, prepared, and agreed colours/hover text appear only to the receiver owning that front, with no arrivals credited before real transfer.
Reject or let the response lapse: only an otherwise safe receiver with room for the whole request is condemned.
An older and newer request at one front must survive each other's row cleanup.

Integrate one complete hosted group.
Expected: one fee, one state/national reception debit, completed zero-amount group, one integration credit, and unchanged native state population.
Repeat integration of that same group: it must not consume the second group's load or add credit again.
Voluntary return and resettlement must retain the resolved group's correct origin, host, amount, and source after helper return.
Run a Camp-owner forced transfer using its normal action and compare native origin debit, destination survivor credit, route deaths, both reception deltas, and conservation residual.
The exact neutral transfer must finish or compensate once, with no duplicate receipt or survivor grant.

### 9. Wartime regional profiles

Use the separate observer campaign from check 10, pause on `1943.5.1`, save it as `qa_famine_1943_fronts`, and use `tag JAP`.
Check `eval_trigger JAP = { has_war_with = ENG }` and `eval_trigger JAP = { has_war_with = RAJ }`.
For a missing war, declare it through the ordinary diplomacy screen in this fixture so the actual war callbacks run.
Run `eval_effect JAP = { set_state_controller = 997 }` to hold Arakan while Bengal remains British/Raj-controlled, then allow bounded anchor processing.
Expected: states 430 and 431 both qualify for the Bengal food-region context.
Return Arakan and end the local disruption: a British war elsewhere alone must not maintain that regional cause.
At Leningrad, compare a real enemy-held neighbouring siege ring to a Soviet war elsewhere.
Expected: only the local siege/food cause opens that profile.

### 10. Long-run balance and persistence

Observe a 1936-1943 war campaign, then compare saved state/group histories around capture, relief, integration, return, and condemnation.
Supply strain must cause no famine deaths, acute shortage must be materially milder than famine, prepared/relieved states must improve, and prolonged isolated/repressed crises must lose a noticeable but bounded population share.
Confirm no historical anchor starts a famine merely from the 1936 date and no ordinary occupation automatically collapses its population.
Check active-registry performance during large wars and verify tracked achievements and profile/group state survive save/reload.
These live observations are still required by spec Part 8 and are not established by source arithmetic.

## Simplifications, omissions, and blockers

No gameplay route, achievement, cost component, visible mechanic value, or asset was removed or replaced by a fallback in this pass.
The source fixes preserve the accepted separate systems and exact population accounting.
The workstream is still incomplete for these explicit reasons:

1. The five inherited round-3 dirty gameplay files require ownership resolution before publication. Their required permanent context/profile/achievement API documentation is queued with that publication, not silently marked complete.
2. Mandatory current same-scenario probability comparisons remain blocked by the actual route/fixture limitations above, including the earlier affordability and stage-urgency changes.
3. Current header visual artifacts were not returned. No successful PNG/validation review or current matched visual acceptance can be claimed.
4. The exact live checks above remain orchestrator-owned, including SCN-010 successful launch, conservation/refunds, metadata lifetime in native execution, natural profile/achievement reachability, persistence, and long-run balance/performance.
5. Event 014 setup/Settings feedback and its SCN-010 wording/catalog update remain with that owner. The existing `catalog_changes_pending.md` gives the requested text. No workbook or CSV was edited.
6. Camp-owner cohort-origin resolver calls at `camp_repression_rework_effects.txt` lines 5350 and 5405 need equivalent caller-storage review by that owner. Their files were not edited.
7. Generic strategic bombing has no documented callback, Events 118/120/131 remain absent, and the previously excluded event-specific hooks retain their recorded owner boundaries. These accepted exclusions are not claimed as implemented adapters.
8. The probability auditor covered the 25 legacy-cost IDs in source only. Open Reception, corridor acceptance, and corridor rejection still need their own scenario evaluation, alongside the decision/donor cases. Four donor/contract-absent minimum-weight branches are dormant under the ordinary target gates. They remain defensive guards pending the required numeric comparison and do not make an invalid action selectable.

Skills used: `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-subagents`, `chaos-redux-shared-git-commit`, `chaos-redux-scripted-gui`, `chaos-redux-event-assets`, `chaos-redux-save-inspection`, and the probability auditor's `chaos-redux-mtth` reference.
No skill was created or changed because helper-output lifetime, exact payments, sparse scheduling, and shared-index publication are already covered by the existing skills.
