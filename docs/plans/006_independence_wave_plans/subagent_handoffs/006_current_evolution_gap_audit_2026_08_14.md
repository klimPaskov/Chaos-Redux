# Event 006 Current Evolution, League, and Super-Event Gap Audit

Date: 2026-08-14

Mode: read-only gameplay audit; this handoff is the only file updated by the auditor.

## Current re-audit verdict after `7a4e0d7a9`

**No concrete safe local source defect remains in the audited evolution, League, or super-event surfaces. The former `EVOL-006-DISABLE-REMOVE-TAIL` finding is stale as a current gap and is superseded by gameplay commit `7a4e0d7a9`.**

The live `common/decisions/006_independence_wave_evolution_incident_decisions.txt` contains five symmetric `remove_effect` transactions at lines 35-44, 79-88, 123-132, 169-178, and 214-223. Each enabled branch requires `is_independence_wave_active_country = yes` and the absence of its exact `events_log_disabled_evolution_6_21_n` flag before firing its exact event `chaosx.nr6.360` through `.364`; each `else` branch clears the exact pending flag set by that decision. No event ID, disable-stage suffix, or pending-flag family is mismatched.

Fresh post-`7a4e0d7a9` focused Event MCP inspection and rendering returned `EVENT_INSPECTED_PARTIAL` and `EVENT_RENDERED_PARTIAL`, zero selected blocking diagnostics, event graph revision `741883f50501db1f866db675ee6ad6cb4009a90ad539eb84b08ce5e82602f65b`, and graph hash `37eb00185cb12c74f97438ecee7380780cf4eec14d3693f7930e97a91ce4b720`. The revision is unchanged because `7a4e0d7a9` edits a decision file rather than an event-graph source. The large-workspace helper/lifecycle projection remains deferred, so MCP evidence does not independently model the decision timer transaction; the exact source audit above is the closure evidence.

Fresh inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/84615cdc283df235b22639b183d5537e6ea4aeb80afba0a607457aa417b75510/aad2d89cd8a030407af23a9fb620b534cf9e9ec2b8a5a8113cafb797d15a298f/event-state_flow-741883f50501.json`.

Fresh five-event options-render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0ef71acf61d680d85afc222a577bab7ff6fb070175766eab65ca69f61db0260d/0262e9202ad5f988c58caed96e2a0901160b0c5d6e922948edfdc016fed2a345/event-options-741883f50501-manifest.json`.

Post-patch baseline: gameplay commit `b66899d16` (`Fix disabled evolution incident lifecycle`), documentation commit `fc8d2c45d` (`Clarify evolution incident source mirrors`), and gameplay/documentation commit `7a4e0d7a9` (`Fix disabled evolution incident removal cleanup`).

No Event 006 counts, package attestation, central adapter, preflight, deterministic Join, or admission status changed.

## Disposition

**NO SAFE LOCAL SOURCE GAP FOUND. The audited evolution and League surfaces pass the source audit, with the documented MCP projection limit; super-event `23` remains an external rights/user-selection blocker rather than a locally implementable defect.**

The five canonical Event 006 evolutions, their active-event delivery, pre-fire opening delivery, Event Log context, paid incident families, League phase progression, first-congress news, and ordinary super-event `24` remain source-present. Ordinary super-event `23` remains deliberately blocked on user-selected, rights-cleared audio plus parent-owned wrapper and firing work and is not a safe local patch.

Commit `b66899d16` correctly added stage-specific disable guards to the five incident decisions and the five resolution-event triggers. The parent repair now completes the removal transaction: each timed decision has an enabled branch that fires its matching event and a disabled or inactive branch that clears the already-set pending flag. The timer-expiry/disable stale-state risk is closed without refunding the paid cost or applying a resolution helper.

## Former finding, now superseded

### EVOL-006-DISABLE-REMOVE-TAIL (resolved): guarded events no longer reject an uncleaned timer removal

The five paid decisions set their pending flag in `complete_effect` when selected, as defined by the decision lifecycle, then wait for `days_remove` and reach a guarded resolution-or-cleanup branch from `remove_effect`:

