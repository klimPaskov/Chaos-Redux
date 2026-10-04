# Mengele import decisions: AI baseline and eligibility comparison

**Status:** Unresolved; the required hash-bound baseline inspect was accepted as a native task but its persistent job remained queued without a result through 15:03:34 UTC. Ordinary tool-call retries timed out at 600 seconds. No evaluate, sweep, compare, or rendered probability artifact has returned.

## Scope and source identities

This read-only audit covers exactly `import_subjects_from_japanese_china`, `import_subjects_from_india`, and `import_subjects_from_africa` in `common/decisions/germany_mengele_decisions.txt`, plus the shared `germany_mengele_import_subjects_from_from_state` helper in `common/scripted_effects/germany_mengele_effects.txt` as eligibility context.

Frozen before decision snapshot: `docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation/mengele_foreign_purchase_retirement_2026-10-03/before_germany_mengele_decisions.txt`, SHA-256 `c9c32f368baf263b76a013dee17508463ba330efb66ed55cf7343bd77c4e31b4`.

Owner-provided after decision snapshot: `docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation/mengele_foreign_purchase_retirement_2026-10-03/after_germany_mengele_decisions.txt`, SHA-256 `4425e12b2afe38eb62426095ee30eb765a3e5f02c041f2c1ac40127e4436d33d`; the current live decision file hash matches this after snapshot.

The three targeted before blocks are at source lines 124-179, 182-227, and 230-275; after blocks are at lines 124-180, 183-229, and 232-278. A direct before/after substring check confirms each audited AI block is byte-identical: `ai_will_do = { base = constant:germany_mengele_decision_ai.silence_dissenting_file }`. That constant is `12` at `common/script_constants/germany_mengele_constants.txt:188`. There are no choice-specific AI modifiers. This is static source score evidence only, not MCP probability evidence.

The owner’s source fixture report lists 33 passing retirement/payment fixtures in `source_results.json`. Those fixtures concern source/effect replay and refunds; they do not test AI willingness, eligibility selection, normalized odds, or runtime choice. No HOI4 process was launched.

## Connected MCP identity, schemas, and task negotiation

The configured entry in `C:\Users\klimp\.codex\config.toml` is `mcp_servers.hoi4_agent_tools`, command `hoi4-agent-tools.cmd`, with `HOI4_AGENT_CONFIG` at `C:\Users\klimp\AppData\Roaming\hoi4-agent-tools\config.json`. The command resolves to `C:\Users\klimp\AppData\Roaming\npm\hoi4-agent-tools.cmd`, which launches `C:\Users\klimp\AppData\Roaming\npm\node_modules\hoi4-agent-tools\dist\bin\stdio.js`; its `package.json` reports `hoi4-agent-tools` version `3.6.0`.

The live server answered resource discovery with an empty resource list and returned the artifact byte-range template. A direct stdio client using the provided `@modelcontextprotocol/sdk` 1.30.0 package and the configured global server binary initialized successfully and reported server version 3.6.0, server task capabilities `list`, `cancel`, and `requests.tools.call`, and `execution.taskSupport = optional` for probability tools. That direct client advertised task list/cancel support and successfully negotiated task-based tool execution.

The owner’s reference artifacts came from workspace `camp_famine_oct3`, which is not registered in the fresh configured server process. A task request using that ID completed with tool error `WORKSPACE_NOT_REGISTERED`; this was a workspace-selection error, not probability evidence. The registered `current` workspace resolves to canonical workspace `mod_chaos_redux_ea3b2d67c2c0`.

The corrected baseline task used `hoi4.probability_inspect`, adapter `decision_ai_will_do`, exact candidate subset [`import_subjects_from_japanese_china`, `import_subjects_from_india`, `import_subjects_from_africa`], and source selector `{ path: "common/decisions/germany_mengele_decisions.txt", snapshotPath: "docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation/mengele_foreign_purchase_retirement_2026-10-03/before_germany_mengele_decisions.txt", expectedSourceHash: "c9c32f368baf263b76a013dee17508463ba330efb66ed55cf7343bd77c4e31b4" }` in workspace `current`.

