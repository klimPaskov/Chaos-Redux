# Event 029 late-outcome gap and integration audit

Disposition: completed read-only source audit, with outstanding account implementation and blocked MCP/runtime evidence.
Acceptance basis: the parent's explicit bounded sidecar request to map the existing specification's Gilded Sovereignty and Bottomless Account requirements, plus the subsequent explicit metric/tuning direction.
Only this report is written.
Core, triggers, decisions, metrics, constants, incident, harm, achievement, maintenance, and aggregate-stage sources remain read-only for this worker.
DecisionAudit owns decision edits and the parent owns metrics, progression, wiring, and final acceptance.
No new design, substitute route, invented reward, new decision, or gameplay simplification is proposed here.

## Source boundary and concurrent changes

The source design is `docs\specs\029_riches_found_specs\029_riches_found_spec_part_4_evolutions.md`, especially Gilded entry lines 369-380 and Bottomless entry lines 1020-1031.
The account contract additionally occupies lines 1033-1081 and 1083-1142, including one active obligation, five bounded payment families, closure, and promise-specific breach.
The parent patched metrics and gates during this audit.
The initial high-legitimacy/low-concession Gilded gate and development/legitimacy/integrity-only Bottomless gate were observed before those patches.
They are not reported as current unresolved gate bodies.
The latest inspected gates use the parent-created authority, receipt, reform, accepted-term, and post-contact inputs described below.
Exact symbol names remain the primary call-site references because concurrent edits move line numbers.

Named inspected gameplay files are under `common\scripted_triggers\029_riches_found_triggers.txt`, `common\scripted_effects\029_riches_found_effects.txt`, `029_riches_found_incident_effects.txt`, `029_riches_found_harm_effects.txt`, `029_riches_found_achievement_effects.txt`, `029_riches_found_maintenance_effects.txt`, and `common\decisions\029_riches_found_decisions.txt`.
The parent's new `common\scripted_effects\029_riches_found_late_outcome_effects.txt` and appended constant groups were read after the parent supplied their scope and tuning.
The aggregate-stage helper was read only to trace the stage-PP input used by the new receipt allocator.
No local event file or Event 004 script was read or edited.

Skills applied are the already-read `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents` contracts.
AGENTS.md was reread.
No skill was changed.

## Gilded entry requirement map

| Specification requirement | Current source evidence | Remaining integration or evidence limit |
| --- | --- | --- |
| Resource Curse active | `riches_found_gilded_sovereignty_gate` requires `riches_found_resource_curse_active` and retains `riches_found_evolution_i_recorded` as history. | Current active/history distinction is implemented in the inspected gate. |
| High development and very low legitimacy | Gate checks development against `riches_found_threshold.mature_development = 80` inclusively and legitimacy below `riches_found_late_outcome.legitimacy_very_low = 20` strictly. | Matches the parent's supplied tuning. No source-only engine execution is claimed. |
| High capture and concession exposure or private-security autonomy | `riches_found_private_or_patronage_dominance` requires capture at least 60 and either exposure or autonomy at least 60. | All three reuse existing threshold constants. Current numeric checks are present. |
| Private or patronage dominance held long enough | Predicate additionally requires one of `riches_found_curse_private_dominance`, `riches_found_private_enclave`, `riches_found_patronage_tolerated`, or `riches_found_curse_corruption_tolerated`. `riches_found_refresh_local_authority_history` tracks `riches_found_private_dominance_since` and publishes `riches_found_private_dominance_prolonged` after 120 days. | Current predicate failure clears the date and prolonged flag. Source proves sampled continuity, not every intervening campaign change. |
| Actual government receipt dependence | Gate requires `riches_found_treasury_depends_on_mine` and equality between `riches_found_receipt_dependence_controller` and the current CONTROLLER. | The parent receipt helper replaces a country-stage label or random `riches_found_budget_dependence` incident with controller-bound calculation. See exact semantics below. |
| No successful recent reform | Gate rejects `riches_found_recent_successful_reform`, derived from `riches_found_successful_reform_date` and a 120-day protection window. | A successful public-settlement producer is wired. Sovereignty-restoration receipt integration remains incomplete at the inspected checkpoint. Starting diversification remains insufficient proof of success. |

