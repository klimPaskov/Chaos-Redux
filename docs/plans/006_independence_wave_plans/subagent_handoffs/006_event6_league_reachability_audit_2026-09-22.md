# Event 006 League reachability audit handoff — 2026-09-22

## Status and conclusion

Status: **HOLD/PARTIAL**.

This was a read-only, evidence-only audit of the existing Independence Wave League surface.

No League architecture was expanded, no readiness or attestation flag was promoted, no gameplay or content file was edited, and no commit was created.

The named League scenarios are mostly source-statically reachable, but one concrete source-backed lifecycle defect prevents a clean reachability conclusion: the accepted `CongressFailed -> RegionalConferences` retry transition is defined as `independence_wave_reopen_regional_conferences` but has no caller anywhere in the current repository.

The parent can address that defect with a narrow patch to an existing League decision/effect path without adding a pillar, phase, GUI, focus lane, formable family, or event chain.

Event MCP evidence is structural and partial because workspace-wide helper projection and lifecycle analysis were deferred.

Typed probability evidence remains unresolved, and no source-only observation in this handoff is treated as balance evidence.

Live HOI4, save/load, timer progression, event-target persistence, and runtime consumer behavior were not tested and remain user-owned.

## Authority and accepted-plan disposition

- Event 006 remains HOLD/PARTIAL.
- The automatic allocator remains unchanged at 3/4/5/7/10, with World Collapse at 10.
- The accepted package accounting remains 32 content-attested selectable packages, 29 compatible reservation groups, 40 adapters, and 161 unattested selectable rows.
- The existing League design remains authoritative: four living Event 006 origins, three willing founders, congress preparation, five charter pillars, five route proposals, consultative/formal/durable phases, leadership and disciplinary actions, crisis/reform/split/reunification/dissolution, and generation-aware cleanup.
- The League proof item in `006_event6_next_safe_tranche_improvement_addendum_2026_08_29.md` is not promoted to implemented completion by this audit.
- The current implementation is source-backed for most accepted states and transitions, but the congress-failure retry defect, partial MCP lifecycle coverage, unresolved typed probability evidence, and unavailable runtime proof keep the addendum disposition at accepted/in-progress evidence rather than complete.
- `006_event6_league_lifecycle_audit_2026-09-05.md` is stale on two reachability statements: current decisions now call the consultative, upgrade, reform, normalization, reunification, dissolution, and restart effects, while its claim that DM45 timeout has an existing retry path is contradicted by the current single-definition/no-caller census for `independence_wave_reopen_regional_conferences`.

## Files and identifiers reviewed

### Accepted design and current authority

