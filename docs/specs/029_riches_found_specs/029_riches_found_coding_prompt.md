# Event 029 full implementation prompt

Implement the complete Chaos Redux Event 029, Riches Found, from the accepted specification package under `docs/specs/029_riches_found_specs/`.

Do not implement a reduced prototype.

Do not replace mapped systems with small static modifiers, generic events, placeholder art, a political-power shop, a full scripted GUI, a new country tag, a new custom unit, or an Event 018 fallback.

Report every blocker, omission, merge, renamed route, substituted effect, unavailable engine behavior, and unresolved asset honestly.

## Required preflight

Before editing:

1. Read repository `AGENTS.md` in full.
2. Read `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-improvement-loop`, `chaos-redux-subagents`, and every file in the Event 029 spec package.
3. Read the relevant offline Paradox wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on-actions, event modding, decision modding, idea modding, AI modding, graphical assets, and any other touched surface.
4. Read relevant installed vanilla documentation and inspect at least one vanilla precedent for every engine-facing system.
5. Inspect the current Event 029 source, its registration, log mappings, details, assets, docs, and catalog state.
6. Inspect Event 018 Resources Found and preserve strict separation.
7. Inspect current persistent-state registries, controller-transfer hooks, dynamic modifiers, selected-target decisions, Deaths, Condemnation, repeatable-event logic, Event Details, evolution logs, asset folders, achievements, and workbook exporter.
8. Use `chaosx_repo_explorer` with `fork_context=false` only if file locations, patterns, or edit order remain unclear after direct inspection.
9. Use `hoi4.event_inspect`, `hoi4.event_render`, and `hoi4.event_compare` for the event chain.
10. Use the specialized probability workflow for every weighted or timed surface.

If the required repository, wiki, vanilla documentation, or MCP route is unavailable, stop the affected implementation surface and report the exact blocker.

Do not treat memory or this prompt as equivalent evidence.

## Event identity and registration

Keep entry event `chaosx.nr29.1`.

Register Event 029 as Minor Repeatable.

Use the shared repeatable weight cap-halving and monthly recovery.

Keep Event 029 outside every cluster.

Add one reusable valid-target gate.

When no valid ordinary country and suitable state pair exists, the event must show `N/A` and have no live selection weight.

Keep Event 029 disabled by default until the full rework is ready.

Add it to the reworked-event default allowlist only in the same final change that completes registration, log wiring, decisions, AI, assets, docs, and catalog alignment.

## Recipient and state selection

Select one existing ordinary country with at least one valid owned and controlled state.

Give every valid recipient country the same country-selection weight. Do not bias the roll by mine count, country size, major status, ideology, faction, or player control.

Exclude special and actual nonhuman countries through the shared classifiers.

Exclude temporary system carriers, invalid civil-war shells, and any current repository exclusions for ordinary civilian events.

Select one suitable state through weighted randomness.

Prefer populated, buildable, connected states with usable infrastructure, land adjacency, or a valid port route.

Reject wasteland, empty remote islands without a usable port, impassable states, Event 018 sites, existing Event 029 mines, unstable transfer scopes, and other reserved persistent sites.

Save the original discoverer, current controller, selected state, commodity profile, quality, and registry entry.

## Immediate reward

Grant the recipient exactly 1,000 political power once.

Do not lower, split, cap, or replace this amount.

Apply it once even if the event is reopened, transferred, saved, or reloaded.

Document any engine cap or actual loss found in testing.

## Persistent mine system

Create one persistent state identity that follows the state through war, occupation, annexation, civil war, release, and peace settlement.

The one-time discovery grant stays with the original recipient.

Ongoing benefits follow the current controller.

Use a bounded mine registry and one reusable controller reconciliation effect.

Controller reconciliation must:

- remove the old contribution
- save the new controller
- preserve local values, quality, projects, damage, contracts, operating state, and evolution history
- recalculate core, compliance, resistance, supply, and occupation factors
- apply the new bounded contribution once
- rebuild valid decisions and missions
- clear stale selections and targets
- re-evaluate one surviving contract

