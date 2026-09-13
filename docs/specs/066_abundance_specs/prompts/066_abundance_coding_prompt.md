# Event 066 Abundance Coding Prompt

Implement the accepted Event 66 Abundance specification to its full extent.
The source-of-truth folder is `docs/specs/066_abundance_specs/`.
Read every file in that folder before editing.

## Required project guidance

Read and follow:

- `AGENTS.md`
- `chaos-redux-events`
- `chaos-redux-subagents`
- `chaos-redux-improvement-loop`
- `chaos-redux-event-assets`
- the current localisation rules
- the current dynamic effects and triggers registries
- the offline Paradox wiki pages and installed vanilla documentation required by the touched event, effect, trigger, localisation, AI, achievement, and cluster surfaces
- current Chaos Redux precedents for global events, repeatable events, event details, evolution logs, cluster members, dynamic scripted localisation, and save-safe random choices

Use the installed HOI4 MCP event tools for narrow inspection, rendering, linting, and post-change comparison.
Use the probability tools through the required auditor for every weighted surface.

## Event identity

Keep Event ID `66` and entry identity `chaosx.nr66.1`.
Replace the old `CIC` behavior completely.
Register Event 66 as Minor Repeatable with Chaos level `1`.
Do not add it to the default reworked-event enable allowlist until every implementation, text, AI, asset, achievement, cluster, documentation, and audit requirement is complete.

## Global event flow

One normal Event 66 selection creates one global wave and one pacing transaction.
Build one participant snapshot.
Process every valid country once through a bounded event-time pass.
Do not add daily, weekly, monthly, or other recurring whole-world scans.

Player countries receive a visible standard event with four stored option shells.
AI countries receive a hidden resolver over the same four stored cards.
The global history row, repeatable cap change, first-manifestation Chaos, and cluster transaction execute once.
Country application receipts execute once per selected atomic value.

A human country with an unresolved Event 66 choice is invalid for a later wave so its stored cards cannot be overwritten.
Persist pending choices, cards, option order, targets, evolution state, novelty memory, receipts, first-manifestation guard, and achievement ledgers through save and load.

## Provider contract

Use `prompts/066_abundance_provider_contract_prompt.md` and route the reusable architecture to `chaosx_scripted_system_architect` with `fork_context=false`.

Do not create a small central candidate list.
Build an idempotent registry populated by core providers, dynamic family providers, DLC providers, country packages, event systems, and crisis owners.
Every provider needs validity, spoiler-safe presentation, owner application, AI facts, deduplication, conflict, harm, rarity, strangeness, source class, and receipt behavior.

Enumeration is read-only.
It cannot fire or initialize another event, mutate gameplay, or write a ledger.
Application returns to the owner package.
Use owner APIs for population, Deaths, Air Cleanliness, Condemnation, famine, migration, occupation, stockpiles, country mechanics, and global contribution ledgers.
Do not duplicate shared source accounting.

Complete the repository-wide value inventory in `research/066_abundance_value_provider_coverage_matrix.md`.
Every player-meaningful value needs a provider, dynamic family, named reveal gate, reasoned exclusion, or blocker.
Raw proof variables, indexes, debug values, hidden spoilers, and unsafe global totals remain excluded.

## Four-card generator

Every country builds its own live candidate pool.
Generate four distinct card signatures and store them before display.
At baseline every card contains one value.
Evolution II can introduce pairs.
Evolution III can introduce triples.

Atomic values are independently drawn from the full current pool.
There are no authored packages, thematic bundles, ideology bundles, country bundles, or helpfulness filters.
Harmful values remain eligible.
Reject only exact duplicates, hard storage conflicts, invalid candidates, and malformed provider records.

Use the uniqueness hierarchy, small-pool rules, recent-value dampening, stored-roll rules, provider fault isolation, and click-time revalidation from the specs.
Do not insert fallback Political Power, dummy tokens, invalid mechanics, or no-op cards when generation fails.

Candidate generation cannot read country utility or AI preference.
Randomize final option order without index bias.

## Abundance application

Implement country-relative magnitude with provider-defined floors, caps, rounding, persistence, and strength axes.
Support accumulator, bounded gauge, stockpile, capacity, stage, state-distributed, and owner-custom shapes.
High values follow the public meaning of the candidate, including harmful gauges.

Every atomic item has an idempotent wave-item identity.
Revalidate the stored candidate at selection time.
Apply valid pair or triple items independently.
Keep successful items when another item fails.
Do not reroll failed items after the player chooses.
Return complete, partial, and rejected receipts with stable reasons.

The first campaign manifestation adds one guarded `+5` Chaos entry.
Later Event 66 firings, evolution activation, pair construction, triple construction, and cluster coalescing add no automatic direct Chaos.
Let owner consequences use their existing Chaos, Deaths, contamination, war, ideology, and other shared pipelines.