- `docs/specs/006_independence_wave_specs/`, including the accepted League specification, `diagrams/006_league_state_machine.md`, `matrices/006_decision_mission_map.csv`, the achievement matrix, and the relevant accepted prompts.
- `docs/plans/006_independence_wave_plans/006_event6_next_safe_tranche_improvement_addendum_2026_08_29.md`.
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`.
- `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md`.
- `docs/events/006_independence_wave/overview.md`.
- Current League, decision, rival-bloc, achievement, and MCP handoffs under `docs/plans/006_independence_wave_plans/subagent_handoffs/`.

### Runtime source

- `common/script_constants/006_independence_wave_constants_registry.txt`: League constants include `minimum_living_origins = 4`, `formation_members = 3`, `formation_cohesion = 50`, `formation_common_cause = 45`, `durable_members = 3`, `durable_days = 365`, `durable_cohesion = 60`, `fracture_cohesion = 20`, `fracture_confidence = 20`, and `charter_expulsion_member_minimum = 4`.
- `common/scripted_triggers/006_independence_wave_triggers.txt`: founder/member registry alignment, regional-conference gate, formal-formation gate, and durable gate.
- `common/scripted_triggers/006_independence_wave_decision_triggers.txt`: lifecycle action gates, exact selected-target checks, expulsion authority/target checks, and war-mandate target checks.
- `common/scripted_effects/006_independence_wave_effects.txt`: founder/member registries, generation reconciliation, regions/count rebuild, conference/congress/charter transitions, formal and durable entry, crisis/reform/split/normalization/reunification/dissolution/restart, shared reserve interaction, and origin-generation cleanup.
- `common/scripted_effects/006_independence_wave_decision_effects.txt`: selected-target storage/cleanup, war-mandate cleanup, and expulsion success/failure resolution.
- `common/scripted_effects/006_independence_wave_rival_bloc_effects.txt`: expulsion-created rival contract, split behavior, rival membership, reunification transfer, and rival cleanup.
- `common/scripted_effects/006_independence_wave_achievement_effects.txt` and `common/scripted_triggers/006_independence_wave_achievement_triggers.txt`: League achievement writers, clocks, predicates, and disqualifiers.
- `common/decisions/006_independence_wave_decisions.txt`: DM41-DM47 and DM58-DM62, plus the lifecycle decisions for consultative status, formal upgrade, durability, reform, normalization, reunification, dissolution, and restart.
- `common/national_focus/006_independence_wave_focus.txt`: `independence_wave_draft_league_charter`, `independence_wave_convene_league_congress`, and the five proposal focuses.
- `events/006_independence_wave.txt`: `chaosx.nr6.35` and `chaosx.nr6.309`.
- `events/006_independence_wave_support_events.txt`: support-event consumers were included in the source census; no separate core League transition chain is owned there.
- `common/on_actions/006_independence_wave_achievement_on_actions.txt`: war-mandate consumption, unauthorized-war evidence, member-war/annexation witnesses, and achievement disqualifiers.
- `common/achievements/chaos_redux_achievements.txt`: `chaosx_006_found_league`, `chaosx_006_cross_regional_league`, `chaosx_006_rescue_member`, `chaosx_006_radical_bloc`, and `chaosx_006_league_arbitrator`.
- Relevant decision categories, scripted localisation, and English localisation for the League category, decisions, focuses, routes, phases, events, and achievements.

### Principal IDs

- Founder/member arrays: `global.independence_wave_league_founder_entries`, `global.independence_wave_league_founder_generation_entries`, `global.independence_wave_league_founder_region_entries`, `global.independence_wave_league_member_country_entries`, `global.independence_wave_league_member_generation_entries`, `global.independence_wave_league_member_region_entries`, `global.independence_wave_league_member_contribution_entries`, and `global.independence_wave_league_member_confidence_entries`.
- Main phase effects: `independence_wave_open_regional_conference`, `independence_wave_complete_congress_preparation`, `independence_wave_fail_congress`, `independence_wave_reopen_regional_conferences`, `independence_wave_open_charter_vote`, `independence_wave_proclaim_consultative_league`, `independence_wave_proclaim_formal_league`, `independence_wave_upgrade_consultative_league`, `independence_wave_mark_durable_league`, `independence_wave_enter_league_crisis`, `independence_wave_reform_league`, `independence_wave_split_league`, `independence_wave_normalize_reformed_league`, `independence_wave_reunify_rival_leagues`, `independence_wave_dissolve_league_to_network`, and `independence_wave_restart_informal_network`.
- Main decisions: `independence_wave_contribute_emergency_reserve`, `independence_wave_request_collective_recognition`, `independence_wave_request_border_arbitration`, `independence_wave_rescue_threatened_member`, `independence_wave_convene_founding_congress`, `independence_wave_adopt_charter_pillar`, `independence_wave_challenge_league_leadership`, `independence_wave_establish_consultative_league`, `independence_wave_upgrade_consultative_league`, `independence_wave_begin_league_durability`, `independence_wave_reform_league`, `independence_wave_normalize_reformed_league`, `independence_wave_reunify_rival_leagues`, `independence_wave_dissolve_league`, `independence_wave_restart_informal_network`, `independence_wave_call_charter_expulsion_vote`, `independence_wave_sponsor_member_coup`, `independence_wave_request_charter_war_mandate`, `independence_wave_coordinate_reclamation_fronts`, and `independence_wave_transform_league_charter`.
- Five proposals: `independence_wave_propose_defensive_congress`, `independence_wave_propose_development_compact`, `independence_wave_propose_sovereign_equality`, `independence_wave_propose_armed_liberation`, and `independence_wave_propose_revisionist_charter`.

## Scenario coverage

Evidence classes used below are source/static PASS, source/static FAIL, structural/partial MCP, unresolved probability, and unavailable runtime proof.

| Scenario | Source/static result | Evidence and limit |
| --- | --- | --- |
| `LEAGUE_3_LIVING_FAIL_CLOSED` | **PASS** | `can_independence_wave_open_regional_conference` and `can_independence_wave_form_league` require the global active-country count to meet `minimum_living_origins = 4`; three living origins cannot enter the formation path. Runtime proof is unavailable. |
| `LEAGUE_4_LIVING_3_WILLING` | **PASS, conditional contract** | Formation requires four living origins, three aligned founders, prepared congress, shared strategic problem, cohesion 50, common cause 45, and every founder to remain live, a network member, non-client, and outside patron control. The source contract is complete; no live scenario was run. |
| `LEAGUE_CONGRESS_FAILURE` | **FAIL** | DM45 timeout calls `independence_wave_fail_congress`, which sets `congress_failed`. The accepted retry effect `independence_wave_reopen_regional_conferences` exists only as a definition and has no caller; DM45 is not available in `congress_failed`, so the accepted retry transition is source-unreachable. |
| `LEAGUE_FIVE_PILLARS_ADOPTED` | **PASS** | DM46 sets the first missing pillar in a fixed five-pillar sequence and, after all five are present, selects the proposer route and calls formal proclamation. Runtime sequencing was not exercised. |
| `LEAGUE_EACH_ROUTE` | **PASS for reachability; probability unresolved** | All five proposal focuses set distinct proposal flags and DM46 maps them to the five authored route values. Visibility/availability gates exist for patron and chaos restrictions. No typed AI-selection or quantitative balance conclusion is available. |
| `LEAGUE_LEADERSHIP_CHALLENGE` | **PASS** | DM47 is visible/available in formal or durable phases for a compliant active member with the required standing; success transfers the current leader and failure applies the authored losses. Timer and concurrent-candidate behavior remain runtime-unproven. |
| `LEAGUE_MEMBER_EXPULSION` | **PASS for source path; runtime partial** | DM60 requires exact leader authority, at least four members, an exact selected member, and a recorded charter ground; success unregisters the member, records the achievement disqualifier, and opens the rival contract/split path. Timed target persistence and runtime cancellation remain unproved. |
| `LEAGUE_WAR_MANDATE` | **PASS for source path; runtime partial** | DM62 validates an external living nonmember target, writes a target-specific 365-day authorization and metadata, and `on_war_relation_added` consumes the exact authorization or records an unauthorized-war expulsion ground. Timed-flag expiry and save/load persistence remain unproved. |
| `LEAGUE_FAILED_RESCUE` | **PASS** | DM44 failure sets `independence_wave_league_failed_rescue`; `independence_wave_enter_league_crisis` consumes that global witness as a crisis cause; reform/dissolution/restart cleanup clears it. No live rescue timer was run. |
| `LEAGUE_CRISIS_REFORM` | **PASS** | The crisis gate and `independence_wave_reform_league` decision/effect path are present and enter the reformed phase with the accepted state changes. Runtime availability and player-facing sequencing remain unproved. |
| `LEAGUE_CRISIS_SPLIT` | **PASS** | Expulsion-created rival-contract logic enters crisis and calls `independence_wave_split_league`; the separate rival registry and route are source-wired. Runtime transfer and simultaneous cleanup remain unproved. |
| `LEAGUE_RIVAL_REUNIFICATION` | **PASS for source path; runtime partial** | The reunification decision calls the main reunification effect, transfers valid rival members through generation-aware registration, and dissolves the rival contract. No live member-array migration or save/load test was run. |
| `LEAGUE_DURABLE` | **PASS for source path; runtime partial** | The 365-day durability mission requires at least three members and cohesion 60, rechecks validity, marks the durable phase, and publishes the durable outcome. Timer completion and publication delivery remain unproved. |
| `LEAGUE_GENERATION_CLEANUP` | **PASS source-statically; MCP lifecycle partial** | Founder/member rows carry generation values; reconciliation drops dead, mismatched, nonmember, and stale rows; origin cleanup unregisters founder/member state and clears a matching leader target; dissolution/restart clear arrays, charter-generation flags, leader variables, and global target state. MCP explicitly deferred workspace-wide lifecycle analysis, and no save/load or tag-reuse run was performed. |

## Surface findings

### Founder/member registries and minimum living-origin calculation

The founder and member registries use aligned arrays and generation values rather than tag-only membership.

Registration rejects dead/inactive origins, stale generations, duplicates, incompatible client state, and main/rival cross-membership where applicable.

Reconciliation rebuilds founder/member counts and regional coverage after invalid rows are removed.

The four-living/three-founder split is source-explicit and fail-closed through the formation trigger.

This is a source/static PASS, not runtime evidence of array alignment through save/load or tag reuse.

### Conferences, congress, charter, pillars, and routes

Regional conference, congress preparation, charter vote, all five pillars, and all five route proposals are authored and have current callers.

DM45 writes the regional/preparation/vote states on success and the failed-congress state on timeout.

DM46 serializes pillar adoption and dispatches the selected formal route once the charter is complete.

The only confirmed reachability defect in this audit is the missing caller from failed congress back to regional conferences.

### Formal/durable phases and governance actions

Consultative proclamation, consultative-to-formal upgrade, direct formal proclamation, durability, leadership challenge, expulsion, coup, and war mandate all have decision or effect consumers in the current tree.

The 2026-09-05 handoff statement that most of these effects lack active callers no longer describes the current source.

DM45 still lacks a global single-congress latch: its crisis/active-action guards are country-local and `fire_only_once` is per decision owner.

That is recorded as a structural concurrency risk requiring parent/runtime review, not as a second confirmed defect, because this audit did not execute concurrent founder missions.

### Crisis, reform, split, reunification, dissolution, reserve, and cleanup

Low League values, failed rescue, member war, patron capture, and rival pressure can feed the crisis effect.

Existing decisions call reform, normalization, reunification, dissolution, and restart effects.

DM41 writes the shared reserve, while reclamation, rival, crisis, and route effects consume or adjust it through existing constants.

Dissolution and restart clear the active charter pillars, radical charter state, failed-rescue latch, leader country flag, leader event target/variables, member/founder arrays, counts, and generation-local member state while retaining historical receipts.

Generation mismatch behavior is source-defensive but lacks MCP lifecycle completion and runtime/save-load proof.

### Route/phase visibility and availability

The League category and its actions are gated by active Event 006 country status, network/member/founder role, exact phase, crisis state, selected-target validity, client/patron restrictions, standing, and action-in-progress state.

The five proposal focuses have distinct route conditions and all set the proposal flags consumed by DM46.

The decision-level crisis lock is country-local, so the absence of a global DM45 concurrency latch remains a review item.

No new route or phase is recommended or authorized by this audit.

### Focus callbacks and event consumers

The League focus lane sets the accepted charter/congress/proposal flags and calls the existing League effects.

`chaosx.nr6.35` is the first-congress news consumer fired by the existing proclamation path.

`chaosx.nr6.309` is the DM58 reclamation-front expiry callback and validates the stored coordinator target before cleanup.

No additional event chain is required to describe the current source reachability, and none is proposed.

### Achievement writers and disqualifiers

`chaosx_006_found_league` requires a naturally formed, non-scenario League, the founding-actor receipt, at least the configured founding-member threshold, all five pillars, and a formal/durable/reformed phase.

Formal proclamation and consultative upgrade call `independence_wave_achievement_mark_formal_league_founders`.

`chaosx_006_cross_regional_league` uses the member/region/cohesion threshold clock and disqualifies scenario-preformed and radical/revisionist membership.

`chaosx_006_rescue_member` is written by the successful rescue decision and requires the protected target to remain active, independent, uncapitulated, and outside voluntary reunion for the configured survival period.

`chaosx_006_league_arbitrator` is written by peaceful arbitration and disqualified for member war, coercive settlement, or member expulsion during the leadership term.

`chaosx_006_radical_bloc` has a current qualification writer and rejects scenario-forced danger.

The writers and disqualifiers are source-wired; date clocks and on-action witnesses remain runtime-unproved.

### Localisation coverage

A targeted exact-key census checked 61 current League category, decision, focus, and `chaosx.nr6.35` title/description/option keys and found zero missing keys.

This was a coverage check only; it does not prove in-game interpolation, scripted-localisation scope resolution, clipping, or readability.

## MCP artifacts and limitations

### `chaosx.nr6.35`

- `hoi4.event_inspect`, trace/both, returned `EVENT_INSPECTED_PARTIAL` at revision `5d73a0f565b8e820a715982b124b7e4de595a0c6619f59cebf2dca66ed924d1e`, graph hash `3b646fa519df44eaaa1b3525b1988109369902b9eaaec315dc54f2cd3887b585`, with zero blocking diagnostics.
- Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e6a480338b4ac52609f5a5e4c018c0d58236c4499b05d80ef7355fd026332b0a/6a5a3b4a65c7df9c4d0d96cc0d6d8d5f6fc94ef4de9095a09de4d36557aeae8e/event-trace-5d73a0f565b8.json`.
- `hoi4.event_render`, reachability/both, returned `EVENT_RENDERED_PARTIAL`, selected 3 nodes, and omitted 42,793 nodes.
- Render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c755ed9c70638fd7d36993ff524b407cb970d7fbcbd98cc152781c221e9767bf/0448bf45f0de67c5673de84ff1bed158be25bf91fbb6b110a5ced3e6652ddebd/event-reachability-5d73a0f565b8-manifest.json`.
- Render JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a73b3d410aeb33f6062905731ddc4e74be8bb295e325213c36b2eb8b57b5e352/ad25180b88f6381b23bbaee90e41d27b45505ccbda7ad0399c9fbcfe1f016ac9/event-reachability-5d73a0f565b8.json`.
- Render SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4a97d7a8cf724d1f03ff662c751bc6f767518d15f5f727356175d9cda28ec3b7/6c3a300a5463c328b10643bca8036a127567c5bdcd4b56bb669f9c5b2d94355f/event-reachability-5d73a0f565b8.svg`.
- Render PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/471f989e1d108edfa3d5c16ce682e100ac3179606a78115ee521d281dd471d70/7c13726cace9768d693b82bdb65fc2f135b83e8dea56aaac9408bb80ea8c2a59/event-reachability-5d73a0f565b8.png`.

