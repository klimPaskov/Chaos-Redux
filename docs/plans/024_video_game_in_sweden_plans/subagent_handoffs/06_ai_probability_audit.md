# Event 24 AI and probability audit handoff

## Scope

The probability role reviewed opening `ai_chance`, route selection, ordinary actions, evolution openings, emergency behavior, and the named scenario matrix.

## Named scenarios

The final matrix is `P24_FINAL_OPENING_MATRIX` with `P24-O1` stable peace, `P24-O2` low-experience domestic pressure, `P24-O3` wartime high Chaos, and `P24-O4` severe instability with supply and core-loss crisis flags.

## Findings and parent integration

Route-specific weights remain explicit for the three openings and action routes. The maximum-risk route is suppressed by near capitulation, broken supply, severe instability, and severe campaign crisis checks.

The emergency matrix showed the controlled route dominant in `P24-O4`, and the commercial route factor was reduced to zero for the emergency crisis branch so it cannot outrank the bounded response.

## Validation

The opening candidate pool was complete for all three options, and the named evaluation completed with four scenarios and one bounded diagnostic indicating that the supply modifier on the commercial opening was inactive in the supplied scenario set.

## Remaining risks

The full probability comparison timed out in the large workspace after the final emergency factor change, so the final report preserves the successful inspect and evaluation evidence and records the comparison timeout rather than claiming a completed comparison artifact.
