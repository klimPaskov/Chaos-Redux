# Implementation Acceptance and Validation

## Implementation goal

Implement Event 57 as a complete fire-once bootstrap plus persistent event-owned Black Market system.

The completed feature must preserve:

- invitation-only membership
- compartmentalized country knowledge
- a connected founding cell
- sparse member, route, offer, delivery, evidence, and provider registries
- real source debits
- Market Credit
- Exposure
- Network Reach
- route-backed delayed deliveries
- rotating inventory
- government postures
- outsider evidence and counterplay
- three paced evolutions
- Event 57 Chaos milestones and reversals
- Positive Economy High membership
- AI behavior
- DLC compatibility
- event logs and Event Details
- assets
- achievements
- permanent docs and workbook alignment

## Required source review before code

Implementation must follow the current repository versions of:

- `AGENTS.md`
- `chaos-redux-events`
- `chaos-redux-decisions-missions`
- `chaos-redux-event-assets`
- `chaos-redux-improvement-loop`
- `chaos-redux-subagents`
- the offline Paradox wiki pages required by the touched systems
- current vanilla documentation and precedents
- current Chaos Redux event, decision, scripted-effect, event-log, cluster, achievement, and catalog patterns

Any current repository rule that is stricter than this planning package remains binding.

## Likely implementation files

Final paths must follow the current repository convention after inspection.

### Event-owned gameplay

- `events/057_the_black_market.txt`
- `common/decisions/057_the_black_market_decisions.txt`
- `common/decisions/categories/057_the_black_market_categories.txt`
- `common/scripted_effects/057_the_black_market_effects.txt`
- `common/scripted_effects/057_the_black_market_provider_effects.txt`
- `common/scripted_triggers/057_the_black_market_triggers.txt`
- `common/scripted_triggers/057_the_black_market_provider_triggers.txt`
- `common/script_constants/057_the_black_market_constants.txt`
- `common/on_actions/057_the_black_market_on_actions.txt` for narrow event-owned change hooks only
- `common/ideas/057_the_black_market_ideas.txt` for modifier-free carriers or visible posture ideas only when the final UI needs them
- `common/ai_strategy/057_the_black_market_ai_strategy.txt` when persistent strategy support is useful
- `common/scripted_localisation/057_the_black_market_scripted_localisation.txt`

### Shared event integration

- event-category registration
- Chaos-level registration
- reworked-event default allowlist
- event-name selectors
- event history and Event Details
- evolution log selectors
- Positive Economy cluster definitions and member arrays
- event manual-fire validation
- Chaos history source selectors

### Localisation

- Event 57 event and decision localisation
- shared event-name localisation
- Event Details and evolution localisation
- scripted localisation
- achievement localisation
- texticon localisation when required

### Assets

- `gfx/event_pictures/057_the_black_market/`
- event-owned decision and category asset folders
- root achievement assets
- event-owned `.gfx` registration
- Market Credit texticon registration

### Documentation

- `docs/events/057_the_black_market/`
- `docs/specs/057_the_black_market_specs/`
- `docs/plans/057_the_black_market_plans/`
- authoritative event catalog workbook
- regenerated CSV exports

## Script architecture

### Owner-owned helpers

Event 57 should own:

- founder selection
- membership state changes
- route creation and refresh
- offer generation
- Market Credit transactions
- Exposure changes
- Network Reach changes
- transaction receipts
- recent-import locks
- invitation cadence
- evolution readiness
- provider request and receipt handling
- outsider evidence
- dormancy and dismantling

### Shared helpers

Reuse the shared dynamic effects when their contracts fit.

Examples include supported stockpile debit helpers for infantry equipment, support equipment, motorized equipment, convoys, trains, plague bombs, and fuel.

When a needed neutral debit or transaction helper has callers across several systems, add it to the shared dynamic registry and document its purpose, scope, inputs, outputs, defaults, side effects, and usage.

One-event orchestration remains in Event 57 files.

### Tuning

Centralize:

- founder counts
- offer-slot caps
- rotation intervals
- invitation intervals
- Exposure bands and changes
- Reach thresholds and changes
- route limits
- transaction time bands
- credit floors and caps
- seller reserve factors
- price factors
- recent-import lock duration
- auction cadence
- evolution MTTH factors
- AI weights
- Chaos milestone values

Use script constants where the engine field accepts them. Use documented local constants or variables where it does not.

## No whole-world recurring scan

The system must use:

- member arrays
- route arrays
- active offer arrays
- active delivery arrays
- evidence-case arrays
- provider registry
- dirty records
- bounded candidate sampling

Do not add a whole-world `on_daily`, `on_weekly`, `on_monthly`, or equivalent scan.

