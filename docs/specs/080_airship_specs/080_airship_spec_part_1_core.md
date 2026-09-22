# Event 080: Airship
## Part 1: The voyage

## Catalog entry

| Field | Value |
|---|---|
| Event ID | 80 |
| Event name | Airship |
| Type | Minor Fire-Once |
| Status | To Be Reworked |
| Chaos level | 1 |
| Cluster | None |
| Evolution I | The Grand Tour, eligible at 200+ Chaos |
| Evolution II | Experimental Flight, eligible at 400+ Chaos |
| Evolution III | The Flying City, eligible at 600+ Chaos |

## The experience

The United States sends a giant civilian passenger airship around the world. The player follows a single expedition across a changing political map. The ship carries people with different reasons for travelling, depends on foreign ground crews, and enters airspace that may have become hostile since departure. A prosperous host can turn a visit into a public celebration. A country fighting for survival can treat the same arrival as an unwelcome security problem.

The voyage has three recurring decisions: whether to spend time on safety, what to do with the people aboard, and how much risk to accept for prestige or useful aviation work. Airship Condition is the central management value. Route progress and the number of people aboard provide context. There is no separate prestige, happiness, fuel, diplomacy, research, and suspicion bar to maintain.

The map remains the event's main interface. It should tell the player where the ship is, where it has been, what lies next, why it is delayed, and which country is currently responsible for the ground beneath it. The trip remains interesting during a peaceful campaign through passenger stories, stops, mechanical problems, scientific work, and diplomatic choices. War adds another source of danger without becoming a prerequisite.

The United States controls expedition policy. A host controls its own reception, inspections, ground assistance, and response to incidents. A passenger's country of residence can receive a narrowly relevant message about a serious individual incident. Other countries normally receive only occasional international news.

All figures introduced in these parts are proposed balancing values. The user's catalog classification, 121-step route, two-day movement, foreign-controller retaliation, and three evolution thresholds are fixed requirements. Neutral content labels in tables are planning labels, not finished localisation.

## Launch

The event becomes available when the United States exists as a normal civilian country and can launch from the existing route's American departure location. It must control a valid departure site and have enough real civilian population to support the initial manifest. Being at war does not by itself prevent departure. There is no prerequisite American air superiority, special research, or victory in an existing war.

The event launches the ship when it fires. It does not ask the player to buy an unlock with Political Power or repeat a preparation chain. The opening introduces the route, the manifest, Condition, and the consequences of a foreign crash. It establishes a civilian expedition funded before the event began. No military airship unit or new aircraft technology is created as a substitute for the expedition.

The opening ship has Condition 100 and a proposed complement of 500 passengers and 100 crew. These are fictional design figures for this giant airship. They are not claims about the capacity of a historical model. The manifest must be backed by actual people under the population contract in Part 3.

The launch notification tells the United States about its next practical choice. The departure news tells the world that the voyage has begun. Countries along the entire route do not all receive a personal welcome event on launch day. They become hosts when the ship actually reaches their territory.

## The 121-step journey

The existing route is retained in its original order. Departure is position 0. There are 121 subsequent progression transitions, ending at position 121. Position 0 is not an extra travel step.

| Moment in an uninterrupted voyage | Position |
|---|---:|
| Departure | 0 |
| After 2 days | 1 |
| After 20 days | 10 |
| After 120 days | 60 |
| After 240 days | 120 |
| After 242 days | 121, completion after arrival resolution |

Each ordinary transition consumes two days. Planned basic servicing and ceremonies are included in the abstract travel window attached to a stop. Repairs, detention, searches, diversions, refits, and extended visits add time. They never create extra numbered route positions or reduce the required 121 transitions.

A stop can contain a reception and a repair choice without each activity adding an automatic extra two days. Only an explicitly displayed extension changes the schedule. The map distinguishes scheduled service from an additional delay.

At a delay, the marker remains at the actual location. The interface displays the reason and remaining time. It must not visibly advance while the ship is undergoing repairs. When a pause begins partway through a travel window, the unspent travel time is retained. Finishing a pause does not grant an instant free transition or require the player to repeat travel already completed.

Every arrival resolves its relevant flight exposure before receiving stop benefits. The final arrival is subject to this same rule. Reaching the last approach with a critically damaged ship is not immunity from a final accident.

## Locations and hosts

The route's geographic position and the political controller are separate facts. A route location stays geographically fixed while its controller can change. At every arrival and important ground interaction, the current controller is resolved from the actual state at that position.

An occupation therefore changes the host. An owner who has lost control cannot welcome the ship, charge for its repairs, or become the target of automatic retaliation merely because it retains ownership. A change of controller during an extended stop moves unresolved host responsibilities to the new controller. The previous host retains credit only for help it actually delivered.

