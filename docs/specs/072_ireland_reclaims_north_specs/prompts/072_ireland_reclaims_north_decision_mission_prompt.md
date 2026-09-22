# Implement the complete decision and mission system

Read the current decision, event, scripted-GUI, MTTH, subagent and asset skills with their required references.
Read specs/decisions/072_decisions_and_missions.md and both action-register companions inside docs/specs/072_ireland_reclaims_north_specs/.
Implement all 42 actions and their linked focus groups, including reserve mobilization, naval and air exercises, diaspora investment, sovereign independence negotiation and joint defense exercises.

Keep three to five primary actions visible in the current phase, with a hard ceiling of six and normally one to three active missions.
Complete the six category designs and the five territorial GUI attachments.
An action moved into a different category must retain its eligibility and the required territorial display.
National Development remains outside the formation family only while it has no formation or territorial integration action.

The reclamation is a 180-day real-war mission with a five-day continuous full-northern-control test.
The one 90-day extension costs 50 Political Power and 250 support equipment and requires at least 5,000 available manpower, which is a gate and not a payment.
The mission ends in automatic verified settlement and earned tree unlock or permanent failure.
Do not add a paid victory click or a second army grant.

For every action, implement its exact gate, target scope, quoted cost, response window, work duration, success effect, interruption, cleanup and repeat guard.
Diplomatic offers have 30-day response windows.
Accepted longer investment and procurement contracts begin their separate work timer only after acceptance.
Sending an offer is not consent.
A human refusal cannot be overridden by an AI fallback.

There are at most four spendable resource types per action.
Use the same final quoted values in the tooltip, AI, availability and debit.
Exact equality must pass affordability.
Freeze quoted costs, revalidate the actual actor and target immediately before commitment, and pay once.
D37 calculates all four costs from the actual selected ordinary reserve-infantry template and finite batch size.
Do not substitute a guessed fixed manpower value for that calculation.
Resolve civilian-capacity commitment semantics before using them, with release on completion or cancellation and no invented factory-day effect.

Use one live territorial helper across the state pieces, summary, decision and AI.
Imperial formation requires Irish ownership and control.
Federal formation requires each sovereign member's ownership, control and accepted charters.
Access treaties are distinct from sovereign ownership.
Never cache stale owner names or use GUI-only broad ownership logic.

Use the current universal registry and category attachment audit.
The archived producer chain is not a routine command.
Keep consumers draft until approved geometry, final DDS and mandatory map/GUI evidence exist.
Inspect and render the actual linked category for relevant partial, complete, missing-target, long-text and optional-hidden states.
Review native text icons and cost clipping at supported resolutions.

Dispatch the decision/mission auditor and probability auditor through the provided isolated-role workflow.
Run exact-cost, invalid-target, duplicate-click, failed-offer, interrupted-project, treaty-change, all-tier and save/reload tests.
Report actual changed files and evidence, with remaining source, scope or tool blockers separated from completed implementation.
