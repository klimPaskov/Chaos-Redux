# Coding-agent prompt: Event 061 Return to Peacetime

Implement the complete Event 61 rework from `docs/specs/061_return_to_peacetime_specs/`.

Treat every mapped rule, route, decision family, evolution, law, asset, achievement, Event Logs surface, cluster update, AI behavior, documentation task, and anti-exploit rule as acceptance criteria.

Do not replace the specification with a smaller one-click event.

## Mandatory reading

Before editing:

1. Read repository `AGENTS.md` in full.
2. Read every file under `docs/specs/061_return_to_peacetime_specs/`.
3. Read the current Event 61 implementation, registration, names, logs, cluster references, docs, and catalog row.
4. Read the event, decisions and missions, event assets, improvement loop, subagents, and achievement rules.
5. Inspect relevant offline Paradox wiki pages and installed Hearts of Iron IV documentation.
6. Inspect vanilla and Chaos Redux precedents for law definitions, adjacent law movement, state building conversion, decision state targets, timed missions, safe scripted division disband, equipment stockpile debits, event scheduling, Event Logs, cluster members, and achievements.
7. Inspect `chaosx_dynamic_effects.md` and `chaosx_dynamic_triggers.md` before adding shared helpers.
8. Inspect the authoritative event workbook. Do not edit CSV exports directly.

Record the local references used.

If a required local reference or MCP route is unavailable, record the exact blocker. Do not guess engine behavior for factory conversion, law definitions, or unit disband.

## Repository exploration and architecture

Spawn `chaosx_repo_explorer` with `fork_context=false` when current Event 61 file locations or cross-file ownership are uncertain.

Spawn `chaosx_scripted_system_architect` before duplicating law-rank, atomic factory conversion, stockpile debit, or safe-disband logic.

Use event-owned files for Event 61 orchestration and state. Promote only neutral reusable helpers to shared registries, then document those helpers in the correct source.

Preserve unrelated user changes. Do not reset or clean the repository.

## Canonical event behavior

Keep `chaosx.nr61.1` as the canonical entry.

Keep Event 61 as Minor Repeatable, Chaos level 1, and the High member of the Peace cluster.

One firing affects every country that uses normal civilian systems.

For each valid country:

- convert `floor(eligible military factories / 2)` physical military factory levels into civilian factory levels
- use only states owned and controlled by the country
- record every conversion in a persistent state-level ledger
- remove half of current War Support and add the same amount to Stability, subject to the Stability ceiling
- move economy law one valid step toward Civilian Economy
- move conscription law one valid step toward Disarmed Nation
- rely on the ordinary law model for released recruitable population
- apply or refresh one staged Industrial Reconversion Shock
- open or refresh Return to Rearmament

The state ledger is authoritative and follows state ownership.

Reopening one factory must consume one civilian factory and one positive ledger unit in the same validated transaction.

New construction, annexation, focus rewards, and unrelated events must not create ledger units.

## Law model

Implement explicit validated rank helpers.

Economy order:

Peacetime Economy, Civilian Economy, Early Mobilization, Partial Mobilization, War Economy, Total Mobilization.

Conscription order:

No Army, Disarmed Nation, Volunteer Only, Limited Conscription, Extensive Conscription, Service by Requirement, All Adults Serve, Scraping the Barrel.

The baseline floors are Civilian Economy and Disarmed Nation.

Evolution III alone can force the new rank-zero laws.

Record the highest unresolved ordinary rank that Event 61 removed. Return to Rearmament can restore only toward that target.

External changes such as Event 82 count. Recheck current law at decision completion so the same rank cannot be granted twice.

## Return to Rearmament

Use one ordinary decision category with one public numeric value, Rearmament Readiness from 0 to 100.

Calculate it from five hidden pillars:

- Event 61 industrial capacity restored
- current economy law
- current conscription law
- contracts and defence institutions
- War Support and material preparation

Show qualitative pillar states, not five additional raw meters.

Meaningful rearmament requires Readiness 50 and at least one restored factory, economy-law step, or conscription step.

Keep the category to five primary actions and one active mission at most.

Implement the complete phased decision family from Part 2, including:

- Restart Arms Contracts
- up to three targeted Reopen State Arms Plants actions
- Reconstitute the General Staff
- Make the Case for Defence
- Restore Mobilisation Law
- Restore Conscription
- Emergency Rearmament
- Make the Conversion Permanent
- National Rearmament Program
- extreme-law recovery through Defence Ministry, National Arsenal, Service Registry, and Emergency National Defence

Use the universal cost framework.

Use real civilian factory commitments, political power, army experience, Stability, time, and valid requirements.

Do not turn the category into political power purchases.

Ensure the first extreme-law exit steps do not require army experience or recruitable manpower.

Spawn `chaosx_decision_mission_auditor` after the category and missions work as a complete playable system.

## Industrial Reconversion Shock

Implement one staged lifecycle spirit.

Starting target:

- 90 days severe
- 90 days disrupted
- 90 days easing

Use the modifier directions and starting values from Part 1.

A repeat firing returns the country to the severe phase and extends remaining duration within the 540-day cap.

Do not stack copies.

High Readiness can mitigate part of the later penalty after the first 90 days, but it cannot erase the transition immediately.

## Evolution I

At Chaos 200+, follow the shared evolution activation and enable system.

Schedule a visible Inventory Liquidation mission after the baseline delay.

At resolution:

- calculate current positive surplus by supported conventional family
- apply dynamic reserve floors
- prioritize captured and obsolete equipment when the engine supports exact variant selection
- exclude deployed need, ships, nuclear and missile assets, special projects, unknown special equipment, and every family without a safe debit
- use exact positive stockpile debit helpers
- remove a starting base of 25 percent of eligible surplus, dynamically 10 to 35 percent
- apply Readiness, threat, protection, and merged-cycle factors
- offer at most three relevant protection decisions
- convert actual removed value into capped Reconstruction Materials tiers
- support Central Reconstruction and Civilian Auctions with a complete DLC-safe base

Do not reward requested amounts. Reward actual successful debits.

Do not show one popup per equipment type.

## Evolution II

At Chaos 400+, schedule Mustering Out with a 60-day target warning.

Build an eligible conventional division pool.

Exclude every unsafe, foreign, combat, transported, locked, civil-war-owned, or special owner-protected unit.

Apply candidate scoring, tiny-army caps, Readiness mitigation, war protection, cadre retention, and threatened-border protection.

Use a verified native or project-supported safe disband route that returns manpower and equipment.

A destructive unit-deletion effect is unacceptable.

Calculate Veteran Reintegration from actual successful disbands and actual returned scale.

Block one-battalion template farming through unit age and actual manpower or equipment value.

## Evolution III

At Chaos 600+, introduce Peacetime Economy and No Army through the verified law database pattern.

Start a 90-day National Defence Settlement.

Immediate exemption:

- Readiness at least 50
- meaningful structural proof

Last-chance exemption for countries not prepared at settlement start:

- Readiness at least 60
- at least two distinct structural action families
- at least one factory or law action

Countries under direct war danger receive a bounded deferral and postwar review.

Non-exempt countries:

- enter Peacetime Economy
- convert `floor(remaining eligible military factories / 3)` through the same ledgered transaction
- enter No Army
- safely disband remaining eligible conventional divisions after a final warning
- receive bounded Peace Dividend
- retain a difficult but functional recovery route

Guard the first-entry effects per cycle.

Do not attach a daily destructive loop directly to the laws.

## Evolution pacing and repeat merge

Use one event-owned scheduler.

Schedule only the next enabled unresolved evolution.

A disabled earlier evolution must not block a later enabled one.

An evolution that activates while a country transition is active must schedule without requiring a new baseline firing.

A repeat firing while an evolved mission is active must keep one visible mission, add bounded pending-cycle pressure, preserve the minimum response window, and resolve once at the capped combined intensity.

Persist every cycle and resolution guard through save and reload.

## AI

Implement the three AI stances from Part 4:

- Reconstruction Pacifist, target Readiness 0 to 30
- Cautious Hedge, target Readiness 50 to 70
- Wartime Rearmament, target Readiness 80 to 100

Direct danger overrides ideology.

Majors and faction leaders usually preserve a mobilisation skeleton.

