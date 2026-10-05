# Repo Explorer Handoff

> **Current-status disposition (2026-10-06): superseded by** [takeover_status_2026-10-06.md](../takeover_status_2026-10-06.md) for current famine and migration status.
> This dated document remains historical evidence, with its original acceptance basis, source snapshot, audit outcome, and validation limits scoped to the work described below.
> This reconciliation grants no new design acceptance and upgrades no historical evidence to current or native validation.

Disposition: unresolved audit handoff. This report records current source evidence and does not promote a proposal to accepted design.

## Scope read

- Parent task: re-audit whether current Event 005, 006, 013, 014, 015, 020, 021, 028, 033, Camp, CBRN, and Air Winter owners now provide exact facts for the accepted famine/migration connections, and identify any safe current callback that can supply a missing adapter.
- Explicit constraints: read-only source exploration; Event 001–040 work is active in parallel; do not duplicate or edit those owners; do not modify the Event 012-owned Gods reception addition in `migration_adapter_effects`; do not use deaths, pressure values, dispatch IDs, flags, or total state population as live migrant counts; do not add generic adapter dedupe; do not repeat recovery work for retired/missing Event 118, 120, or 131.
- Files and IDs requested: the August 26 completion report adapter section, current `source_of_truth_map`, binding integration matrix, Part 7, coding prompt, owner scripts and callsites for the listed events and shared systems.
- Skills and docs read: local `AGENTS.md`, `chaos-redux-subagents`, `chaos-redux-events`, the prepared explorer prompt and targeted input-manifest inventory, source-of-truth map, completion report, integration matrix, Part 7, coding prompt, offline Event Modding page, and installed `effects_documentation.md` state-event section.

## Primary findings

The live-person evidence is concentrated in one current Camp callback: `camp_rework_commit_exact_cohort_custody` resolves an explicitly selected, unambiguous, living migration cohort at its current host and calls `migration_record_current_state_cohort_custody_exact`. It records custody evidence only; it does not transfer people or change Deaths, route, reception, or food ledgers.

Event 013, Event 020, Camp mortality, CBRN, and Air Winter already have source-specific famine-pressure calls after exact state-local death or hazard outcomes. Those calls are secondary famine-pressure channels; their death counts are not live people or migration transfers.

Event 005, 006, 014, 015, 021, 028, and 033 have no direct call to the famine/migration adapter APIs in the current source. Their observed population, political, control, hazard, death, and legacy migration fields do not establish an accepted live cohort or finalized transfer transaction.

`common/scripted_effects/migration_adapter_effects.md:15` is stale against the current source: it says no owner supplies all custody facts, while the Camp owner now stages and re-resolves the exact cohort, amount, host, actor, site, and action before calling the strict custody receipt.

No new event-to-migration movement adapter is safe to wire from the listed owner callbacks. The only current exact living cohort callback is already connected to custody recording, and extending its same people into a second movement or pressure output would double count the cohort.

## Relevant files

