# Event 006 Rival Bloc Invitation Response Expiry — Follow-up Plan

## Problem

`independence_wave_rival_bloc_invite_member` spends resources and runs for 90
days before `independence_wave_rival_bloc_issue_invitation` sets the target's
pending invitation. That 90-day `days_remove` is a delivery timer; it is not a
response timer. If the recipient never selects Accept or Decline, its pending
flag, the global pending-target event target, and
`independence_wave_rival_bloc_invitation_open` persist indefinitely. The last
flag blocks every later leader invitation.

The Decision Modding reference confirms why a second response mechanism is
needed: `remove_effect` starts only after a decision has been selected, not
while an available decision is ignored. A timed country flag alone is also not
sufficient because expiry would not clear the global pending target or apply
the intended decline consequences.

## Proposed bounded implementation

1. Add one response-window constant to
   `common/script_constants/006_independence_wave_rival_bloc_constants.txt`.
2. When delivery succeeds, activate a recipient-owned timed response mission
   (or fire an equivalent delayed event) bound to the same exact pending target,
   inviter, and contract generation.
3. Its timeout must call `independence_wave_rival_bloc_decline_invitation` in
   the recipient scope. Acceptance and explicit decline must remove/cancel the
   response surface first, then use the same central cleanup helper.
4. Keep the existing 30-day acceptance ratification timer and its eligibility
   recheck. The response timer only governs whether a recipient responds at
   all; it must not duplicate membership registration or material costs.
5. Ensure leader removal, origin cleanup, registry reconciliation, dissolution,
   and reunification clear/cancel the response mission or event state along
   with `independence_wave_rival_bloc_clear_pending_invitation`.
6. Add recipient-facing localisation that distinguishes delivery, response
   deadline, acceptance ratification, and a declined/expired offer. Do not
   claim a deadline until the response surface exists.

## Required validation scenarios

- Delivery followed by no recipient choice: response expiry clears all pending
  flags/variables/global target and permits a new invitation.
- Accept before expiry: response state clears, 30-day ratification completes,
  and one valid member row is created.
- Decline before expiry: same cleanup path with one confidence loss.
- Recipient joins main league, becomes an incompatible client, enters war, or
  the leader changes/dissolves while the response is open: the offer closes
  safely and does not alter main/rival values twice.
- A reused tag or old contract generation cannot accept, expire, or clear the
  current contract's invitation.

## Ownership and scope

This is a targeted expansion of the existing rival decision lifecycle, but it
adds a new timed response surface and requires event/mission design review.
It was deliberately not implemented during the decision-audit hardening patch.
No fallback is proposed.