## Evolutions

Implement and log:

1. Strange Abundance at `200+` Chaos.
2. Abundance Comes in Pairs at `400+` Chaos.
3. Everything in Excess at `600+` Chaos.

The next normal Event 66 wave records newly eligible enabled stages in order, then uses them.
No separate empty announcement event is needed.

Evolution I shifts the same live pool toward rare, unusual, country-specific, DLC, Chaos Redux, active-crisis, and harmful candidates.
Evolution II permits pairs while retaining singles.
Evolution III permits triples, keeps pairs, retains rare singles, and increases strange weighting again.

Respect individual evolution enable controls.
When Evolution II is disabled, Evolution III cardinality is suppressed.
Disabled stages cannot set recorded flags, change weights, raise cardinality, or qualify achievements.
Evolution state adds zero Chaos.

## Sudden Abundance cluster

Register Event 66 as three ordered logical member rows, Low, Medium, and High, in the verified Sudden Abundance cluster.
Treat cluster ID `9` as provisional until the authoritative workbook and runtime constants confirm it.
Reconcile Event 64 and every other accepted cluster member.

Implement Low, Standard, Medium, and High strength profiles.
Multiple Event 66 slots selected in one cluster firing coalesce into one world wave.
Use the highest severity and bounded slot-count pressure.
Create one participant snapshot, one set of four cards per country, one Event 66 history row, one cap change, and one pacing result.
Do not bypass evolution cardinality gates.

## AI and probability

Implement AI card scoring after generation.
Use shortage, war state, strategic plan, headroom, overflow waste, harm, desperation, route identity, persistence, uncertainty, bundle interaction, Chaos tolerance, and bounded noise.
AI can choose harmful cards.
Stable ordinary AI should usually prefer strong safe cards, while desperate or owner-specialized AI can take greater risks.
Never choose by option index.

Run the full audit cycle through `prompts/066_abundance_ai_probability_audit_prompt.md`.
Establish named baseline scenarios before tuning.
After owner changes, run `hoi4.probability_compare` against the same scenarios.
Do not claim exact shares from an incomplete provider pool.

## Presentation and logs

Use the standard event popup and one 210x176 report image.
Do not create a dedicated scripted GUI.
Use four fixed option shells with scripted localisation from stored card data.
Providers supply short and full names.
Tooltips show current state, broad result, target, risk, and persistence without exposing raw internals.

Record one global Event 66 history row per wave with no random country actor.
Record evolution stages through the shared pipeline with global actor context.
Show three Event 66 rows in Cluster Details and one coalesced result in cluster history.
Keep country receipts out of global history.

Write final player-facing localisation from the direction in the specs.
Do not paste prompt labels, raw variables, weights, safety caps, hidden routes, provider IDs, or implementation notes into game text.
Route broad text through `chaosx_localisation_auditor` before completion.

## Achievements and assets

Implement all three achievements through `prompts/066_abundance_achievement_prompt.md`.
Use successful provider receipts, force and debug disqualifiers, save-safe timed attempts, same-country tracking, and partial-result rules.

Produce and wire every asset in `prompts/066_abundance_asset_prompt.md` through the correct asset subagents.
Create the report image and all achievement icon states.
Keep final runtime files outside temporary docs workspaces.

## Documentation and workbook

Create or update the Event 66 implementation documentation.
Document provider authoring, candidate coverage, card storage, application shapes, AI, multiplayer, evolutions, cluster coalescing, Chaos sources, achievements, assets, and meaningful validation.

Update Event Log, Event Details, scripted localisation, debug name mappings, event name mappings, cluster details, evolution details, and all related docs in the same change.

Use `chaosx_spreadsheet_doc_worker` only after final in-game wording exists.
Update only `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.
Then run `python .tools/export_event_catalog_csv.py`.
Never edit the three CSV exports directly.

## Required final passes

After meaningful implementation, use `chaosx_improvement_loop_planner` with `fork_context=false`.
Fold an accepted addendum into the source specs or record a closure handoff.
Do not spawn another pass while an earlier addendum remains unresolved.

Before completion, run:

- event inspect, render, lint, and compare
- provider coverage audit
- probability baseline and comparison audit
- localisation audit
- asset and achievement coverage review
- cluster accounting review
- save and load review
- multiplayer authority review
- event completion audit
- spreadsheet alignment pass

Provide a concrete completion report with changed files, identifiers, provider coverage, balance evidence, assets, achievements, docs, catalog changes, meaningful tests, and every blocker or simplification.

Do not claim completion while any accepted provider family, cluster slot, evolution, AI path, achievement, asset, localisation surface, document, workbook field, or audit remains missing.
Do not use fallbacks, placeholders, small fixed pools, direct foreign-ledger writes, or good-enough approximations.
