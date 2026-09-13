# Event 037 implementation acceptance criteria

## Purpose

This file converts the accepted design into pass or fail implementation checks. It does not replace live repository inspection, HOI4 MCP evidence, source review, or in-game testing by the user.

## 1. Event identity and registration

- Entry event uses `chaosx.nr37.1`.
- Event ID `37` is registered as Minor Repeatable.
- Chaos level is `1`.
- Event remains a Low member of Various Anomalies.
- Event is restored to the reworked-event default allowlist only when implementation is ready.
- One automatic firing creates one shared pacing event.
- Repeatable weight, recovery, and cap reduction use the shared event system.
- One firing creates one Event 037 history entry.
- Global state changes apply once in multiplayer and cluster contexts.
- Event Details, event-name selectors, debug-name selectors, actor behavior, history, and evolution previews are aligned.

## 2. Source and engine proof

- Required offline wiki pages and installed vanilla documentation are read before engine-facing implementation.
- At least one vanilla or established Chaos Redux precedent is inspected for state population gain, state population loss, decision targeting, dynamic modifier presentation, events, achievements, and report art.
- Actual engine behavior for positive real state population mutation is proven.
- If no existing neutral helper is suitable, a shared positive-population helper is created only after proof and documented with purpose, scope, inputs, outputs, defaults, side effects, and example.
- Existing exact civilian-population loss contracts are reused for deaths.
- Any new shared classifier or helper remains neutral and cross-system. Event-owned orchestration stays with Event 037.
- Required HOI4 MCP event inspection, render, and comparison routes are used for the final chain.
- Every weighted surface follows the probability audit cycle.

## 3. Valid-state transaction

- Every valid inhabited state is evaluated once at firing.
- Invalid, empty, wasteland, or unsafe nonhuman states are skipped.
- Populated occupied states are handled through the defined controller and owner rules.
- Pre-fire state population is snapshotted before any grant.
- Stage grant uses the accepted ratio, floor, cap, and local ceiling shape.
- Applied population gain is real state population.
- State provenance increases by exactly the applied gain.
- Country and world totals increase by exactly the sum of applied gains.
- No report, delayed event, player option, cluster member, or multiplayer client reapplies the transaction.
- State invalidation during firing produces no half-applied ledger.
- Latest-firing totals are available only after the transaction completes.

## 4. Provenance invariants

- Every state begins with zero Event 037 provenance.
- Provenance never falls below zero.
- Provenance never exceeds real state population.
- Repeated firings add to the same living total.
- Original population is derived safely from real population minus provenance.
- Country and world totals update incrementally after creation, death, movement, and ownership change.
- Bounded reconciliation can repair totals from authoritative state data.
- Reconciliation is not a recurring whole-world runtime loop.
- Save and reload preserve ledgers, totals, milestones, policy, integration, and pending receipts.
- Transaction IDs or equivalent proof prevent replay after reload.

## 5. Ordinary mortality

- Untargeted real civilian loss reduces Event 037 provenance proportionally.
- Rounding conserves applied population loss.
- Provenance reduction cannot exceed applied loss or living mysterious population.
- The population-loss owner records Deaths once.
- Event 037 does not duplicate the death cause.
- Famine, bombing, nuclear, disease, disaster, chemical, biological, cannibalism, and other ordinary losses all preserve the same contract.
- A mysterious-majority state behaves correctly.
- A state reaching zero population leaves no positive provenance.

## 6. Targeted movement and killing

- Targeted requests are limited by living mysterious population.
- Migration owns origin debit, route deaths, survivors, destination credit, and trapped people.
- Event 037 updates provenance only from applied Migration results.
- Ordinary movement uses a proportional mysterious share unless a narrower cohort is proven.
- Targeted relocation can move a fully mysterious cohort up to the ledger amount.
- Failed routes do not erase people.
- Closed borders create trapped population.
- Forced-displacement deaths are recorded through Migration once.
- Forced labor and systematic killing use Camp and Repression.
- Systematic killing applies exact real population loss and exact provenance loss.
- Evidence, discovery, Condemnation, resistance, survivor flight, sanctions, and perpetrator history remain active.
- No ledger-only pressure reduction exists.

## 7. Integration and manpower

- Real population appears immediately.
- Administrative and military integration is tracked separately.
- Baseline integration begins high and later stages begin lower under overload.
- Integration responds to policy, capacity, occupation, famine, persecution, war, and projects.
- Full military benefit does not appear instantly for every created person.
- If engine limitations require an approximation, real population remains authoritative.
- Any recruitable-manpower reconciliation is proven against engine behavior.
- Integration effects end or transform when the cohort becomes fully absorbed.
- The same population cannot receive duplicate recruitment benefits.

