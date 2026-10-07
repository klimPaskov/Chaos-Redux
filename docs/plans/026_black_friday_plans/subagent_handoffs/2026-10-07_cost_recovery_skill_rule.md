# Cost recovery skill rule handoff

Disposition: `implemented` for the bounded skill maintenance assignment only.
Acceptance basis: the parent's explicit request to capture two observed reusable safety rules with at most about eight logical sentences, preserve the shared tree, and supply this handoff without staging or committing.

## Changed files and identifiers

- `.agents\skills\chaos-redux-events\SKILL.md:192-195`: four sentences under `Helper output lifetime`, following the existing record-consumption transaction guidance.
- `.agents\skills\chaos-redux-decisions-missions\SKILL.md:242-243`: two sentences under `Custom-cost affordability and payment`.
- `.agents\skills\chaos-redux-decisions-missions\SKILL.md:1000`: one sentence under `Production action contract tests`.
- This handoff is the only documentation file created outside those two skills.

No skill names, headings, gameplay IDs, helper identifiers, localisation keys, routing contracts, or runtime definitions were added or renamed.
Skills used: `skill-creator`, `chaos-redux-subagents`, and the two existing skills being maintained.
Created skills: none.
Updated skills: `chaos-redux-events` and `chaos-redux-decisions-missions`.
Left unchanged: `chaos-redux-subagents`, AGENTS.md, generated runtime definitions, and the existing inclusive affordability guidance.

## Coverage decision

The event skill already distinguishes validator state from a fresh consumption receipt and requires actual-source transaction tests, but did not cover preserving an unvisited queue suffix at the native loop ceiling or rotating unresolved popped rows behind it.
The decision skill already requires a shared inclusive affordability predicate for availability, native cost gating, and resource colour/display selectors with matching payer, quote, units, and equipment token, including below/exactly/above-cost checks.
That exact affordability rule was retained without duplication.
Its finite-registry preflight guidance did not cover malformed pending-payment pointers, record identity and phase, or the existence and positivity of the actual-paid field, so only that gap and its production-test cases were added.
Both additions are generic and contain no event or mechanic names.

## Meaningful validation and evidence limits

Before editing, both skill files were already modified in the shared tree.
Comparison of the reviewed sibling copies against the pre-edit files showed only five added lines in the event skill and four added lines in the decision skill, comprising seven logical sentences and two paragraph separators.
Removing exactly those additions reproduced the original bytes and SHA-256 hashes for both files, preserving all prior edits and existing mixed line endings.

Pre-edit SHA-256 evidence:

- Events: `D5277B6B5BF13F0EDA8C97C1301AB79BDB2856052B4FA7AAA90687EA79228C55`.
- Decisions: `CEFA08F61CB0F73EE1D6918A0F88189D39CDA026F1D69479587C2FCB335A0696`.

The normal apply_patch write failed twice without changing either original.
Following the existing event skill's sibling-file recovery guidance, task-owned sibling copies were patched with apply_patch, verified against those baselines, and installed through native PowerShell Move-Item only after rechecking the exact original hashes and confirming both resolved paths were in the same owned skill directory inside the repository.
Each replacement was re-read and matched the reviewed sibling's SHA-256.
The task-owned sibling copies were consumed by replacement and are not deliverables.

Both skills passed the official validator using:

```powershell
python -X utf8 'C:\Users\klimp\.codex\skills\.system\skill-creator\scripts\quick_validate.py' '.agents\skills\chaos-redux-events'
python -X utf8 'C:\Users\klimp\.codex\skills\.system\skill-creator\scripts\quick_validate.py' '.agents\skills\chaos-redux-decisions-missions'
```

The first validator attempt without UTF-8 mode passed the event skill but encountered a cp1252 decoding error for existing decision-skill text.
UTF-8 mode resolved that tool invocation issue without changing the validator or rewriting existing text.
Manual coverage review confirmed that the added rules require suffix and receipt preservation, pop-before-recovery rotation, acknowledged receipt cleanup, exact pending-record preflight, rejection without fabricated quotes or fresh payment, and production consumer agreement with a pure preflight.
The observed behavior and tested queue strategy were supplied by the parent.
No gameplay fixtures, engine validation, MCP scenarios, or live-game tests were executed by this documentation-only assignment, and the added test instructions are not claims that those cases were run here.

