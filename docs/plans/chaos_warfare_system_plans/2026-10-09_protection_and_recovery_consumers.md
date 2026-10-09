# Automatic protection and recovery consumers

Disposition: implemented in source, with bounded source scenarios and conditional probability evidence.
Native equipment handling, MIO completion timing and full campaign acceptance remain unproved.
The wider CBRN goal remains incomplete.

## Acceptance and behavior

The user's accepted overhaul requires automatic issue and replacement from real stock, military priority, derived readiness and usable industrial specialization.
These repairs implement those existing requirements without selecting new rewards, costs, weights, policies or maintenance intervals.

Routine maintenance serves military filters, issues military masks, services civilian filters and distributes civilian masks in that order.
The existing quarter-requirement issue increment, historical replacement reserve, civilian eligibility and annual storage schedule remain in force.
Filter service owns its completed-debit output before entering the stock helper, so proportional restoration and reduced replacement demand use the amount returned by that helper.
Population registration likewise retains the completed debit when crediting damaged material for reconditioning.
External and reserved distribution wrappers retain useful-delivery output through their internal helper before testing proof and aid credit.
Outer callers consuming public temporary outputs retain their own declaration obligation.
Reconditioning retains recovered output before its existing positive-batch guard and 20/80 defective/safe quality roll.

Vehicle Recovery Teams immediately refreshes the stored contamination-related truck penalty in the completing country's controlled states.
The common MIO callback is inherited by ICI, DuPont and Montecatini.
Its existing helper recomputes from contamination strength and the current controller's trait, so duplicate refreshes and multiple organizations do not stack the reduction.
New contamination, cleanup and control changes retain their existing paths.

## Implementation evidence

| Surface | Files and evidence |
| --- | --- |
| Eight protection callers and maintenance order | `common/scripted_effects/cbrn_protection_effects.txt`, `common/scripted_effects/cbrn_protection_decision_effects.txt`, [owner handoff](subagent_handoffs/2026-10-09_automatic_protection_repair.md) |
| Existing MIO reward callback | `common/military_industrial_organization/organizations/cbrn_chemical_protection_organizations.txt`, explanatory comment in `common/scripted_effects/cbrn_designer_effects.txt`, [source receipt](../../testing/2026-10-09_mio_vehicle_recovery/source_results.json) |
| Helper contracts and mechanic guides | `common/scripted_effects/cbrn_scripted_effects.md`, `docs/systems/cbrn_warfare/cbrn_simplification.md`, `docs/systems/cbrn_warfare/cbrn_designers.md` |
| Neighboring unit-family documentation | `docs/events/019_infantry_spawn/systems/unit_family_coverage.md` lists the twelve retained support roles and provider-521 combat role, and refers to the current CXT registration contract. Obsolete aggregate combat/support counts are omitted because this bounded review does not reclassify every other family. |
| Remaining source review | [Completion audit](subagent_handoffs/2026-10-09_remaining_source_gaps.md) distinguishes the repaired MIO callback from continuing-protection, historical-start and project-validation questions. Its preliminary missing-burn-hook finding was withdrawn after tracing the event caller. |

No event-log, event-detail, evolution-detail or cluster prose changed, so this tranche requires no event catalog edit or CSV export.
Existing public descriptions still describe the same rewards and requirements.
No asset or GUI layout was changed.

## Meaningful validation

`node docs/testing/2026-10-09_automatic_protection_repair/automatic_protection_source_tests.js` passes 58 scenarios using actual before/after helper ASTs and the unchanged conservative helper-lifetime model.
The fixtures cover zero, partial and full service stock, all five mask models, registration recovery, shared military/civilian shortage, historical reserve behavior, maintenance timing, distribution proof and both reconditioning outcomes.
In the competing-stock fixture, 90 crates go to the under-equipped army before civilian servicing.
In the worn-filter fixture, partial and full service raise derived readiness from 27.5 to 41.25 and 55 respectively.
These are declared source-model results, not observed game values.
The tests retain ten unchanged helper bodies and the exact original reconditioning guard and weighted body.
Native stock operations, initialized country/state data, ancillary no-ops and refund-entry limits are explicitly documented in the owner handoff.

