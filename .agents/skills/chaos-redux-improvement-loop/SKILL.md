---
name: chaos-redux-improvement-loop
description: Use when recursively deepening Chaos Redux mechanics, events, focus trees, countries, decisions, assets, lore, super-events, and implementation audits into concrete expansion specs and improvement handoffs.
---

# Chaos Redux Improvement Loop

Use this skill when a Chaos Redux feature is functional but may need more depth, cohesion, variation, visual progression, lore clarity, AI behavior, or meaningful gameplay.

This is an active implementation loop. It is not only an end-of-task audit.

## 1. Core purpose

Chaos Redux systems should not stop at the first working implementation.

A feature should be inspected and, when needed, expanded for:

- shallow mechanics
- duplicate content
- repeated rewards
- missing player choices
- missing AI behavior
- weak or unreadable lore
- static visuals that should evolve
- missing event log, evolution, cluster, or detail support
- decisions that are passive buttons
- focus trees that are long reward lists
- countries that exist only as tags
- super-events that have only one finished surface
- docs, spreadsheet rows, or manifests that describe intent instead of implemented state

The goal is not endless scope creep. The goal is to create concrete addenda that make a mechanic more playable, clearer, more reactive, more readable, more visually coherent, or better integrated with existing systems.

## 2. When to use this skill

Use this skill:

- during implementation checkpoints for large events, mechanics, countries, focus trees, decisions, super-events, or asset systems
- when an audit subagent inspects an actual system
- when a feature works but feels shallow, generic, disconnected, duplicated, or repetitive
- when the user complains about simplification, missing depth, duplicate content, or weak rewards
- before calling a major implementation complete
- when the main agent needs a concrete expansion spec addendum
- when repeated audit findings suggest a reusable skill update

Do not use this skill to invent unrelated expansions during a narrow bug fix unless the bug reveals a real design weakness.

## 3. Relationship with other skills

Use this skill together with the relevant system skill:

- `chaos-redux-event-planning` for turning depth gaps into concrete design addenda
- `chaos-redux-events` for event chains, event logs, evolutions, clusters, event details, and spreadsheet alignment
- `chaos-redux-event-assets` for visual depth, asset evolution, icons, portraits, flags, report images, and sprite handoff quality
- `chaos-redux-super-events` for super-event role, title, description, quote, audio, image, trigger, and docs depth
- `hoi4-focus-trees` for focus route depth, reward variety, AI, and country identity
- `hoi4-decisions-missions` for active decisions, missions, costs, timers, cleanup, and objective quality
- `chaos-redux-subagents` for routing improvement passes and handoffs

When this skill reveals a repeated workflow or repeated failure pattern, route the reusable instruction to `chaosx_skill_maintainer`.

## 4. Recursive expansion model

The main agent may run this loop several times during implementation.

A normal loop is:

1. implement or inspect the current feature state
2. identify shallow, duplicated, generic, disconnected, or low-impact areas
3. spawn `chaosx_mechanic_expander` when the issue needs new design rather than a simple fix
4. receive a concrete expansion spec addendum
5. decide what should be implemented now and what should be queued
6. implement accepted additions through the relevant skills
7. run normal audit and completion proof again

The expansion subagent should not merely say “add more flavor.” It must create specific design material that the main agent can implement.

## 5. Depth rubric

### Mechanics

A mechanic should have a clear role in play.

Check whether it has:

- meaningful player choices
- clear pressure, cost, risk, tradeoff, or opportunity
- dynamic scaling where campaign state should matter
- success, failure, partial success, and aftermath where appropriate
- AI behavior that can use or react to it
- integration with existing Chaos Redux systems
- cleanup and stale-state handling
- documentation that explains what the mechanic actually does

Weak signs:

- a passive modifier with no decisions or counterplay
- a value that only goes up or down without consequences
- fixed numbers where country size, war state, chaos, or threat should matter
- a mechanic that never changes player behavior
- a system that exists only because the spec mentioned it

### Events, evolutions, and clusters

An event should feel like part of a living system.

Check whether it has:

- readable cause and consequence
- choices or state changes that matter later
- follow-ups where the situation deserves them
- event log and event detail support
- evolution tracks when the event mutates or escalates
- clusters when the event belongs to a larger related burst
- rare variants when the concept supports them
- world reactions or country-specific reactions when scale requires them
- docs and spreadsheet rows aligned with in-game localisation

Weak signs:

- one popup with no later effect
- evolutions that only change text
- clusters that only fire unrelated popups
- event details that paraphrase or contradict in-game localisation
- lore that is vague, confusing, or detached from gameplay

### Decisions and missions

Decisions and missions should represent actual actions.

Check whether they:

- ask the player to commit resources, units, time, map control, or risk
- use costs that fit the action
- have readable requirements and tooltips
- have success, failure, cleanup, and cooldowns
- connect to focuses, events, AI, and pressure systems
- avoid passive checklist completion when action is expected

Weak signs:

- repeated political power purchases
- missions that are already completed when they appear
- identical timers and costs everywhere
- no failure consequences
- no AI logic

### Focus trees

A focus tree should define playable identity.

Check whether it has:

- real route families
- meaningful political, industry, military, diplomacy, and expansion branches when relevant
- branch interaction and visible payoffs
- varied focus rewards
- idea lifecycles instead of idea spam
- route-specific leaders, flags, advisors, decisions, missions, claims, cores, units, or events where relevant
- route-aware AI
- readable localisation tone
- enough unique or justified reused icons

