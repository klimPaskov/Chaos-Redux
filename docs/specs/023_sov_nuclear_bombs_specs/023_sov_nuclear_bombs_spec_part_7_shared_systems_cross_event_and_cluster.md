# Event 023 specification, Part 7: Shared systems, cross-event links, cluster role, and logs

## Ownership boundary

Event 23 is an event-owned nuclear policy and command system. It should reuse the project's shared nuclear consequences and remain separate from other event identities.

Event 23 owns:

- The Soviet opening and exact event-owned arsenal grants.
- Custody doctrine.
- Arsenal Readiness and Command Integrity.
- Posture.
- Testing choices and site preparation.
- Public knowledge and credibility memory.
- Reactor and arsenal expansion decisions.
- Soviet target selection and demands.
- Authorization, reservation, hold, abort, and event-owned launch context.
- Soviet Collapse custody integration.
- The four Event 23 evolutions.
- The first multi-major exchange super-event trigger.
- Event 23 logs, details, docs, assets, AI, and achievements.

Shared systems own:

- Current vanilla nuclear delivery execution.
- Physical strike and test resolution.
- Population losses.
- Military deaths and disruption where supported.
- Building and infrastructure damage.
- Fallout and state contamination.
- Air Cleanliness changes.
- Condemnation, evidence, and sanctions.
- Direct nuclear-use Chaos changes.
- Death logging.
- Long-term radiation effects.
- Fallout world-end readiness and terminal state.

Other events retain ownership of their own concepts, even when they exchange hooks with Event 23.

## Shared nuclear action contract

Implementation should locate or create one reusable nuclear action adapter that can accept a complete validated request from Event 23 and other systems.

The exact helper name and fields must be designed by the scripted-system architect after repository inspection. The conceptual request includes:

- Action type: test, demonstration, combat strike, accident, demolition, or another verified profile.
- Actor country.
- Target country when relevant.
- Exact target state.
- Weapon class.
- Delivery route.
- Strategic profile.
- Reserved stockpile proof.
- Evidence and attribution policy.
- Test or strike severity.
- Any evacuation or protection state.
- Event source ID and context.
- One-shot contract proof.

The adapter should return:

- Accepted or rejected result.
- Stable rejection reason.
- Confirmation that the stockpile was committed.
- Confirmation of the exact state resolved.
- Shared consequence record ID or equivalent context.
- Any public knowledge result.
- Any terminal Fallout request result.

Validation fails closed. A missing target, unsupported delivery route, invalid state, missing bomb, or unsupported profile should reject the request without consuming the bomb or applying partial consequences.

## Normal nuclear use and thermonuclear use

Event 23 is about atomic weapons at baseline.

- The baseline grants normal nuclear bombs.
- Event 23 does not grant thermonuclear capability.
- If a separate verified system later gives the Soviet Union thermonuclear weapons, Event 23 may use the shared adapter with the correct weapon class.
- Thermonuclear contamination and consequence values remain shared.
- Event 23 evolution access does not substitute for the required technology, project, equipment, or stockpile.

## Air Cleanliness integration

The shared mechanics currently define a normal nuclear detonation as adding 20 basis points, or 0.20 percent, to global contamination, while a thermonuclear strike adds 150 basis points, or 1.50 percent.

Event 23 should call the shared route and should not add these values itself.

Tests, accidents, and demolitions may need separate shared profiles. Their contamination should reflect the actual physical event. A failed high-explosive accident should not automatically receive the same global contamination as a full nuclear yield.

Every net 1 percent contamination change already influences Chaos through the shared system. Event 23 should not add a second contamination-derived Chaos change.

## Deaths integration

Every Event 23 action that kills people must use the shared Deaths system or a shared nuclear adapter that calls it.

This includes:

- Combat strikes.
- Test accidents.
- Test-site exposure.
- Long-term fallout.
- Depot demolition or accidental yield.
- Recovery raids when people are killed through a supported consequence route.

Event 23 should not award recruitable manpower through negative population effects. Exact state losses and death reasons should remain within the shared population transaction contract.

Every 1,000,000 tracked deaths already adds 1 Chaos. Event 23 must not duplicate that effect.

## Condemnation integration

Nuclear tests, threats, attempts, combat use, civilian targeting, cover-ups, and repeat use should feed the shared condemnation system through distinct source profiles.

Recommended distinctions:

- Hidden test with no public evidence.
- Detected test.
- Public demonstration.
- Public nuclear threat.
- Aborted but observable launch attempt.
- Military or logistics strike.
- Industrial strike.
- Capital strike.
- Populated-center strike.
- Cover-up of an accident.
- Repeated use inside the shared recent-use window.