The existing private-interests action is `decision_riches_found_curse_private_interests`.
Its accepted removal branch sets private dominance and enclave flags, lowers legitimacy, and raises capture and private-security autonomy.
The existing corruption route sets `riches_found_curse_corruption_tolerated`.
Those provide authority facts but are not, by themselves, elapsed-time receipts.
The new state-held date supplies that missing distinction.

## Parent metric semantics

The new COUNTRY helper is `riches_found_refresh_controller_receipt_dependence`.
It is called from `riches_found_rebuild_controller_aggregate` after country aggregate publication and `force_update_dynamic_modifier`.
Before aggregate caps, the core stores each output-producing mine's marginally weighted PP in `riches_found_mine_weighted_pp_component`, binds `riches_found_mine_contribution_controller`, and stores total raw mine PP in `riches_found_controller_raw_mine_pp`.
The helper allocates the capped economic portion back to mines after removing the once-per-country stage PP term, so raw mine components do not simply bypass the country cap in the dependence numerator.

Let `D` be the current country `political_power_daily`, `A` its published `riches_found_controller_pp_gain`, `R` its raw weighted mine PP, `S` the stage-PP term, and `W_i` one mine's weighted component.
The current authored arithmetic is:

```text
nonmine = max(D - A, 0.50)
denominator = max(nonmine + A, 0.50)
economic_receipts = clamp(A - S, 0, R)
allocation_factor = economic_receipts / R, or zero when R is not positive
mine_receipts_i = W_i * allocation_factor
share_i = mine_receipts_i / denominator, or zero when the mine provides no output
```

The parent's explicit instruction stated the first floor on non-mine PP.
The current helper also floors the final denominator at 0.50.
That additional floor differs from the stated expression when the mine aggregate is negative.
For example, non-mine PP floored to 0.50 and aggregate PP of -0.04 produce a stated denominator of 0.46, while the helper uses 0.50.
This is recorded as an exact implementation/tuning distinction for the parent, without changing it or selecting an alternative.

The cap allocator reads temporary `riches_found_stage_political_power` from the separate aggregate-stage applier.
That temporary is initialized inside `riches_found_apply_aggregate_stage_terms`, and the inspected parent aggregate does not predefine it before that call.
The offline Data structures reference at lines 436-442 warns that temporaries created within a scripted effect may not remain available outside it, while caller-predefined temporaries carry into and back from the effect.
The allocator therefore needs an explicit caller-lifetime or public-output contract for this field.
This is an engine-evidence and integration gap, not a claimed observed engine failure.
The installed getter's existence and the current formula do not prove the same-tick daily-PP refresh after the DM update.

Exact date and threshold behavior in the current source:

- A share at least 0.05 starts or retains `riches_found_receipt_reliance_since`, clears the exit clock, and sets `riches_found_treasury_depends_on_mine` when 90 days have elapsed.
- A share below 0.05 clears the entry clock.
- A share strictly below 0.03 starts or retains `riches_found_receipt_exit_since`, and clears established dependence after 90 days.
- A share from 0.03 through values below 0.05 resets both qualifying clocks as applicable while preserving an already-established dependence flag.
- Controller mismatch rebinds `riches_found_receipt_dependence_controller`, clears the old dependence flag, and clears both the reliance and exit clocks.
- That mismatch branch does not clear `riches_found_private_dominance_since`.

Thus the transfer code resets both receipt clocks and the old actor's dependence, rather than only the reliance clock literally.
Local authority history persists through transfer if its current local predicate remains true.
Terminal predicate failure or loss of the actual dominance conditions clears the local authority clock.
The parent's instruction is the acceptance basis for controller-specific finance and state-specific authority continuity.