| Path | Why it matters | Evidence |
| --- | --- | --- |
| `docs/plans/famine_and_migration_system_plans/completion_report.md` | August 26 baseline blocker list and exact adapter boundaries. | Adapter section lines 92–111 records source-specific calls, generic owner gaps, and the warning that death totals are not a separate migration receipt. |
| `docs/plans/famine_and_migration_system_plans/source_of_truth_map.md` | Current source ownership and allowed famine/migration seams. | Sections “Explicit connection seams” and “Event 149 and event boundary” keep movement, deaths, context, and cleanup distinct. |
| `docs/specs/famine_and_migration_system_specs/famine_and_migration_system_integration_matrix.csv` | Accepted owner-to-system facts and ownership boundaries. | Rows for Camps/genocide, Event 5, Event 6, Event 14, Event 15, Event 20, Event 21, Event 28, and Event 33. |
| `docs/specs/famine_and_migration_system_specs/famine_and_migration_system_spec_part_7_cross_system_connections.md` | Binding cross-system acceptance. | Sections “Camps and genocide,” “Natural disasters,” “Event 5,” “Event 6,” “Event 14,” “Event 15,” “Event 20,” “Event 21,” “Event 28,” and “Event 33.” |
| `common/scripted_effects/famine_adapter_effects.txt` | Strict state-local cause receipt and current Famine output channels. | Lines 68–112 validate state/actor/source/cause/amount/generation/revision/request fields; lines 166–316 define Air Winter, Camp, CBRN, Black Plague, and natural-disaster famine-pressure adapters. |
| `common/scripted_effects/migration_adapter_effects.txt` and `.md` | Current Camp custody channel and the stale coverage sentence. | `.txt:80–120,131–220` resolves one explicit full living cohort row and records idempotent custody evidence without movement; `.md:15` still says no owner supplies every required fact. |
| `common/scripted_effects/camp_repression_rework_effects.txt` | Current Camp death and living-cohort callbacks. | Lines 2000–2034 submit exact Camp death context to the Famine pressure adapter; lines 5222–5320 stage and re-resolve a live cohort for migration custody; lines 5360–5370 and 5445–5454 call that boundary for detention/labor actions. |
| `common/scripted_effects/cbrn_occupation_effects.txt` and `common/scripted_effects/cbrn_diplomacy_effects.txt` | Resolved CBRN action and its actual owner record ID. | `cbrn_occupation_effects.txt:311–372` records state/action outcome and calls Famine and migration-persecution consumers; `cbrn_diplomacy_effects.txt:339–354` increments the source-owned chemical-action UID and stores it as `cbrn_last_chemical_record_uid`. |
| `common/scripted_effects/013_natural_disasters_effects.txt` | Event 013 exact resolved disaster deaths and current Famine bridge. | Lines 5339–5364 record the exact Deaths result and call `famine_adapt_natural_disaster_state`; lines 3559–3565 show separate sequence and impact-index fields; lines 4163–4183 allocate a sequence for accepted disaster work. |
| `common/scripted_effects/020_black_plague_effects.txt` | Event 020 exact mortality and source-local pulse. | Lines 1333–1468 guard one mortality application per state and pulse, use exact applied deaths, exclude rat provenance, and call the Famine pressure adapter; lines 1722–1728 increment the pulse sequence. |
| `common/scripted_effects/fallout_consolidated_effects.txt` | Air Winter exact death and famine-pressure callback. | Lines 2369–2372 increment `global.air_winter_cycle_id`; lines 4000–4055 apply exact state loss and call `famine_adapt_air_winter_state` with state/cycle context. |
| `common/scripted_effects/005_soviet_collapse_effects.txt` | Current Event 005/Camp boundary. | Lines 22038–22047 call Camp dismantlement only when the UWR aftermath requires a Camp receipt; this is cleanup acceptance, not a people transfer. |
| `common/scripted_effects/006_independence_wave_effects.txt` and `006_independence_wave_host_response_effects.txt` | Event 006 release and host-response values. | Host `population_dispute` and state-release arrays are political/ownership values; the scoped adapter call census found no famine/migration adapter call. |
| `common/scripted_effects/014_cannibalism_effects.txt` and `015_utopia_manifesto_effects.txt` | Event 014/015 apparent migration or death surfaces. | Event 014 “spread migration” identifiers are country/infection continuity; Event 015’s `utopia_manifesto_migration_pressure` is a country-level live-pressure presentation flag, not a cohort or movement receipt. |
| `common/on_actions/021_random_civil_war_cxt_on_actions.txt` | Event 021 state-control context. | Lines 33–40 capture the changed state for mission-continuity handling; no people or movement output is supplied. |
| `common/scripted_effects/028_asteroid_incoming_runtime_effects.txt` | Event 028 impact and rescue outcomes. | Lines 1139–1160 compute/apply exact deaths and update rescue burden; neither is a live survivor cohort. |
| `common/scripted_effects/033_acid_rain_effects.txt` | Event 033 state damage and receipt arrays. | Lines 2532–2601 record exact deaths and generation/state receipts; the `acid_rain_migration_*` legacy counters are cleanup/recovery bookkeeping, not migration-system output. |
| `common/scripted_effects/civilian_transfer_effects.txt` and `migration_core_effects.txt` | Canonical final movement output required for an actual transfer adapter. | The transfer transaction returns exact origin debit, route deaths, survivor credit/destination result and finalized cohort projection; no listed event owner calls `civilian_transfer_execute_transaction`. |

