# Event032 site-work probability baseline and owner-patch comparison

Report date: 2026-10-09.
Disposition: read-only baseline and mandatory same-scenario comparisons delivered for parent final review; native eligibility, transaction behavior, and balance acceptance remain incomplete.

## Outcome and ownership

All four requested candidates were inspected and evaluated, and `hoi4.probability_compare` was executed against the immutable before decision/mission sources and the current owner-integrated sources using the preserved named scenario payloads.
All four comparisons report `assumptionsChanged = false` and `adapterChanged = false`.
The original 35-case fixture was not overwritten.
The five before snapshots retain their recorded hashes and protected read-only attributes.
No numeric AI weights or balance targets were chosen or changed by this auditor.

The four `ai_will_do` bodies are identical before/current after removing whitespace, and their file-local base constants remain 8.
This source fact does not establish unchanged native choice behavior: the owner changed eligibility and transaction gates.
MCP results are `score_only`, with unresolved conditions; they are willingness scores, not click probabilities, mission success probabilities, or evaluation cadence measurements.
There is no complete native-eligible two-division world in the original fixture.

The parent explicitly accepted the part5 concrete-garrison alternative: two country-owned divisions in the actual rogue state at decision entry and due success, identical for human and AI.
Supply observations remain outside that accepted success condition.
This is not a live supply claim, railway/organization proxy, or AI movement order.
The parent retains implementation, world-fact/transition ownership, spec reconciliation, and final acceptance.
The audit does not block nonweighted receipt work.

Only this report and the outcome evidence JSON were added during the resumed turn.
The original fixture had been added during the earlier baseline turn.
No gameplay, tests, assets, localisation, skills, or other owners' files were edited.
No Git commands, game launch, log access, agent spawning, or agent messages were used.
Read-only installed-game documentation and source references were consulted as required.

## Preserved evidence

- [Original fixture](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/docs/plans/032_missiles_plans/evidence/site_work_20261008/site_work_probability_scenarios_2026-10-08.json>): 122346 bytes; SHA-256 `55d82cfaf95514069e2df899ed458fcc05630ada2a6848cd0f36fcb07a6bbc0d`.
- [Before manifest](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/docs/plans/032_missiles_plans/evidence/site_work_20261008/before/snapshot_manifest.json>): physical shared working tree before the site-work changes, not an accepted-design promotion.
- [Outcome evidence](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/docs/plans/032_missiles_plans/evidence/site_work_20261008/site_work_probability_outcomes_2026-10-09.json>): inspect/compare/evaluate/sweep identities, revisions, scenario hashes, artifact URIs and hashes, per-case score/eligibility rows, comparison deltas, sweep points, unresolved findings, and the original division-placement observations.

New output paths were checked absent before creation.
All resumed-turn JSON analysis artifacts were retrieved with contiguous byte-range continuations and their assembled SHA-256 values verified before interpretation.
The outcome JSON retains their authoritative MCP artifact links; its compact rows are evidence extracts, not replacement gameplay or scenario truth.

### Immutable before5 identities

All five files have protected attribute value `524321`, `ReadOnly = true`, and a current raw hash matching the manifest.

| Logical source | Before raw SHA-256 |
| --- | --- |
| Decisions | `003371566277556825f1850d124d986fa75d2fdcf86171a5882cb9621abe822c` |
| Missions | `54e07f433a7d970d2e317637a049dc73cd6f0a1f94ccb78a19d15dd0b3de6602` |
| Missile constants | `926d3cbfd5efc51576238b11d93b90b1770e366fd649d5b3cdc4b9645fe0f52e` |
| Operations triggers | `fe6bba308fe0b92380d4573f5eec8637a804395f245a907ceb86b2848229b430` |
| Operations effects | `50a48865aa2c33575493ed0904f3cfdeea350df72f9bd41db374f98789d2ab91` |

Current raw decision hash: `8011714d946f7f14730458226e3c13e7e821ae0fba58d08148e792dc762bb527`.
Current raw mission hash: `d647ccba132c5a5ec5673bb5d5e1ebfe1a076423de6634cf1d5d46dca5594bcf`.
Current operations effects hash: `e2c6de2c648318652b3cae08852357a64ac4be5d0550dd619b77368866696be3`.
The outcome JSON records the current survey/recovery helper and constant hashes as well.

