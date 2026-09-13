# Event Chain, Logs, Localisation, and Catalog Alignment

## Event namespace

The event chain uses the `chaosx.nr57.*` namespace.

The exact final subevent numbering belongs to implementation, but the following role bands should be preserved so later maintenance remains readable.

| Working range | Role |
| --- | --- |
| `chaosx.nr57.1-9` | entry, founder selection, invitations, and initial member reports |
| `chaosx.nr57.10-19` | offer rotations, purchases, dispatch, and delivery outcomes |
| `chaosx.nr57.20-29` | invitations, reconnections, suspensions, withdrawals, and expulsions |
| `chaosx.nr57.30-39` | evolutions and major network milestones |
| `chaosx.nr57.40-49` | Grand Auctions and exceptional packages |
| `chaosx.nr57.50-59` | outsider discovery, investigations, seizures, and regional dismantling |
| `chaosx.nr57.60-69` | dormancy, reconstruction, and full dismantling |
| `chaosx.nr57.70+` | owner-adapter reports and rare validated outcomes |

These are implementation role labels, not player-facing event names.

## Entry transaction

`chaosx.nr57.1` should be a hidden or minimally visible bootstrap event that owns the founding transaction.

It should:

1. validate that the event can still fire
2. clear temporary selection state
3. build a candidate broker shortlist
4. select a connected founding cell
5. create pending invitations and route proposals
6. resolve AI responses
7. send the player a private invitation only when the player is selected
8. commit the network only after minimum membership and route proof exist
9. register the event in the fire-once system
10. record the sanitized event history row

The implementation must use a transactional order that does not consume the fire-once event if every proposed founder rejects and no valid replacement cell exists.

If the current event framework cannot roll back after `handle_fired_event`, founder acceptance must be resolved before the shared fire-once commit. This ordering requires source inspection and an MCP event-chain pass.

## Founder invitation reports

A player-selected founder receives a private report that explains:

- a controlled contact has arrived
- the offer concerns restricted goods and routes
- the government will know only its direct contact
- accepting creates access, credit, and Exposure
- rejecting closes the invitation for a long period
- an intelligence-capable government may enter under penetration

The report should not reveal the other founders, a global headquarters, or an omniscient organization.

AI founder responses use the same valid options and consequences.

## First member report

After the network commits, every accepted member receives a local setup event or hidden effect that:

- initializes one-time Market Credit
- assigns the accepted posture
- activates the first route
- adds the member to the sparse registry
- opens the category
- schedules the first offer rotation
- records the founding receipt

Only the current player needs a visible report. AI countries can receive hidden equivalent effects unless their response creates a world-visible consequence.

## Offer and delivery events

Offer rotation should be a hidden global event-owned process over registered providers and active members.

Player-facing reports are reserved for:

- a commissioned supplier being found or failing
- a delayed delivery that requires a choice
- a partial delivery
- a seizure
- a betrayal or sting
- an exceptional package
- a Grand Auction

Clean ordinary delivery should normally resolve through the mission and a concise notification. A full popup is unnecessary for every routine shipment.

## Membership events

Visible events are appropriate for:

- receiving an invitation
- suspension after a breach
- expulsion
- a government posture crisis
- reconnection after long dormancy
- a successful suppression campaign

Routine AI membership growth can resolve through hidden events and effects.

## Evolution events

Each evolution uses a global milestone event with no country actor.

The event should:

- verify Chaos and world-state readiness
- verify the evolution is enabled
- set the shared evolution context
- record the evolution entry
- activate the capability set
- update category presentation
- schedule the next relevant pulse

It should not award Chaos merely for activation.

## Outsider events

An outsider receives a local report only after evidence is created.

Useful incident subjects include:

- a customs seizure
- a train manifest that does not match its cargo
- weapons with altered markings
- a broker arrested at a border
- a neutral port authority exposed
- a courier carrying several currencies and route notes

The report names only the proven route, cargo, intermediary, or participant.

## Event history

Event 57 appears once in the main History tab.

The row should show:

- event ID and final event name
- Minor Fire-Once type
- firing date
- no actor flag
- no founder or member identity

The detail view explains the premise of a hidden invitation-only network. It should not list exact effects, hidden values, active members, routes, or future provider classes.

The event row remains available after the network is dormant or dismantled because the event fired historically.

## Evolution log

The Evolutions tab records exactly three Event 57 milestones.

Suggested data model:

- event ID: `57`
- type: one stable network-evolution type
- stage: `1`, `2`, and `3`
- tier: corresponding Chaos tier display
- actor: none

The main Evolutions tab and History-related evolution list use actual logged date and sequence metadata.

The Event Details evolution catalog shows premise and stage description only. It must not show fake history dates or sequence numbers.

## Event Details

Event Details should include:

- accepted name
- event type
- Chaos level `1`
- Positive Economy cluster and High member role
- premise description
- three evolution previews
- current enabled state
- fire-once status

The premise should explain that a small secret network moves restricted goods through covert routes and expands after its first appearance.

It must not show:

- active members
- route endpoints
- seller identities
- Market Credit balances
- current inventory
- exact evolution readiness values
- hidden investigation state

## Event enable state

The current catalog status is To Be Reworked. Event 57 should remain disabled by default in the reworked-event allowlist until the complete implementation, assets, AI, docs, workbook, and audits are ready.

When implementation is complete, the same change should:

