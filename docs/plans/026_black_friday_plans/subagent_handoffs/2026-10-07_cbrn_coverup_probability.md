# CBRN cover-up AI probability audit

Date: 2026-10-07.
Disposition: bounded read-only audit; score evaluation and sensitivity results remain unresolved because domain calls timed out or had no observed response.
Scope: `cbrn_seal_state` and `cbrn_destroy_contaminated_records` in `common/decisions/cbrn_occupation_decisions.txt`.
No gameplay source, parent cost helper, historical snapshot, test fixture, or localisation file was edited.

## Parent scope and current source

The parent requested that the existing weight blocks, action mapping, targets, 30-day re-enable interval, and static AI hints remain unchanged while PP pricing is integrated only through the existing scripted helpers.
The decision source remains untouched and its current local SHA-256 is `7247630690F01A17DF3DDB41C51335984CC17D6E99AB63474129C9CDA741E4F3`.
The matching decision-file provenance hash in the narrow probability inspection is `7247630690f01a17df3ddb41c51335984cc17d6e99ab63474129c9cda741e4f3`.
The shared worktree marks `common/scripted_triggers/cbrn_occupation_triggers.txt` modified by the parent; I did not change it.
An earlier parallel read during patching captured interim hash `0870948142A6FCE77236EED3C79775553C8FB8E01D0F4415026A34EA2CDADBCF`; it was not the current helper version.
I re-read the current physical file and its SHA-256 is `55D9F4CE79911D202F42072F4CC01B59FEAA1315299BE6D0C5A42ADAFBCC5D3F`, matching the latest helper hash recorded in the parent’s 79-case source-test handoff.
This confirms the helper file identity only; I did not rerun the test harness, and the source-model result does not establish native AI-hint or engine behavior.
The parent also reports an in-progress effect-only correction for AI-to-human delayed-settlement payment-time eligibility snapshots; existing decision weights remain unchanged.
That owner-reported correction was not independently inspected or validated here, and no new probability revision, retime artifact, or analysis claim is attached to it.

The current registry records `BF-CBRN-COVERUP-001` and `BF-CBRN-COVERUP-002` as `blocked_pending_evidence`.
Those rows are in `docs/plans/026_black_friday_plans/event26_cost_surface_registry.md:577-578`.
Its source-model matrix declares seal-state ordinary quotes of 40/80/120 PP at Condemnation scores 0/500/1000, baseline-sale quotes of 20/40/60, and Evolution I quotes of 10/20/30.
For contaminated-record destruction it declares ordinary quotes of 60/120/180, baseline-sale quotes of 30/60/90, and Evolution I quotes of 15/30/45.
These are parent-declared source-model cases, not MCP probability results or native-engine observations.
Event 026 remains default-disabled and `NeedsTesting` per the parent; universal, native-row, live, cooldown, save/reload, and multiplayer acceptance remain incomplete.

## MCP calls and retained evidence

The connected HOI4 Agent Tools server-status resource reported version `3.10.0` over stdio.
The workspace is `mod_chaos_redux_ea3b2d67c2c0`.
The selected probability adapter is `decision_ai_will_do` version `hoi4-1.19.2.v1`; its verified game target is Operation Postern v1.19.2.0.a729, checksum `d245`.