- `common/decisions/006_independence_wave_evolution_incident_decisions.txt` sets `independence_wave_evolution_replicable_incident_pending` and now fires `chaosx.nr6.360` only through the enabled branch; the inactive/disabled branch clears the pending flag.
- The same guarded removal shape is present for Dormant Nations and `chaosx.nr6.361`, Armed Birth and `chaosx.nr6.362`, Sovereign Congress and `chaosx.nr6.363`, and Open Sovereignty and `chaosx.nr6.364`.

Commit `b66899d16` added exact disable checks to `visible` and `cancel_trigger`, which normally cancels an in-progress timer and runs `cancel_effect`. It also added exact disable checks to the event triggers at `events/006_independence_wave_evolution_incidents.txt:32-35`, `55-58`, `78-81`, `101-104`, and `124-127`.

The repaired removal branch is fail-closed for the option effects and self-cleaning at the removal boundary. If the timer takes its `remove_effect` path while the corresponding disable flag is set, the country event is not fired and the matching pending flag is cleared immediately. The broad Event 006 country cleanup in `common/scripted_effects/006_independence_wave_effects.txt:504-516` and `3004-3018` remains defense in depth rather than the only cleanup path.

The accepted event workflow requires disabled evolution-gated content to be safely skipped and forbids disabled evolutions from setting state later read by decisions or follow-up content (`.agents/skills/chaos-redux-events/SKILL.md:172-186`). The accepted Event 006 spec also requires the evolution log to retain an explicit enabled state (`docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_2_event_flow_and_evolutions.md:577-586`). The offline decision reference confirms that `complete_effect` runs when the decision is selected, `remove_effect` runs when the timer ends, and a true `cancel_trigger` ends the timer without running `remove_effect` while executing `cancel_effect` (`paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md:266`, `323-339`). The installed vanilla `common/decisions/AFG.txt:47-53` supplies the same selected-state-marker followed by timed `remove_effect` pattern, and its later timed cleanup at lines 122-137 demonstrates that transaction-owned markers are cleared in the removal endpoint.

This was one shared lifecycle-family defect across five symmetric rows, repaired as one bounded source change rather than five independent design requests. It must not be carried forward as an open current-source gap.

## Implementation receipt and safe order already completed

The parent applied this exact contract in the current working tree. The change is limited to the five symmetric `remove_effect` blocks below.

1. Edit only `common/decisions/006_independence_wave_evolution_incident_decisions.txt`.
2. Replace each one-line `remove_effect` with an exact stage-specific branch (completed; the current blocks begin at source lines 35, 79, 123, 169, and 214).
3. In the enabled branch, fire the existing matching event ID (`chaosx.nr6.360` through `chaosx.nr6.364`) unchanged.
4. In the disabled branch, clear only the matching `independence_wave_evolution_*_incident_pending` country flag and do not refund the already-paid cost, invent a new result, write an evolution row, or apply either resolution helper.
5. Keep the post-`b66899d16` decision `visible`, `cancel_trigger`, and event-trigger guards as defense in depth.
6. Do not add an isolated guard inside the ten option resolution helpers. They are already reachable only through the guarded events, and a helper that merely exits would reproduce the pending-state leak unless it also owned cleanup.
7. Re-run `hoi4.event_inspect` and `hoi4.event_render` for `chaosx.nr6.360` through `chaosx.nr6.364`, then run `hoi4.event_compare` against the current graph revision if it remains cached. Route the unchanged `ai_chance` surface through `chaosx_ai_probability_auditor`; a lifecycle-only patch should produce no probability delta.

The direct flag checks are preferable here to reconstructing `is_current_evolution_enabled` temporary context inside five removal blocks. They are the exact persistent flags already used by the decision and event guards and do not broaden tier, identity, admission, or League behavior.

## Completion status by audited surface

