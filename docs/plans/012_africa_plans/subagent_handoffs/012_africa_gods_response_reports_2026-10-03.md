# Gods response and punishment reports

Disposition: implemented and reviewed in source; native acceptance remains incomplete.
Acceptance basis: the complete Gods goal requires real transactions, meaningful reports, correct civilian loss and Deaths attribution, and localisation that agrees with the current action.
These receipts complete the existing `.604` and `.605` reports rather than introduce another mechanic window or player counter.

## Response receipts and indivisible shipments

Successful full compliance and accepted alternatives capture the actual payment family before contract cleanup.
Partial compliance captures the paid amount and exact remaining balance, while preserving its mission and deadline.
Refusal and expiry have separate receipt kinds instead of both relying on the generic failed-demand status.
The five report cases do not expose hidden settlement counters or the entire relationship history.
Receipt fields are cleared on enrollment reset, archival, and unifier-loss cancellation, and ordinary demand cleanup preserves them.
They describe the latest completed response, not a distinct historical archive for every queued popup.

The six physical-equipment families normalize full and partial quotes to whole units with the existing documented modulo helper.
A 55-aircraft quote therefore has a 27-aircraft partial and a 28-aircraft residual, which fixes the same conservation issue found earlier for odd tank quotes.
The full agreed price is preserved; only the split between current and residual shipments is integral.
Infantry, support equipment, the existing aircraft token, convoys, and trains now use native `send_equipment` through the same preflight and sole debit path, preserving actual donor stock instead of creating replacement recipient stock.
The existing infantry reserve ledger and support-focus consequence remain in their original branches.
Armour already uses native transfer; the mobile/artillery branch remains queued for its frozen subtype implementation.
Fuel and political-capital wording retain fractional precision, manpower names its native pool, and resource rights are described as a state concession rather than fractional equipment.

## Punishment outcome and country scope

The punishment receipt uses the actual capability-limited tier after any extreme-gate downgrade.
Its native political power, stability, and war-support changes are measured after minus before, including defensive relief and clamping.
The documented war-support read is `has_war_support`.
Report formatting includes sign and good/bad colouring without claiming that every nominal penalty necessarily reduced the final value.
The body requires the three stat fields before displaying numeric results.

The report audit found that owner-driven expiry and defiance review keep the host as ROOT while processing a participant.
The old population path selected the participant's state but supplied ROOT to the exact civilian-loss helper and wrote the wave flag and receipts through ROOT.
The parent fixed both sides of that mismatch by capturing the calling participant before selecting a state and using that regular event target for the supplied country and all receipt/flag writes.
This changes country attribution and prevents the participant idempotence flag from being written to the host.
It adds no population debit, disaster call, or Deaths registration.
The exact helper's temporary output fields are preinitialized in the caller so the receipt survives the helper return and following country scope.
The per-punishment population receipt starts at zero and copies only the current exact-helper result, so a historical loss cannot be reported a second time.

Local consequences use a measured positive resistance increase or the state in which sabotage effects were invoked.
The building text says infrastructure/factories were targeted, without asserting measurable damage when a selected state lacks those buildings.
Transport preparation and absence of an eligible state suppress the corresponding consequence claim.
The `.605` title also covers repeated defiance instead of asserting that every dispatch came from a broken demand.
The response and punishment sprites are reused from `interface/012_africa_event_pictures.gfx:15-16`.

## Source scenarios

| Scenario | Source conclusion |
| --- | --- |
| Full payment succeeds | The family is captured and balance is zero before demand fields are cleared. |
| Alternative succeeds | Its temporarily installed family is captured by the sole full resolver; failed payment restores the original contract and publishes no new response. |
| Odd equipment partial | 55 becomes 27 paid plus 28 due; 5 tanks becomes 2 paid plus 3 due. |
| Refusal versus timeout | Separate kinds select separate text, with the unpaid balance captured before cleanup. |
| Owner tick has host ROOT and participant current scope | Saved participant supplies the loss country, receives the wave flag and report receipt, and owns the Deaths country attribution. |
| Participant-triggered refusal | The same saved target points to the participant, retaining the legitimate direct-decision behavior. |
| Population wave was already handled | No additional helper call or loss is made, and the new punishment's population receipt stays zero. |
| Defense offsets or exceeds a nominal cost | The net signed native change shows the actual result. |
| Transport preparation protects local effects | Its receipt explains protection after the old preparation flag is cleared. |
| Selected core state gains no resistance | A zero measured increase produces no fabricated unrest claim. |
| Cleanup removes receipts but retains old history | The body chooses the unknown report instead of reviving an old tier with zero-valued stat fields. |

These are source-contract checks and the auditor's review, not executed game scenarios.
No AI weight, probability modifier, target-selection pool, or political/fuel/material price was changed.

## Evidence and open scope

The helper contract and explicit input/output/lifecycle rules are in `common/scripted_effects/012_africa_gods_report_effects.md`.
The independent source review is `012_africa_gods_response_reports_audit_2026-10-03.md`.
Its first review identified the participant/ROOT mismatch, amount-unit rendering, concrete local-consequence text, and the sprite citation; its bounded re-read confirms all four are resolved in source.
The parent then initialized the exact-loss helper's two temporary outputs explicitly and reviewed the native-transfer replacements against the installed/wiki contract and existing vanilla precedent.
Relevant paths/spans/revisions for variables, formatting, scopes, event targets, native equipment, and exact loss are in that audit and helper contract.
No new equipment, archetype, technology, focus, map, GUI, periodic hook, or asset was added.
The existing Event 012 CXT registration remains the subsystem's setup contract.
Public catalog Event Details/evolution text was not changed by these report keys.

The parent `.603` comparison and options render each timed out after 600 seconds at four-node bounds.
The narrower retries used one chain/render node, no helper expansion, and no refresh; comparison and the legal depth-one render also timed out after 600 seconds with no artifact.
An attempted depth-zero render was rejected by schema validation and supplies no evidence.
These attempts do not prove `.604`/`.605` display or helper execution.
The report auditor has no callable domain MCP routes in its own inventory and records that separate route gap.
The parent has exposed routes and remains responsible for its own required evidence.
The supplied cycle-one menu-load log predates these changes and does not establish native receipt, state, or tooltip behavior or a clean full build.

The full goal remains incomplete.
Mobile/artillery implementation, the lifecycle audit's source findings, weighted scenario/compare evidence, and native receipt/loop acceptance remain open.
No design simplification was introduced.
Skills used: events, decisions/missions, subagents, and shared Git commit; the reusable participant-scope rule is assigned to the skill maintainer.
