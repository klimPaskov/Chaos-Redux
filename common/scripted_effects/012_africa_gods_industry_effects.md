# Event 012 industrial support owner API

Acceptance is the parent-reviewed `docs\plans\012_africa_plans\subagent_handoffs\012_gods_industrial_tribute_design_2026-10-08.md` and the bounded owner-helper delegation on 2026-10-08, with parent acceptance within the user's full goal recorded as queued in `c7e9565a4391a1a2d85b5e4fa160bcbc53f2929c` and reaffirmed by the October 9 reconciliation delegation.
This package implements the finite one-site repair contract.
Its public helpers are integrated through the existing parent-owned gameplay files and `012_africa_gods_industry_integration_effects.txt` / `012_africa_gods_industry_integration_triggers.txt`.
The [parent reconciliation](../../docs/plans/012_africa_plans/subagent_handoffs/012_gods_industry_parent_reconciliation_2026-10-09.md) records the current implemented-source disposition separately from unresolved native and AI evidence.
The industrial quote remains CPP, using `constant:gods_of_africa_transaction.industry_pp_amount` as its existing base and `constant:gods_of_africa_demand_family.industry_repair` as its family.
Neither CPP nor equipment quotes are rounded by these helpers.

## Public effects

All identifiers in the table carry the `gods_of_africa_` prefix.
There are no `$PARAM$` arguments or implicit actor overrides.

| Helper | Scope | Required inputs | Output/default | Side effects | Parent call owner |
|---|---|---|---|---|---|
| `select_industry_site` | HOST country | Existing authorized current African host | Host `industry_selected_site`, `industry_selected_damage`, `industry_candidate_available` flag, otherwise cleared | Replaces proposal only, reserves no slot | Need profile and selector |
| `bind_industry_terms` | ACTOR country | Current demand owner/epoch and open ledger, frozen positive industry quote, untouched original remaining balance, valid selected proposal | Frozen participant terms and one reserved host record, otherwise no binding | Sets Q/D/identity/site, grants no service and moves no CPP | Contract creation after demand epoch and ledger open |
| `pay_industrial_tribute` | ACTOR country | Normal `gods_of_africa_payment_family` and `gods_of_africa_payment_amount` initialized by caller | Normal `payment_delivered`, `payment_received` in measured CPP and `industry_payment_new_days`, each reset to zero at entry | Exact CPP transfer, proportional native time, rollback of measured current transaction on observed failure | Explicit industry branch in transfer owner |
| `review_industry_program` | HOST country | Its canonical host record, no donor existence requirement | Damage observations, completion/unresolved flags, bounded retirement receipt when releasable | Removes completed/expired/invalid scoped effect, never purchases/reinstalls service | Existing owner clock before need selection, optional existing owner cleanup |
| `retire_industry_program` | Original HOST country | Five caller-owned frozen `gods_of_africa_industry_retire_*` temps listed below | Bounded `industry_retired_*` receipt on successful matching removal, otherwise preserves record | Removes old recipient-scoped modifier before clearing the site/record, works after revocation | Host loss/epoch retirement before pointer destruction |
| `finish_industry_contract` | ACTOR country | Its frozen terms matching the reserved host record | Participant `industry_contract_closed`/`industry_terms_retired`, host `industry_program_closed` | Closes finance bindings, preserves earned service, rejects in-flight close | Existing ledger/history terminal owner for full/substitute/default/settlement |
| `clear_industry_terms` | ACTOR country | May run after revocation or donor loss | Clears frozen participant variables and terms-bound flag | Calls financial finish when still matching, preserves host record, cannot clear an owned in-flight binding | Existing demand and participant cleanup |

All omitted field prefixes in tables are relative to `gods_of_africa_`.
These effects do not emit fulfillment, compliance, Wrath, material returns, fabricated capacity, or history credits.
The existing parent receipt consumers determine those outcomes once after a positive measured delivery.
`pay_industrial_tribute` leaves `gods_of_africa_demand_remaining` untouched.
The parent must consume `payment_delivered` exactly once before another original CPP transaction, restoring C + remaining = Q.
Do not debit CPP again in the generic branch or interpret a zero output as success.

## Public triggers