## Parent integration

Review and isolate only the three skill hunks reproduced below plus this handoff for the parent commit.
Do not stage the complete skill files indiscriminately because their pre-existing changes belong to other work.
No index-mutating commands, staging, or commits were issued.
The index hash changed during shared activity from `996CAED808957937B377A9C2FE2EB935151000E0A777DCD11E86772014C229BC` to `9209E519273095B6059C90D77A34F8A5F074F704BB9A15CC1009353432C39317`, so no claim is made that the global index remained unchanged.
No gameplay, assets, workbook, framework, generated definitions, or other documentation surfaces were edited.
No AGENTS.md or subagent routing update is needed.

## Complete changed hunks relative to the pre-edit working files

```diff
--- a/.agents/skills/chaos-redux-events/SKILL.md
+++ b/.agents/skills/chaos-redux-events/SKILL.md
@@ -189,4 +189,9 @@
 Clear the fresh receipt immediately before the consumption attempt, set it only on the exact row mutation, and gate irreversible effects and compensation on that receipt so rejection cannot undo a pre-existing tombstone.
 Actual-source fixtures must exercise already-used or tombstoned rows, transitions to used or tombstoned between validation and consumption, and stale receipts from earlier calls, asserting no irreversible effect or rollback of prior state on rejection and exactly one authorized effect on fresh consumption.
 
+Native effect loops stop after 1,000 iterations, so pending-queue recovery must preserve the unvisited suffix and every unacknowledged receipt rather than clear the whole queue and rebuild only visited rows.
+Process a bounded batch by popping each selected row before recovery and appending unresolved rows behind the unvisited suffix, without adding a world scan.
+Clear a receipt only after its matching recovery is acknowledged.
+Actual-source fixtures must enforce the native loop ceiling and verify more than 1,000 queued rows across repeated invocations, unresolved-row rotation, and receipt preservation.
+
 ## Event anatomy
```

```diff
--- a/.agents/skills/chaos-redux-decisions-missions/SKILL.md
+++ b/.agents/skills/chaos-redux-decisions-missions/SKILL.md
@@ -239,4 +239,7 @@
 Do not copy strict, deprecated, or inexact reserve/equipment predicates into display logic.
 Check agreement just below, exactly at, and just above the quoted cost.
 
+For pending-payment actions, use one authoritative pure preflight for cost display, hover text, and availability that requires a positive record ID, matching actor and target, the correct transaction phase, and an existing positive actual-paid field.
+A pointer's presence alone must neither expose a pending-payment quote nor authorize fresh payment when the referenced record is malformed.
+
 For fractional dynamic quotes, show enough decimals in every cost row and tooltip to match the actual debit. Keep any display cache separate from fresh availability and debit calculations so a rounded or stale quote cannot govern payment.
@@ -994,4 +997,5 @@
 Restrict mocks to native primitives or explicitly out-of-scope consumers, and record those boundaries in the evidence.
 Assert the actual native flag identifier, requested cooldown duration, and write count on success, rejection, refund, and repeated invocation where applicable; a mocked success counter does not prove that the production mapper has the required branch.
 Do not replace a required production helper with a no-op solely to pass a loader error; fix the test loader or report the uncovered path.
+Exercise the production pending-payment preflight and display/gate consumers with valid records, presence-only pointers, nonpositive IDs, actor/target or phase mismatches, and missing or nonpositive actual-paid fields, asserting display/gate agreement, no fabricated quote or fresh debit on rejection, and no durable-state mutation by the preflight.
 These source tests do not establish native engine execution or timed expiry.
```

## Simplifications, omissions, and blockers

No simplifications or omissions in the requested skill update.
No remaining blocker for the documentation assignment.
Parent review and an isolated parent commit remain with the parent, and gameplay or runtime completion is outside this handoff's claim.
