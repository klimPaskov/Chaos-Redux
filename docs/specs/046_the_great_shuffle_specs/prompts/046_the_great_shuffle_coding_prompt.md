# Event 046 coding-agent prompt

Implement Chaos Redux Event 046, **The Great Shuffle**, to the full accepted specification under `docs/specs/046_the_great_shuffle_specs/`.

Do not replace the requested system with a small popup, a temporary modifier, a value swap, a conservation shuffle, or a short hardcoded list.

Keep iterating until every accepted surface is implemented, audited, documented, and aligned.

Do not claim completion while a core family, report surface, evolution, cluster relationship, achievement, asset, localisation surface, documentation file, workbook field, or required audit remains missing.

## Read before editing

Read `AGENTS.md`, the complete Event 046 spec pack, `chaos-redux-events`, `chaos-redux-subagents`, `chaos-redux-improvement-loop`, `chaos-redux-event-assets`, `chaos-redux-decisions-missions` for report and clarity rules, `chaosx_dynamic_effects.md`, `chaosx_dynamic_triggers.md`, the mechanics guide, and the current catalog workbook contract.

Read the required offline Paradox wiki pages and current installed vanilla documentation before opening or editing engine-facing source.

At minimum cover Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding where report or action syntax is relevant, Idea modding, AI modding, technology and doctrine documentation, state buildings, equipment stockpiles, production, units, commanders, diplomacy, arrays, event targets, and scripted random behavior.

Inspect matching vanilla and Chaos Redux precedents.

Use `chaosx_repo_explorer` with `fork_turns="none"` only when file locations, existing patterns, dependencies, vanilla precedents, or edit order remain unclear.
Provide the known registration, evolution, log, Chaos, population, stockpile, map-state, production, unit, achievement, cluster, asset, documentation, and workbook context so the explorer investigates the remaining uncertainty.

The explorer must map exact files, current Event 46 remnants, Event 43 and cluster conflicts, relevant helpers, vanilla precedents, and edit order.

Use mandatory HOI4 MCP event inspection, render, lint, and post-change comparison for the event chain.

## Core event behavior

Keep Event 46 as a Chaos level 1 Minor Repeatable event with ordinary repeatable weight, recovery, cap decay, and minor pacing.

Every successful firing is one global permanent transaction.

Every family generates new values independently for every valid scope.

Never swap values, conserve old totals, compensate prior losers, punish prior winners, restore the old world, or weight a later result from an earlier firing.

Read old values only for reports, legal delta application, and reconciliation proof.

Human countries remain valid.

Special Chaos actors, actual nonhuman countries, dormant carriers, and system actors use the exact shared classifiers and owner adapters described in the specs.

Do not add a periodic whole-world on-action.

## Registry and transaction

Use `chaosx_scripted_system_architect` with `fork_turns="none"` and the dedicated architecture prompt.

Create an Event 46-owned allowlist registry with stable family identity, owner, version, capability, scope source, validity, range, distribution, compatibility, dependency, plan, commit, reconciliation, report, Chaos, AI refresh, recovery, cleanup, and tests.

Owner mechanics expose bounded adapters from owner files.

Do not scan arbitrary memory or copy every event's internal logic into Event 46.

Keep Event 46-specific orchestration out of the shared dynamic registry.

Move a helper there only when it is neutral, documented, and has unrelated callers.

Implement the transaction state machine and logical family atomicity.

Every selected result must be fixed before the first write in that family.

A pre-commit failure leaves the family untouched.

A partial commit resumes the exact plan idempotently after save and load.

Never claim unsupported general rollback.

Clear every result plan, scope marker, source-suppression marker, target, report buffer, and lock after close.

## Capability families

Implement the Baseline and Evolutions I through V according to Parts 2 and 3 and the classification matrix.

Core surfaces include basic country values, ordinary stores, absolute state population, legal industry and building families, party shares, approved law categories, approved active progress and production numbers, unit experience, commander experience, and owner adapters.

Conditional families remain disabled until their exact proof passes.

Do not treat completed technology graphs, cores, faction identity, subject identity, wars, supply graphs, stable objects, leaders, characters, templates, equipment definitions, settings, histories, or framework state as safe merely because Evolution V is active.

Evolution V means every proven safe family, not every number in the save.

Audit current technology and doctrine behavior with the required technology tools when any graph-adjacent surface is considered.

## Population and shared ledgers

Create the Event 46-owned absolute state-population rewrite contract for increases and decreases.

Do not use a Deaths-oriented helper as a false substitute.

Population rewrite must not record Deaths, births, famine, migration, or death-generated Chaos.

