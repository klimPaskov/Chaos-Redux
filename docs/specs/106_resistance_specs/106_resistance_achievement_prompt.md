# Achievement implementation handoff for 106 Resistance

Implement the two achievements defined in `106_resistance_spec_part_4_aftermath_chaos_and_achievements.md`, with the asset requirements in Part 5 and the T-series tests in Part 6. Complete the current full source-reading gate first and inspect the actual achievement registry, eligibility rules, lifecycle hooks, and nearby current examples. The proposed IDs below become stable after collision verification.

## `chaosx_106_containment_mastery`

Use an existing eligible human occupier. Its entry wave must be active Stage II or III, nominally +75 or +100, and must actually add at least 50 points in at least five occupied states.

Freeze every positively affected occupied state under that country in the first qualifying wave, including any beyond the five-state minimum. At days 180 and 270 of a valid attempt, every original member must remain a valid occupation under that country with resistance at most 25 and compliance at least 40. Direct control is continuous through the attempt. A lost, released, transferred, cored, omitted, or otherwise invalid original member fails the attempt.

The cohort never shrinks or swaps in new conquests. A later qualifying restart uses the same original cohort, requires every original member to be a valid occupation under the player again, and requires at least five original members to gain at least 50 actual points in the new wave. Do not silently reset an active attempt's dates on every wave.

Resistance and compliance are checked at two stated observations. Continuous control needs real lifecycle evidence. Do not describe or implement uninterrupted low resistance based only on those observations.

Run a due observation and any earned completion once before a new 106 write at the same elapsed-day boundary, following Part 4's finite due-record contract. A completed achievement is not clawed back by the new wave. A missing older checkpoint cannot be replaced by a later favorable state.

## `chaosx_106_home_recovery`

Use an existing independent eligible human country with hostile occupation of its cores. The entry wave has nominal addition at least 50, at least three occupied core states each gain at least 25 actual points, and at least 100 actual points are added across its affected occupied cores. Freeze every positively affected occupied core from that first qualifying wave.

A later 095 firing must commit a genuine armed outcome using a valid positive 106 receipt from at least one original member. The proof names the state, occupation and movement relationship, receipt, 095 transaction, and actual outcome. A selected candidate, attempted release, native-only uprising, or rejected receipt does not satisfy this condition.

095 freezes validated local provenance before its political or military mutations. After physical success, that frame supplies the achievement link even when the outcome's own control-change callbacks have already retired the old live episode. Do not reread retired support as if it had to remain usable after successful restoration.

The player must recover direct ownership and control of the full original cohort. At least two original members must be recovered through that country's own hostile control changes during its war against their occupying side. Gifts, peaceful transfers, release effects, and allied control do not supply those two proofs.

Remain independent and on the supported existing human-control route. Hold the full set for 180 days after full recovery and peace with surviving recorded occupiers and hostile 095 actors, whichever condition is met last. A lost state or resumed relevant war resets the final hold. Ceding a state or changing its core status never shrinks the original requirement.

Losing independence or the eligible human-control route permanently fails this achievement attempt for the rest of the campaign. Retain its immutable cohort and closed identity. Restored independence, a returning player, a fresh wave, and old callbacks cannot restart it or reuse its prior recapture and 095 proof. This terminal failure is separate from an ordinary lost state or renewed war resetting only the hold.

The two own recaptures deliberately permit another member of a minimum three-state cohort to be restored through 095. Do not change this into a demand for deliberate loss and recapture.

## Shared tracking contract

Retain at most one immutable cohort per achievement per eligible human country. Keep original dates, membership, hostile-control proof, continuous eligibility, and armed-outcome evidence separate from the three-receipt 365-day uprising-support buffer. An old proof never refreshes usable local support.

Use verified state-control, ownership, core, subject, human-control, peace, and country-lifecycle contracts. Resolve actual tag and package identity rather than trusting a stale country pointer. Caller-owned temporary outputs begin at zero and distinguish fresh committed proof from an already-used return.

The existing 095 runtime is legacy and has no 106 history reader in the inspected revision. Implement and validate the Part 3 consumer and physical armed-result proof before enabling the homeland achievement. If a required continuity or hostile-recapture detector is unproved, leave the corresponding acceptance gate blocked. Do not replace it with an event-fired flag or an endpoint snapshot.

Apply the current project's test/debug and achievement-eligibility rules. Synthetic fixture firings are not earned campaign progress. Verify any needed firing-origin distinction before enabling unlocks.

## Text, art, and evidence

Write final titles and descriptions from Part 5's directions only after the real conditions are wired. Keep them ambitious and clear about the full affected footprint and the meaningful player actions. Route all final text through `chaosx_localisation_auditor`. This prompt supplies no pasteable title or description.

Coordinate the two completed, grey, and not-eligible icon triplets with the asset prompt. Registered IDs and filenames must match exactly. Validate all native-size consumers.

Return the exact registry and source changes, cohort and hook contracts, saved-state behavior, duplicate handling, T01 through T12 evidence, icon references, and all remaining blockers. The parent reviews the full source and actual evidence before claiming achievement completion.
