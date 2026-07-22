# Event 006 Rival Bloc Response Expiry — Decision/Mission Implementation Handoff

## Scope and status

Implemented the accepted response-expiry follow-up for the existing Event 006
rival-bloc invitation category. The change is limited to invitation timing,
state binding, lifecycle cleanup, player-facing decision text, and the
associated plan record. It does not add a new category, scripted GUI surface,
formable, event chain, or material-cost loop.

## Issue list, sorted by severity

- **Resolved — high:** A delivered invitation could leave the sole global
  invitation lock open indefinitely when the recipient never chose an action.
  The recipient-owned response mission now expires through central decline.
- **Resolved — high:** A stale recipient state could survive a contract or
  Event 006 generation change. The pending trigger now binds the inviter,
  contract generation, and recipient generation; stale ratification is
  removed before a new offer is issued to that recipient.
- **Resolved — medium:** Delivery, recipient response, and acceptance
  ratification shared ambiguous player-facing timing. Their 90/90/30-day
  responsibilities are now separately stated and tuned.
- **Open:** None known in the owned decision/mission scope.

## Changed files and identifiers

| File | Identifiers |
| --- | --- |
| `common/script_constants/006_independence_wave_rival_bloc_constants.txt` | `independence_wave_rival_bloc_duration.invitation_response` |
| `common/scripted_triggers/006_independence_wave_rival_bloc_triggers.txt` | `is_independence_wave_rival_bloc_pending_invitation` |
| `common/scripted_effects/006_independence_wave_rival_bloc_effects.txt` | `independence_wave_rival_bloc_clear_invitation_response`, `independence_wave_rival_bloc_clear_local_invitation_state`, `independence_wave_rival_bloc_begin_acceptance_ratification`, `independence_wave_rival_bloc_expire_invitation` |
| `common/decisions/006_independence_wave_rival_bloc_decisions.txt` | `independence_wave_rival_bloc_respond_to_invitation` |
| `localisation/english/006_independence_wave_rival_bloc_l_english.yml` | `independence_wave_rival_bloc_respond_to_invitation`, `_desc`, `_invitation_response_expired_tt` |
| `docs/plans/006_independence_wave_plans/006_rival_bloc_invitation_response_expiry_followup_2026_07_22.md` | Follow-up marked implemented and resolved |

## Before and after

| Surface | Before | After |
| --- | --- | --- |
| Leader invitation | Its 90-day timer represented delivery; a delivered offer could persist indefinitely. | Delivery remains 90 days and activates a 90-day recipient response mission. |
| Ignored offer | Pending flag, global invitation lock, saved target, and target variables could block later invitations forever. | Mission timeout calls the central decline effect, clears all state, and applies the pre-existing confidence loss once. |
| Acceptance | The 30-day decision timer was the only response-related clock. | Acceptance selection first removes the response mission; the 30-day paid ratification timer and completion eligibility recheck remain intact. |
| Stale country scope | A reused country tag or changed Event 006 generation could retain invitation fields or an active prior ratification. | Pending validity requires matching inviter, rival contract generation, and target `independence_wave_generation_id`; delivery removes any obsolete active ratification before creating a new offer, and stale cleanup cannot clear an unrelated current global offer. |

## Decision category lifecycle notes

1. The bloc leader selects `independence_wave_rival_bloc_invite_member`, pays
   its existing command-power, equipment, and convoy package, and waits
   `independence_wave_rival_bloc_duration.invitation` (90 days).
2. `independence_wave_rival_bloc_issue_invitation` removes an obsolete active
   ratification decision, clears obsolete local invitation state, writes the
   pending metadata, saves the exact global target, and calls
   `activate_mission` on the recipient-owned response mission.
3. The recipient may accept or decline. Accepting removes the response
   mission and begins the distinct 30-day ratification decision; declining
   clears the pending contract and changes rival confidence once.
4. If ignored, the 90-day response mission times out through
   `independence_wave_rival_bloc_expire_invitation` and the same decline path.
