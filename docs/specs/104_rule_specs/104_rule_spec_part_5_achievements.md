# Event 104 Rule: achievements

## Achievement role

Rule's achievements recognise adaptation to the changed campaign.
They do not reward selecting the event, acknowledging a report, reaching an evolution threshold, or accumulating firings without a player accomplishment.
The proposed set contains three achievements with distinct military, coalition, and late-cascade challenges.
They use the existing achievement interface and grant only the ordinary achievement recognition supported by that system.

Names below are working labels for design discussion.
They are not finished localisation strings.
The separate achievement prompt requires final player-facing wording to be written and audited during implementation.

## Shared eligibility

An achievement run belongs to a human-controlled country through the existing shared achievement eligibility framework.
The player must be an independent country when the challenge begins.
Observer execution, AI-only participation, debug fixtures, console-assisted test runs, and forced diagnostic scenarios do not qualify for credit.
Use the project's real eligibility and disqualification mechanisms.
Do not claim to detect arbitrary external save editing or every console action if the shared framework cannot do so.

The player must remain on the same country identity for the challenge.
Cosmetic names and normal country presentation changes do not create a new run.
A player country switch, loss of human control under the framework's continuity rules, annexation, capitulation, or becoming a subject fails the current attempt.
Already earned achievements remain earned.
An eligible later Rule outcome may arm a new attempt after a prior attempt ends.

Only verified Event 104 result rows count as rule changes.
A rule must have a documented material witness affecting the candidate player or the coalition members specified by the achievement.
A globally stored option that affects only an unrelated AI country does not satisfy a player-impact condition.
The result's native rule identity and consumer family determine distinctness.
Two options of the same native rule count as one distinct rule.

Use actual war-result and contribution evidence for victory conditions.
An enemy's disappearance, temporary occupation, white peace, or an ally's unsupported narrative report is not a proven victory.
The implementation must identify a supported end-of-war result or equivalent peace-settlement receipt and preserve the relevant player contribution before the war object disappears.
If the current framework cannot observe that signal reliably, the affected achievement is blocked until its tracking is implemented or its design is explicitly revised.

For A01 and A03, freeze the complete set of qualifying ongoing wars at arming, with the original qualifying enemy-major identities recorded separately for each war.
Use the first victory from that fixed set that satisfies the achievement's contribution, timing, and preceding-rule conditions.
The contribution numerator and denominator must come from that same resolved war.
A war that begins later cannot enter the set, and a later victory cannot replace an already latched qualifying result or reset its continuity timer.
If the engine merges or replaces a war identity, require verified lineage to a frozen qualifying war and a traceable qualifying enemy result.
Unresolvable identity or contribution evidence does not pass.

Both military achievements require at least one state in the original owned-core snapshot when they arm.
An empty set does not create an attempt, so the 75 percent condition is never undefined or a vacuous pass.

## A01: adaptation after a restriction

| Field | Design |
| --- | --- |
| Stable proposed ID | `chaosx_rule_adaptation` |
| Working label | Adaptation Under New Rules |
| Visibility | Visible from the start through the existing achievement interface. |
| Difficulty | Hard. |
| Eligible actor | An independent human country already fighting at least one enemy classified as a major at the start of the attempt. |
| Trigger to arm | A verified Rule transition changes an actually usable diplomatic or intervention action for that player from permitted to blocked. |
| Time window | 365 days from that committed transition. |
| Earliest completion | 180 days after the attempt begins. |

The player must win one of the frozen qualifying ongoing wars against at least one enemy that was a major in that war when the attempt began.
Their preserved war contribution must be at least 20 percent of their winning side's contribution in that war.
At least one additional, distinct native rule in a different consumer family must be successfully changed by Event 104 during the attempt and materially affect that player before the victory is recorded.
The player must remain independent and uncapitulated through the attempt.
At completion they must control at least 75 percent of the states they owned and regarded as cores when the attempt began, counting the fixed state set rather than newly acquired territory.

If victory occurs before day 180, preserve its evidence and evaluate the remaining survival and core-control conditions at day 180.
If victory occurs after day 180 and no later than day 365, evaluate completion immediately.
The additional rule change must precede victory, so a later random firing cannot retroactively satisfy the adaptation challenge.
If the victory or required second change never occurs by day 365, expire the attempt without a gameplay penalty.

