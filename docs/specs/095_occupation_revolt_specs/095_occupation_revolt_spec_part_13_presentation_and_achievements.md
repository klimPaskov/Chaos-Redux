# Occupation revolt: presentation, assets and achievements

## What the player should understand

The opening presentation identifies the actual claimant, the territory that rose, the government's origin and the immediate military problem.
A report must not announce complete independence when the country has only seized a small base.
A government-in-exile return should feel different from a local provisional government emerging after annexation.
A dormant movement's first report concerns observable nationalist organization rather than an already victorious army.

Writing direction is concrete and country-aware.
Use the actual place, people, political relationship and military situation.
Do not make every uprising a mysterious radio broadcast, a changed map or a bureaucratic denial.
The event can include dry irony in appropriate political choices, but civilian suffering is not a punchline.
This package intentionally does not supply finished event descriptions, option text, news prose, achievement titles, quotes or audio selections.

## Information surfaces

Use the native decisions and missions interface for the campaign, the existing event log and detail surfaces for the shared event record, and ordinary map and war views for actual territory and military strength.
Readiness and Cohesion are the only custom persistent values the player must track.
Local preparation and route conditions are qualitative target information.
An occupier's view depends on detected evidence.
An ally's exact access to claimant information depends on the actual liaison agreement.

No new large custom GUI, custom world map mode or focus-tree inlay is required by this design.
If implementation discovers a genuine information problem that cannot be solved cleanly through these native surfaces, propose a bounded addition with reference and native-render evidence before building it.
It must remain within the same visible-value and action budgets.
A new interface must not become a substitute for implementing the underlying operations.

## Required report and news roles

The report-art package needs distinct role coverage for underground organization, an armed homeland opening, the return of a surviving government, a fragile regional base, a negotiated settlement and a failed revolt returning to exile.
Images can be selected contextually from those roles when geography or the government origin differs.
They must not depict a specific historical person or national flag unless that identity is appropriate to the current claimant.
A generic documentary-staged scene should remain visibly plausible for the 1930s–1940s setting.

The news-art package covers armed restoration, a major national settlement and a consequential regional cascade.
A news report may reuse an approved broad role across different countries when its actual image contains no false specific identity.
It cannot resize the report-event card and call that a separate properly produced news asset.
Each family has its own composition, final consumer and dimensions.

## Icons and country identity

The decision category needs a clear national-restoration emblem that remains readable at native size.
Operation icons should distinguish organization, material delivery, government settlement, local spread, integration, containment, evacuation and recovery.
Mission icons distinguish survival, supply connection, institutional agreement and postwar fulfillment.
A small coherent icon vocabulary may serve semantically identical operation variants.
It must not use one vague rebel symbol for every mechanically different action.

The focus tree needs branch-root, meaningful fork, program and capstone coverage corresponding to Part 09.
Specific focus nodes receive their final icon mapping during exact tree authoring.
Route icons should distinguish legal continuity, the resistance compact, emergency authority, rebuilding, procurement, the national army, maritime access and diplomacy.
Existing valid country flags and character portraits are preserved.
Missing real-person art follows the grounded portrait workflow rather than invented faces.

No new custom-unit model or bespoke 3D asset is currently required.
The formations are ordinary humans using supported native military roles.
An original template emblem can distinguish the national restoration force where the existing UI needs it, but does not imply a new battalion or equipment family.
Animation is not required to make the event complete.
Any later justified animation needs genuine source frames, a static fallback and native-size proof under the animation skill.

## A single conditional super-event

The working role is the regional collapse of an occupation order.
It can fire once per campaign after one recorded Liberation Cascade produces at least three distinct genuine national restorations or independence settlements, including the initiating country.
At least one qualifying outcome must remove a major occupier from an authentic national homeland.
Together the outcomes must remove at least 50% of that major occupier's initially tracked occupied authentic-home population in the cascade region, or end that major's occupation presence in that region entirely.
The initial denominator is frozen from the relevant actual occupied home states when the cascade forms and does not include the occupier's own homeland.

The trigger uses successful sovereign settlements or durable restoration outcomes, not merely country spawns.
A qualifying restoration must remain viable for 90 days after its settlement or completion of its survival-and-restoration objective.
Client-state outcomes do not count as independent restorations for this presentation trigger.
Repeated release and reconquest cannot create additional distinct outcomes.
A cascade of small local movements can be important gameplay without automatically qualifying for this world-order presentation.