| Trigger | Scope | Proof and temporary behavior |
|---|---|---|
| `gods_of_africa_industry_site_is_eligible` | STATE | Current global host owns, controls and cores the African site with damage at least 0.50 |
| `gods_of_africa_industry_native_service_is_authorized` | Original HOST country source context, ROOT affected STATE | Boolean only, current program owner, frozen program site equals ROOT and ROOT satisfies the secured-site predicate, closed finance and donor loss do not revoke paid service |
| `gods_of_africa_industry_candidate_is_available` | HOST | Authorized current host, nonconsumed project factory floor, physically eligible site, no reserved record except a closed releasable one |
| `gods_of_africa_industry_quote_is_current` | ACTOR | Existing live demand/ledger/epoch predicates plus exact actor, host, origin, generation, epoch, contract, site, Q/D, valid cumulative bounds and C + remaining = Q |
| `gods_of_africa_industry_host_can_receive_payment` | ACTOR | Current quote, secured site and nonconsumed host factory floor for unfinished repair, or the exact paid completion receipt |
| `gods_of_africa_industry_payment_can_execute` | ACTOR | Arbitrary caller-initialized normal payment amount/family, positive p no greater than remaining, legacy CPP reserve, and positive new days or early completion |
| `gods_of_africa_industry_full_payment_can_execute` | ACTOR | Pure temporary quote from `demand_remaining`, never changes normal quote/family |
| `gods_of_africa_industry_partial_payment_can_execute` | ACTOR | Pure temporary quote from the clamped existing `partial_payment_amount`, existing next-partial-day gate, never changes normal quote/family |
| `gods_of_africa_industry_completion_is_proven` | ACTOR | Historical exact terms plus a host-owned positive-to-zero observation during paid native support at the secured frozen site |

The completion trigger proves early physical completion, not full funding by itself.
When closing full original finance the parent still requires independently received cumulative `industry_program_funded = industry_program_quote`, a positive consumed receipt and earned paid-service proof or the early-completion receipt.
A healthy unpaid site or a quote cannot prove completion.
The pure gates preserve the existing industrial payer reserve by comparing actual CPP with p + `constant:gods_of_africa_value.capacity_floor_industry` inclusively, retaining `gods_of_africa_participant_generation_is_current`.
This is the current legacy industry's native capacity branch, recomputed for the transaction's actual p rather than trusting a stale normal capacity quote.
The pre-contract `gods_of_africa_participant_has_capacity_for_family` budget helper remains independent of any active industrial receipt.
Its parent-owned generic body must retain that separation.

The payment gate's forwarded temporary outputs are `gods_of_africa_industry_entitlement` and `gods_of_africa_industry_increment`.
An outer consumer that reads either after calling the trigger must initialize both to zero before the call.
The public payment effect already initializes them before its nested trigger call.
Other scratch temps have no public lifetime guarantee.
All temporary accesses are bare, while durable country/state variables are scoped.

## Record and duration arithmetic

The host's `gods_of_africa_industry_program_` fields are `participant` (country object), `site` (state object), `host_id`, `generation`, `origin_host_id`, `epoch`, `contract_id`, `quote` (Q), `service_days` (D), `funded` (C), `granted_days` (G), `due_day`, `initial_damage`, `last_damage`, `observation_day`, and `last_consumed_receipt`.
The participant's `gods_of_africa_industry_` fields are `host` (country object), `participant_id`, and the same frozen `site`, identity, Q and D fields.
Its proposal is host-owned under `gods_of_africa_industry_selected_site` and `_selected_damage` with the `_candidate_available` flag.
All Boolean state uses flags.
The program flags are `_reserved`, `_inflight`, `_native_applied`, `_site_completed`, `_unresolved`, and `_closed`.
The single record includes both open unpaid reservations and surviving closed paid service.
The representation has one slot, with accepted `maximum_host_programs = 1`, and increasing the constant alone does not create a multi-record registry.

Freeze D = clamp(floor(60 * Q / existing base CPP quote), 30, 120) only after the final quote is fixed.
Positive modulo-and-subtract flooring uses industry-private temporaries and never calls the equipment floor helper.
For a fresh receipt p, compute total entitlement T = floor(D * (C + p) / Q), with p bounded by Q - C.
Clamp a still-incomplete funding total below D, and grant exactly D on exact full funding.
New service E = T - G must be positive for an unfinished site.
Set the provisional due day to max(current day, previous due day) + E.
Install `gods_of_africa_industry_repair_program` on the frozen state with `scope = PREV` (original HOST) and a normal host variable holding due day minus current day.
Never refresh D for a partial payment, and never grant service merely for an extension/substitution/default.
After early paid completion, further exact CPP settles the original remainder without another native timer write or an increase in G.

