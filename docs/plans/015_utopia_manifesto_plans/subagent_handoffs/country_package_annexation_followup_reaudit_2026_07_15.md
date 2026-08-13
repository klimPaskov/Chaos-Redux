# Event 015 Country-Package Annexation Follow-up Re-audit

Date: `2026-07-15`  
Event: `015_utopia_manifesto`  
Auditor role: `chaosx_country_package_auditor`  
Mode: focused source audit with narrow P1/P2 corrections; no commit

## Verdict

**PASS for the exact Necessary Ground annexation and Event 015 founder-package
surface after the corrections recorded below.**

The accepted annexed founder receives immediate hidden event
`chaosx.nr15.164` in its own country scope. Its safe-state call therefore runs
with the defeated Event 015 actor as `ROOT`, not the annexer. The current
cleanup removes the founder's Event 015 identity, political override, ideas,
characters, advisors, decisions, missions, target and state reverse links,
league/external-network state, aftermath queue, and achievement runtime without
tearing down the annexer's country package. Shared target/state marker flags are
removed only when the exact departing founder was the final registered founder.

The `.163` target-annexation bridge and delayed `.165` selected-state control
bridge preserve the same invariant. Third-party stewardship succession adopts
only the annexer as the founder's new case counterparty; founder extinction
closes the case as coercive and achievement-disqualifying rather than as a
peaceful completion. No open P0-P2 country-package defect remains in this
focused surface.

## Corrections included in the audited shared source

| Severity | Correction | Result |
| --- | --- | --- |
| P1 | `chaosx.nr15.163` and `.164` used undocumented `hide_window = yes`. Both exact bridges now use the documented/vanilla `hidden = yes`. | The immediate bridge events are genuinely hidden and have no empty event window path. |
| P2 | `utopia_manifesto_enter_annexation_safe_state` did not clear the aftermath chain's pending, available, selected, and restitution-response transient flags. | Annexation now clears the entire unfinished aftermath queue before recording dissolution/resolution and entering the ordinary disable safe state. |
| P1, concurrent parent correction | The new `.165` state-control callback was initially immediate and could validate a selected-state transfer before `.163` handled a full target annexation. The shared on-action now schedules `.165` with `hours = 1`. | Immediate `.163` owns annexation successor/extinction ordering. The delayed state callback either validates the settled successor or no-ops after the case/founder cleanup. This auditor did not edit the parent-owned scheduling line. |

## Exact `on_annex` scope and ordering proof

`common/on_actions/015_utopia_manifesto_on_actions.txt:114-188` follows the
documented `on_annex` contract: `ROOT` is the annexer and `FROM` is the annexed
country.

1. The hook saves `ROOT` as `utopia_manifesto_annexing_country` and `FROM` as
   `utopia_manifesto_annexed_case_target`.
2. It snapshots the annexed target's `utopia_manifesto_case_founders` reverse
   array before any founder callback mutates case links.
3. Each snapshotted founder becomes the recipient of immediate hidden event
   `.163`; that event's `ROOT` is therefore the exact founder.
4. After all callbacks, the dead target's reverse founder array and active
   target flag are cleared. Snapshotting makes this safe for multiple founders.
5. Only if annexed `FROM` itself has `utopia_manifesto_accepted` does the hook
   run `FROM = { country_event = { id = chaosx.nr15.164 } }`. There is no delay
   field, so the founder cleanup is immediate and the event recipient resets
   event `ROOT` to the annexed actor.

`.164` contains only
`utopia_manifesto_enter_annexation_safe_state = yes`. It does not enter the
annexer event target or call a helper in on-action `ROOT`. The annexer can still
run its own explicitly scoped territorial and achievement refreshes earlier in
the hook, but those are separate from terminal founder teardown.

## `.164` terminal package matrix

| Surface | Result | Evidence and isolation property |
| --- | --- | --- |
| Acceptance and kernel | PASS | `utopia_manifesto_enter_disable_safe_state` clears `utopia_manifesto_accepted`, performs teardown/runtime cleanup, sets `utopia_manifesto_kernel_disabled`, and records the regime-collapse achievement disqualifier on `.164` `ROOT`. |
| Political restoration | PASS | Identity teardown restores the saved ruling ideology group, exact surviving original leader with its saved exact ideology subtype, and saved election permission before clearing the snapshot. These writes remain in the annexed founder scope, preserving a clean package if the tag later exists again. |
| Characters and advisors | PASS | All eight Event 015 institutional leader roles are removed; the eight institutional characters and all sixteen advisors are retired; advisor active flags are cleared. |
| Cosmetic identity | PASS | `drop_cosmetic_tag = yes` runs on the annexed founder, followed by clearing route, formation, succession, and identity flags. No annexer cosmetic call is reachable from `.164`. |
| Country ideas | PASS | `utopia_manifesto_clear_all_country_idea_lifecycles` removes all Event 015 country-idea families and lifecycle stage flags. |
| Decisions and missions | PASS | The disable path reaches decision, stewardship, league, evolution, prefire, calling, growth, and formation cleanup. Static comparison found all `43/43` defined Event 015 missions referenced by a removal path in the Event 015 scripted effects. |
| Country-target reverse links | PASS | Central case cleanup loops only the founder's `utopia_manifesto_active_case_targets` and removes exact `ROOT` from each target's `utopia_manifesto_case_founders`. A target loses `utopia_manifesto_active_case_target` only when no other founders remain. |
| State-target reverse links | PASS | The same cleanup loops the founder's `utopia_manifesto_active_case_states` and removes exact `ROOT` from each state's `utopia_manifesto_case_state_founders`. A state loses `utopia_manifesto_active_case_state` only when the final founder is removed. |
| Stewardship territory | PASS | Terminal restoration transfers a purchase/ultimatum/enforcement state only if it is still owned by founder `ROOT`. An already annexer-owned state is not stolen back. Lease/joint-administration cleanup may restore control to the exact case target, which removes the founder's temporary administration rather than modifying an annexer country package. |
| League and external network | PASS | Cleanup removes founder-owned pending missions and arrays, removes exact partner/member/observer/sponsor/reserve/aid/defense reverse flags, dismantles only a founder-led Event 015 formal faction, and clears founder-created diplomatic relations. It does not annex or reinitialize another country. |
| Achievement runtime | PASS | The founder is removed from recorded attackers' reverse defender arrays, its own challenge arrays are cleared, and identity/runtime proof is removed. All fourteen Event 015 achievement definitions require `utopia_manifesto_accepted`, so the `.164` founder cannot complete one after terminal cleanup. |
| Aftermath state | PASS | Scheduled/source flags plus chain pending, available branch, selected branch, and restitution-response flags are cleared. Only the deliberate terminal facts `utopia_manifesto_commonwealth_dissolved` and `utopia_manifesto_aftermath_resolved` are set before ordinary disable cleanup. |

