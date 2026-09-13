# Event 57 Implementation Prompt

Implement Chaos Redux Event 57, The Black Market, to the complete source specification under:

`docs/specs/057_the_black_market_specs/`

Read every file in that folder before editing. Also read the current repository versions of `AGENTS.md`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-improvement-loop`, `chaos-redux-subagents`, all required offline Paradox wiki pages, current vanilla documentation, and relevant Chaos Redux precedents.


Spawn every project subagent with a complete self-contained prompt and `fork_context=false`.

## Core event

Keep the canonical entry `chaosx.nr57.1`.

Register Event 57 as:

- Minor Fire-Once
- Chaos level `1`
- Positive Economy
- High member

The entry must create one connected invitation-only founding cell with two to four countries, targeting three. Favor the player only when eligible. Do not force invalid membership or create a route without endpoint proof.

Resolve founder acceptance before consuming the fire-once event when the event framework requires that ordering. If no valid accepted cell can form, leave the event unfired and clean every temporary record.

The global history row must not reveal founders, members, routes, inventory, or an actor flag.

## Persistent system

The random event fires once. Later invitations, routes, offers, deliveries, investigations, evolutions, dormancy, and reconstruction belong to the event-owned runtime.

Create sparse registries for members, routes, cells, offers, deliveries, evidence, providers, recent imports, and one-time receipts. Use bounded registered pulses and narrow change hooks. Do not add a whole-world recurring daily, weekly, or monthly scan.

Implement idempotent membership, route, offer, and transaction state machines. Save and reload must not reroll outcomes, duplicate equipment, repeat credit, repeat Chaos, or create duplicate missions.

## Public mechanic

Expose only:

- Market Credit
- Exposure
- Network Reach

Use the bands, thresholds, and stage meanings in the specs. Keep trust, capacity, reliability, route pressure, candidate scores, demand components, and provider proofs internal.

Implement government postures:

- Compartmentalized Tolerance
- State Patronage
- Counterintelligence Penetration
- Suppression Campaign

Posture changes require cooldowns and valid conditions. They cannot reset Exposure or grant another founding package.

## Routes

Implement land borders, neutral intermediaries, maritime shipping, occupied corridors, Event 55 international corridors, and evolved covert air routes.

Routes need stable IDs, endpoint proof, Open, Strained, Disrupted, Compromised, and Burned states, cargo capacity class, risk class, delivery-time band, pressure, investigations, and cleanup.

Route opening and repair must use real state, port, railway, convoy, fuel, airbase, intelligence, or unit-presence objectives. Do not reduce them to political power purchases.

## Inventory and trade

Implement the exact slot caps:

- baseline `3`
- Evolution I `4`
- Evolution II `5`
- Evolution III `6`

Every offer needs a source, eligible buyer, and route. Preserve an immutable offer receipt. War, ideology, faction membership, hostility, and embargoes are never automatic transaction bans when a valid underground path exists.

Member sales must calculate a dynamic readiness reserve, debit real stock before dispatch, and pay bounded Market Credit. Use the recent-import ledger to prevent immediate resale. Prevent self-purchase, duplicate source debit, repeated listing rewards, and offer rerolls through UI or reload.

Every purchase starts a delayed delivery mission. Support clean, delayed, partial, seized, canceled, and sting outcomes. A delayed job can create one bounded crisis step, then must resolve.

Implement Market Credit sources, caps, network fees, limited underwriting, withdrawal settlement, auction bids, and anti-arbitrage controls. It cannot become unlimited converted political power.

## Provider API

Implement the event-owned versioned provider contract in dedicated Event 57 effects, triggers, and documentation.

Require provider ID, package ID, offer class, minimum evolution, availability, buyer eligibility, source debit, delivery effect, amount, price, route, Exposure, reveal, completion isolation, DLC behavior, and cleanup.

Missing proof returns a reject reason and creates no offer.

Integrate approved adapters for Events 50, 54, 55, and 56, captured or collapsed stock, intelligence, normal technology, naval assets, CBRN equipment, and special projects only where their owners publish valid packages.

Receiving goods must not grant technology. Receiving a technical or experimental package must not complete the source event or project unless its owner explicitly defines that exact result.

## Decisions and missions

Use one hidden member category with evolution-dependent static art. Show three to five primary actions, never more than six, and one to three active missions.

Use a selected-offer flow when needed. AI evaluates all valid offers directly.

Implement member purchase, sale, commission, route, posture, underwriting, Exposure, intelligence, delivery, auction, dormancy, suspension, withdrawal, expulsion, and reconnection actions.

Implement a separate temporary evidence-gated outsider category for investigation, seizure, intermediary pressure, broker turning, local cell dismantling, and member suppression.

Every cost needs the correct texticon and no action may use more than four spendable cost types.

## Evolutions

Implement:

1. International Network at `200+` Chaos, Reach `35+`, world proof, and paced MTTH
2. The Underground Economy at `400+` Chaos, Reach `65+`, world proof, and paced MTTH
3. Anything Has a Price at `600+` Chaos, Reach `85+`, world proof, and paced MTTH

Use the member, region, route, delivery, and alternate readiness packages in the source specs.

Evolution activation gives zero Chaos. Disabled evolutions must not set recorded flags or unlock their content. Baseline trading must continue safely.

## Chaos

Implement the complete guarded Event 57 map:

- first completed interregional delivery
- first completed trade between active enemies
- first major embargo-circumvention delivery
- first approved experimental delivery
- first exceptional stockpile delivery
- first route-backed connection across four regions
- mature regional cell dismantling
- verified network dormancy after Evolution I or later
- full network dismantling

Use one-time or episode receipts and the source values from the spec as tuning anchors. Do not duplicate wars, annexations, deaths, contamination, nuclear use, condemnation, world tension, or other shared sources.

## AI and probability

Implement strategic AI for invitation, posture, purchase, sale, route, Exposure response, penetration, suppression, outsider investigations, and auctions.

Before any weighted patch, run `chaosx_ai_probability_auditor` with `hoi4.probability_inspect` and BM-P01 through BM-P10. The owner applies the patch. The auditor then runs `hoi4.probability_compare` with the same scenarios.

Hard-invalid options must be zero before weighting.

## Event logs and text

Wire event name, debug name, history, actor handling, Event Details, and three evolution records across all required shared surfaces.

Write final localisation from the spec's period clandestine-logistics direction. Do not paste working labels as final text. Preserve country-local knowledge and avoid modern digital-market terms, raw variables, debug phrasing, and implementation history.

## Assets and achievements

Create and wire the complete asset package from the asset prompt:

- three report pictures
- category icon
- Market Credit texticon
- four evolution-dependent category pictures
- twelve decision icons
- seven achievement triplets

Implement all seven achievements from the achievement prompt with exact receipt-based tracking and disqualifiers.

Use generated event art and icon subagents according to the current asset workflow. No placeholder or resized unrelated asset counts as complete.

## DLC support

Implement the no-DLC core and the relevant La Résistance, Arms Against Tyranny, No Step Back, By Blood Alone, Man the Guns, and owner special-project enhancements described in the acceptance spec.

DLC absence must never block the core event lifecycle.

## Catalog and documentation

Replace the stale Event 57 Radar identity in the authoritative XLSX after implementation facts are final. Add Positive Economy High membership and all three evolution summaries. Run `python .tools/export_event_catalog_csv.py`. Never edit the CSV exports directly.

Write permanent Event 57 overview, membership, route, inventory, provider, AI, balance, and validation documentation.

## Required audits

Use the event MCP inspect, render, and compare workflow for the final event chain.

Run:

- scripted-system architecture review
- probability baseline and comparison
- decision and mission audit
- localisation audit
- asset coverage review
- documentation curation
- workbook alignment
- improvement-loop pass
- read-only event completion audit

Resolve every accepted addendum. Do not claim completion while a required system, provider, decision, AI path, text key, asset, achievement, log, doc, workbook field, or validation gate is missing.

Report every blocker or simplification. Do not use an unapproved fallback.
