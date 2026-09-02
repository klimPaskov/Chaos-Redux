# Event 016 elapsed-day receipt repair

Date: 2026-09-02.
Status: owner-reviewed source repair with identical-fixture probability comparison; event-helper and native runtime acceptance remain incomplete.

## Source boundary and disposition

The before boundary is commit `5f31c83ce66f1c00fbf21f7a120f7ba2d1f25d55` and the raw source hashes retained in `016_final_remaining_timer_arithmetic_audit_2026-09-02.md`.
The accepted design is recorded in `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md`, committed separately as `d52bd96fd2`.
The audit's DHR compact expiry and Black Plague devastation findings are implemented; the evolution next-check metadata finding is implemented without changing its live callback timer.
The Black Plague activation/scheduler bridge is a separate unresolved lifecycle review and is not claimed fixed by this receipt patch.

## Changed runtime surfaces

- `common/scripted_effects/016_dhrondan_country_effects.txt`: write, clear, reconcile, and remaining-delay scheduling use `dhrondan_diplomatic_offer_expiry_num_days` on `global.num_days`.
- `common/scripted_triggers/016_dhrondan_country_triggers.txt`: actual response commitment checks that elapsed deadline.
- `events/016_dhrondan_country_events.txt`: `.49` delivery and `.52` watchdog use the same elapsed deadline.
- `common/scripted_effects/020_black_plague_effects.txt`: the stable public helper `black_plague_set_next_devastation_date` writes `black_plague_next_devastation_num_days`; phase-dependent intervals and pulse settlement remain unchanged.
- `common/scripted_effects/016_brilliant_scientist_evolution_effects.txt`: the informational field is `brilliant_scientist_evolution_next_check_num_days`; `.90` still schedules with `brilliant_scientist_evolution_scheduled_delay_days`.

The corresponding DHR, biological-operations, and evolution system documents describe the current receipts.
No cost, outcome weight, evolution count, native timeout duration, actor/recipient ownership rule, or permanent history was changed.

## Meaningful source checks

The unchanged fixture `E016_FINAL_REMAINING_TIMER_PROBABILITY_2026_09_02.scenarios.json` supplies thirteen cases with explicit start and intended due-day inputs.
Direct arithmetic reproduced every intended deadline as start plus thirteen response days plus one grace day.
The day-13 cases retain one day; day-14 cases have zero remaining days and fail the strict future-deadline predicate; day-15 remains expired.
The same results hold for the named January/February and December/January boundary cases.
This is a check of the time predicate only, not a claim that consumed, wrong-actor, or destroyed-recipient offers are otherwise eligible.
Their separate identity, existence, and response guards remain unchanged and require the full event/probability evidence.

Source review confirms the Black Plague branch still selects exactly the existing rat-controlled, collapsed, or severe interval, applies at most one devastation in the current pulse, and then advances the receipt through the same helper.
Source review confirms the evolution field has no live reader; the active scheduling delay and `.90` dispatch are identical to the before boundary.

## MCP evidence and remaining limits

The read-only auditor completed the identical-fixture DHR inspection/evaluation/comparison in `016_final_remaining_timer_probability_2026-09-02.md`.
The retained fourteen-scenario fixture SHA-256 is `B9D58CC5CEA5711572DABFBD257DE861C1C56EB7A27CA6F21F5E6664BFC1F3C7`.
Comparison `probability-9d161494020a35561f9bf10d` retained scenario hash `1fed22d9f63e8ba99020db7dd22b6671aaa0f75cbd7e33e2cd647c676a4474d1` and reported zero changes across 42 candidate rows, with twelve aggregate unresolved items and eighteen diagnostics.
Both sides use current-workspace helpers, and scoped validity/opinion relations remain unresolved, so this is not proof of a normalized response probability or helper-isolated timer execution.
Parent review confirmed the exact three current DHR hashes match that handoff and that both option-weight blocks and native timeout values are unchanged.

The parent also inspected `.49` and rendered its options at focused revision `efbe0ca7016c4e2e981367846826869ed2579ba82e64a7e2438481b73d5354e1`.
The trace artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ea3279636ef5375e6270e7a334bcc02b9dd01d0b0446330d2787970dcd7d8158/dda9dd76a0c02c91935723a0cb70e7da3d929388f92f671d685b9c1964c5d34d/event-trace-efbe0ca7016c.json`.
The inspected options PNG is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/88001a6c8ff2b6a0fe806b917e24b5ed36266cf6cadcdc7f4e417324cc69942e/8e09dd6d7ce09377ab508ee9201cc9fa363e89aba9c0d37073b86a6f8cf10df3/event-options-efbe0ca7016c.png`.
It contains twelve selected nodes and the existing three response options, but the focused catalog has zero indexed helpers and unresolved helper edges.
An initial timing view selected zero timing nodes because the relevant delay is inside deferred helpers; it provides no timer acceptance evidence.
The requested event comparison from retained revision `d8c9140e69ae6d53f2fb77284bb37300a75d320975ad211d21933a46986988cf` to the current revision returned `EVENT_REVISION_NOT_CACHED`, validation false, and no artifacts.
That unavailable comparison remains a recorded MCP blocker rather than a passing source substitute.
Actual popup ordering and shared callback execution are not established by these arithmetic checks.
No game was launched and no logs were searched or requested.
This handoff does not claim Event 016 completion or live acceptance.