The supported source binding used the logical gameplay `path`, real immutable `snapshotPath`, and the raw `expectedSourceHash` for before; after used the real gameplay path and expected current raw hash.
All five snapshots were source-read, but the native snapshot contract binds the selected main file, not a historical whole-workspace overlay.
Shared helpers/constants resolve from the current index.
The unchanged operations-trigger and missile-constant hashes and the recorded referenced-helper provenance must therefore be kept alongside this limitation.
Effects, payment/refund transitions, and every original helper dependency were not replayed as a frozen historical engine world.
The original fixture contains earlier WIP notes, including a stale statement that live decision/mission files still matched before; preserve those bytes and use the manifest, raw observations, and this report as the evidence reconciliation.

## Source and accepted-design findings

The relevant accepted scope comes from the user's site-work instructions and explicit parent review, not merely a spec directory, timestamp, status label, or existing WIP.
The source-design review included part2 site/program rules, part5 decisions/missions, part6 AI/probability, the probability scenario matrix, decision/mission prompt, acceptance criteria, test matrix, traceability, README, manifest, and closure material.

- Part5 survey action/failure requirements include progress-sensitive resource return.
- Part5 line 686 explicitly permits nearby supplied divisions **or** a concrete-garrison condition; the user's parent-reviewed two-owned-division route selects the latter.
- Part5 lines 708–713 describe possible supplied-division/supply mission requirements, not authority to add an undocumented supply primitive to this accepted alternative.
- The test matrix `MISSION-01` names a 60-day survey, and `MISSION-04` names a 14-day recovery with two divisions in the rogue state.
- Part6 line 421 requires a protected interior state to outrank an exposed capital when both are valid; final eligible score ordering remains unresolved here.

### Frozen physical source

[Before decision source](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/docs/plans/032_missiles_plans/evidence/site_work_20261008/before/common/decisions/032_missiles_decisions.txt:57>) shows survey costs 300 manpower / 40 support equipment / 250 fuel behind strict `>` custom-cost predicates, and debits before `missiles_begin_survey`.
The old survey start/cancel helpers have no paid actor/site receipt or progress refund.
That ordering permits debit before a refused helper start; it does not prove an observed duplicate debit.
The frozen recovery decision at line 1416 charges 1200 manpower / 140 infantry equipment / 15 command power with strict `>` predicates and no start garrison gate.

[Before recovery mission](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/docs/plans/032_missiles_plans/evidence/site_work_20261008/before/common/decisions/032_missiles_missions.txt:145>) has a human division requirement and `is_ai = yes` exemption.
It has no supplied-force predicate.
The old recovery completion helper does not make the entire outcome contingent on due/garrison/current actor-context-site proof.
The 60/14-day due helpers and 120/30-day native mission timeouts are distinct source facts, not measured timing distributions.

### Current owner-integrated source

[Current survey decision](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/decisions/032_missiles_decisions.txt:57>) calls the guarded survey wrapper instead of debiting first, and its available/custom-cost gates use the selected-project and shared quote predicates.
[Survey receipt triggers](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/scripted_triggers/032_missiles_survey_triggers.txt:30>) require current payment/generation, actor `id`, site pointer/id, duration, nonnegative paid quantities, and an unsettled receipt.
The funded gate additionally requires `missiles_survey_fully_paid`, positive measured paid components, and exact equality to the frozen quoted components.
The mission retains due and current valid target/holding checks.

[Survey accounting](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/scripted_effects/032_missiles_survey_effects.txt:14>) reads native `manpower_k * 1000`, `num_equipment@support_equipment`, and `fuel_k * 1000` before/after payment or credit.
Paid/refunded quantities derive from those native deltas, not a nominal API-success amount.
The source freezes quote 300/40/250, retires the receipt before refund credit, floors progress-proportional pending credits, and leaves unobserved credit pending or quarantines invalid accounting observations.
These are current source findings; this probability audit does not prove those effect transitions or runtime rounding/holding behavior.

