# Event 016 terminal T1–T4 postpatch review — 2026-09-02

## Result and checkpoint

Read-only postpatch review against source revision `957ae81`, continuing `016_final_terminal_current_review_2026-09-02.md`.
Checkpoint: 2026-09-02 17:49:49 +03:00, current HEAD `62b15587f286b169346b0f326d5d58162ee969da`, with parent-owned uncommitted changes included.
Only this new handoff was written; no gameplay, fixture, configuration, staging, commit, game launch or logs were touched.

**Source acceptance:** T2, T3 and T4 are addressed after the additional terminal-close correction applied during this review.
T1's current-facility gate repair is accepted, but its command/power physical site receipts and component interruption remain explicitly open.
This is not overall terminal/Event 016 acceptance and is not an engine or probability certification.

| Finding | Current result |
| --- | --- |
| T1 stale facility authorization | Fixed at arming continuation, fail-deadly authorization and shared final-commit gates; physical command/power mapping still open. |
| T2 repeat local/regional defeat rewards | Common classification, preparation and popup-consumption boundaries now prevent repeat awards in the traced lifecycle. |
| T3 encoded-date duration | Eleven frozen arithmetic cases match; interval open/close, inactive gaps, nested close and both terminal exits reviewed. |
| T4 stale/duplicate settlement certificate | Selection/cancellation/final helper use the same predicate; permanent receipt precedes award; stale calls are no-ops. |
| MCP | Current inspect/render artifacts exist; full renders capture guarded option accesses and real retry helpers. Historical comparison is blocked by `EVENT_REVISION_NOT_CACHED`. |

## Reviewed source and requirements

Binding contract remains `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md`.
The prior terminal handoff supplies the exact accepted T1–T4 scope and known open physical counterplay boundary.
This pass reviewed the parent-specified seven gameplay files and terminal localisation diff against `957ae81`, then reread the finalizer correction separately.

The required offline Data structures, Decision modding, Event modding, Effects and scope references, and installed documentation consulted in the preceding terminal audit remain the syntax references for this continuation.
The relevant distinction is explicit in installed `documentation/dynamic_variables_documentation.md:977` / `:996`: `global.date` is the display/comparable date, `global.num_days` is total elapsed days.
Vanilla `common/ai_strategy/GER.txt:3847` uses the latter for day arithmetic.
Decision timer cancellation follows the offline Decision modding rules and the vanilla AFG cancellation precedent already cited in the first handoff.
No new skill, source generator or test file was authored.

## T1: current physical gate — accepted first repair, not full closure

The exact existing query `brilliant_scientist_has_required_singularity_facilities` is now called by:

- `common/scripted_triggers/016_brilliant_scientist_kruger_state_decision_triggers.txt:448`: arming continuation, reused by start and timer-end resolution.
- The same file `:481`: fail-deadly authorization, reused at delayed resolution.
- `common/scripted_triggers/016_brilliant_scientist_triggers.txt:960`: shared Singularity final-commit readiness.

Causal trace: all historical component/node/power receipts remain true, but required facilities are no longer currently owned and controlled.
The current query is false, so arming continuation/cancellation and its guarded completion reject; fail-deadly completion rejects; deliberate detonation and the shared failsafe gate reject.
An intact valid facility network still passes this added term.
No extra cost, component, random family, reward, or threshold was introduced.

The terminal gate still does not import the ordinary decision-active gate or a blanket non-capitulation condition.
The capitulation failsafe continues to reuse the shared commit-state predicate, and the ledger-free wrapper remains separate, so a busy shared Fallout ledger can still enter its bounded retry path.
The first repair therefore preserves the intended semantic distinction between physical capability and the ordinary decision UI lifecycle.

**Still open:** accumulated command/power counts are not yet derived from recorded physical sites.
The parent expressly retained this work for a separate implementation.
The earlier state/role/quantity receipt recommendation remains applicable, as does the missing connected component-destruction boundary.
The current facility query alone must not be described as full T1 closure.

## T2: dispatch and popup conservation traces

Source boundaries:

- `common/scripted_effects/016_brilliant_scientist_super_event_effects.txt:564` excludes `brilliant_scientist_local_or_regional_defeat_recorded` at the common evaluator, alongside the existing qualifying-defeat receipt.
- `common/scripted_effects/016_brilliant_scientist_aftermath_effects.txt:77` / `:91` reject preparation when either the pending flag or either permanent outcome already exists.
They set pending before delivering .301/.303.
- `events/016_brilliant_scientist_aftermath_events.txt:26,36,71,85` wrap each option mutation in its package's pending guard.
Each clears pending before writing its permanent outcome and granting its original reward.