| Surface | Status | Evidence and disposition |
| --- | --- | --- |
| Canonical evolution activation and pacing | PASS at source; MCP partial | `common/scripted_effects/006_independence_wave_evolution_effects.txt:552-685` owns the five transitions, pre-fire eligibility, and one-stage active progression; lines 689-738 own MTTH scheduling and due checks. No safe gap found here. |
| Pre-fire evolved openings | PASS at source | `common/scripted_effects/006_independence_wave_evolution_effects.txt:757-779` freezes the five active stages and applies each pending opening to the released country. |
| Evolution Event Log rows | PASS at source; MCP helper projection deferred | `common/scripted_effects/006_independence_wave_evolution_effects.txt:159-290` sets event/type/stage/tier/date/actor context and defers pre-fire rows until an actor exists. |
| Five paid evolution incident families | PASS at source; MCP partial | Events `chaosx.nr6.360` through `.364`, their two options each, costs, timers, AI factors, resolution helpers, and the five removal-tail cleanup branches are source-present. `b66899d16` fixed visibility, cancellation, and event-entry guards, while `7a4e0d7a9` clears matching pending flags for inactive or disabled removals. The Event MCP receipts remain partial with zero selected blocking diagnostics because the large-workspace lifecycle projection is deferred. |
| Armed Birth paid frontier-reserve follow-through | PASS at source | Current authority explicitly states the five incident families and their paid frontier-reserve follow-through are no longer an implementation blocker at `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md:131`. No repeat implementation is authorized. |
| League shared state machine | PASS at source within this scope | `common/scripted_effects/006_independence_wave_effects.txt:2543-2598` covers regional conference, congress preparation/failure/reopen, and charter-vote progression. The first successful proclamation emits `chaosx.nr6.35` once at lines 2601-2609. No locally provable League source omission was found. |
| League first-congress news | PASS at source; MCP partial | `events/006_independence_wave.txt:71-82` defines `chaosx.nr6.35` with accepted ASSET-004. Fresh inspect/render selected zero blocking diagnostics. |
| Ordinary super-event `24`, Every Border a Casus Belli | PASS at source; live reachability remains partial | `common/scripted_effects/006_independence_wave_super_event_effects.txt:121-218` records the factual reason/actor/history payload and queues settings-aware presentation. Current authority at `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md:61` and `77` preserves source wiring while retaining factual host, collision, transaction, and formable reachability gates. No safe local defect was found. |
| Ordinary super-event `23`, The League of New States | BLOCKED, not locally patchable | `common/scripted_effects/006_independence_wave_super_event_effects.txt:4-7` and current authority at `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md:116-127` explicitly withhold rights-cleared audio, wrapper selection, and firing. No audio candidate is approved and no replacement work is authorized without user approval or a rights waiver. |
| Whole Event 006 | HOLD / PARTIAL | Current authority remains 32 content-attested selectable packages across 29 compatible reservation groups, 161 unattested rows, and 40 runtime adapters at `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md:5`. This audit does not widen central admission. |

## Mandatory MCP evidence

The post-patch workspace is `mod_chaos_redux_ea3b2d67c2c0`, event graph revision `741883f50501db1f866db675ee6ad6cb4009a90ad539eb84b08ce5e82602f65b`, and graph hash `37eb00185cb12c74f97438ecee7380780cf4eec14d3693f7930e97a91ce4b720`.

Read-only inspection and rendering covered the Event 006 root `chaosx.nr6.1`, League news `chaosx.nr6.35`, and every evolution incident event `chaosx.nr6.360` through `.364`. Every selected call returned `EVENT_INSPECTED_PARTIAL` or `EVENT_RENDERED_PARTIAL`, zero selected blocking diagnostics, and the exact limitation that the large workspace deferred workspace-wide helper projections and lifecycle passes. The MCP result supports event-node and option structure but does not prove the decision timer cleanup path; direct source inspection proves the former finding is repaired in the current file.

Key artifacts:

