# Event 82 full implementation prompt

Implement Law Upgrade from `docs/specs/082_law_upgrade_specs/` to its fullest extent. Read all ten numbered parts and every companion handoff before writing gameplay code. Preserve the user's fixed requirements and the specification's stated distinctions between those requirements, proposed balance, source observations, and unresolved evidence.

This is a full rework, not a text update to the old economy-only popup.

## Required reading and verification

Read current AGENTS, the event-planning, events, decisions/missions, event-assets, MTTH, subagents, improvement-loop, debug/playtest, and other genuinely relevant skills. Read every must-read source they name for the systems you touch, including current installed-game documentation and complete relevant offline wiki pages. Do not substitute memory, this package's summaries, or archive-completion claims for that external reading.

The research file identifies what this planning session did and did not inspect. The inspected repository revision is `879b3007d3b6bf75c726c11635473fccda45c569`, not an assertion about your current worktree. Reconcile against the actual worktree before editing.

Inspect the real economy, manpower, and trade definitions, all loaded eligible country/DLC policy owners, existing effect helpers, cost framework and detailed contracts, dynamic modifier consumers, evolution framework, central dispatch, achievement owner, and catalog workbook/exporter.

The supplemental `docs/plans/082_law_upgrade_plans/` package provides source coverage, same-author review, reference tests, and isolated role handoffs. None is a completed independent or live-game review.

## Fixed gameplay requirements

Event 82 remains Law Upgrade, Minor Repeatable, Chaos level 1, Military Preparation Low member. Preserve `chaosx.nr82.1` and `chaosx.nr82.2` unless an explicit verified migration requires another public arrangement.

One worldwide firing advances every participating country and compatible category by one adjacent step from a consistent snapshot. It grants support once before evaluating resulting penalties. Use +10/+25/+50/+50 percentage points for baseline/I/II/III. Never add earlier profile awards together.

Economy progresses toward Total Mobilization and conscription toward Scraping the Barrel. At I, Chaos 200+, add trade toward Closed Economy and the defined registered wartime families. At II, Chaos 600+, include every remaining compatible wartime family. At III, Chaos 800+, append Totalen Krieg!!! and Totalen Menschen!!! beyond the ordinary maxima. A country below a cap does not jump to an extreme.

Implement the complete evolution lifecycle from Part 3: shared dynamic pacing after eligibility for an existing lifecycle, highest eligible enabled opening for an unfired event, latched activated history, cumulative settings dependencies, and zero law/support/Chaos reward merely for activation.

## Dispatch and one-step ownership

Move compulsory effects out of the notification option. Preflight and snapshot the world firing, then apply support and exact single steps, reconcile effects, and present the already-completed result.

Use central firing identity and idempotency rather than the current date as the unique key. Two distinct legitimate same-day selections remain two waves. Duplicate delivery of one ticket remains one wave.

Resolve each real category once. Preserve unknown laws and structural prerequisites, while bypassing ordinary political purchase gates for a forced step. Do not instantiate absent institutions, buy technologies, manufacture manpower, or choose arbitrary sidegrades.

The legacy `upgrade_economy_law` cap behavior can award PP and the helper has other callers. Inspect the actual loaded helper. Do not reuse its cap reward or alter unrelated callers as a shortcut.

Implement the owner-maintained progression contract and coverage matrix. The engine has no assumed reflective API for arbitrary law names. Use real supported fixed dispatch or verified generated integration with one owner source of truth, not duplicated Event 82 sequences.

## Extreme laws and effect ownership

Implement the two actual laws in the existing economy and conscription categories. Replace the former law's complete payload. Do not stack hidden leftovers from Total Mobilization or Scraping the Barrel.

The economy law must represent the intended 99% commitment through its verified 1% law-level civilian-consumption baseline. Distinguish actual country results from the legal allocation and do not mutate a global consumer-goods floor.

The conscription law must use an actual 99% legal setting and preserve eligible-population permissions, ordinary mobilization, real casualties, and the ceiling under other recruitment effects. No one-time `add_manpower` substitute is allowed.

Implement Parts 4–6 exactly as the initial balance target. Combine only the two laws' own overlapping capacity factors multiplicatively in one owned aggregate contribution, then leave unrelated native modifiers intact. Do not add +100% and -80% and call it the specified 40% remaining factor.

Apply ongoing current-support scaling, not entry-time tiers. Refresh immediately for the firing and within one game day for later relevant support/law/war changes through existing owner lifecycle or bounded holder mechanisms. No new global daily/weekly polling pass is authorized.

Use actual supported dynamic modifier and law machinery. Validate refresh, history initialization, civil-war inheritance, external removal, tag changes, save/load, and effect cleanup. Do not apply recurring instant Stability or population losses.

Keep the public value budget to law positions and native War Support. Do not add a new player-managed meter or redundant spirit row.

## Exact manual reversal transactions

Implement one small native decision category with two authoritative manual actions. The economy action restores Total Mobilization. The conscription action restores Scraping the Barrel.

Prevent direct native manual selection from bypassing the adjacent reversal or its price. Scripted external removals remain possible under their owners. Do not charge all removals through a generic on-remove fee.

