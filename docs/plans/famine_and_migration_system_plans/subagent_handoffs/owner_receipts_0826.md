# Repo Explorer Handoff

## Scope read

- Parent task: Current-state recovery audit of the separate Chaos Redux famine and migration systems, with exact owner facts for occupation-law transitions, strategic bombing, war/peace callbacks, cluster/scenario dispatch, relief obstruction, and absent Event roots 118, 120, and 131.
- Audit date: 2026-08-26.
- Explicit constraints: Read-only gameplay/source exploration; the only write permitted by this audit was this handoff; runtime namespaces remain separate as `famine_*` and `migration_*`; no `famine_migration_*` or `fm_*` runtime names, invented population amounts, actors, cohorts, routes, or event roots.
- Files or ids requested: All eight files named `famine_and_migration_system_spec_part_1_core.md` through `famine_and_migration_system_spec_part_8_balance_acceptance.md`, all supporting files under `docs/specs/famine_and_migration_system_specs/`, `docs/plans/famine_and_migration_system_plans/completion_report.md`, and `docs/plans/famine_and_migration_system_plans/subagent_handoffs/current_owner_blocker_reaudit.md`.
- Skills and guidance read: `AGENTS.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, and `.agents/skills/chaos-redux-events/SKILL.md`.
- Supporting specification material read: the specification README, goal, coding prompt, implementation surface map, execution status, routing notes, improvement-loop closure, bibliography, matrix CSVs, and subagent prompts under the specification directory.
- Required offline references read: the core offline Paradox wiki snapshots for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding, plus Map modding and State modding for the map substrate.
- Required vanilla references read: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md`, `effects_documentation.md`, `common/on_actions/_documentation.md`, the vanilla occupation-law definitions, and the owner-specific law precedent in `events/GOE_Raj.txt` and `common/on_actions/13_goe_on_actions.txt`.

## Primary findings

- The current architecture is split correctly between `famine_*` food/mortality owners, `migration_*` cohort/flight owners, and neutral `civilian_transfer_*` and humanitarian lifecycle dispatch.
- The six generic/source-recovery blockers from `current_owner_blocker_reaudit.md` remain open in the live worktree.
- Exact narrow owner paths remain usable when they supply a complete proof envelope: accepted CBRN operations, Air Winter exact loss, Event 013 natural-disaster loss, current-host camp custody, exact famine mortality condemnation, deportation, and forced-return or violent-pushback transfers.
- Generic occupation-law, bombing, war/peace, cluster/scenario, and relief callbacks do not currently emit enough facts to certify a famine or migration receipt.
- Exact roots `chaosx.nr118.1`, `chaosx.nr120.1`, and `chaosx.nr131.1` remain absent; similarly numbered descendants are not replacements.
- No gameplay, localisation, GUI, map, event, asset, or documentation source was changed by this audit.

## Relevant files