Hidden evidence should remain hidden until disclosure. Public condemnation should not rise because the opening event secretly grants bombs.

The Event 23 category can summarize current public consequences, but the Chaos Meter Condemnation tab remains the authoritative detailed display.

## Direct Chaos integration

The shared mechanics define a declining direct nuclear-use ladder of plus 10, plus 5, plus 3, plus 2, then plus 1 for later uses. Event 23 should use the shared ladder.

Tests and threats should have their own event-tuned Chaos effects only when the accepted implementation supports them. They must not be counted as combat nuclear use unless the shared system classifies them that way.

Suggested event-owned Chaos changes:

- Hidden opening: modest or zero public Chaos, because the arsenal remains secret.
- Public demonstration: a meaningful one-time Chaos increase.
- Public nuclear ultimatum: a smaller increase, with repeat pressure controlled by cooldown.
- Breakaway custody crisis: increase based on number of disputed operational devices and public exposure.
- Successful reciprocal stand-down or verified dismantlement: limited Chaos reduction.

Exact values require the balance pass and must be centralized.

## Fallout world-end integration

Fallout is the natural terminal consequence of extreme nuclear use.

Event 23 contributes through normal shared contamination and use. It does not own Fallout.

When the shared Fallout route activates:

- Event 23 stops new tests, threats, targeting, production grants, and exchange actions that conflict with the terminal state.
- Active Event 23 preparation missions cancel or freeze according to the shared world-end policy.
- Reserved bombs return only if they were not released or destroyed.
- The Event 23 decision category hides or changes into a noninteractive historical summary if the shared UI supports it.
- Event 23 does not fire a competing super-event.

Event 23 should have no public world-end row in Event Details.

## Final Silence scenario boundary

The supplied mechanics guide identifies `SCN-004 Final Silence` as an explicit manual nuclear or thermonuclear scenario. The supplied scenario CSV snapshot omits that row.

Event 23 should not claim, rename, replace, or depend on `SCN-004` until the authoritative workbook and current scenario registry are inspected.

The implementation task should reconcile the documentation and registry discrepancy separately. Event 23's automatic escalation remains event-driven. It does not gain a manual triggerable scenario through this specification.

## Event 5 link

Event 5 owns Soviet Collapse. Event 23 exposes a bounded custody bridge as defined in Part 6.

The link should use explicit helper calls from Event 5 at state-transfer and settlement points. Event 23 should not monitor every country every day for Soviet breakaways.

Event 5 can query:

- Whether a Soviet arsenal exists.
- Which registered sites are affected.
- Whether a breakaway has physical custody.
- Whether a nuclear settlement remains unresolved.

Event 23 can query:

- Event 5 collapse stage.
- Breakaway origin and parent relationship.
- State transfer and controller results.
- Event 5 settlement or reunification outcomes.

No Event 23 action should advance Event 5's collapse evolution, release count, coalition, or terminal route unless an accepted Event 5 API explicitly owns that interaction.

## Event 32 Missiles link

Event 32 remains a separate event.

Event 23 may expose hooks for:

- Soviet demand for a longer-range delivery route.
- Detection that a missile route is available.
- Missile-backed target range and response time.
- Increased arms-race pressure after public Soviet testing.
- Exchange targeting through a verified shared missile delivery adapter.

Event 23 must not grant Event 32 technology, fire Event 32, create missile equipment, or assume its implementation exists.

## Event 76 USA tests weapons link

Event 76 remains a separate event.

Event 23 may expose hooks for:

- First Soviet public test.
- Private foreign confirmation.
- First Soviet public ultimatum.
- First Soviet combat use.

If Event 76 is later implemented, it can use these hooks to modify its own availability, test preparation, or intensity. Event 23 should never create the United States event content inside its own chain.

## Event 47 BOOM link

The supplied catalog only identifies Event 47 as `BOOM` and does not provide a reworked implementation contract.

Event 23 may expose generic nuclear-use and explosion history through shared systems. No special Event 47 bridge should be implemented until Event 47's accepted design and ownership are known.

## Other shared event interactions

### White Peace

A nuclear ultimatum or exchange stand-down can offer a bounded white peace or armistice outcome through verified shared peace helpers. Event 23 should not force Event 9 to fire or consume its identity.

### Independence Wave

A country released through Event 6 can become a normal coercion target only when it satisfies the Event 23 rules. It does not inherit Soviet collapse custody unless it controls a registered Soviet site through a verified origin link.

### Secret Alliance and factions

