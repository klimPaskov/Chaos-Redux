# Biological native raid temporary-output audit

Date: 2026-10-07.
Disposition: unresolved candidate defects, with source-model reproduction for the isolated deterministic helpers.
Parent authorization: bounded read-only audit of ordinary biological native raid callbacks and exact called lifecycle interfaces.
Owned change: this new handoff only.
No gameplay, tests, shared documentation, probability weights, Git index, or commits were changed.

## Result

The actor-country bridge reconstructs agent and native result identity from chain-local markers and preserves exact actor, victim, and target-state pointers.
The ordinary adapters contain multiple missing caller-owned temporary output declarations that can prevent payload validation, lose outcome selection, suppress acceptance history after a real seed, and lose the agent selector needed for incubation scheduling.
These are source-model candidate defects supported by the documented conservative helper-frame contract, not observations of native engine execution.
The recommended repair is existing-name caller storage at the exact returning boundaries, with no balance change, new transaction layer, payment path, refund, or replacement target.

## Required reading and scope evidence

Read `AGENTS.md`, `.agents/skills/chaos-redux-events/SKILL.md`, `.agents/skills/chaos-redux-native-raids/SKILL.md`, and `.agents/skills/chaos-redux-subagents/SKILL.md`.
The events skill's Helper output lifetime contract at lines 175-184 requires caller-owned scalar and temporary-array outputs at every nested return boundary.
Read the existing neutral-helper registry overview in `common/scripted_effects/chaosx_dynamic_effects.txt` and its matching markdown.
It keeps event-owned orchestration in owner files, so this repair does not need a neutral registry helper.
No decisions or GUI buttons are changed or audited here, so their implementation skills were not applied.

Reference routes were exposed and responded live.
`hoi4.reference_context(surface=event)` identified both source kinds, but omitted On actions and Localisation and did not establish detailed coverage of them.
Neither topic is used for a new implementation in this read-only audit.