| Path | Why it matters | Evidence |
| --- | --- | --- |
| `common/scripted_effects/famine_core_effects.txt` | Famine request wrappers, current occupation-law profile reader, mortality owner, and exact famine condemnation owner. | `famine_request_occupation_pressure`, `famine_request_bombing_pressure`, `famine_request_war_pressure`, `famine_request_peace_pressure`, `famine_request_cluster_pressure`, and `famine_request_scenario_pressure` are definition-only wrappers at lines 512, 520, 530, 532, 542, and 544. `famine_resolve_occupation_profile` reads only the current `occupation_law` at lines 841-1002. `famine_apply_mortality` computes a positive request and calls `apply_exact_state_civilian_population_loss` at lines 2423-2538. `famine_record_exact_mortality_condemnation` binds state and owner targets and submits proof at lines 2650-2705. |
| `common/scripted_effects/famine_adapter_effects.txt` | Defines the fail-closed famine receipt contract and relief-obstruction wrapper. | `famine_validate_state_local_food_receipt_exact` requires valid state, positive food/environment/transport/policy/actor/cause/source tokens, positive amount, generation, revision, request identity, and a live actor target at lines 21-42. `famine_adapt_air_winter_state`, `famine_adapt_camp_state`, `famine_adapt_chemical_state`, `famine_adapt_black_plague_state`, and `famine_adapt_natural_disaster_state` are owner-specific at lines 96-247. `famine_condemn_relief_obstruction` only emits a condemnation after the exact validator succeeds at lines 249-303. |
| `common/scripted_effects/migration_core_effects.txt` | Migration pressure wrappers, state-local bombing projection, and war/peace reassessment markers. | `migration_apply_flight_request` accepts a pre-proven amount and updates flight/incident state at lines 685-733. The occupation, bombing, war, peace, cluster, and scenario wrappers are definition-only at lines 740, 750, 760, 762, 772, and 774. `migration_refresh_native_state_safety_projections` treats rail damage and bombing recency as state-local availability signals with no attacker at lines 1595-1629. `migration_process_registered_country` only consumes pending reassessment and recalculates capacity at lines 1670-1715. `migration_mark_country_war_reassessment` and `migration_mark_country_peace_reassessment` only write pending dates, dirty capacity, and register the country at lines 2119-2135. |
| `common/on_actions/humanitarian_runtime_on_actions.txt` | Current lifecycle callback wiring. | `on_state_control_changed` performs corridor/state-control cleanup at lines 46-57. `on_war_relation_added` only marks country reassessment and corridor revalidation for the two relation scopes at lines 72-83. `on_peace` only marks the ambient country for reassessment and corridor revalidation at lines 85-92. `on_peaceconference_ended` repeats the same country-scoped operation for `ROOT` and `FROM` at lines 94-105. `on_naval_invasion` is a separate exact state-attack candidate at lines 107-114. |
| `common/scripted_effects/humanitarian_runtime_effects.txt` | Neutral dispatchers that prove ownership boundaries. | `humanitarian_process_registered_runtime` iterates sparse famine states, migration states, reception states, countries, and relief donor states at lines 35-71. The war/peace wrappers merely call the separate owners at lines 79-87. No generic source receipt is created here. |
| `common/occupation_laws/chaosx_occupation_laws.txt` | Current Chaos Redux occupation-law definitions. | The file has 170 lines and defines the hidden `concentration` compatibility token plus CBRN laws; it contains no transition callback. |
| `common/scripted_effects/cbrn_occupation_effects.txt` | The only current occupation-law writers and a narrow exact CBRN owner candidate. | `set_occupation_law` appears only at lines 77, 90, and 97 for CBRN coercive security, CBRN protected administration, and clearing the state policy. The accepted-operation owner at lines 459-543 records actor, state-owned operation fields, cause/route ledgers, generation/revision/request values, and calls `famine_adapt_chemical_state` at line 538. This is not a generic law-transition hook. |
| `common/scripted_effects/fallout_consolidated_effects.txt` | Strategic-bombing proxy and Air Winter exact owner. | State pressure uses only `days_since_last_strategic_bombing` and bounded pressure values at lines 2993-3014. The exact Air Winter loss path calls `apply_exact_state_civilian_population_loss` at line 4030 and supplies the famine adapter fields at lines 4034-4049. The source explicitly says the adapter does not infer identity or other ledgers from deaths. |
| `common/scripted_effects/chaosx_event_cluster_effects.txt` | Cluster member selection, scheduling, and downstream dispatch. | Member IDs and role/chance/tier/danger metadata are loaded at lines 407-555. The pending queue and delayed `chaosx.event_clusters.2` event are managed at lines 1161-1303. The Event 013 special dispatch recovers a state and target country, then calls `call_natural_disaster` at lines 1180-1226. No `famine_*` or `migration_*` token occurs in this file. |
| `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt` | Scenario selection and disaster-barrage dispatch. | Scenario selection routes IDs and intensity at lines 886-1042. The disaster barrage supplies target country, caller type, severity, sequence, and intensity to `call_natural_disaster` at lines 1045-1125. No famine or migration receipt is emitted by this generic dispatcher. |
| `events/chaosx_event_clusters.txt` | Hidden cluster queue event root. | `chaosx.event_clusters.2` is a hidden triggered-only event whose immediate effect is `event_cluster_fire_next_pending_member` at lines 1-16. |
| `events/chaosx_triggerable_scenarios.txt` | Scenario acknowledgement event roots. | Current roots are `chaosx.triggerable_scenarios.1` through `.7`, with `.5` retained as a hidden legacy acknowledgement, at lines 1-75. These are not famine or migration event roots. |
| `events/013_natural_disasters.txt` | Existing exact Event 013 downstream owner and source of similarly numbered descendants. | The canonical root is `chaosx.nr13.1` at lines 1-66. `chaosx.nr13.118` and `chaosx.nr13.120` are report descendants at lines 692-760, not `chaosx.nr118.1` or `chaosx.nr120.1`. |
| `common/scripted_effects/013_natural_disasters_effects.txt` | Event 013 exact state-loss downstream owner. | `natural_disaster_apply_population_loss` computes state-local loss, records `natural_disaster_last_deaths`, and carries state/family/severity/sequence/death-driver/cause/generation/revision fields into `famine_adapt_natural_disaster_state` at lines 5244-5364. It does not create migration movement. |
| `common/scripted_effects/migration_adapter_effects.txt` | Exact migration proof envelopes and custody/condemnation owners. | Forced-displacement death validation requires state, positive amount, cohort, route, actor target, generation, revision, request identity, and forced-displacement cause at lines 18-53. Current-host custody requires an aligned live row, whole-row amount, host, action, transaction, actor, route, site, generation, revision, request identity, and actor target at lines 65-109. Exact condemnation is downstream of a finalized transfer at lines 233-355. |
| `common/scripted_effects/civilian_transfer_effects.txt` | Shared exact movement primitive. | `civilian_transfer_civilians_exact` begins at line 372 and performs one validated origin debit, route-death ledger slice, survivor-only destination credit, and rollback/recovery handling. It requires an explicit origin, destination, route, cohort, actor, and transaction envelope. |
| `common/scripted_effects/migration_forced_movement_effects.txt` | Narrow exact deportation owner. | The exact transfer path records positive transfer, origin/destination state, cohort, route, actor, cause, transaction, generation, revision, and request identity and calls `migration_condemn_deportation` at lines 210-270, including line 250. |
| `common/decisions/migration_decisions.txt` | Narrow exact forced-return and violent-pushback owners. | Enforced-closure/violent-pushback transfer validation and condemnation are around lines 1871-1928. Forced-repatriation transfer validation and condemnation are around lines 2485-2577. Both require a finalized transfer, positive debit, and positive survivor credit before recording condemnation. |

