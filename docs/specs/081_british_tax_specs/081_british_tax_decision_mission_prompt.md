# Event 81 decision and mission implementation prompt

Read `chaos-redux-decisions-missions`, AGENTS.md, the full Event 81 package, and the actual installed-game and repository examples relevant to dynamic costs, country targeting, active missions, and factory commitments. Parts 1, 3, and 4 own the permissions and player routes. Part 2 owns the economic accounting.

Use `chaosx_decision_mission_auditor` with a fresh, self-contained bounded task when actual subagent tools are available. The current planning session did not run this agent or the mandatory HOI4 decision tools. Do not convert this prompt into a false prior audit record.

## Categories and action budget

Implement British Tax Resistance for independent taxed countries and British administration for ENG. Use ordinary native decision presentation with two static category pictures. Retain two custom progress values for the whole mechanic, Tax Stage and completed Reform Domains. Normal native effect lines and mission timers explain consequences without adding authority, debt, revenue, or influence currencies.

Keep three to five main actions normally visible, six at the hard maximum, and one to three active missions at the hard maximum. Mutually exclusive stage and country variants replace the same action family. One core reform or consolidation can be active per country. British response missions are bounded additional work, not an extra mission for each monthly invoice.

## Permissions

Enforce the hierarchy at visibility, availability, click, event reply, and completion. British dependents cannot refuse, negotiate away, reduce, or resist. Independent British-led allies can reach Nominal but cannot start the final transition or cancel while ENG leads. Other independent taxpayers may use the full peaceful route or immediate hostile cancellation. Handle other non-independent taxpayers exactly as the authored resolution in Part 1 defines.

Identity is ENG, not the current event ROOT, current player, cosmetic name, or whichever country owns London. Every human country receives its own correct target scope.

## Full chain

Implement all twelve domain projects and all four consolidations. Each domain completion immediately reduces its own taxes and Britain's corresponding benefit. Consolidation establishes the formal next stage. The final transition retains the defined 5% full-assessment floor until completion. No consolidated stage or completed domain is reset by an active Evolution.

Use the source's stage, Evolution, bargaining, partner, and low-industry adjustments. Quote and freeze upfront costs and duration at commitment. Exact affordability is inclusive. Charge the upfront cost once. Continuing factory commitments release on every completion, cancellation, suspension, abolition, or invalidation path.

Never apply a universal cost discount twice. Inspect the project's cost surface and Event 26 integration. Inline costs use the required native icons and no more than three displayed cost types. Political Power is the normal political resource. Do not add an inappropriate Command Power fee.

## Low-industry and partner routes

A taxpayer with less than one available whole factory must have the defined Political-Power-and-time alternative. A country that loses its committed capacity after launch gets the bounded pause and conversion route rather than permanent failure. Preserve work already performed, and do not charge the initial fee again on conversion.

A foreign assistance project requires an actual relevant partner, costs, target validation, and the partner's own consent. AI selection cannot rely on a human UI target. A withdrawing partner triggers domestic substitution with a bounded extension. No eligible partner is not a permanent barrier to independence.

## British response

Implement one pressure episode per country per stage, the 15-day response, the fixed surcharge and delay limits, and the taxpayer's meaningful responses. No British response defaults to allowing a lawful process, not a free tax waiver. A lack of 25 Political Power takes the disclosed fixed delay rather than becoming an infinite mission failure.

Refusing a British objection is not hostile cancellation of the tax itself. Only the exact refusal and cancellation routes create the special entitlement predicate. Emergency and pressure surcharges use the larger applicable rate, never an unbounded stack.

## Completion, cleanup, and evidence

Cover completed domains, paused final work after a faction lock, genuine independence, re-subjection, direct war, capitulation, lost capacity, partner withdrawal, global abolition, and ENG disappearance. Use ownership-aware removal and idempotent outcome handling. The same cancellation event delivered twice must not grant two goals or apply two debits.

Inspect and validate native decision and mission definitions with the currently available HOI4 tool suite. Use actual schemas rather than guessed command names. Record representative scopes, cost quotations, equality-affordability cases, and completion after relationship changes. Do not start or restart the user's game unless separately authorised. Live testing belongs to the user's later authorised workflow.

Deliver bounded implementation changes, localisation coverage, category and icon consumers, the permission matrix, mission outcome checks, and explicit blocked capabilities. Do not claim completion until the real costs, actual economic relief, and all exit paths satisfy the source specification.