## 8. Overpopulation Pressure

- Country has one public pressure value from `0` to `100`.
- Public stages use thresholds `20`, `40`, `60`, and `80`.
- State pressure uses mysterious share, capacity, food, movement, damage, integration, and repeated arrival facts.
- Country aggregation uses both population-weighted burden and severe-state visibility.
- One tiny state cannot dominate a huge country without a justified weighting fact.
- A major capital or industrial state remains significant.
- Player sees stage, trend, next threshold, main positive factor, main negative factor, and useful response.
- Hidden component values do not become a cluttered public ledger.
- Pressure changes after every material creation, loss, movement, capacity, Famine, or occupation transaction.
- Mortality-caused pressure reduction is identified as mortality or atrocity.
- Threshold rewards cannot be farmed through oscillation.

## 9. Demographic dividend and strain

- Dividend scales with integrated population and spare capacity.
- Dividend is weak or absent before meaningful integration.
- Overcrowded pressure largely neutralizes it.
- Emergency and Breakdown apply meaningful strain.
- Trapped, starving, excluded, or imprisoned population cannot create full dividend.
- The system uses a staged dynamic effect or similarly clean lifecycle.
- Repeated firings do not create permanent idea stacks.
- Positive and negative effects materially change player incentives.
- Small countries and major powers receive scale-appropriate results.

## 10. Evolutions

### Population Surge

- Eligibility begins at `200` Chaos.
- Base pacing is near the accepted `90` day direction.
- Future firings use Evolution I scale.
- Housing, utilities, services, agriculture, and planned settlement become meaningful.
- Evolution I activation logs once and adds zero Chaos.

### Overpopulation Crisis

- Eligibility begins at `400` Chaos.
- Base pacing is near the accepted `120` day direction.
- Future firings use Evolution II scale.
- Event 037 burden feeds Famine and Migration through proven adapters.
- Evolution II can function if Evolution I is disabled.
- Activation logs once and adds zero Chaos.

### Humanity Multiplies

- Eligibility begins at `600` Chaos.
- Base pacing is near the accepted `150` day direction.
- Future firings use Evolution III scale.
- Constructive national programs and extreme policy routes become available under their conditions.
- Evolution III can function if lower stages are disabled.
- Activation logs once and adds zero Chaos.

### Pre-fire evolution

- First firing uses highest enabled eligible stage.
- Disabled stages remain unrecorded.
- Required lower mechanics are available without fake lower evolution logs.
- Concrete population outcomes can trigger one-shot Chaos milestones after application.

## 11. Direct Chaos

- First manifestation adds `2` Chaos once.
- World mysterious-population share milestones at `1%`, `5%`, `10%`, and `25%` add the accepted one-shot amounts.
- One extraordinary firing can add `5` once when it creates at least `5%` of pre-fire world population.
- Evolution state adds zero.
- Famine deaths, displacement deaths, atrocities, wars, annexations, and other shared sources are not duplicated.
- Recovery removes `2` only after a proven crisis and full stable year.
- Recovery cannot be farmed.

## 12. Decisions and missions

- Ordinary category communicates total, pressure, policy, and selected state.
- Category picture contains no fake controls.
- Policy stance has meaningful lock or transition cost.
- Open Integration, Managed Settlement, and Restricted Registration create distinct play.
- Selected-state list prioritizes real urgency.
- Human players see one target at a time.
- AI can evaluate all valid targets.
- Visible primary actions stay within the accepted phase budget.
- One action uses no more than four spendable cost types.
- Every displayed cost has a correct texticon.
- Costs scale with population, damage, distance, route, capacity, war, and industry.
- Shared Famine and Migration actions are not duplicated.
- Housing, utilities, services, planned settlement, logistics, relief, new cities, and national programs have meaningful effects.
- Missions require active work and use useful durations.
- Goal-style objectives auto-complete when conditions are met.
- Failure and partial success have distinct consequences.
- Stale state selections, requests, missions, and decisions clean up.

## 13. AI and weighted logic

