# Layout, branch clarity, filters, and navigation

Read the complete applicable sections before laying out, rewriting, rendering, reviewing, or auditing a focus tree, and before adding search filters, Focus Navigation shortcuts, or a focus inlay window. These requirements supplement the main skill’s design, reward, integration, and completion rules.

## Layout rules

The tree must be readable in game. Layout quality is a completion requirement.

The layout is a semantic map of the country's strategy. It must show branch ownership and choice hierarchy before the player reads detailed effects. A tidy graph with unclear branch identity still fails.

Give each major branch family a coherent lane or bounded cluster with a visible root and endpoint. Keep the political family, industry family, military family, diplomacy family, expansion family, and special routes separated by stable spacing and clear geometry. A military family may contain army, navy, and air lanes, but those lanes must remain grouped and individually legible.

If major branch families occupy separate regions of a large tree, plan their Focus Navigation anchors at the same time as the branch lanes. Navigation targets should land on a readable branch overview, not on an arbitrary single node or empty space.

If the tree uses a focus inlay window, reserve its footprint before final focus coordinates are accepted. The inlay belongs to the tree composition and must not be treated as an overlay that can be dropped on top after layout work is finished.

Do not place unrelated focuses inside another branch lane because space is available. Do not scatter navy, air, logistics, diplomacy, or internal politics across the tree as isolated nodes. A cross-system focus still needs one primary branch home. Show secondary interaction through a clear junction, convergence, decision unlock, or mechanic gate.

Use names, icons, and palette families to reinforce branch structure. They cannot substitute for good route logic or placement. The branch should remain recognizable when the reviewer looks mainly at geometry and connectors.

The layout must be compact, symmetrical, and honest about the route structure. Comparable sibling branches should mirror each other around their parent or use evenly balanced spacing. Route families should remain centered around the opening group or main trunk. Symmetry means balanced geometry and matching visual rhythm. It does not require identical focus counts, decorative filler, or empty nodes.

A focus tree must not fake non-linearity. A mechanically linear sequence should use a clean direct sequence. Do not offset focuses horizontally and reconnect them with long or awkward lines to make one chain appear branched. Visual splits, merges, and side lanes must represent real choices, route locks, convergence points, or mechanical interactions.

Every prerequisite connection must use the shortest clean practical path. Position the parent and child close enough that the connector remains direct and easy to follow. Before accepting a long line, a detour, a crossing, or a line through unrelated branch space, move the focuses or simplify the visible prerequisite structure. A distant connector is acceptable only when it represents a real convergence that cannot be placed closer without damaging the rest of the tree.

Do not build unnecessary ladders, staircase shapes, repeated zigzags, or decorative offsets. A complex-looking layout does not create depth. Route depth must come from real choices, mechanics, consequences, and branch interaction.

Focus boxes must never overlap. Connector lines must not overlap each other, intersect each other, pass through a focus box, or cross an unrelated branch. Hidden focuses and continuous focuses must also be included in the overlap review.

Use the MCP focus tools to find layout deformities before rewriting. `hoi4.focus_inspect` and `hoi4.focus_render` report overlapping focus boxes, excessive gaps, cramped spacing, connector crossings, path lines that run through focuses or stretch too far, dangling connectors, bad prerequisite presentation, unbalanced branches, off-center layouts, and related diagnostics. Review the artifacts, then call `hoi4.focus_rewrite` with `layoutMode: "compact"` for cleanup or a complete route plan for creation. Review the rewritten artifacts and source diff. MCP supplies shared parsing, layout, rendering, and writes. This skill owns design, prerequisites, localisation, AI, icons, balance, and completion.

Reward-only changes that preserve layout reuse valid layout review and compare the source changes. Inspect/render again only when the changed text, assets, or layout inputs affect that review. No rewrite call is needed to prove the layout stayed unchanged. An invalid or empty identity-preserving rewrite request is a precise schema failure, not authority to invoke `layoutMode: "compact"` or auto-layout outside the requested scope. Inspect the actual schema and correct the request only within the accepted scope. If that tool operation is unavailable, apply the authorized reward-only edit directly and verify that focus IDs, count, coordinates, and prerequisites remain unchanged; do not run compact or automatic layout as a substitute. If the edit cannot preserve those fields, stop that edit and explain the specific conflict. Capture an immutable before snapshot, preserve accepted non-layout edits, and roll back only proven tool-generated drift through normal `apply_patch`, recording rejected and restored evidence. Compare focus IDs, count, coordinates, and prerequisites, and distinguish `HEAD` from the dirty index before accepting the result.

