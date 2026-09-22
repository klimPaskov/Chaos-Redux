# Part 2: Landing geography and operational objectives

## California first

California is the first region considered for the main landing.
A southern California opening puts Japan near the Los Angeles and San Diego area and gives it a long northward campaign.
A central or northern opening makes the Bay Area and the approaches to the Central Valley the first operational problem.
Both create recognizable California campaigns without requiring the whole state to change control at baseline.

The exact province bundles must be built from the installed map and inspected before coding.
Historical place names describe the intended geography, not verified province IDs.
The old event's use of state 378 proves what its old script selected, but it does not prove that the current map, ports, victory points, or state subdivision are unchanged.
The map worksheet in `reference/074_geography_and_capability_checks.md` defines the required resolution.

## Regional profiles

The labels in this table are design working labels and must not be copied into final localisation without a writing pass.

| Profile | Opening character | First expansion | Main risk |
| --- | --- | --- | --- |
| Southern California | A port-centered position around the southern urban coast | Link the southern ports and move toward the Central Valley | A narrow coastal corridor can be cut from the interior |
| Bay Area | An occupied harbor district with access toward nearby inland routes | Secure the bay approaches and a route toward Sacramento | Disconnected control around the bay can create unusable supply assumptions |
| Oregon coast and Columbia approach | A northern fallback with fewer immediate urban prizes | Establish a usable coastal route toward the Portland area | A river port must not be treated as a directly accessible ocean beach |
| Washington and Puget approach | A northern fallback or additional high-tier theater | Secure the actual approaches to the Seattle and Tacoma area | Apparent proximity on the map can conceal separate crossings and pockets |

Select between safe California profiles according to the actual geometry and existing occupation.
When several are equally suitable, a bounded random choice can vary the campaign.
The score must not make weak American defenses or a healthy Japanese navy a strategic prerequisite.
Oregon and Washington follow only when California cannot provide a safe usable opening, or when a higher-tier bundle needs additional entry points.

## Opening footprint

| Initial tier | Intended occupied states | Port and entry-point anchor | Occupied province anchor | Operational shape |
| --- | --- | --- | --- | --- |
| Baseline | Part of one Pacific state | One principal working port, a second if the bundle supports it | Roughly 4 to 6 | One compact pocket with deployment depth |
| Pacific Army | A broader position in one state | Two working ports | Roughly 6 to 10 | One defensible coastal district with room for concentration |
| The Western Invasion | Parts of two or three Pacific states | Three to four working ports | Roughly 10 to 15 | Two or three positions that need to be connected |
| Invasion of America | Several western coastal positions, preferably all three Pacific states | Five to six working entry points | Roughly 15 to 25 | A large western theater with separate expansion directions |

The province numbers are geometry targets, not mandatory counts to fill with disconnected tiles.
Ports, deployment depth, land connections, and supply coverage take priority over a cosmetic province quota.
Automatic occupation stays in the Pacific landing footprint.
Nevada, Arizona, Utah, Idaho, and other inland regions become objectives for normal combat.
No tier scripts an instant advance to Chicago or Washington, D.C.

A whole coastal state can change control at a high tier only when its provinces genuinely belong to the selected safe footprint.
Do not use full-state transfer merely because it is easier than defining coherent pockets.
Do not change ownership in order to simplify a control problem.

## Legality and existing occupation

A new occupied province must belong to the United States on the current map, lie in the eligible contiguous Pacific mainland region, and be a legal Japanese wartime target.
An already Japanese-controlled American-owned coastal position can host part of the incoming army.
That is useful when Japan already has a small mainland foothold, and it does not require a second landing episode.
The report must then describe the real reinforcement and expansion of the mainland front.

Do not take allied-controlled or neutral-controlled provinces away from another country solely to complete the desired shape.
Where a third-party occupier is also at war with Japan, a separately validated hostile-control profile may be considered, but the first implementation should prefer direct American control and existing Japanese control.
Any extension must preserve the user's availability rule and the current wars without starting a new one.

Existing American and allied formations are not deleted, converted, disbanded, or teleported out of an entire state.
Prefer safe deployment depth around the selected contested coast.
The engine behavior when controller changes intersect a defending division is a release-blocking prototype, not an excuse to move every army in California with a broad state-level effect.

## Distribution of the army

Place line formations along the outer approaches, assault formations near the intended breakthrough, and the mobile reserve behind the front near transport access.
Spread formations over several valid provinces before the simulation advances.
A port province is an unloading anchor, not the mandatory spawn location of every division.

Each detached high-tier pocket receives enough infantry to hold its perimeter and enough transport capacity to operate until it can connect to another pocket.
Do not allocate nearly all combat strength to California while leaving the northern entry points as undefended flags.
Use an opening distribution around 60 percent in the main region and 40 percent across secondary regions at tier II, and around 50 percent in the main region at tier III.
The actual map and supply test can move these proportions in steps of five percentage points.

No force is silently withheld to make a failed port-capacity test pass.
When the selected bundle cannot support the promised opening, improve the bundle, choose another valid profile, or keep the placement unresolved.

## Objectives that change the campaign

The first Japanese objective is a second working port or a transport junction outside the scripted footprint.
This makes early progress depend on combat and gives the United States a clear place to resist.
The next objective is a land connection between occupied districts, followed by a route toward the interior.

The objective selector chooses a reachable target from a small, inspected western registry.
A named city is only offered when its current province, controller, approach route, and supply role make it useful.
Do not offer already-secured objectives as completed achievements, invent railway connections, or target a neutral city because its historical name fits the story.

| Direction | Japan gains through successful fighting | United States can contest |
| --- | --- | --- |
| Complete California | A larger connected operating area and more industry under ordinary occupation | Valley junctions, urban approaches, and the corridor between ports |
| Advance north | Additional unloading capacity and another route around a fixed front | Coastal bottlenecks and links between detached Japanese positions |
| Move into the interior | Depth, inland supply hubs, and pressure on western defenses | Mountain approaches, desert transport routes, and the exposed supply trail |
| Secure port redundancy | A front that survives the loss of one unloading point | The newest and least-developed access point |

The transport network itself is the reward for conquest.
Occupation does not instantly restore full factory output, erase resistance, create cores, or grant the contents of every American warehouse.

## Changing objectives

If another country takes a target before the Japanese operation reaches it, the mission either selects one valid replacement within its original region or cancels without a penalty.
It does not chase new targets around the world.
A target lost through ordinary combat remains a legitimate setback.
A target that becomes neutral or disappears through an external map change is an invalidation case.
These outcomes must be presented differently.

## Defeat and recapture

The United States can isolate a pocket by taking its working ports and cutting its land connection to another supplied Japanese position.
Japan can restore access by winning a normal battle for a port or reconnecting to a retained access point.
No later event recreates an occupied American province after that province has been retaken.

A report about a lost bridgehead should describe lost coastal control.
It must not claim that every Japanese soldier was killed when isolated formations still exist inland or when the engine cannot prove their destruction.
Surviving formations continue to follow normal combat, retreat, surrender, and supply rules.
