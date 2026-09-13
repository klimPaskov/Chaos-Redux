# Coding prompt for Event 41: Disease in Divisions

Implement Event 41 to the full specification under:

`docs/specs/041_disease_in_divisions_specs/`

Read every specification, quality file, diagram, research note, prompt, and handoff in that folder before editing. Follow `AGENTS.md`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-improvement-loop`, and `chaos-redux-subagents`.

Consult the required offline Paradox wiki pages and installed vanilla documentation before choosing event, unit, manpower, decision, on-action, modifier, scope, array, event-target, and GUI syntax. Inspect current Chaos Redux precedents. Use the HOI4 MCP event-chain tools for the event chain and the probability tools for every weighted surface.

## Core event

Keep the root event `chaosx.nr41.1`. Register ID 41 as Minor Repeatable, Chaos level 1, and a Low member of Cluster 8, Diseases. Add the event to the reworked default-enable allowlist only when its full implementation is ready.

Select one valid ordinary country at war with a proven active front. Exclude special Chaos countries through the shared classifier. Fail closed when no valid country, sector, or formation group exists.

Implement one public value, Army Infection Pressure. Keep all profile, node, medical, evacuation, exposure, sick, recovery, and generation data hidden. Use a bounded weekly active-episode process. Do not add a daily or monthly whole-world country, state, or division scan.

## Military disease model

Implement the three hidden profiles and their environmental response rules. Seed a bounded coherent frontline group and create visible formation or sector disease effects.

Prove an engine-supported military manpower model that separates:

- active sick
- convalescent
- returned to duty
- fatal military cases

Do not delete equipment to represent illness. Do not turn every sick soldier into a death. Do not create free manpower. Register fatal cases once through the shared Deaths system as military casualties. Reconcile every episode ledger on recovery and cleanup.

A failed baseline must be able to drive the worst infected front toward roughly half effective strength through sustained burden and combat penalties. It must not routinely halve the whole national army.

## Decisions, missions, and posture

Implement the complete phased category and every mapped action from the decision prompt. Keep the visible action budget. Implement one valid sector-rotation goal mission. Use dynamic concrete costs with no more than four spendable types per action. Keep costs, texticons, blocked reasons, tooltips, AI, cooldowns, and cleanup aligned.

Fight Through the Outbreak preserves operational freedom and raises disease risk. It must not grant free combat strength.

## Evolutions

Implement Camp Fever Across the Trenches at 200 or more Chaos and War Plague at 600 or more Chaos.

Use paced evolution activation and the shared evolution log pipeline. Evolution activation gives zero Chaos.

Implement active-event entry and pre-fire evolved opening for each evolution. Do not reset a running episode when it evolves.

Evolution I must support proven allied and enemy military transmission, weaker secondary national outbreaks, early warning, generation proof, and duplicate prevention.

Evolution II must support distant military routes and a proof-carrying civilian spillover adapter. Use the existing civilian outbreak owner. Event 41 must not create a second civilian disease ledger, register civilian deaths, or add Air Cleanliness contribution itself.

## Integrations

Implement the ownership boundaries for:

- Deaths
- biological warfare and outbreaks
- chemical contamination
- Air Cleanliness
- famine
- migration
- disasters and bombardment
- field hospitals and logistics
- event clusters

Use existing public helpers and adapters where available. If a required neutral helper is genuinely shared across systems, route its design through `chaosx_scripted_system_architect` and document it in the correct dynamic-helper registry. Keep event-owned orchestration in Event 41 files.

Implement the complete event-owned Chaos impact map with one-shot generation guards, positive caps, reversal caps, and shared-source exclusions. Do not duplicate Chaos from war, deaths, contamination, weapon use, or cluster firing.

## Event surfaces

Implement:

- event chain and milestone reports
- event registration and random selection
- event-owned on-actions or sparse delayed work
- decisions and category
- ideas, dynamic modifiers, or unit status needed by the design
- Event Logs actor and history mapping
- Event Details and evolution previews
- cluster member details and skip reasons
- map and formation presentation
- Chaos History entries
- all four achievements
- final localisation
- permanent event documentation
- canonical workbook alignment and CSV export

Write final player-facing wording from the spec direction. Do not paste planning labels as final localisation. Keep the writing concrete, military, and serious. Do not expose raw formulas, hidden profiles, future surprises, implementation history, or achievement conditions in ordinary event text.

## Assets

Produce every required final asset through the asset prompt and proper subagents. Use separate source art for each asset family. Wire final DDS files, sprites, icons, report art, category picture, status art, and achievement variants. Preserve native transparency for alpha-backed assets. Do not use primitive placeholders or resized unrelated icons.

## AI and weighted behavior

Use the full AI strategy and named scenario matrix. Spawn `chaosx_ai_probability_auditor` before weighted patches and again after implementation. Begin with `hoi4.probability_inspect`, evaluate the named scenarios, sweep pressure and threat thresholds, compare the final source, and render evidence where it improves review.

## Required subagents

Use context-complete prompts with `fork_context=false` for:

- `chaosx_scripted_system_architect`
- `chaosx_decision_mission_auditor`
- `chaosx_ai_probability_auditor`
- `chaosx_generated_event_art`
- `chaosx_icon_artist`
- `chaosx_localisation_auditor`
- `chaosx_spreadsheet_doc_worker`
- `chaosx_event_completion_auditor`
- `chaosx_improvement_loop_planner` near completion

Review every handoff. Implement, promote, queue, or reject each plan with a reason. Do not leave an accepted addendum unresolved.

## Completion standard

Run the full acceptance criteria. Produce a concrete completion report covering files, mechanics, manpower and death accounting, decisions, AI probability evidence, evolutions, adapters, Chaos history, cluster behavior, assets, achievements, docs, and workbook export.

Do not use unapproved fallbacks or simplifications. Report every blocker or deviation. Keep iterating until the implemented repository satisfies the full spec. Do not claim completion from a partial event chain, a working popup, or passing syntax alone.