- Event 006 root trace: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/209c49c98bd4f5d9311229e8b754aeb5389a02de47f57e27c6d955c66622e53b/962abce71b0e8d3f3ec767b4c9cdb0de4cbc3123faecaf093c29c47e7b6d7856/event-trace-741883f50501.json`.
- Event 006 root overview manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d43f6c6224fc6a48d3f2fc6f0531ebac3f4b1e2c4226eba7b776350d3d671f67/c7ab1c022e048ba68027a3c0d7e2a55536ae51ed077e68c765cdd94337c95245/event-overview-741883f50501-manifest.json`.
- League news trace: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f591f8b2329a079c7b5d743eab4237635c1cfe32f55a3800f369a4262eb4c2ed/573b4e4093e9912774971f493d087f01c099094fed4859ae5e5c45b6f55b9006/event-trace-741883f50501.json`.
- League news overview manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0f9c6a04cfb631eb98c8a75ef0a34096b7ba47ad898c9af8601cea5015340e6e/216c1167a89c0ed35341b5a90fcfcbb9aab889ed1d005d8bfaf27335bfeaab53/event-overview-741883f50501-manifest.json`.
- Replicable Independence state-flow inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e77f42e3406bec11da9c7e80c8966336d170bc4e65b1f99fa5734314dfb46ba1/ccdb4bd75164429c23a340724fd81405e8ba41de1280595b6247d9ef8b483ffd/event-state_flow-741883f50501.json`.
- Replicable Independence options manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0f0bb86d6ae866e9157bcd169d45de73ef9dd0017123eeb2da175031c3ffdf3c/a1128ab314123d315b54124d085dd790dec6e978ee4c4806fdf5616532db0bab/event-options-741883f50501-manifest.json`.
- Dormant Nations trace/options: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cd763a8044cd5a52feb779ed545e2d794d53fd258bb0772822a6e38cf34dedd4/3ff5392349526157356369028be4943dddabb298a677bd05cbfec8d52e0519d0/event-trace-741883f50501.json`; `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/381a196c45246e20f4a3a49d2a6ffeef08afa57c432a6940703c9083f7b50217/6f3764765a9bde1142c6084faefc24d271696721ba3e266b7b2866beb6f28daa/event-options-741883f50501-manifest.json`.
- Armed Birth trace/options: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2116948a3348610e02a85bcb67f06812a2c053adf5803a89786ac5f7863cc883/165b518f785a51d95b54a1447bef52ee8aa123ced5bc2901f45b48927a68d038/event-trace-741883f50501.json`; `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/887023a42738e1c6fcc8e76c186c414b823dd42bb0fdf1b4a8f76ac8101bd3ea/b459301ea61d3936610d265b74db79d30074221a2dda8cb5e62f6c97e6f03f13/event-options-741883f50501-manifest.json`.
- Sovereign Congress trace/options: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/08493bcc0a6d5fcaa956cb356c42da742ca0adbfb54dae7499dd9e13c7a302e0/4e805c33d5a1a0bef3eea1c5a589227ef9488df18de54455f7b307d1b2185878/event-trace-741883f50501.json`; `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/df0cbedddcc4d2096142cd32ff48b757876fab5ec6316759602cbd3537235875/503dfa0a78156b44fe88f361cc78dd92a4ff27aa95315f90ed08c858bba603a4/event-options-741883f50501-manifest.json`.
- Open Sovereignty trace/options: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/26367ae4859853904de72fe412d692145d542b701c2e153a0c5c5f8a3d2f9e42/7f54df62e5f3d694667529e7f4b6261a3719b084360f63fe4a69398079aa1bf4/event-trace-741883f50501.json`; `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0f6a8e6c2d6a53d25ad8643ac041bd9fcf26c79d5853e26cdc088c21b065d6bd/a0d9c25d1976c84edd5cacec18de99d1955cd1bd4f692226fb1a7f50540f4d92/event-options-741883f50501-manifest.json`.

`hoi4.event_compare` was required for the earlier `b66899d16` event-graph change. The comparison was attempted between the pre-patch graph revision `d21fdfa2723e4a624054076fb1104ba638c4fbb1f733358a99b24aac1839ace2` and post-patch revision `741883f50501db1f866db675ee6ad6cb4009a90ad539eb84b08ce5e82602f65b`; it returned exact blocker `EVENT_REVISION_NOT_CACHED` with message `Requested event graph revision is not cached`, no artifacts, and no comparison claim. A fresh comparison request against the unchanged current revision after `7a4e0d7a9` returned the same blocker. Commit `7a4e0d7a9` changes only the decision removal endpoints, so there is no new event-graph revision to compare. Source diff review is not equivalent compare evidence.

## Weighted-surface disposition

The ten event-option `ai_chance` factors were routed through `chaosx_ai_probability_auditor` under scenario set `E6_EVOLUTION_INCIDENT_AI_CHANCE_POSTPATCH_2026_08_14` with enabled and disabled states for each event.