A bounded event-owned pulse can iterate only the registered records.

## Transaction state machine

Every offer and delivery must pass through an explicit state machine.

Minimum states:

- generated
- available
- reserved
- source debit pending
- dispatched
- delayed
- partially settled
- settled
- seized
- canceled
- invalidated

Each state transition must be idempotent.

A save and reload at any state must not:

- duplicate equipment
- duplicate Market Credit
- reroll the outcome
- lose the debit
- restore an expired offer
- create a second mission
- clear the buyer or seller incorrectly

## Membership state machine

Minimum states:

- candidate
- invited
- active
- dormant
- suspended
- former
- expelled
- dismantler

Every transition must clean obsolete category content and keep one stable country receipt.

## Provider API acceptance

The provider API must:

- be event-owned and documented
- be versioned
- fail closed
- require explicit owner registration
- validate source and buyer
- debit the source once
- deliver once
- preserve owner event completion state
- return reject reasons
- expire safely
- survive save and reload
- prevent duplicate sale of one package
- support no-DLC paths

Event 54, Event 55, Event 56, Event 50, captured-stock systems, and future equipment owners should use adapters and avoid direct ledger access.

## Event and probability MCP evidence

### Event chain

Use:

- `hoi4.event_inspect`
- `hoi4.event_render`
- `hoi4.event_compare`

Inspect entry ordering, invitation branches, transaction scope, evolution flow, outsider evidence, dormancy, and dismantling.

### Weighted logic

`chaosx_ai_probability_auditor` must inspect every weighted surface before patching and compare it after patching.

Use the named BM-P01 through BM-P10 scenarios from the AI specification.

Required surfaces include:

- founder and broker selection
- candidate invitations
- candidate responses
- posture choice
- offer generation
- source and package selection
- purchase choice
- sale size
- route selection
- delivery outcome
- investigation action
- auction bidding
- evolution MTTH

## Decision audit

After implementation, `chaosx_decision_mission_auditor` should inspect and patch only bounded issues.

The audit must cover:

- category lifecycle
- three-value clarity
- visible action cap
- active mission cap
- cost icons
- route requirements
- auto-completion
- success, partial success, and failure
- stale targets
- cleanup
- AI validity
- exploit risk
- impact of rewards and penalties

A broad design gap returns to the parent or improvement planner.

## Localisation audit

`chaosx_localisation_auditor` should review:

- missing and duplicate keys
- encoding
- raw keys
- dynamic offer text
- route and risk text
- blocked reasons
- category clarity
- history and Event Details alignment
- evolution text
- achievement text
- workbook-facing wording
- absence of implementation-history language
- absence of modern digital-market language

## Asset acceptance pass

The asset workers should create the exact package in the asset specification.

The parent must verify:

- source evidence
- reference inspection
- dimensions
- transparency
- independent icon types
- category-picture switching
- event-picture consumers
- Market Credit texticon
- achievement triplets
- runtime paths
- sprite names
- final in-game consumers
- deletion of the temporary event asset workspace after durable evidence is promoted

## DLC matrix

### No DLC

Core requirements:

- founding network
- membership
- Market Credit
- Exposure
- Network Reach
- routes
- rotating offers
- stockpile sales and purchases
- fuel and convoy trade
- base intelligence packages
- counter-smuggling
- three evolutions
- AI
- achievements

### La Résistance

Enhancements:

- agency-backed invitations
- intelligence packages
- penetration
- evidence maturity
- route operations

No core action depends on the DLC.

### Arms Against Tyranny

Enhancements:

- verified legal-market valuation or equipment compatibility where useful
- stronger contrast between legal and illicit access
- supported equipment-market integrations

Black Market membership and offers remain separate from the legal market.

### No Step Back

Enhancements:

- trains and railway objectives
- tank designer compatibility
- route logistics depth

Base-game alternatives preserve transport and armored-package play.

### By Blood Alone

Enhancements:

- aircraft designer compatibility
- shared embargo consequences where present

Base-game aircraft tokens and Event 50's no-DLC embargo path remain valid.

### Man the Guns

Enhancements:

- naval design and ship-package depth where Event 56 supports it

No unsupported ship transfer is invented.

### Special-project DLC surfaces

Special-project equipment appears only through owner adapters. Core Event 57 progression does not require one.

## Acceptance scenarios

### BM-A01: Founding three-country cell

Setup:

- three eligible ordinary countries
- one broker
- two valid routes
- player selected as one founder

Pass conditions:

- one Event 57 firing
- private invitation
- no founder list in global history
- three accepted members or valid bounded replacement
- one-time founding credit
- active category
- first rotation scheduled

