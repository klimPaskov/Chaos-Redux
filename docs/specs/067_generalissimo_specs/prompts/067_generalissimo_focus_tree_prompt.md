# Event 067 Generalissimo Focus Tree Prompt

Implement and validate the complete host-adaptive national focus tree for the Generalissimo government created by Event `067`.

## Required sources

Read in full:

- every file under `docs/specs/067_generalissimo_specs/specs/`
- `docs/specs/067_generalissimo_specs/diagrams/067_generalissimo_state_machine.md`
- `docs/specs/067_generalissimo_specs/handoffs/067_generalissimo_probability_scenario_matrix.md`
- `docs/specs/067_generalissimo_specs/prompts/067_generalissimo_decision_mission_prompt.md`
- `AGENTS.md`
- `chaos-redux-events`
- `chaos-redux-focus-trees`
- `chaos-redux-decisions-missions`
- `chaos-redux-event-assets`
- `chaos-redux-subagents`
- `chaos-redux-improvement-loop`
- the current offline Paradox wiki focus pages
- current vanilla focus, Focus Navigation, and focus-inlay documentation and examples
- the current Event 067 implementation and every prior handoff under `docs/plans/067_generalissimo_plans/`

Use `chaosx_focus_tree_auditor` for the final route and layout review. Route every focus weight and route-choice probability through `chaosx_ai_probability_auditor`. Use `chaosx_event_ui_worker` only for the accepted Event 067 focus inlay and compact event-owned display. The shared focus interface and shared Event Logs remain outside that worker's scope.

## Tree identity

Create one full focus tree that follows the canonical Generalissimo character and loads for the military government after peaceful submission or civil-war victory. It must remain available after reunification.

The tree adapts to the host country through scripted conditions, dynamic localisation, state selection, existing service branches, naval access, air capacity, subjects, faction status, nearby rivals, and the wider world. It must not assume one historical country, one ideology, one continent, or one fixed civil-war map.

Target a complete tree of roughly 65 to 90 meaningful focuses. The final count may differ when the route architecture is stronger, but no named route from the specification may be reduced to a label or token spur.

## Opening architecture

The opening must stabilize the new regime and reveal major choices quickly.

Required opening functions:

- establish the current command structure
- secure the capital and central staff
- assess army loyalty and Command Cohesion
- reopen military supply and armament administration
- begin officer settlement
- choose the permanent political structure within the first useful route phase

The opening should expose two to four clear early choices. It must not force several generic political power, stability, or factory focuses before the player reaches the event's premise.

## Political structure routes

Implement three real and mutually exclusive political structures.

### Personal Command

The Generalissimo centralizes military and civil authority around himself.

Required play:

- strongest direct ruler bonuses
- higher dependence on his survival and personal authority
- loyal appointments and leadership cult institutions
- stronger coercive foreign actions
- weaker succession and institutional resilience
- access to the Supreme Strategic Sphere route
- clear risk when Command Cohesion is low

### Officer Directorate

A senior officer council governs under the Generalissimo's chairmanship.

Required play:

- stronger officer integration and stable Command Cohesion
- council appointments and internal bargaining
- reduced personal concentration
- stronger International Command leadership
- better integration of foreign juntas
- risk of factional deadlock or rival staff blocs

### National Emergency Council

The Generalissimo rules through a military guardian arrangement that retains selected civilian institutions.

Required play:

- stronger civil administration and long-term stability
- legal and bureaucratic continuity
- lower coup-export willingness
- stronger defensive and sovereignty routes
- access to the Guardian State achievement path
- risk of civilian resistance when emergency rule never ends

## Military strategy routes

Implement three real and mutually exclusive strategic doctrines for state policy. They modify ordinary army use without adding a custom doctrine folder or technology tree.

### Decisive Command

- concentration of force
- offensive planning
- breakthrough and encirclement priorities
- armor, artillery, air support, logistics, and operational reserves where relevant
- temporary power windows with supply and equipment costs
- postwar strain when campaigns overreach

### Army of the Nation

- broad mobilization
- reserve systems
- officer training
- manpower organization
- regional commands integrated into one army
- stronger recovery from civil-war division
- lower personal guard priority

### Fortress Command

- capital and strategic-region defense
- rail, supply, air defense, forts, coastal defense, and reserve positioning
- defensive war planning
- lower expansion willingness
- stronger National Emergency Council compatibility
- meaningful use for landlocked, coastal, large, and small hosts through dynamic state selection

## Economy and logistics

Implement full routes for:

- Arsenal State
- Mobilized Construction
- central military logistics
- railway and supply restoration
- fuel, trains, convoys, and strategic material management where relevant
- military production allocation
- civil capacity needed to sustain long rule

These routes must build or repair real infrastructure and production in valid host states. They must use named or dynamically selected regions. Avoid generic factory dumps and repeated national spirits.

## Internal rule

Implement two incompatible governing methods after the political structure becomes clear.

### Rule Through Garrisons

- regional commands and internal security
- force commitment to key states
- rapid response to resistance
- stronger coercion
- higher equipment and legitimacy costs

### Rule Through Service

- veteran administration
- reconstruction battalions
- public service and officer mediation
- slower control gains
- stronger long-term integration
- reduced need for permanent garrisons

Each method must change decisions, missions, officer settlement, occupied-region handling, and Command Cohesion.

## Foreign-policy routes

Implement three complete strategic directions.

### Officer Solidarity

- support compatible military governments
- staff missions
- guarantees and intervention
- International Command formation
- shared planning and military production
- member rules, refusal, expulsion, leadership, and failure states

### Fortress Sovereignty