## Existing patterns

The current safe pattern is owner-supplied, fail-closed adaptation.

For famine, the caller must own the actual state-local food consequence and submit the full state, food, environment, transport, policy, actor, cause, amount, generation, revision, and request identity bundle before a `famine_request_*` adapter is accepted.

For migration, the caller must own a live aligned cohort or an independently owned physical death transaction and submit the exact cohort/host or route, positive amount, actor, cause, transaction, generation, revision, and request identity fields before mutation or condemnation is accepted.

The exact movement primitive is deliberately separate from both mechanics: movement transfers the origin debit minus route deaths as survivors, while deaths remain a separate Deaths transaction.

The narrow CBRN, Air Winter, Event 013, camp custody, deportation, forced-return, and violent-pushback paths follow this pattern and are safe candidates only for their existing owner scope.

No generic wrapper should be called merely because a state has an occupation law, a recent bombing date, a war/peace relation, a queued cluster member, a scenario intensity, or a failed relief choice.

Historical specification wording that uses retired shared names is superseded by the current split runtime design; live runtime names remain `famine_*` and `migration_*`.

## Vanilla or reference precedents

| Reference | What it proves |
| --- | --- |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md:2515-2522` | `days_since_last_strategic_bombing` is a state-scoped recency trigger and does not expose attacker, operation identity, or casualty amount. |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md:6918-6933` | `occupation_law` reads the current state/country law; it does not provide old-law/new-law transition facts. |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md:7434-7464` | `set_occupation_law` and `set_occupation_law_where_available` are direct effects with no documented generic law-changed callback. |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/occupation_laws/occupation_laws.txt` | Vanilla occupation-law definitions do not establish a generic transition event stream. |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/common/on_actions/_documentation.md:24-40` | On-action registration is explicit; the documented callback list does not add a generic occupation-law transition or strategic-bombing attribution callback. |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/events/GOE_Raj.txt:1605-1610` and `common/on_actions/13_goe_on_actions.txt:99` | A direct owner-specific law route exists as a precedent, but it is not evidence for a generic law-transition owner. |
| Offline `paradox_wiki/` Effects, Triggers, Scopes, On actions, Event modding, and Map modding pages | The corresponding syntax and scope rules support the same boundary: relation callbacks, state facts, and direct effects must not be upgraded into unavailable actor/amount/operation receipts. |