Weak signs:

- long vertical reward chains
- repeated equipment, factory, PP, stability, or war support rewards
- focus names that could belong to any country
- duplicate focus effects under different names
- no endgame ambition

### Country packages

A country should be playable or meaningfully purposeful.

Check whether it has:

- tag registration and history consistency
- state setup, capital, cores, claims, supply, and starting map logic
- leader, portrait, party names, flag, ideas, and localisation
- starting military, technology, industry, and production setup
- focus tree or equivalent route system when long-lived
- decisions, missions, AI, and diplomacy behavior where needed
- distinct identity and route purpose

Weak signs:

- a released country with no real identity
- generic leader, generic flag, generic focus tree, or generic ideas
- no AI survival plan
- no starting weakness or meaningful route

### Visuals and assets

Visuals should support progression and identity.

Check whether:

- major mechanic stages have visual changes where the player should notice escalation
- icons are readable, distinct, and tied to gameplay purpose
- flags and portraits support country identity
- report, news, and super-event images fit the era and tone
- reused assets are documented and justified
- asset manifests and handoffs are complete

Weak signs:

- many focuses share a generic icon without route logic
- static visuals across major evolutions
- visuals that look unrelated to the mechanic
- generated placeholders used as final art without approval

### Super-events

A super-event must be a complete package.

Check whether:

- title, description, button text, quote, image, audio, trigger, and docs fit the same role
- the quote is real and sourced
- the audio is licensed, converted, wired, and documented
- the image fits source mode and era requirements
- the super-event marks a moment that deserves the treatment

Weak signs:

- dramatic title with no matching gameplay moment
- missing audio or image documentation
- quote chosen because it sounds dramatic rather than because it fits

## 6. Expansion spec addendum

When depth work is needed, create a spec addendum.

Recommended path:

```text
docs/plans/<event_id>_<event_slug>_plans/<feature_slug>_expansion_addendum.md
```

Do not write new planning output under `docs/planning/`, `planning/`, or any other planning folder. Use `docs/plans/` for plans and addenda. If a prompt says "planning folder", treat that as `docs/plans/` unless the parent explicitly provides another path.

Keep plan addenda readable as concise design handoffs. Prefer player-facing behavior, route purpose, balance intent, asset direction, and audit needs. Put exact constants, full scripted-effect names, long file lists, parser-level implementation notes, and detailed code wiring in implementation docs, code comments, or the main-agent working notes unless the parent explicitly asks for a technical blueprint.

Use this format:

```md
# <Feature name> expansion addendum

## Current depth status
- Complete:
- Adequate:
- Shallow:
- Placeholder or fallback:
- Blocked:

## Evidence from current implementation
- File:
- Identifier:
- Observed issue:
- Why it matters:

## Core expansion thesis
A short explanation of what the feature should become.

## Accepted design constraints
Rules from the user, existing specs, existing implementation, and skills that the expansion must preserve.

## Expansion package

### Immediate implementation additions
For each addition:
- Name:
- Purpose:
- Player-facing behavior:
- Gameplay effect:
- AI behavior:
- Localisation need:
- Asset need:
- Validation need:

### Deeper branch additions
For larger optional additions:
- Name:
- Why it deepens the mechanic:
- New player-facing surfaces:
- Risks:
- User decision needed:

### Cleanup, merging, or removal
- Duplicate content to merge:
- Generic content to replace:
- Filler content to remove:

### Visual progression plan
- Stage or route:
- Needed image, icon, flag, portrait, or UI change:
- Source mode:
- Handoff target:

### Lore and readability plan
- What the player currently understands:
- What is unclear:
- What text, event detail, evolution detail, cluster detail, or doc should clarify it:

## Recursive follow-up
- What should be re-audited after implementation:
- Which subagents should inspect the result:
- Which ideas should remain queued instead of implemented now:
```

## 7. Improvement handoff for audit subagents

Audit subagents do not need to write a full spec addendum every time.

When they inspect real systems, they should include:

```md
## Improvement handoff

### Depth status
- Complete:
- Adequate:
- Shallow:
- Placeholder or fallback:
- Blocked:

### What feels shallow
- File or system:
- Evidence:
- Why it is shallow:
- What player-facing problem it creates:

### Expansion opportunities
1. Immediate fix
   - Change:
   - Why it matters:
   - Files likely touched:
   - Risk:

2. Deeper expansion
   - Change:
   - Why it matters:
   - Files likely touched:
   - Needs user approval:

### Recommended next agent
- None:
- Main agent can fix directly:
- Spawn `chaosx_mechanic_expander`:
- Spawn another specialist:
```

## 8. Scope control

Do not expand everything.

A proposed expansion should be accepted only if it:

- makes player choices more meaningful
- makes the mechanic more reactive
- removes duplicate or filler content
- clarifies unreadable lore
- gives AI a real plan
- adds visible progression where progression matters
- connects the feature to existing Chaos Redux systems
- fixes a mismatch between implementation and intended identity

Queue expansions when they are good but too large for the current task.

Reject expansions that are only bigger, louder, darker, or more complicated without improving play.

## 9. Completion rule

A major feature is not complete until the main agent either:

- implements the accepted expansion addendum
- queues it clearly as future work
- rejects it with a reason
- or records that no meaningful expansion was found

Do not hide accepted expansion work under vague “future improvements.”