### `chaosx.nr6.309`

- `hoi4.event_inspect`, trace/both, returned `EVENT_INSPECTED_PARTIAL` at the same revision and graph hash with zero blocking diagnostics.
- Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b3f02d82b953f2e0d09e4f086c660d3c6360a1ed6f4b1378272bfea63733842e/791127f47c039a5e3f3351bd28cfa4f746cb334996e670c31d05e6701dd06a18/event-trace-5d73a0f565b8.json`.
- `hoi4.event_render`, reachability/both, returned `EVENT_RENDERED_PARTIAL`, selected 2 nodes, and omitted 42,794 nodes.
- Render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fe91d0b70f153a542b0e40fc31a0116f893b089d67ec1b21328d8b2a05872a5e/209a9144f4977836322d4c0acece300180286be69a51347481889aeb8e7e2958/event-reachability-5d73a0f565b8-manifest.json`.
- Render JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c5209d514cce10094097594098eefc63b90f3523351e7cdcbc1eb101ed27ccba/e9e9d7f1a02d4002175c4e674b5abb9649810889be7c32ea21bfc46e65f3db75/event-reachability-5d73a0f565b8.json`.
- Render SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9573dee6b84aef5f0b15d631fc74c2a932474a4e349c2d8e62ae43df09b7f6ae/4fb6a406b4c37436d3d5f27a4059594b1a2f5eb9f3398ef96e44338e5645bce5/event-reachability-5d73a0f565b8.svg`.
- Render PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6ceeb8ea034c28b7b046abb83c8a1e3e165d60630e045b544c89a9fe36ca9648/0ba87672aa43dcc32bcda6050ac07a450d98322fab43063706c965b478581ff9/event-reachability-5d73a0f565b8.png`.

### MCP limits

- Both inspections report 9,827 events, 15,178 options, 1,166 entries, 38,502 edges, 30,713 state accesses, 8,858 unresolved nodes, 2,198 diagnostics, zero blocking diagnostics, zero skipped sources, and zero expanded helpers.
- Validation is false only at the reported analysis boundary: the service explicitly deferred workspace-wide helper projections and lifecycle passes and linked direct evidence instead.
- The inline source inventory was truncated to 64 of 381 paths; the artifacts retain the full inventory.
- No helper expansion, job inspection/cancellation, or native task was attempted because a health/version and live-schema route was not exposed in this session and those routes were not needed for the bounded event calls.
- A required comparison was attempted against the recorded 2026-09-05 revision `1102e50fad94d2051bd32d8a7cd64c3429a191f53e98c50d02aeb60327e1dae8`; `hoi4.event_compare` returned `EVENT_REVISION_NOT_CACHED`, so no comparison artifact exists and no before/after claim is made.

## Probability evidence

The League decisions and focuses contain `ai_will_do` and related weighted surfaces, so source review of their weights is not accepted as balance evidence.

A read-only `chaosx_ai_probability_auditor` sidecar was dispatched with the 14 named scenarios and instructions to start with `hoi4.probability_inspect`, make no patch, and stop with exact incomplete coverage if adapters were unavailable.

The auditor did not return within the bounded completion window used for this handoff.

Accordingly, this handoff records **no typed probability artifact, no quantitative scenario result, no balance conclusion, and no probability PASS**.

No weighted surface was changed, so no `hoi4.probability_compare` was applicable to a patch in this audit.

## Skipped validation and blockers

- No HOI4 process was launched.
- No live League formation, concurrent congress, mission timer, crisis, split, reunification, dissolution, tag reuse, or generation cleanup scenario was executed.
- No save/load or event-target persistence claim is made.
- No publication-delivery claim is made for `chaosx.nr6.35`, `chaosx.nr6.309`, or durable-League presentation.
- MCP helper/lifecycle projection is incomplete by explicit service report.
- The recorded MCP baseline revision is not cached, so event comparison is unavailable.
- Typed probability evidence is unresolved because the named probability-auditor sidecar did not return before this handoff was closed.
- The shared Statehood Ledger GUI was not audited in this reachability-only task; no dedicated League GUI is introduced or proposed here.
- Asset, portrait, animation, 3D, and audio production were not in scope.
- Existing unrelated dirty-worktree changes were preserved and not inspected as League evidence.

## Recommended parent actions

1. Apply a narrow parent-owned patch that gives `independence_wave_reopen_regional_conferences` one existing, accepted retry caller after `congress_failed`, with the accepted cooldown/changed-condition gate, then re-run `LEAGUE_CONGRESS_FAILURE` source and MCP evidence.
2. Review whether DM45 needs a global congress-in-progress latch; treat this as a concurrency question until a runtime or stronger typed lifecycle scenario proves a duplicate-congress failure.
3. Re-run `chaosx_ai_probability_auditor` for the same named scenarios when the probability workflow is available, and retain its typed artifacts before making any AI/balance claim or weighted patch.
4. Let the user validate live formation, timers, event-target persistence, split/reunification transfers, durable publication, and generation cleanup in a new live session.

## Explicit no-patch conclusion

No gameplay, localisation, asset, GUI, GFX, country, AI, source-specification, workbook, or CSV patch was made.

This handoff is the only file written by the audit.

The League should remain HOLD/PARTIAL until the congress-failure retry defect is repaired by the parent and the unresolved MCP lifecycle, typed probability, and user-owned runtime evidence boundaries are preserved accurately.
