# Coding Prompt for Event 55

Implement Chaos Redux Event 55, The Great Infrastructure Project, from the complete source specification pack.

Read every file under `docs/specs/055_the_great_infrastructure_project_specs/`, then follow `AGENTS.md`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-improvement-loop`, and `chaos-redux-subagents`. Consult all required offline Paradox wiki pages, installed vanilla documentation, vanilla precedents, and existing Chaos Redux patterns before editing.

## Core implementation

Keep canonical entry event `chaosx.nr55.1`. Register Event 55 as Minor Repeatable, Chaos level `1`, Positive Economy cluster ID `7`, Medium member.

On a country's first firing, set the constructed infrastructure level of every state it owns at that moment to the engine maximum. Do not turn this into a smaller modifier. Do not apply the grant to future conquests. Do not apply it twice to the same recipient.

Create the persistent Event 55 national works program with one public National Works Capacity value, stable geographic proposals, active project limits, staged project missions, persistent completed project records, route status, repair, rerouting, renegotiation, transfer, and cleanup.

## Required project families

Implement every family in the source specs:

- continental railway
- continental highway
- international trade corridor
- underwater tunnel
- great bridge
- grand port
- resource corridor
- Evolution III continental networks

Use real route states, ports, resources, partners, railways, supply nodes, and validated crossings. Highways must provide route-specific effects above ordinary maximum infrastructure. Fixed links may appear only from a curated registry with map and engine proof. Never substitute a cosmetic modifier for a promised movement and supply connection.

## Decisions and missions

Follow the separate decision and mission prompt. Use one ordinary decision category with a static category picture and compact status header. Do not create a dedicated scripted GUI.

Keep visible action and mission budgets. Use staged costs with no more than four spendable cost types per action. Use concrete transport equipment, fuel, civilian burden, political agreements, and route requirements. Do not use political power as the generic answer to every project action.

## Persistent architecture

Use event-owned script constants, triggers, effects, records, and adapters. Suggested owner files include:

- `events/055_the_great_infrastructure_project.txt`
- `common/decisions/055_the_great_infrastructure_project_decisions.txt`
- `common/decisions/categories/055_the_great_infrastructure_project_categories.txt`
- `common/script_constants/055_the_great_infrastructure_project_constants.txt`
- `common/scripted_triggers/055_the_great_infrastructure_project_triggers.txt`
- `common/scripted_effects/055_the_great_infrastructure_project_effects.txt`
- `common/dynamic_modifiers/055_the_great_infrastructure_project_dynamic_modifiers.txt`
- `common/ideas/055_the_great_infrastructure_project_ideas.txt`
- event-owned on-actions only when sparse registered processing requires them
- event-owned scripted localisation and English localisation files

Use the exact current repository structure when it differs from these suggested paths.

Do not put Event 55 lifecycle checks into shared country classifiers. Reuse existing neutral stockpile debit helpers. Add a shared dynamic helper only when its contract is genuinely neutral across unrelated systems, then document it in the shared registry in the same change.

Use persistent generation identities for proposals, projects, partner invitations, receipts, routes, and transfers. Delayed responses must fail closed when stale. Cleanup must be idempotent.

Do not add a whole-world daily, weekly, or monthly scan. Use sparse registered recipients, bounded critical-node records, and event-driven refresh.

## Evolutions

Implement:

- Evolution I at `200+`, Infrastructure Mania
- Evolution II at `400+`, Engineering Without Limits
- Evolution III at `600+`, The World Connected

Evolution activation changes no Chaos. Use the shared paced evolution contract. Disabled evolutions must set no recorded or unlock flags. Wire every evolution into Event Logs, Event Details, candidate access, AI, decisions, assets, docs, and catalog wording.

## Repeat firing

Prefer countries that have never received Event 55. Apply a long recent-target cooldown. Existing recipients remain eligible for bounded assistance based on current state, including repair support, construction breakthrough, survey renewal, international opening, or maintenance renewal. Never repeat the opening infrastructure grant.

## Integrations

Implement versioned, proof-carrying adapters with clear ownership boundaries:

- Event 18 can seed a same-actor Resource Corridor proposal.
- Famine can consume operational relief-route facts.
- Migration can consume route and reception capacity facts.
- Natural disasters, bombing, combat, and sabotage can damage registered project nodes.
- Great Embargo can suspend international benefits and increase procurement pressure.

Do not edit another system's primary ledger through Event 55.

Ordinary Event 55 outcomes add zero direct Chaos. Do not double count war, annexation, death, disaster, contamination, or embargo sources. Implement the optional one-time `-2` cooperation reversal only if the shared Chaos audit confirms no overlap.

## AI and weighted logic

Implement the full AI strategy from the specs. AI must be able to use every human project action, refuse unsafe projects, negotiate, repair, reroute, reduce scope, and abandon permanently invalid work.

Run the separate probability audit prompt. Every weighted patch requires baseline inspection, owner-applied change, and comparison against the same named scenarios.

## Maps and MCP

Use the HOI4 MCP event tools for the event chain and the map tools for every fixed crossing. Inspect and compare before and after source changes. A missing map route blocks that crossing. Source-only confidence is not equivalent to map evidence.

## Assets and achievements

Complete the separate asset and achievement prompts. Wire every required report image, news image, category asset, idea icon, decision icon, mission icon, modifier icon, and achievement icon triplet. No placeholder, primitive drawing, resized unrelated icon, or unwired asset may remain.

## Writing and documentation

Write final player-facing localisation from the direction in the source specs. Do not paste working labels without review. Remove developer, debug, cap, tuning, rework, and update-history wording. Use dynamic geography and partner names. Keep costs icon-first and requirements concise.

Wire event registration, event type, default enable state when ready, name mappings, actor mappings, History, Event Details, Evolutions, and cluster history in the same implementation.

Create or update the Event 55 event documentation. Use the separate catalog update prompt and authoritative workbook workflow after final localisation exists.

## Required review sequence

- event chain MCP inspect, render, and compare
- decision and mission audit
- baseline and comparison probability audit
- map inspect and compare for every crossing
- localisation audit
- asset audit
- achievement audit
- improvement loop near completion
- documentation and catalog alignment
- event completion audit

Resolve every accepted addendum or report why it is queued or rejected. Do not claim completion while any mapped mechanic, asset, AI path, adapter, achievement, log surface, documentation field, or validated crossing remains missing.
