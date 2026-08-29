# Repo Explorer Handoff

## Scope read

- Parent task: map the remaining source-owner seams for the separate famine and migration mechanics without creating an event ID.
- Explicit constraints: read-only gameplay review; preserve the split famine/migration design; distinguish engine-unavailable facts from existing but unwired facts; do not infer actors, state amounts, or proof receipts.
- Requested surfaces: generic occupation-law changes, strategic bombing, country war/peace, cluster/scenario queues, absence checks for Events 118/120/131, camp current-host custody, and condemnation for deliberate starvation, verified relief obstruction, concealment, forced return, and violent pushback.
- Skills and references read: `chaos-redux-events`, `chaos-redux-mtth`, `chaos-redux-subagents`, the required offline wiki pages in `paradox_wiki/`, and the required vanilla documentation including `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`, `common/script_constants/documentation.md`, and `common/on_actions/_documentation.md`.

## Primary findings

- The two mechanics already have source-owned, fail-closed adapters. Generic occupation-law transitions, ordinary bombing, and generic war/peace callbacks do not supply the exact state-local receipt required by either mechanic.
- Current occupation-law reads are authoritative; a generic law-change callback carrying old law, new law, responsible country, generation, and replay identity is not present. CBRN has narrow direct setters and an accepted-operation receipt, but that is not a generic law transition owner.
- Strategic bombing exposes state-local recency and infrastructure damage only. It does not expose the bomber, strike amount, civilian-loss transaction, or an operation identity to these adapters.
- Country war/peace callbacks only mark reassessment and corridor revalidation. They do not identify affected states, cohorts, people, or a causal operation.
- Cluster and scenario code owns scheduling, participation, intensity, pacing, and dispatch. It is not an incident receipt owner. Event 013's accepted natural-disaster API is the narrow exception because its downstream owner supplies the target state and aftermath facts.
- The exact current-host camp custody receipt is already wired and validates the live ledger row, host state, actor, action, amount, generation, revision, and request identity.
- Deliberate starvation and concealment are emitted from the exact famine mortality owner. Deportation is emitted from the exact forced-movement owner. Forced return and violent pushback are emitted from exact finalized decision transfers. Relief obstruction has a fail-closed API but no current exact caller.

## Relevant files