Some legacy route positions have no land-region match. They must be checked against the original artwork and geography. Once a position is confirmed as open water, it has no territorial host. Ordinary onboard reports then go to the United States. An ocean crash has no invented impact state and creates no automatic war against the last country visited. A deliberate attack over water may be reported as an attack, but it does not silently extend the user's territorial-crash rule into a new automatic retaliation rule.

The design does not supply invented city names, stop coordinates, or a replacement itinerary. Exact state bindings and original stop markers must be recovered from the existing map. The separate route crosswalk preserves the inspected legacy region sequence and identifies the remaining binding work.

## Stops

Retain the existing planned stops. Give each one a primary service role and a secondary content role using its actual location, facilities, and controller. A role describes what happens at an existing stop. It does not add a new stop to the route.

| Stop role | Main opportunity | Main pressure |
|---|---|---|
| Routine service | Refuel, basic checks, provisions, passenger exchange | Poor facilities can require an extension |
| Technical service | Major repairs, specialist inspection, an eligible refit | Longer ground time and equipment costs |
| Diplomatic visit | Reception, foreign guests, press access, bilateral goodwill | Protocol disputes, protests, inspections |
| Commercial visit | Sightseeing, merchants, tourist spending, local publicity | Crowding, customs disputes, missed departures |
| Scientific visit | Weather work, technical demonstration, exchange of observations | Experimental failure and security suspicion |
| Landmark visit | A distinctive view and a rare international report | Public expectations encourage risky scheduling |

A damaged or occupied location can lose its ability to provide a particular service. The geographic stop still exists. The ship can make a reduced visit, wait for assistance, or undertake an emergency diversion. This makes the fixed route responsive to the campaign without replacing it with a procedurally generated tour.

At most three ordinary landmark stops receive worldwide arrival news in one voyage. Selection follows the recovered stop order and spreads coverage across the trip. The departure city and final homecoming do not consume those three slots.

## Diversions

A diversion is a temporary movement away from the current route segment for a stated purpose, such as escaping an attack or reaching a usable landing ground. It must have an actual geographic destination and an additional travel cost. It does not count as completion of an unvisited canonical step.

After the diversion, the ship returns to the pending route connection and continues through every remaining canonical step. Already completed positions are not awarded again. An emergency landing in another state changes the actual host and the possible crash location while the diversion is active.

The map retains the canonical path and draws a temporary branch. A diversion that cannot be represented accurately is an implementation blocker. Replacing it with a random state in a large strategic region would change the central premise of the event.

## Voyage phases

| Phase | Player focus | End condition |
|---|---|---|
| Underway | Condition, next stop, standing orders, active experiment | Next route arrival or a serious incident |
| At a planned stop | Service, local programme, passenger handling | Normal departure or a declared extension |
| Delayed | Complete the named repair, negotiation, or search | Work finishes, a different response is chosen, or the voyage is ended |
| Emergency | Landing, evacuation, rescue, or acceptance of a dangerous continuation | Ship stabilises, becomes lost, or crashes |
| Missing | Search and communication recovery | Contact restored, a confirmed loss, or a bounded unresolved-loss ending |
| Completed | Homecoming and earned rewards | Terminal |
| Crashed | Immediate impact, retaliation, survivor recovery | Flight terminal, shared aftermath may continue |
| Aborted | Safe withdrawal from the voyage and passenger settlement | Terminal |

A safe abort is allowed at a usable landing location. It gives no completion reward and does not reopen the fire-once event. It remains a meaningful alternative to forcing a broken ship through another hostile region. Capture or permanent impoundment can also end the expedition without a crash. The distinction matters because the automatic war rule is tied to a crash in foreign-controlled territory.

## Participation and visibility

The United States always has the expedition view. Other human countries can inspect the public voyage map while the event is active. Host decisions appear only where the current situation gives that country something to do. A departing host's unresolved rescue or missing-passenger task can remain visible until its own deadline, but the old host does not retain flight control.

Routine updates go into the expedition's own voyage notes and map state. They do not each create a separate random-event history row. The event pool records one Event 80 firing. Subsequent developments belong to that same voyage.

Only Condition, route progress, and people aboard are persistent headline values. A contextual delay timer or experiment result can appear in the current task panel. The player is never asked to manage a fourth permanent risk or morale meter. Warnings explain the relevant causes of danger in ordinary language and expose the actual probability through a detailed tooltip where supported.

## Endings

Success means completing all 121 progression transitions and surviving the final arrival. Crash means a physically destroyed ship, with real casualty and damage resolution. Safe abort means the ship and surviving people leave the expedition at a valid landing location. Permanent capture means the voyage ends with a grounded ship and an unresolved political outcome, followed by bounded passenger-release work. Confirmed ocean loss ends the voyage without assigning a false land controller.

These endings are mutually exclusive. A delayed success report cannot overwrite a crash. Rescue and fire recovery can continue after flight has ended, but they never restart the route or grant a second launch.