- register Event 57 as fire-once
- register Chaos level `1`
- restore it to the default enabled allowlist
- add its Positive Economy membership
- add event-name and detail selectors
- add evolution selectors

## Localisation surfaces

Implementation needs finished player-facing text for:

- event name
- founder invitation
- acceptance, patronage, penetration, delay, and rejection options
- first member report
- decision category and status header
- Market Credit, Exposure, and Network Reach labels and tooltips
- reach stages
- government postures
- offer classes
- provenance classes
- route types and states
- risk classes
- purchase, sale, route, posture, cover, and suppression decisions
- delivery missions
- transaction outcome reports
- outsider evidence and counter-smuggling actions
- evolution titles and descriptions
- Event Details
- event history and evolution selectors
- achievements
- catalog-facing summaries

## Writing direction

### General voice

Use clear period logistics and political language.

The text should focus on:

- shortages
- neutral freight
- false paperwork
- state depots
- corrupt officials
- captured stock
- shipping routes
- intelligence contacts
- customs searches
- government risk

Avoid:

- digital-market language
- modern internet slang
- theatrical crime-boss language
- a single named mastermind
- generic office-report prose
- raw variable names
- direct explanations of script caps or tuning
- claims that every member knows the full network

### Founder invitation

The viewpoint is the receiving government. The contact provides enough evidence to prove access without revealing the network.

The serious acceptance route should sound pragmatic. State Patronage should sound opportunistic and controlled. Penetration should sound cold and security-minded. Rejection can be legalist, ideological, or cautious according to the government.

Final option wording must be researched only when it uses a cultural or historical allusion. Plain period wording needs no external quotation.

### Member category

Use short natural lines. Do not simulate a table with divider characters.

Each visible value needs:

- name
- current value or stage
- consequence
- next threshold
- one clear action that can change it

### Offers

An offer should state the cargo, amount, price, route, risk, and expected delivery time without revealing hidden source identity.

Use provenance descriptions such as diverted reserve, captured stock, neutral commercial lot, or unknown broker only when the source receipt supports them.

### Evolutions

Evolution text should show increasing reach through cargo and routes. It should not announce a generic level-up or list every mechanic.

### Outsider discovery

Use observed evidence. The text should not announce that the entire world has discovered the organization.

### Dismantling

Regional success should describe closed routes, seized accounts, and lost contacts. Full dismantling should describe the network's inability to settle or reconnect without claiming that illicit trade has disappeared from human society.

## Dynamic localisation

Dynamic text should support:

- selected offer class and amount
- Market Credit price
- route family
- delivery-time band
- risk class
- current Exposure band
- current Reach stage
- current posture
- named state, port, intermediary, buyer, seller when legitimately known
- blocked reason
- investigation target
- transaction result

The default branch must be neutral and safe. It cannot leak another country's text or an internal key.

## Key naming

Use stable lowercase snake_case with the Event 57 namespace where needed.

Working families include:

- `black_market_*`
- `chaosx_nr57_*`
- `events_log_event_57_*`
- `black_market_route_*`
- `black_market_offer_*`
- `black_market_achievement_*`

Final implementation should follow existing repository conventions after inspecting neighboring event files.

## Catalog conflict

The supplied current Events CSV maps ID `57` to an older event named The Radar and classifies it as Minor Repeatable.

The accepted Event 57 design in this package replaces that stale row with:

- The Black Market
- Minor Fire-Once
- Chaos level `1`
- Positive Economy
- High member
- To Be Reworked until implementation is complete

A supplied cluster-update source also identifies Event 57 as The Black Market in Positive Economy with High severity. That source confirms the accepted membership and should be reconciled with the authoritative workbook.

## Workbook alignment

The only editable catalog source is the authoritative workbook at:

`docs/spreadsheets/chaos_redux_events_catalog.xlsx`

After implementation facts are final, `chaosx_spreadsheet_doc_worker` should update:

- Event 57 name
- details
- type
- Chaos level
- cluster
- member severity
- three evolution summaries
- status
- Positive Economy member list and details when needed

Then run:

`python .tools/export_event_catalog_csv.py`

The three CSV exports must not be edited directly.

Spreadsheet text must match the in-game Event Details and evolution wording. It should describe the premise and progression, not raw effects or implementation history.

## Documentation surfaces

Recommended permanent documentation:

- `docs/events/057_the_black_market/overview.md`
- `docs/events/057_the_black_market/membership_and_secrecy.md`
- `docs/events/057_the_black_market/routes_and_deliveries.md`
- `docs/events/057_the_black_market/inventory_and_credit.md`
- `docs/events/057_the_black_market/provider_api.md`
- `docs/events/057_the_black_market/ai_and_balance.md`
- `docs/events/057_the_black_market/validation.md`

Accepted design remains under:

- `docs/specs/057_the_black_market_specs/`

Working plans and handoffs belong under:

- `docs/plans/057_the_black_market_plans/`

## Event chain MCP pass

Before editing and after final source changes, implementation must use the event MCP route to inspect and compare:

- `chaosx.nr57.1` entry flow
- founder transaction order
- invitation options
- transaction state flow
- evolution events
- outsider evidence events
- dormancy and dismantling

Use narrow `hoi4.event_inspect`, `hoi4.event_render`, and `hoi4.event_compare` calls.

Weighted options, invitations, offer pools, and AI actions require the separate probability workflow.
