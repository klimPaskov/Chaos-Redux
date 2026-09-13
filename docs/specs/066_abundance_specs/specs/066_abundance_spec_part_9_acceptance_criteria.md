# Acceptance Criteria and Completion Standard

## Event identity

- Event ID remains `66`.
- Entry event uses the normal `chaosx.nr66.1` identity.
- The old `CIC` planning concept and random-major market grant are fully replaced.
- Event 66 is registered as Minor Repeatable with Chaos level `1`.
- It remains disabled by default while still marked To Be Reworked.
- It enters the reworked-event default enable set only after the complete implementation and audits pass.

## Global behavior

- One firing creates one global Abundance wave.
- Every valid country is processed once.
- Each country builds its pool from its own current mechanics.
- Each country receives four stored choices.
- Human countries see a visible four-option event.
- AI countries resolve the same stored card structure.
- The wave counts once for pacing, repeatable cap change, event history, and cluster accounting.
- No periodic whole-world on-action is added for Event 66.

## Provider architecture

- Event 66 has no central favored-value list.
- Base game, DLC, country-specific, and Chaos Redux values enter through owner providers or dynamic family providers.
- Every provider has stable identity, validity, presentation, application, AI, and receipt behavior.
- Enumeration is read-only.
- Application uses owner callbacks.
- Provider registration is idempotent.
- Hidden values do not leak before reveal.
- Retired, raw, proof-only, and unsafe variables have documented exclusions.
- A complete value inventory is compared with provider coverage.
- Every uncovered value family is registered, blocked, or excluded with a clear reason.

## Choice generation

- Four cards are distinct by full signature.
- Baseline cards contain one value.
- Evolution II can produce pairs only when enabled and at `400+` Chaos.
- Evolution III can produce triples only when enabled, with Evolution II enabled, and at `600+` Chaos.
- Pair and triple values are drawn independently from the full current pool.
- No authored bundles or thematic packages exist.
- Candidate generation does not use country utility or AI preference.
- Harmful values remain eligible.
- Evolution weighting shifts the same pool without creating a separate list.
- Recent-value dampening improves variety without excluding candidates.
- Option position has no bias.
- Rolls remain fixed through save, load, hover, window changes, and time passage.

## Abundance results

- Every provider defines a visible and strong abundance result.
- Accumulators use country-relative grants with floors and safe ceilings.
- Bounded gauges reach their high practical range.
- Stockpiles and capacities use valid tokens and owner caps.
- Stage mechanics use owner transitions.
- State-distributed effects are bounded.
- High values follow the public meaning of the candidate.
- Harmful values become more harmful when abundant.
- Persistence and repeat stacking use owner-defined caps.
- Saturated candidates remain eligible only when a meaningful saturation consequence exists or an intentional useless result is explicitly documented.

## Transaction integrity

- Every atomic item has a unique wave-item identity.
- The same item cannot apply twice.
- Pair and triple items revalidate separately.
- Partial results keep successful items and report failures.
- Failed items are not rerolled after selection.
- Owner receipts expose success, magnitude or stage, harm class, target summary, persistence, and failure reason.
- Other event owners are not marked fired through enumeration or ordinary application.

## Shared-system integrity

- Population changes use exact population and Deaths paths.
- Air Cleanliness changes use source accounting.
- Condemnation changes use evidence and source categories.
- Famine and migration changes use their owner interfaces.
- Global values use country-attributable owner contributions.
- Shared Chaos sources are not double counted.
- First global manifestation gives one `+5` Chaos change.
- Repeat firings and evolution activation give no automatic Event 66 Chaos.

## Evolutions

- Strange Abundance is recorded and active only when enabled at `200+` Chaos.
- Abundance Comes in Pairs is recorded and active only when enabled at `400+` Chaos.
- Everything in Excess is recorded and active only when enabled at `600+` Chaos.
- Stages record in order when several become eligible together.
- The evolution actor is global.
- Event Details shows the three accepted evolution names and visible effects.
- Disabled stages do not set recorded flags or alter hidden generation state.

## Cluster integration