| Sequence | Observed source result |
| --- | --- |
| Local/regional capitulation, then same KRG annexation | First evaluator records classification and prepares one recipient; second evaluator rejects the recorded classification. |
| Preparation called twice before response | First sets pending and schedules; second rejects pending, so one normal delivery. |
| Two already-queued .301 windows, choose A then B | A consumes pending and grants its archive result; B's effect guard is false, so no stability/war-support award or contradictory permanent outcome. |
| Two already-queued .303 windows, choose B then A | B consumes pending and grants its original nationalization result; A cannot grant an idea/stability result afterward. |
| Preparation after either permanent outcome | Rejects the outcome receipt even though pending was consumed. |
| Distinct package or unrelated country receipt | Local uses only local receipts; regional uses only regional receipts; all are current-recipient country flags. |

The audit did not assume option visibility alone prevents replay.
The actual mutation guards are the protection, and the current MCP option-access records show the guarded clear/write sites.
The original choice rewards and AI blocks were not changed by this patch.
The deterministic once-award conclusion is source/graph evidence, not normalized AI probability evidence.

## T3: frozen arithmetic fixture and lifecycle sequences

Frozen input:
`docs/plans/016_brilliant_scientist_plans/subagent_handoffs/E016_TERMINAL_DATE_SCORE_BASELINE_2026_09_02.scenarios.json`.
SHA-256 verified as `d792ff260cf73c78d757d4d1a9a431fe6e1d51b66e9ed4d141d1064a1557da5b`.
The fixture was not edited.

The current helper at `common/scripted_effects/016_brilliant_scientist_super_event_effects.txt:308` starts duration at zero, adopts only positive accumulated active days, and adds the positive current `global.num_days - start_num_days` interval only while active and the start exists.
The scorer at `:433` calls that helper before applying the unchanged 180/365/730-day additive thresholds.
The fixture intentionally zeroes all non-duration score contributions.

Method: each exact JSON state was evaluated with an inline arithmetic mirror of those reviewed source branches, then checked against its frozen `sourceExpectation`.
This is an arithmetic/source regression check, **not** Clausewitz execution, MCP scenario execution, or probability normalization.
A first PowerShell formatting attempt failed at parse time and changed no files; the corrected read-only calculation returned all eleven matching results.

| Frozen scenario ID (prefix E016_TERMINAL_DATE_) | Active days | Duration points | Frozen expectation |
| --- | ---: | ---: | --- |
| NO_START | 0 | 0 | Matches |
| 179_ACTIVE_DAYS | 179 | 0 | Matches |
| 180_ACTIVE_DAYS | 180 | 2 | Matches |
| 364_ACTIVE_DAYS | 364 | 2 | Matches |
| 365_ACTIVE_DAYS | 365 | 4 | Matches |
| 729_ACTIVE_DAYS | 729 | 4 | Matches |
| 730_ACTIVE_DAYS | 730 | 6 | Matches |
| CLOSED_180_PLUS_100_INACTIVE | 180 | 2 | Matches |
| RESUMED_180_PLUS_10_ACTIVE | 190 | 2 | Matches |
| NEGATIVE_ELAPSED_CLAMP_ZERO | 0 | 0 | Matches |
| DUPLICATED_CLOSE_ONCE | 180 | 2 | Matches |

Additional ordered source traces check behavior that a final-state arithmetic table cannot prove:

1. Open at day 100; refresh at day 280 produces 180.
Repeated refresh recomputes from accumulated zero plus the same open interval, rather than adding another 180.
2. Close at day 280 while active: `close_world_threat_interval` (`:331`) refreshes once, stores accumulated 180, records end date/day, and clears the start-day receipt.
A second close sees no start and is a no-op, even before the caller clears the active flag.
3. Inactive day 380 refresh returns 180.
The 100 inactive days do not accrue; the frozen closed-state case also deliberately retains an obsolete start, which is ignored while inactive.
4. Reactivate at day 380: the activation writer (`:393`) writes a fresh open start but preserves accumulated 180 and the first display/reveal date.
At day 390 duration is 190, not 290 and not 10.
5. Negative open delta contributes zero; positive accumulated history remains intact.
No-start contributes no invented open history.
Negative/unset accumulated values do not make duration negative.
6. Ordinary threat shutdown closes before clearing active/global flags (`:419`–`:421`).
Qualifying defeat computes score before recipient evidence, then closes before clear (`:491`–`:493`), preserving the scored duration for achievement evidence.
7. Local/regional defeat may call arsenal dismantlement, whose nested threat refresh closes the interval first.
The outer close (`:542`) then sees the cleared start and cannot double-count.
If the nested refresh did not close, the outer close remains the single owner.
8. **Both terminal finalizers:** an omission discovered during this review was corrected by the parent before final source acceptance.
Singularity now closes at `:717`, then clears global source and country active flag; LabWorld does the same at `:742`.
Both refresh the Directorate idea lifecycle before shared threat refresh.
For accumulated 180 plus an open 20-day interval, terminal close freezes 200; a subsequent refresh at any later day still returns 200, and the world-end exclusion prevents a new interval.
All five current global-source clear writers now pair close-before-clear with country-active cleanup.

