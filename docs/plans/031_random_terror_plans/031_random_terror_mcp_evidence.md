# Event 31 Random Terror MCP evidence ledger

## Purpose

This ledger records the mandatory HOI4 MCP routes used against the current Event 31 implementation and preserves exact blockers where a route did not return evidence.

Source review, local validation, wiki references, and vanilla precedents remain required in parallel and are not treated as substitutes for a failed MCP route.

## Workspace

- MCP workspace: `mod_chaos_redux_ea3b2d67c2c0`
- Event root: `chaosx.nr31.1`
- Focus tree: `random_terror_actor_focus_tree`
- Shared scenario GUI: `chaosx_scenarios_window`
- Shared super-event framework: Event 31 slots `114` and `115`

## Event route

The narrow post-repair event lint for `chaosx.nr31.1` completed with no blocking diagnostics.

- Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5d493356efdd2fec675d0ad2b4da7da857c9b5ff5017ecb79ab440cf82336878/a4c54b601df599852226342a16112bdb27b658b0370620af0cfed05893e37384/event-lint-00d629f508b7.json`
- The event renderer did not complete within the tool limit and therefore supplies no current rendered-chain artifact.

## Focus route

The post-repair structural focus render covered all 114 Event 31 focuses and 104 connectors.

- Structural hash: `69ec88315409c5c578ffca2852052037f7ee6a48510a92189c11ac79a1a6d2a9`
- Structural diagnostics: zero connector crossings, zero node intersections, and zero same-row spacing violations.
- High-fidelity raster blocker: `tool call failed for hoi4_agent_tools/hoi4.focus_raster: timed out awaiting tools/call after 180s`

The earlier raster remains useful visual evidence for the icon family, but it is not post-repair topology proof.

## GUI routes

Event 31 introduces no dedicated scripted GUI, so the event UI worker and an Event 31 GUI rewrite are out of scope by accepted design.

The shared Global Jihad selection surface completed inspect and render at 1920x1080 with UI scale 1 using Event 31 selected, Random Pattern, and Maximum intensity.

- Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a92973eefa049d05f8bcd45622a120d0f4c83054c4354c9bb7df29160140c10f/5632b6e15e45b3065c52dfa6eaf61390432d48066f97c4f3d53d970211db9a93/gui-inspect.426cc63d2ec2c831.json`
- Render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5f6830b2501a441bcebdecc03874ce13a16f1d7e4d5ded5792c4ce73deab4906/f748c30500493d5bba5e686607517d49e5d10f6a2c6efcdd3b3e98c3a9ee9fab/chaosx_scenarios_window-full.svg`
- The inspector reported no missing Event 31 scenario fields.

The shared super-event framework route did not return fresh inspect or render evidence.

- Inspect blocker: `tool call failed for hoi4_agent_tools/hoi4.gui_inspect: timed out awaiting tools/call after 180s`
- Render blocker: `tool call failed for hoi4_agent_tools/hoi4.gui_render: timed out awaiting tools/call after 180s`

## Technology route

The technology compatibility route was invoked for the carrier baseline technology `infantry_weapons` with prerequisite and descendant tracing, sub-technologies enabled, depth 4, and a 100-node cap.

- Exact blocker: `tool call failed for hoi4_agent_tools/hoi4.tech_inspect: timed out awaiting tools/call after 180s`

The carrier history files still require source-level verification against installed vanilla technology identifiers, but that review is not reported as MCP evidence.

## Map route

The map inspector was invoked for state `104`, the dormant carrier fallback capital used before Event 31 transfers a live state and replaces the capital.

- Exact blocker: `tool call failed for hoi4_agent_tools/hoi4.map_inspect: timed out awaiting tools/call after 180s`

Exact state ownership, capital transfer, adjacency, and allocation checks still require source-level and country-package audit evidence, but those checks are not reported as MCP map evidence.

## Probability route

The previous baseline handoff records partial and failed probability routes and cannot support a final balance claim.

The current comparison pass is assigned to `chaosx_ai_probability_auditor` against the complete accepted scenario matrix.

Its final artifact references, scenario evidence classes, and exact blockers belong in `031_random_terror_probability_comparison.md`; until that file is complete, the probability route remains open.

## Completion status

This ledger is evidence bookkeeping, not a completion claim.

Event, focus, GUI, technology, map, and probability entries must be reconciled with the final subsystem audits and completion review before Event 31 can be declared complete.

## Current-route refresh on 2026-10-03

The connected tool list exposes the domain event, focus, GUI, map, technology, probability, and job routes.

It does not expose `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, or `hoi4.source_lookup`, despite those names appearing in domain-tool descriptions.

The relevant local sections were read directly for the achievement scope correction and cited with line spans and SHA-256 revisions in `subagent_handoffs/031_achievement_count_scope_repair_20261003.md`.

The parent ran `hoi4.probability_inspect` for the current random-list source at `common/scripted_effects/031_random_terror_effects.txt`.