Review the full tree and affected states against the layout checks below. Fix confirmed ambiguity and recheck those changes while rendering is available; once those checks pass, no additional review cycle is required. Apply the AGENTS.md retry limit to tool failures and inspect the same coordinates, connectors, titles, icons, and states from source when necessary, stating what could not be visually checked.

Required layout checks:

- the normal-zoom render makes every supported major branch family recognizable at first glance
- every focus has accurate search filter tags for its actual role, using the current supported filter system
- every spatially separate major branch family in a large tree has a Focus Navigation shortcut with a correct label, icon, anchor, pan target, and useful zoom level
- Focus Navigation shortcuts do not reveal deliberately hidden branches before their reveal conditions are met
- any focus inlay window has reserved space and does not overlap or obstruct focuses, connectors, navigation controls, filters, continuous focuses, or other required tree UI
- every visible focus has one documented primary branch ownership or explicit convergence role
- every major branch has a visible root, readable internal direction, meaningful fork where relevant, and clear endpoint or convergence
- political, industry, military, diplomacy, expansion, and special content is not interleaved into branch soup
- army, navy, and air subbranches are visibly grouped under the military family when they exist
- whitespace and lane placement create clear branch boundaries without wasting large empty areas
- cross-branch connectors are limited to deliberate junctions and do not create a spiderweb
- no random focus islands or mixed-purpose clusters remain
- prerequisite parents are above children
- no duplicate coordinates
- no focus boxes overlap, including hidden and continuous focuses
- no connector lines overlap or intersect
- no connector runs through a focus box or an unrelated branch
- every prerequisite uses the shortest clean practical connector path
- no long connector remains when repositioning the parent, child, or branch can shorten it
- no unnecessary crossing lines
- no unnecessary ladder, staircase, zigzag, or decorative detour pattern
- no mechanically linear chain is offset to fake a non-linear branch
- comparable sibling branches use mirrored or evenly balanced horizontal spacing
- branch rows use a consistent vertical rhythm
- horizontal and vertical gaps are balanced and readable
- visible connectors agree with the scripted prerequisite structure
- route families remain balanced, symmetrical, and centered
- mutually exclusive branches are spaced comfortably and presented as a clear split
- branches are visually distinct without relying on awkward geometry
- continuous focuses are placed somewhere convenient without distorting the main tree
- hidden branches do not clutter ordinary routes
- large branches are not stacked in one vertical column
- the tree does not look like one long checklist
- branch endings are visually and mechanically clear
- side branches feed back into the main route, a mechanic, a decision family, or a real capstone
- the layout does not create random dangling focus chains with weak terminal rewards

If an `available = { has_completed_focus = ... }` condition gates a focus, decide whether it should also be a visible prerequisite. Do not add a visible prerequisite if it creates a crossing line, long detour, or asymmetric distortion. Move the branch, shorten the connection, or redesign the gate.

### First-glance branch clarity gate

A focus tree fails when its major branches cannot be identified from a normal in-game view. Branch clarity is a design requirement and cannot be deferred as visual polish.

At first glance, a reviewer should be able to point to every visible branch family that the country supports:

- the opening group or main trunk
- the main political branch family and its major political forks
- the industry, economy, and logistics branch
- the military branch family
- the army, navy, and air subbranches where they are substantial enough to exist
- the diplomacy, foreign alignment, or faction branch
- the expansion, reunification, liberation, federation, or settlement branch
- the special mechanic, internal struggle, crisis, or high-chaos branch once it is visible
- the late-game ambition or convergence path

The reviewer should not need to read every tooltip, inspect source files, or trace long connectors across the tree to understand what each major area is for.

Every visible focus needs one primary branch ownership or an explicit convergence role. A focus may affect several systems, but its position, prerequisite chain, title, icon family, reward, and follow-up content should still make its main role clear. Related focuses should stay in a coherent lane or compact cluster with an obvious opener, internal progression, meaningful choices, and a clear payoff.