| Constant in `gods_of_africa_industry` | Value | Meaning |
|---|---:|---|
| repair_speed | 0.50 | Native state civilian-factory repair factor |
| base_service_days | 60 | Existing base-quote entitlement |
| minimum_service_days | 30 | Minimum full entitlement |
| maximum_service_days | 120 | Maximum cumulative service per original contract |
| minimum_site_damage | 0.50 | New-program physical damage threshold |
| available_project_factory_floor | 1 | Nonconsumed host capacity requirement |
| maximum_host_programs | 1 | Accepted single-record contract shape |
| negation_factor | -1 | Arithmetic inversion for debit/reversal without unary variable negation |

The category is schema-first with fixed-point data, and the existing family/base/reserve constants remain with the parent.
The modifier icon is the existing `GFX_modifiers_ETH_state_development` in `interface\countrystateview.gfx`, backed by `gfx/interface/state_modifiers/modifiers_ETH_state_development.dds`.
The parent owns localisation for `gods_of_africa_industry_repair_program`, its description and visible funding/site/time terms.
No new icon asset is required.
The native modifier's `enable` uses `gods_of_africa_industry_native_service_is_authorized` rather than unconditional application, preserving the original host/state binding while allowing closed finance and donor loss.
`common\on_actions\012_africa_gods_industry_on_actions.txt` adds only `on_state_control_changed`: in FROM, the old controller, a reserved program whose site equals FROM.FROM, the changed state, calls `gods_of_africa_review_industry_program` then `gods_of_africa_capture_industry_retirement`.
The callback targets the old controller's one matching record before the next owner tick, with no payment, financial closure, service renewal, world scan or recurring hook.

## Receipt, rollback and callback contract

Before debit, the host publishes `_inflight` and `_txn_*` snapshots of participant, every frozen binding, C/G/due, actual p, donor/host `has_political_power`, new entitlement/increment, and prior native presence.
The measured `_txn_debit` and `_txn_credit` must each equal p exactly.
Current authority/ledger/site/capacity is rechecked after money and before receipt publication.
Presence is checked on the recorded state with the recorded HOST scope before any positive payment output.
Only then update C/G/due/sequence and publish measured CPP.
No normal balance update is performed here, so C + unchanged remaining != Q rejects replay before the parent consumes the first delivery.

On an observed failed transaction the private rollback adds only measured new donor debit, subtracts only measured new host credit, and restores only the old native interval if this transaction provisionally wrote it.
Earlier C/G/due and receipt sequence remain unchanged.
Failed restoration/CPP reversal marks `_unresolved` and retains the transaction snapshot for owner review, rather than claiming recovery.
A foreign tuple is never refunded or used to remove a new program, and sets participant `gods_of_africa_industry_transaction_unresolved` instead.
Current transaction snapshots remain a bounded last-transaction evidence record, not a growing registry.

`retire_industry_program` requires these caller-owned bare temps:

```txt
set_temp_variable = { gods_of_africa_industry_retire_host_id = old_host_id }
set_temp_variable = { gods_of_africa_industry_retire_generation = old_generation }
set_temp_variable = { gods_of_africa_industry_retire_origin_host_id = old_origin_id }
set_temp_variable = { gods_of_africa_industry_retire_epoch = old_epoch }
set_temp_variable = { gods_of_africa_industry_retire_contract_id = old_contract_id }
var:old_host_object = { gods_of_africa_retire_industry_program = yes }
```

`old_*` names illustrate the parent's frozen loss/callback receipt, not new mandatory variables.
For delayed callbacks supply the captured old tuple, never reconstruct it from a replacement record.
Host-local review/reclaim captures its own currently selected record immediately before retirement.
Live permission, current global host and donor existence are deliberately unnecessary for matching loss cleanup.
The original state effect must be absent under its original recipient scope before the current site/participant pointers and reservation are cleared.
Successful retirement retains the frozen fields, final C/G, Q - C, observation data, retirement day, last receipt and closed/completed flags under `gods_of_africa_industry_retired_*` plus `_retirement_recorded`.
This is one bounded retirement receipt that the parent must consume through its durable history/report boundary before allowing another reclamation to overwrite it.
No history/fulfillment callback is invented here.

Open partial terms retain the reservation after their purchased interval expires.
Closed expired/no-service records can be reclaimed through exact retirement.
An early-completed open project awaiting finance is still reserved.
Paid support survives actor cleanup/annexation and normal secured-Africa settlement without requiring active Gods permissions.
Physical recipient loss, replacement, capitulation or epoch mismatch retires the original scoped effect.
Parent hostile loss callbacks must call explicit retirement before revocation/pointer cleanup, while normal settlement must call financial finish/clear rather than hostile retirement.

## Private helper contracts