## `.163` successor and founder-extinction invariants

### Third-party stewardship successor

For an exact annexed case target, `.163` adopts the annexer only when the case
is already in stewardship, the saved annexer exists, and the annexer is not the
founder. The helper:

- replaces the founder's one-element country target and selected-country
  arrays with the annexer and records its exact country ID;
- registers only the exact founder in the annexer's reverse founder array;
- applies the configured integrity/support succession losses and immediately
  revalidates the case;
- leaves the exact selected state and its reverse founder registration in
  place, so the delayed `.165` callback checks the settled annexer/state pair;
- grants no `utopia_manifesto_accepted`, route, identity, country idea,
  institution, league, or achievement-proof flag to the annexer.

If the annexer is not an Event 015 actor, every Event 015 achievement remains
blocked by the acceptance gate. If it is independently accepted, adoption
still adds only counterparty/selection markers and does not satisfy a route or
country-package achievement requirement.

### Founder extinguishes its own target

When the saved annexer is the exact founder, `.163` does not adopt the founder
as its own counterparty. It records target extinction, coercive conduct,
unresolved stewardship failure, and the unrelated-annexation achievement
disqualifier; resolves the stewardship burden; removes the exact wargoal and
missions; unregisters both country and state reverse links; and clears the case
and selected target. It never calls peaceful-case completion or grants a
formation/identity/achievement proof.

The one-hour `.165` ordering closes the only observed bypass: selected-state
control changes from the same annexation can no longer invalidate and erase the
case before immediate `.163` performs successor adoption or explicit founder
extinction. After `.163`, `.165` either validates the adopted case or fails its
accepted/active-case/reverse-membership guards and does nothing.

## Focused validation evidence

| Check | Result |
| --- | --- |
| Event 015 event definitions after `.165` addition | `99` |
| `.163`, `.164`, `.165` hidden declarations | `3/3` use `hidden = yes` |
| `.164` delay fields | `0`; immediate |
| `.165` scheduling | `hours = 1` from the state-control hook |
| Defined Event 015 missions / missions with removal references | `43 / 43`; missing `0` |
| Event 015 achievements with acceptance gate | `14 / 14` |
| Country reverse registries | exact founder add/remove plus last-founder flag clear |
| State reverse registries | exact founder add/remove plus last-founder flag clear |

This was a static source and lifecycle audit. No live game execution was
performed or requested.

## Files changed by this follow-up

- `events/015_utopia_manifesto.txt`
  - corrected only `.163` and `.164` to `hidden = yes`;
- `common/scripted_effects/015_utopia_manifesto_aftermath_effects.txt`
  - completed transient aftermath cleanup in
    `utopia_manifesto_enter_annexation_safe_state`;
- this handoff.

The shared `.165`, reverse state-founder registry, exact target predicate, and
one-hour scheduling correction were concurrent parent/decision-system work and
are audited here, not claimed as this auditor's edits.

## References and skills

Skills used:

- `chaos-redux-events` for event-root, hidden-event, integration, and terminal
  lifecycle expectations;
- `chaos-redux-decisions-missions` for Necessary Ground mission/case cleanup and
  target-disappearance invariants;
- `chaos-redux-subagents` for bounded ownership, concurrent-change review, and
  this handoff.

The required offline wiki core pages were consulted, with targeted use of
`On actions`, `Event modding`, `Data structures`, `Effects`, `Scopes`, and
`Triggers` for `on_annex`, event recipients, event targets, and immediate versus
delayed callbacks. Installed vanilla documentation consulted included
`common/on_actions/_documentation.md`, `documentation/effects_documentation.md`,
and `documentation/triggers_documentation.md`. Vanilla and approved-reference
event files were checked for hidden-event syntax; they use `hidden = yes`, and
no `hide_window = yes` precedent was found.

## Simplifications, omissions, blockers, and adjacent risk

- Simplifications or fallbacks in the audited annexation surface: none.
- Open P0-P2 blocker in the audited annexation/country-package surface: none.
- Commit: none, as requested.
- Adjacent out-of-scope observation: legacy Event 015 events `.116`, `.150`,
  `.205`, `.212`, and `.214` still use undocumented `hide_window = yes`. They
  are not part of the `.163-.165` annexation bridge and were deliberately not
  bulk-edited in this bounded follow-up. They should receive a separate
  mechanical hidden-event correction before a whole-event completion claim.