The image direction concerns several national communities emerging from one occupation system, with material signs of a real transition rather than a generic victory crowd.
The final visual must avoid assigning one country's flag, leader or uniform to all claimants.
The text researcher must find a sourceable quotation and a culturally appropriate short remark only after checking fit and attribution.
The audio researcher must verify composition and recording rights separately.
No quote, track, title or registry slot is selected in this specification.
Those are explicit production and registry-verification tasks.

## Achievement set

All identifiers below are proposed and require collision inspection in the existing achievement registry.
Titles and descriptions remain directions.
Each achievement needs the complete color, grey and not-eligible icon triplet under the root achievement directory.
Debug-fired incidents and manipulated release/reannexation cycles are disqualified.
Use durable event receipts rather than reconstructing a supposed achievement from the current map alone.

### `chaosx_095_return_without_a_capital`

The working direction is a government that returned from genuine exile through a precarious first base.
Eligible countries are authentic displaced claimants whose original armed opening lacked their national center and controlled no more than 25% of their authentic homeland population.
The country must complete survival, recover its national center, secure an independent settlement or durable full restoration, and fulfill its government settlement within 365 days of the armed opening.
It must remain independent for another 90 days.
This is visible and hard because it combines a weak opening, military recovery and a completed political outcome.
The icon direction is a national seal recovered from a damaged field case, without a specific country's emblem baked into generic art.

### `chaosx_095_one_country_many_shores`

The working direction is a divided homeland reunited through several genuine centers.
Eligible countries require Evolution II and at least three physically disconnected authentic home components at the opening.
Each component must open with its own finite resource allocation, complete its initial survival or supply objective, and enter a single independent national settlement.
No component may receive a duplicated national opening budget.
The country must sustain all three for 90 days after settlement.
This is visible and very hard because geography, logistics and national coordination all matter.
The icon direction is several distinct island or regional markers joined by a restrained national command motif.

### `chaosx_095_the_uniform_changes_sides`

The working direction is a successful, honored integration of a real local occupation formation.
An authentic claimant must receive a verified Evolution III defection, preserve the formation's exact transfer accounting, integrate it under the agreed government arrangement and use the resulting military contribution in a successful restoration.
The formation or its properly tracked surviving successor must remain part of the national force through the settlement.
The claimant must fulfill its integration promise and remain independent for 90 days.
This is visible and hard because a random event notification or equipment transfer alone is insufficient.
The icon direction is a field insignia being replaced on an otherwise period-correct uniform, with no real national emblem invented.

### `chaosx_095_second_return`

The working direction is a second uprising sustained by actual survivors of the first.
The same authentic claimant must suffer a genuine territorial defeat, preserve a verified national leadership, network or military survivor record, meet the renewed-opportunity and cooldown conditions, and later achieve independent restoration.
Its second opening must not receive a duplicated initial cache or resurrect destroyed forces.
The country must then complete recovery and remain independent for 180 days.
This achievement is hidden and very hard because intentionally losing a trivial scripted revolt is not enough.
The icon direction is a repaired resistance emblem with visible old damage rather than two unrelated flags.

### `chaosx_095_an_empire_loses_its_grip`

The working direction is the initiator of a consequential liberation cascade.
The player's claimant must produce the initiating success for a valid Evolution IV cascade and deliver at least one real, useful support contribution to a different participating claimant.
The cascade must satisfy the super-event's three-national-restoration and regional-occupation-collapse conditions.
The initiating country must remain independent and fulfill its own governing agreement.
This is visible and very hard because it requires several actual successful national outcomes and contribution beyond merely triggering inspiration.
The icon direction is a broken common restraint releasing several distinct national seals, without using unrelated historical symbols.

### `chaosx_095_sovereignty_without_a_master`

The working direction is a difficult restoration that uses cooperation without surrendering sovereignty.
An authentic claimant must begin with an opening force smaller than the locally relevant hostile military force, receive and fulfill at least two distinct real foreign contributions from different sovereign supporters, achieve independent restoration and close its accepted support obligations without becoming a subject or betraying exclusive agreed terms.
The country must remain independent for 180 days after settlement.
The relative-force condition must use a verified comparable native or repository measure at opening, not raw division counts across incompatible templates.
This is visible and very hard because merely refusing all aid does not qualify.
The icon direction is an independent national seal beside fulfilled agreements and returned transport equipment.

## Presentation and achievement proof

Every asset needs source mode, source path, final consumer, dimensions, runtime path, visibility rule, production status and proof.
Research-only, placeholder, generated source, processed preview and final runtime art are separate statuses.
Every achievement needs a scenario proving a legitimate unlock and scenarios proving its principal disqualifiers.
A source-level trigger review is not an in-game or MCP-render pass.
The supplied package contains the design and production briefs, not finished art, licensed audio, verified quotes or implemented achievements.
