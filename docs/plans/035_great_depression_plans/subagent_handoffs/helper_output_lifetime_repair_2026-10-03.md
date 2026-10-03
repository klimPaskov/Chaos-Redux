# Event 35 helper output lifetime repair

## Disposition

Implemented caller-storage repair under the existing fail-closed transaction, weighted selection and owner-adapter contracts.
Native helper-return behavior and probability comparison remain unresolved.
This does not close the full Event 35 goal.

## Exact changes

The country selector initializes `great_depression_independent_target_weight` before the score helper.
The center selector initializes `great_depression_center_candidate_score` before its score helper.
New-crisis setup initializes `great_depression_center_registration_failed` to one before center registration.
Active deepening initializes `great_depression_deepening_value` to zero before amount resolution.

The humanitarian adapter initializes `famine_pressure_request_result`, `migration_pressure_request_result`, and `famine_occupation_context_proven` before the respective owner calls.
Those acknowledgements govern Event 35's one-shot receipt flags.
Owner scripts, pressure amounts, formulas, coefficients, eligibility, project counts and timing remain unchanged.

## Verification

A mechanical source scan traced direct Event 35 callees, temporary values created there, and subsequent caller reads.
It identified the four internal return boundaries above.
An extended owner review found the three external acknowledgements in the Event 35 adapter.
Actual caller-source checks confirm all seven initializations immediately precede their returning helper.
A bounded call-frame model discards callee-created storage and preserves modifications to caller-owned storage.
This proves the intended storage contract only, not production helper arithmetic, native timing, or an engine probability result.

The weighted before-source remains `audit_inputs/helper_lifetime_2026_10_03/035_great_depression_effects_before.txt`, SHA-256 `3B065E7FC529FA4E8A98B7CAF60656ECC2FD22970944B966329986B85D1B1403`.
The isolated baseline is `helper_lifetime_probability_baseline_2026-10-03.md`.
The existing complete CTR35 fixtures are retained unchanged, while the full TGT country pools and current analyzer mapping remain missing.

## References and limits

Offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, lines 435 to 442, documents temporary helper-output lifetime and caller preinitialization.
Its SHA-256 is `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4`.
Installed `documentation/effects_documentation.md`, lines 7820 to 7839, defines temporary assignment and its scope.
Its SHA-256 is `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF`.
Installed `common/scripted_effects/SWE_scripted_effects.txt`, lines 228 to 239, initializes a temporary input before a calculation-helper call.
This is a storage precedent, not independent proof of return lifetime.

The reference-context request terminated after 600 seconds.
Its narrower reference-search retry later lost its observation handle, so that result is unresolved rather than a claimed completed timeout or reference read.
Probability baseline calls timed out and the bounded center inspect returned `INTERNAL_ERROR`.
Current post-change native comparison remains blocked.
No game was launched and no live outcome is claimed.