## Existing patterns

The source census found current calls to `famine_adapt_natural_disaster_state`, `famine_adapt_black_plague_state`, `famine_adapt_camp_state`, `famine_adapt_chemical_state`, and `famine_adapt_air_winter_state`. Each calls Famine after a resolved owner outcome and writes only the Famine pressure channel; none calls a migration movement endpoint.

Event 020 has the strongest current source-local mortality identity among the event owners: `global.black_plague_pulse_sequence` increments on the system pulse, and `black_plague_apply_current_state_mortality_once` rejects a second mortality application for the same state and pulse. Its actual loss remains dead people, and the downstream channel remains famine pressure.

Event 013 has a monotonic accepted sequence, `natural_disaster_sequence_id`, and a distinct per-impact `natural_disaster_impact_index`. The current Famine receipt uses the sequence as generation, the applied death amount as revision, and `global.date` as request ID; it does not pass the impact index. The existing adapter therefore establishes natural-disaster famine pressure but does not establish a replay-unique per-impact migration transaction.

CBRN has an actual monotonic owner UID, `global.cbrn_chemical_action_uid_next`, copied to `cbrn_last_chemical_record_uid` and then to `cbrn_occupation_last_record_uid`. The current Famine callback instead sets generation from the action date and request ID from `global.date`; the UID is currently used for owner history/projection, not as a people amount. The accepted CBRN outputs remain Famine pressure and migration-persecution context, not evacuation.

Camp’s `camp_rework_commit_exact_cohort_custody` re-resolves the explicit cohort and checks the current host and full live-row amount after the concrete site/labor assignment. It passes the actor, state/site, action, amount, and cohort identity to the strict Migration custody recorder. The request and transaction proofs are `global.date`, and the generation is `global.civilian_transfer_generation`; no Camp-local monotonic custody-action ID was found. This is already a custody adapter and is not a transfer receipt.

Air Winter increments `global.air_winter_cycle_id` once per prepared monthly cycle and submits an exact state-loss receipt to Famine. Its stored population-loss memory is cumulative death history, not a live movement request.

State-control cleanup and safe occupation-profile reads are separate metadata paths. They may reassess owner/controller, current law, registry membership, or modifiers without a people receipt because those calls do not claim a transfer, death, or new migrant cohort.

The Event 012-owned `migration_install_gods_of_africa_reception_service` and cleanup helpers are new dirty-tree additions at `migration_adapter_effects.txt:372+`, documented as capacity-only and pending Event 012 callsites in `migration_adapter_effects.md:21+`. They use a safe capital projection to set reception capacity; they do not move civilians and were not changed or treated as evidence for the other events.

## Vanilla or reference precedents