| Path | Why it matters | Evidence |
| --- | --- | --- |
| `common/scripted_effects/famine_core_effects.txt:841-1002` | Read-only occupation-law resolver. | Maps the current `occupation_law` to famine profiles and pressure deltas; it does not observe a transition or write a receipt. |
| `common/scripted_effects/famine_core_effects.txt:1005-1170` | Famine surface collector. | Consumes current occupation profile, Air Winter/bombing recency, camp evidence, and explicit war context; no generic owner callback. |
| `common/scripted_effects/famine_core_effects.txt:2538,2655-2707` | Exact famine mortality and condemnation owner. | A positive applied civilian loss supplies state, owner, food/environment/transport/policy/cause, people, generation, revision, and request ID, then emits deliberate-starvation and/or concealment condemnation once per state. |
| `common/scripted_effects/famine_adapter_effects.txt:252-320` | Famine condemnation adapter contract. | Requires event targets `famine_condemnation_state` and `famine_condemnation_actor` plus all proof variables; relief obstruction is available here but has no exact caller. |
| `common/scripted_effects/migration_core_effects.txt:740-774` | Migration pressure wrappers. | Bombing, war, peace, occupation, and other source enums are APIs only until a caller supplies a positive proven amount and actor. |
| `common/scripted_effects/migration_core_effects.txt:1595-1645` | Native safety projection. | Uses `damaged_building_level@rail_way` and `days_since_last_strategic_bombing` to set local safety flags; comments explicitly reject attacker attribution. |
| `common/scripted_effects/migration_core_effects.txt:2119-2135` | Country war/peace reassessment effects. | Records `migration_war_reassessment_pending` or `migration_peace_reassessment_pending`, dirties capacity, and registers the country; it does not create flight. |
| `common/scripted_effects/migration_persecution_effects.md:71` | Explicit unavailable-source statement. | States that generic occupation-law transitions lack changed state, responsible actor, generation, and replay identity. |
| `common/scripted_effects/cbrn_occupation_effects.txt:65-99` | Narrow occupation-law setters. | `cbrn_occupation_set_coercive_security_state`, `cbrn_occupation_set_protected_administration_state`, and clear-state policy call `set_occupation_law` directly. |
| `common/scripted_effects/cbrn_occupation_effects.txt:459-590` | Accepted CBRN operation owner. | Stores exact responsible actor, route, severity, civilian loss, attribution, and record identity; calls `famine_adapt_chemical_state` and records persecution. This is an operation seam, not a generic law-change hook. |
| `common/occupation_laws/chaosx_occupation_laws.txt:65-170` | Chaos Redux occupation-law definitions. | Defines the two CBRN laws and their availability/AI gates; no transition event or callback is defined. |
| `common/on_actions/humanitarian_runtime_on_actions.txt:72-105` | Existing country war/peace integration. | `on_war_relation_added` has `ROOT` attacker and `FROM` defender; `on_peace` uses ambient `THIS`; peace conference uses `ROOT` winner and `FROM` loser. All three only mark reassessment and revalidate corridors. |
| `common/scripted_effects/humanitarian_runtime_effects.txt:74-92` | Shared dispatch wrappers. | Routes state-control, war, peace, and nuclear callbacks into the separate famine and migration owners. |
| `common/scripted_effects/fallout_consolidated_effects.txt:2974-3014` | Strategic-bombing pressure source. | Uses only `days_since_last_strategic_bombing` thresholds and a bounded `air_winter_strategic_bombing_pressure`. |
| `common/scripted_effects/chaosx_event_cluster_effects.txt:407-553,760-838,1002-1165,1180-1350` | Cluster membership, participation, order, queue, and cooldown. | Member participation and order use random rolls; queued events are fired through the normal event path, with no famine/migration state or people receipt. |
| `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt:886-1040,1047-1133,2367-2430` | Scenario dispatcher and exact exceptions. | Selected scenario and intensity are country-scope inputs; the disaster barrage calls `call_natural_disaster`, while Fallout uses its own manual native sweep. Generic scenario intensity is not a famine/migration receipt. |
| `events/chaosx_event_clusters.txt:1-15` | Delayed cluster queue event. | Only `chaosx.event_clusters.2` exists and calls `event_cluster_fire_next_pending_member`. |
| `events/chaosx_triggerable_scenarios.txt:1-70` | Triggerable scenario acknowledgement events. | These are UI/acknowledgement events; they do not provide missing state-local incident facts. |
| `common/scripted_effects/camp_repression_rework_effects.txt:5111-5165` | Camp current-host custody owner. | Stages exact cohort ID/action/amount/actor/site/generation/revision/request, re-resolves the row, requires `state = event_target:migration_cohort_host`, and calls `migration_record_current_state_cohort_custody_exact`. |
| `common/scripted_effects/migration_adapter_effects.txt:65-231` | Custody receipt validator and ledger writer. | Requires a unique live row, exact current host, valid owner, whole-row amount, route proof, and accepted internment/forced-labor action, then records the owner achievement without moving population. |
| `common/scripted_effects/migration_adapter_effects.txt:237-356` | Migration condemnation adapters. | Forced return and violent pushback require exact cohort/state/people/route/actor/cause/generation/revision/request proof; deportation uses the same contract. |
| `common/scripted_effects/migration_forced_movement_effects.txt:~215-260` | Exact deportation owner. | The valid positive transfer branch supplies origin state, cohort, debit, route, actor, cause, transaction generation, revision, and request identity before `migration_condemn_deportation`. |
| `common/decisions/migration_decisions.txt:1875-1876,2502-2503` | Exact forced-return and violent-pushback owners. | Finalized transfer branches call `migration_record_exact_decision_condemnation`, which derives the adapter proof from the completed transaction. |
| `common/scripted_effects/condemnation_sanctions_effects.txt:371+` | Shared condemnation sink. | `condemnation_add_source` scales the supplied base gain by deaths/contamination, visibility, severity, and context; it cannot recover missing source facts. |

## Existing patterns

The split design's reusable pattern is an owner-supplied receipt followed by a fail-closed adapter. A caller must set explicit state/actor targets, positive measured amount, cause, generation, revision, and request identity before invoking a wrapper. The adapter adds pressure or condemnation and does not perform a second population mutation.

The famine mortality owner is the complete starvation/concealment precedent. The forced movement and finalized decision owners are the complete migration condemnation precedents. The camp owner is the complete current-host custody precedent. The CBRN accepted-operation owner is the closest exact operation precedent for a non-event state action.

The occupation resolver, Air Winter calculator, country war/peace hooks, event cluster queue, and scenario dispatcher are consumers or schedulers. Their current facts must not be promoted to incident receipts by inference.