- armed neutrality or limited guarantees
- border security
- deterrence
- protection against foreign patronage
- defensive regional agreements
- no forced offensive expansion

### Supreme Strategic Sphere

- coercive diplomacy
- client juntas
- pressure on neighboring governments
- intervention and expansion
- postwar military administration
- resistance, foreign reaction, and integration costs

The three foreign routes must create different campaign plans. They must not share the same war goals, faction behavior, and rewards under different names.

## Postwar integration

Implement a complete reunification and reconstruction route for civil-war victors.

Required work:

- unify army registries and templates
- settle loyal, neutral, and defeated officers
- restore rail and supply control
- reopen armament plants
- integrate regions held by the former legal government
- settle subjects and faction membership
- replace temporary emergency ideas
- proclaim the permanent government

Peaceful-submission governments should receive bypassed or adapted versions instead of fake civil-war reconstruction.

## Conditional service branches

Create naval content only when the host has a meaningful navy, coast, dockyards, naval technology, or route need. Create air content only when the host has meaningful air capacity or can build it.

Naval content may support:

- convoy command
- coastal defense
- fleet loyalty
- maritime staff reform
- amphibious operations under expansion routes

Air content may support:

- air command loyalty
- capital defense
- reconnaissance
- operational support
- transport and supply

A landlocked host with no navy must not receive dead naval focuses. A minor host without a viable air branch must receive a compact alternative or safe bypass.

## Hidden world-end extension

Keep the world-end extension hidden until The Generalissimos' World launches.

It should support:

- leadership of International Command
- rivalry with other military blocs
- support for foreign coups
- intervention for aligned regimes
- pressure on neutral juntas
- conflict with Civil Authority Compact
- consolidation or failure of the military world order

Do not expose world-end names, focuses, or route hints before launch.

## Command Cohesion integration

Command Cohesion is the single visible post-takeover Event 067 value.

Focuses must:

- raise or lower it through public actions
- gate risky route steps
- change decision costs and mission difficulty
- respond to victories, defeats, officer settlement, supply, purges, council conflict, and regional control
- provide recovery tools without making low Cohesion harmless
- avoid repeated automatic civil wars as a generic failure response

Influence must be closed before this tree becomes active.

## Idea lifecycle

Use a small set of deep ideas.

Required starting ideas:

- Government at Gunpoint
- Army of the Generalissimo
- Command Economy Under Mobilization

Each must have mitigation, route upgrade, failure, and final forms. Replace or modify existing ideas instead of stacking one new idea per focus. The tree must not exceed the current project spirit budget without an explicit documented reason.

## Layout and first-glance clarity

Before final coordinates, write the branch lane map and primary ownership for every focus.

The normal-zoom render must clearly show:

- opening and state consolidation
- political structures
- military strategies
- economy and logistics
- internal rule
- foreign policy and expansion
- postwar integration
- conditional naval and air content
- hidden world-end content only after reveal

Use compact symmetry where it fits. Use short direct connectors. Do not use decorative ladders, zigzags, crossed lines, overlapping focuses, long connectors around unrelated branches, or random islands.

## Filters, navigation, and inlay

- Assign accurate search filters to every focus.
- Add Focus Navigation for spatially separate major branch families.
- Hide navigation for unrevealed world-end content.
- Reserve clear tree space for the Event 067 focus inlay.
- The inlay shows the canonical portrait, political structure, Command Cohesion, and one next important route condition.
- It remains read-only unless an accepted spec addition explicitly grants an action.
- It must not cover focuses, connectors, navigation controls, filters, or continuous focuses.

## AI

Create route-specific AI plans for:

- personalist conqueror
- collegial officer regime
- guardian-state defender
- war-weary consolidator
- industrially weak junta
- threatened minor
- naval host
- landlocked host
- world-end bloc leader
- rival military government

AI must consider war state, enemy strength, Command Cohesion, industry, manpower, equipment, supply, naval access, air capacity, subjects, faction position, nearby military governments, civilian opposition, and world-end role.

Use the named focus scenarios from the probability matrix. Establish baseline evidence through `chaosx_ai_probability_auditor`, apply the intended weights, then require `hoi4.probability_compare` over the same scenarios.

## Required MCP evidence

Use:

- `hoi4.focus_inspect` before editing
- `hoi4.focus_render` for the existing and planned tree
- `hoi4.focus_rewrite` for bounded structural and layout changes
- post-change focus comparison
- `hoi4.gui_inspect` and `hoi4.gui_render` for the focus inlay
- `hoi4.gui_rewrite` only through the accepted Event 067 GUI scope

Review the final render at normal zoom without source annotations. A route that cannot be identified from the render is not complete.

## Asset and localisation handoff

Use the Event 067 asset prompt for focus icons, inlay elements, ideas, and route emblems. Every icon family needs its own source art and runtime sizing. Do not resize one icon type to satisfy another.

Final focus text must be host-aware and route-specific. It should describe public policy, visible commitments, and consequences. It must not expose hidden AI values, future branches, debug state, or implementation notes.

## Completion report

Return:

- files changed
- full route coverage table
- focus count by branch
- lane and navigation map
- starting idea lifecycle table
- decision and mission unlock crosswalk
- conditional naval and air coverage
- host-adaptation cases
- AI route scenarios and probability comparison evidence
- MCP inspect, render, rewrite, and comparison evidence
- focus auditor findings and dispositions
- asset and localisation status
- unresolved blockers
- every simplification, merger, omission, fallback, or replacement

Do not mark the tree complete while a named route, conditional host case, icon, localisation family, AI plan, inlay state, or postwar function is missing.
