# Event 016 DHR compact lifecycle review — 2026-09-02

## Scope and verdict

Read-only review of `chaosx.nr16.49`, its `.50/.51` notices, `.52` watchdog, and the exact compact offer/cleanup/validity callers.
The binding source is `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md` and the parent's explicit stale-popup, stale-watchdog, and once-only settlement requirements.
Only this handoff is authored; no gameplay, asset, configuration, spreadsheet, or other documentation file is changed.
No commit or game launch was performed and no logs were requested.

The delivery-time valid response pool is correct: `.49.a` and `.49.b` use `dhrondan_compact_response_is_valid`; `.49.c` uses its inverse.
Cleanup therefore cannot compete with accept/refuse in a valid delivery-time AI option set.
This is source eligibility evidence only, not a certified probability result.
The probability owner is capturing the baseline separately.

The lifecycle is incomplete: option effects are not guarded at click time, the valid delivery branch permits duplicate popups, and the watchdog can release an open popup's receipt before that popup has resolved.
Those issues are distinct from the already-correct option visibility split.

## Severity-sorted findings

### P1 / C1 — Stale visible options can grant rewards and clear a newer offer

Evidence: `events/016_dhrondan_country_events.txt:54/80` guard option visibility only.
The actual accept effects at 66–74 and refusal effects at 91–94 contain no `if = { limit = { ... } }` commit-time check.
Invalid cleanup at 101–108 only checks whether the actor target exists; it does not confirm that the global current offer target still belongs to this popup.
`common/scripted_effects/016_dhrondan_country_effects.txt:269–273` then unconditionally clears the actor's active/delivered flags and the global target.

The required offline Event modding reference at line 149 states that option triggers decide visibility when the event fires; a false option does not appear until the event fires again.
Consequently, a popup delivered while valid retains its visible accept/refuse paths even if war, subject status, actor route, or the offer receipt changes before the user chooses.
The `.52` watchdog clears an invalid delivered offer at event lines 139–148, allowing the actor to start another offer because the decision only requires the active flag to be absent (`common/decisions/016_dhrondan_country_decisions.txt:178–183`).
The old popup can subsequently execute accept/refuse and clear that newer offer's global target and flags.
Accept also writes the old recipient's partner flag and actor compact/stability reward without revalidation.
An invalid-at-delivery `.49.c` popup has the same cross-offer cleanup defect if a newer offer starts before the old cleanup choice resolves.

Minimal correction: wrap each option's actual mutations in a click-time ownership/validity guard, not merely its visibility trigger.
Acceptance/refusal must require the exact original actor and recipient to own the still-active delivered offer and the current response predicate to pass.
An invalid choice must perform no diplomacy/reward; it may clear only the receipt demonstrably owned by this popup.
Remove the unconditional global-target clear for an unmatched stale popup.
This must be paired with C2/C3's serialization fix; checking only actor and recipient does not distinguish reused same-pair offers after the old popup's lock has been released.

### P1 / C2 — The delivered receipt does not prevent another valid `.49` delivery

Evidence: the `.49` trigger at event lines 30–43 is an OR.
Its first branch is `dhrondan_compact_response_is_valid`, whose definition at `common/scripted_triggers/016_dhrondan_country_triggers.txt:178–196` requires active state but does not reject delivered state.
Only the fallback invalid-delivery branch tests `NOT = { has_country_flag = dhrondan_diplomatic_offer_delivered }` at event line 40.
The immediate block simply sets delivered again at 45–49.

Source scenario: a second queued or deferred `.49` reaches the same recipient while the original offer is active, delivered, and otherwise valid.
Both deliveries pass, and both popups expose the unguarded accept/refuse effects.
Resolving the first clears the receipt, but the second already-visible accept can still apply stability again because it has no commit guard.
The normal decision currently dispatches one immediate `.49`; this review does not claim a second normal start bypasses the decision's active gate.
It demonstrates failure of the explicitly requested duplicate/deferred delivery scenario.

Minimal correction: make actor-active, exact recipient ownership, and `NOT delivered` common requirements of the entire `.49` delivery trigger, covering both valid and invalid-at-delivery branches.
Set delivered only after those requirements pass.
Keep C1's click-time checks because delivery deduplication alone does not protect an already open event against later invalidation.

### P2 / C3 — Watchdog follows mutable current state rather than its original offer, and releases open locks

