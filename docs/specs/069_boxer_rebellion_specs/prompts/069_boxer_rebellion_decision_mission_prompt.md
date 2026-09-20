# Event 069 decision and mission implementation prompt

Work on Chaos Redux Event 069, Boxer Rebellion, using the current repository instructions and `docs/specs/069_boxer_rebellion_specs/`.
Read `README.md`, `research/source_review.md`, the relevant specification parts, and all mandatory current source and skill files in full before editing your assigned surface.
The package is a proposed design with explicitly incomplete source review, no executed project subagents, and no HOI4 MCP validation from its authoring run.
Do not treat its expected results as evidence.
Preserve `chaosx.nr69.1`, use three-digit event filenames, keep the event Minor Fire-Once with Chaos level 1, and preserve Domestic Unrest Severe plus Diplomacy Medium membership.
Record adopted design, implementation, and validation separately.
Do not silently omit, merge, simplify, replace, or defer a requirement.
Report any unavailable source, tool, identity, asset, or engine capability honestly.


Implement the forty-six action families in Part 5 and eighteen mission families in Part 6, using Parts 1 through 4, 7, 10, 11, 12, and 15 for their context.
Read the current decisions, missions, scripted-GUI, MTTH, event, and applicable shared-system skills and sources in full.
Use `chaosx_decision_mission_auditor` for its permitted patch-capable review and `chaosx_ai_probability_auditor` for read-only probability evidence.

Keep the normal decision surface small.
Expose only Boxer Strength and Intervention Pressure as public event-specific values.
Show three to five primary actions, never more than six on the current surface, and normally one to three active missions.
Use ordinary decision and target interactions.
The approved design does not require a new scripted-GUI window or custom graphical meter panel.
A static category picture is allowed only while that simple presentation remains true.

Implement one validation and payment contract for each gameplay action, shared by human and AI entry paths.
Use real actor and target ownership, current access, phase, cost, cooldown, and objective identity.
At most four spendable or committed cost types are allowed per action, including exclusive force or industry commitments.
Command Power cost must not exceed 60.
Show no more than three inline cost quantities and the full accurate bill in the tooltip.
No stale target, repeated confirmation, or ownership change may cause a second payment or reward.

Mission success follows actual map, diplomacy, production, supply, or sustained compliance.
It completes automatically without a second paid click.
Provide partial success, failure, timeout, cancellation, supersession, and cleanup for every applicable family.
Use ordinary durations of 90, 180, or 365 days as designed, with the explicit 30- or 60-day emergency relief exception.
Do not create an invisible fourth deadline.

Track allocated, delivered, consumed, captured, and released material separately.
Use actual template bills, equipment differences, and supported transport or construction commitments.
Captured depots, donations, country activation, and demobilization must conserve stock and manpower.
A cancelled mission refunds only the assets that actually remain unused and recoverable.

Bind relief, famine, migration, deaths, condemnation, contamination, and current war relationships to their real shared owners.
Do not introduce extra food, debt, compliance, or coalition-cohesion meters.
Do not promise a ceasefire, limited access, payment transfer, or scoped unit effect until the engine representation is verified.

Give the AI the complete valid target pool independently of the human's selected target.
Audit the named scenarios in Part 11 with the actual probability tools and complete source pools.
Decision willingness is not a simple click probability.
Return the actual action and mission coverage table, costs, objective identity checks, AI evidence, presentation review, and unresolved blockers.
