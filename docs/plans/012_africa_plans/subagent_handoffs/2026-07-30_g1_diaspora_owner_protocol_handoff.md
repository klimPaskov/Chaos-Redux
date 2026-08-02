# G1 diaspora owner protocol handoff

## Scope completed

The Event 012 diaspora action readers now have target-owned writers for consent, counterterms, refusal, withdrawal, emergency activation, passage and project capacity, skills, citizenship, representation, and local project ownership. The existing quote, payment, mission, generation, outcome, and generic cleanup kernels remain authoritative.

## Helper map

`africa_diaspora_validate_target_capacity` runs after the existing action-specific validator and returns a temporary capacity result. `africa_diaspora_prepare_target_response` opens a single target event when the target has not supplied standing consent or the fresh emergency state. `africa_diaspora_resume_pending_action` restores the immutable request parameters and re-enters `africa_begin_quoted_action_against_target`, so payment and validation are repeated after the answer.

`africa_diaspora_accept_target_request`, `africa_diaspora_request_counterterms`, `africa_diaspora_refuse_target_request`, `africa_diaspora_offer_counterterms`, and `africa_diaspora_close_host_offer` implement the bounded consent and negotiation chain. `africa_diaspora_open_withdrawal_review`, `africa_diaspora_continue_active_action`, `africa_diaspora_withdraw_active_action`, `africa_diaspora_apply_cancel_cleanup`, and `africa_diaspora_cleanup_action_state` own the active-action withdrawal lifecycle.

`africa_diaspora_apply_current_outcome` dispatches full, partial, and failure result proof after the shared matrix semantics. Full branches record passage waves, skills, housing, volunteers, bonds, protected citizenship/representation, local ownership, and safe emergency evacuation. Partial branches preserve target consent but do not write full achievement proof. Failure branches restore the relevant capacity lane, clear consent where a fresh answer is required, clear emergency state, and write the exact existing Event 012 achievement disqualifiers for catastrophic loss, disaster negligence, discrimination, denied representation, and unresolved corruption.

## Constants and tuning

`common/script_constants/012_africa_diaspora_constants.txt` contains four capacity lanes and maxima, trust deltas, protected ownership, withdrawal review days, and AI response weights. No action cost, duration, risk, or outcome probability was duplicated from the action matrix.

## Event-target and cleanup contract

The short request chain uses regular `africa_diaspora_request_host` and `africa_diaspora_request_target` targets. Resume and cancellation clear both targets after quote restart or closure. Active withdrawal review stores the action generation and is cleared before shared cleanup removes the active record. No global target, recurring world scan, forced relocation, tag creation, or coercive fallback was added.

## Files changed

- `common/script_constants/012_africa_diaspora_constants.txt`
- `common/scripted_triggers/012_africa_diaspora_triggers.txt`
- `common/scripted_effects/012_africa_diaspora_effects.txt`
- `common/scripted_effects/012_africa_action_effects.txt` (narrow begin, record, outcome, and cancel/cleanup hooks)
- `events/012_africa_diaspora_protocol.txt`
- `localisation/english/012_africa_diaspora_protocol_l_english.yml`
- `docs/012_africa_diaspora_owner_protocol.md`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-07-30_g1_diaspora_owner_protocol_handoff.md`

## Validation performed

Brace-depth checks passed for all new files and the modified action-effects file. The touched script set contains no unsupported `<=` or `>=` operators. All local diaspora scripted effect and trigger calls resolve to definitions in the new files, and the localisation file has a UTF-8 BOM. The new event IDs and localisation keys are unique in the repository search performed for this tranche.

## Known limitations and follow-up

Action 54 technical missions retain the existing matrix validation because that action is not one of the current consent-gated readers. The Charter League project panel now exposes the host's live administration and intelligence capacity lanes alongside the action and project caps; the owner event still supplies the target's consent answer. In-game loading and live event interaction remain parent-owned because agents do not launch Hearts of Iron IV.
