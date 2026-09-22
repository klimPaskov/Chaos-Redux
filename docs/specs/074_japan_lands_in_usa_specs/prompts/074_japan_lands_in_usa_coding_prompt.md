# Coding prompt: Event 074

Implement Event 074 from `docs/specs/074_japan_lands_in_usa_specs/`.
Read its README, all eight files under `design/`, and all reference contracts before changing gameplay.
Use the stage prompts in order, and keep implementation plans, specialist handoffs, unresolved evidence and audits under `docs/plans/074_japan_lands_in_usa_plans/`.
The source package remains under `docs/specs/`.
Do not create `docs/planning/` or mix temporary progress notes into the accepted design.

## Read and inspect first

Read the current repository `AGENTS.md`, `README.md`, `CHAOS_REDUX_MECHANICS.md`, the event-planning, events, subagents, decisions-missions, improvement-loop, event-assets, super-events, debug-playtest and MTTH skills, and their applicable must-read references in full.
The source register says exactly which references were not completed during planning.
Resolve those gaps rather than treating its full supplied-file read as a complete vanilla or repository audit.
Read other skills when their actual consumers are involved.
Do not call the focus-tree, portrait or 3D implementation work necessary when this design requests no such new content.

Inspect the existing root in `events/074_japan_california.txt`, its report, shared news consumer, English localisation, shared dispatcher, timer, fire-once records, settings, cluster definitions, evolution log and achievements.
The old root is `chaosx.nr74.1`, its report is `chaosx.nr74.2`, and inspected old news is `chaosx.news.65`.
Retain compatible canonical entry points and remove duplicate old material effects.
Do not assume the inspected old repository snapshot is the current checkout.

## Nonnegotiable gameplay

The strategic requirements are only existing Japan, existing United States, and their active bilateral war.
Shared settings and fire-once rules still apply.
Do not require Japan to win, have a navy, possess naval supremacy, follow an ideology, meet a date gate or remain uncapitulated.
Resolve a safe legal Pacific mainland placement with California preferred.
A genuinely impossible placement remains unconsumed and produces no news.
Do not convert a defended coast into a covert strength restriction.

Create the actual opening army, prepared access and legal wartime control before acknowledgements.
Do not transfer ownership, delete defenders, mass-teleport unrelated units, begin an extra war or quietly reduce the force.
Prove defended-coast behavior before using it in the dispatcher.
The baseline and three tiers grant 30, 60, 100 and 150 immediate divisions before the frozen campaign factor, with lifetime force ceilings of 40, 75, 125 and 180.
The factor is capped at 1.50 and never recomputed after commitment.
Exact rounding, role allocation and embedded-versus-loose accounting are in Part 3 and the capability contract.

Implement actual equipment, manpower, fuel, valid aircraft, ordinary commanders, legal buildings, measured local supply and finite deliveries.
National stocks are not fictional state-local warehouses.
No permanent supply immunity or country-wide combat boost may replace a local requirement.
Use supported ordinary equipment and templates across the declared DLC profiles without undoing research losses.
Inspect any technology grant using `hoi4.tech_inspect`, `hoi4.tech_render` and `hoi4.tech_compare`.

Implement highest-enabled pre-fire tiers at Chaos 200, 400 and 600 and delayed active evolution through the supplied framework.
Active upgrades issue only positive cumulative entitlement through retained access.
They never repeat territorial seizure, replace losses for free, revive a closed support system, or record disabled stages.
Distinguish temporary access interruption, permanent support closure, campaign-operation cleanup and ordinary war ending.
Support expiry does not delete the army or falsely end the mainland war.

## Complete the campaign surfaces