Evidence: `.52` at event lines 137–148 checks only the scoped country's current active flag and current global offer target.
It reschedules itself only for delivered + Covenant + valid-partner state; every other state clears the offer.
The initial watchdog is scheduled before the decision saves the recipient target (`016_dhrondan_country_decisions.txt:189–193`).
Reinitialization also queues `.52` whenever the active flag is present (`016_dhrondan_country_effects.txt:305–309`).
No immutable generation token or regular original-recipient pointer belongs to the watchdog chain.

The definite current-path problem is that war, subject change, route loss, or recipient destruction after delivery clears the offer while the recipient's old popup may still exist, enabling C1.
For the requested stale-watchdog/deferred-delivery scenario, an old `.52` can also see a newer active but not-yet-delivered offer and clear it merely because delivered is false.
Do not overstate this: a stale `.52` seeing a newer valid delivered offer does not clear it; it schedules another monitor.
The normal decision's `.49` call is immediate, so the undelivered overlap specifically concerns delayed/deferred delivery, not a demonstrated ordinary start-order race.

Minimal correction: retain the delivered offer's active/delivered/exact-target lock until its popup response or native timeout closes it, even if current response legality changes.
The click-time guard handles invalid choices without rewards and then releases that owned lock.
Do not let `.52` clear a delivered lock simply because war, subject status, or regime changes.
Capture a regular original-recipient target before scheduling the watchdog and verify both actor and recipient against the current receipt for any undelivered cleanup.
Do not treat `delivered = false` alone as proof that a viable offer failed; an undelivered cleanup must have a real invalidity or delivery-deadline condition and must not affect a delivered replacement.
Keep this as the existing offer's internal lifecycle, not a new diplomatic mechanic or public meter.

## Supported identity mechanism and limits

The recommended serialization uses existing supported country flags, ordinary `if/limit` guards, and regular event-target pointers.
Installed `documentation/effects_documentation.md:6496/6505` documents regular/global target saves, and the offline Data structures reference at 292–301 documents that regular targets carry through events fired from their chain.
Thus an original actor and recipient can be preserved as scope pointers for the popup/watchdog chain.
They are object pointers, not immutable copies of the countries' changing variables or flags.

Do not invent an event-local generation number using a temporary variable: offline Data structures line 415 explicitly says temporary variables do not carry into events.
A normal country variable is likewise mutable and does not snapshot a value separately for each open popup.
No supported per-popup numeric snapshot facility was established by this bounded review.
Retaining the exclusive delivered receipt until resolution, combined with one-delivery admission and click-time actor/target checks, prevents a second same-pair offer from replacing an unresolved popup without requiring that unsupported facility.
The native event timeout provides eventual resolution for an existing recipient; the offline Event modding reference at 178 documents a default timeout of 13 days and the first-option behavior.
Every visible option therefore needs safe invalid-click cleanup, including accept, because a valid-at-delivery popup cannot gain a formerly hidden `.c` option when it later becomes invalid.

Destroyed-country and re-release behavior needs an explicit bounded disposition in the owner patch.
Offline Event modding line 31 states that delayed-event timers on a nonexistent country stop until it exists again.
An actor-only `.52` must not be represented as immediate cleanup proof after DHR destruction.
Retained identity and current ownership must be rechecked on reinitialization and on any surviving recipient response.
This review does not propose a whole-world poll or claim that an inaccessible popup was automatically dismissed.

## Scenario matrix — source trace, not engine execution

| Scenario | Current source result |
| --- | --- |
| Valid delivered offer, no state change | `.a/.b` visible; `.c` excluded. `.52` retains the receipt and queues another one-day check. |
| Accept once | NAP, reciprocal opinion, partner/concluded flags, one stability reward, `.50` notice, and receipt cleanup. `.50` itself is presentation-only. |
| Refuse once | Refusal opinion, `.51` notice, and cleanup; `.51` itself has no reward. There is no permanent refusal flag barring a later intentional retry. |
| War or either country becomes subject after delivery | Response predicate becomes false; `.52` clears the receipt. Existing visible accept/refuse effects remain unguarded, so a stale click can still mutate state. |
| Covenant route flag lost / world end after delivery | Covenant predicate fails through `dhrondan_country_is_active`; watchdog clears. Same stale-click gap applies. A mere ruling-ideology change without changing the route flag is not itself a route-loss check. |
| Recipient destroyed after delivery | The partner predicate's `exists = yes` fails and DHR's watchdog clears the receipt. Whether a particular recipient popup survives re-release is not asserted; current code has no immutable offer generation to distinguish it if it does. |
| Actor destroyed after delivery | Current response predicate fails, but an actor-owned delayed watchdog cannot be assumed to tick while DHR is absent. An already visible recipient option has no click-time actor-existence guard. Reinitialization queues a watchdog if the old active flag survives. |
| Deferred duplicate `.49` while first popup is valid | Valid branch ignores delivered; duplicate popup admitted. Duplicate acceptance can repeat stability because commit effects do not test the remaining receipt. |
| Stale `.52` after offer cleared, no replacement | Its active trigger fails; no cleanup/requeue. |
| Stale `.52` with newer valid delivered offer | Retains current offer and queues another monitor; no immediate erasure in this state. |
| Stale `.52` with newer undelivered offer | Current else branch clears the newer offer without matching the watchdog's original offer. |
| Old invalid `.49.c` after replacement offer | Current `.c` clears the actor/global receipt without checking the replacement's target. |
| Old `.49.a/.b` after replacement offer | Visibility was decided earlier; raw effects address the saved actor and clear its current global receipt, even when the current offer targets a different country. |

