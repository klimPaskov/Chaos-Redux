# Event 41 acceptance criteria

## Core incident

- Event 41 remains Minor Repeatable, Chaos level 1, and a Low member of the Diseases cluster.
- A root firing selects one valid ordinary country at war with a real active front.
- Special Chaos countries are excluded through the shared classifier.
- The opening infects a bounded coherent frontline group.
- The baseline does not infect most of the target army at once.
- Player-controlled countries remain valid targets.
- Invalid target selection fails closed without an empty incident.

## Public mechanic

- Army Infection Pressure is the only persistent event-specific value the player must track.
- The category shows pressure stage, trend, main causes, and current posture clearly.
- Hidden profiles, node scores, medical capacity, evacuation capacity, and spread weights remain internal.
- The player can identify the infected sector and useful response from the category and map.

## Military effects and manpower

- Affected formations suffer meaningful readiness and combat penalties.
- Disease removes or blocks real military manpower through an engine-verified model.
- Active sick, convalescent, recovered, and dead soldiers remain distinct.
- Recoverable soldiers return gradually.
- Fatal cases enter the shared Deaths system once as military casualties.
- Event 41 does not delete equipment to represent sickness.
- The manpower ledger cannot create free manpower or duplicate deaths.
- A failed baseline can push the worst-hit front toward roughly half effective strength over time.
- The baseline does not routinely halve the whole national army.

## Simulation and performance

- Processing is bounded to registered active countries and affected nodes or formations.
- No daily whole-world country, state, or division scan is introduced.
- Ordinary processing uses a clear cadence, preferably weekly.
- Spread evaluates proven military links and valid connected candidates.
- Invalid, annexed, transferred, or resolved entries are cleaned promptly.
- Episode generation prevents duplicate cross-border and civilian handoffs.

## Decisions and missions

- The temporary category exposes three to five primary actions in a normal phase.
- No more than one sector-rotation mission is active at a time.
- Rotation requires a real operational sacrifice and a valid destination or in-place alternative.
- Mission success auto-completes after the player holds the conditions.
- Quarantine, hospitals, sanitation, evacuation, corridor repair, emergency mobilization, district isolation, and posture actions follow the spec.
- Each action uses no more than four spendable cost types.
- Costs use matching texticons and clear blocked reasons.
- Decisions do not become repeated political power purchases.
- Repeating the same action has diminishing returns or a cooldown.
- Fight Through the Outbreak preserves operational freedom and increases disease risk without granting free combat power.

## Resolution and aftermath

- Resolution requires sustained low pressure, low active infection, and a no-spread window.
- Penalties fade through recovery stages.
- Convalescent soldiers return in bounded installments.
- Outcome tiers distinguish clean containment, ordinary costly containment, medical exhaustion, and a shattered infected front.
- Recent-survivor resistance reduces immediate repeat risk without permanent immunity.
- Repeat firings can select a different sector or profile.

## Evolution I

- Evolution I becomes eligible at 200 or more Chaos and uses paced activation.
- Active-event entry upgrades a running episode without resetting its ledgers.
- Pre-fire evolved opening begins wider and can test one valid foreign military route.
- Allied and enemy transmission requires sustained proven military contact.
- Secondary national outbreaks start weaker by default and receive their own category.
- One country cannot receive duplicate Event 41 categories.
- Evolution I does not create civilian cases.

## Evolution II

- Evolution II becomes eligible at 600 or more Chaos and uses paced activation.
- Active-event entry adds civilian and distant-theater risk without resetting military cases.
- Pre-fire evolved opening can begin with an exposed rear transport node and immediate spillover risk.
- Civilian spillover uses a proof-carrying adapter to the existing outbreak system.
- Event 41 does not own civilian mortality, Air Cleanliness contribution, famine ledgers, or migration cohorts.
- Accepted receipts prevent duplicate civilian outbreaks in the same state.
- The military episode can close while a civilian outbreak continues under its owner.

## Cross-system integration

- Biological warfare, contamination, famine, migration, disasters, bombardment, field hospitals, logistics, and Air Cleanliness use documented ownership boundaries.
- Event 41 does not duplicate shared Chaos sources from war, deaths, contamination, or weapon use.
- The full event-owned Chaos impact map is implemented with generation guards and reversal logic.
- Cluster firing counts once for pacing.
- Event 41 is skipped cleanly from a cluster when no valid wartime target exists.

## AI and probability

- AI action weights use pressure, front threat, medical capacity, supply, transport, and evolution state.
- AI does not start impossible missions or spend unavailable resources.
- AI fight-through behavior is limited to severe strategic need.
- AI protects civilian hubs and demobilization routes under War Plague.
- Every weighted surface receives a baseline probability audit and post-change comparison using the named scenarios.
- The audit distinguishes exact, bounded, sampled, score-only, and unresolved evidence.

## Presentation

- Event reports mark material milestones and avoid weekly popup spam.
- Event Details, Event Logs, evolution views, category text, map highlights, and formation tooltips agree.
- Ordinary pressure stages are not logged as evolutions.
- The category picture contains no fake controls.
- Icons are made for their exact asset families and are not resized substitutes from unrelated surfaces.
- Text remains serious, concrete, and soldier-centered.
- Player-facing text does not expose raw variables, exact hidden formulas, or future surprise conditions.

## Achievements

- All four planned achievements are implemented or explicitly reported as blocked.
- Tracking captures maximum pressure, actions, deaths, recoveries, spillover, sector losses, and disqualifiers.
- Achievement icons and localisation are complete.
- No achievement unlocks merely because the event fired.

## Documentation and catalog

- Permanent event documentation covers the full implemented lifecycle.
- Event Details and workbook wording match.
- The canonical XLSX is updated.
- CSV exports are regenerated through the repository exporter.
- Asset provenance and runtime crosswalks are preserved in permanent documentation before temporary workspace cleanup.

## Completion evidence

The implementation completion report should include:

- files changed
- event and decision surfaces implemented
- evolution and adapter behavior
- manpower and death-accounting evidence
- AI probability evidence
- cluster and Chaos history evidence
- asset coverage
- achievement coverage
- documentation and workbook alignment
- unresolved blockers or simplifications

No completion claim is valid while a required mechanic, AI path, asset, achievement, adapter, catalog update, or audit remains silently omitted.