The STATE helpers are `riches_found_refresh_local_authority_history` and `riches_found_record_successful_reform`.
The protection flag is true while current date is strictly less than reform date plus 120 days.
It expires on the exact 120-day boundary at the next refresh.
The success recorder resets the dominance clock and prolonged flag when the successful outcome is recorded.
Subsequent unresolved dominance can start a new local clock.

The existing controller pulse is sampled at its configured cadence.
Dates avoid callback-count accumulation, but source inspection does not prove uninterrupted conditions between samples.
In the inspected maintenance helper, late-gate clearing/queueing occurs before the final aggregate rebuild that refreshes these receipt and authority records.
Consequently a qualifying or expiring metric can be reflected in gate scheduling on a later pulse, and a queued callback can read the previously refreshed flag.
The parent should retain that call-order and sampling limitation in timing validation rather than treat the hold duration as the exact automatic delivery time.
No alternative cadence or global scan is prescribed by this audit.

## Successful reform receipt integration

| Existing hook or flag | What it proves | Required existing call site |
| --- | --- | --- |
| `riches_found_curse_diversification_started` from `decision_riches_found_curse_stabilization_diversification.remove_effect` | Diversification route/start marker. The action also starts a public-settlement mission. | Must not itself call the successful-reform recorder or satisfy a completed-reform/recency gate. |
| `mission_riches_found_public_settlement.complete_effect` | This mission's successful branch, with public project, paid share, and order/legitimacy requirements in its availability path. | It calls `riches_found_complete_mission` while the mission kind and active receipt still exist. |
| New conditional branch in `riches_found_complete_mission` | Active mission of kind `public_settlement` with `riches_found_public_project_complete` and `riches_found_public_revenue_share_paid`. | Calls `riches_found_record_successful_reform` before clearing the live mission receipt. Current source wiring is present. |
| Public-settlement partial/failure/cancel paths | Partial or failed work, not successful reform. | No success recorder is present in the inspected branches. Preserve that distinction. |
| `riches_found_record_achievement_gilded_reform` | Historical Gilded reform completion for achievement tracking, after Gilded already existed. | Current four restoration actions invoke it, but the inspected body does not also invoke `riches_found_record_successful_reform`. Bridge only their genuinely successful outcome path to the parent-owned recency receipt. |

The four existing sovereignty-restoration actions are `decision_riches_found_gilded_revoke_charter`, `decision_riches_found_gilded_buy_back_district`, `decision_riches_found_gilded_share_sovereignty`, and `decision_riches_found_gilded_recognize_board`.
Their successful state branches set corresponding Gilded result flags and call the achievement helper.
The achievement verification deadline in `riches_found_refresh_state_achievement_timers` is a post-Gilded achievement hold.
It does not supply the missing pre-entry successful-reform recency receipt.
Generic mission-success counts also do not identify which reform succeeded or when.

## Bottomless entry requirement map

| Specification requirement | Current gate and existing source facts | Missing normal producer or integration |
| --- | --- | --- |
| Demons active | Current gate requires `riches_found_demons_beneath_mine_active` and recorded Evolution III. | Active/history distinction is implemented. |
| Deliberate agreement or repeated exploitation after clear contact | Gate accepts `riches_found_demons_agreement`, or controlled exploitation with `riches_found_post_contact_excavation` at least `repeated_post_contact_excavation = 20`. Agreement and controlled-exploitation actions exist. | `post_contact_excavation` has no setter or increment in the inspected source set. No producer establishes what the counted units are or binds their accumulation to clear contact. Controlled exploitation is currently a one-time action flag, not a repeated-contact receipt. |
| Very high supernatural pressure and high extraction | Gate checks supernatural pressure against the new value 85 and extraction against the existing severe threshold 80. | Current numeric requirements are implemented. |
| Controller receipt dependence | Gate requires the state dependence flag and current-controller binding from the parent receipt helper. | See metric arithmetic, lifetime, cadence, and transfer limits above. |
| At least one accepted term | Gate requires `riches_found_accepted_account_terms`. | No writer appears in the inspected gate/action/effect surfaces. `decision_riches_found_demons_make_agreement` currently sets only the generic agreement flag and value deltas. The explicit acceptance receipt is unproduced at this checkpoint. |

