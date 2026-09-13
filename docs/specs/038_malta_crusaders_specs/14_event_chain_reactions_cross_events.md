# Event chains, reactions, and cross-event integration

## Event-chain structure

The implementation should keep Event 38 inside the `chaosx.nr38.*` namespace. Exact subevent numbers are assigned after inspecting current namespace use.

Suggested event families:

| Family | Purpose |
| --- | --- |
| Entry and release | Event selection, setup, camera, player introduction, world news |
| Malta opening | government, first council, strategic priorities, immediate wars |
| Order demands | land, wealth, command, headquarters, relics, and arbitration |
| Campaign reports | victories, defeats, supply crises, and regional settlements |
| Local governance | collaboration, resistance, church disputes, and administration |
| Principalities | creation, charters, obligations, succession, and defection |
| Relics | searches, custody, examination, fraud, theft, and recognition |
| Papal route | invitation, Rome, Holy See, Kingdom of God, and terminal preparation |
| Eleventh Crusade | defeat, evacuation, rebuilding, invasion, and final settlement |
| Evolution incidents | one activation event per evolution and evolved follow-ups |
| Hidden Teutonic | hints, negotiations, faction formation, and Final Crusade |
| Atlantis | eligibility choice, betrayal, war, policy, and defeat |
| Holy World | preparation, side choices, activation, regional pulses, victory, and defeat |
| Manual scenario | confirmation handoff, setup reports, and side choices |
| Cleanup | annexation, invalid actor, target death, faction dissolution, and stale state |

The initial event firing produces one normal History entry. Follow-up events do not apply additional random-event pacing.

## Entry presentation

### Camera and map

After a successful release transaction, the player's camera should move to Malta or the Holy Land command according to player context. A human Malta player should see Malta first. Other players can see the larger Holy Land crisis.

### Popup direction

The entry popup should explain:

- Malta has become a crusader state
- several fortified commands and occupied footholds already exist
- wars have begun
- revived orders and foreign volunteers are present
- the new government intends to hold Jerusalem and the Mediterranean sea road

The text should describe people, banners, ships, forts, and armed formations. It should not read as an administrative change log or a list of states.

### Options

The main reaction option acknowledges the crisis. It can vary for Malta, displaced owners, nearby governments, Catholic governments, and ordinary observers.

Final wording should use serious or dry political irony according to actor and stakes. It should not use cheap comedy about war or religion.

## Malta opening events

### The Provisional Council

The Malta player chooses the immediate government posture:

- central emergency command
- balanced council
- civilian constraints

This is an early direction, not a permanent full route lock.

### The Four Anchors

The event identifies Malta, Jerusalem, the maritime bridge, and the primary supply port. It opens the first missions.

### The First Order Demand

One valid order makes a concrete request based on the opening package. The demand cannot fire before the player can inspect the mechanic.

### The War at Sea

A naval and convoy report explains the supply problem and opens escort actions.

## Displaced-owner events

Each displaced owner receives one bounded response event. Options depend on strength, existing war, faction, ideology, and current territory.

Possible responses:

- immediate counterattack
- demand international support
- accept a limited armistice
- back local resistance
- request a great-power guarantee
- negotiate evacuation or prisoner exchange
- exploit Malta's supply weakness

The event should not offer identical choices to every country.

## Regional reactions

Priority recipients:

- direct neighbours
- eastern Mediterranean powers
- countries with territory in the opening package
- Catholic governments likely to support Malta
- Orthodox governments affected by church claims
- Muslim-majority governments affected by the crusade
- colonial powers with ports and mandates in the region
- major naval powers

Possible reaction families:

- volunteers and donations
- condemnation
- naval patrols
- guarantees
- regional defence conference
- local Christian appeals
- resistance sponsorship
- Papal mediation
- port closure
- secret negotiation with an order

Reaction events are prioritized and bounded. Do not notify every country about every local incident.

## Government and ideology reactions

### Catholic-aligned governments

Can support, recognize, limit, or condemn Malta based on Papal relations, ideology, fear, and current war.

### Secular democratic governments

Likely focus on sovereignty, occupation, refugee protection, and regional stability.

### Fascist governments

Can see Malta as ally, rival, propaganda asset, or territorial threat. Nazi Germany's hidden route requires specific flags and cannot begin from generic fascist sympathy.

