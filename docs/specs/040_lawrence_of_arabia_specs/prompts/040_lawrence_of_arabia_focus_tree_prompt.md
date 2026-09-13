# Event 40 Federation Focus Tree Prompt

Implement the dedicated focus tree for the permanent federation created by Evolution III of Event 40.

## Scope boundary

Do not create full Event 40 focus trees for every Arabian target. Existing countries keep their own trees. This prompt applies only to:

- British Arabia
- Independent Arab Federation
- Lawrence's Kingdom

Use one origin-aware federation tree or cleanly separated origin trees according to the implementation architecture. Every origin must receive distinct political content, AI, localisation, identity, and route validity.

## Required reading and evidence

Read in full:

- `AGENTS.md`
- `.agents/skills/chaos-redux-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- every Event 40 specification file
- relevant offline National Focus Modding and interface pages
- installed vanilla focus documentation and precedents

Use the HOI4 MCP focus workflow before and after source changes:

- inspect
- full-tree render
- lint
- rewrite when needed
- compare

A source-only layout review is insufficient.

## Opening

Begin with one focus or a very small opening group that establishes:

- provisional federal government
- founding charter
- temporary or final capital
- member representation
- Federal Authority
- the lifecycle of Uneven Administration, Rival Commands, and the origin-specific political pressure

After the opening, expose a small number of clear choices. Do not reveal every late branch immediately.

## Branch lanes

Create clear, separated lanes for:

1. political identity
2. federal center and member autonomy
3. economy, oil, customs, rail, ports, and supply
4. army and irregular integration
5. air, coast, transport, and communications
6. diplomacy and recognition
7. accession, integration, and regional settlement
8. late regional order

Use short, clean connectors. Avoid ladders, zigzags, crossing lines, overlapping focuses, and mixed-purpose clusters.

## Political routes

### British-Aligned Federal Compact

Purpose:

- stabilize British Arabia as a dominion, protectorate, or allied federation
- use British equipment, training, bases, intelligence, oil, and transport agreements
- create a later autonomy route

Tradeoff:

- strong early support
- continuing British leverage and internal opposition

Required route groups:

- ratify the British compact
- define autonomy status
- military mission and common defense
- oil and transport convention
- federal voice inside the British system
- optional demand for equal partnership

### Sovereign Arab Congress

Purpose:

- create a constitutional independent federation
- build recognition, member guarantees, common defense, and independent institutions

Tradeoff:

- strong long-term sovereignty
- slower consolidation and member veto risk

Required route groups:

- constituent congress
- member guarantees
- federal cabinet and civil service
- independent foreign service
- common defense charter
- external recognition

### Lawrence's Personal Settlement

Purpose:

- resolve the rare Lawrence's Kingdom origin
- establish personal authority, member councils, military government, succession, and later institutionalization

Visibility:

- hidden unless the country origin is Lawrence's Kingdom

Required route groups:

- personal oath
- council of founding houses or governments
- field government
- chartered crown versus commander's state
- secure succession
- separate the state from the man, optional reform

The route must remain playable after Lawrence dies.

## Federal structure routes

Create two broad methods that can interact and converge.

### Central federal state

- common revenue
- unified ministries
- federal court and law
- direct command
- faster integration
- higher member resistance

### Charter federation

- member guarantees
- shared revenue formula
- regional commands
- slower central projects
- easier voluntary accession

Federal Authority must change through focuses, decisions, missions, member behavior, and outcomes. Do not create several redundant authority ideas.

## Economy and logistics

Use real map work.

Required focus groups:

- federal customs line
- connect member railways
- Red Sea and Gulf port plan
- oil revenue settlement
- federal supply depots
- desert air-route infrastructure
- industrial projects outside the core
- common equipment repair standards

Select states dynamically from actual members. Name the relevant regions in tooltips. Do not grant buildings to invalid or foreign states.

Offer distinct funding methods:

- British capital
- member-funded development
- balanced foreign investment

Each method needs timing and dependency consequences.

## Army and irregular integration

Required focus groups:

- register member armies
- resolve officer seniority
- integrate irregular forces
- desert reconnaissance schools
- common artillery and support standards
- federal general staff versus member war council
- mobile supply columns
- defend the long frontier

Use templates, command changes, decisions, training, equipment, and supply. Avoid repeated tiny army modifiers and unnecessary new spirits.

Lawrence can support irregular coordination or mobile strategy when his current role permits it. Local commanders must remain part of the command package.

## Air, coast, transport, and communications

Required focus groups:

- desert airfields
- coastal observation
- federal transport command
- Red Sea convoy protection
- Gulf port defense
- air liaison schools
- long-range communications

Make the branch useful for logistics, reconnaissance, commercial access, and defense. Do not make it valuable only to a player already committed to a large navy or air force.

## Diplomacy and recognition

Required focus groups:

- recognition missions
- settle relations with Britain
- negotiate with France and other regional powers
- invite new members
- guarantee charter states
- build an Arab league or join a valid existing faction
- mediate regional wars
- oppose external protectorates

Any federation-led faction or league needs real membership, refusal, exit, leadership, war, and failure rules.

## Accession and postwar settlement

Use:

- voluntary accession
- associated-state status
- protectorates or guarantees
- negotiated borders
- claims on disputed member territory
- war goals only after failed diplomacy or a real hostile threat
- occupation and integration missions after conflict

Do not grant instant cores on the whole Event 40 registry.

## Idea lifecycle

Implement and resolve:

- Uneven Administration
- Rival Commands
- Promise Debt for British Arabia
- Federal Mistrust for the independent origin
- Personal Settlement for Lawrence's Kingdom

Map every starting idea to mitigation, upgrade, failure, and final forms. Do not leave a dead stack.

## Focus duration and rewards

Use 35-day focuses for early forks, urgent reforms, and short opportunities. Use 70-day focuses for major programs. Use other durations only when justified.

Reward focuses through:

- decisions and missions
- buildings and routes
- units and templates
- leaders and advisers
- laws and institutions
- claims, staged cores, and guarantees
- recognition and faction behavior
- Federal Authority changes
- idea upgrades
- events and settlement routes

Flat modifiers support these rewards. They are not the main branch design.

## AI

Create origin-aware route plans.

- British Arabia favors compact consolidation while Britain is strong and reliable.
- It can seek autonomy after British weakness or broken promises.
- Independent federation AI prioritizes recognition, command integration, and voluntary accession.
- Lawrence's Kingdom prioritizes succession and institutional stability before expansion.
- Low Federal Authority blocks reckless expansion.
- Invalid origin routes remain hidden or receive zero weight.

Route every complex focus weight through the probability audit scenarios.

## Presentation and assets

Use accurate search filters and Focus Navigation for separated branch families.

Request separate focus icons from the Event 40 asset package after stable focus IDs exist.

Keep the hidden Lawrence route concealed until valid.

A focus inlay is not planned. Propose one only when ordinary decision and tooltip presentation cannot keep Federal Authority readable, then obtain explicit parent approval and complete the GUI workflow.

## Completion proof

Produce a route coverage table with:

| Required route | Implemented branch | Status | Notes |
| --- | --- | --- | --- |

Run `chaosx_focus_tree_auditor` after implementation. Report merged, renamed, missing, simplified, or fallback routes. Do not claim completion with missing icons, AI, localisation, decisions, idea lifecycles, or postwar handling.