A threatened target may seek faction protection. Event 23 should use current faction state and should not reveal unrelated secret systems.

### Natural disasters and infrastructure damage

A disaster that damages a registered reactor, storage, command, or delivery site can affect Readiness, Integrity, or exposure through a narrow hook. Event 23 should not call a disaster merely to create difficulty.

### Chemical and biological systems

Nuclear use adds its own condemnation source. It should share sanction and responsibility presentation with chemical and biological use without merging payloads, stockpiles, delivery rules, contamination ledgers, or research.

## Arms-race cluster role

The requested working cluster name is `Arms-race`.

The current supplied cluster catalog contains no Arms-race entry and no stable cluster ID. Event 23 should remain unclustered in implementation until:

- A stable new cluster ID is verified against the authoritative workbook and live registry.
- At least one other member has a reworked and implemented event contract.
- Member roles, minimum tiers, participation chances, danger labels, cooldown, and cluster effect order are specified.
- The cluster can fire without forcing unimplemented draft events.

When registered later, Event 23 is a likely core or severe member because it establishes the Soviet side of the race. The final member severity should be selected in the cluster specification, not guessed here.

A future Arms-race cluster could coordinate:

- Event 23 Soviet breakthrough.
- Event 76 United States testing.
- Event 32 missile proliferation.
- Event 47 only after its design is known.

The cluster must still treat each event as its own identity. Cluster firing counts as one pacing event, while member events retain their own logs, evolution state, and fire-once behavior.

## Event registration

After implementation, Event 23 should:

- Remain in the fire-once event array.
- Start at the standard fire-once weight when a valid Soviet target exists and the chaos-level gate passes.
- Show `N/A` when `SOV` does not exist or cannot receive the event.
- Remain disabled by default until the rework is implemented and accepted.
- Return to the reworked-event default allowlist only in the same change that completes registration, logs, localisation, docs, AI, assets, and audits.

Manual force-trigger mode can bypass normal timing and chaos eligibility for testing. It should not create `SOV` when the country does not exist or bypass impossible stockpile and state operations after the event opens.

## Event history log

The opening records one normal event history row.

Required visible context:

- Event ID 23.
- Event name.
- Minor Fire-Once type.
- Date.
- Soviet actor and flag.
- Event detail premise.

The generic history recorder runs before the event's immediate block in some current paths. If opening preparation must create or refresh the Soviet actor context before logging, use a shared pre-fire helper.

## Evolution log

The four true evolutions record separate evolution rows.

Recommended context:

| Type | Stage | Working meaning | Actor |
| --- | ---: | --- | --- |
| Nuclear escalation | 1 | Wider nuclear race | SOV |
| Nuclear escalation | 2 | Coercive doctrine | SOV |
| Nuclear escalation | 3 | Major nuclear war becomes possible | SOV |
| Nuclear escalation | 4 | AI first-use risk at World Collapse | SOV |

Each row should display event, stage, tier, date, actor, and enabled state across the main Evolutions tab and selected history detail view.

The Event Details evolution catalog remains a preview surface and must not show fake log dates or sequence numbers.

## Event Details direction

Event Details should explain the premise without listing hidden formulas.

The visible premise should cover:

- A secret Soviet arsenal exists.
- The Soviet Union can test, expand, threaten, and use it.
- Command, delivery, and custody determine whether the stockpile is usable.
- Collapse can scatter the arsenal.
- Extreme use can contribute to global Fallout through shared consequences.

It should not reveal hidden target scores, accident weights, AI first-use gates, false-warning incidents, secret foreign evidence, achievement conditions, or exact evolution timing.

## Global threat state

The hidden opening should not automatically mark the Soviet Union as a public existential threat.

Event 23 should set a registered world-threat source only after a public threshold such as:

- Public demonstration.
- Public nuclear ultimatum backed by a prepared device.
- Combat use.
- A public breakaway arsenal crisis.
- Multi-major exchange.

The source can clear after a verified moratorium, complete dismantlement, or a durable settlement, provided no Event 23 nuclear actor remains in an active threat posture.

The exact registration must use the shared world-threat aggregate and update its documentation in the same implementation change.

## Documentation and spreadsheet alignment

Implementation must update:

- The Event 23 player-facing event document.
- This specification package when accepted implementation changes the design.
- Event log and detail localisation.
- Evolution detail localisation.
- Super-event research documentation.
- Shared nuclear API documentation when a new adapter is created.
- Event 5 integration documentation.
- The authoritative event catalog workbook.
- Exported CSV snapshots through the repository exporter.

The CSV files supplied with this planning task are read-only snapshots. They must not be edited as the source of truth.