## Proof envelopes and blocker re-audit

### Generic occupation-law transitions

Confirmed source facts are limited to current-law classification and the three CBRN direct writers.

`famine_resolve_occupation_profile` maps the current law token to a famine profile at `common/scripted_effects/famine_core_effects.txt:841-1002`, but it has no old-law token, new-law token, affected-people amount, responsible actor, generation, revision, or request/operation identity.

The only `set_occupation_law` callsites found by the live source census are `common/scripted_effects/cbrn_occupation_effects.txt:77`, `:90`, and `:97`; no generic callback or arbitrary transition writer was found.

The safe candidate is the already accepted CBRN operation owner at `common/scripted_effects/cbrn_occupation_effects.txt:459-543`, but that is safe only for the accepted CBRN operation and its own state/actor/cause ledgers, not for every occupation-law transition.

To close the generic blocker, a future owner must expose the exact state, old and new law, responsible actor target, positive famine amount or positive migration cohort transaction amount, cause, generation, revision, and request/operation identity before calling separate `famine_*` and/or `migration_*` adapters.

### Strategic bombing

`common/scripted_effects/fallout_consolidated_effects.txt:2993-3014` and `common/scripted_effects/migration_core_effects.txt:1595-1629` use state-local bombing recency and rail damage as bounded pressure/availability signals.

The current Air Winter owner at `fallout_consolidated_effects.txt:4030-4049` does apply a positive exact state loss and can submit a complete famine receipt for that Air Winter cycle, but it does not expose a generic bomber, bombing operation, or attacker attribution.

The safe candidate is therefore Air Winter only when its owner supplies its own positive loss and full receipt; reusing its death amount as generic strategic-bombing or migration proof is not allowed.

The missing generic envelope is affected state, responsible attacker target, positive operation amount, cause, operation identity, generation, revision, and request identity, with separate famine and migration receipts if both consequences are intended.

### Country war/peace callbacks

`humanitarian_runtime_on_actions.txt:72-105` and `humanitarian_runtime_effects.txt:79-87` only mark country reassessment, dirty reception capacity, and corridor revalidation.

`migration_core_effects.txt:2119-2135` confirms that the owner writes only pending war/peace dates, capacity dirtiness, and active-country registration.

No callback exposes an affected state, live cohort, positive people amount, route, destination, or incident owner.

The exact `on_naval_invasion` state-attack candidate at `humanitarian_runtime_on_actions.txt:107-114` is not a war/peace callback and must not be relabelled as one.

The blocker remains open until a concrete war/peace owner identifies the affected state or cohort and submits a positive amount, route or state cause, actor/operation identity, generation, revision, and request identity.

### Cluster/scenario dispatch

Cluster metadata and queue identity are not famine/migration proof.

`chaosx_event_cluster_effects.txt:407-555` loads event/member role, chance, minimum tier, and danger metadata.

`chaosx_event_cluster_effects.txt:1161-1303` schedules and fires queued members, while the Event 013 branch at `:1180-1226` recovers an explicit state and target country before calling the natural-disaster owner.

`chaosx_triggerable_scenarios_effects.txt:886-1042` selects a scenario and intensity, while `:1045-1125` sends scenario caller type, target country, severity, sequence, and intensity to `call_natural_disaster`.

Neither generic dispatcher contains `famine_*` or `migration_*` calls in the live source census.

The safe downstream candidate is Event 013 at `common/scripted_effects/013_natural_disasters_effects.txt:5244-5364`, which owns the resolved state loss and passes its own family/severity/sequence/death-driver fields to `famine_adapt_natural_disaster_state` at line 5363.