## Vanilla or reference precedents

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md:2515-2522` documents `days_since_last_strategic_bombing` as a STATE trigger only; it does not provide attacker or amount.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md:6918-6933` documents `occupation_law` as a current STATE/COUNTRY trigger.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md:7434-7464` documents `set_occupation_law` and `set_occupation_law_where_available`; no generic transition callback is documented.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/occupation_laws/occupation_laws.txt` is the vanilla occupation-law definition set.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/events/GOE_Raj.txt:1605-1610` and `common/on_actions/13_goe_on_actions.txt:99` show explicit owner effects setting occupation law, not a global law-change receipt.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/common/on_actions/_documentation.md:24-40` and the offline On actions page define the country scopes for war, peace, peace-conference, state-control, invasion, and nuke callbacks.

## Authoritative fact and proof status

| Surface | Authoritative facts available now | Truly unavailable or not supplied | Complete non-inferred proof bundle now? |
| --- | --- | --- | --- |
| Generic occupation-law changes | Current state `occupation_law`; state `OWNER`/`CONTROLLER`; direct Chaos Redux CBRN setter callsites. | A generic law-transition callback with old/new law, actor, changed state, generation, and replay identity. | No. CBRN accepted operation is complete for its operation, not for every law change. |
| Strategic bombing | State `days_since_last_strategic_bombing`, rail damage, local `migration_bombing_active`, bounded Air Winter pressure. | Bomber/attacker, exact strike amount, civilian-loss transaction, operation ID, and state callback. | No. The two bombing request wrappers have definitions but no current producer callsite. |
| Country war/peace | `ROOT`/`FROM` country pair on `on_war_relation_added`; ambient `THIS` on `on_peace`; winner/loser on `on_peaceconference_ended`; `has_war`. | Affected state, cohort, people amount, causal action, or route identity. | No for direct famine/migration pressure or condemnation. Current reassessment wiring is complete only as reassessment. |
| Cluster queue | Cluster/member IDs, danger, participation chance, chaos tier, queue order, cooldown, and member event context. | Incident state, affected people, responsible actor, applied loss, or route identity for generic members. | No. Queue evidence is scheduling evidence only. |
| Triggerable scenarios | Selected country, selected scenario ID, intensity, scenario-specific flags; natural-disaster API can carry a selected target and downstream aftermath. | Generic state/people/actor facts for most scenario dispatches. | No generically. Event 013 and Fallout downstream owners must be audited separately. |
| Events 118/120/131 absence | Search found no root `chaosx.nr118.1`, `chaosx.nr120.1`, or `chaosx.nr131.1` under `events/`; scenario and planning references do not create source owners. | Missing source specifications, owner callsites, and event-chain evidence. Existing `chaosx.nr3.120`, `chaosx.nr3.131`, and `chaosx.nr5.131` are unrelated descendants, not replacements. | No. Do not fabricate a new numbered event or use an unrelated descendant. |
| Camp current-host custody | Exact live cohort row, unique ID, current host state, owner, action, amount, route, actor, site, generation, revision, and request identity. | Nothing required for the custody receipt at the current operation seam; it does not prove generic movement or condemnation by itself. | Yes for custody, subject to the existing valid-row branch. |
| Deliberate starvation | Positive applied famine mortality plus state/owner, food stage, environment, transport, extraction policy, cause, generation, revision, and request identity. | No missing fact at the current mortality owner. | Yes; already wired in `famine_record_exact_mortality_condemnation`. |
| Verified relief obstruction | Fail-closed famine condemnation wrapper and shared sink. | No current exact caller with state/actor targets, positive people amount, food/environment/transport/policy/cause, generation, revision, and request identity. | No. |
| Concealment | Exact positive famine mortality and `famine_crisis_concealed`, with the same proof bundle as starvation. | No missing fact at the current mortality owner. | Yes; hidden condemnation is emitted once per state. |
| Forced return | Finalized transfer, exact origin/destination, cohort ID, positive debit, route deaths, actor, cause, transaction generation, revision, and request identity. | No missing fact in the two exact decision branches. | Yes; `migration_record_exact_decision_condemnation` supplies the adapter. |
| Violent pushback | Same finalized transfer facts, with violent-pushback context and exact route-death output forwarded without a second Deaths mutation. | No missing fact in the exact decision branch. | Yes. |

## Likely edit order for the parent