Subjects use their own state, with overlord preference modified by autonomy and overridden by direct local threat.

Voluntary Permanent Peace requires every hard safety gate and is impossible during active war, enemy preparation, occupied cores, faction leadership, Event 59 aggressive strategy, or direct invasion risk.

Spawn `chaosx_ai_probability_auditor` for every complex `ai_will_do`, option chance, weighted target pool, and random selection.

Run all scenarios in `research/061_return_to_peacetime_ai_probability_scenarios.md` through the HOI4 probability tools.

Source-only review does not satisfy this gate.

## Cross-event and cluster work

Implement all integration rules in Part 4.

At minimum:

- Event 9 White Peace resolves before Event 61 inside the Peace cluster
- correct Cluster 4 member list from `9, 9` to `9, 61` in the authoritative workbook and repository registry
- Event 82 law steps update Readiness and cannot be duplicated
- Event 94 forces Evolution I to recalculate current surplus
- Event 59 strongly shifts AI toward rearmament
- Event 103 can reuse law helpers in a future rework
- Event 124 must not duplicate Event 61 factory or law mechanics
- Event 131 units are excluded until their owner resolves them
- Event 148 changes preference only when safe

Cluster execution counts as one pacing event while member histories and repeat states remain separate.

## Chaos accounting

Do not add Event 61 owned Chaos changes for baseline effects, evolutions, demobilization, rearmament, law adoption, stockpile disposal, or civilian benefits.

Evolution activation remains zero.

Use only the shared Minor Event firing contribution and any generic peace result owned by Event 9 or the shared system.

## Assets and localisation

Create every asset in the requirement matrix.

Use `chaosx_generated_event_art` for report and category art.

Use `chaosx_icon_artist` for category, decision, idea, law, and achievement icons.

Use `chaos-redux-event-assets` for references, processing, DDS, manifests, and handoffs.

The main agent owns final GFX wiring.

Write final in-world localisation from the direction in Part 6.

Do not paste working labels or prompt text into the game.

After broad visible text exists, spawn `chaosx_localisation_auditor`.

## Achievements

Implement all three achievements from Part 6 in the single Chaos Redux achievement registry:

- The Arsenal Returns
- Swords, Ploughshares, Swords
- The Arsenal Sleeps

Implement persistent tracking, timing, disqualifiers, tag continuity, ownership changes, icons, localisation, docs, and live test cases.

Do not weaken hard achievements into automatic unlocks.

## Event Logs and documentation

Wire:

- event name and debug name
- one global history row per firing
- aggregate result variables
- three evolution catalog entries
- correct evolution history records
- Event Details row
- Peace cluster detail and member navigation

Update event docs, system docs, law docs, achievement docs, asset records, and the authoritative workbook.

Regenerate CSV exports with the repository exporter.

Spawn `chaosx_documentation_curator` and `chaosx_spreadsheet_doc_worker` after implementation facts are stable.

## Performance and cleanup

Use one all-country pass only when the event fires.

Use bounded owned-state, stockpile-family, and division passes at their specific resolution times.

Use a recursively scheduled 30-day country event only for countries with active Event 61 state.

Do not add a permanent daily, weekly, or monthly whole-world scan.

Stop the pulse when no ledger, law target, spirit, mission, extreme law, or deferred settlement remains.

## Mandatory near-completion loop

After a meaningful implementation tranche, spawn `chaosx_improvement_loop_planner` once.

Resolve every returned item by implementing it, folding it into the source spec, queuing it with a reason, or rejecting it with a reason.

Then run `chaosx_event_completion_auditor`.

Do not claim completion while a required asset, probability result, law validation, safe-disband proof, documentation update, workbook update, or acceptance scenario remains blocked.

## Required completion report

Report:

- files changed
- event chain and identifiers
- baseline transaction evidence
- state ledger tests
- law-rank tests
- decision and mission coverage
- evolution coverage
- AI probability evidence
- cluster correction
- cross-event integrations
- Chaos accounting
- assets and localisation status
- achievement status
- docs and workbook status
- save and reload tests
- performance checks
- subagent handoffs
- simplifications, fallbacks, blockers, and unresolved items

Include a spec coverage table with one row for every acceptance criterion.