The result was `PROBABILITY_SOURCE_INSPECTED`, status `ok`, with 43 candidates and no blocking diagnostic.

- Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6c4092e607cd537105825ac0ac1f62f1d66c59238e2d900660add04fb977d58a/71884521ae2611878c3549f3ffef097abf208dac55ca7b1de252b3920cc5ac92/probability-inspect-101a27aa2c7e.json`
- Local verified copy: `evidence/probability-inspect-101a27aa2c7e.json`
- Exact length: 45,369 bytes
- Verified SHA-256: `6c4092e607cd537105825ac0ac1f62f1d66c59238e2d900660add04fb977d58a`
- Source revision: `85ff082442e553991cd74374d5548b720ba38addd0760208f4b81db1474fbf5b`
- Source analysis hash: `101a27aa2c7e02ce918492115b30437e730e3978d774b90da961728cb24a0e71`
- Underlying indexed source hash: `0ffb0b284b492ae08213a0e29565ecfb91ed0f2a34f5653736cf97061a224096`

The artifact identifies all 24 entries in `random_terror_apply_incident` plus the separate scenario-pattern and three raid-outcome pools.

Whole-file normalization is unresolved with `MULTIPLE_CATEGORICAL_POOLS`: `Select one event-option or random-list pool before requesting normalized probabilities`.

The parent supplied the exact 24 incident candidate IDs and current runtime weight values for a conditional draw evaluation.

The saved fixture is `evidence/incident-draw-scenarios-20261003.json`.

That fixture covers the draw before state-context remapping and does not prove the complete P01 campaign scenario or the P01–P10 acceptance matrix.

The conditional `hoi4.probability_evaluate` request ended with `tool call failed for hoi4_agent_tools/hoi4.probability_evaluate: timed out awaiting tools/call after 600s`.

No normalized probability, ranking, or unresolved-input artifact was returned for that request.

The fresh event lint request for selector `{ kind: event, eventId: chaosx.nr31.1 }`, depth 2, 40 nodes, 80 edges, and helper expansion disabled ended with `tool call failed for hoi4_agent_tools/hoi4.event_inspect: timed out awaiting tools/call after 600s`.

The previous successful lint remains historical evidence and does not prove the current scope repair passed a fresh MCP check.

The one-shot artifact transport returned truncated JSON, so the parent recovered it through 6,000-byte range requests and verified the final byte count and checksum before parsing it.

## Current subagent routing blockers

The named achievement architect `01a10018-5859-7781-af02-1ff1974afab5` and probability auditor `01a10018-61a1-7900-990a-d340088829df` each failed before executing the task with `workspace routing discovery timed out`.

The portrait worker `01a10018-4e39-72d0-bb53-3b8d21c82538` returned `not_found` when polled at continuation and left no new completion handoff.

Those results do not satisfy the required specialist completion audits.

The parent continues bounded implementation and evidence work, while final portrait consumer completion and specialist audit closure remain open.

The later completion auditor `01a10033-b9cf-7f13-bdcb-0c60442eb2c6` and documentation curator `01a10041-a2e2-7a60-9a16-9dc2a661a658` also failed before execution with `workspace routing discovery timed out`.

The focus auditor `01a10033-cfbe-7531-b95c-014bbf241cbd` was still running at its last authoritative poll and had not returned a final handoff.

## Subsequent source repair and commit state

The parent committed the country-owned achievement capital identity repair as `ed717ab21` after reviewing its exact source and handoff scope.

The ordinary-crisis capital and Maximum-scenario capital are separate persistent state references, capital-dependent completion checks require current ownership/control, and repeated capital loss does not extend the recovery deadline.

The implementation and validation limits are recorded in `subagent_handoffs/031_achievement_capital_identity_repair_20261003.md`.

The earlier count-repair commit's shared-index reconciliation completed after the lock cleared, and the capital-repair commit's own index reconciliation also completed.

Both reconciliations touched only their owned paths and preserved unrelated staged work.

No fresh successful MCP lint or live-game evidence is claimed for the capital repair.

## Reference-route refresh and control repair

The connected list subsequently exposed `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, and `hoi4.source_lookup`.

The parent used the live schemas for an event-surface context request, targeted searches for `is_ai` and `on_startup on_daily`, and the source lookup for `random_terror_achievement_record_tag_switch`.

All four requests ended with `timed out awaiting tools/call after 600s`.

No citation IDs or revisions were returned for a valid follow-up `reference_read`, so the parent read the relevant local sections directly.

The exact request roles, source sections, control-predicate cases, CXT correction, and validation limits are recorded in `subagent_handoffs/031_control_and_cxt_registration_repairs_20261003.md`.

Commit `1596b2bbf` contains the country-local control-change tracking and registration-only CXT pending marker repair.