| Source | Read span | Revision SHA-256 | Claim supported |
| --- | --- | --- | --- |
| `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` | 435-443 through `reference_read` | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` | Temporaries are unscoped, do not cross fired events, may disappear after returning scripted helpers, and caller-predefined storage retains changes. |
| Same offline Data structures page | 303-311 through `reference_read` | Same revision | Regular targets carry into fired events and automatically end with their effect chain. |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/raids/_documentation.md` | 167-184 through `reference_read`, 245-300 and 547-557 directly | `eac06474fcbde3920523b9b49364f7797851c0cc45f4f0ef41321999a93be43e` | Native essential equipment is collected after creation, both callback families begin in RAID_INSTANCE, and actor/victim/state pointers are native dynamic variables. |
| Installed `documentation/effects_documentation.md` | 6496-6504 through `reference_read`, 2943-2965 directly | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` | `save_event_target_as` supports any scope, and `country_event` is a country-scoped effect. |
| Installed `common/raids/land_infiltration_raids.txt` | 169-184 directly | Precedent read, not asserted byte-identical afterward | Vanilla enters `var:actor_country` explicitly within actor callbacks and leaves native raid-unit effects in RAID_INSTANCE. |

The installed docs establish scopes and commands but do not promise identical temporary lifetime in every helper path.
The offline lifetime warning is the basis for the conservative model and safe initialization repair.
No Paradox web access was used.

## Actual caller, scope, and value map

`common/raids/biological_battlefield_raids.txt` calls bridge `.1`, `biological_sabotage_raids.txt` calls `.2`, and `biological_raids.txt` calls `.3` from native actor callbacks.
Each callback saves exact regular scope targets and its immutable agent/outcome markers, then fires an immediate hidden country event from `var:actor_country`.
The victim callback is presentation-only for the ordinary adapter transaction.
Bridge `.1` calls `bio_resolve_battlefield_dissemination`, `.2` calls `bio_resolve_supply_chain_raid_outcome`, and `.3` calls `bio_resolve_strategic_raid_outcome`.
Their ROOT is the actor country throughout the returning helper calls, and state or victim work enters explicit event-target scopes.

| Caller and source lines | Returning helper | Inputs | Outputs consumed after return | Persistent side effects or consumer |
| --- | --- | --- | --- | --- |
| Battlefield resolver, `biological_battlefield_effects.txt:482` | `bio_battlefield_set_payload_internal` | `bio_battlefield_agent` | `bio_battlefield_payload_required`, `bio_battlefield_payload_consumed`, `bio_battlefield_weaponization_mult` | Payload validator, seed record and actor consumption history. |
| Battlefield primary-release adapter, line 265 | `bio_battlefield_map_engine_result_internal` | `bio_battlefield_engine_outcome` | `bio_battlefield_lifecycle_result` | Copied into `bio_seed_result`. |
| Battlefield resolver, line 487 | `bio_battlefield_record_failed_attempt_evidence_internal`, state scope | Exact actor/state/victim pointers, agent | `bio_battlefield_attempt_lead_matches_actor` | State attempt evidence persists, then actor condemnation selects visibility from the output. |
| Strategic resolver, lines 571-574 | Reservation and weaponization helpers, then `bio_strategic_raid_select_outcome_internal` | `bio_raid_agent`, engine result, exact actor | Required payload and weaponization are owned, `bio_raid_outcome` is not | Reservation validator and outcome branches. The selector itself owns its outcome before nested failure/success selectors. |
| Strategic resolver, line 583 | `bio_strategic_raid_record_failed_attempt_evidence_internal`, state scope | Exact actor/state/victim pointers | `bio_raid_attempt_lead_matches_actor` | Already owned by resolver line 562. This boundary is covered. |
| Sabotage resolver, line 153 | `bio_sabotage_raid_set_agent_parameters`, then agent parameter helper | `bio_raid_agent` | `bio_sabotage_agent`, required payload/support, consumed payload/support | Used in seed record and actor resolution ledger. Two returning boundaries need storage. |
| Sabotage resolver, lines 154 and 160 | Result selector and actor program getter | Engine result, country readiness/attribution | `bio_sabotage_result`, `bio_sabotage_weaponization_mult`, `bio_sabotage_concealment` | Failure branch, seed result, potency and concealment. |
| Sabotage resolver, line 163 | `bio_sabotage_record_failed_attempt_evidence_internal`, state scope | Exact actor/state/victim pointers, agent | `bio_sabotage_attempt_lead_matches_actor` | Actor condemnation visibility. |
| Each deliberate release adapter and strategic accident adapter | `bio_lifecycle_reset_seed_record`, then state `bio_lifecycle_dispatch_seed` | Agent, route, source, result, exact pointers and payload proofs | Reset defaults and `bio_seed_dispatch_status` | Adapter status copied from seed status. Resolver-owned adapter statuses survive, but the nested seed status does not have owned storage. |
| Seed dispatcher, `biological_lifecycle_effects.txt:844-849` | Route profile, agent profile, finalizer | Prepared seed inputs | Agent, route, result, doctrine, final intensity/share/evidence outputs | Dispatcher entry already owns those outputs. Nested finalizer also owns result and doctrine multipliers. Covered. |
| Seed dispatcher, line 854 | `bio_lifecycle_store_seed_in_current_agent_record`, state scope | Validated seed fields | `bio_active_agent` | State episode persists, then dispatcher meta blocks and incubation scheduling consume the selector. |
| Seed dispatcher, line 853 | `cbrn_diplomacy_classify_biological_seed_retaliation`, state scope | Exact actor/victim and deliberate route | `bio_seed_retaliation_status` | Stored in episode and unified action record. |
| Biological retaliation classifier, `cbrn_diplomacy_effects.txt:92` | Actor `cbrn_diplomacy_classify_retaliation_action` | Exact retaliation victim and proportionate proof | `cbrn_action_retaliation_status` | Copied to biological status. Generic classifier also persists its own country last-status fields. |
| Deliberate-use recorder, lifecycle lines 710-805 | `cbrn_append_unified_action_record`, actor scope | Existing named record fields and exact saved state/victim targets | Regular `cbrn_last_unified_action_record_row` | The consumed row is regular country storage, so this particular return is covered. The append helper's UID and row scratch are consumed inside its own frame. |

No temporary arrays cross these audited adapter boundaries.
Unified action-record arrays are persistent global arrays and are not modeled as temporary outputs.
There are no script-side payload debit or payload refund effects in the three audited ordinary adapters.

## Concrete candidate defects and minimal repair map

1. Battlefield payload values first originate inside `bio_battlefield_set_payload_internal` and are consumed by `bio_battlefield_payload_record_is_valid` after return without resolver-owned storage.
   The conservative model drops them and makes the positive-payload validator fail.
   Add zero storage for required and consumed payload, and owned storage for weaponization, in the resolver before the helper.
   The rejected-reservation recorder also calls this payload getter and consumes its returned values, so it needs the same applicable declarations locally.

2. Battlefield `bio_battlefield_lifecycle_result` first originates in its result mapper and is copied to the seed record after return.
   Own this existing result output in the primary-release adapter before mapping.

3. Strategic `bio_raid_outcome` is initialized inside the selector but not in the resolver.
   The nested random-selector return is covered by the selector's initialization, yet the outer selector return loses the outcome.
   Own `bio_raid_outcome` in `bio_resolve_strategic_raid_outcome` before its selector call.
   Keep all selection weights and branches byte-identical.

4. Sabotage agent parameters lose output at the agent helper return before the adapter computes consumed payload/support, and again at the adapter return to its resolver.
   Own the agent, required payload/support outputs in `bio_sabotage_raid_set_agent_parameters`, and own the forwarded agent/required/consumed outputs in the resolver.
   The command-power output is not a consumed runtime output on this native path and does not justify a new payment path.
   Own `bio_sabotage_result` before selection and weaponization/concealment before the actor program getter.

5. Battlefield and sabotage failed-attempt evidence helpers create lead-matches-actor status, persist state evidence, then lose that status before actor condemnation reads it.
   This can keep condemnation visibility hidden despite the freshly recorded matching evidence.
   Own the respective existing lead-matches-actor scalar in their resolvers before the state evidence call.
   Strategic resolver already owns the equivalent field.

6. All three release adapter families copy `bio_seed_dispatch_status` after the returning lifecycle dispatcher without owning it first.
   Even a valid state mutation can therefore be followed by a missing acceptance receipt, rejection/failure history, and skipped humanitarian/UWR/history integration.
   Initialize this existing receipt to missing immediately before dispatch in target-release, accident, and sabotage adapters.
   Battlefield friendly blowback also consumes it after dispatch to decide whether to record friendly exposure history and needs the declaration at that boundary.
   Keep resolver-owned adapter status separate from the seed receipt.

7. Seed reset defaults first created within the returning reset helper vanish unless the caller owns them.
   Many missing defaults equal zero and alone do not prove a visible failure.
   Nonetheless the public reset contract is incomplete, and default one values or caller-forwarded outputs require storage.
   Declare the reset fields needed by each adapter, using their documented defaults, before the reset call, without resetting immutable input or cursor fields.
   Review every forwarded reset output used across subsequent calls, rather than adding an unrelated output family.

8. Seed storage creates `bio_active_agent`, then returns to a dispatcher that uses this selector for detection and incubation meta blocks without owning it.
   The episode can be stored under the correct agent while post-store scheduling reads the absent selector as zero under the conservative model.
   Own `bio_active_agent` in the dispatcher before storing the seed.
   This is a shared biological lifecycle edit and requires parent coordination across non-raid consumers.

9. Biological retaliation output has two missing ownership boundaries.
   Own `bio_seed_retaliation_status` in the seed dispatcher before the biological classifier, and own `cbrn_action_retaliation_status` in that classifier before the actor generic classifier.
   Otherwise the regular generic retaliation history can persist while the biological episode/action row sees none.
   This is a shared diplomacy touchpoint also used by the chemical owner.

These are small caller-storage fixes using existing helper names and fields.
No new constants, tuning categories, event targets, cleanup scheduler, generic extraction, or mechanics redesign are proposed.
The current zero/missing/one constants already express the needed defaults.
Public owner API documentation should state the exact caller-owned outputs after the parent repair.

## Transaction, exact state, floors, and duplicate guard findings

Native `essential_equipment` remains the sole payload and sabotage-support debit.
Consumption variables in the adapters describe that native reservation and do not perform an additional stockpile debit.
The native reservation receipt is reconstructed from the fixed agent profile and completed callback, not a separate stored receipt of engine collection.
The audit does not prove native cancellation or recovery behavior.

Each bridge requires exactly one agent marker and one outcome marker and verifies actor identity before resolving.
The family marker names are disjoint, so these bridges do not depend on a shared pending scalar.
Ordinary target releases use the exact original saved native state and current victim controller.
Strategic accident uses an internal current actor-owned handling state chosen by the existing helper, and does not claim the real raid source airbase.
No primary target replacement was found.

The battlefield payload validator requires positive required payload and equal consumed payload.
The strategic reservation validator requires positive required/consumed values, a supplied proof, and consumed no greater than required.
Seed validation repeats actor/victim/controller, supported route/source/result, and positive payload checks.
These validators are rejection gates rather than fresh row-consumption receipts.
No tombstone transaction or compensation exists in this bounded native adapter path.

Seed finalization has existing intensity/share/evidence floors.
Those floors do not restore missing agent/result/payload identity and should not be increased to hide lifetime failures.
The dispatcher already owns agent profile, final-value, result-multiplier, and doctrine outputs.
Incubation scheduler locally owns its incubation-day getter outputs.
The principal missing scheduling value here is the selector forwarded from seed storage.

The `bio_native_raid_dispatch_in_progress` flag suppresses integrated release command-power recovery on the ordinary native deliberate path.
It is set and cleared around target-seed dispatch and is not a replay receipt.
Accident and connected-spread sources do not qualify for deliberate release recovery.

The exact-one marker checks prevent ambiguous dispatch but do not make repeated invocation of the same callback chain idempotent.
Sabotage rejects an already incubating/active same-agent episode, whereas battlefield/strategic lifecycle seed storage can strengthen an existing episode.
The audited source contains no unique native raid-instance resolution receipt proving replay suppression for those latter paths.
This is an explicit native callback-cardinality uncertainty, not evidence that the engine calls the callback twice.
Do not add an arbitrary pending scalar or permanent state flag to hide this uncertainty.

Actual outbreak, attribution, death, and action records are ordinary lifecycle state/country storage.
Immediate adapter acceptance does not certify that later protection-response ticks work.
There is no separate returning CBRN protection getter in the bounded immediate adapter path.
The delayed environment/countermeasure implementation is outside this audit, so protection effectiveness, weekly deaths, spread, and recovery cannot be marked validated by these probes.

## Meaningful validation performed

Ran 28 in-memory actual-source probes using the existing parser and strict-frame VM exported by `docs/plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js`.
No new generic VM, test file, or report generator was created.
The probes executed unmodified helper bodies with owned versus unowned output storage, using real numeric constants.
The model drops names first created by returning helpers, retains caller storage, and separates regular variables from temporary maps.

| Probe | Unowned result | Caller-owned result |
| --- | --- | --- |
| Four battlefield agent payload getters | All required/consumed/weaponization outputs dropped | Payloads 50, 25, 25, 10 and potency 1.25, 1.60, 0.95, 2.10 retained. |
| Three battlefield release-result mappings | Result dropped | Partial 2, success 3, catastrophic 4 retained. |
| Strategic critical result | Outcome dropped | Successful outbreak seed 5 retained. |
| Four sabotage parameter adapters including nested agent helper | All forwarded outputs dropped, consumed calculations see absent required fields | Agent identity retained with payload 10, 12, 10, 8 and support 40, 50, 40, 60. |
| Sabotage native success result | Result dropped | Success 3 retained. |
| Seed reset selected defaults | All selected defaults dropped | Weaponization one and explicit zero defaults retained. |

The existing parser cannot parse anonymous nested schema blocks in several constant files.
Two attempted loads failed before execution.
The successful probes stripped only constant schema declarations in memory and recursively loaded their unchanged numeric assignments, while leaving executed effect bodies unchanged.
No random selectors, stockpile transactions, meta expansion, native events, real scopes, or complete raid resolutions were simulated.
No fixture result is presented as probability or native execution evidence.

## MCP artifacts and limitations

`hoi4.source_lookup` read `bio_lifecycle_dispatch_seed`, definition lines 810-897, under source revision `eb277bd6a3588a4bf90095e8f59c8303d742e4059475f256341176b18dbfecc9`.
The bounded inline read covered 810-824 and identified continuation line 825, and the remaining body was read directly from the local source.

An initial event request used an invalid selector without `kind` and was rejected by argument validation.
The corrected namespace trace requested depth 1, nodes 8, edges 10, with helpers disabled.
It returned `EVENT_INSPECTED_PARTIAL` and source revision `4495e77851dc0c9ee60d7951092c239a04924d4bac48bc4bf83047d20eb0d1da`.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f3f888a73a8d3187865ad56599f04b202839c170a498851584e1f7b6a0c340fe/e5a0808c91412697c8726b4e5faef50a60ad39a615df77d2d4116350951f2e0a/event-trace-4495e77851dc.json`.
Its first 6,000-byte range was retrieved and confirms the filters, but does not establish the complete selected root/node coverage.
A full read returned a truncated/invalid payload despite range metadata, so full selection coverage remains unreadable here.
Top-level global inventory counts are not evidence that the selector was ignored, and no such conclusion is made.