### BM-A02: Player excluded from founding

Pass conditions:

- AI network commits
- player receives no member category
- global history remains sanitized
- player can later receive valid invitation or evidence

### BM-A03: No valid cell

Pass conditions:

- event is N/A or rejects before fire-once commit
- no partial registry
- no consumed event weight
- no stale invitations

### BM-A04: Real surplus sale

Pass conditions:

- displayed protected reserve is correct
- source debit occurs once
- seller receives bounded credit
- offer appears once
- recent-import lock prevents resale farming

### BM-A05: Clean land delivery

Pass conditions:

- Market Credit spent once
- delivery mission appears
- source already debited
- cargo arrives once
- receipt settles
- Exposure and Reach change once

### BM-A06: Maritime seizure

Pass conditions:

- no buyer cargo grant
- observer receives bounded evidence
- route becomes Compromised or Burned
- source remains debited
- no duplicate cargo
- member Exposure rises

### BM-A07: Event 50 embargo connection

Pass conditions:

- demand and invitation scores change
- legal restriction remains active
- successful meaningful delivery records the one-time embargo-circumvention Chaos milestone
- no duplicate embargo Chaos

### BM-A08: Event 55 route adapter

Pass conditions:

- corridor receipt improves or creates one route
- Event 55 project state remains owner-controlled
- route invalidates correctly when corridor proof disappears

### BM-A09: Event 56 naval package

Pass conditions:

- only owner-approved package appears
- unsupported ship transfer remains unavailable
- source debit and buyer delivery are exact

### BM-A10: Experimental provider

Pass conditions:

- unapproved package has zero eligibility
- approved package appears only at allowed evolution
- delivery does not complete source project
- possession or use consequences call the owner

### BM-A11: Evolution I

Pass conditions:

- Chaos, Reach, members, regions, routes, enabled state, and MTTH all pass
- evolution log appears once
- no direct Chaos from activation
- four slots and new conventional classes unlock

### BM-A12: Evolution II disabled

Pass conditions:

- baseline and Evolution I trading continue
- no provider classes or flags from Evolution II activate
- no false evolution record

### BM-A13: Evolution III Grand Auction

Pass conditions:

- valid exceptional source
- eligible bidder pool
- unusable AI bidders abstain
- one winner
- one settled bid and delivery
- losing refunds exact
- no member list exposed

### BM-A14: Penetration and regional dismantling

Pass conditions:

- intelligence-capable member enters penetration
- cover trades maintain state
- evidence grows through actions
- one regional cell can be dismantled
- other disconnected cells survive
- regional negative Chaos receipt is one-time

### BM-A15: Full dismantling

Pass conditions:

- no active members, routes, or deliveries
- clearinghouse proof exists
- Reach below threshold
- reconstruction disabled
- final negative Chaos source once
- history preserved

### BM-A16: Civil war

Pass conditions:

- membership and credit do not copy to both sides
- route control decides inheritance or fracture
- active transaction settles safely

### BM-A17: Annexation during delivery

Run before and after dispatch.

Pass conditions:

- before dispatch cancels cleanly
- after dispatch uses successor, seizure, or cancellation rule
- no duplicate equipment or credit

### BM-A18: Save and reload

Save at:

- invitation pending
- offer available
- purchase reserved
- source debited
- delivery delayed
- auction open
- network dormant

Every state must resume without reroll, duplication, or stale UI.

### BM-A19: Multiplayer

Pass conditions:

- each player sees only its own membership and knowledge
- shared Network Reach remains synchronized
- one player cannot reveal another member without evidence
- offer reservation resolves deterministically
- auction winner is unique

### BM-A20: Performance

Pass conditions:

- no broad recurring country scan
- registered arrays remain bounded
- invalid records clean up
- long AI-only operation does not create event or decision spam

## Completion audits

Before completion claim:

1. probability baseline and comparison pass
2. decision and mission audit
3. localisation audit
4. asset coverage audit
5. documentation curation
6. authoritative workbook update and CSV export
7. improvement-loop pass
8. read-only event completion audit
9. parent review and concrete completion report

## Completion report contents

The final implementation report should list:

- files changed
- event and persistent-system identifiers
- member, route, offer, transaction, provider, and evidence architecture
- public values and thresholds
- decisions and missions
- AI scenarios and probability evidence
- Chaos sources and reversals
- cluster integration
- event connections
- DLC paths
- assets and consumers
- achievements
- docs and workbook updates
- task-specific validation findings
- blockers or simplifications

Do not claim completion while any accepted provider, route, decision, AI, localisation, asset, achievement, log, doc, or workbook surface is missing.