Its real-index reconciliation completed after the parent confirmed there were no Git processes running, removed the stale zero-byte `.git/index.lock`, revalidated the six owned index entries, and restored only those paths to HEAD.

The source-predicate model does not observe client identity, same-day round trips, or swaps between countries that remain human-controlled.

The retried portrait worker `01a10067-9244-7df0-b09c-eb3daaf9c64b` and the focus auditor `01a10033-cfbe-7531-b95c-014bbf241cbd` both ultimately failed before execution with `workspace routing discovery timed out`.

No standalone workspace, server-health, version, or capability route appeared in the connected HOI4 tool list during this pass, so no server-health or native-task negotiation claim is made.

## Narrow reference and lint retries

The subsequent installed-documentation search for `is_ai`, limit two, returned a citation whose revision-bound read succeeded.
Read receipt: citation `55b2469d983f0aaea927cc8bf1ec92e5e3dfff7e97ee4990bfef37ec5f1c6b6b`, installed `documentation/triggers_documentation.md`, lines 5244–5252, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`.
It documents country-scope AI-control testing, not client identity or a tag-switch callback.
The wiki-only `is_ai` search returned unrelated Effects/General and MIO sections; those results do not establish wiki coverage of the AI-control rule.
The targeted helper lookup for `random_terror_achievement_campaign_is_valid`, no references, one definition and twelve lines, still timed out after 600 seconds.
No newer `view`/`keyPath` source-lookup fields or `script_validate` route were exposed; none were invented.

Two profile-reference searches, `set_research_slots` and `temporary variables scripted effects`, with limit two, timed out after 600 seconds.
The narrower `set_research_slots` retry restricted to installed documentation and limit one also timed out after 600 seconds.
The parent retained direct installed/wiki sections and hashes in `subagent_handoffs/031_local_actor_research_slots_repair_20261003.md`.
That bounded source change is committed as `24c3697126c406541f707f981ab844f98212cf95` and is not a complete technology/country acceptance claim.

The installed-documentation-only `set_temp_variable` search, limit one, timed out after 600 seconds.
The parent read the pertinent installed section and wiki return-lifetime warning directly, retained their revisions in `subagent_handoffs/031_caller_owned_temporary_outputs_20261003.md`, and committed the two caller declarations as `04689ecb13f203945be130d461fdf4eb957c043b`.
These declarations preserve existing configured values; no target ticket, probability weight, eligibility or pacing callback changed.

The reduced event lint retry used `chaosx.nr31.1`, depth one, four nodes, four edges, helper expansion disabled and refresh enabled.
It timed out after 600 seconds with `tool call failed for hoi4_agent_tools/hoi4.event_inspect` and returned no validation artifact.
This is narrower than the prior depth-two, forty-node/eighty-edge request.
The result does not close current helper, event-chain or lifecycle evidence; the successful historical lint remains historical.

## Terminal comparison and current audit delivery

The named probability auditor delivered `subagent_handoffs/031_terminal_role_probability_baseline_20261003.md` and `031_terminal_role_probability_comparison_20261003.md` around owner commit `87948c017`.
The original W01–W05/P10 fixture remains byte-identical at SHA-256 `13ac75bb269307d21667738ccf2387f52d6cd32cee3dd8a4f8559672c3738727`.
The auditor attempted focused probability inspections and comparisons for the single affected focus, seventeen direct actor-decision consumers and the complete four-option Event 31.7 pool.
All returned 600-second timeouts and produced no numerical artifact, source revision, analyzer scenario hash or ranking.
The source baseline and comparison distinguish those failures from observed game behavior and retain actor/pending-event/owned-state binding gaps.
The byte-identical event source was saved to a distinct before path for the event-option pair.
Transitive before-helper resolution is not established merely by copying the focused file, so future successful evidence must verify its dependency coverage.

The decision auditor's runtime exposed metadata but no callable HOI4 methods, returning `TypeError: tools.mcp__hoi4_agent_tools__<route> is not a function` before service dispatch.
The wave architect's runtime exposed neither HOI4 methods nor a tool-search route.
These are worker-specific exposure blockers, not claims that the parent lacks the exposed routes or that every service request timed out.
The country auditor retained separate 600-second event, focus, technology, map, reference and probability failures, plus its separately checked standalone-viewer package gap.
The exact requests, local source receipts and remaining limits are in their respective handoffs.

The parent confirmed the `hoi4_agent_tools` resource inventory is empty and its only exposed resource template is revision-bound artifact delivery with byte-range reads.
No health/version or probability-input-schema resource was discovered.
This does not establish server health, client task negotiation or a fixture schema.
No native job cancellation or helper-expansion route was invoked.

Eight exact pre-wave files were copied and hash-verified under `evidence/wave_scope_before_20261003/`, including the shared ticket effects/triggers/constants and their public API documentation.
No wave eligibility or ticket change preceded those snapshots.
The same probability auditor is assigned the new wave baseline and matching fixtures before the owner scope/output correction.
