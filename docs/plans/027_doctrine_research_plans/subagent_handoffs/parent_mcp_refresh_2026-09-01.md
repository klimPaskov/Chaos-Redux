# Event 027 parent MCP refresh

## Superseding 2026-09-04 refresh

The current source is now registered as repeatable, included in the default reworked-event allowlist, initialized through the normal startup registry call, and represented by a dedicated fail-closed no-valid-participant N/A reason in the shared Event Log availability path.

The fresh focused Event MCP lint returned `EVENT_INSPECTED_PARTIAL` at revision `57d351df319dd5e7cdd1aa154584e6ac6e4bde5f1e6d0689ede14544ce2eb4cc`, with zero direct Event 027 blocking diagnostics and partial validation caused by deferred large-workspace helper and lifecycle projections.

The earlier revision `fca01297b05d2df4d6d638282d986b847407830db4d98f3ff44b449fb0723dee` is not retained as a comparison-compatible graph by the current service, so the attempted Event MCP comparison returned `EVENT_REVISION_NOT_CACHED` and no before/after result is claimed.

Current doctrine and probability evidence, the visual-asset audit, and the remaining live-engine and presentation blockers are maintained in `docs/plans/027_doctrine_research_plans/documentation_state.md` and `docs/plans/027_doctrine_research_plans/mcp_evidence.md`.

Original refresh date: 2026-09-01.

This is the parent review of the current Event 027 source after the native mastery and AI owner-readiness pass. It supersedes older transport observations where the artifacts below are newer, but it does not waive the acceptance criteria or claim live-game completion.

## Native mastery conclusion

The installed vanilla documentation confirms `add_mastery` as a country effect, `set_sub_doctrine` as the native empty-track assignment effect, and `has_mastery_level` as the native reward-level readback trigger. The console command named `mastery` is a separate developer command and is not used by the mod source.

Event 027 uses explicit native `add_mastery` branches for all 107 registered subdoctrine/track tuples with `amount = constant:doctrine_research_event.mastery_point_increment`, currently one raw mastery point. Each branch rereads native mastery and stops only at the exact pre-level plus one expected reward level, so a single choice cannot intentionally cross multiple mastery levels and banked progress is retained. There is no missing mastery command or mastery implementation blocker here.

Empty-track branches use native `set_sub_doctrine`, reread the resulting level, and either apply one exact Event 027 step when another level remains or record the native banked-completion adoption without consuming the choice. The source still requires live engine evidence for that combined transaction before acceptance.

## Current MCP evidence

The direct installed `hoi4-agent-tools` v3.0.6 JSON-RPC runner is healthy and returned a current file-scoped `hoi4.event_inspect` lint result for `chaosx.nr27.1`: `EVENT_INSPECTED_PARTIAL`, status `ok`, no direct Event 027 blocker, revision `d56afb96621c5db5d4ea7fdf4f8524e99aeab1b51652ab8d0c60f7750cc8a6b5`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3920ae58192f31d34f6a43d141e4f043e966b2064db470c9e723ebc2393a3f67/c7438ad3a302e110248c15549698267fa842fa487bd3d2deeef874e51f6b6936/event-lint-d56afb96621c.json`.

A second file-scoped lint over `events/027_doctrine_research.txt` is represented by the current focused result above; the runner reports no direct Event 027 blocker and only the known deferred helper/lifecycle analysis.

The same runner returned a current file-scoped options render through `events/027_doctrine_research.txt` at revision `d56afb96621c5db5d4ea7fdf4f8524e99aeab1b51652ab8d0c60f7750cc8a6b5`. Its manifest is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f087a48db7a7ddbbfd9651069b5f6e95e493c8f0e433a3ed9fbd4b5cc256487a/d793a3bce603c9ae1ed4803e3dbf9d776129a115153965cdee6d9c9c84d133f0/event-options-d56afb96621c-manifest.json`. The render is partial only because unrelated workspace helper/lifecycle analysis is deferred.