The dispatchers themselves still lack the affected state/cohort, positive people amount, actor, cause, generation, revision, and request/operation identity needed for a generic receipt.

### Relief obstruction

`famine_condemn_relief_obstruction` at `common/scripted_effects/famine_adapter_effects.txt:291-303` is a validator-gated condemnation wrapper, not an obstruction detector.

Its validator at `:249-274` requires a state target, actor target, positive state-local food/environment/transport/policy/cause fields, positive people amount, generation, revision, and request identity.

The live callsite census found the definition but no current gameplay caller in `common`, `events`, `decisions`, or `on_actions`.

No safe caller candidate exists at present; a missing, rejected, or unsuccessful relief decision does not prove that an actor intentionally obstructed a concrete relief operation.

The future owner must prove the blocked relief action itself, including state, responsible actor, positive affected people amount, food/environment/transport/policy cause, generation, revision, and request identity, before this wrapper can be called.

### Absent Event roots 118, 120, and 131

The exact source census for `chaosx.nr118.1`, `chaosx.nr120.1`, and `chaosx.nr131.1` returned no hits under `events`, `common`, `decisions`, or `on_actions`.

The existing root `chaosx.nr13.1` is at `events/013_natural_disasters.txt:11-64`; `chaosx.nr13.118` and `chaosx.nr13.120` at `:692-760` are unrelated Event 013 descendants.

The prior blocker handoff also records similarly numbered `chaosx.nr3.120`, `chaosx.nr3.131`, and `chaosx.nr5.131` as unrelated descendants, so they cannot be used as substitutes.

The specifications describe Event 118 Locust Plague, Event 120 Volcano, and Event 131 Mutiny as backlog integration points at `famine_and_migration_system_spec_part_7_cross_system_connections.md:381-395`, but no source roots or owners were recovered.

No event, actor, state, amount, cohort, or route may be fabricated to fill these roots.

## Mandatory MCP evidence and limits

### Fresh Event 013 route

The read-only `hoi4.event_inspect` call used selector `{ kind: event, eventId: chaosx.nr13.1 }`, `mode = state_flow`, downstream direction, helper expansion disabled, depth 2, 40 nodes, 80 edges, refresh enabled, and workspace `mod_chaos_redux`.

It returned `status = ok`, `code = EVENT_INSPECTED_PARTIAL`, revision `43388d6b2737a1c8e2409f324449210941414fee69c903a1c69d441ca9d33b97`, graph hash `dd30c3585ea090f05881b49253cfb4212d58091d19729649a292f8ed561ed67c`, zero blocking diagnostics, and the informational `MCP_INLINE_FILES_TRUNCATED` diagnostic because 352 source paths were scanned while 64 were returned inline.

Trace artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bdd02c1a8c6ac7bd22f7101fdfeff275c0da79689d1490e62aa81a79862d7596/93d6bb09511cf092adf4c54f558fc7096c9b56d4465bd4b5dfeaf984546af275/event-state_flow-43388d6b2737.json`.

The matching read-only `hoi4.event_render` overview returned `status = ok`, `code = EVENT_RENDERED_PARTIAL`, the same revision and graph hash, zero blocking diagnostics, and the same inline-source truncation limit.

Render artifacts: manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7de316a89b250471c21fe64e0637ed47a7043556d06e2c14290cac56b84d2b53/95468926af3d36b46e0e78ca0caaca87b9f476cd527145b720d8d3a1d0d5f441/event-overview-43388d6b2737-manifest.json`, JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d0ddc3c62fc64fa70c212f895c37020c80f681b31d5673bd9ed7e1baaab/ef6a778afe72844fe1a73b01932af46f041c69e3e2ea9920790b5b15a69b2fd3/event-overview-43388d6b2737.json`, SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e4555b1676d48e478f03c6e86873b559e7ecaec77924d7dd7a4d1f4deac526ea/9c6fa06d059761ff2ac63eb738c11a8e8ba95eaeb55259bcd6677e836a2e6e2b/event-overview-43388d6b2737.svg`, and PNG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d50aefc3d1dd08300da1dce1f3f67320f3a29e1ee0003b3426b3b8d848146e85/8448150b51fd839300d40f863aab7d1ee98248c78d76f19c6c9be934b79d3374/event-overview-43388d6b2737.png`.

The fresh batched cluster/scenario inspect/render attempt was interrupted by the parent’s immediate-finalization request before the MCP service returned results, so no fresh artifact is claimed for those four calls.

Inherited current-worktree cluster artifacts remain available from `current_owner_blocker_reaudit.md`: trace `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b8da1b3e6f9c108563d435f79afed553b0540aab1ce184f05ec50e748e9207e7/ff112ccb8f1e4b8bc010a18f72aa408958e4a033d4d4bd34ee6e4a58ff7d29b9/event-trace-f588a2607444.json` and render manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fb38962fa53ca6e7f94c3df85058521429c65871c5ceadd1d0e160398585184a/c41412a8682f6e89fc07b3f5f906e35842054a0a3adb4e5b4de019db8aaed471/event-state-f588a2607444-manifest.json`.

