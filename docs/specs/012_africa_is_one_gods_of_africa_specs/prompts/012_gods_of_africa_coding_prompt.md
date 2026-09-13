# Coding prompt: Gods of Africa under Event 012

Implement the accepted Gods of Africa specification as a persistent subsystem owned by Event `012`, Africa Is One.

## Hard ownership rules

- Gods of Africa belongs to Event 012.
- Event `070` remains available for another idea.
- Do not register Gods of Africa as a normal event, major event, repeatable event, fire-once event, or separate cluster member.
- Use the Event 012 namespace and authoritative African unifier state.
- Do not duplicate Event 012 continent control, claimant, establishment, evolution, or victory ledgers.

## Required source reading

Before editing, read in full:

- `AGENTS.md`
- every relevant project skill
- all files under the accepted Gods of Africa spec package
- all Event 012 specs, plans, docs, handoffs, events, decisions, focuses, ideas, AI, localisation, assets, scenario, and catalog references
- every live Event 070 reference
- required offline Paradox wiki pages
- installed vanilla documentation and direct vanilla precedents

Use the live source as authority for exact identifiers and syntax.

## Mandatory preflight

1. Use `chaosx_repo_explorer` with a context-complete prompt to map the Event 012 and Event 070 surfaces.
2. Use `hoi4.event_inspect` and `hoi4.event_render` on Event 012.
3. Inspect the authoritative XLSX catalog and current exported CSVs.
4. Identify the exact African unifier target, establishment proof, evolution state, secured-continent trigger, and SCN-011 launch path.
5. Record any conflict between the accepted spec and the live Event 012 implementation before patching.

## Core mechanic

Activate only when:

- Africa Is One has fired
- the African unifier exists
- Evolution I is active and enabled
- about 180 days have passed since establishment
- Event 012 has not already reached its final settlement

Register every valid major and player-controlled country. Exclude the African unifier. Keep registered surviving countries even if they later lose major status. Add bounded onboarding for later majors and later player-controlled countries. Do not add an unrestricted all-country daily, weekly, or monthly on-action.

Expose exactly two public values:

- Gods of Africa Strength, global and shared
- Wrath of the Gods, separate for every participant

Keep all friendship, capacity, need, offense, compliance, and history calculations hidden.

## Strength

Implement Strength on a clamped `0 to 100` scale with five cached bands.

Derive it dynamically from:

- African military readiness and relative power
- industry, fuel, supply, trains, convoys, and transport
- continental control and Event 012 strategic positions
- air, naval, technological, intelligence, and diplomatic reach
- stability, surrender condition, capital, and internal coherence
- Chaos as a bounded amplifier
- Event 012 evolutions and accepted capability routes

A weak Africa at high Chaos must remain limited. Ordinary changes should be smoothed. Major defeat must lower Strength quickly.

## Wrath

Implement Wrath on a clamped `0 to 100` scale with separate participant records.

Use one central transaction helper and reason constants. Add active floors for war, occupation of African core territory, broken agreements, permanent defiance, and recent extreme offenses.

Wrath rises from refusal, failure, war, occupation, aid to African enemies, broken agreements, and direct hostility. It falls from compliance, voluntary aid, returned territory, support in African wars, honored agreements, and reconciliation.

One country action must never alter another country's Wrath.

## Demand contracts

Each participant can have only one ordinary active demand.

Create a frozen contract with:

- sequence identity
- family
- amount or diplomatic condition
- burden band
- deadline
- payment progress
- valid substitute set
- extension state
- current generation proof

Build an African need profile and participant capacity profile before selecting the demand.

Demand families must cover the accepted Evolution I, II, and III design where engine support exists. Include real material transfers, industrial support, recognition, territory return, access, ending aid to enemies, and later alignment or faction concessions.

Do not request a family the target cannot meaningfully provide. Protect operating reserves. Use capacity-scaled amounts and readable rounding. Ensure no-DLC parity for the core loop.

## Participant actions

Implement a phased decision category with:

- fulfill
- propose up to three valid substitutes
- request one normal extension
- refuse this demand
- permanently defy the Gods

Show no more than five primary actions in the active-demand phase. A gameplay action may use no more than four spendable cost types.

Add voluntary aid only during a real African need and block farming.

Defiance stops ordinary demands, sets a high Wrath floor, closes the normal Favored route, and opens active defensive preparation. It does not stop punishment or African hostility.

Add a rare costly reconciliation route with war, territory, political, and reparations requirements. Reconciliation returns the country as distrusted and preserves a prior-defiance mark.

## Africa-side gameplay

Add an African-unifier category with:

- current Strength
- doctrine and current need priority
- grouped foreign reports
- selected-target participant flow
- grant leniency
- mark a proven priority offender
- protect a reliable country at real African cost
- issue a public pardon after valid settlement
- escalate a proven offense inside the normal ceiling

Do not let the African player enter arbitrary demand amounts or choose invalid families.

## Punishment

Calculate desired punishment separately from capability.

Desired punishment uses Wrath, failure history, offense severity, failed demand severity, Chaos, and current hostility.

Maximum punishment uses Strength, real African capability, and Event 012 evolution access.

Apply the lower valid tier after target condition and cooldown checks.

Hard rules:

- low Strength caps at Tier I
- a first ordinary refusal cannot cause Tier IV or Tier V
- Tier V requires extreme Strength, very high Wrath, high Chaos, repeated serious failure or a major offense, Evolution III, a stable African unifier, and no recent extreme cooldown
- track recent punishment families and avoid unjustified repetition
- never reroll a committed punishment after reload

Use `call_natural_disaster` for Event 013 disaster sequences. Inspect its result and fail closed. Use `apply_exact_state_civilian_population_loss` for civilian population loss, preserve a minimum population floor, and log Deaths once. Do not duplicate generic Chaos sources.

## Protection and final outcomes

Reliable participants can receive African equipment, fuel, expeditionary forces, guarantees, reconstruction, disaster mitigation, famine or migration help, favorable trade, and longer demand patience. Every benefit must scale to Africa's real capacity.

When Africa secures the continent through the authoritative Event 012 proof:

- stop new demands
- cancel active contracts
- evaluate full hidden history
- issue Favored, Respected, Distrusted, or Enemy outcomes
- feed the result into World Is One participation

One last payment cannot erase war, occupation, defiance, or broken agreements.

## Focus integration

Add the accepted Event 012 overlay branch after inspecting the live tree.

Required route groups:

- preparation and proclamation
- Reciprocal Covenant
- Sovereign Exaction
- Provision
- Oaths
- Protection
- Judgment
- Evolution II expansion
- Evolution III expansion
- continental settlement

Use varied rewards and real decision unlocks. Render and audit the complete tree. Do not create a separate Gods tree or a full focus inlay for the two values.

## Presentation and assets

Use the normal decision category and compact two-value display by default.

A full scripted GUI requires an explicit parent decision after proving the normal surface insufficient. If accepted, route it to `chaosx_event_ui_worker` and complete mandatory MCP inspect, render, rewrite, and comparison evidence.

Register stable sprites before asset production. Route generated scene art and category art to `chaosx_generated_event_art`, icons to `chaosx_icon_artist`, super-event quote research to `chaosx_super_event_text_researcher`, and music to `chaosx_super_event_audio_researcher`.

The doctrine is fictional. Do not create a universal historical African pantheon, fake proverb, decontextualized sacred-symbol collage, stereotyped visual, or generic tribal music loop.

## Super-event

Implement one optional credibility super-event if the live Event 012 presentation audit confirms it is justified.

It fires once when the active system first reaches the accepted global-reach Strength threshold. Weak activation uses normal news and waits.

Complete unique image, sourced quote, researched button reference if used, unique licensed musical recording, final WAV, sound definitions, volume wrappers, settings-aware playback, scripted localisation, docs, and workbook alignment.

## AI and probability

Run the full named scenario contract from `quality/012_gods_of_africa_ai_probability_scenarios.md`.

Every weighted participant response, target selector, demand family, demand band, substitute, extension, punishment family, protection target, and focus route requires baseline inspection, owner patching, and comparison with the same scenarios.

Do not claim exact probabilities from incomplete pools.

## Documentation and catalog

Update Event 012 docs, decisions, focus documentation, super-event research, audio catalog, asset provenance, Event Details, logs, and authoritative XLSX.

Remove the old Gods assignment from Event 070 and leave ID 070 available.

Run `python .tools/export_event_catalog_csv.py` after the workbook save. Never edit the CSV exports directly.

## Required audits

Before completion, run:

- scripted-system architecture review
- decision and mission audit
- focus audit
- AI probability audit and compare
- localisation audit
- African-unifier country package audit
- event completion audit
- spreadsheet worker
- improvement-loop planner after a meaningful implementation tranche

Resolve or explicitly queue every handoff. Do not claim completion while an accepted addendum remains unreported.

## Completion report

Report:

- exact files and identifiers changed
- Event 012 integration points
- Event 070 disposition
- participant and owner data contracts
- demand family coverage
- punishment tier coverage
- protection and ending coverage
- AI probability evidence
- focus route coverage
- assets and super-event evidence
- workbook and export results
- meaningful validation
- every simplification, blocker, placeholder, skipped audit, and unresolved plan

Do not substitute a smaller system without explicit approval.