[Recovery gates](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/scripted_triggers/032_missiles_recovery_triggers.txt:5>) use `divisions_in_state` on the actual rogue state through a computed floor of minimum 2 minus 1.
Entry checks program management, positive rogue context, registered rogue site, the concrete native garrison, no active recovery/order, and inclusive 1200/140/15 affordability.
The due mission uses current actor/context/site receipt proof and the same garrison gate without an AI exemption.
[Recovery completion](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/scripted_effects/032_missiles_operations_effects.txt:1716>) rechecks receipt, due, and garrison through the goal helper before the outcome.

[Cost getters](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/scripted_localisation/032_missiles_site_work_localisation.txt:5>) use the same component affordability predicates for ready/blocked display branches.
[Cost text](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/localisation/english/032_missiles_decisions_l_english.yml:217>) reads ordinary quote caches.
Source constants, quote-refresh effects, getter branches, affordability predicates, and payment inputs are wired to the stated amounts; native display/cache freshness, equality affordance, debit, and refund parity are not established by score-only results.

## Named scenario contract and completeness

Actor: hypothetical GER; date: 1936.1.1.
Survey interior target: state 53 Oberbayern, GER owned/controlled/core, infrastructure 3.
Survey capital target: state 64 Brandenburg, GER owned/controlled/core, infrastructure 4, capital.
Vanilla history establishes GER capital 64 and those state definitions; this is not a measured live campaign.

The preserved fixture contains 35 unique cases: eight survey-decision intents, four survey-mission intents, twenty recovery intents, and three sweep fixtures.
The same twenty recovery records are reused for decision and mission sets.
Cases include the survey 299/39/249, 300/40/250, 301/41/251 boundaries; active duplicate; invalid state; no program; core/major interior versus capital; human and AI 0/1/2 owned divisions with supplied/unsupplied observations; recovery 1199/139/14, 1200/140/15, 1201/141/16 boundaries; lost/scuttled site; no crisis; peace and war urgency.
Due/not-due survey cases retain their exact saved dates and caches.

All 22 recovery observations, including the two sweeps, explicitly name division owner GER, exact target state, and country-owned count.
The matrix's 0/1/2 divisions are in state 64; lost-site case names state 69 with count 0, owner/controller CZE; scuttled state 64 has count 0.
Recovery cost/urgency/no-crisis observations have two GER-owned divisions in state 64.
Supply observations were not submitted as invented native predicates.
Other countries, national division totals, iterator world pools, external strategic factors, and campaign transitions are incomplete.

The original recovery registry `missiles_launch_site_states` is empty, and new positive rogue context/id and recovery actor/context/site receipt inputs are absent.
Recovery decision records already carry `missiles_site_recovery_active`; they are not fresh start worlds.
The force sweep, conversely, omits that active flag despite a due-mission label.
Stored state scopes lack the evaluator's exact `var:` binding names, root/state numeric getter facts are unbound, and date strings do not resolve numeric `global.date` operands.
Those deficiencies must not be promoted into eligible two-division scenarios.

### Conditional v2 fixture: not created

The parent authorized hypothetical root native id 1 as an equality fact, not a measured GER id, and a real fixture registry containing state 64 with context 71, recovery actor 1, receipt site 64.
A coherent future pair also needs separate fresh-entry versus active/due mission worlds, exact numeric actor/state getters, registered rogue state flags, properly bound stored scopes, native date operands, stockpiles, and genuinely numeric survey paid/frozen-quote facts.
These accepted setup facts remain queued, not silently inserted into the preserved fixture.

Complete source eligibility is not supported by the observed evaluator path: it reports `set_temp_variable`, `subtract_from_temp_variable`, and `meta_trigger` as unbound compound triggers, and cannot resolve the relevant compound stockpile blocks.
This is a source-execution/representation limitation, not only a missing positive context number.
No complete v2 was evaluated or saved, no helper-return truth was assigned, and no primitive/adapter key was invented to force a pass.

## Probability results and mandatory comparisons

Adapter version: `hoi4-1.19.2.v1`.
Installed version verified by MCP: Operation Postern 1.19.2.0, checksum d245.
Both adapters expose raw score and three-valued eligibility, but no normalized probability, sequence model, or time distribution.
Discovery's empty required-input list is not completeness evidence.
Only the four requested candidates were analyzed; there is no whole-workspace probability graph or complete native action-choice denominator.

