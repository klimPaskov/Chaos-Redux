# Coding prompt: Implement Event 011 Secret Alliance

Status: fulfilled historical implementation prompt. Final gameplay and balance authority is commit `1c87d923`. Do not rerun this prompt as open work.

Implement the full Event 011 Secret Alliance rework from this planning package. Treat every file in `specs/`, `matrices/`, and `research/` as one design set. Follow `AGENTS.md`, `chaos-redux-events`, `hoi4-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-frame-animation`, `chaos-redux-super-events`, `chaos-redux-subagents`, and `chaos-redux-improvement-loop`.

## Pre-implementation reading

Before editing, read the repository versions of every relevant skill, the offline Paradox wiki core pages required by AGENTS.md, relevant vanilla documentation, and at least one vanilla precedent for events, decisions, faction creation, targeted country selection, event targets, scripted localisation, scripted GUI, AI decisions, achievements, and super-event wiring.

Use the repo explorer role because this event spans event registration, runtime hooks, decisions, scripted GUI, factions, AI, assets, super-events, docs, settings scenarios, achievements, localisation, and spreadsheet alignment. Save the bounded exploration handoff under `docs/plans/011_secret_alliance_plans/subagent_handoffs/`.

## Event identity and registration

- Keep the canonical entry format `chaosx.nr11.1` and stable related namespace IDs.
- Classify Event 011 as Minor Fire-Once.
- Remove it from the unreworked default-disabled state only when the full rework is ready.
- Register its valid-target gate so the event shows `N/A` when three valid founders cannot be selected.
- Fix the target to the player country at firing. Tag switching must not retarget the chain.
- Preserve multiplayer consent for any human-controlled candidate.
- Do not add Event 011 to an event cluster.

## Hidden pact system

Implement the event-owned hidden membership network, founder selection, motives, doctrine, cohesion, readiness, alertness, recruitment attraction, suspect confidence, and validity cleanup.

Ordinary founders are three valid independent minors. Prefer factionless countries. Exclude the target, target faction, target subjects and overlord, countries already at war with the target, invalid or capitulated actors, and nonhuman or special chaos countries that ordinary diplomacy should not use.

Weight founders and recruits through geography, claims, grievance, ideology, target threat, sponsor pressure, relations, current wars, faction duties, and strategic reach. Do not use a uniform random-country draw.

Use event targets or stable country-scoped membership state with explicit cleanup. Centralize repeated selection, validity, recruitment, operation, reveal, conversion, and cleanup logic in documented scripted effects and triggers. Centralize tuning in script constants where supported.

## Baseline operations and progression

Implement the baseline stages and operation families from Parts 1 and 2. Baseline stages are not evolutions.

Operations include:

- diplomatic isolation
- intelligence penetration
- industrial and transport sabotage
- political and social pressure
- military preparation
- recruitment
- internal pact disputes

Use dynamic MTTH or paced pulses. Avoid global daily or weekly country iteration unless the user explicitly approves it. Use event-owned runtime hooks and narrow scope.

Only one substantial operation should normally be active against the target. Apply anti-repetition weights and recovery windows. Early incidents remain ambiguous. Evolution II may unlock controlled severe sabotage and rare political violence.

## Evolutions

Implement three true evolution stages with shared evolution logging.

- Evolution I at Gathering Storm by default. Active pacts widen minor recruitment and operations. Pre-fire openings use four to five minor founders.
- Evolution II at Rising Chaos by default. Active pacts can gain one valid major sponsor and unlock the counter-network category. Pre-fire openings can be major-led with minor partners.
- Evolution III at Totalen Chaos by default. The faction becomes public, a second major can join when strategically valid, war pressure rises, and direct preemption opens. A pre-fire Evolution III opening must start through the Evolution II package, then progress after a short dynamic delay.

Use dynamic pacing. Respect evolution enable and disable settings. Disabled evolutions must not set recorded flags or lock required baseline progression.

## Decision and mechanic window

Implement the full decision and mission matrix. Open the public foreign-interference category at Evolution II. Show Evidence and Preparedness, recent incidents, selected suspects, confidence bands, and current missions. At Evolution III add war pressure and the single animated coalition-closure warning.

Use varied, dynamic costs and named objectives. Implement partial success, failure, active mission caps, selected-target handling, AI equivalents, and cleanup. False accusation must have consequences. The player must be able to investigate, protect, negotiate, deceive, turn a member, expose the coalition, prepare borders, use limited border conflict when valid, and exploit coalition fractures after reveal.

