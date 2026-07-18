# Coding Prompt: Implement Event 15 Utopia Manifesto

Implement Chaos Redux Event 15 from the complete source package in `docs/specs/015_utopia_manifesto_specs/`.

## Nonnegotiable event identity

- ID 15
- slug `utopia_manifesto`
- Minor Fire-Once
- no cluster
- completely replace the old World Tension Subsides content and mappings
- AI always accepts
- an eligible human player can accept or reject
- acceptance replaces only a safely replaceable focus tree
- rejection leaves the existing tree unchanged and clears all Event 15 temporary state

## Required reading and exploration

Read `AGENTS.md`, all relevant repository skills, the full source-spec package, current Event 15 files and mappings, current event log, focus loading, decision, country, GUI, GFX, achievement, documentation, and catalog patterns.

Consult the required offline Paradox wiki pages, vanilla documentation, and vanilla examples. Use `chaosx_repo_explorer` with `fork_context=false` before editing because the event spans many systems and exact live touchpoints are unknown.

Do not use a shallow additive branch as a fallback for protected unique trees. Exclude unsafe targets instead.

## Implement the full event contract

### Target selection

Build a reusable safe candidate gate and weighted weak-country score.

Exclude:

- majors
- strong-industry countries
- protected or mature unique trees
- other event-created country packages
- civil wars and near-capitulation states
- special Chaos and nonhuman countries
- terminal actors
- dominant faction leaders and extensive subject empires

Prefer eligible players, then safe AI minors. Show clear debug or manual unavailability reasons. Warn a selected player that acceptance replaces the current focus tree.

### Event chain and logs

Implement the opening choice, public circulation, first survey, interpretive congress, first store, route events, first Need case, associate outcomes, formation threshold, foreign reactions, and five evolutions.

Wire:

- random-event classification
- event name mappings
- debug name mappings
- event-log actor
- Event Details
- evolution log stages and actors
- documentation
- catalog handoff

Event Details must describe the premise, not effects.

### Commonwealth Ledger

Implement the four visible values:

- Need
- Plenty
- Concord
- Choice versus Assignment

Create centralized tuning, scripted effects, scripted triggers, breakdown localisation, AI helpers, cleanup, and the scripted GUI described in the specs. Do not add a contradiction meter.

### Focus tree

Create a comprehensive replacement tree with:

- opening survey and institutions
- Consent of Households
- Common Table
- Guardians of Measure
- Closed Island
- hidden The Joke Understood route
- callings and education
- common stores
- Garden City districts
- island project variants
- defense
- foreign commonwealth
- Necessary Ground
- stewardship and integration
- crisis correction
- formation
- post-formation play

Make branches interlock. Use varied rewards, staged ideas, decisions, missions, map work, leaders, advisors, flags, diplomacy, and AI. Do not fill the tree with political power, tiny modifiers, repeated ideas, or generic unit grants. Provide a route coverage table after implementation.

### Decisions and missions

Implement all mapped families and their dynamic costs, durations, partial outcomes, AI, selected-target flow, cleanup, and exploit controls. Use real resources beyond political power.

### Territory and integration

Implement the case ladder from domestic substitution through purchase, lease, joint administration, ultimatum, and war. Cases need real deficits, target relevance, integrity, expiration, and renunciation.

Implement temporary stewardship, provision, route restoration, local charter, association, status vote, long integration, autonomy, return, revolt, and Assigned Colony. Do not grant free instant cores.

### Country identity

Preserve the original tag and base flag before transformation. Add route-specific cosmetic identities, parties, institutions, advisors, ImageGen flags, league emblems, and leadership changes. Practical Commonwealth preserves the saved surviving constitutional leader. The four routes that replace personal leadership use institutional names and people-free ImageGen tableaux built from empty chambers, tables, ledgers, apparatus, stores, seals, tools, empty seats, and route emblems; do not depict people or human representations. Advisors use independent fictional ImageGen portrait masters plus separately generated dossier overlays and regionally plausible gender-matched names.

### AI

Implement route selection, focus plans, Ledger decisions, calling methods, reserves, districts, Need targets, stewardship, league behavior, military behavior, high-chaos exceptions, and invalid-route blocking. The AI must not play a simplified parallel system.

### Evolutions

Implement the five mapped evolutions with active-event and pre-fire entry paths:

1. Glosses in the Margin
2. Necessary Shores
3. Cities of One Measure
4. Nowhere Made Law
5. The Perfect Island

Use dynamic pacing. Disabled evolutions must not set recorded flags or trap baseline progression.

### Assets and super-event

Use the dedicated asset and super-event prompts. Produce and wire every required event image, focus icon, idea icon, decision icon, flag, portrait, emblem, achievement icon, GUI asset, animation sheet, static fallback, final super-event image, verified quote, cultural remark, and uniquely licensed audio.

No placeholder asset, unsourced quote, or temporary audio can be called complete.

### Achievements

Implement every achievement in the achievement matrix with tracking, disqualifiers, localisation, icons, docs, and exploit protection.

## Subagents and review order

Spawn all project subagents with `fork_context=false` and explicit paths.

Use:

- repo explorer before editing
- scripted-system architect before duplicating helpers
- asset and super-event research agents for production
- focus, decision, country, and localisation auditors after their surfaces exist
- documentation curator after major integration
- spreadsheet worker after final localisation
- improvement-loop planner near completion
- event completion auditor before any completion claim

Resolve every accepted addendum. Do not stack an unresolved improvement plan with another pass.

## Completion standard

Do not claim completion while any mapped route, mechanic, AI behavior, evolution, event, decision, mission, achievement, asset, audio package, localisation surface, document, or catalog field is missing. Report every simplification, omission, fallback, and blocker. If none remain, state that and provide file and audit evidence.