| Call | Outcome | Evidence |
| --- | --- | --- |
| `hoi4.probability_inspect`, current source, no explicit pool | Completed, code `PROBABILITY_SOURCE_INSPECTED`; found six active decision candidates, `poolComplete=false`, and ten required paths. | Revision `b1b8a0c83f807e4cf14b6e1b0a69e31b718bd9a38f5de8e02993e50ffd214040`; top-level source hash `7551437660a6977c9ba69b84c4a1520c461a449c6e6a5521b2a762c33114616e`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9d67fd8f8510c8f6dba64d2f857ecf5ee300c1ede0d289299195dd67e102822b/947faacf31b8e7d711599e3d1366bcb55d1cb9711321b1294909736402bb0972/probability-inspect-7551437660a6.json`. |
| Narrow `hoi4.probability_inspect` with exact pool `[cbrn_seal_state, cbrn_destroy_contaminated_records]` | Completed, code `PROBABILITY_SOURCE_INSPECTED`; pool complete for the explicitly scoped pair, with both candidates requiring scenario analysis. | Revision `63fe155f22edc01f9d2bc688ccb6057c77114ac4a1a80d15de5d09b1f451b4f8`; source hash `7551437660a6977c9ba69b84c4a1520c461a449c6e6a5521b2a762c33114616e`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e00ab8066ae40e3039a296a07ca45a4513af5e194055f33586546f3358058cc9/23ca1b59e52f1c63ee9339f6acea3838ee21870d9f198d4a1282d8fe0fbc9d9f/probability-inspect-7551437660a6.json`. |
| `hoi4.probability_evaluate` scenario-schema probe | Rejected the empty set with exact validation: `expected string at scenarioSet.id` and `expected array at scenarioSet.scenarios`. | The next call supplied the required top-level fields; nested scenario semantics remain unverified because no analysis returned. |
| `hoi4.probability_evaluate`, eight route/government cases | Timed out awaiting `tools/call after 600s`. No analysis artifact or scenario hash returned. | Scenario set `cbrn_coverup_route_score_cases_2026-10-07`; IDs listed below. |
| Narrow `hoi4.probability_evaluate`, one autocratic/unrestricted case | Request remained pending with no tool response or artifact when the local wait was stopped for this bounded handoff. This is unobserved, not a confirmed MCP failure. | Scenario set `cbrn_coverup_autocratic_unrestricted_2026-10-07`; no analysis ID, scenario hash, or job handle returned. |
| `hoi4.probability_sweep`, corrected one-case request | The first attempt was rejected because the caller supplied no `scenarioSet.scenarios` array; the corrected request remained pending with no response when the local wait was stopped. No threshold or rank-reversal result is claimed. | Scenario set `cbrn_coverup_autocratic_unrestricted_2026-10-07`; paths requested: `cbrn_occupation_decision_ai.seal_state` and `cbrn_occupation_decision_ai.destroy_records`; no artifact, scenario hash, or analysis ID returned. |
| `hoi4.source_lookup` for both exact decision symbols | Calls remained pending at cutoff; no response or source artifact was observed. | Exact decision-file source revision and spans are retained from the successful probability inspection and local source read. |
| `hoi4.probability_render` | Not called because no evaluate or sweep analysis ID was returned. | No rendered evidence URI exists. |
| `hoi4.probability_compare` | Not called because no weighted source changed; the current decision file was not compared with itself or with the excluded historical snapshot. | No comparison ID exists. |

Both inspect artifacts were retrieved in bounded byte ranges, checked for contiguous offsets and total size, decoded as JSON, and SHA-256 verified against their artifact URIs.
The first artifact was 46,656 bytes and matched `9d67fd8f8510c8f6dba64d2f857ecf5ee300c1ede0d289299195dd67e102822b`.
The narrow artifact was 15,452 bytes and matched `e00ab8066ae40e3039a296a07ca45a4513af5e194055f33586546f3358058cc9`.
No fixture or historical source snapshot supplied an audit baseline.

Reference evidence came from successful `hoi4.reference_context`, `hoi4.reference_search`, and `hoi4.reference_read` calls in the same workspace.
The installed decision documentation is `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\_documentation.md:1-46`, revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`.
The offline Decision modding cost section is `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md:284-336`, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`, section ID `0a37b9f1ad43a16c2d85d25b307d261fcc9e60292b4e164c335c03816535e4d8`.
The offline Decision modding AI section is lines 357-374 of the same revision, section ID `151bbd3b6a875558e43f67a1daa1288c5904dfbedfa09e3fca2e5e42b8ccc58f`.
The offline AI modding article was read locally at `paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md:26-60`, local file SHA-256 `917CD261F7DA51FE4D8687C5D7663E768A09C5C101AC130CE646BC64637AA818`.
The supplementary targeted reference search for that AI article had no observed response and was stopped after the local section was read.
The context bundle reported wiki and game-document coverage available with no omitted or missing sources; the configured `script_doc` source kind was unavailable.

## Candidate pool and scenario completeness

