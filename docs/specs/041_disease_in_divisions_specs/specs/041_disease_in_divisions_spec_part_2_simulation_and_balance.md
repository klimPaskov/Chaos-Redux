# Event 41 simulation and balance specification

## Simulation purpose

The hidden simulation should produce believable military disease behavior without asking the player to track a medical ledger. It needs enough structure to distinguish a supplied rested army from a crowded exhausted army, while remaining bounded enough for reliable HOI4 performance and clear AI use.

The simulation should operate only for registered active episodes and registered affected formations or sector nodes. It should not search the whole world for disease every day.

## Episode ledger

Each active national outbreak needs an episode record containing the following categories of state:

- original outbreak country
- current episode generation
- hidden disease profile
- opening sector and active sector nodes
- registered affected formations or safe formation proxies
- pressure and pressure trend
- active sick manpower estimate
- convalescent manpower estimate
- cumulative military deaths
- medical capacity score
- evacuation capacity score
- sanitation and quarantine states
- operational posture
- recent spread and recent no-spread windows
- first-manifestation and Chaos milestone guards
- evolution state at the episode level
- links to secondary national outbreaks created by the same episode
- civilian spillover handoff receipts when Evolution II is active
- resolution and cleanup state

The implementation can represent some of these through flags, variables, arrays, dynamic modifiers, or event targets. The design requirement is that each episode can be traced, bounded, and cleaned without relying on whole-world reconstruction.

## Processing cadence

The preferred rhythm is a bounded weekly disease pulse for each active country. A shorter internal delay can be used for reports or decision completion. Mortality, recovery, pressure movement, and spread should normally settle on the weekly pulse so the player can understand trends.

A monthly pulse is too slow for an active frontline crisis. A daily global pulse is too broad and would create noisy movement. Weekly processing gives enough time for decisions to matter and enough granularity for a deteriorating front to become urgent.

The active-country registry should contain only countries with an unresolved Event 41 outbreak. The affected-formation or sector registry should contain only the units or nodes needed by those countries. Resolved entries must be removed promptly.

## Sector nodes

A sector node is the event's bounded representation of one military disease environment. It can correspond to a frontline state group, shared supply hub, staging state, port, or military hospital corridor.

Each node tracks hidden exposure and recovery conditions. A country can have more than one active node only after spread has occurred. The baseline should usually remain within one or two connected nodes.

Useful node inputs include:

- number and density of friendly formations
- current combat activity
- average supply state
- infrastructure, railway, and hub condition
- weather and terrain
- local field-hospital coverage
- local bombardment or disaster damage
- local chemical or biological contamination
- famine and displacement pressure
- transport access to safer rear states
- time since the last active combat
- current quarantine or sanitation action

A node should not become a second public value. Its status can be communicated through map color, an icon, a short tooltip, and a working label such as isolated, spreading, severe, or recovering.

## Exposure model

Each weekly pulse evaluates only registered affected nodes and a bounded set of valid connected candidates.

### Same-sector exposure

The strongest baseline transmission occurs among formations that share the infected sector. Risk rises with formation density, combat, low supply, field-hospital crowding, and profile-friendly conditions.

### Neighboring-sector exposure

A connected neighboring node can be tested when formations rotate, retreat, advance, or draw supply through the same route. Baseline neighboring spread should be slower than same-sector spread.

### Rear-area exposure

Staging areas, medical hubs, depots, and transport states can become military nodes when sick troops or contaminated supplies move through them. In the baseline, this remains a military problem and does not create civilian cases.

### Distant-theater exposure

Distant military transmission is normally absent in the baseline. It becomes available through coalition logistics and long transport chains under Evolution II.

## Formation infection states

An affected formation can move through four hidden states.

### Exposed

The formation has shared a dangerous environment but has not yet received the full disease penalty. This state supports delayed spread and gives sanitation or rotation a chance to stop the case.

### Active