The native task ID is `mod_chaos_redux_ea3b2d67c2c0:job_7feeb5acb54a43fde08ab09950abd625fc7bd5a71590a8af5928c56c2eef60ad`; persistent job ID is `job_7feeb5acb54a43fde08ab09950abd625fc7bd5a71590a8af5928c56c2eef60ad`. `hoi4.job_inspect` was called repeatedly against workspace `mod_chaos_redux_ea3b2d67c2c0`; the latest result at `2026-10-03 15:03:34 UTC` was `JOB_STATUS`, status `queued`, revision 1, `resultReady = false`, `cancelRequested = false`, and `updatedAt` unchanged from creation at `2026-10-03T14:32:08.867Z`. A later native `tasks/get` query returned task status `working` with `lastUpdatedAt` still equal to its creation time. The persistent probability worker has not started; the local SDK poll stream was stopped without requesting task or job cancellation.

The connected wrapper’s broad and narrowed ordinary calls each returned `timed out awaiting tools/call after 600s`. A hash-bound request with only `snapshotPath` returned immediate MCP error `-32602` and identified the required logical `path` plus `expectedSourceHash`; the corrected standard tool call with those fields also timed out after 600 seconds. The native task route accepted the correctly formed request, but its persistent job remains queued as described above.

The current probability schemas expose adapter `decision_ai_will_do`, but `scenarioSet` is untyped in `probability_evaluate`, `probability_sweep`, and `probability_compare`. There is no probability inspect result to supply a candidate/input inventory or more specific scenario contract. No MCP source revision, scenario hash, analysis ID, comparison ID, or probability artifact URI has been returned.

## Probability attempts and outcome

1. Broad frozen-source baseline: `hoi4.probability_inspect`, adapter `decision_ai_will_do`, source `path` set to the frozen snapshot, `refresh = true`; it timed out awaiting `tools/call` after 600 seconds.
2. Required narrower retry: the same frozen source plus only the three audited IDs in `candidatePool`; it timed out awaiting `tools/call` after 600 seconds.
3. A hash-bound selector using only `snapshotPath` was rejected with `-32602`; the error required the logical source `path` and `expectedSourceHash`.
4. The corrected ordinary wrapper request using logical `path`, `snapshotPath`, `expectedSourceHash`, and the exact three-ID pool timed out awaiting `tools/call` after 600 seconds.
5. A direct SDK task using the correct selector but `workspaceId = camp_famine_oct3` returned `WORKSPACE_NOT_REGISTERED` and was not a probability analysis.
6. A direct SDK task using `workspaceId = current` created the persistent job above. It remains `queued` with no tool result; after 30 minutes from creation, the exact native `tasks/get` query still returned `working` rather than a terminal result.

`probability_evaluate`, `probability_sweep`, and `probability_compare` have not been run because the mandatory source inspect task has not executed. There are no MCP-confirmed base values, modifier traces, eligibility counts, rankings, sensitivity, before/after deltas, or normalized probability results. `probability_render` was not run because no analysis ID or scenario hash exists.

## Scenario and pool completeness

Planned matched comparison IDs are `ger_1943_active_precutover_valid_foreign_source`, `ger_1943_restricted_precutover_valid_foreign_source`, `ger_1944_active_precutover_valid_foreign_source`, `ger_1944_restricted_precutover_valid_foreign_source`, `ger_1943_invalid_target`, `ger_1944_invalid_target`, `ger_1943_active_initialized_retired`, and `ger_1944_restricted_initialized_retired`. These IDs are planned labels only; no probability scenario using them has completed.

The candidate subset is complete only for the three retired decision IDs. It is incomplete for the full German decision-category race and for each `state_target` map pool because no complete set of matching Asian or African states, controllers, faction relations, owners/cores, imported-state flags, or per-state responsibility variables was supplied. The Japan/China branch requires an Asia state core of CHI, PRC, GXC, MEN, or MAN, controlled by JAP/MAN/a GER faction partner, and not controlled by GER. The India branch requires an Asia state core of RAJ and either GER control or a GER-faction controller. The Africa branch requires an Africa state not core to GER and either GER control or a GER-faction controller. Each also checks responsibility eligibility and an unimported-state flag. No complete eligible-state list was supplied, so no exact selection probability may be stated.