Partner validity at `016_dhrondan_country_triggers.txt:106` checks existence, not DHR, neither country being a subject, no mutual war, no NAP, and no existing compact-partner receipt.
Response validity at 178 additionally checks world-end absence, exact global target identity, actor existence/tag/Covenant/active status, and the recipient's own existence/subject/partner state.
These predicates are materially useful and should be reused, not replaced by a weaker new test.

## MCP evidence and exact limits

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.
Both narrow inspect requests and both renders returned focused partial analysis at revision `18bf807c8be35655138be368b38a6ff43f90d4c9ac0a1470ca1d9d44f43afd8f`, graph hash `e12130ac480e90a1098f39e8c272668599c42b61125c7a027bb8e84ebe6659d2`.
All returned zero indexed helpers and validation false: `Large workspace analysis deferred workspace-wide helper projections and lifecycle passes; direct evidence is linked`.
No full scan/expansion retry was made.

Supported invocations used:

```json
{"workspaceId":"mod_chaos_redux_ea3b2d67c2c0","mode":"trace","selector":{"kind":"event","eventId":"chaosx.nr16.49"},"direction":"both","expandHelpers":true,"maxDepth":2,"maxNodes":24,"maxEdges":60}
{"workspaceId":"mod_chaos_redux_ea3b2d67c2c0","view":"options","selector":{"kind":"event","eventId":"chaosx.nr16.49"},"direction":"both","expandHelpers":true,"maxDepth":2,"maxNodes":24}
{"workspaceId":"mod_chaos_redux_ea3b2d67c2c0","mode":"trace","selector":{"kind":"manifest","manifest":{"id":"event016_dhr_compact_receipts","eventIds":["chaosx.nr16.50","chaosx.nr16.51","chaosx.nr16.52"]}},"direction":"both","expandHelpers":true,"maxDepth":1,"maxNodes":24,"maxEdges":60}
{"workspaceId":"mod_chaos_redux_ea3b2d67c2c0","view":"timing","selector":{"kind":"manifest","manifest":{"id":"event016_dhr_compact_receipts","eventIds":["chaosx.nr16.50","chaosx.nr16.51","chaosx.nr16.52"]}},"direction":"both","expandHelpers":true,"maxDepth":1,"maxNodes":24}
```

Artifacts read locally and inspected:

- [.49 trace JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bf7ecd8acbba54a147efacb876d3c92f9548e1a9f45a2e8558e59a8c52c56a94/339661ab56d41f186d5878602400dbde36d54902547ed160b18bad86aa2108b4/event-trace-18bf807c8be3.json)
- [.49 options JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4278a02575ec940e9c44e6db7ab976619134100f3c1e1e4f3ad72c255f4a6f27/f1486ae9f9e5bee88658a79f06e9c721e4e14ddfce74898a7b85acbd170d0d40/event-options-18bf807c8be3.json)
- [.49 options PNG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b24e9edbc8352ed1008967c93a6d907adfb3f76e9017bf64a69ff2592652f38b/340754bf23022e03b9448dbb3cc86e9d95c011fb177f525f84fae6f071beb509/event-options-18bf807c8be3.png)
- [.50/.51/.52 trace JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/957b73f2f9f9d9a5360d47bdc99ffdeedcffe601a3a1cf98f93496d82c5c487e/30781de4397d2eadc076bb7faf9d12c5117389ba991a6070e3d828e4b47fd751/event-trace-18bf807c8be3.json)
- [.50/.51/.52 timing JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ad76f6dfc163820faa42d1a02a1cdd67bd98920143a10d804c43a1072e2469c9/79870fe84f61acc2220fe0997ceae7ac13d1fd78fdc2c5c30aca3f411824759e/event-timing-18bf807c8be3.json)
- [Timing PNG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/94dd8c0b7ca0434f69be4b46c95b160e222cfcab80184f87a3f14598a716e602/e01378fe031cf838bc27b70a427a6068094b88b5b02d20179e5fbf33bca0452c/event-timing-18bf807c8be3.png)

