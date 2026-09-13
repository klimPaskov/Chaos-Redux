# Coding Prompt for Event 052 Intel Leaked

Implement the complete Chaos Redux Event 052 rework from `docs/specs/052_intel_leaked_specs/`.

Read every specification part, matrix, handoff, specialist prompt, research note, acceptance criterion, `AGENTS.md`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-improvement-loop`, and `chaos-redux-subagents` before editing.

Consult the required offline Paradox wiki pages, installed Hearts of Iron IV documentation, vanilla precedents, and existing Chaos Redux patterns for every engine surface touched. Use the mandatory HOI4 MCP event and probability workflows.

## Core implementation

Preserve Event ID 52, namespace `chaosx.nr52`, Minor Repeatable classification, Chaos level 1, Intelligence cluster membership, and Low member severity.

Replace the legacy permanent maximum-intelligence grant with a temporary, reversible, event-owned exposure system.

Baseline firing must select exactly one target through the accepted player-country or valid-major routes. Deep Files and Total Compromise must follow their separate thresholds, pacing, pre-fire openings, mid-incident escalation, evolution logging, enable controls, and cleanup.

Implement one public value, Exposure. Keep archive depth, confidence, recipient Reliance, operative risk, pair scores, and selection arithmetic hidden.

Create fresh incident state for every firing. Prevent ordinary overlap. Total Compromise owns several targets inside one sequence, with separate Exposure, domains, exploiters, missions, decisions, deception, and cleanup for each target.

## Intelligence and exploitation

Every ordinary foreign government must receive meaningful temporary intelligence against the target while Exposure remains positive. Scale the advantage by Exposure and active archive domains. Track or own every applied effect so cleanup removes it exactly.

Select a bounded group of named exploiters through hostility, war state, geography, claims, capability, agency strength, domain relevance, and current plans. Implement every exploitation family from the specification and keep outcome strength bounded by recipient use and target delay.

Implement agency and operative depth when available. Preserve the complete base-game path. Limit severe personnel outcomes per target and tranche.

## Decisions, missions, and deception

Implement the full phased action and mission map through the separate decision and mission prompt.

Use varied dynamic costs and real sacrifices. Respect the four-cost hard limit and the category action cap. Add AI equivalents, custom blocked tooltips, texticons, target validation, cooldowns, save-safe state, and complete cleanup.

Implement Poison the Leak through recipient Reliance and matching domain use. Support success, partial success, and failure. Stage false deployments through real unit, fleet, air, fuel, transport, or operational commitments where mapped. Do not apply blanket deception penalties to governments that did not rely on the archive.

Implement Trace the Source with practical route classes and no final culprit.

## Evolutions and Chaos

Deep Files requires 400 Chaos. Total Compromise requires 800 Chaos. Use paced evolution activation, one shared log entry per evolution, and zero Chaos from evolution state alone.

Implement the complete Chaos impact map. Commit each manifestation, deep tranche, added target, severe personnel consequence, and active neutralization only through its bounded one-shot proof. Do not double count generic war, tension, death, annexation, ideology, or military-buildup sources.

## Cluster and cross-event integration

Add Event 52 to Intelligence cluster 10 as a Low member. Preserve one cluster pacing transaction and member-specific history and repeatable handling. Implement same-target Event 039 interaction only through stable public adapters and bounded evidence or personnel effects.

Expose the Event 52 public helper contract needed by Event 011 and future systems. Add the bounded Event 011 Evidence and Pact Readiness hooks when its current public adapter supports them. Keep unavailable catalog events optional and nonblocking.

## Event system, presentation, and assets

Complete event registration, eligibility, manual firing, default-enabled state at finished rework, actor mapping, Event Details, event-name selectors, debug-name selectors, history, evolution previews, cluster rows, and multi-target actor presentation.

Write final player-facing event, news, decision, mission, tooltip, achievement, Event Details, scripted-localisation, and catalog wording from the direction files. Do not paste process notes or working labels blindly.

Use the asset prompt. Hydrate and audit the existing Event 52 LFS assets before replacement. Produce every authorized event image, category asset, decision icon, status icon with a real consumer, and achievement icon triplet. Keep static presentation readable and avoid unapproved placeholders.

Implement the four mapped achievements with unique-sequence, unique-recipient, capital-control, personnel-safety, debug-disqualifier, and cleanup-safe tracking.

## Documentation and catalog

Create or update the permanent Event 52 documentation under the established `docs/events/` pattern.

Update only `docs/spreadsheets/chaos_redux_events_catalog.xlsx`. Align Event 52 and Intelligence cluster 10 with final in-game wording, then run `python .tools/export_event_catalog_csv.py`. Never edit the CSV exports directly.

## Mandatory evidence and audits

Use `hoi4.event_inspect` before rewriting the chain. Use `hoi4.event_render` for target selection, baseline flow, evolutions, cluster path, deception, invalidation, and cleanup. Use `hoi4.event_compare` after implementation.

For every weighted surface, spawn `chaosx_ai_probability_auditor` with a self-contained prompt and `fork_context=false`. Start with `hoi4.probability_inspect`, run the named evaluations and sweeps, then compare the final patch against the baseline scenarios.

Run the decision and mission audit, localisation audit, asset review, and Event 52 completion audit. Spawn `chaosx_improvement_loop_planner` near completion. Implement or fold in its accepted addendum, queue it with a reason, reject it with a reason, or use its closure handoff. Do not stack another improvement pass while one remains unresolved.

Keep iterating until every mapped surface is implemented to its fullest extent. Do not use unapproved fallbacks, silent simplifications, temporary substitutes, or good-enough approximations. Do not claim completion until the final repository state satisfies the full specification and the completion report lists files changed, systems touched, task-specific evidence, assets, documentation, catalog alignment, audits, unresolved blockers, and every simplification.
