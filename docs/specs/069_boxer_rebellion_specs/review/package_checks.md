# Package-level review

## What this review is

This is the authoring agent's review of the specification files.
It is not an independent subagent audit, a verified game-script analysis, or a gameplay test.
No HOI4 MCP route or named project subagent ran.
The exhaustive source-reading requirement was not met, as recorded in [Source review](../research/source_review.md).

## Checks actually performed

A local Python check inspected the files and identifiers listed below.
The accompanying [machine-readable record](automated_checks.json) contains the actual results.
Identifier completeness establishes that the proposed rows and references exist.
It does not establish that their mechanics are implementable or balanced.

- Specification part sequence: PASS. Parts 1 through 16 exist once each.
- Required prompt files: PASS. Six requested implementation/production prompt types plus a separate prepared specialist handoff are present.
- D definition sequence: PASS. 46 definitions checked against 46 expected unique identifiers.
- M definition sequence: PASS. 18 definitions checked against 18 expected unique identifiers.
- B definition sequence: PASS. 9 definitions checked against 9 expected unique identifiers.
- DI definition sequence: PASS. 30 definitions checked against 30 expected unique identifiers.
- A definition sequence: PASS. 12 definitions checked against 12 expected unique identifiers.
- T definition sequence: PASS. 40 definitions checked against 40 expected unique identifiers.
- AI definition sequence: PASS. 24 definitions checked against 24 expected unique identifiers.
- Decision icon requirement coverage: PASS. All 46 decision families map once to the 30 planned decision-icon requirements. This checks the plan, not finished artwork.
- Cross-reference identifier ranges: PASS. No D, M, B, DI, A, T, or AI identifier falls outside its defined family range.
- Compact goal character budget: PASS. 3990 characters including its heading and final newline.
- Political route coverage: PASS. Three separate political route sections are present. This is not focus-graph or route-balance validation.
- Scenario type and intensity matrix: PASS. Four scenario types each have four intensity cells, giving sixteen proposed profiles.
- Runtime entry preservation: PASS. The known legacy runtime entry is retained while filenames use 069.
- Balance not represented as tested: PASS. The specification labels tuning values and future acceptance fixtures as untested.
- Source-review failure disclosure: PASS. README and source-review ledger state the incomplete reading and absent subagent execution.
- Source blob format: PASS. Recorded Git blob identities have the correct 40-character format. No new remote source lookup was implied.

## Design corrections made during this review

The visible value bands were changed to continuous ranges with thresholds at 25, 45, 65, and 85.
The earlier labels left small intervals unstated.
The local scaling formula now explicitly takes the square root of the target-to-median population ratio, with both inputs locked and positive.
The civilian construction commitment now explicitly rounds upward to a whole factory.
One transcribed focus-skill blob identity contained an extra trailing character and was corrected to the identity returned in the source response.

## Cost review

The common action contract sets a maximum of four distinct spendable or committed cost types, Command Power no higher than 60, and no more than three inline cost quantities.
The concrete Command Power amounts in the decision catalog were scanned against that limit.
The static rows and conditional template, transport, relief, and treaty bills were reviewed for the stated budget.
Conditional bills still require expansion against actual engine and shared-provider inputs before they can be certified.
This review does not prove that an equipment reservation, factory commitment, unit allocation, or treaty transfer works in the installed game.

## User-brief coverage review

| Requested content | Proposed coverage |
| --- | --- |
| Catalog and both clusters | Part 1 and shared registration in Part 12 |
| Unified, fragmented, occupied, or subject-controlled China | Parts 1–4 and the named AI/acceptance fixtures |
| Several credible centers | Part 2 state and actor selection |
| Autonomous movement and Boxer Strength | Parts 1 and 3 |
| Suppress, tolerate, and support | Parts 3 and 5 |
| Actual foreign targets and incidents | Parts 2–4 |
| Dynamic intervention with different ambitions | Part 4 and the settlement catalog |
| Boxer, foreign, and mixed victories | Part 10 |
| The Righteous Fists | Part 7, regional councils, command, and parallel institutions |
| Heavenly Protection | Part 7, three bounded schools with conventional and anomalous behavior |
| China Against the World | Part 7, Chinese coordination and postwar disagreements |
| Durable Boxer government and focus content | Parts 8 and 9 |
| Permanent route for a supporting Chinese government | Parts 8–10, additive policy and auxiliary institutions |
| Harsh occupation and long-term hostility | Part 10, with a bounded same-crisis resurgence |
| Named cross-event connections | Part 12 |
| Opening and later news | Part 13 |

This table records design coverage, not implementation completion.
The required source-review and subagent process remains unmet regardless of the table's coverage.

## Still not validated

The 24 AI fixtures and 40 acceptance fixtures are future test specifications.
None ran against an implemented Event 069 rework.
The final state manifest, carrier identity, character ownership, focus graph, limited-war behavior, scoped access, demilitarization, troop transfer, local ritual effects, and resource-transfer contracts remain unresolved or unverified.
Source-dependent portraits, flags, quotes, audio, super-event slots, and consumer-level assets are not produced or accepted.
The full current source of the linked shared systems has not been audited.

The package can be used as a proposed implementation brief with these limits retained.
It cannot be used as proof that the user's exhaustive review requirement or the event implementation has been completed.

## Final file scans

- Concrete decision Command Power amounts: PASS. 19 explicit decision-row amounts scanned. Maximum found: 30. Conditional bills still need runtime validation.
- Requested prose conventions: PASS. No em dash, semicolon, or checked prohibited stock phrase appears in the Markdown deliverable.
- Local Markdown links: PASS. 36 local file links resolve inside the completed package.
- Nonempty authored files: PASS. No empty file is included.