The accepted-term and post-contact fields are current gate consumers, not implemented receipt producers.
Normal Bottomless entry cannot be claimed complete merely because those field names are present in a trigger.
The deliberate agreement action is a viable existing acceptance boundary for the owner to inspect, but this report does not choose or invent its terms.
The existing controlled-exploitation action and genuine later extraction outcomes are the existing boundaries relevant to the repeated-after-contact branch.
Pressure growth alone does not establish what promise was accepted or that a particular contact was clear.

## Complete account mechanism still uncovered

The current capability refresh derives `riches_found_account_active` from Bottomless history and absence of `riches_found_account_closed`.
It derives `riches_found_account_material_payment_possible` from that flag and a transport route.
These two booleans do not describe an agreement stage, one active obligation, its fulfillment condition or any promised due date, its family, its responsible actor, its fulfillment receipt, or its promised benefit.
No such live obligation record, single-slot admission guard, fulfillment progression, or family-specific breach dispatcher was found in the inspected source set.
The existing material, authority, and predatory actions are independently offered and each has a one-time route flag.
That bounds those clicks but does not serialize or fulfill one active obligation at a time.

| Required payment family | Existing reusable hook | Exact missing coverage |
| --- | --- | --- |
| Material tribute | `decision_riches_found_account_pay_material` pays existing resources, sets `riches_found_account_material_paid`, and lowers supernatural/extraction pressure. | No accepted material obligation, agreed amount and fulfillment condition, matching fulfillment receipt, next-stage progression, or promise-specific benefit/breach link. Its permanent one-time flag cannot represent later obligations by itself. |
| Political authority | `decision_riches_found_account_spend_authority` debits PP/command power/manpower, sets `riches_found_account_authority_spent`, and lowers pressure/legitimacy. | No obligation-specific staged authority receipt or corresponding payment-to-benefit/breach progression. No safe official/role consumer was demonstrated, and the spec permits that consumer only when valid. |
| Public trust | Authority and predatory actions already lower local revenue legitimacy. Existing dividend, public-settlement, disclosure, and Resource Curse state can expose trust effects. | A generic legitimacy penalty is not an accepted public-trust promise. No live trust payment family or matching broken-dividend/secrecy/stability obligation fulfillment/breach mapping exists in the inspected account surfaces. |
| Territorial or industrial sacrifice | Existing state development, transport, physical-damage, closure, and contribution helpers provide exact-state effect surfaces. | No account-owned industrial/territorial sacrifice action/receipt, accepted sacrifice obligation, bounded target proof, or corresponding account benefit/progression was found. Reusing a generic incident cannot establish a promised sacrifice. |
| Human sacrifice through a scripted crisis choice | `decision_riches_found_account_predatory_prosperity` invokes `riches_found_record_predatory_prosperity_harm`. That wrapper is one-time, state-bound, and uses the exact population-loss API, Deaths reason, actual applied amount, and public Condemnation. | Finite harm infrastructure exists, but no typed human obligation or matching acceptance/fulfillment/progression is present. Reviewed action eligibility uses an active account, without a distinct current severe/high-chaos payment proof. The named people-at-risk presentation is outside this source-only audit and remains unverified. Unrelated deaths are not a valid fulfillment source. |

The harm wrapper currently requests `riches_found_harm.predatory_prosperity_civilian_deaths = 100`, records actual applied losses under `chaos_meter_deaths_reason.resource_field_incident`, and identifies the scoped state OWNER as victim and current CONTROLLER as the public responsible actor.
Its receipt is `riches_found_predatory_prosperity_harm_recorded`.
That finite one-time source is reusable evidence infrastructure, not permission to debit general combat or unrelated civilian deaths as account currency.
The other harm wrappers retain their own causes and must not silently become interchangeable payments.

### Breach must follow the accepted promise