Quote the current ordinary adjacent-law cost using a verified owner provider, including ordinary modifiers, applicable active discounts, and normal rounding. Then double that resolved amount. If the ordinary result is 113, charge 226. If it is zero, charge zero. Do not hardcode 300 or discount the result a second time.

Display the accepted current quote, recompute and check full affordability at confirmation, debit once, change the law once, and record the real result. No partial debit, invisible extra fee, stale discount, multi-step shortcut, or failed purchase that still changes the law.

Use the shared cost framework only through an exact provider. Its bounded coverage is not proof that all native law prices are accessible. Missing exact price access is a blocker to solve, not permission for a fallback.

Human and AI prices and outcomes are identical. No added cooldown, duration, support gate, peace gate, or extra resource fee applies to reversal. Voluntary entry uses ordinary price, immediate predecessor, active enabled III, war, and at least 80% support.

## World systems, Chaos, and persistence

Implement the complete Part 7 impact map: four globally one-shot +5 outcome milestones, two possible -5 durable-recovery milestones, 30-day no-holder recovery conditions, and all anti-farming guards. Evolution state, capped no-ops, reload, re-entry, and multiple same-wave holders cannot duplicate credits.

Do not double count generic wars, annexations, deaths, or contamination. Other crises remain with their owners. Do not create automatic famine, migration, new units, military stockpiles, country tags, or new focus content.

Disabling future firings must not orphan existing law effects or exits. Reconcile annexation, civil wars, player identity changes, and old saves. Specifically test pending legacy notification behavior without replaying the new global wave.

## AI and probability work

Implement Part 8 and the separate scenario contract, including actual shortages, marginal recovery with both laws, current affordability, Political Power reservation, and consistent voluntary-entry/exit reasoning.

Spawn `chaosx_ai_probability_auditor` with a fully self-contained prompt and `fork_turns="none"`. It must start with `hoi4.probability_inspect`, then use evaluate, sweep, simulate, compare, and render as required. Use the actual candidate pool and verified game-version MTTH adapter. Never present a weight as a percentage or a nominal MTTH as a deadline.

If a required probability tool or source is unavailable, record the precise blocker and preserve unverified status. Do not claim its results based on the supplied arithmetic model.

## Presentation, final writing, assets, achievements

Write final player-facing reports, acknowledgments, law descriptions, reversal labels, tooltips, achievement text, evolution text, event Details, and catalog-facing prose from the direction-only specification. Keep fixed law names unchanged. Current mechanics and prices must agree with visible text.

Implement the 17-image asset package through the separate asset prompt, with actual processors, provenance, final sprite wiring, and native-size inspection. No custom scripted window, super-event, animation, portrait, model, new country, or focus tree is specified.

Implement all three achievements through `common/achievements/chaos_redux_achievements.txt` and the existing canonical tracking and award systems. Follow the achievement prompt's complete conditions, disqualifiers, history, visibility, and nine image states.

## File ownership and integration

Keep the public event owner in `events/082_law_upgrade.txt`. Add or update bounded Event 82-owned effects, triggers, constants, laws, dynamic effects, decisions, and localization only in the project's appropriate existing locations. Verify load order before using slot-cost modifiers.

Shared law progression belongs with a genuinely reusable owner contract. Event 82 lifecycle, outcome records, and its two special laws remain Event 82-owned. Do not build an unrelated generic framework that the event does not need.

Use the canonical shared evolution, selection, Chaos History, Event Log, achievements, costs, and settings systems. Implement all actual mapped variants and no unrequested country or technology content. Research-speed modifiers do not authorize grants or a new technology tree.

Update the authoritative workbook's Event 82 and Military Preparation relationship and regenerate exports with the established `.tools/export_event_catalog_csv.py` workflow after inspecting it. The supplied CSVs are read-only exports. A missing workbook remains a documentation blocker.

## Review and completion

Use the 80-case acceptance matrix, all provider fixtures, support endpoints and combined effects, native economics and population accounting, prices with discounts and rounding, settings, multiplayer, inheritance, migration, achievements, and actual visual consumers.

Do not launch HOI4 without explicit user authorization. Build additive, idempotent fixtures using the current project's testing conventions and request user-controlled live evidence when necessary. Static parsing and Python arithmetic do not replace engine checks.

Before claiming the goal is near complete, spawn `chaosx_improvement_loop_planner` using `fork_turns="none"` with all inputs explicitly listed. Resolve its addendum or closure handoff. Route bounded systems and decision reviews to the supplied specialists and obtain a completion audit.

Keep iterating until the full specification is accomplished to its fullest extent. Avoid undisclosed simplifications, temporary versions, broad fallback paths, and good-enough substitutes. Report unresolved exact engine or source access honestly. Do not claim completion until the implemented files satisfy the specification.

Provide a final report of changed files, source and build context, all mapped systems, actual tests and evidence, asset manifests, workbook/export changes, independent-review dispositions, and remaining blockers. Separate implemented, source-verified, arithmetic-checked, and live-validated claims.