5. Successful ratification registers one member row. Failed ratification,
   cancellation, or invalidation routes to decline/local cleanup and cannot
   leave the global invitation lock behind.

## Mission quality notes

| Field | Evidence |
| --- | --- |
| Owner | Recipient country scope created by `independence_wave_rival_bloc_issue_invitation`. |
| Category / region | Existing `independence_wave_rival_bloc_category`; no map region is selected. |
| Requirement | Exact pending inviter, current rival contract generation, matching recipient Event 006 generation, network standing, peace, and no incompatible main-league/client commitment. |
| Duration | `invitation_response = 90`; distinct from 90-day delivery and 30-day ratification. |
| Success | Recipient selects Accept, response mission is removed, then the existing paid ratification path resolves membership. |
| Failure | Explicit Decline, timeout, or cancellation calls central decline/local cleanup; only a valid pending invitation changes confidence. |
| Duplicate risk | The mission is removed before ratification and in local/global cleanup. Delivery first removes obsolete active ratification and local mission state. `decline_invitation` refuses to apply values when the contract or recipient generation is stale. |

## Cost and requirement clarity

No cost was added or moved. Localisation now states the three clocks:
delivery, recipient answer, and acceptance ratification. The existing custom
costs remain visibly blocked when unavailable. The response mission is
non-selectable and has a blocked AI base because it is an automatically
activated deadline rather than an AI action; existing accept/decline actions
continue to own the recipient AI choice.

## AI validity and route-lock notes

The mission only appears for an exact pending invitation. Its cancellation
trigger uses the same full eligibility trigger as acceptance, covering a dead
or reused recipient, leader change, main-league accession, incompatible
client status, insufficient network standing, and war. The target-generation
comparison additionally prevents an old Event 006 country instance from
acting on a later invitation with the same tag.

## Localisation and tooltip gaps

Resolved in the owned localisation file:

- the leader cost text distinguishes delivery and answer periods;
- invitation text tells both sides the answer is time-bounded;
- acceptance text identifies the separate ratification period; and
- the timeout has explicit player-facing refusal text.

No scripted GUI surface is owned by this change. There is therefore no GUI
artifact, render, or fidelity finding to record.

## Cleanup and exploit-risk notes

`independence_wave_rival_bloc_clear_local_invitation_state` is the sole local
owner of the response mission, pending flag, inviter, contract generation,
and target generation. The global clear applies it to the saved target before
removing the global lock and target. Delivery also removes an active stale
ratification decision before it can inherit new pending fields. Existing
member clearing, origin cleanup, leader-loss reconciliation, dissolution,
reunification, and contract opening call those helpers. This closes the
permanent invitation-lock and stale-timer paths without creating a refund,
unit, equipment, war-goal, or core loop.

## Validation evidence

The implementation was reviewed against the offline Decision Modding and
Scopes wiki pages; vanilla `effects_documentation.md` for `activate_mission`,
`remove_mission`, and global event-target cleanup; and the existing Utopia
invitation-mission pattern. Task-specific static validation recorded the
following:

- one response mission declaration is activated only by successful invitation
  delivery and uses the response duration constant;
- all four pending metadata fields have one set site and are cleared by the
  local helper; the pending trigger binds each to the current contract and
  recipient generation;
- acceptance selection removes only the response mission, while completion
  retains the existing 30-day eligibility recheck;
- timeout, explicit decline, invalidation, origin cleanup, registry cleanup,
  dissolution, reunification, and a new contract opening each reach central
  or local invitation cleanup;
- the changed decision/effect/trigger scripts and localisation references
  were checked for matching identifiers and structural balance.

Skipped meaningful validation: live-engine execution was not available in
this coding workspace, so the actual day-90 timeout and save/load behaviour
remain for the parent’s normal live-session verification. No fallback was
used.

## Remaining issues

No high-severity invitation-lock, response-expiry, or duplicate-value gap is
known within this decision/mission scope. This handoff does not audit the
concurrently owned Event Details GUI/member-cycling surfaces.