The formation has a meaningful sick population and receives the visible disease modifier. It contributes strongly to pressure and can transmit within its node.

### Recovering

New cases have fallen, but the formation remains under-strength or medically restricted. It contributes less transmission and more convalescent burden.

### Cleared

The temporary disease modifier has ended. The formation retains short resistance to immediate reinfection during the same episode.

The player does not need to see these exact internal labels. The unit or sector tooltip should communicate the practical condition through a compact status line and the main penalties.

## Pressure calculation model

Army Infection Pressure should be rebuilt from hidden inputs at each weekly pulse, then moved toward the new value with bounded change. This prevents arbitrary stacking and allows old conditions to fall away when the player improves the front.

A useful conceptual model is:

`burden + exposure + operational strain + medical overload + environmental risk - active containment - recovery capacity`

### Burden component

Burden reflects the affected share of the sector, the number of active formations, the active sick pool, and the convalescent backlog.

A large country should not automatically suffer higher pressure merely because it has more divisions. The important comparison is affected formations against the selected sector and medical capacity. A small country with four affected divisions can face a worse crisis than a major with six affected divisions.

### Exposure component

Exposure reflects formation density, shared nodes, recent movement, active combat, hospital crowding, and the hidden disease profile.

### Operational strain component

Operational strain reflects offensives, sustained battles, attrition, repeated movement, forced marches, retreats, and inadequate rest.

### Medical overload component

Medical overload compares sick and recovering manpower against field hospitals, support equipment, trained medical capacity, transport, and available rear-area access.

### Environmental component

Environmental risk reflects weather, terrain, infrastructure, bombardment, contamination, famine, displacement, and profile-specific conditions.

### Containment component

Containment reflects active decisions, quarantine, sanitation, supplied rear rest, transport assignment, repaired routes, and a pause in offensive operations.

### Recovery component

Recovery reflects time without new spread, field-hospital strength, medical technology, supply, infrastructure, profile-specific recovery speed, and the remaining convalescent burden.

## Bounded pressure movement

Ordinary weekly change should usually stay within a moderate band. A successful comprehensive response can produce a clear fall. A dangerous week of combat and supply collapse can produce a clear rise. The meter should not oscillate wildly from one minor condition change.

Recommended movement targets:

- stable mixed conditions should move pressure by only a few points
- one effective action should usually shift the trend and produce a visible result over two or three pulses
- two complementary actions should be able to reverse a moderate outbreak
- high pressure should resist quick reduction until the affected formations are rested or evacuated
- a catastrophic pulse should require several severe factors or a defined escalation event

The exact values belong in centralized tuning. The design needs clear thresholds, caps, and diminishing returns.

## Medical capacity

Medical capacity is hidden and derived from existing country and division systems.

Positive contributors can include:

- field-hospital support companies and their technology level
- relevant medical or support technologies
- support equipment availability
- manpower assigned to the medical response
- military hospital or related Chaos Redux capacity where implemented
- infrastructure and supply in rear states
- sufficient trains, trucks, fuel, and safe evacuation routes
- high organization of the response and prior preparedness

Negative contributors can include:

- field hospitals already overloaded by battle casualties
- low support equipment
- destroyed railways, ports, and infrastructure
- encircled or isolated formations
- heavy bombing and disaster damage
- several active disease nodes
- Evolution II civilian demand competing for medical capacity

The player sees the resulting medical status as a qualitative label and through action effectiveness. A raw medical capacity meter is unnecessary.

## Evacuation capacity

Evacuation capacity measures whether sick soldiers can leave the affected sector.

It should depend on:

- available trains and motorized equipment
- fuel
- intact railway or road connections
- secure rear states
- ports and convoys when the sector is overseas
- enemy air pressure and bombardment
- whether the player has assigned transport to medical use

Low evacuation capacity raises mortality and lengthens recovery. High evacuation capacity moves active sick personnel into the convalescent pool faster, which reduces transmission but can temporarily deepen the under-strength appearance of the sector.