Do not add a whole-world daily, weekly, or monthly scan.

Use a narrow state-control hook, event-driven registry refresh, or another proven repository pattern.

If no valid narrow route exists, report the blocker. Do not add an unauthorized scan.

## Visible values

Implement:

- Extraction Pressure, 0 to 100, primary
- Mine Development, 0 to 100
- Local Order, 0 to 100
- Revenue Legitimacy, 0 to 100

Centralize thresholds, gains, losses, caps, and duration bands in script constants.

Use event-owned scripted effects and triggers for repeated value changes.

Show the values in one decision-category header with concise scripted localisation, clear colors, icons, threshold context, and tooltips.

Keep concession exposure, illicit capture, deep excavation, private-security autonomy, foreign pressure, Gold Disease pressure, supernatural pressure, and sealed-depth integrity hidden as raw values.

Expose their visible consequences through stage, reports, decisions, and modifier text.

## Benefits and diminishing returns

Use one persistent mine ledger, exactly one active state-modifier presentation per mine, and one controller aggregate idea or dynamic modifier. Prefer one dynamic state modifier. If visible stage names or icons require separate variants, replace them mutually exclusively through one lifecycle helper.

Preserve the requested benefit families:

- ticking political power
- nationwide construction speed
- production efficiency
- military factory output
- civilian-factory benefit through a real supported HOI4 modifier or combination

Do not claim a literal civilian factory output modifier if the engine lacks one.

Calculate each mine contribution from quality, development, operating state, pressure policy, control quality, order, legitimacy, and evolution factors.

Apply diminishing national returns:

- first mine full marginal share
- second lower marginal share
- third small marginal share
- fourth and later minimal aggregate share
- hard country cap

Keep local state value and incidents meaningful for every mine.

Use one reusable aggregation helper and script constants.

## Baseline progression

Implement the complete ordinary lifecycle:

1. Discovery and claims
2. The rush
3. Physical development
4. Revenue settlement
5. Foreign concessions
6. Armed protection and raids
7. Consolidation, closure, collapse, recovery, and transfer

Ordinary phases are not evolutions.

Implement the incident families, policies, decisions, missions, costs, AI, cleanup, and outcomes in Parts 1 to 3 of the spec.

Use phase visibility so the category normally shows three to five primary decisions and one to three missions.

Six primary decisions is the hard maximum.

Use an ordinary category with a static category picture.

Do not create a dedicated scripted GUI.

## Decisions and missions

Implement every accepted action family in `029_riches_found_decision_mission_prompt.md`.

Use no more than four spendable cost types per action.

Use physical costs, route requirements, unit presence, supply, construction, equipment, manpower, fuel, trains, convoys, stability, war support, and revenue sacrifice where appropriate.

Do not default to political power or command power.

Keep command-power costs conservative.

Use icon-first cost localisation and custom trigger tooltips.

Implement all accepted missions with dynamic duration, real post-start objectives, success, partial success where mapped, failure, AI behavior, and cleanup.

Do not use passive stockpile checklist missions.

Use the selected-mine pattern for humans and direct full evaluation for AI.

Use a bounded selected-foreign-target pattern for concessions.

## Foreign concessions and interference

Build a plausible foreign target pool from access, distance, relations, faction, ideology, industry, strategic need, convoys, rival involvement, invitation, and mine condition.

Implement limited concession, exclusive concession, offtake, infrastructure-for-access, disclosure, public contract, buyout, compensated nationalization, uncompensated nationalization, renewal, expiry, dispute, transfer, and cleanup.

Allow one exclusive concession per mine.

Prevent contract and infrastructure duplication.

Implement covert and public foreign interference through bounded actors and evidence.

Do not make every major power pursue every mine.

## Security and raids

Implement mine police, private guards, army cordon, armed workers, escort, truce, clearing, and disarmament as distinct approaches.

Use actual supplied unit presence for army actions where the engine and repository pattern permit exact proof.

Target concrete assets and routes in raids.

Apply damage and deaths once.