`node docs/testing/2026-10-09_mio_vehicle_recovery/source_tests.js` passes 15 scenarios using the actual MIO callback, current trait predicates and existing state recalculation helper.
It reproduces the original stale penalty and covers the generic and three inherited organizations, occupied and foreign-controlled states, clean states, repeated refresh, multiple MIOs and control transfer.
At the declared strength of -0.8, the stored truck-attrition input changes from 0.6 to 0.33 and stays 0.33 after another refresh.
The MIO AST is otherwise unchanged, including all weights, bonuses, prerequisites and equipment limits.
All designer-effect bodies are unchanged.
Native scope iterators, completed-trait predicates and modifier refresh are modeled dependencies.
The parent reran both suites in the extracted isolated commit candidate, with all 58 and 15 scenarios passing.
That candidate also preserves the exact frozen probability-source bytes, identical request fixtures and all three fully read, hash-verified conditional probability artifacts.

The [probability handoff](subagent_handoffs/2026-10-09_protection_reconditioning_probability.md) captures exact before/after sources and identical fixtures.
Both source-specific inspections find the complete two-entry pool, and evaluations retain 20% defective and 80% safe conditional probabilities.
The successful matching comparison has no unresolved items or regressions.
Its added/removed candidate records reflect source-line identity changes, with matching semantic paths and independently evaluated weights.
Those probabilities apply only when the list is reached.
The source scenarios separately establish the zero/positive recovery guard under their declared helper-lifetime model.
Standalone probability renders were stale against the workspace revision, while evaluation and comparison emitted their own visual resources.

## MCP, native scope and limits

Installed MIO documentation lines 131-149 and the offline MIO `on_complete` section at line 273 identify the completion scope as INDUSTRIAL_ORG and the country as `FROM`.
Vanilla `GER_organization.txt:117-121` uses that transition.
The installed controlled-state iterator and forced dynamic-modifier update documentation were read directly through the reference tools.
Exact paths, revisions and returned validation are retained in [MIO references](../../testing/2026-10-09_mio_vehicle_recovery/reference_and_validation.json).
The new callback's native syntax, command-kind and scope checks pass within the validator's coverage, but the scripted helper remains unresolved there, so its overall result is partial.

The parent captured matching pre/post `cbrn_protection.1` scans and scope renders.
They have the same graph revision and image hashes because the event shell is unchanged and the service defers the modified helper bodies.
The complete 54,545-byte render JSON was assembled and SHA-256 verified as `4508232be18450de99f90150cba3b91365c2d160467b2f275438fb9a15139004`.
It contains one event and its self-loop, with unresolved refresh and maintenance helpers.
The PNG was reviewed and makes no helper-lifecycle claim.
[Before receipt](../../testing/2026-10-09_automatic_protection_repair/parent_mcp_before.json) and [after receipt](../../testing/2026-10-09_automatic_protection_repair/parent_mcp_after.json) preserve this coverage boundary.
The [comparison attempt](../../testing/2026-10-09_automatic_protection_repair/parent_event_comparison.json) selected only this event with `maxChainNodes = 1` and rendering disabled.
It returned `EVENT_GRAPH_ARTIFACT_LIMIT` because the required whole graph is 96,944,773 bytes against a 67,108,864-byte ceiling, with no comparison artifact.
No source-only or diagram result is treated as native execution.

No gameplay simplification was introduced.
Native stock deltas, real event scheduling, full receipt/refund execution, complete achievement effects, MIO completion visibility and the broader campaign acceptance scenarios remain open.
The source review also leaves continuing-death protection and country-specific 1939 industry as separate implementation/evidence questions.
Skills used: `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-subagents` and the shared-tree commit workflow.
No new skill rule was needed because caller-owned temporary storage and isolated commits are already documented.