The broad inspect discovered these six active candidates in the source file: `cbrn_admit_accidental_release`, `cbrn_adopt_protected_occupation`, `cbrn_authorize_coercive_security`, `cbrn_destroy_contaminated_records`, `cbrn_permit_inspection`, and `cbrn_seal_state`.
The narrow pool is complete only for the two parent-scoped decisions; it is not a complete country/category choice pool.
The adapter declares `selectionRule=score_only`, `normalizedProbability=false`, `rawScore=true`, and eligibility support with a documented runtime boundary.
The adapter also says selection probability and timing are not modeled, so no click probability can be claimed even from a complete pair pool.

The eight-case evaluation request named:

- `cbrn_seal_state_democratic_first_use`
- `cbrn_seal_state_autocratic_first_use`
- `cbrn_seal_state_autocratic_unrestricted`
- `cbrn_seal_state_autocratic_no_route`
- `cbrn_destroy_records_democratic_unrestricted`
- `cbrn_destroy_records_autocratic_unrestricted`
- `cbrn_destroy_records_autocratic_first_use_only`
- `cbrn_destroy_records_autocratic_no_route`

Those attempted cases used actor/date labels USA or GER at 1936.1.1 and the source-defined first-use or unrestricted route flag; their state objects were empty.
The one-case retry used GER at 1936.1.1 with `cbrn_chaos_warfare_unrestricted_ai_route`.
These are declared scenario labels, not live campaign observations.
The connected probability wrapper exposed `scenarioSet` as an unknown nested type, and the only confirmed nested contract was the top-level `id` string plus `scenarios` array.
The scenario objects also carried `date`, `actor`, `flags`, and an empty `state` by reference to the connected decision-scenario contract; the probability call never returned to confirm those fields’ semantics.

For every attempted case, PP balance, the exact `FROM` state, historical suppression-record variables, quote validity, Condemnation score, and the global universal-cost source arrays were not supplied.
The narrow inspector reported required inputs including `has_political_power`, `scope.FROM`, the current quote-valid output, and the helper operations used to calculate it.
Consequently ordinary/sale eligibility and state targeting remain unresolved in MCP evidence.
The parent registry’s score-0 baseline price cases (seal 20 PP, destroy 30 PP) were not represented in a completed probability scenario.

## Source findings and classifications

`cbrn_seal_state` is declared at lines 234-277 of `common/decisions/cbrn_occupation_decisions.txt`.
It targets `any_controlled_state`, retains the existing nerve-suppression history gate, uses the shared state-cover-up predicate for targeting and availability, calls `cbrn_occupation_execute_paid_coverup`, and retains the 30-day re-enable interval.
Its source weight uses base constant `cbrn_occupation_decision_ai.seal_state` (20) and applies the zero constant when the country is democratic or `cbrn_ai_route_allows_first_use` is false.

`cbrn_destroy_contaminated_records` is declared at lines 279-319 of the same file.
It uses the same state/price/cooldown/action structure, with base constant `cbrn_occupation_decision_ai.destroy_records` (10) and a zero factor when `cbrn_ai_route_allows_unrestricted_use` is false.
The route helpers at `common/scripted_triggers/cbrn_doctrine_triggers.txt:443-457` define first-use and unrestricted route flags; the unrestricted route also satisfies the first-use helper.

The current ordinary PP bases and fixed decision hints are 40 for sealing and 60 for destroying records.
Their source constants are in `common/script_constants/cbrn_occupation_constants.txt:52-80`, and the AI score and zero-factor constants are in `common/script_constants/cbrn_occupation_constants.txt:242-261`.
The decision-file macros are `CR_SC_CBRN_OCCUPATION_SEAL_STATE_PP_AI_HINT = 40` and `CR_SC_CBRN_OCCUPATION_DESTROY_RECORDS_PP_AI_HINT = 60`.
The parent handoff `docs/plans/026_black_friday_plans/subagent_handoffs/2026-10-07_cbrn_coverup_cost_adapter.md` says quotes are recomputed through the existing quote helpers and shared affordability/payment contracts, with the ordinary PP amount scaled by Condemnation and a matching universal-cost source applied before one final quantization.
The relevant current quote and affordability helpers are in `common/scripted_triggers/cbrn_occupation_triggers.txt:357-456`.
The parent-owned helper file is modified in the shared tree; the parent handoff reports 79 source-model cases, and its recorded helper hash matches the current physical file after reread.
I did not rerun that suite, and its source-model cases do not establish native AI-hint or engine behavior.