The current focused technology scan and four doctrine renders resolve Land/Chaos Warfare, Naval, Air, and Special Forces at shared revision `63ab11f1e42582df8d24719834b292ab93cb229540e90bab51cd795d0b71faf0`. The focused renders return `TECH_RENDERED` and select Land/Chaos Warfare, Naval, Air, and Special Forces nodes, but the aggregate index reports 1,417 blocking technology diagnostics and every render is explicitly `sourceAccurate: false`. These are source-resolution artifacts only, not source-accurate doctrine completion evidence.

The app-facing MCP bridge still returns `Transport closed` for the latest narrow event call in this task, while the direct local MCP runner returns normal structured tool results. This is an infrastructure limitation on the app route, not a missing native mastery effect.

## Current probability evidence

`hoi4.probability_inspect` against `common/scripted_effects/027_doctrine_research_ai_effects.txt` returned `PROBABILITY_SOURCE_INSPECTED`, zero parser diagnostics, 143 source candidates, and current source artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7186bf0fa1943427c965b57ede69a7e759568ca79af753c6a03f60187a573929/f2d2d205a68f210e50a5cfbb550c2eead3f2146632edb674a67578ad1bd96820/probability-inspect-cbf30e6c9ce4.json`.

The direct current evaluation of DR-A01 through DR-A06 used the complete five-entry domain pool and typed score fixtures, returned `PROBABILITY_ANALYZED`, 30 scenario-candidate rows, zero unresolved inputs, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/96bb7aaa2c95ff29097ac3a88cff79b84dffbc594602cf07dce3e156a9b752ac/9a97f53ba823a99337b92bb9ba80e091296b32c3b3d010d31a58bbbe54e2c6a5/probability-14eaa2038aab24ed85b57be6.json`. This is exact score-fixture evidence, not native GER/JAP/USA/SOV/FRA/ITA campaign-state evidence.

The completed read-only AI auditor handoff is `subagent_handoffs/ai_probability_auditor_current_2026-09-01.md`. It correctly leaves native country-state, sequence, invalid-adapter, DLC, and before/after comparison scenarios unresolved and makes no acceptance claim.

## Source review changes

The AI domain scorer now grants Navy owner-readiness weight only when a coastal state, naval production, an observed fleet, or an active naval doctrine is present, and grants Air owner-readiness weight only when an observed air force, military production, or an active air doctrine is present. The human validity pool remains governed by the native doctrine adapter predicates.

The source continues to use one bounded `every_country` fanout only inside the firing effect; no recurring whole-world on-action was added. Batches remain country-owned and append-only, and new countries are not visited until a later firing.

The authoritative catalog refresh is complete. The current spreadsheet worker handoff is `subagent_handoffs/spreadsheet_worker_current_2026-09-01.md`; it records the four Cluster Memberships display-name corrections, confirms the Event 027 and National Breakthroughs rows, and records the regenerated XLSX-derived CSV exports. The parent then aligned the Event 027 Details and National Breakthroughs membership note with the player-facing mastery-step and curriculum wording, and regenerated the exports again. The catalog remains `Needs Testing` rather than acceptance evidence.

The parent also removed dead Event 027 option-tooltip keys and tightened the track, confirmation, ambiguous-result, and native-completion wording. The post-fix localization audit is queued as `subagent_handoffs/localisation_auditor_post_fix_2026-09-01.md`; it does not waive the unresolved production-layout evidence.

## Acceptance disposition

Event 027 is source-playable: manual or cluster dispatch reaches the country-owned queue, humans receive the chained domain/Grand Doctrine/track/subdoctrine/confirmation/result flow, and AI countries use the same validity predicates and resolve silently. The native mastery step is a real `add_mastery` transaction with exact native readback, not a placeholder or an absent command.

Event 027 is not acceptance-complete or committed. Remaining blockers are live engine mastery and persistence traces, full lifecycle/controller evidence, consumer Event Log/Event Details/pagination presentation evidence, all 37 native probability scenarios, a genuine baseline-to-current probability comparison, a complete event comparison, source-accurate technology evidence, and final audit confirmation after the workbook refresh.
