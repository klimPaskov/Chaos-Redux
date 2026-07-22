# Event 006 Rival Bloc Invitation Response Expiry — Implemented 2026-07-22

## Result

The rival-bloc invitation lifecycle has three distinct, centrally tuned
intervals:

1. **Delivery — 90 days.** The leader pays the existing transport-and-arms
   package when `independence_wave_rival_bloc_invite_member` is selected; its
   `days_remove` represents dispatch and delivery only.
2. **Response — 90 days.** Delivery activates the non-selectable,
   recipient-owned `independence_wave_rival_bloc_respond_to_invitation`
   mission. Ignoring it expires through the same central decline effect as an
   explicit refusal.
3. **Ratification — 30 days.** Choosing Accept removes only the response
   mission, retains the pending contract state, pays the recipient's existing
   cost, and begins the independent acceptance decision timer. Eligibility is
   checked again when that timer completes.

`independence_wave_rival_bloc_clear_local_invitation_state` owns all
recipient-side invitation variables and response-mission removal. The global
`independence_wave_rival_bloc_clear_pending_invitation` effect invokes it on
the saved target, then clears the global lock and event target. The target
also records both the current contract generation and its own
`independence_wave_generation_id`; a stale mission therefore cannot accept or
expire a reused country's later invitation.

## Lifecycle and cleanup guarantees

- Delivery removes any obsolete active ratification decision and recipient
  state before setting the new pending flag, inviter, contract generation,
  target generation, global target, and response mission.
- Explicit decline and unanswered timeout use
  `independence_wave_rival_bloc_decline_invitation`; a valid pending offer
  receives the confidence loss once and all invitation state is removed.
- Acceptance selection removes the response mission. Ratification completion
  registers the member only after the existing full eligibility recheck;
  failed ratification centrally declines the offer.
- Recipient invalidation, leader removal, origin cleanup, registry
  reconciliation, dissolution, reunification, and a new contract generation
  all route through either the global pending clear or the local state helper.
  An old recipient scope that is no longer the saved pending target can only
  clear its own obsolete fields, never the current global offer.

## Files implemented

- `common/script_constants/006_independence_wave_rival_bloc_constants.txt`
- `common/scripted_triggers/006_independence_wave_rival_bloc_triggers.txt`
- `common/scripted_effects/006_independence_wave_rival_bloc_effects.txt`
- `common/decisions/006_independence_wave_rival_bloc_decisions.txt`
- `localisation/english/006_independence_wave_rival_bloc_l_english.yml`

The detailed implementation evidence and validation matrix are recorded in
`subagent_handoffs/2026-07-22_rival_bloc_response_expiry_implementation_handoff.md`.

## Scope resolution

This follow-up is resolved. It introduced no fallback and no additional
decision system; it extends the existing invitation category with one
recipient-owned mission and existing central cleanup paths.