No save-backed campaign snapshot was supplied. Both Mengele program triggers require `camp_admin_country_mengele_historical_gate` at `common/scripted_triggers/germany_mengele_triggers.txt:29-50`; that gate at `common/scripted_triggers/camp_administration_country_triggers.txt:103-107` requires date later than 1943.5.29, GER control of state 88, and an operational state 88. `camp_admin_site_is_operational` at `common/scripted_triggers/camp_administration_triggers.txt:2-12` checks the state-scoped `camp_admin_initialized` flag, active/open status, responsible-country variable, and valid authority. The retirement gate in the decision blocks checks `camp_admin_initialized` in country scope, so these are distinct state and country flags despite sharing a token. A 1943 active/restricted scenario must be dated after May 29; date, both scope flags, state 88 controller/site inputs, and save-backed campaign values remain unverified. I did not invent those inputs or force an implausible transport target to appear valid. `camp_rework_state_can_accept_responsibility_from_root` at `common/scripted_triggers/camp_repression_rework_triggers.txt:41-46` accepts a source state when its responsibility variable is absent or names the acting root; this does not enumerate or prove any eligible map target.

## Result classifications and findings

- Shared source base `12`: **static score-only observation**, not MCP-confirmed and not a selection probability.
- Three before/after AI blocks: **source-exact byte equality**; each still resolves in source to the same shared constant expression.
- All requested AI eligibility and scenario results: **unresolved**; the persistent baseline inspect job is queued without an analysis result.
- Candidate pool: **incomplete** for target-state selection and full-category ranking.
- External factors: **incomplete**; no save-derived country/state/faction/controller inputs or AI-strategy factors were supplied.
- Dominance, starvation, rank reversal, repetition, and exploit risk: **unresolved** by the probability adapter.
- The after snapshot adds `NOT = { has_country_flag = camp_admin_initialized }` to `visible` and `target_root_trigger`, adds the same gate inside `available` as a `hidden_trigger`, and refunds only the native PP cost in stale completion. Both shared compatibility helpers at `common/scripted_effects/germany_mengele_effects.txt:192-201` now only zero the scratch autonomy variable. These source changes leave no physical transfer or additional benefit payload if a transitional scope mismatch leaves a stale decision entry present; the source fixtures report net PP change 0. Whether the engine AI candidate selector excludes the decision before scoring remains unresolved.

## Reference and source review

The current-workspace `hoi4.reference_context` result for surface `ai` returned context ID `8dbf8a701c2c0a45e2377587380bfa4ba9d014010befa091d37b3ee4cac645d9`, revision `917cd261f7da51fe4d8687c5d7663e768a09c5c101ac130ce646bc64637aa818`, and listed omitted sources `Triggers` and `Scopes`; the targeted searches below filled the relevant AI and decision-gate sections.

`hoi4.reference_search` and `hoi4.reference_read` for offline AI semantics returned `AI modding` ID `ab2b62a1e95fe5c84560ceedca6723cea6918faf69b08fd399709a2afbf8efe6`, revision `917cd261f7da51fe4d8687c5d7663e768a09c5c101ac130ce646bc64637aa818`, source `paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md`, lines 26-37. It distinguishes ordinary `ai_will_do` highest-score selection from `ai_chance` probability-proportional event-option sampling and notes that additional multipliers can apply.

The offline `Decision modding` AI result was ID `151bbd3b6a875558e43f67a1daa1288c5904dfbedfa09e3fca2e5e42b8ccc58f`, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`, source `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`, lines 357-374. It says an AI decision requires an `ai_will_do` MTTH-style block and distinguishes that block from event `ai_chance`.

The offline `Decision modding` trigger result was ID `21ff847245747e215d1cb8b5ace4abb3044f2269b53952c53b9bade4b8a2d21f`, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`, source `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`, lines 83-110. Its trigger overview result ID `4cdcf50c6a69c19ca5b7332f0d005982ca57d9081a7ac33519d672ea9ca149ac`, same revision, lines 531-537, explains daily `target_root_trigger`/`target_trigger` checks and the targeted decision’s `ROOT`/`FROM` split.

The installed vanilla `Country Decisions` documentation result was ID `c8ba2a44d708fd3048c019dfb9e36f3ecf59ff754f7cb4ea3bb7c4704deb5c58`, revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`, path `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\_documentation.md`, lines 1-46. It defines `visible` and `available` check cadence and states `target_root_trigger` is a country-scope precheck that should be a subset of `visible`.

## Recommended handling

Keep the owner’s accepted eligibility cutover and cost-only stale completion refund; keep the shared base score at `12` unless a returned MCP trace identifies a weighting defect. The accepted retirement design is eligibility-based and no evidence supports a numeric AI-weight target. Before closing this weighted-change gate, retrieve the result for the queued baseline job, then run matched before/after evaluations and `probability_compare` using the same named scenarios and exact snapshot paths. Run a sensitivity sweep only on a supported path returned by probability inspect, and keep results score-only or unresolved while candidate states and external factors remain incomplete.

