# Event contract

## Catalog identity

| Field | Accepted value |
| --- | --- |
| Event ID | `38` |
| Entry event | `chaosx.nr38.1` |
| Event name | Malta Crusaders |
| Type | Minor Fire-Once |
| Minimum Chaos level | 1, Calm World |
| Status before implementation | To Be Reworked |
| Cluster | Formables |
| Cluster ID | 6 |
| Member severity | High |
| Public world-end route | The Holy World |
| Manual scenario | Believers vs Nonbelievers |

The event must remain unavailable to normal selection until its complete implementation is ready. Registration, default enablement, Event Details, cluster data, scenario data, and workbook status change in the same final implementation tranche.

## Playable promise

The event turns Malta into an armed crusader state that has already seized a small network of Mediterranean and Holy Land footholds. The player begins under immediate pressure from several wars, fragile supply, divided military orders, contested religious legitimacy, and territory that cannot be held through island industry alone.

The campaign is built around five connected questions:

1. Can a tiny fortified island maintain a dispersed war across several seas?
2. Which military order controls the crusade, and what price does that order demand?
3. Will conquered territory become commanderies, principalities, restored local states, or Papal administrations?
4. Does victory produce a durable Malta-led crusader network, the Holy See, or the Kingdom of God?
5. At extreme Chaos, does the campaign become a hidden ideological alliance, a German betrayal, or a Papal terminal war?

The design must produce early military action, medium-term governance and logistics, route-specific politics, several viable forms of territorial rule, and a credible failure comeback. The player cannot be forced to follow the Papal route merely because the event theme is religious.

## Lifecycle

### Selection and preparation

Event 38 enters normal selection as a Fire-Once event once the implementation is complete and the event is enabled. Before the event fires, the evolution system can already have unlocked Evolution I, II, or III. The opening release transaction reads the highest enabled pre-fire evolution and builds the matching cumulative setup.

### Opening transaction

The opening performs one bounded release transaction:

- resolve the Malta actor
- resolve the highest pre-fire package
- freeze and validate selected state targets
- transfer the approved opening states
- build capital, supply, ports, and country history
- create templates and units
- grant equipment, fuel, trains, convoys, and manpower through dynamic setup formulas
- create immediate wars against displaced owners
- initialize the three public mechanic values
- initialize focus, decision, AI, and event-log state
- issue regional reaction events
- clear every temporary request, selection, and bypass marker

The transaction must fail closed. Partial release, partial state transfer, missing capital, missing focus tree, empty armies, and orphan wars are unacceptable.

### Baseline campaign

The baseline campaign contains ordinary stages that are not evolutions:

1. Hold Malta and the maritime bridge.
2. Secure Jerusalem and the Jordan corridor.
3. Stabilize supply through ports, depots, rail, convoys, and local administration.
4. Decide how military orders share power.
5. Establish a territorial governance model.
6. Advance toward a Malta-led crusader realm, the Holy See, or a restored local Christian order.
7. Recover through the Eleventh Crusade route if the expedition collapses.

Only the initial event firing creates the normal random-event History entry. Internal campaign events do not create extra pacing events.

### Evolution campaign

The three evolutions are separate logged mutation tracks:

- Evolution I, The Orders Return, at 200 or more Chaos
- Evolution II, The Crusader Principalities, at 400 or more Chaos
- Evolution III, The Age of Holy War, at 600 or more Chaos

After Event 38 has fired, evolution activation uses dynamic pacing. A nominal 90-day MTTH is the central starting point, modified by war progress, authority, legitimacy, foreign religious support, principalities, and current Chaos. If an evolution is already active before Event 38 fires, its setup effect is applied during release without a later delay.

Evolution activation never changes Chaos by itself.

### Normal country outcomes

These outcomes are public and belong to the focus campaign:

- Malta Crusader State
- Confederation of Military Orders
- Crusader Kingdom of Malta
- The Holy See
- Kingdom of God
- one or more Crusader Principalities
- local Christian restorations or Papal administrations

They are not terminal states unless the Holy World route later activates.

### Hidden outcomes