This achievement tests continued military success after a useful supporting action disappears and a second part of the campaign changes.
It does not require the player to adopt a particular ideology or choose a particular compensating action.
Ordinary strategic adaptation remains open.

### A01 tracking

Snapshot the player identity, start receipt and date, frozen qualifying war set, enemy-major identities per war, nonempty original owned-core state set, first restrictive rule and consumer family, and the relevant old-permitted/new-blocked witness.
During later Rule commits, record the first qualifying different-family rule that affects the player.
At war resolution, capture the winning side, surviving qualifying enemy result, player contribution numerator and denominator, resolution date, and whether the second rule was already recorded.
Maintain disqualification receipts for capitulation, subject status, player switching, and continuity loss.
Use generation-bound day-180 and day-365 checks through existing lifecycle support.

### A01 icon direction

Use a compact period field compass with a clearly redirected route marker and a small worn metal star.
The silhouette should suggest competent navigation after a route changes.
Avoid text, tiny maps, country flags, and a generic trophy cup.
The completed icon uses the unchanged canonical achievement frame and a distinct central subject.

## A02: coalition growth through revisions

| Field | Design |
| --- | --- |
| Stable proposed ID | `chaosx_rule_coalition` |
| Working label | A Coalition That Holds |
| Visibility | Visible from the start. |
| Difficulty | Hard. |
| Eligible actor | An independent human faction leader with at least three independent faction members including itself, spanning at least two ideology groups. |
| Trigger to arm | A verified Rule transition changes an effective faction, guarantee, military-access, or intervention gate for the player or an existing independent member. |
| Time window | 540 days. |
| Minimum continuity | 270 days after the attempt begins. |

Snapshot all independent faction members when the attempt begins.
Every snapshotted member must remain independent, uncapitulated, and in the same faction throughout the attempt.
The player must remain faction leader.
During the attempt, recruit at least two additional independent countries that were outside the faction when it began.
At completion the independent membership must span at least three ideology groups.

At least two distinct qualifying native rules must change during the attempt, including the arming change.
At least one qualifying row must be a genuine revision of a rule touched by an earlier Event 104 firing.
Both changes must affect a current member's applicable diplomatic or intervention options.
At least one of the two new members must join after that revision.
All conditions must coexist on or after day 270 and no later than day 540.

Member independence and faction entry must result from actual campaign actions.
Creating two puppets and adding them does not qualify.
A released country is eligible only if it is genuinely independent and joins through a supported action, with no test fixture or artificial achievement-only bypass.
The player can use ordinary diplomacy, political change, military circumstances, or the newly available rules to achieve the required coalition.

This achievement recognises keeping an established coalition intact while expanding it across political differences under a changing rule set.
It uses the actual faction and diplomacy systems.
It does not add faction cohesion, a special negotiation currency, or a Rule-specific recruitment action.

### A02 tracking

Snapshot faction identity, original independent member identities, start date, start receipt, and ideology groups.
Record ordinary join, leave, faction dissolution, leader-change, independence, and capitulation events for those identities through existing hooks.
Keep the identities and join dates of qualifying new independent members.
Record the two distinct qualifying rule identities and the revision receipt.
At each relevant membership or rule change and at day 270, evaluate current ideology breadth and all continuity conditions.
Expire at day 540 if incomplete.

An original member's temporary departure fails the attempt even if it rejoins later.
An original member's ideology change is allowed if the required final diversity remains.
A new member that leaves before completion does not count among the required two.
Disqualification ends only the attempt and has no additional diplomatic effect.

### A02 icon direction

Use five visibly distinct linked metal fittings around a single small centre, with one repaired joint.
The composition should remain readable as a durable alliance at 64 by 64 pixels.
Avoid a map full of flags, heraldry copied from a live faction, text, and extra interface decoration.

## A03: victory after a substantial reshuffle

| Field | Design |
| --- | --- |
| Stable proposed ID | `chaosx_rule_cascade_victory` |
| Working label | Victory Without a Stable Rulebook |
| Visibility | Hidden until Evolution IV has actually unlocked in the campaign, then reveal its goal through the existing achievement interface. |
| Difficulty | Very Hard. |
| Eligible actor | An independent human country already fighting an enemy classified as a major when the attempt begins. |
| Trigger to arm | An Evolution IV occurrence commits at least four meaningful rule changes, including at least two genuine revisions, across at least two consumer families. |
| Player-impact gate | At least two distinct changed rules materially affect the candidate player in that batch. |
| Victory deadline | 365 days from the qualifying cascade. |
| Post-victory continuity | 90 days. |