A second narrow request selected event `biological_native_raid_bridge.1`, depth 1, nodes 4, edges 6, helpers disabled.
It returned the same partial status and revision.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/612ad2c4f4c4d1362fe08e2988b9edaa58c289d7ebc1c68a4109b08e0580aa7b/0f95cc29cc95a82edebc2fe36ada3811c01d8a6c89d7e9752a1a0a84dfe32833/event-trace-4495e77851dc.json`.
Its complete selection has not been read.
Both tools report one blocking event-chain diagnostic in the broader inventory, which cannot be attributed to this bridge from the inline summary.
No further event or probability calls were made after parent steering.
Event render/compare, probability evidence, complete graph artifact retrieval, full adapter transaction fixtures, and native consumer validation remain parent-owned or unresolved.

## Source snapshot hashes

Paths are relative to `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux`.
These hashes identify the audit snapshot and must be checked against parent edits before applying findings.

| File | SHA-256 |
| --- | --- |
| `events/biological_native_raid_bridge_events.txt` | `5796e5527386360858b3bfc9fa7ca85f2dc6b03c92a8c27fe774325d0085bbbc` |
| `common/scripted_effects/biological_raid_effects.txt` | `c3ecff927917a2bd444123731cbd1accbb4c7ecd06c704d7d58d2aeb5b6a0b4b` |
| `common/scripted_effects/biological_battlefield_effects.txt` | `441dc4dca276178b5489eb79f2f9af6519d53532ef3f9237b61f127d56ed7811` |
| `common/scripted_effects/biological_sabotage_raid_effects.txt` | `f3c222581ebf7d6d518c0c4eec8dea3e35b8fd4d515288fde75f25b1b8465716` |
| `common/scripted_effects/biological_sabotage_effects.txt` | `a2d5777a221755c71bcbb8d1b40c62917647191b0b84e9c310cc3a23ab50a306` |
| `common/scripted_effects/biological_lifecycle_effects.txt` | `898724cc42eab7a09c12173b493902c1b8695fdd961251f169c947107f97965d` |
| `common/scripted_triggers/biological_raid_triggers.txt` | `2855872ec2d83e4835450f85cdb976b0fe333590a5acb4b432644cad38e885a8` |
| `common/scripted_triggers/biological_battlefield_triggers.txt` | `a720d390ca152130e5593411e0bb17116559dc1f221296dce299b401fcb08e34` |
| `common/scripted_triggers/biological_sabotage_raid_triggers.txt` | `79048687fa29324e545e0df75296f40c3b5873c0287049479fbd9d8dd7ae0160` |
| `common/scripted_triggers/biological_lifecycle_triggers.txt` | `d98a10ee659ce86e705f49d3fc499f53901eef1cd111b90cf52c1103f9a3aed4` |
| `common/scripted_effects/cbrn_diplomacy_effects.txt` | `c005b6687b816c9fd8d09e1749f289a19239e63335afbd6c19641c7a33ef14d2` |
| `common/scripted_effects/cbrn_action_record_effects.txt` | `b18cd1274fc1972ab1b670322ed5d876c9a86bbe8f582e8ed71ca760654cd78e` |
| `common/raids/biological_raids.txt` | `80a7aed6e28a0c5a177d1d92eb0a196ae038dbaaf103ec2e40829745e4b2c268` |
| `common/raids/biological_battlefield_raids.txt` | `70d2cb8225ec2b9232ea10a645acdd296fd4e9649698a9ad8ff1edcb23a40ce5` |
| `common/raids/biological_sabotage_raids.txt` | `d1e055b63794b1c8784255a0ec59b1e1d792f4a60921d7d2e02b47b3209dccc5` |
| Existing strict-frame parser/VM module | `b048592fb35b86ae2dd915aec0cda54896f7d2f1c1d3a2e358bd2fe3b2e8ccf7` |
| `docs/systems/cbrn_warfare/biological_warfare/strategic_biological_raids.md` | `6d5423efdeaca3337f14f340833e9b10ce2c9a4be33afe92a8d1310428e97f6a` |

## Parent migration and follow-up

Apply caller declarations first in the three owner adapters, then in the shared seed dispatcher and biological diplomacy classifier, reviewing each boundary independently.
Initialize outputs using existing constants and retain all native reservation definitions, outcome weights, exact state pointers, protected consequence records, and history mutation sites.
Extend the existing task-specific actual-source test route with full caller execution and strict helper cleanup rather than testing only leaf getters.
Exercise accepted and rejected seeds, failed delivery, attacker accident, target/controller loss, same-agent existing episode, stale receipt followed by rejection, and successful receipt followed by a second invocation.
Assert native payload is never debited/refunded by script, no accepted seed is reported as a failure solely because of lost temporary outputs, and the stored agent matches the scheduler/action record.
The parent must establish the permitted native replay contract before choosing any new duplicate receipt mechanism.

Shared owner touchpoints: `biological_lifecycle_effects.txt`, `biological_sabotage_effects.txt`, and `cbrn_diplomacy_effects.txt`.
The diplomacy file is also relevant to the separately owned chemical pass and must not be overwritten wholesale.
The unified record append boundary itself consumes regular saved row storage and does not need an arbitrary new row output.

The strategic raid owner document still describes paid staging selection and partial payload refunds, contrary to the current fixed native full-consumption path and internal handling-state selection.
It needs parent documentation reconciliation and should not be used to reintroduce those retired mechanics.
No documentation changes outside this handoff were made.
Skills used: events, native raids, subagents.
Skills created or updated: none, because the existing events lifetime contract already covers the reusable rule.
No gameplay simplification or fallback was introduced.
The bounded audit deliverable is complete, while candidate repair implementation, complete transaction/protection validation, and engine behavior remain unresolved.

## Parent-requested exact reset ownership addendum

The accompanying `2026-10-07_biological_raid_lifetime_caller_map.json` is a static caller map, not a generator or new framework.
Its five raid owner entries give the exact declaration placement and defaults.
The lists below are minimal residual reset fields for the current valid raid caller paths, assuming the parent separately repairs dispatcher-owned retaliation status and the previously listed adapter outputs.
They omit fields unconditionally set directly by that owner before dispatch, and omit profile/final-value fields already initialized by the dispatcher.
They retain fields assigned only conditionally, because the other path needs the reset default.
Defaults use existing constant tokens and introduce no tuning.

The common residual set is:

```text
bio_seed_batch_condemnation_proof = constant:bio_lifecycle_proof.missing
bio_seed_intensity_override = constant:bio_lifecycle_math.zero
bio_seed_exposed_share_override = constant:bio_lifecycle_math.zero
bio_seed_evidence_override = constant:bio_lifecycle_math.zero
bio_seed_condemnation_override = constant:bio_lifecycle_math.zero
```

| Exact reset owner | Reset site and scope | Minimal residual fields |
| --- | --- | --- |
| `bio_battlefield_dispatch_primary_release_internal` | `biological_battlefield_effects.txt:266`, actor country, before reset | Common set, `bio_seed_concealment = constant:bio_lifecycle_math.zero`, `bio_seed_force_detection_on_activation = constant:bio_lifecycle_proof.missing`. The occupied-friendly-state exposed-share override remains conditional. |
| `bio_battlefield_attempt_friendly_blowback_internal` | Same file:370, inside `if/event_target:bio_battlefield_friendly_state`, before reset | `bio_seed_batch_condemnation_proof = constant:bio_lifecycle_proof.missing`, `bio_seed_payload_debit_proof = constant:bio_lifecycle_proof.missing`, `bio_seed_use_history_proof = constant:bio_lifecycle_proof.missing`, `bio_seed_payload_required = constant:bio_lifecycle_math.zero`, `bio_seed_payload_consumed = constant:bio_lifecycle_math.zero`, `bio_seed_condemnation_override = constant:bio_lifecycle_math.zero`, `bio_seed_concealment = constant:bio_lifecycle_math.zero`, `bio_seed_weaponization_mult = constant:bio_lifecycle_math.one`, `bio_seed_force_detection_on_activation = constant:bio_lifecycle_proof.missing`. Intensity/share/evidence overrides are directly supplied afterward. |
| `bio_strategic_raid_dispatch_target_release_internal` | `biological_raid_effects.txt:332`, actor country, before reset | Common set, `bio_seed_force_detection_on_activation = constant:bio_lifecycle_proof.missing`. Every authorized target-release outcome sets result and concealment, while partial release does not set evidence override and only detected seed sets force-detection. |
| `bio_strategic_raid_dispatch_attacker_accident_internal` | Same file:378, actor country, before reset | Common set, `bio_seed_use_history_proof = constant:bio_lifecycle_proof.missing`, `bio_seed_concealment = constant:bio_lifecycle_math.zero`. Accident result, weaponization, payload and force-detection are directly supplied afterward. |
| `bio_sabotage_raid_dispatch_release` | `biological_sabotage_raid_effects.txt:60`, inside `event_target:bio_sabotage_state_target`, before reset | Common set, `bio_seed_force_detection_on_activation = constant:bio_lifecycle_proof.missing`. Result, concealment, payload, weaponization and deliberate-use proof are directly supplied afterward. |

All five dispatch sites additionally need `bio_seed_dispatch_status = constant:bio_lifecycle_proof.missing` immediately before `bio_lifecycle_dispatch_seed`.
This is a dispatcher output declaration, not a reset output, because the reset helper does not declare it.
The adapter's existing status declaration does not own this nested seed receipt.
The shared dispatcher separately needs caller-owned `bio_seed_retaliation_status = constant:cbrn_retaliation_status.none` before the biological classification helper.
Do not add this to every adapter merely to forward an output consumed only within the dispatcher.
For direct public target-adapter invocations outside the valid resolver route, result/agent/route defaults would need a separate contract review, which is outside this bounded native path.

### Complete shared-consumer inventory

A production `.txt` search outside docs, wiki, tools and agent definitions found 16 direct reset calls and 16 direct dispatch calls.
All are paired in the same owner helper, with no additional direct event, history, GUI, map, or decision-file call sites.
Existing parser traversal resolved their exact top-level owners without expanding their unrelated mechanics.
The five raid owners are listed above.
All eleven other consumers are:

| File under `common/scripted_effects/` | Exact owner | Reset line | Dispatch line and nested path |
| --- | --- | --- | --- |
| `012_africa_disease_effects.txt` | `africa_disease_dispatch_seed_from_current_state` | 35 | 49, current state. |
| Same file | `africa_disease_dispatch_laboratory_accident` | 114 | 119, `if/random_controlled_state`. |
| `016_brilliant_scientist_biological_operations_effects.txt` | `brilliant_scientist_dispatch_standard_biological_release` | 53 | 97, `var:brilliant_scientist_biological_release_target_state`. |
| `032_missiles_operations_effects.txt` | `missiles_dispatch_biological_payload` | 4448 | 4463, `if/var:missiles_operation_impact_state`. |
| `biological_doomsday_effects.txt` | `bio_doomsday_dispatch_current_agent` | 159 | 175, `for_each_scope_loop/if`. |
| `biological_facility_capture_effects.txt` | `bio_facility_capture_dispatch_accidental_release` | 564 | 593, `if/if`. |
| `biological_field_test_effects.txt` | `bio_field_test_resolve_exact_facility_test` | 42 | 52, `if/if`. |
| `biological_lifecycle_effects.txt` | `bio_lifecycle_seed_selected_spread_target` | 2452 | 2465, `event_target:bio_spread_target_state`. |
| `biological_operation_effects.txt` | `bio_operative_release_dispatch_seed_internal` | 106 | 118, current state. |
| `biological_stockpile_safety_effects.txt` | `bio_stockpile_safety_dispatch_selected_accident` | 654 | 673, `var:bio_stockpile_safety_arsenal_state/if`. |
| `japan_biological_campaign_effects.txt` | `japan_bio_campaign_dispatch_native_release` | 121 | 144, `event_target:japan_bio_campaign_state_target`. |

No consumer coverage or defect claim is made for those unrelated systems, and no declarations are proposed there by this addendum.

### `bio_active_agent` storage and cursor safety

Production assignments to the exact name are all `set_temp_variable`, including lifecycle storage line 463, eight lifecycle event entries, operations, countermeasure helpers, sabotage history, and a diplomacy selection helper.
No production regular/global assignment, clear, `has_variable`, or `var:bio_active_agent` pointer was found.
AST traversal of all relevant parsed source also found no regular-variable mutation containing that selector.
Regular episode records use names such as `bio_agent_[BIO_AGENT]_stage`, `bio_agent_[BIO_AGENT]_actor`, and `bio_agent_[BIO_AGENT]_retaliation_status`, rather than a regular `bio_active_agent` slot.
Thus a caller temporary declaration does not shadow an existing saved variable of this name.

An outer spread or iteration caller can already own this unscoped temporary as its current selector.
Do not reset it to zero at dispatcher entry, because a rejected seed should retain that existing input/cursor.
The safest ownership statement is `set_temp_variable = { bio_active_agent = bio_active_agent }` directly before the store helper, preserving the existing selector and creating zero-valued storage only when none exists.
Alternatively, place `set_temp_variable = { bio_active_agent = bio_seed_agent }` inside the accepted branch immediately before `bio_lifecycle_store_seed_in_current_agent_record`, which immediately performs the same assignment as its first statement.
The latter preserves all rejected-path cursor values and introduces no accepted-path change in selected agent identity.
The declaration must remain after the existing seed validator and must not move or weaken any dispatcher duplicate guard.
No new MCP event or probability calls were made for this addendum.