### Baseline evaluation findings

- Survey decision: base 8, major factor 2, core factor 2, capital factor 0.5, and non-manageable program factor 0 are source/MCP trace facts.
  Final eligible interior/capital scores are unresolved; do not substitute hand multiplication as an MCP result.
- Recovery decision: MCP returns raw willingness 8 for peace and 16 for war, including invalid/unaffordable force worlds whose eligibility remains unresolved.
  No active crisis is excluded with score 0.
- Survey mission: four baseline cases return raw 8 with unresolved eligibility, including not-due and invalid-state intents.
- Recovery mission: raw 8 in peace and 16 in war for nineteen unresolved cases; no crisis is excluded with 0.
  Equal 0/1/2-division and supply-observation scores do not prove equal availability or success.

Earlier decision evaluations: `probability-784d3e74357ab2247c19e5bf` (survey) and `probability-04b56f12e9c0a74c27ba995a` (recovery).
Their authoritative JSON hashes are respectively `d43e972df4ef2fcd1ffde35d8fe182a74f7847bee176bdd798e231d61ffd30ed` and `2fe1bc552cf2f2b8aee9820bf78ca3c08bff346579dd06fee64af049d853a3fc`.
Resumed narrower baseline mission evaluations: `probability-c4c17cfc3a2fbadfcdb7f0a0` and `probability-8cb7a554f86807114b3cb0d4`.
Their result identities and full artifact links are in the outcome evidence.

### Matched comparison ledger

| Named set | Cases and compared candidates | Compare analysis | Result |
| --- | --- | --- | --- |
| `E32_SURVEY_DECISION_BASELINE_2026_10_08` | 8 cases; both audited decisions | `probability-4a1a37be63c1812133ef4054` | Partial; survey score deltas unresolved except already-excluded zero cases; active duplicate/no-program become excluded |
| `E32_RECOVERY_DECISION_BASELINE_2026_10_08` | 20 cases; loyal-forces decision | `probability-3a63007964aee9c1f00e3a71` | Partial; current fixture cases all excluded |
| `E32_SURVEY_MISSION_BASELINE_2026_10_08` | 4 cases; survey mission | `probability-52e418786c07e844ddfbd0a5` | Partial; current unfunded/missing-receipt worlds excluded |
| `E32_RECOVERY_MISSION_BASELINE_2026_10_08` | 20 cases; recovery mission | `probability-4487c793f3935f039fd16fba` | Partial; current missing-receipt worlds excluded |

Exact scenario hashes, in that row order:

1. `f322664be53c35a648c57885de9da2ba456b6384d07a40855d3608c8fc481574`
2. `f52b7c45cdac69e8e04e0677846e5d6fb7d7ca9d468857959ec7a5f6e5a83059`
3. `c41b3d52d2628f71848d0e16a2966a82204795b650b301316042252017723f51`
4. `699f51832e87e533146a2f691752a7ff9a0654163e5eba33eebe8496aed1af81`

Decision hashes match the earlier baseline evaluation hashes; resumed mission baseline evaluations match their comparison hashes.
Both sides of each compare use exactly the same saved payload, including labels, dates, actors, targets, flags, caches and uncertainty declarations.
The survey-decision compare retains its original two-candidate pool; the other compares select the single relevant audited candidate, identically before/after, to remain bounded.

Recovery decision and mission deltas are -8 for peace cases and -16 for wartime lost/scuttled/urgency cases, with 0 delta for no active crisis.
Survey mission deltas are -8 in all four original cases.
These are eligibility-suppressed raw values, not reductions in numeric `ai_will_do` tuning.
The tool's `UNRESOLVED_ANALYSIS_INTRODUCED` findings describe additional unbound source/fixture analysis, not confirmed engine regressions.
Archive/current path provenance also causes added/removed AST attribution for identical weight blocks; direct bounded block comparison establishes their unchanged numeric contents.

Compare authoritative JSON artifact SHA-256 values, in ledger order:

1. `1ee1b2e491fc98c8c51bfd64a2849f348ee18c18f2beb20652c715f06c6859ed`
2. `bd3f46ec14ef9773ea4ce5994695460e205f3e530d8b80f00213dc75b0d57dfe`
3. `a7084ea81d9ba3f0e8adde6a09f22fd8672aa48e3e3973e78d8d951e7692dd91`
4. `ed6023a1865b2817129e1f9bef9b600081c2e6812b9153636938ba53820b38c3`

The outcome evidence retains each complete MCP URI, before/after analysis id, source identity/revision, raw/eligibility row, unresolved condition, and native comparison/unresolved visual artifact.

## Bounded threshold sweeps

All six before/current sweeps completed using the saved three-step ranges, one relevant candidate per sweep, and no pairwise expansion.
Each cost sweep has nine one-axis points; each force sweep has three, for 42 points total.
No breakpoints or rank reversals were returned; single-candidate ranks are not evidence of relative balance.

| Boundary | Before analysis | Current analysis | Interpretation |
| --- | --- | --- | --- |
| Survey 299/300/301 manpower, 39/40/41 support, 249/250/251 fuel | `probability-7937cd812384f31496acc1c4` | `probability-13a159fea285d99be530855b` | Scores remain unresolved; no cost boundary proved |
| Recovery 1199/1200/1201 manpower, 139/140/141 infantry, 14/15/16 command | `probability-eabc0882e5af473bd56db2f7` | `probability-b330979c199738188b0970f0` | Before raw 8, current 0; incomplete active/context world masks cost semantics |
| GER-owned divisions in rogue state 64: 0/1/2 | `probability-05aae785b8fdc23f4a7a48aa` | `probability-5543ca8eb8cbe9a4fbb5eb78` | Both return 0; missing active flag and compound native division/meta semantics prevent threshold proof |

The saved sweep source/scenario hashes and all JSON/threshold/unresolved artifact links are in the outcome evidence.
These sweeps are adapter evidence only: no affordability pass, exact equality payment pass, garrison success pass, or supplied-force conclusion is claimed.
No simulation/sequence was used because neither a supported timing distribution nor a random custom pool/transition model was declared.

## Exact capability and unresolved boundaries

Required probability inspect/evaluate/compare/sweep routes are connected and responded in this resumed turn.
No recurring workspace-routing discovery timeout occurred.
The preceding turn's pending exec handle 104 could not be recovered: exact local result `Script error: exec cell 104 not found`.
That lost handle does not prove the server operation failed; its outcome remains unobserved, and the resumed survey-mission evaluation was narrowed to the one requested mission.

There is no exposed `hoi4.mission_inspect` route.
The earlier standalone decision inspect without scenarios rejected the request with `Decision inspection requires declared scenarios at scenarios`; that is an argument-shape rejection, not a successful lifecycle audit.
Required weighted inspect evidence exists separately.
Earlier explicit render attempts returned `PROBABILITY_ANALYSIS_STALE`; refresh evaluation returned the cached analysis, and no stale-render pass is claimed.
Resumed compare/evaluate/sweep calls themselves emitted retained native visual artifacts; this does not repair that earlier explicit-render limitation.
Adapter-advertised local `docs/research/probability-adapter-evidence.md` / `fixtures/probability` were not found in the mod repository, so they are a package-reference gap, not invented documentation.

Concrete unresolved facts include native country existence and owned/controlled-state iterator worlds; `scope.CONTROLLER`; `array.ROOT.missiles_launch_site_states`; exact `scope.var:missiles_survey_site_state`, `scope.var:missiles_rogue_site_state` and `scope.var:missiles_recovery_site_state`; numeric `global.date`; actor/state `id` equality; active mission facts; positive rogue context and receipt values; compound `has_equipment`; native `divisions_in_state`; and the temp-assignment/meta-trigger execution chain.
Availability is partly source-expanded with three-valued logic, but custom-cost/native payment, actual click selection, native mission lifecycle, completion effects, stockpile rounding, refunds, movement, and external strategic world behavior are not established by the raw-score adapter.
No missing condition was filled with `candidateOverrides`, scripted-helper truth, invented native primitives, or fabricated measured ids.