- Every weighted surface is inspected through the probability workflow.
- Baseline scenario IDs in the probability matrix are evaluated.
- Any weight patch receives a before and after comparison.
- Inclusive support dominates ordinary viable cases.
- Relief-dependent AI seeks relief instead of impossible construction.
- Wartime AI protects front supply.
- Donors cannot send missing resources.
- Destinations cannot accept invalid cohorts.
- Atrocity choices require the full mapped political and crisis conditions.
- Democracy and viable relief strongly suppress atrocity.
- Actual nonhuman countries receive no ordinary action candidates.
- Invalid states, countries, routes, and cohorts have zero weight.
- Flavour diversity memory prevents repetition and starvation.

## 14. Event chain and writing

- One global manifestation report appears per firing.
- National report appears only for significant human-country impact.
- No state-by-state popup flood exists.
- Flavour pool covers baseline and all three evolutions.
- Flavour responds to state, policy, integration, Famine, Migration, and repression.
- The origin remains unresolved.
- No text confirms aliens, time travel, clones, returned dead, alternate universes, or secret projects.
- Cross-event callbacks remain suggestive and non-canonical.
- Player-facing text contains no developer wording, update history, debug language, raw variable names, or hidden spoilers.
- Final wording follows project prose rules.
- Event log and Event Details use final player-facing wording.

## 15. Shared-system ownership

- Famine owns food values, relief, famine stages, mortality, and map mode.
- Migration owns movement values, routes, reception, trapped people, settlement, deaths, and map mode.
- Deaths owns death records and chaos from deaths.
- Camp and Repression owns sites, labor, killing, evidence, and reform.
- Condemnation owns public diplomatic consequence.
- Shared civilian classifiers control special and nonhuman eligibility.
- Event 037 does not create duplicate systems.
- Every shared transaction changes real population once and provenance once.

## 16. Performance and multiplayer

- One bounded world-state pass occurs at firing.
- Recurring processing uses active state and country registries.
- No unauthorized recurring all-world country or state scan is introduced.
- Totals update incrementally.
- Resolved entries leave registries.
- Multiplayer world transaction applies once.
- Each human receives relevant reports without duplicate effects.
- Save and reload preserves each national policy and target.
- Cluster firing applies Event 037 once.

## 17. Assets and achievements

- Report image uses accepted documentary direction and verified report family.
- Decision category picture uses verified consumer and no fake controls.
- Category icon and each event-owned icon family have separate source art.
- Modifier and state icons are separate assets.
- Shared system actions reuse established art only after a semantic audit.
- Three achievement triplets exist and use separate source art.
- Native transparency is preserved where required.
- Final DDS files, sprite handoff, manifest, and runtime consumers are complete.
- Temporary asset evidence is promoted or retained according to status.
- Achievement triggers, disqualifiers, persistence, localisation, and icons align.

## 18. Catalog and documentation

- Obsolete major-country recruit premise is removed from the authoritative workbook.
- Workbook row matches final Event Details and evolution wording.
- CSV exports are regenerated from the workbook.
- CSV exports are not edited directly.
- Various Anomalies registry ID is assigned only after collision check.
- Event docs describe population, ledger, pressure, evolutions, decisions, adapters, assets, achievements, and validation.
- Shared dynamic-helper documentation is updated for any new public helper.
- Completion report lists meaningful tests, files, assets, audits, and unresolved blockers.
- Accepted plan material is folded into the source spec or reported with a clear disposition.

## 19. Final validation scenarios

At minimum, validate:

1. Baseline firing in a normal 1936 setup.
2. Tiny inhabited state.
3. Very large population state.
4. Repeated firing and compounding.
5. Highest eligible pre-fire evolution.
6. Disabled lower evolution with enabled higher evolution.
7. Ownership and control changes.
8. Ordinary famine mortality.
9. Bombing or disaster mortality.
10. Internal settlement.
11. Cross-border reception.
12. Trapped border cohort.
13. Forced relocation with route deaths.
14. Forced labor.
15. Systematic killing and discovery.
16. Mysterious-majority state.
17. Actual nonhuman exclusion.
18. Multiplayer one-transaction behavior.
19. Cluster one-transaction behavior when registered.
20. Save and reload after each major transaction.
21. Event Logs and Event Details.
22. Achievement progress and disqualification.
23. Sparse registry cleanup.
24. Probability scenarios before and after any weight change.

## 20. Completion rule

The event cannot be marked complete while any accepted population, provenance, pressure, evolution, humanitarian adapter, decision, AI, flavour, asset, achievement, event-log, documentation, or catalog surface is missing or simplified without approval.

Passing syntax or loading is not enough. Completion requires implemented behavior, aligned player-facing text, final assets, probability evidence, event-chain evidence, meaningful balance review, and an honest final audit.