Do not replace the mapped system with a few generic decisions or passive modifiers.

## Reveal and faction contract

Implement one reusable reveal effect.

Before reveal, refresh membership validity and remove impossible members. Select the leader in this order: designated major sponsor, strongest major, strongest founder, hostile-war trigger country.

The public faction name uses a dynamic Anti-[target adjective] Pact pattern with a grammatical name-based fallback.

Hard rule: when any active pact member enters a normal hostile war against the target, reveal the pact immediately, form the actual faction, add every valid active member, and bring every valid active member into the target war immediately. A border conflict does not count until it becomes normal war.

Other reveal paths include pact-controlled Evolution III reveal, player-forced reveal, and fractured reveal. Every path converges on the same faction and conversion contract.

At reveal convert Cohesion into Coalition Resolve, Readiness into opening coordination, Evidence into known enemy weaknesses, and Preparedness into defensive advantages. Preserve concrete consequences from turned members and false plans.

## Coalition war and aftermath

Implement route-aware coalition war AI, shared target priorities, access-aware theater roles, Resolve changes, member confidence, leadership disputes, separate terms, withdrawal, and sponsor collapse. Distant members may contribute air, naval, expeditionary, equipment, or intelligence support rather than wasting armies on unreachable fronts.

After the target war, evaluate dissolution, continued regional bloc, negotiated security arrangement, leadership split, or coalition victory settlement. Clean all hidden-pact state and obsolete decisions.

## Triggerable scenario

Add the direct scenario described in Part 4 under a final player-facing name written during implementation. Use the next valid scenario registry ID after inspecting the current registry.

Types:

- Regional Ring
- Ideological Front
- Great-Power Sponsor
- Unlikely Coalition
- Random Coalition

Support Low, Medium, High, and Maximum intensity. Confirmation reads the selected type and intensity at launch time. Launch creates the public faction, starts war, and fires the reveal super-event immediately. Bypass normal chaos, evolution, date, and event-history prerequisites. Retain only terminal-state, impossible-scope, and human-consent gates. Clean launch bypass state when setup finishes.

## Super-event

Implement one reveal super-event with a unique slot, image, title, description, button remark, quote, audio track, audio ID, settings-aware playback, GFX, scripted localisation, docs, and music table entry.

Use the researched quote package only after final source review. Treat unselected or unlicensed audio as a blocker. Do not use placeholder, default, reused, or generated-tone audio.

## Assets and achievements

Produce and wire every required asset in the asset register. No visible placeholder is allowed. Use generated period-documentary art for procedural scenes, separate icon sources by asset type, and real source frames for the one animation.

Implement all six achievements from the achievement matrix with exact tracking, disqualifiers, localisation, icon triplets, GFX, docs, and scenario-origin rules.

## AI

Implement the full AI matrix for founders, recruits, sponsors, targets, operations, reveal, coalition war, scenario types, and high-chaos exceptions. AI must respect reach, factions, current wars, stability, resources, motive, Evidence, Preparedness, cohesion, and route validity.

## Localisation and documentation

Write final player-facing localisation from the direction in the specs. Do not paste working labels as final text. Preserve secrecy before reveal. Use custom tooltips and dynamic values. Keep UTF-8 with BOM and project key conventions.

Update:

- event and news localisation
- event names and debug mapping
- event-log details and evolution details
- decisions, missions, ideas, GUI, scenario, faction, achievement, and super-event text
- `docs/events/011_secret_alliance.md`
- triggerable-scenario docs
- super-event and audio docs
- asset manifest and GFX handoff
- event catalog workbook through the spreadsheet worker after final in-game wording exists

Event Details and spreadsheet Details describe the premise, not mechanical effects.

## Specialist audits and improvement loop

Use the scripted-system architect before duplicating helper logic. After implementation, run the decision and mission auditor, localisation auditor, and event completion auditor. Use the documentation curator after handoffs accumulate. The focus-tree and country-package auditors should record that no new trees or country packages are part of the accepted scope, then check that existing countries are not overwritten.

Before near-completion, spawn the improvement-loop planner with `fork_context=false`. Resolve its addendum by implementing it, folding accepted design into specs, queuing it with a reason, rejecting it with a reason, or recording a closure handoff. Do not stack unresolved addenda.

## Completion standard

Do not claim completion until the full spec, all assets, all final audio, all achievements, all AI, all localisation, all docs, all event-log surfaces, the scenario, and the catalog workbook are aligned. Report every simplification, omission, fallback, blocker, renamed surface, and skipped task-specific validation. Fallbacks require user approval.