The `.49` trace contains `.49`, `.50`, `.51`, their option nodes, and unresolved cleanup nodes.
The second trace explicitly contains `.50/.51/.52`; its bounded trace is marked truncated.
The options render shows all three `.49` options and `.50/.51` branches; it does not evaluate their scenario-specific eligibility.
The timing view filters to `.52`'s self-cycle, one selected node, rather than displaying the terminal notices.
Both PNGs were visually inspected; these are static graph diagrams, not in-game popup simulations.

Actual source-linked unresolved records are `dhrondan_clear_diplomatic_offer` at event lines 74, 94, 106, and 148, plus `active` at line 66.
The cleanup helper exists at `common/scripted_effects/016_dhrondan_country_effects.txt:269`; the focused graph omits its catalog, so these are not missing-source findings.
Installed effects documentation at 3564–3575 explicitly documents `diplomatic_relation.active`; its classification as a missing helper is also a graph interpretation limit, not invalid game syntax.
Global graph counts are not substituted for Event 016 diagnostic review.

One explicit cached comparison was attempted with both `before` and `after` set to `{"revision":"18bf807c8be35655138be368b38a6ff43f90d4c9ac0a1470ca1d9d44f43afd8f"}` and `render:false`.
It returned `EVENT_REVISION_NOT_CACHED`, no artifacts, validation false.
No report/render wrapper was retried as a graph artifact and no successful comparison is claimed.

## Source checkpoint and references

HEAD at capture: `4af9495786f600d2487e1ceec7aac7ff4bb9e7fd`.
Capture time: `2026-09-02T12:31:23+03:00`.
The four in-scope source files had no working diff at this checkpoint.

| File | SHA-256 |
| --- | --- |
| `events/016_dhrondan_country_events.txt` | `83c1aae6b2a625bdf4e34dc201c7298be108cef323df21e683f76bac72769945` |
| `common/scripted_effects/016_dhrondan_country_effects.txt` | `b6492039c1d17094ea912696f3daeb5d2128599b0b5a87071ed5279f352896f7` |
| `common/scripted_triggers/016_dhrondan_country_triggers.txt` | `791c97a24e2f97fcae0145087f1997d46f88ac4fe908b36ec5ad39176a1a4e81` |
| `common/decisions/016_dhrondan_country_decisions.txt` — exact offer caller only | `8af7f070ed07d1b3de555a90bf4c4123c222b424ac03818e007882a79e5c373f` |

The event-file hash also matches the MCP trace's `sourceHashes["mod:events/016_dhrondan_country_events.txt"]`.
The other three files are direct source observations, not claimed helper-graph coverage.

Relevant reference evidence: offline Event modding lines 31, 111–137, 149, 174, 178, and 188–211; offline Data structures lines 254–301 and 414–417; installed effects documentation for country events, regular/global event targets, cleanup, and diplomatic relations.
Vanilla `events/AAT_Finland.txt:2010–2018` provides a concrete non-aggression/military-access relation effect precedent.
The required core wiki pages and lifecycle skills were consulted in this agent's preceding Event 016 reviews; this pass rechecked the event timing, option visibility, and target-lifetime references directly.
Skills used: `chaos-redux-events`, `chaos-redux-improvement-loop`, `chaos-redux-subagents`, `chaos-redux-event-planning`, and `chaos-redux-decisions-missions` for the exact targeted-decision entry.
They constrained the work to accepted closure, source-linked evidence, and explicit unsupported-proof boundaries; no skill was changed.

## Disposition

The old claim that cleanup competes with valid accept/refuse options is rejected for current source.
C1–C3 are queued to the parent as bounded lifecycle corrections, not new design families.
No unapproved fallback or simplification was implemented by this audit.
Required post-patch evidence remains click-time invalidation, single delivery/settlement, no replacement-offer erasure, supported narrow MCP evidence, and the probability owner's matching baseline/comparison.
No overall DHR, Event 016, asset, or presentation completion claim is made.
