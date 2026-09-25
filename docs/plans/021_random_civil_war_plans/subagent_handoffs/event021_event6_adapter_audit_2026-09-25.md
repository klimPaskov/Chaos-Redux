# Event 021 / Event 006 adapter anchor and capital rollback audit

Status: bounded source audit written on 2026-09-25. No gameplay source was changed. This handoff is evidence of implementation observed in the current working tree, not design approval or live-game certification.

Disposition: unresolved for engine-level event coverage, weighted-selection scenarios, runtime rollback, and explicit acceptance of the primary-anchor relationship. The source-level checks below are useful but do not close those items.

## Prioritized findings

### P1 — source-level anchor exclusions and rollback order are coherent

The Event 006 package finder iterates Event 021's complete-package registry and dispatches the existing Event 006 package loader before evaluating the package's candidate anchor. It admits only a host-owned and host-controlled anchor with population and infrastructure, and now rejects capitals, globally reserved states, registered front states, and scenario-reserved states unconditionally. A present carrier must pass Event 006 runtime-package preflight and must not be the host; a missing carrier is eligible for registry-controlled release. Selection targets and owner-side validity flags are written only after those checks. Evidence: common/scripted_effects/021_random_civil_war_parent_effects.txt:152-216.

Secondary-front revalidation repeats ownership/control, noncapital, global reservation, active-front, and scenario-reservation checks immediately before transaction setup. Evidence: common/scripted_effects/021_random_civil_war_parent_effects.txt:4219-4227.

The prior-capital helper clears its owner flag before capture, checks that the selected carrier has an owned capital before entering capital_scope, saves the state as a regular event target, and sets the validity flag on the selection owner. Rollback requires that owner flag, target existence, state existence, and ownership by the exact selected carrier before set_capital; the helper then clears the flag whether restoration occurred or not. Evidence: common/scripted_effects/021_random_civil_war_parent_effects.txt:3831-3865. This is consistent with the offline wiki guidance to guard potentially invalid scopes and the vanilla effect contract for regular event targets.

Both capital-setting transfers explicitly use remember_old_capital = yes. The primary opening captures the prior capital before transferring the planned global anchor and setting it as capital: common/scripted_effects/021_random_civil_war_parent_effects.txt:4396-4412. Its failure path returns the transferred anchor to the original host first, then restores the carrier capital, performs adapter cleanup, and only then annexes a carrier released for the failed transaction: common/scripted_effects/021_random_civil_war_parent_effects.txt:4011-4045 and 4455-4466. The secondary path transfers and capitals the selected package anchor: common/scripted_effects/021_random_civil_war_parent_effects.txt:4260-4274. Its rollback returns that anchor to ROOT before restoring capital and cleaning up the actor: common/scripted_effects/021_random_civil_war_parent_effects.txt:4135-4184. Shared cleanup clears the previous-capital validity flag and selected actor/anchor flags: common/scripted_effects/021_random_civil_war_parent_effects.txt:4090-4126.

### P1 — Event graph/render/compare evidence is still unresolved

The adapter auditor's corrected event_inspect and event_render requests did not return before that worker was stopped. The parent independently refreshed `hoi4.event_inspect` lint for `chaosx.nr21.1`; it returned `EVENT_INSPECTED_PARTIAL`, zero blocking diagnostics, and `validation.passed = false` because workspace-wide helper/lifecycle projection was deferred. The graph revision was `f50fb76d44de057fe86eff72c777b7748ed6d79862f47b0fef136453dabd22de`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f5022ee6de49504b3134a00c42409e601c051e2c82e18f76fc82a6dc4ab7d9bc/60c4f3d0ddbd48038b039f0165a63634f093284288bd5684cd949436a7f805e9/event-lint-f50fb76d44de.json`. It does not prove the changed helper bodies. No current Event 021 event render or event_compare result was obtained; that evidence remains pending, not proof that the MCP route is unavailable.

The bounded map_inspect request completed for all 32 package anchor state IDs and returned MAP_INSPECTED with inspectedStateCount = 32 and an overview artifact. Its workspace-wide locator validation failed and diagnostics were truncated: the reported global set includes 1,323 MAP_BUILDING_POSITION_INVALID and 1,331 MAP_PORT_ADJACENT_SEA_INVALID errors. Those diagnostics are not attributed to the 32 Event 006 anchors without inspecting their individual records. Map inspection artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d99d89c81943b67f6d07f2c4e74b4fdbd9f2d963ab04664cc493ec1c771a0ce7/04c92b0536fbc25472b7e93b21ce5d594c209589cc4efc25e68f5f59dc472fa3/map-inspect.7807270f81046f4b.json. Rendered overview artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/06862ee46ae6ff2778002719a3bbd5bcd567fefa7fd3c1da0f612bd363b84d11/46ee0ce2fe9fb927e16d70d3003207e843b266d3b9402d4563ce08ffe141ac89/map-overview.7807270f81046f4b.png.

### P2 — primary package-admission anchor and transferred front anchor resolve to the same planned state

Parent resolution: the automatic Event 006 route in `event021_parent_plan_connected_states` copies `random_civil_war_event6_selected_anchor` into the host's `random_civil_war_anchor_state` and reserves that same state. `event021_parent_prepare_crisis_identity` then saves `random_civil_war_anchor_state` as `random_civil_war_global_anchor_state`; the primary front-plan row captures that target, and `event021_parent_load_planned_primary_front` reloads the same planned state before transfer. Evidence: `common/scripted_effects/021_random_civil_war_parent_effects.txt:2028-2041,2540,1806-1813,1936-1971,4389-4406`. Therefore the primary package-admission anchor and committed front anchor are the same state by source flow; no design ambiguity remains. MCP graph and live execution evidence for the chain remain open.