`riches_found_account_breach_imminent` is read by the close-account AI urgency and the account-closure achievement disqualifier.
No setter or resolution producer was found in the inspected source set.
The existing `riches_found_run_contract_outcome_pool` includes `contract_breach_pressure`, but its prerequisite is `riches_found_contract_dispute` and its effects concern foreign leverage, legitimacy, and sanctions.
That is a foreign concession incident, not a typed Bottomless obligation breach.
The supernatural pool supplies Event 029 phenomena, pressure, and bounded incident harm, without reading an agreed account family or promise.
Neither pool can substitute for the requirement at spec line 1133 that the result follows the promise broken.

Required integration is a traceable path from the one stored obligation and its accepted family through fulfillment or breach to the relevant existing exact-state effect, account benefit change, report, and next obligation.
The report does not choose which breach consequence belongs to which promise.
The full spec's listed consequence possibilities must remain available to the parent rather than be collapsed into one pressure delta or generic random incident.

## Required existing source call sites

| Source owner surface | Existing identifiers and boundary | Required integration fact |
| --- | --- | --- |
| Trigger owner | `riches_found_gilded_sovereignty_gate`, `riches_found_bottomless_account_gate`, `riches_found_private_or_patronage_dominance` | Current metric requirements are present. All receipt consumers must have real producer paths and current actor/state association. |
| Core aggregate | `riches_found_rebuild_controller_aggregate`, `riches_found_refresh_controller_receipt_dependence` | Raw/weighted PP and actor binding are published, then capped allocation and date refresh run after the DM update. Establish stage-term lifetime and getter timing evidence. |
| Core action refresh | `riches_found_refresh_mine_state`, `riches_found_reconcile_controller`, `riches_found_finish_incident` through its owning pulse | Authority/finance facts must be refreshed when their existing actions or incidents change the prerequisites. Preserve bounded controller ownership and state continuity. |
| Successful reform | `riches_found_complete_mission`, public-settlement success, and `riches_found_record_achievement_gilded_reform` from the four restoration actions | Record actual success and its date. Do not lend diversification-start, partial completion, or generic success counts the same meaning. |
| Late entry | `riches_found_enter_gilded_sovereignty`, `riches_found_enter_bottomless_account` | Both already recheck their gate, set history/date, queue report, and refresh the aggregate. Bottomless entry must initialize the actual account agreement/obligation contract once, rather than only a history flag. |
| Maintenance | `riches_found_run_maintenance_pulse`, pending flags and `.904/.905` queues | Preserve the existing queues and gate rechecks. Advance due account work and typed fulfillment/breach within this existing bounded state pass when the parent implements that lifecycle. |
| Existing decision boundaries | Make agreement, controlled exploitation, pay material, spend authority, predatory prosperity, bind terms, close account | DecisionAudit owns edits. Successful outcome branches must call the matching owner receipt/lifecycle API once, with their actual target and paid result. Current static flags remain history, not one active live obligation record. |
| Incident evidence | `riches_found_finish_incident`, `riches_found_run_supernatural_incident_pool`, `riches_found_run_contract_outcome_pool` | Keep foreign contracts distinct. Genuine contact/after-contact outcomes need explicit proof when used by the account branch. Random incident memory does not identify a promise. |
| Harm owner | `riches_found_record_predatory_prosperity_harm`, `riches_found_apply_harm_record` | Preserve finite idempotent exact-state harm and actual Deaths/Condemnation receipt. Do not treat unrelated harm as payment. |
| Transfer/cleanup | `riches_found_handle_state_control_change`, `riches_found_handle_owner_change`, `riches_found_handle_removed_actor`, `riches_found_clear_mine_cleanup`, `riches_found_permanently_seal_mine` | Dependence is current-controller bound and authority is state-bound. A future live obligation must have an explicit migration/cleanup disposition while preserving the spec's active-account transfer endpoint. Existing contract/mission cleanup does not yet own such an account record. |
| Account closure and achievement | Close/bind decision outcomes, `riches_found_record_achievement_account_closure`, `riches_found_refresh_state_achievement_timers` | Distinguish closure initiation, surviving breach exposure, successful binding/sealing, benefit removal, and verified containment. Existing historical closure flags are not a completed obligation lifecycle. |