Use Deaths and Condemnation for mass violence, forced labor, abuse, entombment, destroyed records, blocked inspection, and coverup.

Private guards can become a local authority and contribute to The Gilded Sovereignty.

## Evolutions

Register exactly three evolution stages:

1. The Resource Curse at Chaos Tier, 600+
2. Gold Disease at Totalen Chaos, 800+
3. Demons Beneath the Mine at World Collapse, 1,000+

Use paced dynamic MTTH with roughly 90-day base once full local conditions exist.

Chaos alone is insufficient.

Evolution III may begin at 1,000+ only while no terminal `world_end` state is active, unless an owning terminal route explicitly permits Event 029 continuation. Do not schedule new Event 029 evolution jobs after an incompatible terminal state begins.

Implement active-event and pre-fire evolved-opening behavior.

Respect individual evolution enable state.

Disabled evolutions cannot set recorded flags, hidden pressure, decisions, reports, modifiers, or late outcomes.

Record each evolution once through the shared evolution pipeline with actor context.

Do not record ordinary phases as evolutions.

Do not create Evolution IV or Evolution V rows.

Implement The Gilded Sovereignty as a late Resource Curse outcome.

Implement The Bottomless Account as a late Demons Beneath the Mine outcome.

These outcomes can have events, decisions, modifiers, achievements, and endings, but no fourth or fifth evolution record.

## Resource Curse

Implement corruption, patronage, theft, dependence, local resentment, contract capture, private authority, reform, and the staged controller idea.

Good management requires repeated audit, public terms, ownership disclosure, revenue settlement, diversification, and moderate pressure.

One click cannot cure the evolved state.

Implement The Gilded Sovereignty without a new country tag by default.

The enclave controls gates, payroll, transport, security, contracts, housing, and local authority through state and country mechanics.

Support revocation, buyout, shared sovereignty, representative board, violent nationalization, continued enclave rule, transfer, destruction, and permanent closure.

## Gold Disease

Implement a fictional obsessive greed syndrome.

Do not use biological outbreak, cure, vaccination, contamination, or bioweapon systems.

Move pressure only through specific workers, shipments, guards, contracts, and event routes.

Do not scan the world for spread.

Implement revenue sharing, controlled access, workforce replacement, military control, quarantine, temporary closure, sealed sections, confiscated material, violence, collapse, containment, and lasting susceptibility.

Deaths and atrocities must use shared systems.

Do not create a reward loop from population loss or purge.

## Demons Beneath the Mine

Implement a fictional supernatural force centered on valuation, possession, contracts, promises, and extraction.

Do not use Event 018 caves, Oth-Kesh, or The World Opens Below.

Do not copy or demonize a living mining or religious tradition.

Implement uncertain early signs, confirmed supernatural effects, staged controller condition, evacuation, permanent sealing, military purge, scientific help, religious help, occult help, controlled exploitation, and agreement.

Scientific help must not create Event 016 project history, Kruger ownership, free facilities, free units, or unsupported technology.

Ordinary contained supernatural pressure does not set a global world-threat source.

## Bottomless Account

Implement one active visible obligation at a time.

Allowed bounded payment families include material, political authority, public trust, industrial or territorial sacrifice, and explicit high-chaos human-cost choices with exact caps and shared consequence systems.

Unrelated deaths, genocide, bombing, disease, and military casualties cannot satisfy an obligation.

Implement close account, bind terms, pay in material, spend authority, predatory prosperity, breach, transfer, containment, and permanent closure.

Do not create a supernatural resource shop or world-end scenario.

## AI and probability

Implement route-specific AI using the complete named scenarios in `029_riches_found_ai_probability_scenarios.md`.

Use `chaosx_ai_probability_auditor` for every complex event option, decision weight, MTTH factor, random list, target weight, and policy choice.

The auditor is read-only.

Run baseline inspection and scenario evaluation before weighted patches.

Apply bounded changes through the parent or owning patch agent.

Run `hoi4.probability_compare` against the same scenario IDs after every weighted patch.

Distinguish exact, bounded, sampled, score-only, and unresolved evidence.