- Event 66 occupies Low, Medium, and High Sudden Abundance slots.
- The final cluster ID is verified against the authoritative workbook and runtime registry.
- Cluster Details displays three Event 66 member rows.
- Low, Medium, High, and Standard profiles are mechanically distinct.
- Multiple Event 66 slots in one cluster firing coalesce into one wave.
- Coalescing uses the highest severity and bounded slot-count pressure.
- Coalescing creates one popup set, one history entry, one cap change, and one pacing result.
- Cluster profiles never bypass evolution cardinality gates.
- Effective cluster probability is audited so three slots do not create accidental dominance.

## AI

- AI evaluates only its four generated cards.
- AI utility has no effect on candidate generation.
- AI uses shortage, war state, plan fit, overflow, danger, desperation, persistence, route identity, and bounded noise.
- AI can choose harmful values.
- Stable ordinary AI avoids obvious self-destruction when strong safe choices exist.
- Desperate and special-route AI can take greater risks.
- Pair and triple scores use atomic values plus bounded interaction facts.
- AI never chooses by option index.
- Every weighted surface has baseline and comparison evidence from the probability workflow.

## Multiplayer and persistence

- Authority creates each random result once.
- Every player country receives its own choices.
- One player's selection cannot alter another country's stored cards.
- Pending choices survive save and load.
- A pending country is skipped by a later wave to prevent overwrite.
- Country control changes do not reroll cards.
- Achievement ledgers cannot be combined through tag switching.

## Presentation

- The standard event popup is used.
- Four option shells display stored dynamic card identities.
- Pair and triple names fit the option line through provider short names.
- Tooltips show full names, current state, broad result, target, risk, and persistence when available.
- Player text contains no raw variables, provider IDs, hidden branches, debug counters, probability formulas, or implementation history.
- Event Details explains global per-country generation, harmful eligibility, evolutions, and cluster roles.
- One global history row is recorded per wave.
- Country receipts do not flood Event History.

## Achievements

- All three achievements are implemented with exact player-country tracking.
- Unlocks require successful owner receipts.
- Force and debug launches are disqualifying.
- Partial bundle applications do not count as complete.
- Provider danger, recovery, abundance, and persistence checks are used where required.
- All required icon states are present and wired.

## Assets

- The 210x176 report event image is generated and processed through the report-event workflow.
- The image has a period documentary look, no fake readable text, and no modern objects.
- Three distinct completed achievement icons exist at 64x64.
- Required grey and not-eligible achievement states follow the current consumer pattern.
- Asset manifests, source evidence, processed previews, DDS files, and sprite handoffs agree.
- No runtime asset points into a temporary docs workspace.

## Documentation and catalog

- Event documentation explains provider coverage, generation, magnitude, AI, multiplayer, evolutions, cluster coalescing, Chaos sources, assets, and achievements.
- Event Log, Event Details, localisation, docs, and catalog wording agree.
- The authoritative event catalog workbook row for ID 66 is updated.
- The Sudden Abundance cluster row and three Event 66 slots are updated.
- The export script regenerates all three CSV snapshots after the workbook save.
- Export-only CSV files are not edited directly.

## Required audits

Before completion, the implementation must receive:

- event-chain inspect, render, and compare evidence
- provider and value-space coverage audit
- AI and generation probability baseline audit
- probability comparison after tuning
- localisation audit
- asset review and manifest audit
- achievement tracking audit
- cluster accounting audit
- multiplayer and save-load scenario review
- improvement-loop pass or closure handoff
- event completion audit
- spreadsheet alignment pass

## Blocking failures

Any of these conditions blocks completion:

- a small hardcoded candidate list presented as dynamic coverage
- direct mutation of foreign system ledgers
- hidden mechanic leakage
- missing owner application callbacks
- client-side rerolls
- cards changing after save load
- duplicate application receipts
- pair or triple packages authored by hand
- harmful values filtered from eligibility
- utility used during generation
- several country history rows per wave
- several Event 66 waves from one cluster transaction
- missing AI behavior
- missing probability evidence
- missing achievements or assets
- direct edits to catalog CSV exports
- undocumented provider exclusions
- fallback rewards inserted when pool construction fails

## Simplification rule

The implementation may tune probabilities, magnitude constants, and provider-specific formulas after evidence.
It may not reduce provider coverage, remove harmful candidates, collapse the event into a fixed list, omit country-local generation, omit cluster slots, omit AI, omit achievements, or replace owner callbacks with generic direct writes.

Any unavoidable limitation must be named in the completion report with the affected provider families and gameplay consequences.
