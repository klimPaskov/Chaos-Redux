# Repo Explorer Handoff

## Scope read

- Parent task: Re-audit the documented famine/migration owner-source blockers against the live Chaos Redux worktree and identify exact proof-owning callers, exposed facts, and the smallest safe edit order.
- Explicit constraints: This was a read-only source audit. The famine and migration namespaces remain separate. No famine/migration event IDs, fake facts, or world scans were introduced or inferred. The only permitted write was this handoff.
- Blockers audited: generic occupation-law transitions; strategic bombing attribution, amount, and state; war and peace affected state/cohort/amount; generic cluster/scenario dispatch; verified relief obstruction; and absent roots `chaosx.nr118.1`, `chaosx.nr120.1`, and `chaosx.nr131.1`.
- Design and status references read: `AGENTS.md`; `docs/plans/famine_and_migration_system_plans/subagent_handoffs/remaining_owner_receipts.md`; `docs/plans/famine_and_migration_system_plans/completion_report.md`; the current famine/migration system/spec/plan handoffs; `.agents/skills/chaos-redux-events/SKILL.md`; and `.agents/skills/chaos-redux-subagents/SKILL.md`.
- Required reference surfaces recorded by the prior owner receipt were retained: the offline Paradox wiki pages for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding; and vanilla documentation for triggers, effects, occupation laws, and on actions under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`.
- HOI4 MCP evidence: live Event 013, cluster, and scenario acknowledgement inspections/renders were run. Weighted surfaces began with `hoi4.probability_inspect`. The callable `chaosx_ai_probability_auditor` is not installed or exposed in the current tool registry, so no auditor-owned probability compare/evaluate pass is claimed.

## Primary findings

| Documented blocker | Exact current proof-owning caller now exists? | Current conclusion |
| --- | --- | --- |
| Generic occupation-law transition | No. A narrow CBRN accepted-operation owner exists, but it is not a generic law-transition hook. | `famine_request_occupation_pressure` and `migration_request_occupation_pressure` are definitions only. Current law reads are reassessment/profile inputs, not transition receipts. |
| Strategic bombing attribution/amount/state | No generic caller. | Native state recency and rail damage expose bounded state modifiers only. Air Winter has an exact loss owner, but it does not expose a generic bombing operation or bomber attribution. |
| War/peace affected state/cohort/amount | No. | Country war/peace callbacks only mark reassessment and corridor/capacity work. They do not expose an affected state, cohort, people amount, route, or incident owner. |
| Generic cluster/scenario dispatch | No generic famine/migration proof owner. | Dispatchers select and schedule content. Event 013 has an exact downstream state-loss owner; Fallout has a separate manual scenario owner. Neither makes the generic queue/scenario dispatcher a receipt owner. |
| Verified relief obstruction | No. | `famine_condemn_relief_obstruction` is validator-gated and has no current source caller. |
| Event roots 118/120/131 | No. | No current source hits for `chaosx.nr118.1`, `chaosx.nr120.1`, or `chaosx.nr131.1`. Existing `chaosx.nr3.120`, `chaosx.nr3.131`, and `chaosx.nr5.131` are unrelated descendants and are not substitutes. |

The re-audit therefore leaves the six documented generic/source-recovery blockers open. The exact narrow seams remain closed and usable: accepted CBRN operations, Air Winter exposure loss, Event 013 natural-disaster loss, current-host camp custody, deliberate starvation/concealment mortality, deportation, and forced-return/violent-pushback decision transfers.

## Relevant files

| Path | Why it matters | Evidence |
| --- | --- | --- |
| `docs/plans/famine_and_migration_system_plans/subagent_handoffs/remaining_owner_receipts.md` | Prior owner-source matrix and fail-closed boundary. | Lines 12-18 and 68-81 already identify the same generic gaps and the exact narrow seams. |
| `docs/plans/famine_and_migration_system_plans/completion_report.md` | Current completion/blocker status. | Lines 82-95 list generic occupation, bombing, war/peace, cluster/scenario, and missing-event blockers; lines 160-170 retain relief and source-owner gaps. |
| `common/scripted_effects/cbrn_occupation_effects.txt` | Narrow exact occupation operation owner. | Lines 459-543 validate an accepted CBRN operation, record owner/actor/date/agent/route/severity/payload/disruption/death/contamination/evidence/attribution/generation/revision data, and call `famine_adapt_chemical_state` at line 538. Lines 70-99 only set known CBRN laws; they do not receive arbitrary old-law/new-law transitions. |
| `common/occupation_laws/chaosx_occupation_laws.txt` | CBRN occupation-law definitions and AI gates. | Lines 65-170 contain the laws and availability logic, with no generic transition callback or receipt. |
| `common/scripted_effects/famine_core_effects.txt` | Famine occupation profile and pressure API census. | Lines 512, 530, and 532/544 define occupation/war/peace/cluster/scenario request wrappers without current callers. Lines 838-1002 read the current `occupation_law` into a profile; they do not expose a transition actor, old law, new law, amount, generation, or replay identity. |
| `common/scripted_effects/migration_core_effects.txt` | Migration occupation/bombing/war/peace/cluster/scenario API census and reassessment. | Lines 740, 750, 760, 762, 772, and 774 are definitions without current incident callers. Lines 1670-1691 only process pending country reassessment; lines 2119-2135 mark war/peace reassessment. |
| `common/scripted_effects/fallout_consolidated_effects.txt` | Native bombing recency and exact Air Winter loss owner. | Lines 2993-3014 use state-local `days_since_last_strategic_bombing` and rail damage only as bounded pressure/modifier inputs, with no attacker or operation amount. Lines 4004-4049 compute and apply exact Air Winter state civilian loss, record state/phase/environment/shelter/transport/adaptation/policy/actor/cause/source/generation/revision/date, and call `famine_adapt_air_winter_state`. |
| `common/scripted_effects/migration_core_effects.txt` | Native state safety projection. | Lines 1595-1629 explicitly state that bombing recency is state-local and deliberately has no attacker attribution; rail damage and recency only dirty route/capacity state. |
| `common/on_actions/humanitarian_runtime_on_actions.txt` | Live war/peace callbacks. | Lines 72-105 show `on_war_relation_added`, `on_peace`, and `on_peaceconference_ended` marking country reassessment/revalidation. Lines 107-112 show the separate `on_naval_invasion` exact corridor attack source with invaded state and invading country context. |
| `common/scripted_effects/humanitarian_runtime_effects.txt` | Shared reassessment wrapper. | Lines 74-92 call separate `famine_mark_country_*_reassessment` and `migration_mark_country_*_reassessment`; they do not create incident receipts. |
| `common/scripted_effects/chaosx_event_cluster_effects.txt` | Generic cluster member loading, random selection, queueing, and dispatch. | Lines 407-555 load member IDs/roles/chances; lines 760-860 prepare a random firing order; lines 1161-1165 schedule the delayed cluster event; lines 1180-1232 dispatch Event 013 through `call_natural_disaster` or other members through `fire_event_by_temp_id_no_cluster`; lines 1234-1351 queue and clear. No famine/migration state/people/actor receipt is produced. |
| `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt` | Generic scenario selection and dispatch. | Lines 886-1042 select a country-scoped scenario. Lines 1045-1132 set scenario/caller/intensity metadata and call `call_natural_disaster`; lines 2367-2430 route collapse and Fallout scenarios. Intensity and scheduling are not affected state/cohort/amount facts. |
| `common/scripted_effects/013_natural_disasters_effects.txt` | Exact Event 013 downstream owner. | Lines 5244-5364 compute a positive state death amount, call `apply_exact_state_civilian_population_loss` at lines 5333-5343, record Event 013 state/country/family/severity/sequence/death-driver/cause/revision/date proof, and call `famine_adapt_natural_disaster_state` at line 5363. This is a downstream exception, not generic cluster/scenario ownership. |
| `events/chaosx_event_clusters.txt` | Current delayed cluster event namespace. | Lines 1-15 contain `chaosx.event_clusters.2` and `event_cluster_fire_next_pending_member`; no famine/migration incident owner. |
| `events/chaosx_triggerable_scenarios.txt` | Scenario acknowledgement/UI events. | Lines 1-70 contain acknowledgement events only; they do not expose affected state/cohort/amount facts. |
| `common/scripted_effects/famine_adapter_effects.txt` | Relief and condemnation validation boundary. | Lines 249-274 require state and actor targets, state/food/environment/transport/policy/actor/cause proof, positive people amount, generation, revision, and request ID. Lines 291-303 define `famine_condemn_relief_obstruction` but there is no current gameplay caller. |
| `common/scripted_effects/famine_adapter_effects.md` | Explicit API/caller documentation. | Line 22 records that the relief-obstruction API has no current exact caller and remains fail-closed. |
| `common/scripted_effects/camp_repression_rework_effects.txt` | Exact current-host camp custody owner. | Lines 5102-5165 validate staged cohort custody, resolve the exact current host/cohort row, call `migration_record_current_state_cohort_custody_exact` at line 5145, record the receipt, and clean staging. |
| `common/scripted_effects/migration_adapter_effects.txt` | Exact migration receipt validators and wrappers. | Lines 65-109 enforce live aligned ledgers, exact row, current host, positive transaction/actor/route/site/generation/revision/request facts. Lines 111-231 resolve one exact row. Lines 233-355 validate and record deportation, return, and pushback decision receipts. |
| `common/scripted_effects/famine_core_effects.txt` | Exact mortality owner for starvation/concealment. | Lines 2510-2538 apply exact state civilian loss and record mortality. Lines 2650-2707 require positive loss and proof, then call `famine_condemn_deliberate_starvation` or `famine_condemn_concealment` only under their explicit conditions. |
| `common/scripted_effects/migration_forced_movement_effects.txt` | Exact deportation transfer owner. | Lines 210-270 finalize a positive exact transfer, set state/cohort/people/route/actor/cause/generation/revision/request facts, call `migration_condemn_deportation` at line 250, and record the transaction. |
| `common/decisions/migration_decisions.txt` | Exact forced-return/pushback decision owners. | The enforced-closure branch around lines 1871-1905 and the forced-repatriation branch around lines 2485-2557 stage exact routes and call `migration_record_exact_decision_condemnation` only after positive finalized transfer/debit checks. |
| `events/` and `common/` source census | Requested event-root recovery. | `rg -n "chaosx\.nr118\.1|chaosx\.nr120\.1|chaosx\.nr131\.1" events common decisions on_actions` returned no hits. |

## Existing patterns

The current project pattern is an owner-supplied, fail-closed adapter. An adapter may consume a receipt only after the actual owner supplies a state or host, actor, positive amount, cause, generation, revision, and request identity. Famine and migration wrappers are separate; a famine adapter does not imply a migration receipt and vice versa.

The exact CBRN accepted-operation path is the closest occupation-related precedent. `cbrn_occupation_apply_accepted_operation_state` owns the operation and supplies explicit actor, state, route, policy, causal, attribution, and replay fields before calling the famine adapter. It cannot be generalized to a law transition because `cbrn_occupation_set_*_state` only changes known CBRN laws and stores policy state.

The exact Air Winter path is the closest bombing-related precedent. It owns the positive state population loss and then records an exposure receipt. The separate state projection uses bombing recency and rail damage as modifiers only. Neither path can prove attacker attribution or a generic strike amount.

The exact Event 013 path is the closest cluster/scenario precedent. The cluster/scenario code supplies target and scenario metadata, then Event 013 owns the actual affected state and positive loss. This preserves the boundary between dispatch metadata and proof-bearing gameplay mutation.

The camp, mortality, deportation, and decision paths all follow the same one-owner/one-receipt pattern. They validate exact rows or exact state loss before condemnation and avoid a second population mutation in the adapter.

## Vanilla or reference precedents

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md:2515-2522` documents `days_since_last_strategic_bombing` as a state-scoped recency trigger. It does not provide bomber identity, strike amount, operation ID, or a generic transition callback.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md:6918-6933` documents `occupation_law` as a current state/country trigger, not an old-law/new-law transition receipt.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md:7434-7464` documents `set_occupation_law` and `set_occupation_law_where_available`. The inspected documentation has no generic `on_occupation_law_changed` owner callback.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/occupation_laws/occupation_laws.txt` is the vanilla law-definition precedent; it defines law data and availability rather than a transition event stream.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/events/GOE_Raj.txt:1605-1610` and `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/on_actions/13_goe_on_actions.txt:99` are a direct-owner precedent for a specific scripted law/effect route, not proof of a generic law-change hook.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/common/on_actions/_documentation.md:24-40` documents on-action registration and does not list a generic occupation-law transition or strategic-bombing attribution callback.
- The offline Paradox wiki pages listed in `AGENTS.md` were used as the parallel syntax/scope reference; no wiki or vanilla precedent was found that supplies the missing generic owner facts.
- No approved reference-mod pattern was needed to resolve these blockers. A reference mod would not substitute for a live owner receipt in this design.

## Likely edit order for the parent

1. Keep all six generic APIs fail-closed and preserve the separate `famine_*` and `migration_*` namespaces. Do not create a synthetic on-action, event ID, world scan, or proxy descendant.
2. For occupation, first identify a real current caller that performs the relevant generic `set_occupation_law` operation. Instrument that owner with state, actor, old/new law where available, positive causal amount, generation, revision, and request facts; only then call the separate famine and migration adapters. Do not treat `famine_resolve_occupation_profile` as a transition owner.
3. For strategic bombing, first identify the concrete strike or loss owner that exposes the impacted state, positive measured amount, attacker/actor, and operation/replay identity. Apply the exact state loss or incident receipt there, then call the separate adapters. Keep `days_since_last_strategic_bombing`, rail damage, and Air Winter exposure as bounded native/provenance-specific inputs only.
4. For war and peace, retain the current country reassessment callbacks. Add direct pressure only at a concrete battle, control-change, corridor, or cohort-transfer owner that exposes state/cohort/amount/route/actor/cause facts; the country relation callbacks cannot be upgraded safely by inference.
5. For cluster/scenario behavior, trace each member to its downstream owner. Keep Event 013 and Fallout on their own exact owner paths; do not make `load_event_cluster_members`, `prepare_event_cluster_firing`, `trigger_selected_chaosx_scenario`, or scenario intensity a famine/migration receipt.
6. For relief obstruction, require a concrete relief owner that proves viable route, refusal/blocking action, state, actor, positive affected people, food/environment/transport/policy/cause, generation, revision, and request. Call `famine_condemn_relief_obstruction` once from that owner only after `famine_validate_condemnation_receipt_exact` passes.
7. For Events 118/120/131, recover the authoritative source specification or owner mapping before any event work. If no authoritative roots exist, document that as a source-recovery decision; do not alias `nr3`/`nr5` descendants and do not fabricate roots.
8. After any owner is supplied, rerun the narrow source callsite census, relevant event inspection/render, probability inspection, and the required probability auditor route. Update the completion report only from the resulting live evidence.

## Validation checks

- Re-run `rg -n "famine_request_(occupation|bombing|war|peace|cluster|scenario)_pressure|migration_request_(occupation|bombing|war|peace|cluster|scenario)_pressure" common events decisions on_actions` and require each new callsite to be in a concrete owner rather than a dispatcher or reassessment callback.
- Re-run `rg -n "famine_condemn_relief_obstruction" common events decisions on_actions` and require one owner-bearing callsite plus the full validator inputs before changing the relief status from blocked.
- Re-run `rg -n "chaosx\.nr118\.1|chaosx\.nr120\.1|chaosx\.nr131\.1" events common decisions on_actions` after any source recovery; inspect the exact root event rather than accepting similarly numbered descendants.
- For occupation and bombing, inspect the owner’s emitted facts for state, actor, positive amount, cause, generation, revision, and request/operation identity. A law read or bombing recency flag is not sufficient.
- For war/peace, verify that any new proof-bearing caller exposes the affected state/cohort/amount and does not merely call `*_mark_country_*_reassessment`.
- For cluster/scenario changes, inspect both the dispatcher and downstream owner. Confirm that dispatch metadata does not become a population or cohort fact by assumption.
- Existing HOI4 MCP artifacts for this audit: Event 013 trace `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f56231b01f0ebcfde0fce7017132aee866696e47c165a112fb53b4113270d290/0e85f81e2855ef9003224984d125957d7eec8b3e4c4e800fe3479dfc8a13beb4/event-trace-f588a2607444.json`; Event 013 render manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/be8cbd1e2e9134f5f780d20e0ccf133ad80eb4819404f98eee5fc125285b6a15/c636a3738ac602fbf7cbc9141502d512e55c8802ee48d0e764f58701a91ab68f/event-state-f588a2607444-manifest.json`; cluster trace `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b8da1b3e6f9c108563d435f79afed553b0540aab1ce184f05ec50e748e9207e7/ff112ccb8f1e4b8bc010a18f72aa408958e4a033d4d4bd34ee6e4a58ff7d29b9/event-trace-f588a2607444.json`; cluster render manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fb38962fa53ca6e7f94c3df85058521429c65871c5ceadd1d0e160398585184a/c41412a8682f6e89fc07b3f5f906e35842054a0a3adb4e5b4de019db8aaed471/event-state-f588a2607444-manifest.json`; scenario trace `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/14b6ed883ddf1f48a63cb8c5b6811b1f8eca8681bca0dca063dcfb36becaf1fd/d0d485aff9c1b701899c212a07d9d23c7ad251bc60f02428f41d50a62b970461/event-trace-f588a2607444.json`; and scenario render manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9de0afcbf6f104ed37a1e2285c8f7d00332133de4ed8d8cd52d7b04a0ebfd376/d1fd2970988ed0674c2baa0077aac8b0a8163da836125cf68a0c461081da22f2/event-state-f588a2607444-manifest.json`.
- These event inspections/renders were `*_PARTIAL` with 14 blocking diagnostics and large omitted-node counts in the current workspace; they support live surface mapping but are not a clean full-engine completion proof.
- Probability inspection artifacts include the scenario direct/random-list passes and cluster random-list pass. The cluster `direct_random` inspection returned `INTERNAL_ERROR` with no files scanned; the random-list pass reported no weighted surfaces because the parser did not model the `set_temp_variable_to_random` route. The scenario random-list pass reported unresolved required inputs. No `chaosx_ai_probability_auditor` callable exists, so the required detailed auditor pass remains unavailable and must be reported as such.

