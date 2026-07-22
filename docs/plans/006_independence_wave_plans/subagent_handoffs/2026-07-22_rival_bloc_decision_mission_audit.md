# Event 006 Rival Bloc Decision and Mission Audit — 2026-07-22

## Scope and evidence

Audited the rival-bloc contract introduced by `ed62f4707`, then revised by
`a0f3712a8`, `3cb6c8f80`, and `91cbbaf6a`. Reviewed the decision category,
all rival-bloc scripted effects, triggers, constants, AI profile, scripted
localisation, English localisation, the Event 006 call sites in
`common/scripted_effects/006_independence_wave_effects.txt`, the Event 006
specification parts 2 and 6, and the preceding league-expulsion audits.

The audit also used the offline Decision Modding, Scopes, Triggers, Effects,
Data Structures, Localisation, Modifiers, On Actions, Event Modding, Idea
Modding, and AI Modding wiki snapshots; vanilla decision/effects
documentation; and vanilla decision precedents. The relevant engine rule is
that a decision's `complete_effect` runs on selection, while `remove_effect`
runs only when its timer ends. A `cancel_trigger` ends the decision and runs
`cancel_effect`, not `remove_effect`.

No scripted-GUI surface belongs to this contract, so no GUI inspection or
render artifact was needed. No world-iterating on-action or country scan was
introduced by this surface.

## Conclusion

The implementation is a genuine, separate gameplay contract rather than a
cosmetic phase flag: it owns a contract generation, member and region arrays,
a leader target, values, paid decisions, a separate category, AI priorities,
and explicit reunification/dissolution paths. It intentionally does not create
a vanilla faction; that matches the Event 006 specification's separate
counter-league model.

The patch in this handoff closes the scope, stale-state, stale-acceptance, and
cost-tooltip defects below. One high-severity lifecycle gap remains: an
invitation has a delivery timer but no response deadline once issued. Its
follow-up plan is at
`docs/plans/006_independence_wave_plans/006_rival_bloc_invitation_response_expiry_followup_2026_07_22.md`.

## Issues, sorted by severity

| Severity | Finding | Status |
| --- | --- | --- |
| High | The 90-day invitation `days_remove` measures the leader's delivery operation. Once the target receives the invitation, neither acceptance nor decline expires automatically. An ignored target therefore leaves the single global invitation lock set indefinitely and prevents further leader invitations. | Unresolved; follow-up plan written. |
| High | Registry reconciliation read a temporary variable as `ROOT.independence_wave_rival_bloc_row_generation`. Temporary variables have no scope, so a valid/reused-tag generation row could be evaluated incorrectly. | Fixed. The row comparison now uses the unscoped temporary variable. |
| High | Invitation creation copied the contract generation from `ROOT.global.independence_wave_rival_bloc_contract_generation`. The source global is not a `ROOT`-scoped temporary/value reference. | Fixed. The assignment now reads `global.independence_wave_rival_bloc_contract_generation`, consistent with the effects documentation and existing Event 006 global-variable usage. |
| High | An invitee could select acceptance, then join the main league, become an incompatible client, enter a war, or lose its valid leader linkage during the 30-day ratification timer. The prior `remove_effect` would update bloc/main-league values even if registration rejected the country. | Fixed. `is_independence_wave_rival_bloc_valid_pending_acceptance` rechecks the exact invitation target, current leader, contract generation, network/main-league/client/standing/war gates. Cancellation declines and clears the global invitation state; the completion effect rechecks as defence in depth. |
| Medium | Reconciliation removed an invalid member row without clearing its country flags and invitation variables. A stale country could remain a rival member/leader or retain host/patron pressure after its row was pruned. Misaligned arrays had the same leak. | Fixed. Invalid rows and misaligned-array recovery clear the full member state; an active contract with no members dissolves, and a missing/invalid leader clears the invitation and selects a valid replacement. |
| Medium | Custom cost text keys lacked the required `_blocked` and `_tooltip` localisation variants. Failed resource gates could expose missing keys instead of readable material requirements. | Fixed for all six paid costs, including command power, equipment, trains, fuel, convoys, and Army Experience. |
| Low | The Event Details UI does not render the rival arrays/member list. The category does display route and current bloc values, and the existing rival-bloc system documentation records this UI limitation. | Unchanged; outside this decision-only patch. |

