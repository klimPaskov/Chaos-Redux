# Event 32 evolution timing intent matrix

Accepted basis: the parent task and spec part 4 eligibility take precedence over matrix shorthand.
These are named test conditions, not probability results or new balance targets.
The native event architecture remains under parent review.

All cases use one declared GER host, explicit current global flags, all pending flags false, and no scheduled external state change over a 365-day review horizon.
The pressure values are stipulated at the measurement boundary.
Dynamic registry/site derivation and engine date encoding remain unresolved.

| ID | Declared setup | Intent | Classification |
| --- | --- | --- | --- |
| EVO-01 | Rogue: two vulnerable operational programs at Gathering Storm | Eligible, pressure should shorten ordinary pacing. | Unresolved timing |
| EVO-02 | Rogue: one secure stable program | Ineligible: no vulnerable program. | Unresolved timing |
| EVO-03 | Guidance: three launches, two low-readiness programs at war | Eligible, pressure should shorten ordinary pacing. | Unresolved timing |
| EVO-04 | Guidance: one maintained program, few launches, high readiness, overstocked | Eligible through overstocking, ordinary pacing should lengthen with one program. | Unresolved timing |
| EVO-05 | Saturation: four mature operational programs, two at war | Eligible, near the accepted ordinary base target. | Unresolved timing |
| EVO-06 | Saturation: one early experimental program | Ineligible: operational count and share fail. | Unresolved timing |
| EVO-07 | Special Warheads: two programs and no payload owner | Ineligible: no supported payload owner. | Unresolved timing |
| EVO-08 | Special Warheads: two nuclear payload owners | Eligible, pressure-sensitive pacing. | Unresolved timing |
| EVO-09 | Automatic Retaliation: one responding hostile endpoint below 900 chaos | Ineligible: chaos threshold fails. | Unresolved timing |
| EVO-10 | Automatic Retaliation: one responding hostile endpoint at 900 chaos | Eligible with world_end absent. | Unresolved timing |
| EVO-11 | All five tracks disabled in an otherwise qualifying world | All five tracks must remain inactive and produce no unlock record. | Unresolved timing |
| EVO-12 | All five tracks already unlocked and recorded | All five tracks must remain inactive with no duplicate record. | Unresolved timing |
| EVO-PACE | First high-chaos pulse with all five tracks eligible | Baseline setup precedes unlocks and five popups must not occur on the same day. | Unresolved timing |

EVO-02 is ineligible because its single secure program supplies zero vulnerable programs.
EVO-04 is explicitly overstocked, with reserve 12 and capacity 8, despite high readiness and one launch.
EVO-05 fixes the war-program count at two, below the current shortening threshold of four.
EVO-11 and EVO-12 cover all five existing disable and unlocked flags respectively.
EVO-PACE preserves the first-pulse input without proposing new native event cadence.

The five accepted base targets are Rogue 120, Guidance 105, Saturation 90, Special Warheads 120, and Automatic Retaliation 150 days after eligibility.
Native timing comparisons must use the saved scenarioSet.json bytes and report any unresolved new binding, rather than silently rebuilding this matrix.
