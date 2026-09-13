# Focus-tree implementation prompt for Event 044 Yakub Returns

Use `chaos-redux-focus-trees`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-subagents`, the HOI4 MCP focus tools, and `AGENTS.md`.

Read spec parts 2 through 4, the full focus architecture diagram, the country package matrix, AI strategy matrix, acceptance criteria, and asset prompt.

Implement a full focus tree for the American Event 44 state. Foreign Event 44 states receive the smaller shared regional tree described later. Do not reduce the American state to a generic or shared minor-country tree.

## American tree architecture

Use the lane map in `diagrams/044_yakub_returns_focus_architecture.md` as the route contract.

The opening group must address:

- Founding Emergency
- Secure the Capital
- Feed the Cities
- Define Provisional Rule

These are working focus-group labels, not final localization. The opening should reveal the country's immediate survival problem and lead into political choice, institutions, defense, diplomacy, and integration.

## Political route family

Implement five deep routes:

### Personal Revelation

Role:

Founder-led religious-political authority under Yakub or a valid successor.

Mechanics:

- founder authority
- temple and school institutions
- personal appointments
- doctrinal unity
- succession planning
- tension between charisma and stable government

Tradeoffs:

Strong mobilization and unity, weak succession, institutional dependence on the founder, diplomatic suspicion, and risk of internal cult control.

### Federal New Nation

Role:

Constitutional separatist federation with regional autonomy and negotiated institutions.

Mechanics:

- federal convention
- state accession
- civil administration
- local autonomy
- treaty relations with the United States
- North American New Nation formation
- Diaspora Federation preparation

Tradeoffs:

Slow negotiation, member vetoes, regional inequality, and stronger long-term legitimacy.

### Black Republic

Role:

Secular revolutionary or civic republic based on political equality, labor, citizenship, and state institutions.

Mechanics:

- republican constitution
- labor and civic organizations
- secular courts
- regular army
- anti-colonial diplomacy
- doctrinal break with personal revelation

Tradeoffs:

Factional competition, weaker founder loyalty, political contest, and stronger foreign civic legitimacy.

### Original Supremacy

Role:

Authoritarian Black supremacist state that accepts Yakub's racial narrative as official doctrine.

Mechanics:

- exclusionary citizenship
- ideological education
- loyalty reviews
- security institutions
- centralized mobilization
- International coercion
- resistance and defection
- supremacist terminal variant

Tradeoffs:

Short-term command strength, long-term resistance, Condemnation, sanctions, member exit, diplomatic isolation, economic weakness, and succession danger.

Do not add racial biology modifiers, race-targeted combat bonuses, race-percentage values, or generic racial violence decisions.

### Diaspora Congress

Role:

Plural coalition of Yakubite, separatist, anti-colonial, religious, labor, and civic movements.

Mechanics:

- congress politics
- coalition recognition
- regional representation
- foreign aid and legal defense
- International offices
- associate membership
- doctrinal pluralism
- congress terminal variant

Tradeoffs:

Slow decisions, internal bargaining, local autonomy, and strong transnational legitimacy when Cohesion holds.

## Supporting branch families

### Community economy and institutions

Include schools, food distribution, health or relief administration, printing and press, businesses, finance, courts, cooperative development, state-directed industry, and regulated movement enterprise.

Use staged idea lifecycles and map-based construction. Do not add one new national spirit per focus.

### National defense

Include militia integration, regular army formation, officer development, arsenals, captured depots, logistics, rail defense, air defense, and route-specific military organization.

The army uses ordinary period units. No custom battalion or 3D model is required.

### Diplomacy and recognition

Include relations with the United States, recognition campaigns, guarantees, neutral trade, anti-colonial partnerships, foreign missions, International membership, and route-specific faction policy.

### Intelligence and internal security

Include counterintelligence, infiltrator cleanup, founder protection, opposition policy, foreign intelligence, and route-specific security institutions.

The branch should interact with decisions and should not become a passive spy bonus column.

### Territorial integration and formables

Implement staged state accession, occupied-state administration, local institutional proof, resistance, negotiated settlement, and the two accepted formations:

- North American New Nation
- Diaspora Federation

Do not grant instant cores across all included territory. Use integration missions, compliance, local support, or federal approval.

### International and terminal preparation

Unlock and expand International offices, Cohesion tools, member relations, federation, schism handling, terminal readiness, and route-specific commitment.

The terminal branch remains hidden until Evolution III, 1000 or more Chaos, and owner-specific readiness.

## Branch interaction

Political routes must change the supporting branches. Examples:

- Personal Revelation changes school, security, and succession focuses.
- Federal New Nation expands accession and treaty focuses.
- Black Republic changes labor, citizenship, and anti-colonial focuses.
- Original Supremacy changes loyalty, repression, International discipline, and terminal focus behavior.
- Diaspora Congress expands regional representation, associates, congress decisions, and Cohesion.

Industry supports defense and integration. Diplomacy changes recognition and International options. Expansion creates resistance, treaties, and postwar work. Keep cross-branch junctions deliberate and limited.

## Ideas and identity

The state starts with:

- Disputed Revelation
- Parallel Institutions
- Improvised National Defense

Every idea needs a visible lifecycle. Routes mitigate, replace, upgrade, corrupt, or remove them. Avoid dead idea stacks.

Political routes may change:

- leader or institutional leadership
- ruling party and party names
- flag and cosmetic name
- advisor roster when explicitly implemented
- laws and citizenship
- AI strategy
- diplomacy
- decision categories

Every visible identity change needs matching assets and localization.

## Layout and MCP workflow

Before editing, inspect installed vanilla and current Chaos Redux focus precedents. Use:

- `hoi4.focus_inspect`
- pre-change `hoi4.focus_render`
- bounded `hoi4.focus_rewrite` where appropriate
- post-change inspect, render, lint, and compare

Render the full tree at normal game zoom with real titles and icons. A reviewer must be able to name every branch root, major fork, and payoff from the render.

Use compact coherent lanes, short connectors, and visible symmetry where the route logic supports it. Reject crossings, overlaps, long decorative lines, fake branches, staircases, and disconnected islands.

Every focus needs accurate search filters. Add Focus Navigation entries for spatially separate political, economy, defense, diplomacy, integration, International, and terminal regions. Hidden branches must not appear in navigation before reveal.

No focus inlay window is required. Do not add one unless a separately accepted design proves that the tree needs persistent local presentation beyond decisions and tooltips.

## Focus rewards

Use varied rewards:

- decisions and missions
- buildings and map construction
- railways and supply
- units and templates
- equipment and production lines
- leader and party changes
- laws
- advisors where justified
- claims, cores, and integration work
- recognition and diplomacy
- faction or International mechanics
- idea transformations
- events
- route access

Flat modifiers support these rewards but do not replace them. Avoid filler chains that give only political power, stability, war support, small research bonuses, or new ideas.

## AI

Implement route-specific AI from the AI strategy matrix. AI should read:

- founder state
- faction strength
- territory and population
- war state
- recognition
- relations with the United States
- International form and Cohesion
- economy, supply, equipment, and manpower
- current Chaos
- local and foreign threat
- route validity

Complex focus weights require the named probability scenarios. Establish a baseline with the probability auditor and compare the same scenarios after implementation.

## Foreign shared regional tree

Create a smaller Event 44 regional tree with:

- opening survival
- local political convention
- one region-specific institution branch
- defense
- independence and recognition
- International relationship
- route-specific late game

Country modules must change localization, leaders, decisions, AI, rewards, icons, and regional effects. A shared tree that reads and plays identically across every module fails.

Long-lived major regional states may receive an expanded branch only when implementation evidence and the spec justify it.

## Completion evidence

Produce a route coverage table:

| Required route | Implemented focus branch | Status | Notes |
| --- | --- | --- | --- |

List every focus ID, icon, search filter, AI plan, decision unlock, idea lifecycle change, country identity change, formable hook, and hidden reveal.

Run the focus-tree auditor after implementation. Resolve every route, layout, icon, localization, prerequisite, bypass, AI, and formable finding. Do not claim completion while a required route is missing, merged without approval, visually unreadable, or represented by a thin fallback.
