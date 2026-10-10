# Decision Validation Tests, Improvement Addenda, and Subagent Patches

This reference holds the testing, addendum, and subagent-handoff subsections of section 19 of [chaos-redux-decisions-missions](../SKILL.md). The balance review checklist remains in [section 19](../SKILL.md#19-balance-review).

### Production action contract tests

When source contract tests cover a paid action, execute the real selector, action mapper, debit, refund, receipt, and cooldown helpers that belong to the tested path.
Restrict mocks to native primitives or explicitly out-of-scope consumers, and record those boundaries in the evidence.
Assert the actual native flag identifier, requested cooldown duration, and write count on success, rejection, refund, and repeated invocation where applicable; a mocked success counter does not prove that the production mapper has the required branch.
Do not replace a required production helper with a no-op solely to pass a loader error; fix the test loader or report the uncovered path.
Exercise the production pending-payment preflight and display/gate consumers with valid records, presence-only pointers, nonpositive IDs, actor/target or phase mismatches, and missing or nonpositive actual-paid fields, asserting display/gate agreement, no fabricated quote or fresh debit on rejection, and no durable-state mutation by the preflight.
These source tests do not establish native engine execution or timed expiry.

### Improvement addenda for decisions and mechanic windows

When an improvement addendum proposes decision depth, scripted GUI, or mechanic windows, translate the design into active play. The decision category should show the mechanic clearly, but the gameplay should still live in decisions, missions, scripted effects, scripted triggers, AI rules, and cleanup logic.

Use scripted GUI when the player needs to read or manage values that would otherwise be buried in tooltips. Good uses include influence boards, federation congresses, formable progress, patron leverage, resource routing, public fear, occult pressure, faction cohesion, reform votes, target cards, and timed crisis panels.

The addendum must choose the [presentation layer](formables-and-category-presentation.md#decision-category-presentation-hierarchy) before requesting art or controls and explain why it is the clearest option. For a justified GUI, use the [reference-image workflow](../../chaos-redux-scripted-gui/SKILL.md#reference-image-before-implementation), [content and interaction budget](../../chaos-redux-scripted-gui/SKILL.md#content-and-interaction-budget), and [background mapping](../../chaos-redux-scripted-gui/SKILL.md#background-and-reference-coverage). Do not respond to a shallow mechanic by adding meters, decisions, text, or decorative controls. Every gameplay-changing button must satisfy [GUI action integrity](formables-and-category-presentation.md#gui-action-integrity); animation must not obscure costs or compensate for weak effects.

For formables, the decision should verify the map state. Focuses may reveal claims, prepare institutions, or reduce costs, but the formation decision should prove control, legitimacy, recognition, or integration when those are central to the idea. When exact state control is the main formation proof, the addendum should use the reusable state-puzzle template and keep the visible pieces synchronized with the real eligibility helper.

The state-puzzle package is manifest-driven. Follow `templates/formable_state_puzzle/universal_state_registry_workflow.md`, generate the runtime surfaces from the complete manifest, and complete `templates/formable_state_puzzle/category_attachment_audit.md` before parent review. The audit must enumerate every category in the formable family and prove that each category metadata block attaches the exact generated `scripted_gui` whose block uses `context_type = decision_category`. Do not treat a correct state-piece render as proof that a category is attached.

When an owning event or system declares a strict all-category attachment policy, every shared or phase-specific category that exposes the formable's formation or integration decisions must attach its relevant generated state-puzzle GUI. A static category picture, text-only category, or unrelated status GUI cannot replace that state-puzzle attachment when exact state control is the formation proof. Missing category coverage is a blocker and must be recorded in the owner handoff.

### Subagent patches for decision systems

Decision and mission subagents are active small-patch agents by default inside the current task scope. They can patch varied costs, clearer dynamic localisation, custom trigger tooltips, AI target checks, cleanup hooks, visibility checks, cooldown fixes, scripted GUI button text, narrow helper call sites, and existing formable requirement fixes without waiting for a separate permission prompt.

They should not expand a whole decision system, create a new mechanic window, add a new event chain, or invent a formable suite. When the gap is broad, they should write an improvement plan under `docs/plans/<event_id>_<event_slug>_plans/` and leave implementation to the main agent.

Every patch must write a handoff with changed files, changed decision or mission ids, localisation keys, behavior before and after, meaningful validation, skipped task-specific validation, and remaining design risks.