## Risks and blockers

### Confirmed blockers

- No generic occupation-law transition callback or exact current caller exposes old law, new law, actor, affected state, amount, and replay identity together.
- No generic strategic-bombing caller exposes attacker, operation identity, affected state, and positive amount. Native recency and rail damage are modifiers, not attribution.
- War/peace on actions expose country relation scopes only and intentionally trigger reassessment/capacity work. They do not prove affected state/cohort/amount.
- Generic cluster/scenario dispatchers expose member/scenario/intensity metadata only. Exact facts appear only at downstream owners such as Event 013.
- `famine_condemn_relief_obstruction` has no current gameplay caller and must remain fail-closed.
- Requested roots `chaosx.nr118.1`, `chaosx.nr120.1`, and `chaosx.nr131.1` are absent from the current source census. Similar numeric descendants are not valid replacements.
- The installed tool registry has no callable `chaosx_ai_probability_auditor`; the mandatory route cannot be completed in this environment. The cluster direct-random inspect also returned an internal error, and current event inspections/renders are partial because of source diagnostics/omitted nodes.

### Inference hazards

- Do not infer a law transition from the current `occupation_law` value or from CBRN policy state.
- Do not infer bombing attribution or casualties from `days_since_last_strategic_bombing`, damaged rail, or a country-level scenario intensity.
- Do not infer affected state/cohort/amount from country war/peace callbacks, cluster member IDs, event IDs, or acknowledgement events.
- Do not treat an event number that resembles 118, 120, or 131 as the missing root.
- Do not connect a famine receipt to migration without its own migration owner facts, or a migration receipt to famine without its own famine owner facts.

## Recommended next action

Keep the six generic/source-recovery blockers explicitly fail-closed in the completion documentation. The next implementation pass should begin only when the parent can point to a concrete owner for one blocker and can record its exact state/cohort/amount/actor/cause/generation/revision/request facts. The narrow exact callers documented above can remain unchanged and should not be generalized by inference.
