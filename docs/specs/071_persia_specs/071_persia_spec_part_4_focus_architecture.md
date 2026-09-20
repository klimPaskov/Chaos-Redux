# 071 Persia: focus-tree architecture

## Scope and pacing

This is a large, non-linear tree organized around path and branch contracts. The diagram shows branch relationships and important anchors. It is not a finished node layout, a list of exact coordinates, or an MCP-rendered game tree. The implementation owns the final node count, clean spacing, and detailed connections.

The common opening should take about 140 to 210 focus days to reach a route commitment, depending on the chosen side preparation. A short 35-day opening anchor gives immediate direction. Normal institutional and development focuses use 70 days. A small number of major conclusions may use 105 days when their effects justify it. Optional preparation remains available during war.

The tree must support useful choices from the start. A player choosing to repair supply should not be locked out of basic political settlement. A player choosing a route should not need to finish unrelated naval preparation first.

## Overall shape

A common restoration trunk sits above three mutually exclusive political routes. Shared military, industrial, air, naval, logistics, and reconstruction branches remain available around that trunk. Route-specific branches feed into shared systems through different terms and rewards. Evolutions extend the relevant systems without replacing the chosen route.

The interface should visually distinguish homeland preparation, political route, territorial projects, military development, and reconstruction. Focus filter tags should support those functions. The final layout must reserve enough space for the three routes and their side branches. This plan does not add a focus-tree inlay window, because the dedicated decision interface already holds the meter and territorial puzzle.

## Common trunk anchors

| Anchor | Prerequisite purpose | Player result |
|---|---|---|
| Review the restoration | Event fired | Opens the opening-force review and immediate homeland priorities |
| Establish provisional authority | Review complete | Makes the constitutional choices available without replacing the government |
| Secure the homeland base | Review complete | Opens recovery projects and the first supply repair program |
| Settle the restoration | Provisional authority plus a workable administrative center | Locks the chosen political route |
| Recognize an imperial order | Route institutions and recovered homeland | Converges into earned route conclusions and advanced imperial diplomacy |

The homeland base is a practical side branch. Complete recovery is required for final imperial conclusions, but is not required just to choose a route. This keeps remnant Iran playable.

## Achaemenid branch groups

The political group builds a crown or constitutional imperial office, regional charters, and an assembly. The territorial group splits between westward and eastward networks. The development group funds roads, administrative centers, and negotiated obligations. A tolerance policy and a coercive emergency policy are a meaningful fork, with an explicit way to end emergency rule later.

Its convergence requires a functioning set of regional settlements and connected imperial communications. The widest border project is an optional late ambition, not the only valid ending. A compact chartered empire can complete the political route while leaving Egypt or the Indus for a later campaign.

## Sasanian branch groups

The political group establishes central command, military districts, and oversight of senior commanders. The western and eastern frontier groups can be developed in either order. The army group specializes in strong formations, armor, prepared defensive lines, and reliable operational supply.

Its internal fork concerns military command power. Entrenched frontier commanders can defend and administer effectively, while a centrally appointed command system limits their autonomy at a real cost in local flexibility. Both paths can succeed. A command system that has never been tested by a crisis cannot claim that all rivalry has disappeared.

## Modern branch groups

The political group retains or reforms the current constitutional order. The economy group offers domestic production, foreign concessions, and later renegotiation. The diplomatic group develops clients, access agreements, and an imperial market. The military group joins mechanization to oil, production, air support, and maritime logistics.

Its internal fork concerns how influence is funded. Direct state-led investment gives the center more control and immediate costs. Concession-led development can grow faster but creates obligations and dependency. Neither option gives permanent free factories without a construction or contract process.

## Shared branches

Industry contains home workshops, arsenals, heavy industry, and rebuilding after war. Logistics contains rail corridors, depots, motor transport, and desert support. The army contains training, staff work, standard equipment, and terrain specialization. The Immortals sit alongside the army as an elite family with their own capacity and replacement costs.

The air branch supports fighters, battlefield support, transport infrastructure, and later long-range operations. The naval branch starts with ports, crews, dockyards, and coastal protection before expanding toward a regional fleet. Intelligence and diplomacy support reconnaissance of targets, foreign missions, and treaty management without inventing a separate intelligence currency.

Shared branches continue to work after a route's political conclusion. A country that has chosen a modern bloc can still restore Persepolis. An Achaemenid empire can still develop tanks and aircraft. A Sasanian state can still negotiate a charter instead of annexing a distant region.

## Branch contract format

Each branch in parts 5 to 8 specifies its entry, anchors, choice, output, tradeoff, and recovery. The implementation can divide an anchor into several focuses when the gameplay has distinct stages. It must not inflate the tree by turning one small modifier into several empty steps.

An anchor that opens a construction program should display the program it unlocks. An anchor that grants an elite family must also create a route to obtain its equipment and reinforce it. A regional ambition must show the regions it unlocks. A political focus must describe which institution or obligation changes.

## Route locks and convergence

Only one main political route can be committed. Shared focuses remain independent unless their theme genuinely conflicts with the chosen settlement. A later government change adapts the route rather than silently unlocking the two others.

For final connections, alternatives belong to one OR requirement and cumulative conditions belong to separate AND requirements. The exact syntax must be checked against local documentation. The visual layout must represent the same logic that the engine evaluates.

A bypass can recognize an already completed factual objective, such as an existing railway or already secured homeland. It must not pay the construction reward again. A focus that changes political institutions cannot be bypassed merely because a province happens to be owned.

## Evolutions and crises in the tree

Evolution I opens deeper satrapy charters and court management. Evolution II opens the strongest guard command development. Evolution III opens supremacy and imperial guarantee branches. These appear as extensions with their own requirements. An evolution alone does not complete their construction, recruitment, or diplomatic effects.

Crisis focuses temporarily offer a recovery path when a real crisis occurs. They do not form a fourth prestige route. They can restore the administrative center, negotiate a revised charter, or reorganize a divided command. A recovery focus does not refund the opening force or erase the consequences of lost territory.

## Technology graph design

The baseline tree improves conventional Iranian research and equipment production. It does not grant every technology owned by a major power. Any new guard unlock or equipment support must have a declared prerequisite, a visible consumer, and a reinforcement path.

The guard family should preferentially use standard infantry, support, motorized, and mechanized equipment families where compatible. A custom elite subunit can provide identity without requiring a separate fictional rifle technology tree. Any truly new technology must be inspected, rendered, and compared through the required technology tools in implementation.

## Acceptance

The final tree must remain readable at supported game resolutions. No disconnected anchor, contradictory route lock, unfinishable foreign-state condition, or forced naval dead end is acceptable. A landlocked empire can build toward access without pretending it already has an ocean fleet. A remnant can choose a route before reunification. Each main route has a meaningful political conclusion, a territorial strategy, and useful post-conclusion development.