## Assets

Produce the complete asset inventory in `029_riches_found_asset_prompt.md`.

Use `chaosx_generated_event_art` for generated report art and the static category picture.

Use `chaosx_icon_artist` for decision, mission, category, idea, state-modifier, evolution, and achievement icons.

Use native ImageGen according to the asset skill.

Do not create portraits, flags, animation, audio, 3D models, unit counters, focus icons, or a super-event package.

Asset workers create source files, PNGs, DDS files, contact sheets, manifests, and handoffs.

The parent owns final `.gfx` wiring, gameplay references, docs, and validation.

Do not claim completion with placeholders or unwired assets.

## Achievements

Implement all seven achievements in `029_riches_found_achievement_prompt.md`.

Track historical route state and disqualifiers.

Create completed, grey, and not-eligible 64x64 icon triplets.

Group the achievements in the single root Chaos Redux achievement registry.

Do not reduce hard achievements to final-state checks.

## Event log and Event Details

Wire:

- visible event name
- debug name
- history actor
- Event Details premise
- live weight and `N/A`
- repeatable fired count
- three evolution previews
- three evolution log names and actor context
- enabled and disabled behavior

Main Evolutions and selected History details show real sequence, date, event, evolution, tier, stage, actor, and enabled state.

Event Details previews show catalog information without fake history metadata.

Gilded Sovereignty and Bottomless Account do not appear as evolution rows.

## Localisation

Write finished in-world text for every event, report, decision, mission, cost, requirement, modifier, evolution, Event Details row, log selector, achievement, and tooltip.

Follow the writing direction in Part 6.

Do not paste planning language into localisation.

Do not use implementation-history wording, raw trigger text, hidden variables, generic crisis templates, staccato prose, em dashes, or semicolons.

Gold Disease must not be called a virus.

Supernatural text must not use invented quotes or copied living religious material.

Use `chaosx_localisation_auditor` before completion.

## Shared systems

Integrate:

- Deaths
- Condemnation
- Chaos history
- controller transfer
- Event 013 only through valid exact-state API calls
- Event 016 only through bounded assistance
- Event 018 exclusions
- Event 019 only if a new custom combat unit is later approved

Do not duplicate shared systems.

## Documentation and catalog

Create or update the Event 029 documentation under the current repository pattern.

Document player-facing behavior, decisions, values, evolutions, late outcomes, assets, achievements, AI, controller transfer, interactions, and tuning locations.

Update only `docs/spreadsheets/chaos_redux_events_catalog.xlsx` through `chaosx_spreadsheet_doc_worker` after final in-game wording exists.

Then run `python .tools/export_event_catalog_csv.py`.

Do not edit CSV exports directly.

Keep catalog detail and evolution detail aligned with Event Details localisation.

## Audits

Before completion claim, use:

- `chaosx_decision_mission_auditor`
- `chaosx_ai_probability_auditor`
- `chaosx_localisation_auditor`
- `chaosx_event_completion_auditor`
- asset subagents and parent review
- `chaosx_spreadsheet_doc_worker`

Use `chaosx_improvement_loop_planner` only if a broad design gap remains after this accepted specification has been implemented or formally amended.

Do not stack another unresolved improvement plan on top of this one.

## Validation

Run every scenario in `029_riches_found_acceptance_criteria.md` that can be validated through source, MCP, and repository tooling.

Prepare the live-test cases for the user.

Do not claim in-game verification unless it was actually performed under an explicitly invoked live-test workflow.

The completion report must list files, identifiers, decisions, missions, constants, AI evidence, transfer behavior, evolutions, shared-system calls, assets, achievements, docs, workbook updates, blockers, and every simplification or omission.

## Completion and commit

Event 029 is complete only when every accepted baseline phase, decision family, mission, controller-transfer route, evolution, late outcome, AI behavior, asset, achievement, log surface, document, and catalog field is implemented and aligned.

If any required item is missing, report the goal as incomplete.

After reviewing the final diff and completing all required audits, create one focused Git commit containing only Event 029 and directly required shared-system changes.
