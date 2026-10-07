# Event 006 bilateral progress repair

Disposition: implemented at source, callback regression checked, native result unobserved.
Acceptance basis: the accepted foreign-reaction contract requires one recognition award for a pair and released-country generation and one reward for an actual guarantee.
The user authorized continued full Event 006 implementation and recommended implementation choices without waiting for input.

## Corrected behavior

DM12 records the former-host endorsement before progress and awards Recognition only for a new receipt.
Formal host-outcome settlement, Legitimacy gain and Instability reduction retain their independent effects after a prior endorsement.
DM16 records its selected member's receipt before Recognition, with both countries' Network progress and League effects preserved after an earlier endorsement.
DM34 consumes a copied guarantee result and awards Recognition and Security only for a new guarantee.
Capacity, patron channel, aid, concessions, political tradeoffs and host pressure remain the independent treaty result.
This attribution implements the existing once-per-guarantee reward contract and introduces no new cost or numeric balance baseline.

DM13, the foreign recognition stance and the foreign guarantee stance initialize the temporary result before calling the shared helper.
DM12, DM16 and DM34 also initialize the output they consume.
Caller-owned storage keeps helper modifications under the documented conservative temporary-variable lifetime.
The helper API comments specify this requirement.

The three settlement tooltips state the conditional rewards and distinguish the selected member's Recognition from the payer's.
The refusal sentence remains tied to the acceptance conditions, and the treaty cancellation sentence describes negotiation failure.

## Evidence

The scripted-system architect's [baseline and owner review](006_bilateral_foundation_foreign_queue_review_2026-10-07.md) identifies and closes the four source findings.
The localisation auditor reviewed the three tooltips, and the owner applied its refusal, beneficiary and negotiation corrections.
Nine actual callback AST cases are retained in [the regression evidence](../evidence_20261007/bilateral_progress_regression.json).
The model uses declared external eligibility and helper/ledger API stubs, scoped persistent receipt state, and temporary callframes that discard storage created only in the returning helper.
It is a caller-logic regression check, not a native engine, generation-reuse, timing, full affordability or campaign-eligibility test.

Before the patch, prior endorsements still grant 25 Recognition in DM12 and 15 in DM16, and an existing guarantee still grants 10 in DM34 in those source cases.
After the patch those repeat gains are zero, while the first awards remain 25, 15 and 10.
Under conservative helper-output cleanup, DM13 and the foreign recognition/guarantee stances regain their intended first awards of 15, 10 and 15 after caller initialization.
Network/League behavior in DM16 and treaty Capacity in DM34 match their before-source cases.
Four decision AST comparisons preserve visibility, availability, cost display and affordability, duration, cooldown, initial payment, cancellation and AI blocks.
No AI weight or probability expression changed.

The parent used the connected source-location lookup for decision line 996, then navigated the returned decision and keyPath to the member callback.
The exact paths, source spans and revisions are retained in [the reference reads](../evidence_20261007/bilateral_reference_reads.json).
Offline Data structures lines 435-443, revision 62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4, provide the temporary-variable boundary caveat.
Installed effects documentation lines 7820-7827 and 4565-4573, revision 2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af, cover set_temp_variable and give_guarantee.
The existing shared helper and initialized caller patterns are retained, with no substitute scope or new global target.

Whole-decision script validation timed out after 600 seconds, and the parent retried the changed receipt snippet under explicit country scope.
The snippet result and its check coverage remain separate from source regression and native behavior.
It returned `SCRIPT_CHECK_PARTIAL`, `valid = null`, with four supported native command-kind/scope checks, three unchecked native argument blocks and two unresolved mod-helper calls.
The actual helper bodies and their caller scopes were reviewed separately, and no full native validation is claimed.
The validation output is retained in [the script-check evidence](../evidence_20261007/bilateral_script_validation.json).
The detailed temporary-lifetime reference read timed out at 600 seconds, so the parent retried only the answering line with explicit wiki source.
The local Variable types section was read directly before editing, and the live section search supplied its exact revision and span.
No assets or catalog detail wording changed, and no new UI, country, decision, mission or recurring hook was introduced.
No simplification was made in this repair.
The full Event 006 goal remains incomplete, including the pending focus/signature/formable source tranches and their wider evidence gates.