### P2 — Event 006 lifecycle isolation is supported by the adapter call path

The adapter invokes Event 006's package-only preparation entry, then the established package setup dispatcher, and requires the Event 021 package-complete proof before recording identity/origin receipts. Evidence: common/scripted_effects/021_random_civil_war_parent_effects.txt:3951-3965; common/scripted_triggers/021_random_civil_war_parent_triggers.txt:133-136; common/scripted_effects/006_independence_wave_effects.txt:854-866 and 3731-3759.

Event 021's origin recorder writes Event 021 provenance, and its adapter receipt only sets Event 021 completion flags. It does not call Event 006's normal origin initializer or the active-origin, fired-count, evolution, or league commit paths. Evidence: common/scripted_effects/021_random_civil_war_effects.txt:1094-1123 and the separate Event 006 normal origin/activation/commit path at common/scripted_effects/006_independence_wave_effects.txt:850-928. This supports source-level isolation; the unreturned MCP graph and absent live execution prevent claiming engine/runtime proof.

The registry adapter is explicitly package-only and its source contract forbids mutation of Event 006 lifecycle, league, cap, weight, evolution, and released-package registries: common/scripted_effects/006_independence_wave_event021_adapter_registry_effects.txt:1-7. The registry trigger surface is common/scripted_triggers/006_independence_wave_event021_adapter_registry_triggers.txt:8-43. The complete-package API is documented at docs/events/006_independence_wave/systems/country_registry.md and backed by docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv.

### P2 — probability audit not completed

The Event 021 parent source contains a weighted archetype selection surface upstream of the deterministic Event 006 package finder. The mandated chaosx_ai_probability_auditor was closed before returning a scenario-specific MCP probability pass because the user requested immediate delivery. Close operation observed agent status "running". A prior Event 021 probability handoff exists at docs/plans/021_random_civil_war_plans/subagent_handoffs/ai_probability_audit_current_source_2026-09-25.md, but its recorded parent-effects hash 57DB1DFCDAD699482F9B3313E58A7A0FF87A14DBF00EDC7B0CA35CABFD90A781 differs from the current source hash 59A832ED6B38F101BAF971A1773A1D831E53EE9F6D26560DC568F3197323B751, so it is not current-source validation. Do not infer the weighted-choice result from that prior report.

## Validation performed

- Command: python .tools/audit_event6_allocator.py --strict
- Result: exit 0; Event 006 allocator audit passed. Reported 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, 40 runtime adapters, 32 attested packages, and 29 compatible reservation groups; eight adapter-only IDs were fail-closed.
- Command: python .tools/audit_event6_country_api.py
- Result: exit 0; Event 006 country API audit passed: broad = 242 unique tags, resolved = 191 unique carriers, Soviet = 34, Africa = 45, missing = 0, duplicates = 0, IW-031 crosswalk = pass.
- Read-only HOI4 map inspection: MAP_INSPECTED; 32 requested states inspected, with the workspace-wide locator caveat described above.
- No gameplay source edits, map writes, source overlays, or commits were made.

## References checked

The installed vanilla effects documentation at C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md was consulted. It documents save_event_target_as at lines 6496-6503, set_capital and remember_old_capital at lines 6655-6666, and transfer_state_to ownership/controller semantics at lines 8332-8344.

Offline wiki references consulted: paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:303-316 for regular event-target lifetime; paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md:329-349 for invalid event-target scope guarding and 388 / 533 for capital_scope and owned-state patterns; Triggers - Hearts of Iron 4 Wiki.md for has_event_target and is_capital.

Relevant prior handoffs reviewed: docs/plans/021_random_civil_war_plans/subagent_handoffs/event006_adapter_abort_cleanup_2026-09-20.md and docs/plans/021_random_civil_war_plans/subagent_handoffs/event6_secondary_front_architecture_2026-09-01.md. These provide implementation history and known validation limits, not design acceptance.

## Coverage checklist

- [x] Candidate package search, complete-package registry use, human-carrier preflight, and unconditional anchor exclusions reviewed.
- [x] Primary and secondary capital capture, remember_old_capital use, rollback ordering, owner/existence guards, and cleanup flag reviewed.
- [x] Event 006 package-only setup, Event 021 origin receipt, and source-level lifecycle isolation reviewed.
- [x] Current Event 006 allocator and country API audits passed.
- [x] Parent Event 021 root lint returned partial MCP evidence with zero blocking diagnostics; helper/lifecycle projection remains deferred.
- [ ] Current Event 021 / Event 006 event render evidence returned.
- [ ] Event comparison and weighted-probability scenario pass returned.
- [ ] Anchor-specific map record/render review separated from workspace-wide locator diagnostics.
- [ ] Runtime primary/secondary success and abort sequences verified in game.
- [ ] Accepted design basis recorded for the primary distinction between package-admission anchor and committed Event 021 front anchor.

## Limits and handoff

No live Hearts of Iron IV session, save-state simulation, or rollback execution was run. The MCP calls were stopped before their corrected results returned; no event graph, event render, or event comparison claim is made. The probability audit was closed without results. The allocator and country API scripts validate registry/crosswalk structure, not in-game package execution. Continue with the pending MCP event inspect/render/compare and scenario probability workflow before treating the adapter as fully validated.

Only this requested handoff file was created. The existing dirty gameplay and documentation files were preserved.