The two terminal-close edits are included in the final source hash and in the full render's source-hash inventory, not merely a parent claim.
The first recorded dates remain display/history receipts; completed elapsed time is separate.
No score weights were adjusted here, and the probability owner retains responsibility for its separate weighted-surface gate.

## T4: delayed certificate and once-only award traces

`common/scripted_triggers/016_brilliant_scientist_kruger_state_decision_triggers.txt:418` additionally rejects an already-active durable-settlement receipt.
The paid decision at `common/decisions/016_brilliant_scientist_kruger_state_terminal_decisions.txt:461` uses the same predicate in availability and cancellation, including `cancel_if_not_visible = yes`.
Its final helper at `common/scripted_effects/016_brilliant_scientist_kruger_state_decision_effects.txt:537` repeats that predicate independently of UI cancellation.

- Valid completion writes `brilliant_scientist_durable_settlement_active` before the administration award.
A nested or repeated completion therefore fails the same predicate and grants nothing.
- World-end, removed disarmament eligibility, armed/fail-deadly status, or submitted Singularity receipt during the timer causes cancellation; even a late direct completion call cannot pass the helper guard.
- Administration refresh sees the durable flag before it evaluates threat clearance, so it closes threat history rather than reopening it.
- The subsequent nonterminal-verification helper is not blocked by the newly written durable flag; it checks the actual disarmament proof and releases the commitment lock as intended.
- Existing armed/construction history is retained; no repeated certificate reward or new cost appears.

The added requirement/cancellation tooltips in `localisation/english/016_brilliant_scientist_kruger_state_decisions_l_english.yml` describe current disarmament/terminal eligibility.
Unrelated wording edits visible in the same localisation diff were not re-audited.

## MCP evidence — obtained coverage versus limits

Workspace `mod_chaos_redux_ea3b2d67c2c0`.
Three exact event selectors were inspected: `chaosx.nr16.301`, `.303`, and `.901`.
Each trace used `direction:both, expandHelpers:true, maxDepth:1, maxNodes:24, maxEdges:40`.
They returned `EVENT_INSPECTED_PARTIAL`, focused revision `d9bc467fb6be1fcf671b83710d9940db0a537ee6023f85a3c12c0a3641c39c05`, graph hash `55ad0cfc2056ed488503d6456c2045e83f5a359d86d65b413c920aa3f7c38bf3`, zero projected helpers, and deferred lifecycle validation.

The later narrowly selected renders used `view:options` for .301/.303 and `view:neighborhood` for .901 with the same bounds.
The server selected its full graph for these calls despite the narrow requested selectors.
They returned `EVENT_RENDERED`, full revision `8521b18667d8bd8f709b5df4f7ae580d0a2c8f841de5a65eccefa4a49e7140e6`, graph hash `c3f1d9099acd98af471d04c2698f2e5ffa2bf7a51d9c85f5c05b18d07a659617`.
No explicit full scan/refresh was requested.

Observed selected evidence:

- .301 and .303 each selected the actual event, two options and two terminal exits: five nodes, not an empty/global selection.
Their state-access records show current pending-guarded receipt clears and permanent writes.
For .303 these are lines 71–73 and 85–87; the .301 image was visually inspected.
- The .901 neighborhood selected 24 nodes and contains real `helper:brilliant_scientist_execute_singularity_terminal`, `helper:brilliant_scientist_schedule_singularity_fallout_retry`, `helper:brilliant_scientist_recover_rejected_singularity_fallout_request`, and `helper:brilliant_scientist_evaluate_defeat_after_global_threat`.
This is improved helper presence evidence compared with the focused traces, but is a bounded neighborhood, not complete reachable-path execution.
Two visible unresolved `instant_build` entries belong to neighboring construction branches, not a demonstrated missing terminal helper.
- Full graph validation remains false, reporting 3,948 global blocking diagnostics.
Those counts were not used as Event 016 failures or a clean pass.
- The full source-hash inventory includes final effects, decisions, event and localisation hashes and matches disk.
The two changed scripted-trigger files are absent from that inventory, so their semantic checks remain source-reviewed, not tool-certified.
- Duration arithmetic and timer/callback sequence results above are source evidence; a graph render does not execute them.

