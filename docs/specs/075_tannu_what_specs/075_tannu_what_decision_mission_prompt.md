# 075 · Decision and mission implementation prompt

Implement the entire Event 075 decision and mission loop from `docs/specs/075_tannu_what_specs/`, especially Parts 2-4, 10-13, 16-17 and 20-21.
Read the complete relevant source files, `AGENTS.md`, `chaos-redux-decisions-missions`, `chaos-redux-events`, applicable scripted-GUI references and current cost consumers before implementation.
The main source is an existing TAN aid operation, paid army reveal, outward conquest and earned global campaign.

Preserve five primary action families per phase.
Accumulation manages appeals, a targeted government request, funded industry, paid reserves and the reveal commitment.
Expansion manages fronts, replacements, captured industry, real territorial settlement and continental objectives.
The global campaign manages theater priorities, the earned continental program, overseas operations, submission or administration, and actual final settlement.
Outside TAN, a donor sees its own offers, policies, justified audit and relevant containment choices.
Do not make fifty persistent country buttons or expose private aggregate TAN aid to every donor.

Standing aid campaign priorities are not countdown missions.
Keep at most three actual event-created missions active per country, including funded works, special paid preparation and one relevant holding objective.
Use native construction, research, production and training queues where their own outcomes already cover the work.
A special mission needs a meaningful event-specific success, failure, interruption, cancellation and settlement rule.

One donor has at most one unresolved request.
Quotes are explicit and immutable for that offer, acceptance rechecks actual affordability, and response choices are full, stated smaller, valid substitute and refusal.
Expire unanswered offers without payment.
A standing policy is bounded, revocable and does not override an audit or authorize a new category silently.
Every transfer, program and reveal uses once-only transaction ownership.

Implement real material sacrifices, including manpower, equipment, productive effort, transport and fuel when relevant.
Political or command power is not the universal purchase currency.
Normally expose one to three spendable cost types and never more than four for an action.
Show at most three inline cost values with verified native text icons.
Separate requirements from prices and provide useful disabled tooltips.
Check helper return values and sign mutation against current code before payment.

Readiness is the only persistent event-specific numeric summary in the main interface.
Use native category text and tooltips unless an actual accepted interaction requires a scripted GUI.
No bespoke dashboard, focus inlay, animation or graphical category meter is currently planned.
A static category picture is eligible only for an appropriate simple category and verified consumer.

The early reveal and final short focus enter the same irreversible transition.
They must show actual border opponents, end protection, return foreign-owned support safely and activate only correctly paid reserves.
New post-reveal non-allied neighbors remain political targets even when the player changes operational priority.
Continental and overseas holding conditions need the real map and supply tests, not free timed completion.

Use the read-only decision/mission and probability auditors with self-contained isolated prompts through the actual runtime.
Inspect, render, compare and test the relevant implementation, including multiplayer, stale responses, save/load and cleanup.
Do not launch HOI4 or fabricate live evidence.
Report every missing engine consumer or unsupported cost mechanism instead of silently simplifying the requested loop.