### Communist governments

Likely oppose clerical rule and support local resistance, secular allies, or anti-colonial movements. They can still make tactical agreements against a common enemy.

### Orthodox governments

React strongly to church jurisdiction, Greek territory, and local Orthodox communities. They can negotiate church autonomy, resist Papal administration, or support a local Christian restoration.

### Muslim-majority governments

React to territorial seizure, religious policy, sacred-site access, refugee movement, and regional security. Their behavior should differ by government, war state, and local stake.

The final text must avoid treating whole religions or populations as one actor.

## Event 3: The Holy Realm

The Holy Realm is the critical hidden-route partner.

Event 38 can read owner-published facts for:

- Holy Realm existence
- valid government route
- German contact
- positive or hostile relationship
- transformed leadership state
- faction compatibility

Event 38 must not duplicate Holy Realm values, character ownership, or terminal logic.

The Teutonic Order route uses the exact flags specified in the source brief. The Holy Realm retains ownership of what those flags mean inside its system.

## Event 6: Independence Wave

A country released through Independence Wave can become:

- a local restoration target
- a principality alternative
- a regional opponent
- a Papal administration candidate
- a believer or nonbeliever later

Event 38 must reuse protected carriers and origin facts. It cannot create a duplicate of an active Event 6 country.

When a selected state belongs to a newly released actor, the opening and settlement logic treats that actor as the displaced owner and preserves its release origin.

## Event 11: Secret Alliance

Event 38 should inspect existing secret and revealed alliance structures before creating new blocs.

Possible interactions:

- a secret alliance supports Malta
- a hidden coalition backs regional resistance
- Malta exposes an alliance through relic or order diplomacy
- Holy World preparation absorbs an aligned revealed coalition

Do not create overlapping factions when an existing alliance can be extended safely.

## Event 13: Natural Disasters

Disasters can damage ports, forts, rail, populations, and supply in Event 38 regions. Malta can call the stable natural-disaster gateway only when an Event 38 decision deliberately requests a disaster consequence.

Ordinary disaster effects remain Event 13-owned. Hospitaller and engineer decisions can respond through documented adapters.

## Event 14: Cannibalism and humanitarian systems

There is no default thematic alliance. Event 38 can interact through shared famine, migration, Deaths, atrocity, and special-country routing.

Malta and ordinary principalities use normal civilian systems. Cannibal or actual nonhuman actors are excluded from ordinary local-government and believer assignment where the shared classifier says so.

## Event 16: Brilliant Scientist

Event 38 can receive:

- compatible military or engineering technology
- scientist advisers
- special project support
- alien or advanced equipment interactions where the owner APIs permit it

Custom technology grants use the owner API and compatibility checks. Event 38 does not copy Brilliant Scientist's project system.

The hidden Atlantis or Papal terminal routes can create special requests, but no cross-event grant should bypass its source conditions.

## Event 19: Infantry Spawn and unit registry

Every Event 38 standalone unit family registers through the owner-side unit-family contract expected by the shared consumer. Event 19 does not maintain an Event 38-specific switch.

Spawn requests must preserve:

- provider eligibility
- equipment tokens
- template roles
- sustainment
- presentation
- cleanup

Malformed or missing provider data blocks the request. Generic infantry is not an accepted fallback.

## Event 20: Black Plague

The Order of Saint Lazarus and Hospitaller routes can respond to plague regions through shared outbreak facts.

Possible interactions:

- contaminated-region relief
- hospital missions
- refugee screening
- order prestige from successful care
- condemnation or legitimacy loss from abuse
- defensive specialist units

Event 38 does not claim ownership of plague spread, Rat Nations, or terminal plague routes.

## Event 22: Camps and repression

Atlantis uses the shared camp and repression network. Malta can also enter this system if ordinary or Papal policy creates concentration, detention, extermination, experiment, or restricted chemical sites.

The event must not create a separate atrocity ledger.

Hospitaller or civilian routes can discover, reform, close, or expose sites according to the shared system.

## Event 33: Acid Rain

Acid rain can damage Event 38 supply networks and populations. Hospitaller, Saint Lazarus, engineer, shelter, and evacuation actions can respond through shared state and population contracts.

Event 38 does not duplicate Acid Rain contamination or deaths.

## Event 36: Chemical and Biological Weapons Convention