No new helper name or storage schema is prescribed for the missing account lifecycle.
The report does not require every obligation to have a timer, and any due-date requirement must come from the particular accepted promise.
The parent chooses local implementation identifiers while preserving existing route IDs and the source specification's semantics.
The five families, accepted terms, single active obligation, and promise-specific breach are source requirements rather than optional expansion proposals.

## Evidence and validation limits

The installed `documentation\dynamic_variables_documentation.md:746-749` lists `political_power_daily` as the country's daily political-power increase getter.
Its SHA-256 is `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda`.
The local source was read directly after the parent cited it.
The new exact-token `hoi4.reference_search` for that getter returned `timed out awaiting tools/call after 600s`.
The offline Data structures temporal-variable reference was also read directly at lines 436-442, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
These references establish supported source concepts and cautions, not executed getter or temporary lifetime behavior.

Both `hoi4.event_inspect` calls for `.904` and `.905` used explicit workspace `mod_chaos_redux_ea3b2d67c2c0`, minimum depth 1, one node, one edge, and no helper expansion.
Both returned `tool call failed`, caused by `timed out awaiting tools/call after 600s`.
Those requests already used the smallest supported trace bounds, so no smaller valid request or identical retry is invented.
`hoi4.probability_inspect` for the incident random-list source also returned the same 600-second timeout.
A narrower retry specifies that source file plus identifier `riches_found_run_supernatural_incident_pool` under the same explicit workspace and adapter.
That retry remains pending at this report checkpoint.
No source revision, graph, probability result, scenario, or artifact URI was returned by these failed/pending calls.
No native job, helper-expansion mode, or negotiated task capability was used.

The existing AI auditor `01a10108-e81d-7cc2-b58a-041ccfd61783` was notified of the new gate metrics, incomplete account producers, and the inspection failures.
The auditor and parent retain timing, eligibility, weighted-incident, and same-scenario comparison evidence.
No branch probability, cumulative entry time, or promise-breach distribution is inferred from source alone.

Checkpoint source hashes:

| Source | SHA-256 |
| --- | --- |
| Part 4 specification | `564bf46ce0b14b93e21b8a7cee32935f597ea4095e5136f689371a25dbf778bf` |
| Triggers after parent gate update | `d0460c4b1cb6063a9f5a0700196a6ad23a5cbbf8e20e67763906a4bb22a5d1b5` |
| Core at checkpoint | `b9b5f0241d38dd7174d880b52bbff8e96c537788f0b271c38ec3402d9276db9d` |
| Parent late-outcome helper at checkpoint | `a83bbd69925028a3d095f555456121b853fd937a6d2df803464043b153d7b83c` |
| Maintenance helper | `d8a77199202dc31127d798e6090f7b19b517e03e578d1e28231a1f5c84fe2b8a` |
| Incident effects | `2637eea37acac42c8105cc1e881589752fe33ddea6f08779cda7cdc095dbd5ec` |
| Harm effects | `d0046e3a9c0f7d1b5f118e1571fb61ff0697683c647c7ceac492b3215790fc60` |
| Achievement effects | `e0a1617b7e75aab77bfa3748aaf99665ea3e56b3282d2f40a0788bcec30f3618` |
| Decision file at checkpoint | `b46caeab5fd0392b9d3fe2fe5dbc4cae46b007b46bcd662536573ac84633e0e6` |

The checkpoint hashes bind observations, not an immutable final implementation.
Parent and DecisionAudit work continues concurrently.
Meaningful checks were targeted requirement-to-gate comparisons, producer/consumer searches over the named Event 029 surfaces, full reads of the new metric helper and harm contract, and exact existing action/mission outcome tracing.
No source file was patched, no unrelated event was read, and no HOI4 process was launched.
The source audit is complete, but the complete account mechanic, MCP domain evidence, temporary lifetime, same-tick getter behavior, and campaign validation remain unresolved.