Implement all four Japanese and five American action families, five mission definitions with at most two active per actor, cost parity, reservations, cancellation, lifetime allowances and meaningful objective conditions.
Keep every action at no more than four spendable cost types and use the defined exact resources.
Use native decision categories and two public custom readings, working access and support time.
Do not build another resource wallet or a full custom GUI.
Preserve both countries' existing identities, focus trees, governments, flags and characters.
No custom tag, new focus tree, unique unit model, doctrine family or scripted peace is planned.
If a separately approved expansion adds a tag, perform the complete vanilla, Chaos Redux, Workshop and local-mod collision inventory before creation.
Any separately approved 3D or skeletal-animation work must be delegated to `chaosx_3d_model_pipeline` and pass actual export, reimport and consumer validation.

Implement Japan's mainland retention and useful expansion priorities and the American emergency response.
Separate requested tactical intent from what the engine can actually command.
Run the AI observations and probability scenarios, not merely static strategy-file checks.
Spawn `chaosx_ai_probability_auditor` with no inherited conversation context.
It must start with `hoi4.probability_inspect`, then use evaluation, sweep, justified simulation, comparison, rendering and sequence analysis where applicable.
No manual weight arithmetic is a substitute for a missing game-version adapter.

Implement the full Chaos impact map, including the initial material theater, later actual external conquest, inland spread, no payment for stage flags, bounded recovery reversals and permanent anti-farming receipts.
There is no special Chaos-country growth system in this design.
Do not invent one to fill a generic checklist.
Audit overlap with shared war, military-buildup, annexation, deaths and other generic sources.
Failed containment has the concrete continuing theater and possible later conquest as its consequence, with no automatic daily Chaos income.

## Presentation, achievements and source truth

Use the separate asset, super-event, decision-mission and achievement prompts in this folder.
Write final player-facing event, decision, mission, achievement, category, history and event-detail localisation from the design directions.
The user-supplied event and evolution names are accepted, while other working labels are not finished text.
Research final super-event titles, button text, quotations, cultural references and audio through the required specialists.
Unresearched text, unclear rights or missing audio remains blocked.
Do not fill the super-event slot with default music or generic placeholder copy.

Implement all five compound achievements with exact tracking, disqualifiers and the prescribed three-state icon output.
Generate or source every necessary visual using the exact native references, size, alpha, conversion and provenance rules.
Do not mark a manifest row complete without accepted runtime bytes and its actual consumer.
The plan proposes static visuals and has no requested animated assets to replace with still-image movement.

Update the authoritative workbook `docs/spreadsheets/chaos_redux_events_catalog.xlsx` only after final wording and verified mechanics exist.
Use the spreadsheet specialist and `.tools/export_event_catalog_csv.py` for the export.
Never edit the supplied CSV as the source of truth.
Set Wars Medium while preserving the event's Minor Fire-Once classification and catalog Chaos level 1.
Do not mark To Be Reworked complete merely because code was written.

## Specialist work and closure

Use `collaboration.spawn_agent` with `fork_turns="none"` where available.
Give each specialist the event identity, goal, user constraints, exact spec paths, relevant plan paths, source gaps, assigned question, allowed write scope and required output.
Use the context-complete task cards in `074_japan_lands_in_usa_specialist_tasks.md`.
Do not imply that the planning session already executed those agents.
If the interface is unavailable, state that exact blocker and continue only independent work that remains possible.

Before calling the work near complete, spawn `chaosx_improvement_loop_planner`, obtain its addendum or closure handoff, and dispose every finding.
Integrate accepted changes into the main specs, prompts, assets, tests and working implementation rather than leaving them isolated.
Then obtain the completion audit and document route coverage, unresolved gates and evidence.
Do not grow the design with unrelated tags, trees, currencies or minigames merely to produce an addendum.

Use the acceptance matrix for static, save, multiplayer, map, supply, AI, asset and live-game checks.
Follow the debug-playtest skill and current user authority for game execution.
Never report an unrun test as passed.
Keep iterating until the goal is accomplished to its fullest extent, without silent fallbacks, shortened substitutes or temporary versions presented as final.
Do not claim completion until the implemented files satisfy the specification and the required evidence is available.
The final report must name changed files, completed routes, test results, source and tool limitations, final asset consumers, catalog changes and the disposition of each specialist finding.