Event 38 governments and subjects can choose their treaty stance according to government and route.

Interactions:

- Malta can preserve restrictions, accept chemical warfare, accept first-use limits, reject, or prepare covertly
- a Papal government can treat unconventional weapons as a doctrinal and legitimacy question
- Saint Lazarus and Hospitaller actors can oppose or manage contaminated warfare
- siege ammunition and chemical or biological upgrades require the convention and relevant technology
- use creates shared Condemnation, contamination, Deaths, and treaty consequences

The Holy World terminal does not automatically receive free chemical or biological weapons.

## Event 40: Lawrence of Arabia

Malta is a direct rival in the eastern Mediterranean and Levant.

Relevant interactions:

- control of Jerusalem, Jordan, Levantine territory, Greek islands, or ports
- competition for local governments
- competing aid and military patronage
- British route access
- federation or client-state conflicts
- embargo and convoy pressure

Arabian governments can play Britain and Malta against each other, accept one patron, reject both, or form a counter-bloc.

Older Event 40 notes call Malta a “special Chaos country.” Implementation must interpret that as an event-special actor exclusion from Lawrence targeting, not as automatic placement in `is_special_chaos_country` or `is_actual_nonhuman_country`. Malta should have a narrow `lawrence_invalid_target_malta_crusader` trigger or equivalent owner-specific exclusion.

## Event 45: Third Balkan War

A Balkan war can block Aegean and Greek routes, create new displaced owners, or offer an intervention opportunity.

Event 38 should:

- avoid duplicate wars
- respect existing camps
- treat active fronts as a strategic risk
- allow naval support, local alliances, or opportunistic claims only through valid decisions

## Event 50: The Great Embargo

An embargo against Malta or a sponsor affects:

- convoy access
- resource imports
- foreign donations
- fuel
- workshop production
- principality contributions
- Papal diplomacy

An embargo can push Malta toward conquest, local substitution, Templar finance, or negotiated settlement.

## Event 52: Intel Leaked

Leaks can expose:

- hidden order negotiations
- foreign sponsors
- relic fraud
- principality plots
- Teutonic Order talks after their hint stage
- atrocity evidence
- Atlantis preparations after eligibility

Hidden routes remain protected before an actual leak proof exists.

## Event 56: The Navy

Naval abundance or special naval grants can support Malta's sea road. Event 38 uses source-owned grant effects and does not duplicate fleets.

## Event 126: Heroic Crusade

The supplied catalog marks Event 126 **Heroic Crusade** as unavailable and describes a religious faction formed to destroy rival religions. This overlaps Event 38's Holy World and foreign religious war space.

Accepted ownership rule:

- Event 38 owns Malta, the Holy See, Kingdom of God, believer politics, and The Holy World terminal.
- Event 126 must not independently duplicate Malta's world religious faction or terminal war.
- If Event 126 is later reworked, it should become a generic external reaction, rival crusade, counter-crusade, or non-Malta religious-war event with explicit conflict gates.
- Until then, it remains unavailable.

## General shared-system interactions

Event 38 must read and write through accepted APIs for:

- Chaos Meter
- Air Cleanliness
- Deaths
- Condemnation
- famine
- migration
- camps and repression
- event logs
- world threat
- unit-family providers
- custom technology grants
- natural disasters
- triggerable scenarios
- super-events

It should not create parallel copies of these ledgers.

## Event-log behavior

### History

One initial row for Event 38.

### Evolutions

One row for each of the three actual evolutions.

### Clusters

If Event 38 fires through Formables, the cluster row records Event 38 as a High member and the normal member result.

### Hidden routes

Teutonic Order and Atlantis do not create public evolution rows. They can create ordinary event history or super-event records according to current frameworks without exposing them in advance.

### Terminal route

The Holy World appears through its public Event Details world-end row and terminal super-event.

## Localisation direction

Final text should:

- describe concrete people, forts, ships, orders, local governments, and military actions
- distinguish religious institutions from whole populations
- keep relic and miracle authenticity uncertain
- call Nazi and Atlantean racial claims ideology or fabrication
- avoid developer history, debug labels, raw variables, and exact hidden formulas
- avoid generic map-summary framing
- avoid repeated official-denial contrast formulas
- use route-specific voices for Malta, orders, Pope, Germany, Holy Realm, principalities, displaced owners, and regional governments