## Decision category lifecycle

1. `independence_wave_expel_league_member` opens the separate contract through
   `independence_wave_rival_bloc_open_after_expulsion`; the expelled country is
   registered with a new contract generation and becomes leader.
2. The category is visible only to a valid rival member or the exact pending
   invitee. It displays route, cohesion, common cause, patron capture, reserve,
   confidence, host pressure, and member count from the separate registry.
3. A leader pays an arms/convoy package before the 90-day delivery action. The
   target is stored in a country variable during that timer; it is not a state
   owner pointer, so the previous `FROM.owner` timer-redirection risk is not
   inherited.
4. On delivery, the global pending-target event target, inviter, and contract
   generation prove that the recipient has the current invitation. Acceptance
   starts its own 30-day ratification action and is revalidated at cancellation
   and completion. Decline clears the same pending state immediately.
5. Members can make paid reserve, former-host, patron, and leadership actions,
   or leave. Unregistering a leader clears any open invitation and appoints a
   replacement; unregistering the final member dissolves the contract.
6. Main-league registry registration rejects rival flags. Rival registration
   rejects main-league/founder membership and incompatible client routes. The
   main reunification call copies the rival array before unregistering rows and
   registering them in the league, then dissolves the contract.

## Mission quality notes

| Owner/category/region | Requirement and duration | Success / failure | Duplicate risk |
| --- | --- | --- | --- |
| Rival leader; `independence_wave_rival_bloc_category`; target is a network country, not a state | Authority, valid target, material package; 90-day delivery decision | Success issues exact target invitation. Cancellation clears the leader's transient pointer; paid materials remain spent. | Authority flag, in-progress flag, and global invitation-open flag prevent concurrent invites. |
| Invited country; same category; no region | Exact pending invitation, valid current leader/generation, network standing, peace, no main-league/incompatible client; 30-day ratification | Success registers membership and adjusts separate/main values. Invalidity cancels into decline and clears invitation state; paid acceptance resources are intentionally not refunded. | Exact global target and contract-generation comparison prevent stale or redirected acceptance. **No response expiry exists before the country selects this action.** |
| Invited country; same category; no region | Exact pending invitation; immediate | Decline clears invitation and applies confidence loss. | One global pending target; no repeated effect after cleanup. |
| Rival member; same category; no region | Member and reserve/common-cause gate; selectable 120-day mission | Timeout commits reserve and improves values. Member loss cancels and applies reserve failure loss. | Active-mission check prevents parallel commitments by one country. |
| Host-front member; same category; former-host relationship ledger, no state target | Valid host-front gate; 120 days plus standard cooldown | Lowers bilateral former-host pressure and bloc host pressure. Cancellation forfeits the paid package. | Decision cooldown; no state-owner target to be redirected. |
| Patron-pressure member; same category; patron ledger, no region | Patron pressure/gate; 150 days plus standard cooldown | Reduces capture, refreshes patron status, and only restores pressure when the threshold remains. | Decision cooldown; member cleanup clears patron-pressure flag. |
| Rival member; same category; bloc-wide | Valid leadership candidate; selectable 180-day mission | Timeout transfers leader and redistributes values. Invalidity applies leadership failure effects. | Active-mission check and single global leader target. |
| Rival member; same category; no region | Current membership; immediate with standard cooldown | Unregisters member; last departure dissolves contract. | Member flag and row lookup make repeated execution inert. |

## Cost, requirement, AI, and exploit notes

- All material values and durations use the new `independence_wave_rival_bloc_*`
  script constants; no per-action magic values were introduced. Costs are
  committed in `complete_effect`, so interrupted timed actions do not create a
  refund or equipment-farming loop.