Inherited scenario artifacts remain available from the same handoff: trace `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/14b6ed883ddf1f48a63cb8c5b6811b1f8eca8681bca0dca063dcfb36becaf1fd/d0d485aff9c1b701899c212a07d9d23c7ad251bc60f02428f41d50a62b970461/event-trace-f588a2607444.json` and render manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9de0afcbf6f104ed37a1e2285c8f7d00332133de4ed8d8cd52d7b04a0ebfd376/d1fd2970988ed0674c2baa0077aac8b0a8163da836125cf68a0c461081da22f2/event-state-f588a2607444-manifest.json`.

Those inherited cluster/scenario reports were `EVENT_INSPECTED_PARTIAL`/`EVENT_RENDERED_PARTIAL` with deferred helper/lifecycle projections and are structural evidence only, not complete receipt or runtime proof.

### Map route

The retained bounded `hoi4.map_inspect` route covered representative states 1, 64, 282, 290, and 452 and returned `MAP_INSPECTED` with state/geometry/membership/adjacency/supply/railway substrate checks.

Map-inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a75193c5b26cd1180f60405e66b535e35ff3e96ad25d03aeeded209441129c2f/60deb73e299b4ab6ff6bc342e905d5758b8a18037e0444c2bdc859a58a4dfec6/map-inspect.24d421bcc68e84bf.json`.

