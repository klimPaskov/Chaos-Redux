# Coding Prompt: Event 24 Video Game in Sweden

Implement Chaos Redux Event 24 from the accepted source specification under `docs/specs/024_video_game_in_sweden_specs/`.

Read every file in that folder before editing. Treat the four main specification parts as acceptance criteria. Use the decision map, probability scenarios, asset prompt, achievement prompt, decision and mission prompt, catalog alignment note, research note, review handoff, and source reading audit as supporting contracts.

## Required implementation references

Before editing, read `AGENTS.md`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-improvement-loop`, and `chaos-redux-subagents`. Read the required offline Paradox wiki pages and installed vanilla documentation for events, decisions, ideas, commander traits, achievements, scripted localisation, scopes, modifiers, AI, and graphical assets. Inspect at least one current Chaos Redux fire-once event, one staged event-owned decision system, one commander trait precedent, one achievement group, and matching vanilla precedents.

Use the mandatory HOI4 MCP workflow. Inspect and render the current Event 24 chain before editing when an implementation exists. After editing, compare the chain against the prior state and inspect every event option, MTTH block, random list, decision AI score, and foreign-response pool through the probability route. Use the named scenarios in `024_video_game_in_sweden_ai_probability_scenarios.md`. Missing MCP access is a blocker and must be reported.

## Expected repository surfaces

Inspect the real repository before locking filenames. The implementation will normally need an Event 24 event file, event-owned script constants, host and phase triggers, scripted effects, decision and category files, ideas, commander-trait registration, AI logic, localisation, event-log mappings, the root achievement registry, sprite definitions, final runtime assets, an event documentation folder, and the authoritative catalog workbook. Preserve stable existing paths and ids when Event 24 already has source files. Keep shared Event Log behavior in its established shared files and keep Event 24 gameplay logic in event-owned files.

## Event identity and registration

Keep entry event `chaosx.nr24.1`. Register ID `24` as a Minor Fire-Once event with Chaos level `1`. Keep it unclustered. Add it to the normal reworked-event default enable allowlist only after the complete accepted feature is ready. The package surface list is exhaustive.

Create one reusable Event 24 valid-host trigger or helper. Select one principal Swedish host in the priority order defined by the core spec. Prevent duplicate program instances after civil wars, annexation, release, puppeting, cosmetic changes, or tag switches. When no valid host exists, normal selection and the Events tab must show Event 24 as unavailable with `N/A` weight. Fire-once history remains permanent after the event fires.

## Core mechanic

Implement one visible country value named Simulation Reliance on a `0` to `100` scale. Use the four public states and thresholds from the spec. Centralize gains, losses, thresholds, durations, caps, MTTH anchors, AI factors, and incident cooldowns in event-owned script constants. Do not expose internal score components as extra player-managed values.

Implement one staged idea lifecycle. Only one Event 24 idea may be active at a time. Replace or remove the prior stage whenever the lifecycle advances, recovers, restricts, or concludes. The final validated-methods idea is finite and expires. Do not leave a permanent stack of related bonuses.

## Baseline and evolutions

Implement the three baseline release philosophies and their distinct starting conditions, benefits, risks, AI preferences, and conclusion routes. The baseline must be able to conclude without any evolution after a meaningful review period.

Implement all three evolutions as actual delayed evolution milestones, separate from baseline progression:

1. Gamified Officer Corps at Gathering Storm or higher.
2. A National Obsession at Rising Chaos or higher.
3. Losing the Sense of Reality at Chaos Tier or higher.

Use the eligibility, pacing, route modifiers, high-Chaos opening rules, disabled-evolution handling, incident pools, and resolution states in the evolution spec. A high-Chaos campaign may begin with a stronger opening, but it must never jump directly into an unanswerable Evolution III state. Disabled evolutions must not set recorded flags or unlock their content.

Evolution III must preserve all four response paths. Trust the Model may create a strong finite surge, but it must end in a mandatory reassessment within the specified maximum period. No route may make the crisis permanent or let it dominate the rest of the campaign.

## Decisions, missions, traits, and foreign reactions

Implement one event-owned decision category using normal decisions, scripted localisation, one static category picture, and the staged idea icon. Keep three to five primary actions visible in each phase, with no more than one active mission. Hide obsolete, invalid, and completed actions. Use the complete action and state map in `024_video_game_in_sweden_decision_map.md`.

Use varied and bounded costs that fit each action. Any one action may consume at most four spendable cost types. Use correct texticons for every displayed cost. Keep requirements separate from costs. Do not turn the category into a political-power store or fill it with minor modifier dust.

Implement the field-validation objective and Reality Audit mission with success, partial success, failure, cleanup, and save persistence. Implement Rulebook Commander as a mixed temporary trait for at most one eligible Swedish commander. Remove it on the successful correction route or cleanup without awarding a replacement trait; the user's explicit 2026-09-20 instruction retires Field-Validated Planner. Never assign the trait to an invalid, dead, foreign, or duplicate target.

Foreign reactions must use a bounded pool of at most three meaningful countries. Support copy, study, ban, ridicule, or no-action outcomes according to relations, ideology, military interest, threat, and access. Do not create foreign copies of Sweden's full decision category. Validate targets before selection and record exhausted-pool behavior.

## AI and weighted logic

Implement route-specific AI for the opening, every evolution option, every decision phase, audits, restrictions, the risk route, foreign licensing, commander handling, and conclusion. AI must consider war state, stability, supply, equipment, trains, fuel, occupied cores, army experience, government type, subject status, world tension, Reliance, prior mismatch incidents, and current route validity where relevant.

Run `chaosx_ai_probability_auditor` before changing weighted values, then run the same named scenarios after the owner patch with `hoi4.probability_compare`. The auditor remains read-only. Preserve the intended ordering and safety constraints in the scenario matrix. Near capitulation, broken supply, or severe instability must never make Trust the Model the preferred route.

## Logs, text, assets, achievements, and docs

Wire the full Event Log contract. Add visible event-name mappings, debug mappings, actor selection, history recording, Event Details text, evolution catalog rows, and all three logged evolution milestones. Baseline stages do not count as evolutions. Keep Event Details player-facing and avoid raw effects, hidden conditions, achievement spoilers, or implementation notes.

Write final localisation from the direction in the presentation spec. Use dry period satire, concrete institutional behavior, and dynamic Swedish or foreign actors. Avoid modern gamer slang, direct player references, copied planning labels, generic crisis prose, em dashes, semicolons, staccato, and contrast formulas. Run `chaosx_localisation_auditor` because this event creates broad visible text.

Produce every accepted asset through the asset prompt and the proper asset subagents. Final DDS files, sprites, manifests, contact sheets, and runtime references must exist. Do not use placeholders or satisfy one icon type by resizing another. Create only the asset rows authorized by the asset prompt.

Implement both achievements from the achievement prompt with full tracking, disqualifiers, icons, documentation, and hidden-condition handling. Achievement progress must survive save and reload and must not unlock through force-trigger or debug shortcuts unless the existing project achievement framework permits that behavior.

Update event documentation and the authoritative event catalog workbook only after final in-game wording exists. Do not edit the CSV exports directly. Run `python .tools/export_event_catalog_csv.py` after the workbook update.

## Completion

Run `chaosx_decision_mission_auditor`, `chaosx_localisation_auditor`, `chaosx_ai_probability_auditor`, and `chaosx_event_completion_auditor` on the final state. Resolve every accepted finding or report it as a blocker. Test every acceptance case in the presentation spec through source inspection and available MCP evidence. Live desktop playtesting belongs only to the explicitly invoked debug-playtest workflow.

Do not simplify, merge, omit, or replace an accepted route, response, incident family, asset, achievement, AI behavior, log surface, or recovery path without explicit user approval. Report every unresolved requirement under `Simplifications, omissions, and blockers`. If none exist, state that explicitly and support it with the route, asset, achievement, and acceptance coverage tables.