The Teutonic Order faction and Atlantis betrayal are hidden. Their existence is never previewed in public Event Details, event catalog prose, normal focus descriptions, or public scenario controls. Hints may appear only after the relevant campaign facts exist.

### Terminal outcome

The Holy World is the only public Event 38 world-end branch. The preparation route requires Papal supremacy, 800 or more Chaos, and approved territorial proof. Terminal activation requires 1000 or more Chaos, final readiness, no existing terminal state, and an enabled branch toggle.

The terminal route sets the shared world-end state, freezes normal automatic event firing, fires its own super-event, creates the believer coalition, and stages regional wars through a bounded queue.

### Manual scenario

The Believers vs Nonbelievers scenario bypasses the source event and progression requirements. It creates or selects a valid Papal crusader actor, raises Chaos into World Collapse during setup, divides the world, and calls the same terminal runtime. The bypass exists only during setup and is cleared before the first ordinary terminal pulse.

## Player-facing mechanic budget

Event 38 exposes three persistent custom values:

- **Crusade Authority** measures central command, recognized control, and the ability to govern the expedition.
- **Order Cohesion** measures cooperation among the military orders and the risk of command rupture.
- **Sacred Legitimacy** measures religious recognition, relic prestige, Papal support, and public belief.

The event can track many internal facts, but no fourth persistent public value is approved. Supply is shown through normal HOI4 systems and concise status text. Resistance, relic authenticity, foreign support, local Christian cooperation, Papal relations, order demands, and principality loyalty remain hidden components or qualitative statuses.

## Design boundaries

### Malta remains human

Malta and its normal derivatives use ordinary population, famine, migration, politics, laws, civilian economy, and casualty systems. They are not `is_actual_nonhuman_country`. The phrase “special Chaos country” in older cross-event notes must be interpreted as event-special routing, not as automatic placement in the shared exclusion classifier.

### Religion is political and uncertain

The event can contain zeal, ritual, relics, claims of miracles, blessed formations, and supernatural rumours. It does not prove relic authenticity, divine intervention, racial mythology, or Atlantean ancestry as objective truth.

### No instant universal cores

Ordinary crusader conquest uses claims, occupation, subjects, commanderies, compliance, and staged integration. The Atlantis route's requested “cores” require special treatment because true engine cores would erase much of the resistance and atrocity gameplay. The approved solution is an **Atlantean Core Program** registry described in the Atlantis specification. It grants ideological claim status and route bonuses immediately, then grants actual engine cores only through controlled integration or an explicitly approved terminal exception.

### No whole-world periodic scan

Global assignment, terminal wars, diplomacy, and atrocity processing use registered country and state arrays, sparse active ledgers, staged pulses, and owner-local callbacks. No new all-country daily, weekly, or monthly iteration is approved.

### No free army loop

Starting units are a one-time release package. Later formations require equipment, manpower, order capacity, workshops, sponsors, captured industry, decisions, or focus unlocks. Every unit family needs sustainment and replacement limits.

## Success, failure, and closure

### Campaign success

A successful normal campaign has all of these qualities:

- Malta remains supplied and militarily viable
- Jerusalem or another route-specific sacred center is held
- the order settlement is stable enough to support long-term play
- conquered regions have a coherent governance model
- the focus tree opens a durable political identity
- the army has an equipment and reinforcement pathway
- the player has a credible late-game ambition without being forced into a terminal route

### Campaign failure

Failure is playable. Losing most expeditionary territory or Jerusalem opens the Eleventh Crusade recovery route. Malta can rebuild transport, appeal for foreign volunteers, restore its knight cadres, secure a new landing site, negotiate a local settlement, or retreat into a fortified island realm.

Total defeat remains possible if Malta loses its core island, its government, and every approved successor host. Cleanup must remove event-owned ledgers, temporary decisions, targets, stale faction facts, and inactive provider records.

### Stop condition for design expansion

This pack defines the required depth. Additional broad routes should not be added during implementation unless an accepted improvement addendum proves a distinct gameplay need. Final implementation can add bounded flavour events, names, and small route-specific content, but it should not add another public mechanic value, another terminal route, or another large country family without updating the source specification.
