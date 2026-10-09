# Private Event016 Paleogenetics paired Deployment API

Implemented core only, 2026-10-08; parent integration review pending.
Authority: `docs/plans/016_brilliant_scientist_plans/016_private_paleogenetics_deployment_acceptance_2026-10-08.md`.
Staffing, transport and breeding are accepted and queued after this pair, not implemented by these helpers.
No new operational grant, KRG state, native timer, periodic hook, category, asset or unit is introduced.

## Scope and callers

All effect and COUNTRY trigger names below use prefix `brilliant_scientist_mengele_paleogenetics_`.
Persistent fields/flags use prefix `mengele_event016_paleogenetics_`.
Parent owns existing decisions, public generic dispatch wrappers and default aliases, localisation, cleanup wiring, CXT, audits and commit.
Public begin/cancel/finish wrappers dispatch exact family10/stage3 here and retain their default implementation for every other request.
Core never calls public generic begin recursively or default generic finish.

COUNTRY is the actual payer THIS.
Stored STATE pointers are entered with `var:<field>`; immediate PREV there is the payer, so owned/control checks use PREV, independent of an unrelated outer ROOT.
Native free-selection candidate triggers are STATE APIs with ROOT defined as payer by the source decision.
Selection effects instead check FROM's ownership/control against immediate PREV, so a foreign outer ROOT cannot redirect payment or construction.
No first-class province scope, supply-node reader or fixed state IDs are used.

## Exact interfaces

| Suffix | Scope and input | Result/default and side effects |
|---|---|---|
| `request_is_deployment` | Pure COUNTRY; existing temporary family/stage | Exact family10/stage3 only; no provider/payment mutation |
| `reserve_candidate_is_valid`, `hatchery_candidate_is_valid` | Pure STATE; ROOT payer | Owned/controlled, positive infrastructure, output capacity; hatchery also infrastructure room for later pen and distinct from selected reserve |
| `reserve_selection_is_valid`, `selection_is_valid` | Pure COUNTRY; selected normal scope pointers | Reserve validity or full distinct selected pair/capacity, including future hatchery pen room |
| `serial_can_advance` | Pure COUNTRY; stored serial (missing defaults0) | Non-negative integral serial; temporary modulo scratch only |
| `paid_identity_is_valid` | Pure COUNTRY; explicit action1/family10/stage3, actor, positive integral serial, frozen pair/quantities | Durable identity including after completion; no current capacity or generic-row requirement |
| `pending_is_authenticated` | Pure COUNTRY | Pending + identity + exact positive paid/actual three costs + matching active family9 row/CIC quote; rejects payment/refund faults; does not require live provider |
| `current_pair_is_valid` | Pure COUNTRY | Frozen pair currently owned/controlled with positive infrastructure; delivered components also need total levels at least their recorded post-level; no free-slot test for delivered output |
| `deployment_outputs_are_complete` | Pure COUNTRY | Durable identity, positive matching measured payments, both delivered flags and exact quantity/delta proof; rejects payment/construction faults; survives pending/active-row retirement |
| `recovery_is_ready` | Pure COUNTRY | Authenticated pending, timer inactive, no busy/construction fault, valid provider/Prototype/neutral tech/current pair and at least one undelivered component with capacity; no cost or CIC test |
| `select_reserve`, `select_hatchery` | COUNTRY, input FROMSTATE; parent `choice_is_open` predicate | Free selection normal fields only; changing reserve clears candidate hatchery; no buildings, debit or paid proof |
| `clear_selection` | COUNTRY; parent `choice_is_open` | Clears only candidate fields; never frozen paid proof |
| `begin_deployment` | COUNTRY; temporary family10/stage3 and caller-owned `mengele_event016_paleogenetics_native_entry = 1` | `mengele_event016_stage_started` defaults0; marker consumed0 on every exit; direct-only admission, frozen authority before default debit, then measured aggregate payment authentication |
| `finish_deployment` | COUNTRY; temporary family10/stage3 plus authenticated pending | `mengele_event016_stage_finished` and `mengele_event016_project_output_applied` default0; actual +1 attempts, partial retention or one full history/availability/modifier/incident settlement |
| `cancel_deployment` | COUNTRY; temporary family10/stage3 and owned pending identity | `mengele_event016_stage_cancelled` defaults0; retires timer, no-attempt authenticated refund via default alias only; partial/fault proof remains |
| `recover_deployment` | COUNTRY; ready matching pending authority | Owns finish/output result temps, seeds exact family/stage and calls own finish; remaining construction only; no new payment/CIC/timer |
| `attempt_reserve_construction`, `attempt_hatchery_construction` | Internal COUNTRY literal wrappers | Require authenticated paid proof, busy owner, valid provider/predecessor/pair and no prior attempt/delivery; native STATE pre/post measured proof only |