## Documentation evidence retained from required reading

Offline wiki and installed-game documentation were consulted through live reference/context/search/read routes and direct source reads where needed; no Paradox web access or logs were used.
The following answering sections and source revisions were retained during the baseline work:

| Source | Read section | Revision |
| --- | --- | --- |
| Installed `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/_documentation.md` | lines 1–46: available/visible, country THIS and target FROM, target root/target checks | `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019` |
| Offline `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md` | lines 284–336 cost and 357–374 AI score rules | `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162` |
| Installed `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md` | lines 2648–2662 `divisions_in_state`: COUNTRY-owned divisions in named state; lines 3835–3843 equipment | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| Installed `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/dynamic_variables_documentation.md` | lines 427–430 and 469–471 manpower getter/units | `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda` |
| Offline `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md` | line 1250 manpower, line 1522 fuel, and line 147 state-division context | `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06` |

Native custom-cost text/trigger is not itself a payment effect; the source must authorize and perform manual debit.
Installed `divisions_in_state` explicitly counts divisions owned by the country in scope, supporting the accepted concrete-garrison boundary without asserting supply status.
Vanilla history source reads included GER capital declaration and states 53/64 owner/core/building definitions.
An earlier wrong-revision wiki read yielded `REFERENCE_REVISION_STALE`; the cited answering wiki cost/AI sections above were read under their correct revision, and the rejected read is not additional coverage.

Skills used: `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-event-planning` for the named spec/scenario contract.
No skill was changed.

## Parent review disposition

- Delivered: frozen physical before evidence; preserved original named fixture; baseline score/uncertainty evidence; four matched owner-patch comparisons; six bounded threshold sweeps; source/getter review; hashes and native artifacts.
- Implemented by owner, observed in current source only: survey paid/native-delta receipts and progress refunds; no-first-debit wrapper; funded/frozen quote gate; concrete two-owned-division entry/due recovery route; current receipt actor/context/site guard; inclusive quote predicates; unchanged numeric weights.
- Accepted and queued: coherent paired-v2 setup facts authorized by the parent, pending a supported source/world evaluator; no alternate truth shortcut accepted.
- Incomplete: positive eligible interior/capital ordering, native 0/1/2-division boundary, exact quote/display/payment parity, actual duplicate/debit/refund/lifecycle transitions, and any numerical AI balance acceptance.

No gameplay simplification was made by this auditor.
The evidence limitations and conditional-v2 omission are explicit above; they prevent a full eligibility/balance completion claim.
Return to the parent for final review without selecting tuning or blocking the nonweighted receipt implementation.

## Continuity follow-up after receipt-bound tightening

Date: 2026-10-09.
Disposition: four requested comparison calls completed; compact result classification persists, but detailed numeric continuity is blocked by artifact provenance retrieval.
This section and the new `continuityFollowUps` outcome entry append later observations without replacing the earlier source hashes, findings, or artifacts.

The original 35-case fixture remains 122346 bytes with SHA-256 `55d82cfaf95514069e2df899ed458fcc05630ada2a6848cd0f36fcb07a6bbc0d`.
The before5 files still match their recorded hashes, retain protected attribute value `524321`, and remain read-only.
Both current main files retain the earlier decision hash `8011714d946f7f14730458226e3c13e7e821ae0fba58d08148e792dc762bb527` and mission hash `d647ccba132c5a5ec5673bb5d5e1ebfe1a076423de6634cf1d5d46dca5594bcf`.
Their complete-byte equality preserves the previously reviewed numeric weight bodies, amounts, and main-file garrison wiring; no tuning was chosen.

### Later dependency observations

- Survey triggers: prior `7fdc70580c9ca925c159576cf1465a65aa4f541cbbec57c86f6259c1f4048716`; current `e77071d12c2631c5baaa69034620e429009ccca0af4e2c43e984cce51c144410`.
- Survey effects also changed physically: prior `fc6fe965ed3e6611543f42ea5da918f6df70b508986acda313d028674100acf8`; current `01d379679a43827c06458082b68b3ed5450ec37ca58556e72a6a8ea4362e634c`.
- The other nine recorded source hashes match the earlier observations.