## Sanitation and clean supply

Sanitation should affect every profile, with different strength.

The action can represent:

- clean water and food control
- bathing and laundry
- delousing and vector control
- replacement of contaminated bedding and camp stores
- waste disposal and latrine discipline
- isolation of sick tents and hospital wards
- inspection of depots and kitchens

The simulation should reward sanitation most where the relevant supply route is secure enough to deliver the material. A sanitation order in a cut-off sector should have limited effect unless the player first restores access.

## Operational posture

The episode uses one current military posture toward the outbreak.

### Preserve operations

This is the default posture. The army keeps ordinary freedom of action. Pressure changes through normal conditions.

### Restrict offensive operations

The army accepts lower attack tempo, planning, and movement flexibility in the affected sector. Active combat exposure falls, rotation becomes more effective, and pressure can decline faster.

### Fight through the outbreak

The country deliberately preserves or increases offensive tempo despite the disease. The stance can protect a time-sensitive offensive or threatened capital. It raises infection, mortality, and medical overload. It should not give a free attack bonus. Its benefit is the absence of the restrictions imposed by medical control and the ability to use a short-lived operational effort when the player judges the risk worthwhile.

The stance should be visible as a status label and should be changeable only after a meaningful cooldown or commitment period. The player should not be able to switch every few days to gain the safest parts of each stance.

## Manpower accounting contract

This event is built around real military manpower consequences. The implementation must prove each transition.

### Opening sickness

The opening moves a bounded number of soldiers from available duty into the active sick ledger. It creates matching formation or sector penalties. It does not register deaths and does not delete equipment.

### New infections

Each spread pulse adds only the new estimated sick manpower for newly affected or worsening formations. It must not re-debit the entire infected formation every week.

### Recovery transition

When active cases improve, soldiers move into the convalescent ledger. They remain unavailable for a profile-dependent delay.

### Return to duty

Recovered soldiers return in bounded installments. The return should reconcile the convalescent ledger and remove the matching unavailable-manpower burden. It should never create more manpower than the episode removed.

### Fatal transition

Fatal cases leave the active sick or convalescent ledger and are registered once as military deaths. The fatal amount should be capped by the remaining people in those ledgers.

### Episode close

Cleanup reconciles any small rounding remainder, returns valid survivors, preserves permanent deaths, and clears the event-specific ledgers.

If direct formation manpower transactions prove impossible, the implementation must use an engine-verified proxy that preserves these accounting outcomes. A proxy that destroys equipment, converts all sick soldiers into deaths, or creates free manpower is unacceptable.

## Mortality model

Deaths should follow prolonged failure and medical overload. They should not be the main opening punishment.

Fatality risk rises with:

- high Army Infection Pressure
- long time in active infection
- failed evacuation
- low medical capacity
- severe supply isolation
- heavy combat while sick
- contamination and biological warfare exposure
- famine and ruined infrastructure
- Evolution II medical competition with civilian cases

Fatality risk falls with:

- strong field hospitals
- supplied rear treatment
- evacuation
- sanitation and clean supply
- early rotation
- time without combat
- preparedness from a recent successful outbreak

The hidden profile changes the ratio between readiness loss, recovery time, and fatality. Camp-borne fever should usually create wide sickness with lower mortality. Enteric disease should become lethal when clean supply and hospitals fail. Tropical disease should create long recovery and recurring exposure.

## Balance bands for military losses

The following bands guide tuning. They are not guaranteed outcomes and should scale with the size of the affected sector.

### Successful early containment

- a small affected share
- low permanent deaths
- a short convalescent tail
- no more than a modest temporary loss of combat power
- resolution within roughly two to four months

### Costly containment

- several formations under-strength
- meaningful but limited military deaths
- transport and production committed for several months
- one front loses tempo
- resolution within roughly four to seven months

### Failed baseline management