1. Keep the current exact seams unchanged as the source of truth: famine mortality, forced movement, finalized migration decisions, camp custody, and accepted CBRN operations.
2. If generic occupation-law integration is still required, instrument each known law-setting owner with an explicit state/actor/generation/request receipt; do not invent an `on_occupation_law_changed` hook or infer from the current-law resolver.
3. If bombing integration is required, route only from a concrete strike/loss owner that can supply attacker and measured amount. Treat `days_since_last_strategic_bombing` as a bounded environmental modifier, not as an incident owner.
4. Retain war/peace callbacks as reassessment-only. Add direct famine/migration pressure or condemnation only in a concrete state/cohort owner invoked by the war/peace outcome.
5. Keep cluster/scenario dispatch as scheduling. Audit each downstream event's exact owner separately; do not attach famine or migration effects to cluster membership, queue timing, or scenario intensity alone.
6. Treat the missing 118/120/131 roots as a source-recovery blocker. Continue without a new numbered event, and do not map unrelated numbered descendants into the split mechanics.
7. Relief obstruction remains queued until a real relief-obstruction owner can provide the complete famine condemnation receipt. No wrapper call should be added to a decision merely because it has a relief or concealment label.

## Validation checks

- Confirm no new event root is added: `rg -n "id\s*=\s*chaosx\.nr(118|120|131)\.1" events`.
- Confirm generic law and bombing wrappers remain owner-gated: `rg -n "set_occupation_law|famine_request_bombing_pressure|migration_request_bombing_pressure" common/scripted_effects common/on_actions`.
- Confirm country callbacks remain reassessment-only: `rg -n -C 3 "on_war_relation_added|on_peaceconference_ended|on_peace|humanitarian_mark_country_(war|peace)_reassessment" common/on_actions/humanitarian_runtime_on_actions.txt common/scripted_effects/humanitarian_runtime_effects.txt`.
- Confirm exact condemnation callers and no duplicate mortality path: `rg -n "famine_record_exact_mortality_condemnation|famine_condemn_relief_obstruction|migration_condemn_deportation|migration_record_exact_decision_condemnation|migration_condemn_forced_return|migration_condemn_violent_pushback" common/scripted_effects common/decisions`.
- Confirm camp custody's current-host guard remains present: `rg -n -C 5 "migration_cohort_custody_route_proven|state = event_target:migration_cohort_host|migration_record_current_state_cohort_custody_exact" common/scripted_effects/camp_repression_rework_effects.txt common/scripted_effects/migration_adapter_effects.txt`.
- For any weighted follow-up, start with `hoi4.probability_inspect` and require a same-scenario `hoi4.probability_compare` through `chaosx_ai_probability_auditor`. The installed tool registry has no callable `chaosx_ai_probability_auditor`, so a complete detailed probability pass is currently blocked.

## Risks and blockers

Confirmed blockers:

- No generic occupation-law transition callback is available in the repo or the consulted vanilla documentation.
- No strategic-bombing callback with attacker, amount, or operation identity is available; the engine fact is only state-local bombing recency.
- Generic war/peace callbacks cannot identify a state/cohort incident.
- The requested 118/120/131 roots have no matching source owner; unrelated numbered descendants must not be substituted.
- The detailed probability auditor route is not installed as a callable MCP tool. The available probability adapters cannot satisfy the required auditor handoff alone.
- The targeted event scan was authoritative but partial because the large workspace deferred helper/lifecycle passes. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/298a789886cac842fc24378a2ee58cf991865891bf9dd35bf612b778e2fded0b/c4dd09ecdaedb087cdc67fd9963319bc841742cbdb0bceaf195290b199c70ab6/event-scan-f588a2607444.json` for `chaosx.nr5.1`. The targeted event render request was interrupted and produced no rendering artifact, so source review is not being represented as render evidence.

Ordinary risks:

- Direct `set_occupation_law` effects can be scattered across country/event/focus owners; each must be mapped before adding a receipt.
- A cluster's participation or cooldown roll is not a causal probability for famine or migration and must not be used as one.
- Condemnation's shared sink scales only supplied deaths and contamination; it cannot recover missing cohort, state, actor, or replay identity.

## Recommended next action

Parent should integrate only the already complete exact seams and queue the remaining work by owner: first recover or name the real occupation-law and bombing producers, then add explicit receipts at those owners, while leaving generic war/peace, cluster/scenario, and missing-event surfaces as reassessment/scheduling or source-recovery blockers. No new event ID is needed for this route.
