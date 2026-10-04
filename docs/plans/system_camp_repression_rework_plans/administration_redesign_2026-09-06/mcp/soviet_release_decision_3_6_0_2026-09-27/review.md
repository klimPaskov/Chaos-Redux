# Soviet prisoner-release decision inspection

Status: bounded current-source decision MCP result; native availability, click, PP refund and survivor receipts remain unproved.
Installed HOI4 MCP 3.6.0 accepted an exact-ID `hoi4.decision_inspect` with three declared scenarios and returned `DECISION_ANALYZED_PARTIAL` at source revision `96e7a779b0103078c73fbab4f67feaf14ed1e4d69084514a2f7e56e36f4b0774`.
The [manifest](manifest.json) verifies the exact request/result wrappers and original authoritative 515,155-byte JSON artifact.

The declared SOV wartime scenario with a candidate living Gulag, the SOV no-custody case, and the GER invalid-actor case all resolved the native cost to 45 Political Power and marked it affordable at the stated 100 PP.
The invalid GER actor was excluded; the two SOV `available` gates remained unresolved.
The adapter does not bind this source's `any_of_scopes` and `all_of_scopes` custody arrays from these fixtures, and the scenarios did not declare the cooldown flag. Each SOV decision gate therefore reports those three unresolved inputs.
Its score-only decision model returned raw `ai_will_do` 40 for the two SOV fixtures with unresolved eligibility and zero for the excluded GER actor; no AI click probability follows.
The source-tested [release contract](../../soviet_release_integrity_2026-09-27.md) separately verifies the row preflight, one positive release receipt before policy relief, refund and cooldown guard with mocked engine primitives.
This MCP result does not prove those effect-time consequences in Hearts of Iron IV.