The offline wiki’s `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md:25–33` explains event ROOT/THIS and the FROM/event-target scoping carried from effect-fired events. Installed vanilla documentation at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md:8096–8106` lists `state_event` as supporting STATE and COUNTRY scopes.

No vanilla content-file precedent was needed for this re-audit because no new event syntax or population transaction is proposed. The source-owned Chaos Redux Camp custody and `civilian_transfer` patterns are the relevant current implementation precedents.

## Likely edit order for the parent

1. Treat `camp_rework_commit_exact_cohort_custody` as the only in-scope live-person callback, and only for its already accepted record-only custody purpose.
2. Reconcile `migration_adapter_effects.md:15` and its handoff disposition with the current Camp callsite; do not add a second pressure or movement output from the same custody row.
3. Keep the Event 013, Event 020, Camp, CBRN, and Air Winter callbacks on the Famine pressure channel they currently own; never reuse their death amount as live migrant population.
4. For a later event-owned movement connection, wait for that event owner to expose a resolved, living source/destination or cohort receipt with the responsible actor, cause, route, and a transaction identity, then pass its finalized output through the existing exact `civilian_transfer` path.
5. Leave the Event 012 Gods reception helper and its callsites to the Event 012 owner.

## Validation checks

The targeted source census was run over `common` with `rg -n --glob '*.txt' 'famine_adapt_|migration_adapt_|famine_request_.*pressure|migration_request_.*pressure|civilian_transfer_execute_transaction' common` and then checked against the exact owner files listed above.

Before any owner write, rerun `hoi4.event_inspect` and `hoi4.event_render` for each current root: `chaosx.nr5.1`, `chaosx.nr6.1`, `chaosx.nr13.1`, `chaosx.nr14.1`, `chaosx.nr15.1`, `chaosx.nr20.1`, `chaosx.nr21.1`, `chaosx.nr28.1`, and `chaosx.nr33.1`. Preserve each source revision, diagnostics, and returned artifact URI.

If a source call is added, review the exact owner callback’s output fields and scope, verify the living/dead/cohort distinction and source-local identity at that callback, and compare the final adapter output to the accepted contract. A pressure unit, dispatch index, country flag, existing Deaths amount, or whole-state population must not be reported as a live migration transaction.

## Risks and blockers

Confirmed stale documentation: `migration_adapter_effects.md:15` says no owner supplies every strict custody field, contradicted by the current Camp source at `camp_repression_rework_effects.txt:5222–5320`.

Confirmed request-identity limitation: the Camp custody proof uses date-based transaction/request fields and a shared transfer generation. Do not add a generic adapter dedupe; the owner remains responsible for its operation identity.

Confirmed live-event tooling blocker: corrected one-root Event 005 trace and a one-node retry both ended with `tool call failed for hoi4_agent_tools/hoi4.event_inspect: timed out awaiting tools/call after 600s`. The earlier invalid selector and `maxDepth = 0` requests were schema errors, not service evidence.

Confirmed source tooling blocker: `hoi4.source_lookup` for `famine_adapt_natural_disaster_state` timed out after 600 seconds with references enabled, and the narrower one-definition, 20-line, no-reference retry also timed out after 600 seconds. No source artifact or revision was returned.

Confirmed reference-context blocker: `hoi4.reference_context(surface = event, limit = 3)` timed out after 600 seconds. The local offline wiki and installed documentation sections above were read as the fallback reference; they are not live MCP evidence.

Pending at handoff time: the one-root Event 005 overview render and exact `hoi4.reference_search` retry had not returned. They produced no artifacts or URIs before the report was written; they are pending calls, not recorded as completed timeouts.

Event MCP evidence is required for all nine listed event roots, but no fresh event artifact URI, source revision, or render result was returned in this audit. The local source map is not equivalent to that missing engine-tool evidence.

The shared worktree is dirty, including active Event 005/006 effect changes and Event 014/028/033 source changes. The parent’s parallel event owners retain those files. No gameplay, event, adapter, or documentation-source files were edited by this audit.

The connected tools expose `hoi4_tech_inspect`, `hoi4_tech_render`, and `hoi4_tech_compare`, but no standalone Technology Tree Viewer tool was found, and `Get-StartApps` found no matching app. This is a package gap separate from the exposed read-only technology routes; no technology surface was part of this event audit.

## Recommended next action

Use the current Camp custody callback only as the accepted record-only live-cohort connection and reconcile the stale adapter documentation. For any requested Event 005/006/013/014/015/020/021/028/033 migration movement, record an explicit owner-data blocker until the event supplies an actual living cohort/route transaction; the present event deaths, pressure, release, control, and region receipts cannot safely stand in for one.
