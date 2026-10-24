# Decision and mission implementation prompt


> **Authorization and acceptance:** The user confirmed the uploaded planning identities 115 Heroic Crusade and 116 Warlords and authorized catalog migration; the parent has installed that shared migration. This does not accept gameplay design or authorize implementation, asset production, localisation, GUI, or live testing. Do not execute those tasks from this imported prompt until the parent separately accepts the design and authorizes that scope. Follow current `AGENTS.md`, current owner skills, identifier registry, and MCP retry limits; do not launch HOI4 autonomously.

Implement every decision, mission, target variant and settlement in Part 06 for Event 115, Heroic Crusade. Read current `AGENTS.md`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-map-states` and its `references/state-ledgers.md`, `chaos-redux-mtth`, `chaos-redux-subagents`, the relevant shared helper references, Parts 02 through 08 and 12, and the acceptance matrix. This handoff is separate from the full specification and does not replace its action tables.

## Required families and paths

| Family | Required behavior |
| --- | --- |
| Formation | First charter, candidate eligibility, compatible-government proposal, acceptance, refusal, limited cooperation and first operational compact. |
| Membership | Material obligations, current access and military terms, contribution, current command, succession, withdrawal, independent adherence and genuine repudiation. |
| Campaign and client | Real target and route selection, affordable offensive preparation, viable conquered region, funded client package, current sustainment, withdrawal and local control loss. |
| Protection | Defensive promise, support for a threatened government, reception agreement, actual route protection, material aid and support for resistance under shared ownership. |
| Civilian relief | Shared-system links for detention and policy administration where appropriate, living-cohort movement, destination support, liberation, custody reconciliation and settlement. |
| Doctrine | Actual Purity proposal, supported added union, renewed assent, narrower agreement where authored, refusal, protection, departure and explicit repeal. |
| Final preparation | Current failing-gate explanation, disclosed universal charter, warning, government assent or refusal, current capability and route checks and withdrawal of a counted commitment. |
| Aftermath | Surviving clients, authority loss, protection and return choices, old obligations, terminal war continuation and final political settlement. |

Use the working names and detailed rows in Part 06 to create exact source IDs and final localisation. Preserve their trigger, visibility, target, payer, cost, duration, success, failure and cancellation meaning. The coding owner must not implement only the opening and leave ongoing opposition or aftermath as narrative text.

## Interaction and value budget

Expose bloc cohesion as the only persistent custom numeric value. Readiness is a current explanation of conditions and observed capability, not a second resource bar. Use shared Event Details and ordinary categories with a static picture and basic formatted value. No dedicated event GUI or inlay is selected.

Apply one aggregate role and phase filter. A country can be a threatened member, client, successor or ally at the same time. Display at most six primary action rows in total, counting shared-system links. Alternative labels in the design replace one another. Keep one to three meaningful active missions and prioritize immediate survival and actual obligations. Make lower-priority target choices discoverable without flooding the category.

If an accepted later change introduces richer GUI controls, re-evaluate category-picture eligibility. Remove an incompatible picture and follow the full scripted-GUI reference and native render workflow. Do not add a window merely to expose internal accounting values.

## Quote, commit and settle

Every action needs an authoritative quote identifying the actor, current authority, payer for each material, recipient, region or state, charter revision, operation family, nonce and current owner references. Separate non-consumed requirements from payments. Access, a valid route, government consent and available forces are not automatically spendable currencies.

Keep four or fewer spendable cost types per action and three or fewer inline cost icons. The full tooltip must name every cost and its payer even when it does not fit inline. Command Power never exceeds the specified 60 anchor. Every major family includes a meaningful material, industrial, equipment, manpower, supply, force, experience, stability, war support or other real commitment where designed, rather than only Political Power or Command Power.

Use the actual contribution owner's balance for payment. A recipient's reception obligation is a distinct child commitment. Timed industrial or logistics support tracks elapsed consumed service separately from future reservations. Do not grant factories to simulate rented production or double-debit a donor and recipient for one payment.

Revalidate current target, authority, charter, resources, route and capacity at commitment. A stale quote rejected before mutation releases all reservations. Partial completion settles actual expenditure and outcome, preserves real loss and releases only unused balance. Failed conservation enters the exact shared recovery path. Completion, cancellation, save load and repeated callbacks must be idempotent.

The fully read native references distinguish interface conditions from execution. Startup `allowed` can be cached, direct mission activation can bypass normal eligibility, custom cost text does not pay, and scripted removal can omit `remove_effect`. Require the current paid-operation receipt before activation or consequences and perform explicit settlement before every scripted removal. Refund actual paid components, not a new quote. Native targeted fire-once state does not replace cross-surface operation deduplication. Delayed work must also revalidate actor incarnation when a country disappears, returns or resolves through a dynamic offshoot.

The canonical operation identity includes episode, acting authority, target, family, charter revision and transaction nonce. One primary operation owns progress. Multiple donors receive separate contribution receipts. Tasks, focus completions, decisions and missions can refer to that operation but cannot create duplicate rewards or payments. If an ally completes the target first, close or transform the remaining work to a real unmet objective.

## Duration and mission quality

Use dynamic timing from actual scale, distance, route, controversy, current war, force commitment and available infrastructure. Respect the specification's local 90-day, regional 120-to-180-day and large 180-to-365-day anchors. Short 30-to-60-day emergency windows require an actual urgent event and feasible player response.

Liberation is a staged operation. Use a 180-to-245-day military phase followed by a 90-to-120-day relief phase, remaining within the 365-day combined bound. Show only the active phase as one mission. Military success is retained if relief later fails. Current custody, displacement and reception owners decide whether the relief stage actually settles.

Automatic success must depend on a verified outcome rather than a second unnecessary button. Failure must describe the real missed obligation and its bounded consequences. No catastrophic invented punishment for a route that ceased to exist, a friendly ally's prior success or an authority that no longer controls the target. Dynamic extensions or transformations must state why they occurred and preserve all previous actual costs.

## Shared-system and terminal boundaries

Use the supported disjoint cohort union and exact living records. Repression and Camps owns custody, release, forced labor and killing. The exact population endpoint and Deaths record one measured debit. Migration owns movement and reception. Resistance and Condemnation retain their source-linked ownership. No event-private camp, population, death or migration loop may be introduced.

Use Part 12's versioned source contracts. The generic loss helper's pinned output is planned, while Camp measures actual loss and its disabled-Deaths gate can block the whole transaction. Respect that gate and keep national Deaths totals separate from responsibility. The broad Resistance intake needs explicit shared adapters beyond the verified native/narrow hooks. Additive Condemnation needs accepted-action and discovery receipts; missing evidence is repaired without repeating physical work.

A partial overall relief outcome means finalized whole transfer tranches. Current custody evidence and physical transfer require complete living rows; create a supported shared split before requesting a subgroup. A primitive success, evidence token or partially completed destination credit cannot stand in for final binding and paired reception. Count positive surviving arrivals only, retain unresolved rollback state, and use durable history after corridor cleanup. The inspected corridor evacuation role requests zero route deaths. Close the identified proof comparison, minimum input, actor-binding and paid-adapter gaps before enabling dependent actions.

An actual liberation changes control but does not restore dead people, count displaced people at home or close live custody through a flag. Keep original responsibility across controller changes. Unknown or unreconciled identity data remains blocked or unclassified according to the current charter. Shared operations require their real supported metadata.

After terminal commitment, ordinary automatic event firing stops permanently. Ongoing missions, defense, campaign, withdrawal, protection, shared civilian processing, succession and final-war settlement continue. Do not gate these operations behind the same flag that disables new automatic events. After founder defeat, independent governments retain their current missions and obligations unless their own current conditions change.

## AI, presentation and completion

Give the AI actual goals and hard feasibility checks before its scores. Implement the role and action matrix in Part 08. The mandatory harder-player-crisis factor applies once at the declared cap point and respects routes, costs and unrelated war reserves. Do not manufacture probabilities from relative scores.

Use `chaosx_ai_probability_auditor` for read-only native inspect, evaluate, sweep and matched compare evidence for every affected weighted surface. Preserve immutable before sources and the exact scenario set before the patch owner changes a weight. The decision and mission auditor cannot substitute for this probability pass.

Use `chaosx_decision_mission_auditor` with a self-contained `fork_turns="none"` handoff to review every family, lifecycle, quote, duration, tooltip, cancellation, mission capacity, AI and exploit guard. Final localisation must state actual requirements, full costs, current blocked reasons and measured results. Dynamic text must not display a requested amount as if it were the achieved amount.

Validate the relevant C, D and E scenarios in Part 13, including stale quotes, mixed payers, partial settlement, founder loss, post-terminal continuation, ally-first success and repeated callbacks. Provide a one-row-per-action implementation map with source ID, owner, category, target, visibility, requirement, payer, quote, timer, outcome, cleanup, AI surface, art and localisation. Keep iterating until all mapped decisions and missions satisfy the specification, or report the precise remaining blocker without claiming completion.

## Specialist handoff location

Write durable specialist handoffs to `docs/plans/115_heroic_crusade_plans/subagent_handoffs/`, using the exact filename assigned in each self-contained delegation. Preserve asset production evidence in the assigned active workspace until promotion under the owning skill. The parent integrates and reviews every handoff.