Before invoking any API, the caller must create each temporary output it consumes afterward.
At each nested boundary the consuming helper creates its own output storage; newly created helper-only temporaries may be discarded on return.
Inputs family/stage and native marker are caller-owned and consumed/cleared as documented.
The outer caller must preinitialize `mengele_event016_stage_started`, `mengele_event016_stage_finished`, `mengele_event016_stage_cancelled` and/or `mengele_event016_project_output_applied` as appropriate.
Only the named result for that API is meaningful; begin does not promise fresh finish/cancel values.
Parent public wrappers clear selectors on every exit; core cancel/finish also clear them idempotently.
Do not qualify temporary variables with ROOT/PREV.

## Persistent fields and flags

Candidates: `selected_reserve`, `selected_hatchery`.
Frozen identity: `deployment_actor`, `deployment_action = 1`, `deployment_family = 10`, `deployment_stage = 3`, positive integral `deployment_serial`, `paid_reserve`, `paid_hatchery`.
Frozen quantities: `reserve_quantity = 1`, `hatchery_quantity = 1`.
Quote/measurement: `paid_pp`, `paid_support`, `paid_fuel`; `actual_pp`, `actual_support`, `actual_fuel`.
Refund measurement: `refunded_pp`, `refunded_support`, `refunded_fuel`.
For each component: `reserve_pre/post/delta`, `hatchery_pre/post/delta`.
Post-levels remain durable after successful close for later current undamaged-capacity qualification.
They do not establish unique building identity.

Flags: `deployment_pending`, `deployment_timer_active`, `deployment_busy`; `reserve_attempted`, `hatchery_attempted`; `reserve_delivered`, `hatchery_delivered`; `payment_unverified`, `construction_unverified`, `refund_unverified`.
Parent recovery visibility may show pending plus valid identity even when a fault defeats authentication.
Availability must use `recovery_is_ready`; fault visibility is not permission to retry.
The generic aligned array index9 and its positive direct costs remain paid authority until full construction or verified no-output cancellation.
No new private generic family entry is allowed while pending.

## Lifecycle and economics

Price and timer remain in existing authoritative tables: 130 PP,975 aggregate support,1,500 fuel,CIC4,480 days.
The new schema-first constant category contains structural zero/one, quantity1, index9 and fuel conversion1000 only; it does not duplicate the stage price or timer.
Native availability owns four free CIC.
Entry consumes the source-bound marker and rechecks direct resources/provider/predecessor/pair before persistent mutation.
It freezes receipt identity/pair/quantities and nominal three costs before `brilliant_scientist_mengele_begin_project_stage_default`, then compares aggregate PP/support/fuel before/after with frozen quotes and the generic receipt.
Bare entry, duplicate entry, malformed serial and preflight rejection cannot debit or overwrite paid state.

Finish revalidates operational entitlement `brilliant_scientist_paleogenetic_formations_tech`.
Undelivered component capacity is checked immediately before its actual attempt.
A successful measured delta1 sets delivered; external construction never satisfies a component.
A capacity-blocked component has not attempted output and may recover freely after capacity returns.
An attempted delta other than exactly1 is quarantined: its before/post/delta and attempted flag persist, no blind full refund or retry.
This covers ambiguous zero, fractional/extra output and interrupted acknowledgment conservatively.