| Audit question | Finding | Classification |
| --- | --- | --- |
| AI score versus probability | The adapter is score-only and does not model a selection denominator or timing. No normalized selection probability is available. | Score-only capability; scenario outputs unresolved. |
| Effective base values and modifier traces | Source constants are 20 and 10, with the route/government zero factors above. The attempted scenario calls returned no traces, so no effective scenario score or ranking is asserted. | Source values exact; scenario result unresolved. |
| Ordinary versus sale eligibility | Parent test documentation declares exact source-model prices, but no probability evaluation returned a quote/eligibility trace for those cases. | Unresolved for this audit. |
| Native AI saving hint at exact discounted balance | The 40/60 hints remain above the parent-declared score-0 baseline-sale quotes of 20/30. Offline Decision modding documentation says the hint is a literal amount the AI thinks the decision uses and is intended to make it save that amount. No native evidence establishes whether this behaves as an independent gate at PP 20/30. | Unresolved engine behavior; do not infer effective AI affordability from `available` alone. |
| AI validity and positive weight on blocked targets | Source AI weights gate government/doctrine willingness; target history, state ownership/control, prior response/discovery, quote validity, and PP affordability are separate gates. Their runtime combination was not evaluated. | Source separation exact; eligibility unresolved. |
| Dominance, starvation, and rank reversal | No completed ranking or sweep exists. The larger source base value is not a probability ratio and does not establish starvation. | Unresolved. |
| Repetition and exploit risk | The source has a 30-day re-enable interval and a one-response-per-state predicate; native cooldown consumption and broader multi-state AI pacing were not tested. | Bounded source observation; runtime cadence unresolved. |

The game documentation says `available` is checked for current takeability and `target_trigger` selects state targets; it does not establish AI’s internal treatment of the separate saving hint.
The offline Decision modding section says custom costs require a manual debit and documents the hint as a constant amount.
The offline AI modding article describes common `ai_will_do` scoring behavior, while the probability adapter deliberately returns score/rank only for this decision surface.

## Concrete follow-up for the parent

Keep both source weight blocks, actions, targets, cooldown, and the 40/60 hints unchanged as requested.
Before claiming AI can use the sale at exact balance, obtain native evidence for seal at PP 20 with quote 20 and hint 40, and destruction at PP 30 with quote 30 and hint 60, alongside ordinary-price controls at PP 40/60.
Record whether the engine waits for the hint amount independently of the discounted `available` predicate; this audit does not establish that behavior.
Do not tune the hint or weights based on this source-only mismatch.

Once the probability service returns, rerun evaluation with the parent-declared price cases and complete `FROM`/PP/Condemnation/source-registry inputs, then run the corresponding sensitivity and rank-reversal sweep.
Do not report a normalized decision probability or a complete category ranking unless the adapter supplies a complete selection rule and candidate pool.
Keep the registry rows blocked until native row, hint, cooldown, recovery, serialization, and live acceptance evidence is reconciled.
The summary at `docs/plans/026_black_friday_plans/event26_cost_surface_registry.md:222` still describes CBRN occupation as the two-definition Protective Aid action, while the detailed cover-up rows are at lines 577-578; reconcile that summary during the parent’s next registry update.

## Skipped analysis, blockers, and limits

- The eight-case evaluate call timed out after 600 seconds; the narrower one-case evaluate and corrected sweep had no observed response before cutoff and are not labelled failed.
- No effective scenario trace, scenario hash, ranking, sensitivity threshold, rank reversal, analysis ID, comparison ID, or render URI was returned.
- No comparison was run because the weighted decision source is unchanged and the September snapshot is explicitly excluded as a new baseline.
- No simulation was run because no uncertain input distribution was declared; no sequence analysis was run because these are not a declared custom weighted pool with cadence and transitions.
- The adapter’s probability capability does not cover the native saving-hint behavior, and no game launch or log search was performed.
- The supplementary reference search for the main AI-modification article had no observed response; the relevant offline local article was read directly. The reference bundle reported the installed game documentation and wiki available, with script_doc unavailable.

No weights, costs, helpers, actions, targets, hints, source snapshots, or tests were changed by this audit.
Only this handoff report was created.
