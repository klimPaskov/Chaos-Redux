# Goal: Implement Event 066 Abundance Completely

Implement Event 66 from `docs/specs/066_abundance_specs/` and read all files there before editing.
Use `prompts/066_abundance_coding_prompt.md` as the main handoff and follow the other prompt files for their named surfaces.
Follow `AGENTS.md`, the named project skills, and required wiki and vanilla references.
Keep Event ID `66` and `chaosx.nr66.1`, replacing the old `CIC` behavior.

One selection creates one world wave, snapshots every valid country once, and gives each country four stored cards generated from applicable values.
The event core must not contain a favored list.
Implement an idempotent owner-provider registry covering core HOI4 values, DLC mechanics, country systems, Chaos Redux mechanics, event values, and dynamic stockpile families.
Complete the repository-wide value inventory and give every player-meaningful value a provider, family, reveal gate, reasoned exclusion, or blocker.
Raw proof variables, indexes, debug counters, unsafe global totals, and hidden spoilers are not candidates.

Provider enumeration must be read-only.
Selected values must apply through owner callbacks with save-safe idempotent receipts.
Use owner paths for shared ledgers and never mark another event fired or write its internal state directly.

Baseline cards contain one value.
Strange Abundance at `200+` shifts the same live pool toward unusual, rare, country-specific, DLC, Chaos Redux, active-crisis, and harmful values.
Abundance Comes in Pairs at `400+` permits independently drawn pairs.
Everything in Excess at `600+` permits independently drawn triples and raises strange weighting again.
No authored packages, utility filters, or hidden best-choice generation are allowed.
Harmful values remain eligible.
AI utility begins after its cards are stored.

Use the standard event popup with four dynamic option shells.
Preserve cards and option order through save, load, and control changes.
Revalidate selected items without rerolling.
Apply bundle items independently, retain successful items in partial results, and report failures.
A later wave cannot overwrite a pending choice.

Register Event 66 as Low, Medium, and High logical slots in Sudden Abundance.
Verify provisional cluster ID `9`, reconcile Event 64 and other accepted members, and coalesce every Event 66 slot hit in one cluster transaction into one wave.
Use the highest severity and bounded slot-count pressure, with one card set per country, one log row, one cap change, and one pacing result.
Cluster severity cannot bypass evolutions.

The first campaign manifestation adds one guarded `+5` Chaos entry.
Ordinary repeats, evolution activation, bundle size, and cluster coalescing add no automatic direct Chaos.
Prove that shared sources are not counted twice.

Implement all AI, multiplayer, persistence, pool-failure, novelty, magnitude, achievements, asset, localisation, Event Details, evolution-log, cluster, documentation, and workbook requirements in the spec pack.
Never edit catalog CSV exports directly.

Use HOI4 MCP event inspect, render, lint, and compare.
Run the named probability baseline, tuning, and `hoi4.probability_compare` cycle.
Use the correct project subagents with `fork_context=false` for architecture, assets, localisation, probability, completion, and spreadsheet work.
Run and resolve `chaosx_improvement_loop_planner` after a meaningful implementation tranche.

Keep iterating until `specs/066_abundance_spec_part_9_acceptance_criteria.md` passes in full.
Do not use placeholders, fallback rewards, direct foreign writes, partial coverage, or silent simplifications.
Do not claim completion until implementation, audits, assets, achievements, docs, logs, cluster state, localisation, workbook, and exported catalogs agree.
Provide a completion report covering provider breadth, probability evidence, Chaos sources, multiplayer, persistence, assets, achievements, catalog changes, unresolved plans, blockers, and simplifications.