The source scores are `.360 = 60/40`, `.361 = 55/45`, `.362 = 55/45`, `.363 = 60/40`, and `.364 = 45/55`. All factors are positive, every two-option source pool sums to 100, the event-local `@` mirrors match the shared script constants, and no zero-total, negative, deterministic, or tied outcome was found. The disable flags change event and decision lifecycle eligibility, not option weights: a disabled row fails the event trigger before either option becomes selectable.

The probability inspection returned `PROBABILITY_SOURCE_INSPECTED` with ten discovered options, `poolComplete = false`, and one unresolved item at probability revision `d863b818b3caabad74526c14c0f85ca622c5d690024e3c266d505fd4e1f5a9b2`, source hash `4e5be8dc153d929a23f1b988d488265e2720424f17d9a657dfd384d5b8364e85`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/158fdd320707057f42830404f57876223017fb99826ac7ede6200627b2b87d4b/bff9fa8120279f68af774de5d9e97b7536d1ce66b4648c21a72ebb1b25dbfad1/probability-inspect-4e5be8dc153d929a23f1b988d488265e2720424f17d9a657dfd384d5b8364e85.json`.

Evaluation returned `PROBABILITY_ANALYZED_PARTIAL`, analysis `probability-6947e572931779539eeb0f71`, scenario hash `ba1c305cb7e66d238e14c80a7698458826333b92c339c4cb0ef04e9477c657fe`, and diagnostic `PROBABILITY_CANDIDATE_POOL_INCOMPLETE` because the adapter received five distinct event pools as one combined candidate set. Normalized probabilities were withheld; the exact source score ordering above is not presented as an MCP-proven normalized probability. Evaluation artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/79766f59f4b19bbf75bfd003ae408a2695ba098d0cf52304f76334a24ad5e77c/583f458125721b90b3a47784b91f6e45a0b11850e6e9627cefe36377ecdcb1f0/probability-6947e572931779539eeb0f71.json`. Render JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/45c444749aaa9f537e458fdac982fb778108e9640e89dc1f4364190254e9796c/077ea3d02b80a6f60bf61cd3a41312c13db25390f3e15faf908211ebd6881c97/probability-6947e572931779539eeb0f71.json`.

The sweep attempt returned exact blocker `PROBABILITY_SWEEP_RANGE_REQUIRED` because the literal factor paths had no declared numeric alternatives. Simulation and sequence analysis were not applicable because no uncertain inputs or custom cadence were declared. No weight change is recommended or authorized. The adapter does not model the decision timer's same-tick cancel/remove ordering, so weighted evidence cannot independently prove the cleanup; the live source establishes that both removal endpoints are now safe.

## Accepted-plan and documentation disposition

- Preserve the five accepted evolution identities and stage order in `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_2_event_flow_and_evolutions.md:381-576`.
- Preserve the source-wired active/pre-fire/logging implementation. Do not repeat the incident-family or Armed Birth follow-through tranche.
- Treat `docs/plans/006_independence_wave_plans/subagent_handoffs/006_evolution_incident_disable_guard_patch_2026_08_14.md` as the source receipt for the five removal-tail cleanup branches, with Event MCP evidence still partial and source commit `7a4e0d7a9` as the implementation receipt.
- Preserve League and ordinary super-event `24` source wiring.
- Keep ordinary super-event `23` blocked. Do not select audio, create wrappers, or add a firing transaction from this audit.
- Keep the whole event at HOLD / PARTIAL and do not change central admission, package attestations, asset rights, workbook rows, or unrelated shared UI.

## Assets, documentation, and remaining blockers

No new visual asset is needed, and no safe local source defect remains. The five incidents reuse the existing Event 006 wave-summary report image, League news uses accepted ASSET-004, and ordinary super-event `24` retains its final source-wired package.

Ordinary super-event `23` remains blocked on explicit audio selection, worldwide redistribution rights, human listening, composition-jurisdiction review, wrappers, and parent-owned firing. That blocker is intentionally outside this safe source tranche.

No gameplay, central admission, audio, asset, localisation, workbook, scripted GUI, or League source was edited by this auditor. Only this handoff was updated to retire the stale current-gap classification.

The shared worktree was already dirty, including concurrent modifications to `common/scripted_effects/006_independence_wave_effects.txt` and `common/scripted_effects/006_independence_wave_super_event_effects.txt`. This audit read the current workspace versions, did not alter or revert them, and does not present the worktree as clean.