Read-only source inspection shows the survey receipt requires present positive frozen quotes and paid amounts no greater than each quoted component.
The pending-return gate checks closed payment/settlement and payer identity, present component balances, nonnegative pending/credited amounts, and credited plus pending no greater than observed paid.
The survey effects source invokes that pending gate before credit at lines 100–104.
These observations are not native payment/refund execution proof, and this follow-up did not execute the parent's malformed-pending source case.

### Same-request comparison continuity

Exactly four `hoi4.probability_compare` calls were made with the same original saved payloads, pools, before snapshot bindings, after main-file hashes, outputs and refresh settings as the preceding four comparisons.
No new probability evaluation, sweep, inspect, fixture, candidate override, helper truth, or narrower comparison request was added.
The initial probability-inspect requirement was satisfied by the preceding audit; this bounded follow-up reuses that inspected surface.

| Named set | New compare analysis | Unresolved items: earlier → current | Compact classification |
| --- | --- | --- | --- |
| Survey decision | `probability-3c4eafcfaba86988e231780b` | 170 → 170 | Partial; 0 eligible, 11 excluded, 5 unresolved candidates |
| Recovery decision | `probability-dadf61b1f47ffb93a50e2c40` | 17 → 17 | Partial; 0 eligible, 20 excluded, 0 unresolved candidates |
| Survey mission | `probability-8ad12fbd27117deaa7996a48` | 18 → 24 | Partial; 0 eligible, 4 excluded, 0 unresolved candidates |
| Recovery mission | `probability-3107904d236dd0b58064996b` | 14 → 14 | Partial; 0 eligible, 20 excluded, 0 unresolved candidates |

All four returned scenario hashes exactly match the corresponding earlier hashes listed above.
All returned eligible/excluded/unresolved-candidate summary counts and partial analysis classifications match the earlier results.
The survey mission's six additional unresolved items are retained as a changed uncertainty total, not described as an identical finding list.
The documented adapter remains a willingness-score surface; no click probability, complete eligible v2 world, native funded receipt, or observed stockpile/refund proof is claimed.
The compact tool results omit per-case raw scores and comparison deltas, so exact row-by-row score/support/delta continuity could not be verified after the artifact failure below.

Decision compare source revision: `9be3b76253b9d6b20dc81df0886310560bdd2589da5fea4ab613e7946347aef0`.
Mission compare source revision: `5ee8712c15bd44c79e8f5579fb2b8b677b437ecd13ff6e43b748d976f432c768`.
All four new comparison requests, returned summaries, artifact URIs/hashes and prior/current identities are appended to the outcome JSON.
Their artifact hashes are server declarations only; the new artifact bytes were not successfully retrieved or independently hash-verified.

### Exact retrieval blocker and bounded retry

The comparison route returned successful partial results without a routing timeout or comparison blocker.
The first authoritative JSON resource read failed at offset 0 / length 8192; exactly one narrower read retried the same artifact at offset 0 / length 4096 and failed again.
Exact terminal route error: `resources/read` for server `hoi4_agent_tools` returned `Mcp error: -32603: Artifact provenance manifest is unavailable`.
Failed artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ed1c77db057f356ab2936e2d3a057186e25b5cd8c579588f68bff03578e172db/fcc60d7b3886fb451fd5837f16d4545b98abe8f62d6e0c49006d004859960a14/probability-3c4eafcfaba86988e231780b.json`.
The outcome JSON retains the full initial/retry URIs and exact error text.
No further native calls, alternative transport, artifact-root workaround, new comparison, or other provenance recovery was attempted after that retry.

Parent-reported source-test evidence: 16 site cases, full 175 expected, 43 CBRN plus 11 Event21; the new actual-source malformed-pending case reportedly retains balances without minting.
Those counts and that source-case finding were reported directly by the user, not rerun or independently observed by this auditor, and do not establish native funding behavior.

Only this report and the existing outcomes JSON were appended.
Skills used for this continuity follow-up: `chaos-redux-subagents` and `chaos-redux-decisions-missions`; neither changed.
No gameplay/source, tests, localisation, assets, skills, Git, game launch, logs, or agents were modified or used beyond the authorized read-only source/reference observations.