The player must win one of the frozen qualifying ongoing wars against an enemy that was a major in that war at the start of the attempt.
Their preserved contribution must be at least 25 percent of their winning side's contribution in that war.
They must remain independent and uncapitulated from the qualifying cascade through the post-victory check.
At that final check they must control at least 75 percent of the fixed state set they owned and regarded as cores at the cascade.

At least four historically Rule-touched native rules must still have non-default current options at the final check.
They do not have to retain the exact options from the qualifying cascade.
Later legitimate revisions are part of the challenge.
An externally restored default cannot count among those four.
The victory must occur by the inclusive day-365 deadline, but its 90-day continuity check can complete afterward.
The maximum lifetime of an otherwise valid attempt is therefore 455 days.
With no timely qualifying victory, expire the attempt only after that inclusive window has closed.
A victory on day 366 is too late and cannot revive the expired attempt.

The same receipt cannot satisfy a second attempt for the same player after a reset.
A later independently qualifying IV cascade can start a new attempt once the previous attempt has failed or expired.
If a qualifying cascade occurs while an attempt is active, it can contribute to the actual campaign but does not reset the deadline or replace the starting conditions.

### A03 tracking

Preserve the qualifying IV receipt, verified change count, revision count, family set, and the two player-impact witnesses.
Snapshot the frozen qualifying war set, enemy majors per war, nonempty original owned-core state set, and player identity.
Schedule a generation-bound victory-expiry check at the first supported point strictly after the inclusive day-365 window.
Use one documented campaign-date convention and capture all qualifying results through the deadline before an expiry callback can reject the attempt.
At a timely victory, preserve the result, its date, and contribution before the war state is retired.
Schedule one generation-bound post-victory check for 90 days later and mark that continuity phase explicitly.
The victory-expiry callback must preserve a valid pending continuity phase, including a deadline-day victory whose final check falls on day 455.
It cannot retire that phase merely because day 365 has passed.
Read current native rule options for the four-rule final condition.
Use touched provenance without replaying historical mutations.

### A03 icon direction

Use a battered rulebook clasp crossed by a small campaign laurel, with several shifted metal tabs visible behind it.
The object should communicate a victory achieved amid repeated changes.
Do not use readable writing, a modern office binder, a pile of tiny pages, or the same compass motif as A01.

## Tracking architecture

Use existing achievement callbacks, rule commit receipts, war results, faction lifecycle hooks, and bounded delayed checks.
At most one active attempt per achievement per eligible player is needed.
The design does not require daily iteration through all countries.
Delayed checks carry an attempt generation and reject stale callbacks after failure, expiry, country switching, or a new attempt.

Cross-country snapshots use validated stable country identities and explicit handling for annexation or release.
Original core ownership uses a fixed state set captured at arming.
Adding new cores later cannot reduce the denominator or manufacture a pass.
If a state is legitimately split or its identity changes through an update, migration must preserve the original challenge meaning or retire the attempt without granting credit.

The war-contribution ratios are evaluated using stored numerator and denominator values from the same war result.
If the denominator is zero, missing, or unresolved, the ratio does not pass.
Round only for display, not to cross the 20 or 25 percent threshold.
The achievement UI can show rounded progress while the actual gate uses the supported precise comparison.

## Asset and localisation handoff

Each achievement requires one original completed 64 by 64 icon and the canonical grey and not-eligible derivatives.
The planned runtime basenames are the exact stable IDs above.
Use the current achievement template and preserve its frame, overlays, and state treatment exactly.
The asset prompt contains the complete paths and owner contract.

Localisation should describe the player's accomplishment and the conditions needed to pursue it.
It should not expose request IDs, hidden receipt variables, source paths, parser limitations, or test fixtures.
Hidden A03 wording must not appear as a dated evolution history entry before IV actually unlocks.
All numerical conditions in UI text must match the authored tuning and tracking contract.

## Achievement acceptance

For each achievement, verify one genuine successful path and the nearest failing boundaries.
Those include one day too late, one point below contribution, a missing distinct rule, a masked player-impact witness, a default-restored rule, a subject participant, a stale delayed callback, and a player switch.
Confirm that qualifying progress survives save and reload without duplicate awards.
Verify all three icon states in the actual shared achievement consumer.
No achievement is complete merely because its final trigger parses.