On both proven increments, publish exact private completion and success outputs before generic row retirement.
Restore modifiers/availability through `brilliant_scientist_mengele_reconcile_project_availability`, then force native dynamic-modifier update and invoke the existing conventional-incident dispatcher once with family10/stage3 still intact.
Its current family gate does not select a Paleogenetics weighted incident; this core does not invent a new one.
Clear generic active row only after this successful physical proof; preserve frozen actor/pair/actual costs/attempt proof afterward.
No redundant neutral grant, KRG rebuild or KRG history helper is called.

Cancellation may refund when provider/Prototype eligibility is lost, provided original actor and exact payment are authenticated and **neither component was attempted or delivered**.
Requiring a live provider for that refund would strand the existing provider-loss caller.
Clear pending authority/busy-guard reentry before default cancellation, then measure aggregate credits.
Repeated cancel cannot replay credits.
If default refund is unverified, retain pending fault, original payments and observed credits; the default may already have retired its generic row.
No automatic second credit or fake success is provided.
Remaining debt is `actual_* - refunded_*`; parent recovery must verify the original obligation before any future exact retry.
`stage_cancelled = 1` on retained partial/fault cancellation means the native timer was retired, not that the financial/output receipt was closed.
Provider/site loss preserves delivered buildings and neutral tech and suspends completion/recovery until qualification returns.

## Usage

In native complete_effect, parent creates native-entry temp1 and caller result storage, sets existing family10/stage3 inputs and calls public generic begin.
On native expiry/cancel, parent sets exact selectors and initializes consumed result temps before calling public generic finish/cancel.
In the phase-exclusive recovery action, parent initializes finished/output temps and calls `recover_deployment` only when `recovery_is_ready`.
Selection uses FROMSTATE and parent-owned free-choice gate.
Parent CXT observers read the documented normal fields/flags without granting content.

## Evidence and remaining limits

Retained driver: `docs/testing/event016_private_paleogenetics_20261008/core_source_tests.py`.
Run from repository root: `python docs/testing/event016_private_paleogenetics_20261008/core_source_tests.py`.
51 actual-source cases pass; `core_results.json` records exact source hashes and explicit stubs.
Actual public wrappers/default quote/debit/refund/receipt and current success restoration/dispatcher bodies execute; defaults are not no-op fixtures.
Two external provider-identity helpers are stubbed; native stockpiles, slots, scope pointers, flags, modifier operations and no-DLC/no-completed-project scenario inputs are modeled.
Temporary call frames discard newly created storage; an explicit cold-frame case proves absent caller-owned output disappears while warm caller-owned output survives.
Decimals are exact fixture arithmetic, not engine fixed-point/overflow proof.

Required syntax evidence is in the consumer report and `core_validation.json`: installed STATE construction, slot/current-level readers, decision scopes and offline parallels.
Additional directly read aggregate stockpile evidence: installed `documentation\\dynamic_variables_documentation.md:557-559`, revision `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda`; offline `paradox_wiki\\Data structures - Hearts of Iron 4 Wiki.md:1615`, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
The whole-file MCP checks have unknown root scopes and unchecked argument blocks; snippet checks recognize native scopes but do not resolve scripted helpers or validate native parameters.
They are partial evidence, not full engine validation.

Aggregate payment/refund does not prove concrete model/producer/design restoration.
Native fuel clipping, delayed stockpile/building recount, effect/acknowledgment interruption, state pointer/control semantics and cancellation/expiry timing remain user-owned engine proof.
The marker proves authorized source entry, not reservation order.
A mutable serial does not isolate stale same-action native callbacks.
No automatic recovery for unverified payment/building/refund faults is claimed.
Parent owns fault text, cleanup retention, frontend/CXT cases, incident lifecycle acceptance, audits and live integration.
No simplification to the paired increment contract; no claim that the full private Paleogenetics payoff or Event016 is complete.