- the infected sector approaches half effective strength
- pressure remains above the operational epidemic threshold
- permanent military deaths become strategically visible
- medical exhaustion lasts after transmission ends
- resolution can take most of a year without decisive intervention

The event should scale with the country. It should not routinely erase a small country's whole recruitable population or generate millions of deaths from a limited baseline sector.

## Spread chance and protection

Spread should be calculated from exposure conditions and then checked against protection.

### Exposure strength

- active cases in the source node
- formation density
- shared front or supply link
- combat and movement
- hidden disease profile
- pressure stage
- evolution state

### Protection strength

- medical capacity
- sanitation
- quarantine
- strong supply
- rest away from combat
- cleared-formation resistance
- recent national preparedness
- intelligence warning for secondary countries under Evolution I

This approach lets a strong army prevent spread without granting absolute immunity.

## Report cadence

The event should not fire a popup for every weekly change. Reports should mark material milestones.

Useful report thresholds include:

- first spread beyond the opening group
- first sector reaching severe status
- medical capacity becoming overloaded
- the affected front approaching the half-strength danger band
- successful reversal from high to moderate pressure
- resolution entering the final recovery window
- first cross-border military transmission under Evolution I
- first civilian spillover under Evolution II

Routine changes belong in the category, map status, and tooltips.

## Repeatability

A fully resolved country receives a recent-survivor resistance state. This state should reduce selection weight and opening severity for a substantial period.

Recommended behavior:

- strongest protection during the first nine to twelve months after resolution
- fading protection for several additional months
- earlier vulnerability when the country suffers biological warfare, severe contamination, infrastructure collapse, famine, or a new War Plague episode
- no protection while the previous outbreak is unresolved

The resistance state represents learned sanitation, field medicine, command awareness, and stocked procedures. It should not make the country permanently immune.

A repeat firing should usually select a different sector or hidden profile when the campaign state supports it. Repeated identical outbreaks in the same place should be uncommon unless the country has failed to correct the original conditions.

## Edge cases

### War ends during the episode

Transmission pressure from combat should fall sharply. Demobilization and returning troops can still create rear-area military risk. Under Evolution II, an uncontrolled high-pressure episode can gain civilian spillover risk during demobilization. The country keeps the temporary category until the military outbreak resolves.

### Country is annexed

The episode must transfer or close safely. A valid ordinary controller that inherits affected formations and medical nodes can receive a reduced continuation. Invalid or special Chaos controllers should trigger cleanup and route any valid existing civilian outbreak through its own owner system.

### Civil war begins

Affected formations and nodes should be divided by actual control where the engine can prove ownership. Each successor receives only its valid inherited burden. The split must not duplicate sick manpower or deaths.

### Front disappears

Affected formations move into recovery. Pressure can fall quickly if they are supplied and rested. The episode should not end instantly while a large convalescent pool remains.

### Encirclement

Encircled infected formations face poor evacuation and higher mortality. Response actions that require transport or safe rear access should be blocked or weakened with clear text.

### Overseas theater

Evacuation may require ports, convoys, and secure sea access. A country without a viable route can still use local sanitation, quarantine, and field hospitals, but it cannot receive the full effect of strategic evacuation.

### No safe rear state

The rotation mission should choose another valid action path. The player must never receive an impossible target. Quarantine in place or emergency field hospitals can become the main response.

## Performance and cleanup standard

The event should use:

- a global or event-owned registry of active outbreak countries
- country-local registries of affected nodes and formations or safe proxies
- bounded weekly processing
- event-owned delayed work
- immediate removal of invalid entries
- generation or sequence proof for cross-border and civilian handoffs
- full cleanup after resolution, annexation, invalidation, or a global terminal transition

It should avoid:

- daily iteration over every country
- daily iteration over every division in the world
- repeated scans of every state
- permanent hidden modifiers after the episode closes
- stale event targets that can route a later episode into an old country
- a spread check that can infect the same formation or country repeatedly without state change