Mandatory comparison was attempted once with real revisions:

```json
{"before":{"revision":"3278b34c53341a910d3959107765bb43be6cba2fb27f8562b8b0557d20fefc2f"},"after":{"revision":"d9bc467fb6be1fcf671b83710d9940db0a537ee6023f85a3c12c0a3641c39c05"},"render":false}
```

Result: `EVENT_REVISION_NOT_CACHED`, no comparison artifact, failed validation.
The retained prior report wrappers were not misrepresented as full graph baselines.
No retry loop or fabricated comparison acceptance was used.

### Returned artifacts


chaosx.nr16.301 inspect:

- event-trace-d9bc467fb6be.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9949f1785802dd009a88c4fedc1da36ec10ea5ca06e7f999c0e47dde2c56fb5a/8688304784fee789ac4123a6fec3b2e9842b590245913a9722b825258ac2cbc8/event-trace-d9bc467fb6be.json`

chaosx.nr16.301 render:

- event-options-8521b18667d8-manifest.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3fb89dad91ad090b9dd2d18328ce3d687a14a24952ce58630a8fb13b0188599e/6b983305d537cce08066ddf9c2674e28251245c455cf874dee1ea278f9a885a6/event-options-8521b18667d8-manifest.json`
- event-options-8521b18667d8.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f177b7f5172b797ef4cf3e99f89039adba9b90a7ac68eff88efdec1eaec2e8d9/4967588d954378efd2f875f6bd8b3dad5c2323d451af81febcccc0055ea74cda/event-options-8521b18667d8.json`
- event-options-8521b18667d8.svg: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8db90a19c1b5e4447b4d03ca2c8382a79492382eefab7cc36008c1824de9a479/e084c75b50e0a95f53acc347800f1f1657409c0bf5e72008151defa77980e04b/event-options-8521b18667d8.svg`
- event-options-8521b18667d8.png: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/da919a42cc38501de08380eb8a3d996c7f343584efe9ea5bace630622f946d7f/d7aeed705cfcaa71071e980211f329f0485a031ecfa7c75a12f350366bcabd3c/event-options-8521b18667d8.png`

chaosx.nr16.303 inspect:

- event-trace-d9bc467fb6be.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f70ff3e6bab9891b5b11975e4c5d3c56fad10eae232ad91828d124b4f257e7dd/24f1dbdb0b445cbf07bda202b4151d4f12d2c6a89cb659248dc45fb5bdec818f/event-trace-d9bc467fb6be.json`

chaosx.nr16.303 render:

- event-options-8521b18667d8-manifest.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5db703d1352adee839f1cc22aeafcd7b0cc365a6e2a8d7d50f344ec605ed7add/3d3037c158b57d1c4dc0139382257e9ae7d115987057af151580ded9df0c39e8/event-options-8521b18667d8-manifest.json`
- event-options-8521b18667d8.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2cb0a8dab347905ca40e56a14a71a80b980db2b422e7eb8378f0ce5eb760b565/742ce626dd3032cbb443f61f8018c59120c7e02f8d38933e9d217cebc4bea04e/event-options-8521b18667d8.json`
- event-options-8521b18667d8.svg: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cccd1aba2c42ed12d84e0eefd1ee85932cfc6481a4490fa2ba71c0197089402c/e5af418a28350ac3734fa8327c4d242101c39ab8b1d12b63544e309957961db4/event-options-8521b18667d8.svg`
- event-options-8521b18667d8.png: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/70be0b7999fd2ca37de5b913b4c09c7d371cfcf88887540790c3ebdda265e53c/ef0cb5840be92a975c433dc8e4b3ae8788551c0b73d10ca1283cc6673c648343/event-options-8521b18667d8.png`

chaosx.nr16.901 inspect:

- event-trace-d9bc467fb6be.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/104947add53808318b90d52cd15acd2f1ed09ba1e0830fc4ed7fe4c6f979d842/7ecdd6997123c4bd061b53b45cc26a024030a0ad3f8e24d16ccf6e3de8f53099/event-trace-d9bc467fb6be.json`

chaosx.nr16.901 render:

- event-neighborhood-8521b18667d8-manifest.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1348fc4389fd9745526a92b003adb5fd30a7a947a740a7e8cd6a96cced0e7ec8/6f17c24065a4e7b25994a4f8f3e0b04d62ca3e580721b8232f5161812d918390/event-neighborhood-8521b18667d8-manifest.json`
- event-neighborhood-8521b18667d8.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7fad60b058e9f086cdcbe4d47c4cb41f0a2f04974cf370207ad138cb0d3689f4/89a16d46ea3ac576e7bdd870c3c17b0349d9a06d4c9d5ae1302ff0a919d50290/event-neighborhood-8521b18667d8.json`
- event-neighborhood-8521b18667d8.svg: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d0884522ae8460ac74c60ea6b85ec9048feac420d300862435ed25322d9d6146/8f2670e91f72bca5a520dc04de9bf54066384661eb2920bfafa5d70a5e7d2b23/event-neighborhood-8521b18667d8.svg`
- event-neighborhood-8521b18667d8.png: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/66cd2199e7367be5bc02167499784a386db720b5c86abcc976a1efc7bdea5600/f1c78ad24c13981910fde93926e6fda0760ae847f0b2e86f8876a56bf37a5d76/event-neighborhood-8521b18667d8.png`

Cached PNGs, no regeneration:

- .301: `C:/Users/klimp/AppData/Local/hoi4-agent-tools/workspaces/mod_chaos_redux_ea3b2d67c2c0/artifacts/da/da919a42cc38501de08380eb8a3d996c7f343584efe9ea5bace630622f946d7f/event-options-8521b18667d8.png`.
- .303: `C:/Users/klimp/AppData/Local/hoi4-agent-tools/workspaces/mod_chaos_redux_ea3b2d67c2c0/artifacts/70/70be0b7999fd2ca37de5b913b4c09c7d371cfcf88887540790c3ebdda265e53c/event-options-8521b18667d8.png`.
- .901: `C:/Users/klimp/AppData/Local/hoi4-agent-tools/workspaces/mod_chaos_redux_ea3b2d67c2c0/artifacts/66/66cd2199e7367be5bc02167499784a386db720b5c86abcc976a1efc7bdea5600/event-neighborhood-8521b18667d8.png`.

## Final source hashes

| File | SHA-256 |
| --- | --- |
| common/scripted_effects/016_brilliant_scientist_super_event_effects.txt | b2c58fc0ce3600eadab37f2b3cf7f7f0f91f17bcaa170b85e1a6647edaac4cfb |
| common/scripted_effects/016_brilliant_scientist_aftermath_effects.txt | 9c8268a04824cbe473ec4f37da9979e5d8eb504580635aa34381a49e699705ca |
| common/scripted_effects/016_brilliant_scientist_kruger_state_decision_effects.txt | ef9de1e07f710e284a6a1b7c2cbd1202f535c2b46b137f07e5fb947714d802e8 |
| common/scripted_triggers/016_brilliant_scientist_kruger_state_decision_triggers.txt | b321a84787578fdb434101013490dbd088dc6cce5fd919a6843d5f8db3105272 |
| common/scripted_triggers/016_brilliant_scientist_triggers.txt | 30c24c285c64a59faa97cb1c00e3bd0e161c0581768b7ee6bfd0b0be3d419fbd |
| common/decisions/016_brilliant_scientist_kruger_state_terminal_decisions.txt | e5d24548df4cbe01f25a63a4528b65ebc2935274409ff4a098c3b78488bb65f3 |
| events/016_brilliant_scientist_aftermath_events.txt | 0445bec0b3ae5f0f60fe6f2b9c556e93158b6dc108661cb49342616fbdf82890 |
| localisation/english/016_brilliant_scientist_kruger_state_decisions_l_english.yml | 0f498991a11c33c08d03a6b347550a51d471f55c2c585ac93504769ba2cfd3d4 |

Skills applied from the terminal audit: chaos-redux-events, chaos-redux-subagents, chaos-redux-improvement-loop, chaos-redux-event-planning, chaos-redux-decisions-missions and chaos-redux-super-events.
Their required lifecycle, source-of-truth and MCP evidence separation informed this post-review; none was modified.
No new artwork or asset acceptance was attempted.
No simplification was implemented by the reviewer.
The remaining physical T1 work and the explicit MCP comparison/semantic limits must travel with the parent's completion status.