A military family can split into army, navy, and air subbranches. Keep those subbranches visibly grouped under the military family while making each one separately readable. Maritime powers need a clear naval path. Countries whose strategy depends on air power need a clear air path. A landlocked or very small country may omit or compress a branch when its identity genuinely does not support it. Document that choice instead of scattering token naval or air focuses through unrelated branches.

Cross-branch interaction should use a small number of deliberate junctions, convergence focuses, decision unlocks, mission gates, or shared mechanic thresholds. Do not create a spiderweb of prerequisite lines. Whitespace, lane placement, focus names, icon families, and connectors should all describe the same branch taxonomy.

Visual grouping cannot rescue weak route logic. If two branches use the same goals, rewards, next steps, and campaign plan, redesign the routes before adjusting coordinates. If the tree looks random because the underlying choices are random, rewrite the branch architecture, prerequisites, rewards, and payoffs.

First-glance review:

1. Record the route architecture map and intended lane order before final coordinates are accepted.
2. Prefer a full-tree render at normal in-game zoom with real titles/icons; if the route cannot answer within the shared budget, inspect native coordinates, bounds, connector paths, titles, and icon references and report the visual limitation.
3. Review the available render without source annotations. Name every major branch, its visible root, its important fork, and its payoff from the render alone; when possible, use the parent or focus auditor instead of only the layout author. If rendering is unavailable, inspect the source layout and state that first-glance visual clarity was not observed.
4. Mark every focus whose primary branch, next choice, or relationship to nearby focuses is ambiguous.
5. Rewrite branch logic, branch roots, prerequisites, names, icons, spacing, or coordinates as required. Do not limit the fix to moving boxes when the route design itself is unclear.
6. Recheck actual fixes in the affected layout/branches; do not rerun the entire audit or wait for unavailable renders. Confirmed ambiguity remains a defect, while missing visual proof is a stated limitation.

Hard rejection conditions include:

- a major branch can only be found by reading all tooltips or following long connector lines
- political, industry, military, naval, air, diplomacy, expansion, and special content is mixed together without clear boundaries
- a branch has no obvious root, internal direction, meaningful route consequence, or capstone
- focuses appear as random islands or mixed-purpose clusters with no stable route identity
- reviewers cannot agree where major branches begin and end because the layout and route logic conflict
- the graph is clean but the routes remain interchangeable, shallow, or meaningless

Do not accept a tree as mostly readable, functional, or ready for later polish. Continue the render, review, and rewrite loop until the tree is logical, meaningful, and clean.

### Focus filters and Focus Navigation

Every focus tree must use clear focus search filters. Give each focus the current supported `search_filters` tags that describe its primary gameplay role. The filter taxonomy should agree with branch ownership, layout, titles, icons, and rewards.

Use the current vanilla filter keys whenever they fit. Create or extend custom filter definitions only when the tree genuinely needs a category that the existing filters cannot represent cleanly. Do not assign one generic filter to most of the tree. Do not tag a political focus as industry, a naval focus as army, or a special-mechanic focus as a generic political focus merely because that is convenient.

A focus may use more than one filter when it genuinely belongs to more than one gameplay system. Multi-tagging does not excuse unclear branch ownership. Every visible focus still needs one primary branch home or an explicit convergence role.

Large trees with spatially separate branch families must use HOI4 Focus Navigation shortcuts. A player should be able to select a branch tab or button and be taken directly to that part of the tree at a useful zoom level instead of dragging across a large canvas.

Each Focus Navigation entry must:

- represent one real branch family or another clearly defined tree region
- use a short localised label and a distinct, readable icon
- target a stable branch root, anchor focus, or deliberate visual center
- pan and zoom to a view that shows enough of the branch to understand its immediate structure
- work correctly after the player has manually panned or zoomed elsewhere
- stay aligned with the branch's filter tags, icon family, route name, and actual content
- hide or remain unavailable when showing it would reveal a deliberately hidden or unrevealed branch

Provide navigation entries for separate political route groups when they occupy distant regions and need separate access. Do the same for army, navy, air, economy or industry, diplomacy, expansion, crisis, or special-mechanic regions when they are large and spatially distinct. Do not add navigation buttons for tiny nearby side spurs.

Focus Navigation improves usability. It does not rescue a bad layout. A tree still fails if its branches are random, interleaved, overly distant without reason, or unreadable after the navigation shortcut moves the player there.
