# Event 095 decision and mission implementation prompt

Implement the complete operation map in Part 10 and its associated military, government, foreign-support, evolution and recovery behavior in Parts 03–09 and 14.
Follow CLAUDE.md and read chaos-redux-decisions-missions, chaos-redux-events, chaos-redux-focus-trees, chaos-redux-map-states, chaos-redux-mtth and the current universal-cost and shared-price contracts.
Read the applicable offline wiki pages and installed native documentation before using an engine construct.
Do not convert the design into a collection of fixed political-power buttons with nominal effects.

Use native decision categories and missions as the normal interface.
Expose only Readiness and Cohesion as custom persistent values across the whole event.
Keep the phase budgets in Part 10, with at most six primary actions and normally three to five.
No more than three event missions are concurrent for the claimant and two for an occupier or supporter.
Do not evade the budget through additional tabs or several duplicate variants of the same operation.
Dormant claimants do not click decisions or spend nonexistent national resources before activation.

Implement claimant preparation, one Organize Region action used before and after the opening, military organization, governing settlement, national programs, foreign talks, emergency withdrawal, recovery and temporary-force settlement.
Implement occupier containment, exposed-network response, negotiation and withdrawal.
Implement sponsor liaison, exact military delivery, actual personnel return or training, and political agreements.
Relief, evacuation, reception and civilian return are the famine and migration owners' actions; Event 095 adds no copies and reads grievance states from those owners (Part 11).
Every operation requires an explicit owner, claimant, target, source variant, quote, commitment, deadline, success, failure, cancellation and cleanup path.

Use one shared operation contract for decision, focus and event-choice access to the same program.
Preserve identical material requirements and one-shot outcomes.
Native opportunity costs must be disclosed and cannot double-charge the same explicit setup payment.
An already completed focus or decision receipt prevents a second reward from the alternative interface.
An inherited meaningful tree remains intact, while all essential restoration programs are available through these operations.

Calculate the quote from current actor resources, the exact target, supported equipment variants and current shared pricing.
Use that same quote for display, inclusive affordability, actual debit and refund.
Distinguish actual paid, reserved, delivered, captured, destroyed and refundable amounts.
Do not use a helper that mutates an input value as proof that the requested amount was successfully paid.
Do not double-charge native costs through a custom effect.
Do not offer refunds larger than actual eligible payment.

A port, supplied army, local organization, diplomatic access or Cohesion threshold is a condition rather than a resource price.
Keep at most four spendable resource types per action and command-power costs no higher than 60.
Use real icons and the compact cost-display limits from the skill.
The baseline shipment is resource-scaled and capped by both recipient need and donor surplus.
No decision creates tanks, ships, veteran formations, food relief or civilian transfers from political power alone.

Use ordinary 100-day missions for small attainable goals, 150–180 days for substantial or difficult campaigns, and 30–60 days only for a real immediate battlefield emergency.
Operations with 35- or 70-day work periods retain their actual start and completion state.
Mission success completes automatically when the exact objective is met.
Deadlines do not reset on save/load, category visibility or target reselection.
A target changing hands revalidates the task and never issues a duplicate state, unit or building reward.

Route physical civilian movement and deaths through the separate current shared owners with exact proof.
A state transfer is not migration.
A military recruit is not a civilian casualty.
Maintain actor, owner, controller and source/destination identity through nested calls, initializing every temporary output and retaining durable operation IDs for delayed work.
Use bounded tracked-state callbacks and the existing active scheduler rather than adding a worldwide recurring scan.

Implement AI target selection independently from human selectors.
Use the priority matrix and scenario plan in Part 12.
Use `chaosx_ai_probability_auditor`, with the probability tools where they support the adapter, for the actual weighted action and timing surfaces.
Retain baseline/candidate and scenario inputs, and label calculations from the script as such rather than as tool evaluation.

Write final decision, mission, report and tooltip copy from the concrete effects after implementation.
Use the available interface tools, or source review where they are unavailable, for blocked, affordable, exact-equality, in-progress, completed, failed, expired, cancelled and multi-actor states; the user runs live tests.
Report changed paths, operation IDs, exact cost and refund proof, mission and AI evidence, reference reads and unresolved blockers.
Do not mark the system complete while a promised transfer, settlement, cost path or recovery action remains a placeholder.
