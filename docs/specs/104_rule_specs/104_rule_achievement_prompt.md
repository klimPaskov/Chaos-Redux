# Achievement prompt: Event 104 Rule

Implement and validate the three achievements in Part 5 through the current shared Chaos Redux achievement framework.
Read Part 5 in full, Part 3's novelty and evolution rules, the immutable receipt contract, the validation matrix, the current achievement-related project instructions, and the current role definitions before work.
The labels in the specification are working labels.
Write final player-facing titles and descriptions from their intended accomplishments rather than pasting planning prose.

## Required identities

| ID | Challenge identity |
| --- | --- |
| `chaosx_rule_adaptation` | Win an existing major war after a useful action is restricted and a second distinct rule family changes, with contribution, independence, survival time, deadline, and fixed-core conditions. |
| `chaosx_rule_coalition` | Preserve an independent coalition while recruiting across ideology groups under multiple rule changes, including a genuine revision. |
| `chaosx_rule_cascade_victory` | Win an existing major war after a substantial IV reshuffle and maintain the required post-victory state. |

Use the exact conditions and timings from Part 5.
Do not simplify them into a count of firings, a final flag check, or an acknowledgement reward.
The expected windows are A01 day 180 through day 365, A02 day 270 through day 540, and A03 a victory by day 365 followed by a 90-day continuity check.
A03 can therefore finish no later than day 455 for an otherwise valid attempt.
Its day-365 victory deadline is inclusive.
Expire only after that window closes when no qualifying victory was captured, and preserve a timely victory's pending 90-day check even when it completes on day 455.
A day-366 victory cannot revive an expired attempt.

## Tracking requirements

Bind every qualifying change to an immutable verified Event 104 receipt and stable native rule identity.
Use frozen pre-request provenance for fresh and revision counts.
Require an actual player or coalition-member material witness where specified.
A global option change affecting only another country does not satisfy a player-impact gate.
Keep consumer-family distinctness separate from destination-option distinctness.

Preserve the arming player's country identity, war or faction identity, fixed owned-core state set where applicable, original enemy-major identities, original independent faction members, qualifying joins, deadlines, and disqualifier receipts.
For A01 and A03, freeze every qualifying ongoing war at arming with its own original major enemies and use the first qualifying victory from that fixed set.
Later wars cannot enter the attempt and later victories cannot reset a latched result.
Require verified identity lineage when a war object changes and a nonempty original owned-core snapshot before either military attempt can arm.
Capture war outcome and contribution before the relevant war object disappears.
Use the same war and contribution denominator for the final ratio.
Do not round a near miss upward across a threshold.
An unavailable or ambiguous war result cannot pass.

Use the existing shared player eligibility framework.
Respect observer, AI, debug, force-test, country-switch, subject, annexation, capitulation, and continuity disqualifiers exactly as specified.
Do not claim account-level continuity or comprehensive cheat detection without actual support.
One active attempt per achievement per eligible player is sufficient.
An active attempt cannot extend its deadline when another qualifying Rule event fires.

Use relevant existing rule, war, faction, and player lifecycle hooks plus generation-bound delayed checks.
Do not add an all-country daily scan.
Every stale deadline, victory, membership, or post-victory callback must reject an expired or replaced generation.
Save/load must preserve a valid attempt and cannot replay an earned award.

## Presentation and art

A01 and A02 are visible from the start.
A03 is hidden until Evolution IV actually unlocks, then its goal can appear through the existing achievement interface.
Do not reveal A03 through a fake dated evolution preview.
Final wording should explain the accomplishment and material requirements in readable terms while keeping internal receipt IDs, source paths, and hidden implementation counters out of player text.

Use the three original completed 64 by 64 subjects and exact grey/not-eligible derivatives in the asset prompt.
Bind the nine final DDS files directly under `gfx/achievements/` using the exact achievement IDs and suffixes.
Verify all states in the real shared consumer.
The parent owns final bindings and `.gfx` integration.

## Acceptance

Run C06 through C14 and the relevant persistence and presentation cases in the validation matrix.
For every achievement, demonstrate a true positive, the nearest numerical and date failures, a missing distinct rule or revision, a masked witness, an invalid player continuity path, and a stale callback.
Verify no credit from startup-selected options, another system's changes, ambiguous writes, or a debug fixture.
Retain exact evidence and unresolved tracking limitations.
An achievement is complete only when its actual accomplishment can be observed and awarded correctly through the shared system, with final art and localisation aligned.