Reconcile engine-created recruitable-manpower effects so the reserve-manpower family remains separate.

Protect Chaos, Deaths, Air Cleanliness, Condemnation, famine and migration ledgers, camps and evidence, world threat, event weights and timers, histories, enable state, evolutions, clusters, scenarios, Event Log arrays, world-end state, super-event state, stable IDs, object identities, provider registries, settings, debug state, and achievements.

Produce a write-path audit.

## Evolution and World Collapse behavior

Evolutions I through IV use normal evolution pacing and can activate before the first Event 46 firing.

Evolution activation adds zero Chaos.

Disabled evolutions cannot record or unlock content.

Evolution V activates immediately at 1000+.

Inspect the live World Collapse freeze order.

Use normal selection when events remain active until terminal commitment.

Otherwise implement the one bounded enabled pre-freeze Event 46 opportunity from Part 1.

It must consume one normal repeatable firing, never reopen other events, never bypass an existing terminal state, and never run twice.

## Weighted logic

Use the exact scenarios in `matrices/046_probability_scenario_matrix.md`.

Run `chaosx_ai_probability_auditor` before any weight patch.

The auditor starts with `hoi4.probability_inspect` and uses evaluation, sweep, simulation, sequence, comparison, and rendering only under the declared evidence conditions.

The owner chooses balance targets and applies patches.

Run `hoi4.probability_compare` afterward on the same scenarios.

Prove coverage monotonicity, quota termination, no starvation, Evolution V saturation, repeated independence, evolution pacing, cluster non-duplication, and direct Chaos compression.

## Chaos accounting

Add one direct Event 46 Chaos history entry per successful transaction using the accepted capability bands and actual committed disruption.

First manifestation can receive its one-time premium inside the cap.

Evolution state gives zero.

Suppress generic Chaos or ledger hooks caused only by Event 46 setters so ruling-ideology, population, and structural results do not double count.

Later real wars, deaths, peace, and other consequences remain normal shared sources.

Event 46 has no direct negative Chaos reversal.

## Report, AI, and multiplayer

Use a standard report event and shared Event Details.

Do not build a decision category, persistent meter, custom GUI, focus tree, or super-event.

Every human gets one concise personalized report from the same global transaction.

AI receives no protection and no compensation.

Owner reconciliation can refresh AI legality but cannot improve a bad result.

Use family-normalized report importance, exact before and after values, grouped high-tier sections, and omitted counts.

Do not expose registry internals.

One transaction creates one Event Log entry.

Multiplayer clients do not reroll locally.

## Clusters and catalog

Create the Randomizations cluster relationship with Event 46 as Medium and prevent one-member duplicate firing.

Create Domestic Unrest with Event 1 Medium, Event 21 Low, and Event 31 Medium.

Keep Event 21 in Wars.

Support multiple cluster relationships without overwriting relationship-specific severity.

Verify Event 2 remains Severe in Diseases.

Resolve Alien Invasions and Event 43 against the authoritative repo before changing them.

Do not infer a cluster ID from the missing numeric value in the export.

Update only `docs/spreadsheets/chaos_redux_events_catalog.xlsx` through the spreadsheet worker, then run the exporter.

Never edit the CSVs directly.

Use Needs Testing after source completion unless the user explicitly approves Playable.

## Assets, achievements, and text

Implement all six achievements and their protected tracking from the achievement prompt.

Produce the one report image and six achievement icon packages through the correct asset subagents and asset prompt.

Do not use placeholders or create unrequested visual families.

Write final in-world localisation from the localisation prompt and run `chaosx_localisation_auditor`.

Keep Event Details, Event Log, evolution text, cluster text, achievement text, docs, and workbook wording aligned.

Create or update `docs/events/046_the_great_shuffle.md` and clearly distinguish implemented core families from blocked conditional families.

## Completion passes

After a meaningful implementation tranche, use the improvement loop only when a real depth gap remains.

Near completion, spawn `chaosx_improvement_loop_planner` with `fork_turns="none"` and the full current status.

Implement, promote, queue with a reason, or reject its output before another pass.

Run the event completion auditor, localisation auditor, probability auditor, asset review, protected-state audit, acceptance matrix, and documentation alignment.

Do not invoke autonomous live desktop testing unless the user explicitly invokes that separate skill.

The user owns live in-game validation.

Provide a concrete completion report with changed files, family coverage, blocked conditional families, transaction and recovery evidence, probability comparisons, cluster and catalog changes, achievements, assets, documentation, meaningful validation, and every simplification or blocker.

No fallback, partial substitute, hidden omission, or completion claim is allowed.