Map overview artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/06862ee46ae6ff2778002719a3bbd5bcd567fefa7fd3c1da0f612bd363b84d11/b04a6c5d1ff423af5c952585d61d898aebacec114217214d4839c21d5974539b/map-overview.24d421bcc68e84bf.png`.

The retained map render returned `MAP_RENDERED` for the state substrate, with `map-state.png`, `map-state.json`, and `map-state.html` artifacts recorded in `two_mapmode_owner_patch.md`; the route cannot execute scripted mapmode colors or tooltips.

The map service also reports unrelated `MAP_BUILDING_POSITION_INVALID` and `MAP_PORT_ADJACENT_SEA_INVALID` diagnostics, so map evidence is substrate-only and not a famine/migration dynamic-mapmode proof.

### Probability route limits

The cluster direct-random probability inspection in the prior handoff returned `INTERNAL_ERROR` with no files scanned.

The callable tool registry does not expose `chaosx_ai_probability_auditor`, so no auditor-owned evaluation, sweep, simulation, sequence, comparison, or rendered probability claim is made.

No weighted conclusion is used to close any owner blocker.

## Likely edit order for the parent

1. Keep all six generic blockers closed until a real owner supplies the complete proof envelope; do not add a generic wrapper call to a dispatcher, relation callback, recency reader, or decision failure path.
2. If a source owner is recovered for occupation law or bombing, first add or expose its exact state/actor/amount/cause/generation/revision/request or operation identity in that owner’s scope, then route famine and migration consequences separately through their validators.
3. If a war/peace owner is recovered, bind the affected state or cohort before any reassessment marker is consumed, and prove positive amount and route/destination where movement is involved.
4. For cluster/scenario work, preserve dispatcher metadata as pacing/identity only and wire the downstream owner that actually resolves a state and positive amount.
5. For relief obstruction, add no call until a concrete blocked relief action is owned and all validator fields are available.
6. For Events 118/120/131, recover or classify the canonical source before creating any event, actor, amount, cohort, or route; similarly numbered descendants remain invalid substitutes.
7. After any owner-source change, rerun narrow `hoi4.event_inspect` and `hoi4.event_render` for the affected event root, and rerun the bounded map route only if state/route/mapmode surfaces change.

## Validation checks

- Re-run `rg -n "famine_request_(occupation|bombing|war|peace|cluster|scenario)_pressure|migration_request_(occupation|bombing|war|peace|cluster|scenario)_pressure" common events decisions on_actions` and require each new callsite to be inside a concrete owner with a complete receipt.
- Re-run `rg -n "famine_condemn_relief_obstruction" common events decisions on_actions` and inspect any new caller for the full state/actor/amount/cause/generation/revision/request envelope.
- Re-run `rg -n "chaosx\.nr118\.1|chaosx\.nr120\.1|chaosx\.nr131\.1" events common decisions on_actions` and inspect the exact root if any source is recovered.
- Re-run `rg -n "\bset_occupation_law\b|\bset_occupation_law_where_available\b" common events` and classify every writer as owner-specific or generic before accepting occupation receipts.
- For bombing, verify a new owner exposes attacker target, affected state, positive operation amount, cause, generation, revision, and request/operation identity rather than only `days_since_last_strategic_bombing` or `migration_bombing_active`.
- For war/peace, verify affected state/cohort, positive amount, route/destination, actor, cause, generation, revision, and request identity before accepting more than reassessment/capacity work.
- Preserve the namespace census: live runtime names must remain in `famine_*` and `migration_*`; historical superseded names must not be reintroduced into runtime files.
- Repeat mandatory `hoi4.event_inspect`/`hoi4.event_render` for changed event surfaces and `hoi4.map_inspect`/`hoi4.map_render` for changed map surfaces; record `PARTIAL`, timeout, truncation, and unrelated diagnostics as limits rather than passes.
- For any weighted surface, start with `hoi4.probability_inspect` and route detailed evaluation through `chaosx_ai_probability_auditor` when that callable route is available; otherwise record the exact unavailable route and leave the result unresolved.

## Risks and blockers

### Confirmed blockers

- Generic occupation-law transition ownership is absent; current-law profile reads are not transition receipts.
- Generic strategic-bombing ownership is absent; state recency and Air Winter loss do not expose a generic attacker/operation receipt.
- War/peace callbacks are country-scoped reassessment/capacity hooks and do not identify an affected state, cohort, amount, route, or transaction.
- Generic cluster/scenario queues carry event/member/scenario/intensity metadata but no complete famine or migration proof envelope.
- `famine_condemn_relief_obstruction` has no current gameplay caller and must remain fail-closed.
- Canonical roots `chaosx.nr118.1`, `chaosx.nr120.1`, and `chaosx.nr131.1` are absent; no substitute event was accepted.
- Fresh cluster/scenario MCP requests were interrupted before returning; inherited reports are partial and not fresh final-pass evidence.
- The map route cannot execute scripted mapmode colors/tooltips and reports unrelated map diagnostics.
- The installed tool registry lacks the callable `chaosx_ai_probability_auditor`, and the inherited cluster direct-random inspect returned `INTERNAL_ERROR` with no files scanned.

### Ordinary risks

- Event MCP results are workspace-wide partial projections with helper/lifecycle deferral and inline source truncation, even when blocking diagnostics are zero.
- A future source recovery can accidentally turn a queue identity or prior death amount into a proxy actor, amount, cohort, or route; the validators must reject that shortcut.
- Similar numeric Event 013 descendants can be mistaken for the requested roots during future recovery searches.
- Any future cross-system caller must preserve the separate famine and migration namespaces and avoid reintroducing combined category, mapmode, registry, stage, or value identifiers.

## Recommended next action

Keep the six blockers open and request the missing owner source or an explicit source-of-truth decision before implementation. The only immediately usable paths are the existing owner-specific CBRN, Air Winter, Event 013, custody, exact mortality, deportation, and exact-transfer routes described above; none is evidence for a generic occupation, bombing, war/peace, cluster/scenario, relief-obstruction, or absent-event integration.

This handoff is an exploration receipt only. No gameplay implementation or completion claim is made.
