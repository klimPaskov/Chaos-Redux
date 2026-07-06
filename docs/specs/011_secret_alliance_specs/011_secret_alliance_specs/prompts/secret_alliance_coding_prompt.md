# Coding prompt for 011 Secret Alliance

Implement Event 11, Secret Alliance, according to the source spec package at `docs/specs/011_secret_alliance_specs/`.

Follow `AGENTS.md`, `chaos-redux-events`, `hoi4-decisions-missions`, `chaos-redux-super-events`, `chaos-redux-event-assets`, `chaos-redux-frame-animation`, `chaos-redux-improvement-loop`, and `chaos-redux-subagents`.

## Non-negotiable design requirements

- Keep Event 11 as a Minor Fire-Once event.
- Create a hidden pact against the current player country.
- Select three initial countries that are not at war with the player, preferring minors outside factions.
- Use scored selection so members have motives, such as fear, ideology, border revenge, opportunism, or patron dependency.
- Track hidden roles, membership rings, Evidence, Preparedness, player isolation, Pact Cohesion, Pact Readiness, and War Clock.
- The player should not know all members at the start.
- Baseline is subtle and slow.
- Evolution I expands minor membership and activity.
- Evolution II adds or starts with a major patron, opens the decision category, and enables serious sabotage and counterplay.
- Evolution III makes the pact public on the map, opens the player war option, and makes war likely without deleting the final preparation window unless hard reveal already fired.
- If the event first fires at Evolution III conditions, start from Evolution II and advance to Evolution III after a short readable interval.
- If a full pact country goes to war with the player, reveal the pact, form Anti-[player country] Pact, and call full signatories into war.
- Reveal must fire a completed researched super-event package.

## Decisions and missions

Implement the dossier category and mapped decisions from the decision map. Use concrete costs such as equipment, trains, convoys, fuel, XP, manpower commitments, stability risk, civilian burden, and real unit placement. Do not reduce major decisions to political power or command power purchases.

## Assets and super-event

Use the asset prompt for all icons, super-event image, achievements, and optional animated dossier or warning assets. Use real frame animation workflow for any final animation. Use the super-event prompt to research final title, quote, cultural remark, and audio. Treat unresearched text or audio as blockers.

## AI

Implement motive-based AI for pact members, major patron, neutrals, allies, innocent suspects, invitations, sabotage, reveal, war entry, exits, and public faction behavior. AI must avoid invalid targets and invalid border actions.

## Documentation and catalog

Keep event script, registration, event log, evolution log, Event Details, localisation, docs, assets, super-event docs, and catalog wording aligned. Update the event catalog workbook only after final in-game wording exists and use the spreadsheet worker.

## Required subagent pass before completion

Before any completion claim, spawn `chaosx_improvement_loop_planner` with `fork_context=false` and explicit context for this event. Resolve its addendum or closure handoff by implementing it, promoting it into specs, queueing it with a reason, or rejecting it with a reason. Then run appropriate audits, including decision, localisation, scripted-system, asset, super-event, and completion audit as the implementation scope requires.

Do not claim completion while any mapped evolution, reveal behavior, decision family, AI behavior, asset, achievement, super-event element, documentation update, catalog alignment, validation, or accepted planner result is missing.