- Paid outcomes are bounded by gates/cooldowns: reserve can only improve while
  the reserve/common-cause threshold calls for it; host and patron actions have
  standard re-enable timers; leadership and reserve are single selectable
  missions. No free unit, equipment, core, war-goal, or resource grant exists
  in this surface.
- The acceptance action now exposes a custom tooltip for its otherwise long
  route-lock/standing/war/leader requirements. All custom-cost keys now have
  normal, blocked, and hover tooltip localisation.
- Every decision has an `ai_will_do`; leader/member AI profiles are scoped to
  rival member flags and apply material/defence/war-restraint priorities. The
  AI cannot target dead countries, a main-league member, an incompatible client,
  a country at war, or a stale invitation generation. The unresolved response
  deadline also affects AI: an AI invitee can leave the invitation open.
- Main and rival exclusivity is enforced at both registration and acceptance.
  Patron-balanced clients are the explicit route exception. Origin cleanup,
  member removal, stale-row reconciliation, leader replacement, dissolution,
  and reunification each now clear their relevant flags, variables, arrays, or
  event targets.

## Changed files and identifiers

- `common/scripted_effects/006_independence_wave_rival_bloc_effects.txt`
  - Added `independence_wave_rival_bloc_clear_pending_invitation` and
    `independence_wave_rival_bloc_clear_member_state`.
  - Hardened `independence_wave_rival_bloc_reconcile_registry`,
    `independence_wave_rival_bloc_unregister_member`,
    `independence_wave_rival_bloc_issue_invitation`,
    `independence_wave_rival_bloc_accept_invitation`,
    `independence_wave_rival_bloc_decline_invitation`,
    `independence_wave_rival_bloc_dissolve_contract`, and
    `independence_wave_rival_bloc_cleanup_for_origin`.
- `common/scripted_triggers/006_independence_wave_rival_bloc_triggers.txt`
  - Hardened `is_independence_wave_rival_bloc_pending_invitation` and added
    `is_independence_wave_rival_bloc_valid_pending_acceptance`.
- `common/decisions/006_independence_wave_rival_bloc_decisions.txt`
  - Hardened `independence_wave_rival_bloc_accept_membership` availability and
    cancellation with a player-facing requirement tooltip.
- `localisation/english/006_independence_wave_rival_bloc_l_english.yml`
  - Added blocked/tooltip cost keys and updated invitation/ratification wording
    to describe the actual delivery and cancellation behaviour.

## Meaningful validation

- Confirmed the rival registry is actually called by Event 006 main registry
  reconciliation, expulsion, origin cleanup, and reunification call sites.
- Confirmed all decision `custom_cost_text` values have base, `_blocked`, and
  `_tooltip` localisation entries; localisation remains UTF-8 with BOM.
- Searched the patched decision surface for `ROOT.global` and scoped temporary
  uses: none remain. Also found no `on_daily`, `on_weekly`, `on_monthly`,
  `every_country`, or `random_country` hook in the rival runtime surface.
- Scoped diff hygiene completed without errors. Static review used the vanilla
  decision timer/cancellation lifecycle and existing Event 006 material-cost
  patterns.
- HOI4 Agent Tools `hoi4.event_inspect` lint produced the read-only artifact
  `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/18013cc25faf720734bd249d14c77d3b85c9daf1d85dfc391929337f6ef3dfb3/9fc2fe7bcc3a98f3e0d8e2fe1d1b8abd24b3656cccb37c1f3694ab7d3133e32f/event-lint-4fc5ca5cd6ef.json`.
  Its fidelity is workspace-global rather than rival-bloc-specific (4,899
  sources and pre-existing global diagnostics), so it is recorded as evidence
  of inspection only and not treated as a clean rival-bloc lint result.

## Skipped validation and remaining issues

- No live game scenario or save-state test was run in this audit environment.
  The key runtime uncertainty is the planned invitation-expiry behavior, not
  source reachability.
- The response-expiry mechanism and Event Details member-list rendering remain
  outside this narrow patch. No fallback was added.