| Symbol after `gods_of_africa_` | Scope | Inputs/outputs/defaults | Purpose and side effects |
|---|---|---|---|
| `industry_program_site_is_secured` | STATE directly from HOST | PREV is record-owning HOST, Boolean only | Exact site ownership/control/core/Africa proof |
| `industry_program_owner_is_current` | HOST | Current record and host identity, Boolean only | Historical host validity without active-epoch permission gate |
| `industry_program_can_reclaim` | HOST | Closed record, due/completed flags, Boolean only | No release of open partial or unresolved/in-flight records |
| `industry_record_matches_terms` | ACTOR | Frozen participant/host record, Boolean only | Historical binding proof for finance cleanup after revocation |
| `industry_amount_can_execute` | ACTOR | Caller `industry_amount` temp and preinitialized entitlement/increment outputs | Shared pure p/capacity/cumulative-day preflight |
| `industry_retire_tuple_matches` | HOST | Five expected retire temps, Boolean only | Prevent stale loss callbacks from touching a replacement |
| `industry_transaction_is_owned` | ACTOR | In-flight host transaction and unchanged frozen terms/prior totals | Authorizes only current measured rollback |
| `industry_transaction_can_commit` | ACTOR | Owned transaction plus fresh ledger/authority/site/capacity | Authorizes successful native installation/publication |
| `industry_remove_native` | HOST effect | Original frozen site, no defaults | Scoped removal with unresolved evidence on failure, retains pointer |
| `industry_rollback_transaction` | ACTOR effect | Matching published transaction, no defaults | Measured current money/timer reversal with explicit unresolved flag |

Every private helper has local production callers in this package.
Public effect call sites in existing gameplay source remain parent-owned and are implemented in need selection, contract binding, transfer, financial closure, owner review and cleanup.
The transfer owner captures payment-time retirement from `var:gods_of_africa_industry_host` before response capture.
The integration helpers preserve original industrial report data across material substitution with zero new days and publish private terminal history kind 23 independently of financial outcomes.

## Evidence limits and follow-up

Run `node .tools/validation/test_012_gods_industry_helpers.js` from the mod root for actual-source owner scenarios.
The interpreter executes every local helper, scope transition, debit/credit, receipt, removal and rollback branch under conservative helper-temp cleanup.
Its seven external existing authorization predicates and native primitives are explicit fixtures rather than claims about integrated campaign behavior.
`SourceNoNativeProof` is the explicit native-evidence model.
Native presence cannot reveal exact expiry or timer refresh, cannot prove a factory was assigned to this repair queue, and cannot attribute observed damage reduction to the program.
The test includes a counterexample where a failed refresh leaves old presence and therefore passes the only documented presence predicate while actual timer extension remains unproven.
Native numeric CPP precision, exact timer extension/restoration/expiry and real repairs remain user-owned acceptance evidence.
Installed `common\dynamic_modifiers\bba_dynamic_modifiers.txt:1–27,269–279` documents targeted source scope, ROOT state and daily updates.
Offline `Modifiers:123–130` documents `enable`, and offline `On actions:450` plus installed `common\on_actions\00_on_actions.txt:5075–5085` document the control-change scopes.
The [parent reconciliation](../../docs/plans/012_africa_plans/subagent_handoffs/012_gods_industry_parent_reconciliation_2026-10-09.md) retains exact paths and SHA-256 revisions for these read sections.
Actual native daily enable evaluation and callback ordering remain unproved.
The bounded source guard/callback does not establish immediate engine acceptance.
No guessed timer reader, free reinstall, fallback service, or completion waiver substitutes for that evidence.

The [integration review](../../docs/plans/012_africa_plans/subagent_handoffs/012_gods_industry_integration_review_2026-10-09.md) records current caller coverage, 29 helper and 44 integration source cases, source/reference revisions, domain artifacts and validation limits.
The parent retains the supplied ten-file before snapshot and the [completed matched AFTER comparison](../../docs/plans/012_africa_plans/subagent_handoffs/012_gods_industry_probability_2026-10-08.md).
It returned a finite partial result with 619 unresolved traces and establishes no numeric AI equivalence or click probabilities because the preserved decision roots do not freeze helper dependencies.
Current weighted source is unchanged, and the separate F2 adapter audit excluded all five cases with 74 unresolved traces and no score.
The original owner-helper patch did not change weights, probability pools, GUI layouts, existing hooks, workbook, localisation, CXT integration or Git.
That is historical patch scope, not a claim that the later parent integration is absent.
Current parent integration includes the existing CXT extension's inert `gods_of_africa_cxt_industry_fixture_ready` flag and the production receipt/report/cleanup callers.
Final parent review and native/AI evidence remain unresolved, with no simplification or new registry.
